"""CASE sheet: clamshell, panel is the lid (designed for use). Look: Field."""
import math, sys
from kit import *
from panels import panel_rect
from common_views import *

OUT = "/home/claude/model-d/design/instrument/concepts/case/"


def case_top_open(p, night=False, light_on=True):
    """Played top view, local mm: lid (panel) at top, hinge, base with keys at bottom."""
    o = []
    # lid: 315 x 150, panel inset 5 (top view; 15 deg tilt foreshortens <4 %, ignored)
    lid = (f'<g filter="url(#shbig)"><rect x="0" y="0" width="315" height="150" rx="5" '
           f'{body_fill(p) if not night else "fill=\"#0a0a0a\""}/></g>')
    o.append(lid)
    o.append(G(5, 5, 1, panel_rect(p, night=night, light="pip", light_on=light_on)))
    # hinge knuckles
    for x in (30, 140, 255):
        o.append(f'<rect x="{x}" y="150" width="30" height="7" rx="2" fill="url(#brassg)"/>')
    base, ky = keys_base(p, night=night)
    o.append(G(0, 157, 1, base))
    return "".join(o), 157 + 150


def side_open(p, s):
    """Side elevation, open/playing. Player on the left. Returns svg in px (scale s)."""
    o = []
    base_layers = [(3, "cork")] + [(3, "ply_grey")] * 8 + [(2, "felt2"), (1.6, "pcb_black")]
    b, top = stack_side(0, 0, 150, base_layers)
    o.append(b)
    # keys on base (side): white key profile + black key bump
    o.append(f'<rect x="10" y="{top-8}" width="92" height="8" fill="{p["nat"]}" stroke="#0004" stroke-width="0.2"/>')
    o.append(f'<rect x="12" y="{top-16}" width="55" height="8" fill="{p["sharp"]}" />')
    # lid: hinge at (150, top); lid local frame: x along lid from hinge, outer face at y=0, panel on top
    lid_layers = [(3, "felt")] + [(3, "ply_grey")] * 7 + [(2, "felt2"), (1.6, "pcb_black")]
    lid2, l2top = stack_side(0, 0, 150, lid_layers)
    caps2 = ""
    for x, h, w, col in [(8, 14, 40, p["hero"]), (56, 13, 16, p["cap"]), (80, 13, 16, p["cap"]),
                         (104, 13, 16, p["cap"]), (126, 9, 7, p["cap"])]:
        caps2 += f'<rect x="{x}" y="{l2top-h:.2f}" width="{w}" height="{h}" rx="1.5" fill="{col}"/>'
    o.append(f'<g transform="translate(150,{top:.2f}) rotate(-15)">{lid2}{caps2}</g>')
    # hinge pin
    o.append(f'<circle cx="150" cy="{top}" r="3.5" fill="url(#brassg)" stroke="#5a4515" stroke-width="0.4"/>')
    # rear leg from lid far end down to table
    fx = 150 + 150 * math.cos(math.radians(15)) - 12
    fy = top - 150 * math.sin(math.radians(15)) + 6
    o.append(f'<line x1="{fx:.1f}" y1="{fy:.1f}" x2="{fx+6:.1f}" y2="0" stroke="#7d7a74" stroke-width="5" stroke-linecap="round"/>')
    return "".join(o), top, fx


def side_closed(p):
    o = []
    base_layers = [(3, "cork")] + [(3, "ply_grey")] * 8 + [(2, "felt2"), (1.6, "pcb_black")]
    b, top = stack_side(0, 0, 150, base_layers)
    o.append(b)
    lid_layers = [(2, "felt2")] + [(3, "ply_grey")] * 9 + [(3, "felt")]
    l, ltop = stack_side(0, top, 150, lid_layers)
    o.append(l)
    o.append(f'<rect x="-2" y="{top-6:.1f}" width="4" height="12" fill="url(#brassg)"/>')
    return "".join(o), ltop


