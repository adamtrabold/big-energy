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
NS = 1.3                          # note / position-word size (Kalam), the smallest legend on the panel
UD_GAP = 1.75                     # up / down toggle words: 1.75 from the toggle, at LS x 0.72 = 1.69 (visual)
BESIDE_GAP = {"FOLLOW": 6.4}      # beside words' offset from the toggle centre (default 6.2)
BEHIND_EXTRA = 1.0                                 # behind-legends sit 1.0 further back (clear of the knobs' top ticks)
VARIANT = (sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] in ("P", "S") else os.environ.get("CATHEDRAL_LID", "P"))

lid = []      # name, x, d, r, kind ('k' knob / 't' toggle), legend, legend placement
BREAKS = []   # engraved group breaks: (x, d_from, d_to), vertical lines
SECTIONS = [] # group headings for the visual: (name, x, d)
NOTES = []    # small free legends: (text, x, d, size, anchor left/center/right)
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
    # steer 4: every toggle carries its positions under its name, listed lever-down -> lever-up (§18.1)
    L("PARA", 23.5, A2, "t", "para|mono · para · +4", "right2")     # whole bank: PARA + OSC MOD together at the bank's left
    L("OSC MOD", 48.0, A2, "t", "osc mod|off · on", "right2")       #   (review 3; the Model D's osc mod sits at the bank's top-left)
    L("OSC 3 CTL", 133.5, A2, "t", "osc 3 ctl|free · keys", "right2")   # VCO 3's own switch, under VCO 3
    L("SOURCE", 262.5, A2, "t", "source|noise · ext · fb", "right2")   # under NOISE / EXT, the knob it re-points (review 2)
    NOTES += [("para: detune", 88.5 + 3.525 + 1.6, A + KN + 3.5 + BEHIND_EXTRA, NS, "left"),   # FREQ 2 / 3 in PARA (review 9)
              ("para: detune", 153.5 + 3.525 + 1.6, A + KN + 3.5 + BEHIND_EXTRA, NS, "left")]
    SECTIONS += [("oscillators", 98.5, A + 16.9), ("mixer", 232.5, A + 16.9)]   # d 101.45 (visual: real Kalam vs "freq 2")
    # ---- band 2: CONTOURS. Score-8 fix 1: symmetric about the axis. Filter contour at the mirror of the loudness
    # contour's x (63.5 / 83.5 / 103.5 <-> 182.5 / 202.5 / 222.5), read A D S left to right; its two switches form a
    # left-edge column at x 23.5 that mirrors the out column at 262.5 (KBD <-> DRY PAN at d 49.5, FILT MOD <-> FOLLOW at
    # d 32.8). No break left of the filter knobs: the column belongs to the filter contour (the out column is another group).
    for n, x, lab in [("F ATTACK", 63.5, "attack"), ("F DECAY", 83.5, "decay"), ("F SUSTAIN", 103.5, "sustain"),
                      ("L ATTACK", 182.5, "attack"), ("L DECAY", 202.5, "decay"), ("L SUSTAIN", 222.5, "sustain")]:
        L(n, x, B, "k", lab, "behind")
    # KBD + FILT MOD leave the lid for the base filter group, beside CUTOFF (review 5; §18.4); the lone "filter"
    # heading and its rule go with them.
    L("VEL", 178.5, B2, "t", "velocity|loud · both · filt", "right2")  # the keys pair, under a small "keys" lead-in
    L("AFTERTOUCH", 203.0, B2, "t", "touch|mod · off · filt", "right2")
    NOTES.append(("keys", 173.9 - 1.5, B2, SW_LS, "right"))
    L("RELEASE", 143.0, 61.5, "t", "release|off · = decay", "right2")  # acts on BOTH contours (Model D), so it sits
                                                                    #   between them, on the axis over the window (review 6)
    # one heading per contour, each flush to the knob edge nearest the window, so the pair mirrors about the axis
    # (filter flush right at 110.95, loudness flush left at 175.05); flush left, "filter contour" ran into OSC MOD
    SECTIONS += [("filter contour", 103.5 + KN - len("filter contour") * 0.5 * HS / 2, 67.5),
                 ("loudness contour", 182.5 - KN + len("loudness contour") * 0.5 * HS / 2, 67.5)]
    # ---- band 3 (nearest the hinge, the BOTTOM): EFFECTS -> OUT. Echo left, the opening, reverb right; out in a column.
    for n, x, lab in [("ECHO TYPE", 23.5, "type"), ("ECHO TIME", 43.5, "time"), ("ECHO REPEATS", 76.0, "repeats"),
                      ("ECHO MIX", 96.0, "mix"), ("ECHO PAN", 116.0, "echo pan"),
                      ("REVERB TYPE", 182.5, "type"), ("REVERB DECAY", 202.5, "decay"), ("REVERB MIX", 222.5, "mix"),
                      ("VOLUME", 262.5, "volume")]:
        L(n, x, C, "k", lab, "front")
    L("FREE/SYNC", 62.0, C, "t", "sync|free", "updown")             # in the echo row, right of TIME's scale, before REPEATS
    L("DRY PAN", 262.5, B, "k", "dry pan", "behind")                # out column: DRY PAN -> FOLLOW -> VOLUME, top to bottom
    L("FOLLOW", 262.5, 32.8, "t", "own|follows dry", "beside")     # ends beside at ± 6.4, its name under it (review 7)
    NOTES += [("echo pan", 262.5, 32.8 - TGL - UD_GAP - 0.85 * SW_LS / 2, SW_LS, "center"),
              ("(off if follow)", 108.0, 25.05, NS, "center")]      # the cue by ECHO PAN: FOLLOW overrides it
    BREAKS.append((242.5, 7.0, B + 9.0))                            # reverb / loudness | out column
    SECTIONS += [("echo", 69.5, 26.5), ("reverb", 204.5, 26.5), ("out", 249.0, 58.0)]   # "out": top-left of its column (SOURCE took d 66.5)
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
                         ("ECHO PAN", 202.5, B, "echo pan"), ("REVERB TYPE", 222.5, B, "type"), ("REVERB DECAY", 242.5, B, "decay"),
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

