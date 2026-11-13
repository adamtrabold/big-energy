"""FOLD round 5 layout check: same rules as layout_r4_check.py, in FOLD open coordinates,
for both variants, plus the closed-landing checks.  Run: python3 fold_r5_check.py
Coordinates: FOLD x (286 wide). Rev 5.1: FOLD has its own balanced x layout (mirror about x 143); the common layout still governs HUSH and ONE SHEET. y from the base's front edge, open.
Lid distance d from the hinge edge; open y = D + d; closed, d lands over base y = D - d.
"""
import math, itertools

KN = 7.45; CUT = 10.4; TGL = 4.6; STK = 6.0; LED3 = 1.5; LED5 = 2.5
W = 286
P = 68                       # base PLAY row (settled)
SHARP_TOP, WHITE_TOP = 19.5, 17.5
LID_FACE_CLOSED = 35.0       # lid plate face, closed (base 15.6 + lid hollow 19.4)
KNOB_H = 13.5                # black 18T knob height; lid knob bottoms closed = 21.5
BASE_PLATE = 15.6
SEAM_MARGIN = 7.0            # knob edge >= 7 from the seam (it is the PLAY|VOICE break, R2)
RIM_MARGIN = 12.0            # lid side/far rims rise when open (R4)
RIM = 4.0

play = [  # name, x, r, kind  (FOLD x) -- rev 5.1 balanced row: mirror-symmetric about x 143
    ("BEND stick", 25, STK, "stick"), ("MOD", 47, KN, "k"), ("TUNE", 67, KN, "k"), ("GLIDE", 87, KN, "k"),
    ("CUTOFF", 119, CUT, "k"), ("not-in-ctl", 131, LED3, "l", 81), ("EMPHASIS", 143, KN, "k"),
    ("status", 155, LED5, "l", 81), ("CONTOUR AMT", 167, KN, "k"),
    ("ECHO REPEATS", 199, KN, "k"), ("ECHO MIX", 219, KN, "k"), ("REVERB MIX", 239, KN, "k"), ("TAP", 261, 6.0, "b"),
]
TL, TR = 109.25, 176.75     # lid toggle columns flanking the mixer
v1 = [("RANGE 1", 23.5, KN, "k"), ("RANGE 2", 43.5, KN, "k"), ("RANGE 3", 63.5, KN, "k"),
      ("FREQ 2", 83.5, KN, "k"), ("OSC MOD", TL, TGL, "t"), ("OSC 1", 123, KN, "k"),
      ("OSC 3", 143, KN, "k"), ("MOD MIX", 163, KN, "k"), ("FILTER MOD", TR, TGL, "t"),
      ("F ATTACK", 202.5, KN, "k"), ("F DECAY", 222.5, KN, "k"), ("F SUSTAIN", 242.5, KN, "k"),
      ("KBD CTRL", 262.5, TGL, "t")]
v2 = [("WAVE 1", 23.5, KN, "k"), ("WAVE 2", 43.5, KN, "k"), ("WAVE 3", 63.5, KN, "k"),
      ("FREQ 3", 83.5, KN, "k"), ("OSC 3 CTL", TL, TGL, "t"), ("OSC 2", 123, KN, "k"),
      ("NOISE/EXT", 143, KN, "k"), ("SOURCE", 163, TGL, "t"), ("VEL", TR, TGL, "t"),
      ("L ATTACK", 202.5, KN, "k"), ("L DECAY", 222.5, KN, "k"), ("L SUSTAIN", 242.5, KN, "k"),
      ("DECAY tgl", 262.5, TGL, "t")]
vb_play = [101.5, 184.5]; vb_voice = [101.5, 184.5]   # the same break lines on both halves
TAPR = 6.0   # TAP button cap (UNVERIFIED part), treated like a knob for margins
fx = [("DRIFT", 79.5, KN, "k"), ("ECHO TYPE", 108.5, KN, "k"), ("ECHO TIME", 128.5, KN, "k"),
      ("REVERB DECAY", 157.5, KN, "k"), ("REVERB TYPE", 177.5, KN, "k"), ("VOLUME", 206.5, KN, "k")]
# back row = the chain in one line: drift (source) | echo | reverb | volume (out)
vb_fx = [94, 143, 192]
# key/voice-assignment switch pair, mirrored about 143 (FOLD: at d 26, between V1 and the band)
sw = [("PARA (MONO/PARA/PARA+4)", 93.9, TGL, "t"), ("AFTERTOUCH", 192.1, TGL, "t")]
D_SW = 26.0
# flat concepts put the same pair mid-way between the VOICE rows, in the switch columns
sw_flat = [("PARA (MONO/PARA/PARA+4)", TL, TGL, "t"), ("AFTERTOUCH", TR, TGL, "t")]
KNUCKLES = [(0, 10), (276, 286)]

VARIANTS = {  # D, lid row d (V1, V2)
    "FOLD-105 (slim battery)": dict(D=108, dV1=14.45, dV2=60.85, dFX=83.85),
    "FOLD-113 (big battery)":  dict(D=129, dV1=14.45, dV2=82.45, dFX=105.45),
}

