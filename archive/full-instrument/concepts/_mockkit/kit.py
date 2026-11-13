"""Mock kit: SVG primitives at real millimetres for the instrument concept mocks.

Everything is drawn in mm. A view is wrapped in <g transform="translate(px,py) scale(s)">.
Panel legends use Kalam (hand-made placeholder); sheet annotations use Inter.
"""
import math, random

# ---------------------------------------------------------------- palettes
PAL = {
    "field": dict(
        name="Field", panel="#1d1d1c", silk="#ece8df", gold="#c9a24e",
        cap="#3b3a37", cap_hi="#5a5853", cap_lo="#232220", ptr="#e9f3cf",
        hero="#ff5a1f", hero_hi="#ff8a55", hero_lo="#c23d0c", signal="#ff5a1f",
        nat="#e3dfd5", nat_edge="#b9b3a6", sharp="#66625b", sharp_hi="#7d7870",
        body_top="#8b8780", body_mat="felt", base_mat="cork", tog="#c9c6bf",
        bg="#efece6", ink="#22211f", sub="#6b675f", led="#ff5a1f", brass="#b8933f",
        grille="topo", hole="#8a857c"),
    "proof": dict(
        name="Proof", panel="#f1ede3", silk="#1b1917", gold="#c29a45",
        cap="#1f1d1b", cap_hi="#3c3935", cap_lo="#0f0e0d", ptr="#eaf2cf",
        hero="#d42a1f", hero_hi="#ec5a4c", hero_lo="#9a1810", signal="#d42a1f",
        nat="#efe9dc", nat_edge="#c6bda9", sharp="#2a2420", sharp_hi="#433a33",
        body_top="#5b3a26", body_mat="walnut", base_mat="walnut", tog="#cfcac0",
        bg="#f3efe7", ink="#22211f", sub="#6e675c", led="#d42a1f", brass="#b8933f",
        grille="letter", hole="#2a2522"),
    "desk": dict(
        name="Desk", panel="#121212", silk="#e7e3da", gold="#d2ab55",
        cap="#1b1b1b", cap_hi="#383838", cap_lo="#080808", ptr="#e9f3cf",
        hero="#2fdc86", hero_hi="#6ff0b0", hero_lo="#169c58", signal="#2fdc86",
        nat="#d8d5cd", nat_edge="#a9a59b", sharp="#1e1e1e", sharp_hi="#353535",
        body_top="#1f2523", body_mat="acrylic", base_mat="acrylic", tog="#bdbdbd",
        bg="#eceae5", ink="#1f1f1f", sub="#666", led="#2fdc86", brass="#b8933f",
        grille="holes", hole="#3d4442"),
}

LEG_FONT = "Kalam, 'Comic Neue', cursive"
UI_FONT = "Inter, 'DejaVu Sans', sans-serif"


