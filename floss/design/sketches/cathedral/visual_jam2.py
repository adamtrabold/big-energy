# floss CATHEDRAL-cues jam, turn 2 (visual). Rough 2-D concept sketches, mm, not renders.
# Draws (SystemRandom): Oblique "Abandon normal instruments", "Water"; fields sledge runner, pencil case,
# font/basin; section primitive TEARDROP; angle 25 deg; constraint "two identical halves".
# Run: python3 visual_jam2.py -> cathedral-jam2-*.png
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle, FancyBboxPatch, Arc, Wedge
WAL="#6b4429"; WALD="#4e311d"; CREAM="#f1ebdd"; BLACK="#1d1b19"; BRASS="#c9a24a"; RED="#b8322a"
GREY="#8a8276"; BG="#f6f2ea"; KB="#2b2b2b"
T25 = math.radians(25)

def fig_new(title, sub):
    fig = plt.figure(figsize=(16, 10), dpi=110); fig.patch.set_facecolor(BG)
    fig.text(0.02, 0.965, title, fontsize=13, weight="bold")
    fig.text(0.02, 0.937, sub, fontsize=9, color="#444")
    fig.text(0.02, 0.01, "floss · CATHEDRAL-cues jam turn 2 · visual · rough concept sketch, to scale in mm, nothing measured · draws: teardrop · 25° · 'Water' · sledge runner · pencil case · font", fontsize=7, color=GREY)
    return fig
def ax_new(fig, rect, xl, yl, title):
    ax = fig.add_axes(rect); ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(*xl); ax.set_ylim(*yl)
    ax.set_title(title, fontsize=9.5, loc="left", weight="bold"); return ax
def ground(ax, x0, x1, y=0):
    ax.plot([x0, x1], [y, y], color=GREY, lw=0.8)
    for x in range(int(x0), int(x1), 8): ax.plot([x, x-4], [y, y-4], color=GREY, lw=0.4)
def rot(pts, a, about=(0, 0)):
    c, s = math.cos(a), math.sin(a); ox, oy = about
    return [(ox+(x-ox)*c-(y-oy)*s, oy+(x-ox)*s+(y-oy)*c) for x, y in pts]

# ---- DROP section (body frame): flat base, pipe r at the back, panel at 25 deg tangent to the pipe ----
R = 36; CX = 110; CY = R
PX, PY = CX - R*math.sin(T25), CY + R*math.cos(T25)
Y0 = PY - PX*math.tan(T25)            # front lip height
LAND = 20                              # half-chord of the rear land
def drop_outline(n=60):
    pts = [(4, 0)]
    a_land = math.degrees(math.asin(LAND/R))
    # bottom of pipe -> rear land (flat) -> up to the panel tangent
    for i in range(n+1):
        a = math.radians(-90 + (90 - a_land)*i/n); pts.append((CX+R*math.cos(a), CY+R*math.sin(a)))
    for i in range(n+1):
        a = math.radians(a_land + (90+25-a_land)*i/n); pts.append((CX+R*math.cos(a), CY+R*math.sin(a)))
    pts += [(3, Y0+1.4), (0, Y0-3), (0, 4)]
    return pts
