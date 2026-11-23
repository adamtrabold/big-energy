"""Quick line sketches for round 2 (owner 21:08: sketches, not renders).

EASEL (rev 2.1 + top utility band) and LOW GNOMON (rev 1, lid's rim).
Loose ink lines, paper ground, end view + one 3/4 view each, one shared scale.

Run from this folder:  python3 r2_sketch.py
Writes ../r2-easel/sketch.png, ../r2-lowgnomon/sketch.png, ../r2-sketches.png
"""
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.path import Path
from scipy.spatial import ConvexHull

PAPER = "#f6f1e7"
INK = "#26221e"
SOFT = "#8c8379"
RED = "#a8432f"
FONT = "DejaVu Sans"
plt.rcParams["font.family"] = FONT

RNG = np.random.default_rng(2111)


# --------------------------------------------------------------- line work
def wob(ax, xy, lw=2.0, color=INK, amp=0.45, closed=False, passes=2, alpha=0.9,
        dashed=False, over=1.2, z=3):
    """Hand-drawn line: resample, add smooth noise normal to the path, draw twice."""
    xy = np.asarray(xy, float)
    if closed:
        xy = np.vstack([xy, xy[:1]])
    seg = np.hypot(*np.diff(xy, axis=0).T)
    if seg.sum() < 1e-6:
        return
    s = np.concatenate([[0], np.cumsum(seg)])
    n = max(int(s[-1] / 0.8), 4)
    t = np.linspace(0, s[-1], n)
    x = np.interp(t, s, xy[:, 0]); y = np.interp(t, s, xy[:, 1])
    if not closed and over > 0:  # slight overshoot, like a pen run past the corner
        d0 = np.array([x[1]-x[0], y[1]-y[0]]); d0 /= (np.hypot(*d0) + 1e-9)
        d1 = np.array([x[-1]-x[-2], y[-1]-y[-2]]); d1 /= (np.hypot(*d1) + 1e-9)
        x = np.concatenate([[x[0]-d0[0]*over], x, [x[-1]+d1[0]*over]])
        y = np.concatenate([[y[0]-d0[1]*over], y, [y[-1]+d1[1]*over]])
        t = np.concatenate([[t[0]-over], t, [t[-1]+over]])
    dx = np.gradient(x); dy = np.gradient(y); L = np.hypot(dx, dy) + 1e-9
    nx, ny = -dy / L, dx / L
    for p in range(passes):
        ph = RNG.uniform(0, 2*np.pi, 3)
        k = RNG.uniform(0.6, 1.0)
        off = amp*k*(0.6*np.sin(t/23+ph[0]) + 0.3*np.sin(t/9+ph[1]) + 0.15*np.sin(t/3.7+ph[2]))
        if closed:  # keep the loop closed
            off = off - np.linspace(0, off[-1]-off[0], len(off))
        ax.plot(x+nx*off, y+ny*off, color=color, lw=lw*(1 if p == 0 else 0.55),
                alpha=alpha if p == 0 else alpha*0.6, solid_capstyle="round",
                ls=(0, (5, 4)) if dashed else "-", zorder=z)


FLIP = True   # end views seen from the RIGHT end (front on the left); 3/4 from front-right


def label(ax, x, y, s, size=13, color=INK, ha="left", va="center", **kw):
    if FLIP and ha in ("left", "right"): ha = "right" if ha == "left" else "left"
    ax.text(x, y, s, fontsize=size, color=color, ha=ha, va=va, zorder=10, **kw)


def leader(ax, p0, p1, color=SOFT):
    wob(ax, [p0, p1], lw=1.0, color=color, amp=0.25, passes=1, over=0)
    ax.plot(*p1, "o", ms=3, color=color, zorder=10)


# --------------------------------------------------------------- 2D geometry
def rounded(pts, radii, per=10):
    """Closed polygon (y,z) with a fillet radius per corner -> dense pts, corner-mid indices."""
    pts = [np.array(p, float) for p in pts]
    n = len(pts); out = []; mids = []
    for i in range(n):
        p0, p1, p2 = pts[i-1], pts[i], pts[(i+1) % n]
        r = radii[i]
        a = p0 - p1; b = p2 - p1
        a /= np.linalg.norm(a); b /= np.linalg.norm(b)
        ang = math.acos(np.clip(a @ b, -1, 1))
        if r <= 0 or ang > math.pi - 1e-3:
            mids.append(len(out)); out.append(p1); continue
        d = r / math.tan(ang/2)
        s0 = p1 + a*d; s1 = p1 + b*d
        bis = (a + b) / np.linalg.norm(a + b)
        c = p1 + bis * r / math.sin(ang/2)
        t0 = math.atan2(*(s0-c)[::-1]); t1 = math.atan2(*(s1-c)[::-1])
        dt = (t1 - t0 + math.pi) % (2*math.pi) - math.pi
        for k in range(per+1):
            if k == per//2: mids.append(len(out))
            th = t0 + dt*k/per
            out.append(c + r*np.array([math.cos(th), math.sin(th)]))
    return np.array(out), mids


def area(p):
    return 0.5*np.sum(p[:, 0]*np.roll(p[:, 1], -1) - np.roll(p[:, 0], -1)*p[:, 1])


def inward_normals(p):
    if area(p) < 0: sgn = -1
    else: sgn = 1
    prv = np.roll(p, 1, 0); nxt = np.roll(p, -1, 0)
    t = nxt - prv; t /= (np.linalg.norm(t, axis=1)[:, None] + 1e-9)
    # CCW polygon: inward normal = left of tangent
    n = np.stack([-t[:, 1], t[:, 0]], 1) * sgn
    return n


def ray_depth(p, i, n):
    """Distance from vertex i along inward normal n to the far boundary."""
    o = p[i]; best = 1e9
    m = len(p)
    for j in range(m):
        if j == i or (j+1) % m == i or j == (i-1) % m: continue
        a = p[j]; b = p[(j+1) % m]
        e = b - a
        den = n[0]*(-e[1]) - n[1]*(-e[0])
        if abs(den) < 1e-9: continue
        w = a - o
        tt = (w[0]*(-e[1]) - w[1]*(-e[0])) / den
        uu = (n[0]*w[1] - n[1]*w[0]) / den
        if tt > 0.5 and -1e-6 <= uu <= 1+1e-6: best = min(best, tt)
    return best


# --------------------------------------------------------------- 3D mesh
class Mesh:
    """Section (y,z) swept along x from 0..L; ends eased by a plan corner
    (n 5 superellipse) whose radius is big on near-vertical faces (CATHEDRAL's
    plan corners) and small on near-horizontal ones (rolled edges)."""
    def __init__(self, sec, x0, L, r_plan=17.5, r_roll=3.0, mids=(), soft_mids=(), steps=7, nexp=5):
        self.sec = sec; m = len(sec)
        nrm = inward_normals(sec)
        rv = np.array([r_roll + (r_plan - r_roll)*nrm[i, 0]**2 for i in range(m)])
        for i in range(m):
            rv[i] = min(rv[i], 0.42*ray_depth(sec, i, nrm[i]))
        phis = np.linspace(0, math.pi/2, steps)
        rings = []
        def ring(phi, right):
            c = math.cos(phi); s = math.sin(phi)
            xo = rv*(1 - c**(2/nexp)); ins = rv*(1 - s**(2/nexp))
            yz = sec + nrm*ins[:, None]
            x = (x0 + L - xo) if right else (x0 + xo)
            return np.column_stack([x, yz])
        for ph in phis: rings.append(ring(ph, False))
        for ph in phis[::-1]: rings.append(ring(ph, True))
        self.R = np.array(rings)   # K x m x 3
        self.K = len(rings); self.m = m
        self.mids = list(mids); self.soft_mids = list(soft_mids)
        self.centroid = self.R.reshape(-1, 3).mean(0)

    def faces(self):
        K, m = self.K, self.m; F = []
        for k in range(K-1):
            for j in range(m):
                F.append([(k, j), (k+1, j), (k+1, (j+1) % m), (k, (j+1) % m)])
        F.append([(0, j) for j in range(m)])
        F.append([(K-1, j) for j in range(m)])
        return F


