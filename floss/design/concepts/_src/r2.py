"""floss concept round 2 (visual): one module, three carries. Rough 2-D drawings to scale (mm).
Plan coordinates: x right, y away from the player, origin at the module's front-left (or the kit's front-left).
Run from this folder:  python3 r2.py [module fallboard spine cloth]   (not with -I: nothing imported locally, but keep the habit)
Outputs go to ../module/, ../fallboard/, ../spine/, ../cloth/.
"""
import math, sys, textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Rectangle, FancyBboxPatch, Ellipse, Arc
plt.rcParams["font.family"] = "Inter"

BG = "#f6f2ea"; INK = "#1d1b19"; GREY = "#8a8276"; CORAL = "#ef7f68"; BRASS = "#c9a24a"; BRASSD = "#8a6d27"
SHELL = "#5b3a24"; SHELLD = "#432a19"; CREAM = "#f1ebdd"; CREAMD = "#e2d8c3"; CROWN = "#e8dcc2"
WAL = "#6b4429"; WALD = "#4a2e1b"; BED = "#2e2622"; GUT = "#1f1916"; FOAM = "#5a524c"
CLOTHC = "#3f4a47"; CLOTHL = "#56625e"; THREAD = "#e7dcc0"; SKIN = "#cdbca5"; SLAT = "#a88b6a"
SILVER = "#c8c8c6"; KWHITE = "#ecebe7"; LAPTOP = "#9aa0a6"; BOOK = "#7d8a8f"

# ------------------------------------------------------------------ the module: geometry
U = 35.0                              # the module unit: 35 mm
MW, MD = 8 * U, 3 * U                 # 280 × 105: 8 : 3 (an octave and a fourth); each half 140 × 105 = 4 : 3 (a fourth)
MEND = 2 * U                          # ends 70: centre : end = 3 : 2 (a fifth)
SAG = MD - MEND
R_ARC = ((MW / 2) ** 2 + SAG ** 2) / (2 * SAG)   # rear arc radius ≈ 374
ARC_CY = MD - R_ARC
H_RIM, H_DECK = 1 * U, 26.0           # rim / crown top 35 (length : height = 8 : 1, three octaves); sunk deck 26, knob tops 34
CROWN_X0, CROWN_X1 = MW / 2 - U, MW / 2 + U   # speaker crown 70 wide (2 units), on the axis
RAKE0, RAKE1 = 47.0, 55.0             # crown's raked front face (nameboard), foot → top
FRONT_Y, REAR_Y = 16.0, 40.0
SH = -8.5                             # systems' x map (297 wide, 16.5 margins) moved to 280 wide, 8 mm margins
FRETS = [f + SH for f in (54, 83, 134, 163, 214, 243)]

def rear_y(x):
    return ARC_CY + math.sqrt(R_ARC ** 2 - (x - MW / 2) ** 2)

def hull_pts(ox=0, oy=0, s=1.0, n=60, rf=10.0):
    """Plan outline: straight front, straight ends 70 deep, a fair rear arc to 105 on the axis; front corners r 10."""
    pts = []
    for k in range(9):                       # front-left corner
        a = math.radians(180 + 90 * k / 8); pts.append((rf + rf * math.cos(a), rf + rf * math.sin(a)))
    for k in range(9):                       # front-right corner
        a = math.radians(270 + 90 * k / 8); pts.append((MW - rf + rf * math.cos(a), rf + rf * math.sin(a)))
    pts.append((MW, MEND - 6))
    for k in range(n + 1):                   # rear arc, right to left, with a soft blend at each end
        x = MW - MW * k / n
        y = rear_y(x)
        pts.append((x, y))
    pts.append((0, MEND - 6))
    return [(ox + x * s, oy + y * s) for x, y in pts]

# controls (systems' map, concepts/module/how-it-works.md §3)
FRONT = [("octave", 25.0, "oct"), ("hold", 60.0, "hold"), ("attack", 89.0, "pot"), ("tone", 111.0, "pot"),
         ("depth", 140.0, "coral"), ("echo", 169.0, "pot"), ("tap", 191.0, "tap"), ("volume", 220.0, "pot"), ("octave", 255.0, "oct")]
REAR = [("tabs", 25.0, "tabs"), ("pressure", 60.0, "kind"), ("release", 89.0, "pot"), ("drift", 111.0, "pot"),
        ("shimmer", 140.0, "kind"), ("time", 169.0, "pot"), ("free·sync", 191.0, "tog"), ("reverb", 220.0, "pot"), ("tabs", 255.0, "tabs")]

def module_plan(ax, ox, oy, s=1.0, detail=2, target=None, z=1):
    """detail 0: outline + crown only; 1: + knobs; 2: + labels, frets, grille (for 1:1 and large views)."""
    P = lambda x, y: (ox + x * s, oy + y * s)
    ax.add_patch(Polygon(hull_pts(ox, oy, s), closed=True, fc=SHELL, ec=SHELLD, lw=0.6 if s < 1 else 0.8, zorder=z))
    # deck (sunk): inset 4 mm from the outline
    deck = []
    for x, y in hull_pts(0, 0, 1.0):
        cx, cy = MW / 2, MD * 0.45
        dx, dy = x - cx, y - cy
        L = math.hypot(dx, dy)
        deck.append(P(x - 4 * dx / L * (1 if abs(dy) < 1e9 else 1), y - 4 * dy / L))
    # simpler, robust inset: rebuild with a smaller outline
    deck = [P(4 + (x) * (MW - 8) / MW, 4 + y * (MD - 8) / MD) for x, y in hull_pts(0, 0, 1.0)]
    ax.add_patch(Polygon(deck, closed=True, fc=CREAM, ec=CREAMD, lw=0.4, zorder=z + 0.1))
    # crown: raked face + flat top following the rear arc
    top = [(x, rear_y(x) - 4) for x in [CROWN_X1 - i * (CROWN_X1 - CROWN_X0) / 20 for i in range(21)]]
    crown = [P(CROWN_X0, RAKE0), P(CROWN_X1, RAKE0)] + [P(x, y) for x, y in top]
    ax.add_patch(Polygon(crown, closed=True, fc=CROWN, ec=CREAMD, lw=0.5, zorder=z + 0.2))
    ax.add_patch(Polygon([P(CROWN_X0, RAKE0), P(CROWN_X1, RAKE0), P(CROWN_X1, RAKE1), P(CROWN_X0, RAKE1)], closed=True,
                         fc="#d8cbb0", ec="none", zorder=z + 0.25))   # the rake, seen from above
    if detail >= 1:
        # grille over the driver (Ø 46 field of Ø 1.8 holes at 2.6 pitch ≈ 245 holes ≈ 620 mm² open)
        gx, gy = MW / 2, 78.0
        if detail >= 2:
            p = 2.6
            for i in range(-9, 10):
                for j in range(-9, 10):
                    hx, hy = gx + i * p, gy + j * p
                    if (hx - gx) ** 2 + (hy - gy) ** 2 <= 21.5 ** 2:
                        ax.add_patch(Circle(P(hx, hy), 0.9 * s, fc="#b9ab90", ec="none", zorder=z + 0.3))
        else:
            ax.add_patch(Circle(P(gx, gy), 23 * s, fc="#cdbf9f", ec="none", zorder=z + 0.3))
        # wordmark on the crown top, centred above the shimmer column
        if detail >= 2:
            ax.text(*P(MW / 2, 60.5), "floss", ha="center", va="center", fontsize=9 * s, style="italic", color=SHELLD, zorder=z + 0.4, clip_on=True)
        # frets (raised brass, 1 mm), front rim to the crown's foot
        if detail >= 2:
            for fx in FRETS:
                ax.add_patch(Rectangle(P(fx - 0.6, 5), 1.2 * s, (RAKE0 - 6) * s, fc=BRASS, ec="none", zorder=z + 0.3))
        for name, x, k in FRONT:
            knob(ax, P(x, FRONT_Y), k, s, z + 0.5)
        for name, x, k in REAR:
            knob(ax, P(x, REAR_Y), k, s, z + 0.5)
        if detail >= 2:
            fs = 4.6 * s
            for name, x, k in FRONT:
                ax.text(*P(x, FRONT_Y + 10.2), name, ha="center", va="center", fontsize=fs, color=INK, zorder=z + 0.6, clip_on=True)
            for name, x, k in REAR:
                if k == "tabs":
                    for j, t in enumerate(["low", "main", "high"]):
                        ax.text(*P(x - 10 + 10 * j, REAR_Y), t, ha="center", va="center", fontsize=fs * 0.62, color=INK, zorder=z + 0.7, clip_on=True)
                    continue
                ax.text(*P(x, 51.0 if not (CROWN_X0 <= x <= CROWN_X1) else 51.0), name, ha="center", va="center",
                        fontsize=fs, color=INK, zorder=z + 0.6, clip_on=True)
        # front rim: brass target rail (graduated), target rider
        ax.add_patch(Rectangle(P(MW / 2 - 132, 0.8), 264 * s, 2.0 * s, fc=BRASS, ec="none", zorder=z + 0.4))
        if detail >= 2:
            for t in range(-130, 131, 10):
                ax.plot([ox + (MW / 2 + t) * s] * 2, [oy + 0.8 * s, oy + (2.8 if t == 0 else 2.0) * s], color=BRASSD, lw=0.3, zorder=z + 0.45)
        tx = MW / 2 - 18 if target is None else target
        ax.add_patch(Polygon([P(tx - 3.5, 3.6), P(tx + 3.5, 3.6), P(tx, -1.2)], closed=True, fc=BRASS, ec=BRASSD, lw=0.4, zorder=z + 0.5))

def knob(ax, c, k, s, z):
    x, y = c
    if k in ("pot", "oct", "coral"):
        r = 7.45 * s
        ax.add_patch(Circle((x, y), r, fc=CORAL if k == "coral" else INK, ec="none", zorder=z))
        ax.plot([x, x], [y, y + r * 0.8], color="white", lw=0.8 * max(s, 0.4), zorder=z + 0.1)
        if k == "oct":   # stepped: detent ticks only
            for a in range(-2, 3):
                ang = math.radians(90 + a * 30)
                ax.plot([x + (r + 0.9 * s) * math.cos(ang), x + (r + 2.0 * s) * math.cos(ang)],
                        [y + (r + 0.9 * s) * math.sin(ang), y + (r + 2.0 * s) * math.sin(ang)], color=INK, lw=0.35 * max(s, 0.5), zorder=z)
    elif k == "kind":
        r = 5.0 * s
        ax.add_patch(Circle((x, y), r, fc=INK, ec="none", zorder=z))
        ax.plot([x, x], [y, y + r * 0.8], color="white", lw=0.7 * max(s, 0.4), zorder=z + 0.1)
    elif k == "hold":
        ax.add_patch(Circle((x, y), 7.0 * s, fc=BRASS, ec=BRASSD, lw=0.5, zorder=z))
        ax.add_patch(Circle((x, y), 4.3 * s, fc="#dcbb63", ec="none", zorder=z + 0.1))
    elif k == "tap":
        ax.add_patch(Circle((x, y), 6.6 * s, fc="#86cf86", ec="none", zorder=z))
        ax.add_patch(Circle((x, y), 5.2 * s, fc=INK, ec="none", zorder=z + 0.1))
    elif k == "tog":
        ax.add_patch(Rectangle((x - 3 * s, y - 5 * s), 6 * s, 10 * s, fc="#bdbdbd", ec="#777", lw=0.4, zorder=z))
        ax.add_patch(Rectangle((x - 1 * s, y), 2 * s, 6 * s, fc="#555", ec="none", zorder=z + 0.1))
    elif k == "tabs":
        for j in range(3):
            ax.add_patch(FancyBboxPatch((x - 15 * s + 10 * j * s, y - 7.5 * s), 9.0 * s, 15 * s,
                                        boxstyle=f"round,pad=0,rounding_size={1.5*s}", fc="#fbf7ee", ec=GREY, lw=0.4, zorder=z))

