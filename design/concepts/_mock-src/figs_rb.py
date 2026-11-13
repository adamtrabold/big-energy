#!/usr/bin/env python3
"""Branch figures for the project site (owner: images only where it must be visual; words live in the markdown).
Takes the renders from rb.py (out/rb_*.png), adds only what a drawing needs to be read (dimensions, a scale bar),
and writes web-ready files into design/branches/concepts/<concept>/img/.
PNG for exact drawings and true-scale views, high-quality JPEG for renders. Run after rb.py: python3 figs_rb.py"""
import math, os, shutil
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
DEST = os.path.join(HERE, "..", "..", "branches", "concepts")
FONT = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
FONTB = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
INK, ACC, PAPER = (46, 41, 36), (196, 72, 40), (243, 239, 232)

def F(px, b=False):
    return ImageFont.truetype(FONTB if b else FONT, int(px))

def dest(concept, name):
    d = os.path.join(DEST, concept, "img")
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, name)

def save_render(src, concept, name, maxw=2400):
    """renders: long edge capped for the web (still ≥ 2x a wide desktop column), JPEG q 90."""
    im = Image.open(os.path.join(OUT, src)).convert("RGB")
    if im.width > maxw:
        im = im.resize((maxw, int(im.height * maxw / im.width)), Image.LANCZOS)
    p = dest(concept, name)
    im.save(p, quality=90, optimize=True, progressive=True)
    return p

def scale_bar(d, x, y, px_per_mm, mm=10, h=None, col=INK):
    h = h or max(3, px_per_mm * 0.35)
    L = px_per_mm * mm
    d.rectangle([x, y, x + L / 2, y + h], fill=col)
    d.rectangle([x + L / 2, y, x + L, y + h], outline=col, width=max(1, int(h / 4)))
    d.text((x + L + px_per_mm * 1.2, y + h / 2), f"{mm} mm", font=F(px_per_mm * 2.2), fill=col, anchor="lm")

def crop_top(src, world_box, frame, px_per_mm_out=None):
    """crop an exact top view (rb top views are cropped to `frame` = (x0, y0, x1, y1) world mm)."""
    im = Image.open(os.path.join(OUT, src)).convert("RGB")
    fx0, fy0, fx1, fy1 = frame
    s = im.width / (fx1 - fx0)
    x0, y0, x1, y1 = world_box
    c = im.crop((int((x0 - fx0) * s), int((fy1 - y1) * s), int((x1 - fx0) * s), int((fy1 - y0) * s)))
    if px_per_mm_out:
        f = px_per_mm_out / s
        c = c.resize((int(c.width * f), int(c.height * f)), Image.LANCZOS)
        s = px_per_mm_out
    return c, s

def detail(src, frame, box, concept, name, ppm=None):
    """native-resolution crop of an exact top view (no upsampling), with a 10 mm bar; px/mm goes in the name."""
    c, s = crop_top(src, box, frame, ppm)
    name = name.replace("{ppm}", f"{s:.2f}px-per-mm")
    pad = int(s * 6)
    out = Image.new("RGB", (c.width, c.height + pad), PAPER)
    out.paste(c, (0, 0))
    scale_bar(ImageDraw.Draw(out), s * 2, c.height + s * 2, s, 10)
    p = dest(concept, name)
    out.save(p, optimize=True)
    return p

def true_scale(src, concept, stem, frame_w):
    """1:1-ready top view: its real px/mm (measured from the markers' crop) goes in the file name, so the site can
    size it in real mm: CSS width = image px / (px per mm) mm."""
    w = Image.open(os.path.join(OUT, src)).width
    ppm = w / frame_w
    p = dest(concept, f"{stem}-{ppm:.2f}px-per-mm.png")
    shutil.copy(os.path.join(OUT, src), p)
    return p

# ------------------------------------------------------------------ annotated drawings (dimensions only)
def dim_text(d, x, y, s, px, col=INK, anchor="mm", bold=True):
    d.text((x, y), s, font=F(px, bold), fill=col, anchor=anchor)