class Cam:
    def __init__(self, yaw=34, pitch=24):
        y = math.radians(yaw); p = math.radians(pitch)
        self.c = np.array([-math.sin(y)*math.cos(p), -math.cos(y)*math.cos(p), math.sin(p)])
        f = -self.c
        r = np.cross(f, [0, 0, 1]); self.r = r/np.linalg.norm(r)
        self.u = np.cross(self.r, f); self.f = f

    def P(self, X):
        X = np.asarray(X, float)
        return np.stack([X @ self.r, X @ self.u], -1)

    def depth(self, X):
        return np.asarray(X) @ self.f


def draw_mesh(ax, cam, M, lw=2.1, color=INK, soft=SOFT, fill=PAPER, z=3):
    F = M.faces(); V = M.R
    vis = []
    for f in F:
        pts = np.array([V[k, j] for k, j in f])
        if len(f) == 4:
            nrm = np.cross(pts[1]-pts[0], pts[3]-pts[0])
            if np.linalg.norm(nrm) < 1e-9:
                nrm = np.cross(pts[2]-pts[1], pts[0]-pts[1])
        else:
            nrm = np.zeros(3)
            for i in range(len(pts)):
                nrm += np.cross(pts[i], pts[(i+1) % len(pts)])
        if nrm @ (pts.mean(0) - M.centroid) < 0: nrm = -nrm
        vis.append(nrm @ cam.c > 1e-9)
    # fill visible faces (covers anything drawn behind)
    for f, v in zip(F, vis):
        if not v: continue
        pts = cam.P(np.array([V[k, j] for k, j in f]))
        ax.fill(pts[:, 0], pts[:, 1], color=fill, lw=0.6, ec=fill, zorder=z)
    # edges -> faces
    E = {}
    for fi, f in enumerate(F):
        for i in range(len(f)):
            a, b = f[i], f[(i+1) % len(f)]
            E.setdefault(frozenset((a, b)), []).append(fi)
    sil = []
    for e, fs in E.items():
        vv = [vis[i] for i in fs]
        if len(fs) == 2 and vv[0] != vv[1]: sil.append(tuple(e))
    for pl in chain(sil):
        wob(ax, cam.P(np.array([V[k, j] for k, j in pl])), lw=lw, color=color, z=z+0.5)
    # end-cap rims (where the cap and the rounding are both visible): light
    for capk in (0, M.K-1):
        capf = len(F) - (2 if capk == 0 else 1)
        if not vis[capf]: continue
        run = []
        for j in range(M.m):
            fi = (0 if capk == 0 else M.K-2)*M.m + j
            if vis[fi]: run.append(j)
            elif run:
                draw_run(ax, cam, V, capk, run, soft, z); run = []
        if run: draw_run(ax, cam, V, capk, run, soft, z)
    # feature lines along x at corner mids (only where both sides visible)
    for j, wgt in [(j, 1.0) for j in M.mids] + [(j, 0.5) for j in M.soft_mids]:
        seg = []
        for k in range(M.K-1):
            fa = k*M.m + j; fb = k*M.m + (j-1) % M.m
            if vis[fa] and vis[fb]: seg.append(k)
            elif seg:
                draw_feat(ax, cam, V, seg, j, wgt, lw, color, soft, z); seg = []
        if seg: draw_feat(ax, cam, V, seg, j, wgt, lw, color, soft, z)
    return vis


def draw_run(ax, cam, V, k, run, soft, z):
    if len(run) < 2: return
    pts = np.array([V[k, j] for j in run] + [V[k, (run[-1]+1) % V.shape[1]]])
    wob(ax, cam.P(pts), lw=1.0, color=soft, amp=0.3, passes=1, over=0, z=z+0.4)


def draw_feat(ax, cam, V, seg, j, wgt, lw, color, soft, z):
    pts = np.array([V[k, j] for k in seg] + [V[seg[-1]+1, j]])
    if wgt >= 1: wob(ax, cam.P(pts), lw=lw*0.75, color=color, z=z+0.45)
    else: wob(ax, cam.P(pts), lw=1.0, color=soft, amp=0.3, passes=1, z=z+0.45)


def chain(edges):
    adj = {}
    for a, b in edges:
        adj.setdefault(a, []).append(b); adj.setdefault(b, []).append(a)
    used = set(); out = []
    def key(a, b): return frozenset((a, b))
    starts = [v for v in adj if len(adj[v]) != 2] + list(adj)
    for s in starts:
        for nb in adj[s]:
            if key(s, nb) in used: continue
            pl = [s, nb]; used.add(key(s, nb)); cur = nb; prev = s
            while True:
                nxt = [w for w in adj[cur] if key(cur, w) not in used]
                if not nxt or len(adj[cur]) > 2: break
                w = nxt[0]; used.add(key(cur, w)); pl.append(w); prev, cur = cur, w
            out.append(pl)
    return out


# --------------------------------------------------------------- small parts
def plane_circle(o, eu, ev, r, n=28):
    t = np.linspace(0, 2*np.pi, n, endpoint=False)
    return o + r*np.outer(np.cos(t), eu) + r*np.outer(np.sin(t), ev)


def knob3d(ax, cam, o, eu, ev, en, r=6.0, h=9.0, z=6.2, tick=True):
    b = plane_circle(o, eu, ev, r); t = plane_circle(o + en*h, eu, ev, r)
    pts = cam.P(np.vstack([b, t]))
    hull = ConvexHull(pts); hp = pts[hull.vertices]
    ax.fill(hp[:, 0], hp[:, 1], color=PAPER, zorder=z)
    wob(ax, hp, lw=1.4, amp=0.2, closed=True, passes=1, z=z+0.1)
    wob(ax, cam.P(t), lw=1.0, amp=0.15, closed=True, passes=1, color=INK, z=z+0.2)
    if tick:
        c = o + en*h
        wob(ax, cam.P(np.array([c, c + ev*r*0.8])), lw=1.2, amp=0.1, passes=1, over=0, z=z+0.3)


def kb_mesh(x0, y0):
    sec, mids = rounded([(y0, 0), (y0+90, 0), (y0+90, 16), (y0, 16)], [2, 2, 3, 3], per=6)
    return Mesh(sec, x0, 330, r_plan=8, r_roll=2, steps=5)


def draw_keyboard(ax, cam, x0, y0, color=SOFT):
    M = kb_mesh(x0, y0)
    draw_mesh(ax, cam, M, lw=1.5, color=color, soft="#b9b1a6", z=7)
    # keys on the top face: 15 white keys
    kx0, kx1 = x0 + 14, x0 + 330 - 14; ky0, ky1 = y0 + 8, y0 + 72
    w = (kx1 - kx0) / 15
    wob(ax, cam.P(np.array([[kx0, ky0, 16], [kx1, ky0, 16], [kx1, ky1, 16], [kx0, ky1, 16]])),
        lw=1.1, color=color, amp=0.25, closed=True, passes=1, z=8)
    for i in range(1, 15):
        x = kx0 + i*w
        wob(ax, cam.P(np.array([[x, ky0, 16], [x, ky1, 16]])), lw=0.9, color=color, amp=0.2,
            passes=1, over=0, z=8)
    pat = [1, 1, 0, 1, 1, 1, 0] * 3
    for i in range(14):
        if not pat[i]: continue
        x = kx0 + (i+1)*w
        q = np.array([[x-w*0.3, ky0+26, 16], [x+w*0.3, ky0+26, 16], [x+w*0.3, ky1, 16], [x-w*0.3, ky1, 16]])
        pq = cam.P(q); ax.fill(pq[:, 0], pq[:, 1], color=color, alpha=0.55, zorder=8.2, lw=0)


