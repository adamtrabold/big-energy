#!/usr/bin/env python3
"""Branches (2026-11-13), concept turn 1: CHAMBER, RAIN, BUTTERFLY, DIPTYCH.

Geometry follows systems' branch docs (design/branches/concepts/*/how-it-works.md, common-how-it-works.md) and
reuses the v1.1 models in r5.py / r4.py unchanged (the board is the constant; only the outside is the branch).
Run: python3 rb.py [--test] [job ...]   Outputs out/rb_*.png.  Cards (phone-first): cards_rb.py.
Coordinates as r5: origin front-left outer corner, x right, y away from the player, z up. mm.
"""
import math, os, sys, random
import ld, r4, r5
from ld import box, cyl, txt, c, toggle, led, ticks
from r4 import rrect2d, ext, knob_black, pg_layers, halo, shot4, top4, MAPLE, MAPLE_DK, WAL_P, WAL_R, FO_INK, K_RED, Style
from r5 import (rows, breaks, item5, draw_row, joystick, keys_raised, fx_heads, F, LAB, OS_W, OS_D, OS_Z, OS_DX, OS_KZ,
                OS_LEG, OS_HEAD_Y, JACKS, OJ0, OJP, FO_W, BASE_H, LID_H, LID_PF, AX_Z, FO_HEAD_D, AT_FLAT_Y, AT_FOLD_D,
                fp_rect, shot_ortho, Fold)

OUT = ld.OUT
HAND = "Kalam:style=Bold"              # installed by systems (~/.local/share/fonts/kalam, OFL)
r5.FAN_OUT_K, r5.FAN_OUT_I = 7.2, 6.6     # outer type-name rows (v1.1 6.5 / 6.2): clear of the raised inner row (checker)
SERIF = "EB Garamond:style=Regular"
SERIF_I = "EB Garamond:style=Italic"

# ------------------------------------------------------------------ shared: FREE / SYNC, TIME's two scales, status hood
SYNC_FLAT = (128.0, 132.7)          # common §2 [CHECK]
SYNC_FOLD_D = (133.0, 70.6)         # lid (x, d)
SYNC_DY_B = 1.5      # checker 7c: 0 at 1.5 / 2.0 / 2.5; 0.64 to FREQ 3 at 0.5
BEHIND_FLAT, BEHIND_FOLD = 159.2, 96.9   # TIME / DECAY legends behind their knobs (common §2 fix 1)
DIVS = ["1/16", "1/8T", "1/16.", "1/8", "1/4T", "1/8.", "1/4", "1/4.", "1/2"]

def sync_toggle(x, y, z, words, size, ink, font, up=False, lever_to="right", dy=0.5):
    """FREE / SYNC: the panel's mini toggle, thrown LEFT / RIGHT (common §2 fix 2); words beside, lever points at one."""
    s = cyl(x, y, z, 1.8, 6.0, "#9a9da1", fn=6) + cyl(x, y, z + 1.8, 1.0, 4.5, "#b9bcbf", fn=24)
    sg = 1 if lever_to == "right" else -1
    s += f'{c("#b9bcbf")} translate([{x:.3f},{y:.3f},{z+2.5:.3f}]) rotate([0,{18*sg},0]) cylinder(h=8, d1=2.6, d2=2.1, $fn=16);\n'
    a, b = words
    s += txt(x - 6.2, y + dy, z, a.upper() if up else a, size, ink, font=font, halign="right")   # 0.5 behind (common rev 2)
    s += txt(x + 6.2, y + dy, z, b.upper() if up else b, size, ink, font=font, halign="left")
    return s

def _tick(x, y, z, r, a, L, w, col):
    return (f'{c(col)} translate([{x:.3f},{y:.3f},{z:.3f}]) rotate([0,0,{-a+90:.2f}]) '
            f'translate([{r:.2f},{-w/2:.3f},0]) cube([{L:.2f},{w:.3f},0.1]);\n')

def time_dial(x, y, z, r, ink_ms, ink_div, font=None, full=False, size=1.05, up=True):
    """TIME's two scales over +-135 deg (common §2): inner ring = ms (log, 20 ms .. 2 s), outer = 9 divisions.
    Dotted = a dot beside the mark, triplet = a small triangle, straight = a tick. full=True adds the numbers (DIPTYCH)."""
    s = ""
    # inner: ms, log, 11 ticks (decade marks longer)
    for i in range(11):
        a = -135 + 27 * i
        s += _tick(x, y, z, r + 0.9, a, 1.0 if i % 5 else 1.4, 0.28 if i % 5 else 0.4, ink_ms)
    # outer: divisions
    for i, d in enumerate(DIVS):
        a = -135 + 33.75 * i
        th = math.radians(a)
        px, py = x + (r + 3.0) * math.sin(th), y + (r + 3.0) * math.cos(th)
        if d.endswith("."):
            s += _tick(x, y, z, r + 2.4, a, 1.2, 0.45, ink_div)
            tx, ty = x + (r + 3.0) * math.sin(th + 0.14), y + (r + 3.0) * math.cos(th + 0.14)
            s += cyl(tx, ty, z, 0.1, 0.75, ink_div, fn=12)
        elif d.endswith("T"):
            s += (f'{c(ink_div)} translate([{px:.3f},{py:.3f},{z:.3f}]) rotate([0,0,{-a:.2f}]) linear_extrude(0.1) '
                  f'polygon([[-0.62,-0.55],[0.62,-0.55],[0,0.6]]);\n')
        else:
            s += _tick(x, y, z, r + 2.4, a, 1.2, 0.45, ink_div)
    if full:
        f = font or "Inter:style=SemiBold"
        for i, lab in ((0, "1/16"), (3, "1/8"), (6, "1/4"), (8, "1/2")):
            a = -135 + 33.75 * i
            th = math.radians(a)
            rr = r + 5.0 if abs(a) < 120 else r + 4.8
            s += txt(x + rr * math.sin(th), y + rr * math.cos(th), z, lab, size, ink_div, font=f)
        for a, lab in ((-148, "20"), (143, "2s")):
            th = math.radians(a)
            s += txt(x + (r + 1.2) * math.sin(th), y + (r + 1.2) * math.cos(th), z, lab, size * 0.9, ink_ms, font=f)
    return s

def status_hood(x, y, z):
    """status LED 3-4 mm down a printed tube (common §3): a dark well with the light deep inside."""
    return cyl(x, y, z - 0.02, 0.06, 6.0, "#121110", fn=36) + cyl(x, y, z - 0.01, 0.05, 3.0, "#7fbf55", fn=24)

def rows_branch(R, row_y, z, st, tap_style, centre, time_st, behind, time_kw, legend_size=None, skip=(), nuts=(),
                back=("REVERB DECAY",)):
    """v1.1 rows, with: TIME's ticks replaced by the two scales; TIME and DECAY legends moved behind their knobs;
    the status light hooded. row_y: {row: y}. behind: y offset of the moved legends from the FX row."""
    s = ""
    ls = legend_size or st.lsize
    for key, yy in row_y.items():
        for name, lab, x, kind, midi, yo in R[key]:
            if name in skip:
                continue
            if name == "ECHO TIME":
                s += item5(name, "" if behind is not None else lab, x, yy, kind, midi, z, time_st, tap_style, None, True, centre)
                s += time_dial(x, yy, z, st.knob_r, **time_kw)
                if behind is not None:
                    s += txt(x, yy + behind, z, lab if st.upper else lab.lower(), ls, st.ink, font=st.font)
            elif name in back and behind is not None:          # back: the other legends moved behind (A: DECAY; CATHEDRAL B: REPEATS)
                s += item5(name, "", x, yy, kind, midi, z, st, tap_style, None, True, centre)
                s += txt(x, yy + behind, z, lab if st.upper else lab.lower(), ls, st.ink, font=st.font)
            elif kind == "k" and st.ticks and (name in NO_TOP_TICK or nuts):
                angs = [-150, -100, -50, 0, 50, 100, 150]
                if name == "OSC 2":
                    angs = [-150, -100, -50, 100, 150]
                elif name == "NOISE/EXT":
                    angs = [-150, -100, 50, 100, 150]
                angs = _ticks_clear(x, yy, angs, st.knob_r + 0.9, st.knob_r + 1.9, nuts)
                s += item5(name, lab, x, yy + yo, kind, midi, z, copy_style(st, ticks=False), tap_style, None, True, centre)
                s += ticks(x, yy, z, st.knob_r + 0.9, angs, st.scale_ink or st.ink, length=1.0, width=0.35)
            elif name == "status":
                s += status_hood(x, yy + yo, z)       # legend beside the hood, not above: above, it crowded MOD MIX (v1.1 near-miss)
                s += txt(x + 4.4, yy + yo, z, lab if st.upper else lab.lower(), st.lsize * 0.8, st.ink, font=st.font, halign="left")
            else:
                tp = r5.ECHO_POS if name == "ECHO TYPE" else r5.VERB_POS
                s += item5(name, lab, x, yy + yo, kind, midi, z, st, tap_style, tp, True, centre)
    return s

NO_TOP_TICK = ("OSC 2", "NOISE/EXT")    # top tick under "free"/"sync"; OSC 2's +50 and NOISE's -50 under the nut (common rev 2)

FAN_IN = 3.8          # inner type-name row (v1.1: 3.4; names sat 0.7-0.9 from their detent ticks, rule 1.0)

def _type_fan(x, y, z, r, pos, ink, font, size, upper, bib=None):
    s = ticks(x, y, z, r + 0.9, [a for a, _ in pos], ink, length=1.5, width=0.5)
    sz = 1.05 if "Inter" in font else 1.3
    for a, w in pos:
        th = math.radians(a)
        row = FAN_IN if abs(a) < 40 else (r5.FAN_OUT_K if "Kalam" in font else r5.FAN_OUT_I)
        s += txt(x + 11.85 * math.sin(th), y + r + row, z, w.upper() if upper else w, sz, ink, font=font)
    return s
r5.type_fan = _type_fan     # branch renders only (rb imports r5; the locked v1.1 renders run r5 directly)

TGL_NUT = 4.6 + 0.5   # spec nut ≈ 9.2 across corners (systems) + the 0.5 tick rule

def _ticks_clear(x, y, angles, r_in, r_out, nuts):
    """keep only ticks whose span stays clear of every toggle nut."""
    keep = []
    for a in angles:
        th = math.radians(a)
        ok = True
        for (nx, ny) in nuts:
            for rr in (r_in, (r_in + r_out) / 2, r_out):
                if math.hypot(x + rr * math.sin(th) - nx, y + rr * math.cos(th) - ny) < TGL_NUT:
                    ok = False
        if ok:
            keep.append(a)
    return keep

def toggle_nuts(R, row_y, extra=()):
    return [(x, yy + yo) for key, yy in row_y.items() for name, lab, x, kind, midi, yo in R[key] if kind == "t"] + list(extra)

def copy_style(st, **kw):
    d = dict(st.__dict__); d.update(kw)
    return Style(**d)

# =================================================================== BUTTERFLY (ONE SHEET): from tool to tree
BONE = "#e2dacb"                 # matte bone / stone PETG (director: try it against the walnut)
BONE_RING = "#c9bfac"
WAL_LEAF = "#6e4628"             # real oiled walnut (grain in post: 'walnut')
SAP = "#b98f62"                  # sapwood band along the live edge
BOG = "#3b2a1e"                  # butterfly: bog oak / wenge
JOINT_Y = 165.0                  # systems [CHECK]: every legend stays on the print

def live_edge(seed=5, n=70):
    """overhang behind the printed rear wall (y 180), 0 .. 12 mm, end-matched: right half mirrors the left about x 138."""
    rng = random.Random(seed)
    xs = [138.0 * i / (n - 1) for i in range(n)]       # left half, x 0..138
    v, vals = 0.0, []
    for i in range(n):
        v += rng.gauss(0, 0.8)
        vals.append(v)
    k = 5
    sm = [sum(vals[max(0, i - k):i + k + 1]) / len(vals[max(0, i - k):i + k + 1]) for i in range(n)]
    lo, hi = min(sm), max(sm)
    prof = []
    for x, v in zip(xs, sm):
        o = 1.5 + 9.0 * (v - lo) / (hi - lo + 1e-9)
        o += 2.5 * math.exp(-((x - 138) / 22) ** 2)      # a gentle crown on the axis (the power legend sits there)
        o *= min(1.0, 0.25 + x / 18.0)                   # tapers into the shell's R 6 corners at the ends
        prof.append((x, max(0.0, min(12.0, o))))
    right = [(276 - x, o) for x, o in reversed(prof)]
    return prof + right[1:]