def defs(p):
    """Shared <defs>: gradients, filters, textures. One per sheet (ids are global)."""
    return f"""
<defs>
  <filter id="sh" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="0.7"/><feOffset dx="0.6" dy="1.0"/>
    <feComponentTransfer><feFuncA type="linear" slope="0.55"/></feComponentTransfer>
    <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="shbig" x="-10%" y="-10%" width="130%" height="140%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="3"/><feOffset dx="1.5" dy="4"/>
    <feComponentTransfer><feFuncA type="linear" slope="0.35"/></feComponentTransfer>
    <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="glow" x="-200%" y="-200%" width="500%" height="500%">
    <feGaussianBlur stdDeviation="1.4" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="feltf" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="1.6" numOctaves="3" seed="4" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.22 0" result="na"/>
    <feComposite in="na" in2="SourceGraphic" operator="in" result="nm"/>
    <feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="nm"/></feMerge></filter>
  <filter id="corkf" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="9" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0.25  0 0 0 0 0.15  0 0 0 0 0.05  0 0 0 0.5 0" result="na"/>
    <feComposite in="na" in2="SourceGraphic" operator="in" result="nm"/>
    <feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="nm"/></feMerge></filter>
  <filter id="grainf" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.04 0.9" numOctaves="3" seed="2" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0.1  0 0 0 0 0.05  0 0 0 0 0  0 0 0 0.55 0" result="na"/>
    <feComposite in="na" in2="SourceGraphic" operator="in" result="nm"/>
    <feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="nm"/></feMerge></filter>
  <filter id="grainv" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.9 0.04" numOctaves="3" seed="7" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0.1  0 0 0 0 0.05  0 0 0 0 0  0 0 0 0.55 0" result="na"/>
    <feComposite in="na" in2="SourceGraphic" operator="in" result="nm"/>
    <feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="nm"/></feMerge></filter>
  <radialGradient id="capg" cx="35%" cy="30%" r="75%">
    <stop offset="0" stop-color="{p['cap_hi']}"/><stop offset="0.6" stop-color="{p['cap']}"/>
    <stop offset="1" stop-color="{p['cap_lo']}"/></radialGradient>
  <radialGradient id="herog" cx="35%" cy="30%" r="75%">
    <stop offset="0" stop-color="{p['hero_hi']}"/><stop offset="0.6" stop-color="{p['hero']}"/>
    <stop offset="1" stop-color="{p['hero_lo']}"/></radialGradient>
  <linearGradient id="metal" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#f4f3ef"/><stop offset="0.45" stop-color="{p['tog']}"/>
    <stop offset="1" stop-color="#77746d"/></linearGradient>
  <linearGradient id="brassg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#e8cf8a"/><stop offset="0.5" stop-color="#b8933f"/>
    <stop offset="1" stop-color="#7a5e22"/></linearGradient>
  <linearGradient id="natg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{p['nat']}"/><stop offset="0.92" stop-color="{p['nat']}"/>
    <stop offset="1" stop-color="{p['nat_edge']}"/></linearGradient>
  <linearGradient id="sharpg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{p['sharp']}"/><stop offset="0.85" stop-color="{p['sharp_hi']}"/>
    <stop offset="1" stop-color="{p['sharp']}"/></linearGradient>
  <linearGradient id="acryl" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#3a4442"/><stop offset="0.3" stop-color="#1c2221"/>
    <stop offset="1" stop-color="#0d1110"/></linearGradient>
</defs>"""


# ---------------------------------------------------------------- per-palette gradients (several palettes on one sheet)
def pgrad(p):
    k = (p["hero"] + p["nat"] + p["sharp"]).replace("#", "")
    d = (f'<defs><radialGradient id="herog{k}" cx="35%" cy="30%" r="75%"><stop offset="0" stop-color="{p["hero_hi"]}"/>'
         f'<stop offset="0.6" stop-color="{p["hero"]}"/><stop offset="1" stop-color="{p["hero_lo"]}"/></radialGradient>'
         f'<linearGradient id="natg{k}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{p["nat"]}"/>'
         f'<stop offset="0.92" stop-color="{p["nat"]}"/><stop offset="1" stop-color="{p["nat_edge"]}"/></linearGradient>'
         f'<linearGradient id="sharpg{k}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{p["sharp"]}"/>'
         f'<stop offset="0.85" stop-color="{p["sharp_hi"]}"/><stop offset="1" stop-color="{p["sharp"]}"/></linearGradient></defs>')
    return k, d


# ---------------------------------------------------------------- helpers
def pol(cx, cy, r, deg):
    """deg measured clockwise from 12 o'clock (knob convention)."""
    a = math.radians(deg)
    return cx + r * math.sin(a), cy - r * math.cos(a)


