#!/usr/bin/env python3
"""Round 5 sheets (A3, 300 dpi): A look · B real-size top · C construction · D front views (NEW).
python3 sheets_r5.py [hush one-sheet fold105 fold113]"""
import math, os, sys
from sheets import img, para, write, OUT, ROOT
from drawings import t, rect, line, circ, dim_h, dim_v, INK, MUTE, ACC, PAPER
from sheets_r4 import Sec, rounded_profile, knob_sec, pot_sec, GREEN, FELTC, SHELL, WAL, PGC, BLK, CREAMK, PCRM, PLY, POT, STEEL, BRASS
import r5

RND = 5
FOOT_TAG = "Round 5 · S2 · drawn to systems round-5 final + DRIFT + pre-build fixes (common 7.3, fold 5.6) + 120° stand (fold 5.7) + bend joystick · name to come"
FLAG = "#7a3f8f"

def head(title, kind, idea, page):
    s = [rect(0, 0, 420, 297, PAPER, "none", 0)]
    s.append(t(12, 17, title, 9.5, INK, weight="bold"))
    s.append(t(12, 24.5, kind, 3.4, ACC, weight="bold"))
    s.append(t(408, 17, f"concept mocks, round {RND} · name to come", 3.2, MUTE, "end"))
    s.append(t(408, 23, page, 3.0, MUTE, "end"))
    body, _ = para(12, 31.5, idea, 190, 3.2, fill=INK, style="italic", family="DejaVu Serif")
    s.append(body)
    s.append(line(12, 37.5, 408, 37.5, "#d8d0c2", 0.3))
    return s

def foot(s):
    s.append(t(408, 293, FOOT_TAG, 2.0, MUTE, "end"))

# ================================================================== content
FX_SENT = "Effects (owner: echo + reverb, digital, great models, more than one type; full 8): amounts in front, kinds and times behind. A separate AFTERTOUCH toggle (owner; destination likely VIB / OFF / FILT, eng confirming) sits in the VELOCITY column, between the voice rows, mirrored by the PARA toggle (MONO / PARA / PARA+4) in the oscillator switch column (systems 7.3). PLAY row right: REPEATS, ECHO MIX, REVERB MIX, TAP. The back row is the chain in one line: DRIFT | ECHO: TYPE (tape / bbd / clean / ping-pong), TIME | REVERB: DECAY, TYPE (plate / hall / spring / shimmer) | VOLUME, short legends under each section heading. DRIFT (owner: controllable) is a firmware pitch wander; fully left = rock steady."

H = dict(
    folder="hush", title="HUSH", key="hu",
    kind="a material · sauce · printed pebble shell, one wool-felt skin · unibody, shut from below",
    idea="The material that makes it quiet is the whole outside: one seamless skin of grey wool felt blocked over a soft printed pebble, maple pegs rising through it, and every screw underneath.",
    main="r5_hu_main.png",
    main_caption=f"290 × {r5.HU_D:.0f}, key edge A (drawn). The layout is one balanced plan: three columns (PITCH · FILTER · FX & OUT in front, OSCILLATORS · MIXER · CONTOURS behind), mirrored about the centre, with the back row (drift → echo → reverb → volume) behind the voice, set off by its own pressed rules. TAP ends the PLAY row as a maple peg on its own felt collar, beside the keys: tapped like a key, so it is one.",
    edges=("r5_hu_edgeA.png", "r5_hu_edgeB.png"),
    edge_caps=("A · keys at the edge: the front round-over tightens to r 4; pegs move 6 forward (whites y 13.5). 7 mm of felt in front of the heads.",
               "B · small lip: the round-4 r 12 felt brow in front (13 mm deep, flush at 25.5); pegs at y 19.5."),
    principles=[
        ("One skin, no edges.", "a soft object has nothing to catch or pick at: the shell is rounded so a wool hood can be steam-blocked over it, and the felt ends only underneath."),
        ("The skin is a working part.", "if felt makes it quiet, the felt you see must work: each maple peg lands on its own punched felt collar, the silent stop."),
        ("Nothing hard touches the hand except what plays.", "pegs, knobs, stick and TAP are hard; everything else is wool. TAP is tapped like a key, so it is a key: a maple peg."),
        ("Nothing shouts; even the words are pressed.", "names, rules and the jack legend are blind-pressed with a hot brass die; the fine scales and the type names live on printed tags."),
        ("Shut from below.", "the top carries only what you play; the binding ring and the back panel screw on underneath, and opening the back never releases the skin."),
    ],
    facts=[
        ("ENCLOSURE", "≈ $30–55 (systems ESTIMATE); the felt is most of it. FX adds board, not enclosure cost."),
        ("SIZE", f"290 × {r5.HU_D:.0f} × 25.5 felt; peg heads ≈ 32, knob tops ≈ 36, CUTOFF ≈ 37.6 (cream KN1250)."),
        ("KEYS", "25 ½-in maple pegs on Choc V2 silent, 6.5 proud of the felt by mechanism (2.5 travel to the collar + a ≈ 4 mm head). Edge A or B: sheet D."),
        ("EFFECTS", "8 FX controls + DRIFT, each on its own tag; TYPE rotaries 4-way with the type names on the tag. TAP: a peg at the end of the PLAY row."),
        ("UNIBODY", "One closed-top shell loaded from below; 10 + 8 screws underneath; battery under the main board."),
        ("TO TEST", "Steam-blocking over the shell (systems' corner test), now including the r 4 front edge of option A."),
    ],
    foot="Knobs: cream KN1250 on round-shaft A-5518 pots (visual round 4; systems hasn't ruled yet); CUTOFF cream 1083. TYPE rotaries: RS16211 under a cream KN1250, body height UNVERIFIED (eng). TAP: a 12 mm momentary under a maple peg (part UNVERIFIED). " + FX_SENT,
)

O = dict(
    folder="one-sheet", title="ONE SHEET", key="os",
    kind="an economy · designed for use · one printed shell, one filament · unibody, opened from below",
    idea="One closed shell, printed face down in one filament with one swap. The face has only two finishes: still, and rippled where something turns.",
    main="r5_os_main.png",
    main_caption="276 × 180, key edge A (drawn). Two finishes only (owner): smooth everywhere, and concentric first-layer rings round every rotary control, including the two TYPE switches, DRIFT and VOLUME (rings drawn 2.5× coarse). TAP, the toggles and the lights sit on smooth: they don't turn. Sections read by the sunk grooves and the dark names.",
    edges=("r5_os_edgeA.png", "r5_os_edgeB.png"),
    edge_caps=("A · keys at the edge: skirted key tops run to the front; the wall under them drops to z 17.5, leaving a 4 mm shadow slot.",
               "B · small lip: a 2.4 mm wall rises to z 25.5 (R 1.2), 1 mm below the white tops; it guards the key fronts in a bag."),
    principles=[
        ("One face.", "in an economy you don't add a line the drawing doesn't already have: one closed top; if the bed forces a split, it hides in a break groove."),
        ("Still water, ripples where it turns.", "two finishes, both free from the nozzle: the plain first layer, and concentric rings round every rotary (r 9.25; CUTOFF 12.5). A control that turns gets a ripple; a control you press or flick doesn't."),
        ("Face down on smooth steel.", "the first layer is FDM's best surface, and smooth PEI shows ring sheen. Layer lines stay inside."),
        ("One filament, one swap.", "legends and section names are cut-outs in the first 0.6 mm, filled dark by one change."),
        ("Opened from behind.", "every screw is underneath, one M3 size into brass inserts, so the face stays whole and reprintable."),
    ],
    facts=[
        ("ENCLOSURE", "≈ $10–13 (systems ESTIMATE). The finish adds $0. Still the cheapest."),
        ("SIZE", "276 × 180 × 24; white keys 26.5 (2.5 proud), sharps 28.5; knob tops ≈ 34.5, CUTOFF ≈ 36.1."),
        ("KEYS", "25 short acrylic tops on Choc V2 silent (button keys, ≈ 3 mm travel, not pivoting levers). Edge A or B: sheet D."),
        ("EFFECTS", "8 FX controls + DRIFT: rippled rotaries, and TAP, a white acrylic cap on smooth at the end of the PLAY row. Type names printed round each TYPE switch."),
        ("UNIBODY", "One shell, top and walls in one; 8 screws underneath; battery bay x 20–150, y 110–176."),
        ("TO TEST", "The coupon is now simpler (director): two patches, smooth and rings, on smooth PEI in raking light."),
    ],
    foot="Knobs: cream KN1250 on round-shaft A-5518 pots (visual round 4; not yet ruled); CUTOFF cream 1083, red line. Rings: concentric bottom-layer infill per region needs a slicer modifier (UNVERIFIED in PrusaSlicer; 'concentric' bottom pattern on a cylinder modifier is the likely route). " + FX_SENT,
)

