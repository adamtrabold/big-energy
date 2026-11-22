# floss jam turn 2 (visual): quick sketches, not to scale-perfect. Run: python3 visual_jam1.py
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Polygon, Ellipse
import numpy as np

WAL="#6b4429"; CREAM="#f1ebdd"; BRASS="#c9a24a"; BLACK="#1d1b19"; CORAL="#f0806a"; CLOTH="#e4dccb"; MAPLE="#e8cf9c"; GREY="#8a8276"

fig = plt.figure(figsize=(16.5, 11.7), dpi=150)
fig.patch.set_facecolor("#f6f2ea")

# ---------- A: SAIL top view of the base, "above each half, its own" ----------
ax = fig.add_axes([0.03, 0.40, 0.56, 0.55]); ax.set_aspect("equal"); ax.axis("off")
ax.set_xlim(-10, 300); ax.set_ylim(-28, 150)
ax.add_patch(FancyBboxPatch((0,0),286,132,boxstyle="round,pad=0,rounding_size=14",fc=WAL,ec="none"))
ax.add_patch(FancyBboxPatch((4.3,4.3),277.4,123.4,boxstyle="round,pad=0,rounding_size=10",fc=CREAM,ec="none"))
# keys: 15 naturals at 18, pegs
x0 = 143-135
whites=[]; 
for i in range(15):
    cx = x0+9+18*i; whites.append(cx)
    ax.add_patch(Circle((cx,16),6.2,fc=MAPLE,ec="#b89a62",lw=0.8))
    ax.add_patch(Circle((cx,16),7.6,fc="none",ec="#cfc6b4",lw=0.6))  # felt collar
sharp_after=[0,1,3,4,5,7,8,10,11,12]
for i in sharp_after:
    cx = x0+18*(i+1)
    ax.add_patch(Circle((cx,38),6.2,fc="#3a2a1e",ec="#22170f",lw=0.8))
    ax.add_patch(Circle((cx,38),7.6,fc="none",ec="#cfc6b4",lw=0.6))
# split: between B (white 7, idx6) and C (white 8, idx7)
xs = (whites[6]+whites[7])/2
ax.plot([xs,xs],[50,120],color=CORAL,lw=1.6)
ax.text(xs,123.5,"the coral thread: where the keyboard splits, the panel splits",ha="center",fontsize=7.5,color=CORAL)
# near row (per half)
def knob(x,y,r=6.5,c=BLACK,label="",lc=BLACK,fs=6.5):
    ax.add_patch(Circle((x,y),r,fc=c,ec="none"))
    ax.plot([x,x+r*0.0],[y,y+r*0.85],color="white",lw=1)
    if label: ax.text(x,y+r+2.2,label,ha="center",fontsize=fs,color=lc)
def tab(x,y,on,label):
    ax.add_patch(FancyBboxPatch((x-4.5,y-7),9,14,boxstyle="round,pad=0,rounding_size=2",fc=(MAPLE if on else "#d8cfbd"),ec="#9c8b6c",lw=0.7))
    ax.add_patch(Rectangle((x-4.5,y+(1 if on else -7)),9,6,fc=("#b48a4e" if on else "#c4b9a3"),ec="none"))
    ax.text(x,y+9.5,label,ha="center",fontsize=6.3)
yN=66
knob(22,yN,7.5,label="octave  16' 8' 4' 2'")
for k,(lab,on) in enumerate([("cello",1),("viola",1),("violin",0)]):
    tab(48+15*k,yN,on,lab)
ax.add_patch(Circle((104,yN),4.2,fc="#e9e2d2",ec=BLACK,lw=0.8)); ax.text(104,yN+7,"set",ha="center",fontsize=6.5)
ax.add_patch(Circle((104,yN),1.4,fc=CORAL,ec="none"))
for k,(lab,on) in enumerate([("cello",0),("viola",1),("violin",1)]):
    tab(182+15*k,yN,on,lab)
knob(264,yN,7.5,label="octave  16' 8' 4' 2'")
ax.text(60,yN-14,"LEFT HALF owns this", ha="center",fontsize=7,color=GREY)
ax.text(212,yN-14,"RIGHT HALF owns this", ha="center",fontsize=7,color=GREY)
# far row: shared
yF=101
far=[("tone",24),("swell",46),("release",68),("pressure",94),("shimmer",126),("",0),("echo",196),("reverb",218),("volume",262)]
for lab,x in far:
    if not lab: continue
    knob(x,yF,6.5,label=lab)
