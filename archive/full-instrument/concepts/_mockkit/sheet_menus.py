"""Key menu + controls menu sheets (round 2), grounded in eng/key-sourcing.md and owner.md
("real parts", no printed knobs/keys, no harvested keybed, bend/mod brainstorm)."""
from r2s_common import *

CARD = "#fbf9f4"


def card(x, y, w, h, title, sub, tag=None, tagcol="#2f7d4a"):
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{CARD}" stroke="#d8d2c6" stroke-width="2"/>',
         txt(x + 34, y + 62, title, 40, INK, anchor="start", font=UI_FONT, weight=800),
         txt(x + 34, y + 104, sub, 25, SUB, anchor="start", font=UI_FONT, weight=500)]
    if tag:
        tw = len(tag) * 14 + 40
        o.append(f'<rect x="{x+w-tw-30}" y="{y+30}" width="{tw}" height="44" rx="22" fill="{tagcol}"/>')
        o.append(txt(x + w - tw / 2 - 30, y + 60, tag, 22, "#fff", font=UI_FONT, weight=700))
    return "".join(o)


def stat_lines(x, y, rows, size=23, col2=300):
    o = []
    for i, (k, v) in enumerate(rows):
        yy = y + i * size * 1.45
        o.append(txt(x, yy, k, size, SUB, anchor="start", font=UI_FONT, weight=600))
        o.append(txt(x + col2, yy, v, size, INK, anchor="start", font=UI_FONT))
    return "".join(o)


# ------------------------------------------------------------------ key sections (side views, mm, y down)
def sec_switch(cap_w=18, cap_col="#e8e4da", choc=False):
    o = [part(0, 14, 70, 1.6, "#2e6b3a"), part(0, 9, 70, 1.5, "#888")]       # switch PCB + plate
    o.append(part(26, 9, 15, 5 if not choc else 4, "#3a3a3a", rx=1))         # housing
    o.append(part(31, 6.4, 5, 2.6, "#9aa", rx=0.5))                            # stem
    o.append(part(33.5 - cap_w / 2, 3.2, cap_w, 3.4, cap_col, "#444", 0.25, 1.2))
    if not choc:
        o.append(part(30.5, 15.6, 6, 2.4, "#222", rx=0.4))                     # Hall sensor under PCB
        o.append(txt(44, 18, "Hall sensor under the board", 2.6, "#555", anchor="start", font=UI_FONT))
    o.append(f'<path d="M50,3.2 v3.3" stroke="#c0392b" stroke-width="0.5" marker-end="url(#arr)"/>')
    o.append(txt(52, 6, "3.3 mm" if not choc else "2.8 mm", 2.8, "#c0392b", anchor="start", font=UI_FONT, weight=700))
    return "".join(o)


def sec_lever():
    o = [part(0, 16, 82, 1.6, "#2e6b3a"), part(0, 11, 82, 1.5, "#888")]
    o.append(part(16, 11, 15, 5, "#3a3a3a", rx=1))
    o.append(part(21, 8.4, 5, 2.6, "#9aa", rx=0.5))
    o.append(f'<path d="M4,5 L70,5 L70,8.4 L4,8.4 Z" fill="#e8e4da" stroke="#444" stroke-width="0.25"/>')
    o.append(f'<circle cx="72" cy="7" r="2" fill="#bbb" stroke="#333" stroke-width="0.3"/>')
    o.append(part(60, 3, 10, 2, "#6f6b65", rx=0.5))
    o.append(txt(72, 2.2, "steel rod pivot", 2.6, "#555", font=UI_FONT))
    o.append(txt(48, 1.4, "felt top stop", 2.6, "#555", font=UI_FONT))
    o.append(txt(4, 21.8, "lever top (service-cut) presses a bought Hall switch", 2.6, "#555", anchor="start", font=UI_FONT))
    o.append(f'<path d="M8,5 v3.6" stroke="#c0392b" stroke-width="0.5"/>')
    o.append(txt(10, 3.4, "≈ 5 mm at the front", 2.8, "#c0392b", anchor="start", font=UI_FONT, weight=700))
    return "".join(o)


