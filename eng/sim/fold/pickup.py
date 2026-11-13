#!/usr/bin/env python3
"""FOLD: scan-tone pickup on the EMPHASIS lines crossing the hinge ribbon.
Aggressor: 3.3 V, 4 kHz square (mux select S3-class), 1 us edges, coupled by Cc into a node (top-level "ain" or "xf.emi_c" / "xf.emo_c"),
i.e. the base-side end of a crossing line. No audio in. Output: 4 kHz level at the filter out, and
dB relative to the output for a 1 V-peak 400 Hz tone into one 33K mixer channel."""
import subprocess, numpy as np, sys
from pathlib import Path
H=Path(__file__).resolve().parent; W=H/'work'; W.mkdir(exist_ok=True)
CA72=(H/'../../../ref/ca-72').resolve()
def r14(d): p=min(max(d/10,0),1); return 50e3*(81**(1-p)-1)/80
def run(adapter, name, cut, dial, cc, node, src="0"):
    inc=W/f'{adapter}.inc'; inc.write_text((H/f'{adapter}.inc').read_text().replace('${CA72}',str(CA72)))
    agg = f"vag ag 0 pulse(0 3.3 2m 1u 1u 124u 250u)\ncag ag {node} {cc}" if cc>0 else ""
    cir=f"""* pickup
.include {inc}
.options reltol=1e-4 abstol=1e-12 vntol=1e-7 method=gear maxord=2
vp vp 0 10
vn vn 0 -10
vcut cut 0 {cut}
vsrc src 0 {src}
rmix src ain 33k
rbus ain 0 5.5k
vamt amt 0 0
xf ain cut amt out vp vn dut_vcf r14={r14(dial):.4g}
{agg}
.control
set wr_singlescale
set wr_vecnames
tran 0.2u 32m 0 0.2u
wrdata {name}.dat v(out)
quit
.endc
.end
"""
    (W/f'{name}.cir').write_text(cir)
    subprocess.run(['ngspice','-b',f'{name}.cir'],cwd=W,capture_output=True,timeout=900)
    d=np.loadtxt(W/f'{name}.dat',skiprows=1); t,y=d[:,0],d[:,1]
    tt=np.arange(12e-3,32e-3,1/400e3); yy=np.interp(tt,t,y); yy-=yy.mean()
    Y=np.abs(np.fft.rfft(yy*np.hanning(len(yy))))*4/len(yy); f=np.fft.rfftfreq(len(yy),1/400e3)
    return f,Y
if __name__=='__main__':
    f,Y=run('fold_emph_guarded','ref',6,0,0,'emi_c',src="sin(0 1 400)")
    ref=Y[np.argmin(abs(f-400))]; print(f"reference 400 Hz out {ref*1e3:.1f} mV peak")
    for ad in ('fold_emph_guarded',):
      for cut,dial in [(3.8,0),(3.8,7),(6,0),(6,7)]:
        for node,cc in [('xf.emi_c',4e-12),('xf.emi_c',0.4e-12),('xf.emo_c',4e-12),('xf.emo_c',0.4e-12),('ain',0.4e-12)]:
          f,Y=run(ad,f'p_{cut}_{dial}_{node}_{cc:.0e}',cut,dial,cc,node)
          a=max(Y[np.argmin(abs(f-k))] for k in (4000,12000))
          a4=Y[np.argmin(abs(f-4000))]
          print(f"cut {cut:+} dial {dial} {node} Cc {cc*1e12:.1f} pF: 4k {a4*1e6:8.2f} uV  max(4k,12k) {a*1e6:8.2f} uV  {20*np.log10(a/ref):6.1f} dB re ref")