def diptych_side():
    """the standing right-end elevation, exact (ortho): cord at the latitude of home, 120 deg, feet 59 behind."""
    a0, a1, b0, b1 = -4, 200, -4, 108 + 64          # frame from rb.py job rb_dp_side
    im = Image.open(os.path.join(OUT, "rb_dp_side.png")).convert("RGB")
    s = im.width / (a1 - a0)
    P = lambda y, z: ((y - a0) * s, (b1 - z) * s)
    d = ImageDraw.Draw(im)
    lw = max(2, int(s * 0.25))
    # cord angle at the base anchor (53.2, 9) to the lid eye (as modelled: lid eye on the hinge axis line, s 60)
    ax, az = 53.2, 9.0
    ly, lz = 109 + 60 * math.cos(math.radians(60)), 25.0 + 60 * math.sin(math.radians(60))
    ang = math.degrees(math.atan2(lz - az, ly - ax))
    R = 18
    cx, cy = P(ax, az)
    d.line([P(ax, az), P(ax + R + 6, az)], fill=ACC, width=lw)
    d.arc([cx - R * s, cy - R * s, cx + R * s, cy + R * s], start=-ang, end=0, fill=ACC, width=lw)
    dim_text(d, *P(ax - 3, az + 24), f"cord {ang:.1f}° as drawn", s * 3.0, ACC, "rb")
    dim_text(d, *P(ax - 3, az + 19), "(target: 37.4°, the latitude of home)", s * 2.4, ACC, "rb", bold=False)
    # lid angle at the hinge: from the base plane (toward the player) round to the lid
    hx, hz = 109, 25.0
    hcx, hcy = P(hx, hz)
    R2 = 14
    d.arc([hcx - R2 * s, hcy - R2 * s, hcx + R2 * s, hcy + R2 * s], start=180, end=300, fill=INK, width=lw)
    tx, ty = P(hx + (R2 + 6) * math.cos(math.radians(120)), hz + (R2 + 6) * math.sin(math.radians(120)))
    dim_text(d, tx, ty, "120°", s * 3.2, INK)
    # feet: tips 59 behind the base
    y0, y1 = 108, 167
    yy = -2.2
    d.line([P(y0, yy), P(y1, yy)], fill=INK, width=lw)
    for y in (y0, y1):
        d.line([P(y, yy - 1.5), P(y, yy + 1.5)], fill=INK, width=lw)
    out = Image.new("RGB", (im.width, im.height + int(s * 8)), PAPER)
    out.paste(im, (0, 0))
    d2 = ImageDraw.Draw(out)
    dim_text(d2, *P((y0 + y1) / 2, -6.0), "feet: tips 59 behind the base", s * 3.0, INK)
    scale_bar(d2, s * 4, im.height + s * 2.5, s, 20)
    p = dest("diptych", "diptych-standing-side-exact.png")
    out.save(p, optimize=True)
    return p

def chamber_closed_front():
    """closed, exact front elevation: 52.7 high with pegs inside (v1.1 FOLD 50.1)."""
    a0, a1, b0, b1 = -2, 288, -1, 56
    im = Image.open(os.path.join(OUT, "rb_ch_front_closed.png")).convert("RGB")
    s = im.width / (a1 - a0)
    P = lambda x, z: ((x - a0) * s, (b1 - z) * s)
    pad = int(s * 26)
    out = Image.new("RGB", (im.width + pad, im.height), PAPER)
    out.paste(im, (0, 0))
    d = ImageDraw.Draw(out)
    lw = max(2, int(s * 0.25))
    X = 292
    for z in (0, 52.6):
        d.line([P(286.5, z), P(X + 3, z)], fill=INK, width=lw)
    d.line([P(X, 0), P(X, 52.6)], fill=INK, width=lw)
    dim_text(d, *P(X + 4, 29), "52.7", s * 3.6, INK, "lm")
    dim_text(d, *P(X + 4, 22), "v1.1: 50.1", s * 2.6, (120, 112, 100), "lm", bold=False)
    p = dest("chamber", "chamber-closed-front-exact.png")
    out.save(p, optimize=True)
    return p