# ------------------------------------------------------------------ keyboards, objects, people
KB = {"nano": ("Korg nanoKEY2", 325, 83, 16, "#202020", ("#202020", "#4a4a4a"), "smallest"),
      "kbc":  ("KMI K-Board C", 325, 84, 11, "#f1f1ef", ("#e4e4e1", "#cdcdca"), "smallest"),
      "xkey": ("CME Xkey 25", 388, 135, 16, SILVER, (KWHITE, INK), "largest"),
      "mpk":  ("Akai MPK Mini IV", 348, 192, 46, "#3a3a3a", (KWHITE, INK), "chunky")}

def keyboard(ax, x, y, key, s=1.0, z=3, label=True):
    name, w, d, h, col, keys, _ = KB[key]
    ax.add_patch(FancyBboxPatch((x, y), w * s, d * s, boxstyle=f"round,pad=0,rounding_size={4*s}", fc=col, ec="#666", lw=0.4, zorder=z))
    nwhite = 15; kw = (w - 30) / nwhite; k0 = x + 15 * s
    keyd = min(d * 0.68, 85)
    if key == "mpk": keyd = 80
    for i in range(nwhite):
        ax.add_patch(Rectangle((k0 + i * kw * s, y + 4 * s), kw * s, keyd * s, fc=keys[0], ec="#888", lw=0.3, zorder=z + 0.1))
    for i in [0, 1, 3, 4, 5, 7, 8, 10, 11, 12]:
        ax.add_patch(Rectangle((k0 + ((i + 1) * kw - kw * 0.3) * s, y + (4 + keyd * 0.38) * s), kw * 0.6 * s, keyd * 0.62 * s, fc=keys[1], ec="none", zorder=z + 0.2))
    if key == "mpk":
        for i in range(8):
            ax.add_patch(Rectangle((x + (60 + i * 30) * s, y + 115 * s), 24 * s, 24 * s, fc="#666", ec="none", zorder=z + 0.2))
    if label:
        ax.text(x + w * s / 2, y + (d - 6) * s, f"{name} · {w} × {d} × {h}", ha="center", va="top", fontsize=max(4.0, 5.2 * s), color="#888", zorder=z + 0.3, clip_on=True)
    return k0, kw

def bc_x(x, key, s=1.0):
    name, w, d, h, col, keys, _ = KB[key]; kw = (w - 30) / 15
    return x + (15 + 7 * kw) * s

def thighs(ax, x, y, s=1.0, z=0):
    """Top view of a seated lap: body at the top (rear), knees toward the player? No: the player sits at the BOTTOM of the page,
    facing up; so thighs run from the bottom edge (hips) upward (knees)."""
    for cx in (x + 85 * s, x + 255 * s):
        ax.add_patch(FancyBboxPatch((cx - 75 * s, y), 150 * s, 430 * s, boxstyle=f"round,pad=0,rounding_size={60*s}", fc=SKIN, ec="none", zorder=z))
    ax.add_patch(Ellipse((x + 170 * s, y - 30 * s), 420 * s, 140 * s, fc="#b9a68c", ec="none", zorder=z))

def bench(ax, x, y, w, d, s=1.0, z=0):
    n = 4; sw = d / n
    for i in range(n):
        ax.add_patch(Rectangle((x, y + i * sw * s), w * s, (sw - 8) * s, fc=SLAT, ec="#8d7254", lw=0.5, zorder=z))

def laptop(ax, x, y, s=1.0, z=1):
    ax.add_patch(FancyBboxPatch((x, y), 356 * s, 248 * s, boxstyle=f"round,pad=0,rounding_size={8*s}", fc=LAPTOP, ec="#7d838a", lw=0.5, zorder=z))
    ax.text(x + 178 * s, y + 124 * s, "16-inch laptop\n≈ 356 × 248 × 17\n≈ 2.1 kg", ha="center", va="center", fontsize=6.2, color="white", zorder=z + 0.1)

def book(ax, x, y, s=1.0, z=1):
    ax.add_patch(Rectangle((x, y), 156 * s, 234 * s, fc=BOOK, ec="#677379", lw=0.5, zorder=z))
    ax.text(x + 78 * s, y + 117 * s, "hardback\n≈ 156 × 234 × 35\n≈ 0.6 kg", ha="center", va="center", fontsize=6.0, color="white", zorder=z + 0.1)

def backpack(ax, x, y, s=1.0, z=0):
    ax.add_patch(FancyBboxPatch((x, y), 300 * s, 450 * s, boxstyle=f"round,pad=0,rounding_size={40*s}", fc="none", ec="#6d7f8a", lw=0.9, ls=(0, (5, 3)), zorder=z))
    ax.text(x + 150 * s, y + 462 * s, "a 20–25 L daypack's main compartment ≈ 300 × 450 (illustrative, not a product)", ha="center", fontsize=5.6, color="#6d7f8a")

def sheet(title, sub, foot):
    fig = plt.figure(figsize=(16.54, 11.69), dpi=150); fig.patch.set_facecolor(BG)
    fig.text(0.025, 0.968, title, fontsize=13, weight="bold")
    fig.text(0.025, 0.945, sub, fontsize=9, color="#444")
    fig.text(0.025, 0.010, foot, fontsize=6.6, color=GREY)
    return fig

def axes(fig, rect, xl, yl):
    ax = fig.add_axes(rect); ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(*xl); ax.set_ylim(*yl); return ax

def notes(ax, rows, x0=0.0, x1=0.24, width=95, fs=7.3, step=None, top=0.98):
    y = top
    for h, b in rows:
        ax.text(x0, y, h, fontsize=fs + 1.0, weight="bold", va="top", transform=ax.transAxes)
        wrapped = textwrap.fill(b, width)
        ax.text(x1, y, wrapped, fontsize=fs, va="top", transform=ax.transAxes, color="#333")
        y -= step if step else (0.05 + 0.034 * wrapped.count("\n"))

FOOT = "floss · concept round 2 · visual · rough 2-D drawing to scale, not a render · draws: 'Change instrument roles' + organ stops (jam), 'a ship hull in plan' + 'Go slowly all the way round the outside' (outline)"

