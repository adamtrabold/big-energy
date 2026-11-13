#!/usr/bin/env python3
"""Scenes for the round-2 concepts (OpenSCAD text). Flush deck (R4): keys and panel at z ~ 24 unless stated."""
import math
from ld import *

PLY = "#d8ad74"; PLY_EDGE = "#c99b62"; INK = "#26221f"; CREAM = "#ece2c6"; CARD = "#fbf9f3"
RED = "#b8432a"; FELT = "#8d8b88"; FELT_DK = "#7b7976"; WALNUT = "#71492c"; BRASS = "#c9a24a"
STEEL = "#8e9296"; ACRYL_W = "#f6f3ec"; PAPER_C = "#efe4c9"
K_RED = "#b8432a"; K_WHITE = "#f3f2ee"; K_YEL = "#e6c62a"; K_BLUE = "#2f5fa8"; K_CREAM = "#ece2c6"
SHELL_G = "#7f858c"; SHELL_LT = "#d6d4ce"; PRINT_CREAM = "#e8dcc2"; DARK = "#2e2f31"; WHITE_P = "#f4f3ef"
GLASS_BLK = "#121314"; ALU = "#b4b8bc"; SMOKE = "#3a3836"; MASK = "#16181a"
SPLIT_X = 121.0     # every printed part splits here: the II|III gap (oscillators | everything that mixes and shapes them)

JACKS = ["PHONES", "EXT IN", "FILTER CV", "PITCH CV", "GATE", "MIDI IN", "USB-C"]

def jacks_rear(zc=13.0, x0=152, pitch=19, yw=D):
    s = ""
    for k, lab in enumerate(JACKS):
        x = x0 + k * pitch
        if lab == "USB-C":
            s += box(x - 4.5, yw - 0.3, zc - 1.7, x + 4.5, yw + 0.05, zc + 1.7, "#1a1a1a")
        else:
            s += f'{c("#9a9da1")} translate([{x},{yw-0.2},{zc}]) rotate([-90,0,0]) cylinder(h=0.6,d=7.5,$fn=6);\n'
            s += f'{c("#151515")} translate([{x},{yw},{zc}]) rotate([-90,0,0]) cylinder(h=0.7,d=3.6,$fn=24);\n'
    x = x0 - 22
    s += box(x - 6, yw - 0.3, zc - 2.5, x + 6, yw + 0.05, zc + 2.5, "#2a2826")
    s += box(x - 4, yw - 0.4, zc - 1.2, x - 0.5, yw - 0.2, zc + 1.2, "#bfbfbf")
    return s

def jacks_rear_labels(z_text, col, yw=D, x0=152):
    s = ""
    for k, lab in enumerate(JACKS + ["POWER"]):
        x = x0 + k * 19 if lab != "POWER" else x0 - 22
        s += f'{c(col)} translate([{x},{yw+0.06},{z_text}]) rotate([90,0,180]) linear_extrude(0.1) text("{lab}", size=1.8, font="Inter:style=SemiBold", halign="center", valign="center");\n'
    return s

def jacks_right(zc=13.0, y0=92, pitch=12.5, xw=W):
    s = ""
    for k, lab in enumerate(JACKS):
        y = y0 + k * pitch
        if lab == "USB-C":
            s += box(xw - 0.3, y - 4.5, zc - 1.7, xw + 0.05, y + 4.5, zc + 1.7, "#1a1a1a")
        else:
            s += f'{c("#9a9da1")} translate([{xw-0.2},{y},{zc}]) rotate([0,90,0]) cylinder(h=0.6,d=7.5,$fn=6);\n'
            s += f'{c("#151515")} translate([{xw},{y},{zc}]) rotate([0,90,0]) cylinder(h=0.7,d=3.6,$fn=24);\n'
    return s

def footprint(x0=0, y0=0, x1=W, y1=D):
    return box(x0, y0, 0, x1, y1, 0.2, "#000000")

def stick_column(top_z, plate_col, eng_col, mod_knob_col=CREAM, plate=True, y0=0.0, ptr="#2a2622"):
    s = box(3, y0 + 3, top_z - 3, 25, y0 + 52, top_z, plate_col) if plate else ''
    sy = STICK[1] + y0; my = MOD_DIAL[2] + y0
    s += box(STICK[0] - 1.6, sy - 8, top_z, STICK[0] + 1.6, sy + 8, top_z + 0.05, "#1d1b19")
    s += stick(STICK[0], sy, top_z)
    s += knob_std(MOD_DIAL[1], my, top_z + KNOB_GAP, ANG["MOD"], col=mod_knob_col, line=ptr)
    s += txt(STICK[0], y0 + 7.0, top_z, "BEND", 1.7, eng_col)
    s += txt(MOD_DIAL[1], y0 + 37.0, top_z, "MOD", 1.7, eng_col)
    return s

def rbox(x0, y0, z0, x1, y1, z1, r, col, fn=32):
    """box with vertical edges rounded r."""
    return (f'{c(col)} hull(){{ for(p=[[{x0+r},{y0+r}],[{x1-r},{y0+r}],[{x0+r},{y1-r}],[{x1-r},{y1-r}]]) '
            f'translate([p[0],p[1],{z0}]) cylinder(h={z1-z0},r={r},$fn={fn}); }}\n')

def seam_x(x, y0, y1, z, col="#00000055", w=0.35):
    return box(x - w / 2, y0, z, x + w / 2, y1, z + 0.08, col)

def sleeve(scene, hz, y0=74, col=FELT, label="any 13-in laptop sleeve"):
    s = scene
    y1, t = D + 28, 2.5
    s += box(-6, y0, -3, W + 6, y1, -3 + t, col)
    s += box(-6, y0, hz - t, W + 6, y1, hz, col)
    s += box(-6, y0, -3, -6 + t, y1, hz, col)
    s += box(W + 6 - t, y0, -3, W + 6, y1, hz, col)
    s += box(-6, y1 - t, -3, W + 6, y1, hz, col)
    s += f'{c(col)} translate([-6,{y0},{hz/2-1.5}]) rotate([0,90,0]) cylinder(h={W+12}, r={1.5}, $fn=12);\n'
    s += box(-6, y0 + 4, hz, W + 6, y0 + 4.6, hz + 0.1, "#cfcac2")
    s += txt(W - 30, y0 + 40, hz, label, 4.0, "#cfcac2", font="Inter:style=SemiBold")
    return s

# =========================================================== TYPE CASE
TC_RIM = 36.7          # sides + rear only, level with the tallest sort (CUTOFF 24.5 + 12.15)
TC_CARDS = [("I", "CONTROLLERS"), ("II", "OSCILLATORS"), ("III", "MIXER"), ("IV", "MODIFIERS"), ("V", "OUTPUT")]

