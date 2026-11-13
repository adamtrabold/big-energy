"""Desktop frames 1-7 for C, D, E at 1:1 (1440 x 900). Owner 13 Nov: responsive, no size leads.
Output: ../<concept>/frames-desktop.{svg,png}. Frame 8 in each phone sheet is the same as frame 1 here.
"""
from lib import *

DW, DH = 1440, 900

def shell(c, dx, dy, title):
    c.t(dx, dy - 18, title, 18, 700)
    c.r(dx, dy, DW, DH, BG); c.r(dx - 0.5, dy - 0.5, DW + 1, DH + 1, "none", "#8f8c85")

def compare_pair(c, x, y, w, keyL, keyR, labL, labR):
    gw = (w - 24) / 2
    h = c.img(keyL, x, y, gw); c.img(keyR, x + gw + 24, y, gw)
    c.label(x, y + h + 18, labL, INK); c.label(x + gw + 24, y + h + 18, labR, INK)
    c.t(x + w, y + h + 18, "synced zoom · pan", 12, 500, INK2, "end")
    return y + h + 30

def audio(c, x, y, w, h=150, label_ab=True):
    c.r(x, y, w, h, CELL)
    c.play(x + 40, y + h * 0.42, playing=True)
    c.wave("perturbed", x + 80, y + h * 0.42, w - 240, h * 0.55)
    c.l(x + 80 + 0.31 * (w - 240), y + 12, x + 80 + 0.31 * (w - 240), y + h * 0.75, INK, 1.5)
    c.t(x + w - 20, y + h * 0.42 + 4, "0:00.6 / 0:01.98", 12.5, 500, INK2, "end")
    if label_ab:
        c.t(x + 24, y + h - 16, "golden", 14, 400, INK2); c.t(x + 96, y + h - 16, "perturbed", 14, 600)
        c.r(x + 96, y + h - 11, tw("perturbed", 14, 600), 2, INK)
        c.t(x + w - 20, y + h - 16, "peak 1.86 V (golden 1.05 V)", 12.5, 400, INK2, "end")
    return y + h

def decision_block(c, x, y, w):
    c.t(x, y, "you asked · 13 Nov", 12, 500, INK2)
    y = c.wrap(x, y + 22, "“Check the pin thing. Audio feels the most important since we're introducing digital stuff”", w, 15, 400, INK2, lh=22)
    c.l(x, y + 6, x + w, y + 6)
    c.t(x, y + 32, "you decided · 13 Nov · time not recorded", 12, 500, INK2)
    c.t(x, y + 60, "“Switch to Daisy Seed”", 20, 600)
    y = c.wrap(x, y + 88, "Daisy Seed replaces the Pico 2 as the one digital chip (control + echo/reverb). Dry voice stays analog.", w, 14, 400, INK2, lh=21)
    return y

CAUSED = [("D-031", "Pin check and audio-quality check", "before · the evidence", DAISY_PIN_TITLE, DAISY_PIN),
          ("D-032", "Daisy Seed, from first principles", "after · the redesign", DAISY_FP_TITLE, DAISY_FP),
          ("D-019", "Budget variant spec", "rev 13 · Daisy replaces Pico", SPEC_TITLE, SPEC)]

# ======================= C · Cabinet =======================
import importlib
def c_frames():
    import cabinet as C  # reuse cabinet() / DET drawing on its own canvas would duplicate; redraw here
    pass

def cab_left(c, dx, dy, state, line, dots=(), snapshot=False):
    from cabinet_parts import cabinet_grid
    c.lampline(dx + 48, dy + 48, state, line)
    c.t(dx + 48, dy + 92, "( name to come )", 28, 600)
    c.t(dx + 48, dy + 118, "a portable Model D · v1.1 current", 14, 400, INK2)
    c.label(dx + 48, dy + 160, "Waiting on you"); c.t(dx + 48, dy + 184, "ONE SHEET or FOLD", 18, 600)
    cabinet_grid(c, dx + 60, dy + 240, cw=92, rh=50, name_w=104, dots=dots, snapshot=snapshot)
    c.l(dx + 560, dy + 40, dx + 560, dy + DH - 130)

def cab_scrub(c, dx, dy, at=7):
    DET = ["R1 12 Nov", "R2 12 Nov", "R3 12 Nov", "R4 12 Nov", "R5 13 Nov", "v1 13 Nov", "v1.1 13 Nov", "now"]
    sx0, sx1, sy = dx + 60, dx + DW - 60, dy + DH - 70
    c.l(sx0, sy, sx1, sy, INK, 1.5)
    for i, d in enumerate(DET):
        xx = sx0 + i * (sx1 - sx0) / 7
        big = d.startswith("v") or d == "now"
        c.l(xx, sy - (10 if big else 6), xx, sy + (10 if big else 6), INK, 1.5 if big else 1)
        c.t(xx, sy + 30, d, 12.5, 600 if big else 400, INK if big else INK2, "middle")
    c.r(sx0 + at * (sx1 - sx0) / 7 - 8, sy - 16, 16, 32, INK)
    c.t(sx1, sy - 26, "history ›", 13, 500, INK2, "end")

