# floss module jam, turn 2 (visual): FALLBOARD, the piano-form kit. Rough, to scale (mm).
# Run: python3 visual_module_jam2a.py  -> visual-module-jam2a-fallboard.png
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Polygon
plt.rcParams["font.family"] = "Inter"
WAL="#6b4429"; WALD="#563520"; CREAM="#f1ebdd"; BLACK="#1d1b19"; CORAL="#f0806a"; BRASS="#c9a24a"
GREY="#8a8276"; BED="#2e2622"; WHITEKB="#e9e7e2"; SILVER="#c8c8c6"; BG="#f6f2ea"

fig = plt.figure(figsize=(16.5, 11.7), dpi=150); fig.patch.set_facecolor(BG)
fig.text(0.03, 0.965, "floss · module jam turn 2 · visual · FALLBOARD: the piano form (rough, to scale, 2026-11-22)", fontsize=13, weight="bold")
fig.text(0.03, 0.94, "A full-width rail behind any slim keyboard on a dark bed; one lid over both. Open, the lid stands as shade, music stand or lamp. Closed, it's one flat board about a 16-inch laptop's footprint.", fontsize=9.5, color="#444")

W = 400; RAIL = 80; TRAY = 150

def rail(ax, x0, y0, kb_label=True):
    ax.add_patch(FancyBboxPatch((x0, y0), W, RAIL, boxstyle="round,pad=0,rounding_size=10", fc=WAL, ec=WALD, lw=0.8))
    ax.add_patch(FancyBboxPatch((x0+5, y0+5), W-10, RAIL-10, boxstyle="round,pad=0,rounding_size=6", fc=CREAM, ec="none"))
    # grille strip at the back
    for i in range(46):
        ax.plot([x0+20+i*7.8, x0+20+i*7.8], [y0+RAIL-22, y0+RAIL-11], color="#b9ae99", lw=1.1)
    # single row: L hands | shared | R hands, signal order left->right in the middle
    labels = ["oct L", "attack", "release", "press", "tone", "shimmer", "depth", "echo", "time", "tap", "reverb", "volume", "hold", "oct R"]
    n = len(labels); pitch = 25.5; start = x0 + W/2 - pitch*(n-1)/2
    for i, l in enumerate(labels):
        cx = start + i*pitch; cy = y0 + 28
        r = 8.5 if l.startswith("oct") else 7.45
        col = CORAL if l == "press" else (BRASS if l in ("tap", "hold") else BLACK)
        ax.add_patch(Circle((cx, cy), r, fc=col, ec="none"))
        if l not in ("tap", "hold"):
            ax.plot([cx, cx], [cy, cy+r*0.8], color="white", lw=0.9)
        ax.text(cx, cy+r+3, l, ha="center", fontsize=5.2, color="#333")
    # group rules (3 groups)
    for gx in (start + 0.5*pitch, start + 3.5*pitch):
        pass
    ax.text(x0+W-12, y0+RAIL-6.5, "floss", ha="right", fontsize=6, style="italic", color=WALD)
    # brass split target on the front edge
    return start, pitch

def tray(ax, x0, y0, kb, kbw, kbd, kbcol, keycol):
    ax.add_patch(FancyBboxPatch((x0, y0), W, TRAY, boxstyle="round,pad=0,rounding_size=10", fc=WAL, ec=WALD, lw=0.8))
    ax.add_patch(Rectangle((x0+6, y0+6), W-12, TRAY-6, fc=BED, ec="none"))
    kx = x0 + (W-kbw)/2; ky = y0 + TRAY - kbd - 12   # keyboard pushed back to a 12 mm cable gutter in front of the rail
    ax.add_patch(FancyBboxPatch((kx, ky), kbw, kbd, boxstyle="round,pad=0,rounding_size=4", fc=kbcol, ec="#666", lw=0.5))
    nwhite = 15; kw = (kbw-30)/nwhite; k0 = kx+15
    keyd = kbd*0.62
    for i in range(nwhite):
        ax.add_patch(Rectangle((k0+i*kw, ky+3), kw, keyd, fc=keycol[0], ec="#888", lw=0.4))
    for i in [0,1,3,4,5,7,8,10,11,12]:
        ax.add_patch(Rectangle((k0+(i+1)*kw-kw*0.3, ky+3+keyd*0.38), kw*0.6, keyd*0.62, fc=keycol[1], ec="none"))
    ax.text(x0+W/2, y0+10, kb, ha="center", fontsize=5.5, color="#777")
    # elastic bands across
    for bx in (x0+40, x0+W-40):
        ax.add_patch(Rectangle((bx-4, y0+6), 8, TRAY-6, fc="#3b3330", ec="none", alpha=0.85))
    # B|C position on this keyboard (keys 8th white is C4 if lowest key is C3)
    bc = k0 + 7*kw
    return bc

