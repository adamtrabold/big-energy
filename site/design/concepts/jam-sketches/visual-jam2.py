"""Visual designer, site jam turn 2: phone sketches for A Lab Book, C Panel+Cabinet,
D The Set, plus the shared parts (lamp states, sheet-on-phone, audio row, palette, type).
Run: python3 visual-jam2.py  -> visual-jam2.svg + visual-jam2.png (rsvg-convert)
Sketch fidelity: words, layout and proportion are the point; content is real where cheap.
"""
import subprocess, warnings, base64, io, os
import numpy as np
from scipy.io import wavfile
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "../../../.."))

# palette (proposal)
BG = "#E6E4DF"      # site ground: warm light grey, cooler/darker than the sheets' cream
INK = "#1B1B19"
INK2 = "#5F5D58"
RULE = "#C4C1BA"
ON = "#23863F"      # the one signal colour (hue drawn: 131)
CREAM = "#F3EFE8"   # the sheets' own ground, for reference only
F = "Inter"

W, H = 2760, 1140
out = []
def a(s): out.append(s)
def t(x, y, s, size=13, w=400, fill=INK, anchor="start", ls=0, extra=""):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    a(f'<text x="{x}" y="{y}" font-family="{F}" font-size="{size}" font-weight="{w}" fill="{fill}" '
      f'text-anchor="{anchor}" letter-spacing="{ls}" style="font-feature-settings:\'tnum\'" {extra}>{s}</text>')
