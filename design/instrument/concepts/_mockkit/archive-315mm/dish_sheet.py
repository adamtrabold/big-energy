"""DISH sheet (sauce): round control dish on a fold-flat fork, like a radio telescope.
Turn things on the dish; slide and flip things on the wings. Look: Proof (white dish, walnut, red)."""
import math
from kit import *
from common_views import *

OUT = "/home/claude/model-d/design/instrument/concepts/dish/"
BD = 290                 # base depth
RC = 80                  # recess radius
CX, CY = 157.5, 85       # recess centre (svg y from the back)
R = 77.5                 # dish radius
p0 = PAL["proof"]


def dish_face(p, night=False, light_on=True):
    """Dish face, local coords centred at (0,0), mm. Clock angles, 0 = top."""
    o = []
    if night:
        o.append(f'<circle r="{R}" fill="#060606"/>')
    else:
        o.append(f'<circle r="{R}" fill="{p["panel"]}" stroke="#5b3a26" stroke-width="2.2"/>')
        # section arcs (gold) + tangential names on the rim
        def arc(a0, a1, r):
            x0, y0 = pol(0, 0, r, a0); x1, y1 = pol(0, 0, r, a1)
            large = 1 if (a1 - a0) % 360 > 180 else 0
            return f'M{x0:.2f},{y0:.2f} A{r},{r} 0 {large} 1 {x1:.2f},{y1:.2f}'
        for a0, a1, name, flip in ((290, 50, "oscillators", 0), (52, 146, "mixer", 0),
                                   (250, 288, "control", 0), (206, 248, "play", 1)):
            o.append(f'<path d="{arc(a0, a1, 75)}" fill="none" stroke="{p["gold"]}" stroke-width="0.5"/>')
            pid = f"tp{a0}"
            if flip:  # bottom half: run the text path the other way so it reads left-to-right
                x0, y0 = pol(0, 0, 72.6, a1); x1, y1 = pol(0, 0, 72.6, a0)
                d = f'M{x0:.2f},{y0:.2f} A72.6,72.6 0 0 0 {x1:.2f},{y1:.2f}'
            else:
                d = arc(a0, a1, 73.2)
            o.append(f'<path id="{pid}" d="{d}" fill="none"/>')
            o.append(f'<text font-family="{LEG_FONT}" font-size="2.7" font-weight="700" fill="{p["gold"]}">'
                     f'<textPath href="#{pid}" startOffset="50%" text-anchor="middle">{name}</textPath></text>')
    # outer ring r 61: oscillators across the top, controllers left, mixer right
    ro, ri = 61, 45
    osc = [(300, "range", 2), (320, "wave", 2), (340, "range", 2), (0, "wave", 3), (20, "range", 3), (40, "wave", 5)]
    for a, kind, pos in osc:
        x, y = pol(0, 0, ro, a)
        o.append(rotary(x, y, p, kind, pos=pos, night=night, d=14))
    for k, a in enumerate((300, 340, 20)):
        x, y = pol(0, 0, ro + 0, a)
    for a, lab, v in ((280, "tune", 0.5), (262, "mod mix", 0.3)):
        x, y = pol(0, 0, ro, a)
        o.append(knob(x, y, p, d=14, val=v, ticks=False, night=night))
        if not night:
            lx, ly = pol(0, 0, ro - 12.5, a)
            o.append(txt(lx, ly + 1, lab, 2.4, p["silk"]))
    for k, (a, lab, v) in enumerate(((58, "osc 1", .8), (78, "osc 2", .6), (98, "osc 3", .5), (118, "ext", 0), (138, "noise", .15))):
        x, y = pol(0, 0, ro, a)
        o.append(knob(x, y, p, d=14, val=v, ticks=False, night=night))
        if not night:
            lx, ly = pol(0, 0, ro - 12.5, a)
            o.append(txt(lx, ly + 1, lab, 2.4, p["silk"]))
    # inner ring r 45: freq 2/3 under their oscillators, the play strip lower-left
    for a, lab, v in ((330, "freq 2", .5), (30, "freq 3", .58), (282, "glide", .2), (256, "emph", .6), (230, "contour", .45)):
        x, y = pol(0, 0, ri, a)
        o.append(knob(x, y, p, d=14, val=v, ticks=False, night=night))
        if not night:
            lx, ly = pol(0, 0, ri - 11.8, a) if a in (282, 256, 230) else pol(0, 0, ri + 0, a)
            if a in (330, 30):
                o.append(txt(x, y + 11.2, lab, 2.4, p["silk"]))
            else:
                o.append(txt(lx, ly + 1, lab, 2.4, p["silk"]))
    if not night:
        for k, a in enumerate((310, 350, 30)):
            x, y = pol(0, 0, 51.5, a + (0 if k else 0))
        x, y = pol(0, 0, ri, 310)
        o.append(txt(x, y + 1, "1 2 3", 3.2, p["silk"], weight=700))
    # centre: grille + bullseye light + cutoff ring
    if not night:
        o.append(grille(0, 0, 17.5, p, "bull"))
        o.append(scale_ticks(0, 0, 34, 36.6, 21, p, w=0.4))
    if light_on:
        o.append(f'<circle r="19.4" fill="none" stroke="#ffb020" stroke-width="1.6" filter="url(#glow)" opacity="0.95"/>')
    if night:
        o.append('<circle r="32.5" fill="none" stroke="#b9ff9e" stroke-width="0.6" opacity="0.5" filter="url(#glow)"/>')
    else:
        o.append(f'<g filter="url(#sh)"><path d="M0,-32.5 A32.5,32.5 0 1 1 0,32.5 A32.5,32.5 0 1 1 0,-32.5 Z '
                 f'M0,-20.5 A20.5,20.5 0 1 0 0,20.5 A20.5,20.5 0 1 0 0,-20.5 Z" fill="url(#herog)" fill-rule="evenodd"/></g>')
        o.append(f'<circle r="31.9" fill="none" stroke="{p["hero_lo"]}" stroke-width="1.2" stroke-dasharray="0.5 0.55"/>')
        o.append(f'<circle r="26.5" fill="none" stroke="{p["hero_lo"]}" stroke-width="0.3" opacity="0.6"/>')
    ang = -135 + 270 * 0.55
    x0, y0 = pol(0, 0, 21.5, ang); x1, y1 = pol(0, 0, 31.8, ang)
    o.append(f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" stroke="{"#b9ff9e" if night else p["ptr"]}" '
             f'stroke-width="2.2" stroke-linecap="round"{" filter=\"url(#glow)\"" if night else ""}/>')
    if not night:
        o.append(txt(0, 40.6, "cutoff", 3.4, p["silk"], weight=700) if False else "")
        lx, ly = pol(0, 0, 38.5, 180)
        o.append(txt(lx, ly + 1.4, "cutoff", 3.2, p["hero"], weight=700))
    return "".join(o)