def sec_pad():
    o = [part(0, 12, 70, 1.6, "#2e6b3a")]
    o.append(f'<path d="M12,12 L12,8 Q12,4 18,4 L34,4 Q40,4 40,8 L40,12 Z" fill="#c9562f" stroke="#7a2f18" stroke-width="0.3"/>')
    o.append(f'<path d="M0,12 L12,12 M40,12 L70,12" stroke="#c9562f" stroke-width="1.2"/>')
    o.append(part(22, 10.4, 8, 1.4, "#111", rx=0.6))
    o.append(txt(46, 7, "silicone sheet, carbon pill", 2.6, "#555", anchor="start", font=UI_FONT))
    o.append(txt(46, 10, "+ magnet over a Hall = velocity", 2.6, "#555", anchor="start", font=UI_FONT))
    return "".join(o)


def sec_plug():
    o = [part(0, 16, 70, 1.6, "#2e6b3a"), part(0, 11, 70, 1.5, "#888")]
    o.append(part(26, 11, 15, 5, "#3a3a3a", rx=1))
    o.append(part(31, 8.4, 5, 2.6, "#9aa", rx=0.5))
    o.append(part(27, 6.6, 13, 2, "#c9c2b3", rx=0.6))
    o.append(part(31, 3, 5, 3.6, "#c9a77a"))
    o.append(f'<path d="M26.5,3 Q26.5,-2.5 33.5,-2.5 Q40.5,-2.5 40.5,3 Z" fill="#d9b98a" stroke="#8a6a3a" stroke-width="0.3"/>')
    o.append(part(10, 2.2, 15, 2, "#7d7a74") + part(42, 2.2, 15, 2, "#7d7a74"))
    o.append(part(24.6, 2.2, 1.6, 2, "#444") + part(40.8, 2.2, 1.6, 2, "#444"))
    o.append(txt(46, -1, "maple button plug (bought)", 2.6, "#555", anchor="start", font=UI_FONT))
    o.append(txt(46, 9.5, "drilled blank cap on a Hall switch", 2.6, "#555", anchor="start", font=UI_FONT))
    o.append(txt(2, 1, "top skin + felt collar", 2.6, "#555", anchor="start", font=UI_FONT))
    return "".join(o)


def sec_fatar():
    o = [txt(0, 0, "full-size key, ≈ 150 mm long", 8.5, "#555", anchor="start", font=UI_FONT),
         part(0, 6, 150, 9, "#efe9dc", "#444", 0.4, 1.5), part(0, 15, 150, 5, "#333", rx=1)]
    o.append(txt(0, 44, "25 full-size keys ≈ 352 mm", 11, "#c0392b", anchor="start", font=UI_FONT, weight=700))
    o.append(txt(0, 60, "the only true keybed sold to individuals;", 8.5, "#555", anchor="start", font=UI_FONT))
    o.append(txt(0, 73, "it doesn't fit a 285–300 mm body", 8.5, "#555", anchor="start", font=UI_FONT))
    return "".join(o)


