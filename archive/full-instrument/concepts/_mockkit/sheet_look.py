"""Look sheet on SLAB at real proportions (R9) + size sheet against eng's box (R1)."""
from r2s_common import *
from sheet_slab import slab_top, BW, BD
from sheet_motto import outline_path

LOOKS = [
    ("field", "Field", "warm-grey felt-faced ply stack · black panel · gold rules · orange cutoff",
     [(3, "cork"), (3, "ply_grey"), (3, "ply_grey"), (3, "ply_grey"), (3, "ply_grey"), (3, "ply_grey"), (3, "ply_grey"), (3, "ply_grey"), (3, "ply_grey"), (3, "felt"), (4, "felt")],
     "Quiet, soft, bag-friendly. Felt edges hide knocks."),
    ("proof", "Proof", "walnut ply body · cream panel, black legends · red cutoff",
     [(3, "walnut")] * 11 + [(1, "walnut")], "Warm, furniture-like, his walnut built-ins. Watch: walnut + big left knob reads 'Moog' (R4/R6)."),
    ("desk", "Desk", "smoked acrylic stack · black panel · green cutoff",
     [(3, "acrylic")] * 11 + [(1, "acrylic_hi")], "Studio object, glows at night through the edges. Shows fingerprints."),
    ("motto", "Cork", "cork-faced body · white panel · acid-chartreuse cutoff (MOTTO's draw, tried on SLAB)",
     [(3, "cork")] * 11 + [(1, "cork")], "The odd one: soft, light, warm to hold, and nobody will call it a clone."),
]


def look_sheet():
    S = 6.0
    b = [head(90, 150, "Look sheet · on SLAB", "Round 2 (R9) · the same SLAB at real proportions in four looks · 1 mm = 6 px",
              ["Same instrument, same panel, four material and colour directions, so the looks can be judged like for like.",
               "The owner letters or paints the legends himself (owner.md Q5): Kalam here is only a stand-in.",
               "Every look uses bought knobs and caps; the colours come from the bought cap, paint, or the laser-cut body."],
              "Checked against owner.md Q5 (\"id have to see mocks of the ideas to tell you which look appeals\") · scores.md R9, R4 · eng v2 §5 (enclosure ≈ $30–80)"),
         placeholder(90, 600)]
    cw = 1830
    for i, (key, name, desc, stack, verdict) in enumerate(LOOKS):
        p = PAL[key]
        x = 90 + (i % 2) * (cw + 60)
        y = 700 + (i // 2) * 1480
        b.append(txt(x, y, name, 52, INK, anchor="start", font=UI_FONT, weight=800))
        b.append(txt(x + 260, y - 4, desc, 25, SUB, anchor="start", font=UI_FONT, weight=500))
        b.append(G(x, y + 40, S, slab_top(p)))
        es, top = stack_side(0, 0, 185, stack)
        b.append(txt(x, y + 40 + BD * S + 70, "edge, as cut (side, 1 mm = 4 px)", 22, SUB, anchor="start", font=UI_FONT))
        b.append(G(x, y + 40 + BD * S + 90 + 34 * 4, 4, es))
        b.append(para(x + 185 * 4 + 60, y + 40 + BD * S + 110, [(verdict, 600)], 24))
    H = 700 + 2 * 1480 + 40
    return save(ROOT + "look-sheet.svg", W, H, "".join(b), PAL["field"])


def size_sheet():
    S = 5.0
    p = PAL["field"]
    b = [head(90, 150, "Size sheet", "Round 2 (R1) · every footprint over eng's box (285 × 170–190 × ≤ 36) · 1 mm = 5 px",
              ["Grey band = eng's realistic box (architecture-v2 §4: 280–290 × 170–190). Dotted = OP-1 field (288 × 102), only a reference:",
               "owner: \"dont over index on OP1… it should feel good to use.\" Thickness bars below each, played and carried."],
              "Checked against eng v2 §4, §4.2 · owner.md size entries · each concept's how-it-works (systems' numbers)")]
    items = [("SLAB", f'<rect width="285" height="185" rx="5" fill="#8b8780" opacity="0.85"/>', [("played", 34, "+ stand 27 at the rear"), ("carried", 46, "")]),
             ("DOCK", f'<rect width="300" height="237" rx="5" fill="#1d2423" opacity="0.85"/><rect y="136" width="300" height="1" fill="#fff"/>', [("played", 33, "300 × 237: over the box"), ("carried", 70, "300 × 136")]),
             ("MOTTO", f'<path d="{outline_path()}" fill="#b48a5e" opacity="0.9"/>', [("played", 34, "lid stands 195 tall"), ("carried", 46, "")]),
             ("DISH", f'<rect width="285" height="188" rx="5" fill="#5b3a26" opacity="0.9"/><ellipse cx="142.5" cy="23.8" rx="56" ry="36" fill="#f1ede3" stroke="#a8823a"/>', [("played", 38, "dish up to ≈ 98"), ("carried", 38, "no lid")])]
    for i, (name, shape, th) in enumerate(items):
        x = 120 + i * 940
        y = 720
        band = (f'<rect x="0" y="0" width="290" height="190" fill="#d9d4ca"/><rect x="0" y="0" width="280" height="170" fill="none" stroke="#9a948a" stroke-width="0.8" stroke-dasharray="3 2"/>'
                f'<rect x="0" y="0" width="288" height="102" fill="none" stroke="#555" stroke-width="0.8" stroke-dasharray="1 1.5"/>')
        b.append(txt(x, y - 30, name, 44, INK, anchor="start", font=UI_FONT, weight=800))
        b.append(G(x, y + 60, S * 0.6, band + shape))
        for k, (lab_, t, note_) in enumerate(th):
            yy = y + 60 + 250 * S * 0.6 + 40 + k * 175
            b.append(txt(x, yy, lab_, 24, SUB, anchor="start", font=UI_FONT, weight=600))
            b.append(f'<rect x="{x+130}" y="{yy-24}" width="560" height="{t*S*0.6}" rx="4" fill="{"#c0392b" if t > 36 else "#4a7a5a"}" opacity="0.8"/>')
            b.append(txt(x + 130 + 560 + 14, yy, f"{t} mm", 24, INK, anchor="start", font=UI_FONT, weight=700))
            if note_:
                b.append(txt(x + 130, yy + t * S * 0.6 + 6, note_, 21, SUB, anchor="start", font=UI_FONT))
    b.append(note(120, 1950, ["Red bars are over eng's ≤ 36 mm. Carried thickness includes the cap pocket: knobs stand 8 mm above the rim (common §1).",
                              "DOCK is the only concept that leaves the footprint box (played 237 deep); systems and I both flag it for the director."], 24))
    return save(ROOT + "size-sheet.svg", W, 2100, "".join(b), p)


if __name__ == "__main__":
    print(look_sheet()); print(size_sheet())
