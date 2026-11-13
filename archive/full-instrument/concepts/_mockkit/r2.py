"""Round-2 parts at R1 minimums (scores.md R1): panel 280 x 100, caps 12 mm at >= 17 mm pitch,
faders 11 mm pitch / 28 mm travel, legends Kalam 3.6 mm (cap height 2.66 mm; Kalam capHeight = 0.739 em),
rotary numerals 3.4 mm (cap 2.5 mm). All coordinates in mm. Panel origin = rear-left, y grows toward the keys.

Controls are drawn as BOUGHT parts (owner.md: "finished instrument should be real parts"):
skirted knurled knobs (Davies-1900H-style clone), a big skirted hero, Alpha-style fader caps,
sub-mini toggles, thumbwheel pots. Nothing touched is 3D-printed.
"""
import math
from kit import *

LS = 3.6     # legend font size, mm  -> cap height 2.66 mm  (R1: >= 2.5)
NS = 3.4     # rotary numerals        -> cap height 2.51 mm
HS = 3.2     # gold section headers
OWN_C = "#ffb020"   # amber: the "not in control" light colour everywhere
PW, PD = 280, 100


def lab(x, y, s, p, size=LS, fill=None, weight=400, anchor="middle"):
    return txt(x, y, s, size, fill or p["silk"], weight=weight, anchor=anchor)


def own_ring(cx, cy, r, p):
    """Gold ring = 'MIDI can take this one' (director R7 visual idea)."""
    return f'<circle cx="{cx}" cy="{cy}" r="{r+0.75:.2f}" fill="none" stroke="{p["gold"]}" stroke-width="0.55"/>'


def Kn(cx, cy, p, val, label=None, night=False, own=False, d=12, size=LS, lab_dy=9.8):
    o = knob(cx, cy, p, d, val=val, label=None, night=night)
    if own and not night:
        o = own_ring(cx, cy, d / 2, p) + o
    if label and not night:
        o += lab(cx, cy + lab_dy, label, p, size)
    return o


