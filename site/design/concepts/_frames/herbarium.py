"""E · Herbarium — 8 frames. Output: ../herbarium/frames.{svg,png}
Every item is shown as itself, at its own shape, full column width (height capped), with one label
in the same place and the same fields for every kind. Revisions are slips on the label.
"""
from lib import *

GAP = 64
W = 60 * 2 + 7 * PW + 6 * GAP
H = 150 + PH + 250 + 900 + 80
c = Canvas(W, H)
c.r(0, 0, W, H, WHITE)
c.t(60, 64, "E · Herbarium — how it looks and feels · 8 frames", 30, 700)
c.t(60, 96, "Phones 1:1 inside browser chrome (714 px usable). Every item shown as itself; one label, same fields, same place. Existing A3 sheets shown as they are (legacy); new images are screen-shaped and simply sit at their own shape.", 15, 400, INK2)
X = [60 + i * (PW + GAP) for i in range(7)]
PY = 170
STAGES = ["Concept", "Lock", "Handoff", "Spec", "BOM", "Breadboard", "Boards", "Prints", "Assembly"]

def head(px, state, line):
    y = px_y = PY + TOP
    c.lampline(px + 16, y + 28, state, line)
    c.t(px + 16, y + 62, "( name to come )", 22, 600)
    c.t(px + 16, y + 84, "a portable Model D ·", 13, 400, INK2)
    vx = px + 16 + tw("a portable Model D · ", 13)
    c.t(vx, y + 84, "v1.1 current", 13, 500, INK); c.l(vx, y + 87, vx + tw("v1.1 current", 13, 500), y + 87, INK, 0.8)
    c.label(px + 16, y + 112, "Waiting on you")
    c.t(px + 16, y + 134, "ONE SHEET or FOLD", 16, 600)
    # stage level strip
    sy = y + 152
    n = 9; gap = 4; sw = (358 - gap * (n - 1)) / n
    for i in range(n):
        x = px + 16 + i * (sw + gap)
        if i == 0: c.r(x, sy, sw, 6, INK)
        elif i == 1: c.r(x, sy, sw, 6, INK); c.r(x, sy + 9, sw, 2, INK)
        elif i == 3: c.r(x, sy, sw, 6, "none", INK2, 1)
        else: c.r(x, sy, sw, 6, RULE)
    c.t(px + 16, sy + 28, "Lock", 12.5, 600); c.t(px + 16 + tw("Lock ", 12.5, 600), sy + 28, "· 2 of 9 · Spec begun early · next Handoff", 12.5, 400, INK2)
    return sy + 42

def label(px, y, code, title, fields, slips, more=None, unseen=False, w=358):
    x = px + 16
    c.l(x, y, x + w, y, INK, 1)
    c.t(x, y + 22, code, 15, 700); c.t(x + tw(code, 15, 700) + 8, y + 22, title, 15, 400)
    if unseen: c.dot(x + w - 4, y + 16)
    c.t(x, y + 42, fields, 12.5, 400, INK2)
    yy = y + 52
    for i, (rv, txt) in enumerate(slips):
        c.r(x, yy, w, 24, PAGE if i == 0 else "none", RULE)
        c.t(x + 8, yy + 16.5, "rev " + rv, 12, 700 if i == 0 else 500, INK if i == 0 else INK2)
        c.t(x + 58, yy + 16.5, txt, 12, 400 if i else 500, INK if i == 0 else INK2)
        yy += 27
    if more:
        c.t(x + 8, yy + 13, more, 11.5, 500, INK2); yy += 18
    return yy

def specimen_sheet(px, y, key, maxh=300):
    h = c.img(key, px + 16, y, 358)
    return y + min(h, maxh)

def one_of_each(px, y):
    c.label(px + 16, y, "Newest of each kind")
    tw_ = 114; gap = (358 - 3 * tw_) / 2
    ty = y + 10
    x = px + 16
    c.img("SKETCH", x, ty, tw_, 62); c.t(x, ty + 78, "image · G-021", 11, 600)
    x += tw_ + gap
    doc_page(c, x, ty, tw_, 62, "Daisy Seed, from first principles", DAISY_FP[:1], size=6); c.t(x, ty + 78, "doc · D-032", 11, 600)
    x += tw_ + gap
    c.r(x, ty, tw_, 62, CELL); c.wave("golden", x + 8, ty + 31, tw_ - 16, 44, n=34, sw=1)
    c.t(x, ty + 78, "test · T-007", 11, 600)
    return ty + 84

