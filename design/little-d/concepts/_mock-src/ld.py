#!/usr/bin/env python3
"""Little D mock generator: shared layout, OpenSCAD scene builder, renderer, post-processing.

Coordinates as concepts/common-how-it-works.md: origin front-left outer corner, x right, y away from player,
z up from the outside of the bottom. mm.
"""
import math, os, subprocess, random
import numpy as np
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- layout (common §2)
W, D = 298.0, 180.0
PZ = 24.0          # control panel top: eng E-L2 answer (50 mm CDS-5076, 7.6 deep) gives 22.7-24.2; keys flush (R4)
KEY_Z = 17.5       # key surface: Choc V2 silent + 3 mm pressed-on top (eng velocity-and-keys-v2)
SHARP_Z = 19.5     # rear-row sharps, +2 mm
LIP_Z = 22.0
KNOB_H = 10.45     # Tayda KN1250 fluted, A-2810 (cream)
KNOB_D = 14.86
HERO_H = 12.15     # Tayda 1083 serrated pointer, A-5582 (cream)
HERO_D = 20.8
KNOB_GAP = 0.5     # knob skirt above panel

ROWS = {"F": 104.0, "M": 127.0, "B": 150.0}
# Round 2 layout (director R2): knob-to-knob pitch >= 20 mm; IV's played row CUTOFF->EMPHASIS 25, EMPHASIS->AMOUNT 24
# (CUTOFF gap 7.2, others 9.1). Walls/section breaks: 3 mm air on a toggle side, 7 mm on a knob side; 7.5 mm to the rim.
SECTIONS = [  # numeral, name, x0, x1 (label/card extents, between walls)
    ("I", "CONTROLLERS", 5, 38),
    ("II", "OSCILLATORS", 45, 117.5),
    ("III", "MIXER", 124.5, 169.4),
    ("IV", "MODIFIERS", 176.4, 261),
    ("V", "OUTPUT", 268, 293),
]
GAP_CENTRES = [3.0, 41.5, 121.0, 172.9, 264.5, 295.0]
C_I, C_TG1 = 18.0, 34.0
C_R, C_F, C_W, C_TG2 = 57.5, 77.5, 97.5, 113.5
C_O, C_N = 137.0, 157.0
C_CUT, C_EMP, C_AMT, C_TG4 = 192.0, 217.0, 241.0, 257.0
C_VOL = 280.5

# knobs: (label, x, y, kind, midi)   kind: std | hero | rot
KNOBS = [
    ("TUNE", C_I, ROWS["F"], "std", True),
    ("GLIDE", C_I, ROWS["M"], "std", True),
    ("MOD MIX", C_I, ROWS["B"], "std", False),
    ("RANGE 1", C_R, ROWS["F"], "std", True),
    ("WAVE 1", C_W, ROWS["F"], "rot", False),
    ("RANGE 2", C_R, ROWS["M"], "std", True),
    ("FREQ 2", C_F, ROWS["M"], "std", True),
    ("WAVE 2", C_W, ROWS["M"], "rot", False),
    ("RANGE 3", C_R, ROWS["B"], "std", True),
    ("FREQ 3", C_F, ROWS["B"], "std", True),
    ("WAVE 3", C_W, ROWS["B"], "rot", False),
    ("OSC 1", C_O, ROWS["F"], "std", False),
    ("OSC 2", C_O, ROWS["M"], "std", False),
    ("NOISE/EXT", C_N, ROWS["M"], "std", False),
    ("OSC 3", C_O, ROWS["B"], "std", False),
    ("CUTOFF", C_CUT, ROWS["F"], "hero", True),
    ("EMPHASIS", C_EMP, ROWS["F"], "std", False),
    ("CONTOUR AMT", C_AMT, ROWS["F"], "std", False),
    ("F. ATTACK", C_CUT, ROWS["M"], "std", False),
    ("F. DECAY", C_EMP, ROWS["M"], "std", False),
    ("F. SUSTAIN", C_AMT, ROWS["M"], "std", False),
    ("L. ATTACK", C_CUT, ROWS["B"], "std", False),
    ("L. DECAY", C_EMP, ROWS["B"], "std", False),
    ("L. SUSTAIN", C_AMT, ROWS["B"], "std", False),
    ("VOLUME", C_VOL, ROWS["F"], "std", False),
]
MOD_DIAL = ("MOD", 14, 46)
STICK = (14, 22)
# toggles: (label, x, y, positions)
TOGGLES = [
    ("OSC MOD", C_TG1, ROWS["M"], 2),
    ("FILTER MOD", C_TG1, ROWS["B"], 2),
    ("OSC 3 CTRL", C_TG2, ROWS["B"], 2),
    ("SOURCE", C_N, ROWS["F"], 3),
    ("KBD CTRL", C_TG4, ROWS["F"], 3),
    ("DECAY", C_TG4, ROWS["B"], 2),
    ("VELOCITY", C_TG4, ROWS["M"], 3),      # owner 2026-11-12: velocity -> LOUD / BOTH / FILT, by a switch
]
STATUS_LED = (C_VOL, 127)
NIC_LED = (205.5, 93)    # "not in control" light by CUTOFF (H7), in the 7 mm gap CUTOFF|EMPHASIS

