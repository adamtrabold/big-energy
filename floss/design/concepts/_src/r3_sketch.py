"""Round 3 quick line sketches: EASEL rev 2.4, SILL, TRIANGLE (b) [+ (a) inset], HULL (killed).

Same line language as r2_sketch.py (imported). End views look at the RIGHT end (front on the
left); 3/4 views from front-right. One scale for every end view, one for every 3/4.

Director text: put it in r3_director.json  {"EASEL": ["score", "opinion", "change"], ...}
and re-run; missing entries print as placeholders.

Run from this folder:  python3 r3_sketch.py
"""
import json, math, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import r2_sketch as r2
from r2_sketch import (wob, label, leader, rounded, Mesh, draw_mesh, knob3d, plane_circle,
                       draw_keyboard, kb_mesh, rings_2d, ConvexHull, PAPER, INK, SOFT, RED, W, CAM, setup)

HERE = os.path.dirname(os.path.abspath(__file__))
KB_Y0 = -96.0          # keyboard pushed up to ≈ 6 mm from every front
S45 = math.sqrt(0.5)


# ------------------------------------------------------------------ shared drawing helpers
def plate3(o2, ev2):
    """3D plate frame from a 2D origin (y,z) and unit direction along the plate (y,z)."""
    o = np.array([0, o2[0], o2[1]]); ev = np.array([0, ev2[0], ev2[1]])
    en = np.array([0, -ev2[1], ev2[0]]); eu = np.array([1, 0, 0])
    return o, eu, ev, en


def tab3(ax, cam, o, eu, ev, en, x, s_):
    q = np.array([o + eu*(x-3.5) + ev*(s_-6), o + eu*(x+3.5) + ev*(s_-6),
                  o + eu*(x+3.5) + ev*(s_+6), o + eu*(x-3.5) + ev*(s_+6)])
    top = q + en*4
    P = cam.P(np.vstack([q, top])); hp = P[ConvexHull(P).vertices]
    ax.fill(hp[:, 0], hp[:, 1], color=PAPER, zorder=6.2)
    wob(ax, hp, lw=1.2, amp=0.08, closed=True, passes=1, z=6.3)
    wob(ax, cam.P(top), lw=0.8, amp=0.06, closed=True, passes=1, z=6.4)


def controls3(ax, cam, frame, items):
    """items: (x, s, kind) with kind knob / tab / sw / tap / lights."""
    o, eu, ev, en = frame
    items = sorted(items, key=lambda t: -cam.depth(o + eu*t[0] + ev*t[1]))
    for x, s_, k in items:
        p = o + eu*x + ev*s_
        if k == "knob": knob3d(ax, cam, p, eu, ev, en, r=6.5, h=8)
        elif k == "tab": tab3(ax, cam, o, eu, ev, en, x, s_)
        elif k == "sw": knob3d(ax, cam, p, eu, ev, en, r=3.0, h=5, tick=False)
        elif k == "tap":
            knob3d(ax, cam, p, eu, ev, en, r=5.0, h=3, tick=False)
            wob(ax, cam.P(plane_circle(p, eu, ev, 7.5)), lw=0.8, color=SOFT, closed=True, passes=1,
                amp=0.05, z=6.1)
        elif k == "lights":
            for dx in (-4.5, 4.5):
                pc = cam.P(plane_circle(p + eu*dx, eu, ev, 1.8, n=12))
                ax.fill(pc[:, 0], pc[:, 1], color=INK, zorder=6.5)


