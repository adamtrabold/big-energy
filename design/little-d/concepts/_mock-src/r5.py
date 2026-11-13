#!/usr/bin/env python3
"""Round 5 mock geometry: HUSH, ONE SHEET (key edge A / B), FOLD-105 and FOLD-113.

Drawn to systems "round 5 final" (common rev 7.1, fold rev 5.3); layout data read from fold_r5_check.py
(FOLD x; ONE SHEET x = FOLD - 5, HUSH x = FOLD + 2). Origin front-left outer corner, x right, y away, z up. mm.
Run: python3 r5.py [job ...]  (--test for low-res). Outputs out/r5_*.png. Primitives come from r4.py.
"""
import importlib.util, io, contextlib, math, os, sys
import ld, r4
from ld import box, cyl, txt, c, knob_std, knob_hero, toggle, led, stick, ticks
from r4 import (pebble, rrect2d, ext, knob_black, pg_layers, halo, woodfill, feltfill, top4, shot4, under_shot,
                FELT, FELT_DK, FELT_DEB, TAG, MAPLE, MAPLE_DK, K_CREAM, PCREAM, WAL_P, WAL_R, PG, FO_INK, K_RED,
                ACRYL_W, ACRYL_K, Style, sharps_after)

OUT = ld.OUT
KEY_LIFT = float(os.environ.get("R5_KEY_LIFT", 0))   # aftertouch: key strip may rise 1-2 mm on a compliant layer (eng confirming)
HERE = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ layout from the checker (FOLD x)
_spec = importlib.util.spec_from_file_location("frc", os.path.join(HERE, "fold_r5_check.py"))
F = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(F)

LAB = {"BEND stick": "BEND", "CONTOUR AMT": "AMOUNT", "ECHO REPEATS": "REPEATS", "F ATTACK": "ATTACK",
       "F DECAY": "DECAY", "F SUSTAIN": "SUSTAIN", "L ATTACK": "ATTACK", "L DECAY": "DECAY", "L SUSTAIN": "SUSTAIN",
       "DECAY tgl": "DECAY", "VEL": "VELOCITY", "NOISE/EXT": "NOISE / EXT", "RANGE 1": "RANGE", "RANGE 2": "RANGE",
       "RANGE 3": "RANGE", "WAVE 1": "WAVE", "WAVE 2": "WAVE", "WAVE 3": "WAVE",
       # S1 label pass: the back row's legends are short, under a section heading (echo: type · time; reverb: decay · type)
       "ECHO TYPE": "TYPE", "ECHO TIME": "TIME", "REVERB DECAY": "DECAY", "REVERB TYPE": "TYPE",
       "PARA (MONO/PARA/PARA+4)": "MONO / PARA / PARA+4"}
FX_HEADS = [("ECHO", 118.5), ("REVERB", 167.5)]     # FOLD x: centred over each pair (= centre of its break-bounded group)
ABOVE_GAP = 7.4      # toggle legends set above their toggle (flat concepts): 7.4 from centre (was 8.4), >= 1.5 clear both ways
SW_LAB_DX = 6.2      # switch-pair legends beside the toggle: 6.2 from centre (was 5.6) = 1.6 clear of the nut
MIDI = {"MOD", "TUNE", "GLIDE", "CUTOFF", "RANGE 1", "RANGE 2", "RANGE 3", "FREQ 2", "FREQ 3"}
ECHO_POS = [(-60, "tape"), (-20, "bbd"), (20, "clean"), (60, "ping-pong")]
VERB_POS = [(-60, "plate"), (-20, "hall"), (20, "spring"), (60, "shimmer")]

def kind_of(name, k):
    if k == "stick": return "s"
    if k == "l": return "l"
    if k == "t": return "t"
    if k == "b": return "b"
    if name.startswith("RANGE"): return "g"
    if name.startswith("WAVE"): return "r"
    if name.endswith("TYPE"): return "y"
    if name == "CUTOFF": return "h"
    return "k"

def rows(dx):
    """{row: [(name, label, x, kind, midi, yoff)]} with x shifted by dx (yoff only for the lights, +13 behind PLAY)."""
    out = {}
    out["P"] = [(e[0], LAB.get(e[0], e[0] if e[3] != "l" else ("STATUS" if e[0] == "status" else "")), e[1] + dx,
                 kind_of(e[0], e[3]), e[0] in MIDI, (e[4] - 68) if len(e) > 4 else 0) for e in F.play]
    for key, src in (("V1", F.v1), ("V2", F.v2), ("FX", F.fx)):
        out[key] = [(n, LAB.get(n, n), x + dx, kind_of(n, k), n in MIDI, 0) for n, x, r, k in src]
    # PARA | AFTERTOUCH (flat). No legend fits beside PARA here (2.3 mm between its nut and OSC 2's legend): drawn bare, FLAGGED to systems
    out["SW"] = [(n, "" if n.startswith("PARA") else LAB.get(n, n), x + dx, "t", False, 0) for n, x, r, k in F.sw_flat]
    out["SWF"] = [(n, LAB.get(n, n), x + dx, "t", False, 0) for n, x, r, k in F.sw]         # FOLD: moved outward (rev 5.6)
    return out

def breaks(dx):
    return [b + dx for b in F.vb_play], [b + dx for b in F.vb_fx]

random_ang = r4.ang

# ------------------------------------------------------------------ one control
FAN_OUT_I, FAN_OUT_K = 6.2, 6.5     # outer detent names' row (was 5.6 for both): S1 clearance

def fx_heads(dx, y, z, ink, font, size, upper, h=0.12):
    """S1: the section heading over each back-row pair, set above the type-name fan (baseline y)."""
    return "".join(txt(x + dx, y, z, n if upper else n.lower(), size, ink, font=font, valign="baseline", h=h)
                   for n, x in FX_HEADS)

def type_fan(x, y, z, r, pos, ink, font, size, upper, bib=None):
    """4 detents fanned over the top; the names in one straight row above, each over its detent."""
    s = ""
    if bib:      # HUSH: the tag grows a bib behind the knob to carry the names (felt can't hold fine marks)
        s += f'{c(bib)} hull(){{ translate([{x-12.6},{y+12.2},{z-1}]) cylinder(h=1.06,r=2.8,$fn=24); translate([{x+12.6},{y+12.2},{z-1}]) cylinder(h=1.06,r=2.8,$fn=24); translate([{x},{y+4},{z-1}]) cylinder(h=1.06,r=4,$fn=24);}}\n'
    s += ticks(x, y, z, r + 0.9, [a for a, _ in pos], ink, length=1.5, width=0.5)
    sz = 1.05 if "Inter" in font else 1.3
    for a, w in pos:
        th = math.radians(a)
        row = 3.4 if abs(a) < 40 else (FAN_OUT_K if "Kalam" in font else FAN_OUT_I)   # inner low, outer high: >= 1.5 clear
        s += txt(x + 11.85 * math.sin(th), y + r + row, z, w.upper() if upper else w, sz, ink, font=font)
    return s