# ---------- A: plan, open, two keyboards ----------
for j, (kb, kbw, kbd, kbcol, keys) in enumerate([("CME Xkey 25 · 388 × 135", 388, 135, SILVER, (WHITEKB, BLACK)),
                                                  ("Korg nanoKEY2 · 325 × 83", 325, 83, BLACK, (BLACK, "#555"))]):
    ax = fig.add_axes([0.03 + j*0.31, 0.47, 0.30, 0.43]); ax.set_aspect("equal"); ax.axis("off")
    ax.set_xlim(-20, 420); ax.set_ylim(-60, 290)
    bc = tray(ax, 0, 0, kb, kbw, kbd, kbcol, keys)
    start, pitch = rail(ax, 0, TRAY)
    # target rail on rail front edge + slider over B|C
    ax.plot([20, W-20], [TRAY+2.5, TRAY+2.5], color=BRASS, lw=1.0)
    for t in range(0, 361, 10):
        ax.plot([20+t, 20+t], [TRAY+1, TRAY+(4 if t % 50 == 0 else 2.5)], color=BRASS, lw=0.4)
    ax.add_patch(Polygon([[bc-5, TRAY+6], [bc+5, TRAY+6], [bc, TRAY-2]], fc=BRASS, ec="#8a6d27", lw=0.6))
    # host port at the centre of the rail's front face + coiled cable
    ax.add_patch(Rectangle((W/2-5, TRAY-1.5), 10, 3, fc="#222", ec="none"))
    ax.text(W/2, -14, "plan, open (to scale)", ha="center", fontsize=8, color="#444")
    ax.text(W/2, -28, "footprint 400 × 230 (open and closed alike)", ha="center", fontsize=7.5, color=GREY)
    ax.annotate("brass split target, slid over\ntoday's B | C (graduated rail)", xy=(bc, TRAY+4), xytext=(bc-130 if j == 0 else bc+40, TRAY+125),
                fontsize=6.5, color="#6b5320", arrowprops=dict(arrowstyle="-", color=BRASS, lw=0.6))
    if j == 0:
        ax.annotate("host port: centre of the rail's front face\nin a 12 mm cable gutter (shortest worst-case\nreach to a socket anywhere on the keyboard back edge)", xy=(W/2, TRAY-1),
                    xytext=(215, 262), fontsize=6.2, color="#333", arrowprops=dict(arrowstyle="-", color="#333", lw=0.5))
        ax.annotate("dark coated bookcloth bed:\nthe guest's plastic edge disappears", xy=(12, 30), xytext=(-18, -50), fontsize=6.2, color="#333",
                    arrowprops=dict(arrowstyle="-", color="#333", lw=0.5))
    else:
        ax.annotate("smaller keyboard: same outline,\nmore bed showing in front", xy=(200, 25), xytext=(250, -52), fontsize=6.2, color="#333",
                    arrowprops=dict(arrowstyle="-", color="#333", lw=0.5))

# ---------- B: side sections, three states ----------
ax = fig.add_axes([0.66, 0.47, 0.32, 0.43]); ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-30, 500); ax.set_ylim(-40, 560)
def section(y, lid_angle, title, note):
    # tray + kb + rail, side view (x = depth from front)
    ax.add_patch(Rectangle((0, y), TRAY, 4, fc=WAL, ec="none"))
    ax.add_patch(Rectangle((0, y), 4, 10, fc=WAL, ec="none"))
    ax.add_patch(Rectangle((TRAY-135, y+4), 135, 16, fc=SILVER, ec="#777", lw=0.4))
    ax.add_patch(FancyBboxPatch((TRAY, y), RAIL, 25, boxstyle="round,pad=0,rounding_size=4", fc=WAL, ec="none"))
    ax.add_patch(Rectangle((TRAY+14, y+25), 15, 8, fc=BLACK, ec="none"))   # knob
    import math
    L = TRAY + RAIL
    hx, hy = TRAY + RAIL, y + 34  # hinge at the rail's rear top
    a = math.radians(lid_angle)
    ex, ey = hx - L*math.cos(a), hy + L*math.sin(a)
    ax.plot([hx, ex], [hy, ey], color=WALD, lw=3.2, solid_capstyle="round")
    if 60 < lid_angle < 120:
        # strut and lamp
        ax.plot([hx-60*math.cos(a), hx+35], [hy+60*math.sin(a), y], color=BRASS, lw=1.0)
        ax.add_patch(Circle((ex+2, ey-4), 3, fc="#ffd98a", ec="none"))
        ax.add_patch(Polygon([[ex+2, ey-4], [10, y+21], [TRAY-10, y+21]], fc="#ffe2a0", ec="none", alpha=0.35))
    ax.text(-25, y+70, title, fontsize=7.5, weight="bold")
    ax.text(-25, y+58, note, fontsize=6.2, color="#444", va="top")
