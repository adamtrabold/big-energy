"""floss concept round 2, visual turn 2: a fully printed case (PRINCIPLES §7, owner 2026-11-22).
Replaces r2.py (walnut, brass, bookcloth, engraved line: all superseded). Rough 2-D drawings to scale (mm).
Plan coordinates: x right, y away from the player, origin at the module's (or kit's) front-left.
Run from this folder:  python3 r3.py [module fallboard spine cloth yoke]
Material story "stage blacks and spike marks": warm near-black for everything structural (the house),
cream for the deck (the stage, where the hands work) and for every mark you read or set to (spike marks),
coral once (DEPTH), and light for state. Two filament spools (black, cream) + a black TPU for the divider strips.
Draws (python secrets): 'Faced with a choice, do both' · stage lighting · 'the colour comes from the spool, never paint'.
"""
import math, sys, textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.transforms as mt
from matplotlib.patches import Polygon, Circle, Rectangle, FancyBboxPatch, Ellipse
plt.rcParams["font.family"] = "Inter"

BG = "#f6f2ea"; INK = "#1d1b19"; GREY = "#8a8276"; CORAL = "#ef7f68"
BLK = "#2a2725"; BLK2 = "#1a1817"; BLKL = "#48433e"; EDGE = "#5e5750"; WALLTOP = "#3b3733"
CREAM = "#efe8d8"; CREAMD = "#d6ccb6"; RAKE = "#34302d"; TPU = "#141312"; AMBER = "#ffb54a"
CLOTH = "#252321"; CLOTHE = "#3a3633"; THREAD = "#eadfc4"; SKIN = "#cdbca5"; SLAT = "#a88b6a"
SILVER = "#c8c8c6"; KWHITE = "#ecebe7"; LAPTOP = "#9aa0a6"; BOOK = "#7d8a8f"; GRASS = "#86a362"; GRASSD = "#6f8c4f"
PERSON = "#b8a58e"

# ------------------------------------------------------------------ the module, two knob options
def option(k):
    """A: Tayda alu Ø 10 × 8 knobs → 280 × 105 × 35 (35 unit, 8:3:1).  B: family 18T Ø 14.9 × 13.5 → 280 × 112 × 42 (14 unit, 20:8:3)."""
    if k == "A":
        return dict(k="A", D=105.0, H=35.0, DECK=25.0, FY=14.0, RY=31.0, RF=5.0, RR=5.0, RK=5.0, FOOT=41.0, KH=8.0,
                    GY=73.0, GR=23.0, name="A · Ø 10 × 8 knobs · 280 × 105 × 35")
    return dict(k="B", D=112.0, H=42.0, DECK=26.5, FY=14.0, RY=35.9, RF=7.45, RR=7.45, RK=5.0, FOOT=48.5, KH=13.5,
                GY=81.0, GR=23.0, name="B · Ø 14.9 knobs · 280 × 112 × 42")

MW = 280.0; MEND = 70.0; AX = 140.0; CX0, CX1 = 105.0, 175.0
FACETS = [(20.0, 96.0), (184.0, 260.0)]           # flat port facets on the rear arc (plan x ranges)
DIVS = [45.5, 74.5, 125.5, 154.5, 205.5, 234.5]
INSERTS = [(60.0, 30.0), (220.0, 30.0)]

def arc_y(x, D):
    sag = D - MEND; R = (AX ** 2 + sag ** 2) / (2 * sag); cy = D - R
    return cy + math.sqrt(R ** 2 - (x - AX) ** 2)

def rear_y(x, D):
    for a, b in FACETS:
        if a <= x <= b:
            ya, yb = arc_y(a, D), arc_y(b, D)
            return ya + (yb - ya) * (x - a) / (b - a)
    return arc_y(x, D)

def hull(D, ox=0, oy=0, s=1.0, inset=0.0, rf=10.0, n=140):
    pts = []
    for k in range(9):
        a = math.radians(180 + 90 * k / 8); pts.append((rf + rf * math.cos(a), rf + rf * math.sin(a)))
    for k in range(9):
        a = math.radians(270 + 90 * k / 8); pts.append((MW - rf + rf * math.cos(a), rf + rf * math.sin(a)))
    for k in range(n + 1):
        x = MW - MW * k / n; pts.append((x, rear_y(x, D)))
    if inset:
        pts = [(inset + x * (MW - 2 * inset) / MW, inset + y * (D - 2 * inset) / D) for x, y in pts]
    return [(ox + x * s, oy + y * s) for x, y in pts]

FRONT = [("octave", 25, "oct"), ("hold", 60, "hold"), ("attack", 89, "pot"), ("tone", 111, "pot"), ("depth", 140, "coral"),
         ("echo", 169, "pot"), ("tap", 191, "tap"), ("volume", 220, "pot"), ("octave", 255, "oct")]
REAR = [("tabs", 25, "tabs"), ("pressure", 60, "kind"), ("release", 89, "pot"), ("drift", 111, "pot"), ("shimmer", 140, "kind"),
        ("time", 169, "pot"), ("free·sync", 191, "tog"), ("reverb", 220, "pot"), ("tabs", 255, "tabs")]

def grille_holes(M, d=1.9, p=2.6):
    """Hex field of holes inside a circle on the crown top (clipped to the crown's flat top)."""
    holes = []; gx, gy, R = AX, M["GY"], M["GR"]
    top0 = M["FOOT"] + 8 + 1.5
    j = 0; y = gy - R
    while y <= gy + R:
        off = (p / 2) if j % 2 else 0; x = gx - R - off
        while x <= gx + R + p:
            if (x - gx) ** 2 + (y - gy) ** 2 <= (R - d / 2) ** 2 and y >= top0 and y <= rear_y(x, M["D"]) - 5:
                holes.append((x, y))
            x += p
        y += p * 0.866; j += 1
    return holes, len(holes) * math.pi * (d / 2) ** 2

def knob(ax, x, y, k, M, s, z, row):
    r = (M["RF"] if row == "f" else M["RR"]) * s
    if k in ("pot", "oct", "coral"):
        ax.add_patch(Circle((x, y), r, fc=CORAL if k == "coral" else BLK, ec="none", zorder=z))
        if M["k"] == "A":   # knurled aluminium: a ring of fine ticks on the skirt
            ax.add_patch(Circle((x, y), r * 0.78, fc="none", ec=BLKL if k != "coral" else "#d86a55", lw=0.3, zorder=z + 0.05))
        ax.plot([x, x], [y, y + r * 0.85], color=CREAM, lw=0.8 * max(s, 0.4), zorder=z + 0.1)
        if k == "oct":
            for a in range(-2, 3):
                g = math.radians(90 + a * 30)
                ax.plot([x + (r + 0.9 * s) * math.cos(g), x + (r + 2.2 * s) * math.cos(g)],
                        [y + (r + 0.9 * s) * math.sin(g), y + (r + 2.2 * s) * math.sin(g)], color=INK, lw=0.35 * max(s, .5), zorder=z)
    elif k == "kind":
        rk = M["RK"] * s
        ax.add_patch(Circle((x, y), rk, fc=BLK, ec="none", zorder=z))
        ax.plot([x, x], [y, y + rk * 0.85], color=CREAM, lw=0.7 * max(s, 0.4), zorder=z + 0.1)
        for a in range(4):
            g = math.radians(135 - a * 30)
            ax.plot([x + (rk + 0.9 * s) * math.cos(g), x + (rk + 2.0 * s) * math.cos(g)],
                    [y + (rk + 0.9 * s) * math.sin(g), y + (rk + 2.0 * s) * math.sin(g)], color=INK, lw=0.35 * max(s, .5), zorder=z)
    elif k == "hold":
        ax.add_patch(FancyBboxPatch((x - 6 * s, y - 6 * s), 12 * s, 12 * s, boxstyle=f"round,pad=0,rounding_size={2.5*s}", fc=BLK, ec="none", zorder=z))
        ax.add_patch(Circle((x, y), 1.4 * s, fc=CREAM, ec="none", zorder=z + .1))
    elif k == "tap":
        ax.add_patch(Circle((x, y), 6.6 * s, fc=AMBER, ec="none", zorder=z))
        ax.add_patch(Circle((x, y), 5.3 * s, fc=BLK, ec="none", zorder=z + 0.1))
    elif k == "tog":
        ax.add_patch(Rectangle((x - 3 * s, y - 4.5 * s), 6 * s, 9 * s, fc=BLKL, ec="none", zorder=z))
        ax.add_patch(Rectangle((x - 1 * s, y), 2 * s, 5.5 * s, fc=BLK, ec="none", zorder=z + .1))
    elif k == "tabs":
        for j in range(3):
            ax.add_patch(FancyBboxPatch((x - 15 * s + 10 * j * s, y - 7.5 * s), 9 * s, 15 * s,
                                        boxstyle=f"round,pad=0,rounding_size={1.5*s}", fc=BLK, ec="none", zorder=z))
            ax.add_patch(Rectangle((x - 15 * s + 10 * j * s + 2 * s, y + 2 * s), 5 * s, 1.0 * s, fc=BLKL, ec="none", zorder=z + .1))

def module_plan(ax, ox, oy, M, s=1.0, detail=2, z=1, target=None, labels=True):
    D = M["D"]; P = lambda x, y: (ox + x * s, oy + y * s)
    ax.add_patch(Polygon(hull(D, ox, oy, s), closed=True, fc=BLK, ec=EDGE, lw=0.5, zorder=z))
    ax.add_patch(Polygon(hull(D, ox, oy, s, inset=4.0), closed=True, fc=CREAM, ec=CREAMD, lw=0.3, zorder=z + .1))
    F = M["FOOT"]; R1 = F + 8.0
    top = [(x, rear_y(x, D) - 4) for x in [CX1 - i * (CX1 - CX0) / 24 for i in range(25)]]
    ax.add_patch(Polygon([P(CX0, F), P(CX1, F)] + [P(x, y) for x, y in top], closed=True, fc=BLK, ec=EDGE, lw=0.3, zorder=z + .2))
    ax.add_patch(Polygon([P(CX0, F), P(CX1, F), P(CX1, R1), P(CX0, R1)], closed=True, fc=RAKE, ec="none", zorder=z + .25))
    if detail == 0:
        return
    if detail >= 2:
        holes, _ = grille_holes(M)
        for hx, hy in holes:
            ax.add_patch(Circle(P(hx, hy), 0.95 * s, fc="#0c0b0a", ec="none", zorder=z + .3))
        for dx in DIVS:   # flush black TPU strips, front deck edge to the crown foot
            ax.add_patch(Rectangle(P(dx - 0.8, 4.5), 1.6 * s, (F - 5) * s, fc=TPU, ec="none", zorder=z + .3))
    else:
        ax.add_patch(Circle(P(AX, M["GY"]), M["GR"] * s, fc="#121110", ec="none", zorder=z + .3))
        for dx in DIVS:
            ax.add_patch(Rectangle(P(dx - 0.8, 4.5), 1.6 * s, (F - 5) * s, fc=TPU, ec="none", zorder=z + .3))
    for n, x, k in FRONT: knob(ax, *P(x, M["FY"]), k, M, s, z + .5, "f")
    for n, x, k in REAR: knob(ax, *P(x, M["RY"]), k, M, s, z + .5, "r")
    if detail >= 2 and labels:
        fs = 4.4 * s
        for n, x, k in FRONT:
            ax.text(*P(x, M["FY"] + M["RF"] + 2.6), n, ha="center", va="center", fontsize=fs, color=INK, zorder=z + .6, clip_on=True)
        for n, x, k in REAR:
            if k == "tabs":
                for j, t in enumerate(["low", "main", "high"]):
                    ax.text(*P(x - 10 + 10 * j, M["RY"] + 9.7), t, ha="center", va="center", fontsize=fs * .62, color=INK, zorder=z + .7, clip_on=True)
                continue
            if CX0 <= x <= CX1:
                ax.text(*P(x, F + 4), n, ha="center", va="center", fontsize=fs, color=CREAM, zorder=z + .6, clip_on=True)
            else:
                ax.text(*P(x, M["RY"] + (M["RR"] if k == "pot" else M["RK"]) + 2.8), n, ha="center", va="center", fontsize=fs, color=INK, zorder=z + .6, clip_on=True)
    # front rim: graduated rail (cream ticks inlaid in the black rim) + cream target rider
    if detail >= 2:
        for t in range(-130, 131, 10):
            ax.plot([ox + (AX + t) * s] * 2, [oy + 0.6 * s, oy + (3.2 if t == 0 else 2.0) * s], color=CREAM, lw=0.35, zorder=z + .45)
    tx = AX - 18 if target is None else target
    ax.add_patch(Polygon([P(tx - 4, 3.8), P(tx + 4, 3.8), P(tx + 4, 2.0), P(tx + 0.7, 2.0), P(tx, -1.5), P(tx - 0.7, 2.0), P(tx - 4, 2.0)],
                         closed=True, fc=CREAM, ec=CREAMD, lw=0.3, zorder=z + .5))

