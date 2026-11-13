#!/usr/bin/env python3
"""Compose A3 mock sheets (SVG in mm) and render to PNG. Round 2."""
import base64, math, os, subprocess, textwrap
from PIL import Image
from drawings import t, rect, line, circ, esc, INK, MUTE, ACC, PAPER, dim_h, dim_v
from ld import W, D, KNOBS, TOGGLES, KNOB_D, HERO_D, GAP_CENTRES, white_keys, sharp_keys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
ROOT = os.path.dirname(HERE)
DPI = 300
BLUE = "#3d6e8f"; SPLIT_X = 121.0
SHEET_TAG = "concept mocks, round 2 · name to come"

def img(path, x, y, w, h, exact=False):
    im = Image.open(path)
    iw, ih = im.size
    if exact:
        dw, dh, ox, oy = w, h, x, y
    else:
        s = min(w / iw, h / ih)
        dw, dh = iw * s, ih * s
        ox, oy = x + (w - dw) / 2, y + (h - dh) / 2
    with open(path, "rb") as f:
        b = base64.b64encode(f.read()).decode()
    return (f'<image x="{ox:.2f}" y="{oy:.2f}" width="{dw:.2f}" height="{dh:.2f}" preserveAspectRatio="none" '
            f'href="data:image/png;base64,{b}"/>'), (ox, oy, dw, dh)

def para(x, y, text, width_chars, size=2.9, lead=1.32, fill=INK, weight="normal", style="normal", family="Inter"):
    out = []; yy = y
    for p in text.split("\n"):
        for ln in textwrap.wrap(p, width_chars) or [""]:
            out.append(t(x, yy, ln, size, fill, weight=weight, style=style, family=family))
            yy += size * lead
    return "\n".join(out), yy

def head(title, kind, idea, page, rnd=2):
    s = [rect(0, 0, 420, 297, PAPER, "none", 0)]
    s.append(t(12, 17, title, 9.5, INK, weight="bold"))
    s.append(t(12, 24.5, kind, 3.4, ACC, weight="bold"))
    s.append(t(408, 17, f"concept mocks, round {rnd} · name to come", 3.2, MUTE, "end"))
    s.append(t(408, 23, page, 3.0, MUTE, "end"))
    body, _ = para(12, 31.5, idea, 190, 3.2, fill=INK, style="italic", family="DejaVu Serif")
    s.append(body)
    s.append(line(12, 37.5, 408, 37.5, "#d8d0c2", 0.3))
    return s

def write(svg_parts, name, folder):
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="420mm" height="297mm" viewBox="0 0 420 297">\n'
           + "\n".join(svg_parts) + "\n</svg>")
    os.makedirs(folder, exist_ok=True)
    sp = os.path.join(OUT, os.path.basename(folder) + "-" + name + ".svg")
    with open(sp, "w") as f:
        f.write(svg)
    png = os.path.join(folder, name + ".png")
    subprocess.run(["rsvg-convert", "-d", str(DPI), "-p", str(DPI), sp, "-o", png], check=True)
    return png

# ------------------------------------------------------------------ small explanatory insets (SVG, mm)
def wear_inset(x, y, w, h):
    s = [rect(x, y, w, h, "#ece7de", "#d8d0c2", 0.25)]
    bx, by = x + 4, y + 4
    s.append(rect(bx, by, 74, 17, "#8d8b88", INK, 0.2))
    s.append(rect(bx, by + 17, 74, 5, "#6f6d6a", INK, 0.2))
    s.append(t(bx + 1, by + 20.8, "palm strip", 1.9, "#f1ece2"))
    for k in range(3):
        cx = bx + 10 + k * 18
        s.append(circ(cx, by + 8.5, 9.5, "#74726f", INK, 0.2))
        s.append(circ(cx, by + 8.5, 6.35, "#e2c290", INK, 0.25))
    s.append(circ(bx + 64, by + 8.5, 9.5, "none", INK, 0.2, dash="0.8 0.6"))
    s.append(circ(bx + 88, by + 8.5, 9.5, "#74726f", INK, 0.25))
    s.append(circ(bx + 88, by + 8.5, 4.6, "#ece7de", INK, 0.2))
    s.append(line(bx + 70, by + 8.5, bx + 77, by + 8.5, ACC, 0.3))
    p, _ = para(x + 104, y + 6, "Palm strip: one felt strip, tucked under the shell's front lip; swap it when grubby. Collars: 19 mm felt washers punched from the felt sheet's offcut, with a 1 mm clearance hole so they never grip the peg (eng E-L5). Lift the peg cap, swap the collar. Both cost $0: they come from the same sheet.", 62, 2.1)
    s.append(p)
    return "\n".join(s)