def tap_cap(x, y, z, style):
    """TAP: 12 mm momentary cap (part UNVERIFIED). style: 'peg' (HUSH maple), 'acryl' (white key acrylic), 'proof'."""
    if style == "peg":
        s = cyl(x, y, z - 0.15, 0.2, 17.0, FELT_DK, fn=48)          # its own felt collar, like a key
        s += cyl(x, y, z, 2.6, 7.0, "#d4b385", fn=24)
        s += cyl(x, y, z + 2.5, 1.7, 12.7, MAPLE, fn=48)
        s += f'{c(MAPLE)} translate([{x},{y},{z+4.2}]) scale([1,1,0.28]) sphere(d=12.7,$fn=48);\n'
        return s
    col = ACRYL_W if style == "acryl" else "#f4efe4"
    s = cyl(x, y, z, 0.6, 14.2, "#2a2724" if style == "proof" else "#cfc4ad", fn=48)      # bezel ring
    s += cyl(x, y, z + 0.6, 3.4, 12.0, col, fn=48, d2=11.6)
    return s

def joystick(x, y, z, ink, tilt=0.0):
    """BEND (round 5 S2): a one-axis spring-to-centre thumbstick (#2765 class, cap UNVERIFIED in hand), drawn so it
    reads as a joystick, not a fader. Ink: a round gate ring (15 / 13.4) with two bezel pointers at 12 and 6 o'clock
    (the tilt axis; watch-bezel idea). Panel: a short fore-aft gate slot 4.0 x 11.2 (stem + clearance + throw), dark.
    Part: a 3.2 stem standing 8 mm clear of the plate, a flared 10 mm cap with a grip rim and a dished centre.
    Top at z + 12.6 (was 13.5): no clearance changes. tilt: degrees about x (+ = away), for diagrams only."""
    s = (f'{c(ink)} translate([{x:.3f},{y:.3f},{z+0.01:.3f}]) linear_extrude(0.1) difference(){{ circle(d=15,$fn=72); circle(d=13.4,$fn=72); }}\n')
    for sg in (1, -1):
        s += (f'{c(ink)} translate([{x:.3f},{y + sg * 7.3:.3f},{z+0.01:.3f}]) linear_extrude(0.1) '
              f'polygon([[-0.85,0],[0.85,0],[0,{sg * 1.15:.2f}]]);\n')
    s += (f'{c("#0e0d0c")} translate([{x:.3f},{y:.3f},{z-0.4:.3f}]) linear_extrude(0.46) '
          f'hull(){{ translate([0,{-3.6:.2f}]) circle(d=4.0,$fn=24); translate([0,{3.6:.2f}]) circle(d=4.0,$fn=24); }}\n')
    part = cyl(0, 0, -0.4, 8.6, 3.2, "#4a4a4f", fn=24)                       # stem, seen in every side / 3/4 view
    part += cyl(0, 0, 8.2, 3.0, 8.4, "#2f2f33", fn=48, d2=10.0)              # flared cap body
    part += cyl(0, 0, 11.2, 1.0, 10.0, "#2f2f33", fn=48)
    part += (f'{c("#5c5c63")} translate([0,0,12.2]) linear_extrude(0.4) difference(){{ circle(d=10,$fn=48); circle(d=6.6,$fn=48); }}\n')
    part += cyl(0, 0, 11.7, 0.5, 6.6, "#1f1f22", fn=48)                       # dished centre, sunk
    s += f'translate([{x:.3f},{y:.3f},{z:.3f}]) rotate([{tilt:.2f},0,0]) {{\n{part}}}\n'
    return s

AT_FLAT_Y, AT_FOLD_D = 111.5, F.D_SW   # switch pair PARA | AFTERTOUCH (systems common 7.3 / fold 5.6): flat y 111.5
                                      # between the voice rows; FOLD d 26, moved outward to x 93.9 / 192.1

SW_NAMES = ("AFTERTOUCH", "PARA (MONO/PARA/PARA+4)")

def item5(name, lab, x, y, kind, midi, z, st, tap_style="acryl", type_pos=None, vel_above=False, centre=143.0, sw_in=True):
    if name in SW_NAMES or (name in ("VEL", "SOURCE", "OSC 3 CTL") and vel_above):
        s = st.tag(x, y, z, None) if st.tag else ""
        s += toggle(x, y, z)
        L = lab if st.upper else lab.lower()
        if name in SW_NAMES and not L:
            pass
        elif name in SW_NAMES:
            # mirrored pair: legends toward the centre (flat) or outward (FOLD, where the breaks sit inboard)
            right = (x < centre) == sw_in
            s += txt(x + SW_LAB_DX if right else x - SW_LAB_DX, y, z, L, st.lsize * 0.72, st.ink, font=st.font,
                     halign="left" if right else "right")
        else:
            s += txt(x, y + ABOVE_GAP, z, L, st.lsize * 0.85, st.ink, font=st.font)
        return s
    if kind == "y":
        s = st.tag(x, y, z, False) if st.tag else ""
        s += (st.knob)(x, y, z + ld.KNOB_GAP + st.kz_extra, random_ang((name,)))
        s += type_fan(x, y, z, st.knob_r, type_pos, st.scale_ink or st.ink, st.font, st.lsize * 0.72, st.upper,
                      bib=TAG if st.tag else None)
        s += txt(x, y - st.knob_r - st.lab_gap - 0.6, z, lab if st.upper else lab.lower(), st.lsize, st.ink, font=st.font)
        return s
    if kind == "b":
        s = tap_cap(x, y, z, tap_style)
        s += txt(x, y - 6 - st.lab_gap - 0.6, z, "TAP" if st.upper else "tap", st.lsize, st.ink, font=st.font)
        return s
    if kind == "s":
        s = joystick(x, y, z, st.ink)
        s += txt(x, y - 11.5, z, lab if st.upper else lab.lower(), st.lsize, st.ink, font=st.font)
        return s
    if kind == "l":
        s = led(x, y, z, col="#9fd36b" if lab else "#efe3c8")
        if lab:
            s += txt(x, y + 4.6, z, lab if st.upper else lab.lower(), st.lsize * 0.8, st.ink, font=st.font)
        return s
    return r4.item(lab, x, y, kind, midi, z, st, (name,))

def draw_row(rw, y, z, st, tap_style="acryl", which="P", vel_above=False, centre=143.0, sw_in=True):
    s = ""
    for name, lab, x, kind, midi, yo in rw:
        tp = ECHO_POS if name == "ECHO TYPE" else VERB_POS
        s += item5(name, lab, x, y + yo, kind, midi, z, st, tap_style, tp, vel_above, centre, sw_in)
    return s

# =================================================================== keys
def keys_raised(x0, y0, wz, skirt=False, white=ACRYL_W, sharp=ACRYL_K, bed="#0e0d0c", bed_z=None, front_y=None):
    """short tops; wz = white surface. skirt: option A (tops run forward to front_y with a 3 mm front skirt)."""
    s = ""
    for i in range(15):
        xa = x0 + 18 * i
        yf = front_y if skirt else y0
        s += box(xa + 0.3, yf, wz - 3, xa + 17.7, y0 + 30, wz, white)
        if skirt:
            s += box(xa + 0.3, yf, wz - 5, xa + 17.7, yf + 1.6, wz - 3, white)
    for i in sharps_after():
        xc = x0 + 18 * (i + 1)
        s += box(xc - 8, y0 + 32, wz - 1, xc + 8, y0 + 46, wz + 2, sharp)
    bz = (wz - 3.2 - 5) if bed_z is None else bed_z
    s += box(x0 - 0.2, y0 - 0.2, bz - 1, x0 + 270.2, y0 + 46.5, bz, bed)
    return s