def txt(x, y, s, size=2.8, fill="#000", anchor="middle", font=LEG_FONT, weight=400,
        rot=None, ls=0, style=""):
    tr = f' transform="rotate({rot} {x:.2f} {y:.2f})"' if rot is not None else ""
    s = str(s).replace("&", "&amp;").replace("&amp;amp;", "&amp;").replace("<", "&lt;")
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-family="{font}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
            f'letter-spacing="{ls}"{tr} style="{style}">{s}</text>')


def scale_ticks(cx, cy, r0, r1, n, p, a0=-135, a1=135, w=0.35, color=None):
    c = color or p["silk"]
    out = []
    for i in range(n):
        a = a0 + (a1 - a0) * i / (n - 1)
        x0, y0 = pol(cx, cy, r0, a)
        x1, y1 = pol(cx, cy, r1, a)
        out.append(f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" '
                   f'stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>')
    return "".join(out)


# ---------------------------------------------------------------- controls
def knob(cx, cy, p, d=16, val=0.4, label=None, lab_dy=None, ticks=True, night=False,
         label_size=2.7, lab_dx=0):
    r = d / 2
    ang = -135 + 270 * val
    out = []
    if ticks and not night:
        out.append(scale_ticks(cx, cy, r + 1.3, r + 2.6, 11, p))
    if night:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#0c0c0c" stroke="#1a1a1a" stroke-width="0.3"/>')
    else:
        out.append(f'<g filter="url(#sh)"><circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#capg)"/></g>')
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r-0.5}" fill="none" stroke="{p["cap_lo"]}" '
                   f'stroke-width="0.9" stroke-dasharray="0.35 0.45" opacity="0.9"/>')
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r*0.74}" fill="{p["cap"]}" opacity="0.55"/>')
    x0, y0 = pol(cx, cy, r * 0.18, ang)
    x1, y1 = pol(cx, cy, r * 0.92, ang)
    g = ' filter="url(#glow)"' if night else ""
    pc = "#b9ff9e" if night else p["ptr"]
    out.append(f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" stroke="{pc}" '
               f'stroke-width="{1.1 if d < 30 else 1.6}" stroke-linecap="round"{g}/>')
    if label and not night:
        dy = lab_dy if lab_dy is not None else r + 6.2
        out.append(txt(cx + lab_dx, cy + dy, label, label_size, p["silk"]))
    return "".join(out)


def hero(cx, cy, p, d=40, val=0.55, label="cutoff", night=False, lab_dy=None):
    r = d / 2
    ang = -135 + 270 * val
    out = []
    if not night:
        out.append(scale_ticks(cx, cy, r + 1.4, r + 3.4, 21, p, w=0.4))
        out.append(scale_ticks(cx, cy, r + 1.4, r + 4.6, 3, p, w=0.6))
        gk, gd = pgrad(p)
        out.append(gd + f'<g filter="url(#sh)"><circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#herog{gk})"/></g>')
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r-0.7}" fill="none" stroke="{p["hero_lo"]}" '
                   f'stroke-width="1.3" stroke-dasharray="0.45 0.55"/>')
        for k in (0.78, 0.6, 0.42):
            out.append(f'<circle cx="{cx}" cy="{cy}" r="{r*k}" fill="none" stroke="{p["hero_lo"]}" '
                       f'stroke-width="0.25" opacity="0.6"/>')
    else:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#0e0e0e"/>')
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r-0.4}" fill="none" stroke="#b9ff9e" '
                   f'stroke-width="0.6" opacity="0.55" filter="url(#glow)"/>')
    x0, y0 = pol(cx, cy, r * 0.25, ang)
    x1, y1 = pol(cx, cy, r * 0.93, ang)
    pc = "#b9ff9e" if night else p["ptr"]
    g = ' filter="url(#glow)"' if night else ""
    out.append(f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" stroke="{pc}" '
               f'stroke-width="2.0" stroke-linecap="round"{g}/>')
    if label and not night:
        dy = lab_dy if lab_dy is not None else r + 8
        out.append(txt(cx, cy + dy, label, 4.2, p["silk"], weight=700))
    return "".join(out)