def chamfer_wall(x0, y0, x1, y1, z1, col, ch=1.5, axis="y"):
    """wall up to z1 with its top edges chamfered ch."""
    if axis == "y":   # wall runs along y (side cheek)
        return (f'{c(col)} hull(){{ translate([{x0},{y0},3]) cube([{x1-x0},{y1-y0},{z1-3-ch}]); '
                f'translate([{x0+ch},{y0},3]) cube([{x1-x0-2*ch},{y1-y0},{z1-3}]); }}\n')
    return (f'{c(col)} hull(){{ translate([{x0},{y0},3]) cube([{x1-x0},{y1-y0},{z1-3-ch}]); '
            f'translate([{x0},{y0+ch},3]) cube([{x1-x0},{y1-y0-2*ch},{z1-3}]); }}\n')

def type_case():
    s = ""
    s += box(0, 0, 0, W, D, 3, PLY_EDGE)
    # cheeks (sides) and rear rail: the case, at the rim; open front (R4: nothing between hands and controls)
    s += chamfer_wall(0, 0, 4, D, TC_RIM, PLY, axis="y")
    s += chamfer_wall(W - 4, 0, W, D, TC_RIM, PLY, axis="y")
    s += chamfer_wall(4, D - 4, W - 4, D, TC_RIM, PLY, axis="x")
    s += box(4, 0, 3, W - 4, 3, PZ - 3, PLY)                        # front wall under the key fronts
    # flat front rail (key edge, H3'): natural ply at panel height, card pockets in it
    s += box(4, 52, PZ - 3, W - 4, 78, PZ, PLY)
    for (num, name), (_, _, x0, x1) in zip(TC_CARDS, SECTIONS):
        a, b = max(x0 + 1, 6), min(x1 - 1, W - 6)
        s += box(a - 1.2, 61.8, PZ, b + 1.2, 74.2, PZ + 0.02, "#b98a55")   # pocket shadow edge
        s += box(a, 63, PZ - 0.6, b, 73, PZ + 0.05, CARD)
        cx = (a + b) / 2
        if b - a > 40:
            s += txt(a + 2.5, 68, PZ + 0.05, num, 7.0, "#1b1918", font="DejaVu Serif:style=Bold", halign="left", h=0.14)
            s += txt(a + 4.0 + 5.2 * len(num), 67.6, PZ + 0.05, name, 3.4, "#1b1918", font="Inter:style=Bold", halign="left", h=0.14)
        else:
            s += txt(a + 2.0, 68, PZ + 0.05, num, 6.0, "#1b1918", font="DejaVu Serif:style=Bold", halign="left", h=0.14)
            s += txt(b - 1.5, 67.6, PZ + 0.05, name if b - a > 30 else name[:3], 2.6 if len(name) < 9 or b - a < 30 else 2.1, "#1b1918", font="Inter:style=Bold", halign="right", h=0.14)
    # ink-dyed compartment floors, separated by FLUSH rules: the egg-crate walls run under the floor, their tops show pale
    edges = [4] + [e for xc in GAP_CENTRES[1:5] for e in (xc - 1.5, xc + 1.5)] + [W - 4]
    for i in range(0, len(edges), 2):
        s += box(edges[i], 78, PZ - 3, edges[i + 1], D - 4, PZ, INK)
    # sunk rules (owner: feel the sections without anything in the knobs' way): wall tops 1 mm below the floor face
    for xc in GAP_CENTRES[1:5]:
        s += box(xc - 1.5, 78, PZ - 3, xc + 1.5, D - 4, PZ - 1.0, PLY)
    s += box(4, 78, PZ - 3, W - 4, 79.2, PZ + 0.04, PLY)            # front rule where the floors meet the rail
    # stick compartment floor + key bed
    s += stick_column(PZ, INK, "#efe3cc", mod_knob_col=K_RED, ptr="#f3eadb")
    s += box(25, 3, PZ - 3, 26.5, 52, PZ + 0.04, PLY)               # flush rule between stick cell and keys
    s += keys(style="short", plate=INK, wz=PZ)
    s += panel_controls(PZ, knob_col=K_RED, eng="#e9d9bb", hero_col=CREAM, ptr="#f3eadb")
    s += jacks_rear(zc=14) + jacks_rear_labels(7.0, "#4a3320")
    return s

def type_case_fp():
    return footprint()

# =========================================================== HYMNAL (cigar box, walnut, lean)
HY_RIM = 35.0; HY_PZ = PZ; HY_LID_T = 3.0

