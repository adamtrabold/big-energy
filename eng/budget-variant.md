# Budget variant ("Little D"): a ~$100 instrument with the Model D spirit

Status: rev 0, 2026-11-12; **latest rev 14 (2026-11-13, owner decision: channel aftertouch with its own switch; §v1.12, `aftertouch.md`)**; rev 13 (2026-11-13, Daisy Seed replaces the Pico 2; §v1.11); rev 12 FOLD only: `fold-answers.md`; rev 11 battery: `battery.md`. This is a **separate, second instrument** (owner: "lets keep the expensiver one too"). It
shares no boards with `architecture-v2.md`. It does reuse ideas: autotune, background re-tune, jump-on-move,
and the "keys on their own strip" rule.

Conventions: link = price/stock read this session (2026-11-12). **ESTIMATE** = my number, not checked.
**UNVERIFIED** = a source exists but I could not confirm the figure. [ENG] = engineering judgement.

Constraints still in force:
- hand-soldered through-hole only; anything SMD arrives as a ready-made module;
- no factory assembly;
- 25 keys minimum, feels like an instrument;
- portable and battery-capable;
- analog audio path, and analog wherever possible;
- no calibration rigmarole.

---

# PART 1: LITTLE D v1, LOCKED SPEC (rev 2, 2026-11-12; **rev 8 changes marked [rev 8]**, **rev 9 marked [rev 9]**, **rev 10 marked [rev 10]**, **rev 11 marked [rev 11]**, **rev 12 marked [rev 12]**)

**[rev 14] (2026-11-13, owner decision "now i want it"; detail in §v1.12 and `aftertouch.md`):** **channel aftertouch.**
- **Sensing:** two Interlink FSR UX 408 300 mm strips ($4.99 each), trimmed to ≈ 240 mm, form parallel pressure lanes under the two key rows. Strip C now **floats** on the lanes, held down by 4 light springs, so all key force passes through the sensors. No added key travel.
- **Height:** **+0 mm nominal** (the stack fills the existing ≈ 8 mm under strip C).
- **Electronics:** a divider on spare mux B channel 15; the new **AFTERTOUCH toggle MOD / OFF / FILT** on mux B channel 14. 0 new pins; mux 48/48.
- **Routing:** MOD adds to the AS3360 A mod-depth CV, FILT adds to the CUTOFF CV. Channel pressure goes out on USB and TRS, and incoming pressure drives the same destinations.
- **Cost:** ≈ +$18–33. The TRS MIDI out jack (owner: "Add MIDI out") is now counted too, +$0.50.
- **Design:** 8 toggles; the back panel carries the key load; FOLD's base board must split.

**[rev 13] (2026-11-13, owner decision; detail in §v1.11):** the digital brain is now an **Electrosmith Daisy Seed (Seed3 or 65 MB Seed2 DFM, $34.99)**, socketed, replacing the Pico 2. It does all control duties **plus the digital echo + reverb**; the dry voice path stays analog. No SGTL5000 shield and no 74HC595 are needed. Consequences:
- **Cost ≈ +$39–50** (USB) over rev 12 (Seed +$29.24 net; 8 FX controls, DRIFT and wet path ≈ +$10–21); **+$6–12 more with a battery** for a bigger boost. One-unit totals in §v1.11.4.
- **Power:** ≈ 2.4–4.4 W (was 2.0–3.6). Runtime on 22.2 Wh ≈ 3.9–7.5 h; on the slim 11.1 Wh pack ≈ 1.9–3.7 h.
- **Footprint:** 2 × 20 pins at 0.6" row spacing (the Pico is 0.7"), so it is a different socket. 51 × 18 mm, under the Pico's 51 × 21.
- **USB:** the E3 pad-wiring trick (D± to Pico test pads) does not carry over as written (§v1.11.3).
- Subsystem implementation (key scan, autotune counters, pot scan, CVs, MIDI, FX path, sequencing) is **pending `daisy-first-principles.md`**. Pico-specific text below (PIO counters, Pico-sequenced enables, "Pico-read") is history until that lands.
- Design-facing list: `daisy-switch-notes.md`.

**[rev 12] (2026-11-12, `fold-answers.md`, FOLD only):**
- **FOLD band pack option:** 4 × PiShop 952540 (9.5 × 25 × 40, 750 mAh, PCM), 1S4P, 11.1 Wh. Runtime ≈ 4.5 h at 2.0 W, ≈ 2.4 h at 3.6 W. Star harness + 2 A fuse. $40.75 with the charger.
- **FOLD depth:** set by lid board area + battery footprint, **D ≥ 6 + (23,300 + A)/262**. ≤ 90 needs no internal cell *and* the ladder in the base.
- **FOLD EMPHASIS can cross the hinge:** 2-wire rheostat (SPICE: no effect on response or self-oscillation onset). The emphasis-input wire goes at the far ribbon edge, ≤ 0.1 pF to the mux selects. 40-way ribbon. Bench pass ≤ −70 dB.
- Flat concepts unchanged.

**[rev 11] (2026-11-12, `battery.md`):** internal battery is now **two 50 × 60 mm pouch cells in parallel (1S2P)**, 22.2 Wh with PiShop 755060 ×2 (runtime ≈ 4.7–9 h), or 18.5 Wh with Adafruit #328 ×2 (verified in stock, ≈ 3.9–7.5 h). Same bq25185 charger/boost. LiPo line is now ≈ **$38.85–40.85** (was $21.45), so totals with LiPo ≈ +$17.4–19.4. Only the power lines below changed.

**[rev 10] (2026-11-12, `round4-answers.md`):**
- **Main board:** 268 × 85 doesn't fit. It becomes ≈ 268 × 115, with 1/8 W standing resistors, top-side parts ≤ 6.5 mm and the Pico on the underside.
- **Pots:** the Tayda A-5531 has a 40-tooth shaft, so they change to the A-5622 T18 spline (+$3.22).
- **Power:** recounted at ≈ 2.0–3.6 W, so LiPo runtime ≈ 1.8–3.3 h. The sensor LDO is switched on last.
- **Boards:** 67.5 in².
- **Totals:** ≈ +$12–20.

**[rev 8] (2026-11-12, `velocity-and-keys-v2.md`):** velocity now sounds, selected by a LOUD / BOTH / FILT switch (≈ +$2). Keys are 25 bought Choc V2 silent switches with short pressed-on tops and a magnet over a flat SS49E; the owner won't build a key mechanism, so RAIL is out. Totals ≈ +$3.

**[rev 9] (2026-11-12, `little-d-design-answers.md`):** the 3" speaker (Adafruit #1313) is 25.5 mm deep and fits no concept; replaced by a **50 mm, 7.6 mm-deep Same Sky CDS-5076-1SP ($3.88)**, no board cutout, with a lead-free keep-out on the main board underside over it. ≈ 4–6 dB quieter, less low end. Totals ≈ +$2.

This section follows the owner decisions in `owner-requirements.md`, under "budget instrument ('Little D')
decisions" and the corrections after it:
- **one test unit**;
- **quantity-1 board fabrication, no 5-board minimums**;
- **3 VCOs**;
- **all original waveforms**;
- **modern pin-for-pin "original chips"** (AS3046 etc.; "i dont need vintage parts");
- **keep the speaker**;
- **no extra patch points**;
- **US distributors where it helps**;
- **keys as silent as possible**, mechanism still open;
- **bend/mod control undecided**: priced as options in §v1.5, not in the base total.

**Part 1 supersedes Part 2 (the rev 0 tier exploration) wherever they conflict.** Part 2 stays for the
reasoning, the cut list and the calibration method (§4 there still applies).

Rev 2 changes:
- touch strips moved out of the total and into options;
- all boards re-costed at quantity 1 with US/one-off fabs;
- board designs cut from 5 to **1**;
- LCSC dropped (it only made sense riding in a JLC box), so those parts now come from Tayda or US vendors.

## v1.0 Bottom line (one unit, one-off)

| Configuration | Parts | Board (qty 1, §v1.3) | Shipping + duty | **One-unit total** |
|---|---|---|---|---|
| v1 core, USB power bank (includes the old printed-key/Hall allowance of $22.90) | $138 | $75–130 | $31–43 | ≈ $244–311 |
| **v1, USB, K3 silent switches + SoftPot strips** (cheapest all-bought keys and bend/mod) | +$14–17 | — | — | **≈ $258–328** |
| **v1, USB, K3 silent switches + real wheels** (Doepfer pitch wheel + thumbwheel mod, §v1.5) | +$25–34 | — | — | **≈ $269–345** |
| v1, USB, K1 harvested keybed + real wheels | +$44–63 | — | — | ≈ $288–374 |
| Internal LiPo (recommended: "completely portable") | +$21.45 ~~on any row~~ **[rev 11] +$38.85–40.85 (2 cells + bq25185, `battery.md`)** | — | — | — |

**Superseded by §v1.10 (rev 4 clean totals).** Owner rule (2026-11-12): **knobs, keys and wheels must be real bought parts, not 3D-printed.** The rows above
use the key options in §v1.4 and the bend/mod options in §v1.5.

Add 10 % contingency for a first build (wrong parts, a re-order).

**Honest read:**
- **Revised one-unit range ≈ $245–350**, depending on battery, bend/mod choice and which fab wins the quote.
- **The board is now the biggest single unknown, about $75–130 (ESTIMATE).** None of the quantity-1 fabs publishes a price for a board this size without uploaded files.
- For the record: JLC's 5-board order (≈ $30–42 including tariff, rev 1) would be about $40–90 cheaper and still means one order and one fee. The owner has declined minimums, so it is not in the totals.

It is still about half of the full version's $490–810.

**Next action (10 minutes, no design needed):** upload a placeholder 280 × 170 mm, 2-layer outline Gerber to
these instant quoters and replace the board ESTIMATE with real numbers:
- Pad2Pad
- PCBCart
- AtlasPCB
- Advanced Circuits BareBones
- Ponoko (quote by request)

## v1.1 What of the old $150/$200 tiers is included

