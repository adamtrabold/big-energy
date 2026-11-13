"""C · Cabinet — 8 frames (7 phone at 1:1 + desktop at 1:1). Output: ../cabinet/frames.{svg,png}"""
from lib import *

GAP = 64
W = max(60 * 2 + 7 * PW + 6 * GAP, 60 + 1440 + 60 + 390 + 360)
H = 150 + PH + 250 + 900 + 420
c = Canvas(W, H)
c.r(0, 0, W, H, WHITE)
c.t(60, 64, "C · Cabinet — how it looks and feels · 8 frames", 30, 700)
c.t(60, 96, "Phones 1:1 (390 × 844) inside real browser chrome: the no-scroll area is 714 px. Real content: v1.1 sheets, golden/perturbed bass pluck, owner.md. Counts from a repo survey 13 Nov (approximate until backfill); D-codes illustrative.", 15, 400, INK2)

from cabinet_parts import cabinet_grid, STAGES, KINDS, COUNTS
def cabinet(x, y, **k):
    return cabinet_grid(c, x, y, **k)

def header(px, py, state, line):
    y = py + TOP
    c.lampline(px + 16, y + 28, state, line)
    c.t(px + 16, y + 64, "( name to come )", 22, 600)
    c.t(px + 16, y + 86, "a portable Model D · v1.1 current", 13, 400, INK2)
    c.l(px + 16, y + 102, px + PW - 16, y + 102)
    c.label(px + 16, y + 124, "Waiting on you")
    c.t(px + 16, y + 146, "ONE SHEET or FOLD", 16, 600)
    c.t(px + PW - 16, y + 146, "then the name", 13, 400, INK2, "end")
    return y + 160

def newest(px, y, code, line, sub, key, mark=False):
    c.l(px + 16, y, px + PW - 16, y)
    c.label(px + 16, y + 22, "Newest")
    c.img(key, px + 16, y + 32, 96, 68)
    c.t(px + 124, y + 50, code, 15, 600)
    c.t(px + 124, y + 70, line, 13, 400)
    c.t(px + 124, y + 90, sub, 12.5, 400, INK2)
    if mark: c.dot(px + 124 + tw(code, 15, 600) + 10, y + 45)
    c.t(px + PW - 16, y + 50, "›", 18, 400, INK2, "end")
    return y + 108

DET = [("R1", "12 Nov"), ("R2", "12 Nov"), ("R3", "12 Nov"), ("R4", "12 Nov"), ("R5", "13 Nov"), ("v1", "13 Nov"), ("v1.1", "13 Nov"), ("now", "")]
def scrubber(px, y, at=7, label=None):
    x0, x1 = px + 24, px + PW - 24
    if label: c.t(px + 16, y - 6, label, 12, 500, INK2)
    yl = y + 22
    c.l(x0, yl, x1, yl, INK, 1.5)
    for i, (d, _) in enumerate(DET):
        xx = x0 + i * (x1 - x0) / 7
        big = d.startswith("v") or d == "now"
        c.l(xx, yl - (9 if big else 5), xx, yl + (9 if big else 5), INK, 1.5 if big else 1)
        c.t(xx, yl + 26, d, 12, 600 if big else 400, INK if big else INK2, "middle")
    hx = x0 + at * (x1 - x0) / 7
    c.r(hx - 7, yl - 14, 14, 28, INK)
    c.t(px + PW - 16, y - 6, "history ›", 13, 500, INK2, "end")
    return yl + 34

# ---------- frame positions
X = [60 + i * (PW + GAP) for i in range(7)]
PY = 170

# 1 STANDBY
px = X[0]
c.phone(px, PY, "1 · Landing, standby", [
    "Lamp ring + last event. Waiting on you is the biggest line after the name: it's his.",
    "The level: rows above the 1.5 px line are filled (done or now); below, outlines and ‘not yet’ once per row, never a dot per cell.",
    "Spec's 19 docs sit below the level in ink 2: work begun early, honestly shown out of order.",
    "Newest names one thing to look at (director push 1)."], "0 taps")
y = header(px, PY, "standby", "Standby · last FOLD-D rev C · 14:02")
y = cabinet(px + 16, y + 30)
y = newest(px, y + 10, "FOLD-D · Front", "rev C · 14:02", "legacy sheet · Concept · round 6", "FOLD-D")
scrubber(px, PY + BOT - 74)

