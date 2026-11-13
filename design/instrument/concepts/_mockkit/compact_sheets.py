"""OP-1-class (282 mm) mocks for CASE, DOCK, MOTTO, DISH + look sheet + size sheet."""
import math, random, sys
from kit import *
from compact import *
from common_views import NAME, title_block, placeholder_note, view_label, G

ROOT = "/home/claude/model-d/design/instrument/concepts/"
OP1 = (282, 102, 13.5)   # teenage.engineering product page: L 282, H 102, D 13.5 mm
S = 9.0                  # main view: 1 mm = 9 px
W = 3900


def save(path, w, h, body, p):
    open(path, "w").write(svg_doc(w, h, body, p))
    return path


def size_note(x, y, lines):
    return para(x, y, lines, 24, "#7a3b12")


def panel_half(p, night=False, light="pip", light_on=True, mat=None, sunk=False):
    o = [f'<g filter="url(#shbig)"><rect x="0" y="0" width="{HW}" height="{HD}" rx="4" '
         f'{body_fill(p, mat) if not night else "fill=\"#0a0a0a\""}/></g>']
    if sunk:
        o.append(f'<rect x="2" y="2" width="{HW-4}" height="{HD-4}" rx="3" fill="#000" opacity="0.6"/>')
    o.append(G(3, 3, 1, panel_compact(p, night, light, light_on)))
    return "".join(o)


def caps_side(x0, y_face, p, flip=False):
    """Little cap silhouettes on a panel face at y_face (upwards)."""
    items = [(4, 12, 24, p["hero"]), (34, 11, 10.5, p["cap"]), (52, 11, 10.5, p["cap"]), (70, 7, 5, p["cap"])]
    o = ""
    for x, h, w, c in items:
        xx = x0 + (76 - x - w if flip else x)
        o += f'<rect x="{xx}" y="{y_face-h}" width="{w}" height="{h}" rx="1.2" fill="{c}"/>'
    return o


# ------------------------------------------------------------------ CASE
def case_c(p=PAL["field"]):
    H = 2950
    b = [title_block(90, 140, "CASE", "Designed for use · clamshell; the panel is the lid · OP-1 width",
                     ["Closed it is a 282 × 76 mm block, about the size of a hardcover book. Open, the lid swings back",
                      "to a hard stop at 15° with a fold-out leg. Keys: short Delrin flexure levers (real travel, silent).",
                      "Panel at eurorack density (Plaits / Rings sized caps), the one hero is the 24 mm cutoff."],
                     f"Look shown: {p['name']} — warm-grey felt + cork stack, black panel, gold rules, orange cutoff", 28),
         placeholder_note(90, 520)]
    X0, Y0 = 90, 620
    tv = panel_half(p) + "".join(f'<rect x="{x}" y="76" width="24" height="5" rx="1.5" fill="url(#brassg)"/>' for x in (24, 129, 234))
    tv += G(0, 81, 1, key_strip(p, "lever"))
    b.append(view_label(X0, Y0 - 14, "PLAYING — top view, real size × 9 (1 mm = 9 px)"))
    b.append(G(X0, Y0, S, tv))
    b.append(dim_h(X0, X0 + 282 * S, Y0 + 157 * S + 60, "282 mm  (OP-1: 282)"))
    b.append(dim_v(X0 + 282 * S + 40, Y0, Y0 + 76 * S, "lid 76"))
    b.append(dim_v(X0 + 282 * S + 40, Y0 + 81 * S, Y0 + 157 * S, "keys 76"))
    # sides
    sy = 2660; ss = 5.5
    b.append(view_label(X0, 2170, "SIDE — playing (1 mm = 5.5 px)"))
    base, top = stack_side(0, 0, 76, [(3, "cork")] + [(3, "ply_grey")] * 5 + [(2, "felt2"), (1.6, "pcb_black")])
    keys = f'<rect x="4" y="{top-6:.1f}" width="52" height="6" fill="{p["nat"]}"/><rect x="5" y="{top-11:.1f}" width="31" height="5" fill="{p["sharp"]}"/>'
    lid, lt = stack_side(0, 0, 76, [(3, "felt")] + [(3, "ply_grey")] * 7 + [(2, "felt2"), (1.6, "pcb_black")])
    lidg = f'<g transform="translate(76,{top:.1f}) rotate(-15)">{lid}{caps_side(0, lt, p)}</g>'
    fx = 76 + 76 * math.cos(math.radians(15)) - 6
    fy = top - 76 * math.sin(math.radians(15)) + 4
    leg = f'<line x1="{fx:.1f}" y1="{fy:.1f}" x2="{fx+3:.1f}" y2="0" stroke="#7d7a74" stroke-width="2.6" stroke-linecap="round"/>'
    pin = f'<circle cx="76" cy="{top:.1f}" r="2" fill="url(#brassg)"/>'
    b.append(G(X0 + 30, sy, ss, '<line x1="-6" y1="0" x2="160" y2="0" stroke="#999" stroke-width="0.4"/>' + base + keys + lidg + pin + leg))
    b.append(txt(X0 + 20, sy + 40, "← player", 22, "#777", anchor="start", font=UI_FONT))
    b.append(dim_h(X0 + 30, X0 + 30 + 152 * ss, sy + 80, "open ≈ 152 mm deep"))
    # closed side
    cx0 = X0 + 1150
    b.append(view_label(cx0, 2170, "SIDE — closed"))
    cb, ct = stack_side(0, 0, 76, [(3, "cork")] + [(3, "ply_grey")] * 5 + [(2, "felt2"), (1.6, "pcb_black")])
    cl, clt = stack_side(0, ct, 76, [(2, "felt2")] + [(3, "ply_grey")] * 8 + [(3, "felt")])
    b.append(G(cx0 + 20, sy, ss, '<line x1="-6" y1="0" x2="84" y2="0" stroke="#999" stroke-width="0.4"/>' + cb + cl
               + f'<rect x="-1.5" y="{ct-4:.1f}" width="3" height="8" fill="url(#brassg)"/>'))
    b.append(dim_v(cx0 + 20 + 76 * ss + 20, sy, sy + clt * ss, f"≈ {-clt:.0f} mm (est.)"))
    b.append(dim_h(cx0 + 20, cx0 + 20 + 76 * ss, sy + 80, "76 mm"))
    b.append(size_note(cx0 + 700, 2300, ["Not OP-1 slim (13.5 mm).", "Real pots + jacks + keys", "with travel set the floor:",
                                         "≈ 50 closed, ≈ 22 base.", "Assumes a flat LiPo pouch,", "not 18650s (eng)."]))
    # right column: carry + night
    RX = 2840
    b.append(view_label(RX, 606, "CARRY — top (lid outside), 1 mm = 3.4 px"))
    ct_ = [f'<g filter="url(#shbig)"><rect width="282" height="76" rx="4" {body_fill(p)}/></g>',
           txt(141, 44, NAME, 10, "#2b2a27", weight=700), f'<rect x="126" y="74" width="30" height="4" rx="1.5" fill="url(#brassg)"/>']
    b.append(G(RX, 640, 3.4, "".join(ct_)))
    b.append(txt(RX, 640 + 76 * 3.4 + 50, "282 × 76 × ≈ 50 mm · fits a laptop sleeve pocket", 24, "#333", anchor="start", font=UI_FONT))
    nv = panel_half(p, night=True) + G(0, 81, 1, key_strip(p, "lever", night=True))
    b.append(view_label(RX, 1080, "LIGHTS OFF"))
    b.append(f'<rect x="{RX}" y="1100" width="{int(282*3.4)+40}" height="{int(157*3.4)+40}" rx="10" fill="#050605"/>')
    b.append(G(RX + 20, 1120, 3.4, nv))
    b.append(para(RX, 1760, [("Key idea: short lever keys", 700),
                             "Laser-cut Delrin comb, each key a flexure tongue;",
                             "17.4 mm white pitch (OP-1-wide 2 octaves),",
                             "52 mm whites, 31 mm sharps, ~5 mm travel, felt stop.",
                             "Sensing sits on its own thin key strip, not the",
                             "main boards.", "",
                             ("“Not in control”: one amber pip", 700),
                             "Beside the cutoff hero (shown lit). With MIDI",
                             "control now limited to a few parameters, it only",
                             "ever means cutoff or glide."], 24, "#333"))
    return save(ROOT + "case/case-mock.svg", W, H, "".join(b), p)