def draw_drop(ax, a=0.0, about=(0, 0), dx=0, dy=0, keyboard=False, label=None):
    pts = [(x+dx, y+dy) for x, y in rot(drop_outline(), a, about)]
    ax.add_patch(Polygon(pts, closed=True, fc=WAL, ec=WALD, lw=1))
    # cream plate on the panel line
    p0 = (6, Y0+0.6+6*math.tan(T25)); p1 = (PX-4, PY-4*math.tan(T25)+0.6)
    pl = [(x+dx, y+dy) for x, y in rot([p0, p1], a, about)]
    ax.plot([pl[0][0], pl[1][0]], [pl[0][1], pl[1][1]], color=CREAM, lw=3.2, solid_capstyle="butt")
    # knobs: two rows on the panel
    for t in (22, 58):
        bx, by = t*math.cos(T25), Y0 + t*math.sin(T25)
        k = [(bx - 5*math.sin(T25)*0, by)]
        kp = rot([(bx-4*math.sin(T25)+0, by+1), (bx-4*math.sin(T25)-8*math.sin(T25), by+1+8*math.cos(T25)),
                  (bx+8*math.cos(T25)-8*math.sin(T25), by+1+8*math.cos(T25)+8*math.sin(T25)), (bx+8*math.cos(T25), by+1+8*math.sin(T25))], a, about)
        ax.add_patch(Polygon([(x+dx, y+dy) for x, y in kp], fc=BLACK, ec=BLACK))
    # clerestory: lancet slots on the pipe's upper front (drivers inside the pipe)
    for ang in (40, 52, 64, 76):
        q = rot([(CX+R*math.cos(math.radians(ang)), CY+R*math.sin(math.radians(ang)))], a, about)[0]
        ax.add_patch(Circle((q[0]+dx, q[1]+dy), 1.3, fc=BLACK, ec=BLACK))
    # brass runners under the base (wear strips) / rear land
    r1 = rot([(14, -0.2), (100, -0.2)], a, about)
    ax.plot([r1[0][0]+dx, r1[1][0]+dx], [r1[0][1]+dy, r1[1][1]+dy], color=BRASS, lw=2.4)
    al = math.asin(LAND/R)
    r2 = rot([(CX+R*math.cos(-al)+0.3, CY-LAND+3), (CX+R*math.cos(al)+0.3, CY+LAND-3)], a, about)
    ax.plot([r2[0][0]+dx, r2[1][0]+dx], [r2[0][1]+dy, r2[1][1]+dy], color=BRASS, lw=2.4)
    # port mouth (end face) at the pipe's centre
    pc = rot([(CX, CY)], a, about)[0]
    ax.add_patch(Circle((pc[0]+dx, pc[1]+dy), 7, fc=WALD, ec=BLACK, lw=0.6))
    for rr in (12, 18, 25): ax.add_patch(Circle((pc[0]+dx, pc[1]+dy), rr, fc="none", ec=WALD, lw=0.5))
    if keyboard:
        ax.add_patch(Rectangle((6+dx, -17+dy), 98, 16, fc=KB, ec=BLACK))
        ax.text(55+dx, -9+dy, "slim keyboard, k2 (ends)", color="white", ha="center", va="center", fontsize=6)
    if label: ax.text(dx+60, dy-28 if keyboard else dy-14, label, ha="center", fontsize=8)

# ---------------- sheet 1: sections ----------------
fig = fig_new("Sections: WEDGE (systems, 14°) sharpened into DROP (25°, drawn), and the hinge-free cover",
              "End elevations, same scale. Player on the left in every pose. Walnut = printed body, cream = the framed plate, brass = printed-metal runners (wear strips), black = knobs. Nothing measured.")
ax = ax_new(fig, [0.02, 0.52, 0.30, 0.38], (-10, 150), (-35, 90), "1  WEDGE (systems turn 1): 35 front, 61 back, 14°")
w = [(0, 0), (105, 0), (105, 61), (0, 35)]
ax.add_patch(Polygon(w, fc=WAL, ec=WALD)); ax.plot([4, 101], [35+4*math.tan(math.radians(14))+0.6, 35+101*math.tan(math.radians(14))+0.6], color=CREAM, lw=3)
ground(ax, -10, 140); ax.text(52, -18, "honest, but the end face is a trapezoid:\nthe silhouette any synth has", ha="center", fontsize=8)

