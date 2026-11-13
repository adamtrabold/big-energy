#!/usr/bin/env python3
"""Round 4 mock geometry: HUSH (pebble), ONE SHEET (closed-top shell), FOLD (walnut blocks + white pickguards).

Layout = systems common rev 6 (PLAY row in front, VOICE behind), ONE SHEET frame; HUSH x+7, FOLD x+5.
Coordinates: origin front-left outer corner, x right, y away from the player, z up from the table. mm.
Render with:  python3 r4.py [job ...]   (--test for quick low-res).  Outputs in out/r4_*.png
"""
import math, os, random, sys
import ld
from ld import box, cyl, txt, c, knob_std, knob_hero, toggle, led, stick, ticks, KNOB_D, HERO_D, KNOB_H, HERO_H

OUT = ld.OUT

# ------------------------------------------------------------------ the common layout (ONE SHEET frame, 276 wide)
# (label, x, kind, midi)   kind: k knob · h hero · t toggle · s stick · l led · r rotary switch (WAVE) · g range
PLAY = [("BEND", 20, "s", False), ("MOD", 42, "k", True), ("MOD MIX", 62, "k", False), ("OSC MOD", 78, "t", False),
        ("FILTER MOD", 92, "t", False), ("GLIDE", 108, "k", True), ("CUTOFF", 140, "h", True),
        ("EMPHASIS", 164, "k", False), ("AMOUNT", 188, "k", False), ("KBD CTRL", 204, "t", False),
        ("VELOCITY", 220, "t", False), ("VOLUME", 243, "k", False), ("STATUS", 262, "l", False)]
NIC = (152, 79)                       # "not in control" light, behind-right of CUTOFF (frame; y relative to PLAY 68)
VF = [("TUNE", 18.5, "k", True), ("RANGE", 38.5, "g", True), ("RANGE", 58.5, "g", True), ("RANGE", 78.5, "g", True),
      ("FREQ 2", 98.5, "k", True), ("OSC 1", 137, "k", False), ("OSC 3", 157, "k", False),
      ("ATTACK", 197, "k", False), ("DECAY", 217, "k", False), ("SUSTAIN", 237, "k", False)]
VB = [("WAVE", 38.5, "r", False), ("WAVE", 58.5, "r", False), ("WAVE", 78.5, "r", False), ("FREQ 3", 98.5, "k", True),
      ("OSC 3 CTL", 114.5, "t", False), ("OSC 2", 137, "k", False), ("NOISE / EXT", 157, "k", False),
      ("SOURCE", 173, "t", False), ("ATTACK", 197, "k", False), ("DECAY", 217, "k", False), ("SUSTAIN", 237, "k", False),
      ("DECAY", 253, "t", False)]
BREAK_FULL = 122.5; BREAK_PLAY = 228.0; BREAK_VOICE = 181.0; HBREAK = 85.4

random.seed(11)
_ANGS = [-120, -90, -60, -30, 0, 15, 30, 60, 90, 120]
ANG = {}
def ang(key):
    if key not in ANG:
        ANG[key] = random.choice(_ANGS)
    return ANG[key]
ANG[("CUTOFF", 140)] = 40

def sharps_after():
    return [i for i in range(14) if [1, 1, 0, 1, 1, 1, 0][i % 7]]

# ------------------------------------------------------------------ colours
FELT = "#868b94"; FELT_DK = "#70757e"; FELT_DEB = "#666b74"; TAG = "#d8d3c9"; MAPLE = "#e3c493"; MAPLE_DK = "#c9a06c"
K_CREAM = "#ece2c6"; RED = "#b8432a"; INK_H = "#3a3631"
PCREAM = "#e8dcc2"; OS_INK = "#5b4a39"
WAL_P = "#6b4429"      # walnut-tone filament (printed blocks)
WAL_R = "#6e4628"      # real walnut (grain added in post)
PG = "#f1ebdd"; PG_CH = "#d9d0bf"; PG_BLK = "#1d1c1b"; FO_INK = "#1f1d1b"
K_BLACK = "#1c1c1e"; K_RED = "#b3302a"
ACRYL_W = "#f6f3ec"; ACRYL_K = "#3b3734"

# ------------------------------------------------------------------ primitives
def knob_black(x, y, z, a, col=K_BLACK, line="#f4f3ef", d=14.5, h=13.5):
    """Tayda plastic black knob, 6 mm x 18T split shaft, ~14.5 x 13.5, white indicator."""
    n = 24; pts = []
    for i in range(n * 4):
        t = 2 * math.pi * i / (n * 4)
        r = d / 2 - 0.3 * (0.5 + 0.5 * math.cos(n * t))
        pts.append(f"[{r*math.cos(t):.3f},{r*math.sin(t):.3f}]")
    s = f'{c(col)} translate([{x:.3f},{y:.3f},{z:.3f}]) linear_extrude(height={h-1.0}, scale=0.94) polygon([{",".join(pts)}]);\n'
    s += f'{c("#262628")} translate([{x:.3f},{y:.3f},{z+h-1.0:.3f}]) cylinder(h=1.0, d1={d*0.93:.2f}, d2={d*0.86:.2f}, $fn=48);\n'
    s += (f'{c(line)} translate([{x:.3f},{y:.3f},{z+h:.3f}]) rotate([0,0,{90-a:.1f}]) '
          f'translate([{d*0.08:.2f},-0.5,0]) cube([{d*0.34:.2f},1.0,0.08]);\n')
    return s

def corner_profile(R, H, rt, rb):
    pts = [(0, 0)]
    if rb > 0:
        pts.append((R - rb, 0))
        for k in range(1, 24):
            t = -math.pi / 2 + (math.pi / 2) * k / 24
            pts.append((R - rb + rb * math.cos(t), rb + rb * math.sin(t)))
        pts.append((R, rb))
    else:
        pts.append((R, 0))
    if rt > 0:
        pts.append((R, H - rt))
        for k in range(1, 24):
            t = (math.pi / 2) * k / 24
            pts.append((R - rt + rt * math.cos(t), H - rt + rt * math.sin(t)))
        pts.append((R - rt, H))
    else:
        pts.append((R, H))
    pts.append((0, H))
    return "[" + ",".join(f"[{a:.3f},{b:.3f}]" for a, b in pts) + "]"

def pebble(x0, y0, W, D, H, Rf, Rr, rt, rb, z0=0.0, fn=160):
    """solid with plan corners Rf (front) / Rr (rear), top edge round rt, bottom round rb, flat top and bottom."""
    pf, pr = corner_profile(Rf, H, rt, rb), corner_profile(Rr, H, rt, rb)
    out = "hull(){\n"
    for (cx, cy, p) in [(x0 + Rf, y0 + Rf, pf), (x0 + W - Rf, y0 + Rf, pf), (x0 + Rr, y0 + D - Rr, pr), (x0 + W - Rr, y0 + D - Rr, pr)]:
        out += f' translate([{cx:.3f},{cy:.3f},{z0:.3f}]) rotate_extrude($fn={fn}) polygon({p});\n'
    return out + "}\n"