def bed_inset(x, y, w, h):
    s = [rect(x, y, w, h, "#ece7de", "#d8d0c2", 0.25)]
    sc = 0.115
    for k, (lab, pw, note) in enumerate([("L", SPLIT_X, "I–II, stick, keys 1–6"), ("R", W - SPLIT_X, "III–V, keys 6–15")]):
        bx, by = x + 4 + k * (250 * sc + 5), y + 3.5
        s.append(rect(bx, by, 250 * sc, 210 * sc, "#d9d6cf", INK, 0.25))
        px, py = bx + (250 * sc - 180 * sc) / 2, by + (210 * sc - pw * sc) / 2
        s.append(rect(px, py, 180 * sc, pw * sc, "#e8dcc2", INK, 0.3))
        s.append(t(px + 90 * sc, py + pw * sc / 2 + 1.4, lab, 4, "#5b4a39", "middle", weight="bold"))
        s.append(t(bx, by + 210 * sc + 3, f"bed {k+1}: {note}", 1.8, INK))
    p, _ = para(x + 70, y + 6, "Two jobs on a Prusa 250 × 210 bed: each half deck-down, rotated 90° (its 180 along the bed's 250, its width along the 210). One filament swap (M600) after layer 3 makes the legends. Part name, half, revision and date are printed on the face. The 3MF is the parts list.", 64, 2.1)
    s.append(p)
    return "\n".join(s)

def fold_inset(x, y, w, h):
    """r3: side views (open; closed 51 as drawn with the ~44 floor) + the five-plate alternative as a small top view."""
    s = [rect(x, y, w, h, "#ece7de", "#d8d0c2", 0.25)]
    sc = 0.26
    def R(y0, z0, y1, z1, fill, ox, oz, dash=None, stroke=INK):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        return (f'<rect x="{ox + min(y0,y1)*sc:.2f}" y="{oz - max(z0,z1)*sc:.2f}" width="{abs(y1-y0)*sc:.2f}" '
                f'height="{abs(z1-z0)*sc:.2f}" fill="{fill}" stroke="{stroke}" stroke-width="0.12"{d}/>')
    DK, WAL, WH, KB, CR = "#2e2f31", "#71492c", "#f4f3ef", "#1c1c1e", "#efe5cb"
    def base(ox, oz):
        g = [R(0, 0, 106, 17.5, DK, ox, oz), R(4, 11.5, 37, 17.5, WAL, ox, oz), R(46, 14.5, 76, 17.5, "#f6f3ec", ox, oz),
             R(78.5, 16.5, 92.5, 19.5, "#62656b", ox, oz)]
        return g
    oz = y + 23.5
    ox = x + 4
    s.append(t(ox, y + 5, "OPEN 180°: one deck", 2.0, INK, weight="bold"))
    s += base(ox, oz)
    s += [R(106, 0, 212, 2, DK, ox, oz), R(106, 14, 209.6, 16.5, WH, ox, oz), R(209.6, 0, 212, 32, DK, ox, oz)]
    s.append(R(147 - 10.4, 17, 147 + 10.4, 29.15, CR, ox, oz))
    for yk in (170, 193):
        s.append(R(yk - 7.25, 17, yk + 7.25, 30.5, KB, ox, oz))
    s.append(circ(ox + 106 * sc, oz - 25.5 * sc, 0.9, "#9a9da1", INK, 0.12))
    s.append(t(ox, oz + 3.0, "keys 17.5 · panel 16.5 · knob tops 30.5", 1.7, MUTE))
    ox2 = x + 66
    s.append(t(ox2, y + 5, "CLOSED: 51 as drawn", 2.0, INK, weight="bold"))
    s += base(ox2, oz)
    s += [R(0, 49, 106, 51, DK, ox2, oz), R(4, 34.5, 103, 37, WH, ox2, oz), R(0, 19, 2.4, 51, DK, ox2, oz)]
    s.append(R(65 - 10.4, 34.0, 65 + 10.4, 21.85, CR, ox2, oz))
    for yk in (42, 19):
        s.append(R(yk - 7.25, 34.0, yk + 7.25, 20.5, KB, ox2, oz))
    zf = 44
    s.append(line(ox2 - 2, oz - zf * sc, ox2 + 106 * sc + 2, oz - zf * sc, ACC, 0.25, dash="0.9 0.6"))
    s.append(t(ox2 + 106 * sc + 2.8, oz - zf * sc + 0.7, "≈ 44 floor", 1.7, ACC, weight="bold"))
    s.append(t(ox2 + 106 * sc + 2.8, oz - 51 * sc + 0.7, "51", 1.7, INK, weight="bold"))
    s.append(t(ox2, oz + 3.0, "298 × 106 × 51 · HYMNAL closes at 38", 1.7, MUTE))
    p, _ = para(x + 113, y + 5, "Closed, every knob lands over the whites or the walnut, never the sharps: the panel sits 12 mm back in the lid. "
                "The ≈ 44 floor needs a 2 mm panel, a 1.6 mm lid back and 10.45 mm knobs everywhere, CUTOFF too; with these black knobs it's ≈ 47.", 44, 1.85, lead=1.3)
    s.append(p)
    ix = x + 192
    s.append(t(ix, y + 5, "ROUND 2 ALTERNATIVE: five plates", 1.8, INK, weight="bold"))
    ii, b = img(os.path.join(OUT, "fo_five.png"), ix, y + 6.5, w - (ix - x) - 3, h - 11)
    s.append(ii)
    s.append(t(ix, y + h - 2.0, "one plate per section, dark mullions", 1.6, MUTE))
    return "\n".join(s)