def hymnal(open_state=True, lid_angle=104, keystyle="short", show_lid=True):
    s = ""
    s += box(0, 0, 0, W, D, 3, WALNUT)
    s += box(0, 0, 3, 3, D, HY_RIM, WALNUT)
    s += box(W - 3, 0, 3, W, D, HY_RIM, WALNUT)
    s += box(3, D - 3, 3, W - 3, D, HY_RIM, WALNUT)
    for (x0, y0, x1, y1) in [(0, 0, 3, D), (W - 3, 0, W, D), (0, D - 3, W, D)]:
        s += box(x0, y0, HY_RIM - 0.01, x1, y1, HY_RIM + 0.15, PAPER_C)
    if open_state:
        s += box(3, -35, 0, W - 3, 0, 3, WALNUT)
        s += box(3, -35, 3, W - 3, -32.5, 3.15, PAPER_C)
        s += box(3, -2.0, 0, W - 3, 0.5, 3.25, "#3b3a37")             # cloth-tape hinge (bookcloth)
    else:
        s += box(3, 0, 3, W - 3, 3, HY_RIM, WALNUT)
    s += box(3, 78, HY_PZ - 3, W - 3, D - 3, HY_PZ, PLY)
    # key edge: flat, paper-edged band at panel height with the key names
    s += box(3, 52, HY_PZ - 3, W - 3, 78, HY_PZ, PAPER_C)
    s += box(3, 52, HY_PZ, W - 3, 53.0, HY_PZ + 0.1, RED)
    s += box(3, 77, HY_PZ, W - 3, 78, HY_PZ + 0.1, RED)
    for x0, i in white_keys():
        nm = "CDEFGAB"[i % 7] if i < 14 else "C"
        s += txt(x0 + 9, 60, HY_PZ, nm, 2.6, "#7a2a1a", font="Inter:style=Bold")
    for num, name, x0, x1 in SECTIONS:
        s += txt(x0 + 1, 83.4, HY_PZ, num, 2.8, RED, font="DejaVu Serif:style=Bold", halign="left")
        if x1 - x0 > 30:
            s += txt(x0 + 2 + 2.6 * len(num), 83.4, HY_PZ, name, 2.0, "#2a2420", font="Inter:style=Bold", halign="left")
    s += stick_column(HY_PZ, PLY, "#3a2a1c", mod_knob_col=K_WHITE)
    s += keys(white="#f4efe4", sharp="#2b2523", style=keystyle, plate="#2b2523", wz=HY_PZ)
    s += panel_controls(HY_PZ, knob_col=K_WHITE, eng="#3a2a1c", hero_col=CREAM)
    lid = ""
    lid += box(0, 0, 0, W, D, HY_LID_T, WALNUT)
    lid += box(14, 12, -0.15, W - 14, D - 12, 0, "#00ff00")          # inside: patch chart paper (chroma key)
    def ly(y):
        return D - ((y - 78) * 1.0 + 22)
    def lidtxt(x, y, s_, size, col, font="Inter:style=SemiBold", halign="center"):
        s_ = s_.replace('"', '\\"')
        return (f'{c(col)} translate([{x:.2f},{y:.2f},-0.32]) mirror([0,1,0]) linear_extrude(0.1) '
                f'text("{s_}", size={size}, font="{font}", halign="{halign}", valign="center", $fn=20);\n')
    for (num, name, x0, x1) in SECTIONS:
        lid += box(x0, ly(90), -0.3, x1, ly(90) + 0.5, -0.25, RED)
        lid += lidtxt(x0, ly(86), num + ("  " + name if x1 - x0 > 30 else ""), 2.6, RED, font="Inter:style=Bold", halign="left")
    for lab, x, y, kind, midi in KNOBS:
        r = 5.5 if kind != "hero" else 8.0
        lid += (f'{c(RED)} translate([{x:.2f},{ly(y):.2f},-0.32]) difference(){{ cylinder(h=0.07,r={r},$fn=32);'
                f' translate([0,0,-0.1]) cylinder(h=0.3,r={r-0.45},$fn=32);}}\n')
        lid += f'{c(RED)} translate([{x:.2f},{ly(y)-r-0.4:.2f},-0.32]) cube([0.4,1.2,0.07],center=true);\n'
    lid += lidtxt(20, ly(185), "PATCH  ________________________     DATE  __________", 4.0, "#3a2a1c", font="Inter:style=Regular", halign="left")
    lid += lidtxt(W - 20, ly(185), "No. 1", 4.0, RED, font="Inter:style=Bold", halign="right")
    # outside: a blank label for the owner's own lettering (no borrowed script)
    lid += box(24, 34, HY_LID_T, W - 24, D - 34, HY_LID_T + 0.15, PAPER_C)
    lid += box(28, 38, HY_LID_T + 0.15, W - 28, D - 38, HY_LID_T + 0.2, RED)
    lid += box(30, 40, HY_LID_T + 0.2, W - 30, D - 40, HY_LID_T + 0.25, PAPER_C)
    for yy in (D / 2 + 2, D / 2 + 22):
        lid += box(60, yy, HY_LID_T + 0.25, W - 60, yy + 0.35, HY_LID_T + 0.3, "#c9bfa9")
    lid += txt(W / 2, D / 2 + 12, HY_LID_T + 0.25, "your title here", 6.0, "#a99f8a", font="Inter:style=Medium")
    lid += txt(W / 2, D / 2 - 14, HY_LID_T + 0.25, "THREE OSCILLATORS  ·  LADDER FILTER  ·  HAND BUILT", 3.8, "#2a2420", font="Inter:style=Bold")
    lid += txt(W / 2, D / 2 - 24, HY_LID_T + 0.25, "No. 1", 3.6, "#2a2420", font="Inter:style=Medium")
    lid += box(0, 0, HY_LID_T, W, 3, HY_LID_T + 0.15, PAPER_C)
    if open_state and not show_lid:
        pass
    elif open_state:
        s += f'translate([0,{D},{HY_RIM}]) rotate([{-lid_angle},0,0]) translate([0,{-D},0]) {{\n{lid}}}\n'
        s += (f'{c(RED)} hull(){{ translate([{W-8},{D-62},{HY_RIM-1}]) cube([6,0.4,1]); '
              f'translate([{W-8},{D+12},{HY_RIM+57}]) cube([6,0.4,1]); }}\n')
        s += box(0, D - 1.5, HY_RIM - 0.2, W, D + 0.6, HY_RIM + 0.2, "#3b3a37")   # cloth-tape lid hinge
    else:
        s += f'translate([0,0,{HY_RIM}]) {{\n{lid}}}\n'
        s += box(0, D - 0.4, HY_RIM - 4, W, D + 0.4, HY_RIM + HY_LID_T, "#3b3a37")
    s += jacks_right(zc=14)
    return s

def hymnal_fp(open_state=True):
    return footprint(0, -35 if open_state else 0, W, D)

# =========================================================== HUSH (printed shell + wool felt top)
HU_SHELL = 22.7       # printed shell top (= eng's panel floor)
HU_FT = 25.5          # felt top, deck and panel flush
PEG_D = 12.7
WHITE_PEG_Y, SHARP_PEG_Y = 16.0, 42.0

def tag(x, y, z, r, label, col, eng, tab=True, tw=13.0):
    """printed keyhole tag: a ring under a knob + a tab with its name (legends by filament swap)."""
    s = cyl(x, y, z - 1.2, 1.25, 2 * r, col, fn=48)
    if tab:
        s += box(x - tw / 2, y - r - 3.6, z - 1.2, x + tw / 2, y - r + 1.5, z + 0.05, col)
        s += txt(x, y - r - 1.6, z + 0.05, label, 1.7, eng, font="Inter:style=Bold")
    return s

