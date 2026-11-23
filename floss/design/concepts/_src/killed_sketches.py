"""Line sketches of the ideas killed in discussion before anyone drew them.

Owner: "Draw all those ones rejected before the draw" (sketches, not renders).
Drawn as described in floss/design/jam-cathedral.md (and r2-handle/how-it-works.md),
not improved. Rough sizes from the records; idea level. Same visual language as
r2_sketch.py (its line helpers are reused).

End views: front (player side) on the LEFT, seen from an end. All end views share one scale.

Run from this folder:  python3 killed_sketches.py
Writes ../killed-sketches.png (round 1) and ../killed-sketches-2.png (round 1-2)
"""
import math
import os
import textwrap
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from r2_sketch import (PAPER, INK, SOFT, RED, wob, rounded, Mesh, Cam, draw_mesh,
                       plane_circle, knob3d)

CAM = Cam(-34, 24)
W = 280.0
EV = (-30, 360, -26, 150)          # end-view frame (mm): one scale for every idea


# ------------------------------------------------------------------ helpers
def rot(pts, deg, about=(0, 0)):
    a = math.radians(deg); c, s = math.cos(a), math.sin(a)
    p = np.asarray(pts, float) - about
    return np.column_stack([c*p[:, 0] - s*p[:, 1], s*p[:, 0] + c*p[:, 1]]) + about


def sh(pts, dx=0, dz=0):
    return np.asarray(pts, float) + (dx, dz)


def soft(pts, r=4, per=6):
    return rounded(pts, [r]*len(pts), per=per)[0]


def ground(ax, x0, x1, z=0):
    wob(ax, [(x0, z), (x1, z)], lw=1.2, color=SOFT, passes=1, amp=0.15)


def knobs_on(ax, a, b, ts=(0.25, 0.5), h=9, w=11):
    """Knob stubs standing on the face from a to b (a = front edge), at fractions ts."""
    a = np.asarray(a, float); b = np.asarray(b, float)
    ev = (b - a) / np.linalg.norm(b - a); en = np.array([-ev[1], ev[0]])
    for t in ts:
        c = a + (b - a)*t
        q = np.array([c - ev*w/2, c - ev*w/2 + en*h, c + ev*w/2 + en*h, c + ev*w/2])
        wob(ax, q, lw=1.4, passes=1, amp=0.1, over=0)


def note(ax, x, y, s, size=12, color=SOFT, ha="center", va="center"):
    ax.text(x, y, s, fontsize=size, color=color, ha=ha, va=va, zorder=10, linespacing=1.05)


def arc_mark(ax, c, r, a0, a1, color=SOFT):
    aa = np.radians(np.linspace(a0, a1, 14))
    wob(ax, np.column_stack([c[0] + r*np.cos(aa), c[1] + r*np.sin(aa)]), lw=1.0, color=color,
        passes=1, amp=0.06, over=0)


def setup(ax, xl, xr, zb, zt):
    ax.set_xlim(xl, xr); ax.set_ylim(zb, zt); ax.set_aspect("equal"); ax.axis("off")


# ------------------------------------------------------------------ WEDGE
# r1 §4.1: 105 deep, 35 front -> ~61 back (14°); pose 2 stood on its back face (~76°).
WG = [(0, 0), (105, 0), (105, 61), (0, 35)]


def wedge_end(ax):
    p = soft(WG, 4)
    wob(ax, p, lw=2.4, closed=True)
    knobs_on(ax, WG[3], WG[2], (0.25, 0.55))
    arc_mark(ax, WG[3], 26, 0, 14); note(ax, 40, 26, "14°")
    note(ax, 52, -14, "≈ 105 deep", color=INK)
    note(ax, 116, 61, "61", ha="left", color=INK); note(ax, -6, 35, "35", ha="right", color=INK)
    # pose 2: stood on its back face
    q = rot(WG, 90, (105, 0)); q = sh(q, 240 - q[:, 0].min(), -q[:, 1].min())
    wob(ax, soft(q, 4), lw=2.4, closed=True)
    knobs_on(ax, q[3], q[2], (0.25, 0.55))
    note(ax, 280, 128, "pose 2: on its back,\npanel ≈ 76°")
    ground(ax, -20, 350)


