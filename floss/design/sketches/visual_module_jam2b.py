# floss module jam, turn 2 (visual): proportions riff + the family on a shelf. Rough, to scale (mm).
# Run: python3 visual_module_jam2b.py  -> visual-module-jam2b-proportions-shelf.png
import textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle
plt.rcParams["font.family"] = "Inter"
WAL="#6b4429"; WALD="#563520"; CREAM="#f1ebdd"; BLACK="#1d1b19"; CORAL="#f0806a"; BRASS="#c9a24a"; GREY="#8a8276"; BG="#f6f2ea"
OAT="#d9cdb4"; BED="#2e2622"

fig = plt.figure(figsize=(16.5, 11.7), dpi=150); fig.patch.set_facecolor(BG)
fig.text(0.03, 0.965, "floss · module jam turn 2 · visual · proportions against the keyboards, and the family on a shelf (rough, to scale)", fontsize=13, weight="bold")

# ---------- A: three module proportions over the keyboard envelope ----------
ax = fig.add_axes([0.03, 0.50, 0.58, 0.42]); ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-10, 1330); ax.set_ylim(-120, 330)
ax.text(0, 315, "A · three module proportions, each drawn behind the slim keyboard envelope (dashed: Xkey 388 × 135; dotted: nanoKEY2 / K-Board 325 × 84)", fontsize=8.5, weight="bold")
mods = [("SLAB · 400 × 133 · 3 : 1", 400, 133, "two rows; spare area → speaker box\n≈ 150 × 110 × 20 ≈ 330 cm³ (systems' calc).\nFits SPINE: boards the same size."),
        ("RAIL · 400 × 80 · 5 : 1", 400, 80, "one row of 14; grille strip behind.\nFits FALLBOARD. Breaks the drawn 3 : 1\non purpose: a single line needs it."),
        ("BLOCK · 270 × 100 · 2.7 : 1", 270, 100, "eng's minimum. Narrower than every\nkeyboard: the guest sticks out.\nFits CLOTH (two packages, meets T4).")]
x = 0
for name, w, d, note in mods:
    kbtop = 0
    ax.add_patch(Rectangle((x+(400-388)/2, kbtop-135), 388, 135, fc="none", ec=GREY, lw=0.7, ls=(0, (4, 3))))
    ax.add_patch(Rectangle((x+(400-325)/2, kbtop-84), 325, 84, fc="none", ec=GREY, lw=0.7, ls=(0, (1, 2))))
    mx = x + (400-w)/2
    ax.add_patch(FancyBboxPatch((mx, 4), w, d, boxstyle="round,pad=0,rounding_size=10", fc=WAL, ec=WALD, lw=0.8))
    ax.add_patch(FancyBboxPatch((mx+5, 9), w-10, d-10, boxstyle="round,pad=0,rounding_size=6", fc=CREAM, ec="none"))
    rows = 2 if d > 110 else 1
    n = 14 if rows == 1 else 8
    if w < 300: n, rows = 8, 2
    pitch = (w-40)/n
    for r in range(rows):
        for i in range(n):
            cx = mx+20+pitch*(i+0.5); cy = 4+d-(28 if rows == 1 else 30+r*32)
            if rows == 1: cy = 4+30
            ax.add_patch(Circle((cx, cy), 7.45, fc=CORAL if (i == 3 and r == 0) else BLACK, ec="none"))
    ax.text(x+200, d+16, name, ha="center", fontsize=8, weight="bold")
    ax.text(x+200, -150+28, note, ha="center", va="top", fontsize=6.6, color="#444")
    x += 460

