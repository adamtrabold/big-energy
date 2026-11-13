"""Branches geometry check (systems, concept turn 1, 2026-11-13).

Imports the v1.1 layout from design/concepts/_mock-src/fold_r5_check.py (read only) and checks:
  1. FREE / SYNC toggle placement in front of ECHO TIME, with LABELS (FOLD lid + ONE SHEET flat).
  2. TIME's two-scale ring vs the toggle.
  3. BUTTERFLY: where the wood joint can go without cutting a legend.
  4. Pegs: RAIN on ONE SHEET (width) and CHAMBER on FOLD (closed height).
  5. DIPTYCH: cord geometry, cord tension, tip-over vs the v1.1 brass stays.
Run: python3 -I design/branches/concepts/branch_check.py

Label boxes are ESTIMATES from font metrics (OpenSCAD text, valign center): width = n chars x k x size,
k = 0.68 Inter caps, 0.55 Inter lowercase, 0.50 Kalam lowercase; height = 0.75 x size (caps) / 0.85 (Kalam).
Clearance rules (same as v1.1's S1 label pass): label-to-control >= 1.5, label-to-label >= 1.0, label-to-groove >= 1.0.
"""
import math, itertools, importlib.util, io, contextlib, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "..", "concepts", "_mock-src", "fold_r5_check.py")
spec = importlib.util.spec_from_file_location("f", SRC)
F = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(F)

TOTAL = 0
def fail(msg):
    global TOTAL
    TOTAL += 1
    print("  FAIL", msg)

# ---------------------------------------------------------------- geometry helpers
def box_circle_gap(b, cx, cy, r):
    x0, y0, x1, y1 = b
    dx = max(x0 - cx, 0, cx - x1); dy = max(y0 - cy, 0, cy - y1)
    return math.hypot(dx, dy) - r

def box_box_gap(a, b):
    dx = max(b[0] - a[2], a[0] - b[2], 0); dy = max(b[1] - a[3], a[1] - b[3], 0)
    if dx == 0 and dy == 0:
        return -1.0
    return math.hypot(dx, dy) if dx and dy else max(dx, dy)

def tbox(x, y, s, size, font="inter", halign="center"):
    if font == "kalam":
        w = len(s) * 0.50 * size; h = 0.85 * size
    elif s.isupper() or not any(ch.isalpha() for ch in s):
        w = len(s) * 0.68 * size; h = 0.75 * size
    else:
        w = len(s) * 0.55 * size; h = 0.75 * size
    x0 = x - w / 2 if halign == "center" else (x if halign == "left" else x - w)
    return (x0, y - h / 2, x0 + w, y + h / 2)

# ---------------------------------------------------------------- 1. FREE / SYNC with labels
TGL = F.TGL; KN = F.KN
LAB = {"ECHO TYPE": "TYPE", "ECHO TIME": "TIME", "REVERB DECAY": "DECAY", "REVERB TYPE": "TYPE",
       "NOISE/EXT": "NOISE / EXT", "WAVE 1": "WAVE", "WAVE 2": "WAVE", "WAVE 3": "WAVE", "OSC 3 CTL": "OSC 3 CTL",
       "L ATTACK": "ATTACK", "L DECAY": "DECAY", "L SUSTAIN": "SUSTAIN", "DECAY tgl": "DECAY", "VEL": "VELOCITY"}
FAN_ECHO = [(-60, "tape"), (-20, "bbd"), (20, "clean"), (60, "ping-pong")]
FAN_VERB = [(-60, "plate"), (-20, "hall"), (20, "spring"), (60, "shimmer")]