def wedge_34(ax):
    M = Mesh(rounded(WG, [3, 3, 4, 4], per=6)[0], 0, W, r_plan=17.5, r_roll=3)
    draw_mesh(ax, CAM, M)
    a = np.array([0, 0, 35.0]); ev = np.array([0, 105, 26.0]); ev /= np.linalg.norm(ev)
    en = np.cross([1, 0, 0], ev)
    ks = [(x, s) for s in (28, 58) for x in np.linspace(35, 245, 9)]
    ks.sort(key=lambda t: -CAM.depth(a + [t[0], 0, 0] + ev*t[1]))
    for x, s in ks:
        knob3d(ax, CAM, a + [x, 0, 0] + ev*s, np.array([1., 0, 0]), ev, en, r=6, h=8)


# ------------------------------------------------------------------ TRIPTYCH
# r1 §4.2 cover hinged along the back edge; r2 base 2: hinged at the rear base edge, folds under.
SL_D, SL_T, CV = 105.0, 35.0, 5.0


def slab(ax, x0, z0, D=SL_D, T=SL_T, knobs=True, lw=2.4):
    p = [(x0, z0), (x0 + D, z0), (x0 + D, z0 + T), (x0, z0 + T)]
    wob(ax, soft(p, 5), lw=lw, closed=True)
    if knobs: knobs_on(ax, p[3], p[2], (0.25, 0.55), h=8)
    return p


def triptych_end(ax):
    # 1 closed: cover over the plate (over the knob tops), hinge at the back
    slab(ax, 0, 0, knobs=False)
    cov = [(0, SL_T + 2), (SL_D, SL_T + 2), (SL_D, SL_T + 2 + CV), (0, SL_T + 2 + CV)]
    wob(ax, soft(cov, 2), lw=1.8, closed=True)
    ax.plot(SL_D, SL_T + 2, "o", ms=6, mfc=PAPER, mec=INK, zorder=8)
    note(ax, 52, 66, "closed:\ncover over the panel")
    # 2 flat: cover folded under
    x2 = 125
    wob(ax, soft([(x2, 0), (x2 + SL_D, 0), (x2 + SL_D, CV), (x2, CV)], 2), lw=1.8, closed=True)
    slab(ax, x2, CV)
    ax.plot(x2 + SL_D, CV, "o", ms=6, mfc=PAPER, mec=INK, zorder=8)
    note(ax, x2 + 52, 66, "flat:\ncover folded under")
    # 3 angled: cover propped as a triangle under the back
    x3 = 250; th = 9.0
    s = rot([(0, 0), (SL_D, 0), (SL_D, SL_T), (0, SL_T)], th, (0, 0)); s = sh(s, x3)
    wob(ax, soft(s, 5), lw=2.4, closed=True); knobs_on(ax, s[3], s[2], (0.25, 0.55), h=8)
    hb = s[1]
    tri = np.array([hb, (hb[0] - 62, 0), (hb[0] + 2, 0)])
    wob(ax, tri, lw=1.8, closed=True, amp=0.2)
    ax.plot(*hb, "o", ms=6, mfc=PAPER, mec=INK, zorder=8)
    note(ax, x3 + 52, 66, "angled: cover\nas a triangle")
    note(ax, 175, 104, "o = hinge", size=11)
    ground(ax, -20, 360)


