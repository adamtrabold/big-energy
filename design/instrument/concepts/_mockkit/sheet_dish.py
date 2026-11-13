"""DISH round-2 sheet + exploded. Base 285 x 188 x 38; dish Ø112 on a fold-flat fork.
Visual's geometry change (to systems): the fork pivots at the well's REAR edge and leans 70° toward the player.
With the round-1 front pivot, a 50° dish hangs its lower rim 36 mm forward, 7 mm above the sharps."""
import math
from r2s_common import *

BW, BD = 292, 188      # F3: 22 mm bend/mod zone (3 mm edge margins, as systems)
SX = (BW - 285) / 2    # upper part (wings, well, dish) re-centred
WC = (142.5, 62.0)      # well centre (y from the rear)
WR = 58.0
ARM = 58.0
FORK = 70.0             # fork angle from horizontal, leaning toward the player
TILT = 50.0
SPK = (142.5, 66.0)     # speaker centre: >= 60 mm from the sharps switch row (y 137)
EMP = (63.5, 52.0)      # D1: emphasis, wing inner edge, 6 mm clear of the raised fork's left arm (x 79.5)
T_BASE, SINK, CAP = 38.0, 8.0, 12.0
_tipz = T_BASE + ARM * math.sin(math.radians(70.0))            # axle height above the table
CUT_PLAN_Y = 4 + ARM * math.cos(math.radians(70.0)) + CAP * math.sin(math.radians(50.0))
_cutz = _tipz + CAP * math.cos(math.radians(50.0))
_empz = T_BASE - SINK + CAP
SPAN_PLAN = math.hypot(142.5 - EMP[0], EMP[1] - CUT_PLAN_Y)
SPAN3D = math.sqrt(SPAN_PLAN ** 2 + (_cutz - _empz) ** 2)


def dish_face(p, night=False, bull_on=True):
    """Dish face in local mm 0..112, centre (56,56), as the player sees it (face-on)."""
    c = 56
    o = [f'<circle cx="{c}" cy="{c}" r="56" fill="{"#060606" if night else p["panel"]}" stroke="{"#222" if night else p["gold"]}" stroke-width="0.8"/>']
    if not night:
        o.append(f'<circle cx="{c}" cy="{c}" r="53.6" fill="none" stroke="{p["gold"]}" stroke-width="0.3"/>')
    ring = [("glide", "k", .25), ("tune", "k", .5), ("range 1", "r", 2), ("range 2", "r", 2), ("freq 2", "k", .5),
            ("range 3", "r", 3), ("freq 3", "k", .58), ("f · a", "k", .15), ("f · d", "k", .55), ("f · s", "k", .7),
            ("l · a", "k", .1), ("l · d", "k", .45), ("l · s", "k", .85)]
    for i, (name, kind, v) in enumerate(ring):
        a = 270 + i * 360 / 13
        x, y = pol(c, c, 38, a)
        if kind == "k":
            o.append(Kn(x, y, p, v, None, night, own=True))
        else:
            o.append(Rot(x, y, p, "range", v, night, numerals=False))
        if not night:
            aa = a % 360
            if 90 < aa < 270:      # bottom half: flip so it reads upright
                lx, ly = pol(c, c, 49.0, a)
                o.append(txt(lx, ly, name, 3.4, p["silk"], rot=aa - 180, style="dominant-baseline:hanging"))
            else:
                lx, ly = pol(c, c, 49.6, a)
                o.append(txt(lx, ly, name, 3.4, p["silk"], rot=aa))
    # bullseye light ring + hero
    if bull_on:
        o.append(f'<circle cx="{c}" cy="{c}" r="16.6" fill="none" stroke="{OWN_C}" stroke-width="2.0" filter="url(#glow)" opacity="0.95"/>')
    elif not night:
        o.append(f'<circle cx="{c}" cy="{c}" r="16.6" fill="none" stroke="#c9c2b3" stroke-width="2.0"/>')
    o.append(hero(c, c, p, d=26, night=night, label=None))
    if not night:
        o.append(lab(c, c + 23.4, "cutoff", p, 4.2, weight=700))
    return "".join(o)


