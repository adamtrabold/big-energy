"""Round-2 sheet helpers: title, check/cost boxes, palettes, exploded-view renderer."""
from kit import *
from r2 import *
from common_views import G, view_label

ROOT = "/home/claude/model-d/design/instrument/concepts/"
W = 3900
NAME = "untitled no.1"

# MOTTO palette from the round-2 draws: cork body + white panel (body draw),
# "Use an unacceptable colour" -> acid chartreuse hero; walnut only on the lid's outside.
PAL["motto"] = dict(
    name="Motto", panel="#f2eee4", silk="#1d1a17", gold="#a8823a",
    cap="#24221f", cap_hi="#45413c", cap_lo="#111", ptr="#f4ffd0",
    hero="#c6e01c", hero_hi="#e2f56a", hero_lo="#8ea310", signal="#c6e01c",
    nat="#efe7d6", nat_edge="#c9bda5", sharp="#4b2f1d", sharp_hi="#6a442c",
    body_top="#b48a5e", body_mat="cork", base_mat="cork", tog="#d0cbc1",
    bg="#f1ede5", ink="#22211f", sub="#6b675f", led="#d42a1f", brass="#b8933f",
    grille="rose", hole="#2a2420")

INK = "#22211f"
SUB = "#6b675f"
WARN = "#9a4a14"


def head(x, y, title, kind, lines, look):
    o = [txt(x, y, title, 96, "#1d1c1a", anchor="start", font=UI_FONT, weight=800, ls=2),
         txt(x, y + 56, kind, 32, SUB, anchor="start", font=UI_FONT, weight=500)]
    o.append(para(x, y + 118, lines, 30, "#2a2926"))
    o.append(txt(x, y + 118 + len(lines) * 30 * 1.38 + 18, look, 27, "#8a8478", anchor="start", font=UI_FONT, weight=600))
    return "".join(o)


def placeholder(x, y):
    return txt(x, y, "Hand-lettered legends, wordmark, grille pattern and paintings are PLACEHOLDERS: the owner letters or paints the real ones.",
               24, WARN, anchor="start", font=UI_FONT, weight=600)


def box(x, y, w, title, lines, size=24, fill="#fbf9f4", stroke="#d8d2c6", tcol=INK):
    h = 70 + len(lines) * size * 1.4
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h:.0f}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="2"/>',
         txt(x + 28, y + 46, title, 27, tcol, anchor="start", font=UI_FONT, weight=700)]
    o.append(para(x + 28, y + 46 + size * 1.55, lines, size, "#33312d"))
    return "".join(o), h


def note(x, y, lines, size=24, color="#33312d"):
    return para(x, y, lines, size, color)


def save(path, w, h, body, p, bg=None):
    open(path, "w").write(svg_doc(w, h, body, p, bg))
    return path


def lbl(x, y, s, size=26, color=INK, anchor="start", weight=500):
    return txt(x, y, s, size, color, anchor=anchor, font=UI_FONT, weight=weight)


# ------------------------------------------------------------------ exploded side view
def exploded(parts, s=7.0, x0=120, y0=200, label_x=None, gap=46, title=None, front_note="← player (front)"):
    """parts: list of dicts top->bottom: name, a, b (mm along depth, 0 = front), t (mm), fill,
    lines (label), step (int or str), draw (optional fn(x0px,ypx,s)->svg drawn instead of a box), dx (mm shift).
    Returns svg, bottom y."""
    o = []
    y = y0
    lx = label_x or (x0 + 200 * s + 80)
    for pt in parts:
        a, b, t = pt["a"], pt["b"], pt["t"]
        h = max(t * s, 4)
        if pt.get("draw"):
            o.append(pt["draw"](x0, y, s))
        else:
            o.append(f'<rect x="{x0 + a*s:.1f}" y="{y:.1f}" width="{(b-a)*s:.1f}" height="{h:.1f}" rx="4" fill="{pt["fill"]}" stroke="#2a2a2a" stroke-width="1.2" {pt.get("extra","")}/>')
        mid_y = y + h / 2
        ax = x0 + b * s
        o.append(f'<line x1="{ax+8:.1f}" y1="{mid_y:.1f}" x2="{lx-14}" y2="{mid_y:.1f}" stroke="#9a948a" stroke-width="1.4" stroke-dasharray="5 5"/>')
        st = pt.get("step")
        if st is not None:
            o.append(f'<circle cx="{lx+16}" cy="{mid_y:.1f}" r="19" fill="{INK}"/>')
            o.append(txt(lx + 16, mid_y + 8, str(st), 22 if len(str(st)) < 3 else 15, "#fff", font=UI_FONT, weight=700))
        for i, ln in enumerate(pt["lines"]):
            o.append(txt(lx + 48, mid_y + 9 + i * 30, ln, 25 if i else 26, INK if i == 0 else "#4a4741",
                         anchor="start", font=UI_FONT, weight=700 if i == 0 else 400))
        y += h + gap + max(0, (len(pt["lines"]) - 2) * 30)
    o.append(txt(x0, y + 10, front_note, 24, "#777", anchor="start", font=UI_FONT))
    return "".join(o), y