def keys_sheet():
    p = PAL["field"]
    H = 3480
    b = [f'<defs><marker id="arr" markerWidth="4" markerHeight="4" refX="2" refY="2" orient="auto"><path d="M0,0 L4,2 L0,4 Z" fill="#c0392b"/></marker></defs>']
    b.append(head(90, 150, "Key menu", "Round 2 · real, bought parts only · any key fits any straight-row concept (the switch board is separate)",
                  ["Owner: \"finished instrument should be real parts\", no printed keys, no keybed taken from another product.",
                   "Eng found no bare mini keybed sold to individuals (key-sourcing.md). So every option below is a bought switch",
                   "or pad per key, with a top that is either bought or cut by a laser service. One octave shown, 1 mm = 7 px."],
                  "Checked against owner.md (2026-11-12, all key entries) · eng/key-sourcing.md · eng v2 §1, §4.1 C · scores.md R6"))
    S = 7.0
    cw, ch = 1830, 700
    cards = [
        ("K-A  Flat keys, all catalogue", "OP-1-like: Gateron low-profile Hall switches + bought 1u caps", "ALL BOUGHT", "#2f7d4a",
         lambda: keys_switch(0, 0, p, n=13), sec_switch(),
         [("Silence", "3/5 · no click, light bottom-out; felt under the plate"), ("Feel", "2/5 · short, switch-like; analog travel helps"),
          ("Velocity", "yes (analog Hall position)"), ("25 keys", "≈ 285 mm at 19 mm pitch (UNVERIFIED fit)"),
          ("Cost", "≈ $21 switches + ≈ $4–10 caps (US: Nuphy, keeb.io)"), ("Fits", "any concept · now Little D's first choice")]),
        ("K-B  Lever keys on switches", "Piano-shaped tops on a pivot rod, each pressing a Hall switch", "TOPS SERVICE-CUT", "#b7791f",
         lambda: keys_lever(0, 0, p, n=13, wlen=56, blen=34), sec_lever(),
         [("Silence", "4/5 · switch spring + felt top stop; no click"), ("Feel", "4/5 · a real lever; the switch gives the spring"),
          ("Velocity", "yes"), ("25 keys", "261 mm at 17.4 mm (switch fit UNVERIFIED)"),
          ("Cost", "≈ $21 switches + tops (laser quote needed) + rod ≈ $3"), ("Fits", "SLAB, DOCK (80 mm tops), MOTTO (walnut)")]),
        ("K-C  Quietest switch", "Kailh Choc V2 silent (dampened both ways) + bought caps", "OUT: NO VELOCITY", "#a33a2b",
         lambda: keys_switch(0, 0, p, n=13, cap="#d6d2c8", cap2="#55524c"), sec_switch(choc=True),
         [("Silence", "4/5 · built-in dampers, the quietest mechanical"), ("Feel", "2/5 · short, on/off"),
          ("Velocity", "NO (on/off): out, owner: \"i want velocity\""), ("25 keys", "≈ 270 mm (Choc spacing)"),
          ("Cost", "≈ $17.50 switches + ≈ $4 caps (keeb.io, US)"), ("Fits", "out for both instruments (was Little D's pick)")]),
        ("K-D  Pads in a key layout", "Owner's drum-machine idea: bought silicone pad sheets", "VELOCITY NEEDS ADDED SENSOR", "#b7791f",
         lambda: keys_pads(0, 0, p, n=13), sec_pad(),
         [("Silence", "5/5 · the pad is its own damper"), ("Feel", "3/5 · squishy, familiar from Maschine"),
          ("Velocity", "only added: magnet under each pad over a Hall"), ("25 keys", "pad pitch not stated (UNVERIFIED)"),
          ("Cost", "$5.25 × 2 sheets + ≈ $3 magnets (or FSRs ≈ +$125)"), ("Fits", "any · Hall travel in 2–3 mm squash: UNVERIFIED")]),
        ("K-E  Button plugs, two rows", "Critter and Guitari reference: maple button plugs on Hall switches", "ALL BOUGHT", "#2f7d4a",
         lambda: keys_pegs(0, 0, p, n=13), sec_plug(),
         [("Silence", "4/5 · felt collar in each hole stops rattle"), ("Feel", "3/5 · button-box, warm wood under the finger"),
          ("Velocity", "yes (Hall switch)"), ("25 keys", "261 mm at 17.4 mm"),
          ("Cost", "≈ $21 switches + ≈ $5–10 plugs + ≈ $4 blank caps"), ("Fits", "DISH · any concept · drilled caps = 1 step")]),
        ("K-F  Real keybed (for honesty)", "Fatar TP/9 via Doepfer: true piano action, felt-damped", "TOO WIDE", "#a33a2b",
         lambda: keys_lever(0, 0, p, n=13, wlen=56, blen=34, pitch=23.5), sec_fatar(),
         [("Silence", "5/5 · the quietest and best feel of all"), ("Feel", "5/5 · a real keyboard"),
          ("Velocity", "yes (dual contact)"), ("25 keys", "≈ 352 mm: breaks the 285–300 body"),
          ("Cost", "€120 + €11 cable, ships from Germany"), ("Fits", "only a wider instrument (≈ 370 mm)")]),
    ]
    for i, (t, sub, tag, tc, top, sec, rows) in enumerate(cards):
        cx = 90 + (i % 2) * (cw + 60)
        cy = 640 + (i // 2) * (ch + 50)
        b.append(card(cx, cy, cw, ch, t, sub, tag, tc))
        F = "K-F" in t
        sv = 5.0 if F else S
        b.append(G(cx + 40, cy + 150, sv, f'<rect x="-3" y="-3" width="{(188 if F else 139)+6}" height="{62 if "lever" in t.lower() or F else 50}" rx="2" fill="#0b0b0b"/>' + top()))
        b.append(txt(cx + 40, cy + 150 + (62 * sv if (F or "lever" in t.lower()) else 50 * sv) + 40, "top view, one octave (13 keys)" + (", drawn at 1 mm = 5 px: really 35% wider than the others" if F else ""), 21, SUB, anchor="start", font=UI_FONT))
        if F:
            b.append(G(cx + 1020, cy + 190, 2.6, sec))
        else:
            b.append(G(cx + 1080, cy + 200, 8.5, sec))
            b.append(txt(cx + 1080, cy + 175, "section", 21, SUB, anchor="start", font=UI_FONT))
        b.append(stat_lines(cx + (1080 if not F else 1020), cy + 470, rows, 22, 150))
    # retired strip
    ry = 640 + 3 * (ch + 50) + 10
    bx, bh = box(90, ry, 3720, "Retired this round (and why)", [
        "Laser-cut Delrin lever comb (K1), rockers (K6), magnetic let-off (M1): the touched key itself would be made, not bought. K-B keeps the lever idea with bought switches.",
        "Cast silicone keys and printed TPU pillows (K2): owner: no 3D-printed keys, no printed samples. K-D replaces them with bought pad sheets.",
        "Donor mini keybed (my first round-2 route) and the OP-1 replacement keyboard ($119.99): owner: \"i dont want to steal a keybed\". Walnut-faced tongues (K3) become K-B with walnut tops.",
        "Velocity is required (owner: \"i want velocity\"): K-C is out; K-D only with a magnet + Hall per pad. Samples: none printed. The cheap way to feel these: buy 5 Hall switches + one pad sheet + magnets (≈ $12) and press them on a desk."], 24)
    b.append(bx)
    b.append(txt(90, ry + bh + 60, "Open: owner OK on service-cut lever tops (K-B)? · switch fit at 17.4 mm pitch · Gateron LP caps compatibility · SparkFun pad pitch. All UNVERIFIED until parts are in hand.",
                 24, WARN, anchor="start", font=UI_FONT, weight=600))
    return save(ROOT + "keys/key-menu.svg", W, H, "".join(b), p)


# ------------------------------------------------------------------ controls menu drawings (mm, top views)
def k_skirt(p):
    return knob(10, 10, p, 12, .4, ticks=False)


def k_soft(p):
    return (f'<g filter="url(#sh)"><circle cx="10" cy="10" r="6" fill="#2b2b2b"/></g><circle cx="10" cy="10" r="5.4" fill="#333"/>'
            f'<line x1="10" y1="10" x2="10" y2="4.8" stroke="#eee" stroke-width="1"/>')


def k_collet(p):
    return (f'<g filter="url(#sh)"><circle cx="10" cy="10" r="6.5" fill="#1e1e1e"/></g><circle cx="10" cy="10" r="4" fill="#c0392b"/>'
            f'<line x1="10" y1="3.6" x2="10" y2="6" stroke="#fff" stroke-width="1"/>')


def k_alu(p):
    o = f'<g filter="url(#sh)"><circle cx="10" cy="10" r="6" fill="url(#metal)"/></g>'
    for a in range(0, 360, 12):
        x0, y0 = pol(10, 10, 5.2, a); x1, y1 = pol(10, 10, 6, a)
        o += f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" stroke="#666" stroke-width="0.3"/>'
    return o + '<line x1="10" y1="10" x2="10" y2="4.8" stroke="#222" stroke-width="0.8"/>'


def k_chicken(p):
    return ('<g filter="url(#sh)"><path d="M10,2 L13.5,10 Q13.5,15 10,15 Q6.5,15 6.5,10 Z" fill="#1d1d1d"/></g>'
            '<line x1="10" y1="3" x2="10" y2="8" stroke="#e9f3cf" stroke-width="0.8"/>')


def k_hero(p):
    return hero(15, 15, p, d=26, label=None).replace("scale_ticks", "")


def k_leather(p):
    return (knob(10, 10, p, 12, .4, ticks=False) + '<circle cx="10" cy="10" r="6.2" fill="none" stroke="#7a4a26" stroke-width="1.6"/>'
            '<circle cx="10" cy="10" r="6.2" fill="none" stroke="#c49a6c" stroke-width="0.25" stroke-dasharray="0.8 0.6"/>')


def bm_patch(inner, w=40, h=62, p=None):
    return f'<rect x="0" y="0" width="{w}" height="{h}" rx="2" fill="#1d1d1c"/>' + inner


def stick(cx, cy, d=18, cap="#2b2b2b"):
    return (f'<rect x="{cx-d/2-3}" y="{cy-d/2-3}" width="{d+6}" height="{d+6}" rx="3" fill="#0d0d0d"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{d/2}" fill="#151515"/><g filter="url(#sh)"><circle cx="{cx+1.5}" cy="{cy-1}" r="{d/2-2.5}" fill="{cap}"/></g>'
            f'<circle cx="{cx+1.5}" cy="{cy-1}" r="{d/2-5}" fill="none" stroke="#444" stroke-width="0.4" stroke-dasharray="0.6 0.6"/>')


def mini_stick(cx, cy):
    return (f'<circle cx="{cx}" cy="{cy}" r="4" fill="url(#metal)" stroke="#555" stroke-width="0.2"/><circle cx="{cx}" cy="{cy}" r="2.6" fill="#777"/>'
            f'<g filter="url(#sh)"><line x1="{cx}" y1="{cy}" x2="{cx+1.8}" y2="{cy-3.2}" stroke="#ddd" stroke-width="1.4" stroke-linecap="round"/>'
            f'<circle cx="{cx+2}" cy="{cy-3.6}" r="1.9" fill="#1d1d1d"/></g>')


def fader_v(cx, y0, L=36, val=0.3):
    cy = y0 + 3 + (L - 6) * (1 - val)
    return (f'<rect x="{cx-0.9}" y="{y0}" width="1.8" height="{L}" rx="0.9" fill="#050505"/>'
            f'<g filter="url(#sh)"><rect x="{cx-3.5}" y="{cy-5}" width="7" height="10" rx="1" fill="url(#capg)"/></g>'
            f'<line x1="{cx-3.3}" y1="{cy}" x2="{cx+3.3}" y2="{cy}" stroke="#e9f3cf" stroke-width="0.9"/>')


def strip(x, y, w=8, L=50):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{L}" rx="2" fill="#2a2a2a" stroke="#555" stroke-width="0.3"/>'
            f'<rect x="{x+2}" y="{y+2}" width="{w-4}" height="{L-4}" rx="1.4" fill="#3a3a3a"/>'
            f'<circle cx="{x+w/2}" cy="{y+L/2}" r="1.2" fill="#e9f3cf" opacity="0.5"/>')


