# Built-in delay / echo: options and recommendation

Status: rev 0, 2026-11-12. Answers the owner's round-4 request (`design/little-d/owner.md`, 22:30): "Is there a way for us to build in some effects, mainly a delay and echo?"
Base documents: `budget-variant.md` rev 12 (power, boards), `round4-answers.md` (board-area method, power recount), `fold-answers.md` (FOLD depth formula).

Conventions as in `budget-variant.md`: link = read this session (2026-11-12). **ESTIMATE** = my number. **UNVERIFIED** = a source exists but I couldn't confirm the figure. [ENG] = engineering judgement. [CALC] = arithmetic from cited figures.
This doc gives constraints (control count, board area, power). Panel placement and looks stay with the design team.

---

## 0. Bottom line

**Recommend (a): one PT2399 echo chip, about $10–14 all in, about +0.2–0.5 W, and 3 pots plus 1 toggle.** Its repeats get darker and crunchier as the delay gets longer, which is the "echo" sound by default, with no firmware and no trimmers. The dry signal stays 100 % analog and is untouched when MIX is at zero.

**Ask the owner one thing first:** *does the delay need to lock to MIDI clock or tap tempo, or run longer than about half a second?*
- **No:** build (a).
- **Yes:** build (c), a second Pico 2 with I2S converter modules. It costs about $28–35, draws about +0.35–0.5 W, and needs firmware work, but it gives 4+ s delays, tape modelling and sync.

| | (a) PT2399 | (b) BBD (V3205/V3207) | (c) Pico 2 + I2S modules | (d) ready-made DSP (FV-1, Daisy Seed) |
|---|---|---|---|---|
| Wet path | Digital inside the chip (ADC/DAC built in), all controls analog | **True analog** | Digital | Digital |
| Max delay | ≈ 340 ms at datasheet spec, ≈ 600 ms lo-fi; ≈ 1 s with two chips | 51 ms (V3207), 205 ms (V3205) | ≈ 4–7 s | FV-1 ≈ 1 s (UNVERIFIED); Daisy minutes |
| Character | Gets darker and grittier with length: "echo" | Dark and warm, but too short for echo except on the V3205 | Anything, including tape models | Anything |
| Panel controls | 3 pots + 1 toggle | 3 pots + 1 toggle | 3 pots + 1 toggle + optional TAP button | 3 pots + toggle |
| Power (at 5 V) | ≈ 0.2–0.5 W | ≈ 0.2–0.35 W | ≈ 0.35–0.5 W | FV-1 ≈ 0.1–0.2 W; Daisy ≈ 0.5 W+ (UNVERIFIED) |
| Main-board area | ≈ 1,600–2,000 mm² | ≈ 3,000–3,500 mm² | ≈ 3,500–4,000 mm², plus height issues | ≈ 2,000–3,000 mm² |
| Cost (one unit) | **≈ $10–14** | ≈ $25–35 | ≈ $28–35 | ≈ $30–40 |
| Build effort | Low (one DIP, about 40 parts) | High (trims, companding, filters) | Medium hardware, **high firmware** | Medium, plus programming and supply risk |
| MIDI sync | Not in v1 (possible later, §2.6) | Possible (Pico clock) | **Yes** | Yes (Daisy); FV-1 awkward |
| Calibration | None | **Bias and balance trimmers**: conflicts with "no rigmarole" | None | None |
| Verdict | **Recommended** | Out | **The upgrade path if sync matters** | Out |

---

## 1. What "delay" and "echo" should mean here (proposal)

The owner said "mainly a delay and echo". That covers two flavours of one effect, so one block with a character switch covers both:

- **DELAY (clean):** repeats that stay close to the original's tone and decay evenly, with no pitch movement. Good for rhythmic doubling and slapback.
- **ECHO (tape-style):** each repeat is **darker and a little softer at the edges than the one before**, with a **slow, slight pitch wobble** (wow) and **soft saturation in the feedback loop**. Turned up high, it runs into a controlled **self-oscillating swell** without hard clipping. This is the Space Echo / Echoplex idea.

So the proposal is **one delay line plus a 2-position CHARACTER toggle (DELAY / ECHO)**. In ECHO the toggle switches in a lower loop-filter corner and turns on the wobble. Reverb is out of scope; the owner didn't ask for it.

---

## 2. Option (a): PT2399 echo chip (recommended)