# knob pointer angles (deg from 12 o'clock, clockwise) for a lived-in patch
random.seed(7)
ANG = {k[0]: random.choice([-120, -90, -60, -30, 0, 15, 30, 60, 90, 120]) for k in KNOBS}
ANG["CUTOFF"] = 40; ANG["MOD"] = -60

def white_keys():
    return [(25 + i * 18, i) for i in range(15)]

def sharp_keys():
    out = []
    pat = [1, 1, 0, 1, 1, 1, 0]
    for i in range(14):
        if pat[i % 7]:
            out.append(25 + (i + 1) * 18)
    return out

# ---------------------------------------------------------------- SCAD primitives
def c(col):
    return f'color("{col}")'

def box(x0, y0, z0, x1, y1, z1, col):
    return f'{c(col)} translate([{x0:.3f},{y0:.3f},{z0:.3f}]) cube([{x1-x0:.3f},{y1-y0:.3f},{z1-z0:.3f}]);\n'

def cyl(x, y, z0, h, d, col, fn=48, d2=None):
    d2 = d if d2 is None else d2
    return f'{c(col)} translate([{x:.3f},{y:.3f},{z0:.3f}]) cylinder(h={h:.3f}, d1={d:.3f}, d2={d2:.3f}, $fn={fn});\n'

def txt(x, y, z, s, size, col, font="Inter:style=SemiBold", halign="center", valign="center", rot=0, h=0.12):
    s = s.replace('"', '\\"')
    return (f'{c(col)} translate([{x:.3f},{y:.3f},{z:.3f}]) rotate([0,0,{rot}]) linear_extrude({h}) '
            f'text("{s}", size={size}, font="{font}", halign="{halign}", valign="{valign}", $fn=24);\n')

def vtxt(x, y, z, s, size, col, font="Inter:style=SemiBold", halign="center", valign="center", h=0.15):
    """text standing on an XZ face, readable from the front (facing -y)."""
    s = s.replace('"', '\\"')
    return (f'{c(col)} translate([{x:.3f},{y:.3f},{z:.3f}]) rotate([90,0,0]) linear_extrude({h}) '
            f'text("{s}", size={size}, font="{font}", halign="{halign}", valign="{valign}", $fn=24);\n')

def knob_std(x, y, z, ang, col="#ece2c6", line="#2a2622"):
    pts = []
    n = 18
    for i in range(n * 4):
        a = 2 * math.pi * i / (n * 4)
        r = KNOB_D / 2 - 0.45 * (0.5 + 0.5 * math.cos(n * a))
        pts.append(f"[{r*math.cos(a):.3f},{r*math.sin(a):.3f}]")
    poly = ",".join(pts)
    zt = z + KNOB_H
    a = math.radians(90 - ang)
    s = f'{c(col)} translate([{x:.3f},{y:.3f},{z:.3f}]) linear_extrude(height={KNOB_H}, scale=0.9) polygon([{poly}]);\n'
    s += f'{c(col)} translate([{x:.3f},{y:.3f},{zt-0.6:.3f}]) cylinder(h=0.6, d1={KNOB_D*0.9:.2f}, d2={KNOB_D*0.84:.2f}, $fn=48);\n'
    # pointer line (top), inked
    s += (f'{c(line)} translate([{x:.3f},{y:.3f},{zt:.3f}]) rotate([0,0,{math.degrees(a):.1f}]) '
          f'translate([{KNOB_D*0.12:.2f},-0.45,0]) cube([{KNOB_D*0.3:.2f},0.9,0.08]);\n')
    return s