def filters(px, y, sel):
    c.r(px, y, PW, 40, BG)
    x = px + 16
    for f in ["all", "stage", "kind", "version", "decisions", "history"]:
        on = f == sel
        c.t(x, y + 25, f, 14, 600 if on else 400, INK if on else INK2)
        if on: c.r(x, y + 31, tw(f, 14, 600), 2, INK)
        x += tw(f, 14, 600) + 18
    c.l(px, y + 40, px + PW, y + 40)
    return y + 40

# 1 STANDBY
px = X[0]
c.phone(px, PY, "1 · Landing, standby", [
    "The work is the biggest thing: the newest item at full column width, at its own shape (a legacy A3 here; new screen-shaped images just sit taller).",
    "The label: code + title, then kind · stage · status, then slips, newest on top on paper ground. Same fields, same place, every kind.",
    "Stage as a level strip (director: J6 was E's weak spot): 9 segments, filled to Lock, Spec outlined (begun early).",
    "Newest of each kind: image, doc, test (FOLD-D is already the newest image). Labels and slips are HTML text, never baked into images."], "0 taps")
y = head(px, "standby", "Standby · last FOLD-D rev C · 14:02")
y = specimen_sheet(px, y, "FOLD-D")
y = label(px, y + 10, "FOLD-D", "Front", "legacy sheet · Concept · exploring",
          [("C", "14:02 · round 6"), ("B", "13 Nov · v1.1 · shows MIDI IN")], "+ rev A (v1) · r1–r4 not kept")
c.t(px + 16, y + 20, "+ 6 more since you last looked ›", 13, 600)
one_of_each(px, y + 46)

# 2 ON
px = X[1]
c.phone(px, PY, "2 · On — FOLD-D rev C lands", [
    "Lamp ON, dips once. The new rev takes the specimen place: image cross-fades 180 ms, a new slip ‘rev C · just now’ lands on top of the stack, the old top slip steps down.",
    "Unseen dot on the label; the count ticks to 7.",
    "If an event names an item not yet published, the label and slip appear at once and the image area says ‘image arriving with the next publish’ (no stand-in picture)."], "0 taps")
y = head(px, "dip", "On · round 6 sheets · since 13:40")
y = specimen_sheet(px, y, "FOLD-D")
y = label(px, y + 10, "FOLD-D", "Front", "legacy sheet · Concept · exploring",
          [("C", "just now · round 6"), ("B", "13 Nov · v1.1 · shows MIDI IN")], "+ rev A (v1) · r1–r4 not kept", unseen=True)
c.t(px + 16, y + 20, "+ 7 more since you last looked ›", 13, 600)
one_of_each(px, y + 46)

# 3 FOLD-A v1.1 -> v1
px = X[2]
c.phone(px, PY, "3 · FOLD-A v1.1 → its v1 form", [
    "Path: ‘v1.1 current’ under the name (1) → FOLD-A in the set (2) → v1 in the lineage row (3).",
    "Opened, the slips unfold: every rev with its one line. The lineage row repeats the same image small, so the eye catches what moved; r1–r4 is one labelled gap.",
    "Wipe to compare (phone), side by side on desktop."], "3 taps")
y = PY + TOP
c.t(px + 16, y + 30, "‹ v1.1", 14, 500, INK2); c.t(px + PW - 16, y + 30, "copy link", 13, 500, INK2, "end")
iy = y + 48
h = c.img("FOLD-A", px + 16, iy, 358)
cut = 0.47
c.img("FOLD-A@v1", px + 16 + 358 * cut, iy, 358 * (1 - cut), h, crop=(cut, 0, 1 - cut, 1))
hx = px + 16 + 358 * cut
c.l(hx, iy, hx, iy + h, INK, 1.5); c.circle(hx, iy + h / 2, 13, WHITE, INK, 1.5); c.t(hx, iy + h / 2 + 4, "‹›", 11, 700, INK, "middle")
c.label(px + 22, iy + h + 16, "rev C · v1.1", INK); c.label(px + PW - 22, iy + h + 16, "rev B · v1", INK, "end")
y = label(px, iy + h + 28, "FOLD-A", "The look", "legacy sheet · Concept · locked in v1.1",
          [("C", "13 Nov · v1.1 · bend drawn as a joystick"), ("B", "13 Nov · v1 · first lock"), ("A", "13 Nov · round 5 · archive")], "earlier revs (r1–r4) not kept")
