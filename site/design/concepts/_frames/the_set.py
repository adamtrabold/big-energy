"""D · The Set — 8 frames. Output: ../the-set/frames.{svg,png}"""
from lib import *

GAP = 64
W = 60 * 2 + 7 * PW + 6 * GAP
H = 150 + PH + 250 + 900 + 80
c = Canvas(W, H)
c.r(0, 0, W, H, WHITE)
c.t(60, 64, "D · The Set — how it looks and feels · 8 frames", 30, 700)
c.t(60, 96, "Phones 1:1 inside browser chrome (714 px usable). Stays textual until an item opens. Revision clouds drawn from a real pixel diff of FOLD-A v1 → v1.1. D-codes illustrative; counts approximate.", 15, 400, INK2)
X = [60 + i * (PW + GAP) for i in range(7)]
PY = 170

SECTIONS = [("Concept", "112", 3), ("Lock", "v1.1 · 2 versions", 0), ("Handoff", "not yet", 0), ("Spec", "19", 0), ("BOM", "not yet", 0),
            ("Breadboard", "not yet", 0), ("Boards", "not yet", 0), ("Prints", "not yet", 0), ("Assembly", "not yet", 0), ("Records", "14", 1)]

def titleblock(px, y, state, statustext, w=PW - 32, x=None):
    x = px + 16 if x is None else x
    c.r(x, y, w, 150, "none", INK, 1.2)
    c.t(x + 12, y + 30, "( name to come )", 21, 600)
    c.t(x + 12, y + 50, "a portable Model D", 12.5, 400, INK2)
    c.l(x, y + 64, x + w, y + 64, INK, 1)
    c.l(x + w * 0.5, y + 64, x + w * 0.5, y + 150, INK, 1)
    c.l(x, y + 107, x + w, y + 107, INK, 1)
    c.label(x + 12, y + 80, "Status")
    c.lamp(x + 17, y + 96, state)
    c.t(x + 30, y + 100, statustext, 13, 600 if state in ("on", "dip") else 500, INK if state in ("on", "dip") else INK2)
    c.label(x + w * 0.5 + 12, y + 80, "Current set")
    c.t(x + w * 0.5 + 12, y + 100, "v1.1 · 13 Nov", 13.5, 600)
    c.label(x + 12, y + 123, "Waiting on you")
    c.t(x + 12, y + 142, "ONE SHEET or FOLD", 14, 600)
    c.label(x + w * 0.5 + 12, y + 123, "Go to")
    c.r(x + w * 0.5 + 12, y + 128, w * 0.5 - 24, 18, WHITE, RULE)
    c.t(x + w * 0.5 + 18, y + 141, "code, e.g. FOLD-A", 11.5, 400, INK2)
    return y + 150

def revisions(px, y, top=None, w=PW - 32, x=None):
    x = px + 16 if x is None else x
    c.label(x, y, "Revisions"); c.t(x + w, y, "all (8) ›", 12.5, 500, INK2, "end")
    rows = ([top] if top else []) + [("v1.1", "13 Nov", "FOLD 120° · joystick in every view · MIDI IN", True),
                                      ("v1", "13 Nov", "first lock: HUSH, ONE SHEET, FOLD", False),
                                      ("R5", "13 Nov", "round 5 · 9 · 9 · 9", False)]
    rows = rows[:3]
    yy = y + 12
    for rv, dt, ds, strong in rows:
        c.l(x, yy, x + w, yy)
        c.t(x, yy + 22, rv, 13, 700 if strong else 500, INK if strong else INK2)
        c.t(x + 50, yy + 22, dt, 12.5, 400, INK2)
        c.wrap(x + 108, yy + 22, ds, w - 108, 12.5, 500 if strong else 400, INK if strong else INK2, maxlines=1)
        yy += 32
    c.l(x, yy, x + w, yy)
    return yy

