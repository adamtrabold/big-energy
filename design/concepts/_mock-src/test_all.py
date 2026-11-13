import sys
from scenes import *
import ld
which = sys.argv[1]; sz=(1600,1100)
if which=="tc": print(ld.shot(type_case(), type_case_fp(), "tc_test", size=sz, dist=760))
if which=="os": print(ld.shot(one_sheet(), one_sheet_fp(), "os_test", size=sz, dist=760))
if which=="hy": print(ld.shot(hymnal(), hymnal_fp(), "hy_test", size=sz, dist=980, center=(149,100,62), grain_classes=("ply","cedar")))
if which=="hu": print(ld.shot(hush(), hush_fp(), "hu_test", size=sz, dist=780, grain_classes=("ply","felt")))