ty = y + 12
tx = px + 16
for k, a in [("FOLD-A@r5", "A"), (None, "r1–r4"), ("FOLD-A@v1", "B"), ("FOLD-A", "C")]:
    if k:
        c.img(k, tx, ty, 80, 57)
        if a == "B": c.r(tx - 2, ty - 2, 84, 61, "none", INK, 2)
        c.t(tx, ty + 72, "rev " + a, 11.5, 600); tx += 92
    else:
        c.l(tx + 4, ty + 28, tx + 44, ty + 28, RULE, 1, "3 3"); c.t(tx + 4, ty + 72, "not kept", 11.5, 400, INK2); tx += 58

# 4 test
px = X[3]
c.phone(px, PY, "4 · Bass pluck · golden vs perturbed", [
    "Path: Newest of each kind → test tile (1) if it's the newest test; else filter kind → test (2) → T-006 (3).",
    "A test's specimen is its sound: the mount holds play, the waveform, the playhead and A/B. Same label below as a sheet gets. The result is the first slip.",
    "Plot follows as a second image."], "1–3 taps")
y = PY + TOP
c.t(px + 16, y + 30, "‹ tests", 14, 500, INK2); c.t(px + PW - 16, y + 30, "copy link", 13, 500, INK2, "end")
my = y + 48
c.r(px + 16, my, 358, 200, CELL)
c.play(px + 48, my + 80, playing=True)
c.wave("perturbed", px + 84, my + 80, 274, 110)
c.l(px + 84 + 0.31 * 274, my + 18, px + 84 + 0.31 * 274, my + 142, INK, 1.5)
c.t(px + 84, my + 160, "0:00.6 / 0:01.98", 12, 500, INK2)
c.t(px + 32, my + 186, "golden", 14, 400, INK2); c.t(px + 104, my + 186, "perturbed", 14, 600, INK)
c.r(px + 104, my + 191, tw("perturbed", 14, 600), 2, INK)
c.t(px + PW - 32, my + 186, "peak 1.86 V", 12.5, 400, INK2, "end")
y = label(px, my + 212, "T-006", "Bass pluck", "test · Concept · ran 13 Nov",
          [("A", "RAN · no limits set · osc 110.0 Hz"), ("—", "golden env. peak 87 ms · perturbed 69 ms")])
c.img("PLOT-pluck", px + 16, y + 10, 358, 220)

# 5 Decision
px = X[4]
c.phone(px, PY, "5 · Find “Switch to Daisy Seed”", [
    "Path: filter ‘decisions’ (1) → scroll to 13 Nov → a caused item (2).",
    "A decision is a specimen: what it caused is mounted (two docs as pages, the spec as a page), and his words sit on the label at body size, verbatim.",
    "Docs as specimens: the first lines set as real text on paper ground, readable at this size, not a thumbnail of a page."], "2 taps + scroll")
y = PY + TOP
y = filters(px, y + 8, "decisions")
c.label(px + 16, y + 24, "13 Nov", INK)
my = y + 36
cw = (358 - 12) / 3
doc_page(c, px + 16, my, cw, 168, "Pin check and audio-quality check", DAISY_PIN, size=7.2)
doc_page(c, px + 16 + cw + 6, my, cw, 168, "Daisy Seed, from first principles", DAISY_FP, size=7.2)
doc_page(c, px + 16 + 2 * (cw + 6), my, cw, 168, "Budget variant spec", SPEC, size=7.2)
for i, (cd, nt) in enumerate([("D-031", "before"), ("D-032", "after"), ("D-019", "rev 13")]):
    c.t(px + 16 + i * (cw + 6), my + 186, cd, 11.5, 700); c.t(px + 16 + i * (cw + 6) + 44, my + 186, nt, 11.5, 400, INK2)
ly = my + 200
c.l(px + 16, ly, px + PW - 16, ly, INK, 1)
c.t(px + 16, ly + 26, "“Switch to Daisy Seed”", 17, 600)
c.t(px + 16, ly + 48, "decision · Concept · 13 Nov · time not recorded", 12.5, 400, INK2)
c.r(px + 16, ly + 58, 358, 24, PAGE, RULE)
c.t(px + 24, ly + 74.5, "asked: “Check the pin thing. Audio feels the most important…”", 12, 500)
ny = ly + 110
c.l(px + 16, ny, px + PW - 16, ny)
c.label(px + 16, ny + 24, "13 Nov")
c.t(px + 16, ny + 50, "“Add MIDI out”", 15, 600, INK2)
c.t(px + 16, ny + 70, "decision · caused D-019 rev 13 edit", 12.5, 400, INK2)