def sections(px, y, deltas=True, bump=0, w=PW - 32, x=None, rh=33):
    x = px + 16 if x is None else x
    c.label(x, y, "Index by stage")
    yy = y + 12
    for i, (n, cnt, d) in enumerate(SECTIONS):
        if n == "Concept": d += bump
        future = cnt == "not yet"
        c.l(x, yy, x + w, yy)
        c.t(x + (22 if True else 0), yy + 22, n, 13.5, 600 if n == "Lock" else 400, INK2 if future else INK)
        if n == "Lock": c.r(x, yy + 8, 3, rh - 16, INK)
        c.t(x + w - 40, yy + 22, cnt, 13, 500 if not future else 400, INK2 if future else INK, "end")
        if deltas and d:
            c.delta(x + w - 18, yy + 15, None, 7)
            c.t(x + w - 4, yy + 22, str(d), 11, 700, INK, "start")
        yy += rh
    c.l(x, yy, x + w, yy)
    return yy

# 1 STANDBY
px = X[0]
c.phone(px, PY, "1 · Landing, standby", [
    "A title block (ruled 1.2 px ink), then revisions (3 rows), then the index collapsed to stages: one row each, a count, a Δ count. No scroll.",
    "Δ = changed since you last looked. Plain triangle, no issue number (see push: issues are by day, not per publish).",
    "Lock row carries the 3 px ‘now’ bar. Future stages in ink 2.",
    "One input: ‘Go to’ a code. A register earns a search field; it's the only one."], "0 taps")
y = titleblock(px, PY + TOP + 14, "standby", "Standby · 14:02")
y = revisions(px, y + 26)
sections(px, y + 24)

# 2 ON
px = X[1]
c.phone(px, PY, "2 · On — FOLD-D rev C lands", [
    "Status cell goes ON (mid-dip drawn). The revision table grows a top row: ‘Today · in progress · FOLD-D rev C’, inserted with a 180 ms height + fade; older rows push down, the oldest drops off.",
    "Concept's Δ ticks 3 → 4.",
    "At day end the in-progress row becomes ‘13 Nov’. That's how a register feels live without images."], "0 taps")
y = titleblock(px, PY + TOP + 14, "dip", "On · round 6 sheets")
y = revisions(px, y + 26, top=("Today", "now", "in progress · FOLD-D rev C", True))
c.r(px + 16, y - 3 * 32 - 0, 3, 32, ON, op=0)  # placeholder (no colour on rows)
sections(px, y + 24, bump=1)

# 3 FOLD-A v1.1 vs v1, clouds
px = X[2]
c.phone(px, PY, "3 · FOLD-A v1.1 → its v1 form", [
    "Path: revisions ‘v1.1’ (1) → FOLD-A (2) → rev B row (3). Or Concept (1) → FOLD-A (2) → rev B (3).",
    "‘Show changes’ draws revision clouds from a real pixel diff of v1 → v1.1: the joystick, the closed view, the effects text and the footer. Ink only; the scallop is the mark.",
    "The item's own revision table is the lineage; ‘r1–r4 not kept’ is one row.",
    "Wipe for compare, same as every concept."], "3 taps")
y = PY + TOP
c.t(px + 16, y + 30, "‹ v1.1 set", 14, 500, INK2); c.t(px + PW - 16, y + 30, "copy link", 13, 500, INK2, "end")
c.t(px + 16, y + 66, "FOLD-A", 20, 700); c.t(px + 100, y + 66, "The look", 17, 400)
c.t(px + 16, y + 88, "legacy sheet · Concept · rev C · locked in v1.1", 13, 400, INK2)
iy = y + 104
h = c.img("FOLD-A", px + 16, iy, 358)
CL = [(0.813, 0.178, 0.048, 0.068), (0.668, 0.219, 0.048, 0.082), (0.116, 0.328, 0.048, 0.082),
      (0.194, 0.410, 0.068, 0.109), (0.629, 0.835, 0.184, 0.096), (0.610, 0.944, 0.348, 0.055)]
for fx, fy, fw, fh in CL:
    c.cloud(px + 16 + fx * 358 - 2, iy + fy * h - 2, fw * 358 + 4, min(fh * h + 4, h - fy * h), bump=3.2, sw=1.1)
