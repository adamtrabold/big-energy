import math, itertools
# shared 276-wide frame (ONE SHEET). HUSH +7 (290), FOLD +5 (286)
KN=7.45; CUT=10.4; TGL=4.6; STK=6.0; LED3=1.5; LED5=2.5
P=68; V1=100; V2=123; HB=85.4   # rows, horizontal break
items=[ # name,x,y,r,kind
("BEND stick",20,P,STK,"stick"),("MOD",42,P,KN,"k"),("MOD MIX",62,P,KN,"k"),
("OSC MOD",78,P,TGL,"t"),("FILTER MOD",92,P,TGL,"t"),("GLIDE",108,P,KN,"k"),
("CUTOFF",140,P,CUT,"k"),("not-in-ctl",152,79,LED3,"l"),("EMPHASIS",164,P,KN,"k"),("CONTOUR AMT",188,P,KN,"k"),
("KBD CTRL",204,P,TGL,"t"),("VEL",220,P,TGL,"t"),("VOLUME",243,P,KN,"k"),("status",262,P,LED5,"l"),
("TUNE",18.5,V1,KN,"k"),
("RANGE 1",38.5,V1,KN,"k"),("WAVE 1",38.5,V2,KN,"k"),("RANGE 2",58.5,V1,KN,"k"),("WAVE 2",58.5,V2,KN,"k"),
("RANGE 3",78.5,V1,KN,"k"),("WAVE 3",78.5,V2,KN,"k"),("FREQ 2",98.5,V1,KN,"k"),("FREQ 3",98.5,V2,KN,"k"),
("OSC 3 CTL",114.5,V2,TGL,"t"),
("OSC 1",137,V1,KN,"k"),("OSC 2",137,V2,KN,"k"),("OSC 3",157,V1,KN,"k"),("NOISE/EXT",157,V2,KN,"k"),("SOURCE",173,V2,TGL,"t"),
("F ATTACK",197,V1,KN,"k"),("F DECAY",217,V1,KN,"k"),("F SUSTAIN",237,V1,KN,"k"),
("L ATTACK",197,V2,KN,"k"),("L DECAY",217,V2,KN,"k"),("L SUSTAIN",237,V2,KN,"k"),("DECAY tgl",253,V2,TGL,"t"),
]
vbreaks_play=[122.5,228]; vbreaks_voice=[122.5,181]
rounds=[i for i in items if i[4] in("k",)]; tg=[i for i in items if i[4]=="t"]
print("rounds on panel",len(rounds),"(+0; MOD included) toggles",len(tg))
bad=0
for a,b in itertools.combinations(items,2):
    d=math.dist(a[1:3],b[1:3])
    if a[4]=="k" and b[4]=="k" and a[2]==b[2]:
        need=24 if {a[0],b[0]}<= {"CUTOFF","EMPHASIS","CONTOUR AMT"} else 20
        if d<need-1e-6: print("PITCH",a[0],b[0],d); bad+=1
    gap=d-a[3]-b[3]
    if gap<1.5: print("GAP",a[0],b[0],round(gap,2)); bad+=1
for n,x,y,r,k in items:
    bl=vbreaks_play if y<HB else vbreaks_voice
    need=7 if k in("k","stick") else 3 if k=="t" else 1
    for b in bl:
        if abs(x-b)-r<need-1e-6: print("BREAK",n,b,round(abs(x-b)-r,2)); bad+=1
    if abs(y-HB)-r<need-1e-6: print("HBREAK",n,round(abs(y-HB)-r,2)); bad+=1
    if x-r<10 or 276-(x+r)<10: print("EDGE",n,x-r,276-x-r); bad+=1
print("violations",bad)
print("min knob x-edge",min(x-r for n,x,y,r,k in items),"max",max(x+r for n,x,y,r,k in items),"back edge",V2+KN)
print("reach stick->CUTOFF",math.dist((20,P),(140,P)))
for n,x,y,r,k in items: print(f"{n:12s} {x:6.1f} {y:6.1f}  HUSH x {x+7:6.1f}  FOLD x {x+5:6.1f}")