# =================================================================== MODULE at 1:1 (A3 landscape, print at 100 %)
def sheet_module():
    fig = plt.figure(figsize=(420 / 25.4, 297 / 25.4), dpi=150); fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 420); ax.set_ylim(0, 297); ax.set_aspect("equal"); ax.axis("off")
    T = lambda x, y, t, **k: ax.text(x, y, t, **k)
    T(12, 287, "floss module · 1 : 1 on A3 (print at 100 %) · plan, front, rear, section on the axis · 280 × 105 × 35", fontsize=11, weight="bold")
    T(12, 281.5, "280 × 105 × 35 = 8 : 3 : 1 in one 35 mm unit, a hull plan with ends 70 deep (2 units). Walnut-brown printed shell, cream deck sunk 9 mm, brass frets and rail, one coral (DEPTH), speaker crown on the axis.", fontsize=6.8, color="#444")
    # 50 mm scale bar
    ax.add_patch(Rectangle((330, 268), 50, 1.4, fc=INK)); T(330, 271, "0", fontsize=5); T(372, 271, "50 mm", fontsize=5)
    for t in range(0, 51, 10): ax.plot([330 + t] * 2, [268, 270], color=INK, lw=0.4)
    T(330, 263, "check: this bar measures 50 mm when printed at 100 %", fontsize=4.4, color=GREY)
    # ---- plan
    PX, PY = 14, 152
    module_plan(ax, PX, PY, 1.0, detail=2, target=PX + 0 + MW / 2 - 18 - PX + PX - PX + 0)
    T(PX, PY + 112, "PLAN (from above) · player at the bottom", fontsize=6.2, weight="bold")
    # envelope and the two √2 halves
    ax.add_patch(Rectangle((PX, PY), MW, MD, fc="none", ec=GREY, lw=0.35, ls=(0, (3, 2)), zorder=0.5))
    ax.plot([PX + MW / 2] * 2, [PY - 6, PY + MD + 4], color=GREY, lw=0.35, ls=(0, (1, 1.5)), zorder=5)
    T(PX + MW / 2, PY - 9, "axis · 140", fontsize=4.8, ha="center", color=GREY)
    T(PX + MW + 2, PY + MD - 2, "105", fontsize=5, color=GREY); T(PX + MW + 2, PY + MEND - 3, "70 (3 : 2)", fontsize=5, color=GREY)
    T(PX + 2, PY + MD + 2, "dashed: the 8 : 3 envelope = two 4 : 3 halves (a fourth each), one per half of the keyboard; grid = 35 mm units", fontsize=4.8, color=GREY)
    for k in range(1, 8): ax.plot([PX + k * U] * 2, [PY, PY + MD], color=GREY, lw=0.2, ls=(0, (1, 3)), zorder=0.6)
    for k in range(1, 3): ax.plot([PX, PX + MW], [PY + k * U] * 2, color=GREY, lw=0.2, ls=(0, (1, 3)), zorder=0.6)
    # inserts (underside), dashed
    for ix in (68.5 + SH, 228.5 + SH):
        ax.add_patch(Circle((PX + ix, PY + 30), 4, fc="none", ec=GREY, lw=0.4, ls=(0, (1.5, 1)), zorder=6))
    T(PX + MW + 2, PY + 30, "dashed circles:\n¼\"-20 inserts\nunderneath (S4)", fontsize=4.4, color=GREY, va="center")
    # ---- front elevation
    FX, FY = 14, 104
    ax.add_patch(Rectangle((FX + 10, FY), MW - 20, 1.2, fc=INK))                  # feet line
    ax.add_patch(FancyBboxPatch((FX, FY + 1.2), MW, H_RIM - 1.2, boxstyle="round,pad=0,rounding_size=3", fc=SHELL, ec=SHELLD, lw=0.6))
    ax.add_patch(Rectangle((FX + MW / 2 - 132, FY + H_RIM - 1.6), 264, 1.6, fc=BRASS, ec="none"))   # rail seen on edge
    ax.add_patch(Polygon([(FX + MW / 2 - 21.5, FY + H_RIM + 2.5), (FX + MW / 2 - 14.5, FY + H_RIM + 2.5), (FX + MW / 2 - 18, FY + H_RIM - 4)], fc=BRASS, ec=BRASSD, lw=0.4))
    ax.add_patch(FancyBboxPatch((FX + MW / 2 - 4.5, FY + 9), 9, 3.2, boxstyle="round,pad=0,rounding_size=1.4", fc="#111", ec="none"))
    ax.add_patch(Circle((FX + MW / 2 + 9, FY + 10.6), 1.1, fc="#ffcf6b", ec="none"))
    T(FX + MW / 2 - 12, FY + 18.5, "keep the keyboard", fontsize=4.6, ha="right", color=CREAM, style="italic")
    T(FX + MW / 2 + 14, FY + 18.5, "at its home octave", fontsize=4.6, ha="left", color=CREAM, style="italic")
    T(FX + MW / 2, FY + 4.0, "USB-C host · port light", fontsize=3.8, ha="center", color="#d9cbb0")
    T(FX, FY + H_RIM + 5, "FRONT (faces the keyboard) · host port on the axis, low; the line engraved either side; brass target riding the rail on the rim", fontsize=6.0, weight="bold")
    # ---- rear elevation (seen from behind: plan-left appears on the right)
    RX, RY = 14, 58
    ax.add_patch(Rectangle((RX + 10, RY), MW - 20, 1.2, fc=INK))
    ax.add_patch(FancyBboxPatch((RX, RY + 1.2), MW, H_RIM - 1.2, boxstyle="round,pad=0,rounding_size=3", fc=SHELL, ec=SHELLD, lw=0.6))
    # crown band (rear-centre, in front of view)
    ax.add_patch(Rectangle((RX + MW - CROWN_X1, RY + 1.2), CROWN_X1 - CROWN_X0, H_RIM - 1.2, fc=SHELLD, ec="none"))
    # two flat port facets either side of the crown
    left_ports = [("phones", "jack"), ("line", "jack"), ("midi in", "trs"), ("midi out", "trs")]       # plan-right side → appears left in rear view
    right_ports = [("power", "slide"), ("usb-c", "usbc"), ("tune", "trim"), ("split", "slide")]     # plan-left side → appears right
    def facet(x0, ports):
        ax.add_patch(Rectangle((x0, RY + 5), 76, 22, fc="#4f3220", ec="#3a2516", lw=0.5))
        for i, (name, kind) in enumerate(ports):
            cx = x0 + 9.5 + i * 19
            if kind == "jack": ax.add_patch(Circle((cx, RY + 15), 3.0, fc="#111", ec="#888", lw=0.4))
            if kind == "trs": ax.add_patch(Circle((cx, RY + 15), 2.6, fc="#111", ec="#888", lw=0.4))
            if kind == "usbc": ax.add_patch(FancyBboxPatch((cx - 4.5, RY + 13.4), 9, 3.2, boxstyle="round,pad=0,rounding_size=1.4", fc="#111", ec="none"))
            if kind == "slide":
                ax.add_patch(Rectangle((cx - 4.5, RY + 13), 9, 4, fc="#222", ec="none")); ax.add_patch(Rectangle((cx - 4.5, RY + 13.5), 3.5, 3, fc="#bbb", ec="none"))
            if kind == "trim": ax.add_patch(Circle((cx, RY + 15), 2.4, fc="#bbb", ec="#555", lw=0.4)); ax.plot([cx - 1.6, cx + 1.6], [RY + 15, RY + 15], color="#333", lw=0.5)
            T(cx, RY + 22.5, name, fontsize=3.9, ha="center", color=CREAM)
    facet(RX + 20, left_ports); facet(RX + MW - 20 - 76, right_ports)
    T(RX + MW / 2, RY + 17, "crown\n(speaker box)", fontsize=4.2, ha="center", va="center", color="#bfa98b")
    T(RX, RY + H_RIM + 5, "REAR (seen from behind) · two flat port facets on the rear arc: set-once on one side (power · usb-c · tune · split), sound and MIDI on the other", fontsize=6.0, weight="bold")
    T(RX, RY - 6, "Power is a recessed slide, so it can't switch on in a bag. The two USB-C sockets are a whole body apart: host on the front face, charging on the rear facet.", fontsize=5.4, color="#444")
    # ---- section on the axis (x = 140), y horizontal (front at left)
    SX, SY = 180, 12
    ax.add_patch(Polygon([(SX, SY), (SX + MD, SY), (SX + MD, SY + H_RIM), (SX + RAKE1, SY + H_RIM), (SX + RAKE0, SY + H_DECK),
                          (SX + 4, SY + H_DECK), (SX + 4, SY + H_RIM), (SX, SY + H_RIM)], closed=True, fc="none", ec=SHELLD, lw=0.8))
    ax.add_patch(Rectangle((SX + 2, SY + 2.4), 46, 1.6, fc="#3a7a4a", ec="none"))       # board (front part)
    ax.add_patch(Rectangle((SX + 2, SY + 2.4 + 7.5 + 3), 46, 1.6, fc="#3a7a4a", ec="none"))
    ax.add_patch(Rectangle((SX + 2, SY + 2.4), 46, 7.5, fc="#c9c3b5", ec="none", alpha=0.5))
    ax.text(SX + 25, SY + 6, "cells beside the crown,\nnot on the axis (dashed)", fontsize=3.4, ha="center", va="center", color="#555")
    ax.add_patch(Rectangle((SX + 12, SY + H_DECK), 15, 8, fc=CORAL, ec="none"))           # DEPTH knob
    ax.add_patch(Rectangle((SX + 35, SY + H_DECK), 10, 8, fc=INK, ec="none"))             # SHIMMER mode
    # speaker box and driver
    ax.add_patch(Rectangle((SX + 49, SY + 2.4), MD - 51, H_RIM - 4.4, fc="none", ec="#7a6a55", lw=0.5, ls=(0, (2, 1))))
    ax.add_patch(Polygon([(SX + 56, SY + H_RIM - 2.5), (SX + 101, SY + H_RIM - 2.5), (SX + 90, SY + H_RIM - 22), (SX + 67, SY + H_RIM - 22)], fc="#9c8f7a", ec="none"))
    ax.add_patch(Rectangle((SX + 70, SY + H_RIM - 26.5), 17, 4.5, fc="#555", ec="none"))
    ax.text(SX - 166, SY + 30, "SECTION on the axis (x = 140), front at the left", fontsize=6.0, weight="bold")
    ax.text(SX - 166, SY + 24, "deck 26 · knob tops 34 · rim and crown 35 (speaker needs 32 [r2])", fontsize=4.8, color=GREY)
    ax.text(SX - 166, SY + 19, "driver TEBM28C10-4B Ø 55 × 24 [r2], firing up through the crown's grille;\nsealed box ≈ 60 × 55 × 27 inside ≈ 76 cm³ net (≥ 60 [r2]); driver position: eng.\nCells (2 × 50 × 60 × 7.5) sit beside the crown, under the deck, so the deck can sit at 26 (eng's flat stack is ≈ 23.5).", fontsize=4.6, va="top", color="#444")
    # ---- margin notes
    nx, ny = 330, 255
    rows = [("Ratio: one unit, harmonic", "Unit 35 mm. Length : depth : height = 8 : 3 : 1, ends 2 units. Each half (140 × 105) is 4 : 3, a fourth; the halves together, 8 : 3, an octave and a fourth; centre : end = 3 : 2, a fifth; length : height = 8 : 1, three octaves. A string machine proportioned by string lengths."),
            ("Why these sizes", "The panel needs 264 of controls (family pitch), plus 8 each end = 280. The speaker crown needs 105 at the centre [r2]; the jambs need only ≈ 56 at the ends, so 70. The speaker needs a 32 body [r2]; 35 gives 3 mm of margin. The parts set the sizes; the ratio tunes them."),
            ("Outline: a hull in plan", "Front straight: it faces the keyboard and carries the brass rail. Ends 70 deep. Rear: one fair arc rising to 105 over the speaker. Two flat port facets sit on the arc, either side of the crown. Every edge has a job."),
            ("Height 35, not 40", "Only the speaker needs 32 [r2]. The deck sits at 26 over eng's flat stack (cells beside the crown), the knobs top out at 34, and the rim and crown stand at 35. Eng to confirm the stack."),
            ("Rows and touch", "Front row = amounts (Ø 14.9), rear = kinds and set-then-left (PRESSURE, SHIMMER mode Ø 10). Words above controls; DRIFT · SHIMMER · TIME on the crown's rake. Brass frets, mirrored; jambs at both ends; HOLD brass; TAP's ring is the status light."),
            ("Colour", "Shell walnut-brown PETG, deck cream, brass for what you touch to set (frets, rail, target, HOLD), black knobs, one coral: DEPTH, on the axis.")]
    y = ny
    for h, b in rows:
        T(nx, y, h, fontsize=5.6, weight="bold", va="top")
        w = textwrap.fill(b, 52)
        T(nx, y - 3.2, w, fontsize=4.6, va="top", color="#333")
        y -= 6.5 + 2.6 * w.count("\n") + 2.6
    T(12, 6, FOOT, fontsize=4.6, color=GREY)
    fig.savefig("../module/module-1to1-A3.png", facecolor=BG, dpi=150)
    fig.savefig("../module/module-1to1-A3.pdf", facecolor=BG)


# =================================================================== shared kit parts
KW = 412.0; INNER = 404.0
MOD_H = H_RIM           # 35, PROPOSAL (40 if the sunk deck isn't adopted)
WEIGHTS = {  # kit totals (module 0.67–0.93 [r2] + carry + cable/adapter), from systems' kit files; T5 withdrawn by the owner: shown, not judged
    "fallboard": ("0.5–0.7", {"nano": "1.45–1.91", "kbc": "1.55–2.01", "xkey": "1.80–2.27"}),
    "spine":     ("0.3–0.4", {"nano": "1.25–1.61", "kbc": "1.35–1.71", "xkey": "1.60–1.97"}),
    "cloth":     ("0.23–0.36", {"nano": "1.17–1.56", "kbc": "1.27–1.66", "xkey": "1.53–1.92"}),
}