def butterfly_leaves(z0=18.0, z1=24.0):
    prof = live_edge()
    pts = [(0.0, JOINT_Y)] + [(x, 180.0 + o) for x, o in prof] + [(276.0, JOINT_Y)]
    poly = "polygon([" + ",".join(f"[{x:.2f},{y:.2f}]" for x, y in pts) + "]);"
    clip = f"union(){{ translate([6,{JOINT_Y}]) square([264,40]); {rrect2d(0, 0, OS_W, OS_D, 6, 6)} translate([0,{JOINT_Y}]) square([276,9]); }}"
    leaf = f"intersection(){{ {poly} {clip} }}"
    s = f'{c(WAL_LEAF)} translate([0,0,{z0}]) linear_extrude({z1-z0-0.6:.2f}) {leaf}\n'
    s += f'{c(WAL_LEAF)} translate([0,0,{z1-0.6:.2f}]) linear_extrude(0.6) offset(delta=-0.7) {leaf}\n'   # hand-eased top edge
    # sapwood: a pale band just inside the live edge, on the top (the bark line kept, director)
    band = f"difference(){{ {leaf} translate([0,-3.2]) {leaf} }}"
    s += f'{c(SAP)} translate([0,0,{z1-0.6+0.002:.3f}]) linear_extrude(0.6) offset(delta=-0.7) {band}\n'
    s += box(137.85, JOINT_Y + 0.2, z1 - 0.01, 138.15, 186, z1 + 0.012, "#3a2616")             # the end butt seam
    # the butterfly: one key across the butt, inlaid half the leaf (3 mm), 20 x 10
    bt = "polygon([[-8,-4],[-8,4],[-2.1,1.8],[2.1,1.8],[8,4],[8,-4],[2.1,-1.8],[-2.1,-1.8]]);"
    s += f'{c(BOG)} translate([138,{JOINT_Y+7.5},{z1-0.02:.2f}]) linear_extrude(0.04) {bt}\n'
    # engraved jack legends + ticks, located from the straight joint (one fence)
    for k, lab in enumerate(JACKS):
        x = OJ0 + OJP * k
        s += txt(x, JOINT_Y + 6.2, z1 + 0.02, lab, 1.5, "#2c1b10", font="Inter:style=Bold")
        s += box(x - 0.25, JOINT_Y + 8.6, z1 + 0.01, x + 0.25, JOINT_Y + 11.4, z1 + 0.03, "#2c1b10")
    s += txt(135, 180.0, z1 + 0.02, "POWER", 1.5, "#2c1b10", font="Inter:style=Bold")
    return s

def butterfly(face=True):
    """ONE SHEET edge A in bone, rear band stepped down 6 mm behind y 165, walnut leaves laid in like a tabletop."""
    W, D, Z = OS_W, OS_D, OS_Z
    shell2d = rrect2d(0, 0, W, D, 6, 6)
    win = "translate([3,-1]) square([270,50.5]);"
    sh = f'{c(BONE)} translate([0,0,0.5]) linear_extrude({Z-2-0.5:.2f}) difference(){{ {shell2d} {win} }}\n'
    for zz, inset, hh in ((Z - 2, 0.6, 0.6), (Z - 1.4, 0.0, 0.8), (Z - 0.6, 0.9, 0.6)):
        sh += f'{c(BONE)} translate([0,0,{zz:.2f}]) linear_extrude({hh}) difference(){{ {rrect2d(inset, inset, W-inset, D-inset, 6-inset, 6-inset)} offset(delta={inset}) {win} }}\n'
    s = f"difference(){{ union(){{\n{sh}}}\n translate([-1,{JOINT_Y},18]) cube([{W+2},30,10]); }}\n"
    s += box(3, 0, 0.5, 273, 2.4, 17.5, BONE) + box(3, 2.4, 0.5, 273, 4.0, 15.8, "#1a1816")
    s += f'{c("#c99b62")} linear_extrude(0.5) offset(delta=-2.6) {shell2d}\n'
    if face:
        s += box(0.6, 49.6, Z + 0.004, W - 0.6, JOINT_Y - 0.4, Z + 0.006, BONE)
        R = rows(OS_DX)
        for key, yy in (("P", 68), ("V1", 100), ("V2", 123), ("FX", 146)):
            for name, lab, x, kind, midi, yo in R[key]:
                if kind in "kgryh":
                    r1 = 12.5 if kind == "h" else 9.25
                    r0 = 10.9 if kind == "h" else 7.75
                    s += halo(x, yy, Z + 0.02, r0, r1, BONE, BONE_RING)
    gz, g = Z + 0.05, "#b3a993"
    vb, fb = breaks(OS_DX)
    for xb in vb:
        s += box(xb - 0.6, 52.6, gz, xb + 0.6, 133.5, gz + 0.03, g)
    s += box(4, 85.4 - 0.6, gz, W - 4, 85.4 + 0.6, gz + 0.03, g)
    for xb in fb:
        s += box(xb - 0.6, 138.5, gz, xb + 0.6, 156.5, gz + 0.03, g)
    tz = Z + 0.04
    for (tx, ty, name, ha) in [(vb[0] - 4, 81.0, "PITCH", "right"), (vb[1] - 4, 81.0, "FILTER", "right"), (W - 6, 81.0, "FX & OUT", "right"),
                               (6, 136.0, "OSCILLATORS", "left"), (138, 136.0, "MIXER", "center"), (W - 6, 136.0, "CONTOURS", "right")]:
        s += txt(tx, ty, tz, name, 1.8 if name == "MIXER" else 2.1, OS_LEG, font="Inter:style=Bold", halign=ha)
    s += keys_raised(3, 3, OS_KZ, skirt=True, front_y=0.3)
    st = Style(ink=OS_LEG, lsize=1.9)
    s += cyl(25 + OS_DX, 68, Z - 0.1, 0.16, 18.6, "#efe9dc", fn=72)
    R = rows(OS_DX)
    s += rows_branch(R, {"P": 68, "V1": 100, "V2": 123, "FX": 146, "SW": AT_FLAT_Y}, Z + 0.06, st, "acryl", 138,
                     copy_style(st, ticks=False), BEHIND_FLAT - 146, dict(ink_ms=OS_LEG, ink_div=OS_LEG))
    s += sync_toggle(*SYNC_FLAT, Z + 0.06, ("free", "sync"), 1.9 * 0.72, OS_LEG, "Inter:style=SemiBold", up=True)
    s += fx_heads(OS_DX, OS_HEAD_Y, Z + 0.06, OS_LEG, "Inter:style=Bold", 1.8, True)
    s += r5.os_jacks()
    s += butterfly_leaves()
    return s

def butterfly_hanging():
    """on a wall, tree side up (systems §5): the instrument rotated face-out, a French cleat behind, a plaster wall."""
    s = f"translate([0,0,0]) rotate([90,0,0]) {{\n{butterfly()}}}\n"
    # after rotate([90,0,0]): (x, y, z) -> (x, -z, y). Back panel at world y 0, face at y -24, rear (tree) up at z 180.
    s += box(-120, 0.6, -60, 400, 8, 300, "#e9e3d8")                                 # wall
    s += box(30, -2.0, 150, 210, 0.6, 162, "#cdbb98")                              # cleat strip on the wall (hidden mostly)
    return s

# =================================================================== RAIN (ONE SHEET): a pond after rain
STONE = "#ddd3c1"      # round 2: pale wet stone with warmth (director fix 3: off concrete)
STONE_LN = "#b9ab93"   # deep ring (0.4 deep, near the stone)
STONE_LN2 = "#cbbfaa"  # shallow ring (0.2 deep, outer zone): the depth step is the decay (systems R2.2)
PEG_W, PEG_S = "#aaa192", "#6e675b"   # two warm stone greys (white / black kept)
MUSTARD = "#c9a032"
RAIN_PITCH = float(os.environ.get("RB_RAIN_PITCH", 0.9))

def rain_pegs():
    whites = [(12 + 18 * n, 14.0) for n in range(15)]
    sharps = [(3 + 18 * (i + 1), 36.5) for i in r4.sharps_after()]
    return whites, sharps

def rain_section(x, y, name=""):
    """which part of the map an element belongs to: keys; PLAY pitch / filter / fx; VOICE osc / mixer / contours;
    back row drift / echo / reverb / volume (the v1.1 break lines, ONE SHEET x = FOLD x - 5)."""
    if name == "SYNC":
        return "fx-echo"
    if y < 52:
        return "keys"
    vb = [b + OS_DX for b in F.vb_play]
    col = 0 if x < vb[0] else (1 if x < vb[1] else 2)
    if y < 85.4:
        return "play-%d" % col
    if y < 138.5:
        return "voice-%d" % col
    fb = [b + OS_DX for b in F.vb_fx]
    return "fx-" + ["drift", "echo", "reverb", "volume"][sum(x > b for b in fb)]

def rain_items():
    """every element that breaks the surface: (x, y, r0 = where its ripples start, section)."""
    R = rows(OS_DX)
    out = []
    for key, yy in (("P", 68), ("V1", 100), ("V2", 123), ("FX", 146), ("SW", AT_FLAT_Y)):
        for name, lab, x, kind, midi, yo in R[key]:
            r0 = {"h": 10.9, "t": 3.7, "s": 9.3, "l": 3.7, "b": 7.6}.get(kind, 7.75)
            out.append((x, yy + yo, r0, rain_section(x, yy + yo, name)))
    out.append((SYNC_FLAT[0], SYNC_FLAT[1], 3.7, "fx-echo"))
    w, sh = rain_pegs()
    out += [(x, y, 7.3, "keys") for x, y in w + sh]
    return out

def _clip(poly, a, b, cst):
    """keep a*x + b*y <= cst (Sutherland-Hodgman)."""
    out = []
    n = len(poly)
    for i in range(n):
        P, Q = poly[i], poly[(i + 1) % n]
        fp, fq = a * P[0] + b * P[1] - cst, a * Q[0] + b * Q[1] - cst
        if fp <= 0:
            out.append(P)
        if (fp <= 0) != (fq <= 0):
            t = fp / (fp - fq)
            out.append((P[0] + t * (Q[0] - P[0]), P[1] + t * (Q[1] - P[1])))
    return out

BAND_IN, BAND_OUT = 1.0, 3.0      # still bands: inside a section / between sections (director fix 2: ~3x)

def power_cells(items, x0, y0, x1, y1, bands=True):
    """each element's cell in a power diagram (weights = ring start r0), each edge pulled back by half its still
    band, so the band between two sections is 3x the band inside one: the seams draw the map."""
    cells = []
    for i, it in enumerate(items):
        xi, yi, ri, si = it
        poly = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        for j, jt in enumerate(items):
            if i == j:
                continue
            xj, yj, rj, sj = jt
            a, b = 2 * (xj - xi), 2 * (yj - yi)
            cst = (xj * xj + yj * yj - rj * rj) - (xi * xi + yi * yi - ri * ri)
            if bands:
                half = (BAND_IN if si == sj else BAND_OUT) / 2
                cst -= half * math.hypot(a, b)
            poly = _clip(poly, a, b, cst)
            if not poly:
                break
        cells.append(poly)
    return cells

def text_w(s, size, font_path="/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"):
    from PIL import ImageFont
    f = ImageFont.truetype(font_path, 200)
    return f.getlength(s) / 200 * size * 1.30     # OpenSCAD size ~ cap height; Inter caps ~0.73 em [rough]

