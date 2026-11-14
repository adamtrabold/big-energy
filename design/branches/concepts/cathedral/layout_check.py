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
VCO4 = os.environ.get("CATHEDRAL_VCO4", "0") == "1"   # the optional 4th analog VCO (owner question, §19.5): lid + base mixer 4
ML, MR = 4.3 + 3 * M, 281.7 - 3 * M                # the margin lines: 3M inside the plate edges (x 19.3 / 266.7)
GHOST = []     # P5O without VCO 4: the slot's knob outlines (light ink), checked as controls: (name, x, d, r, legend)
NAME_BOX = None  # the name, a light-ink word under the window: (text, x, d, size)
HAIR = []      # engraved hairlines checked as obstacles: (name, x0, d0, x1, d1)
BELOW2_LEAD, BELOW2_TOP = 1.25, 2.25   # under-switch legends (visual rev 9): line gap, block top under the nut
RESERVED = []  # (row, x0, x1): a slot kept for VCO 4, drawn blank; the gap rule counts it as a group

lid = []      # name, x, d, r, kind ('k' knob / 't' toggle), legend, legend placement
BREAKS = []   # engraved group breaks: (x, d_from, d_to), vertical lines
SECTIONS = [] # group headings for the visual: (name, x, d)
NOTES = []    # small free legends: (text, x, d, size, anchor left/center/right)
SECTIONS_LEFT = []  # P5O (steer 5 score 8 fix 2): every heading top-left of its group: (name, x of its left edge, d);
                    # SECTIONS carries the same headings as centres (estimated width) for the checks
SUBHEADS = [] # sub-heads under a heading: (text, x, d), Kalam SUB_S
DOTS = []     # link dots (Ø 1.2): (name, x, d, paired control)
def L(n, x, d, k, lab, where): lid.append((n, x, d, KN if k == "k" else TGL, k, lab, where))