knob(158,yF,9.5,c=CORAL,label="depth",fs=7)
ax.text(126,yF-12,"bbd · wide · haze · still",ha="center",fontsize=5.5,color=GREY)
ax.text(94,yF-12,"swell · vib · bright · shimmer",ha="center",fontsize=5.5,color=GREY)
ax.add_patch(Circle((240,yF),2.2,fc="#7bd389",ec="none")); ax.text(240,yF+5,"status",ha="center",fontsize=6)
ax.text(143,140,"A · SAIL base, top view (rough, ≈ 286 × 132, CATHEDRAL's base footprint).  Shared controls on the far row; each half's own controls sit above that half.",ha="center",fontsize=8.5)
ax.text(143,-14,"maple pegs on felt collars (HUSH's 'old idea', on CATHEDRAL's interchangeable key carrier); a lean squashes the felt = bow pressure you can feel",ha="center",fontsize=7.5,color=GREY)
ax.text(143,-22,"labels and positions are placeholders for systems; the point is the map, not the words",ha="center",fontsize=7,color=GREY)

# ---------- B: SAIL standing, side elevation ----------
ax2 = fig.add_axes([0.61, 0.52, 0.37, 0.43]); ax2.set_aspect("equal"); ax2.axis("off")
ax2.set_xlim(-60, 230); ax2.set_ylim(-20, 175)
ax2.add_patch(Rectangle((0,0),132,27,fc=WAL,ec="none"))
ax2.add_patch(Rectangle((4,27),40,4,fc=MAPLE,ec="none")); ax2.text(20,34,"keys",fontsize=7,ha="center")
for x in (70,95,118): ax2.add_patch(Rectangle((x-4,27),8,8,fc=BLACK,ec="none"))
ang=np.radians(65)  # leans back, away from the player
hx,hy=132,27
L=132; T=24
d=np.array([np.cos(ang),np.sin(ang)]); n=np.array([np.sin(ang),-np.cos(ang)])
p0=np.array([hx,hy]); p1=p0+d*L; 
poly=[p0, p1, p1+n*T, p0+n*T]
ax2.add_patch(Polygon(poly,closed=True,fc=WAL,ec="none"))
# cloth face (inner face toward player is the side opposite n)
c0=p0+d*6; c1=p0+d*(L-6)
ax2.plot([c0[0],c1[0]],[c0[1],c1[1]],color=CLOTH,lw=6,solid_capstyle="butt")
ax2.plot([c0[0],c1[0]],[c0[1],c1[1]],color=CORAL,lw=0.8)
# glow
for k,s in enumerate([0.3,0.55,0.8]):
    q=p0+d*(L*s)-n*6
    ax2.add_patch(Circle(q,9,fc="#ffcf8a",ec="none",alpha=0.35))
# sound arrows to player
for s in (0.35,0.6):
    q=p0+d*(L*s)-n*3
    ax2.annotate("",xy=(q[0]-38,q[1]-22),xytext=(q[0],q[1]),arrowprops=dict(arrowstyle="->",color=GREY,lw=0.9))
# stay
ax2.plot([hx+n[0]*T+d[0]*60, hx+n[0]*T+d[0]*60+25],[hy+n[1]*T+d[1]*60, 0],color=BRASS,lw=2)
ax2.text(-55,150,"B · SAIL standing (side)",fontsize=9)
ax2.text(-55,140,"Base: CATHEDRAL's case, keys, stays, hinge.",fontsize=7.5)
ax2.text(-55,132,"Lid: no controls. A walnut frame with cloth",fontsize=7.5)
ax2.text(-55,124,"stretched over it (a kite's frame + skin): the",fontsize=7.5)
ax2.text(-55,116,"sealed box for the driver + passive radiator,",fontsize=7.5)
ax2.text(-55,108,"and a lantern: warm light behind the cloth",fontsize=7.5)
ax2.text(-55,100,"moves with the ensemble's LFOs.",fontsize=7.5)
ax2.text(-55,88,"Open the lid = on. Close it = off.",fontsize=7.5,color=CORAL)
ax2.text(-50,-14,"← player",fontsize=7,color=GREY)