def rings_2d(center, sec, radii):
    """Concentric arcs about center, clipped to sec (2D)."""
    path = Path(sec); out = []
    for r in radii:
        t = np.linspace(0, 2*np.pi, 240)
        pts = np.column_stack([center[0] + r*np.cos(t), center[1] + r*np.sin(t)])
        inside = path.contains_points(pts)
        run = []
        for p, ok in zip(pts, inside):
            if ok: run.append(p)
            elif run:
                if len(run) > 3: out.append(np.array(run))
                run = []
        if len(run) > 3: out.append(np.array(run))
    return out


# =============================================================== EASEL
# rev 2.1 (systems) + the director's top band: predella 36, both faces 60°,
# plate (to the sharp apex) 58 + 17 = 75. Soft top r 6.
EA_F = 36.0
EA_PL = 58.0
S60, C60 = math.sin(math.radians(60)), math.cos(math.radians(60))
EA_H = EA_F + EA_PL*S60                       # sharp apex ≈ 101
EA_AY = EA_PL*C60                             # apex y ≈ 37.5
EA_D = EA_AY + EA_H/math.tan(math.radians(60))  # footprint ≈ 95.8
EA_TOP_R = 6.0
EA_TOP = EA_H - EA_TOP_R*(1/math.sin(math.radians(30)) - 1)  # real top ≈ 95
W = 280.0


def easel_section(pl=EA_PL):
    h = EA_F + pl*S60; ay = pl*C60; d = ay + h/math.tan(math.radians(60))
    pts = [(0, 0), (d, 0), (ay, h), (0, EA_F)]
    return pts, d, h


def easel_mesh():
    pts, d, h = easel_section()
    sec, mids = rounded(pts, [3, 4, EA_TOP_R, 4], per=8)
    # sharp-ish corners: base corners + predella lip -> mids; the soft top -> soft mid
    return Mesh(sec, 0, W, r_plan=17.5, r_roll=3, mids=[mids[0], mids[1], mids[3]],
                soft_mids=[mids[2]]), sec


def easel_plate_frame():
    o = np.array([0, 0, EA_F]); ev = np.array([0, C60, S60]); eu = np.array([1, 0, 0])
    en = np.array([0, -S60, C60])
    return o, eu, ev, en


def easel_end(ax, ox=0, oz=0, labels=True, kb=True, ghost=True):
    """End view of the left end: front on the right (u = -y)."""
    pts, d, h = easel_section()
    sec, _ = rounded(pts, [3, 4, EA_TOP_R, 4], per=10)
    U = lambda p: np.column_stack([ox - p[:, 0], oz + p[:, 1]])
    if ghost:  # rev 2.1 outline
        g, gd, gh = easel_section(58.0)
        gs, _ = rounded(g, [3, 4, EA_TOP_R, 4], per=10)
        wob(ax, U(gs), lw=1.0, color=SOFT, closed=True, passes=1, dashed=True, amp=0.2)
    # rings about the port mouth (end grain centroid ≈ y 34, z 32 here)
    for arc in rings_2d((34, 31), sec, [12, 24, 38]):
        wob(ax, U(arc), lw=0.9, color=SOFT, amp=0.2, passes=1, over=0)
    port = plane_circle(np.array([34, 31, 0.0]), np.array([1, 0, 0]), np.array([0, 1, 0]), 6)[:, :2]
    wob(ax, U(port), lw=1.4, closed=True, passes=1, amp=0.15)
    wob(ax, U(sec), lw=2.4, closed=True)
    # driver lying in the foot (dashed), cone down, firing out the front slots
    drv = np.array([(10, 6), (65, 6), (65, 30), (10, 30)])
    wob(ax, U(drv), lw=1.1, color=RED, closed=True, passes=1, dashed=True, amp=0.15)
    for zz in (8, 13, 18):
        wob(ax, U(np.array([(4, zz), (-5, zz)])), lw=1.0, color=RED, passes=1, amp=0.1, over=0)
    # controls: two knob rows + slim top band toggle
    o = np.array([0, EA_F]); ev = np.array([C60, S60]); en = np.array([-S60, C60])
    for s, hh, ww in [(14, 11, 12), (31, 11, 12), (48, 6, 5)]:
        b = o + ev*s
        q = np.array([b - ev*ww/2, b - ev*ww/2 + en*hh, b + ev*ww/2 + en*hh, b + ev*ww/2])
        wob(ax, U(q), lw=1.5, passes=1, amp=0.12, over=0)
    # ground
    wob(ax, [(ox - d - 30, oz), (ox + 230, oz)], lw=1.2, color=SOFT, passes=1, amp=0.15)
    if kb:
        kq = np.array([(-60, 0), (-150, 0), (-150, 16), (-60, 16)]); label(ax, ox + 105, oz + 8, "keyboard", size=11, color=SOFT, ha="center")
        wob(ax, U(kq), lw=1.2, color=SOFT, closed=True, passes=1, amp=0.15)
    if labels:
        # one angle mark at the heel, label outside the body
        aa = np.radians(np.linspace(0, 60, 16))
        wob(ax, np.column_stack([ox - d + 16*np.cos(aa), oz + 16*np.sin(aa)]),
            lw=1.0, color=SOFT, passes=1, amp=0.08, over=0)
        leader(ax, (ox - d - 8, oz + 46), (ox - d + 12, oz + 6))
        label(ax, ox - d - 24, oz + 52, "both faces 60°", size=12, color=SOFT, ha="left")
        # dims
        wob(ax, [(ox - d, oz - 12), (ox, oz - 12)], lw=1.0, color=INK, passes=1, amp=0.1, over=0)
        label(ax, ox - d/2, oz - 22, f"≈ {d:.0f} deep", ha="center", size=13)
        label(ax, ox + 12, oz + EA_TOP, f"≈ {EA_TOP:.0f} tall", size=13, va="bottom")
        wob(ax, [(ox - EA_AY, oz + EA_TOP), (ox + 10, oz + EA_TOP)], lw=0.8, color=SOFT, passes=1,
            amp=0.1, over=0, dashed=True)
        # callouts
        bt = U(np.array([o + ev*48 + en*6]))[0]
        leader(ax, (ox + 58, oz + 108), bt)
        label(ax, ox + 60, oz + 113, "slim top band: lights +\npower / TUNE / SPLIT", size=12, va="bottom")
        leader(ax, (ox + 58, oz + 56), U(np.array([o + ev*22 + en*11]))[0])
        label(ax, ox + 61, oz + 56, "two rows of controls", size=12)
        leader(ax, (ox + 30, oz + 30), (ox - 8, oz + 13))
        label(ax, ox + 33, oz + 30, "one speaker, lying in the foot,\nfiring out slots in the front",
              size=12, color=RED)
        g, gd, gh = easel_section(58.0)
        label(ax, ox - gd + 4, oz + 86, "rev 2.1\n(79 × 86)", size=10.5, color=SOFT, ha="right", va="bottom")
    return d