def toolpath_inset(x, y, w, h):
    """ONE SHEET r3: the first-layer toolpath per region, magnified."""
    s = [rect(x, y, w, h, "#ece7de", "#d8d0c2", 0.25)]
    sz, gap, by = 21.0, 4.0, y + 3.5
    defs = []
    sw_ = [("A", "#e6d9bd", "#c9b893", 45, "I · III · V: +45°"), ("B", "#efe6d1", "#d6c8aa", -45, "II · IV: −45°"),
           ("K", "#efe6d1", "#d6c8aa", None, "under every knob: rings")]
    for k, (nm, base, ln, ang, lab) in enumerate(sw_):
        bx = x + 4 + k * (sz + gap)
        cid = f"tp{k}"
        s.append(f'<clipPath id="{cid}"><rect x="{bx:.2f}" y="{by:.2f}" width="{sz}" height="{sz}"/></clipPath>')
        g = [rect(bx, by, sz, sz, base, "none", 0)]
        pitch = 1.15
        if ang is not None:
            n = int(2 * sz / pitch) + 4
            for i in range(-n, n):
                d = i * pitch
                if ang > 0:
                    g.append(line(bx + d, by + sz, bx + d + sz, by, ln, 0.42))
                else:
                    g.append(line(bx + d, by, bx + d + sz, by + sz, ln, 0.42))
        else:
            n = int(2 * sz / pitch) + 4
            for i in range(-n, n):
                d = i * pitch
                g.append(line(bx + d, by, bx + d + sz, by + sz, ln, 0.42))
            cx, cy = bx + sz / 2, by + sz / 2
            g.append(circ(cx, cy, 9.6, base, "none", 0))
            r = 5.1
            while r <= 9.4:
                g.append(circ(cx, cy, r, "none", ln, 0.42)); r += pitch
            g.append(circ(cx, cy, 4.6, "#ece2c6", INK, 0.2))
        s.append(f'<g clip-path="url(#{cid})">' + "\n".join(g) + "</g>")
        s.append(rect(bx, by, sz, sz, "none", INK, 0.2))
        s.append(t(bx, by + sz + 2.6, lab, 1.75, INK))
    p, _ = para(x + 81, y + 5.5, "Same cream filament, same print. The slicer sets the first layer's direction per region (a modifier for each section and knob), so the "
                "nozzle's lines turn at every section break and circle every knob. On a smooth PEI sheet the line direction reads as sheen; "
                "it shifts as you move your head. Magnified here: the real lines are 0.45 mm. Free: no extra filament, no extra swap.", 58, 1.95, lead=1.3)
    s.append(p)
    return "\n".join(s)

INSETS = {"wear_inset": wear_inset, "bed_inset": bed_inset, "fold_inset": fold_inset, "toolpath_inset": toolpath_inset}