def wings(p, night=False):
    o = []
    for (x0, x1) in ((3, 78), (207, 282)):
        o.append(f'<rect x="{x0-1}" y="3" width="{x1-x0+2}" height="118" rx="2.5" fill="#000" opacity="0.55"/>')
        o.append(f'<rect x="{x0}" y="4" width="{x1-x0}" height="116" rx="2" fill="{"#050505" if night else p["panel"]}"/>')
    if not night:
        o.append(lab(40.5, 8.6, "set the tone", p, HS, p["gold"], 700))
        o.append(lab(244.5, 8.6, "waveforms · mixer · out", p, HS, p["gold"], 700))
    # left wing
    o.append(Kn(14, 20, p, .3, "mod mix", night))
    o.append(Tg(37, 19, p, True, "osc mod", night))
    o.append(Tg(60, 19, p, False, "filt mod", night))
    o.append(Tg(14, 51, p, False, "osc 3 ctl", night, size=3.3))
    o.append(Kn(37, 52, p, .45, "amount", night))
    o.append(Kn(EMP[0], EMP[1], p, .62, None, night, d=20))      # D1: second-largest cap, at the inner edge
    if not night:
        o.append(lab(EMP[0], EMP[1] + 15.2, "emphasis", p, 4.0, weight=700))
    o.append(Tg(14, 80, p, True, "glide on", night, size=3.3))
    o.append(Tg(37, 80, p, False, "decay", night))
    o.append(Bt(12, 104, p, 7, "hold", night, lab_dy=10))
    o.append(Bt(30, 104, p, 7, "tune", night, lab_dy=10))
    o.append(led(21, 96, p["led"], 1.0))
    o.append(Tg(50, 103, p, True, "kbd 1", night, size=3.3, lab_dy=8.8))
    o.append(Tg(68, 103, p, False, "kbd 2", night, size=3.3, lab_dy=8.8))
    # right wing
    for i, x in enumerate((218, 244, 270)):
        o.append(Rot(x, 21, p, "wave", [2, 3, 5][i], night))
    for k, (l_, v) in enumerate((("osc 1", .8), ("osc 2", .6), ("osc 3", .5))):
        x = 216 + k * 24
        o.append(Kn(x, 47, p, v, l_, night))
        o.append(Tg(x + 11, 46, p, True, None, night))
    o.append(Kn(216, 71, p, 0.0, "ext", night)); o.append(Tg(227, 70, p, False, None, night))
    o.append(Kn(240, 71, p, .15, "noise", night)); o.append(Tg(251, 70, p, False, None, night))
    o.append(Tg(270, 70, p, False, "feedbk", night, size=3.3))
    o.append(Tg(214, 95, p, True, "wh/pk", night, size=3.3))
    o.append(Tg(232, 95, p, False, "pad", night, size=3.3))
    o.append(Kn(252, 96, p, .6, "volume", night, lab_dy=9.6))
    o.append(Kn(272, 96, p, .4, "phones", night, lab_dy=9.6))
    return "".join(o)