def rrect2d(x0, y0, x1, y1, rf, rr):
    """2D rounded rectangle, front corner radius rf, rear rr (0 = square)."""
    def cor(cx, cy, r, sx, sy):
        if r <= 0:
            return f'translate([{cx - (0.01 if sx > 0 else 0):.3f},{cy - (0.01 if sy > 0 else 0):.3f}]) square([0.01,0.01]);'
        return f'translate([{cx - sx*r:.3f},{cy - sy*r:.3f}]) circle(r={r:.3f},$fn=48);'
    return ("hull(){" + cor(x0, y0, rf, -1, -1) + cor(x1, y0, rf, 1, -1) + cor(x0, y1, rr, -1, 1) + cor(x1, y1, rr, 1, 1) + "}")

def ext(shape2d, z0, z1, col):
    return f'{c(col)} translate([0,0,{z0:.3f}]) linear_extrude({z1-z0:.3f}) {shape2d}\n'

# ------------------------------------------------------------------ keys
def keys_flat(x0, y0, wz, white=ACRYL_W, sharp=ACRYL_K, bed="#0e0d0c", bed_z=None):
    """short tops (eng S1): whites 17.6 x 30 at 18 pitch, sharps 16 x 14 rear row +2. y0 = white front edge."""
    s = ""
    for i in range(15):
        xa = x0 + 18 * i
        s += box(xa + 0.3, y0, wz - 3, xa + 17.7, y0 + 30, wz, white)
    for i in sharps_after():
        xc = x0 + 18 * (i + 1)
        s += box(xc - 8, y0 + 32, wz - 1, xc + 8, y0 + 46, wz + 2, sharp)
    bz = (wz - 3.2) if bed_z is None else bed_z
    s += box(x0 - 0.2, y0 - 0.2, bz - 1, x0 + 270.2, y0 + 46.5, bz, bed)
    return s

# ------------------------------------------------------------------ panel content (shared by the three)
class Style:
    def __init__(self, **kw):
        self.__dict__.update(dict(knob=lambda x, y, z, a: knob_std(x, y, z, a, col=K_CREAM),
                                  hero=lambda x, y, z, a: knob_hero(x, y, z, a, col=K_CREAM),
                                  ink="#3a3631", font="Inter:style=SemiBold", lsize=1.9, upper=True,
                                  knob_r=7.45, hero_r=10.4, kz_extra=0.0, tag=None, ticks=True, scale_ink=None,
                                  lab_gap=3.2))
        self.__dict__.update(kw)

def item(lab, x, y, kind, midi, z, st, key):
    s = ""
    lab_s = lab if st.upper else lab.lower()
    p = z
    kz = z + ld.KNOB_GAP + st.kz_extra
    ink = st.scale_ink or st.ink
    if kind in "kgrh":
        hero = kind == "h"
        r = st.hero_r if hero else st.knob_r
        if st.tag:
            s += st.tag(x, y, z, hero)
        a = ang(key)
        s += (st.hero if hero else st.knob)(x, y, kz, a)
        if st.ticks:
            if hero:
                s += ticks(x, y, p, r + 1.4, 11, ink, length=1.8, width=0.45)
            elif kind == "g":
                s += ticks(x, y, p, r + 0.9, [-125, -75, -25, 25, 75, 125], ink, length=1.8, width=0.6)
            elif kind == "r":
                s += ticks(x, y, p, r + 0.9, [-125, -75, -25, 25, 75, 125], ink, length=1.2, width=0.45)
            else:
                s += ticks(x, y, p, r + 0.9, 7, ink, length=1.0, width=0.35)
        s += txt(x, y - r - st.lab_gap - 0.6, p, lab_s, st.lsize, st.ink, font=st.font)
        if midi:
            rr = r + 3.0
            s += cyl(x + rr * 0.72, y + rr * 0.72, p, 0.1, 1.1, st.ink, fn=12)
    elif kind == "t":
        if st.tag:
            s += st.tag(x, y, z, None)
        s += toggle(x, y, z)
        s += txt(x, y - 8.4, p, lab_s, st.lsize * 0.85, st.ink, font=st.font)
    elif kind == "s":
        s += box(x - 1.7, y - 8, z, x + 1.7, y + 8, z + 0.05, "#1d1b19")
        s += stick(x, y, z)
        s += txt(x, y - 11.5, p, lab_s, st.lsize, st.ink, font=st.font)
    elif kind == "l":
        s += led(x, y, z, col="#9fd36b")
        s += txt(x, y - 5.6, p, lab_s, st.lsize * 0.85, st.ink, font=st.font)
    return s

def panel(z, st, xo=0.0, py=68.0, vfy=100.0, vby=123.0, zmap=None, parts=("play", "voice"), skip=()):
    s = ""
    zf = zmap or (lambda x, y: z)
    if "play" in parts:
        for lab, x, k, m in PLAY:
            if lab in skip:
                continue
            s += item(lab, x + xo, py, k, m, zf(x + xo, py), st, (lab, x))
        s += led(NIC[0] + xo, py + (NIC[1] - 68), zf(NIC[0] + xo, py), col="#efe3c8")
    if "voice" in parts:
        for lab, x, k, m in VF:
            s += item(lab, x + xo, vfy, k, m, zf(x + xo, vfy), st, ("F", lab, x))
        for lab, x, k, m in VB:
            s += item(lab, x + xo, vby, k, m, zf(x + xo, vby), st, ("B", lab, x))
    return s

# =================================================================== HUSH (pebble)
HU_W = 290.0
HU_D = float(os.environ.get('R4_HU_D', 176))   # eng round4 E-L9: main board 268 x 115 -> +30 at the back (systems to confirm)
HU_FT = 25.5                # felt surface
HU_XO = 7.0

def hush_body(col=FELT):
    return f'{c(col)} ' + pebble(0, 0, HU_W, HU_D, HU_FT, 20, 44, 12, 6)

def hush_tag(x, y, z, hero):
    """printed tag flush in the felt: a ring (scale) + nothing else; names are on the tag's lower lip."""
    if hero is None:     # toggle: small round tag
        return cyl(x, y, z - 1.0, 1.06, 9.5, TAG, fn=40)
    r = 12.4 if hero else 9.6
    return cyl(x, y, z - 1.0, 1.06, 2 * r, TAG, fn=64) + \
        f'{c(TAG)} hull(){{ translate([{x-6.5},{y-r-0.2},{z-1}]) cylinder(h=1.06,r=2.6,$fn=24); translate([{x+6.5},{y-r-0.2},{z-1}]) cylinder(h=1.06,r=2.6,$fn=24); translate([{x},{y-r+4},{z-1}]) cylinder(h=1.06,r=2,$fn=12);}}\n'