def check(name, D, dV1, dV2, dFX):
    bad = 0
    items = [(e[0], e[1], e[4] if len(e) > 4 else P, e[2], e[3], "base") for e in play]
    items += [(n, x, D + dV1, r, k, "V1") for n, x, r, k in v1]
    items += [(n, x, D + dV2, r, k, "V2") for n, x, r, k in v2]
    items += [(n, x, D + dFX, r, k, "FX") for n, x, r, k in fx]
    items += [(n, x, D + D_SW, r, k, "SW") for n, x, r, k in sw]
    # 1. same rules as layout_r4_check.py
    for a, b in itertools.combinations(items, 2):
        d = math.dist(a[1:3], b[1:3])
        if a[4] == "k" and b[4] == "k" and a[2] == b[2]:
            need = 24 if {a[0], b[0]} <= {"CUTOFF", "EMPHASIS", "CONTOUR AMT"} else 20
            if d < need - 1e-6: print("  PITCH", a[0], b[0], d); bad += 1
        if d - a[3] - b[3] < 1.5: print("  GAP", a[0], b[0], round(d - a[3] - b[3], 2)); bad += 1
    for n, x, y, r, k, h in items:
        need = 7 if k in ("k", "stick", "b") else 3 if k == "t" else 1
        for b in (vb_play if h == "base" else vb_fx if h == "FX" else vb_voice):
            if abs(x - b) - r < need - 1e-6: print("  BREAK", n, b, round(abs(x - b) - r, 2)); bad += 1
        # the seam is the horizontal break
        if abs(y - D) - r < (SEAM_MARGIN if k in ("k", "stick", "b") else 3) - 1e-6:
            print("  SEAM", n, round(abs(y - D) - r, 2)); bad += 1
        # side edges: base >= 10 from the outside (flush rims); lid >= rim + 12 (rims rise)
        lim = 10 if h == "base" else RIM + RIM_MARGIN
        if x - r < lim - 1e-6 or W - (x + r) < lim - 1e-6: print("  EDGE", n); bad += 1
        if h != "base":
            for k0, k1 in KNUCKLES:
                g = (k0 - (x + r)) if x < k0 else (x - r - k1) if x > k1 else -1
                if g < 5 and y - D - r < 15: print("  KNUCKLE", n, round(g, 2)); bad += 1
    # far rim
    far = max(dV2, dFX) + KN + RIM_MARGIN + RIM
    if far > D + 1e-6: print("  FAR RIM", far, D); bad += 1
    # 2. closed landing: lid knob lands at base y = D - d; plan gap >= 3 to any base control
    report = []
    for n, x, r, k, row, dd in [(n, x, r, k, "V1", dV1) for n, x, r, k in v1] + \
                               [(n, x, r, k, "V2", dV2) for n, x, r, k in v2] + \
                               [(n, x, r, k, "FX", dFX) for n, x, r, k in fx] + \
                               [(n, x, r, k, "SW", D_SW) for n, x, r, k in sw]:
        yl = D - dd
        for bn, bx, br, bk, *_ in play:
            if bk == "l": continue
            g = math.dist((x, yl), (bx, P)) - r - br
            if g < 3 - 1e-6: print("  CLOSED PLAN", n, bn, round(g, 2)); bad += 1
        # what it lands over, and z clearance
        lo, hi = yl - r, yl + r
        bottom = LID_FACE_CLOSED - KNOB_H
        if hi <= 4.5 or lo >= 54.6 + 3 - 3:   # lands behind the keys: over the base plate
            under = BASE_PLATE; what = "base plate"
            if hi > D - RIM: print("  LANDS ON RIM", n); bad += 1
            if lo < P + CUT + 3 - 1e-6 and lo > P: pass
        else:
            under = SHARP_TOP if hi > 36.5 else WHITE_TOP
            what = "sharps" if hi > 36.5 else "whites"
        clr = bottom - under
        if clr < 2.0 - 1e-6: print("  CLOSED Z", n, clr); bad += 1
        report.append((row, n, round(yl, 2), what, round(clr, 2)))
    # 3. summary numbers
    gap_c = (D + dV1) - P
    print(f"{name}: half 286 x {D}; open 286 x {2*D}; V1 d {dV1} (open y {D+dV1:.2f}), "
          f"V2 d {dV2} (open y {D+dV2:.2f})")
    print(f"  PLAY row -> V1 (centres) {gap_c:.2f}; clear between knob edges "
          f"{(D+dV1-KN)-(P+CUT):.2f} (CUTOFF) / {(D+dV1-KN)-(P+KN):.2f} (others)")
    print(f"  V1 -> V2 pitch {dV2-dV1:.2f}; clear band between knob edges {dV2-dV1-2*KN:.2f}")
    print(f"  V2 -> FX row pitch {dFX-dV2:.2f}; FX knob edge -> rim {D-RIM-(dFX+KN):.2f}; back row open y {D+dFX:.2f}")
    if dV2 - 6 - 22.45 < 0: print("  band?")
    print(f"  band under the plate (V1 pins 22.45 -> V2 footprint {dV2-6:.2f}): {dV2-6-22.45:.2f}")
    print(f"  stick -> CUTOFF {math.dist((25,P),(119,P)):.1f}; CUTOFF|EMPHASIS pitch 24, same row")
    rows = {}
    for row, n, yl, what, clr in report:
        rows.setdefault(row, set()).add((yl, what, clr))
    for row, s in rows.items():
        print(f"  closed {row}: lands at base y, over, z clearance -> {sorted(s)}")
    for row, lst in (("PLAY", play), ("V1", v1), ("V2", v2), ("FX", fx), ("SW", sw)):
        xs = sorted(e[1] for e in lst)
        asym = max(abs((a + b) / 2 - 143) for a, b in zip(xs, reversed(xs)))
        print(f"  mirror about x 143, {row}: worst slot offset {asym:.2f} mm")
    print(f"  violations {bad}\n")
    return bad

total = sum(check(n, **v) for n, v in VARIANTS.items())
print("TOTAL violations", total)
