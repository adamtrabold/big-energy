"""Concept building round 2 (visual): C Cabinet and E Herbarium, 9 frames each, phone AND desktop, 1:1.
New-format work leads: the branches round's BUTTERFLY group (real renders in design/branches/concepts/butterfly/img/,
made from _mock-src/out/rb_bf_*.png) with its how-it-works text as HTML.
Outputs: ../cabinet/frames.{svg,png}, ../cabinet/frames-desktop.{svg,png}, same for ../herbarium/.
"""
from lib import *
import sys

DW, DH = 1440, 900
GAP = 56

# ---------------------------------------------------------------- real words
BF_LINE = "ONE SHEET with a walnut top: exact at the playing edge, free at the rear."
BF_SECTIONS = [
    ("1. What changes from ONE SHEET, and what doesn't",
     ["Unchanged: the printed shell's outline (276 × 180), heights, every control, the main board, the I/O board on the printed rear wall with the jack barrels flush in its holes, the speaker, the battery, the back panel, v1.1's grooves and type."],
     "BF-main", "BUTTERFLY · render · the look"),
    ("Changes",
     ["1. The joint moves to y 165.0.", "2. The rear band becomes a walnut top, laid on the shell like a tabletop on its apron.",
      "3. Two bookmatched leaves joined on the axis by one butterfly.", "4. A French-cleat slot in the back panel, to hang."],
     "BF-joint", "the joint, close · render"),
    ("3. Construction: the top and the apron",
     ["Drilling the jacks through the wood fails: the rail is 15 mm deep at its thinnest. What works, and it's honest furniture: a tabletop over an apron. The printed shell keeps its rear wall with the I/O board and the flush jacks exactly as v1.1."],
     "BF-rear", "rear section · drawing · 24 px/mm"),
    ("5. Hanging",
     ["French-cleat slot routed at 45° along the back panel's rear zone, y ≈ 150–170, x ≈ 40–200. It clears the speaker. Hung, the tree side is up, the knobs face the room."],
     "BF-wall", "on the wall · render"),
]
DECISIONS = [  # newest first, from design/owner.md (verbatim)
    (None, "“i think it needs its own switch but yes now i want it”", "after: D-019 rev 14 · D-034", False),
    ("add a 3.5 mm TRS MIDI OUT jack (free in pins)?", "“Add MIDI out”", "after: D-019", False),
    (None, "“Also the key thing you need to port - go back to first principles and see if there's a better way with Daisy seed…”", "after: D-032", False),
    ("switch the digital brain to the Daisy Seed?", "“Switch to Daisy Seed”", None, True),
    (None, "“It is not a requirement that you can change the angle”", "after: FOLD rev B", False),
    (None, "“I like the idea of drift, but I'd want it to be controllable”", "after: D-019", False),
    (None, "“Check the pin thing. Audio feels the most important since we're introducing digital stuff”", "after: D-031", False),
]
CAUSED = [("before", "D-031", "Pin check and audio-quality check"), ("after", "D-032", "Daisy Seed, from first principles"), ("after", "D-019", "Budget variant spec · rev 13")]
CLOUDS = [(0.813, 0.178, 0.048, 0.068), (0.668, 0.219, 0.048, 0.082), (0.116, 0.328, 0.048, 0.082),
          (0.194, 0.410, 0.068, 0.109), (0.629, 0.835, 0.184, 0.096), (0.610, 0.944, 0.348, 0.055)]

# ---------------------------------------------------------------- shared components
def label(c, x, y, w, code, title, fields, slips, more=None, unseen=False, s=1.0):
    c.l(x, y, x + w, y, INK, 1)
    c.t(x, y + 22 * s, code, 15 * s, 700); c.t(x + tw(code, 15 * s, 700) + 8, y + 22 * s, title, 15 * s, 400)
    if unseen: c.dot(x + w - 4, y + 16 * s)
    c.t(x, y + 42 * s, fields, 12.5 * s, 400, INK2)
    yy = y + 52 * s
    for i, (rv, txt) in enumerate(slips):
        h = 24 * s
        c.r(x, yy, w, h, PAGE if i == 0 else "none", RULE)
        c.t(x + 8, yy + h * 0.69, rv, 12 * s, 700 if i == 0 else 500, INK if i == 0 else INK2)
        c.t(x + 58 * s, yy + h * 0.69, txt, 12 * s, 500 if i == 0 else 400, INK if i == 0 else INK2)
        yy += h + 3
    if more:
        c.t(x + 8, yy + 13 * s, more, 11.5 * s, 500, INK2); yy += 18 * s
    return yy

def doc_tile(c, x, y, w, h, code, title, line=None, size=12):
    c.r(x, y, w, h, PAGE, RULE)
    c.t(x + 8, y + 17, code, 11, 700, INK2)
    yy = c.wrap(x + 8, y + 35, title, w - 16, size, 600, INK, lh=size * 1.3, maxlines=3)
    if line and yy < y + h - 6: c.wrap(x + 8, yy + 2, line, w - 16, size - 1, 400, INK2, lh=(size - 1) * 1.35, maxlines=max(1, int((y + h - yy - 4) / ((size - 1) * 1.35))))

def test_tile(c, x, y, w, h, code, word):
    c.r(x, y, w, h, CELL)
    c.wave("golden", x + 8, y + h * 0.45, w - 16, h * 0.55, n=int(w / 3.5), sw=1)
    c.t(x + 8, y + h - 7, word, 10.5, 700)

def stage_strip(c, x, y, w, words=False):
    n, gap = 9, 4
    sw = (w - gap * 8) / 9
    names = ["Concept", "Lock", "Handoff", "Spec", "BOM", "Breadboard", "Boards", "Prints", "Assembly"]
    for i in range(9):
        xx = x + i * (sw + gap)
        if i <= 1: c.r(xx, y, sw, 6, INK)
        elif i == 3: c.r(xx, y, sw, 6, "none", INK2, 1)
        else: c.r(xx, y, sw, 6, RULE)
        if i == 1: c.r(xx, y + 9, sw, 2, INK)
        if words: c.t(xx, y + 26, names[i], 11.5, 600 if i == 1 else 400, INK if i <= 1 else INK2)
    if not words:
        c.t(x, y + 26, "Lock", 12.5, 600); c.t(x + tw("Lock ", 12.5, 600), y + 26, "· 2 of 9 · Spec begun early · next Handoff", 12.5, 400, INK2)

def lamp_and_name(c, x, y, state, line, w, big=False):
    c.lampline(x, y, state, line)
    c.t(x, y + (40 if big else 32), "( name to come )", 26 if big else 22, 600)
    sub = "a portable Model D · "
    c.t(x, y + (64 if big else 52), sub, 14 if big else 13, 400, INK2)
    vx = x + tw(sub, 14 if big else 13)
    c.t(vx, y + (64 if big else 52), "v1.1 current", 14 if big else 13, 500, INK)
    c.l(vx, y + (67 if big else 55), vx + tw("v1.1 current", 14 if big else 13, 500), y + (67 if big else 55), INK, 0.8)