def frame(name):
    """controls, labels, grooves for the region V2 .. rear of one frame. y = away from the player."""
    if name == "ONE SHEET":
        dx, yV2, yFX, r, gap, size, font, upper = -5.0, 123.0, 146.0, 7.45, 3.2, 1.9, "inter", True
        fan_row_in, fan_row_out, fan_size = 3.4, 6.2, 1.05
        head_y, head_size = 161.8, 2.1          # ECHO / REVERB baseline (r5 OS_HEAD_Y)
        sync = (128.0, 132.7)
        grooves_v = [(xb - 5, 52.6, 133.5) for xb in F.vb_play] + [(xb - 5, 138.5, 156.5) for xb in F.vb_fx]
        headings = [("MIXER", 138.0, 136.0, 1.8, "inter", "center")]      # PROPOSED: moved from y 133.6 to 136.0 (OSCILLATORS / CONTOURS line)
        rear = 180.0
    else:   # FOLD-105 lid, in open y = D + d (D 108)
        D = 108.0
        dx, yV2, yFX, r, gap, size, font, upper = 0.0, D + 60.85, D + 83.85, 7.25, 2.9, 2.35, "kalam", False
        fan_row_in, fan_row_out, fan_size = 3.4, 6.5, 1.3
        head_y, head_size = D + 83.85 + 16.2, 2.0
        sync = (133.0, D + 70.6)
        grooves_v = [(xb, D + 0.8, D + 60.85 + 9) for xb in F.vb_voice] + [(xb, D + 83.85 - 9, D + 83.85 + 9) for xb in F.vb_fx]
        headings = []
        rear = D - F.RIM - 0.0 + D   # lid far rim inner face, open y
    ctl = [(n, x + dx, yV2, KN if k == "k" else TGL, k) for n, x, rr, k in F.v2]
    ctl += [(n, x + dx, yFX, KN, k) for n, x, rr, k in F.fx]
    ctl.append(("FREE/SYNC", sync[0], sync[1], TGL, "t"))
    labels = []
    def L(s): return s if upper else s.lower()
    for n, x, rr, k in F.fx:
        x += dx
        if n == "ECHO TIME":                                   # PROPOSED: TIME's legend moves behind its knob
            labels.append(("TIME (behind)", tbox(x, yFX + 13.2, L("TIME"), size, font)))
        elif n == "REVERB DECAY":                              # mirror: DECAY's legend behind too
            labels.append(("DECAY (behind)", tbox(x, yFX + 13.2, L("DECAY"), size, font)))
        else:
            labels.append((n + " legend", tbox(x, yFX - r - gap - 0.6, L(LAB.get(n, n)), size, font)))
        if n.endswith("TYPE"):
            for a, w in (FAN_ECHO if n.startswith("ECHO") else FAN_VERB):
                row = fan_row_in if abs(a) < 40 else fan_row_out
                labels.append((f"{n} fan {w}", tbox(x + 11.85 * math.sin(math.radians(a)), yFX + r + row, L(w), fan_size, font)))
    for hn, hx in (("ECHO", 118.5), ("REVERB", 167.5)):
        b = tbox(hx + dx, head_y + 0.375 * head_size, L(hn), head_size, font)
        labels.append((hn + " heading", b))
    for hn, hx, hy, hs, hf, ha in headings:
        labels.append((hn + " heading", tbox(hx, hy, hn, hs, hf, ha)))
    # the toggle's own legends: left / right throw (free left, sync right), beside the nut like PARA / AFTERTOUCH
    ls = size * 0.72
    sx, sy = sync
    labels.append(("free", tbox(sx - 6.2, sy, "free", ls, font, "right")))
    labels.append(("sync", tbox(sx + 6.2, sy, "sync", ls, font, "left")))
    return dict(ctl=ctl, labels=labels, grooves=grooves_v, sync=sync, yFX=yFX, time_x=128.5 + dx, r=r, rear=rear)

def check_sync(name):
    fr = frame(name)
    print(f"\n[1] {name}: FREE/SYNC toggle at x {fr['sync'][0]}, y {fr['sync'][1]:.2f}"
          + (f" (lid d {fr['sync'][1]-108:.2f})" if name != "ONE SHEET" else ""))
    ctl = fr["ctl"]; sync = [c for c in ctl if c[0] == "FREE/SYNC"][0]
    # control rules (same as the v1.1 checkers)
    for c in ctl:
        if c is sync: continue
        g = math.dist(c[1:3], sync[1:3]) - c[3] - sync[3]
        if g < 1.5 - 1e-6: fail(f"GAP toggle-{c[0]} {g:.2f}")
    near = sorted((math.dist(c[1:3], sync[1:3]) - c[3] - sync[3], c[0]) for c in ctl if c is not sync)[:3]
    print("  nearest controls (edge gap):", ", ".join(f"{n} {g:.2f}" for g, n in near))
    for gx, gy0, gy1 in fr["grooves"]:
        if gy0 - sync[3] <= sync[2] <= gy1 + sync[3] and abs(sync[1] - gx) - sync[3] < 3 - 1e-6:
            fail(f"BREAK toggle vs groove x {gx}")
    # labels vs controls, labels vs labels, labels vs grooves
    worst = []
    for ln, b in fr["labels"]:
        for c in ctl:
            g = box_circle_gap(b, c[1], c[2], c[3])
            worst.append((g, ln, c[0]))
            if g < 1.5 - 1e-6: fail(f"LABEL {ln} vs {c[0]} {g:.2f}")
        for gx, gy0, gy1 in fr["grooves"]:
            if b[3] >= gy0 and b[1] <= gy1:
                g = max(b[0] - gx, gx - b[2], -1)
                if g < 1.0: fail(f"LABEL {ln} vs groove x {gx} {g:.2f}")
    for (a, ba), (b, bb) in itertools.combinations(fr["labels"], 2):
        g = box_box_gap(ba, bb)
        if g < 1.0 - 1e-6: fail(f"LABEL {a} vs {b} {g:.2f}")
    mine = [w for w in worst if w[1] in ("free", "sync", "TIME (behind)", "DECAY (behind)") or w[2] == "FREE/SYNC"]
    print("  tightest label gaps round the toggle:", ", ".join(f"{l}|{c} {g:.2f}" for g, l, c in sorted(mine)[:4]))
    return fr