def dish_top(p, night=False, bull_on=True, stowed=False, mod_pip=False, span=False):
    o = [f'<g filter="url(#shbig)"><rect x="0" y="0" width="{BW}" height="{BD}" rx="5" {body_fill(p) if not night else "fill=\"#0a0a0a\""}/></g>']
    # keys + left zone (full width), then the upper part shifted by SX
    o.append(key_well(2.6, 127.1, ZW + 0.8, 55.8, night))
    o.append(bendmod_lead(3.0, 127.5, p, night, h=55, pip=mod_pip))
    if not night:
        o.append(txt(3 + ZW / 2, 125.8, "mod", 2.4, "#e9dccb"))
        o.append(txt(3 + ZW / 2, 186.0, "bend", 2.4, "#e9dccb"))
    o.append(keys_pegs(25.6, 123, p, night))
    u = []
    u.append(wings(p, night))
    # fork channels + well
    for x in (79.5, 201.5):
        u.append(f'<rect x="{x}" y="4" width="4" height="62" rx="1.5" fill="#111"/>')
    u.append(f'<circle cx="{WC[0]}" cy="{WC[1]}" r="{WR}" fill="#0c0c0c"/>')
    if not night:
        u.append(grille(SPK[0], SPK[1], 19.5, p, "bull"))
    if stowed:
        u.append(f'<circle cx="{WC[0]}" cy="{WC[1]}" r="56" fill="{"#111" if night else "#3b2a1c"}" filter="url(#grainf)"/>')
        o.append(G(SX, 0, 1, "".join(u)))
        return "".join(o)
    # fork arms (foreshortened) + dish ellipse
    ty = 4 + ARM * math.cos(math.radians(FORK))
    for x in (81.5, 203.5):
        u.append(f'<rect x="{x-2}" y="4" width="4" height="{ty-4+2:.1f}" rx="1.5" fill="url(#brassg)"/>')
    u.append(f'<rect x="81.5" y="12.2" width="122" height="2.2" rx="1" fill="url(#brassg)" opacity="0.85"/>')   # D2 cross-tie
    k = math.cos(math.radians(TILT))
    u.append(f'<ellipse cx="{WC[0]+3}" cy="{ty+40:.1f}" rx="55" ry="{56*k:.1f}" fill="#000" opacity="0.35"/>')
    u.append(f'<g transform="translate({WC[0]},{ty:.2f}) scale(1,{k:.3f}) translate(-56,-56)">{dish_face(p, night, bull_on)}</g>')
    u.append(f'<rect x="{WC[0]-58}" y="{ty-1.6:.1f}" width="116" height="3.2" rx="1.6" fill="url(#brassg)" opacity="0.9"/>')
    if span and not night:
        # D1: the left hand spanning emphasis and cutoff (plan), measured in 3D below
        ex, ey = EMP
        cx_, cy_ = WC[0], CUT_PLAN_Y
        u.append(f'<path d="M{ex},{ey} Q{(ex+cx_)/2-6},{(ey+cy_)/2+16} {cx_-4},{cy_+6}" fill="none" stroke="#2b6cb0" stroke-width="5" stroke-linecap="round" opacity="0.22"/>')
        u.append(f'<path d="M{ex},{ey} Q{(ex+cx_)/2-6},{(ey+cy_)/2+16} {cx_-4},{cy_+6}" fill="none" stroke="#2b6cb0" stroke-width="0.5" stroke-dasharray="1.6 1.2"/>')
        u.append(f'<circle cx="{ex}" cy="{ey}" r="2.4" fill="#2b6cb0" opacity="0.55"/><circle cx="{cx_-4}" cy="{cy_+6}" r="2.4" fill="#2b6cb0" opacity="0.55"/>')
        u.append(txt((ex + cx_) / 2 - 22, (ey + cy_) / 2 + 26, f"left hand ≈ {SPAN3D:.0f} mm", 3.2, "#1f4f87", anchor="start", font=UI_FONT, weight=700))
    o.append(G(SX, 0, 1, "".join(u)))
    return "".join(o)


def dish_side(p, raised=True, ghost=True):
    """Side from the right, x = depth from the front, y up negative; base top at -38."""
    T = 38
    o = [part(0, -T, BD, T, p["body_top"], "#222", 0.3, 3, 'filter="url(#grainf)"' if p["body_mat"] == "walnut" else "")]
    wf, wr = BD - 120, BD - 4           # well front/rear edges (from the front)
    o.append(f'<rect x="{wf}" y="{-T}" width="{wr-wf}" height="23" fill="#151515" opacity="0.8"/>')
    o.append(part(BD - SPK[1] - 20, -T + 23, 40, 9, "#444", "#111", 0.3, 2))
    o.append(capsil(BD - SPK[1] - 20, -T + 23, 40, 0.0, "#000"))
    # pegs
    for x in (25, 51):
        o.append(capsil(x - 7, -T, 14 if x == 25 else 12, 7, "#d9b98a" if x == 25 else "#3a2618", 3))
    # wing caps (low)
    for x in (70, 100):
        o.append(capsil(BD - x - 6, -T + 8, 12, 8, p["cap"], 2))
    if raised:
        px, pz = wr, -T
        tx = px - ARM * math.cos(math.radians(FORK)); tz = pz - ARM * math.sin(math.radians(FORK))
        o.append(f'<line x1="{px}" y1="{pz}" x2="{tx:.1f}" y2="{tz:.1f}" stroke="#b8933f" stroke-width="3"/>')
        o.append(f'<circle cx="{px}" cy="{pz}" r="2.2" fill="url(#brassg)"/><circle cx="{tx:.1f}" cy="{tz:.1f}" r="2.2" fill="url(#brassg)"/>')
        # dish: 112 long, 11 body + 10 caps toward the player-up side
        o.append(f'<g transform="translate({tx:.1f},{tz:.1f}) rotate({-TILT})">'
                 f'{part(-56, 0, 112, 11, "#2a2a2a", "#111", 0.3, 3)}{part(-56, -1.6, 112, 1.6, p["panel"], "#111", 0.2, 0)}'
                 f'{capsil(-13, -1.6, 26, 12, p["hero"], 3)}{capsil(-46, -1.6, 12, 10, p["cap"], 2)}{capsil(34, -1.6, 12, 10, p["cap"], 2)}</g>')
        # reach line
        o.append(f'<line x1="18" y1="{-T-14}" x2="{tx-6:.1f}" y2="{tz+3:.1f}" stroke="#2b6cb0" stroke-width="0.6" stroke-dasharray="2 1.5"/>')
        if ghost:
            gx, gz = wf, -T - 50
            o.append(f'<line x1="{wf}" y1="{-T}" x2="{gx}" y2="{gz}" stroke="#c0392b" stroke-width="1" stroke-dasharray="2 1.5"/>')
            o.append(f'<g transform="translate({gx},{gz}) rotate({-TILT})"><rect x="-56" y="0" width="112" height="11" fill="none" stroke="#c0392b" stroke-width="0.8" stroke-dasharray="2 1.5"/></g>')
    else:
        o.append(part(wf + 4, -T + 2, 112, 21, "#2a2a2a", "#111", 0.3, 3))
    return "".join(o)