if VARIANT == "P5O":
    # ---- steer 5, score-8 fixes. Columns, left to right: oscillator block | filter column | window | amp column
    # (filter's mirror about x 143) | echo -> reverb -> out on the right. One heading rule panel-wide: every heading
    # sits top-left of its group. Rows 104 / 79 / 49 / 24; attack and decay symmetric about the window (d 64 ± 15).
    # Every VCO reads octave · wave · pitch; VCO 1 has no pitch knob (master tune is its pitch), so on R1 VCO 1 is
    # followed by its own "tuning" pair (tune · drift), then the oscillator switches, then echo, at equal gutters.
    # Column legends (filter, amp, right block below R1) sit in front of their knobs, so the column headings clear R1.
    R1, R2, R3, R4 = 104.0, 79.0, 49.0, 24.0
    G = 4 * M
    C1 = ML + KN; OX = (C1, C1 + 20, C1 + 40)                       # octave · wave · pitch columns
    FX5 = OX[2] + KN + G + KN; AX5 = 286.0 - FX5                    # filter 101.65 / amp 184.35 (mirror)
    RC = AX5 + KN + G + KN; RX = (RC, RC + 20, RC + 40)             # right block columns 219.25 / 239.25 / 259.25
    NUMX = C1 - 9.9                                                 # VCO numerals hang in the margin (visual rev 9)
    for n, x, d, lab in [("RANGE 1", OX[0], R1, "octave"), ("WAVE 1", OX[1], R1, "wave"),
                         ("RANGE 2", OX[0], R2, "octave"), ("WAVE 2", OX[1], R2, "wave"), ("FREQ 2", OX[2], R2, "pitch"),
                         ("RANGE 3", OX[0], R3, "octave"), ("WAVE 3", OX[1], R3, "wave"), ("FREQ 3", OX[2], R3, "pitch")]:
        L(n, x, d, "k", lab, "behind")
    NOTES += [(t, NUMX, d, NUM_S, "center") for t, d in (("1", R1), ("2", R2), ("3", R3))]
    if VCO4:
        for n, x, lab in [("RANGE 4", OX[0], "octave"), ("WAVE 4", OX[1], "wave"), ("FREQ 4", OX[2], "pitch")]:
            L(n, x, R4, "k", lab, "behind")
        NOTES.append(("4", NUMX, R4, NUM_S, "center"))
    else:
        RESERVED.append(("lid R4", OX[0] - KN, OX[2] + KN))
        GHOST += [(n, x, R4, KN, lab) for n, x, lab in (("ghost octave 4", OX[0], "octave"), ("ghost wave 4", OX[1], "wave"),
                                                         ("ghost pitch 4", OX[2], "pitch"))]
        NOTES.append(("4", NUMX, R4, NUM_S, "center"))
    # what VCO 4 costs, for every drawing that shows it (director fix 5); the stick line is this layout's, with or without it
    VCO4_CAPTION = ("VCO 4 (optional, owner's call): ≈ +$20–30, ≈ −0.5 h of battery, the Daisy's last pin. "
                    "P5O lowers the bend stick to 9.0 mm to close at 55.2 (as is: 58.8)")
    # R1: VCO 1 | tuning | oscillator switches | echo (type · time · repeats), equal gutters margin to margin
    BW = 4.6 + 40 + 6.2 + 5.2                                       # switch bank: first nut -> track's "off · on"
    g1 = (MR - ML - (2 * KN + 20) * 3 - BW - 4 * M) / 3              # echo's R1 pair ends one G (4M) short of the margin, as R2-R4
    TX = ML + 2 * KN + 20 + g1 + KN                                  # tune
    BX = TX + 20 + KN + g1 + 4.6                                     # voices
    L("TUNE", TX, R1, "k", "tune", "behind"); L("DRIFT", TX + 20, R1, "k", "drift", "behind")
    L("PARA", BX, R1, "t", "voices|" + ("1 · 2 · 4" if VCO4 else "1 · 3 · 4"), "right2")
    L("OSC MOD", BX + 20, R1, "t", "mod|off · on", "right2"); L("OSC 3 CTL", BX + 40, R1, "t", "track|off · on", "right2")
    for n, d, lab in [("F ATTACK", R2, "attack"), ("F DECAY", R3, "decay"), ("F SUSTAIN", R4, "sustain")]:
        L(n, FX5, d, "k", lab, "front")
    for n, d, lab in [("L ATTACK", R2, "attack"), ("L DECAY", R3, "decay"), ("L SUSTAIN", R4, "sustain")]:
        L(n, AX5, d, "k", lab, "front")
    # keys under the window (R4): names + positions under each switch, one G from each sustain
    VW, TW = len("amp · both · filter") * 0.5 * NS / 2, len("mod · off · filter") * 0.5 * NS / 2
    L("VEL", FX5 + KN + G + VW, R4, "t", "velocity|amp · both · filter", "below2")
    L("AFTERTOUCH", AX5 - KN - G - TW, R4, "t", "touch|mod · off · filter", "below2")
    # right block. echo: R1 type · time, R2 free · sync · repeats · pan (free · sync on the gutter line, where R2's
    # first slot starts, so the type's legend below it doesn't meet a knob legend) -> reverb R3 -> out R4
    L("ECHO TYPE", RX[0], R1, "k", "type", "front"); L("ECHO TIME", RX[1], R1, "k", "time", "behind")
    L("FREE/SYNC", RX[0] - KN + 4.6, R2, "t", "free · sync", "under")
    L("ECHO REPEATS", RX[1], R2, "k", "repeats", "behind"); L("ECHO PAN", RX[2], R2, "k", "pan", "behind")
    L("REVERB TYPE", RX[0], R3, "k", "type", "front"); L("REVERB DECAY", RX[1], R3, "k", "decay", "front")
    L("DRY PAN", RX[0], R4, "k", "pan", "front"); L("FOLLOW", RX[1], R4, "t", "link|off · on", "right2")
    DOTS += [("dot echo pan", RX[2] + 1.75 + 1.55 + 0.6, R2 + KN + 3.5 + BEHIND_EXTRA, "ECHO PAN"),
             ("dot link", RX[1] + 6.2 + 8 * 0.5 * NS + 2.1, R4 + TS_LEAD[0], "FOLLOW")]
    over = lambda d, top_extra=0.0: d + KN + top_extra + 1.5 + 0.425 * HS     # a heading's centre over a row's knob tops
    fan_top = KN + 7.2 + 0.425 * 1.3                                          # a TYPE knob's outer fan names, above its centre
    # visual rev 9.1 real-Kalam fits: filter / amp +0.8 more, keys +0.7, echo +0.5 x, reverb +0.3, out 3.8 into the gutter
    SECTIONS_LEFT += [("oscillators", ML, 120.9), ("tuning", TX - KN, 120.9), ("echo", RX[0] - KN + 0.5, 120.9),
                      ("filter", FX5 - KN, over(R2) + 1.6), ("amp", AX5 - KN, over(R2) + 1.6),
                      ("reverb", RX[0] - KN, R3 + fan_top + 1.5 + 0.425 * HS + 0.3),
                      ("keys", FX5 + KN + G, R4 + 4.6 + 1.5 + 0.425 * HS + 1.0), ("out", RX[0] - KN - 3.8, over(R4))]
    SECTIONS += [(t, x + len(t) * 0.25 * HS, d) for t, x, d in SECTIONS_LEFT]
    # "oscillators" runs on as an engraved hairline (0.4); it stops before "tuning" and restarts over the switches
    # (at voices' nut, visual rev 9.1), so it doesn't read as tuning's leader
    BANK_END = BX + 40 + 6.2 + 8 * 0.5 * NS * 1.25
    HAIR += [("oscillators hairline a", ML + 21.5, 120.9 - 0.2, TX - KN - 2.5, 120.9 + 0.2),
             ("oscillators hairline b", BX - 4.6, 120.9 - 0.2, BANK_END, 120.9 + 0.2)]
    NAME_BOX = ("big energy", 143.0, 37.6, 2.0)                    # rev 9.1: +0.3, keeping 1.5 over "keys"
    FX, FX_BREAKS, SWL = R1, [], R4
    GAP_ROWS = [("lid R1", R1, [["RANGE 1", "WAVE 1"], ["TUNE", "DRIFT"], ["PARA", "OSC MOD", "OSC 3 CTL"],
                                ["ECHO TYPE", "ECHO TIME"]]),
                ("lid R2", R2, [["RANGE 2", "WAVE 2", "FREQ 2"], ["F ATTACK"], "WIN", ["L ATTACK"], ["FREE/SYNC", "ECHO REPEATS", "ECHO PAN"]]),
                ("lid R3", R3, [["RANGE 3", "WAVE 3", "FREQ 3"], ["F DECAY"], "WIN", ["L DECAY"], ["REVERB TYPE", "REVERB DECAY"]]),
                ("lid R4", R4, [["RANGE 4", "WAVE 4", "FREQ 4"] if VCO4 else "RES", ["F SUSTAIN"], ["VEL", "AFTERTOUCH"],
                                ["L SUSTAIN"], ["DRY PAN", "FOLLOW"]])]
