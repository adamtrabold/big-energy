"""OP-1-class compact parts: 282 mm wide. Panel 276 x 70 (eurorack density), key strips 282 x 76.

Standard cap 10.5 mm at >= 14 mm pitch (Plaits/Rings density), hero 26 mm, sub-mini toggles,
20 mm-travel mini faders at 7.5 mm pitch, 26 mm grille over a ~36 mm driver."""
import math
from kit import *

PW, PH = 276, 70      # panel
HW, HD = 282, 76      # each half (panel half / key half)
KC = 10.5             # standard cap


def mfader(cx, y0, p, val, label=None, night=False, travel=20):
    o = []
    L = travel + 6
    if not night:
        for i in range(5):
            yy = y0 + 3 + travel * i / 4
            o.append(f'<line x1="{cx-2.6-(1.6 if i % 2 == 0 else 0.9):.2f}" y1="{yy:.2f}" x2="{cx-2.6:.2f}" y2="{yy:.2f}" stroke="{p["silk"]}" stroke-width="0.25"/>')
    o.append(f'<rect x="{cx-0.7}" y="{y0}" width="1.4" height="{L}" rx="0.7" fill="#050505"/>')
    cy = y0 + 3 + travel * (1 - val)
    if night:
        o.append(f'<rect x="{cx-2.4}" y="{cy-3.5}" width="4.8" height="7" rx="0.8" fill="#0d0d0d"/>')
        o.append(f'<line x1="{cx-2}" y1="{cy}" x2="{cx+2}" y2="{cy}" stroke="#b9ff9e" stroke-width="0.8" filter="url(#glow)"/>')
    else:
        o.append(f'<g filter="url(#sh)"><rect x="{cx-2.4}" y="{cy-3.5}" width="4.8" height="7" rx="0.8" fill="url(#capg)"/></g>')
        o.append(f'<line x1="{cx-2.2}" y1="{cy}" x2="{cx+2.2}" y2="{cy}" stroke="{p["ptr"]}" stroke-width="0.7"/>')
    if label and not night:
        o.append(txt(cx, y0 + L + 3.4, label, 2.1, p["silk"]))
    return "".join(o), cy


def stog(cx, cy, p, up=True, label=None, night=False, lab_dy=6.6, size=1.85):
    """Sub-mini toggle."""
    if night:
        return f'<circle cx="{cx}" cy="{cy}" r="2" fill="#101010"/>'
    hexpts = " ".join(f"{cx+2.4*math.cos(math.radians(30+60*i)):.2f},{cy+2.4*math.sin(math.radians(30+60*i)):.2f}" for i in range(6))
    dy = -1 if up else 1
    o = [f'<polygon points="{hexpts}" fill="url(#metal)" stroke="#555" stroke-width="0.12"/>',
         f'<circle cx="{cx}" cy="{cy}" r="1.6" fill="#8d8a84"/>',
         f'<g filter="url(#sh)"><line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy+dy*3.2}" stroke="#d9d6cf" stroke-width="1.3" stroke-linecap="round"/>'
         f'<circle cx="{cx}" cy="{cy+dy*3.3}" r="1.0" fill="#f2f0ea" stroke="#77746d" stroke-width="0.15"/></g>']
    if label:
        o.append(txt(cx, cy + lab_dy, label, size, p["silk"]))
    return "".join(o)


