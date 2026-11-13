"""MOTTO fix-pass sheet + exploded. Body 292 wide x 190 (spine) -> 165 (right) x 34; lid 12 hinged at the tail.
Draws (secrets.choice, this round): body = cork with a white panel; strategy = "Use an unacceptable colour"
(acid chartreuse hero); lid placeholder = the motto ribbon alone on raw wood."""
import math
from r2s_common import *

BW, BD = 292, 190      # F3 (3 mm edge margins, as systems): 22 mm bend/mod zone; M2: spine 195 -> 190 (panel 115 -> 110)
PX = (BW - 280) / 2


def rear(x):
    return motto_rear(x - PX) if x > PX else 0.0


def outline_path(front=BD):
    pts = [(0, 0), (115 + PX, 0)] + [(x, rear(x)) for x in range(124, int(BW) + 1, 4)] + [(BW, rear(BW)), (BW, front), (0, front)]
    return "M" + " L".join(f"{x:.1f},{y:.2f}" for x, y in pts) + " Z"


RC = (22 + PX, 27.5)     # rose = speaker centre (M1 option a: stays top-left)


def motto_top(p, night=False, owned=None, light_on=True, keepout=False):
    owned = owned or set()
    o = [f'<g filter="url(#shbig)"><path d="{outline_path()}" {body_fill(p) if not night else "fill=\"#0a0a0a\""}/></g>']
    o.append(G(PX, 2.5, 1, panel(p, "motto", night, "pips", light_on, owned=owned)))
    if night:
        o.append(f'<circle cx="{RC[0]}" cy="{RC[1]}" r="21" fill="#080808"/>')
    else:
        o.append(grille(RC[0], RC[1], 20, p, "rose"))
        o.append(f'<rect x="{PX+1.5}" y="-1.6" width="110" height="2.6" rx="1" fill="url(#brassg)"/>')
        o.append(f'<circle cx="{BW-4}" cy="{rear(BW-4)+4:.1f}" r="2.2" fill="url(#brassg)" stroke="#6b5420" stroke-width="0.3"/>')
        o.append(txt(BW - 53, 120.6, NAME, 6.2, "#2b2a27", weight=700))
        for x in (8, BW - 8):
            o.append(f'<circle cx="{x}" cy="118" r="2.2" fill="#9a9a9a" stroke="#555" stroke-width="0.3"/>')
    kx = 3 + ZW + 0.6
    o.append(key_well(kx, 123, 263.4, 61, night))
    o.append(key_well(2.6, 125.6, ZW + 0.8, 54.8, night))
    o.append(bendmod_lead(3.0, 126.0, p, night, pip=("mod" in owned) and light_on))
    if not night:
        o.append(txt(3 + ZW / 2, 124.6, "mod", 2.4, "#2b2a27"))
        o.append(txt(3 + ZW / 2, 185.3, "bend", 2.4, "#2b2a27"))
    o.append(keys_lever(kx + 1.7, 125, p, night, wlen=57, blen=35, reverse=True))
    if keepout and not night:
        # M1 (a) + eng E8: VCO cores >= 30 mm from the driver frame (r 20) -> keep-out r 50
        o.append(f'<circle cx="{RC[0]}" cy="{RC[1]}" r="50" fill="none" stroke="#2b6cb0" stroke-width="0.45" stroke-dasharray="1.6 1.2"/>')
        o.append(txt(RC[0] + 36, RC[1] + 44, "E8 keep-out: VCO cores ≥ 30 mm from the driver", 2.6, "#2b6cb0", anchor="start", font=UI_FONT, weight=700))
    return "".join(o)


