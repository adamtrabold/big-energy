"""CATHEDRAL steer 2 geometry check (systems, 2026-11-13): evenly spaced lid rows, a Ø 46 speaker window on the
axis above CUTOFF, the base PLAY row symmetric (stick left, TAP right, CUTOFF on the axis), and the two routes
R-TALL / R-LOW for closing. Run: python3 -I design/branches/concepts/cathedral/layout_check.py
Rules as fold_r5_check: same-row knob pitch >= 20, gaps >= 1.5, lid edge >= 16, seam >= 7, far rim, window >= 1.5;
closed: every lid item landing within 3 mm (plan) of a base item clears it by >= 2.0 in z; legends (estimated
Kalam metrics: width 0.50 x size per char, height 0.85 x size) >= 1.5 from controls and other legends, >= 1.0 from
the window. CATHEDRAL today: lid face closed z 37.6 (closed 52.7 incl. pegs, lid +2.6)."""
import math, itertools
KN, TGL, CUT, STK, TAPR = 7.45, 4.6, 10.4, 6.0, 6.0
D = 108.0
V1, SWL, V2, FX = 14.45, 32.0, 49.5, 84.55          # evenly spaced (V1 -> V2 -> FX 35.05), switch line between V1 and V2
WIN = (143.0, 32.0, 23.0)                          # Ø 46 opening, concentric with the 50 mm driver
LS = 2.35                                          # FOLD legend size (Kalam)

lid = []   # name, x, d, r, kind, legend, legend placement ('front','behind','above','side-l','side-r')
def L(n, x, d, r, k, lab=None, where="front"): lid.append((n, x, d, r, k, lab if lab is not None else n.lower(), where))
for n, x in [("RANGE 1", 23.5), ("RANGE 2", 43.5), ("RANGE 3", 63.5), ("FREQ 2", 83.5), ("OSC 1", 103.5), ("OSC 3", 182.5),
             ("F ATTACK", 202.5), ("F DECAY", 222.5), ("F SUSTAIN", 242.5)]:
    L(n, x, V1, KN, "k", {"RANGE 1": "range", "RANGE 2": "range", "RANGE 3": "range", "F ATTACK": "attack", "F DECAY": "decay",
                          "F SUSTAIN": "sustain"}.get(n, n.lower()))
L("KBD CTRL", 262.5, V1, TGL, "t", "kbd", "above")
for n, x in [("WAVE 1", 23.5), ("WAVE 2", 43.5), ("WAVE 3", 63.5), ("FREQ 3", 83.5), ("OSC 2", 103.5), ("NOISE/EXT", 182.5),
             ("L ATTACK", 202.5), ("L DECAY", 222.5), ("L SUSTAIN", 242.5)]:
    L(n, x, V2, KN, "k", {"WAVE 1": "wave", "WAVE 2": "wave", "WAVE 3": "wave", "NOISE/EXT": "noise / ext", "L ATTACK": "attack",
                          "L DECAY": "decay", "L SUSTAIN": "sustain"}.get(n, n.lower()), "behind")
L("DECAY tgl", 262.5, V2, TGL, "t", "decay", "behind")
for n, x in [("OSC MOD", 23.5), ("OSC 3 CTL", 43.5), ("PARA", 63.5), ("SOURCE", 182.5), ("FILTER MOD", 202.5), ("VEL", 222.5),
             ("AFTERTOUCH", 242.5)]:
    L(n, x, SWL, TGL, "t", {"OSC 3 CTL": "osc 3", "VEL": "velocity", "AFTERTOUCH": "touch", "FILTER MOD": "filt mod", "PARA": "para"}.get(n, n.lower()), "above")
fx = [("ECHO TYPE", 62.5, "type", "front"), ("ECHO TIME", 82.5, "time", "behind"), ("ECHO REPEATS", 102.5, "repeats", "behind"),
      ("ECHO MIX", 122.5, "mix", "front"), ("DELAY PAN", 142.5, "delay pan", "front"), ("REVERB TYPE", 171.5, "type", "front"),
      ("REVERB DECAY", 191.5, "decay", "front"), ("REVERB MIX", 211.5, "mix", "front"), ("DRY PAN", 240.5, "dry pan", "behind"),
      ("VOLUME", 260.5, "volume", "behind")]
for n, x, lab, w in fx: L(n, x, FX, KN, "k", lab, w)
L("FREE/SYNC", 96.0, FX - 14.85, TGL, "t", "free|sync", "beside")
L("FOLLOW", 250.5, FX - 11.55, TGL, "t", "off|follow", "beside")

def base(hk, hstick, hcut=12.15, htap=8.0):
    """PLAY row, symmetric about x 143: stick ↔ TAP, CUTOFF (hero) on the axis. R3 = director's call (counted as a knob)."""
    return [("BEND stick", 25, 68, STK, hstick), ("MOD", 47, 68, KN, hk), ("TUNE", 67, 68, KN, hk), ("GLIDE", 87, 68, KN, hk),
            ("EMPHASIS", 119, 68, KN, hk), ("CUTOFF", 143, 68, CUT, hcut), ("CONTOUR AMT", 167, 68, KN, hk),
            ("MOD MIX", 199, 68, KN, hk), ("DRIFT", 219, 68, KN, hk), ("R3 (open)", 239, 68, KN, hk), ("TAP", 261, 68, TAPR, htap)]

