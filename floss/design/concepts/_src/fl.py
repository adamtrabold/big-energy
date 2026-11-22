"""floss concept round 1 (visual): shared geometry, a tiny orthographic 3/4 renderer, and the 1:1 plan drawer.
Coordinates: origin front-left outer corner, x right, y away from the player, z up, mm (as Big Energy's r5/rb).
No OpenSCAD here, so the 3/4 views are slice-stacked orthographic drawings (matplotlib). Legends use Inter as a
stand-in for the family's Kalam (not installed in this environment)."""
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, PathPatch, Circle, FancyBboxPatch, Rectangle
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties
from matplotlib.transforms import Affine2D

FONT = FontProperties(family="Inter", weight="semibold")
FONT_B = FontProperties(family="Inter", weight="bold")
PAPER = "#f6f2ea"; INK = "#1d1b19"; GREY = "#8a8276"; CORAL = "#ef7f68"; CORAL_D = "#c9604c"
WAL = "#6b4429"; WAL_D = "#4a2e1b"; CREAM = "#f1ebdd"; CLOTH = "#e2d9c6"; BRASS = "#c9a24a"
EBONY = "#2d2522"; BONE = "#efe6d2"; FELT = "#9b968d"; FELT_D = "#827d75"; FELT_TAG = "#d8d3c9"; MAPLE = "#e9d09e"
PETG = "#e8dcc2"; GREEN = "#7bd389"

# ------------------------------------------------------------------ outlines
def rrect(x0, y0, w, d, r, n=10):
    r = min(r, w / 2, d / 2); pts = []
    for cx, cy, a0 in ((x0 + w - r, y0 + r, -90), (x0 + w - r, y0 + d - r, 0), (x0 + r, y0 + d - r, 90), (x0 + r, y0 + r, 180)):
        for k in range(n + 1):
            a = math.radians(a0 + 90 * k / n); pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts

def rrect4(x0, y0, w, d, rf, rb, n=12):
    """front corners rf, back corners rb (HUSH: r 4 front edge feel, R 44 rear)."""
    pts = []
    for cx, cy, a0, r in ((x0 + w - rf, y0 + rf, -90, rf), (x0 + w - rb, y0 + d - rb, 0, rb), (x0 + rb, y0 + d - rb, 90, rb), (x0 + rf, y0 + rf, 180, rf)):
        for k in range(n + 1):
            a = math.radians(a0 + 90 * k / n); pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts

def circle(cx, cy, r, n=44):
    return [(cx + r * math.cos(2 * math.pi * k / n), cy + r * math.sin(2 * math.pi * k / n)) for k in range(n)]

def inset(pts, d):
    """crude inset toward the centroid-free normal (outline is convex-ish rounded rect / circle)."""
    P = np.array(pts); n = len(P); out = []
    for i in range(n):
        a, b, c_ = P[i - 1], P[i], P[(i + 1) % n]
        t = c_ - a; nrm = np.array([t[1], -t[0]]); L = np.hypot(*nrm) or 1
        out.append(b - nrm / L * d)          # CCW outline: (t1,-t0) points outward, so minus = inward
    return [tuple(p) for p in out]

# ------------------------------------------------------------------ camera
class Cam:
    def __init__(self, az=32, el=34):
        a, e = math.radians(az), math.radians(el)
        self.d = np.array([math.sin(a) * math.cos(e), math.cos(a) * math.cos(e), -math.sin(e)])
        self.r = np.array([math.cos(a), -math.sin(a), 0.0])
        up = np.cross(self.r, self.d)
        if up[2] < 0: up = -up
        self.u = up / np.linalg.norm(up)
    def p(self, P):
        P = np.atleast_2d(P); return np.c_[P @ self.r, P @ self.u]
    def depth(self, P):
        return float(np.mean(np.atleast_2d(P) @ self.d))

def shade(col, f):
    c = np.array(matplotlib.colors.to_rgb(col)); return tuple(np.clip(c * f, 0, 1))