def easel_34(ax, cam, kb=True):
    M, sec = easel_mesh()
    draw_mesh(ax, cam, M)
    o, eu, ev, en = easel_plate_frame()
    # plate field (cream panel outline)
    s0, s1 = 4, EA_PL - 13
    q = np.array([o + eu*14 + ev*s0, o + eu*(W-14) + ev*s0, o + eu*(W-14) + ev*s1, o + eu*14 + ev*s1])
    wob(ax, cam.P(q), lw=1.0, color=SOFT, closed=True, passes=1, amp=0.2, z=5.6)
    # lancet slots in the predella front face (y = 0)
    for i in range(8):
        x = W/2 - 3.5*13 + i*13
        sl = np.array([[x-3, -0.1, 4], [x+3, -0.1, 4], [x+3, -0.1, 14], [x, -0.1, 17], [x-3, -0.1, 14]])
        wob(ax, cam.P(sl), lw=1.1, closed=True, passes=1, amp=0.1, z=5.6)
    # USB-C host port above the slots
    hp = np.array([[W/2-5, -0.1, 25], [W/2+5, -0.1, 25], [W/2+5, -0.1, 28.5], [W/2-5, -0.1, 28.5]])
    wob(ax, cam.P(hp), lw=1.0, closed=True, passes=1, amp=0.08, z=5.6)
    # controls: two rows of 11 at 22 pitch (gutter in the middle), sorted far to near
    ks = []
    for s in (14, 31):
        for i in range(11):
            x = 30 + i*22 + (6 if i > 5 else 0) - 3
            ks.append((x, s))
    ks.sort(key=lambda t: -cam.depth(o + eu*t[0] + ev*t[1]))
    for x, s in ks:
        knob3d(ax, cam, o + eu*x + ev*s, eu, ev, en, r=6.5, h=8)
    # top band: three small toggles left, four lights centre
    for x in (34, 48, 62):
        knob3d(ax, cam, o + eu*x + ev*48, eu, ev, en, r=3.2, h=5, tick=False)
    for x in (W/2 - 24, W/2 - 8, W/2 + 8, W/2 + 24):
        c = plane_circle(o + eu*x + ev*48, eu, ev, 1.8, n=12)
        pc = cam.P(c); ax.fill(pc[:, 0], pc[:, 1], color=INK, zorder=6.5)
    # port mouth on the left end cap + rings
    cap = M.R[0]
    capyz = cap[:, 1:]
    for arc in rings_2d((34, 31), capyz, [12, 24]):
        P3 = np.column_stack([np.full(len(arc), cap[0, 0]), arc])
        wob(ax, cam.P(P3), lw=0.8, color=SOFT, amp=0.15, passes=1, over=0, z=5.6)
    pm = plane_circle(np.array([cap[0, 0], 34, 31]), np.array([0, 1, 0]), np.array([0, 0, 1]), 6)
    wob(ax, cam.P(pm), lw=1.2, closed=True, passes=1, amp=0.1, z=5.6)
    if kb: draw_keyboard(ax, cam, W/2 - 165, -60 - 90)


# =============================================================== LOW GNOMON
TH = math.atan(35/(2*105))   # 9.46°
CT, ST = math.cos(TH), math.sin(TH)
LG_P1 = np.array([-35*ST, 35*CT])                 # top of the front face
LG_P2 = LG_P1 + 105*np.array([CT, ST])            # top-back
LG_B = LG_P2[0]                                   # back y ≈ 97.8
LG_HL = LG_B*math.tan(TH)                         # hairline height at the back ≈ 16.3
RIM = 2.0


def lg_sections():
    slab = [(0, 0), (LG_B, LG_HL), tuple(LG_P2), tuple(LG_P1)]
    wedge = [(0, 0), (LG_B, 0), (LG_B, LG_HL)]
    whole = [(0, 0), (LG_B, 0), tuple(LG_P2), tuple(LG_P1)]
    return slab, wedge, whole


def lg_end(ax, ox=0, oz=0, labels=True, kb=True):
    slab, wedge, whole = lg_sections()
    sec, _ = rounded(whole, [3, 4, 6, 10], per=10)
    U = lambda p: np.column_stack([ox - p[:, 0], oz + p[:, 1]])
    for arc in rings_2d((51, 22), sec, [12, 26, 42]):
        wob(ax, U(arc), lw=0.9, color=SOFT, amp=0.2, passes=1, over=0)
    for y, z in lg_jacks():
        jc = plane_circle(np.array([y, z, 0.0]), np.array([1, 0, 0]), np.array([0, 1, 0]), 3.2, n=16)[:, :2]
        wob(ax, U(jc), lw=1.2, closed=True, passes=1, amp=0.06)
    wob(ax, U(sec), lw=2.4, closed=True)
    # the hairline = the lid's rim step (slab 2 mm proud of the cheek)
    hl = np.array([(3, 0.5), (LG_B - 1, LG_HL)])
    wob(ax, U(hl), lw=1.6, passes=1, amp=0.15, over=0)
    # knob stubs on the plate (rows t 22 / 42) and the grille zone
    for t in (22, 42):
        b = LG_P1 + t*np.array([CT, ST]); en = np.array([-ST, CT]); ev = np.array([CT, ST])
        q = np.array([b - ev*6, b - ev*6 + en*11, b + ev*6 + en*11, b + ev*6])
        wob(ax, U(q), lw=1.5, passes=1, amp=0.12, over=0)
    # right angle mark, base and back
    c = np.array([LG_B, 0])
    wob(ax, U(np.array([c + (-7, 0), c + (-7, 7), c + (0, 7)])), lw=1.0, color=SOFT, passes=1, amp=0.05, over=0)
    wob(ax, [(ox - LG_B - 30, oz), (ox + 230, oz)], lw=1.2, color=SOFT, passes=1, amp=0.15)
    if kb:
        kq = np.array([(-60, 0), (-150, 0), (-150, 16), (-60, 16)]); label(ax, ox + 105, oz + 8, "keyboard", size=11, color=SOFT, ha="center")
        wob(ax, U(kq), lw=1.2, color=SOFT, closed=True, passes=1, amp=0.15)
    if labels:
        lip = U(np.array([LG_P1]))[0]
        wob(ax, [lip, (lip[0] - 60, lip[1])], lw=0.8, color=SOFT, passes=1, amp=0.1, over=0, dashed=True)
        aa = np.radians(np.linspace(180, 180 - math.degrees(TH), 10))
        wob(ax, np.column_stack([lip[0] + 52*np.cos(aa), lip[1] + 52*np.sin(aa)]), lw=1.0,
            color=SOFT, passes=1, amp=0.05, over=0)
        label(ax, ox - 60, oz + 62, "≈ 9.5°", size=12, color=SOFT, ha="center")
        wob(ax, [(ox - LG_B, oz - 12), (ox + 35*ST, oz - 12)], lw=1.0, passes=1, amp=0.1, over=0)
        label(ax, ox - LG_B/2, oz - 22, "≈ 104 deep", ha="center", size=13)
        wob(ax, [(ox - LG_B - 12, oz), (ox - LG_B - 12, oz + LG_P2[1])], lw=1.0, passes=1, amp=0.1, over=0)
        label(ax, ox - LG_B - 16, oz + LG_P2[1]/2, "52", ha="right", size=13)
        label(ax, ox - LG_B + 10, oz + 12, "90°", size=10.5, color=SOFT)
        leader(ax, (ox + 40, oz + 100), U(np.array([(60, 60*math.tan(TH))]))[0])
        label(ax, ox + 43, oz + 100, "the lid's rim: the slab stands\n2 mm proud of the cheek here",
              size=12, va="bottom")
        leader(ax, (ox + 40, oz + 58), U(np.array([(LG_B*0.25, 4)]))[0])
        label(ax, ox + 43, oz + 58, "cheek (the wedge):\nspeaker box + cells", size=12)
        leader(ax, (ox - 20, oz + 92), U(np.array([lg_jacks()[1]]))[0])
        label(ax, ox - 18, oz + 96, "jacks, one row on the right end", size=12, va="bottom", ha="right")
    return LG_B


def lg_jacks():
    """Right end: one row of 5 (phones, line, MIDI in / out, device USB-C), about 18.5 below the plate."""
    out = []
    for y in (22, 34, 46, 58, 70):
        zp = LG_P1[1] + (y - LG_P1[0])*math.tan(TH)
        out.append((y, zp - 18.5))
    return out


def lg_meshes():
    slab, wedge, whole = lg_sections()
    s_sec, s_m = rounded(slab, [2, 0.01, 6, 10], per=8)
    w_sec, w_m = rounded(wedge, [2, 4, 0.01], per=6)
    S = Mesh(s_sec, 0, W, r_plan=17.5, r_roll=3, mids=[s_m[2], s_m[3]], soft_mids=[])
    Wd = Mesh(w_sec, RIM, W - 2*RIM, r_plan=17.5, r_roll=3, mids=[w_m[1]], soft_mids=[])
    return S, Wd


