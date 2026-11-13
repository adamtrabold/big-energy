"""DOCK round-2 sheet + exploded. Body 300 x 136 x 32 (+15 mm wheel pod beside the panel: visual's push);
key module 300 x 100 x 33. Played 300 x 237, carried 300 x 136 x ~70."""
from r2s_common import *

BW = 300


def dock_top(p, night=False, docked=True):
    o = []
    # body
    o.append(f'<g filter="url(#shbig)"><rect x="0" y="0" width="{BW}" height="136" rx="5" '
             f'{body_fill(p) if not night else "fill=\"#0a0a0a\""}/></g>')
    if not night:
        # D strip under the top skin: vent slots
        for i in range(34):
            x = 24 + i * 7.6
            o.append(f'<rect x="{x:.1f}" y="10" width="4.2" height="16" rx="2" fill="#000" opacity="0.45"/>')
        o.append(txt(150, 31.2, "board D strip under the skin (E6): Picos, DACs, charger", 2.6, "#9aa6a3", font=UI_FONT))
    o.append(f'<rect x="16.4" y="32.4" width="282.2" height="102" rx="2.6" fill="#000" opacity="0.6"/>')
    o.append(G(17.5, 33.5, 1, panel(p, "dock", night, "none")))
    o.append(key_well(2.6, 66, 13.4, 66, night))
    o.append(bendmod_lead(3.2, 70, p, night, h=60, w=12.6))
    if not night:
        o.append(txt(9.5, 64.6, "mod · bend", 2.4, "#c9c9c9"))
    # module
    my = 137 if docked else 150
    o.append(f'<g filter="url(#shbig)"><rect x="0" y="{my}" width="{BW}" height="100" rx="5" '
             f'{body_fill(p) if not night else "fill=\"#0a0a0a\""}/></g>')
    if not night:
        for i in range(7):
            o.append(f'<rect x="{138+i*4:.1f}" y="{my+1.2}" width="2.4" height="2.4" rx="0.4" fill="url(#brassg)"/>')
        for x in (36, 258):
            o.append(f'<path d="M{x},{my} l3,4 h6 l3,-4 Z" fill="#000" opacity="0.7"/>')
        for x in (6, 294):
            o.append(f'<circle cx="{x}" cy="{my+50}" r="2.2" fill="#9a9a9a" stroke="#555" stroke-width="0.3"/>')
        o.append(txt(276, my + 6.2, NAME, 4.4, p["silk"], weight=700))
    o.append(key_well(18, my + 8, 264, 86, night))
    o.append(keys_lever(19.5, my + 10, p, night, wlen=80, blen=48))
    return "".join(o)


def dock_side_played(p):
    o = [part(0, -33, 100, 33, "#1d2423", "#000", 0.3, 3), part(101, -32, 136, 32, "#1d2423", "#000", 0.3, 3)]
    o.append(part(8, -32, 80, 3, p["nat"], "#555", 0.2))
    o.append(part(40, -35, 46, 3, p["sharp"], "#000", 0.2))
    o.append(part(101.5, -28.5, 100, 0.8, p["panel"], "#000", 0.1, 0))
    o.append(capsil(117, -28, 26, 12, p["hero"], 3))
    for x in (150, 164, 178, 192):
        o.append(capsil(x, -28, 12, 11, p["cap"], 2))
    o.append(part(99, -20, 3, 8, "url(#brassg)", rx=0.5))
    return "".join(o)


def dock_side_carried(p):
    o = [part(0, -32, 136, 32, "#1d2423", "#000", 0.3, 3)]
    o.append(part(2, -28.5, 100, 0.8, p["panel"], "#000", 0.1, 0))
    o.append(capsil(15, -28, 26, 12, p["hero"], 3))
    for x in (50, 64, 78, 92):
        o.append(capsil(x, -28, 12, 11, p["cap"], 2))
    # module flipped on top with a 9 mm skirt
    o.append(part(-1, -32 - 8 - 33, 102, 33, "#26302e", "#000", 0.3, 3))
    o.append(part(-1, -41, 3, 10, "#26302e", "#000", 0.3, 1))
    o.append(part(99, -41, 3, 10, "#26302e", "#000", 0.3, 1))
    o.append(part(10, -73 - 0, 80, 3, p["nat"], "#555", 0.2))
    return "".join(o)


