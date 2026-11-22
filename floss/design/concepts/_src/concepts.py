"""floss concept round 1 (visual): BOW, KEPT, TIDE. Geometry + sheets.  Run: python3 -I concepts.py [bow kept tide compare]
Layouts follow systems' how-it-works rev 1 panel maps, with the visual changes listed in each how-it-looks-and-feels.md."""
import sys, math
import numpy as np
from fl import *

def T(x, y, k, w="", **kw):
    d = dict(k=k, x=x, y=y, w=w); d.update(kw); return d

OCT = "−2 · −1 · 0 · +1 · +2"
PRESS = "swell · vibrato · tone · shimmer"
PRESS_T = "drift · swell · tone · shimmer"
SHIM = "analog · wide · glass · tape"

# ------------------------------------------------------------------ BOW: CATHEDRAL base + sound lid
BOW = dict(name="bow", W=286.0, D=132.0, H=27.6, axis=143.0, case_r=28.0, plate_in=4.3, plate_r=24.0,
    style=dict(knob=INK, ink="#2a2420", key_w=EBONY, key_s=BONE, collar="#a39680", tab=BONE),
    keys=dict(kind="peg", yw=22.0, ys=44.0, d=12.7),
    ctrls=[
        T(22, 68, "octave", "octave", pos=OCT, d=14.0), T(48, 68, "knob", "tone", d=10), T(74, 68, "knob", "depth", d=10), T(100, 68, "hold", "hold"),
        T(22, 93, "knob", "attack", d=10), T(48, 93, "knob", "release", d=10), T(74, 93, "sel4", "pressure", pos=PRESS, col=CORAL, d=10, ang=-45),
        T(100, 93, "sel4", "shimmer", pos=SHIM, d=10, ang=-45),
        T(186, 68, "knob", "echo", d=10), T(212, 68, "knob", "reverb", d=10), T(238, 68, "knob", "volume", d=10), T(264, 68, "octave", "octave", pos=OCT, d=14.0),
        T(186, 93, "knob", "time", d=10), T(212, 93, "toggle", "tempo", pos="free · sync"), T(238, 93, "knob", "repeats", d=10), T(264, 93, "blank"),
        T(143, 101, "tap", "tap"),
    ] + [T(124.5, y, "tab", on=o) for y, o in ((60, 1), (72, 1), (84, 0))] + [T(161.5, y, "tab", on=o) for y, o in ((60, 0), (72, 1), (84, 1))],
    gutter_words=[(143, 60, "low"), (143, 72, "main"), (143, 84, "high")])

# ------------------------------------------------------------------ KEPT: ONE SHEET slab
KEPT = dict(name="kept", W=276.0, D=148.0, H=24.0, axis=138.0, case_r=12.0,
    style=dict(knob=PETG, knob_line=INK, ink="#2e2924", key_w="#fbfaf6", key_s=INK, ripple=True, tab="#f4efe4"),
    keys=dict(kind="cap", yw0=3.0, yw1=27.0, ys0=31.0, ys1=50.0),
    ctrls=[
        T(22, 68, "octave", "octave", pos=OCT), T(45, 68, "tab", "bass", on=1), T(67, 68, "tab", "strings", on=1), T(89, 68, "tab", "brass", on=0),
        T(111, 68, "hold", "hold"), T(138, 68, "tap", "tap"),
        T(165, 68, "knob", "depth", col=CORAL), T(187, 68, "knob", "echo"), T(209, 68, "knob", "reverb"), T(231, 68, "knob", "volume"), T(254, 68, "octave", "octave", pos=OCT),
        T(45, 100, "knob", "attack"), T(67, 100, "knob", "release"), T(89, 100, "sel4", "pressure", pos=PRESS, ang=15), T(111, 100, "blank"),
        T(165, 100, "sel4", "ensemble", pos=SHIM, ang=-45), T(187, 100, "knob", "time"), T(209, 100, "toggle", "tempo", pos="free · sync"), T(231, 100, "knob", "repeats"),
    ])

