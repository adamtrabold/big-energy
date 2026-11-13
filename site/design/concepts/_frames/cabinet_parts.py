from lib import *

STAGES = ["Concept", "Lock", "Handoff", "Spec", "BOM", "Breadboard", "Boards", "Prints", "Assembly"]
COUNTS = {"Concept": [67, 38, 7], "Spec": [0, 19, 0]}
KINDS = ["images", "docs", "tests"]

def cabinet_grid(c, x, y, cw=67.5, rh=34, name_w=88, dots=(), snapshot=False, past=None):
    gx = x + name_w
    cw = cw * 4 / 3
    for j, k in enumerate(KINDS):
        c.label(gx + j * cw + cw / 2, y - 8, k, anchor="middle")
    for i, s in enumerate(STAGES):
        yy = y + i * rh
        now = s == "Lock"
        done = s in ("Concept",)
        future = i >= 2
        c.t(x, yy + rh / 2 + 5, s, 13.5, 600 if now else 400, INK if i < 2 else INK2)
        if s == "Spec": c.t(x + tw("Spec", 13.5) + 6, yy + rh / 2 + 5, "early", 11, 500, INK2)
        if now:
            c.r(x - 12, yy + 7, 3, rh - 14, INK)
        if s == "Lock":
            c.r(gx + 2, yy + 3, 3 * cw - 4, rh - 6, CELL, RULE)
            c.t(gx + 14, yy + rh / 2 + 5, "v1.1 current · 2 versions", 14, 600)
            c.t(gx + 3 * cw - 12, yy + rh / 2 + 5, "now", 12, 500, INK2, "end")
        elif s == "Handoff":
            c.r(gx + 2, yy + 3, 3 * cw - 4, rh - 6, "none", RULE)
            c.t(gx + 14, yy + rh / 2 + 5, "next · starts when you pick", 13, 400, INK2)
        elif s in COUNTS:
            for j in range(3):
                n = COUNTS[s][j]
                cx = gx + j * cw
                if s == "Concept":
                    c.r(cx + 2, yy + 3, cw - 4, rh - 6, CELL if n else "none", RULE)
                    if n: c.t(cx + cw / 2, yy + rh / 2 + 6, str(n), 16, 500, INK, "middle")
                else:  # begun early, below the level
                    c.r(cx + 2, yy + 3, cw - 4, rh - 6, "none", RULE)
                    if n: c.t(cx + cw / 2, yy + rh / 2 + 6, str(n), 16, 500, INK2, "middle")
                if (s, j) in dots and not snapshot:
                    c.dot(cx + cw - 10, yy + 11)
        else:
            c.t(gx + 14, yy + rh / 2 + 5, "not yet", 13, 400, INK2)
        if s == "Lock":  # the level
            c.l(x - 12, yy + rh + 0.5, gx + 3 * cw, yy + rh + 0.5, INK, 1.5)
    return y + 9 * rh

