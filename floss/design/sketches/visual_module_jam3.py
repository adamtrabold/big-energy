# floss module jam, pass 2 (visual turn): FALLBOARD with end blocks + grouped rail + pocket; SPINE closed and on a lap;
# CLOTH spread as a frame; closed kits vs a 16-inch laptop and a book. Rough 2-D, to scale (mm).
# Run from this folder: python3 visual_module_jam3.py  -> visual-module-jam3{a,b,c}-*.png
import math, textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Polygon, Ellipse
plt.rcParams["font.family"] = "Inter"
WAL="#6b4429"; WALD="#563520"; CREAM="#f1ebdd"; CREAMD="#e3d9c4"; BLACK="#1d1b19"; CORAL="#f0806a"; BRASS="#c9a24a"; BRASSD="#8a6d27"
GREY="#8a8276"; BED="#2e2622"; BEDL="#3d3430"; SILVER="#c8c8c6"; WHITEKB="#e9e7e2"; BG="#f6f2ea"; FOAM="#5a524c"; CLOTHC="#3f4a47"; CLOTHL="#56625e"
DRAW = "floss · module jam pass 2 · visual · rough 2-D sketch, not a render · draw this turn: 'Change instrument roles' + pipe-organ stop knobs"

W = 412; RAILD = 95; BEDD = 155; INNER = 404
KB = {"xkey": ("CME Xkey 25 · 388 × 135 × 16", 388, 135, 16, SILVER, (WHITEKB, BLACK)),
      "nano": ("Korg nanoKEY2 · 325 × 83 × 16", 325, 83, 16, BLACK, (BLACK, "#555")),
      "kbc":  ("KMI K-Board C · 325 × 84 × 11", 325, 84, 11, "#f2f2f0", ("#e6e6e3", "#cfcfcc"))}

def fig_new(title, sub):
    fig = plt.figure(figsize=(16.5, 11.7), dpi=150); fig.patch.set_facecolor(BG)
    fig.text(0.03, 0.965, title, fontsize=13, weight="bold")
    fig.text(0.03, 0.94, sub, fontsize=9.3, color="#444")
    fig.text(0.03, 0.012, DRAW, fontsize=7, color=GREY)
    return fig

def axes(fig, rect, xl, yl):
    ax = fig.add_axes(rect); ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(*xl); ax.set_ylim(*yl); return ax

# ---------------- the rail (layout D, grouped, organ jambs at the ends) ----------------
FRONT = [  # (name, slot width, kind)
    [("oct L", 24, "oct"), ("tabsL", 22, "tabs")],
    [("attack", 22, "pot"), ("release", 22, "pot"), ("hold", 22, "hold")],
    [("drift", 22, "pot"), ("tone", 22, "pot")],
    [("depth", 22, "pot")],
    [("echo", 22, "pot"), ("time", 22, "pot"), ("tap", 16, "tap"), ("reverb", 22, "pot")],
    [("volume", 22, "pot")],
    [("tabsR", 22, "tabs"), ("oct R", 24, "oct")]]
BREAK = 10
def row_layout():
    xs = []; x = 0; breaks = []
    for gi, g in enumerate(FRONT):
        if gi: breaks.append(x + BREAK/2); x += BREAK
        for name, w, k in g:
            xs.append((name, x + w/2, k)); x += w
    return xs, breaks, x
ROW, BREAKS, ROWLEN = row_layout()   # ROWLEN = 388 at pitch 22, break 10

