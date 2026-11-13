import sys
from scenes import *
import ld
SZ = (5200, 3500)
if "--test" in sys.argv:
    SZ = (1600, 1080); sys.argv.remove("--test")
CL = ("ply",)
jobs = {
 "tc_main":  lambda: ld.shot(type_case(), type_case_fp(), "tc_main", size=SZ, dist=740, el=36),
 "tc_carry": lambda: ld.shot(type_case(), type_case_fp(), "tc_carry", size=SZ, az=148, el=30, dist=760),
 "hy_main":  lambda: ld.shot(hymnal(), hymnal_fp(), "hy_main", size=SZ, dist=1180, center=(149,105,70)),
 "hy_closed":lambda: ld.shot(hymnal(open_state=False), hymnal_fp(False), "hy_closed", size=SZ, dist=800, center=(149,90,20)),
 "hy_piano": lambda: ld.shot(hymnal(keystyle="piano"), hymnal_fp(), "hy_piano", size=SZ, az=-12, el=48, dist=430, center=(120,30,22)),
 "hu_main":  lambda: ld.shot(hush(), hush_fp(), "hu_main", size=SZ, dist=760, center=(149,95,14), grain_classes=("ply","felt")),
 "hu_closed":lambda: ld.shot(hush_closed(), hush_closed_fp(), "hu_closed", size=SZ, dist=780, center=(149,90,20), grain_classes=("felt",)),
 "os_main":  lambda: ld.shot(one_sheet_printed(), one_sheet_printed_fp(), "os_main", size=SZ, dist=740, grain_classes=()),
 "os_carry": lambda: ld.shot(sleeve(one_sheet_printed(), 38), footprint(-6,-6,W+6,D+40), "os_carry", size=SZ, az=-32, el=34, dist=820, center=(149,100,16), grain_classes=("felt",)),
 "fo_main":  lambda: ld.shot(fold(True), fold_fp(True), "fo_main", size=SZ, dist=900, el=40, center=(149,106,12), grain_classes=("walnut",), grain_angle=-27),
 "fo_closed":lambda: ld.shot(fold(False, book=True), fold_fp(False, book=True), "fo_closed", size=SZ, dist=1150, el=28, az=-24, center=(278,70,22), grain_classes=("walnut",), grain_angle=-27),
 "fo_five":  lambda: ld.shot_top(fold_five_top(), "fo_five", -2, 104, 300, 214, px_per_mm=6, grain_classes=()),
 "ug_main":  lambda: ld.shot(under_glass(), under_glass_fp(), "ug_main", size=SZ, dist=740, el=46, grain_classes=()),
 "ug_carry": lambda: ld.shot(sleeve(under_glass(), 37, col="#5d5f62"), footprint(-6,-6,W+6,D+40), "ug_carry", size=SZ, az=-32, el=34, dist=820, center=(149,100,16), grain_classes=()),
}
from content import CONCEPTS
TOPS = {"type-case": lambda: type_case(), "hymnal": lambda: hymnal(show_lid=False), "hush": lambda: hush(),
        "one-sheet": lambda: one_sheet_printed(), "fold": lambda: fold(True), "under-glass": lambda: under_glass()}
GC = {"type-case": ("ply",), "hymnal": ("ply",), "hush": ("felt",), "one-sheet": (), "fold": ("walnut",), "under-glass": ()}
for cc in CONCEPTS:
    nm = cc["top"][:-4]
    jobs[nm] = (lambda cc=cc, nm=nm: ld.shot_top(TOPS[cc["folder"]](), nm, *cc["topbox"], px_per_mm=12, grain_classes=GC[cc["folder"]]))
for k in (sys.argv[1:] or jobs):
    print(jobs[k]())
