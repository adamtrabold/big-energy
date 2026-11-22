# floss CATHEDRAL-cues round: idea-level sheets for DROP, GNOMON, CASKET-B (visual, 2026-11-22).
# Rough flat-shaded 3/4 views from a tiny painter's renderer; sizes from systems' how-it-works files ([calc], nothing measured).
# Same scales on every sheet: end view 3:2, 3/4 views 1:2, bag inset 1:4. Sheet 14 x 20 in at 200 dpi.
# Run from this folder: python3 cathedral_sheets.py  -> ../c-drop/sheet.png, ../c-gnomon/sheet.png, ../c-casket/sheet.png
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Ellipse, PathPatch, FancyBboxPatch, Rectangle
from matplotlib.path import Path
plt.rcParams["font.family"] = "Inter"

WAL = (0.42, 0.27, 0.16); WALD = (0.30, 0.19, 0.11); CREAM = (0.945, 0.92, 0.865); BLACK = (0.11, 0.105, 0.10)
RED = (0.72, 0.20, 0.16); BRASS = (0.79, 0.64, 0.29); TPU = (0.16, 0.15, 0.14); KBC = (0.24, 0.24, 0.25)
KEYW = (0.93, 0.92, 0.90); BG = (0.965, 0.95, 0.92); GREY = (0.54, 0.51, 0.46); INK = (0.13, 0.12, 0.11)
FIG_W, FIG_H, DPI = 14.0, 20.0, 200
MM = 25.4
LBL = 24; SML = 17; TTL = 44

# ---------------- geometry helpers ----------------
def fillet(poly, r, n=8):
    """round every corner of a convex CCW polygon with radius r (clamped)."""
    out = []; m = len(poly)
    for i in range(m):
        p0, p1, p2 = poly[i-1], poly[i], poly[(i+1) % m]
        a = (p0[0]-p1[0], p0[1]-p1[1]); b = (p2[0]-p1[0], p2[1]-p1[1])
        la, lb = math.hypot(*a), math.hypot(*b)
        if la < 1e-6 or lb < 1e-6: continue
        ua = (a[0]/la, a[1]/la); ub = (b[0]/lb, b[1]/lb)
        cosang = max(-1, min(1, ua[0]*ub[0]+ua[1]*ub[1])); ang = math.acos(cosang)
        if ang > math.radians(175): out.append(p1); continue
        rr = min(r, 0.45*min(la, lb)*math.tan(ang/2))
        d = rr/math.tan(ang/2)
        t1 = (p1[0]+ua[0]*d, p1[1]+ua[1]*d); t2 = (p1[0]+ub[0]*d, p1[1]+ub[1]*d)
        bis = (ua[0]+ub[0], ua[1]+ub[1]); lbis = math.hypot(*bis); bis = (bis[0]/lbis, bis[1]/lbis)
        cdist = rr/math.sin(ang/2); c = (p1[0]+bis[0]*cdist, p1[1]+bis[1]*cdist)
        a1 = math.atan2(t1[1]-c[1], t1[0]-c[0]); a2 = math.atan2(t2[1]-c[1], t2[0]-c[0])
        da = (a2 - a1 + math.pi) % (2*math.pi) - math.pi
        for k in range(n+1):
            aa = a1 + da*k/n; out.append((c[0]+rr*math.cos(aa), c[1]+rr*math.sin(aa)))
    return out

def offset_convex(poly, d):
    """inward offset of a convex CCW polygon (simple: edge lines moved in, consecutive lines intersected)."""
    m = len(poly); lines = []
    for i in range(m):
        p, q = poly[i], poly[(i+1) % m]
        dx, dy = q[0]-p[0], q[1]-p[1]; L = math.hypot(dx, dy)
        if L < 1e-6: continue
        nx, ny = -dy/L, dx/L
        lines.append(((p[0]+nx*d, p[1]+ny*d), (dx/L, dy/L)))
    out = []
    for i in range(len(lines)):
        (p1, d1), (p2, d2) = lines[i-1], lines[i]
        den = d1[0]*d2[1]-d1[1]*d2[0]
        if abs(den) < 1e-6: out.append(p2); continue
        t = ((p2[0]-p1[0])*d2[1]-(p2[1]-p1[1])*d2[0])/den
        out.append((p1[0]+d1[0]*t, p1[1]+d1[1]*t))
    return out

def area(poly):
    return 0.5*sum(poly[i-1][0]*poly[i][1]-poly[i][0]*poly[i-1][1] for i in range(len(poly)))
def ccw(poly): return poly if area(poly) > 0 else poly[::-1]

# ---------------- the three profiles (end face, y forward->back, z up) ----------------
# DROP: lip 26.5, pipe R 31 at the back, plate tangent, theta ~37 deg [systems c-drop]
DR_R, DR_C = 31.0, (57.0, 31.0); DR_LIP = 26.5
def drop_theta():
    # solve 57 sin t - (31-26.5) cos t = 31
    lo, hi = 0.3, 1.2
    for _ in range(60):
        t = (lo+hi)/2
        f = DR_C[0]*math.sin(t) - (DR_C[1]-DR_LIP)*math.cos(t) - DR_R
        lo, hi = (t, hi) if f < 0 else (lo, t)
    return (lo+hi)/2
DR_T = drop_theta()
def drop_profile():
    tang = math.pi/2 + DR_T
    pts = [(0, 0)]
    for k in range(0, 61):
        a = -math.pi/2 + (tang + math.pi/2)*k/60
        pts.append((DR_C[0]+DR_R*math.cos(a), DR_C[1]+DR_R*math.sin(a)))
    pts.append((0, DR_LIP))
    pts = ccw(pts)
    # soften the two front corners only (the pipe is already round)
    return fillet_some(pts, {0: 3.5, len(pts)-1: 5.0})
def fillet_some(pts, radii):
    out = []
    m = len(pts)
    for i, p in enumerate(pts):
        if i in radii:
            tri = [pts[i-1], p, pts[(i+1) % m]]
            f = fillet(tri, radii[i])
            # fillet returns rounded corners of the triangle; keep only those near p
            near = [q for q in f if math.hypot(q[0]-p[0], q[1]-p[1]) < radii[i]*2.2]
            out += near
        else:
            out.append(p)
    return out

# GNOMON: slab T 35, D 105, sin(theta)=T/D -> 19.47 deg; cheeks below [systems c-gnomon]
GN_T, GN_D = 35.0, 105.0; GN_TH = math.atan(GN_T/GN_D)   # rev 2: tan(theta) = T/D, rear face = 2T, square to the plate
def gn_pts():
    c, s = math.cos(GN_TH), math.sin(GN_TH)
    fb = (0.0, 0.0); bb = (GN_D*c, GN_D*s); nt = (-s*GN_T, c*GN_T)
    ft = (fb[0]+nt[0], fb[1]+nt[1]); bt = (bb[0]+nt[0], bb[1]+nt[1])
    return fb, bb, bt, ft