ax = ax_new(fig, [0.33, 0.52, 0.34, 0.38], (-10, 160), (-40, 90), "2  DROP pose 1: the panel at 25° by shape")
draw_drop(ax, keyboard=True, label="")
ground(ax, -10, 155, y=-17)
ax.text(70, -33, f"lip {Y0:.0f} · pipe Ø{2*R} at the back = speaker box + port + hand grip · brass runner = foot", ha="center", fontsize=7.5)
ax.annotate("clerestory: lancet slots in the pipe,\ndrivers behind, firing over the plate", (CX+R*math.cos(math.radians(58)), CY+R*math.sin(math.radians(58))), (95, 86), fontsize=7, arrowprops=dict(arrowstyle="-", color=GREY, lw=0.6))
ax.annotate("end grain rings round\nthe port mouth", (CX, CY), (128, 2), fontsize=7, arrowprops=dict(arrowstyle="-", color=GREY, lw=0.6))

ax = ax_new(fig, [0.68, 0.52, 0.30, 0.38], (-40, 120), (-45, 145), "3  DROP pose 2: on its rear land, panel ≈ 65°, player on the right")
LX = CX + math.sqrt(R**2 - LAND**2)
draw_drop(ax, a=math.radians(-90), about=(LX, CY), dx=40-LX, dy=-CY)
ground(ax, -40, 115, y=0 - 0)
ax.text(40, -30, "panel faces the other way (≈ 90 − 25): retable / shelf / friend across the table.\nCost: the clerestory now fires at the table. COM must sit in the land's 40 mm: UNVERIFIED", ha="center", fontsize=7.5)

# cover as stand (pencil-tin lid) with a flat slab module
ax = ax_new(fig, [0.02, 0.07, 0.46, 0.38], (-10, 260), (-25, 85), "4  CASKET: TRIPTYCH without the hinge (pencil-tin lid = stand; absorbs SLED)")
# packed
ax.add_patch(FancyBboxPatch((0, 0), 108, 30, boxstyle="round,pad=0,rounding_size=6", fc=WAL, ec=WALD))
ax.add_patch(FancyBboxPatch((-2, 22), 112, 14, boxstyle="round,pad=0,rounding_size=5", fc=WALD, ec=BLACK, lw=0.6))
for i in range(9): ax.plot([10+i*11, 10+i*11], [36, 36+3+abs(4-i)*1.2], color=BRASS, lw=1)
ax.text(54, -12, "packed: lid over the plate;\nthe lid's face carries his pipe façade", ha="center", fontsize=7.5)
# playing: lid flipped, ledge inside, module sits in at 25deg
ox = 135
ax.add_patch(FancyBboxPatch((ox-2, 0), 112, 14, boxstyle="round,pad=0,rounding_size=5", fc=WALD, ec=BLACK, lw=0.6))
ax.add_patch(Polygon([(ox+70, 14), (ox+108, 14), (ox+108, 30)], fc=WALD, ec=BLACK, lw=0.6))
slab = rot([(0, 0), (108, 0), (108, 30), (0, 30)], T25, (0, 0))
ax.add_patch(Polygon([(x+ox+8, y+12) for x, y in slab], fc=WAL, ec=WALD))
c = rot([(4, 30.6), (104, 30.6)], T25, (0, 0)); ax.plot([c[0][0]+ox+8, c[1][0]+ox+8], [c[0][1]+12, c[1][1]+12], color=CREAM, lw=3)
ground(ax, ox-8, ox+125)
ax.text(ox+55, -14, "playing: lid flipped, a printed ledge seats the module at 25°;\nflat without the lid. Keyboard rides on the lid (k3).", ha="center", fontsize=7.5)
fig.savefig("cathedral-jam2-sections.png", facecolor=BG); plt.close(fig)

# ---------------- sheet 2: ROSE ----------------
fig = fig_new("ROSE: differs in kind. The plan is the rose window; the panel reads like one big knob scale",
              "Plan Ø 190 (drawn, not derived yet). Controls on one 300° arc from 7 o'clock (synth) to 5 o'clock (out), the CATHEDRAL marking system's own sweep, round one central window. Signal order = clockwise.")