def module_section(ax, ox, oy, M, s=1.0):
    """Section on the axis, y horizontal (front at left)."""
    D, H, DK, F = M["D"], M["H"], M["DECK"], M["FOOT"]
    P = lambda y, z_: (ox + y * s, oy + z_ * s)
    ax.add_patch(Polygon([P(0, 0), P(D, 0), P(D, H), P(F + 8, H), P(F, DK), P(4, DK), P(4, H), P(0, H)], closed=True, fc="#d9d3ca", ec=BLK, lw=0.7))
    ax.add_patch(Rectangle(P(4, DK - 2.5), (F - 4) * s, 2.5 * s, fc=CREAM, ec=CREAMD, lw=0.3))
    # knobs on the axis: DEPTH (front), SHIMMER mode (rear, Ø 10)
    ax.add_patch(Rectangle(P(M["FY"] - M["RF"], DK), 2 * M["RF"] * s, M["KH"] * s, fc=CORAL, ec="none"))
    ax.add_patch(Rectangle(P(M["RY"] - M["RK"], DK), 2 * M["RK"] * s, 8 * s, fc=BLK, ec="none"))
    # finger room
    y0 = M["RY"] + M["RK"]
    ax.annotate("", xy=P(F, DK + 4), xytext=P(y0, DK + 4), arrowprops=dict(arrowstyle="<->", lw=0.4, color=CORAL, shrinkA=0, shrinkB=0))
    ax.text(*P((y0 + F) / 2, DK + 5.3), f"{F - y0:.0f}", ha="center", fontsize=4.2, color=CORAL)
    # board, sealed box, driver
    ax.add_patch(Rectangle(P(3, 2.4 + 7.5 + 3), (F - 6) * s, 1.6 * s, fc="#3a7a4a", ec="none"))
    ax.add_patch(Rectangle(P(F, 2.4), (D - F - 2.5) * s, (H - 4.4) * s, fc="none", ec="#7a6a55", lw=0.45, ls=(0, (2, 1))))
    dc = F + 27.5
    ax.add_patch(Polygon([P(dc - 27.5, H - 2.5), P(dc + 27.5, H - 2.5), P(dc + 15, H - 2.5 - 20), P(dc - 15, H - 2.5 - 20)], fc="#9c8f7a", ec="none"))
    ax.add_patch(Rectangle(P(dc - 9, H - 2.5 - 24), 18 * s, 4 * s, fc="#555", ec="none"))
    ax.plot([ox + F * s, ox + (F + 8) * s], [oy + DK * s, oy + H * s], color=BLK, lw=0.7)

def module_front(ax, ox, oy, M, s=1.0, target=None):
    H = M["H"]
    ax.add_patch(FancyBboxPatch((ox, oy + 1.2 * s), MW * s, (H - 1.2) * s, boxstyle=f"round,pad=0,rounding_size={3*s}", fc=BLK, ec=EDGE, lw=0.5))
    ax.add_patch(Rectangle((ox + 10 * s, oy), (MW - 20) * s, 1.2 * s, fc=BLK2))
    for t in range(-130, 131, 10):
        ax.plot([ox + (AX + t) * s] * 2, [oy + (H - 0.4) * s, oy + (H - (3.2 if t == 0 else 1.8)) * s], color=CREAM, lw=0.35)
    tx = AX - 18 if target is None else target
    ax.add_patch(Polygon([(ox + (tx - 4) * s, oy + (H + 1.6) * s), (ox + (tx + 4) * s, oy + (H + 1.6) * s), (ox + (tx + 4) * s, oy + (H - 1) * s),
                          (ox + (tx + 0.8) * s, oy + (H - 1) * s), (ox + tx * s, oy + (H - 7) * s), (ox + (tx - 0.8) * s, oy + (H - 1) * s), (ox + (tx - 4) * s, oy + (H - 1) * s)],
                         fc=CREAM, ec=CREAMD, lw=0.3))
    ax.add_patch(FancyBboxPatch((ox + (AX - 4.5) * s, oy + 8 * s), 9 * s, 3.2 * s, boxstyle=f"round,pad=0,rounding_size={1.4*s}", fc="#080808", ec="#555", lw=0.3))
    ax.add_patch(Circle((ox + (AX + 9) * s, oy + 9.6 * s), 1.2 * s, fc=AMBER, ec="none"))

def module_rear(ax, ox, oy, M, s=1.0, word=True):
    """Seen from behind: plan-left facet appears on the right."""
    H = M["H"]
    ax.add_patch(FancyBboxPatch((ox, oy + 1.2 * s), MW * s, (H - 1.2) * s, boxstyle=f"round,pad=0,rounding_size={3*s}", fc=BLK, ec=EDGE, lw=0.5))
    ax.add_patch(Rectangle((ox + 10 * s, oy), (MW - 20) * s, 1.2 * s, fc=BLK2))
    ports_R = [("phones", "jack"), ("line", "jack"), ("midi in", "trs"), ("midi out", "trs")]
    ports_L = [("power", "slide"), ("usb-c", "usbc"), ("tune", "trim"), ("split", "slide")]
    cz = 4 + (H - 8) * 0.45
    for x0, ports in ((MW - 96, ports_R), (20, ports_L)):   # mirrored: plan-right facet (x 184–260) shows at 20–96 from the left
        X0 = ox + x0 * s
        ax.add_patch(Rectangle((X0, oy + 4 * s), 76 * s, (H - 8) * s, fc="#322e2b", ec=BLK2, lw=0.4))
        for i, (n, kind) in enumerate(ports):
            cx = X0 + (9.5 + i * 19) * s; cy = oy + cz * s
            if kind == "jack": ax.add_patch(Circle((cx, cy), 3.0 * s, fc="#080808", ec="#777", lw=0.3))
            if kind == "trs": ax.add_patch(Circle((cx, cy), 2.6 * s, fc="#080808", ec="#777", lw=0.3))
            if kind == "usbc": ax.add_patch(FancyBboxPatch((cx - 4.5 * s, cy - 1.6 * s), 9 * s, 3.2 * s, boxstyle=f"round,pad=0,rounding_size={1.4*s}", fc="#080808", ec="#555", lw=.3))
            if kind == "slide":
                ax.add_patch(Rectangle((cx - 4.5 * s, cy - 2 * s), 9 * s, 4 * s, fc="#080808", ec="none")); ax.add_patch(Rectangle((cx - 4.5 * s, cy - 1.5 * s), 3.5 * s, 3 * s, fc="#999", ec="none"))
            if kind == "trim": ax.add_patch(Circle((cx, cy), 2.4 * s, fc="#999", ec="#444", lw=0.3)); ax.plot([cx - 1.6 * s, cx + 1.6 * s], [cy, cy], color="#333", lw=0.5)
            ax.text(cx, oy + (H - 6) * s, n, fontsize=3.7 * s, ha="center", color=CREAM)
    if word:
        ax.text(ox + AX * s, oy + H * 0.5 * s, "floss", ha="center", va="center", fontsize=10.5 * s, style="italic", color=CREAM)

# ------------------------------------------------------------------ keyboards, objects, people
KB = {"nano": ("Korg nanoKEY2", 325, 83, 16, "#202020", ("#202020", "#4a4a4a")),
      "kbc": ("KMI K-Board C", 325, 84, 11, "#f1f1ef", ("#e4e4e1", "#cdcdca")),
      "xkey": ("CME Xkey 25", 388, 135, 16, SILVER, (KWHITE, INK)),
      "mpk": ("Akai MPK Mini IV", 348, 192, 46, "#3a3a3a", (KWHITE, INK))}

def keyboard(ax, x, y, key, s=1.0, z=3, label=True):
    name, w, d, h, col, keys = KB[key]
    ax.add_patch(FancyBboxPatch((x, y), w * s, d * s, boxstyle=f"round,pad=0,rounding_size={4*s}", fc=col, ec="#666", lw=0.4, zorder=z))
    kw = (w - 30) / 15; k0 = x + 15 * s; kd = 80 if key == "mpk" else min(d * 0.68, 85)
    for i in range(15):
        ax.add_patch(Rectangle((k0 + i * kw * s, y + 4 * s), kw * s, kd * s, fc=keys[0], ec="#888", lw=0.3, zorder=z + .1))
    for i in [0, 1, 3, 4, 5, 7, 8, 10, 11, 12]:
        ax.add_patch(Rectangle((k0 + ((i + 1) * kw - kw * .3) * s, y + (4 + kd * .38) * s), kw * .6 * s, kd * .62 * s, fc=keys[1], ec="none", zorder=z + .2))
    if key == "mpk":
        for i in range(8): ax.add_patch(Rectangle((x + (60 + i * 30) * s, y + 115 * s), 24 * s, 24 * s, fc="#666", ec="none", zorder=z + .2))
    if label:
        ax.text(x + w * s / 2, y + (d - 5) * s, f"{name} · {w} × {d} × {h}", ha="center", va="top", fontsize=max(4.0, 5.0 * s), color="#888", zorder=z + .3, clip_on=True)

def bc_x(x, key, s=1.0):
    w = KB[key][1]; return x + (15 + 7 * (w - 30) / 15) * s

def thighs(ax, x, y, s=1.0, z=0):
    for cx in (x + 85 * s, x + 255 * s):
        ax.add_patch(FancyBboxPatch((cx - 75 * s, y), 150 * s, 430 * s, boxstyle=f"round,pad=0,rounding_size={60*s}", fc=SKIN, ec="none", zorder=z))
    ax.add_patch(Ellipse((x + 170 * s, y - 30 * s), 420 * s, 140 * s, fc="#b9a68c", ec="none", zorder=z))

def bench(ax, x, y, w, d, z=0):
    for i in range(4):
        ax.add_patch(Rectangle((x, y + i * d / 4), w, d / 4 - 8, fc=SLAT, ec="#8d7254", lw=0.5, zorder=z))

def laptop(ax, x, y):
    ax.add_patch(FancyBboxPatch((x, y), 356, 248, boxstyle="round,pad=0,rounding_size=8", fc=LAPTOP, ec="#7d838a", lw=0.5))
    ax.text(x + 178, y + 124, "16-inch laptop\n≈ 356 × 248 × 17\n≈ 2.1 kg", ha="center", va="center", fontsize=6.2, color="white")

def book(ax, x, y):
    ax.add_patch(Rectangle((x, y), 156, 234, fc=BOOK, ec="#677379", lw=0.5))
    ax.text(x + 78, y + 117, "hardback\n≈ 156 × 234 × 35", ha="center", va="center", fontsize=6.0, color="white")

def backpack(ax, x, y):
    ax.add_patch(FancyBboxPatch((x, y), 300, 450, boxstyle="round,pad=0,rounding_size=40", fc="none", ec="#6d7f8a", lw=0.9, ls=(0, (5, 3))))
    ax.text(x + 150, y + 462, "a daypack's main compartment ≈ 300 × 450\n(illustrative, not a product)", ha="center", fontsize=5.6, color="#6d7f8a")

def sheet(title, sub):
    fig = plt.figure(figsize=(16.54, 11.69), dpi=150); fig.patch.set_facecolor(BG)
    fig.text(0.025, 0.968, title, fontsize=13, weight="bold")
    fig.text(0.025, 0.945, sub, fontsize=9, color="#444")
    fig.text(0.025, 0.010, FOOT, fontsize=6.6, color=GREY)
    return fig

def axes(fig, rect, xl, yl):
    ax = fig.add_axes(rect); ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(*xl); ax.set_ylim(*yl); return ax

FOOT = ("floss · concept round 2, visual turn 2 · fully printed case · rough 2-D drawing to scale, not a render · "
        "material story: stage blacks and spike marks (draws: 'Faced with a choice, do both' · stage lighting · 'colour from the spool, never paint')")
LAB = dict(fontsize=6.2, color="#111", bbox=dict(fc="#f6f2ea", ec="none", alpha=0.88, pad=1.2), zorder=40)