def Rot(cx, cy, p, kind, pos, night=False, d=12, rr=10.0, numerals=True):
    """6-position rotary switch (bought: Lorlin-type) with a skirted pointer knob."""
    r = d / 2
    angs = [-75, -45, -15, 15, 45, 75]   # Lorlin-type 30-degree index
    o = []
    if not night:
        for i, a in enumerate(angs):
            x0, y0 = pol(cx, cy, r + 1.0, a); x1, y1 = pol(cx, cy, r + 2.4, a)
            o.append(f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" stroke="{p["silk"]}" stroke-width="0.45" stroke-linecap="round"/>')
            if not numerals:
                continue
            lx, ly = pol(cx, cy, rr, a)
            if kind == "range":
                o.append(txt(lx, ly + 1.2, ["lo", "32", "16", "8", "4", "2"][i], NS, p["silk"]))
            else:
                o.append(wave_glyph(lx, ly, ["tri", "shark", "saw", "sq", "wide", "narrow"][i], 3.4, 2.0, p["silk"], 0.38))
    o.append(knob(cx, cy, p, d, val=(angs[pos] + 135) / 270, ticks=False, night=night))
    return "".join(o)


def Tg(cx, cy, p, up=True, label=None, night=False, size=LS, lab_dy=9.2):
    o = toggle(cx, cy, p, up=up, label=None, night=night)
    if label and not night:
        o += lab(cx, cy + lab_dy, label, p, size)
    return o


def Bt(cx, cy, p, d=8, label=None, night=False, lit=None, lab_dy=None):
    o = button(cx, cy, p, d=d, label=None, night=night, lit=lit)
    if label and not night:
        o += lab(cx, cy + (lab_dy or d / 2 + 6.4), label, p)
    return o


def Fd(cx, y0, p, val, label=None, night=False, own=False, travel=28):
    s, cy = fader(cx, y0, p, travel=travel, val=val, night=night)
    if own and not night:
        s = f'<circle cx="{cx}" cy="{y0-1.6}" r="0.9" fill="{p["gold"]}"/>' + s
    if label and not night:
        s += lab(cx, y0 + travel + 6 + 4.6, label, p)
    return s, cy


def pip(cx, cy, on=True, r=0.95):
    return led(cx, cy, OWN_C, r, on=on)


# ------------------------------------------------------------------------------------------ panel
def motto_rear(x):
    """MOTTO bentside: rear-edge offset (mm) along the panel. Straight to x=115, then an S to +25 (fix pass; was +30)."""
    if x <= 115:
        return 0.0
    t = min((x - 115) / 168.0, 1.0)
    return 25 * t * t * (3 - 2 * t)      # fix pass: 110 spine -> 85 right (systems: 190 -> 165 body)


def panel(p, kind="slab", night=False, light="pip", light_on=True, owned=None):
    """kind: slab | dock | motto.  light: pip (V-a) | none (V-b) | pips (V-c).
    owned: set of control ids currently owned by MIDI (lights their pip in V-c)."""
    owned = owned or set()
    o = []
    M = kind == "motto"
    D = 10 if M else 0                      # MOTTO: panel 110 deep at the spine (M2: was 115); rows sit nearer the keys
    depth = 110 if M else PD
    rows = [16 + D, 40 + D, 64 + D, 88 + D]
    bg = "#050505" if night else p["panel"]
    if M:
        pts = [(0, 0), (115, 0)] + [(x, motto_rear(x)) for x in range(120, 281, 5)] + [(280, depth), (0, depth)]
        o.append(f'<path d="M{" L".join(f"{x:.1f},{y:.2f}" for x, y in pts)} Z" fill="{bg}"/>')
    else:
        o.append(f'<rect x="0" y="0" width="{PW}" height="{PD}" rx="2" fill="{bg}"/>')
    pips = []        # (cx, cy, id) for V-c

    def own_k(cx, cy, val, label, cid, d=12):
        pips.append((cx + d / 2 + 2.0, cy - d / 2 - 1.0, cid))
        return Kn(cx, cy, p, val, label, night, own=True, d=d)

    # ---- section rules + headers
    if not night:
        for x in (55, 74, 146, 202):
            y0 = (motto_rear(x) + 4) if M else 4
            o.append(rule(x, y0, x, depth - 4, p, 0.4))
        heads = [(27.5, "play"), (64.5, "control"), (86, "osc 1"), (110, "osc 2"), (134, "osc 3"), (174, "mixer")]
        for x, s in heads:
            yy = (D + 4.6) if (M and x > 55) else 4.6
            if M and x < 55:
                continue
            o.append(lab(x, yy, s, p, HS, p["gold"], 700))
    # ---- PLAY
    if not M:
        o.append(Kn(9, 16, p, .62, "emphasis", night))
        o.append(Kn(27, 16, p, .45, "amount", night))
        o.append(own_k(45, 16, .25, "glide", "glide"))
        hx, hy = 18, 55
        if not night:
            o.append(own_ring(hx, hy, 13, p))
        o.append(hero(hx, hy, p, d=26, night=night, label=None))
        pips.append((hx + 12, hy - 13, "cutoff"))
        if not night:
            o.append(lab(hx, hy + 19.2, "cutoff", p, 4.6, weight=700))
        o.append(Tg(45, 40, p, True, "on", night))
        o.append(Tg(45, 63, p, False, "decay", night))
        o.append(Bt(45, 86, p, 8, "hold", night))
        o.append(Tg(9, 88, p, True, "kbd 1", night))
        o.append(Tg(27, 88, p, False, "kbd 2", night))
        if light == "pip":
            o.append(pip(52.2, 79, light_on))
    else:
        # rose sits at the rear-left, drawn by the concept (it is the grille)
        o.append(Kn(10, 56, p, .62, "emphasis", night))
        o.append(Kn(30, 56, p, .45, "amount", night))
        hx, hy = 20, 84
        if not night:
            o.append(own_ring(hx, hy, 13, p))
        o.append(hero(hx, hy, p, d=26, night=night, label=None))
        pips.append((hx + 12, hy - 13, "cutoff"))
        if not night:
            o.append(lab(hx, 104.6, "cutoff", p, 4.6, weight=700))
        o.append(Tg(48.5, 13, p, True, "kbd 1", night, size=3.4))
        o.append(Tg(48.5, 37, p, False, "kbd 2", night, size=3.4))
        o.append(own_k(46, 56, .25, "glide", "glide"))
        o.append(Tg(46, 80, p, True, "on", night))
        o.append(Tg(46, 98, p, False, "decay", night, lab_dy=8.6))
    # ---- CONTROL
    cx = 64.5
    o.append(own_k(cx, rows[0], .5, "tune", "tune"))
    o.append(Kn(cx, rows[1], p, .3, "mod mix", night))
    o.append(Tg(cx, rows[2], p, True, "osc mod", night))
    o.append(Tg(cx, rows[3], p, False, "filt mod", night, lab_dy=8.6 if M else 9.2))
    # ---- OSCILLATORS
    for i, x in enumerate((86, 110, 134)):
        o.append(Rot(x, rows[0] + 2, p, "range", [2, 2, 3][i], night))
        o.append(Rot(x, rows[1] + 2, p, "wave", [2, 3, 5][i], night))
    o.append(own_k(110, rows[2] + 2, .5, "freq 2", "freq2"))
    o.append(own_k(134, rows[2] + 2, .58, "freq 3", "freq3"))
    o.append(Tg(134, rows[3], p, False, "osc 3 ctl", night, lab_dy=8.6 if M else 9.2))
    if not night:
        o.append(lab(98, rows[2] + 4, "range ↑", p, 3.0, p["gold"]))
        o.append(lab(98, rows[2] + 9, "wave ↑", p, 3.0, p["gold"]))
    # ---- MIXER
    for k, (labl, v, on) in enumerate((("osc 1", .8, 1), ("osc 2", .6, 1), ("osc 3", .5, 1))):
        o.append(Kn(156, rows[k], p, v, labl, night))
        o.append(Tg(167.5, rows[k] - 1, p, bool(on), None, night))
    for k, (labl, v, on) in enumerate((("ext", 0.0, 0), ("noise", .15, 0))):
        o.append(Kn(182, rows[k], p, v, labl, night))
        o.append(Tg(193.5, rows[k] - 1, p, bool(on), None, night))
    o.append(Tg(182, rows[2], p, False, "feedback", night))
    o.append(Tg(156, rows[3], p, True, "wh/pk", night, lab_dy=8.6 if M else 9.2))
    o.append(Tg(182, rows[3], p, False, "ext pad", night, lab_dy=8.6 if M else 9.2))
    # ---- RIGHT BLOCK: contours + out (+ grille on SLAB/DOCK)
    fv = [0.15, 0.55, 0.7, 0.1, 0.45, 0.85]
    xs = (210, 221, 232, 248, 259, 270)
    fy = 40 if M else 58
    for i, x in enumerate(xs):
        s, _ = Fd(x, fy, p, fv[i], ["a", "d", "s"][i % 3], night, own=True)
        o.append(s)
        pips.append((x + 4.2, fy - 1.6, "fader%d" % i))
    if not night:
        for grp, vals in ((xs[:3], fv[:3]), (xs[3:], fv[3:])):
            pts = " ".join(f"{x},{fy+3+28*(1-v):.1f}" for x, v in zip(grp, vals))
            o.append(f'<polyline points="{pts}" fill="none" stroke="{p["gold"]}" stroke-width="0.35" stroke-dasharray="0.8 0.8"/>')
        o.append(lab(221, fy - 4.2, "filter contour", p, 3.0, p["gold"], 700))
        o.append(lab(259, fy - 4.2, "loudness contour", p, 3.0, p["gold"], 700))
    if not M:
        o.append(Kn(212, 16, p, .6, "volume", night))
        o.append(Kn(212, 40, p, .4, "phones", night))
        o.append(Bt(226.5, 15, p, 7, None, night))
        if not night:
            o.append(lab(226.5, 26, "tune", p))
        o.append(led(226.5, 38, p["led"], 1.1))
        if night:
            o.append('<circle cx="257" cy="27" r="22" fill="#080808"/>')
        else:
            o.append(grille(257, 27, 20.5, p))
            o.append(lab(257, 3.6, "speaker Ø40 driver", p, 2.6, p["gold"]))
    else:
        o.append(Kn(213, 92, p, .6, "volume", night, lab_dy=9.4))
        o.append(Kn(233, 92, p, .4, "phones", night, lab_dy=9.4))
        o.append(Bt(252, 91, p, 7, "hold", night, lab_dy=10))
        o.append(Bt(268, 91, p, 7, "tune", night, lab_dy=10))
        o.append(led(276.5, 81, p["led"], 1.1))
    # ---- V-c: 11 panel pips (the 12th, mod, is drawn by bendmod_lead)
    if light == "pips":
        for (x, y, cid) in pips:
            o.append(pip(x, y, (cid in owned) and light_on, 0.85))
    return "".join(o)


# ------------------------------------------------------------------------------------------ keys
def key_well(x0, y0, w, h, night=False):
    return f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="1.4" fill="{"#060606" if night else "#0b0b0b"}"/>'


def keys_lever(x0, y0, p, night=False, wlen=56, blen=34, reverse=False, n=25, pitch=17.4):
    """Piano-shaped lever key tops (service-cut) on bought Hall switches, piano layout. Uses kit.keyboard (25 keys) or one octave (n=13)."""
    if n == 25:
        return keyboard(x0, y0, p, pitch=pitch, wlen=wlen, blen=blen, reverse=reverse, night=night)
    gk, gd = pgrad(p)
    out = [gd]
    nat = "#0c0c0c" if night else (f"url(#sharpg{gk})" if reverse else f"url(#natg{gk})")
    sh = "#151515" if night else (f"url(#natg{gk})" if reverse else f"url(#sharpg{gk})")
    wi, wpos = 0, {}
    for k in range(n):
        if k % 12 in WHITE:
            x = x0 + wi * pitch; wpos[k] = x; wi += 1
            out.append(f'<rect x="{x+0.3:.2f}" y="{y0}" width="{pitch-0.6:.2f}" height="{wlen}" rx="0.8" fill="{nat}" stroke="#000" stroke-opacity="0.35" stroke-width="0.25"/>')
    for k in range(n):
        if k % 12 not in WHITE:
            xl = wpos[k - 1] + pitch - 5
            out.append(f'<g filter="url(#sh)"><rect x="{xl:.2f}" y="{y0}" width="10" height="{blen}" rx="0.9" fill="{sh}"/></g>')
            c = "#b9ff9e" if night else p["ptr"]
            out.append(f'<rect x="{xl+1.5:.2f}" y="{y0+blen-2.6}" width="7" height="1.6" rx="0.6" fill="{c}" opacity="0.9"/>')
    return "".join(out)


def keys_pegs(x0, y0, p, night=False, n=25, pitch=17.4, wood="#d9b98a", wood2="#3a2618"):
    """Bought maple button-top plugs, two rows: naturals Ø14 front, sharps Ø12 behind (DISH)."""
    o = []
    yb, yf = y0 + 14, y0 + 40
    wi, wpos = 0, {}
    for k in range(n):
        if k % 12 in WHITE:
            x = x0 + wi * pitch + pitch / 2; wpos[k] = x; wi += 1
            f = "#0e0e0e" if night else wood
            o.append(f'<circle cx="{x:.2f}" cy="{yf}" r="8.2" fill="#2b2b2b" opacity="{0.3 if night else 0.55}"/>')  # felt collar
            o.append(f'<g filter="url(#sh)"><circle cx="{x:.2f}" cy="{yf}" r="7" fill="{f}"/></g>')
            if not night:
                o.append(f'<ellipse cx="{x-2:.2f}" cy="{yf-2.2}" rx="3" ry="1.8" fill="#fff" opacity="0.25"/>')
            if k % 12 == 0:
                c = "#b9ff9e" if night else p["signal"]
                o.append(f'<circle cx="{x:.2f}" cy="{yf+10.4}" r="0.9" fill="{c}"{" filter=\"url(#glow)\"" if night else ""}/>')
    for k in range(n):
        if k % 12 not in WHITE:
            x = wpos[k - 1] + pitch / 2
            f = "#151515" if night else wood2
            o.append(f'<circle cx="{x:.2f}" cy="{yb}" r="7.2" fill="#2b2b2b" opacity="{0.3 if night else 0.55}"/>')
            o.append(f'<g filter="url(#sh)"><circle cx="{x:.2f}" cy="{yb}" r="6" fill="{f}"/></g>')
            c = "#b9ff9e" if night else p["ptr"]
            o.append(f'<circle cx="{x:.2f}" cy="{yb+3.4}" r="0.8" fill="{c}"{" filter=\"url(#glow)\"" if night else ""}/>')
    return "".join(o)


def keys_pads(x0, y0, p, night=False, n=13, pitch=17.4, nat="#3b3f3d", sh="#c9562f"):
    """Bought silicone button pads (12 x 12 class) laid out naturals-front / sharps-behind."""
    o = []
    wi, wpos = 0, {}
    for k in range(n):
        if k % 12 in WHITE:
            x = x0 + wi * pitch; wpos[k] = x; wi += 1
            o.append(f'<rect x="{x+1.6:.2f}" y="{y0+26}" width="{pitch-3.2:.2f}" height="{pitch-3.2:.2f}" rx="2.4" fill="{"#0e0e0e" if night else nat}"/>')
            if not night:
                o.append(f'<rect x="{x+2.6:.2f}" y="{y0+27}" width="{pitch-5.2:.2f}" height="{pitch-6.2:.2f}" rx="1.8" fill="#fff" opacity="0.06"/>')
    for k in range(n):
        if k % 12 not in WHITE:
            x = wpos[k - 1] + pitch - (pitch - 3.2) / 2
            o.append(f'<g filter="url(#sh)"><rect x="{x:.2f}" y="{y0+6}" width="{pitch-3.2:.2f}" height="{pitch-3.2:.2f}" rx="2.4" fill="{"#151515" if night else sh}"/></g>')
    return "".join(o)


def keys_switch(x0, y0, p, night=False, n=13, pitch=17.4, cap="#e8e4da", cap2="#2d2b28"):
    """Hall-effect keyboard switches + blank 1u caps, OP-1-like flat keys in piano order."""
    o = []
    wi, wpos = 0, {}
    for k in range(n):
        if k % 12 in WHITE:
            x = x0 + wi * pitch; wpos[k] = x; wi += 1
            o.append(f'<rect x="{x+1:.2f}" y="{y0+24}" width="{pitch-2:.2f}" height="{pitch-1:.2f}" rx="1.6" fill="#9a968d"/>')
            o.append(f'<rect x="{x+2.2:.2f}" y="{y0+25}" width="{pitch-4.4:.2f}" height="{pitch-4:.2f}" rx="1.4" fill="{"#0e0e0e" if night else cap}"/>')
    for k in range(n):
        if k % 12 not in WHITE:
            x = wpos[k - 1] + pitch / 2 + 1
            o.append(f'<rect x="{x:.2f}" y="{y0+4}" width="{pitch-2:.2f}" height="{pitch-1:.2f}" rx="1.6" fill="#1a1918"/>')
            o.append(f'<rect x="{x+1.2:.2f}" y="{y0+5}" width="{pitch-4.4:.2f}" height="{pitch-4:.2f}" rx="1.4" fill="{"#151515" if night else cap2}"/>')
    return "".join(o)


def wheels_thin(x0, y0, p, night=False, h=46, w=5.2, gap=1.8):
    """Two bought thumbwheel pots in the 13 mm wheel zone (bend centre-sprung, mod free)."""
    o = []
    for i, val in enumerate((0.5, 0.3)):
        x = x0 + i * (w + gap)
        o.append(f'<rect x="{x}" y="{y0}" width="{w}" height="{h}" rx="1.4" fill="#070707"/>')
        o.append(f'<rect x="{x+0.7}" y="{y0+2}" width="{w-1.4}" height="{h-4}" rx="2" fill="url(#capg)"/>')
        for k in range(int((h - 6) / 2.1)):
            yy = y0 + 3.4 + k * 2.1
            o.append(f'<line x1="{x+0.9}" y1="{yy:.1f}" x2="{x+w-0.9}" y2="{yy:.1f}" stroke="{p["cap_lo"]}" stroke-width="0.4"/>')
        cy = y0 + 2 + (h - 4) * (1 - val)
        c = "#b9ff9e" if night else p["ptr"]
        o.append(f'<rect x="{x+0.7}" y="{cy-0.6:.1f}" width="{w-1.4}" height="1.2" fill="{c}"{" filter=\"url(#glow)\"" if night else ""}/>')
    return "".join(o)


# ------------------------------------------------------------------------------------------ side-view helpers
def capsil(x, ytop, w, h, col, rx=1.0):
    """A cap silhouette standing on a surface whose top is ytop (y up = negative)."""
    return f'<rect x="{x:.2f}" y="{ytop-h:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx}" fill="{col}"/>'


def part(x, y, w, h, fill, stroke="#222", sw=0.25, rx=0.6, extra=""):
    return f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'


ZW = 22.0     # bend/mod zone width (scores.md F3; eng budget-variant §v1.5b: Adafruit #2765 body 17.5 x 17.4)


def bendmod_lead(x0, y0, p, night=False, h=54, w=ZW, pip=None):
    """LEAD bend/mod, fix pass (F3 + MIDI correction):
    rear: 20 mm-travel mod slide pot, Pico-read -> AS3360 (eng E1), so it is MIDI-ownable (gold dot, CC1 in/out);
    front: Adafruit #2765 mini thumbstick (17.5 x 17.4 body, through-hole) under a fore-aft Delrin gate slot,
    one axis read, springs back. Dashed = part bodies under the deck. pip: None | False | True (V-c light)."""
    o = [f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="1.8" fill="{"#060606" if night else "#141414"}"/>']
    cx = x0 + w / 2
    # part bodies under the deck (dashed): slide pot body ~30 mm (UNVERIFIED), stick body 17.5 x 17.4
    sb_y = y0 + h - 2.2 - 17.4
    if not night:
        o.append(f'<rect x="{cx-2.5}" y="{y0+1.2}" width="5" height="30" rx="0.6" fill="none" stroke="#555" stroke-width="0.25" stroke-dasharray="0.8 0.6"/>')
        o.append(f'<rect x="{cx-8.75}" y="{sb_y:.2f}" width="17.5" height="17.4" rx="0.8" fill="none" stroke="#555" stroke-width="0.25" stroke-dasharray="0.8 0.6"/>')
    # mod fader: 20 mm travel slot
    fy = y0 + 3
    o.append(f'<rect x="{cx-0.8}" y="{fy}" width="1.6" height="26" rx="0.8" fill="#000"/>')
    if not night:
        for k in range(6):
            yy = fy + 3 + k * 4
            o.append(f'<line x1="{cx-5.6}" y1="{yy}" x2="{cx-4.2}" y2="{yy}" stroke="#777" stroke-width="0.3"/>')
        # gold dot = MIDI can take it (same mark as the contour faders)
        o.append(f'<circle cx="{cx+5.2}" cy="{fy+1.0}" r="0.9" fill="{p["gold"]}"/>')
    cyf = fy + 3 + 20 * 0.35
    if night:
        o.append(f'<line x1="{cx-3}" y1="{cyf}" x2="{cx+3}" y2="{cyf}" stroke="#b9ff9e" stroke-width="0.9" filter="url(#glow)"/>')
    else:
        o.append(f'<g filter="url(#sh)"><rect x="{cx-3.5}" y="{cyf-4.5}" width="7" height="9" rx="1" fill="url(#capg)"/></g>'
                 f'<line x1="{cx-3.3}" y1="{cyf}" x2="{cx+3.3}" y2="{cyf}" stroke="{p["ptr"]}" stroke-width="0.8"/>')
    if pip is not None:
        o.append(led(cx + 5.2, fy + 4.6, OWN_C, 0.85, on=pip))
    # bend stick: fore-aft gate slot over the stick centre
    sc = sb_y + 8.7
    gy0, gy1 = sc - 7, sc + 7
    o.append(f'<rect x="{cx-2.0}" y="{gy0:.2f}" width="4.0" height="{gy1-gy0:.2f}" rx="2.0" fill="#000" stroke="{"#222" if night else p["gold"]}" stroke-width="0.35"/>')
    if not night:
        o.append(f'<line x1="{cx-7.6}" y1="{sc:.2f}" x2="{cx-6.4}" y2="{sc:.2f}" stroke="{p["gold"]}" stroke-width="0.45"/>'
                 f'<line x1="{cx+6.4}" y1="{sc:.2f}" x2="{cx+7.6}" y2="{sc:.2f}" stroke="{p["gold"]}" stroke-width="0.45"/>')
        o.append(f'<g filter="url(#sh)"><circle cx="{cx}" cy="{sc:.2f}" r="5.5" fill="url(#capg)"/></g>'
                 f'<circle cx="{cx}" cy="{sc:.2f}" r="3.6" fill="none" stroke="{p["cap_lo"]}" stroke-width="0.35" stroke-dasharray="0.5 0.5"/>')
    else:
        o.append(f'<circle cx="{cx}" cy="{sc:.2f}" r="1.2" fill="#b9ff9e" filter="url(#glow)"/>')
    return "".join(o)