# =================================================================== ONE SHEET
OS_W, OS_D, OS_Z = 276.0, 180.0, 24.0
OS_DX = -5.0
OS_HEAD_Y = 161.8      # S1: ECHO / REVERB baseline, above the type-name fan
OS_KZ = 26.5           # whites (2.5 proud)
OS_LEG = "#2e2924"     # one swap: legends and names in one dark
RING_BASE, RING_LN = "#ece2ca", "#cdbd9c"

def os_face(z):
    """two finishes only: smooth everywhere, rings round every rotary (drawn 1.1 pitch, 2.5x coarse)."""
    s = ""
    R = rows(OS_DX)
    for key, yy in (("P", 68), ("V1", 100), ("V2", 123), ("FX", 146)):
        for name, lab, x, kind, midi, yo in R[key]:
            if kind in "kgryh":
                r1 = 12.5 if kind == "h" else 9.25
                r0 = 10.9 if kind == "h" else 7.75
                s += halo(x, yy, z + 0.02, r0, r1, RING_BASE, RING_LN)
    return s

def one_sheet(edge="A", face=True):
    s = ""
    W, D, Z = OS_W, OS_D, OS_Z
    shell2d = rrect2d(0, 0, W, D, 6, 6)
    winA = "translate([3,-1]) square([270,50.5]);"
    win = winA if edge == "A" else "translate([3,3]) square([270,46.5]);"
    # walls + top in one (top edge R 2 drawn as steps)
    s += f'{c(PCREAM)} translate([0,0,0.5]) linear_extrude({Z-2-0.5:.2f}) difference(){{ {shell2d} {win} }}\n'
    for zz, inset, hh in ((Z - 2, 0.6, 0.6), (Z - 1.4, 0.0, 0.8), (Z - 0.6, 0.9, 0.6)):
        s += f'{c(PCREAM)} translate([0,0,{zz:.2f}]) linear_extrude({hh}) difference(){{ {rrect2d(inset, inset, W-inset, D-inset, 6-inset, 6-inset)} offset(delta={inset}) {win} }}\n'
    if edge == "A":
        s += box(3, 0, 0.5, 273, 2.4, 17.5, PCREAM)           # front wall under the keys drops to z 17.5
        s += box(3, 2.4, 0.5, 273, 4.0, 15.8, "#1a1816")       # dark inside of the shadow slot
    else:
        s += box(3, 0, 0.5, 273, 2.4, 24.3, PCREAM)             # lip y 0-2.4 up to 25.5, R 1.2 top
        s += f'{c(PCREAM)} translate([3,1.2,24.3]) rotate([0,90,0]) cylinder(h=270,r=1.2,$fn=24);\n'
    s += f'{c("#c99b62")} linear_extrude(0.5) offset(delta=-2.6) {shell2d}\n'
    if face:
        s += box(0.6, 49.6, Z + 0.004, W - 0.6, D - 0.6, Z + 0.006, "#ece2ca")
        s += os_face(Z + 0.005)
    # sunk grooves (0.6 x 1.2): two verticals through PLAY + VOICE, the full-width horizontal, the FX row's own two
    gz, g = Z + 0.05, "#b7a98e"
    vb, fb = breaks(OS_DX)
    for xb in vb:
        s += box(xb - 0.6, 52.6, gz, xb + 0.6, 133.5, gz + 0.03, g)
    s += box(4, 85.4 - 0.6, gz, W - 4, 85.4 + 0.6, gz + 0.03, g)
    for xb in fb:
        s += box(xb - 0.6, 138.5, gz, xb + 0.6, 156.5, gz + 0.03, g)
    tz = Z + 0.04
    for (tx, ty, name, ha) in [(vb[0] - 4, 81.0, "PITCH", "right"), (vb[1] - 4, 81.0, "FILTER", "right"), (W - 6, 81.0, "FX & OUT", "right"),
                               (6, 136.0, "OSCILLATORS", "left"), (138, 133.6, "MIXER", "center"), (W - 6, 136.0, "CONTOURS", "right")]:
        s += txt(tx, ty, tz, name, 1.8 if name == "MIXER" else 2.1, OS_LEG, font="Inter:style=Bold", halign=ha)
    # rear band: jack legend over the rear-wall ports, the label line
    for k, lab in enumerate(JACKS):
        s += txt(OJ0 + OJP * k, D - 9.0, tz, lab, 1.5, OS_LEG, font="Inter:style=Bold")
        s += box(OJ0 + OJP * k - 0.25, D - 6.8, tz, OJ0 + OJP * k + 0.25, D - 4.2, tz + 0.02, OS_LEG)
    s += txt(OJ0 - 17, D - 9.0, tz, "POWER", 1.5, OS_LEG, font="Inter:style=Bold")
    s += txt(8, D - 9.0, tz, "shell rev 5  ·  one filament, one swap  ·  printed face down", 1.7, OS_LEG, halign="left")
    s += keys_raised(3, 3, OS_KZ + KEY_LIFT, skirt=(edge == "A"), front_y=0.3)
    st = Style(ink=OS_LEG, lsize=1.9)
    s += cyl(25 + OS_DX, 68, Z - 0.1, 0.16, 18.6, "#efe9dc", fn=72)    # Delrin gate plate, round (S2: a bezel, not a fader track)
    R = rows(OS_DX)
    for key, yy in (("P", 68), ("V1", 100), ("V2", 123), ("FX", 146), ("SW", AT_FLAT_Y)):
        s += draw_row(R[key], yy, Z + 0.06, st, "acryl", vel_above=True, centre=143 + OS_DX)
    s += fx_heads(OS_DX, OS_HEAD_Y, Z + 0.06, OS_LEG, "Inter:style=Bold", 1.8, True)
    s += os_jacks()
    return s

def os_jacks(D=OS_D):
    s = ""
    for k in range(8):
        x = OJ0 + OJP * k
        if k == 7:
            s += box(x - 4.5, D - 0.3, 10.3, x + 4.5, D + 0.1, 13.7, "#1a1a1a")
        else:
            s += f'{c("#151515")} translate([{x},{D-0.25},12]) rotate([-90,0,0]) cylinder(h=0.4,d=4.6,$fn=24);\n'
    s += box(OJ0 - 17 - 5, D - 0.3, 10.5, OJ0 - 17 + 5, D + 0.1, 13.5, "#2a2826")
    return s

