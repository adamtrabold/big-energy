"""DOCK sheet: flat body + keyboard module that docks in front and flips on top as the lid. Look: Desk."""
from kit import *
from panels import panel_rect
from common_views import *

OUT = "/home/claude/model-d/design/instrument/concepts/dock/"


def body_top(p, night=False):
    o = [f'<g filter="url(#shbig)"><rect x="0" y="0" width="315" height="150" rx="5" '
         f'{body_fill(p) if not night else "fill=\"#0a0a0a\""}/></g>']
    if not night:  # acrylic gloss edge
        o.append('<rect x="0.6" y="0.6" width="313.8" height="148.8" rx="4.6" fill="none" stroke="#7f8f8b" stroke-width="0.5" opacity="0.6"/>')
    # sunken panel: inner shadow wall
    o.append('<rect x="4" y="4" width="307" height="142" rx="3" fill="#000" opacity="0.6"/>')
    o.append(G(5, 5, 1, panel_rect(p, night=night, light="none")))
    return "".join(o)


def sheet(p=PAL["desk"], fname="dock-mock"):
    W, H = 3800, 3260
    b = []
    b.append(title_block(90, 140, "DOCK", "Designed for use · the keyboard is its own lid (Polaroid SX-70)",
                         ["Play: the key module snaps to the body's front face (magnets + 6 pogo pins, MIDI-UART).",
                          "Carry: lift it, flip it, lay it face-up on the body — keys on top, panel sealed under it.",
                          "Flat panel, no hinge, no cable. Same panel PCB as CASE."],
                         f"Look shown: {p['name']} — smoked acrylic stack, black panel, gold rules, green cutoff", 30))
    b.append(placeholder_note(90, 520))
    s = 7.0
    X0, Y0 = 90, 600
    b.append(view_label(X0, Y0 - 12, "PLAYING — top view, real proportions (1 mm = 7 px)"))
    inner = body_top(p)
    base, ky = keys_base(p)
    inner += G(0, 153, 1, base)
    # dock seam: magnets + cones at the ends, pogo row in the middle
    for x in (18, 297):
        inner += f'<circle cx="{x}" cy="151.5" r="2.4" fill="#9aa" stroke="#333" stroke-width="0.3"/>'
    for i in range(6):
        inner += f'<rect x="{150+i*3}" y="150.6" width="1.4" height="2" fill="{p["gold"]}"/>'
    b.append(G(X0, Y0 + 20, s, inner))
    b.append(dim_h(X0, X0 + 315 * s, Y0 + 20 + 303 * s + 60, "315 mm"))
    b.append(dim_v(X0 + 315 * s + 40, Y0 + 20, Y0 + 20 + 150 * s, "body 150"))
    b.append(dim_v(X0 + 315 * s + 40, Y0 + 20 + 153 * s, Y0 + 20 + 303 * s, "module 150"))
    RX = 2470
    # side playing
    sx, sy = RX + 60, 1000
    b.append(view_label(RX, 660, "SIDE — playing (1 mm = 4 px)"))
    blay = [(3, "acrylic")] + [(3, "acrylic_hi"), (3, "acrylic")] * 7 + [(3, "acrylic_hi")]
    bs, btop = stack_side(150, 0, 150, blay)     # body behind (right)
    mlay = [(3, "acrylic")] + [(3, "acrylic_hi"), (3, "acrylic")] * 3 + [(3, "acrylic_hi")]
    ms, mtop = stack_side(0, 0, 148, mlay)       # module in front (left)
    keys = f'<rect x="12" y="{mtop-7}" width="92" height="7" fill="{p["nat"]}"/><rect x="14" y="{mtop-14}" width="55" height="7" fill="{p["sharp"]}"/>'
    caps = "".join(f'<rect x="{150+x}" y="{btop+18-h:.1f}" width="{w}" height="{h}" rx="1.5" fill="{c}"/>'
                   for x, h, w, c in [(8, 14, 40, p["hero"]), (56, 13, 16, p["cap"]), (82, 13, 16, p["cap"]),
                                      (108, 13, 16, p["cap"]), (130, 9, 7, p["cap"])])
    well = f'<rect x="153" y="{btop:.1f}" width="144" height="18" fill="#0d0f0f"/>'
    pogo = f'<rect x="147" y="{-20}" width="4" height="6" fill="{p["gold"]}"/>'
    b.append(G(sx, sy, 4, f'<line x1="-10" y1="0" x2="320" y2="0" stroke="#999" stroke-width="0.5"/>' + ms + keys + bs + well + caps + pogo))
    b.append(txt(sx - 10, sy + 50, "← player", 22, "#777", anchor="start", font=UI_FONT))
    b.append(dim_v(sx + 300 * 4 + 20, sy, sy + btop * 4, f"{-btop:.0f} mm"))
    b.append(dim_h(sx, sx + 1200, sy + 95, "played footprint ≈ 300 mm"))
    b.append(para(RX, sy + 160, ["Panel sunk 18 mm in the body rim; caps top out level with the rim.",
                                 "Gold = pogo pins on the body's front face (flat ENIG pads on the module)."], 22, "#444"))
    # side carry
    cy = 1720
    b.append(view_label(RX, 1340, "SIDE — carry (module flipped face-up on top)"))
    bs2, btop2 = stack_side(0, 0, 150, blay)
    mlay_r = list(reversed(mlay))
    # module is 28 tall overall: 12 mm deck + 16 mm rim at the ends; keys sit inside the rim
    ms2, mtop2 = stack_side(0, btop2, 150, [(3, "acrylic"), (3, "acrylic_hi"), (3, "acrylic"), (3, "acrylic_hi")])
    keys2 = f'<rect x="40" y="{mtop2-7:.1f}" width="92" height="7" fill="{p["nat"]}"/><rect x="60" y="{mtop2-14:.1f}" width="55" height="7" fill="{p["sharp"]}"/>'
    rimup = f'<rect x="0" y="{mtop2-16:.1f}" width="6" height="16" fill="#2a3533"/><rect x="144" y="{mtop2-16:.1f}" width="6" height="16" fill="#2a3533"/>'
    b.append(G(sx, cy, 4, f'<line x1="-10" y1="0" x2="170" y2="0" stroke="#999" stroke-width="0.5"/>' + bs2 + ms2 + keys2 + rimup))
    b.append(dim_v(sx + 160 * 4, cy, cy + (mtop2 - 16) * 4, f"≈ {-(mtop2-16):.0f} mm (est.)"))
    b.append(dim_h(sx, sx + 600, cy + 50, "150 mm"))
    b.append(para(RX, cy + 110, ["Keys ride on top, inside a rim 2 mm proud of the black keys:",
                                 "nothing flat can press them. Lid magnets at the ends → it sleeps."], 22, "#444"))
    # carry top view
    b.append(view_label(RX, 1950, "CARRY — top (keys up)"))
    ct, _ = keys_base(p)
    rim = '<rect x="0.5" y="0.5" width="314" height="149" rx="5" fill="none" stroke="#7f8f8b" stroke-width="0.8"/>'
    b.append(G(RX + 40, 2000, 3.0, ct + rim))
    # night inset
    nv = body_top(p, night=True) + G(0, 153, 1, keys_base(p, night=True)[0])
    b.append(view_label(RX, 2530, "LIGHTS OFF"))
    b.append(f'<rect x="{RX}" y="2550" width="{int(315*2.1)+40}" height="{int(303*2.1)+40}" rx="10" fill="#050605"/>')
    b.append(G(RX + 20, 2570, 2.1, nv))
    b.append(para(RX + 760, 2600, [("“Not in control”: none.", 700), "This concept tests the", "no-light option: the status",
                                   "LED flashes amber once when", "MIDI first takes a knob.", "HOLD + TUNE hands every", "knob back."], 22, "#444"))
    open(OUT + fname + ".svg", "w").write(svg_doc(W, H, "".join(b), p))
    return OUT + fname + ".svg"


if __name__ == "__main__":
    print(sheet())
