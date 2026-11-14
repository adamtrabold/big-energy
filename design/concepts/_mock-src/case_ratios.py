# CATHEDRAL case ratio candidates, true scale silhouettes (no words; captions in the look doc)
import math, sys
sys.path.insert(0, '/home/claude/big-energy/design/concepts/_mock-src')
import figs_rb as f
from PIL import Image, ImageDraw
P = 4.0; S = 3                                   # px per mm (final), supersample
W, WALL, SEAM, CL = 286.0, 4.3, 2.0, 55.2
RC, RP, N = 28.3, 24.0, 5.0
CANDS = [("A", 132.44, 277.4 / 56), ("B", 143.0, 277.4 / 56), ("C", 147.3, 277.4 / 56)]
BG = (243, 239, 232); WAL = (110, 70, 40); CREAM = (238, 232, 218); GRID = (205, 196, 178); BRASS = (190, 150, 70); INK = (40, 36, 32)
def sq(x0, y0, x1, y1, rc, k=160):
    pts = []
    for i in range(4 * k):
        th = 2 * math.pi * i / (4 * k); c, sn = math.cos(th), math.sin(th)
        cx = x1 - rc if c >= 0 else x0 + rc; cy = y1 - rc if sn >= 0 else y0 + rc
        pts.append((cx + rc * math.copysign(abs(c) ** (2 / N), c), cy + rc * math.copysign(abs(sn) ** (2 / N), sn)))
    return pts
colw = W + 40; gap_r = 24
heights = [max(D for _, D, _ in CANDS), CL, 2 * max(D for _, D, _ in CANDS) + SEAM, max(D for _, D, _ in CANDS) - 2 * WALL]
TOT_H = 20 + sum(heights) + gap_r * 4 + 20
img = Image.new("RGB", (int(len(CANDS) * colw * P * S + 40 * P * S), int((TOT_H + 14) * P * S)), BG)
d = ImageDraw.Draw(img)
def X(v): return v * P * S
def poly(pts, ox, oy, fill=None, outline=None, w=1):
    d.polygon([(X(ox + x), X(oy + y)) for x, y in pts], fill=fill, outline=outline, width=w)
for ci, (nm, D, M) in enumerate(CANDS):
    ox = 20 + ci * colw + 20
    y = 20
    # 1. closed, from above (the lid back), aligned to the row's bottom so the depths compare
    top = y + heights[0] - D
    poly(sq(0, 0, W, D, RC), ox, top, fill=WAL)
    poly(sq(WALL, WALL, W - WALL, D - WALL, RP), ox, top, fill=(124, 82, 50))
    y += heights[0] + gap_r
    # 2. closed, front elevation (thickness 55.2)
    d.rounded_rectangle([X(ox), X(y), X(ox + W), X(y + CL)], radius=X(6), fill=WAL)
    d.line([X(ox + 6), X(y + CL - 15.6), X(ox + W - 6), X(y + CL - 15.6)], fill=(70, 45, 26), width=S * 2)
    y += heights[1] + gap_r
    # 3. open flat: two halves and the seam
    top = y + heights[2] - (2 * D + SEAM)
    for yy in (top, top + D + SEAM):
        poly(sq(0, 0, W, D, RC), ox, yy, fill=WAL)
        poly(sq(WALL, WALL, W - WALL, D - WALL, RP), ox, yy, fill=CREAM)
    y += heights[2] + gap_r
    # 4. one face with its module grid and the ratio's construction
    fw, fh = W - 2 * WALL, D - 2 * WALL
    top = y + heights[3] - fh
    poly(sq(0, 0, fw, fh, RP), ox + WALL, top, fill=CREAM, outline=GRID, w=S)
    gx = ox + WALL
    mask = Image.new("L", img.size, 0); ImageDraw.Draw(mask).polygon([(X(gx + x), X(top + y)) for x, y in sq(0, 0, fw, fh, RP)], fill=255)
    layer = img.copy(); d_main = d; d = ImageDraw.Draw(layer)
    i = 0
    while i * M <= fw + 1e-6:
        d.line([X(gx + i * M), X(top), X(gx + i * M), X(top + fh)], fill=GRID, width=1 if i % 4 else S); i += 1
    j = 0
    while j * M <= fh + 1e-6:
        d.line([X(gx), X(top + fh - j * M), X(gx + fw), X(top + fh - j * M)], fill=GRID, width=1 if j % 4 else S); j += 1
    img.paste(layer, (0, 0), mask); d = d_main
    bw = S * 2
    if nm == "A":    # sqrt5 ~ 9:4: a centred square with a golden rectangle each side
        s_ = fh; xs = gx + (fw - s_) / 2
        d.rectangle([X(xs), X(top), X(xs + s_), X(top + fh)], outline=BRASS, width=bw)
    elif nm in ("B", "C"):   # two squares (B: the case; C: the face)
        if nm == "C":
            d.line([X(gx + fw / 2), X(top), X(gx + fw / 2), X(top + fh)], fill=BRASS, width=bw)
            d.line([X(gx), X(top + fh), X(gx + fw / 2), X(top)], fill=BRASS, width=bw); d.line([X(gx + fw / 2), X(top + fh), X(gx + fw), X(top)], fill=BRASS, width=bw)
    # B's double square is the case outline: draw on the closed plan
    if nm == "B":
        t0 = 20 + heights[0] - D
        d.line([X(ox + W / 2), X(t0), X(ox + W / 2), X(t0 + D)], fill=BRASS, width=bw)
        d.line([X(ox), X(t0 + D), X(ox + W / 2), X(t0)], fill=BRASS, width=bw); d.line([X(ox + W / 2), X(t0 + D), X(ox + W), X(t0)], fill=BRASS, width=bw)
        # and the open case as one square
        t3 = 20 + heights[0] + gap_r + heights[1] + gap_r + heights[2] - (2 * D + SEAM)
        d.line([X(ox), X(t3 + 2 * D + SEAM), X(ox + W), X(t3)], fill=BRASS, width=bw); d.line([X(ox), X(t3), X(ox + W), X(t3 + 2 * D + SEAM)], fill=BRASS, width=bw)
    if nm == "C":    # the two faces together, open, make a square
        t3 = 20 + heights[0] + gap_r + heights[1] + gap_r + heights[2] - (2 * D + SEAM)
        d.line([X(ox + WALL), X(t3 + WALL), X(ox + W - WALL), X(t3 + 2 * D + SEAM - WALL)], fill=BRASS, width=bw)
        d.line([X(ox + WALL), X(t3 + 2 * D + SEAM - WALL), X(ox + W - WALL), X(t3 + WALL)], fill=BRASS, width=bw)