WAVES = {  # tiny glyphs, unit box 0..1 x, -0.5..0.5 y
    "tri": [(0, .5), (.25, -.5), (.75, .5), (1, -.5)],
    "shark": [(0, .5), (.15, -.5), (.5, .5), (.65, -.5), (1, .5)],
    "saw": [(0, .5), (.5, -.5), (.5, .5), (1, -.5), (1, .5)],
    "sq": [(0, .5), (0, -.5), (.5, -.5), (.5, .5), (1, .5), (1, -.5)],
    "wide": [(0, .5), (0, -.5), (.32, -.5), (.32, .5), (1, .5), (1, -.5)],
    "narrow": [(0, .5), (0, -.5), (.14, -.5), (.14, .5), (1, .5), (1, -.5)],
}


def wave_glyph(x, y, kind, w, h, color, sw=0.3):
    pts = " ".join(f"{x - w/2 + px*w:.2f},{y + py*h:.2f}" for px, py in WAVES[kind])
    return f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round"/>'


def rotary(cx, cy, p, kind="range", pos=3, label=None, d=16, night=False, lab_dy=None):
    """6-position stepped control (MCU-read pot with detents)."""
    r = d / 2
    angs = [-125, -75, -25, 25, 75, 125]
    out = []
    if not night:
        for i, a in enumerate(angs):
            x0, y0 = pol(cx, cy, r + 1.2, a)
            x1, y1 = pol(cx, cy, r + 2.6, a)
            out.append(f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" '
                       f'stroke="{p["silk"]}" stroke-width="0.45" stroke-linecap="round"/>')
            lx, ly = pol(cx, cy, r + 3.9, a)
            if kind == "range":
                lab = ["LO", "32", "16", "8", "4", "2"][i]
                out.append(txt(lx, ly + 0.7, lab, 1.95, p["silk"]))
            else:
                k = ["tri", "shark", "saw", "sq", "wide", "narrow"][i]
                out.append(wave_glyph(lx, ly, k, 2.3, 1.4, p["silk"]))
    val = (angs[pos] + 135) / 270
    out.append(knob(cx, cy, p, d, val=val, label=None, ticks=False, night=night))
    if label and not night:
        dy = lab_dy if lab_dy is not None else r + 8.2
        out.append(txt(cx, cy + dy, label, 2.7, p["silk"]))
    return "".join(out)


def fader(cx, y0, p, travel=30, val=0.5, label=None, night=False):
    """Vertical fader; y0 = top of travel. Value 1 = top."""
    out = []
    L = travel + 6
    if not night:
        for i in range(11):
            yy = y0 + 3 + travel * i / 10
            w = 2.4 if i % 5 == 0 else 1.4
            out.append(f'<line x1="{cx-3.2-w:.2f}" y1="{yy:.2f}" x2="{cx-3.2:.2f}" y2="{yy:.2f}" '
                       f'stroke="{p["silk"]}" stroke-width="0.3"/>')
    out.append(f'<rect x="{cx-0.9}" y="{y0}" width="1.8" height="{L}" rx="0.9" fill="#050505"/>')
    cy = y0 + 3 + travel * (1 - val)
    if night:
        out.append(f'<rect x="{cx-3.5}" y="{cy-5}" width="7" height="10" rx="1" fill="#0d0d0d"/>')
        out.append(f'<line x1="{cx-3}" y1="{cy}" x2="{cx+3}" y2="{cy}" stroke="#b9ff9e" '
                   f'stroke-width="1" filter="url(#glow)"/>')
    else:
        out.append(f'<g filter="url(#sh)"><rect x="{cx-3.5}" y="{cy-5}" width="7" height="10" rx="1" '
                   f'fill="url(#capg)"/></g>')
        for k in (-2.6, -1.3, 1.3, 2.6):
            out.append(f'<line x1="{cx-2.8}" y1="{cy+k}" x2="{cx+2.8}" y2="{cy+k}" '
                       f'stroke="{p["cap_lo"]}" stroke-width="0.35"/>')
        out.append(f'<line x1="{cx-3.3}" y1="{cy}" x2="{cx+3.3}" y2="{cy}" stroke="{p["ptr"]}" stroke-width="0.9"/>')
    if label and not night:
        out.append(txt(cx, y0 + L + 4.2, label, 2.7, p["silk"]))
    return "".join(out), cy