def grille3(ax, cam, frame, x, s_, w, h):
    o, eu, ev, en = frame
    c = o + eu*x + ev*s_
    pts = rounded([(-w/2, -h/2), (w/2, -h/2), (w/2, h/2), (-w/2, h/2)], [h/2.6]*4, per=6)[0]
    wob(ax, cam.P(np.array([c + eu*a + ev*b for a, b in pts])), lw=1.1, closed=True, passes=1,
        amp=0.1, z=5.7)
    n = int(w // 6)
    for i in range(n):
        a = -w/2 + 6 + i*(w - 12)/(n - 1)
        hh = h/2 - 6
        wob(ax, cam.P(np.array([c + eu*a - ev*hh, c + eu*a + ev*hh])), lw=0.9, passes=1, amp=0.05,
            over=0, z=5.7)


def field3(ax, cam, frame, s0, s1, inset=14):
    o, eu, ev, en = frame
    q = np.array([o + eu*inset + ev*s0, o + eu*(W-inset) + ev*s0, o + eu*(W-inset) + ev*s1,
                  o + eu*inset + ev*s1])
    wob(ax, cam.P(q), lw=1.0, color=SOFT, closed=True, passes=1, amp=0.2, z=5.6)


def end_rings3(ax, cam, M, center, radii=(12, 24)):
    cap = M.R[-1]; xc = cap[0, 0]
    for arc in rings_2d(center, cap[:, 1:], list(radii)):
        wob(ax, cam.P(np.column_stack([np.full(len(arc), xc), arc])), lw=0.8, color=SOFT, amp=0.15,
            passes=1, over=0, z=5.6)
    return xc


def pocket3(ax, cam, xc, y, z, w=27, h=14):
    pk = rounded([(y-w/2, z-h/2), (y+w/2, z-h/2), (y+w/2, z+h/2), (y-w/2, z+h/2)], [3]*4, per=5)[0]
    wob(ax, cam.P(np.column_stack([np.full(len(pk), xc), pk])), lw=1.1, closed=True, passes=1,
        amp=0.05, z=5.7)
    for dy, r in ((-9, 2.2), (0, 3.5), (9, 2.2)):
        c = plane_circle(np.array([xc, y+dy, z]), np.array([0, 1, 0]), np.array([0, 0, 1]), r, n=14)
        wob(ax, cam.P(c), lw=0.9, closed=True, passes=1, amp=0.04, z=5.8)


def U_(ox, oz):
    return lambda p: np.column_stack([ox - np.asarray(p)[:, 0], oz + np.asarray(p)[:, 1]])


def end_common(ax, sec, ox=0, oz=0, kb=True, ground=(-140, 230), rings=None):
    U = U_(ox, oz)
    if rings:
        for arc in rings_2d(rings, sec, [12, 24, 38]):
            wob(ax, U(arc), lw=0.9, color=SOFT, amp=0.2, passes=1, over=0)
    wob(ax, U(sec), lw=2.4, closed=True)
    wob(ax, [(ox + ground[0], oz), (ox + ground[1], oz)], lw=1.2, color=SOFT, passes=1, amp=0.15)
    if kb:
        kq = np.array([(-6, 0), (-96, 0), (-96, 16), (-6, 16)])
        wob(ax, U(kq), lw=1.2, color=SOFT, closed=True, passes=1, amp=0.15)
    return U


def stubs(ax, U, o2, ev2, ss, hh=11, ww=12):
    o2 = np.array(o2); ev2 = np.array(ev2); en2 = np.array([-ev2[1], ev2[0]])
    for s_ in ss:
        b = o2 + ev2*s_
        q = np.array([b - ev2*ww/2, b - ev2*ww/2 + en2*hh, b + ev2*ww/2 + en2*hh, b + ev2*ww/2])
        wob(ax, U(q), lw=1.5, passes=1, amp=0.12, over=0)


# ------------------------------------------------------------------ TRIANGLE (b): right, 45°, 91 × 91
TB = 91.0
TRI_RAD = [3, 4, 6]
TRI_ROWS = (51.0, 68.0)          # s along the plate (z ≈ 36 / 48)
TRI_TAP_S = 97.6                 # z ≈ 69
TRI_LEFT = [21.3 + i*19.6 for i in range(5)]
TRI_RIGHT = [W - x for x in TRI_LEFT][::-1]


def tri_section():
    return rounded([(0, 0), (TB, 0), (TB, TB)], TRI_RAD, per=10)


def tri_mesh():
    sec, m = tri_section()
    return Mesh(sec, 0, W, r_plan=17.5, r_roll=3, mids=[m[0], m[1]], soft_mids=[m[2]]), sec


def tri_items():
    it = []
    top = ["knob"]*5
    low = ["knob", "tab", "tab", "tab", "sw"]
    for xs, kinds in ((TRI_LEFT, top), (TRI_RIGHT, top[::-1])):
        for x, k in zip(xs, kinds): it.append((x, TRI_ROWS[1], k))
    for xs, kinds in ((TRI_LEFT, low), (TRI_RIGHT, low[::-1])):
        for x, k in zip(xs, kinds): it.append((x, TRI_ROWS[0], k))
    it += [(W/2, TRI_TAP_S, "tap"), (W/2 - 14, TRI_TAP_S, "lights"), (W/2 + 14, TRI_TAP_S, "lights")]
    return it


def tri_34(ax, cam, kb=True):
    M, sec = tri_mesh(); draw_mesh(ax, cam, M)
    fr = plate3((0, 0), (S45, S45))
    field3(ax, cam, fr, 30, 112)
    grille3(ax, cam, fr, W/2, 59.5, 56, 52)
    controls3(ax, cam, fr, tri_items())
    xc = end_rings3(ax, cam, M, (61, 30))
    pocket3(ax, cam, xc, 62, 20)
    if kb: draw_keyboard(ax, cam, W/2 - 165, KB_Y0)


def tri_end(ax, ox=0, oz=0, labels=True, kb=True, inset=True):
    sec, _ = tri_section()
    U = end_common(ax, sec, ox, oz, kb, rings=(61, 30))
    stubs(ax, U, (0, 0), (S45, S45), TRI_ROWS)
    stubs(ax, U, (0, 0), (S45, S45), [TRI_TAP_S], hh=4, ww=9)
    # grille zone (dashed, red) behind the plate
    g0, g1 = 33, 86
    q = np.array([(g0*S45, g0*S45), (g1*S45, g1*S45), (g1*S45 + 20, g1*S45 - 20), (g0*S45 + 20, g0*S45 - 20)])
    wob(ax, U(q), lw=1.0, color=RED, closed=True, passes=1, dashed=True, amp=0.1)
    pk = rounded([(48.5, 13), (75.5, 13), (75.5, 27), (48.5, 27)], [3]*4, per=5)[0]
    wob(ax, U(pk), lw=1.3, closed=True, passes=1, amp=0.05)
    for jy in (8, 14, 20):  # jacks, low on the vertical back (seen edge-on)
        pass
    if inset:   # (a) equilateral 108 × 94, small and dashed, at 0.45 scale
        k = 0.45; ix, iz = ox + 122, oz + 24
        a, _ = rounded([(0, 0), (108, 0), (54, 94)], [3, 3, 6], per=8)
        wob(ax, np.column_stack([ix - k*a[:, 0], iz + k*a[:, 1]]), lw=1.1, color=SOFT, closed=True,
            passes=1, dashed=True, amp=0.1)
        label(ax, ix - 24, iz + 46, "(a) equilateral, 108 × 94", size=10.5, color=SOFT, ha="center", va="bottom")
    if labels:
        aa = np.radians(np.linspace(180, 135, 12))
        wob(ax, U(np.column_stack([18*np.cos(aa) + 18, 18*np.sin(aa)]) * np.array([1, 1]) - np.array([18, 0])
                  + np.array([0, 0])) if False else
            U(np.column_stack([16*np.cos(np.radians(np.linspace(0, 45, 12))),
                               16*np.sin(np.radians(np.linspace(0, 45, 12)))])),
            lw=1.0, color=SOFT, passes=1, amp=0.05, over=0)
        label(ax, ox - 24, oz + 7, "45°", size=12, color=SOFT)
        wob(ax, U(np.array([(TB - 7, 0), (TB - 7, 7), (TB, 7)])), lw=1.0, color=SOFT, passes=1, amp=0.05, over=0)
        label(ax, ox - TB + 10, oz + 12, "90°", size=10.5, color=SOFT, ha="right")
        wob(ax, [(ox - TB, oz - 12), (ox, oz - 12)], lw=1.0, passes=1, amp=0.1, over=0)
        label(ax, ox - TB/2, oz - 22, "≈ 91 deep", ha="center", size=13)
        label(ax, ox - TB - 8, oz + 50, "≈ 91\ntall", size=13, ha="right")
        leader(ax, (ox + 30, oz + 92), U(np.array([(62*S45 - 4, 62*S45 + 4)]))[0])
        label(ax, ox + 33, oz + 94, "one grille in the plate:\n5 | grille | 5 per row", size=12, color=RED)
        leader(ax, (ox + 30, oz + 116), U(np.array([(TRI_TAP_S*S45 - 2, TRI_TAP_S*S45 + 4)]))[0])
        label(ax, ox + 33, oz + 118, "TAP + lights on the axis", size=12)
        leader(ax, (ox - 62, oz + 112), U(np.array([(70, 22)]))[0])
        label(ax, ox - 62, oz + 114, "power / TUNE / SPLIT pocket", size=12, ha="center", va="bottom")


# ------------------------------------------------------------------ SILL (round 2, D 105, bar 17.5)
SD, ST_ = 105.0, 35.0
SIL_TH = math.asin(17.5/100.0)        # ≈ 10.1°
CS, SS = math.cos(SIL_TH), math.sin(SIL_TH)


def rot(p, c=CS, s=SS):
    p = np.asarray(p, float)
    return np.column_stack([p[:, 0]*c - p[:, 1]*s, p[:, 0]*s + p[:, 1]*c])


def sill_section(tilt=True):
    pts = [(0, 0), (SD, 0), (SD, ST_), (0, ST_)]
    sec, m = rounded(pts, [3, 3, 8, 8], per=8)
    return (rot(sec) if tilt else sec), m


def sill_bar_section():
    # bar under the back, from the table to the tilted slab's underside, at y ≈ 92–100 (body frame)
    y0, y1 = 90.0, 98.0
    z0 = y0*SS; z1 = y1*SS
    yy0 = y0*CS; yy1 = y1*CS
    return rounded([(yy0, 0), (yy1, 0), (yy1, z1), (yy0, z0)], [1.5, 1.5, 0.01, 0.01], per=3)


def sill_meshes():
    sec, m = sill_section()
    S = Mesh(sec, 0, W, r_plan=17.5, r_roll=3, mids=[m[0], m[1]], soft_mids=[m[2], m[3]])
    bsec, bm = sill_bar_section()
    B = Mesh(bsec, 22, W - 44, r_plan=3, r_roll=1.5, mids=[bm[0], bm[1]])
    return S, B


def sill_frame():
    o2 = rot(np.array([[0, ST_]]))[0]
    return plate3(o2, (CS, SS))


def sill_items():
    it = []
    for t in (22, 42):
        for i in range(10):
            it.append((30 + i*24 + (4 if i > 4 else 0) - 2, t, "knob"))
    for x in (30, 44, 58): it.append((x, 72, "sw"))
    return it


def sill_34(ax, cam, kb=True):
    S, B = sill_meshes()
    draw_mesh(ax, cam, B, lw=1.6, z=3)
    draw_mesh(ax, cam, S, z=4)
    fr = sill_frame()
    field3(ax, cam, fr, 6, 99)
    o, eu, ev, en = fr
    gc = o + eu*243 + ev*72
    wob(ax, cam.P(plane_circle(gc, eu, ev, 21, n=40)), lw=1.1, closed=True, passes=1, amp=0.15, z=5.7)
    for i in range(-3, 4):
        x = i*5.5; hh = math.sqrt(max(21**2 - x**2, 0)) - 5
        wob(ax, cam.P(np.array([gc + eu*x - ev*hh, gc + eu*x + ev*hh])), lw=0.9, passes=1, amp=0.05,
            over=0, z=5.7)
    controls3(ax, cam, fr, sill_items())
    end_rings3(ax, cam, S, tuple(rot(np.array([[52, 17]]))[0]))
    if kb: draw_keyboard(ax, cam, W/2 - 165, KB_Y0)


def sill_end(ax, ox=0, oz=0, labels=True, kb=True):
    sec, _ = sill_section()
    U = end_common(ax, sec, ox, oz, kb, rings=tuple(rot(np.array([[52, 17]]))[0]))
    flat, _ = sill_section(tilt=False)
    wob(ax, U(flat), lw=0.9, color=SOFT, closed=True, passes=1, dashed=True, amp=0.1)
    bsec, _ = sill_bar_section()
    wob(ax, U(bsec), lw=1.8, closed=True, passes=1, amp=0.08)
    o2 = rot(np.array([[0, ST_]]))[0]
    stubs(ax, U, o2, (CS, SS), (22, 42))
    if labels:
        label(ax, ox - 52, oz + 66, "≈ 10° on its flip-down bar", size=12, ha="center")
        label(ax, ox - 52, oz - 22, "flat (dashed) or ≈ 10°", size=12, ha="center", color=SOFT)


# ------------------------------------------------------------------ HULL (killed): two facets 9.5° apart
HH = 10.0                      # hull depth under the slab
HR = 52.0                      # ridge, mid-slab
HPH = math.radians(9.5)


def hull_body_pts():
    zf = HR*math.tan(HPH)          # front facet rises toward the front; rear facet is the flat one
    return [(0, zf), (HR, 0), (SD, 0), (SD, HH + ST_), (0, HH + ST_)]


def hull_section(angled=True):
    pts = np.array(hull_body_pts(), float)
    sec, m = rounded([tuple(p) for p in pts], [3, 2, 3, 8, 8], per=8)
    if angled:   # roll forward onto the front facet about the ridge: the back rises
        c, s = math.cos(HPH), math.sin(HPH)
        sec = sec - [HR, 0]
        sec = np.column_stack([sec[:, 0]*c - sec[:, 1]*s, sec[:, 0]*s + sec[:, 1]*c]) + [HR, 0]
        sec[:, 1] -= sec[:, 1].min()
    return sec, m


def hull_xform(p, angled=True):
    p = np.asarray(p, float)
    if not angled: return p
    c, s = math.cos(HPH), math.sin(HPH)
    q = p - [HR, 0]
    q = np.column_stack([q[:, 0]*c - q[:, 1]*s, q[:, 0]*s + q[:, 1]*c]) + [HR, 0]
    raw = np.array(hull_body_pts(), float) - [HR, 0]
    raw = np.column_stack([raw[:, 0]*c - raw[:, 1]*s, raw[:, 0]*s + raw[:, 1]*c]) + [HR, 0]
    q[:, 1] -= raw[:, 1].min()
    return q


def hull_frame(angled=True):
    a = hull_xform([[0, HH + ST_], [SD, HH + ST_]], angled)
    d = a[1] - a[0]; d /= np.linalg.norm(d)
    return plate3(a[0], d)


def hull_34(ax, cam, kb=True, angled=True):
    sec, m = hull_section(angled)
    M = Mesh(sec, 0, W, r_plan=17.5, r_roll=3, mids=[m[0], m[1], m[2]], soft_mids=[m[3], m[4]])
    draw_mesh(ax, cam, M)
    fr = hull_frame(angled)
    field3(ax, cam, fr, 6, 99)
    # the glaze line: shell split above the hull
    gl = hull_xform([[0, HH], [SD, HH]], angled)
    o, eu, ev, en = fr
    for x0 in (W - 0.1,):
        pass
    gc = o + eu*243 + ev*72
    wob(ax, cam.P(plane_circle(gc, eu, ev, 21, n=40)), lw=1.1, closed=True, passes=1, amp=0.15, z=5.7)
    for i in range(-3, 4):
        x = i*5.5; hh = math.sqrt(max(21**2 - x**2, 0)) - 5
        wob(ax, cam.P(np.array([gc + eu*x - ev*hh, gc + eu*x + ev*hh])), lw=0.9, passes=1, amp=0.05,
            over=0, z=5.7)
    controls3(ax, cam, fr, sill_items())
    if kb: draw_keyboard(ax, cam, W/2 - 165, KB_Y0)


def hull_end(ax, ox=0, oz=0, labels=True, kb=True, angled=True, ghost=True):
    sec, _ = hull_section(angled)
    U = end_common(ax, sec, ox, oz, kb)
    if ghost:
        other, _ = hull_section(not angled)
        wob(ax, U(other), lw=0.9, color=SOFT, closed=True, passes=1, dashed=True, amp=0.1)
    gl = hull_xform([[2, HH], [SD - 2, HH]], angled)
    wob(ax, U(gl), lw=1.0, color=SOFT, passes=1, amp=0.08, over=0)
    a = hull_xform([[0, HH + ST_]], angled)[0]
    b = hull_xform([[SD, HH + ST_]], angled)[0]
    d = (b - a)/np.linalg.norm(b - a)
    stubs(ax, U, a, d, (22, 42))
    ridge = hull_xform([[HR, 0]], angled)[0]
    ax.plot(*U([ridge])[0], "^", ms=8, color=RED, zorder=8)
    if labels:
        lo = hull_xform([[22 if not angled else 88, HH + ST_]], angled)[0]
        wob(ax, U(np.array([lo + [0, 22], lo + [0, 13]])), lw=2.0, color=RED, passes=1, amp=0.03, over=0)
        ax.annotate("", xy=tuple(U([lo + [0, 11]])[0]), xytext=tuple(U([lo + [0, 14]])[0]),
                    arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.8), zorder=9)
        txt = ("a press behind the ridge\n(≈ 0.6 N) rocks it back flat" if angled else
               "a lower-row press (≈ 0.6 N)\nrocks it onto the angle")
        label(ax, ox - 52, oz + 80, txt, size=12, color=RED, ha="center", va="bottom")
        label(ax, ox - 52, oz - 22, "ridge ▲", size=11.5, color=SOFT, ha="center")