elif VARIANT == "P5R":
    # ---- steer 5, score-9 fix 1: the rule in rows. A oscillators (VCO 1 | 2 | 3, each octave · wave · pitch)
    # ‖ tuning, with all three oscillator switches on one line under it (A', d 89: voices under VCO 1, mod under
    # VCO 2, track under VCO 3); B filter | window | amp | keys (a side column); C echo -> reverb -> out.
    # Rows 8M: 104 / 64 / 24. Every row: equal gutters, no empty area wider than one.
    A5, A5s, B5, C5 = 104.0, 89.0, 64.0, 24.0
    BU, BD = 78.0, 50.0                                             # the keys' pair straddles row B
    wA = [2, 3, 3, 2]; gA = (MR - ML - sum(2 * KN + 20 * (k - 1) for k in wA)) / 3
    xs, x0 = [], ML
    for k in wA:
        xs.append([x0 + KN + 20 * i for i in range(k)]); x0 += 2 * KN + 20 * (k - 1) + gA
    for n, x, lab in zip(["RANGE 1", "WAVE 1", "RANGE 2", "WAVE 2", "FREQ 2", "RANGE 3", "WAVE 3", "FREQ 3", "TUNE", "DRIFT"],
                         sum(xs, []), ["octave", "wave", "octave", "wave", "pitch", "octave", "wave", "pitch", "tune", "drift"]):
        L(n, x, A5, "k", lab, "behind")
    NOTES += [(t, g[0] - 9.9, A5, NUM_S, "center") for t, g in zip(("1", "2", "3"), xs)]
    BREAKS.append(((xs[2][-1] + xs[3][0]) / 2, 96.0, 113.0))        # oscillators ‖ tuning
    mid = lambda g: (g[0] + g[-1]) / 2
    L("PARA", mid(xs[0]), A5s, "t", "voices|1 · 3 · 4", "right2")
    L("OSC MOD", mid(xs[1]), A5s, "t", "mod|off · on", "right2")
    L("OSC 3 CTL", mid(xs[2]), A5s, "t", "track|off · on", "right2")
    # row B. The keys' column (names + positions under each switch) ends on the right margin line; amp sits one
    # gutter (= row A's) before it; filter takes the left, with its end and window gaps each within one gutter.
    # (Filter alone on one side, amp + keys on the other: the envelopes can't be centred on the window, 5.9 mm off.)
    G = gA
    KW = len("amp · both · filter") * 0.5 * NS / 2
    KYX = MR - KW
    AXR = KYX - KW - G - KN - 40                                    # amp attack
    left = 120.0 - ML - (2 * KN + 40)                               # the empty run left of the window, end + window gap
    FXR = ML + (left + 0.2) / 2 + KN                                # filter attack (end 0.2 wider than the window gap)
    for n, x, lab in [("F ATTACK", FXR, "attack"), ("F DECAY", FXR + 20, "decay"), ("F SUSTAIN", FXR + 40, "sustain"),
                      ("L ATTACK", AXR, "attack"), ("L DECAY", AXR + 20, "decay"), ("L SUSTAIN", AXR + 40, "sustain")]:
        L(n, x, B5, "k", lab, "behind")
    L("VEL", KYX, BU, "t", "velocity|amp · both · filter", "below2"); L("AFTERTOUCH", KYX, BD, "t", "touch|mod · off · filter", "below2")
    # row C: echo (type · time · free · sync · repeats · pan) | reverb (type · decay) | out (pan · link), equal gaps
    wE = 2 * KN + 75; wR = 2 * KN + 20; wO = KN + 20 + 6.2 + 8 * 0.5 * NS
    gC = (MR - ML - wE - wR - wO) / 2
    EC = ML + KN; RVC = ML + wE + gC + KN; OC = RVC + 20 + KN + gC + KN
    for n, x, lab in [("ECHO TYPE", EC, "type"), ("ECHO TIME", EC + 20, "time"), ("ECHO REPEATS", EC + 55, "repeats"),
                      ("ECHO PAN", EC + 75, "pan"), ("REVERB TYPE", RVC, "type"), ("REVERB DECAY", RVC + 20, "decay"),
                      ("DRY PAN", OC, "pan")]:
        L(n, x, C5, "k", lab, "front")
    L("FREE/SYNC", EC + 40, C5, "t", "free · sync", "under"); L("FOLLOW", OC + 20, C5, "t", "link|off · on", "right2")
    DOTS += [("dot echo pan", EC + 75 + 1.75 + 1.55 + 0.6, C5 - KN - 3.5, "ECHO PAN"),
             ("dot link", OC + 20 + 6.2 + 8 * 0.5 * NS + 2.1, C5 + TS_LEAD[0], "FOLLOW")]
    SECTIONS += [("oscillators", (xs[0][0] + xs[2][-1]) / 2, 120.9), ("tuning", (xs[3][0] + xs[3][1]) / 2, 120.9),
                 ("envelopes", 143.0, 91.8), ("keys", KYX, BU + 4.6 + 1.5 + 0.425 * HS + 1.0),
                 ("echo", ML + wE / 2, 37.5), ("reverb", RVC + 22.0, 37.5), ("out", OC + 10, 37.5)]
    SUBHEADS += [("filter", FXR + 20, 79.5), ("amp", AXR + 20, 79.5)]
    NAME_BOX = ("big energy", 143.0, 34.0, 2.0)
    FX, FX_BREAKS, SWL = C5, [], BD
    GAP_ROWS = [("lid A", A5, [["RANGE 1", "WAVE 1", "PARA"], ["RANGE 2", "WAVE 2", "FREQ 2", "OSC MOD"],
                               ["RANGE 3", "WAVE 3", "FREQ 3", "OSC 3 CTL"], ["TUNE", "DRIFT"]]),
                ("lid B", B5, [["F ATTACK", "F DECAY", "F SUSTAIN"], "WIN", ["L ATTACK", "L DECAY", "L SUSTAIN"], ["VEL", "AFTERTOUCH"]]),
                ("lid C", C5, [["ECHO TYPE", "ECHO TIME", "FREE/SYNC", "ECHO REPEATS", "ECHO PAN"], ["REVERB TYPE", "REVERB DECAY"],
                               ["DRY PAN", "FOLLOW"]])]
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
SLIDE_H = 6.0  # a low slide switch (left / right throw), actuator top above the plate (ESTIMATE, UNVERIFIED part)
BAT_H = 15.0   # base toggle: bat tip above the base plate, mini toggle on a low nut (ESTIMATE, UNVERIFIED part; §18.4)
def base(hk, hstick, hcut=12.15, htap=8.0, hbat=BAT_H):
    """PLAY row, steer 4 (review 4, 5): three groups, hero on the axis, stick <-> TAP mirrored about x 143.
    controllers: BEND 25 · MOD 47 · MOD MIX 67 · GLIDE 87 | filter: EMPHASIS 112.5 · KBD (t) 126.4 · CUTOFF 143 ·
    FILT MOD (t) 159.6 · AMOUNT 173.5 | tune: TUNE 199 · DRIFT 222 ‖ TAP ("echo tap") 261, alone behind a break at x 242.2. EMPHASIS / AMOUNT open out
    6.5 each way (119 -> 112.5, 167 -> 173.5) to seat the two toggles beside CUTOFF (gaps hold for both R-LOW Ø 10 and R-TALL Ø 14.9 knobs)."""
    if STEER5:   # steer 5 score fix (a): two rows, each spread to equal gutters between the margin lines
        return [(n, x, y, r, {"k": hk, "s": hstick, "c": hcut, "p": htap, "t": hbat, "l": SLIDE_H}[h]) for n, x, y, r, h in BASE5]
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
    # ---- the shared base, steer 5 score fix (a). Front y 68 (what the hands ride): controllers (bend · mod · glide)
    # | filter (pinned: CUTOFF under the window) | out (volume) | tempo (tap). Rear y 93 (the levels): controllers'
    # rear (release behind bend, blend behind mod) | mixer (1 2 3 [4] extra, source) | effects | lights.
    # "controllers" heads both rows, so release / bend and blend / mod read as columns.
    BK = 7.0                                       # a low knob with its tick ring
    FL, FR = 112.5 - BK, 173.5 + BK                # the filter group's edges (fixed round CUTOFF 143)
    wO, wT = 2 * BK, 2 * TAPR
    gF = (MR - FR - wO - wT) / 2                   # right of the filter: out, tempo; tempo on the margin line
    wCF = STK + 40 + BK                            # controllers front: stick, mod, glide at 4M
    CX = FL - gF - wCF + STK                       # the same gutter left of the filter; the rest stays in the margin
    nmix = 5 if VCO4 else 4
    SRC = 16.6                                     # source switch beyond "extra": legend half-width 6.5 + nut + 1.5 + knob
    wM = 2 * BK + 20 * (nmix - 1) + SRC + len("noise · input · loop") * 0.5 * NS / 2 - BK
    wFX, wL = 2 * BK + 20, 2 * 2.5 + 10
    RL = CX + 20 + BK                              # controllers' rear right edge (blend)
    gR = (MR - RL - wM - wFX - wL) / 3             # rear: three gutters, lights on the margin line
    MX = RL + gR + BK; EX = MX + 20 * (nmix - 1) + SRC + len("noise · input · loop") * 0.5 * NS / 2 + gR + BK
    LX = MR - 2.5 - 10
    BASE5 = [("BEND stick", CX, 68, STK, "s"), ("MOD", CX + 20, 68, KN, "k"), ("GLIDE", CX + 40, 68, KN, "k"),
             ("EMPHASIS", 112.5, 68, KN, "k"), ("KBD CTRL", 126.4, 68, TGL, "t"), ("CUTOFF", 143, 68, CUT, "c"),
             ("FILTER MOD", 159.6, 68, TGL, "t"), ("CONTOUR AMT", 173.5, 68, KN, "k"),
             ("VOLUME", FR + gF + BK, 68, KN, "k"), ("TAP", MR - TAPR, 68, TAPR, "p"),
             ("RELEASE", CX, 93, TGL, "l"), ("MOD MIX", CX + 20, 93, KN, "k")] + \
            [(f"OSC {i + 1}", MX + 20 * i, 93, KN, "k") for i in range(nmix - 1)] + \
            [("NOISE/EXT", MX + 20 * (nmix - 1), 93, KN, "k"), ("SOURCE", MX + 20 * (nmix - 1) + SRC, 93, TGL, "l"),
             ("ECHO MIX", EX, 93, KN, "k"), ("REVERB MIX", EX + 20, 93, KN, "k")]
    BASE_GAP_ROWS = [("base front", 68, [["BEND stick", "MOD", "GLIDE"], ["EMPHASIS", "KBD CTRL", "CUTOFF", "FILTER MOD", "CONTOUR AMT"],
                                         ["VOLUME"], ["TAP"]]),
                     ("base rear", 93, [["RELEASE", "MOD MIX"], [f"OSC {i + 1}" for i in range(nmix - 1)] + ["NOISE/EXT", "SOURCE"],
                                        ["ECHO MIX", "REVERB MIX"], ["LIGHTS"]])]