def lid_face(p, w=BW, h=BD):
    """Lid seen from the player, standing: raw birch inner face; bottom edge follows the bentside."""
    pts = [(0, 0), (w, 0), (w, h - rear(w))] + [(x, h - rear(x)) for x in range(int(w) - 1, 116 + int(PX), -4)] + [(0, h)]
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"
    o = [f'<path d="{d}" fill="#4b2f1d" filter="url(#grainf)"/>']
    inset = []
    for x, y in pts:
        inset.append((min(max(x, 3), w - 3), min(max(y, 3), h - 3) if y > 3 else 3))
    d2 = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in inset) + " Z"
    o.append(f'<path d="{d2}" fill="#dcc7a0" filter="url(#grainv)"/>')
    # the motto ribbon alone (placeholder)
    o.append('<path d="M44,58 Q147,40 250,58 L257,74 Q147,58 38,74 Z" fill="#f4efe4" stroke="#b9ab8e" stroke-width="0.6"/>')
    o.append('<path d="M38,74 l-10,6 l8,-14 Z M257,74 l10,6 l-8,-14 Z" fill="#e7dfcd"/>')
    o.append(txt(147, 65.5, "[ your motto here ]", 7.5, "#7a5a2a"))
    o.append(txt(147, 117, "raw birch: the owner's canvas", 5.2, "#8a7550", font=UI_FONT, weight=600))
    o.append(txt(147, 125, "(placeholder: no painting proposed)", 4.2, "#8a7550", font=UI_FONT))
    return "".join(o)


def motto_side(p, open_=True):
    """Side from the right: body (spine depth 190), lid hinged at the rear, stay; local mm, front at x=0."""
    o = [part(0, -34, BD, 34, p["body_top"], "#222", 0.3, 3, 'filter="url(#corkf)"')]
    o.append(part(6, -33, 56, 3.5, p["sharp"], "#222", 0.2))
    o.append(part(28, -35.6, 34, 3.6, p["nat"], "#555", 0.2))
    o.append(part(78, -30.4, 110, 0.8, p["panel"], "#222", 0.1, 0))
    o.append(capsil(92, -30, 26, 12, p["hero"], 3))
    for x in (120, 134, 148, 160):
        o.append(capsil(x, -30, 12, 11, p["cap"], 2))
    if open_:
        o.append(f'<g transform="translate({BD},-34) rotate(-100)">{part(0, 0, BD, 12, "#4b2f1d", "#222", 0.3, 2)}{part(0, 0, BD, 2, "#dcc7a0", "none", 0, 0)}</g>')
        o.append(f'<line x1="{BD-60}" y1="-34" x2="{BD-3}" y2="-120" stroke="#b8933f" stroke-width="1.6"/>')
        o.append(f'<circle cx="{BD}" cy="-34" r="2.2" fill="url(#brassg)"/>')
        for k in range(3):
            o.append(f'<path d="M168,{-46-k*8} q8,-6 16,-2" fill="none" stroke="#c9a24e" stroke-width="0.8" opacity="{0.9-k*0.25}"/>')
        o.append(f'<path d="M180,-90 q-40,-10 -80,6" fill="none" stroke="#c9a24e" stroke-width="0.8" stroke-dasharray="2 2"/>')
    else:
        o.append(part(0, -46, BD, 12, "#4b2f1d", "#222", 0.3, 2, 'filter="url(#grainf)"'))
    return "".join(o)