# ------------------------------------------------------------------ TIDE: HUSH felt pebble
TIDE = dict(name="tide", W=290.0, D=186.0, H=25.5, axis=145.0,
    style=dict(knob="#efe7d6", knob_line=INK, ink="#3b3732", key_w=MAPLE, key_s="#b98f55", collar=FELT_D, tag=FELT_TAG),
    keys=dict(kind="peg", yw=20.0, ys=43.0, d=12.7),
    ctrls=[
        T(24, 72, "octave", "octave", pos=OCT), T(52, 72, "knob", "tone"), T(80, 72, "sel4", "shimmer", pos=SHIM, ang=-45), T(108, 72, "knob", "depth", ang=30),
        T(52, 102, "knob", "attack"), T(80, 102, "knob", "release", ang=60), T(108, 102, "sel4", "pressure", pos=PRESS_T, ang=-45), T(24, 102, "blank"),
        T(145, 70, "peg", "hold", d=16.0), T(145, 106, "knob", "drift", col=CORAL, d=24.0, ang=40), T(145, 134, "light"),
        T(182, 72, "knob", "echo", ang=-30), T(210, 72, "knob", "reverb", ang=20), T(238, 72, "tap", "tap", ring="#4b4741"), T(266, 72, "octave", "octave", pos=OCT),
        T(182, 102, "knob", "repeats"), T(210, 102, "knob", "time"), T(238, 102, "toggle", "tempo", pos="free · sync"), T(266, 102, "knob", "volume"),
    ])

# ------------------------------------------------------------------ prims
def key_prims(C, z):
    st, k = C["style"], C["keys"]; ps = []
    if k["kind"] == "peg":
        wh, sh, x0 = key_xy(C["axis"], k["yw"], k["ys"])
        for x, y in wh: ps += peg_prims(x, y, z, k["d"], st["key_w"], collar=st.get("collar"))
        for x, y in sh: ps += peg_prims(x, y, z, k["d"] - 0.7, st["key_s"], collar=st.get("collar"), h=7.5)
    else:
        wh, sh, x0 = key_xy(C["axis"], 0, 0)
        for x, _ in wh: ps.append(Prim(rrect(-8.3, k["yw0"], 16.6, k["yw1"] - k["yw0"], 1.2), 2.5, "#dcd9d2", st["key_w"], o=(x, 0, z), layer=2))
        for x, _ in sh: ps.append(Prim(rrect(-5.5, k["ys0"], 11, k["ys1"] - k["ys0"], 1.0), 4.5, "#111", "#2a2827", o=(x, 0, z), layer=2))
    return ps

def body_prims(C, labels=True):
    n = C["name"]; W, D, H = C["W"], C["D"], C["H"]; st = C["style"]; ps = []
    def plate_dec(ax, cam, pr, zf):
        ink = st["ink"]
        if n == "bow":
            for x, y, s in C["gutter_words"]: ptext(ax, cam, pr, zf, s, x, y, 2.4, ink, font=FONT_B)
        if n == "kept":
            xs = C["axis"]
            for x in np.arange(xs - 40, xs + 41, 2.8): pline(ax, cam, pr, zf, [(x, 124), (x, 140)], "#3a342c", 0.9)
            pline(ax, cam, pr, zf, [(12, 55), (52, 55)], "#cdbf9f", 0.9); pline(ax, cam, pr, zf, [(246, 55), (264, 55)], "#cdbf9f", 0.9)
        if n == "tide":
            lantern(ax, cam, pr, zf)
        if labels:
            for c in C["ctrls"]:
                if c.get("w") and c["k"] not in ("blank",):
                    r = c.get("d", KN_D) / 2 if c["k"] in ("knob", "octave", "sel4") else (7 if c["k"] == "tap" else 6)
                    ptext(ax, cam, pr, zf, c["w"], c["x"], c["y"] + r + 4.6, 2.5, ink, font=FONT_B)
        # rim tick: the only split mark
        xs = C["axis"] - 9
        ppoly(ax, cam, pr, zf, [(xs - 0.6, 0.6), (xs + 0.6, 0.6), (xs + 0.6, 4.2), (xs - 0.6, 4.2)], CORAL)
    if n == "bow":
        ps.append(Prim(rrect(0, 0, W, D, C["case_r"]), H - 0.6, WAL, WAL, layer=0, dark=0.55))
        ps.append(Prim(rrect(C["plate_in"], C["plate_in"], W - 2 * C["plate_in"], D - 2 * C["plate_in"], C["plate_r"]), 0.6, CREAM, CREAM, o=(0, 0, H - 0.6), layer=1, decor=plate_dec))
    elif n == "kept":
        ps.append(Prim(rrect(0, 0, W, D, C["case_r"]), H, "#d9cbb0", PETG, layer=0, round_top=1.5, decor=plate_dec, dark=0.7))
    else:
        ps.append(Prim(rrect4(0, 0, W, D, 16, 44), H, FELT, FELT, layer=0, round_top=9.0, decor=plate_dec, dark=0.62, step=0.5))
    z = H
    ps += key_prims(C, z)
    for c in C["ctrls"]:
        if C["style"].get("tag") and c["k"] in ("knob", "octave", "sel4"):
            ps.append(Prim(circle(0, 0, c.get("d", KN_D) / 2 + 2.6), 0.3, FELT_TAG, FELT_TAG, o=(c["x"], c["y"], z), layer=1))
        ps += control_prims(c, z + (0.3 if C["style"].get("tag") else 0), C["style"])
    return ps

