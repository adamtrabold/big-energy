# floss jam pass 2 (visual): the split solved about middle C, and three faces. Rough. Run: python3 -I visual_jam2.py
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle
WAL="#6b4429"; CREAM="#f1ebdd"; BLACK="#1d1b19"; CORAL="#f0806a"; MAPLE="#e8cf9c"; GREY="#8a8276"; FELT="#9a958c"; FELTD="#86817a"; EBONY="#2b2320"; BONE="#efe6d2"
fig=plt.figure(figsize=(16.5,11.7),dpi=150); fig.patch.set_facecolor("#f6f2ea")
fig.text(0.03,0.975,"floss · jam pass 2 · visual · the split about middle C, and three faces (rough, 2026-11-22)",fontsize=11,weight="bold")

# ---------- 1: split geometry ----------
ax=fig.add_axes([0.03,0.60,0.94,0.34]); ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-95,330); ax.set_ylim(-30,110)
K0=8  # key run starts 8 mm in from case edge (286 case, 270 run)
ax.add_patch(Rectangle((0,0),286,95,fc=CREAM,ec=GREY,lw=0.6))
for i in range(15):
    ax.add_patch(Rectangle((K0+18*i,0),18,34,fc="white",ec=GREY,lw=0.6))
for i in [0,1,3,4,5,7,8,10,11,12]:
    ax.add_patch(Rectangle((K0+18*(i+1)-5,14),10,20,fc=BLACK,ec="none"))
axis=143
ax.plot([axis,axis],[-8,103],color=GREY,lw=0.6,ls=(0,(4,3)))
ax.text(axis,105,"case axis = centre of middle C",ha="center",fontsize=7.5,color=GREY)
# groups
ax.add_patch(Rectangle((K0,42),126,40,fc="#e6dccb",ec="none")); ax.text(K0+63,62,"LEFT group · 126 wide\nover C–B (7 whites)",ha="center",va="center",fontsize=8)
ax.add_patch(Rectangle((K0+144,42),126,40,fc="#e6dccb",ec="none")); ax.text(K0+144+63,62,"RIGHT group · 126 wide\nover D–C (7 whites)",ha="center",va="center",fontsize=8)
ax.add_patch(Rectangle((K0+126,42),18,40,fc="none",ec=CORAL,lw=0.8,ls=(0,(2,2))))
ax.text(axis,86,"gutter = one key wide",ha="center",fontsize=7,color=CORAL)
for k,n in enumerate(["high","main","low"]): ax.text(axis,74-k*10,n,ha="center",fontsize=6.5)
# split tick at key rim
xs=K0+126
ax.plot([xs,xs],[-6,0],color=CORAL,lw=2.2)
ax.text(xs-2,-14,"the only split mark: a coral tick on the front rim, between B and C",ha="right",fontsize=7.5,color=CORAL)
ax.text(axis+12,-14,"middle C belongs to the right half; its own key sits under the gutter",ha="left",fontsize=7.5,color=GREY)
ax.text(-92,95,"1 · The face is symmetric; the split is true.",fontsize=9.5,weight="bold")
ax.text(-92,86,"25 keys = 7 whites + middle C + 7 whites.",fontsize=7.5)
ax.text(-92,79,"Middle C is the centre key,",fontsize=7.5); ax.text(-92,72,"so the axis runs through it.",fontsize=7.5)
ax.text(-92,62,"Each half's controls fill",fontsize=7.5); ax.text(-92,55,"126 mm; the gutter over",fontsize=7.5); ax.text(-92,48,"middle C carries what",fontsize=7.5); ax.text(-92,41,"both halves share.",fontsize=7.5)
ax.text(292,80,"Rejected:",fontsize=7.5,weight="bold")
for k,t in enumerate(["line through the face","(9 mm off centre)","keys shifted 9 mm","(case +18 mm)","case asymmetric","on purpose (reads","as a mistake)","24 keys (owner-only","trade, not needed)"]):
    ax.text(292,72-k*7,t,fontsize=6.5,color=GREY)

# ---------- 2: three faces ----------
def knob(a,x,y,r=5.5,c=BLACK,lab="",fs=5.6,lc=BLACK):
    a.add_patch(Circle((x,y),r,fc=c,ec="none")); a.plot([x,x],[y,y+r*0.85],color="white",lw=0.8)
    if lab: a.text(x,y+r+2,lab,ha="center",fontsize=fs,color=lc)