# =================================================================== MODULE at 1:1 (A2 landscape, both knob options side by side)
def sheet_module():
    W, Hh = 594.0, 420.0
    fig = plt.figure(figsize=(W / 25.4, Hh / 25.4), dpi=120); fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, Hh); ax.set_aspect("equal"); ax.axis("off")
    T = lambda x, y, t, **k: ax.text(x, y, t, **k)
    T(14, 408, "floss module · 1 : 1 on A2 (print at 100 %) · the knob choice both ways · plan, front, rear, section on the axis", fontsize=12, weight="bold")
    T(14, 401, "Fully printed: warm near-black PETG shell and crown, a cream PETG deck, flush black TPU dividers, cream marks. One coral (DEPTH). "
               "Left: A, the low Ø 10 × 8 knob, 35 holds. Right: B, the family Ø 14.9 knob, the body grows and the ratio is restated.", fontsize=7.2, color="#444")
    ax.add_patch(Rectangle((520, 386), 50, 1.4, fc=INK)); T(520, 389, "0", fontsize=5); T(560, 389, "50 mm", fontsize=5)
    for t in range(0, 51, 10): ax.plot([520 + t] * 2, [386, 388], color=INK, lw=0.4)
    T(520, 381.5, "check: 50 mm when printed at 100 %", fontsize=4.6, color=GREY)
    for col, k in ((0, "A"), (1, "B")):
        M = option(k); D, H = M["D"], M["H"]
        X = 16 + col * 292
        holes, area = grille_holes(M)
        T(X, 372, M["name"], fontsize=9, weight="bold", color=INK)
        sub = ("Tayda aluminium Ø 10 × 8, 6 mm 18T (Big Energy CATHEDRAL's low knob) · deck 25, knob tops 33, rim 35 · "
               "unit 35: 8 : 3 : 1, halves 4 : 3 (a fourth), centre : end 3 : 2 (a fifth)") if k == "A" else \
              ("family 18T push-on Ø 14.5 × 13.5 (Tayda) · deck 26.5, knob tops 41, rim 42 · depth 112 (finger room needs ≈ 108–110) · "
               "restated unit 14: 20 : 8 : 3, halves 5 : 4 (a third), centre : end 8 : 5 (a sixth)")
        T(X, 367, textwrap.fill(sub, 118), fontsize=5.2, color="#444", va="top")
        # plan
        PY = 230
        module_plan(ax, X, PY, M, 1.0, detail=2)
        ax.add_patch(Rectangle((X, PY), MW, D, fc="none", ec=GREY, lw=0.3, ls=(0, (3, 2)), zorder=0.5))
        u = 35 if k == "A" else 14
        for i in range(1, int(MW / u)): ax.plot([X + i * u] * 2, [PY - 3, PY - 1], color=GREY, lw=0.3)
        ax.plot([X + AX] * 2, [PY - 8, PY + D + 3], color=GREY, lw=0.3, ls=(0, (1, 1.5)), zorder=8)
        T(X + AX + 3, PY - 7, "axis 140 · ticks below the plan = the unit", fontsize=4.4, ha="left", color=GREY)
        T(X + MW + 1.5, PY + D - 2, f"{D:.0f}", fontsize=4.8, color=GREY); T(X + MW + 1.5, PY + MEND - 3, "70", fontsize=4.8, color=GREY)
        for ix, iy in INSERTS: ax.add_patch(Circle((X + ix, PY + iy), 4, fc="none", ec=GREY, lw=0.4, ls=(0, (1.5, 1)), zorder=9))
        T(X + 2, PY + D + 4, f"PLAN · grille: Ø 1.9 holes, 2.6 hex pitch, Ø {2*M['GR']:.0f} field on the crown top → {len(holes)} holes ≈ {area:.0f} mm² open (≥ 620) · "
              f"finger room behind DRIFT · SHIMMER · TIME = {M['FOOT'] - (M['RY'] + M['RR']):.0f} mm (≥ 5)", fontsize=4.6, color="#333")
        T(X + 2, PY + D + 9, "dashed circles: ¼\"-20 inserts underneath (S4) · the two flat facets on the rear arc carry the ports (x 20–96, 184–260)", fontsize=4.6, color=GREY)
        # front
        FY = 168
        module_front(ax, X, FY, M)
        T(X, FY + H + 6, "FRONT (faces the keyboard) · cream target rides the inlaid rail · USB-C host + amber port light on the axis · no words", fontsize=5.4, weight="bold")
        # rear
        RY_ = 110
        module_rear(ax, X, RY_, M)
        T(X, RY_ + H + 6, "REAR (from behind) · two port facets; the wordmark on the crown's rear face between them, cream", fontsize=5.4, weight="bold")
        # section
        SX, SY = X + 160, 60
        module_section(ax, SX, SY, M)
        T(X, SY + 40, "SECTION on the axis", fontsize=5.4, weight="bold")
        T(X, SY + 34, textwrap.fill(f"front at left · deck {M['DECK']} · rim {H:.0f} · crown foot y {M['FOOT']:.1f}, rake 8 mm · coral = DEPTH · "
                                    f"the coral arrow = finger room behind SHIMMER mode · driver TEBM28C10-4B Ø 55 × 24 [r2] under the crown, "
                                    f"sealed box (dashed); its exact seat is eng's", 62), fontsize=4.5, color="#444", va="top")
    # bottom band: material story, divider detail, knob verdict
    by = 52
    T(16, by, "ONE MATERIAL STORY: STAGE BLACKS AND SPIKE MARKS", fontsize=7.4, weight="bold")
    story = ("The house is black: shell, crown, knobs and every carry part print in one warm near-black matte PETG, so the instrument recedes the way stage equipment does. "
             "The stage is cream: the sunk deck, where the hands work, is the one lit surface (it also reads best in sun). Spike marks are cream: anything you read or set to on a black "
             "surface (the rail's ticks, the target, the crown's words, the wordmark, the kits' scales, CLOTH's thread). Colour comes from the spool, never paint. "
             "Coral appears once (DEPTH). The lights are the only other colour: both warm amber (TAP's ring, the port light).")
    T(16, by - 4, textwrap.fill(story, 120), fontsize=5.0, color="#333", va="top")
    # divider detail at 4:1
    dx0, dy0, sc = 250, 14, 4.0
    T(dx0 - 4, by, "DIVIDER, section at 4 : 1 (my call: a pressed-in TPU strip)", fontsize=7.0, weight="bold")
    ax.add_patch(Rectangle((dx0, dy0), 40 * sc / 2, 2.5 * sc, fc=CREAM, ec=CREAMD, lw=0.4))
    ax.add_patch(Rectangle((dx0 + 9 * sc, dy0 + 0.5 * sc), 1.6 * sc, 2.0 * sc, fc=TPU, ec="none"))
    T(dx0 + 22 * sc, dy0 + 2.4 * sc, textwrap.fill("black TPU 95A strip 1.6 × 2.0, pressed into a printed 1.6 slot in the cream deck, flush. You find it by the 7 mm wider gap and by its "
                                                    "soft, warm, faintly grippy feel against hard PETG: a change of touch with no edge. Fallback for a one-spool build: a printed groove 1.0 × 0.4.", 58),
      fontsize=4.6, va="top", color="#333")
    # knob verdict
    T(456, by, "THE KNOB, BOTH WAYS (owner decides)", fontsize=7.0, weight="bold")
    v = ("A keeps every part-derived size and the 35 unit; kits stay thin (FALLBOARD 42, SPINE 59). Knurled aluminium pinches well; it's CATHEDRAL's part. "
         "Cost: a smaller knob under the hand, 12 mm of air between knobs. B is the bigger, friendlier knob; the body grows to 112 × 42 and the kits by 7 mm. "
         "My pick: A. floss's knobs are set and tended, not ridden.")
    T(456, by - 4, textwrap.fill(v, 50), fontsize=4.8, va="top", color="#333")
    fig.savefig("../module/module-1to1-A2.png", facecolor=BG, dpi=120)
    fig.savefig("../module/module-1to1-A2.pdf", facecolor=BG)
    for k in "AB":
        print(k, "grille", len(grille_holes(option(k))[0]), round(grille_holes(option(k))[1]))

# =================================================================== kit parts (printed, black)
KW = 412.0; INNER = 404.0; MA = option("A"); MD_ = MA["D"]; MH = MA["H"]

def end_blocks(ax, ox, y_front, kbkey, s=1.0, z=4, depth=80):
    """Blocks run 80 deep from the front wall (y_front = bed's front edge)."""
    w = KB[kbkey][1]; gap = (INNER - w) / 2
    for side in (0, 1):
        bx = ox + 4 * s if side == 0 else ox + (4 + gap + w) * s
        ax.add_patch(Rectangle((bx, y_front), gap * s, depth * s, fc=BLKL, ec=EDGE, lw=0.4, zorder=z))
        lip = bx + (gap - 6) * s if side == 0 else bx
        ax.add_patch(Rectangle((lip, y_front), 6 * s, depth * s, fc="#5a544e", ec="none", zorder=z + .1))
        nx = bx + max(0, gap - 8) * s if side == 0 else bx
        ax.add_patch(Rectangle((nx, y_front + (depth - 15) * s), min(8, gap) * s, 15 * s, fc=BLK2, ec="none", zorder=z + .2))
        ax.add_patch(Circle((bx + gap * s / 2, y_front + depth * s / 2), 2.4 * s, fc=BLK2, ec=EDGE, lw=0.3, zorder=z + .3))

def scale_marks(ax, ox, y, s=1.0, z=5):
    for t in range(0, 33, 4):
        for side in (0, 1):
            X = ox + (4 + t) * s if side == 0 else ox + (KW - 4 - t) * s
            ax.plot([X, X], [y, y + (2.4 if t % 8 else 3.6) * s], color=CREAM, lw=0.45, zorder=z)
    ax.plot([ox + KW / 2 * s] * 2, [y, y + 3.6 * s], color=CREAM, lw=0.6, zorder=z)

def coil(ax, x0, x1, y, s=1.0, z=5, col="#8a8a8a", h=9):
    n = int(abs(x1 - x0) / (3.2 * s))
    for i in range(n): ax.add_patch(Ellipse((x0 + i * 3.2 * s, y), 3.2 * s, h * s, fc="none", ec=col, lw=0.5, zorder=z))

def charger(ax, x, y, s=1.0, z=5):
    ax.add_patch(FancyBboxPatch((x, y), 30 * s, 30 * s, boxstyle=f"round,pad=0,rounding_size={4*s}", fc="#e9e9e9", ec="#999", lw=0.4, zorder=z))
    ax.add_patch(Rectangle((x + 9 * s, y + 13 * s), 12 * s, 4 * s, fc="#555", ec="none", zorder=z + .1))

def adapter(ax, x, y, s=1.0, z=5):
    ax.add_patch(FancyBboxPatch((x, y), 22 * s, 9 * s, boxstyle=f"round,pad=0,rounding_size={2*s}", fc="#6a6a6a", ec="none", zorder=z))

def card(ax, x, y, s=1.0, z=4.9):
    ax.add_patch(Rectangle((x, y), 50 * s, 80 * s, fc=CREAM, ec=CREAMD, lw=0.3, zorder=z))