def hush(show_jacks=True):
    s = hush_body()
    z = HU_FT
    # pressed (blind-debossed) rules on the breaks and pressed section names: letterpress without ink
    xo = HU_XO
    s += box(BREAK_FULL + xo - 0.5, 56, z - 0.4, BREAK_FULL + xo + 0.5, 140, z + 0.02, FELT_DEB)
    s += box(18, HBREAK - 0.5, z - 0.4, HU_W - 18, HBREAK + 0.5, z + 0.02, FELT_DEB)
    s += box(BREAK_PLAY + xo - 0.5, 56, z - 0.4, BREAK_PLAY + xo + 0.5, HBREAK, z + 0.02, FELT_DEB)
    s += box(BREAK_VOICE + xo - 0.5, HBREAK, z - 0.4, BREAK_VOICE + xo + 0.5, 140, z + 0.02, FELT_DEB)
    for (tx, ty, name) in [(40 + xo, 80.4, "PITCH & MOD"), (170 + xo, 80.4, "TONE"), (232 + xo, 80.4, "LEVEL"),
                           (25.5 + xo, 136.5, "OSCILLATORS"), (126 + xo, 136.5, "MIXER"), (185 + xo, 136.5, "CONTOURS  ·  filter front, loudness back")]:
        s += txt(tx, ty, z - 0.25, name, 2.6, FELT_DEB, font="Inter:style=Bold", halign="left", h=0.3)
    # pegs (maple mushroom plugs) on punched felt collars
    for n in range(15):
        xc = 19 + 18 * n
        s += cyl(xc, 19.5, z - 0.15, 0.2, 19.0, FELT_DK, fn=48)
        s += cyl(xc, 19.5, z, 2.6, 7.0, "#d4b385", fn=24)
        s += cyl(xc, 19.5, z + 2.5, 1.7, 12.7, MAPLE, fn=48)
        s += f'{c(MAPLE)} translate([{xc},19.5,{z+4.2}]) scale([1,1,0.28]) sphere(d=12.7,$fn=48);\n'
    for i in sharps_after():
        xc = 10 + 18 * (i + 1)
        s += cyl(xc, 42, z - 0.15, 0.2, 19.0, FELT_DK, fn=48)
        s += cyl(xc, 42, z, 3.4, 7.0, "#b98f5e", fn=24)
        s += cyl(xc, 42, z + 3.3, 1.7, 12.7, MAPLE_DK, fn=48)
        s += f'{c(MAPLE_DK)} translate([{xc},42,{z+5.0}]) scale([1,1,0.28]) sphere(d=12.7,$fn=48);\n'
    st = Style(ink=INK_H, font="Inter:style=Bold", lsize=1.75, tag=hush_tag, kz_extra=0.06, lab_gap=3.4)
    # the stick sits on its own printed tag (same hard material)
    s += f'{c(TAG)} hull(){{ translate([{20+xo},60,{z-1}]) cylinder(h=1.06,r=6.5,$fn=32); translate([{20+xo},76,{z-1}]) cylinder(h=1.06,r=6.5,$fn=32);}}\n'
    s += panel(z + 0.06, st, xo=xo)
    # back band: the jack legend pressed above the ports (read from the playing seat), and the name space
    for k, lab in enumerate(JACK_LABELS):
        s += txt(80 + 19 * k, HU_D - 15.5, z - 0.25, lab, 1.9, FELT_DEB, font="Inter:style=Bold", h=0.3)
    s += txt(60, HU_D - 15.5, z - 0.25, "POWER", 1.9, FELT_DEB, font="Inter:style=Bold", h=0.3)
    s += box(52, HU_D - 20.5, z - 0.4, 222, HU_D - 20, z + 0.02, FELT_DEB)
    if show_jacks:
        s += hush_jacks()
    return s

JACK_LABELS = ["PHONES", "EXT IN", "FILTER CV", "PITCH CV", "GATE", "MIDI IN", "USB-C"]

def hush_jacks():
    """felt cut round the ports on the rear wall's straight run (x 60-230: the R 44 corners leave no straight wall past it)."""
    s = ""
    xs = [80 + 19 * k for k in range(7)]
    for k, x in enumerate(xs):
        if k == 6:
            s += box(x - 4.5, HU_D - 0.4, 8.0, x + 4.5, HU_D + 0.1, 11.4, "#1a1a1a")
        else:
            s += f'{c("#151515")} translate([{x},{HU_D-0.3},9.7]) rotate([-90,0,0]) cylinder(h=0.5,d=4.6,$fn=24);\n'
    s += box(60 - 5, HU_D - 0.4, 8.2, 60 + 5, HU_D + 0.1, 11.2, "#2a2826")
    return s

def hush_under():
    """the underside: binding ring clamps the felt; back panel inside it; every screw is here."""
    s = hush_body()
    z = -0.05
    ring = rrect2d(5, 5, HU_W - 5, HU_D - 5, 15, 39)
    inner = rrect2d(20, 20, HU_W - 20, HU_D - 20, 1, 24)
    s += f'{c("#8a8682")} translate([0,0,{z-1.6}]) linear_extrude(1.6) difference(){{ {ring} {inner} }}\n'
    s += ext(rrect2d(20.4, 20.4, HU_W - 20.4, HU_D - 20.4, 1, 23.6), z - 1.2, z, "#a39e97")
    # binding-ring screws (10) and back-panel screws (8)
    for (x, y) in [(13, 30), (13, 110), (HU_W - 13, 30), (HU_W - 13, 110), (75, 12.5), (145, 12.5), (215, 12.5), (75, HU_D - 12.5), (145, HU_D - 12.5), (215, HU_D - 12.5)]:
        s += cyl(x, y, z - 1.75, 0.2, 4.6, "#3b3e42", fn=20)
    for (x, y) in [(28, 28), (28, HU_D - 28), (HU_W - 28, 28), (HU_W - 28, HU_D - 28), (100, 28), (190, 28), (100, HU_D - 24), (190, HU_D - 24)]:
        s += cyl(x, y, z - 1.35, 0.2, 4.6, "#3b3e42", fn=20)
    for (x, y) in [(38, 38), (HU_W - 38, 38), (38, HU_D - 38), (HU_W - 38, HU_D - 38)]:
        s += cyl(x, y, z - 3.2, 2.0, 11, "#2a2a2a", fn=32)
    gx, gy = 243, 113
    for k in range(-4, 5):
        s += box(gx - math.sqrt(max(0, 400 - (k * 4.2) ** 2)), gy + k * 4.2 - 0.9, z - 1.3, gx + math.sqrt(max(0, 400 - (k * 4.2) ** 2)), gy + k * 4.2 + 0.9, z - 1.22, "#2b2d30")
    s += box(140, HU_D / 2, z - 1.3, 152, HU_D / 2 + 4, z - 1.22, "#2b2d30")   # keyhole (J18)
    s += hush_jacks()
    return s

# =================================================================== ONE SHEET (closed-top shell)
OS_W, OS_Z = 276.0, 24.0
OS_D = float(os.environ.get('R4_OS_D', 170))    # eng round4 E-L9 (was 140)
OS_PITCH = 1.1
OS_TONE = {"A": ("#e0d1b0", "#c8b48d"), "B": ("#f1e9d7", "#e2d5bb"), "P": ("#ebe0c8", "#d2c3a4")}

