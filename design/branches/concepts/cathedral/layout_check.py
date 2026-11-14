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
TS_LEAD = (1.2, 1.3)              # two-line toggle legend: name centre d + 1.2, positions centre d - 1.3 (visual, 4e52223)
UNDER_GAP = 2.0                   # "free · sync" under its toggle (visual: at 1.75 real Kalam sat 1.27 from the nut)
OUT_X, OUT_BREAK = 255.0, 238.75  # out column (DRY PAN, FOLLOW, VOLUME) moved in from 262.5 so FOLLOW's "own · follows
                                  #   dry" (≈ 13.8 real) ends on the plate with the column still in line; its break
                                  #   moves with it (7 from REVERB MIX / L SUSTAIN at 222.5 and from the column)
NUM_S = 2.35                      # VCO numerals, at legend size
SUB_S = 2.35                      # sub-heads ("filter", "amp"): legend size, under the 3.0 heading
NS = 1.3                          # note / position-word size (Kalam), the smallest legend on the panel
UD_GAP = 1.75                     # up / down toggle words: 1.75 from the toggle, at LS x 0.72 = 1.69 (visual)
BESIDE_GAP = {"FOLLOW": 6.4}      # beside words' offset from the toggle centre (default 6.2)
BEHIND_EXTRA = 1.0                                 # behind-legends sit 1.0 further back (clear of the knobs' top ticks)
VARIANT = (sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] in ("P", "S", "P5O", "P5R") else os.environ.get("CATHEDRAL_LID", "P5O"))
# steer 5 (2026-11-13 evening): both halves 132 deep (D), a two-row base, two lid options:
#   P5O  the owner's lid direction (20:43): oscillators stacked on the left, filter round the window, amp along the top
#   P5R  the director's rule laid in rows: oscillators ‖ tuning on top, envelopes round the window, effects below
# P (steer 4) and S (steer 3) stay as history at D 108.
STEER5 = VARIANT in ("P5O", "P5R")
M = 5.0                                            # the module (mm): every spacing below is a multiple of it (§19.3)
if STEER5:
    D = 132.0                                      # +24: a second base row (y 93) and the battery strip behind it
    WIN = (143.0, D - 68.0, 23.0)                  # the window stays over CUTOFF (base y 68) -> lid d 64

lid = []      # name, x, d, r, kind ('k' knob / 't' toggle), legend, legend placement
BREAKS = []   # engraved group breaks: (x, d_from, d_to), vertical lines
SECTIONS = [] # group headings for the visual: (name, x, d)
NOTES = []    # small free legends: (text, x, d, size, anchor left/center/right)
SUBHEADS = [] # sub-heads under a heading: (text, x, d), Kalam SUB_S
DOTS = []     # link dots (Ø 1.2): (name, x, d, paired control)
def L(n, x, d, k, lab, where): lid.append((n, x, d, KN if k == "k" else TGL, k, lab, where))