# =================================================================== FALLBOARD 412 × 265 × 42
FB_D = 265.0; FB_BED = (4, 141); FB_LANE = (141, 156); FB_BAY = (156, 261)
def fallboard_plan(ax, ox, oy, kbkey="xkey", s=1.0, cable=True, md=1, packed=False, seams=True):
    P = lambda x, y: (ox + x * s, oy + y * s)
    ax.add_patch(FancyBboxPatch(P(0, 0), KW * s, FB_D * s, boxstyle=f"round,pad=0,rounding_size={8*s}", fc=WALLTOP, ec=EDGE, lw=0.6, zorder=1))
    ax.add_patch(Rectangle(P(4, 4), INNER * s, (FB_D - 8) * s, fc=BLK, ec="none", zorder=1.1))
    mx = (KW - MW) / 2
    for wx in (mx - 3, mx + MW):    # pocket walls
        ax.add_patch(Rectangle(P(wx, FB_BAY[0]), 3 * s, (FB_BAY[1] - FB_BAY[0]) * s, fc=WALLTOP, ec="none", zorder=1.2))
    ax.add_patch(Polygon(hull(MD_, ox + (mx - 1.5) * s, oy + (FB_BAY[0] - 1.5) * s, s * (MW + 3) / MW), closed=True, fc="none", ec=WALLTOP, lw=1.6 * s, zorder=1.25))
    for a, b in FACETS:   # rear-wall windows
        ax.add_patch(Rectangle(P(mx + a, FB_D - 4), (b - a) * s, 4 * s, fc=BG, ec="none", zorder=1.3))
    if seams:
        ax.plot([ox + KW / 2 * s] * 2, [oy, oy + 4 * s], color=BLK2, lw=0.6, zorder=1.4)
        ax.plot([ox, ox + 4 * s], [oy + 148.5 * s] * 2, color=BLK2, lw=0.6, zorder=1.4)
        ax.plot([ox + (KW - 4) * s, ox + KW * s], [oy + 148.5 * s] * 2, color=BLK2, lw=0.6, zorder=1.4)
    module_plan(ax, ox + mx * s, oy + FB_BAY[0] * s, MA, s, detail=md, z=2)
    w, d = KB[kbkey][1], KB[kbkey][2]
    keyboard(ax, ox + (KW - w) / 2 * s, oy + 4 * s, kbkey, s, z=3, label=s > 0.6)
    end_blocks(ax, ox, oy + 4 * s, kbkey, s)
    scale_marks(ax, ox, oy + 0.4 * s, s)
    # right pocket: charger + card; left pocket: coil + adapter
    card(ax, *P(KW - mx + 6, 170), s); charger(ax, *P(KW - mx + 16, 190), s)
    if packed or cable:
        coil(ax, ox + 12 * s, ox + 56 * s, oy + 222 * s, s, h=22); adapter(ax, *P(20, 175), s)
    if cable:
        sx = (KW - w) / 2 + w * 0.70
        ax.plot([ox + sx * s, ox + sx * s, ox + KW / 2 * s, ox + KW / 2 * s], [oy + (4 + d) * s, oy + 148.5 * s, oy + 148.5 * s, oy + 156 * s], color="#cfcfcf", lw=1.3, zorder=6)
        ax.add_patch(Rectangle(P(sx - 5, 4 + d - 2), 10 * s, 7 * s, fc="#ddd", ec="#777", lw=0.4, zorder=6.1))
        ax.plot([ox + 40 * s, ox + 40 * s, ox + (KW / 2 - 10) * s], [oy + 205 * s, oy + 150 * s, oy + 150 * s], color="#cfcfcf", lw=0.0, zorder=6)
    bx = bc_x(ox + (KW - w) / 2 * s, kbkey, s)
    tgt = (bx - ox) / s - mx
    ax.add_patch(Polygon([P(mx + tgt - 4, 159.8), P(mx + tgt + 4, 159.8), P(mx + tgt, 154.5)], fc=CREAM, ec=CREAMD, lw=0.3, zorder=7))

def fb_side(ax, ox, oy, lid_deg, s=1.0, kb_h=16, kb_d=135, mod_h=MH, lid=True):
    wall_h = mod_h + 1.2 + 4
    ax.add_patch(Rectangle((ox, oy), FB_D * s, 1.2 * s, fc=BLK, ec="none", zorder=2))
    ax.add_patch(Rectangle((ox, oy), 4 * s, 12 * s, fc=BLK, ec="none", zorder=2))
    ax.add_patch(Rectangle((ox + (FB_D - 4) * s, oy), 4 * s, wall_h * s, fc=BLK, ec="none", zorder=2))
    ax.add_patch(Rectangle((ox + 4 * s, oy + 1.2 * s), kb_d * s, kb_h * s, fc=SILVER, ec="#777", lw=0.3, zorder=2))
    b = 1.2; F = MA["FOOT"]
    ax.add_patch(Polygon([(ox + 156 * s, oy + b * s), (ox + 261 * s, oy + b * s), (ox + 261 * s, oy + (b + mod_h) * s), (ox + (156 + F + 8) * s, oy + (b + mod_h) * s),
                          (ox + (156 + F) * s, oy + (b + MA["DECK"]) * s), (ox + 160 * s, oy + (b + MA["DECK"]) * s), (ox + 160 * s, oy + (b + mod_h) * s), (ox + 156 * s, oy + (b + mod_h) * s)],
                         fc=BLKL, ec="none", zorder=2))
    if not lid: return
    hx, hy = ox + FB_D * s, oy + wall_h * s; a = math.radians(lid_deg)
    ex, ey = hx - FB_D * s * math.cos(a), hy + FB_D * s * math.sin(a)
    ax.plot([hx, ex], [hy, ey], color=BLK, lw=2.6, solid_capstyle="butt", zorder=3)
    if 30 < lid_deg < 150:   # over-centre brace: two printed links, locked straight
        p1 = (hx - 95 * s * math.cos(a), hy + 95 * s * math.sin(a)); p3 = (hx - 6 * s, hy - 26 * s); mid = ((p1[0] + p3[0]) / 2, (p1[1] + p3[1]) / 2)
        ax.plot([p1[0], mid[0], p3[0]], [p1[1], mid[1], p3[1]], color=EDGE, lw=1.2, zorder=3)
        ax.add_patch(Circle(mid, 1.6 * s, fc=BG, ec=EDGE, lw=0.6, zorder=3.1))

def fb_closed(ax, ox, oy, s=1.0, D=FB_D):
    ax.add_patch(FancyBboxPatch((ox, oy), KW * s, D * s, boxstyle=f"round,pad=0,rounding_size={8*s}", fc=BLK, ec=EDGE, lw=0.7))
    for i in range(1, 12):     # ribs ghosted (they're underneath): the 35 grid
        ax.plot([ox + (KW / 2 + (i - 6) * 35) * s] * 2, [oy + 6 * s, oy + (D - 6) * s], color="#302d2a", lw=0.5)
    ax.plot([ox + KW / 2 * s] * 2, [oy, oy + D * s], color=BLK2, lw=1.0)
    ax.plot([ox, ox + KW * s], [oy + 148.5 * s] * 2, color=BLK2, lw=1.0)
    for x in (KW / 2 - 50, KW / 2 + 50):
        ax.add_patch(Rectangle((ox + (x - 6) * s, oy - 0.5 * s), 12 * s, 3 * s, fc=BLK2, ec="none"))

def sheet_fallboard():
    fig = sheet("FALLBOARD · printed · in use: bench, lap, the keyboard range, the lane and pockets, the rear wall",
                "One plane, one lid, all black PETG. 412 × 265 × 42. Keyboard against the front wall, a 15 mm lane, the module behind; left pocket = coil + adapter, right = charger. No gutter, no lamp.")
    ax = axes(fig, [0.015, 0.47, 0.32, 0.44], (-70, 560), (-90, 450))
    bench(ax, -60, -10, 600, 400)
    fallboard_plan(ax, 30, 40, "xkey", 0.999)
    ax.add_patch(Rectangle((30, 40 + FB_D), 412, 46, fc=BLK, ec=EDGE, lw=0.5, zorder=8))
    ax.text(236, 40 + FB_D + 23, "lid standing ≈ 100° on its brace (seen from above)", ha="center", fontsize=6, color=CREAM, zorder=9)
    ax.text(236, -45, "▲ you", ha="center", fontsize=8, weight="bold", color="#333")
    ax.text(-60, 432, "ON A BENCH · plan · Xkey 25 · lid standing", fontsize=8.5, weight="bold")
    ax = axes(fig, [0.345, 0.73, 0.30, 0.18], (-30, 300), (-30, 300))
    ax.add_patch(Rectangle((-30, -10), 330, 10, fc=SLAT, ec="none"))
    fb_side(ax, 0, 0, 100)
    ax.text(-30, 298, "side · the lid on a printed over-centre brace (two links\nlock straight at ≈ 100°): music stand and low-sun shade.\nNo lamp: at night only TAP's ring and the port light glow", fontsize=6.4, va="top")
    ax = axes(fig, [0.345, 0.47, 0.30, 0.22], (-60, 330), (-150, 170))
    a8 = math.radians(8)
    ax.add_patch(Polygon([(-50, -6), (330, -6 - 380 * math.tan(a8)), (330, -60 - 380 * math.tan(a8)), (-50, -60)], fc=SKIN, ec="none"))
    tr = mt.Affine2D().rotate_deg_around(0, 0, -8) + ax.transData
    n0, l0 = len(ax.patches), len(ax.lines); fb_side(ax, 0, 0, 0, lid=False)
    for p in ax.patches[n0:]: p.set_transform(tr)
    ax.text(-60, 160, "ON A LAP · side · the lid lifts off its knuckle hinges;\none stiff 412 × 265 board along both thighs", fontsize=6.4, va="top")
    ax.text(-55, -115, "hips", fontsize=6, color="#7a6a55"); ax.text(270, -118, "knees →", fontsize=6, color="#7a6a55")
    ax = axes(fig, [0.655, 0.47, 0.33, 0.44], (-60, 480), (-110, 520))
    thighs(ax, 36, -40)
    fallboard_plan(ax, 0, 30, "kbc", 0.999)
    ax.text(206, -95, "▲ you (hips)", ha="center", fontsize=8, weight="bold", color="#333")
    ax.text(-60, 505, "ON A LAP · plan · lid off · K-Board C against the front wall", fontsize=8.5, weight="bold")
    ax.text(-60, 482, "behind a shallow keyboard the bed is the plug's room, not an empty strip", fontsize=6.4, color="#444")
    # range
    ax = axes(fig, [0.015, 0.04, 0.27, 0.40], (-10, 425), (-50, 650))
    fallboard_plan(ax, 0, 0, "nano", 0.999, cable=True)
    fallboard_plan(ax, 0, 320, "xkey", 0.999, cable=True)
    ax.text(0, -12, "below: smallest, nanoKEY2 325 × 83 · blocks fully out (≈ 40 each);\n54 mm behind it = the plug's room (straight plug or adapter)", fontsize=6.2, va="top")
    ax.text(0, 638, "THE KEYBOARD RANGE · against the front wall · one printed scale", fontsize=8.5, weight="bold")
    ax.text(0, 592, "above: largest, Xkey 25 388 × 135 · blocks fully in (8) · 2 + 15 behind it: flat right-angle plug", fontsize=6.2, va="bottom")
    # zoom
    ax = axes(fig, [0.30, 0.04, 0.36, 0.40], (0, 230), (60, 270))
    fallboard_plan(ax, 0, 0, "nano", 1.0, md=2)
    ax.text(2, 266, "THE LANE AND THE POCKETS (left half, enlarged, nanoKEY2)", fontsize=8.5, weight="bold")
    ax.text(6, 248, "left pocket 59 × 105: coil + C-to-A adapter", **LAB)
    ax.text(70, 145, "lane 404 × 15: the live run to the host port on the axis", **LAB)
    ax.text(60, 100, "plug's room behind a shallow keyboard", **LAB)
    ax.text(6, 70, "end block: printed carriage, foam face, notch for an end socket", **LAB)
    ax.text(118, 232, "cream target over B | C;\nthe module's words read from your seat", **LAB)
    # rear wall
    ax = axes(fig, [0.675, 0.06, 0.315, 0.30], (-10, 425), (-50, 62))
    wall_h = MH + 1.2 + 4
    ax.add_patch(Rectangle((0, 0), KW, wall_h, fc=BLK, ec=EDGE, lw=0.5))
    module_rear(ax, (KW - MW) / 2, 1.2, MA, word=False)
    for a, b in FACETS:
        X = (KW - MW) / 2 + (MW - b); ax.add_patch(Rectangle((X - 2, 3), (b - a) + 4, wall_h - 6, fc="none", ec=EDGE, lw=0.6))
    ax.add_patch(Rectangle((96 + (KW - MW) / 2, 3), 88, wall_h - 4, fc=BLK, ec="none"))
    ax.plot([KW / 2] * 2, [0, wall_h], color=BLK2, lw=0.8)
    ax.text(-10, 58, "REAR WALL (from behind) · two windows on the module's facets", fontsize=8.5, weight="bold")
    ax.text(0, -8, "power, charging, phones and MIDI reachable while it plays; the wordmark stays on the module (inside).\nThe thin line on the axis is the print seam, left as an honest line.", fontsize=6.2, va="top")
    fig.savefig("../fallboard/fallboard-A-in-use.png", facecolor=BG)

def packing_strip(fig, rect, frames, title):
    ax = fig.add_axes(rect); ax.axis("off"); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.text(0, 0.97, title, fontsize=9, weight="bold", va="top")
    n = len(frames)
    for i, (draw, cap) in enumerate(frames):
        sub = fig.add_axes([rect[0] + rect[2] * i / n + 0.004, rect[1] + rect[3] * 0.22, rect[2] / n - 0.01, rect[3] * 0.64])
        sub.set_aspect("equal"); sub.axis("off"); draw(sub)
        ax.text((i + 0.03) / n, 0.18, f"{i+1}", fontsize=11, weight="bold", color=CORAL, va="top")
        ax.text((i + 0.03) / n + 0.022, 0.18, textwrap.fill(cap, 34), fontsize=6.8, va="top", color="#333")

