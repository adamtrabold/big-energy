# Little D: velocity routing (loudness / filter / both) and bought-switch keys (v2)

Status: rev 1, 2026-11-12. Answers two owner decisions in `design/little-d/owner.md` (2026-11-12 answers):
- velocity: "Both, with a switch", so a switch selects loudness / filter / both;
- keys: "I don't want to build custom keys", then "Whatever the design needs", so keys use bought mechanisms with minimal assembly.

Conventions as `budget-variant.md`: a link means read this session. **ESTIMATE** = my number. **UNVERIFIED** = a
source exists but the figure isn't confirmed. **[ENG]** = engineering judgement. **[SIM]** = ngspice run this
session on the CA-72 golden netlists (files in `eng/sim/velocity/`).

## 0. Bottom line

- **Loudness:** velocity scales the **loudness contour** before the VCA, using the **spare half of the AS3360** that the
  locked bend/mod design already buys (§v1.5b). The original VCA and its EXT LOUDNESS normal are untouched.
  **Rejected:** driving the original second VCA stage (EXT LOUDNESS) with velocity. It works as a level control, but
  [SIM] a velocity step there makes a **0.13–0.22 V output thump**, 1.2–2× the **0.10 V** thump the loudness attack
  already makes (§1.3).
- **Filter:** velocity is added **in firmware to the existing CUTOFF CV** (a Pico channel that already exists). It
  costs **$0** in hardware.
- **Switch:** one sub-mini ON-OFF-ON toggle, **LOUD / BOTH / FILT**, read through a spare CD4067 channel. It uses no GPIO.
- **Velocity routing cost: ≈ +$2** (toggle, one TL072, passives). It needs **one extra PWM pin**, and no DAC channel
  (both MCP4822s are full).
- **Keys:** **25 Kailh Choc V2 silent (Deep Sea Mini) switches** soldered to the key strip, with **short pressed-on
  tops** (≤ 1.75u, so they don't rock) and a **K&J D31 magnet in each top over a flat TO-92S SS49E**. Recomputed for
  2.8 mm travel: **rest gap 5.6 mm, bottom gap 2.8 mm**, so the magnet face sits **7.6 mm above the strip at rest**
  (§2.2).
- **Key cost: ≈ $51–56 with bought acrylic, or $38–43 on scrap.** That is ≈ parity with the v1.10 row ($50–55). The
  +$0.50 is the sensor LDO, now counted.
- **Net change to the v1.10 totals: ≈ +$3**, giving (a) **≈ $258–323** and (b) **≈ $242–305**. Long piano tops with
  bought stabilisers would add **+$30**.

---

## 1. Velocity routing

### 1.1 Signal plan

```
                    Pico PWM "VEL" (10-bit, ~146 kHz) -> 2-pole RC (2 x 10k / 8.2n, ~1.9 kHz/pole)
                                                         -> divider to 0..~1.8 V -> AS3360 half B CV
loudness contour --+-- 5k dummy load (keeps the original loading) 
                   +-- R_in -> AS3360 half B (current in) -> TL072 I-V (Rf sets unity at full CV)
                        -> [TL072 half 2: inverter, only if the I-V output is inverted] -> R59 68k -> VCA (Q18), as original

CUTOFF CV (existing Pico channel) = knob/CC value + velocity offset (firmware)   -> filter control node, as now

LOUD/BOTH/FILT toggle -> 100k/100k divider at mid-rail -> spare CD4067 channel (36 of 48 used)
```

| Switch | VEL CV (loudness) | CUTOFF offset (filter) |
|---|---|---|
| **LOUD** | velocity curve | 0 |
| **BOTH** (centre) | velocity curve | velocity × span |
| **FILT** | full scale (= unity gain, so the original loudness path) | velocity × span |

- **Velocity is latched at each new trigger** (gate 0 → 1). Legato notes keep the last value, which is single-trigger
  behaviour. MIDI note velocity drives the same two values.
- **Loudness curve [ENG]:** the AS3360 is linear in CV, so the firmware maps velocity to gain on a dB curve with a
  floor (e.g. velocity 1 → −30 dB) so pp is never silent. The curve is a firmware setting.
- **Filter span [ENG]:** default full velocity = **+1.5 octaves** over the knob setting. Soft notes play at the knob
  setting. The offset goes on the **CUTOFF channel, not the keytrack DAC channel**: keytrack passes through the
  KEYBOARD CONTROL toggle (off / ⅓ / ⅔), so "off" would also mute velocity. Which Pico channel carries CUTOFF in v1
  (PWM, per Part 2 §2.2) is **UNVERIFIED**. Confirm it at schematic capture.
- **Why no DAC:** both MCP4822s are full (VCO 1–3 plus filter keytrack, `keys-answers.md` §4). A PWM is fine for a
  non-pitch CV. At 10-bit / 146 kHz, a 2-pole 1.9 kHz RC attenuates ripple ≈ (146/1.9)² ≈ 5,900×, about 0.5 mV p-p
  at 3.3 V. That is ultrasonic AM, inaudible. It settles to 1 % in ≈ 0.4 ms, so it adds no audible latency.
  1,024 steps is plenty for 127 velocities [ENG].

### 1.2 Why the loudness contour, not the VCA's own second stage

The original VCA is **two cascaded discrete pairs**:
- the first pair's tail is driven by the loudness contour (R59 → Q18);
- the second pair's tail is driven by **EXT LOUDNESS** (Q21), normalled to +10 V through 33 k by jack J3 (CA-72
  `board4-vca.lib`, drawn from service manual Fig. 9-11).

