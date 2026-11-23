# floss round 2 (flat or slightly angled): CRADLE and PLINTH sheets, and the one comparison sheet with SILL.
# Visual, 2026-11-22. Reuses cathedral_sheets.py's renderer, palette and scales so the family of sheets matches
# (end views 3:2, 3/4 views 1:2 on the concept sheets; the comparison sheet uses one scale per row for all three).
# Geometry from systems' r2-cradle/how-it-works.md and r2-plinth/how-it-works.md ([calc], nothing measured).
# Run from this folder: python3 r2_sheets.py  -> ../r2-cradle/sheet.png, ../r2-plinth/sheet.png, ../r2-compare.png
import math, textwrap
import cathedral_sheets as cs
from cathedral_sheets import (WAL, WALD, CREAM, BLACK, RED, TPU, KBC, BG, GREY, INK, MM, LBL, SML, TTL,
                              Cam, Scene, add_face, add_line, extrude, box, plate_frame, knob, lancet_window,
                              keyboard, KB_W, KB_D, KB_H, fillet_radii, offset_edges, squircle_delta, roll_delta,
                              ccw, area, heading, scale_bar, leader, save)
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Rectangle

W, T, D = 280.0, 35.0, 105.0     # director 2026-11-22: all slabs D 105 with one driver
RPLAN, ROLL, RPLATE = T/2, 3.0, 10.0
PLC = (0.25, 0.155, 0.095)      # PLINTH: the base in the darker brown (visual's call; the shadow it floats on)
SHD = (0.07, 0.05, 0.04)        # shadow gap
HIDE = (0.20, 0.12, 0.06)
KB_GAP = [60.0]                 # keyboard's distance in front of the module in the 3/4 views

# ---------------- shared slab ----------------
SLAB_Q = [(0, 0), (D, 0), (D, T), (0, T)]
SLAB_R = [3, 3, 6, 8]            # front-bottom, rear-bottom, rear-top, front-top (SILL / GNOMON rev 5)
PORT0 = (78.0, 17.5)
JK_END = [(32 + i*9, 17.5, k) for i, k in enumerate(["j", "j", "j", "j", "usb"])]

def section(quad, rad, d, rplan=RPLAN, roll=ROLL):
    pl = squircle_delta(d, rplan) if rplan > 0 else 0.0
    rl = roll_delta(d, roll) if roll > 0 else 0.0
    return fillet_radii(offset_edges(quad, [rl, pl+rl, rl, pl+rl]), rad, n=8)

def rot(th, about=(0.0, 0.0), shift=(0.0, 0.0)):
    c, s = math.cos(th), math.sin(th)
    def f(p):
        y, z = p[0]-about[0], p[1]-about[1]
        return (about[0] + y*c - z*s + shift[0], about[1] + y*s + z*c + shift[1])
    return f
IDENT = lambda p: (p[0], p[1])