def lantern(ax, cam, pr, zf, holes=True):
    cx = 145.0
    for r, a in ((26, 0.10), (18, 0.14), (10, 0.18)):
        for gx in (124, 145, 168):
            ppoly(ax, cam, pr, zf, circle(gx, 156, r, 30), (1.0, 0.82, 0.55, a))
    rng = np.random.default_rng(4)
    for j, y in enumerate(np.arange(142, 171, 3.0)):
        for x in np.arange(cx - 42 + (1.6 if j % 2 else 0), cx + 42, 3.2):
            warm = math.exp(-((x - 128) ** 2 + (y - 156) ** 2) / 300) + 0.7 * math.exp(-((x - 162) ** 2 + (y - 152) ** 2) / 250)
            col = "#ffd28a" if warm > 0.45 + 0.1 * rng.random() else "#5d5850"
            ppoly(ax, cam, pr, zf, circle(x, y, 0.85, 10), col)

def lid_prims(C, opened=True):
    W, D, H = C["W"], C["D"], C["H"]; LT = 22.0
    def dec(ax, cam, pr, zf):
        ppoly(ax, cam, pr, zf, rrect(6.5, 6.5, W - 13, D - 13, 22), CLOTH)
        for t in np.arange(9, D - 8, 1.6): pline(ax, cam, pr, zf, [(10, t), (W - 10, t)], "#d6ccb6", 0.25)
        pline(ax, cam, pr, zf, [(8, 20), (W - 8, 20)], CORAL, 0.9)
    if opened:
        n = np.array([0, -math.sin(math.radians(60)), math.cos(math.radians(60))])      # toward player
        ey = np.array([0, math.cos(math.radians(60)), math.sin(math.radians(60))])      # up the lid
        o = np.array([0, D + 4, H + 2]) - n * LT
        return [Prim(rrect(0, 0, W, D, C["case_r"]), LT, WAL, WAL, o=o, ex=(1, 0, 0), ey=ey, n=n, layer=-1, decor=dec, dark=0.55)]
    return []

def closed_prims(C):
    W, D, H = C["W"], C["D"], C["H"]
    def dec(ax, cam, pr, zf):
        for yy in (D * 0.30, D * 0.30 + 8): pline(ax, cam, pr, zf, [(34, yy), (W - 34, yy)], BRASS, 0.8)
        ppoly(ax, cam, pr, zf, rrect(40, 52, W - 80, 58, 6), shade(WAL, 1.06))
        ptext(ax, cam, pr, zf, "the owner's façade field (blank)", W / 2, 81, 4.0, "#8f6d52")
    return [Prim(rrect(0, 0, W, D, C["case_r"]), 2 * H - 0.4, WAL, WAL, layer=0, dark=0.55, decor=dec)]