def fold_content(v):
    Fo = r5.Fold(v)
    ok = v == 105
    open_ = 2 * Fo.D + 2
    return dict(
        folder="fold", title=f"FOLD-{v}", key=f"fo{v}", v=v, Fo=Fo, variant=("" if v == 105 else f"-{v}"),
        kind=("a hinge · designed for use · walnut + white (Proof) · self-protecting · " + ("slim battery, RECOMMENDED" if ok else "big battery, shown to explain why not")),
        idea=("Each half is a hollowed walnut block with a white pickguard dropped in and screwed from behind. The keys' half holds what you play, the lid holds the voice and the effects; three columns and one axis balance it, and it closes into a flat-topped walnut bar."
              if ok else "The same FOLD with the big 22 Wh battery. The cells need a 52 mm window in the lid, so the voice spreads apart and the deck opens to ≈ 260 deep: it fails the ≤ 60 mm rule between the PLAY row and the voice. Drawn honestly, so the trade can be seen."),
        main=f"r5_fo{v}_main.png",
        main_caption=(f"Open, 286 × {open_:.0f} (halves 286 × {Fo.D:.0f}), wood-fill walnut-tone print. Balance, made visible: one set of column rules runs through both pickguards and lines up across the seam; EMPHASIS, the status light, the grille, the back row's centre break and the name all sit on the centre axis, marked by a brass pin on the front rim. PLAY row → voice 54.45 mm ✓."
                      if ok else f"Open, 286 × {open_:.0f} (halves 286 × {Fo.D:.0f}). PLAY row → voice front row 75.45 mm ✗ (director's limit ≈ 60): the wide cream band between them is the battery's window, under the plate. The layout, the axis and the columns are identical to FOLD-105; only the depths differ."),
        second=("r5_fo105_closed_wal.png" if ok else "r5_fo113_closed.png"),
        second_caption=(f"Closed, 286 × 108 × ≈ 50, in his planed walnut (later), beside a 400-page hardback. The lid's back: 6 brass screws, 4 cork pads, 2 push-out holes."
                        if ok else f"Closed, 286 × 129 × ≈ 50: 21 mm deeper than FOLD-105, for twice the runtime (≈ 9 h vs ≈ 4.5 h at 2 W, eng ESTIMATE)."),
        principles=[
            ("Block and pickguard.", "it's the owner's guitar: one solid body per half, rounded edges, flat top and bottom; one white plate carries everything, drops in and is screwed from behind."),
            ("The swap draws the pickguard's line.", "the plate prints face down, white for 1.0 mm, then black: a 45° bevel on every edge shows a white band over a black line, for $0."),
            ("Three columns and one axis.", "the owner felt it wasn't balanced: every row mirrors about x 143, the same two rules divide both halves (source → shape → output), and everything single sits on the axis. The rigging trick: the centreline is marked, so the eye has a datum."),
            ("Amounts under the hand, kinds behind.", "the base row is what you do during a note (REPEATS, the two FX mixes and TAP, which mirrors the bend stick); the lid holds the voice, and its back row runs the chain: drift, echo, reverb, volume."),
            ("Open flat, closed a bar.", "open, the lid lies flat at 180° with nothing raised; closed, a walnut bar that guards its own knobs. No case."),
        ],
        facts=[
            ("ENCLOSURE", "≈ $20–26 printed (systems ESTIMATE). Battery " + ("4 × 952540, 11.1 Wh, ≈ 4.5 h at 2 W." if ok else "2 × 50 × 60 pouch, 22.2 Wh, ≈ 9 h at 2 W.")),
            ("SIZE", f"Halves 286 × {Fo.D:.0f}; open {open_:.0f} deep; closed ≈ 50.1. Key front → back row {Fo.D + Fo.dFX:.1f}."),
            ("GAP", "PLAY → voice " + ("54.45 ✓" if ok else "75.45 ✗") + f"; voice rows {Fo.dV2 - Fo.dV1:.1f} apart (the band holds the grille; cells under it)."),
            ("KEYS", "25 short acrylic tops, 1.9 above the plate behind a 4 mm flush rim (= option B). See sheet D."),
            ("EFFECTS", "REPEATS, ECHO MIX, REVERB MIX, TAP in the base; DRIFT | echo: type, time | reverb: decay, type | VOLUME on the lid. PARA | AFTERTOUCH toggles at d 26. Daisy Seed in the base, rear right (sheet C). Lid also stands at 120° (sheet E). BEND is a spring-to-centre joystick (sheet B)."),
            ("THE OWNER'S HAND", "A blank name lozenge on the axis behind the back row. The walnut is his to plane."),
        ],
        foot="Knobs: black 18T push-on (Tayda, 14.5 × 13.5, white line) on A-5622 T18 pots; CUTOFF red 1083 on a round-shaft A-5518. TYPE rotaries RS16211 under black 18T (height UNVERIFIED). TAP: 12 mm momentary, cream cap on a black bezel (UNVERIFIED part). " + FX_SENT,
    )

CONTENT = {"hush": H, "one-sheet": O, "fold105": fold_content(105), "fold113": fold_content(113)}

# ================================================================== insets (sheet A)
def inset_hush(x, y, w, h):
    s = [rect(x, y, w, h, "#ece7de", "#d8d0c2", 0.25)]
    i, b = img(os.path.join(OUT, "r5_hu_under.png"), x + 1, y + 1, 95, h - 2)
    s.append(i)
    p, _ = para(x + 100, y + 6, "UNDERNEATH: the felt turns under the r 6 edge and ends 15 mm in, clamped by a printed binding ring (10 × M3). The back panel sits inside the ring on its own 8 × M3, with feet, the speaker grille and the keyhole. Opening the back never releases the felt.", 72, 2.15)
    s.append(p)
    p, _ = para(x + 100, y + 22, "TYPE TAGS: felt can't hold a fine mark, so each TYPE switch's tag grows a small bib behind the knob that carries the four type names, each over its detent. Same print, same swap.", 72, 2.15, fill="#4a443d")
    s.append(p)
    return "\n".join(s)

def inset_rings(x, y, w, h):
    s = [rect(x, y, w, h, "#ece7de", "#d8d0c2", 0.25)]
    def sw(sx, sy, sz, pitch, ring, label, knob=False):
        g = [f'<clipPath id="r{int(sx*10)}{int(sy)}"><rect x="{sx}" y="{sy}" width="{sz}" height="{sz}"/></clipPath>',
             f'<g clip-path="url(#r{int(sx*10)}{int(sy)})">', rect(sx, sy, sz, sz, "#ece2ca", "none", 0)]
        if ring:
            cx, cy = sx + sz / 2, sy + sz / 2
            rr = 7.75 * sz / 24 if knob else 0.5
            r1 = 9.25 * sz / 24 if knob else sz
            while rr < r1:
                g.append(circ(cx, cy, rr, "none", "#cdbd9c", pitch * 0.42)); rr += pitch
            if knob:
                g.append(circ(cx, cy, 7.25 * sz / 24, "#efe5cb", "#b9ab90", 0.2))
        g.append("</g>"); g.append(rect(sx, sy, sz, sz, "none", "#b9ab90", 0.2))
        g.append(t(sx, sy + sz + 3, label, 1.9, INK))
        return "\n".join(g)
    s.append(t(x + 2, y + 4.5, "THE ONLY TWO FINISHES", 2.1, ACC, weight="bold"))
    s.append(sw(x + 2, y + 6.5, 18, 1.1, False, "smooth (still)"))
    s.append(sw(x + 23, y + 6.5, 18, 1.1, True, "rings, drawn 1.1 pitch"))
    s.append(sw(x + 44, y + 6.5, 18, 0.45 * 18 / 24, True, "round a knob, 24 mm field", knob=True))
    s.append(t(x + 68, y + 4.5, "TRUE SCALE (0.45 mm, a 0.4 nozzle)", 2.1, ACC, weight="bold"))
    s.append(sw(x + 68, y + 6.5, 18, 0.45, True, "rings at 1:1"))
    s.append(sw(x + 89, y + 6.5, 18, 0.45, False, "smooth at 1:1"))
    p, _ = para(x + 112, y + 6, "The ±45° per-section sheen of round 4 is retired (owner: \"only use no texture and that texture\"). Rings go round every rotary: knobs, CUTOFF (r 12.5) and both 4-way TYPE switches, outer r 9.25 at 20 pitch, leaving 1.5 mm of smooth between neighbours and ≈ 2 mm showing past each skirt. The rule is one sentence: if it turns, it ripples. TAP, toggles, lights, the key-window border and the rear band are smooth. Coupon: two patches, still not printed.", 64, 2.0)
    s.append(p)
    return "\n".join(s)

def inset_fold(c):
    def f(x, y, w, h):
        s = [rect(x, y, w, h, "#ece7de", "#d8d0c2", 0.25)]
        # balance diagram: three columns + axis, base and lid
        Fo = c["Fo"]; D = Fo.D; OP = 2 * D + 2
        sc = (h - 6) / OP; ox, oy = x + 8, y + h - 3
        X = lambda xx: ox + xx * sc; Y = lambda yy: oy - yy * sc
        s.append(rect(X(0), Y(OP), 286 * sc, OP * sc, "#f6f2ea", "#8d6b3c", 0.25))
        s.append(line(X(0), Y(D + 1), X(286), Y(D + 1), "#8d6b3c", 0.25, "0.8 0.5"))
        for xb in r5.F.vb_play:
            s.append(line(X(xb), Y(52), X(xb), Y(OP - 6), "#b9ab90", 0.35))
        s.append(line(X(143), Y(-2), X(143), Y(OP + 2), ACC, 0.3, "1 0.6"))
        R = r5.rows(0)
        for key, yy in (("P", 68), ("V1", Fo.LY0 + Fo.dV1), ("V2", Fo.LY0 + Fo.dV2), ("FX", Fo.LY0 + Fo.dFX)):
            for name, lab, xx, kind, midi, yo in R[key]:
                r = 10.4 if kind == "h" else 2.3 if kind == "t" else 1.5 if kind == "l" else 6 if kind in "bs" else 7.25
                col = "#b3302a" if kind == "h" else "#f4efe4" if kind == "b" else BLK
                s.append(circ(X(xx), Y(yy + yo), r * sc, col, INK, 0.1))
        g0, g1 = Fo.p["grille"]
        s.append(rect(X(118), Y(Fo.LY0 + g1), 50 * sc, (g1 - g0) * sc, "#3b3734", "none", 0))
        s.append(rect(X(4), Y(50.5), 278 * sc, 46 * sc, "#ffffff", "#b9ab90", 0.15))
        s.append(t(X(300), Y(OP) + 2, "BALANCE, AS A DIAGRAM", 2.1, ACC, weight="bold"))
        p, _ = para(X(300), Y(OP) + 6.5, "Red dashes: the axis x 143 (EMPHASIS, status, grille, back-row centre break, name). Grey: the two column rules, the same on both halves. Every row mirrors about the axis (checker: 0.00 mm).", 40, 1.9)
        s.append(p)
        # bevel detail
        S = Sec(x + 205, y + h - 4 + 9.8 * 3.0, 3.0)
        S.R(-4, 9.8, 0, 15.6, WAL, INK, 0.15)
        S.P([(0.3, 13.1), (0.3, 14.0), (0.9, 14.6), (1.9, 15.6), (14, 15.6), (14, 13.1)], BLK, INK, 0.12)
        S.P([(0.9, 14.6), (1.9, 15.6), (14, 15.6), (14, 14.6)], PGC, INK, 0.12)
        S.note(1.4, 15.1, 5, 17.3, "45° bevel: 1.0 white over black", INK, 1.8)
        s.append(S.svg())
        s.append(t(x + 192, y + 4.5, "THE PICKGUARD'S LINE · 3:1", 2.1, ACC, weight="bold"))
        return "\n".join(s)
    return f