def end_blocks(ax, ox, oy_back, kbkey, s=1.0, z=4, depth=80):
    """Blocks at the back of a bed whose keyboard's rear edge is at oy_back (block spans oy_back-depth .. oy_back)."""
    name, w, d, h, *_ = KB[kbkey]
    gap = (INNER - w) / 2
    for side in (0, 1):
        bx = ox + 4 * s if side == 0 else ox + (4 + gap + w) * s
        ax.add_patch(Rectangle((bx, oy_back - depth * s), gap * s, depth * s, fc=WAL, ec=WALD, lw=0.5, zorder=z))
        lip = ox + (4 + gap - 0.5) * s if side == 0 else ox + (4 + gap + w - 6.5) * s
        ax.add_patch(Rectangle((lip, oy_back - depth * s), 7 * s, depth * s, fc=WALD, ec="none", alpha=0.85, zorder=z + 0.1))
        # 15 mm notch at the back corner for an end-socket plug
        nx = bx + (gap - 8) * s if side == 0 else bx
        ax.add_patch(Rectangle((nx if gap > 9 else bx, oy_back - 15 * s), min(8, gap) * s, 15 * s, fc=GUT, ec="none", zorder=z + 0.2))
        ax.add_patch(Circle((bx + gap * s / 2, oy_back - depth * s / 2), 2.2 * s, fc=BRASS, ec="none", zorder=z + 0.3))
    return gap

def brass_scale(ax, ox, y, s=1.0, z=5):
    for t in range(0, 33, 4):
        for side in (0, 1):
            X = ox + (4 + t) * s if side == 0 else ox + (KW - 4 - t) * s
            ax.plot([X, X], [y, y + (3.2 if t % 8 else 4.4) * s], color=BRASS, lw=0.45, zorder=z)

def coil(ax, x0, x1, y, s=1.0, z=5, col="#6b6b6b"):
    n = int(abs(x1 - x0) / (3.2 * s))
    for i in range(n):
        ax.add_patch(Ellipse((x0 + i * 3.2 * s, y), 3.2 * s, 9 * s, fc="none", ec=col, lw=0.5, zorder=z))

def charger(ax, x, y, s=1.0, z=5):
    ax.add_patch(FancyBboxPatch((x, y), 30 * s, 30 * s, boxstyle=f"round,pad=0,rounding_size={4*s}", fc="#e9e9e9", ec="#999", lw=0.4, zorder=z))
    ax.add_patch(Rectangle((x + 9 * s, y + 13 * s), 12 * s, 4 * s, fc="#555", ec="none", zorder=z + 0.1))

def adapter(ax, x, y, s=1.0, z=5):
    ax.add_patch(FancyBboxPatch((x, y), 22 * s, 9 * s, boxstyle=f"round,pad=0,rounding_size={2*s}", fc="#3a3a3a", ec="none", zorder=z))

# =================================================================== FALLBOARD
FB_D = 288.0
def fallboard_plan(ax, ox, oy, kbkey="xkey", s=1.0, labels=False, cable=True, lidstate=None, target=True, md=1):
    P = lambda x, y: (ox + x * s, oy + y * s)
    ax.add_patch(FancyBboxPatch(P(0, 0), KW * s, FB_D * s, boxstyle=f"round,pad=0,rounding_size={10*s}", fc=WAL, ec=WALD, lw=0.8, zorder=1))
    ax.add_patch(Rectangle(P(4, 4), INNER * s, 140 * s, fc=BED, ec="none", zorder=1.1))            # bed
    ax.add_patch(Rectangle(P(4, 144), INNER * s, 35 * s, fc=GUT, ec="none", zorder=1.1))            # gutter
    ax.add_patch(Rectangle(P(4, 179), INNER * s, 105 * s, fc="#3a2f2a", ec="none", zorder=1.1))     # rear band floor
    for dx in ((KW - MW) / 2 - 3, (KW + MW) / 2):                                                                     # pocket dividers
        ax.add_patch(Rectangle(P(dx, 179), 3 * s, 105 * s, fc=WAL, ec="none", zorder=1.2))
    # rear-wall windows behind the module's port facets
    for wx in ((KW - MW) / 2 + 20, (KW - MW) / 2 + 184):
        ax.add_patch(Rectangle(P(wx, 284), 76 * s, 4 * s, fc="#2a201b", ec="none", zorder=1.3))
    module_plan(ax, ox + (KW - MW) / 2 * s, oy + 179 * s, s, detail=md, z=2)
    k0, kw = keyboard(ax, ox + (KW - KB[kbkey][1]) / 2 * s, oy + (144 - KB[kbkey][2]) * s, kbkey, s, z=3, label=labels or s > 0.6)
    gap = end_blocks(ax, ox, oy + 144 * s, kbkey, s)
    brass_scale(ax, ox, oy + 0.5 * s, s)
    # pockets: charger left, spare cable + card right
    charger(ax, *P(13, 215), s)
    ax.add_patch(Rectangle(P(366, 196), 30 * s, 70 * s, fc="#e7dfcc", ec="#b8ad95", lw=0.4, zorder=5))   # 1:1 card, folded
    coil(ax, ox + 370 * s, ox + 392 * s, oy + 235 * s, s, col="#888")
    if cable:
        # coiled cable lying in the gutter + adapter; live run from keyboard rear socket to the host port
        coil(ax, ox + 30 * s, ox + 150 * s, oy + 161 * s, s)
        adapter(ax, *P(300, 157), s)
        sx = (KW - KB[kbkey][1]) / 2 + KB[kbkey][1] * 0.78
        ax.plot([ox + sx * s, ox + sx * s, ox + KW / 2 * s, ox + KW / 2 * s], [oy + 144 * s, oy + 168 * s, oy + 168 * s, oy + 179 * s], color="#c9c9c9", lw=1.3, zorder=6)
        ax.add_patch(Rectangle(P(sx - 5, 141), 10 * s, 6 * s, fc="#ddd", ec="#777", lw=0.4, zorder=6.1))
    if target:
        bx = bc_x(ox + (KW - KB[kbkey][1]) / 2 * s, kbkey, s)
        ax.add_patch(Polygon([(bx - 3.5 * s, oy + 182.6 * s), (bx + 3.5 * s, oy + 182.6 * s), (bx, oy + 176 * s)], fc=BRASS, ec=BRASSD, lw=0.4, zorder=7))
    return gap

def fb_side(ax, ox, oy, lid_deg, s=1.0, lamp=False, kb_h=16, mod_h=MOD_H, thigh=False):
    """Side elevation, front at the left: tray, keyboard, module, lid hinged at the rear top."""
    base = 4; wall_h = mod_h + 4
    ax.add_patch(Rectangle((ox, oy), FB_D * s, base * s, fc=WAL, ec="none", zorder=2))
    ax.add_patch(Rectangle((ox, oy), 4 * s, 14 * s, fc=WAL, ec="none", zorder=2))
    ax.add_patch(Rectangle((ox + (FB_D - 4) * s, oy), 4 * s, wall_h * s, fc=WAL, ec="none", zorder=2))
    ax.add_patch(Rectangle((ox + 9 * s, oy + base * s), 135 * s, kb_h * s, fc=SILVER, ec="#777", lw=0.3, zorder=2))
    mb = 0
    ax.add_patch(Polygon([(ox + 179 * s, oy + mb * s), (ox + 284 * s, oy + mb * s), (ox + 284 * s, oy + (mb + mod_h) * s),
                          (ox + (179 + RAKE1) * s, oy + (mb + mod_h) * s), (ox + (179 + RAKE0) * s, oy + (mb + H_DECK) * s),
                          (ox + 183 * s, oy + (mb + H_DECK) * s), (ox + 183 * s, oy + (mb + mod_h) * s), (ox + 179 * s, oy + (mb + mod_h) * s)],
                         fc=SHELL, ec="none", zorder=2))
    hx, hy = ox + FB_D * s, oy + (wall_h + 0) * s
    a = math.radians(lid_deg)
    L = FB_D * s
    ex, ey = hx - L * math.cos(a), hy + L * math.sin(a)
    ax.plot([hx, ex], [hy, ey], color=WALD, lw=3.0, solid_capstyle="butt", zorder=3)
    if 30 < lid_deg < 150:
        ax.plot([hx - 90 * s * math.cos(a), hx - 20 * s], [hy + 90 * s * math.sin(a), hy - 2 * s], color=BRASS, lw=0.9, zorder=3)
        if lamp:
            ax.add_patch(Circle((ex + 3 * s, ey - 3 * s), 3.5 * s, fc="#ffd98a", ec="none", zorder=4))
            ax.add_patch(Polygon([(ex + 3 * s, ey - 3 * s), (ox + 10 * s, oy + (base + kb_h) * s), (ox + 145 * s, oy + (base + kb_h) * s)], fc="#ffe2a0", ec="none", alpha=0.4, zorder=1))

# =================================================================== SPINE (solander box), open flat
SP_KT = 143.0; SP_SPINE = MOD_H + 16 + 3 + 2   # 54 (61 with a 40 module)
def spine_plan(ax, ox, oy, kbkey="xkey", s=1.0, labels=False, cable=True, target=True, md=1):
    P = lambda x, y: (ox + x * s, oy + y * s)
    # keyboard tray
    ax.add_patch(FancyBboxPatch(P(0, 0), KW * s, SP_KT * s, boxstyle=f"round,pad=0,rounding_size={5*s}", fc=WAL, ec=WALD, lw=0.8, zorder=1))
    ax.add_patch(Rectangle(P(4, 4), INNER * s, (SP_KT - 8) * s, fc=BED, ec="none", zorder=1.1))
    # spine (open flat: a cloth band with the rigid spine board)
    y1 = SP_KT; y2 = SP_KT + SP_SPINE
    ax.add_patch(Rectangle(P(0, y1), KW * s, SP_SPINE * s, fc="#4a3020", ec="none", zorder=1))
    ax.add_patch(Rectangle(P(0, y1 + 6), KW * s, (SP_SPINE - 12) * s, fc="#3b2619", ec="none", zorder=1.05))
    # module tray
    y3 = y2; MT = 143.0
    ax.add_patch(FancyBboxPatch(P(0, y3), KW * s, MT * s, boxstyle=f"round,pad=0,rounding_size={5*s}", fc=WAL, ec=WALD, lw=0.8, zorder=1))
    ax.add_patch(Rectangle(P(4, y3 + 4), INNER * s, (MT - 8) * s, fc="#3a2f2a", ec="none", zorder=1.1))
    ax.add_patch(Rectangle(P(4, y3 + 4), INNER * s, 30 * s, fc=GUT, ec="none", zorder=1.15))       # cable strip
    for dx in ((KW - MW) / 2 - 3, (KW + MW) / 2):
        ax.add_patch(Rectangle(P(dx, y3 + 34), 3 * s, 105 * s, fc=WAL, ec="none", zorder=1.2))
    for wx in ((KW - MW) / 2 + 20, (KW - MW) / 2 + 184):
        ax.add_patch(Rectangle(P(wx, y3 + MT - 4), 76 * s, 4 * s, fc="#2a201b", ec="none", zorder=1.3))
    for cx, cy in [(0, 0), (KW - 22, 0), (0, y3 + MT - 22), (KW - 22, y3 + MT - 22)]:
        pass
    module_plan(ax, ox + (KW - MW) / 2 * s, oy + (y3 + 34) * s, s, detail=md, z=2)
    name, w, d, h, *_ = KB[kbkey]
    keyboard(ax, ox + (KW - w) / 2 * s, oy + (SP_KT - 4 - d) * s, kbkey, s, z=3, label=labels or s > 0.6)
    end_blocks(ax, ox, oy + (SP_KT - 4) * s, kbkey, s)
    brass_scale(ax, ox, oy + 0.5 * s, s)
    charger(ax, *P(13, y3 + 70), s)
    ax.add_patch(Rectangle(P(366, y3 + 50), 30 * s, 70 * s, fc="#e7dfcc", ec="#b8ad95", lw=0.4, zorder=5))
    if cable:
        coil(ax, ox + 40 * s, ox + 150 * s, oy + (y3 + 19) * s, s)
        adapter(ax, *P(300, y3 + 14), s)
        sx = (KW - w) / 2 + w * 0.78
        ax.plot([ox + sx * s, ox + sx * s, ox + KW / 2 * s, ox + KW / 2 * s], [oy + (SP_KT - 4) * s, oy + (y2 - 10) * s, oy + (y2 - 10) * s, oy + (y3 + 34) * s], color="#c9c9c9", lw=1.3, zorder=6)
        ax.add_patch(Rectangle(P(sx - 5, SP_KT - 7), 10 * s, 6 * s, fc="#ddd", ec="#777", lw=0.4, zorder=6.1))
    if target:
        bx = bc_x(ox + (KW - w) / 2 * s, kbkey, s)
        ax.add_patch(Polygon([(bx - 3.5 * s, oy + (y3 + 37.6) * s), (bx + 3.5 * s, oy + (y3 + 37.6) * s), (bx, oy + (y3 + 31) * s)], fc=BRASS, ec=BRASSD, lw=0.4, zorder=7))
    return y3 + MT