# ------------------------------------------------------------------ BAIL
# r1 §4.3: U printed-metal bail pivoting at the two ends: up = handle, down behind = 14° stay,
# folded flat against the back = 0°.
def bail_end(ax):
    # flat, bail folded flat against the back; handle-up shown dashed
    slab(ax, 0, 0)
    pv = np.array([SL_D - 14, SL_T/2])
    L = 70
    ax.plot(*pv, "o", ms=6, mfc=PAPER, mec=INK, zorder=8)
    wob(ax, [pv, pv + (L, 0)], lw=3.0, color=INK, passes=1, amp=0.1)
    wob(ax, [pv, pv + rot([(L, 0)], 100)[0]], lw=2.0, color=SOFT, passes=1, dashed=True, amp=0.1)
    note(ax, 72, 108, "up: carry handle", size=11.5)
    note(ax, 150, -12, "0°: folded flat\nagainst the back", size=11.5, va="top")
    # angled 14°: bail swung down behind as the stay
    x3 = 215; th = 14.0
    s = sh(rot([(0, 0), (SL_D, 0), (SL_D, SL_T), (0, SL_T)], th, (0, 0)), x3)
    wob(ax, soft(s, 5), lw=2.4, closed=True); knobs_on(ax, s[3], s[2], (0.25, 0.55), h=8)
    p2 = sh(rot([pv], th, (0, 0)), x3)[0]
    foot = np.array([p2[0] + math.sqrt(max(L**2 - p2[1]**2, 0)), 0])
    ax.plot(*p2, "o", ms=6, mfc=PAPER, mec=INK, zorder=8)
    wob(ax, [p2, foot], lw=3.0, passes=1, amp=0.1)
    arc_mark(ax, (x3, 0), 30, 0, 14); note(ax, x3 - 10, 18, "14°", size=11.5, ha="right")
    note(ax, x3 + 70, 108, "down behind: the stay\n(printed detent)", size=11.5)
    ground(ax, -20, 360)


def bail_34(ax):
    p = soft([(0, 0), (SL_D, 0), (SL_D, SL_T), (0, SL_T)], 5)
    M = Mesh(p, 0, W, r_plan=17.5, r_roll=3)
    draw_mesh(ax, CAM, M)
    a = np.array([0, 0, SL_T]); ex, ey, ez = np.eye(3)
    ks = [(x, s) for s in (26, 58) for x in np.linspace(35, 245, 9)]
    ks.sort(key=lambda t: -CAM.depth(a + ex*t[0] + ey*t[1]))
    for x, s in ks:
        knob3d(ax, CAM, a + ex*x + ey*s, ex, ey, ez, r=6, h=8)
    # the bail, swung up: pivots on each end, a U over the top
    y, z0, r = SL_D - 14, SL_T/2, 70
    U = [(-4, y, z0), (-4, y - 8, z0 + r), (W + 4, y - 8, z0 + r), (W + 4, y, z0)]
    U = np.array([[-4, y, z0], [-4, y - 6, z0 + r - 10], [6, y - 8, z0 + r], [W - 6, y - 8, z0 + r],
                  [W + 4, y - 6, z0 + r - 10], [W + 4, y, z0]])
    wob(ax, CAM.P(U), lw=3.0, amp=0.2, z=9)
    for X in (U[0], U[-1]):
        ax.plot(*CAM.P(X), "o", ms=6, mfc=PAPER, mec=INK, zorder=10)