def hatch(x0, y0, x1, y1, a, z, col, pitch=OS_PITCH, w=0.32):
    th = math.radians(a); ux, uy = math.cos(th), math.sin(th); nx, ny = -uy, ux
    ds = [cx * nx + cy * ny for cx, cy in [(x0, y0), (x1, y0), (x0, y1), (x1, y1)]]
    out = ""; d = math.ceil(min(ds) / pitch) * pitch
    while d <= max(ds):
        px, py = d * nx, d * ny; t0, t1 = -1e9, 1e9
        for p0, u, lo, hi in ((px, ux, x0, x1), (py, uy, y0, y1)):
            if abs(u) < 1e-9:
                if not (lo <= p0 <= hi): t0, t1 = 1, 0
            else:
                aa, bb = (lo - p0) / u, (hi - p0) / u
                t0, t1 = max(t0, min(aa, bb)), min(t1, max(aa, bb))
        if t1 - t0 > 0.5:
            cx, cy = px + ux * (t0 + t1) / 2, py + uy * (t0 + t1) / 2
            out += (f'{c(col)} translate([{cx:.3f},{cy:.3f},{z:.3f}]) rotate([0,0,{a:.2f}]) '
                    f'translate([{-(t1-t0)/2:.3f},{-w/2:.3f},0]) cube([{t1-t0:.3f},{w:.3f},0.03]);\n')
        d += pitch
    return out

def loops(x0, y0, x1, y1, n, z, col, pitch=OS_PITCH, w=0.32, outward=False):
    """perimeter loops the slicer draws anyway: n rectangles inside (x0,y0,x1,y1)."""
    s = ""
    for k in range(n):
        o = (k + 0.5) * pitch * (-1 if outward else 1)
        a0, b0, a1, b1 = x0 + o, y0 + o, x1 - o, y1 - o
        s += box(a0, b0 - w / 2, z, a1, b0 + w / 2, z + 0.03, col) + box(a0, b1 - w / 2, z, a1, b1 + w / 2, z + 0.03, col)
        s += box(a0 - w / 2, b0, z, a0 + w / 2, b1, z + 0.03, col) + box(a1 - w / 2, b0, z, a1 + w / 2, b1, z + 0.03, col)
    return s

def halo(x, y, z, r0, r1, base, ring, pitch=OS_PITCH, w=0.32):
    s = cyl(x, y, z, 0.035, 2 * r1 + 0.6, base, fn=72)
    r = r0
    while r <= r1:
        s += (f'{c(ring)} translate([{x:.3f},{y:.3f},{z+0.035:.3f}]) difference(){{ cylinder(h=0.03,r={r+w/2:.3f},$fn=96);'
              f' translate([0,0,-1]) cylinder(h=2,r={r-w/2:.3f},$fn=96);}}\n')
        r += pitch
    return s

OS_FIELDS = [  # (x0, y0, x1, y1, tone, angle): checkerboard so every neighbour turns the other way
    (3.6, 52.6, 122.5, HBREAK, "A", 45), (122.5, 52.6, BREAK_PLAY, HBREAK, "B", -45), (BREAK_PLAY, 52.6, OS_W - 3.6, HBREAK, "A", 45),
    (3.6, HBREAK, 122.5, 141.0, "B", -45), (122.5, HBREAK, BREAK_VOICE, 141.0, "A", 45), (BREAK_VOICE, HBREAK, OS_W - 3.6, 141.0, "B", -45),
    (3.6, 141.0, OS_W - 3.6, OS_D - 3.6, "P", 0)]

def one_sheet_face(z):
    s = ""
    for (x0, y0, x1, y1, tone, a) in OS_FIELDS:
        xa = x0 + (0.6 if x0 > 4 else 0); xb = x1 - (0.6 if x1 < OS_W - 4 else 0)
        ya = y0 + (0.6 if y0 > 60 else 0); yb = y1 - (0.6 if y1 < OS_D - 4 else 0)
        base, ln = OS_TONE[tone]
        s += box(xa, ya, z, xb, yb, z + 0.01, base) + hatch(xa, ya, xb, yb, a, z + 0.01, ln)
    base, ln = OS_TONE["P"]
    # perimeter loops round the outside and round the key window: the slicer draws these anyway
    s += box(0.6, 0.6, z, OS_W - 0.6, 3.4, z + 0.005, base)
    s += box(0.6, 0.6, z, 3.4, OS_D - 0.6, z + 0.005, base) + box(OS_W - 3.4, 0.6, z, OS_W - 0.6, OS_D - 0.6, z + 0.005, base)
    s += box(0.6, OS_D - 3.4, z, OS_W - 0.6, OS_D - 0.6, z + 0.005, base) + box(3, 49.5, z, OS_W - 3, 52.6, z + 0.005, base)
    s += loops(0.4, 0.4, OS_W - 0.4, OS_D - 0.4, 3, z + 0.01, ln)
    s += loops(3.0, 3.0, OS_W - 3.0, 49.5, 3, z + 0.01, ln, outward=True)
    def tone_at(x, y):
        for (x0, y0, x1, y1, tone, a) in OS_FIELDS:
            if x0 <= x < x1 and y0 <= y < y1:
                return OS_TONE[tone]
        return OS_TONE["P"]
    for lab, x, k, m in PLAY:
        if k in "kh":
            b, l = tone_at(x, 68)
            s += halo(x, 68, z + 0.02, (10.4 + 0.6) if k == "h" else 7.85, (10.4 + 2.9) if k == "h" else 10.05, b, l)
    for row, yy in ((VF, 100), (VB, 123)):
        for lab, x, k, m in row:
            if k in "kgr":
                b, l = tone_at(x, yy)
                s += halo(x, yy, z + 0.02, 7.85, 10.05, b, l)
    return s