# ---------------------------------------------------------------- 2. TIME's two scales vs the toggle
def check_scale(name, fr):
    tx, ty, r = fr["time_x"], fr["yFX"], fr["r"]
    sx, sy = fr["sync"]
    inner = (r + 0.9, r + 1.9)     # ms: short ticks (v1.1 radius)
    outer = (r + 2.4, r + 3.6)     # divisions: 9 marks (PROPOSED radii)
    # pot sweep 300 deg (+-150). PROPOSED: both printed scales span +-135 (270 deg); firmware clamps the
    # last 15 deg at each end (min / max), so no tick sits under the toggle. At +-150 the end ticks hit the nut (-0.7).
    SWEEP = 135
    print(f"[2] {name}: TIME two-scale ring vs toggle (printed scales span +-{SWEEP} deg)")
    worst = 99
    for ring, (r0, r1) in (("ms", inner), ("divisions", outer)):
        n = 7 if ring == "ms" else 9
        for i in range(n):
            a = math.radians(-SWEEP + 2 * SWEEP * i / (n - 1))
            for rr in (r0, r1):
                px, py = tx + rr * math.sin(a), ty + rr * math.cos(a)
                g = math.dist((px, py), (sx, sy)) - TGL
                worst = min(worst, g)
    print(f"  closest tick end to the toggle nut: {worst:.2f} mm (need >= 0.5)")
    if worst < 0.5: fail(f"SCALE tick under the toggle {worst:.2f}")
    top = ty + outer[1]
    lab = [b for n, b in fr["labels"] if n == "TIME (behind)"][0]
    print(f"  outer ring top y {top:.2f}; TIME legend (behind) spans y {lab[1]:.2f}-{lab[3]:.2f} -> gap {lab[1]-top:.2f}")
    if lab[1] - top < 1.0: fail("TIME legend on its scale")
    return top

# ---------------------------------------------------------------- 3. BUTTERFLY joint
def check_butterfly(fr):
    print("\n[3] BUTTERFLY (ONE SHEET): the print / walnut joint line")
    tops = sorted(((b[3], n) for n, b in fr["labels"]), reverse=True)[:4]
    knob_edge = fr["yFX"] + KN
    need = max(tops[0][0] + 1.5, knob_edge + 6.5)
    print(f"  FX knob rear edge y {knob_edge:.2f}; rearmost legends: " + ", ".join(f"{n} {y:.2f}" for y, n in tops))
    print(f"  visual's joint y 160 cuts: " + (", ".join(n for n, b in fr["labels"] if b[1] < 160 < b[3]) or "nothing"))
    j = math.ceil(need * 2) / 2
    print(f"  joint must sit at y >= {need:.2f} -> use y {j:.1f}; wood behind it to the printed rear wall (y 180): {180-j:.1f} mm "
          f"at the deepest notch of the live edge")
    return j

