"""CATHEDRAL lid geometry check (systems). Steer 3, 2026-11-13: the lid re-ordered so it reads synth -> effects -> output
(owner: "synth stuff -> fx stuff -> output stuff like volume"). Two arrangements live here:
  P  "page order" (recommended, director's lead): three bands, far edge -> hinge = sources -> contours -> effects/out;
  S  "left-to-right stages" (alternative, differs in kind): synth on the left two-thirds, effects + out a right-hand block.
Run: python3 -I design/branches/concepts/cathedral/layout_check.py            (checks P, the live layout)
     python3 -I design/branches/concepts/cathedral/layout_check.py S          (checks S)
Rules as fold_r5_check: same-row knob pitch >= 20, gaps >= 1.5, >= 7 from a knob/toggle edge to an engraved break,
lid edge >= 16, seam >= 7, far rim, window >= 1.5; closed: every lid item landing within 3 mm (plan) of a base item
clears it by >= 2.0 in z; legends (estimated Kalam metrics: width 0.50 x size per char, height 0.85 x size) >= 1.5
from controls and other legends, >= 1.0 from the window. CATHEDRAL today: lid face closed z 37.6 (closed 52.7 incl.
pegs, lid +2.6). Distances d are from the hinge; d grows towards the lid's far edge, which reads as the TOP of the
panel both lying flat behind the base and standing (§17.2)."""
import math, itertools, os, sys
KN, TGL, CUT, STK, TAPR = 7.45, 4.6, 10.4, 6.0, 6.0
D = 108.0
A, A2, B, B2, C = 84.55, 70.0, 49.5, 35.0, 14.45   # band rows: A knobs, A' switches, B knobs, B' switches, C knobs
WIN = (143.0, 32.0, 23.0)                          # Ø 46 opening, concentric with the 50 mm driver (unchanged)
LS = 2.35                                          # FOLD legend size (Kalam)
SW_LS = 1.55                                       # switch legends beside their toggle (right, x + 6.2)
HS = 3.0                                           # group heading size: above the 2.35 legends (director fix 2)
BEHIND_EXTRA = 1.0                                 # behind-legends sit 1.0 further back (clear of the knobs' top ticks)
VARIANT = (sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] in ("P", "S") else os.environ.get("CATHEDRAL_LID", "P"))

lid = []      # name, x, d, r, kind ('k' knob / 't' toggle), legend, legend placement
BREAKS = []   # engraved group breaks: (x, d_from, d_to), vertical lines
SECTIONS = [] # group headings for the visual: (name, x, d)
def L(n, x, d, k, lab, where): lid.append((n, x, d, KN if k == "k" else TGL, k, lab, where))