def one_sheet(face=True):
    s = ""
    shell2d = rrect2d(0, 0, OS_W, OS_D, 6, 6)
    win = f'translate([3,3]) square([270,46.5]);'
    # closed-top shell: walls + top in one; key window the only big opening; top edge R 2 (drawn as a 2-step)
    s += f'{c(PCREAM)} translate([0,0,6]) linear_extrude({OS_Z-2-6:.2f}) difference(){{ {shell2d} {win} }}\n'
    s += f'{c(PCREAM)} translate([0,0,{OS_Z-2:.2f}]) linear_extrude(2) offset(delta=0) difference(){{ offset(r=-0.0) {rrect2d(0.6,0.6,OS_W-0.6,OS_D-0.6,5.4,5.4)} {win} }}\n'
    s += f'{c(PCREAM)} translate([0,0,{OS_Z-1.4:.2f}]) linear_extrude(1.4) difference(){{ {rrect2d(0,0,OS_W,OS_D,6,6)} offset(delta=0.6) {win} }}\n'
    s += f'{c(PCREAM)} translate([0,0,{OS_Z-0.6:.2f}]) linear_extrude(0.6) difference(){{ {rrect2d(0.9,0.9,OS_W-0.9,OS_D-0.9,5.1,5.1)} offset(delta=0.9) {win} }}\n'
    s += f'{c(PCREAM)} translate([0,0,0.5]) linear_extrude(5.5) difference(){{ {shell2d} offset(delta=-2.4) {shell2d} }}\n'
    s += f'{c("#c99b62")} translate([0,0,0]) linear_extrude(0.6) offset(delta=-2.6) {shell2d}\n'  # back panel peeking at the bottom edge
    if face:
        s += one_sheet_face(OS_Z + 0.005)
    # sunk grooves on the breaks (0.6 deep, 1.2 wide)
    gz = OS_Z + 0.05
    g = "#b7a98e"
    s += box(BREAK_FULL - 0.6, 52.6, gz, BREAK_FULL + 0.6, 141.0, gz + 0.03, g) + box(4, 140.4, gz, OS_W - 4, 141.6, gz + 0.03, g)
    s += box(4, HBREAK - 0.6, gz, OS_W - 4, HBREAK + 0.6, gz + 0.03, g)
    s += box(BREAK_PLAY - 0.6, 52.6, gz, BREAK_PLAY + 0.6, HBREAK, gz + 0.03, g)
    s += box(BREAK_VOICE - 0.6, HBREAK, gz, BREAK_VOICE + 0.6, 141.0, gz + 0.03, g)
    tz = OS_Z + 0.04
    for (tx, ty, name) in [(30, 80.8, "PITCH & MOD"), (170, 80.8, "TONE"), (232, 80.8, "LEVEL"),
                           (6, 136.0, "II  OSCILLATORS"), (126, 136.0, "III  MIXER"), (185, 136.0, "IV  CONTOURS  ·  filter front, loudness back")]:
        s += txt(tx, ty, tz, name, 2.1, OS_INK, font="Inter:style=Bold", halign="left")
    # back band (the board's extra depth): jack legend over the rear-wall ports, read from the seat; the file is the drawing
    for k, lab in enumerate(["PHONES", "EXT IN", "FILTER CV", "PITCH CV", "GATE", "MIDI IN", "USB-C"]):
        s += txt(160 + 17 * k, OS_D - 9.0, tz, lab, 1.7, OS_INK, font="Inter:style=Bold")
        s += box(160 + 17 * k - 0.25, OS_D - 6.8, tz, 160 + 17 * k + 0.25, OS_D - 4.2, tz + 0.02, OS_INK)
    s += txt(140, OS_D - 9.0, tz, "POWER", 1.7, OS_INK, font="Inter:style=Bold")
    s += txt(8, OS_D - 9.0, tz, "shell rev 4  ·  one filament, one swap  ·  printed face down", 1.7, OS_INK, halign="left")
    s += keys_flat(3, 3, OS_Z)
    st = Style(ink=OS_INK, lsize=1.9)
    s += box(20 - 9, 59, OS_Z - 0.1, 20 + 9, 77, OS_Z + 0.06, "#efe9dc")    # Delrin gate plate, flush in its pocket
    s += panel(OS_Z + 0.06, st)
    s += os_jacks()
    return s

def os_jacks():
    s = ""
    for k in range(7):
        x = 160 + 17 * k
        if k == 6:
            s += box(x - 4.5, OS_D - 0.3, 10.3, x + 4.5, OS_D + 0.1, 13.7, "#1a1a1a")
        else:
            s += f'{c("#151515")} translate([{x},{OS_D-0.25},12]) rotate([-90,0,0]) cylinder(h=0.4,d=4.6,$fn=24);\n'
    s += box(140 - 5, OS_D - 0.3, 10.5, 140 + 5, OS_D + 0.1, 13.5, "#2a2826")
    return s

def one_sheet_under():
    s = one_sheet(face=False)
    shell2d = rrect2d(0, 0, OS_W, OS_D, 6, 6)
    s += f'{c("#c99b62")} translate([0,0,-0.05]) linear_extrude(3.0) offset(delta=-2.6) {shell2d}\n'
    for (x, y) in [(10, 10), (138, 7), (OS_W - 10, 10), (10, OS_D - 10), (138, OS_D - 7), (OS_W - 10, OS_D - 10), (7, 70), (OS_W - 7, 70)]:
        s += cyl(x, y, -0.25, 0.2, 5.0, "#3b3e42", fn=20)
    for (x, y) in [(20, 20), (OS_W - 20, 20), (20, OS_D - 20), (OS_W - 20, OS_D - 20)]:
        s += cyl(x, y, -6, 5.95, 12, "#2a2a2a", fn=32)
    for k in range(-5, 6):
        for j in range(-5, 6):
            if k * k + j * j <= 25:
                s += cyl(240 + k * 4.2, 113 + j * 4.2, -0.15, 0.1, 2.4, "#2b2d30", fn=12)
    s += box(132, OS_D / 2, -0.15, 144, OS_D / 2 + 4, -0.05, "#2b2d30")
    s += (f'{c("#8a6a44")} translate([110,{OS_D/2+20},-0.12]) mirror([1,0,0]) linear_extrude(0.06) '
          f'text("shell rev 4 · back panel 3 mm ply · 8 x M3", size=3.0, font="Inter:style=Bold", halign="center", valign="center");\n')
    return s

# =================================================================== FOLD (walnut-tone blocks + white pickguards)
FO_W, FO_H = 286.0, 116.0     # systems rev 4.2: internal battery bay in the lid band (was 100 in 4.1, 86 in 4)
BASE_H, LID_H = 15.6, 34.5
LID_PF = 15.1               # lid plate face, open
AX_Y, AX_Z = 117.0, 25.0    # hinge axis
LY0 = 118.0                 # lid's hinge edge, open
VD_F, VD_B = 68.65, 91.65   # lid VOICE rows, distance from the hinge edge
EMPH = (169.0, 48.0)        # EMPHASIS on the lid (FOLD x, d): eng keeps it on the ladder's half
FO_XO = 5.0

def pg_layers(shape2d, face_z, body_col=PG_BLK):
    """the pickguard: white face (first 1.0 mm, printed face down), then the swap to black for the rest.
    A 45° bevel round every edge shows white over black: the guitar pickguard's line, made by the one swap."""
    s = ext(shape2d, face_z - 2.5, face_z - 1.0, body_col)
    s += ext(f"offset(delta=-0.6) {shape2d}", face_z - 1.0, face_z - 0.05, PG_CH)
    s += ext(f"offset(delta=-1.6) {shape2d}", face_z - 0.05, face_z, PG)
    return s

def base_plate2d():
    outer = rrect2d(4.3, 4.0, FO_W - 4.3, FO_H - 4.3, 0, 7.7)
    win = "translate([8,2]) square([270,49]);"
    return f"difference(){{ {outer} {win} }}"

def lid_plate2d():
    return rrect2d(4.3, LY0 + 0.3, FO_W - 4.3, LY0 + FO_H - 4.3, 0, 7.7)