# ------------------------------------------------------------------ DOCK
def dock_c(p=None):
    p = dict(PAL["desk"]); p.update(pillow_nat="#2a2e2d", pillow_sharp="#3f6b57")
    H = 2950
    b = [title_block(90, 140, "DOCK", "Designed for use · the key module is its own lid (Polaroid SX-70) · OP-1 width",
                     ["Play: the key module snaps to the body's front (magnets + pogo pins). Carry: flip it face-up onto",
                      "the sunken panel. Keys: one soft TPU sheet of pillow keys over magnets — silent, squashy, real",
                      "travel (~4 mm), printable in NinjaFlex at the makerspace. Same panel as CASE."],
                     f"Look shown: Desk — smoked acrylic stack, black panel, gold rules, green cutoff, TPU keys", 28),
         placeholder_note(90, 520)]
    X0, Y0 = 90, 620
    tv = panel_half(p, light="none", sunk=True)
    tv += G(0, 79, 1, key_strip(p, "pillow"))
    for x in (12, 270):
        tv += f'<circle cx="{x}" cy="77.5" r="1.6" fill="#9aa" stroke="#333" stroke-width="0.25"/>'
    for i in range(6):
        tv += f'<rect x="{134+i*2.6}" y="76.6" width="1.2" height="1.8" fill="{p["gold"]}"/>'
    b.append(view_label(X0, Y0 - 14, "PLAYING — top view, real size × 9"))
    b.append(G(X0, Y0, S, tv))
    b.append(dim_h(X0, X0 + 282 * S, Y0 + 155 * S + 60, "282 mm"))
    b.append(dim_v(X0 + 282 * S + 40, Y0, Y0 + 76 * S, "body 76"))
    b.append(dim_v(X0 + 282 * S + 40, Y0 + 79 * S, Y0 + 155 * S, "module 76"))
    sy = 2660; ss = 5.5
    b.append(view_label(X0, 2170, "SIDE — playing (flat, 30 mm)"))
    blay = [(3, "acrylic"), (3, "acrylic_hi")] * 5
    bs, bt = stack_side(78, 0, 76, blay)
    ms, mt = stack_side(0, 0, 76, [(3, "acrylic"), (3, "acrylic_hi")] * 3 + [(3, "acrylic")])
    keys = f'<rect x="4" y="{mt-4:.1f}" width="52" height="4" rx="1.5" fill="#2a2e2d"/><rect x="5" y="{mt-8:.1f}" width="31" height="4" rx="1.5" fill="#3f6b57"/>'
    well = f'<rect x="80" y="{bt:.1f}" width="72" height="12" fill="#0d0f0f"/>' + caps_side(78, bt + 12, p)
    b.append(G(X0 + 30, sy, ss, '<line x1="-6" y1="0" x2="162" y2="0" stroke="#999" stroke-width="0.4"/>' + ms + keys + bs + well
               + f'<rect x="76" y="-14" width="2" height="4" fill="{p["gold"]}"/>'))
    b.append(txt(X0 + 20, sy + 40, "← player", 22, "#777", anchor="start", font=UI_FONT))
    b.append(dim_v(X0 + 30 + 154 * ss + 20, sy, sy + bt * ss, f"{-bt:.0f} mm"))
    cx0 = X0 + 1150
    b.append(view_label(cx0, 2170, "SIDE — carry (module on top, keys up)"))
    cb, ct = stack_side(0, 0, 76, blay)
    cm, cmt = stack_side(0, ct, 76, [(3, "acrylic_hi"), (3, "acrylic"), (3, "acrylic_hi")])
    rim = f'<rect x="0" y="{cmt-13:.1f}" width="3" height="13" fill="#2a3533"/><rect x="73" y="{cmt-13:.1f}" width="3" height="13" fill="#2a3533"/>'
    ck = f'<rect x="12" y="{cmt-6:.1f}" width="52" height="6" rx="1.5" fill="#2a2e2d"/><rect x="18" y="{cmt-11:.1f}" width="31" height="5" rx="1.5" fill="#3f6b57"/>'
    b.append(G(cx0 + 20, sy, ss, '<line x1="-6" y1="0" x2="84" y2="0" stroke="#999" stroke-width="0.4"/>' + cb + cm + rim + ck))
    b.append(dim_v(cx0 + 20 + 76 * ss + 20, sy, sy + (cmt - 13) * ss, f"≈ {-(cmt-13):.0f} mm (est.)"))
    b.append(size_note(cx0 + 700, 2300, ["Played it is one flat 30 mm", "slab, 282 × 155 — the closest", "to OP-1 feel of the four.",
                                         "Carry ≈ 52 mm (est.)."]))
    RX = 2840
    b.append(view_label(RX, 606, "CARRY — top (keys up)"))
    b.append(G(RX, 640, 3.4, key_strip(p, "pillow") + '<rect x="0.4" y="0.4" width="281.2" height="75.2" rx="4" fill="none" stroke="#7f8f8b" stroke-width="0.6"/>'))
    nv = panel_half(p, night=True, light="none", sunk=True) + G(0, 79, 1, key_strip(p, "pillow", night=True))
    b.append(view_label(RX, 1080, "LIGHTS OFF"))
    b.append(f'<rect x="{RX}" y="1100" width="{int(282*3.4)+40}" height="{int(155*3.4)+40}" rx="10" fill="#050605"/>')
    b.append(G(RX + 20, 1120, 3.4, nv))
    b.append(para(RX, 1760, [("Key idea: pillow keys", 700),
                             "One printed TPU (NinjaFlex) sheet, piano layout,",
                             "a magnet in each pillow over a Hall sensor.",
                             "Soft landing, no click, ~4 mm travel; sharps raised",
                             "and tinted. Feel is tunable by print infill.",
                             "Risk: may read as 'pad', not 'key' — needs a",
                             "printed sample in the owner's hands.", "",
                             ("“Not in control”: none", 700),
                             "Status LED flashes amber once when MIDI takes",
                             "a parameter. HOLD + TUNE hands it back."], 24, "#333"))
    return save(ROOT + "dock/dock-mock.svg", W, H, "".join(b), p)