# =================================================================== CLOTH, spread
def cloth_plan(ax, ox, oy, kbkey="nano", s=1.0, labels=False, cable=True, size=800, words=True):
    P = lambda x, y: (ox + x * s, oy + y * s)
    ax.add_patch(Rectangle(P(0, 0), size * s, size * s, fc=CLOTHC, ec="none", zorder=1))
    ax.add_patch(Rectangle(P(14, 14), (size - 28) * s, (size - 28) * s, fc="none", ec=CLOTHL, lw=1.0, zorder=1.1))
    fx, fy = (size - KW) / 2, 230
    ax.add_patch(Rectangle(P(fx, fy), KW * s, FB_D * s, fc="none", ec=THREAD, lw=0.9, zorder=1.2))
    ax.plot([ox + size / 2 * s] * 2, [oy + (fy - 25) * s, oy + (fy + FB_D + 15) * s], color=THREAD, lw=0.6, ls=(0, (6, 4)), zorder=1.2)
    if words: ax.text(*P(size / 2, fy - 40), "keep the keyboard at its home octave", ha="center", fontsize=max(4.5, 6 * s * 1.4), color=THREAD, style="italic", zorder=1.3, clip_on=True)
    module_plan(ax, ox + (size / 2 - MW / 2) * s, oy + (fy + 179) * s, s, detail=1, z=2)
    name, w, d, h, *_ = KB[kbkey]
    keyboard(ax, ox + (size / 2 - w / 2) * s, oy + (fy + 144 - d) * s, kbkey, s, z=3, label=labels)
    ax.add_patch(Rectangle(P(40, 40), 200 * s, 150 * s, fc=CLOTHL, ec="#6d7a75", lw=0.8, zorder=1.3))
    charger(ax, *P(60, 70), s); adapter(ax, *P(110, 80), s); coil(ax, ox + 150 * s, ox + 220 * s, oy + 140 * s, s, col="#9aa")
    ax.add_patch(Rectangle(P(size - 360, size - 170), 320 * s, 130 * s, fc=CLOTHL, ec="#6d7a75", lw=0.8, zorder=1.3))
    xl, yl = ax.get_xlim(), ax.get_ylim()
    if words and xl[0] <= ox + (size - 200) * s <= xl[1] and yl[0] <= oy + (size - 105) * s <= yl[1]:
      ax.text(*P(size - 200, size - 105), "module sleeve (removable, washable)", ha="center", va="center", fontsize=max(4.5, 6 * s * 1.4), color=THREAD, zorder=1.4, clip_on=True)
    for cx, cy in [(0, 0), (size, 0), (0, size), (size, size)]:
        ax.add_patch(Circle(P(cx, cy), 14 * s, fc=BRASS, ec="none", zorder=1.5))
    if cable:
        sx = size / 2 - w / 2 + w * 0.78
        ax.plot([ox + sx * s, ox + sx * s, ox + size / 2 * s, ox + size / 2 * s], [oy + (fy + 144) * s, oy + (fy + 162) * s, oy + (fy + 162) * s, oy + (fy + 179) * s], color="#c9c9c9", lw=1.3, zorder=6)

def rear_wall(ax, ox, oy, s, wall_h, windows_x, mod_off_x, label):
    """Elevation from behind. windows_x: plan-x of each window's left edge (in kit coords). Seen from behind, x is mirrored."""
    ax.add_patch(Rectangle((ox, oy), KW * s, wall_h * s, fc=WAL, ec=WALD, lw=0.6, zorder=1))
    ports = {0: [("power", "slide"), ("usb-c", "usbc"), ("tune", "trim"), ("split", "slide")],
             1: [("phones", "jack"), ("line", "jack"), ("in", "trs"), ("out", "trs")]}
    for i, wx in enumerate(windows_x):
        X = ox + (KW - wx - 76) * s               # mirror
        ax.add_patch(Rectangle((X, oy + 6 * s), 76 * s, (wall_h - 10) * s, fc="#4f3220", ec="#2a1a10", lw=0.6, zorder=2))
        pl = ports[0] if i == 0 else ports[1]     # plan-left window holds power side (as the module's rear view)
        for j, (name, kind) in enumerate(pl):
            cx = X + (9.5 + j * 19) * s; cy = oy + (6 + (wall_h - 10) / 2) * s
            if kind in ("jack", "trs"): ax.add_patch(Circle((cx, cy), 2.8 * s, fc="#111", ec="#888", lw=0.4, zorder=3))
            elif kind == "usbc": ax.add_patch(FancyBboxPatch((cx - 4.5 * s, cy - 1.6 * s), 9 * s, 3.2 * s, boxstyle="round,pad=0,rounding_size=1", fc="#111", ec="none", zorder=3))
            elif kind == "slide":
                ax.add_patch(Rectangle((cx - 4.5 * s, cy - 2 * s), 9 * s, 4 * s, fc="#222", ec="none", zorder=3)); ax.add_patch(Rectangle((cx - 4.5 * s, cy - 1.5 * s), 3.5 * s, 3 * s, fc="#bbb", ec="none", zorder=3.1))
            elif kind == "trim": ax.add_patch(Circle((cx, cy), 2.4 * s, fc="#bbb", ec="#555", lw=0.4, zorder=3))
            ax.text(cx, oy + (wall_h - 2) * s, name, ha="center", va="top", fontsize=4.6, color=CREAM, zorder=4)
    ax.text(ox, oy - 9 * s, label, fontsize=6.4, color="#333", va="top")

def packing_strip(fig, rect, frames, title):
    ax = fig.add_axes(rect); ax.axis("off"); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.text(0, 0.97, title, fontsize=9, weight="bold", va="top")
    n = len(frames)
    for i, (draw, cap) in enumerate(frames):
        sub = fig.add_axes([rect[0] + rect[2] * i / n + 0.004, rect[1] + rect[3] * 0.22, rect[2] / n - 0.01, rect[3] * 0.64])
        sub.set_aspect("equal"); sub.axis("off")
        draw(sub)
        ax.text((i + 0.03) / n, 0.18, f"{i+1}", fontsize=11, weight="bold", color=BRASSD, va="top")
        ax.text((i + 0.03) / n + 0.022, 0.18, textwrap.fill(cap, 34), fontsize=6.8, va="top", color="#333")