# ------------------------------------------------------------------ plan (1:1)
def plan(ax, C, ox, oy, labels=True):
    st = C["style"]; W, D = C["W"], C["D"]; n = C["name"]
    import matplotlib.transforms as mt
    sub = ax  # draw in mm with an offset
    def P(pts): return [(x + ox, y + oy) for x, y in pts]
    if n == "bow":
        ax.add_patch(Polygon(P(rrect(0, 0, W, D, C["case_r"])), fc=WAL, ec="none"))
        ax.add_patch(Polygon(P(rrect(4.3, 4.3, W - 8.6, D - 8.6, 24)), fc=CREAM, ec="none"))
    elif n == "kept":
        ax.add_patch(Polygon(P(rrect(0, 0, W, D, C["case_r"])), fc=PETG, ec="#cdbf9f", lw=0.4))
        for x in np.arange(C["axis"] - 40, C["axis"] + 41, 2.8): ax.add_patch(Rectangle((x - 0.8 + ox, 124 + oy), 1.6, 16, fc="#3a342c", ec="none"))
        for x0, x1 in ((12, 52), (246, 264)): ax.add_patch(Rectangle((x0 + ox, 54.4 + oy), x1 - x0, 1.2, fc="#d6c8aa", ec="none"))
    else:
        ax.add_patch(Polygon(P(rrect4(0, 0, W, D, 16, 44)), fc=FELT, ec="none"))
        ax.add_patch(Polygon(P(inset(rrect4(0, 0, W, D, 16, 44), 9)), fc=shade(FELT, 1.04), ec="none"))
        cx = C["axis"]
        for r, a in ((26, 0.12), (18, 0.16), (10, 0.2)):
            for gx in (124, 145, 168): ax.add_patch(Circle((gx + ox, 156 + oy), r, fc=(1, 0.82, 0.55, a), ec="none"))
        for j, y in enumerate(np.arange(142, 171, 3.0)):
            for x in np.arange(cx - 42 + (1.6 if j % 2 else 0), cx + 42, 3.2):
                warm = math.exp(-((x - 128) ** 2 + (y - 156) ** 2) / 300) + 0.7 * math.exp(-((x - 162) ** 2 + (y - 152) ** 2) / 250)
                ax.add_patch(Circle((x + ox, y + oy), 0.85, fc=("#ffd28a" if warm > 0.5 else "#5d5850"), ec="none"))
    # keys
    k = C["keys"]
    if k["kind"] == "peg":
        wh, sh, x0 = key_xy(C["axis"], k["yw"], k["ys"])
        for (x, y), col, d in [(p, st["key_w"], k["d"]) for p in wh] + [(p, st["key_s"], k["d"] - 0.7) for p in sh]:
            if st.get("collar"): ax.add_patch(Circle((x + ox, y + oy), d / 2 + 2, fc=st["collar"], ec="none"))
            ax.add_patch(Circle((x + ox, y + oy), d / 2, fc=col, ec=shade(col, 0.8), lw=0.4))
    else:
        wh, sh, x0 = key_xy(C["axis"], 0, 0)
        for x, _ in wh: ax.add_patch(FancyBboxPatch((x - 8.3 + ox, k["yw0"] + oy), 16.6, k["yw1"] - k["yw0"], boxstyle="round,pad=0,rounding_size=1.2", fc=st["key_w"], ec="#bdb6a8", lw=0.4))
        for x, _ in sh: ax.add_patch(FancyBboxPatch((x - 5.5 + ox, k["ys0"] + oy), 11, k["ys1"] - k["ys0"], boxstyle="round,pad=0,rounding_size=1.0", fc="#222", ec="none"))
    # rim tick
    xs = C["axis"] - 9; ax.add_patch(Rectangle((xs - 0.6 + ox, oy + 0.4), 1.2, 3.8, fc=CORAL, ec="none"))
    shifted = [dict(c, x=c["x"] + ox, y=c["y"] + oy) for c in C["ctrls"]]
    plan_controls(ax, shifted, st)
    for x, y, s in C.get("gutter_words", []): plan_text(ax, x + ox, y + oy, s, 2.4, st["ink"], va="center", font=FONT_B)