class Prim:
    """an outline (in its own s,t plane) extruded along n by h. o = origin, ex/ey/n = unit vectors (3D)."""
    def __init__(self, pts, h, side, top, o=(0, 0, 0), ex=(1, 0, 0), ey=(0, 1, 0), n=(0, 0, 1), layer=1,
                 bottom=None, round_top=0.0, step=0.7, decor=None, edge=None, dark=0.72):
        self.pts, self.h, self.side, self.top = pts, h, side, top
        self.o, self.ex, self.ey, self.n = map(np.array, (o, ex, ey, n))
        self.o = self.o.astype(float); self.layer = layer; self.bottom = bottom or side
        self.round_top, self.step, self.decor, self.edge, self.dark = round_top, step, decor, edge, dark
    def world(self, st, z):
        st = np.array(st); return self.o + np.outer(st[:, 0], self.ex) + np.outer(st[:, 1], self.ey) + z * self.n
    def key(self, cam):
        return (self.layer, -cam.depth(self.world(self.pts, self.h)))
    def draw(self, ax, cam):
        toward = float(self.n @ cam.d) < 0           # the +n end faces the camera
        nz = max(2, int(self.h / self.step))
        zs = np.linspace(0, self.h, nz + 1)
        order = zs if toward else zs[::-1]
        for z in order:
            pts = self.pts
            if self.round_top and z > self.h - self.round_top:
                k = (z - (self.h - self.round_top)) / self.round_top
                pts = inset(self.pts, self.round_top * (1 - math.sqrt(max(0, 1 - k * k))))
            f = self.dark + (1 - self.dark) * (z / self.h if toward else 1 - z / self.h)
            ax.add_patch(Polygon(cam.p(self.world(pts, z)), closed=True, fc=shade(self.side, f), ec="none", zorder=1))
        zf = self.h if toward else 0.0
        pts = inset(self.pts, self.round_top) if (self.round_top and toward) else self.pts
        ax.add_patch(Polygon(cam.p(self.world(pts, zf)), closed=True, fc=(self.top if toward else self.bottom),
                             ec=(self.edge or "none"), lw=0.4, zorder=1))
        if self.decor and toward:
            self.decor(ax, cam, self, zf)

def plane_affine(cam, prim, z):
    """affine map from the prim's (s,t) plane at height z to screen."""
    o = cam.p(prim.world([(0, 0)], z))[0]; a = cam.p(prim.world([(1, 0)], z))[0] - o; b = cam.p(prim.world([(0, 1)], z))[0] - o
    return Affine2D(np.array([[a[0], b[0], o[0]], [a[1], b[1], o[1]], [0, 0, 1]]))

def ptext(ax, cam, prim, z, s, x, y, size, col, ha="center", font=FONT, rot=0):
    tp = TextPath((0, 0), s, size=size, prop=font)
    bb = tp.get_extents(); dx = {"center": -bb.width / 2 - bb.x0, "left": -bb.x0, "right": -bb.x1}[ha]
    T = Affine2D().translate(dx, -bb.height / 2 - bb.y0).rotate_deg(rot).translate(x, y) + plane_affine(cam, prim, z) + ax.transData
    ax.add_patch(PathPatch(tp, fc=col, ec="none", transform=T, zorder=2))

def pline(ax, cam, prim, z, pts, col, lw=0.8):
    P = cam.p(prim.world(pts, z)); ax.plot(P[:, 0], P[:, 1], color=col, lw=lw, zorder=2, solid_capstyle="butt")

def ppoly(ax, cam, prim, z, pts, col):
    ax.add_patch(Polygon(cam.p(prim.world(pts, z)), closed=True, fc=col, ec="none", zorder=2))

def render(ax, cam, prims):
    for p in sorted(prims, key=lambda q: q.key(cam)):
        p.draw(ax, cam)
    ax.set_aspect("equal"); ax.axis("off"); ax.autoscale_view()

# ------------------------------------------------------------------ controls (shared vocabulary)
# kinds: knob, octave (stepped, 5 detents), sel4 (stepped 4), tab (mini rocker), hold (latching button + dot),
#        tap (cap in bezel; the bezel ring is the status light where noted), light, toggle (FREE/SYNC), peg (TIDE HOLD)
KN_D = 14.9; KN_H = 12.0          # KN1250-class (the family's lid knob size)