WEIGHTS = {"FALLBOARD": ("0.47–0.60", "1.42–1.81", "1.52–1.91", "1.78–2.17"),
           "SPINE": ("0.42–0.52", "1.37–1.73", "1.47–1.83", "1.73–2.09"),
           "CLOTH": ("0.23–0.36", "1.18–1.57", "1.28–1.67", "1.54–1.93")}

def closed_sheet(kit, title, sub, draw, dims, thick, thick_b, frames, packtitle, standing_fill=BLK):
    fig = sheet(title, sub)
    ax = axes(fig, [0.015, 0.40, 0.63, 0.50], (-20, 1370), (-120, 560))
    draw(ax, 0, 0)
    W_, D_ = dims
    ax.text(W_ / 2, -24, f"{kit} closed · {W_:.0f} × {D_:.0f} × {thick:.0f}  (B knobs: {thick_b})", ha="center", fontsize=7.4, weight="bold")
    laptop(ax, 470, 0); book(ax, 860, 0)
    bx = 1050; backpack(ax, bx, 0)
    ax.add_patch(Rectangle((bx + 150 - D_ / 2, 6), D_, W_, fc=standing_fill, ec=EDGE, lw=0.5))
    c = (300 - D_) / 2
    ax.annotate("", xy=(bx, 300), xytext=(bx + 150 - D_ / 2, 300), arrowprops=dict(arrowstyle="<->", lw=0.6, color=CORAL, shrinkA=0, shrinkB=0))
    ax.text(bx + (150 - D_ / 2) / 2, 308, f"{c:.1f} a side", ha="center", fontsize=6.4, color=CORAL)
    ax.text(bx + 150, -24, f"standing in the pack: {300 - D_:.0f} mm spare across", ha="center", fontsize=6.4)
    ax.text(0, 548, "CLOSED, beside a 16-inch laptop and a hardback, and in a daypack · same scale", fontsize=8.5, weight="bold")
    ax = axes(fig, [0.66, 0.60, 0.32, 0.30], (-20, 330), (-30, 300))
    y = 190
    for name, d, t, col, alt in [(kit, D_, thick, standing_fill, thick_b), ("16-inch laptop", 248, 17, LAPTOP, None), ("hardback", 234, 35, BOOK, None)]:
        ax.add_patch(Rectangle((0, y), d, t, fc=col, ec="none"))
        if alt: ax.add_patch(Rectangle((0, y + t), d, float(str(alt).split()[0]) - t, fc=col, ec="none", alpha=0.3))
        ax.text(d + 6, y + t / 2, f"{name}: {t:.0f}" + (f" (B: {alt})" if alt else ""), fontsize=7, va="center")
        y -= 85
    ax.text(-20, 292, "END VIEWS to scale (depth × thickness) · pale = with B knobs", fontsize=7.4, weight="bold")
    ax = fig.add_axes([0.66, 0.40, 0.32, 0.18]); ax.axis("off")
    cw, n_, k_, x_ = WEIGHTS[kit]
    rows = [("carry parts (systems)", f"{cw} kg"), ("module [r2]", "0.67–0.93 kg"), ("kit + nanoKEY2", f"{n_} kg"), ("kit + K-Board C", f"{k_} kg"),
            ("kit + Xkey 25", f"{x_} kg"), ("for scale: 16-inch laptop", "≈ 2.1 kg")]
    ax.text(0, 1.0, "WEIGHT, honestly (lighter is better; no target)", fontsize=8.4, weight="bold", va="top", transform=ax.transAxes)
    for i, (a_, b_) in enumerate(rows):
        ax.text(0.0, 0.84 - i * 0.14, a_, fontsize=7.4, va="top", transform=ax.transAxes)
        ax.text(0.55, 0.84 - i * 0.14, b_, fontsize=7.4, va="top", weight="bold" if "kit" in a_ else None, transform=ax.transAxes)
    packing_strip(fig, [0.015, 0.03, 0.97, 0.33], frames, packtitle)
    fig.savefig(f"../{kit.lower()}/{kit.lower()}-B-closed-and-packing.png", facecolor=BG)

def fb_frames():
    def f1(a): a.set_xlim(-10, 425); a.set_ylim(-10, 280); fallboard_plan(a, 0, 0, "xkey", .999); a.add_patch(Circle(((KW - MW) / 2 + 58, 262), 14, fc="none", ec=CORAL, lw=1.6, zorder=30))
    def f2(a):
        a.set_xlim(-10, 425); a.set_ylim(-10, 280); fallboard_plan(a, 0, 0, "xkey", .999, cable=False, packed=True)
        a.plot([206, 206, 40, 40], [156, 148.5, 148.5, 200], color="#cfcfcf", lw=1.3, zorder=6)
        a.add_patch(Rectangle((6, 160), 56, 95, fc="none", ec=CORAL, lw=1.6, zorder=30))
    def f3(a): a.set_xlim(-10, 425); a.set_ylim(-10, 280); fallboard_plan(a, 0, 0, "xkey", .999, cable=False, packed=True); [a.add_patch(Circle((x, 44), 12, fc="none", ec=CORAL, lw=1.6, zorder=30)) for x in (8, 404)]
    def f4(a): a.set_xlim(-30, 300); a.set_ylim(-20, 280); fb_side(a, 0, 0, 35); a.text(140, 230, "lid down: a foam strip\npins the keyboard", ha="center", fontsize=6.5)
    def f5(a): a.set_xlim(-10, 425); a.set_ylim(-10, 280); fb_closed(a, 0, 0); a.add_patch(Circle((206, 1), 18, fc="none", ec=CORAL, lw=1.6, zorder=30))
    return [(f1, "Switch off at the module's rear facet, through the left window."),
            (f2, "Unplug the keyboard end. The tail runs along the lane; coil it and the adapter into the left pocket. The cable stays in the host port."),
            (f3, "Thumb-lock both end blocks (they lock empty too: nothing rattles)."),
            (f4, "Lid down. The foam strip presses the keyboard; the knobs sit under the module's rim."),
            (f5, "Two magnets catch. Into the backpack on its 265 edge. Charger and card ride in the right pocket.")]

# =================================================================== SPINE 412 × 148 × 59, open flat 412 × 335
SP_T = 143.0; SP_S = 49.0
def spine_plan(ax, ox, oy, kbkey="xkey", s=1.0, cable=True, md=1):
    P = lambda x, y: (ox + x * s, oy + y * s)
    ax.add_patch(FancyBboxPatch(P(0, 0), KW * s, SP_T * s, boxstyle=f"round,pad=0,rounding_size={6*s}", fc=WALLTOP, ec=EDGE, lw=0.6, zorder=1))
    ax.add_patch(Rectangle(P(4, 4), INNER * s, (SP_T - 4) * s, fc=BLK, ec="none", zorder=1.1))
    y1 = SP_T; y2 = SP_T + SP_S
    ax.add_patch(Rectangle(P(0, y1), KW * s, SP_S * s, fc="#221f1d", ec=EDGE, lw=0.4, zorder=1))
    for yy in (y1 + 2.5, y2 - 2.5): ax.plot([ox, ox + KW * s], [oy + yy * s] * 2, color=BLKL, lw=2.2 * s, zorder=1.05)    # beads
    for i in range(7):   # knuckles
        for yy in (y1, y2):
            ax.add_patch(Rectangle(P(6 + i * 58, yy - 2), 26 * s, 4 * s, fc=BLKL, ec="none", zorder=1.06))
    y3 = y2; MT = SP_T
    ax.add_patch(FancyBboxPatch(P(0, y3), KW * s, MT * s, boxstyle=f"round,pad=0,rounding_size={6*s}", fc=WALLTOP, ec=EDGE, lw=0.6, zorder=1))
    ax.add_patch(Rectangle(P(4, y3), INNER * s, (MT - 4) * s, fc=BLK, ec="none", zorder=1.1))
    mx = (KW - MW) / 2; my = y3 + 34
    for wx in (mx - 3, mx + MW):
        ax.add_patch(Rectangle(P(wx, y3 + 34), 3 * s, (MT - 38) * s, fc=WALLTOP, ec="none", zorder=1.2))
    ax.add_patch(Polygon(hull(MD_, ox + (mx - 1.5) * s, oy + (my - 1.5) * s, s * (MW + 3) / MW), closed=True, fc="none", ec=WALLTOP, lw=1.6 * s, zorder=1.25))
    for a, b in FACETS: ax.add_patch(Rectangle(P(mx + a, y3 + MT - 4), (b - a) * s, 4 * s, fc=BG, ec="none", zorder=1.3))
    module_plan(ax, ox + mx * s, oy + my * s, MA, s, detail=md, z=2)
    w, d = KB[kbkey][1], KB[kbkey][2]
    keyboard(ax, ox + (KW - w) / 2 * s, oy + 4 * s, kbkey, s, z=3, label=s > 0.6)
    end_blocks(ax, ox, oy + 4 * s, kbkey, s)
    scale_marks(ax, ox, oy + 0.4 * s, s)
    card(ax, *P(KW - mx + 6, y3 + 45), s); charger(ax, *P(KW - mx + 16, y3 + 70), s)
    coil(ax, ox + 12 * s, ox + 56 * s, oy + (y3 + 95) * s, s, h=22); adapter(ax, *P(20, y3 + 50), s)
    if cable:
        sx = (KW - w) / 2 + w * 0.70
        ax.plot([ox + sx * s, ox + sx * s, ox + KW / 2 * s, ox + KW / 2 * s], [oy + (4 + d) * s, oy + (y1 + 24) * s, oy + (y1 + 24) * s, oy + my * s], color="#cfcfcf", lw=1.3, zorder=6)
        ax.add_patch(Rectangle(P(sx - 5, 4 + d - 2), 10 * s, 7 * s, fc="#ddd", ec="#777", lw=0.4, zorder=6.1))
    bx = bc_x(ox + (KW - w) / 2 * s, kbkey, s); tgt = (bx - ox) / s
    ax.add_patch(Polygon([P(tgt - 4, my + 3.8), P(tgt + 4, my + 3.8), P(tgt, my - 1.5)], fc=CREAM, ec=CREAMD, lw=0.3, zorder=7))

def spine_closed(ax, ox, oy, s=1.0):
    ax.add_patch(FancyBboxPatch((ox, oy), KW * s, SP_T * s, boxstyle=f"round,pad=0,rounding_size={6*s}", fc=BLK, ec=EDGE, lw=0.7))
    ax.plot([ox + KW / 2 * s] * 2, [oy, oy + SP_T * s], color=BLK2, lw=1.0)
    ax.add_patch(Rectangle((ox, oy + SP_T * s), KW * s, 5 * s, fc="#221f1d", ec=EDGE, lw=0.4))
    for sx in (110, 288): ax.add_patch(Rectangle((ox + sx * s, oy - 2 * s), 14 * s, (SP_T + 9) * s, fc="#121212", ec="none", alpha=0.9))

def spine_elev(ax, ox, oy, s=1.0):
    """The closed box seen on its spine (412 × 59): the two stop beads read as a book's bands."""
    ax.add_patch(FancyBboxPatch((ox, oy), KW * s, 59 * s, boxstyle=f"round,pad=0,rounding_size={4*s}", fc="#221f1d", ec=EDGE, lw=0.6))
    for z_ in (5, 54): ax.add_patch(Rectangle((ox, oy + (z_ - 2.5) * s), KW * s, 5 * s, fc=BLKL, ec="none"))
    for i in range(7):
        for z_ in (5, 54): ax.add_patch(Rectangle((ox + (6 + i * 58) * s, oy + (z_ - 3) * s), 26 * s, 6 * s, fc="#5a544e", ec="none"))
    ax.plot([ox + KW / 2 * s] * 2, [oy, oy + 59 * s], color=BLK2, lw=0.8)
    for sx in (110, 288): ax.add_patch(Rectangle((ox + sx * s, oy - 1), 14 * s, 61 * s, fc="#121212", ec="none", alpha=0.9))