# ------------------------------------------------------------------ sheets
def sheet_look(C, title, idea, principles, facts, extra=None, cam=Cam(30, 33), out=None):
    fig = plt.figure(figsize=(16.54, 11.69), dpi=160); fig.patch.set_facecolor(PAPER)
    ax = fig.add_axes([0.0, 0.17, 0.66, 0.76]); ax.set_facecolor(PAPER)
    prims = body_prims(C) + (lid_prims(C) if C["name"] == "bow" else [])
    render(ax, cam, prims)
    fig.text(0.03, 0.955, title, fontsize=17, weight="bold", family="Inter")
    fig.text(0.03, 0.928, idea, fontsize=10.5, family="Inter", color="#3a3530")
    x0 = 0.665; y = 0.885
    fig.text(x0, y, "Principles", fontsize=11.5, weight="bold", family="Inter"); y -= 0.028
    for head, why in principles:
        fig.text(x0, y, head, fontsize=9.6, weight="bold", family="Inter"); y -= 0.019
        for line in why: fig.text(x0 + 0.008, y, line, fontsize=8.6, family="Inter", color="#3a3530"); y -= 0.0175
        y -= 0.008
    y -= 0.01; fig.text(x0, y, "Facts", fontsize=11.5, weight="bold", family="Inter"); y -= 0.025
    for f_ in facts: fig.text(x0, y, f_, fontsize=8.6, family="Inter", color="#3a3530"); y -= 0.0175
    if extra: extra(fig)
    fig.text(0.03, 0.012, "floss · concept round 1 · visual · 2026-11-22 · slice-stacked orthographic drawing, not a photoreal render · legends: Inter stand-in for Kalam",
             fontsize=7.5, color=GREY, family="Inter")
    fig.savefig(out, facecolor=fig.get_facecolor()); plt.close(fig)

def sheet_real(C, title, notes, out):
    fig, ax = a3_mm()
    ox, oy = 20.0, 297 - 30 - C["D"]
    plan(ax, C, ox, oy)
    plan_text(ax, 20, 285, title, 6.0, INK, ha="left", font=FONT_B)
    plan_text(ax, 20, 278.5, f"real size, top view · {C['W']:.0f} × {C['D']:.0f} mm · front edge at the bottom", 3.2, GREY, ha="left")
    # axis + gutter guides (outside the body only)
    ax.plot([ox + C["axis"]] * 2, [oy - 9, oy - 2], color=GREY, lw=0.5); plan_text(ax, ox + C["axis"], oy - 13, "axis = centre of middle C", 2.2, GREY)
    ax.plot([ox + C["axis"] - 9] * 2, [oy - 6, oy - 1], color=CORAL, lw=0.8); plan_text(ax, ox + C["axis"] - 11, oy - 7.5, "B | C", 2.2, CORAL, ha="right")
    scale_bar(ax, 20, 14)
    y = oy - 26
    for s in notes:
        plan_text(ax, 20, y, s, 2.9, INK if not s.startswith("  ") else "#4a443d", ha="left"); y -= 5.0
    nx = ox + C["W"] + 12
    fig.savefig(out, facecolor=fig.get_facecolor()); plt.close(fig)

