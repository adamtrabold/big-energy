# Branches jam turn 2 (visual) quick sketches. Not render-grade; for judging ideas.
# Run: python3 -I sketch_turn2.py   (writes PNGs next to this file)
# Layout is read from ../../../concepts/_mock-src/fold_r5_check.py (ONE SHEET x = FOLD x - 5; flat rows 68/100/123/146).
import math, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "../../../concepts/_mock-src/fold_r5_check.py")
g = {}; exec(open(SRC).read().split("def check")[0], g)
FONT = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
FONTB = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
SER = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
def F(s, b=False): return ImageFont.truetype(FONTB if b else FONT, s)

INK = (46, 41, 36); RED = (196, 72, 40)
SHARPS_AFTER = [0, 1, 3, 4, 5, 7, 8, 10, 11, 12]

def flat_items(dx=-5):
    Y = {"P": 68, "V1": 100, "V2": 123, "FX": 146}
    it = []
    for e in g["play"]:
        it.append((e[0], e[1] + dx, Y["P"] if len(e) <= 4 else e[4], e[2], e[3]))
    for n, x, r, k in g["v1"]: it.append((n, x + dx, Y["V1"], r, k))
    for n, x, r, k in g["v2"]: it.append((n, x + dx, Y["V2"], r, k))
    for n, x, r, k in g["fx"]: it.append((n, x + dx, Y["FX"], r, k))
    for n, x, r, k in g["sw_flat"]: it.append((n, x + dx, 111.5, r, k))
    return it

def pegs(dx=0):
    w = [(17 + 18 * n + dx, 13.5, 6.35, "white") for n in range(15)]
    s = [(8 + 18 * (i + 1) + dx, 36.0, 6.35, "sharp") for i in SHARPS_AFTER]
    return w + s

# ------------------------------------------------------------------ 1. RAIN (new branch)
def rain(path, S=6, pitch=1.1):
    W, D = 276, 180
    it = flat_items()
    stones = [(x, y, r + 0.3) for n, x, y, r, k in it if k != "l"] + [(x, y, r + 0.6) for x, y, r, _ in pegs()]
    H, Wp = D * S, W * S
    ys, xs = np.mgrid[0:H, 0:Wp]
    X = xs / S; Y = D - ys / S                     # y up from the front edge
    best = np.full(X.shape, 1e9); second = np.full(X.shape, 1e9)
    for (sx, sy, sr) in stones:
        d = np.hypot(X - sx, Y - sy) - sr
        second = np.where(d < best, best, np.minimum(second, d))
        best = np.minimum(best, d)
    ring = 0.5 + 0.5 * np.cos(2 * np.pi * best / pitch)
    seam = np.clip((second - best) / 0.35, 0, 1)     # meeting lines of two ripple fields stay smooth
    edge = np.clip(np.minimum.reduce([X - 3, W - 3 - X, Y - 3, D - 3 - Y]) / 2, 0, 1)
    lines = (ring > 0.78) * seam * edge * (best > 0.4)
    base = np.array([221, 218, 205], float)          # pale stone (wet slate after rain)
    lineC = np.array([176, 176, 160], float)
    img = base[None, None, :] * (1 - lines[..., None]) + lineC[None, None, :] * lines[..., None]
    im = Image.fromarray(img.astype(np.uint8)); d = ImageDraw.Draw(im)
    P = lambda x, y: (x * S, (D - y) * S)
    d.rounded_rectangle([0, 0, Wp - 1, H - 1], radius=6 * S, outline=(150, 146, 132), width=3)
    for n, x, y, r, k in it:
        cx, cy = P(x, y)
        if k == "k":
            col = (214, 168, 46) if n == "CUTOFF" else (236, 230, 214)
            d.ellipse([cx - r * S, cy - r * S, cx + r * S, cy + r * S], fill=col, outline=(120, 112, 96), width=2)
            d.line([cx, cy, cx, cy - r * S * 0.85], fill=INK, width=3)
        elif k == "t":
            d.ellipse([cx - r * S, cy - r * S, cx + r * S, cy + r * S], fill=(200, 196, 184), outline=(120, 112, 96), width=2)
            d.ellipse([cx - 1.6 * S, cy - 1.6 * S, cx + 1.6 * S, cy + 1.6 * S], fill=(90, 86, 80))
        elif k == "b":
            d.ellipse([cx - r * S, cy - r * S, cx + r * S, cy + r * S], fill=(240, 236, 226), outline=(120, 112, 96), width=2)
        elif k == "stick":
            d.ellipse([cx - 5 * S, cy - 5 * S, cx + 5 * S, cy + 5 * S], fill=(40, 38, 36))
        elif k == "l":
            d.ellipse([cx - r * S, cy - r * S, cx + r * S, cy + r * S], fill=(120, 190, 110) if n == "status" else (200, 80, 60))
    for x, y, r, kind in pegs():
        cx, cy = P(x, y)
        col = (128, 126, 118) if kind == "white" else (92, 90, 84)
        d.ellipse([cx - r * S, cy - r * S, cx + r * S, cy + r * S], fill=col, outline=(70, 68, 62), width=2)
        d.ellipse([cx - r * S * 0.55, cy - r * S * 0.7, cx + r * S * 0.1, cy - r * S * 0.2], fill=tuple(min(255, c + 40) for c in col))
    # proposed SYNC toggle in front of ECHO TIME (FOLD x 133, d 71 -> flat: rules-only fit, labels not yet checked)
    sx, sy = 133 - 5, 146 - 12.85
    cx, cy = P(sx, sy)
    d.ellipse([cx - 4.6 * S, cy - 4.6 * S, cx + 4.6 * S, cy + 4.6 * S], fill=(200, 196, 184), outline=RED, width=3)
    d.text((cx + 6 * S, cy - 2 * S), "SYNC?", font=F(int(2.4 * S), True), fill=RED)
    im.save(path)
    return im