ty = iy + h + 22
c.t(px + 16, ty, "Show changes from rev B", 13, 600)
c.r(px + PW - 60, ty - 14, 44, 20, INK); c.circle(px + PW - 26, ty - 4, 7, WHITE)
c.t(px + 16, ty + 20, "6 changed areas", 12.5, 400, INK2)
c.label(px + 16, ty + 52, "Revisions of FOLD-A")
rows = [("C", "13 Nov", "v1.1 · bend drawn as a joystick", "current", True), ("B", "13 Nov", "v1 · first lock", "compare ›", False),
        ("A", "13 Nov", "round 5 · archive", "", False), ("—", "", "r1–r4 not kept", "", False)]
ry = ty + 64
for rv, dt, ds, act, strong in rows:
    c.l(px + 16, ry, px + PW - 16, ry)
    c.t(px + 16, ry + 23, rv, 14, 700 if strong else 500, INK if strong else INK2)
    c.t(px + 44, ry + 23, dt, 12.5, 400, INK2)
    c.t(px + 104, ry + 23, ds, 12.5, 500 if strong else 400, INK if strong or rv == "B" else INK2)
    c.t(px + PW - 16, ry + 23, act, 12.5, 600 if rv == "B" else 400, INK if rv == "B" else INK2, "end")
    ry += 34
c.l(px + 16, ry, px + PW - 16, ry)

# 4 Bass pluck
px = X[3]
c.phone(px, PY, "4 · Bass pluck · golden vs perturbed", [
    "Path: Concept (1) → T-006 (2). Concept's index lists tests after sheets/diagrams/docs, by code.",
    "D's test page leads with a runs table (variant · peak · envelope), the register's way to compare. The table rows are the A/B switch: tap a row to hear it; the playhead stays.",
    "Plot below at full width."], "2 taps")
y = PY + TOP
c.t(px + 16, y + 30, "‹ Concept", 14, 500, INK2); c.t(px + PW - 16, y + 30, "copy link", 13, 500, INK2, "end")
c.t(px + 16, y + 66, "T-006", 20, 700); c.t(px + 90, y + 66, "Bass pluck", 17, 400)
c.t(px + 16, y + 88, "test · Concept · rev A · 13 Nov · RAN, no limits set", 13, 400, INK2)
c.label(px + 16, y + 120, "Runs")
c.label(px + 190, y + 120, "peak"); c.label(px + 260, y + 120, "env. peak")
ry = y + 130
for v, pk, en, on in [("golden", "1.05 V", "87 ms", False), ("perturbed", "1.86 V", "69 ms", True)]:
    c.l(px + 16, ry, px + PW - 16, ry)
    if on: c.r(px + 16, ry + 1, 3, 34, INK)
    c.t(px + 28, ry + 23, v, 14, 600 if on else 400, INK if on else INK2)
    c.t(px + 190, ry + 23, pk, 13.5, 500); c.t(px + 260, ry + 23, en, 13.5, 500)
    c.t(px + PW - 16, ry + 23, "playing" if on else "play", 12.5, 600 if on else 400, INK if on else INK2, "end")
    ry += 36
c.l(px + 16, ry, px + PW - 16, ry)
ay = ry + 14
c.r(px + 16, ay, 358, 110, CELL)
c.play(px + 48, ay + 50, playing=True)
c.wave("perturbed", px + 84, ay + 50, 270, 64)
c.l(px + 84 + 0.31 * 270, ay + 14, px + 84 + 0.31 * 270, ay + 86, INK, 1.5)
c.t(px + 84, ay + 102, "0:00.6 / 0:01.98 · osc 110.0 Hz", 12, 500, INK2)
c.img("PLOT-pluck", px + 16, ay + 124, 358)

# 5 Decisions
px = X[4]
c.phone(px, PY, "5 · Find “Switch to Daisy Seed”", [
    "Path: Records (1) → Decisions (2) → the row → a code (3).",
    "Decisions are a register too: date · his words verbatim · the codes it caused. 45 rows today, newest first; this one is a scan away.",
    "Undated entries say ‘time not recorded’. The ask that led to it is the row below it (older)."], "3 taps")