def spine_side(ax, ox, oy, angle, s=1.0):
    kt_h = 23
    ax.add_patch(Rectangle((ox, oy), SP_T * s, 5 * s, fc=BLK, ec="none", zorder=2))
    ax.add_patch(Rectangle((ox, oy), 4 * s, kt_h * s, fc=BLK, ec="none", zorder=2))
    ax.add_patch(Rectangle((ox + 4 * s, oy + 5 * s), 135 * s, 16 * s, fc=SILVER, ec="#777", lw=0.3, zorder=2))
    ax.add_patch(Rectangle((ox + SP_T * s, oy), SP_S * s, 5 * s, fc="#221f1d", ec="none", zorder=2))
    px, py = ox + (SP_T + SP_S) * s, oy; rot = math.radians(180 - angle)
    R = lambda x, y: (px + (x * math.cos(rot) - y * math.sin(rot)) * s, py + (x * math.sin(rot) + y * math.cos(rot)) * s)
    ax.add_patch(Polygon([R(0, 0), R(SP_T, 0), R(SP_T, 36), R(SP_T - 4, 36), R(SP_T - 4, 5), R(0, 5)], closed=True, fc=BLK, ec="none", zorder=2))
    F = MA["FOOT"]
    ax.add_patch(Polygon([R(34, 1.2), R(139, 1.2), R(139, 36.2), R(34 + F + 8, 36.2), R(34 + F, 26.2), R(38, 26.2), R(38, 36.2), R(34, 36.2)], closed=True, fc=BLKL, ec="none", zorder=2.1))

def stop_detail(ax, ox, oy, s=3.0):
    """Section through the spine's edge at 180°: bead face on tray edge face, below the hinge axis (5 mm)."""
    ax.add_patch(Rectangle((ox - 30 * s, oy), 30 * s, 5 * s, fc=BLK, ec=EDGE, lw=0.5))            # keyboard tray floor edge
    ax.add_patch(Rectangle((ox, oy), 22 * s, 3 * s, fc="#221f1d", ec=EDGE, lw=0.5))               # spine panel
    ax.add_patch(Rectangle((ox, oy), 5 * s, 5 * s, fc=BLKL, ec=EDGE, lw=0.5))                      # bead
    ax.add_patch(Circle((ox, oy + 5 * s), 3 * s, fc=WALLTOP, ec=EDGE, lw=0.5))                     # knuckle
    ax.add_patch(Circle((ox, oy + 5 * s), 1.5 * s, fc="#9a9a9a", ec="none"))                       # Ø 3 steel rod
    ax.plot([ox, ox], [oy, oy + 5 * s], color=CORAL, lw=2.0)
    for z_ in (1.2, 3.8):
        ax.annotate("", xy=(ox - 0.3 * s, oy + z_ * s), xytext=(ox - 9 * s, oy + z_ * s), arrowprops=dict(arrowstyle="->", lw=0.6, color="#333"))
        ax.annotate("", xy=(ox + 0.3 * s, oy + z_ * s), xytext=(ox + 9 * s, oy + z_ * s), arrowprops=dict(arrowstyle="->", lw=0.6, color="#333"))
    ax.text(ox - 30 * s, oy - 4 * s, "tray's 5 mm edge face", fontsize=5.6, va="top")
    ax.text(ox + 2 * s, oy - 4 * s, "spine's 5 mm bead", fontsize=5.6, va="top")
    ax.text(ox + 4 * s, oy + 8.5 * s, "hinge axis 5 above the underside;\nØ 3 steel rod in printed knuckles", fontsize=5.6)
    ax.text(ox - 30 * s, oy + 13 * s, "coral line = 412 mm of face meeting face at 180°: a keypress is compression,\nthe pin only hinges. Folding toward closed, the faces part.", fontsize=5.8)

def sheet_spine():
    fig = sheet("SPINE · printed · in use: flat on a bench and a lap, the geometric stop, the keyboard range, the lane and bays, the rear wall",
                "A printed clamshell: keyboard tray and module tray of one outline, joined by a spine whose two 5 mm beads stop it at flat. 412 × 148 × 59 closed, 412 × 335 open. No standing pose, no lamp.")
    ax = axes(fig, [0.015, 0.47, 0.32, 0.44], (-70, 560), (-90, 470))
    ax.add_patch(Rectangle((-60, -10), 600, 420, fc="#b79c7c", ec="none"))
    spine_plan(ax, 30, 40, "xkey", .999)
    ax.text(236, -45, "▲ you", ha="center", fontsize=8, weight="bold", color="#333")
    ax.text(-60, 450, "OPEN FLAT ON A TABLE · plan · 412 × 335", fontsize=8.5, weight="bold")
    ax = axes(fig, [0.345, 0.70, 0.30, 0.21], (-40, 130), (-30, 60))
    stop_detail(ax, 60, 0, 3.0)
    ax.text(-40, 58, "THE STOP AT FLAT · section at 3 : 1", fontsize=8.5, weight="bold")
    ax = axes(fig, [0.345, 0.47, 0.30, 0.20], (-60, 400), (-150, 170))
    a8 = math.radians(8)
    ax.add_patch(Polygon([(-50, -6), (390, -6 - 440 * math.tan(a8)), (390, -60 - 440 * math.tan(a8)), (-50, -60)], fc=SKIN, ec="none"))
    tr = mt.Affine2D().rotate_deg_around(0, 0, -8) + ax.transData
    n0 = len(ax.patches); spine_side(ax, 0, 0, 180)
    for p in ax.patches[n0:]: p.set_transform(tr)
    ax.text(-60, 165, "ON A LAP · side · flat: the stop takes the press across both thighs.\nBridged (held only at its far edges) it folds: don't.", fontsize=6.4, va="top")
    ax.text(-55, -115, "hips", fontsize=6, color="#7a6a55"); ax.text(330, -125, "knees →", fontsize=6, color="#7a6a55")
    ax = axes(fig, [0.655, 0.47, 0.33, 0.44], (-60, 480), (-110, 520))
    thighs(ax, 36, -40); spine_plan(ax, 0, 20, "kbc", .999)
    ax.text(206, -95, "▲ you (hips)", ha="center", fontsize=8, weight="bold", color="#333")
    ax.text(-60, 505, "ON A LAP · plan · K-Board C", fontsize=8.5, weight="bold")
    ax = axes(fig, [0.015, 0.04, 0.27, 0.40], (-10, 425), (-50, 420))
    for yy, k, cap in [(0, "nano", "below: nanoKEY2 · blocks fully out"), (220, "xkey", "above: Xkey 25 · blocks fully in")]:
        ax.add_patch(FancyBboxPatch((0, yy), KW, SP_T, boxstyle="round,pad=0,rounding_size=6", fc=WALLTOP, ec=EDGE, lw=0.6))
        ax.add_patch(Rectangle((4, yy + 4), INNER, SP_T - 4, fc=BLK, ec="none"))
        keyboard(ax, (KW - KB[k][1]) / 2, yy + 4, k); end_blocks(ax, 0, yy + 4, k); scale_marks(ax, 0, yy + 0.4)
        ax.add_patch(Rectangle((0, yy + SP_T), KW, 10, fc="#221f1d", ec="none"))
        ax.text(0, yy - 6 if k == "nano" else yy + SP_T + 16, cap, fontsize=6.2, va="top" if k == "nano" else "bottom")
    ax.text(0, 412, "THE KEYBOARD RANGE · the same printed blocks and scale as FALLBOARD", fontsize=8.5, weight="bold")
    ax = axes(fig, [0.30, 0.04, 0.36, 0.40], (0, 230), (110, 345))
    spine_plan(ax, 0, 0, "xkey", 1.0, md=2)
    ax.text(2, 341, "THE LANE AND THE BAYS (left half, enlarged)", fontsize=8.5, weight="bold")
    ax.text(6, 322, "left bay: coil + adapter", **LAB)
    ax.text(70, 210, "lane 280 × 30: host port → spine gap", **LAB)
    ax.text(70, 160, "spine 49: open, any rear socket, straight plug", **LAB)
    ax.text(6, 125, "end block: printed, foam face, notch", **LAB)
    ax = axes(fig, [0.675, 0.06, 0.315, 0.30], (-10, 425), (-130, 62))
    wall_h = 36
    ax.add_patch(Rectangle((0, 0), KW, wall_h, fc=BLK, ec=EDGE, lw=0.5))
    module_rear(ax, (KW - MW) / 2, 0.6, MA, word=False)
    ax.add_patch(Rectangle((96 + (KW - MW) / 2, 3), 88, wall_h - 4, fc=BLK, ec="none"))
    ax.plot([KW / 2] * 2, [0, wall_h], color=BLK2, lw=0.8)
    ax.text(-10, 58, "MODULE TRAY'S FAR WALL (from behind, open) · two windows", fontsize=8.5, weight="bold")
    spine_elev(ax, 0, -95, 1.0)
    ax.text(0, -102, "below: the closed box on its spine, 412 × 59. The two stop beads and knuckles read\nlike a book's raised bands. No name on the carry: the name is on the module.", fontsize=6.0, va="top")
    fig.savefig("../spine/spine-A-in-use.png", facecolor=BG)

def sp_frames():
    def f1(a): a.set_xlim(-10, 425); a.set_ylim(-10, 350); spine_plan(a, 0, 0, "xkey", .999); a.add_patch(Circle(((KW - MW) / 2 + 58, 333), 14, fc="none", ec=CORAL, lw=1.6, zorder=30))
    def f2(a): a.set_xlim(-10, 425); a.set_ylim(-10, 350); spine_plan(a, 0, 0, "xkey", .999, cable=False); a.add_patch(Rectangle((6, 230), 56, 100, fc="none", ec=CORAL, lw=1.6, zorder=30))
    def f3(a): a.set_xlim(-10, 425); a.set_ylim(-10, 350); spine_plan(a, 0, 0, "xkey", .999, cable=False); [a.add_patch(Circle((x, 44), 12, fc="none", ec=CORAL, lw=1.6, zorder=30)) for x in (8, 404)]
    def f4(a): a.set_xlim(-30, 360); a.set_ylim(-20, 200); spine_side(a, 0, 0, 60); a.text(160, 180, "swing the module tray over:\npanel down onto the keys", ha="center", fontsize=6.5)
    def f5(a): a.set_xlim(-10, 425); a.set_ylim(-60, 200); spine_closed(a, 0, 0)
    return [(f1, "Switch off at the rear facet, through the far wall's left window."),
            (f2, "Unplug the keyboard end (and the adapter). Tail along the lane; coil and adapter into the left bay."),
            (f3, "Thumb-lock both end blocks (they lock empty too)."),
            (f4, "Close: the module tray swings over, panel to keys; knobs under the rim; rim foam pins the keyboard."),
            (f5, "Strap. Into the backpack. Charger and card ride in the right bay.")]

# =================================================================== CLOTH (near-black coated cloth, cream thread)
CS = 800.0; OUT_W, OUT_D = 412.0, 265.0; OUT_Y = CS - 100 - OUT_D     # outline 100 from the far edge: 435 of near cloth
def cloth_plan(ax, ox, oy, kbkey="xkey", s=1.0, cable=True, objects=True):
    P = lambda x, y: (ox + x * s, oy + y * s)
    ax.add_patch(Rectangle(P(0, 0), CS * s, CS * s, fc=CLOTH, ec=CLOTHE, lw=0.6, zorder=1))
    for i in range(1, 8):   # quilting lines (tonal)
        ax.plot([ox + i * 100 * s] * 2, [oy, oy + CS * s], color="#2d2a28", lw=0.5, zorder=1.05)
    fx = (CS - OUT_W) / 2
    ax.add_patch(Rectangle(P(fx, OUT_Y), OUT_W * s, OUT_D * s, fc="none", ec=THREAD, lw=0.9, ls=(0, (4, 1.5)), zorder=1.2))
    ax.plot([ox + CS / 2 * s] * 2, [oy + (OUT_Y - 20) * s, oy + (OUT_Y + OUT_D + 12) * s], color=THREAD, lw=0.6, ls=(0, (6, 4)), zorder=1.2)
    ax.add_patch(Rectangle(P(30, 30), 200 * s, 150 * s, fc=CLOTH, ec=THREAD, lw=0.7, ls=(0, (4, 1.5)), zorder=1.3))   # pocket, near-left
    if objects:
        mx = CS / 2 - MW / 2
        module_plan(ax, ox + mx * s, oy + (OUT_Y + 156) * s, MA, s, detail=1, z=2)
        w, d = KB[kbkey][1], KB[kbkey][2]
        keyboard(ax, ox + (CS / 2 - w / 2) * s, oy + (OUT_Y + 4) * s, kbkey, s, z=3, label=False)
        if cable:
            sx = CS / 2 - w / 2 + w * 0.7
            ax.plot([ox + sx * s, ox + sx * s, ox + CS / 2 * s, ox + CS / 2 * s], [oy + (OUT_Y + 4 + d) * s, oy + (OUT_Y + 150) * s, oy + (OUT_Y + 150) * s, oy + (OUT_Y + 156) * s], color="#cfcfcf", lw=1.3, zorder=6)
    charger(ax, *P(50, 60), s); adapter(ax, *P(100, 70), s); card(ax, *P(150, 50), s, z=5.1)

