#!/usr/bin/env python3
"""Jam sketches for Little D (visual designer, jam turn 1). Plans at 1 mm = 1 unit."""
import sys

out = []
def a(s): out.append(s)

W, H = 960, 1060
INK = "#2b2722"; PAPER = "#f4efe6"; MUTE = "#8a8174"; ACC = "#c4512e"; DARK = "#3a3631"

def keys(x0, y0, white="#fbf8f2", black=DARK, stroke=INK, sw=0.6, kw=18.0, depth=72, bdepth=46):
    """15 white keys (C..C two octaves + top C = 25 keys), 270 mm."""
    s = []
    for i in range(15):
        s.append(f'<rect x="{x0+i*kw:.1f}" y="{y0}" width="{kw:.1f}" height="{depth}" fill="{white}" stroke="{stroke}" stroke-width="{sw}"/>')
    pattern = [1,1,0,1,1,1,0]  # sharp after C D (no E) F G A (no B)
    for i in range(14):
        if pattern[i % 7]:
            s.append(f'<rect x="{x0+(i+1)*kw-5.5:.1f}" y="{y0}" width="11" height="{bdepth}" fill="{black}"/>')
    return "\n".join(s)

def knob(x, y, r=6.5, fill=DARK, ring=None):
    s = f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}"/>'
    s += f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x:.1f}" y2="{y-r+1:.1f}" stroke="{PAPER}" stroke-width="1.2"/>'
    return s

def toggle(x, y):
    return f'<rect x="{x-2.5:.1f}" y="{y-5:.1f}" width="5" height="10" rx="2" fill="{MUTE}"/>'

def text(x, y, t, size=9, fill=INK, anchor="start", weight="normal", family="DejaVu Sans", style="normal"):
    t = t.replace("&", "&amp;")
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" font-style="{style}">{t}</text>'

def frame(gx, gy, title, sub):
    a(f'<g transform="translate({gx},{gy})">')
    a(text(0, 0, title, 13, INK, weight="bold"))
    a(text(0, 15, sub, 8.5, MUTE, style="italic"))