# ------------------------------------------------------------------ MOTTO
MD = 193            # depth at the spine
TAIL = 44           # tail strip behind the panel (rose + hinge)


def motto_outline(i=0):
    return (f"M{i},{MD-i} L{i},{i} L100,{i} C165,{i} 200,{TAIL-2+i*0.4} {282-i},{TAIL+i} L{282-i},{MD-i} Z")


def motto_top(p, night=False):
    o = [f'<g filter="url(#shbig)"><path d="{motto_outline()}" {body_fill(p) if not night else "fill=\"#0a0a0a\""}/></g>']
    o.append(f'<clipPath id="mpc"><path d="{motto_outline(3)}"/></clipPath>')
    o.append(f'<rect x="0" y="0" width="282" height="{MD-76}" fill="{"#050505" if night else p["panel"]}" clip-path="url(#mpc)"/>')
    if night:
        o.append(f'<circle cx="46" cy="23" r="19" fill="#070707"/>')
    else:
        o.append(grille(46, 23, 18, p, "rose"))
        o.append(f'<path d="{motto_outline(5.5)}" fill="none" stroke="{p["gold"]}" stroke-width="0.3" stroke-dasharray="1 1" opacity="0.7"/>')
        o.append(txt(132, 37, NAME, 7.5, p["silk"], weight=700))
    o.append(G(3, TAIL + 3, 1, panel_compact(p, night, light="perknob", light_on=True, grille_on=False)
               .replace(f'<rect x="0" y="0" width="{PW}" height="{PH}" rx="2" fill="{p["panel"]}"/>', "")))
    o.append(G(0, MD - 76, 1, key_strip(p, "tongue", night=night, reverse=True, bg=False)))
    o.append(f'<rect x="5" y="-2" width="92" height="2.6" fill="url(#brassg)"/>')
    return "".join(o)