def rain_legends():
    """(x, y, text, size, halign) for every printed word, so each gets a smooth lily pad."""
    st_l = 1.9
    R = rows(OS_DX)
    L = []
    full = {"ECHO TYPE": "ECHO TYPE", "REVERB TYPE": "REVERB TYPE"}
    for key, yy in (("P", 68), ("V1", 100), ("V2", 123), ("FX", 146), ("SW", AT_FLAT_Y)):
        for name, lab, x, kind, midi, yo in R[key]:
            lab = full.get(name, lab)
            if kind in "kgryh":
                r = 10.4 if kind == "h" else 7.45
                if name in ("ECHO TIME", "REVERB DECAY"):
                    L.append((x, BEHIND_FLAT, lab, st_l, "center"))
                else:
                    L.append((x, yy - r - 3.2 - 0.6, lab, st_l, "center"))
                if kind == "y":
                    pos = r5.ECHO_POS if name == "ECHO TYPE" else r5.VERB_POS
                    for a, w in pos:
                        th = math.radians(a)
                        row = 3.4 if abs(a) < 40 else r5.FAN_OUT_I
                        L.append((x + 11.85 * math.sin(th), yy + r + row, w.upper(), 1.05, "center"))
            elif kind == "t":
                if name in r5.SW_NAMES:
                    if lab:
                        right = (x < 138)
                        L.append((x + 6.2 if right else x - 6.2, yy, lab.upper(), st_l * 0.72, "left" if right else "right"))
                else:
                    L.append((x, yy + 7.4, lab.upper(), st_l * 0.85, "center"))
            elif kind == "b":
                L.append((x, yy - 6 - 3.2 - 0.6, "TAP", st_l, "center"))
            elif kind == "s":
                L.append((x, yy - 11.5, lab.upper(), st_l, "center"))
            elif kind == "l" and lab:
                L.append((x + 4.4, yy + yo, lab.upper(), st_l * 0.8, "left"))
    L.append((SYNC_FLAT[0] - 6.2, SYNC_FLAT[1], "FREE", st_l * 0.72, "right"))
    L.append((SYNC_FLAT[0] + 6.2, SYNC_FLAT[1], "SYNC", st_l * 0.72, "left"))
    for k, lab in enumerate(JACKS):
        L.append((OJ0 + OJP * k, OS_D - 9.0, lab, 1.5, "center"))
    L.append((OJ0 - 17, OS_D - 9.0, "POWER", 1.5, "center"))
    return L

def pad2d(x, y, s, size, ha, m=0.85):
    w = text_w(s, size)
    x0 = x - w / 2 if ha == "center" else (x if ha == "left" else x - w)
    return rrect2d(x0 - m, y - size / 2 - m, x0 + w + m, y + size / 2 + m, 1.2, 1.2)

def _cell(items, i, x0, y0, x1, y1, extra=0.0):
    """element i's cell; every internal edge pulled back by half its still band + `extra` (the outer edge isn't)."""
    xi, yi, ri, si = items[i]
    poly = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    for j, (xj, yj, rj, sj) in enumerate(items):
        if i == j:
            continue
        a, b = 2 * (xj - xi), 2 * (yj - yi)
        cst = (xj * xj + yj * yj - rj * rj) - (xi * xi + yi * yi - ri * ri)
        cst -= ((BAND_IN if si == sj else BAND_OUT) / 2 + extra) * math.hypot(a, b)
        poly = _clip(poly, a, b, cst)
        if not poly:
            break
    # director R1: the panel's edge is still water like every seam, so the fade finishes there too
    e = BAND_OUT / 2 + extra
    for (a, b, cst) in ((-1, 0, -(x0 + e)), (1, 0, x1 - e), (0, -1, -(y0 + e)), (0, 1, y1 - e)):
        if poly:
            poly = _clip(poly, a, b, cst)
    return poly