# ================================================================== sheet A
def sheet_a(c):
    s = head(c["title"], c["kind"], c["idea"], "sheet A — the look")
    i, box = img(os.path.join(OUT, c["main"]), 10, 41, 262, 146)
    s.append(i)
    cap, _ = para(12, 189.5, c["main_caption"], 205, 2.45, fill=MUTE, style="italic")
    s.append(cap)
    x0 = 280
    if "edges" in c:
        s.append(t(x0, 43, "THE KEY EDGE, BOTH WAYS (owner: \"show me both\")", 2.6, ACC, weight="bold"))
        yy = 45
        for f, cp in zip(c["edges"], c["edge_caps"]):
            i2, b2 = img(os.path.join(OUT, f), x0, yy, 72, 36)
            s.append(i2)
            p, _ = para(x0 + 74, yy + 6, cp, 30, 2.15, fill=MUTE, style="italic")
            s.append(p)
            yy += 37
        yy += 1
    else:
        i2, b2 = img(os.path.join(OUT, c["second"]), x0, 41, 128, 56)
        s.append(i2)
        cap, yy = para(x0, b2[1] + b2[3] + 3, c["second_caption"], 72, 2.3, fill=MUTE, style="italic")
        s.append(cap)
        yy += 1.5
    s.append(t(x0, yy + 2, "PRINCIPLES (each follows from the idea)", 3.0, ACC, weight="bold"))
    yy += 6.5
    for k, (p, because) in enumerate(c["principles"], 1):
        hd, yy = para(x0, yy, f"{k}. {p}", 62, 2.7, weight="bold")
        s.append(hd)
        bc, yy = para(x0 + 3.5, yy, "because " + because, 76, 2.2, fill="#4a443d")
        s.append(bc)
        yy += 0.8
    ins = {"hush": inset_hush, "one-sheet": inset_rings}.get(c["folder"]) or inset_fold(c)
    s.append(ins(12, 200, 262, 34))
    s.append(line(12, 238, 408, 238, "#d8d0c2", 0.3))
    cw = 396 / len(c["facts"])
    for k, (hdr, val) in enumerate(c["facts"]):
        xx = 12 + k * cw
        s.append(t(xx, 244, hdr, 2.6, ACC, weight="bold"))
        v, _ = para(xx, 249, val, int(cw / 1.25), 2.3)
        s.append(v)
    fp, _ = para(12, 276, c["foot"], 275, 2.1, fill=MUTE)
    s.append(fp)
    foot(s)
    return write(s, "mock-A-look" + c.get("variant", ""), os.path.join(ROOT, c["folder"]))

# ================================================================== S2: the bend stick, explained (owner: "is it a snap to center fader or what?")
def _stick_side(cx, py, ang, sc, ink=INK):
    """side view at sc:1. Panel line at py; pivot 6 mm under the panel; stem 3.2; flared cap 10 at the top (z 12.6)."""
    out = []
    a = math.radians(ang)
    px, pz = cx, py + 6 * sc                      # pivot (sheet y grows downward)
    def P(r, off=0.0):                            # point r mm up the stem, off mm across it
        return (px + r * sc * math.sin(a) + off * sc * math.cos(a), pz - r * sc * math.cos(a) + off * sc * math.sin(a))
    out.append(line(cx - 14 * sc, py, cx - 3.75 * sc, py, ink, 0.6))         # panel, cut at the round opening (Ø 7.5)
    out.append(line(cx + 3.75 * sc, py, cx + 14 * sc, py, ink, 0.6))
    out.append(rect(cx - 6 * sc, pz - 1.6 * sc, 12 * sc, 5.6 * sc, "#e4ddd0", MUTE, 0.2, rx=0.8))   # the #2765 body under the panel
    out.append(circ(px, pz, 0.9 * sc, "#ffffff", ink, 0.25))
    x1, y1 = P(0); x2, y2 = P(14.6)
    out.append(line(x1, y1, x2, y2, "#4a4a4f", 3.2 * sc))
    cap = [P(14.2, -4.2), P(14.2, 4.2), P(18.6, 5.0), P(18.6, -5.0)]
    out.append('<polygon points="' + " ".join(f"{u:.2f},{v:.2f}" for u, v in cap) + '" fill="#2f2f33" stroke="none"/>')
    return out

def _arrow(x1, y1, x2, y2, col, sw=0.35):
    a = math.atan2(y2 - y1, x2 - x1); h = 1.4
    tip = f'<polygon points="{x2:.2f},{y2:.2f} {x2 - h*math.cos(a-0.45):.2f},{y2 - h*math.sin(a-0.45):.2f} {x2 - h*math.cos(a+0.45):.2f},{y2 - h*math.sin(a+0.45):.2f}" fill="{col}"/>'
    return line(x1, y1, x2, y2, col, sw) + tip

def stick_callout(x0, y0, upper=True):
    """a 290 x 34 band: what BEND is, in words and three side views (1:1)."""
    s = []
    s.append(t(x0, y0 + 3, "BEND IS A JOYSTICK, NOT A FADER", 3.0, ACC, weight="bold"))
    txt_ = ("A mini thumbstick (Adafruit #2765 class). It tilts, it doesn't slide: push it away to bend up, pull it toward "
            "you to bend down, let go and its spring snaps it back to centre (no bend). A gate under the panel lets it move "
            "on that one axis only, which is why the panel shows two pointers, not four. MOD is the knob beside it: it stays where you leave it.")
    p, _ = para(x0, y0 + 8, txt_, 70, 2.25, fill="#4a443d")
    s.append(p)
    sc, py = 1.0, y0 + 19
    for k, (ang, cap, col) in enumerate([(-22, "pull: bend down", INK), (0, "let go: springs to centre", ACC), (22, "push: bend up", INK)]):
        cx = x0 + 150 + k * 42
        s += _stick_side(cx, py, ang, sc)
        s.append(t(cx, py + 13.0, cap, 2.2, col, "middle", weight="bold"))
    # motion arrows (sheet left = toward the player, right = away; side view from the left end)
    s.append(_arrow(x0 + 150 + 2, y0 + 1.5, x0 + 150 - 9, y0 + 1.5, INK))
    s.append(_arrow(x0 + 234 - 2, y0 + 1.5, x0 + 234 + 9, y0 + 1.5, INK))
    s.append(_arrow(x0 + 150 + 7, y0 + 6.5, x0 + 192 - 9, y0 + 6.5, ACC))
    s.append(_arrow(x0 + 234 - 7, y0 + 6.5, x0 + 192 + 9, y0 + 6.5, ACC))
    s.append(t(x0 + 192, y0 + 1.6, "spring", 1.9, ACC, "middle"))
    s.append(t(x0 + 260, py + 2.0, "← player", 1.9, MUTE))
    s.append(t(x0 + 260, py + 5.0, "side view, 1 : 1", 1.9, MUTE))
    s.append(t(x0 + 260, py + 8.0, "cap Ø 10, 12.6 above", 1.9, MUTE))
    s.append(t(x0 + 260, py + 11.0, "the panel (check in hand)", 1.9, MUTE))
    return "\n".join(s)

# ================================================================== sheet B (1:1)
def sheet_b(c):
    f = c["folder"]
    if f == "fold":
        return sheet_b_fold(c)
    flat = dict(hush=(r5.HU_W, r5.HU_D, r5.HU_DX, "r5_hu_top.png"), **{"one-sheet": (r5.OS_W, r5.OS_D, r5.OS_DX, "r5_os_top.png")})
    W, D, dx, top = flat[f]
    s = head(c["title"], c["kind"], "Real size: print at 100 % on A3. The top view is 1:1, rendered straight down from the same model as sheet A (key edge A shown; B differs only in the front 20 mm, see sheet D).", "sheet B — top view, real size")
    ox, oy = 26, 44
    i, _ = img(os.path.join(OUT, top), ox, oy, W + 4, D + 4, exact=True)
    s.append(i)
    X = lambda x: ox + (x + 2); Y = lambda y: oy + (D + 2 - y)
    s.append(dim_h(X(0), X(W), Y(0) + 6, f"{W:.0f} mm"))
    s.append(dim_v(X(W) + 5, Y(D), Y(0), f"{D:.0f} mm"))
    for yy, lab in [(68, "PLAY 68"), (85.4, "break 85.4"), (100, "VOICE 100"), (123, "VOICE 123"), (146, "back row 146"), (D - 15, "rear band")]:
        s.append(line(X(-8), Y(yy), X(-1), Y(yy), MUTE, 0.2)); s.append(t(X(-8.5), Y(yy) + 0.8, lab, 1.9, MUTE, "end"))
    cx = W / 2
    s.append(line(X(cx), Y(-3), X(cx), Y(-9), ACC, 0.25)); s.append(t(X(cx), Y(-11), f"centre x {cx:.0f}: every row mirrors about it", 2.1, ACC, "middle", weight="bold"))
    s.append(stick_callout(26, Y(-11) + 7))
    xr = 340
    yy = 48
    s.append(t(xr, yy, "PARTS YOU SEE", 3.0, ACC, weight="bold")); yy += 5.5
    parts = ([("Felt skin", "grey wool hood, steam-blocked; names, rules and the jack legend blind-pressed."),
              ("Tags", "light warm-grey print under every knob, toggle and TYPE switch; TYPE tags have a bib carrying the 4 type names."),
              ("Pegs", "25 maple ½-in plugs on felt collars + one more for TAP (end of the PLAY row)."),
              ("Knobs", "cream KN1250 × 31 + MOD (incl. DRIFT); cream 1083 CUTOFF, red line."),
              ("Breaks", "pressed 1 mm rules: x 103.5 / 186.5 (PLAY + VOICE), y 85.4, x 96 / 145 / 194 in the back row."),
              ("Rear band", "pressed jack legend over the rear-wall ports; a blank name line."),
              ("Bend", "a joystick: black thumbstick cap on a round tag printed with its gate ring and two pointers (callout below).")] if f == "hush" else
             [("Shell", "one cream PETG print, face down on smooth PEI; legends dark from one swap at 0.6 mm."),
              ("Finish", "smooth, plus rings round every rotary (drawn 2.5× coarse). Nothing else."),
              ("Grooves", "0.6 × 1.2 sunk: x 96.5 / 179.5 (PLAY + VOICE), y 85.4, x 89 / 138 / 187 in the back row."),
              ("Knobs", "cream KN1250 × 31 + MOD (incl. DRIFT); cream 1083 CUTOFF, red line."),
              ("TAP", "white acrylic 12 mm cap (the key material) on a smooth ring, end of the PLAY row."),
              ("Rear band", "y 154–180: jack legend with ticks over each port; the print's label line."),
              ("Bend", "a joystick: black thumbstick cap on a round white Delrin gate disc, dark gate ring and two pointers (callout below).")])
    for k, v in parts:
        hd, yy = para(xr, yy, k, 32, 2.5, weight="bold"); s.append(hd)
        pv, yy = para(xr, yy, v, 34, 2.2, fill="#4a443d"); s.append(pv); yy += 1.1
    yy += 2
    s.append(t(xr, yy, "FX, SET OUT", 3.0, ACC, weight="bold")); yy += 5.5
    pv, yy = para(xr, yy, "Amounts in front, kinds and times behind. The back row is the chain: DRIFT ↔ VOLUME (source ↔ out), TYPE ↔ TYPE, TIME ↔ DECAY, mirrored about the centre, with ECHO and REVERB headed over their pairs. TAP ends the PLAY row, mirroring the bend stick.", 34, 2.2, fill="#4a443d")
    s.append(pv)
    yy += 3
    s.append(t(xr, yy, "FLAG · PARA LEGEND (systems)", 2.6, FLAG, weight="bold")); yy += 4.5
    pv, yy = para(xr, yy, "The PARA toggle (MONO / PARA / PARA+4) is drawn bare. Its mirror, AFTERTOUCH, has its legend beside it because SOURCE's legend sits above SOURCE; PARA's neighbour is the OSC 2 knob, whose legend takes the same line. There is 2.3 mm between PARA's nut and that legend, and the break rule is 3 mm to its left. The three position words need ≈ 15 mm. Needs a new spot or a smaller set of words.", 34, 2.1, fill=FLAG)
    s.append(pv)
    foot(s)
    return write(s, "mock-B-real-size", os.path.join(ROOT, f))