y = PY + TOP
c.t(px + 16, y + 30, "‹ Records", 14, 500, INK2)
c.t(px + 16, y + 66, "Decisions", 20, 700); c.t(px + PW - 16, y + 66, "R-001 · 45", 13, 500, INK2, "end")
rows = [("13 Nov", "“i think it needs its own switch but yes now i want it”", "D-019 rev 14 · D-034", False),
        ("13 Nov", "“Add MIDI out”", "D-019", False),
        ("13 Nov", "“Also the key thing you need to port - go back to first principles…”", "D-032", False),
        ("13 Nov", "“Switch to Daisy Seed”", "D-031 · D-032 · D-019 rev 13", True),
        ("13 Nov", "“Check the pin thing. Audio feels the most important since we're introducing digital stuff”", "D-031", False)]
ry = y + 84
for dt, words, codes, open_ in rows:
    c.l(px + 16, ry, px + PW - 16, ry)
    c.t(px + 16, ry + 22, dt, 12, 500, INK2)
    yy = c.wrap(px + 76, ry + 22, words, 298, 14 if open_ else 13.5, 600 if open_ else 400, INK if open_ else INK2, lh=19, maxlines=2 if not open_ else 3)
    if open_:
        c.t(px + 76, yy + 2, "time not recorded · it caused", 12, 500, INK2)
        yy += 14
        for code, t1 in [("D-031", "Pin check and audio-quality check · before"), ("D-032", "Daisy Seed, from first principles · after"), ("D-019", "Budget variant spec · rev 13")]:
            c.t(px + 76, yy + 14, code, 12.5, 700); c.t(px + 124, yy + 14, t1, 12.5, 400)
            c.l(px + 124, yy + 17, px + 124 + tw(t1, 12.5), yy + 17, INK, 0.6)
            yy += 22
        ry = yy + 10
    else:
        c.t(px + 76, yy + 2, codes, 12, 500, INK2)
        ry = yy + 14
c.l(px + 16, ry, px + PW - 16, ry)

# 6 v1.1 set index
px = X[5]
c.phone(px, PY, "6 · What's in v1.1", [
    "Path: revisions ‘v1.1’ (1). The set's own title strip, then its index: code · title · rev, grouped by concept, docs after sheets.",
    "Every row is a link. Lock rule (double ink line) under the title.",
    "This is the track list as a register; it scrolls (32 rows), which is fine one tap in."], "1 tap")
y = PY + TOP
c.t(px + 16, y + 30, "‹ Index", 14, 500, INK2); c.t(px + PW - 16, y + 30, "copy link", 13, 500, INK2, "end")
c.t(px + 16, y + 70, "v1.1", 26, 700); c.t(px + 86, y + 70, "locked 13 Nov · current", 13, 500, INK2)
c.l(px + 16, y + 84, px + PW - 16, y + 84, INK, 1.5); c.l(px + 16, y + 88, px + PW - 16, y + 88, INK, 1.5)
yy = c.wrap(px + 16, y + 112, "v1, plus: FOLD stands at 120°; bend drawn as a joystick in every view; FOLD sheet D shows MIDI IN.", 358, 13, 400, INK, lh=19)
ry = yy + 4
for grp, items in [("FOLD", [("FOLD-A", "The look", "C"), ("FOLD-B", "Real size", "C"), ("FOLD-C", "Construction", "C"), ("FOLD-D", "Front", "B"), ("FOLD-E", "Standing", "C")]),
                   ("HUSH", [("HUSH-A", "The look", "B"), ("HUSH-B", "Real size", "B"), ("HUSH-C", "Construction", "A"), ("HUSH-D", "Front", "B")]),
                   ("ONE SHEET", [("ONESHEET-A", "The look", "B"), ("ONESHEET-B", "Real size", "B")])]:
    c.label(px + 16, ry + 22, grp, INK); ry += 30
    for code, t1, rv in items:
        c.l(px + 16, ry, px + PW - 16, ry)
        c.t(px + 16, ry + 21, code, 13, 600); c.t(px + 128, ry + 21, t1, 13, 400)
        c.t(px + PW - 16, ry + 21, "rev " + rv, 12.5, 400, INK2, "end")
        ry += 30
    if ry > PY + BOT - 60: break
c.t(px + 16, PY + BOT - 14, "+ ONE SHEET C, D · 9 docs · spec · records", 12.5, 500, INK2)

# 7 Snapshot
px = X[6]
c.phone(px, PY, "7 · Landing, signed-out snapshot", [
    "Status cell: a short rule and ‘Snapshot · 13 Nov 14:02’.",
    "Δ marks switch meaning for a signed-out viewer: changed in the latest day's publishes, labelled ‘changed 13 Nov’ in the index header so the mark never lies.",
    "No in-progress row."], "0 taps")