def sweep(L, cam, quad, rad, x0, x1, ends, tf, col, rplan=RPLAN, roll=ROLL, cap0=None, cap1=None, secf=None):
    xs = {x0, x1}
    if ends != "none":
        for dd in [0, 0.4, 1.0, 1.8, 3.0, 4.5, 6.5, 9.0, 12.0, 15.0, rplan]:
            if ends in ("both", "left") and x0+dd <= x1: xs.add(x0+dd)
            if ends in ("both", "right") and x1-dd >= x0: xs.add(x1-dd)
    xs = sorted(xs)
    def dist(x):
        if ends == "both": return min(x-x0, x1-x)
        if ends == "left": return x-x0
        if ends == "right": return x1-x
        return 1e9
    secf = secf or (lambda d: section(quad, rad, d, rplan, roll))
    secs = [ccw([tf(p) for p in secf(dist(x))]) for x in xs]
    mid = secs[len(secs)//2]
    cy = sum(v[0] for v in mid)/len(mid); cz = sum(v[1] for v in mid)/len(mid); cx = (x0+x1)/2
    for k in range(len(xs)-1):
        A, B = secs[k], secs[k+1]; m = len(A)
        for i in range(m):
            P0 = (xs[k], *A[i]); P1 = (xs[k], *A[(i+1) % m]); P2 = (xs[k+1], *B[(i+1) % m]); P3 = (xs[k+1], *B[i])
            u_ = [P2[j]-P0[j] for j in range(3)]; v_ = [P3[j]-P1[j] for j in range(3)]
            nn = (u_[1]*v_[2]-u_[2]*v_[1], u_[2]*v_[0]-u_[0]*v_[2], u_[0]*v_[1]-u_[1]*v_[0])
            ln = math.sqrt(sum(c*c for c in nn)) or 1; nn = tuple(c/ln for c in nn)
            qc = [(P0[j]+P1[j]+P2[j]+P3[j])/4 for j in range(3)]
            out = (qc[1]-cy)*nn[1] + (qc[2]-cz)*nn[2] + ((qc[0]-cx)*nn[0] if abs(nn[0]) > 0.7 else 0)
            if out < 0: nn = tuple(-c for c in nn)
            add_face(L, cam, [P0, P1, P2, P3], nn, col)
    add_face(L, cam, [(xs[0], y, z) for y, z in secs[0][::-1]], (-1.0, 0.0, 0.0), col, extra=cap0)
    add_face(L, cam, [(xs[-1], y, z) for y, z in secs[-1]], (1.0, 0.0, 0.0), col, extra=cap1)
    return secs[0], secs[-1]

def ring_lines(ax, cam, x, centre, patch, r0=12.5, rmax=170, step=6.0, lw=0.5):
    r = r0
    while r < rmax:
        pts = [cam.p((x, centre[0]+r*math.cos(t), centre[1]+r*math.sin(t))) for t in [2*math.pi*k/120 for k in range(121)]]
        ax.plot([q[0] for q in pts], [q[1] for q in pts], color=WALD, lw=lw, clip_path=patch)
        r += step*(1 + 0.035*(r/10))

def disc(ax, cam, x, c, r, fc, N=40):
    pts = [cam.p((x, c[0]+r*math.cos(t), c[1]+r*math.sin(t))) for t in [2*math.pi*k/N for k in range(N)]]
    ax.add_patch(Polygon(pts, closed=True, fc=fc, ec="none"))

def cap_port(x, tf):
    def extra(ax, cam, patch):
        port = tf(PORT0)
        ring_lines(ax, cam, x, port, patch)
        disc(ax, cam, x, port, 8, (0.10, 0.07, 0.05))
        pts = [cam.p((x, port[0]+10.5*math.cos(t), port[1]+10.5*math.sin(t))) for t in [2*math.pi*k/60 for k in range(61)]]
        ax.plot([q[0] for q in pts], [q[1] for q in pts], color=HIDE, lw=0.9)
    return extra
def cap_jacks(x, tf):
    def extra(ax, cam, patch):
        ring_lines(ax, cam, x, tf(PORT0), patch)
        for y, z, k in JK_END:
            yy, zz = tf((y, z))
            if k == "j": disc(ax, cam, x+0.3, (yy, zz), 3.2, (0.09, 0.08, 0.07), N=24)
            else:
                pts = [cam.p((x+0.3, yy+dy, zz+dz)) for dy, dz in ((-4.5, -2), (4.5, -2), (4.5, 2), (-4.5, 2))]
                ax.add_patch(Polygon(pts, closed=True, fc=(0.09, 0.08, 0.07), ec="none"))
    return extra

def squircle_field(L, cam, P, n, s0, s1, t0, t1, r, lift=0.3, N=10):
    pts = []
    for (c0, c1), a0 in [((s1-r, t1-r), 0), ((s0+r, t1-r), 90), ((s0+r, t0+r), 180), ((s1-r, t0+r), 270)]:
        for k in range(N+1):
            t = math.radians(a0 + 90*k/N); c, s_ = math.cos(t), math.sin(t)
            pts.append(P(c0 + r*abs(c)**0.4*(1 if c >= 0 else -1), c1 + r*abs(s_)**0.4*(1 if s_ >= 0 else -1), lift))
    add_face(L, cam, pts, n, CREAM, ec=(0.80, 0.76, 0.69))

def dress(sc, cam, tf, th, xoff=0.0):
    """the plate: cream field, two lancet grilles, split rail, two knob rows (DEPTH red), three small controls."""
    P0, n = plate_frame(tf((0, T)), th, W)
    P = lambda x, t, h=0.0: P0(x+xoff, t, h)
    L2 = sc.layer(); squircle_field(L2, cam, P, n, 8, W-8, 9, D-8, RPLATE)
    L3 = sc.layer()
    # owner 2026-11-22: one speaker. One grille at the output end (right), in the rear band behind the knob rows,
    # centred on the last knob column so it lines up with the grid (visual's proposal).
    lancet_window(L3, cam, P, n, GRILLE_X, ROW_G, R=GR_R, lw=1.3)
    add_line(L3, cam, [P(40, 4.6, 0.4), P(W-40, 4.6, 0.4)], CREAM, 0.8)
    for i in range(21):
        sx = 40 + i*(W-80)/20
        add_line(L3, cam, [P(sx, 3.4, 0.4), P(sx, 5.8, 0.4)], CREAM, 0.8 if i % 5 else 1.4)
    L4 = sc.layer()
    for i in range(10): knob(L4, cam, P, n, 24 + i*(W-48)/9, ROW1)
    for i in range(9): knob(L4, cam, P, n, 24 + (i+0.5)*(W-48)/9, ROW2, col=RED if i == 4 else BLACK)
    # power, TUNE, split move to the rear band's left end: the start of the chain (power first), mirroring the grille
    for x, col, d, h in SMALLS:
        knob(L4, cam, P, n, x, ROW_G, col=col, d=d, h=h)

ROW1, ROW2, ROW_G, GR_R = 22.0, 42.0, 72.0, 21.0   # D 105: rows pulled forward; grille field Ø 42 (was Ø 46)
GRILLE_X = 24 + 8.5*(W-48)/9          # ≈ 243: over the last half-step column, 37 from the right end
SMALLS = [(30, (0.62, 0.62, 0.60), 4.5, 6), (44, BLACK, 7, 5), (58, (0.62, 0.62, 0.60), 4.5, 6)]

# ======================= SILL (as its sheet; h = T/2, D 105) =======================
SI_H, SI_BAR = T/2, 3.5
SI_TH = math.asin(SI_H/(D-5))
def sill_bar(th):
    hx, hz = rot(th)((D-2.5, 0.0))
    return [(hx-SI_BAR/2, hz), (hx+SI_BAR/2, hz), (hx+SI_BAR/2+0.8, 0.0), (hx-SI_BAR/2+0.8, 0.0)]
def build_sill(sc, cam, tilted=False, kb_front=False, packed=False):
    th = SI_TH if tilted else 0.0; tf = rot(th)
    if packed: keyboard(sc, cam, W/2-KB_W/2, 12, z0=-KB_H, keys_up=False)
    if tilted:
        Lb = sc.layer(); extrude(Lb, cam, sill_bar(th), 22, W-22, (0.36, 0.23, 0.14), ec=WALD)
    L = sc.layer(); sweep(L, cam, SLAB_Q, SLAB_R, 0, W, "both", tf, WAL, cap0=cap_port(0, tf), cap1=cap_jacks(W, tf))
    dress(sc, cam, tf, th)
    if kb_front: keyboard(sc, cam, W/2-KB_W/2, -KB_D-KB_GAP[0])

# ======================= CRADLE =======================
CR_CHK, CR_GAP = 12.0, 1.0
CR_X0 = CR_CHK + CR_GAP                       # slab x 13..293, overall 306
CR_WT = W + 2*(CR_CHK + CR_GAP)
CR_PIN = (8.0, 8.0); CR_SLIDE = 5.0
CR_SEAT = T/2
CR_RAIL = (D+1.0, D+11.0, CR_SEAT-10.0, CR_SEAT)
CR_SLAB_R = [8, 3, 6, 8]                       # front-bottom = the r 8 arc on the pin
def _cr_theta():
    lo, hi = 0.0, 0.4
    a = D - CR_PIN[0]; b = CR_PIN[1]
    for _ in range(60):
        t = (lo+hi)/2
        f = CR_PIN[1] + a*math.sin(t) - b*math.cos(t) - CR_SEAT
        lo, hi = (t, hi) if f < 0 else (lo, t)
    return (lo+hi)/2
CR_TH = _cr_theta()
CR_TF_ANG = rot(CR_TH, about=CR_PIN, shift=(CR_SLIDE, 0.0))
_lip = CR_TF_ANG((0, T))
CR_DEP = D + 12.0
def cr_top(y): return _lip[1] + (y - _lip[0])*math.tan(CR_TH)     # cheek A's top: the angled plate's line
CR_ZF, CR_ZB = cr_top(0.0), cr_top(CR_DEP)
CR_QA = [(0, 0), (CR_DEP, 0), (CR_DEP, CR_ZB), (0, CR_ZF)]
CR_QB = [(0, 0), (CR_DEP, 0), (CR_DEP, T), (0, T)]
CR_RA = [3, 3, 8, 8]
CR_PORT_REAR = (D, 27.0)                       # port mouth on the slab's rear face, above the rail (systems)
CR_JACKS = [(196 + i*14.4, k) for i, k in enumerate(["usb", "j", "j", "j", "j", "usb"])]   # front face, one row of 6

def cap_pivot(x):
    def extra(ax, cam, patch):
        ring_lines(ax, cam, x, CR_PIN, patch, r0=7.0, rmax=150, step=7.0, lw=0.55)
    return extra

def build_cradle(sc, cam, tilted=False, kb_front=False, packed=False, cheek="A", dress_on=True):
    tf = CR_TF_ANG if tilted else IDENT; th = CR_TH if tilted else 0.0
    Q = CR_QA if cheek == "A" else CR_QB
    if packed: keyboard(sc, cam, CR_WT/2-KB_W/2, 12, z0=-KB_H, keys_up=False)
    near_left = cam.c[0] < 0
    def lc(L): sweep(L, cam, Q, CR_RA, 0, CR_CHK, "left", IDENT, WAL, cap0=cap_pivot(0))
    def rc(L): sweep(L, cam, Q, CR_RA, CR_WT-CR_CHK, CR_WT, "right", IDENT, WAL, cap1=cap_pivot(CR_WT))
    Lf = sc.layer(); (rc if near_left else lc)(Lf)
    Lr = sc.layer(); box(Lr, cam, CR_CHK, CR_WT-CR_CHK, CR_RAIL[0], CR_RAIL[1], CR_RAIL[2], CR_RAIL[3], (0.36, 0.23, 0.14))
    L = sc.layer(); sweep(L, cam, SLAB_Q, CR_SLAB_R, CR_X0, CR_X0+W, "none", tf, WAL, rplan=0, roll=0)
    # front-face jacks and rear port mouth (on the slab), drawn as their own layer
    Lj = sc.layer()
    c, s = math.cos(th), math.sin(th)
    nf = (0.0, -c, -s)                      # the slab's front-face normal
    for x, k in CR_JACKS:
        X = CR_X0 + x; yy, zz = tf((0.0, 17.5))
        if k == "j":
            pts = [(X + 3.0*math.cos(a), yy - 0.3*c + 3.0*math.sin(a)*(-s), zz + 3.0*math.sin(a)*c) for a in [2*math.pi*q/20 for q in range(20)]]
        else:
            pts = [(X+dx, yy - 0.3*c - dz*s, zz + dz*c) for dx, dz in ((-4.5, -1.8), (4.5, -1.8), (4.5, 1.8), (-4.5, 1.8))]
        add_face(Lj, cam, pts, nf, (0.09, 0.08, 0.07), bias=60)
    nr = (0.0, c, s)
    py, pz = tf(CR_PORT_REAR)
    for xm in (W*0.18,):
        X = CR_X0 + xm
        pts = [(X + 7.0*math.cos(a), py + 0.3*c - 7.0*math.sin(a)*s, pz + 7.0*math.sin(a)*c) for a in [2*math.pi*q/30 for q in range(30)]]
        add_face(Lj, cam, pts, nr, (0.09, 0.07, 0.05), bias=60)
    if dress_on: dress(sc, cam, tf, th, xoff=CR_X0)
    Ln = sc.layer(); (lc if near_left else rc)(Ln)
    if kb_front: keyboard(sc, cam, CR_WT/2-KB_W/2, -KB_D-KB_GAP[0])

# ======================= PLINTH =======================
PL_IN = 10.0
PL_D, PL_W = D - 2*PL_IN, W - 2*PL_IN          # 95 x 260
PL_TH = math.asin((T/2)/D)
PL_ZF = T/3
PL_ZB = PL_ZF + PL_D*math.tan(PL_TH)
PL_REB, PL_REBW = 3.0, 6.0
def pl_top(y): return PL_ZF + y*math.tan(PL_TH)
PL_Q = [(0, 0), (PL_D, 0), (PL_D, PL_ZB-PL_REB), (0, PL_ZF-PL_REB)]
PL_CORE = [(PL_REBW, 0), (PL_D-PL_REBW, 0), (PL_D-PL_REBW, pl_top(PL_D-PL_REBW)), (PL_REBW, pl_top(PL_REBW))]
PL_Y0 = PL_IN                                   # plinth front edge in world y
_c, _s = math.cos(PL_TH), math.sin(PL_TH)
PL_MOD0 = (PL_Y0 - PL_IN*_c, PL_ZF - PL_IN*_s)  # module's front-bottom corner on the plinth's top line, extended
PL_TF = rot(PL_TH, shift=PL_MOD0)
def pl_shift(q): return [(y+PL_Y0, z) for y, z in q]

def build_plinth_base(sc, cam, drawer_out=0.0, tongue=False, core=SHD):
    near_left = cam.c[0] < 0
    L = sc.layer()
    sweep(L, cam, pl_shift(PL_Q), [2, 2, 2, 2], PL_IN, W-PL_IN, "both", IDENT, PLC, rplan=RPLAN-PL_IN, roll=2.0)
    Lc = sc.layer()
    sweep(Lc, cam, pl_shift(PL_CORE), [1, 1, 1, 1], PL_IN+PL_REBW, W-PL_IN-PL_REBW, "none", IDENT, core, rplan=0, roll=0)
    if tongue:
        Lt = sc.layer(); n = (0.0, -_s, _c)
        P, n = plate_frame((PL_Y0 + PL_REBW, pl_top(PL_REBW)), PL_TH, W)
        add_face(Lt, cam, [P(W/2-100, 0, 0.6), P(W/2+100, 0, 0.6), P(W/2+100, 56, 0.6), P(W/2-100, 56, 0.6)], n, (0.33, 0.21, 0.13), ec=(0.18, 0.11, 0.07))
        add_face(Lt, cam, [P(W/2-92, 6, 1.4), P(W/2+92, 6, 1.4), P(W/2+92, 50, 1.4), P(W/2-92, 50, 1.4)], n, (0.36, 0.23, 0.14), ec=(0.18, 0.11, 0.07))
    if drawer_out > 0:
        Ld = sc.layer()
        x1 = W - PL_IN + drawer_out; x0 = W - PL_IN      # only the part out of the plinth shows
        y0, y1 = PL_Y0 + 7.5, PL_Y0 + 87.5
        q = [(y0, 1.5), (y1, 1.5), (y1, pl_top(87.5)-PL_REB-1.5), (y0, pl_top(7.5)-PL_REB-1.5)]
        # tray: floor, front and back walls, the outer end (drawer front)
        add_face(Ld, cam, [(x0, y0, 1.5), (x1, y0, 1.5), (x1, y1, 1.5), (x0, y1, 1.5)], (0, 0, 1), (0.20, 0.13, 0.08))
        for (ya, za), (yb, zb), nrm in (((y0, q[3][1]), (y0, 1.5), (0, -1, 0)), ((y1, q[2][1]), (y1, 1.5), (0, 1, 0))):
            add_face(Ld, cam, [(x0, ya, za), (x1, ya, za), (x1, yb, zb), (x0, yb, zb)], nrm, PLC)
        Lf = sc.layer()
        add_face(Lf, cam, [(x1, y, z) for y, z in [(y0-1.5, 0.5), (y1+1.5, 0.5), (y1+1.5, q[2][1]+1.0), (y0-1.5, q[3][1]+1.0)]], (1, 0, 0), PLC, ec=(0.15, 0.09, 0.05))
        add_face(Lf, cam, [(x1+0.4, y, z) for y, z in [(PL_Y0+35, 4), (PL_Y0+60, 4), (PL_Y0+60, 9), (PL_Y0+35, 9)]], (1, 0, 0), SHD)
        # contents on the floor: coiled cable, adapter, card
        Lk = sc.layer()
        cx, cy = x0 + 2, PL_Y0 + 47
        for r, col in ((27, (0.12, 0.12, 0.12)), (20, (0.20, 0.13, 0.08))):
            add_face(Lk, cam, [(cx + r*math.cos(a), cy + r*math.sin(a), 1.8 + (27-r)*0.0 + (0.3 if r == 20 else 0)) for a in [2*math.pi*k/36 for k in range(36)]], (0, 0, 1), col)
        box(Lk, cam, x0 + 34, x0 + 52, PL_Y0 + 20, PL_Y0 + 34, 1.6, 7.6, (0.62, 0.62, 0.60))
        add_face(Lk, cam, [(x0+30, PL_Y0+44, 1.9), (x0+56, PL_Y0+44, 1.9), (x0+56, PL_Y0+80, 1.9), (x0+30, PL_Y0+80, 1.9)], (0, 0, 1), CREAM, ec=(0.6, 0.58, 0.55))

def build_plinth(sc, cam, docked=True, kb_front=False, packed=False):
    if packed: keyboard(sc, cam, W/2-KB_W/2, PL_Y0+2, z0=-KB_H, keys_up=False)
    if docked:
        build_plinth_base(sc, cam)
        tf, th = PL_TF, PL_TH
    else:
        tf, th = IDENT, 0.0
    L = sc.layer(); sweep(L, cam, SLAB_Q, SLAB_R, 0, W, "both", tf, WAL, cap0=cap_port(0, tf), cap1=cap_jacks(W, tf))
    dress(sc, cam, tf, th)
    if kb_front: keyboard(sc, cam, W/2-KB_W/2, -KB_D-KB_GAP[0])

# ======================= 2D end views =======================
def slab_sil(tf, rad=SLAB_R, d=100.0, rplan=RPLAN, roll=ROLL):
    return ccw([tf(p) for p in section(SLAB_Q, rad, d, rplan, roll)])
def rings2d(ax, centre, clip, r0=12.5, rmax=180, step=6.0, lw=0.7):
    r = r0
    while r < rmax:
        ax.add_patch(Circle(centre, r, fc="none", ec=WALD, lw=lw, clip_path=clip)); r += step*(1 + 0.035*(r/10))
def shiftp(pts, dy=0.0, dz=0.0): return [(y+dy, z+dz) for y, z in pts]

def end_sill(ax, tilted, dy=0.0, dz=0.0, lw=2.0, detail=True, mover=None):
    th = SI_TH if tilted else 0.0; tf = rot(th)
    sil = slab_sil(tf); face = ccw([tf(p) for p in section(SLAB_Q, SLAB_R, 0.0)])
    z0 = min(z for y, z in sil)
    sh = lambda pts: shiftp(pts, dy, dz - z0)
    if tilted:
        ax.add_patch(Polygon([(y+dy, max(z - z0, 0) + dz) for y, z in sill_bar(th)], closed=True, fc=mover or (0.30, 0.19, 0.11), ec=WALD, lw=1.2))
    ax.add_patch(Polygon(sh(sil), closed=True, fc=(0.47, 0.31, 0.19), ec=WALD, lw=lw))
    fl = Polygon(sh(face), closed=True, fc=WAL, ec=(0.55, 0.38, 0.24), lw=1.0); ax.add_patch(fl)
    port = sh([tf(PORT0)])[0]
    if detail: rings2d(ax, port, fl)
    ax.add_patch(Circle(port, 8, fc=(0.10, 0.07, 0.05), ec="none"))
    if detail: ax.add_patch(Circle(port, 10.5, fc="none", ec=HIDE, lw=1.2))
    if not tilted:
        rec = [(D-2-SI_H, 0.2), (D-2, 0.2), (D-2, SI_BAR), (D-2-SI_H, SI_BAR)]
        ax.add_patch(Polygon(shiftp(rec, dy, dz), closed=True, fc=mover or (0.30, 0.19, 0.11), ec="none"))
    return port

def end_cradle(ax, tilted, dy=0.0, dz=0.0, lw=2.0, cheek="A", detail=True, hidden=True, mover=None, hidden_lw=1.3):
    Q = CR_QA if cheek == "A" else CR_QB
    tf = CR_TF_ANG if tilted else IDENT
    slab = ccw([tf(p) for p in section(SLAB_Q, CR_SLAB_R, 50.0, 0, 0)])
    sil = ccw(section(Q, CR_RA, 100.0)); face = ccw(section(Q, CR_RA, 0.0))
    if cheek == "B":   # the slab shows above the low cheek
        ax.add_patch(Polygon(shiftp(slab, dy, dz), closed=True, fc=(0.47, 0.31, 0.19), ec=WALD, lw=lw*0.8))
    ax.add_patch(Polygon(shiftp(sil, dy, dz), closed=True, fc=(0.47, 0.31, 0.19), ec=WALD, lw=lw))
    fl = Polygon(shiftp(face, dy, dz), closed=True, fc=WAL, ec=(0.55, 0.38, 0.24), lw=1.0); ax.add_patch(fl)
    if detail: rings2d(ax, (CR_PIN[0]+dy, CR_PIN[1]+dz), fl, r0=7.0, rmax=150, step=7.0)
    if hidden:
        hs = shiftp(slab, dy, dz) + [shiftp(slab, dy, dz)[0]]
        ax.plot([p[0] for p in hs], [p[1] for p in hs], color=CREAM if mover else HIDE, lw=hidden_lw, ls=(0, (4, 2.5)))
        r = CR_RAIL
        ax.add_patch(Rectangle((r[0]+dy, r[2]+dz), r[1]-r[0], r[3]-r[2], fc=mover or "none", ec=CREAM if mover else HIDE, lw=hidden_lw, ls=(0, (3, 2))))
        pin = tf(CR_PIN)
        ax.add_patch(Circle((pin[0]+dy, pin[1]+dz), 2.0, fc="none", ec=CREAM if mover else HIDE, lw=hidden_lw))
    return sil

def end_plinth(ax, tilted, dy=0.0, dz=0.0, lw=2.0, detail=True, mover=None):
    if not tilted:
        return end_sill_plain(ax, dy, dz, lw, detail)
    q = pl_shift(PL_Q); core = pl_shift(PL_CORE)
    pq = ccw(fillet_radii(q, [2, 2, 2, 2], n=6))
    ax.add_patch(Polygon(shiftp(ccw(core), dy, dz), closed=True, fc=SHD, ec="none"))
    ax.add_patch(Polygon(shiftp(pq, dy, dz), closed=True, fc=mover or PLC, ec=(0.15, 0.09, 0.05), lw=lw*0.8))
    tf = PL_TF
    sil = slab_sil(tf); face = ccw([tf(p) for p in section(SLAB_Q, SLAB_R, 0.0)])
    ax.add_patch(Polygon(shiftp(sil, dy, dz), closed=True, fc=(0.47, 0.31, 0.19), ec=WALD, lw=lw))
    fl = Polygon(shiftp(face, dy, dz), closed=True, fc=WAL, ec=(0.55, 0.38, 0.24), lw=1.0); ax.add_patch(fl)
    port = shiftp([tf(PORT0)], dy, dz)[0]
    if detail: rings2d(ax, port, fl)
    ax.add_patch(Circle(port, 8, fc=(0.10, 0.07, 0.05), ec="none"))
    if detail: ax.add_patch(Circle(port, 10.5, fc="none", ec=HIDE, lw=1.2))
    return port

def end_sill_plain(ax, dy, dz, lw, detail):
    sil = slab_sil(IDENT); face = ccw(section(SLAB_Q, SLAB_R, 0.0))
    ax.add_patch(Polygon(shiftp(sil, dy, dz), closed=True, fc=(0.47, 0.31, 0.19), ec=WALD, lw=lw))
    fl = Polygon(shiftp(face, dy, dz), closed=True, fc=WAL, ec=(0.55, 0.38, 0.24), lw=1.0); ax.add_patch(fl)
    port = (PORT0[0]+dy, PORT0[1]+dz)
    if detail: rings2d(ax, port, fl)
    ax.add_patch(Circle(port, 8, fc=(0.10, 0.07, 0.05), ec="none"))
    if detail: ax.add_patch(Circle(port, 10.5, fc="none", ec=HIDE, lw=1.2))
    return port

def gline(ax, x0, x1, z=0.0): ax.plot([x0, x1], [z, z], color=GREY, lw=1.2)

# ======================= sheet frame =======================
def new_sheet(h, title, dims, sub, foot):
    cs.FIG_H = h
    fig = plt.figure(figsize=(cs.FIG_W, h), dpi=cs.DPI); fig.patch.set_facecolor(BG)
    top = 1 - 0.75/h
    fig.text(0.04, top, title, fontsize=TTL, weight="bold", color=INK, va="top")
    fig.text(0.04, top - 0.85/h, dims, fontsize=LBL+4, color=INK, va="top")
    fig.text(0.04, top - 1.55/h, "\n".join(textwrap.wrap(sub, 100)), fontsize=SML, color="#555", va="top", linespacing=1.15)
    fig.text(0.04, 0.2/h, foot, fontsize=11, color=GREY)
    return fig
def axes_mm(fig, box_mm, scale, center): return cs.axes_mm(fig, box_mm, scale, center)

FOOT = ("floss · round 2, flat or slightly angled · idea level, not a render · sizes [calc] from systems' how-it-works, nothing measured · "
        "end views 3:2, 3/4 views 1:2 (as SILL)\nprinted body (walnut-brown), printed cream plate, bought knobs (black, one red), printed TPU grip strips")

# ======================= EASEL (B: footprint : height = 1 : phi) =======================
EA_TH = math.radians(60.0); EA_L = 100.0; EA_F0 = 12.0
EA_HB = EA_F0 + EA_L*math.sin(EA_TH)            # 98.6
EA_F = EA_HB/1.618                               # ~ 61
EA_APEX = (EA_L*math.cos(EA_TH), EA_HB)          # (50, 98.6)
EA_Q = [(0, 0), (EA_F, 0), (EA_F, EA_HB), EA_APEX, (0, EA_F0)]
EA_QA = [(0, 0), (EA_L*math.cos(EA_TH), 0), EA_APEX, (0, EA_F0)]   # version A: footprint 50, 30 deg apex
EA_R = [3, 3, 8, 8, 4]
EA_PORT = (32.0, 16.0)
EA_JK = [(22, 14, "j"), (32, 14, "j"), (42, 14, "j"), (27, 28, "j"), (38, 28, "usb")]
AMBER = (0.96, 0.64, 0.20)
EA_RPLAN = 8.0      # plan corners n 5, r 8: the body is only ~11 thick at the roof, so T/2 would eat the whole top
def _clip(poly, a, b, c):
    """keep the part of a convex polygon where a*y + b*z <= c."""
    out = []; m = len(poly)
    for i in range(m):
        P, Q = poly[i], poly[(i+1) % m]
        fp, fq = a*P[0]+b*P[1]-c, a*Q[0]+b*Q[1]-c
        if fp <= 0: out.append(P)
        if fp*fq < 0:
            t = fp/(fp-fq); out.append((P[0]+t*(Q[0]-P[0]), P[1]+t*(Q[1]-P[1])))
    return out
def easel_section(d, F=None, rplan=None):
    """end section at distance d from the end: plan rounding insets horizontally (back, plate, front), the roll insets every edge."""
    F = F or EA_F; rplan = EA_RPLAN if rplan is None else rplan
    p = squircle_delta(d, rplan); r = roll_delta(d, ROLL)
    s60, c60 = math.sin(EA_TH), math.cos(EA_TH)
    poly = [(-50, -50), (200, -50), (200, 200), (-50, 200)]
    poly = _clip(poly, 0, -1, -r)                         # base: z >= r
    poly = _clip(poly, 1, 0, F - p - r)                   # back: y <= F - p - r
    poly = _clip(poly, 0, 1, EA_HB - r)                   # roof: z <= HB - r
    poly = _clip(poly, -1, 0, -(p + r))                   # front: y >= p + r
    # plate line through (0, F0) at 60 deg, shifted back by p horizontally and in by r: keep the side behind it
    t60 = math.tan(EA_TH)
    poly = _clip(poly, -t60, 1, EA_F0 - t60*p - r*math.sqrt(1 + t60*t60))
    poly = ccw(poly)
    rad = []
    for y, z in poly:
        if z < r + 1: rad.append(3.0)
        elif z < EA_F0 + 6 and y < 20: rad.append(4.0)
        else: rad.append(8.0)
    return resample(fillet_radii(poly, rad, n=8))

def resample(poly, N=96):
    """same vertex count for every section (so the sweep can join them): start at the base's front end, equal arc steps."""
    poly = ccw(poly)
    k0 = min(range(len(poly)), key=lambda i: poly[i][1]*4 + poly[i][0])
    poly = poly[k0:] + poly[:k0]
    pts = poly + [poly[0]]
    seg = [math.hypot(pts[i+1][0]-pts[i][0], pts[i+1][1]-pts[i][1]) for i in range(len(poly))]
    tot = sum(seg); out = []; i = 0; acc = 0.0
    for k in range(N):
        target = tot*k/N
        while acc + seg[i] < target: acc += seg[i]; i += 1
        t = (target-acc)/seg[i] if seg[i] > 0 else 0
        out.append((pts[i][0]+t*(pts[i+1][0]-pts[i][0]), pts[i][1]+t*(pts[i+1][1]-pts[i][1])))
    return out

def ea_cap_left(ax, cam, patch):
    ring_lines(ax, cam, 0, EA_PORT, patch, r0=10.0, rmax=120)
    disc(ax, cam, 0, EA_PORT, 6.0, (0.10, 0.07, 0.05))
def ea_cap_right(ax, cam, patch):
    ring_lines(ax, cam, W, EA_PORT, patch, r0=10.0, rmax=120)
    for y, z, k in EA_JK:
        if k == "j": disc(ax, cam, W+0.3, (y, z), 3.2, (0.09, 0.08, 0.07), N=24)
        else:
            pts = [cam.p((W+0.3, y+dy, z+dz)) for dy, dz in ((-4.5, -2), (4.5, -2), (4.5, 2), (-4.5, 2))]
            ax.add_patch(Polygon(pts, closed=True, fc=(0.09, 0.08, 0.07), ec="none"))

def build_easel(sc, cam, kb_front=False, packed=False, dress_on=True):
    L = sc.layer(); sweep(L, cam, EA_Q, EA_R, 0, W, "both", IDENT, WAL, rplan=EA_RPLAN, cap0=ea_cap_left, cap1=ea_cap_right, secf=easel_section)
    Lh = sc.layer()
    add_face(Lh, cam, [(W/2+dx, -0.3, 6+dz) for dx, dz in ((-4.5, -1.8), (4.5, -1.8), (4.5, 1.8), (-4.5, 1.8))], (0, -1, 0), (0.09, 0.08, 0.07), bias=60)
    if dress_on:
        P, n = plate_frame((0.0, EA_F0), EA_TH, W)
        L2 = sc.layer(); squircle_field(L2, cam, P, n, 8, W-8, 6, EA_L-6, RPLATE)
        L3 = sc.layer(); lancet_window(L3, cam, P, n, W/2, 31, R=GR_R, lw=1.3)
        add_line(L3, cam, [P(40, 2.6, 0.4), P(W-40, 2.6, 0.4)], CREAM, 0.8)
        L4 = sc.layer()
        for i in range(5):
            for t in (13, 35): knob(L4, cam, P, n, 22 + i*21, t)
        for i in range(4):
            for t in (13, 35): knob(L4, cam, P, n, 174 + i*21, t, col=RED if (i == 0 and t == 35) else BLACK)
        for t, (col, d, h) in zip((12, 24, 36), [((0.62, 0.62, 0.60), 4.5, 6), (BLACK, 7, 5), ((0.62, 0.62, 0.60), 4.5, 6)]):
            knob(L4, cam, P, n, 258, t, col=col, d=d, h=h)
        for x in (124, 140, 156): knob(L4, cam, P, n, x, 70, col=AMBER, d=3.2, h=0.6)
    if packed:
        Lk = sc.layer(); box(Lk, cam, W/2-KB_W/2, W/2+KB_W/2, EA_F+0.5, EA_F+0.5+KB_H, 6, 6+KB_D, KBC)
    if kb_front: keyboard(sc, cam, W/2-KB_W/2, -KB_D-KB_GAP[0])

def end_easel(ax, dy=0.0, dz=0.0, lw=2.0, detail=True, ghostA=False):
    sil = ccw(easel_section(100.0)); face = ccw(easel_section(0.0))
    ax.add_patch(Polygon(shiftp(sil, dy, dz), closed=True, fc=(0.47, 0.31, 0.19), ec=WALD, lw=lw))
    fl = Polygon(shiftp(face, dy, dz), closed=True, fc=WAL, ec=(0.55, 0.38, 0.24), lw=1.0); ax.add_patch(fl)
    pc = (EA_PORT[0]+dy, EA_PORT[1]+dz)
    if detail: rings2d(ax, pc, fl, r0=10.0, rmax=130)
    ax.add_patch(Circle(pc, 6.0, fc=(0.10, 0.07, 0.05), ec="none"))
    if ghostA:
        qa = shiftp(EA_QA + [EA_QA[0]], dy, dz)
        ax.plot([p[0] for p in qa], [p[1] for p in qa], color=INK, lw=1.4, ls=(0, (5, 3)))
    return sil

def thumbs(fig, box_mm, scale=0.4):
    """the director's test: every end outline, solid, same scale."""
    heading(fig, box_mm, "7  The thumbnail test: end outlines, same scale (2:5)")
    ax = axes_mm(fig, box_mm, scale, (box_mm[2]/scale/2 - 10, box_mm[3]/scale/2 - 34))
    items = [
        ("SILL\nflat", [slab_sil(IDENT)]),
        ("SILL\ntilted", [slab_sil(rot(SI_TH)), sill_bar(SI_TH)]),
        ("CRADLE\nboth", [ccw(section(CR_QA, CR_RA, 100.0))]),
        ("PLINTH\nflat", [slab_sil(IDENT)]),
        ("PLINTH\ntilted", [ccw(fillet_radii(pl_shift(PL_Q), [2]*4, n=6)), slab_sil(PL_TF)]),
        ("EASEL\n(one pose)", [ccw(easel_section(100.0))]),
    ]
    x = 5
    for lab, polys in items:
        zmin = min(z for p in polys for _, z in p)
        for p in polys: ax.add_patch(Polygon(shiftp(p, x, -min(0, zmin)), closed=True, fc=INK))
        wid = max(y for p in polys for y, _ in p) - min(y for p in polys for y, _ in p)
        ax.text(x + wid/2, -8, lab, ha="center", va="top", fontsize=SML-3, color=INK, linespacing=1.1)
        x += max(wid, 60) + 22
    gline(ax, -5, x, 0)

def sheet_easel(path):
    fig = new_sheet(27.0, "EASEL · the lid standing on its own",
                    f"280 × {EA_F:.0f} × {EA_HB:.1f} mm · plate 60° · one pose · no moving parts",
                    "The framed plate stands at CATHEDRAL's raised-lid angle on tall soft end faces that carry the end grain. "
                    "Footprint : height = 1 : 1.618, so the top is a soft roof, not a point. Steep, as he asked: not flat or slightly angled.", FOOT)
    box_mm = (14, 395, 328, 190)
    heading(fig, box_mm, "1  End view (3:2): B, with A's sharper outline dashed")
    ax = axes_mm(fig, box_mm, 1.5, (95, 56))
    end_easel(ax, ghostA=True); gline(ax, -20, 120, 0)
    c, s_ = math.cos(EA_TH), math.sin(EA_TH)
    nrm = (-s_, c)
    def on_plate(t, off): return (t*c + off*nrm[0], EA_F0 + t*s_ + off*nrm[1])
    for (t0, t1, col, lab, ly) in ((0, 45, (0.62, 0.22, 0.15), "controls: only the lower 45 mm\n(higher, a press tips it back)", 26),
                                    (45, 100, GREY, "upper plate: lights only\n(too thin for pots)", 72)):
        p0, p1 = on_plate(t0, 7), on_plate(t1, 7)
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=col, lw=4, solid_capstyle="butt")
        mid = on_plate((t0+t1)/2, 8)
        leader(ax, mid, lab, (82, ly + 10), ha="left")
    ap = EA_APEX
    ax.annotate("", (ap[0]-26, ap[1]+6), (ap[0]+2, ap[1]+6), arrowprops=dict(arrowstyle="-|>", color=(0.62, 0.22, 0.15), lw=2))
    ax.text(ap[0]+6, ap[1]+12, "a pull of ≈ 1.5–2 N here\ntips it forward", fontsize=SML-2, color=(0.62, 0.22, 0.15), va="center")
    leader(ax, (EA_F-1, 50), f"back vertical, {EA_HB:.1f}; footprint {EA_F:.0f} (B),\nA's {EA_QA[1][0]:.0f} dashed (a sharp 30° top)", (82, 56))
    leader(ax, (EA_PORT[0]+4, EA_PORT[1]+4), "port mouth: the rings' centre", (82, 18))
    leader(ax, (2, 6), "host USB-C on the front face", (82, 4))
    scale_bar(ax, 140, 104, 50, "50 mm (at 3:2)")
    cam = Cam(40, 18); sc = Scene(cam); build_easel(sc, cam, kb_front=True)
    box_mm = (14, 290, 328, 96)
    heading(fig, box_mm, "2  Playing (1:2), the keyboard in front")
    cpt = cam.p((W/2, -40, 30)); ax = axes_mm(fig, box_mm, 0.5, (cpt[0]+8, cpt[1]+4)); sc.draw(ax)
    camf = Cam(28, 12); scf = Scene(camf); build_easel(scf, camf)
    box_mm = (14, 204, 160, 76)
    heading(fig, box_mm, "3  Face on, low (1:2)")
    cp = camf.p((W/2, 30, 45)); ax = axes_mm(fig, box_mm, 0.5, (cp[0], cp[1]-2)); scf.draw(ax)
    ax.text(cp[0], cp[1]-74, "one centred grille; knobs either side, low; lights above", ha="center", fontsize=SML-3, color=INK)
    camr = Cam(180+42, 16); scr = Scene(camr)
    build_easel(scr, camr, dress_on=False)
    box_mm = (186, 204, 156, 76)
    heading(fig, box_mm, "4  From behind (1:2)")
    cp = camr.p((W/2, 30, 45)); ax = axes_mm(fig, box_mm, 0.5, (cp[0], cp[1]-2)); scr.draw(ax)
    ax.text(cp[0], cp[1]-74, "flat back (SHOE docks here); jacks low on the right end", ha="center", fontsize=SML-3, color=INK)
    camp = Cam(222, 20); scp = Scene(camp); build_easel(scp, camp, packed=True, dress_on=False)
    box_mm = (14, 116, 160, 78)
    heading(fig, box_mm, "5  Packed (1:2): keyboard on its back")
    cp = camp.p((W/2, 40, 50)); ax = axes_mm(fig, box_mm, 0.5, (cp[0], cp[1]-2)); scp.draw(ax)
    camq = Cam(36, 22); scq = Scene(camq); build_easel(scq, camq)
    box_mm = (186, 116, 156, 78)
    heading(fig, box_mm, "6  Packed alone (1:2): panel out")
    cp = camq.p((W/2, 30, 45)); ax = axes_mm(fig, box_mm, 0.5, (cp[0], cp[1]-2)); scq.draw(ax)
    thumbs(fig, (14, 20, 328, 86))
    save(fig, path)