if VARIANT == "P5O":
    # ---- the owner's lid (20:43): "oscillators should all be stacked on the left, then top case filter/envelope where
    # there's less room cuz of speaker in the middle, then amp controls going left to right in the top row".
    # Rows at 5M pitch: R1 104, R2 79, R3 54, R4 29. Read by zones, left to right: oscillators -> filter (round the
    # window) -> amp (along the top) -> effects and out (right, top to bottom).
    R1, R2, R3, R4 = 104.0, 79.0, 54.0, 29.0
    OX = (38.6, 58.6, 78.6)                        # octave · pitch · wave columns (x 38.6: clear of the bend stick, closed)
    for n, x, d, lab in [("RANGE 1", OX[0], R1, "octave"), ("TUNE", OX[1], R1, "tune"), ("WAVE 1", OX[2], R1, "wave"),
                         ("DRIFT", 98.6, R1, "drift"),
                         ("RANGE 2", OX[0], R2, "octave"), ("FREQ 2", OX[1], R2, "pitch"), ("WAVE 2", OX[2], R2, "wave"),
                         ("RANGE 3", OX[0], R3, "octave"), ("FREQ 3", OX[1], R3, "pitch"), ("WAVE 3", OX[2], R3, "wave")]:
        L(n, x, d, "k", lab, "behind")             # VCO 1's pitch slot is master tune (the Model D's osc 1 has no freq)
    NOTES += [(t, 24.0, d, NUM_S, "center") for t, d in (("1", R1), ("2", R2), ("3", R3))]   # each VCO row numbered
    L("PARA", OX[0], R4, "t", "voices|1 · 3 · 4", "right2")        # the bank's switches under the block
    L("OSC MOD", OX[1], R4, "t", "mod|off · on", "right2")
    L("OSC 3 CTL", OX[2], R4, "t", "track|off · on", "right2")
    BREAKS.append((93.5, 20.0, 88.0))                              # oscillators | filter
    # filter envelope: a column down the window's left side (attack · decay · sustain, top to bottom)
    for n, d, lab in [("F ATTACK", R2, "attack"), ("F DECAY", R3, "decay"), ("F SUSTAIN", R4, "sustain")]:
        L(n, 108.5, d, "k", lab, "behind")
    # keys: the window's right side
    L("VEL", 174.0, R2, "t", "velocity|amp · both · filter", "right2")
    L("AFTERTOUCH", 174.0, R3, "t", "touch|mod · off · filter", "right2")
    # amp along the top row, then echo continues it
    for n, x, lab, w in [("L ATTACK", 128.5, "attack", "behind"), ("L DECAY", 148.5, "decay", "behind"),
                         ("L SUSTAIN", 168.5, "sustain", "behind"), ("ECHO TYPE", 198.4, "type", "front"),
                         ("ECHO TIME", 218.4, "time", "behind"), ("ECHO REPEATS", 251.55, "repeats", "behind")]:
        L(n, x, R1, "k", lab, w)
    L("FREE/SYNC", 238.0, R1, "t", "free · sync", "under")
    BREAKS += [(113.5, 96.0, 113.0), (183.5, 96.0, 113.0)]          # tuning | amp | echo on the top row
    L("ECHO PAN", 210.0, R2, "k", "pan", "behind")                   # echo's pan, under its time
    L("REVERB TYPE", 202.0, R3, "k", "type", "front"); L("REVERB DECAY", 222.0, R3, "k", "decay", "behind")
    L("DRY PAN", 232.0, R4, "k", "pan", "behind"); L("FOLLOW", 252.0, R4, "t", "link|off · on", "right2")
    DOTS += [("dot echo pan", 213.9, R2 + KN + 3.5 + BEHIND_EXTRA, "ECHO PAN"), ("dot link", 252.0 + 6.2 + 8 * 0.5 * NS + 2.1, R4 + TS_LEAD[0], "FOLLOW")]
    SECTIONS += [("oscillators", 68.6, 120.9), ("filter", 108.5, 120.9), ("amp", 148.5, 120.9), ("keys", 174.0, 120.9),
                 ("echo", 225.0, 120.9), ("reverb", 212.0, 37.5), ("out", 242.0, 15.0)]
    FX, FX_BREAKS, SWL = R1, [183.5], R4
elif VARIANT == "P5R":
    # ---- the director's rule in rows (§19.1): A oscillators ‖ tuning, B envelopes round the window with keys and out
    # columns, C the effect settings. Rows C 29 -> B 64 (7M) -> A 104 (8M: room for "envelopes" over the window).
    A5, A5s, B5, C5 = 104.0, 89.0, 64.0, 29.0
    for n, x, lab in [("RANGE 1", 43, "octave"), ("WAVE 1", 63, "wave"), ("RANGE 2", 88, "octave"), ("FREQ 2", 108, "pitch"),
                      ("WAVE 2", 128, "wave"), ("RANGE 3", 153, "octave"), ("FREQ 3", 173, "pitch"), ("WAVE 3", 193, "wave"),
                      ("TUNE", 223, "tune"), ("DRIFT", 243, "drift")]:
        L(n, x, A5, "k", lab, "behind")
    NOTES += [(t, x, A5, NUM_S, "center") for t, x in (("1", 30.0), ("2", 75.5), ("3", 140.5))]
    BREAKS.append((208.0, 96.0, 113.0))                             # oscillators | tuning
    L("PARA", 38.0, A5s, "t", "voices|1 · 3 · 4", "right2"); L("OSC MOD", 58.0, A5s, "t", "mod|off · on", "right2")
    L("OSC 3 CTL", 173.0, A5s, "t", "track|off · on", "right2")
    for n, x, lab in [("F ATTACK", 70, "attack"), ("F DECAY", 90, "decay"), ("F SUSTAIN", 110, "sustain"),
                      ("L ATTACK", 176, "attack"), ("L DECAY", 196, "decay"), ("L SUSTAIN", 216, "sustain")]:
        L(n, x, B5, "k", lab, "behind")
    L("VEL", 40.0, B5, "t", "velocity|amp · both · filter", "left2")
    L("AFTERTOUCH", 40.0, 49.5, "t", "touch|mod · off · filter", "left2")
    L("DRY PAN", 246.0, B5, "k", "pan", "behind"); L("FOLLOW", 246.0, 49.5, "t", "link|off · on", "right2")
    BREAKS += [(55.0, 40.0, 76.0), (231.0, 40.0, 76.0)]             # keys | envelopes | out
    for n, x, lab in [("ECHO TYPE", 37, "type"), ("ECHO TIME", 57, "time"), ("ECHO REPEATS", 90.5, "repeats"),
                      ("ECHO PAN", 110.5, "pan"), ("REVERB TYPE", 175.5, "type"), ("REVERB DECAY", 195.5, "decay")]:
        L(n, x, C5, "k", lab, "front")
    L("FREE/SYNC", 76.6, C5, "t", "free · sync", "under")
    DOTS += [("dot echo pan", 114.4, C5 - KN - 3.5, "ECHO PAN"), ("dot link", 246.0 + 6.2 + 8 * 0.5 * NS + 2.1, 49.5 + TS_LEAD[0], "FOLLOW")]
    SECTIONS += [("oscillators", 118.0, 120.9), ("tuning", 233.0, 120.9), ("envelopes", 143.0, 91.8), ("keys", 40.0, 81.5),
                 ("out", 246.0, 81.5), ("echo", 73.75, 47.5), ("reverb", 185.5, 47.5)]
    SUBHEADS += [("filter", 90.0, 79.5), ("amp", 196.0, 79.5)]
    FX, FX_BREAKS, SWL = C5, [231.0], 49.5