if STEER5:
    BASE_TOGGLES = {"KBD CTRL": "track|off · 1/3 · 2/3", "FILTER MOD": "mod|off · on", "RELEASE": "release|off · on",
                    "SOURCE": "source|noise · input · loop"}
    BASE_LEGEND = {"BEND stick": "bend", "MOD": "mod", "MOD MIX": "blend", "GLIDE": "glide", "EMPHASIS": "resonance",
                   "CUTOFF": "cutoff", "CONTOUR AMT": "envelope", "VOLUME": "volume", "TAP": "tap", "OSC 1": "1",
                   "OSC 2": "2", "OSC 3": "3", "OSC 4": "4", "NOISE/EXT": "extra", "ECHO MIX": "echo", "REVERB MIX": "reverb"}
    # headings on top of their groups (left-aligned, Kalam 2.4): the rear row's at y 109 (visual rev 8), with
    # "controllers" heading both rows; the front row's at y 78
    BASE_SECTIONS = [("controllers", CX - TGL, 109.0), ("mixer", MX - BK, 109.0), ("effects", EX - BK, 109.0),
                     ("filter", FL, 78.0), ("out", FR + gF, 78.0), ("tempo", MR - 2 * TAPR, 78.0)]
    BASE_LEDS = [(LX, 93.0, 2.5), (LX + 10, 93.0, 2.5)]
    BASE_NOTES = [("midi", LX, 93.0 + 2.5 + 1.8 + 0.85 * 1.55 / 2), ("status", LX + 10, 93.0 + 2.5 + 1.8 + 0.85 * 1.55 / 2)]
    BASE_BREAKS = []
    BATTERY = (36.0, 100.0, 196.0, 126.0)        # 4 × 952540 end to end (4 × 40), 1S4P, behind the rear row
    DAISY = (199.0, 100.0, 251.0, 126.0)         # Daisy Seed 51 × 18 on its header strip
    # fix (d): the side pivots move inboard of the soft corners. Each pivot is a pair of 4 mm brass leaves on an
    # internal bulkhead just inside where the back wall turns straight (x = case corner), axis y D + 1, z 26.25
    PIVOT_W = 4.0