def gnomon_profile():
    fb, bb, bt, ft = gn_pts()
    return fillet(ccw([fb, (bb[0], 0.0), bb, bt, ft]), 6)
def gnomon_slab():
    fb, bb, bt, ft = gn_pts()
    return fillet(ccw([fb, bb, bt, ft]), 6)
def gnomon_cheek():
    fb, bb, bt, ft = gn_pts()
    return ccw([(fb[0]+0.5, 0.0), (bb[0], 0.0), (bb[0], bb[1]+0.5)])

# CASKET-B: module 280 x 107 x 35; lid 15 deep; angled 11 deg on the lid's front skirt in the groove [systems c-casket]
CA_D, CA_T, CA_LID = 107.0, 35.0, 15.0
CA_GROOVE = 86.0          # contact distance along the base (groove y 80-92)
CA_TH = math.asin(CA_LID/CA_GROOVE)
CA_LIDD = 109.0
def casket_module_local():
    return fillet(ccw([(0, 0), (CA_D, 0), (CA_D, CA_T), (0, CA_T)]), 6)
def tilt(pts, th, about=(0, 0)):
    c, s = math.cos(th), math.sin(th)
    return [(about[0]+(y-about[0])*c-(z-about[1])*s, about[1]+(y-about[0])*s+(z-about[1])*c) for y, z in pts]
def casket_angled_module():
    return tilt(casket_module_local(), CA_TH)
def casket_lid_angled():
    y0 = CA_GROOVE*math.cos(CA_TH) - 3          # front skirt wall sits in the groove
    return fillet(ccw([(y0, 0), (y0+CA_LIDD, 0), (y0+CA_LIDD, CA_LID), (y0, CA_LID)]), 3), y0

# ---------------- tiny renderer ----------------
class Cam:
    def __init__(self, az=28, el=24):
        a, e = math.radians(az), math.radians(el)
        sa, ca, se, ce = math.sin(a), math.cos(a), math.sin(e), math.cos(e)
        self.c = (-sa*ce, -ca*ce, se)
        self.r = (ca, -sa, 0.0)
        self.u = (se*sa, se*ca, ce)
    def p(self, P):
        return (P[0]*self.r[0]+P[1]*self.r[1]+P[2]*self.r[2], P[0]*self.u[0]+P[1]*self.u[1]+P[2]*self.u[2])
    def depth(self, P): return P[0]*self.c[0]+P[1]*self.c[1]+P[2]*self.c[2]
    def faces(self, n): return n[0]*self.c[0]+n[1]*self.c[1]+n[2]*self.c[2] > 1e-6

LIGHT = (-0.45, -0.55, 0.70)
LN = math.sqrt(sum(v*v for v in LIGHT)); LIGHT = tuple(v/LN for v in LIGHT)
def shade(col, n, amb=0.62):
    k = amb + (1-amb)*max(0.0, sum(a*b for a, b in zip(n, LIGHT)))
    return tuple(min(1, c*k) for c in col)

class Scene:
    def __init__(self, cam): self.cam = cam; self.layers = []
    def layer(self): self.layers.append([]); return self.layers[-1]
    def draw(self, ax):
        for L in self.layers:
            items = [it for it in L if it[0] == "line" or self.cam.faces(it[2])]
            items.sort(key=lambda it: it[4])
            for it in items:
                if it[0] == "face":
                    _, pts, n, col, d, ec, extra = it
                    xy = [self.cam.p(P) for P in pts]
                    patch = Polygon(xy, closed=True, fc=shade(col, n), ec=ec or shade(col, n), lw=0.5, joinstyle="round")
                    ax.add_patch(patch)
                    if extra: extra(ax, self.cam, patch)
                else:
                    _, pts, col, lw, d = it
                    xy = [self.cam.p(P) for P in pts]
                    ax.plot([q[0] for q in xy], [q[1] for q in xy], color=col, lw=lw, solid_capstyle="round")

def add_face(L, cam, pts, n, col, ec=None, extra=None, bias=0.0):
    d = sum(cam.depth(P) for P in pts)/len(pts) + bias
    L.append(("face", pts, n, col, d, ec, extra))
def add_line(L, cam, pts, col, lw):
    L.append(("line", pts, col, lw, sum(cam.depth(P) for P in pts)/len(pts), ))

def extrude(L, cam, prof, x0, x1, col, cap_extra=None, ec=None):
    prof = ccw(prof)
    m = len(prof)
    for i in range(m):
        (y1, z1), (y2, z2) = prof[i], prof[(i+1) % m]
        dy, dz = y2-y1, z2-z1; Ln = math.hypot(dy, dz)
        if Ln < 1e-9: continue
        n = (0.0, dz/Ln, -dy/Ln)
        add_face(L, cam, [(x0, y1, z1), (x1, y1, z1), (x1, y2, z2), (x0, y2, z2)], n, col, ec=ec)
    add_face(L, cam, [(x0, y, z) for y, z in prof[::-1]], (-1.0, 0.0, 0.0), col, extra=cap_extra, ec=WALD if col == WAL else ec)
    add_face(L, cam, [(x1, y, z) for y, z in prof], (1.0, 0.0, 0.0), col, ec=ec)

def box(L, cam, x0, x1, y0, y1, z0, z1, col):
    extrude(L, cam, [(y0, z0), (y1, z0), (y1, z1), (y0, z1)], x0, x1, col)

def plate_frame(origin_yz, th, W):
    """origin (y,z) of the plate's front edge, slope angle th. Returns function (x, t, h) -> 3D, and the normal."""
    c, s = math.cos(th), math.sin(th)
    n = (0.0, -s, c)
    def P(x, t, h=0.0):
        return (x, origin_yz[0] + t*c + h*n[1], origin_yz[1] + t*s + h*n[2])
    return P, n

def field(L, cam, P, n, x0, x1, t0, t1, col=CREAM, lift=0.25):
    add_face(L, cam, [P(x0, t0, lift), P(x1, t0, lift), P(x1, t1, lift), P(x0, t1, lift)], n, col, ec=(0.80, 0.76, 0.69))