elif VARIANT == "P":
    # Steer 4, owner rule 19:57 ("Labels should only be one word ..."): every word from the director's vocabulary.md.
    # ---- band 1 (far edge, the TOP): oscillators (VCO 1 | 2 | 3 by spacing, 20 inside / 25 between) ‖ mixer.
    for n, x, lab in [("RANGE 1", 23.5, "octave"), ("WAVE 1", 43.5, "wave"),
                      ("RANGE 2", 68.5, "octave"), ("FREQ 2", 88.5, "pitch"), ("WAVE 2", 108.5, "wave"),
                      ("RANGE 3", 133.5, "octave"), ("FREQ 3", 153.5, "pitch"), ("WAVE 3", 173.5, "wave"),
                      ("OSC 1", 202.5, "1"), ("OSC 2", 222.5, "2"), ("OSC 3", 242.5, "3"), ("NOISE/EXT", 262.5, "extra")]:
        L(n, x, A, "k", lab, "behind")
    # the VCO numerals: there's no room OVER the groups (2.1 mm between the legends and "oscillators"), so each numeral
    # leads its group at knob height, in the gap before its first knob (x 10 / 56 / 121), like channel numbers
    NOTES += [(t, x, A, NUM_S, "center") for t, x in (("1", 10.0), ("2", 56.0), ("3", 121.0))]
    BREAKS.append((188.0, 70.5, A + 9.0))                           # oscillators | mixer
    L("PARA", 23.5, A2, "t", "voices|1 · 3 · 4", "right2")          # whole bank: voices + mod together at the bank's left
    L("OSC MOD", 50.0, A2, "t", "mod|off · on", "right2")
    L("OSC 3 CTL", 121.0, A2, "t", "track|off · on", "left2")       # legend LEFT (visual: on the right it read "track envelopes"); x 121, under the "3" that leads
                                                                    #   VCO 3 (director: at 163.5 it read as an envelope switch).
                                                                    #   x 133.5, under octave 3, puts its legend into "envelopes"
                                                                    #   (the scan fails from x 124: gap 0.85)
    L("SOURCE", 257.5, A2, "t", "source|noise · input · loop", "right2")   # under EXTRA; x 257.5 keeps the line inside the rim
    SECTIONS += [("oscillators", 98.5, A + 16.9), ("mixer", 232.5, A + 16.9)]
    # ---- band 2: keys column | filter envelope | release (axis) | amp envelope | out column
    for n, x, lab in [("F ATTACK", 63.5, "attack"), ("F DECAY", 83.5, "decay"), ("F SUSTAIN", 103.5, "sustain"),
                      ("L ATTACK", 182.5, "attack"), ("L DECAY", 202.5, "decay"), ("L SUSTAIN", 222.5, "sustain")]:
        L(n, x, B, "k", lab, "behind")
    L("VEL", 48.0, B, "t", "velocity|amp · both · filter", "left2")
    L("AFTERTOUCH", 48.0, 36.5, "t", "touch|mod · off · filter", "left2")   # d 36.5: legend ≥ 3 from ECHO TYPE's fan
    SECTIONS.append(("keys", 37.0, 58.0))
    L("RELEASE", 143.0, 61.5, "t", "release|off · on", "right2")    # centred under "envelopes", between the two groups:
                                                                    #   its place says it acts on both
    SECTIONS.append(("envelopes", 143.0, 69.8))                     # one heading over both groups, on the axis (0.8 up: visual,
                                                                    #   real Kalam sat 0.73 from RELEASE's nut)
    SUBHEADS += [("filter", 83.5, 68.5), ("amp", 202.5, 68.5)]     # visual fec6093: centred over their groups on the
                                                                    #   heading line ("filter · envelopes · amp"); lower down
                                                                    #   they read as "filter sustain" / "amp attack"
    # ---- band 3 (nearest the hinge, the BOTTOM): echo · window · reverb ‖ out column
    for n, x, lab in [("ECHO TYPE", 23.5, "type"), ("ECHO TIME", 43.5, "time"), ("ECHO REPEATS", 76.0, "repeats"),
                      ("ECHO MIX", 96.0, "mix"), ("ECHO PAN", 116.0, "pan"),
                      ("REVERB TYPE", 182.5, "type"), ("REVERB DECAY", 202.5, "decay"), ("REVERB MIX", 222.5, "mix"),
                      ("VOLUME", OUT_X, "volume")]:
        L(n, x, C, "k", lab, "front")
    L("FREE/SYNC", 62.0, C, "t", "free · sync", "under")            # throws left / right; its words in throw order under it
    L("DRY PAN", OUT_X, B, "k", "pan", "behind")                    # out column: pan -> link -> volume, top to bottom
    L("FOLLOW", OUT_X, 32.8, "t", "link|off · on", "right2")        # on = the echo pan follows this pan
    # matching link dots (Ø 1.2): one right of the echo "pan" legend, one right of "link"
    DOTS += [("dot echo pan", 120.0, C - KN - 3.5, "ECHO PAN"), ("dot link", OUT_X + 6.2 + 8 * 0.5 * NS + 2.1, 32.8 + TS_LEAD[0], "FOLLOW")]
    BREAKS.append((OUT_BREAK, 7.0, B + 9.0))                        # reverb / amp | out column
    SECTIONS += [("echo", 69.5, 26.5), ("reverb", 204.5, 26.5), ("out", 248.5, 66.5)]
    FX, FX_BREAKS = C, [OUT_BREAK]                                  # kept for rb.py: the effects row and its break(s)
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
if VARIANT in ("P", "S"):
    SWL = B2   # legacy name (rb.py): the switch line under the contours