def one_sheet_under():
    s = one_sheet("A", face=False)
    W, D = OS_W, OS_D
    shell2d = rrect2d(0, 0, W, D, 6, 6)
    s += f'{c("#c99b62")} translate([0,0,-0.05]) linear_extrude(3.0) offset(delta=-2.6) {shell2d}\n'
    for (x, y) in [(10, 10), (138, 7), (W - 10, 10), (10, D - 10), (138, D - 7), (W - 10, D - 10), (7, 80), (W - 7, 80)]:
        s += cyl(x, y, -0.25, 0.2, 5.0, "#3b3e42", fn=20)
    for (x, y) in [(20, 20), (W - 20, 20), (20, D - 20), (W - 20, D - 20)]:
        s += cyl(x, y, -6, 5.95, 12, "#2a2a2a", fn=32)
    for k in range(-5, 6):
        for j in range(-5, 6):
            if k * k + j * j <= 25:
                s += cyl(240 + k * 4.2, 113 + j * 4.2, -0.15, 0.1, 2.4, "#2b2d30", fn=12)
    s += box(132, D / 2, -0.15, 144, D / 2 + 4, -0.05, "#2b2d30")
    return s

# =================================================================== HUSH
HU_W, HU_D, HU_FT = 290.0, 187.0, 25.5    # D 186 -> 187: S1 label pass
HU_DX = 2.0
HU_HEAD_Y = 162.6


def hush_body(edge="A", col=FELT):
    """pebble: plan R 20 front / R 44 rear; top round r 12 (option A: r 4 along the front, blending to r 12 by y 40)."""
    W, D, H = HU_W, HU_D, HU_FT
    if edge == "B":
        return f'{c(col)} ' + pebble(0, 0, W, D, H, 20, 44, 12, 6)
    pf = r4.corner_profile(20, H, 4, 6)
    pr = r4.corner_profile(44, H, 12, 6)
    pp = r4.corner_profile(12, H, 12, 6)
    out = f'{c(col)} hull(){{\n'
    for (cx, cy, p) in [(20, 20, pf), (W - 20, 20, pf), (44, D - 44, pr), (W - 44, D - 44, pr), (12, 44, pp), (W - 12, 44, pp)]:
        out += f' translate([{cx:.3f},{cy:.3f},0]) rotate_extrude($fn=160) polygon({p});\n'
    return out + "}\n"

def hush_tag(x, y, z, hero):
    return r4.hush_tag(x, y, z, hero)

def hush(edge="A", show_jacks=True):
    s = hush_body(edge)
    z = HU_FT
    vb, fb = breaks(HU_DX)
    for xb in vb:
        s += box(xb - 0.5, 56, z - 0.4, xb + 0.5, 133.5, z + 0.02, FELT_DEB)
    s += box(14, 85.4 - 0.5, z - 0.4, HU_W - 14, 85.4 + 0.5, z + 0.02, FELT_DEB)
    for xb in fb:
        s += box(xb - 0.5, 138.5, z - 0.4, xb + 0.5, 155.5, z + 0.02, FELT_DEB)
    # the FX plinth: a pressed field (0.3 deep, flush: R4) under the FX row, the instrument's base course
    for (tx, ty, name, ha) in [(vb[0] - 4, 81.6, "PITCH", "right"), (vb[1] - 4, 81.6, "FILTER", "right"), (HU_W - 14, 81.6, "FX & OUT", "right"),
                               (16, 136.5, "OSCILLATORS", "left"), (HU_W - 16, 136.5, "CONTOURS", "right")]:
        s += txt(tx, ty, z - 0.25, name, 2.6, FELT_DEB, font="Inter:style=Bold", halign=ha, h=0.3)
    s += txt(145, 134.6, z - 0.25, "MIXER", 2.0, FELT_DEB, font="Inter:style=Bold", h=0.3)
    wy, sy = (13.5, 36.0) if edge == "A" else (19.5, 42.0)
    for n in range(15):
        xc = 19 + 18 * n
        s += cyl(xc, wy, z - 0.15, 0.2, 19.0, FELT_DK, fn=48)
        s += cyl(xc, wy, z, 2.6, 7.0, "#d4b385", fn=24)
        s += cyl(xc, wy, z + 2.5 + KEY_LIFT, 1.7, 12.7, MAPLE, fn=48)
        s += f'{c(MAPLE)} translate([{xc},{wy},{z+4.2+KEY_LIFT}]) scale([1,1,0.28]) sphere(d=12.7,$fn=48);\n'
    for i in sharps_after():
        xc = 10 + 18 * (i + 1)
        s += cyl(xc, sy, z - 0.15, 0.2, 19.0, FELT_DK, fn=48)
        s += cyl(xc, sy, z, 3.4, 7.0, "#b98f5e", fn=24)
        s += cyl(xc, sy, z + 3.3 + KEY_LIFT, 1.7, 12.7, MAPLE_DK, fn=48)
        s += f'{c(MAPLE_DK)} translate([{xc},{sy},{z+5.0+KEY_LIFT}]) scale([1,1,0.28]) sphere(d=12.7,$fn=48);\n'
    st = Style(ink=r4.INK_H, font="Inter:style=Bold", lsize=1.75, tag=hush_tag, kz_extra=0.06, lab_gap=3.4)
    # S2: the stick's tag is round (a bezel, not a fader track); the gate ring and pointers print on it (felt can't hold them)
    s += r4.hush_tag(25 + HU_DX, 68, z, False) + cyl(25 + HU_DX, 68, z - 1.0, 1.06, 18.6, TAG, fn=64)
    R = rows(HU_DX)
    for key, yy in (("P", 68), ("V1", 100), ("V2", 123), ("FX", 146), ("SW", AT_FLAT_Y)):
        s += draw_row(R[key], yy, z + 0.06, st, "peg", vel_above=True, centre=143 + HU_DX)
    s += fx_heads(HU_DX, HU_HEAD_Y, z - 0.25, FELT_DEB, "Inter:style=Bold", 2.0, True, h=0.3)   # pressed, like MIXER
    for k, lab in enumerate(JACKS):
        s += txt(HJ0 + 19 * k, HU_D - 15.5, z - 0.25, lab, 1.9, FELT_DEB, font="Inter:style=Bold", h=0.3)
    s += txt(HJ0 - 17, HU_D - 15.5, z - 0.25, "POWER", 1.9, FELT_DEB, font="Inter:style=Bold", h=0.3)
    s += box(HJ0 - 22, HU_D - 20.5, z - 0.4, HJ0 + 19 * 7 + 8, HU_D - 20, z + 0.02, FELT_DEB)
    if show_jacks:
        s += hush_jacks()
    return s

JACKS = ["PHONES", "EXT IN", "FILTER CV", "PITCH CV", "GATE", "MIDI IN", "MIDI OUT", "USB-C"]   # MIDI OUT: owner, round 5
HJ0 = 76.0      # HUSH: 8 ports at 19 pitch, x 76-209, power at 59: inside the straight rear run (x 44-246)
OJ0, OJP = 152.0, 15.5   # ONE SHEET: 8 ports x 152-260.5, power at 135

def hush_jacks():
    s = ""
    for k in range(8):
        x = HJ0 + 19 * k
        if k == 7:
            s += box(x - 4.5, HU_D - 0.4, 8.0, x + 4.5, HU_D + 0.1, 11.4, "#1a1a1a")
        else:
            s += f'{c("#151515")} translate([{x},{HU_D-0.3},9.7]) rotate([-90,0,0]) cylinder(h=0.5,d=4.6,$fn=24);\n'
    s += box(HJ0 - 22, HU_D - 0.4, 8.2, HJ0 - 12, HU_D + 0.1, 11.2, "#2a2826")
    return s