def knob(L, cam, P, n, x, t, col=BLACK, d=10.0, h=8.0, N=22):
    """cylinder standing on the plate: side quads + top disc (own layer, depth-sorted)."""
    ex = (1.0, 0.0, 0.0); et = (0.0, n[2], -n[1])    # in-plate direction up the slope
    base = P(x, t, 0.0)
    def pt(a, hh):
        r = d/2
        return (base[0] + r*math.cos(a)*ex[0] + r*math.sin(a)*et[0] + hh*n[0],
                base[1] + r*math.cos(a)*ex[1] + r*math.sin(a)*et[1] + hh*n[1],
                base[2] + r*math.cos(a)*ex[2] + r*math.sin(a)*et[2] + hh*n[2])
    for k in range(N):
        a1, a2 = 2*math.pi*k/N, 2*math.pi*(k+1)/N
        am = (a1+a2)/2
        nn = tuple(math.cos(am)*ex[i] + math.sin(am)*et[i] for i in range(3))
        add_face(L, cam, [pt(a1, 0), pt(a2, 0), pt(a2, h), pt(a1, h)], nn, col, ec=None)
    add_face(L, cam, [pt(2*math.pi*k/N, h) for k in range(N)], n, tuple(min(1, c*1.25+0.04) for c in col), bias=40)

def lancet_window(L, cam, P, n, xc, tc, R=23.0, pitch=3.0, col=(0.07, 0.065, 0.06), lw=2.0):
    k = 0
    for k in range(-7, 8):
        dx = k*pitch; h = math.sqrt(max(0, R*R - dx*dx))
        add_line(L, cam, [P(xc+dx, tc-h, 0.5), P(xc+dx, tc+h, 0.5)], col, lw)

# ---------------- keyboard ----------------
KB_W, KB_D, KB_H = 330.0, 90.0, 16.0
def keyboard(scene, cam, x0, y0, z0=0.0, keys_up=True):
    L = scene.layer()
    box(L, cam, x0, x0+KB_W, y0, y0+KB_D, z0, z0+KB_H, KBC)
    if not keys_up: return
    L2 = scene.layer()
    nat = 15; kx0 = x0+22; kw = (KB_W-44)/nat
    for i in range(nat):
        xa = kx0+i*kw+0.6; xb = kx0+(i+1)*kw-0.6
        add_face(L2, cam, [(xa, y0+6, z0+KB_H+0.3), (xb, y0+6, z0+KB_H+0.3), (xb, y0+60, z0+KB_H+0.3), (xa, y0+60, z0+KB_H+0.3)], (0, 0, 1), KEYW, ec=(0.75, 0.74, 0.72))
    L3 = scene.layer()
    blk = [0, 1, 3, 4, 5, 7, 8, 10, 11, 12]
    for i in blk:
        xc = kx0+(i+1)*kw
        add_face(L3, cam, [(xc-kw*0.3, y0+30, z0+KB_H+0.6), (xc+kw*0.3, y0+30, z0+KB_H+0.6), (xc+kw*0.3, y0+60, z0+KB_H+0.6), (xc-kw*0.3, y0+60, z0+KB_H+0.6)], (0, 0, 1), (0.10, 0.10, 0.10))

# ---------------- end-face decoration (growth rings round the port mouth, bead, brass ring) ----------------
def end_face_2d(ax, prof, port, ring_step=6.0, bead=4.0, brass_ring=True, strips=()):
    poly = Polygon(prof, closed=True, fc=WAL, ec=WALD, lw=2.2, joinstyle="round")
    ax.add_patch(poly)
    rmax = max(math.hypot(y-port[0], z-port[1]) for y, z in prof)
    r = 11.0
    while r < rmax:
        ax.add_patch(Circle(port, r, fc="none", ec=WALD, lw=0.9, clip_path=poly))
        r += ring_step*(1 + 0.035*(r/10))
    inner = offset_convex(prof, bead)
    ax.add_patch(Polygon(inner, closed=True, fc="none", ec=(0.55, 0.38, 0.24), lw=1.4))
    if brass_ring: ax.add_patch(Circle(port, 9.5, fc=BRASS, ec=(0.55, 0.43, 0.17), lw=0.8))
    ax.add_patch(Circle(port, 7.0, fc=(0.10, 0.07, 0.05), ec="none"))
    for (y0, y1) in strips:
        ax.add_patch(Rectangle((y0, -1.6), y1-y0, 1.6, fc=TPU, ec="none"))

def rings_on_cap(port_yz, x, prof, step=6.0):
    def extra(ax, cam, patch):
        rmax = max(math.hypot(y-port_yz[0], z-port_yz[1]) for y, z in prof)
        r = 11.0
        while r < rmax:
            pts = [cam.p((x, port_yz[0]+r*math.cos(a), port_yz[1]+r*math.sin(a))) for a in [2*math.pi*k/90 for k in range(91)]]
            ax.plot([q[0] for q in pts], [q[1] for q in pts], color=WALD, lw=0.6, clip_path=patch)
            r += step*(1 + 0.035*(r/10))
        inner = offset_convex(ccw(prof), 3.0)
        pts = [cam.p((x, y, z)) for y, z in inner] + [cam.p((x, inner[0][0], inner[0][1]))]
        ax.plot([q[0] for q in pts], [q[1] for q in pts], color=(0.55, 0.38, 0.24), lw=0.8)
        for rr, fc in ((9.5, BRASS), (7.0, (0.10, 0.07, 0.05))):
            pts = [cam.p((x, port_yz[0]+rr*math.cos(a), port_yz[1]+rr*math.sin(a))) for a in [2*math.pi*k/40 for k in range(40)]]
            ax.add_patch(Polygon(pts, closed=True, fc=fc, ec="none"))
    return extra

# ---------------- sheet layout ----------------
def new_sheet(title, sub, dims, scales="same scales on all three sheets"):
    fig = plt.figure(figsize=(FIG_W, FIG_H), dpi=DPI); fig.patch.set_facecolor(BG)
    fig.text(0.04, 0.968, title, fontsize=TTL, weight="bold", color=INK, va="top")
    fig.text(0.04, 0.938, dims, fontsize=LBL+4, color=INK, va="top")
    import textwrap
    fig.text(0.04, 0.905, "\n".join(textwrap.wrap(sub, 100)), fontsize=SML, color="#555", va="top", linespacing=1.15)
    fig.text(0.04, 0.010, "floss · CATHEDRAL-cues round · idea level, not a render · sizes [calc] from systems' how-it-works, nothing measured · " + scales + "\n"
             "printed body (walnut-brown), printed cream plate, bought knobs (black, one red), brass = printed metal (only if cast counts), printed TPU grip strips",
             fontsize=11, color=GREY)
    return fig

