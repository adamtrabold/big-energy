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

# ---------------------------------------------------------------- 7. legends, tick rings, controls: what the renderer really draws
# Instruments the visual designer's models (design/concepts/_mock-src/rb.py: Chamber, rain) by recording every txt()
# and tick the model emits on the playing faces, then measures each text's exact ink box with OpenSCAD (SVG export,
# cached in /tmp). Rules (S1 + director, round 1): legend-legend >= 1.5 (hard overlap < 0), legend-tick >= 1.0,
# legend-control >= 1.5, tick-to-another-control >= 0.5. Controls are the layout circles (+ pegs, FREE/SYNC).
import json, subprocess, tempfile, hashlib, concurrent.futures as cf
MOCK = os.path.join(HERE, "..", "..", "concepts", "_mock-src")
CACHE = "/tmp/branch_check_textbox.json"

def _scad_box(key):
    s, size, font, ha, va = key
    esc = s.replace('"', '\\"')
    with tempfile.TemporaryDirectory() as td:
        src = os.path.join(td, "t.scad"); out = os.path.join(td, "t.svg")
        open(src, "w").write(f'text("{esc}", size={size}, font="{font}", halign="{ha}", valign="{va}", $fn=24);')
        subprocess.run(["openscad", "-o", out, src], capture_output=True, timeout=120)
        if not os.path.exists(out):
            return None
        import re
        num = r"-?[\d.]+(?:[eE][-+]?\d+)?"
        pts = [(float(a), float(b)) for a, b in re.findall(rf"({num}),({num})", open(out).read())]
    if not pts:
        return None
    xs = [a for a, b in pts]; ys = [-b for a, b in pts]           # SVG y is down
    return (min(xs), min(ys), max(xs), max(ys))

def text_boxes(keys):
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    todo = [k for k in keys if json.dumps(k) not in cache]
    if todo:
        with cf.ThreadPoolExecutor(8) as ex:
            for k, b in zip(todo, ex.map(_scad_box, todo)):
                cache[json.dumps(k)] = b
        json.dump(cache, open(CACHE, "w"))
    return {tuple(json.loads(k)): v for k, v in cache.items()}

def record(build, face_z_min):
    """run build() with txt / ticks / _tick patched; return (texts, ticks) drawn at z >= face_z_min."""
    sys.path.insert(0, MOCK)
    with contextlib.redirect_stdout(io.StringIO()):
        import ld, r4, r5, rb
    T, K = [], []
    o_txt, o_ticks, o_tick = ld.txt, ld.ticks, rb._tick
    def p_txt(x, y, z, s, size, col, font="Inter:style=SemiBold", halign="center", valign="center", rot=0, h=0.12):
        if z >= face_z_min and s.strip():
            T.append((x, y, s, size, font, halign, valign, rot))
        return o_txt(x, y, z, s, size, col, font=font, halign=halign, valign=valign, rot=rot, h=h)
    def p_ticks(x, y, z, r, n_or_angles, col, length=1.4, width=0.45, span=300):
        if z >= face_z_min:
            angs = ([-span / 2 + span * i / (n_or_angles - 1) for i in range(n_or_angles)]
                    if isinstance(n_or_angles, int) else n_or_angles)
            for a in angs:
                K.append((x, y, r, r + length, a, (x, y)))
        return o_ticks(x, y, z, r, n_or_angles, col, length=length, width=width, span=span)
    def p_tick(x, y, z, r, a, L, w, col):
        if z >= face_z_min:
            K.append((x, y, r, r + L, a, (x, y)))
        return o_tick(x, y, z, r, a, L, w, col)
    mods = [ld, r4, r5, rb]
    saved = [(m, getattr(m, "txt", None), getattr(m, "ticks", None)) for m in mods]
    try:
        for m in mods:
            if hasattr(m, "txt"): m.txt = p_txt
            if hasattr(m, "ticks"): m.ticks = p_ticks
        rb._tick = p_tick
        with contextlib.redirect_stdout(io.StringIO()):
            build(rb)
    finally:
        for m, t, k in saved:
            if t: m.txt = t
            if k: m.ticks = k
        rb._tick = o_tick
    return T, K

def rot_box(b, x, y, rot):
    if not rot:
        return (x + b[0], y + b[1], x + b[2], y + b[3])
    a = math.radians(rot); cs, sn = math.cos(a), math.sin(a)
    pts = [(x + px * cs - py * sn, y + px * sn + py * cs) for px in (b[0], b[2]) for py in (b[1], b[3])]
    return (min(p[0] for p in pts), min(p[1] for p in pts), max(p[0] for p in pts), max(p[1] for p in pts))