def hush(closed=False):
    s = ""
    s += rbox(-3, -3, 0, W + 3, D + 3, HU_SHELL, 6, SHELL_G)
    s += box(SPLIT_X - 0.25, -3.25, 1, SPLIT_X + 0.25, -2.9, HU_SHELL - 1, "#5b6066")
    s += box(SPLIT_X - 0.25, D + 2.9, 1, SPLIT_X + 0.25, D + 3.25, HU_SHELL - 1, "#5b6066")
    # felt skin: one piece over the whole top, soft rolled edge
    s += (f'{c(FELT)} hull(){{ for(p=[[-1,-1],[{W+1},-1],[-1,{D+1}],[{W+1},{D+1}]]) translate([p[0],p[1],{HU_SHELL}]) '
          f'cylinder(h={HU_FT-HU_SHELL-1.2},r=4,$fn=32); for(p=[[0.2,0.2],[{W-0.2},0.2],[0.2,{D-0.2}],[{W-0.2},{D-0.2}]]) '
          f'translate([p[0],p[1],{HU_FT-1.2}]) scale([1,1,0.4]) sphere(r=3,$fn=24); }}\n')
    # replaceable palm strip (darker felt) along the front
    s += f'{c(FELT_DK)} hull(){{ translate([2,-3.6,{HU_SHELL-3}]) cube([{W-4},1,{HU_FT-HU_SHELL+2}]); translate([2,-2.6,{HU_FT-0.4}]) rotate([0,90,0]) cylinder(h={W-4},r=0.9,$fn=16); translate([2,5.5,{HU_FT-0.2}]) rotate([0,90,0]) cylinder(h={W-4},r=0.5,$fn=12);}}\n'
    # pegs with separate punched felt collars (wear parts)
    for x0, i in white_keys():
        xc = x0 + 9
        s += cyl(xc, WHITE_PEG_Y, HU_FT - 0.2, 0.8, 19.0, "#74726f", fn=48)
        s += cyl(xc, WHITE_PEG_Y, HU_FT, 2.0, 8.0, "#d9b98a", fn=32)
        s += cyl(xc, WHITE_PEG_Y, HU_FT + 2.0, 2.2, PEG_D, "#e2c290", fn=48)
        s += f'{c("#e2c290")} translate([{xc},{WHITE_PEG_Y},{HU_FT+4.2}]) scale([1,1,0.3]) sphere(d={PEG_D},$fn=48);\n'
    for xc in sharp_keys():
        s += cyl(xc, SHARP_PEG_Y, HU_FT - 0.2, 0.8, 19.0, "#74726f", fn=48)
        s += cyl(xc, SHARP_PEG_Y, HU_FT, 3.2, 8.0, "#c49a68", fn=32)
        s += cyl(xc, SHARP_PEG_Y, HU_FT + 3.2, 2.2, PEG_D, "#cfa572", fn=48)
        s += f'{c("#cfa572")} translate([{xc},{SHARP_PEG_Y},{HU_FT+5.4}]) scale([1,1,0.3]) sphere(d={PEG_D},$fn=48);\n'
    for x0, i in white_keys():
        if i % 7 == 0:
            s += txt(x0 + 9, 60, HU_FT + 0.05, "C" + str(i // 7 + 1), 2.8, "#e8e1d2", font="Inter:style=Bold", h=0.35)
    # stick: printed plate (same hard material as the tags)
    s += rbox(4, 4, HU_FT - 1.2, 24, 52, HU_FT + 0.05, 3, SHELL_LT)
    s += box(STICK[0] - 1.6, STICK[1] - 8, HU_FT + 0.05, STICK[0] + 1.6, STICK[1] + 8, HU_FT + 0.1, "#2a2826")
    s += stick(STICK[0], STICK[1], HU_FT)
    s += knob_std(MOD_DIAL[1], MOD_DIAL[2], HU_SHELL + 3.3, ANG["MOD"], col=K_CREAM)
    s += txt(STICK[0], 7.5, HU_FT + 0.05, "BEND", 1.7, "#3a3631")
    s += txt(14, 37.5, HU_FT + 0.05, "MOD", 1.7, "#3a3631")
    # a printed tag per knob: ring + name tab, legends dark by the colour swap
    eng = "#3a3631"
    for lab, x, y, kind, midi in KNOBS:
        short = lab.replace("F. ", "").replace("L. ", "")
        short = {"CONTOUR AMT": "AMOUNT"}.get(short, short.split(" ")[0] if short.startswith(("RANGE", "WAVE", "FREQ")) else short)
        r = 13.0 if kind == "hero" else 9.0
        s += tag(x, y, HU_FT, r, short, SHELL_LT, eng)
        if kind == "hero":
            s += ticks(x, y, HU_FT + 0.05, HERO_D / 2 + 0.6, 11, eng, length=1.6)
        elif lab.startswith("RANGE") or kind == "rot":
            s += ticks(x, y, HU_FT + 0.05, KNOB_D / 2 + 0.2, [-125, -75, -25, 25, 75, 125], eng, length=1.2, width=0.5)
        else:
            s += ticks(x, y, HU_FT + 0.05, KNOB_D / 2 + 0.2, 7, eng, length=0.9, width=0.35)
    for lab, x, y, n in TOGGLES:
        s += f'{c(SHELL_LT)} hull(){{ for(p=[[{x-3},{y-7}],[{x+3},{y-7}],[{x-3},{y+5}],[{x+3},{y+5}]]) translate([p[0],p[1],{HU_FT-1.2}]) cylinder(h=1.25,r=2,$fn=16); }}\n'
        s += txt(x, y - 9.6, HU_FT + 0.05, lab, 1.45, eng, font="Inter:style=Bold")
        s += toggle(x, y, HU_FT)
    for lab, x, y, kind, midi in KNOBS:
        z = HU_SHELL + KNOB_GAP + 1.25
        if kind == "hero":
            s += knob_hero(x, y, z, ANG[lab], col=CREAM)
        else:
            s += knob_std(x, y, z, ANG[lab], col=K_CREAM)
    s += tag(STATUS_LED[0], STATUS_LED[1], HU_FT, 4, "STATUS", SHELL_LT, eng, tw=11)
    s += led(STATUS_LED[0], STATUS_LED[1], HU_FT + 0.05)
    s += led(NIC_LED[0], NIC_LED[1], HU_FT + 0.05, col="#e9dfc8")
    for num, name, x0, x1 in SECTIONS:
        s += txt(x0 + 1, 82.0, HU_FT + 0.05, num, 3.4, "#b8432a", font="DejaVu Serif:style=Bold", halign="left", h=0.4)
        if x1 - x0 > 30:
            s += txt(x0 + 2.5 + 3.0 * len(num), 82.0, HU_FT + 0.05, name, 2.3, "#efe8da", font="Inter:style=Bold", halign="left", h=0.4)
    s += jacks_rear(zc=12, yw=D + 3)
    return s

def hush_fp():
    return footprint(-3, -3, W + 3, D + 3)

def hush_closed():
    """optional roll flap (+$32-35 per systems): a soft parcel."""
    s = rbox(-3, -3, 0, W + 3, D + 3, HU_SHELL, 6, SHELL_G)
    s += (f'{c(FELT)} hull(){{ for(p=[[-1,-1],[{W+1},-1],[-1,{D+1}],[{W+1},{D+1}]]) translate([p[0],p[1],8]) cylinder(h=22,r=4.5,$fn=24);'
          f' for(p=[[4,4],[{W-4},4],[4,{D-4}],[{W-4},{D-4}]]) translate([p[0],p[1],33]) scale([1,1,0.6]) sphere(r=8,$fn=24); }}\n')
    s += f'{c(FELT_DK)} translate([-2,-5.6,9]) cube([{W+4},0.6,0.8]);\n'
    s += box(W / 2 - 40, D / 2 - 6, 37.7, W / 2 + 40, D / 2 + 14, 38.0, "#9a9894")
    s += txt(W / 2, D / 2 + 4, 38.0, "( name )", 7, "#efe8da", font="Inter:style=Medium", h=0.3)
    s += f'{c("#d9b98a")} translate([{W/2-12},-7.0,22]) rotate([0,90,0]) cylinder(h=24, d=6, $fn=32);\n'
    s += f'{c("#2f2c2a")} translate([{W/2},-6.0,9]) cube([1.2,1.2,13]);\n'
    return s

def hush_closed_fp():
    return footprint(-6, -6, W + 6, D + 6)

# =========================================================== ONE SHEET, printed
OSP_Z = PZ             # shell top = panel face, printed face-down on SMOOTH PEI (r3: the toolpath shows as sheen)
OSP_EDGE = "#5b4a39"   # legends: dark, by one filament swap at layer 4


# ---- ONE SHEET r3: the toolpath is the finish (first-layer line direction per region, shown as sheen)
OS_PITCH = 1.1      # drawn pitch; the real first-layer pitch is ~0.45 (0.4 nozzle), drawn ~2.5x coarser to read at sheet scale
OS_TONE = {"A": ("#e1d2b1", "#c9b68f"), "B": ("#f1e9d7", "#e2d6bc"), "BAND": ("#e9ddc3", "#d6c7a8")}

def hatch(x0, y0, x1, y1, ang, z, col, pitch=OS_PITCH, w=0.32):
    """parallel first-layer lines at angle ang (deg) clipped to a rectangle, drawn as thin boxes."""
    th = math.radians(ang); ux, uy = math.cos(th), math.sin(th); nx, ny = -uy, ux
    corners = [(x0, y0), (x1, y0), (x0, y1), (x1, y1)]
    ds = [cx * nx + cy * ny for cx, cy in corners]
    out = ""
    d = math.ceil(min(ds) / pitch) * pitch
    while d <= max(ds):
        px, py = d * nx, d * ny
        t0, t1 = -1e9, 1e9
        for p0, u, lo, hi in ((px, ux, x0, x1), (py, uy, y0, y1)):
            if abs(u) < 1e-9:
                if not (lo <= p0 <= hi): t0, t1 = 1, 0
            else:
                a, b = (lo - p0) / u, (hi - p0) / u
                t0, t1 = max(t0, min(a, b)), min(t1, max(a, b))
        if t1 - t0 > 0.5:
            cx, cy = px + ux * (t0 + t1) / 2, py + uy * (t0 + t1) / 2
            out += (f'{c(col)} translate([{cx:.3f},{cy:.3f},{z:.3f}]) rotate([0,0,{ang:.2f}]) '
                    f'translate([{-(t1-t0)/2:.3f},{-w/2:.3f},0]) cube([{t1-t0:.3f},{w:.3f},0.03]);\n')
        d += pitch
    return out

def halo(x, y, z, r0, r1, base, ring, pitch=OS_PITCH, w=0.32):
    """concentric first-layer spot under a knob: a disc of the field cleared, then rings."""
    s = cyl(x, y, z, 0.035, 2 * r1 + 0.6, base, fn=72)
    r = r0
    while r <= r1:
        s += (f'{c(ring)} translate([{x:.3f},{y:.3f},{z+0.035:.3f}]) difference(){{ cylinder(h=0.03,r={r+w/2:.3f},$fn=96);'
              f' translate([0,0,-1]) cylinder(h=2,r={r-w/2:.3f},$fn=96);}}\n')
        r += pitch
    return s

def toolpath_face(z):
    s = ""
    edges = [0.0] + GAP_CENTRES[1:5] + [W]
    for k in range(5):
        kind = "A" if k % 2 == 0 else "B"
        base, line = OS_TONE[kind]
        xa, xb = edges[k] + (0.0 if k == 0 else 0.6), edges[k + 1] - (0.0 if k == 4 else 0.6)
        xa, xb = max(xa, 1.5), min(xb, W - 1.5)
        s += box(xa, 79.0, z, xb, D - 1.5, z + 0.01, base)
        s += hatch(xa, 79.0, xb, D - 1.5, 45 if kind == "A" else -45, z + 0.01, line)
    base, line = OS_TONE["BAND"]       # key-edge band + stick deck: lines along the keys
    s += box(25.5, 52.5, z, W - 6.6, 78.4, z + 0.01, base)
    s += hatch(25.5, 52.5, W - 6.6, 78.4, 0, z + 0.01, line)
    for lab, x, y, kind, midi in KNOBS:
        hero = kind == "hero"
        k = sum(1 for e in GAP_CENTRES[1:5] if x > e)
        tone = OS_TONE["A" if k % 2 == 0 else "B"]
        s += halo(x, y, z + 0.02, (HERO_D / 2 + 0.6) if hero else (KNOB_D / 2 + 0.4), (HERO_D / 2 + 2.9) if hero else (KNOB_D / 2 + 2.6), tone[0], tone[1])
    return s

def one_sheet_printed():
    s = ""
    s += box(2, 2, 0, W - 2, D - 2, 2.5, "#c99b62")                 # laser-cut ply bottom (bridges the seam)
    # shell: top surface over key-edge band + panel; key zone open; rounded vertical corners r 4
    s += rbox(0, 52, 2.5, W, D, OSP_Z, 4, PRINT_CREAM)
    s += rbox(0, 0, 2.5, 6.4, 56, OSP_Z, 2.4, PRINT_CREAM)
    s += rbox(W - 6.4, 0, 2.5, W, 56, OSP_Z, 2.4, PRINT_CREAM)
    s += rbox(0, 0, 2.5, W, 2.4 + 2, OSP_Z - 3, 2.0, PRINT_CREAM)    # low front wall under the key fronts
    s += box(6.4, 3, OSP_Z - 3, 25, 52, OSP_Z, PRINT_CREAM)          # stick column deck (part of the left half)
    # the seam: one straight cut at x 121 through top, front and rear
    s += box(SPLIT_X - 0.2, 52, OSP_Z, SPLIT_X + 0.2, D, OSP_Z + 0.06, "#8d7f68")
    s += box(SPLIT_X - 0.2, -0.06, 2.5, SPLIT_X + 0.2, 0.0, OSP_Z - 3, "#8d7f68")
    s += box(SPLIT_X - 0.2, D, 2.5, SPLIT_X + 0.2, D + 0.06, OSP_Z, "#8d7f68")
    # printed grooves at the section gaps (0.6 deep, 1.2 wide): feel the sections, nothing raised
    for xc in GAP_CENTRES[1:5]:
        if abs(xc - SPLIT_X) > 1:
            s += box(xc - 0.6, 80, OSP_Z - 0.05, xc + 0.6, D - 6, OSP_Z + 0.045, "#b9ab90")
    s += toolpath_face(OSP_Z + 0.005)
    # visible M3 screws, one size (corners + seam)
    for (x, y) in [(8, 172), (W - 8, 172), (8, 82), (W - 8, 82), (SPLIT_X - 5, 172), (SPLIT_X + 5, 172), (SPLIT_X - 5, 57), (SPLIT_X + 5, 57)]:
        s += cyl(x, y, OSP_Z, 0.5, 5.4, "#9b9a95", fn=24) + box(x - 1.3, y - 0.35, OSP_Z + 0.5, x + 1.3, y + 0.35, OSP_Z + 0.55, "#555")
    # section titles in the band, legends by the swap
    for num, name, x0, x1 in SECTIONS:
        s += txt(x0 + 1, 83.0, OSP_Z, num + "  " + name if x1 - x0 > 40 else num, 2.3, OSP_EDGE, font="Inter:style=Bold", halign="left")
    for x0, i in white_keys():
        if i % 7 == 0:
            s += txt(x0 + 9, 58.0, OSP_Z, "C" + str(i // 7 + 1), 2.2, OSP_EDGE, font="Inter:style=Bold")
    s += txt(W - 8, 74.0, OSP_Z, "R  ·  rev 2  ·  printed 2026", 1.7, OSP_EDGE, halign="right")
    s += txt(8, 74.0, OSP_Z, "L  ·  rev 2", 1.7, OSP_EDGE, halign="left")
    s += box(STICK[0] - 9, 5, OSP_Z, STICK[0] + 9, 52 - 2, OSP_Z + 0.4, "#f6f4ee")   # Delrin gate plate in its pocket
    s += stick_column(OSP_Z + 0.4, PRINT_CREAM, OSP_EDGE, mod_knob_col=K_CREAM, plate=False)
    s += keys(white=ACRYL_W, sharp="#2a2826", style="short", plate="#3a352e", wz=OSP_Z)
    s += panel_controls(OSP_Z, knob_col=K_CREAM, eng=OSP_EDGE)
    s += jacks_rear(zc=12) + jacks_rear_labels(5.5, OSP_EDGE)
    return s

def one_sheet_printed_fp():
    return footprint()

# =========================================================== FOLD (round 3)
FO_BD = 106.0          # base depth = lid depth
FO_KZ = 17.5           # key surface (open)
FO_PF = 16.5           # panel face, open (lid lying on the table)
FO_LW = 32.0           # lid surround walls (sides + far edge), open height (systems rev 2: +3 for CUTOFF clearance)
FO_AX = 25.5           # hinge axis height = half the closed stack (51)
FO_KY = 41.0           # keys zone start in the base
FO_SHIFT = 12.0        # visual r3: panel content moved 12 mm toward the lid's far edge, so closed every knob lands over
                       # whites / palm rest (17.5), never over the sharps (19.5); open reach key front -> back row = 145 (= the set)
FO_PLATES = [(3.0, SPLIT_X), (SPLIT_X, 295.0)]   # ONE white panel, two plates meeting in a hairline at the print split
FO_PLATES5 = [(3.0, 38.5), (44.5, 118.0), (124.0, 170.0), (175.8, 261.5), (267.5, 295.0)]  # r2 alternative (inset only)
K_BLACK = "#1c1c1e"
KB_H, KB_D = 13.5, 14.5    # Tayda plastic black knob, 6 mm x 18T split shaft, white indicator (page: ~14.5 x 13.5)

def knob_black(x, y, z, ang, col=K_BLACK, line="#f4f3ef"):
    pts = []
    n = 24
    for i in range(n * 4):
        a = 2 * math.pi * i / (n * 4)
        r = KB_D / 2 - 0.3 * (0.5 + 0.5 * math.cos(n * a))
        pts.append(f"[{r*math.cos(a):.3f},{r*math.sin(a):.3f}]")
    poly = ",".join(pts)
    zt = z + KB_H
    a = math.radians(90 - ang)
    s = f'{c(col)} translate([{x:.3f},{y:.3f},{z:.3f}]) linear_extrude(height={KB_H-1.0}, scale=0.94) polygon([{poly}]);\n'
    s += f'{c("#262628")} translate([{x:.3f},{y:.3f},{z+KB_H-1.0:.3f}]) cylinder(h=1.0, d1={KB_D*0.93:.2f}, d2={KB_D*0.86:.2f}, $fn=48);\n'
    s += (f'{c(line)} translate([{x:.3f},{y:.3f},{zt:.3f}]) rotate([0,0,{math.degrees(a):.1f}]) '
          f'translate([{KB_D*0.08:.2f},-0.5,0]) cube([{KB_D*0.34:.2f},1.0,0.08]);\n')
    return s

def fold_base():
    s = ""
    s += box(0, 0, 0, W, FO_BD, 2.5, "#1f2022")                      # laser-cut bottom plate
    s += rbox(0, 0, 2.5, W, FO_KY, FO_KZ, 3, DARK)                   # palm-rest frame (battery under it)
    s += box(0, FO_KY - 3, 2.5, 3, FO_BD, FO_KZ, DARK)               # side walls
    s += box(W - 3, FO_KY - 3, 2.5, W, FO_BD, FO_KZ, DARK)
    s += box(3, 93, 2.5, W - 3, FO_BD, FO_KZ - 0.6, DARK)            # hinge band + rear wall
    s += box(22, 94.5, FO_KZ - 0.6, W - 22, 102, FO_KZ - 0.1, "#3a3b3e")   # TPU flap over the ribbon slot
    s += box(SPLIT_X - 0.2, -0.06, 2.5, SPLIT_X + 0.2, 0.0, FO_KZ, "#55575b")   # the seam, palm-rest front
    # palm rest: a planed walnut insert, flush (his walnut starts here); a 1 mm dark reveal round it
    s += box(4.0, 4.0, FO_KZ - 6, W - 4.0, FO_KY - 4.0, FO_KZ + 0.02, "#603f28")   # oiled walnut
    s += box(4.0, 3.2, FO_KZ - 0.2, W - 4.0, 4.0, FO_KZ + 0.03, "#141416")       # reveal shadow, front
    # name space: a flush white inlay, blank, two screws (the panel's language: white screwed into the surround)
    s += box(W / 2 - 30, 15, FO_KZ - 0.5, W / 2 + 30, 26, FO_KZ + 0.05, WHITE_P)
    for x in (W / 2 - 27, W / 2 + 27):
        s += cyl(x, 20.5, FO_KZ + 0.05, 0.25, 2.2, "#3a3b3e", fn=16)
    s += stick_column(FO_KZ, DARK, "#c9cacc", mod_knob_col=K_WHITE, y0=FO_KY, ptr="#26272a")
    s += keys(white=ACRYL_W, sharp="#62656b", style="short", plate="#1a1b1d", wz=FO_KZ, sdz=2.0, y0=FO_KY)
    return s

def knuckles(z_ax, y_ax, lid_side):
    s = ""
    for (a, b, owner) in [(3, 8.5, "b"), (8.5, 14.5, "l"), (14.5, 20, "b"), (278, 283.5, "b"), (283.5, 289.5, "l"), (289.5, 295, "b")]:
        if (owner == "l") == lid_side:
            s += f'{c(DARK)} translate([{a},{y_ax},{z_ax}]) rotate([0,90,0]) cylinder(h={b-a-0.3},r=4.6,$fn=40);\n'
            s += f'{c("#9a9da1")} translate([{a-0.05},{y_ax},{z_ax}]) rotate([0,90,0]) cylinder(h=0.1,r=1.9,$fn=20);\n'
    return s

def fold_panel_controls(pf, dy):
    """the common panel content with FOLD's black knobs (cream CUTOFF stays the hero)."""
    return panel_controls(pf, knob_col=K_BLACK, eng="#26272a", hero_col=CREAM, dy=dy, ptr="#f4f3ef",
                          knob_fn=lambda x, y, z, a: knob_black(x, y, z, a))

def fold_lid_local(plates=FO_PLATES):
    """lid in its OPEN position (lying on the table behind the base): y from FO_BD to 2*FO_BD."""
    y0 = FO_BD
    s = ""
    s += rbox(0, y0, 0, W, y0 + FO_BD, 2.0, 3, DARK)                 # back
    s += box(0, y0, 2.0, 2.4, y0 + FO_BD, FO_LW, DARK)              # side walls
    s += box(W - 2.4, y0, 2.0, W, y0 + FO_BD, FO_LW, DARK)
    s += rbox(0, y0 + FO_BD - 2.4, 2.0, W, y0 + FO_BD, FO_LW, 1.2, DARK)   # far edge wall
    s += box(2.4, y0, FO_PF - 3, W - 2.4, y0 + FO_BD - 2.4, FO_PF - 0.4, DARK)   # surround deck
    s += box(SPLIT_X - 0.2, y0 + FO_BD - 0.06, 2, SPLIT_X + 0.2, y0 + FO_BD, FO_LW, "#55575b")
    py0, py1 = y0 + 3.0, y0 + 102.0
    for (a, b) in plates:
        s += box(a, py0, FO_PF - 2.5, b, py1, FO_PF, WHITE_P)
        s += box(a, py0, FO_PF - 0.02, b, py0 + 0.5, FO_PF + 0.03, "#d6d5d0")     # edge chamfer shadow
    if plates is FO_PLATES:
        s += box(SPLIT_X - 0.12, py0, FO_PF - 0.02, SPLIT_X + 0.12, py1, FO_PF + 0.04, "#8f8e8a")   # hairline joint
        for xc in (GAP_CENTRES[1], GAP_CENTRES[3], GAP_CENTRES[4]):     # sunk printed grooves (ONE SHEET's), 0.6 deep
            s += box(xc - 0.6, py0 + 5, FO_PF - 0.05, xc + 0.6, py1 - 5, FO_PF + 0.03, "#c9c8c2")
        for x in (6.5, 62, SPLIT_X - 4.5, SPLIT_X + 4.5, 208, 291.5):
            for y in (py0 + 3.5, py1 - 3.5):
                s += cyl(x, y, FO_PF, 0.35, 2.6, "#2b2c2e", fn=16)
    else:
        for (a, b) in plates:
            for (x, y) in [(a + 3, py0 + 3), (b - 3, py0 + 3), (a + 3, py1 - 3), (b - 3, py1 - 3)]:
                s += cyl(x, y, FO_PF, 0.35, 2.6, "#2b2c2e", fn=16)
    dy = (py0 + FO_SHIFT) - 78.0
    for num, name, x0, x1 in SECTIONS:
        s += txt(x0 + 1.5, 82.5 + dy, FO_PF, num + ("  " + name if x1 - x0 > 30 else ""), 2.2, "#26272a", font="Inter:style=Bold", halign="left")
    s += fold_panel_controls(FO_PF, dy)
    s += jacks_right(zc=9.5, y0=y0 + 32, pitch=11.5, xw=W)
    s += knuckles(FO_AX, FO_BD, True)
    return s

def hardback(x0, y0, wx=235.0, dy=156.0, h=38.0, cloth="#2f4a3e", pages="#efe8d6"):
    """a 400-page hardback novel lying flat, fore-edge (pages) toward the viewer, spine at the back."""
    b = 2.6
    s = rbox(x0, y0, 0, x0 + wx, y0 + dy - 4, b, 1.0, cloth)
    s += rbox(x0, y0, h - b, x0 + wx, y0 + dy - 4, h, 1.0, cloth)
    s += box(x0 + 3, y0 + 3, b, x0 + wx - 3, y0 + dy - 5, h - b, pages)
    s += f'{c(cloth)} translate([{x0},{y0+dy-5},{h/2}]) rotate([0,90,0]) scale([1,0.42,1]) cylinder(h={wx},d={h},$fn=48);\n'
    return s

def fold(open_state=True, book=False):
    s = fold_base() + knuckles(FO_AX, FO_BD, False)
    if open_state:
        s += fold_lid_local()
    else:
        s += f'translate([0,{FO_BD},{FO_AX}]) rotate([180,0,0]) translate([0,{-FO_BD},{-FO_AX}]) {{\n{fold_lid_local()}}}\n'
        zt = 2 * FO_AX
        for k in range(1, 6):
            r = 5 + k * 4.6
            s += (f'{c("#141416")} translate([{W-62},{FO_BD/2},{zt-0.02}]) difference(){{ cylinder(h=0.1,r={r},$fn=72);'
                  f' translate([0,0,-1]) cylinder(h=2,r={r-1.6},$fn=72);}}\n')
        s += box(SPLIT_X - 0.2, 0, zt - 0.02, SPLIT_X + 0.2, FO_BD, zt + 0.05, "#55575b")
        if book:
            s += hardback(322, -8)
    return s

def fold_fp(open_state=True, book=False):
    s = footprint(0, 0, W, 2 * FO_BD if open_state else FO_BD)
    if book:
        s += footprint(322, -8, 557, 148)
    return s

def fold_five_top():
    """r2 alternative for the inset: five faceplates with dark mullions."""
    return fold_lid_local(plates=FO_PLATES5)

# =========================================================== UNDER GLASS
UG_GZ = 24.0; UG_RAIL = 25.4; UG_KZ = 22.0; UG_BOARD = 14.0
WIN = [(60, 122), (180, 254)]
WY = (80, 96)

def ug_board_parts():
    """what the windows show: black-mask board, white silkscreen, gold pads, the parts that make the voice."""
    s = ""
    for (a, b) in WIN:
        s += box(a - 2, WY[0] - 2, UG_BOARD - 1.6, b + 2, WY[1] + 2, UG_BOARD, MASK)
    # VCO cores: 3 x AS3046 DIP-14 + tempco bead bonded on top
    for k in range(3):
        x0 = 61 + k * 20.3
        s += box(x0 + 0.5, 85.0, UG_BOARD, x0 + 19.8, 91.35, UG_BOARD + 4.6, "#1b1b1c")
        for p in range(7):
            for yy in (84.1, 92.2):
                s += box(x0 + 2.0 + p * 2.54, yy - 0.35, UG_BOARD, x0 + 2.6 + p * 2.54, yy + 0.35, UG_BOARD + 0.6, "#e0b956")
        s += cyl(x0 + 10, 88.2, UG_BOARD + 4.6, 1.4, 3.2, "#4fae7f", fn=20)
        for (a_, b_, c_, d_) in [(x0, 84.6, x0 + 20.3, 84.9), (x0, 91.8, x0 + 20.3, 92.1), (x0, 84.6, x0 + 0.3, 92.1), (x0 + 20.0, 84.6, x0 + 20.3, 92.1)]:
            s += box(a_, b_, UG_BOARD, c_, d_, UG_BOARD + 0.03, "#e9e9e6")
        s += txt(x0 + 10, 88.2, UG_BOARD + 4.62, "AS3046", 1.3, "#8d8d8a", h=0.03)
        s += txt(x0 + 10, 82.0, UG_BOARD + 0.02, f"VCO {k+1}", 1.6, "#e9e9e6", h=0.03)
        s += box(x0 + 0.2, 93.4, UG_BOARD, x0 + 19.9, 93.6, UG_BOARD + 0.03, "#e9e9e6")
    # ladder: input pair + 4 rung pairs (TO-92, glued face to face), 4 red film caps, silkscreen ladder rails
    for k in range(5):
        xp = 184 + k * 13
        for d_ in (-2.3, 2.3):
            s += (f'{c("#1b1b1c")} translate([{xp+d_},{84.5},{UG_BOARD}]) intersection(){{ cylinder(h=5.2,d=4.6,$fn=24); '
                  f'translate([{-2.3 if d_<0 else -0.4},-2.4,0]) cube([2.7,4.8,5.3]); }}\n')
        if k > 0:
            s += box(xp - 9.5, 90.0, UG_BOARD, xp - 2.5, 93.5, UG_BOARD + 6.0, "#c0332b")
    s += box(183, 81.6, UG_BOARD, 250, 81.9, UG_BOARD + 0.03, "#e9e9e6")
    s += box(183, 88.2, UG_BOARD, 250, 88.5, UG_BOARD + 0.03, "#e9e9e6")
    s += txt(244, 95.0, UG_BOARD + 0.02, "LADDER", 1.6, "#e9e9e6", h=0.03)
    return s

def under_glass():
    s = ""
    s += box(0, 0, 0, W, D, 3, "#1b1b1c")                            # bottom (black)
    # rear rail: 1 in x 1/2 in U-channel, opening forward
    s += box(0, D - 1.6, 0, W, D, UG_RAIL, ALU)
    s += box(0, D - 12.7, UG_RAIL - 1.6, W, D, UG_RAIL, ALU)
    s += box(0, D - 12.7, 0, W, D, 1.6, ALU)
    # front rail: 1/2 in channel capping the bottom's front edge, below the keys
    s += box(0, 0, 0, W, 1.6, 12.7, ALU)
    s += box(0, 0, 11.1, W, 12.7, 12.7, ALU)
    # end plates: smoked acrylic, the body's side section
    for x0 in (0, W - 3):
        s += box(x0, 1.6, 0, x0 + 3, 52, UG_KZ - 0.5, SMOKE)
        s += box(x0, 52, 0, x0 + 3, D - 1.6, UG_GZ, SMOKE)
    # key bed: strip C front edge + switches read as a dark slot under the tops
    s += box(3, 12.7, 3, W - 3, 52, UG_KZ - 6.0, "#101112")
    s += stick_column(UG_KZ, "#151617", "#e8e8e4", mod_knob_col=K_WHITE)
    s += keys(white="#f7f7f4", sharp="#141415", style="short", plate="#101112", wz=UG_KZ, sdz=2.0)
    # board + the window parts
    s += box(8, 78, UG_BOARD - 1.6, W - 8, D - 13, UG_BOARD, MASK)
    s += ug_board_parts()
    # the glass: painted ground (seen through 3 mm clear) everywhere except the windows and two light dots
    g0, g1 = 52.0, D - 1.6
    xs = [3, WIN[0][0], WIN[0][1], WIN[1][0], WIN[1][1], W - 3]
    s += box(3, g0, UG_GZ - 3, W - 3, WY[0], UG_GZ, GLASS_BLK)
    s += box(3, WY[1], UG_GZ - 3, W - 3, g1, UG_GZ, GLASS_BLK)
    for i in (0, 2, 4):
        s += box(xs[i], WY[0], UG_GZ - 3, xs[i + 1], WY[1], UG_GZ, GLASS_BLK)
    # clear glass over the windows (faint), window frames painted white, polished front edge = key edge
    for (a, b) in WIN:
        s += f'color([0.85,0.95,1.0,0.07]) translate([{a},{WY[0]},{UG_GZ-3}]) cube([{b-a},{WY[1]-WY[0]},3]);\n'
        for (x0_, y0_, x1_, y1_) in [(a - 1.2, WY[0] - 1.2, b + 1.2, WY[0] - 0.7), (a - 1.2, WY[1] + 0.7, b + 1.2, WY[1] + 1.2),
                                     (a - 1.2, WY[0] - 1.2, a - 0.7, WY[1] + 1.2), (b + 0.7, WY[0] - 1.2, b + 1.2, WY[1] + 1.2)]:
            s += box(x0_, y0_, UG_GZ, x1_, y1_, UG_GZ + 0.03, "#e8e8e4")
    s += txt(WIN[0][0], 70.5, UG_GZ, "fig. 1   three oscillators", 2.3, "#e8e8e4", font="DejaVu Serif:style=Italic", halign="left")
    s += txt(WIN[1][0], 70.5, UG_GZ, "fig. 2   the ladder", 2.3, "#e8e8e4", font="DejaVu Serif:style=Italic", halign="left")
    s += box(3, g0 - 0.01, UG_GZ - 3, W - 3, g0 + 0.4, UG_GZ, "#b9c9c5")    # polished glass edge: a line of light
    for x0, i in white_keys():
        if i % 7 == 0:
            s += txt(x0 + 9, 56.5, UG_GZ, "C" + str(i // 7 + 1), 2.0, "#e8e8e4", font="Inter:style=Bold")
    for num, name, x0, x1 in SECTIONS:
        s += box(x0 + 1, 160.5, UG_GZ, x1 - 1, 160.8, UG_GZ + 0.03, "#e8e8e4")
        s += txt(x0 + 1, 163.6, UG_GZ, num + ("  " + name if x1 - x0 > 30 else ""), 2.1, "#e8e8e4", font="Inter:style=Bold", halign="left")
    s += panel_controls(UG_GZ, knob_col=K_WHITE, eng="#e8e8e4", hero_col=CREAM, leds=False, flip_front=(76.6, WIN))
    s += cyl(STATUS_LED[0], STATUS_LED[1], UG_GZ - 0.02, 0.06, 3.0, "#ffb347", fn=24)
    s += cyl(STATUS_LED[0], STATUS_LED[1], UG_GZ - 0.04, 0.05, 6.0, "#7a5a32", fn=24)
    s += txt(STATUS_LED[0], STATUS_LED[1] - 5.5, UG_GZ, "STATUS", 1.6, "#e8e8e4")
    s += cyl(NIC_LED[0], NIC_LED[1], UG_BOARD, 1.0, 2.6, "#efe3c4", fn=16)
    s += jacks_right(zc=13.0, y0=95, pitch=11.5, xw=W)
    return s

def under_glass_fp():
    return footprint()