def base_labels(bs):
    """every base legend as rb draws it (visual rev 8): front row in front of the knob / under the switch; rear row
    (y > 80) behind the knob (y + 10.95) and, for switches, name over positions ABOVE the switch (from y + TGL + 2.35)."""
    labs = []
    for n, x, y, r, h in bs:
        rear = STEER5 and y > 80
        if n in BASE_TOGGLES:
            nm, pos = BASE_TOGGLES[n].split("|")
            if rear:
                hn, hp = 0.85 * SW_LS, 0.85 * NS; w = max(len(nm) * 0.5 * SW_LS, len(pos) * 0.5 * NS); bot = y + TGL + 2.35
                labs.append((n, (x - w / 2, bot, x + w / 2, bot + hp + 0.9 + hn)))
            else:
                labs.append((n, legend2(x, y, nm, pos, "below2")))
            continue
        t = BASE_LEGEND[n]; w, hh = len(t) * 0.5 * LS, 0.85 * LS
        cy = {"BEND stick": y - 11.5, "CUTOFF": y - CUT - 3.5, "TAP": y - TAPR - 3.5}.get(n, y + 10.95 if rear else y - 10.95)
        labs.append((n, (x - w / 2, cy - hh / 2, x + w / 2, cy + hh / 2)))
    return labs