a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
a(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
a(text(24, 32, "LITTLE D — jam sketches, visual designer, turn 1", 16, INK, weight="bold"))
a(text(24, 50, "Plans at 1 mm = 1 unit (body 290 × 170). Rough: for judging the idea, not the layout. Knob counts indicative.", 9, MUTE))

# ---------- 1. THE SPREAD ----------
frame(24, 82, "1  THE SPREAD  (Second reduction + tarot)", "signal sentence as five numbered plates; gaps, not lines; one emblem per plate")
a('<g transform="translate(0,28)">')
a(f'<rect x="0" y="0" width="290" height="170" rx="4" fill="{DARK}"/>')
plates = [("I", 4, 40, 1), ("II", 44, 138, 3), ("III", 142, 176, 1), ("IV", 180, 252, 3), ("V", 256, 286, 1)]
names = {"I": "CONTROL", "II": "SOURCES", "III": "MIX", "IV": "SHAPE", "V": "VOICE"}
for num, x1, x2, cols in plates:
    a(f'<rect x="{x1}" y="4" width="{x2-x1}" height="88" fill="#e9e1d1"/>')
    a(text((x1+x2)/2, 15, num, 9, ACC, "middle", "bold", "DejaVu Serif"))
    a(text((x1+x2)/2, 88, names[num], 5, INK, "middle"))
# knobs per plate
for x in (22,):
    for y in (32, 54): a(knob(x, y, 5.5))
for c in range(4):
    for r in range(3): a(knob(56 + c*25, 30 + r*20, 6))
for y in (32, 54, 74): a(knob(159, y, 5.5))
for c in range(3):
    for r in range(3): a(knob(193 + c*23, 30 + r*20, 6))
a(f'<circle cx="271" cy="40" r="11" fill="none" stroke="{INK}" stroke-width="0.6" stroke-dasharray="1.5 1.5"/>')
a(knob(271, 70, 6))
a(keys(20, 96))
a(f'<circle cx="10" cy="125" r="4" fill="{ACC}"/>')
a('</g>')
a(text(300, 40, "Plate = section. Numeral = reading", 8)); a(text(300, 51, "order (start at I, findable blind", 8))
a(text(300, 62, "of position). Owner paints one", 8)); a(text(300, 73, "emblem per plate: the 'major", 8))
a(text(300, 84, "arcana' of the signal path.", 8)); a(text(300, 100, "Expected pole. Flat, cheap,", 8, ACC))
a(text(300, 111, "designed for use.", 8, ACC))
a('</g>')

# ---------- 2. TYPE CASE ----------
frame(490, 82, "2  TYPE CASE  (sharpened)", "cells = sections, sized by content; walls = bag armour; slide-in label cards")
a('<g transform="translate(0,28)">')
a(f'<rect x="0" y="0" width="290" height="170" rx="2" fill="#d9c7a6" stroke="{INK}" stroke-width="0.8"/>')
# cells (x1,x2,y1,y2)
cells = [(5,40,5,92),(44,140,5,62),(44,140,66,92),(144,178,5,92),(182,250,5,50),(182,250,54,92),(254,285,5,92)]
for x1,x2,y1,y2 in cells:
    a(f'<rect x="{x1}" y="{y1}" width="{x2-x1}" height="{y2-y1}" fill="#5b4a3a"/>')
    a(f'<rect x="{x1+3}" y="{y2-7}" width="{min(22,x2-x1-6)}" height="5" fill="#f4efe6"/>')
for y in (24, 50): a(knob(22, y, 5.5, "#e9e1d1"))
for c in range(4):
    for r in range(2): a(knob(58 + c*25, 22 + r*20, 6, "#e9e1d1"))
for c in range(4): a(knob(58+c*25, 77, 5, "#e9e1d1"))
for y in (24, 48, 70): a(knob(161, y, 5.5, "#e9e1d1"))
for c in range(3): a(knob(196 + c*22, 24, 6, "#e9e1d1"))
for c in range(3): a(knob(196 + c*22, 70, 5.5, "#e9e1d1"))
a(knob(270, 30, 7, "#e9e1d1"))
a(keys(20, 96))
a(f'<rect x="3" y="110" width="14" height="40" fill="#5b4a3a"/>')
a(f'<circle cx="10" cy="128" r="4" fill="{ACC}"/>')
a('</g>')
a(text(300, 40, "Knob tops sit below wall", 8)); a(text(300, 51, "tops: no lid, no pouch.", 8))
a(text(300, 62, "Cards letterpress-printed", 8)); a(text(300, 73, "at Vector Space, or hand-", 8))
a(text(300, 84, "lettered; swap any time.", 8)); a(text(300, 100, "Speaker must leave the face", 8, ACC))
a(text(300, 111, "(bottom) or cells won't fit.", 8, ACC))
a('</g>')

# ---------- 3. HYMNAL ----------
frame(24, 330, "3  HYMNAL  (new: a bound book you carry)", "cover = bag protection; opened, it stands as a music desk held by its ribbon, or folds under as a rake")
a('<g transform="translate(0,140)">')
def body_section(x, y, sc=1.0):
    s = []
    # depth 170 horizontal, height 36
    s.append(f'<rect x="{x}" y="{y}" width="{170*sc}" height="{34*sc}" fill="#e9e1d1" stroke="{INK}" stroke-width="0.7"/>')
    s.append(f'<rect x="{x+3*sc}" y="{y-3*sc}" width="{164*sc}" height="3" fill="{INK}"/>')
    # knobs
    for k in range(4): s.append(f'<rect x="{x+(95+k*18)*sc}" y="{y-14*sc}" width="{11*sc}" height="{11*sc}" fill="{DARK}"/>')
    # keys
    s.append(f'<rect x="{x+4*sc}" y="{y-4*sc}" width="{70*sc}" height="4" fill="#fbf8f2" stroke="{INK}" stroke-width="0.5"/>')
    return "\n".join(s)
# closed: cover on top of rim
sc = 0.95
a(text(0, 0, "closed", 8, MUTE))
a(body_section(0, 30, sc))
a(f'<rect x="-2" y="{30-20*sc}" width="{174*sc}" height="4" fill="{ACC}"/>')
a(f'<path d="M {172*sc} {30-20*sc} q 8 0 8 10 v {34*sc} q 0 8 -8 8" fill="none" stroke="{ACC}" stroke-width="4"/>')
a(text(0, 82, "≈ 40 mm thick closed (rim taller than knobs)", 7, MUTE))
# open: desk
ox = 210
a(text(ox, 0, "open: music desk", 8, MUTE))
a(body_section(ox, 30, sc))
a(f'<line x1="{ox+168*sc}" y1="{30-3}" x2="{ox+168*sc+18}" y2="{30-120}" stroke="{ACC}" stroke-width="4"/>')
a(f'<line x1="{ox+60}" y1="{30-6}" x2="{ox+168*sc+10}" y2="{30-70}" stroke="{ACC}" stroke-width="0.8" stroke-dasharray="2 1.5"/>')
a(text(ox+70, 30-48, "ribbon = stay", 7, ACC))
a(text(ox+184, 30-104, "endpaper: patch chart", 7, INK)); a(text(ox+184, 30-94, "+ lyric / chord sheet", 7, INK))
# open: rake
rx = 470
a(text(rx, 0, "open: folded under (rake)", 8, MUTE))
a(f'<g transform="rotate(-5 {rx} 50)">')
a(body_section(rx, 30, sc))
a('</g>')
a(f'<path d="M {rx+162*sc} 57 q 14 0 14 -10 v -4" fill="none" stroke="{ACC}" stroke-width="4"/>')
a(f'<line x1="{rx}" y1="64" x2="{rx+168}" y2="50" stroke="{ACC}" stroke-width="4"/>')
a(f'<line x1="{rx-10}" y1="66" x2="{rx+190}" y2="66" stroke="{MUTE}" stroke-width="0.6"/>')
a(text(rx, 82, "spine roll under the back ≈ 14 mm → ≈ 5°", 7, MUTE))
a('</g>')
a(text(0, 240, "Bookcloth over 3 mm ply boards; title blind-stamped on the spine (letterpress); no recall, so the patch is written in pencil on the endpaper — the Model D patch-book habit made part of the object.", 8))
a('</g>')

# ---------- 4. HUSH ----------
frame(24, 610, "4  HUSH  (new: built from the material of silence)", "the felt that stops the keys is the skin of the whole; the skin wrapping the lip IS the key's top stop")
a('<g transform="translate(20,40)">')
FELT="#9a948a"
a(f'<rect x="0" y="100" width="330" height="3" fill="{DARK}"/>')
a(f'<line x1="-4" y1="107" x2="330" y2="107" stroke="{FELT}" stroke-width="6"/>')
a(f'<line x1="-4" y1="107" x2="-4" y2="60" stroke="{FELT}" stroke-width="6"/>')
# key lever: front at x=8, tail + rod at x=170
a(f'<rect x="8" y="58" width="172" height="5" fill="#fbf8f2" stroke="{INK}" stroke-width="0.6"/>')
a(f'<rect x="8" y="58" width="5" height="24" fill="#fbf8f2" stroke="{INK}" stroke-width="0.6"/>')
a(f'<circle cx="176" cy="66" r="3.5" fill="{INK}"/>')
a(f'<ellipse cx="80" cy="96" rx="6" ry="3.5" fill="{ACC}"/>')
a(f'<line x1="80" y1="63" x2="80" y2="92" stroke="{MUTE}" stroke-width="0.6"/>')
# panel + felt wrap
a(f'<rect x="120" y="42" width="210" height="4" fill="{DARK}"/>')
a(f'<path d="M 330 38 H 120 q -7 0 -7 6 q 0 6 7 6 H 172" fill="none" stroke="{FELT}" stroke-width="5"/>')
for k in range(4): a(f'<rect x="{200+k*30}" y="22" width="13" height="16" fill="{DARK}"/>')
a(text(8, 54, "key (RAIL lever)", 7, MUTE)); a(text(182, 70, "rod", 7, MUTE))
a(text(64, 120, "silicone tube", 7, MUTE)); a(text(200, 120, "rigid tray, felt skin under", 7, MUTE))
a(f'<line x1="150" y1="54" x2="150" y2="10" stroke="{ACC}" stroke-width="0.6"/>')
a(text(60, 6, "felt skin on the panel wraps the lip: the key tail rises into it = top stop", 7, ACC))
a('</g>')
a(text(380, 60, "Body: rigid tray wrapped in 3–5 mm wool felt.", 8))
a(text(380, 72, "Labels: embroidered (Vector Space embroidery", 8))
a(text(380, 84, "machine) or laser-browned into the felt.", 8))
a(text(380, 96, "Bag: a felt flap rolls over panel + keys, closes", 8))
a(text(380, 108, "with a wooden toggle and loop (chisel-roll logic).", 8))
a(text(380, 120, "Lap: grips, warm, silent on a table.", 8))
a(text(380, 136, "Risks: grime/pilling at knobs; felt deadens", 8, ACC))
a(text(380, 148, "the speaker — grille must be an open window.", 8, ACC))
a('</g>')

# ---------- 5. UNDER GLASS ----------
frame(24, 800, "5  UNDER GLASS  (Proof + pinball, merged)", "board = playfield under a clear top, reverse-painted underneath")
a('<g transform="translate(0,30)">')
a(f'<rect x="0" y="0" width="290" height="170" fill="#b98a5a"/>')  # board (bare FR4/copper tone)
for i in range(40):
    y = 6 + (i*2.3) % 86
    a(f'<line x1="{8+(i*37)%200}" y1="{y:.1f}" x2="{60+(i*53)%220}" y2="{y:.1f}" stroke="#d9a86a" stroke-width="0.8"/>')
# paint mask with windows
a(f'<path fill="#1f2a33" fill-rule="evenodd" d="M0 0 H290 V96 H0 Z M48 8 h90 v26 h-90 Z M182 8 h64 v26 h-64 Z"/>')
a(text(93, 24, "VCO window", 6, PAPER, "middle")); a(text(214, 24, "ladder window", 6, PAPER, "middle"))
for c in range(9):
    for r in range(2): a(knob(30 + c*28, 52 + r*22, 6, "#e9e1d1"))
a(keys(20, 96, white="#fbf8f2"))
a(f'<rect x="-4" y="-3" width="298" height="4" fill="#9aa3a8"/>'); a(f'<rect x="-4" y="169" width="298" height="4" fill="#9aa3a8"/>')
a(f'<circle cx="10" cy="125" r="4" fill="{ACC}"/>')
a('</g>')
a(text(300, 40, "Bought aluminium U-channel rails", 8)); a(text(300, 51, "front + back (lockdown bar), not", 8))
a(text(300, 62, "end blocks: no cheeks.", 8)); a(text(300, 73, "Reverse painting: labels can't wear,", 8))
a(text(300, 84, "gloss face, backglass craft. Key", 8)); a(text(300, 95, "levers seen through side windows.", 8))
a(text(300, 111, "Weak in a bag: needs a sleeve.", 8, ACC))
a('</g>')

# ---------- 6. RADIO (sharpened) ----------
frame(490, 800, "6  RADIO  (sharpened)", "speaker face carries the identity; one big dial on the panel")
a('<g transform="translate(0,30)">')
# upright view: bottom face as radio front, 290 x 32 -> show 290 x 170 bottom face? show standing silhouette
a(f'<rect x="0" y="0" width="290" height="170" rx="16" fill="#e9e1d1" stroke="{INK}" stroke-width="0.8"/>')
for r in range(11):
    for c in range(30):
        cx = 30 + c*7.5; cy = 22 + r*11
        if ((cx-150)/112)**2 + ((cy-78)/58)**2 < 1:
            a(f'<circle cx="{cx}" cy="{cy}" r="2.2" fill="{DARK}"/>')
a(f'<circle cx="150" cy="78" r="38" fill="none" stroke="{ACC}" stroke-width="0.8" stroke-dasharray="2 2"/>')
a(text(150, 150, "3-inch speaker behind (dashed)", 7, MUTE, "middle"))
a(text(145, 160, "standing: the bottom is the face (speaker + grille)", 7, MUTE, "middle"))
a(f'<path d="M 40 4 q 105 -18 210 0" fill="none" stroke="{ACC}" stroke-width="3"/>')
a('</g>')
a(text(300, 40, "Keep: the speaker-face and", 8)); a(text(300, 51, "handle-stand are real logic.", 8))
a(text(300, 62, "Reframe layout: a radio has", 8)); a(text(300, 73, "ONE big dial — so CUTOFF is", 8))
a(text(300, 84, "large; the rest stay in signal", 8)); a(text(300, 95, "order. Hand-split dropped.", 8))
a(text(300, 111, "Risk: OB-4 / Braun pastiche.", 8, ACC))
a('</g>')

a('</svg>')
open(sys.argv[1], "w").write("\n".join(out))