def build(p=PAL["field"], fname="case-mock"):
    W, H = 3800, 3160
    body = []
    body.append(title_block(90, 140, "CASE", "Designed for use · clamshell, the panel is the lid",
                            ["Opens like a theodolite case: plain outside, the reveal is the event.",
                             "Lid swings back to a hard stop at 15°, a fold-out leg takes the knob pressure.",
                             "Keys in the base (25 lever keys, silent, Hall-sensed). Speaker in the lid, far right."],
                            f"Look shown: {p['name']} — warm-grey felt + cork stack, black panel, gold rules, orange cutoff", 30))
    body.append(placeholder_note(90, 520))
    s = 7.0
    tv, depth = case_top_open(p)
    X0, Y0 = 90, 580
    body.append(view_label(X0, Y0 - 12 + 0, "PLAYING — top view, real proportions (1 mm = 7 px)"))
    body.append(G(X0, Y0 + 20, s, tv))
    # dims
    body.append(dim_h(X0, X0 + 315 * s, Y0 + 20 + depth * s + 60, "315 mm"))
    body.append(dim_v(X0 + 315 * s + 40, Y0 + 20, Y0 + 20 + 150 * s, "lid 150"))
    body.append(dim_v(X0 + 315 * s + 40, Y0 + 20 + 157 * s, Y0 + 20 + 307 * s, "base 150"))
    # right column
    RX = 2470
    # side open
    so, top, fx = side_open(p, 4)
    sx, sy = RX + 60, 1030
    body.append(view_label(RX, 660, "SIDE — playing (1 mm = 4 px)"))
    body.append(G(sx, sy, 4, f'<line x1="-10" y1="0" x2="330" y2="0" stroke="#999" stroke-width="0.5"/>' + so))
    body.append(txt(sx - 10, sy + 50, "← player", 22, "#777", anchor="start", font=UI_FONT))
    body.append(dim_h(sx, sx + int((fx + 8) * 4), sy + 95, "open footprint ≈ 300 mm"))
    body.append(para(RX, sy + 160, ["Hard stop at 165° + fold-out leg: one playing angle, no friction",
                                    "hinge to creep. Pressing knobs pushes into the stop and the leg."], 22, "#444"))
    # side closed
    sc, ctop = side_closed(p)
    cy = 1640
    body.append(view_label(RX, 1340, "SIDE — closed / carry"))
    body.append(G(sx, cy, 4, f'<line x1="-10" y1="0" x2="170" y2="0" stroke="#999" stroke-width="0.5"/>' + sc))
    body.append(dim_v(sx + 160 * 4, cy, cy + ctop * 4, f"≈ {-ctop:.0f} mm (est.)", side=1))
    body.append(dim_h(sx, sx + 600, cy + 50, "150 mm"))
    body.append(para(RX, cy + 110, ["Low caps (hero 14 mm, others 13 mm) keep the knob pocket at",
                                    "18 mm instead of 24 — about 6 mm thinner closed."], 22, "#444"))
    # closed top
    ct = []
    ct.append(f'<g filter="url(#shbig)"><rect x="0" y="0" width="315" height="150" rx="5" {body_fill(p)}/></g>')
    ct.append(f'<rect x="6" y="6" width="303" height="138" rx="3" fill="none" stroke="#0003" stroke-width="0.6"/>')
    ct.append(txt(157, 82, NAME, 14, "#2b2a27", weight=700))
    ct.append(f'<rect x="140" y="146" width="35" height="6" rx="2" fill="url(#brassg)"/>')
    for x in (30, 140, 255):
        ct.append(f'<rect x="{x}" y="-5" width="30" height="5" rx="2" fill="url(#brassg)"/>')
    ct.append(f'<circle cx="157" cy="118" r="4" fill="url(#brassg)"/>')
    body.append(view_label(RX, 1880, "CLOSED — top (lid outside)"))
    body.append(G(RX + 40, 1930, 3.0, "".join(ct)))
    body.append(para(RX + 1000, 1950, ["brass catch", "(front)", "", "tripod insert", "under base"], 20, "#666"))
    # night inset
    nv, _ = case_top_open(p, night=True, light_on=True)
    body.append(view_label(RX, 2450 - 20, "LIGHTS OFF — glow pointers + sharp fronts"))
    body.append(f'<rect x="{RX}" y="2450" width="{int(315*2.1)+40}" height="{int(307*2.1)+40}" rx="10" fill="#050605"/>')
    body.append(G(RX + 20, 2470, 2.1, nv))
    # callouts on main view
    def mm(x, y):
        return X0 + x * s, Y0 + 20 + y * s
    cx, cy2 = mm(33.5, 108)
    body.append(callout(cx - 150, cy2 + 40, 40, cy2 + 260, [], 24, dot=False) if False else "")
    out = svg_doc(W, H, "".join(body), p)
    open(OUT + fname + ".svg", "w").write(out)
    return OUT + fname + ".svg"


if __name__ == "__main__":
    print(build())