# 2 ON, event lands
px = X[1]
c.phone(px, PY, "2 · On — FOLD-D rev C lands", [
    "Lamp ON, dips once (drawn mid-dip). Line says what the session is doing.",
    "The count doesn't move (a rev isn't a new item); the drawer gets an unseen dot, Newest swaps with a 180 ms fade.",
    "Unseen count sits by Newest: ‘3 unseen’. Taps through to the drawer, unseen first.",
    "Nothing else moves. Liveness is the lamp, one dot, one strip."], "0 taps")
y = header(px, PY, "dip", "On · round 6 sheets · since 13:40")
y = cabinet(px + 16, y + 30, dots={("Concept", 0), ("Concept", 1)})
y2 = newest(px, y + 10, "FOLD-D · Front", "rev C · just now", "legacy sheet · Concept · round 6", "FOLD-D", mark=True)
c.t(px + PW - 16, y + 32, "3 unseen", 12.5, 600, INK, "end")
scrubber(px, PY + BOT - 74)

# 3 FOLD-A v1.1 -> v1 compare
px = X[2]
c.phone(px, PY, "3 · FOLD-A v1.1 → its v1 form", [
    "Path: Concept·images drawer (1) → FOLD-A (2) opens at its current rev = the v1.1 form → v1 in the lineage row (3).",
    "Phone compare is a wipe: drag the hairline. Here: v1.1 left, v1 right; the joystick redraw sits under the line.",
    "Lineage by repetition, real counts: r5 (archive) · ‘r1–r4 not kept’ · v1 · v1.1. One gap, labelled.",
    "No read mode (owner 12:13). Pinch zooms to 3200 px; turn the phone for edge to edge."], "3 taps")
y = PY + TOP
c.t(px + 16, y + 30, "‹ Concept · images", 14, 500, INK2)
c.t(px + PW - 16, y + 30, "copy link", 13, 500, INK2, "end")
iy = y + 48
h = c.img("FOLD-A", px + 16, iy, 358)
cut = 0.47
c.img("FOLD-A@v1", px + 16 + 358 * cut, iy, 358 * (1 - cut), h, crop=(cut, 0, 1 - cut, 1))
hx = px + 16 + 358 * cut
c.l(hx, iy, hx, iy + h, INK, 1.5)
c.circle(hx, iy + h / 2, 13, WHITE, INK, 1.5)
c.t(hx, iy + h / 2 + 4, "‹›", 11, 700, INK, "middle")
c.label(px + 22, iy + h + 18, "v1.1 · rev C", INK); c.label(px + PW - 22, iy + h + 18, "v1 · rev B", INK, "end")
ly = iy + h + 38
c.l(px + 16, ly, px + PW - 16, ly)
c.t(px + 16, ly + 26, "FOLD-A · The look", 17, 600)
c.t(px + 16, ly + 48, "legacy sheet · Concept · rev C · 13 Nov · locked in v1.1", 13, 400, INK2)
c.t(px + 16, ly + 68, "4961 × 3508 · download original", 13, 400, INK2)
ry = ly + 90
c.label(px + 16, ry, "Lineage")
ty = ry + 12
tiles = [("FOLD-A@r5", "r5 · rev A", "archive"), (None, "r1–r4", "not kept"), ("FOLD-A@v1", "v1 · rev B", "compare"), ("FOLD-A", "v1.1 · rev C", "current")]
tx = px + 16
for k, a, b in tiles:
    if k:
        c.img(k, tx, ty, 80, 57)
        if b == "compare": c.r(tx - 2, ty - 2, 84, 61, "none", INK, 2)
        c.t(tx, ty + 74, a, 11.5, 600); c.t(tx, ty + 90, b, 11.5, 400, INK2)
        tx += 92
    else:
        c.l(tx + 4, ty + 28, tx + 44, ty + 28, RULE, 1, "3 3")
        c.t(tx + 4, ty + 74, a, 11.5, 600, INK2); c.t(tx + 4, ty + 90, b, 11.5, 400, INK2)
        tx += 58
c.label(px + 16, ty + 124, "Side by side on desktop · wipe on phone")

# 4 Bass pluck A/B
px = X[3]
c.phone(px, PY, "4 · Bass pluck · golden vs perturbed", [
    "Path: Concept·tests (1) → T-006 Bass pluck (2).",
    "Result in words first. Waveform is a static peak line; golden and perturbed share one scale, so the louder perturbed run looks louder.",
    "A/B is two words with an underline; switching keeps the playhead (0:00.6). One sound plays at a time.",
    "The plot follows at full width; pinch for detail."], "2 taps")