def lg_plate_frame():
    o = np.array([0, LG_P1[0], LG_P1[1]]); eu = np.array([1, 0, 0])
    ev = np.array([0, CT, ST]); en = np.array([0, -ST, CT])
    return o, eu, ev, en


def lg_34(ax, cam, kb=True):
    S, Wd = lg_meshes()
    draw_mesh(ax, cam, Wd, z=3)
    draw_mesh(ax, cam, S, z=4)
    o, eu, ev, en = lg_plate_frame()
    s0, s1 = 6, 99
    q = np.array([o + eu*14 + ev*s0, o + eu*(W-14) + ev*s0, o + eu*(W-14) + ev*s1, o + eu*14 + ev*s1])
    wob(ax, cam.P(q), lw=1.0, color=SOFT, closed=True, passes=1, amp=0.2, z=5.6)
    # one grille at the output (right) end, rear band; lancet slots in a round field
    gc = o + eu*243 + ev*72
    wob(ax, cam.P(plane_circle(gc, eu, ev, 21, n=40)), lw=1.1, closed=True, passes=1, amp=0.15, z=5.6)
    for i in range(-3, 4):
        x = i*5.5; hh = math.sqrt(max(21**2 - x**2, 0)) - 5
        seg = np.array([gc + eu*x - ev*hh, gc + eu*x + ev*hh])
        wob(ax, cam.P(seg), lw=1.0, passes=1, amp=0.08, over=0, z=5.6)
    # utilities mirror it at the left end
    for x in (30, 44, 58):
        knob3d(ax, cam, o + eu*x + ev*72, eu, ev, en, r=3.2, h=5, tick=False)
    ks = []
    for t in (22, 42):
        for i in range(10):
            x = 30 + i*24 + (4 if i > 4 else 0) - 2
            ks.append((x, t))
    ks.sort(key=lambda t: -cam.depth(o + eu*t[0] + ev*t[1]))
    for x, t in ks:
        knob3d(ax, cam, o + eu*x + ev*t, eu, ev, en, r=6.5, h=8)
    # host port on the front face
    fy = lambda z: -z*math.tan(TH)
    hp = np.array([[W/2-5, fy(15)-0.1, 15], [W/2+5, fy(15)-0.1, 15], [W/2+5, fy(18.5)-0.1, 18.5],
                   [W/2-5, fy(18.5)-0.1, 18.5]])
    wob(ax, cam.P(hp), lw=1.0, closed=True, passes=1, amp=0.08, z=5.6)
    # rings on the left end (slab cap and cheek cap), port mouth on the slab band
    for M in (Wd, S):
        cap = M.R[-1]
        for arc in rings_2d((51, 22), cap[:, 1:], [12, 26]):
            P3 = np.column_stack([np.full(len(arc), cap[0, 0]), arc])
            wob(ax, cam.P(P3), lw=0.8, color=SOFT, amp=0.15, passes=1, over=0, z=5.6)
    for y, z in lg_jacks():
        pm = plane_circle(np.array([W + 0.1, y, z]), np.array([0, 1, 0]), np.array([0, 0, 1]), 3.2, n=16)
        wob(ax, cam.P(pm), lw=1.1, closed=True, passes=1, amp=0.06, z=5.7)
    if kb: draw_keyboard(ax, cam, W/2 - 165, -60 - 90)



# ---- EASEL rev 2.3: utilities on the right end face (owner: "Face or edge imo")
EA_UTIL = [(22, 19, "t"), (34, 19, "k"), (46, 19, "t")]   # (y, z, toggle/knob) on the right end


def easel_end(ax, ox=0, oz=0, labels=True, kb=True, ghost=False):
    pts, d, h = easel_section()
    sec, _ = rounded(pts, [3, 4, EA_TOP_R, 4], per=10)
    U = lambda p: np.column_stack([ox - p[:, 0], oz + p[:, 1]])
    for arc in rings_2d((34, 31), sec, [12, 24, 38]):
        wob(ax, U(arc), lw=0.9, color=SOFT, amp=0.2, passes=1, over=0)
    wob(ax, U(sec), lw=2.4, closed=True)
    drv = np.array([(10, 6), (65, 6), (65, 30), (10, 30)])
    wob(ax, U(drv), lw=1.1, color=RED, closed=True, passes=1, dashed=True, amp=0.15)
    for zz in (8, 13, 18):
        wob(ax, U(np.array([(4, zz), (-5, zz)])), lw=1.0, color=RED, passes=1, amp=0.1, over=0)
    # the three utilities, seen face-on on this (right) end
    for y, z, kind in EA_UTIL:
        r = 3.5 if kind == "k" else 2.6
        c = plane_circle(np.array([y, z, 0.0]), np.array([1, 0, 0]), np.array([0, 1, 0]), r, n=18)[:, :2]
        wob(ax, U(c), lw=1.6, closed=True, passes=1, amp=0.05)
        if kind == "t":
            wob(ax, U(np.array([(y, z), (y, z + 4)])), lw=1.6, passes=1, amp=0.03, over=0)
    o = np.array([0, EA_F]); ev = np.array([C60, S60]); en = np.array([-S60, C60])
    for s_, hh, ww in [(14, 11, 12), (31, 11, 12)]:
        b = o + ev*s_
        q = np.array([b - ev*ww/2, b - ev*ww/2 + en*hh, b + ev*ww/2 + en*hh, b + ev*ww/2])
        wob(ax, U(q), lw=1.5, passes=1, amp=0.12, over=0)
    wob(ax, [(ox - d - 30, oz), (ox + 230, oz)], lw=1.2, color=SOFT, passes=1, amp=0.15)
    if kb:
        kq = np.array([(-60, 0), (-150, 0), (-150, 16), (-60, 16)])
        wob(ax, U(kq), lw=1.2, color=SOFT, closed=True, passes=1, amp=0.15)
        label(ax, ox + 105, oz + 8, "keyboard", size=11, color=SOFT, ha="center")
    if labels:
        aa = np.radians(np.linspace(0, 60, 16))
        wob(ax, np.column_stack([ox - d + 16*np.cos(aa), oz + 16*np.sin(aa)]),
            lw=1.0, color=SOFT, passes=1, amp=0.08, over=0)
        leader(ax, (ox - d + 2, oz + 66), (ox - EA_AY - 30, oz + 52))
        label(ax, ox - d, oz + 70, "both faces 60°", size=12, color=SOFT, ha="right")
        wob(ax, [(ox - d, oz - 12), (ox, oz - 12)], lw=1.0, color=INK, passes=1, amp=0.1, over=0)
        label(ax, ox - d/2, oz - 22, f"≈ {d:.0f} deep", ha="center", size=13)
        label(ax, ox + 12, oz + EA_TOP, f"≈ {EA_TOP:.0f} tall", size=13, va="bottom")
        wob(ax, [(ox - EA_AY, oz + EA_TOP), (ox + 10, oz + EA_TOP)], lw=0.8, color=SOFT, passes=1,
            amp=0.1, over=0, dashed=True)
        leader(ax, (ox + 58, oz + 64), U(np.array([o + ev*22 + en*11]))[0])
        label(ax, ox + 61, oz + 64, "two rows of controls,\nlights on the face", size=12)
        leader(ax, (ox + 30, oz + 34), (ox - 8, oz + 13))
        label(ax, ox + 33, oz + 36, "one speaker, lying in the foot,\nfiring out slots in the front",
              size=12, color=RED)
        leader(ax, (ox - 62, oz + 99), U(np.array([(46, 22)]))[0])
        label(ax, ox - 62, oz + 101, "power / TUNE / SPLIT on this end", size=12, ha="center", va="bottom")
        # fallback inset: 10 mm face band, predella 28, plate 68 (84 x 81), at 0.45 scale
        k = 0.45; ix, iz = ox + 205, oz + 62
        bp = [(0, 0), (68*C60 + (28 + 68*S60)/math.tan(math.radians(60)), 0), (68*C60, 28 + 68*S60), (0, 28)]
        bs, _ = rounded(bp, [3, 4, EA_TOP_R, 4], per=8)
        Ui = lambda p: np.column_stack([ix - k*p[:, 0], iz + k*p[:, 1]])
        wob(ax, Ui(bs), lw=1.1, color=SOFT, closed=True, passes=1, dashed=True, amp=0.1)
        b = np.array([0, 28]) + np.array([C60, S60])*50
        wob(ax, Ui(np.array([b, b + np.array([-S60, C60])*6])), lw=1.4, color=SOFT, passes=1, amp=0.05, over=0)
        label(ax, ix - 20, iz - 9, "fallback: 10 mm face band\nfor them, 84 × 81", size=10.5,
              color=SOFT, ha="center", va="top")
    return d