def base_check():
    """the base row in the open layout: gaps (R-TALL radii, the larger), pitch, and every legend as R-LOW draws it
    (knob legends in front, the stick's 11.5 below, toggle name + positions under the toggle, headings at y 85)."""
    bad, bs = [], base(13.5, 12.6)
    for a, b in itertools.combinations(bs, 2):
        dd = math.dist(a[1:3], b[1:3])
        if a[3] == KN and b[3] == KN and dd < 20 - 1e-6: bad.append(f"BASE PITCH {a[0]}/{b[0]}")
        if dd - a[3] - b[3] < 1.5 - 1e-6: bad.append(f"BASE GAP {a[0]}/{b[0]} {dd - a[3] - b[3]:.2f}")
    labs = base_labels(bs)
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
    top = d - TGL - BELOW2_TOP                                      # under the toggle (visual rev 9: 2.25, 1.25 between the lines)
    return (x - w / 2, top - hn - BELOW2_LEAD - hp, x + w / 2, top)

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
    for n, x, d, r, lab in GHOST:                                    # the VCO 4 outlines are controls for every check
        for m, x2, d2, r2, *_ in lid:
            if math.dist((x, d), (x2, d2)) - r - r2 < 1.5 - 1e-6: bad.append(f"GAP {n}/{m}")
    labs = labels() + [(n, (lambda b: (b[0], b[1] + BEHIND_EXTRA, b[2], b[3] + BEHIND_EXTRA))(tbox(x, d, lab, LS, "behind", r)))
                       for n, x, d, r, lab in GHOST] + \
           [(n, (x0, d0, x1, d1)) for n, x0, d0, x1, d1 in HAIR] + \
           ([("name", (NAME_BOX[1] - len(NAME_BOX[0]) * 0.25 * NAME_BOX[3], NAME_BOX[2] - 0.425 * NAME_BOX[3],
                       NAME_BOX[1] + len(NAME_BOX[0]) * 0.25 * NAME_BOX[3], NAME_BOX[2] + 0.425 * NAME_BOX[3]))] if NAME_BOX else []) + \
           [("head " + t, (x - len(t) * 0.5 * HS / 2, d - 0.425 * HS, x + len(t) * 0.5 * HS / 2, d + 0.425 * HS))
                       for t, x, d in SECTIONS] + decor() + note_boxes() + \
           [("sub " + t, (x - len(t) * 0.5 * SUB_S / 2, d - 0.425 * SUB_S, x + len(t) * 0.5 * SUB_S / 2, d + 0.425 * SUB_S))
            for t, x, d in SUBHEADS] + [(n, (x - 0.6, d - 0.6, x + 0.6, d + 0.6)) for n, x, d, _ in DOTS]
    ghost = [(n, x, d, r, "k") for n, x, d, r, lab in GHOST]
    for ln, b in labs:
        for n, x, d, r, k, *_ in list(lid) + ghost:
            if ln == n: continue                                       # a ghost's own legend
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
PLATE_RC = 24.0     # plate corner size: the visual's choice (rev 8); §19.6 gives the largest that fits
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
if STEER5:   # the module checks read the same groups the gap rule spreads
    GROUPS = {row: [g for g in groups if isinstance(g, list)] for row, d, groups in GAP_ROWS + BASE_GAP_ROWS}
    GROUPS = {row: [[n for n in g if n != "LIGHTS"] for g in gs if g != ["LIGHTS"]] for row, gs in GROUPS.items()}