def base_plan(p, night=False):
    """Base top view (svg y from the back), dish removed."""
    o = [f'<g filter="url(#shbig)"><rect x="0" y="0" width="315" height="{BD}" rx="6" '
         f'{body_fill(p) if not night else "fill=\"#0a0a0a\""}/></g>']
    # white panel PCB over the wings, circular cut-out
    hole = f'M{CX-RC},{CY} a{RC},{RC} 0 1 0 {2*RC},0 a{RC},{RC} 0 1 0 {-2*RC},0 Z'
    o.append(f'<path d="M5,5 H310 V{BD-128} H5 Z {hole}" fill="{"#050505" if night else p["panel"]}" fill-rule="evenodd"/>')
    o.append(f'<circle cx="{CX}" cy="{CY}" r="{RC}" fill="#1b1612"/>')
    o.append(f'<circle cx="{CX}" cy="{CY}" r="{RC-3}" fill="#2a221c" filter="url(#feltf)"/>')
    # fork pivots + channels for the folded fork arms
    for sx in (-1, 1):
        x = CX + sx * 84
        o.append(f'<rect x="{x-4}" y="{CY-2}" width="8" height="{RC+4}" rx="2" fill="#120e0b"/>')
        o.append(f'<circle cx="{x}" cy="{CY+RC}" r="3.2" fill="url(#brassg)"/>')
    # left wing: filter faders, kbd toggles, controllers toggles, hold / tune / status
    K = dict(night=night)
    fv = [0.15, 0.55, 0.7, 0.1, 0.45, 0.85]
    for i, x in enumerate((16, 28, 40)):
        s, _ = fader(x, 16, p, 30, fv[i], label=["a", "d", "s"][i], night=night); o.append(s)
    for i, x in enumerate((275, 287, 299)):
        s, _ = fader(x, 16, p, 30, fv[3 + i], label=["a", "d", "s"][i], night=night); o.append(s)
    if not night:
        o.append(txt(28, 11, "filter", 2.7, p["gold"], weight=700))
        o.append(txt(287, 11, "loudness", 2.7, p["gold"], weight=700))
    o.append(toggle(57, 22, p, True, "kbd 1", label_size=2.1, **K))
    o.append(toggle(57, 44, p, False, "kbd 2", label_size=2.1, **K))
    o.append(toggle(258, 22, p, True, "decay", label_size=2.1, **K))
    for i, (lab, up) in enumerate((("osc mod", 1), ("filt mod", 0), ("osc3", 0), ("glide", 1))):
        o.append(toggle(12 + i * 16, 82, p, bool(up), lab, label_size=2.1, **K))
    o.append(button(22, 140, p, label="hold", **K))
    o.append(button(46, 140, p, d=7.5, label="tune", **K))
    o.append(led(64, 136, p["led"], 1.3))
    if not night:
        o.append(txt(64, 145.5, "status", 2.0, p["silk"]))
    # right wing: mixer switches, output
    for i, (lab, up) in enumerate((("osc1", 1), ("osc2", 1), ("osc3", 1), ("ext", 0), ("noise", 0))):
        o.append(toggle(247 + i * 13.5, 82, p, bool(up), lab, label_size=2.0, **K))
    for i, (lab, up) in enumerate((("wh/pk", 1), ("line/mod", 1), ("feedbk", 0))):
        o.append(toggle(262 + i * 16, 108, p, bool(up), lab, label_size=2.0, **K))
    if not night:
        o.append(txt(278, 70, "mixer on", 2.5, p["gold"], weight=700))
    o.append(knob(266, 140, p, d=14, val=0.6, label="volume", ticks=False, **K))
    o.append(knob(292, 140, p, d=14, val=0.4, label="phones", ticks=False, **K))
    # keys
    ky = BD - 10 - 90
    o.append(f'<rect x="38" y="{ky-2}" width="274" height="92" rx="1.5" fill="#0b0b0b"/>')
    o.append(keyboard(41.5, ky, p, night=night))
    o.append(f'<rect x="4" y="{ky+12}" width="31" height="66" rx="2" fill="#0b0b0b"/>')
    o.append(wheels(4, ky + 15, p, night=night))
    return "".join(o)