def knob_prims(x, y, z0, d=KN_D, h=KN_H, col=INK, ang=0.0, line="#ffffff", layer=2):
    def dec(ax, cam, pr, zf):
        r = d * 0.36; a = math.radians(90 - ang)
        pline(ax, cam, pr, zf, [(0, 0), (r * math.cos(a), r * math.sin(a))], line, 1.1)
    skirt = Prim(circle(0, 0, d / 2 + 0.6), 2.5, shade(col, 0.85), shade(col, 0.95), o=(x, y, z0), layer=layer)
    body = Prim(circle(0, 0, d / 2 - 0.6), h, col, shade(col, 1.08) if col != INK else "#2b2926", o=(x, y, z0 + 0.01), layer=layer, decor=dec, step=0.8)
    return [skirt, body]

def peg_prims(x, y, z0, d, col, collar=None, h=6.5, layer=2):
    ps = []
    if collar: ps.append(Prim(circle(0, 0, d / 2 + 2.0), 1.2, shade(collar, 0.9), collar, o=(x, y, z0), layer=layer))
    ps.append(Prim(circle(0, 0, d / 2), h, col, shade(col, 1.06), o=(x, y, z0 + (1.2 if collar else 0)), layer=layer, round_top=2.2, step=0.5))
    return ps

def tab_prims(x, y, z0, on, layer=2, cap=BONE):
    """mini rocker 15 (x) by 10 (y); the raised end is the end pressed down... drawn as: on = rear half raised + ink bar."""
    base = Prim(rrect(-7.5, -5, 15, 10, 1.5), 3.0, "#3a3633", "#3a3633", o=(x, y, z0), layer=layer)
    def dec(ax, cam, pr, zf):
        if on: ppoly(ax, cam, pr, zf, rrect(-5.5, 0.8, 11, 2.2, 0.8), CORAL_D if False else INK)
    hi = 5.2 if on else 3.6
    capp = Prim(rrect(-6.5, -4.2, 13, 8.4, 1.3), hi, shade(cap, 0.88), cap, o=(x, y, z0 + 3.0), layer=layer, decor=dec)
    return [base, capp]

def hold_prims(x, y, z0, layer=2, lit=True):
    def dec(ax, cam, pr, zf):
        ppoly(ax, cam, pr, zf, circle(0, 0, 1.6), CORAL if lit else "#bdb3a2")
    return [Prim(circle(0, 0, 6.0), 1.5, "#b9b0a0", "#d9d1c2", o=(x, y, z0), layer=layer),
            Prim(circle(0, 0, 4.6), 4.5, "#e7e0d2", "#efe9dd", o=(x, y, z0 + 1.5), layer=layer, decor=dec)]

def tap_prims(x, y, z0, ring=GREEN, layer=2):
    return [Prim(circle(0, 0, 7.4), 2.0, shade(ring, 0.8), ring, o=(x, y, z0), layer=layer),
            Prim(circle(0, 0, 6.0), 4.0, "#262422", "#2e2c2a", o=(x, y, z0 + 2.0), layer=layer, round_top=1.2)]

def toggle_prims(x, y, z0, layer=2):
    return [Prim(circle(0, 0, 3.0, 6), 2.0, "#9a9da1", "#b9bcbf", o=(x, y, z0), layer=layer),
            Prim(circle(0, 0, 1.1, 12), 8.0, "#b9bcbf", "#d0d2d4", o=(x, y, z0 + 2), layer=layer)]

def light_prims(x, y, z0, col=GREEN, layer=2):
    return [Prim(circle(0, 0, 1.8), 1.0, shade(col, 0.8), col, o=(x, y, z0), layer=layer)]