# ------------------------------------------------------------------ sheet A
def look_sheet(c):
    s = head(c["title"], c["kind"], c["idea"], "sheet A — the look", c.get("round", 2))
    has_inset = bool(c.get("inset"))
    i, box = img(os.path.join(OUT, c["main"]), 10, 41, 262, 148 if has_inset else 184)
    s.append(i)
    cap, _ = para(12, 229.5, c["main_caption"], 190, 2.6, fill=MUTE, style="italic")
    s.append(cap)
    x0 = 280
    i2, b2 = img(os.path.join(OUT, c["carry"]), x0, 41, 128, 66)
    s.append(i2)
    cap, yy = para(x0, b2[1] + b2[3] + 3.5, c["carry_caption"], 66, 2.5, fill=MUTE, style="italic")
    s.append(cap)
    yy += 1.5
    s.append(t(x0, yy + 2, "PRINCIPLES (each follows from the idea)", 3.1, ACC, weight="bold"))
    yy += 7
    for k, (p, because) in enumerate(c["principles"], 1):
        hd, yy = para(x0, yy, f"{k}. {p}", 60, 2.9, weight="bold")
        s.append(hd)
        bc, yy = para(x0 + 3.5, yy, "because " + because, 68, 2.45, fill="#4a443d")
        s.append(bc)
        yy += 1.3
    if has_inset:
        ins = c["inset"]
        bx, by, bw, bh = 12, 194, ins.get("w", 165), ins.get("h", 30)
        s.append(t(bx, by - 1.5, ins["caption"], 2.2, ACC, weight="bold"))
        if ins["kind"] == "img":
            s.append(rect(bx, by, bw, bh, "#ece7de", "#d8d0c2", 0.25))
            ii, _ = img(os.path.join(OUT, ins["src"]), bx + 1, by + 1, 70, bh - 2)
            s.append(ii)
            p, _ = para(bx + 76, by + 6, ins.get("note", ""), 46, 2.1)
            s.append(p)
        else:
            s.append(INSETS[ins["fn"]](bx, by, bw, bh))
    s.append(line(12, 238, 408, 238, "#d8d0c2", 0.3))
    cols = c["facts"]
    cw = 396 / len(cols)
    for k, (hdr, val) in enumerate(cols):
        xx = 12 + k * cw
        s.append(t(xx, 244.5, hdr, 2.6, ACC, weight="bold"))
        v, _ = para(xx, 249.5, val, int(cw / 1.36), 2.55)
        s.append(v)
    fp, _ = para(12, 281, c["foot"], 255, 2.3, fill=MUTE)
    s.append(fp)
    return write(s, "mock-A-look", os.path.join(ROOT, c["folder"]))

# ------------------------------------------------------------------ sheet B (real size, from the orthographic render)
def thumb_inset(x, y):
    """TYPE CASE: worst knob beside a section break, seen from the front (across x), at 1:1 and 2:1."""
    s = [rect(x, y, 64, 94, "#ece7de", "#d8d0c2", 0.25)]
    s.append(t(x + 2, y + 5, "WORST KNOB BY A SECTION BREAK", 2.3, ACC, weight="bold"))
    def group(sc, ox, oz):
        g = []
        P = lambda xx, zz: (ox + (xx - 4) * sc, oz - (zz - 21) * sc)
        a = P(4, 24); g.append(rect(a[0], a[1], 5 * sc, 3 * sc, "#26221f", INK, 0.15))
        a = P(12, 24); g.append(rect(a[0], a[1], 22 * sc, 3 * sc, "#26221f", INK, 0.15))
        a = P(9, 23); g.append(rect(a[0], a[1], 3 * sc, 2 * sc, "#d8ad74", INK, 0.15))
        kx = 12 + 7.0
        a = P(kx, 34.95); g.append(rect(a[0], a[1], 14.86 * sc, 10.45 * sc, "#b8432a", INK, 0.2, rx=0.6 * sc))
        c0 = P(kx - 5.2, 34.0)
        g.append(f'<ellipse cx="{c0[0]:.2f}" cy="{c0[1]:.2f}" rx="{5.6*sc:.2f}" ry="{8.0*sc:.2f}" transform="rotate(-35 {c0[0]:.2f} {c0[1]:.2f})" fill="#e7c9b0" fill-opacity="0.8" stroke="{INK}" stroke-width="0.2"/>')
        return "\n".join(g)
    s.append(t(x + 2, y + 9.5, "1:1", 2.0, MUTE))
    s.append(group(1.0, x + 8, y + 27))
    p, _ = para(x + 2, y + 33, "Knob edge 7 mm from the sunk rule. The rule's top is 1 mm BELOW the floor, so the thumb pad has nothing to hit. In round 1 a 7 mm wall stood 3.3 mm away.", 52, 1.9)
    s.append(p)
    s.append(t(x + 2, y + 47, "2:1", 2.0, MUTE))
    s.append(group(2.0, x + 2, y + 88))
    return "\n".join(s)