def easel_34(ax, cam, kb=True):
    M, sec = easel_mesh()
    draw_mesh(ax, cam, M)
    o, eu, ev, en = easel_plate_frame()
    s0, s1 = 4, EA_PL - 11
    q = np.array([o + eu*14 + ev*s0, o + eu*(W-14) + ev*s0, o + eu*(W-14) + ev*s1, o + eu*14 + ev*s1])
    wob(ax, cam.P(q), lw=1.0, color=SOFT, closed=True, passes=1, amp=0.2, z=5.6)
    for i in range(8):
        x = W/2 - 3.5*13 + i*13
        sl = np.array([[x-3, -0.1, 4], [x+3, -0.1, 4], [x+3, -0.1, 14], [x, -0.1, 17], [x-3, -0.1, 14]])
        wob(ax, cam.P(sl), lw=1.1, closed=True, passes=1, amp=0.1, z=5.6)
    hp = np.array([[W/2-5, -0.1, 25], [W/2+5, -0.1, 25], [W/2+5, -0.1, 28.5], [W/2-5, -0.1, 28.5]])
    wob(ax, cam.P(hp), lw=1.0, closed=True, passes=1, amp=0.08, z=5.6)
    ks = []
    for s_ in (14, 31):
        for i in range(11):
            x = 30 + i*22 + (6 if i > 5 else 0) - 3
            ks.append((x, s_))
    ks.sort(key=lambda t: -cam.depth(o + eu*t[0] + ev*t[1]))
    for x, s_ in ks:
        knob3d(ax, cam, o + eu*x + ev*s_, eu, ev, en, r=6.5, h=8)
    for x in (W/2 - 24, W/2 - 8, W/2 + 8, W/2 + 24):
        c = plane_circle(o + eu*x + ev*43, eu, ev, 1.8, n=12)
        pc = cam.P(c); ax.fill(pc[:, 0], pc[:, 1], color=INK, zorder=6.5)
    cap = M.R[-1]; xc = cap[0, 0]
    for arc in rings_2d((34, 31), cap[:, 1:], [12, 24]):
        P3 = np.column_stack([np.full(len(arc), xc), arc])
        wob(ax, cam.P(P3), lw=0.8, color=SOFT, amp=0.15, passes=1, over=0, z=5.6)
    ey = np.array([0, 1, 0]); ez = np.array([0, 0, 1]); ex = np.array([1, 0, 0])
    for y, z, kind in EA_UTIL:
        knob3d(ax, cam, np.array([xc, y, z]), ey, ez, ex, r=3.5 if kind == "k" else 2.6,
               h=6 if kind == "k" else 4, tick=(kind == "k"))
    if kb: draw_keyboard(ax, cam, W/2 - 165, -60 - 90)



# ---- EASEL rev 2.4 (systems, after the director's 8): mirrored face, true count,
# lancets raised above keyboard height, end controls in a flush pocket.
EA_F = 37.0                                     # predella ≈ 37 (plenum needs driver centre ≥ 38.5 back)
EA_H = EA_F + EA_PL*S60
EA_D = EA_AY + EA_H/math.tan(math.radians(60))
EA_TOP = EA_H - EA_TOP_R*(1/math.sin(math.radians(30)) - 1)
EA_POCKET = (34, 19, 27, 14)                    # centre y, centre z, width, height on the right end
EA_POCKET_CTRL = [(25, "t"), (34, "k"), (43, "t")]
COLS = [140 + (i - 5)*22 for i in range(11)]
TOP_ROW = ["ATTACK", "RELEASE", "PRESSURE", "SHIMMER", "DEPTH", "TAP",
           "ECHO", "TIME", "REPEATS", "REVERB", "VOLUME"]
LOW_ROW = ["OCT L", "tab", "tab", "tab", "HOLD", "lights",
           "FREE/\nSYNC", "tab", "tab", "tab", "OCT R"]
SLOT_X = [140 + (k - 2.5)*13 for k in range(6)]  # 6 lancets, z 18–32
SLOT_Z0, SLOT_Z1 = 18.0, 32.0
HOST_X = SLOT_X[0] - 20


def easel_section(pl=EA_PL, f=None):
    f = EA_F if f is None else f
    h = f + pl*S60; ay = pl*C60; d = ay + h/math.tan(math.radians(60))
    return [(0, 0), (d, 0), (ay, h), (0, f)], d, h


def _pocket_2d():
    y, z, w, h = EA_POCKET
    return rounded([(y - w/2, z - h/2), (y + w/2, z - h/2), (y + w/2, z + h/2), (y - w/2, z + h/2)],
                   [3, 3, 3, 3], per=5)[0]


def easel_end(ax, ox=0, oz=0, labels=True, kb=True, ghost=False):
    pts, d, h = easel_section()
    sec, _ = rounded(pts, [3, 4, EA_TOP_R, 4], per=10)
    U = lambda p: np.column_stack([ox - p[:, 0], oz + p[:, 1]])
    for arc in rings_2d((34, 31), sec, [12, 24, 38]):
        wob(ax, U(arc), lw=0.9, color=SOFT, amp=0.2, passes=1, over=0)
    wob(ax, U(sec), lw=2.4, closed=True)
    # driver in the foot + plenum up the front to the raised slots (dashed, red)
    drv = np.array([(12, 6), (67, 6), (67, 30), (12, 30)])
    wob(ax, U(drv), lw=1.1, color=RED, closed=True, passes=1, dashed=True, amp=0.15)
    wob(ax, U(np.array([(10, 6), (10, SLOT_Z1)])), lw=1.0, color=RED, passes=1, dashed=True, amp=0.1, over=0)
    for zz in (19.5, 25, 30.5):
        wob(ax, U(np.array([(4, zz), (-6, zz)])), lw=1.0, color=RED, passes=1, amp=0.1, over=0)
    # the flush pocket on this (right) end, controls inside, nothing proud
    wob(ax, U(_pocket_2d()), lw=1.5, closed=True, passes=1, amp=0.05)
    for y, kind in EA_POCKET_CTRL:
        r = 3.5 if kind == "k" else 2.2
        c = plane_circle(np.array([y, EA_POCKET[1], 0.0]), np.array([1, 0, 0]), np.array([0, 1, 0]), r, n=16)[:, :2]
        wob(ax, U(c), lw=1.2, closed=True, passes=1, amp=0.04)
    o = np.array([0, EA_F]); ev = np.array([C60, S60]); en = np.array([-S60, C60])
    for s_, hh, ww in [(14, 11, 12), (31, 11, 12)]:
        b = o + ev*s_
        q = np.array([b - ev*ww/2, b - ev*ww/2 + en*hh, b + ev*ww/2 + en*hh, b + ev*ww/2])
        wob(ax, U(q), lw=1.5, passes=1, amp=0.12, over=0)
    wob(ax, [(ox - d - 30, oz), (ox + 230, oz)], lw=1.2, color=SOFT, passes=1, amp=0.15)
    if kb:
        kq = np.array([(-6, 0), (-96, 0), (-96, 16), (-6, 16)])   # pushed right up to the front
        wob(ax, U(kq), lw=1.2, color=SOFT, closed=True, passes=1, amp=0.15)
        label(ax, ox + 51, oz + 8, "keyboard, pushed up", size=10.5, color=SOFT, ha="center")
    if labels:
        aa = np.radians(np.linspace(0, 60, 16))
        wob(ax, np.column_stack([ox - d + 16*np.cos(aa), oz + 16*np.sin(aa)]),
            lw=1.0, color=SOFT, passes=1, amp=0.08, over=0)
        leader(ax, (ox - d + 2, oz + 66), (ox - EA_AY - 30, oz + 52))
        label(ax, ox - d, oz + 70, "both faces 60°", size=12, color=SOFT, ha="right")
        wob(ax, [(ox - d, oz - 12), (ox, oz - 12)], lw=1.0, color=INK, passes=1, amp=0.1, over=0)
        label(ax, ox - d/2, oz - 22, f"≈ {d:.0f} deep", ha="center", size=13)
        label(ax, ox + 12, oz + EA_TOP, f"≈ {EA_TOP:.0f} tall", size=13, va="bottom")
        wob(ax, [(ox - EA_AY, oz + EA_TOP), (ox + 10, oz + EA_TOP)], lw=0.8, color=SOFT, passes=1,
            amp=0.1, over=0, dashed=True)
        leader(ax, (ox + 58, oz + 64), U(np.array([o + ev*22 + en*11]))[0])
        label(ax, ox + 61, oz + 64, "two rows of 11, mirrored", size=12)
        leader(ax, (ox + 60, oz + 36), (ox - 6, oz + 27))
        label(ax, ox + 63, oz + 38, "speaker slots raised to 18–32 mm,\nclear of the keyboard",
              size=12, color=RED)
        leader(ax, (ox - 62, oz + 99), U(np.array([(EA_POCKET[0] + 10, EA_POCKET[1] + 4)]))[0])
        label(ax, ox - 62, oz + 101, "power / TUNE / SPLIT in a flush pocket", size=12, ha="center",
              va="bottom")
    return d


