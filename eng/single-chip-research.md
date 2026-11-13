# One chip for everything? Echo + reverb on the existing digital brain

Status: rev 0, 2026-11-13. Answers the owner: "Is there a single chip that could handle all of it?" Scope as updated during the research (owner, via orchestrator):
- "I want echo and reverb": reverb is now in scope.
- "Delay and verb can be digital": the voice stays analog, the effects may be fully digital. Analog-only effect routes are dropped unless they clearly win.
- "I would want great models tho — would be cool if digital could do more than one type": quality and several selectable types per effect are hard requirements.

Base documents: `effects.md` rev 0 (PT2399 / second Pico options), `budget-variant.md` rev 12, `velocity-and-keys-v2.md` §1 (GPIO note), `owner-requirements-budget.md`.
Conventions as in `budget-variant.md`: link = read this session. **ESTIMATE** = my number. **UNVERIFIED** = a source exists but I couldn't confirm the figure. [ENG] = engineering judgement. [CALC] = arithmetic.

---

## 0. Bottom line

**Yes. The Pico 2 already in the design can run echo and reverb on its second core, using one ready-made converter module. No second MCU and no PT2399 are needed.**

- **Hardware added:** one **Teensy Audio Shield Rev D (SGTL5000 codec, line in, line out and headphone out, $9.80, in stock at SparkFun)**. It is used purely as an I2S codec module; it doesn't need a Teensy. Add one 74HC595 (DIP) to free GPIO, plus a TL072 for levels. **≈ $21–25 including 5 pots, 2 rotary switches and a TAP button.** That compares with $28–35 for the second Pico (`effects.md` (c)) and $10–14 for the PT2399 echo, which has no reverb.
- **Power:** ≈ +0.1–0.25 W (ESTIMATE). Half of `effects.md` (c)'s figure.
- **What it runs:** core 0 keeps every current job: key scan, MIDI, DACs, PWM CVs, autotune. **Core 1 runs only audio**: one echo (TAPE / BBD / CLEAN types) and one reverb (PLATE / HALL / SPRING / SHIMMER types) together at 48 kHz in single-precision float. Estimated load ≈ 20–40 % of core 1 (§1.2).
- **The binding limit is RAM, not CPU.** With a reverb resident, the 520 KB SRAM leaves room for **≈ 3.5–3.9 s of echo at 48 kHz / 16-bit** (≈ 5.5 s at 32 kHz). If that ever isn't enough, the **Pimoroni Pico Plus 2** (same footprint, RP2350B, 8 MB PSRAM) drops into the same socket and lifts the echo to minutes.
- **Firmware effort is moderate, not huge.** The best open effect code (DaisySP, Mutable Instruments, hexefx, CloudSeed) is portable C/C++ under MIT-style licences, so it is not locked to Daisy or Teensy (§3).
- **The runner-up "single chip" is the Daisy Seed**, with 10× the headroom and a 24-bit codec on board. It would replace the Pico outright. It's out for v1: ≈ +$19, ≈ +0.3–0.6 W, a 2026 production pause, and every control-side driver would have to be redone on STM32. **Use it as the fallback if the §6 spike fails.**

**Gate before the board order (§6):** a 1-evening breadboard spike: Pico 2 + SGTL5000 shield running plate reverb + tape echo on core 1 while core 0 runs a dummy 100 ksps mux scan and PIO counters. Pass = core 1 < 60 %, zero I2S underruns, key-scan timing jitter < 2 µs.

---

## 1. Can the existing RP2350 do it? (question 1)