def bow():
    C = BOW
    def extra(fig):
        a2 = fig.add_axes([0.03, 0.03, 0.28, 0.16]); render(a2, Cam(30, 33), closed_prims(C))
        fig.text(0.04, 0.19, "Closed: the same brick as Big Energy (CATHEDRAL); the lid's back is the owner's field", fontsize=8.5, family="Inter")
        a3 = fig.add_axes([0.33, 0.03, 0.30, 0.16]); a3.axis("off"); a3.set_xlim(-20, 300); a3.set_ylim(-10, 140); a3.set_aspect("equal")
        a3.add_patch(Rectangle((0, 0), 132, 27.6, fc=WAL, ec="none"))
        import matplotlib.patches as mp
        a = math.radians(60); n = np.array([0, -math.sin(a), math.cos(a)])
        p0 = np.array([132 + 4, 29.6]); ey = np.array([math.cos(a), math.sin(a)]); nn = np.array([-math.sin(a), math.cos(a)])
        lid = [p0 - nn * 22, p0 - nn * 22 + ey * 132, p0 + ey * 132, p0]
        a3.add_patch(Polygon(lid, fc=WAL, ec="none"))
        a3.plot(*zip(p0 + ey * 6, p0 + ey * 126), color=CLOTH, lw=3.5)
        st0 = p0 - nn * 22 + ey * 70; a3.plot([st0[0], st0[0] + 48], [st0[1], 0], color=BRASS, lw=1.8)
        for s in (0.3, 0.55, 0.8):
            q = p0 + ey * 132 * s + nn * 3; a3.annotate("", xy=(q[0] - 46, q[1] - 14), xytext=q, arrowprops=dict(arrowstyle="->", color=GREY, lw=0.8))
        a3.text(0, 128, "Standing (side): CATHEDRAL's 120°, cloth toward you", fontsize=8.5, family="Inter")
        a3.text(-15, -8, "← you", fontsize=7.5, color=GREY, family="Inter")
    sheet_look(C, "BOW  ·  life lives in each finger",
        "CATHEDRAL's base and hinge; the lid has no controls: it's the voice. Dark keys you lean into; one coral knob says what a lean does.",
        [("1  The lid is the voice, not a second panel.", ["Because floss needs half Big Energy's controls; the freed lid holds the", "sealed box (driver + passive radiator) and faces you when it stands."]),
         ("2  Above each half, its own.", ["Because the split is the instrument: octaves at the outer ends, each half's", "strands in a column beside the gutter, the shared things on the axis."]),
         ("3  The keys are a fingerboard.", ["Because every note is bowed: ebony-dark naturals, bone sharps (a violin's", "fingerboard and nut), on felt collars so a lean gives a little."]),
         ("4  Coral is where the life lives: pressure.", ["Because BOW's whole idea is what your finger does after the strike."]),
         ("5  Open is on.", ["Because the lid already says 'playing' or 'packed'. Closed covers the", "keys, so it can't switch on in a bag."])],
        ["Base 286 × 132 × 27.6 (CATHEDRAL); lid ≈ 22 deep, no knobs.", "Closed ≈ 55 (as CATHEDRAL; eng to confirm with the lid box).",
         "Knobs: the family's low Ø 10 × 8 (black); octave Ø 14 × 8 (part to pick).", "Keys: CATHEDRAL carrier, dark-stained birch heads Ø 12.7; bone sharps.",
         "Tabs: 6 mini rockers 15 × 10, in two columns of three.", "TAP's bezel is the status light (CATHEDRAL precedent).",
         "Coral: no bought coral knob checked yet (open).", "Lid inner face: oatmeal speaker cloth, one coral thread, no motif."],
        extra=extra, cam=Cam(28, 30), out="../bow/mock-A-look.png")
    sheet_real(C, "BOW · real-size panel (base)", [
        "Left of the gutter: the left half's octave (outer end) and its strands column; HOLD (left half only) at the inner end of the front row.",
        "Right of the gutter: the right half's strands column; its octave at the outer end.  Shared: front row amounts, rear row kinds and times.",
        "Gutter (18 mm, over middle C): strand names once (low · main · high, low nearest the keys), TAP whose ring is the status light.",
        "Signal order, rear row left to right: attack · release · pressure (coral) · shimmer | tap | time · tempo · repeats · (blank, kept blank).",
        "The only split mark is the coral tick on the front rim between B and C.  Positions are systems' rev 1 map; tabs shown cello-left / violins-right."],
        "../bow/mock-B-real-size.png")

