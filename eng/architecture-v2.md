# Architecture v2: modules + through-hole only, small (OP-1 class)

Status: rev 0, 2026-11-12. **This supersedes the build-variant, power, DAC and §5e-tier parts of
`architecture.md`.** Unchanged and still in force from v1:
- the original-circuit research (§1);
- the autotune concept (§3);
- the risk and verification method (§6–§7);
- the patch I/O list (§5b);
- the jump-on-move behaviour (§5e.5).

**Rev 1 (2026-11-12): changes from `answers-E1-E10.md` are marked [CHANGED E#].**

Conventions as in v1: link = sourced; **UNVERIFIED** = not confirmed this session; **[ENG]** = my estimate.

**New owner constraints (owner-requirements.md, 2026-11-12):**
- no custom PCBA and no factory minimums: every custom board is a bare board the owner solders, through-hole only;
- all SMD arrives as ready-made modules from US vendors, plugged into sockets;
- **one build variant**;
- **small**, OP-1 class. The OP-1 field is **288 × 102 × 29 mm, 589 g** ([teenage.engineering](https://teenage.engineering/store/op-1-field)).

---

## 1. Off-the-shelf modules

| Function | Module | Price / stock (checked 2026-11-12) | Notes |
|---|---|---|---|
| Main MCU | **Raspberry Pi Pico 2** (RP2350, 150 MHz, 3 PIO, 12-bit ADC with 3 user pins) | **$5 RRP** ([datasheet](https://pip-assets.raspberrypi.com/categories/1005-raspberry-pi-pico-2/documents/RP-008299-DS-3-pico-2-datasheet.pdf)); US stock at Adafruit/PiShop UNVERIFIED | On 2× 20-pin female headers. **[CHANGED E3]** USB-MIDI and firmware updates come through the **rear USB-C breakout wired to the Pico's TP1/TP2/TP3 USB pads**; the Pico's micro-USB is unused and its VBUS pin is left unconnected. TUNE-at-power-on enters the ROM bootloader; TP6 (BOOTSEL) goes to a pinhole recovery switch |
| Key-scan MCU | 2nd **Pico 2** | $5 | Reads the Hall keys through muxes and sends notes over UART. Keeps scan noise off the main MCU and voice [ENG]. **[CHANGED E4]** Firmware: the main Pico reflashes it over SWD (3-wire lead to its debug header); slave MCUs across a joint use a UART A/B-slot update |
| Charger (USB-C, play while charging) | **Adafruit bq24074 Universal USB/DC/Solar charger (#4755)** | **$14.95, in stock**; USB-C input; 1 A default charge (jumper 0.5/1.5 A); input used first when present; LOAD up to 1.5 A, ≤ 4.4 V ([Adafruit](https://www.adafruit.com/products/4755)) | Charges the pack (BAT); LOAD unused (§5b). **[CHANGED E3]** Fed on its DC/VBUS input from the rear USB-C breakout; its own USB-C is unused. Optional: LM393 CC-sense → EN1/EN2 (or CE) for 500 mA ports |
| **[NEW E3] Rear USB-C port** | **Adafruit USB-C breakout, downstream (#4090)**: VBUS, GND, D+, D−, 5.1 k Rd on CC, 20.4 × 14.2 mm | **$3.45** ([PiShop](https://www.pishop.us/product/adafruit-usb-type-c-breakout-board-downstream-connection/)) | On board A's rear edge. The single port for charging + USB-MIDI + firmware. No ESD protection stated |
| Battery → 5 V (digital only) | **Adafruit MiniBoost 5V @ 1A (TPS61023, #4654)** | price UNVERIFIED (≈ $5) ([listing](https://thepihut.com/products/adafruit-miniboost-5v-1a-tps61023)) | **Revised (§5b): digital + LEDs + keys only**, worst case ≈ 0.31 A (69 % margin). It no longer feeds the analog rails or the speaker |
| ±12 V rails | **Revised (§5b): Pololu U3V40F12 boost (battery → 12 V; $9.95; 3.5 A typ max input) ([Pololu](https://www.pololu.com/product/4016/specs)) → Mean Well DCWN06A-12** (9–18 V in, ±12 V at **±250 mA**, 6 W, 83 % eff., DIP-24, 3 kV isolation) ([Mean Well AU](https://www.meanwellaustralia.com.au/products/dcwn06); [TRC listing](https://trcelectronics.com/products/mean-well-dcwn06a-12)) → LC → LM317/LM337 → ±10 V | DCWN06A price UNVERIFIED (≈ $15–20). The 6 W DCWN06 family has no 4.5–9 V-input model on Mean Well's list, so the 12 V boost hop is needed. The earlier DCWN03E-12 (±125 mA) is **dropped** for inadequate margin |
| VCO pitch DAC (×3) | **Adafruit AD5693R 16-bit I²C DAC (#5811)**: 2.5 V internal reference, 2 ppm/°C typ, 2.5 or 5 V span, 2 addresses per bus | **$10.95, 7 in stock** ([Adafruit](https://www.adafruit.com/product/5811)) | 3 boards: 2 on I²C0 and 1 on I²C1. One per VCO, so no coarse/fine tricks. Low stock: buy early (§6) |
| Other CVs (8 ch) | **Adafruit MCP4728 quad 12-bit DAC (#4470)**: internal 2.048 V reference ×1/×2, EEPROM-programmable address, DNL ±0.2 LSB typ | **$7.50, in stock** ([Adafruit](https://www.adafruit.com/product/4470)) | ×2 boards for cutoff/filter tracking, sustain ×2, CV out, VCA balance ×2, velocity or pressure out, **[CHANGED E1] ch 8 = mod depth**. All 8 used; velocity *and* pressure out would need a 3rd board |
| **[NEW E1] Mod-depth VCA** | **Alfa AS3360** dual VCA, DIP-14, ±3–12 V, linear CV ≈ 1.7 V full gain, 5 MHz, CV feedthrough ≤ 10 mV/10 Vpp untrimmed ([Tubes and More](https://www.tubesandmore.com/products/integrated-circuit-as3360-dual-vca-alfa-14-pin-dip)) + TL072 I-V | ≈ $4–6 (UNVERIFIED) | Replaces the mod wheel pot in the mod path (after R57). **[CHANGED E1 rev 1] No trimmer:** feedthrough is auto-nulled at every autotune. H11F1 photo-FET (DIP-6) mutes the VCA input; the 2nd TL072 half (×10) reads the VCA output on a 4067 channel; a PWM + 2-pole RC injects the correction into the I-V node (answers E1). Chosen over LM13700 because TI's DIP LM13700 is discontinued ([synthDIY](https://wiki.synthdiy.com/parts/otas)). 2nd half spare |
| Pitch CV input (optional, J15) | Adafruit ADS1115 16-bit ADC breakout | ≈ $15 (UNVERIFIED) | 860 SPS: ~1–2 ms latency, fine for sequencing. Not for audio-rate FM (the analog OSC/MOD input covers that) |
| Speaker amp | **Adafruit PAM8302 mono class-D (#2130)**: 2.0–5.5 V, 2.5 W into 4 Ω, 15 × 24 mm | **$3.95, in stock** ([Adafruit](https://adafruit.com/products/2130)) | **Revised (§5b): powered directly from the battery** (3.0–4.2 V is inside its 2.0–5.5 V range), so it loads no converter. Shutdown pin driven by the MCU from the phones-jack switch (auto-mute). **[CHANGED E2/E8] Mounted at the speaker (≤ 50 mm twisted leads), not on board D**; line feed from B |
| **[NEW E2] Speaker** | 40 mm Nd driver, e.g. CUI CMS-4021-34SP-X5 (4 Ω, 3 W, 21 mm deep) ([Digi-Key](https://www.digikey.com/en/products/detail/same-sky-formerly-cui-devices/CMS-4021-34SP-X5/18742615)); thin option PUI AS04008MR-2-LWC80 (40 × 5 mm, 8 Ω) ([RS](https://uk.rs-online.com/web/p/miniature-speakers/0807262)) | in §5 battery+speaker line | Magnet ≥ 60 mm from key sensors, ≥ 50 mm from the lid Hall switch, ≥ 30 mm from VCO cores |
| **[NEW E5] Lid sleep sensor** | **TI DRV5023** unipolar Hall switch, TO-92, open drain ([Digi-Key](https://www.digikey.co.uk/en/products/detail/texas-instruments/DRV5023AJQLPG/5031904)) | ≈ $1–2 (UNVERIFIED) | Power-gated by a GPIO in sleep (≈ µA average) |
| Headphone amp | none needed: **NJM4556AD** DIP-8 through-hole ([Digi-Key listing](https://www.digikey.com.br/en/products/detail/nisshinbo-micro-devices-inc/NJM4556AD/673767); specs in v1) | ≈ $1–2 (UNVERIFIED) | |
| MIDI DIN/TRS | none needed: 6N138/H11L1 DIP opto + 3.5 mm TRS jacks | ≈ $3 (UNVERIFIED) | |
| USB-MIDI | Pico 2's own USB | $0 | Ground-loop risk with a laptop (v1 R29). Mitigation is a USB isolator *module*: buy one if hum appears |
| Key sensing | Linear Hall sensors in **TO-92 (through-hole)**, e.g. DRV5053/SS49E class; 2× CD74HC4067 DIP 16:1 muxes **on a separate thin key strip** (§4.1 board C) | ≈ $0.8–1.5 per sensor (UNVERIFIED) | 25 keys (owner minimum: 2 octaves). Power-gate sensors in groups (v1 §5d); 25 sensors × 3–6 mA ≈ 0.25–0.75 W ungated |

**Is a 12-bit MCP4728 good enough for VCO pitch with per-octave calibration? [ENG]**
- Over an ≈ 8-octave span, 4096 codes is 512 codes per octave, so **2.3 cents per step**: ±1.2 cents worst-case
  quantisation on held notes.
- Calibration tables fix INL. DNL is ±0.2 LSB typ ([Adafruit](https://www.adafruit.com/product/4470)), which is
  fine, but tables can't add resolution.
- Glide, bend and the background re-tune would move in 2.3-cent steps. That is audible as faint stepping on slow
  glides.
- **Verdict: acceptable only with coarse+fine channel summing** (two 12-bit channels per VCO, the fine one at
  1/64 weight, both calibrated). Even then it takes 6 channels and needs per-unit fine-scale calibration.
- **Recommended: 3× AD5693R 16-bit** (0.15 cent per step on a 5 V/≈ 8-oct span) for +$25 against the 12-bit
  route.
- I²C bandwidth: ≈ 100 µs per 400 kHz write, so 3 VCOs at 1–2 kHz glide updates fit across the two buses. Fast
  Mode Plus support on the breakout is UNVERIFIED.

## 2. What MIDI parameter control survives (through-hole parts only)

| Parameter | MIDI-controllable? | How (all through-hole or modules) |
|---|---|---|
| Notes, bend, glide time/on, TUNE, OSC 2/3 FREQ, RANGE ×3, OSC 3 CONTROL, DECAY sw, KBD CTRL 1/2, A-440 | **Yes** | Firmware into the DACs (v1 §3). **[CHANGED E1] Knobs read through 2× CD74HC4067** (the analog inputs already totalled 17 with the RANGE ladders and rail monitors, 18 with the mod wheel; switch-type controls go to GPIO) |
| **[CHANGED E1] Mod wheel (mod depth)** | **Yes** | Wheel pot read by the MCU; MCP4728 ch 8 → AS3360 VCA in the mod path. CC1 in and out; jump-on-move applies |
| **Cutoff** (+ filter keyboard tracking) | **Yes** | MCP4728 channel into the original R55 summing node, 12-bit plus slew (v1 §5e.4: ≈ 6 cents per step, inaudible for a filter) |
| **Envelope ATTACK/DECAY ×2** | **Yes** | v1 §5e.8 option (c)(ii): PWM gated into the original attack/decay switch transistors through a **74HC08 (DIP)** plus **2N7000 (TO-92)** range MOSFETs. The original contour circuit stays intact. All through-hole |
| **Sustain ×2** | **Yes** | MCP4728 channels into the original sustain dividers |
| VCA balance (auto-null) | n/a (zero-cal) | MCP4728 channels |
| **Emphasis** | **Knob only** | No through-hole ±10 V digipot exists. Chopping a resistor inside the audio feedback loop is rejected (sidebands, charge spikes) [ENG] |
| Mixer levels ×5, Mod Mix, Contour Amount (**[CHANGED E1]** mod wheel moved to "Yes") | **Knob only** (pots in circuit, as the original) | Could be done with LM13700 DIP OTAs (DIP sold by resellers: [listing](https://www.tubesandmore.com/node/45564/ask)), but that replaces the passive mixer → ladder overdrive and costs area. Rejected for size and character |
| Waveform ×3, noise colour, osc/filter mod, feedback | **Knob/switch only** (recommended) | Feasible with **ADG413BNZ (16-PDIP)** ([Digi-Key listing](https://www.digikey.ie/en/products/detail/analog-devices-inc/ADG413BNZ/997732); stock UNVERIFIED) or DG4xx muxes, but adds ~4 ICs and area |
| Main/phones/ext volume | Knob only | as v1 |

So MIDI controls the **"playing" parameters: pitch, glide, cutoff, both envelopes and (**[CHANGED E1]**) mod depth**. Tone-setting controls
(mixer, emphasis, waveforms, mod) are knobs in the circuit, as on the original. Jump-on-move (v1 §5e.5) applies to
everything in the "Yes" rows. CC map as v1 §5e.6, restricted to those rows.

## 3. Analog voice: through-hole availability check
| Part | Through-hole? | Source |
|---|---|---|
| AS3046 (VCO expo ×3, ladder ×2, VCA pairs ×1) | **Yes, DIP-14** | [listing](https://www.tubesandmore.com/node/45569/ask); pin-compatible CA3046 clone ([Electric Druid](https://electricdruid.net/?p=440)). Price UNVERIFIED |
| THAT300/340 (optional filter expo) | **Yes, DIP-14** | [THAT datasheet](https://web.ece.ucsb.edu/Faculty/rodwell/Classes/ECE137B/datasheets/THAT300data.pdf) |
| LSK489 dual JFET (VCO ramp buffer ×3) | **Yes, TO-71** | [Linear Systems](https://www.linearsystems.com/jfet-amplifiers-duals/lsk489-series). Price UNVERIFIED |
| Tempco 3300 ppm (×3) | **Yes**, 2 kΩ 1/4 W | [MFOS](https://musicfromouterspace.com/analogsynth_new/ELECTRONIC_PARTS/MFTEMPCO3300.php) (rescale the divider: v1 §2.3) |
| NJM4556A | **Yes, DIP-8** | [Digi-Key listing](https://www.digikey.com.br/en/products/detail/nisshinbo-micro-devices-inc/NJM4556AD/673767) |
| Op-amps (OPA2277PA / TL072CP class), LM393N, 74HC08, CD74HC4067E, 6N138, LM317/LM337, LM4040 (TO-92), 2N3904/3906, BC550C/560C, 2N7000, film/electrolytic caps | Through-hole versions are standard catalogue parts | Specific stock UNVERIFIED; confirm at BOM time against Mouser/Digi-Key/Tayda |
| PhotoMOS for filter calibration (DIP-4) | likely yes (UNVERIFIED part) | Or drop it: firmware asks "turn EMPHASIS fully up and press TUNE". That breaks zero-rigmarole slightly; owner choice |

**Conclusion: the whole voice is buildable through-hole.** There is no SMD left in the analog path.

## 4. Board partitioning for an OP-1-class box

**Reality check [ENG].** OP-1 depth is 102 mm ([TE](https://teenage.engineering/store/op-1-field)). About 40
controls plus a playable key row can't fit 102 mm of depth: controls at an 18 mm grid need ≈ 3 rows × 15 columns
≈ 270 × 60–70 mm, and keys need ≈ 70–90 mm more. **Realistic footprint: 280–290 × 170–190 mm**, about OP-1 width
and roughly 1.8× its depth.

### 4.1 Boards (all 2-layer, bare, owner-soldered)
| # | Board | Size (mm) | Contents |
|---|---|---|---|
| A | Panel/control board | 2 pieces ≈ 140 × 95 (fits 2 JLC/PCBWay panels; > 100 × 100 mm costs a bit more) | All pots, rotary and toggle switches, LEDs, **jacks along the back edge** (≈ 16 × 14 mm pitch = 225 mm). Small circuits that belong next to their controls (mixer resistors, contour time and peak parts) sit between the pots |
| B | Voice board | 2 pieces ≈ 140 × 95, stacked under A on 2.54 mm headers (≈ 11 mm stack) | VCOs, ladder, VCAs, contours, preamp, noise filters, mod mix, ±10 V LDOs |
| C | **Key sensor strip(s), separate and priced separately** (owner: keys must not drive main PCB size). **[CHANGED E10]** footprints at all 25 key x-positions, centres ≥ 6.5 mm apart, 100 k pull-down per mux channel; a second offset row (strip ≈ 22 mm wide) only if a layout's positions collide | 2 strips ≈ 140 × 15 mm (or 1 × 280 × 15) | Per strip: 12–13 TO-92 Hall sensors at key pitch (2 octaves = 15 white keys over ~280 mm ≈ 18.7 mm per white key, near full size), 1× CD74HC4067, group power-gate transistor, 8-pin JST/IDC cable to board D (power, gate, 4 select lines, analog out). The key mechanism (design team) mounts to the shell, and the strip just sits under the magnets. Fits any mechanism with magnets over a straight line of sensors |
| D | Digital/power board | ≈ 100 × 70 | Sockets for 2× Pico 2, 3× AD5693R, 2× MCP4728, bq24074, MiniBoost, **[CHANGED, fixes stale text] U3V40F12 + DCWN06A-12** (+ LC pre-filter, soft-start), (ADS1115). **[CHANGED E2] PAM8302 moved to the speaker.** **[CHANGED E3]** twisted-pair USB lead from the rear USB-C breakout to the main Pico's test pads; VBUS pair to the charger. In DOCK (E6) D becomes ≈ 300 × 30 or 270 × 40, converters at the end away from the VCOs. Sits under the key area, **away from the voice**, linked to B by one ribbon (±10 V, DAC CVs, gates, PWM, mux) and to C by the key cable |

**Area estimate [ENG].** Voice parts ≈ 400 R, 150 C, 90 TO-92, ~20 DIP. Packed at ≈ 0.25/0.3/0.25/2.5 cm² each
with ×2 routing overhead, that is ≈ 370 cm². Under-panel area is 2 × (2 × 140 × 95) ≈ 530 cm². Of that, the
A boards lose ~60 % to controls, so the usable total is ≈ 320 (B) + 100 (A) ≈ 420 cm²: **tight but feasible**.
Modules on D take ≈ 60 cm² plus sockets (board D ≈ 70 cm²).

- **Total bare board area ≈ 620 cm² for A + B + D (≈ 96 in²), plus ≈ 42 cm² (6.5 in²) of key strip.** OSH Park at $5/in² per 3 boards (figure from the
  coordinator, UNVERIFIED) would be **≈ $480** for the main boards and **≈ $33** for the key strips. JLC/PCBWay 2-layer, 5 pcs, plus the 35 % tariff:
  **≈ $60–130** (UNVERIFIED).
- **Recommendation: JLC/PCBWay bare boards**; OSH Park only for small boards.

### 4.2 Height budget [ENG]
| Layer | Control section (mm) | Key section (mm) |
|---|---|---|
| Top shell / panel | 2–3 | 2 (keys pivot in the shell) |
| Knobs/keys above panel | (knobs stand proud, not counted) | key travel 6–8 |
| Pot/switch bodies (9 mm pots) + panel board A | 7 + 1.6 | key strip C 1.6 |
| Header stack to voice board B (tallest caps ≤ 10 mm) | 11 | Board D with socketed modules (beside or under the strip): 12–14 |
| Board B + solder clearance | 1.6 + 2 | Battery: **flat LiPo pouch 7–9 mm** (UNVERIFIED sizes) or 18650 at 18.6 mm |
| Bottom shell | 2–3 | 2–3 |
| **Total** | **≈ 28–32** | **≈ 31–36 (pouch) / ≈ 42+ (18650)** |

So **≈ 32–36 mm thick with pouch cells** against the OP-1's 29 mm. 18650s would push it past 40 mm. Recommend
pouch LiPo, 2P ≥ 2500 mAh each, rated ≥ 1C. That gives ≈ 4 h at the revised ≈ 4.3 W typical (§5b); 2× 5000 mAh pouches give ≈ 8 h.

Power through this chain [ENG]:
- analog 2.1 W ÷ 0.83 (LDO) ÷ ~0.78 (DCWN03, efficiency UNVERIFIED) ÷ 0.9 (boost) ≈ 3.6 W;
- plus digital and the key sensors (power-gated) ≈ 0.3–0.5 W;
- total ≈ 4 W typical. **Superseded by §5b:** the converter chain was revised so every rail has ≥ 40 % margin at worst case.

## 5. Revised one-unit cost (USD) [ENG; cited where marked]
| Item | Estimate |
|---|---|
| Modules/converters: 2× Pico 2 $10 (cited) + bq24074 $14.95 (cited) + MiniBoost ~$5 + **U3V40F12 $9.95 (cited) + DCWN06A-12 ~$15–20** + 3× AD5693R $32.85 (cited) + 2× MCP4728 $15 (cited) + PAM8302 $3.95 (cited) + ADS1115 ~$15 (opt.) | **≈ $107–127** |
| Power protection/filtering (§5b): soft-start P-MOSFET + driver, polyfuse, 6 A switch, 2× 47 µH chokes, Schottkys, bulk caps | ≈ $8–12 |
| Voice through-hole parts: AS3046 ×6, LSK489 ×3, tempcos, ~10 DIP ICs, ~90 transistors, ~400 R, ~150 C (film where required), regulators, sockets/headers | ≈ $100–150 |
| Panel hardware: ~21 pots, 6 rotary switches, ~16 toggles, ~16 jacks, ~27 knobs, wheels or alternatives, LEDs | ≈ $100–150 |
| **Keys (priced separately):** strip PCBs ~$5–15 bare + 25 Hall sensors ~$20–38 + 2× 4067 ~$2 + cable ~$3 + magnets ~$3. Mechanism (keys, springs, pivots) from the design team, makerspace-printed, ~$10–30 | ≈ $45–90 |
| Battery (2 pouch cells) + speaker | ≈ $25–40 |
| Bare PCBs A + B + D (JLC/PCBWay, incl. shipping and tariff) | ≈ $55–120 |
| Enclosure materials (makerspace laser/CNC/print; walnut or ply + acrylic/aluminium panel) | ≈ $30–80 |
| Shipping from 4–5 vendors, wire, hardware | ≈ $40–70 |
| **[CHANGED E1/E3/E5]** AS3360 VCA + TL072 + H11F1 auto-null + 2nd 4067 (E1) $8–13; USB-C breakout + recovery switch + optional CC-sense (E3) $4–6; DRV5023 + gate (E5) $1–2 | ≈ $13–21 |
| **Total, first unit** (keys ≈ $45–90 of this) | **≈ $530–860** (was $515–840) |

Down from $1,150–3,530, mainly because there is no PCBA, no factory minimums and only one variant.
Biggest levers [ENG]:
- panel hardware: cheaper pots and switches, about −$40;
- 16-bit DACs: the 12-bit coarse/fine route saves about $25 but adds risk;
- board area: JLC rather than OSH Park.

## 5b. Power v2.1: ≥ 40 % margin on every rail and converter at worst case

**Worst case used everywhere:**
- all LEDs on, speaker at full output, Hall sensors un-gated (gating fault), cold start, low battery (3.0 V);
- the analog current estimate (v1 §4.1, from SPICE of the original circuit) carries +30 % model uncertainty plus
  +10 % for cold, so **±150 mA worst** against ±105 mA nominal [ENG].

### 5b.1 Topology (modules and through-hole only)
```
2P LiPo pouch (protected cells) ── polyfuse 5 A hold ── power switch (≥ 6 A) ── soft-start P-MOSFET ──┬── U3V40F12 (12 V) ── [100 µF] ── DCWN06A-12 ── LC ── LM317 → +10 V
   ▲                                                                                                │                                         └── LC ── LM337 → −10 V
   └── bq24074 BAT (USB-C charger; its LOAD output unused)                                         ├── MiniBoost 5 V ── Pico×2, DACs, ADC, muxes, Hall keys, LEDs, MIDI
                                                                                                    └── PAM8302 (direct from battery, own 470 µF bulk and ground return)
```

### 5b.2 Margin table (worst case)
| Element | Rating | Worst-case load | Utilisation | Margin |
|---|---|---|---|---|
| ±12 V converter DCWN06A-12 | ±250 mA ([Mean Well AU](https://www.meanwellaustralia.com.au/products/dcwn06)) | ±150 mA | 60 % | **40 %** ✓ |
| LM317 / LM337 (TO-220) | 1.5 A class (UNVERIFIED per vendor) | 150 mA; dissipation (12 − 10) V × 0.15 A = 0.3 W each, no heatsink | 10 % | 90 % ✓ |
| DCWN06A input (at 83 %) | from U3V40F12 | 2 × 12 V × 0.15 A / 0.83 = 4.3 W → 0.36 A at 12 V | — | — |
| 12 V boost U3V40F12 | 3.5 A typ max input ([Pololu](https://www.pololu.com/product/4016/specs)) | 4.3 W / 0.88 (efficiency UNVERIFIED) / 3.0 V = **1.64 A in** | 47 % | **53 %** ✓ (check the output-current graph before layout: UNVERIFIED) |
| 5 V MiniBoost (digital) | 1 A out | Pico ×2 50 mA + DACs/ADC 15 mA + muxes/logic/comparators 15 mA + MIDI 10 mA + Hall un-gated 25 × 6 mA = 150 mA + LEDs 8 × 10 mA = 80 mA → **≈ 0.31 A** | 31 % | **69 %** ✓ |
| PAM8302 | 2.5 W at 5.5 V ([Adafruit](https://adafruit.com/products/2130)) | Battery-fed: ≤ ~1.7 W out at 4.2 V into 4 Ω, ≈ 0.67 A in at 3.0 V [ENG] | within rating | ✓ (a lower supply cuts output power, not margin) |
| Battery pack: 2P pouch, ≥ 2500 mAh each, ≥ 1C cells | ≥ 5 A | 1.64 + 0.57 (MiniBoost in) + 0.67 = **≈ 2.9 A** | 58 % | **42 %** ✓ (cell C-rating and protection trip ≥ 2.5 A per cell must be confirmed for the chosen cells: UNVERIFIED) |
| Polyfuse / switch / wiring | 5 A hold / 6 A / 22 AWG | 2.9 A | 58 % / 48 % | ✓ |
| Charger bq24074 | 1 A charge; LOAD 1.5 A ([Adafruit](https://www.adafruit.com/products/4755)) | **not in the load path** | n/a | n/a |

Runtime [ENG]:
- Typical draw ≈ 2.1 W analog ÷ 0.83 ÷ 0.83 ÷ 0.88 ≈ 3.5 W, plus digital ≈ 0.5 W, plus speaker average ≈ 0.3 W,
  so **≈ 4.3 W**.
- 2 × 2500 mAh (18.5 Wh) gives **≈ 4 h**; 2 × 5000 mAh pouches (thicker, ~10 mm) give ≈ 8 h.
- The double conversion (12 V boost, then isolated ±12 V) costs about 10 % against v1's single TPS65131 stage.
  That's the price of THT/module-only.

### 5b.3 Inrush and soft-start
| Point | Spec |
|---|---|
| Main input | P-MOSFET high-side soft-start (FQP27P06-class TO-220 + 2N3904 driver; part UNVERIFIED), gate RC 100 kΩ / 1 µF, so **20–30 ms ramp**. Target **peak inrush < 3 A** (60 % of the pack's 5 A) into ≈ 800 µF total downstream input capacitance (dV/dt ≈ 3.7 V / 25 ms gives I = C·dV/dt ≈ 0.12 A of cap charging, plus load). Verify in SPICE with the MOSFET model |
| DCWN06A output capacitance | Keep ≤ 220 µF per rail before the LDO. Mean Well's max capacitive load is UNVERIFIED (datasheet), so confirm before layout |
| ±10 V LDOs | LM317/LM337 adjust-pin soft-start (C_adj 10 µF with discharge diodes) for a **≈ 15 ms rise**. **Both rails rise together within 5 ms** because the MCU holds nothing on them; the LDOs ramp from the same converter. **1N5819 reverse clamps** from each rail to ground (anti-reversal / latch-up). Voice-board bulk ≤ 470 µF per rail |
| Speaker pop | PAM8302 SD held low by the MCU until 300 ms after the rails are good (the MCU reads ±10 V through dividers on spare mux inputs) |
| Autotune at power-up | Starts after a 2 s warm-up; re-tunes after 10 min (thermal settling), then on the NTC trigger (v1 §3) |

### 5b.4 Ripple filtering (numbers) [ENG; DCWN06 ripple/f_sw UNVERIFIED, assumed ≤ 100 mVp-p at ≥ 100 kHz]
| Stage | Component | Attenuation at 100 kHz | Result |
|---|---|---|---|
| 12 V boost output → DCWN06A input | 100 µF low-ESR + DCWN internal input filter | — | Isolates the boost ripple from the converter's own ripple |
| After DCWN06A, per rail | **LC: 47 µH (THT, ≥ 0.5 A, DCR ≤ 0.5 Ω) + 100 µF low-ESR; damping 1 Ω + 220 µF across**. f₀ = 1/(2π√(47 µH·100 µF)) ≈ 2.3 kHz | 40·log(100/2.3) ≈ **65 dB** | 100 mVp-p → ≈ 56 µVp-p |
| LM317/LM337 with C_adj 10 µF | PSRR ≈ 60–80 dB at 120 Hz falling to ≈ 20–30 dB at 100 kHz (UNVERIFIED) | +20 dB | ≈ **6 µVp-p at f_sw** |
| In-band (20 Hz–20 kHz) noise on ±10 V | LDO noise + residual | — | **Target < 50 µVrms** (as v1 §7.8), then verify with SPICE (vendor LDO models) |
| Damping check | The LC resonance at 2.3 kHz is in band. Q ≤ 1 with the 1 Ω / 220 µF snubber; **load-step test in SPICE** (VCA thump current step) must show < 5 mV ring | — | — |
| 5 V digital | MiniBoost → ferrite + 22 µF at each DAC/ADC breakout (AD5693R uses its internal 2.5 V reference, 2 ppm/°C, [Adafruit](https://www.adafruit.com/product/5811)) | — | Digital ground joins analog at one star point on board B |

### 5b.5 Alternative (not default): USB-PD 12 V path for true power-path charging
Adafruit's HUSB238 PD sink breakout selects 5/9/12/15/18/20 V at 2–3 A, $5.95 in stock
([Adafruit](https://www.adafruit.com/product/5807)). At 12 V it could feed the DCWN06A directly (Schottky-OR with
the boost, battery→boost switched off when PD is present), taking the analog load off the battery while charging.
But charging would then need either a second USB-C port into the bq24074 (5–10 V input) or a 12 → 5 V buck: more
parts. Keep it as an option if "play all night on the charger" matters to the owner.

## 6. New/changed risks
| Risk | L | Mitigation |
|---|---|---|
| ~~DCWN03E-12 margin~~ **Resolved (§5b)**: DCWN06A-12 at ±250 mA against a ±150 mA worst case. Remaining: DCWN06 ripple, switching frequency and max capacitive load are UNVERIFIED until the datasheet is read | L–M | §5b filter sized for 100 mVp-p at ≥ 100 kHz; read datasheet before layout |
| ~~MiniBoost near limit~~ **Resolved (§5b)**: digital only, 0.31 A of 1 A | L | — |
| **[NEW E3]** Old USB-A host port (500 mA) via A-to-C cable: 1 A charging could make the host drop the port, and USB-MIDI with it | L–M | bq24074 VIN-DPM backs off below ≈ 4.5 V; optional LM393 CC-sense → 500 mA mode. Bench-test on several hosts |
| **[NEW E1]** Mod VCA CV feedthrough shifts pitch as the wheel moves (≈ 5 cents untrimmed) | M | **[CHANGED E1 rev 1]** Firmware auto-null at every autotune (H11F1 mute + ADC sense + PWM injection), target < 0.5 mV. No manual trim |
| **[NEW E3]** No ESD protection on the rear USB-C D± lines | L–M | Connector shell to the ground star; look for a through-hole TVS |
| Charging while playing: loads sit on the battery node, not the charger's power path (bq24074 LOAD is limited to 1.5 A ([Adafruit](https://www.adafruit.com/products/4755)), below the 2.9 A worst case). So while playing, the charger keeps feeding the battery and may not terminate | M | Accept and document: at worst-case draw the battery still discharges slowly while plugged in. Charger thermal and safety limits stay active (charge-timer config on the Adafruit board UNVERIFIED). Alternative: USB-PD 12 V path (§5b.5) |
| AD5693R stock (7 when checked) | M | Buy early; 12-bit coarse/fine fallback is designed in |
| Board area too small for the voice (tight estimate) | M | Lay out the VCO block first and re-estimate. Fallback: grow depth 10–15 mm, or a 3rd stacked board |
| Header-stack noise/microphonics (analog over 2.54 mm headers) | L–M | Machined pins, ground pins interleaved, short runs |
| Thickness over OP-1 (≈ 32–36 mm) | H (certain) | Accept, or cut controls. Owner decision |
| Modules discontinued (Adafruit revisions) | L | Socketed, so a swap needs only a footprint-compatible replacement |

## 7. Owner questions
1. Is a ≈ 285 × 180 × 34 mm box acceptable? (The OP-1 is 288 × 102 × 29; 40 controls plus keys can't fit 102 mm of depth.)
2. Is MIDI control of pitch, glide, cutoff and envelopes enough, with mixer, emphasis and waveforms as knobs only?
3. ~~Do you prefer USB-C charging (bq24074 + MiniBoost) or a single PowerBoost 1000C on micro-USB?~~ **[CHANGED E3] Resolved: one rear USB-C for charging, USB-MIDI and firmware.**
4. Filter-tracking calibration: PhotoMOS (automatic), or "turn emphasis up, press TUNE" (one gesture)?
