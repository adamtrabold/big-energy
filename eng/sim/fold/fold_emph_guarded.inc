* =====================================================================================
* GOLDEN adapter: wraps the CA-72 transcription (github.com/idlefoundry/ca-72, GPL-3.0)
* behind DUT-neutral subcircuit interfaces. Used ONLY as a verification oracle.
* ${CA72} is substituted by run_all.py with the absolute path of the read-only clone.
*
* A DUT adapter (our KiCad export) must define the same five subcircuits with the same
* ports. Parameters may differ (each adapter owns its own trims/calibration).
*
*   dut_vco     kbd rng width ramp saw tri rect vp vn
*   dut_vcf     ain cut amt out vp vn          params: r14 (EMPHASIS rheostat, ohm)
*   dut_contour gate fout lout vp15 vp10 vn10  params: fa fd fs la ld ls decay_on
*   dut_vca     vin cont out vp vn
* =====================================================================================
.include ${CA72}/circuits/models/mm-devices.lib
.include ${CA72}/circuits/models/ua741.lib
.include ${CA72}/circuits/boards/board1-vco.lib
.include ${CA72}/circuits/boards/board1-refs.lib
.include ${CA72}/circuits/boards/board4-vcf.lib
.include ${CA72}/circuits/boards/board2-contour.lib
.include ${CA72}/circuits/boards/board4-vca.lib

* -------------------------------------------------------------------------------------
* Oscillator 1 with its board-level input resistors (Fig. 9-3; CA-72 docs/circuit/board1.md)
*   kbd   keyboard CV (V), 84.8 mV/key in CA-72's calibration (1.0176 V/oct)
*   rng   range-switch tap voltage: -5 V - octave_step * (octaves below 2')
*   width rectangle width bias node (bench supplies the switch-pole divider)
* Trims default to CA-72's committed Folkman-1973 calibration
* (circuits/boards/reference/vco1-tracking.json): r11 183.63 ohm, a8 0.13518, tune 7.5315 V.
* Pitch wheel at detent (+6.12 V via R12), MOD bus grounded (A21), EXT input at 0 V as in CA-72's calibration bench (on the instrument the empty-jack
* bus sits at +0.0669 V, board1.md item 4; CA-72 tunes with 0 V, so we do too).
* -------------------------------------------------------------------------------------
.subckt dut_vco kbd rng width ramp saw tri rect vp vn
+ params: r11=183.6307 a8=0.135178 tc20=3.5e-3 tune=7.531474 bend=6.12
xrefs  vp vn m5 m5 m4 mm_refs
rstring m5 vn 167
vbend  nbend 0 {bend}
vtune  ntune 0 {tune}
vext   next 0 0
r12  nbend sum 150k
r21  ntune sum 560k
r27  kbd   sum 51.1k
r32  0     sum 51.1k
r38  next  sum 50.5k
r43  rng   sum 15k
x1 sum pos sum ramp buf saw tri rect width vp vn m5 m4 mm_vco r11={r11} a8={a8} tc20={tc20}
.ends dut_vco

* -------------------------------------------------------------------------------------
* Filter with its front-panel control-node resistors (board4.md item 2):
*   cut   CUTOFF control voltage (-10..+10 V) through R55 200K
*   amt   AMOUNT OF CONTOUR wiper (into R74 47K, on the board)
*   r14   EMPHASIS, 50K reverse-audio pot used as a rheostat (50K = dial 0)
* KEYBOARD CONTROL resistors R53 300K / R54 150K to 0 V (keyboard CV = 0), FILTER MOD R52 33K
* grounded (A21), EXT FILTER jack R51 100K grounded (A5).
* Trims: Folkman-1973 factory result per CA-72 board4.md: R39 0.632, R49 327 ohm, R73 0.783.
* -------------------------------------------------------------------------------------
.subckt dut_vcf ain cut amt out vp vn params: r14=50k r39=0.632 r49=327 r73=0.783
r55  cut ctl 200k
r53  0 ctl 300k
r54  0 ctl 150k
r52  0 ctl 33k
r51  0 ctl 100k
* FOLD: EMPHASIS rheostat in the base, both ends crossing a 100 mm hinge ribbon.
* per-conductor C to guard grounds 1e-11, emo-emi mutual 5e-13, 28 AWG + loop L 1e-07
x1 ain ctl amt emo emi out vp vn mm_vcf r39={r39} r49={r49} r73={r73}
lco emo emo_b 1e-07
rco emo_b emo_c 0.03
lci emi emi_b 1e-07
rci emi_b emi_c 0.03
cgo1 emo 0 5e-12
cgo2 emo_c 0 5e-12
cgi1 emi 0 5e-12
cgi2 emi_c 0 5e-12
cm1 emo_c emi_c 5e-13
rr14 emo_c emi_c {max(r14,1e-3)}
.ends dut_vcf

* -------------------------------------------------------------------------------------
* Both contour generators with their panel controls (CA-72 ca72-lab contour bench wiring):
*   gate  logic gate, >0.5 V = key held. Closes the key contact (+10 V bar -> trigger bus),
*         with board 2's keyboard-circuit load on the bus (R65 5.1K, R34 100K, C13 .01u).
*   fa fd la ld   ATTACK / DECAY rheostats, ohm (1M audio pots)
*   fs ls         SUSTAIN 5K linear wiper position 0..1 (+10 V to ground)
*   decay_on      1: DECAY switch on (release follows DECAY); 0: dump through 1.5K to V-trig
* -------------------------------------------------------------------------------------
.subckt dut_contour gate fout lout vp15 vp10 vn10
+ params: fa=100k fd=100k fs=1 la=100k ld=100k ls=1 decay_on=1
skey vp10 trig gate 0 swkey
.model swkey sw(vt=0.5 vh=0.1 ron=1 roff=1e12)
r65 trig t2 5.1k
r34 t2 vn10 100k
c13 t2 vn10 0.01u
rstrig strig 0 1e12
rfatt fatt fcap {max(fa,1)}
rfdec fdec fcap {max(fd,1)}
rlatt latt lcap {max(la,1)}
rldec ldec lcap {max(ld,1)}
r18t vp10 fsus {max(5k*(1-fs),1e-3)}
r18b fsus 0    {max(5k*fs,1e-3)}
r19t vp10 lsus {max(5k*(1-ls),1e-3)}
r19b lsus 0    {max(5k*ls,1e-3)}
rfin_f ffin vtrig 1m
rfin_l lfin vtrig 1m
r1401f fdump vtrig {decay_on > 0.5 ? 1e12 : 1.5k}
r1401l ldump vtrig {decay_on > 0.5 ? 1e12 : 1.5k}
x1 trig strig vtrig fatt fcap fdec fdump ffin fsus fout latt lcap ldec ldump lfin lsus lout
+ vp15 vp10 vn10 mm_contour2
.ends dut_contour

* -------------------------------------------------------------------------------------
* VCAs + output stage. EXT LOUDNESS jack empty (J3 ties it to +10 V via 33K), A-440 off,
* main output into a 10K load (CA-72 voice output convention). R2 = 160K (Folkman 1973 kit,
* CA-72's default; Fig. 9-11 has 82K - owner decision Q6 in our architecture).
* -------------------------------------------------------------------------------------
.subckt dut_vca vin cont out vp vn params: r2=160k
vj3  nj3 0 10
rj3  nj3 ext 33k
va440 na440 0 0
rload out 0 10k
x1 vin cont ext na440 out nphones vp vn mm_vca r2={r2}
rph nphones 0 10k
.ends dut_vca