def kept():
    C = KEPT
    def extra(fig):
        a3 = fig.add_axes([0.03, 0.03, 0.6, 0.15]); a3.axis("off"); a3.set_xlim(-10, 300); a3.set_ylim(-8, 40); a3.set_aspect("equal")
        a3.add_patch(FancyBboxPatch((0, 0), 276, 24, boxstyle="round,pad=0,rounding_size=1.5", fc="#d9cbb0", ec="none"))
        for i in range(15): a3.add_patch(Rectangle((3 + 18 * i + 0.7, 24), 16.6, 2.5, fc="#fbfaf6", ec="#bdb6a8", lw=0.3))
        for x in (22, 45, 67, 89, 111, 165, 187, 209, 231, 254): a3.add_patch(Rectangle((x - 7, 24), 14, 12, fc=(CORAL if x == 165 else PETG), ec="#b9ab8e", lw=0.3))
        a3.text(0, 38, "Front elevation (schematic): one low slab; keys stand 2.5 proud at the front edge (ONE SHEET edge A)", fontsize=8.5, family="Inter")
    sheet_look(C, "KEPT  ·  life lives in 1974",
        "ONE SHEET's single printed shell, read like a string machine: tabs first, then the ensemble. Everything new is under the fingers.",
        [("1  It looks like a string machine.", ["Because KEPT asks whether he wants floss to look new or feel new; this", "face answers 'feel new', so the panel can be one a 1974 player knows."]),
         ("2  If it turns, it ripples.", ["Because ONE SHEET's rule costs nothing: rings round every rotary, smooth", "everywhere else (tabs, hold, tap, keys)."]),
         ("3  The bass belongs to the left.", ["Because bass only sounds on the left half: its tab sits next to OCTAVE L,", "joined by a sunk groove; OCTAVE R has its own short groove."]),
         ("4  Coral is the ensemble.", ["Because the BBD ensemble is what made 1974 strings sound like strings."]),
         ("5  Ordinary keys.", ["Because nothing on the face should look clever: white and black keys,", "the only concept that looks like a keyboard."])],
        ["Shell 276 × 148 × 24, one filament (cream PETG), one swap for legends.", "Knobs: cream KN1250 Ø 14.9; DEPTH coral (part open).",
         "Keys: ONE SHEET's caps, white and black, 2.5 / 4.5 proud.", "Tabs: 3 mini rockers 15 × 10.  Grille: slots across the back band.",
         "TAP's ring is the status light.  No passive radiator (honest trade).", "Needs a sleeve for the bag (cost open, as Big Energy's ONE SHEET)."],
        extra=extra, cam=Cam(30, 34), out="../kept/mock-A-look.png")
    sheet_real(C, "KEPT · real-size panel", [
        "Front row, the Solina's order: octave L · bass · strings · brass · hold | tap | depth (coral) · echo · reverb · volume · octave R.",
        "Rear row: attack · release · pressure · (blank) | — | ensemble (behind depth) · time · tempo · repeats.",
        "Sunk grooves (0.6 × 1.2): under OCTAVE L + bass (the left half's pair) and under OCTAVE R.  Rings round every rotary; smooth elsewhere.",
        "Visual change to systems' map: attack / release move to the rear row (front row was 5 + 5 dense), ensemble sits behind depth,",
        "  volume moves to the front; the rear-left blank stays blank.  The rim tick between B and C is the only split mark."],
        "../kept/mock-B-real-size.png")

def tide():
    C = TIDE
    def extra(fig):
        a3 = fig.add_axes([0.03, 0.03, 0.6, 0.15]); a3.axis("off"); a3.set_xlim(-10, 300); a3.set_ylim(-14, 46); a3.set_aspect("equal")
        prof = [(0, 0), (290, 0)] + [(290 - 9 + 9 * math.cos(t), 25.5 - 9 + 9 * math.sin(t)) for t in np.linspace(0, math.pi / 2, 10)] + \
               [(9 - 9 * math.cos(t), 25.5 - 9 + 9 * math.sin(t)) for t in np.linspace(math.pi / 2, 0, 10)]
        prof = [(0, 0), (290, 0)] + [(290 - 9 + 9 * math.cos(t), 16.5 + 9 * math.sin(t)) for t in np.linspace(0, math.pi / 2, 10)] + \
               [(9 - 9 * math.cos(math.pi / 2 - t), 16.5 + 9 * math.sin(math.pi / 2 - t)) for t in np.linspace(0, math.pi / 2, 10)]
        a3.add_patch(Polygon(prof, fc=FELT, ec="none"))
        for i in range(15):
            a3.add_patch(Rectangle((10 + 18 * i + 0.6, 25.5), 16.7, 1.2, fc=FELT_D, ec="none")); a3.add_patch(Rectangle((10 + 18 * i + 2.6, 25.5 + 1.2), 12.7, 6.5, fc=MAPLE, ec="none"))
        a3.add_patch(Rectangle((137, 25.5), 16, 8.2, fc=MAPLE, ec="none"))
        for x in (40, 250): a3.add_patch(Rectangle((x - 8, -3), 16, 3, fc="#5a564f", ec="none"))
        a3.text(0, 40, "Front elevation: a soft stone; felt everywhere but what you play; a foot ring keeps the radiator off a lap (eng)", fontsize=8.5, family="Inter")
    sheet_look(C, "TIDE  ·  life lives in time",
        "HUSH's felt pebble. Plant notes, then tend them: the coral DRIFT is the hero, and warm light breathes out of the speaker holes.",
        [("1  A stone you set down and tend.", ["Because TIDE is played less than it's looked after: soft, heavy-feeling,", "nothing hard but what you touch, every word pressed blind."]),
         ("2  HOLD is a key.", ["Because in TIDE every note you play joins the chord: a 26th maple peg on", "its own felt collar, on the axis, nearest the keys."]),
         ("3  Coral is drift.", ["Because the life is in how the notes wander: one large coral knob,", "on the axis, the only big thing on the face."]),
         ("4  The light comes out where the sound does.", ["Because the lantern follows the ensemble's three phases through the", "speaker holes; it never shows state. Amber = analog, paler = Daisy."]),
         ("5  Same grammar as BOW.", ["Because the family should read alike: amounts in front, ranges and times", "behind, octaves at the outer ends."])],
        ["Pebble 290 × 186 × 25.5 (HUSH), rear corners R 44, top round-over r 9.", "Felt: mid-grey undyed wool; tags light warm grey; words pressed.",
         "Knobs: cream KN1250 Ø 14.9 on tags; DRIFT Ø 24, coral (part open).", "Keys: HUSH maple pegs Ø 12.7 on felt collars; HOLD a Ø 16 peg.",
         "Lantern: 3 warm LEDs behind the punched speaker field (≈ 84 × 30).", "Status light on the axis behind DRIFT; TAP is in the echo group.",
         "Passive radiator in the domed underside (direction: eng).", "Needs a sleeve for the bag (as HUSH)."],
        extra=extra, cam=Cam(30, 36), out="../tide/mock-A-look.png")
    sheet_real(C, "TIDE · real-size panel", [
        "Front: octave L · tone · shimmer · depth | HOLD peg | echo · reverb · tap · octave R.   Rear: (blank) · attack · release · pressure | DRIFT | repeats · time · tempo · volume.",
        "Centre band 28 mm (wider than BOW's 18): HOLD nearest the keys, DRIFT (coral, Ø 24) behind it, the status light behind DRIFT.",
        "Visual change to systems' map: rebalanced 4 | 4 front and 3–4 | 4 rear; TAP moves to the front (it's played), FREE / SYNC sits beside",
        "  TIME and behind TAP; the shimmer pair and tone move left, next to touch (signal order).  The rim tick marks B | C."],
        "../tide/mock-B-real-size.png")