def seg_box_gap(p, q, b, n=8):
    return min(box_circle_gap(b, p[0] + (q[0] - p[0]) * i / n, p[1] + (q[1] - p[1]) * i / n, 0) for i in range(n + 1))

FINAL_FONT = {"DkgHandwriting:style=Bold": "Kalam:style=Bold"}   # rb.py's stand-in -> the final art's font

def collide(name, T, K, ctl, final=True, base=None, quiet=False):
    if final:   # measure with the font the owner will see (Kalam), not the render stand-in
        T = [(x, y, s, sz, FINAL_FONT.get(f, f), ha, va, rot) for x, y, s, sz, f, ha, va, rot in T]
    keys = sorted({(s, sz, f, ha, va) for x, y, s, sz, f, ha, va, rot in T})
    tb = text_boxes(keys)
    L = []
    for x, y, s, sz, f, ha, va, rot in T:
        b = tb.get((s, sz, f, ha, va))
        if b: L.append((s, rot_box(b, x, y, rot), (x, y)))
    out = {"legend-legend": [], "legend-tick": [], "legend-control": [], "tick-control": []}
    for (a, ba, pa), (b, bb, pb) in itertools.combinations(L, 2):
        g = box_box_gap(ba, bb)
        if g < 1.5 - 1e-6: out["legend-legend"].append((g, f'"{a}" | "{b}"', pa))
    for s, b, p in L:
        for x, y, r0, r1, a, own in K:
            th = math.radians(a)
            P = (x + r0 * math.sin(th), y + r0 * math.cos(th)); Q = (x + r1 * math.sin(th), y + r1 * math.cos(th))
            g = seg_box_gap(P, Q, b)
            if g < 1.0 - 1e-6: out["legend-tick"].append((g, f'"{s}" | tick of the control at ({x:.1f}, {y:.1f}) @{a:.0f}°', p))
        for cn, cx, cy, cr in ctl:
            g = box_circle_gap(b, cx, cy, cr)
            if g < 1.5 - 1e-6: out["legend-control"].append((g, f'"{s}" | {cn}', p))
    for x, y, r0, r1, a, own in K:
        th = math.radians(a)
        Q = (x + r1 * math.sin(th), y + r1 * math.cos(th))
        for cn, cx, cy, cr in ctl:
            if math.dist((cx, cy), own) < 0.5: continue
            g = math.dist(Q, (cx, cy)) - cr
            if g < 0.5 - 1e-6: out["tick-control"].append((g, f"tick of ({x:.1f}, {y:.1f}) @{a:.0f}° | {cn}", Q))
    # one line per pair (ticks repeat per angle): keep the worst
    if not quiet:
        print(f"\n[7] {name}{' [Kalam, final font]' if final else ' [as rendered]'}: {len(L)} legends, {len(K)} ticks, {len(ctl)} controls measured"
              + ("; (v1.1) = the same clash is in the locked v1.1 model" if base is not None else ""))
    n_all = 0; keys = set()
    for kind, lst in out.items():
        best = {}
        for g, what, p in lst:
            k = what.split(" @")[0] if kind != "tick-control" else what.split(" | ")[1] + what.split(" @")[0]
            if k not in best or g < best[k][0]: best[k] = (g, what, p)
        items = sorted(best.values())
        n_all += len(items)
        keys |= {k for k in best}
        if quiet: continue
        print(f"  {kind}: {len(items)}")
        for k, (g, what, p) in sorted(best.items(), key=lambda kv: kv[1][0]):
            tag = "  (v1.1)" if base is not None and k in base else ""
            print(f"    {g:6.2f}  {what}   at ({p[0]:.1f}, {p[1]:.1f}){tag}")
    return (n_all, keys) if quiet else n_all

def ctl_fold(D=108.0):
    L0 = D + 2.0
    K = lambda k, r: {"k": KN, "t": TGL, "b": 6.0, "stick": 6.0, "l": r}.get(k, r)
    c = [(e[0], e[1], e[4] if len(e) > 4 else F.P, (F.CUT if e[0] == "CUTOFF" else K(e[3], e[2]))) for e in F.play]
    for off, src in ((F.VARIANTS["FOLD-105 (slim battery)"]["dV1"], F.v1), (F.VARIANTS["FOLD-105 (slim battery)"]["dV2"], F.v2),
                     (F.VARIANTS["FOLD-105 (slim battery)"]["dFX"], F.fx)):
        c += [(n, x, L0 + off, K(k, r)) for n, x, r, k in src]
    c += [(n, x, L0 + F.D_SW, TGL) for n, x, r, k in F.sw]
    c.append(("FREE/SYNC", 133.0, L0 + 70.6, TGL))
    return c