def fold_base(walnut=WAL_P, plate=True, plate_dz=0.0, controls=True):
    s = ""
    pocket = f"translate([0,0,11]) linear_extrude(10) {rrect2d(4, 4, FO_W-4, FO_H-4, 0, 8)}"
    s += f'{c(walnut)} difference(){{ {pebble(0, 0, FO_W, FO_H, BASE_H, 12, 12, 3, 6)} {pocket} }}\n'
    s += box(8, 4.4, 11, 278, 51, 12.6, "#0e0d0c")     # strip C / key bed seen between keys
    if plate:
        g = f"translate([0,0,{plate_dz}]) {{\n"
        g += pg_layers(base_plate2d(), BASE_H)
        gz = BASE_H + 0.02
        for xb in (127.5, 233.0):
            g += box(xb - 0.6, 53.5, gz, xb + 0.6, 80.5, gz + 0.03, "#d3cab8")
        st = fold_style()
        if controls:
            g += box(25 - 9, 60, BASE_H - 0.05, 25 + 9, 76, BASE_H + 0.03, "#ece6d8")   # gate pocket plate
            g += panel(BASE_H, st, xo=FO_XO, parts=("play",), skip=("EMPHASIS",))
            g += emph_ghost(BASE_H)
            for (tx, name) in [(14, "pitch & mod"), (198, "tone"), (237, "level")]:
                g += txt(tx, 83.2, BASE_H + 0.01, name, 2.4, "#8d6b3c", font="Kalam:style=Bold", halign="left")
            # the base's rear strip: the name, Proof's place for it (between the panel and the keys' half)
            g += signal_map(gz, x0=60.0, y0=84.0)     # the base's rear strip (y 82-112): the map of the signal, on the fold
        g += "}\n"
        s += g
    s += keys_flat(8, 4.5, 17.5, bed_z=12.6)
    return s

def emph_ghost(z):
    """the empty slot EMPHASIS left in the PLAY row: a printed ring where it parks when closed, pointing to the lid."""
    x, y = EMPH[0], 68.0
    s = (f'{c(FO_INK)} translate([{x},{y},{z+0.02}]) difference(){{ cylinder(h=0.04,r=7.6,$fn=64); translate([0,0,-1]) cylinder(h=2,r=7.15,$fn=64);}}\n')
    s += txt(x, y + 1.2, z + 0.02, "emphasis", 2.0, FO_INK, font="Kalam:style=Bold")
    s += txt(x, y - 2.6, z + 0.02, "is on the lid", 1.6, "#8d6b3c", font="Kalam:style=Bold")
    return s

def signal_map(z, x0=14.0, y0=LY0 + 8):
    """the lid band's left part: a printed signal map (oscillators -> mixer -> filter -> amp), Proof's legends as a map."""
    s = ""; ink = FO_INK; br = "#8d6b3c"
    boxes = [("osc 1 2 3", x0, 14), ("mixer", x0 + 32, 12), ("filter", x0 + 60, 12), ("amp", x0 + 88, 10), ("out", x0 + 112, 8)]
    yb = y0 + 14
    for i, (lab, x, w) in enumerate(boxes):
        bw = 6 + w * 1.2
        s += f'{c(ink)} translate([0,0,{z}]) linear_extrude(0.04) difference(){{ {rrect2d(x, yb - 4, x + bw, yb + 4, 1.5, 1.5)} {rrect2d(x+0.35, yb - 3.65, x + bw-0.35, yb + 3.65, 1.2, 1.2)} }}\n'
        s += txt(x + bw / 2, yb, z, lab, 2.2, ink, font="Kalam:style=Bold")
        if i < len(boxes) - 1:
            nx = boxes[i + 1][1]
            s += box(x + bw, yb - 0.2, z, nx, yb + 0.2, z + 0.04, ink)
            s += f'{c(ink)} translate([{nx-0.1},{yb},{z}]) rotate([0,0,180]) linear_extrude(0.04) polygon([[0,0],[1.6,0.9],[1.6,-0.9]]);\n'
    # contours feed filter and amp from below; osc 3 / noise feed the mod bus from above
    s += txt(x0 + 74, y0 + 2, z, "contours", 2.0, br, font="Kalam:style=Bold")
    s += box(x0 + 67, y0 + 4, z, x0 + 67.4, yb - 4, z + 0.04, br) + box(x0 + 94, y0 + 4, z, x0 + 94.4, yb - 4, z + 0.04, br)
    s += box(x0 + 67, y0 + 3.8, z, x0 + 94.4, y0 + 4.2, z + 0.04, br)
    s += txt(x0 + 10, y0 + 24, z, "mod: osc 3 / noise  to  pitch & filter", 2.0, br, font="Kalam:style=Bold", halign="left")
    s += box(x0 + 7, yb + 4, z, x0 + 7.4, y0 + 22.5, z + 0.04, br)
    return s

def fold_style():
    return Style(knob=lambda x, y, z, a: knob_black(x, y, z, a),
                 hero=lambda x, y, z, a: knob_hero(x, y, z, a, col=K_RED, line="#f3ead6"),
                 ink=FO_INK, font="Kalam:style=Bold", lsize=2.35, upper=False, knob_r=7.25, lab_gap=2.9)

def lid_pocket():
    sh = rrect2d(4, LY0 - 6, FO_W - 4, LY0 + FO_H - 4, 0, 8)
    return f"translate([0,0,{LID_PF-2.5:.2f}]) linear_extrude(30) {sh}"

def fold_lid(walnut=WAL_P, plate=True, plate_dz=0.0, controls=True, back_detail=True):
    """lid OPEN (lying on its back behind the base): y 88-174."""
    s = f'{c(walnut)} difference(){{ {pebble(0, LY0, FO_W, FO_H, LID_H, 12, 12, 3, 6)} {lid_pocket()} }}\n'
    if plate:
        g = f"translate([0,0,{plate_dz}]) {{\n"
        g += pg_layers(lid_plate2d(), LID_PF)
        gz = LID_PF + 0.02
        for xb in (127.5, 186.0):
            g += box(xb - 0.6, LY0 + 60, gz, xb + 0.6, LY0 + 108, gz + 0.03, "#d3cab8")
        # the band: rectangular speaker's grille (Proof's bars, made rectangular) at x 205-265, d 2-32; signal map left
        for k in range(11):
            yy = LY0 + 5 + k * 2.3
            g += box(208, yy, LID_PF - 0.4, 262, yy + 1.25, LID_PF + 0.03, "#1d1b19")
        g += f'{c(FO_INK)} translate([0,0,{gz}]) linear_extrude(0.04) difference(){{ {rrect2d(40,LY0+18,140,LY0+32,3,3)} {rrect2d(40.45,LY0+18.45,139.55,LY0+31.55,2.6,2.6)} }}\n'   # name, blank
        if controls:
            st = fold_style()
            g += item("EMPHASIS", EMPH[0], LY0 + EMPH[1], "k", False, LID_PF, st, ("EMPH",))
            g += panel(LID_PF, st, xo=FO_XO, vfy=LY0 + VD_F, vby=LY0 + VD_B, parts=("voice",))
            for (tx, name) in [(14, "oscillators"), (132, "mixer"), (191, "contours  ·  filter front, loudness back")]:
                g += txt(tx, LY0 + 103.6, LID_PF + 0.01, name, 2.4, "#8d6b3c", font="Kalam:style=Bold", halign="left")
        g += "}\n"
        s += g
    # jacks in the lid's right wall, below the plate
    for k in range(7):
        y = LY0 + 20 + k * 10
        if k == 6:
            s += box(FO_W - 0.3, y - 4.5, 6.3, FO_W + 0.1, y + 4.5, 9.7, "#1a1a1a")
        else:
            s += f'{c("#151515")} translate([{FO_W-0.25},{y},8]) rotate([0,90,0]) cylinder(h=0.4,d=4.6,$fn=24);\n'
    if back_detail:   # the lid's back (table side open, top face closed): 6 brass countersunk screws + 4 inlaid cork pads
        for (x, y) in [(16, LY0 + 12), (FO_W - 16, LY0 + 12), (16, LY0 + FO_H - 12), (FO_W - 16, LY0 + FO_H - 12), (143, LY0 + 12), (143, LY0 + FO_H - 12)]:
            s += cyl(x, y, -0.06, 0.1, 5.4, "#c2a25e", fn=24) + box(x - 1.8, y - 0.35, -0.1, x + 1.8, y + 0.35, -0.04, "#6a5228")
        for (x, y) in [(40, LY0 + 32), (FO_W - 40, LY0 + 32), (40, LY0 + FO_H - 32), (FO_W - 40, LY0 + FO_H - 32)]:
            s += cyl(x, y, -0.6, 0.6, 12, "#c9a77c", fn=32)
        for (x, y) in [(110, LY0 + FO_H / 2), (176, LY0 + FO_H / 2)]:
            s += cyl(x, y, -0.08, 0.1, 6, "#24170e", fn=24)
    return s