y = titleblock(px, PY + TOP + 14, "snapshot", "Snapshot · 13 Nov")
y = revisions(px, y + 26)
sections(px, y + 24)
c.t(px + PW - 16, y + 24, "Δ = changed 13 Nov", 11, 500, INK2, "end")

# 8 Desktop
dx, dy = 60, PY + PH + 260
DW, DH = 1440, 900
c.t(dx, dy - 18, "8 · Desktop landing, 1440 × 900 (standby)", 17, 700)
c.r(dx, dy, DW, DH, BG); c.r(dx - 0.5, dy - 0.5, DW + 1, DH + 1, "none", "#8f8c85")
titleblock(0, dy + 40, "standby", "Standby · last FOLD-D rev C · 14:02", w=520, x=dx + DW - 560)
revisions(0, dy + 56, w=760, x=dx + 48)
# full index table
ty = dy + 230
cols = [("Δ", 0), ("code", 30), ("title", 170), ("kind", 470), ("rev", 580), ("date", 650), ("status", 760), ("stage", 920)]
c.label(dx + 48, ty, "Index · Concept (112) · showing sheets", INK)
for n, ox in cols: c.label(dx + 48 + ox, ty + 30, n)
rows = [(1, "FOLD-D", "Front", "sheet", "C", "13 Nov", "exploring", "Concept"), (1, "FOLD-A", "The look", "sheet", "C", "13 Nov", "locked in v1.1", "Concept"),
        (0, "FOLD-B", "Real size", "sheet", "C", "13 Nov", "locked in v1.1", "Concept"), (0, "FOLD-C", "Construction", "sheet", "C", "13 Nov", "locked in v1.1", "Concept"),
        (0, "FOLD-E", "Standing", "sheet", "C", "13 Nov", "locked in v1.1", "Concept"), (1, "HUSH-A", "The look", "sheet", "B", "13 Nov", "locked in v1.1", "Concept"),
        (0, "HUSH-B", "Real size", "sheet", "B", "13 Nov", "locked in v1.1", "Concept"), (0, "ONESHEET-A", "The look", "sheet", "B", "13 Nov", "locked in v1.1", "Concept"),
        (0, "ONESHEET-B", "Real size", "sheet", "B", "13 Nov", "locked in v1.1", "Concept"), (0, "FOLD113-A", "The look (113)", "sheet", "A", "13 Nov", "dropped", "Concept"),
        (0, "TYPECASE-A", "The look", "sheet", "A", "12 Nov", "dropped", "Concept"), (0, "HYMNAL-A", "The look", "sheet", "A", "12 Nov", "dropped", "Concept")]
ry = ty + 40
for d, *vals in rows:
    c.l(dx + 48, ry, dx + DW - 48, ry)
    op = 0.4 if vals[5] == "dropped" else 1
    if d: c.delta(dx + 56, ry + 15, None, 7)
    for (n, ox), v in zip(cols[1:], vals):
        c.t(dx + 48 + ox, ry + 22, v, 13.5, 600 if n == "code" else 400, INK if n in ("code", "title") else INK2, op=op)
    ry += 34
c.l(dx + 48, ry, dx + DW - 48, ry)
c.t(dx + 48, ry + 30, "Diagrams (22) ›   Docs (38) ›   Tests (7) ›   then Lock · Handoff · Spec · … · Records", 13.5, 500, INK2)
nx = dx + DW + 60
yy = dy + 20
c.t(nx, yy, "Desktop notes", 17, 700); yy += 30
for n in ["Title block top right, as on a drawing. Revisions top left. The index as one table, one stage open at a time, kind groups inside.",
          "Rows are 34 px; codes in 600, everything else 400. Dropped rows at 40% with ‘dropped’ in the status column.",
          "Click a row → the item opens in place of the index (same page, back returns to the row)."]:
    yy = c.wrap(nx, yy, n, 520, 14, 400, INK2, lh=21) + 12
c.save(os.path.join(ROOT, "site/design/concepts/the-set/frames"))
print("set ok")