SUBGROUP_OK = {("PARA", "RANGE 2"), ("OSC MOD", "RANGE 3"), ("WAVE 1", "RANGE 2"), ("FREQ 2", "RANGE 3")}   # VCO sub-gutters: 2M clear

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
    return bad + gap_rule() + pivot_check()[0]

def gap_rule(verbose=False):
    """steer 5 fix (e): along every row, the gutters between neighbouring groups are equal (within 1.0) and no
    other empty area (margin line -> first / last group, group -> window, a reserved slot counts as a group) is wider
    than one gutter (+ 0.5). A group's extent is its controls plus their own legends (fans, scales, numerals and
    headings are print around it, not part of it). Returns violations; with verbose, the gutters per row."""
    bad, out = [], []
    ll = {}
    for n, b in labels(): ll.setdefault(n.split(":")[0], []).append(b)
    ls = {n: (x, d, r) for n, x, d, r, *_ in lid}
    bsl = base(9.0, 12.6); bs = {n: (x, y, 7.0 if r == KN else r) for n, x, y, r, h in bsl}
    bl = {}
    for n, b in base_labels(bsl): bl.setdefault(n, []).append(b)
    for row, d, groups in GAP_ROWS + BASE_GAP_ROWS:
        src, lab = (bs, bl) if row.startswith("base") else (ls, ll)
        seq = []
        for g in groups:
            if g == "WIN": seq.append("WIN"); continue
            if g == "RES":
                seq.append(next((x0, x1, []) for r_, x0, x1 in RESERVED if r_ == row)); continue
            if g == ["LIGHTS"]:
                xs = [(x - rr, x + rr) for x, y, rr in BASE_LEDS] + \
                     [(x - len(t) * 0.25 * SW_LS, x + len(t) * 0.25 * SW_LS) for t, x, y in BASE_NOTES]
                seq.append((min(a for a, b in xs), max(b for a, b in xs), [])); continue
            x0 = min(min(src[n][0] - src[n][2], *[b[0] for b in lab.get(n, [])]) for n in g)
            x1 = max(max(src[n][0] + src[n][2], *[b[2] for b in lab.get(n, [])]) for n in g)
            seq.append((x0, x1, g))
        gaps = []                                   # (kind, width)
        real = [q for q in seq if q != "WIN"]
        gaps.append(("end", real[0][0] - ML)); gaps.append(("end", MR - real[-1][1]))
        for a, b in zip(seq, seq[1:]):
            if "WIN" in (a, b):
                grp = b if a == "WIN" else a
                cl = min(math.dist((src[n][0], src[n][1]), WIN[:2]) - src[n][2] - WIN[2] for n in grp[2])
                gaps.append(("win", cl))
            else:
                gaps.append(("gut", b[0] - a[1]))
        gut = [w for k, w in gaps if k == "gut"]
        G = max(gut) if gut else 3 * M
        if gut and max(gut) - min(gut) > 1.0 + 1e-6: bad.append(f"GAP {row}: gutters unequal {min(gut):.2f} .. {max(gut):.2f}")
        for k, w in gaps:
            if k != "gut" and w > G + 0.5 + 1e-6: bad.append(f"GAP {row}: empty {k} {w:.2f} > gutter {G:.2f}")
            if k == "end" and w < -0.05: bad.append(f"GAP {row}: past the margin line by {-w:.2f}")
        out.append(f"{row}: gutters {', '.join(f'{w:.1f}' for w in gut)}; ends {gaps[0][1]:.1f} / {gaps[1][1]:.1f}"
                   + (f"; window {', '.join(f'{w:.1f}' for k, w in gaps if k == 'win')}" if any(k == 'win' for k, w in gaps) else ""))
    return (bad, out) if verbose else bad

def pivot_check():
    """fix (d): each side pivot's leaf pair (PIVOT_W wide, on an internal bulkhead) must sit where the back wall is
    straight, i.e. inboard of the case's soft corner (x >= CASE_RC on the left, mirrored on the right), and clear
    (>= 1.0 in x) of the battery and the Daisy in the rear strip; the stays' pivots (lid end faces, d 30) must sit on
    the straight end wall (d >= CASE_RC)."""
    bad = []
    PIV = [(CASE_RC, CASE_RC + PIVOT_W), (286.0 - CASE_RC - PIVOT_W, 286.0 - CASE_RC)]
    for x0, x1 in PIV:
        for nm, (bx0, by0, bx1, by1) in (("battery", BATTERY), ("Daisy", DAISY)):
            if x1 > bx0 - 1.0 and x0 < bx1 + 1.0: bad.append(f"PIVOT x {x0:.1f}-{x1:.1f} meets the {nm}")
    if STAY_D < CASE_RC: bad.append(f"STAY pivot d {STAY_D} is on the soft corner (straight from d {CASE_RC})")
    return bad, PIV