def sheet_b_fold(c):
    Fo = c["Fo"]; D = Fo.D; OP = 2 * D + 2
    s = [rect(0, 0, 420, 297, PAPER, "none", 0)]
    ox, oy = 14, 8 if OP > 240 else 30
    i, _ = img(os.path.join(OUT, f"r5_fo{c['v']}_top.png"), ox, oy, 290, OP + 4, exact=True)
    s.append(i)
    X = lambda x: ox + (x + 2); Y = lambda y: oy + (OP + 2 - y)
    s.append(dim_v(X(286) + 22, Y(OP), Y(0), f"{OP:.0f}"))
    xr = 342
    s.append(t(xr, 17, c["title"], 9.5, INK, weight="bold"))
    s.append(t(xr, 23, "sheet B — top view, real size (open 180°)", 3.0, MUTE))
    p, yy = para(xr, 30, "Print at 100 % on A3; 1:1, rendered straight down from the same model as sheet A. Front of the instrument at the bottom.", 40, 2.4, style="italic")
    s.append(p); yy += 3
    rowsY = [(68, "PLAY 68"), (D + 1, "seam"), (Fo.LY0 + Fo.dV1, "V1"), (Fo.LY0 + Fo.dV2, "V2"), (Fo.LY0 + Fo.dFX, "back row")]
    for y_, lab in rowsY:
        s.append(line(X(286) + 1, Y(y_), X(286) + 2.5, Y(y_), MUTE, 0.2))
    for y_, lab in rowsY:
        s.append(t(X(286) + 4, Y(y_) + 0.8, f"{lab} {y_:.1f}" if lab not in ("seam",) else f"seam {y_:.0f}", 1.9, MUTE))
    gap = Fo.LY0 + Fo.dV1 - 68 - 2
    s.append(t(xr, yy, "THE NUMBERS", 3.0, ACC, weight="bold")); yy += 5.5
    for k, v in [("Halves", f"286 × {D:.0f}; open 286 × {OP:.0f}; closed ≈ 50.1."),
                 ("PLAY → voice", f"{gap:.2f} mm (centres) " + ("✓ (≤ 60)" if gap <= 60 else "✗ (limit ≈ 60)")),
                 ("Voice rows", f"{Fo.dV2 - Fo.dV1:.1f} apart: the band between holds the centred grille; " + ("4 slim cells under it." if c['v'] == 105 else "two 50 × 60 cells under it force the spread.")),
                 ("Back row", f"DRIFT … VOLUME, 23 behind V2, open y {Fo.LY0 + Fo.dFX:.1f}; closed it lands over the whites, 4.0 clear."),
                 ("Axis x 143", "EMPHASIS, status light, grille, back-row break, name lozenge; brass pin on the front rim, a tick on the far rim."),
                 ("Columns", "rules x 101.5 / 184.5 on both pickguards, aligned across the seam.")]:
        hd, yy = para(xr, yy, k, 32, 2.5, weight="bold"); s.append(hd)
        pv, yy = para(xr, yy, v, 34, 2.2, fill="#4a443d"); s.append(pv); yy += 1.1
    yy += 2
    s.append(t(xr, yy, "PARTS YOU SEE", 3.0, ACC, weight="bold")); yy += 5.5
    for k, v in [("Blocks", "walnut-tone wood-fill PLA (his walnut later); R 12 plan, flat top and bottom."),
                 ("Pickguards", "cream, white 1.0 mm then black; bevelled edges show the line."),
                 ("Knobs", "black 18T × 30 + MOD; red 1083 CUTOFF."),
                 ("TAP", "cream 12 mm cap in a black bezel, end of the PLAY row."),
                 ("Stays", "brass lines in both lid end faces: the 120° stand (sheet E)."),
                 ("Bend", "a joystick, not a fader: black thumbstick cap, gate ring and two pointers on a round well (callout under the plan)."),
                 ("Legends", "black lowercase, Kalam (Proof's hand); one swap.")]:
        hd, yy = para(xr, yy, k, 32, 2.5, weight="bold"); s.append(hd)
        pv, yy = para(xr, yy, v, 34, 2.2, fill="#4a443d"); s.append(pv); yy += 1.1
    s.append(stick_callout(ox + 2, oy + OP + 5))
    foot(s)
    return write(s, "mock-B-real-size" + c["variant"], os.path.join(ROOT, "fold"))

# ================================================================== sheet C (construction)
def sec_flat(S, D, kind, edge="A"):
    rowsy = (68, 100, 123, 146)
    if kind == "hush":
        FT = 25.5
        S.P(rounded_profile(0, D, FT, 12, 6), FELTC, INK, 0.2)
        S.P(rounded_profile(2, D - 2, FT - 2, 10, 4), SHELL, INK, 0.15)
        S.P(rounded_profile(4.4, D - 4.4, FT - 4.5, 7.6, 1.6), "#f7f4ee", INK, 0.12)
        S.R(4.4, -0.05, D - 4.4, 3.0, "#f7f4ee", "none", 0)
        S.R(3, -0.05, 17, 1.4, FELTC, INK, 0.12); S.R(D - 17, -0.05, D - 3, 1.4, FELTC, INK, 0.12)
        S.R(4, -1.6, 20, 0.0, "#8a8682", INK, 0.12); S.R(D - 20, -1.6, D - 4, 0.0, "#8a8682", INK, 0.12)
        S.R(20.4, -1.2, D - 20.4, 1.8, "#a39e97", INK, 0.12)
        for y in (12, D - 12): S.screw_up(y, -3.2, 5.0, STEEL)
        for y in (28, D - 28): S.screw_up(y, -2.8, 6.0, "#6f7378")
        S.R(8, 7, 56, 8.6, GREEN, INK, 0.12)
        for yc, top in ((19.5, 32.0), (42, 33.3)):
            S.R(yc - 3.5, 8.6, yc + 3.5, 14.5, "#3a3a3a", INK, 0.1)
            S.R(yc - 1.8, 14.5, yc + 1.8, top - 3, "#c9a06c", INK, 0.1)
            S.P([(yc - 6.35, top - 3.5), (yc + 6.35, top - 3.5), (yc + 5.5, top - 0.6), (yc, top), (yc - 5.5, top - 0.6)], "#e3c493", INK, 0.12)
        S.R(58, 12.4, D - 9, 14.0, GREEN, INK, 0.12)
        for yk in rowsy:
            hero = yk == 68
            pot_sec(S, yk, 14.0, FT + 2.0)
            S.R(yk - (12.4 if hero else 9.6), FT - 1.0, yk + (12.4 if hero else 9.6), FT + 0.06, "#d8d3c9", INK, 0.1)
            knob_sec(S, yk, FT + 0.56, d=20.8 if hero else 14.86, h=12.15 if hero else 10.45)
        S.R(116, 1.5, 180, 11.0, "#5d6a7a", INK, 0.1, dash="0.8 0.6", op=0.35)
        return FT
    Z = 24.0
    S.P([(0, 0), (D, 0), (D, Z - 2), (D - 2, Z), (49.5, Z), (49.5, Z - 2.5), (D - 2.4, Z - 2.5), (D - 2.4, 0.6), (2.4, 0.6), (2.4, 17.5), (0, 17.5)], PCRM, INK, 0.15)
    S.R(2.6, 0, D - 2.6, 3.0, PLY, INK, 0.12)
    for y in (7, D - 7): S.screw_up(y, -1.6, 7.5, STEEL)
    S.R(18, -6, 30, 0, "#2a2a2a", INK, 0.1); S.R(D - 30, -6, D - 18, 0, "#2a2a2a", INK, 0.1)
    S.R(3, 15.1, 50, 16.7, GREEN, INK, 0.12)
    S.P([(0.3, 21.5), (0.3, 26.5), (33, 26.5), (33, 23.5), (1.9, 23.5), (1.9, 21.5)], "#f6f3ec", INK, 0.12)
    S.R(35, 25.5, 49, 28.5, "#3b3734", INK, 0.12)
    for yc, zt in ((18, 23.5), (42, 25.5)):
        S.R(yc - 3.5, 16.7, yc + 3.5, 20.0, "#3a3a3a", INK, 0.1)
        S.R(yc - 1.2, 20.0, yc + 1.2, zt, "#c94a3a", INK, 0.08)
    S.R(52, 12.9, D - 6, 14.5, GREEN, INK, 0.12)
    for yk in rowsy:
        pot_sec(S, yk, 14.5, 26.5)
        knob_sec(S, yk, Z + 0.5, d=20.8 if yk == 68 else 14.86, h=12.15 if yk == 68 else 10.45)
    S.R(110, 1.5, 176, 11.0, "#5d6a7a", INK, 0.1, dash="0.8 0.6", op=0.35)
    for y in (60, 111.5, 160):
        S.R(y - 3, 14.5, y + 3, Z - 2.5, "#d9cdb2", INK, 0.1)
    return Z