section(0, 0, "closed", "400 × 230 × ≈ 38 · lid sits 12 mm\nabove the keyboard, 4 above the knobs [calc]")
section(250, 100, "standing lid (≈ 100°)", "shade in sun · music stand · at night a dim\nwarm strip on its top edge lights the keys")
section(110, 180, "", "")
ax.text(-25, 165, "lid flat back", fontsize=7.5, weight="bold"); ax.text(-25, 155, "full lap mode: 400 × 460, or lift it off (pin hinge)", fontsize=6.2, color="#444", va="top")
ax.text(230, -30, "side sections · keyboard 16 tall, rail 25 + knobs 8 · front is left", ha="center", fontsize=7, color=GREY)

# ---------- C: why, and what it borrows ----------
ax = fig.add_axes([0.03, 0.03, 0.94, 0.40]); ax.axis("off")
txt = [
("Own the outline, host the keys.", "The kit's edge is always floss's: walnut rail and tray lip. The keyboard is a guest laid in a bed, like a harmonica in its case. Black keyboards sink into the bed; white ones float on it like ivory on felt. From two metres away you see floss and a field of keys, not a logo."),
("Width is ours.", "Module width 400 ≥ every slim keyboard (325–388 [eng]), so the guest never sticks out past floss. Depth comes from the parts: a single row of knobs needs ≈ 80. [eng: board ≈ 16,000 mm² → ≈ 260 × 62 inside, + speaker box ≈ 120 × 62 × 22 ≈ 164 cm³, the low end of ≥ 150–300; battery under the board. Tight; eng to check.]"),
("One line of controls.", "Fourteen controls in one row at 25.5 pitch, parallel to the keys: octave L at the left end over the left hand, octave R at the right end, the shared voice and room between in signal order. Read by counting from either end, eyes closed. Harmonica holes, not a synth panel."),
("The split, on any keyboard.", "A brass target slides on a graduated rail along the rail's front edge. Slide it over B | C once for today's keyboard. It's systems' ribbon made precise, touchable at night, and free to sit off-centre if the keyboard does. Surveying: the rod and its sliding target."),
("The lid earns its place three ways.", "Closed it protects keys and knobs. Standing it's shade for the panel in sun (job 20), a stand for a lyric sheet, and at night a dim warm strip lights the keys (LAMP's idea, without LAMP's lap problem). The inside of the lid carries a printed card: the MIDI map and 'keep the keyboard at its home octave' (job 6, 18)."),
("Weak, honestly.", "230 deep is a big footprint (thin, though). The lid's size depends on the module's depth, so it isn't one family part. Holding 83–135-deep keyboards uses two elastic bands and the rail as a back stop: fine for slim ones, no good for the 39–49 mm chunky minis (they play, they don't pack). Hinge + strut + lamp are three more parts to build."),
]
y = 0.97
for h, b in txt:
    ax.text(0.0, y, h, fontsize=9.5, weight="bold", va="top", transform=ax.transAxes)
    import textwrap; ax.text(0.22, y, textwrap.fill(b, 150), fontsize=8.3, va="top", transform=ax.transAxes, color="#333")
    y -= 0.16
fig.text(0.03, 0.012, "floss · module jam turn 2 · visual · rough 2-D sketch, not a render · draws: 'Abandon normal instruments', harmonica case, surveying instruments, 'lives on a shelf', 3", fontsize=7, color=GREY)
fig.savefig("visual-module-jam2a-fallboard.png", facecolor=BG)