def person_seated(ax, cx, cy, s=1.0, z=4):
    """Top view, cross-legged, facing +y."""
    ax.add_patch(Ellipse((cx - 120 * s, cy + 170 * s), 230 * s, 120 * s, angle=25, fc=PERSON, ec="none", zorder=z))   # shins
    ax.add_patch(Ellipse((cx + 120 * s, cy + 170 * s), 230 * s, 120 * s, angle=-25, fc=PERSON, ec="none", zorder=z))
    ax.add_patch(Ellipse((cx, cy + 40 * s), 380 * s, 150 * s, fc="#a8957e", ec="none", zorder=z + .1))              # shoulders
    ax.add_patch(Circle((cx, cy + 45 * s), 85 * s, fc="#6d5c4a", ec="none", zorder=z + .2))                          # head
    for sd in (-1, 1):
        ax.plot([cx + sd * 170 * s, cx + sd * 150 * s, cx + sd * 120 * s], [cy + 60 * s, cy + 230 * s, cy + 330 * s], color="#a8957e", lw=6, solid_capstyle="round", zorder=z + .05)

def sheet_cloth():
    fig = sheet("CLOTH · in use: on the grass, on a table, on a lap (two objects), the keyboard range, the pocket",
                "One module and any keyboard in an 800 quilted square of near-black coated cloth, cream thread. Spread liner-up, the stitched 412 × 265 outline (FALLBOARD's footprint) is the frame. On the ground it is the mat.")
    # ground pose, plan
    ax = axes(fig, [0.015, 0.40, 0.40, 0.51], (-150, 1000), (-150, 1000))
    ax.add_patch(Rectangle((-150, -150), 1150, 1150, fc=GRASS, ec="none"))
    import random
    rnd = random.Random(7)
    for _ in range(500):
        x, y = rnd.uniform(-150, 1000), rnd.uniform(-150, 1000)
        ax.plot([x, x + rnd.uniform(-4, 4)], [y, y + 10], color=GRASSD, lw=0.5)
    cloth_plan(ax, 50, 50, "xkey", 1.0)
    person_seated(ax, 450, 120)
    ax.text(-140, 975, "ON THE GRASS · plan · the park pose", fontsize=8.5, weight="bold")
    ax.text(-140, 940, "spread liner-up (coated side to the damp); sit on the 435 mm of near cloth; keyboard on the outline in front of your knees,\n"
                       "module behind it, speaker firing up; the pocket by your left hip", fontsize=6.4, color="#222", va="top")
    # ground pose, side
    ax = axes(fig, [0.43, 0.70, 0.27, 0.21], (-80, 900), (-30, 640))
    ax.add_patch(Rectangle((-80, -30), 980, 30, fc=GRASS, ec="none"))
    ax.add_patch(Rectangle((0, 0), 800, 4, fc=CLOTH, ec="none"))
    ax.add_patch(Rectangle((439, 4), 135, 16, fc=SILVER, ec="#777", lw=0.3))
    ax.add_patch(Polygon([(591, 4), (696, 4), (696, 39), (591 + 49, 39), (591 + 41, 29), (595, 29), (595, 39), (591, 39)], fc=BLK, ec="none"))
    for k in range(3): ax.add_patch(Ellipse((668, 50 + 18 * k), 30 + 16 * k, 6 + 3 * k, fc="none", ec=AMBER, lw=0.6))
    ax.add_patch(Ellipse((160, 60), 260, 110, fc=PERSON, ec="none"))           # crossed legs
    ax.add_patch(Polygon([(80, 70), (230, 70), (330, 360), (220, 400)], fc="#a8957e", ec="none"))   # torso leaning in
    ax.add_patch(Circle((300, 440), 55, fc="#6d5c4a", ec="none"))
    ax.plot([300, 420, 480], [330, 160, 30], color="#a8957e", lw=5, solid_capstyle="round")
    ax.text(-80, 635, "ON THE GRASS · side", fontsize=8.5, weight="bold")
    ax.text(-80, 605, "the crown fires up, so cloth and grass don't muffle it", fontsize=6.2, va="top")
    # table
    ax = axes(fig, [0.72, 0.62, 0.27, 0.29], (-60, 880), (-60, 880))
    ax.add_patch(Rectangle((-50, -50), 920, 920, fc="#b79c7c", ec="none"))
    cloth_plan(ax, 20, 20, "nano", 1.0)
    ax.text(-60, 860, "SPREAD ON A TABLE · nanoKEY2", fontsize=8.5, weight="bold")
    # lap: two objects
    ax = axes(fig, [0.43, 0.40, 0.27, 0.27], (-80, 760), (-120, 560))
    bench(ax, -60, -100, 820, 420)
    thighs(ax, 0, -40)
    keyboard(ax, 8, 200, "kbc", 1.0, z=6)
    ax.add_patch(Rectangle((400, 20), 330, 160, fc=CLOTH, ec="none", zorder=4))
    module_plan(ax, 425, 45, MA, 1.0, detail=1, z=5)
    ax.plot([8 + 325 * 0.7, 8 + 325 * 0.7, 410, 410, 565, 565], [200, 188, 188, 30, 30, 45], color="#cfcfcf", lw=1.3, zorder=7)
    ax.text(-80, 540, "ON A LAP · two objects (honest)", fontsize=8.5, weight="bold")
    ax.text(-80, 510, "keyboard on the lap; module on the folded cloth beside you, 0.5 m cable", fontsize=6.2, color="#444")
    # range
    ax = axes(fig, [0.72, 0.36, 0.27, 0.24], (-20, 900), (-40, 440))
    for i, k in enumerate(["nano", "xkey", "mpk"]):
        x0 = i * 300
        ax.add_patch(Rectangle((x0 - 6, 0), 290, 400, fc=CLOTH, ec="none"))
        s = 0.66
        ax.add_patch(Rectangle((x0 + 2, 20), OUT_W * s, OUT_D * s, fc="none", ec=THREAD, lw=0.6, ls=(0, (4, 1.5))))
        w, d = KB[k][1], KB[k][2]
        keyboard(ax, x0 + 2 + (OUT_W - w) / 2 * s, 22, k, s, label=False)
        module_plan(ax, x0 + 2 + (OUT_W - MW) / 2 * s, 20 + max(156, d + 12) * s, MA, s, detail=0)
        ax.text(x0, 410, ["nanoKEY2", "Xkey 25", "MPK Mini IV (chunky):\nmodule sits past the line"][i], fontsize=5.8, va="bottom")
    ax.text(-20, 470, "THE KEYBOARD RANGE · nothing holds the keys", fontsize=8.5, weight="bold")
    # pocket zoom
    ax = axes(fig, [0.015, 0.04, 0.40, 0.32], (0, 520), (0, 330))
    cloth_plan(ax, 0, 0, "xkey", 1.0, objects=False)
    ax.text(250, 80, "pocket 200 × 150, its edge in cream thread: cable, C-to-A\nadapter, charger and the 1:1 card (what travels with the cable)", **LAB)
    ax.text(250, 250, "cream thread shows on both faces (quilting stitches pass through),\nso the outline reads liner-up on the grass and coated-up on a table", **LAB)
    fig.text(0.015, 0.375, "THE POCKET (near-left corner, enlarged) · weights sewn into the hem, unseen", fontsize=8.5, weight="bold")
    # palette strip
    ax = fig.add_axes([0.44, 0.05, 0.54, 0.28]); ax.axis("off"); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.text(0, 0.95, "ONE STORY ACROSS MODULE AND CARRIES", fontsize=8.5, weight="bold", va="top")
    sw = [(BLK, "warm near-black matte PETG", "shell, crown, knobs, every printed carry part"), (CLOTH, "near-black coated cloth + liner", "CLOTH, its sleeve and pocket"),
          (CREAM, "cream PETG / cream thread", "the deck; every mark you read or set to"), (TPU, "black TPU 95A", "the flush divider strips"),
          (CORAL, "coral", "DEPTH only"), (AMBER, "warm amber light", "TAP's ring, the port light")]
    for i, (c, n, u) in enumerate(sw):
        y = 0.78 - i * 0.13
        ax.add_patch(Rectangle((0.0, y - 0.04), 0.05, 0.09, fc=c, ec="#999", lw=0.4))
        ax.text(0.065, y + 0.02, n, fontsize=7.2, weight="bold", va="center"); ax.text(0.40, y + 0.02, u, fontsize=7.0, va="center", color="#333")
    fig.savefig("../cloth/cloth-A-in-use.png", facecolor=BG)

def cloth_bundle(ax, ox, oy, s=1.0):
    ax.add_patch(FancyBboxPatch((ox, oy), 400 * s, 150 * s, boxstyle=f"round,pad=0,rounding_size={30*s}", fc=CLOTH, ec=CLOTHE, lw=0.8))
    ax.add_patch(Ellipse((ox + 200 * s, oy + 150 * s), 90 * s, 50 * s, fc=CLOTH, ec=CLOTHE, lw=0.6))
    ax.text(ox + 200 * s, oy + 70 * s, "knotted bundle with an Xkey", ha="center", fontsize=6.4, color=THREAD)

def cl_frames():
    def f1(a): a.set_xlim(-10, 810); a.set_ylim(-10, 810); cloth_plan(a, 0, 0, "xkey", 1.0); a.add_patch(Rectangle((22, 22), 216, 166, fc="none", ec=CORAL, lw=1.6, zorder=30))
    def f2(a):
        a.set_xlim(-10, 810); a.set_ylim(-10, 810); a.add_patch(Rectangle((0, 0), 800, 800, fc=CLOTH)); a.add_patch(Rectangle((250, 330), 300, 125, fc="#2f2c29", ec=CLOTHE))
        module_plan(a, 260, 340, MA, 1.0, detail=1, z=3); a.text(400, 300, "module in its sleeve, panel up", ha="center", fontsize=6.4, color=THREAD)
    def f3(a):
        a.set_xlim(-10, 810); a.set_ylim(-10, 810); a.add_patch(Rectangle((0, 0), 800, 800, fc=CLOTH)); a.add_patch(Rectangle((250, 330), 300, 125, fc="#2f2c29", ec=CLOTHE))
        a.add_patch(FancyBboxPatch((206, 325), 388, 135, boxstyle="round,pad=0,rounding_size=4", fc=SILVER, ec="#666", zorder=4)); a.text(400, 392, "keyboard keys-down\non the quilted sleeve", ha="center", fontsize=6.4, zorder=5)
    def f4(a):
        a.set_xlim(-10, 810); a.set_ylim(-10, 810); a.add_patch(Polygon([(400, 0), (800, 400), (400, 800), (0, 400)], fc=CLOTH))
        a.add_patch(FancyBboxPatch((206, 325), 388, 135, boxstyle="round,pad=0,rounding_size=4", fc="#2f2c29", ec=CLOTHE, zorder=4))
    def f5(a): a.set_xlim(-10, 420); a.set_ylim(-60, 260); cloth_bundle(a, 0, 0)
    return [(f1, "Shake the coated side clean. Cable, adapter, charger and card into the pocket."),
            (f2, "Module into its sleeve at the cloth's centre, panel up (knobs under its rim)."),
            (f3, "Keyboard keys-down on the sleeve's quilted top: the keys bear only the keyboard's own weight."),
            (f4, "Fold two opposite corners over the pair (coated side out)."),
            (f5, "Tie the other two (hem weights inside) into the handle knot. Into the backpack.")]