THROW = "left-right"   # steer 4 score-8 fix 1: every toggle (lid and base) mounted to throw left / right, the same part
                       # rotated 90°; position words read left · middle · right. Plan footprint: a ~10 mm bat at ±20°
                       # tips ~3.4 mm off its axis, inside the 4.6 nut circle the checks already use (ESTIMATE)
BAT_H = 15.0   # base toggle: bat tip above the base plate, mini toggle on a low nut (ESTIMATE, UNVERIFIED part; §18.4)
def base(hk, hstick, hcut=12.15, htap=8.0, hbat=BAT_H):
    """PLAY row, steer 4 (review 4, 5): three groups, hero on the axis, stick <-> TAP mirrored about x 143.
    controllers: BEND 25 · MOD 47 · MOD MIX 67 · GLIDE 87 | filter: EMPHASIS 112.5 · KBD (t) 126.4 · CUTOFF 143 ·
    FILT MOD (t) 159.6 · AMOUNT 173.5 | tune: TUNE 199 · DRIFT 222 ‖ TAP ("echo tap") 261, alone behind a break at x 242.2. EMPHASIS / AMOUNT open out
    6.5 each way (119 -> 112.5, 167 -> 173.5) to seat the two toggles beside CUTOFF (gaps hold for both R-LOW Ø 10 and R-TALL Ø 14.9 knobs)."""
    if STEER5:   # two rows (§19.2): front y 68 = what the hands ride; rear y 93 = the levels, both left to right in order
        return [("BEND stick", 25.5, 68, STK, hstick), ("MOD", 43.5, 68, KN, hk), ("MOD MIX", 63.5, 68, KN, hk),
                ("GLIDE", 83.5, 68, KN, hk), ("EMPHASIS", 112.5, 68, KN, hk), ("KBD CTRL", 126.4, 68, TGL, hbat),
                ("CUTOFF", 143, 68, CUT, hcut), ("FILTER MOD", 159.6, 68, TGL, hbat), ("CONTOUR AMT", 173.5, 68, KN, hk),
                ("VOLUME", 232.5, 68, KN, hk), ("TAP", 260.5, 68, TAPR, htap),
                ("RELEASE", 25.5, 93, TGL, hbat), ("OSC 1", 52.5, 93, KN, hk), ("OSC 2", 72.5, 93, KN, hk),
                ("OSC 3", 92.5, 93, KN, hk), ("NOISE/EXT", 112.5, 93, KN, hk), ("SOURCE", 129.1, 93, TGL, hbat),
                ("ECHO MIX", 189, 93, KN, hk), ("REVERB MIX", 209, 93, KN, hk)]
    return [("BEND stick", 25, 68, STK, hstick), ("MOD", 47, 68, KN, hk), ("MOD MIX", 67, 68, KN, hk), ("GLIDE", 87, 68, KN, hk),
            ("EMPHASIS", 112.5, 68, KN, hk), ("KBD CTRL", 126.4, 68, TGL, hbat), ("CUTOFF", 143, 68, CUT, hcut),
            ("FILTER MOD", 159.6, 68, TGL, hbat), ("CONTOUR AMT", 173.5, 68, KN, hk),
            ("TUNE", 199, 68, KN, hk), ("DRIFT", 222, 68, KN, hk), ("TAP", 261, 68, TAPR, htap)]
