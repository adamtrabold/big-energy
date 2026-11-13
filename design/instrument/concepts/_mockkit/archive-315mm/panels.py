"""Panel layouts at real mm. Each returns an SVG string in panel-local coordinates."""
from kit import *

# Panel 305 x 140 (CASE lid / DOCK body). y=0 is the far edge, y=140 is nearest the keys.
RECT_W, RECT_H = 305, 140


def panel_rect(p, night=False, light="pip", light_on=False, pcb_bg=True):
    o = []
    if pcb_bg:
        o.append(f'<rect x="0" y="0" width="{RECT_W}" height="{RECT_H}" rx="2.5" fill="{"#050505" if night else p["panel"]}"/>')
    K = lambda *a, **k: knob(*a, p=p, night=night, **k) if False else knob(a[0], a[1], p, night=night, **k)
    if not night:
        # gold ENIG rules: section compartments (job case)
        for x in (57, 91, 171, 226):
            o.append(rule(x, 6, x, RECT_H - 6, p))
        o.append(rule(227, 62, 305 - 4, 62, p))
        # section heads (hand-lettered placeholder)
        heads = [(28.5, "play"), (74, "control"), (131, "oscillators"), (198.5, "mixer"),
                 (247, "filter"), (287, "loudness")]
        for x, s in heads[:4]:
            o.append(txt(x, 7.5, s, 3.0, p["gold"], weight=700))
        o.append(txt(246, 68.5, "filter contour", 2.7, p["gold"], weight=700))
        o.append(txt(286, 68.5, "loudness", 2.7, p["gold"], weight=700))
        o.append(txt(240, 7.5, "output", 3.0, p["gold"], weight=700))
    # --- play strip (left hand)
    o.append(knob(14, 24, p, val=0.25, label="glide", night=night))
    o.append(button(43, 24, p, label="hold", night=night, lit=None))
    o.append(knob(14, 58, p, val=0.62, label="emphasis", night=night))
    o.append(knob(43, 58, p, val=0.45, label="contour amt", night=night, label_size=2.5))
    o.append(hero(28.5, 103, p, night=night, lab_dy=27.5))
    # --- controllers
    o.append(knob(74, 24, p, val=0.5, label="tune", night=night))
    o.append(knob(74, 58, p, val=0.3, label="mod mix", night=night))
    o.append(toggle(66.5, 88, p, True, "osc mod", night=night))
    o.append(toggle(81.5, 88, p, False, "filter mod", night=night))
    o.append(toggle(66.5, 114, p, False, "osc 3 ctl", night=night))
    o.append(toggle(81.5, 114, p, True, "glide", night=night))
    # --- oscillators: one column per osc (range far, wave, freq near)
    for i, x in enumerate((105, 131, 157)):
        o.append(rotary(x, 26, p, "range", pos=[2, 2, 3][i], night=night, lab_dy=None if False else 13.0,
                        label=None))
        o.append(rotary(x, 62, p, "wave", pos=[2, 3, 5][i], night=night))
        if i:
            o.append(knob(x, 96, p, val=[0.5, 0.58][i - 1], label="freq", night=night))
        if not night:
            o.append(txt(x, 128, str(i + 1), 10, p["silk"], weight=700))
    if not night:
        o.append(txt(105, 98, "osc 1 is", 2.3, p["silk"], style="opacity:.6"))
        o.append(txt(105, 101.5, "the reference", 2.3, p["silk"], style="opacity:.6"))
        o.append(txt(92.5, 27, "range", 2.3, p["silk"], anchor="end", rot=-90))
        o.append(txt(92.5, 63, "wave", 2.3, p["silk"], anchor="end", rot=-90))
    # --- mixer: channel rows
    rows = [("osc 1", 0.8, True), ("osc 2", 0.6, True), ("osc 3", 0.5, True), ("ext", 0.0, False), ("noise", 0.15, False)]
    for k, (lab, v, on) in enumerate(rows):
        y = 21 + k * 25
        o.append(knob(183, y, p, val=v, night=night, label=None, ticks=False))
        o.append(toggle(200, y, p, on, None, night=night))
        if not night:
            o.append(txt(174, y - 9.6, lab, 2.6, p["silk"], anchor="start"))
    o.append(toggle(215, 96, p, True, "line/mod", night=night, lab_dy=-6.5, label_size=2.1))
    o.append(toggle(215, 71, p, False, "feedbk", night=night, lab_dy=-6.5, label_size=2.1))
    o.append(toggle(215, 121, p, True, "white/pink", night=night, lab_dy=-6.5, label_size=2.1))
    # --- output + speaker
    o.append(knob(240, 22, p, val=0.6, label="volume", night=night))
    o.append(knob(240, 51, p, val=0.4, label=None, night=night, ticks=False))
    if not night:
        o.append(txt(249.5, 51.8, "phones", 2.4, p["silk"], anchor="start"))
        o.append(grille(282, 31, 21, p))
    else:
        o.append(f'<circle cx="282" cy="31" r="22" fill="#080808"/>')
    # --- contours: 6 faders
    fvals = [0.15, 0.55, 0.7, 0.1, 0.45, 0.85]
    for i, x in enumerate((234, 246, 258, 275, 287, 299)):
        s, _ = fader(x, 74, p, 30, fvals[i], label=["a", "d", "s"][i % 3], night=night)
        o.append(s)
    if not night:
        # dotted envelope traced through cap centres (the shape you will hear)
        def env(xs, vals):
            pts = " ".join(f"{x},{fader_cap_y(74, 30, v):.1f}" for x, v in zip(xs, vals))
            return f'<polyline points="{pts}" fill="none" stroke="{p["gold"]}" stroke-width="0.35" stroke-dasharray="0.8 0.8"/>'
        o.append(env((234, 246, 258), fvals[:3]))
        o.append(env((275, 287, 299), fvals[3:]))
    o.append(toggle(240, 126, p, True, "kbd 1", night=night, lab_dy=-6.2, label_size=2.1))
    o.append(toggle(252, 126, p, False, "kbd 2", night=night, lab_dy=-6.2, label_size=2.1))
    o.append(toggle(270, 126, p, True, "decay", night=night, lab_dy=-6.2, label_size=2.1))
    o.append(button(287, 127, p, d=7.5, label=None, night=night))
    if not night:
        o.append(txt(287, 120, "tune", 2.4, p["silk"]))
    o.append(led(299, 123.5, p["led"], 1.3, on=True))
    if light == "pip":
        o.append(led(299, 131, "#ffb020", 1.0, on=light_on))
        if not night:
            o.append(txt(299, 137.5, "not in ctl", 1.8, p["silk"]))
    elif light == "none" and not night:
        pass
    if not night:
        o.append(txt(299, 119, "status", 1.8, p["silk"]))
        # placeholder mark
        o.append(txt(302, 137.8, "", 1.8, p["silk"], anchor="end"))
    return "".join(o)