def waiting_inline(c, x, y):
    c.label(x, y, "Waiting on you"); c.t(x + 118, y + 1, "ONE SHEET or FOLD", 15, 600)

def decisions_list(c, x, y, w, ybot, s=1.0, desktop=False):
    c.label(x, y, "13 Nov", INK)
    yy = y + 10
    for q, words, caused, open_ in DECISIONS:
        if yy > ybot - 40: break
        c.l(x, yy, x + w, yy)
        yy += 22 * s
        if q:
            yy = c.wrap(x, yy, "asked: " + q, w, 12 * s, 400, INK2, lh=17 * s, maxlines=2)
        yy = c.wrap(x, yy + (2 if q else 0), words, w, (16 if open_ else 14) * s, 600 if open_ else 400, INK if open_ else INK2, lh=21 * s, maxlines=2 if not open_ else 3)
        if open_:
            c.t(x, yy, "time not recorded", 12 * s, 500, INK2); yy += 8
            for ba, code, t1 in CAUSED:
                yy += 22 * s
                c.t(x, yy, ba, 12 * s, 500, INK2); c.t(x + 50 * s, yy, code, 13 * s, 700)
                c.t(x + 100 * s, yy, t1, 13 * s, 400); c.l(x + 100 * s, yy + 3, x + 100 * s + tw(t1, 13 * s), yy + 3, INK, 0.6)
            yy += 16
        else:
            c.t(x, yy, caused, 12 * s, 500, INK2); yy += 12
    c.l(x, yy, x + w, yy)

def compare_wipe(c, x, y, w, clouds=True):
    h = c.img("FOLD-A", x, y, w)
    cut = 0.47
    c.img("FOLD-A@v1", x + w * cut, y, w * (1 - cut), h, crop=(cut, 0, 1 - cut, 1))
    if clouds:
        for fx, fy, fw, fh in CLOUDS:
            c.cloud(x + fx * w - 2, y + fy * h - 2, fw * w + 4, min(fh * h + 4, h - fy * h), bump=max(3, w / 120), sw=1.1)
    hx = x + w * cut
    c.l(hx, y, hx, y + h, INK, 1.5); c.circle(hx, y + h / 2, 13, WHITE, INK, 1.5); c.t(hx, y + h / 2 + 4, "‹›", 11, 700, INK, "middle")
    return h

def show_changes(c, x, y, w):
    c.t(x, y, "Show changes from rev B", 13, 600)
    c.r(x + w - 44, y - 14, 44, 20, INK); c.circle(x + w - 10, y - 4, 7, WHITE)
    c.t(x, y + 19, "6 areas: joystick, closed view, effects text, footer", 12, 400, INK2)

def lineage(c, x, y, tile=80):
    tx = x
    th = tile * 0.71
    for k, a, b in [("FOLD-A@r5", "rev A", "round 5"), (None, "r1–r4", "not kept"), ("FOLD-A@v1", "rev B", "v1"), ("FOLD-A", "rev C", "v1.1")]:
        if k:
            c.img(k, tx, y, tile, th)
            if a == "rev B": c.r(tx - 2, y - 2, tile + 4, th + 4, "none", INK, 2)
            c.t(tx, y + th + 16, a, 11.5, 600); c.t(tx, y + th + 31, b, 11.5, 400, INK2); tx += tile + 12
        else:
            c.l(tx + 4, y + th / 2, tx + 44, y + th / 2, RULE, 1, "3 3"); c.t(tx + 4, y + th + 16, a, 11.5, 600, INK2); c.t(tx + 4, y + th + 31, b, 11.5, 400, INK2); tx += 58

def test_block(c, x, y, w, h):
    c.r(x, y, w, h, CELL)
    c.play(x + 36, y + h * 0.42, playing=True)
    c.wave("perturbed", x + 72, y + h * 0.42, w - 100, h * 0.5)
    c.l(x + 72 + 0.31 * (w - 100), y + 12, x + 72 + 0.31 * (w - 100), y + h * 0.72, INK, 1.5)
    c.t(x + 72, y + h * 0.42 + h * 0.36, "0:00.6 / 0:01.98", 12, 500, INK2)
    c.t(x + 20, y + h - 14, "golden", 14, 400, INK2); c.t(x + 92, y + h - 14, "perturbed", 14, 600)
    c.r(x + 92, y + h - 9, tw("perturbed", 14, 600), 2, INK)
    c.t(x + w - 16, y + h - 14, "peak 1.86 V", 12.5, 400, INK2, "end")

def group_label(c, x, y, w, unseen=False, s=1.0):
    yy = label(c, x, y, w, "BUTTERFLY", "rev A", "concept group · 6 images · 1 doc · exploring",
               [("rev A", "13 Nov 14:02 · branches round · first rev")], None, unseen, s)
    c.t(x, yy + 14 * s, "grew from ONE SHEET · v1.1 (legacy sheets) ›", 12.5 * s, 500, INK)
    return yy + 22 * s

def html_section(c, x, y, w, head, paras, size=14):
    yy = c.wrap(x, y, head, w, size + 2, 600, INK, lh=(size + 2) * 1.35) + (size + 2) * 0.2
    for p in paras:
        yy = c.wrap(x, yy, p, w, size, 400, INK, lh=size * 1.5) + size * 0.4
    return yy

def group_page_phone(c, px, y, ybot):
    x, w = px + 16, 358
    yy = group_label(c, x, y, w)
    c.t(x, yy + 22, BF_LINE, 15, 400, INK) if tw(BF_LINE, 15) < w else c.wrap(x, yy + 22, BF_LINE, w, 15, 400, INK, lh=21)
    yy += 78
    for head, paras, key, cap in BF_SECTIONS:
        if yy > ybot - 60: break
        yy = html_section(c, x, yy, w, head, paras, 14)
        iw, ih = IMG(key).size
        nat = w * ih / iw
        h = c.img(key, x, yy, w, min(nat, max(60, ybot - yy - 40)))
        c.t(x, yy + h + 16, cap, 11.5, 500, INK2)
        yy += h + 40
    return yy

# ---------------------------------------------------------------- sheet scaffolds
def phone_sheet(title, sub, n_extra=0, tall9=1900):
    xs = [60 + i * (PW + GAP) for i in range(9 + n_extra)]
    W = xs[-1] + PW + 60
    H = 170 + tall9 + 260
    c = Canvas(W, H); c.r(0, 0, W, H, WHITE)
    c.t(60, 64, title, 30, 700); c.t(60, 96, sub, 15, 400, INK2)
    return c, xs, 170