BASE_TOGGLES = {"KBD CTRL": "track|off · 1/3 · 2/3", "FILTER MOD": "mod|off · on"}   # spelled out: Kalam has no ⅓ ⅔
BASE_LEGEND = {"BEND stick": "bend", "MOD": "mod", "MOD MIX": "blend", "GLIDE": "glide", "EMPHASIS": "resonance",
               "CUTOFF": "cutoff", "CONTOUR AMT": "envelope", "TUNE": "tune", "DRIFT": "drift", "TAP": "tap"}
BASE_SECTIONS = [("controllers", 14.0, 85.0), ("filter", 105.0, 85.0), ("tuning", 191.5, 85.0), ("tempo", 255.0, 85.0)]   # left-aligned, Kalam 2.4
BASE_LEDS = [(131.0, 81.0, 2.5), (155.0, 81.0, 2.5)]
BASE_NOTES = [("midi", 131.0, 81.0 + 2.5 + 1.8 + 0.85 * 1.55 / 2), ("status", 155.0, 81.0 + 2.5 + 1.8 + 0.85 * 1.55 / 2)]
              # the two lights named, behind them (131: not-in-control / MIDI holds a knob; 155: status), Kalam 1.55
BASE_BREAKS = [(242.2, 56.0, 80.0)]   # tune ‖ echo tap: TAP stands alone at the end (director fix 4), x, y from, y to
BASE_R_DRAWN = {"BEND stick": None, "CUTOFF": CUT, "TAP": TAPR}   # R-LOW render: Tayda Ø 10 knobs (r 5) elsewhere
if STEER5:
    BASE_TOGGLES = {"KBD CTRL": "track|off · 1/3 · 2/3", "FILTER MOD": "mod|off · on", "RELEASE": "release|off · on",
                    "SOURCE": "source|noise · input · loop"}
    BASE_LEGEND = {"BEND stick": "bend", "MOD": "mod", "MOD MIX": "blend", "GLIDE": "glide", "EMPHASIS": "resonance",
                   "CUTOFF": "cutoff", "CONTOUR AMT": "envelope", "VOLUME": "volume", "TAP": "tap", "OSC 1": "1",
                   "OSC 2": "2", "OSC 3": "3", "NOISE/EXT": "extra", "ECHO MIX": "echo", "REVERB MIX": "reverb"}
    BASE_SECTIONS = [("controllers", 14.0, 78.0), ("filter", 105.0, 78.0), ("out", 225.5, 78.0), ("tempo", 254.5, 78.0),
                     ("mixer", 45.5, 103.5), ("effects", 182.0, 103.5)]
    BASE_LEDS = [(231.0, 93.0, 2.5), (251.0, 93.0, 2.5)]
    BASE_NOTES = [("midi", 231.0, 93.0 - 2.5 - 1.8 - 0.85 * 1.55 / 2), ("status", 251.0, 93.0 - 2.5 - 1.8 - 0.85 * 1.55 / 2)]
    BASE_BREAKS = [(247.0, 58.0, 80.0)]          # out ‖ tempo
    BATTERY = (15.0, 100.0, 185.0, 126.0)        # 4 × 952540 cells, 1S4P, under the plate behind the rear row
    DAISY = (190.0, 100.0, 270.0, 126.0)

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
        cy = {"BEND stick": y - 11.5, "CUTOFF": y - CUT - 3.5, "TAP": y - TAPR - 3.5}.get(n, y - 10.95)   # R-LOW render
        labs.append((n, (x - w / 2, cy - hh / 2, x + w / 2, cy + hh / 2)))
    for t, x, y in BASE_NOTES:
        w, hh = len(t) * 0.5 * SW_LS, 0.85 * SW_LS; labs.append(("base note " + t, (x - w / 2, y - hh / 2, x + w / 2, y + hh / 2)))
    for t, x, y in BASE_SECTIONS:
        labs.append(("base head " + t, (x, y - 0.425 * 2.4, x + len(t) * 0.5 * 2.4, y + 0.425 * 2.4)))
    ctl = [(n, x, y, 7.0 if r == KN else r) for n, x, y, r, h in bs]   # low knobs measured to their tick ring (6.0 + 1.0)
    ctl += [("led", x, y, r) for x, y, r in BASE_LEDS]
    for ln, b in labs:
        for n, x, y, r in ctl:
            if gap_bc(b, x, y, r) < 1.5 - 1e-6: bad.append(f"BASE LABEL {ln} vs {n} {gap_bc(b, x, y, r):.2f}")
    for (a, ba), (b, bb) in itertools.combinations(labs, 2):
        if gap_bb(ba, bb) < 1.5 - 1e-6: bad.append(f"BASE LABEL {a} vs {b} {gap_bb(ba, bb):.2f}")
    for bx, y0, y1 in BASE_BREAKS:
        for n, x, y, r, h in bs:
            if y0 - r < y < y1 + r and abs(x - bx) - r < 7 - 1e-6: bad.append(f"BASE BREAK {n} @ x {bx}")
        for ln, b in labs:
            if b[0] - 1.5 < bx < b[2] + 1.5 and b[1] < y1 and b[3] > y0: bad.append(f"BASE LABEL {ln} on the break @ x {bx}")
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