def sheet_c_flat(c):
    kind = "hush" if c["folder"] == "hush" else "os"
    s = head(c["title"], c["kind"], "How it's built: one closed-top body loaded from underneath, then a panel screwed on from behind. Section front-to-back near the centre column (knobs of all four rows projected); key edge A.", "sheet C — construction")
    D = r5.HU_D if kind == "hush" else r5.OS_D
    sc = 1.42
    S = Sec(22, 128, sc)
    FT = sec_flat(S, D, kind)
    S.s.append(dim_h(S.X(0), S.X(D), S.Z(-9), f"{D:.0f} mm deep"))
    S.s.append(dim_v(S.X(D) + 6, S.Z(FT), S.Z(0), f"{FT} body"))
    for yk, lab in ((68, "PLAY"), (100, "V1"), (123, "V2"), (146, "BACK")):
        S.s.append(t(S.X(yk), S.Z(44), lab, 2.0, MUTE, "middle"))
    if kind == "hush":
        S.note(1, 16, 0, 46, "felt skin ≈ 2 mm over every edge (front r 4 in option A)", INK, 2.0)
        S.note(42, 33, 50, 52, "maple peg on its felt collar: the silent stop", INK, 2.0)
        S.note(160, 13.5, 160, -17, "main board ≈ 268 × 122 (ESTIMATE; Daisy Seed on board), screwed UP to 10 bosses", INK, 2.0, "end")
        S.note(12, -3, 12, -24, "binding ring: 10 × M3 clamp the felt's turn-in", INK, 2.0)
        S.note(D - 28, -2.5, D - 4, -31, "back panel inside the ring: 8 × M3", INK, 2.0, "end")
        S.note(130, 4, 110, -31, "battery bay under the board", INK, 2.0, "end")
    else:
        S.note(1, 19, 0, 46, "option A: wall at 17.5, a 4 mm shadow slot, the key's skirt", INK, 2.0)
        S.note(30, 26.5, 34, 52, "white tops 26.5: 2.5 proud of the face (strip C on 2.5 taller spacers)", INK, 2.0)
        S.note(111.5, 18, 120, 40, "printed boss + M3 insert", INK, 2.0)
        S.note(160, 13.8, 160, -17, "main board ≈ 268 × 122 (ESTIMATE; Daisy Seed on board): pots pulled up to the face", INK, 2.0, "end")
        S.note(7, -1, 7, -24, "8 × M3 from below", INK, 2.0)
        S.note(140, 4, 120, -31, "battery bay x 20–150, y 110–176", INK, 2.0, "end")
    s.append(S.svg())
    s.append(t(22, 47, f"SECTION · {sc}:1 · front of the instrument on the left", 3.0, INK, weight="bold"))
    i, b = img(os.path.join(OUT, "r5_hu_under.png" if kind == "hush" else "r5_os_under.png"), 296, 44, 112, 66)
    s.append(i)
    s.append(t(296, 116, "Every screw is on this face.", 2.4, MUTE, style="italic"))
    steps = ([
        "Print the shell (2 halves split at x 129.5: the felt hides the joint) and the binding ring.",
        "Steam-block the felt hood over a sacrificial copy of the shell or the shell itself, whichever the corner test allows; dry; trim.",
        "Punch the holes from inside using the shell's own holes. Press the names, rules and the jack legend.",
        "Fit the collars (26: keys + TAP); screw on the binding ring.",
        "Load from below: gate, main board (10 × M3 up), strip C, I/O board, speaker and battery on the back panel.",
        "Back panel on. Flip. Tags, pegs, knobs and stick cap go on from above, last.",
    ] if kind == "hush" else [
        "Print the shell face down on smooth PEI with the ring modifiers; one swap at 0.6 mm.",
        "Press in ≈ 25 heat-set inserts.",
        "Shell face down on a towel; gate plate into its pocket.",
        "Main board in (10 × M3 up); strip C on 4 bosses on the taller spacers; I/O board on the rear wall.",
        "Battery and speaker on the back panel; back panel on (8 × M3).",
        "Flip. Key tops, TAP cap, knobs and the stick cap go on from above.",
    ])
    yy = 124
    s.append(t(296, yy, "BUILD ORDER (F9)", 3.0, ACC, weight="bold")); yy += 5.5
    for k, st in enumerate(steps, 1):
        p, yy = para(296, yy, f"{k}. {st}", 52, 2.3); s.append(p); yy += 1.0
    yy += 2
    s.append(t(296, yy, "WHAT CHANGED SINCE ROUND 4", 3.0, ACC, weight="bold"))
    p, yy = para(296, yy + 5.5, f"{D:.0f} deep (was {176 if kind == 'hush' else 170}): the back row and the digital FX grow the back only. Keys up 2.5. The front edge has two options (sheet D). DRIFT added; VOLUME back on the face, at the end of the back row; TAP at the end of the PLAY row; no wall wheel, no wall toggle.", 52, 2.3)
    s.append(p)
    # detail: the FX row on its plinth / rings in section
    s.append(t(22, 186, "DETAIL · 3:1 · TAP, cut through (PLAY row, x 263)" if kind == "hush" else "DETAIL · 3:1 · a ripple in section (first layer, face down)", 3.0, INK, weight="bold"))
    D2 = Sec(22 - 108 * 3.0, 303, 3.0)
    D2.s.append('<clipPath id="dclipr5"><rect x="12" y="188" width="228" height="92"/></clipPath><g clip-path="url(#dclipr5)">')
    if kind == "hush":
        D2.R(110, 21.5, 182, 23.5, SHELL, INK, 0.12); D2.R(110, 23.5, 182, 25.5, FELTC, INK, 0.12)
        D2.R(131, 25.2, 133, 25.5, "#5f5d5a", INK, 0.05); D2.R(159, 25.2, 161, 25.5, "#5f5d5a", INK, 0.05)
        D2.R(146 - 8.5, 24.5, 146 + 8.5, 25.5, "#6f6d6a", INK, 0.08)
        D2.R(146 - 3.5, 12, 146 + 3.5, 18, "#3a3a3a", INK, 0.1)
        D2.R(146 - 1.8, 18, 146 + 1.8, 29, "#c9a06c", INK, 0.1)
        D2.P([(146 - 6.35, 28), (146 + 6.35, 28), (146 + 5.5, 31.4), (146, 32), (146 - 5.5, 31.4)], "#e3c493", INK, 0.12)
        D2.R(110, 10.4, 182, 12, GREEN, INK, 0.12)
        notes = ["1  TAP: a 12 mm momentary under a maple peg (part UNVERIFIED)", "2  its own punched felt collar, like every key", "3  a pressed rule in the felt (no ink), flush (R4)", "4  same: blind-pressed with the hot brass die"]
        marks = [(146, 33.5), (139, 24), (131.5, 26.6), (160, 26.6)]
    else:
        D2.R(110, 21.5, 182, 24, PCRM, INK, 0.12)
        for k in range(16):
            for side in (-1, 1):
                y = 146 + side * (7.75 + k * 0.45)
                if abs(y - 146) <= 9.25:
                    D2.R(y - 0.12, 24.0, y + 0.12, 24.4, "#9c8560", "none", 0)
        D2.R(146 - 3.5, 14.5, 146 + 3.5, 21.5, POT, INK, 0.1); D2.R(146 - 3.5, 21.5, 146 + 3.5, 26.5, "#9a9da1", INK, 0.1)
        knob_sec(D2, 146, 24.5)
        D2.R(110, 12.9, 182, 14.5, GREEN, INK, 0.12)
        notes = ["1  rings: concentric first-layer lines, r 7.75 → 9.25 (0.45 pitch; relief drawn exaggerated)", "2  smooth: the plain first layer, everywhere else", "3  the knob skirt hides the bushing; no top nut", "4  1.5 mm of smooth between neighbouring ripples"]
        marks = [(155, 25.6), (172, 25.6), (146, 37), (163, 21.2)]
    for k, (yy_, zz) in enumerate(marks):
        D2.s.append(circ(D2.X(yy_), D2.Z(zz), 1.6, "#f3efe8", ACC, 0.25))
        D2.s.append(t(D2.X(yy_), D2.Z(zz) + 0.75, str(k + 1), 2.0, ACC, "middle", weight="bold"))
    D2.s.append("</g>")
    s.append(D2.svg())
    for k, n in enumerate(notes):
        s.append(t(250, 210 + k * 7, n, 2.2, INK))
    foot(s)
    return write(s, "mock-C-construction", os.path.join(ROOT, c["folder"]))