if VARIANT == "P":
    # ---- band 1 (far edge, the TOP): SOURCES. Oscillators by VCO, then the mixer, one row; their switches beneath.
    # Score-8 fix 3: VCO 1 | 2 | 3 grouped by spacing: 20 inside a VCO, 25 between VCOs (edge gaps 5.1 vs 10.1), so the
    # row reads as three runs. Uses the row's whole width (RANGE 1 and NOISE / EXT both at the 16 mm edge rule).
    for n, x, lab in [("RANGE 1", 23.5, "range 1"), ("WAVE 1", 43.5, "wave 1"),
                      ("RANGE 2", 68.5, "range 2"), ("FREQ 2", 88.5, "freq 2"), ("WAVE 2", 108.5, "wave 2"),
                      ("RANGE 3", 133.5, "range 3"), ("FREQ 3", 153.5, "freq 3"), ("WAVE 3", 173.5, "wave 3"),
                      ("OSC 1", 202.5, "osc 1"), ("OSC 2", 222.5, "osc 2"), ("OSC 3", 242.5, "osc 3"), ("NOISE/EXT", 262.5, "noise / ext")]:
        L(n, x, A, "k", lab, "behind")                              # legends numbered (visual): which VCO, at a glance
    BREAKS.append((188.0, 70.5, A + 9.0))                           # oscillators | mixer (from d 70.5, above the contour heading)
    L("PARA", 33.5, A2, "t", "para", "right")                       # voice mode, under VCO 1 (the voice's first switch)
    L("OSC MOD", 88.5, A2, "t", "osc mod", "right")                 # wheel -> pitch, under VCO 2 (acts on all VCOs)
    L("OSC 3 CTL", 153.5, A2, "t", "osc 3 ctl", "right")            # VCO 3 keyboard on/off (LFO), under VCO 3 (visual's legend)
    L("SOURCE", 242.5, A2, "t", "source", "right")                  # noise / ext / feedback, under the mixer
    SECTIONS += [("oscillators", 98.5, A + 16.9), ("mixer", 232.5, A + 16.9)]   # d 101.45 (visual: real Kalam vs "freq 2")
    # ---- band 2: CONTOURS. Score-8 fix 1: symmetric about the axis. Filter contour at the mirror of the loudness
    # contour's x (63.5 / 83.5 / 103.5 <-> 182.5 / 202.5 / 222.5), read A D S left to right; its two switches form a
    # left-edge column at x 23.5 that mirrors the out column at 262.5 (KBD <-> DRY PAN at d 49.5, FILT MOD <-> FOLLOW at
    # d 32.8). No break left of the filter knobs: the column belongs to the filter contour (the out column is another group).
    for n, x, lab in [("F ATTACK", 63.5, "attack"), ("F DECAY", 83.5, "decay"), ("F SUSTAIN", 103.5, "sustain"),
                      ("L ATTACK", 182.5, "attack"), ("L DECAY", 202.5, "decay"), ("L SUSTAIN", 222.5, "sustain")]:
        L(n, x, B, "k", lab, "behind")
    L("KBD CTRL", 23.5, B, "t", "kbd", "right")                     # keyboard -> cutoff
    L("FILTER MOD", 23.5, B2, "t", "filt mod", "right")             # wheel -> cutoff; d 35, clear of ECHO TYPE's fan (visual)
    L("VEL", 178.5, B2, "t", "velocity", "right")                   # loud / both / filt: the keys' dynamics pair,
    L("AFTERTOUCH", 199.5, B2, "t", "touch", "right")               #   under the loudness contour (VEL's default)
    L("DECAY tgl", 222.0, B2, "t", "decay", "right")                # release = decay, loudness contour's own switch
    # one heading per contour (visual), flush left at its first knob's edge, between the contour legends and A'
    for t, x0 in (("filter contour", 63.5 - KN), ("loudness contour", 182.5 - KN)):
        SECTIONS.append((t, x0 + len(t) * 0.5 * HS / 2, 67.5))     # d 67.5 (visual: clear of the contour legends)
    SECTIONS.append(("filter", 21.0, 66.5))                         # the kbd / filt mod column's heading, mirroring "out"
    BREAKS.append((43.5, 31.0, 58.5))                               # its rule, mirroring the out rule, stopping above echo
    # ---- band 3 (nearest the hinge, the BOTTOM): EFFECTS -> OUT. Echo left, the opening, reverb right; out in a column.
    for n, x, lab in [("ECHO TYPE", 23.5, "type"), ("ECHO TIME", 43.5, "time"), ("ECHO REPEATS", 76.0, "repeats"),
                      ("ECHO MIX", 96.0, "mix"), ("DELAY PAN", 116.0, "delay pan"),
                      ("REVERB TYPE", 182.5, "type"), ("REVERB DECAY", 202.5, "decay"), ("REVERB MIX", 222.5, "mix"),
                      ("VOLUME", 262.5, "volume")]:
        L(n, x, C, "k", lab, "front")
    L("FREE/SYNC", 62.0, C, "t", "sync|free", "updown")             # in the echo row, right of TIME's scale, before REPEATS
    L("DRY PAN", 262.5, B, "k", "dry pan", "behind")                # out column: DRY PAN -> FOLLOW -> VOLUME, top to bottom
    L("FOLLOW", 262.5, 32.8, "t", "off|follow", "beside")          # words beside at ± 6.4 (visual)
    BREAKS.append((242.5, 7.0, B + 9.0))                            # reverb / loudness | out column
    SECTIONS += [("echo", 69.5, 26.5), ("reverb", 204.5, 26.5), ("out", 262.5, 66.5)]
    FX, FX_BREAKS = C, [242.5]                                      # kept for rb.py: the effects row and its break(s)