def big_wheels(p):
    o = ""
    for i in range(2):
        x = 6 + i * 15
        o += f'<rect x="{x}" y="6" width="11" height="50" rx="2" fill="#070707"/><rect x="{x+1.5}" y="9" width="8" height="44" rx="3" fill="url(#capg)"/>'
        for k in range(20):
            o += f'<line x1="{x+2}" y1="{10.5+k*2.1:.1f}" x2="{x+9}" y2="{10.5+k*2.1:.1f}" stroke="#232220" stroke-width="0.5"/>'
    return o


def controls_sheet():
    p = PAL["field"]
    H = 4300
    b = [head(90, 150, "Controls menu", "Round 2 · knobs, bend/mod and faders · bought parts only · serves the full instrument and Little D",
              ["Owner: \"finished instrument should be real parts\" and, on bend/mod, \"just getting creative here\": wheels, sticks,",
               "mini sticks, touch strips, faders, little dials. All laid out side by side below; nothing is decided. Every bend/mod",
               "option is a pot underneath (eng v2 §2: mod is an analog pot), so each works electrically. Drawn at 1 mm = 7 px."],
              "Checked against owner.md (\"real parts\"; \"can we get creative with any of the knob / wheel styles\"; bend/mod entries; silence) · eng v2 §2, §5 · budget-variant §3")]
    S = 7.0
    # ---- row 1: knobs
    y1 = 640
    b.append(view_label(90, y1, "1 · KNOBS (all bought; any colour; glow pointer = luminous paint on the bought cap)"))
    knobs = [("Skirted, knurled", "Davies-1900H-style clone", "≈ $0.40–0.70", "default", k_skirt),
             ("Soft-touch", "rubberised (Rogan-style)", "≈ $2–4", "quiet grip", k_soft),
             ("Collet + coloured cap", "Sifam-style", "≈ $4–8", "premium", k_collet),
             ("Knurled aluminium", "set-screw", "≈ $1–2", "Desk look", k_alu),
             ("Chicken-head", "pointer knob", "≈ $1–3", "readable in the dark", k_chicken),
             ("Hero, large skirted", "Ø26–30", "≈ $1–3", "cutoff", k_hero),
             ("Leather band (draw)", "bought knob + glued leather", "+ ≈ $0.10", "bookbinding × do both", k_leather)]
    for i, (t, s2, c, use, fn) in enumerate(knobs):
        x = 90 + i * 535
        b.append(f'<rect x="{x}" y="{y1+30}" width="505" height="430" rx="14" fill="{CARD}" stroke="#d8d2c6" stroke-width="2"/>')
        b.append(G(x + 40 + (0 if fn is not k_hero else -30), y1 + 60, S * (1.4 if fn is not k_hero else 0.95), fn(p)))
        b.append(para(x + 30, y1 + 340, [(t, 700), s2, f"{c} · {use}"], 22))
    b.append(note(90, y1 + 520, ["Silence: all silent (no detents). Every MIDI-able knob gets the gold ring painted on the panel, not on the cap, so any cap style works.",
                                 "Draw this round (bookbinding × \"faced with a choice, do both\"): one bought knob type, plus a strip of bookbinding leather on every rotating edge (knobs and wheels) = grip, silence, and it matches SLAB's sewn leather hinge."], 23))
    # ---- row 2: bend / mod spread
    y2 = 1300
    b.append(view_label(90, y2, "2 · BEND AND MOD: the owner's lead, then every alternative side by side"))
    ly = y2 + 40
    b.append(f'<rect x="90" y="{ly}" width="3720" height="600" rx="16" fill="#fff8e6" stroke="#c9a24e" stroke-width="3"/>')
    b.append(txt(130, ly + 64, "LEAD · owner's pick: a one-way bend stick + a mod fader (or dial)", 40, INK, anchor="start", font=UI_FONT, weight=800))
    b.append(txt(130, ly + 106, "owner.md: joystick chosen; \"joystick is great if we can go one direction\"; bend springs back, mod stays put", 25, "#8a6a2a", anchor="start", font=UI_FONT, weight=600))
    b.append(G(150, ly + 150, 7.5, bm_patch(bendmod_lead(2, 2, p), 16.2, 58)))
    b.append(txt(290, ly + 585, "13 mm zone, 1 mm = 7.5 px", 20, SUB, anchor="start", font=UI_FONT))
    # gate detail
    gd = (f'<rect x="0" y="0" width="40" height="40" rx="2" fill="#1d1d1c"/><rect x="17.8" y="6" width="4.4" height="28" rx="2.2" fill="#000" stroke="#c9a24e" stroke-width="0.4"/>'
          f'<circle cx="20" cy="20" r="9" fill="none" stroke="#666" stroke-width="0.4" stroke-dasharray="1 1"/>'
          f'<g filter="url(#sh)"><circle cx="20" cy="14" r="4.4" fill="url(#capg)"/></g>'
          f'<path d="M27,12 v-5 M27,28 v5" stroke="#e9f3cf" stroke-width="0.6"/>' + txt(31, 9, "up", 2.8, "#ddd", anchor="start", font=UI_FONT) + txt(31, 34, "down", 2.8, "#ddd", anchor="start", font=UI_FONT)
          + txt(20, 38.6, "dashed: full stick circle · slot: one axis", 2.4, "#aaa", font=UI_FONT))
    b.append(G(500, ly + 150, 9, gd))
    b.append(para(940, ly + 180, [("Bend: spring-return stick, one direction", 700),
                                  "Route 1: a true single-axis sprung stick (part UNVERIFIED).",
                                  "Route 2 (sure to exist): a standard 2-axis thumbstick",
                                  "(ALPS RKJXV-class) under a laser-cut slot in the panel:",
                                  "the gate stops sideways travel; only Y is read.",
                                  "Push = up, pull = down, let go = centre. Quiet springs.",
                                  "≈ $3–10. Its pot sits in the MCU-read bend path (eng §2)."], 25))
    b.append(para(1900, ly + 180, [("Mod: stays where you leave it", 700),
                                   "A short 20 mm slide pot + bought fader cap behind the",
                                   "stick (drawn), or a small dial in the same spot.",
                                   "Analog pot in the mod path, as eng v2 §2 requires.",
                                   "≈ $1–2. Silent. Reads its own position: no light needed."], 25))
    b.append(para(2860, ly + 180, [("Where it goes", 700),
                                   "SLAB, MOTTO, DISH: the 13 mm zone at the left of",
                                   "the keys (stick at the front, fader behind).",
                                   "DOCK: the pod beside the panel.",
                                   "Fit of the stick body (≈ 17 mm square) under a 13 mm",
                                   "zone: UNVERIFIED; a mini stick is the fallback.",
                                   "Drawn on every concept mock this round."], 25))
    y2 = y2 + 660
    b.append(txt(90, y2 + 20, "Alternatives (still on the table):", 28, SUB, anchor="start", font=UI_FONT, weight=700))
    spread = [
        ("Thumbwheels", "", bm_patch(wheels_thin(10, 6, p, h=50) + txt(20, 61, "13 mm zone", 3, "#ccc", font=UI_FONT), 40, 64),
         ["Bought thumbwheel pots, side by side", "Feel 3/5 · bend centre-sprung", "Silent · ≈ $2–6 the pair (UNVERIFIED)", "Fits the 13 mm zone, no width cost"]),
        ("Classic wheels", "", bm_patch(big_wheels(p), 40, 64),
         ["Ø40-class wheels on pots", "Feel 5/5 · the Model D gesture", "Silent · bought wheel part UNVERIFIED", "+30 mm width at the left"]),
        ("X/Y thumbstick", "Korg-style", bm_patch(stick(20, 26) + txt(20, 52, "X bend · Y mod", 3.2, "#ccc", font=UI_FONT), 40, 64),
         ["ALPS RKJXV-class / 2-axis module", "Feel 4/5 · one thumb does both", "Quiet springs · ≈ $3–10", "Mod springs back: Y = mod while held"]),
        ("Two sticks", "", bm_patch(stick(12, 22, 14) + stick(30, 44, 14) + txt(20, 61, "bend | mod", 3, "#ccc", font=UI_FONT), 42, 64),
         ["Two bought thumbsticks", "Bend X on one, mod Y on the other", "Quiet · ≈ $6–20", "Mod still springs back (see note)"]),
        ("Mini sticks", "owner's \"tiny joysticks\"", bm_patch(mini_stick(12, 20) + mini_stick(28, 20) + txt(20, 40, "bend · mod", 3, "#ccc", font=UI_FONT) + txt(20, 46, "≈ toggle-sized", 2.6, "#999", font=UI_FONT), 40, 64),
         ["ALPS RKJXT/RKJXM-class mini sticks", "Feel 3/5 · fingertip, like a tone switch", "Quiet · ≈ $3–8 · must be ANALOG,", "not 4-way switches (UNVERIFIED)"]),
        ("Touch strips", "option", bm_patch(strip(8, 6) + strip(24, 6) + txt(20, 62, "bend · mod", 3, "#ccc", font=UI_FONT), 40, 66),
         ["SoftPot 50 mm (a resistive pot)", "Feel 3/5 · bend from where you land", "Silent · $8.95 each", "Above the keys or in the 13 mm zone"]),
        ("Fader for mod", "owner: \"sweet\"", bm_patch(fader_v(12, 8, 44, 0.65) + fader_v(28, 8, 44, 0.2) + txt(20, 60, "mod · (bend?)", 3, "#ccc", font=UI_FONT), 40, 64),
         ["Bought 45 mm slide pot + fader cap", "Mod stays put: perfect for mod", "Silent · ≈ $1–2", "Sprung fader for bend: UNVERIFIED"]),
        ("Little dials", "owner: \"would even work\"", bm_patch(knob(12, 20, p, 12, .5, ticks=False) + knob(28, 20, p, 12, .3, ticks=False) +
                                                                 '<path d="M6,10 q6,-5 12,0" fill="none" stroke="#e9f3cf" stroke-width="0.6"/>' + txt(20, 36, "bend · mod", 3, "#ccc", font=UI_FONT), 40, 64),
         ["Mod: a plain small knob (stays put)", "Bend: centre-detent pot ($1) = feel", "  the centre, no return; spring-return", "  pot in TH: UNVERIFIED part"]),
    ]
    for i, (t, tag, g, lines) in enumerate(spread):
        x = 90 + (i % 4) * 935
        y = y2 + 40 + (i // 4) * 620
        b.append(f'<rect x="{x}" y="{y}" width="905" height="590" rx="14" fill="{CARD}" stroke="#d8d2c6" stroke-width="2"/>')
        b.append(txt(x + 30, y + 54, t, 34, INK, anchor="start", font=UI_FONT, weight=800))
        if tag:
            b.append(txt(x + 875, y + 52, tag, 22, "#8a6a2a", anchor="end", font=UI_FONT, weight=600))
        b.append(G(x + 40, y + 90, S, g))
        b.append(para(x + 360, y + 150, [(lines[0], 700)] + lines[1:], 25))
    # mixes + mod note
    ym = y2 + 40 + 2 * 620
    bx, bh = box(90, ym, 3720, "Mixes worth sampling (one hand each, no width cost unless noted)", [
        "Mini stick for bend + fader for mod: the lead above in a smaller part, if the thumbstick body doesn't fit the 13 mm zone.",
        "Thumbwheel for bend + little dial for mod: the cheapest, smallest pair (Little D).     ·     Touch strip for bend + fader for mod: no moving parts for bend at all.",
        "Sprung sticks and mod: a sprung axis can't hold a mod depth. Either Y = mod only while held (Korg style), or pair the stick with a fader/dial for mod. A latching button would click: rejected (silence).",
        "Electrical: every option above is a pot, so mod stays in the analog path (eng v2 §2). Hall-type mini sticks would need eng's E1 (mod as a VCA) first."], 23)
    b.append(bx)
    # ---- row 3: faders + selectors
    y3 = ym + bh + 80
    b.append(view_label(90, y3, "3 · FADERS AND SELECTORS"))
    fs = [("Slide pot + fader cap", "default contour faders", g := bm_patch(fader_v(10, 8, 40, .7) + fader_v(21, 8, 40, .3) + fader_v(32, 8, 40, .5), 42, 58),
           "Bought 30–45 mm slide pots + Alpha-style caps · silent · ≈ $0.60–1.20 + cap · felt strip under the slot for dust"),
          ("Abacus faders", "MOTTO's sauce option", bm_patch("".join(f'<line x1="{x}" y1="6" x2="{x}" y2="52" stroke="#b8933f" stroke-width="0.8"/><circle cx="{x}" cy="{14+ (x*7)%30}" r="3.4" fill="#8a5a32"/>' for x in (8, 17, 26, 35)), 42, 58),
           "Bought wooden beads on 3 mm brass rods, each coupled to a hidden slide pot · quiet with a bushing · ≈ $1–1.60 each"),
          ("RANGE selector", "rotary switch vs pot", bm_patch(Rot(12, 22, p, "range", 2) + knob(32, 22, p, 12, .5, ticks=False) + txt(12, 44, "Lorlin", 3, "#ccc", font=UI_FONT) + txt(32, 44, "pot + detents", 3, "#ccc", font=UI_FONT), 44, 58),
           "Lorlin-type rotary switch (bought, soft tick, ≈ $1.50–3) vs a pot with firmware detents (silent, no feel). Drawn: Lorlin"),
          ]
    for i, (t, tag, g, line) in enumerate(fs):
        x = 90 + i * 1245
        b.append(f'<rect x="{x}" y="{y3+30}" width="1215" height="520" rx="14" fill="{CARD}" stroke="#d8d2c6" stroke-width="2"/>')
        b.append(txt(x + 30, y3 + 86, t, 34, INK, anchor="start", font=UI_FONT, weight=800))
        b.append(txt(x + 1185, y3 + 84, tag, 22, "#8a6a2a", anchor="end", font=UI_FONT, weight=600))
        b.append(G(x + 40, y3 + 120, S, g))
        import textwrap
        b.append(para(x + 380, y3 + 170, textwrap.wrap(line, 44), 25))
    yr = y3 + 600
    b.append(txt(90, yr, "Retired (printed, so out per owner): printed knob caps (C1), printed wheels and edge wheels (C2, C3), printed abacus beads (C6), printed zipper rack for RANGE (C8). Edge wheels survive only with a bought thumbwheel pot.",
                 23, WARN, anchor="start", font=UI_FONT, weight=600))
    b.append(txt(90, yr + 40, "Prices are rough catalogue figures (UNVERIFIED) except SoftPot $8.95 (eng budget-variant). The owner wants to see before buying: no quotes requested.",
                 23, SUB, anchor="start", font=UI_FONT))
    H = yr + 100
    return save(ROOT + "controls/controls-menu.svg", W, int(H), "".join(b), p)


if __name__ == "__main__":
    print(keys_sheet()); print(controls_sheet())