# ------------------------------------------------------------------ 2. CHAMBER: closed bar = organ facade
def chamber(path, S=5):
    W, D = 286, 108
    im = Image.new("RGB", (W * S, int((D + 70) * S)), (244, 240, 232)); d = ImageDraw.Draw(im)
    # lid back, closed, seen from above: walnut
    d.rounded_rectangle([0, 0, W * S, D * S], radius=12 * S, fill=(107, 68, 41))
    rng = np.random.default_rng(7)
    for i in range(70):                                # grain hint
        y = rng.uniform(4, D - 4) * S
        d.line([(10 * S, y), (W * S - 10 * S, y + rng.uniform(-6, 6) * S)], fill=(98, 61, 37), width=1)
    # facade: 25 pipes, lengths prop. to the real scale 2^(-n/12), mirrored "tower" layout (longest centre)
    lens = [2 ** (-n / 12) for n in range(25)]          # C (longest) ... C two octaves up
    order = []                                          # organ builders place pipes alternately left/right from the centre
    for i, L in enumerate(lens): order.append(L)
    slots = [None] * 25; c = 12
    for i, L in enumerate(order):
        k = (i + 1) // 2 * (1 if i % 2 else -1)
        slots[c + k] = L
    pw, gap = 6.2, 2.6
    x0 = (W - (25 * pw + 24 * gap)) / 2
    ybase = D - 18
    for i, L in enumerate(slots):
        h = 18 + 58 * L
        xa = (x0 + i * (pw + gap)) * S
        top = (ybase - h) * S
        d.rounded_rectangle([xa, top, xa + pw * S, ybase * S], radius=int(pw * S / 2), fill=(196, 160, 96), outline=(150, 112, 60), width=2)
        my = ybase * S - h * S * 0.22                  # pipe mouth
        d.polygon([(xa + 1.0 * S, my), (xa + pw * S - 1.0 * S, my), (xa + pw * S / 2, my - 3.2 * S)], fill=(90, 58, 30))
        d.rectangle([xa + 1.0 * S, my, xa + pw * S - 1.0 * S, my + 1.2 * S], fill=(90, 58, 30))
    d.line([(x0 * S - 6 * S, ybase * S), ((W - x0) * S + 6 * S, ybase * S)], fill=(196, 160, 96), width=4)
    d.text((W * S / 2, (ybase + 8) * S), "little d", font=ImageFont.truetype(SER, int(4.4 * S)), fill=(214, 184, 120), anchor="mm")
    # open keyboard strip below: reverse colours, pegs
    ky = D + 12
    d.rounded_rectangle([0, ky * S, W * S, (ky + 50) * S], radius=4 * S, fill=(241, 235, 221))
    for x, y, r, kind in pegs(dx=5):
        cx, cy = x * S, (ky + 50 - y) * S
        col = (74, 46, 28) if kind == "white" else (226, 206, 168)
        d.ellipse([cx - r * S, cy - r * S, cx + r * S, cy + r * S], fill=col, outline=(40, 26, 16), width=2)
        d.ellipse([cx - r * S * 0.5, cy - r * S * 0.65, cx, cy - r * S * 0.25], fill=tuple(min(255, c + 45) for c in col))
    im.save(path)

