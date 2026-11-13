# Pin check and audio-quality check: Daisy Seed vs Pico 2 + SGTL5000

Status: rev 0, 2026-11-13. Answers the owner: "Check the pin thing. Audio feels the most important since we're introducing digital stuff."
Compares (A) **Pico 2 + Teensy Audio Shield Rev D (SGTL5000) + 74HC595** (`single-chip-research.md` §1.6) with (B) **Daisy Seed as the only digital chip**.
I/O list from `budget-variant.md` rev 12 (§v1.2, Part 2 §4) and the control counts in `design/concepts/common-how-it-works.md` rev 7.1.
Conventions as in `budget-variant.md`. Link = read this session. **UNVERIFIED** = a source exists but I couldn't confirm the figure. **ESTIMATE** = my number. [ENG] = engineering judgement. [CALC] = arithmetic.

---

## 0. Bottom line

1. **Daisy Seed pins: everything fits on the 31 header GPIO with 5 spare, and no expander is needed.** Three things to note:
   - The codec, SDRAM and QSPI flash use **none** of the header pins.
   - **TIM5 is a 32-bit timer with all 4 channels on header pins** (D25, D24, D28, D16). That gives 3 VCO counters plus a 4th for filter-scale cal.
   - TIM3 provides the 3 PWM CVs. MIDI in and out and SPI each get their own peripheral.
2. **Pico 2 + SGTL5000 also fits, but with 0 spare, and only with the 74HC595.** The earlier claim holds for the list it counted. That list missed two items:
   - **A 4th count input for the automatic filter-scale cal.** v1.2 promises this cal, and Part 2 §4 wires the ladder to a count input.
   - **TRS MIDI out**, if it's wanted. The locked spec has MIDI in only.

   Neither fits on the Pico without another workaround (§2.3). There is also a power-up hazard: **the 74HC595 would drive the sensor-LDO enable**, and its outputs are random at power-up (§2.2).
3. **Audio: the Daisy wins on all four axes.**
   - **Converter:** wet-path noise floor **8–18 dB lower**, ADC distortion **≈ 20–25 dB lower**.
   - **DSP throughput:** ≈ 5–7× (ESTIMATE).
   - **Memory:** ≈ 1 MB of on-chip SRAM plus 64 MB SDRAM, against 520 KB shared with the control firmware. Long halls in float, CloudSeed-class reverbs and multi-second tape echo fit only on the Daisy.
   - **Pin room.**

   The **Pico Plus 2 closes only the echo-length gap.** Its PSRAM is too slow for reverb taps (§3.5).
4. **Recommendation, with audio weighted highest: switch to the Daisy Seed (buy a Seed3 or a 65 MB Seed2 DFM, $34.99).** Keep the dry path analog. The costs:
   - ≈ +$19;
   - ≈ +0.3–0.6 W;
   - porting the control firmware off PIO (§1.4).

   If the owner won't take those costs, the best audio on the Pico path is **PCM1808 + PCM5102A instead of the SGTL5000**. Its converter is roughly PCM3060-class and it frees 2 pins, but DSP and memory stay Pico-sized and the PCM1808 comes only from marketplace sellers.

---

## 1. Daisy Seed pin check

### 1.1 Which Seed you'd actually get
libDaisy's board-detect code ([daisy_seed.h](https://github.com/electro-smith/libDaisy/blob/master/src/daisy_seed.h), [daisy_seed.cpp](https://github.com/electro-smith/libDaisy/blob/master/src/daisy_seed.cpp), read via raw.githubusercontent) names five versions:

| libDaisy name | Common name | Codec |
|---|---|---|
| DAISY_SEED | Rev 4 (original) | **AK4556** |
| DAISY_SEED_1_1 | Rev 5 | **WM8731** (I2C-configured) |
| DAISY_SEED_2_DFM | Seed2 DFM | **PCM3060** |
| DAISY_SEED_1_2 | **Rev 7** | **PCM3060** |
| DAISY_SEED_3 | **Seed3** | **TI TAC5242**, USB-C, "pin-compatible" |

