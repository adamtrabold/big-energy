# Cooler / more interesting clone candidates (lens: character, unusual architecture, portable playful object)

Status: rev 0, 2026-11-13. Research pass for the owner's ask: "explore if there would be easier / cheaper / cooler synth clones to make with these principles". This file covers the **cooler** lens only.
Compared against: `explore/principles.md` and `eng/budget-variant.md` (Little D ≈ $244–311 core one-unit; principles.md quotes the full build at ≈ $311–448).

Conventions: [src] = read this session. **UNVERIFIED** = from memory, or a source exists but I did not confirm the figure. **ESTIMATE** = my number. [ENG] = engineering judgement.

---

## Ranking (cooler)

| # | Candidate | One-line why | Fit to principles | Cost vs Model D build (ESTIMATE) |
|---|---|---|---|---|
| 1 | **Synthi AKS-style "matrix lunchbox"** | The original portable synth: a pin matrix, a joystick and three wild oscillators. Autotune fixes its biggest historic flaw | High. A joystick is already in the spec; Daisy reverb replaces the spring | ≈ 1.2–1.6× (the matrix is the cost driver) |
| 2 | **Music Easel-style west-coast portable** | Complex oscillator, wavefolding timbre, and vactrol low-pass gates that "plonk". Born portable, with battery terminals | Medium-high. Keys replace the touch plate; LPGs need no calibration | ≈ 1.1–1.5× |
| 3 | **Polivoks-style duophonic** | Soviet, gritty, aggressive filter built from programmable op-amps. Two VCOs, duo mode | High. Smaller than the Model D. Daisy autotunes 2 VCOs | ≈ 0.8–1.0× |