# ------------------------------------------------------------------ SLED
# r1 §4.4: module = flat slab; printed sled holds the keyboard by its ends, raised seat behind.
def sled_end(ax):
    # sled base with keyboard (held at the ends, so seen in section here), seat behind
    KB_D, KB_T = 90, 16
    sled = [(0, 0), (KB_D + 150, 0), (KB_D + 150, 30), (KB_D + 20, 4), (0, 4)]
    wob(ax, np.array(sled), lw=1.8, closed=True, amp=0.2)
    wob(ax, soft([(4, 4), (4 + KB_D, 4), (4 + KB_D, 4 + KB_T), (4, 4 + KB_T)], 2), lw=1.3,
        color=SOFT, closed=True)
    note(ax, 4 + KB_D/2, 4 + KB_T + 12, "keyboard", size=11.5)
    th = math.degrees(math.atan2(26, 130))
    s = sh(rot([(0, 0), (SL_D, 0), (SL_D, 28), (0, 28)], th, (0, 0)), KB_D + 22, 4)
    wob(ax, soft(s, 5), lw=2.4, closed=True); knobs_on(ax, s[3], s[2], (0.25, 0.55), h=8)
    note(ax, 180, 92, "module dropped on\nthe sled's seat: angled")
    note(ax, 120, -13, "the sled (printed), holds the keyboard by its ends", size=11.5, va="top")
    # without the sled: flat slab
    x4 = 270
    slab(ax, x4, 0, D=SL_D - 20, T=28)
    note(ax, x4 + 42, 74, "no sled:\nflat")
    ground(ax, -20, 360)


# ------------------------------------------------------------------ RETABLE
# r1 §4.5: stands on a thick foot, panel ≈ 60–75°, like a tabletop radio; on its back = 0°.
def retable_sec(th=70.0, foot=30.0, D=105.0, T=35.0):
    s = rot([(0, 0), (D, 0), (D, T), (0, T)], th, (0, 0))
    s = sh(s, -s[:, 0].min() + 6, foot)
    return s


def retable_end(ax):
    x0 = 20
    s = sh(retable_sec(), x0)
    ft = soft([(x0 - 4, 0), (x0 + 58, 0), (x0 + 58, 30), (x0 - 4, 30)], 4)
    wob(ax, ft, lw=2.4, closed=True)
    wob(ax, soft(s, 5), lw=2.4, closed=True)
    # panel face = the side toward the player (left)
    a, b = s[3], s[2]
    if a[0] > s[0][0]: pass
    face = (s[0], s[3]) if s[0][0] < s[1][0] else (s[1], s[2])
    knobs_on(ax, s[3], s[2], (0.3, 0.65), h=8)
    arc_mark(ax, (s[0][0], 30), 24, 0, 70); note(ax, s[0][0] + 34, 50, "≈ 70°", size=11.5)
    note(ax, x0 + 26, 15, "foot", size=11.5)
    note(ax, x0 + 150, 120, "knobs turned from\nthe front, like a radio")
    # lying on its back: 0°, packs that way
    x4 = 210
    slab(ax, x4, 0)
    wob(ax, soft([(x4 + SL_D, 0), (x4 + SL_D + 30, 0), (x4 + SL_D + 30, SL_T), (x4 + SL_D, SL_T)], 4),
        lw=2.0, closed=True)
    note(ax, x4 + 68, 74, "on its back: 0°\n(packs this way)")
    ground(ax, -20, 360)


def retable_34(ax):
    s = retable_sec()
    foot = soft([(-4, 0), (58, 0), (58, 30), (-4, 30)], 4)
    draw_mesh(ax, CAM, Mesh(foot, 0, W, r_plan=17.5, r_roll=3), z=3)
    draw_mesh(ax, CAM, Mesh(soft(s, 5), 0, W, r_plan=17.5, r_roll=3), z=4)
    # knobs on the steep long face toward the player (s[3] -> s[2])
    o = np.array([0, *s[3]]); ev = np.array([0, *(s[2] - s[3])]); ev /= np.linalg.norm(ev)
    en = np.array([0, -ev[2], ev[1]]); ex = np.array([1., 0, 0])
    ks = [(x, t) for t in (30, 65) for x in np.linspace(35, 245, 9)]
    ks.sort(key=lambda q: -CAM.depth(o + ex*q[0] + ev*q[1]))
    for x, t in ks:
        knob3d(ax, CAM, o + ex*x + ev*t, ex, ev, en, r=6, h=8)