def knuckles(walnut, part):
    """two knuckle hinges at the rear corners; part 'b' (base leaves) or 'l' (lid leaves)."""
    s = ""
    segs = [(1.5, 5.4, "b"), (5.4, 9.1, "l"), (9.1, 13.0, "b"), (273.0, 276.9, "b"), (276.9, 280.6, "l"), (280.6, 284.5, "b")]
    for a, b, who in segs:
        if who != part:
            continue
        s += f'{c(walnut)} translate([{a+0.15},{AX_Y},{AX_Z}]) rotate([0,90,0]) cylinder(h={b-a-0.3},r=4.8,$fn=40);\n'
        if who == "b":
            s += f'{c(walnut)} hull(){{ translate([{a+0.15},{AX_Y},{AX_Z}]) rotate([0,90,0]) cylinder(h={b-a-0.3},r=4.8,$fn=40); translate([{a+0.15},{AX_Y-10},{BASE_H-1}]) cube([{b-a-0.3},8,1]); }}\n'
        else:
            s += f'{c(walnut)} hull(){{ translate([{a+0.15},{AX_Y},{AX_Z}]) rotate([0,90,0]) cylinder(h={b-a-0.3},r=4.8,$fn=40); translate([{a+0.15},{AX_Y+1},{LID_PF}]) cube([{b-a-0.3},8,1]); }}\n'
    for x in (1.4, 284.6):
        if part == "b":
            s += f'{c("#a6a9ad")} translate([{x-0.05},{AX_Y},{AX_Z}]) rotate([0,90,0]) cylinder(h=0.1,r=2.0,$fn=24);\n'
    return s

def fold(open_state=True, walnut=WAL_P, book=False):
    s = fold_base(walnut) + knuckles(walnut, "b")
    lid = fold_lid(walnut) + knuckles(walnut, "l")
    if open_state:
        s += lid
    else:
        s += f'translate([0,{AX_Y},{AX_Z}]) rotate([180,0,0]) translate([0,{-AX_Y},{-AX_Z}]) {{\n{lid}}}\n'
        if book:
            s += hardback(318, -10)
    return s

def fold_exploded(walnut=WAL_P, lift=58.0):
    """open; the base assembled, the lid's pickguard lifted out of its block with everything that hangs from it."""
    s = fold_base(walnut) + knuckles(walnut, "b")
    s += fold_lid(walnut, plate=False) + knuckles(walnut, "l")
    g = f"translate([0,0,{lift}]) {{\n" + pg_layers(lid_plate2d(), LID_PF)
    for k in range(11):
        yy = LY0 + 5 + k * 2.3
        g += box(208, yy, LID_PF - 0.4, 262, yy + 1.25, LID_PF + 0.03, "#1d1b19")
    g += f'{c(FO_INK)} translate([0,0,{LID_PF+0.02}]) linear_extrude(0.04) difference(){{ {rrect2d(40,LY0+18,140,LY0+32,3,3)} {rrect2d(40.45,LY0+18.45,139.55,LY0+31.55,2.6,2.6)} }}\n'
    bz = LID_PF - 2.5 - 7
    g += f'{c("#2f6b4f")} translate([0,0,{bz-1.6}]) linear_extrude(1.6) difference(){{ {rrect2d(12, LY0 + 2, 274, LY0 + FO_H - 6, 0, 4)} translate([203,{LY0}]) square([64,34]); translate([20,{LY0}]) square([134,57]); }}\n'   # lid board, speaker cut-out
    g += box(205, LY0 + 2, LID_PF - 2.5 - 10.3, 265, LY0 + 32, LID_PF - 2.5, "#3b3d40")   # rectangular speaker
    for xa in (24, 88):     # battery bay x 22-152, d 3-55: two pouch cells on JST leads
        g += box(xa, LY0 + 4, LID_PF - 2.5 - 9.5, xa + 60, LY0 + 54, LID_PF - 2.5, "#5d6a7a")
    g += box(EMPH[0] - 4.75, LY0 + EMPH[1] - 4.75, bz, EMPH[0] + 4.75, LY0 + EMPH[1] + 4.75, bz + 7, "#2b55a0")
    for (x, y) in [(10, LY0 + 6), (10, LY0 + FO_H - 10), (276, LY0 + 6), (276, LY0 + FO_H - 10), (165, LY0 + 6), (165, LY0 + FO_H - 10)]:
        g += cyl(x, y, LID_PF - 2.5 - 13, 13, 5.5, "#c9b27a", fn=6)                      # hex standoffs (screws come up from the back)
    for lab, x, k, m in VF + VB:
        if k in "kgr":
            yy = LY0 + (VD_F if (lab, x, k, m) in VF else VD_B)
            g += box(x + FO_XO - 4.75, yy - 4.75, bz, x + FO_XO + 4.75, yy + 4.75, bz + 7, "#2b55a0")   # pot bodies
    g += item("EMPHASIS", EMPH[0], LY0 + EMPH[1], "k", False, LID_PF, fold_style(), ("EMPH",))
    g += panel(LID_PF, fold_style(), xo=FO_XO, vfy=LY0 + VD_F, vby=LY0 + VD_B, parts=("voice",))
    g += "}\n"
    s += g
    s += f'{c("#9aa3ad")} hull(){{ translate([160,{FO_H-6},{BASE_H-3}]) cube([24,1,0.4]); translate([160,{LY0+60},{lift+bz-2}]) cube([24,1,0.4]); }}\n'
    return s

def hardback(x0, y0, wx=235.0, dy=156.0, h=38.0, cloth="#2f4a3e", pages="#efe8d6"):
    from ld import box as B
    import scenes
    return scenes.hardback(x0, y0, wx, dy, h, cloth, pages)

# ------------------------------------------------------------------ footprints (shadows)
def fp_rect(x0, y0, x1, y1):
    return box(x0, y0, 0, x1, y1, 0.2, "#000000")