def hush_under():
    s = hush_body("A")
    W, D = HU_W, HU_D
    z = -0.05
    ring = rrect2d(5, 5, W - 5, D - 5, 15, 39)
    inner = rrect2d(20, 20, W - 20, D - 20, 1, 24)
    s += f'{c("#8a8682")} translate([0,0,{z-1.6}]) linear_extrude(1.6) difference(){{ {ring} {inner} }}\n'
    s += ext(rrect2d(20.4, 20.4, W - 20.4, D - 20.4, 1, 23.6), z - 1.2, z, "#a39e97")
    for (x, y) in [(13, 30), (13, 120), (W - 13, 30), (W - 13, 120), (75, 12.5), (145, 12.5), (215, 12.5), (75, D - 12.5), (145, D - 12.5), (215, D - 12.5)]:
        s += cyl(x, y, z - 1.75, 0.2, 4.6, "#3b3e42", fn=20)
    for (x, y) in [(28, 28), (28, D - 28), (W - 28, 28), (W - 28, D - 28), (100, 28), (190, 28), (100, D - 24), (190, D - 24)]:
        s += cyl(x, y, z - 1.35, 0.2, 4.6, "#3b3e42", fn=20)
    for (x, y) in [(38, 38), (W - 38, 38), (38, D - 38), (W - 38, D - 38)]:
        s += cyl(x, y, z - 3.2, 2.0, 11, "#2a2a2a", fn=32)
    gx, gy = 243, 113
    for k in range(-4, 5):
        hw = math.sqrt(max(0, 400 - (k * 4.2) ** 2))
        s += box(gx - hw, gy + k * 4.2 - 0.9, z - 1.3, gx + hw, gy + k * 4.2 + 0.9, z - 1.22, "#2b2d30")
    s += box(140, D / 2, z - 1.3, 152, D / 2 + 4, z - 1.22, "#2b2d30")
    s += hush_jacks()
    return s

# =================================================================== FOLD
FO_W, BASE_H, LID_H, LID_PF = 286.0, 15.6, 34.5, 15.1
AX_Z = 25.0
FO_DX = 0.0
FO_IO_PWR = 66.0                                     # rev 5.6: power switch, then 6 jacks along the lid's far wall
FO_IO_JACKS = [90.0 + 25.0 * k for k in range(6)]    # phones, line out, EXT in, filter CV in, pitch CV out, gate out (x 90-215)
FO_USB_Y, FO_MIDI_Y = 94.0, 83.0                      # base right end face, y 80-100
FO_HEAD_D = 16.2       # S1: echo / reverb baseline, this far behind the back row
VAR = {105: dict(D=108.0, dV1=14.45, dV2=60.85, dFX=83.85, spk=(26.7, 56.7), grille=(28.0, 46.0),
                 cells=[(15, 103, 28.2, 55.2), (183, 271, 28.2, 55.2)]),
       113: dict(D=129.0, dV1=14.45, dV2=82.45, dFX=105.45, spk=(34.45, 64.45), grille=(36.0, 66.0),
                 cells=[(15, 80, 23.45, 75.45), (206, 271, 23.45, 75.45)])}

def fold_style():
    return Style(knob=lambda x, y, z, a: knob_black(x, y, z, a),
                 hero=lambda x, y, z, a: knob_hero(x, y, z, a, col=K_RED, line="#f3ead6"),
                 ink=FO_INK, font="Kalam:style=Bold", lsize=2.35, upper=False, knob_r=7.25, lab_gap=2.9)