# ---------- C: lid inner face, rose window ----------
ax3 = fig.add_axes([0.03, 0.03, 0.42, 0.34]); ax3.set_aspect("equal"); ax3.axis("off")
ax3.set_xlim(-10, 300); ax3.set_ylim(-15, 158)
ax3.add_patch(FancyBboxPatch((0,0),286,132,boxstyle="round,pad=0,rounding_size=14",fc=WAL,ec="none"))
ax3.add_patch(FancyBboxPatch((6,6),274,120,boxstyle="round,pad=0,rounding_size=9",fc=CLOTH,ec="none"))
# lantern glow blobs
for x,a in [(70,0.25),(143,0.45),(216,0.2)]:
    for r in (34,24,14): ax3.add_patch(Circle((x,66),r,fc="#ffcf8a",ec="none",alpha=a*0.5))
# rose: six-fold
cx,cy,R=143,66,26
ax3.add_patch(Circle((cx,cy),R,fc="none",ec=WAL,lw=1.6))
for k in range(6):
    a=np.radians(60*k+90)
    ax3.add_patch(Circle((cx+R*0.5*np.cos(a),cy+R*0.5*np.sin(a)),R*0.5,fc="none",ec=WAL,lw=1.1))
ax3.add_patch(Circle((cx,cy),R*0.22,fc="none",ec=WAL,lw=1.1))
ax3.plot([6,280],[20,20],color=CORAL,lw=0.9)
ax3.text(143,151,"C · lid inner face: cloth, one six-fold rose (the cathedral's rose window to Big Energy's lancets;",ha="center",fontsize=8)
ax3.text(143,144,"a lute's rose; six strands of floss), a single coral thread woven across, glow behind",ha="center",fontsize=8)
ax3.text(143,-11,"the rose sits over the driver; the passive radiator behind plain cloth (no hole needed)",ha="center",fontsize=7,color=GREY)

# ---------- D: lighthouse characteristics for the one status light ----------
ax4 = fig.add_axes([0.50, 0.05, 0.48, 0.40]); ax4.axis("off"); ax4.set_xlim(0,100); ax4.set_ylim(0,100)
ax4.text(0,94,"D · one status light that speaks in lighthouse 'characters' (each state has its own rhythm, like a chart's Fl(2) 10s)",fontsize=8.5)
rows=[("ready","F  (fixed, dim green)",[(0,100)]),
      ("low battery","Fl(2) 10s  (two short flashes every 10 s, amber)",[(0,3),(6,9)]),
      ("charging","Iso 4s  (equal on / off, slow)",[(0,20),(40,60),(80,100)]),
      ("echo synced to MIDI clock","Q  (quick flash on each beat)",[(0,3),(25,28),(50,53),(75,78)]),
      ("a knob not in control (MIDI moved it)","Oc  (on, with one short eclipse)",[(0,45),(50,95)]),
      ("set is holding","the set button's own coral dot, fixed",[(0,100)])]
for k,(st,ch,segs) in enumerate(rows):
    y=80-k*12
    ax4.text(0,y,st,fontsize=7.5)
    ax4.text(0,y-4,ch,fontsize=6.8,color=GREY)
    ax4.add_patch(Rectangle((50,y-3),48,4,fc="#e6e0d4",ec="none"))
    for a,b in segs: ax4.add_patch(Rectangle((50+48*a/100,y-3),48*(b-a)/100,4,fc=(CORAL if "set" in st else "#7bd389" if k in (0,3) else "#e8b34a"),ec="none"))
ax4.text(50,86,"one 10 s cycle →",fontsize=6.5,color=GREY)
ax4.text(0,4,"Rule: the lantern never signals state; it only shows the sound moving. States live on the status light.",fontsize=7.5,color=CORAL)

fig.text(0.03,0.975,"floss · jam turn 2 · visual · rough sketches, not layouts (2026-11-22)",fontsize=11,weight="bold")
fig.savefig("/home/claude/big-energy/floss/design/sketches/visual-jam1-sail.png",facecolor=fig.get_facecolor())
print("ok")
