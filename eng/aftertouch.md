# Little D: channel aftertouch (pressure lanes under a floating key strip)

Status: rev 0, 2026-11-13. Answers the owner (`design/owner.md`, last entry): "i think it needs its own switch but yes now i want it". Recorded as: add channel aftertouch, sensed under a compliantly mounted key strip, with its **own** destination switch (separate from VELOCITY LOUD/BOTH/FILT), sent on MIDI out.

Builds on `daisy-first-principles.md` rev 0 (Daisy pin table §9, mux scan §1/§3, CVs §4), `velocity-and-keys-v2.md` rev 1 (keys, velocity routing) and `budget-variant.md` rev 13. Conventions as there: a link means I read it this session; **ESTIMATE** = my number; **UNVERIFIED** = a source exists but I couldn't confirm the figure; [ENG] = engineering judgement; [CALC] = arithmetic.

---

## 0. Bottom line

- **Sensing:** two **Interlink FSR UX 408, 300 mm** strips ($4.99 each, solder tabs, [Interlink](https://www.interlinkelectronics.com/products/fsr-ux-408-300mm-length)), trimmed to ≈ 240 mm. One lane runs under each key row (whites, sharps) and they're **wired in parallel**, so their conductances add.
- **Mechanism:** strip C stops being screwed tight. It **floats on the two lanes**. Four springs at the existing bosses push it down with a light, fixed preload (≈ 4 N in total). Because the lanes are the **only** thing holding strip C up, the lanes carry the whole force of every key wherever you press. Pressure after bottom-out reaches the sensors with **no extra key travel**: the stack moves ≈ 10–50 µm at 20 N (ESTIMATE).
- **Added height under the keys: 0 mm nominal.** The lane stack (≈ 8.1 mm) fills the ≈ 8 mm of air that's already under the raised strip C (`round4-answers.md` §1.3). The key surface stays at z 24. If the real gap is short, a thinner base strip makes it up, and keys rise only by any shortfall below 7.6 mm.
- **Electronics:** a divider (FSRs to the sensor rail, 10 k to ground, 100 nF) feeds **spare mux B channel 15 → ADC2**, and the toggle is a resistor ladder on **mux B channel 14**. **0 new header pins**; D16 stays spare. The FSR is sampled at the 8–10 kHz frame, averaged to 1 kHz, and smoothed with τ ≈ 10 ms.
- **False triggers:** pressure is **forced to 0 unless a key is bottomed** (the Halls know). Above that there's a **self-learning dead zone** sitting over normal holding force, a 30 ms blank after each note-on, and auto-zero whenever no key is held. Moving the instrument with no key down can't trigger it. A bump with a key held stays under the dead zone (≈ 1 N per g against ≈ 1.5 N, ESTIMATE).
- **Routing:** an ON-OFF-ON toggle, **MOD / OFF / FILT**:
  - MOD adds to the mod-depth CV (AS3360 A, Seed DAC1_OUT2), so it's vibrato when OSC MOD is on. Default: full pressure = +50 % of the MOD range.
  - FILT adds to the CUTOFF CV (MCP4822 #4 B). Default: full pressure = +2 octaves.
  - Channel pressure always goes out on USB-MIDI and TRS out, in every switch position. Incoming channel pressure drives the same destinations: max(local, MIDI).
- **Cost ≈ +$18–33** (ESTIMATE; the spread is mostly shipping and the silicone). Power ≈ 1 mW. Pins +0, mux channels 46 → **48 of 48**. Risk: **M** (FSR repeatability and creep, whether the UX strip can be trimmed, force bypass). All of it gets tested on the breadboard spike (§6) before layout.

---

## 1. Sensing

### 1.1 What the job needs
- One number, **total key force beyond normal playing**, the same wherever on the keyboard you press (channel aftertouch on a mono synth).
- Range ≈ 1–20 N on top of the bottom-out holding force. Bandwidth ≈ 20 Hz (pressure gestures are slow). Latency ≤ 20 ms.
- No change to the bought Choc V2 key feel. No user calibration. Through-hole or a ready-made part. Fits under the keys.

### 1.2 Options (US, qty 1)

| Option | Part / price | For | Against | Verdict |
|---|---|---|---|---|
| **A. 2 × FSR UX 408, 300 mm, parallel lanes** | $4.99 each, solder tabs, active width 10.2 mm, 0.41 mm thick, "switch travel 0.15 mm" ([Interlink 300 mm](https://www.interlinkelectronics.com/products/fsr-ux-408-300mm-length)). Series range 0.5–150 N ([UX 408](https://www.interlinkelectronics.com/products/fsr-ux-408)) | Cheap, thin (fits the existing gap), solderable tabs, two lanes so the sum is position-independent (§1.3) | Typical FSR behaviour: ±2 % single-part and ±6 % part-to-part repeatability, ≈ +10 % hysteresis, creep under load (400-series datasheet, [Rapid PDF](https://static.rapidonline.com/pdf/78-4000.pdf)). The 300 mm part is **312.7 mm overall**, longer than the ≈ 271 mm shell interior, so it **must be trimmed**. The FSR 408 "can be cut down to a very short length" ([DigiKey](https://www.digikey.de/de/product-highlight/i/interlink/fsr-408-strip-force-sensing-resistor)); that this holds for the **UX** line is UNVERIFIED (spike §6 test A1) | **Pick** |
| B. Original FSR 408 (24") | SparkFun SEN-09674 **$30.95**, "only 3 left", 100 g–10 kg ([SparkFun](https://sparkfun.com/products/9674)); Adafruit #1071 $19.95 **no longer stocked** ([Adafruit](https://www.adafruit.com:443/products/1071)) | Proven, trimmable | 2 × $31. Crimped tabs, can't be soldered (Adafruit warns it melts) | Fallback if UX trimming fails |
| C. Pressure-sensitive film (Velostat/Linqstat) + copper-tape electrodes | Adafruit sheet, 11 × 11", 0.1 mm, **$4.90** ([reseller listing](https://reach.dog/shop/kjdelectronics/products/adafruit-pressure-sensitive-conductive-sheet)) | Cheapest, cut to any length | DIY sensor, with larger drift, hysteresis and humidity sensitivity than an FSR [ENG]. Hand-made electrodes | Second fallback: same lanes, same firmware |
| D. 4 load cells under the strip mounts + HX711 | HX711 board **$9.95**, **10 or 80 SPS** ([Adafruit 5974](https://www.adafruit.com/product/5974)), plus 4 bar cells (ESTIMATE $5–10 each) | True force sum, linear, low drift | Bar cells plus mounting ≈ 10–15 mm tall (ESTIMATE): **no room**. 80 SPS = 12.5 ms per sample, before smoothing. 2 GPIO. ≈ $30–50 | Rejected |
| E. Hall displacement (a spare SS49E watching the strip sink into foam) | $0 (5 spare SS49E) | Free | Needs ≈ 0.3 mm of soft travel (a mushy key feel) and a rigid strip. Hall offset drift is the same size as the signal | Rejected |
| F. Hall "squeeze" of the Choc damper | $0 | Free | Damper squish ≈ 0.1–0.3 mm, not repeatable (`daisy-first-principles.md` §1.4) | Still an experiment only (spike test 5) |

### 1.3 Why two lanes, and why strip C must float
- **Statics:** if strip C is held up *only* by the lanes, the sum of the lane forces equals the applied key force, whichever key is pressed and however much strip C flexes. Two FSRs in parallel give a total conductance ≈ G₁(F₁) + G₂(F₂), roughly ∝ F₁ + F₂ in the FSR's near-linear conductance region [ENG]. So the reading is position-independent to first order.
- **One lane would not do it.** A single line support plus anything passive splits the force by leverage. The sharps' row would read ≈ ¼–½ of the whites' [CALC from the 47 mm strip geometry]. Firmware could correct per key, because the Halls know which key is down, but that's the fallback (§7), not the plan.
- **Anything else touching strip C steals force.** That includes rigid screws, key tops rubbing the window, a taut harness and felt. Strip C must touch **only** the lanes and the springs.
- **Feel:** the lanes are stiff. Silicone or foam strips 1.6 mm thick and 6 mm wide over ≈ 2 × 240 mm ≈ 2,900 mm² move ≈ 10–50 µm at 20 N, depending on the material (ESTIMATE). Pressing harder adds **no perceptible key travel**; the FSR senses force, not travel. The compliant layer is there to **spread** the load along the FSR (FSRs read concentrated loads inconsistently) and to soak up ±0.1 mm of flatness error. It isn't there to give.

### 1.4 Mechanical stack (flat concepts, at each lane; z from the outside of the back panel)

```
 z 24.0  ─ white key surface (unchanged)
          Choc V2 + top
 z 12.7  ─ strip C top          ┌── spring (≈1 N) in a Ø7 counterbore in each boss pushes strip C down
 z 11.1  ─ strip C underside ───┤   M3 screw from below + nylon sleeve through a Ø6 hole: strip floats, ±0.5 mm lateral
          pressure rib, 3 mm acrylic × 6 mm, epoxied to a lead-free lane on strip C's underside (clears 1.5 mm lead tails)
 z  8.1  ─ actuator: 1.6 mm (1/16") soft silicone (30–40A) or PORON strip, 6 mm wide (narrower than the 10.2 mm active width)
 z  6.5  ─ FSR UX 408, trimmed to ≈ 240 mm active, on thin transfer tape
 z  6.0  ─ base strip, 3 mm laser-cut acrylic × 16 mm, glued to the back panel (flat ≤ 0.1 mm over 240 mm)
 z  3.0  ─ back panel inner face (the reference; it takes the load straight to the feet)
 z  0    ─ back panel outside, feet
```

- **Height budget [CALC]:** 3 + 0.46 + 1.6 + 3 = **8.06 mm** against ≈ 8 mm of existing air under strip C (keys at 24, strip on spacers; `round4-answers.md` §1.3). Trim at assembly by choosing the base strip's thickness: base = gap − 5.06 mm (2 or 3 mm acrylic, plus 0.5 mm shims). The rib must stay ≥ 2.5 mm to clear the lead tails, so **keys rise only if the gap is < 7.6 mm**, and only by the shortfall.
- **Lanes:** two lanes, one under each key row (≈ y 12 and y 38 on strip C, ESTIMATE), each 6 mm wide on strip C's underside with **no through-hole leads or vias**, within ≤ 8 mm of the row's switch centreline. Active length ≈ 240 mm, centred. End keys sit a few mm past the lane ends, but their force still goes into the lanes through strip C (§1.3).
- **Clamping the FSR:**
  - Each FSR is bonded to its base strip with thin transfer tape (e.g. 3M 467-class, ESTIMATE).
  - The cut end is sealed with Kapton tape.
  - The solder-tab end sits **outside** the rib's footprint (the rib stops 5 mm short) and is held by a small acrylic clip.
  - Two thin wires run in a slack loop from the tabs up to pads on strip C. Both FSRs go in parallel at strip C.
- **Retention and preload:**
  - The 4 existing shell bosses keep their M3 inserts. Each screw (still from below) passes through a **nylon sleeve** in a Ø 6 hole in strip C and tightens against the sleeve, so strip C isn't clamped.
  - A **light compression spring** (≈ 0.5 N/mm, ≈ 2 mm compressed ≈ 1 N, from an assortment, ESTIMATE) sits in a Ø 7 × 2.5 counterbore in each boss face and presses strip C down.
  - Preload ≈ 4 N plus strip weight ≈ 0.8 N (ESTIMATE). That keeps the FSR above its ≈ 0.5 N onset, so pressure starts smoothly, and stops rattle.
  - Spring force changes ≈ 0.03 N over the ≈ 50 µm the strip moves, so the springs don't bypass load [CALC].
- **Load path:** finger → strip C → lanes → back panel → feet → table. **The shell and bosses no longer carry key load.** Put 2 of the feet under the key zone near the lane ends.

---

## 2. Electronics

| Item | Design |
|---|---|
| Divider | Both FSRs in parallel, from the **sensor-LDO 3.3 V rail, upstream of any Hall-gating PNP** (`daisy-first-principles.md` §1.5), to node P. **R_M = 10 k** P → GND (bench-pick 4.7–47 k in test A2). **100 nF** film at P. V_P rises with force; ≤ 0.33 mA, ≈ 1 mW |
| Ratiometric | The FSR rail is the Hall rail. The existing Hall-rail monitor channel corrects supply drift against the Seed's ADC reference, the same way as for the keys (§1.4 there) |
| ADC input | **Mux B channel 15 → ADC2 (D17 / PB1)**. **No new header pin.** P is low-impedance at the mux (100 nF reservoir against 4 pF + mux C), so charge-sharing error is ≈ 0.05 % [CALC]. **D16 stays spare** (comparator / VCA-sense fallback). Putting the FSR on D16 instead would need an injected conversion inside the ADC1+2 dual-mode paced scan, which risks timing skew on velocity. Not worth it |
| Toggle | ON-OFF-ON sub-mini, 3-step resistor ladder → **mux B channel 14**, read like VELOCITY: ±⅓-step windows, 20 ms debounce |
| Mux tally | `daisy-first-principles.md` §3.1 lists 20 controls + the Hall-rail monitor = 21 + 25 keys = **46**. Its §3.2 layout ("mux B 9–15 = 6 controls + monitor") overcounts by 2. Correct allocation: mux C = 16 controls; mux B 0–8 keys 17–25, 9–12 controls, 13 Hall-rail monitor, **14 AT toggle, 15 FSR**. **48 of 48 used, 0 spare** |
| Harness | +1 wire (node P) if the muxes stay on the main board. Whether the 2 × 14 strip-C header has a free pin is UNVERIFIED (check at capture). Local if the muxes move onto strip C |
| Scan and smoothing | Sampled every frame (8–10 kHz, 4× hardware oversampling) → box average to 1 kHz → linearising LUT (FSR conductance from V_P) → detection logic (§3.2) → 1-pole τ ≈ 10 ms → slew limit (full scale ≥ 30 ms) → destinations at 1 kHz. Resolution ≈ 14 bits after averaging [CALC as §3.2 there], far beyond 7-bit pressure |

---

## 3. Firmware: calibration and rejecting false triggers

### 3.1 Auto-zero (no user step)
- **Boot:** after the sensor LDO enables (last in sequence) plus 200 ms, average 0.5 s with no key down → baseline F₀. If a key is down at boot, wait for release.
- **Running:** whenever no key has been bottomed for ≥ 0.5 s, F₀ tracks slowly (τ ≈ 5 s). Steps > 2 N with no key down (a knock, being set down) are ignored for 1 s, not tracked. This absorbs preload creep, temperature, orientation (strip weight × cos tilt) and FSR drift.
- **Full scale:** a fixed default span of **8 N** above the dead zone (ESTIMATE, a firm press), with a mild curve (γ ≈ 1.5) so light pressure stays subtle. Span and curve are settings (hold-TAP gesture or MIDI, like the velocity curve). Nothing to set up.

### 3.2 Gating and dead zone
1. **Key-held gate:** output = 0 unless at least one key's Hall depth is ≥ 0.9 (bottomed). That covers all handling, lifting and tilting with no key down.
2. **Dead zone above normal holding:** T = max(1.5 N, 1.3 × the rolling median of (F − F₀) measured 150–300 ms after each note-on, over the last 32 notes), plus 0.5 N for each extra held key. It **learns the player's resting weight** automatically. Pressure P = clamp(((F − F₀ − T) / 8 N)^γ, 0, 1).
3. **Strike blanking:** for 30 ms after any note-on, P is held at its previous value, so the bottom-out impact spike (a few ms, ESTIMATE) never reads as pressure. A re-strike under held pressure doesn't glitch.
4. **Sustain:** P must stay above 0 for ≥ 20 ms before it leaves 0 (rejects bumps), then the τ 10 ms smoother and the slew limit apply.
5. **Bumps with a key held:** the strip and keys weigh ≈ 80–100 g (ESTIMATE), so a 1 g jolt ≈ ±1 N. That's inside the 1.5 N minimum dead zone, and the 20 ms sustain catches the rest.
6. **Release:** when the last key releases, P ramps to 0 in 20 ms and a final MIDI pressure of 0 is sent.

---

## 4. Routing

### 4.1 Switch (its own toggle, separate from VELOCITY)

| Position | Destination | Default depth (settings) |
|---|---|---|
| **MOD** (up) | Added to the **mod-depth CV**: Seed DAC1_OUT2 (D22) → AS3360 half A, the same stage the MOD dial and CC1 drive. depth = clamp(MOD dial + 0.5 · P, 0, 1) | Full pressure = **+50 % of MOD range** (0–100 %) |
| **OFF** (centre) | No sound change. MIDI pressure is still sent | — |
| **FILT** (down) | Added to the **CUTOFF CV**: MCP4822 #4 ch B. cutoff = knob/CC + velocity offset + 2 oct · P, clamped | Full pressure = **+2 octaves** (0–4 oct) |

- **Why OFF in the centre, not BOTH:** there's no AT amount knob, so OFF is the only way to play without pressure effects. A centre-off ON-OFF-ON is the natural part. BOTH could be a firmware option that turns OFF into BOTH, but it isn't the default.
- **Legend:** MOD adds *modulation amount*. It's vibrato when OSC MOD is on with osc 3 as the LFO, and a filter wobble when FILTER MOD is on, both set by the existing toggles and MOD MIX. "MOD" is the honest legend; "VIB" matches the owner's wording. **Owner/design to choose.**
- **Interactions:**
  - The closed-loop pitch trim freezes on period variance (`daisy-first-principles.md` §2.3), so AT vibrato can't fight it.
  - The §v1.5b passive-MOD-dial cut would also remove AT → MOD.
  - Velocity stays latched per note; pressure is continuous. The two add on CUTOFF.
  - MIDI never flips the switch (owner rule).

### 4.2 MIDI
- **Out:** channel pressure (Dn) on USB-MIDI and TRS out (owner: "Add MIDI out"). 7-bit, sent on change, at most once every 5 ms, a final 0 on release. Sent in **all** switch positions, so Little D works as a pressure controller. Can be disabled in settings.
- **In:** channel pressure drives the same destination through the same switch: P_eff = max(P_local, P_MIDI). P_MIDI decays to 0 over 50 ms after the last MIDI note-off, so a stuck value can't hang. Optional: polyphonic pressure (An) for the sounding note maps to the same path ($0).

---

## 5. Cost, power, pins

| Item | Cost | Source |
|---|---|---|
| 2 × FSR UX 408, 300 mm, solder tabs | $9.98 | [Interlink store, $4.99](https://www.interlinkelectronics.com/products/fsr-ux-408-300mm-length). DigiKey also lists UX 408 parts (34-00158 at €8.45 on [digikey.fr](https://www.digikey.fr/en/products/detail/interlink-electronics/34-00158/16803578), length not shown; US price UNVERIFIED) |
| Shipping from Interlink (or $0 if bought on the DigiKey order) | $0–12 | ESTIMATE |
| Sub-mini ON-OFF-ON toggle | $0.80–1.00 | ESTIMATE, as the VELOCITY toggle (`velocity-and-keys-v2.md` §1.5) |
| R_M, ladder resistors, 100 nF film | $0.15 | Tayda, ESTIMATE |
| Actuator strip: 1/16" soft silicone or PORON sheet, cut to 2 × 6 mm strips | $4–8 | ESTIMATE |
| 4 springs (assortment allocation), 4 nylon sleeves, transfer tape | $2–4 | ESTIMATE |
| Acrylic ribs, base strips, tab clips | $0 | Vector Space scrap, laser-cut |
| **Total** | **≈ +$18–33** | |

- **Power:** ≤ 1 mW. CPU: negligible (one channel already in the scan).
- **Pins:** 0 new header pins. Mux 46 → 48 of 48. D16 is the last analog spare.
- **Board:** strip C needs two 6 mm lead-free lanes, 4 Ø 6 holes (were M3 clearance) and 2 FSR pads. Area should be unchanged (UNVERIFIED until placement).

---

## 6. Breadboard spike additions (≈ +1 evening; joins `daisy-first-principles.md` §10)

Rig: a scrap 270 × 47 strip of 1.6 mm perfboard or FR4 carrying 4 Choc V2 + tops (2 front row, 2 rear row, at both ends and the middle), the two lanes on a flat acrylic base, 4 sleeves + springs, the Seed reading the divider through a CD74HC4067 channel. Use 0.5 / 1 / 2 kg weights (water bottles) on the key tops.

| # | Test | Pass |
|---|---|---|
| A1 | **Trim one UX 408** to 240 mm, seal the end. Force/resistance against an untrimmed one, per unit length | Within ±10 %; no open circuit after 1,000 presses |
| A2 | Force → counts, 0–20 N, at 6 key positions (both rows, ends and middle); pick R_M | Position spread ≤ ±20 % of reading; monotonic; ≥ 500 counts span |
| A3 | Actuator material: 40A silicone vs PORON | Pick the one with the smaller A2 spread |
| A4 | **False triggers:** 2 min of normal playing (staccato, legato, ff strikes) with the firmware gate on | Zero pressure output above 2 % |
| A5 | **Handling:** with no key held, lift, set down hard, knock the case, tilt 45°; then repeat holding one key lightly | 0 output with no key held; < 10 % transient with a key held |
| A6 | Creep: hold 5 N for 60 s; release; re-zero | Reading drifts < 10 %; baseline returns within 1 s of release |
| A7 | Latency: force step → MIDI pressure out (scope on the TRS out) | ≤ 20 ms to 90 % |
| A8 | Feel: compare key bottom-out with the strip floating vs rigidly screwed | No difference noticed (blind, owner) |

**Gate:** A1 fails → buy the original FSR 408 (option B). A2 spread > ±20 % → per-key gain table from the Halls (§7). A4/A5 fail → raise the dead-zone floor and sustain time before changing hardware.

---

## 7. Risks

| Risk | Level | Mitigation |
|---|---|---|
| FSR repeatability, hysteresis, creep (±6 % part-to-part, ≈ 10 % hysteresis per the 400-series datasheet) | M | Auto-zero, learned dead zone, a soft curve; aftertouch is a gesture, not a measurement. Spike A2/A6 |
| UX 408 not trimmable, or the cut end delaminates | M | Spike A1 first. Fallback: SparkFun FSR 408 ($30.95 each, crimped tabs → clamp connector) or the Velostat lane |
| **Force bypass:** anything but the lanes touching strip C (key tops on the window edge, a taut harness, HUSH felt on peg shanks) | M | Strip C touches only lanes + springs; ≥ 1 mm clear around key tops in the window; slack harness loop; HUSH felt hole clearance (already ≥ 0.5 mm radial) |
| Strip C layout can't fit two lead-free 6 mm lanes in 47 mm | M | Check at placement. Fallback: one centred lane plus a per-key gain table (Halls know the key), or a rigid aluminium carrier under strip C (costs height) |
| Back panel not flat or stiff enough under the keys | L–M | 3 mm acrylic base strips; feet under the lane ends; flatness ≤ 0.1 mm over 240 mm |
| Mux full (48/48) | L | D16 remains as a direct ADC input for any later analog need |
| FSR temperature effect on gain | L | Offset handled by auto-zero; gain change UNVERIFIED; acceptable for a gesture control |

---

## 8. Design-facing constraints (for the design team)

1. **Height under the keys: +0 mm nominal.** The ≈ 8 mm under strip C is now **occupied** by two lanes (one under each key row). Keys stay at z 24. Only if the measured gap is < 7.6 mm do the keys rise, by the shortfall (≤ ≈ 0.5 mm expected). `round4-answers.md`'s optional "muxes + LD1117 under strip C" now fits only in the band between the lanes, parts ≤ 5 mm. Prefer the main board.
2. **New toggle: AFTERTOUCH (or PRESSURE), MOD · OFF · FILT** (or VIB · OFF · FILT, owner's choice). Same sub-mini body as the others, so **8 toggles** (was 7). Logical spot: beside VELOCITY as a "keyboard response" pair, but a **separate** switch. Same body-height check as the other toggles (`budget-variant.md` §v1.8, rev 10).
3. **The back panel becomes structural under the key zone** (HUSH, ONE SHEET): flat, with 2 acrylic base strips glued on, and 2 of the feet under the lane ends. It's still screwed from underneath (no visible change). With the back panel off, strip C just hangs on its 4 screws.
4. **Strip C floats.** The 4 bosses become retention posts: a **Ø 7 × 2.5 mm spring counterbore** in each boss face, strip C holes Ø 6. Screws are still from below. Keep **≥ 1 mm clearance between key tops and the key-window edges** all round (strip C can shift ±0.5 mm). Nothing in the shell may touch strip C or the keys.
5. **FOLD:** the 270 × 78 base board (keys + PLAY strip on one board, `round4-answers.md` §1.4) **must split** into a floating key strip and a fixed PLAY board (fixed pots can't float). Add a short ribbon between them. The printed base floor under the keys must be flat (glue in a 3 mm acrylic base strip).
6. **Panel/legend:** "AFTERTOUCH" or "PRESSURE", positions MOD/OFF/FILT. No new jack: MIDI out already carries it.