| Old tier item | In v1? |
|---|---|
| $150: VCO 3 | **Yes** |
| $150: tempcos ×3 | **Yes** (with the AS3046s) |
| $150: pitch + mod wheels | **Undecided**: wheels, SoftPot strips or DIY copper strips are priced as options (§v1.5) |
| $150: internal LiPo | **Optional, recommended** (+$21.45, §v1.6) |
| $150: 2nd MCP4822 | **Yes** (VCO 3 + filter keytrack CV, enables filter cal) |
| $200: full waveform sets on rotary switches | **Yes** (all 6 per VCO; osc 3 has reverse saw in place of shark tooth, as original) |
| $200: noise/osc-3 MOD MIX crossfade | **Yes** (original mod path; osc 3 is the LFO, as original) |
| $200: AS3046 expo arrays | **Yes**, one per VCO |
| $200: MCP4728 (MIDI sustain etc.) | No |
| $200: PAM8302 louder speaker | No (LM386 + 3" speaker kept) |
| $200: more patch points, A-440 | No (owner: no extra patch points) |
| $200: nicer panel | No (laser-cut ply/acrylic; owner's own walnut possible at $0 extra) |
| rev 0 firmware LFO + LFO RATE pot | **Dropped**: osc 3 is the mod source, as on the original |

## v1.2 Locked spec

**Size** ≈ 290 × 170 × 32 mm. Wheels, if chosen, add ≈ 40–45 mm of width (§v1.5).
**Power** 5 V USB, ~~≈ 1.0–1.5 W [ENG]: internal 2000 mAh LiPo (≈ 5–7 h)~~ **[rev 10] ≈ 2.0–3.6 W at 5 V (ESTIMATE, recount: the voice rails 1.2–1.9 W, and the sensors 0.6–1.25 W because the LDO draws 5 V × I). The internal 2000 mAh LiPo gives ≈ 1.8–3.3 h. **[rev 11] With two 50 × 60 mm cells in parallel (22.2 Wh): ≈ 4.7–9 h, see `battery.md`.** **[rev 13] With the Daisy Seed and echo + reverb: ≈ 2.4–4.4 W, 22.2 Wh pack ≈ 3.9–7.5 h, §v1.11.2.** The sensor LDO comes up last through an MCU-switched P-FET (boost stall)**, or any USB power bank (no auto-off at 0.4–0.7 A).

| Block | Circuit ("original-style chips", modern equivalents) | Panel |
|---|---|---|
| VCO 1–3 | **AS3046 expo** per VCO (pin-for-pin modern CA3046) + **2 kΩ 3300 ppm tempco**. Original-topology core: discrete reset and comparator. Ramp buffer is the original discrete JFET-differential topology, using **hand-matched through-hole JFETs** (Pico Idss jig). Original waveshapers (tri folder, shark/reverse-saw, 3 rectangle widths) | **WAVE** 6-way rotary ×3. **RANGE** ×3 (Pico-read pots, 6 firmware detents: LO, 32'–2'). **FREQ** osc 2, osc 3 (Pico-read). **OSC 3 CONTROL** toggle (keyboard off) |
| Controllers | Firmware glide (saturating curve), master tune | **TUNE**, **GLIDE** (Pico-read). **MOD MIX** pot (osc 3 ↔ noise, analog). **OSC MOD** and **FILTER MOD** toggles. Bend/mod controller: option, §v1.5 |
| Mixer | **Passive into the ladder input pair** (original) | **OSC 1/2/3** levels, **NOISE/EXT** level. **SOURCE** 3-way toggle: noise / ext / feedback. No per-channel on/off switches: turn the level down instead |
| Filter | 4-pole discrete ladder (hand-matched 2N3904 pairs, as the original's matched TIS97s), film caps, discrete-pair expo, original-style output stage | **CUTOFF** (Pico-read, MIDI CC). **EMPHASIS**, **CONTOUR AMT**. **KEYBOARD CONTROL** 3-way toggle (off / ⅓ / ⅔) |
| Contours ×2 | Original ADS topology, overshoot kept | **A/D/S** ×2. **DECAY** toggle |
| VCA, output | Discrete pair, auto-nulled. LM386 → ~~3" speaker~~ **[rev 9] 50 mm thin speaker (7.6 mm deep); main-board underside lead-free over a ≈ 54 mm circle, speaker ≥ 30 mm from ladder/expos**; phones/line. **[rev 8]** Loudness contour passes through AS3360 half B (velocity) before the VCA; EXT LOUDNESS normal untouched | **VOLUME** |
| **[rev 8] Velocity** | Pico PWM "VEL" → 2-pole RC → AS3360 half B (scales loudness contour); filter = velocity offset added in firmware to the CUTOFF CV | **VELOCITY** ON-OFF-ON toggle: LOUD / BOTH / FILT (read on a spare CD4067 channel) |
| **[rev 14] Aftertouch** | Channel pressure: 2 × FSR UX 408 lanes under a floating strip C → divider → mux B ch 15 (ADC2). Firmware gate (key bottomed), learned dead zone, auto-zero. MOD → AS3360 A mod depth; FILT → CUTOFF CV; MIDI pressure out (USB + TRS) and in. `aftertouch.md` | **AFTERTOUCH** ON-OFF-ON toggle: MOD / OFF / FILT (mux B ch 14) |
| Keys | ~~25. Hall (default) or tactile buttons, see §v1.4~~ **[rev 8]** 25 Kailh Choc V2 silent switches soldered to the key strip, short pressed-on tops (≤ 1.75u), K&J D31 magnet in each top over a flat SS49E (rest gap 5.6 mm, bottom 2.8 mm); strip on its own LD1117V33. `velocity-and-keys-v2.md` §2 | — |
| I/O | **PITCH CV out, GATE out, FILTER CV in**, EXT audio in, PHONES/LINE out, TRS MIDI in, USB-MIDI **[rev 13] USB route changes, §v1.11.3; optional TRS MIDI out is free on the Seed** | — |
| Digital | ~~Pico 2 (socketed)~~ **[rev 13] Daisy Seed (socketed, 2 × 20 pins), §v1.11.** **2× MCP4822** (VCO 1–3 pitch + filter keytrack). 3× CD4067 (25 keys + 8 Pico-read pots + 2 bend/mod inputs = 35 channels) | — |
| Power | 2× MC34063 → ±12 V → 78L09/79L09 → ±9 V (rev 0 §2.4) | Power switch |

**Panel count:** 23 pots (8 Pico-read), 3 rotary switches, ~~6~~ ~~7 toggles [rev 8: + VELOCITY]~~ **8 toggles [rev 14: + AFTERTOUCH]**, plus the power switch. (FX controls and DRIFT from rev 13 are additional: §v1.11.1.)

**[rev 10] Boards now:**
- **Main board ≈ 268 × 115** (flat concepts). The design's 268 × 85 is short by ≈ 15–35 mm of depth (part-by-part courtyard tally, `round4-answers.md` §1).
- **Strip C is 270 × 47.**
- **Every top-side main-board part is ≤ 6.5 mm.** That means:
  - 1/8 W resistors standing;
  - DIPs soldered directly or in low-profile sockets;
  - 5 mm electrolytics.
- **The Pico and the MC34063 inductors go on the underside**, with a stack ≤ 8 mm.
- **FOLD's lid board (262 × 50) is ≈ 9–12k mm² short**; see §1.4 there.

The single-board text below is history.

**One board.** Everything goes on a **single 2-layer board, ≈ 280 × 170 mm (≈ 73.8 in²)**, covering the whole footprint:
- **Back ≈ 100 mm:** pots, switches and jacks, with voice circuitry between them.
- **Front ≈ 70 mm:** the rest of the voice, the Pico and the DACs, all kept to ≤ 8 mm height, with the **row of Hall sensors (or tactile pads) under the keys**. The printed keys mount above it on standoffs.
- This replaces the 5 small boards of rev 1, so there is one order, one handling/tooling fee and no inter-board cables.
- It also fits BareBones' 10 × 16 in maximum ([Advanced Circuits](https://advancedpcb.com/en-us/barebones-special)).
- The owner's earlier note that keys must not drive *main board* size is respected in spirit: the sensor row is a strip region of the one board, and a different key mechanism only changes that region's footprints.

**Calibration:** "no rigmarole" holds:
- VCO autotune at boot, plus background re-tune;
- VCA auto-null;
- self-learning keys and strips;
- automatic filter scale cal, with one optional gesture (EMPHASIS full), as rev 0 §4.

## v1.3 One-unit BOM (one-off)

Prices as listed 2026-11-12, quantity 1. **US** = ships domestically.

### Electronics
| Item | Qty | Unit | Ext. | Source |
|---|---|---|---|---|
| ~~Raspberry Pi Pico 2~~ **[rev 13] replaced by the Daisy Seed, §v1.11.1** | ~~1~~ | ~~$5.75~~ | ~~$5.75~~ | ~~SparkFun~~ |
| MCP4822-E/P DAC, DIP-8 | 2 | ≈ $3.99 | $7.98 | Price basis [TME $3.99](https://www.tme.com/us/en-us/details/mcp4822-e_p/d-a-converters-integrated-circuits/microchip-technology/). **US** DigiKey/Mouser at about the same price is ESTIMATE |
| **AS3046 DIP-14** | 3 | ≈ $5.20 (€4.50 ex VAT) | $15.60 | [Electric Druid, 350 in stock](https://electricdruid.net/?p=15205) (EU, so duty applies). **US**: [Amplified Parts / Tubes and More](https://www.tubesandmore.com/node/45569/ask) lists the DIP, price not shown (ESTIMATE same). Order the DIP; the AS3046**D** is SOIC ([Erica](https://www.ericasynths.lv/shop/ics/as3046d-npn-transistor-array)) |
| **Tempco 2 kΩ +3300 ppm** | 3 | ≈ $2.50 | $7.50 | **US** [MFOS](https://musicfromouterspace.com/analogsynth_new/ELECTRONIC_PARTS/MFTEMPCO3300.php), price not shown: **ESTIMATE** |
| JFETs for ramp buffers (bag, matched in the Pico jig) | 10 | — | $2.00 | ESTIMATE |
| TL072CP | 13 | ≈ $0.30 | $3.90 | Tayda, ESTIMATE (LCSC is [$0.22](https://lcsc.com/product-detail/FET-InputAmplifiers_Texas-Instruments-TL072CP_C7236.html) but no longer rides in a JLC box. [DigiKey $0.869 @10, 0 stock until 28 Dec](https://www.digikey.com/en/products/detail/texas-instruments/TL072CP/277421) would be $11.30) |
| LM386 | 1 | $0.23 | $0.23 | [Tayda](https://www.taydaelectronics.com/ic-integrated-circuits/lm386-lm386l-audio-power-amplifier-ic.html) |
| CD4067 DIP-24 | 3 | ≈ $0.60 | $1.80 | ESTIMATE |
| MC34063 ×2 + inductors, Schottkys, 78L09/79L09 | — | — | $2.60 | ESTIMATE (Tayda), basis [LCSC $0.3989](https://www.lcsc.com/product-detail/C126078.html) |
| 6N138 MIDI-in set | 1 | — | $0.60 | ESTIMATE |
| 2N3904 ×100 / 2N3906 ×30 | — | $0.02 | $2.60 | [Tayda A-111](https://www.taydaelectronics.com/catalogsearch/result/?q=2n3904); 2N3906 ESTIMATE |
| SS49E linear Hall | 30 | $0.38 | $11.40 | **US** [Addicore](https://addicore.com/SS49E-Linear-Hall-Sensor-p/ad316.htm). Tayda's [$1.99 is out of stock](https://taydaelectronics.com/ss49e-linear-hall-effect-sensor-ic.html) |
| Resistors ≈ 350 **[rev 10] 1/8 W metal film (standing, ≤ 6.5 mm)** | — | $0.015 | $5.25 | [Tayda](https://taydaelectronics.com/resistors.html); [1/8 W range](https://www.taydaelectronics.com/resistors/1-8w-metal-film-resistors.html), price ESTIMATE same |
| Film caps ≈ 20 | — | $0.10 | $2.00 | [Tayda](https://www.taydaelectronics.com/0-1uf-100v-5-polyester-film-box-type-capacitor-jfj.html) |
| Electrolytic/ceramic ≈ 90, diodes, LEDs | — | — | $3.95 | ESTIMATE |
| IC sockets, Pico headers | — | — | $3.00 | ESTIMATE (no inter-board ribbons now) |
| **Subtotal** | | | **≈ $76.2** | |

### Panel and speaker
| Item | Qty | Unit | Ext. | Source |
|---|---|---|---|---|
| 9 mm pots, linear knurled. **[rev 10] All 23 pots: Tayda A-5622, T18 spline, $0.59.** The A-5531 is a 40-tooth knurl and won't key 18T knobs. The 100k contour pots in §v1.10 also need T18 (stock UNVERIFIED) | 19 | $0.45 | $8.55 | [Tayda](https://www.taydaelectronics.com/catalogsearch/result/?q=b10k); [A-5622](https://www.taydaelectronics.com/tayda-10k-ohm-linear-taper-potentiometer-spline-shaft-pcb-mount-9mm.html). **+$3.22** (counted in §v1.10) |
| 9 mm 1 MΩ (contour A/D) | 4 | $1.29 | $5.16 | [Tayda A-1882](https://www.taydaelectronics.com/potentiometer-variable-resistors/rotary-potentiometer/linear/1m-ohm-linear-taper-potentiometer-round-shaft-pcb-9mm.html) |
| Knobs (19 split-shaft + 4 set-screw + 3 rotary). **[rev 10] Black 6 mm × 18T push-on on all pots. WAVE: 18T if the RS16211 spline is 18T (UNVERIFIED), else set-screw** | 26 | $0.30 / $0.42 | $8.28 | [Tayda knobs](https://www.taydaelectronics.com/potentiometer-variable-resistors/rotary-potentiometer/knobs.html) |
| Rotary switch 1P8T (stop set to 6) | 3 | $1.21 | $3.63 | [Tayda RS16211](https://www.taydaelectronics.com/mini-rotary-switch-1-pole-8-position-alpha-rs16211-20mm.html) (PCB-mount version: ESTIMATE same price) |
| Sub-mini toggles, PCB | 6 | $0.80 | $4.80 | [Tayda](https://www.taydaelectronics.com/non-threaded-sub-mini-toggle-switch-spdt-on-none-on-short-handle-gold-pcb-pins.html) |
| Power switch | 1 | — | $0.30 | ESTIMATE |
| 3.5 mm jacks | 6 | $0.12 | $0.72 | [Tayda PJ-302](https://www.taydaelectronics.com/pj-302-3-5-mm-mono-phone-jack-3691.html) |
| ~~Speaker 3" 8 Ω~~ **[rev 9] Speaker 50 mm 8 Ω 1 W, 7.6 mm deep** | 1 | ~~$1.95~~ **$3.88** | **$3.88** | ~~Adafruit #1313~~ (25.5 mm deep, doesn't fit) **US** [DigiKey Same Sky CDS-5076-1SP](https://www.digikey.com/en/products/detail/same-sky-formerly-cui-devices/CDS-5076-1SP/22521367); alt. [PUI AS05008MR-4-R $4.13, 7.2 mm](https://azcus.digikey.com/en/products/detail/pui-audio-inc/AS05008MR-4-R/1745548) |
| **Subtotal** | | | **≈ $33.4** | |

### Keys and mechanics
| Item | Ext. | Source |
|---|---|---|
| 25 magnets 5 × 2 mm (**replaced by the chosen key option**, §v1.4) | $8.00 | [Magnet Baron $15.99/50](https://themagnetbaron.com/products/10-3-16-x-1-16-disc-super-strong-rare-earth-magnets-neodymium-n35-nicuni) (sold out when checked), so ESTIMATE |
| PETG (case sides only; keys are now bought parts, §v1.4) | $3.50 | ESTIMATE. $1.50 of it was key allowance, replaced in §v1.4 |
| Felt/TPU stops (silence), feet, standoffs, screws | $5.00 | ESTIMATE |
| Laser-cut ply/acrylic top + bottom (Vector Space) | $12.00 | ESTIMATE |
| **Subtotal** | **≈ $28.5** | |

**Parts total ≈ $138** (no bend/mod controller, no battery).

### Board: one design, quantity 1 (≈ 280 × 170 mm, 2-layer, ≈ 73.8 in²)

| Fab | Origin / tariff | What's published | One-board cost |
|---|---|---|---|
| **Advanced Circuits BareBones** | USA, no tariff | Min qty 1, **no soldermask or silkscreen**, **$20 handling per order** (per the orchestrator from [4pcb pricing](https://4pcb.com/pcb-prototype-2-4-layer-boards-pricing.html), which now redirects to advancedpcb.com; I could not load it), size 1 × 1 in to 10 × 16 in ([AC BareBones](https://advancedpcb.com/en-us/barebones-special)). Per-board/area price not readable | **ESTIMATE $75–130** = board $45–90 + $20 handling + shipping $10–20. Basis: AC's full-spec "$33 each" special covers boards up to 60 in², minimum 3 ([AC](https://www.advancedpcb.com/en-us/33-each-special/)), so AC prices this size class in the tens of dollars, and BareBones is their cheaper no-mask line |
| **Pad2Pad** | Ships from Mahwah, NJ; **free shipping** in the contiguous US; no minimum ([FAQ](https://www.pad2pad.com/faq/)) | Instant online quote, no published table | **ESTIMATE $100–200** (typical US quick-turn qty-1 pricing for ~74 in²; no data) |
| **PCBCart** standard | **Thailand or China** factory ([PCBCart](https://www.pcbcart.com/pcb-fab/standard-pcb.html)), so tariff applies (China ≥ 35 % per [JLC FAQ](https://jlcpcb.com/help/article/us-tariff-policy-faq); Thailand lower, UNVERIFIED) | Order qty "1pc – 10,000,000 pcs", instant quote | **ESTIMATE $60–110** (board $30–60 + shipping $20–35 + duty) |
| **AtlasPCB** | **Origin not stated**; the site links a "PCB Manufacturer China" page, so assume China tariff. DHL Express extra ([Atlas pricing](https://atlaspcb.com/pricing/)) | Tooling and e-test included, quote by Gerber upload | **ESTIMATE $60–110** |
| **Ponoko** | "Made in USA", though its FAQ says facilities are "around the globe"; $0 setup, no MOQ ([Ponoko](https://www.ponoko.com/printed-circuit-boards-fabrication-assembly)) | Quote by request only | No basis. Get a quote |
| OSH Park (reference) | USA | **$5/in² for 3 copies** ([OSH Park](https://docs.oshpark.com/services/two-layer/)), so a quantity-3 minimum | $369 for this board, ruled out (minimum and price) |

**Provisional choice:** BareBones at **$75–130**, the range used in the totals.
- **Trade-off:** no soldermask means easier solder bridges on a dense hand-soldered board, and no silkscreen means you need a printed placement map. THT at 2.54 mm pitch is manageable.
- **Full-spec board instead:** the cheapest real quote among Pad2Pad, PCBCart and Atlas wins. The quotes may come in under the ESTIMATE range.
- **Why one board:** each quantity-1 order carries its own fixed fee or tooling. One 73.8 in² design beats rev 1's 5 designs (≈ 96 in² total, with 5 fees) on both area and fees [ENG].

### Shipping and duty (ESTIMATE unless cited)
| Order | Shipping | Note |
|---|---|---|
| Tayda (pots, knobs, switches, passives, TL072, MC34063 ≈ $60) | $6–10 + ≈ 10 % duty ≈ $6 | [PedalPCB forum](https://forum.pedalpcb.com/goto/post?id=311248) (2024 rates); duty rate UNVERIFIED |
| One US order (DigiKey or Adafruit/SparkFun): Pico, MCP4822 ×2, speaker, + LiPo/charger, + SoftPots if chosen | ≈ $6–8 | — |
| Addicore (Hall), **US** | ≈ $4–6 (free over $50 per [Addicore](https://addicore.com/SS49E-Linear-Hall-Sensor-p/ad316.htm)) | — |
| AS3046 (Amplified Parts US, or Electric Druid EU + duty) | ≈ $6–10 | — |
| MFOS tempcos, **US** | ≈ $3–5 | — |
| Board | in the board line | — |
| **Total** | **≈ $31–43** | |

## v1.4 Keys (rev 4): one switch per key, owner-cut key tops

Owner decisions:
- no harvested keybeds;
- one bought switch per key;
- key tops laser- or CNC-cut by the owner at Vector Space (material cost only).

Options are from `key-sourcing.md`. Both use a **key-strip PCB** (≈ 280 × 25 mm, ≈ 10.9 in²) in the **same fab order** as the main board.

| | **KC: Kailh Choc V2 silent** (Deep Sea Mini) | **KH: Gateron low-profile Hall** (HE Jade Pro class) |
|---|---|---|
| Switches | $0.70 × 25 = **$17.50** (keeb.io, US; per `key-sourcing.md`) | $0.84 × 25 = **$21.00** (Nuphy, US; per `key-sourcing.md`; stock to confirm) |
| Sensors | none (contacts) | 30 × SS49E-class linear Hall = **$11.40** ([Addicore](https://addicore.com/SS49E-Linear-Hall-Sensor-p/ad316.htm)). These switches are built for a PCB Hall sensor under the magnet stem; fit of a TO-92 part under a low-profile switch is UNVERIFIED, and an SOT-23 sensor would be SMD (not allowed) |
| Key tops | 2 sheets of 1/8" cast acrylic, white + black, 5 × 10 in, **$3.99 each** ([3D Universe](https://shop3duniverse.com/products/1-8-solid-cast-acrylic)), ≈ $8 + shipping ≈ $5 (ESTIMATE). Delrin is similar or more (ESTIMATE); makerspace scrap is $0 | same |
| Stem adapter | Laser-cut cross hole in the top, or glue the top onto a bought blank cap (≈ $0.15–0.30 each, `key-sourcing.md`/ESTIMATE): $0–5 | same |
| Strip PCB area | In the board line (§v1.10) | same |
| **Key cost** | **≈ $25–36** | **≈ $40–50** (+ ≈ $5 Addicore shipping) |
| Velocity | **No** | **Yes** |
| Silence | **Quietest** (dampened both strokes) | "Moderately quiet", no click |

**Superseded by §v1.4b (velocity required).** KC alone has no velocity.
The magnets and Hall sensors in the rev 1–3 base BOM ($20.90 including key plastic) are removed and replaced by the line above.

## v1.4b Velocity keys, through-hole only (rev 6: owner "i want velocity")

Velocity is now required. KC (Choc without sensing) is out. Three through-hole routes:

| Route | How | Geometry / buildability | Silence | Key cost | Verdict |
|---|---|---|---|---|---|
| **(a) Gateron low-profile Hall switch + TO-92S SS49E** | The switch carries its own magnet. Gateron quotes ≈ 122 G at rest to ≈ 550 G at bottom-out at the sensor in a 1.2 mm-PCB configuration ([Gateron](https://gateron.com/blog/detail/hall-sensor-magnetic-keyboard-switches)). With SS49E sensitivity of ≈ 1.4–2.0 mV/G that is a ≈ 0.6–0.9 V swing [ENG] | The switches are designed for a **surface-mount sensor under the switch**; Gateron doesn't publish where. A TO-92S (≈ 4 × 3 × 1.5 mm) can't stand under a seated switch. The through-hole workaround is to **lay it flat, face up, in a slot cut in the key-strip PCB** (1.5 mm body in a 1.6 mm board), leads bent to pads, so its face sits about where the SMD part would. The position is UNVERIFIED and needs a 1-switch test. No ready-made "Hall-switch sensor module" was found | "Moderately quiet", no click (`key-sourcing.md`) | $21.00 switches + $11.40 sensors + $8 acrylic + $5 shipping + $0–5 adapters = **≈ $45–50** | Cheaper by ≈ $5, but the sensor position is unverified and the switches are louder. **Fallback** |
| **(b) Choc V2 silent switch for feel and return + magnet in the laser-cut key top over a TO-92 SS49E on the key strip** (the full version's approach) | Choc V2 is a plain mechanical switch with no magnet (only a small steel spring and contacts: a fixed offset, calibrated out). A 5 × 2 mm magnet is glued into a laser-engraved pocket under the key top, **beside the switch along the key's length** (a white key top is ≈ 50–60 mm long). The SS49E **stands on the key strip** under it, with its leads trimmed so its face sits ≈ 3.5 mm below the magnet at rest. Choc V2 travel is 2.8 mm (`key-sourcing.md`), so the gap goes ≈ 3.5 → 0.7 mm: a large swing, likely hundreds of gauss [ENG; verify with a test key] | **All through-hole.** No PCB slots. Sensor position is free to choose, not dictated by a switch vendor. 25 analog channels on the existing CD4067s; velocity from time-of-travel between two thresholds. Power the SS49Es at 3.3 V so the output stays inside the Pico ADC range (SS49E runs from 2.7 V; confirm on the datasheet). Long tops on a single stem may rock, so the design team needs to guide or stabilise them | **Quietest**: dampened switch, contactless sensing | $17.50 switches + $11.40 sensors + ≈ $8 magnets (ESTIMATE; [Magnet Baron $15.99/50](https://themagnetbaron.com/products/10-3-16-x-1-16-disc-super-strong-rare-earth-magnets-neodymium-n35-nicuni) sold out) + $8 acrylic + $5 shipping + $0–5 adapters = **≈ $50–55** | **Recommended** |
| (c) Dual-contact conductive-rubber strips, timed by the Pico | Dual-contact (note + velocity) 12-note rubber strips are sold as **spare parts for specific keyboards** (e.g. a Korg/Kurzweil-family 12-note strip, price not shown: [Keyboard Kountry](https://www.keyboardkountry.com/key-contact-strip-12-notes-for-triton-le-studio-88-extreme-88-some-pa-series)) | Contact pitch matches *that* keyboard (full-size octave ≈ 164 mm; our octave is ≈ 131 mm), so it doesn't fit our key pitch. Needs an interdigitated contact PCB and key levers that press the domes. It is also close to the "harvested keybed" route the owner ruled out | Good (rubber) | Unknown | **Not recommended** |
| (c′) Two switches per key at different heights | — | Impractical (per brief) | — | — | Rejected |

**[rev 8] Superseded by `velocity-and-keys-v2.md` §2:** route (b) stays, now with short tops (no rocking), K&J D31 magnets at a 5.6 / 2.8 mm rest/bottom gap (magnet face 7.6 mm above the strip at rest), flat sensors and the LDO counted. RAIL/FLOAT/COMB are out (owner: "I don't want to build custom keys"). Gateron route (a) remains the fallback.

**Recommendation (rev 6): (b), Choc V2 silent + key-top magnet + standing TO-92 SS49E.** It is through-hole only, the quietest of the three, uses the same sensing as the full version (one firmware), and lets us set the sensor geometry ourselves.

**Before ordering the board:** buy 2 Choc V2 + 2 Gateron low-profile Hall switches + 5 SS49E (≈ $8) and measure both setups on perfboard. If (a)'s flat-in-slot sensor reads well, it saves ≈ $5.

**Rev 7 corrections (2026-11-12, `keys-answers.md`). These apply to every Hall route, including RAIL:**
- **Gap.** A 5 × 2 mm N35 magnet gives ≈ 2,100 G at a 0.7 mm gap. The SS49E at 3.3 V is linear only to ≈ 650–760 G. Use a **bottom gap of ≈ 2.8 mm and a rest gap of ≈ 5.6 mm** (≈ 470 G, ≈ 530 counts of swing). N52 gains nothing.
- **Orientation.** The **SS49E lies flat, face up** (leads bent 90°), not standing: it senses the field perpendicular to its branded face.
- **Power.** 25 sensors draw 150–250 mA at 3.3 V, so strip C gets **its own 3.3 V LDO** (≈ +$0.50); the Pico's 3V3 pin is limited to < 300 mA. **[rev 8]** Part: LD1117V33 TO-220 from 5 V. Worst case 0.43 W, no heatsink. ≥ 10 µF output cap (UNVERIFIED). Now counted in the keys row. LiPo runtime ≈ 3.5–5 h if v1.2's power budget excluded the sensors (`velocity-and-keys-v2.md` §2.4).
- **Velocity.** Use a least-squares slope fit on linearised depth. Scan at ≥ 4 kHz per key (≈ 8–10 kHz is possible).
- ~~**Velocity CV.** Velocity has no CV destination yet: both MCP4822s are full.~~ **[rev 8]** Solved without a DAC: a PWM CV into the spare AS3360 half scales the loudness contour, and the filter gets a firmware offset on CUTOFF (`velocity-and-keys-v2.md` §1).

## v1.5 Bend/mod (rev 5): cheapest bought options, incl. mini joysticks

**Electrical confirmation [ENG].** Bend and mod both go through the Pico's ADC, via 2 channels of the CD4067 muxes (35 of 48 used; a second stick would use 37).

| Axis | How it works | Extra parts |
|---|---|---|
| **X = pitch bend** | Added digitally to the VCO pitch values before the MCP4822s, as the rev 1 strips did | None. Spring-to-centre is mechanical on these sticks |
| **Y = mod depth** | Little D's mod path is analog (osc 3/noise → MOD MIX → OSC/FILTER MOD). A Pico-read controller needs a **voltage-controlled depth stage**. Adopt the full version's **E1 design**: an **AS3360** VCA (DIP-14) in the mod path after MOD MIX, CV from a Pico PWM + 2-pole RC, feedthrough auto-nulled at autotune (`answers-E1-E10.md`, `architecture-v2.md`) | **≈ +$5–8** (AS3360 ≈ $4–6 UNVERIFIED per v2; TL072 half, RC, optional H11F1 mute) |

So a joystick works electrically **once the AS3360 mod VCA is added**. This was missing from rev 1–4 Little D costs. It applies to **every Pico-read bend/mod option** (sticks, SoftPots, thumbwheels).

The only option that needs no VCA is a wheel pot wired **passively** into the mod path, as on the original. That gives up MIDI CC1 control of mod depth.

A **MOD DEPTH pot** (9 mm pot + knob, ≈ $0.75, Tayda) gives latched mod. Firmware uses whichever of the pot or stick Y is higher, since a stick's Y snaps back.

| Option | Part | Qty-1 price (US) | Size / mounting | Notes |
|---|---|---|---|---|
| **M1. One mini analog stick** (X bend, Y mod): the small "guitar-tone-switch"-sized lever | **Adafruit #2765 Mini 2-Axis Analog Thumbstick**: 2× 10 kΩ, self-centring | **$2.50** ([Adafruit](https://www.adafruit.com/product/2765), in stock) | **17.5 × 17.4 × 12 mm, through-hole** | **Cheapest bought bend/mod.** Pin pitch not listed (check the drawing). Sits on the main or key-strip PCB under a panel hole |
| M2. **Two mini sticks** (e.g. left = bend/mod, right = assignable: filter mod or glide) | 2× Adafruit #2765 | **$5.00** | as above | 2 more ADC channels (37/48 used). Each extra CV destination beyond pitch needs its own CV path (PWM-CV); the second stick's targets are firmware-assignable |
| M3. Mini Joy-Con-style stick | Adafruit #5628, 2× 10 kΩ, self-centring | $5.95 each, sold in 2s ([Jameco listing](https://www.jameco.com/z/5628-Adafruit-Industries-Mini-Analog-Thumbstick-Similar-to-Joycon-Style_2525887.html)) | 2 mm pin pitch (not 0.1") | Smaller cap profile. Higher price |
| J1. PS2-size thumb stick, bare | SparkFun COM-09032, spring-return | $5.25 ([SparkFun](https://www.sparkfun.com/thumb-joystick.html)) | Larger; pins not on 0.1" (breakout optional) | Bigger thumb surface |
| J2. PS2-size stick on a breakout | Adafruit #512 (with select button) | $5.95 ([Adafruit](https://adafruit.com/products/512)) | Breakout board, 0.1" header | Easiest to wire. Centring not stated on page |
| J3. Adafruit 2-axis joystick module | Adafruit #245, 2× 10 kΩ, sprung | $9.95 ([Adafruit](https://www.adafruit.com/products/245), 40 in stock) | Larger module | — |
| (ALPS RKJXV1224005) | — | Not buyable: **obsolete**, "restricted availability" ([Mouser](https://www.mouser.com/ProductDetail/688-RKJXV1224005)) | — | ALPS RKJXM-class parts are digital (switch) sticks, not analog |
| B. SoftPot strips ×2 | SparkFun SEN-08680 | $17.90 ([SparkFun](https://www.sparkfun.com/softpot-membrane-potentiometer-50mm.html)) | Flat | Cheaper than any wheel |
| A2. Doepfer sprung pitch wheel + thumbwheel | — | ≈ $29–35 incl. EU shipping | Wheels | A passive in-circuit mod wheel could skip the VCA (no MIDI CC1) |
| A1. Two Doepfer wheels | — | ≈ $41–47 | Wheels | — |

**Ranking (with the +$5–8 mod VCA on the Pico-read options):**

| Option | Total |
|---|---|
| M1 mini stick | ≈ $8–11 |
| M2 two mini sticks | ≈ $11–14 |
| PS2-size sticks | ≈ $11–15 |
| SoftPots | ≈ $24–27 |
| Hybrid wheels | ≈ $29–43 |
| Two wheels | ≈ $41–55 |

**Pick for cost: M1, one Adafruit #2765 mini stick plus the MOD DEPTH pot.**

### v1.5b Rev 7: bend springs back (one direction), mod stays put

Owner: "joystick is great if we can go one direction". **Mod = a plain dial** (stays put): the existing MOD DEPTH 9 mm pot + knob, ≈ $0.75 (Tayda).

| # | Single-axis spring-return bend control | Qty-1 price (US unless noted) | Findings | Verdict |
|---|---|---|---|---|
| 1 | **True single-axis spring-return lever pot** | **≈ $229+**. ETI Systems J3R-I-10K, 1-axis, 10 kΩ, surface-mount rocker, **$229.39** ([DigiKey joystick-pot listing](https://www.digikey.com/en/products/filter/joystick-potentiometers/82)). Novotechnik LS1 "with return spring" exists ([datasheet listing](https://datasheets.globalspec.com/ds/Novotechnik-U-S/ls1-series-with-return-spring/9e049a2e-ac62-41a0-81b6-351e138c96b8)), price not shown, industrial class | The cheap through-hole joystick pots found are all **2-axis**: Favor FJR10K (£2.71, 26°, [DigiKey UK](https://www.digikey.co.uk/en/products/detail/favor-electronics/FJR10K-S1B10KD0/16627935)) and FJP10K (45°, [DigiKey](https://www.digikey.ca/en/products/detail/favor-electronics/FJP10K-0118A/17737265)), marketplace sellers shipping in ≈ 14 days. Spring-return slide pots: none found at hobby prices | **Out**: only industrial parts, ≈ 100× the budget |
| 2 | **Adafruit #2765 mini stick, one axis used, gated by a slot in the laser-cut panel** | **$2.50** ([Adafruit](https://www.adafruit.com/product/2765); [DigiKey $2.50, 613 in stock](https://www.digikey.com/en/products/detail/adafruit-industries-llc/2765/6193582)) | Through-hole, 2× 10 kΩ, self-centring, 17.5 × 17.4 × 12 mm. **Throw angle not published** (DigiKey lists none; datasheet not read), so it's UNVERIFIED. **Gate design [ENG]:** a slot in the panel (or in a 1.5–3 mm Delrin gate plate under it) as wide as the stem plus ≈ 0.3 mm, as long as the full throw, at the stem height between body and cap. Fit the cap after the panel. Arcade "restrictor gates" work the same way. Gate loads are light thumb forces. The only wear point is the stick's plastic pivot rubbing the slot edge, so Delrin is the right gate material (low friction). Only one axis (X) is read; Y stays centred by the gate. **Risk:** DigiKey calls the actuator a "puck"; if the cap slides rather than tilts on a stem, a slot can't capture it. Check one part in hand before cutting the panel | **Recommended**: cheapest, and it gives the owner's one-direction spring-back stick |
| 2′ | SparkFun COM-09032 thumb joystick, gated the same way | **$5.25** ([SparkFun](https://www.sparkfun.com/thumb-joystick.html)), spring-return | Bigger PS2-style lever with a clear stem, so it's easier to gate, but its pins are not on a 0.1" grid | Backup if #2765 can't be gated |
| 3 | **Spring-return rotary pot** | None found at qty 1 | Center-*detent* pots exist (e.g. a 9 mm center-detent pot at [Stompbox Parts](https://stompboxparts.com/potentiometers/9mm-potentiometer-center-detent)), but a detent clicks to centre, it doesn't spring back. The cheapest real sprung rotary control is the **Doepfer wheel kit** (pot + return spring), [€15 incl. VAT](https://schneidersladen.de/en/doepfer-mod-wheel-single-wheel-diy-kit), ≈ $27–33 with EU shipping | Wheel fallback |

**Locked bend/mod (cost):**

| Part | Cost |
|---|---|
| **#2765 mini stick, slot-gated to one axis (bend, springs back)** | $2.50 |
| **MOD dial** (stays put) | $0.75 |
| **AS3360 mod VCA** (needed because the dial is Pico-read, for MIDI CC1) | $5–8 |
| **Total** | **≈ $8.25–11.25** (unchanged from rev 5) |

Optional cut: wire the MOD dial **passively** into the analog mod path, as on the original, and skip the VCA. That saves **$5–8** with no sound loss, but mod depth is then not MIDI-controllable. **[rev 8] The cut no longer removes the AS3360:** its half B now carries velocity → loudness, so the saving falls to ≈ $0.

## v1.6 Internal battery: in or out
| | USB power bank (out) | **Internal LiPo (in), recommended** |
|---|---|---|
| Parts | $0 (owner's bank or charger) | **Adafruit bq25185 USB-C charger + 5 V boost #6106, $8.95**, with load-sharing (plays while charging), 1 A boost ([Adafruit](https://www.adafruit.com/product/6106)) + **2000 mAh LiPo #2011, $12.50** ([Adafruit](https://adafruit.com/products/2011)) = **$21.45** |
| **[rev 11] Cells** | n/a | **2 × 50 × 60 mm pouch, 1S2P, one JST-PH each, joined by a Y-harness:** PiShop 755060 3000 mAh 7.5 mm $15.95 ea (**$31.90**, 22.2 Wh) or Adafruit #328 2500 mAh 7.3 mm $14.95 ea (**$29.90**, 18.5 Wh, in stock). With bq25185 #6106 $8.95: **$40.85 / $38.85**. Details, links, safety: `battery.md` |
| **[rev 12] FOLD band cells** | n/a | **4 × PiShop 952540, 9.5 × 25 × 40 mm, 750 mAh, PCM, JST-XH, $7.95 ea, in stock** ($31.80, 11.1 Wh, 1S4P); star harness with a 2 A fuse, optional ≈ 1 A PTC per cell lead; XH→PH adapter; **$40.75** with #6106; runtime ≈ 4.5 h / 2.4 h; charge ≈ 3.3 h at 1 A. Thickness 9.5 is at the band limit: measure one first. `fold-answers.md` §1 |
| Runtime | Depends on the bank | ~~≈ 5–7 h at 1.0–1.5 W [ENG]~~ **[rev 10] ≈ 1.8–3.3 h at 2.0–3.6 W** (single #2011). **[rev 11] 1S2P 6000 mAh: ≈ 4.7–9 h; 1S2P 5000 mAh: ≈ 3.9–7.5 h; charge ≈ 6–7 h at the default 1 A.** ~~A 3000 mAh 7.5 × 50 × 60 pouch (PiShop 755060; size UNVERIFIED) fits under the flat concepts' board: ≈ 2.7–5 h~~ |
| Caveats | Banks may auto-off at low draw; there's a cable hanging off it | The boost "stalls above ≈ 200 mA when a high-current load switches on instantly" (Adafruit page), so the ±12 V converters need soft-start: an RC on the MC34063s, plus Pico-sequenced LM386 enable. It also means **two USB ports**: USB-C to charge, micro-USB on the Pico for MIDI. Option [ENG]: feed the Pico's VBUS into the charger's 5–18 V DC pads, so the Pico port charges too |
| "Completely portable" | Not really | **Yes** |

**Recommendation: in.** It costs ~~$21.45~~ **[rev 11] $38.85–40.85 with the two-cell bay**, rides on the same Adafruit order, and is the only way to meet the owner's
"completely portable".

## v1.7 Remaining ESTIMATE items
**The board: $75–130, the largest unknown.** Replace it with real instant quotes (see "Next action" in §v1.0).

**Priced, but the figure carries a caveat:**
- AS3046 DIP: EUR price converted, and the US price is not shown.
- MCP4822: priced at TME; US price assumed similar.
- Magnets: sold out at the cited price.
- The PCB-mount rotary version: assumed the same price.

**Pure ESTIMATE:**
- tempcos (MFOS shows no price);
- Tayda TL072 and MC34063;
- CD4067;
- 2N3906;
- JFET bag;
- caps, diodes, LEDs;
- sockets and headers;
- power passives;
- 6N138 set;
- power switch;
- PETG, felt, hardware and laser-cut materials;
- all shipping except Tayda's;
- Tayda duty rate;
- the bend/mod option C and the wheel spring.

## v1.8 New risks
| Risk | L | Mitigation |
|---|---|---|
| One-board design: a single layout error means re-fabbing the whole board | M | Full netlist cross-check against the CA-72 reference (v1 §7.0), ERC/DRC, and a 1:1 paper print to test-fit parts before ordering |
| No soldermask (if BareBones) on a dense board | M | Generous pad spacing, wider clearances; or pick a full-spec quantity-1 quote |
| Components under the keys must stay ≤ 8 mm | L–M | Low-profile electrolytics, nothing tall in the front region; check in a 3D model |
| AS3046 DIP availability in the US | M | Order early; the CA3046 is pin-compatible if Tayda restocks ($1.10); Electric Druid has 350 |
| bq25185 boost stall at power-up | M | Soft-start the MC34063s and sequence the loads (§v1.6) |
| **[rev 9]** Speaker/battery height under the main board | M | 7.6 mm speaker + 0.5 mm air: no THT lead tails over the speaker (≈ 54 mm keep-out) or the battery (`little-d-design-answers.md` §1.3) |
| **[rev 9]** UNDER GLASS only: window band (y 80–96) holds 3 × AS3046 + tempcos and the ladder | L–M | Parts ≤ 6.5 mm seated; tempco bonded to its chip; LD1117, MC34063s, 78L/79L09, LM386 ≥ 25 mm and key harness/CD4067s/Pico ≥ 20–25 mm from windows; strip-C connector not under a window (§2 there) |
| **[rev 9]** HUSH only: felt gripping the moving peg shank | M | Uneven velocity and slow return; holes clear the shank ≥ 0.5 mm radial (§3.4 there) |
| Matched JFETs for the discrete ramp buffer | M | Pico Idss jig with a bag of 10; fallback is the LSK489 (+$38) |
| **[rev 10]** WAVE rotary (Ø 16) and sub-mini toggle **body heights** vs the 7 mm under-panel space | M | Measure one of each before freezing panel z. If > 7 mm: a board cutout with flying leads, or a local spacer (`round4-answers.md` §5) |
| **[rev 10]** FOLD lid board ≈ 9–12k mm² short | H (FOLD) | Design picks: deeper halves, a stacked lid board, or a digital board under the keys (§1.4 there) |
| **[rev 10]** FOLD: EMPHASIS across the hinge ribbon picks up scan-rate tones | M (FOLD) | Keep EMPHASIS on the ladder's half. If it must cross: low-Z drive, series R at the ladder, ground guards, 40-way ribbon, bench test first |
| **[rev 10]** Boost stall with 0.4–0.7 A total load | M | Sensor LDO switched on last (P-FET), MC34063 soft-start |
| **[rev 12]** FOLD depth set by lid board area, not only the battery | H (FOLD) | D ≥ 6 + (23,300 + A)/262 mm. With the ladder in the lid: 95 (no cell), 113 (slim 4-cell), 121 (22 Wh). With the ladder in the base: 87 / 105 / 113. Rev 4.2's lid board recounts at ≈ 20,260 mm² (< 21,500): recount (`fold-answers.md` §1.3) |
| **[rev 13]** Seed module height and USB-connector position unverified; a stock socket stack may exceed the 8 mm underside limit | M–H | Buy one, measure, before freezing z and the rear edge (§v1.11.3) |
| **[rev 13]** Boost headroom: 4.4 W ≈ 0.88 A at 5 V against the bq25185 board's 1 A boost | M | Measure real draw in the spike; a 3.3 V buck for the sensor LDO saves ≈ 0.2–0.4 W; fallback a ≥ 2 A boost module (+$6–12) |
| **[rev 13]** Seed supply (2026 production pause reported, price rise Nov 1) | M | Check stock before order; Seed3 and Seed2 DFM are pin-compatible |
| **[rev 14]** FSR repeatability/creep; UX 408 trimmability UNVERIFIED | M | Auto-zero + learned dead zone; spike test A1 trims one first; fallback SparkFun FSR 408 ($30.95) or a Velostat lane (`aftertouch.md` §7) |
| **[rev 14]** Force bypass: anything but the lanes touching the floating strip C (key tops on the window, taut harness, felt) | M | ≥ 1 mm key-top clearance in the window, slack harness, nothing in the shell touching strip C |
| **[rev 14]** Strip C may not fit two 6 mm lead-free lanes; FOLD's single base board can't float | M | Check at placement (fallback: one lane + per-key gain from the Halls); FOLD splits keys from the PLAY board |
| **[rev 12]** FOLD EMPHASIS in the base: scan-tone pickup on the emphasis-input wire | M (FOLD) | Supersedes the rev 10 row's premise: it's a 2-wire rheostat between low-Z nodes, and SPICE shows no response or onset change. The emphasis-input wire goes at the far ribbon edge with ground each side, ≤ 0.1 pF to S0–S3 (SPICE: −70 dB). 40-way ribbon. Bench pass ≤ −70 dB re note. Fallback: a separate 5-way cable, or EMPHASIS back in the lid (`fold-answers.md` §2) |

## v1.9 Cost-cut ladder toward ≈ $200 (one unit; rev 3, final numbers in §v1.10)

**Baseline (rev 3, all bought keys, knobs and wheels):** v1 on a USB power bank, **K3 silent switches**, and **A2 hybrid wheels**.
That is **≈ $269–345, midpoint ≈ $307**. The internal LiPo would add +$21.45 on top of every line below. Printed knobs, keys and wheels are no longer allowed, so that cut is gone.

Ranked from most dollars per least pain. **Sound?** says whether the cut changes the sound or tuning.

### No sound impact
| # | Cut | Saves | What's lost | Sound? |
|---|---|---|---|---|
| 1 | **Shrink the board to the control area only (≈ 280 × 100 mm, 43 in², down from 74 in²).** The 25 Hall sensors move to a strip of Tayda stripboard under the keys (≈ $2–3, ESTIMATE), with a 28-wire harness to a header | **$16–34** with K1; **≈ $3–27** with K2/K3, which still need a small key-strip PCB in the same order (board area at the ESTIMATE rate of $0.61–1.22/in², from §v1.3) | About 1–2 h of extra wiring. One more mechanical part to mount | No |
| 1b | *Alternative to 1, going further:* **voice-only board (≈ 190 × 100 mm, 30 in²)**. All pots, switches and jacks mount on the laser-cut panel and are wired to the board. Keys on stripboard | **$19–46** net (after ≈ $5 wire + $3 stripboard) | About 4–6 h of wiring (≈ 110 wires) and more chances of wiring errors. A small hum/noise risk on the mixer and ladder lines, so keep those pots closest to the board. Makes cut 7 possible | No, if wired short |
| 2 | **SoftPot strips (B) instead of the A2 hybrid wheels** | ≈ $11–17 | Strips instead of wheels; the owner prefers wheels. Saves the EU shipment | No (playing feel only) |
| 3 | **Consolidate vendors to about 3 shipments**: Tayda, one US distributor order (Pico, MCP4822, speaker, Hall if stocked; ESTIMATE), and the AS3046 source. Drop separate Adafruit/SparkFun/Addicore boxes | ≈ $5–10 (ESTIMATE) | Fewer price choices; some items may cost a little more at the consolidated vendor | No |
| 4 | **Cheaper enclosure**: makerspace scrap acrylic/ply, the owner's walnut offcuts, or a printed shell | ≈ $5–10 (ESTIMATE) | Finish | No |
| 5 | **Bulk magnets** (only if K2 or Hall keys are used) | ≈ $2–4 (ESTIMATE) | — | No |
| 6 | **100k Tayda pots ($0.45) for contour A/D in place of 1 MΩ ($1.29)**, with contour timing scaled in the circuit | $3.36 | Needs the contour ranges re-checked in sim. No loss if done right [ENG] | No |
| 7 | (Only with 1b) **solder-lug toggles** at $0.44 in place of PCB toggles at $0.80 ([Tayda](https://www.taydaelectronics.com/mini-toggle-switch-spdt-on-off-on-mts-103-c1.html)) | $2.16 | — | No |
| — | **Power-rail simplification** | **< $2**: not worth it | The two MC34063s plus regulators cost ≈ $2.60 in total. Two 9 V batteries would save ≈ $2 but lose USB power and add consumables | — |
| | **Running total after 1–6** (K3; cut 5 n/a) | **−$27–67** | | **≈ $242–278, midpoint ≈ $260** (the board saving in cut 1 scales with the board price) |

### Sound or tuning impact (in order of least audible)
| # | Cut | Saves | What's lost | Sound? |
|---|---|---|---|---|
| 8 | **Drop the 3 tempcos** (and the MFOS shipment) | ≈ $11–13 | Timbre is unchanged. Tuning drifts more for the first minutes after a cold start and on room-temperature swings; background re-tune corrects only held notes. A re-tune button press may be needed after warm-up | Tuning stability |
| 9 | **TL072 ramp buffer instead of the discrete matched-JFET buffer** | ≈ $2, plus the JFET matching step | The CA3046-era board's slightly curved ramp ("has some curve to it", v1 §1.2) becomes the linear ramp of later boards. Subtle | Subtle timbre |
| 10 | **Drop the 2nd MCP4822**. VCO 3 shares VCO 2's DAC channel, plus its own analog FREQ offset; filter keytrack comes from a Pico PWM-CV | ≈ $4 | VCO 3's tracking can't be corrected separately, so detune against VCO 1/2 grows across the keyboard (a few cents per octave [ENG]). Filter keytrack becomes slightly noisier and the automatic filter-scale cal is lost | Tuning |
| ✗ | Tactile keys | $10–17 | Cheap tactile switches click, which breaks the owner's "as silent as possible" | **Not recommended** |
| ✗ | Cutting VCO 3, waveforms, a contour, or the speaker | — | Owner decisions / spirit | Not offered |
| | **Running total after 1–10** | **−$44–86** | | **≈ $225–261, midpoint ≈ $243** |

### How close to $200 (rev 3, bought keys, knobs and wheels)
- **Bought keys and wheels add ≈ $25–60** over the printed versions, depending on the K and A/B options.
- **Keeping the sound exactly (cuts 1–6, with SoftPots): about $260 at the midpoint, range $242–278.**
- **With real wheels (no cut 2): about $274 at the midpoint.**
- **Accepting cuts 8–10 (tuning stability, subtle ramp shape): about $243 at the midpoint, range $225–261.**
- **~$200 is no longer reachable** with the current owner rules (3 VCOs, all waveforms, AS3046, bought keys/wheels, qty-1 boards) unless the board quote lands well below its ESTIMATE.
- **The remaining big levers are owner decisions, not engineering:**
  - a 5-piece JLC board order: −$40–90;
  - K3 over K1 keys: about −$20–30 (K1 is already excluded from the baseline);
  - SoftPots over wheels: −$11–17.

## v1.10 Clean one-unit totals (rev 4): the numbers to show the owner

Assumptions:
- one unit, quantity-1 boards;
- all knobs, keys and controllers are bought parts;
- 3 VCOs, all waveforms, AS3046 + tempcos as locked in §v1.2;
- USB power bank (add **+$21.45** for the internal LiPo, §v1.6).

| Line | (a) Cheapest that keeps the sound | (b) + tuning cuts |
|---|---|---|
| Core parts (§v1.3 $138, minus the old key allowance $20.90; **[rev 9]** + $1.93 thin speaker) | $117.10 **→ $119.03** | $117.10 **→ $119.03** |
| No-sound cuts: 100k contour pots (−$3.36), scrap/offcut enclosure (−$5–10) | −$8.36 to −$13.36 | same |
| Keys: **[rev 8] K-v2**: 25 Choc V2 silent soldered to the strip, short pressed-on tops, K&J D31 magnets, flat SS49E, LD1117V33 (`velocity-and-keys-v2.md` §2.5). **$38–43** on scrap acrylic. ~~Lean RAIL alternative~~ (out: owner-built mechanism) | ~~$50–55~~ **$51–56** | ~~$50–55~~ **$51–56** |
| **[rev 8] Velocity routing**: LOUD/BOTH/FILT toggle, TL072, PWM RC passives (AS3360 half already counted) | **≈ $2** | **≈ $2** |
| Bend/mod: **#2765 mini stick slot-gated to one axis** (bend, springs back) $2.50 + **MOD dial** $0.75 + **AS3360 mod VCA** $5–8 (§v1.5b) | $8.25–11.25 | $8.25–11.25 |
| **Boards: main ≈ 280 × 100 mm (43.4 in²) + key strip 280 × 25 mm (10.9 in²), one qty-1 order** (BareBones-class: 54.3 in² at the ESTIMATE $0.61–1.22/in² + $20 handling + $10–20 shipping). **[rev 10] main 268 × 115 (47.8 in²) + strip C 270 × 47 (19.7 in²) = 67.5 in²** | ~~$63–106~~ **$71–122** | ~~$63–106~~ **$71–122** |
| **[rev 10]** T18 spline pots (+$3.22), sensor-LDO P-FET (+≈ $0.30) | +$3.52 | +$3.52 |
| Shipping + duty, ≈ 5 vendors (Tayda, one US distributor, AS3046 source, MFOS, Addicore for the Hall sensors) | $30–39 | $27–34 (no MFOS) |
| Tuning cuts: no tempcos (−$7.50), TL072 ramp buffer (−$2), no 2nd MCP4822 (−$3.99) | — | −$13.49 |
| **One-unit total (velocity keys)** | ~~≈ $255–320~~ ~~[rev 8] ≈ $258–323~~ ~~[rev 9] ≈ $260–325~~ **[rev 10] ≈ $272–345 (midpoint ≈ $308)** | ~~≈ $239–302~~ ~~[rev 8] ≈ $242–305~~ ~~[rev 9] ≈ $244–307~~ **[rev 10] ≈ $256–327 (midpoint ≈ $291)** |
| **[rev 13] Daisy Seed + FX (§v1.11.4)** | **≈ $311–395 (USB); ≈ $356–448 with the 22.2 Wh pack** | **≈ $295–377 (USB); ≈ $340–430 with the pack** |
| With internal LiPo | ~~≈ $276–341~~ ~~≈ $279–344~~ ~~[rev 9] ≈ $281–346~~ ~~[rev 10] ≈ $293–366 (runtime ≈ 1.8–3.3 h)~~ **[rev 11] ≈ $311–386 (two-cell 1S2P, runtime ≈ 3.9–9 h)** | ~~≈ $260–323~~ ~~≈ $263–326~~ ~~[rev 9] ≈ $265–328~~ ~~[rev 10] ≈ $277–348~~ **[rev 11] ≈ $295–368** |

Variants (add to either column):

| Change | Δ |
|---|---|
| Gateron Hall route (a) instead of (b), if the test passes | ≈ −$5 |
| **[rev 8]** Scrap acrylic key tops | ≈ −$13 |
| **[rev 8]** Long piano whites + Choc V2 stabilisers (S2) | +$29.85 |
| **[rev 8]** Velocity → filter *contour amount* via a 2nd AS3360 (instead of cutoff offset) | +$5–7 |
| Two mini sticks (M2) instead of one | +$2.50 |
| SoftPot strips instead of the mini stick | +$15.40 |
| Real wheels (A2 / A1) instead of the mini stick (VCA kept, for MIDI CC1) | +$26–33 / +$38–45 |

**Where the range comes from:** about $43 of the ≈ $67 spread is the unquoted board ($63–106).
Upload placeholder 280 × 100 and 280 × 25 mm outlines to the quantity-1 fabs (Pad2Pad, PCBCart, AtlasPCB, BareBones, Ponoko) to collapse it.

**[rev 8]:** velocity now sounds (switchable) and keys are all bought with minimal assembly, for ≈ +$3: **≈ $258–323**, or **≈ $242–305** with tuning cuts. Internal-LiPo runtime may drop to ≈ 3.5–5 h once the 0.5–0.8 W sensor load is counted.

**Honest bottom line (rev 6, velocity required):** the cheapest build that keeps the Model D sound is **≈ $255–320**. With tuning-stability cuts it is **≈ $239–302**. Velocity costs ≈ $25–30 over the non-velocity keys. About $200 is only reachable at the low end of the board quote with the tuning cuts taken.


## v1.11 Rev 13: Daisy Seed as the digital brain (owner decision, 2026-11-13)

Sources: `daisy-pin-and-audio-check.md` (rev 0), `single-chip-research.md` (rev 0), `round4-answers.md` §3, `battery.md`, `fold-answers.md`, `answers-E1-E10.md` E3. Conventions as above. **Pending `daisy-first-principles.md`**: key scan, autotune counting, pot scan, CVs, MIDI, FX signal path, power sequencing. Items marked "provisional" come from `daisy-pin-and-audio-check.md` and may change there.

### v1.11.1 What changes in the BOM

Rev 12 never carried the SGTL5000 shield or 74HC595 (they existed only in `single-chip-research.md`). Against rev 12 the swap is:

| Line | Δ cost | Note |
|---|---|---|
| Pico 2 removed | −$5.75 | |
| **Daisy Seed, 65 MB (Seed3 TAC5242 or Seed2 DFM PCM3060), pre-soldered headers** | +$34.99 | $34.99 from Nov 1 per [PedalPCB tracker, Oct 26](https://forum.pedalpcb.com/threads/free-stock-price-tracker-for-daisy-seeds-heads-up-prices-change-nov-1.30660/latest). Thonk lists the 65 MB at £31 ex VAT, in stock ([Thonk](https://www.thonk.co.uk/shop/electrosmith-daisy-seed)). Avoid used Rev 5 (WM8731) |
| 2 × 20 socket strips for the Seed (replace the Pico headers in the $3 line) | ≈ +$0.50 (ESTIMATE) | 0.6" row spacing |
| FX wet path: 2 TL072, level/AA/recon passives (no 595, no shield) | ≈ +$1.50 (ESTIMATE) | `single-chip-research.md` §5.3 less the shield |
| FX panel controls, **owner-approved "Full 8, grow the panel"** (`design/owner.md`): 5 pots + knobs ($4.45), 2 four-way rotaries + knobs ($3.26), TAP ($0.50) | +$8.21 | `single-chip-research.md` §5.2 |
| **DRIFT knob** (owner: controllable drift; firmware slow random pitch wander per oscillator, 0 = steady): 1 pot + knob; mux channel, no GPIO | +$0.89 | Placement is the design team's; mux use ≈ 46 of 48 |
| **Bigger 5 V boost** (battery builds only; flag below) | +$6–12 (ESTIMATE, part not identified) | The bq25185 board's boost is 1 A and 4.4 W is ≈ 0.88 A. Fix: keep the bq25185 for charging and add a ≥ 2 A 5 V boost module fed from the cells (no ≥ 2 A load-sharing Adafruit board found; the PowerBoost 1000C is also 1 A) |
| Extra board area (§v1.11.5) | ≈ +$0.50–1.00 | at $0.61–1.22/in² |
| Seed shipping (separate vendor) | +$0–6 (ESTIMATE) | |
| **Δ vs rev 12** | **≈ +$39–50 on USB power; ≈ +$45–62 with a battery (boost swap)** | vs the Pico + shield FX plan: ≈ +$16–20, matching the +$19 in `daisy-pin-and-audio-check.md` |

Optional, not counted: TRS MIDI out (jack + 2 resistors, ≈ +$0.50), free on the Seed (provisional pin D13).

### v1.11.2 Power budget and runtime (all ESTIMATE; measure in the spike)

No official Seed current figure was found (the vendor pages and datasheet text I could read give none). `single-chip-research.md` carries ≈ 0.4–0.8 W at 5 V.

| Load (at 5 V) | Rev 12 | Rev 13 |
|---|---|---|
| ±9 V voice | 1.2–1.9 W | 1.2–1.9 W (+ ≈ 0.1 W for 2 FX TL072) |
| 25 SS49E via LD1117 | 0.6–1.25 W | 0.6–1.25 W |
| Digital brain | Pico 0.1–0.15 W | **Seed 0.4–0.8 W** (codec, 400 MHz M7, SDRAM) |
| LM386, mux, DACs, MIDI, LEDs | ≈ 0.07–0.35 W | same |
| **Total** | **2.0–3.6 W** | **≈ 2.4–4.4 W** |

Runtime = 90 % of nominal Wh ÷ (load ÷ boost efficiency; 90 % at 2.4 W, 85 % at 4.4 W), same method as `battery.md`:

| Pack | Usable | 2.4 W | 4.4 W | Rev 12 (2.0 / 3.6 W) |
|---|---|---|---|---|
| **22.2 Wh** (2 × PiShop 755060, 1S2P) | 20.0 Wh | **≈ 7.5 h** | **≈ 3.9 h** | 9.0 / 4.7 h |
| 18.5 Wh (2 × Adafruit #328) | 16.6 Wh | ≈ 6.2 h | ≈ 3.2 h | 7.5 / 3.9 h |
| **Slim 11.1 Wh** (FOLD: 4 × PiShop 952540, 1S4P) | 10.0 Wh | **≈ 3.7 h** | **≈ 1.9 h** | 4.5 / 2.4 h |

About −17 % across the board. Notes:
- **Boost headroom:** 4.4 W is ≈ 0.88 A at 5 V against the board's 1 A boost rating: too thin. **Fix: a ≥ 2 A 5 V boost module, ≈ +$6–12 (ESTIMATE).** Pack current at end of discharge ≈ 1.7 A (≈ 0.43 A per 750 mAh slim cell, ≈ 0.6 C; the cell PCM rating is unknown).
- **Where the watts are:** the SS49E LDO (5 V × I) is the biggest single item. A 3.3 V buck in place of the LD1117 saves ≈ 0.2–0.4 W [ENG], recovering most of the Seed's cost in runtime. Pending first-principles.
- **Thermal:** ≈ 0.4–0.8 W in 51 × 18 mm with no heatsink. Not large, but a warm spot: keep it ≥ 30 mm from the ladder, AS3046s and tempcos, as the Pico was (`little-d-design-answers.md` "Digital noise"). Seed temperature ratings are UNVERIFIED.
- **Sequencing:** the Seed boots through the Electrosmith bootloader; boot-to-main time is unmeasured. The sensor-LDO enable must default off at reset (provisional: D23/PA4, defined low, so no 595 hazard).
- The Seed's 3V3 output rating is not stated (UNVERIFIED): keep the key strip on its own LD1117V33 and draw only the MCP4822s and mux logic from the Seed.

### v1.11.3 USB: does the single rear USB-C from E3 still work?

E3 (`answers-E1-E10.md`) is the **full instrument's** plan: a USB-C breakout on the rear edge, VBUS to the charger, **D± wired to the Pico 2 test pads TP2/TP3**. Little D's own §v1.6 plan was two ports (USB-C charger plus the Pico's micro-USB). The pad trick goes away:
1. **The Seed has no test pads for D±.** Its USB is a connector on the module (Seed3 USB-C, earlier Seeds micro-USB; physical position and height **not found, UNVERIFIED**). That port carries MIDI **and** the DFU/bootloader.
2. The header exposes USB HS D−/D+ on **D29/D30** (provisional spare pins), so a rear breakout *could* feed the Seed over the header, with VBUS to the charger only. Whether libDaisy and the bootloader run MIDI and DFU on those pins is **UNVERIFIED** (not read this session).
3. **Do not join the breakout's VBUS to the Seed.** Seed power arrives on VIN (4–17 V per vendor pages). How the module combines USB 5 V with VIN is not documented in what I read (UNVERIFIED), so back-powering is a real risk, as E3 found for the Pico.

| | How | Verdict |
|---|---|---|
| **A. One rear USB-C via D29/D30** (E3 adapted) | Breakout D± to D29/D30, VBUS to the charger only | One user-facing port, but **the spike must confirm MIDI on those pins**, and firmware update still needs the module's own port |
| **B. Seed's own connector is the data port** | Module connector faces the rear edge, or a short USB-C extension to a panel receptacle. Charger keeps its own USB-C | No unknowns and DFU-friendly, but **two rear ports** and the connector position drives the board edge |
| **C. Two ports, as §v1.6 already said** | Same as B | Baseline fallback |

**Recommendation (provisional):** plan the rear-edge geometry for **B**, keep D29/D30 free for **A**, and let the spike decide. Either way the design team must hold a **service opening for the module's connector** (or an extension cable). E3's one-port promise no longer holds automatically.

### v1.11.4 Cost totals (one unit, rev 13)

| Config | Rev 12 range | **Rev 13 range** | Midpoint |
|---|---|---|---|
| (a) cheapest that keeps the sound, USB power | $272–345 | **≈ $311–395** | ≈ $353 |
| (b) + tuning cuts, USB power | $256–327 | **≈ $295–377** | ≈ $336 |
| (a) with the 22.2 Wh pack (rev 11: $311–386) | — | **≈ $356–448** (incl. bigger boost) | ≈ $402 |
| (b) with the 22.2 Wh pack (rev 11: $295–368) | — | **≈ $340–430** (incl. bigger boost) | ≈ $385 |

The slim 11.1 Wh pack ($40.75 with the charger) changes the battery line, not this delta. The board quote remains the largest unknown.

### v1.11.5 Board area and footprint

- **Module:** 51 × 18 mm (the 51 and 18 appear among the dimensions on the datasheet drawing, but I could not read their labels, so this is **not independently confirmed**). 2 × 20 pins at 2.54 mm pitch; **15.24 mm (0.6") row spacing** per the datasheet landing pattern (read via a text summary; confirm on the drawing). The Pico 2 is 51 × 21 with 17.78 mm (0.7") rows, so **this is not a drop-in socket**.
- **Height:** the drawing lists 8.4 and 8 mm but I could not tell which dimension each is. Seated height and connector height are **UNVERIFIED**. The flat concepts allow a **≤ 8 mm underside stack** (`round4-answers.md` §1.3; a standard 8.5 mm female header already failed for the Pico), and a Seed in a header socket probably stacks higher. Measure one before freezing z. Fallbacks: low-profile machine-pin sockets, or solder directly (gives up "socketed").
- **Courtyard:** Seed 918 mm² (Pico 1,070), ≈ 1,100–1,200 with keep-out for the USB end. Net ≈ −150 mm² on its own.
- **Added by the FX decision:** 8 panel controls ≈ 1,375 mm² (5 pots × 125, 2 rotaries × 325, button ≈ 100) plus wet-path analog ≈ 600–800 mm². Rev 12's 19,500 mm² becomes **≈ 21,500–21,700 mm²**, which at 65–75 % fill is ≈ 29–33k mm² against 30,800 on 268 × 115, so the main board likely grows to **≈ 268 × 120–126** [CALC].
- **FOLD:** anything placed on the lid board costs ≈ 1 mm of depth per 262 mm² (rev 12 formula); ≈ +2,000 mm² in the lid ≈ +8 mm. Put the Seed and wet path in the base.

### v1.11.6 Pin allocation (provisional, from `daisy-pin-and-audio-check.md` §1.4; pending first-principles)

26 of 31 header GPIO used, 5 spare, no expander. The codec, SDRAM and QSPI use no header pins.

| Function | Provisional pins |
|---|---|
| VCO 1/2/3 count + filter-scale count | D25, D24, D28, D16 (TIM5 CH1–4, 32-bit) |
| PWM CVs (VCA balance, mod depth, velocity) | D4 (TIM3_CH3), D9 (CH1), D18 (CH2) |
| SPI to 2 × MCP4822 (SCK, MOSI, CS1, CS2) | D8, D10, D7, D0 |
| CD4067 selects S0–S3 (all port C) | D2, D1, D6, D3 |
| Mux outputs → ADC | D15, D20, D21 |
| TRS MIDI in / (optional) out | D14 / D13 (USART1) |
| Gate out, LEDs, LM386 enable, sensor-LDO enable | D26, D27/D5, D19, D22, D23 |
| Audio in/out (codec) | header pins 16–19, AGND pin 20 |
| **Spare** | D11, D12 (I2C1), D17 (A2), D29, D30 (USB HS; spare unless USB option A) |

Constraints that stand regardless: libDaisy owns TIM2 (use TIM5 for the counters); its default TIM3 CH2 pin is the on-board LED (name PA7 explicitly); its ADC mux helper handles 8 channels and 3 selects, so a 4-select CD4067 scan is custom code.

### v1.11.7 Pre-layout breadboard spike (replaces `single-chip-research.md` §6)

One evening; parts are reused in the build. Pass numbers are my proposals.
1. **Four TIM5 input-capture counters** on function-generator squares (10 Hz–20 kHz): error ≤ 0.1 cent at 20 kHz with audio running; no missed edges.
2. **Timer-driven CD4067 mux scan**, 48 positions at ≥ 4 kHz/key (≈ 192 ksps), DMA-stepped selects on port C; scan-period jitter ≤ 2 µs at S0, with and without audio.
3. **Plate reverb (Dattorro) + tape echo** together (then a long hall if wanted): zero underruns.
4. **Codec noise** through the synth's level stage: idle, FX input muted, and worst case (tape repeats near runaway + long tail). Pass: typical ≤ −95 dB re full scale (PCM3060-class predicts ≈ −98 / −88 worst, TAC5242 ≈ −108 / −98). Record which codec the board has.
5. **CPU load** (DWT cycle counter): < 50 % at 400 MHz with everything running.
6. **Also measure:** 5 V current at idle and full load (feeds §v1.11.2); seated height in the candidate socket; USB connector position; USB-MIDI via the module port and, if wanted, D29/D30; boot-to-main time and the LDO-enable state at reset; 3V3 current drawn.

**Gate:** pass → lock the Seed and start layout. Noise fail → try the other codec variant. Timing fail → pending first-principles redesign.

## v1.12 Rev 14: channel aftertouch (owner decision, 2026-11-13)

Detail, sources and test plan: `aftertouch.md` rev 0. Summary:

| Item | Rev 14 |
|---|---|
| Sensor | 2 × Interlink FSR UX 408 300 mm ($4.99 each, solder tabs), trimmed to ≈ 240 mm (trimming UX parts is UNVERIFIED; spike A1), one lane under each key row, wired in parallel so the reading is the total force wherever you press |
| Mechanics | Strip C floats on the lanes (acrylic pressure rib → 1.6 mm soft silicone/PORON → FSR → acrylic base strip on the back panel); 4 springs (≈ 1 N each) at the existing bosses; screws through nylon sleeves. Stack ≈ 8.06 mm in the existing ≈ 8 mm gap: **+0 mm** key height nominal. Key load now goes to the back panel and feet |
| Electronics | FSRs from the sensor-LDO rail, 10 k + 100 nF → **mux B ch 15 (ADC2)**; toggle ladder → **mux B ch 14**. 0 header pins; mux 46 → **48/48**; D16 stays spare. 8–10 kHz → 1 kHz → τ 10 ms |
| Firmware | Output only while a key is bottomed (Hall); learned dead zone above holding force; 30 ms strike blank; auto-zero with no keys held; full scale 8 N default |
| Routing | **MOD / OFF / FILT** toggle. MOD: + up to 50 % mod depth (Seed DAC1_OUT2 → AS3360 A). FILT: + up to 2 octaves on CUTOFF (MCP4822 #4 B). MIDI channel pressure out (USB + TRS) in all positions; MIDI pressure in → same path, max(local, MIDI) |
| Power | ≈ 1 mW |
| **Cost** | **≈ +$18–33** (FSRs $9.98, shipping $0–12, toggle, silicone, springs; acrylic $0 on scrap). Plus TRS MIDI out now owner-approved: **+$0.50** |

**Totals (one unit, rev 14 = rev 13 + $18.5–33.5) [CALC]:**

| Config | Rev 13 | **Rev 14** |
|---|---|---|
| (a) cheapest that keeps the sound, USB power | $311–395 | **≈ $330–429** |
| (b) + tuning cuts, USB power | $295–377 | **≈ $314–411** |
| (a) with the 22.2 Wh pack | $356–448 | **≈ $375–482** |
| (b) with the 22.2 Wh pack | $340–430 | **≈ $359–464** |

**Design-facing:** 8 toggles (new AFTERTOUCH, legend MOD or VIB is the owner's call); ≥ 1 mm key-top clearance in the key window; Ø 7 spring counterbores in the 4 strip-C bosses; the back panel is flat and structural under the keys, with 2 feet under the lane ends; FOLD's base board splits into a floating key strip and a fixed PLAY board. `aftertouch.md` §8.

**Spike:** tests A1–A8 (≈ +1 evening) join `daisy-first-principles.md` §10.

---

# PART 2: REV 0 EXPLORATION (tiers, cut list, calibration)

Kept for reasoning. Superseded by Part 1 where they conflict. §4 calibration still applies.

## 0. Bottom line

| | One-off (you build 1, pay for minimum board orders and 3 shipments) | Per unit when 5 are built (boards and shipping split 5 ways) |
|---|---|---|
| **"$100" tier** (spec §2) | **≈ $125–150** | **≈ $95–110** |
| "$150" tier | ≈ $175–195 | ≈ $140–155 |
| "$200" tier | ≈ $230–255 | ≈ $190–205 |
| Full version (architecture-v2) | $490–810 | — |

**Honest answer: $100 per unit holds when you build a small batch (or sell it as a kit). The first single unit
costs about $125–150.** The parts themselves come to about $88. What pushes a one-off past $100 is fixed cost:
- a minimum board order of 5;
- three vendor shipments;
- the 35 % JLC DDP tariff.

That fixed cost is about $40–55, and no circuit cut removes it. Cutting circuits until a one-off hits $100 means
dropping things that are the spirit, such as the second VCO or real keys (§1.3). **The real floor for a single
unit that keeps the spirit is about $120.**

---

## 1. What "the spirit" is

### 1.1 Essential: keep, even at $100
Ranked by how much of the sound and feel it carries (from `architecture.md` §1.9):

| # | Element | Why it's the spirit | Cost to keep |
|---|---|---|---|
| 1 | **Transistor ladder, 24 dB/oct, self-oscillating** | It *is* the Moog tone | Discrete matched 2N3904s at $0.02 each. Nearly free |
| 2 | **Passive mixer into the ladder's input pair (overdrive)** and the **feedback trick** | Overdrive comes from the input pair's tanh, not from an op-amp (CA-72 model, v1 §1.4) | 3 pots, resistors, one switch position. Nearly free |
| 3 | **Contour overshoot ("punch")** | Lightner: attack overshoots sustain max (v1 §1.6) | Resistor ratios, so free if we keep the contour topology |
| 4 | **≥ 2 free-running, detunable VCOs** | Beating and thickness. One VCO is a different instrument | ≈ $5 per VCO |
| 5 | **Panel-as-patch**: a pot for every main parameter, no menus | The "immediacy" | Pots $0.45 plus knobs $0.30 each, about $0.75 per control |
| 6 | **Glide, low-note priority, single trigger** | Model D playing style | Firmware, so free |
| 7 | **Keys with travel**, not pads | Owner: "feel like an instrument" | ≈ $15 (Hall + magnets + printed keys) |
| 8 | **Osc-as-modulator** (osc 3 → LO, keyboard off) | Model D's mod source, and audio-rate FM | One switch + resistor on VCO 2 |

### 1.2 Cut list with sound cost

| Cut | Saves | Sound / feel cost | Decision at $100 |
|---|---|---|---|
| 3 → 2 VCOs | ≈ $5–9 (TL072, pairs, cap, 2 pots, switch, knobs, DAC channel) | Less "wall" on bass and no 3-osc chords. VCO 2 doubles as the mod oscillator, so detuned-pair *or* osc-FM, not both at once | **Cut**. Back at $150 |
| Osc 3 as LFO-only | — | Superseded: VCO 2 has a LO/keyboard-off switch (the Model D behaviour), and the Pico adds a firmware triangle LFO as an analog CV | Firmware LFO **added** for free |
| Fixed waveforms (saw / square / narrow pulse on a 3-way toggle, not 6-way rotary) | ≈ $2 per VCO, plus panel area | Lose triangle and shark-tooth. Saw and pulse are ~90 % of Model D use [ENG] | **Cut** |
| One shared contour (instead of filter + loudness) | ≈ $4–5 | Large. No filter sweeps over a held, steady level, and plucks with long tails go. Very Model D-defining | **Keep both** (they're cheap) |
| Fewer pots (≈ 23 → 18) | ≈ $4 | Lose separate osc-2/3 freq, mod-mix crossfade, and the keyboard-control 1/2 split | **Cut to 18** |
| Pitch and mod wheels | ≈ $2 plus printed parts | Bends via MIDI only. Mod depth is a pot | **Cut**. Back at $150 |
| MIDI CC beyond notes | $0 | — | **Keep**: USB-MIDI is the Pico's own port. CC covers cutoff, glide, osc-2 detune, LFO rate/depth and octave (every Pico-read pot), with jump-on-move |
| TRS MIDI in (6N138) | ≈ $1.5 | — | **Keep** (cheap) |
| Autotune | $0 parts (firmware + 1 divider per VCO) | — | **Keep**. Without it you need trimmers plus tempcos, which breaks "no rigmarole" |
| Tempco resistors | ≈ $5–8 (3300 ppm, price UNVERIFIED) | Without them, about 12 cents/°C at 3 octaves above the calibration point [ENG]. Background re-tune absorbs it during held notes, and the first minute after a cold start may wander | **Cut**. Back at $150 |
| Built-in speaker | ≈ $2.20 (LM386 + speaker) | — | **Keep** (owner: "incredible") |
| Internal LiPo + charger | ≈ $23–32 | You need a USB power bank or cable. Some banks auto-off below ~50–100 mA. Our ~150 mA idle should hold, but that is ESTIMATE | **Cut**: power from any USB power bank. Back at $150 |
| Rails from a charge pump (ICL7660) | — | 20 mA class ([DigiKey listing](https://www.digikey.com.mx/en/products/detail/analog-devices-inc-maxim-integrated/ICL7660CPA/1303023)), too weak for ~25–35 mA rails. ±4 V would starve the ladder's headroom and the noise junction | **Rejected**. Use 2× MC34063 DIP (§2.4) |
| ±9 V from two 9 V batteries | ≈ $3 | Works and sounds right, but has 2 non-rechargeable consumables, no USB-only operation, and a battery door | **Rejected** (fallback only) |
| Capacitive PCB pads instead of keys | ≈ $12 | Stylophone feel, no travel, no velocity. Fails "feel like an instrument" | **Rejected** |
| Stylus / resistor strip | ≈ $14 | Novelty; not a keyboard | **Rejected** |
| PCB sandwich enclosure (panel PCB + bottom PCB) | — | Large PCBs (>100 × 100 mm) leave JLC's $2 tier. Three 280 × 180 mm boards would cost about $100–160 per order (ESTIMATE). Laser-cut ply/acrylic at Vector Space costs ≈ $10, and the owner can hand-paint it | **Rejected**: makerspace laser-cut panel; all circuit boards ≤ 100 × 100 mm |
| 16-bit DACs | ≈ $25 | 12-bit MCP4822 gives ≈ 1.8 cents/step over 6 octaves. Dither plus a post-filter hides the stepping on slow glides [ENG] | **Cut** to 12-bit |

### 1.3 What a "true one-off $100" would cost in spirit
Cuts that would bring a single unit to about $105–115 (still not $100, because of fixed costs):
- drop the loudness contour (gate-only VCA, −$4);
- wire solder-lug toggles instead of PCB toggles (−$3);
- remove the speaker (−$2);
- remove TRS MIDI (−$1.5).

Not recommended: the second contour and the speaker are spirit and joy for $6.

---

## 2. Spec: "$100" tier

**Size** ≈ 285 × 160 × 30 mm. Width matches the OP-1 class; depth is 1.6× the OP-1's.
**Weight** ≈ 0.6–0.8 kg (ESTIMATE). **Power** 5 V USB, ≈ 0.75–1.5 W (ESTIMATE).

### 2.1 Voice (all analog, through-hole)
| Block | Circuit | Controls |
|---|---|---|
| VCO 1 | Saw core: 2N3904 expo pair (matched and thermally glued), TL072 summer + integrator, 2N3906 reset; pulse from comparator thresholds | **WAVE** 3-way toggle: saw / square / narrow pulse. **OCTAVE** pot (Pico-read, 5 detents in firmware) |
| VCO 2 | Same circuit | **WAVE** toggle. **FREQ** pot (Pico-read: ±7 semitones plus fine; detune). **LO** toggle: keyboard off, sub-audio range, so it becomes a mod oscillator (Model D osc-3 behaviour) |
| Noise | Reverse-biased 2N3904 E-B junction off the +12 V pre-rail, TL072 gain stage, pink-ish filter | — |
| Mixer | **Passive**: pot + resistor per channel into the ladder input pair (Model D topology, v1 §1.4) | **OSC 1**, **OSC 2**, **NOISE/EXT** pots. **SOURCE 3** 3-way toggle: noise / ext in / **feedback** (output normalled back into the ext preamp) |
| Ext preamp | TL072, gain ≈ 100, into the mixer bus; overload LED | (shares the NOISE/EXT pot) |
| Filter | 4-pole **2N3904 ladder** (5 pairs, Vbe-matched from a bag of 100), film caps, TL072 differential output. Expo on a matched pair. CV sum = cutoff + keytrack + contour + mod + **FILTER CV jack** | **CUTOFF** (Pico-read, so MIDI CC). **EMPHASIS** (in circuit). **CONTOUR AMT** (in circuit). **KEYTRACK** toggle |
| Contours ×2 | Model D ADS topology (cap, switch transistors, TL072), with the **overshoot ratio kept** | Filter **A/D/S**, Loudness **A/D/S** (A and D on 1 MΩ pots). **DECAY** toggle (release = decay, as original) |
| VCA | Discrete 2N3904 differential pair (Model D style). Balance is auto-nulled at boot by a Pico PWM-CV (v1 §3.1 method) | — |
| Mod | Source toggle: **firmware LFO** (Pico PWM, triangle, as analog CV) / **VCO 2**. Destination 3-way: pitch / off / filter | **MOD AMT** (in circuit). **LFO RATE** (Pico-read) |
| Glide | Firmware, emulating the saturating S/H curve (v1 §1.8) | **GLIDE** (Pico-read) |
| Output | LM386 → speaker. Phones jack switch mutes the speaker; phones/line from the same LM386 via a series R | **VOLUME** (in circuit) |

**Controls: 18 pots** (5 Pico-read: OCTAVE, OSC 2 FREQ, CUTOFF, LFO RATE, GLIDE; 13 in-circuit) and **8 toggles**.
Plus a power switch and 3 LEDs (power, overload, "knob not in control" for the Pico-read pots; the owner was open to that light).

**Jacks (7):**
- PHONES/LINE out
- EXT audio in
- FILTER CV in
- PITCH CV out (1 V/oct, buffered MCP4822 channel)
- GATE out
- TRS MIDI in
- USB (the Pico's own micro-USB) for power + USB-MIDI. That is micro-USB, not USB-C. A USB-C THT receptacle doesn't really exist. A USB-C breakout module would add ≈ $3 (ESTIMATE) and would split power from the MIDI port, so I left it out.

### 2.2 Digital (one ready-made module)
- **Raspberry Pi Pico 2**, socketed.
- **MCP4822** (DIP-8, 12-bit dual, internal 2.048 V ref) for the VCO 1 and VCO 2 pitch CVs.
- Pico PWM, with 2-pole RC filters and TL072 buffers, for: cutoff CV, LFO CV, VCA balance. These aren't pitch-critical.
- **2× CD4067** (DIP-24) read 25 key sensors plus the 5 Pico-read pots (32 channels, 2 spare) into 2 ADC pins.
  The 3rd ADC pin watches the VCA output for the auto-null.
- GPIO budget [ENG]: SPI DAC 3, mux select 4, mux ADC 2 + 1, VCO count inputs 2, PWM 3, gate out 1, MIDI RX 1, LEDs 2, spare ≈ 4.

### 2.3 Keys
- 25 keys, 15 white at ≈ 18.7 mm pitch across 280 mm, so near full size.
- **3D-printed one-piece flexure key combs** (PETG, makerspace). No springs, felt end-stops, ≈ 6 mm travel.
- A 5 × 2 mm magnet under each key. **SS49E-class linear Hall sensors** (TO-92S, through-hole) sit on **3 identical 95 × 20 mm strips**
  (9 positions each, 8 used on two strips), and a 14-pin ribbon runs to the main board.
- Linear sensing gives **velocity** (time between two thresholds). Firmware learns each key's min/max as you play, so no per-key trimming.
- Honest feel: better than pads or tact switches and silent, but not a sprung keybed. This is the cheapest thing that passes "instrument".

### 2.4 Power
- USB 5 V (power bank, phone charger or laptop) → LC filter.
- **MC34063 boost → +12 V** and **MC34063 inverter → −12 V** (DIP-8, through-hole inductors and Schottkys).
- Then **78L09 / 79L09 → ±9 V** for the voice.
- The +12 V pre-rail also feeds the noise junction. LM386 and Pico run on the 5 V.
- Rail estimate ≈ 25–35 mA each (9× TL072 at ≈ 2.5 mA, plus ladder bias and discretes) [ENG].
- Switching ripple needs SPICE and layout care: keep the 34063s at the board edge away from the VCO cores, and post-LDO. **Risk M.**

### 2.5 Boards and enclosure
| Board | Size | Contents |
|---|---|---|
| A: VCOs + digital | ≤ 100 × 100 | 2 VCOs, Pico socket, MCP4822, muxes, MIDI, power |
| B: mixer + filter | ≤ 100 × 100 | mixer, ext preamp, noise, ladder, filter CV |
| C: contours + VCA + out | ≤ 100 × 100 | 2 contours, VCA, LM386, jacks |
| D: key strip ×3 (one design) | 95 × 20 | 9 Hall positions + header |

A, B and C sit side by side (≈ 290 mm) under a **laser-cut 3 mm ply or acrylic top panel**. Pots are soldered to the boards and poke through the panel; the owner can hand-paint or engrave the labels. There is a ply bottom, and the sides are printed or ply. All of it is made at Vector Space.

---

## 3. Bottom-up BOM ("$100" tier)

Prices as listed 2026-11-12 at quantity 1 unless noted.

### 3.1 Electronics
| Item | Qty | Unit | Ext. | Source |
|---|---|---|---|---|
| Raspberry Pi Pico 2 | 1 | $5.75 | $5.75 | [SparkFun DEV-26124, in stock](https://www.sparkfun.com/raspberry-pi-pico-2.html) |
| MCP4822-E/P 12-bit dual DAC, DIP-8 | 1 | $3.99 | $3.99 | [TME US, 144 in stock](https://www.tme.com/us/en-us/details/mcp4822-e_p/d-a-converters-integrated-circuits/microchip-technology/) (likely cheaper at LCSC; ESTIMATE) |
| TL072CP DIP-8 | 9 | $0.22 | $2.02 | [LCSC C7236, from $0.2243](https://lcsc.com/product-detail/FET-InputAmplifiers_Texas-Instruments-TL072CP_C7236.html) |
| LM386 DIP-8 | 1 | $0.23 | $0.23 | [Tayda A-206](https://www.taydaelectronics.com/ic-integrated-circuits/lm386-lm386l-audio-power-amplifier-ic.html) |
| CD4067 DIP-24 | 2 | ≈ $0.60 | $1.20 | ESTIMATE |
| 6N138 opto + 1N4148 + R (MIDI in) | 1 set | ≈ $0.60 | $0.60 | ESTIMATE |
| MC34063AN DIP-8 | 2 | $0.40 | $0.80 | [LCSC C126078, from $0.3989, out of stock when checked](https://www.lcsc.com/product-detail/C126078.html). Tayda/TME alternatives ESTIMATE |
| Inductors ×2, Schottky ×2, 78L09 + 79L09, ferrite | 1 set | — | $2.00 | ESTIMATE |
| 2N3904 (bag of 100, for matching) | 100 | $0.02 | $2.00 | [Tayda A-111](https://www.taydaelectronics.com/catalogsearch/result/?q=2n3904) |
| 2N3906 | 20 | ≈ $0.02 | $0.40 | ESTIMATE (assumed same as 2N3904) |
| SS49E-class linear Hall, TO-92S | 25 (+5 spare) | $0.10 | $3.00 | [LCSC C18189021 SS49E-JSM, $0.0996, 2,840 stock](https://www.lcsc.com/product-detail/C18189021.html). Tayda's SS49E is [$1.99, out of stock](https://taydaelectronics.com/ss49e-linear-hall-effect-sensor-ic.html) |
| 1/4 W metal-film resistors | ≈ 250 | $0.015 | $3.75 | [Tayda, $0.015/pc](https://taydaelectronics.com/resistors.html) |
| Film caps (ladder, timing, contour) | ≈ 15 | $0.10 | $1.50 | [Tayda 100 nF polyester box](https://www.taydaelectronics.com/0-1uf-100v-5-polyester-film-box-type-capacitor-jfj.html) |
| Electrolytic + ceramic caps | ≈ 70 | ≈ $0.035 | $2.50 | ESTIMATE |
| Diodes, LEDs ×3 | — | — | $0.60 | ESTIMATE |
| IC sockets (12) + Pico headers 2×20 | — | — | $2.50 | ESTIMATE |
| Ribbon + IDC 14-pin ×3 pairs | — | — | $2.00 | ESTIMATE |
| **Electronics subtotal** | | | **≈ $34.8** | |

### 3.2 Panel hardware
| Item | Qty | Unit | Ext. | Source |
|---|---|---|---|---|
| 9 mm pot, linear, knurled (10k/50k/100k) | 14 | $0.45 | $6.30 | [Tayda A-5531/5530/5690](https://www.taydaelectronics.com/catalogsearch/result/?q=b10k) |
| 9 mm pot, 1 MΩ linear (contour A/D) | 4 | $1.29 | $5.16 | [Tayda/Alpha A-1882, 1,391 stock](https://www.taydaelectronics.com/potentiometer-variable-resistors/rotary-potentiometer/linear/1m-ohm-linear-taper-potentiometer-round-shaft-pcb-9mm.html) (round shaft, so it takes the set-screw knobs below) |
| Knobs, 16 × 14 mm, 6 mm 18T split | 14 | $0.30 | $4.20 | [Tayda A-6046..6050](https://www.taydaelectronics.com/potentiometer-variable-resistors/rotary-potentiometer/knobs.html) |
| Set-screw knobs (for 1M pots) | 4 | $0.42 | $1.68 | [Tayda A-6019](https://www.taydaelectronics.com/potentiometer-variable-resistors/rotary-potentiometer/knobs.html) |
| Sub-mini toggle, PCB pins | 8 | $0.80 | $6.40 | [Tayda 2MS1T2B2M6RES](https://www.taydaelectronics.com/non-threaded-sub-mini-toggle-switch-spdt-on-none-on-short-handle-gold-pcb-pins.html) (on-on; the 3-way ones are on-off-on or on-on-on, similar price, ESTIMATE). Solder-lug alternative [$0.44](https://www.taydaelectronics.com/mini-toggle-switch-spdt-on-off-on-mts-103-c1.html) |
| 3.5 mm jacks | 7 | ≈ $0.12 | $0.84 | [Tayda PJ-302 $0.12](https://www.taydaelectronics.com/pj-302-3-5-mm-mono-phone-jack-3691.html), [PJ-320A THT $0.07](https://www.taydaelectronics.com/pj-320a-3-5-mm-audio-socket-through-hole-pcb-silver-plated.html) |
| Power slide switch | 1 | — | $0.30 | ESTIMATE |
| Speaker, 3" 8 Ω 1 W | 1 | $1.95 | $1.95 | [Adafruit #1313](https://www.adafruit.com/categories/271) (thin 1.5" #1891 $1.75 if depth is tight) |
| **Panel subtotal** | | | **≈ $26.8** | |

### 3.3 Keys and mechanics
| Item | Ext. | Source |
|---|---|---|
| 25× 5 × 2 mm N35 magnets | $8.00 | [Magnet Baron $15.99/50](https://themagnetbaron.com/products/10-3-16-x-1-16-disc-super-strong-rare-earth-magnets-neodymium-n35-nicuni) (sold out when checked; bulk Amazon packs likely cheaper, ESTIMATE) |
| PETG for key combs + case sides (≈ 150 g) | $3.00 | ESTIMATE |
| Felt, rubber feet, M3 standoffs/screws | $5.00 | ESTIMATE |
| Laser-cut 3 mm ply/acrylic top + bottom (makerspace) | $10.00 | ESTIMATE |
| **Mechanics subtotal** | **≈ $26** | |

**Parts total ≈ $87.6.**

### 3.4 Boards (JLCPCB)
- JLC 2-layer ≤ 100 × 100 mm is **$2 per 5 pcs** ([Hack Club JLC guide](https://highway.hackclub.com/guides/JLC-cost-optimizing)).
  Boards over 100 mm in any dimension "may get you out of the standard … pricing" ([r/synthdiy](https://pol1.lr.ggtyler.dev/r/synthdiy/comments/1hue1ge/jlcpcb_size_thresholds_for_pricing)).
- JLC's US DDP tariff is **35 % minimum** (Section 301 25 % + Section 122 10 %; total range 35–92.5 %)
  ([JLC tariff FAQ](https://jlcpcb.com/help/article/us-tariff-policy-faq)).
- I'm assuming the $2 tier applies to each of 4 designs; confirm with placeholder Gerbers.

| Item | One-off order | Per unit if 5 built |
|---|---|---|
| A, B, C ×5 each, $2 per design | $6.00 | (5 sets, so $1.20) |
| Key strip D: need 3 per unit, so order 5 (1 unit) or 15 (5 units) | $2.00 | ≈ $1.00 (15 pcs ≈ $5, ESTIMATE) |
| Shipping: economy line ≈ $8–12 (ESTIMATE); DHL ≈ $18 ([pamfinds](https://pamfinds.pages.dev/guides/pcb-tariffs-us-makers-2026/)) | $10–18 | $2–4 |
| LCSC parts merged into the same shipment (TL072, Hall, MC34063), extra weight | ≈ $3 | ≈ $1 |
| 35 % DDP on boards + LCSC goods (≈ $16 of goods) | ≈ $6 | ≈ $1.5 |
| **Boards total** | **≈ $27–35** | **≈ $6–9** |

### 3.5 Shipping split (other vendors)
| Vendor | Goods | Shipping | Source |
|---|---|---|---|
| Tayda (Thailand) | ≈ $45 | $6–10 (users report $6 UPS Express on ~$100, often $0.99 promos on large orders) | [PedalPCB forum, Dec 2024](https://forum.pedalpcb.com/goto/post?id=311248); 2026 rates ESTIMATE |
| Import duty on the Tayda order | — | ≈ $4–5 (≈ 10 %, ESTIMATE; de minimis status and rate UNVERIFIED) | — |
| SparkFun or Adafruit (Pico, speaker) | ≈ $8 | ≈ $6–10 | ESTIMATE |
| TME (MCP4822), or move it to LCSC | $4 | $0–10 | Move it to LCSC to save the shipment |
| Magnets (Amazon) | — | $0 | ESTIMATE |
| **Shipping + duty** | | **≈ $16–30** one-off; ≈ $4–6/unit across 5 | |

### 3.6 Total
| | One-off | Per unit, 5 built |
|---|---|---|
| Parts | $88 | $85 (small bulk breaks) |
| Boards | $27–35 | $6–9 |
| Shipping + duty | $16–30 | $4–6 |
| **Total** | **≈ $131–153** (call it **$125–150**) | **≈ $95–100** (call it **$95–110** with contingency) |

Contingency: plan +10 % for wrong parts and a second Tayda order (common on a first build).

---

## 4. Calibration: "no rigmarole" still holds
- **No trimmers anywhere.**
- **VCOs**: each VCO's square goes through a 100 k + 1N4148 clamp into a Pico GPIO, and a PIO reciprocal counter measures it (v1 §3.1).
  At power-on (≈ 2–3 s) the firmware steps the MCP4822 across the range and builds a per-VCO octave table. That absorbs:
  - unmatched expo pairs;
  - missing tempcos;
  - op-amp offsets;
  - DAC INL.

  Background re-tune trims offset during held notes, without locking the VCOs together.
  Without tempcos, expect some wander in the first minute after a cold start, plus re-tunes on big temperature swings [ENG].
- **VCA thump**: auto-nulled at boot by the PWM balance CV, watching the VCA output on the 3rd ADC.
- **Hall keys**: self-learning min/max per key.
- **Transistor matching**: the Pico doubles as a Vbe matching jig. Firmware mode plus a socket on board A: insert each 2N3904, and it reports bins. That is a one-time build step, not ongoing calibration.
- **Filter tracking**: one optional gesture (EMPHASIS full, hold a button). The ladder output is already wired to a count input via the same divider trick.
  Without it, keytrack is about right (fixed resistor, ±10 % [ENG]). This is the one place the $100 tier falls a little short of zero-rigmarole. It matches open question Q4 in v2.

---

## 5. Tiers: what each buys back

| Tier | Adds (vs. the tier below) | Delta | Source / note |
|---|---|---|---|
| **$150** | **Internal LiPo**: 2000 mAh ([Adafruit #2011, $12.50](https://adafruit.com/products/2011)) + USB-C charger ([Adafruit #4410, $5.95](https://www.adafruit.com/products/4410); load-sharing not stated, so diode power-path ESTIMATE) + 5 V boost (≈ $5, UNVERIFIED); or PowerBoost 1000C, load-sharing, $19.95 (v2 §1) | +$23–32 | Runtime at ≈ 1 W: ≈ 6 h [ENG] |
| | **VCO 3** (true 3-osc Model D stack; VCO 2/3 detune and osc-3-as-LFO at the same time) + 2nd MCP4822 (VCO 3 + clean filter CV) | +$10 | — |
| | **Tempcos ×3** (stable from cold) | +$5–8 | price UNVERIFIED ([MFOS](https://musicfromouterspace.com/analogsynth_new/ELECTRONIC_PARTS/MFTEMPCO3300.php)) |
| | **Pitch + mod wheels** (printed wheels on 9 mm pots) | +$2–3 | ESTIMATE |
| | Extra shipping (Adafruit order) | +$0–8 | — |
| **$200** | Full waveform sets (tri / shark / saw / 3 pulses) on rotary switches; noise/osc-3 **mod mix** crossfade as original | +$8–12 | ESTIMATE |
| | AS3046 expo arrays (as the full version) instead of hand-matched pairs | +$9–15 | price UNVERIFIED (v2 §3) |
| | MCP4728 quad DAC ([Adafruit #4470, $7.50](https://www.adafruit.com/product/4470), v2 §1): MIDI-controllable sustain ×2 + loudness CV | +$7.50 | — |
| | PAM8302 class-D ([$3.95](https://adafruit.com/products/2130), v2 §1) + enclosed speaker ([Adafruit #3351 $3.95](https://www.adafruit.com/categories/271)): louder | +$8 | — |
| | More patch points (loudness CV in, osc mod in), A-440, a nicer panel (walnut or fiber-laser-marked aluminium at Vector Space) | +$10–20 | ESTIMATE |

Beyond $200 you are rebuilding the full version. Its extra $300–600 goes to:
- 16-bit DACs;
- proper ±10 V isolated rails;
- full Model D control set (≈ 40 controls);
- full eurorack I/O;
- a larger battery;
- a refined enclosure.

---

## 6. Risks specific to the budget variant
| Risk | L | Mitigation |
|---|---|---|
| MC34063 switching noise (≈ 30–100 kHz) leaks into the VCOs/ladder | M | LC filter + 78L/79L post-regulation, edge placement, ground pour; footprint for a fallback isolated DC-DC (Mean Well DCWN03E-12, $10.93, v2 §1) |
| Power bank auto-off at low current | M | ~150 mA draw is likely enough (ESTIMATE); otherwise a firmware "keep-alive" load pulse, or the $150 LiPo tier |
| JLC $2 tier may not apply to every design in one order | L–M | Quote placeholder Gerbers before layout. Worst case +$5–10 |
| 12-bit pitch stepping on slow glides | L | Dither + post-DAC RC; upgrade path is 2× MCP4822 coarse/fine |
| Printed flexure keys feel cheap or fatigue | M | Print test combs early (PETG vs. TPU hinge); keys are a separate strip, so you can swap the mechanism without touching electronics |
| Hall sensor and magnet tolerance | L | Self-learning per-key range; 5 spare sensors |
| Ladder at ±9 V vs. original ±10 V | L | Re-run the CA-72 ladder model at ±9 V before layout (sim/) |
| Tariff and duty figures change | M | JLC charges DDP at checkout, so the number is known before paying |