### 2.1 Part and price
| Item | Price | Source |
|---|---|---|
| PT2399, DIP-16, through-hole | **$1.50, in stock** | [PedalPCB A6006](https://www.pedalpcb.com/product/a6006/) (US) |
| Same | price not shown on page | [Tayda](https://taydaelectronics.com/pt2399-2399-echo-audio-processor-guitar-ic.html), rides the existing Tayda order (price UNVERIFIED) |
| Same | from $0.50, 794 in stock | [LCSC C84963](https://lcsc.com/product-detail/Audio-Interface-ICs_PTC-Princeton-Tech-PT2399_C84963.html) (not used: no JLC box to ride in) |

### 2.2 What the chip can do
- **Supply:** 4.5–5.5 V; **30 mA typ, 40 mA max** ([datasheet](https://www.rigpix.com/components/pt2399.pdf)).
- **Delay vs THD:** 31.3 ms at 0.13 % THD up to **342 ms at 1.0 % THD** (datasheet table, clock 22 → 2 MHz).
- **Output noise:** −90 dBV typ / −80 dBV max, A-weighted (datasheet; not tied to a delay time).
- **Delay vs control:** delay (ms) ≈ 11.46 × R(kΩ) + 29.7, where R is the resistance from pin 6 to ground. **A 50 kΩ pot gives about 35–600 ms.** The chip "sounds crunchier and crunchier the longer the delay gets" ([Electric Druid](https://electricdruid.net/useful-design-equations-for-the-pt2399/)).

**Usable range for this instrument [ENG]:** set the TIME pot to give **≈ 40–450 ms**. Above about 350 ms the repeats get gritty and lose highs, which is exactly the ECHO character, so stopping at 450 ms keeps the top of the pot musical. If the owner wants longer, a **second PT2399 in series** gives ≈ 0.8–0.9 s. That costs +$2–3 and ≈ +600 mm² of board, and noise roughly doubles at the long end.

### 2.3 Circuit [ENG]
The standard PT2399 echo topology (datasheet application circuit, as used in countless pedals), adapted to our levels:

```
VCA out (op-amp, ~1 V) ──┬───────────────────────────────── dry ──► OUTPUT MIXER (TL072) ──► VOLUME ──► LM386 / phones / line
                         │                                                  ▲
                         └► input buffer/attenuator ─► 2-pole LPF ─► PT2399 ─► 2-pole LPF (reconstruction, the chip's own op-amps + 1 TL072 half)
                                    ▲                                                       │
                                    │                                                       ├──► MIX pot (wet level) ──┘
                                    └──── REPEATS pot ◄── loop LPF (DELAY: ≈ 5 kHz / ECHO: ≈ 2 kHz, set by the CHARACTER toggle) ◄── soft clip (2 diodes)
   TIME pot (50 k rheostat + series R) ── PT2399 pin 6 ─── + small wobble current from a 1-op-amp triangle LFO (≈ 0.5–2 Hz), switched in on ECHO
```

- **Placement in the chain:** **after the VCA, before VOLUME** and the output stage. That way it treats EXT audio in too, the speaker and phones/line both get the echo, and repeats ring on after the VCA closes (the point of an echo). The **dry path stays fully analog and is never switched**: the wet signal is only added in the output mixer. With MIX at minimum the instrument is electrically the same as today (the wiper sits at ground).
- **Wobble LFO:** analog, one TL072 half wired as a triangle/square oscillator. It feeds a few µA into pin 6 through a large resistor, on the ECHO setting only. **It uses no Pico GPIO.**
- **Runaway:** at full REPEATS the loop gain goes slightly above 1, and the 2-diode soft clip plus the loop LPF turn that into a dark, controlled swell instead of a hard squeal [ENG]. Bench-check the level at the speaker.
- **Supply [ENG]:** the PT2399 is digital inside and known to put clock noise on its supply. **Default: feed it from the bq25185 5 V boost through a ferrite plus 100 µF**, with its own ground return to the star point. That adds ≈ 0.15–0.2 W at the cell. **Fallback**, if the bench shows noise: a 78L05 from the +9 V rail. That's cleaner, but ≈ 0.4–0.5 W, because 30 mA has to come up through the MC34063 boost at ≈ 75 % [CALC from `round4-answers.md` §3.1 efficiencies].
- **Placement on the board [ENG]:** keep the PT2399 (internal clock 2–22 MHz) **≥ 30 mm from the ladder, the AS3046 expos and the Hall-sensor strip harness**, which is the same rule as the MC34063s. Keep its digital ground on its own return.

### 2.4 Panel controls (constraint for design)
| Control | Part | Notes |
|---|---|---|
| **TIME** | 9 mm pot, 50 kΩ (Tayda A-5622 T18 family if it comes in 50 k, else nearest; UNVERIFIED) | 2-wire rheostat into pin 6. Analog only, so no MIDI (consistent with "knob-only controls send no MIDI") |
| **REPEATS** (feedback) | 9 mm 10 kΩ | Up to slight self-oscillation |
| **MIX** (wet level) | 9 mm 10 kΩ | Fully counter-clockwise = no effect |
| **CHARACTER** DELAY / ECHO | sub-mini toggle, ON-ON | Switches the loop LPF corner and the wobble |

**Total: 3 pots + 1 toggle.** It uses no Pico channels and no GPIO. The minimum version (cut the toggle and always run ECHO) is 3 pots. An optional bypass LED is not counted.

### 2.5 Power, area, cost
- **Power:** ≈ **+0.2–0.5 W** at 5 V [ESTIMATE]: PT2399 0.15 W, plus 1.5 TL072 on ±9 V (≈ 0.05–0.1 W after the converters), plus the supply path (§2.3). Against today's 2.0–3.6 W, **runtime drops ≈ 6–20 %**: on the 22.2 Wh 1S2P pack, ≈ 4.7–9 h becomes ≈ 4.2–8.4 h [CALC, scaled by P/(P+ΔP)].
- **Board area [ESTIMATE, using the `round4-answers.md` §1 courtyard method]:**
  - PT2399 DIP-16 ≈ 220 mm², 2 × TL072 ≈ 200, ≈ 25 standing 1/8 W resistors ≈ 200, ≈ 15 caps ≈ 450, plus the LFO and filter parts: **≈ 1,100–1,300 mm² of courtyard, so ≈ 1,600–2,000 mm² of board** at 65–75 % fill.
  - The 4 controls add their own footprints wherever the design puts them (≈ 4 × 130 mm² for 9 mm pots plus a toggle).
  - **Flat concepts:** on the 268-wide main board, that's **≈ +6–8 mm of depth** (268 × 115 → ≈ 268 × 121–123), unless the strip-C harness saving in `round4-answers.md` §1 materialises.
  - **FOLD:** the echo belongs with the VCA and output, which are in the **lid**. That adds to the lid's existing 9–12k mm² shortfall: in `fold-answers.md`'s D ≥ 6 + (23,300 + A)/262, A grows by ≈ 1,600–2,000, so **D grows ≈ 6–8 mm**. If its pots sit in the base: MIX and REPEATS are low-Z audio (cross like VOLUME, guarded). **TIME on pin 6 is sensitive** (current noise becomes pitch wobble in the repeats), so keep TIME in the lid.
- **Cost:**

| Item | Cost |
|---|---|
| PT2399 | $1.50 ([PedalPCB](https://www.pedalpcb.com/product/a6006/)) |
| 2 × TL072 | $0.60 (Tayda, ESTIMATE as in `budget-variant.md`) |
| ≈ 25 resistors, ≈ 15 caps, 2 diodes, ferrite | ≈ $2.00 (ESTIMATE) |
| 3 pots (A-5622 class, $0.59) + 3 knobs ($0.30) | $2.67 |
| 1 toggle | $0.80 ([Tayda](https://www.taydaelectronics.com/non-threaded-sub-mini-toggle-switch-spdt-on-none-on-short-handle-gold-pcb-pins.html)) |
| Board area, ≈ 2.5–3.1 in² at $0.61–1.22/in² | ≈ $1.50–3.80 |
| Shipping (rides the Tayda order; PedalPCB separately ≈ $5, ESTIMATE) | $0–5 |
| **Total** | **≈ $9–16, call it $10–14** |

### 2.6 MIDI sync (not in v1; a possible later add)
The PT2399 delay is set by the current out of pin 6. A **Pico PWM-CV into a transistor current sink on pin 6** could set the delay, and the Pico could **close the loop by counting the chip's clock** (the VCO pin) to land exactly on a MIDI-clock division. Cost: ≈ $0.50 plus **2 GPIO**. The main Pico's spare GPIO is already thin (`velocity-and-keys-v2.md` §1 notes the old ≈ 4 spare are being eaten; tally UNVERIFIED), and a 2–22 MHz trace runs across the board. **Not recommended for v1.** Reserve the option only if a GPIO recount shows 2 spare.

### 2.7 Risks
| Risk | L | Mitigation |
|---|---|---|
| PT2399 supply/clock noise into the audio or speaker | M | Ferrite + bulk cap, own ground return, ≥ 30 mm keep-away; 78L05 fallback. **Breadboard test first** (§6.2) |
| Hiss on long repeats | M | It's mixed in only, not in the dry path. Pot range stops at ≈ 450 ms. The loop LPF hides the HF hiss on ECHO |
| Counterfeit or poor-batch chips (pedal forums report variance, UNVERIFIED) | L | Buy 2 ($3) |
| Lid/main-board area growth | M (FOLD) | Count it in the next placement pass (§2.5) |

---

## 3. Option (b): BBD analog delay (out)

- **Parts:**
  - **V3207** (1024 stages): ≈ 1–51.2 ms ([Electric Druid](https://dev.electricdruid.net/?p=31623)).
  - **V3208** (2048 stages): 2–100 ms ([Electric Druid](https://electricdruid.net/product/v3208/)).
  - **V3205** (4096 stages): **20.48–204.8 ms**, VDD 4–9 V, max clock 100 kHz, **S/N 67 dB**, "Special DIL-8" ([datasheet](https://studylib.net/doc/18525851/v3205-4096-stage-low-noise-bbd-analog-delay-line)).
  - All are through-hole DIP-8, but **stock is patchy:** in May 2026 Aion FX ($5.35) was the only V3207D source a forum user found not out of stock ([PedalPCB forum](https://forum.pedalpcb.com/threads/v3207d-sources.29316/)). V3205 price and US stock are UNVERIFIED ([op-electronics](https://www.op-electronics.com/en/delay-chips/93-v3207d.html) lists it, no price).
- **Needs:**
  - a two-phase clock: a V3102, or the Pico PIO plus a CMOS buffer at the BBD supply;
  - 3rd–4th-order anti-alias and reconstruction filters (≈ 2 TL072);
  - a **compander** (NE570/SA571 class; US qty-1 availability UNVERIFIED) to get past ≈ 67 dB;
  - **bias and balance trimmers.**
- **Sound:** genuinely analog, dark and warm. Only the V3205 reaches echo lengths, and at 205 ms its clock is 10 kHz, so the bandwidth is under ≈ 4 kHz: murky but nice.
- **Power ≈ 0.2–0.35 W; area ≈ 3,000–3,500 mm²; cost ≈ $25–35 (ESTIMATE); 3 pots + 1 toggle.**
- **Why it's out:** it is the only option that needs **trimmers**, which breaks the "no calibration rigmarole" rule. It's ≈ 2–3× the cost and area of (a), its max delay is shorter than (a)'s, and the part supply is shaky. Its single advantage, an analog wet path, isn't worth that when the dry path is analog either way.

---

## 4. Option (c): second Pico 2 + I2S converter modules (the upgrade path)

- **Hardware (all through-hole or ready-made modules):**

| Item | Price | Source |
|---|---|---|
| Raspberry Pi Pico 2 | $5.75 | [SparkFun](https://www.sparkfun.com/raspberry-pi-pico-2.html) (as `budget-variant.md`) |
| DAC: Adafruit #6250 PCM5102, line out, 112 dB SNR, 3–5 V | $6.45 ea in 2s ($12.90) at Jameco; Adafruit single price UNVERIFIED | [Jameco](https://www.jameco.com/z/6250-Adafruit-Industries-Adafruit-PCM5102-I2S-DAC-with-Line-Level-Output-112dB-SNR_2884135.html) |
| ADC: generic PCM1808 module (24-bit, 105 dB class) | ≈ $5–8, **ESTIMATE** (marketplace listings, e.g. [Walmart](https://www.walmart.com/ip/PCM1808-Audio-Decoder-Module-24-bit-ADC-Board-for-Audio-Signal-Development/20533666242), no reliable US stocked source found) | — |
| *(One-chip codec alternative: SparkFun WM8960 BOB-21250, $17.95: **retired**, not for sale ([SparkFun](https://www.sparkfun.com/sparkfun-audio-codec-breakout-wm8960.html)))* | — | — |
| TL072 level shifting (±9 V ↔ 3.3 V-domain modules), passives, sockets | ≈ $2–3 | ESTIMATE |

- **Capability [CALC/ENG]:**
  - The RP2350's 520 KB of SRAM holds ≈ 4.5 s at 48 kHz/16-bit mono, or ≈ 7 s at 32 kHz.
  - The Cortex-M33 FPU handles a tape model: interpolated read head with wow/flutter, saturation and a darkening LPF in the loop, and a ping-pong-free mono echo.
  - Tap tempo and MIDI-clock sync.
- **MIDI:** fan the 6N138 TRS-MIDI output to the effect Pico's UART RX as well. That costs no main-Pico GPIO. USB-MIDI clock arrives only at the main Pico, so forwarding it needs **1 main-Pico GPIO** (UART TX).
- **Controls:** TIME, REPEATS and TONE go to the effect Pico's own 3 ADC pins. **MIX stays an analog pot** in the output mixer, so the dry path stays analog. Add the CHARACTER toggle, plus an optional TAP button. **Total: 3 pots + 1 toggle (+1 button).** It uses no main-Pico mux channels.
- **Power ≈ +0.35–0.5 W [ESTIMATE]:** Pico 2 0.1–0.25 W plus the two modules (current not published, UNVERIFIED) plus TL072. That's a runtime cut of ≈ 9–20 %.
- **Area ≈ 3,500–4,000 mm² [ESTIMATE]:** Pico courtyard 1,070 mm² (`round4-answers.md`) plus two modules (sizes UNVERIFIED) plus interface. **Height problem:** modules on headers break the main board's ≤ 6.5 mm top-side rule, so they need the underside (≤ 8 mm stack, like the main Pico) or must be soldered flat.
- **Cost ≈ $28–35:** parts ≈ $21–25, controls ≈ $3–4, board ≈ $3–5, shipping rides the US order.
- **Risks:**
  - **firmware** (a whole second program; audio-rate I2S via PIO on the RP2350 is well trodden, but it's real work);
  - the PCM1808 module source;
  - digital noise from a second MCU near the analog voice.

---

## 5. Option (d): ready-made delay/DSP modules (out)

- **Spin FV-1:** $20 "pre-soldered", in stock, plus a separate $1 through-hole adapter ([PedalPCB](https://pedalpcb.com/product/6-1-4)). The chip is SOIC-28, so it only counts as "ready-made" with the pre-soldered adapter. It needs a crystal, a program EEPROM (the main Pico could program it) and 3.3 V. Max delay ≈ 1 s (UNVERIFIED). It's **≈ $30+** with support parts, programming is fiddly, and it gains nothing over (a) for a single echo.
- **Electro-Smith Daisy Seed:** about $25.20 direct in March 2026, with a codec and SDRAM on board. Forum reports in March–April 2026 were mixed on whether production had paused; later posts said it was in stock ([PedalPCB forum](https://forum.pedalpcb.com/posts/379045/)). Huge capability, but it's a whole STM32 platform. Power is likely ≥ 0.5 W (UNVERIFIED), and there's supply risk. It's (c) with more cost and less certainty.
- **Generic PT2399 boards:** the ones on sale are karaoke mic-reverb boards running from 7–24 V with mic preamps ([example](https://www.fruugo.us/pt2399-karaoke-reverb-board-with-mic-preamplifier-7v24v-diy-audio-effects-amplifier/p-449621212)), so they're wrong for line level. Eurorack PT2399 modules are the wrong form and price. **No suitable ready-made module.**

---

## 6. Recommendation

1. **Build (a), one PT2399 with a DELAY/ECHO CHARACTER toggle**, after the VCA and before VOLUME, with the dry path untouched.
   - **Constraints for design:** 3 pots (TIME, REPEATS, MIX) + 1 toggle (CHARACTER); ≈ 1,600–2,000 mm² of main/lid board (+6–8 mm depth at 268 wide); +0.2–0.5 W; ≈ $10–14.
   - It uses no Pico channels and no GPIO, and needs no calibration.
2. **Before the board order:** breadboard one PT2399 ($3, about 1 h) on the synth's actual VCA output, with the battery boost as its supply. Check clock whine at the speaker and phones, the TIME range, and the runaway level. Fall back to a 78L05 supply if needed.
3. **If the owner answers "yes" to sync or long delays, switch to (c)** instead of (a). Don't build both: a hybrid doubles the area and the controls for little gain.
4. **Totals impact:** with (a), the one-unit totals in `budget-variant.md` §v1.10 rise by ≈ $10–14 (e.g. LiPo build ≈ $311–386 → ≈ $321–400).