def rail(ax, x0, y0, scale_labels=1.0, labels=True, target_x=None):
    """Plan of the rail; y0 = front edge. Front of rail faces -y (toward the keys)."""
    ax.add_patch(FancyBboxPatch((x0, y0), W, RAILD, boxstyle="round,pad=0,rounding_size=12", fc=WAL, ec=WALD, lw=0.8))
    # sunk channel (cream deck) holding the controls
    ax.add_patch(FancyBboxPatch((x0+7, y0+6), W-14, 58, boxstyle="round,pad=0,rounding_size=6", fc=CREAM, ec=CREAMD, lw=0.8))
    # grille strip / nameboard at the back
    ax.add_patch(FancyBboxPatch((x0+7, y0+68), W-14, 21, boxstyle="round,pad=0,rounding_size=5", fc=CREAMD, ec="none"))
    for i in range(52):
        gx = x0+16+i*7.5
        if abs(gx-(x0+W/2)) > 22: ax.plot([gx, gx], [y0+72, y0+85], color="#b9ae99", lw=1.0)
    ax.text(x0+W/2, y0+78.5, "floss", ha="center", va="center", fontsize=8*scale_labels, style="italic", color=WALD)
    sx = x0 + (W-ROWLEN)/2; fy = y0+22; by = y0+48
    for bx in BREAKS:   # brass frets across the channel at each group break (raised 1 mm: count by touch)
        ax.add_patch(Rectangle((sx+bx-0.9, y0+8), 1.8, 54, fc=BRASS, ec="none"))
    pos = {}
    for name, cx, k in ROW:
        X = sx+cx; pos[name] = X
        if k == "oct":
            ax.add_patch(Circle((X, fy), 7.45, fc=BLACK, ec="none")); ax.plot([X, X], [fy, fy+6], color="white", lw=0.9)
        elif k == "pot":
            ax.add_patch(Circle((X, fy), 7.45, fc=BLACK, ec="none")); ax.plot([X, X], [fy, fy+6], color="white", lw=0.9)
        elif k == "hold":
            ax.add_patch(Circle((X, fy), 7.0, fc=BRASS, ec=BRASSD, lw=0.6)); ax.add_patch(Circle((X, fy), 4.2, fc="#d9b75e", ec="none"))
        elif k == "tap":
            ax.add_patch(Circle((X, fy), 6.3, fc="#8fd18a", ec="none")); ax.add_patch(Circle((X, fy), 5.0, fc=BLACK, ec="none"))
        elif k == "tabs":   # three stop tabs, front to back: low, main, high (theatre-organ stop tabs)
            for j, t in enumerate(["low", "main", "high"]):
                ax.add_patch(FancyBboxPatch((X-7.5, fy-8+j*12), 15, 10, boxstyle="round,pad=0,rounding_size=2", fc="#fbf7ee", ec=GREY, lw=0.5))
                if labels: ax.text(X, fy-3+j*12, t, ha="center", va="center", fontsize=3.6*scale_labels, color="#333")
        if labels and k != "tabs":
            ax.text(X, fy-12.5, name, ha="center", fontsize=4.4*scale_labels, color="#333")
    # back line of kinds, behind the amounts they qualify
    bl = [("pressure", (pos["attack"]+pos["release"])/2, CORAL), ("shimmer", pos["depth"], BLACK), ("free/sync", pos["time"], None)]
    for name, X, col in bl:
        if col:
            ax.add_patch(Circle((X, by), 5.0, fc=col, ec="none")); ax.plot([X, X], [by, by+4], color="white", lw=0.8)
        else:
            ax.add_patch(Rectangle((X-3, by-5), 6, 10, fc="#bdbdbd", ec="#777", lw=0.4)); ax.add_patch(Rectangle((X-1, by), 2, 6, fc="#555", ec="none"))
        if labels: ax.text(X, by+7.5, name, ha="center", fontsize=4.0*scale_labels, color="#333")
    # target rail on the front edge of the rail + host port + port light (in the gutter)
    ax.plot([x0+20, x0+W-20], [y0+2.5, y0+2.5], color=BRASS, lw=1.0)
    for t in range(-180, 181, 10):
        ax.plot([x0+W/2+t]*2, [y0+1, y0+(4.5 if t == 0 else 3)], color=BRASSD if t == 0 else BRASS, lw=0.5 if t == 0 else 0.35)
    if target_x is not None:
        ax.add_patch(Polygon([[target_x-5, y0+6], [target_x+5, y0+6], [target_x, y0-2]], fc=BRASS, ec=BRASSD, lw=0.6))
    return pos

def bed(ax, x0, y0, kbkey):
    """Plan of the keyboard bed; y0 = front edge. Keyboard pushed back to the 12 mm gutter."""
    name, kw, kd, kh, kcol, keys = KB[kbkey]
    ax.add_patch(FancyBboxPatch((x0, y0), W, BEDD, boxstyle="round,pad=0,rounding_size=12", fc=WAL, ec=WALD, lw=0.8))
    ax.add_patch(Rectangle((x0+4, y0+4), INNER, BEDD-4, fc=BED, ec="none"))
    # gutter = the pocket: 12 wide along the whole bed, against the rail
    ax.add_patch(Rectangle((x0+4, y0+BEDD-12), INNER, 12, fc="#1d1714", ec="none"))
    # coiled cable lying in the gutter + a flat spare
    for i in range(40):
        cx = x0+60+i*3.2
        ax.add_patch(Ellipse((cx, y0+BEDD-6), 3.2, 9, fc="none", ec="#6b6b6b", lw=0.5))
    ax.plot([x0+W/2+30, x0+W-40], [y0+BEDD-4, y0+BEDD-4], color="#4c4c4c", lw=1.4)
    ax.add_patch(Rectangle((x0+W/2-5, y0+BEDD-1.6), 10, 1.6, fc="#000", ec="none"))     # host port in the rail face
    ax.add_patch(Circle((x0+W/2+12, y0+BEDD-1.5), 1.6, fc="#ffcf6b", ec="none"))       # port light
    # keyboard
    kx = x0 + (W-kw)/2; ky = y0 + BEDD - 12 - kd
    ax.add_patch(FancyBboxPatch((kx, ky), kw, kd, boxstyle="round,pad=0,rounding_size=4", fc=kcol, ec="#666", lw=0.5))
    nwhite = 15; kwid = (kw-30)/nwhite; k0 = kx+15; keyd = min(kd*0.7, 85)
    for i in range(nwhite):
        ax.add_patch(Rectangle((k0+i*kwid, ky+3), kwid, keyd, fc=keys[0], ec="#888", lw=0.4))
    for i in [0,1,3,4,5,7,8,10,11,12]:
        ax.add_patch(Rectangle((k0+(i+1)*kwid-kwid*0.3, ky+3+keyd*0.38), kwid*0.6, keyd*0.62, fc=keys[1], ec="none"))
    # end blocks: from the bed wall to the keyboard's end, 80 deep at the back; lip over the end cap
    gap = (INNER-kw)/2
    for side in (-1, 1):
        if side < 0: bx = x0+4; bw = gap
        else: bx = kx+kw; bw = gap
        ax.add_patch(Rectangle((bx, y0+BEDD-12-80), bw, 80, fc=WAL, ec=WALD, lw=0.6))
        lipx = (kx-0) if side < 0 else kx+kw-7
        ax.add_patch(Rectangle((lipx if side > 0 else kx, y0+BEDD-12-80), 7, 80, fc=WALD, ec="none", alpha=0.9))
        ax.add_patch(Circle((bx+bw/2 if bw > 12 else bx+bw/2, y0+BEDD-12-40), 2.2, fc=BRASS, ec="none"))   # thumb lock
    # graduated scale on the front lip, mirrored, 0..32 each side
    for t in range(0, 33, 4):
        for side in (-1, 1):
            X = x0+4+t if side < 0 else x0+W-4-t
            ax.plot([X, X], [y0+0.8, y0+3.2 if t % 8 else 4.2], color=BRASS, lw=0.4)
    ax.text(x0+W/2, y0+12, name, ha="center", fontsize=5.5, color="#999" if kbkey != "nano" else "#888")
    return k0, kwid, gap