def tall_phone(c, x, y, h, title, notes, tap):
    c.r(x, y, PW, h, BG)
    c.r(x, y, PW, TOP, CHROME, op=0.55); c.t(x + 30, y + 31, "9:41", 15, 600)
    c.r(x - 0.5, y - 0.5, PW + 1, h + 1, "none", "#8f8c85")
    c.l(x - 10, y + BOT, x - 2, y + BOT, INK2, 1); c.t(x - 12, y + BOT + 4, "fold", 10, 500, INK2, "end")
    c.t(x, y - 18, title, 17, 700); c.t(x + PW, y - 18, tap, 13, 600, INK2, "end")
    yy = y + h + 28
    for n in notes: yy = c.wrap(x, yy, n, PW, 12.5, 400, INK2, lh=18)

def desk_sheet(title, sub, n=8):
    W = 60 * 2 + 2 * DW + 80
    H = 140 + ((n + 1) // 2) * (DH + 90)
    c = Canvas(W, H); c.r(0, 0, W, H, WHITE)
    c.t(60, 60, title, 30, 700); c.t(60, 92, sub, 15, 400, INK2)
    pos = [(60 + (i % 2) * (DW + 80), 150 + (i // 2) * (DH + 90)) for i in range(n)]
    return c, pos

def shell(c, dx, dy, title):
    c.t(dx, dy - 18, title, 18, 700)
    c.r(dx, dy, DW, DH, BG); c.r(dx - 0.5, dy - 0.5, DW + 1, DH + 1, "none", "#8f8c85")

# ================================================================ C · CABINET
def cab(c, x, y, w, rh=34, dots=False, snapshot=False, desktop=False):
    """wide Concept row (concept groups), Lock, level, Handoff, Spec by kind, collapsed not-yet line"""
    nw = 104 if desktop else 88
    gx, gw = x + nw, w - nw
    fs = 14 if desktop else 13.5
    def row(i, name, strong=False, fill=CELL, text="", right="", tcol=INK, tw_=600):
        yy = y + i
        c.t(x, yy + rh / 2 + 5, name, fs, 600 if strong else 400, INK if fill == CELL else INK2)
        if strong: c.r(x - 12, yy + 7, 3, rh - 14, INK)
        c.r(gx + 2, yy + 3, gw - 4, rh - 6, fill, RULE)
        c.t(gx + 12, yy + rh / 2 + 5, text, 13.5 if not desktop else 14.5, tw_, tcol)
        if right: c.t(gx + gw - 10, yy + rh / 2 + 5, right, 12, 500, INK2, "end")
        return yy + rh
    yy = row(0, "Concept", text="18 concepts · 3 locked · 4 exploring", right="11 dropped ›" if desktop else "›")
    if dots and not snapshot: c.dot(gx + gw - 30 - (tw("11 dropped ›", 12, 500) if desktop else 0), y + 11)
    yy = row(rh, "Lock", True, text="v1.1 current · 2 versions", right="now")
    c.l(x - 12, yy + 0.5, x + w, yy + 0.5, INK, 1.5)
    yy = row(2 * rh, "Handoff", fill="none", text="next · starts when you pick", tcol=INK2, tw_=400)
    # Spec, by kind
    hy = yy + 13
    cw = gw / 3
    for j, k in enumerate(["images", "docs", "tests"]):
        c.label(gx + j * cw + cw / 2, hy, k, anchor="middle")
    sy = hy + 4
    c.t(x, sy + rh / 2 + 5, "Spec", fs, 400, INK2); c.t(x + tw("Spec", fs) + 5, sy + rh / 2 + 5, "early", 11, 500, INK2)
    for j, n in enumerate([0, 19, 7]):
        cx = gx + j * cw
        c.r(cx + 2, sy + 3, cw - 4, rh - 6, "none", RULE)
        if n: c.t(cx + cw / 2, sy + rh / 2 + 6, str(n), 16, 500, INK2, "middle")
    ny = sy + rh + 22
    c.t(x, ny, "BOM · Breadboard · Boards · Prints · Assembly — not yet", 13 if not desktop else 14, 400, INK2)
    c.t(x + w, ny, "›", 15, 400, INK2, "end")
    return ny + 10

def cab_scrub(c, x, y, w, at=7, dated=False):
    det = ["R1", "R2", "R3", "R4", "R5", "v1", "v1.1", "now"]
    dates = ["12 Nov"] * 4 + ["13 Nov"] * 3 + [""]
    c.t(x + w, y - 8, "history ›   decisions ›", 13, 500, INK2, "end")
    yl = y + 18
    c.l(x + 8, yl, x + w - 8, yl, INK, 1.5)
    for i, d in enumerate(det):
        xx = x + 8 + i * (w - 16) / 7
        big = d.startswith("v") or d == "now"
        c.l(xx, yl - (9 if big else 5), xx, yl + (9 if big else 5), INK, 1.5 if big else 1)
        c.t(xx, yl + 26, d + ("  " + dates[i] if dated and dates[i] else ""), 12, 600 if big else 400, INK if big else INK2, "middle")
    hx = x + 8 + at * (w - 16) / 7
    c.r(hx - 7, yl - 14, 14, 28, INK)

def cab_phone_landing(c, px, py, state, line, newest_slip, dots=False, snapshot=False, unseen=None):
    x, y0 = px + 16, py + TOP
    lamp_and_name(c, x, y0 + 26, state, line, 358)
    c.l(x, y0 + 92, x + 358, y0 + 92)
    waiting_inline(c, x, y0 + 114)
    yy = cab(c, x, y0 + 130, 358, dots=dots, snapshot=snapshot)
    c.label(x, yy + 18, "Newest")
    if unseen: c.t(x + 358, yy + 18, unseen, 12.5, 600, INK, "end")
    h = c.img("BF-main", x, yy + 28, 358)
    ly = yy + 28 + h
    c.t(x, ly + 22, "BUTTERFLY", 15, 700); c.t(x + tw("BUTTERFLY", 15, 700) + 8, ly + 22, "rev A · " + newest_slip, 13, 400)
    if dots and not snapshot: c.dot(x + 358 - 4, ly + 16)
    c.t(x, ly + 41, "concept group · Concept · exploring · open ›", 12.5, 400, INK2)
    cab_scrub(c, x, py + BOT - 70, 358)

def cabinet_sheets():
    # ---------------- phone
    c, xs, PY = phone_sheet("C · Cabinet — round 2 · 9 frames at phone (390 × 844, 1:1)",
                            "New-format work leads: BUTTERFLY rev A (branches round): real renders + its how-it-works as HTML. Wide Concept row of groups; not-yet stages on one line; Newest at full width. Desktop frames: frames-desktop.png.", 1)
    px = xs[0]
    c.phone(px, PY, "1 · Landing, standby", [
        "Systems' wide Concept row holds: one drawer of concept groups (18 · 3 locked · 4 exploring · 11 dropped). It reads as a status panel, and the grid only starts at Spec. That's fine: the grid fills as stages start.",
        "Not-yet stages on one line (ink 2, ›) free 140 px. The newest work now shows at full width: BUTTERFLY's lead render, at its own shape.",
        "Waiting on you on one line beside its label."], "0 taps")
    cab_phone_landing(c, px, PY, "standby", "Standby · last BUTTERFLY rev A · 14:02", "14:02")
    px = xs[1]
    c.phone(px, PY, "2 · On — BUTTERFLY rev A lands", [
        "Lamp ON, one dip. Concept drawer gets the unseen dot. Newest cross-fades (180 ms) to the new group; ‘1 unseen’.",
        "Counts don't change: the 4 exploring already included it once its doc existed. If the images aren't published yet, Newest shows the label and ‘images arriving with the next publish’."], "0 taps")
    cab_phone_landing(c, px, PY, "dip", "On · branches round · since 13:40", "just now", dots=True, unseen="1 unseen")
    # 3
    px = xs[2]
    c.phone(px, PY, "3 · FOLD-A v1.1 → v1, changes on", [
        "Path: ‘v1.1 current’ (1) → FOLD-A under FOLD (2) → rev B in the lineage (3). Via the cabinet: 4.",
        "‘Show changes’ (from D) is in the shared viewer, off by default; here on. Ink scallops from a real pixel diff, on the wipe.",
        "Legacy sheet, labelled so. Pinch to zoom; no read mode."], "3 taps")
    x, y0 = px + 16, PY + TOP
    c.t(x, y0 + 30, "‹ v1.1", 14, 500, INK2); c.t(x + 358, y0 + 30, "copy link", 13, 500, INK2, "end")
    h = compare_wipe(c, x, y0 + 48, 358)
    c.label(x + 6, y0 + 48 + h + 16, "rev C · v1.1", INK); c.label(x + 352, y0 + 48 + h + 16, "rev B · v1", INK, "end")
    show_changes(c, x, y0 + 48 + h + 44, 358)
    yy = label(c, x, y0 + 48 + h + 82, 358, "FOLD-A", "The look", "legacy sheet · Concept · locked in v1.1",
               [("rev C", "13 Nov · v1.1 · bend drawn as a joystick"), ("rev B", "13 Nov · v1 · first lock")], "+ rev A (round 5) · r1–r4 not kept")
    lineage(c, x, yy + 14)
    # 4
    px = xs[3]
    c.phone(px, PY, "4 · Bass pluck · golden vs perturbed", [
        "Path: Spec·tests (1) → T-004 (2). Tests serve Spec (ruling), marked early.",
        "Result in words, numbers as one line, the sound block, A/B keeps the playhead. Plot below."], "2 taps")
    x, y0 = px + 16, PY + TOP
    c.t(x, y0 + 30, "‹ Spec · tests", 14, 500, INK2); c.t(x + 358, y0 + 30, "copy link", 13, 500, INK2, "end")
    c.t(x, y0 + 68, "T-004", 20, 700); c.t(x + 74, y0 + 68, "Bass pluck", 18, 400)
    c.t(x, y0 + 90, "test · Spec (early) · ran 13 Nov", 13, 400, INK2)
    c.t(x, y0 + 120, "RAN", 15, 700); c.t(x + 40, y0 + 120, "no limits set · osc 110.0 Hz", 13, 400, INK2)
    c.t(x, y0 + 140, "envelope peak 87 ms golden · 69 ms perturbed", 12.5, 400, INK2)
    test_block(c, x, y0 + 156, 358, 150)
    c.img("PLOT-pluck", x, y0 + 322, 358)
    # 5
    px = xs[4]
    c.phone(px, PY, "5 · Decisions: “Switch to Daisy Seed”", [
        "Path: ‘decisions ›’ above the scrubber (1) → scroll → a caused item (2).",
        "D's register, in C: date · the question in ink 2 · his words verbatim at body size · what it caused (before / after, codes as links). The open one is 600 weight."], "2 taps + scroll")
    x, y0 = px + 16, PY + TOP
    c.t(x, y0 + 30, "‹ Cabinet", 14, 500, INK2)
    c.t(x, y0 + 66, "Decisions", 22, 600); c.t(x + 358, y0 + 66, "45 · newest first", 12.5, 500, INK2, "end")
    decisions_list(c, x, y0 + 96, 358, PY + BOT)
    # 6
    px = xs[5]
    c.phone(px, PY, "6 · What's in v1.1", [
        "Path: ‘v1.1 current’ (1) or the Lock drawer (1).",
        "Cover (lock rule, one line), then its groups: FOLD@C, HUSH@B, ONE SHEET@B, each with its legacy sheets as images, then shared docs and spec as text rows."], "1 tap")
    version_phone(c, px, PY, "‹ Cabinet")
    # 7
    px = xs[6]
    c.phone(px, PY, "7 · Landing, signed-out snapshot", [
        "No lamp (a rule), ‘Snapshot · 13 Nov 14:02’, no dots, no unseen count. Everything else the same."], "0 taps")
    cab_phone_landing(c, px, PY, "snapshot", "Snapshot · 13 Nov 14:02", "14:02", snapshot=True)
    # 9 (tall)
    px = xs[8]
    tall_phone(c, px, PY, 1900, "9 · Concept group: BUTTERFLY rev A", [
        "Path: Newest (1). The whole scrolled page drawn; the fold mark shows the first screen.",
        "Images only where they're images (renders, a section drawing), each at its own shape, full width; everything else is HTML text from the group's how-it-works, in its order.",
        "Label + slip on top; ‘grew from ONE SHEET’ links to the legacy group."], "1 tap")
    x, y0 = px + 16, PY + TOP
    c.t(x, y0 + 30, "‹ Cabinet", 14, 500, INK2); c.t(x + 358, y0 + 30, "copy link", 13, 500, INK2, "end")
    group_page_phone(c, px, y0 + 48, PY + 1900)
    # 8 placeholder note
    px = xs[7]
    c.t(px, PY - 18, "8 · Desktop landing", 17, 700)
    c.r(px, PY, PW, 200, CELL); c.wrap(px + 16, PY + 30, "Frame 8 is desktop frame 1 in frames-desktop.png (all nine frames are drawn at 1440 × 900 there).", PW - 32, 14, 400, INK2, lh=21)
    # extra scrubbed
    px = xs[9]
    c.phone(px, PY, "Extra · scrubbed to Round 2 · #/h/round/2", [
        "Kept from round 1: the real case (his two finalists were 7s in R2). Own URL now."], "drag")
    scrubbed_phone(c, px, PY)
    c.save(os.path.join(ROOT, "site/design/concepts/cabinet/frames"))

    # ---------------- desktop
    c, pos = desk_sheet("C · Cabinet — round 2 · 9 frames at desktop (1440 × 900, 1:1)",
                        "Master–detail: the cabinet panel stays left (520); the right (792) is the work. Frame 8 = frame 1.", 8)
    RX, RW = 600, 792
    def left(dx, dy, state, line, dots=False, snapshot=False):
        lamp_and_name(c, dx + 48, dy + 48, state, line, 460, big=True)
        c.label(dx + 48, dy + 150, "Waiting on you"); c.t(dx + 48, dy + 174, "ONE SHEET or FOLD", 18, 600)
        cab(c, dx + 60, dy + 210, 460, rh=46, dots=dots, snapshot=snapshot, desktop=True)
        c.l(dx + 560, dy + 40, dx + 560, dy + DH - 120)
        cab_scrub(c, dx + 48, dy + DH - 86, DW - 96, dated=True)
    def newest_right(dx, dy, slip, unseen=False):
        c.label(dx + RX, dy + 52, "Newest")
        h = c.img("BF-main", dx + RX, dy + 64, RW, 470)
        yy = group_label(c, dx + RX, dy + 64 + 480, 420, unseen)
        c.wrap(dx + RX + 450, dy + 64 + 504, BF_LINE, 340, 15, 400, INK, lh=22)
        for i, k in enumerate(["BF-joint", "BF-wall", "BF-rear"]):
            c.img(k, dx + RX + 450 + i * 116, dy + 64 + 560, 108, 72)
        c.t(dx + RX + 450, dy + 64 + 650, "+ 3 more images · open group ›", 12.5, 500, INK2)
    dx, dy = pos[0]; shell(c, dx, dy, "1 / 8 · Landing, standby")
    left(dx, dy, "standby", "Standby · last BUTTERFLY rev A · 14:02"); newest_right(dx, dy, "14:02")
    dx, dy = pos[1]; shell(c, dx, dy, "2 · On — BUTTERFLY rev A lands")
    left(dx, dy, "dip", "On · branches round · since 13:40", dots=True); newest_right(dx, dy, "just now", True)
    c.t(dx + RX + RW, dy + 52, "1 unseen ›", 13, 600, INK, "end")
    # 3
    dx, dy = pos[2]; shell(c, dx, dy, "3 · FOLD-A v1.1 beside v1, changes on · 3 clicks")
    left(dx, dy, "standby", "Standby · last BUTTERFLY rev A · 14:02")
    c.t(dx + RX, dy + 52, "‹ v1.1", 14, 500, INK2); c.t(dx + RX + RW, dy + 52, "copy link", 13, 500, INK2, "end")
    gw = (RW - 20) / 2
    for i, (k, lab) in enumerate([("FOLD-A", "rev C · v1.1 · current"), ("FOLD-A@v1", "rev B · v1")]):
        xx = dx + RX + i * (gw + 20)
        h = c.img(k, xx, dy + 70, gw)
        for fx, fy, fw, fh in CLOUDS:
            c.cloud(xx + fx * gw - 2, dy + 70 + fy * h - 2, fw * gw + 4, min(fh * h + 4, h - fy * h), bump=3.2, sw=1)
        c.label(xx, dy + 70 + h + 18, lab, INK)
    show_changes(c, dx + RX, dy + 70 + h + 52, 360)
    yy = label(c, dx + RX, dy + 70 + h + 92, 380, "FOLD-A", "The look", "legacy sheet · Concept · locked in v1.1",
               [("rev C", "13 Nov · v1.1 · bend as joystick"), ("rev B", "13 Nov · v1 · first lock")], "+ rev A · r1–r4 not kept")
    lineage(c, dx + RX + 420, dy + 70 + h + 100, 80)
    # 4
    dx, dy = pos[3]; shell(c, dx, dy, "4 · Bass pluck · golden vs perturbed · 2 clicks")
    left(dx, dy, "standby", "Standby · last BUTTERFLY rev A · 14:02")
    c.t(dx + RX, dy + 52, "‹ Spec · tests", 14, 500, INK2)
    c.t(dx + RX, dy + 92, "T-004", 24, 700); c.t(dx + RX + 90, dy + 92, "Bass pluck", 22, 400)
    c.t(dx + RX, dy + 116, "test · Spec (early) · ran 13 Nov · RAN, no limits set · osc 110.0 Hz · env. peak 87 / 69 ms", 13, 400, INK2)
    test_block(c, dx + RX, dy + 136, RW, 170)
    c.img("PLOT-pluck", dx + RX + 136, dy + 324, 520)
    # 5
    dx, dy = pos[4]; shell(c, dx, dy, "5 · Decisions: “Switch to Daisy Seed” · 2 clicks + scroll")
    left(dx, dy, "standby", "Standby · last BUTTERFLY rev A · 14:02")
    c.t(dx + RX, dy + 60, "Decisions", 24, 600); c.t(dx + RX + RW, dy + 60, "45 · newest first", 13, 500, INK2, "end")
    decisions_list(c, dx + RX, dy + 96, RW, dy + DH - 120)
    # 6
    dx, dy = pos[5]; shell(c, dx, dy, "6 · What's in v1.1 · 1 click")
    left(dx, dy, "standby", "Standby · last BUTTERFLY rev A · 14:02")
    version_desktop(c, dx + RX, dy + 30, RW, cols=6)
    # 7
    dx, dy = pos[6]; shell(c, dx, dy, "7 · Landing, signed-out snapshot")
    left(dx, dy, "snapshot", "Snapshot · 13 Nov 14:02", snapshot=True); newest_right(dx, dy, "14:02")
    # 9
    dx, dy = pos[7]; shell(c, dx, dy, "9 · Concept group: BUTTERFLY rev A · 1 click")
    left(dx, dy, "standby", "Standby · last BUTTERFLY rev A · 14:02")
    c.t(dx + RX, dy + 52, "‹ Cabinet", 14, 500, INK2); c.t(dx + RX + RW, dy + 52, "copy link", 13, 500, INK2, "end")
    yy = group_label(c, dx + RX, dy + 66, 420)
    c.wrap(dx + RX + 450, dy + 90, BF_LINE, 340, 15, 400, INK, lh=22)
    head, paras, key, cap = BF_SECTIONS[0]
    yy = html_section(c, dx + RX, yy + 26, RW, head, paras, 14)
    h = c.img(key, dx + RX, yy, RW, 380)
    c.t(dx + RX, yy + 396, cap + " · the page continues: changes, the joint, construction, hanging", 12, 500, INK2)
    c.save(os.path.join(ROOT, "site/design/concepts/cabinet/frames-desktop"))

def version_phone(c, px, py, back):
    x, y0 = px + 16, py + TOP
    c.t(x, y0 + 30, back, 14, 500, INK2); c.t(x + 358, y0 + 30, "copy link", 13, 500, INK2, "end")
    c.l(x, y0 + 50, x + 358, y0 + 50, INK, 1.5); c.l(x, y0 + 54, x + 358, y0 + 54, INK, 1.5)
    c.t(x, y0 + 88, "v1.1", 26, 700); c.t(x + 70, y0 + 88, "current · locked 13 Nov", 13, 500, INK2)
    yy = c.wrap(x, y0 + 114, "v1, plus: FOLD stands at 120° so the face catches more light; bend drawn as a joystick in every view; FOLD sheet D shows MIDI IN.", 358, 13.5, 400, INK, lh=20)
    gy = yy + 8
    for grp, keys in [("FOLD · rev C · 5 legacy sheets", ["FOLD-A", "FOLD-B", "FOLD-C", "FOLD-D"]), ("HUSH · rev B · 4 legacy sheets", ["HUSH-A", "HUSH-B"])]:
        c.label(x, gy + 12, grp, INK); gy += 22
        for i, k in enumerate(keys):
            xx = x + (i % 2) * 183
            if i % 2 == 0 and i: gy += 146
            c.img(k, xx, gy, 175, 124); c.t(xx, gy + 138, k, 11.5, 700)
        gy += 156
    c.t(x, py + BOT - 14, "+ FOLD-E · HUSH-C, D · ONE SHEET · shared docs · spec rev 14", 12.5, 500, INK2)

def version_desktop(c, x, y, w, cols=5):
    c.l(x, y + 4, x + w, y + 4, INK, 1.5); c.l(x, y + 8, x + w, y + 8, INK, 1.5)
    c.t(x, y + 48, "v1.1", 30, 700); c.t(x + 80, y + 48, "current · locked 13 Nov", 14, 500, INK2)
    c.wrap(x, y + 76, "v1, plus: FOLD stands at 120° so the face catches more light; bend drawn as a joystick in every view; FOLD sheet D shows MIDI IN. The director held all three at 9.", w, 14, 400, INK, lh=21)
    gy = y + 130
    tw_ = (w - (cols - 1) * 10) / cols
    for grp, keys in [("FOLD · rev C", ["FOLD-A", "FOLD-B", "FOLD-C", "FOLD-D", "FOLD-E"]), ("HUSH · rev B", ["HUSH-A", "HUSH-B", "HUSH-C", "HUSH-D"]), ("ONE SHEET · rev B", ["ONESHEET-A", "ONESHEET-B", "ONESHEET-C", "ONESHEET-D"])]:
        c.label(x, gy, grp + " · legacy sheets", INK)
        for i, k in enumerate(keys[:cols]):
            c.img(k, x + i * (tw_ + 10), gy + 10, tw_, tw_ * 0.707); c.t(x + i * (tw_ + 10), gy + 26 + tw_ * 0.707, k, 11.5, 700)
        gy += tw_ * 0.707 + 46
    c.label(x, gy, "Shared docs · spec · records", INK)
    for i, (code, t1) in enumerate([("D-003", "Common how it works"), ("D-004", "Common looks and feels"), ("D-019", "Budget variant spec · rev 14"), ("R-001", "Owner record (as at the lock)")]):
        c.l(x, gy + 12 + i * 30, x + w, gy + 12 + i * 30)
        c.t(x, gy + 32 + i * 30, code, 13, 600); c.t(x + 70, gy + 32 + i * 30, t1, 13.5, 400)

def scrubbed_phone(c, px, py):
    y = py + TOP
    c.r(px, y + 8, PW, 36, INK)
    c.t(px + 16, y + 31, "As it stood · Round 2 · 12 Nov", 13, 600, WHITE); c.t(px + PW - 16, y + 31, "back to now ›", 13, 500, WHITE, "end")
    c.t(px + 16, y + 80, "( name to come )", 22, 600); c.t(px + 16, y + 102, "no version yet · six concepts in play", 13, 400, INK2)
    c.label(px + 16, y + 140, "Round 2 scores, then")
    ry = y + 154
    for n, sc, fate in [("TYPE CASE", "9", "set aside later"), ("HYMNAL", "9", "set aside later"), ("HUSH", "8", "locked in v1, v1.1"),
                        ("FOLD", "7", "now: one of your two"), ("ONE SHEET", "7", "now: one of your two"), ("UNDER GLASS", "6", "killed this round")]:
        st = "your two" in fate
        c.l(px + 16, ry, px + PW - 16, ry)
        c.t(px + 16, ry + 26, n, 14, 600 if st else 400, INK if st else INK2); c.t(px + 150, ry + 26, sc, 16, 600, INK if st else INK2)
        c.t(px + PW - 16, ry + 26, fate, 12.5, 600 if st else 400, INK if st else INK2, "end"); ry += 40
    c.l(px + 16, ry, px + PW - 16, ry)
    cab_scrub(c, px + 16, py + BOT - 70, 358, at=1)

# ================================================================ E · HERBARIUM
def herb_phone_landing(c, px, py, state, line, slip, unseen_line, mark=False):
    x, y0 = px + 16, py + TOP
    lamp_and_name(c, x, y0 + 26, state, line, 358)
    waiting_inline(c, x, y0 + 104)
    stage_strip(c, x, y0 + 120, 358)
    h = c.img("BF-main", x, y0 + 160, 358)
    yy = label(c, x, y0 + 160 + h + 10, 358, "BUTTERFLY", "rev A", "concept group · Concept · exploring",
               [("rev A", slip + " · branches round · first rev")], None, mark)
    c.t(x, yy + 12, "grew from ONE SHEET · v1.1 ›", 12, 500, INK2)
    c.t(x, yy + 40, unseen_line, 13, 600)
    ty = yy + 56
    c.label(x, ty + 10, "Newest of each kind")
    tw_ = 114; g = (358 - 3 * tw_) / 2
    c.img("CH-standing", x, ty + 20, tw_, 72); c.t(x, ty + 106, "image · CHAMBER", 11, 600)
    doc_tile(c, x + tw_ + g, ty + 20, tw_, 72, "D-032", "Daisy Seed, from first principles", size=11.5)
    c.t(x + tw_ + g, ty + 106, "doc · 13 Nov", 11, 600)
    test_tile(c, x + 2 * (tw_ + g), ty + 20, tw_, 72, "T-004", "RAN")
    c.t(x + 2 * (tw_ + g), ty + 106, "test · T-004", 11, 600)

def filters(c, x, y, w, sel, unseen=None):
    xx = x
    for f in ["all", "stage", "kind", "version", "decisions", "history"]:
        on = f == sel
        c.t(xx, y, f, 14, 600 if on else 400, INK if on else INK2)
        if on: c.r(xx, y + 6, tw(f, 14, 600), 2, INK)
        xx += tw(f, 14, 600) + 18
    if unseen: c.t(x + w, y, unseen, 14, 600, INK, "end")

def herbarium_sheets():
    c, xs, PY = phone_sheet("E · Herbarium — round 2 · 9 frames at phone (390 × 844, 1:1)",
                            "New-format work leads: BUTTERFLY rev A (branches round), real renders + HTML text. Doc tiles are real text. Show changes and the decisions register shared with C. Desktop frames: frames-desktop.png.")
    px = xs[0]
    c.phone(px, PY, "1 · Landing, standby", [
        "The newest work is a group, shown by its lead render at its own shape, full width. Its label is the group's: rev slip, one-line ‘grew from ONE SHEET’ link.",
        "Newest of each kind: CHAMBER's render (an image), D-032 as real text (code, title at 11.5/600), T-004 as its waveform + RAN.",
        "Fits 714 px with the level strip."], "0 taps")
    herb_phone_landing(c, px, PY, "standby", "Standby · last BUTTERFLY rev A · 14:02", "14:02", "+ 6 more since you last looked ›")
    px = xs[1]
    c.phone(px, PY, "2 · On — BUTTERFLY rev A lands", [
        "Lamp dips; the lead render cross-fades in; slip ‘rev A · just now’ lands on top of the label; unseen dot; ‘+ 7 more’.",
        "Not yet published: label + slip + ‘images arriving with the next publish’ in the image's place."], "0 taps")
    herb_phone_landing(c, px, PY, "dip", "On · branches round · since 13:40", "just now", "+ 7 more since you last looked ›", True)
    # 3
    px = xs[2]
    c.phone(px, PY, "3 · FOLD-A v1.1 → v1, changes on", [
        "Path: ‘v1.1 current’ (1) → FOLD-A (2) → rev B in lineage (3). Clouds on, from the real diff.",
        "Opened, the label's slips unfold."], "3 taps")
    x, y0 = px + 16, PY + TOP
    c.t(x, y0 + 30, "‹ v1.1", 14, 500, INK2); c.t(x + 358, y0 + 30, "copy link", 13, 500, INK2, "end")
    h = compare_wipe(c, x, y0 + 48, 358)
    c.label(x + 6, y0 + 48 + h + 16, "rev C · v1.1", INK); c.label(x + 352, y0 + 48 + h + 16, "rev B · v1", INK, "end")
    show_changes(c, x, y0 + 48 + h + 44, 358)
    yy = label(c, x, y0 + 48 + h + 82, 358, "FOLD-A", "The look", "legacy sheet · Concept · locked in v1.1",
               [("rev C", "13 Nov · v1.1 · bend drawn as a joystick"), ("rev B", "13 Nov · v1 · first lock"), ("rev A", "13 Nov · round 5 · archive")], "earlier revs (r1–r4) not kept")
    lineage(c, x, yy + 12)
    # 4
    px = xs[3]
    c.phone(px, PY, "4 · Bass pluck · golden vs perturbed", [
        "Path: test tile (1). The sound is the specimen; the result is the first slip."], "1 tap")
    x, y0 = px + 16, PY + TOP
    c.t(x, y0 + 30, "‹ all", 14, 500, INK2); c.t(x + 358, y0 + 30, "copy link", 13, 500, INK2, "end")
    test_block(c, x, y0 + 48, 358, 200)
    yy = label(c, x, y0 + 260, 358, "T-004", "Bass pluck", "test · Spec (early) · ran 13 Nov",
               [("rev A", "RAN · no limits set · osc 110.0 Hz"), ("", "env. peak 87 ms golden · 69 ms perturbed")])
    c.img("PLOT-pluck", x, yy + 12, 358, 220)
    # 5
    px = xs[4]
    c.phone(px, PY, "5 · Decisions: “Switch to Daisy Seed”", [
        "Path: filter ‘decisions’ (1) → scroll → a caused item (2). Same register as C (replaces round 1's doc cards)."], "2 taps + scroll")
    x, y0 = px + 16, PY + TOP
    filters(c, x, y0 + 32, 358, "decisions")
    c.l(px, y0 + 46, px + PW, y0 + 46)
    decisions_list(c, x, y0 + 74, 358, PY + BOT)
    # 6
    px = xs[5]
    c.phone(px, PY, "6 · What's in v1.1", ["Path: ‘v1.1 current’ (1). Cover, then groups with their legacy sheets, then shared docs as text."], "1 tap")
    version_phone(c, px, PY, "‹ all")
    # 7
    px = xs[6]
    c.phone(px, PY, "7 · Landing, signed-out snapshot", ["No lamp, no dot; ‘+ 6 more on 13 Nov’."], "0 taps")
    herb_phone_landing(c, px, PY, "snapshot", "Snapshot · 13 Nov 14:02", "14:02", "+ 6 more on 13 Nov ›")
    # 9 tall
    px = xs[8]
    tall_phone(c, px, PY, 1900, "9 · Concept group: BUTTERFLY rev A", [
        "Path: the newest work (1). Same group page as C's (shared): label, one line, then the doc as HTML with its images where it places them.",
        "The thing the owner asked for: images only where they're images; words as words."], "1 tap")
    x, y0 = px + 16, PY + TOP
    c.t(x, y0 + 30, "‹ all", 14, 500, INK2); c.t(x + 358, y0 + 30, "copy link", 13, 500, INK2, "end")
    group_page_phone(c, px, y0 + 48, PY + 1900)
    px = xs[7]
    c.t(px, PY - 18, "8 · Desktop landing", 17, 700)
    c.r(px, PY, PW, 200, CELL); c.wrap(px + 16, PY + 30, "Frame 8 is desktop frame 1 in frames-desktop.png (all nine frames are drawn at 1440 × 900 there).", PW - 32, 14, 400, INK2, lh=21)
    c.save(os.path.join(ROOT, "site/design/concepts/herbarium/frames"))

    # ---------------- desktop
    c, pos = desk_sheet("E · Herbarium — round 2 · 9 frames at desktop (1440 × 900, 1:1)",
                        "The work as large as the screen allows, the label in the bottom-right corner beside it. Frame 8 = frame 1.", 8)
    def head(dx, dy, state, line, sel="all", unseen="+ 6 more since you last looked ›"):
        lamp_and_name(c, dx + 48, dy + 44, state, line, 460, big=True)
        c.label(dx + 560, dy + 66, "Waiting on you"); c.t(dx + 560, dy + 90, "ONE SHEET or FOLD", 18, 600)
        stage_strip(c, dx + 860, dy + 70, 532)
        c.l(dx + 48, dy + 128, dx + DW - 48, dy + 128)
        filters(c, dx + 48, dy + 160, DW - 96, sel, unseen)
    def landing(dx, dy, state, line, slip, unseen, mark=False):
        head(dx, dy, state, line, unseen=unseen)
        h = c.img("BF-main", dx + 48, dy + 190, 940, 587)
        lx, lw = dx + 1020, 372
        c.label(lx, dy + 206, "Newest of each kind")
        c.img("CH-standing", lx, dy + 218, 180, 112); c.t(lx, dy + 346, "image · CHAMBER rev A", 11.5, 600)
        doc_tile(c, lx + 192, dy + 218, 180, 112, "D-032", "Daisy Seed, from first principles", "Every subsystem the Seed touches, re-derived.", size=12.5)
        c.t(lx + 192, dy + 346, "doc · 13 Nov", 11.5, 600)
        test_tile(c, lx, dy + 360, lw, 60, "T-004", "RAN · T-004 Bass pluck")
        yy = label(c, lx, dy + 590, lw, "BUTTERFLY", "rev A", "concept group · Concept · exploring",
                   [("rev A", slip + " · branches round")], None, mark)
        c.wrap(lx, yy + 18, BF_LINE, lw, 13.5, 400, INK, lh=19)
        c.t(lx, yy + 62, "grew from ONE SHEET · v1.1 ›", 12.5, 500, INK2)
        c.t(dx + 48, dy + 808, "Below: everything else, newest first, three across", 12.5, 400, INK2)
        for i, k in enumerate(["CH-standing", "DP-standing", "RN-main"]):
            c.img(k, dx + 48 + i * 456, dy + 822, 440, 78, crop=(0, 0, 1, 0.24))
    dx, dy = pos[0]; shell(c, dx, dy, "1 / 8 · Landing, standby")
    landing(dx, dy, "standby", "Standby · last BUTTERFLY rev A · 14:02", "14:02", "+ 6 more since you last looked ›")
    dx, dy = pos[1]; shell(c, dx, dy, "2 · On — BUTTERFLY rev A lands")
    landing(dx, dy, "dip", "On · branches round · since 13:40", "just now", "+ 7 more since you last looked ›", True)
    # 3
    dx, dy = pos[2]; shell(c, dx, dy, "3 · FOLD-A v1.1 beside v1, changes on · 3 clicks")
    c.t(dx + 48, dy + 52, "‹ v1.1", 14, 500, INK2); c.t(dx + DW - 48, dy + 52, "copy link", 13, 500, INK2, "end")
    gw = (1344 - 24) / 2
    for i, (k, lab) in enumerate([("FOLD-A", "rev C · v1.1 · current"), ("FOLD-A@v1", "rev B · v1")]):
        xx = dx + 48 + i * (gw + 24)
        h = c.img(k, xx, dy + 70, gw)
        for fx, fy, fw, fh in CLOUDS:
            c.cloud(xx + fx * gw - 3, dy + 70 + fy * h - 3, fw * gw + 6, min(fh * h + 6, h - fy * h), bump=5, sw=1.2)
        c.label(xx, dy + 70 + h + 18, lab, INK)
    show_changes(c, dx + 48, dy + 70 + h + 54, 400)
    label(c, dx + 48 + gw + 24, dy + 70 + h + 40, 640, "FOLD-A", "The look", "legacy sheet · Concept · locked in v1.1",
          [("rev C", "13 Nov · v1.1 · bend drawn as a joystick"), ("rev B", "13 Nov · v1 · first lock"), ("rev A", "13 Nov · round 5 · archive")], "earlier revs (r1–r4) not kept")
    lineage(c, dx + 48, dy + 70 + h + 100, 100)
    # 4
    dx, dy = pos[3]; shell(c, dx, dy, "4 · Bass pluck · golden vs perturbed · 1 click")
    c.t(dx + 48, dy + 52, "‹ all", 14, 500, INK2)
    test_block(c, dx + 48, dy + 72, 940, 340)
    label(c, dx + 1020, dy + 72 + 340 - 120, 372, "T-004", "Bass pluck", "test · Spec (early) · ran 13 Nov",
          [("rev A", "RAN · no limits set · 110.0 Hz"), ("", "env. peak 87 ms / 69 ms")])
    c.img("PLOT-pluck", dx + 48, dy + 440, 600)
    # 5
    dx, dy = pos[4]; shell(c, dx, dy, "5 · Decisions: “Switch to Daisy Seed” · 2 clicks + scroll")
    head(dx, dy, "standby", "Standby · last BUTTERFLY rev A · 14:02", sel="decisions", unseen=None)
    decisions_list(c, dx + 48, dy + 206, 900, dy + DH - 20)
    # 6
    dx, dy = pos[5]; shell(c, dx, dy, "6 · What's in v1.1 · 1 click")
    c.t(dx + 48, dy + 52, "‹ all  ·  filter: version", 14, 500, INK2); c.t(dx + DW - 48, dy + 52, "copy link", 13, 500, INK2, "end")
    version_desktop(c, dx + 48, dy + 64, 1344, cols=7)
    # 7
    dx, dy = pos[6]; shell(c, dx, dy, "7 · Landing, signed-out snapshot")
    landing(dx, dy, "snapshot", "Snapshot · 13 Nov 14:02", "14:02", "+ 6 more on 13 Nov ›")
    # 9
    dx, dy = pos[7]; shell(c, dx, dy, "9 · Concept group: BUTTERFLY rev A · 1 click")
    group_desktop(c, dx, dy, "‹ all")
    c.save(os.path.join(ROOT, "site/design/concepts/herbarium/frames-desktop"))

def group_desktop(c, dx, dy, back):
    c.t(dx + 48, dy + 52, back, 14, 500, INK2); c.t(dx + DW - 48, dy + 52, "copy link", 13, 500, INK2, "end")
    # label top right, line beside
    group_label(c, dx + 1020, dy + 70, 372)
    c.wrap(dx + 1020, dy + 200, BF_LINE, 372, 15, 400, INK, lh=22)
    # sections: image left (≤ 940), text right column beside the image it follows
    y = dy + 70
    head, paras, key, cap = BF_SECTIONS[0]
    c.t(dx + 48, y + 18, head, 18, 600)
    h = c.img(key, dx + 48, y + 34, 940, 500)
    c.t(dx + 48, y + 34 + 516, cap, 12, 500, INK2)
    c.wrap(dx + 1020, dy + 270, paras[0], 372, 14, 400, INK, lh=21)
    y2 = dy + 640
    head, paras, key, cap = BF_SECTIONS[1]
    c.t(dx + 1020, dy + 470, head, 16, 600)
    yy = dy + 496
    for p in paras: yy = c.wrap(dx + 1020, yy, p, 372, 13.5, 400, INK, lh=20) + 4
    c.img("BF-joint", dx + 48, y2, 460, 240); c.img("BF-rear", dx + 528, y2, 460, 240)
    c.t(dx + 48, y2 + 254, "the joint, close · render", 12, 500, INK2); c.t(dx + 528, y2 + 254, "rear section · drawing · 24 px/mm", 12, 500, INK2)

if __name__ == "__main__":
    w = sys.argv[1:] or ["c", "e"]
    if "c" in w: cabinet_sheets(); print("c ok")
    if "e" in w: herbarium_sheets(); print("e ok")