def fader_cap_y(y0, travel, val):
    return y0 + 3 + travel * (1 - val)


def toggle(cx, cy, p, up=True, label=None, night=False, lab_dy=8.8, label_size=2.3):
    out = []
    if night:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="2.6" fill="#101010"/>')
        return "".join(out)
    hexpts = " ".join(f"{cx+3.1*math.cos(math.radians(30+60*i)):.2f},{cy+3.1*math.sin(math.radians(30+60*i)):.2f}"
                      for i in range(6))
    out.append(f'<polygon points="{hexpts}" fill="url(#metal)" stroke="#555" stroke-width="0.15"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="2.1" fill="#8d8a84"/>')
    dy = -1 if up else 1
    out.append(f'<g filter="url(#sh)"><line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy+dy*4.2}" '
               f'stroke="#d9d6cf" stroke-width="1.7" stroke-linecap="round"/>'
               f'<line x1="{cx-0.35}" y1="{cy}" x2="{cx-0.35}" y2="{cy+dy*4.2}" stroke="#fff" stroke-width="0.4" opacity="0.8"/>'
               f'<circle cx="{cx}" cy="{cy+dy*4.4}" r="1.3" fill="#f2f0ea" stroke="#77746d" stroke-width="0.2"/></g>')
    if label:
        out.append(txt(cx, cy + lab_dy, label, label_size, p["silk"]))
    return "".join(out)