ELEV = 40  # viewing elevation (deg): a dish tilted 50 deg is seen face-on
FS = math.sin(math.radians(ELEV))   # plan foreshortening
FV = math.cos(math.radians(ELEV))   # vertical foreshortening
ARM = 80


def player_view(p, night=False, light_on=True):
    o = []
    # base top plane, foreshortened
    o.append(f'<g transform="scale(1,{FS:.4f})">{base_plan(p, night)}</g>')
    # base front face
    st, _ = stack_side(0, BD * FS + 40 * FV, 315, [(40 * FV / 12, "walnut")] * 12)
    o.append(st if not night else f'<rect x="0" y="{BD*FS:.1f}" width="315" height="{40*FV:.1f}" fill="#050505"/>')
    # fork arms (vertical, rising from the pivots)
    py = (CY + RC) * FS
    ay = py - ARM * FV
    for sx in (-1, 1):
        x = CX + sx * 84
        o.append(f'<rect x="{x-4}" y="{ay-4:.1f}" width="8" height="{py-ay+4:.1f}" rx="3" '
                 f'fill="{"#5b3a26" if not night else "#0a0a0a"}" filter="{"url(#grainv)" if not night else ""}"/>')
        o.append(f'<circle cx="{x}" cy="{ay:.1f}" r="3.4" fill="url(#brassg)"/>')
        o.append(f'<circle cx="{x}" cy="{py:.1f}" r="3.0" fill="url(#brassg)"/>')
    # dish: thickness hint then face
    o.append(f'<circle cx="{CX}" cy="{ay+3:.1f}" r="{R}" fill="{"#3b2618" if not night else "#050505"}"/>')
    o.append(f'<g transform="translate({CX},{ay:.1f})" filter="url(#shbig)">{dish_face(p, night, light_on)}</g>')
    return "".join(o), BD * FS + 40 * FV, ay - R