def bc_x(k0, kwid): return k0 + 7*kwid   # B|C if the lowest key is C (default octave)

# =========================================================== SHEET A: FALLBOARD
def sheetA():
    fig = fig_new("floss · module jam pass 2 · visual · FALLBOARD with end blocks, the grouped rail and the pocket (rough, to scale)",
                  "412 wide (S8 at ≈ 412). Rail 412 × 95: a sunk channel with the front row and a back line of three kinds, brass frets between groups, organ stop tabs at each end. Bed 412 × 155 with sliding end blocks and the gutter pocket.")
    for j, kk in enumerate(["xkey", "nano"]):
        ax = axes(fig, [0.02+j*0.31, 0.50, 0.31, 0.42], (-15, 430), (-55, 300))
        k0, kwid, gap = bed(ax, 0, 0, kk)
        rail(ax, 0, BEDD, scale_labels=0.9, target_x=bc_x(k0, kwid))
        ax.text(W/2, -14, f"plan, open · {'blocks fully in (8 mm)' if kk=='xkey' else f'blocks out ≈ {gap:.0f} mm each'}", ha="center", fontsize=7.5, color="#444")
        ax.text(W/2, -26, "footprint 412 × 250, open or closed", ha="center", fontsize=6.8, color=GREY)
        if j == 0:
            ax.annotate("gutter = the pocket: 404 × 12, coiled cable +\na flat spare; host port and port light at its centre",
                        xy=(120, BEDD-6), xytext=(-12, -50), fontsize=6, color="#333", arrowprops=dict(arrowstyle="-", color="#333", lw=0.5))
            ax.annotate("one brass scale on the bed lip (0–32 each side)\nand on the target rail: set both blocks to the same number",
                        xy=(30, 2), xytext=(205, -50), fontsize=6, color="#6b5320", arrowprops=dict(arrowstyle="-", color=BRASS, lw=0.5))
        else:
            ax.annotate("end blocks hold the ends, 80 deep at the back,\na lip over each end cap; nothing crosses a key", xy=(gap/2+4, BEDD-60),
                        xytext=(150, -50), fontsize=6, color="#333", arrowprops=dict(arrowstyle="-", color="#333", lw=0.5))
    # enlarged rail
    ax = axes(fig, [0.63, 0.62, 0.36, 0.30], (-8, 420), (-30, 110))
    rail(ax, 0, 0, scale_labels=1.25, target_x=W/2-30)
    ax.text(0, 103, "the rail, enlarged · front row 388 long at pitch 22, groups broken by 10 + a brass fret", fontsize=7.2, weight="bold")
    groups = ["octave · stops", "touch", "voice", "shimmer", "room", "out", "stops · octave"]
    sx = (W-ROWLEN)/2; edges = [0] + BREAKS + [ROWLEN]
    for g, (a, b) in zip(groups, zip(edges[:-1], edges[1:])):
        ax.text(sx+(a+b)/2, -10, g, ha="center", fontsize=5.6, color=BRASSD)
    ax.text(W/2, -22, "jambs at each end: octave + three stop tabs (low · main · high) own their half · back line: pressure (coral) · shimmer mode · free/sync", ha="center", fontsize=5.6, color="#444")
    # sections: closed, slim and published speaker paths
    ax = axes(fig, [0.63, 0.30, 0.36, 0.30], (-20, 300), (-35, 150))
    def closed(y, H, lab):
        ax.add_patch(Rectangle((0, y), BEDD, 4, fc=WAL, ec="none")); ax.add_patch(Rectangle((0, y), 4, 9, fc=WAL, ec="none"))
        ax.add_patch(Rectangle((BEDD-12-135, y+4), 135, 16, fc=SILVER, ec="#777", lw=0.4))
        rx = BEDD
        ax.add_patch(Polygon([[rx, y], [rx+RAILD, y], [rx+RAILD, y+H], [rx+64, y+H], [rx+64, y+24], [rx+6, y+24], [rx+6, y+H], [rx, y+H]], fc=WAL, ec=WALD, lw=0.5))
        for kx in (rx+16, rx+42): ax.add_patch(Rectangle((kx, y+24), 15 if kx < rx+30 else 10, 8, fc=BLACK if kx < rx+30 else CORAL, ec="none"))
        top = max(H, 32)
        lid_u = top + 2
        ax.add_patch(Rectangle((0, y+lid_u), BEDD+RAILD, 4, fc=WALD, ec="none"))
        ax.add_patch(Rectangle((10, y+20), 120, lid_u-20, fc=FOAM, ec="none", alpha=0.75))   # foam strip under the lid
        ax.add_patch(Rectangle((BEDD-12, y+4), 12, lid_u-4, fc="none", ec="#c9a24a", lw=0.6, ls=(0,(2,1.5))))  # gutter pocket
        ax.text(-18, y+lid_u+10, lab, fontsize=6.6, weight="bold")
        ax.text(BEDD+RAILD+6, y+lid_u/2, f"≈ {lid_u+4:.0f}", fontsize=7, va="center")
    closed(0, 30, "slim driver + radiator path: rim 30 → closed ≈ 38")
    closed(80, 38, "published-data path: body 32–38 (drawn 38) → closed ≈ 40–46")
    ax.text(130, -28, "closed side sections · front left · knobs (8) sit in the channel (deck 24), so on the published path\nthe knob tops (32) are already under the rim and the thicker body costs only its own depth [calc]\ndotted brass = the gutter pocket, 12 wide × ≈ 30–36 tall × 404 long", ha="center", fontsize=5.8, color=GREY)
    # end block detail + text
    ax = axes(fig, [0.63, 0.04, 0.36, 0.22], (-10, 140), (-25, 50))
    ax.add_patch(Rectangle((0, 0), 130, 4, fc=WAL, ec="none")); ax.add_patch(Rectangle((0, 0), 4, 30, fc=WAL, ec="none"))
    ax.add_patch(Rectangle((4, 4), 34, 3, fc="#222", ec="none"))            # track
    ax.add_patch(Rectangle((8, 7), 6, 22, fc=WAL, ec=WALD, lw=0.5))          # block body
    ax.add_patch(Rectangle((14, 7), 2, 16, fc=FOAM, ec="none"))              # pad
    ax.add_patch(Rectangle((8, 23), 26, 6, fc=WAL, ec=WALD, lw=0.5))         # lip
    ax.add_patch(Rectangle((16, 20), 18, 3, fc=FOAM, ec="none"))             # foam under lip
    ax.add_patch(Rectangle((16, 4), 110, 16, fc=SILVER, ec="#777", lw=0.4)) # keyboard end
    ax.add_patch(Circle((11, 26), 2.0, fc=BRASS, ec="none"))
    ax.text(0, 42, "end block, section across the bed (2:1 of the plan)", fontsize=6.8, weight="bold")
    ax.text(40, 33, "6 body + 2 pad + lip with 6 foam; slides 32 on a track,\nthumb lock; presses down on 11–16 tall keyboards", fontsize=5.8, color="#333")
    ax.text(0, -18, "track · block · pad · lip · foam · keyboard end cap", fontsize=5.6, color=GREY)
    # notes
    ax = fig.add_axes([0.03, 0.04, 0.58, 0.40]); ax.axis("off")
    rows = [
    ("The face (director objection 5).", "Draw: 'Change instrument roles' + pipe-organ stops. The rail's ends play the stop jambs of an organ: each end holds its half's octave and its three stop tabs, so each end owns its half and the instrument has two 'shoulders'. Between them, a quiet line on a cream channel, broken by brass frets. The wordmark sits centred in the grille, where a piano puts its nameboard. Walnut, cream, brass, one coral."),
    ("Grouping you can count.", "Seven groups, octave·stops | touch | voice | shimmer | room | out | stops·octave. Within a group the pitch is 22; between groups 32, with a 1 mm raised brass fret across the channel. Count frets from either end with eyes closed. HOLD (brass, larger) sits with touch. Front row 388 long on a 412 rail (+4 spare) [calc]."),
    ("The back line of kinds.", "Three set-and-leave controls sit behind what they qualify: PRESSURE (coral, the life) behind attack/release, SHIMMER mode behind depth, FREE/SYNC behind time. Smaller (Ø 10) than the amounts (Ø 14.9) so the hand meets amounts first."),
    ("Knobs in a channel.", "The deck is sunk 6 mm under the walnut rim. On the slim speaker path that only guards the knobs; on the published path (body 32–38) the knob tops are already under the rim, so FALLBOARD closes at ≈ 40–46, not ≈ 48–54 [calc]. Also: nothing snags in a bag if the lid is left open."),
    ("End blocks and pocket.", "Systems' numbers: 8 mm in, 40 out, 32 travel, inside 404. Blocks sit at the back (80 deep) so an 83-deep keyboard is fully held and a 135-deep one by its rear 80. The gutter is the pocket: cable and a flat spare; no charger (honest). A foam strip under the lid pins the keyboard when closed (14–20 mm, more on the published path)."),
    ("Open questions.", "Stop-tab words: low · main · high (plain, my default) or the organ's 16′ · 8′ · 4′ (jargon, but it's what the tabs are). Frets: brass (family) or a walnut ridge (quieter)? Self-centring blocks: I'd stay with the scale (no mechanism)."),
    ]
    y = 0.98
    for h, b in rows:
        ax.text(0.0, y, h, fontsize=8.6, weight="bold", va="top", transform=ax.transAxes)
        ax.text(0.27, y, textwrap.fill(b, 108), fontsize=7.4, va="top", transform=ax.transAxes, color="#333")
        y -= 0.165
    fig.savefig("visual-module-jam3a-fallboard.png", facecolor=BG)