STAY_D = 34.0          # the stays' pivot on the lid end faces (was d 30; the straight wall now starts at d 28.3)
def stand(Dd=None, stay_reach=59.0, cells_in_base=True, face=40.1):
    """standing at 120°: the push on the top row's knob tip (normal to the panel) that tips the instrument back
    over the stays' rubber tips. branch_check's DIPTYCH model (v1.1 check: 6.9 N vs the recorded 6.8), with
    D and the masses scaled: each half's shell (60 % of its mass, ESTIMATE) grows with its area; cells 90 g."""
    Dd = Dd or D
    AXY, AXZ, ST = Dd + 1.0, 25.0 + (face - 37.6) / 2, math.radians(60)
    def lid_pt(vy, vz): return (AXY + vy * math.cos(ST) - vz * math.sin(ST), AXZ + vy * math.sin(ST) + vz * math.cos(ST))
    k = Dd / 108.0; cells = 0.09
    mb = 0.40 * (0.4 + 0.6 * k); ml = 0.375 * (0.4 + 0.6 * k)
    yb = mb * Dd / 2; lid_cg = lid_pt(Dd / 2 + 1, -8.0)
    if cells_in_base: mb_t, ml_t, yb = mb + cells, ml - cells, yb + cells * (Dd - 19.0)
    else: mb_t, ml_t = mb, ml
    ycg = (yb + ml_t * lid_cg[0]) / (mb_t + ml_t)
    top = max(d for n, x, d, r, kk, *_ in lid) if lid and Dd == D else Dd - 24
    tip = lid_pt(top + 1, (15.1 + 13.5) - AXZ)
    yp = AXY + stay_reach
    m_push = math.cos(math.radians(30)) * tip[1] + math.sin(math.radians(30)) * (tip[0] - yp)
    return (mb_t + ml_t) * 9.81 * (yp - ycg) / m_push

def p5r_vco4():
    """P5R with VCO 4: can row A hold four VCOs (2 + 3 + 3 + 3 knobs) and tuning (2) at 2M sub-gutters and a 3M
    gutter? Returns (needed, available, gutter if tuning leaves row A, row C's gutter with tuning added)."""
    w = lambda k: 2 * KN + 20 * (k - 1)
    need = w(2) + 3 * w(3) + w(2) + 3 * 2 * M + 3 * M
    avail = MR - ML
    g_no_tune = (avail - w(2) - 3 * w(3)) / 3
    wE = 2 * KN + 75; wR = 2 * KN + 20; wO = KN + 20 + 6.2 + 8 * 0.5 * NS
    g_c = (avail - wE - wR - wO - w(2)) / 3
    return need, avail, g_no_tune, g_c

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
        print(f"steer 5: D {D}, module {M}; VCO 4 {'fitted' if VCO4 else 'not fitted (slot kept)'}; plate corner superellipse n {SE_N}, size {PLATE_RC} (largest that passes: {max_corner()})")
        for line in gap_rule(True)[1]: print("  gap rule", line)
        piv = pivot_check()[1]
        print(f"  pivots (leaf pairs) at x {piv[0][0]:.1f}-{piv[0][1]:.1f} / {piv[1][0]:.1f}-{piv[1][1]:.1f}; stays pivot at lid d {STAY_D}")
        print(f"  stand tip threshold: v1.1 model D 108, cells in lid {stand(108.0, cells_in_base=False, face=37.6):.1f} N; "
              f"D 108 cells in base {stand(108.0, face=37.6):.1f} N; D {D:.0f} (stays as today, 59 behind) {stand():.1f} N; "
              f"stays scaled to D (72 behind) {stand(stay_reach=59.0 * D / 108):.1f} N")
        if VARIANT == "P5R":
            nd, av, g1, g2 = p5r_vco4()
            print(f"  P5R + VCO 4: row A needs {nd:.1f} of {av:.1f} mm with tuning (short {nd - av:.1f}); without tuning row A's gutter is {g1:.1f}; tuning on row C makes C's gutters {g2:.1f}")
    have = {n for n, *_ in lid}
    print("reach from TAP with the lid standing:", {n: round(reach(n, (261, 68))) for n in ("VOLUME", "ECHO TIME", "FREE/SYNC") if n in have})
    print("reach from CUTOFF:", {n: round(reach(n)) for n in ("ECHO MIX", "REVERB MIX", "F ATTACK", "OSC 1", "L ATTACK", "ECHO TYPE") if n in have})
