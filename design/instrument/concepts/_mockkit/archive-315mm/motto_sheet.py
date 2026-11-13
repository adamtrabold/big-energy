"""MOTTO sheet (sauce): a tiny harpsichord. Spine left, S-bentside right, lid hinged at the tail
stands behind as a painted backdrop + sound reflector. Reverse-colour keys, finger-dial ranges."""
import math
from kit import *
from common_views import *

OUT = "/home/claude/model-d/design/instrument/concepts/motto/"
D = 255          # depth at the spine (front y = D)
CHEEK_Y = 64     # where the S-bentside meets the right cheek
TAIL_X = 150     # straight tail (hinge) length, back-left

P = dict(PAL["desk"])
P.update(name="Motto (Desk panel + walnut)", body_top="#5b3a26", body_mat="walnut", base_mat="walnut",
         nat="#efe7d6", nat_edge="#c9bea6", sharp="#2a2320", sharp_hi="#3d332d",
         hero="#c8341f", hero_hi="#e2624b", hero_lo="#8d2112", signal="#c8341f", led="#c8341f",
         grille="rose", hole="#3a2a20", bg="#efe9df")


def outline_path(inset=0.0):
    i = inset
    return (f"M{i},{D-i} L{i},{i} L{TAIL_X},{i} "
            f"C{TAIL_X+70},{i} {TAIL_X+100},{CHEEK_Y-2+i*0.5} {315-i},{CHEEK_Y+i} "
            f"L{315-i},{D-i} Z")