# ------------------------------------------------------------------ 3. GROUND -> HORN: side section + underside
def horn(path, S=5):
    im = Image.new("RGB", (330 * S, 150 * S), (244, 240, 232)); d = ImageDraw.Draw(im)
    gy = 120
    d.line([(0, gy * S), (330 * S, gy * S)], fill=(110, 140, 80), width=6)          # grass
    for i in range(0, 330, 4):
        d.line([(i * S, gy * S), ((i + 1.5) * S, (gy - 3) * S)], fill=(110, 150, 80), width=2)
    rake = math.radians(12); L = 180
    fx, fy = 40, gy - 2                                   # front edge on the ground
    def pt(u, v):  # u along panel depth (front->back), v up from panel underside
        return ((fx + u * math.cos(rake) - v * math.sin(rake)) * S, (fy - u * math.sin(rake) - v * math.cos(rake)) * S)
    # body (cream) 24 thick
    d.polygon([pt(0, 0), pt(L, 0), pt(L, 24), pt(0, 24)], fill=(232, 220, 194), outline=(150, 140, 120))
    # wedge (persimmon), ground to panel underside
    back = pt(L, 0)
    d.polygon([pt(4, 0), pt(L, 0), (back[0], gy * S), ((fx + 4) * S, gy * S)], fill=(226, 100, 52), outline=(170, 70, 30))
    # folded horn path inside the wedge: speaker throat under rear of panel -> flares to a mouth at the back
    sp = pt(L - 40, 0)
    d.ellipse([sp[0] - 13 * S, sp[1] - 2 * S, sp[0] + 13 * S, sp[1] + 6 * S], fill=(60, 50, 44))
    hp = [pt(L - 40, -4), pt(75, -9), pt(70, -12), pt(95, -16), pt(L - 4, -30)]
    for w, a in ((9, (246, 170, 120)), (3, (120, 50, 20))):
        d.line(hp, fill=a, width=w, joint="curve")
    mouth_top = pt(L, -2); d.line([mouth_top, (back[0], (gy - 3) * S)], fill=(40, 30, 26), width=8)
    d.text((back[0] + 4 * S, (gy - 30) * S), "mouth\n(rear + sides)", font=F(int(3.2 * S)), fill=INK)
    # PIERCED's carry job, moved here: a finger pocket in the wedge's rear, under the panel (no added length)
    pk = [back[0] - 26 * S, (gy - 26) * S, back[0] - 4 * S, (gy - 12) * S]
    for i in range(int(pk[0]), int(pk[2]), 3 * S): d.line([(i, pk[1]), (min(i + 1.5 * S, pk[2]), pk[1])], fill=INK, width=2); d.line([(i, pk[3]), (min(i + 1.5 * S, pk[2]), pk[3])], fill=INK, width=2)
    d.text((back[0] + 4 * S, (gy - 14) * S), "finger pocket (carry)\nfrom PIERCED, felt-lined", font=F(int(3.2 * S)), fill=INK)
    # pegs / knobs hint on top
    for u in (14, 36):
        p = pt(u, 24); d.ellipse([p[0] - 5 * S, p[1] - 6 * S, p[0] + 5 * S, p[1] + 1 * S], fill=(130, 128, 120))
    for u in (68, 100, 123, 146):
        p = pt(u, 24); d.rectangle([p[0] - 7 * S, p[1] - 13 * S, p[0] + 7 * S, p[1]], fill=(236, 230, 214), outline=(120, 112, 96))
    d.text((8 * S, 8 * S), "player sits here (left) · front edge on the grass", font=F(int(3.4 * S), True), fill=INK)
    d.text((fx * S, (gy + 8) * S), "12° rake = ≈ 37 mm at the back over 180 deep · cream on top (calm) · persimmon underneath (loud) · the wedge is a folded horn", font=F(int(3.4 * S)), fill=INK)
    im.save(path)