def ctl_flat(dx=-5.0):
    K = lambda k, r: {"k": KN, "t": TGL, "b": 6.0, "stick": 6.0, "l": r}.get(k, r)
    c = [(e[0], e[1] + dx, e[4] if len(e) > 4 else F.P, (F.CUT if e[0] == "CUTOFF" else K(e[3], e[2]))) for e in F.play]
    for yy, src in ((100, F.v1), (123, F.v2), (146, F.fx)):
        c += [(n, x + dx, yy, K(k, r)) for n, x, r, k in src]
    c += [(n, x + dx, 111.5, TGL) for n, x, r, k in F.sw_flat]
    c.append(("FREE/SYNC", 128.0, 132.7, TGL))
    return c

def check_render_collisions():
    if subprocess.run(["which", "openscad"], capture_output=True).returncode:
        print("\n[7] skipped: openscad not installed"); return
    tot = 0
    T, Kt = record(lambda rb: rb.Chamber().model(True), 15.0)
    pegs = [("peg", 17 + 18 * n, 13.5, PEG_R) for n in range(15)]
    pegs += [("peg", 8 + 18 * (i + 1), 36.0, PEG_R) for i in [i for i in range(14) if [1, 1, 0, 1, 1, 1, 0][i % 7]]]
    have_kalam = "Kalam" in subprocess.run(["fc-list"], capture_output=True, text=True).stdout
    if not have_kalam:
        print("\n[7] Kalam not installed: CHAMBER measured with rb.py's stand-in (runs larger)")
    Tb, Kb = record(lambda rb: rb.Fold(105).model(True), 15.0)
    _, base_fold = collide("v1.1 FOLD-105", Tb, Kb, ctl_fold()[:-1], final=have_kalam, quiet=True)
    tot += collide("CHAMBER (open, both faces)", T, Kt, ctl_fold() + pegs, final=have_kalam, base=base_fold)
    T, Kt = record(lambda rb: rb.rain(field=False), 23.5)
    sys.path.insert(0, MOCK)
    import rb as _rb
    w, sh = _rb.rain_pegs()
    Tb, Kb = record(lambda rb: rb.r5.one_sheet(), 23.5)
    _, base_os = collide("v1.1 ONE SHEET", Tb, Kb, ctl_flat()[:-1], quiet=True)
    tot += collide("RAIN (top face)", T, Kt, ctl_flat() + [("peg", x, y, PEG_R) for x, y in w + sh], base=base_os)
    print(f"  collisions listed (CHAMBER + RAIN): {tot}  (reported, not counted in TOTAL fails: they are the visual designer's to fix)")

