"""SLAB fix-pass sheet + exploded view. Body 292 x 185 x 34; lid 12; stand = lid folded (24) under the rear."""
import math
from r2s_common import *

BW, BD, BT = 292, 185, 34      # F3: 22 mm bend/mod zone -> 292 wide (3 mm edge margins), as systems


PX = (BW - 280) / 2      # panel offset in the wider body
FELT = "#3e3a35"         # S2: felt lining inside the lid


def slab_top(p, night=False, light_on=True, wordmark=True):
    o = [f'<g filter="url(#shbig)"><rect x="0" y="0" width="{BW}" height="{BD}" rx="5" '
         f'{body_fill(p) if not night else "fill=\"#0a0a0a\""}/></g>']
    # sunk panel (4 mm): dark reveal around it
    o.append(f'<rect x="{PX-0.9}" y="3.4" width="281.8" height="101.8" rx="2.6" fill="#000" opacity="{0.55 if not night else 0.9}"/>')
    o.append(G(PX, 4.5, 1, panel(p, "slab", night, "pip", light_on)))
    # strip between panel and keys: hides the keybed's rear; wordmark plate; lid magnets
    if not night:
        if wordmark:
            o.append(txt(BW - 53, 115.2, NAME, 6.2, p["silk"] if p["body_mat"] == "acrylic" else "#2b2a27", weight=700))
        for x in (8, BW - 8):
            o.append(f'<circle cx="{x}" cy="112" r="2.2" fill="#9a9a9a" stroke="#555" stroke-width="0.3"/>')
    kx = 3 + ZW + 0.6
    o.append(key_well(kx, 118, 263.4, 61, night))
    o.append(key_well(2.6, 120.6, ZW + 0.8, 54.8, night))
    o.append(bendmod_lead(3.0, 121.0, p, night))
    if not night:
        c = "#2b2a27" if p["body_mat"] != "acrylic" else "#ccc"
        o.append(txt(3 + ZW / 2, 119.6, "mod", 2.4, c))
        o.append(txt(3 + ZW / 2, 180.3, "bend", 2.4, c))
    o.append(keys_lever(kx + 1.7, 120, p, night, wlen=57, blen=35))
    return "".join(o)


def slab_side(p, s, stand=True, lid_on=False, tilt=True):
    """Side elevation (from the right), local mm, x = depth from the front, y up negative. Returns svg."""
    body = p["body_top"]
    o = []
    # stand block (lid folded) under the rear
    lc = p["body_top"]
    if stand:
        o.append(part(80, 0, 105, 12, lc) + part(80, 12, 105, 12, lc))
        o.append(part(80, 10.4, 105, 1.6, FELT, "none", 0, 0) + part(80, 12, 105, 1.6, FELT, "none", 0, 0))
        o.append(f'<path d="M80,12 q-4,0 -4,0" stroke="#3a2a1a" stroke-width="1.6" fill="none"/>')
        o.append(part(76.5, 9.5, 4, 5, "#3a2a1a", rx=2))       # sewn leather hinge at the fold
        o.append(part(176, 24, 8, 3, "#222", rx=1))            # foot
        o.append(part(82, 24, 8, 3, "#222", rx=1))
    # body shell
    o.append(part(0, -BT, BD, BT, body, "#222", 0.3, rx=3))
    for k in range(1, 11):
        o.append(f'<line x1="0" y1="{-k*3.1:.1f}" x2="{BD}" y2="{-k*3.1:.1f}" stroke="#000" stroke-opacity="0.12" stroke-width="0.2"/>')
    # keys (top 1.5 below rim), panel sunk 4, caps 8 above rim
    o.append(part(6, -33, 56, 3.5, p["nat"], "#555", 0.2, rx=0.6))
    o.append(part(28, -35.6, 34, 3.6, p["sharp"], "#222", 0.2, rx=0.6))
    o.append(part(80, -30.4, 101, 0.8, p["panel"], "#222", 0.1, rx=0))
    o.append(capsil(92, -30, 26, 12, p["hero"], 3))
    for x in (126, 140, 152, 168):
        o.append(capsil(x, -30, 12, 11, p["cap"], 2))
    if lid_on:
        o.append(part(0, -BT - 12, BD, 12, lc, "#222", 0.3, rx=2))
        o.append(part(1, -BT - 1.8, BD - 2, 1.6, FELT, "none", 0, 0))
        o.append(part(78, -BT - 12.5, 4, 2, "#3a2a1a", rx=1))
    return "".join(o)