class Fold:
    def __init__(self, v):
        self.v = v
        p = VAR[v]
        self.D = p["D"]; self.dV1, self.dV2, self.dFX = p["dV1"], p["dV2"], p["dFX"]
        self.AX_Y = self.D + 1.0; self.LY0 = self.D + 2.0
        self.p = p

    def base_plate2d(self):
        outer = rrect2d(4.3, 4.0, FO_W - 4.3, self.D - 4.3, 0, 7.7)
        return f"difference(){{ {outer} translate([8,2]) square([270,49]); }}"

    def lid_plate2d(self):
        return rrect2d(4.3, self.LY0 + 0.3, FO_W - 4.3, self.LY0 + self.D - 4.3, 0, 7.7)

    def axis_marks(self, z, y0, y1, col="#8d6b3c"):
        """the centreline, marked: a fine tick on the rim (rigging: the boat's centreline)"""
        return box(142.7, y0, z, 143.3, y1, z + 0.05, col)

    def base(self, walnut=WAL_P):
        D = self.D
        s = ""
        pocket = f"translate([0,0,11]) linear_extrude(10) {rrect2d(4, 4, FO_W-4, D-4, 0, 8)}"
        s += f'{c(walnut)} difference(){{ {pebble(0, 0, FO_W, D, BASE_H, 12, 12, 3, 6)} {pocket} }}\n'
        s += box(8, 4.4, 11, 278, 51, 12.6, "#0e0d0c")
        s += pg_layers(self.base_plate2d(), BASE_H)
        gz = BASE_H + 0.02
        for xb in F.vb_play:
            s += box(xb - 0.6, 53.5, gz, xb + 0.6, D - 5.5, gz + 0.03, "#d3cab8")      # the column rules run to the seam
        st = fold_style()
        s += cyl(25, 68, BASE_H - 0.05, 0.08, 18.6, "#e6dfcf", fn=72)     # S2: a round well tone under the stick, not a fader plate
        s += draw_row(rows(FO_DX)["P"], 68, BASE_H, st, "proof")
        for (tx, name) in [(14, "pitch"), (105.5, "filter"), (188.5, "effects & out")]:
            s += txt(tx, 85.0, BASE_H + 0.01, name, 2.4, FO_INK, font="Kalam:style=Bold", halign="left")
        s += f'{c("#c9a77c")} translate([143,{D-0.2},8]) rotate([-90,0,0]) cylinder(h=0.3,d=1.2,$fn=12);\n'
        s += r4.keys_flat(8, 4.5, 17.5 + KEY_LIFT, bed_z=12.6)
        s += f'{c("#c2a25e")} translate([142.6,-0.1,7.5]) cube([0.8,0.3,4]);\n'       # brass pin on the front rim: the axis
        # base right end face (rev 5.6): USB-C + TRS MIDI out, straight off the Daisy Seed (base rear right)
        s += box(FO_W - 0.3, FO_USB_Y - 4.5, 4.8, FO_W + 0.1, FO_USB_Y + 4.5, 8.2, "#1a1a1a")
        s += f'{c("#151515")} translate([{FO_W-0.25},{FO_MIDI_Y},6.5]) rotate([0,90,0]) cylinder(h=0.4,d=4.6,$fn=24);\n'
        return s

    def lid(self, walnut=WAL_P, plate=True, back_detail=True, controls=True, lift=0.0, stowed=True):
        D, L0 = self.D, self.LY0
        sh = rrect2d(4, L0 - 6, FO_W - 4, L0 + D - 4, 0, 8)
        pocket = f"translate([0,0,{LID_PF-2.5:.2f}]) linear_extrude(30) {sh}"
        s = f'{c(walnut)} difference(){{ {pebble(0, L0, FO_W, D, LID_H, 12, 12, 3, 6)} {pocket} }}\n'
        if plate:
            s += f"translate([0,0,{lift}]) {{\n" + self.lid_face(controls) + "}\n"
        # I/O (systems rev 5.6): audio/CV jacks + power switch in the lid's FAR wall, x 60-230; no I/O in either end face
        yw = L0 + D
        s += box(FO_IO_PWR - 5, yw - 0.3, 5.5, FO_IO_PWR + 5, yw + 0.1, 9.5, "#2a2826")          # recessed slide switch
        s += box(FO_IO_PWR - 1.5, yw - 0.1, 6.5, FO_IO_PWR + 1.5, yw + 0.3, 8.5, "#5a5754")
        for x in FO_IO_JACKS:
            s += f'{c("#151515")} translate([{x},{yw-0.25},7.5]) rotate([-90,0,0]) cylinder(h=0.4,d=4.6,$fn=24);\n'
        for xs in ((-0.06, FO_W - 0.2) if stowed else ()):   # brass lid-stays, stowed flush in the end faces
            s += box(xs, L0 + 30, 2.0, xs + 0.26, L0 + 30 + Fold.STAY_L, 10.0, "#c2a25e")
            s += f'{c("#8a6f38")} translate([{xs-0.02},{L0+30+4},6]) rotate([0,90,0]) cylinder(h=0.32,r=1.4,$fn=16);\n'
        if back_detail:
            for (x, y) in [(16, L0 + 12), (FO_W - 16, L0 + 12), (16, L0 + D - 12), (FO_W - 16, L0 + D - 12), (143, L0 + 12), (143, L0 + D - 12)]:
                s += cyl(x, y, -0.06, 0.1, 5.4, "#c2a25e", fn=24) + box(x - 1.8, y - 0.35, -0.1, x + 1.8, y + 0.35, -0.04, "#6a5228")
            for (x, y) in [(40, L0 + 30), (FO_W - 40, L0 + 30), (40, L0 + D - 30), (FO_W - 40, L0 + D - 30)]:
                s += cyl(x, y, -0.6, 0.6, 12, "#c9a77c", fn=32)
            for (x, y) in [(110, L0 + D / 2), (176, L0 + D / 2)]:
                s += cyl(x, y, -0.08, 0.1, 6, "#24170e", fn=24)
        return s

    def lid_face(self, controls=True):
        D, L0 = self.D, self.LY0
        s = pg_layers(self.lid_plate2d(), LID_PF)
        gz = LID_PF + 0.02
        for xb in F.vb_voice:
            s += box(xb - 0.6, L0 + 0.8, gz, xb + 0.6, L0 + self.dV2 + 9, gz + 0.03, "#d3cab8")
        for xb in F.vb_fx:
            s += box(xb - 0.6, L0 + self.dFX - 9, gz, xb + 0.6, L0 + self.dFX + 9, gz + 0.03, "#d3cab8")
        g0, g1 = self.p["grille"]
        n = int((g1 - g0) / 2.3)
        for k in range(n):
            yy = L0 + g0 + k * 2.3
            s += box(118, yy, LID_PF - 0.4, 168, yy + 1.25, LID_PF + 0.03, "#1d1b19")
        # blank name lozenge, on the axis behind TAP
        nz = L0 + self.dFX + 12.5
        s += f'{c(FO_INK)} translate([0,0,{gz}]) linear_extrude(0.04) difference(){{ {rrect2d(127,nz,159,nz+6,3,3)} {rrect2d(127.4,nz+0.4,158.6,nz+5.6,2.6,2.6)} }}\n'
        s += self.axis_marks(gz, L0 + D - 4.3, L0 + D - 6.5)
        if controls:
            st = fold_style()
            R = rows(FO_DX)
            s += draw_row(R["V1"], L0 + self.dV1, LID_PF, st, "proof")
            s += draw_row(R["V2"], L0 + self.dV2, LID_PF, st, "proof")
            s += draw_row(R["FX"], L0 + self.dFX, LID_PF, st, "proof")
            s += draw_row(R["SWF"], L0 + AT_FOLD_D, LID_PF, st, "proof", sw_in=False)
            s += fx_heads(FO_DX, L0 + self.dFX + FO_HEAD_D, LID_PF + 0.01, FO_INK, "Kalam:style=Bold", 2.0, False)
            for (tx, name, ha) in [(14, "oscillators", "left"), (143, "mixer", "center"), (272, "contours", "right")]:
                s += txt(tx, L0 + self.dV1 + 11.3, LID_PF + 0.01, name, 2.4, FO_INK, font="Kalam:style=Bold", halign=ha)
        return s

    def knuckles(self, walnut, part):
        s = ""
        AY = self.AX_Y
        segs = [(0.6, 3.6, "b"), (3.6, 6.6, "l"), (6.6, 9.6, "b"), (276.4, 279.4, "b"), (279.4, 282.4, "l"), (282.4, 285.4, "b")]
        for a, b, who in segs:
            if who != part:
                continue
            s += f'{c(walnut)} translate([{a+0.15},{AY},{AX_Z}]) rotate([0,90,0]) cylinder(h={b-a-0.3},r=4.8,$fn=40);\n'
            if who == "b":
                s += f'{c(walnut)} hull(){{ translate([{a+0.15},{AY},{AX_Z}]) rotate([0,90,0]) cylinder(h={b-a-0.3},r=4.8,$fn=40); translate([{a+0.15},{AY-10},{BASE_H-1}]) cube([{b-a-0.3},8,1]); }}\n'
            else:
                s += f'{c(walnut)} hull(){{ translate([{a+0.15},{AY},{AX_Z}]) rotate([0,90,0]) cylinder(h={b-a-0.3},r=4.8,$fn=40); translate([{a+0.15},{AY+1},{LID_PF}]) cube([{b-a-0.3},8,1]); }}\n'
        return s

    STAND = 60.0          # lid at 120 deg (systems rev 5.7): rotated 60 deg up from flat
    STAY_L = 44.4         # stay length (rev 5.7; was 52.4)

    def stays(self):
        """two brass stays deployed, in world coords: pivot at the lid back's edge, d 30; rubber tips on the table."""
        a = math.radians(self.STAND)
        vy, vz = self.LY0 + 30 - self.AX_Y, -AX_Z
        py = self.AX_Y + vy * math.cos(a) - vz * math.sin(a); pz = AX_Z + vy * math.sin(a) + vz * math.cos(a)
        ez = 0.0
        ty = py + math.sqrt(self.STAY_L ** 2 - (pz - ez) ** 2)
        self.stay_pts = (py, pz, ty)
        s = ""
        for x0 in (0.3, FO_W - 3.3):
            s += f'{c("#c2a25e")} hull(){{ translate([{x0},{py},{pz}]) rotate([0,90,0]) cylinder(h=3,r=4,$fn=24); translate([{x0},{ty-1.5},{ez+4}]) rotate([0,90,0]) cylinder(h=3,r=4,$fn=24); }}\n'
            s += f'{c("#8a6f38")} translate([{x0-0.3},{py},{pz}]) rotate([0,90,0]) cylinder(h=3.6,r=1.6,$fn=16);\n'
            s += cyl(x0 + 1.5, ty - 1.5, 0, 3.0, 9.0, "#1e1e1e", fn=24)
        return s

    def model(self, open_state=True, walnut=WAL_P, book=False):
        s = self.base(walnut) + self.knuckles(walnut, "b")
        lid = self.lid(walnut, stowed=(open_state != "stand")) + self.knuckles(walnut, "l")
        if open_state == "stand":
            s += f'translate([0,{self.AX_Y},{AX_Z}]) rotate([{self.STAND},0,0]) translate([0,{-self.AX_Y},{-AX_Z}]) {{\n{lid}}}\n'
            s += self.stays()
            return s
        if open_state:
            s += lid
        else:
            s += f'translate([0,{self.AX_Y},{AX_Z}]) rotate([180,0,0]) translate([0,{-self.AX_Y},{-AX_Z}]) {{\n{lid}}}\n'
            if book:
                s += r4.hardback(318, -10)
        return s

    def exploded(self, walnut=WAL_P, lift=58.0):
        """open; the lid's pickguard lifted with its board, cells, speaker and (dashed-in) Daisy Seed."""
        D, L0 = self.D, self.LY0
        s = self.base(walnut) + self.knuckles(walnut, "b") + self.lid(walnut, plate=False) + self.knuckles(walnut, "l")
        g = f"translate([0,0,{lift}]) {{\n" + self.lid_face()
        bz = LID_PF - 2.5 - 7
        s0, s1 = self.p["spk"]
        cuts = "".join(f"translate([{a},{L0+d0}]) square([{b-a},{d1-d0}]);" for a, b, d0, d1 in self.p["cells"])
        cuts += f"translate([113,{L0+s0}]) square([60,{s1-s0}]);"
        g += f'{c("#2f6b4f")} translate([0,0,{bz-1.6}]) linear_extrude(1.6) difference(){{ {rrect2d(12, L0 + 2, 274, L0 + D - 6, 0, 4)} {cuts} }}\n'
        g += box(113, L0 + s0, LID_PF - 2.5 - 10.3, 173, L0 + s1, LID_PF - 2.5, "#3b3d40")
        for a, b, d0, d1 in self.p["cells"]:
            g += box(a + 1, L0 + d0 + 1, LID_PF - 2.5 - 9.5, b - 1, L0 + d1 - 1, LID_PF - 2.5, "#5d6a7a")
        # far-wall I/O board (rev 5.6), standing inside the far wall (105: d 92-104)
        g += box(60, L0 + D - 10, bz - 1.6 - 9, 230, L0 + D - 8.4, bz - 1.6, "#2f6b4f")
        R = rows(FO_DX)
        for key, d in (("V1", self.dV1), ("V2", self.dV2), ("FX", self.dFX)):
            for name, lab, x, kind, midi, yo in R[key]:
                if kind in "kgry":
                    g += box(x - 4.75, L0 + d - 4.75, bz, x + 4.75, L0 + d + 4.75, bz + 7, "#2b55a0")
        g += "}\n"
        s += g
        s += f'{c("#9aa3ad")} hull(){{ translate([150,{D-6},{BASE_H-3}]) cube([24,1,0.4]); translate([150,{L0+4},{lift+bz-2}]) cube([24,1,0.4]); }}\n'
        return s

    def fx_shield(self):
        """Daisy Seed (51 x 18), systems rev 5.6: in the BASE, rear right strip (x 200-272, y 80..D-4), on the floor
        in a board cutout, USB-C toward the right end face. Base coords (x0, x1, y0, y1). Seated height UNVERIFIED."""
        return (219.0, 270.0, FO_USB_Y - 9.0, FO_USB_Y + 9.0)