def dish_sheet():
    p = PAL["proof"]
    H = 3900
    S = 9.0
    b = [head(90, 150, "DISH", "Sauce · a round dish rises out of the speaker well like a radio telescope · round 2 (rebuilt per R5)",
              ["The dish is everything the MCU reads: cutoff in the centre, glide, tune, freq, range and both contours around",
               "it. The wings are the analog tone you set and leave. Only 4 wires cross the pivots. When MIDI owns any dish",
               "control, the ring of light around cutoff glows. Keys: maple button plugs on Hall switches, in two rows."],
              "Look shown: Proof (white panel, black caps, walnut base, red cutoff). Dish raised at 50°, fork at 70°"),
         placeholder(90, 590)]
    X0, Y0 = 90, 860
    b.append(view_label(X0, Y0 - 170, "PLAYING · top view, dish raised (seen from above, so the dish is foreshortened) · 1 mm = 9 px"))
    b.append(G(X0, Y0, S, dish_top(p)))
    b.append(dim_h(X0, X0 + BW * S, Y0 + BD * S + 70, "285 mm", 26))
    b.append(dim_v(X0 + BW * S + 50, Y0, Y0 + BD * S, "188 mm base", 24))
    b.append(lbl(X0, Y0 - 120, "Raised, the dish overhangs the rear by 12 mm. Its lower rim floats 12 mm above the speaker grille.", 24, "#555"))
    RX = 2900
    b.append(view_label(RX, 130, "THE DISH, face-on · Ø112 · 1 mm = 8.4 px"))
    b.append(G(RX + 20, 170, 8.4, dish_face(p)))
    b.append(note(RX, 170 + 112 * 8.4 + 50, [("Bullseye lit (V-d) = MIDI owns a dish control", 700),
                                              "Gold rings: the 10 ring controls + cutoff that MIDI can take.",
                                              "Range switches sit on the dish (MCU-read) but are physical",
                                              "truth: MIDI never flips them (owner.md, latest).",
                                              "Ring chord 18.3 mm ≥ 17; legends 2.5 mm, around the rim."], 22))
    bx, bh = box(RX, 1520, 900, "Cost and build (R8)", [
        "Cost vs SLAB: +$25–40 (dish MCU ≈ $5, 2 brass pivots,",
        "  detents, round dish PCB, low-profile B extension;",
        "  no lid) · +$5–10 for the button plugs",
        "Steps after soldering: 17",
        "Bought: maple button plugs, Hall switches, knobs,",
        "  caps, bend stick, mod fader · Service-cut: none"], 23)
    b.append(bx)
    bx2, bh2 = box(RX, 1520 + bh + 24, 900, "Checked against", [
        "owner.md: \"portable…small\"; \"feel good to use\"; MIDI",
        "  entries (knob-only no MIDI; MIDI can't flip switches);",
        "  Critter and Guitari reference; \"as silent as possible\";",
        "  \"real parts\"; \"explore the light thing\"",
        "eng v2: §2 (dish = 'Yes' rows only), §4.1, §4.2",
        "scores.md: R1, R5, R6, R7, R8"], 23)
    b.append(bx2)
    # sides
    sy = 3330
    ss = 4.4
    b.append(view_label(X0, 2680, "SIDE · raised · 1 mm = 4.4 px"))
    b.append(G(X0 + 40, sy, ss, dish_side(p) + '<line x1="-6" y1="0" x2="215" y2="0" stroke="#999" stroke-width="0.4"/>'))
    b.append(lbl(X0 + 40, sy + 44, "← player", 22, "#666"))
    b.append(note(X0 + 40, sy + 100, [("Blue: reach to cutoff ≈ 150 mm, like a far panel row.", 600),
                                     ("Red dashed: round-1 front pivot. A 50° dish hangs its rim 7 mm", 600),
                                     ("over the sharps. So the fork now pivots at the well's REAR.", 600)], 22, "#333"))
    cx = X0 + 1100
    b.append(view_label(cx, 2680, "SIDE · stowed: flat, no lid"))
    b.append(G(cx, sy, ss, dish_side(p, raised=False)))
    b.append(dim_v(cx + BD * ss + 30, sy - 38 * ss, sy, "38 mm", 22))
    b.append(lbl(cx, sy + 44, "carry 285 × 188 × 38: wing caps sit below the rim", 22, "#666"))
    nx = X0 + 2150
    b.append(view_label(nx, 2680, "LIGHTS OFF · bullseye lit"))
    b.append(f'<rect x="{nx}" y="2700" width="{int(BW*2.6)+40}" height="{int((BD+16)*2.6)+40}" rx="10" fill="#050605"/>')
    b.append(G(nx + 20, 2720 + 16 * 2.6, 2.6, dish_top(p, night=True)))
    ny2 = 3600
    b.append(note(X0, ny2, [("Changes to systems' DISH (for systems to confirm)", 700),
                            "1. Fork pivots at the well's rear, 70° detent (was front, 90°): clears the keys.",
                            "2. Speaker moves to the well centre (Ø40, ≥ 60 mm from the sharps' switch row):",
                            "    the dish lifts off it and its lower rim hangs 12 mm above the grille's rear half."], 23))
    b.append(note(X0 + 1500, ny2, [("Keys: K-E button plugs on Hall switches", 700),
                                   "Bought maple button-top plugs (woodworking part) on a drilled blank cap",
                                   "over a Gateron low-profile Hall switch. Two rows, naturals Ø14 in front.",
                                   "No service-cut parts, velocity from the Hall switch."], 23))
    b.append(note(X0 + 2900, ny2, [("Open", 700), "Board area under the wings (E7).", "Ø112, not R5's 130–140.",
                                   "38 mm base (+2 over R1).", "4-core cable life through 2 pivots."], 23))
    return save(ROOT + "dish/dish-mock.svg", W, H, "".join(b), p)