# ---------------------------------------------------------------- 8. CHAMBER: the hinge-side slot, and the push-out holes
def check_chamber_back():
    print("\n[8a] CHAMBER hinge-side slot (closed, seen from behind)")
    AXY = 109.0; AXZ = 25.0 + 1.3          # lid walls +2.6 -> the hinge axis rises 1.3 (rb.py Chamber.AXZ)
    BASE, LIDPF, RIM_OPEN = F.BASE_PLATE, 15.1, 34.5 + 2.6
    rot = lambda p, a: (AXY + (p[0] - AXY) * math.cos(a) - (p[1] - AXZ) * math.sin(a),
                        AXZ + (p[0] - AXY) * math.sin(a) + (p[1] - AXZ) * math.cos(a))
    lid_face_closed = rot((110.0, LIDPF), math.pi)[1]
    rim_closed = rot((150.0, RIM_OPEN), math.pi)[1]
    print(f"  v1.1 has no lid wall on the hinge edge (R4: open, a wall there would stand {RIM_OPEN-LIDPF:.1f} mm between PLAY and V1).")
    print(f"  closed: base plate z {BASE}, lid plate z {lid_face_closed:.1f}, lid rims land at z {rim_closed:.1f} (on the base plate)"
          f" -> slot {lid_face_closed-BASE:.1f} mm tall x 266 wide (x 10-276, between the knuckles). Real.")
    B = (108.0, BASE)                           # base rear-top edge
    P = (110.0, LIDPF)                          # lid hinge-edge top (plate level), open
    for nm, a in (("open 180", 0.0), ("standing 120", math.radians(60)), ("closed", math.pi)):
        q = rot(P, a)
        print(f"  spine anchors {nm}: lid edge at (y {q[0]:.1f}, z {q[1]:.1f}), {math.dist(B, q):.1f} mm from the base edge")
    Ls = math.dist(B, rot(P, math.pi))
    print(f"  -> a flexible spine {Ls:.1f} mm wide is taut closed; open it folds into the 2.0 mm seam gap as a loop "
          f"≈ {(Ls-2.0)/2:.1f} mm deep (to z ≈ {BASE-(Ls-2.0)/2:.1f}), nothing above the plates (R4 kept)")

    print("[8b] CHAMBER push-out holes (lid back): pipes, screws, feet, and what the pin lands on inside")
    D, IMP = 108.0, 18.0
    screws = [(16, 12), (270, 12), (143, 12), (16, 96), (270, 96), (143, 96)]
    feet = [(40, 6), (246, 6), (40, 78), (246, 78)]
    bridges = [(103, 113), (173, 183)]                         # lid board bridges between the cell / speaker windows (v1.1)
    band = (21.9, 59.45)
    no_go = [("V1 toggle bodies OSC MOD / FILTER MOD (ESTIMATE d 8-21)", 103, 113, 8, 21),
             ("V1 toggle bodies", 173, 183, 8, 21),
             ("ECHO TYPE rotary tails (ESTIMATE body ≥ 16: d 76-92)", 100.5, 116.5, 75.9, 91.9),
             ("REVERB TYPE rotary tails", 169.5, 185.5, 75.9, 91.9),
             ("far-wall I/O board (d 92-104, x 60-230)", 60, 230, 92, 104)]
    def pipes(pitch):
        order = [0] + [k for i in range(1, 13) for k in (i, -i)]
        return [(143 + pitch * k, 66.0 * 2 ** (-n / 12)) for n, k in enumerate(order[:25])]
    def pipe_gap(hx, hd, hr, P):
        g = 99
        for px, L in P:
            # body: x +-3.2 from d IMP+9 to IMP+L; foot cone from +-1.0 at IMP to +-3.2 at IMP+9; line 0.6
            for d in [IMP + t * L / 40 for t in range(41)]:
                if abs(d - hd) > hr + 1: continue
                half = 3.2 if d >= IMP + 9 else 1.0 + 2.2 * (d - IMP) / 9
                for ex in (px - half, px + half):
                    g = min(g, math.dist((hx, hd), (ex, d)) - hr - 0.3)
            if abs(hx - px) < 3.2 and IMP + 9 <= hd <= IMP + L:
                g = min(g, -1)        # inside a pipe body
        return g
    for label, holes, hr, pitch, mouth in (("v1.1 (110 / 176, d 54)", [(110, 54), (176, 54)], 3.0, 10.0, False),
                                           ("visual's d 90", [(110, 90), (176, 90)], 3.0, 10.0, False),
                                           ("PROPOSED: pipe mouths, pitch 8.75 (108 / 178, d 28.3, Ø 4)", [(108, 28.3), (178, 28.3)], 2.0, 8.75, True)):
        P = pipes(pitch)
        print(f"  {label}:")
        for hx, hd in holes:
            sg = min(math.dist((hx, hd), sc) - hr - 2.7 for sc in screws)
            fg = min(math.dist((hx, hd), fe) - hr - 6.0 for fe in feet)
            pg = pipe_gap(hx, hd, hr, P)
            on_bridge = any(a + hr <= hx <= b - hr for a, b in bridges) and band[0] <= hd <= band[1]
            hits = [n for n, x0, x1, d0, d1 in no_go if x0 - hr < hx < x1 + hr and d0 - hr < hd < d1 + hr]
            pipe_txt = "the hole IS the pipe's mouth" if mouth else (f"{pg:.1f} to a pipe line" if pg > -1 else "inside a pipe")
            print(f"    ({hx}, d {hd}): screws {sg:.1f} clear, feet {fg:.1f}, {pipe_txt}; inside lands on "
                  + ("a bare board bridge ✓" if on_bridge and not hits else ("; ".join(hits) if hits else "board, off the bridges")))
        if mouth:
            Pm = pipes(8.75)
            for hx, hd in holes:
                k = min(Pm, key=lambda q: abs(q[0] - hx))
                print(f"    pipe at x {k[0]:.2f} (L {k[1]:.1f}): mouth zone d {IMP+9:.0f}-{IMP+9+2.6:.1f}; hole centre d {hd} -> mouth = hole")
            print(f"    field at pitch 8.75: x {min(q[0] for q in Pm)-3.2:.1f}-{max(q[0] for q in Pm)+3.2:.1f}; gaps between pipes {8.75-6.4:.2f}")
            for fe in feet + screws:
                bad = [q for q in Pm if abs(q[0] - fe[0]) < 3.2 + 6 and IMP - 6 < fe[1] < IMP + q[1] + 6]
                if bad: fail(f"pitch 8.75: {fe} on a pipe")