def motto_sheet():
    p = PAL["motto"]
    H = 3840
    S = 9.0
    b = [head(90, 150, "MOTTO", "Sauce · a tiny bentside harpsichord with a painted lid · round 2 fix pass (the sauce lead)",
              ["The panel IS the bentside: 110 mm deep at the spine, 85 at the right, so the curve costs no extra",
               "depth (190 overall, inside the box). The rose is the speaker grille. The lid hinges at the tail and stands",
               "behind the panel facing you, a raw-birch canvas for whatever you paint. Reverse-colour keys. Twelve amber",
               "pips, one per MIDI-able control (mod's sits by its fader)."],
              "Look (round-2 draws): cork body, white panel, acid-chartreuse cutoff (\"use an unacceptable colour\"; swap: one cap), walnut only outside the lid"),
         placeholder(90, 590)]
    X0, Y0 = 90, 720
    b.append(view_label(X0, Y0 - 40, "PLAYING · top view · 1 mm = 9 px"))
    b.append(G(X0, Y0, S, motto_top(p, owned={"cutoff", "fader1"})))
    b.append(callout(X0 + RC[0] * S, Y0 + (RC[1] - 21) * S, X0 + 1250, Y0 - 100, ["M1 (a): the rose stays top-left over a Ø40 driver;", "eng puts the VCO cores on the right B board (E8)"], 24))
    b.append(dim_h(X0, X0 + BW * S, Y0 + BD * S + 70, "292 mm", 26))
    b.append(dim_v(X0 + BW * S + 50, Y0, Y0 + BD * S, "190 at the spine", 24))
    b.append(dim_v(X0 + BW * S + 50, Y0 + rear(285) * S, Y0 + BD * S, "", 24))
    b.append(lbl(X0 + BW * S + 70, Y0 + 30 * S + 60, "165 at the right", 24, "#555"))
    b.append(G(X0, Y0, S, f'<circle cx="27" cy="118" r="1.1" fill="{OWN_C}"/>' + txt(30, 119.2, "amber pip beside each of the 12 gold-marked controls lights when MIDI owns it (V-c): 2 lit here", 3.0, "#2b2a27", anchor="start", font=UI_FONT, weight=600)))
    RX = 3010
    b.append(view_label(RX, 130, "FROM THE PLAYER · lid up · 1 mm = 2.95 px"))
    lf = lid_face(p) + G(0, BD, 1, part(0, 0, BW, 34, p["body_top"], "#222", 0.3, 2, 'filter="url(#corkf)"') +
                         "".join(part(27.3 + i * 17.4, 2, 16.6, 6, p["sharp"], "#000", 0.2, 0.6) for i in range(15)))
    b.append(G(RX, 170, 2.95, lf))
    b.append(note(RX, 170 + 226 * 2.95 + 50, ["Lid lifts off (6 hinge screws + the stay) to paint it flat.",
                                             "Speaker → lid → you: the reflector claim is UNVERIFIED.",
                                             "Cheap test: a cardboard lid behind the first speaker."], 23))
    bx, bh = price_box(RX, 1180, 850, "≈ $565–920", [
        "= eng architecture-v2 §5 first unit ≈ $530–860 (rev. with",
        "  E1/E3/E5, keys route b) + MOTTO's +$35–60",
        "Cost vs SLAB: +$35–60 (brass piano hinge $8–12, stay",
        "  $5–10, walnut ply lid skin $15–25, 12 LEDs + 2 ×",
        "  74HC595 ≈ $3, walnut for the key tops ≈ $10–20)",
        "Steps after soldering: 15",
        "Bought: Choc V2 silent + SS49E + magnets, knobs, caps,",
        "  #2765 stick, mod slide pot · Owner-cut at Vector",
        "  Space: walnut lever tops (material only)"], 23)
    b.append(bx)
    bx2, bh2 = box(RX, 1180 + bh + 24, 850, "Checked against", [
        "owner.md: \"hand paint it…based on outcome\" (Q5);",
        "  \"portable…small\"; \"feel good to use\"; MIDI entries",
        "  (knob-only = no MIDI, MIDI can't flip switches);",
        "  \"explore the light thing\"; \"real parts\"; silent",
        "eng architecture-v2 §2 as changed by E1 (12 ownable",
        "  incl. mod, CC1), §4.1, §4.2, §5 · answers E2, E8",
        "  (speaker over the left B board) · budget-variant",
        "  §v1.4b rev 6 (keys), §v1.5b rev 7 (stick)",
        "scores.md round 2: F1–F5, M1–M4"], 23)
    b.append(bx2)
    # sides + night
    sy = 3420
    ss = 3.2
    b.append(view_label(X0, 2640, "SIDE · lid up at 100°, on its stay"))
    b.append(G(X0 + 40, sy, ss, motto_side(p) + '<line x1="-6" y1="0" x2="215" y2="0" stroke="#999" stroke-width="0.4"/>'))
    b.append(lbl(X0 + 40, sy + 40, "← player · rose fires up in front of the lid", 22, "#666"))
    cx = X0 + 1250
    b.append(view_label(cx, 2640, "SIDE · closed"))
    b.append(G(cx, sy, ss, motto_side(p, False)))
    b.append(dim_v(cx + BD * ss + 30, sy - 46 * ss, sy, "46 mm", 22))
    b.append(lbl(cx, sy + 40, "carry 292 × 190 × 46, a recognisable outline", 22, "#666"))
    nx = X0 + 2300
    b.append(view_label(nx, 2640, "LIGHTS OFF · 2 pips lit"))
    b.append(f'<rect x="{nx}" y="2660" width="{int(BW*2.6)+40}" height="{int(BD*2.6)+40}" rx="10" fill="#050605"/>')
    b.append(G(nx + 20, 2680, 2.6, motto_top(p, night=True, owned={"cutoff", "fader1"})))
    ny2 = 3540
    b.append(note(X0, ny2, [("Speaker vs VCOs (M1, option a)", 700),
                            "The rose stays top-left, where a harpsichord's is. Eng E8's rule:",
                            "VCO cores ≥ 30 mm from the driver frame: eng puts the VCO cores on the right",
                            "B board, well clear. PAM8302 at the speaker; foam-gasketed chamber."], 23))
    b.append(note(X0 + 1300, ny2, [("MIDI (owner.md, latest; eng E1)", 700),
                                   "12 pips, one per MIDI-able control: 11 gold rings + the mod fader (CC1).",
                                   "Knob-only controls never send MIDI; MIDI never flips a switch; no RANGE ring.",
                                   "A lit pip = 'this one isn't in control: move it to take it back'."], 23))
    b.append(note(X0 + 2550, ny2, [("Open", 700), "Reflector: unverified. Test as written: a",
                                   "cardboard lid behind the first speaker (M4).", "Chartreuse stays (M3); swap = one cap.",
                                   "#2765 gate in hand; keys rethink pending."], 23))
    return save(ROOT + "motto/motto-mock.svg", W, H, "".join(b), p)