y = PY + TOP
c.t(px + 16, y + 30, "‹ Concept · tests", 14, 500, INK2)
c.t(px + PW - 16, y + 30, "copy link", 13, 500, INK2, "end")
c.t(px + 16, y + 68, "T-006 · Bass pluck", 20, 600)
c.t(px + 16, y + 90, "test · Concept · run 13 Nov · golden, perturbed", 13, 400, INK2)
c.t(px + 16, y + 122, "RAN", 15, 700); c.t(px + 54, y + 122, "no limits set for this test", 13, 400, INK2)
c.t(px + 16, y + 144, "osc 110.0 Hz · envelope peak 87 ms golden, 69 ms perturbed", 12.5, 400, INK2)
ay = y + 162
c.r(px + 16, ay, 358, 150, CELL)
c.play(px + 48, ay + 56, playing=True)
c.wave("perturbed", px + 84, ay + 56, 270, 70)
c.l(px + 84 + 0.31 * 270, ay + 16, px + 84 + 0.31 * 270, ay + 96, INK, 1.5)
c.t(px + 84, ay + 116, "0:00.6 / 0:01.98", 12, 500, INK2)
c.t(px + 32, ay + 138, "golden", 14, 400, INK2)
c.t(px + 104, ay + 138, "perturbed", 14, 600, INK)
c.r(px + 104, ay + 143, tw("perturbed", 14, 600), 2, INK)
c.t(px + PW - 32, ay + 138, "peak 1.86 V", 12.5, 400, INK2, "end")
c.img("PLOT-pluck", px + 16, ay + 166, 358)

# 5 Daisy decision
px = X[4]
c.phone(px, PY, "5 · Find “Switch to Daisy Seed”", [
    "Path: ‘history’ at the scrubber's end (1) → Day, 13 Nov (scroll) → a caused item (2).",
    "Decisions verbatim at body size, never headline. The ask that led to it sits above; the work it caused sits under it as rows.",
    "No time recorded for this entry, so none is shown (‘time not recorded’), not a guessed one.",
    "Grain switch at the bottom, in thumb reach."], "2 taps + scroll")
y = PY + TOP
c.t(px + 16, y + 30, "‹ Cabinet", 14, 500, INK2)
c.t(px + 16, y + 66, "History", 22, 600)
c.label(px + 16, y + 96, "13 Nov · Thursday", INK)
c.l(px + 16, y + 106, px + PW - 16, y + 106)
ey = y + 130
c.t(px + 16, ey, "you asked", 12, 500, INK2)
ey = c.wrap(px + 16, ey + 20, "“Check the pin thing. Audio feels the most important since we're introducing digital stuff”", 358, 15, 400, INK2, lh=21)
c.t(px + 16, ey + 4, "→ D-031 Pin check and audio-quality check", 13, 500, INK2)
ey += 34
c.l(px + 16, ey, px + PW - 16, ey)
c.t(px + 16, ey + 24, "you decided · time not recorded", 12, 500, INK2)
c.t(px + 16, ey + 48, "“Switch to Daisy Seed”", 17, 600)
ey = c.wrap(px + 16, ey + 72, "Daisy Seed replaces the Pico 2 as the one digital chip (control + echo/reverb). Dry voice stays analog.", 358, 13, 400, INK2, lh=19)
c.label(px + 16, ey + 10, "It caused")
rows = [("D-031", "Pin check and audio-quality check", "before · the evidence"),
        ("D-032", "Daisy Seed, from first principles", "after · the redesign"),
        ("D-019", "Budget variant spec", "rev 13 · Daisy replaces Pico")]
ry = ey + 22
for code, t1, t2 in rows:
    c.l(px + 16, ry, px + PW - 16, ry)
    c.t(px + 16, ry + 22, code, 13, 600); c.t(px + 72, ry + 22, t1, 13.5, 500)
    c.t(px + 72, ry + 41, t2, 12, 400, INK2); c.t(px + PW - 16, ry + 30, "›", 18, 400, INK2, "end")
    ry += 52
c.l(px + 16, ry, px + PW - 16, ry)
by = PY + BOT - 46
c.l(px, by - 10, px + PW, by - 10)
for i, s in enumerate(["Day", "Round", "Version"]):
    cx = px + 70 + i * 125
    c.t(cx, by + 18, s, 14, 600 if i == 0 else 400, INK if i == 0 else INK2, "middle")
    if i == 0: c.r(cx - 22, by + 26, 44, 2, INK)