def r(x, y, w, h, fill="none", stroke=None, sw=1, op=1):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"{st} opacity="{op}"/>')
def l(x1, y1, x2, y2, c=RULE, sw=1):
    a(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{sw}"/>')
def lamp(x, y, state):
    if state == "on":
        a(f'<circle cx="{x}" cy="{y}" r="5" fill="{ON}"/>')
    elif state == "standby":
        a(f'<circle cx="{x}" cy="{y}" r="4.5" fill="none" stroke="{INK2}" stroke-width="1.2"/>')
def label(x, y, s, fill=INK2):
    t(x, y, s.upper(), 10.5, 500, fill, ls=0.9)

# sheet thumbnail (real FOLD sheet A, v1.1)
im = Image.open(os.path.join(ROOT, "versions/v1.1/fold/mock-A-look.png")).convert("RGB")
im.thumbnail((900, 640))
buf = io.BytesIO(); im.save(buf, "JPEG", quality=70)
SHEET = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
SW, SH = im.size
def sheet(x, y, w, op=1, crop=None, maxh=None):
    h = w * SH / SW
    if crop:  # crop = (fx, fy, fw, fh) as fractions; show region scaled into w x hh
        fx, fy, fw, fh = crop
        hh = w * (fh * SH) / (fw * SW)
        if maxh: hh = min(hh, maxh)
        cid = f"c{len(out)}"
        a(f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{hh}"/></clipPath>')
        sc = w / (fw * SW)
        a(f'<image href="{SHEET}" x="{x - fx*SW*sc}" y="{y - fy*SH*sc}" width="{SW*sc}" height="{SH*sc}" clip-path="url(#{cid})" opacity="{op}"/>')
        return hh
    a(f'<image href="{SHEET}" x="{x}" y="{y}" width="{w}" height="{h}" opacity="{op}"/>')
    return h

# waveform peaks (real: golden voice_bass_pluck.wav)
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    rate, d = wavfile.read(os.path.join(ROOT, "eng/sim/reference/out/golden/wav/voice_bass_pluck.wav"))
def wave_path(x, y, w, h, n=120):
    seg = np.array_split(np.abs(d), n)
    pk = np.array([s.max() for s in seg]); pk = pk / pk.max()
    pts = []
    for i, p in enumerate(pk):
        xx = x + i * w / (n - 1)
        pts.append(f"M{xx:.1f},{y - p*h/2:.1f}L{xx:.1f},{y + p*h/2:.1f}")
    a(f'<path d="{" ".join(pts)}" stroke="{INK}" stroke-width="1.4"/>')

a(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
r(0, 0, W, H, "#FFFFFF")
t(60, 70, "Project site · jam turn 2 · visual", 30, 700)
t(60, 100, "Phone sketches at 1:1 (390 × 844). Real content where cheap: FOLD sheet A v1.1, golden voice_bass_pluck.wav, owner quotes verbatim. Draws tag cd6dbb85.", 15, 400, INK2)

PW, PH, PY = 390, 844, 150
def phone(x, title, sub):
    r(x, PY, PW, PH, BG)
    r(x - 0.5, PY - 0.5, PW + 1, PH + 1, "none", "#9a978f", 1)
    t(x, PY + PH + 34, title, 18, 700)
    for i, line in enumerate(sub):
        t(x, PY + PH + 58 + i * 20, line, 13.5, 400, INK2)

def header(x, y, state, line):
    # common top: lamp + one status line, then project name
    lamp(x + 21, y + 26, state)
    label(x + 34, y + 30, line, INK if state == "on" else INK2)
    t(x + 16, y + 66, "( name to come )", 22, 600)
    t(x + 16, y + 88, "a portable Model D · stage: concept → lock", 13, 400, INK2)
    l(x + 16, y + 104, x + PW - 16, y + 104)

# ---------------- A: Lab Book ----------------
x = 60
phone(x, "A · Lab Book", ["Time-first. His words are the largest type.",
      "Fisheye rail: today wide, older days thin.", "Locks are ruled, signed pages."])
header(x, PY, "on", "On · round 6 sheets · since 14:02")
y = PY + 128
label(x + 16, y, "Waiting on you"); t(x + 16, y + 22, "Pick: ONE SHEET or FOLD for the park test", 15, 500)
l(x + 16, y + 40, x + PW - 16, y + 40)
# fisheye rail
rail = [("13 Nov", 360), ("12 Nov", 150), ("11", 50), ("10", 26), ("9", 14), ("…", 10)]
ry = y + 56
for name, hh in rail:
    r(x + 16, ry, 3, hh - 4, INK if name == "13 Nov" else RULE)
    t(x + 26, ry + 11, name, 10.5, 500, INK2)
    ry += hh
# entry today
ey = y + 76
t(x + 72, ey, "13 Nov · 11:47 · you said", 11, 500, INK2)
t(x + 72, ey + 34, "“i want to take this", 27, 500)
t(x + 72, ey + 68, "to the park and be", 27, 500)
t(x + 72, ey + 102, "inspired”", 27, 500)
t(x + 72, ey + 132, "→ branches round opened (3 designers)", 13, 400, INK2)
# figures
fy = ey + 150
sheet(x + 72, fy, 140); sheet(x + 220, fy, 140, op=0.38)
t(x + 72, fy + 116, "fig. 1  FOLD A · new", 11, 500)
t(x + 220, fy + 116, "fig. 2  dropped", 11, 500, INK2)
# signed lock
ly = fy + 140
l(x + 72, ly, x + PW - 16, ly, INK, 1.5); l(x + 72, ly + 4, x + PW - 16, ly + 4, INK, 1.5)
t(x + 72, ly + 24, "LOCKED v1.1 · 13 Nov", 12, 700, INK, ls=0.8)
t(x + 72, ly + 42, "FOLD stands at 120° · bend is a joystick", 12.5, 400, INK2)
# yesterday compressed
yy = ly + 74
t(x + 72, yy, "12 Nov · 22:30 · you said", 11, 500, INK2)
t(x + 72, yy + 24, "“Switch to Daisy Seed”", 18, 500)
t(x + 72, yy + 46, "+ 14 events · scores 9 9 9", 12.5, 400, INK2)
# speed dial at bottom
by = PY + PH - 54
l(x, by - 10, x + PW, by - 10)
for i, s in enumerate(["Day", "Round", "Version"]):
    cx = x + 70 + i * 125
    t(cx, by + 20, s, 14, 600 if i == 0 else 400, INK if i == 0 else INK2, "middle")
    if i == 0: r(cx - 22, by + 30, 44, 2, INK)

# ---------------- C: Panel + Cabinet ----------------
x = 60 + (PW + 110)
phone(x, "C · Panel (+ drawer cabinet)", ["Structure-first. One screen, never scrolls.",
      "Rows: the build chain. Columns: kinds.", "Scrubber: drag back = the project as it stood."])
header(x, PY, "standby", "Standby · last 14:02 · waiting on you")
cols = ["sheets", "diagr.", "docs", "tests", "rec."]
stages = ["Concept", "Lock", "Handoff", "Spec", "BOM", "Tests", "Boards", "Prints", "Assembly"]
counts = [[58, 12, 41, 0, 18], [11, 0, 9, 0, 2], [0, 2, 6, 0, 1], [0, 3, 19, 0, 0], [0, 0, 1, 0, 0],
          [0, 7, 2, 9, 0], [0]*5, [0]*5, [0]*5]
newc = {(0, 0), (0, 2), (5, 3)}
gx, gy = x + 96, PY + 150
cw, ch = 56, 50
for j, c in enumerate(cols):
    label(gx + j * cw + cw / 2 - 16, gy - 10, c)
for i, s in enumerate(stages):
    yy = gy + i * ch
    cur = (i == 1)
    if cur: r(x + 12, yy + 6, 3, ch - 12, INK)
    t(x + 22, yy + 30, s, 13, 600 if cur else 400, INK if i < 6 else INK2)
    for j in range(5):
        cx = gx + j * cw
        r(cx + 2, yy + 3, cw - 4, ch - 6, "#EFEDE9" if counts[i][j] else "none", RULE, 1)
        if counts[i][j]:
            t(cx + cw / 2, yy + 31, str(counts[i][j]), 16, 500, INK, "middle")
        else:
            t(cx + cw / 2, yy + 31, "·", 16, 400, RULE, "middle")
        if (i, j) in newc:
            a(f'<circle cx="{cx + cw - 9}" cy="{yy + 10}" r="3" fill="{INK}"/>')
# scrubber
sy = PY + PH - 92
l(x + 24, sy, x + PW - 24, sy, INK, 1.5)
marks = [(0.0, "r1"), (0.22, "r3"), (0.45, "r5"), (0.62, "v1"), (0.78, "v1.1"), (1.0, "now")]
for f, m in marks:
    mx = x + 24 + f * (PW - 48)
    big = m.startswith("v") or m == "now"
    l(mx, sy - (9 if big else 5), mx, sy + (9 if big else 5), INK, 1.5 if big else 1)
    t(mx, sy + 28, m, 12, 600 if big else 400, INK if big else INK2, "middle")
a(f'<rect x="{x + 24 + (PW-48) - 7}" y="{sy - 14}" width="14" height="28" fill="{INK}"/>')
t(x + 24, sy - 26, "13 Nov 14:02 · as it stands", 12, 500, INK2)

# ---------------- D: The Set ----------------
x = 60 + 2 * (PW + 110)
phone(x, "D · The Set (drawing register)", ["Document-first. Every publish is an Issue.",
      "Title block, revision table, sheet index.", "Δ marks = changed since you last looked."])
# title block
tb = PY + 16
r(x + 16, tb, PW - 32, 120, "none", INK, 1.2)
l(x + 16, tb + 70, x + PW - 16, tb + 70, INK, 1)
l(x + 230, tb + 70, x + 230, tb + 120, INK, 1)
t(x + 28, tb + 32, "( name to come )", 21, 600)
t(x + 28, tb + 54, "portable Model D · current set v1.1", 12.5, 400, INK2)
label(x + 28, tb + 88, "Issue"); t(x + 28, tb + 110, "14 · 13 Nov 14:02", 15, 600)
label(x + 242, tb + 88, "Status")
lamp(x + 248, tb + 106, "standby"); t(x + 260, tb + 111, "Standby", 14, 500, INK2)
# revision table
rt = tb + 148
label(x + 16, rt, "Revisions")
rows = [("v1.1", "13 Nov", "FOLD 120° · joystick · MIDI IN", True),
        ("v1", "13 Nov", "First lock: HUSH, ONE SHEET, FOLD", False),
        ("R5", "12 Nov", "Round 5 · 9 9 9", False)]
for i, (rv, dt, ds, cur) in enumerate(rows):
    yy = rt + 16 + i * 30
    l(x + 16, yy, x + PW - 16, yy)
    t(x + 16, yy + 20, rv, 13, 700 if cur else 500)
    t(x + 66, yy + 20, dt, 12.5, 400, INK2)
    t(x + 130, yy + 20, ds, 12.5, 400, INK if cur else INK2)
# sheet index
si = rt + 128
label(x + 16, si, "Sheet index · design")
idx = [("FOLD-A", "The look", "F", 2), ("FOLD-B", "Real size", "F", 2), ("FOLD-C", "Construction", "E", 0),
       ("FOLD-D", "Front", "G", 1), ("FOLD-E", "Standing", "B", 0), ("HUSH-A", "The look", "D", 0),
       ("ONE-A", "The look", "E", 0), ("FOLD113-A", "dropped", "C", -1)]
for i, (no, nm, rv, delta) in enumerate(idx):
    yy = si + 14 + i * 34
    op = 0.4 if delta == -1 else 1
    l(x + 16, yy, x + PW - 16, yy)
    a(f'<g opacity="{op}">')
    t(x + 16, yy + 23, no, 13, 600)
    t(x + 116, yy + 23, nm, 13, 400, INK2 if delta == -1 else INK)
    t(x + 300, yy + 23, "rev " + rv, 12.5, 400, INK2)
    a('</g>')
    if delta > 0:
        tx, ty = x + PW - 32, yy + 18
        a(f'<path d="M{tx},{ty-10} L{tx+10},{ty+7} L{tx-10},{ty+7} Z" fill="none" stroke="{INK}" stroke-width="1.3"/>')
        t(tx, ty + 4, str(delta), 9.5, 700, INK, "middle")
label(x + 16, si + 14 + 8 * 34 + 26, "Tests · Spec · BOM · Boards · Records  ›")

# ---------------- Sheet on a phone ----------------
x = 60 + 3 * (PW + 110)
phone(x, "All · an A3 sheet on a phone", ["Fit-width first (unreadable on purpose: it’s the map).",
      "Then ‘read’ steps through crops the sheet renderer", "already knows. Pinch for full-res at any time."])
t(x + 16, PY + 36, "‹  FOLD · sheet A — the look", 14, 600)
t(x + 16, PY + 56, "v1.1 · rev F · 4961 × 3508", 12, 400, INK2)
hh = sheet(x + 16, PY + 72, PW - 32)
# crop boxes drawn on the map
bx = [(0.11, 0.13, 0.43, 0.48), (0.66, 0.36, 0.23, 0.24), (0.03, 0.80, 0.97, 0.10)]
for i, (fx, fy, fw, fh) in enumerate(bx):
    X = x + 16 + fx * (PW - 32); Y = PY + 72 + fy * hh
    r(X, Y, fw * (PW - 32), fh * hh, "none", INK, 1.3)
    t(X + 4, Y + 13, str(i + 1), 11, 700)
cy = PY + 72 + hh + 24
label(x + 16, cy, "Read · 1 of 3 · the hero")
h2 = sheet(x + 16, cy + 12, PW - 32, crop=(0.11, 0.13, 0.43, 0.48))
r(x + 16, cy + 12, PW - 32, h2, "none", RULE)
by = cy + 12 + h2 + 26
label(x + 16, by, "Read · 2 of 3 · principles")
by2 = PY + PH - 50
h3 = sheet(x + 16, by + 12, PW - 32, crop=(0.66, 0.36, 0.23, 0.24), maxh=by2 - 22 - (by + 12))
by2 = PY + PH - 50
l(x, by2 - 10, x + PW, by2 - 10)
t(x + 16, by2 + 18, "‹ sheet D", 14, 400, INK2); t(x + PW - 16, by2 + 18, "sheet B ›", 14, 400, INK2, "end")
t(x + PW / 2, by2 + 18, "1 / 3", 14, 500, INK, "middle")

# ---------------- right column: parts ----------------
X0 = 60 + 4 * (PW + 110) - 30
t(X0, PY + 10, "Shared parts (all directions)", 18, 700)
# lamp states
y = PY + 50
label(X0, y, "The status lamp · three states, never a lie")
states = [("on", "On", "a session is working · says what · since when"),
          ("standby", "Standby", "nothing running · last seen 14:02 · auto after 20 min silence"),
          (None, "Snapshot 13 Nov 14:02", "signed-out viewer: no live data, so no lamp at all")]
for i, (s, n, d_) in enumerate(states):
    yy = y + 30 + i * 48
    lamp(X0 + 8, yy - 4, s)
    if s is None:
        a(f'<line x1="{X0+3}" y1="{yy-4}" x2="{X0+13}" y2="{yy-4}" stroke="{RULE}" stroke-width="1.5"/>')
    t(X0 + 24, yy, n, 15, 600)
    t(X0 + 24, yy + 19, d_, 12.5, 400, INK2)
# audio row
y = y + 190
label(X0, y, "A test, with its sound · real waveform")
r(X0, y + 14, 580, 132, BG)
a(f'<circle cx="{X0 + 36}" cy="{y + 60}" r="20" fill="none" stroke="{INK}" stroke-width="1.5"/>')
a(f'<path d="M{X0+30},{y+50} L{X0+44},{y+60} L{X0+30},{y+70} Z" fill="{INK}"/>')
wave_path(X0 + 72, y + 60, 430, 46)
l(X0 + 72 + 0.31 * 430, y + 30, X0 + 72 + 0.31 * 430, y + 90, INK, 1.5)
t(X0 + 520, y + 65, "0:00.6 / 1.98", 12, 500, INK2)
t(X0 + 16, y + 112, "Bass pluck · golden", 14, 600)
t(X0 + 16, y + 132, "PASS · 48 kHz · A/B: golden | perturbed (keeps playhead)", 12.5, 400, INK2)
# palette
y = y + 180
label(X0, y, "Colour · the frame recedes; the work carries colour")
sw = [(BG, "ground", "#E6E4DF"), ("#EFEDE9", "cell", "#EFEDE9"), (RULE, "rule", "#C4C1BA"),
      (INK2, "ink 2", "#5F5D58"), (INK, "ink", "#1B1B19"), (ON, "ON only", "#23863F")]
for i, (c, n, hx) in enumerate(sw):
    xx = X0 + i * 97
    r(xx, y + 14, 86, 52, c, "#9a978f" if c in (BG, "#EFEDE9") else None)
    t(xx, y + 84, n, 12.5, 600); t(xx, y + 102, hx, 11.5, 400, INK2)
t(X0, y + 128, "No red or orange anywhere in the frame: those belong to the sheets.", 12.5, 400, INK2)
# type
y = y + 162
label(X0, y, "Type · Inter (the sheets’ own face), tabular figures")
t(X0, y + 40, "His words 27/34", 27, 500)
t(X0, y + 70, "Project 22 · Item 15 semibold", 18, 600)
t(X0, y + 94, "Body 15/22 · Meta 12.5 ink 2", 15, 400)
label(X0, y + 116, "Label 10.5 caps +0.9 tracking", INK)
t(X0, y + 142, "Four sizes on the phone. No other weights than 400/500/600/700.", 12.5, 400, INK2)

a("</svg>")
svg = os.path.join(HERE, "visual-jam2.svg")
open(svg, "w").write("\n".join(out))
subprocess.run(["rsvg-convert", "-o", os.path.join(HERE, "visual-jam2.png"), svg], check=True)
print("ok")