def sheet(p=p0, fname="dish-mock"):
    W, H = 3800, 3300
    b = []
    b.append(title_block(90, 140, "DISH", "Sauce · a control dish on a fold-flat fork (radio telescope × furniture)",
                         ["A circle cut out of the panel becomes the dish. Signal flow spirals inward to the cutoff ring;",
                          "the speaker plays through the bullseye. Rule: you TURN things on the dish, you SLIDE and FLIP",
                          "things on the wings. Fork swings up 80 mm, dish tilts 50°; both fold flat for carry."],
                         "Look shown: Proof — white panel, walnut stack + fork, black caps, red cutoff ring", 30))
    b.append(placeholder_note(90, 520))
    s = 6.6
    pv, hbot, htop = player_view(p)
    X0, Y0 = 110, 620 + int(-htop * s)
    b.append(view_label(90, 600, "PLAYING — from the player's eye (40° above; the dish is seen face-on). 1 mm = 6.6 px"))
    b.append(G(X0, Y0, s, pv))
    b.append(dim_h(X0, X0 + 315 * s, Y0 + hbot * s + 60, "315 mm"))
    RX = 2400
    # face-on dish detail
    b.append(view_label(RX, 600, "DISH FACE — Ø 155 mm (1 mm = 7.5 px)"))
    b.append(G(RX + 80 + R * 7.5, 660 + R * 7.5, 7.5, dish_face(p)))
    b.append(para(RX, 660 + 2 * R * 7.5 + 70, [
        ("Reading the dish", 700),
        "Outer ring, clockwise from 9 o'clock: tune, mod mix, then the three",
        "oscillators (range + wave pairs) across the top, then the mixer down",
        "the right. Inner ring: freq 2/3 under their oscillators; glide, emphasis",
        "and contour at 7–9 o'clock, where the left hand arrives. Centre: the",
        "red cutoff ring around the speaker. All legends sit upright; only the",
        "section names follow the rim.",
        "",
        ("“Not in control”: the bullseye glows", 700),
        "One amber ring of light inside the cutoff ring (shown lit).",
    ], 24, "#333"))
    # side views
    sy = 2560
    b.append(view_label(RX, 2280, "SIDE — playing / carry (1 mm = 2.6 px)"))
    ss = 2.6
    se = []
    st, top = stack_side(0, 0, BD, [(40 / 13, "walnut")] * 13)
    se.append(st)
    pvx = BD - (CY + RC)   # pivot x from the front (player at left)
    se.append(f'<rect x="{pvx-3}" y="{top-ARM}" width="6" height="{ARM}" fill="#5b3a26"/>')
    se.append(f'<g transform="translate({pvx},{top-ARM}) rotate(-50)"><rect x="{-R}" y="-20" width="{2*R}" height="20" rx="3" fill="{p["panel"]}" stroke="#5b3a26" stroke-width="1.6"/>'
              f'<rect x="-20" y="-34" width="40" height="14" rx="2" fill="{p["hero"]}"/></g>')
    se.append(f'<line x1="-10" y1="0" x2="{BD+10}" y2="0" stroke="#999" stroke-width="0.8"/>')
    b.append(G(RX + 40, sy, ss, "".join(se)))
    b.append(txt(RX + 30, sy + 36, "← player", 22, "#777", anchor="start", font=UI_FONT))
    sc = []
    st2, top2 = stack_side(0, 0, BD, [(40 / 13, "walnut")] * 13)
    sc.append(st2)
    sc.append(f'<rect x="{BD-(CY+RC)}" y="{top2-10}" width="{2*RC}" height="10" fill="#5b3a26" filter="url(#grainf)"/>')
    b.append(G(RX + 40, 3020, ss, "".join(sc)))
    b.append(dim_v(RX + 40 + BD * ss + 20, 3020, 3020 - 50 * ss, "≈ 50 mm carry"))
    b.append(dim_h(RX + 40, RX + 40 + BD * ss, 3060, f"{BD} mm"))
    b.append(para(RX + 820, 2330, ["Fork pivots at the recess's", "front edge, so the dish rises", "toward you, not away.",
                                   "Dish edge clears the base", "by ≈ 20 mm at 50°."], 22, "#444"))
    # closed / carry top view: dish face-down, its back is the second canvas
    b.append(view_label(90, 2560 + 120, "CARRY — top (dish face-down, flush; its back is a second canvas)"))
    ct = [base_plan(p)]
    ct.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="#16213a" stroke="#5b3a26" stroke-width="2"/>')
    import random
    rnd = random.Random(11)
    for _ in range(70):
        a = rnd.uniform(0, 6.283); rr = R * math.sqrt(rnd.uniform(0, 0.95))
        ct.append(f'<circle cx="{CX+rr*math.cos(a):.1f}" cy="{CY+rr*math.sin(a):.1f}" r="{rnd.uniform(0.3,1.1):.2f}" fill="#f4e8c8"/>')
    ct.append(txt(CX, CY + 4, "[ your painting ]", 7, "#f4e8c8", weight=700))
    for sx in (-1, 1):
        ct.append(f'<rect x="{CX+sx*84-3.5}" y="{CY-1}" width="7" height="{RC+1}" rx="2" fill="#5b3a26"/>')
    b.append(G(110, 2720, 1.75, "".join(ct)))
    nv, nb, nt = player_view(p, night=True)
    b.append(view_label(1000, 2680, "LIGHTS OFF"))
    b.append(f'<rect x="1000" y="2700" width="{int(315*2.2)+40}" height="{int((nb-nt)*2.2)+40}" rx="10" fill="#050605"/>')
    b.append(G(1020, 2720 + int(-nt * 2.2), 2.2, nv))
    open(OUT + fname + ".svg", "w").write(svg_doc(W, H, "".join(b), p))
    return OUT + fname + ".svg"


if __name__ == "__main__":
    print(sheet())