def button(cx, cy, p, d=9, label=None, lit=None, night=False, lab_dy=None):
    out = []
    r = d / 2
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r+1}" fill="none" stroke="{p["gold"]}" stroke-width="0.5"/>')
    if night:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#0f0f0f"/>')
    else:
        out.append(f'<g filter="url(#sh)"><circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#capg)"/></g>')
    if lit:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r*0.35}" fill="{lit}" filter="url(#glow)"/>')
    if label and not night:
        out.append(txt(cx, cy + (lab_dy or r + 5.4), label, 2.6, p["silk"]))
    return "".join(out)


def led(cx, cy, color, r=1.4, on=True):
    if not on:
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#3a3a3a" stroke="#000" stroke-width="0.2"/>'
    return (f'<circle cx="{cx}" cy="{cy}" r="{r*2.4}" fill="{color}" opacity="0.18"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" filter="url(#glow)"/>')


def rule(x1, y1, x2, y2, p, w=0.45):
    return (f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{p["gold"]}" '
            f'stroke-width="{w}" stroke-linecap="round"/>')


# ---------------------------------------------------------------- grilles
def grille(cx, cy, r, p, kind=None, seed=3):
    kind = kind or p["grille"]
    rnd = random.Random(seed)
    hole = p["hole"]
    out = [f'<circle cx="{cx}" cy="{cy}" r="{r+1.2}" fill="none" stroke="{p["gold"]}" stroke-width="0.5"/>']
    if kind == "topo":  # survey contour map, laser-cut slots
        for k in range(9):
            rr = r * (0.14 + 0.098 * k)
            pts = []
            ph = [rnd.uniform(0, 6.28) for _ in range(3)]
            amp = [rnd.uniform(0.015, 0.045) for _ in range(3)]
            for i in range(73):
                t = 2 * math.pi * i / 72
                m = 1 + sum(a * math.sin((j + 2) * t + ph[j]) for j, a in enumerate(amp))
                pts.append(f"{cx + rr*m*math.cos(t) + r*0.06:.2f},{cy + rr*m*math.sin(t) - r*0.05:.2f}")
            out.append(f'<polygon points="{" ".join(pts)}" fill="none" stroke="{hole}" stroke-width="0.95" stroke-linejoin="round"/>')
    elif kind == "holes":
        pitch = 2.9
        rows = int(2 * r / (pitch * 0.866)) + 2
        for i in range(-rows, rows + 1):
            for j in range(-rows, rows + 1):
                x = cx + j * pitch + (i % 2) * pitch / 2
                y = cy + i * pitch * 0.866
                if (x - cx) ** 2 + (y - cy) ** 2 < (r - 1) ** 2:
                    out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="0.85" fill="{hole}"/>')
    elif kind == "rose":  # harpsichord rose, pierced
        for k, rr in enumerate([r * 0.95, r * 0.88]):
            out.append(f'<circle cx="{cx}" cy="{cy}" r="{rr}" fill="none" stroke="{hole}" stroke-width="{0.9 if k==0 else 0.5}"/>')
        for i in range(16):
            a = 360 * i / 16
            x, y = pol(cx, cy, r * 0.58, a)
            out.append(f'<ellipse cx="{x:.2f}" cy="{y:.2f}" rx="{r*0.09:.2f}" ry="{r*0.26:.2f}" '
                       f'transform="rotate({a} {x:.2f} {y:.2f})" fill="{hole}"/>')
        for i in range(8):
            a = 360 * i / 8 + 11.25
            x, y = pol(cx, cy, r * 0.26, a)
            out.append(f'<ellipse cx="{x:.2f}" cy="{y:.2f}" rx="{r*0.06:.2f}" ry="{r*0.14:.2f}" '
                       f'transform="rotate({a} {x:.2f} {y:.2f})" fill="{hole}"/>')
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r*0.07}" fill="{hole}"/>')
    elif kind == "bull":
        for k in range(1, 8):
            rr = r * k / 8
            out.append(f'<circle cx="{cx}" cy="{cy}" r="{rr:.2f}" fill="none" stroke="{hole}" '
                       f'stroke-width="0.9" stroke-dasharray="{rr*0.7:.2f} 0.9"/>')
    elif kind == "letter":  # letterpress: rows of slot "rules", like a type case grid
        for i, yy in enumerate(range(int(cy - r) + 2, int(cy + r) - 1, 3)):
            half = math.sqrt(max(r * r - (yy - cy) ** 2, 0)) - 1.2
            x = cx - half
            while x < cx + half - 1:
                ln = min(rnd.choice([2, 3, 4, 5, 7]), cx + half - x)
                out.append(f'<line x1="{x:.2f}" y1="{yy}" x2="{x+ln-0.9:.2f}" y2="{yy}" stroke="{hole}" '
                           f'stroke-width="1.1" stroke-linecap="round"/>')
                x += ln
    return "".join(out)


# ---------------------------------------------------------------- keys + wheels
WHITE = [0, 2, 4, 5, 7, 9, 11]