def tabcol(a,x,y,states,c1="#b48a4e",c0="#cfc5b1"):
    for k,on in enumerate(states):
        a.add_patch(FancyBboxPatch((x-4,y-k*11-4),8,8,boxstyle="round,pad=0,rounding_size=1.5",fc=(c1 if on else c0),ec="none"))
def keys(a,y0,wc,sc,peg=False,collar=None):
    for i in range(15):
        cx=K0+9+18*i
        if peg:
            if collar: a.add_patch(Circle((cx,y0+9),7.6,fc=collar,ec="none"))
            a.add_patch(Circle((cx,y0+9),6,fc=wc,ec="none"))
        else: a.add_patch(Rectangle((cx-9,y0),18,32,fc=wc,ec=GREY,lw=0.5))
    for i in [0,1,3,4,5,7,8,10,11,12]:
        cx=K0+18*(i+1)
        if peg:
            if collar: a.add_patch(Circle((cx,y0+30),7.6,fc=collar,ec="none"))
            a.add_patch(Circle((cx,y0+30),6,fc=sc,ec="none"))
        else: a.add_patch(Rectangle((cx-5,y0+13),10,19,fc=sc,ec="none"))
    a.plot([K0+126,K0+126],[y0-5,y0-1],color=CORAL,lw=2)

# BOW
a=fig.add_axes([0.02,0.05,0.32,0.50]); a.set_aspect("equal"); a.axis("off"); a.set_xlim(-5,291); a.set_ylim(-20,300)
a.add_patch(FancyBboxPatch((0,150),286,132,boxstyle="round,pad=0,rounding_size=14",fc=WAL,ec="none"))
a.add_patch(FancyBboxPatch((6,156),274,120,boxstyle="round,pad=0,rounding_size=9",fc="#e4dccb",ec="none"))
a.plot([6,280],[170,170],color=CORAL,lw=0.8); a.text(143,215,"lid: cloth over the sealed box\n(driver + passive radiator); no motif",ha="center",fontsize=6.5,color=GREY)
a.add_patch(FancyBboxPatch((0,0),286,140,boxstyle="round,pad=0,rounding_size=14",fc=WAL,ec="none"))
a.add_patch(FancyBboxPatch((4.3,4.3),277.4,131.4,boxstyle="round,pad=0,rounding_size=10",fc=CREAM,ec="none"))
keys(a,8,EBONY,BONE,peg=True,collar="#cfc6b4")
knob(a,22,72,7,lab="octave"); tabcol(a,124,82,[1,1,0]); tabcol(a,162,82,[0,1,1]); knob(a,264,72,7,lab="octave")
for k,n in enumerate(["high","main","low"]): a.text(143,80-k*11,n,ha="center",va="center",fontsize=5.6)
a.add_patch(Circle((60,66),4,fc="#e9e2d2",ec=BLACK,lw=0.7)); a.text(60,72,"hold",ha="center",fontsize=5.6)
a.add_patch(Circle((143,124),1.8,fc="#7bd389",ec="none"))
row=[("attack",20),("release",42),("pressure",64,CORAL),("tone",96),("shimmer",186),("depth",208),("echo",230),("reverb",252)]
for r in row: knob(a,r[1],112,5.5,c=(r[2] if len(r)>2 else BLACK),lab=r[0])
knob(a,272,112,5.5,lab="vol")
a.text(0,292,"BOW · CATHEDRAL case, lid is the soundbox",fontsize=9,weight="bold")
a.text(0,-8,"dark naturals, bone sharps, felt collars (lean = give). coral = pressure: what a lean does.",fontsize=6.3,color=GREY)
a.text(0,-16,"strand tabs stand in columns either side of the gutter; their names are printed once, in it.",fontsize=6.3,color=GREY)