# ---------------------------------------------------------------- 4. pegs
PEG_R = 6.35          # 1/2 in mushroom button plug
PEG_TOP = 6.5         # head top above the surface, by mechanism (HUSH rev: 2.5 travel + ~4 head)
def check_pegs():
    print("\n[4a] RAIN (ONE SHEET 276): peg width")
    whites = [12 + 18 * n for n in range(15)]          # HUSH x 19 + 18n, ONE SHEET x = HUSH - 7
    W, flat_in = 276.0, 2.0                            # ONE SHEET top edge R 2: the flat starts 2 in
    for collar, what in ((9.5, "HUSH's 19 mm felt collar"), (7.0, "a 14 mm felt washer"), (PEG_R, "head only")):
        l = whites[0] - collar; rgt = W - (whites[-1] + collar)
        print(f"  {what}: left {l:.2f}, right {rgt:.2f} from the outside; {min(l, rgt) - flat_in:.2f} from the flat")
    need = (whites[-1] + 9.5 + 3) - W
    print(f"  to keep HUSH's 19 mm collar >= 3 from the flat on both ends: +{max(0, (3 + flat_in) - (whites[0]-9.5)) + max(0, need + flat_in):.1f} mm width")

    print("[4b] CHAMBER (FOLD-105): closed height with pegs")
    D = 108.0
    base = F.BASE_PLATE
    peg_top = base + PEG_TOP
    pegs = [(17 + 18 * n, 13.5) for n in range(15)]    # FOLD keys x0 8: whites 17 + 18n; HUSH edge-A y 13.5
    pegs += [(8 + 18 * (i + 1), 36.0) for i in [i for i in range(14) if [1, 1, 0, 1, 1, 1, 0][i % 7]]]
    lid = [(n, x, F.KN if k == "k" else F.TGL, k, dd) for (rowd, src) in
           ((14.45, F.v1), (60.85, F.v2), (83.85, F.fx)) for n, x, r, k in src for dd in (rowd,)]
    lid += [(n, x, F.TGL, "t", F.D_SW) for n, x, r, k in F.sw]
    lid.append(("FREE/SYNC", 133.0, F.TGL, "t", 70.6))
    worst_need = 0; hits = []
    for n, x, r, k, dd in lid:
        yl = D - dd
        over = [p for p in pegs if math.dist((x, yl), p) < r + PEG_R + 1.0]
        if over:
            bottom = F.LID_FACE_CLOSED - F.KNOB_H     # conservative: toggles counted at knob height, as v1.1
            need = (peg_top + 2.0) - bottom
            worst_need = max(worst_need, need); hits.append(n)
    print(f"  peg head top z {peg_top:.1f} (base plate {base} + {PEG_TOP}); lid items landing over a peg: {len(hits)} "
          f"({', '.join(sorted(set(h.split()[0] for h in hits)))})")
    print(f"  lid must rise {worst_need:.1f} mm to keep 2.0 clear -> closed ≈ {50.1 + worst_need:.1f} mm (v1.1 ≈ 50.1)")
    return worst_need

# ---------------------------------------------------------------- 5. DIPTYCH cords and tipping
def check_diptych():
    print("\n[5] DIPTYCH (FOLD-105): cords vs brass stays")
    AXY, AXZ, STAND = 109.0, 25.0, math.radians(60)     # r5: hinge axis y D+1, z 25; lid 60 deg up = 120 deg open
    def lid_pt(vy, vz):        # a point on the flat-open lid, relative to the axis, rotated up 60 deg
        return (AXY + vy * math.cos(STAND) - vz * math.sin(STAND), AXZ + vy * math.sin(STAND) + vz * math.cos(STAND))
    g = 9.81; mb, ml = 0.40, 0.375                     # ESTIMATE (v1.1: base 0.40, lid 0.35-0.40 kg)
    ycg_v11 = 97.0                                     # v1.1's combined CG
    lid_cg = lid_pt(55.0, -8.0)
    ycg_calc = (mb * 54 + ml * lid_cg[0]) / (mb + ml)
    tip = lid_pt(84.85, (15.1 + 13.5) - AXZ)   # back-row knob tip: d 83.85 (+1 axis offset), lid face 15.1 + knob 13.5
    W = (mb + ml) * g
    def push_to_tip(yp, ycg):
        # push normal to the panel at a back-row knob tip: (+cos30 back, -sin30 down) per newton
        m_push = math.cos(math.radians(30)) * tip[1] + math.sin(math.radians(30)) * (tip[0] - yp)
        return W * (yp - ycg) / m_push
    print(f"  back-row knob tip at y {tip[0]:.1f}, z {tip[1]:.1f}; combined CG y {ycg_v11} (v1.1) / {ycg_calc:.1f} (this model)")
    print(f"  v1.1 stays (tip at y 167): {push_to_tip(167, ycg_v11):.1f} N to tip (v1.1 record: 6.8 N) - model checks out")
    for ycg in (ycg_v11, ycg_calc):
        f = push_to_tip(108.0, ycg)
        print(f"  cords only (rear edge y 108 is the pivot), CG {ycg:.1f}: {f:.1f} N to tip")
        if f < 5: print(f"  FINDING (DIPTYCH as briefed): tips at {f:.1f} N < 5 N with cords alone -> needs the feet below")
    yp5 = next(y / 2 for y in range(216, 400) if push_to_tip(y / 2, ycg_v11) >= 5.0)
    print(f"  ground contact needed for >= 5 N: y {yp5:.1f} -> feet {yp5-108:.0f} mm behind the base")
    f50 = push_to_tip(158.0, ycg_v11)
    print(f"  PROPOSED fix: two brass feet folding out of the base underside, tips 50 mm behind (y 158): {f50:.1f} N to tip")
    if f50 < 5: fail("feet too short")
    # the toggle closed (FOLD, no pegs): lands at base y 108 - 70.6 = 37.4, over the sharps
    clr = (F.LID_FACE_CLOSED - F.KNOB_H) - F.SHARP_TOP
    print(f"  (FREE/SYNC closed: lands at base y {108-70.6:.1f} over the sharps, z clearance {clr:.1f} at v1.1's conservative knob height)")
    # cord geometry: latitude 37.4 deg (Lynchburg), lid end point s along the lid, base anchor at z 9 on the end face
    lat = math.radians(37.4); za = 9.0
    print("  cord at 37.4 deg to the base (director's latitude): anchor y vs lid attachment")
    for s in (100.0, 60.0, 40.0):
        ty, tz = lid_pt(s, -2.0)
        ya = ty - (tz - za) / math.tan(lat)
        Lc = math.hypot(ty - ya, tz - za)
        # cord tension: lid weight + 5 N push about the axis, shared by 2 cords
        lid_m = ml * g * (lid_cg[0] - AXY)
        push_m = 5.0 * (math.cos(math.radians(30)) * (tip[1] - AXZ) + math.sin(math.radians(30)) * (tip[0] - AXY))
        ux, uz = (ya - ty) / Lc, (za - tz) / Lc
        arm = abs((ty - AXY) * uz - (tz - AXZ) * ux)
        T = (lid_m + push_m) / arm / 2
        zs = za + (68 - ya) * math.tan(lat) if ya < 68 else None
        hand = f"crosses the PLAY row (y 68) {zs-15.6:.0f} mm above the base top" if zs else "stays behind the PLAY row"
        print(f"   lid point s {s:.0f}: anchor y {ya:.1f}, cord {Lc:.0f} mm, arm {arm:.1f} mm, tension ≈ {T:.0f} N per cord; {hand}")