def keyboard(x0, y0, p, pitch=18.0, wlen=90, blen=55, reverse=False, night=False,
             pressed=None, glow_front=True):
    """25 keys C..C. (x0,y0) = top-left of the key run (back edge of visible keys)."""
    out = []
    gk, gd = pgrad(p)
    out.append(gd)
    nat_fill = f"url(#natg{gk})" if not reverse else f"url(#sharpg{gk})"
    sh_fill = f"url(#sharpg{gk})" if not reverse else f"url(#natg{gk})"
    if night:
        nat_fill = "#0c0c0c"; sh_fill = "#151515"
    # whites
    wi = 0
    wpos = {}
    for n in range(25):
        if n % 12 in WHITE:
            x = x0 + wi * pitch
            wpos[n] = x
            dy = 0.6 if pressed == n else 0
            out.append(f'<rect x="{x+0.3:.2f}" y="{y0+dy}" width="{pitch-0.6:.2f}" height="{wlen}" rx="0.8" '
                       f'fill="{nat_fill}" stroke="{"#000" if not night else "#222"}" stroke-opacity="0.35" stroke-width="0.25"/>')
            if reverse and glow_front is False:
                pass
            wi += 1
    # blacks
    bw = 10.0
    for n in range(25):
        if n % 12 not in WHITE:
            xl = wpos[n - 1] + pitch - bw / 2
            out.append(f'<g filter="url(#sh)"><rect x="{xl:.2f}" y="{y0}" width="{bw}" height="{blen}" rx="0.9" '
                       f'fill="{sh_fill}"/></g>')
            if not night:
                out.append(f'<rect x="{xl+1.2:.2f}" y="{y0+2}" width="{bw-2.4}" height="{blen-6}" rx="0.6" '
                           f'fill="#fff" opacity="0.05"/>')
            if glow_front:
                c = "#b9ff9e" if night else p["ptr"]
                g = ' filter="url(#glow)"' if night else ""
                out.append(f'<rect x="{xl+1.5:.2f}" y="{y0+blen-2.6}" width="{bw-3}" height="1.6" rx="0.6" '
                           f'fill="{c}"{g} opacity="{1 if night else 0.9}"/>')
    # front glow strip for reverse (bone) sharps handled above; add C markers for orientation at night
    return "".join(out)


def wheels(x0, y0, p, night=False, h=60):
    """Two thumbwheels in a 35 mm zone. (x0,y0) top-left of the zone."""
    out = []
    for i, (lab, val) in enumerate((("bend", 0.5), ("mod", 0.25))):
        x = x0 + 4 + i * 15
        out.append(f'<rect x="{x}" y="{y0}" width="12" height="{h}" rx="2" fill="#070707"/>')
        out.append(f'<rect x="{x+1.5}" y="{y0+3}" width="9" height="{h-6}" rx="3" fill="url(#capg)"/>')
        for k in range(int((h - 8) / 2.2)):
            yy = y0 + 4.5 + k * 2.2
            out.append(f'<line x1="{x+2}" y1="{yy:.2f}" x2="{x+10}" y2="{yy:.2f}" stroke="{p["cap_lo"]}" stroke-width="0.6"/>')
        cy = y0 + h * (1 - val) if i else y0 + h / 2
        c = "#b9ff9e" if night else p["ptr"]
        g = ' filter="url(#glow)"' if night else ""
        out.append(f'<rect x="{x+1.5}" y="{cy-0.8:.2f}" width="9" height="1.6" fill="{c}"{g}/>')
        if not night:
            out.append(txt(x + 6, y0 + h + 5, lab, 2.8, p["silk"] if p.get("wheel_on_panel") else p["ink"]))
    return "".join(out)


# ---------------------------------------------------------------- materials
def body_fill(p, mat=None):
    mat = mat or p["body_mat"]
    if mat == "felt":
        return f'fill="{p["body_top"]}" filter="url(#feltf)"'
    if mat == "walnut":
        return f'fill="{p["body_top"]}" filter="url(#grainf)"'
    if mat == "acrylic":
        return 'fill="url(#acryl)"'
    if mat == "cork":
        return 'fill="#b48a5e" filter="url(#corkf)"'
    return f'fill="{p["body_top"]}"'


LAYER = {
    "felt": ("#8b8780", "url(#feltf)"),
    "felt2": ("#6f6b65", "url(#feltf)"),
    "cork": ("#b48a5e", "url(#corkf)"),
    "walnut": ("#5b3a26", "url(#grainf)"),
    "birch": ("#d8c39a", "url(#grainf)"),
    "acrylic": ("#1d2423", None),
    "acrylic_hi": ("#2a3533", None),
    "pcb_black": ("#1b1b1b", None),
    "pcb_white": ("#efeadf", None),
    "ply_grey": ("#7d7a74", "url(#feltf)"),
    "brass": ("#b8933f", None),
}