def knob_hero(x, y, z, ang, col="#ece2c6", line="#c4512e"):
    pts = []
    n = 36
    for i in range(n * 2):
        a = 2 * math.pi * i / (n * 2)
        r = HERO_D / 2 - (0.5 if i % 2 else 0.0)
        pts.append(f"[{r*math.cos(a):.3f},{r*math.sin(a):.3f}]")
    poly = ",".join(pts)
    zt = z + HERO_H
    a = math.radians(90 - ang)
    s = f'{c(col)} translate([{x:.3f},{y:.3f},{z:.3f}]) linear_extrude(height={HERO_H-1.2}, scale=0.95) polygon([{poly}]);\n'
    s += f'{c(col)} translate([{x:.3f},{y:.3f},{z+HERO_H-1.2:.3f}]) cylinder(h=1.2, d1={HERO_D*0.95:.2f}, d2={HERO_D*0.82:.2f}, $fn=72);\n'
    s += (f'{c(line)} translate([{x:.3f},{y:.3f},{zt:.3f}]) rotate([0,0,{math.degrees(a):.1f}]) '
          f'translate([{HERO_D*0.08:.2f},-0.6,0]) cube([{HERO_D*0.33:.2f},1.2,0.08]);\n')
    return s

def toggle(x, y, z, col="#b9bcbf"):
    s = cyl(x, y, z, 1.8, 6.0, "#9a9da1", fn=6)
    s += cyl(x, y, z + 1.8, 1.0, 4.5, col, fn=24)
    s += f'{c(col)} translate([{x:.3f},{y:.3f},{z+2.5:.3f}]) rotate([-18,0,0]) cylinder(h=8, d1=2.6, d2=2.1, $fn=16);\n'
    return s

def led(x, y, z, col="#ffb347"):
    return cyl(x, y, z, 0.6, 3.2, col, fn=24) + cyl(x, y, z, 0.3, 5.0, "#3a3631", fn=24)

def stick(x, y, z, col="#2f2f33"):
    s = cyl(x, y, z, 4, 3.0, "#555", fn=16)
    s += f'{c(col)} translate([{x:.3f},{y:.3f},{z+5:.3f}]) scale([1,1,0.55]) sphere(d=11, $fn=40);\n'
    s += cyl(x, y, z + 3, 2.2, 10.5, col, fn=40)
    return s

def keys(white="#f7f4ee", sharp="#2a2826", style="short", plate="#2e5f48", wz=24.0, sdz=2.0, y0=0.0, plate_z=None):
    """style 'short': eng S1 tops (whites 30 x 17.2 front row y 5-35, sharps 16 x 14 rear row y 37-52), no rocking.
    style 'piano': S2 full-length piano tops on Choc V2 stabilisers (+$29.85). wz = white key surface (R4: ~ panel)."""
    s = ""
    pz_ = (wz - 6.5) if plate_z is None else plate_z
    if style == "short":
        for x0, i in white_keys():
            s += box(x0 + 0.4, y0 + 5, wz - 3, x0 + 17.6, y0 + 35, wz, white)
        for xc in sharp_keys():
            s += box(xc - 7.0, y0 + 37.5, wz + sdz - 3, xc + 7.0, y0 + 51.5, wz + sdz, sharp)
        s += box(25, y0 + 3, pz_ - 1.5, 295, y0 + 52, pz_, plate)
    else:
        for x0, i in white_keys():
            s += box(x0 + 0.3, y0 + 3.2, wz - 3, x0 + 17.7, y0 + 52, wz, white)
        for xc in sharp_keys():
            s += box(xc - 5.0, y0 + 22, wz, xc + 5.0, y0 + 51, wz + 2.8, sharp)
        s += box(25, y0 + 3, pz_ - 1.5, 295, y0 + 52, pz_, plate)
    return s

def ticks(x, y, z, r, n_or_angles, col, length=1.4, width=0.45, span=300):
    s = ""
    if isinstance(n_or_angles, int):
        n = n_or_angles
        angs = [-span / 2 + span * i / (n - 1) for i in range(n)]
    else:
        angs = n_or_angles
    for a in angs:
        s += (f'{c(col)} translate([{x:.3f},{y:.3f},{z:.3f}]) rotate([0,0,{-a+90:.2f}]) '
              f'translate([{r:.2f},{-width/2:.2f},0]) cube([{length:.2f},{width:.2f},0.1]);\n')
    return s