# 6 What's in v1.1
px = X[5]
c.phone(px, PY, "6 · What's in v1.1", [
    "Path: tap the Lock drawer (1). Lock is one wide drawer: locking makes versions, not sheets.",
    "The version page: one line, what changed from v1, then the track list (by concept, sheet letters as 44 px targets).",
    "Docs and records as one plain list. A lock is a ruled, signed line at the top.",
    "Older version (v1) one row below; never edited."], "1 tap")
y = PY + TOP
c.t(px + 16, y + 30, "‹ Cabinet", 14, 500, INK2)
c.t(px + PW - 16, y + 30, "copy link", 13, 500, INK2, "end")
c.l(px + 16, y + 50, px + PW - 16, y + 50, INK, 1.5); c.l(px + 16, y + 54, px + PW - 16, y + 54, INK, 1.5)
c.t(px + 16, y + 88, "v1.1", 26, 600); c.t(px + 84, y + 88, "current · locked 13 Nov", 13, 500, INK2)
yy = c.wrap(px + 16, y + 116, "v1, plus: FOLD stands at 120° so the face catches more light; bend drawn as a joystick in every view; FOLD sheet D shows MIDI IN. The director held all three at 9.", 358, 13.5, 400, INK, lh=20)
c.label(px + 16, yy + 12, "Sheets")
ty = yy + 24
for name, letters in [("HUSH", "ABCD"), ("ONE SHEET", "ABCD"), ("FOLD", "ABCDE")]:
    c.l(px + 16, ty, px + PW - 16, ty)
    c.t(px + 16, ty + 30, name, 14, 600)
    for i, L in enumerate(letters):
        bx = px + 130 + i * 48
        c.r(bx, ty + 6, 44, 38, CELL, RULE)
        c.t(bx + 22, ty + 31, L, 14, 500, INK, "middle")
    ty += 50
c.l(px + 16, ty, px + PW - 16, ty)
c.label(px + 16, ty + 28, "Docs and records")
dy = ty + 50
for d in ["How it works · HUSH, ONE SHEET, FOLD", "Looks and feels · HUSH, ONE SHEET, FOLD", "Common how it works · common looks and feels", "Spec · budget variant (as of the lock)", "Owner record · scores · team notes"]:
    c.t(px + 16, dy, d, 13.5, 400); dy += 24
c.l(px + 16, dy, px + PW - 16, dy)
c.t(px + 16, dy + 26, "v1 · 13 Nov · first official lock", 13.5, 400, INK2); c.t(px + PW - 16, dy + 26, "›", 18, 400, INK2, "end")

# 7 Snapshot
px = X[6]
c.phone(px, PY, "7 · Landing, signed-out snapshot", [
    "No lamp (a short rule in its place): this viewer gets no live data, so it can't say on or standby.",
    "‘Snapshot · 13 Nov 14:02’ is the publish time. No unseen dots, no unseen count.",
    "Everything else is identical; every drawer, item and the scrubber work from the snapshot.",
    "Waiting on you stays: ‘it is primarily me’."], "0 taps")
y = header(px, PY, "snapshot", "Snapshot · 13 Nov 14:02")
y = cabinet(px + 16, y + 30, snapshot=True)
newest(px, y + 10, "FOLD-D · Front", "rev C · 14:02", "legacy sheet · Concept · round 6", "FOLD-D")
scrubber(px, PY + BOT - 74)

# 8 Desktop 1440 x 900
dx, dy = 60, PY + PH + 260
DW, DH = 1440, 900
c.t(dx, dy - 18, "8 · Desktop landing, 1440 × 900 (standby)", 17, 700)
c.r(dx, dy, DW, DH, BG); c.r(dx - 0.5, dy - 0.5, DW + 1, DH + 1, "none", "#8f8c85")
c.lampline(dx + 48, dy + 48, "standby", "Standby · last FOLD-D rev C · 14:02")
c.t(dx + 48, dy + 92, "( name to come )", 28, 600)
c.t(dx + 48, dy + 118, "a portable Model D · v1.1 current", 14, 400, INK2)
c.label(dx + 48, dy + 160, "Waiting on you"); c.t(dx + 48, dy + 184, "ONE SHEET or FOLD", 18, 600)
cabinet(dx + 60, dy + 240, cw=92, rh=50, name_w=104)
c.l(dx + 560, dy + 40, dx + 560, dy + DH - 130)
# right: the newest item open
rx = dx + 600
c.label(rx, dy + 52, "Newest · FOLD-D · Front · rev C · 14:02")
hh = c.img("FOLD-D", rx, dy + 66, 790)
c.t(rx, dy + 66 + hh + 30, "FOLD-D · Front", 17, 600)
c.t(rx, dy + 66 + hh + 52, "legacy sheet · Concept · rev C · 13 Nov · exploring · open ›", 13, 400, INK2)
# scrubber full width
sx0, sx1, sy = dx + 60, dx + DW - 60, dy + DH - 70
c.l(sx0, sy, sx1, sy, INK, 1.5)
for i, (d, dt) in enumerate(DET):
    xx = sx0 + i * (sx1 - sx0) / 7
    big = d.startswith("v") or d == "now"
    c.l(xx, sy - (10 if big else 6), xx, sy + (10 if big else 6), INK, 1.5 if big else 1)
    c.t(xx, sy + 30, d + ("  " + dt if dt else ""), 12.5, 600 if big else 400, INK if big else INK2, "middle")