def stack_side(x, ybot, w, layers, round_end=0):
    """Side elevation of a laminated stack. layers: list of (thickness_mm, material) bottom→top."""
    out = []
    y = ybot
    for t, m in layers:
        col, flt = LAYER[m]
        f = f' filter="{flt}"' if flt else ""
        out.append(f'<rect x="{x:.2f}" y="{y-t:.2f}" width="{w:.2f}" height="{t:.2f}" fill="{col}"{f}/>')
        if m == "walnut":  # ply edge: show the thin plies
            n = max(int(t / 0.6), 1)
            for k in range(1, n):
                yy = y - t * k / n
                out.append(f'<line x1="{x:.2f}" y1="{yy:.2f}" x2="{x+w:.2f}" y2="{yy:.2f}" stroke="#c8ad7f" stroke-width="0.12" opacity="0.7"/>')
        if m.startswith("acrylic"):
            out.append(f'<line x1="{x:.2f}" y1="{y-t+0.25:.2f}" x2="{x+w:.2f}" y2="{y-t+0.25:.2f}" stroke="#6c7c79" stroke-width="0.3"/>')
        out.append(f'<line x1="{x:.2f}" y1="{y:.2f}" x2="{x+w:.2f}" y2="{y:.2f}" stroke="#000" stroke-opacity="0.25" stroke-width="0.12"/>')
        y -= t
    return "".join(out), y


# ---------------------------------------------------------------- annotation (sheet space, px)
def dim_h(x1, x2, y, label, size=22, color="#555", tick=10):
    return (f'<g stroke="{color}" stroke-width="1.5"><line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}"/>'
            f'<line x1="{x1}" y1="{y-tick}" x2="{x1}" y2="{y+tick}"/><line x1="{x2}" y1="{y-tick}" x2="{x2}" y2="{y+tick}"/></g>'
            + txt((x1 + x2) / 2, y - 8, label, size, color, font=UI_FONT, weight=500))


def dim_v(x, y1, y2, label, size=22, color="#555", tick=10, side=1):
    return (f'<g stroke="{color}" stroke-width="1.5"><line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}"/>'
            f'<line x1="{x-tick}" y1="{y1}" x2="{x+tick}" y2="{y1}"/><line x1="{x-tick}" y1="{y2}" x2="{x+tick}" y2="{y2}"/></g>'
            + txt(x + side * 14, (y1 + y2) / 2 + 8, label, size, color, font=UI_FONT, weight=500,
                  anchor="start" if side > 0 else "end"))


def callout(x, y, tx, ty, lines, size=24, color="#22211f", anchor="start", dot=True):
    out = [f'<line x1="{x}" y1="{y}" x2="{tx}" y2="{ty}" stroke="{color}" stroke-width="1.5"/>']
    if dot:
        out.append(f'<circle cx="{x}" cy="{y}" r="6" fill="none" stroke="{color}" stroke-width="2.5"/>')
    for i, l in enumerate(lines):
        out.append(txt(tx + (8 if anchor == "start" else -8), ty + 8 + i * size * 1.3, l, size, color,
                       font=UI_FONT, anchor=anchor, weight=600 if i == 0 else 400))
    return "".join(out)


def para(x, y, lines, size=24, color="#22211f", lh=1.38, weight_first=None, anchor="start"):
    out = []
    for i, l in enumerate(lines):
        w = 400
        if isinstance(l, tuple):
            l, w = l
        out.append(txt(x, y + i * size * lh, l, size, color, font=UI_FONT, anchor=anchor, weight=w))
    return "".join(out)


def svg_doc(w, h, body, p, bg=None):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            + defs(p) + f'<rect width="{w}" height="{h}" fill="{bg or p["bg"]}"/>' + body + "</svg>")