def rain_ring_compare(ppm=40):
    """three ring pitches round a 14.86 knob, at 40 px per mm, left to right 0.45 / 0.6 / 0.9 (director fix 5).
    No words in the image: the captions live in the doc (director ruling). Only a 10 mm bar."""
    W, H = int(ppm * 94), int(ppm * 32)
    S = ppm * 2
    im = Image.new("RGB", (W * 2, H * 2), PAPER)
    d = ImageDraw.Draw(im)
    base, line, knob = (221, 211, 193), (185, 171, 147), (236, 230, 214)
    for k, (pitch, groove) in enumerate(((0.45, 0.30), (0.60, 0.30), (0.90, 0.45))):
        cx, cy = (16 + 31 * k) * S, 15 * S
        d.rectangle([(2 + 31 * k) * S, 2 * S, (30 + 31 * k) * S, 28 * S], fill=base)
        r = 7.75 + groove / 2
        while r < 12.6:
            d.ellipse([cx - (r + groove / 2) * S, cy - (r + groove / 2) * S, cx + (r + groove / 2) * S, cy + (r + groove / 2) * S],
                      outline=line, width=max(1, int(groove * S)))
            r += pitch
        d.ellipse([cx - 7.43 * S, cy - 7.43 * S, cx + 7.43 * S, cy + 7.43 * S], fill=knob, outline=(140, 130, 112), width=int(0.2 * S))
    im = im.resize((W, H), Image.LANCZOS)
    out = Image.new("RGB", (W, H + int(ppm * 4)), PAPER)
    out.paste(im, (0, 0))
    scale_bar(ImageDraw.Draw(out), ppm * 2, H + ppm * 0.8, ppm, 10)
    p = dest("rain", "rain-ring-pitch-045-06-09-40px-per-mm.png")
    out.save(p, optimize=True)
    return p