# ======================= CRADLE sheet =======================
def sheet_cradle(path):
    th = math.degrees(CR_TH)
    fig = new_sheet(27.0, "CRADLE · the lid tilts inside its own cheeks",
                    f"{CR_WT:.0f} × {CR_DEP:.0f} × {CR_ZF:.0f}–{CR_ZB:.0f} mm · flat or ≈ {th:.1f}° · one moving part: the slab itself",
                    "The slab hangs between two soft cheeks on pins at its front edge. Flat, it lies inside them; lift the back, push it away 5 mm, "
                    "set it on the rail, and the plate lies flush with the cheek tops. From the end it is one soft wedge either way.", FOOT)
    # 1 end views
    box_mm = (14, 395, 328, 190)
    heading(fig, box_mm, "1  End view (3:2): one outline, two states inside it")
    ax = axes_mm(fig, box_mm, 1.5, (100, 55))
    DZ = 63
    end_cradle(ax, False, dz=DZ); gline(ax, -8, 140, DZ)
    end_cradle(ax, True); gline(ax, -8, 140, 0)
    ax.text(-8, DZ+CR_ZB-2, "flat", fontsize=SML, color=INK, weight="bold", va="top")
    ax.text(-8, CR_ZB-2, "tilted", fontsize=SML, color=INK, weight="bold", va="top")
    leader(ax, (70, DZ+40), "the cheek: a soft wedge, 1.5T\nat the back, the same outline\nflat and tilted", (142, DZ+46))
    leader(ax, (CR_PIN[0]+2, DZ+CR_PIN[1]+2), "rings struck from the pivot pin\n(what the slab turns about)", (142, DZ+20))
    leader(ax, (100, DZ+33), "flat: the slab (dashed) lies inside", (142, DZ+4))
    pin = CR_TF_ANG(CR_PIN)
    leader(ax, (60, cr_top(60)-1), f"tilted ≈ {th:.1f}°: the plate flush\nwith the cheek tops", (142, 44))
    leader(ax, (CR_RAIL[1]-2, CR_RAIL[3]-3), "rail at T/2 = 17.5: the stretcher,\nand the ledge the slab sits on", (142, 18))
    scale_bar(ax, 142, -6, 50, "50 mm (at 3:2)")
    # 2 tilted 3/4 with keyboard
    cam = Cam(40, 22); sc = Scene(cam); build_cradle(sc, cam, tilted=True, kb_front=True)
    box_mm = (14, 290, 328, 96)
    heading(fig, box_mm, "2  Tilted (1:2), the keyboard in front")
    cpt = cam.p((CR_WT/2, -45, 22)); ax = axes_mm(fig, box_mm, 0.5, (cpt[0]+8, cpt[1]+12)); sc.draw(ax)
    jp = cam.p((CR_X0+232, -2, 14))
    leader(ax, jp, "jacks: one row of 6\non the front face", (jp[0]+95, jp[1]+30), size=SML-2)
    # 3 flat 3/4
    camf = Cam(40, 22); scf = Scene(camf); build_cradle(scf, camf)
    box_mm = (14, 204, 160, 76)
    heading(fig, box_mm, "3  Flat (1:2)")
    cp = camf.p((CR_WT/2, 55, 18)); ax = axes_mm(fig, box_mm, 0.5, (cp[0], cp[1]+6)); scf.draw(ax)
    # 4 from behind, tilted
    camr = Cam(180+40, 6); scr = Scene(camr)
    Lg = scr.layer(); add_face(Lg, camr, [(-6, -10, -0.2), (CR_WT+6, -10, -0.2), (CR_WT+6, CR_DEP+8, -0.2), (-6, CR_DEP+8, -0.2)], (0, 0, 1), (0.86, 0.83, 0.78), ec=(0.86, 0.83, 0.78))
    build_cradle(scr, camr, tilted=True, dress_on=False)
    box_mm = (186, 204, 156, 76)
    heading(fig, box_mm, "4  Tilted, from behind (1:2)")
    cp = camr.p((CR_WT/2, 60, 25)); ax = axes_mm(fig, box_mm, 0.5, (cp[0], cp[1]+4)); scr.draw(ax)
    rp = camr.p((CR_WT/2, CR_RAIL[1], CR_RAIL[3]-4))
    ax.text(rp[0]+10, rp[1]+48, "the rail takes the slab's back edge;\nport mouth on the rear face", ha="center", va="bottom", fontsize=SML-3, color=INK)
    # 5 packed
    camp = Cam(36, 26); scp = Scene(camp); build_cradle(scp, camp, packed=True)
    box_mm = (14, 116, 160, 78)
    heading(fig, box_mm, "5  Packed (1:2), keyboard on SHOE")
    cp = camp.p((CR_WT/2, 55, 8)); ax = axes_mm(fig, box_mm, 0.5, (cp[0], cp[1]+6)); scp.draw(ax)
    # 6 cheek B inset
    box_mm = (186, 116, 156, 78)
    heading(fig, box_mm, "6  Cheek B (3:4): low cheeks")
    ax = axes_mm(fig, box_mm, 0.75, (95, 50))
    end_cradle(ax, False, dy=0, dz=58, cheek="B", lw=1.4, hidden=False); gline(ax, -6, 135, 58)
    end_cradle(ax, True, dy=0, dz=0, cheek="B", lw=1.4, hidden=False); gline(ax, -6, 135, 0)
    ax.text(140, 58+16, "flat: a plain\nrounded block\n(SILL's outline)", fontsize=SML-3, color=INK, va="center")
    ax.text(140, 22, "tilted: the back\nrises 17 above\nthe cheeks", fontsize=SML-3, color=INK, va="center")
    thumbs(fig, (14, 20, 328, 86))
    save(fig, path)