- **Seed3 launched July 2026.** It has the "same MCU", USB-C and a "new audio codec … 32-bit, 192kHz". A forum user reports Electrosmith "are no longer selling the previous Daisy Seed version" ([PedalPCB Seed3 thread](https://forum.pedalpcb.com/threads/new-pin-for-pin-compatible-daisyseed-seed3.29897/latest), Jul 24–Aug 24 2026).
- From Nov 1 2026, "the 65MB Seed2 DFM and Seed3 go from $29.99 to $34.99" ([PedalPCB tracker, Oct 26 2026](https://forum.pedalpcb.com/threads/free-stock-price-tracker-for-daisy-seeds-heads-up-prices-change-nov-1.30660/latest)).
- **So a new purchase is a Seed3 (TAC5242) or a Seed2 DFM (PCM3060). A Rev 7 from reseller stock is also PCM3060.** All are pin-compatible for this map.
- The TAC5242 identification comes only from libDaisy's comment; Electrosmith's page wasn't readable here (UNVERIFIED).

### 1.2 Pins consumed on-module (not on the header)
From [daisy_seed.cpp](https://github.com/electro-smith/libDaisy/blob/master/src/daisy_seed.cpp):
- **Codec:** SAI1 on PE2 (MCLK), PE3 and PE6 (data), PE4 (FS), PE5 (SCK). Codec reset/de-emphasis on PB11.
- **QSPI flash:** PF6–PF10, PG6.
- **Board detect:** PD3–PD5, PH6. **User LED:** PC7. **Test point:** PG14.
- **SDRAM:** the FMC bus (ports D–I), internal. Not listed in the files read, but none of it is a header pin.
- **USB device (MIDI, DFU):** the on-module USB FS port, internal.

**Result: none of D0–D30 is taken by the codec, SDRAM or flash.** Header pins 16–21 are audio in L/R, audio out L/R, AGND and +3V3A ([Seed datasheet v1.0.5, mirror](https://www.electrokit.com/upload/product/41020/41020659/Daisy_Seed_datasheet_v1.0.5.pdf)).

**Software conflicts to respect:**
- **libDaisy's `System` runs TIM2 as its free-running µs timer** ([system.cpp](https://github.com/electro-smith/libDaisy/blob/master/src/sys/system.cpp)). **Use TIM5 for the counters**; it sits on the same pins, PA0–PA3.
- libDaisy's default pin for TIM3 CH2 is the on-board LED (PC7). Name PA7 explicitly.

### 1.3 Timer, ADC and peripheral facts used
- **Timer channel pins** come from libDaisy [pwm.h](https://github.com/electro-smith/libDaisy/blob/master/src/per/pwm.h). TIM3 and TIM4 are 16-bit; TIM5 is 32-bit.
  - **TIM5:** CH1 PA0 = D25, CH2 PA1 = D24, CH3 PA2 = D28, CH4 PA3 = D16.
  - **TIM3:** CH1 PA6 = D19 or PB4 = D9; CH2 PA7 = D18 or PB5 = D10; CH3 PC8 = D4; CH4 PB1 = D17 or PC9 = D3.
  - **TIM4:** CH1–CH4 on PB6–PB9 = D13, D14, D11, D12. These clash with USART1 and I2C1, so TIM4 isn't used here.
  - The datasheet also lists TIM2 CH1–4 on PA0/PA5, PA1, PA2, PA3.
- **ADC:** 12 inputs (A0–A11), 16-bit. Header pins 24, 25, 28, 29 and 30 (D17, D18, D21, D22, D23) are **3.3 V-only**; the rest are 5 V-tolerant (datasheet).
  - libDaisy's built-in mux reader handles at most **8 channels per mux, 3 select lines** ([adc.cpp](https://github.com/electro-smith/libDaisy/blob/master/src/per/adc.cpp)). Our CD4067s need 4 selects, so the scanner is custom code (§1.4).
- **Clock:** libDaisy defaults to 400 MHz CPU (480 MHz "Boost"), with timer clock = 2 × PCLK1 ([system.h](https://github.com/electro-smith/libDaisy/blob/master/src/sys/system.h), [tim.cpp](https://github.com/electro-smith/libDaisy/blob/master/src/per/tim.cpp)). That gives ≈ 200 MHz at the default and 240 MHz in Boost; the PCLK1 value is UNVERIFIED.

### 1.4 Allocation table (Daisy Seed; header pin in brackets)

| Need | Seed pin | MCU pin / function | Why this pin |
|---|---|---|---|
| **VCO 1 frequency count** | D25 [32] | PA0 **TIM5_CH1** input capture | 32-bit timer |
| **VCO 2 count** | D24 [31] | PA1 TIM5_CH2 | " |
| **VCO 3 count** | D28 [35] | PA2 TIM5_CH3 | " |
| **Filter self-osc count** (filter-scale cal) | D16 [23] | PA3 TIM5_CH4 | Free 4th channel on the same timer |
| PWM CV: VCA balance (auto-null) | D4 [5] | PC8 TIM3_CH3 | 16-bit PWM |
| PWM CV: mod depth (AS3360 A) | D9 [10] | PB4 TIM3_CH1 | Free because SPI runs TX-only (no MISO) |
| PWM CV: velocity (AS3360 B) | D18 [25] | PA7 TIM3_CH2 | 3.3 V-only pin, output: fine |
| SPI SCK → 2× MCP4822 | D8 [9] | PG11 SPI1_SCK | |
| SPI MOSI | D10 [11] | PB5 SPI1_MOSI | |
| DAC 1 CS | D7 [8] | PG10 SPI1_NSS (or GPIO) | |
| DAC 2 CS | D0 [1] | PB12 GPIO | |
| CD4067 S0 / S1 / S2 / S3 | D2 [3] / D1 [2] / D6 [7] / D3 [4] | PC10 / PC11 / PC12 / PC9 | **All on port C**, so one DMA write to GPIOC→BSRR steps all four [ENG] |
| Mux A → ADC | D15 [22] | PC0 (A0) | Pins with no timer use |
| Mux B → ADC | D20 [27] | PC1 (A5) | " |
| Mux C → ADC | D21 [28] | PC4 (A6) | " |
| TRS MIDI in | D14 [15] | PB7 USART1_RX | |
| **TRS MIDI out** (optional, free here) | D13 [14] | PB6 USART1_TX | |
| USB-MIDI device | on-module USB | OTG FS (internal) | 0 header pins |
| Gate out | D26 [33] | PD11 GPIO | |
| Status LED red / green | D27 [34] / D5 [6] | PG9 / PD2 | |
| "Not in control" LED | D19 [26] | PA6 | |
| LM386 enable | D22 [29] | PA5 | 3.3 V-only, output |
| Sensor-LDO P-FET enable | D23 [30] | PA4 | 3.3 V-only, output; **defined low at reset (no expander)** |
| Audio in/out | pins 16–19, AGND 20 | on-module codec | 0 GPIO |
| FX controls (8), 25 Halls, Pico-read pots, stick, VEL toggle | mux channels | — | ≈ 45 of 48, unchanged |
| **Spare** | **D11, D12** (I2C1, for a future MCP4728 or OLED), **D17** (A2: a dedicated VCA-null sense ADC, or spare), **D29, D30** (USB-HS D−/D+; free if no second USB) | | **5 spare** |

**Used: 26 of 31. It fits, with no external part.**

**Option:** use the Seed's two **12-bit DC DAC outputs (D22, D23)** for VCA balance and velocity instead of PWM. That removes PWM ripple. LM386/LDO enable then move to D11/D12, leaving 3 spare. Noise of the on-chip DAC is UNVERIFIED, so keep PWM as the default.

**Frequency counter check [CALC]:**
- At a 200 MHz timer clock, a 20 kHz VCO gives 10,000 counts per period. With the capture prescaler at ÷8 that's 80,000 counts, ≈ 0.02 cents resolution.
- 10 Hz gives 20 M counts per period. The 32-bit counter wraps at 21 s, so there's no overflow handling.
- Each channel captures into its own register, and DMA (via DMAMUX) can log every edge, so the CPU is out of the timing loop. **This is equivalent to the Pico's PIO reciprocal counter.** TIM5 DMA request availability is per the STM32H7 reference manual, not read this session (UNVERIFIED).
- Inputs need the same 100 k + clamp as today. Clamp to 3.3 V even though D16/D24/D25/D28 are 5 V-tolerant.

**Key scan check [ENG]:**
- A timer triggers the ADC (3 channels in scan, DMA to RAM), and a second DMA stream steps S0–S3 through port C's BSRR on the same timer.
- 48 mux positions × 4 kHz ≈ 192 k conversions/s over 3 ADC channels: well inside the H750's ADC.
- This is the same hardware-paced design as `single-chip-research.md` §1.4, ported from PIO to timer + DMA. **Porting effort: about 1 weekend for scan + counters + PWM (ESTIMATE).**

**Logic levels:** the Seed is 3.3 V logic, like the Pico, so CD4067/MCP4822/6N138 interfacing is unchanged.

---

## 2. Pico 2 + SGTL5000 shield + 74HC595 pin check

### 2.1 Allocation (Pico 2 header: GP0–22, GP26–28 = 26 GPIO)
RP2350 function-select facts: UART0 RX on GP1; I2C0 on GP8/9; SPI0 on GP17–19; GPOUT0 on GP21 (GPOUT1–3 are GP23–25, which aren't on the Pico 2 header); ADC on GP26–28. These are well-known RP2350 mappings, not re-read this session (UNVERIFIED).

| GP | Use | GP | Use |
|---|---|---|---|
| 0 | I2S DIN (from codec, PIO) | 14 | I2S BCLK (PIO side-set) |
| 1 | UART0 RX: MIDI in | 15 | I2S LRCLK (side-set, must be consecutive with BCLK) |
| 2–4 | VCO 1–3 count (PIO) | 16 | 74HC595 latch (RCLK) |
| 5 | PWM: VCA balance | 17 | SPI0 CS: DAC 1 |
| 6 | PWM: mod depth | 18 | SPI0 SCK (+ 595 SRCLK) |
| 7 | PWM: velocity | 19 | SPI0 TX (+ 595 SER) |
| 8 / 9 | I2C0 SDA / SCL: SGTL5000 control | 20 | DAC 2 CS |
| 10–13 | CD4067 S0–S3 | 21 | **GPOUT0 → SGTL5000 MCLK** (12.288 MHz = 147.456 MHz / 12, integer) |
| 26–28 | ADC: mux A/B/C | 22 | I2S DOUT (to codec) |

**74HC595 outputs:** Q0 gate, Q1/Q2 status LED R/G, Q3 not-in-control LED, Q4 LM386 enable, Q5 sensor-LDO enable, Q6–Q7 spare.

**Total: 26 of 26. It fits with 0 spare,** confirming `single-chip-research.md` §1.6.

### 2.2 Hazards in the Pico plan
1. **595 power-up state.** The 595's output register comes up random. Q5 (sensor-LDO P-FET) could switch the 150–250 mA sensor load on at power-up, which is exactly the boost-stall case `budget-variant.md` §v1.6 sequences against.
   - The fix without a pin: an RC on /OE (≈ 100 k / 1 µF, ≈ 100 ms) holding the outputs Hi-Z, with pull-ups/pull-downs setting safe states, and firmware loading the 595 before the RC times out.
   - That needs the Pico 2 boot-to-main time to come in under ≈ 50 ms (UNVERIFIED; measure it in the §6 spike).
2. **SGTL5000 PLL mode forces the codec to be I2S master** (datasheet p. 32). Either feed a synchronous MCLK (256 × fs) from GPOUT0, as above, or run the PIO as I2S slave.
3. **RP2350 A2 erratum E9** (internal pull-downs latch; noted for the Pico Plus 2 in `single-chip-research.md` §1.3). Use external resistors on the count and MIDI inputs. Whether current Pico 2 stock has the fix is UNVERIFIED.

### 2.3 What doesn't fit on the Pico
- **Filter-scale cal count input (4th counter): no pin.** Workaround [ENG]: wire-OR the filter comparator and VCO 3's square into GP4 through two open-collector stages enabled by 595 Q6/Q7. During filter cal, VCO 3 is gated off.
- **TRS MIDI out: no pin.** The 595 can't run a UART. To get it: the Pico Plus 2's extra GPIO (which pins are UNVERIFIED), or swap the SGTL5000 for PCM1808 + PCM5102A, which has no I2C and frees GP8/GP9.
- **No spare for anything added at schematic capture.**

---

## 3. Audio quality (the owner's priority)

### 3.1 Converter datasheet figures

| | **SGTL5000** (Teensy shield Rev D) | **PCM3060** (Rev 7, Seed2 DFM) | **TAC5242** (Seed3) |
|---|---|---|---|
| Source | [NXP datasheet (PJRC copy)](https://pjrc.com/teensy/SGTL5000.pdf) | [TI datasheet](https://www.ti.com/lit/gpn/PCM3060) | [TI datasheet](https://ti.com/lit/gpn/TAC5242) |
| ADC SNR / DR | **85 dB** at 1.8 V; **90 dB** at 3.3 V (−60 dB input) (pp. 7–8) | **99 dB** typ (95 min), A-wtd, 48 kHz (p. 4) | **110 dB** single-ended; 119 dB differential (A-wtd, 3.3 V) |
| ADC THD+N | **−72 dB** at 3.3 V (p. 8) | **−93 dB** (p. 4) | **−98 dB** (differential, −1 dBFS) |
| DAC SNR / DR (line out) | **100 dB** at 3.3 V, 95 dB at 1.8 V (pp. 7–8) | **103–104 dB** single-ended (p. 5) | **111 dB** single-ended; 120 dB differential |
| DAC THD+N | **−85 dB** (pp. 7–8) | **−93 dB** single-ended (p. 5) | **−96 dB** single-ended |
| Line-in full scale | 2.83 Vpp at 3.3 V VDDA; 1.60 Vpp at 1.8 V (p. 6); 29 kΩ | 0.6·VCC = 3 Vpp at 5 V | 1 Vrms single-ended (≈ 2.83 Vpp) |
| Line-out full scale | 2.61 Vpp at 3.3 V; 320 Ω out, ≥ 10 kΩ load (p. 6) | 0.8·VCC = 4 Vpp single-ended | 1 Vrms single-ended |
| Word length / rates | 16/20/24/32-bit I2S; 8–96 kHz; **48 kHz supported** (pp. 12–13, 32) | 16/24-bit; ADC 16–96 kHz, DAC to 192 kHz | 24/32-bit; 8–192 kHz |

**Notes:**
- **Seed board-level figures:** the Seed's audio pins are single-ended, so the single-ended columns apply.
  - The "−120 dB" in an Electrosmith email matches the TAC5242's *differential* figure, not what the Seed pins will deliver (UNVERIFIED).
  - A Seed3 user measured a "lower noise floor" than the old Seed (PedalPCB thread, Jul 29 2026).
  - The older Seed datasheet gives AC-coupled inputs, 3.6 Vpp (≈ 1 Vrms) full scale, ≈ 30 kΩ in, ≈ 100 Ω line out (datasheet v1.0.5, pre-Seed3).
- **SGTL5000 VDDA on the PJRC shield** (1.8 V or 3.3 V) is UNVERIFIED. The difference is 5 dB on the ADC. PJRC states only "16 bit, 44.1 kHz … CD quality" ([PJRC](https://www.pjrc.com/store/teensy3_audio.html)).
- **The SGTL5000's headphone output uses a virtual ground** (its HP_VGND pin). Don't tie it to system ground; use LINE OUT only. PJRC does warn about this, but the page wasn't re-read this session (UNVERIFIED).
- **Earlier Seeds:** WM8731 (Rev 5), with forum reports of a ≈ 13 dB higher noise floor (thread title only, UNVERIFIED); AK4556 (Rev 4). Avoid used Rev 5 boards.

### 3.2 What it means for this synth (wet path only; dry stays analog) [CALC + ESTIMATE]
**ADC → DSP → DAC chain noise** (power sum, 3.3 V supplies, single-ended):

| Codec | Chain noise re full scale |
|---|---|
| SGTL5000 | **−89.6 dB** (−85 dB if VDDA is 1.8 V) |
| PCM3060 | **−97.5 dB** |
| TAC5242 | **−107.5 dB** |

**Referred to the dry signal's peak:**
- Scale the synth so its hottest patch (full EMPHASIS, overdriven mixer) peaks at −6 dBFS.
- The wet return is at −6 dB.
- **Worst case:** TAPE repeats near runaway, where noise recirculates at a gain of 1/(1−g²): +7 dB at g = 0.9, +12 dB at g = 0.97. Add a long HALL tail on top: ≈ +10 dB.

| Codec | Typical | Worst case |
|---|---|---|
| SGTL5000 | **−90 dB** | **−80 dB** |
| PCM3060 | **−98 dB** | **−88 dB** |
| TAC5242 | **−108 dB** | **−98 dB** |

**Against the analog voice's own floor** (≈ −80 to −90 dB re peak; ESTIMATE, not measured):
- **SGTL5000:** in the worst case it sits *at* the voice's own hiss, so tails in quiet passages get audibly noisier (≈ +3 dB of hiss). Its −72 dB ADC THD is inaudible under a reverb but is the weakest link for a CLEAN echo.
- **PCM3060:** sits 8–18 dB under the voice's hiss. Inaudible.
- **TAC5242:** sits 18–28 dB under. Inaudible.

**Mitigation on either platform [ENG]: a gate-aware input mute.** The MCU knows when the VCA is closed, so it can ramp the FX *input* to zero between notes while tails ring on. No new ADC noise enters during silence. This narrows, but doesn't close, the SGTL5000 gap during held notes.

**Analog interface (same for both):**
- One TL072 stage sets the level to ≈ −6 dBFS peak at the codec's full scale (2.6–3 Vpp), with soft diode clipping ahead of the ADC.
- The delta-sigma ADCs need only a simple RC anti-alias filter. Add an RC after the DAC to strip out-of-band noise before the output mixer and LM386.
- TL072 noise (≈ 18 nV/√Hz → ≈ 2.5 µV in band) is ≈ 25 dB below even the SGTL5000's ≈ 56 µV floor [CALC], so it's not a factor.
- On the Daisy, return the codec's AGND (pin 20) to the analog star point. The shield has only one GND.
- **Keep the dry path analog and never switched** (`single-chip-research.md` §5.1). It costs nothing and removes latency and converter colour from the dry sound on both platforms.

### 3.3 Processing headroom: float on both
- **Both use 32-bit float in the DSP:**
  - The RP2350's M33 has a single-precision FPU.
  - The H750's M7 has a double-precision FPU, but float32 is the norm in DaisySP.
- Float32 gives a 24-bit mantissa (≈ 144 dB per operation) and an 8-bit exponent, so neither will clip internally. Fixed vs float is **not** a difference between A and B.
- **The real difference is storage:**
  - Pico RAM forces **16-bit delay-line storage** (`single-chip-research.md` §1.3). That's a −96 dBFS quantisation floor per pass, under the SGTL5000's own floor, so it's acceptable with that codec. In recirculating reverb tanks it adds a little noise per pass. Mutable's 16-bit-storage reverbs show it can sound good [ENG].
  - The Daisy can store everything as float.
  - Paired with a 107 dB TAC5242, 16-bit storage *would* become the limit. That's another reason the better codec only pays off with Daisy-class RAM.

### 3.4 CPU and memory for top-quality algorithms (48 kHz, float32) [ESTIMATE]
Budgets:
- **Pico core 1:** 3,125 cycles/sample at 150 MHz, ≈ 2–3 cycles per multiply-accumulate.
- **Daisy:** 8,333 cycles/sample at 400 MHz (10,000 at 480). The M7 is dual-issue, so ≈ 1–1.5 cycles per multiply-accumulate with buffers in SRAM/TCM.

| Algorithm (quality version) | Work per sample (stereo out) | Working memory | **Pico core 1** | **Daisy** |
|---|---|---|---|---|
| Tape echo (cubic read, wow/flutter, saturation, filters) | ≈ 150–250 cyc (Pico) | 4 s float = 768 KB; 16-bit = 384 KB | 5–8 %; **≈ 3.8 s max** at 16-bit | ≈ 1–2 %; **minutes** (SDRAM) |
| Multi-head tape (RE-201-style, 3 heads + spring) | ≈ 400–600 | ≈ 1 s × 3 heads share one buffer | 13–19 %, fits | ≈ 3 % |
| Dattorro plate | ≈ 300–450 | ≈ 36 k samples: 72 KB (16-bit) / 144 KB (float) | 10–15 %, fits at 16-bit | ≈ 2–3 %, float |
| FDN hall, 8 lines | ≈ 400–600 | ≈ 0.75–1.5 s total: 72–144 KB (16-bit) | 13–19 %, fits at 16-bit | ≈ 3–4 % |
| **Long hall: FDN-16, long predelay, stereo, float** | ≈ 1,200–1,800 | ≈ 1.5 s + 0.5 s predelay ≈ 380 KB float | **38–58 %, and RAM doesn't fit next to an echo** | ≈ 8–12 % |
| **CloudSeed-class** (8 late lines, 6-stage modulated diffusers per line, 30-tap multitap, stereo) | ≈ 3,000–4,000 ops → 7–10 k cyc (Pico) / 3.5–5 k (Daisy) | ≈ 1–3 MB float | **≈ 220–330 %: doesn't run, doesn't fit** | **≈ 40–60 %: runs, with buffers in SDRAM; full-size presets may not** |
| Shimmer (plate + 2-grain pitch shift) | ≈ 550–750 | + ≈ 40 KB | 18–24 % | ≈ 4 % |
| Long looper / reverse / freeze echo (> 10 s) | small | ≥ 1.9 MB | **no** | yes |

**Reading:**
- **What the Pico can do well:** its four planned types (TAPE/BBD/CLEAN + PLATE/HALL/SPRING/SHIMMER at single-hall size), at 16-bit storage, with ≈ 3.8 s of echo.
- **What it can't do:** a lush long hall in float, CloudSeed, long or multi-feature tape delays, or several of these at once.
- **What the Daisy can do:** all of them, with headroom left for running echo + big reverb + modulation at the same time.

**Daisy caveats:**
- The H750 has **128 KB of internal flash**. A large program runs from QSPI (XIP) or is copied to the 512 KB AXI SRAM by the Daisy bootloader, which takes RAM from the reverbs. Plan reverb buffers in D2 SRAM and SDRAM accordingly [ENG].
- Random access to SDRAM is slower than SRAM. Keep the dense reverb taps in SRAM and long linear buffers in SDRAM.

### 3.5 Does a Pimoroni Pico Plus 2 (8 MB PSRAM) close the gap? [ENG/ESTIMATE]
- **Echo length: yes.**
  - 8 MB ≈ 87 s at 16-bit (`single-chip-research.md` §1.3).
  - Echo access is sequential (1 write and ≈ 4 adjacent reads per sample, mostly in one cache line), so cache stalls stay at a few percent.
  - Block DMA of 32-sample chunks avoids the cache altogether.
- **Reverb quality: no.**
  - Assume QSPI PSRAM at ≈ 75 MHz (UNVERIFIED clock). An uncached random 32-bit read is command + address + wait + data ≈ 20+ clocks ≈ 0.3 µs.
  - A float hall/CloudSeed with ≈ 40–50 scattered taps per sample needs ≈ 2–2.4 M random accesses/s, which is ≈ 0.6–0.7 s of stall per second. That's on top of the 16 KB XIP cache shared with code.
  - So reverbs stay in the 520 KB SRAM, and the Pico's limits on reverb size and float storage remain.
- **CPU:** unchanged at 150 MHz. CloudSeed still doesn't run.
- **Converter:** unchanged (still the SGTL5000).

The Plus 2 also adds GPIO via its connectors (which pins: UNVERIFIED) and carries the E9 pull-down caveat.

---

## 4. Recommendation (audio weighted highest)

| Criterion | Weight | Pico 2 + SGTL5000 | Daisy Seed (Seed3 / Seed2 DFM) |
|---|---|---|---|
| Converter noise and distortion (wet) | **Highest** | 85–90 dB ADC, −72 dB THD: at the voice's floor in the worst case | 99–110 dB, −93 to −98 dB: inaudible |
| DSP and memory for "great models, several types" | **High** | Good plate/spring/small hall/tape at 16-bit, ≈ 3.8 s echo | Float everything, CloudSeed-class, long halls, minutes of echo |
| Pins | Medium | 26/26 with a 595; filter-cal counter and MIDI out don't fit; 595 power-up hazard | 26/31, no expander, 4th counter and MIDI out free |
| Cost | Medium | ≈ $15.55 + $0.50 | **$34.99 (≈ +$19)** |
| Power | Medium | ≈ +0.1–0.25 W | ≈ +0.4–0.8 W (ESTIMATE): runtime ≈ −10–20 % |
| Firmware | Low–medium | Control side as planned + audio core | Control drivers ported to timers/DMA (≈ 1 weekend); audio framework turnkey |
| Supply | Medium | Low risk | Seed3 in production since Jul 2026; prices rose Nov 1 |

**Pick: Daisy Seed as the single digital chip.**
- It is the better audio engine on every measured axis, and it removes the Pico plan's 0-spare pin squeeze and the 595 power-up hazard.
- **Buy a Seed3 or a 65 MB Seed2 DFM. Avoid used Rev 5 (WM8731) boards.**
- Keep the MCP4822s for pitch, and keep the dry path analog.

**Gate before layout:** re-aim the one-evening spike in `single-chip-research.md` §6 at the Daisy:
- TIM5 capture ×4 on a function generator;
- a timer + DMA CD4067 scan at 4 kHz/key;
- Dattorro + tape echo running;
- then measure codec output noise with the synth's level stage.

**If the owner won't take +$19 / +0.5 W:** stay on the Pico, but replace the SGTL5000 with **PCM1808 + PCM5102A**.
- **Converter:** PCM1808 ≈ 99 dB ADC and PCM5102A ≈ 112 dB DAC; the PCM1808 figure is UNVERIFIED this session, and the PCM5102A figure is Adafruit's listing as cited in `single-chip-research.md` §1.5. That's ≈ PCM3060-class.
- **Pins:** it frees GP8/GP9 for the filter counter and MIDI out.
- **What doesn't change:** DSP and memory limits are as in §3.4.
- **Sourcing:** the PCM1808 module is marketplace-only.