# ---------- B: same height on the shelf ----------
ax = fig.add_axes([0.63, 0.50, 0.35, 0.42]); ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-40, 420); ax.set_ylim(-60, 470)
ax.text(-40, 455, "B · 'same height on the shelf': the family standard I'd add", fontsize=8.5, weight="bold")
ax.add_patch(Rectangle((-40, -8), 460, 8, fc="#8f7a62", ec="none"))
books = [("floss", 38, CREAM, CORAL), ("big energy", 46, "#e8dfc9", BRASS), ("port-a-poly", 52, "#e4d8c0", BLACK)]
bx = 20
for name, t, col, acc in books:
    ax.add_patch(FancyBboxPatch((bx, 0), t, 400, boxstyle="round,pad=0,rounding_size=4", fc=WAL, ec=WALD, lw=0.8))
    ax.add_patch(Rectangle((bx+4, 290), t-8, 85, fc=col, ec="none"))
    ax.add_patch(Rectangle((bx+4, 276), t-8, 4, fc=acc, ec="none"))
    for c in (0, 392):
        ax.add_patch(Rectangle((bx, c), t, 8, fc=BRASS, ec="none"))
    ax.text(bx+t/2, 332, name, rotation=90, ha="center", va="center", fontsize=6.5, color=WALD)
    bx += t + 6
# a real book for scale
ax.add_patch(Rectangle((bx+10, 0), 30, 297, fc="#7d8a8f", ec="none")); ax.text(bx+25, 150, "A4 book", rotation=90, ha="center", va="center", fontsize=6.5, color="white")
ax.add_patch(Rectangle((bx+46, 0), 22, 240, fc="#a3967f", ec="none"))
ax.text(250, 395, textwrap.fill("Every kit closes to 400 tall when stood on end, spine out: brass corners (surveyor's box), cream label, one accent per instrument. "
        "Thickness and depth vary with each module's parts; the 400 doesn't. Fixing one dimension (the keyboard's width, a real reason) lets the keyboard bed, lid hinge "
        "and cable be the same part on every instrument. It sharpens systems' 'fix the connections, not the sizes': fix the connections and the one size the keyboard sets.", 44),
        fontsize=6.6, va="top", color="#333")
ax.text(200, -40, "spine thicknesses illustrative, not calculated", ha="center", fontsize=6.5, color=GREY)

# ---------- C: kit verdicts ----------
ax = fig.add_axes([0.03, 0.03, 0.94, 0.42]); ax.axis("off")
rows = [
("FALLBOARD (new) · lead", "Rail + keyboard bed + one lid. One plane, piano form. Owns the outline best; lid = shade, stand, lamp. Separate sheet: visual-module-jam2a-fallboard.png."),
("SPINE · keep, sharpen", "Systems' book with SLAB boards. Add: brass book corners, a spine label (shelf), the printed card inside the cover, the brass split target instead of the ribbon, "
                          "two adjustable straps on the keyboard board instead of four sliding photo corners (fewer parts, takes 83–135 depth). Its gift is the closed stack (400 × ≈ 140 × 55)."),
("CLOTH · keep as the two-package answer", "BLOCK module with its knobs sunk below a raised walnut rim (no knob above the rim, so a cloth carry can't snap one). The spread cloth is the frame: "
                          "it owns the outline when open, the way FALLBOARD's tray does. Coated bookcloth outside, washable quilted liner. The only kit for the chunky minis."),
("LAMP · kill as a kit, keep the light", "The wedge has nowhere to stand on a lap and no good carry. The light that falls on the keys moves into FALLBOARD's lid (and SPINE's standing state)."),
("TETHER · kill as a kit, keep the strap", "Two bare objects: no protection, no spatial mapping. The strap becomes an accessory on the S4 inserts of any kit (crossbody carry), and the cable-in-the-handle idea stays in SPINE."),
("BACKBONE · agree with the kill", "A jaw on unknown edges is a fitted dock by another name."),
]
y = 0.98
ax.text(0, y, "C · the kits, after turn 2", fontsize=9.5, weight="bold", transform=ax.transAxes); y -= 0.09
for h, b in rows:
    ax.text(0.0, y, h, fontsize=8.8, weight="bold", va="top", transform=ax.transAxes)
    ax.text(0.25, y, textwrap.fill(b, 140), fontsize=8.2, va="top", transform=ax.transAxes, color="#333")
    y -= 0.15
fig.text(0.03, 0.012, "floss · module jam turn 2 · visual · rough 2-D sketch, not a render", fontsize=7, color=GREY)
fig.savefig("visual-module-jam2b-proportions-shelf.png", facecolor=BG)