else:
    # ---- S: left-to-right stages. Synth = left two-thirds; effects + out = a 4-column block on the right (x >= 202.5).
    for n, x, lab in [("RANGE 1", 23.5, "range"), ("WAVE 1", 43.5, "wave"), ("RANGE 2", 63.5, "range"), ("FREQ 2", 83.5, "freq 2"),
                      ("WAVE 2", 103.5, "wave"), ("RANGE 3", 123.5, "range"), ("FREQ 3", 143.5, "freq 3"), ("WAVE 3", 163.5, "wave"),
                      ("ECHO TYPE", 197.5, "type"), ("ECHO TIME", 217.5, "time"), ("ECHO REPEATS", 240.5, "repeats"),
                      ("ECHO MIX", 260.5, "mix")]:
        L(n, x, A, "k", lab, "front" if n == "ECHO TYPE" else "behind")
    for n, x, d, lab in [("OSC 1", 23.5, B, "osc 1"), ("OSC 2", 43.5, B, "osc 2"), ("OSC 3", 23.5, C, "osc 3"), ("NOISE/EXT", 43.5, C, "noise"),
                         ("F ATTACK", 72.5, B, "attack"), ("F DECAY", 92.5, B, "decay"), ("F SUSTAIN", 112.5, B, "sustain"),
                         ("L ATTACK", 72.5, C, "attack"), ("L DECAY", 92.5, C, "decay"), ("L SUSTAIN", 112.5, C, "sustain"),
                         ("DELAY PAN", 202.5, B, "delay pan"), ("REVERB TYPE", 222.5, B, "type"), ("REVERB DECAY", 242.5, B, "decay"),
                         ("REVERB MIX", 262.5, B, "mix"), ("DRY PAN", 222.5, C, "dry pan"), ("VOLUME", 262.5, C, "volume")]:
        L(n, x, d, "k", lab, "front" if n == "REVERB TYPE" or d == C else "behind")
    L("PARA", 33.5, A2, "t", "para", "right"); L("OSC MOD", 93.5, A2, "t", "osc mod", "right")
    L("OSC 3 CTL", 143.5, A2, "t", "osc 3", "right"); L("FREE/SYNC", 232.5, A2 + 1.2, "t", "free|sync", "beside")
    L("SOURCE", 33.5, 32.0, "t", "src", "right")                    # in the middle of the mixer's 2 x 2 square
    for n, x, lab in [("KBD CTRL", 69.6, "kbd"), ("FILTER MOD", 84.2, "fm"), ("VEL", 98.8, "vel"), ("AFTERTOUCH", 113.4, "tch")]:
        L(n, x, 32.0, "t", lab, "above")                            # between the two contour rows, legends abbreviated
    L("DECAY tgl", 113.5, A2, "t", "decay", "right")               # no room left between the contours: up among the
                                                                    #   oscillator switches (a signal-path break, §17.4)
    L("FOLLOW", 242.5, C, "t", "follow|off", "updown")
    BREAKS += [(183.0, 7.0, A + 9.0), (58.0, 7.0, B + 9.0)]
    FX, FX_BREAKS = B, [183.0]
SWL = B2   # legacy name (rb.py): the switch line under the contours

def base(hk, hstick, hcut=12.15, htap=8.0):
    """PLAY row (unchanged by steer 3), symmetric about x 143: stick 25 <-> TAP 261, CUTOFF (hero) on the axis."""
    return [("BEND stick", 25, 68, STK, hstick), ("MOD", 47, 68, KN, hk), ("TUNE", 67, 68, KN, hk), ("GLIDE", 87, 68, KN, hk),
            ("EMPHASIS", 119, 68, KN, hk), ("CUTOFF", 143, 68, CUT, hcut), ("CONTOUR AMT", 167, 68, KN, hk),
            ("MOD MIX", 199, 68, KN, hk), ("DRIFT", 230, 68, KN, hk), ("TAP", 261, 68, TAPR, htap)]

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