def _internal_reach(items, i, cell, W, D):
    """median distance from the element to its cell's internal edges (edges not on the panel's outline)."""
    x, y = items[i][0], items[i][1]
    ds = []
    n = len(cell)
    for k in range(n):
        (ax, ay), (bx, by) = cell[k], cell[(k + 1) % n]
        on_edge = (abs(ax - bx) < 1e-6 and (abs(ax) < 1e-6 or abs(ax - W) < 1e-6)) or \
                  (abs(ay - by) < 1e-6 and (abs(ay) < 1e-6 or abs(ay - D) < 1e-6))
        if on_edge:
            continue
        L = math.hypot(bx - ax, by - ay)
        if L < 1e-6:
            continue
        ds.append(abs((bx - ax) * (ay - y) - (by - ay) * (ax - x)) / L)
    ds.sort()
    return ds[len(ds) // 2] if ds else 20.0

def _poly(cell):
    return "polygon([" + ",".join(f"[{px:.3f},{py:.3f}]" for px, py in cell) + "]);"

def rain_field(z, pitch=RAIN_PITCH, groove=0.45):
    """ripples that lose amplitude toward the still bands (director fix 1, built the way a printer can: systems R2.2):
    near each stone, deep rings (0.4) at `pitch`; further out, shallow rings (0.2) at 2 x pitch; then smooth water
    up to the band. Bands: 1.0 inside a section, 3.0 between sections (fix 2). Toward the panel's outline the rings
    run on to the edge, over the chamfer (fix 3). Two finishes only: smooth, and rings."""
    items = rain_items()
    W, D = OS_W, OS_D
    deep_p, shal_p = [], []
    for i, (x, y, r0, sec) in enumerate(items):
        base = _cell(items, i, 0, 0, W, D)
        if len(base) < 3:
            continue
        span = max(_internal_reach(items, i, base, W, D) - r0, 0.5)
        zA = _cell(items, i, 0, 0, W, D, extra=max(0.0, span - max(min(span, 2.4), 0.5 * span)))   # deep: >= 2-3 rings hug every stone
        zB = _cell(items, i, 0, 0, W, D, extra=0.14 * span)        # shallow zone ends short of the band
        rmax = max(math.hypot(px - x, py - y) for px, py in base) + 1
        REACH = {"deep": 3.5, "shallow": 7.0}     # director R1: rings die out ~7 mm out; beyond is a still pool
        def rings(p):
            lim = min(rmax, r0 + (REACH["deep"] if p == pitch else REACH["shallow"]))
            rs, r = [], r0 + 0.25 + groove / 2
            while r < lim:
                rs.append(r); r += p
            return "union(){ " + " ".join(f"difference(){{ circle(r={r + groove/2:.3f}); circle(r={r - groove/2:.3f}); }}" for r in rs) + " }"
        if len(zA) >= 3:
            deep_p.append(f"intersection(){{ {_poly(zA)} translate([{x:.3f},{y:.3f}]) {rings(pitch)} }}")
        if len(zB) >= 3:
            outer = f"difference(){{ {_poly(zB)} {_poly(zA)} }}" if len(zA) >= 3 else _poly(zB)
            shal_p.append(f"intersection(){{ {outer} translate([{x:.3f},{y:.3f}]) {rings(2 * pitch)} }}")
    pads = "".join(pad2d(*L) for L in rain_legends())
    outline = rrect2d(0.25, 0.25, W - 0.25, D - 0.25, 5.8, 5.8)
    out = ""
    for col, ps in ((STONE_LN2, shal_p), (STONE_LN, deep_p)):
        field = f"intersection(){{ {outline} difference(){{ union(){{ {' '.join(ps)} }} union(){{ {pads} }} }} }}"
        out += f'{c(col)} translate([0,0,{z:.3f}]) linear_extrude(0.03) {field}\n'
    return out

def rain(field=True):
    W, D, Z = OS_W, OS_D, OS_Z
    shell2d = rrect2d(0, 0, W, D, 6, 6)
    s = f'{c(STONE)} translate([0,0,0.5]) linear_extrude({Z-2-0.5:.2f}) {shell2d}\n'
    for zz, inset, hh in ((Z - 2, 0.6, 0.6), (Z - 1.4, 0.0, 0.8), (Z - 0.6, 0.9, 0.6)):
        s += f'{c(STONE)} translate([0,0,{zz:.2f}]) linear_extrude({hh}) {rrect2d(inset, inset, W-inset, D-inset, 6-inset, 6-inset)}\n'
    s += f'{c("#a39784")} linear_extrude(0.5) offset(delta=-2.6) {shell2d}\n'
    if field:
        s += rain_field(Z + 0.01)
    # pegs: stepping stones, on 14 mm felt washers in the deck
    whites, sharps = rain_pegs()
    for (pts, col, lift) in ((whites, PEG_W, 0.0), (sharps, PEG_S, 0.0)):
        for x, y in pts:
            s += cyl(x, y, Z - 0.15, 0.2, 14.0, "#4a4844", fn=48)
            s += cyl(x, y, Z, 2.6, 7.0, "#8b877b", fn=24)
            s += (f'{c(col)} hull(){{ translate([{x},{y},{Z+2.5}]) cylinder(h=2.2,d=12.7,$fn=48); '
                  f'translate([{x},{y},{Z+4.7}]) scale([1,1,0.28]) sphere(d=12.7,$fn=48); }}\n')
    st = Style(ink=OS_LEG, lsize=1.9, hero=lambda x, y, z, a: ld.knob_hero(x, y, z, a, col=MUSTARD, line="#3b2f12"))
    s += cyl(25 + OS_DX, 68, Z - 0.1, 0.16, 18.6, "#e6e3d8", fn=72)
    R = rows(OS_DX)
    # full back-row legends (no section headings in RAIN)
    for k in ("FX",):
        R[k] = [(n, {"ECHO TYPE": "ECHO TYPE", "REVERB TYPE": "REVERB TYPE"}.get(n, lab), x, kind, midi, yo)
                for n, lab, x, kind, midi, yo in R[k]]
    s += rows_branch(R, {"P": 68, "V1": 100, "V2": 123, "FX": 146, "SW": AT_FLAT_Y}, Z + 0.06, st, "acryl", 138,
                     copy_style(st, ticks=False), BEHIND_FLAT - 146, dict(ink_ms=OS_LEG, ink_div=OS_LEG),
                     nuts=toggle_nuts(R, {"P": 68, "V1": 100, "V2": 123, "FX": 146, "SW": AT_FLAT_Y}, [SYNC_FLAT]))
    s += sync_toggle(*SYNC_FLAT, Z + 0.06, ("free", "sync"), 1.9 * 0.72, OS_LEG, "Inter:style=SemiBold", up=True)
    tz = Z + 0.04
    for k, lab in enumerate(JACKS):
        s += txt(OJ0 + OJP * k, D - 9.0, tz, lab, 1.5, OS_LEG, font="Inter:style=Bold")
    s += txt(OJ0 - 17, D - 9.0, tz, "POWER", 1.5, OS_LEG, font="Inter:style=Bold")
    s += r5.os_jacks()
    return s

# =================================================================== FOLD branches: CHAMBER and DIPTYCH
WAL_DK = "#5d3a22"
NAME_D = 94.6

class Branch(Fold):
    """FOLD-105 with the shared branch changes: SYNC on the lid, TIME's two scales, TIME/DECAY legends behind, hood."""
    AXZ = AX_Z
    LIDH = LID_H

    def __init__(self):
        super().__init__(105)

    def style(self):
        return copy_style(r5.fold_style(), font=HAND)     # Kalam isn't installable here: same stand-in everywhere

    def lid_ink(self):
        return FO_INK

    def time_kw(self):
        return dict(ink_ms=FO_INK, ink_div=FO_INK)

    def pegs(self):
        return False

    def base(self, walnut=WAL_P):
        D = self.D
        s = ""
        pocket = f"translate([0,0,11]) linear_extrude(10) {rrect2d(4, 4, FO_W-4, D-4, 0, 8)}"
        s += f'{c(walnut)} difference(){{ {r4.pebble(0, 0, FO_W, D, BASE_H, 12, 12, 3, 6)} {pocket} }}\n'
        st = self.style()
        if self.pegs():
            plate = self.peg_plate2d()
            s += pg_layers(plate, BASE_H)
            s += self.peg_keys(walnut)
        else:
            s += box(8, 4.4, 11, 278, 51, 12.6, "#0e0d0c")
            s += pg_layers(self.base_plate2d(), BASE_H)
            s += r4.keys_flat(8, 4.5, 17.5, bed_z=12.6)
        gz = BASE_H + 0.02
        for xb in F.vb_play:
            s += box(xb - self.RULE_HW, 53.5, gz, xb + self.RULE_HW, D - 5.5, gz + 0.03, self.rule_col())
        s += cyl(25, 68, BASE_H - 0.05, 0.08, 18.6, "#e6dfcf", fn=72)
        s += rows_branch({"P": self.play_row()}, {"P": 68}, BASE_H, st, "proof", 143, st, 0, self.time_kw())
        s += self.base_names()
        s += f'{c("#c2a25e")} translate([142.6,-0.1,7.5]) cube([0.8,0.3,4]);\n'
        s += box(FO_W - 0.3, r5.FO_USB_Y - 4.5, 4.8, FO_W + 0.1, r5.FO_USB_Y + 4.5, 8.2, "#1a1a1a")
        for my in (r5.FO_MIDI_IN_Y, r5.FO_MIDI_Y):
            s += f'{c("#151515")} translate([{FO_W-0.25},{my},6.5]) rotate([0,90,0]) cylinder(h=0.4,d=4.6,$fn=24);\n'
        s += self.base_extra(walnut)
        return s

    def rule_col(self):
        return "#d3cab8"

    RULE_HW = 0.6

    # ---- hooks (CATHEDRAL overrides them)
    def peg_plate2d(self):
        return r4.rrect2d(4.3, 4.0, FO_W - 4.3, self.D - 4.3, 0, 7.7)

    def play_row(self):
        return rows(0)["P"]

    def lid_rows(self):
        return rows(0)

    def fx_breaks(self):
        return F.vb_fx

    def voice_rule_end(self):
        return 9.0

    def sync_pos(self):
        return SYNC_FOLD_D

    def behind(self):
        return BEHIND_FOLD - self.dFX

    def behind_names(self):
        return ("REVERB DECAY",)

    def sync_dy(self):
        return 0.5

    def grille(self, L0):
        g0, g1 = self.p["grille"]
        out = ""
        for k in range(int((g1 - g0) / 2.3)):
            yy = L0 + g0 + k * 2.3
            out += box(118, yy, LID_PF - 0.4, 168, yy + 1.25, LID_PF + 0.03, "#1d1b19")
        return out

    def base_names(self):
        return "".join(txt(tx, 85.0, BASE_H + 0.01, n, 2.4, FO_INK, font=HAND, halign="left")
                       for tx, n in [(14, "pitch"), (105.5, "filter"), (188.5, "effects & out")])

    def base_extra(self, walnut):
        return ""

    def lid(self, walnut=WAL_P, plate=True, back_detail=True, controls=True, lift=0.0, stowed=True):
        D, L0 = self.D, self.LY0
        sh = rrect2d(4, L0 - 6, FO_W - 4, L0 + D - 4, 0, 8)
        pocket = f"translate([0,0,{LID_PF-2.5:.2f}]) linear_extrude(40) {sh}"
        s = f'{c(walnut)} difference(){{ {r4.pebble(0, L0, FO_W, D, self.LIDH, 12, 12, 3, 6)} {pocket} }}\n'
        if plate:
            s += self.lid_face(controls)
        yw = L0 + D
        s += box(r5.FO_IO_PWR - 5, yw - 0.3, 5.5, r5.FO_IO_PWR + 5, yw + 0.1, 9.5, "#2a2826")
        for x in r5.FO_IO_JACKS:
            s += f'{c("#151515")} translate([{x},{yw-0.25},7.5]) rotate([-90,0,0]) cylinder(h=0.4,d=4.6,$fn=24);\n'
        s += self.lid_ends(stowed)
        if back_detail:
            s += self.lid_back(walnut)
        return s

    def lid_ends(self, stowed):
        s = ""
        for xs in ((-0.06, FO_W - 0.2) if stowed else ()):
            s += box(xs, self.LY0 + 30, 2.0, xs + 0.26, self.LY0 + 30 + Fold.STAY_L, 10.0, "#c2a25e")
        return s

    def lid_back(self, walnut):
        L0, D = self.LY0, self.D
        s = ""
        for (x, y) in [(16, L0 + 12), (FO_W - 16, L0 + 12), (16, L0 + D - 12), (FO_W - 16, L0 + D - 12), (143, L0 + 12), (143, L0 + D - 12)]:
            s += cyl(x, y, -0.06, 0.1, 5.4, "#c2a25e", fn=24) + box(x - 1.8, y - 0.35, -0.1, x + 1.8, y + 0.35, -0.04, "#6a5228")
        for (x, y) in [(40, L0 + 30), (FO_W - 40, L0 + 30), (40, L0 + D - 30), (FO_W - 40, L0 + D - 30)]:
            s += cyl(x, y, -0.6, 0.6, 12, "#c9a77c", fn=32)
        return s

    def lid_face(self, controls=True):
        D, L0 = self.D, self.LY0
        s = pg_layers(self.lid_plate2d(), LID_PF)
        gz = LID_PF + 0.02
        for xb in F.vb_voice:
            s += box(xb - self.RULE_HW, L0 + 0.8, gz, xb + self.RULE_HW, L0 + self.dV2 + self.voice_rule_end(), gz + 0.03, self.rule_col())
        for xb in self.fx_breaks():
            s += box(xb - self.RULE_HW, L0 + self.dFX - 9, gz, xb + self.RULE_HW, L0 + self.dFX + 9, gz + 0.03, self.rule_col())
        s += self.grille(L0)
        s += self.name_mark(gz)
        if controls:
            st = self.style()
            R = self.lid_rows()
            ink = self.lid_ink()
            sx, sd = self.sync_pos()
            ry = {"V1": L0 + self.dV1, "V2": L0 + self.dV2, "FX": L0 + self.dFX}
            nuts = toggle_nuts(R, ry, [(sx, L0 + sd)] + [(x, L0 + AT_FOLD_D) for n, l, x, k, m, yo in R["SWF"]])
            s += rows_branch(R, ry, LID_PF, st, "proof", 143, copy_style(st, ticks=False), self.behind(), self.time_kw(), nuts=nuts,
                               back=self.behind_names())
            s += self.sw_row(R, L0, st)
            s += sync_toggle(sx, L0 + sd, LID_PF, ("free", "sync"), st.lsize * 0.72, ink, st.font, up=st.upper,
                             dy=self.sync_dy())
            s += self.lid_names(gz)
            s += self.lid_extra(gz)
        return s

    def sw_row(self, R, L0, st):
        return draw_row(R["SWF"], L0 + AT_FOLD_D, LID_PF, st, "proof", sw_in=False)

    def name_mark(self, gz):
        L0 = self.LY0
        nz = L0 + NAME_D      # 16 x 5 on the axis, between the moved TIME and DECAY legends (the 32 x 6 no longer fits)
        return (f'{c(FO_INK)} translate([0,0,{gz}]) linear_extrude(0.04) difference(){{ {rrect2d(135,nz,151,nz+5,2.5,2.5)} '
                f'{rrect2d(135.4,nz+0.4,150.6,nz+4.6,2.1,2.1)} }}\n')

    def lid_names(self, gz):
        L0 = self.LY0
        s = fx_heads(0, L0 + self.dFX + FO_HEAD_D + 1.2, LID_PF + 0.01, FO_INK, HAND, 2.0, False)
        for (tx, name, ha) in [(14, "oscillators", "left"), (143, "mixer", "center"), (272, "contours", "right")]:
            s += txt(tx, L0 + self.dV1 + 11.3, LID_PF + 0.01, name, 2.4, FO_INK, font=HAND, halign=ha)
        return s

    def lid_extra(self, gz):
        return ""

    def knuckles(self, walnut, part):
        s = ""
        AY = self.AX_Y
        segs = [(0.6, 3.6, "b"), (3.6, 6.6, "l"), (6.6, 9.6, "b"), (276.4, 279.4, "b"), (279.4, 282.4, "l"), (282.4, 285.4, "b")]
        for a, b, who in segs:
            if who != part:
                continue
            s += f'{c(walnut)} translate([{a+0.15},{AY},{self.AXZ}]) rotate([0,90,0]) cylinder(h={b-a-0.3},r=4.8,$fn=40);\n'
            if who == "b":
                s += f'{c(walnut)} hull(){{ translate([{a+0.15},{AY},{self.AXZ}]) rotate([0,90,0]) cylinder(h={b-a-0.3},r=4.8,$fn=40); translate([{a+0.15},{AY-10},{BASE_H-1}]) cube([{b-a-0.3},8,1]); }}\n'
            else:
                s += f'{c(walnut)} hull(){{ translate([{a+0.15},{AY},{self.AXZ}]) rotate([0,90,0]) cylinder(h={b-a-0.3},r=4.8,$fn=40); translate([{a+0.15},{AY+1},{LID_PF}]) cube([{b-a-0.3},8,1]); }}\n'
        return s

    def rot(self, ang, body):
        return f'translate([0,{self.AX_Y},{self.AXZ}]) rotate([{ang},0,0]) translate([0,{-self.AX_Y},{-self.AXZ}]) {{\n{body}}}\n'

    def stand_extra(self, walnut):
        """v1.1 brass stays (the default)."""
        a = math.radians(self.STAND)
        vy, vz = self.LY0 + 30 - self.AX_Y, -self.AXZ
        py = self.AX_Y + vy * math.cos(a) - vz * math.sin(a); pz = self.AXZ + vy * math.sin(a) + vz * math.cos(a)
        ty = py + math.sqrt(max(1, self.STAY_L ** 2 - pz ** 2))
        s = ""
        for x0 in (0.3, FO_W - 3.3):
            s += f'{c(METALS[getattr(self, "metal", "brass")][1])} hull(){{ translate([{x0},{py},{pz}]) rotate([0,90,0]) cylinder(h=3,r=4,$fn=24); translate([{x0},{ty-1.5},4]) rotate([0,90,0]) cylinder(h=3,r=4,$fn=24); }}\n'
            s += cyl(x0 + 1.5, ty - 1.5, 0, 3.0, 9.0, "#1e1e1e", fn=24)
        return s

    def model(self, state=True, walnut=WAL_P, book=False):
        s = self.base(walnut) + self.knuckles(walnut, "b")
        lid = self.lid(walnut, stowed=(state != "stand")) + self.knuckles(walnut, "l")
        if state == "stand":
            return s + self.rot(self.STAND, lid) + self.stand_extra(walnut)
        if state is True or state == "open":
            return s + lid
        s += self.rot(180, lid)
        if book:
            s += r4.hardback(318, -10)
        return s

# ------------------------------------------------------------------ CHAMBER: closed an organ case, open a console
class Chamber(Branch):
    AXZ = AX_Z + 1.3          # lid walls +2.6 (systems §3): closed 52.7
    LIDH = LID_H + 2.6
    SPINE = "#6b2c23"         # bookcloth spine (systems R2.1), oxblood: the cloth an organ case shows behind its pipes

    def __init__(self, fallback=False):
        super().__init__()
        self.fallback = fallback          # director fix 3: maple naturals, walnut sharps (geometry identical)

    def lid_face(self, controls=True):
        old = r5.ABOVE_GAP
        r5.ABOVE_GAP = self.vel_gap()     # systems R2.3: "velocity" clear of the VEL nut
        try:
            return super().lid_face(controls)
        finally:
            r5.ABOVE_GAP = old

    def pegs(self):
        return True

    def vel_gap(self):
        return 7.7

    def peg_keys(self, walnut):
        """reverse pegs (systems §2): naturals walnut (the body's own), sharps maple; 14 mm felt washers; head top +6.5."""
        z = BASE_H
        s = ""
        nat_c, sh_c = (MAPLE, WAL_DK) if self.fallback else (walnut, MAPLE)
        for n in range(15):
            x, y = 17 + 18 * n, 13.5
            s += self.peg(x, y, z, nat_c, nat=not self.fallback)
        for i in r4.sharps_after():
            s += self.peg(8 + 18 * (i + 1), 36.0, z, sh_c, nat=self.fallback)
        return s

    @staticmethod
    def peg(x, y, z, col, nat):
        s = cyl(x, y, z - 0.15, 0.2, 14.0, "#3e3b38", fn=48)
        s += cyl(x, y, z, 2.6, 7.0, "#c7a679" if not nat else "#4e311d", fn=24)
        # head + dome as ONE hull: two touching meshes left a hairline crack that rendered as a white streak (director fix 5)
        s += (f'{c(col)} hull(){{ translate([{x},{y},{z+2.5}]) cylinder(h=2.2,d=12.7,$fn=48); '
              f'translate([{x},{y},{z+4.7}]) scale([1,1,0.28]) sphere(d=12.7,$fn=48); }}\n')
        return s

    def lid_back(self, walnut):
        """the facade: 25 pipes, length = 66 x 2^(-n/12), organ builders' tower about x 143, feet on an impost at d 18.
        Engraved line work with brass-tone fill (first build: printed relief). No shading, no tracery (director)."""
        L0, D = self.LY0, self.D
        z = -0.07
        brass = "#e2bf6a"
        s = ""
        IMP = L0 + 18.0
        s += box(30, IMP - 0.35, z - 0.03, 256, IMP + 0.35, z, brass)          # impost line
        s += box(30, IMP - 8.35, z - 0.03, 256, IMP - 7.65, z, brass)          # plinth line (the screws sit between)
        for n in range(25):
            k = (n + 1) // 2 * (1 if n % 2 else -1)
            x = 143 + 8.75 * k                       # systems R2.2: pitch 10 -> 8.75, pipes 7 / 8 on the board bridges
            L = 66.0 * 2 ** (-n / 12)
            s += self.pipe(x, IMP, L, z, brass)
        for x in (108.0, 178.0):                     # their mouths are the push-out holes: real, Ø 4
            s += cyl(x, L0 + 28.3, -0.2, 0.3, 4.0, "#0f0b08", fn=32)
        for (x, y) in [(16, L0 + 12), (FO_W - 16, L0 + 12), (143, L0 + 12), (16, L0 + D - 12), (FO_W - 16, L0 + D - 12), (143, L0 + D - 12)]:
            s += cyl(x, y, -0.06, 0.1, 5.4, "#c2a25e", fn=24) + box(x - 1.8, y - 0.35, -0.1, x + 1.8, y + 0.35, -0.04, "#6a5228")
        for (x, y) in [(40, L0 + 6), (FO_W - 40, L0 + 6), (40, L0 + D - 30), (FO_W - 40, L0 + D - 30)]:   # front feet moved to d 6
            s += cyl(x, y, -0.6, 0.6, 12, "#2a2522", fn=32)
        return s

    @staticmethod
    def pipe(x, y0, L, z, col, w=6.4, foot=9.0, lw=0.6):
        """one flue pipe as line work: conical foot, mouth (a low arch), body, flat top."""
        s = ""
        def seg(x1, y1, x2, y2):
            dx, dy = x2 - x1, y2 - y1
            ln = math.hypot(dx, dy); a = math.degrees(math.atan2(dy, dx))
            return (f'{c(col)} translate([{x1:.3f},{y1:.3f},{z-0.03:.3f}]) rotate([0,0,{a:.2f}]) '
                    f'translate([0,{-lw/2},0]) cube([{ln+lw/2:.3f},{lw},0.03]);\n')
        yt = y0 + L
        ym = y0 + foot
        s += seg(x - 1.0, y0, x - w / 2, ym) + seg(x + 1.0, y0, x + w / 2, ym)       # foot
        s += seg(x - w / 2, ym, x - w / 2, yt) + seg(x + w / 2, ym, x + w / 2, yt)   # body
        s += seg(x - w / 2, yt, x + w / 2, yt)                                        # top
        s += seg(x - w / 2, ym, x + w / 2, ym)                                        # languid line
        s += seg(x - 1.9, ym, x, ym + 2.6) + seg(x, ym + 2.6, x + 1.9, ym)            # the mouth's upper lip
        return s

    def spine_closed(self):
        """closed: the taut spine closes the hinge-side slot (x 10.5-275.5, from the base plate z 15.6 to the lid plate)."""
        top = 2 * self.AXZ - (LID_PF - 2.5)       # up over the plate's edge to the lid body, so no white line shows
        return box(10.5, self.AX_Y - 1.2, BASE_H - 0.4, 275.5, self.AX_Y - 0.4, top, self.SPINE)

    def spine_stand(self):
        """standing: ~9 mm of slack drapes in the opened gap behind the PLAY row, like a book's joint."""
        a = math.radians(self.STAND)
        vy, vz = self.LY0 - self.AX_Y, LID_PF - self.AXZ        # lid hinge-top edge, rotated up with the lid
        p1 = (self.AX_Y + vy * math.cos(a) - vz * math.sin(a), self.AXZ + vy * math.sin(a) + vz * math.cos(a))
        p0 = (self.D, BASE_H)
        mid = ((p0[0] + p1[0]) / 2 + 1.0, min(p0[1], p1[1]) - 6.5)
        pts = []
        for i in range(13):
            t = i / 12
            pts.append(((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * mid[0] + t * t * p1[0],
                        (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * mid[1] + t * t * p1[1]))
        prof = pts + [(y, z - 0.8) for y, z in reversed(pts)]
        poly = ",".join(f"[{y:.3f},{z:.3f}]" for y, z in prof)
        return f'{c(self.SPINE)} translate([10.5,0,0]) rotate([90,0,90]) linear_extrude(265) polygon([{poly}]);\n'

    def model(self, state=True, walnut=WAL_P, book=False):
        s = super().model(state, walnut, book)
        if state is False:
            s += self.spine_closed()
        elif state == "stand":
            s += self.spine_stand()
        return s

    def lid_extra(self, gz):
        """RANGE in feet, serif (graphics only). Round the knob the side labels collide at 20 pitch (found in the 1:1
        crop), so, like the TYPE fan: 16' 8' in a low row above, 32' 4' in a higher row, lo and 2' under the end ticks."""
        L0 = self.LY0
        s = ""
        y0 = L0 + self.dV1
        for name, x, r, k in F.v1:
            if not name.startswith("RANGE"):
                continue
            R = 7.25
            for a, lab, row in ((-25, "16'", 3.4), (25, "8'", 3.4), (-75, "32'", 6.0), (75, "4'", 6.0)):
                th = math.radians(a)
                xo = 11.85 * math.sin(th) if abs(a) < 40 else 8.3 * (1 if a > 0 else -1)
                s += txt(x + xo, y0 + R + row, LID_PF + 0.01, lab, 1.2, FO_INK, font=SERIF)
            for a, lab in ((-138, "lo"), (138, "2'")):      # beside the end ticks, clear of "range" (checker R2 run)
                th = math.radians(a)
                s += txt(x + 10.4 * math.sin(th), y0 + 10.4 * math.cos(th), LID_PF + 0.01, lab, 1.2, FO_INK, font=SERIF)
        return s

    def lid_names(self, gz):
        L0 = self.LY0
        s = fx_heads(0, L0 + self.dFX + FO_HEAD_D + 1.2, LID_PF + 0.01, FO_INK, HAND, 2.0, False)
        for (tx, name, ha, dd) in [(14, "oscillators", "left", 17.5), (143, "mixer", "center", 11.3), (272, "contours", "right", 17.5)]:
            s += txt(tx, L0 + self.dV1 + dd, LID_PF + 0.01, name, 2.4, FO_INK, font=HAND, halign=ha)   # mixer stays under the grille
        return s

    def sw_row(self, R, L0, st):
        """PARA's legend moves above its toggle and shortens ("mono / para / +4"): beside it, it sat on RANGE 3's 4'."""
        s = ""
        for name, lab, x, kind, midi, yo in R["SWF"]:
            y = L0 + AT_FOLD_D
            if name.startswith("PARA"):
                s += toggle(x, y, LID_PF) + txt(x, y + 7.4, LID_PF, "mono / para / +4", st.lsize * 0.72, st.ink, font=st.font)
            else:
                s += item5(name, lab, x, y, "t", False, LID_PF, st, "proof", None, False, 143, False)
        return s

# ------------------------------------------------------------------ CATHEDRAL (owner 14:12-14:18): CHAMBER x FOLD v1.1
EBONY, BONE = "#1d1b1a", "#ece4d2"
PALETTES = {                       # (naturals, sharps): owner: "too many colours, the brown feels out of place"
    "walnut-maple": (WAL_P, MAPLE),        # CHAMBER rev 2, for reference
    "ebony-maple": (EBONY, MAPLE),         # the organ's own convention, no brown: black like the knobs, light like the plate
    "maple-ebony": (MAPLE, EBONY),         # a piano's light / dark
    "ebony": (EBONY, EBONY),               # one colour: the keys join the knobs
    "maple": (MAPLE, MAPLE),               # one colour: the keys join the plate and TAP
}
# turn 2 (visual, after systems §10-11): pegs from REAL parts only. (head, neck) per row. The neck is the printed
# carrier's 2.8 mm stem under a bought plug (black filament, so it reads as the deck hole's shadow), or the peg's own
# body when the peg is printed in one piece.
BIRCH, BIRCH_BLK, PRINT_BLK, PRINT_CRM, CARRIER = "#e6d3aa", "#26211d", "#1d1c1b", "#efe8d8", "#1b1a19"
BRASS_K = "#d4ae5e"           # polished brass, a shade richer than the façade fill so the keys read as metal
PEGS = {
    "birchblack-birch": ((BIRCH_BLK, CARRIER), (BIRCH, CARRIER)),     # bought birch plugs, naturals dyed black
    "birch-birchblack": ((BIRCH, CARRIER), (BIRCH_BLK, CARRIER)),     # piano light / dark, same parts
    "birch": ((BIRCH, CARRIER), (BIRCH, CARRIER)),                    # one pack, no finishing
    "printed-black-cream": ((PRINT_BLK, PRINT_BLK), (PRINT_CRM, PRINT_CRM)),   # one-piece printed pegs, plate cream
    # owner (after turn 1): "what about brass and black keys? Or all brass?" Brass heads (cast or brass-fill print)
    # carry the plug's own 9.53 x 3.2 tenon into the same printed carrier, so the neck stays black
    "brass-black": ((BRASS_K, CARRIER), (PRINT_BLK, CARRIER)),
    "black-brass": ((PRINT_BLK, CARRIER), (BRASS_K, CARRIER)),
    "brass": ((BRASS_K, CARRIER), (BRASS_K, CARRIER)),
}
METALS = {"brass": ("#e2bf6a", "#c2a25e", "#6a5228"),     # façade fill, screws / stays, screw slot
          "steel": ("#b9b8b2", "#a9aaa6", "#5d5e5b")}     # printed 316L / stainless screws / pewter gilding wax
B_FX = [("DRIFT", "DRIFT", 33.5, "k"), ("ECHO TYPE", "TYPE", 62.5, "y"), ("ECHO TIME", "TIME", 82.5, "k"),
        ("ECHO REPEATS", "REPEATS", 102.5, "k"), ("ECHO MIX", "MIX", 122.5, "k"), ("TAP", "TAP", 142.5, "b"),
        ("REVERB TYPE", "TYPE", 171.0, "y"), ("REVERB DECAY", "DECAY", 191.0, "k"), ("REVERB MIX", "MIX", 211.0, "k"),
        ("VOLUME", "VOLUME", 240.0, "k")]          # systems cathedral §2 option B [CHECK §9]; labels unchecked
B_MOVED = {"ECHO REPEATS", "ECHO MIX", "REVERB MIX", "TAP"}

def vesica_slots(cx, cy, z, W=50.0, H=19.0, pitch=2.3, w=1.25, col="#1d1b19", ring=None):
    """option A's grille, his tapered lines in the band's real room (≈ 22 mm between the mixer heading and the V2
    legends): a vesica (pointed lens, the cathedral's own figure) whose slots are shortest at top and bottom."""
    a, b = W / 2, H / 2
    Rc = (a * a + b * b) / (2 * b); cc = Rc - b                  # two circles at (0, ±cc) meet in the lens
    s = ""
    n = int((H - w) / pitch) + 1
    y0 = -(n - 1) * pitch / 2
    for k in range(n):
        yk = y0 + k * pitch
        yy = abs(yk) + w / 2
        half = math.sqrt(max(Rc * Rc - (cc + yy) ** 2, 0)) - w / 2 - 0.6
        if half < 0.8:
            continue
        s += (f'{c(col)} hull(){{ translate([{cx-half:.3f},{cy+yk:.3f},{z-0.4:.3f}]) cylinder(h=0.43,d={w},$fn=16); '
              f'translate([{cx+half:.3f},{cy+yk:.3f},{z-0.4:.3f}]) cylinder(h=0.43,d={w},$fn=16); }}\n')
    if ring:
        lens = f"intersection(){{ translate([0,{cc}]) circle(r={Rc},$fn=180); translate([0,{-cc}]) circle(r={Rc},$fn=180); }}"
        s += (f'{c(ring)} translate([{cx},{cy},{z+0.02}]) linear_extrude(0.03) difference(){{ offset(delta=1.6) {lens} '
              f'offset(delta=1.1) {lens} }}\n')
    return s

def rose_slots(cx, cy, z, R, pitch=2.3, w=1.25, col="#1d1b19", ring=None):
    """the grille as a rose window, his first option: horizontal slots whose lengths follow a circle
    (shortest at the top and bottom, longest through the middle)."""
    s = ""
    n = int((2 * R - w) / pitch)
    y0 = -(n - 1) * pitch / 2
    for k in range(n):
        yk = y0 + k * pitch
        half = math.sqrt(max(R * R - (abs(yk) + w / 2) ** 2, 0)) - w / 2
        if half < 0.8:
            continue
        s += (f'{c(col)} hull(){{ translate([{cx-half:.3f},{cy+yk:.3f},{z-0.4:.3f}]) cylinder(h=0.43,d={w},$fn=16); '
              f'translate([{cx+half:.3f},{cy+yk:.3f},{z-0.4:.3f}]) cylinder(h=0.43,d={w},$fn=16); }}\n')
    if ring:
        s += (f'{c(ring)} translate([{cx},{cy},{z+0.02}]) linear_extrude(0.03) difference(){{ circle(r={R+1.6:.2f},$fn=96); '
              f'circle(r={R+1.1:.2f},$fn=96); }}\n')
    return s

# ---- the woody fine-line texture, BUILT (director ruling 4): shallow arched grooves in the printed walnut-tone body.
# Print: 0.4 wide x 0.25 deep U-grooves (modelled in the body's CAD from these same polylines). Render stand-in: a
# 0.03 strip in a darker walnut, which is how a groove reads under raking light. Line count ≈ the old straight
# streaks: 7 nested arches on a 286 x 108 face; long sides carry the arches' tails; end faces show ring arcs.
GROOVE_W, GROOVE_D = 0.4, 0.25

def _strip(pts, w):
    """a polyline -> a closed 2D strip polygon of width w (for OpenSCAD polygon())."""
    L, R = [], []
    for i, (x, y) in enumerate(pts):
        a = pts[max(i - 1, 0)]; b = pts[min(i + 1, len(pts) - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]; n = math.hypot(dx, dy) or 1
        nx, ny = -dy / n * w / 2, dx / n * w / 2
        L.append((x + nx, y + ny)); R.append((x - nx, y - ny))
    poly = L + R[::-1]
    return "polygon([" + ",".join(f"[{x:.2f},{y:.2f}]" for x, y in poly) + "]);"

def arch_lines(W, H, apex_u=0.72, n=7, sp=11.0, k=0.022, seed_shift=0.0):
    """cathedral figure on a W x H face: nested parabolic arches whose axis runs along the length (u), apex toward
    +u, opening toward -u; the outer ones run off the edges as long, nearly straight lines (as flat-sawn boards do)."""
    out = []
    v0 = H * 0.5 + seed_shift
    for i in range(n):
        ua = W * apex_u - i * sp - (i * i) * 0.6            # spacing opens out a little toward the outside
        kk = k / (1 + 0.35 * i)                               # outer arches flatter
        pts = []
        for j in range(161):
            v = -H * 0.2 + (H * 1.4) * j / 160
            u = ua - kk * W / 286 * (v - v0) ** 2 * 286 / W
            pts.append((u, v))
        out.append(pts)
    return out

def side_lines(W, z0, z1, n):
    """the arches' tails on a long side: gentle, slightly converging curves across the flat band."""
    out = []
    for i in range(n):
        zc = z0 + (z1 - z0) * (i + 1) / (n + 1)
        out.append([(u, zc + 0.9 * math.sin(math.pi * u / W + i) * (1 if i % 2 else -1)) for u in
                    [W * j / 120 for j in range(121)]])
    return out

def ring_arcs(W, z0, z1, n=2):
    """end faces: end grain, so growth-ring arcs (circles centred below the face)."""
    out = []
    for i in range(n):
        r = 60 + 9 * i
        cy, cz = W * 0.55, z0 - 48
        pts = [(cy + r * math.cos(t), cz + r * math.sin(t)) for t in
               [math.radians(40 + 100 * j / 80) for j in range(81)]]
        out.append(pts)
    return out

def grooves_on(lines, clip2d, M, col, minus2d=None):
    """lines in a face's (u, v); clip2d / minus2d: OpenSCAD 2D in the same frame; M: 3x4 multmatrix rows mapping
    (u, v, w) to the model (w = outward, 0..0.03)."""
    body = "union(){ " + " ".join(_strip(p, GROOVE_W) for p in lines) + " }"
    if minus2d:
        body = f"difference(){{ {body} {minus2d} }}"
    mm = "[" + ",".join("[" + ",".join(f"{v}" for v in r) + "]" for r in M) + ",[0,0,0,1]]"
    return f'{c(col)} multmatrix({mm}) linear_extrude(0.03) intersection(){{ {body} {clip2d} }}\n'

GROOVE_COL = {WAL_P: "#4f321e", WAL_R: "#3d2616"}

class Cathedral(Chamber):
    """CATHEDRAL: CHAMBER's case and façade on FOLD's layout, with the owner's 14:18 notes applied."""
    SPINE = "#5a3923"             # walnut-matched leather / bookcloth: keeps the slot closed, loses the accent.
                                  # (a near-black spine read as the opening itself in the closed render)

    def spine_closed(self):
        """with side pivots there are no knuckles, so the spine runs wall to wall (x 4.1-281.9)."""
        top = 2 * self.AXZ - (LID_PF - 2.5)
        return box(4.1, self.AX_Y - 1.2, BASE_H - 0.4, FO_W - 4.1, self.AX_Y - 0.4, top, self.SPINE)

    def __init__(self, layout="A", palette="black-brass", spine="none", metal="brass", grain=True):
        super().__init__()
        self.layout, self.palette, self.spine, self.metal, self.grain = layout, palette, spine, metal, grain

    # all four plate corners R 7.7, concentric with the block (systems §4)
    def peg_plate2d(self):
        return rrect2d(4.3, 4.0, FO_W - 4.3, self.D - 4.3, 7.7, 7.7)

    def lid_plate2d(self):
        return rrect2d(4.3, self.LY0 + 0.3, FO_W - 4.3, self.LY0 + self.D - 4.3, 7.7, 7.7)

    @staticmethod
    def peg_real(x, y, z, head, neck):
        """systems §10.2: deck hole Ø 12 (dark ring), neck Ø 11.2 up to deck + 2.8, a 12.7 mushroom head. Head height
        H is unpublished; drawn at 4.0 (1.2 rim + a low dome), so the top is deck + 6.8."""
        s = cyl(x, y, z - 0.15, 0.18, 12.0, "#0e0d0c", fn=48)
        s += cyl(x, y, z - 0.1, 2.95, 11.2, neck, fn=48)
        s += (f'{c(head)} hull(){{ translate([{x},{y},{z+2.8}]) cylinder(h=1.2,d=12.7,$fn=48); '
              f'translate([{x},{y},{z+4.0}]) scale([1,1,0.44]) sphere(d=12.7,$fn=48); }}\n')
        return s

    def peg_keys(self, walnut):
        if self.palette in PEGS:
            (nh, nn), (sh_, sn) = PEGS[self.palette]
            z = BASE_H
            s = "".join(self.peg_real(17 + 18 * n, 13.5, z, nh, nn) for n in range(15))
            s += "".join(self.peg_real(8 + 18 * (i + 1), 36.0, z, sh_, sn) for i in r4.sharps_after())
            return s
        nat, sh = PALETTES[self.palette]
        nat = walnut if nat == WAL_P else nat
        z = BASE_H
        s = ""
        for n in range(15):
            s += self.peg(17 + 18 * n, 13.5, z, nat, nat=False)
        for i in r4.sharps_after():
            s += self.peg(8 + 18 * (i + 1), 36.0, z, sh, nat=False)
        return s

    # ---- layout A (nothing moves) / B (one FX row on the lid, the speaker in the base)
    def play_row(self):
        P = rows(0)["P"]
        return [e for e in P if e[0] not in B_MOVED] if self.layout == "B" else P

    def lid_rows(self):
        R = rows(0)
        if self.layout == "B":
            R["FX"] = [(n, l, x, k, False, 0) for n, l, x, k in B_FX]
        return R

    def fx_breaks(self):
        return [48.0, 156.0, 225.5] if self.layout == "B" else F.vb_fx

    def voice_rule_end(self):
        return 5.5 if self.layout == "B" else 9.0     # B: the left voice rule stopped under "sync"

    def vel_gap(self):
        # B: FREE / SYNC sits at d 69, where the V2 toggles' legends were ("sync" hit "osc 3 ctl"). The band below is
        # empty in B, so those three legends (osc 3 ctl, source, velocity) go under their toggles instead
        return -8.4 if self.layout == "B" else 7.7

    def sync_pos(self):
        return (96.0, 69.0) if self.layout == "B" else SYNC_FOLD_D

    def behind(self):
        return BEHIND_FOLD - self.dFX      # B too now (systems' check: REPEATS legend under FREE / SYNC by 1.7)

    def behind_names(self):
        # B: TIME (always, with behind set) and REPEATS go behind their knobs; "free" / "sync" already sit 0.5 behind the
        # toggle centre (sync_toggle). A: TIME and DECAY, as v1.1 / CHAMBER.
        return ("ECHO REPEATS",) if self.layout == "B" else ("REVERB DECAY",)

    def sync_dy(self):
        # B: at 0.5 behind, "free" sat 0.64 from FREQ 3 (checker 7c); with TIME / REPEATS legends gone behind,
        # the words can sit further back, away from the V2 row
        return SYNC_DY_B if self.layout == "B" else 0.5

    def grille(self, L0):
        if self.layout == "B":
            return ""                                   # the band is the crossing: a quiet rest
        return vesica_slots(143.0, L0 + 37.6, LID_PF, W=66.0, H=16.0, ring="#d3cab8")   # ring clear of "noise / ext" and "mixer"

    def base_extra(self, walnut):
        s = self.grooves_base(walnut) if self.grain else ""
        if self.layout != "B":
            return s
        return s + rose_slots(228.0, 68.0, BASE_H, 13.5, ring="#d3cab8")

    # ---- ruling 4: the woody fine-line grooves on the base underside, its sides, and the lid (back outside the
    # façade field, sides). The lid back's façade field (x 30-256, d 8-86) is left for the owner's own design.
    FACADE_FIELD = (30.0, 8.0, 256.0, 86.0)

    def grooves_base(self, walnut):
        D, col = self.D, GROOVE_COL.get(walnut, "#4f321e")
        s = grooves_on(arch_lines(FO_W, D), rrect2d(6.5, 6.5, FO_W - 6.5, D - 6.5, 5.5, 5.5),
                       [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0]], col)                       # underside (faces down)
        band = f"translate([12.5,6.2]) square([{FO_W-25},{BASE_H-3-6.4}]);"
        s += grooves_on(side_lines(FO_W, 6.2, BASE_H - 3.2, 1), band, [[1, 0, 0, 0], [0, 0, -1, 0], [0, 1, 0, 0]], col)   # front
        s += grooves_on(side_lines(FO_W, 6.2, BASE_H - 3.2, 1), band, [[1, 0, 0, 0], [0, 0, 1, D], [0, 1, 0, 0]], col)    # hinge side
        end = f"translate([12.5,6.2]) square([{D-25},{BASE_H-3-6.4}]);"
        s += grooves_on(ring_arcs(D, 6.2, BASE_H - 3.2), end, [[0, 0, -1, 0], [1, 0, 0, 0], [0, 1, 0, 0]], col)            # left end
        # right end: USB-C / MIDI live at y 65-104, z 4.8-8.2; the arcs stay at y < 58
        s += grooves_on(ring_arcs(D, 6.2, BASE_H - 3.2), f"translate([12.5,8.8]) square([45,{BASE_H-3-9}]);",
                        [[0, 0, 1, FO_W], [1, 0, 0, 0], [0, 1, 0, 0]], col)
        return s

    def grooves_lid(self, walnut):
        D, L0, H, col = self.D, self.LY0, self.LIDH, GROOVE_COL.get(walnut, "#4f321e")
        x0, d0, x1, d1 = self.FACADE_FIELD
        # lid back: the first arch's apex peeks into the right margin (x ≈ 262) and the arches' tails run out through
        # the bands above and below the façade field, so the figure reads around his design without entering it
        s = grooves_on(arch_lines(FO_W, D, apex_u=262 / FO_W, seed_shift=4.0),
                       rrect2d(6.5, 6.5, FO_W - 6.5, D - 6.5, 5.5, 5.5),
                       [[1, 0, 0, 0], [0, 1, 0, L0], [0, 0, -1, 0]], col,
                       minus2d=f"translate([{x0},{d0}]) square([{x1-x0},{d1-d0}]);")
        band = f"translate([12.5,13.0]) square([{FO_W-25},{H-3-13.2}]);"                          # far wall: above the I/O
        s += grooves_on(side_lines(FO_W, 13.0, H - 3.2, 2), band, [[1, 0, 0, 0], [0, 0, 1, L0 + D], [0, 1, 0, 0]], col)
        end = f"translate([12.5,6.2]) square([{D-25},{H-3-6.4}]);"
        s += grooves_on(ring_arcs(D, 6.2, H - 3.2, 3), end, [[0, 0, -1, 0], [1, 0, 0, L0], [0, 1, 0, 0]], col)
        s += grooves_on(ring_arcs(D, 6.2, H - 3.2, 3), end, [[0, 0, 1, FO_W], [1, 0, 0, L0], [0, 1, 0, 0]], col)
        return s

    def base_names(self):
        names = [(14, "pitch"), (105.5, "filter")] + ([] if self.layout == "B" else [(188.5, "effects")])
        return "".join(txt(tx, 85.0, BASE_H + 0.01, n, 2.4, FO_INK, font=HAND, halign="left") for tx, n in names)

    def lid_names(self, gz):
        if self.layout != "B":
            return super().lid_names(gz)
        L0 = self.LY0
        s = "".join(txt(x, L0 + self.dFX + FO_HEAD_D + 1.2, LID_PF + 0.01, n, 2.0, FO_INK, font=HAND, valign="baseline")
                    for n, x in (("echo", 102.5), ("reverb", 191.0)))
        for (tx, name, ha, dd) in [(14, "oscillators", "left", 17.5), (143, "mixer", "center", 11.3), (272, "contours", "right", 17.5)]:
            s += txt(tx, L0 + self.dV1 + dd, LID_PF + 0.01, name, 2.4, FO_INK, font=HAND, halign=ha)
        return s

    # ---- hidden side pivots instead of knuckles (systems §1): a brass leaf pair inside each wall, a blind pin
    def knuckles(self, walnut, part):
        if part != "b":
            return ""
        s = ""
        for x0 in (0.0, FO_W - 4.05):
            s += (f'{c(walnut)} hull(){{ translate([{x0},{self.AX_Y},{self.AXZ}]) rotate([0,90,0]) cylinder(h=4.05,r=5.2,$fn=48); '
                  f'translate([{x0},{self.AX_Y-9},{BASE_H-1}]) cube([4.05,13,1]); }}\n')
            xp = x0 - 0.04 if x0 == 0 else x0 + 4.05
            s += f'{c("#5a3a22")} translate([{xp},{self.AX_Y},{self.AXZ}]) rotate([0,90,0]) cylinder(h=0.08,r=1.6,$fn=24);\n'   # walnut plug over the pin
        return s

    # ---- feet that are the case screws (systems §3): 4 corner screw-feet, the 2 axis screws flush brass
    def lid_back(self, walnut):
        L0, D = self.LY0, self.D
        z = -0.07
        brass, screw, slot = METALS[self.metal]
        s = ""
        IMP = L0 + 18.0
        s += box(30, IMP - 0.35, z - 0.03, 256, IMP + 0.35, z, brass)
        s += box(30, IMP - 8.35, z - 0.03, 256, IMP - 7.65, z, brass)
        for n in range(25):
            k = (n + 1) // 2 * (1 if n % 2 else -1)
            s += self.pipe(143 + 8.75 * k, IMP, 66.0 * 2 ** (-n / 12), z, brass)
        for x in (108.0, 178.0):
            s += cyl(x, L0 + 28.3, -0.2, 0.3, 4.0, "#0f0b08", fn=32)
        for (x, y) in [(143, L0 + 12), (143, L0 + D - 12)]:
            s += cyl(x, y, -0.06, 0.1, 5.4, screw, fn=24) + box(x - 1.8, y - 0.35, -0.1, x + 1.8, y + 0.35, -0.04, slot)
        for (x, y) in [(16, L0 + 12), (FO_W - 16, L0 + 12), (16, L0 + D - 12), (FO_W - 16, L0 + D - 12)]:
            s += cyl(x, y, -2.6, 2.6, 12, "#23201e", fn=40) + cyl(x, y, -2.66, 0.1, 5.0, "#151312", fn=24)   # foot + its cap plug
        if self.grain:
            s += self.grooves_lid(walnut)
        return s

    def model(self, state=True, walnut=WAL_P, book=False):
        s = Branch.model(self, state, walnut, book)
        if self.spine != "none":
            if state is False:
                s += self.spine_closed()
            elif state == "stand":
                s += self.spine_stand()
        return s

def cathedral_grain(png, angle=-14.0, spacing=26.0, curv=0.0016, strength=0.13, seed=3):
    """'woody' but as sparse as before (owner): flat-sawn figure, the arches woodworkers call cathedral grain,
    at about the line count of the straight streaks he liked. Applied to the walnut-hue pixels of a render."""
    import numpy as np
    from PIL import Image
    im = np.asarray(Image.open(png).convert("RGB")).astype(np.float32)
    r, g, b = [im[..., k] / 255 for k in range(3)]
    mx = np.maximum(np.maximum(r, g), b); mn = np.minimum(np.minimum(r, g), b)
    d = np.maximum(mx - mn, 1e-6)
    hue = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    wal = (hue > 12) & (hue < 40) & (sat > 0.42) & (mx > 0.10) & (mx < 0.62)
    h, w = mx.shape
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    th = math.radians(angle)
    u = xx * math.cos(th) + yy * math.sin(th)
    v = -xx * math.sin(th) + yy * math.cos(th)
    vs = v[wal]
    v0 = float(np.median(vs)) if vs.size else h / 2
    warp = ld._noise(h, w, 180, seed) * 40 + ld._noise(h, w, 50, seed + 1) * 6
    f = u + curv * (v - v0) ** 2 * w / 1000.0 + warp
    ph = (f / spacing) % 1.0
    line = np.clip(1.0 - np.abs(ph - 0.5) / 0.07, 0, 1) ** 1.5
    fine = ld._noise(h, w, 2, seed + 2)
    k = 1.0 - strength * line - 0.025 * fine
    out = np.where(wal[..., None], im * k[..., None], im)
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(png)
    return png

# ------------------------------------------------------------------ DIPTYCH: a pocket instrument for reading the day
RED = "#a8322a"

class Diptych(Branch):
    def style(self):
        return Style(knob=lambda x, y, z, a: knob_black(x, y, z, a),
                     hero=lambda x, y, z, a: ld.knob_hero(x, y, z, a, col=K_RED, line="#f3ead6"),
                     ink="#151413", font="EB Garamond:style=Medium", lsize=2.0, upper=True, knob_r=7.25, lab_gap=3.3,
                     ticks=False)

    def lid_ink(self):
        return "#151413"

    def time_kw(self):
        return dict(ink_ms="#151413", ink_div=RED, font="EB Garamond:style=Medium", full=True, size=1.25)

    def rule_col(self):
        return RED

    RULE_HW = 0.22

    def graduations(self, R, row_y, z):
        """'graduations everywhere': every knob a fine red ring of 31 ticks (10 deg) + black majors every 30 deg."""
        s = ""
        for key, yy in row_y.items():
            for name, lab, x, kind, midi, yo in R[key]:
                if name == "ECHO TIME" or kind not in "kgrh":
                    continue
                r = 10.4 if kind == "h" else 7.25
                if kind in "gr":
                    for a in [-125, -75, -25, 25, 75, 125]:
                        s += _tick(x, yy, z, r + 0.9, a, 1.6, 0.42, "#151413")
                    continue
                skip = 35 if name in NO_TOP_TICK else -1
                for i in range(31):
                    a = -150 + 10 * i
                    if abs(a) > skip:
                        s += _tick(x, yy, z, r + 0.9, a, 0.8, 0.16, RED)
                for i in range(11):
                    a = -150 + 30 * i
                    if abs(a) > skip:
                        s += _tick(x, yy, z, r + 0.9, a, 1.5, 0.3, "#151413")
        return s

    def base_names(self):
        R = {"P": rows(0)["P"]}
        s = self.graduations(R, {"P": 68}, BASE_H + 0.005)
        for tx, n in [(14, "PITCH"), (105.5, "FILTER"), (188.5, "EFFECTS & OUT")]:
            s += txt(tx, 85.0, BASE_H + 0.01, n, 2.1, RED, font=SERIF_I, halign="left")
        return s

    def lid_names(self, gz):
        L0 = self.LY0
        R = rows(0)
        s = self.graduations(R, {"V1": L0 + self.dV1, "V2": L0 + self.dV2, "FX": L0 + self.dFX}, LID_PF + 0.005)
        s += "".join(txt(x, L0 + self.dFX + FO_HEAD_D + 1.2, LID_PF + 0.01, n, 1.9, RED, font=SERIF_I, valign="baseline")
                     for n, x in r5.FX_HEADS)
        for (tx, name, ha) in [(14, "OSCILLATORS", "left"), (143, "MIXER", "center"), (272, "CONTOURS", "right")]:
            s += txt(tx, L0 + self.dV1 + 11.3, LID_PF + 0.01, name, 2.1, RED, font=SERIF_I, halign=ha)
        return s

    def name_mark(self, gz):
        """the maker's cartouche (blank until he names it): a red double rule, notched corners."""
        L0 = self.LY0
        nz = L0 + NAME_D
        cart = "polygon([[135,{a}],[136.5,{b}],[149.5,{b}],[151,{a}],[151,{c}],[149.5,{d}],[136.5,{d}],[135,{c}]]);"
        outer = cart.format(a=nz + 1.5, b=nz, c=nz + 3.5, d=nz + 5)
        return (f'{c(RED)} translate([0,0,{gz}]) linear_extrude(0.04) difference(){{ {outer} offset(delta=-0.35) {outer} }}\n')

    def lid_ends(self, stowed):
        """no stay grooves: the cords' brass eyes only (d 60 from the hinge axis, on the axis height)."""
        s = ""
        for xs in (-0.3, FO_W + 0.05):
            s += f'{c("#c2a25e")} translate([{xs},{self.AX_Y + 60},{self.AXZ}]) rotate([0,90,0]) difference(){{ cylinder(h=0.25,d=4.2,$fn=24); translate([0,0,-1]) cylinder(h=2,d=2.0,$fn=16); }}\n'
        return s

    def base_extra(self, walnut):
        """base end-face eyes (y 53.2, z 9) and the two brass feet, stowed flush in the underside."""
        s = ""
        for xs in (-0.3, FO_W + 0.05):
            s += f'{c("#c2a25e")} translate([{xs},53.2,9]) rotate([0,90,0]) difference(){{ cylinder(h=0.25,d=4.2,$fn=24); translate([0,0,-1]) cylinder(h=2,d=2.0,$fn=16); }}\n'
        return s

    def stand_extra(self, walnut):
        """cords at the latitude of home (37.4 deg) + feet out to y 167 (systems §1-2)."""
        a = math.radians(self.STAND)
        ly = self.AX_Y + 60 * math.cos(a); lz = self.AXZ + 60 * math.sin(a)
        s = ""
        for x in (-1.3, FO_W + 1.3):
            p0, p1 = (x, ly, lz), (x, 53.2, 9.0)
            dx, dy, dz = [p1[i] - p0[i] for i in range(3)]
            L = math.sqrt(dx * dx + dy * dy + dz * dz)
            ax = math.degrees(math.acos(dz / L)); az = math.degrees(math.atan2(dy, dx))
            s += f'{c(RED)} translate([{p0[0]},{p0[1]},{p0[2]}]) rotate([0,{ax:.3f},{az:.3f}]) cylinder(h={L:.2f},d=2.0,$fn=12);\n'
            s += cyl(x, 53.2, 9.0 - 1.2, 2.4, 3.0, "#c2a25e", fn=16)          # brass snap
        for x0 in (6.0, FO_W - 9.0):          # feet: 3 x 8 brass bar from a pivot under the base to a rubber tip at y 167
            s += box(x0, 92, 0.0, x0 + 3, 165, 3.0, "#c2a25e")
            s += cyl(x0 + 1.5, 92, -0.2, 3.6, 5, "#8a6f38", fn=20)
            s += cyl(x0 + 1.5, 164, 0.0, 4.5, 9.0, "#1e1e1e", fn=24)
        return s

# =================================================================== jobs
def jobs(SZ):
    ch, dp = Chamber(), Diptych()
    D = ch.D; OPEN = 2 * D + 2
    W = FO_W
    J = {
        # BUTTERFLY
        "rb_bf_main": lambda: ld.shot(butterfly(), fp_rect(0, 0, OS_W, 190), "rb_bf_main", size=SZ, az=-30, el=36, dist=700, center=(138, 88, 12), grain_classes=("walnut",), grain_angle=-21),
        "rb_bf_rear": lambda: ld.shot(butterfly(), fp_rect(0, 0, OS_W, 190), "rb_bf_rear", size=SZ, az=-152, el=26, dist=430, center=(150, 160, 14), grain_classes=("walnut",), grain_angle=8),
        "rb_bf_joint": lambda: ld.shot(butterfly(), fp_rect(0, 0, OS_W, 190), "rb_bf_joint", size=SZ, az=-20, el=40, dist=170, center=(140, 168, 22), grain_classes=("walnut",), grain_angle=-4),
        "rb_bf_top": lambda: top4(butterfly(), "rb_bf_top", -2, -2, OS_W + 2, 194, px_per_mm=12, grain_classes=("walnut",), grain_angle=0),
        "rb_bf_wall": lambda: hanging(os.path.join(OUT, "rb_bf_top.png"), os.path.join(OUT, "rb_bf_wall.png"), 12),
        "rb_bf_end": lambda: shot_ortho(butterfly(), "rb_bf_end", "right", -2, 196, -1, 40, wmax=OS_W),
        # RAIN
        "rb_rn_main": lambda: ld.shot(rain(), fp_rect(0, 0, OS_W, OS_D), "rb_rn_main", size=SZ, az=-30, el=38, dist=700, center=(138, 84, 12), grain_classes=()),
        "rb_rn_far": lambda: ld.shot(rain(), fp_rect(0, 0, OS_W, OS_D), "rb_rn_far", size=SZ, az=-30, el=50, dist=1500, center=(138, 90, 12), grain_classes=()),
        "rb_rn_near": lambda: ld.shot(rain(), fp_rect(0, 0, OS_W, OS_D), "rb_rn_near", size=SZ, az=-34, el=30, dist=190, center=(122, 118, 24), grain_classes=()),
        "rb_rn_keys": lambda: ld.shot(rain(), fp_rect(0, 0, OS_W, OS_D), "rb_rn_keys", size=SZ, az=-40, el=18, dist=200, center=(48, 26, 26), grain_classes=()),
        "rb_rn_top": lambda: top4(rain(), "rb_rn_top", -2, -2, OS_W + 2, OS_D + 2, px_per_mm=14, grain_classes=()),
        # CHAMBER
        "rb_ch_main": lambda: shot4(ch.model(True), fp_rect(0, 0, W, OPEN), "rb_ch_main", size=SZ, az=-30, el=44, dist=880, center=(143, OPEN / 2, 12), grain_classes=(), wood=True),
        "rb_ch_closed": lambda: ld.shot(ch.model(False, walnut=WAL_R, book=True), fp_rect(0, 0, W, D) + fp_rect(318, -10, 553, 146), "rb_ch_closed", size=SZ, az=158, el=52, dist=1100, center=(275, 60, 22), grain_classes=("walnut",), grain_angle=25),
        "rb_ch_closed_p": lambda: shot4(ch.model(False), fp_rect(0, 0, W, D), "rb_ch_closed_p", size=SZ, az=160, el=50, dist=640, center=(143, D / 2, 22), grain_classes=(), wood=True),
        "rb_ch_stand_back": lambda: ld.shot(ch.model("stand", walnut=WAL_R), fp_rect(0, 0, W, D + 64), "rb_ch_stand_back", size=SZ, az=160, el=14, dist=820, center=(143, D * 0.8, 60), grain_classes=("walnut",), grain_angle=30),
        "rb_ch_stand": lambda: shot4(ch.model("stand"), fp_rect(0, 0, W, D + 64), "rb_ch_stand", size=SZ, az=-32, el=24, dist=760, center=(143, D * 0.6, 50), grain_classes=(), wood=True) and relight(os.path.join(OUT, "rb_ch_stand.png")),
        "rb_ch_flat_under": lambda: shot4(ch.model(True), fp_rect(0, 0, W, OPEN), "rb_ch_flat", size=SZ, az=-20, el=62, dist=900, center=(143, OPEN / 2, 12), grain_classes=(), wood=True),
        "rb_ch_keys": lambda: shot4(ch.model(True), fp_rect(0, 0, W, OPEN), "rb_ch_keys", size=SZ, az=-36, el=24, dist=300, center=(64, 30, 18), grain_classes=(), wood=True),
        "rb_ch_keys_fallback": lambda: shot4(Chamber(fallback=True).model(True), fp_rect(0, 0, W, OPEN), "rb_ch_keys_fallback", size=SZ, az=-36, el=24, dist=300, center=(64, 30, 18), grain_classes=(), wood=True),
        "rb_ch_top": lambda: top4(ch.model(True), "rb_ch_top", -2, -2, W + 2, OPEN + 2, px_per_mm=12, grain_classes=()),
        "rb_ch_front_closed": lambda: shot_ortho(ch.model(False), "rb_ch_front_closed", "front", -2, W + 2, -1, 56, wood=True),
        # CATHEDRAL (owner 14:18): only what's needed to judge colours, A vs B, the wood and the spine
        **{f"rb_ct_col_{p}": (lambda p=p: shot4(Cathedral("A", p).model(True), fp_rect(0, 0, W, OPEN), f"rb_ct_col_{p}", size=SZ, az=-36, el=24, dist=300, center=(64, 30, 18), grain_classes=(), wood=True))
           for p in ("ebony-maple", "maple-ebony", "ebony", "maple")},
        **{f"rb_ct2_col_{p}": (lambda p=p: shot4(Cathedral("A", p).model(True), fp_rect(0, 0, W, OPEN), f"rb_ct2_col_{p}", size=SZ, az=-36, el=24, dist=300, center=(64, 30, 18), grain_classes=(), wood=True))
           for p in PEGS},
        "rb_ct2_closed_steel": lambda: cathedral_grain(ld.shot(Cathedral("A", "birchblack-birch", metal="steel").model(False, walnut=WAL_R, book=True), fp_rect(0, 0, W, D) + fp_rect(318, -10, 553, 146), "rb_ct2_closed_steel", size=SZ, az=158, el=52, dist=1100, center=(275, 60, 22), grain_classes=())),
        "rb_ct_A_stand": lambda: shot4(Cathedral("A").model("stand"), fp_rect(0, 0, W, D + 64), "rb_ct_A_stand", size=SZ, az=-32, el=24, dist=760, center=(143, D * 0.6, 50), grain_classes=(), wood=True) and relight(os.path.join(OUT, "rb_ct_A_stand.png")),
        "rb_ct_B_stand": lambda: shot4(Cathedral("B").model("stand"), fp_rect(0, 0, W, D + 64), "rb_ct_B_stand", size=SZ, az=-32, el=24, dist=760, center=(143, D * 0.6, 50), grain_classes=(), wood=True) and relight(os.path.join(OUT, "rb_ct_B_stand.png")),
        "rb_ct_closed": lambda: ld.shot(Cathedral("A").model(False, walnut=WAL_R, book=True), fp_rect(0, 0, W, D) + fp_rect(318, -10, 553, 146), "rb_ct_closed", size=SZ, az=158, el=52, dist=1100, center=(275, 60, 22), grain_classes=()),   # grooves are modelled now (ruling 4): no cathedral_grain post-process
        "rb_ct_top_A": lambda: top4(Cathedral("A").model(True), "rb_ct_top_A", -2, -2, W + 2, OPEN + 2, px_per_mm=12, grain_classes=()),
        "rb_ct_top_B": lambda: top4(Cathedral("B").model(True), "rb_ct_top_B", -2, -2, W + 2, OPEN + 2, px_per_mm=12, grain_classes=()),
        # DIPTYCH
        "rb_dp_stand": lambda: shot4(dp.model("stand"), fp_rect(0, 0, W, 175), "rb_dp_stand", size=SZ, az=-38, el=22, dist=800, center=(143, 80, 50), grain_classes=(), wood=True) and relight(os.path.join(OUT, "rb_dp_stand.png")),
        "rb_dp_main": lambda: shot4(dp.model(True), fp_rect(0, 0, W, OPEN), "rb_dp_main", size=SZ, az=-30, el=44, dist=880, center=(143, OPEN / 2, 12), grain_classes=(), wood=True),
        "rb_dp_side": lambda: shot_ortho(dp.model("stand"), "rb_dp_side", "right", -4, 200, -4, D + 64, wmax=W + 2, wood=True),
        "rb_dp_top": lambda: top4(dp.model(True), "rb_dp_top", -2, -2, W + 2, OPEN + 2, px_per_mm=14, grain_classes=()),
        "rb_dp_closed": lambda: shot4(dp.model(False), fp_rect(0, 0, W, D), "rb_dp_closed", size=SZ, az=-28, el=30, dist=640, center=(143, D / 2, 22), grain_classes=(), wood=True),
    }
    return J


# ------------------------------------------------------------------ post: OpenSCAD's fixed light renders faces turned away
# from it as mid-grey (the standing lid's cream plate looks grey). Lift low-saturation mid-greys back toward the intended
# cream. Only used on views where a cream face points away from the light; noted in the docs.
def relight(png, lo=105, hi=200, gain=None, ymax=0.6, target=(241, 236, 224)):
    import numpy as np
    from PIL import Image
    im = np.asarray(Image.open(png).convert("RGB")).astype(np.float32)
    mx, mn = im.max(axis=2), im.min(axis=2)
    sat = (mx - mn) / np.maximum(mx, 1)
    bg = np.all(np.abs(im - im[2, 2]) < 4, axis=2)
    m = (~bg) & (sat < 0.09) & (mx > lo) & (mx < hi)
    m[int(m.shape[0] * ymax):, :] = False       # the lid only: keep the ground shadow (also a low-saturation grey) as is
    if gain is None:      # scale the plate's median grey to the intended cream (v1.1 E's "visibly lighter" plate)
        med = float(np.median(mx[m])) if m.any() else 150.0
        gain = target[0] / max(med, 1.0)
    warm = np.array([1.0, target[1] / target[0], target[2] / target[0]], np.float32)
    out = np.where(m[..., None], np.clip(im * gain * warm, 0, 250), im)
    Image.fromarray(out.astype(np.uint8)).save(png)
    return png

def hanging(top_png, out_png, px_per_mm):
    """BUTTERFLY hung on a wall, tree side up: the exact top view IS the elevation; plaster, a soft shadow, the cleat."""
    from PIL import Image, ImageFilter, ImageDraw
    import numpy as np
    obj = Image.open(top_png).convert("RGB")
    a = np.asarray(obj).astype(np.int16)
    mask = ~np.all(np.abs(a - np.array([243, 239, 232])) <= 1, axis=2)
    m = Image.fromarray((mask * 255).astype(np.uint8))
    pad = int(60 * px_per_mm)
    W, H = obj.size[0] + 2 * pad, obj.size[1] + 2 * pad
    wall = Image.new("RGB", (W, H), (233, 228, 219))
    sh = Image.new("L", (W, H), 0)
    sh.paste(m, (pad + int(4 * px_per_mm), pad + int(7 * px_per_mm)))
    sh = sh.filter(ImageFilter.GaussianBlur(5 * px_per_mm))
    dark = Image.new("RGB", (W, H), (150, 142, 130))
    wall = Image.composite(dark, wall, sh.point(lambda v: int(v * 0.55)))
    wall.paste(obj, (pad, pad), m)
    wall.save(out_png)
    return out_png

if __name__ == "__main__":
    SZ = (5200, 3500)
    if "--test" in sys.argv:
        SZ = (1600, 1080); sys.argv.remove("--test")
    J = jobs(SZ)
    sel = sys.argv[1:] or list(J)
    if len(sel) == 1 and sel[0].endswith("*"):
        sel = [k for k in J if k.startswith(sel[0][:-1])]
    for k in sel:
        print(J[k]())