# ------------------------------------------------------------------ orthographic elevations (front from the player / right end)
def shot_ortho(scene, name, view, a0, a1, b0, b1, wmax=300.0, px_per_mm=14, felt=False, wood=False):
    """view 'front': image x = world x, image up = z (camera at -y).  view 'right': image x = world y (front at left),
    image up = z (camera at +x). Two magenta markers fix the frame; output cropped exactly to [a0,a1] x [b0,b1]."""
    import subprocess
    import numpy as np
    from PIL import Image
    if view == "front":
        mk = box(a0 - 2, -32, b0 - 2, a0, -30, b0, "#ff00ff") + box(a1, -32, b1, a1 + 2, -30, b1 + 2, "#ff00ff")
        ca, cb = (a0 + a1) / 2, (b0 + b1) / 2
        dist = ((b1 - b0) + 20) / (2 * math.tan(math.radians(11.25)))
        cam = f"{ca:.2f},{-dist:.1f},{cb:.2f},{ca:.2f},0,{cb:.2f}"
    else:
        X = wmax + 30
        mk = box(X, a0 - 2, b0 - 2, X + 2, a0, b0, "#ff00ff") + box(X, a1, b1, X + 2, a1 + 2, b1 + 2, "#ff00ff")
        ca, cb = (a0 + a1) / 2, (b0 + b1) / 2
        dist = ((b1 - b0) + 20) / (2 * math.tan(math.radians(11.25)))
        cam = f"{wmax+dist:.1f},{ca:.2f},{cb:.2f},{wmax:.1f},{ca:.2f},{cb:.2f}"
    wmm, hmm = (a1 - a0) + 20, (b1 - b0) + 20
    size = (int(wmm * px_per_mm), int(hmm * px_per_mm))
    path = os.path.join(OUT, name + ".scad")
    with open(path, "w") as f:
        f.write("$fa=3; $fs=0.3;\n" + scene + mk)
    raw = os.path.join(OUT, name + "_raw.png")
    cmd = ["xvfb-run", "-a", "-s", "-screen 0 6400x4400x24", "openscad", "-o", raw, f"--imgsize={size[0]},{size[1]}",
           f"--camera={cam}", "--projection=o", "--colorscheme=Tomorrow", path]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    # orthographic: the view must be scaled to the frame; OpenSCAD's ortho scale follows distance, so we fit by markers
    im = np.asarray(Image.open(raw).convert("RGB")).astype(np.float32)
    mag = (im[..., 0] > 180) & (im[..., 1] < 100) & (im[..., 2] > 180) & (np.abs(im[..., 0] - im[..., 2]) < 40)
    ys, xs = np.where(mag)
    if len(xs) == 0:
        raise RuntimeError("markers not found " + r.stderr[-500:])
    h, w, _ = im.shape
    left = xs < w / 2
    ax0, ay1 = xs[left].max() + 1, ys[left].min()
    bx1, by0 = xs[~left].min(), ys[~left].max() + 1
    bg = im[2, 2].copy()
    im = np.where(mag[..., None], bg, im)
    isbg = np.all(np.abs(im - bg) < 3, axis=2)
    lit = np.clip(im * 1.12 + 6, 0, 255)
    im = np.where(isbg[..., None], np.array([243, 239, 232], np.float32), lit)
    img = Image.fromarray(im.astype(np.uint8)).crop((int(ax0), int(by0), int(bx1), int(ay1)))
    out = os.path.join(OUT, name + ".png")
    img.save(out)
    if felt:
        feltfill(out)
    if wood:
        woodfill(out)
    return out

def fp_rect(x0, y0, x1, y1):
    return box(x0, y0, 0, x1, y1, 0.2, "#000000")