def axes_mm(fig, box_mm, scale, center):
    """box_mm = (left, bottom, w, h) in mm on the sheet; scale = paper mm per model mm; center = model (x, y) at the box centre."""
    l, b, w, h = box_mm
    W, H = FIG_W*MM, FIG_H*MM
    ax = fig.add_axes([l/W, b/H, w/W, h/H]); ax.set_aspect("equal"); ax.axis("off")
    dw, dh = w/scale, h/scale
    ax.set_xlim(center[0]-dw/2, center[0]+dw/2); ax.set_ylim(center[1]-dh/2, center[1]+dh/2)
    return ax

def heading(fig, box_mm, text, size=LBL+2):
    W, H = FIG_W*MM, FIG_H*MM
    fig.text(box_mm[0]/W, (box_mm[1]+box_mm[3])/H, text, fontsize=size, weight="bold", color=INK, va="bottom")

def scale_bar(ax, x, y, mm, label, size=SML):
    ax.plot([x, x+mm], [y, y], color=INK, lw=2.5, solid_capstyle="butt")
    for xx in (x, x+mm): ax.plot([xx, xx], [y-1.5*mm/50, y+1.5*mm/50], color=INK, lw=1.5)
    ax.text(x+mm/2, y-4*mm/50, label, ha="center", va="top", fontsize=size, color=INK)

def ground(ax, x0, x1, y=0.0, step=8):
    ax.plot([x0, x1], [y, y], color=GREY, lw=1.2)

def leader(ax, xy, txt, xytext, size=SML, ha="left"):
    ax.annotate(txt, xy, xytext, fontsize=size, color=INK, ha=ha, va="center",
                arrowprops=dict(arrowstyle="-", color=GREY, lw=1.0, shrinkA=0, shrinkB=2))

def bag_inset(fig, box_mm, items, label):
    """loose in the bag, end section at 1:4: items = list of (profile, (dy, dz))."""
    ax = axes_mm(fig, box_mm, 0.25, (150, 55))
    ax.add_patch(FancyBboxPatch((0, 0), 300, 120, boxstyle="round,pad=0,rounding_size=30", fc=(0.88, 0.86, 0.82), ec=GREY, lw=1.5))
    for prof, (dy, dz), col in items:
        ax.add_patch(Polygon([(y+dy, z+dz) for y, z in prof], closed=True, fc=col, ec=WALD if col == WAL else (0.1, 0.1, 0.1), lw=1))
    ax.text(150, -16, label, ha="center", va="top", fontsize=SML, color=INK)
    heading(fig, (box_mm[0], box_mm[1]+box_mm[3]-12, box_mm[2], 10), "loose in the bag (1:4)", size=SML+3)
    return ax

KB_SECTION = [(0, 0), (16, 0), (16, 90), (0, 90)]   # keyboard on its edge in a bag

def save(fig, path):
    fig.savefig(path, facecolor=BG, dpi=DPI); plt.close(fig)

# ======================= DROP =======================
def sheet_drop(path):
    W = 260.0
    prof = drop_profile()
    fig = new_sheet("DROP · the angle is a pipe",
                    "One solid tool you pick up by its handle. The pipe at the back is the speaker box, the port, the batteries and the grip; "
                    "the plate leans on it at the angle the parts give.", f"260 × 88 × 62 mm · ≈ {math.degrees(DR_T):.0f}° · one pose")
    # 1. end view, big
    box_mm = (14, 280, 328, 146)
    heading(fig, box_mm, "1  End view (3:2): the silhouette")
    ax = axes_mm(fig, box_mm, 1.5, (60, 30))
    end_face_2d(ax, prof, DR_C, strips=((3, 14), (66, 76)))
    ground(ax, -40, 150)
    leader(ax, (DR_C[0]+3, DR_C[1]+6), "port mouth at the\nheart of the end grain", (100, 52))
    leader(ax, (DR_C[0]+DR_R*math.cos(1.95), DR_C[1]+DR_R*math.sin(1.95)), "one rim line wraps\nplate and pipe", (100, 82))
    leader(ax, (14, DR_LIP+8), "plate (2 rows)", (-48, 66), ha="left")
    leader(ax, (6, 1), "TPU grip strips", (-48, 10))
    scale_bar(ax, -45, -7, 50, "50 mm (at 3:2)")
    # 2. 3/4 playing, keyboard in front
    P, n = plate_frame((0, DR_LIP), DR_T, W)
    tlen = (DR_C[0]-DR_R*math.sin(DR_T))/math.cos(DR_T)
    xs1 = [20 + i*(W-40)/9 for i in range(10)]; xs2 = [20 + (i+0.5)*(W-40)/9 for i in range(9)]
    def drop_body(sc, cam):
        L = sc.layer()
        extrude(L, cam, prof, 0, W, WAL, cap_extra=rings_on_cap(DR_C, 0, prof))
        L2 = sc.layer()
        field(L2, cam, P, n, 8, W-8, 4.0, tlen)
        tang = math.pi/2 + DR_T
        arc = [tang - k*(tang-math.radians(62))/14 for k in range(15)]
        for a1, a2 in zip(arc[:-1], arc[1:]):
            am = (a1+a2)/2; nn = (0.0, math.cos(am), math.sin(am)); R2 = DR_R+0.25
            q = lambda x, a: (x, DR_C[0]+R2*math.cos(a), DR_C[1]+R2*math.sin(a))
            add_face(L2, cam, [q(8, a1), q(W-8, a1), q(W-8, a2), q(8, a2)], nn, CREAM, ec=CREAM)
        L3 = sc.layer()
        for xc in (W/2-31, W/2+31):
            for k in range(-7, 8):
                dx = k*3.0; h = math.sqrt(max(0, 22**2-dx*dx))/DR_R
                am = math.radians(100)
                pts = [(xc+dx, DR_C[0]+(DR_R+0.5)*math.cos(a), DR_C[1]+(DR_R+0.5)*math.sin(a)) for a in [am-h+2*h*j/10 for j in range(11)]]
                add_line(L3, cam, pts, (0.07, 0.065, 0.06), 1.5)
        L4 = sc.layer()
        for x in xs1: knob(L4, cam, P, n, x, 13)
        for i, x in enumerate(xs2): knob(L4, cam, P, n, x, 33, col=RED if i == 4 else BLACK)
    cam = Cam(28, 26); sc = Scene(cam)
    drop_body(sc, cam)
    keyboard(sc, cam, W/2-KB_W/2, -KB_D-55)
    box_mm = (14, 120, 328, 150)
    heading(fig, box_mm, "2  Playing (1:2), the keyboard in front")
    ax = axes_mm(fig, box_mm, 0.5, (cam.p((W/2, -40, 20))[0], cam.p((W/2, -40, 20))[1]+8))
    sc.draw(ax)
    # 3. packed with SHOE
    cam2 = Cam(28, 26); sc2 = Scene(cam2)
    keyboard(sc2, cam2, W/2-KB_W/2, -1, z0=-KB_H, keys_up=False)
    drop_body(sc2, cam2)
    box_mm = (14, 22, 200, 88)
    heading(fig, box_mm, "3  Packed (1:2): SHOE, keys out")
    ax = axes_mm(fig, box_mm, 0.5, cam2.p((W/2, 30, 10)))
    sc2.draw(ax)
    bag_inset(fig, (226, 22, 116, 88), [(prof, (30, 20), WAL), (KB_SECTION, (200, 15), KBC)], "or loose: no carry needed")
    save(fig, path)