# ======================= PLINTH sheet =======================
def sheet_plinth(path):
    th = math.degrees(PL_TH)
    fig = new_sheet(27.0, "PLINTH · the lid floating on its base",
                    f"280 × {D:.0f} × 35 flat · ≈ {th:.1f}° on the plinth · 2 pieces, nothing moves",
                    "CATHEDRAL's lid and base as two pieces. The module plays flat on its own; slide it downhill onto a darker printed wedge, "
                    "set in 10 mm behind a shadow gap, and the soft slab floats at a slight angle. The plinth's drawer holds the cable.", FOOT)
    box_mm = (14, 395, 328, 190)
    heading(fig, box_mm, "1  End view (3:2): the module alone, and on its plinth")
    ax = axes_mm(fig, box_mm, 1.5, (100, 56))
    DZ = 76
    end_plinth(ax, False, dz=DZ); gline(ax, -20, 140, DZ)
    end_plinth(ax, True); gline(ax, -20, 140, 0)
    ax.text(119, DZ+1.5, "flat", fontsize=SML, color=INK, weight="bold", va="bottom")
    ax.text(119, 1.5, "tilted", fontsize=SML, color=INK, weight="bold", va="bottom")
    leader(ax, (100, DZ+30), "flat: the module alone, the slab\nas SILL's, no recess in it", (142, DZ+30))
    mp = PL_TF((60, T))
    leader(ax, (mp[0], mp[1]-1), f"on the plinth ≈ {th:.1f}°:\nthe back rises T/2", (142, 54))
    leader(ax, (PL_Y0+PL_D-3, pl_top(PL_D)-PL_REB-0.5), "shadow gap: the plinth's top\nsteps down 3 mm round its edge", (142, 30))
    leader(ax, (PL_Y0+50, 6), "plinth: darker brown, set in 10,\nfront T/3, back 26", (142, 8))
    scale_bar(ax, 142, -1, 50, "50 mm (at 3:2)")
    cam = Cam(40, 22); sc = Scene(cam); build_plinth(sc, cam, kb_front=True)
    box_mm = (14, 290, 328, 96)
    heading(fig, box_mm, "2  Tilted on the plinth (1:2), the keyboard in front")
    cpt = cam.p((W/2, -45, 24)); ax = axes_mm(fig, box_mm, 0.5, (cpt[0]+8, cpt[1]+12)); sc.draw(ax)
    camf = Cam(40, 22); scf = Scene(camf); build_plinth(scf, camf, docked=False)
    box_mm = (14, 204, 160, 76)
    heading(fig, box_mm, "3  Flat (1:2): the module alone")
    cp = camf.p((W/2, 55, 15)); ax = axes_mm(fig, box_mm, 0.5, (cp[0], cp[1]+6)); scf.draw(ax)
    camd = Cam(-34, 30); scd = Scene(camd); build_plinth_base(scd, camd, drawer_out=60, tongue=True, core=(0.29, 0.18, 0.11))
    box_mm = (186, 204, 156, 76)
    heading(fig, box_mm, "4  The plinth alone (1:2), drawer out")
    cp = camd.p((W/2+30, 50, 10)); ax = axes_mm(fig, box_mm, 0.5, (cp[0]+22, cp[1]+2)); scd.draw(ax)
    ax.text(cp[0]-75, cp[1]-30, "drawer (right end):\ncable, adapter, card", ha="center", va="top", fontsize=SML-3, color=INK)
    camp = Cam(36, 26); scp = Scene(camp); build_plinth(scp, camp)
    box_mm = (14, 116, 160, 78)
    heading(fig, box_mm, "5  Packed (1:2): docked, ready to play")
    cp = camp.p((W/2, 55, 25)); ax = axes_mm(fig, box_mm, 0.5, (cp[0], cp[1]+4)); scp.draw(ax)
    camq = Cam(36, 26); scq = Scene(camq); build_plinth(scq, camq, packed=True)
    box_mm = (186, 116, 156, 78)
    heading(fig, box_mm, "6  Packed (1:2), keyboard under")
    cp = camq.p((W/2, 55, 16)); ax = axes_mm(fig, box_mm, 0.5, (cp[0], cp[1]+4)); scq.draw(ax)
    # 7 two pieces apart, end view at 3:2
    box_mm = (14, 20, 328, 86)
    heading(fig, box_mm, "7  Apart (1:1, end view): two pieces, one family of corners")
    ax = axes_mm(fig, box_mm, 1.0, (150, 18))
    end_sill_plain(ax, -5, 0, 2.0, True)
    pq = ccw(fillet_radii(PL_Q, [2, 2, 2, 2], n=6))
    ax.add_patch(Polygon(shiftp(ccw(PL_CORE), 125), closed=True, fc=SHD, ec="none"))
    ax.add_patch(Polygon(shiftp(pq, 125), closed=True, fc=PLC, ec=(0.15, 0.09, 0.05), lw=1.6))
    gline(ax, -10, 225, 0)
    ax.text(52, -4, f"module 280 × {D:.0f} × 35", ha="center", va="top", fontsize=SML-2, color=INK)
    ax.text(172, -4, f"plinth {PL_W:.0f} × {PL_D:.0f} × {PL_ZB:.0f}", ha="center", va="top", fontsize=SML-2, color=INK)
    save(fig, path)