# =================================================================== YOKE: an attachment-point answer (owner, just now)
def yoke_arm(ax, px, py, ang, reach, s=1.0, z=6, side=-1):
    """A printed arm pivoting on the module's ¼"-20 insert (px, py); ang in degrees; a swivel cup at 'reach'."""
    c, sn = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    L = reach + 14.0
    pts = [(-12, -11), (L, -9), (L, 9), (-12, 11)]
    poly = [(px + (x * c - y * sn) * s, py + (x * sn + y * c) * s) for x, y in pts]
    ax.add_patch(Polygon(poly, closed=True, fc=BLK, ec=EDGE, lw=0.5, zorder=z))
    sl = [(55, -3), (150, -3), (150, 3), (55, 3)]
    ax.add_patch(Polygon([(px + (x * c - y * sn) * s, py + (x * sn + y * c) * s) for x, y in sl], closed=True, fc=BLK2, ec="none", zorder=z + .1))
    ax.add_patch(Circle((px, py), 8 * s, fc=BLKL, ec=EDGE, lw=0.5, zorder=z + .2))    # thumbscrew head
    ax.add_patch(Circle((px, py), 2.5 * s, fc=BLK2, ec="none", zorder=z + .3))
    cx, cy = px + reach * c * s, py + reach * sn * s
    ax.add_patch(Circle((cx, cy), 4 * s, fc=BLKL, ec=EDGE, lw=0.4, zorder=z + .4))
    return cx, cy

def yoke_cup(ax, x, y, side, d, s=1.0, z=7):
    """Swivel cup holding the keyboard's end: side -1 = left end (cup opens +x)."""
    w = 12
    x0 = x - (w if side < 0 else 0) * s
    ax.add_patch(Rectangle((x0, y - (d / 2 + 4) * s), w * s, (d + 8) * s, fc=BLK, ec=EDGE, lw=0.5, zorder=z))
    ax.add_patch(Rectangle((x0 + (w - 4 if side < 0 else 0) * s, y - (d / 2 + 4) * s), 4 * s, (d + 8) * s, fc="#5a544e", ec="none", zorder=z + .1))

def sheet_yoke():
    fig = sheet("YOKE · an attachment-point answer (owner: \"the case does not need to surround it, just have an attachment point\") · sketch for the director",
                "No tray, no box: two printed arms swing on the module's own ¼\"-20 inserts (S4). Carry: the keyboard hangs keys-up under the module, held by its ends. Play: swing the arms forward and it sits in front. A stage light's yoke holds a fixture by its two ends and lets it swing.")
    M = MA
    # PLAY plan
    ax = axes(fig, [0.015, 0.42, 0.40, 0.49], (-120, 560), (-260, 300))
    bench(ax, -110, -250, 660, 540)
    ox, oy = 100, 60
    for key, yoff, alpha in (("xkey", 0, 1.0),):
        w, d = KB[key][1], KB[key][2]
        kx, ky = ox + AX - w / 2, oy - 15 - d
        keyboard(ax, kx, ky, key, 1.0, z=3)
        for side, (ix, iy) in ((-1, INSERTS[0]), (1, INSERTS[1])):
            ex, ey = (kx - 6) if side < 0 else (kx + w + 6), ky + d / 2
            px, py = ox + ix, oy + iy
            ang = math.degrees(math.atan2(ey - py, ex - px)); reach = math.hypot(ex - px, ey - py)
            yoke_arm(ax, px, py, ang, reach, z=1.5)
            yoke_cup(ax, ex, ey, side, d)
        module_plan(ax, ox, oy, M, 1.0, detail=1, z=2)
        sx = kx + w * 0.7
        ax.plot([sx, sx, ox + AX, ox + AX], [ky + d, oy - 7, oy - 7, oy], color="#cfcfcf", lw=1.3, zorder=6)
    ax.text(ox + AX, -245, "▲ you", ha="center", fontsize=8, weight="bold", color="#333")
    ax.text(-110, 288, "PLAY · plan · arms swung forward, Xkey 25 in front (module drawn see-through over the arms)", fontsize=8.5, weight="bold")
    ax.text(-110, 268, "the arms run under the module (they're its feet) and out to two swivel cups on the keyboard's ends;\none rigid instrument on a bench or a lap; the cable is 15 mm long in effect", fontsize=6.2, va="top", color="#333")
    # CARRY plan (from below, so the keyboard shows)
    ax = axes(fig, [0.43, 0.42, 0.30, 0.49], (-80, 460), (-120, 360))
    ox, oy = 50, 60
    for row, key in enumerate(["xkey", "nano"]):
        oyr = oy + row * 0 if row == 0 else oy - 999
    key = "xkey"; w, d = KB[key][1], KB[key][2]
    module_plan(ax, ox, oy, M, 1.0, detail=0, z=1)
    kx, ky = ox + AX - w / 2, oy + 52.5 - d / 2
    keyboard(ax, kx, ky, key, 1.0, z=3, label=False)
    ax.add_patch(Polygon(hull(MD_, ox, oy), closed=True, fc="none", ec=CORAL, lw=1.0, ls=(0, (3, 2)), zorder=8))
    for side, (ix, iy) in ((-1, INSERTS[0]), (1, INSERTS[1])):
        ex, ey = (kx - 6) if side < 0 else (kx + w + 6), ky + d / 2
        px, py = ox + ix, oy + iy
        ang = math.degrees(math.atan2(ey - py, ex - px)); reach = math.hypot(ex - px, ey - py)
        yoke_arm(ax, px, py, ang, reach, z=6); yoke_cup(ax, ex, ey, side, d)
    ax.text(-80, 345, "CARRY · plan · arms swung out sideways", fontsize=8.5, weight="bold")
    ax.text(-80, 325, "keyboard keys-up under the module (dashed coral = the module above it, X-ray),\nheld by its ends; 396 × 135 with an Xkey, 333 × 105 with a nanoKEY2", fontsize=6.2, va="top", color="#333")
    # CARRY side
    ax = axes(fig, [0.75, 0.62, 0.24, 0.29], (-40, 300), (-40, 160))
    def carry_side(ax, ox, oy, h=16, d=135):
        ax.add_patch(Rectangle((ox, oy), d + 8, 3, fc=BLK, ec="none"))                         # cup floor (seen through)
        ax.add_patch(Rectangle((ox + 4, oy + 3), d, h, fc=SILVER, ec="#777", lw=0.3))
        for i in range(14): ax.add_patch(Rectangle((ox + 8 + i * 9.4, oy + 3 + h), 8, 1.5, fc=KWHITE, ec="#999", lw=0.2))
        top = oy + 3 + h + 6 + 4
        ax.add_patch(Rectangle((ox + 4 + (d - 105) / 2, top - 4), 105, 4, fc=BLK, ec=EDGE, lw=0.3))      # arm plate / feet
        F = M["FOOT"]; mx0 = ox + 4 + (d - 105) / 2
        ax.add_patch(Polygon([(mx0, top), (mx0 + 105, top), (mx0 + 105, top + 35), (mx0 + F + 8, top + 35), (mx0 + F, top + 25), (mx0 + 4, top + 25), (mx0 + 4, top + 35), (mx0, top + 35)], fc=BLKL, ec="none"))
        ax.add_patch(Rectangle((ox - 4, oy), 4, top + 2 - oy, fc=BLK, ec=EDGE, lw=0.3))
        return top + 35 - oy
    t = carry_side(ax, 0, 0)
    ax.annotate("", xy=(160, 0), xytext=(160, t), arrowprops=dict(arrowstyle="<->", lw=0.6, color=CORAL, shrinkA=0, shrinkB=0))
    ax.text(166, t / 2, f"≈ {t:.0f}", fontsize=7, color=CORAL, va="center")
    ax.text(-40, 150, "CARRY · side (end view)", fontsize=8.5, weight="bold")
    ax.text(-40, 132, "cup floor 3 · keyboard 11–16 · ≥ 6 air above the keys\n(nothing touches a key) · arm plate 4 · module 35", fontsize=6.2, va="top")
    # pack/bag comparison
    ax = axes(fig, [0.75, 0.42, 0.24, 0.18], (-20, 460), (-30, 170))
    rows = [("YOKE (Xkey)", 396, 135, 64, BLK), ("SPINE", 412, 148, 59, BLK), ("FALLBOARD", 412, 265, 42, BLK)]
    y = 120
    for n, w_, d_, t_, c in rows:
        ax.add_patch(Rectangle((0, y), d_, t_ * 0.6, fc=c, ec=EDGE, lw=0.3))
        ax.text(d_ + 6, y + 8, f"{n}: {w_} × {d_} × {t_} ≈ {w_*d_*t_/1e6:.1f} L", fontsize=6.2, va="center")
        y -= 55
    ax.text(-20, 168, "END VIEWS (depth × thickness, half height scale)", fontsize=7.4, weight="bold")
    # the arm, 1:2
    ax = axes(fig, [0.015, 0.04, 0.40, 0.33], (-40, 260), (-70, 110))
    yoke_arm(ax, 20, 20, 0, 160, 1.0)
    yoke_cup(ax, 180, 20, -1, 60)
    ax.text(-40, 105, "ONE ARM (two per kit, mirror pair) · printed black PETG, ≈ 190 × 22 × 4–14", fontsize=8.5, weight="bold")
    ax.text(-40, 88, "pivot: the module's own ¼\"-20 thumbscrew (S4) · slot: the cup slides 55–150 from the pivot (reach 89–165 covers 325–388 keyboards, carry and play) · "
                     "\ncup: swivels on its pin to sit square on the keyboard's end, foam lined, a lip over the end cap, a 15 mm notch for an end socket", fontsize=6.0, va="top")
    ax.text(-40, -40, "detents in the pivot disc at 'carry' and 'play' (printed bumps, no fitting); the arm plate doubles as the module's foot", fontsize=6.0, va="top")
    # comparison table
    ax = fig.add_axes([0.44, 0.04, 0.55, 0.33]); ax.axis("off")
    ax.text(0, 1.0, "HOW IT COMPARES (visual's reading; systems and eng to check)", fontsize=8.5, weight="bold", va="top", transform=ax.transAxes)
    hdr = ["", "YOKE", "FALLBOARD", "SPINE", "CLOTH"]
    rws = [["carry parts", "≈ 0.08–0.12 kg [est]", "0.47–0.60", "0.42–0.52", "0.23–0.36"],
           ["closed (Xkey)", "396 × 135 × ≈ 64", "412 × 265 × 42", "412 × 148 × 59", "≈ 400 × 150 × 65 soft"],
           ["keys protected by", "the module, 6 mm above", "lid", "module tray", "quilted sleeve"],
           ["cable / adapter / charger", "stays plugged / clip on an arm / loose", "pockets", "bays", "pocket"],
           ["lap", "one rigid piece", "one board", "flat, stopped", "two objects"],
           ["family reuse", "any module with S4", "bed, blocks, lid", "trays, spine", "cloth, outline"],
           ["makes", "4 small prints", "≈ 11 prints, joints", "6 halves + rods", "sewing"]]
    cols = [0.0, 0.17, 0.42, 0.59, 0.78]
    for j, h in enumerate(hdr): ax.text(cols[j], 0.88, h, fontsize=7.4, weight="bold", transform=ax.transAxes, va="top")
    for i, r in enumerate(rws):
        for j, c in enumerate(r): ax.text(cols[j], 0.78 - i * 0.105, c, fontsize=6.6, transform=ax.transAxes, va="top", color="#222" if j else "#555")
    fig.savefig("../yoke/yoke-A-carry-and-play.png", facecolor=BG)

if __name__ == "__main__":
    which = sys.argv[1:] or ["module", "fallboard", "spine", "cloth", "yoke"]
    if "module" in which: sheet_module()
    if "fallboard" in which:
        sheet_fallboard()
        closed_sheet("FALLBOARD", "FALLBOARD · closed and packing: size, weight, pack-up order",
                     "Closed it's one black board, about a 15-inch laptop's footprint and 2½ laptops thick. The lid's only mark is the print-seam cross; the name is on the module inside.",
                     lambda ax, x, y: fb_closed(ax, x, y), (KW, FB_D), 42, "48 · 412 × 272", fb_frames(), "PACKING (unpack is the reverse)")
    if "spine" in which:
        sheet_spine()
        closed_sheet("SPINE", "SPINE · closed and packing: size, weight, pack-up order",
                     "Closed it's a black box like a thick hardback, a little wider than the keyboard: the smallest rigid enclosing kit.",
                     lambda ax, x, y: spine_closed(ax, x, y), (KW, 148), 59, "66", sp_frames(), "PACKING (unpack is the reverse)")
    if "cloth" in which:
        sheet_cloth()
        closed_sheet("CLOTH", "CLOTH · wrapped and packing: size, weight, wrap order",
                     "Wrapped it's a soft near-black bundle the size of the keyboard you bring (≈ 400 × 150 × 65 with an Xkey; the module alone ≈ 290 × 115 × 45). The lightest enclosing kit.",
                     lambda ax, x, y: cloth_bundle(ax, x, y), (400, 150), 65, "72", cl_frames(), "WRAPPING (unwrap is the reverse)", standing_fill=CLOTH)
    if "yoke" in which: sheet_yoke()