# ======================= GNOMON =======================
def fillet_radii(poly, radii, n=10):
    out = []; m = len(poly)
    for i in range(m):
        p0, p1, p2 = poly[i-1], poly[i], poly[(i+1) % m]
        a = (p0[0]-p1[0], p0[1]-p1[1]); b = (p2[0]-p1[0], p2[1]-p1[1])
        la, lb = math.hypot(*a), math.hypot(*b)
        ua = (a[0]/la, a[1]/la); ub = (b[0]/lb, b[1]/lb)
        ang = math.acos(max(-1, min(1, ua[0]*ub[0]+ua[1]*ub[1])))
        rr = min(radii[i], 0.48*min(la, lb)*math.tan(ang/2))
        if rr <= 0.01: out.append(p1); continue
        d = rr/math.tan(ang/2)
        t1 = (p1[0]+ua[0]*d, p1[1]+ua[1]*d); t2 = (p1[0]+ub[0]*d, p1[1]+ub[1]*d)
        bis = (ua[0]+ub[0], ua[1]+ub[1]); lbis = math.hypot(*bis); bis = (bis[0]/lbis, bis[1]/lbis)
        c = (p1[0]+bis[0]*rr/math.sin(ang/2), p1[1]+bis[1]*rr/math.sin(ang/2))
        a1 = math.atan2(t1[1]-c[1], t1[0]-c[0]); a2 = math.atan2(t2[1]-c[1], t2[0]-c[0])
        da = (a2 - a1 + math.pi) % (2*math.pi) - math.pi
        for k in range(n+1):
            aa = a1 + da*k/n; out.append((c[0]+rr*math.cos(aa), c[1]+rr*math.sin(aa)))
    return out

