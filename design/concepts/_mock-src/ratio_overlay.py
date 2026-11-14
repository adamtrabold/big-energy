"""CATHEDRAL case ratio constructions drawn over each layout's exact top view (director: derived from the device).
A (sqrt5 / 9:4 face) on P5R at D 132; C (double-square face) on P5OB-D at D 147.3. Labels in a band above."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figs_rb as f
from PIL import Image, ImageDraw, ImageFont
exec(open('/tmp/scr/ct3_fig.py').read().split("W = 1200")[0]) if os.path.exists('/tmp/scr/ct3_fig.py') else None
FB = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"; FR = "/usr/share/fonts/opentype/inter/Inter-Regular.otf"
BG = (243, 239, 232); INK = (40, 36, 32); LINE = (176, 58, 46)    # construction in a red-brown, so it reads over cream and walnut
W, WALL = 286.0, 4.3
def compose(src, D, out_name, title, sub, draw):
    im = Image.open(os.path.join(f.OUT, src)).convert("RGB")
    try: im = brassify(im)
    except Exception: pass
    ppm = im.width / (W + 4.0); ymax = 2 * D + 4.0
    P = lambda x, y: ((x + 2.0) * ppm, (ymax - y) * ppm)
    d = ImageDraw.Draw(im)
    lw = max(3, int(ppm * 0.45))
    draw(d, P, lw, D)
    band = int(ppm * 30)
    out = Image.new("RGB", (im.width, im.height + band + int(ppm * 10)), BG)
    out.paste(im, (0, band))
    dd = ImageDraw.Draw(out)
    dd.text((ppm * 6, ppm * 12), title, font=ImageFont.truetype(FB, int(ppm * 7.5)), fill=INK, anchor="ls")
    dd.text((ppm * 6, ppm * 23), sub, font=ImageFont.truetype(FR, int(ppm * 5.0)), fill=INK, anchor="ls")
    f.scale_bar(dd, ppm * 6, out.height - ppm * 7, ppm, 20)
    p = f.dest("cathedral", out_name); out.save(p, optimize=True); print(p, out.size, round(ppm, 2))

def faces(D):
    return [(WALL, WALL, W - WALL, D - WALL), (WALL, D + 2 + WALL, W - WALL, 2 * D + 2 - WALL)]   # base, lid

def draw_A(d, P, lw, D):
    for x0, y0, x1, y1 in faces(D):
        h = y1 - y0; xs = 143.0 - h / 2
        d.rectangle([P(xs, y1), P(xs + h, y0)], outline=LINE, width=lw)            # the square, centred on the axis
        for xa in (x0, x1):                                                         # the two wings (≈ golden), dashed edge
            pass
        d.rectangle([P(x0, y1), P(x1, y0)], outline=LINE, width=max(2, lw // 2))   # the face's own rectangle

def draw_C(d, P, lw, D):
    F = faces(D)
    for x0, y0, x1, y1 in F:
        d.rectangle([P(x0, y1), P(x1, y0)], outline=LINE, width=max(2, lw // 2))
        d.line([P(143.0, y0), P(143.0, y1)], fill=LINE, width=lw)                  # the seam between the two squares
        for a, b in ((x0, 143.0), (143.0, x1)):
            d.line([P(a, y0), P(b, y1)], fill=LINE, width=max(2, lw // 2))         # each square's diagonal
    # (the open pair's one-square X is left off: it nearly coincides with the squares' diagonals and read as doubled lines)

if __name__ == "__main__":
    compose("rb_nv5_R_top.png", 132.0, "cathedral-s9-P5R-ratio-A-top-9.9px-per-mm.png",
            "A  √5 face (≈ 9 : 4) on P5R  ·  286 × 132 per half",
            "each face 277.4 × 123.4 = a square on the axis (the window's bay) with a ≈ golden wing either side", draw_A)
    compose("rb_s9_P5OBD_C_top.png", 147.3, "cathedral-s9-P5OBD-ratio-C-top-9.9px-per-mm.png",
            "C  double-square face on P5OB-D  ·  286 × 147.3 per half",
            "each face 277.4 × 138.7 = two squares; their seam is the axis, through the window and cutoff", draw_C)