# ------------------------------------------------------------------ EASEL (rev 2.4, from r2_sketch)
def easel_end(ax, ox=0, oz=0, labels=False, kb=True):
    pts, d, h = r2.easel_section()
    sec, _ = rounded(pts, [3, 4, r2.EA_TOP_R, 4], per=10)
    U = end_common(ax, sec, ox, oz, kb, rings=(34, 31))
    drv = np.array([(12, 6), (67, 6), (67, 30), (12, 30)])
    wob(ax, U(drv), lw=1.0, color=RED, closed=True, passes=1, dashed=True, amp=0.12)
    for zz in (19.5, 25, 30.5):
        wob(ax, U(np.array([(4, zz), (-6, zz)])), lw=1.0, color=RED, passes=1, amp=0.1, over=0)
    pk = r2._pocket_2d()
    wob(ax, U(pk), lw=1.3, closed=True, passes=1, amp=0.05)
    stubs(ax, U, (0, r2.EA_F), (r2.C60, r2.S60), (14, 31))


def easel_34(ax, cam, kb=True):
    r2.easel_34(ax, cam, kb=kb)


# ------------------------------------------------------------------ sheets
END_FRAME = (-120, 128, -30, 128)          # u (before flip), z


def bounds34():
    pts = []
    M, _ = r2.easel_mesh(); pts.append(M.R.reshape(-1, 3))
    M, _ = tri_mesh(); pts.append(M.R.reshape(-1, 3))
    S, B = sill_meshes(); pts.append(S.R.reshape(-1, 3))
    sec, _ = hull_section(True); pts.append(Mesh(sec, 0, W).R.reshape(-1, 3))
    pts.append(kb_mesh(W/2 - 165, KB_Y0).R.reshape(-1, 3))
    P = CAM.P(np.vstack(pts))
    return P[:, 0].min() - 6, P[:, 0].max() + 6, P[:, 1].min() - 6, P[:, 1].max() + 10


