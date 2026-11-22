"""floss concept round 2, visual turn 3 (director steer 2): a fully printed case in a warm walnut-brown house.
Supersedes r2.py and this file's own turn-2 version (near-black "stage blacks"; see notes/visual.md). Rough 2-D drawings to scale (mm).
Plan coordinates: x right, y away from the player, origin at the module's (or kit's) front-left.
Run from this folder:  python3 r3.py [module fallboard spine yoke]      (cloth: retired, kept only as functions YOKE's wrap reuses)
Colour system (colour from the spool, never paint): walnut-brown house (ASA/PETG); a cream stage only where the hands work; cream marks on brown;
gold knurled aluminium knobs (bought finish); black only for switches you flip or press and the TPU dividers; one coral (DEPTH); amber light.
"""
import math, sys, textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.transforms as mt
from matplotlib.patches import Polygon, Circle, Rectangle, FancyBboxPatch, Ellipse
plt.rcParams["font.family"] = "Inter"

BG = "#f6f2ea"; INK = "#1d1b19"; GREY = "#8a8276"; CORAL = "#ef7f68"
HOUSE = "#6e4831"; HOUSED = "#4b2f1f"; HOUSEL = "#8a644b"; RAKEC = "#5c3b28"
GOLD = "#cfae62"; GOLDD = "#9c7d38"; SW = "#1a1918"
BLK = HOUSE; BLK2 = "#3b2416"; BLKL = "#8f6a52"; EDGE = HOUSED; WALLTOP = "#7f573f"     # kit parts: the same walnut-brown house
CREAM = "#efe8d8"; CREAMD = "#d6ccb6"; RAKE = RAKEC; TPU = "#141312"; AMBER = "#ffb54a"
CLOTH = "#252321"; CLOTHE = "#3a3633"; THREAD = "#eadfc4"; SKIN = "#cdbca5"; SLAT = "#a88b6a"
SILVER = "#c8c8c6"; KWHITE = "#ecebe7"; LAPTOP = "#9aa0a6"; BOOK = "#7d8a8f"; GRASS = "#86a362"; GRASSD = "#6f8c4f"
PERSON = "#b8a58e"

# ------------------------------------------------------------------ the module (steer 2: walnut-brown house, cream stage, roof, speaker E)
def option(k):
    """A (baseline): Tayda alu Ø 10 × 8 → 280 × 105 × 35.  B (owner's column): family 18T Ø 14.5 × 13.5 → 280 × 112 × 42.
    STAGE = where the cream ends (= crown foot, 5 mm behind the rear knobs). RUN = the roof's raked edge in plan (≥ 63° [r3])."""
    if k == "A":
        return dict(k="A", D=105.0, H=35.0, DECK=25.0, FY=14.0, RY=31.0, RF=5.0, RR=5.0, RK=5.0, KH=8.0, STAGE=41.0, FOOT=41.0, RUN=5.0,
                    name="A (baseline) · Ø 10 × 8 knobs · 280 × 105 × 35")
    return dict(k="B", D=112.0, H=42.0, DECK=26.5, FY=14.0, RY=35.9, RF=7.45, RR=7.45, RK=5.0, KH=13.5, STAGE=48.4, FOOT=48.4, RUN=5.0,
                name="B (owner's column) · Ø 14.5 knobs · 280 × 112 × 42")

MW = 280.0; MEND = 70.0; AX = 140.0
FACETS = [(20.0, 96.0), (184.0, 260.0)]           # flat port facets: chords under the roof's arc (plan x ranges)
DIVS = [45.5, 74.5, 125.5, 154.5, 205.5, 234.5]
INSERTS = [(60.0, 30.0), (220.0, 30.0)]
DRV_DX = 31.0                                     # speaker E: two drivers at x 140 ± 31
CROWN_W = 125.0

def arc_y(x, D):
    sag = D - MEND; R = (AX ** 2 + sag ** 2) / (2 * sag); cy = D - R
    return cy + math.sqrt(max(0.0, R ** 2 - (x - AX) ** 2))

def rear_y(x, D):
    return arc_y(x, D)

def chord_y(x, D):
    for a, b in FACETS:
        if a <= x <= b:
            ya, yb = arc_y(a, D), arc_y(b, D); return ya + (yb - ya) * (x - a) / (b - a)
    return arc_y(x, D)

def hull(D, ox=0, oy=0, s=1.0, inset=0.0, rf=10.0, n=140):
    pts = []
    for k in range(9):
        a = math.radians(180 + 90 * k / 8); pts.append((rf + rf * math.cos(a), rf + rf * math.sin(a)))
    for k in range(9):
        a = math.radians(270 + 90 * k / 8); pts.append((MW - rf + rf * math.cos(a), rf + rf * math.sin(a)))
    for k in range(n + 1):
        x = MW - MW * k / n; pts.append((x, arc_y(x, D)))
    if inset:
        pts = [(inset + x * (MW - 2 * inset) / MW, inset + y * (D - 2 * inset) / D) for x, y in pts]
    return [(ox + x * s, oy + y * s) for x, y in pts]

FRONT = [("octave", 25, "oct"), ("hold", 60, "hold"), ("attack", 89, "pot"), ("tone", 111, "pot"), ("depth", 140, "coral"),
         ("echo", 169, "pot"), ("tap", 191, "tap"), ("volume", 220, "pot"), ("octave", 255, "oct")]
REAR = [("tabs", 25, "tabs"), ("pressure", 60, "kind"), ("release", 89, "pot"), ("drift", 111, "pot"), ("shimmer", 140, "kind"),
        ("time", 169, "pot"), ("free·sync", 191, "tog"), ("reverb", 220, "pot"), ("tabs", 255, "tabs")]

def grille_holes(M, d=2.0, p=2.6, R=23.0):
    """Two Ø 46 hex fields of Ø 2.0 holes on 2.6 pitch [r3], one over each driver, clipped to the roof's flat."""
    holes = []; gy = M["STAGE"] + 32.0; top0 = M["STAGE"] + M["RUN"] + 1.5
    for gx in (AX - DRV_DX, AX + DRV_DX):
        j = 0; y = gy - R
        while y <= gy + R:
            off = (p / 2) if j % 2 else 0; x = gx - R - off
            while x <= gx + R + p:
                if (x - gx) ** 2 + (y - gy) ** 2 <= (R - d / 2) ** 2 and top0 <= y <= arc_y(x, M["D"]) - 5:
                    holes.append((x, y))
                x += p
            y += p * 0.866; j += 1
    return holes, len(holes) * math.pi * (d / 2) ** 2