def fold_half_sec(S, Fo, closed=False):
    """FOLD section at x 150 (through the grille/speaker band, beside EMPHASIS and TAP on the axis)."""
    D = Fo.D
    def base():
        S.P(rounded_profile(0, D, r5.BASE_H, 3, 6), WAL, INK, 0.2)
        S.R(4, 2, D - 4, r5.BASE_H + 0.05, "#f7f4ee", "none", 0)
        S.L(4, 2, 4, 15.6, INK, 0.12); S.L(D - 4, 2, D - 4, 15.6, INK, 0.12); S.L(4, 2, D - 4, 2, INK, 0.12)
        S.R(8, 4.5, 82, 6.1, GREEN, INK, 0.12)
        S.R(52, 13.1, D - 4.3, 14.6, BLK, INK, 0.1); S.R(52, 14.6, D - 4.3, 15.6, PGC, INK, 0.1)
        for y0, y1, zt, col in ((4.8, 34.2, 17.5, "#f6f3ec"), (36.5, 50.5, 19.5, "#3b3734")):
            S.R(y0, zt - 3, y1, zt, col, INK, 0.12)
            S.R((y0 + y1) / 2 - 3.5, 6.1, (y0 + y1) / 2 + 3.5, zt - 3, "#3a3a3a", INK, 0.1)
        pot_sec(S, 68, 6.1, 18.1)
        knob_sec(S, 68, 16.1, d=14.5, h=13.5, col=BLK)
        for y in (56, D - 12):
            S.R(y - 2.75, 6.1 if y < 82 else 2, y + 2.75, 13.1, "#c9b27a", INK, 0.1)
            S.screw_up(y, 0, 6.5)
    def lid(flip):
        L0 = Fo.LY0
        Y = (lambda d: D - d) if flip else (lambda d: L0 + d)
        Zf = (lambda z: 50 - z) if flip else (lambda z: z)
        def RR(d0, z0, d1, z1, fill, **k): S.R(Y(d0), Zf(z0), Y(d1), Zf(z1), fill, **k)
        S.P([(Y(p[0]), Zf(p[1])) for p in rounded_profile(0, D, r5.LID_H, 3, 6)], WAL, INK, 0.2)
        RR(-1.5, 12.6, D - 4, r5.LID_H + 0.2, PAPER, stroke="none", sw=0)
        RR(4, 2, D - 4, 12.6, "#f7f4ee", stroke=INK, sw=0.1)
        RR(0.3, 12.6, D - 4.3, 14.1, BLK, stroke=INK, sw=0.1); RR(0.3, 14.1, D - 4.3, 15.1, PGC, stroke=INK, sw=0.1)
        s0, s1 = Fo.p["spk"]
        RR(s0, 2.3, s1, 12.6, "#3b3d40", stroke=INK, sw=0.12)
        RR(2, 4.0, s0 - 1, 5.6, GREEN, stroke=INK, sw=0.12); RR(s1 + 1, 4.0, D - 6, 5.6, GREEN, stroke=INK, sw=0.12)
        for d in (Fo.dV1, Fo.dV2, Fo.dFX):
            RR(d - 4.75, 5.6, d + 4.75, 12.6, POT, stroke=INK, sw=0.1)
            RR(d - 3.5, 12.6, d + 3.5, 17.6, "#9a9da1", stroke=INK, sw=0.1)
            S.P([(Y(d - 7.25), Zf(15.6)), (Y(d + 7.25), Zf(15.6)), (Y(d + 6.5), Zf(29.1)), (Y(d - 6.5), Zf(29.1))], BLK, INK, 0.15)
        S.C(Fo.AX_Y, 25, 4.8, "none", MUTE, 0.2, dash="1 0.8")
    if closed:
        lid(True); base()
    else:
        base(); lid(False)

def lid_plan(s, Fo, ox, oy, sc):
    """plan of the lid's insides (open, looking down through the plate)."""
    D, L0 = Fo.D, Fo.LY0
    X = lambda x: ox + x * sc; Y = lambda d: oy - d * sc
    s.append(rect(X(0), Y(D), 286 * sc, D * sc, "#f6f2ea", WAL, 0.4, rx=12 * sc))
    s.append(rect(X(12), Y(D - 6), 262 * sc, (D - 8) * sc, "#d7e4dc", GREEN, 0.25))
    for a, b, d0, d1 in Fo.p["cells"]:
        s.append(rect(X(a), Y(d1), (b - a) * sc, (d1 - d0) * sc, "#5d6a7a", INK, 0.2))
    s0, s1 = Fo.p["spk"]
    s.append(rect(X(113), Y(s1), 60 * sc, (s1 - s0) * sc, "#3b3d40", INK, 0.2))
    s.append(rect(X(60), Y(D - 8.4), 170 * sc, 1.6 * sc, GREEN, INK, 0.2))          # far-wall I/O board (rev 5.6)
    s.append(t(X(145), Y(D - 10) + 2.4, "I/O board (jacks + power in the far wall)", 1.6, INK, "middle"))
    R = r5.rows(0)
    for key, d in (("V1", Fo.dV1), ("V2", Fo.dV2), ("FX", Fo.dFX)):
        for name, lab, x, kind, midi, yo in R[key]:
            if kind in "kgry":
                s.append(rect(X(x - 4.75), Y(d + 4.75), 9.5 * sc, 9.5 * sc, POT, "none", 0))
            elif kind == "t":
                s.append(circ(X(x), Y(d), 3 * sc, "#9a9da1", "none", 0))
            elif kind == "b":
                s.append(circ(X(x), Y(d), 6 * sc, "#f4efe4", INK, 0.2))
    s.append(t(X(143), Y((s0 + s1) / 2) + 0.8, "speaker", 2.0, "#f3efe8", "middle"))
    for a, b, d0, d1 in Fo.p["cells"]:
        s.append(t(X((a + b) / 2), Y((d0 + d1) / 2) + 0.8, "cells", 2.0, "#f3efe8", "middle"))
    s.append(t(X(0), Y(-4), "hinge edge", 1.9, MUTE))

def sheet_c_fold(c):
    Fo = c["Fo"]; D = Fo.D
    s = head(c["title"], c["kind"], "How it's built: each half is one hollowed block; one pickguard carries that half's controls (and keys), drops in and is screwed from behind. Sections at x 150, through the speaker band.", "sheet C — construction")
    sc = 1.15 if D < 120 else 0.98
    S = Sec(22, 112, sc)
    fold_half_sec(S, Fo, closed=False)
    OP = 2 * D + 2
    S.s.append(dim_h(S.X(0), S.X(OP), S.Z(-6), f"{OP:.0f} mm open (two halves of {D:.0f} + a 2 mm seam)"))
    S.note(20, 17.5, 20, 40, "keys 1.9 above the plate, behind a 4 mm flush rim", INK, 2.0)
    S.note(56, 1, 12, -8, "6 × M3 up through the block into standoffs on the pickguard", INK, 2.0)
    S.note(Fo.LY0 + Fo.p["spk"][0] + 10, 9, Fo.LY0 + 40, 40, "speaker under the centred grille; cells either side (plan, right)", INK, 2.0)
    S.note(Fo.LY0 + Fo.dFX, 29, Fo.LY0 + Fo.dFX + 6, 44, "back row", INK, 2.0)
    s.append(S.svg())
    s.append(t(22, 54, f"OPEN · {sc}:1", 3.0, INK, weight="bold"))
    S2 = Sec(22, 196, sc)
    fold_half_sec(S2, Fo, closed=True)
    S2.s.append(dim_v(S2.X(D) + 4, S2.Z(50), S2.Z(0), "≈ 50.1 closed"))
    S2.note(Fo.D - Fo.dFX, 21, Fo.D - Fo.dFX + 30, 61, "closed: the back row lands over the whites (4.0 clear), V2 over the sharps (2.0)", INK, 2.0)
    S2.note(D - Fo.dV1, 21, D - Fo.dV1 + 6, 55, "V1 parks behind the PLAY row (5.9 clear)", INK, 2.0)
    s.append(S2.svg())
    s.append(t(22, 133, f"CLOSED · {sc}:1", 3.0, INK, weight="bold"))
    # lid plan + flag
    pl_sc = 0.62
    lid_plan(s, Fo, 210, 132 + D * pl_sc, pl_sc)
    s.append(t(210, 128, "THE LID'S INSIDES · plan, 0.62:1 (plate removed)", 2.6, INK, weight="bold"))
    fy = 140 + D * pl_sc
    s.append(rect(210, fy, 198, 24, "#f3eaf6", FLAG, 0.35))
    s.append(t(213, fy + 4.5, "DAISY SEED: IN THE BASE (systems rev 5.6) · HEIGHT UNVERIFIED", 2.4, FLAG, weight="bold"))
    msg = ("The Daisy Seed (51 × 18) moves to the base's rear right strip (x ≈ 200–272, y 80 to D − 4), on the floor in a board cutout, with its USB-C facing the base's right end face. USB-C (y 90–99) and TRS MIDI IN (y 70) and OUT (y 80) sit in that end face. The audio/CV jacks and the power switch move to the lid's far wall (x 60–230), so neither lid end face carries I/O and the stays stay symmetric. Open: the Seed's seated height (8–8.4 + socket) against 11.1 mm floor to plate; the spike must measure it.")
    p, _ = para(213, fy + 8.5, msg, 104, 2.05)
    s.append(p)
    i, b = img(os.path.join(OUT, f"r5_fo{c['v']}_exploded.png"), 22, 216, 180, 64)
    s.append(i)
    p, _ = para(22, 283, "The lid's pickguard lifted out with its board, speaker, cells and the far-wall I/O board. One ribbon to the base; the Daisy Seed is in the base (not shown).", 110, 2.2, fill=MUTE, style="italic")
    s.append(p)
    foot(s)
    return write(s, "mock-C-construction" + c["variant"], os.path.join(ROOT, "fold"))

# ================================================================== sheet D (front views)
def key_detail_os(S, edge, pressed=False):
    """ONE SHEET front edge at large scale: y right (front at left), z up."""
    tz = 26.5 - (3.0 if pressed else 0)
    S.R(-2, -1.5, 30, 0, "#e7e0d2", "none", 0)
    S.R(0, 0, 2.4, 17.5 if edge == "A" else 24.3, PCRM, INK, 0.15)
    if edge == "B":
        S.C(1.2, 24.3, 1.2, PCRM, INK, 0.15)
        S.R(0.02, 23.0, 2.38, 24.3, PCRM, "none", 0)
    S.R(2.4, 0.6, 30, 3.0, PLY, INK, 0.12)
    S.R(3, 15.1, 30, 16.7, GREEN, INK, 0.12)
    yc = 18
    S.R(yc - 7, 16.7, yc + 7, 20.0, "#3a3a3a", INK, 0.12)
    S.R(yc - 1.2, 20.0, yc + 1.2, tz - 3, "#c94a3a", INK, 0.1)
    S.R(yc - 3, tz - 3 - 1.5, yc + 3, tz - 3, "#c94a3a", INK, 0.1)
    if edge == "A":
        S.P([(0.3, tz - 5), (0.3, tz), (30, tz), (30, tz - 3), (1.9, tz - 3), (1.9, tz - 5)], "#f6f3ec", INK, 0.15)
    else:
        S.R(3, tz - 3, 30, tz, "#f6f3ec", INK, 0.15)
    S.R(26.5, 16.7, 29.5, 18.2, "#555", INK, 0.08)          # flat Hall sensor on strip C
    S.R(26.8, tz - 3 - 1.2, 29.2, tz - 3, "#8e9296", INK, 0.08)  # magnet in the key top (D31)