ax = ax_new(fig, [0.02, 0.06, 0.52, 0.84], (-110, 110), (-110, 110), "plan (panel face)")
ax.add_patch(Circle((0, 0), 95, fc=WAL, ec=WALD, lw=1.2))
ax.add_patch(Circle((0, 0), 88, fc=CREAM, ec=WALD, lw=0.6))
# central window with lancets
for i in range(-7, 8):
    x = i*3.0; h = math.sqrt(max(0, 23**2 - x**2))
    ax.add_patch(Rectangle((x-0.9, -h), 1.8, 2*h, fc=BLACK))
groups = [("oct L · tone L", 2, BLACK), ("attack · release", 2, BLACK), ("hold", 1, BLACK), ("drift · tone", 2, BLACK),
          ("depth", 1, RED), ("echo · time · tap", 3, BLACK), ("reverb", 1, BLACK), ("volume", 1, BLACK), ("tone R · oct R", 2, BLACK)]
n = sum(g[1] for g in groups) + len(groups) - 1
start, sweep = 240, 300               # 7 o'clock (240 deg from +x) clockwise 300 deg
step = sweep / (n - 1); k = 0
for name, cnt, col in groups:
    angs = []
    for j in range(cnt):
        a = math.radians(start - step*k); angs.append(a)
        ax.add_patch(Circle((66*math.cos(a), 66*math.sin(a)), 7.2 if name != "hold" else 6, fc=col, ec=BLACK))
        k += 1
    am = sum(angs)/len(angs)
    ax.text(83*math.cos(am)*0.98, 83*math.sin(am)*0.98, name, fontsize=6.5, ha="center", va="center",
            rotation=math.degrees(am) - 90 if math.sin(am) > -0.2 else math.degrees(am) + 90)
    k += 1
ax.add_patch(Rectangle((-5, -97), 10, 4, fc=BLACK)); ax.text(0, -104, "USB-C host at 6 o'clock, toward the keyboard", ha="center", fontsize=7)
ax.text(0, 36, "rose window (one driver? E wants two: eng)", ha="center", fontsize=7, color=GREY)

ax = ax_new(fig, [0.56, 0.50, 0.42, 0.40], (-120, 120), (-20, 110), "side: a drum cut at an angle (font on its foot)")
for ang, ls, lab in ((25, "-", "25° (the draw): back rises ≈ 80"), (12, "--", "12°: ≈ 40")):
    a = math.radians(ang)
    top = [(-95*math.cos(a), 28 + 0), (95*math.cos(a), 28 + 190*math.sin(a))]
    poly = [(-60, 0), (60, 0), top[1], top[0]]
    if ang == 25: ax.add_patch(Polygon(poly, fc=WAL, ec=WALD))
    ax.plot([top[0][0], top[1][0]], [top[0][1]+0.8, top[1][1]+0.8], color=CREAM if ang == 25 else GREY, lw=3 if ang == 25 else 1, ls=ls)
    ax.text(70, top[1][1] + 4, lab, fontsize=7)
ax.plot([-60, 60], [0, 0], color=BRASS, lw=3); ground(ax, -115, 115)
ax.text(0, -14, "brass foot ring (printed metal, the wear surface)", ha="center", fontsize=7)
ax = ax_new(fig, [0.56, 0.06, 0.42, 0.38], (-10, 400), (-10, 120), "carry: the honest weak point")
ax.add_patch(Rectangle((0, 0), 360, 16, fc=KB)); ax.text(180, 8, "keyboard 325–388", color="white", ha="center", va="center", fontsize=7)
ax.add_patch(Circle((180, 16+95), 95, fc="none", ec=WALD, lw=1, ls="--"))
ax.text(180, 60, "a disc doesn't share an edge with a bar:\nno end-held carry without a strap or a\nseparate carrier. Bag: Ø190 × 40–80 puck.", ha="center", fontsize=7.5)
fig.savefig("cathedral-jam2-rose.png", facecolor=BG); plt.close(fig)
print("lip", round(Y0, 1), "back", round(2*R, 1))