def sheet_gnomon(path):
    """GNOMON pass 2: director fixes 1-6. Hairline one slab-thickness below the plate; rear 3/4 with the open
    underside; port as grooves only; lip rounded into the plate; packed on SHOE and loose at the same size;
    rear face square to the plate (a true gnomon), so it also stands upright with the plate vertical."""
    global FIG_H, LIGHT
    old_h = FIG_H; FIG_H = 25.0
    W = 280.0; CHK = 10.0
    fb, bb, bt, ft = gn_pts()
    cth, sth = math.cos(GN_TH), math.sin(GN_TH)
    # fix 6: the rear face runs square to the plate from bt down to the table
    Rq = (bt[0] + 2*GN_T*sth, bt[1] - 2*GN_T*cth)     # rear face 2T, square to the plate, lands on the table
    LIP_R = 16.0
    prof0 = fillet_radii([fb, Rq, bt, ft], [3, 4, 6, LIP_R])
    slab0 = fillet_radii([fb, bb, bt, ft], [3, 0.01, 6, LIP_R])
    port0 = (fb[0] + 80*cth - 17.5*sth, fb[1] + 80*sth + 17.5*cth)
    hair0 = [(fb[0]+3.5*cth, fb[1]+3.5*sth), (bb[0]-0.3*cth, bb[1]-0.3*sth)]
    # jacks on the right end face, in the cheek below the hairline (y, z, kind)
    jk0 = []
    for i, kind in enumerate(["usb", "sw", "pot", "sw", "j", "j", "j", "j"]):
        t = 34 + i*8.5
        jk0.append((fb[0] + t*cth - 17.5*sth, fb[1] + t*sth + 17.5*cth, kind))
    jk0 = [(y, z, k) for (y, z, k) in jk0]

    ang_up = -(math.pi - math.atan2(bt[1]-Rq[1], Rq[0]-bt[0]))     # puts the rear face on the table
    def tf_up(p):
        y, z = p[0]-Rq[0], p[1]-Rq[1]
        c, s_ = math.cos(ang_up), math.sin(ang_up)
        return (y*c - z*s_, y*s_ + z*c)
    ident = lambda p: (p[0], p[1])

    def geo(tf):
        prof = ccw([tf(p) for p in prof0]); slab = ccw([tf(p) for p in slab0])
        zmin = min(z for y, z in prof)
        sh = lambda p: (p[0], p[1]-zmin)
        prof = [sh(p) for p in prof]; slab = [sh(p) for p in slab]
        port = sh(tf(port0)); hair = [sh(tf(p)) for p in hair0]
        ftt, btt = sh(tf(ft)), sh(tf(bt))
        th = math.atan2(btt[1]-ftt[1], btt[0]-ftt[0])
        jk = [(sh(tf((y, z))), k) for y, z, k in jk0]
        return prof, slab, port, hair, ftt, th, jk

    def rings(ax, cam, x, prof, port, patch, step=6.0):
        rmax = max(math.hypot(y-port[0], z-port[1]) for y, z in prof)
        r = 12.5
        while r < rmax:
            pts = [cam.p((x, port[0]+r*math.cos(t), port[1]+r*math.sin(t))) for t in [2*math.pi*k/90 for k in range(91)]]
            ax.plot([q[0] for q in pts], [q[1] for q in pts], color=WALD, lw=0.5, clip_path=patch)
            r += step*(1 + 0.035*(r/10))
    def cap_left(prof, port, hair):
        def extra(ax, cam, patch):
            rings(ax, cam, 0, prof, port, patch)
            h = [cam.p((0, y, z)) for y, z in hair]
            ax.plot([h[0][0], h[1][0]], [h[0][1], h[1][1]], color=(0.20, 0.12, 0.06), lw=1.3)
            pts = [cam.p((0, port[0]+8*math.cos(t), port[1]+8*math.sin(t))) for t in [2*math.pi*k/40 for k in range(40)]]
            ax.add_patch(Polygon(pts, closed=True, fc=(0.10, 0.07, 0.05), ec="none"))
            pts = [cam.p((0, port[0]+10.5*math.cos(t), port[1]+10.5*math.sin(t))) for t in [2*math.pi*k/60 for k in range(61)]]
            ax.plot([q[0] for q in pts], [q[1] for q in pts], color=(0.20, 0.12, 0.06), lw=0.9)
        return extra
    def cap_right(prof, port, hair, jk):
        def extra(ax, cam, patch):
            rings(ax, cam, W, prof, port, patch)
            h = [cam.p((W, y, z)) for y, z in hair]
            ax.plot([h[0][0], h[1][0]], [h[0][1], h[1][1]], color=(0.20, 0.12, 0.06), lw=1.3)
            for (y, z), k in jk:
                if k == "j": r = 3.2; col = (0.09, 0.08, 0.07)
                elif k == "pot": r = 2.4; col = (0.75, 0.73, 0.70)
                else: r = None
                if r:
                    pts = [cam.p((W+0.3, y+r*math.cos(t), z+r*math.sin(t))) for t in [2*math.pi*q/24 for q in range(24)]]
                else:
                    w, hh = (4.5, 2.0) if k == "usb" else (4.0, 2.0)
                    pts = [cam.p((W+0.3, y+dy, z+dz)) for dy, dz in ((-w, -hh), (w, -hh), (w, hh), (-w, hh))]
                    col = (0.09, 0.08, 0.07)
                ax.add_patch(Polygon(pts, closed=True, fc=col, ec="none"))
        return extra

    xs1 = [22 + i*(W-44)/9 for i in range(10)]; xs2 = [22 + (i+0.5)*(W-44)/9 for i in range(9)]

    def build(sc, cam, tf=ident, kb_front=False, packed=False, plate=True, stretcher=False):
        prof, slab, port, hair, ftt, th, jk = geo(tf)
        if packed: keyboard(sc, cam, W/2-KB_W/2, 4, z0=-KB_H, keys_up=False)
        far_is_right = cam.c[0] < 0
        Lfar = sc.layer()
        if far_is_right: extrude(Lfar, cam, prof, W-CHK, W, WAL, ec=WALD)
        else: extrude(Lfar, cam, prof, 0, CHK, WAL, cap_extra=cap_left(prof, port, hair), ec=WALD)
        if stretcher:
            Ls = sc.layer(); box(Ls, cam, CHK, W-CHK, 20, 80, 0, 6, WALD)
        L = sc.layer(); extrude(L, cam, slab, CHK, W-CHK, WAL)
        Lnear = sc.layer()
        if far_is_right:
            extrude(Lnear, cam, prof, 0, CHK, WAL, cap_extra=cap_left(prof, port, hair), ec=WALD)
        else:
            Lr = Lnear
            prof_c = ccw(prof)
            m = len(prof_c)
            for i in range(m):
                (y1, z1), (y2, z2) = prof_c[i], prof_c[(i+1) % m]
                dy, dz = y2-y1, z2-z1; Ln = math.hypot(dy, dz)
                if Ln < 1e-9: continue
                nn = (0.0, dz/Ln, -dy/Ln)
                add_face(Lr, cam, [(W-CHK, y1, z1), (W, y1, z1), (W, y2, z2), (W-CHK, y2, z2)], nn, WAL, ec=WAL)
            add_face(Lr, cam, [(W, y, z) for y, z in prof_c], (1.0, 0.0, 0.0), WAL, ec=WALD, extra=cap_right(prof, port, hair, jk))
            add_face(Lr, cam, [(W-CHK, y, z) for y, z in prof_c[::-1]], (-1.0, 0.0, 0.0), WAL)
        if not plate: return
        P, n = plate_frame(ftt, th, W)
        L2 = sc.layer(); field(L2, cam, P, n, 8, W-8, 9, GN_D-5)
        L3 = sc.layer()
        for xc in (W*0.36, W*0.64): lancet_window(L3, cam, P, n, xc, 74, lw=1.3)
        L4 = sc.layer()
        for x in xs1: knob(L4, cam, P, n, x, 20)
        for i, x in enumerate(xs2): knob(L4, cam, P, n, x, 41, col=RED if i == 4 else BLACK)
        if kb_front: keyboard(sc, cam, W/2-KB_W/2, -KB_D-60)

    prof, slab, port, hair, ftt, th, jk = geo(ident)
    fig = new_sheet("GNOMON · the lid on its own cheeks",
                    "CATHEDRAL's framed lid standing on its own ends: the rim carries on down into two cheeks, open underneath. "
                    "Plate and rear face are square: angled on its runners, or upright on its back.",
                    f"280 × 122 × 66 mm · ≈ {math.degrees(GN_TH):.1f}° or 90° · no moving parts",
                    scales="end view 3:2, 3/4 views 1:2")
    # 1. end view
    box_mm = (14, 433, 328, 110)
    heading(fig, box_mm, "1  End view (3:2): a true gnomon (tan θ = T/D, rear face 2T)")
    ax = axes_mm(fig, box_mm, 1.5, (62, 32))
    poly = Polygon(prof, closed=True, fc=WAL, ec=WALD, lw=2.2, joinstyle="round"); ax.add_patch(poly)
    rmax = max(math.hypot(y-port[0], z-port[1]) for y, z in prof); r = 12.5
    while r < rmax:
        ax.add_patch(Circle(port, r, fc="none", ec=WALD, lw=0.8, clip_path=poly)); r += 6.0*(1 + 0.035*(r/10))
    ax.plot([hair[0][0], hair[1][0]], [hair[0][1], hair[1][1]], color=(0.20, 0.12, 0.06), lw=1.8)
    ax.add_patch(Circle(port, 8, fc=(0.10, 0.07, 0.05), ec="none"))
    ax.add_patch(Circle(port, 10.5, fc="none", ec=(0.20, 0.12, 0.06), lw=1.4))
    for (y0, y1) in ((3, 14), (Rq[0]-14, Rq[0]-3)): ax.add_patch(Rectangle((y0, -1.6), y1-y0, 1.6, fc=TPU, ec="none"))
    ax.add_patch(Rectangle((20, 0), 60, 6, fc="none", ec=INK, lw=1.2, ls=(0, (5, 3))))
    # right-angle mark at bt
    u = (cth, sth); v = (sth, -cth); k = 6
    ax.plot([bt[0]-u[0]*k, bt[0]-u[0]*k+v[0]*k, bt[0]+v[0]*k], [bt[1]-u[1]*k, bt[1]-u[1]*k+v[1]*k, bt[1]+v[1]*k], color=CREAM, lw=1.6)
    ground(ax, -50, 175)
    leader(ax, (bt[0]+2, bt[1]-6), "plate and rear face square", (122, 66))
    leader(ax, (port[0]+5, port[1]+5), "port: grooves only", (122, 50))
    leader(ax, (60, 21.5), "hairline: the lid above,\nits own thickness below", (122, 30))
    leader(ax, (ft[0]+4, ft[1]-2), "lip rounded\ninto the plate", (-48, 50))
    leader(ax, (50, 4), "stretcher:\nSHOE only", (-48, 14))
    scale_bar(ax, 122, 4, 50, "50 mm (at 3:2)")
    # 2. playing
    cam = Cam(46, 20); sc = Scene(cam); build(sc, cam, kb_front=True)
    box_mm = (14, 321, 328, 100)
    heading(fig, box_mm, "2  Playing angled (1:2), the keyboard in front")
    cpt = cam.p((W/2, -45, 22)); ax = axes_mm(fig, box_mm, 0.5, (cpt[0]+10, cpt[1]+12)); sc.draw(ax)
    hl = cam.p((0, (hair[0][0]+hair[1][0])/2, (hair[0][1]+hair[1][1])/2))
    leader(ax, hl, "hairline: the slab\non its own cheek", (hl[0]-150, hl[1]+12), ha="left")
    # 3. from behind, right end: open underneath, the jacks
    camr = Cam(180+56, 12); scr = Scene(camr)
    Lg = scr.layer(); add_face(Lg, camr, [(-6, -14, -0.2), (W+6, -14, -0.2), (W+6, Rq[0]+6, -0.2), (-6, Rq[0]+6, -0.2)], (0, 0, 1), (0.86, 0.83, 0.78), ec=(0.86, 0.83, 0.78))
    build(scr, camr, plate=False)
    box_mm = (14, 225, 160, 84)
    heading(fig, box_mm, "3  From behind (1:2)")
    cpt = camr.p((W/2, 60, 30)); ax = axes_mm(fig, box_mm, 0.5, (cpt[0]+10, cpt[1]+6)); scr.draw(ax)
    jp = camr.p((W, jk[4][0][0], jk[4][0][1]))
    leader(ax, jp, "jacks on the\nright end", (jp[0]-20, jp[1]+70), size=SML-2, ha="center")
    hp = camr.p((W/2, 80, 0))
    ax.text(hp[0], hp[1]-22, "open underneath", ha="center", fontsize=SML-2, color=INK)
    # 4. upright on the rear face
    camu = Cam(180-34, 18); scu = Scene(camu)
    build(scu, camu, tf=tf_up)
    box_mm = (186, 225, 156, 84)
    heading(fig, box_mm, "4  Upright (1:2): on its back")
    cpt = camu.p((W/2, 30, 50)); ax = axes_mm(fig, box_mm, 0.5, (cpt[0], cpt[1]-8))
    keep = LIGHT; lu = (0.35, 0.75, 0.55); ln = math.sqrt(sum(v*v for v in lu)); LIGHT = tuple(v/ln for v in lu)
    scu.draw(ax); LIGHT = keep
    ax.text(cpt[0], cpt[1]-84, "plate vertical, turned to face you", ha="center", fontsize=SML-2, color=INK)
    # 5. packed on SHOE
    camp = Cam(36, 24); scp = Scene(camp); build(scp, camp, packed=True, stretcher=True)
    box_mm = (14, 131, 160, 80)
    heading(fig, box_mm, "5  Packed, SHOE (1:2)")
    cp = camp.p((W/2, 40, 12)); ax = axes_mm(fig, box_mm, 0.5, (cp[0], cp[1]+6)); scp.draw(ax)
    # 6. the two poses by shape, end silhouettes at 1:2
    box_mm = (186, 131, 156, 80)
    heading(fig, box_mm, "6  Two poses, one shape (1:2)")
    ax = axes_mm(fig, box_mm, 0.5, (125, 52))
    pu, _, _, hu, _, _, _ = geo(tf_up)
    for pp, hh, dx in ((prof, hair, 0), (pu, hu, 175)):
        ax.add_patch(Polygon([(y+dx, z) for y, z in pp], closed=True, fc=WAL, ec=WALD, lw=1.4))
        ax.plot([hh[0][0]+dx, hh[1][0]+dx], [hh[0][1], hh[1][1]], color=(0.20, 0.12, 0.06), lw=1.0)
    ground(ax, -20, 290)
    ax.text(55, -14, f"angled ≈ {math.degrees(GN_TH):.1f}°", ha="center", va="top", fontsize=SML-1, color=INK)
    upx = sum(y for y, z in pu)/len(pu) + 175
    ax.text(upx, -14, "upright 90°", ha="center", va="top", fontsize=SML-1, color=INK)
    # 7. loose, same size
    caml = Cam(36, 24); scl = Scene(caml)
    build(scl, caml)
    keyboard(scl, caml, W-10, -170)
    box_mm = (14, 22, 328, 97)
    heading(fig, box_mm, "7  Or loose (1:2, same size): no carry part, no stretcher")
    m_ = caml.p((W/2, 55, 30)); k_ = caml.p((W-10+KB_W/2, -125, 8))
    ax = axes_mm(fig, box_mm, 0.5, ((m_[0]+k_[0])/2 + 6, (m_[1]+k_[1])/2 - 4)); scl.draw(ax)
    save(fig, path)
    FIG_H = old_h