# ------------------------------------------------------------------ ROSE
# turn 2 §5: round plan Ø ≈ 190, every control on one 300° arc (7 -> 5 o'clock), one lancet
# window (speaker) in the centre, standing on a smaller brass foot ring cut at an angle (≈ 12°).
R_ROSE = 95.0


def rose_end(ax):
    th = 12.0
    c = (115, 0)
    disc = rot([(-R_ROSE, 14), (R_ROSE, 14), (R_ROSE, 34), (-R_ROSE, 34)], th, (0, 14))
    disc = sh(disc, c[0])
    ring_l, ring_r = c[0] - 45, c[0] + 45
    zl = 14 + math.tan(math.radians(th))*(-45); zr = 14 + math.tan(math.radians(th))*45
    ring = np.array([(ring_l, 0), (ring_r, 0), (ring_r, zr + 2), (ring_l, zl + 2)])
    wob(ax, ring, lw=1.8, closed=True, amp=0.15)
    wob(ax, soft(disc, 6), lw=2.4, closed=True)
    knobs_on(ax, disc[3], disc[2], (0.12, 0.88), h=8)
    note(ax, c[0], -12, "brass foot ring, cut at an angle", size=11.5, va="top")
    note(ax, c[0] - 70, 80, "a Ø 190 disc,\ntilted ≈ 12°", size=11.5)