def crot(cx, cy, p, kind, pos, night=False, d=KC):
    """Compact 6-position rotary with tight legends."""
    r = d / 2
    angs = [-125, -75, -25, 25, 75, 125]
    o = []
    if not night:
        for i, a in enumerate(angs):
            x0, y0 = pol(cx, cy, r + 0.9, a); x1, y1 = pol(cx, cy, r + 1.9, a)
            o.append(f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" stroke="{p["silk"]}" stroke-width="0.35"/>')
            lx, ly = pol(cx, cy, r + 2.85, a)
            if kind == "range":
                o.append(txt(lx, ly + 0.5, ["LO", "32", "16", "8", "4", "2"][i], 1.4, p["silk"]))
            else:
                o.append(wave_glyph(lx, ly, ["tri", "shark", "saw", "sq", "wide", "narrow"][i], 1.8, 1.1, p["silk"], 0.25))
    o.append(knob(cx, cy, p, d, val=(angs[pos] + 135) / 270, ticks=False, night=night))
    return "".join(o)


def K(cx, cy, p, val, label=None, night=False, d=KC, ticks=True, size=2.1, lab_dy=None):
    return knob(cx, cy, p, d, val=val, label=label, night=night, ticks=ticks, label_size=size,
                lab_dy=lab_dy if lab_dy is not None else d / 2 + 4.3)


def panel_compact(p, night=False, light="pip", light_on=True, grille_on=True):
    """276 x 70. y=0 far edge, y=70 nearest the keys. Returns svg."""
    o = [f'<rect x="0" y="0" width="{PW}" height="{PH}" rx="2" fill="{"#050505" if night else p["panel"]}"/>']
    if not night:
        for x in (46, 72, 128, 196, 246):
            o.append(rule(x, 4, x, PH - 4, p, 0.35))
        for x, s in ((23, "play"), (59, "control"), (100, "oscillators"), (162, "mixer"), (221, "contours"), (261, "out")):
            o.append(txt(x, 3.6, s, 2.3, p["gold"], weight=700))
    # play
    o.append(K(8, 12, p, .25, "glide", night))
    o.append(K(23, 12, p, .62, "emph", night))
    o.append(K(38, 12, p, .45, "contour", night))
    o.append(hero(18, 48, p, d=24, night=night, lab_dy=19.3).replace('font-size="4.2"', 'font-size="2.9"'))
    o.append(button(39, 42, p, d=6, label=None, night=night))
    if not night:
        o.append(txt(39, 50, "hold", 1.9, p["silk"]))
    o.append(stog(39, 59, p, True, "glide", night, lab_dy=5.6))
    if light == "pip":
        o.append(led(33, 30.5, "#ffb020", 0.7, on=light_on))
    elif light == "perknob":   # one pip beside each MIDI-ownable control (cutoff, glide)
        o.append(led(33, 30.5, "#ffb020", 0.6, on=light_on))
        o.append(led(14.2, 5.2, "#ffb020", 0.55, on=False))
    # control
    o.append(K(59, 12, p, .5, "tune", night))
    o.append(K(59, 33, p, .3, "mod mix", night))
    o.append(stog(53, 54, p, True, "osc mod", night, size=1.7))
    o.append(stog(65, 54, p, False, "filt mod", night, size=1.7))
    # oscillators
    for i, x in enumerate((82, 100, 118)):
        o.append(crot(x, 12, p, "range", [2, 2, 3][i], night))
        o.append(crot(x, 33, p, "wave", [2, 3, 5][i], night))
        if i:
            o.append(K(x, 54, p, [.5, .58][i - 1], None, night, ticks=False))
        if not night:
            o.append(txt(x + 7.6, 22, str(i + 1), 3.2, p["silk"], weight=700))
    o.append(stog(82, 52, p, False, "osc 3 ctl", night, size=1.7, lab_dy=6.0))
    if not night:
        o.append(txt(109, 64.5, "freq 2 · freq 3", 1.9, p["silk"]))
    # mixer: knobs on top row, on/off under each, extras on the third row
    for k, (lab, v, on) in enumerate((("osc1", .8, 1), ("osc2", .6, 1), ("osc3", .5, 1), ("ext", 0, 0), ("noise", .15, 0))):
        x = 134 + k * 14
        o.append(K(x, 12, p, v, lab, night, d=10, ticks=False, lab_dy=8.6))
        o.append(stog(x, 31, p, bool(on), None, night))
    for x, lab, up in ((141, "wh/pk", 1), (162, "line/mod", 1), (183, "feedbk", 0)):
        o.append(stog(x, 52, p, bool(up), lab, night))
    # contours: 6 mini faders
    fv = [0.15, 0.55, 0.7, 0.1, 0.45, 0.85]
    xs = (202, 209.5, 217, 226, 233.5, 241)
    for i, x in enumerate(xs):
        s, _ = mfader(x, 7, p, fv[i], ["a", "d", "s"][i % 3], night)
        o.append(s)
    if not night:
        for grp in (xs[:3], xs[3:]):
            vals = fv[:3] if grp == xs[:3] else fv[3:]
            pts = " ".join(f"{x},{7+3+20*(1-v):.1f}" for x, v in zip(grp, vals))
            o.append(f'<polyline points="{pts}" fill="none" stroke="{p["gold"]}" stroke-width="0.3" stroke-dasharray="0.7 0.7"/>')
        o.append(txt(209.5, 44.5, "filter", 1.9, p["gold"]))
        o.append(txt(233.5, 44.5, "loudness", 1.9, p["gold"]))
    o.append(stog(204, 55, p, True, "kbd 1", night, size=1.7))
    o.append(stog(215, 55, p, False, "kbd 2", night, size=1.7))
    o.append(stog(234, 55, p, True, "decay", night, size=1.7))
    # out
    o.append(K(254, 12, p, .6, "vol", night, d=10, ticks=False, lab_dy=8.6))
    o.append(K(269, 12, p, .4, "phones", night, d=10, ticks=False, lab_dy=8.6))
    if not grille_on:
        if not night:
            o.append(txt(261.5, 40, "sound comes", 1.8, p["silk"], style="opacity:.55"))
            o.append(txt(261.5, 43, "from the rose", 1.8, p["silk"], style="opacity:.55"))
    elif night:
        o.append('<circle cx="261.5" cy="41" r="13" fill="#080808"/>')
    else:
        o.append(grille(261.5, 41, 12, p))
    o.append(button(253, 63, p, d=5, night=night))
    o.append(led(269, 63, p["led"], 1.0))
    if not night:
        o.append(txt(257.5, 64, "tune", 1.7, p["silk"], anchor="start"))
    return "".join(o)


# ---------------------------------------------------------------- key strips (282 x 76)
def key_strip(p, style="lever", night=False, reverse=False, bg=True, mat=None):
    """Key half, 282 x 76, player at the bottom. Styles explore different key ideas:
    lever   - short Delrin flexure levers (piano layout, real travel)
    pillow  - one cast/printed TPU sheet of soft keys over Hall magnets (silent, squashy)
    tongue  - laser-cut walnut tongues (one sheet, each key a flexing tongue), reverse colours
    buttons - two staggered rows of round keys (accordion/OP-1 order), shallow depth
    """
    o = []
    if bg:
        o.append(f'<g filter="url(#shbig)"><rect x="0" y="0" width="{HW}" height="{HD}" rx="4" '
                 f'{body_fill(p, mat) if not night else "fill=\"#0a0a0a\""}/></g>')
    pitch = 17.4
    x0 = 18.0   # wheel zone 3..16
    # mini wheels (bend spring-centred, mod free)
    for i, val in enumerate((0.5, 0.3)):
        x = 3.5 + i * 6.8
        o.append(f'<rect x="{x}" y="14" width="5.8" height="46" rx="1.5" fill="#070707"/>')
        o.append(f'<rect x="{x+0.8}" y="16" width="4.2" height="42" rx="2" fill="url(#capg)"/>')
        for k in range(18):
            o.append(f'<line x1="{x+1}" y1="{17.5+k*2.2:.1f}" x2="{x+4.8}" y2="{17.5+k*2.2:.1f}" stroke="{p["cap_lo"]}" stroke-width="0.4"/>')
        cy = 16 + 42 * (1 - val)
        o.append(f'<rect x="{x+0.8}" y="{cy-0.6:.1f}" width="4.2" height="1.2" fill="{"#b9ff9e" if night else p["ptr"]}"'
                 f'{" filter=\"url(#glow)\"" if night else ""}/>')
    if not night and not reverse:
        o.append(txt(7.3, 66, "bend", 1.8, p["ink"] if style != "pillow" else "#ccc"))
        o.append(txt(14, 69, "mod", 1.8, p["ink"] if style != "pillow" else "#ccc"))
    if style == "buttons":
        return "".join(o) + _buttons(p, x0, pitch, night)
    ky = 16
    wlen, blen = 52, 31
    o.append(f'<rect x="{x0-1.5}" y="{ky-2}" width="{15*pitch+3}" height="{wlen+3}" rx="1.2" fill="#0b0b0b"/>')
    if style == "lever":
        o.append(keyboard(x0, ky, p, pitch=pitch, wlen=wlen, blen=blen, night=night))
    elif style == "pillow":
        o.append(_pillows(p, x0, ky, pitch, wlen, blen, night))
    elif style == "tongue":
        o.append(_tongues(p, x0, ky, pitch, wlen, blen, night))
    return "".join(o)


def _pillows(p, x0, ky, pitch, wlen, blen, night):
    o = []
    nat = "#0c0c0c" if night else p.get("pillow_nat", "#2b2e2d")
    sh = "#151515" if night else p.get("pillow_sharp", "#4a5350")
    wi, wpos = 0, {}
    for n in range(25):
        if n % 12 in WHITE:
            x = x0 + wi * pitch; wpos[n] = x; wi += 1
            o.append(f'<rect x="{x+0.9:.2f}" y="{ky+1}" width="{pitch-1.8:.2f}" height="{wlen-2}" rx="3.2" fill="{nat}"/>')
            if not night:
                o.append(f'<rect x="{x+1.6:.2f}" y="{ky+2}" width="{pitch-3.2:.2f}" height="{wlen-5}" rx="2.6" fill="#fff" opacity="0.035"/>')
    for n in range(25):
        if n % 12 not in WHITE:
            xl = wpos[n - 1] + pitch - 4.6
            o.append(f'<g filter="url(#sh)"><rect x="{xl:.2f}" y="{ky}" width="9.2" height="{blen}" rx="3.5" fill="{sh}"/></g>')
            c = "#b9ff9e" if night else p["ptr"]
            o.append(f'<circle cx="{xl+4.6:.2f}" cy="{ky+blen-3.5}" r="1" fill="{c}"{" filter=\"url(#glow)\"" if night else ""}/>')
    return "".join(o)


def _tongues(p, x0, ky, pitch, wlen, blen, night):
    """Laser-cut walnut tongues, reverse colours (dark naturals, bone sharps on top)."""
    o = []
    wi, wpos = 0, {}
    for n in range(25):
        if n % 12 in WHITE:
            x = x0 + wi * pitch; wpos[n] = x; wi += 1
            fill = "#0c0c0c" if night else "#3a2416"
            o.append(f'<path d="M{x+0.45:.2f},{ky} h{pitch-0.9:.2f} v{wlen-3} q0,3 -3,3 h{-(pitch-6.9):.2f} q-3,0 -3,-3 Z" '
                     f'fill="{fill}"{" filter=\"url(#grainv)\"" if not night else ""}/>')
    for n in range(25):
        if n % 12 not in WHITE:
            xl = wpos[n - 1] + pitch - 4.5
            fill = "#151515" if night else "url(#natg)"
            o.append(f'<g filter="url(#sh)"><rect x="{xl:.2f}" y="{ky}" width="9" height="{blen}" rx="1.4" fill="{fill}"/></g>')
            c = "#b9ff9e" if night else "#b9a77a"
            o.append(f'<rect x="{xl+2:.2f}" y="{ky+blen-2.4}" width="5" height="1.2" rx="0.5" fill="{c}"{" filter=\"url(#glow)\"" if night else ""}/>')
    # the uncut root of the sheet (all tongues are one piece)
    if not night:
        o.append(f'<rect x="{x0}" y="{ky-1.6}" width="{15*pitch}" height="1.6" fill="#2a190f"/>')
    return "".join(o)


def _buttons(p, x0, pitch, night):
    """Two staggered rows: naturals front (Ø 14), sharps behind (Ø 12) at the black-key positions."""
    o = []
    yb, yf = 30, 50
    o.append(f'<rect x="{x0-1.5}" y="{yb-9}" width="{15*pitch+3}" height="{yf-yb+18}" rx="9" fill="#0b0b0b"/>')
    wi, wpos = 0, {}
    for n in range(25):
        if n % 12 in WHITE:
            x = x0 + wi * pitch + pitch / 2; wpos[n] = x; wi += 1
            f = "#0e0e0e" if night else "url(#natg)"
            o.append(f'<g filter="url(#sh)"><circle cx="{x:.2f}" cy="{yf}" r="7.2" fill="{f}"/></g>')
            if not night:
                o.append(f'<circle cx="{x:.2f}" cy="{yf}" r="5.2" fill="#000" opacity="0.06"/>')
            if n % 12 == 0:
                c = "#b9ff9e" if night else p["signal"]
                o.append(f'<circle cx="{x:.2f}" cy="{yf+4.6}" r="0.8" fill="{c}"{" filter=\"url(#glow)\"" if night else ""}/>')
    for n in range(25):
        if n % 12 not in WHITE:
            x = wpos[n - 1] + pitch / 2
            f = "#151515" if night else "url(#sharpg)"
            o.append(f'<g filter="url(#sh)"><circle cx="{x:.2f}" cy="{yb}" r="6.2" fill="{f}"/></g>')
            c = "#b9ff9e" if night else p["ptr"]
            o.append(f'<circle cx="{x:.2f}" cy="{yb+3.6}" r="0.8" fill="{c}"{" filter=\"url(#glow)\"" if night else ""}/>')
    return "".join(o)