def _tab(ax, cam, o, eu, ev, en, x, s_):
    q = np.array([o + eu*(x-3.5) + ev*(s_-6), o + eu*(x+3.5) + ev*(s_-6),
                  o + eu*(x+3.5) + ev*(s_+6), o + eu*(x-3.5) + ev*(s_+6)])
    top = q + en*4
    P = cam.P(np.vstack([q, top])); hull = ConvexHull(P); hp = P[hull.vertices]
    ax.fill(hp[:, 0], hp[:, 1], color=PAPER, zorder=6.2)
    wob(ax, hp, lw=1.3, amp=0.1, closed=True, passes=1, z=6.3)
    wob(ax, cam.P(top), lw=0.9, amp=0.08, closed=True, passes=1, z=6.4)


def easel_34(ax, cam, kb=True):
    M, sec = easel_mesh()
    draw_mesh(ax, cam, M)
    o, eu, ev, en = easel_plate_frame()
    s0, s1 = 4, EA_PL - 11
    q = np.array([o + eu*14 + ev*s0, o + eu*(W-14) + ev*s0, o + eu*(W-14) + ev*s1, o + eu*14 + ev*s1])
    wob(ax, cam.P(q), lw=1.0, color=SOFT, closed=True, passes=1, amp=0.2, z=5.6)
    for x in SLOT_X:
        sl = np.array([[x-3.5, -0.1, SLOT_Z0], [x+3.5, -0.1, SLOT_Z0], [x+3.5, -0.1, SLOT_Z1-4],
                       [x, -0.1, SLOT_Z1], [x-3.5, -0.1, SLOT_Z1-4]])
        wob(ax, cam.P(sl), lw=1.1, closed=True, passes=1, amp=0.1, z=5.6)
    hp = np.array([[HOST_X-5, -0.1, 23.5], [HOST_X+5, -0.1, 23.5], [HOST_X+5, -0.1, 27], [HOST_X-5, -0.1, 27]])
    wob(ax, cam.P(hp), lw=1.0, closed=True, passes=1, amp=0.08, z=5.6)
    items = []
    for i, nm in enumerate(TOP_ROW): items.append((COLS[i], 31, nm))
    for i, nm in enumerate(LOW_ROW): items.append((COLS[i], 14, nm))
    items.sort(key=lambda t: -cam.depth(o + eu*t[0] + ev*t[1]))
    for x, s_, nm in items:
        if nm == "TAP":
            knob3d(ax, cam, o + eu*x + ev*s_, eu, ev, en, r=5.0, h=3, tick=False)
            wob(ax, cam.P(plane_circle(o + eu*x + ev*s_, eu, ev, 7.5)), lw=0.9, color=SOFT,
                closed=True, passes=1, amp=0.05, z=6.1)
        elif nm == "tab":
            _tab(ax, cam, o, eu, ev, en, x, s_)
        elif nm in ("HOLD", "FREE/\nSYNC"):
            knob3d(ax, cam, o + eu*x + ev*s_, eu, ev, en, r=3.0, h=5, tick=False)
        elif nm == "lights":
            for dx in (-4.5, 4.5):
                c = plane_circle(o + eu*(x+dx) + ev*s_, eu, ev, 1.8, n=12)
                pc = cam.P(c); ax.fill(pc[:, 0], pc[:, 1], color=INK, zorder=6.5)
        else:
            knob3d(ax, cam, o + eu*x + ev*s_, eu, ev, en, r=6.5, h=8)
    cap = M.R[-1]; xc = cap[0, 0]
    for arc in rings_2d((34, 31), cap[:, 1:], [12, 24]):
        P3 = np.column_stack([np.full(len(arc), xc), arc])
        wob(ax, cam.P(P3), lw=0.8, color=SOFT, amp=0.15, passes=1, over=0, z=5.6)
    pk = _pocket_2d()
    wob(ax, cam.P(np.column_stack([np.full(len(pk), xc), pk])), lw=1.2, closed=True, passes=1, amp=0.05, z=5.7)
    for y, kind in EA_POCKET_CTRL:
        c = plane_circle(np.array([xc, y, EA_POCKET[1]]), np.array([0, 1, 0]), np.array([0, 0, 1]),
                         3.5 if kind == "k" else 2.2, n=14)
        wob(ax, cam.P(c), lw=1.0, closed=True, passes=1, amp=0.04, z=5.8)
    if kb: draw_keyboard(ax, cam, W/2 - 165, -6 - 90)


def easel_face(ax):
    """Face-on strip: the mirrored layout with names (signal order left to right)."""
    wob(ax, rounded([(0, 0), (W, 0), (W, 56), (0, 56)], [6, 6, 6, 6], per=5)[0], lw=1.6, closed=True, passes=1)
    wob(ax, [(140, 2), (140, 54)], lw=0.8, color=SOFT, passes=1, dashed=True, amp=0.05, over=0)
    for row, zc in ((TOP_ROW, 41), (LOW_ROW, 17)):
        for x, nm in zip(COLS, row):
            if nm == "tab":
                wob(ax, rounded([(x-3.5, zc-5), (x+3.5, zc-5), (x+3.5, zc+5), (x-3.5, zc+5)], [1.5]*4, per=3)[0],
                    lw=1.2, closed=True, passes=1, amp=0.05)
            elif nm == "lights":
                for dx in (-4.5, 4.5): ax.plot(x+dx, zc, "o", ms=4, color=INK)
            elif nm in ("HOLD", "FREE/\nSYNC"):
                wob(ax, plane_circle(np.array([x, zc, 0.]), np.array([1, 0, 0]), np.array([0, 1, 0]), 3)[:, :2],
                    lw=1.2, closed=True, passes=1, amp=0.04)
            elif nm == "TAP":
                wob(ax, plane_circle(np.array([x, zc, 0.]), np.array([1, 0, 0]), np.array([0, 1, 0]), 5)[:, :2],
                    lw=1.3, closed=True, passes=1, amp=0.04)
                wob(ax, plane_circle(np.array([x, zc, 0.]), np.array([1, 0, 0]), np.array([0, 1, 0]), 7.5)[:, :2],
                    lw=0.8, color=SOFT, closed=True, passes=1, amp=0.04)
            else:
                wob(ax, plane_circle(np.array([x, zc, 0.]), np.array([1, 0, 0]), np.array([0, 1, 0]), 6.5)[:, :2],
                    lw=1.3, closed=True, passes=1, amp=0.05)
            nm2 = {"tab": "", "lights": "lights", "FREE/\nSYNC": "FREE/SYNC"}.get(nm, nm)
            if nm2:
                ax.text(x, zc - 8.5, nm2, fontsize=7, color=SOFT, ha="center", va="top", linespacing=0.9)