# ------------------------------------------------------------------ 4. BUTTERFLY reshaped: printed sheet + REAL live-edge walnut rail
def butterfly(path, S=5):
    W, D, rail, CREAM = 276, 180, 22, 160.0
    im = Image.new("RGB", (W * S + 40, int((CREAM + rail + 16) * S)), (244, 240, 232)); d = ImageDraw.Draw(im)
    ox = 20
    rng = np.random.default_rng(11)
    # live edge: smooth random walk
    xs = np.linspace(0, W, 120); n = np.cumsum(rng.normal(0, 0.9, 120)); n -= np.linspace(n[0], n[-1], 120)
    n = np.convolve(n, np.ones(9) / 9, mode="same")
    edge = [(ox + x * S, (6 + 9 + v * 1.6) * S) for x, v in zip(xs, n)]
    railtop = rail + 10
    poly = edge + [(ox + W * S, railtop * S), (ox, railtop * S)]
    d.polygon(poly, fill=(92, 58, 36))
    d.line(edge, fill=(170, 130, 90), width=5)                      # sapwood band
    for i in range(14):
        y0 = rng.uniform(18, railtop - 3) * S
        d.line([(ox, y0), (ox + W * S, y0 + rng.uniform(-8, 8) * S)], fill=(80, 50, 30), width=1)
    d.rectangle([ox, railtop * S, ox + W * S, (railtop + CREAM) * S], fill=(232, 220, 194))
    d.line([(ox, railtop * S), (ox + W * S, railtop * S)], fill=(60, 40, 26), width=2)
    # butterflies across the joint
    for bx in (138,):   # one butterfly on the axis, in the centre break; the jacks own the right of the rail
        cx, cy = ox + bx * S, railtop * S
        a, b, c = 7 * S, 3.6 * S, 2.0 * S
        d.polygon([(cx - c, cy - a), (cx + c, cy - a), (cx + b, cy), (cx + c, cy + a), (cx - c, cy + a), (cx - b, cy)], fill=(60, 36, 22))
        d.polygon([(cx - c * 0.2, cy - a), (cx - b * 1.6, cy - a * 0.95), (cx - b * 1.2, cy), (cx - b * 1.6, cy + a * 0.95), (cx - c * 0.2, cy + a),
                   (cx + c * 0.2, cy + a), (cx + b * 1.6, cy + a * 0.95), (cx + b * 1.2, cy), (cx + b * 1.6, cy - a * 0.95), (cx + c * 0.2, cy - a)], fill=(60, 36, 22))
    # jacks drilled in the wood rail's back face (shown as dots on the rail top edge)
    for i, jx in enumerate(range(152, 262, 15)):
        d.ellipse([ox + jx * S - 3 * S, (railtop - 9) * S - 3 * S, ox + jx * S + 3 * S, (railtop - 9) * S + 3 * S], fill=(30, 22, 16))
    # face controls (rows only, simplified)
    it = flat_items(); top = railtop + CREAM
    for nme, x, y, r, k in it:
        cx, cy = ox + x * S, (top - y) * S
        if k == "k":
            col = (196, 72, 40) if nme == "CUTOFF" else (236, 230, 214)
            d.ellipse([cx - r * S, cy - r * S, cx + r * S, cy + r * S], fill=col, outline=(120, 112, 96), width=2)
        elif k in ("t", "b"):
            d.ellipse([cx - r * S, cy - r * S, cx + r * S, cy + r * S], fill=(210, 204, 190), outline=(120, 112, 96), width=2)
    for i in range(15):
        d.rectangle([ox + (3.3 + 18 * i) * S, (top - 30) * S, ox + (20.7 + 18 * i) * S, top * S], fill=(250, 248, 242), outline=(170, 160, 140))
    for i in SHARPS_AFTER:
        xc = 3 + 18 * (i + 1)
        d.rectangle([ox + (xc - 8) * S, (top - 46) * S, ox + (xc + 8) * S, (top - 32) * S], fill=(40, 36, 32))
    im.save(path)

# ------------------------------------------------------------------ 5. PIERCED, shy: a felt-lined slot, not a big round hole
def pierced(path, S=5):
    W, D, add = 276, 180, 32
    im = Image.new("RGB", ((W + add) * S + 40, (D + 60) * S), (244, 240, 232)); d = ImageDraw.Draw(im)
    ox, oy = 20, 10
    d.rounded_rectangle([ox, oy * S, ox + (W + add) * S, (oy + D) * S], radius=8 * S, fill=(232, 220, 194), outline=(150, 140, 120), width=3)
    sx = W + add / 2
    d.rounded_rectangle([ox + (sx - 11) * S, (oy + 50) * S, ox + (sx + 11) * S, (oy + 140) * S], radius=11 * S, fill=(120, 120, 124), outline=(90, 90, 96), width=3)
    d.rounded_rectangle([ox + (sx - 8.5) * S, (oy + 53) * S, ox + (sx + 8.5) * S, (oy + 137) * S], radius=8 * S, fill=(244, 240, 232))
    d.line([(ox + W * S, oy * S), (ox + W * S, (oy + D) * S)], fill=(200, 190, 170), width=2)
    # light bar on grass below
    d.rectangle([ox, (oy + D + 12) * S, ox + (W + add) * S, (oy + D + 50) * S], fill=(118, 150, 86))
    d.rounded_rectangle([ox + (sx - 26) * S, (oy + D + 22) * S, ox + (sx + 30) * S, (oy + D + 32) * S], radius=5 * S, fill=(214, 226, 140))
    d.text((ox + 6 * S, (oy + D + 20) * S), "noon: a bar of light on the grass, not a disc", font=F(int(3.6 * S)), fill=(240, 244, 230))
    d.text((ox + 6 * S, (oy + 6) * S), "ONE SHEET + 32 mm (not + 55): a 22 × 90 slot at the right end, lined in grey felt", font=F(int(3.6 * S), True), fill=INK)
    im.save(path)

if __name__ == "__main__":
    rain(os.path.join(HERE, "t2-rain-top.png"))
    chamber(os.path.join(HERE, "t2-chamber-closed-facade.png"))
    horn(os.path.join(HERE, "t2-ground-horn-section.png"))
    butterfly(os.path.join(HERE, "t2-butterfly-real-rail.png"))
    print("ok")
