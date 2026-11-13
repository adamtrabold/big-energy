"""Round 5 flat-concept check (HUSH, ONE SHEET): FOLD rev 5.1's balanced layout in the flat frames.
Same rules as layout_r4_check.py. ONE SHEET x = FOLD x - 5 (276 wide, centre 138); HUSH x = FOLD x + 2 (290, centre 145).
Rows: PLAY 68, VOICE 100 / 123, horizontal break 85.4. Run: python3 flat_r5_check.py"""
import math, itertools, importlib.util, io, contextlib
spec = importlib.util.spec_from_file_location("f", __file__.replace("flat_r5_check.py", "fold_r5_check.py"))
f = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(f)
P, V1, V2, HB, VF = 68, 100, 123, 85.4, 146
FR = {"ONE SHEET": dict(dx=-5, W=276, edge=10), "HUSH": dict(dx=2, W=290, edge=12)}
tot = 0
for name, c in FR.items():
    dx, W, edge = c["dx"], c["W"], c["edge"]; bad = 0
    it = [(e[0], e[1]+dx, e[4] if len(e) > 4 else P, e[2], e[3], "P") for e in f.play]
    it += [(n, x+dx, V1, r, k, "V") for n, x, r, k in f.v1] + [(n, x+dx, V2, r, k, "V") for n, x, r, k in f.v2]
    it += [(n, x+dx, VF, r, k, "F") for n, x, r, k in f.fx]
    it += [(n, x+dx, 111.5, r, k, "V") for n, x, r, k in f.sw_flat]
    br = [b+dx for b in f.vb_play]; brf = [b+dx for b in f.vb_fx]
    for a, b in itertools.combinations(it, 2):
        d = math.dist(a[1:3], b[1:3])
        if a[4] == "k" and b[4] == "k" and a[2] == b[2]:
            need = 24 if {a[0], b[0]} <= {"CUTOFF", "EMPHASIS", "CONTOUR AMT"} else 20
            if d < need-1e-6: print(" PITCH", a[0], b[0]); bad += 1
        if d-a[3]-b[3] < 1.5: print(" GAP", a[0], b[0], round(d-a[3]-b[3], 2)); bad += 1
    for n, x, y, r, k, h in it:
        need = 7 if k in ("k", "stick", "b") else 3 if k == "t" else 1
        for b in (brf if h == "F" else br):
            if abs(x-b)-r < need-1e-6: print(" BREAK", n); bad += 1
        if abs(y-HB)-r < need-1e-6: print(" HBREAK", n, round(abs(y-HB)-r, 2)); bad += 1
        if x-r < edge or W-(x+r) < edge: print(" EDGE", n); bad += 1
    xs = lambda row: sorted(e[1] for e in it if e[2] == row)
    sym = max(max(abs((a+b)/2 - W/2) for a, b in zip(xs(y), reversed(xs(y)))) for y in (P, V1, V2, VF, 111.5))
    print(f"{name}: breaks {br} (FX row {brf}), FX row y {VF}, last edge {VF+7.45}, centre {W/2}, worst mirror offset {sym:.2f}, stick->CUTOFF 94, violations {bad}")
    tot += bad
print("TOTAL", tot)