def panel_controls(pz=PZ, knob_col="#ece2c6", eng="#f1e6d0", eng_font="Inter:style=SemiBold",
                   label=True, scales=True, midi_col=None, hero_col=None, zmap=None, dy=0.0, ptr="#2a2622",
                   leds=True, toggles=True, flip_front=None, knob_fn=None):
    """All knobs, toggles, LEDs and machine marks on a panel whose top is pz (or zmap(x)), shifted by dy in y."""
    s = ""
    zf = zmap or (lambda x: pz)
    midi_col = midi_col or eng
    for lab, x, y, kind, midi in KNOBS:
        y = y + dy
        p = zf(x)
        z = p + KNOB_GAP
        if kind == "hero":
            s += knob_hero(x, y, z, ANG[lab], col=hero_col or knob_col)
            if scales:
                s += ticks(x, y, p, HERO_D / 2 + 1.6, 11, eng, length=1.8)
        else:
            s += (knob_fn(x, y, z, ANG[lab]) if knob_fn else knob_std(x, y, z, ANG[lab], col=knob_col, line=ptr))
            if scales:
                if lab.startswith("RANGE"):
                    s += ticks(x, y, p, KNOB_D / 2 + 1.0, [-125, -75, -25, 25, 75, 125], eng, length=1.8, width=0.6)
                elif kind == "rot":
                    s += ticks(x, y, p, KNOB_D / 2 + 1.0, [-125, -75, -25, 25, 75, 125], eng, length=1.2, width=0.45)
                else:
                    s += ticks(x, y, p, KNOB_D / 2 + 1.0, 7, eng, length=1.0, width=0.35)
        if label:
            short = lab.replace("F. ", "").replace("L. ", "")
            short = {"RANGE 1": "RANGE", "RANGE 2": "RANGE", "RANGE 3": "RANGE", "WAVE 1": "WAVE", "WAVE 2": "WAVE",
                     "WAVE 3": "WAVE", "FREQ 2": "FREQ", "FREQ 3": "FREQ", "CONTOUR AMT": "AMOUNT"}.get(short, short)
            dd = -(HERO_D / 2 + 3.6) if kind == "hero" else -(KNOB_D / 2 + 3.4)
            if flip_front and abs((y - dy) - ROWS["F"]) < 0.1 and any(a - 8 <= x <= b + 8 for a, b in flip_front[1]):
                dd = flip_front[0] - y
            s += txt(x, y + dd, p, short, 1.9, eng, font=eng_font)
        if midi:
            r = (HERO_D if kind == "hero" else KNOB_D) / 2 + 3.2
            s += cyl(x + r * 0.72, y + r * 0.72, p, 0.1, 1.1, midi_col, fn=12)
    if toggles:
        for lab, x, y, n in TOGGLES:
            y = y + dy
            s += toggle(x, y, zf(x))
            if label:
                s += txt(x, y - 9.2, zf(x), lab, 1.6, eng, font=eng_font)
    if leds:
        s += led(STATUS_LED[0], STATUS_LED[1] + dy, zf(STATUS_LED[0]))
        if label:
            s += txt(STATUS_LED[0], STATUS_LED[1] + dy - 6, zf(STATUS_LED[0]), "STATUS", 1.6, eng, font=eng_font)
        s += led(NIC_LED[0], NIC_LED[1] + dy, zf(NIC_LED[0]), col="#e9dfc8")
    return s

# ---------------------------------------------------------------- render
def render(scad_text, name, eye, center, size=(3000, 2000), bg_note=True):
    path = os.path.join(OUT, name + ".scad")
    with open(path, "w") as f:
        f.write("$fa=4; $fs=0.4;\n" + scad_text)
    png = os.path.join(OUT, name + "_raw.png")
    cam = ",".join(f"{v:.2f}" for v in (*eye, *center))
    cmd = ["xvfb-run", "-a", "-s", "-screen 0 6400x4400x24", "openscad", "-o", png,
           f"--imgsize={size[0]},{size[1]}", f"--camera={cam}", "--projection=p", "--colorscheme=Tomorrow", path]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    if not os.path.exists(png) or os.path.getsize(png) == 0:
        raise RuntimeError(r.stderr[-2000:])
    return png