# ------------------------------------------------------------------- FALLBOARD sheets
def sheet_fallboard():
    fig = sheet("FALLBOARD · in use: on a bench, on a lap, the keyboard range, the cable and pockets, the rear wall",
                "One plane, one lid. The module (280 × 105 × 35) sits centred in the rear band of a 412 × 288 walnut tray; the guest keyboard lies in a dark bed in front, held by its ends. Charger in the left pocket.", FOOT)
    # bench, plan
    ax = axes(fig, [0.015, 0.47, 0.32, 0.44], (-70, 560), (-90, 470))
    bench(ax, -60, -10, 600, 420)
    fallboard_plan(ax, 30, 40, "xkey", 1.0 * 0 + 0.999)
    ax.add_patch(Rectangle((30, 40 + 288), 412, 52, fc=WALD, ec="none", alpha=0.85, zorder=8))      # lid standing (seen from above)
    ax.add_patch(Rectangle((40, 40 + 288 + 44), 392, 4, fc="#ffd98a", ec="none", zorder=8.1))
    ax.text(236, 40 + 288 + 26, "lid standing ≈ 100° (seen from above)", ha="center", fontsize=6, color=CREAM, zorder=9)
    ax.text(236, -40, "▲ you", ha="center", fontsize=8, weight="bold", color="#333")
    ax.text(-60, 450, "ON A BENCH · plan · lid up, lamp optional", fontsize=8.5, weight="bold")
    # bench, side with lamp
    ax = axes(fig, [0.345, 0.73, 0.30, 0.18], (-30, 320), (-30, 330))
    ax.add_patch(Rectangle((-30, -10), 350, 10, fc=SLAT, ec="none"))
    fb_side(ax, 0, 0, 100, 1.0, lamp=True)
    ax.text(-30, 320, "side · lid at ≈ 100° on its stay: music stand, a low sun's shade,\nand (optional) a warm strip on its top edge, on its own AAA cells", fontsize=6.4, va="top")
    # lap, side
    ax = axes(fig, [0.345, 0.47, 0.30, 0.22], (-60, 330), (-150, 170))
    a = math.radians(8)
    ax.add_patch(Polygon([(-50, -6), (330, -6 - 380 * math.tan(a)), (330, -60 - 380 * math.tan(a)), (-50, -60)], fc=SKIN, ec="none"))
    import matplotlib.transforms as mt
    tr = mt.Affine2D().rotate_deg_around(0, 0, -8) + ax.transData
    for art in []: pass
    sub_ox = 0
    # draw the kit rotated by drawing into a temporary list of patches
    before = len(ax.patches); before_l = len(ax.lines)
    fb_side(ax, 0, 0, 0, 1.0, lamp=False)
    for pt in ax.patches[before:]: pt.set_transform(tr)
    for ln in ax.lines[before_l:]: ln.set_transform(tr)
    ax.lines[-1].set_visible(False)   # no lid on the lap
    ax.text(-60, 160, "ON A LAP · side · lid lifted off its pins; one stiff 412 × 288 board\nalong both thighs, keys nearest you", fontsize=6.4, va="top")
    ax.text(-55, -115, "hips", fontsize=6, color="#7a6a55"); ax.text(280, -115, "knees →", fontsize=6, color="#7a6a55")
    # lap, plan
    ax = axes(fig, [0.655, 0.47, 0.33, 0.44], (-60, 480), (-110, 520))
    thighs(ax, 36, -40, 1.0)
    fallboard_plan(ax, 0, 20, "kbc", 0.999)
    ax.text(206, -95, "▲ you (hips)", ha="center", fontsize=8, weight="bold", color="#333")
    ax.text(-60, 505, "ON A LAP · plan · lid off · K-Board C", fontsize=8.5, weight="bold")
    ax.text(-60, 480, "the tray spans both thighs; no hinge to fold", fontsize=6.4, color="#444")
    # keyboard range
    ax = axes(fig, [0.015, 0.04, 0.27, 0.40], (-10, 425), (-50, 660))
    fallboard_plan(ax, 0, 0, "nano", 0.999, cable=False)
    fallboard_plan(ax, 0, 340, "xkey", 0.999, cable=False)
    ax.text(0, -12, "below: smallest, nanoKEY2 325 × 83 · blocks fully out (≈ 40 mm each);\nthe ≈ 57 mm of bed in front stays empty (director)", fontsize=6.2, va="top")
    ax.text(0, 652, "THE KEYBOARD RANGE · end blocks · one brass scale", fontsize=8.5, weight="bold")
    ax.text(0, 300, "above: largest, Xkey 25 388 × 135 · blocks fully in (8 mm)", fontsize=6.2, va="bottom")
    # cable + pocket detail (zoom)
    ax = axes(fig, [0.30, 0.04, 0.36, 0.40], (0, 230), (110, 300))
    fallboard_plan(ax, 0, 0, "xkey", 1.0, md=2)
    ax.text(2, 296, "THE CABLE PATH AND THE POCKETS (left half, enlarged)", fontsize=8.5, weight="bold")
    lab = dict(fontsize=6.2, color="#111", bbox=dict(fc="#f6f2ea", ec="none", alpha=0.85, pad=1.2), zorder=20)
    ax.text(10, 270, "left pocket ≈ 59 × 105: a ≈ 30 mm charger", **lab)
    ax.text(30, 172, "gutter 404 × 35: coiled 0.3–0.5 m cable + C-to-A adapter", **lab)
    ax.text(150, 150, "live run: keyboard socket → host port on the axis", **lab)
    ax.text(14, 125, "end block (left edge): 80 deep, foamed lip over the end cap,\nthumb lock, 15 mm notch for an end socket", **lab)
    ax.text(70, 205, "window in the rear wall\nbehind each port facet ↑", **lab)
    # rear wall
    ax = axes(fig, [0.675, 0.06, 0.315, 0.30], (-10, 425), (-45, 60))
    rear_wall(ax, 0, 0, 1.0, MOD_H + 4, [(KW - MW) / 2 + 20, (KW - MW) / 2 + 184], 57.5,
              "THE REAR WALL (from behind) · two windows line up with the module's port facets:\npower and charging reachable while it plays; unplug the phones before the lid closes")
    ax.text(-10, 58, "REAR", fontsize=8.5, weight="bold")
    fig.savefig("../fallboard/fallboard-A-in-use.png", facecolor=BG)

def closed_sheet(kit, title, sub, closed_draw, dims, thick, thick_alt, carry_w, frames, packtitle):
    fig = sheet(title, sub, FOOT)
    ax = axes(fig, [0.015, 0.40, 0.63, 0.50], (-20, 1370), (-120, 560))
    closed_draw(ax, 0, 0)
    W_, D_ = dims
    ax.text(W_ / 2, -22, f"{kit} closed · {W_:.0f} × {D_:.0f} × {thick:.0f}" + (f" ({thick_alt:.0f} if the module stays 40 tall)" if thick_alt else ""), ha="center", fontsize=7.4, weight="bold")
    laptop(ax, 470, 0); book(ax, 860, 0)
    # backpack, front view, kit standing on its short edge
    bx = 1050
    backpack(ax, bx, 0, 1.0)
    ax.add_patch(Rectangle((bx + 150 - D_ / 2, 6), D_, W_, fc=WAL if kit != "CLOTH" else CLOTHC, ec=WALD, lw=0.5, alpha=0.9))
    ax.text(bx + 150, -22, "standing in the pack (front view)", ha="center", fontsize=6.4)
    ax.text(0, 548, "CLOSED, beside a 16-inch laptop and a hardback, and in a daypack · all at the same scale", fontsize=8.5, weight="bold")
    # end views
    ax = axes(fig, [0.66, 0.60, 0.32, 0.30], (-20, 330), (-30, 300))
    y = 190
    for name, d, t, col, alt in [(kit, D_, thick, WAL if kit != "CLOTH" else CLOTHC, thick_alt), ("16-inch laptop", 248, 17, LAPTOP, None), ("hardback", 234, 35, BOOK, None)]:
        ax.add_patch(Rectangle((0, y), d, t, fc=col, ec="none"))
        if alt: ax.add_patch(Rectangle((0, y + t), d, alt - t, fc=col, ec="none", alpha=0.3))
        ax.text(d + 6, y + t / 2, f"{name}: {t:.0f}" + (f" ({alt:.0f})" if alt else ""), fontsize=7, va="center")
        y -= 85
    ax.text(-20, 292, "END VIEWS, to scale (depth × thickness)" + (" · pale = with a 40-tall module" if thick_alt else ""), fontsize=7.4, weight="bold")
    # weights
    ax = fig.add_axes([0.66, 0.40, 0.32, 0.18]); ax.axis("off")
    cw, kw = WEIGHTS[kit.lower()]
    rows = [("carry parts", f"{cw} kg"), ("module [r2]", "0.67–0.93 kg"), ("kit + nanoKEY2", f"{kw['nano']} kg"),
            ("kit + K-Board C", f"{kw['kbc']} kg"), ("kit + Xkey 25", f"{kw['xkey']} kg"), ("for scale: 16-inch laptop", "≈ 2.1 kg")]
    ax.text(0, 1.0, "WEIGHT, honestly (lighter is better; no target)", fontsize=8.4, weight="bold", va="top", transform=ax.transAxes)
    for i, (a_, b_) in enumerate(rows):
        ax.text(0.0, 0.84 - i * 0.14, a_, fontsize=7.4, va="top", transform=ax.transAxes)
        ax.text(0.55, 0.84 - i * 0.14, b_, fontsize=7.4, va="top", weight="bold" if "kit" in a_ else None, transform=ax.transAxes)
    packing_strip(fig, [0.015, 0.03, 0.97, 0.33], frames, packtitle)
    fig.savefig(f"../{kit.lower()}/{kit.lower()}-B-closed-and-packing.png", facecolor=BG)

def fb_closed(ax, ox, oy, s=1.0):
    ax.add_patch(FancyBboxPatch((ox, oy), KW * s, FB_D * s, boxstyle=f"round,pad=0,rounding_size={10*s}", fc=WALD, ec="#33200f", lw=0.8))
    ax.add_patch(Rectangle((ox + (KW / 2 - 60) * s, oy + 130 * s), 120 * s, 36 * s, fc=CREAM, ec="none"))
    ax.text(ox + KW / 2 * s, oy + 148 * s, "floss", ha="center", va="center", fontsize=10 * s, style="italic", color=SHELLD)
    ax.add_patch(Rectangle((ox + (KW / 2 - 60) * s, oy + 124 * s), 120 * s, 3 * s, fc=CORAL, ec="none"))
    ax.add_patch(Rectangle((ox + (KW / 2 - 12) * s, oy - 1 * s), 24 * s, 8 * s, fc=BRASS, ec="none"))    # catch

def fb_frames():
    def f1(a):
        a.set_xlim(-10, 425); a.set_ylim(-10, 300); fallboard_plan(a, 0, 0, "xkey", 0.999)
        a.add_patch(Circle(((KW - MW) / 2 + 20 + 66, 292), 14, fc="none", ec=CORAL, lw=1.6, zorder=30))
    def f2(a):
        a.set_xlim(-10, 425); a.set_ylim(-10, 300); fallboard_plan(a, 0, 0, "xkey", 0.999, cable=True)
        a.add_patch(Rectangle((20, 146), 380, 31, fc="none", ec=CORAL, lw=1.6, zorder=30))
    def f3(a):
        a.set_xlim(-10, 425); a.set_ylim(-10, 300); fallboard_plan(a, 0, 0, "xkey", 0.999)
        for x in (8, 404): a.add_patch(Circle((x, 104), 12, fc="none", ec=CORAL, lw=1.6, zorder=30))
    def f4(a):
        a.set_xlim(-30, 330); a.set_ylim(-20, 300); fb_side(a, 0, 0, 35, 1.0)
        a.text(150, 250, "lid down: a foam strip\npins the keyboard", ha="center", fontsize=6.5)
    def f5(a):
        a.set_xlim(-10, 425); a.set_ylim(-10, 300); fb_closed(a, 0, 0)
        a.add_patch(Circle((206, 3), 16, fc="none", ec=CORAL, lw=1.6, zorder=30))
    return [(f1, "Switch off at the rear (recessed slide, through the left window)."),
            (f2, "Unplug the keyboard end. Coil the cable and the C-to-A adapter into the gutter; the cable stays in the host port."),
            (f3, "Thumb-lock both end blocks (they lock empty too, so nothing rattles)."),
            (f4, "Close the lid. The foam strip under it presses the keyboard; the knobs sit under the module's rim."),
            (f5, "Catch. Into the backpack, standing on its short edge. Charger rides in the left pocket.")]