ECHO_POS = [(-60, "tape"), (-20, "dark"), (20, "clean"), (60, "pingpong")]   # as the renders draw them (r5 / rb)
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
    if where == "right2":                                           # real-Kalam leading (visual): d + 1.1 / d - 1.25
        return (x + 6.2, d - TS_LEAD[1] - hp / 2, x + 6.2 + w, d + TS_LEAD[0] + hn / 2)
    if where == "left2":                                            # the mirror: right-aligned at x - 6.2
        return (x - 6.2 - w, d - TS_LEAD[1] - hp / 2, x - 6.2, d + TS_LEAD[0] + hn / 2)
    top = d - TGL - 2.1                                             # base: under the toggle, 0.9 between the lines
    return (x - w / 2, top - hn - 0.9 - hp, x + w / 2, top)

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
        elif w == "under":                                          # one line, centred under the toggle (FREE / SYNC)
            wdt, h = len(lab) * 0.5 * SW_LS, 0.85 * SW_LS; cy = d - r - UNDER_GAP - h / 2
            out.append((n, (x - wdt / 2, cy - h / 2, x + wdt / 2, cy + h / 2)))
        elif w in ("right2", "left2", "below2"):                             # name over its positions, as one block
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
                       for t, x, d in SECTIONS] + decor() + note_boxes() + \
           [("sub " + t, (x - len(t) * 0.5 * SUB_S / 2, d - 0.425 * SUB_S, x + len(t) * 0.5 * SUB_S / 2, d + 0.425 * SUB_S))
            for t, x, d in SUBHEADS] + [(n, (x - 0.6, d - 0.6, x + 0.6, d + 0.6)) for n, x, d, _ in DOTS]
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
    # the plate's inner edge (rb lid_plate2d: x 4.3 .. 281.7): legends end >= 1.5 inside it, with widths at x 1.25
    # (real Kalam runs ~25 % wider than the 0.50 estimate at these sizes: "own · follows dry" 11.05 est., 13.8 real)
    for ln, b in labs:
        x0 = b[0] if b[0] < 143 else b[0]
        w = (b[2] - b[0]) * 1.25
        if b[0] > 143 and b[0] + w > 281.7 - 1.5: bad.append(f"RIM {ln} ends {b[0] + w:.1f}")
        if b[2] < 143 and b[2] - w < 4.3 + 1.5: bad.append(f"RIM {ln} starts {b[2] - w:.1f}")
    # the touch legend keeps 3 mm from ECHO TYPE's fan names (director, steer 4 score 9)
    tb = dict(labs).get("AFTERTOUCH")
    if tb:
        for ln, b in labs:
            if ln.startswith("ECHO TYPE fan") and gap_bb(tb, b) < 3.0 - 1e-6: bad.append(f"TOUCH vs {ln} {gap_bb(tb, b):.2f}")
    return bad