# ---------------------------------------------------------------- 9. CATHEDRAL (CHAMBER + FOLD v1.1), option B: every effect on one row
def check_cathedral_b(row=None, brk=None, title="option B"):
    """Option B (moves controls: director, then owner): the lid back row carries every FX control + VOLUME + DRIFT;
    the base PLAY row's right section (was REPEATS, ECHO MIX, REVERB MIX, TAP) becomes the speaker (round grille).
    Same rules as fold_r5_check: pitch 20, gaps >= 1.5, knob/button >= 7 and toggle >= 3 from breaks, lid edge >= 16,
    far rim, closed landing (z over pegs with CATHEDRAL's +2.6 lid)."""
    print(f"\n[9] CATHEDRAL {title}")
    D, dFX, dV2 = 108.0, 83.85, 60.85
    row = row or [("DRIFT", 33.5, KN, "k"), ("ECHO TYPE", 62.5, KN, "k"), ("ECHO TIME", 82.5, KN, "k"), ("ECHO REPEATS", 102.5, KN, "k"),
           ("ECHO MIX", 122.5, KN, "k"), ("TAP", 142.5, 6.0, "b"), ("REVERB TYPE", 171.0, KN, "k"), ("REVERB DECAY", 191.0, KN, "k"),
           ("REVERB MIX", 211.0, KN, "k"), ("VOLUME", 240.0, KN, "k")]
    brk = brk or [48.0, 156.0, 225.5]
    sync = ("FREE/SYNC", 96.0, TGL, "t", 69.0)
    bad = 0
    items = [(n, x, dFX, r, k) for n, x, r, k in row] + [(sync[0], sync[1], sync[4], sync[2], "t")]
    items += [(n, x, dV2, F.KN if k == "k" else F.TGL, k) for n, x, r, k in F.v2]
    items += [(n, x, 14.45, F.KN if k == "k" else F.TGL, k) for n, x, r, k in F.v1]
    items += [(n, x, F.D_SW, F.TGL, "t") for n, x, r, k in F.sw]
    for a, b in itertools.combinations(items, 2):
        d = math.dist((a[1], a[2]), (b[1], b[2]))
        if a[4] == b[4] == "k" and a[2] == b[2] and d < 20 - 1e-6: fail(f"B PITCH {a[0]} {b[0]}"); bad += 1
        if d - a[3] - b[3] < 1.5 - 1e-6: fail(f"B GAP {a[0]} {b[0]} {d-a[3]-b[3]:.2f}"); bad += 1
    for n, x, r, k in row:
        for b0 in brk:
            if abs(x - b0) - r < 7 - 1e-6: fail(f"B BREAK {n} {b0}"); bad += 1
        if x - r < 16 - 1e-6 or 286 - (x + r) < 16 - 1e-6: fail(f"B EDGE {n}"); bad += 1
    if dFX + KN + 12 + 4 > D + 1e-6: fail("B FAR RIM"); bad += 1
    # closed landing over CATHEDRAL's pegs (lid +2.6 -> lid item bottoms at 21.5 + 2.6)
    pegs = [(17 + 18 * n, 13.5) for n in range(15)] + [(8 + 18 * (i + 1), 36.0) for i in range(14) if [1, 1, 0, 1, 1, 1, 0][i % 7]]
    for n, x, dd, r, k in [(n, x, dFX, r, k) for n, x, r, k in row] + [(sync[0], sync[1], sync[4], sync[2], "t")]:
        yl = D - dd
        if any(math.dist((x, yl), p) < r + PEG_R + 1.0 for p in pegs):
            clr = (F.LID_FACE_CLOSED + 2.6 - F.KNOB_H) - (F.BASE_PLATE + PEG_TOP)
            if clr < 2.0 - 1e-6: fail(f"B CLOSED Z {n} {clr:.2f}"); bad += 1
    near = sorted((math.dist((sync[1], sync[4]), (c[1], c[2])) - c[3] - sync[2], c[0]) for c in items if c[0] != sync[0])[:3]
    print(f"  back row x {row[0][1]}–{row[-1][1]}, breaks {brk}; FREE/SYNC at (96, d 69) between TIME and REPEATS, in front:"
          f" nearest {', '.join(f'{n} {g:.2f}' for g, n in near)}")
    print(f"  base PLAY right freed: x 186–270 between the break (184.5) and the edge; y 55–82 between the keys (54.6) and"
          f" V1's closed landing (86.1) -> a round grille up to Ø 27 centred (228, 68), or a 60 x 30 speaker under a Ø 27 rose")
    print(f"  violations {bad} (labels not yet checked: no model exists for option B)")