c.r(sx1 - 8, sy - 16, 16, 32, INK)
c.t(sx1, sy - 26, "history ›", 13, 500, INK2, "end")
# side notes
nx = dx + DW + 60
notes = ["Master–detail, no page changes: cabinet left (5 of 12 cols), the newest item open on the right so the big area is the work, not empty.",
         "Tapping a drawer replaces the right side with the drawer (sheets as a 3-up thumbnail grid, other kinds as rows).",
         "The scrubber spans the full width; detents are rounds and locks only (8), never one per decision (45 in ~30 h would put ticks 7 px apart on a phone).",
         "Tablet uses this layout from 768 px."]
yy = dy + 20
c.t(nx, yy, "Desktop notes", 17, 700); yy += 30
for n in notes: yy = c.wrap(nx, yy, n, 520, 14, 400, INK2, lh=21) + 12

# extra: scrubbed to Round 2 (director push 3: the real case)
px, py2 = nx, dy + 300
c.phone(px, py2, "Extra · scrubbed back to Round 2", [], "drag")
y = py2 + TOP
c.r(px, y + 8, PW, 36, INK)
c.t(px + 16, y + 31, "As it stood · Round 2 · 12 Nov", 13, 600, WHITE)
c.t(px + PW - 16, y + 31, "back to now ›", 13, 500, WHITE, "end")
c.t(px + 16, y + 80, "( name to come )", 22, 600)
c.t(px + 16, y + 102, "no version yet · six concepts in play", 13, 400, INK2)
c.l(px + 16, y + 118, px + PW - 16, y + 118)
c.label(px + 16, y + 142, "Round 2 scores, then")
rows = [("TYPE CASE", "9", "set aside later"), ("HYMNAL", "9", "set aside later"), ("HUSH", "8", "locked in v1, v1.1"),
        ("FOLD", "7", "now: one of your two"), ("ONE SHEET", "7", "now: one of your two"), ("UNDER GLASS", "6", "killed in this round")]
ry = y + 156
for n, sc, fate in rows:
    c.l(px + 16, ry, px + PW - 16, ry)
    strong = "your two" in fate
    c.t(px + 16, ry + 26, n, 14, 600 if strong else 400, INK if strong else INK2)
    c.t(px + 150, ry + 26, sc, 16, 600, INK if strong else INK2)
    c.t(px + PW - 16, ry + 26, fate, 12.5, 600 if strong else 400, INK if strong else INK2, "end")
    ry += 40
c.l(px + 16, ry, px + PW - 16, ry)
ry = c.wrap(px + 16, ry + 26, "Sheets from rounds 1–4 weren't kept; the records were. Drawers show what was kept, marked ‘not kept’ where not.", 358, 12.5, 400, INK2, lh=18)
scrubber(px, py2 + BOT - 74, at=1, label="12 Nov · Round 2")
c.t(px + PW + 24, py2 + 40, "Why the scrubber stays:", 15, 700)
yy = py2 + 66
for n in ["Drag to R2 and the records say: the two concepts he's choosing between today were both 7s; the two 9s were later set aside. That's a thing he'd want to see, and no other concept shows it in one gesture.",
          "It scrubs records (scores, decisions, locks), not files, so the builder computes states from scores.md / owner.md / VERSIONS.md, not from lost images.",
          "Detents: rounds + locks only. Decisions show in the history list, not as ticks."]:
    yy = c.wrap(px + PW + 24, yy, n, 300, 13, 400, INK2, lh=19) + 10

c.save(os.path.join(ROOT, "site/design/concepts/cabinet/frames"))
print("cabinet ok")