def _noise(h, w, scale, seed):
    rng = np.random.default_rng(seed)
    small = rng.random((max(2, h // scale + 2), max(2, w // scale + 2))).astype(np.float32)
    img = Image.fromarray((small * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)
    return np.asarray(img).astype(np.float32) / 255.0

def finish(raw_png, shadow_png, out_png, grain_angle_deg=-18, paper=(243, 239, 232), down=2,
           grain_classes=("ply",), extra=None, crop=True):
    im = np.asarray(Image.open(raw_png).convert("RGB")).astype(np.float32)
    h, w, _ = im.shape
    bg = im[2, 2].copy()
    isbg = np.all(np.abs(im - bg) < 3, axis=2)
    r, g, b = im[..., 0] / 255, im[..., 1] / 255, im[..., 2] / 255
    mx = np.maximum(np.maximum(r, g), b); mn = np.minimum(np.minimum(r, g), b)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    hue = np.zeros_like(mx)
    d = np.maximum(mx - mn, 1e-6)
    hue = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60
    # wood: grain
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    th = math.radians(grain_angle_deg)
    v = -xx * math.sin(th) + yy * math.cos(th)
    u = xx * math.cos(th) + yy * math.sin(th)
    warp = _noise(h, w, 220, 1) * 60 + _noise(h, w, 40, 2) * 6
    grain = 0.5 + 0.5 * np.sin((v + warp) * 0.9 + np.sin(u * 0.004) * 3)
    grain = grain ** 4 * 0.6 + _noise(h, w, 2, 9) * 0.4
    fine = _noise(h, w, 3, 3)
    wood = (~isbg) & (hue > 18) & (hue < 48) & (sat > 0.3) & (mx > 0.35)
    cedar = (~isbg) & (hue >= 5) & (hue <= 22) & (sat > 0.45) & (mx > 0.2) & (mx < 0.75)
    felt = (~isbg) & (sat < 0.07) & (mx > 0.28) & (mx < 0.7)
    out = im.copy()
    # chroma-keyed paper (rendered pure green): re-light as paper so vertical faces aren't muddy
    key = (~isbg) & (hue > 100) & (hue < 140) & (sat > 0.8)
    if key.any():
        sh = g / max(float(g[key].max()), 1e-6)
        paper_c = np.array([243, 234, 212], np.float32)
        lit = np.clip(0.80 + 0.22 * sh, 0, 1.05)[..., None] * paper_c[None, None, :]
        tex = (0.97 + 0.03 * _noise(h, w, 2, 11))[..., None]
        out = np.where(key[..., None], lit * tex, out)
    if "ply" in grain_classes:
        m = wood[..., None]
        out = np.where(m, out * (0.93 + 0.07 * grain[..., None] + 0.03 * fine[..., None]), out)
    if "cedar" in grain_classes:
        m = cedar[..., None]
        out = np.where(m, out * (0.86 + 0.14 * grain[..., None] + 0.04 * fine[..., None]), out)
    if "walnut" in grain_classes:   # oiled walnut: darker figure, stronger contrast than birch ply
        wal = (~isbg) & (hue > 12) & (hue < 38) & (sat > 0.45) & (mx > 0.12) & (mx < 0.6)
        wv = _noise(h, w, 400, 22) * 40 + _noise(h, w, 120, 23) * 6
        ph = (v + wv) * 0.22
        g2 = (0.55 * (0.5 + 0.5 * np.sin(ph)) + 0.45 * (0.5 + 0.5 * np.sin(ph * 2.7 + 1.3))) ** 2.2
        streak = _noise(h, w, 6, 24)
        g2 = g2 * 0.8 + 0.2 * streak
        fig = _noise(h, w, 160, 21)
        out = np.where(wal[..., None], out * (0.80 + 0.26 * g2[..., None] + 0.08 * fig[..., None] + 0.03 * fine[..., None]), out)
    if "pei" in grain_classes:   # textured-PEI first-layer face on printed parts: fine satin speckle
        pei = (~isbg) & (hue > 25) & (hue < 60) & (sat > 0.06) & (sat < 0.3) & (mx > 0.6)
        sp = _noise(h, w, 1, 12) * 0.7 + _noise(h, w, 2, 13) * 0.3
        out = np.where(pei[..., None], out * (0.955 + 0.075 * sp[..., None]), out)
    if "felt" in grain_classes:
        speck = _noise(h, w, 1, 4) * 0.6 + _noise(h, w, 2, 5) * 0.4
        mott = _noise(h, w, 60, 6)
        m = felt[..., None]
        out = np.where(m, out * (0.88 + 0.16 * speck[..., None] + 0.06 * mott[..., None]), out)
    # shadow
    paper_a = np.array(paper, np.float32)
    shadow = np.zeros((h, w), np.float32)
    if shadow_png:
        sim = Image.open(shadow_png).convert("L")
        sarr = np.asarray(sim).astype(np.float32)
        sbg = sarr[2, 2]
        mask = (np.abs(sarr - sbg) > 3).astype(np.float32)
        ms = Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(radius=w / 90))
        shadow = np.asarray(ms).astype(np.float32) / 255.0 * 0.32
        ms2 = Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(radius=w / 400))
        shadow = np.maximum(shadow, np.asarray(ms2).astype(np.float32) / 255.0 * 0.38)
    bgcol = paper_a[None, None, :] * (1 - shadow[..., None])
    out = np.where(isbg[..., None], bgcol, out)
    out = np.clip(out, 0, 255).astype(np.uint8)
    img = Image.fromarray(out)
    # auto-crop to object + shadow
    obj = (~isbg) | (shadow > 0.02)
    ys, xs = np.where(obj)
    if len(xs) and crop:
        m = int(w * 0.03)
        img = img.crop((max(0, xs.min() - m), max(0, ys.min() - m), min(w, xs.max() + m), min(h, ys.max() + m)))
        w, h = img.size
    if down > 1:
        img = img.resize((w // down, h // down), Image.LANCZOS)
    img.save(out_png)
    return out_png

def eye_from(center, az_deg, el_deg, dist):
    az, el = math.radians(az_deg), math.radians(el_deg)
    return (center[0] + dist * math.cos(el) * math.sin(az),
            center[1] - dist * math.cos(el) * math.cos(az),
            center[2] + dist * math.sin(el))

def shot(scene, footprint, name, az=-32, el=38, dist=1050, center=(149, 92, 14), size=(3200, 2200),
         grain_angle=-14, grain_classes=("ply",)):
    eye = eye_from(center, az, el, dist)
    raw = render(scene, name, eye, center, size)
    sh = render(footprint, name + "_sh", eye, center, size)
    return finish(raw, sh, os.path.join(OUT, name + ".png"), grain_angle_deg=grain_angle, grain_classes=grain_classes)


# ---------------------------------------------------------------- orthographic top view for the real-size sheets
def shot_top(scene, name, x0, y0, x1, y1, px_per_mm=12, grain_classes=("ply",), grain_angle=0):
    """Render straight down, orthographic. Two marker cubes at (x0,y0) and (x1,y1) fix the scale; output is cropped
    exactly to that world rectangle, so it can be placed on a sheet at 1:1 with no guessing."""
    mk = (box(x0 - 2, y0 - 2, -5, x0, y0, -4.9, "#ff00ff") + box(x1, y1, -5, x1 + 2, y1 + 2, -4.9, "#ff00ff"))
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    wmm, hmm = (x1 - x0) + 30, (y1 - y0) + 30
    size = (int(wmm * px_per_mm * 1.15), int(hmm * px_per_mm * 1.15))
    path = os.path.join(OUT, name + ".scad")
    with open(path, "w") as f:
        f.write("$fa=4; $fs=0.4;\n" + scene + mk)
    raw = os.path.join(OUT, name + "_raw.png")
    dist = max(wmm, hmm) * 2.2
    cam = f"{cx:.2f},{cy-0.001:.3f},{dist:.1f},{cx:.2f},{cy:.2f},0"
    cmd = ["xvfb-run", "-a", "-s", "-screen 0 6400x4400x24", "openscad", "-o", raw, f"--imgsize={size[0]},{size[1]}",
           f"--camera={cam}", "--projection=o", "--colorscheme=Tomorrow", "--viewall", path]
    cmd.remove("--viewall")
    subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    im = np.asarray(Image.open(raw).convert("RGB")).astype(np.float32)
    mag = (im[..., 0] > 180) & (im[..., 1] < 100) & (im[..., 2] > 180) & (np.abs(im[..., 0] - im[..., 2]) < 40)
    ys, xs = np.where(mag)
    h, w, _ = im.shape
    left = xs < w / 2
    ax0, ay1 = xs[left].max() + 1, ys[left].min()        # inner corner of marker A (world x0,y0) -> image bottom-left
    bx1, by0 = xs[~left].min(), ys[~left].max() + 1     # inner corner of marker B (world x1,y1) -> image top-right
    tmp = os.path.join(OUT, name + "_tmp.png")
    Image.fromarray(np.where(mag[..., None], np.array([im[2, 2]] * 1)[0], im).astype(np.uint8)).save(tmp)
    finish(tmp, None, tmp, grain_angle_deg=grain_angle, down=1, grain_classes=grain_classes, crop=False)
    img = Image.open(tmp).crop((int(ax0), int(by0), int(bx1), int(ay1)))
    out = os.path.join(OUT, name + ".png")
    img.save(out)
    return out