def dock_sheet():
    p = PAL["desk"]
    H = 3800
    S = 8.0
    b = [head(90, 150, "DOCK", "Designed for use · the keyboard is its own lid (SX-70) · round 2",
              ["The key module drops onto two felt-lined cleats on the body's front (it falls into its notch like a harp",
               "pedal) and powers up. To carry, lift it, turn it over, lay it face-up on the panel. Because the module must",
               "be as deep as the panel it covers, DOCK gets the longest keys of the set: 80 mm whites (\"use an old idea\")."],
              "Look shown: Desk (smoked acrylic layers, black panel, gold rules, green cutoff). Light: none (V-b)"),
         placeholder(90, 590)]
    X0, Y0 = 90, 700
    b.append(view_label(X0, Y0 - 20, "PLAYING · module docked · top view · 1 mm = 8 px"))
    b.append(G(X0, Y0, S, dock_top(p)))
    b.append(dim_h(X0, X0 + BW * S, Y0 + 237 * S + 70, "300 mm  (285 + 15 mm wheel pod: see open question)", 26))
    b.append(dim_v(X0 + BW * S + 50, Y0, Y0 + 136 * S, "body 136", 24))
    b.append(dim_v(X0 + BW * S + 50, Y0 + 137 * S, Y0 + 237 * S, "module 100", 24))
    b.append(dim_v(X0 + BW * S + 250, Y0, Y0 + 237 * S, "237 mm played", 26))
    b.append(note(X0, Y0 + 237 * S + 150, [("Gold pads at the joint = the pogo face", 700), "VBAT ×2, GND ×2, TX, RX + short DETECT; pads dead until docked"], 23))
    b.append(note(X0 + 1300, Y0 + 237 * S + 150, [("Dark notches = two asymmetric cleats", 700), "felt-faced; the module drops in one way only, silently"], 23))
    RX = 3000
    bx, bh = box(RX, 120, 830, "Cost and build (R8)", [
        "Cost vs SLAB: +$15–25 (7 pogo pins ≥ 2 A,",
        "  gating MOSFET, pad board, cleats; no lid)",
        "Steps after soldering: 14",
        "Bought: Hall switches, knobs, caps, bend stick, mod fader",
        "Service-cut: 80 mm lever key tops (owner OK)"], 23)
    b.append(bx)
    bx2, bh2 = box(RX, 120 + bh + 24, 830, "Checked against", [
        "owner.md: \"portable…small\"; \"feel good to",
        "  use\"; 2 octaves; ready-made modules;",
        "  MIDI entries (knob-only = no MIDI, MIDI",
        "  can't flip switches); \"real parts\"; silent",
        "eng v2: §2, §4.1 (D stays with B), §4.2,",
        "  §5b (2.9 A worst case over the pogo pins)",
        "scores.md: R1, R3, R7, R8"], 23)
    b.append(bx2)
    ny = 1180
    b.append(view_label(RX, ny, "LIGHTS OFF · no pip (V-b)"))
    b.append(f'<rect x="{RX}" y="{ny+20}" width="{int(BW*2.6)+40}" height="{int(237*2.6)+40}" rx="10" fill="#050605"/>')
    b.append(G(RX + 20, ny + 40, 2.6, dock_top(p, night=True)))
    b.append(note(RX, ny + 720, ["No 'not in control' light. The status LED gives", "one amber flash when MIDI first takes a",
                                 "gold-ringed control. HOLD + TUNE takes all back.", "The quiet option."], 22))
    # sides
    sy = Y0 + 237 * S + 760
    ss = 5.2
    b.append(view_label(X0, sy - 470, "SIDE · played: one flat slab, 33 mm · 1 mm = 5.2 px"))
    b.append(G(X0 + 40, sy, ss, dock_side_played(p) + '<line x1="-6" y1="0" x2="245" y2="0" stroke="#999" stroke-width="0.4"/>'))
    b.append(lbl(X0 + 40, sy + 60, "← player · module | body · cleat + pogo face at the joint", 22, "#666"))
    cx = X0 + 1500
    b.append(view_label(cx, sy - 470, "SIDE · carried: module face-up on the panel"))
    b.append(G(cx + 40, sy, ss, dock_side_carried(p)))
    b.append(dim_v(cx + 40 + 140 * ss, sy - 73 * ss, sy, "≈ 70 mm", 24))
    b.append(lbl(cx + 40, sy + 60, "skirt sleeves over the body rim and hides the 8 mm cap gap; it can't remove it", 22, "#666"))
    # cleat detail
    dx = X0 + 2650
    b.append(view_label(dx, sy - 470, "THE SEAT · detail × 3"))
    det = (part(0, -32, 30, 32, "#1d2423", "#000", 0.3, 2) + part(31, -32, 30, 32, "#26302e", "#000", 0.3, 2)
           + f'<path d="M30,-6 l6,0 l0,-8 l-3,0 Z" fill="#c9a24e"/>' + part(28, -24, 3, 10, "url(#brassg)", rx=0.5)
           + f'<path d="M36,-14 l-3,0" stroke="#8b8780" stroke-width="1.2"/>')
    b.append(G(dx, sy, 9, det))
    b.append(note(dx, sy + 60, ["Cleat (gold) hooks a notch in the", "module's rear: gravity + end magnets", "seat it; felt faces; pogo pins above"], 22))
    ny2 = sy + 260
    b.append(note(X0, ny2, [("Systems' honest numbers, drawn", 700),
                            "Played 300 × 237 (over R1's 190: the module must cover a 100 mm panel).",
                            "Carried ≈ 70 thick; R3 asked under 45, floor is 56 (eng §4.2 stack + caps + module).",
                            "Same carry volume as SLAB (≈ 2.7 vs 2.4 L), best keys of the set."], 23))
    b.append(note(X0 + 1350, ny2, [("Bend stick + mod fader: pod beside the panel (visual's push)", 700),
                                   "Mod wheel is an analog pot (eng v2 §2) so it can't ride on the module.",
                                   "Systems put the pod inside 285 at the cost of the play group; I put it",
                                   "outside: +15 mm width, panel untouched. If eng takes E1, the pod moves to the module."], 23))
    b.append(note(X0 + 2650, ny2, [("Open", 700), "Accept DOCK over the box, or retire?", "Pogo pin rating ≥ 2 A (E6).",
                                   "80 mm levers on switches: feel UNVERIFIED.", "Knocked dock = reboot + re-tune."], 23))
    return save(ROOT + "dock/dock-mock.svg", W, H, "".join(b), p)


