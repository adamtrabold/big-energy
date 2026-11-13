"""Shared view builders: base with keys, body rims, wordmark, title block."""
from kit import *

NAME = "untitled no.1"  # placeholder wordmark (owner names it)


def keys_base(p, w=315, d=150, night=False, reverse=False, front_lip=10, rim_mat=None, top_plate=True):
    """Top view of a keyboard base/module, local mm. Player at the bottom (y = d)."""
    o = []
    o.append(f'<g filter="url(#shbig)"><rect x="0" y="0" width="{w}" height="{d}" rx="5" '
             f'{body_fill(p, rim_mat) if not night else "fill=\"#0a0a0a\""}/></g>')
    ky = d - front_lip - 90
    # key well
    o.append(f'<rect x="38" y="{ky-2}" width="{w-41}" height="{92}" rx="1.5" fill="#0b0b0b"/>')
    o.append(keyboard(41.5, ky, p, reverse=reverse, night=night))
    # wheel well
    o.append(f'<rect x="4" y="{ky+12}" width="31" height="66" rx="2" fill="#0b0b0b"/>')
    o.append(wheels(4, ky + 15, p, night=night, h=60))
    if top_plate and not night:
        # top plate behind keys: panel-PCB strip with the wordmark
        # small inlaid wordmark plate (panel PCB offcut) on the body top behind the keys
        o.append(f'<rect x="{w-92}" y="{ky-24}" width="80" height="15" rx="1.5" fill="{p["panel"]}"/>')
        o.append(txt(w - 52, ky - 13.2, NAME, 7, p["silk"], weight=700))
    return "".join(o), ky


def title_block(x, y, title, kind, lines, look, size=30):
    o = [txt(x, y, title, 92, "#1d1c1a", anchor="start", font=UI_FONT, weight=800, ls=2),
         txt(x, y + 52, kind, 30, "#6b675f", anchor="start", font=UI_FONT, weight=500)]
    o.append(para(x, y + 112, lines, size, "#2a2926"))
    o.append(txt(x, y + 112 + len(lines) * size * 1.38 + 16, look, 26, "#8a8478", anchor="start",
                 font=UI_FONT, weight=600))
    return "".join(o)


def placeholder_note(x, y, size=22):
    return txt(x, y, "Hand-lettered legends, wordmark and grille are PLACEHOLDERS — the owner draws or paints the real ones.",
               size, "#9a5b2a", anchor="start", font=UI_FONT, weight=600)


def view_label(x, y, s, size=30):
    return txt(x, y, s, size, "#1d1c1a", anchor="start", font=UI_FONT, weight=700, ls=1)


def G(px, py, s, inner, rot=None):
    r = f" rotate({rot})" if rot else ""
    return f'<g transform="translate({px},{py}) scale({s}){r}">{inner}</g>'