def motto_exploded():
    p = PAL["motto"]
    s = 6.6
    X0 = 130
    cork = "#b48a5e"

    def lid(x0, y, s_):
        return (f'<rect x="{x0}" y="{y}" width="{190*s_}" height="{3*s_}" rx="3" fill="#4b2f1d" stroke="#222"/>'
                f'<rect x="{x0}" y="{y+3*s_}" width="{190*s_}" height="{7*s_}" rx="2" fill="none" stroke="#777" stroke-dasharray="6 5"/>'
                f'<rect x="{x0}" y="{y+3*s_}" width="{8*s_}" height="{7*s_}" fill="#7d7a74"/><rect x="{x0+182*s_}" y="{y+3*s_}" width="{8*s_}" height="{7*s_}" fill="#7d7a74"/>'
                f'<rect x="{x0}" y="{y+10*s_}" width="{190*s_}" height="{2*s_}" rx="2" fill="#dcc7a0" stroke="#222"/>')

    def hinge(x0, y, s_):
        return (f'<rect x="{x0+183*s_}" y="{y}" width="{7*s_}" height="{4*s_}" rx="2" fill="url(#brassg)" stroke="#6b5420"/>'
                f'<line x1="{x0+125*s_}" y1="{y+10*s_}" x2="{x0+190*s_}" y2="{y+2*s_}" stroke="#b8933f" stroke-width="{1.2*s_}"/>')

    def caps(x0, y, s_):
        return caps_row(x0, y + 12 * s_, s_, [120, 134, 148, 160], p["cap"], hero_x=105, hero_col=p["hero"])

    def ab(x0, y, s_):
        o = f'<rect x="{x0+78*s_}" y="{y}" width="{115*s_}" height="{1.6*s_}" fill="{p["panel"]}" stroke="#555"/>'
        for x in (105, 120, 134, 148):
            o += f'<rect x="{x0+(x-4.5)*s_}" y="{y+1.6*s_}" width="{9*s_}" height="{7*s_}" rx="2" fill="#4a6fa5"/>'
        o += f'<rect x="{x0+78*s_}" y="{y+19.6*s_}" width="{115*s_}" height="{1.6*s_}" fill="#2e6b3a" stroke="#222"/>'
        o += f'<rect x="{x0+160*s_}" y="{y+1.6*s_}" width="{28*s_}" height="{10*s_}" rx="6" fill="#111" stroke="#555"/>'
        for x in (84, 110, 140, 156):
            o += f'<rect x="{x0+x*s_}" y="{y+8.6*s_}" width="{1.2*s_}" height="{11*s_}" fill="#999"/>'
        return o

    def keybed(x0, y, s_):
        return (f'<rect x="{x0+6*s_}" y="{y+6*s_}" width="{56*s_}" height="{4*s_}" rx="3" fill="{p["sharp"]}" stroke="#222"/>'
                f'<rect x="{x0+28*s_}" y="{y+2*s_}" width="{34*s_}" height="{4*s_}" rx="3" fill="{p["nat"]}" stroke="#555"/>'
                f'<rect x="{x0+4*s_}" y="{y+10*s_}" width="{74*s_}" height="{4*s_}" rx="2" fill="#3a3a3a"/>')

    parts = [
        dict(a=0, b=190, t=12, draw=lid, step="13", lines=["Lid: 3 mm walnut skin (outside only) · 12 mm laser frame · raw birch face", "the inner face is the canvas; the frame clears the knobs"]),
        dict(a=125, b=190, t=10, draw=hinge, step="14", lines=["Brass piano hinge (110 mm, straight tail) + captive folding stay", "stay detent at 100°; no half-open detent (can't fall on a hand)"]),
        dict(a=78, b=193, t=12, draw=caps, step=None, lines=["Knobs: bought skirted caps; the chartreuse hero is one bought cap", "painted or ordered in colour"]),
        dict(a=78, b=193, t=21, draw=ab, step="5", lines=["Panel sandwich: A over B cut to the curve (Edge.Cuts arc)", "rose grille over the Ø40 driver at the rear-left; 12 pip LEDs (11 on A + mod)"]),
        dict(a=0, b=190, t=27, draw=frame_draw([(0, 5), (76, 80), (185, 190)], 27, cork, (0, 190)), step="6",
             lines=["Body: ≈ 10 curved laser layers, cork-faced", "jacks follow board A's curved back edge"]),
        dict(a=0, b=80, t=14, draw=keybed, step="1", lines=["Keys: walnut lever tops, owner-cut at Vector Space; bone acrylic sharps", "on Choc V2 silent, magnet in the top over a TO-92 SS49E: reverse colours"]),
        dict(a=26, b=40, t=1.6, fill="#2e6b3a", step="2", lines=["Strip C = switch board: 25 Choc V2 + 25 standing SS49E", "#2765 stick + mod slide pot sit at the left (22 mm zone)"]),
        dict(a=4, b=78, t=9, fill="#3d6fae", step="3", lines=["Board D + 2 LiPo pouch cells under the keys", "away from the VCOs"]),
        dict(a=0, b=190, t=3, fill=cork, step="7", lines=["Base plate, screws; felt feet", "the outline follows the bentside"]),
    ]
    svg, yb = exploded(parts, s=s, x0=X0, y0=520, label_x=X0 + 200 * s + 60, gap=64)
    b = [head(90, 150, "MOTTO · how it goes together", "Exploded side view (from the right) at the spine, front at the left · 1 mm = 6.6 px",
              ["Same core as SLAB (keys, strip C, D and battery under the keys; A over B under the panel). What's new is",
               "the curved board edge, the rose, the hinge and stay, and the lid that comes off whole for painting.",
               "Numbers = build steps (15 in total)."],
              "Checked against eng v2 §4.1, §4.2 · answers E8 · budget-variant §v1.4b rev 6 · common-how-it-works §1, §5, §6"),
         svg, mm_ruler(X0, yb + 70, s, 190)]
    ay = yb + 230
    b.append(view_label(90, ay, "ASSEMBLED · lid up · same scale"))
    b.append(G(X0, ay + 1640, s, motto_side(p)))
    H = int(ay + 1730)
    return save(ROOT + "motto/motto-exploded.svg", 3000, H, "".join(b), p)


if __name__ == "__main__":
    print(motto_sheet()); print(motto_exploded())