B34 = bounds34()

COLS = [
    ("EASEL", "rev 2.4", easel_end, easel_34,
     "280 × 79 × 81 · 60° · steep and narrow, mirrored face, no grille;\n"
     "slots in the front face; slides ≈ 5 N on an end flick", False),
    ("SILL", "round 2", sill_end, sill_34,
     "280 × 105 × 35 · flat or ≈ 10° · calm, the flattest pack;\n"
     "a flip-down bar (one moving part); not distinctive", False),
    ("TRIANGLE", "(b) right, 45°", lambda ax, **k: tri_end(ax, labels=False, **k), tri_34,
     "280 × 91 × 91 · 45° · a true triangle; grille in the plate;\n"
     "bigger than EASEL; TAP tips at ≈ 7 N", False),
    ("HULL", "killed", lambda ax, **k: hull_end(ax, labels=False, **k), hull_34,
     "killed because: two facets 9.5° apart rock at ≈ 0.3–1.8 N;\n"
     "a lower-row press flips it; holding a pose needs a detent", True),
]


def director_text():
    p = os.path.join(HERE, "r3_director.json")
    d = json.load(open(p)) if os.path.exists(p) else {}
    return d


def compare(path):
    D = director_text()
    fig = plt.figure(figsize=(14, 25), dpi=110, facecolor=PAPER)
    fig.text(0.04, 0.988, "floss: round 3, four ways it can sit (sketches, same scale)", fontsize=27,
             weight="bold", color=INK, va="top")
    fig.text(0.04, 0.972, "seen from the right end and from front-right · the keyboard pushed up to the front in each",
             fontsize=15, color=SOFT, va="top")
    cw, ch = 0.47, 0.475
    for i, (nm, sub, ef, isf, trade, killed) in enumerate(COLS):
        cx = 0.025 + (i % 2)*0.49; cy = 0.955 - (i//2)*0.48   # top of the cell
        fig.text(cx + 0.01, cy, nm, fontsize=24, weight="bold", color=RED if killed else INK, va="top")
        fig.text(cx + 0.01 + 0.0195*len(nm) + 0.015, cy - 0.003, sub, fontsize=15, color=RED if killed else SOFT,
                 va="top")
        a1 = fig.add_axes([cx, cy - 0.16, cw, 0.14]); setup(a1, -120, 128, -30, 112, flip=r2.FLIP)
        ef(a1)
        a2 = fig.add_axes([cx, cy - 0.31, cw, 0.155]); setup(a2, *B34)
        isf(a2, CAM)
        if killed:
            a2.text(0.5, 0.55, "KILLED", transform=a2.transAxes, fontsize=46, color=RED, alpha=0.28,
                    ha="center", va="center", rotation=12, weight="bold", zorder=20)
        fig.text(cx + 0.01, cy - 0.318, trade, fontsize=13.5, color=INK, va="top", linespacing=1.35)
        # director block
        bx, by, bw, bh = cx + 0.005, cy - 0.465, cw - 0.01, 0.1
        fig.patches.append(plt.Rectangle((bx, by), bw, bh, transform=fig.transFigure, fill=False,
                                         ec=SOFT, lw=1.2, ls=(0, (4, 3))))
        t = D.get(nm, ["[pending]", "[pending]", "[pending]"])
        lines = [("Director's score", t[0]), ("Opinion", t[1]), ("What I'd change", t[2])]
        yy = by + bh - 0.008
        for k, v in lines:
            fig.text(bx + 0.008, yy, f"{k}: ", fontsize=13, weight="bold", color=INK, va="top")
            import textwrap
            fig.text(bx + 0.008, yy - 0.0105, "\n".join(textwrap.wrap(v, 78)) or v, fontsize=12,
                     color=INK if v != "[pending]" else SOFT, va="top", linespacing=1.2)
            yy -= 0.031
    # one scale bar
    a = fig.axes[0]
    wob(a, [(70, -22), (120, -22)], lw=1.4, passes=1, amp=0.05, over=0)
    label(a, 95, -15, "50 mm", size=11, color=SOFT, ha="center")
    fig.savefig(path, facecolor=PAPER); plt.close(fig)


def single(path, title, sub, end_fn, iso_fn, trade, killed=False, extra_end=None):
    fig = plt.figure(figsize=(9, 12.6), dpi=170, facecolor=PAPER)
    fig.text(0.05, 0.977, title, fontsize=26, weight="bold", color=RED if killed else INK, va="top")
    fig.text(0.05, 0.947, sub, fontsize=13.5, color=SOFT, va="top")
    if extra_end:
        a0 = fig.add_axes([0.03, 0.66, 0.46, 0.25]); setup(a0, -120, 30, -30, 128, flip=r2.FLIP)
        extra_end[0](a0)
        a0.text(0.5, 0.98, extra_end[1], transform=a0.transAxes, fontsize=12, color=SOFT, ha="center", va="top")
        a1 = fig.add_axes([0.51, 0.66, 0.46, 0.25]); setup(a1, -120, 30, -30, 128, flip=r2.FLIP)
        end_fn(a1)
        a1.text(0.5, 0.98, "angled, on the front facet", transform=a1.transAxes, fontsize=12, color=SOFT, ha="center", va="top")
    else:
        a1 = fig.add_axes([0.03, 0.58, 0.94, 0.34]); setup(a1, *END_FRAME, flip=r2.FLIP)
        end_fn(a1)
        wob(a1, [(60, -22), (110, -22)], lw=1.4, passes=1, amp=0.05, over=0)
        label(a1, 85, -15, "50 mm", size=10.5, color=SOFT, ha="center")
    a2 = fig.add_axes([0.03, 0.14, 0.94, 0.44]); setup(a2, *B34)
    iso_fn(a2, CAM)
    a2.text(0.01, 0.99, "3/4, keyboard pushed up to the front", transform=a2.transAxes, fontsize=12,
            color=SOFT, va="top")
    if killed:
        a2.text(0.5, 0.55, "KILLED", transform=a2.transAxes, fontsize=70, color=RED, alpha=0.25,
                ha="center", va="center", rotation=12, weight="bold", zorder=20)
    fig.text(0.05, 0.12, trade, fontsize=13.5, color=RED if killed else INK, va="top", linespacing=1.4)
    fig.savefig(path, facecolor=PAPER); plt.close(fig)


if __name__ == "__main__":
    base = os.path.join(HERE, "..")
    os.makedirs(os.path.join(base, "r3-triangle"), exist_ok=True)
    os.makedirs(os.path.join(base, "r3-hull"), exist_ok=True)
    single(os.path.join(base, "r3-triangle", "sketch.png"), "TRIANGLE (b)",
           "sketch · 280 × 91 × 91 mm · right triangle, plate 45° · end view from the right end",
           tri_end, tri_34,
           "Trade: a true triangle from the end (his ask). The grille sits in the plate, 5 | grille | 5,\n"
           "TAP + lights on the axis. Bigger than EASEL (91 × 91 vs 79 × 81); TAP tips it at ≈ 7 N;\n"
           "width is tight (257 of 260). Inset: (a) equilateral, 108 × 94, the alternative.")
    single(os.path.join(base, "r3-hull", "sketch.png"), "HULL: killed",
           "sketch · SILL-sized slab on a hull, two facets 9.5° apart",
           lambda ax: hull_end(ax, angled=True, ghost=False), hull_34,
           "Killed because: the centre of mass has only a ≈ 3–5 mm window over\n"
           "the ridge, so it rocks between poses at ≈ 0.3–1.8 N: an ordinary knob\n"
           "press flips it. Holding a pose would need a click-stop or magnet (a\n"
           "detent), which the rule kills. What survives: the glaze line.",
           killed=True,
           extra_end=(lambda ax: hull_end(ax, angled=False, ghost=False, labels=True, kb=False), "flat, on the rear facet"))
    compare(os.path.join(base, "r3-sketches.png"))
    print("ok")