def slab_sheet():
    p = PAL["field"]
    LC = p["body_top"]
    H = 3620
    S = 9.0
    b = [head(90, 150, "SLAB", "Designed for use · one rigid body · the lid becomes the stand · round 2 fix pass",
              ["One stiff body, nothing moves, no cable crosses anything. A separate lid covers panel and keys for the",
               "bag. To play, the lid folds in half and clicks under the back: an 8° desk stand. The panel finally has",
               "room: 12 mm knobs at 17+ mm pitch, 11 mm faders, 2.7 mm-high legends, a Ø40 mm speaker. 292 mm wide:",
               "the extra 7 mm over round 2 is the 22 mm bend/mod zone that fits the real stick (eng §v1.5b)."],
              "Look shown: Field (warm-grey felt layers, black panel, gold rules, orange cutoff). Lid in the same felt-faced ply, felt-lined. Other looks: look-sheet.png"),
         placeholder(90, 590)]
    X0, Y0 = 90, 700
    b.append(view_label(X0, Y0 - 20, "PLAYING · top view at real proportions · 1 mm = 9 px"))
    b.append(G(X0, Y0, S, slab_top(p)))
    b.append(dim_h(X0, X0 + BW * S, Y0 + BD * S + 70, "292 mm", 26))
    b.append(dim_v(X0 + BW * S + 50, Y0, Y0 + 105 * S, "panel zone 100", 24))
    b.append(dim_v(X0 + BW * S + 50, Y0 + 105 * S, Y0 + BD * S, "keys 75 + lip 5", 24))
    b.append(dim_v(X0 + BW * S + 235, Y0, Y0 + BD * S, "185 mm", 26))
    # callouts
    b.append(callout(X0 + (257 + PX) * S, Y0 + 31 * S, X0 + 2400, Y0 - 90,
                     ["Ø40 driver under a Ø41 grille", "≈125 mm from the key sensors (60 mm rule ✓)"], 24))
    b.append(G(X0, Y0, S, f'<circle cx="20" cy="111.6" r="1.1" fill="{OWN_C}"/>' + txt(23, 112.8, "amber pip by HOLD (V-a) = a gold-ringed knob is not in control", 3.0, "#2b2a27", anchor="start", font=UI_FONT, weight=600)))
    b.append(lbl(X0, Y0 + BD * S + 125, "↑ 22 mm zone at the left of the keys: Adafruit #2765 stick (dashed = its 17.5 × 17.4 body) in a one-axis Delrin gate; mod slide pot behind it (gold dot = MIDI, CC1)", 22, "#555"))
    # right column
    RX = 3160
    bx, bh = price_box(RX - 60, 120, 760, "≈ $530–860", [
        "eng architecture-v2 §5 first-unit total (rev. with",
        "  E1/E3/E5), keys route (b) included",
        "Cost vs SLAB: baseline, $0",
        "Lid ≈ $10–15 (laser layers, leather strip, felt,",
        "  12 magnets, 4 steel discs): inside §5 enclosure",
        "Steps after soldering: 12",
        "Bought: 25 Choc V2 silent switches, 25 SS49E,",
        "  25 magnets, knobs, fader caps, #2765 stick,",
        "  mod slide pot · Owner-cut at Vector Space:",
        "  25 lever key tops (material only) · No 3D print"], 23)
    b.append(bx)
    bx2, bh2 = box(RX - 60, 120 + bh + 24, 760, "Checked against", [
        "owner.md: \"portable…small\"; \"dont over",
        "  index on OP1…feel good\"; 2 octaves min;",
        "  ready-made modules; MIDI jump-on-move;",
        "  knob-only = no MIDI; MIDI can't flip",
        "  switches; \"real parts\"; \"as silent as",
        "  possible\"; \"explore the light thing\"",
        "eng architecture-v2 §2 as changed by E1 (12",
        "  MIDI-ownable incl. mod, CC1), §4.1, §4.2, §5",
        "eng answers E1, E2, E5 · budget-variant §v1.4b",
        "  (keys, rev 6), §v1.5b (stick, rev 7)",
        "scores.md round 2: F1–F5, S1, S2"], 23)
    b.append(bx2)
    # carry + lights off (right column, under boxes)
    cy0 = 1150
    b.append(view_label(RX - 60, cy0, "CARRY · lid on · 1 mm = 2.5 px"))
    lid = [f'<g filter="url(#shbig)"><rect width="{BW}" height="{BD}" rx="5" {body_fill(p)}/></g>',
           f'<rect x="0" y="103" width="{BW}" height="4" fill="#3a2a1a"/>',
           txt(BW / 2, 64, NAME, 13, "#2b2a27", weight=700), txt(BW / 2, 150, "leather hinge strip ↑ · felt-lined inside", 6, "#3a3631", font=UI_FONT)]
    b.append(G(RX - 60, cy0 + 30, 2.5, "".join(lid)))
    b.append(lbl(RX - 60, cy0 + 30 + BD * 2.5 + 46, "292 × 185 × 46 mm · one flat block · asleep", 24))
    ny = cy0 + 640
    b.append(view_label(RX - 60, ny, "LIGHTS OFF · pip lit"))
    b.append(f'<rect x="{RX-60}" y="{ny+20}" width="{int(BW*2.5)+40}" height="{int(BD*2.5)+40}" rx="10" fill="#050605"/>')
    b.append(G(RX - 40, ny + 40, 2.5, slab_top(p, night=True)))
    b.append(note(RX - 60, ny + 560, ["Glow pointers on every knob and fader cap,", "glow stripes on the sharps (luminous paint",
                                      "on bought caps), amber pip, red status LED."], 22))
    # bottom: sides
    sy = 2900
    ss = 5.6
    b.append(view_label(X0, 2540, "SIDE · playing on the stand (8°) · 1 mm = 5.6 px"))
    tilt = math.degrees(math.atan(27 / 185))
    side = (f'<line x1="-10" y1="27" x2="200" y2="27" stroke="#999" stroke-width="0.4"/>'
            f'<g transform="translate(0,27) rotate({-tilt:.2f})"><g transform="translate(0,-0)">{slab_side(p, ss)}</g></g>')
    b.append(G(X0 + 60, sy, ss, side))
    b.append(lbl(X0 + 20, sy + 220, "← player", 22, "#777"))
    b.append(lbl(X0 + 60 + 120 * ss, sy + 220, "stand = the lid folded in half (2 × 12 mm), held by 4 magnets on steel discs", 22, "#555"))
    b.append(lbl(X0 + 60 + 120 * ss, sy + 252, "rear row rises ≈ 25 mm; the stand's magnets are > 80 mm from the key sensors", 22, "#555"))
    # fold sequence
    fx = X0 + 1350
    b.append(view_label(fx, 2540, "LID → STAND in two moves"))
    seq = [
        (0, "1  lift the lid off (wakes)", f'{part(0,0,105,12,LC)}{part(105,0,80,12,LC)}{part(0,10.4,185,1.6,FELT,"none",0,0)}{part(103,-1,4,14,"#3a2a1a",rx=1)}'),
        (1, "2  fold it at the leather strip", f'{part(0,0,105,12,LC)}{part(0,10.4,105,1.6,FELT,"none",0,0)}<g transform="translate(105,12) rotate(150)">{part(0,-12,80,12,LC)}</g>{part(102,9,5,5,"#3a2a1a",rx=2)}'),
        (2, "3  press it under the back: click", f'{part(0,0,185,34,p["body_top"],rx=3)}{part(80,34,105,12,LC)}{part(80,46,105,12,LC)}'),
    ]
    for i, (k, cap, g) in enumerate(seq):
        gx = fx + i * 430
        b.append(G(gx, sy - 80, 2.0, g))
        b.append(lbl(gx, sy + 70, cap, 22, INK, weight=600))
    # carry side
    cx = fx + 1350
    b.append(view_label(cx, 2540, "SIDE · carry"))
    b.append(G(cx, sy + 40, ss * 0.6, slab_side(p, ss, stand=False, lid_on=True)))
    b.append(dim_v(cx + BD * ss * 0.6 + 30, sy + 40 - 46 * ss * 0.6, sy + 40, "46 mm", 22))
    # notes row
    ny2 = 3260
    b.append(note(X0, ny2, [("Keys (K-B): lever tops, owner-cut at Vector Space, on Choc V2 silent switches", 700),
                            "A 5 × 2 mm magnet in each top, beside the switch, over a standing TO-92 SS49E:",
                            "contactless travel = velocity, the quietest route (eng §v1.4b b). Steel-rod pivot",
                            "at the rear. Gateron LP Hall = fallback, pending eng's bench test. Keys rethink pending.",
                            ("Bend: Adafruit #2765 stick, Delrin slot = one axis, springs back. Mod: slide pot.", 600)], 23))
    b.append(note(X0 + 1250, ny2, [("MIDI and the light (owner.md, latest)", 700),
                                   "Gold ring/dot = MIDI can take it (12): glide, tune, freq 2, freq 3, cutoff,",
                                   "6 contour faders, mod (CC1 in and out, eng E1). None on RANGE or bend.",
                                   "No ring = the knob is the sound. It never sends MIDI. MIDI never flips a switch.",
                                   "Pip lit = some ringed knob isn't in control. Move it, or HOLD + TUNE: all back."], 23))
    b.append(note(X0 + 2550, ny2, [("Open", 700),
                                   "Stand holds 20 N at the rear edge? #2765 cap tilts on a stem",
                                   "(gate works) or slides as a puck (gate fails: SparkFun backup)?",
                                   "Throw angle and slide-pot body length: UNVERIFIED in hand."], 23))
    return save(ROOT + "slab/slab-mock.svg", W, H, "".join(b), p)


