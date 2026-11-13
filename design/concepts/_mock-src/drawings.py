#!/usr/bin/env python3
"""2D drawings in mm (SVG fragments): real-size top views, real-size side sections, the ONE SHEET nest."""
import math
from ld import (W, D, KNOBS, TOGGLES, SECTIONS, GAP_CENTRES, STICK, MOD_DIAL, STATUS_LED, NIC_LED,
                KNOB_D, HERO_D, ANG, white_keys, sharp_keys)

INK = "#2b2722"; MUTE = "#8a8174"; ACC = "#c4512e"; PLYC = "#e6c79c"; PLYE = "#c99b62"
FELT = "#9a9894"; CEDAR = "#a5643f"; PAPER = "#f3efe8"; BLUE = "#3d6e8f"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def t(x, y, s, size=2.2, fill=INK, anchor="start", weight="normal", family="Inter", style="normal", rot=0):
    tr = f' transform="rotate({rot} {x:.2f} {y:.2f})"' if rot else ""
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-family="{family}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}" font-style="{style}"{tr}>{esc(s)}</text>')

def rect(x, y, w, h, fill="none", stroke=INK, sw=0.25, rx=0, extra=""):
    return f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'

def line(x1, y1, x2, y2, stroke=INK, sw=0.25, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def circ(cx, cy, r, fill="none", stroke=INK, sw=0.25, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def dim_h(x1, x2, y, label, size=2.6):
    s = line(x1, y, x2, y, MUTE, 0.2) + line(x1, y - 2, x1, y + 2, MUTE, 0.2) + line(x2, y - 2, x2, y + 2, MUTE, 0.2)
    return s + t((x1 + x2) / 2, y - 1.2, label, size, MUTE, "middle")

def dim_v(x, y1, y2, label, size=2.6):
    s = line(x, y1, x, y2, MUTE, 0.2) + line(x - 2, y1, x + 2, y1, MUTE, 0.2) + line(x - 2, y2, x + 2, y2, MUTE, 0.2)
    return s + t(x + 1.8, (y1 + y2) / 2, label, size, MUTE, "start", rot=0)

# ------------------------------------------------------------------ top views (1:1)
CFG = {
    "type-case": dict(body=PLYC, panel="#2a2522", eng="#e9d9bb", knob="#efe5cb", keys="short", jacks="rear"),
    "one-sheet": dict(body=PLYC, panel=PLYC, eng="#6b4a2a", knob="#efe5cb", keys="short-ply", jacks="rear"),
    "hymnal": dict(body=CEDAR, panel=PLYC, eng="#3a2a1c", knob="#b8432a", keys="piano", jacks="right"),
    "hush": dict(body=FELT, panel=FELT, eng="#f1ece2", knob="#efe5cb", keys="pegs", jacks="right"),
}

def plan(concept, ox, oy):
    """Top view at 1:1. (ox, oy) = SVG position of the body's rear-left outer corner (y flips)."""
    cfg = CFG[concept]
    Y = lambda y: oy + (D - y)
    X = lambda x: ox + x
    s = []
    if concept == "one-sheet":
        r = 10
        s.append(f'<path d="M {X(r)} {Y(0)} L {X(W)} {Y(0)} L {X(W)} {Y(D-r)} A {r} {r} 0 0 0 {X(W-r)} {Y(D)} '
                 f'L {X(0)} {Y(D)} L {X(0)} {Y(r)} A {r} {r} 0 0 0 {X(r)} {Y(0)} Z" fill="{cfg["body"]}" stroke="{INK}" stroke-width="0.35"/>')
    elif concept == "hush":
        s.append(rect(X(-3), Y(D + 3), W + 6, D + 6, cfg["body"], INK, 0.35, rx=3))
        s.append(rect(X(-3), Y(D + 31), W + 6, 26, "#8f8d89", INK, 0.25, rx=12))
        s.append(t(X(W / 2), Y(D + 16), "felt flap, rolled behind (bolster)", 2.6, "#f1ece2", "middle"))
    else:
        s.append(rect(X(0), Y(D), W, D, cfg["body"], INK, 0.35))
    if concept == "hymnal":
        s.append(rect(X(3), Y(0) , W - 6, 37, "#b9774f", INK, 0.25, extra='stroke-dasharray="1.2 0.8"'))
        s.append(t(X(W / 2), Y(-20), "front wall, dropped flat: fallboard / palm rest (37 mm)", 2.6, "#f6eadb", "middle"))
        for xh in (40, W - 40):
            s.append(rect(X(xh - 8), Y(1.5), 16, 3, "#c9a24a", INK, 0.2))
        for xh in (50, W - 50):
            s.append(rect(X(xh - 9), Y(D + 1.2), 18, 1.4, "#c9a24a", INK, 0.2))
        s.append(t(X(W / 2), Y(D + 4.5), "lid hinged on the rear edge (stands open as the patch-chart desk)", 2.4, MUTE, "middle"))
    # panel
    if concept != "hush":
        s.append(rect(X(3), Y(D - 3), W - 6, D - 3 - 78, cfg["panel"], INK, 0.2))
    else:
        s.append(rect(X(57.5), Y(159.5), 66, 65, PLYC, INK, 0.2))
        s.append(circ(X(192), Y(104), 17, PLYC, INK, 0.2))
    # type case: walls and card rail
    if concept == "type-case":
        for xc in GAP_CENTRES[1:5]:
            s.append(rect(X(xc - 1.5), Y(D - 3), 3, D - 3 - 81, PLYC, INK, 0.2))
        s.append(rect(X(3), Y(81), W - 6, 3, PLYC, INK, 0.2))
        s.append(rect(X(3), Y(D - 3), W - 6, 3, PLYC, INK, 0.2))
        for num, name, x0, x1 in SECTIONS:
            s.append(rect(X(x0 + 1.5), Y(79.5), x1 - x0 - 3, 1.5, "#ffffff", INK, 0.15))
    if concept == "one-sheet":
        for xc in GAP_CENTRES[1:5]:
            s.append(line(X(xc), Y(172), X(xc), Y(84), cfg["eng"], 0.25))
        for (x, y) in [(8, 84), (W - 8, 84), (8, D - 8), (W - 8, D - 8)]:
            s.append(circ(X(x), Y(y), 2.1, "#b8bcc0", INK, 0.15))
        s.append(t(X(10), Y(-6), "kerf-bent corner", 2.4, ACC))
        s.append(t(X(W - 10), Y(D + 3.5), "kerf-bent corner", 2.4, ACC, "end"))
    # section titles
    for num, name, x0, x1 in SECTIONS:
        col = cfg["eng"] if concept != "hymnal" else "#b8432a"
        if concept == "type-case":
            s.append(t(X(x0 + 2), Y(79.8), num + ("  " + name if x1 - x0 > 30 else ""), 1.6, INK, weight="bold"))
        else:
            s.append(t(X(x0 + 1), Y(82.4), num + ("  " + name if x1 - x0 > 30 else ""), 2.3, col, weight="bold"))
    # lip
    lipcol = {"type-case": PLYC, "one-sheet": PLYC, "hymnal": "#efe4c9", "hush": FELT}[concept]
    if concept != "hush":
        s.append(rect(X(3), Y(78), W - 6, 23, lipcol, INK, 0.25))
        for k in range(9):
            s.append(circ(X(25 + 13.5 + k * 30), Y(72), 2.1, "#b8bcc0" if concept != "hymnal" else "#c9a24a", INK, 0.15))
    # keys
    if cfg["keys"] in ("short", "short-ply"):
        ply = cfg["keys"] == "short-ply"
        s.append(rect(X(25), Y(55), 270, 52, "#2a2522" if not ply else PLYE, INK, 0.2))
        for x0, i in white_keys():
            s.append(rect(X(x0 + 0.4), Y(33.5), 17.2, 30, "#e9c58f" if ply else "#fbf9f4", INK, 0.25))
        for xc in sharp_keys():
            s.append(rect(X(xc - 7), Y(53), 14, 16, "#d7a86e" if ply else "#3a3632", INK if ply else "#8a8174", 0.4))
            if ply:
                s.append(circ(X(xc), Y(45), 1.1, "#6b4a2a", None, 0))
        s.append(t(X(160), Y(-5.5), "short pressed-on tops (eng S1): whites 30 × 17.2 front row, sharps 16 × 14 rear row; no rocking, no stabilisers", 2.2, MUTE, "middle"))
    elif cfg["keys"] == "piano":
        s.append(t(X(160), Y(-48) if False else Y(-50), "", 2, MUTE))
        for x0, i in white_keys():
            s.append(rect(X(x0 + 0.3), Y(55), 17.4, 52, "#fbf9f4", INK, 0.2))
        for xc in sharp_keys():
            s.append(rect(X(xc - 5), Y(55), 10, 32, "#2b2826", INK, 0.2))
    else:
        for x0, i in white_keys():
            s.append(circ(X(x0 + 9), Y(16), 6.35, "#e2c290", INK, 0.25))
        for xc in sharp_keys():
            s.append(circ(X(xc), Y(37), 6.35, "#c99a62", INK, 0.25))
        s.append(rect(X(-2), Y(2), W + 4, 5, "#85837f", INK, 0.15))
    # stick column
    s.append(rect(X(4), Y(55), 20, 51, "#2a2522" if concept == "type-case" else ("#f2f0ea" if concept == "hush" else cfg["panel"]), INK, 0.2))
    s.append(rect(X(STICK[0] - 1.6), Y(STICK[1] + 8), 3.2, 16, "#1d1b19", None, 0))
    s.append(circ(X(STICK[0]), Y(STICK[1]), 5.2, "#2f2f33", INK, 0.2))
    mk = cfg["knob"] if concept != "hymnal" else "#b8432a"
    s.append(circ(X(MOD_DIAL[1]), Y(MOD_DIAL[2]), KNOB_D / 2, mk, INK, 0.25))
    s.append(t(X(14), Y(5.5), "BEND", 1.7, "#e9d9bb" if concept == "type-case" else INK, "middle"))
    s.append(t(X(14), Y(36.5), "MOD", 1.7, "#e9d9bb" if concept == "type-case" else INK, "middle"))
    # knobs
    for lab, x, y, kind, midi in KNOBS:
        r = (HERO_D if kind == "hero" else KNOB_D) / 2
        col = "#efe5cb" if kind == "hero" else cfg["knob"]
        s.append(circ(X(x), Y(y), r, col, INK, 0.3))
        a = math.radians(ANG[lab])
        s.append(line(X(x + r * 0.15 * math.sin(a)), Y(y + r * 0.15 * math.cos(a)), X(x + r * 0.85 * math.sin(a)),
                      Y(y + r * 0.85 * math.cos(a)), ACC if kind == "hero" else INK, 0.6))
        short = lab.replace("F. ", "").replace("L. ", "")
        short = {"CONTOUR AMT": "AMOUNT"}.get(short, short.split(" ")[0] if short.startswith(("RANGE", "WAVE", "FREQ")) else short)
        dy = -(r + 3.0)
        s.append(t(X(x), Y(y + dy) , short, 1.7, cfg["eng"], "middle"))
        if midi:
            rr = r + 3.0
            s.append(circ(X(x + rr * 0.72), Y(y + rr * 0.72), 0.55, cfg["eng"], None, 0))
    for lab, x, y, n in TOGGLES:
        s.append(rect(X(x - 2.2), Y(y + 4.5), 4.4, 9, "#b9bcbf", INK, 0.2, rx=1))
        s.append(t(X(x), Y(y - 8.7), lab, 1.5, cfg["eng"], "middle"))
    s.append(circ(X(STATUS_LED[0]), Y(STATUS_LED[1]), 1.6, "#ffb347", INK, 0.2))
    s.append(t(X(STATUS_LED[0]), Y(STATUS_LED[1] - 5.2), "STATUS", 1.5, cfg["eng"], "middle"))
    s.append(circ(X(NIC_LED[0]), Y(NIC_LED[1]), 1.4, "#e9dfc8", INK, 0.2))
    # speaker (on the bottom), dashed
    s.append(circ(X(170), Y(128), 38.5, "none", BLUE, 0.35, dash="2 1.5"))
    s.append(t(X(170), Y(128 - 41.5), "3-in speaker on the bottom (behind)", 2.0, BLUE, "middle"))
    # jacks
    if cfg["jacks"] == "rear":
        for k in range(7):
            s.append(rect(X(152 + k * 19 - 3), Y(D) - 1.8, 6, 1.8, "#555", None, 0))
        s.append(rect(X(130 - 6), Y(D) - 1.8, 12, 1.8, "#999", None, 0))
        s.append(t(X(205), Y(D) - 3.2, "jacks + recessed power switch on the rear edge", 2.4, BLUE, "middle"))
    else:
        for k in range(7):
            s.append(rect(X(W) + (3 if concept == "hush" else 0), Y(92 + k * 12.5) - 3, 1.8, 6, "#555", None, 0))
        s.append(t(X(W) + 7, Y(130), "jacks on the right edge", 2.4, BLUE, "middle", rot=90))
    # hero callout
    s.append(line(X(192 + 11), Y(104 - 7), X(206), Y(70), ACC, 0.3))
    s.append(t(X(207), Y(68.5), "CUTOFF: the one hero knob (Tayda 1083, 20.8 mm)", 2.4, ACC))
    # reading order arrow
    if concept != "hush":
      s.append(line(X(14), Y(D) - 9, X(284), Y(D) - 9, MUTE, 0.3))
      s.append(f'<path d="M {X(284)} {Y(D)-9} l -3 -1.5 l 0 3 z" fill="{MUTE}"/>')
      s.append(t(X(14), Y(D) - 11, "reading order: I → V left to right; front row first within a section", 2.4, MUTE))
    # dims
    s.append(dim_h(X(0), X(W), Y(0) + (14 if concept != "hymnal" else 46), "298 mm"))
    s.append(dim_v(X(W) + (16 if cfg["jacks"] == "right" else 8), Y(D), Y(0), "180 mm"))
    return "\n".join(s)

# ------------------------------------------------------------------ sections (1:1), y → right, z → up
def section(concept, ox, oy, sc=1.0):
    """Side section through a white key and section IV (CUTOFF column), front at left.
    (ox, oy) = SVG position of y=0, z=0."""
    Y = lambda y: ox + y * sc
    Z = lambda z: oy - z * sc
    s = []
    def R(y0, z0, y1, z1, fill, stroke=INK, sw=0.2, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        return (f'<rect x="{Y(y0):.2f}" y="{Z(z1):.2f}" width="{(y1-y0)*sc:.2f}" height="{(z1-z0)*sc:.2f}" '
                f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
    def L(y, z, text, ty, tz, col=INK, size=2.1, anchor="start"):
        return line(Y(y), Z(z), Y(ty), Z(tz), col, 0.18) + t(Y(ty) + (0.8 if anchor == "start" else -0.8), Z(tz) + 0.8, text, size, col, anchor)
    pz = {"type-case": 27, "one-sheet": 27, "hymnal": 26, "hush": 27}[concept]
    body = {"type-case": PLYC, "one-sheet": PLYC, "hymnal": CEDAR, "hush": PLYC}[concept]
    # bottom + feet
    s.append(R(0, 0, D, 3, body))
    for yf in (15, D - 15):
        s.append(R(yf - 6, -6, yf + 6, 0, "#6b6b6b"))
    style = CFG[concept]["keys"]
    # strip C + switches: bought Kailh Choc V2 silent, stems at 14.1 (eng velocity-and-keys-v2)
    s.append(R(8, 4.5, 58, 6.1, "#2f6b4f"))                                   # strip C (printed board)
    s.append(R(10.5, 6.1, 25.5, 11.1, "#3a3a3a"))                              # white switch housing (stem at y 18)
    s.append(R(16, 11.1, 20, 14.1, "#b14c3a"))                                 # stem
    s.append(R(37.5, 6.1, 52.5, 11.1, "#3a3a3a", MUTE, 0.15, "0.8 0.6"))      # sharp switch (other plane)
    s.append(R(26.5, 6.1, 30.5, 8.1, "#111"))                                  # SS49E flat, 10.5 mm from the stem
    if style in ("short", "short-ply"):
        topc = "#e9c58f" if style == "short-ply" else "#fbf9f4"
        s.append(R(3.5, 11.0, 58, 12.5, "#2a2522" if style == "short" else PLYE))   # switch plate
        s.append(R(3.5, 14.1, 33.5, 17.1, topc))                               # short top, cross pocket on the stem
        s.append(R(26.1, 13.7, 30.9, 15.3, "#8a8f96"))                          # D31 magnet, face 7.6 above strip
        s.append(R(37, 16.5, 53, 19.5, "#d7a86e" if style == "short-ply" else "#2b2826", MUTE, 0.15, "0.8 0.6"))
        lipz = 22
    elif style == "piano":
        s.append(R(3, 14.1, 59, 17.1, "#fbf9f4"))                               # long piano top
        s.append(R(26.1, 13.7, 30.9, 15.3, "#8a8f96"))
        s.append(R(6, 11.0, 50, 11.8, "#c0c0c0", MUTE, 0.15, "1 0.6"))          # Choc V2 stabiliser wire (dashed)
        s.append(R(23, 17.1, 54.5, 19.9, "#2b2826", MUTE, 0.15, "0.8 0.6"))
        lipz = 22
    else:
        s.append(R(14, 14.1, 22, 17.1, "#d9d6cf"))                              # blank 1u cap (narrow in section)
        s.append(R(26.1, 13.7, 30.9, 15.3, "#8a8f96"))
        s.append(R(3, 17.6, 78, 19.1, FELT))
        s.append(R(3, 19.1, 78, 22.1, PLYC))
        s.append(R(-3, 22.1, 78, 25.1, FELT))
        s.append(R(15, 17.1, 21, 28.1, "#e2c290"))                              # shank
        s.append(f'<path d="M {Y(11.65)} {Z(28.1)} L {Y(24.35)} {Z(28.1)} Q {Y(24.35)} {Z(32.1)} {Y(18)} {Z(32.3)} Q {Y(11.65)} {Z(32.1)} {Y(11.65)} {Z(28.1)} Z" fill="#e2c290" stroke="{INK}" stroke-width="0.2"/>')
        s.append(R(11.65, 22.1, 15, 25.1, "#7f7d7a")); s.append(R(21, 22.1, 24.35, 25.1, "#7f7d7a"))
        lipz = None
    # front wall
    if concept == "hymnal":
        s.append(R(-37, 0, 0, 3, CEDAR, INK, 0.2))
        s.append(R(0, 3, 3, 37, CEDAR, MUTE, 0.15, "1 0.8"))
        s.append(t(Y(-36), Z(5.5), "front wall dropped (open)", 1.9, INK))
        s.append(t(Y(3.6), Z(35), "closed position", 1.7, MUTE))
    elif concept == "hush":
        s.append(R(-3, 3, 0, 22.1, FELT)); s.append(R(0, 3, 3, 19, PLYC))
    else:
        s.append(R(0, 3, 3, 15, body))
    # lip / step / panel per concept
    if concept == "type-case":
        s.append(R(55, 19, 78, 22, PLYC))
        s.append(R(78, 22, 81, 40, PLYC))
        s.append(R(76.4, 22, 77.9, 40, PLYC)); s.append(R(77.9, 29, 78, 37.4, "#ffffff"))
        s.append(R(81, 24, D - 3, 27, "#2a2522"))
        s.append(R(D - 3, 3, D, 40, PLYC))
        s.append(R(126, 27, 129, 34, PLYC))
    elif concept == "one-sheet":
        s.append(R(55, 19, 78, 22, PLYC))
        s.append(R(78, 24, D - 3, 27, PLYC))
        s.append(R(D - 3, 3, D, 27, PLYC))
    elif concept == "hymnal":
        s.append(R(55, 17.3, 78, 19.0, FELT))
        s.append(R(55, 19.0, 78, 22.0, PLYC)); s.append(R(55, 22.0, 78, 22.25, "#efe4c9"))
        s.append(R(78, 23, D - 3, 26, PLYC))
        s.append(R(D - 3, 3, D, 37, CEDAR))
        s.append(R(0, 37, D, 40, CEDAR, MUTE, 0.2, "1.2 0.8"))
        s.append(t(Y(60), Z(41.2), "lid, closed (40 mm): the CUTOFF knob sits in a 2 mm pocket in its underside", 1.9, MUTE))
    else:
        s.append(R(78, 24, D, 27, PLYC)); s.append(R(78, 27, D + 3, 30, FELT))
        s.append(R(D, 3, D + 3, 27, FELT))
        s.append(f'<circle cx="{Y(D+16):.2f}" cy="{Z(16):.2f}" r="{13.5*sc:.2f}" fill="{FELT}" stroke="{INK}" stroke-width="0.2"/>')
    # main board + pot + knob (CUTOFF column y=104)
    plytop = 27 if concept == "hush" else pz
    bz = plytop - 3 - 8.6
    s.append(R(82, bz - 1.6, D - 6, bz, "#2f6b4f"))
    s.append(R(99, bz, 109, plytop - 3, "#555"))
    kz = plytop + 0.5
    s.append(R(104 - 10.4, kz, 104 + 10.4, kz + 12.15, "#efe5cb"))
    s.append(R(127 - 7.43, kz, 127 + 7.43, kz + 10.45, "#efe5cb" if concept != "hymnal" else "#b8432a"))
    s.append(R(150 - 7.43, kz, 150 + 7.43, kz + 10.45, "#efe5cb" if concept != "hymnal" else "#b8432a"))
    # speaker under the board, battery
    s.append(R(110, 3.5, 150, 12, "#8aa0b0", BLUE, 0.2)); s.append(t(Y(130), Z(7), "speaker (thin, E-L2)", 1.7, INK, "middle"))
    # z scale
    for zz in (0, 10, 20, 30, 40):
        s.append(line(Y(-8 if concept != "hymnal" else -44), Z(zz), Y(D + 34), Z(zz), "#d8d2c8", 0.12, "0.6 0.8"))
        s.append(t(Y(-9 if concept != "hymnal" else -45), Z(zz) + 0.7, f"{zz}", 1.8, MUTE, "end"))
    # labels (common)
    s.append(L(45, 5.3, "strip C (printed board)", 40, -9, INK))
    s.append(L(18, 9, "Kailh Choc V2 silent switch (bought), soldered", 55, -14, INK))
    s.append(L(28.5, 7.5, "flat Hall sensor (SS49E)", 70, -4, INK))
    if style in ("short", "short-ply"):
        s.append(L(28, 14.5, "D31 magnet in the top, over the flat sensor: velocity", 6, 36, INK))
        s.append(L(18, 16.5, "short top pressed onto the stem" + (" (cut from the same birch sheet)" if style == "short-ply" else " (laser-cut acrylic)"), 6, 42, INK))
        s.append(L(45, 18.5, "sharp, rear row (other plane)", 56, 33, MUTE))
    elif style == "piano":
        s.append(L(28, 14.5, "D31 magnet in the top: velocity", 6, 36, INK))
        s.append(L(30, 11.4, "Choc V2 stabiliser (+$29.85 for 15 whites)", 70, -9, INK))
        s.append(L(40, 16.5, "full-length piano top, tail tucked under the lip", 6, 42, INK))
        s.append(L(66, 18, "felt under the lip: no tick if a tail lifts", 60, 49, ACC))
    else:
        s.append(L(18, 31, "maple button peg (bought), glued to a blank cap", 6, 44, INK))
        s.append(L(13, 23.6, "felt collar wipes the peg; the head lands on felt = silent bottom stop", 30, 50, ACC))
    s.append(L(104, kz + 12, "CUTOFF 12.15 mm", 104, kz + 18, INK, anchor="middle"))
    s.append(L(150, kz + 10.45, f"knob tops {kz + 10.45:.1f}", 150, kz + 16, INK, anchor="middle"))
    return "\n".join(s)

# ------------------------------------------------------------------ ONE SHEET nest (sheet coords, mm)
SHEET_W, SHEET_L = 304.8, 609.6

def band_profile(length, segs):
    """segs: list of (s0, s1, height); returns polygon points of an unfolded band (s along x, height down)."""
    pts = [(0, 0), (length, 0)]
    back = []
    for s0, s1, hgt in reversed(segs):
        back += [(s1, hgt), (s0, hgt)]
    return pts + back

def nest_parts():
    """Return list of parts: dict(name, id, poly or rect, x, y, w, h, notes). Coordinates: sheet x across 305, y along 610."""
    P = []
    R10 = 10
    # bottom: 298 along sheet y, 180 across x
    P.append(dict(id="B", name="bottom (nest map engraved; battery hatch = its own offcut)", x=3, y=5, w=180, h=298, kind="bottom"))
    arc = math.pi / 2 * (R10 - 1.5)
    la = 288 + arc + 170
    lb = 288 + arc + 167
    P.append(dict(id="LA", name=f"L-band A: front + left, one kerf corner ({la:.0f} long)", x=186, y=5, w=24, h=la, kind="bandA",
                  segs=[(0, 288 + arc, 16), (288 + arc, 288 + arc + 68, 23.2), (288 + arc + 68, la, 24)], kerf=(288, 288 + arc)))
    P.append(dict(id="LB", name=f"L-band B: rear + right, one kerf corner ({lb:.0f} long)", x=212, y=5, w=24, h=lb, kind="bandB",
                  segs=[(0, 288 + arc + 92, 24), (288 + arc + 92, lb, 23.2)], kerf=(288, 288 + arc)))
    P.append(dict(id="L", name="lip (key-name ruler)", x=240, y=5, w=23, h=292, kind="rect"))
    P.append(dict(id="P", name="control panel", x=3, y=308, w=99, h=292, kind="panel"))
    # small parts region x 106-183, y 308-600 and x 235-300, y 300-600
    P.append(dict(id="ST", name="stick-column top", x=108, y=308, w=22, h=52, kind="rect"))
    P.append(dict(id="GT", name="gate plate", x=134, y=308, w=26, h=30, kind="rect"))
    for k in range(4):
        P.append(dict(id=f"C{k+1}", name="corner block" if k == 0 else "", x=164, y=308 + k * 14, w=12, h=12, kind="rect"))
    for k in range(8):
        P.append(dict(id=f"F{k+1}", name="foot disc" if k == 0 else "", x=108 + (k % 4) * 19, y=366 + (k // 4) * 19, w=17, h=17, kind="disc"))
    P.append(dict(id="HL", name="hatch ledges", x=108, y=408, w=6, h=50, kind="rect"))
    P.append(dict(id="HL2", name="", x=117, y=408, w=6, h=50, kind="rect"))
    P.append(dict(id="SB", name="speaker baffle ring", x=128, y=408, w=50, h=50, kind="ring"))
    P.append(dict(id="BB", name="battery cradle", x=108, y=464, w=70, h=40, kind="rect"))
    P.append(dict(id="JB", name="jack-edge doubler", x=108, y=510, w=20, h=88, kind="rect"))
    P.append(dict(id="KC", name="patch-card", x=132, y=510, w=46, h=88, kind="rect"))
    for k in range(15):
        P.append(dict(id=f"K{k+1}", name="white key tops ×15" if k == 0 else "", x=238 + (k % 3) * 20, y=304 + (k // 3) * 32, w=17.2, h=30, kind="rect"))
    for k in range(10):
        P.append(dict(id=f"S{k+1}", name="sharp tops ×10" if k == 0 else "", x=238 + (k % 4) * 15.5, y=466 + (k // 4) * 18, w=14, h=16, kind="rect"))
    P.append(dict(id="SP", name="spare", x=238, y=522, w=62, h=78, kind="spare"))
    P.append(dict(id="SP2", name="spare", x=266, y=5, w=34, h=292, kind="spare"))
    P.append(dict(id="SP3", name="spare", x=186, y=480, w=50, h=120, kind="spare"))
    return P

def nest_svg(ox, oy, sc, rotate=True):
    """Nest drawing. rotate=True lays the 610 length horizontally: sheet y -> drawing x, sheet x -> drawing y."""
    def T(x, y):
        return (ox + y * sc, oy + x * sc) if rotate else (ox + x * sc, oy + y * sc)
    def RR(x, y, w, h, fill, stroke=INK, sw=0.25, dash=None, rx=0):
        (ax, ay) = T(x, y); (bx, by) = T(x + w, y + h)
        d = f' stroke-dasharray="{dash}"' if dash else ""
        return f'<rect x="{min(ax,bx):.2f}" y="{min(ay,by):.2f}" width="{abs(bx-ax):.2f}" height="{abs(by-ay):.2f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
    s = []
    s.append(RR(0, 0, SHEET_W, SHEET_L, "#efd9b6", INK, 0.4))
    # grain lines along the sheet length
    for k in range(0, int(SHEET_W), 6):
        (ax, ay) = T(k + 2, 0); (bx, by) = T(k + 2, SHEET_L)
        s.append(f'<line x1="{ax:.2f}" y1="{ay:.2f}" x2="{bx:.2f}" y2="{by:.2f}" stroke="#e2c9a0" stroke-width="0.25"/>')
    parts = nest_parts()
    used = 0
    for p in parts:
        x, y, w, h = p["x"], p["y"], p["w"], p["h"]
        if p["kind"] == "spare":
            s.append(RR(x, y, w, h, "none", MUTE, 0.25, "2 1.5"))
        elif p["kind"] in ("bandA", "bandB"):
            # unfolded band: along y (length), width = max height; profile steps drawn
            pts = []
            for s0, s1, hh in p["segs"]:
                pts += [(x, y + s0), (x, y + s1)]
            poly = [(x, y)] + [(x, y + p["segs"][-1][1])]
            path = f"M {T(x, y)[0]:.2f} {T(x, y)[1]:.2f} "
            path += f"L {T(x, y + p['segs'][-1][1])[0]:.2f} {T(x, y + p['segs'][-1][1])[1]:.2f} "
            for s0, s1, hh in reversed(p["segs"]):
                a = T(x + hh, y + s1); b = T(x + hh, y + s0)
                path += f"L {a[0]:.2f} {a[1]:.2f} L {b[0]:.2f} {b[1]:.2f} "
            path += "Z"
            s.append(f'<path d="{path}" fill="#f6e7cc" stroke="{INK}" stroke-width="0.3"/>')
            k0, k1 = p["kerf"]
            hk = p["segs"][0][2]
            n = 14
            for i in range(n):
                yy = y + k0 + (k1 - k0) * (i + 0.5) / n
                off = 2 if i % 2 else 0
                a = T(x + 1 + off, yy); b = T(x + hk - 1 - (2 - off), yy)
                s.append(f'<line x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{b[0]:.2f}" y2="{b[1]:.2f}" stroke="{ACC}" stroke-width="0.25"/>')
            used += sum((s1 - s0) * hh for s0, s1, hh in p["segs"])
        elif p["kind"] == "disc":
            c = T(x + w / 2, y + h / 2)
            s.append(f'<circle cx="{c[0]:.2f}" cy="{c[1]:.2f}" r="{w/2*sc:.2f}" fill="#f6e7cc" stroke="{INK}" stroke-width="0.3"/>')
            used += math.pi * (w / 2) ** 2
        elif p["kind"] == "ring":
            c = T(x + w / 2, y + h / 2)
            s.append(f'<circle cx="{c[0]:.2f}" cy="{c[1]:.2f}" r="{w/2*sc:.2f}" fill="#f6e7cc" stroke="{INK}" stroke-width="0.3"/>')
            s.append(f'<circle cx="{c[0]:.2f}" cy="{c[1]:.2f}" r="{(w/2-6)*sc:.2f}" fill="#efd9b6" stroke="{INK}" stroke-width="0.3"/>')
            used += math.pi * ((w / 2) ** 2 - (w / 2 - 6) ** 2)
        else:
            s.append(RR(x, y, w, h, "#f6e7cc", INK, 0.3))
            used += w * h
            if p["kind"] == "bottom":
                # rounded corners note, speaker grille slots, battery hatch (own offcut), keyholes
                c = T(x + 180 - 128, y + 170)
                for r in range(4, 37, 5):
                    s.append(f'<circle cx="{c[0]:.2f}" cy="{c[1]:.2f}" r="{r*sc:.2f}" fill="none" stroke="{INK}" stroke-width="0.2" stroke-dasharray="{3*sc:.2f} {1.6*sc:.2f}"/>')
                s.append(RR(x + 120, y + 30, 40, 60, "#f6e7cc", ACC, 0.35))
                hx, hy = T(x + 140, y + 60)
                s.append(t(hx, hy, "hatch = own offcut", 6 * sc, ACC, "middle"))
                for kx in (60, 240):
                    a = T(x + 160, y + kx)
                    s.append(f'<circle cx="{a[0]:.2f}" cy="{a[1]:.2f}" r="{3*sc:.2f}" fill="none" stroke="{INK}" stroke-width="0.25"/>')
            if p["kind"] == "panel":
                for lab, kx, ky, kind, midi in KNOBS:
                    # panel coords: panel x 3..295 -> along sheet y; panel y 78..177 -> across sheet x
                    a = T(x + (ky - 78), y + (kx - 3))
                    r = 3.6 if kind != "rot" else 4.6
                    s.append(f'<circle cx="{a[0]:.2f}" cy="{a[1]:.2f}" r="{r*sc:.2f}" fill="#efd9b6" stroke="{INK}" stroke-width="0.2"/>')
                for lab, kx, ky, n in TOGGLES:
                    a = T(x + (ky - 78), y + (kx - 3))
                    s.append(f'<circle cx="{a[0]:.2f}" cy="{a[1]:.2f}" r="{3.2*sc:.2f}" fill="#efd9b6" stroke="{INK}" stroke-width="0.2"/>')
        if p["name"]:
            cx, cy = T(x + w / 2, y + h / 2) if p["kind"] not in ("bandA", "bandB") else T(x + w + 0.5, y + 150)
            if p["kind"] in ("bandA", "bandB"):
                cx, cy = T(x + p["segs"][0][2] / 2, y + 150)
            fs = 2.6 if w * h > 4000 else 1.9
            if p["kind"] in ("bottom", "panel", "spare"):
                fs = 3.2
            lab = f'{p["id"]}  {p["name"]}'
            s.append(t(cx, cy + 0.9, lab, fs, INK, "middle", weight="bold" if p["kind"] in ("bottom", "panel") else "normal"))
    return "\n".join(s), used
