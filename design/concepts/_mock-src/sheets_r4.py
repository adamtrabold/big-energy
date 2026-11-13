#!/usr/bin/env python3
"""Round 4 sheets (A3, 300 dpi): A look · B real-size top · C construction section. python3 sheets_r4.py [hush one-sheet fold]"""
import os, sys
from sheets import img, para, head, write, OUT, ROOT
from drawings import t, rect, line, circ, dim_h, dim_v, INK, MUTE, ACC, PAPER
import r4

GREEN = "#2f6b4f"; FELTC = "#8b8986"; SHELL = "#b9b6b0"; WAL = "#6b4429"; PGC = "#f1ebdd"; BLK = "#1d1c1b"
CREAMK = "#ece2c6"; PCRM = "#e8dcc2"; PLY = "#c99b62"; POT = "#2b55a0"; STEEL = "#8e9296"; BRASS = "#c2a25e"
FOOT_TAG = "Round 4 · drawn to systems rev 7.2 (common 6.1, fold 4.2: eng round-4 answers + internal battery) · name to come"

# ------------------------------------------------------------------ section helpers (y right, z up)
class Sec:
    def __init__(self, ox, oy, sc):
        self.ox, self.oy, self.sc, self.s = ox, oy, sc, []
    def X(self, y): return self.ox + y * self.sc
    def Z(self, z): return self.oy - z * self.sc
    def R(self, y0, z0, y1, z1, fill, stroke=INK, sw=0.15, dash=None, op=1.0):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.s.append(f'<rect x="{self.X(min(y0,y1)):.2f}" y="{self.Z(max(z0,z1)):.2f}" width="{abs(y1-y0)*self.sc:.2f}" '
                      f'height="{abs(z1-z0)*self.sc:.2f}" fill="{fill}" fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
    def P(self, pts, fill, stroke=INK, sw=0.15, close=True):
        d = "M " + " L ".join(f"{self.X(y):.2f} {self.Z(z):.2f}" for y, z in pts) + (" Z" if close else "")
        self.s.append(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    def C(self, y, z, r, fill, stroke=INK, sw=0.15, dash=None):
        self.s.append(circ(self.X(y), self.Z(z), r * self.sc, fill, stroke, sw, dash))
    def L(self, y0, z0, y1, z1, col=INK, sw=0.2, dash=None):
        self.s.append(line(self.X(y0), self.Z(z0), self.X(y1), self.Z(z1), col, sw, dash))
    def note(self, y, z, ty, tz, text, col=INK, size=2.0, anchor="start"):
        self.L(y, z, ty, tz, col, 0.15)
        dx = 0.8 if anchor == "start" else -0.8
        self.s.append(t(self.X(ty) + dx, self.Z(tz) + 0.7, text, size, col, anchor))
    def screw_up(self, y, z_head, length, col=STEEL):
        """M3 screw driven up from underneath: head at z_head (bottom), shank upward."""
        self.R(y - 2.75, z_head - 0.0, y + 2.75, z_head + 1.6, col, INK, 0.12)
        self.R(y - 1.5, z_head + 1.6, y + 1.5, z_head + length, col, INK, 0.12)
    def svg(self): return "\n".join(self.s)

def rounded_profile(y0, y1, H, rt, rb, n=10):
    """outline of a block section: flat bottom, bottom round rb, vertical, top round rt, flat top (both ends)."""
    import math
    pts = []
    for k in range(n + 1):                 # front bottom round (centre y0+rb, rb)
        a = math.pi + (math.pi / 2) * k / n
        pts.append((y0 + rb + rb * math.cos(a), rb + rb * math.sin(a)))
    pts = pts[::-1]
    out = [(y0 + rb, 0)] + [(y1 - rb, 0)]
    for k in range(n + 1):
        a = -math.pi / 2 + (math.pi / 2) * k / n
        out.append((y1 - rb + rb * math.cos(a), rb + rb * math.sin(a)))
    for k in range(n + 1):
        a = (math.pi / 2) * k / n
        out.append((y1 - rt + rt * math.cos(a), H - rt + rt * math.sin(a)))
    for k in range(n + 1):
        a = math.pi / 2 + (math.pi / 2) * k / n
        out.append((y0 + rt + rt * math.cos(a), H - rt + rt * math.sin(a)))
    for k in range(n + 1):
        a = math.pi + (math.pi / 2) * k / n
        out.append((y0 + rb + rb * math.cos(a), rb + rb * math.sin(a)))
    return out

def knob_sec(S, y, zb, d=14.86, h=10.45, col=CREAMK, hero=False):
    w = d / 2
    S.P([(y - w, zb), (y + w, zb), (y + w * 0.9, zb + h), (y - w * 0.9, zb + h)], col, INK, 0.15)

def pot_sec(S, y, zb, ztop_bush):
    S.R(y - 4.75, zb, y + 4.75, zb + 7, POT, INK, 0.12)
    S.R(y - 3.5, zb + 7, y + 3.5, ztop_bush, "#9a9da1", INK, 0.1)

# ------------------------------------------------------------------ concept content
H_CONTENT = dict(
    folder="hush", title="HUSH",
    kind="a material · sauce · printed pebble shell, one wool-felt skin · unibody, shut from below",
    idea="The material that makes it quiet is the whole outside: one seamless skin of grey wool felt blocked over a soft printed pebble, maple pegs rising through it, and every screw underneath.",
    main="r4_hu_main.png",
    main_caption="290 × 176. The felt runs over the top, round every edge and under; pegs start at the brow of the front curve, so the keys meet the edge. Section names, break rules and the jack legend are pressed into the felt, not printed. Cream knobs sit on printed tags that carry the scales.",
    second="r4_hu_low.png",
    second_caption="Low from the left: r 12 over the top, a short side, r 6 under, R 20 front and R 44 rear corners. Nothing to catch: no seam, no screw, no edge.",
    principles=[
        ("One skin, no edges.", "a soft object should have nothing to catch or pick at: the shell is rounded so a wool hat hood can be steam-blocked over it (the shell is the hat block), and the felt ends only underneath."),
        ("The skin is a working part.", "if felt makes it quiet, the felt you see must work: each maple peg lands on its own punched felt collar, the silent bottom stop (after the velocity window, eng E-L5)."),
        ("Nothing hard touches the hand except what plays.", "silence is also what hands meet: pegs, knobs and stick are hard; everything else is wool."),
        ("Nothing shouts; even the words are pressed.", "a quiet instrument shouldn't be loud to look at: grey wool, maple, cream. Names, rules and the jack legend are blind-pressed with a hot brass die (letterpress with no ink); the fine scales live on printed tags, because felt can't hold a fine mark."),
        ("Shut from below.", "the owner's unibody: the top carries only what you play. The felt's binding ring and the back panel screw on underneath, and opening the back never releases the skin."),
    ],
    inset="hush",
    facts=[
        ("ENCLOSURE", "≈ $30–55 (systems ESTIMATE): shell ≈ $4–5; the skin is most of it (hood $15–35 UNVERIFIED, or F3 12 × 24 in ≈ $25–30)."),
        ("BUILD", "≈ 10–12 h printing (2 halves; the felt hides the joint) + block the felt overnight + ≈ 4–5 h assembly."),
        ("THICKNESS", "Felt 25.5, peg heads ≈ 32, knob tops ≈ 36, CUTOFF ≈ 37.6 (cream KN1250 on round-shaft pots; 18T push-on would be ≈ 39)."),
        ("KEYS", "25 ½-in maple mushroom pegs on Choc V2 silent; whites pale, sharps a darker cut. Front peg heads 13 mm from the front: the felt rolls away right in front of them."),
        ("UNIBODY", "One closed-top shell, loaded from below. 10 + 8 screws, all underneath; nothing on the top or sides. Battery bay under the main board: back panel off."),
        ("THE OWNER'S HAND", "The rear band (eng's extra 30 mm) holds the pressed jack legend and a blank name line, to press or stitch."),
    ],
    foot="Knobs: Tayda KN1250 cream (set-screw, 6.4 bore) on Tayda A-5518 round 6.35 shaft pots ($0.59, the same as the A-5622 spline), so HUSH stays cream; CUTOFF Tayda 1083 cream. Felt: grey wool hood, steam-blocked; F3 with 4 hidden darts is the fallback. Pressed legends: test on an offcut (heat, dwell). Findings for systems: the I/O board must sit in the rear wall's straight run (x ≈ 60–230; the R 44 corners leave no straight wall past x 246); the 50 mm speaker at (247, 113) overlaps the binding ring by ≈ 2 mm (move it to x ≤ 243).",
)

O_CONTENT = dict(
    folder="one-sheet", title="ONE SHEET",
    kind="an economy · designed for use · one printed shell, one filament · unibody, opened from below",
    idea="One closed shell, printed face down in one filament with one swap. The nozzle's own first-layer lines are the finish, and the face is opened only from behind.",
    main="r4_os_main.png",
    main_caption="276 × 170. One cream face with holes only for what you play. Keys run to a 2.4 mm front wall flush with their tops. Sections read by line direction (drawn 2.5× coarse) and 0.6 mm sunk grooves. The rear band carries the jack legend over the rear-wall ports.",
    second="r4_os_under.png",
    second_caption="From below: 3 mm ply back panel on 8 × M3 into inserts in the shell's rim, feet, speaker holes, keyhole. Every fastener is here.",
    principles=[
        ("One face.", "in an economy you don't add a line the drawing doesn't already have: the top is one closed surface. If the bed forces a split, it sits at x 122.5, at the bottom of a break groove you'd see anyway."),
        ("The toolpath is the finish.", "the nozzle draws every line anyway: per-section direction (a checkerboard of ±45°) and rings under the knobs are set by slicer modifiers, and the perimeter loops round the outside and the key window come free. It costs $0."),
        ("Face down on smooth steel.", "the first layer is FDM's best surface, and smooth PEI shows line direction as sheen. Layer lines stay inside."),
        ("One filament, one swap.", "legends are cut-outs in the first 0.6 mm, filled dark by one change. The knobs are bought to match the filament."),
        ("Opened from behind.", "every screw is underneath, one M3 size into brass inserts, so the face stays whole and reprintable from the 3MF."),
    ],
    inset="toolpath",
    facts=[
        ("ENCLOSURE", "≈ $10–13 (systems ESTIMATE): ≈ 200 g filament, inserts, a ply back panel. The finish adds $0. Still the cheapest."),
        ("BUILD", "≈ 10–12 h printing: one piece on a 350 bed (Voron, UNVERIFIED), or two parts split at x 122.5 on a Prusa."),
        ("THICKNESS", "Face 24, knob tops ≈ 34.5, CUTOFF ≈ 36.1 (cream KN1250 on round-shaft pots; 18T push-on would be ≈ 37.5)."),
        ("KEYS", "25 short acrylic tops on Choc V2 silent, whites from 3 mm behind the front face. The front wall is the only thing in front of them."),
        ("UNIBODY", "One shell, top and walls in one. 8 screws, all underneath; no outside jack nuts. Battery bay under the main board (x 20–150): back panel off."),
        ("THE OWNER'S HAND", "The rear band holds the jack legend and the print's own label line; the name goes there when there is one."),
    ],
    foot="Knobs: Tayda KN1250 cream on Tayda A-5518 round 6.35 shaft pots ($0.59); CUTOFF Tayda 1083 cream, red line. Toolpath: per-region bottom-layer angle by PrusaSlicer modifier meshes is UNVERIFIED. The director's test coupon (≈ 80 × 80, +45 / −45 / rings, smooth PEI, raking light) hasn't been printed yet: until it is, the line fields on these sheets are an illustration, drawn 2.5× coarse (a true-scale swatch is in the inset).",
)

F_CONTENT = dict(
    folder="fold", title="FOLD",
    kind="a hinge · designed for use · walnut-tone blocks with white pickguards · self-protecting",
    idea="Each half is a hollowed walnut block with a white pickguard dropped in and screwed from behind. The keys' half holds what you play, the lid holds the voice, and it closes into a flat-topped walnut bar.",
    main="r4_fo_main.png",
    main_caption="Open, 286 × 234, printed in walnut-tone wood-fill filament (the first build). Cream pickguards, black knobs, red CUTOFF, black lowercase legends: Proof's colours. Keys run to a 4 mm rim. A white-over-black bevel lines every pickguard edge. The base's rear strip carries a printed map of the signal.",
    second="r4_fo_closed_wal.png",
    second_caption="Closed, 286 × 116 × ≈ 50, in his planed walnut (later, CNC-pocketed from the same model), beside a 400-page hardback. On top (the lid's back): 6 brass screws, 4 cork pads, 2 push-out holes.",
    principles=[
        ("Block and pickguard.", "it's the owner's guitar: one solid body per half, rounded edges, flat top and bottom; one white plate carries everything, drops in and is screwed from behind. No screw on the white face."),
        ("The swap draws the pickguard's line.", "a pickguard's bevel shows its layers: the plate prints face down, white for 1.0 mm, then black. A 45° bevel round the outline and the key window shows a white band over a black line, made by the same swap that fills the legends. $0."),
        ("Proof's colours, each from its material.", "that's the look he asked to go back to: walnut-tone body (wood-fill first, his walnut later), cream pickguard, black 18T knobs, red CUTOFF, black legends."),
        ("The fold line is the logic line.", "PLAY in the base, VOICE on the lid. EMPHASIS is the one crossing (eng: it stays by the ladder), so the base keeps a printed ring where it parks when closed: 'emphasis is on the lid'."),
        ("Open flat, closed a bar.", "a fold earns its hinge twice: open, the lid lies flat at 180° with nothing raised; closed, it's a walnut bar that guards its own knobs. No case."),
    ],
    inset="fold",
    facts=[
        ("ENCLOSURE", "≈ $20–26 printed (systems ESTIMATE; filament ≈ $8–10). Walnut later: his stock and CNC time. Battery: 2 pouch cells in the lid band, under the pickguard (eng to confirm the cell)."),
        ("BUILD", "Blocks in one piece on a 350 bed, or lap-split at x 127.5; plates split at x 127.5 in a break groove. ≈ 18–22 h printing."),
        ("THICKNESS", "Closed ≈ 50.1 (unchanged). Open: keys 17.5, base plate 15.6, lid plate 15.1, black knob tops ≈ 29.1."),
        ("KEYS", "25 short acrylic tops, white and smoke black, on Choc V2 silent. Whites start 4.5 mm from the front: only the block's rim is in front."),
        ("SCREWS", "6 per half, up through the block's back into standoffs on the pickguard. Base: underneath. Lid: brass, on the back."),
        ("THE OWNER'S HAND", "A blank name line in the lid band, over the battery bay. The walnut is his to plane."),
    ],
    foot="Knobs: Tayda plastic black 18T push-on, 14.5 × 13.5, white indicator, on Tayda A-5622 T18 spline pots. CUTOFF: Tayda 1083 RED (the same serrated pointer as the cream one, 20 × 12, set-screw); give CUTOFF a round-shaft A-5518 pot so the set-screw seats. Visual proposals for systems: the base's empty rear strip (y 82–112) carries a printed signal map; the lid back gets brass screws and 4 inlaid cork pads. Hinge knuckles at the rear corners only.",
)

CONTENT = {"hush": H_CONTENT, "one-sheet": O_CONTENT, "fold": F_CONTENT}

# ------------------------------------------------------------------ insets for sheet A
def inset_hush(x, y, w, h):
    s = [rect(x, y, w, h, "#ece7de", "#d8d0c2", 0.25)]
    i, b = img(os.path.join(OUT, "r4_hu_under.png"), x + 1, y + 1, 95, h - 2)
    s.append(i)
    p, _ = para(x + 100, y + 6, "UNDERNEATH: the felt turns under the r 6 edge and ends 15 mm in, clamped by a printed binding ring (10 × M3). The back panel sits inside the ring on its own 8 × M3, with the feet, the speaker grille and the keyhole (J18). Opening the back never releases the felt.", 72, 2.15)
    s.append(p)
    p, _ = para(x + 100, y + 22, "WEAR: collars are punched rings, lifted out with the peg; the skin comes off whole (pull knobs, tags and pegs; undo the ring) and is brushed, steamed, re-blocked or replaced.", 72, 2.15, fill="#4a443d")
    s.append(p)
    return "\n".join(s)

def inset_toolpath(x, y, w, h):
    import math
    s = [rect(x, y, w, h, "#ece7de", "#d8d0c2", 0.25)]
    def swatch(sx, sy, sw, sh, ang, pitch, base, ln, label, ring=False):
        g = [f'<clipPath id="c{int(sx*10)}{int(sy*10)}"><rect x="{sx}" y="{sy}" width="{sw}" height="{sh}"/></clipPath>',
             f'<g clip-path="url(#c{int(sx*10)}{int(sy*10)})">', rect(sx, sy, sw, sh, base, "none", 0)]
        if ring:
            cx, cy = sx + sw / 2, sy + sh / 2
            r = 1.0
            while r < max(sw, sh):
                g.append(circ(cx, cy, r, "none", ln, pitch * 0.42)); r += pitch
        else:
            th = math.radians(ang); L = sw + sh
            k = -L
            while k < L:
                x0 = sx + sw / 2 + k * math.cos(th + math.pi / 2) - L * math.cos(th)
                y0 = sy + sh / 2 + k * math.sin(th + math.pi / 2) - L * math.sin(th)
                g.append(line(x0, y0, x0 + 2 * L * math.cos(th), y0 + 2 * L * math.sin(th), ln, pitch * 0.42))
                k += pitch
        g.append("</g>"); g.append(rect(sx, sy, sw, sh, "none", "#b9ab90", 0.2))
        g.append(t(sx, sy + sh + 3, label, 1.9, INK))
        return "\n".join(g)
    s.append(t(x + 2, y + 4.5, "THE FACE, MAGNIFIED (drawn 1.1 mm pitch)", 2.1, ACC, weight="bold"))
    s.append(swatch(x + 2, y + 6.5, 18, 18, -45, 1.1, "#e0d1b0", "#c8b48d", "+45°: P1, P3, III"))
    s.append(swatch(x + 23, y + 6.5, 18, 18, 45, 1.1, "#f1e9d7", "#e2d5bb", "−45°: P2, II, IV"))
    s.append(swatch(x + 44, y + 6.5, 18, 18, 0, 1.1, "#f1e9d7", "#d9cbb0", "rings under knobs", ring=True))
    s.append(t(x + 68, y + 4.5, "TRUE SCALE (0.45 mm, a 0.4 nozzle)", 2.1, ACC, weight="bold"))
    s.append(swatch(x + 68, y + 6.5, 18, 18, -45, 0.45, "#e0d1b0", "#c8b48d", "+45° at 1:1"))
    s.append(swatch(x + 89, y + 6.5, 18, 18, 45, 0.45, "#f1e9d7", "#e2d5bb", "−45° at 1:1"))
    p, _ = para(x + 112, y + 6, "On smooth PEI the two directions read as sheen that flips as you move your head. The perimeter loops round the outside and the key window are free (the slicer draws them anyway); the ± 45° fields and the rings need modifier meshes (UNVERIFIED in PrusaSlicer). NOT YET PRINTED: the director's coupon decides whether the effect is real at true scale. If it reads faintly, ONE SHEET is the plain baseline.", 64, 2.0)
    s.append(p)
    return "\n".join(s)

def inset_fold(x, y, w, h):
    s = [rect(x, y, w, h, "#ece7de", "#d8d0c2", 0.25)]
    i, b = img(os.path.join(OUT, "r4_fo_closed.png"), x + 1, y + 1, 62, h - 2)
    s.append(i)
    s.append(t(x + 3, y + h - 2, "the first build: wood-fill walnut-tone PLA", 1.8, MUTE))
    # bevel detail at 6:1
    S = Sec(x + 84, y + 65.3, 3.5)
    S.R(-4, 9.8, 0, 15.6, WAL, INK, 0.15)                  # block rim
    S.R(0, 9.8, 0.3, 15.6, "#f3efe8", "none", 0)
    S.P([(0.3, 13.1), (0.3, 14.0), (0.9, 14.6), (1.9, 15.6), (8, 15.6), (8, 13.1)], BLK, INK, 0.12)
    S.P([(0.9, 14.6), (1.9, 15.6), (8, 15.6), (8, 14.6)], PGC, INK, 0.12)
    S.note(1.4, 15.1, 10, 17.4, "45° bevel: 1.0 mm white ...", INK, 1.8)
    S.note(0.6, 14.3, 10, 15.4, "... over 0.6 mm black", INK, 1.8)
    S.note(6, 13.6, 10, 11.2, "plate body: black (after the swap)", INK, 1.8)
    S.note(-2, 12, -2.5, 9.2, "walnut block", INK, 1.8, "end")
    s.append(S.svg())
    s.append(t(x + 66, y + 4.5, "THE PICKGUARD'S LINE · section at 3.5:1", 2.1, ACC, weight="bold"))
    p, _ = para(x + 172, y + 8, "One filament swap makes both the dark legends and the bevel's black line, round the outline and the key window, like a guitar's W/B pickguard. Swap at 1.0 mm (not 0.6) so the black doesn't grey through the white.", 58, 1.95)
    s.append(p)
    return "\n".join(s)

INSET = {"hush": inset_hush, "toolpath": inset_toolpath, "fold": inset_fold}

# ------------------------------------------------------------------ sheet A
def sheet_a(c):
    s = head(c["title"], c["kind"], c["idea"], "sheet A — the look", 4)
    i, box = img(os.path.join(OUT, c["main"]), 10, 41, 262, 146)
    s.append(i)
    cap, _ = para(12, 189.5, c["main_caption"], 205, 2.45, fill=MUTE, style="italic")
    s.append(cap)
    x0 = 280
    i2, b2 = img(os.path.join(OUT, c["second"]), x0, 41, 128, 60)
    s.append(i2)
    cap, yy = para(x0, b2[1] + b2[3] + 3, c["second_caption"], 72, 2.3, fill=MUTE, style="italic")
    s.append(cap)
    yy += 1.5
    s.append(t(x0, yy + 2, "PRINCIPLES (each follows from the idea)", 3.0, ACC, weight="bold"))
    yy += 6.5
    for k, (p, because) in enumerate(c["principles"], 1):
        hd, yy = para(x0, yy, f"{k}. {p}", 62, 2.8, weight="bold")
        s.append(hd)
        bc, yy = para(x0 + 3.5, yy, "because " + because, 74, 2.3, fill="#4a443d")
        s.append(bc)
        yy += 1.0
    s.append(INSET[c["inset"]](12, 200, 262, 34))
    s.append(line(12, 238, 408, 238, "#d8d0c2", 0.3))
    cw = 396 / len(c["facts"])
    for k, (hdr, val) in enumerate(c["facts"]):
        xx = 12 + k * cw
        s.append(t(xx, 244, hdr, 2.6, ACC, weight="bold"))
        v, _ = para(xx, 249, val, int(cw / 1.3), 2.4)
        s.append(v)
    fp, _ = para(12, 278, c["foot"], 270, 2.15, fill=MUTE)
    s.append(fp)
    s.append(t(408, 293, FOOT_TAG, 2.0, MUTE, "end"))
    return write(s, "mock-A-look", os.path.join(ROOT, c["folder"]))

# ------------------------------------------------------------------ sheet B (1:1)
B_INFO = {
    "hush": dict(top="r4_hu_top.png", box=(-2, -2, r4.HU_W + 2, r4.HU_D + 2), W=r4.HU_W, D=r4.HU_D, xo=7, rows=(68, 100, 123),
                 front_note="pegs' front heads 13 mm from the front edge; the felt rolls over r 12 right in front of them",
                 parts=[("Felt skin", "grey wool hood, steam-blocked over the shell; ends 15 mm underneath. Names, rules and jack legend blind-pressed."),
                        ("Tags", "light warm-grey print under every knob: the scale and the name, legends by one swap; flush in punched holes."),
                        ("Pegs", "½-in maple mushroom plugs, 25, on felt collars; sharps a darker cut of maple."),
                        ("Knobs", "cream KN1250 ×24 + MOD; cream 1083 CUTOFF with a red line."),
                        ("Rear band", "y 140–176: the jack legend over the rear-wall ports; a pressed name line, blank."),
                        ("Breaks", "pressed 1 mm rules in the felt at x 129.5 (full), y 85.4, x 235 (PLAY), x 188 (VOICE).")]),
    "one-sheet": dict(top="r4_os_top.png", box=(-2, -2, r4.OS_W + 2, r4.OS_D + 2), W=r4.OS_W, D=r4.OS_D, xo=0, rows=(68, 100, 123),
                 front_note="whites start 3 mm behind the front face; the 2.4 mm front wall is flush with their tops",
                 parts=[("Shell", "one cream PETG print, closed top, face down on smooth PEI; legends dark from one swap at 0.6 mm."),
                        ("Face", "first-layer lines: ±45° checkerboard per section, rings under knobs, perimeter loops round the edge and key window (drawn 2.5× coarse)."),
                        ("Grooves", "0.6 × 1.2 sunk at x 122.5 (full), y 85.4, x 228, x 181, y 141 (rear band)."),
                        ("Knobs", "cream KN1250 ×24 + MOD; cream 1083 CUTOFF, red line."),
                        ("Keys", "short acrylic tops, white and smoke black; Delrin gate plate flush."),
                        ("Rear band", "y 141–170: jack legend with tick marks over each port; the print's label line.")]),
    "fold": dict(top="r4_fo_top.png", box=(-2, -2, r4.FO_W + 2, 2 * r4.FO_H + 4), W=r4.FO_W, D=2 * r4.FO_H + 2, xo=5, rows=(68, None, None),
                 front_note="whites start 4.5 mm from the front: only the block's rounded rim is in front",
                 parts=[("Blocks", "walnut-tone wood-fill PLA, rounded edges (R 12 plan, R 6 outer face, R 3 meeting edges), flat top and bottom."),
                        ("Pickguards", "cream, printed face down: white 1.0 mm then black; 45° bevel shows a white band and a black line on every edge."),
                        ("Knobs", "black 18T push-on ×23 + MOD, white indicator; red 1083 CUTOFF with a cream line."),
                        ("Base", "keys, PLAY row (y 68), the EMPHASIS ring at x 169; the rear strip y 82–112 carries the printed signal map."),
                        ("Lid", f"EMPHASIS ({r4.EMPH[0]:.0f}, {r4.LY0 + r4.EMPH[1]:.0f}); grille slots x 208–262; blank name line over the battery bay; VOICE rows y {r4.LY0 + r4.VD_F:.2f} / {r4.LY0 + r4.VD_B:.2f}."),
                        ("Hinge", f"knuckles at the rear corners only; seam y {r4.FO_H:.0f}–{r4.FO_H + 2:.0f}; jacks + USB-C on the lid's right wall.")]),
}

def sheet_b(c):
    f = c["folder"]; b = B_INFO[f]
    s = head(c["title"], c["kind"], "Real size: print at 100 % on A3; the top view is 1:1, rendered straight down from the same model as sheet A (re-lit so whites read white).", "sheet B — top view, real size", 4)
    x0w, y0w, x1w, y1w = b["box"]
    ox, oy = (28, 43) if f == "fold" else (18, 47)
    i, _ = img(os.path.join(OUT, b["top"]), ox, oy, x1w - x0w, y1w - y0w, exact=True)
    s.append(i)
    X = lambda x: ox + (x - x0w)
    Y = lambda y: oy + (y1w - y)
    s.append(t(18, 41.5 if f == "fold" else 44.5, "TOP VIEW · 1:1 · front of the instrument at the bottom" + (" · open 180°" if f == "fold" else ""), 3.0, INK, weight="bold"))
    s.append(dim_h(X(0), X(b["W"]), Y(0) + 7, f"{b['W']:.0f} mm"))
    s.append(dim_v(X(b["W"]) + 6, Y(b["D"]), Y(0), f"{b['D']:.0f} mm" + (" open" if f == "fold" else "")))
    # front edge callout
    if f != "fold":
        s.append(line(X(b["W"] * 0.62), Y(0) + 1.0, X(b["W"] * 0.62), Y(0) + 12, ACC, 0.25))
        s.append(t(X(b["W"] * 0.62) + 1, Y(0) + 12, "KEYS TO THE FRONT EDGE: " + b["front_note"], 2.3, ACC, weight="bold"))
    # row callouts on the left margin
    xo = b["xo"]
    if f == "fold":
        for yy, lab in [(68, "PLAY row y 68"), (97, "base strip"), (r4.AX_Y, "hinge seam"), (r4.LY0 + r4.EMPH[1], "EMPHASIS"), (r4.LY0 + r4.VD_F, "VOICE front"), (r4.LY0 + r4.VD_B, "VOICE back")]:
            s.append(line(X(-6), Y(yy), X(-1), Y(yy), MUTE, 0.2)); s.append(t(X(-6.5), Y(yy) + 0.8, lab, 2.0, MUTE, "end"))
    else:
        for yy, lab in [(68, "PLAY y 68"), (85.4, "break 85.4"), (100, "VOICE 100"), (123, "VOICE 123"), (b["D"] - 18, "rear band")]:
            s.append(line(X(-6), Y(yy), X(-1), Y(yy), MUTE, 0.2)); s.append(t(X(-6.5), Y(yy) + 0.8, lab, 2.0, MUTE, "end"))
    xr = 336 if f != "hush" else 338
    yy = 49
    s.append(t(xr, yy, "PARTS YOU SEE", 3.0, ACC, weight="bold"))
    yy += 5.5
    for k, v in b["parts"]:
        hd, yy = para(xr, yy, k, 34, 2.6, weight="bold")
        s.append(hd)
        pv, yy = para(xr, yy, v, 40, 2.25, fill="#4a443d")
        s.append(pv)
        yy += 1.2
    if f == "fold":
        s.append(line(X(b["W"]) + 2, Y(10), 334, Y(10), ACC, 0.25))
        p_, _ = para(336, Y(10) - 1, "KEYS TO THE FRONT EDGE: " + b["front_note"] + ".", 36, 2.4, fill=ACC, weight="bold")
        s.append(p_)
    s.append(t(408, 293, FOOT_TAG, 2.0, MUTE, "end"))
    return write(s, "mock-B-real-size", os.path.join(ROOT, f))

# ------------------------------------------------------------------ sheet C (construction)
def sec_flat(S, D, kind):
    """section at x ≈ CUTOFF (front-to-back) through HUSH or ONE SHEET."""
    if kind == "hush":
        FT = 25.5
        S.P(rounded_profile(0, D, FT, 12, 6), FELTC, INK, 0.2)                  # felt (outer)
        S.P(rounded_profile(2, D - 2, FT - 2, 10, 4), SHELL, INK, 0.15)          # shell outer
        inner = rounded_profile(4.4, D - 4.4, FT - 4.5, 7.6, 1.6)
        S.P(inner, "#f7f4ee", INK, 0.12)                                         # hollow
        S.R(4.4, -0.05, D - 4.4, 3.0, "#f7f4ee", "none", 0)                       # open bottom of the shell
        # felt turned under, binding ring, back panel
        S.R(3, -0.05, 17, 1.4, FELTC, INK, 0.12); S.R(D - 17, -0.05, D - 3, 1.4, FELTC, INK, 0.12)
        S.R(4, -1.6, 20, 0.0, "#8a8682", INK, 0.12); S.R(D - 20, -1.6, D - 4, 0.0, "#8a8682", INK, 0.12)
        S.R(20.4, -1.2, D - 20.4, 1.8, "#a39e97", INK, 0.12)
        for y in (12, D - 12):
            S.screw_up(y, -3.2, 5.0, STEEL)
        for y in (28, D - 28):
            S.screw_up(y, -2.8, 6.0, "#6f7378")
        S.R(30, -3.2, 40, -1.2, "#2a2a2a", INK, 0.1); S.R(D - 40, -3.2, D - 30, -1.2, "#2a2a2a", INK, 0.1)
        # strip C + pegs
        S.R(8, 7, 56, 8.6, GREEN, INK, 0.12)
        for yc, top in ((19.5, 32.0), (42, 33.3)):
            S.R(yc - 3.5, 8.6, yc + 3.5, 14.5, "#3a3a3a", INK, 0.1)              # switch
            S.R(yc - 1.8, 14.5, yc + 1.8, top - 3, "#c9a06c", INK, 0.1)           # shank
            S.P([(yc - 6.35, top - 3.5), (yc + 6.35, top - 3.5), (yc + 5.5, top - 0.6), (yc, top), (yc - 5.5, top - 0.6)], "#e3c493", INK, 0.12)
            S.R(yc - 9.5, FT - 1, yc - 2.2, FT, "#6f6d6a", INK, 0.08); S.R(yc + 2.2, FT - 1, yc + 9.5, FT, "#6f6d6a", INK, 0.08)
        top_shell = FT - 2
        S.R(58, 12.4, D - 9, 14.0, GREEN, INK, 0.12)                              # main board 268 x 115
        for yk, hero in ((68, True), (100, False), (123, False)):
            pot_sec(S, yk, 14.0, FT + 2.0)
            S.R(yk - (12.4 if hero else 9.6), FT - 1.0, yk + (12.4 if hero else 9.6), FT + 0.06, "#d8d3c9", INK, 0.1)
            knob_sec(S, yk, FT + 0.56, d=20.8 if hero else 14.86, h=12.15 if hero else 10.45)
        S.R(106, 1.5, 170, 11.0, "#5d6a7a", INK, 0.1, dash="0.8 0.6", op=0.35)
        return FT
    else:
        Z = 24.0
        S.P([(0, 0), (D, 0), (D, Z - 2), (D - 2, Z), (49.5, Z), (49.5, Z - 2.5), (D - 2.4, Z - 2.5), (D - 2.4, 0.6), (2.4, 0.6), (2.4, Z - 2), (2.4, Z), (0 + 2, Z), (0, Z - 2)], PCRM, INK, 0.15)
        S.R(2.6, 0, D - 2.6, 3.0, PLY, INK, 0.12)
        for y in (7, D - 7):
            S.screw_up(y, -1.6, 7.5, STEEL)
        S.R(18, -6, 30, 0, "#2a2a2a", INK, 0.1); S.R(D - 30, -6, D - 18, 0, "#2a2a2a", INK, 0.1)
        S.R(3, 12.6, 50, 14.2, GREEN, INK, 0.12)                                  # strip C
        for y0, y1, zt in ((3.3, 32.7, 24), (35, 49, 26)):
            S.R(y0, zt - 3, y1, zt, "#f6f3ec" if zt == 24 else "#3b3734", INK, 0.12)
            S.R((y0 + y1) / 2 - 3.5, 14.2, (y0 + y1) / 2 + 3.5, zt - 3, "#3a3a3a", INK, 0.1)
        S.R(52, 12.9, 167, 14.5, GREEN, INK, 0.12)                               # main board 268 x 115
        for yk, hero in ((68, True), (100, False), (123, False)):
            pot_sec(S, yk, 14.5, 26.5)
            knob_sec(S, yk, Z + 0.5, d=20.8 if hero else 14.86, h=12.15 if hero else 10.45)
        S.R(100, 1.5, 166, 11.0, "#5d6a7a", INK, 0.1, dash="0.8 0.6", op=0.35)
        for y in (60, 96, 140):
            S.R(y - 3, 14.5, y + 3, Z - 2.5, "#d9cdb2", INK, 0.1)                 # boss with insert
        return Z

def sheet_c_flat(c, kind):
    s = head(c["title"], c["kind"], "How it's built: one closed-top body loaded from underneath, then a panel screwed on from behind (owner). Section front-to-back through CUTOFF.", "sheet C — construction", 4)
    D = r4.HU_D if kind == "hush" else r4.OS_D
    sc = 1.45
    S = Sec(22, 128, sc)
    FT = sec_flat(S, D, kind)
    S.s.append(dim_h(S.X(0), S.X(D), S.Z(-9), f"{D:.0f} mm deep"))
    S.s.append(dim_v(S.X(D) + 6, S.Z(FT), S.Z(0), f"{FT} body"))
    if kind == "hush":
        S.note(1, 16, 0, 44, "felt skin ≈ 2 mm, blocked over every edge", INK, 2.0)
        S.note(5, 22.8, 22, 50, "shell 2.5 top / 2.4 wall, printed: a closed top with holes only", INK, 2.0)
        S.note(42, 33, 52, 44, "maple peg on its felt collar (the stop)", INK, 2.0)
        S.note(68, 38, 90, 46, "cream knobs on printed tags, flush in the felt", INK, 2.0)
        S.note(150, 13.5, 150, -17, "main board 268 × 115, screwed UP to 10 bosses: pots pulled tight to the shell, no top nuts", INK, 2.0, "end")
        S.note(12, -3, 12, -24, "binding ring: 10 × M3 from below clamp the felt's turn-in", INK, 2.0)
        S.note(D - 28, -2.5, D - 4, -24, "back panel inside the ring: 8 × M3 from below", INK, 2.0, "end")
        S.note(118, 4, 100, -31, "battery bay (systems 7.2) under the board: back panel off to reach it", INK, 2.0, "end")
    else:
        S.note(1.2, 23, 0, 44, "front wall 2.4, flush with the key tops", INK, 2.0)
        S.note(30, 24.5, 38, 50, "key window: tops pressed on last, from above", INK, 2.0)
        S.note(85, 23.5, 92, 50, "top face 2.5, printed face down (legends 0.6 deep, one swap)", INK, 2.0)
        S.note(96, 18, 112, 42, "printed boss + M3 insert: the board screws UP", INK, 2.0)
        S.note(150, 13.8, 150, -17, "main board 268 × 115 (eng): pots pulled tight to the shell, bushings under the knob skirts", INK, 2.0, "end")
        S.note(7, -1, 7, -24, "8 × M3 from below into the shell's rim", INK, 2.0)
        S.note(60, 1.5, 60, -31, "3 mm ply back panel", INK, 2.0)
        S.note(118, 4, 118, -31, "battery bay (systems 7.2): back panel off", INK, 2.0)
    s.append(S.svg())
    s.append(t(22, 47, f"SECTION · {sc}:1 · front of the instrument on the left · cut at x ≈ CUTOFF", 3.0, INK, weight="bold"))
    # right: underside render + assembly order
    i, b = img(os.path.join(OUT, "r4_hu_under.png" if kind == "hush" else "r4_os_under.png"), 296, 44, 112, 66)
    s.append(i)
    s.append(t(296, 116, "Every screw is on this face.", 2.4, MUTE, style="italic"))
    steps = ([
        "Print the shell (2 halves split at x 129.5: the felt hides the joint) and the binding ring.",
        "Steam-block the felt hood over the empty shell (the shell is the hat block); dry overnight; trim the turn-in.",
        "Punch the holes from inside, using the shell's own holes as the template. Press the names and rules with the brass die.",
        "Fit the collars; screw on the binding ring (10 × M3).",
        "Load from below: stick gate, main board (10 × M3 up), strip C, I/O board, speaker and battery on the back panel.",
        "Back panel on (8 × M3). Flip. Tags, pegs, knobs and stick cap go on from above, last.",
    ] if kind == "hush" else [
        "Print the shell face down on smooth PEI (one piece on a 350 bed, or two at x 122.5); one swap at 0.6 mm.",
        "Press in ≈ 25 heat-set inserts (board 10, strip C 4, I/O 2, back panel 8).",
        "Shell face down on a towel. Gate plate into its pocket.",
        "Main board in: shafts and stick up through their holes; 10 × M3 up. Strip C on 4 bosses. I/O board on the rear wall.",
        "Battery and speaker on the back panel; plug in. Back panel on: 8 × M3 from below. Feet on the panel.",
        "Flip. Key tops pressed on through the window; knobs and the stick cap on.",
    ])
    yy = 124
    s.append(t(296, yy, "BUILD ORDER (F9)", 3.0, ACC, weight="bold"))
    yy += 5.5
    for k, st in enumerate(steps, 1):
        p, yy = para(296, yy, f"{k}. {st}", 52, 2.3)
        s.append(p); yy += 1.0
    yy += 2
    s.append(t(296, yy, "WHAT THE OWNER SEES OF IT", 3.0, ACC, weight="bold"))
    p, yy = para(296, yy + 5.5, ("A felt pebble with no seam, no screw and no edge; underneath, a tidy ring and a panel."
                                 if kind == "hush" else "One cream face with holes only; underneath, one ply panel and eight screws of one size."), 52, 2.3)
    s.append(p)
    # detail at 4:1 (left bottom)
    s.append(t(22, 186, "DETAIL · 2.5:1 · the front edge" if kind == "hush" else "DETAIL · 2:1 · where the keys meet the face", 3.0, INK, weight="bold"))
    D2 = Sec(34, 278, 2.5)
    D2.s.append('<clipPath id="dclip"><rect x="10" y="198" width="130" height="96"/></clipPath><g clip-path="url(#dclip)">')
    if kind == "hush":
        D2.P(rounded_profile(0, 120, 25.5, 12, 6), FELTC, INK, 0.2)
        D2.P(rounded_profile(2, 118, 23.5, 10, 4), SHELL, INK, 0.15)
        D2.P(rounded_profile(4.4, 115.6, 21.0, 7.6, 1.6), "#f7f4ee", INK, 0.12)
        D2.R(4.4, -0.05, 115, 3.0, "#f7f4ee", "none", 0)
        D2.R(3, -0.05, 17, 1.4, FELTC, INK, 0.12)
        D2.R(4, -1.6, 20, 0.0, "#8a8682", INK, 0.12)
        D2.R(20.4, -1.2, 60, 1.8, "#a39e97", INK, 0.12)
        D2.screw_up(12, -3.2, 5.0)
        D2.screw_up(28, -2.8, 6.0, "#6f7378")
        D2.R(19.5 - 1.8, 14.5, 19.5 + 1.8, 29, "#c9a06c", INK, 0.1)
        D2.P([(13.15, 28.5), (25.85, 28.5), (25, 31.4), (19.5, 32), (14, 31.4)], "#e3c493", INK, 0.12)
        D2.R(10, 24.5, 17.3, 25.5, "#6f6d6a", INK, 0.08); D2.R(21.7, 24.5, 29, 25.5, "#6f6d6a", INK, 0.08)
        D2.R(36.5, 25.1, 37.5, 25.5, "#5f5d5a", INK, 0.08)
    else:
        D2 = Sec(12 - 36 * 2, 282, 2.0)
        D2.s.append('<clipPath id="dclip2"><rect x="10" y="190" width="130" height="102"/></clipPath><g clip-path="url(#dclip2)">')
        D2.R(49.5, 21.5, 95, 24, PCRM, INK, 0.15)
        D2.R(35, 23, 49, 26, "#3b3734", INK, 0.12); D2.R(3.3, 21, 32.7, 24, "#f6f3ec", INK, 0.12)
        D2.R(38.5, 14.2, 45.5, 23, "#3a3a3a", INK, 0.1)
        D2.R(3, 12.6, 50, 14.2, GREEN, INK, 0.12)
        D2.R(52, 12.9, 95, 14.5, GREEN, INK, 0.12)
        pot_sec(D2, 68, 14.5, 26.5)
        knob_sec(D2, 68, 24.5, d=20.8, h=12.15)
        D2.R(84, 14.5, 90, 21.5, "#d9cdb2", INK, 0.1); D2.R(86, 16, 88, 21.5, "#c2a25e", INK, 0.08)
        for k in range(30):
            y = 50.2 + k * 1.4
            if not (79.5 <= y <= 82.6) and not (56 <= y <= 80):
                D2.R(y, 23.82, y + 0.9, 24, "#c8b48d", "none", 0)
        D2.R(80, 23.4, 82.4, 24, OS_INK_HEX, INK, 0.08)
        D2.R(84.8, 23.4, 86, 24, "#f7f4ee", INK, 0.1)
    D2.s.append("</g>")
    nx = 145
    notes = ([("felt: round r 12, a short side, round r 6, then under", 18),
              ("felt ends 15 mm in, on a 2 mm recessed land", 8),
              ("the binding ring clamps it; the back panel opens separately", 2),
              ("peg head lands on its punched collar (25.5 → 28)", 30),
              ("pressed rule: a hot brass die, no ink", 25.5)] if kind == "hush" else
             [("sharps end at y 49, the face starts at 49.5: nothing rises between keys and knobs", 0),
              ("first layer, printed face down: lines turned per section (sheen)", 0),
              ("legend: a cut-out 0.6 deep, filled dark by the one swap", 0),
              ("sunk groove 0.6 × 1.2 on each break (here: y 85.4)", 0),
              ("the pot is pulled up against the face; no top nut, the bushing hides under the skirt", 0),
              ("printed boss + brass insert: the board screws UP into it", 0)])
    for k, (txt_, _) in enumerate(notes):
        s.append(t(nx, 216 + k * 7, f"{k + 1}  {txt_}", 2.2, INK))
    marks = ([(1, 14), (10, 0.7), (14, -1.5), (19.5, 26.5), (37, 25.3)] if kind == "hush" else
             [(49.3, 27.5), (53, 24.6), (81.2, 25.2), (85.4, 25.2), (64, 22.5), (87, 18)])
    for k, (yy, zz) in enumerate(marks):
        D2.s.append(circ(D2.X(yy), D2.Z(zz), 1.6, "#f3efe8", ACC, 0.25))
        D2.s.append(t(D2.X(yy), D2.Z(zz) + 0.75, str(k + 1), 2.0, ACC, "middle", weight="bold"))
    s.append(D2.svg())
    s.append(t(408, 293, FOOT_TAG, 2.0, MUTE, "end"))
    return write(s, "mock-C-construction", os.path.join(ROOT, c["folder"]))

OS_INK_HEX = "#5b4a39"

def fold_half_sec(S, closed=False):
    """FOLD section at x 145 (through CUTOFF; inside the battery bay's x range, outside EMPHASIS's x 169)."""
    H = r4.FO_H
    def base():
        S.P(rounded_profile(0, H, r4.BASE_H, 3, 6), WAL, INK, 0.2)
        S.R(4, 2, H - 4, r4.BASE_H + 0.05, "#f7f4ee", "none", 0)
        S.L(4, 2, 4, 15.6, INK, 0.12); S.L(H - 4, 2, H - 4, 15.6, INK, 0.12); S.L(4, 2, H - 4, 2, INK, 0.12)
        S.R(8, 4.5, 82, 6.1, GREEN, INK, 0.12)                              # base board 270 x 78
        S.R(52, 13.1, H - 4.3, 14.6, BLK, INK, 0.1)
        S.R(52, 14.6, H - 4.3, 15.6, PGC, INK, 0.1)
        for y0, y1, zt, col in ((4.8, 34.2, 17.5, "#f6f3ec"), (36.5, 50.5, 19.5, "#3b3734")):
            S.R(y0, zt - 3, y1, zt, col, INK, 0.12)
            S.R((y0 + y1) / 2 - 3.5, 6.1, (y0 + y1) / 2 + 3.5, zt - 3, "#3a3a3a", INK, 0.1)
        pot_sec(S, 68, 6.1, 15.6 + 2.5)
        knob_sec(S, 68, 16.1, d=20.8, h=12.15, col="#b3302a")
        for y in (56, H - 12):
            S.R(y - 2.75, 6.1 if y < 82 else 2, y + 2.75, 13.1, "#c9b27a", INK, 0.1)   # standoff
            S.screw_up(y, 0, 6.5)
    def lid(flip):
        L0 = r4.LY0
        if flip:
            Y = lambda d: H - d; Zf = lambda z: 50 - z
        else:
            Y = lambda d: L0 + d; Zf = lambda z: z
        def RR(d0, z0, d1, z1, fill, **k):
            S.R(Y(d0), Zf(z0), Y(d1), Zf(z1), fill, **k)
        S.P([(Y(p[0]), Zf(p[1])) for p in rounded_profile(0, H, r4.LID_H, 3, 6)], WAL, INK, 0.2)
        RR(-1.5, 12.6, H - 4, r4.LID_H + 0.2, PAPER, stroke="none", sw=0)      # the open hollow (no wall on the hinge edge)
        RR(4, 2, H - 4, 12.6, "#f7f4ee", stroke=INK, sw=0.1)
        RR(0.3, 12.6, H - 4.3, 14.1, BLK, stroke=INK, sw=0.1)
        RR(0.3, 14.1, H - 4.3, 15.1, PGC, stroke=INK, sw=0.1)
        RR(4, 2.0, 54, 11.5, "#5d6a7a", stroke=INK, sw=0.12)                    # battery bay: 2 pouch cells
        RR(57, 4.0, H - 6, 5.6, GREEN, stroke=INK, sw=0.12)                     # lid board (outside the bay)
        for d in (r4.VD_F, r4.VD_B):
            RR(d - 4.75, 5.6, d + 4.75, 12.6, POT, stroke=INK, sw=0.1)
            RR(d - 3.5, 12.6, d + 3.5, 17.6, "#9a9da1", stroke=INK, sw=0.1)
            S.P([(Y(d - 7.25), Zf(15.6)), (Y(d + 7.25), Zf(15.6)), (Y(d + 6.5), Zf(29.1)), (Y(d - 6.5), Zf(29.1))], BLK, INK, 0.15)
        for d in (60, H - 10):
            RR(d - 2.75, 5.6, d + 2.75, 12.6, "#c9b27a", stroke=INK, sw=0.1)
        S.C(r4.AX_Y, 25, 4.8, "none", MUTE, 0.2, dash="1 0.8")
    if closed:
        lid(True); base()
    else:
        base(); lid(False)

def sheet_c_fold(c):
    s = head(c["title"], c["kind"], "How it's built: each half is one hollowed block; one pickguard carries that half's controls (and keys), drops in and is screwed from behind (owner's guitar). Sections through CUTOFF (x 145).", "sheet C — construction", 4)
    S = Sec(22, 112, 1.15)
    fold_half_sec(S, closed=False)
    OPEN = 2 * r4.FO_H + 2
    S.s.append(dim_h(S.X(0), S.X(OPEN), S.Z(-6), f"{OPEN:.0f} mm open (two halves of {r4.FO_H:.0f} + a 2 mm seam)"))
    S.note(2, 10, -4, 30, "base block, walnut-tone (R 6 under, R 3 on top)", INK, 2.0)
    S.note(20, 17.5, 20, 40, "keys from y 4.5: only the 4 mm rim is in front", INK, 2.0)
    S.note(68, 28, 80, 44, "CUTOFF, red 1083", INK, 2.0)
    S.note(56, 1, 40, -14, "6 × M3 up through the block's bottom into standoffs on the pickguard", INK, 2.0)
    S.note(r4.AX_Y, 25, r4.AX_Y + 10, 46, "hinge axis z 25 (knuckles at the rear corners only)", MUTE, 1.9)
    S.note(r4.LY0 + 30, 15.1, r4.LY0 + 30, 44, "lid face 15.1: 2.4 under the keys", INK, 2.0)
    S.note(r4.LY0 + 30, 9, r4.LY0 + 62, 30, "battery bay: 2 pouch cells under the pickguard (lift it to reach them)", INK, 2.0)
    S.note(2 * r4.FO_H + 1, 30, 2 * r4.FO_H + 4, 40, "rims: sides + far edge only", INK, 2.0, "end")
    S.note(r4.LY0 + 8, 1, r4.LY0 + 40, -14, "lid: 6 brass M3 from the back + push-out holes", INK, 2.0)
    s.append(S.svg())
    s.append(t(22, 54, "OPEN · 1.15:1", 3.0, INK, weight="bold"))
    S2 = Sec(22, 200, 1.15)
    fold_half_sec(S2, closed=True)
    S2.s.append(dim_v(S2.X(r4.FO_H) + 4, S2.Z(50), S2.Z(0), "≈ 50.1 closed"))
    S2.note(52, 34, 60, 58, "closed: VOICE knobs land over the keys (front row 2.0 above the sharps)", INK, 2.0)
    S2.note(68, 28.5, 130, 34, "EMPHASIS (lid, x 169, beside this cut) drops into its ring next to CUTOFF", INK, 2.0)
    s.append(S2.svg())
    s.append(t(22, 133, "CLOSED · 1.15:1", 3.0, INK, weight="bold"))
    i, b = img(os.path.join(OUT, "r4_fo_exploded.png"), 180, 134, 228, 96)
    s.append(i)
    p, _ = para(180, 234, "The lid's pickguard lifted out of its block: the plate with every pot, toggle, the lid board, the rectangular speaker and the standoffs, as one unit; under it, the battery bay's two cells on JST leads; one 34-way ribbon to the base. The base comes out the same way, keys and all. With the plates out, everything is reachable.", 110, 2.3, fill=MUTE, style="italic")
    s.append(p)
    yy = 252
    s.append(t(22, yy - 6, "BUILD ORDER (F9), per half", 3.0, ACC, weight="bold"))
    for k, st in enumerate(["Print the block (outer face down) and the pickguard (face down; swap to black at 1.0 mm).",
                            "Inserts; screw the board up to the plate; lay the plate assembly in its block; plug the ribbon and the I/O cable.",
                            "6 screws from behind. Flip: key tops, knobs, stick cap. Pin the corner hinges."], 1):
        p, yy = para(22, yy, f"{k}. {st}", 75, 2.3)
        s.append(p); yy += 0.8
    s.append(t(408, 293, FOOT_TAG, 2.0, MUTE, "end"))
    return write(s, "mock-C-construction", os.path.join(ROOT, c["folder"]))

if __name__ == "__main__":
    for f in (sys.argv[1:] or ["hush", "one-sheet", "fold"]):
        c = CONTENT[f]
        print(sheet_a(c)); print(sheet_b(c))
        print(sheet_c_fold(c) if f == "fold" else sheet_c_flat(c, "hush" if f == "hush" else "os"))