def tbox(x, d, s, size, where, r):
    w = len(s) * 0.50 * size; h = 0.85 * size
    if where == "front": cy = d - r - 2.9 - 0.6
    elif where == "behind": cy = d + r + 2.9 + 0.6
    elif where == "above": cy = d + 7.6
    else: cy = d
    return (x - w / 2, cy - h / 2, x + w / 2, cy + h / 2)

def gap_bc(b, cx, cy, r):
    dx = max(b[0] - cx, 0, cx - b[2]); dy = max(b[1] - cy, 0, cy - b[3]); return math.hypot(dx, dy) - r
def gap_bb(a, b):
    dx = max(b[0] - a[2], a[0] - b[2], 0); dy = max(b[1] - a[3], a[1] - b[3], 0)
    return -1 if dx == 0 and dy == 0 else (math.hypot(dx, dy) if dx and dy else max(dx, dy))

def labels():
    out = []
    for n, x, d, r, k, lab, w in lid:
        if w == "beside":
            a, b = lab.split("|"); s = LS * 0.72
            out.append((n + ":" + a, (x - 6.2 - len(a) * 0.5 * s, d - 0.43 * s * 1.0, x - 6.2, d + 0.43 * s)))
            out.append((n + ":" + b, (x + 6.2, d - 0.43 * s, x + 6.2 + len(b) * 0.5 * s, d + 0.43 * s)))
        else:
            out.append((n, tbox(x, d, lab, LS if k == "k" else LS * 0.85, w, r)))
    return out

def check():
    bad = []
    for a, b in itertools.combinations(lid, 2):
        dd = math.dist(a[1:3], b[1:3])
        if a[4] == b[4] == "k" and a[2] == b[2] and dd < 20 - 1e-6: bad.append(f"PITCH {a[0]}/{b[0]} {dd:.2f}")
        if dd - a[3] - b[3] < 1.5 - 1e-6: bad.append(f"GAP {a[0]}/{b[0]} {dd - a[3] - b[3]:.2f}")
    for n, x, d, r, k, *_ in lid:
        if math.dist((x, d), WIN[:2]) - r - WIN[2] < 1.5 - 1e-6: bad.append(f"WINDOW {n}")
        if x - r < 16 - 1e-6 or 286 - (x + r) < 16 - 1e-6: bad.append(f"EDGE {n}")
        if d - r < 7 - 1e-6: bad.append(f"SEAM {n}")
        if d + r > D - 4 - 12 + 1e-6: bad.append(f"FAR RIM {n}")
    labs = labels()
    for ln, b in labs:
        for n, x, d, r, k, *_ in lid:
            if gap_bc(b, x, d, r) < 1.5 - 1e-6: bad.append(f"LABEL {ln} vs {n} {gap_bc(b, x, d, r):.2f}")
        if gap_bc(b, *WIN) < 1.0: bad.append(f"LABEL {ln} vs window {gap_bc(b, *WIN):.2f}")
        if b[3] > D - 4 or b[1] < 0.5: bad.append(f"LABEL {ln} off the plate")
    for (a, ba), (b, bb) in itertools.combinations(labs, 2):
        if gap_bb(ba, bb) < 1.5 - 1e-6: bad.append(f"LABEL {a} vs {b} {gap_bb(ba, bb):.2f}")
    return bad

def closed_need(bs, hlid=13.5, peg_top=15.6 + 6.5):
    need, worst = peg_top + 2.0 + hlid, ("pegs", "")
    for n, x, d, r, k, *_ in lid:
        for bn, bx, by, br, bh in bs:
            if math.dist((x, D - d), (bx, by)) - r - br < 3 - 1e-6 and 15.6 + bh + 2.0 + hlid > need:
                need, worst = 15.6 + bh + 2.0 + hlid, (n, bn)
    return need, worst

if __name__ == "__main__":
    v = check()
    print(f"open layout + labels: {len(v)} violations"); [print("  ", x) for x in v]
    print("closed (lid face today z 37.6; closed 52.7):")
    for nm, hk, hs in [("R-TALL: today's knobs (13.5), stick 12.6", 13.5, 12.6),
                       ("R-LOW: Tayda 10 x 8 knobs (seat 1.0 → 9.0), stick as is 12.6", 9.0, 12.6),
                       ("R-LOW: Tayda 10 x 8 (9.0), stick lowered to 9.0", 9.0, 9.0),
                       ("R-LOW: Tayda 10 x 8 with a nut under it (10.5), stick 9.0", 10.5, 9.0)]:
        need, w = closed_need(base(hk, hs))
        print(f"  {nm}: face ≥ {need:.2f} → +{need - 37.6:.1f} → closed ≈ {52.7 + need - 37.6:.1f} mm (binding: {w[0]} over {w[1]})")
    print("base items under the window:", [b[0] for b in base(9, 9) if math.dist((b[1], D - b[2]), WIN[:2]) - b[3] < WIN[2]])