def mm_ruler(x0, y, s, length, step=20):
    o = [f'<line x1="{x0}" y1="{y}" x2="{x0+length*s}" y2="{y}" stroke="#777" stroke-width="1.5"/>']
    for m in range(0, length + 1, step):
        o.append(f'<line x1="{x0+m*s}" y1="{y-8}" x2="{x0+m*s}" y2="{y+8}" stroke="#777" stroke-width="1.5"/>')
        o.append(txt(x0 + m * s, y + 32, str(m), 20, "#777", font=UI_FONT))
    o.append(txt(x0 + length * s + 20, y + 8, "mm", 20, "#777", anchor="start", font=UI_FONT))
    return "".join(o)


def caps_row(x0, y, s, xs, col="#2a2826", hero_x=None, hero_col="#ff5a1f", h=11):
    """Knob silhouettes (side) standing on y (px), xs = mm positions along depth."""
    o = []
    for x in xs:
        o.append(f'<rect x="{x0+(x-6)*s:.1f}" y="{y-h*s:.1f}" width="{12*s:.1f}" height="{h*s:.1f}" rx="6" fill="{col}"/>')
    if hero_x is not None:
        o.append(f'<rect x="{x0+(hero_x-13)*s:.1f}" y="{y-12*s:.1f}" width="{26*s:.1f}" height="{12*s:.1f}" rx="8" fill="{hero_col}"/>')
    return "".join(o)


def frame_draw(segs, t, fill="#7d7a74", outline=(0, 185)):
    """Body frame in side view: solid only where the laser layers are (segs = [(a,b),...]), dashed outline elsewhere."""
    def f(x0, y, s_):
        o = f'<rect x="{x0+outline[0]*s_:.1f}" y="{y:.1f}" width="{(outline[1]-outline[0])*s_:.1f}" height="{t*s_:.1f}" rx="4" fill="none" stroke="#888" stroke-width="1.5" stroke-dasharray="8 6"/>'
        for a, b in segs:
            o += f'<rect x="{x0+a*s_:.1f}" y="{y:.1f}" width="{(b-a)*s_:.1f}" height="{t*s_:.1f}" rx="3" fill="{fill}" stroke="#2a2a2a" stroke-width="1.2"/>'
            for k in range(1, int(t / 3)):
                o += f'<line x1="{x0+a*s_:.1f}" y1="{y+k*3*s_:.1f}" x2="{x0+b*s_:.1f}" y2="{y+k*3*s_:.1f}" stroke="#000" stroke-opacity="0.18" stroke-width="1"/>'
        return o
    return f


def price_box(x, y, w, price, lines, size=24):
    """F1: full one-unit price in large type above the cost lines."""
    h = 150 + len(lines) * size * 1.4
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h:.0f}" rx="12" fill="#fbf9f4" stroke="#d8d2c6" stroke-width="2"/>',
         txt(x + 28, y + 46, "Full instrument, one unit (F1)", 27, INK, anchor="start", font=UI_FONT, weight=700),
         txt(x + 28, y + 112, price, 58, "#1d1c1a", anchor="start", font=UI_FONT, weight=800)]
    o.append(para(x + 28, y + 112 + size * 1.9, lines, size, "#33312d"))
    return "".join(o), h