def key_detail_hu(S, edge, pressed=False):
    FT = 25.5
    rt = 4 if edge == "A" else 12
    yc = 13.5 if edge == "A" else 19.5
    S.P(rounded_profile(0, 60, FT, rt, 6), FELTC, INK, 0.2)
    S.P(rounded_profile(2, 58, FT - 2, max(rt - 2, 1.5), 4), SHELL, INK, 0.15)
    S.P(rounded_profile(4.4, 56, FT - 4.5, max(rt - 4.4, 1), 1.6), "#f7f4ee", INK, 0.12)
    S.R(4.4, -0.05, 56, 3.0, "#f7f4ee", "none", 0)
    S.R(2, 7, 56, 8.6, GREEN, INK, 0.12)
    dz = -2.5 if pressed else 0
    S.R(yc - 3.5, 8.6, yc + 3.5, 14.5, "#3a3a3a", INK, 0.1)
    S.R(yc - 1.2, 14.5, yc + 1.2, 18 + dz, "#c94a3a", INK, 0.08)
    S.R(yc - 2, 17 + dz, yc + 12.5, 19 + dz, "#d9e2ea", INK, 0.1)          # acrylic arm carrying the magnet
    S.R(yc + 9, 15.5 + dz, yc + 12, 17 + dz, "#888", INK, 0.08)
    S.R(yc - 1.8, 19 + dz, yc + 1.8, 28 + dz, "#c9a06c", INK, 0.1)
    S.P([(yc - 6.35, 28 + dz), (yc + 6.35, 28 + dz), (yc + 5.5, 31.4 + dz), (yc, 32 + dz), (yc - 5.5, 31.4 + dz)], "#e3c493", INK, 0.12)
    S.R(yc - 9.5, FT - 1, yc - 2.2, FT, "#6f6d6a", INK, 0.08); S.R(yc + 2.2, FT - 1, yc + 9.5, FT, "#6f6d6a", INK, 0.08)

def sheet_d(c):
    f = c["folder"]
    if f == "fold":
        return sheet_d_fold(c)
    kind = "hu" if f == "hush" else "os"
    W, D = (r5.HU_W, r5.HU_D) if kind == "hu" else (r5.OS_W, r5.OS_D)
    s = head(c["title"], c["kind"], "Front views (owner: \"front views of all of these so I can see the details\"): orthographic, from the player's seat, 1:1, the same model as sheets A–C. Key edge A and B, both (\"show me both\"). Keys may rise 1–2 mm if eng adds the aftertouch layer (re-render with R5_KEY_LIFT).", "sheet D — front views, real size (NEW)")
    ox = 30
    y = 42
    kz = (24, 26.5, "knobs 34.5 · CUTOFF 36.1") if kind == "os" else (25.5, 32, "knobs 36 · CUTOFF 37.6")
    for e, title in (("A", "A · KEYS AT THE EDGE, RAISED, NO LIP"), ("B", "B · SMALL LIP JUST BELOW THE KEY TOPS")):
        s.append(t(ox, y + 2, f"FRONT ELEVATION · 1:1 · {title}", 2.8, INK, weight="bold"))
        i, _ = img(os.path.join(OUT, f"r5_{kind}_front{e}.png"), ox, y + 4, W + 4, 41, exact=True)
        s.append(i)
        Z = lambda z: y + 4 + (40 - z)
        X = lambda x: ox + x + 2
        for zz, lab in ((0, "0"), (kz[0], f"face {kz[0]}"), (kz[1], f"keys {kz[1]}"), (36.1 if kind == "os" else 37.6, kz[2])):
            s.append(line(X(W) + 3, Z(zz), X(W) + 6, Z(zz), MUTE, 0.2))
            s.append(t(X(W) + 7, Z(zz) + 0.7, lab, 1.8, MUTE))
        y += 48
    s.append(t(12, y + 2, "RIGHT END · 1:1 · the profile (front at the left)", 2.8, INK, weight="bold"))
    ew = D + 4
    for k, e in enumerate(("A", "B")):
        xx = 12 + k * (ew + 8)
        i, _ = img(os.path.join(OUT, f"r5_{kind}_end{e}.png"), xx, y + 4, ew, 41, exact=True)
        s.append(i)
        s.append(t(xx, y + 48.5, e, 2.8, ACC, weight="bold"))
    y += 54
    s.append(t(12, y + 1, "THE EDGE AND THE PRESS · " + ("2.3:1" if kind == "os" else "1.45:1") + " · how a key works here (schematic heights)", 2.8, INK, weight="bold"))
    sc = 2.3 if kind == "os" else 1.45
    ztop = 28.5 if kind == "os" else 33
    for k, e in enumerate(("A", "B")):
        for j, pr in enumerate((False, True)):
            gx = 12 + k * 200 + j * 98
            S = Sec(gx + (4 if kind == "os" else 0), y + 5 + ztop * sc, sc)
            if kind == "os":
                key_detail_os(S, e, pr)
            else:
                key_detail_hu(S, e, pr)
            cw = 46 if kind == "hu" else 31
            cid = f"kd{k}{j}"
            s.append(f'<clipPath id="{cid}"><rect x="{S.X(-2):.2f}" y="{S.Z(ztop + 3):.2f}" width="{(cw + 2) * sc:.2f}" height="{(ztop + 6) * sc:.2f}"/></clipPath><g clip-path="url(#{cid})">{S.svg()}</g>')
            s.append(line(S.X(cw), S.Z(-2), S.X(cw), S.Z(ztop + 2), MUTE, 0.25, "1 0.7"))
            s.append(t(gx, y + 10 + (ztop + 1.5) * sc, f"{e} · {'pressed' if pr else 'at rest'}", 2.2, ACC if not pr else INK, weight="bold"))
    y = y + 13 + (ztop + 1.5) * sc - 63
    cap_, _ = para(12, y + 70, ("Choc V2 silent switch (dark) on strip C (green); its stem (red) carries the pressed-on acrylic top. A key goes straight down ≈ 3 mm: a button with a key-shaped top, not a pivoting piano lever. The magnet in the top (grey) closes on a flat Hall sensor on strip C: how fast it closes is the velocity. A: the top's skirt drops into the 4 mm slot and stops 1 mm above the wall. B: the top stands 1 mm over the lip at rest and 2 mm below it pressed."
                             if kind == "os" else "Choc V2 silent switch (dark) on strip C (green); the acrylic arm carries the peg over the stem and the magnet 10.5 mm behind it, over the Hall sensor. The peg goes straight down 2.5 mm and lands on its felt collar before the switch bottoms: felt is the stop, which is why it's silent. A: r 4 front edge, pegs 6 forward. B: the r 12 brow."), 220, 2.1, fill=MUTE)
    s.append(cap_)
    foot(s)
    return write(s, "mock-D-front", os.path.join(ROOT, f))

def sheet_d_fold(c):
    Fo = c["Fo"]; D = Fo.D; OP = 2 * D + 2; v = c["v"]
    s = head(c["title"], c["kind"], "Front views (owner: \"front views of all of these so I can see the details\"): orthographic, from the player's seat, 1:1, the same model as sheets A–C. FOLD's key edge is option B by construction: a 4 mm flush rim, keys 1.9 proud (+1–2 mm if eng adds the aftertouch layer).", "sheet D — front views, real size (NEW)")
    ox = 30; y = 44
    for nm, title, hz in (("front_open", "OPEN", 41), ("front_closed", "CLOSED (the walnut bar)", 55)):
        s.append(t(ox, y + 2, f"FRONT ELEVATION · 1:1 · {title}", 2.8, INK, weight="bold"))
        i, _ = img(os.path.join(OUT, f"r5_fo{v}_{nm}.png"), ox, y + 4, 290, hz, exact=True)
        s.append(i)
        Z = lambda z, y=y, hz=hz: y + 4 + (hz - 1 - z)
        X = lambda x: ox + x + 2
        ticks_ = ((0, "0"), (15.6, "plate"), (17.5, "keys"), (29.1, "knob tops"), (34.5, "lid")) if nm == "front_open" else ((0, "0"), (15.6, "seam"), (50.1, "closed"))
        for zz, lab in ticks_:
            s.append(line(X(286) + 3, Z(zz), X(286) + 6, Z(zz), MUTE, 0.2)); s.append(t(X(286) + 7, Z(zz) + 0.7, f"{lab} {zz}", 1.8, MUTE))
        s.append(line(X(143), y + 4 + hz + 1, X(143), y + 4 + hz + 4, ACC, 0.25))
        s.append(t(X(143), y + 4 + hz + 6.5, "axis x 143 · brass pin" if nm == "front_open" else "axis x 143", 1.9, ACC, "middle"))
        y += hz + 13
    s.append(t(ox, y + 2, "RIGHT END · 1:1 · front at the left (USB-C + MIDI in / out in the base's right end; jacks in the lid's far wall)", 2.8, INK, weight="bold"))
    sc_end = min(1.0, 386 / (OP + 4 + D + 10))
    ox = 12
    i, b = img(os.path.join(OUT, f"r5_fo{v}_end_open.png"), ox, y + 4, (OP + 4) * sc_end, 41 * sc_end, exact=True)
    s.append(i)
    for yw_, lab_ in ((r5.FO_MIDI_IN_Y, "midi in"), (r5.FO_MIDI_Y, "midi out"), (r5.FO_USB_Y, "usb-c")):   # rev 5.6 base end face
        s.append(t(ox + (yw_ + 2) * sc_end, y + 4 + 41 * sc_end + 2.6, lab_, 1.7, ACC, "middle"))
    s.append(t(ox, y + 4 + 41 * sc_end + 4, f"open, {OP:.0f} deep" + (f" (shown at {sc_end:.2f}:1 to fit)" if sc_end < 1 else ""), 2.2, ACC, weight="bold"))
    x2 = ox + (OP + 4) * sc_end + 10
    i, _ = img(os.path.join(OUT, f"r5_fo{v}_end_closed.png"), x2, y + 4 - 14 * sc_end, (D + 10) * sc_end, 55 * sc_end, exact=True)
    s.append(i)
    s.append(t(x2, y + 4 + 41 * sc_end + 4, f"closed, {D:.0f} × ≈ 50", 2.2, ACC, weight="bold"))
    y += 41 * sc_end + 14
    # rim detail
    s.append(t(ox, y + 1, "THE FRONT RIM AND THE PRESS · 2:1 (schematic heights)", 2.8, INK, weight="bold"))
    for j, pr in enumerate((False, True)):
        S = Sec(ox + 6 + j * 92, y + 8 + 18 * 2.0, 2.0)
        S.P(rounded_profile(0, 40, r5.BASE_H, 3, 6), WAL, INK, 0.2)
        S.R(4, 2, 40, 15.65, "#f7f4ee", "none", 0)
        S.R(8, 4.5, 40, 6.1, GREEN, INK, 0.12)
        dz = -3 if pr else 0
        S.R(18 - 7, 6.1, 18 + 7, 9.6, "#3a3a3a", INK, 0.1)
        S.R(18 - 1.2, 9.6, 18 + 1.2, 14.5 + dz, "#c94a3a", INK, 0.08)
        S.R(4.8, 14.5 + dz, 40, 17.5 + dz, "#f6f3ec", INK, 0.15)
        s.append(S.svg())
        s.append(t(ox + 6 + j * 92, y + 50, "pressed" if pr else "at rest", 2.2, ACC, weight="bold"))
    s.append(rect(ox + 192, y + 30, 186, 22, "#f3eaf6", FLAG, 0.35))
    s.append(t(ox + 195, y + 34.5, "I/O MOVED (systems rev 5.6) · stay clash resolved", 2.3, FLAG, weight="bold"))
    pf, _ = para(ox + 195, y + 38.5, "Audio/CV jacks + power switch: the lid's far wall, x 60–230 (on the bar's front face when closed, above). USB-C (y 90–99) + TRS MIDI IN (y 70) and MIDI OUT (y 80): the base's right end face, off the Daisy Seed. Both lid end faces carry only the stays.", 100, 2.0)
    s.append(pf)
    p, _ = para(ox + 192, y + 4, "The rim (y 0–4) is flush with the base plate (15.6) and the keys stand 1.9 above it: you feel the keys over a low lip, and closed, the rim and the lid's rim meet so the key tops are guarded. A raised-skirt option A is possible for FOLD (keys +0.6 to 18.1, skirt over a lowered wall), but B is the default: it is the base's own meeting edge. Keys are button keys (≈ 3 mm straight down), not pivoting levers.", 70, 2.15)
    s.append(p)
    foot(s)
    return write(s, "mock-D-front" + c["variant"], os.path.join(ROOT, "fold"))