# =========================================================== SHEET B: SPINE + CLOTH
def sheetB():
    fig = fig_new("floss · module jam pass 2 · visual · SPINE closed and on a lap; CLOTH spread as a frame (rough, to scale)",
                  "SPINE: two 412 × 145 boards and a 56–62 spine. The sag question, answered from the lap's geometry. CLOTH: a 270-wide BLOCK and any keyboard on an 800 cloth whose woven frame is the family outline.")
    BD = 145
    # --- SPINE closed plan
    ax = axes(fig, [0.02, 0.62, 0.30, 0.29], (-20, 440), (-40, 190))
    ax.add_patch(FancyBboxPatch((0, 0), W, BD, boxstyle="round,pad=0,rounding_size=6", fc=WAL, ec=WALD, lw=0.8))
    for cx, cy in [(0, 0), (W-26, 0), (0, BD-26), (W-26, BD-26)]:
        ax.add_patch(Polygon([[cx+(0 if cx == 0 else 26), cy+(0 if cy == 0 else 26)], [cx+(26 if cx == 0 else 0), cy+(0 if cy == 0 else 26)], [cx+(0 if cx == 0 else 26), cy+(26 if cy == 0 else 0)]], fc=BRASS, ec="none"))
    ax.add_patch(Rectangle((0, BD), W, 8, fc="#4a3020", ec="none"))
    ax.add_patch(Rectangle((W/2-60, 50), 120, 40, fc=CREAM, ec="none")); ax.text(W/2, 70, "floss", ha="center", va="center", fontsize=9, style="italic", color=WALD)
    ax.add_patch(Rectangle((W/2-60, 44), 120, 3, fc=CORAL, ec="none"))
    ax.text(W/2, -15, "SPINE closed, front cover · 412 × 145 (+ the spine on the far edge)", ha="center", fontsize=7, color="#444")
    ax.text(W/2, -28, "brass book corners, a cream label, one coral line", ha="center", fontsize=6.4, color=GREY)
    # --- SPINE closed sections, two thicknesses
    ax = axes(fig, [0.33, 0.62, 0.30, 0.29], (-30, 230), (-40, 180))
    def spine_sec(y, T, lab):
        ax.add_patch(Rectangle((0, y), BD, 4, fc=WAL, ec="none"))                    # keyboard board
        ax.add_patch(Rectangle((5, y+4), 135, 16, fc=SILVER, ec="#777", lw=0.4))     # keyboard
        top = 4+16+4                                                                 # air + foam
        ax.add_patch(Rectangle((0, y+top), BD, T, fc=WAL, ec=WALD, lw=0.5))          # module, panel facing down
        ax.add_patch(Rectangle((30, y+top-2), 15, 2, fc=BLACK, ec="none"))
        H = top+T
        ax.add_patch(FancyBboxPatch((BD, y), 6, H, boxstyle="round,pad=0,rounding_size=3", fc="#4a3020", ec="none"))
        ax.text(BD+12, y+H/2, f"≈ {H:.0f}", fontsize=7, va="center")
        ax.text(0, y+H+6, lab, fontsize=6.4, weight="bold")
    spine_sec(0, 30, "slim path: module 30 → closed ≈ 54")
    spine_sec(85, 36, "published path: module 32–38 (drawn 36) → ≈ 56–62")
    ax.text(100, -30, "closed sections · keyboard board, keyboard 16, 4 foam/air, module face-down,\nknobs in their channel · spine on the right", ha="center", fontsize=5.8, color=GREY)
    # --- SPINE on a lap: from the front
    ax = axes(fig, [0.64, 0.62, 0.35, 0.29], (-60, 480), (-120, 160))
    for tx in (40, 250):
        ax.add_patch(Ellipse((tx+60, -35), 150, 80, fc="#c9b9a3", ec="none"))
    ax.add_patch(Rectangle((0, 6), W, 4, fc=WAL, ec="none")); ax.add_patch(Rectangle((0, 10), W, 30, fc=WAL, ec=WALD, lw=0.5, alpha=0.95))
    ax.plot([0, W], [5, 5], color="#4a3020", lw=2)
    ax.text(W/2, 60, "on a lap, from the front: the spine and both boards run ACROSS both thighs", ha="center", fontsize=6.6, weight="bold")
    ax.text(W/2, 48, "each rigid board spans the gap between the thighs; the spine is supported on both", ha="center", fontsize=6.0, color="#444")
    ax.text(W/2, -100, "so the boards don't sag between the thighs [geometry]", ha="center", fontsize=6.2, color="#333")
    # --- SPINE on a lap: from the side, and the dip case
    ax = axes(fig, [0.02, 0.29, 0.61, 0.32], (-30, 900), (-140, 170))
    def lapside(x0, slope, dip, title, note, ends=False):
        a = math.radians(slope)
        # thigh
        if not ends: ax.add_patch(Polygon([[x0-10, -40], [x0+380*math.cos(a), -40-380*math.sin(a)], [x0+380*math.cos(a), -10-380*math.sin(a)], [x0-10, -10]], fc="#c9b9a3", ec="none"))
        # boards: module (rear, near the body) on the left, keyboard on the right
        def board(xa, ya, L, ang, col, thick):
            aa = math.radians(ang)
            pts = [[xa, ya], [xa+L*math.cos(aa), ya-L*math.sin(aa)], [xa+L*math.cos(aa)-thick*math.sin(aa), ya-L*math.sin(aa)+thick*math.cos(aa)], [xa-thick*math.sin(aa), ya+thick*math.cos(aa)]]
            ax.add_patch(Polygon(pts, fc=col, ec=WALD, lw=0.4)); return xa+L*math.cos(aa), ya-L*math.sin(aa)
        ex, ey = board(x0, -10, BD, slope + dip, WAL, 30)
        ax.plot([ex, ex+56*math.cos(math.radians(slope))], [ey, ey-56*math.sin(math.radians(slope))], color="#4a3020", lw=3)
        sx2, sy2 = ex+56*math.cos(math.radians(slope)), ey-56*math.sin(math.radians(slope))
        board(sx2, sy2, BD, slope - dip, "#8a6a52", 4)
        aa = math.radians(slope - dip)
        ax.add_patch(Polygon([[sx2+5*math.cos(aa), sy2-5*math.sin(aa)], [sx2+140*math.cos(aa), sy2-140*math.sin(aa)], [sx2+140*math.cos(aa)-16*math.sin(aa), sy2-140*math.sin(aa)+16*math.cos(aa)], [sx2+5*math.cos(aa)-16*math.sin(aa), sy2-5*math.sin(aa)+16*math.cos(aa)]], fc=SILVER, ec="#777", lw=0.3))
        if ends:   # supports only under the two outer ends (knees / hands / slats)
            for (ux, uy) in [(x0+20, -10), (sx2+120*math.cos(aa), sy2-120*math.sin(aa))]:
                ax.add_patch(Polygon([[ux-14, uy-30], [ux+14, uy-30], [ux, uy-1]], fc="#c9b9a3", ec="none"))
        ax.text(x0, 120, title, fontsize=6.8, weight="bold")
        ax.text(x0, 108, note, fontsize=5.9, color="#333", va="top")
    lapside(0, 8, 0, "on a lap, from the side: fine", "Thighs slope gently to the knees (drawn 8°). Both boards lie on them;\nthe spine lies on them too. Module near the body, keys toward the knees.")
    lapside(470, 0, 9, "where it does fold: no support under the spine", "Knees apart with the kit on your knees, a gap between bench slats,\nor lifted by its two ends: the joints dip (drawn 9° each). Pressing\nkeys makes it worse. This is the real 'sag', and it's a joint problem.", ends=True)
    ax.text(0, -105, textwrap.fill("FIX (PROPOSAL): the spine stops at flat. A rigid spine board between two cloth joints, with the boards' inner edges bevelled to bear on it at 180°: it folds up to close or stand, never down. "
            "Open, it's one stiff board in the way gravity loads it. Bookbinding craft; a making step to list.", 190), ha="left", va="top", fontsize=6.4, color="#333", weight="bold")
    # --- CLOTH spread
    ax = axes(fig, [0.66, 0.04, 0.33, 0.52], (-30, 830), (-60, 830))
    ax.add_patch(Rectangle((0, 0), 800, 800, fc=CLOTHC, ec="none"))
    ax.add_patch(Rectangle((14, 14), 772, 772, fc="none", ec=CLOTHL, lw=1.2))
    # woven family outline: 412 × 250, the same footprint as FALLBOARD
    fx, fy = 194, 270
    ax.add_patch(Rectangle((fx, fy), 412, 250, fc="none", ec="#d8cfb9", lw=1.0))
    ax.plot([400, 400], [fy-30, fy+280], color="#e7dcc0", lw=0.6, ls=(0, (6, 4)))
    ax.text(400, fy-48, "keep the keyboard at its home octave", ha="center", fontsize=5.6, color="#e7dcc0", style="italic")
    # BLOCK module behind, rim, knobs below the rim
    bx, by = 400-135, fy+150
    ax.add_patch(FancyBboxPatch((bx, by), 270, 100, boxstyle="round,pad=0,rounding_size=10", fc=WAL, ec=WALD, lw=0.8))
    ax.add_patch(FancyBboxPatch((bx+8, by+8), 254, 84, boxstyle="round,pad=0,rounding_size=6", fc=CREAM, ec="none"))
    for r in range(2):
        for i in range(8):
            ax.add_patch(Circle((bx+25+i*31, by+30+r*36), 7.45, fc=CORAL if (r == 1 and i == 1) else BLACK, ec="none"))
    # keyboard in front (nanoKEY2)
    kx, ky = 400-162.5, fy+20
    ax.add_patch(FancyBboxPatch((kx, ky), 325, 83, boxstyle="round,pad=0,rounding_size=4", fc=BLACK, ec="#666", lw=0.5))
    for i in range(15): ax.add_patch(Rectangle((kx+15+i*19.7, ky+3), 19.7, 58, fc=BLACK, ec="#555", lw=0.4))
    # pocket + sleeve, corner ties
    ax.add_patch(Rectangle((40, 40), 160, 110, fc=CLOTHL, ec="#6d7a75", lw=0.8)); ax.text(120, 95, "pocket:\ncable, spare,\ncharger", ha="center", va="center", fontsize=5.6, color="#e7dcc0")
    ax.add_patch(Rectangle((560, 640), 220, 140, fc=CLOTHL, ec="#6d7a75", lw=0.8)); ax.text(670, 710, "module sleeve\n(removable, washable)", ha="center", va="center", fontsize=5.6, color="#e7dcc0")
    for cx, cy in [(0, 0), (800, 0), (0, 800), (800, 800)]:
        ax.add_patch(Circle((cx, cy), 14, fc=BRASS, ec="none"))
    ax.text(400, -30, "CLOTH spread on a bench · 800 square · the woven frame is FALLBOARD's 412 × 250 outline", ha="center", fontsize=6.4, color="#444")
    ax.text(400, -50, "module 270 × 100 (meets T4) · knobs below a raised rim · drawn with a nanoKEY2", ha="center", fontsize=6.0, color=GREY)
    # notes
    ax = fig.add_axes([0.03, 0.04, 0.60, 0.24]); ax.axis("off")
    rows = [("The sag question.", "Mostly a false alarm on a lap: the spine runs left to right, across both thighs, so the thighs carry both boards and the spine. It folds where nothing is under the spine: knees apart, a slatted bench, lifted by its ends. Fix: a spine that stops at flat (bevelled board edges bearing on a rigid spine board). If the director wants zero risk, a 3 mm slat stowed in the spine slides across the joint to lock it."),
            ("SPINE's face.", "Closed it's a book: brass corners, a cream label, a coral line. It stands 412 tall on a shelf, spine out. Its module board is 412 × 145: the rail's layout D fits with 50 mm to spare, which goes to the speaker box (useful on the published path)."),
            ("CLOTH as a frame.", "Spread, the cloth carries the family outline woven in pale thread: the same 412 × 250 as FALLBOARD, so 'own the outline' holds in the soft kit too. Dark slate-green cloth (CLOTH's own colour; walnut and brass on the module). The home-octave line is woven beside the centre line. Brass weights at the corners keep it flat outdoors and make the knot's corners. On a lap it drapes: CLOTH is a bench and table kit, honestly.")]
    y = 0.98
    for h, b in rows:
        ax.text(0.0, y, h, fontsize=8.6, weight="bold", va="top", transform=ax.transAxes)
        ax.text(0.2, y, textwrap.fill(b, 118), fontsize=7.4, va="top", transform=ax.transAxes, color="#333")
        y -= 0.33
    fig.savefig("visual-module-jam3b-spine-cloth.png", facecolor=BG)