def dish_exploded():
    p = PAL["proof"]
    s = 6.6
    X0 = 130
    wal = "#5b3a26"

    def dishp(x0, y, s_):
        o = f'<rect x="{x0+68*s_}" y="{y+10*s_}" width="{112*s_}" height="{1.6*s_}" fill="{p["panel"]}" stroke="#333"/>'
        o += caps_row(x0, y + 10 * s_, s_, [80, 100, 160, 168], p["cap"], hero_x=124, hero_col=p["hero"], h=10)
        o += f'<rect x="{x0+70*s_}" y="{y+11.6*s_}" width="{108*s_}" height="{8*s_}" rx="4" fill="#2a2a2a" stroke="#111"/>'
        o += f'<rect x="{x0+112*s_}" y="{y+12*s_}" width="{24*s_}" height="{5*s_}" rx="2" fill="#3d6fae"/>'
        return o

    def fork(x0, y, s_):
        return (f'<rect x="{x0+66*s_}" y="{y}" width="{116*s_}" height="{2.5*s_}" rx="4" fill="url(#brassg)" stroke="#6b5420"/>'
                f'<rect x="{x0+126*s_}" y="{y+4*s_}" width="{58*s_}" height="{4*s_}" rx="3" fill="url(#brassg)" stroke="#6b5420"/>'
                f'<circle cx="{x0+184*s_}" cy="{y+6*s_}" r="{2.2*s_}" fill="url(#brassg)" stroke="#6b5420"/>')

    def keys(x0, y, s_):
        o = ""
        for x, d, c in ((25, 14, "#d9b98a"), (51, 12, "#3a2618")):
            o += f'<rect x="{x0+(x-d/2)*s_}" y="{y}" width="{d*s_}" height="{6*s_}" rx="{3*s_}" fill="{c}" stroke="#333"/>'
            o += f'<rect x="{x0+(x-3)*s_}" y="{y+6*s_}" width="{6*s_}" height="{3*s_}" fill="#c9c2b3" stroke="#333"/>'
            o += f'<rect x="{x0+(x-7.5)*s_}" y="{y+9*s_}" width="{15*s_}" height="{5*s_}" rx="2" fill="#7a9a6a" stroke="#333"/>'
        return o

    parts = [
        dict(a=68, b=184, t=20, draw=dishp, step="10–12", lines=["Dish: caps + round face PCB (13 pots/rotaries + hero, 4067, light ring)", "dish MCU board on its back; back skin is a second canvas"]),
        dict(a=66, b=186, t=8, draw=fork, step="13", lines=["Brass axle tube across the fork tips + 2 laser-stacked fork arms", "pivot at the well's rear; 4-core silicone cable runs through both tubes"]),
        dict(a=68, b=184, t=19, draw=lambda x0, y, s_: caps_row(x0, y + 8 * s_, s_, [82, 112, 142, 172], p["cap"], h=8) +
             f'<rect x="{x0+68*s_}" y="{y+8*s_}" width="{116*s_}" height="{1.6*s_}" fill="{p["panel"]}" stroke="#333"/>', step="5",
             lines=["Wings: low caps on board A, panels sunk 8 mm", "analog tone controls in the audio path (eng §2 knob-only)"]),
        dict(a=68, b=184, t=11, fill="#2e6b3a", step="4", lines=["Board B under the wings + low-profile B extension under the well", "≤ 8 mm parts only under the well floor (E7)"]),
        dict(a=102, b=142, t=9, fill="#444", step="9", lines=["Ø40 driver (≤ 12 mm deep) + chamber at the well centre", "grille in the well floor"]),
        dict(a=0, b=188, t=38, draw=frame_draw([(0, 5), (64, 68), (184, 188)], 38, wal, (0, 188)), step="6",
             lines=["Base: ≈ 12 laser layers (walnut ply), the well cut through the top 8", "fork channels beside the well"]),
        dict(a=10, b=60, t=14, draw=keys, step="1–2", lines=["Keys: bought maple button plugs on drilled blank caps", "on Gateron low-profile Hall switches; felt collar per hole"]),
        dict(a=4, b=64, t=9, fill="#3d6fae", step="3", lines=["Board D + 2 LiPo pouch cells under the keys", ""]),
        dict(a=0, b=188, t=3, fill=wal, step="7", lines=["Base plate, screws, felt feet", ""]),
    ]
    svg, yb = exploded(parts, s=s, x0=X0, y0=520, label_x=X0 + 195 * s + 60, gap=60)
    b = [head(90, 150, "DISH · how it goes together", "Exploded side view (from the right), front at the left · 1 mm = 6.6 px",
              ["The base is SLAB's core with a round well cut in the middle. The dish is its own small instrument: a round",
               "PCB with its own MCU that talks to the base over 4 wires through the hollow pivots. Numbers = build steps (17)."],
              "Checked against eng v2 §2, §4.1, §4.2 · common-how-it-works §1 (joint rule), §5 · dish/how-it-works"),
         svg, mm_ruler(X0, yb + 70, s, 188)]
    ay = yb + 230
    b.append(view_label(90, ay, "ASSEMBLED · raised · same scale"))
    b.append(G(X0, ay + 900, s, dish_side(p, ghost=False)))
    H = int(ay + 1000)
    return save(ROOT + "dish/dish-exploded.svg", 3000, H, "".join(b), p)


if __name__ == "__main__":
    print(dish_sheet()); print(dish_exploded())