def fp_pebble():
    return ext(rrect2d(5, 5, HU_W - 5, HU_D - 5, 15, 39), 0, 0.2, "#000000")

def jobs(SZ):
    F5, F3 = Fold(105), Fold(113)
    J = {
        # HUSH
        "r5_hu_main": lambda: shot4(hush("A"), fp_pebble(), "r5_hu_main", size=SZ, az=-30, el=34, dist=720, center=(145, 88, 12), grain_classes=("felt",), felt=True),
        "r5_hu_edgeA": lambda: shot4(hush("A"), fp_pebble(), "r5_hu_edgeA", size=SZ, az=-38, el=17, dist=175, center=(52, 22, 24), grain_classes=("felt",), felt=True),
        "r5_hu_edgeB": lambda: shot4(hush("B"), fp_pebble(), "r5_hu_edgeB", size=SZ, az=-38, el=17, dist=175, center=(52, 22, 24), grain_classes=("felt",), felt=True),
        "r5_hu_under": lambda: under_shot(hush_under(), "r5_hu_under", SZ, -150, -38, 720, (145, 78, 10)),
        "r5_hu_top": lambda: top4(hush("A", show_jacks=False), "r5_hu_top", -2, -2, HU_W + 2, HU_D + 2, px_per_mm=12, grain_classes=("felt",), felt=True),
        "r5_hu_frontA": lambda: shot_ortho(hush("A"), "r5_hu_frontA", "front", -2, HU_W + 2, -1, 40, felt=True),
        "r5_hu_frontB": lambda: shot_ortho(hush("B"), "r5_hu_frontB", "front", -2, HU_W + 2, -1, 40, felt=True),
        "r5_hu_endA": lambda: shot_ortho(hush("A"), "r5_hu_endA", "right", -2, HU_D + 2, -1, 40, wmax=HU_W, felt=True),
        "r5_hu_endB": lambda: shot_ortho(hush("B"), "r5_hu_endB", "right", -2, HU_D + 2, -1, 40, wmax=HU_W, felt=True),
        # ONE SHEET
        "r5_os_main": lambda: ld.shot(one_sheet("A"), fp_rect(0, 0, OS_W, OS_D), "r5_os_main", size=SZ, az=-30, el=36, dist=700, center=(138, 82, 12), grain_classes=()),
        "r5_os_edgeA": lambda: ld.shot(one_sheet("A"), fp_rect(0, 0, OS_W, OS_D), "r5_os_edgeA", size=SZ, az=-38, el=17, dist=165, center=(50, 22, 24), grain_classes=()),
        "r5_os_edgeB": lambda: ld.shot(one_sheet("B"), fp_rect(0, 0, OS_W, OS_D), "r5_os_edgeB", size=SZ, az=-38, el=17, dist=165, center=(50, 22, 24), grain_classes=()),
        "r5_os_under": lambda: under_shot(one_sheet_under(), "r5_os_under", SZ, -150, -38, 700, (138, 80, 10)),
        "r5_os_top": lambda: top4(one_sheet("A"), "r5_os_top", -2, -2, OS_W + 2, OS_D + 2, px_per_mm=12, grain_classes=()),
        "r5_os_frontA": lambda: shot_ortho(one_sheet("A"), "r5_os_frontA", "front", -2, OS_W + 2, -1, 40),
        "r5_os_frontB": lambda: shot_ortho(one_sheet("B"), "r5_os_frontB", "front", -2, OS_W + 2, -1, 40),
        "r5_os_endA": lambda: shot_ortho(one_sheet("A"), "r5_os_endA", "right", -2, OS_D + 2, -1, 40, wmax=OS_W),
        "r5_os_endB": lambda: shot_ortho(one_sheet("B"), "r5_os_endB", "right", -2, OS_D + 2, -1, 40, wmax=OS_W),
    }
    for v, Fo in ((105, F5), (113, F3)):
        D = Fo.D; OPEN = 2 * D + 2
        J.update({
            f"r5_fo{v}_main": (lambda Fo=Fo, v=v, OPEN=OPEN: shot4(Fo.model(True), fp_rect(0, 0, FO_W, OPEN), f"r5_fo{v}_main", size=SZ, az=-30, el=44, dist=880 + (OPEN - 218) * 2.2, center=(143, OPEN / 2, 12), grain_classes=(), wood=True)),
            f"r5_fo{v}_closed": (lambda Fo=Fo, v=v, D=D: shot4(Fo.model(False), fp_rect(0, 0, FO_W, D), f"r5_fo{v}_closed", size=SZ, az=-28, el=30, dist=640, center=(143, D / 2, 22), grain_classes=(), wood=True)),
            f"r5_fo{v}_exploded": (lambda Fo=Fo, v=v, OPEN=OPEN: shot4(Fo.exploded(), fp_rect(0, 0, FO_W, OPEN), f"r5_fo{v}_exploded", size=SZ, az=-24, el=38, dist=980 + (OPEN - 218) * 2.2, center=(143, OPEN / 2 + 4, 30), grain_classes=(), wood=True)),
            f"r5_fo{v}_top": (lambda Fo=Fo, v=v, OPEN=OPEN: top4(Fo.model(True), f"r5_fo{v}_top", -2, -2, FO_W + 2, OPEN + 2, px_per_mm=12, grain_classes=())),
            f"r5_fo{v}_front_open": (lambda Fo=Fo, v=v: shot_ortho(Fo.model(True), f"r5_fo{v}_front_open", "front", -2, FO_W + 2, -1, 40, wood=True)),
            f"r5_fo{v}_front_closed": (lambda Fo=Fo, v=v: shot_ortho(Fo.model(False), f"r5_fo{v}_front_closed", "front", -2, FO_W + 2, -1, 54, wood=True)),
            f"r5_fo{v}_end_open": (lambda Fo=Fo, v=v, OPEN=OPEN: shot_ortho(Fo.model(True), f"r5_fo{v}_end_open", "right", -2, OPEN + 2, -1, 40, wmax=FO_W, wood=True)),
            f"r5_fo{v}_stand": (lambda Fo=Fo, v=v, D=D: shot4(Fo.model("stand"), fp_rect(0, 0, FO_W, D + 64), f"r5_fo{v}_stand", size=SZ, az=-32, el=24, dist=760, center=(143, D * 0.6, 50), grain_classes=(), wood=True)),
            f"r5_fo{v}_stand_side": (lambda Fo=Fo, v=v, D=D: shot_ortho(Fo.model("stand"), f"r5_fo{v}_stand_side", "right", -4, D + 84, -1, D + 34, wmax=FO_W, wood=True)),
            f"r5_fo{v}_end_closed": (lambda Fo=Fo, v=v, D=D: shot_ortho(Fo.model(False), f"r5_fo{v}_end_closed", "right", -2, D + 8, -1, 54, wmax=FO_W, wood=True)),
        })
    J["r5_fo105_closed_wal"] = lambda: ld.shot(F5.model(False, walnut=WAL_R, book=True), fp_rect(0, 0, FO_W, F5.D) + fp_rect(318, -10, 553, 146), "r5_fo105_closed_wal", size=SZ, az=-26, el=28, dist=1100, center=(275, 60, 22), grain_classes=("walnut",), grain_angle=-25)
    return J

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