def butterfly_section(ppm=24):
    """section at x 200 through the rear band: the walnut top in its rebate over the printed apron; jacks below."""
    from PIL import ImageFilter
    y0, y1, z0, z1 = 122.0, 222.0, -4.0, 32.0
    S = ppm * 2
    W, H = int((y1 - y0) * S), int((z1 - z0) * S)
    im = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(im)
    P = lambda y, z: ((y - y0) * S, (z1 - z) * S)
    BONE, WAL, DARK = (226, 218, 203), (110, 70, 40), (40, 34, 30)
    _rect = d.rectangle
    class _D:   # rectangles given as two corners in any order
        pass
    def rect(xy, fill):
        x0_, y0_, x1_, y1_ = xy
        _rect([min(x0_, x1_), min(y0_, y1_), max(x0_, x1_), max(y0_, y1_)], fill=fill)
    d.rectangle = rect
    # printed shell: top 2.4 thick to the joint, rebate floor at z 18 to the rear wall, rear wall 2.4
    d.rectangle([*P(140, 24), *P(165, 21.6)], fill=BONE)
    d.rectangle([*P(162.6, 21.6), *P(165, 15.6)], fill=BONE)
    d.rectangle([*P(165, 18), *P(180, 15.6)], fill=BONE)
    d.rectangle([*P(177.6, 15.6), *P(180, 0.5)], fill=BONE)
    d.rectangle([*P(140, 3.5), *P(180, 0.5)], fill=(206, 196, 178))           # back panel
    # walnut leaf: 6 thick, flush at z 24, live edge out to 190 here
    d.polygon([P(165, 24), P(189, 24), P(190.2, 23.0), P(190.6, 20.5), P(189.6, 18), P(165, 18)], fill=WAL)
    d.rectangle([*P(165, 24), *P(165.3, 18)], fill=(60, 38, 22))
    # screw up through the rebate floor, slotted hole (front to back)
    d.rectangle([*P(171.2, 21.5), *P(172.8, 15.6)], fill=(120, 120, 124))
    d.rectangle([*P(170.0, 15.6), *P(174.0, 14.6)], fill=(120, 120, 124))
    d.rectangle([*P(170.4, 18), *P(173.6, 18.25)], fill=PAPER)
    # jack on the I/O board inside the rear wall, plug socket through the wall
    d.rectangle([*P(168, 13.5), *P(177.4, 6.5)], fill=(30, 30, 30))
    d.rectangle([*P(177.6, 11.3), *P(180, 8.7)], fill=(12, 12, 12))
    d.rectangle([*P(160, 5.0), *P(177.4, 3.6)], fill=(47, 107, 79))         # I/O board
    # a plug, under the overhang
    d.rectangle([*P(180, 10.75), *P(186, 9.25)], fill=(170, 170, 172))
    d.rectangle([*P(186, 12.5), *P(197, 7.5)], fill=(25, 25, 25))
    im = im.resize((W // 2, H // 2), Image.LANCZOS)
    s = ppm
    P = lambda y, z: ((y - y0) * s, (z1 - z) * s)
    d = ImageDraw.Draw(im)
    lw = 2
    def lab(y, z, t, ty, tz, anchor="lm"):
        d.line([P(y, z), P(ty, tz)], fill=INK, width=lw)
        d.text(P(ty + (0.6 if anchor == "lm" else -0.6), tz), t, font=F(s * 1.25), fill=INK, anchor=anchor)
    lab(180, 22, "walnut 6 mm", 196, 29.0)
    lab(165.1, 22, "joint y 165", 156, 29.0, "rm")
    lab(172, 16.8, "screw, slotted hole", 156, 11.0, "rm")
    lab(192, 10, "plug, under the live edge", 197, 3.0)
    lab(150, 22.8, "printed face", 140, 29.0, "rm")
    lab(178.8, 6, "rear wall + jacks (v1.1)", 156, 6.0, "rm")
    d.line([P(180, 26), P(190.6, 26)], fill=ACC, width=lw)
    d.text(P(185, 26.6), "0–12", font=F(s * 1.1, True), fill=ACC, anchor="mb")
    out = Image.new("RGB", (im.width, im.height + int(s * 4)), PAPER)
    out.paste(im, (0, 0))
    scale_bar(ImageDraw.Draw(out), s * 2, im.height + s * 1.2, s, 10)
    p = dest("butterfly", f"butterfly-rear-section-{ppm}px-per-mm.png")
    out.save(p, optimize=True)
    return p

if __name__ == "__main__":
    # ---------------- renders
    for src, con, name in [
        ("rb_ch_main.png", "chamber", "chamber-open.jpg"), ("rb_ch_closed.png", "chamber", "chamber-closed-with-book.jpg"),
        ("rb_ch_stand_back.png", "chamber", "chamber-standing-from-behind.jpg"), ("rb_ch_stand.png", "chamber", "chamber-standing.jpg"),
        ("rb_ch_keys.png", "chamber", "chamber-reverse-pegs.jpg"), ("rb_ch_keys_fallback.png", "chamber", "chamber-pegs-fallback-colours.jpg"),
        ("rb_rn_far.png", "rain", "rain-arms-length.jpg"), ("rb_rn_near.png", "rain", "rain-close.jpg"),
        ("rb_bf_main.png", "butterfly", "butterfly.jpg"), ("rb_bf_rear.png", "butterfly", "butterfly-from-behind.jpg"),
        ("rb_bf_joint.png", "butterfly", "butterfly-joint.jpg"), ("rb_bf_wall.png", "butterfly", "butterfly-on-the-wall.jpg"),
        ("rb_dp_stand.png", "diptych", "diptych-standing.jpg"), ("rb_dp_main.png", "diptych", "diptych-open.jpg"),
        ("rb_dp_closed.png", "diptych", "diptych-closed.jpg"),
    ]:
        print(save_render(src, con, name))
    # ---------------- true-scale top views (px per mm in the name)
    print(true_scale("rb_ch_top.png", "chamber", "chamber-top", 290))
    print(true_scale("rb_rn_top.png", "rain", "rain-top", 280))
    print(true_scale("rb_bf_top.png", "butterfly", "butterfly-top", 280))
    print(true_scale("rb_dp_top.png", "diptych", "diptych-top", 290))
    # ---------------- details at 40 px/mm with a scale bar
    OPEN = 218.0
    print(detail("rb_dp_top.png", (-2, -2, 288, OPEN + 2), (98, 168, 172, 212), "diptych", "diptych-time-dial-{ppm}.png"))
    print(detail("rb_ch_top.png", (-2, -2, 288, OPEN + 2), (98, 168, 172, 212), "chamber", "chamber-time-dial-{ppm}.png"))
    print(detail("rb_ch_top.png", (-2, -2, 288, OPEN + 2), (6, 112, 80, 142), "chamber", "chamber-range-feet-{ppm}.png"))
    print(detail("rb_ch_top.png", (-2, -2, 288, OPEN + 2), (2, 2, 90, 52), "chamber", "chamber-pegs-{ppm}.png"))
    print(detail("rb_rn_top.png", (-2, -2, 278, 182), (92, 116, 170, 168), "rain", "rain-time-and-pads-{ppm}.png"))
    print(detail("rb_rn_top.png", (-2, -2, 278, 182), (0, 0, 80, 60), "rain", "rain-pegs-{ppm}.png"))
    print(detail("rb_bf_top.png", (-2, -2, 278, 194), (100, 126, 176, 194), "butterfly", "butterfly-joint-top-{ppm}.png"))
    print(detail("rb_bf_top.png", (-2, -2, 278, 194), (92, 120, 170, 165), "butterfly", "butterfly-time-dial-{ppm}.png"))
    print(detail("rb_dp_top.png", (-2, -2, 288, OPEN + 2), (0, 110, 143, 218), "diptych", "diptych-lid-left-graduations-{ppm}.png"))
    # ---------------- annotated exact drawings
    print(diptych_side()); print(chamber_closed_front()); print(rain_ring_compare()); print(butterfly_section())