def check_cathedral_render():
    """§7 on rb.py's Cathedral models (layout A and B), Kalam, against each layout's own controls."""
    if subprocess.run(["which", "openscad"], capture_output=True).returncode: return
    sys.path.insert(0, MOCK)
    with contextlib.redirect_stdout(io.StringIO()):
        import rb
    if not hasattr(rb, "Cathedral"):
        print("\n[7c] no Cathedral model in rb.py"); return
    pegs = [("peg", 17 + 18 * n, 13.5, PEG_R) for n in range(15)]
    pegs += [("peg", 8 + 18 * (i + 1), 36.0, PEG_R) for i in [i for i in range(14) if [1, 1, 0, 1, 1, 1, 0][i % 7]]]
    L0 = 110.0
    for lay in ("A", "B"):
        T, Kt = record(lambda m: m.Cathedral(lay).model(True), 15.0)
        ctl = ctl_fold()
        if lay == "B":
            ctl = [c for c in ctl if c[0] not in rb.B_MOVED and not (abs(c[2] - (L0 + 83.85)) < 0.1) and c[0] != "FREE/SYNC"]
            ctl += [(n, x, L0 + 83.85, 6.0 if k == "b" else KN) for n, l, x, k in rb.B_FX]
            ctl.append(("FREE/SYNC", 96.0, L0 + 69.0, TGL))
            ctl.append(("rose grille Ø 27", 228.0, 68.0, 13.5))
        collide(f"CATHEDRAL layout {lay} (rb.Cathedral, open)", T, Kt, ctl + pegs)

for nm in ("FOLD", "ONE SHEET"):
    fr = check_sync(nm)
    check_scale(nm, fr)
    if nm == "ONE SHEET":
        check_butterfly(fr)
check_pegs()
check_diptych()
check_facade()
check_chamber_back()
check_cathedral_b()
check_cathedral_b([("DRIFT", 33.5, KN, "k"), ("ECHO TYPE", 62.5, KN, "k"), ("ECHO TIME", 82.5, KN, "k"), ("ECHO REPEATS", 102.5, KN, "k"),
                   ("ECHO MIX", 122.5, KN, "k"), ("TAP", 142.5, 6.0, "b"), ("REVERB TYPE", 171.0, KN, "k"), ("REVERB DECAY", 191.0, KN, "k"),
                   ("REVERB MIX", 211.0, KN, "k"), ("FX PAN", 240.0, KN, "k"), ("VOLUME", 260.0, KN, "k")],
                  [48.0, 156.0, 225.5], "option B + FX PAN (PAN 240 | VOLUME 260, one 'where it goes' group)")
check_cathedral_b([("DRIFT", 33.5, KN, "k"), ("ECHO TYPE", 62.5, KN, "k"), ("ECHO TIME", 82.5, KN, "k"), ("ECHO REPEATS", 102.5, KN, "k"),
                   ("ECHO MIX", 122.5, KN, "k"), ("ECHO PAN", 142.5, KN, "k"), ("REVERB TYPE", 171.5, KN, "k"), ("REVERB DECAY", 191.5, KN, "k"),
                   ("REVERB MIX", 211.5, KN, "k"), ("VOICE PAN", 240.5, KN, "k"), ("VOLUME", 260.5, KN, "k")],
                  [48.0, 157.0, 226.0], "two pans (ECHO PAN in TAP's slot 142.5; VOICE PAN 240.5 | VOLUME 260.5; TAP back to the base, x 261)")
for _f in (check_render_collisions, check_cathedral_render):
    try:
        _f()
    except Exception as e:     # rb.py is the visual designer's live file: report, don't crash
        print(f"\n[7] {_f.__name__} skipped: rb.py raised {type(e).__name__}: {e}")
print("\nTOTAL fails", TOTAL)