# ------------------------------------------------------------------ exploded
def slab_exploded():
    p = PAL["field"]
    s = 7.0
    X0 = 140
    felt, ply = "#8b8780", "#7d7a74"

    def caps(x0, y, s_):
        return caps_row(x0, y + 12 * s_, s_, [126, 140, 152, 168], p["cap"], hero_x=105, hero_col=p["hero"]) + \
               f'<rect x="{x0+60*s_}" y="{y+12*s_-0.5}" width="{0}" height="0"/>'

    def keybed(x0, y, s_):
        return (f'<rect x="{x0+6*s_}" y="{y+6*s_}" width="{56*s_}" height="{4*s_}" rx="3" fill="{p["nat"]}" stroke="#333" stroke-width="1"/>'
                f'<rect x="{x0+28*s_}" y="{y+2*s_}" width="{34*s_}" height="{4*s_}" rx="3" fill="{p["sharp"]}"/>'
                f'<rect x="{x0+4*s_}" y="{y+10*s_}" width="{74*s_}" height="{4*s_}" rx="2" fill="#3a3a3a"/>'
                f'<circle cx="{x0+70*s_}" cy="{y+8*s_}" r="{1.4*s_}" fill="#c0c0c0" stroke="#333"/>'
                + "".join(f'<rect x="{x0+(x-4)*s_}" y="{y+10*s_}" width="{8*s_}" height="{4*s_}" rx="2" fill="#7a9a6a" stroke="#333"/>' for x in (18, 46)))

    def board(fill, comps):
        def f(x0, y, s_, fill=fill, comps=comps):
            o = ""
            for (a, b_, t, c) in comps:
                o += f'<rect x="{x0+a*s_:.1f}" y="{y+(0 if t>0 else 0):.1f}" width="{(b_-a)*s_:.1f}" height="{abs(t)*s_:.1f}" rx="3" fill="{c}" stroke="#222" stroke-width="1"/>'
            return o
        return f

    def ab(x0, y, s_):
        o = f'<rect x="{x0+80*s_}" y="{y}" width="{101*s_}" height="{1.6*s_}" fill="{p["panel"]}" stroke="#222"/>'
        for x in (100, 126, 140, 152, 168):
            o += f'<rect x="{x0+(x-4.5)*s_}" y="{y+1.6*s_}" width="{9*s_}" height="{7*s_}" rx="2" fill="#4a6fa5"/>'
        o += f'<rect x="{x0+150*s_}" y="{y+1.6*s_}" width="{0}" height="0"/>'
        o += f'<rect x="{x0+80*s_}" y="{y+19.6*s_}" width="{101*s_}" height="{1.6*s_}" fill="#2e6b3a" stroke="#222"/>'
        for x in (86, 112, 118, 140, 160, 174):
            o += f'<rect x="{x0+x*s_}" y="{y+8.6*s_}" width="{1.2*s_}" height="{11*s_}" fill="#999"/>'
        o += f'<rect x="{x0+150*s_}" y="{y+1.6*s_}" width="{28*s_}" height="{10*s_}" rx="6" fill="#111" stroke="#555"/>'
        return o

    parts = [
        dict(name="lid", a=0, b=185, t=12, fill=felt, step="11",
             lines=["Lid: two laser-stacked leaves (105 + 80), the body's material + leather hinge", "frame + 3 mm skin, felt-lined 9 mm cap pocket; end magnets; S-pole sense magnet"]),
        dict(a=80, b=181, t=12, draw=caps, step=None,
             lines=["Knobs: bought skirted caps (12 mm) + one 26 mm hero; fader caps", "push-fit on the pot shafts last of all"]),
        dict(a=80, b=181, t=21, draw=ab, step="4",
             lines=["Panel sandwich: board A (the panel itself, bare PCB) over board B", "pots/switches under A · 11 mm headers · B = the voice · speaker in A/B notch"]),
        dict(a=0, b=185, t=27, draw=frame_draw([(0, 5), (78, 82), (180, 185)], 27, ply), step="6",
             lines=["Body: ≈ 9 laser-cut layers (felt-faced ply), through-bolted", "a frame: open over the panel zone and the key zone"]),
        dict(a=0, b=80, t=14, draw=keybed, step="1",
             lines=["Keys: 25 lever tops, owner-cut at Vector Space, on a steel pivot rod", "each on a Choc V2 silent switch, magnet in the top; felt top stop"]),
        dict(a=26, b=40, t=1.6, fill="#2e6b3a", step="2",
             lines=["Strip C = the switch board: 25 Choc V2 + 25 standing TO-92 SS49E", "its own thin board (keys don't size the main PCB)"]),
        dict(a=4, b=78, t=9, fill="#3d6fae", step="3",
             lines=["Board D (2 Pico 2, DACs, charger, boosts) beside 2 LiPo pouch cells", "under the keys, away from the VCOs (eng §4.1)"]),
        dict(a=0, b=185, t=3, fill=ply, step="7",
             lines=["Base plate, 4 screws: open it to swap the battery (J17)", "4 steel discs at the rear catch the stand; 4 felt feet"]),
    ]
    svg, yb = exploded(parts, s=s, x0=X0, y0=500, label_x=X0 + 190 * s + 60, gap=70)
    b = [head(90, 150, "SLAB · how it goes together", "Exploded side view (from the right), front of the instrument at the left · 1 mm = 7 px",
              ["Build order is bottom-up: keys and strip C into the body, D and battery under them, then the panel",
               "sandwich drops in from the top, the base closes it. Numbers = build steps (12 in total; 8, 9, 10, 12 are",
               "magnets, feet, grille and the hinge strip)."], "Checked against eng v2 §4.1 (boards A–D), §4.2 (height stack) · budget-variant §v1.4b rev 6 (keys) · common-how-it-works §1, §6"),
         svg, mm_ruler(X0, yb + 70, s, 185)]
    # assembled reference
    ay = yb + 230
    b.append(view_label(90, ay, "ASSEMBLED · same scale"))
    b.append(G(X0, ay + 330, s, slab_side(p, s, stand=False)))
    b.append(lbl(X0 + 190 * s + 60, ay + 230, "34 mm body: control stack 28–32 (eng §4.2) under a panel sunk 4 mm;", 24))
    b.append(lbl(X0 + 190 * s + 60, ay + 262, "keys stack 31–36 with pouch cells. Caps stand 8 mm above the rim.", 24))
    H = int(ay + 420)
    return save(ROOT + "slab/slab-exploded.svg", 2750, H, "".join(b), p)


if __name__ == "__main__":
    print(slab_sheet()); print(slab_exploded())