Velocity into EXT LOUDNESS looks free, but [SIM] says no (§1.3). Scaling the contour **before** Q18 is thump-free by
construction: at silence the contour is 0 V, and 0 × velocity = 0. The only residue is AS3360 CV feedthrough
(≤ 10 mV untrimmed, [Tubes and More](https://www.tubesandmore.com/products/integrated-circuit-as3360-dual-vca-alfa-14-pin-dip)).
Against a ≈ 6 V contour that is < 0.2 % of the attack's own thump [ENG].

**Interaction with the bend/mod cut:** §v1.5b offers an optional cut that wires the MOD dial passively and drops
the AS3360. **With velocity, that cut no longer saves the chip.** Both halves are then in use: half A for mod depth
(MIDI CC1), half B for velocity.

### 1.3 SPICE already run (CA-72 golden `mm_vca`, ±10 V, 1 kHz 0.5 V input)

| Test | Result | File |
|---|---|---|
| EXT LOUDNESS level vs CV (CV replaces J3's +10 V, through 33 k) | Output p-p: 10 V → 1.19, 8 → 0.93, 6 → 0.67, 4 → 0.41, 2 → 0.16, 1 → 0.035, 0.5 → 0.0004. **Linear above ≈ 0.8 V**, so it works as a level control | `ext_loudness_sweep.txt` |
| Velocity step 1 → 10 V (0.5 ms) into EXT LOUDNESS, contour 0 V, no audio | **Thump 0.22 V peak** at the reference 2nd-VCA BAL (r12 0.496); 0.32 V at r12 0.45; 0.66 V at 0.30. From 5 V start: 0.13 / 0.19 / 0.39 V | `vel_step_thump.txt` |
| Reference: loudness contour step 0 → 6 V (0.5 ms), EXT at normal, no audio | **0.10 V** (independent of r12) | `ref_contour_thump.txt` |

**Verdict:** routing velocity through EXT LOUDNESS adds 1.2–6× the instrument's inherent attack thump, depending on
trim, and Little D has no trim for the second pair. **Use contour scaling.**

### 1.4 SPICE verification still to do (reference harness `eng/sim/reference/`)

1. **Behavioural AS3360 half** in a voice-bench variant:
   - a B-source, I_out = (V_in / R_in) · g(V_cv), plus a feedthrough term of ±10 mV, non-linear in CV, sign swept;
   - placed between `dut_contour` lout and `dut_vca` cont, with the 5 k dummy load;
   - plus the PWM + RC source.
   - **Pass criteria:**
     - (a) at VEL = full, `compare.py` against `out/golden` passes on bass_pluck and resonant_sweep, so the original
       loudness behaviour is intact;
     - (b) VEL at 0.5 and 0.25 gives output RMS within ±0.5 dB of the target curve;
     - (c) thump with no audio and a VEL step at gate-on is ≤ golden + 10 %;
     - (d) PWM ripple at the VCA output < 10 µV rms (the E1 criterion).
2. **Contour loading:** `contour_tran` with R_in in parallel with the 5 k dummy on lout. **Pass:** contour metrics
   (attack/decay times, overshoot ratio) inside the compare.py tolerances.
3. **Filter offset:** `filter_ac` with the CUTOFF source stepped by the velocity span. **Pass:** +1.5 oct ±0.2 oct. A
   `voice_tran` case with the offset arriving through the real CUTOFF RC must reach 90 % within 2 ms of gate-on. If
   it doesn't, write the offset ahead of the gate, or speed up the CUTOFF RC.
4. **Scaling note:** CA-72 runs at ±10 V; Little D runs at ±9 V. Re-run 1–3 on the Little D adapter once it exists.

### 1.5 Parts and cost

| Item | Cost | Source |
|---|---|---|
| AS3360 half B | $0 (already in §v1.5b) | — |
| TL072 (I-V, plus inverter if needed) | $0.30 | Tayda, ESTIMATE as §v1.3 |
| RC (4 R, 2 film C), divider, R_in/Rf, 5 k dummy, toggle divider | ≈ $0.40 | Tayda passives, ESTIMATE |
| Sub-mini toggle **ON-OFF-ON**, PCB | ≈ $0.80–1.00 | ESTIMATE. The §v1.3 Tayda link is ON-ON; buy the ON-OFF-ON version |
| **Total** | **≈ +$1.50–1.70, call it +$2** | |

- **Panel:** 7 toggles, up from 6. Flag it to the design team (owner panel mocks).
- **GPIO:** +1 PWM. The v1 tally isn't re-done (UNVERIFIED). Part 2's ≈ 4 spare has been eaten by the 2nd DAC CS,
  the 3rd mux ADC, mod-VCA PWM and LM386 enable, so it is tight.
- **Optional upgrade:** velocity → filter **contour amount** (Voyager-style) instead of a cutoff offset. It needs a
  2nd AS3360 between the filter contour and the AMOUNT pot, same circuit as §1.1: **+$5–7** (AS3360 price
  UNVERIFIED). It isn't needed for the owner's ask.

---

## 2. Keys: bought switches, minimal assembly

### 2.1 What changes

The RAIL / FLOAT / COMB mechanisms are owner-built, so they are **out**. The base becomes §v1.4b route (b), simplified:

| | **K-v2 (recommended)** | Fallback: Gateron low-profile Hall |
|---|---|---|
| Mechanism | 25 **Kailh Choc V2 silent** (Deep Sea Mini): **2.8 ± 0.25 mm** total travel, actuation 1.3 mm, dampened both strokes, ≤ 35 dB with caps, MX cross stem ([OZO](https://www.ozokeyboards.com/products/kailh-deep-sea-silent-mini-low-profile-switches-choc-v2); [keeb.io $0.70, US](https://keeb.io/products/kailh-choc-v2-silent-low-profile-switches-mx-stem); silent variant 2.8 mm per [Deskthority](https://deskthority.net/wiki/Kailh_PG1353_series)) | Switch carries its own magnet: ≈ 122 → 550 G at the sensor ([Gateron](https://gateron.com/blog/detail/hall-sensor-magnetic-keyboard-switches)), inside the SS49E's 650 G limit at 3.3 V |
| Assembly | **Solder 25 switches** (2 pins each) to the key strip; press tops on; glue 25 magnets; bend and seat 25 sensors | Same, minus the magnets |
| Sensor | TO-92S SS49E **flat, face up**, beside the switch under the top's overhang (§2.2) | Designed for an **SMD sensor under the switch**. The only through-hole idea is a TO-92S flat in a slot in the strip. The position is **UNVERIFIED** and no through-hole sensor module was found |
| Silence | Quietest bought switch | "Moderately quiet" (`key-sourcing.md`) |
| Verdict | **Base** | **Fallback**, only if the $8 bench test shows the slot position reads well |

**Mounting note:** Choc V2 is listed as **plate-mount only**, with no PCB pegs
([Deskthority](https://deskthority.net/wiki/Kailh_PG1353_series)). Soldered pins plus the centre post locate it on
the strip. An **optional laser-cut 1.2–1.5 mm plate** adds rigidity, and it is required if stabilisers are used.
Whether the clips engage acrylic is UNVERIFIED.

### 2.2 Magnet geometry recomputed for 2.8 mm travel

**Basis:**
- on-axis disc formula;
- Hall element 0.5 mm under the face (UNVERIFIED, as `keys-answers.md` §2);
- SS49E at 3.3 V linear to ≈ 650 G (min);
- sensor face 2.0 mm above the strip (TO-92S laid flat on bent leads) [CALC].

| Magnet | Rest gap | Bottom gap (nominal 2.8 travel) | B rest / bottom | Swing | ADC counts | Bottom at +0.25 mm travel |
|---|---|---|---|---|---|---|
| 5 × 2 N35 | 5.6 | 2.8 | 180 / 639 G | 459 G | 524 | 731 G (clips the last ≈ 0.2 mm on a low-sensitivity part) |
| 5 × 2 N35 | 5.8 | 3.0 | 167 / 575 G | 408 G | 466 | 656 G |
| **K&J D31 4.76 × 1.59 N42 (recommended)** | **5.6** | **2.8** | **154 / 573 G** | **419 G** | **478** | **659 G** |

- **Recommendation:** D31 at **rest gap 5.6 mm**. At $0.19 each in the US ([K&J](https://www.kjmagnetics.com/proddetail.asp?prod=D31))
  it is cheaper than the sold-out 5 × 2 ESTIMATE. It stays linear over the full travel tolerance.
- **Magnet face height at rest = 2.0 + 5.6 = 7.6 mm above the strip top.** That is **2.1 mm higher relative to the
  sensor** than the original §v1.4b plan (3.5 mm rest → 0.7 mm bottom), which saturated.
- **Setting it [ENG]:**
  1. Measure H_u, the height of the top's underside above the strip at rest, on one switch with its top fitted. The
     Choc V2 is quoted at 12.3 mm overall ([OZO](https://www.ozokeyboards.com/products/kailh-deep-sea-silent-mini-low-profile-switches-choc-v2)),
     pins included or not is unclear, so H_u is UNVERIFIED.
  2. If H_u > 7.6 mm: add a laser-cut acrylic **boss** of (H_u − 7.6) under the magnet, or raise the sensors on a
     laser-cut **spacer comb** of that thickness. Either is owner-cut, $0 on scrap.
  3. If H_u < 7.6 mm: seat the sensor in a slot in the strip (down by up to 1.6 mm, `keys-answers.md` §1), or pocket
     the magnet deeper.
- **Lateral placement:** the magnet must sit beside the switch housing (Choc footprint ≈ 15 × 15 mm, ESTIMATE from V1),
  with its centre ≈ 10.5 mm from the stem centre along the key. A top must therefore be **≥ ≈ 28 mm long** with the
  stem centred. The boss clears the housing; at bottom-out the magnet still has 2.8 mm of air to the sensor.
- **Velocity resolution** stays at ≈ 1 MIDI step RMS at ff (478 vs 537 counts in the `keys-answers.md` §3 Monte
  Carlo, ≈ 1.1× the noise share) with the least-squares slope fit at ≥ 4 kHz [CALC, scaled].
- **Crosstalk:** whites sit at 18.7 mm pitch (≈ 0.4 % of swing, `keys-answers.md` §6). Black-key sensors in a rear row
  are ≥ 18 mm from white sensors, so the figure is similar. Only negative-going, so no false notes.
- **Switch steel:** the Choc spring compresses near the sensor, a small monotonic offset in the reading.
  Learned rest/bottom and linearisation absorb it [ENG]. Check it in the bench test.

### 2.3 Rocking: long tops on one stem

A piano-length white top (≈ 50–60 mm) on one MX-type stem tilts when pressed off-axis. That is §v1.4b's open issue.
Tilt also moves a magnet sitting 10 mm off the stem, which shows up as velocity error. Keyboard practice puts
stabilisers on keys of 2u (≈ 36 mm) and longer. Shorter keys run without them [ENG; common keyboard practice,
not sourced].

| Fix | Cost | Effect |
|---|---|---|
| **S1. Short tops, ≤ 1.75u (≈ 30 × 18 mm whites, stem centred; blacks 1u on a rear row)** | **$0** | No stabiliser needed, so no rocking. Button-like: OP-1 / KeyStep class, which fits the owner's loose OP-1 reference. Compatible with both "flat piano tops" (shortened) and "maple pegs" (owner: "show me both") |
| S2. Long piano tops + **Kailh Choc V2 stabilisers** on the 15 whites | 15 × **$1.99** = **+$29.85**, plus a laser-cut plate (stabs snap into the plate) ([keeb.io](https://keeb.io/products/kailh-choc-v2-stabilizers)) | Real piano-shaped whites. Stab rattle needs grease, and stabs add a little noise (ESTIMATE) |
| S3. Long tops on **two switches per white key** | 15 × $0.70 = **+$10.50** | Rigid, but double spring force (≈ 70–86 gf) and the contacts sit unused. Not recommended |

**Recommendation: S1.** S2 is the paid route if the design team's concept needs full-length piano whites.

**Pressed-on tops:** a laser-cut 3 mm acrylic (or maple) top with an MX cross pocket is the simplest. The cross is
4 × 1.17 mm, and kerf makes the fit trial-and-error, so cut a test strip of pocket widths first. Alternatively, glue
the top onto bought blank MX low-profile caps ($0.15–0.30, ESTIMATE, as §v1.4).

### 2.4 3.3 V sensor regulator (updated)

- **Load:** 25 SS49E at 6 mA typ / 10 mA max = **150–250 mA** ([Honeywell datasheet](https://atom.ubbcluj.ro/alpar/datasheets/sensors_actuators/Honeywell%20SS49E.pdf)).
  That is too close to the Pico 2's < 300 mA 3V3 recommendation
  ([Pico 2 datasheet](https://pip-assets.raspberrypi.com/categories/1005-raspberry-pi-pico-2/documents/RP-008299-DS-3-pico-2-datasheet.pdf) §3.1),
  so the strip gets **its own LDO**.
- **Part:** **LD1117V33, TO-220**, from the 5 V rail.
  - Dropout ≈ 1.1–1.2 V, against 1.7 V of headroom.
  - It dissipates (5 − 3.3) × 0.25 = **0.43 W worst case**, ≈ +20 °C on a bare TO-220 [ENG]. No heatsink.
  - It needs a ≥ 10 µF output capacitor for stability (UNVERIFIED; check the ST datasheet).
  - Fit it at the strip connector. 100 nF at every 2–3 sensors.
  - ≈ $0.50, ESTIMATE. **Now counted in the keys row.**
  - A 78L33 (100 mA) is too small.
- **Ratiometric:** the SS49E output tracks the LDO, while the ADC references the Pico's 3V3. The mismatch is a gain
  error that per-key rest/bottom learning absorbs. Re-learn rest at wake and on idle keys (`keys-answers.md` §3, §6).
- **Power budget:** the sensors add 0.5–0.8 W. If the 1.0–1.5 W in v1.2 excluded them, internal-LiPo runtime falls
  from ≈ 5–7 h to **≈ 3.5–5 h** [ENG]. Power gating doesn't suit continuous scanning.

### 2.5 Key cost (25 keys)

| Line | Bought acrylic | Scrap |
|---|---|---|
| 25 Choc V2 silent | $17.50 | $17.50 |
| 30 SS49E | $11.40 | $11.40 |
| 25 K&J D31 + shipping ≈ $4 (ESTIMATE) | ≈ $8.75 | ≈ $8.75 |
| Tops, acrylic + shipping | $13 | $0 |
| Stem adapters (blank caps), if used | $0–5 | $0–5 |
| Sensor LDO + caps | $0.50 | $0.50 |
| Spacer comb / bosses | $0 | $0 |
| **Total** | **≈ $51–56** | **≈ $38–43** |

This is parity with v1.10's $50–55. The scrap route saves ≈ $12. Add **+$29.85** for S2 stabilisers.

### 2.6 Bench test before the board order (≈ $10)

Buy 2 Choc V2 silent, 2 Gateron low-profile Hall, 5 SS49E and 10 D31. Then:
1. Measure H_u and the real travel.
2. Plot field against gap on a real SS49E at 3.3 V, to find where it saturates.
3. Confirm D31 at a 5.6 mm rest gap reads ≈ 450–480 counts of swing.
4. Try the Gateron flat-in-slot sensor.
5. Check the switch-steel offset.
6. Feel a 30 mm top for wobble.

---

## 3. Changes to `budget-variant.md`

- §v1.2 table: velocity row and switch added.
- §v1.4b: superseded note pointing here.
- §v1.10: keys row and totals.
- §v1.5b: the passive-dial cut no longer drops the AS3360.

## Sources
- AS3360 (dual VCA, CV feedthrough): https://www.tubesandmore.com/products/integrated-circuit-as3360-dual-vca-alfa-14-pin-dip
- CA-72 VCA netlist (Fig. 9-11 transcription): `ref/ca-72/circuits/boards/board4-vca.lib`
- Choc V2 silent specs: https://www.ozokeyboards.com/products/kailh-deep-sea-silent-mini-low-profile-switches-choc-v2 · https://deskthority.net/wiki/Kailh_PG1353_series · https://keeb.io/products/kailh-choc-v2-silent-low-profile-switches-mx-stem
- Choc V2 stabilisers: https://keeb.io/products/kailh-choc-v2-stabilizers
- Gateron Hall field figures: https://gateron.com/blog/detail/hall-sensor-magnetic-keyboard-switches
- K&J D31: https://www.kjmagnetics.com/proddetail.asp?prod=D31
- SS49E: https://atom.ubbcluj.ro/alpar/datasheets/sensors_actuators/Honeywell%20SS49E.pdf
- Pico 2 datasheet: https://pip-assets.raspberrypi.com/categories/1005-raspberry-pi-pico-2/documents/RP-008299-DS-3-pico-2-datasheet.pdf