def panel(p, night=False, light_on=True):
    o = []
    K = dict(p=p, night=night)
    # section rules (gold) and the "water" line
    if not night:
        o.append(f'<path d="M70,14 L70,148" stroke="{p["gold"]}" stroke-width="0.45" fill="none"/>')
        o.append(f'<path d="M176,22 L176,148" stroke="{p["gold"]}" stroke-width="0.45" fill="none"/>')
        o.append(f'<path d="M238,52 L238,148" stroke="{p["gold"]}" stroke-width="0.45" fill="none"/>')
        # current: flows from oscillators, under the mixer, along the bentside back to the rose in the tail
        o.append(f'<path d="M168,150 C200,150 230,150 312,150" stroke="{p["gold"]}" stroke-width="0.45" fill="none" opacity="0.8"/>')
        o.append(f'<path d="{outline_path(6)}" stroke="{p["gold"]}" stroke-width="0.35" fill="none" stroke-dasharray="1.2 1.2" opacity="0.7"/>')
        o.append(txt(34, 70, "", 2.8, p["gold"]))
    # tail: the rose (speaker)
    if night:
        o.append('<circle cx="34" cy="36" r="24" fill="#070707"/>')
    else:
        o.append(grille(34, 36, 23, p, "rose"))
    # left hand: hero + arc
    o.append(hero(36, 124, p, night=night, d=38, label="cutoff", lab_dy=25.5))
    for (x, y, lab, v) in ((36, 93, "emphasis", 0.6), (14.5, 102.5, "glide", 0.2), (57.5, 102.5, "contour", 0.45)):
        o.append(knob(x, y, p, val=v, night=night, label=lab, lab_dy=-10.2, ticks=False))
    o.append(button(61, 140, p, d=7, label=None, night=night))
    if not night:
        o.append(txt(61, 148.5, "hold", 2.4, p["silk"]))
    # controllers row (back)
    o.append(knob(84, 22, p, val=0.5, label="tune", night=night))
    o.append(knob(106, 22, p, val=0.3, label="mod mix", night=night))
    for i, (lab, up) in enumerate((("osc mod", True), ("filt mod", False), ("osc3 ctl", False), ("glide", True))):
        o.append(toggle(124 + i * 13, 19, p, up, lab, night=night, label_size=2.1))
    # oscillator rows: finger dial (range) · wave · freq
    for r, y in enumerate((56, 88, 120)):
        o.append(dial(86, y, p, pos=[2, 2, 3][r], night=night))
        o.append(rotary(119, y, p, "wave", pos=[2, 3, 5][r], night=night))
        if r:
            o.append(knob(146, y, p, val=[0.5, 0.58][r - 1], night=night, label=None))
        if not night:
            o.append(txt(164, y + 4, str(r + 1), 9, p["silk"], weight=700))
            if r == 0:
                o.append(txt(146, y + 1, "ref", 2.4, p["silk"], style="opacity:.55"))
    if not night:
        o.append(txt(86, 142, "range", 2.5, p["silk"]))
        o.append(txt(119, 142, "wave", 2.5, p["silk"]))
        o.append(txt(146, 142, "freq", 2.5, p["silk"]))
    # mixer column
    for k, (lab, v, on) in enumerate((("osc 1", .8, 1), ("osc 2", .6, 1), ("osc 3", .5, 1), ("ext", 0, 0), ("noise", .15, 0))):
        y = 44 + k * 24
        o.append(knob(190, y, p, val=v, night=night, ticks=False))
        o.append(toggle(206, y, p, bool(on), None, night=night))
        if not night:
            o.append(txt(181, y - 9.6, lab, 2.5, p["silk"], anchor="start"))
    o.append(toggle(222, 92, p, False, "feedbk", night=night, lab_dy=-6.5, label_size=2.0))
    o.append(toggle(222, 116, p, True, "line/mod", night=night, lab_dy=-6.5, label_size=2.0))
    o.append(toggle(222, 140, p, True, "wh/pk", night=night, lab_dy=-6.5, label_size=2.0))
    # contours (deep enough below the cheek line)
    fv = [0.15, 0.55, 0.7, 0.1, 0.45, 0.85]
    for i, x in enumerate((245, 257, 269, 282, 294, 306)):
        s, _ = fader(x, 74, p, 30, fv[i], label=["a", "d", "s"][i % 3], night=night)
        o.append(s)
    if not night:
        o.append(txt(259, 70, "filter", 2.6, p["gold"], weight=700))
        o.append(txt(297, 70, "loudness", 2.6, p["gold"], weight=700))
    # bottom row on the right: kbd toggles, decay, volume, phones, tune, status, section pips
    o.append(toggle(246, 136, p, True, "kbd1", night=night, lab_dy=-6.3, label_size=2.0))
    o.append(toggle(256, 136, p, False, "kbd2", night=night, lab_dy=-6.3, label_size=2.0))
    o.append(toggle(266, 136, p, True, "decay", night=night, lab_dy=-6.3, label_size=2.0))
    o.append(knob(281, 136, p, val=0.6, d=12, night=night, ticks=False, label=None))
    o.append(knob(297, 136, p, val=0.4, d=12, night=night, ticks=False, label=None))
    if not night:
        o.append(txt(281, 128.4, "vol", 2.2, p["silk"]))
        o.append(txt(297, 128.4, "phones", 2.2, p["silk"]))
    o.append(button(310, 140, p, d=5.5, night=night))
    o.append(led(310, 131, p["led"], 1.1))
    if not night:
        o.append(txt(310, 148.8, "tune", 2.0, p["silk"]))
    # V-c: section pips (amber) on the rules: controllers, oscillators, mixer, filter, loudness
    pips = [(95, 8.5, False), (70, 150, light_on), (176, 150, False), (238, 150, light_on), (279, 64, False)]
    for x, y, on in pips:
        o.append(led(x, y, "#ffb020", 0.8, on=on))
    return "".join(o)