SPEAKER = (170, 128)

def real_sheet(c):
    s = head(c["title"], c["kind"], "Real size: print at 100 % on A3 (or tabloid at 'actual size'); the top view is 1:1, rendered straight down from the same model as sheet A.", "sheet B — top view, real size", c.get("round", 2))
    x0w, y0w, x1w, y1w = c["topbox"]
    ox, oy = 18, 46
    i, _ = img(os.path.join(OUT, c["top"]), ox, oy, x1w - x0w, y1w - y0w, exact=True)
    s.append(i)
    X = lambda x: ox + (x - x0w)
    Y = lambda y: oy + (y1w - y)
    s.append(t(18, 44, "TOP VIEW · 1:1 · front of the instrument at the bottom" + (" · lid left off so the panel shows; front dropped" if c["folder"] == "hymnal" else (" · open 180°" if c["folder"] == "fold" else "")), 3.0, INK, weight="bold"))
    fold = c["folder"] == "fold"
    depth = 2 * 106 if fold else D
    s.append(dim_h(X(0), X(W), Y(0) + 9 if not c["folder"] == "hymnal" else Y(-35) + 6, "298 mm"))
    s.append(dim_v(X(W) + 11, Y(depth), Y(0), f"{depth:.0f} mm" + (" open" if fold else "")))
    if fold:
        s.append(line(X(-6), Y(106), X(W + 4), Y(106), ACC, 0.25, dash="1.5 1"))
        s.append(t(X(-6), Y(106) - 1.2, "hinge axis (25.5 mm up); base below, lid above", 2.2, ACC))
    if c["folder"] in ("one-sheet", "fold", "hush"):
        top = depth if fold else D
        s.append(line(X(SPLIT_X), Y(top) - 3, X(SPLIT_X), Y(0) + 3, ACC, 0.3, dash="2 1.2"))
        s.append(t(X(SPLIT_X) + 1.2, Y(top) - 4, "print split x 121 (II|III)", 2.2, ACC))
    if not fold:
        SPEAKER = (150, 150) if c["folder"] == "under-glass" else (170, 128)
        s.append(circ(X(SPEAKER[0]), Y(SPEAKER[1]), 25, "none", BLUE, 0.3, dash="1.6 1.2"))
        s.append(t(X(0), (Y(-35) + 12 if c["folder"] == "hymnal" else Y(0) + 15), "dashed blue circle: 50 mm speaker (CDS-5076), on the bottom, firing down (eng)" + (" · moved to (150, 150): ≥ 30 mm from both windows' parts (eng E-L4)" if c["folder"] == "under-glass" else ""), 2.2, BLUE))
    xr = 345
    yy = 48
    s.append(t(xr, yy, "PARTS YOU SEE", 3.1, ACC, weight="bold"))
    yy += 5.5
    for k, v in c["parts"]:
        hd, yy = para(xr, yy, k, 34, 2.6, weight="bold")
        s.append(hd)
        pv, yy = para(xr, yy, v, 36, 2.4, fill="#4a443d")
        s.append(pv)
        yy += 1.2
    if c["folder"] == "type-case":
        s.append(thumb_inset(xr - 2, max(yy + 3, 188)))
    return write(s, "mock-B-real-size", os.path.join(ROOT, c["folder"]))