# 6 v1.1
px = X[5]
c.phone(px, PY, "6 · What's in v1.1", [
    "Path: ‘v1.1 current’ (1). The version's cover is a label with no image: one line, what changed, a ruled signed line.",
    "Then the set as specimens, 2-up, grouped by concept: the track list you can see.",
    "Filter row stays on top with ‘version’ selected; its own URL."], "1 tap")
y = PY + TOP
y = filters(px, y + 8, "version")
c.l(px + 16, y + 18, px + PW - 16, y + 18, INK, 1.5); c.l(px + 16, y + 22, px + PW - 16, y + 22, INK, 1.5)
c.t(px + 16, y + 56, "v1.1", 26, 700); c.t(px + 86, y + 56, "locked 13 Nov · current", 13, 500, INK2)
yy = c.wrap(px + 16, y + 82, "v1, plus: FOLD stands at 120°; bend drawn as a joystick in every view; FOLD sheet D shows MIDI IN.", 358, 13, 400, INK, lh=19)
gy = yy + 6
for grp, keys in [("FOLD · 5 sheets", ["FOLD-A", "FOLD-B", "FOLD-C", "FOLD-D"]), ("HUSH · 4 sheets", ["HUSH-A", "HUSH-B"])]:
    c.label(px + 16, gy + 14, grp, INK); gy += 24
    for i, k in enumerate(keys):
        x = px + 16 + (i % 2) * 183
        if i % 2 == 0 and i: gy += 152
        c.img(k, x, gy, 175, 124)
        c.t(x, gy + 140, k, 11.5, 700)
    gy += 158
    if gy > PY + BOT - 120: break
c.t(px + 16, PY + BOT - 14, "+ FOLD-E · HUSH-C, D · ONE SHEET A–D · docs", 12.5, 500, INK2)

# 7 Snapshot
px = X[6]
c.phone(px, PY, "7 · Landing, signed-out snapshot", [
    "No lamp; ‘Snapshot · 13 Nov 14:02’. No unseen dot, no ‘since you last looked’ line: it becomes ‘+ 6 more on 13 Nov’.",
    "Everything else identical."], "0 taps")
y = head(px, "snapshot", "Snapshot · 13 Nov 14:02")
y = specimen_sheet(px, y, "FOLD-D")
y = label(px, y + 10, "FOLD-D", "Front", "legacy sheet · Concept · exploring",
          [("C", "14:02 · round 6"), ("B", "13 Nov · v1.1 · shows MIDI IN")], "+ rev A (v1) · r1–r4 not kept")
c.t(px + 16, y + 20, "+ 6 more on 13 Nov ›", 13, 600)
one_of_each(px, y + 46)

# 8 Desktop
dx, dy = 60, PY + PH + 260
DW, DH = 1440, 900
c.t(dx, dy - 18, "8 · Desktop landing, 1440 × 900 (standby)", 17, 700)
c.r(dx, dy, DW, DH, BG); c.r(dx - 0.5, dy - 0.5, DW + 1, DH + 1, "none", "#8f8c85")
from desktop import herb_landing
herb_landing(c, dx, dy, "standby", "Standby · last FOLD-D rev C · 14:02", "14:02 · round 6")
nx = dx + DW + 60
y2 = dy + 20
c.t(nx, y2, "Desktop notes", 17, 700); y2 += 30
for t_ in ["Reshaped (owner: responsive, no size leads): the fixed 600 px column is gone. I drew it first; at 1440 it left 840 px of grey and showed a sheet smaller than a phone in landscape.",
           "Now the work takes the width it can use, and the label sits in the bottom-right corner beside it: the herbarium's own place for a label. On a phone the label drops below the work. Same fields either way, all HTML text.",
           "Below the fold: everything else, newest first, three across (two on tablet, one on phone).",
           "All seven desktop frames: frames-desktop.png."]:
    y2 = c.wrap(nx, y2, t_, 520, 14, 400, INK2, lh=21) + 12
c.save(os.path.join(ROOT, "site/design/concepts/herbarium/frames-r1"))
print("herbarium ok")