ECHO_POS = [(-60, "tape"), (-20, "bbd"), (20, "clean"), (60, "ping-pong")]   # as the renders draw them (r5 / rb)
VERB_POS = [(-60, "plate"), (-20, "hall"), (20, "spring"), (60, "shimmer")]
def decor():
    """Printed marks that belong to a knob but sit outside its legend: the TYPE fans (names behind the knob, rb
    _type_fan: x + 11.85 sin a, d + r + 3.8 inner / 7.2 outer, Kalam 1.3) and TIME's note scale (rb time_dial full:
    1/16 1/8 1/4 1/2 at r + 5.0 / 4.8, size 1.25; tick ring to r + 3.6). Returned as legend boxes."""
    out = []
    for n, x, d, r, k, lab, w in lid:
        if n in ("ECHO TYPE", "REVERB TYPE"):
            for a, t in (ECHO_POS if n == "ECHO TYPE" else VERB_POS):
                th = math.radians(a); cx, cy = x + 11.85 * math.sin(th), d + r + (3.8 if abs(a) < 40 else 7.2)
                wd, h = len(t) * 0.5 * 1.3, 0.85 * 1.3
                out.append((n + " fan " + t, (cx - wd / 2, cy - h / 2, cx + wd / 2, cy + h / 2)))
        if n == "ECHO TIME":
            for i, t in ((0, "1/16"), (3, "1/8"), (6, "1/4"), (8, "1/2")):
                a = -135 + 33.75 * i; th = math.radians(a); rr = r + (5.0 if abs(a) < 120 else 4.8)
                cx, cy = x + rr * math.sin(th), d + rr * math.cos(th); wd, h = len(t) * 0.5 * 1.25, 0.85 * 1.25
                out.append((n + " scale " + t, (cx - wd / 2, cy - h / 2, cx + wd / 2, cy + h / 2)))
    return out
RING = {"ECHO TIME": 3.6}   # extra radius of a printed ring for control-to-control gaps

UD_GAP = 1.75                     # up / down toggle words: 1.75 from the toggle, at LS x 0.72 = 1.69 (visual)
BESIDE_GAP = {"FOLLOW": 6.4}      # beside words' offset from the toggle centre (default 6.2)

def labels():
    out = []
    for n, x, d, r, k, lab, w in lid:
        if w == "right":
            wdt = len(lab) * 0.5 * SW_LS; h = 0.85 * SW_LS
            out.append((n, (x + 6.2, d - h / 2, x + 6.2 + wdt, d + h / 2)))
        elif w == "updown":                                         # 'top|bottom', at FREE / SYNC's size, centred
            a, b = lab.split("|"); s = LS * 0.72; h = 0.85 * s
            for t, cy in ((a, d + r + UD_GAP + h / 2), (b, d - r - UD_GAP - h / 2)):
                wdt = len(t) * 0.5 * s; out.append((n + ":" + t, (x - wdt / 2, cy - h / 2, x + wdt / 2, cy + h / 2)))
        elif w == "beside":
            a, b = lab.split("|"); s = LS * 0.72; g = BESIDE_GAP.get(n, 6.2)
            out.append((n + ":" + a, (x - g - len(a) * 0.5 * s, d - 0.43 * s, x - g, d + 0.43 * s)))
            out.append((n + ":" + b, (x + g, d - 0.43 * s, x + g + len(b) * 0.5 * s, d + 0.43 * s)))
        else:
            bx = tbox(x, d, lab, LS if k == "k" else LS * 0.85, w, r)
            if w == "behind": bx = (bx[0], bx[1] + BEHIND_EXTRA, bx[2], bx[3] + BEHIND_EXTRA)
            out.append((n, bx))
    return out