Honourable mentions, detailed below: MS-20 (strong #4), Oberheim SEM, ARP Odyssey, Steiner-Parker, EDP Wasp, Yamaha CS-01, Roland SH-101 (fails through-hole).

---

## 1. EMS Synthi AKS (briefcase, pin matrix)

**What makes it cool.** It is the original "synth in a case": 3 oscillators, a noise source, a ring modulator, a diode-ladder filter, a trapezoid envelope, a joystick, and a pin matrix where any source patches to any destination. Behringer said it spent a year designing and tooling its matrix, using "gold-played pins with built in resistors" [src: [gearnews 2020](https://www.gearnews.com/behringer-pin-matrix-board-for-synthi-clone-is-coming-along)]. Its full VCS3 project now looks stalled, and the speculation is "It's not the synth voice, but the pin matrix" [src: [synthanatomy 2025-10](https://synthanatomy.com/2025/10/has-behringer-canceled-the-long-awaited-vcs-3-and-pro-16-synth-projects.html)]. What shipped instead is the AKS Mini: 27 keys, 3 shared-control oscillators, no matrix mentioned, €119 [src: [synthanatomy 2026-07](https://synthanatomy.com/2026/07/behringer-aks-mini-project-a-portable-1-oscillator-vcs-3-style-synthesizer.html)]. **So a portable, keyed Synthi with a real matrix does not exist at a sane price.** That is the gap.

**Why the principles shine here.**
- **Autotune solves the Synthi's famous tuning problem.** SoS notes the original's unbuffered matrix could affect oscillator tuning [src: [SoS Syntrx review](https://www.soundonsound.com/reviews/erica-synths-syntrx)]. VCOs 1–2 have only a 100R exponential-tracking trimmer, and VCO3 has none [src: [Hinton](https://hinton-instruments.co.uk/ems/emsmisc.html)]. Daisy autotune with per-octave tables makes it playable from keys.
- **The joystick is already in the spec.** Promote it to a 2-axis matrix source (X/Y), as on the original.
- **Daisy reverb stands in for the AKS spring reverb** (spring "type" in the FX menu). [ENG]
- **"Controllable DRIFT" is very on-brand** for a Synthi.

**Matrix options** (the key design decision):
- (a) A real pin matrix. A Ghielmetti Type 621 20×20 is ≈ €370 new [src: [dsl-man Synthi A clone](https://dsl-man.atlassian.net/wiki/spaces/DSO/pages/1147091/EMS+Synthi+A+Clone)]. Too dear, and too big for an OP-1 footprint.
- (b) A DIY pin matrix: two perfboard layers with headers, and pins made of a resistor inside a tube. UNVERIFIED feasibility and cost; this would be a makerspace project in itself.
- (c) A **digital matrix**. An LED grid plus encoders, with Daisy setting analog switches (DIP CD4066/DG4xx class) and the audio staying analog. This is what Erica's Syntrx does: an LED grid, encoders, 256 stored matrix patches, and level steps by repeated click [src: SoS Syntrx]. That gives preset recall and MIDI, but loses the tactile pins. A 16×16 crosspoint from DIP switches is ≈ 64 × 4066 at 4 switches each; **too many parts**. Shrinking to ≈ 8×10 is realistic. [ENG/ESTIMATE]
- Recommendation: a hybrid. A **small physical pin matrix (≈ 10×8) using cheap DIY pins** for the tactile core, plus Daisy-side "virtual pins" for modulation into the DIGITAL FX.

**Schematic / reference.**
- Clone PCB sets exist. phutney.com sold a 3-PCB kit at €85, with known substitutes [src: dsl-man Synthi A clone]:
  - 2C746 → LM394/2N2916;
  - TAB101 → CA3046 on an adapter;
  - ME9002 → BSX20/2N2369;
  - DK10 → 1N34A.
- The "Cloney / Synthey AKS" kit exists, but its guides are restricted to registered owners, and the page was "CLEANED UP due to copyright claims March2026" [src: [dsl-man Cloney](https://dsl-man.atlassian.net/wiki/spaces/DSO/pages/1147606/The+Cloney+project+Synthey+AKS+clone)]. **This is a legal signal.**
- Original EMS service schematics circulate online. UNVERIFIED source and licence.

**Simulation.** There is no CA-72-equivalent full-board ngspice model (none found). The VCS3 VCF has a published nonlinear model that was checked against a PSpice simulation of the same structure (Civolani & Fontana, DAFx-2008) [src: [DAFx](https://dafx.de/paper-archive/details/y9N6dG2Rw_L1-hVzFviCrw)]. A 2026 DAFx paper on a reduced VCS3 diode ladder exists but was not read: UNVERIFIED [link: [DAFx26 p29](https://www.dafx.de/paper-archive/2026/papers/DAFx26_paper_29.pdf)]. **We would have to build the golden SPICE model ourselves**, which costs more verification effort than the Model D did.

**Key parts (through-hole).** All are discrete transistors, a CA3046-class array (Little D already uses the AS3046), op-amps, and germanium diodes. There are no unobtainable custom ICs. The LM394 is obsolete (UNVERIFIED stock); THAT300 or a matched-pair substitute is the fallback.

**Calibration vs autotune.** The VCOs gain the most from autotune. The trapezoid envelope and the filter have trims, but these are not pitch-critical.

**Portability.** It is the archetype. An OP-1 footprint needs the matrix shrunk. [ENG]

**Legal.** EMS still trades and sells new Synthis (SoS: just under £6,000 with a waiting list) [src: SoS Syntrx]. **Do not use "EMS", "Synthi", "VCS3" or "AKS".** Erica's legally distinct approach was new circuitry inspired by the concept [src: SoS Syntrx]. The March 2026 copyright cleanup on the Cloney page suggests EMS-derived documentation is actively policed: **use it for personal one-off only, and do not publish layouts**. UNVERIFIED legal reading; not legal advice.

**Complexity / cost.** It has more modules than the Model D: 3 VCOs, a ring mod, an envelope, the matrix, and the joystick. The matrix adds ≈ $40–150 depending on the option. ≈ 1.2–1.6× the Model D build. ESTIMATE.

**Pitch.** *A lunchbox with a joystick and a little grid of pins. Push a pin to send VCO3 into the filter, wiggle the stick, and the whole thing howls into a Daisy plate reverb. It is in tune every time you switch it on, which no Synthi ever was. Part instrument, part puzzle, the most "hand-built object" thing you could carry.*

---

## 2. Buchla Music Easel (208 + 218)

**What makes it cool.** It is the west coast portable:
- a complex oscillator with timbre/wavefolding;
- a balanced (ring) modulator;
- vactrol low-pass gates that give acoustic, percussive "plonk";
- a pulser/envelope;
- a 5-step sequencer;
- a touch-plate keyboard;
- stored program cards.

Buchla USA still sells it: $4,999 in 2023, with the 218 "Touch Activated Voltage Source" [src: [synthtopia 2023](https://www.synthtopia.com/content/2023/05/11/buchla-usa-intros-music-easel-50th-anniversary-music-easel/)]. The original "was designed with battery terminals … as portable as any acoustic instrument" [src: same].

**Fit.**
- The LPGs (vactrols) are **calibration-free in practice**, and the sound is forgiving of drift.
- The complex oscillator is roughly 1.2 V/oct, and the DIY notes include resistor changes for 1–1.2 V/oct [src: [dsl-man 208 clone](https://diysynth.wiki.dsl-man.de/wiki/spaces/DSO/pages/1147560/Buchla+208+Clone)]. **Autotune makes the scaling irrelevant**: Daisy learns whatever law it gets.
- Daisy echo/reverb on vactrol plucks is a classic pairing. [ENG]
- **Keys conflict:** the Easel identity is the touch plate. The spec's Choc + Hall keys with a pressure strip can sit where the 218 sits. Velocity maps naturally to LPG strike level and aftertouch to timbre. [ENG]

**Schematic / reference and clones.**
- 208R (Roman F.) PCBs via Electric Music Store, 208P (Papz) via Portabellabz, and full kits from samodular [src: dsl-man 208 clone].
- A "DIY 208r Music Easel clone front panel & PCB" listing [src: [reach.dog](https://reach.dog/shop/tone-tweakers-inc/products/diy-208r-music-easel-clone-front-panel-pcb)].
- Aaron Lanterman (Georgia Tech) publishes Easel-derived PCBs, **with Don Buchla's permission**, and points to the original Easel schematics [src: [Lanterman](https://lanterman.ece.gatech.edu/?p=43)].
- A DIY mod expander adds a sequencer, LFO and ADSR [src: [CDM 2022](https://cdm.link/2022/07/the-classic-buchla-208-music-easel-gets-a-new-diy-expansion-and-it-can-sound-totally-evil/)].

**Simulation.** No open full-board SPICE model found. Lanterman's per-board adaptations are a good start for hand-built ngspice decks. Vactrols need a behavioural model (LDR + LED time constants), which is UNVERIFIED accuracy.

**Key parts.**
- Vactrols: Xvive VTL5C3 and VTL5C3/2 are current production and through-hole, from $6.50 [src: [tubesandmore](https://www.tubesandmore.com/products/vactrols)].
- Op-amps: the RC4558 tested OK [src: Lanterman].
- Otherwise discrete transistors and arrays. No unobtainable ICs known. UNVERIFIED for every card.

**Calibration vs autotune.** Autotune covers the oscillators. The LPGs and wavefolder are "set by ear" trims.

**Portability.** Excellent. It was designed for it.

**Legal.** Buchla USA actively sells the product. **Do not use "Buchla" or "Music Easel"**, and do not copy the panel art. Lanterman's permission covers his adaptations, not ours. Personal one-off only. UNVERIFIED legal reading.

**Complexity / cost.** The 208 is 12 cards [src: dsl-man 208 clone], dense but each simple. ≈ 1.1–1.5×. ESTIMATE.

**Pitch.** *Play a key and it doesn't "beep", it rings: a struck, woody, bell-like note that decays into a Daisy echo. Lean into the pressure strip and the timbre folds open. Flip on the 5-step sequencer and the pulser and it plays itself while you drift the timbre. This is the most musical of the three for ambient and songwriting, and nothing like the Model D.*

---

## 3. Polivoks (USSR, Vladimir Kuzmin)

**What makes it cool.** It is duophonic, with:
- 2 VCOs with cross-mod;
- a LP/BP filter;
- 2 ADSRs with AD looping;
- an LFO [src: [SoS Polivoks Pro](https://www.soundonsound.com/reviews/polivoks-pro)].

The filter integrators are **programmable op-amps (K140UD12 ≈ uA776)**, with resonance partly set by the op-amp's current limit and clamping diodes. It is known for "distorted, dirty and gritty behavior", and without limiting it self-oscillates rail to rail [src: [Kuzmin VCF page](https://modularsynthesis.com/kuzmin/polivoks/polivoks_vcf.htm)]. Punk, acid and industrial character in a small package.

**Fit.**
- Two VCOs suit autotune well; it is the same Daisy job as Little D minus one VCO.
- The filter **drifts with temperature but stabilises when warm** [src: Kuzmin page]. Autotune covers pitch, and a HARD/SOFT resonance switch (the author's mod) tames it [src: same].
- Duo mode adds playing interest at near-zero cost: Daisy handles 2-note allocation. [ENG]

**Schematic / reference and clones.**
- The modularsynthesis.com page documents the VCF with tested substitutes [src: Kuzmin page].
- Erica Synths sold a DIY Polivoks VCF II, now discontinued [link: [Erica](https://www.ericasynths.lv/shop/discontinued-products/diy-polivoks-vcf-ii/)].
- Synthrotek has a DIY Polivoks VCF 2 [link: [ModularGrid](https://modulargrid.com/e/modules/view/40675)].
- Full-synth service schematics circulate. UNVERIFIED.

**Simulation.** No open SPICE model found. A uA776/LM4250-class programmable op-amp macromodel would be needed (UNVERIFIED availability). Moderate effort.

**Key parts.**
- **NTE888M** (uA776 replacement, 8-pin DIP) "work[s] equally well", at under $2 per the author [src: Kuzmin page]. Vetco lists it [link: [Vetco](https://vetco.net/products/low-power-programmable-op-amp-8-pin-dip-nte888m)]. Stock and price are UNVERIFIED.
- Risk: NTE is a relabeller, so this is effectively single-source. Buy spares. LM4250 as an alternative is UNVERIFIED.
- The rest is TL07x and 2N3904-class parts.

**Calibration vs autotune.** VCOs via autotune. The filter needs a 1 V/oct trim (R9 175k + 100k trim) [src: Kuzmin page] if keytracking matters.

**Portability.** Compact architecture. The original was fragile [src: SoS]; ours would not be.

**Legal.** polivoks.pro sells a reissue (€1,650, built with ≈ 85% Soviet NOS parts) [src: SoS]. **Do not use the "Polivoks" name.** Soviet-era schematics are unlikely to be actively policed, but this is UNVERIFIED.

**Complexity / cost.** Fewer modules than the Model D: 2 VCOs and 1 filter. ≈ 0.8–1.0×. ESTIMATE.

**Pitch.** *A small, mean, duophonic box. Hold two keys and the oscillators split. Crank resonance and the filter snarls and clips like a broken radio, then the Daisy tape echo smears it. It's the cheapest of the three and the one most likely to make people laugh when they hear it.*

---

## Honourable mentions

| Candidate | Cool factor | References / clones | Key parts | Why not top 3 |
|---|---|---|---|---|
| **Korg MS-20** | Dual HP+LP filters that scream, a patch panel, an ESP (pitch-to-CV) input | RS-20 (René Schmitz) and KS-20 (Kassutronics) transistor + op-amp filter clones, with stripboard layouts by LMNC [src: [synthdiy wiki](https://wiki.synthdiy.com/modules/vcf/ms-20-filter/)]. Korg's own kit has both filter revisions on an internal switch [src: [synthtopia 2014](https://www.synthtopia.com/content/2014/01/23/korg-ms-20-kit-lets-you-build-a-full-size-analog-monophonic-synth-classic/)] | Discrete, TL07x. Late OTA rev needs a 13700: DIP from XINLUDA/HGSEMI on LCSC; TI DIP discontinued [src: [synthdiy OTAs](https://wiki.synthdiy.com/parts/otas)] | Strong #4. Very well trodden; Korg (and Behringer K-2, UNVERIFIED) already cover it cheaply, so it is less "unusual" |
| **Oberheim SEM** | 12 dB state-variable filter with LP→notch→HP sweep | Many SEM VCF clones (Synthcube etc.) [link: [ModularGrid](https://modulargrid.net/e/synthcube-sem-vcf-)] | CA3080 → **AS3080 DIP-8, current** [src: [Erica 2022](https://www.ericasynths.lv/news/post/as3109-as3080-now-available/)] | Gorgeous, but polite. Best as a **filter option** in another build. Oberheim name is trademarked (UNVERIFIED owner) |
| **ARP Odyssey** | Duophonic, sync/ring mod, 3 filter revisions (4023/4035/4075) | AMSynths Athena: Odyssey-inspired, 4075 standard, 4023/4035 options [src: [matrixsynth 2013](https://www.matrixsynth.com/2013/12/new-amsynths-athena-arp-odyssey-clone.html?m=0)] | Discrete, OTA VCA | Slider-heavy panel is a poor OP-1 fit. Korg owns ARP (UNVERIFIED) |
| **Steiner-Parker Synthacon** | Diode-string multimode (LP/BP/HP/AP) filter, nasty and unique | Elektor Labs extended Synthacon (free for private DIY) [src: [Elektor](https://www.elektormagazine.com/labs/extended-steiner-parker-synthacon-vcf)]. Yusynth-derived Eurorack build [src: [modlfo](https://modlfo.github.io/projects/vult-analog-steiner-parker)] | CA3046/LM3046, 13700/CA3080A, matched BAV99 [src: Elektor] | The full Synthacon synth's references are thin (UNVERIFIED). **Best as a filter swap** in Polivoks- or Little D-style builds |
| **EDP Wasp** | Battery (6 × C), speaker, 25 flat capacitive keys, a 1978-ish oddball (UNVERIFIED year) [src: [matrixsynth](https://www.matrixsynth.com/2008/09/edp-wasp-with-schematics-and-patch.html)] | Jasper and Pixie clones [src: [Elby Pixie](https://www.elby-designs.com/contents/en-us/d11.html)]. CD4069 Wasp filter [src: [schmitzbits](https://schmitzbits.de/wasp.html)] | CD4069UB, single 5 V | **DCO oscillators** (not an analog voice); better for the "cheaper" lens |
| **Yamaha CS-01** | Battery mono, speaker, 32 mini keys, breath control (BC1 to VCF/VCA), 1.5 kg [src: [E&MM 1982](https://www.muzines.co.uk/articles/yamaha-cs-01-breath-control-synthesiser/4350)] | No open clones found | Unknown (UNVERIFIED) | Single VCO, so thin character. **Steal the idea:** a breath-sensor jack (Daisy ADC → VCF/VCA) is a cheap add-on to any candidate |
| **Roland SH-101** | Keytar-portable, battery, mod grip | AS3109 replaces the IR3109 | **AS3109 is SOIC-16 only** [src: Erica 2022] | Breaks through-hole unless a ready-made adapter counts (owner call) |

---

## Cross-cutting notes
- **None of the three has a CA-72-style open full-board SPICE model.** "Verification-first" means building our own golden ngspice decks from the schematics. Budget roughly 1.5–2× the Model D verification effort (ESTIMATE). Polivoks is the smallest to model.
- **Trademarks:** all three originals are sold today under their names (EMS, Buchla USA, polivoks.pro). Use new names and panel art. Personal one-off builds of published circuits are common practice, but layouts derived from restricted kits (Cloney) should not be published.
- **Mix-and-match is possible.** A Polivoks voice with a small pin matrix and a joystick would be cheap and wild. [ENG]