# ---- steer 5: the module system and the softer corners (§19.3, §19.6) -----------------------------------------
SE_N = 5.0          # corner exponent: |u|^n + |v|^n = 1, a continuous-curvature (G2-like) corner, not an arc (owner 20:5x)
PLATE_RC = 16.0     # plate corner size (was an R 7.7 arc); the visual sets the final size; §19.6 gives the largest that fits
CASE_RC = PLATE_RC + 4.3   # the case outline, concentric (4.3 wall)
def se_outline(x0, y0, x1, y1, rc, n=SE_N, k=90):
    """sampled outline of a rectangle whose four corners are superellipse quadrants of size rc."""
    pts = []
    for cx, cy, sx, sy in ((x1 - rc, y1 - rc, 1, 1), (x0 + rc, y1 - rc, -1, 1), (x0 + rc, y0 + rc, -1, -1), (x1 - rc, y0 + rc, 1, -1)):
        for i in range(k + 1):
            t = math.pi / 2 * i / k
            pts.append((cx + sx * rc * math.cos(t) ** (2 / n), cy + sy * rc * math.sin(t) ** (2 / n)))
    fill = []
    for (xa, ya), (xb, yb) in (((x0 + rc, y0), (x1 - rc, y0)), ((x0 + rc, y1), (x1 - rc, y1)),
                               ((x0, y0 + rc), (x0, y1 - rc)), ((x1, y0 + rc), (x1, y1 - rc))):   # the straight edges
        m = max(1, int(math.dist((xa, ya), (xb, yb))))
        fill += [(xa + (xb - xa) * j / m, ya + (yb - ya) * j / m) for j in range(m + 1)]
    return pts + fill
def edge_gap(pts, x, y, r):
    return min(math.dist((x, y), q) for q in pts) - r

PEGS = [(17 + 18 * i, 13.5, 7.0) for i in range(15)] + \
       [(8 + 18 * (i + 1), 36.0, 7.0) for i in range(14) if [1, 1, 0, 1, 1, 1, 0][i % 7]]   # felt washers Ø 14
GROUPS = {}
if VARIANT == "P5O":
    GROUPS = {"lid R1": [["RANGE 1", "TUNE", "WAVE 1", "DRIFT"], ["L ATTACK", "L DECAY", "L SUSTAIN"], ["ECHO TYPE", "ECHO TIME", "FREE/SYNC", "ECHO REPEATS"]],
              "lid R2": [["RANGE 2", "FREQ 2", "WAVE 2"], ["F ATTACK"], ["VEL"], ["ECHO PAN"]],
              "lid R3": [["RANGE 3", "FREQ 3", "WAVE 3"], ["F DECAY"], ["AFTERTOUCH"], ["REVERB TYPE", "REVERB DECAY"]],
              "lid R4": [["PARA", "OSC MOD", "OSC 3 CTL"], ["F SUSTAIN"], ["DRY PAN", "FOLLOW"]]}
elif VARIANT == "P5R":
    GROUPS = {"lid A": [["RANGE 1", "WAVE 1"], ["RANGE 2", "FREQ 2", "WAVE 2"], ["RANGE 3", "FREQ 3", "WAVE 3"], ["TUNE", "DRIFT"]],
              "lid B": [["VEL"], ["F ATTACK", "F DECAY", "F SUSTAIN"], ["L ATTACK", "L DECAY", "L SUSTAIN"], ["DRY PAN"]],
              "lid C": [["ECHO TYPE", "ECHO TIME", "FREE/SYNC", "ECHO REPEATS", "ECHO PAN"], ["REVERB TYPE", "REVERB DECAY"]]}
if STEER5:
    GROUPS.update({"base front": [["BEND stick", "MOD", "MOD MIX", "GLIDE"], ["EMPHASIS", "KBD CTRL", "CUTOFF", "FILTER MOD", "CONTOUR AMT"], ["VOLUME"], ["TAP"]],
                   "base rear": [["RELEASE"], ["OSC 1", "OSC 2", "OSC 3", "NOISE/EXT", "SOURCE"], ["ECHO MIX", "REVERB MIX"]]})
SUBGROUP_OK = {("RANGE 1", "RANGE 2"), ("WAVE 1", "RANGE 2"), ("WAVE 2", "RANGE 3")}   # VCO sub-gutters: 2M clear