# ======================= CASKET-B =======================
def sheet_casket(path):
    W = 280.0
    mod = casket_angled_module(); lid, ly0 = casket_lid_angled()
    port_local = (60.0, 17.5)
    port = tilt([port_local], CA_TH)[0]
    fig = new_sheet("CASKET-B · closed, it's CATHEDRAL closed",
                    "A calm framed slab with his pipe façade on the lid. Open, the lid goes face down under the back and its own depth sets a low desk angle; "
                    "lid off, it plays flat. No moving parts.",
                    f"280 × 107 × 50 mm closed · flat or ≈ {math.degrees(CA_TH):.0f}° · two pieces")
    box_mm = (14, 306, 328, 120)
    heading(fig, box_mm, "1  End view (3:2): angled on its lid")
    ax = axes_mm(fig, box_mm, 1.5, (92, 22))
    ax.add_patch(Polygon(lid, closed=True, fc=WAL, ec=WALD, lw=2.2))
    ax.plot([ly0+4, ly0+CA_LIDD-4], [CA_LID-3, CA_LID-3], color=(0.55, 0.38, 0.24), lw=1.2)
    end_face_2d(ax, mod, port, strips=((3, 14),))
    ground(ax, -10, 205)
    leader(ax, (ly0+80, 8), "lid, face down, in the groove:\nshows ≈ 80 behind", (130, 40))
    leader(ax, port, "port mouth at the heart of the end grain", (-10, 58))
    scale_bar(ax, 150, 60, 50, "50 mm (at 3:2)")
    # 3/4 playing angled
    def module(sc, cam, th, y_off=0.0, z_off=0.0, knobs=True):
        prof = [(y+y_off, z+z_off) for y, z in tilt(casket_module_local(), th)]
        pp = tilt([port_local], th)[0]; pp = (pp[0]+y_off, pp[1]+z_off)
        L = sc.layer(); extrude(L, cam, prof, 0, W, WAL, cap_extra=rings_on_cap(pp, 0, prof))
        tl = tilt([(0, CA_T)], th)[0]
        P, n = plate_frame((tl[0]+y_off, tl[1]+z_off), th, W)
        L2 = sc.layer(); field(L2, cam, P, n, 8, W-8, 5, CA_D-5)
        L3 = sc.layer()
        for xc in (W*0.36, W*0.64): lancet_window(L3, cam, P, n, xc, 75, lw=1.3)
        if knobs:
            L4 = sc.layer()
            xs1 = [22 + i*(W-44)/9 for i in range(10)]; xs2 = [22 + (i+0.5)*(W-44)/9 for i in range(9)]
            for x in xs1: knob(L4, cam, P, n, x, 18)
            for i, x in enumerate(xs2): knob(L4, cam, P, n, x, 40, col=RED if i == 4 else BLACK)
    cam = Cam(28, 26); sc = Scene(cam)
    Ll = sc.layer(); extrude(Ll, cam, lid, -1, W+1, WAL)
    module(sc, cam, CA_TH)
    keyboard(sc, cam, W/2-KB_W/2, -KB_D-50)
    box_mm = (14, 178, 328, 132)
    heading(fig, box_mm, "2  Playing angled (1:2), the keyboard in front")
    cpt = cam.p((W/2, -10, 18)); ax = axes_mm(fig, box_mm, 0.5, (cpt[0], cpt[1]+6)); sc.draw(ax)
    # closed 3/4 with facade
    def facade(sc, cam, z_top):
        Lf = sc.layer()
        n = (0, 0, 1)
        npipe = 19
        for i in range(npipe):
            x = 46 + i*(W-92)/(npipe-1)
            hgt = 30 + 38*(1 - abs(i-(npipe-1)/2)/((npipe-1)/2))**1.3
            y0, w = 70, 7
            pts = [(x-w/2, y0-hgt, z_top), (x+w/2, y0-hgt, z_top), (x+w/2, y0, z_top), (x-w/2, y0, z_top), (x-w/2, y0-hgt, z_top)]
            add_line(Lf, cam, pts, BRASS, 1.0)
            add_line(Lf, cam, [(x-w/2, y0-hgt+9, z_top), (x, y0-hgt+5, z_top), (x+w/2, y0-hgt+9, z_top)], BRASS, 1.0)
        add_line(Lf, cam, [(36, 74, z_top), (W-36, 74, z_top)], BRASS, 1.0)
        add_line(Lf, cam, [(36, 80, z_top), (W-36, 80, z_top)], BRASS, 1.0)
    def closed(sc, cam, kb=False):
        if kb: keyboard(sc, cam, W/2-KB_W/2, 8, z0=-KB_H, keys_up=False)
        cl3 = fillet(ccw([(0, 0), (CA_D, 0), (CA_D, CA_T), (0, CA_T)]), 6)
        L = sc.layer(); extrude(L, cam, cl3, 0, W, WAL, cap_extra=rings_on_cap(port_local, 0, cl3))
        lid3 = fillet(ccw([(-1, CA_T), (CA_D+1, CA_T), (CA_D+1, CA_T+CA_LID), (-1, CA_T+CA_LID)]), 5)
        L2 = sc.layer(); extrude(L2, cam, lid3, -1, W+1, WAL, ec=WALD)
        facade(sc, cam, CA_T+CA_LID+0.3)
    cam2 = Cam(28, 30); sc2 = Scene(cam2); closed(sc2, cam2)
    box_mm = (14, 94, 160, 76)
    heading(fig, box_mm, "3  Closed (1:2): his façade on the lid")
    ax = axes_mm(fig, box_mm, 0.5, cam2.p((W/2, 50, 20))); sc2.draw(ax)
    ax.text(cam2.p((W/2, 50, 25))[0], cam2.p((W, 0, 0))[1]-32, "façade = placeholder for his design", ha="center", fontsize=SML-2, color=GREY)
    cam3 = Cam(28, 30); sc3 = Scene(cam3); closed(sc3, cam3, kb=True)
    box_mm = (182, 94, 160, 76)
    heading(fig, box_mm, "4  Packed (1:2): + SHOE")
    ax = axes_mm(fig, box_mm, 0.5, cam3.p((W/2, 50, 14))); sc3.draw(ax)
    # underside plan, once
    box_mm = (14, 22, 200, 62)
    heading(fig, box_mm, "5  Underside (1:2)")
    ax = axes_mm(fig, box_mm, 0.5, (150, 50))
    ax.add_patch(FancyBboxPatch((0, 0), W, CA_D, boxstyle="round,pad=0,rounding_size=14", fc=WAL, ec=WALD, lw=1.5))
    ax.add_patch(Rectangle((40, CA_D-70), 200, 60, fc=WALD, ec=(0.2, 0.12, 0.07), lw=1.2))
    ax.add_patch(Rectangle((0.5, CA_D-92), W-1, 12, fc=(0.25, 0.15, 0.09), ec="none"))
    ax.annotate("", (140, CA_D-60), (140, CA_D+6), arrowprops=dict(arrowstyle="-|>", color=CREAM, lw=2.5))
    ax.text(140, CA_D-40, "SHOE dock (all three)\nslides in from the front", ha="center", va="center", fontsize=SML-1, color=CREAM)
    ax.text(W+6, CA_D-86, "lid groove\n(CASKET)", ha="left", va="center", fontsize=SML-1, color=INK)
    ax.text(W+6, CA_D+2, "front", ha="left", va="center", fontsize=SML-1, color=INK)
    bag_inset(fig, (226, 22, 116, 62), [(fillet(ccw([(0, 0), (CA_D, 0), (CA_D, 50), (0, 50)]), 6), (40, 30), WAL), (KB_SECTION, (200, 15), KBC)], "or loose")
    save(fig, path)

if __name__ == "__main__":
    sheet_drop("../c-drop/sheet.png")
    sheet_gnomon("../c-gnomon/sheet.png")
    sheet_casket("../c-casket/sheet.png")
    print("theta drop %.1f gnomon %.1f casket %.1f" % (math.degrees(DR_T), math.degrees(GN_TH), math.degrees(CA_TH)))