def knob(ax, x, y, k, M, s, z, row):
    r = (M["RF"] if row == "f" else M["RR"]) * s
    if k in ("pot", "oct", "coral"):
        ax.add_patch(Circle((x, y), r, fc=CORAL if k == "coral" else GOLD, ec=GOLDD if k != "coral" else "#cf654f", lw=0.4, zorder=z))
        ax.add_patch(Circle((x, y), r * 0.72, fc="none", ec=GOLDD if k != "coral" else "#cf654f", lw=0.3, zorder=z + 0.05))
        ax.plot([x, x], [y + r * 0.2, y + r * 0.9], color=HOUSED, lw=0.8 * max(s, 0.4), zorder=z + 0.1)
        if k == "oct":
            for a in range(-2, 3):
                g = math.radians(90 + a * 30)
                ax.plot([x + (r + 0.9 * s) * math.cos(g), x + (r + 2.2 * s) * math.cos(g)],
                        [y + (r + 0.9 * s) * math.sin(g), y + (r + 2.2 * s) * math.sin(g)], color=HOUSED, lw=0.35 * max(s, .5), zorder=z)
    elif k == "kind":
        rk = M["RK"] * s
        ax.add_patch(Circle((x, y), rk, fc=GOLD, ec=GOLDD, lw=0.4, zorder=z))
        ax.plot([x, x], [y + rk * 0.2, y + rk * 0.9], color=HOUSED, lw=0.7 * max(s, 0.4), zorder=z + 0.1)
        for a in range(4):
            g = math.radians(135 - a * 30)
            ax.plot([x + (rk + 0.9 * s) * math.cos(g), x + (rk + 2.0 * s) * math.cos(g)],
                    [y + (rk + 0.9 * s) * math.sin(g), y + (rk + 2.0 * s) * math.sin(g)], color=HOUSED, lw=0.35 * max(s, .5), zorder=z)
    elif k == "hold":
        ax.add_patch(FancyBboxPatch((x - 6 * s, y - 6 * s), 12 * s, 12 * s, boxstyle=f"round,pad=0,rounding_size={2.5*s}", fc=SW, ec="none", zorder=z))
        ax.add_patch(Circle((x, y), 1.4 * s, fc=CREAM, ec="none", zorder=z + .1))
    elif k == "tap":
        ax.add_patch(Circle((x, y), 6.6 * s, fc=AMBER, ec="none", zorder=z))
        ax.add_patch(Circle((x, y), 5.3 * s, fc=SW, ec="none", zorder=z + 0.1))
    elif k == "tog":
        ax.add_patch(Rectangle((x - 3 * s, y - 4.5 * s), 6 * s, 9 * s, fc="#5a5653", ec="none", zorder=z))
        ax.add_patch(Rectangle((x - 1 * s, y), 2 * s, 5.5 * s, fc=SW, ec="none", zorder=z + .1))
    elif k == "tabs":
        for j in range(3):
            ax.add_patch(FancyBboxPatch((x - 15 * s + 10 * j * s, y - 7.5 * s), 9 * s, 15 * s,
                                        boxstyle=f"round,pad=0,rounding_size={1.5*s}", fc=SW, ec="none", zorder=z))
            ax.add_patch(Rectangle((x - 15 * s + 10 * j * s + 2 * s, y + 2 * s), 5 * s, 1.0 * s, fc="#4a4644", ec="none", zorder=z + .1))

def stage_poly(M, ox, oy, s, inset=4.0, rf=6.0):
    st = M["STAGE"]; pts = []
    for k in range(9):
        a = math.radians(180 + 90 * k / 8); pts.append((inset + rf + rf * math.cos(a), inset + rf + rf * math.sin(a)))
    for k in range(9):
        a = math.radians(270 + 90 * k / 8); pts.append((MW - inset - rf + rf * math.cos(a), inset + rf + rf * math.sin(a)))
    pts += [(MW - inset, st), (inset, st)]
    return [(ox + x * s, oy + y * s) for x, y in pts]

def module_plan(ax, ox, oy, M, s=1.0, detail=2, z=1, target=None, labels=True, ghost115=False):
    D = M["D"]; st = M["STAGE"]; run = M["RUN"]; P = lambda x, y: (ox + x * s, oy + y * s)
    ax.add_patch(Polygon(hull(D, ox, oy, s), closed=True, fc=HOUSE, ec=HOUSED, lw=0.5, zorder=z))
    ax.add_patch(Polygon(stage_poly(M, ox, oy, s), closed=True, fc=CREAM, ec=CREAMD, lw=0.3, zorder=z + .1))
    ax.add_patch(Polygon([P(4, st), P(MW - 4, st), P(MW - 4, st + run), P(4, st + run)], closed=True, fc=RAKEC, ec="none", zorder=z + .15))
    # the crown: the speaker box's own printed lid, set in the roof with a hairline seam
    c0, c1 = AX - CROWN_W / 2, AX + CROWN_W / 2
    top = [(x, arc_y(x, D) - 5) for x in [c1 - i * CROWN_W / 30 for i in range(31)]]
    ax.add_patch(Polygon([P(c0, st + run + 1), P(c1, st + run + 1)] + [P(x, y) for x, y in top], closed=True, fc="none", ec=HOUSED, lw=0.4 * max(s, .5), zorder=z + .2))
    if detail == 0:
        return
    if detail >= 2:
        holes, _ = grille_holes(M)
        for hx, hy in holes: ax.add_patch(Circle(P(hx, hy), 1.0 * s, fc="#24160e", ec="none", zorder=z + .3))
        for a, b in FACETS:   # the facets are chords under the roof's lip: dashed in plan
            xs = [a + (b - a) * i / 20 for i in range(21)]
            ax.plot([ox + x * s for x in xs], [oy + chord_y(x, D) * s for x in xs], color=CREAMD, lw=0.35, ls=(0, (2, 1.5)), zorder=z + .3)
        if ghost115:
            pts = hull(115.0, ox, oy, s)
            ax.plot([p[0] for p in pts[18:]], [p[1] for p in pts[18:]], color=GREY, lw=0.4, ls=(0, (3, 2)), zorder=z - .1)
    else:
        for gx in (AX - DRV_DX, AX + DRV_DX): ax.add_patch(Circle(P(gx, st + 32), 21 * s, fc="#3a2416", ec="none", zorder=z + .3))
    for dx in DIVS:
        ax.add_patch(Rectangle(P(dx - 0.8, 4.5), 1.6 * s, (st - 4.5) * s, fc=TPU, ec="none", zorder=z + .3))
    for n, x, k in FRONT: knob(ax, *P(x, M["FY"]), k, M, s, z + .5, "f")
    for n, x, k in REAR: knob(ax, *P(x, M["RY"]), k, M, s, z + .5, "r")
    if detail >= 2 and labels:
        fs = 4.4 * s
        for n, x, k in FRONT:
            ax.text(*P(x, M["FY"] + M["RF"] + 2.6), n, ha="center", va="center", fontsize=fs, color=HOUSED, zorder=z + .6, clip_on=True)
        for n, x, k in REAR:
            if k == "tabs":
                for j, t in enumerate(["low", "main", "high"]):
                    ax.text(*P(x - 10 + 10 * j, st + run / 2), t, ha="center", va="center", fontsize=fs * .62, color=CREAM, zorder=z + .7, clip_on=True)
                continue
            ax.text(*P(x, st + run / 2), n, ha="center", va="center", fontsize=fs * 0.9, color=CREAM, zorder=z + .6, clip_on=True)
    if detail >= 2:
        for t in range(-130, 131, 10):
            ax.plot([ox + (AX + t) * s] * 2, [oy + 0.6 * s, oy + (3.2 if t == 0 else 2.0) * s], color=CREAM, lw=0.35, zorder=z + .45)
    tx = AX - 18 if target is None else target
    ax.add_patch(Polygon([P(tx - 4, 3.8), P(tx + 4, 3.8), P(tx + 4, 2.0), P(tx + 0.7, 2.0), P(tx, -1.5), P(tx - 0.7, 2.0), P(tx - 4, 2.0)],
                         closed=True, fc=CREAM, ec=CREAMD, lw=0.3, zorder=z + .5))

def module_section(ax, ox, oy, M, s=1.0):
    """Section through the left driver (x = 109), y horizontal, front at left."""
    D, H, DK, st, run = M["D"], M["H"], M["DECK"], M["STAGE"], M["RUN"]
    P = lambda y, z_: (ox + y * s, oy + z_ * s)
    ax.add_patch(Polygon([P(0, 0), P(D, 0), P(D, H), P(st + run, H), P(st, DK), P(4, DK), P(4, H), P(0, H)], closed=True, fc=HOUSEL, ec=HOUSED, lw=0.7))
    ax.add_patch(Rectangle(P(4, DK - 2.0), (st - 4) * s, 2.0 * s, fc=CREAM, ec=CREAMD, lw=0.3))
    ax.add_patch(Rectangle(P(M["FY"] - M["RF"], DK + 1), 2 * M["RF"] * s, M["KH"] * s, fc=GOLD, ec="none"))
    ax.add_patch(Rectangle(P(M["RY"] - M["RR"], DK + 1), 2 * M["RR"] * s, M["KH"] * s, fc=GOLD, ec="none"))
    y0 = M["RY"] + M["RR"]
    ax.annotate("", xy=P(st, DK + 4), xytext=P(y0, DK + 4), arrowprops=dict(arrowstyle="<->", lw=0.4, color=CORAL, shrinkA=0, shrinkB=0))
    ax.text(*P((y0 + st) / 2, DK + 5.3), f"{st - y0:.0f}", ha="center", fontsize=4.2, color=CORAL)
    for zb in (11.0, 17.0): ax.add_patch(Rectangle(P(5, zb), (st - 9) * s, 1.6 * s, fc="#3a7a4a", ec="none"))   # two stacked boards, front band
    ax.add_patch(Rectangle(P(st + 1, 2.0), (D - st - 3) * s, (H - 4) * s, fc="none", ec="#7a5a45", lw=0.45, ls=(0, (2, 1))))
    dc = st + 32
    ax.add_patch(Polygon([P(dc - 27.5, H - 3), P(dc + 27.5, H - 3), P(dc + 15, H - 3 - 20), P(dc - 15, H - 3 - 20)], fc="#9c8f7a", ec="none"))
    ax.add_patch(Rectangle(P(dc - 9, H - 3 - 24), 18 * s, 4 * s, fc="#555", ec="none"))
    ax.add_patch(Circle(P(D - 14, 10), 8 * s, fc="none", ec="#7a5a45", lw=0.5))
    ax.text(*P(D - 14, 10), "port", fontsize=3.4, ha="center", va="center", color="#5a4030")