# ======================= comparison sheet =======================
# Four column slots: SILL, CRADLE, PLINTH, and a fourth concept still to come (systems is structuring a narrow, steep one).
# To add it: give COLUMNS[3] its name, idea, end/kb/pack builders and trade lines.
MOVER = (0.24, 0.14, 0.08)
def _end_sill(ax, t): end_sill(ax, t, lw=2.2, mover=MOVER)
def _end_cradle(ax, t): end_cradle(ax, t, lw=2.2, mover=MOVER, hidden_lw=1.8)
def _end_plinth(ax, t): end_plinth(ax, t, lw=2.2, mover=MOVER)
def _vol(*dims): return dims[0]*dims[1]*dims[2]/1e6
CR_PACK = (CR_WT, CR_DEP, CR_ZB)
PL_PACK_D = max(PL_TF((D, 0))[0], PL_TF((D, T))[0]) - min(PL_TF((0, T))[0], PL_TF((0, 0))[0])
PL_PACK_H = PL_TF((D, T))[1]
COLUMNS = [
    dict(name="SILL", idea="a bar flips down", end=_end_sill, kb=lambda sc, c: build_sill(sc, c, tilted=True, kb_front=True),
         pack=lambda sc, c: build_sill(sc, c), cx=W/2,
         notes=("bar hidden in the base", "bar down"),
         trade=["1 piece", "1 moving part: the bar", f"280 × {D:.0f} × 35", f"{_vol(W, D, T):.2f} L", f"≈ {math.degrees(SI_TH):.1f}°", "watch: the plainest\noutline"]),
    dict(name="CRADLE", idea="tilts in its cheeks", end=_end_cradle, kb=lambda sc, c: build_cradle(sc, c, tilted=True, kb_front=True),
         pack=lambda sc, c: build_cradle(sc, c), cx=CR_WT/2,
         notes=("slab inside the cheeks", "same outline"),
         trade=["1 piece", "1 moving part: the slab", f"{CR_WT:.0f} × {CR_DEP:.0f} × {CR_ZB:.0f}", f"{CR_WT*CR_DEP*(CR_ZF+CR_ZB)/2/1e6:.2f} L", f"≈ {math.degrees(CR_TH):.1f}°", "watch: jacks move\nto the front face"]),
    dict(name="PLINTH", idea="sits on a 2nd piece", end=_end_plinth, kb=lambda sc, c: build_plinth(sc, c, kb_front=True),
         pack=lambda sc, c: build_plinth(sc, c), cx=W/2,
         notes=("the module alone", "on the plinth"),
         trade=["2 pieces", "0 moving parts", f"280 × {PL_PACK_D:.0f} × {PL_PACK_H:.0f}", "packs ready to play", f"≈ {math.degrees(PL_TH):.1f}°", "watch: plain slab flat;\nplinth can stay home"]),
    dict(name="EASEL", idea="stands steep, narrow", end=None, kb=lambda sc, c: build_easel(sc, c, kb_front=True),
         pack=lambda sc, c: build_easel(sc, c), cx=W/2,
         notes=("no flat pose", "its one pose, steep"),
         trade=["1 piece", "0 moving parts", f"280 × {EA_F:.0f} × {EA_HB:.0f}", f"{W*abs(area(ccw(easel_section(100.0))))/1e6:.2f} L, narrowest foot", "60°: steep, not slight",
                "watch: controls only in\nthe lower 45 mm;\na 1.5–2 N pull at\nthe top tips it;\nfour boards;\nweakest panel\nprotection; not flat\nor slightly angled\n(steep, as he asked)"]),
]
def sheet_compare(path):
    H = 22.0
    cs.FIG_H = H
    fig = plt.figure(figsize=(cs.FIG_W, H), dpi=cs.DPI); fig.patch.set_facecolor(BG)
    Wmm, Hmm = cs.FIG_W*MM, H*MM
    fig.text(0.03, 1-0.45/H, "floss: four ways it can sit", fontsize=50, weight="bold", color=INK, va="top")
    fig.text(0.03, 1-1.3/H, "Same controls, one speaker, same scale across each row.\nDark brown = the part that makes the angle.", fontsize=24, color="#555", va="top", linespacing=1.2)
    X0, GAP = 8.0, 2.0
    CW = (Wmm - 2*X0 - 3*GAP)/4
    colx = [X0 + i*(CW+GAP) for i in range(4)]
    ytop = Hmm - 84
    for col, x in zip(COLUMNS, colx):
        name, idea = col["name"], col["idea"]
        fig.text((x+2)/Wmm, ytop/Hmm, name, fontsize=40, weight="bold", color=INK if col else (0.70, 0.67, 0.62), va="bottom")
        fig.text((x+2)/Wmm, (ytop-1.5)/Hmm, idea, fontsize=22, color=INK if col else (0.70, 0.67, 0.62), va="top")
    rows = [("End view, flat", 40, "end", False), ("End view, angled", 66, "end", True),
            ("Playing, keyboard in front", 70, "kb", None), ("Packed", 52, "pack", None)]
    ES, VS = 0.6, 0.25
    KB_GAP[0] = 25.0
    y = ytop - 14
    for label, hgt, kind, tilted in rows:
        y -= 11
        fig.text(X0/Wmm, (y+1)/Hmm, label, fontsize=28, weight="bold", color=INK, va="bottom")
        fig.add_artist(plt.Line2D([X0/Wmm, (Wmm-X0)/Wmm], [(y+0.2)/Hmm]*2, color=(0.80, 0.77, 0.72), lw=1.5))
        y -= hgt
        for col, x in zip(COLUMNS, colx):
            bx = (x, y, CW, hgt)
            if col is None:
                ax = axes_mm(fig, bx, 1.0, (0, 0))
                ax.add_patch(Rectangle((-CW/2+3, -hgt/2+3), CW-6, hgt-6, fc="none", ec=(0.78, 0.75, 0.70), lw=1.5, ls=(0, (4, 3))))
                continue
            if kind == "end":
                ax = axes_mm(fig, bx, ES, (60, hgt/ES/2 - 8))
                if col["end"] is None:
                    if tilted: end_easel(ax, dy=30, lw=2.2); gline(ax, -20, 140, 0)
                    else: ax.text(60, hgt/ES/2 - 8, "no flat pose", ha="center", va="center", fontsize=24, color=(0.62, 0.22, 0.15))
                    continue
                col["end"](ax, tilted); gline(ax, -20, 140, 0)
            else:
                cam = Cam(40, 22) if kind == "kb" else Cam(36, 26); sc = Scene(cam)
                (col["kb"] if kind == "kb" else col["pack"])(sc, cam)
                cp = cam.p((col["cx"], -30 if kind == "kb" else 55, 20))
                ax = axes_mm(fig, bx, 0.2 if kind == "kb" else VS, (cp[0]+(11 if kind == "kb" else 6), cp[1]+(-8 if kind == "kb" else 6))); sc.draw(ax)
        if kind == "end":
            for col, x in zip(COLUMNS, colx):
                if col and not (col["end"] is None and not tilted):
                    fig.text((x+2)/Wmm, (y-0.5)/Hmm, col["notes"][1 if tilted else 0], fontsize=19, color="#555", va="top", linespacing=1.1)
            y -= 16 if tilted else 11
    y -= 12
    fig.text(X0/Wmm, (y+1)/Hmm, "The trade", fontsize=28, weight="bold", color=INK, va="bottom")
    fig.add_artist(plt.Line2D([X0/Wmm, (Wmm-X0)/Wmm], [(y+0.2)/Hmm]*2, color=(0.80, 0.77, 0.72), lw=1.5))
    for col, x in zip(COLUMNS, colx):
        if not col: continue
        yy = y - 3
        for k, t in enumerate(col["trade"]):
            fig.text((x+2)/Wmm, yy/Hmm, t, fontsize=21, va="top", linespacing=1.15,
                     color=(0.62, 0.22, 0.15) if k == 5 else INK, weight="bold" if k in (0, 1, 4) else "normal")
            yy -= 8.2 * (t.count("\n") + 1)
    fig.text(0.03, 0.2/H, "trade: pieces · moving parts · packed size (mm) · volume · angle · what to watch\n"
             "idea level, not a render · sizes [calc] from systems, nothing measured · end views 3:5 · keyboard row 1:5 · packed 1:4",
             fontsize=13, color=GREY)
    fig.savefig(path, facecolor=BG, dpi=cs.DPI); plt.close(fig)
    KB_GAP[0] = 60.0

if __name__ == "__main__":
    import sys
    which = sys.argv[1:] or ["cradle", "plinth", "easel", "compare"]
    if "cradle" in which: sheet_cradle("../r2-cradle/sheet.png")
    if "plinth" in which: sheet_plinth("../r2-plinth/sheet.png")
    if "easel" in which: sheet_easel("../r2-easel/sheet.png")
    if "compare" in which: sheet_compare("../r2-compare.png")
    print("SILL %.2f  CRADLE %.2f (cheek %.1f / %.1f, lip y %.2f)  PLINTH %.2f (plinth %.1f / %.1f)" % (
        math.degrees(SI_TH), math.degrees(CR_TH), CR_ZF, CR_ZB, _lip[0], math.degrees(PL_TH), PL_ZF, PL_ZB))