def check():
    bad = []
    for a, b in itertools.combinations(lid, 2):
        dd = math.dist(a[1:3], b[1:3])
        if a[4] == b[4] == "k" and a[2] == b[2] and dd < 20 - 1e-6: bad.append(f"PITCH {a[0]}/{b[0]} {dd:.2f}")
        if dd - a[3] - b[3] - RING.get(a[0], 0) - RING.get(b[0], 0) < 1.5 - 1e-6:
            bad.append(f"GAP {a[0]}/{b[0]} {dd - a[3] - b[3] - RING.get(a[0], 0) - RING.get(b[0], 0):.2f}")
    for n, x, d, r, k, *_ in lid:
        for bx, d0, d1 in BREAKS:
            if d0 - r < d < d1 + r and abs(x - bx) - r < 7 - 1e-6: bad.append(f"BREAK {n} @ x {bx}")
        if math.dist((x, d), WIN[:2]) - r - WIN[2] < 1.5 - 1e-6: bad.append(f"WINDOW {n}")
        if x - r < 16 - 1e-6 or 286 - (x + r) < 16 - 1e-6: bad.append(f"EDGE {n}")
        if d - r < 7 - 1e-6: bad.append(f"SEAM {n}")
        if d + r > D - 4 - 12 + 1e-6: bad.append(f"FAR RIM {n}")
    labs = labels() + [("head " + t, (x - len(t) * 0.5 * HS / 2, d - 0.425 * HS, x + len(t) * 0.5 * HS / 2, d + 0.425 * HS))
                       for t, x, d in SECTIONS] + decor()
    for ln, b in labs:
        for n, x, d, r, k, *_ in lid:
            if ln.startswith(n + " ") and (" fan " in ln or " scale " in ln): continue   # a knob's own fan / scale
            if gap_bc(b, x, d, r) < 1.5 - 1e-6: bad.append(f"LABEL {ln} vs {n} {gap_bc(b, x, d, r):.2f}")
        if gap_bc(b, *WIN) < 1.0: bad.append(f"LABEL {ln} vs window {gap_bc(b, *WIN):.2f}")
        if b[3] > D - 4 or b[1] < 0.5: bad.append(f"LABEL {ln} off the plate")
        for bx, d0, d1 in BREAKS:
            if b[0] - 1.5 < bx < b[2] + 1.5 and b[1] < d1 and b[3] > d0: bad.append(f"LABEL {ln} on the break @ x {bx}")
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

def reach(name, frm=(143.0, 68.0)):
    """Plan distance (mm) from a base point (default CUTOFF) to a lid control with the lid standing: the lid's d adds to
    the base's depth behind the hinge (base y 108) plus the hinge offset (~6), so a lid control sits at y ~ 114 + d."""
    x, d = next((x, d) for n, x, d, *_ in lid if n == name)
    return math.dist(frm, (x, 114.0 + d))

if __name__ == "__main__":
    v = check()
    print(f"variant {VARIANT}: {sum(1 for i in lid if i[4] == 'k')} knobs, {sum(1 for i in lid if i[4] == 't')} toggles")
    print(f"open layout + labels: {len(v)} violations"); [print("  ", x) for x in v]
    print("closed (lid face today z 37.6; closed 52.7):")
    for nm, hk, hs in [("R-TALL: today's knobs (13.5), stick 12.6", 13.5, 12.6),
                       ("R-LOW: Tayda 10 x 8 knobs (seat 1.0 → 9.0), stick as is 12.6", 9.0, 12.6),
                       ("R-LOW: Tayda 10 x 8 (9.0), stick lowered to 9.0", 9.0, 9.0),
                       ("R-LOW: Tayda 10 x 8 with a nut under it (10.5), stick 9.0", 10.5, 9.0)]:
        need, w = closed_need(base(hk, hs))
        print(f"  {nm}: face ≥ {need:.2f} → +{need - 37.6:.1f} → closed ≈ {52.7 + need - 37.6:.1f} mm (binding: {w[0]} over {w[1]})")
    print("reach from TAP (261, 68) with the lid standing:", {n: round(reach(n, (261, 68))) for n in ("VOLUME", "ECHO TIME", "FREE/SYNC")})
    print("reach from CUTOFF:", {n: round(reach(n)) for n in ("ECHO MIX", "REVERB MIX", "F ATTACK", "OSC 1")})