# KEPT
a=fig.add_axes([0.35,0.05,0.30,0.50]); a.set_aspect("equal"); a.axis("off"); a.set_xlim(-5,291); a.set_ylim(-20,300)
a.add_patch(FancyBboxPatch((0,0),286,165,boxstyle="round,pad=0,rounding_size=10",fc="#e8dcc2",ec="none"))
keys(a,8,"white",BLACK)
knob(a,22,66,7,lab="octave"); knob(a,264,66,7,lab="octave")
for k,n in enumerate(["bass","strings","brass"]):
    x=[56,90,196][k]
    a.add_patch(FancyBboxPatch((x-6,58),12,16,boxstyle="round,pad=0,rounding_size=2",fc=("#c4544a" if k==0 else "#d8cdb5"),ec="none"))
    a.text(x,77,n,ha="center",fontsize=5.6)
a.text(56,50,"(left only)",ha="center",fontsize=5,color=GREY)
a.add_patch(Circle((118,66),4,fc="#e9e2d2",ec=BLACK,lw=0.7)); a.text(118,72,"hold",ha="center",fontsize=5.6)
row=[("attack",30),("release",56),("pressure",82),("tone",118),("ensemble",168),("echo",200),("reverb",226),("vol",262)]
for r in row: knob(a,r[1],110,5.5,c=(CORAL if r[0]=="ensemble" else BLACK),lab=r[0])
for x in range(30,260,8): a.add_patch(Rectangle((x,140),3,14,fc="#cbbd9f",ec="none"))
a.text(143,135,"slotted grille across the back band",ha="center",fontsize=5.5,color=GREY)
a.add_patch(Circle((143,158),1.8,fc="#7bd389",ec="none"))
a.text(0,292,"KEPT · ONE SHEET slab, a string machine's panel",fontsize=9,weight="bold")
a.text(0,180,"one row, in the Solina's order;\nlooks like 1974, plays like now.\ncoral = the ensemble.",fontsize=7,color=GREY)
a.text(0,-8,"white and black keys: the only one that looks like a keyboard.",fontsize=6.3,color=GREY)
a.text(0,-16,"hold sits in the left group: it latches the left half (the bass region).",fontsize=6.3,color=GREY)

# TIDE
a=fig.add_axes([0.67,0.05,0.31,0.50]); a.set_aspect("equal"); a.axis("off"); a.set_xlim(-5,295); a.set_ylim(-20,300)
a.add_patch(FancyBboxPatch((0,0),290,186,boxstyle="round,pad=0,rounding_size=34",fc=FELT,ec="none"))
keys(a,12,MAPLE,"#b9925a",peg=True,collar=FELTD)
knob(a,24,74,7,lab="octave",lc="#2a2622"); knob(a,266,74,7,lab="octave",lc="#2a2622")
a.add_patch(Circle((145,72),7,fc=MAPLE,ec="none")); a.add_patch(Circle((145,72),9,fc="none",ec=FELTD,lw=1.5)); a.text(145,84,"hold",ha="center",fontsize=5.6)
a.text(145,60,"(a peg: all keys)",ha="center",fontsize=5,color="#3a3530")
row=[("attack",40),("release",64),("pressure",88),("tone",112)]
for r in row: knob(a,r[1],112,5.5,c="#efe7d6",lab=r[0],lc="#2a2622")
knob(a,145,116,10,c=CORAL,lab="drift",fs=6.5,lc="#2a2622")
for r in [("shimmer",178),("echo",202),("reverb",226),("vol",250)]: knob(a,r[1],112,5.5,c="#efe7d6",lab=r[0],lc="#2a2622")
import numpy as np
for i in range(9):
    for j in range(3):
        x=105+i*10; y=148+j*8
        a.add_patch(Circle((x,y),1.6,fc="#ffd79a" if (i+j)%3==0 else "#5f5a52",ec="none"))
a.text(145,176,"speaker holes; the lantern glows through them",ha="center",fontsize=5.5,color="#2a2622")
a.text(0,292,"TIDE · HUSH's felt pebble, the one you watch",fontsize=9,weight="bold")
a.text(0,200,"grey wool, maple pegs, words pressed blind.\ncoral = drift. no registers.",fontsize=7,color=GREY)
a.text(0,-8,"soft strike = longest, most wandering note; lean while planting = how far it will drift.",fontsize=6.3,color=GREY)
a.text(0,-16,"the lantern lives only here: the light comes out of the same holes as the sound.",fontsize=6.3,color=GREY)
fig.savefig("/home/claude/big-energy/floss/design/sketches/visual-jam2-faces.png",facecolor=fig.get_facecolor()); print("ok")