def control_prims(c, z0, style):
    k = c["k"]; x, y = c["x"], c["y"]
    if k in ("knob", "octave", "sel4"):
        d = c.get("d", KN_D + (1.5 if k == "octave" else 0)); col = c.get("col", style["knob"])
        line = style.get("knob_line", "#ffffff") if col not in (CORAL,) else "#ffffff"
        return knob_prims(x, y, z0, d=d, col=col, ang=c.get("ang", 0), line=line)
    if k == "tab": return tab_prims(x, y, z0, c.get("on", True), cap=style.get("tab", BONE))
    if k == "hold": return hold_prims(x, y, z0)
    if k == "tap": return tap_prims(x, y, z0, ring=c.get("ring", GREEN))
    if k == "toggle": return toggle_prims(x, y, z0)
    if k == "light": return light_prims(x, y, z0)
    if k == "peg": return peg_prims(x, y, z0, c.get("d", 16.0), style["key_w"], collar=style.get("collar"), h=7.0)
    return []

# ------------------------------------------------------------------ keys (25, C3..C5; middle C is the centre key)
SHARP_AFTER = [0, 1, 3, 4, 5, 7, 8, 10, 11, 12]
def key_xy(axis, yw, ys):
    x0 = axis - 135.0
    whites = [(x0 + 9 + 18 * i, yw) for i in range(15)]
    sharps = [(x0 + 18 * (i + 1), ys) for i in SHARP_AFTER]
    return whites, sharps, x0

# ------------------------------------------------------------------ 1:1 plan drawing
def tick_ring(ax, x, y, r, kind, col, n=None):
    R = r + 1.7
    if kind == "cont":
        angs = [-150 + 30 * i for i in range(11)]; major = {0, 10}
    elif kind == "centre":
        angs = [-150 + 30 * i for i in range(11)]; major = {0, 5, 10}
    elif kind == "step5":
        angs = [-60, -30, 0, 30, 60]; major = set(range(5))
    elif kind == "step4":
        angs = [-45, -15, 15, 45]; major = set(range(4))
    else:
        return
    for i, a in enumerate(angs):
        L = 1.0 if i in major else 0.55; t = math.radians(90 - a)
        ax.plot([x + (R - L) * math.cos(t), x + R * math.cos(t)], [y + (R - L) * math.sin(t), y + R * math.sin(t)], color=col, lw=0.35 * 72 / 25.4, solid_capstyle="butt")

def plan_text(ax, x, y, s, size_mm, col, ha="center", va="baseline", font=FONT, rot=0):
    """text sized in mm (cap-ish height ~ 0.72 * size) on a 1:1 axes (data units = mm)."""
    if not s.strip(): return
    tp = TextPath((0, 0), s, size=size_mm, prop=font); bb = tp.get_extents()
    dx = {"center": -bb.width / 2 - bb.x0, "left": -bb.x0, "right": -bb.x1}[ha]
    dy = {"baseline": 0, "center": -bb.height / 2 - bb.y0, "top": -bb.y1}[va]
    T = Affine2D().translate(dx, dy).rotate_deg(rot).translate(x, y) + ax.transData
    ax.add_patch(PathPatch(tp, fc=col, ec="none", transform=T))