def steer5_checks():
    """module rules (M = 5): within a group knob pitch >= 4M; between groups on a row >= 3M clear (VCO sub-groups
    >= 2M); every control >= 3M clear of its plate's edge, corners included (superellipse); rows on multiples of M;
    pegs >= 1.5 and feet >= 1.5 inside the softer outlines; base pots clear of the battery and the Daisy."""
    bad = []
    lid_pts = se_outline(4.3, 0.3, 281.7, D - 4.3, PLATE_RC)
    base_pts = se_outline(4.3, 4.3, 281.7, D - 0.3, PLATE_RC)
    case_pts = se_outline(0.0, 0.0, 286.0, D, CASE_RC)
    bs = {n: (x, y, (7.0 if r == KN else r)) for n, x, y, r, h in base(9.0, 12.6)}
    ls = {n: (x, d, r) for n, x, d, r, *_ in lid}
    for row, groups in GROUPS.items():
        src = bs if row.startswith("base") else ls
        flat = [g for g in groups]
        for g in flat:
            ks = [n for n in g if src[n][2] in (KN, 7.0)]
            for a, b in zip(ks, ks[1:]):
                if abs(src[b][0] - src[a][0]) < 4 * M - 1e-6: bad.append(f"MODULE pitch {a}/{b} {abs(src[b][0] - src[a][0]):.2f}")
        for g, h in zip(flat, flat[1:]):
            a, b = g[-1], h[0]
            clear = abs(src[b][0] - src[a][0]) - src[a][2] - src[b][2]
            need = 2 * M if (a, b) in SUBGROUP_OK else 3 * M
            if clear < need - 0.05: bad.append(f"MODULE gutter {a} | {b} {clear:.2f} < {need:.0f}")
    for n, (x, d, r) in ls.items():
        if edge_gap(lid_pts, x, d, r) < 3 * M - 0.05: bad.append(f"MARGIN lid {n} {edge_gap(lid_pts, x, d, r):.2f}")
    for n, (x, y, r) in bs.items():
        if edge_gap(base_pts, x, y, r) < 3 * M - 0.05: bad.append(f"MARGIN base {n} {edge_gap(base_pts, x, y, r):.2f}")
    for x, y, r in PEGS:
        if edge_gap(base_pts, x, y, r) < 1.5: bad.append(f"PEG ({x}, {y}) {edge_gap(base_pts, x, y, r):.2f}")
    for x, y in ((16, 12), (270, 12), (16, D - 12), (270, D - 12)):
        if edge_gap(case_pts, x, y, 6.0) < 1.5: bad.append(f"FOOT ({x}, {y}) {edge_gap(case_pts, x, y, 6.0):.2f}")
    rows = sorted({round(d, 2) for n, x, d, r, k, *_ in lid if k == "k"})
    for a, b in zip(rows, rows[1:]):
        if abs((b - a) / M - round((b - a) / M)) > 0.01: bad.append(f"ROW pitch {a} -> {b} not a multiple of M")
    for n, (x, y, r) in bs.items():                                 # 9 mm pots / toggles: body ≈ 10 × 10 under the plate
        for nm, (x0, y0, x1, y1) in (("battery", BATTERY), ("Daisy", DAISY)):
            if x0 - 5 < x < x1 + 5 and y0 - 5 < y < y1 + 5: bad.append(f"UNDER {n} over the {nm}")
    return bad

def max_corner():
    """the largest plate corner (superellipse, n = SE_N) for which every steer-5 check still passes."""
    global PLATE_RC, CASE_RC
    keep = PLATE_RC; best = None
    for rc in [x / 2 for x in range(16, 81)]:
        PLATE_RC, CASE_RC = rc, rc + 4.3
        if not steer5_checks(): best = rc
        else: break
    PLATE_RC, CASE_RC = keep, keep + 4.3
    return best

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
    return math.dist(frm, (x, D + 6.0 + d))

if __name__ == "__main__":
    v = check() + base_check() + (steer5_checks() if STEER5 else [])
    print(f"variant {VARIANT}: {sum(1 for i in lid if i[4] == 'k')} knobs, {sum(1 for i in lid if i[4] == 't')} toggles")
    print(f"open layout + labels: {len(v)} violations"); [print("  ", x) for x in v]
    print("closed (lid face today z 37.6; closed 52.7):")
    for nm, hk, hs in [("R-TALL: today's knobs (13.5), stick 12.6", 13.5, 12.6),
                       ("R-LOW: Tayda 10 x 8 knobs (seat 1.0 → 9.0), stick as is 12.6", 9.0, 12.6),
                       ("R-LOW: Tayda 10 x 8 (9.0), stick lowered to 9.0", 9.0, 9.0),
                       ("R-LOW: Tayda 10 x 8 with a nut under it (10.5), stick 9.0", 10.5, 9.0)]:
        need, w = closed_need(base(hk, hs))
        print(f"  {nm}: face ≥ {need:.2f} → +{need - 37.6:.1f} → closed ≈ {52.7 + need - 37.6:.1f} mm (binding: {w[0]} over {w[1]})")
    if STEER5:
        print(f"steer 5: D {D}, module {M}; plate corner superellipse n {SE_N}, size {PLATE_RC} (largest that passes: {max_corner()})")
    have = {n for n, *_ in lid}
    print("reach from TAP with the lid standing:", {n: round(reach(n, (261, 68))) for n in ("VOLUME", "ECHO TIME", "FREE/SYNC") if n in have})
    print("reach from CUTOFF:", {n: round(reach(n)) for n in ("ECHO MIX", "REVERB MIX", "F ATTACK", "OSC 1", "L ATTACK", "ECHO TYPE") if n in have})