# ------------------------------------------------------------------- SPINE sheets
SP_MT_H = MOD_H + 2      # module tray height (floor cut-out, 2 mm rim over the module)
def spine_side(ax, ox, oy, angle, s=1.0, lamp=False):
    """Side elevation, front at the left. angle = module tray's opening angle (180 flat, ≈110 standing)."""
    kt_h = 21
    ax.add_patch(Rectangle((ox, oy), SP_KT * s, 3 * s, fc=WAL, ec="none", zorder=2))
    ax.add_patch(Rectangle((ox, oy), 3 * s, kt_h * s, fc=WAL, ec="none", zorder=2))
    ax.add_patch(Rectangle((ox + (SP_KT - 3) * s, oy), 3 * s, kt_h * s, fc=WAL, ec="none", zorder=2))
    ax.add_patch(Rectangle((ox + 4 * s, oy + 3 * s), 135 * s, 16 * s, fc=SILVER, ec="#777", lw=0.3, zorder=2))
    px, py = ox + (SP_KT + SP_SPINE) * s, oy
    ax.add_patch(Rectangle((ox + SP_KT * s, oy), SP_SPINE * s, 2.5 * s, fc="#4a3020", ec="none", zorder=2))
    rot = math.radians(180 - angle)
    def R(x, y):
        return (px + (x * math.cos(rot) - y * math.sin(rot)) * s, py + (x * math.sin(rot) + y * math.cos(rot)) * s)
    tray = [R(0, 0), R(143, 0), R(143, SP_MT_H), R(0, SP_MT_H)]
    ax.add_patch(Polygon(tray, closed=True, fc=WAL, ec=WALD, lw=0.5, zorder=2))
    mod = [R(34, 0), R(139, 0), R(139, MOD_H), R(34 + RAKE1, MOD_H), R(34 + RAKE0, H_DECK), R(38, H_DECK), R(38, MOD_H), R(34, MOD_H)]
    ax.add_patch(Polygon(mod, closed=True, fc=SHELL, ec="none", zorder=2.1))
    if lamp:
        lx, ly = R(143, SP_MT_H)
        ax.add_patch(Circle((lx, ly), 3.5 * s, fc="#ffd98a", ec="none", zorder=4))
        ax.add_patch(Polygon([(lx, ly), (ox + 6 * s, oy + 19 * s), (ox + 140 * s, oy + 19 * s)], fc="#ffe2a0", ec="none", alpha=0.4, zorder=1))

def spine_closed(ax, ox, oy, s=1.0):
    ax.add_patch(FancyBboxPatch((ox, oy), KW * s, SP_KT * s, boxstyle=f"round,pad=0,rounding_size={4*s}", fc=WAL, ec=WALD, lw=0.8))
    for cx, cy, sx, sy in [(0, 0, 1, 1), (KW, 0, -1, 1), (0, SP_KT, 1, -1), (KW, SP_KT, -1, -1)]:
        ax.add_patch(Polygon([(ox + cx * s, oy + cy * s), (ox + (cx + 24 * sx) * s, oy + cy * s), (ox + cx * s, oy + (cy + 24 * sy) * s)], fc=BRASS, ec="none"))
    ax.add_patch(Rectangle((ox, oy + SP_KT * s), KW * s, 7 * s, fc="#4a3020", ec="none"))
    ax.add_patch(Rectangle((ox + (KW / 2 - 55) * s, oy + 52 * s), 110 * s, 34 * s, fc=CREAM, ec="none"))
    ax.text(ox + KW / 2 * s, oy + 69 * s, "floss", ha="center", va="center", fontsize=10 * s, style="italic", color=SHELLD)
    ax.add_patch(Rectangle((ox + (KW / 2 - 55) * s, oy + 46 * s), 110 * s, 3 * s, fc=CORAL, ec="none"))
    for sx in (120, 292):
        ax.add_patch(Rectangle((ox + sx * s, oy - 2 * s), 14 * s, (SP_KT + 9) * s, fc="#2c2c2c", ec="none", alpha=0.8))   # strap

def sheet_spine():
    fig = sheet("SPINE · in use: standing on a table, open flat on a lap, the keyboard range, the cable and pockets, the rear wall",
                "A solander (clamshell) box: a shallow keyboard tray and a deep module tray of one outline, joined by a stop-at-flat spine. The module rides in its tray, front face toward the spine.", FOOT)
    # table, plan (standing)
    ax = axes(fig, [0.015, 0.47, 0.32, 0.44], (-70, 560), (-90, 470))
    ax.add_patch(Rectangle((-60, -10), 600, 420, fc="#b79c7c", ec="none"))
    spine_plan(ax, 30, 40, "xkey", 0.999)
    ax.add_patch(Rectangle((30, 40 + SP_KT + SP_SPINE), KW, 143 * 0.34, fc=WALD, ec="none", alpha=0.0))
    ax.text(236, -40, "▲ you", ha="center", fontsize=8, weight="bold", color="#333")
    ax.text(-60, 450, "OPEN FLAT ON A BENCH OR TABLE · plan · 412 × 340", fontsize=8.5, weight="bold")
    # standing side
    ax = axes(fig, [0.345, 0.73, 0.30, 0.18], (-30, 330), (-30, 200))
    ax.add_patch(Rectangle((-30, -10), 360, 10, fc="#b79c7c", ec="none"))
    spine_side(ax, 0, 0, 110, 1.0, lamp=True)
    ax.text(-30, 198, "side · STANDING ≈ 110° on a table: the module stands behind the keys,\npanel and speaker toward you; optional clip-on lamp on the tray's top edge", fontsize=6.4, va="top")
    # lap side
    ax = axes(fig, [0.345, 0.47, 0.30, 0.22], (-60, 400), (-150, 170))
    import matplotlib.transforms as mt
    a = math.radians(8)
    ax.add_patch(Polygon([(-50, -6), (390, -6 - 440 * math.tan(a)), (390, -60 - 440 * math.tan(a)), (-50, -60)], fc=SKIN, ec="none"))
    tr = mt.Affine2D().rotate_deg_around(0, 0, -8) + ax.transData
    n0 = len(ax.patches); spine_side(ax, 0, 0, 180, 1.0)
    for pt in ax.patches[n0:]: pt.set_transform(tr)
    ax.text(-60, 160, "ON A LAP · side · open flat: the spine stops at 180°, so it can't fold\ndown under a keypress; it runs across both thighs (one trial on the first build)", fontsize=6.4, va="top")
    ax.text(-55, -115, "hips", fontsize=6, color="#7a6a55"); ax.text(340, -125, "knees →", fontsize=6, color="#7a6a55")
    # lap plan
    ax = axes(fig, [0.655, 0.47, 0.33, 0.44], (-60, 480), (-110, 520))
    thighs(ax, 36, -40, 1.0)
    spine_plan(ax, 0, 20, "kbc", 0.999)
    ax.text(206, -95, "▲ you (hips)", ha="center", fontsize=8, weight="bold", color="#333")
    ax.text(-60, 505, "ON A LAP · plan · open flat · K-Board C", fontsize=8.5, weight="bold")
    # keyboard range: keyboard trays only
    ax = axes(fig, [0.015, 0.04, 0.27, 0.40], (-10, 425), (-50, 420))
    for yy, k, cap in [(0, "nano", "below: smallest, nanoKEY2 · blocks fully out (≈ 40 each)"), (220, "xkey", "above: largest, Xkey 25 · blocks fully in (8)")]:
        ax.add_patch(FancyBboxPatch((0, yy), KW, SP_KT, boxstyle="round,pad=0,rounding_size=5", fc=WAL, ec=WALD, lw=0.8))
        ax.add_patch(Rectangle((4, yy + 4), INNER, SP_KT - 8, fc=BED, ec="none"))
        keyboard(ax, (KW - KB[k][1]) / 2, yy + SP_KT - 4 - KB[k][2], k, 1.0, label=True)
        end_blocks(ax, 0, yy + SP_KT - 4, k)
        brass_scale(ax, 0, yy + 0.5)
        ax.add_patch(Rectangle((0, yy + SP_KT), KW, 10, fc="#4a3020", ec="none"))
        ax.text(0, yy - 6 if k == "nano" else yy + SP_KT + 16, cap, fontsize=6.2, va="top" if k == "nano" else "bottom")
    ax.text(0, 412, "THE KEYBOARD RANGE · keyboard tray · the same blocks and scale as FALLBOARD", fontsize=8.5, weight="bold")
    # cable and pockets zoom
    ax = axes(fig, [0.30, 0.04, 0.36, 0.40], (0, 230), (110, 345))
    spine_plan(ax, 0, 0, "xkey", 1.0, md=2)
    lab = dict(fontsize=6.2, color="#111", bbox=dict(fc="#f6f2ea", ec="none", alpha=0.85, pad=1.2), zorder=20)
    ax.text(2, 341, "THE CABLE PATH AND THE POCKETS (left half, enlarged)", fontsize=8.5, weight="bold")
    ax.text(8, 312, "left pocket ≈ 59 × 105: charger", **lab)
    ax.text(30, 222, "cable strip 404 × 30: coiled cable + C-to-A adapter", **lab)
    ax.text(16, 168, f"open spine = the gutter ({SP_SPINE:.0f} wide): any rear socket, straight plug", **lab)
    ax.text(14, 125, "end block (left): 80 deep, foamed lip, thumb lock, 15 mm notch", **lab)
    # rear wall of the module tray
    ax = axes(fig, [0.675, 0.06, 0.315, 0.30], (-10, 425), (-45, 60))
    rear_wall(ax, 0, 0, 1.0, SP_MT_H, [(KW - MW) / 2 + 20, (KW - MW) / 2 + 184], 0,
              "THE MODULE TRAY'S OUTER WALL (from behind, open) · two windows on the module's\nport facets: power and charging reachable while it plays; unplug the phones before closing")
    ax.text(-10, 58, "REAR", fontsize=8.5, weight="bold")
    fig.savefig("../spine/spine-A-in-use.png", facecolor=BG)

def sp_frames():
    def f1(a):
        a.set_xlim(-10, 425); a.set_ylim(-10, 350); spine_plan(a, 0, 0, "xkey", 0.999)
        a.add_patch(Circle(((KW - MW) / 2 + 86, 344), 14, fc="none", ec=CORAL, lw=1.6, zorder=30))
    def f2(a):
        a.set_xlim(-10, 425); a.set_ylim(-10, 350); spine_plan(a, 0, 0, "xkey", 0.999)
        a.add_patch(Rectangle((10, SP_KT + SP_SPINE + 4), 390, 30, fc="none", ec=CORAL, lw=1.6, zorder=30))
    def f3(a):
        a.set_xlim(-10, 425); a.set_ylim(-10, 350); spine_plan(a, 0, 0, "xkey", 0.999)
        for x in (8, 404): a.add_patch(Circle((x, 99), 12, fc="none", ec=CORAL, lw=1.6, zorder=30))
    def f4(a):
        a.set_xlim(-30, 360); a.set_ylim(-20, 200); spine_side(a, 0, 0, 60, 1.0)
        a.text(160, 185, "swing the module tray over:\npanel down onto the keys", ha="center", fontsize=6.5)
    def f5(a):
        a.set_xlim(-10, 425); a.set_ylim(-60, 200); spine_closed(a, 0, 0)
    return [(f1, "Switch off at the rear (through the left window of the module tray)."),
            (f2, "Unplug the keyboard end. Coil the cable and the adapter into the cable strip."),
            (f3, "Thumb-lock both end blocks (they lock empty too)."),
            (f4, "Close: the module tray swings over, panel to keys. Knobs sit under the module's rim; rim foam pins the keyboard."),
            (f5, "Strap it. Into the backpack, spine up: you carry it by the spine, where the cable lives.")]