def rose_plan(ax):
    cx, cy = 0, 0
    wob(ax, plane_circle(np.array([cx, cy, 0.]), np.array([1, 0, 0]), np.array([0, 1, 0]), R_ROSE, 72)[:, :2],
        lw=2.4, closed=True)
    # 300° arc of controls, 7 o'clock -> 5 o'clock clockwise (depth, the red hero, at 12)
    n = 15
    for i in range(n):
        ang = math.radians(240 - i*300/(n - 1))   # 7 o'clock = 240°, 5 o'clock = -60°
        x, y = 70*math.cos(ang), 70*math.sin(ang)
        col = RED if i == n//2 else INK
        wob(ax, plane_circle(np.array([x, y, 0.]), np.array([1, 0, 0]), np.array([0, 1, 0]),
                             8 if i == n//2 else 6.5, 18)[:, :2], lw=1.4, color=col, closed=True, passes=1, amp=0.05)
    # central lancet window: vertical slots whose lengths follow a circle
    for k in range(-3, 4):
        x = k*7; hh = math.sqrt(max(32**2 - x**2, 0)) - 4
        wob(ax, [(x, -hh), (x, hh)], lw=1.3, passes=1, amp=0.06, over=0)
    wob(ax, plane_circle(np.array([0, 0, 0.]), np.array([1, 0, 0]), np.array([0, 1, 0]), 36, 48)[:, :2],
        lw=1.0, color=SOFT, closed=True, passes=1, amp=0.1)
    note(ax, 0, -100, "host port in the 6 o'clock gap", size=10.5, va="top")
    note(ax, -118, 100, "plan", size=11.5, ha="left")


# ------------------------------------------------------------------ TURNING CHEEKS
# r2 base 3: GNOMON's two end caps turn half a turn, linked through the slab;
# one way flat, the other way a lobe lifts the back.
TC_D, TC_T = 115.0, 35.0


def cheek_cap(cx, cz, lobe_down):
    """End cap outline: the slab's rounded end with a cam lobe near the back."""
    base = [(0, 0), (TC_D, 0), (TC_D, TC_T), (0, TC_T)]
    return sh(soft(base, 12, per=8), cx, cz)


def cheeks_end(ax):
    # flat: lobe turned up, inside the outline
    slab(ax, 0, 0, D=TC_D, T=TC_T)
    lobe = np.array([TC_D - 22, TC_T/2])
    wob(ax, plane_circle(np.array([*lobe, 0.]), np.array([1, 0, 0]), np.array([0, 1, 0]), 14, 30)[:, :2] + (0, 3),
        lw=1.8, closed=True, passes=1, amp=0.08)
    ax.plot(*lobe, "+", ms=9, mew=1.6, color=INK, zorder=9)
    note(ax, 58, 70, "flat: cap turned\none way")
    # angled: turned half a turn, the lobe pushes the back up
    x3 = 200; e = 9.0; th = math.degrees(math.asin(2*e/(TC_D - 22)))
    s = sh(rot([(0, 0), (TC_D, 0), (TC_D, TC_T), (0, TC_T)], th, (0, 0)), x3)
    wob(ax, soft(s, 5), lw=2.4, closed=True); knobs_on(ax, s[3], s[2], (0.25, 0.55), h=8)
    lc = sh(rot([lobe], th, (0, 0)), x3)[0]
    wob(ax, plane_circle(np.array([lc[0], lc[1] - 3, 0.]), np.array([1, 0, 0]), np.array([0, 1, 0]), 14, 30)[:, :2]
        - (0, 2*e - 6), lw=1.8, closed=True, passes=1, amp=0.08)
    ax.plot(*lc, "+", ms=9, mew=1.6, color=INK, zorder=9)
    note(ax, x3 + 60, 80, "turned half a turn:\na lobe lifts the back")
    note(ax, 120, 118, "both ends linked through the slab:\nturn one, both move", size=11)
    ground(ax, -20, 360)


# ------------------------------------------------------------------ HANDLE
# r2 turn 3/4: U bail flush in a groove round the base's rear and ends, pivoting near the front
# of each end; flush = flat, swung down past the base = props the back (≈ 9°), up = carry handle.
def handle_end(ax):
    slab(ax, 0, 0, D=TC_D, T=TC_T)
    pv = np.array([14, 6]); L = 100
    wob(ax, [pv, pv + (L, 0)], lw=3.0, passes=1, amp=0.08)
    ax.plot(*pv, "o", ms=6, mfc=PAPER, mec=INK, zorder=8)
    wob(ax, [pv, pv + rot([(L, 0)], 82)[0]], lw=2.0, color=SOFT, passes=1, dashed=True, amp=0.1)
    note(ax, 70, 118, "up: carry handle", size=11.5)
    note(ax, 58, -12, "flush in a groove: flat", size=11.5, va="top")
    # angled: bail swung down past the base, ≈ 14° below it, back propped ≈ 9°
    x3 = 215; th = 9.0
    s = sh(rot([(0, 0), (TC_D, 0), (TC_D, TC_T), (0, TC_T)], th, (0, 0)), x3)
    wob(ax, soft(s, 5), lw=2.4, closed=True); knobs_on(ax, s[3], s[2], (0.25, 0.55), h=8)
    p2 = sh(rot([pv], th, (0, 0)), x3)[0]
    foot = p2 + rot([(L, 0)], th - 14)[0]
    foot[1] = max(foot[1], 0)
    ax.plot(*p2, "o", ms=6, mfc=PAPER, mec=INK, zorder=8)
    wob(ax, [p2, (foot[0], 0)], lw=3.0, passes=1, amp=0.1)
    arc_mark(ax, (x3, 0), 30, 0, 9); note(ax, x3 - 8, 16, "≈ 9°", size=11.5, ha="right")
    note(ax, x3 + 64, 88, "swung down past\nthe base: props the back", size=11.5)
    ground(ax, -20, 360)


def handle_34(ax):
    p = soft([(0, 0), (TC_D, 0), (TC_D, TC_T), (0, TC_T)], 5)
    M = Mesh(p, 0, W, r_plan=17.5, r_roll=3)
    draw_mesh(ax, CAM, M)
    a = np.array([0, 0, TC_T]); ex, ey, ez = np.eye(3)
    ks = [(x, s) for s in (28, 62) for x in np.linspace(35, 245, 9)]
    ks.sort(key=lambda t: -CAM.depth(a + ex*t[0] + ey*t[1]))
    for x, s in ks:
        knob3d(ax, CAM, a + ex*x + ey*s, ex, ey, ez, r=6, h=8)
    # flush groove line round the rear and ends, low on the body
    g = np.array([[-0.2, 14, 6], [-0.2, TC_D - 12, 6]])
    gr = np.array([[W + 0.2, 14, 6], [W + 0.2, TC_D - 12, 6]])
    wob(ax, CAM.P(gr), lw=1.2, color=SOFT, passes=1, amp=0.05, over=0, z=6)
    # the U swung up as a handle from the front pivots
    U = np.array([[W + 4, 14, 6], [W + 6, 20, 90], [W - 6, 24, 100], [6, 24, 100], [-6, 20, 90], [-4, 14, 6]])
    wob(ax, CAM.P(U), lw=3.0, amp=0.2, z=9)
    for X in (U[0], U[-1]):
        ax.plot(*CAM.P(X), "o", ms=6, mfc=PAPER, mec=INK, zorder=10)


# ------------------------------------------------------------------ the sheet
IDEAS = {
    "WEDGE": dict(
        what="Round 1. The angle is the body: a fixed wedge (14°), the tall back is the speaker box. "
             "No hinge, no leg. Second pose: stood on its back.",
        kill="anonymous: a trapezoid end face is the silhouette every desktop synth already has, "
             "and shape lost the last round. Merged into DROP and GNOMON. (Visual designer; director confirmed.)",
        end=wedge_end, iso=wedge_34),
    "TRIPTYCH": dict(
        what="Rounds 1 and 2. The cover is the stand: one hinged cover closes over the panel, "
             "folds under for flat, or props as a triangle for the angle.",
        kill="one hinge can't both close over the top and fold flat underneath; it needs two hinges "
             "plus a catch: three parts and three states for one job. (Systems, round 2; director accepted. "
             "Round 1 it had been folded into CASKET as one line.)",
        end=triptych_end, iso=None),
    "BAIL": dict(
        what="Round 1. A printed-metal U handle pivoting at the ends: up = carry handle, "
             "down behind = the stay (14°), folded flat = 0°. Also the keyboard anchor.",
        kill="a part hanging off the body, YOKE's mistake again; a swinging loop reads as a radio or "
             "a cooking pot; printed metal wearing on printed metal at the detent. "
             "(Visual designer; director confirmed.)",
        end=bail_end, iso=bail_34),
    "SLED": dict(
        what="Round 1. The module is a dumb flat slab; the angle lives in the keyboard's printed carrier, "
             "which has a raised seat behind the keys.",
        kill="alone the module has no stance, and forget the sled and you have no angle. "
             "Its idea was merged into CASKET (the lid as the sled you can't forget). "
             "(Visual designer; director confirmed.)",
        end=sled_end, iso=None),
    "RETABLE": dict(
        what="Round 1. Stand it up: on a thick foot with the panel at ≈ 60–75°, like a tabletop radio. "
             "Lying on its back = 0°.",
        kill="knobs on a steep face read as a radio front, poor under the hands on a lap, and it was the "
             "biggest costume risk (a church front). Kept only as DROP's 2nd pose, later cut. "
             "(Visual designer; director confirmed.)",
        end=retable_end, iso=retable_34),
    "ROSE": dict(
        what="Round 1. A round plan: every control on one 300° arc around a central speaker window, "
             "the disc tilted on a brass foot ring.",
        kill="he'd said \"Cathedral\" and had just rejected an arched plan, so a circle repeats that risk; "
             "no end to hold when carried; scaling to Big Energy's ≈ 40 controls unsolved. (Director.)",
        end=rose_end, iso=rose_plan),
    "TURNING CHEEKS": dict(
        what="Round 2. GNOMON's two end caps turn half a turn as cams, linked through the slab: "
             "one way flat, the other way a lobe lifts the back.",
        kill="turning a whole end cap gives no lift (same outline), so it needs an eccentric that reads "
             "as a knob, plus a 280 mm rod through the speaker box. Not simple. "
             "(Systems; director accepted.)",
        end=cheeks_end, iso=None),
    "HANDLE": dict(
        what="Round 2. BAIL revived, made flush: a U bail in a groove round the rear and ends. "
             "Flush = flat; swung down = props the back; swung up = carry handle.",
        kill="neither simple nor distinctive: the ≈ 9° prop is a shallow lever that needs sprung toothed "
             "hubs and a release, carry and stand want different pivots, and at rest it looks like SILL. "
             "(Systems, on the director's condition.)",
        end=handle_end, iso=handle_34),
}


def cell(fig, x0, y0, w, h, name, d):
    """One idea in a cell (figure fractions; y0 = bottom)."""
    WRAP = 50
    fig.text(x0 + 0.012, y0 + h - 0.004, name, fontsize=27, weight="bold", color=INK, va="top")
    fig.text(x0 + 0.012, y0 + h - 0.033, textwrap.fill(d["what"], WRAP), fontsize=14.5, color=INK,
             va="top", linespacing=1.3)
    kill = textwrap.fill("Killed because: " + d["kill"], WRAP)
    fig.text(x0 + 0.012, y0 + 0.006, kill, fontsize=14.5, color=RED, va="bottom", linespacing=1.3)
    top = y0 + h - 0.105; bot = y0 + 0.088
    if d["iso"] is None:
        a1 = fig.add_axes([x0, bot + 0.02, w, top - bot - 0.02]); setup(a1, *EV)
        d["end"](a1)
    else:
        split = bot + (top - bot)*0.42
        a1 = fig.add_axes([x0, split, w, top - split]); setup(a1, *EV)
        d["end"](a1)
        a2 = fig.add_axes([x0 + w*0.12, bot, w*0.76, split - bot])
        if d["iso"] is rose_plan:
            setup(a2, -130, 130, -118, 112)
        else:
            a2.axis("off"); a2.set_aspect("equal")
        d["iso"](a2)
        if d["iso"] is not rose_plan:
            a2.autoscale_view(); a2.margins(0.04)
            a2.text(0.0, 1.0, "3/4", transform=a2.transAxes, fontsize=12, color=SOFT, va="top")


def sheet(names, title, sub, path):
    fig = plt.figure(figsize=(13, 18), dpi=130, facecolor=PAPER)
    fig.text(0.03, 0.993, title, fontsize=28, weight="bold", color=INK, va="top")
    fig.text(0.03, 0.974, sub, fontsize=13, color=SOFT, va="top", linespacing=1.25)
    cw, ch = 0.47, 0.455
    for i, nm in enumerate(names):
        r, c = divmod(i, 2)
        x0 = 0.025 + c*(cw + 0.03); y0 = 0.49 - r*(ch + 0.012)
        cell(fig, x0, y0, cw, ch, nm, IDEAS[nm])
    # light divider lines
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off"); ax.patch.set_alpha(0)
    ax.plot([0.5, 0.5], [0.02, 0.945], color="#d8d0c3", lw=1.2)
    ax.plot([0.03, 0.97], [0.484, 0.484], color="#d8d0c3", lw=1.2)
    # scale bar (end views share one scale)
    fig.savefig(path, facecolor=PAPER); plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "..")
    sub = ("ideas killed in discussion before anyone drew them · sketched as described, not improved\n"
           "end views: player on the left, all at one scale · 3/4 views not to scale")
    sheet(["WEDGE", "TRIPTYCH", "BAIL", "SLED"], "floss: killed before the draw (1 of 2)", sub,
          os.path.join(out, "killed-sketches.png"))
    sheet(["RETABLE", "ROSE", "TURNING CHEEKS", "HANDLE"], "floss: killed before the draw (2 of 2)", sub,
          os.path.join(out, "killed-sketches-2.png"))
    print("ok")