def cabinet_desktop():
    c = Canvas(60 * 2 + 2 * DW + 80, 140 + 4 * (DH + 90))
    c.r(0, 0, c.W, c.H, WHITE)
    c.t(60, 60, "C · Cabinet — desktop frames 1–7, 1440 × 900 at 1:1", 30, 700)
    c.t(60, 92, "Master–detail: the cabinet never leaves the left; the right side is the work. Scrubber across the bottom.", 15, 400, INK2)
    pos = [(60 + (i % 2) * (DW + 80), 150 + (i // 2) * (DH + 90)) for i in range(7)]
    RX, RW = 600, 792
    # 1
    dx, dy = pos[0]; shell(c, dx, dy, "1 · Landing, standby")
    cab_left(c, dx, dy, "standby", "Standby · last FOLD-D rev C · 14:02")
    c.label(dx + RX, dy + 52, "Newest · FOLD-D · Front · rev C · 14:02")
    h = c.img("FOLD-D", dx + RX, dy + 66, RW)
    c.t(dx + RX, dy + 66 + h + 30, "FOLD-D · Front", 17, 600)
    c.t(dx + RX, dy + 66 + h + 52, "legacy sheet · Concept · rev C · 13 Nov · exploring · open ›", 13, 400, INK2)
    cab_scrub(c, dx, dy)
    # 2
    dx, dy = pos[1]; shell(c, dx, dy, "2 · On — FOLD-D rev C lands")
    cab_left(c, dx, dy, "dip", "On · round 6 sheets · since 13:40", dots={("Concept", 0), ("Concept", 1)})
    c.label(dx + RX, dy + 52, "Newest · FOLD-D · Front · rev C · just now", INK); c.dot(dx + RX + 330, dy + 48)
    c.t(dx + RX + RW, dy + 52, "3 unseen ›", 13, 600, INK, "end")
    h = c.img("FOLD-D", dx + RX, dy + 66, RW)
    c.t(dx + RX, dy + 66 + h + 30, "FOLD-D · Front", 17, 600)
    c.t(dx + RX, dy + 66 + h + 52, "legacy sheet · Concept · rev C · just now · exploring", 13, 400, INK2)
    cab_scrub(c, dx, dy)
    # 3
    dx, dy = pos[2]; shell(c, dx, dy, "3 · FOLD-A v1.1 beside its v1 form · 3 clicks")
    cab_left(c, dx, dy, "standby", "Standby · last FOLD-D rev C · 14:02")
    c.t(dx + RX, dy + 52, "‹ Concept · images", 14, 500, INK2); c.t(dx + RX + RW, dy + 52, "copy link", 13, 500, INK2, "end")
    y = compare_pair(c, dx + RX, dy + 70, RW, "FOLD-A", "FOLD-A@v1", "v1.1 · rev C · current", "v1 · rev B")
    c.t(dx + RX, y + 24, "FOLD-A · The look", 18, 600)
    c.t(dx + RX, y + 46, "legacy sheet · Concept · rev C · 13 Nov · locked in v1.1 · 4961 × 3508 (legacy A3) · download", 13, 400, INK2)
    ty = y + 66; tx = dx + RX
    for k, a, b in [("FOLD-A@r5", "rev A", "round 5 · archive"), (None, "r1–r4", "not kept"), ("FOLD-A@v1", "rev B", "v1 · shown right"), ("FOLD-A", "rev C", "v1.1 · shown left")]:
        if k:
            c.img(k, tx, ty, 120, 85); c.t(tx, ty + 102, a, 12, 600); c.t(tx, ty + 118, b, 12, 400, INK2); tx += 140
        else:
            c.l(tx + 4, ty + 42, tx + 64, ty + 42, RULE, 1, "3 3"); c.t(tx + 4, ty + 102, a, 12, 600, INK2); c.t(tx + 4, ty + 118, b, 12, 400, INK2); tx += 90
    cab_scrub(c, dx, dy)
    # 4
    dx, dy = pos[3]; shell(c, dx, dy, "4 · Bass pluck · golden vs perturbed · 2 clicks")
    cab_left(c, dx, dy, "standby", "Standby · last FOLD-D rev C · 14:02")
    c.t(dx + RX, dy + 52, "‹ Concept · tests", 14, 500, INK2)
    c.t(dx + RX, dy + 92, "T-006 · Bass pluck", 24, 600)
    c.t(dx + RX, dy + 116, "test · Concept · ran 13 Nov · RAN, no limits set · osc 110.0 Hz · envelope peak 87 ms golden, 69 ms perturbed", 13, 400, INK2)
    y = audio(c, dx + RX, dy + 136, RW, 160)
    c.img("PLOT-pluck", dx + RX + 136, y + 18, 520)
    cab_scrub(c, dx, dy)
    # 5
    dx, dy = pos[4]; shell(c, dx, dy, "5 · Find “Switch to Daisy Seed” · 2 clicks + scroll")
    cab_left(c, dx, dy, "standby", "Standby · last FOLD-D rev C · 14:02")
    c.t(dx + RX, dy + 52, "History · 13 Nov", 22, 600)
    for i, s in enumerate(["Day", "Round", "Version"]):
        xx = dx + RX + RW - 240 + i * 84
        c.t(xx, dy + 52, s, 14, 600 if i == 0 else 400, INK if i == 0 else INK2)
        if i == 0: c.r(xx, dy + 58, tw(s, 14, 600), 2, INK)
    y = decision_block(c, dx + RX, dy + 100, RW)
    c.label(dx + RX, y + 14, "It caused")
    ry = y + 26
    for code, t1, t2, _, _ in CAUSED:
        c.l(dx + RX, ry, dx + RX + RW, ry)
        c.t(dx + RX, ry + 26, code, 14, 600); c.t(dx + RX + 70, ry + 26, t1, 15, 500); c.t(dx + RX + 420, ry + 26, t2, 13, 400, INK2)
        ry += 44
    c.l(dx + RX, ry, dx + RX + RW, ry)
    cab_scrub(c, dx, dy, at=6)
    # 6
    dx, dy = pos[5]; shell(c, dx, dy, "6 · What's in v1.1 · 1 click")
    cab_left(c, dx, dy, "standby", "Standby · last FOLD-D rev C · 14:02")
    c.l(dx + RX, dy + 44, dx + RX + RW, dy + 44, INK, 1.5); c.l(dx + RX, dy + 48, dx + RX + RW, dy + 48, INK, 1.5)
    c.t(dx + RX, dy + 88, "v1.1", 30, 600); c.t(dx + RX + 80, dy + 88, "current · locked 13 Nov", 14, 500, INK2)
    c.wrap(dx + RX, dy + 118, "v1, plus: FOLD stands at 120° so the face catches more light; bend drawn as a joystick in every view; FOLD sheet D shows MIDI IN.", RW, 14, 400, INK, lh=21)
    gy = dy + 170
    for name, keys in [("FOLD", ["FOLD-A", "FOLD-B", "FOLD-C", "FOLD-D", "FOLD-E"]), ("HUSH", ["HUSH-A", "HUSH-B", "HUSH-C", "HUSH-D"]), ("ONE SHEET", ["ONESHEET-A", "ONESHEET-B", "ONESHEET-C", "ONESHEET-D"])]:
        c.label(dx + RX, gy, name, INK)
        for i, k in enumerate(keys):
            c.img(k, dx + RX + i * 158, gy + 10, 150, 106); c.t(dx + RX + i * 158, gy + 132, k, 11.5, 600)
        gy += 150
    c.t(dx + RX, gy + 6, "Docs and records: how it works ×3 · looks and feels ×3 · common ×2 · spec (as of the lock) · owner record · scores · notes", 13, 400, INK2)
    cab_scrub(c, dx, dy, at=6)
    # 7
    dx, dy = pos[6]; shell(c, dx, dy, "7 · Landing, signed-out snapshot")
    cab_left(c, dx, dy, "snapshot", "Snapshot · 13 Nov 14:02", snapshot=True)
    c.label(dx + RX, dy + 52, "Newest · FOLD-D · Front · rev C · 14:02")
    h = c.img("FOLD-D", dx + RX, dy + 66, RW)
    c.t(dx + RX, dy + 66 + h + 30, "FOLD-D · Front", 17, 600)
    cab_scrub(c, dx, dy)
    c.save(os.path.join(ROOT, "site/design/concepts/cabinet/frames-desktop"))

# ======================= D · The Set =======================
def set_title(c, x, y, w, state, st):
    c.r(x, y, w, 150, "none", INK, 1.2)
    c.t(x + 12, y + 30, "( name to come )", 21, 600); c.t(x + 12, y + 50, "a portable Model D", 12.5, 400, INK2)
    c.l(x, y + 64, x + w, y + 64, INK); c.l(x + w / 2, y + 64, x + w / 2, y + 150, INK); c.l(x, y + 107, x + w, y + 107, INK)
    c.label(x + 12, y + 80, "Status"); c.lamp(x + 17, y + 96, state)
    c.t(x + 30, y + 100, st, 13, 600 if state in ("on", "dip") else 500, INK if state in ("on", "dip") else INK2)
    c.label(x + w / 2 + 12, y + 80, "Current set"); c.t(x + w / 2 + 12, y + 100, "v1.1 · 13 Nov", 13.5, 600)
    c.label(x + 12, y + 123, "Waiting on you"); c.t(x + 12, y + 142, "ONE SHEET or FOLD", 14, 600)
    c.label(x + w / 2 + 12, y + 123, "Go to"); c.r(x + w / 2 + 12, y + 128, w / 2 - 24, 18, WHITE, RULE)
    c.t(x + w / 2 + 18, y + 141, "code, e.g. FOLD-A", 11.5, 400, INK2)

def set_revs(c, x, y, w, top=None):
    c.label(x, y, "Revisions"); c.t(x + w, y, "all (8) ›", 12.5, 500, INK2, "end")
    rows = ([top] if top else []) + [("v1.1", "13 Nov", "FOLD 120° · joystick in every view · MIDI IN", True), ("v1", "13 Nov", "first lock: HUSH, ONE SHEET, FOLD", False), ("R5", "13 Nov", "round 5 · 9 · 9 · 9", False)]
    yy = y + 12
    for rv, dt, ds, s in rows[:3]:
        c.l(x, yy, x + w, yy); c.t(x, yy + 22, rv, 13, 700 if s else 500, INK if s else INK2)
        c.t(x + 60, yy + 22, dt, 12.5, 400, INK2); c.t(x + 130, yy + 22, ds, 13, 500 if s else 400, INK if s else INK2)
        yy += 32
    c.l(x, yy, x + w, yy)

def set_top(c, dx, dy, state, st, top=None):
    set_title(c, dx + DW - 560, dy + 40, 520, state, st)
    set_revs(c, dx + 48, dy + 56, 760, top)

def set_index(c, dx, y, deltas=True, snapshot=False, extra=False):
    cols = [("Δ", 0), ("code", 30), ("title", 170), ("kind", 470), ("rev", 580), ("date", 650), ("status", 760), ("stage", 920)]
    c.label(dx + 48, y, "Index · Concept (112) · sheets" + ("   Δ = changed 13 Nov" if snapshot else ""), INK)
    for n, ox in cols: c.label(dx + 48 + ox, y + 30, n)
    rows = [(1, "FOLD-D", "Front", "sheet", "C", "13 Nov", "exploring"), (1 if not extra else 0, "FOLD-A", "The look", "sheet", "C", "13 Nov", "locked in v1.1"),
            (0, "FOLD-B", "Real size", "sheet", "C", "13 Nov", "locked in v1.1"), (0, "FOLD-C", "Construction", "sheet", "C", "13 Nov", "locked in v1.1"),
            (0, "FOLD-E", "Standing", "sheet", "C", "13 Nov", "locked in v1.1"), (1, "HUSH-A", "The look", "sheet", "B", "13 Nov", "locked in v1.1"),
            (0, "HUSH-B", "Real size", "sheet", "B", "13 Nov", "locked in v1.1"), (0, "ONESHEET-A", "The look", "sheet", "B", "13 Nov", "locked in v1.1"),
            (0, "FOLD113-A", "The look (113)", "sheet", "A", "13 Nov", "dropped"), (0, "TYPECASE-A", "The look", "sheet", "A", "12 Nov", "dropped")]
    ry = y + 40
    for d, *v in rows:
        c.l(dx + 48, ry, dx + DW - 48, ry)
        op = 0.4 if v[5] == "dropped" else 1
        if d and deltas: c.delta(dx + 56, ry + 15, None, 7)
        for (n, ox), val in zip(cols[1:], v + ["Concept"]):
            c.t(dx + 48 + ox, ry + 22, val, 13.5, 600 if n == "code" else 400, INK if n in ("code", "title") else INK2, op=op)
        ry += 34
    c.l(dx + 48, ry, dx + DW - 48, ry)
    c.t(dx + 48, ry + 30, "Diagrams (22) ›   Docs (38) ›   Tests (7) ›   · Lock · Handoff · Spec · BOM · Breadboard · Boards · Prints · Assembly · Records", 13.5, 500, INK2)

def set_desktop():
    c = Canvas(60 * 2 + 2 * DW + 80, 140 + 4 * (DH + 90))
    c.r(0, 0, c.W, c.H, WHITE)
    c.t(60, 60, "D · The Set — desktop frames 1–7, 1440 × 900 at 1:1", 30, 700)
    c.t(60, 92, "Title block top right, revisions top left; the index (or the open item) fills the rest. Textual until an item opens.", 15, 400, INK2)
    pos = [(60 + (i % 2) * (DW + 80), 150 + (i // 2) * (DH + 90)) for i in range(7)]
    dx, dy = pos[0]; shell(c, dx, dy, "1 · Landing, standby")
    set_top(c, dx, dy, "standby", "Standby · last FOLD-D rev C · 14:02"); set_index(c, dx, dy + 230)
    dx, dy = pos[1]; shell(c, dx, dy, "2 · On — FOLD-D rev C lands")
    set_top(c, dx, dy, "dip", "On · round 6 sheets · since 13:40", top=("Today", "now", "in progress · FOLD-D rev C", True)); set_index(c, dx, dy + 230)
    # 3
    dx, dy = pos[2]; shell(c, dx, dy, "3 · FOLD-A v1.1 vs v1, changes clouded · 3 clicks")
    c.t(dx + 48, dy + 52, "‹ Index", 14, 500, INK2)
    c.t(dx + 48, dy + 92, "FOLD-A", 26, 700); c.t(dx + 160, dy + 92, "The look", 22, 400)
    c.t(dx + 48, dy + 116, "legacy sheet · Concept · rev C · locked in v1.1 · legacy A3", 13, 400, INK2)
    iy = dy + 136; w = 900
    h = c.img("FOLD-A", dx + 48, iy, w)
    CL = [(0.813, 0.178, 0.048, 0.068), (0.668, 0.219, 0.048, 0.082), (0.116, 0.328, 0.048, 0.082), (0.194, 0.410, 0.068, 0.109), (0.629, 0.835, 0.184, 0.096), (0.610, 0.944, 0.348, 0.055)]
    for fx, fy, fw, fh in CL:
        c.cloud(dx + 48 + fx * w - 3, iy + fy * h - 3, fw * w + 6, min(fh * h + 6, h - fy * h), bump=6)
    rx = dx + 990
    c.t(rx, iy + 14, "Show changes from rev B", 14, 600); c.r(rx + 330, iy, 44, 20, INK); c.circle(rx + 364, iy + 10, 7, WHITE)
    c.t(rx, iy + 36, "6 changed areas (joystick, closed view, effects text, footer)", 12.5, 400, INK2)
    c.label(rx, iy + 76, "Revisions of FOLD-A")
    ry = iy + 88
    for rv, dt, ds, act in [("C", "13 Nov", "v1.1 · bend as joystick", "shown"), ("B", "13 Nov", "v1 · first lock", "compare ›"), ("A", "13 Nov", "round 5 · archive", ""), ("—", "", "r1–r4 not kept", "")]:
        c.l(rx, ry, rx + 400, ry); c.t(rx, ry + 23, rv, 14, 700 if rv == "C" else 500, INK if rv == "C" else INK2)
        c.t(rx + 30, ry + 23, dt, 12.5, 400, INK2); c.t(rx + 96, ry + 23, ds, 13, 400, INK if rv in "CB" else INK2)
        c.t(rx + 400, ry + 23, act, 12.5, 600 if act.startswith("c") else 400, INK if act.startswith("c") else INK2, "end"); ry += 34
    c.l(rx, ry, rx + 400, ry)
    c.t(rx, ry + 34, "Compare opens v1 beside v1.1 at full width,", 12.5, 400, INK2); c.t(rx, ry + 52, "clouds on both.", 12.5, 400, INK2)
    # 4
    dx, dy = pos[3]; shell(c, dx, dy, "4 · Bass pluck · golden vs perturbed · 2 clicks")
    c.t(dx + 48, dy + 52, "‹ Index · Concept · tests", 14, 500, INK2)
    c.t(dx + 48, dy + 92, "T-006", 26, 700); c.t(dx + 140, dy + 92, "Bass pluck", 22, 400)
    c.t(dx + 48, dy + 116, "test · Concept · rev A · 13 Nov · RAN, no limits set · osc 110.0 Hz", 13, 400, INK2)
    c.label(dx + 48, dy + 160, "Runs"); c.label(dx + 300, dy + 160, "peak"); c.label(dx + 420, dy + 160, "env. peak")
    ry = dy + 170
    for v, pk, en, on in [("golden", "1.05 V", "87 ms", False), ("perturbed", "1.86 V", "69 ms", True)]:
        c.l(dx + 48, ry, dx + 640, ry)
        if on: c.r(dx + 48, ry + 1, 3, 34, INK)
        c.t(dx + 60, ry + 23, v, 14, 600 if on else 400, INK if on else INK2); c.t(dx + 300, ry + 23, pk, 13.5, 500); c.t(dx + 420, ry + 23, en, 13.5, 500)
        c.t(dx + 640, ry + 23, "playing" if on else "play", 12.5, 600 if on else 400, INK if on else INK2, "end"); ry += 36
    c.l(dx + 48, ry, dx + 640, ry)
    audio(c, dx + 48, ry + 24, 592, 150, label_ab=False)
    c.img("PLOT-pluck", dx + 700, dy + 150, 680)
    # 5
    dx, dy = pos[4]; shell(c, dx, dy, "5 · Find “Switch to Daisy Seed” · 3 clicks")
    c.t(dx + 48, dy + 52, "‹ Records", 14, 500, INK2)
    c.t(dx + 48, dy + 92, "Decisions", 26, 700); c.t(dx + 220, dy + 92, "R-001 · 45 rows · newest first", 14, 500, INK2)
    cols = [("date", 0), ("his words, verbatim", 100), ("caused", 860), ("time", 1180)]
    for n, ox in cols: c.label(dx + 48 + ox, dy + 140, n)
    rows = [("13 Nov", "“i think it needs its own switch but yes now i want it”", "D-019 rev 14 · D-034", "not recorded", False),
            ("13 Nov", "“Add MIDI out”", "D-019", "not recorded", False),
            ("13 Nov", "“Also the key thing you need to port - go back to first principles and see if there's a better way with Daisy seed…”", "D-032", "not recorded", False),
            ("13 Nov", "“Switch to Daisy Seed”", "D-031 · D-032 · D-019 rev 13", "not recorded", True),
            ("13 Nov", "“Check the pin thing. Audio feels the most important since we're introducing digital stuff”", "D-031", "not recorded", False),
            ("13 Nov", "“I like the idea of drift, but I'd want it to be controllable”", "D-019", "not recorded", False)]
    ry = dy + 150
    for dt, wd, cs, tm, op in rows:
        c.l(dx + 48, ry, dx + DW - 48, ry)
        c.t(dx + 48, ry + 26, dt, 13, 500, INK2)
        c.wrap(dx + 148, ry + 26, wd, 720, 15 if op else 14, 600 if op else 400, INK if op else INK2, maxlines=1)
        c.t(dx + 908, ry + 26, cs, 13, 600 if op else 500, INK if op else INK2); c.t(dx + 1228, ry + 26, tm, 12.5, 400, INK2)
        if op:
            yy = ry + 52
            for code, t1, t2, _, _ in CAUSED:
                c.t(dx + 148, yy, code, 13, 700); c.t(dx + 210, yy, t1 + " · " + t2, 13, 400); c.l(dx + 210, yy + 3, dx + 210 + tw(t1 + " · " + t2, 13), yy + 3, INK, 0.6); yy += 24
            ry = yy + 6
        else:
            ry += 42
    c.l(dx + 48, ry, dx + DW - 48, ry)
    # 6
    dx, dy = pos[5]; shell(c, dx, dy, "6 · What's in v1.1 · 1 click")
    c.t(dx + 48, dy + 52, "‹ Index", 14, 500, INK2)
    c.t(dx + 48, dy + 98, "v1.1", 32, 700); c.t(dx + 140, dy + 98, "locked 13 Nov · current", 14, 500, INK2)
    c.l(dx + 48, dy + 114, dx + DW - 48, dy + 114, INK, 1.5); c.l(dx + 48, dy + 118, dx + DW - 48, dy + 118, INK, 1.5)
    c.t(dx + 48, dy + 146, "v1, plus: FOLD stands at 120°; bend drawn as a joystick in every view; FOLD sheet D shows MIDI IN. The director held all three at 9.", 14, 400)
    colx = [dx + 48, dx + 508, dx + 968]
    for ci, (grp, items) in enumerate([("FOLD", [("FOLD-A", "The look", "C"), ("FOLD-B", "Real size", "C"), ("FOLD-C", "Construction", "C"), ("FOLD-D", "Front", "B"), ("FOLD-E", "Standing", "C")]),
                                       ("HUSH", [("HUSH-A", "The look", "B"), ("HUSH-B", "Real size", "B"), ("HUSH-C", "Construction", "A"), ("HUSH-D", "Front", "B")]),
                                       ("ONE SHEET", [("ONESHEET-A", "The look", "B"), ("ONESHEET-B", "Real size", "B"), ("ONESHEET-C", "Construction", "A"), ("ONESHEET-D", "Front", "B")])]):
        x = colx[ci]; ry = dy + 190
        c.label(x, ry, grp, INK); ry += 12
        for code, t1, rv in items:
            c.l(x, ry, x + 420, ry); c.t(x, ry + 22, code, 13.5, 600); c.t(x + 130, ry + 22, t1, 13.5, 400); c.t(x + 420, ry + 22, "rev " + rv, 12.5, 400, INK2, "end"); ry += 34
        c.l(x, ry, x + 420, ry)
    c.label(dx + 48, dy + 430, "Docs and records", INK)
    ry = dy + 442
    for code, t1 in [("D-011", "How it works · FOLD"), ("D-012", "Looks and feels · FOLD"), ("D-013", "How it works · HUSH"), ("D-019", "Budget variant spec · rev 12 (as of the lock)"), ("R-001", "Owner record"), ("R-002", "Scores")]:
        c.l(dx + 48, ry, dx + 880, ry); c.t(dx + 48, ry + 22, code, 13.5, 600); c.t(dx + 130, ry + 22, t1, 13.5, 400); ry += 34
    c.l(dx + 48, ry, dx + 880, ry)
    # 7
    dx, dy = pos[6]; shell(c, dx, dy, "7 · Landing, signed-out snapshot")
    set_top(c, dx, dy, "snapshot", "Snapshot · 13 Nov 14:02"); set_index(c, dx, dy + 230, snapshot=True)
    c.save(os.path.join(ROOT, "site/design/concepts/the-set/frames-desktop"))

# ======================= E · Herbarium =======================
STAGES = ["Concept", "Lock", "Handoff", "Spec", "BOM", "Breadboard", "Boards", "Prints", "Assembly"]
def herb_head(c, dx, dy, state, line, unseen="+ 6 more since you last looked ›"):
    c.lampline(dx + 48, dy + 44, state, line)
    c.t(dx + 48, dy + 84, "( name to come )", 26, 600)
    c.t(dx + 48, dy + 108, "a portable Model D · v1.1 current", 14, 400, INK2)
    c.label(dx + 560, dy + 66, "Waiting on you"); c.t(dx + 560, dy + 90, "ONE SHEET or FOLD", 18, 600)
    sx, sw = dx + 860, (532 - 8 * 5) / 9
    for i in range(9):
        x = sx + i * (sw + 5)
        if i <= 1: c.r(x, dy + 70, sw, 6, INK)
        elif i == 3: c.r(x, dy + 70, sw, 6, "none", INK2)
        else: c.r(x, dy + 70, sw, 6, RULE)
    c.t(sx, dy + 98, "Lock · 2 of 9 · Spec begun early · next Handoff", 13, 500, INK2)
    c.l(dx + 48, dy + 128, dx + DW - 48, dy + 128)
    x = dx + 48
    for f in ["all", "stage", "kind", "version", "decisions", "history"]:
        c.t(x, dy + 160, f, 14, 600 if f == "all" else 400, INK if f == "all" else INK2)
        if f == "all": c.r(x, dy + 166, tw(f, 14, 600), 2, INK)
        x += tw(f, 14, 600) + 22
    if unseen: c.t(dx + DW - 48, dy + 160, unseen, 14, 600, INK, "end")

def herb_label(c, x, y, w, code, title, fields, slips, more=None, unseen=False):
    c.l(x, y, x + w, y, INK)
    c.t(x, y + 26, code, 17, 700); c.t(x + tw(code, 17, 700) + 10, y + 26, title, 17, 400)
    if unseen: c.dot(x + w - 4, y + 20)
    c.t(x, y + 50, fields, 13, 400, INK2)
    yy = y + 64
    for i, (rv, t) in enumerate(slips):
        c.r(x, yy, w, 28, PAGE if i == 0 else "none", RULE)
        c.t(x + 10, yy + 19, "rev " + rv, 12.5, 700 if i == 0 else 500, INK if i == 0 else INK2)
        c.t(x + 64, yy + 19, t, 12.5, 500 if i == 0 else 400, INK if i == 0 else INK2); yy += 31
    if more: c.t(x + 10, yy + 14, more, 12, 500, INK2); yy += 20
    return yy

def herb_landing(c, dx, dy, state, line, slip0, unseen_text="+ 6 more since you last looked ›", mark=False):
    herb_head(c, dx, dy, state, line, unseen_text)
    # specimen large left, label in the bottom-right corner (desktop)
    w = 940
    h = c.img("FOLD-D", dx + 48, dy + 190, w, 560)
    lx = dx + 48 + w + 32; lw = dx + DW - 48 - lx
    herb_label(c, lx, dy + 190 + 560 - 190, lw, "FOLD-D", "Front", "legacy sheet · Concept · exploring",
               [("C", slip0), ("B", "13 Nov · v1.1 · shows MIDI IN")], "+ rev A (v1) · r1–r4 not kept", unseen=mark)
    # newest of each kind row
    c.label(lx, dy + 206, "Newest of each kind")
    tw_ = (lw - 12) / 2
    c.img("SKETCH", lx, dy + 218, tw_, 100); c.t(lx, dy + 334, "image · G-021", 11.5, 600)
    doc_page(c, lx + tw_ + 12, dy + 218, tw_, 100, "Daisy Seed, from first principles", DAISY_FP[:2], size=6.5); c.t(lx + tw_ + 12, dy + 334, "doc · D-032", 11.5, 600)
    c.r(lx, dy + 350, lw, 60, CELL); c.wave("golden", lx + 12, dy + 380, lw - 24, 40, n=60, sw=1); c.t(lx, dy + 426, "test · T-007", 11.5, 600)
    # next row peeks
    c.t(dx + 48, dy + 790, "Below: everything else, newest first, 3 across.", 13, 400, INK2)
    for i, k in enumerate(["FOLD-E", "HUSH-A", "ONESHEET-A"]):
        c.img(k, dx + 48 + i * 456, dy + 806, 440, 94, crop=(0, 0, 1, 0.3))

def herb_desktop():
    c = Canvas(60 * 2 + 2 * DW + 80, 140 + 4 * (DH + 90))
    c.r(0, 0, c.W, c.H, WHITE)
    c.t(60, 60, "E · Herbarium — desktop frames 1–7, 1440 × 900 at 1:1", 30, 700)
    c.t(60, 92, "Reshaped for the owner's ‘responsive, no size leads’: no fixed 600 px column. The work is as large as the screen allows; the label sits in the bottom-right corner beside it (below it on a phone).", 15, 400, INK2)
    pos = [(60 + (i % 2) * (DW + 80), 150 + (i // 2) * (DH + 90)) for i in range(7)]
    dx, dy = pos[0]; shell(c, dx, dy, "1 · Landing, standby")
    herb_landing(c, dx, dy, "standby", "Standby · last FOLD-D rev C · 14:02", "14:02 · round 6")
    dx, dy = pos[1]; shell(c, dx, dy, "2 · On — FOLD-D rev C lands")
    herb_landing(c, dx, dy, "dip", "On · round 6 sheets · since 13:40", "just now · round 6", "+ 7 more since you last looked ›", mark=True)
    # 3
    dx, dy = pos[2]; shell(c, dx, dy, "3 · FOLD-A v1.1 beside its v1 form · 3 clicks")
    c.t(dx + 48, dy + 52, "‹ v1.1", 14, 500, INK2); c.t(dx + DW - 48, dy + 52, "copy link", 13, 500, INK2, "end")
    y = compare_pair(c, dx + 48, dy + 72, 1344, "FOLD-A", "FOLD-A@v1", "rev C · v1.1 · current", "rev B · v1")
    herb_label(c, dx + 48, y + 14, 640, "FOLD-A", "The look", "legacy sheet · Concept · locked in v1.1 · legacy A3",
               [("C", "13 Nov · v1.1 · bend drawn as a joystick"), ("B", "13 Nov · v1 · first lock"), ("A", "13 Nov · round 5 · archive")], "earlier revs (r1–r4) not kept")
    tx = dx + 740; ty = y + 30
    c.label(tx, ty - 6, "Lineage")
    for k, a in [("FOLD-A@r5", "rev A"), (None, "r1–r4"), ("FOLD-A@v1", "rev B"), ("FOLD-A", "rev C")]:
        if k:
            c.img(k, tx, ty + 6, 140, 99)
            if a == "rev B": c.r(tx - 2, ty + 4, 144, 103, "none", INK, 2)
            c.t(tx, ty + 124, a, 12, 600); tx += 156
        else:
            c.l(tx + 4, ty + 55, tx + 60, ty + 55, RULE, 1, "3 3"); c.t(tx + 4, ty + 124, "not kept", 12, 400, INK2); tx += 76
    # 4
    dx, dy = pos[3]; shell(c, dx, dy, "4 · Bass pluck · golden vs perturbed · 1–3 clicks")
    c.t(dx + 48, dy + 52, "‹ tests", 14, 500, INK2)
    audio(c, dx + 48, dy + 72, 940, 360)
    herb_label(c, dx + 1020, dy + 72 + 360 - 160, 372, "T-006", "Bass pluck", "test · Concept · ran 13 Nov",
               [("A", "RAN · no limits set · 110.0 Hz"), ("—", "env. peak 87 ms / 69 ms")])
    c.img("PLOT-pluck", dx + 48, dy + 460, 560)
    # 5
    dx, dy = pos[4]; shell(c, dx, dy, "5 · Find “Switch to Daisy Seed” · 2 clicks + scroll")
    herb_head(c, dx, dy, "standby", "Standby · last FOLD-D rev C · 14:02", None)
    c.r(dx + 48 + tw("all", 14, 600) + 22 + tw("stage", 14, 600) + 22 + tw("kind", 14, 600) + 22 + tw("version", 14, 600) + 22, dy + 166, tw("decisions", 14, 600), 2, INK)
    c.label(dx + 48, dy + 206, "13 Nov", INK)
    cw = (940 - 24) / 3
    for i, (code, t1, t2, tt, lines) in enumerate(CAUSED):
        x = dx + 48 + i * (cw + 12)
        doc_page(c, x, dy + 220, cw, 400, tt, lines, size=13)
        c.t(x, dy + 644, code, 13, 700); c.t(x + 56, dy + 644, t2, 13, 400, INK2)
    lx = dx + 1020; lw = 372
    c.l(lx, dy + 450, lx + lw, dy + 450, INK)
    c.t(lx, dy + 480, "“Switch to Daisy Seed”", 20, 600)
    c.t(lx, dy + 504, "decision · Concept · 13 Nov", 13, 400, INK2)
    c.t(lx, dy + 522, "time not recorded", 13, 400, INK2)
    c.r(lx, dy + 536, lw, 50, PAGE, RULE)
    c.wrap(lx + 10, dy + 556, "asked: “Check the pin thing. Audio feels the most important since we're introducing digital stuff”", lw - 20, 12, 500, INK, lh=17, maxlines=2)
    c.l(dx + 48, dy + 680, dx + DW - 48, dy + 680)
    c.label(dx + 48, dy + 706, "13 Nov"); c.t(dx + 48, dy + 734, "“Add MIDI out”", 16, 600, INK2); c.t(dx + 48, dy + 756, "decision · caused D-019 edit", 13, 400, INK2)
    # 6
    dx, dy = pos[5]; shell(c, dx, dy, "6 · What's in v1.1 · 1 click")
    c.t(dx + 48, dy + 52, "‹ all", 14, 500, INK2)
    c.l(dx + 48, dy + 70, dx + DW - 48, dy + 70, INK, 1.5); c.l(dx + 48, dy + 74, dx + DW - 48, dy + 74, INK, 1.5)
    c.t(dx + 48, dy + 116, "v1.1", 32, 700); c.t(dx + 140, dy + 116, "locked 13 Nov · current", 14, 500, INK2)
    c.t(dx + 48, dy + 146, "v1, plus: FOLD stands at 120°; bend drawn as a joystick in every view; FOLD sheet D shows MIDI IN.", 14, 400)
    gy = dy + 176
    for grp, keys in [("FOLD · 5 sheets", ["FOLD-A", "FOLD-B", "FOLD-C", "FOLD-D", "FOLD-E"]), ("HUSH · 4 sheets", ["HUSH-A", "HUSH-B", "HUSH-C", "HUSH-D"]), ("ONE SHEET · 4 sheets", ["ONESHEET-A", "ONESHEET-B", "ONESHEET-C", "ONESHEET-D"])]:
        c.label(dx + 48, gy, grp, INK)
        for i, k in enumerate(keys):
            c.img(k, dx + 48 + i * 270, gy + 10, 258, 182 * 0.7, crop=(0, 0, 1, 0.7)) if False else c.img(k, dx + 48 + i * 270, gy + 10, 258)
            c.t(dx + 48 + i * 270, gy + 202, k, 12, 700)
        gy += 226
    # 7
    dx, dy = pos[6]; shell(c, dx, dy, "7 · Landing, signed-out snapshot")
    herb_landing(c, dx, dy, "snapshot", "Snapshot · 13 Nov 14:02", "14:02 · round 6", "+ 6 more on 13 Nov ›")
    c.save(os.path.join(ROOT, "site/design/concepts/herbarium/frames-desktop"))

if __name__ == "__main__":
    import sys
    which = sys.argv[1:] or ["c", "d", "e"]
    if "c" in which: cabinet_desktop(); print("c ok")
    if "d" in which: set_desktop(); print("d ok")
    if "e" in which: herb_desktop(); print("e ok")