### 1.1 What the chip has
- **Two Cortex-M33 cores at 150 MHz, 520 KB SRAM in ten independent banks, three PIO blocks with 12 state machines, 30 GPIO (QFN-60) or 48 (QFN-80), 4 or 8 ADC inputs** ([RP2350 product brief](https://pip-assets.raspberrypi.com/categories/1214-rp2350/documents/RP-008374-DS-1-rp2350-product-brief.pdf)).
- The M33 has a **single-precision FPU and DSP extensions** ([Arm](https://newsroom.arm.com/blog/raspberry-pi-pico-2-arm-cortex-m33)). This matters: the old Pico (RP2040) had no FPU, and DIY effects on it had to go fixed-point because a float EQ "couldn't keep up" ([101 Things guitar-effects project](https://101-things.readthedocs.io/en/latest/guitar_effects.html), which still ran delay, echo and an FDN reverb on an RP2040).
- External QSPI PSRAM is supported (up to 16 MB on a second chip-select, per the brief).
- DMA channel count: not in the brief. 16 per the RP2350 datasheet (UNVERIFIED this session).

### 1.2 CPU budget [ESTIMATE, from typical op counts of the algorithms]
Core 1 at 150 MHz = 3,125 cycles per sample at 48 kHz. Assume ≈ 2–3 cycles per float multiply-accumulate including loads, plus overhead.

| Block (mono in, mono or stereo out) | ≈ cycles/sample | % of core 1 |
|---|---|---|
| I2S via PIO + DMA, 32-sample double buffers (one interrupt per 0.67 ms, not per sample) | ≈ 20 | < 1 % |
| Tape echo: fractional (cubic) read head with wow/flutter LFOs, tanh-style saturation, loop LPF/HPF, noise | ≈ 150–250 | 5–8 % |
| Dattorro plate (≈ 12 allpasses/delays, 2 modulated, ≈ 14 output taps) | ≈ 300–450 | 10–15 % |
| 8-line FDN hall with modulation and damping (Hadamard mix) | ≈ 400–600 | 13–19 % |
| Spring emulation (allpass chirp cascade + dispersion, hexefx-style) | ≈ 300–500 | 10–16 % |
| Shimmer = plate + 2-grain octave-up pitch shifter in the loop | ≈ 550–750 | 18–24 % |
| Control smoothing, tempo/MIDI clock, parameter mapping | ≈ 50 | 2 % |
| **Worst case: tape echo + shimmer** | **≈ 800–1,100** | **≈ 25–35 %** |

Only one reverb type runs at a time, so the worst case is echo + shimmer: **≈ 2–3× headroom**. The M33 FPU on the RP2350 has no double precision, so state must stay in float, with denormal flushing. All of this is ESTIMATE until the §6 spike measures it.

### 1.3 RAM budget [CALC]
| Use | Size |
|---|---|
| Firmware data, stacks, key/velocity buffers, MIDI, I2S DMA buffers | ≈ 40–60 KB (ESTIMATE) |
| Reverb working memory: Dattorro tank ≈ 0.75 s of total delay ≈ 36 k samples at 48 kHz → 72 KB at 16-bit storage (144 KB float); FDN hall or spring similar | **≈ 75–110 KB** (mixed 16-bit storage, float state) |
| **Left for echo** | **≈ 350–400 KB** |

Echo length from that remainder:

| Format | Bytes/s | Seconds in 360 KB |
|---|---|---|
| 48 kHz, 16-bit mono | 96,000 | **≈ 3.8 s** |
| 32 kHz, 16-bit mono | 64,000 | ≈ 5.6 s |
| 48 kHz, 12-bit packed | 72,000 | ≈ 5.0 s |
| 32 kHz, 12-bit packed (tape type only; it's band-limited anyway) | 48,000 | ≈ 7.5 s |

3.8 s covers a dotted half note at 60 BPM. Long enough for an echo instrument [ENG].

**PSRAM upgrade:** the [Pimoroni Pico Plus 2](https://shop.pimoroni.com/en-us/products/pimoroni-pico-plus-2) is RP2350B with 16 MB flash and **8 MB PSRAM**, keeps "the original Pico footprint", and is "compatible with Raspberry Pi Pico add-ons" ([Core Electronics](https://core-electronics.com.au/pimoroni-pico-plus-2-rp2350-dev-board-usb-c-16mb-flash-8mb-psram.html.plain.md) confirms RP2350B, 8 MB).
- 8 MB holds ≈ 87 s at 48 kHz/16-bit [CALC].
- Put the **echo** in PSRAM, because its reads and writes are sequential and cache-friendly. Keep the **reverb in SRAM**: it makes ≈ 20–30 scattered taps per sample, which would thrash the XIP cache [ENG].
- **Caveats:**
  - US price not shown. Core Electronics lists AU$29.64 ex GST, out of stock (≈ US$19, UNVERIFIED).
  - Pimoroni's note says current stock uses the **A2 RP2350 with erratum E9**: internal pull-downs latch, so use external pull-downs of ≤ 8.2 kΩ.
  - USB-C, not micro-USB, which is fine.
  - It is a socket-compatible option for later, not a v1 need.

### 1.4 Real-time interaction with existing duties [ENG]
- **Autotune frequency counting** is a **PIO reciprocal counter** (`budget-variant.md` Part 2 §4). PIO runs in hardware, independent of CPU interrupts, so the audio core can't disturb it. Counters use 3 SMs and I2S uses 1, out of 12.
- **Key scan (25 Halls at ≥ 4 kHz/key ≈ 100 ksps + pots):** this stays on core 0. Pace it from a PIO or timer that drives the mux selects, with the ADC drained by DMA, so its timing doesn't depend on interrupt latency. Core 1 takes **no** interrupts except its own DMA-complete. Give core 0's scan DMA the higher bus priority.
  - SRAM is in 10 banks: put each core's stack and hot buffers in separate banks (the SDK's scratch X/Y banks), so contention is negligible.
  - Expected scan jitter effect: **sub-µs**, against a 250 µs per-key period.
- **MIDI:** UART RX FIFO + USB (TinyUSB) on core 0, unaffected.
- **Clocking:** clean I2S wants an integer relationship between the system clock and fs. Either set sys_clk to an audio-friendly value (e.g. 147.456 MHz = 3072 × 48 kHz, inside spec), or use the SGTL5000's own PLL from a 12 MHz MCLK. PWM-CV carrier frequencies and UART baud just get recomputed. Avoid fractional PIO dividers for BCLK: they add jitter ([artemis.sh bidirectional PIO I2S](https://artemis.sh/2026/03/22/pio-i2s-bidirectional.html), which runs full-duplex I2S on one SM with 4 pins at a 150 MHz sysclk).
- **Latency:** in+out buffering ≈ 2–3 ms. That's irrelevant here, because only the wet path is digital and the dry path stays analog (§4).
- **Noise:** core 1 activity adds supply current pulses on the same Pico. Same ground rules as today (`little-d-design-answers.md` "Digital noise"): codec module ≥ 30 mm from the ladder and expos, its own analog ground return to the star point.

### 1.5 Converter module options (all ready-made, through-hole headers)
| Module | In / out | Pins from Pico | Price (US, qty 1) | Notes |
|---|---|---|---|---|
| **Teensy Audio Shield Rev D, SGTL5000 (pick)** | Stereo line in, stereo line out, headphone amp | **7**: MCLK, BCLK, LRCLK, TX, RX, SDA, SCL ([PJRC](https://www.pjrc.com/store/teensy3_audio.html)) | **$9.80, in stock** ([SparkFun DEV-15845](https://www.sparkfun.com/teensy-4-audio-shield-rev-d.html)) | One module covers ADC and DAC. SparkFun lists "16-bit, 44.1kHz". The chip runs 48 kHz too (UNVERIFIED this session). Pico use isn't documented by PJRC, but the bus is standard I2S + I2C [ENG]. MCLK from an RP2350 GPOUT clock pin or PIO |
| Adafruit PCM5102 #6250 (DAC) + generic PCM1808 (ADC) | Line out 112 dB SNR / 24-bit in | 5: BCLK, LRCLK, DOUT, DIN, MCLK (no I2C) | $6.45 ea in 2s at [Jameco](https://www.jameco.com/z/6250-Adafruit-Industries-Adafruit-PCM5102-I2S-DAC-with-Line-Level-Output-112dB-SNR_2884135.html) + PCM1808 ≈ $5–8 ESTIMATE (marketplace only, `effects.md`) | Better DAC spec, 2 fewer pins, but two modules and no reliable US PCM1808 source |
| Pimoroni Pico Audio Pack (PCM5100A) | Out only | — | [PiShop](https://www.pishop.us/product/pico-audio-pack-line-out-and-headphone-amp/), price not read | No input, so it can't process the synth. Out |
| WM8960 breakout | — | — | Retired at SparkFun (`effects.md`) | Out |
| RP2350 internal ADC + PWM out | — | 0–1 | $0 | Lo-fi (12-bit ADC, PWM DAC). Fails "great models" [ENG] |

### 1.6 Pin count [reconstruction, UNVERIFIED: the v1 GPIO tally was never redone, `velocity-and-keys-v2.md` §1]
Pico 2 header GPIO: 26 (GP0–22, GP26–28).

| Use | Pins |
|---|---|
| SPI to 2× MCP4822 (SCK, MOSI, CS1, CS2) | 4 |
| CD4067 select S0–S3 | 4 |
| Mux outputs → ADC (GP26–28) | 3 |
| VCO 1–3 count inputs (PIO) | 3 |
| PWM CVs: VCA balance, mod depth (AS3360 A), velocity (AS3360 B) | 3 |
| Gate out, MIDI RX, LEDs ×2, LM386 enable, sensor-LDO P-FET | 6 |
| **Total ≈ 23 → ≈ 3 spare** | |

**The SGTL5000 needs 7.** Fix with a **74HC595 (DIP-16, ≈ $0.50)** on the existing SPI bus plus one latch pin. Move the 2 LEDs, LM386 enable, LDO enable and gate out onto it. That frees 5 and costs 1, so spare goes **3 → 7, exactly enough.** The gate takes a ≈ 2 µs SPI write: no audible timing cost [ENG].
- With PCM5102A + PCM1808 (5 pins), 2 spare remain.
- New effect pots, type switches and TAP go on **existing CD4067 channels** (≈ 37 of 48 used → ≈ 45 of 48 after §5): **no GPIO.**
- MIDI clock for sync is already parsed on core 0, so **sync costs no pins.**
- *Tightness flag:* zero spare GPIO with the SGTL5000. If the recount at schematic capture comes out worse, use PCM5102A + PCM1808, or the Pico Plus 2 (its Qw/ST and SP/CE connectors carry extra GPIO; which GPIO is UNVERIFIED).

---

## 2. Alternative single-chip platforms (question 2)

**Our I/O needs** (from §1.6 and `budget-variant.md` §v1.2):
- ≈ 3 ADC inputs (muxed to ≈ 48 channels);
- 4 pitch-grade CV channels (VCO 1–3 + filter): 12-bit, autotune-corrected;
- 3 PWM CVs;
- 3 frequency-count inputs;
- SPI;
- gate;
- UART MIDI in + USB device MIDI;
- ≈ 6 misc digital;
- full-duplex audio.

| | **Pico 2 + SGTL5000 shield (pick)** | Pimoroni Pico Plus 2 + shield | **Daisy Seed (runner-up)** | Teensy 4.1 + Audio Shield | ESP32-S3 module + codec |
|---|---|---|---|---|---|
| Price (US qty 1) | $5.75 + $9.80 = **$15.55** | ≈ $19 (UNVERIFIED) + $9.80 ≈ $29 | **$34.99** for 65 MB from Nov 1 2026 ([PedalPCB tracker post, Oct 26 2026](https://forum.pedalpcb.com/threads/free-stock-price-tracker-for-daisy-seeds-heads-up-prices-change-nov-1.30660/latest)) | $31.50 ([SparkFun](https://www.sparkfun.com/teensy-4-1.html)) + $9.80 = **$41.30** | ≈ $15 dev board (ESTIMATE) + codec ≈ $10 |
| CPU | 2× M33 150 MHz, SP FPU | same | M7 **480 MHz**, FPU ([Thonk](https://www.thonk.co.uk/shop/electrosmith-daisy-seed)) | M7 **600 MHz** | 2× LX7 240 MHz (ESTIMATE) |
| Audio RAM | 520 KB (≈ 3.8 s echo + reverb) | + **8 MB PSRAM** | **64 MB SDRAM** | 1 MB; PSRAM pads need SMD soldering (breaks our rule) | 512 KB + PSRAM on N8R8 modules |
| Codec | SGTL5000, 16-bit class | same | **On board, 24-bit/96 kHz stereo**, AC-coupled (Thonk) | SGTL5000 | external |
| Built-in DACs for CVs | none (keep 2× MCP4822) | none | **2 × 12-bit DC-coupled**: could replace only one MCP4822, and the DAC sits inside a noisy MCU (noise UNVERIFIED). Keep the MCP4822s | none | none on S3 |
| ADC | 3 usable, 12-bit | 3 on header | **12 × 16-bit** | 18 analog | noisy, nonlinear: poor for Hall velocity [ENG] |
| GPIO | 26 (tight, §1.6) | 26 + connectors | 31 | 55 | ≈ 30+ |
| Frequency counting | PIO (ideal) | PIO | timer input capture (pin mapping UNVERIFIED) | timers/FlexPWM | PCNT |
| Power (5 V) | Pico ≈ 0.1–0.25 W (`effects.md`) + shield ≈ 0.05–0.1 W (UNVERIFIED) | +PSRAM ≈ small | **≈ 0.4–0.8 W ESTIMATE** (no official figure found) | ≈ 100 mA at 600 MHz ≈ 0.5 W (SparkFun) + shield | ≈ 0.2–0.5 W without radio (ESTIMATE) |
| Ecosystem for synth control | Pico SDK, TinyUSB, PIO: the design is built around it | same | libDaisy, USB MIDI, DaisySP | Teensy Audio Library, USB MIDI built in | ESP-IDF; little synth-control precedent |
| Firmware effort | Control firmware as planned + audio core | same | Re-do control drivers on STM32 (key-scan DMA, counters, PWM), but audio is turnkey | Re-do control drivers; audio graph is turnkey | Highest |
| Supply risk | Low | Medium (out of stock at Core Electronics) | **Medium–high**: production halt reported in 2026 ([PedalPCB PSA](https://forum.pedalpcb.com/posts/385746/)); price rises | Low–medium | Low |
| Through-hole fit | Socketed module | same | Pre-soldered headers | Headers | Headers |

**Reading:**
- **Daisy** is the strongest audio engine: unlimited RAM, a better codec, a framework designed for exactly this.
  - Against it for *this* instrument: it costs ≈ $19 more than Pico + shield and roughly 2–4× the power (runtime ≈ −10–20 % on the 22.2 Wh pack [CALC against 2.0–3.6 W]).
  - The 2026 supply history threatens a one-unit "no rev 2" build.
  - Its 2 DACs don't remove the MCP4822s.
- **Teensy 4.1:** more headroom than the RP2350 and a mature audio library, but 1 MB RAM without SMD PSRAM, and $41 plus the same driver port. No advantage over Daisy for audio or over the Pico for control.
- **ESP32-S3:** weak ADC for velocity, no PIO, least synth precedent. Out.

### Ready-made effect chips (re-ranked for echo + reverb, multiple types)
| | Echo | Reverb | Types | Verdict |
|---|---|---|---|---|
| **Spin FV-1** ($20 pre-soldered + $1 adapter, `effects.md`) | ≤ ≈ 1 s (UNVERIFIED) | Decent classic algorithms | 8 programs per EEPROM. 128 instructions per sample limits tape modelling and shimmer quality [ENG] | Out: fails "great models", adds an EEPROM and a crystal |
| **Accutronics/Belton BTDR-2** digital reverb brick | none | One fixed algorithm, 2.5–2.85 s decay, 5 V, 60 mA typ / 100 mA max, needs only in/out/+5 V/GND ([Amplified Parts](https://www.amplifiedparts.com/products/P-RBTDR-2V-L)) | 1 | Out: one type, no echo, ≈ 0.3 W |
| Spring tank + driver (analog) | — | Real spring | 1 | Out: tank depth (≥ 25 mm class) doesn't fit a 30–36 mm body, it's microphonic in a portable, and the owner allows digital |
| PT2399 | ≈ 0.35–0.6 s | none | 1 | Out (see §4) |

---

## 3. "Great models": the code exists and is portable (firmware effort)

| Library | Licence | Useful content | Platform lock |
|---|---|---|---|
| **DaisySP** (Electrosmith) | MIT per repo README (UNVERIFIED this session) | DelayLine, Tone/SVF filters, oscillators for modulation, pitch shifter, overdrive | Plain C++, no HAL. **Compiles for the RP2350** [ENG] |
| **DaisySP-LGPL** | **LGPL-2.1**: users must be able to relink ([GitHub](https://github.com/electro-smith/DaisySP-LGPL)) | Csound-derived modules (ReverbSc lives here, per community usage; UNVERIFIED) | Avoid it, or ship the source. Fine for a one-unit personal build, but note it |
| **hexefx_audiolib_F32** | **MIT** ([GitHub](https://github.com/hexeguitar/hexefx_audiolib_F32)) | **Stereo plate reverb, spring reverb emulation, stereo ping-pong delay with modulation**, ReverbSc (optionally in PSRAM) | Wrapped in the Teensy Audio / OpenAudio framework, but the DSP cores are portable float C++ [ENG] |
| Teensy Audio Library | MIT (UNVERIFIED this session) | Freeverb, delay, chorus | Teensy-specific I/O |
| CloudSeed (Valdemar Erlingsson) / DaisyCloudSeed | MIT (UNVERIFIED) | Lush algorithmic hall | Heavier, likely too big for 520 KB with an echo. PSRAM variant is a later option |
| Mutable Instruments (Clouds/Rings/Elements reverb, Griesinger/Dattorro-style) | MIT (UNVERIFIED this session) | Compact, excellent-sounding 16-bit-storage reverb designed for 128 KB-class STM32F4s | Portable C++. **A good fit for the RP2350's RAM** |
| Dattorro 1997 paper | Published algorithm | Plate topology and delay lengths | Implement directly (≈ 200 lines) |

**Effort [ESTIMATE]:** ≈ 2–4 weekends of agent-assisted firmware for core 1:
- I2S/codec bring-up;
- port of the plate + spring + FDN hall + tape echo;
- type switching with crossfades;
- tap/MIDI sync;
- parameter smoothing.

That is about the same as the second-Pico plan in `effects.md`, minus the second program's own MIDI, ADC and boot plumbing. On Daisy the audio part would be ≈ 1–2 weekends, but the control side (key scan, counters, PWM CVs) would need porting off PIO. Net effort is about even, so it doesn't decide the choice.

---

## 4. PT2399 clocked by the Pico (question 3), now dropped
- **Feasibility.** Delay time is set by current out of pin 6 ([Electric Druid](https://electricdruid.net/?p=388)). The usual tap-tempo route replaces the TIME pot with a digital pot: the PTAP project used an MCP41050 ([DIYstompboxes](https://diystompboxes.com/smfforum/index.php?msg=648847)). Electric Druid's TAPTEMPO-family chips are another route.
- **How the Pico would do it.** It could do the same with a PWM-CV into a current sink and close the loop by counting the chip's clock on a PIO counter. Which pin to probe is UNVERIFIED: pedal forums cite the VCO pin. That gives MIDI-clock sync for ≈ $0.50 and 2 GPIO.
- **Why it's dropped.** It still gives only one echo flavour, ≈ 0.6 s maximum, and **no reverb**. The owner wants great models, several types and reverb, and has said the effects can be digital. **Not recommended.**

---

## 5. Recommended path and panel

### 5.1 Signal flow
```
VCA out ─┬──────────────────────────── dry (analog, never switched) ──► OUTPUT MIXER ─► VOLUME ─► LM386 / phones / line
         └► TL072 level/AA buffer ─► SGTL5000 LINE IN ─► [core 1: ECHO ─► REVERB] ─► SGTL5000 LINE OUT ─► TL072 ─┘ (wet sum)
```
- **Wet only.** Mix happens in DSP (ECHO MIX and REVERB MIX set wet levels). With both at zero the instrument is electrically today's. If the DAC is muted, nothing changes in the dry path.
- **Placement:** echo feeds reverb (series, the classic order). EXT audio in gets the effects too.
- **Stereo:** the SGTL5000 is stereo out. If the phones jack is wired TRS stereo, reverb and ping-pong can be stereo on phones while the speaker and line out get the mono sum. That's an optional extra jack wiring choice, not a new patch point.

### 5.2 Panel controls (constraint for design)
| Section | Control | Part | Read via |
|---|---|---|---|
| ECHO | **TYPE**: TAPE (wow/flutter, saturation, darkening repeats) / BBD (dark, short-range character, clock-noise-free) / CLEAN digital / PING-PONG (stereo phones; mono elsewhere = CLEAN with alternating tone) | 4-position rotary (Tayda RS16211 with stop, $1.21) on a resistor ladder | 1 mux channel |
| | **TIME** (free; or note division when synced) | 9 mm pot | mux |
| | **REPEATS** (to controlled runaway on TAPE) | 9 mm pot | mux |
| | **ECHO MIX** | 9 mm pot | mux |
| REVERB | **TYPE**: PLATE (Dattorro) / HALL (FDN) / SPRING / SHIMMER | 4-position rotary on a ladder | 1 mux channel |
| | **DECAY** (size and damping scaled together per type) | 9 mm pot | mux |
| | **REVERB MIX** | 9 mm pot | mux |
| Shared | **TAP** button. Hold + TIME = sync on/off; with MIDI clock present it follows clock | momentary, THT | mux channel (with pull-up) |

**Total: 5 pots + 2 four-way rotaries + 1 button = 8 mux channels, no GPIO.** Mux use ≈ 37 → ≈ 45 of 48.
- **Minimum version:** drop TAP (sync is automatic when MIDI clock is present) and merge the MIXes into one FX MIX. That gives 4 pots + 2 rotaries.
- **Not in v1:** a hidden TONE per effect (set by firmware per type).
- Consistent with "knob-only controls send no MIDI" and "MIDI never flips switches": the TYPE switches are read-only.

### 5.3 Cost, power, area
| Item | Cost |
|---|---|
| Teensy Audio Shield Rev D | $9.80 ([SparkFun](https://www.sparkfun.com/teensy-4-audio-shield-rev-d.html)) |
| Headers/socket for the shield | ≈ $1 (ESTIMATE) |
| 74HC595 DIP-16 + TL072 + passives | ≈ $1.50–2.50 (ESTIMATE) |
| 5 pots (A-5622 $0.59) + 5 knobs ($0.30) | $4.45 |
| 2 rotaries ($1.21) + knobs ($0.42) | $3.26 |
| TAP switch | ≈ $0.50 (ESTIMATE) |
| Board area ≈ 2.5–3 in² | ≈ $1.50–3.70 |
| **Total** | **≈ $22–25** |

- **Against the alternatives:** `effects.md` (a) PT2399 is $10–14 for echo only. (c) second Pico is $28–35 for echo only, before adding reverb.
- **Power [ESTIMATE]:** core 1 active ≈ +15–25 mA, SGTL5000 module ≈ 10–30 mA (UNVERIFIED), TL072 ≈ 5 mA on ±9 V. Total **≈ +0.1–0.25 W → runtime ≈ −3–11 %** on today's 2.0–3.6 W [CALC: P/(P+ΔP)].
- **Area [ESTIMATE]:** shield ≈ 35 × 31 mm (UNVERIFIED) ≈ 1,100 mm² + 74HC595/TL072/passives ≈ 600–800 mm² → **≈ 1,700–1,900 mm² of board**, about the same as the PT2399 block.
  - The shield on headers breaks the ≤ 6.5 mm top-side rule, so mount it on the **underside next to the Pico** (≤ 8 mm stack), as the Pico is.
  - FOLD: it lives with the Pico (base), not the lid, so it doesn't worsen the lid shortfall. Only 2 analog lines (send/return) cross the hinge, routed like VOLUME and guarded.

### 5.4 Trade-offs and risks
| Risk | L | Mitigation |
|---|---|---|
| RP2350 CPU or bus contention disturbs key-scan or I2S timing | L–M | §6 spike before the board order. Hardware-paced scan; core 1 isolated |
| Zero spare GPIO after the SGTL5000 | M | 74HC595 expander. PCM5102A + PCM1808 (5 pins) or Pico Plus 2 as fallbacks |
| 3.8 s echo cap | L | 32 kHz/12-bit TAPE mode ≈ 7 s. Pico Plus 2 PSRAM later, same socket |
| Codec/MCU digital noise into the analog voice | M | Underside placement, ≥ 30 mm keep-away, separate analog return, wet-only path |
| SGTL5000 shield not documented for Pico use | L | Standard I2S/I2C. Breadboard first (§6) |
| LGPL code pulled in by accident | L | Use MIT sources (§3) |
| "No rev 2": wrong platform choice | M | The spike decides between Pico + shield and a Daisy-centred board *before* layout |

---

## 6. Next action (one evening, ≈ $16 of parts that are reused in the build)
Buy a Pico 2 (or use a spare) and the Teensy Audio Shield Rev D. On a breadboard:
1. PIO I2S full duplex at 48 kHz, with MCLK from GPOUT.
2. Core 1: Dattorro plate + tape echo (hexefx/DaisySP/MI-derived), then shimmer.
3. Core 0: a dummy CD4067 scan at 100 ksps via DMA, 3 PIO counters on a function-generator square, and TinyUSB MIDI.
4. Measure:
   - core-1 cycle use (DWT cycle counter);
   - I2S underruns;
   - scan-period jitter (scope on S0);
   - counter readings vs. no-audio;
   - noise on the codec output.

**Pass → lock the Pico + shield path. Fail → re-plan around Daisy Seed as the single chip** (≈ +$19, ≈ +0.3–0.6 W, check stock first).