def top4(scene, name, *box_, felt=False, **kw):
    """orthographic 1:1 top view, re-lit: straight-down light renders whites as mid-grey, so lift it back."""
    import numpy as np
    from PIL import Image
    out = ld.shot_top(scene, name, *box_, **kw)
    if felt:
        feltfill(out)
    im = np.asarray(Image.open(out).convert("RGB")).astype(np.float32)
    bg = np.all(np.abs(im - im[2, 2]) < 3, axis=2)
    lit = np.clip(im * 1.25 + 4, 0, 255)
    im = np.where(bg[..., None], np.array([243, 239, 232], np.float32), lit)
    Image.fromarray(im.astype(np.uint8)).save(out)
    return out

def fp_pebble():
    return ext(rrect2d(5, 5, HU_W - 5, HU_D - 5, 15, 39), 0, 0.2, "#000000")

# ------------------------------------------------------------------ render jobs
def woodfill(png):
    """walnut-tone wood-fill PLA: matte, fine speckle, faint fibre streaks (no figure: it isn't wood yet)."""
    import numpy as np
    from PIL import Image
    im = np.asarray(Image.open(png).convert("RGB")).astype(np.float32)
    r, g, b = [im[..., k] / 255 for k in range(3)]
    mx = np.maximum(np.maximum(r, g), b); mn = np.minimum(np.minimum(r, g), b)
    d = np.maximum(mx - mn, 1e-6)
    hue = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    m = (hue > 14) & (hue < 36) & (sat > 0.42) & (mx > 0.08) & (mx < 0.62)
    h, w = mx.shape
    sp = ld._noise(h, w, 1, 31) * 0.6 + ld._noise(h, w, 3, 32) * 0.4
    st = ld._noise(h, w // 1, 2, 33)
    st = np.asarray(Image.fromarray((st * 255).astype(np.uint8)).resize((w // 14 + 1, h)).resize((w, h))).astype(np.float32) / 255
    f = 0.93 + 0.09 * sp + 0.05 * st
    im = np.where(m[..., None], im * f[..., None], im)
    Image.fromarray(np.clip(im, 0, 255).astype(np.uint8)).save(png)
    return png

def feltfill(png):
    """wool felt, after downsampling: fibre speckle at pixel scale, soft mottling; hides facet banding."""
    import numpy as np
    from PIL import Image, ImageFilter
    img = Image.open(png).convert("RGB")
    im = np.asarray(img).astype(np.float32)
    r, g, b = [im[..., k] / 255 for k in range(3)]
    mx = np.maximum(np.maximum(r, g), b); mn = np.minimum(np.minimum(r, g), b)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    bg = np.all(np.abs(im - im[2, 2]) < 4, axis=2)
    m = (~bg) & (sat < 0.2) & (mx > 0.08) & (mx < 0.85) & (im[..., 2] >= im[..., 0] + 8)
    soft = np.asarray(img.filter(ImageFilter.GaussianBlur(1.2))).astype(np.float32)
    base = np.where(m[..., None], soft, im)
    h, w = mx.shape
    sp = ld._noise(h, w, 1, 41) * 0.65 + ld._noise(h, w, 2, 42) * 0.35
    mot = ld._noise(h, w, 40, 43)
    f = 0.90 + 0.15 * sp + 0.05 * mot
    warm = np.array([1.045, 1.0, 0.94], np.float32)
    out = np.where(m[..., None], base * f[..., None] * warm, im)
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(png)
    return png

def shot4(scene, fp, name, wood=False, felt=False, **kw):
    out = ld.shot(scene, fp, name, **kw)
    if felt:
        feltfill(out)
    return woodfill(out) if wood else out

def under_shot(scene, name, size, az, el, dist, center):
    eye = ld.eye_from(center, az, el, dist)
    raw = ld.render(scene, name, eye, center, size)
    out = ld.finish(raw, None, os.path.join(OUT, name + ".png"), grain_classes=("felt",))
    return feltfill(out) if "hu" in name else out

if __name__ == "__main__":
    SZ = (5200, 3500)
    if "--test" in sys.argv:
        SZ = (1600, 1080); sys.argv.remove("--test")
    J = {
        "r4_hu_main": lambda: shot4(hush(), fp_pebble(), "r4_hu_main", size=SZ, az=-30, el=34, dist=700, center=(145, 82, 12), grain_classes=("felt",), felt=True),
        "r4_hu_low": lambda: shot4(hush(), fp_pebble(), "r4_hu_low", size=SZ, az=-62, el=12, dist=560, center=(120, 60, 12), grain_classes=("felt",), felt=True),
        "r4_hu_under": lambda: under_shot(hush_under(), "r4_hu_under", SZ, -150, -38, 700, (145, 72, 10)),
        "r4_os_main": lambda: ld.shot(one_sheet(), fp_rect(0, 0, OS_W, OS_D), "r4_os_main", size=SZ, az=-30, el=36, dist=680, center=(138, 68, 12), grain_classes=()),
        "r4_os_under": lambda: under_shot(one_sheet_under(), "r4_os_under", SZ, -150, -38, 680, (138, 70, 10)),
        "r4_os_edge": lambda: ld.shot(one_sheet(), fp_rect(0, 0, OS_W, OS_D), "r4_os_edge", size=SZ, az=-58, el=14, dist=420, center=(60, 40, 14), grain_classes=()),
        "r4_fo_main": lambda: shot4(fold(True), fp_rect(0, 0, FO_W, 2 * FO_H + 2), "r4_fo_main", size=SZ, az=-30, el=42, dist=920, center=(143, 116, 12), grain_classes=(), wood=True),
        "r4_fo_closed_wal": lambda: ld.shot(fold(False, walnut=WAL_R, book=True), fp_rect(0, 0, FO_W, FO_H) + fp_rect(318, -10, 553, 146), "r4_fo_closed_wal", size=SZ, az=-26, el=28, dist=1100, center=(275, 60, 22), grain_classes=("walnut",), grain_angle=-25),
        "r4_fo_closed": lambda: shot4(fold(False), fp_rect(0, 0, FO_W, FO_H), "r4_fo_closed", size=SZ, az=-28, el=30, dist=620, center=(143, 58, 22), grain_classes=(), wood=True),
        "r4_fo_exploded": lambda: shot4(fold_exploded(), fp_rect(0, 0, FO_W, 2 * FO_H + 2), "r4_fo_exploded", size=SZ, az=-24, el=36, dist=1000, center=(143, 120, 30), grain_classes=(), wood=True),
        "r4_fo_wal_open": lambda: ld.shot(fold(True, walnut=WAL_R), fp_rect(0, 0, FO_W, 2 * FO_H + 2), "r4_fo_wal_open", size=SZ, az=-30, el=42, dist=920, center=(143, 116, 12), grain_classes=("walnut",), grain_angle=-25),
        # 1:1 top views (orthographic)
        "r4_hu_top": lambda: top4(hush(show_jacks=False), "r4_hu_top", -2, -2, HU_W + 2, HU_D + 2, px_per_mm=12, grain_classes=("felt",), felt=True),
        "r4_os_top": lambda: top4(one_sheet(), "r4_os_top", -2, -2, OS_W + 2, OS_D + 2, px_per_mm=12, grain_classes=()),
        "r4_fo_top": lambda: top4(fold(True), "r4_fo_top", -2, -2, FO_W + 2, 2 * FO_H + 4, px_per_mm=12, grain_classes=()),
    }
    for k in (sys.argv[1:] or J):
        print(J[k]())