def compare():
    fig, ax = a3_mm()
    s = 0.62
    import matplotlib.transforms as mt
    plan_text(ax, 20, 284, "floss · three concepts, one family · plans at the same scale (≈ 1:2.4 on A3) · round 1", 6.0, INK, ha="left", font=FONT_B)
    for i, (C, t) in enumerate([(BOW, "BOW · CATHEDRAL base, lid = voice"), (KEPT, "KEPT · ONE SHEET slab"), (TIDE, "TIDE · HUSH felt pebble")]):
        sub = fig.add_axes([0.03 + i * 0.325, 0.30, 0.30, 0.55]); sub.set_facecolor(PAPER); sub.axis("off")
        sub.set_xlim(-5, 295); sub.set_ylim(-5, 190); sub.set_aspect("equal")
        plan(sub, C, 0, 0)
        sub.set_title(t, fontsize=10, family="Inter", loc="left")
    rows = [("", "BOW", "KEPT", "TIDE"),
            ("life lives in", "each finger", "1974", "time"),
            ("body", "CATHEDRAL case; lid = speaker box", "ONE SHEET printed shell", "HUSH felt pebble"),
            ("keys", "dark naturals, bone sharps, felt", "white and black caps", "maple pegs on felt"),
            ("coral", "pressure", "ensemble depth", "drift (large, on the axis)"),
            ("knobs", "black low Ø 10", "cream Ø 14.9, rings", "cream Ø 14.9 on felt tags"),
            ("speaker", "cloth lid + radiator", "back-band slots, no radiator", "punched felt + lantern + radiator"),
            ("carry", "lid closes over the keys", "sleeve", "sleeve")]
    y = 80
    for r in rows:
        for j, cell in enumerate(r):
            plan_text(ax, [20, 70, 175, 285][j], y, cell, 3.0, INK if (j == 0 or y == 80) else "#3a3530", ha="left", font=FONT_B if (j == 0 or y == 80) else FONT)
        y -= 7.5
    fig.savefig("../compare-faces.png", facecolor=fig.get_facecolor()); plt.close(fig)

if __name__ == "__main__":
    jobs = sys.argv[1:] or ["bow", "kept", "tide", "compare"]
    for j in jobs: globals()[j](); print("done", j)