BAT_H = 15.0   # base toggle: bat tip above the base plate, mini toggle on a low nut (ESTIMATE, UNVERIFIED part; §18.4)
def base(hk, hstick, hcut=12.15, htap=8.0, hbat=BAT_H):
    """PLAY row, steer 4 (review 4, 5): three groups, hero on the axis, stick <-> TAP mirrored about x 143.
    controllers: BEND 25 · MOD 47 · MOD MIX 67 · GLIDE 87 | filter: EMPHASIS 112.5 · KBD (t) 126.4 · CUTOFF 143 ·
    FILT MOD (t) 159.6 · AMOUNT 173.5 | tune: TUNE 199 · DRIFT 230 · TAP ("echo tap") 261. EMPHASIS / AMOUNT open out
    6.5 each way (119 -> 112.5, 167 -> 173.5) to seat the two toggles beside CUTOFF (gaps hold for both R-LOW Ø 10 and R-TALL Ø 14.9 knobs)."""
    return [("BEND stick", 25, 68, STK, hstick), ("MOD", 47, 68, KN, hk), ("MOD MIX", 67, 68, KN, hk), ("GLIDE", 87, 68, KN, hk),
            ("EMPHASIS", 112.5, 68, KN, hk), ("KBD CTRL", 126.4, 68, TGL, hbat), ("CUTOFF", 143, 68, CUT, hcut),
            ("FILTER MOD", 159.6, 68, TGL, hbat), ("CONTOUR AMT", 173.5, 68, KN, hk),
            ("TUNE", 199, 68, KN, hk), ("DRIFT", 230, 68, KN, hk), ("TAP", 261, 68, TAPR, htap)]
BASE_TOGGLES = {"KBD CTRL": "kbd|off · ⅓ · ⅔", "FILTER MOD": "filt mod|off · on"}
BASE_LEGEND = {"BEND stick": "bend", "MOD": "mod", "MOD MIX": "mod mix", "GLIDE": "glide", "EMPHASIS": "emphasis",
               "CUTOFF": "cutoff", "CONTOUR AMT": "amount", "TUNE": "tune", "DRIFT": "drift", "TAP": "echo tap"}
BASE_SECTIONS = [("controllers", 14.0, 85.0), ("filter", 105.0, 85.0), ("tune", 191.5, 85.0)]   # left-aligned, Kalam 2.4
BASE_LEDS = [(131.0, 81.0, 2.5), (155.0, 81.0, 2.5)]
BASE_R_DRAWN = {"BEND stick": None, "CUTOFF": CUT, "TAP": TAPR}   # R-LOW render: Tayda Ø 10 knobs (r 5) elsewhere