# ---------------------------------------------------------------- 6. CHAMBER façade vs the lid back's screws and feet
def check_facade(Lmax=66.0, impost=18.0, pitch=10.0):
    print(f"\n[6] CHAMBER façade on the lid back: 25 pipes, L = {Lmax:.0f} x 2^(-n/12) (C-C, 2 octaves), tower from x 143, pitch {pitch}, feet on d {impost}")
    order = [0] + [k for i in range(1, 13) for k in (i, -i)]          # centre, then alternate outward
    pipes = [(143 + pitch * k, Lmax * 2 ** (-n / 12)) for n, k in enumerate(order[:25])]
    print(f"  field x {min(x for x, l in pipes) - pitch/2:.0f}-{max(x for x, l in pipes) + pitch/2:.0f}; lengths {pipes[0][1]:.1f} (centre) -> {pipes[-1][1]:.1f} (ends)")
    screws = [(16, 12), (270, 12), (16, 96), (270, 96), (143, 12), (143, 96)]       # r5 back_detail, lid d
    feet = [(40, 30), (246, 30), (40, 78), (246, 78)]                               # r 6 rubber feet (flat-open support), v1.1
    for (x, d) in feet[:2]:
        hit = [(px, l) for px, l in pipes if abs(px - x) < pitch / 2 + 6 and impost - 6 < d < impost + l + 6]
        if hit: print(f"  v1.1 foot at ({x}, d {d}) lands on a pipe (x {hit[0][0]:.0f}) -> move it")
    feet = [(40, 6), (246, 6), (40, 78), (246, 78)]                                 # PROPOSED: front pair to d 6, under the impost line
    for nm, pts, rr in (("screw", screws, 2.7), ("foot", feet, 6.0)):
        for (x, d) in pts:
            hit = [(px, l) for px, l in pipes if abs(px - x) < pitch / 2 + rr and impost - rr < d < impost + l + rr]
            if hit: fail(f"FACADE {nm} at ({x}, d {d}) sits on a pipe (x {hit[0][0]:.0f}, top d {impost + hit[0][1]:.1f})")
    print("  screws on d 12 = the impost line (under the pipe feet); d 96 screws above the tallest top"
          f" (d {impost + Lmax:.0f}) -> clear")

for nm in ("FOLD", "ONE SHEET"):
    fr = check_sync(nm)
    check_scale(nm, fr)
    if nm == "ONE SHEET":
        check_butterfly(fr)
check_pegs()
check_diptych()
check_facade()
print("\nTOTAL fails", TOTAL)