def plan_controls(ax, ctrls, style, word_size=2.6):
    ink = style["ink"]
    for c in ctrls:
        k, x, y = c["k"], c["x"], c["y"]
        if k in ("knob", "octave", "sel4"):
            d = c.get("d", KN_D + (1.5 if k == "octave" else 0)); r = d / 2
            if style.get("ripple"):
                for rr in np.arange(r + 0.6, r + 2.4, 0.45): ax.add_patch(Circle((x, y), rr, fc="none", ec="#d7cab0", lw=0.25))
            if style.get("tag"): ax.add_patch(Circle((x, y), r + 2.6, fc=style["tag"], ec="none"))
            col = c.get("col", style["knob"])
            ax.add_patch(Circle((x, y), r + 0.6, fc=shade(col, 0.85), ec="none")); ax.add_patch(Circle((x, y), r - 0.6, fc=col, ec="none"))
            a = math.radians(90 - c.get("ang", 0)); ax.plot([x, x + r * 0.75 * math.cos(a)], [y, y + r * 0.75 * math.sin(a)], color="white", lw=1.2)
            kind = {"octave": "step5", "sel4": "step4"}.get(k, c.get("ticks", "cont"))
            if not style.get("tag"): tick_ring(ax, x, y, r + 0.6, kind, ink)
            else: tick_ring(ax, x, y, r + 0.9, kind, ink)
            top = y + r + (4.6 if not style.get("tag") else 5.0)
            if c.get("pos"): plan_text(ax, x, top, c["pos"], 1.5, ink); top += 2.6
            plan_text(ax, x, top, c["w"], word_size, ink, font=FONT_B)
        elif k == "tab":
            ax.add_patch(FancyBboxPatch((x - 7.5, y - 5), 15, 10, boxstyle="round,pad=0,rounding_size=1.5", fc="#3a3633", ec="none"))
            ax.add_patch(FancyBboxPatch((x - 6.5, y - 4.2), 13, 8.4, boxstyle="round,pad=0,rounding_size=1.3", fc=style.get("tab", BONE), ec="none"))
            if c.get("on", True): ax.add_patch(FancyBboxPatch((x - 5.5, y + 0.8), 11, 2.2, boxstyle="round,pad=0,rounding_size=0.8", fc=INK, ec="none"))
            if c.get("w"): plan_text(ax, x, y + 7.5, c["w"], word_size, ink, font=FONT_B)
        elif k == "hold":
            ax.add_patch(Circle((x, y), 6.0, fc="#d9d1c2", ec="none")); ax.add_patch(Circle((x, y), 4.6, fc="#efe9dd", ec="none"))
            ax.add_patch(Circle((x, y), 1.6, fc=CORAL, ec="none")); plan_text(ax, x, y + 9.0, c.get("w", "hold"), word_size, ink, font=FONT_B)
        elif k == "tap":
            ax.add_patch(Circle((x, y), 7.4, fc=c.get("ring", GREEN), ec="none")); ax.add_patch(Circle((x, y), 6.0, fc="#2b2927", ec="none"))
            plan_text(ax, x, y + 10.0, c.get("w", "tap"), word_size, ink, font=FONT_B)
        elif k == "toggle":
            ax.add_patch(Circle((x, y), 3.0, fc="#b9bcbf", ec="none")); ax.add_patch(Circle((x, y), 1.1, fc="#e0e2e4", ec="#8b8e91", lw=0.3))
            if c.get("pos"): plan_text(ax, x, y + 5.0, c["pos"], 1.5, ink)
            plan_text(ax, x, y + 7.6, c["w"], word_size, ink, font=FONT_B)
        elif k == "light":
            ax.add_patch(Circle((x, y), 1.8, fc=GREEN, ec="none"))
            if c.get("w"): plan_text(ax, x, y + 4.2, c["w"], 1.8, ink)
        elif k == "peg":
            if style.get("collar"): ax.add_patch(Circle((x, y), c.get("d", 16) / 2 + 2, fc=style["collar"], ec="none"))
            ax.add_patch(Circle((x, y), c.get("d", 16) / 2, fc=style["key_w"], ec=shade(style["key_w"], 0.85), lw=0.4))
            plan_text(ax, x, y + c.get("d", 16) / 2 + 5.0, c.get("w", "hold"), word_size, ink, font=FONT_B)
        elif k == "blank":
            ax.add_patch(Circle((x, y), KN_D / 2, fc="none", ec=style["ink"], lw=0.3, ls=(0, (2, 2))))

def a3_mm():
    """A3 landscape figure whose axes are 1 data unit = 1 mm when printed at 100%."""
    W, H = 420.0, 297.0
    fig = plt.figure(figsize=(W / 25.4, H / 25.4), dpi=300); fig.patch.set_facecolor(PAPER)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.set_aspect("equal"); ax.axis("off")
    return fig, ax

def scale_bar(ax, x, y, L=50):
    for i in range(5):
        ax.add_patch(Rectangle((x + i * L / 5, y), L / 5, 1.6, fc=(INK if i % 2 == 0 else PAPER), ec=INK, lw=0.3))
    plan_text(ax, x, y - 4, "0", 2.2, INK, ha="center"); plan_text(ax, x + L, y - 4, f"{L} mm", 2.2, INK, ha="center")
    plan_text(ax, x + L + 6, y, "print A3 at 100%: this bar is 50 mm", 2.2, GREY, ha="left")