def single_easel(path):
    global B34
    if B34 is None: B34 = scene_bounds()
    fig = plt.figure(figsize=(9, 13.4), dpi=170, facecolor=PAPER)
    fig.text(0.05, 0.977, "EASEL", fontsize=26, weight="bold", color=INK, va="top")
    fig.text(0.05, 0.947, f"sketch · 280 × {EA_D:.0f} × {EA_TOP:.0f} mm · both faces 60° · one piece, no moving parts",
             fontsize=13.5, color=SOFT, va="top")
    a1 = fig.add_axes([0.03, 0.60, 0.94, 0.33]); setup(a1, END_XL, END_XR, END_ZB, END_ZT, flip=FLIP)
    easel_end(a1)
    label(a1, END_XR - 2, END_ZT - 4, "from the right end", size=12, color=SOFT, va="top", ha="right")
    wob(a1, [(150, END_ZB + 6), (200, END_ZB + 6)], lw=1.4, passes=1, amp=0.05, over=0)
    label(a1, 175, END_ZB + 12, "50 mm", size=10.5, color=SOFT, ha="center")
    a2 = fig.add_axes([0.03, 0.20, 0.94, 0.40]); setup(a2, *B34)
    easel_34(a2, CAM)
    a2.text(B34[0] + 2, B34[3] - 4, "3/4, keyboard pushed up to the front", fontsize=12, color=SOFT,
            va="top", ha="left")
    a3 = fig.add_axes([0.06, 0.07, 0.88, 0.13]); setup(a3, -4, W + 4, -4, 62)
    easel_face(a3)
    a3.text(-4, 59, "the face, mirrored about its centre line (signal order left to right)", fontsize=11,
            color=SOFT, va="bottom", ha="left")
    fig.text(0.05, 0.045, "Packed: SHOE in the base, the rim 1 mm over the knobs; a printed slip cover is optional.",
             fontsize=12.5, color=INK, va="top")
    fig.text(0.05, 0.025, "Flicking an end switch slides it at ≈ 5 N: steady it with the other hand.",
             fontsize=12.5, color=SOFT, va="top")
    fig.savefig(path, facecolor=PAPER); plt.close(fig)


# =============================================================== sheets
CAM = Cam(-34, 24)
END_XL, END_XR, END_ZB, END_ZT = -125, 245, -36, 128      # mm, end-view frame (u, z)


def scene_bounds():
    pts = []
    for build in (easel_mesh, ):
        M, _ = build(); pts.append(CAM.P(M.R.reshape(-1, 3)))
    S, Wd = lg_meshes(); pts += [CAM.P(S.R.reshape(-1, 3)), CAM.P(Wd.R.reshape(-1, 3))]
    pts.append(CAM.P(kb_mesh(W/2 - 165, -150).R.reshape(-1, 3)))
    P = np.vstack(pts)
    return P[:, 0].min() - 8, P[:, 0].max() + 8, P[:, 1].min() - 8, P[:, 1].max() + 14


B34 = None


def setup(ax, xl, xr, zb, zt, flip=False):
    ax.set_xlim(xr, xl) if flip else ax.set_xlim(xl, xr); ax.set_ylim(zb, zt); ax.set_aspect("equal"); ax.axis("off")


def single(name, end_fn, iso_fn, title, sub, path):
    global B34
    if B34 is None: B34 = scene_bounds()
    fig = plt.figure(figsize=(9, 12.2), dpi=170, facecolor=PAPER)
    fig.text(0.05, 0.975, title, fontsize=26, weight="bold", color=INK, va="top")
    fig.text(0.05, 0.94, sub, fontsize=13.5, color=SOFT, va="top")
    a1 = fig.add_axes([0.03, 0.53, 0.94, 0.39]); setup(a1, END_XL, END_XR, END_ZB, END_ZT, flip=FLIP)
    a1.set_facecolor(PAPER)
    end_fn(a1)
    label(a1, END_XR - 2, END_ZT - 4, "from the right end", size=12, color=SOFT, va="top", ha="right")
    a2 = fig.add_axes([0.03, 0.03, 0.94, 0.50]); setup(a2, *B34)
    iso_fn(a2, CAM)
    a2.text(B34[0] + 2, B34[3] - 4, "3/4, keyboard in front", fontsize=12, color=SOFT, va="top", ha="left")
    # scale bar on the end view
    wob(a1, [(150, END_ZB + 6), (200, END_ZB + 6)], lw=1.4, passes=1, amp=0.05, over=0)
    label(a1, 175, END_ZB + 12, "50 mm", size=10.5, color=SOFT, ha="center")
    fig.savefig(path, facecolor=PAPER); plt.close(fig)


def compare(path):
    global B34
    if B34 is None: B34 = scene_bounds()
    fig = plt.figure(figsize=(14, 11.0), dpi=150, facecolor=PAPER)
    fig.text(0.03, 0.975, "floss: two ways it can sit (sketches, same scale)", fontsize=26,
             weight="bold", color=INK, va="top")
    fig.text(0.03, 0.937, "one ground line, the same keyboard, the same scale: only the shape changes",
             fontsize=14, color=SOFT, va="top")
    cols = [("EASEL", easel_end, easel_34,
             "280 × 79 × 81 mm · 60° · narrow and upright; face mirrored,\n"
             "packed: SHOE in the base, rim over the knobs"),
            ("LOW GNOMON", lg_end, lg_34,
             "280 × 104 × 52 mm · ≈ 9.5° · the steadiest, zero parts,\n"
             "but no flat pose, and it reads close to SILL tilted")]
    for i, (nm, ef, isf, cap) in enumerate(cols):
        x0 = 0.02 + i*0.49
        fig.text(x0 + 0.01, 0.885, nm, fontsize=21, weight="bold", color=INK, va="top")
        a1 = fig.add_axes([x0, 0.56, 0.47, 0.30]); setup(a1, END_XL, END_XR, -22, 108, flip=FLIP)
        ef(a1, labels=False)
        a2 = fig.add_axes([x0, 0.15, 0.47, 0.42]); setup(a2, *B34)
        isf(a2, CAM)
        fig.text(x0 + 0.01, 0.13, cap, fontsize=14.5, color=INK, va="top", linespacing=1.4)
    wob(fig.axes[0], [(170, -14), (220, -14)], lw=1.4, passes=1, amp=0.05, over=0)
    label(fig.axes[0], 195, -7, "50 mm", size=11, color=SOFT, ha="center")
    fig.savefig(path, facecolor=PAPER); plt.close(fig)


if __name__ == "__main__":
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    single_easel(os.path.join(here, "..", "r2-easel", "sketch.png"))
    single("lowgnomon", lg_end, lg_34, "LOW GNOMON",
           "sketch · 280 × 104 × 52 mm · ≈ 9.5° by shape · base and back 90° · no moving parts",
           os.path.join(here, "..", "r2-lowgnomon", "sketch.png"))
    compare(os.path.join(here, "..", "r2-sketches.png"))
    print(f"EASEL: H sharp {EA_H:.1f}, top {EA_TOP:.1f}, D {EA_D:.1f}; LOW GNOMON theta {math.degrees(TH):.2f}, "
          f"back {LG_B:.1f}, hairline {LG_HL:.1f}, top {LG_P2[1]:.1f}, front lean {LG_P1[0]:.1f}")