# =========================================================== SHEET C: closed kits compared
def sheetC():
    fig = fig_new("floss · module jam pass 2 · visual · the three closed kits beside a 16-inch laptop and a hardback book (rough, to scale)",
                  "Same scale throughout. Two thicknesses each: the slim speaker path and the published-data path (eng/module-r2.md to confirm). Dashed: T4's old 290 × 135.")
    items = [
        ("FALLBOARD", 412, 250, (38, 46), WAL, "one thin board; Xkey or any slim keyboard inside"),
        ("SPINE", 412, 145, (54, 62), WAL, "a book; the smallest rigid footprint"),
        ("CLOTH (Xkey)", 400, 150, (56, 64), CLOTHC, "soft bundle: BLOCK on the keyboard, wrapped; module alone 270 × 100"),
        ("CLOTH (nanoKEY2)", 335, 110, (56, 64), CLOTHC, "with a 325-wide keyboard"),
        ("16-inch laptop", 356, 248, (17, 17), "#9aa0a6", "≈ 356 × 248 × 17 (a 16-inch MacBook Pro class, rounded)"),
        ("hardback book", 156, 234, (35, 35), "#7d8a8f", "≈ 156 × 234 × 35 (a typical novel, illustrative)"),
    ]
    # plans, overlaid on a grid
    ax = axes(fig, [0.02, 0.40, 0.62, 0.52], (-20, 1400), (-80, 600))
    pos = [(0, 300), (480, 300), (960, 300), (0, 0), (480, 0), (960, 0)]
    for (name, w, d, th, col, note), (px, py) in zip(items, pos):
        ax.add_patch(FancyBboxPatch((px, py), w, d, boxstyle="round,pad=0,rounding_size=8", fc=col, ec="none", alpha=0.92))
        if name in ("FALLBOARD", "SPINE"):
            ax.add_patch(Rectangle((px, py), 290, 135, fc="none", ec="#e9dcc0", lw=0.8, ls=(0, (4, 3))))
        if name.startswith("16"):
            ax.add_patch(Rectangle((px, py), 412, 250, fc="none", ec=WAL, lw=0.8, ls=(0, (2, 2))))
            ax.text(px+412, py+255, "FALLBOARD outline", ha="right", fontsize=5.6, color=WAL)
        ax.text(px, py+d+30 if d < 240 else py+d+14, name, fontsize=8, weight="bold")
        ax.text(px, py-16, f"{w} × {d}", fontsize=6.6, color="#444")
    ax.text(0, 590, "plans, to scale · dashed cream box on FALLBOARD and SPINE = T4's old 290 × 135", fontsize=7, color=GREY)
    # end elevations (thickness)
    ax = axes(fig, [0.66, 0.40, 0.32, 0.52], (-20, 330), (-40, 590))
    y = 500
    for name, w, d, th, col, note in items:
        ax.add_patch(Rectangle((0, y), d, th[0], fc=col, ec="none"))
        if th[1] != th[0]:
            ax.add_patch(Rectangle((0, y+th[0]), d, th[1]-th[0], fc=col, ec="none", alpha=0.35))
        lab = f"{th[0]}" if th[0] == th[1] else f"{th[0]} / {th[1]}"
        ax.text(d+8, y+th[1]/2, f"{name}: {lab}", fontsize=6.6, va="center")
        y -= 85
    ax.text(0, 570, "end views (depth × thickness), to scale · solid = slim path, pale = published path (upper bound)", fontsize=6.4, color=GREY)
    # table
    ax = fig.add_axes([0.03, 0.04, 0.94, 0.33]); ax.axis("off")
    hdr = ["", "footprint (mm)", "thickness (mm)", "volume (L)", "vs the laptop", "what it says"]
    rows = []
    lap = 356*248*17/1e6
    for name, w, d, th, col, note in items:
        v0 = w*d*th[0]/1e6; v1 = w*d*th[1]/1e6
        vol = f"{v0:.1f}" if th[0] == th[1] else f"{v0:.1f}–{v1:.1f}"
        rel = "—" if name.startswith("16") else (f"{v0/lap:.1f}–{v1/lap:.1f}×" if th[0] != th[1] else f"{v0/lap:.1f}×")
        rows.append([name, f"{w} × {d}", f"{th[0]}" if th[0] == th[1] else f"{th[0]}–{th[1]}", vol, rel, note])
    cols = [0.0, 0.14, 0.26, 0.37, 0.47, 0.57]
    for c, h in zip(cols, hdr): ax.text(c, 0.97, h, fontsize=8, weight="bold", va="top", transform=ax.transAxes)
    for r, row in enumerate(rows):
        for c, cell in zip(cols, row): ax.text(c, 0.84-r*0.105, cell, fontsize=7.6, va="top", transform=ax.transAxes, color="#222")
    ax.text(0.0, 0.17, textwrap.fill("Read: FALLBOARD is a laptop's footprint, 56 mm wider and 2.2–2.7 times as thick, and it's the only kit that's open-and-play with a lid that works. SPINE is about 40 % less area than FALLBOARD and 3.2–3.6 times a laptop's thickness: the bag-space winner. "
             "CLOTH's bundle is about SPINE's size with a big keyboard and smaller with a small one, but soft; its module alone is the only thing under T4. None of the one-package kits meets T4; that was eng's finding, and S8 ('floss adds about an inch to the widest travel keyboard') is the honest answer. "
             "Weights are eng's to add (T5, 1.5 kg). Thicknesses: [calc] from the sections on sheets a and b; CLOTH's ± a few mm of cloth.", 210), fontsize=7.2, va="top", transform=ax.transAxes, color="#333")
    fig.savefig("visual-module-jam3c-closed-kits.png", facecolor=BG)

if __name__ == "__main__":
    import sys
    which = sys.argv[1:] or ["a", "b", "c"]
    if "a" in which: sheetA()
    if "b" in which: sheetB()
    if "c" in which: sheetC()
    print("ROWLEN", ROWLEN)