def module_front(ax, ox, oy, M, s=1.0, target=None):
    H = M["H"]
    ax.add_patch(FancyBboxPatch((ox, oy + 1.2 * s), MW * s, (H - 1.2) * s, boxstyle=f"round,pad=0,rounding_size={3*s}", fc=HOUSE, ec=HOUSED, lw=0.5))
    ax.add_patch(Rectangle((ox + 10 * s, oy), (MW - 20) * s, 1.2 * s, fc=HOUSED))
    for t in range(-130, 131, 10):
        ax.plot([ox + (AX + t) * s] * 2, [oy + (H - 0.4) * s, oy + (H - (3.2 if t == 0 else 1.8)) * s], color=CREAM, lw=0.35)
    tx = AX - 18 if target is None else target
    ax.add_patch(Polygon([(ox + (tx - 4) * s, oy + (H + 1.6) * s), (ox + (tx + 4) * s, oy + (H + 1.6) * s), (ox + (tx + 4) * s, oy + (H - 1) * s),
                          (ox + (tx + 0.8) * s, oy + (H - 1) * s), (ox + tx * s, oy + (H - 7) * s), (ox + (tx - 0.8) * s, oy + (H - 1) * s), (ox + (tx - 4) * s, oy + (H - 1) * s)],
                         fc=CREAM, ec=CREAMD, lw=0.3))
    ax.add_patch(FancyBboxPatch((ox + (AX - 8) * s, oy + 6 * s), 16 * s, 10 * s, boxstyle=f"round,pad=0,rounding_size={3*s}", fc=HOUSED, ec="none"))
    ax.add_patch(FancyBboxPatch((ox + (AX - 4.5) * s, oy + 9.4 * s), 9 * s, 3.2 * s, boxstyle=f"round,pad=0,rounding_size={1.4*s}", fc="#080808", ec="none"))
    ax.add_patch(Circle((ox + (AX + 13) * s, oy + 11 * s), 1.2 * s, fc=AMBER, ec="none"))

def module_rear(ax, ox, oy, M, s=1.0, word=True):
    """Seen from behind: the roof's arc runs unbroken along the top; the two facets are flat bays under its lip."""
    H = M["H"]
    ax.add_patch(FancyBboxPatch((ox, oy + 1.2 * s), MW * s, (H - 1.2) * s, boxstyle=f"round,pad=0,rounding_size={3*s}", fc=HOUSE, ec=HOUSED, lw=0.5))
    ax.add_patch(Rectangle((ox + 10 * s, oy), (MW - 20) * s, 1.2 * s, fc=HOUSED))
    ports_R = [("phones", "jack"), ("line", "jack"), ("midi in", "trs"), ("midi out", "trs")]
    ports_L = [("power", "slide"), ("usb-c", "usbc"), ("tune", "trim"), ("split", "slide")]
    cz = 4 + (H - 10) * 0.45
    for x0, ports in ((MW - 96, ports_R), (20, ports_L)):
        X0 = ox + x0 * s
        ax.add_patch(Rectangle((X0, oy + 3 * s), 76 * s, (H - 8) * s, fc=HOUSED, ec="#3a2316", lw=0.4))
        for i, (n, kind) in enumerate(ports):
            cx = X0 + (9.5 + i * 19) * s; cy = oy + cz * s
            if kind == "jack": ax.add_patch(Circle((cx, cy), 3.0 * s, fc="#080808", ec="#777", lw=0.3))
            if kind == "trs": ax.add_patch(Circle((cx, cy), 2.6 * s, fc="#080808", ec="#777", lw=0.3))
            if kind == "usbc": ax.add_patch(FancyBboxPatch((cx - 4.5 * s, cy - 1.6 * s), 9 * s, 3.2 * s, boxstyle=f"round,pad=0,rounding_size={1.4*s}", fc="#080808", ec="#555", lw=.3))
            if kind == "slide":
                ax.add_patch(Rectangle((cx - 4.5 * s, cy - 2 * s), 9 * s, 4 * s, fc="#080808", ec="none")); ax.add_patch(Rectangle((cx - 4.5 * s, cy - 1.5 * s), 3.5 * s, 3 * s, fc="#999", ec="none"))
            if kind == "trim": ax.add_patch(Circle((cx, cy), 2.4 * s, fc="#999", ec="#444", lw=0.3)); ax.plot([cx - 1.6 * s, cx + 1.6 * s], [cy, cy], color="#333", lw=0.5)
            ax.text(cx, oy + (H - 7.5) * s, n, fontsize=3.7 * s, ha="center", color=CREAM)
    ax.plot([ox + 4 * s, ox + (MW - 4) * s], [oy + (H - 2.2) * s] * 2, color=HOUSED, lw=0.4)
    if word:
        ax.text(ox + AX * s, oy + H * 0.45 * s, "floss", ha="center", va="center", fontsize=10.5 * s, style="italic", color=CREAM)


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

def backpack(ax, x, y, label=True):
    ax.add_patch(FancyBboxPatch((x, y), 300, 450, boxstyle="round,pad=0,rounding_size=40", fc="none", ec="#6d7f8a", lw=0.9, ls=(0, (5, 3))))
    if label: ax.text(x + 150, y + 462, "a daypack's main compartment ≈ 300 × 450\n(illustrative, not a product)", ha="center", fontsize=5.6, color="#6d7f8a")

def sheet(title, sub):
    fig = plt.figure(figsize=(16.54, 11.69), dpi=150); fig.patch.set_facecolor(BG)
    fig.text(0.025, 0.968, title, fontsize=13, weight="bold")
    fig.text(0.025, 0.953, textwrap.fill(sub, 240), fontsize=8, color="#444", va="top")
    fig.text(0.025, 0.010, FOOT, fontsize=6.6, color=GREY)
    return fig

def axes(fig, rect, xl, yl):
    ax = fig.add_axes(rect); ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(*xl); ax.set_ylim(*yl); return ax

FOOT = ("floss · concept round 2, visual turn 3 (steer 2) · fully printed case · rough 2-D drawing to scale, not a render · "
        "walnut-brown house from the spool, cream stage and marks, gold knobs, one coral, amber light")
LAB = dict(fontsize=6.2, color="#111", bbox=dict(fc="#f6f2ea", ec="none", alpha=0.88, pad=1.2), zorder=40)