def dial(cx, cy, p, pos=2, night=False, d=28):
    """Telephone finger dial for RANGE: 6 holes, detented (not spring-return). The hole under the
    fixed finger-stop (at 4 o'clock) is the current range."""
    r = d / 2
    o = []
    labs = ["LO", "32", "16", "8", "4", "2"]
    stop_ang = 128
    rot = (pos - 0) * 0  # dial rotation by detent
    base = stop_ang - pos * 42  # angle of hole 0 so that hole `pos` sits at the stop
    if not night:
        o.append(f'<g filter="url(#sh)"><circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#capg)"/></g>')
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r*0.42}" fill="{p["panel"]}" stroke="{p["gold"]}" stroke-width="0.4"/>')
    else:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#0c0c0c"/>')
    for i in range(6):
        a = base - i * 42
        x, y = pol(cx, cy, r * 0.7, a)
        if night:
            if i == pos:
                o.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2.6" fill="none" stroke="#b9ff9e" stroke-width="0.5" filter="url(#glow)"/>')
            continue
        o.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2.85" fill="{p["panel"]}" stroke="#000" stroke-width="0.3"/>')
        o.append(txt(x, y + 0.8, labs[i], 2.0, p["silk"] if i != pos else p["ptr"], weight=700 if i == pos else 400))
    # fixed finger stop
    x0, y0 = pol(cx, cy, r - 0.5, stop_ang + 8)
    x1, y1 = pol(cx, cy, r + 3.2, stop_ang + 8)
    o.append(f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" stroke="{p["gold"] if not night else "#b9ff9e"}" stroke-width="1.6" stroke-linecap="round"/>')
    return "".join(o)


def body_top(p, night=False, light_on=True):
    o = [f'<g filter="url(#shbig)"><path d="{outline_path()}" {body_fill(p) if not night else "fill=\"#0a0a0a\""}/></g>']
    # panel PCB: outline inset 5, cut at the key well
    o.append(f'<clipPath id="pc"><path d="{outline_path(5)}"/></clipPath>')
    o.append(f'<rect x="0" y="0" width="315" height="153" fill="{"#050505" if night else p["panel"]}" clip-path="url(#pc)"/>')
    o.append(panel(p, night, light_on))
    # keys
    ky = D - 10 - 90
    o.append(f'<rect x="38" y="{ky-2}" width="274" height="92" rx="1.5" fill="#0b0b0b"/>')
    o.append(keyboard(41.5, ky, p, reverse=True, night=night))
    o.append(f'<rect x="4" y="{ky+12}" width="31" height="66" rx="2" fill="#0b0b0b"/>')
    o.append(wheels(4, ky + 15, p, night=night))
    # tail hinge (brass piano hinge along the straight tail)
    o.append(f'<rect x="6" y="-2.5" width="{TAIL_X-12}" height="3" fill="url(#brassg)"/>')
    return "".join(o)


def painting(w=315):
    """Placeholder lid painting, drawn in lid-local coords (0..315 x 0..255, top = front edge)."""
    return f"""
<defs>
 <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#1f2a4a"/><stop offset="0.45" stop-color="#6b4f7a"/>
  <stop offset="0.75" stop-color="#e08a5a"/><stop offset="1" stop-color="#f2c27a"/></linearGradient>
 <filter id="paint"><feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" seed="5"/>
  <feDisplacementMap in="SourceGraphic" scale="6"/></filter>
 <filter id="canvas"><feTurbulence type="fractalNoise" baseFrequency="0.7" numOctaves="2" seed="1" result="n"/>
  <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.12 0" result="na"/>
  <feComposite in="na" in2="SourceGraphic" operator="in" result="m"/><feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="m"/></feMerge></filter>
</defs>
<g filter="url(#canvas)">
 <rect width="315" height="255" fill="url(#sky)"/>
 <circle cx="205" cy="168" r="26" fill="#ffd69a" opacity="0.9" filter="url(#paint)"/>
 <path d="M0,180 C60,150 110,175 160,160 C210,146 260,170 315,150 L315,255 L0,255 Z" fill="#3c2f4f" filter="url(#paint)"/>
 <path d="M0,205 C70,185 120,210 190,195 C240,186 280,200 315,192 L315,255 L0,255 Z" fill="#26203a" filter="url(#paint)"/>
 <path d="M0,232 C80,220 150,236 315,222 L315,255 L0,255 Z" fill="#17132a" filter="url(#paint)"/>
 <path d="M40,40 C120,22 200,22 280,40 L272,62 C200,46 120,46 48,62 Z" fill="#efe3c6" opacity="0.92" filter="url(#paint)"/>
 <text x="160" y="52" font-family="{LEG_FONT}" font-size="12" fill="#5a2a1e" text-anchor="middle" font-weight="700">[ your motto here ]</text>
</g>"""


def sheet(p=P, fname="motto-mock"):
    W, H = 3800, 3560
    b = []
    b.append(title_block(90, 140, "MOTTO", "Sauce · a tiny harpsichord with a painted lid",
                         ["Spine left, S-bentside right (true harpsichord hand). Reverse-colour keys: ebony naturals, bone sharps.",
                          "The lid hinges at the tail and stands up behind the panel: your painting faces you and the camera,",
                          "and the up-firing speaker (the rose) bounces off it toward you. Ranges are telephone finger dials."],
                         f"Look shown: walnut stack, black panel, gold rules, vermilion cutoff · lid painting is a placeholder", 30))
    b.append(placeholder_note(90, 520))
    s = 7.0
    X0, Y0 = 90, 640
    b.append(view_label(X0, Y0 - 50, "PLAYING — top view, real proportions (1 mm = 7 px). Lid stands behind (not shown here)."))
    b.append(G(X0, Y0, s, body_top(p)))
    b.append(dim_h(X0, X0 + 315 * s, Y0 + D * s + 60, "315 mm"))
    b.append(dim_v(X0 + 315 * s + 30, Y0, Y0 + D * s, f"{D}", side=1))
    b.append(dim_v(X0 + 315 * s + 40 + 0, Y0 + CHEEK_Y * s, Y0 + D * s, "", side=1) if False else "")
    # callouts
    b.append(callout(X0 + 34 * s, Y0 + 36 * s, X0 - 0, Y0 - 6, [], 22, dot=False) if False else "")
    # front elevation with lid standing
    RX = 2470
    b.append(view_label(RX, 600, "FROM THE PLAYER — lid up (1 mm = 3.6 px)"))
    fs = 3.6
    fx, fy = RX + 30, 1700
    fe = []
    # lid: standing, leaning back 10 deg -> projected height ~ D*cos10
    lh = D * math.cos(math.radians(10))
    fe.append(f'<g transform="translate(0,{-45 - lh:.1f}) scale(1,{math.cos(math.radians(10)):.4f})">'
              f'<clipPath id="lidclip"><path d="M0,0 L315,0 L315,{D-CHEEK_Y} C{TAIL_X+100},{D-CHEEK_Y+2} {TAIL_X+70},{D} {TAIL_X},{D} L0,{D} Z"/></clipPath>'
              f'<g clip-path="url(#lidclip)">{painting()}</g>'
              f'<path d="M0,0 L315,0 L315,{D-CHEEK_Y} C{TAIL_X+100},{D-CHEEK_Y+2} {TAIL_X+70},{D} {TAIL_X},{D} L0,{D} Z" fill="none" stroke="#3b2618" stroke-width="3"/></g>')
    # body front: walnut stack 45 tall with keys in front
    st, top = stack_side(0, 0, 315, [(3, "walnut")] * 15)
    fe.append(st)
    fe.append(f'<rect x="41" y="{-30}" width="271" height="10" fill="#2a2320"/>')
    for i in range(15):
        fe.append(f'<rect x="{41.5+i*18+0.4:.1f}" y="-30" width="17.2" height="10" fill="#2a2320" stroke="#000" stroke-width="0.3"/>')
    fe.append(f'<line x1="-20" y1="0" x2="335" y2="0" stroke="#999" stroke-width="0.6"/>')
    b.append(G(fx, fy, fs, "".join(fe)))
    b.append(txt(fx + 157 * fs, fy + 70, "PLACEHOLDER painting — this is the owner's canvas (≈ 315 × 255 mm)", 22, "#9a5b2a", font=UI_FONT, weight=600))
    b.append(dim_v(fx + 330 * fs, fy, fy - (45 + lh) * fs, f"≈ {45+lh:.0f} mm lid up"))
    # side elevation (from the right)
    ss = 2.4
    b.append(view_label(RX, 1880, "SIDE (from the right) — playing, then closed (1 mm = 2.4 px)"))
    sx, sy = RX + 60, 2640
    se = []
    st2, t2 = stack_side(0, 0, D, [(3, "walnut")] * 15)
    se.append(st2)
    se.append(f'<g transform="translate({D},{t2}) rotate(-80)"><rect x="0" y="0" width="{D}" height="8" fill="#5b3a26" filter="url(#grainf)"/></g>')
    se.append(f'<line x1="{D-70}" y1="{t2}" x2="{D+10}" y2="{t2-130}" stroke="#b8933f" stroke-width="2"/>')
    se.append(f'<line x1="-10" y1="0" x2="{D+70}" y2="0" stroke="#999" stroke-width="0.8"/>')
    b.append(G(sx, sy, ss, "".join(se)))
    b.append(txt(sx - 10, sy + 36, "← player", 22, "#777", anchor="start", font=UI_FONT))
    b.append(para(RX + 820, sy - 420, ["Captive brass stay holds", "the lid at 100°", "(10° past upright).", "", "Speaker → lid → you."], 22, "#444"))
    sy2 = 2820
    sc = []
    st3, t3 = stack_side(0, 0, D, [(3, "walnut")] * 15)
    sc.append(st3)
    sc.append(f'<rect x="0" y="{t3-8}" width="{D}" height="8" fill="#5b3a26" filter="url(#grainf)"/>')
    b.append(G(sx, sy2, ss, "".join(sc)))
    b.append(dim_v(sx + D * ss + 20, sy2, sy2 - 53 * ss, "≈ 53 mm closed"))
    b.append(dim_h(sx, sx + D * ss, sy2 + 40, f"{D} mm"))
    # closed top
    b.append(view_label(RX, 2960, "CLOSED — top (lid outside, inlaid wordmark)"))
    ct = [f'<g filter="url(#shbig)"><path d="{outline_path()}" fill="#5b3a26" filter="url(#grainf)"/></g>',
          f'<path d="{outline_path(4)}" fill="none" stroke="#c29a45" stroke-width="0.7"/>',
          txt(110, 140, NAME, 16, "#e9dcc0", weight=700)]
    b.append(G(RX + 30, 3000, 2.0, "".join(ct)))
    # night inset
    b.append(view_label(90, 2620 + 300 + 40, ""))
    nv = body_top(p, night=True)
    b.append(view_label(X0, Y0 + D * s + 150, "LIGHTS OFF"))
    b.append(f'<rect x="{X0}" y="{Y0 + D*s + 170}" width="{int(315*2.0)+40}" height="{int(D*2.0)+40}" rx="10" fill="#050605"/>')
    b.append(G(X0 + 20, Y0 + D * s + 190, 2.0, nv))
    b.append(para(X0 + 720, Y0 + D * s + 210, [
        ("“Not in control”: five section pips.", 700),
        "Tiny amber pips sit on the gold rules, one per section",
        "(controllers, oscillators, mixer, filter, loudness).",
        "Lit = a knob in that section isn't in control.",
        "Shown: oscillators + filter lit.",
        "",
        ("Finger dials (range).", 700),
        "Detented, not spring-return: the hole under the gold",
        "finger-stop is the current range. Holes are findable",
        "by touch in the dark; the selected one glows.",
    ], 24, "#333"))
    open(OUT + fname + ".svg", "w").write(svg_doc(W, H, "".join(b), p))
    return OUT + fname + ".svg"


if __name__ == "__main__":
    print(sheet())