def base_check():
    """the base row in the open layout: gaps (R-TALL radii, the larger), pitch, and every legend as R-LOW draws it
    (knob legends in front, the stick's 11.5 below, toggle name + positions under the toggle, headings at y 85)."""
    bad, bs = [], base(13.5, 12.6)
    for a, b in itertools.combinations(bs, 2):
        dd = math.dist(a[1:3], b[1:3])
        if a[3] == KN and b[3] == KN and dd < 20 - 1e-6: bad.append(f"BASE PITCH {a[0]}/{b[0]}")
        if dd - a[3] - b[3] < 1.5 - 1e-6: bad.append(f"BASE GAP {a[0]}/{b[0]} {dd - a[3] - b[3]:.2f}")
    labs = []
    for n, x, y, r, h in bs:
        if n in BASE_TOGGLES:
            nm, pos = BASE_TOGGLES[n].split("|"); labs.append((n, legend2(x, y, nm, pos, "below2"))); continue
        t = BASE_LEGEND[n]; w, hh = len(t) * 0.5 * LS, 0.85 * LS
        cy = y - 11.5 if n == "BEND stick" else y - BASE_R_DRAWN.get(n, 5.0) - 3.5
        labs.append((n, (x - w / 2, cy - hh / 2, x + w / 2, cy + hh / 2)))
    for t, x, y in BASE_SECTIONS:
        labs.append(("base head " + t, (x, y - 0.425 * 2.4, x + len(t) * 0.5 * 2.4, y + 0.425 * 2.4)))
    ctl = [(n, x, y, (r if n not in BASE_R_DRAWN or BASE_R_DRAWN[n] else r) if r != KN else 5.0) for n, x, y, r, h in bs]
    ctl += [("led", x, y, r) for x, y, r in BASE_LEDS]
    for ln, b in labs:
        for n, x, y, r in ctl:
            if gap_bc(b, x, y, r) < 1.5 - 1e-6: bad.append(f"BASE LABEL {ln} vs {n} {gap_bc(b, x, y, r):.2f}")
    for (a, ba), (b, bb) in itertools.combinations(labs, 2):
        if gap_bb(ba, bb) < 1.5 - 1e-6: bad.append(f"BASE LABEL {a} vs {b} {gap_bb(ba, bb):.2f}")
    if abs((25 + 261) / 2 - 143) > 1e-6: bad.append("BASE stick / TAP mirror")
    return bad

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


def legend2(x, d, nm, pos, where="right2"):
    """a toggle's two-line legend: name (SW_LS) over its positions (NS, lever-down -> lever-up). 'right2': left-aligned
    at x + 6.2, the pair centred on the toggle's d (name line centre d + 0.85, positions d - 1.0). 'below2': centred
    under the toggle (base), name line first. Returns the block's box."""
    hn, hp = 0.85 * SW_LS, 0.85 * NS
    w = max(len(nm) * 0.5 * SW_LS, len(pos) * 0.5 * NS)
    if where == "right2":
        return (x + 6.2, d - 1.0 - hp / 2, x + 6.2 + w, d + 0.85 + hn / 2)
    top = d - TGL - 1.6
    return (x - w / 2, top - hn - 0.5 - hp, x + w / 2, top)

def note_boxes():
    out = []
    for t, x, d, sz, a in NOTES:
        w, h = len(t) * 0.5 * sz, 0.85 * sz
        x0 = x if a == "left" else (x - w if a == "right" else x - w / 2)
        out.append(("note " + t, (x0, d - h / 2, x0 + w, d + h / 2)))
    return out

def labels():
    out = []
    for n, x, d, r, k, lab, w in lid:
        if w == "right":
            wdt = len(lab) * 0.5 * SW_LS; h = 0.85 * SW_LS
            out.append((n, (x + 6.2, d - h / 2, x + 6.2 + wdt, d + h / 2)))
        elif w in ("right2", "below2"):                             # name over its positions, as one block
            nm, pos = lab.split("|"); bx = legend2(x, d, nm, pos, w); out.append((n, bx))
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
                       for t, x, d in SECTIONS] + decor() + note_boxes()
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
    v = check() + base_check()
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