# =================================================================== MODULE at 1:1 (A2 landscape, A beside B)
def sheet_module():
    W, Hh = 594.0, 420.0
    fig = plt.figure(figsize=(W / 25.4, Hh / 25.4), dpi=120); fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, Hh); ax.set_aspect("equal"); ax.axis("off")
    T = lambda x, y, t, **k: ax.text(x, y, t, **k)
    T(14, 408, "floss module · 1 : 1 on A2 (print at 100 %) · A (baseline) beside B · plan, front, rear, section through a driver · speaker E", fontsize=12, weight="bold")
    T(14, 401, "Walnut-brown house (ASA or PETG, from the spool), a cream stage that ends 5 mm behind the rear row, the house rising behind it as the roof that holds the crown. "
               "Two drivers, two grilles. One fair rear arc; the two port facets sit under its lip. Gold knurled knobs, one coral (DEPTH), amber lights.", fontsize=7.2, color="#444")
    ax.add_patch(Rectangle((520, 386), 50, 1.4, fc=INK)); T(520, 389, "0", fontsize=5); T(560, 389, "50 mm", fontsize=5)
    for t in range(0, 51, 10): ax.plot([520 + t] * 2, [386, 388], color=INK, lw=0.4)
    T(520, 381.5, "check: 50 mm when printed at 100 %", fontsize=4.6, color=GREY)
    for col, k in ((0, "A"), (1, "B")):
        M = option(k); D, H = M["D"], M["H"]
        X = 16 + col * 292
        holes, area = grille_holes(M)
        T(X, 372, M["name"], fontsize=9, weight="bold", color=INK)
        sub = ("Tayda aluminium 3010 Ø 10 × 8, 6 mm 18T, gold (in stock [r3]) · deck 25, knob tops 34, rim 35 · rows y 14 / 31 · stage ends y 41 (= crown foot) · "
               "unit 35: 8 : 3 : 1; 105 holds with speaker E's ≈ 4 % margin, ≈ 115 if not (dashed)") if k == "A" else \
              ("family 18T Ø 14.5 × 13.5 · deck 26.5, rim 42 · rows y 14 / 35.9 · stage ends y 48.4 · drawn 112 deep; with speaker E systems expects 112–120 · "
               "the ratio is restated after the fact (the director's objection to B)")
        T(X, 367, textwrap.fill(sub, 118), fontsize=5.2, color="#444", va="top")
        PY = 230
        module_plan(ax, X, PY, M, 1.0, detail=2, ghost115=(k == "A"))
        ax.add_patch(Rectangle((X, PY), MW, D, fc="none", ec=GREY, lw=0.3, ls=(0, (3, 2)), zorder=0.5))
        if k == "A":
            for i in range(1, 8): ax.plot([X + i * 35] * 2, [PY - 3, PY - 1], color=GREY, lw=0.3)
        ax.plot([X + AX] * 2, [PY - 8, PY + D + 3], color=GREY, lw=0.3, ls=(0, (1, 1.5)), zorder=8)
        T(X + AX + 3, PY - 7, "axis 140" + (" · ticks = the 35 unit" if k == "A" else ""), fontsize=4.4, ha="left", color=GREY)
        T(X + MW + 1.5, PY + D - 2, f"{D:.0f}", fontsize=4.8, color=GREY); T(X + MW + 1.5, PY + MEND - 3, "70", fontsize=4.8, color=GREY)
        if k == "A": T(X + AX + 66, PY + 113, "dashed: 115 if E's margin doesn't hold", fontsize=4.2, color=GREY)
        for ix, iy in INSERTS: ax.add_patch(Circle((X + ix, PY + iy), 4, fc="none", ec=GREY, lw=0.4, ls=(0, (1.5, 1)), zorder=9))
        T(X + 2, PY + D + 9 + (7 if k == "A" else 0), f"PLAN · two grilles, each a Ø 46 field of Ø 2.0 holes on 2.6 hex pitch [r3], clipped to the roof's flat → {len(holes)} holes ≈ {area:.0f} mm² open in all (≥ 620 per driver: "
              f"{area/2:.0f} each) · finger room behind DRIFT · SHIMMER · TIME = {M['STAGE'] - (M['RY'] + M['RR']):.0f} mm", fontsize=4.5, color="#333")
        T(X + 2, PY + D + 4 + (7 if k == "A" else 0), "dashed cream lines on the arc: the two flat port facets, under the roof's lip · dashed circles: ¼\"-20 inserts underneath (S4) · hairline: the crown = the speaker box's own printed lid", fontsize=4.5, color=GREY)
        FY = 168
        module_front(ax, X, FY, M)
        T(X, FY + H + 6, "FRONT (faces the keyboard) · cream target on the inlaid rail · USB-C host in a recessed pocket + amber port light · no words", fontsize=5.4, weight="bold")
        RY_ = 110
        module_rear(ax, X, RY_, M)
        T(X, RY_ + H + 6, "REAR (from behind) · the roof's arc unbroken along the top; two flat facets under its lip; cream wordmark between them", fontsize=5.4, weight="bold")
        SX, SY = X + 160, 58
        module_section(ax, SX, SY, M)
        T(X, SY + 44, "SECTION through the left driver (x 109)", fontsize=5.4, weight="bold")
        T(X, SY + 38, textwrap.fill(f"front at left · deck {M['DECK']} · rim {H:.0f} · the cream ends at y {M['STAGE']:.1f}; the roof's raked edge rises {H - M['DECK']:.0f} mm in 5 (≥ 63° [r3]) · "
                                    f"behind it the whole rear region is the ported box (dashed) · two stacked boards in the front band · cells under the jambs (not in this section)", 62), fontsize=4.5, color="#444", va="top")
    by = 52
    T(16, by, "COLOUR AND MATERIAL: THE IDEA OF THE THING", fontsize=7.4, weight="bold")
    story = ("A string machine is a piece of furniture you play: a warm wooden house with a lit keyboard of controls. So the house is warm walnut-brown, from the spool "
             "(director S3: warmth is the owner's word; the family is walnut and cream). The cream stage is only where the hands work; behind it the house rises as a roof and carries "
             "the speaker. Cream marks sit on brown (rail, target, roof words, wordmark). Gold knurled aluminium knobs (eng: gold in stock, black not until Jan 2027) bring back the "
             "family's brass honestly, as a bought finish. Black only for what you flip or press (tabs, HOLD, TAP, toggle) and the TPU dividers. One coral. Amber light. "
             "The alternative for the owner, in one line: the same system with a near-black house.")
    T(16, by - 4, textwrap.fill(story, 120), fontsize=5.0, color="#333", va="top")
    dx0, dy0, sc = 250, 14, 4.0
    T(dx0 - 4, by, "DIVIDER, section at 4 : 1: pressed-in black TPU strip", fontsize=7.0, weight="bold")
    ax.add_patch(Rectangle((dx0, dy0), 40 * sc / 2, 2.0 * sc, fc=CREAM, ec=CREAMD, lw=0.4))
    ax.add_patch(Rectangle((dx0 + 9 * sc, dy0 + 0.0 * sc), 1.6 * sc, 2.0 * sc, fc=TPU, ec="none"))
    T(dx0 + 22 * sc, dy0 + 2.4 * sc, textwrap.fill("TPU 95A, 1.6 × 2.0, in a printed slot, flush. Black, not brown: black TPU is the stock colour, and on cream it reads "
                                                    "as a drawn rule, the same black as the tabs and HOLD (the things you touch). Felt as softer and grippier, no edge. "
                                                    "Fallback: a printed groove 1.0 × 0.4. With a split print, the shell's seams at x 74.5 / 205.5 hide under two strips [r3].", 58),
      fontsize=4.6, va="top", color="#333")
    T(456, by, "THE KNOB (owner decides; director recommends A)", fontsize=7.0, weight="bold")
    v = ("A keeps the part-derived 280 × 105 × 35 and the 35 unit; every kit stays 7 mm thinner. Cost: a smaller knob under the hand. "
         "B is the bigger knob; the body grows to 112–120 × 42 and the ratio is found after the fact. "
         "Stepped controls are now firmware-stepped 9 mm pots [r3]: you see and hear the step, you don't feel it.")
    T(456, by - 4, textwrap.fill(v, 50), fontsize=4.8, va="top", color="#333")
    fig.savefig("../module/module-1to1-A2.png", facecolor=BG, dpi=120)
    fig.savefig("../module/module-1to1-A2.pdf", facecolor=BG)
    for k in "AB":
        h, a = grille_holes(option(k)); print(k, "grille holes", len(h), "area", round(a))


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
    ax.add_patch(Polygon([(ox + 156 * s, oy + b * s), (ox + 261 * s, oy + b * s), (ox + 261 * s, oy + (b + mod_h) * s), (ox + (156 + F + 5) * s, oy + (b + mod_h) * s),
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
    for i in range(-11, 12):   # ribs underneath on a 17.5 grid [r3 §6c], ghosted
        ax.plot([ox + (KW / 2 + i * 17.5) * s] * 2, [oy + 6 * s, oy + (D - 6) * s], color="#7a543c", lw=0.35)
    for j in range(1, int(D / 17.5)):
        ax.plot([ox + 6 * s, ox + (KW - 6) * s], [oy + j * 17.5 * s] * 2, color="#7a543c", lw=0.35)
    ax.plot([ox + KW / 2 * s] * 2, [oy, oy + D * s], color=BLK2, lw=1.0)
    ax.plot([ox, ox + KW * s], [oy + 148.5 * s] * 2, color=BLK2, lw=1.0)
    for x in (KW / 2 - 50, KW / 2 + 50):
        ax.add_patch(Rectangle((ox + (x - 6) * s, oy - 0.5 * s), 12 * s, 3 * s, fc=BLK2, ec="none"))

def sheet_fallboard():
    fig = sheet("FALLBOARD · printed · in use: bench, lap, the keyboard range, the lane and pockets, the rear wall",
                "One plane, one lid, all walnut-brown from the spool (ASA or PETG). 412 × 265 × 42; the lid ribbed underneath on a 17.5 grid [r3]. Keyboard against the front wall, a 15 mm lane, the module behind; left pocket = coil + adapter, right = charger. No gutter, no lamp.")
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
    rows = [("carry parts (systems)", f"{cw} kg"), ("module [r2] (r3, speaker E: 0.70–0.85)", "0.67–0.93 kg"), ("kit + nanoKEY2", f"{n_} kg"), ("kit + K-Board C", f"{k_} kg"),
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
    ax.add_patch(Rectangle(P(0, y1), KW * s, SP_S * s, fc=HOUSED, ec=EDGE, lw=0.4, zorder=1))
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
    ax.add_patch(Rectangle((ox, oy + SP_T * s), KW * s, 5 * s, fc=HOUSED, ec=EDGE, lw=0.4))
    for sx in (110, 288): ax.add_patch(Rectangle((ox + sx * s, oy - 2 * s), 14 * s, (SP_T + 9) * s, fc="#121212", ec="none", alpha=0.9))

def spine_elev(ax, ox, oy, s=1.0):
    """The closed box seen on its spine (412 × 59): the two stop beads read as a book's bands."""
    ax.add_patch(FancyBboxPatch((ox, oy), KW * s, 59 * s, boxstyle=f"round,pad=0,rounding_size={4*s}", fc=HOUSED, ec=EDGE, lw=0.6))
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
    ax.add_patch(Rectangle((ox + SP_T * s, oy), SP_S * s, 5 * s, fc=HOUSED, ec="none", zorder=2))
    px, py = ox + (SP_T + SP_S) * s, oy; rot = math.radians(180 - angle)
    R = lambda x, y: (px + (x * math.cos(rot) - y * math.sin(rot)) * s, py + (x * math.sin(rot) + y * math.cos(rot)) * s)
    ax.add_patch(Polygon([R(0, 0), R(SP_T, 0), R(SP_T, 36), R(SP_T - 4, 36), R(SP_T - 4, 5), R(0, 5)], closed=True, fc=BLK, ec="none", zorder=2))
    F = MA["FOOT"]
    ax.add_patch(Polygon([R(34, 1.2), R(139, 1.2), R(139, 36.2), R(34 + F + 5, 36.2), R(34 + F, 26.2), R(38, 26.2), R(38, 36.2), R(34, 36.2)], closed=True, fc=BLKL, ec="none", zorder=2.1))

def stop_detail(ax, ox, oy, s=3.0):
    """Section through the spine's edge at 180°: bead face on tray edge face, below the hinge axis (5 mm)."""
    ax.add_patch(Rectangle((ox - 30 * s, oy), 30 * s, 5 * s, fc=BLK, ec=EDGE, lw=0.5))            # keyboard tray floor edge
    ax.add_patch(Rectangle((ox, oy), 22 * s, 3 * s, fc=HOUSED, ec=EDGE, lw=0.5))               # spine panel
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
        ax.add_patch(Rectangle((0, yy + SP_T), KW, 10, fc=HOUSED, ec="none"))
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
def cloth_plan(ax, ox, oy, kbkey="xkey", s=1.0, cable=True, objects=True, pocket_items=True):
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
    if pocket_items: charger(ax, *P(50, 60), s); adapter(ax, *P(100, 70), s); card(ax, *P(150, 50), s, z=5.1)

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

# =================================================================== YOKE (concept; systems rev 1 mechanism; absorbs CLOTH's wrap and mat)
PIV = [(-80.0, 30.0), (80.0, 30.0)]          # systems' coords: axis x = 0, module front y = 0, keyboard on −y
ARM_L, SLOT0, SLOT1 = 165.0, 105.0, 150.0

def yk_pins(key, pose):
    w = KB[key][1]; rear = 105.0 if pose == "carry" else -15.0
    return [(-(w / 2 + 12), rear), (w / 2 + 12, rear)], rear

def yk_arm(ax, P, piv, pin, z=6):
    (px, py), (qx, qy) = piv, pin
    ang = math.atan2(qy - py, qx - px); c, sn = math.cos(ang), math.sin(ang)
    T_ = lambda u, v: P(px + u * c - v * sn, py + u * sn + v * c)
    ax.add_patch(Polygon([T_(0, -11), T_(ARM_L, -8), T_(ARM_L, 8), T_(0, 11)], closed=True, fc=HOUSE, ec=HOUSED, lw=0.5, zorder=z))
    ax.add_patch(Polygon([T_(10, -2), T_(ARM_L - 4, -2), T_(ARM_L - 4, 2), T_(10, 2)], closed=True, fc=HOUSEL, ec="none", zorder=z + .05))   # rib
    ax.add_patch(Polygon([T_(SLOT0, -2.2), T_(SLOT1, -2.2), T_(SLOT1, 2.2), T_(SLOT0, 2.2)], closed=True, fc=HOUSED, ec="none", zorder=z + .1))
    ax.add_patch(Circle(P(px, py), 15, fc=HOUSE, ec=HOUSED, lw=0.5, zorder=z + .15))
    for i in range(24):   # index ring
        g = 2 * math.pi * i / 24
        ax.plot([P(px + 12 * math.cos(g), 0)[0], P(px + 14.5 * math.cos(g), 0)[0]], [P(0, py + 12 * math.sin(g))[1], P(0, py + 14.5 * math.sin(g))[1]], color=CREAM, lw=0.3, zorder=z + .2)
    ax.add_patch(Circle(P(px, py), 8, fc=SW, ec="none", zorder=z + .25))
    ax.add_patch(Circle(P(qx, qy), 3.5, fc=SW, ec="none", zorder=z + .3))     # M4 thumbscrew at the cup

def yk_cup(ax, P, pin, side, w, z=7):
    qx, qy = pin; end = side * w / 2
    xo = end if side > 0 else end - 4
    ax.add_patch(Rectangle(P(xo, qy - 40), 4, 40, fc=HOUSE, ec=HOUSED, lw=0.4, zorder=z))                  # end wall
    xl = end - 8 if side > 0 else end
    ax.add_patch(Rectangle(P(xl, qy - 40), 8, 40, fc=HOUSEL, ec=HOUSED, lw=0.4, zorder=z + .1))             # lip over the end cap
    lx = end + 4 if side > 0 else end - 12
    ax.add_patch(Rectangle(P(lx, qy - 8), 8, 8, fc=HOUSE, ec=HOUSED, lw=0.4, zorder=z + .1))                # lug to the pin
    nx = end + (0 if side > 0 else -4)
    ax.add_patch(Rectangle(P(nx, qy - 30), 4, 15, fc=HOUSED, ec="none", zorder=z + .2))                     # 15 mm end-socket notch

def yk_plan(ax, ox, oy, key, pose, s=1.0, module_detail=1, xray=False, cap=True, cable=True):
    """ox, oy = where the module's front-left corner sits."""
    P = lambda x, y: (ox + (140 + x) * s, oy + y * s)
    w, d = KB[key][1], KB[key][2]
    pins, rear = yk_pins(key, pose)
    if pose == "play" and cap:
        ax.add_patch(Polygon(hull(MA["D"] + 1.5, ox - 0.75 * s, oy + 47 * s, s), closed=True, fc=HOUSE, ec=HOUSED, lw=0.5, zorder=1))
        ax.text(*P(0, 47 + 112), "cap, rim-down: the module's rear foot", ha="center", fontsize=5.4, color=CREAM, zorder=1.1)
    keyboard(ax, ox + (140 - w / 2) * s, oy + (rear - d) * s, key, s, z=3, label=False)
    zarm = 6 if (pose == "carry") else 1.5
    for i, side in ((0, -1), (1, 1)):
        yk_arm(ax, P, PIV[i], pins[i], z=zarm)
        yk_cup(ax, P, pins[i], side, w, z=zarm + 1)
    if xray:
        ax.add_patch(Polygon(hull(MA["D"], ox, oy, s), closed=True, fc="none", ec=CORAL, lw=1.0, ls=(0, (3, 2)), zorder=9))
    else:
        module_plan(ax, ox, oy, MA, s, detail=module_detail, z=2)
    if pose == "play" and cable:
        sx = 140 - w / 2 + w * 0.7
        ax.plot([ox + sx * s, ox + sx * s, ox + 140 * s, ox + 140 * s], [oy + rear * s, oy - 7 * s, oy - 7 * s, oy], color="#cfcfcf", lw=1.3, zorder=6)

def yk_side(ax, ox, oy, pose, key="xkey", s=1.0):
    """End view (y horizontal, front of the module at left of the module), bench at z 0."""
    w, d, h = KB[key][1], KB[key][2], KB[key][3]
    P = lambda y, z_: (ox + y * s, oy + z_ * s)
    st, run = MA["STAGE"], MA["RUN"]
    def module_at(z0):
        ax.add_patch(Polygon([P(0, z0), P(105, z0), P(105, z0 + 35), P(st + run, z0 + 35), P(st, z0 + 25), P(4, z0 + 25), P(4, z0 + 35), P(0, z0 + 35)], closed=True, fc=HOUSE, ec=HOUSED, lw=0.5, zorder=3))
        ax.add_patch(Rectangle(P(4, z0 + 23), (st - 4) * s, 2 * s, fc=CREAM, ec="none", zorder=3.1))
        for yk in (MA["FY"], MA["RY"]): ax.add_patch(Rectangle(P(yk - 5, z0 + 26), 10 * s, 8 * s, fc=GOLD, ec="none", zorder=3.1))
    if pose == "carry":
        rear = 105.0
        ax.add_patch(Rectangle(P(rear - 40, 0), 40 * s, 3 * s, fc=HOUSE, ec=HOUSED, lw=0.4, zorder=2))           # cup jaw
        ax.add_patch(Rectangle(P(rear - d, 3), d * s, h * s, fc=SILVER, ec="#777", lw=0.3, zorder=2))
        for i in range(14): ax.add_patch(Rectangle(P(rear - d + 6 + i * 9.4, 3 + h), 8 * s, 1.5 * s, fc=KWHITE, ec="#999", lw=0.2, zorder=2))
        ax.add_patch(Rectangle(P(rear - 40, 3 + h + 0.5), 40 * s, 3 * s, fc=HOUSEL, ec=HOUSED, lw=0.3, zorder=2.1))   # lip
        ax.add_patch(Polygon([P(30, 27), P(rear + 4, 27), P(rear + 4, 37), P(30, 37)], closed=True, fc=HOUSEL, ec=HOUSED, lw=0.4, zorder=2.5))   # arm (seen end-on, foreshortened)
        module_at(37)
        ax.add_patch(Polygon([P(-1.5, 35.5), P(-1.5, 74), P(106.5, 74), P(106.5, 35.5), P(105, 35.5), P(105, 72.5), P(0, 72.5), P(0, 35.5)], closed=True, fc=HOUSED, ec="none", zorder=3.3))
        return 74
    rear = -15.0
    ax.add_patch(Rectangle(P(rear - d, 3), d * s, h * s, fc=SILVER, ec="#777", lw=0.3, zorder=2))
    for i in range(14): ax.add_patch(Rectangle(P(rear - d + 6 + i * 9.4, 3 + h), 8 * s, 1.5 * s, fc=KWHITE, ec="#999", lw=0.2, zorder=2))
    ax.add_patch(Rectangle(P(rear - 40, 0), 40 * s, 3 * s, fc=HOUSE, ec=HOUSED, lw=0.4, zorder=2.2))
    ax.add_patch(Polygon([P(rear - 12, 3 + h), P(rear + 2, 3 + h), P(rear + 2, 37), P(rear - 12, 37)], closed=True, fc=HOUSE, ec=HOUSED, lw=0.4, zorder=2.3))   # cup's lug rising to the arm
    ax.add_patch(Polygon([P(rear - 4, 27), P(30, 27), P(30, 37), P(rear - 4, 37)], closed=True, fc=HOUSEL, ec=HOUSED, lw=0.4, zorder=2.5))
    ax.add_patch(Polygon([P(47, 0), P(47 + 105, 0), P(47 + 105, 36.5), P(47, 36.5)], closed=True, fc=HOUSED, ec=HOUSE, lw=0.5, zorder=2.4))   # cap rim-down
    module_at(37)
    return 72

def sheet_yoke():
    fig = sheet("YOKE A · carry and play · the module is the carry; two printed arms hang on its own ¼\"-20 inserts (S4)",
                "Cups at the keyboard's rear corners reach forward along its ends; each arm is clamped at any angle by the module's thumbscrew, so the keyboard is the jig. "
                "Carry: keyboard keys-up under the module, the cap over the panel. Play: arms forward, keyboard in front, the cap becomes the module's rear foot. All walnut-brown, from the spool.")
    ax = axes(fig, [0.015, 0.40, 0.42, 0.52], (-140, 560), (-260, 300))
    bench(ax, -130, -250, 690, 540)
    yk_plan(ax, 120, 0, "xkey", "play", 1.0, module_detail=1)
    ax.text(260, -245, "▲ you", ha="center", fontsize=8, weight="bold", color="#333")
    ax.text(-130, 290, "PLAY · plan · Xkey 25 · on a bench (three points: two cups + the cap)", fontsize=8.5, weight="bold")
    ax.text(-130, 272, "the arms run from the pivots under the module out to the keyboard's rear corners: behind and outside the keys, never over them;\n"
                       "the cable runs 15 mm from the keyboard's rear socket to the recessed host pocket", fontsize=6.0, va="top", color="#333")
    ax = axes(fig, [0.45, 0.40, 0.28, 0.52], (-90, 470), (-120, 330))
    yk_plan(ax, 50, 40, "xkey", "carry", 1.0, xray=True)
    ax.text(-90, 318, "CARRY · plan · Xkey 25 · X-ray (dashed coral = the module above)", fontsize=8.5, weight="bold")
    ax.text(-90, 300, "keyboard keys-up under the module, rear edge under the module's rear; arms ≈ 31° back;\n≥ 9 mm of air from the keys to the arms' ribs (nothing touches a key); ≈ 395 wide whatever the keyboard", fontsize=6.0, va="top", color="#333")
    ax = axes(fig, [0.75, 0.66, 0.24, 0.26], (-60, 190), (-20, 110))
    ax.add_patch(Rectangle((-60, -4), 250, 4, fc="#d9d0c2", ec="none"))
    t = yk_side(ax, 40, 0, "carry")
    ax.annotate("", xy=(170, 0), xytext=(170, t), arrowprops=dict(arrowstyle="<->", lw=0.6, color=CORAL, shrinkA=0, shrinkB=0))
    ax.text(174, t / 2, f"≈ {t}", fontsize=7, color=CORAL, va="center")
    ax.text(-60, 106, "CARRY · end view", fontsize=8.5, weight="bold")
    ax.text(-60, 96, "jaw 3 · keyboard 11–16 · air ≥ 9 · arm 27–37 · module 37–72 · cap to 74", fontsize=5.8, va="top")
    ax = axes(fig, [0.75, 0.40, 0.24, 0.24], (-170, 170), (-20, 110))
    ax.add_patch(Rectangle((-170, -4), 340, 4, fc=SLAT, ec="none"))
    yk_side(ax, 0, 0, "play")
    ax.text(-170, 106, "PLAY · end view", fontsize=8.5, weight="bold")
    ax.text(-170, 96, "keyboard on the bench, ends on the jaws · module level at 37 on\nthe arms in front and the cap (36.5) behind · no tilt, no shade", fontsize=5.8, va="top")
    # cup and arm detail
    ax = axes(fig, [0.015, 0.04, 0.42, 0.32], (-30, 330), (-80, 120))
    P = lambda x, y: (x, y)
    yk_arm(ax, lambda x, y: (x + 20, y + 20), (0, 0), (ARM_L - 30, 0), z=2)
    ax.text(-30, 112, "ONE ARM AND CUP (mirror pair) · ≈ 165 long, T-section 22 wide × 10 tall, 45 mm slot, fits a 220 bed", fontsize=8.5, weight="bold")
    ax.text(-30, 96, "pivot disc Ø 30 under the module's thumbscrew, with a cream index ring so both arms sit at equal angles · rib on top · slot near the tip · "
                     "\none M4 thumbscrew locks the cup's reach and swivel · printed clips on the ribs: left = cable coil, right = C-to-A adapter", fontsize=5.8, va="top")
    # cup section
    cx, cy, k = 190, -55, 2.2
    ax.add_patch(Rectangle((cx, cy), 30 * k, 3 * k, fc=HOUSE, ec=HOUSED, lw=0.5))
    ax.add_patch(Rectangle((cx + 30 * k, cy), 3 * k, 27 * k, fc=HOUSE, ec=HOUSED, lw=0.5))
    ax.add_patch(Rectangle((cx + 22 * k, cy + 24 * k), 11 * k, 3 * k, fc=HOUSE, ec=HOUSED, lw=0.5))
    ax.add_patch(Rectangle((cx, cy + 3 * k), 30 * k, 5 * k * 0.6, fc="#3a3836", ec="none"))
    ax.add_patch(Rectangle((cx + 22 * k, cy + 21 * k), 8 * k, 3 * k * 0.9, fc="#3a3836", ec="none"))
    ax.add_patch(Rectangle((cx + 2 * k, cy + 6 * k), 27 * k, 14 * k, fc=SILVER, ec="#777", lw=0.3))
    ax.text(cx, cy - 8, "the cup, section at 2.2 : 1: lower jaw 30 under the keyboard, end wall, lip ≤ 8 over the end cap,\n5 mm closed-cell foam on both jaws: grips 11–16 of thickness, never the end's shape", fontsize=5.6, va="top")
    # comparison table
    ax = fig.add_axes([0.45, 0.04, 0.54, 0.32]); ax.axis("off")
    ax.text(0, 1.0, "HOW THE THREE CONCEPTS COMPARE (systems' numbers; the module 0.70–0.85 kg with speaker E [r3])", fontsize=8.5, weight="bold", va="top", transform=ax.transAxes)
    hdr = ["", "YOKE", "FALLBOARD", "SPINE"]
    rws = [["kind", "no case: attachment point", "open frame + lid", "closed box"],
           ["carry parts", "0.14–0.20 kg (+ wrap 0.23–0.36)", "0.47–0.60", "0.42–0.52"],
           ["carried (Xkey)", "395 × 135 × 74 ≈ 3.9 L", "412 × 265 × 42 ≈ 4.6 L", "412 × 148 × 59 ≈ 3.6 L"],
           ["keys protected by", "the module, 9 mm above", "lid", "module tray"],
           ["panel protected by", "the cap", "lid", "keyboard tray"],
           ["charger", "loose (or the wrap's pocket)", "right pocket", "right bay"],
           ["lap", "one piece (cap pegged in)", "one board", "flat, stopped"],
           ["family reuse", "any module with S4", "bed, blocks, lid", "trays, spine"]]
    cols = [0.0, 0.20, 0.52, 0.76]
    for j, h in enumerate(hdr): ax.text(cols[j], 0.88, h, fontsize=7.4, weight="bold", transform=ax.transAxes, va="top")
    for i, r in enumerate(rws):
        for j, c in enumerate(r): ax.text(cols[j], 0.79 - i * 0.095, c, fontsize=6.6, transform=ax.transAxes, va="top", color="#222" if j else "#555")
    fig.savefig("../yoke/yoke-A-carry-and-play.png", facecolor=BG)

def yk_bundle(ax, ox, oy, s=1.0, label=True):
    ax.add_patch(FancyBboxPatch((ox, oy), 425 * s, 165 * s, boxstyle=f"round,pad=0,rounding_size={34*s}", fc=CLOTH, ec=CLOTHE, lw=0.8))
    ax.add_patch(Ellipse((ox + 212 * s, oy + 165 * s), 95 * s, 52 * s, fc=CLOTH, ec=CLOTHE, lw=0.6))
    for i in range(1, 4): ax.plot([ox + (i * 106) * s] * 2, [oy + 8 * s, oy + 157 * s], color="#2d2a28", lw=0.5)
    if label: ax.text(ox + 212 * s, oy + 80 * s, "YOKE wrapped (Xkey) ≈ 425 × 165 × 95 [est]", ha="center", fontsize=6.2, color=THREAD)

def sheet_yoke_b():
    fig = sheet("YOKE B · the wrap (CLOTH's square, now YOKE's option): wrapped, on the grass as the mat, in a pack",
                "The near-black coated quilted square, cream thread, liner-up when spread. Wrapped, it covers the keyboard's open edges and its pocket holds the charger. "
                "On the grass it's the mat you sit on, the yoked instrument on the stitched outline. Without the wrap, YOKE is the module, the cap and the arms.")
    # grass plan
    ax = axes(fig, [0.015, 0.36, 0.40, 0.56], (-150, 1000), (-150, 1000))
    ax.add_patch(Rectangle((-150, -150), 1150, 1150, fc=GRASS, ec="none"))
    import random
    rnd = random.Random(7)
    for _ in range(500):
        x, y = rnd.uniform(-150, 1000), rnd.uniform(-150, 1000); ax.plot([x, x + rnd.uniform(-4, 4)], [y, y + 10], color=GRASSD, lw=0.5)
    cloth_plan(ax, 50, 50, "xkey", 1.0, objects=False, pocket_items=False)
    yk_plan(ax, 50 + (CS / 2 - 140), 50 + OUT_Y + 154, "xkey", "play", 1.0, module_detail=1)
    person_seated(ax, 450, 100)
    ax.text(-140, 975, "ON THE GRASS · plan · the park pose", fontsize=8.5, weight="bold")
    ax.text(-140, 945, "the wrap spread liner-up (coated face to the damp); the yoked instrument on the stitched outline, cap behind the module;\n"
                       "you sit cross-legged on the 435 mm of near cloth; the pocket (charger, card) by your left hip", fontsize=6.2, color="#222", va="top")
    # grass side
    ax = axes(fig, [0.43, 0.70, 0.27, 0.22], (-80, 900), (-30, 640))
    ax.add_patch(Rectangle((-80, -30), 980, 30, fc=GRASS, ec="none"))
    ax.add_patch(Rectangle((0, 0), 800, 4, fc=CLOTH, ec="none"))
    sub_ox = 600
    ax.add_patch(Rectangle((sub_ox - 15 - 135, 4), 135, 19, fc=SILVER, ec="#777", lw=0.3))
    ax.add_patch(Polygon([(sub_ox, 41), (sub_ox + 105, 41), (sub_ox + 105, 76), (sub_ox + 46, 76), (sub_ox + 41, 66), (sub_ox, 66)], fc=HOUSE, ec="none"))
    ax.add_patch(Rectangle((sub_ox + 47, 4), 105, 36.5, fc=HOUSED, ec="none"))
    for k in range(3): ax.add_patch(Ellipse((sub_ox + 73, 86 + 18 * k), 30 + 16 * k, 6 + 3 * k, fc="none", ec=AMBER, lw=0.6))
    ax.add_patch(Ellipse((160, 60), 260, 110, fc=PERSON, ec="none"))
    ax.add_patch(Polygon([(80, 70), (230, 70), (330, 360), (220, 400)], fc="#a8957e", ec="none"))
    ax.add_patch(Circle((300, 440), 55, fc="#6d5c4a", ec="none"))
    ax.plot([300, 400, 480], [330, 160, 30], color="#a8957e", lw=5, solid_capstyle="round")
    ax.text(-80, 635, "ON THE GRASS · side", fontsize=8.5, weight="bold")
    ax.text(-80, 605, "both drivers fire up through the roof's grilles, so grass and cloth don't muffle them", fontsize=6.2, va="top")
    # wrapped bundle
    ax = axes(fig, [0.72, 0.70, 0.27, 0.22], (-20, 470), (-40, 230))
    yk_bundle(ax, 10, 10)
    ax.text(-20, 222, "WRAPPED · knotted bundle", fontsize=8.5, weight="bold")
    ax.text(-20, -10, "carry stack 395 × 135 × 74 inside the quilt; the knot is the handle", fontsize=6.2, va="top")
    # pack
    ax = axes(fig, [0.43, 0.36, 0.30, 0.32], (-30, 1000), (-60, 560))
    backpack(ax, 0, 0)
    ax.add_patch(Rectangle((150 - 67.5, 6), 135, 395, fc=HOUSE, ec=HOUSED, lw=0.5))
    ax.annotate("", xy=(0, 300), xytext=(82.5, 300), arrowprops=dict(arrowstyle="<->", lw=0.6, color=CORAL, shrinkA=0, shrinkB=0))
    ax.text(41, 308, "82.5 a side", ha="center", fontsize=6.0, color=CORAL)
    ax.text(150, -30, "bare: 395 × 135 × 74\n165 mm spare across", ha="center", fontsize=6.2, va="top")
    backpack(ax, 340, 0, label=False)
    ax.add_patch(FancyBboxPatch((340 + 150 - 82.5, 6), 165, 425, boxstyle="round,pad=0,rounding_size=30", fc=CLOTH, ec=CLOTHE, lw=0.5))
    ax.text(490, -30, "wrapped: ≈ 425 × 165 × 95 [est]\n135 mm spare across", ha="center", fontsize=6.2, va="top")
    backpack(ax, 680, 0, label=False)
    ax.add_patch(Rectangle((680 + 150 - 54, 6), 108, 283, fc=HOUSE, ec=HOUSED, lw=0.5))
    ax.text(830, 330, "module + cap,\nno keyboard:\n283 × 108 × 37", ha="center", fontsize=6.0)
    ax.text(830, -30, "keyboard missing:\narms off, the smallest bundle", ha="center", fontsize=6.2, va="top")
    ax.text(-30, 548, "IN A PACK · same 300 × 450 outline (illustrative) · standing on edge", fontsize=8.5, weight="bold")
    # weights
    ax = fig.add_axes([0.75, 0.38, 0.24, 0.28]); ax.axis("off")
    rows = [("carry parts (arms, cups, cap)", "0.14–0.20 kg"), ("+ the wrap (option)", "0.23–0.36 kg"), ("module, speaker E [r3]", "0.70–0.85 kg"),
            ("kit + nanoKEY2", "1.12–1.33 kg"), ("kit + K-Board C", "1.22–1.43 kg"), ("kit + Xkey 25", "1.48–1.69 kg"), ("for scale: 16-inch laptop", "≈ 2.1 kg")]
    ax.text(0, 1.0, "WEIGHT (systems; lighter is better, no target)", fontsize=8.4, weight="bold", va="top", transform=ax.transAxes)
    for i, (a_, b_) in enumerate(rows):
        ax.text(0.0, 0.86 - i * 0.12, a_, fontsize=7.0, va="top", transform=ax.transAxes)
        ax.text(0.66, 0.86 - i * 0.12, b_, fontsize=7.0, va="top", weight="bold" if "kit" in a_ else None, transform=ax.transAxes)
    ax.text(0, 0.0, "the wrap adds weight; bare YOKE is still the lightest kit", fontsize=6.2, color="#444", transform=ax.transAxes)
    # wrap steps
    def f1(a):
        a.set_xlim(-70, 350); a.set_ylim(-50, 140); yk_plan(a, 0, 0, "xkey", "carry", 1.0, xray=False, module_detail=0)
        a.add_patch(Polygon(hull(MA["D"] + 3, -1.5, -1.5, 1.0), closed=True, fc=HOUSED, ec=HOUSE, lw=0.5, zorder=12))
        a.text(140, 50, "cap on", ha="center", fontsize=6.4, color=CREAM, zorder=13)
    def f2(a):
        a.set_xlim(-10, 810); a.set_ylim(-10, 810); cloth_plan(a, 0, 0, "xkey", 1.0, objects=False, pocket_items=True)
        a.add_patch(Rectangle((202, 330), 395, 135, fc=HOUSE, ec=HOUSED, zorder=4)); a.text(400, 397, "yoked stack, cap up", ha="center", fontsize=6.4, color=CREAM, zorder=5)
    def f3(a):
        a.set_xlim(-10, 810); a.set_ylim(-10, 810); a.add_patch(Polygon([(400, 0), (800, 400), (400, 800), (0, 400)], fc=CLOTH))
        a.add_patch(FancyBboxPatch((202, 330), 395, 135, boxstyle="round,pad=0,rounding_size=4", fc="#2f2c29", ec=CLOTHE, zorder=4))
    def f4(a): a.set_xlim(-10, 450); a.set_ylim(-60, 250); yk_bundle(a, 0, 0, label=False)
    packing_strip(fig, [0.015, 0.03, 0.97, 0.30], [
        (f1, "Pack the yoke as on sheet A: keyboard under, arms back, cable and adapter on the arms' clips, cap on."),
        (f2, "Charger and card into the wrap's pocket. Set the stack on the cloth's centre, liner side up."),
        (f3, "Fold two opposite corners over (coated face out)."),
        (f4, "Tie the other two into the knot handle (hem weights inside). Into the pack.")],
        "WRAPPING (the option; unwrap is the reverse and ends with the mat spread)")
    fig.savefig("../yoke/yoke-B-wrap-grass-pack.png", facecolor=BG)

if __name__ == "__main__":
    which = sys.argv[1:] or ["module", "fallboard", "spine", "yoke"]
    if "module" in which: sheet_module()
    if "fallboard" in which:
        sheet_fallboard()
        closed_sheet("FALLBOARD", "FALLBOARD · closed and packing: size, weight, pack-up order",
                     "Closed it's one walnut-brown board, about a 15-inch laptop's footprint and 2½ laptops thick. The lid's marks are its ribs (17.5 grid, seen as a faint relief) and the seam cross; the name is on the module inside.",
                     lambda ax, x, y: fb_closed(ax, x, y), (KW, FB_D), 42, "48 · 412 × 272", fb_frames(), "PACKING (unpack is the reverse)")
    if "spine" in which:
        sheet_spine()
        closed_sheet("SPINE", "SPINE · closed and packing: size, weight, pack-up order",
                     "Closed it's a walnut-brown box like a thick hardback, a little wider than the keyboard: the smallest rigid enclosing kit.",
                     lambda ax, x, y: spine_closed(ax, x, y), (KW, 148), 59, "66", sp_frames(), "PACKING (unpack is the reverse)")
    if "yoke" in which:
        sheet_yoke(); sheet_yoke_b()