# ================================================================== sheet E (FOLD standing, NEW)
def sheet_e_fold(c):
    Fo = c["Fo"]; D = Fo.D; v = c["v"]
    Fo.stays(); py, pz, ty = Fo.stay_pts
    _a = math.radians(Fo.STAND); _vy, _vz = Fo.LY0 + Fo.dFX - Fo.AX_Y, r5.LID_PF + 13.5 - r5.AX_Z
    by_ = Fo.AX_Y + _vy * math.cos(_a) - _vz * math.sin(_a); bz_ = r5.AX_Z + _vy * math.sin(_a) + _vz * math.cos(_a)
    s = head(c["title"], c["kind"], "Standing (owner: \"some sort of method for the top case to stand up … it should blend into the case\"; one angle is fine). Leaned back to 120° (owner: \"a bit less steep so the front face catches more light\") on two brass stays that live flush in its end faces.", "sheet E — standing at 120° (rev 5.7)")
    i, b = img(os.path.join(OUT, f"r5_fo{v}_stand.png"), 10, 42, 196, 150)
    s.append(i)
    cap, _ = para(12, 196, "Standing, wood-fill print. The stays are the same brass as the lid's back screws, and the same idea as a writing box's lid stay: flat bar, one pin, a hard stop in its boss. Stowed, each is a brass line in the end face; there is no prop, no hatch and nothing proud when it lies flat or closes.", 100, 2.3, fill=MUTE, style="italic")
    s.append(cap)
    # 1:1 side elevation with overlays
    a0, a1, b0, b1 = -4, D + 84, -1, D + 34      # S2: wider, the 120° lid reaches further back
    ox, oy = 210, 44
    i, _ = img(os.path.join(OUT, f"r5_fo{v}_stand_side.png"), ox, oy, a1 - a0, b1 - b0, exact=True)
    s.append(i)
    X = lambda y: ox + (y - a0); Z = lambda z: oy + (b1 - z)
    s.append(t(ox, oy - 1.5, "RIGHT END · 1:1 · standing (front at the left)", 2.8, INK, weight="bold"))
    s.append(line(X(-4), Z(0), X(a1), Z(0), MUTE, 0.25))
    s.append(dim_h(X(D), X(ty), Z(0) + 6, f"{ty - D:.0f} behind the base"))
    s.append(dim_h(X(0), X(D), Z(0) + 6, f"base {D:.0f}"))
    s.append(circ(X(Fo.AX_Y), Z(25), 1.0, "none", ACC, 0.3))
    s.append(t(X(Fo.AX_Y) - 9, Z(25) + 4.5, "hinge axis", 1.9, ACC, "end"))
    s.append(circ(X(py), Z(pz), 1.0, "none", ACC, 0.3))
    s.append(t(X(py) + 6, Z(pz) - 1.5, "stay pivot, d 30", 1.9, ACC))
    s.append(t(X(ty) + 3, Z(4), "rubber tip", 1.9, ACC))
    # the angle, drawn: base (toward the player) to the lid face, swept over the open side
    hx, hz, R_ = X(Fo.AX_Y), Z(r5.AX_Z), 22.0
    a_lid = math.radians(Fo.STAND)                      # lid direction, maths angle (y up, sheet right = world +y)
    s.append(f'<path d="M {hx - R_:.2f} {hz:.2f} A {R_} {R_} 0 0 1 {hx + R_ * math.cos(a_lid):.2f} {hz - R_ * math.sin(a_lid):.2f}" fill="none" stroke="{ACC}" stroke-width="0.35"/>')
    s.append(line(hx - R_ - 3, hz, hx - 1.5, hz, ACC, 0.25, dash="1,0.8"))
    am = math.radians(120)
    s.append(t(hx + (R_ + 3) * math.cos(am), hz - (R_ + 3) * math.sin(am), f"{180 - Fo.STAND:.0f}°", 3.2, ACC, "end", weight="bold"))
    s.append(t(X(ty) + 3, Z(14), f"stay {Fo.STAY_L:.1f}", 1.9, ACC))
    yy = 212
    s.append(t(12, yy, "WHY 120°, AND WHY STAYS (systems rev 5.5 + 5.7)", 3.0, ACC, weight="bold")); yy += 5.5
    for k, txt_ in enumerate([
        "At 90° the lid's weight sits right over the hinge, so a knock tips it either way. At 120° it leans 30° back onto its stays and holds itself up: no detent, no friction hinge. The panel faces 30° up, so it catches ≈ 1.9× the overhead light it got at 105° (cos 60° vs cos 75°) and sits close to square-on to a seated eye. 125° would add little light, more lamp glare and a longer reach.",
        "A hinge stop alone isn't enough: upright, the lid's weight is over the base's rear edge, and ≈ 1.5–1.8 N on a back-row knob would tip the whole instrument backwards (weights ESTIMATE). The stays carry the push to the table: tip threshold ≈ 6.8 N (FOLD-113 6.0); turning a knob pushes ≈ 1–3 N, and at 120° the push runs more downward, which helps.",
        "Stand: open the lid past its standing angle, flip both stays out, lower the lid onto them. Flat: lift, fold the stays in, lower. Closed: the stays are flush.",
    ], 1):
        p, yy = para(12, yy, f"{k}. {txt_}", 125, 2.3); s.append(p); yy += 1
    yy2 = 212
    s.append(rect(12, 262, 190, 16, "#f3eaf6", FLAG, 0.35))
    pf, _ = para(15, 266.5, "Resolved (systems rev 5.6): the jacks and power switch moved to the lid's far wall, USB-C and MIDI in / out to the base's right end. Both lid end faces carry only their stays, symmetric.", 120, 2.1, fill=FLAG)
    s.append(pf)
    xr = 210; yr = oy + (b1 - b0) + 14
    s.append(t(xr, yr, "HOW IT LOOKS AND FEELS", 3.0, ACC, weight="bold")); yr += 5.5
    for k, v_ in [("Stay", "3 × 8 brass flat bar, ends rounded R 4, brushed, then waxed; the pin a domed brass rivet head, flush."),
                  ("Groove", "3.5 deep in the walnut end face, d 30–74.4 (stay 44.4), crisp edges; a 6 mm finger scoop at the free end."),
                  ("Tip", "black rubber cap, 9 Ø, hidden from the seat behind the lid."),
                  ("Feel", "a firm click as the stay meets its stop; the lid settles onto both with a soft knock."),
                  ("Light", "the cream plate faces 30° up: it reads as cream in a room, not the grey of a vertical face."),
                  ("Reach", f"standing, the back row's knob tops sit ≈ {bz_:.0f} mm up and ≈ {by_ - 68:.0f} behind the PLAY row: still a short reach.")]:
        hd, yr = para(xr, yr, k, 30, 2.5, weight="bold"); s.append(hd)
        pv, yr = para(xr, yr, v_, 78, 2.2, fill="#4a443d"); s.append(pv); yr += 0.8
    foot(s)
    return write(s, "mock-E-standing" + c["variant"], os.path.join(ROOT, "fold"))

if __name__ == "__main__":
    which = sys.argv[1:] or ["hush", "one-sheet", "fold105", "fold113"]
    pages = [a for a in which if a in "ABCDE"]
    which = [a for a in which if a not in "ABCDE"] or ["hush", "one-sheet", "fold105", "fold113"]
    pages = pages or list("ABCDE")
    for k in which:
        c = CONTENT[k]
        for p in pages:
            if p == "E" and c["folder"] != "fold":
                continue
            fn = {"A": sheet_a, "B": sheet_b, "C": (sheet_c_fold if c["folder"] == "fold" else sheet_c_flat), "D": sheet_d, "E": sheet_e_fold}[p]
            print(fn(c))