def painting():
    return f"""
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#1f2a4a"/><stop offset="0.45" stop-color="#6b4f7a"/>
  <stop offset="0.75" stop-color="#e08a5a"/><stop offset="1" stop-color="#f2c27a"/></linearGradient>
 <filter id="paint"><feTurbulence type="fractalNoise" baseFrequency="0.06" numOctaves="2" seed="5"/><feDisplacementMap in="SourceGraphic" scale="5"/></filter></defs>
<rect width="282" height="{MD}" fill="url(#sky)"/>
<circle cx="190" cy="128" r="20" fill="#ffd69a" opacity="0.9" filter="url(#paint)"/>
<path d="M0,135 C55,112 100,132 145,120 C190,110 235,128 282,113 L282,{MD} L0,{MD} Z" fill="#3c2f4f" filter="url(#paint)"/>
<path d="M0,155 C60,140 110,158 170,147 C215,140 250,150 282,145 L282,{MD} L0,{MD} Z" fill="#26203a" filter="url(#paint)"/>
<path d="M30,28 C110,14 180,14 252,28 L246,46 C180,34 110,34 36,46 Z" fill="#efe3c6" opacity="0.92" filter="url(#paint)"/>
<text x="141" y="38" font-family="{LEG_FONT}" font-size="10" fill="#5a2a1e" text-anchor="middle" font-weight="700">[ your motto here ]</text>"""


def motto_c():
    p = dict(PAL["desk"])
    p.update(name="Motto", body_top="#5b3a26", body_mat="walnut", hero="#c8341f", hero_hi="#e2624b", hero_lo="#8d2112",
             signal="#c8341f", led="#c8341f", hole="#3a2a20", bg="#efe9df")
    H = 3150
    b = [title_block(90, 140, "MOTTO", "Sauce · a tiny harpsichord with a painted lid · OP-1 width, deeper",
                     ["The standard compact panel plus a harpsichord tail at the back-left: the tail holds the speaker as a",
                      "carved rose and the lid's hinge. The lid stands up behind as a painted backdrop that faces you and",
                      "reflects the speaker. Keys: laser-cut walnut tongues, reverse colours (dark naturals, bone sharps)."],
                     "Look shown: walnut stack, black panel, gold rules, vermilion cutoff · lid painting is a placeholder", 28),
         placeholder_note(90, 520)]
    X0, Y0 = 90, 640
    b.append(view_label(X0, Y0 - 34, "PLAYING — top view, real size × 9 (lid stands behind, see right)"))
    b.append(G(X0, Y0, S, motto_top(p)))
    b.append(dim_h(X0, X0 + 282 * S, Y0 + MD * S + 60, "282 mm"))
    b.append(dim_v(X0 + 282 * S + 40, Y0, Y0 + MD * S, f"{MD} at the spine"))
    b.append(dim_v(X0 + 282 * S + 40 + 0, Y0 + TAIL * S, Y0 + TAIL * S + 1, ""))
    RX = 2840
    fs = 3.3
    b.append(view_label(RX, 606, "FROM THE PLAYER — lid up (1 mm = 3.3 px)"))
    lh = MD * math.cos(math.radians(10))
    fy = 640 + (30 + lh) * fs
    lidpath = f"M0,0 L282,0 L282,{MD-TAIL} C200,{MD-TAIL+2} 165,{MD} 100,{MD} L0,{MD} Z"
    fe = (f'<g transform="translate(0,{-30-lh:.1f}) scale(1,{math.cos(math.radians(10)):.4f})"><clipPath id="lc"><path d="{lidpath}"/></clipPath>'
          f'<g clip-path="url(#lc)">{painting()}</g><path d="{lidpath}" fill="none" stroke="#3b2618" stroke-width="2.4"/></g>')
    st, _ = stack_side(0, 0, 282, [(3, "walnut")] * 10)
    fe += st + "".join(f'<rect x="{18+i*17.4+0.4:.1f}" y="-22" width="16.6" height="6" fill="#3a2416" stroke="#000" stroke-width="0.3"/>' for i in range(15))
    b.append(G(RX + 10, fy, fs, fe + '<line x1="-10" y1="0" x2="292" y2="0" stroke="#999" stroke-width="0.6"/>'))
    b.append(txt(RX + 10 + 141 * fs, fy + 50, "PLACEHOLDER — the owner's canvas, ≈ 282 × 193 mm", 22, "#9a5b2a", font=UI_FONT, weight=600))
    b.append(dim_v(RX + 10 + 290 * fs, fy, fy - (30 + lh) * fs, f"≈ {30+lh:.0f} mm"))
    sy = 1700 + 560; ss = 2.8
    b.append(view_label(RX, 1720, "SIDE (from the right) — playing / closed"))
    se, t2 = stack_side(0, 0, MD, [(3, "walnut")] * 10)
    se += f'<g transform="translate({MD},{t2}) rotate(-80)"><rect width="{MD}" height="6" fill="#5b3a26" filter="url(#grainf)"/></g>'
    se += f'<line x1="{MD-50}" y1="{t2}" x2="{MD+8}" y2="{t2-95}" stroke="#b8933f" stroke-width="1.6"/>'
    b.append(G(RX + 40, sy, ss, se + f'<line x1="-6" y1="0" x2="{MD+40}" y2="0" stroke="#999" stroke-width="0.5"/>'))
    b.append(txt(RX + 30, sy + 36, "← player", 22, "#777", anchor="start", font=UI_FONT))
    sc, t3 = stack_side(0, 0, MD, [(3, "walnut")] * 10)
    sc += f'<rect x="0" y="{t3-6}" width="{MD}" height="6" fill="#5b3a26" filter="url(#grainf)"/>'
    b.append(G(RX + 40, sy + 200, ss, sc))
    b.append(dim_v(RX + 40 + MD * ss + 20, sy + 200, sy + 200 - 36 * ss, "≈ 36 mm closed (est.)"))
    b.append(para(RX + 700, 2000, ["Captive brass stay holds", "the lid at 100°.", "Speaker → lid → you."], 22, "#444"))
    # bottom-left: night + notes
    ny = Y0 + MD * S + 150
    nv = motto_top(p, night=True)
    b.append(view_label(X0, ny, "LIGHTS OFF"))
    b.append(f'<rect x="{X0}" y="{ny+20}" width="{int(282*2.6)+40}" height="{int(MD*2.6)+40}" rx="10" fill="#050605"/>')
    b.append(G(X0 + 20, ny + 40, 2.6, nv))
    b.append(para(X0 + 830, ny + 40, [("Key idea: walnut tongue keys", 700),
                                      "One laser-cut sheet of walnut ply; every key is a",
                                      "tongue that flexes from the uncut root (kalimba ×",
                                      "harpsichord). Bone sharps glued on top.",
                                      "Risk: wood fatigue at the root — Delrin core with",
                                      "a walnut veneer face is the safe version.", "",
                                      ("“Not in control”: per-control pips", 700),
                                      "With only cutoff and glide MIDI-ownable now, a pip",
                                      "beside each of them is affordable and exact.",
                                      "(Was five section pips at 315 mm.)"], 24, "#333"))
    b.append(size_note(X0 + 1700, ny + 40, ["Breaks OP-1 depth:", "193 mm at the spine (1.9×).", "The tail is the price of", "the silhouette and the rose."]))
    return save(ROOT + "motto/motto-mock.svg", W, H, "".join(b), p)