img = img.resize((img.width // S, img.height // S), Image.LANCZOS)
# labels (coordinator: the owner must be able to read it): column headings, row labels, the scale bar's unit
from PIL import ImageFont
FB = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"; FR = "/usr/share/fonts/opentype/inter/Inter-Regular.otf"
LW, TH = 78.0, 40.0                                         # left label column, top heading band (mm)
out = Image.new("RGB", (int(img.width + LW * P), int(img.height + TH * P)), BG)
out.paste(img, (int(LW * P), int(TH * P)))
dd = ImageDraw.Draw(out)
fh, fs = ImageFont.truetype(FB, int(P * 8.0)), ImageFont.truetype(FR, int(P * 6.0))
HEAD = {"A": ("A  √5 face (≈ 9 : 4)", "286 × 132.4 · face 2.24 : 1"),
        "B": ("B  double-square case", "286 × 143 · case 2 : 1, open ≈ square"),
        "C": ("C  double-square face", "286 × 147.3 · face 2 : 1 (recommended)")}
for ci, (nm, D, M) in enumerate(CANDS):
    x = (LW + 20 + ci * colw + 20) * P
    dd.text((x, P * 16), HEAD[nm][0], font=fh, fill=INK, anchor="ls")
    dd.text((x, P * 27), HEAD[nm][1], font=fs, fill=INK, anchor="ls")
    dd.text((x, P * 15), "", font=fs, fill=INK)
rows = ["closed, plan", "closed, front", "open flat", "face + grid"]
y = 20.0
for k, lab in enumerate(rows):
    yc = TH + y + heights[k] / 2
    dd.text((P * 6, yc * P), lab, font=fh, fill=INK, anchor="lm")
    y += heights[k] + gap_r
f.scale_bar(dd, (LW + 20) * P, out.height - P * 10, P, 50); dd.rectangle([(LW + 20 + 50) * P + 2, out.height - P * 14, (LW + 20 + 50) * P + P * 12, out.height - P * 4], fill=BG); dd.text(((LW + 20 + 50) * P + P * 2, out.height - P * 10 + 1), "50 mm", font=fs, fill=INK, anchor="lm")
dd.text(((LW + 20 + 50) * P + P * 30, out.height - P * 10 + 1), "(true scale, 4 px per mm)", font=fs, fill=INK, anchor="lm")
img = out
p = f.dest("cathedral", "cathedral-s9-case-ratios-4px-per-mm.png"); img.save(p, optimize=True); print(p, img.size)
for nm, D, M in CANDS:
    fh = D - 8.6
    print(nm, "D", D, "case", round(W / D, 3), "face", round(277.4 / fh, 3), "open", round((2 * D + 2) / W, 3), "face in M", round(277.4 / M, 2), "x", round(fh / M, 2))