def dock_exploded():
    p = PAL["desk"]
    s = 6.0
    X0 = 120
    acr = "#2a3533"

    def caps(x0, y, s_):
        return caps_row(x0, y + 12 * s_, s_, [150, 164, 178, 192], p["cap"], hero_x=130, hero_col=p["hero"])

    def ab(x0, y, s_):
        o = f'<rect x="{x0+101*s_}" y="{y}" width="{100*s_}" height="{1.6*s_}" fill="{p["panel"]}" stroke="#555"/>'
        for x in (122, 150, 164, 178):
            o += f'<rect x="{x0+(x-4.5)*s_}" y="{y+1.6*s_}" width="{9*s_}" height="{7*s_}" rx="2" fill="#4a6fa5"/>'
        o += f'<rect x="{x0+101*s_}" y="{y+19.6*s_}" width="{100*s_}" height="{1.6*s_}" fill="#2e6b3a" stroke="#222"/>'
        for x in (106, 130, 160, 190):
            o += f'<rect x="{x0+x*s_}" y="{y+8.6*s_}" width="{1.2*s_}" height="{11*s_}" fill="#999"/>'
        o += f'<rect x="{x0+170*s_}" y="{y+1.6*s_}" width="{28*s_}" height="{10*s_}" rx="6" fill="#111" stroke="#555"/>'
        return o

    def keybed(x0, y, s_):
        return (f'<rect x="{x0+8*s_}" y="{y+5*s_}" width="{80*s_}" height="{4*s_}" rx="3" fill="{p["nat"]}" stroke="#333"/>'
                f'<rect x="{x0+40*s_}" y="{y+1*s_}" width="{46*s_}" height="{4*s_}" rx="3" fill="{p["sharp"]}"/>'
                f'<rect x="{x0+6*s_}" y="{y+9*s_}" width="{90*s_}" height="{4*s_}" rx="2" fill="#3a3a3a"/>')

    def pogo(x0, y, s_):
        return (f'<rect x="{x0+97*s_}" y="{y}" width="{3*s_}" height="{10*s_}" fill="url(#brassg)" stroke="#333"/>'
                f'<rect x="{x0+101*s_}" y="{y}" width="{4*s_}" height="{10*s_}" fill="#333"/>'
                f'<path d="M{x0+101*s_},{y+10*s_} l{-5*s_},0 l0,{4*s_} l{3*s_},0 Z" fill="#c9a24e"/>')

    parts = [
        dict(a=101, b=201, t=12, draw=caps, step=None, lines=["Knobs: bought skirted caps + 26 mm hero; fader caps", "last on"]),
        dict(a=101, b=201, t=21, draw=ab, step="5", lines=["Panel sandwich A over B (same panel PCB as SLAB)", "speaker Ø40 in the A/B notch, rear right"]),
        dict(a=202, b=233, t=12, fill="#3d6fae", step="4", lines=["Board D reshaped as a 270 × 30 strip behind A/B (E6)", "charger here, next to the single USB-C (E3)"]),
        dict(a=100, b=237, t=26, draw=frame_draw([(100, 103), (201, 203), (234, 237)], 26, acr, (100, 237)), step="6",
             lines=["Body frame: ≈ 9 laser-cut acrylic layers", "front face carries the pogo pins + 2 cleats"]),
        dict(a=95, b=106, t=14, draw=pogo, step="7", lines=["Dock face: 7 pogo pins (body) · ENIG pads + notch (module)", "brass cleats bolt through the front layers"]),
        dict(a=0, b=100, t=13, draw=keybed, step="1", lines=["Module keys: 80 mm service-cut lever tops on a bought pivot rod", "each over a bought Hall low-profile switch; felt stops"]),
        dict(a=55, b=70, t=1.6, fill="#2e6b3a", step="2", lines=["Switch board (strip C) + key Pico, in the module", "notes go to the body over UART"]),
        dict(a=6, b=96, t=8, fill="#c9a24e", step="3", lines=["2 LiPo pouch cells in the module", "VBAT crosses the dock on paired pins"]),
        dict(a=0, b=100, t=12, draw=frame_draw([(0, 3), (97, 100)], 12, acr, (0, 100)), step="8",
             lines=["Module shell: ≈ 5 layers + 9 mm skirt", "the skirt sleeves over the body when carried"]),
        dict(a=0, b=237, t=3, draw=lambda x0, y, s_: f'<rect x="{x0}" y="{y}" width="{100*s_}" height="{3*s_}" rx="3" fill="{acr}" stroke="#222"/><rect x="{x0+101*s_}" y="{y}" width="{136*s_}" height="{3*s_}" rx="3" fill="{acr}" stroke="#222"/>', step="9", lines=["Two base plates (body, module), screws", "battery swap: module base"]),
    ]
    svg, yb = exploded(parts, s=s, x0=X0, y0=500, label_x=X0 + 245 * s + 60, gap=62)
    b = [head(90, 150, "DOCK · how it goes together", "Exploded side view (from the right), module at the left (the player's side) · 1 mm = 6 px",
              ["Two separate builds that meet at one face. Only power and UART cross it (common §1 joint rule):",
               "never ±10 V, a DAC CV, an audio-path pot or audio. Numbers = build steps (14 in total)."],
              "Checked against eng v2 §4.1 (D stays with B), §4.2, §5b · common-how-it-works §1 · dock/how-it-works"),
         svg, mm_ruler(X0, yb + 70, s, 237)]
    ay = yb + 230
    b.append(view_label(90, ay, "ASSEMBLED · played · same scale"))
    b.append(G(X0, ay + 320, s, dock_side_played(p)))
    H = int(ay + 400)
    return save(ROOT + "dock/dock-exploded.svg", 3000, H, "".join(b), p)


if __name__ == "__main__":
    print(dock_sheet()); print(dock_exploded())