# ------------------------------------------------------------------ sheet C (key-edge section, fit check)
def section_svg(concept, ox, oy, sc):
    Y = lambda y: ox + y * sc
    Z = lambda z: oy - z * sc
    s = []
    def R(y0, z0, y1, z1, fill, stroke=INK, sw=0.2, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        return (f'<rect x="{Y(min(y0,y1)):.2f}" y="{Z(max(z0,z1)):.2f}" width="{abs(y1-y0)*sc:.2f}" height="{abs(z1-z0)*sc:.2f}" '
                f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
    def L(y, z, text, ty, tz, col=INK, size=2.1, anchor="start"):
        return line(Y(y), Z(z), Y(ty), Z(tz), col, 0.18) + t(Y(ty) + (0.8 if anchor == "start" else -0.8), Z(tz) + 0.8, text, size, col, anchor)
    def keystack(kz, y0=0.0, top="#fbf9f4", sharp="#2b2826", peg=False):
        st = kz - 11.4
        s.append(R(y0 + 4, st - 1.6, y0 + 54, st, "#2f6b4f"))
        s.append(R(y0 + 10.5, st, y0 + 25.5, st + 5, "#3a3a3a"))
        s.append(R(y0 + 16, st + 5, y0 + 20, st + 8.4, "#b14c3a"))
        s.append(R(y0 + 37.5, st, y0 + 52.5, st + 5, "#3a3a3a", MUTE, 0.15, "0.8 0.6"))
        s.append(R(y0 + 26.5, st, y0 + 30.5, st + 2, "#111"))
        if not peg:
            s.append(R(y0 + 5, kz - 3, y0 + 35, kz, top))
            s.append(R(y0 + 26.1, st + 7.6, y0 + 30.9, st + 9.2, "#8a8f96"))
            s.append(R(y0 + 37.5, kz - 1, y0 + 51.5, kz + 2, sharp, MUTE, 0.15, "0.8 0.6"))
        return st
    def knobs(pz, y0=0.0, col="#efe5cb", hero=True):
        kz = pz + 0.5
        if hero:
            s.append(R(y0 + 104 - 10.4, kz, y0 + 104 + 10.4, kz + 12.15, "#efe5cb"))
        for yk in ((127, 150) if hero else (104, 127, 150)):
            s.append(R(y0 + yk - 7.43, kz, y0 + yk + 7.43, kz + 10.45, col))
        s.append(R(y0 + 99, pz - 3 - 7, y0 + 109, pz - 3, "#555"))
        return kz
    def board(pz, y0=0.0, y1=None):
        s.append(R(y0 + 80, pz - 3 - 7 - 1.6, (y1 or y0 + D - 6), pz - 3 - 7, "#2f6b4f"))
    def speaker(y0=0.0, z0=3.0):
        s.append(R(y0 + 145, z0, y0 + 195, z0 + 7.6, "#8aa0b0", BLUE, 0.2))
        s.append(t(Y(y0 + 170), Z(z0 + 3.2), "50 mm speaker, 7.6 deep", 1.6, INK, "middle"))
    labels = []
    if concept == "type-case":
        s.append(R(0, 0, D, 3, "#e6c79c"))
        keystack(24)
        s.append(R(0, 3, 4, 21, "#e6c79c"))
        s.append(R(52, 21, 78, 24, "#e6c79c")); s.append(R(63, 23.4, 73, 24, "#ffffff"))
        s.append(R(78, 21, D - 4, 24, "#2a2522"))
        s.append(R(D - 4, 3, D, 36.7, "#e6c79c"))
        board(24); kz = knobs(24, col="#b8432a"); speaker()
        labels += [L(68, 24, "card in a flat pocket in the front rail", 60, 40), L(D - 2, 36.7, "rear rail 36.7 (sides + rear only)", 150, 44),
                   L(30, 24, "keys 24 = floors 24: one deck (R4)", 6, 46, ACC)]
    elif concept == "hymnal":
        s.append(R(0, 0, D, 3, "#a5643f"))
        keystack(24)
        s.append(R(-35, 0, 0, 3, "#a5643f")); s.append(R(0, 3, 3, 35, "#a5643f", MUTE, 0.15, "1 0.8"))
        s.append(R(52, 21, 78, 24, "#efe4c9"))
        s.append(R(78, 21, D - 3, 24, "#e6c79c"))
        s.append(R(D - 3, 3, D, 35, "#a5643f"))
        s.append(R(0, 35, D, 38, "#a5643f", MUTE, 0.2, "1.2 0.8")); s.append(R(4, 31, 9, 35, "#a5643f", MUTE, 0.2, "1.2 0.8"))
        board(24); kz = knobs(24, col="#f3f2ee"); speaker()
        labels += [L(-30, 3, "front dropped (open): palm rest", -36, -10), L(6, 33, "batten under the lid holds the front shut", 20, 50, ACC),
                   L(60, 38, "lid, closed: 38; CUTOFF in a 2 mm pocket", 80, 46), L(65, 24, "paper-edged key band, flat at 24", 52, 30)]
    elif concept == "hush":
        s.append(R(-3, 0, D + 3, 3, "#7f858c"))
        st = keystack(17.5, peg=True)
        s.append(R(4, 14.5, 34, 17.5, "#d9d6cf"))                          # hidden arm
        s.append(R(26.1, st + 7.6, 30.9, st + 9.2, "#8a8f96"))
        s.append(R(-3, 3, 0, 22.7, "#7f858c"))
        s.append(R(0, 20.2, D, 22.7, "#7f858c")); s.append(R(-3, 22.7, D + 3, 25.5, "#9a9894"))
        s.append(R(D, 3, D + 3, 22.7, "#7f858c"))
        s.append(R(12.5, 17.5, 19.5, 28, "#e2c290"))
        s.append(f'<path d="M {Y(9.65)} {Z(28)} L {Y(22.35)} {Z(28)} Q {Y(22.35)} {Z(32)} {Y(16)} {Z(32.2)} Q {Y(9.65)} {Z(32)} {Y(9.65)} {Z(28)} Z" fill="#e2c290" stroke="{INK}" stroke-width="0.2"/>')
        s.append(R(6.5, 25.5, 25.5, 26.3, "#74726f"))
        s.append(R(91, 25.5, 117, 26.7, "#d6d4ce"))
        board(22.7 + 1.3); kz = knobs(22.7 + 1.2, col="#ece2c6"); speaker()
        labels += [L(16, 26.0, "punched felt collar (wear part); the head lands on it at 2.5 of 2.8 mm", 30, 48, ACC),
                   L(20, 16, "hidden 1.75u arm; magnet 10.5 mm off the stem (eng E-L5)", 40, -12),
                   L(110, 26.5, "printed tag clamps the felt", 120, 50), L(D + 1, 24, "felt 22.7–25.5, deck = panel", 150, 32)]
    elif concept == "one-sheet":
        s.append(R(2, 0, D - 2, 2.5, "#c99b62"))
        keystack(24)
        s.append(R(0, 2.5, 2.4, 21, "#e8dcc2"))
        s.append(R(52, 21.5, D, 24, "#e8dcc2")); s.append(R(D - 2.4, 2.5, D, 21.5, "#e8dcc2"))
        board(24); kz = knobs(24, col="#ece2c6"); speaker(z0=2.5)
        labels += [L(60, 24, "shell deck 2.5 mm, printed face-down on smooth PEI: the first layer's lines are the finish", 52, 40),
                   L(121, 23.8, "legends: 0.6 mm cut-outs filled dark by one swap", 110, 47), L(30, 24, "keys 24 = deck 24", 6, 46, ACC)]
    elif concept == "under-glass":
        s.append(R(0, 0, D, 3, "#1b1b1c"))
        keystack(22, sharp="#141415")
        s.append(R(0, 0, 1.6, 12.7, "#b4b8bc")); s.append(R(0, 11.1, 12.7, 12.7, "#b4b8bc"))
        s.append(R(52, 21, D - 1.6, 24, "#cfe0dc")); s.append(R(52, 20.8, 80, 21, "#121314")); s.append(R(96, 20.8, D - 1.6, 21, "#121314"))
        s.append(R(D - 1.6, 0, D, 25.4, "#b4b8bc")); s.append(R(D - 12.7, 23.8, D, 25.4, "#b4b8bc")); s.append(R(D - 12.7, 0, D, 1.6, "#b4b8bc"))
        s.append(R(78, 12.4, D - 13, 14, "#16181a"))
        s.append(R(84, 14, 92, 18.6, "#1b1b1c")); s.append(R(82, 14, 85, 20, "#b8322b"))
        s.append(R(99, 14 , 109, 21, "#555"))
        for yk, h in ((104, 12.15), (127, 10.45), (150, 10.45)):
            s.append(R(yk - (10.4 if h > 11 else 7.43), 24.5, yk + (10.4 if h > 11 else 7.43), 24.5 + h, "#efe5cb" if h > 11 else "#f3f2ee"))
        speaker(); kz = 24.5
        labels += [L(88, 18, "window band y 80–96: parts ≤ 6.5 mm (glass underside 7 mm above the board)", 70, 48, ACC),
                   L(52, 22.5, "polished glass edge = the key edge", 30, 42), L(1, 12, "front rail 1/2 in, below the keys", -6, -10),
                   L(D - 1, 24, "rear rail 1 in = body 25.4", 150, 38), L(120, 20.9, "paint + back-filled legends on the underside", 125, -8)]
    elif concept == "fold":
        s.append(R(0, 0, 106, 2.5, "#1f2022"))
        keystack(17.5, y0=41, sharp="#62656b")
        s.append(R(0, 2.5, 41, 17.5, "#2e2f31")); s.append(R(4, 11.5, 37, 17.5, "#71492c")); s.append(R(93, 2.5, 106, 16.9, "#2e2f31"))
        s.append(R(106, 0, 212, 2, "#2e2f31")); s.append(R(209.6, 2, 212, 32, "#2e2f31"))
        s.append(R(109, 14, 208, 16.5, "#f4f3ef"))
        s.append(R(110, 4, 206, 5.6, "#2f6b4f"))
        s.append(R(112 + 50, 2, 112 + 100, 9.6, "#8aa0b0", BLUE, 0.2, "1 0.6"))
        for yk, h, w2, col in ((147, 12.15, 10.4, "#efe5cb"), (170, 13.5, 7.25, "#1c1c1e"), (193, 13.5, 7.25, "#1c1c1e")):
            s.append(R(yk - w2, 17, yk + w2, 17 + h, col))
        s.append(f'<circle cx="{Y(106):.2f}" cy="{Z(25.5):.2f}" r="{4.6*sc:.2f}" fill="none" stroke="{INK}" stroke-width="0.2" stroke-dasharray="0.8 0.6"/>')
        kz = 17
        labels += [L(106, 25.5, "hinge axis 25.5 (knuckles at the corners only)", 90, 46, ACC), L(60, 17.5, "keys 17.5", 50, 36),
                   L(130, 16.5, "white panel 16.5: level with the keys; front row 12 mm back", 120, 40), L(187, 6, "speaker on the lid's back in a board cutout (eng E-L6)", 150, -10),
                   L(20, 17.5, "walnut palm rest, flush; battery under", 4, 30), L(211, 32, "lid walls 32 (sides + far edge)", 190, 50)]
    for zz in (0, 10, 20, 30, 40):
        s.append(line(Y(-40 if concept == "hymnal" else -8), Z(zz), Y((212 if concept == "fold" else D) + 8), Z(zz), "#d8d2c8", 0.12, "0.6 0.8"))
        s.append(t(Y(-41 if concept == "hymnal" else -9), Z(zz) + 0.7, f"{zz}", 1.8, MUTE, "end"))
    s += labels
    return "\n".join(s)

def section_sheet(c):
    hd = ("The key edge in section (rule H3′, a fit check): through a white key and the CUTOFF column, front at the left. "
          + ("FOLD's own heights (systems rev 2): open flat, keys 17.5, panel 16.5, hinge axis 25.5, closed 51." if c["folder"] == "fold" else "Heights from eng (panel ≈ 24 with the 7.6 mm speaker)."))
    s = head(c["title"], c["kind"], hd, "sheet C — key-edge section (fit check)", c.get("round", 2))
    fold = c["folder"] == "fold"
    sc = 1.25 if fold else 1.6
    ox = {"hymnal": 80, "fold": 40}.get(c["folder"], 36)
    s.append(t(18, 46, f"SIDE SECTION · scale {sc} : 1 (grid every 10 mm of height)", 3.0, INK, weight="bold"))
    s.append(section_svg(c["folder"], ox, 150, sc))
    s.append(t(18, 205, "THE KEY EDGE", 3.3, ACC, weight="bold"))
    p, yy = para(18, 211.5, c["edge"], 150, 2.9)
    s.append(p)
    p2, yy = para(18, yy + 3, "Keys (eng velocity-and-keys-v2): 25 Kailh Choc V2 silent switches on strip C, a pressed-on short top per key with a K&J D31 magnet over a flat SS49E "
                  "(rest gap 5.6 mm, bottom 2.8 mm). R4 (owner: nothing raised between keys and controls): strip C rides on taller spacers so the key surface is within ≈ 3 mm of the panel. "
                  "Owner: no printed keys or knobs; printed enclosures are welcome.", 150, 2.5, fill="#4a443d")
    s.append(p2)
    return write(s, "mock-C-edge-section", os.path.join(ROOT, c["folder"]))

if __name__ == "__main__":
    import sys
    from content import CONCEPTS
    only = sys.argv[1:]
    for c in CONCEPTS:
        if only and c["folder"] not in only:
            continue
        print(look_sheet(c)); print(real_sheet(c)); print(section_sheet(c))