# ------------------------------------------------------------------ DISH
R, RC, CX, CY = 55, 58, 141, 62
BD = CY + RC + 3 + 66      # 189
ARM = 50
FS_, FV_ = math.sin(math.radians(40)), math.cos(math.radians(40))


def dish_face_c(p, night=False, light_on=True):
    o = []
    if night:
        o.append(f'<circle r="{R}" fill="#060606"/>')
    else:
        o.append(f'<circle r="{R}" fill="{p["panel"]}" stroke="#5b3a26" stroke-width="1.6"/>')
        def arc(a0, a1, r):
            x0, y0 = pol(0, 0, r, a0); x1, y1 = pol(0, 0, r, a1)
            return f'M{x0:.2f},{y0:.2f} A{r},{r} 0 {1 if (a1-a0)%360>180 else 0} 1 {x1:.2f},{y1:.2f}'
        for a0, a1 in ((292, 48), (52, 146), (250, 288), (206, 246)):
            o.append(f'<path d="{arc(a0, a1, 53.6)}" fill="none" stroke="{p["gold"]}" stroke-width="0.45"/>')
    ro, ri = 44, 29.5
    for a, kind, pos in ((300, "range", 2), (320, "wave", 2), (340, "range", 2), (0, "wave", 3), (20, "range", 3), (40, "wave", 5)):
        x, y = pol(0, 0, ro, a); o.append(crot(x, y, p, kind, pos, night))
    for a, lab, v in ((280, "tune", .5), (262, "mod mix", .3), (58, "osc1", .8), (78, "osc2", .6), (98, "osc3", .5), (118, "ext", 0), (138, "noise", .15)):
        x, y = pol(0, 0, ro, a); o.append(K(x, y, p, v, None, night, ticks=False))
        if not night:
            lx, ly = pol(0, 0, 51.3, a); o.append(txt(lx, ly + 0.6, lab, 1.7, p["silk"]))
    for a, lab, v in ((330, "freq 2", .5), (30, "freq 3", .58), (282, "glide", .2), (256, "emph", .6), (230, "contour", .45)):
        x, y = pol(0, 0, ri, a); o.append(K(x, y, p, v, None, night, ticks=False))
        if not night:
            lx, ly = pol(0, 0, 37.0, a); o.append(txt(lx, ly + 0.6, lab, 1.7, p["silk"]))
    if not night:
        x, y = pol(0, 0, ri, 0); o.append(txt(x, y + 1, "osc", 2.0, p["silk"], weight=700))
        o.append(grille(0, 0, 12.2, p, "bull"))
        o.append(scale_ticks(0, 0, 21.6, 23.3, 21, p, w=0.3))
    if light_on:
        o.append('<circle r="13.6" fill="none" stroke="#ffb020" stroke-width="1.1" filter="url(#glow)"/>')
    if night:
        o.append('<circle r="20.5" fill="none" stroke="#b9ff9e" stroke-width="0.5" opacity="0.5" filter="url(#glow)"/>')
    else:
        o.append(f'<g filter="url(#sh)"><path d="M0,-20.8 A20.8,20.8 0 1 1 0,20.8 A20.8,20.8 0 1 1 0,-20.8 Z M0,-14.6 A14.6,14.6 0 1 0 0,14.6 A14.6,14.6 0 1 0 0,-14.6 Z" fill="url(#herog)" fill-rule="evenodd"/></g>')
        o.append(f'<circle r="20.3" fill="none" stroke="{p["hero_lo"]}" stroke-width="0.9" stroke-dasharray="0.45 0.5"/>')
    a = -135 + 270 * .55
    x0, y0 = pol(0, 0, 15.2, a); x1, y1 = pol(0, 0, 20.4, a)
    o.append(f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" stroke="{"#b9ff9e" if night else p["ptr"]}" stroke-width="1.6" stroke-linecap="round"/>')
    if not night:
        o.append(txt(0, 26.6, "cutoff", 2.4, p["hero"], weight=700))
    return "".join(o)


def dish_base(p, night=False):
    o = [f'<g filter="url(#shbig)"><rect width="282" height="{BD}" rx="5" {body_fill(p) if not night else "fill=\"#0a0a0a\""}/></g>']
    hole = f'M{CX-RC},{CY} a{RC},{RC} 0 1 0 {2*RC},0 a{RC},{RC} 0 1 0 {-2*RC},0 Z'
    o.append(f'<path d="M3,3 H279 V{BD-69} H3 Z {hole}" fill="{"#050505" if night else p["panel"]}" fill-rule="evenodd"/>')
    o.append(f'<circle cx="{CX}" cy="{CY}" r="{RC}" fill="#1b1612"/><circle cx="{CX}" cy="{CY}" r="{RC-2}" fill="#2a221c" filter="url(#feltf)"/>')
    for sx in (-1, 1):
        x = CX + sx * (R + 5)
        o.append(f'<rect x="{x-2.5}" y="{CY-1}" width="5" height="{RC+1}" rx="1.5" fill="#120e0b"/><circle cx="{x}" cy="{CY+RC}" r="2.2" fill="url(#brassg)"/>')
    fv = [0.15, 0.55, 0.7, 0.1, 0.45, 0.85]
    for i, x in enumerate((12, 20, 28)):
        o.append(mfader(x, 12, p, fv[i], "ads"[i], night)[0])
    for i, x in enumerate((254, 262, 270)):
        o.append(mfader(x, 12, p, fv[3 + i], "ads"[i], night)[0])
    if not night:
        o.append(txt(20, 8.4, "filter", 2.0, p["gold"], weight=700)); o.append(txt(262, 8.4, "loudness", 2.0, p["gold"], weight=700))
        o.append(txt(262, 60, "mixer on", 2.0, p["gold"], weight=700)); o.append(txt(22, 60, "control", 2.0, p["gold"], weight=700))
    o.append(stog(40, 18, p, True, "kbd 1", night)); o.append(stog(40, 34, p, False, "kbd 2", night))
    o.append(stog(242, 18, p, True, "decay", night))
    for i, (lab, up) in enumerate((("osc mod", 1), ("filt mod", 0), ("osc 3", 0), ("glide", 1))):
        o.append(stog(9 + i * 11, 68, p, bool(up), lab, night, size=1.6))
    for i, (lab, up) in enumerate((("osc1", 1), ("osc2", 1), ("osc3", 1), ("ext", 0), ("noise", 0))):
        o.append(stog(232 + i * 11, 68, p, bool(up), lab, night, size=1.6))
    for i, (lab, up) in enumerate((("wh/pk", 1), ("line/mod", 1), ("feedbk", 0))):
        o.append(stog(244 + i * 13, 87, p, bool(up), lab, night, size=1.6))
    o.append(button(14, 98, p, d=6, night=night)); o.append(button(30, 98, p, d=5, night=night)); o.append(led(44, 96, p["led"], 1))
    if not night:
        o.append(txt(14, 106, "hold", 1.8, p["silk"])); o.append(txt(30, 106, "tune", 1.8, p["silk"]))
    o.append(K(250, 106, p, .6, "vol", night, d=9, ticks=False, lab_dy=7.6)); o.append(K(266, 106, p, .4, "phones", night, d=9, ticks=False, lab_dy=7.6))
    o.append(G(0, BD - 69, 1, key_strip(p, "buttons", night=night, bg=False)))
    return "".join(o)


def dish_view(p, night=False, light_on=True):
    o = [f'<g transform="scale(1,{FS_:.4f})">{dish_base(p, night)}</g>']
    st, _ = stack_side(0, BD * FS_ + 30 * FV_, 282, [(30 * FV_ / 10, "walnut")] * 10)
    o.append(st if not night else f'<rect y="{BD*FS_:.1f}" width="282" height="{30*FV_:.1f}" fill="#050505"/>')
    py = (CY + RC) * FS_; ay = py - ARM * FV_
    for sx in (-1, 1):
        x = CX + sx * (R + 5)
        o.append(f'<rect x="{x-2.8}" y="{ay-3:.1f}" width="5.6" height="{py-ay+3:.1f}" rx="2" fill="{"#5b3a26" if not night else "#0a0a0a"}"/>')
        o.append(f'<circle cx="{x}" cy="{ay:.1f}" r="2.4" fill="url(#brassg)"/><circle cx="{x}" cy="{py:.1f}" r="2.1" fill="url(#brassg)"/>')
    o.append(f'<circle cx="{CX}" cy="{ay+2:.1f}" r="{R}" fill="{"#3b2618" if not night else "#050505"}"/>')
    o.append(f'<g transform="translate({CX},{ay:.1f})" filter="url(#shbig)">{dish_face_c(p, night, light_on)}</g>')
    return "".join(o), BD * FS_ + 30 * FV_, ay - R


def dish_c(p=PAL["proof"]):
    H = 3100
    b = [title_block(90, 140, "DISH", "Sauce · a control dish on a fold-flat fork (radio telescope × furniture) · OP-1 width",
                     ["Turn things on the dish, slide and flip things on the wings. Signal flow spirals inward to the red cutoff",
                      "ring; the speaker plays through the bullseye. The fork swings up from the recess's front edge (dish",
                      "rises toward you), the dish tilts 50°. Keys: two staggered rows of round keys — shallow, accordion-like."],
                     "Look shown: Proof — white panel + dish, walnut stack and fork, black caps, red cutoff ring", 28),
         placeholder_note(90, 520)]
    s = 9.0
    pv, hb, ht = dish_view(p)
    X0, Y0 = 90, 640 + int(-ht * s)
    b.append(view_label(X0, 606, "PLAYING — from the player's eye (40° above; the dish is seen face-on), 1 mm = 9 px"))
    b.append(G(X0, Y0, s, pv))
    b.append(dim_h(X0, X0 + 282 * s, Y0 + hb * s + 60, "282 mm"))
    RX = 2840
    b.append(view_label(RX, 606, "DISH FACE — Ø 110 mm (1 mm = 8.4 px)"))
    b.append(G(RX + 30 + R * 8.4, 650 + R * 8.4, 8.4, dish_face_c(p)))
    b.append(para(RX, 650 + 2 * R * 8.4 + 60, [
        ("Reading the dish", 700),
        "Outer ring from 9 o'clock: tune, mod mix, then the",
        "three oscillators (range + wave) over the top, the",
        "mixer down the right. Inner ring: freq 2/3 under their",
        "oscillators; glide, emphasis, contour at 7–9 o'clock",
        "where the left hand arrives. Legends stay upright.", "",
        ("“Not in control”: the bullseye glows", 700),
        "An amber ring inside the cutoff ring (shown lit).", "",
        ("Key idea: round keys, two rows", 700),
        "Naturals front (Ø 14), sharps behind (Ø 12) in piano",
        "order; ~4 mm travel on Hall sensors. Only 66 mm deep."], 23, "#333"))
    sy = 2740; ss = 3.4
    b.append(view_label(X0, 2250, "SIDE — playing / carry (1 mm = 3.4 px)"))
    se, top = stack_side(0, 0, BD, [(3, "walnut")] * 10)
    pvx = BD - (CY + RC)
    se += f'<rect x="{pvx-2}" y="{top-ARM}" width="4" height="{ARM}" fill="#5b3a26"/>'
    se += (f'<g transform="translate({pvx},{top-ARM}) rotate(-50)"><rect x="{-R}" y="-14" width="{2*R}" height="14" rx="2" fill="{p["panel"]}" stroke="#5b3a26" stroke-width="1"/>'
           f'<rect x="-14" y="-22" width="28" height="8" rx="2" fill="{p["hero"]}"/></g>')
    b.append(G(X0 + 30, sy, ss, se + f'<line x1="-6" y1="0" x2="{BD+6}" y2="0" stroke="#999" stroke-width="0.5"/>'))
    b.append(txt(X0 + 20, sy + 40, "← player", 22, "#777", anchor="start", font=UI_FONT))
    sc, t2 = stack_side(0, 0, BD, [(3, "walnut")] * 10)
    b.append(G(X0 + 1000, sy, ss, sc + f'<rect x="{pvx}" y="{t2-2}" width="{2*RC}" height="2" fill="#5b3a26"/>'))
    b.append(dim_v(X0 + 1000 + BD * ss + 20, sy, sy + (t2 - 2) * ss, "≈ 32 mm carry (est.)"))
    b.append(dim_h(X0 + 1000, X0 + 1000 + BD * ss, sy + 50, f"{BD} mm"))
    b.append(size_note(X0 + 1900, 2450, ["Breaks OP-1 depth: 189 mm", "(1.85×), but carries flat", "at ≈ 32 mm, the slimmest", "of the four closed."]))
    nv, nb, nt = dish_view(p, night=True)
    b.append(view_label(RX, 2330, "LIGHTS OFF"))
    b.append(f'<rect x="{RX}" y="2350" width="{int(282*3.0)+40}" height="{int((nb-nt)*3.0)+40}" rx="10" fill="#050605"/>')
    b.append(G(RX + 20, 2370 + int(-nt * 3.0), 3.0, nv))
    return save(ROOT + "dish/dish-mock.svg", W, H, "".join(b), p)


# ------------------------------------------------------------------ look sheet
def look_sheet():
    p = PAL["field"]
    Hh = 1700
    b = [txt(90, 140, "LOOK SHEET — one concept (CASE), three directions", 76, "#1d1c1a", anchor="start", font=UI_FONT, weight=800),
         para(90, 210, ["Pick by eye. Same instrument, same layout; only panel ink, cap colour, signal colour and the body stack change.",
                        "Every option is something you can make at Vector Space (laser, printers) or order cut; the panel is a PCB in all three."], 28, "#333"),
         placeholder_note(90, 320)]
    cols = [("field", "Field", "felt", ["Panel: black mask, white silk, gold ENIG rules", "Body: warm-grey felt + cork laminated stack",
                                        "Signal: safety orange. Brass hinge + inserts", "Feel: field instrument, soft to hold"]),
            ("proof", "Proof", "walnut", ["Panel: WHITE mask, black silk, gold rules", "Body: walnut-ply stack, plies show on the edge",
                                          "Signal: letterpress red. Black caps", "Feel: printer's proof on a walnut block"]),
            ("desk", "Desk", "acrylic", ["Panel: black mask, white silk, gold rules", "Body: smoked acrylic stack, glassy edges",
                                         "Signal: green. Black caps", "Feel: a lighting desk at night"])]
    sc = 4.1
    for i, (k, name, mat, lines) in enumerate(cols):
        pp = dict(PAL[k])
        x = 90 + i * (282 * sc + 90)
        y = 420
        b.append(txt(x, y, name, 52, "#1d1c1a", anchor="start", font=UI_FONT, weight=800))
        tv = panel_half(pp, mat=mat) + "".join(f'<rect x="{xx}" y="76" width="24" height="5" rx="1.5" fill="url(#brassg)"/>' for xx in (24, 129, 234))
        tv += G(0, 81, 1, key_strip(pp, "lever", mat=mat))
        ids = ("capg", "herog", "natg", "sharpg")
        dd = defs(pp)
        for gid in ids:
            dd = dd.replace(f'id="{gid}"', f'id="{gid}_{k}"')
            tv = tv.replace(f'url(#{gid})', f'url(#{gid}_{k})')
        b.append(dd)
        b.append(G(x, y + 40, sc, tv))
        # stack edge swatch
        lay = {"felt": [(3, "cork")] + [(3, "ply_grey"), (2, "felt")] * 4,
               "walnut": [(3, "walnut")] * 7,
               "acrylic": [(3, "acrylic"), (3, "acrylic_hi")] * 4}[mat]
        sw, _ = stack_side(0, 0, 76, lay)
        b.append(G(x, y + 40 + 160 * sc + 210, 6.0, sw))
        b.append(txt(x + 76 * 6 + 30, y + 40 + 160 * sc + 140, "body edge, 1 mm = 6 px", 20, "#777", anchor="start", font=UI_FONT))
        b.append(para(x, y + 40 + 160 * sc + 290, lines, 25, "#333"))
    return save(ROOT + "look-sheet.svg", 3900, Hh, "".join(b), p)


# ------------------------------------------------------------------ size sheet
def size_sheet():
    p = PAL["field"]
    s = 3.2
    b = [txt(90, 140, "SIZE — OP-1 class, checked", 76, "#1d1c1a", anchor="start", font=UI_FONT, weight=800),
         para(90, 210, ["OP-1: 282 × 102 × 13.5 mm (teenage.engineering product page). Grey = OP-1 footprint, drawn under every concept.",
                        "All outlines to the same scale (1 mm = 3.2 px). Orange = where a concept exceeds OP-1 depth."], 28, "#333")]
    items = [("old CASE (315 mm round, open)", 315, 307, None), ("CASE — open", 282, 157, 76), ("DOCK — played", 282, 155, 76),
             ("MOTTO", 282, 193, 193), ("DISH", 282, 189, 189)]
    x, y = 90, 360
    for i, (name, w, d, carry) in enumerate(items):
        xx = x + (i % 3) * (330 * s + 80)
        yy = y + (i // 3) * (340 * s + 80)
        b.append(txt(xx, yy, name, 30, "#1d1c1a", anchor="start", font=UI_FONT, weight=700))
        g = [f'<rect x="0" y="{d-102}" width="282" height="102" fill="#cfcac0"/>',
             f'<rect x="0" y="0" width="{w}" height="{d}" fill="none" stroke="#22211f" stroke-width="0.8"/>']
        if d > 102:
            g.append(f'<rect x="0" y="0" width="{min(w,282)}" height="{d-102}" fill="#e2783b" opacity="0.25"/>')
        if carry:
            g.append(f'<rect x="0" y="{d-carry}" width="282" height="{carry}" fill="none" stroke="#2f7d4f" stroke-width="0.8" stroke-dasharray="3 2"/>')
        b.append(G(xx, yy + 30, s, "".join(g)))
        b.append(txt(xx, yy + 30 + d * s + 40, f"{w} × {d} mm" + (f" · carry {282}×{carry}" if carry and carry < d else ""), 24, "#444", anchor="start", font=UI_FONT))
    b.append(para(90 + 2 * (330 * s + 80), 360 + 340 * s + 140, [
        ("Reading it", 700), "CASE and DOCK fold to 282 × 76 (green dashes):",
        "smaller than an OP-1 when carried, 1.5× its depth", "when played. MOTTO and DISH stay ~1.9× deep:",
        "the tail and the dish are what they are.", "", ("Thickness (est.)", 700),
        "CASE ≈ 50 closed · DOCK 30 played / 52 carry", "MOTTO ≈ 36 closed · DISH ≈ 32 carry",
        "OP-1 is 13.5 — pots, jacks and keys with travel", "won't go below ≈ 22 per layer."], 26, "#333"))
    return save(ROOT + "size-sheet.svg", 3600, 2320, "".join(b), p)


if __name__ == "__main__":
    which = sys.argv[1:] or ["case", "dock", "motto", "dish", "look", "size"]
    fns = dict(case=case_c, dock=dock_c, motto=motto_c, dish=dish_c, look=look_sheet, size=size_sheet)
    for w in which:
        print(fns[w]())