# ------------------------------------------------------------------- CLOTH sheets
def sheet_cloth():
    fig = sheet("CLOTH · in use: spread on a table, on a lap (two objects), the keyboard range, the cable and pocket, the rear",
                "One module and any keyboard in an 800 quilted square. Spread, the stitched outline (412 × 288) is the frame: it owns the outline and hosts the keys. A bench-and-table kit, honestly.", FOOT)
    ax = axes(fig, [0.015, 0.45, 0.32, 0.46], (-60, 900), (-120, 880))
    ax.add_patch(Rectangle((-50, -60), 940, 920, fc="#b79c7c", ec="none"))
    cloth_plan(ax, 20, 20, "xkey", 1.0)
    ax.text(420, -100, "▲ you", ha="center", fontsize=8, weight="bold", color="#333")
    ax.text(-60, 860, "SPREAD ON A TABLE · plan · Xkey 25", fontsize=8.5, weight="bold")
    ax.text(-60, 830, "on a bench the 800 cloth hangs over the front edge like a tablecloth: fine, but a table is its home", fontsize=6.2, color="#444")
    # lap: two objects
    ax = axes(fig, [0.345, 0.45, 0.30, 0.46], (-80, 760), (-120, 560))
    bench(ax, -60, -100, 820, 420)
    thighs(ax, 0, -40, 1.0)
    ax.text(700, 330, "bench front edge", ha="right", fontsize=6, color="#6b5640")
    keyboard(ax, 8, 200, "kbc", 1.0, z=6)
    ax.add_patch(Rectangle((400, 20), 360, 150, fc=CLOTHC, ec="none", alpha=0.9, zorder=4))
    module_plan(ax, 440, 40, 1.0, detail=1, z=5)
    ax.plot([8 + 325 * 0.78, 8 + 325 * 0.78, 415, 415, 580, 580], [200, 185, 185, 28, 28, 40], color="#c9c9c9", lw=1.3, zorder=7)
    ax.text(300, -100, "▲ you (hips)", ha="center", fontsize=8, weight="bold", color="#333")
    ax.text(-80, 540, "ON A LAP · plan · two objects: keyboard on the lap,", fontsize=8.5, weight="bold")
    ax.text(-80, 510, "module on the bench by your hip, on its folded cloth, on the 0.5 m cable", fontsize=6.2, color="#444")
    # keyboard range: small, large, chunky on the outline
    ax = axes(fig, [0.655, 0.45, 0.33, 0.46], (-20, 450), (-20, 1180))
    for yy, k, ph, cap in [(0, "nano", 320, "smallest: nanoKEY2 325 × 83"), (370, "xkey", 320, "largest slim: Xkey 25 388 × 135"),
                           (740, "mpk", 380, "chunky mini: MPK Mini IV 348 × 192 × 46 (only CLOTH carries it); the module sits past the stitched line")]:
        ax.add_patch(Rectangle((-10, yy), 432, ph, fc=CLOTHC, ec="none"))
        ax.add_patch(Rectangle((0, yy + 16), KW, FB_D, fc="none", ec=THREAD, lw=0.8))
        name, w, d, *_ = KB[k]
        extra = 0 if k != "mpk" else 48
        keyboard(ax, (KW - w) / 2, yy + 16 + 144 - d + extra, k, 1.0)
        module_plan(ax, (KW - MW) / 2, yy + 16 + 179 + extra - (0 if k != "mpk" else -4), 1.0, detail=1, z=5)
        ax.text(-10, yy + ph + 6, textwrap.fill(cap, 66), fontsize=6.0, va="bottom")
    fig.text(0.655, 0.925, "THE KEYBOARD RANGE · nothing holds the keys", fontsize=8.5, weight="bold")
    # pocket zoom
    ax = axes(fig, [0.015, 0.04, 0.40, 0.355], (0, 520), (0, 330))
    cloth_plan(ax, 0, 0, "xkey", 1.0)
    lab = dict(fontsize=6.4, color="#111", bbox=dict(fc="#f6f2ea", ec="none", alpha=0.85, pad=1.2), zorder=20)
    ax.text(250, 60, "sewn pocket 200 × 150: cable, C-to-A adapter, spare, and the charger\n(the only kit that carries one)", **lab)
    ax.text(250, 250, "live run: keyboard socket (rear or end) → host port on the module's axis,\na few centimetres over the cloth, never across hands or speaker", **lab)
    fig.text(0.015, 0.405, "THE CABLE AND THE POCKET (front-left corner, enlarged)", fontsize=8.5, weight="bold")
    # rear: module free
    ax = axes(fig, [0.44, 0.06, 0.54, 0.30], (-20, 560), (-60, 70))
    ax.add_patch(FancyBboxPatch((0, 0), MW, MOD_H, boxstyle="round,pad=0,rounding_size=3", fc=SHELL, ec=SHELLD, lw=0.6))
    ax.add_patch(Rectangle((MW - CROWN_X1, 0), CROWN_X1 - CROWN_X0, MOD_H, fc=SHELLD, ec="none"))
    for x0, ports in ((20, ["phones", "line", "in", "out"]), (MW - 96, ["power", "usb-c", "tune", "split"])):
        ax.add_patch(Rectangle((x0, 5), 76, 24, fc="#4f3220", ec="#3a2516", lw=0.5))
        for j, n in enumerate(ports):
            ax.add_patch(Circle((x0 + 9.5 + j * 19, 16), 2.8, fc="#111", ec="#888", lw=0.4))
            ax.text(x0 + 9.5 + j * 19, 26, n, ha="center", fontsize=5.0, color=CREAM)
    ax.text(0, 62, "REAR · the module's own rear, nothing in front of it: every port open while it plays", fontsize=8.5, weight="bold")
    ax.text(300, 30, "CLOTH has no wall, so the rear needs nothing.\nThe module's two port facets face away from you on the cloth;\nphones and line leave over the back edge of the outline.", fontsize=6.6, va="top")
    fig.savefig("../cloth/cloth-A-in-use.png", facecolor=BG)

def cloth_bundle(ax, ox, oy, s=1.0):
    ax.add_patch(FancyBboxPatch((ox, oy), 400 * s, 150 * s, boxstyle=f"round,pad=0,rounding_size={30*s}", fc=CLOTHC, ec="#2c3533", lw=0.8))
    ax.add_patch(Ellipse((ox + 200 * s, oy + 150 * s), 90 * s, 50 * s, fc=CLOTHL, ec="#2c3533", lw=0.6))
    for cx in (-25, 25):
        ax.add_patch(Circle((ox + (200 + cx) * s, oy + 170 * s), 8 * s, fc=BRASS, ec="none"))
    ax.text(ox + 200 * s, oy + 70 * s, "knotted bundle with an Xkey", ha="center", fontsize=6.4, color=THREAD)

def cl_frames():
    def f1(a):
        a.set_xlim(-10, 810); a.set_ylim(-10, 810); cloth_plan(a, 0, 0, "xkey", 1.0, words=False)
        a.add_patch(Rectangle((35, 35), 210, 160, fc="none", ec=CORAL, lw=1.6, zorder=30))
    def f2(a):
        a.set_xlim(-10, 810); a.set_ylim(-10, 810)
        a.add_patch(Rectangle((0, 0), 800, 800, fc=CLOTHC)); a.add_patch(Rectangle((246, 330), 308, 125, fc=CLOTHL, ec="#6d7a75"))
        module_plan(a, 260, 340, 1.0, detail=1, z=3); a.text(400, 300, "module in its sleeve, panel up, centre", ha="center", fontsize=6.4, color=THREAD)
    def f3(a):
        a.set_xlim(-10, 810); a.set_ylim(-10, 810)
        a.add_patch(Rectangle((0, 0), 800, 800, fc=CLOTHC)); a.add_patch(Rectangle((246, 330), 308, 125, fc=CLOTHL, ec="#6d7a75"))
        a.add_patch(FancyBboxPatch((206, 325), 388, 135, boxstyle="round,pad=0,rounding_size=4", fc=SILVER, ec="#666", zorder=4))
        a.text(400, 392, "keyboard keys-down\non the quilted sleeve", ha="center", fontsize=6.4, zorder=5)
    def f4(a):
        a.set_xlim(-10, 810); a.set_ylim(-10, 810)
        a.add_patch(Polygon([(400, 0), (800, 400), (400, 800), (0, 400)], fc=CLOTHC))
        a.add_patch(FancyBboxPatch((206, 325), 388, 135, boxstyle="round,pad=0,rounding_size=4", fc=CLOTHL, ec="#2c3533", zorder=4))
    def f5(a):
        a.set_xlim(-10, 420); a.set_ylim(-60, 260); cloth_bundle(a, 0, 0)
    return [(f1, "Cable, adapter and charger into the sewn pocket."),
            (f2, "Module into its sleeve at the cloth's centre, panel up (the knobs sit under its rim)."),
            (f3, "Keyboard keys-down on the sleeve's quilted top: the keys bear only the keyboard's own weight."),
            (f4, "Fold two opposite corners over the pair."),
            (f5, "Tie the other two corners (brass weights) into the handle knot. Into the backpack.")]
if __name__ == "__main__":
    which = sys.argv[1:] or ["module", "fallboard", "spine", "cloth"]
    if "module" in which: sheet_module()
    if "fallboard" in which:
        sheet_fallboard()
        closed_sheet("FALLBOARD", "FALLBOARD · closed and packing: size, weight, and the pack-up order",
                     "Closed it's one board: about a laptop's footprint and 2½ laptops thick. Weights are eng's estimates; the owner set no weight target.",
                     lambda ax, x, y: fb_closed(ax, x, y), (KW, FB_D), MOD_H + 8, 48, None, fb_frames(), "PACKING, in the tea-box order (unpack is the reverse)")
    if "spine" in which:
        sheet_spine()
        closed_sheet("SPINE", "SPINE · closed and packing: size, weight, and the pack-up order",
                     "Closed it's a box like a thick hardback, a little wider than the keyboard: the smallest rigid kit. Weights are eng's estimates; the owner set no weight target.",
                     lambda ax, x, y: spine_closed(ax, x, y), (KW, SP_KT), SP_SPINE, 61, None, sp_frames(), "PACKING, in the tea-box order (unpack is the reverse)")
    if "cloth" in which:
        sheet_cloth()
        closed_sheet("CLOTH", "CLOTH · wrapped and packing: size, weight, and the wrap order",
                     "Wrapped it's a soft bundle the size of the keyboard you bring (≈ 400 × 150 × 65 with an Xkey; ≈ 335 × 115 × 60 with a nanoKEY2; the module alone ≈ 300 × 115 × 45). The lightest kit.",
                     lambda ax, x, y: cloth_bundle(ax, x, y), (400, 150), 65, None, None, cl_frames(), "WRAPPING, in a fixed order like a tea set (unwrap is the reverse)")
