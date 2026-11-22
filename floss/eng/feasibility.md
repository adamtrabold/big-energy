# floss: engineering feasibility gate (rev 0, 2026-11-22)

Status: **rev 0**, by the engineer, for Adam and the design team. Desk research and first-principles arithmetic only; nothing was built or measured. Inputs: `floss/REQUIREMENTS.md` (T1–T12), `floss/README.md`, `design/owner.md` (2026-11-21 onward), `eng/budget-variant.md`, `eng/battery.md`, `eng/aftertouch.md`, `eng/velocity-and-keys-v2.md`, `eng/key-sourcing.md`, the floss concepts (`floss/design/concepts/common-how-it-works.md`, `bow/`, `tide/`), CATHEDRAL (`design/branches/concepts/cathedral/how-it-works.md`) and HUSH (`design/concepts/hush/how-it-works.md`). The designers' part numbers are treated as placeholders.

**Marks:** **[chk]** checked against the linked source this session · **[plat]** taken from Big Energy's eng records (their own mark carries over: most of their power and cost figures are ESTIMATE) · **[calc]** my arithmetic from the numbers beside it · **[est]** my estimate, not checked.

---

## 1. Summary for Adam

### 1.1 Engines side by side

"Every key a voice" means each key has its own tone, its own envelope and its own amplitude control. Pressure is the shared strip in every row except B, because per-key pressure has no proven route with these keys (§1.2).

| Engine | What you get | Engine chips | Engine parts cost | One-unit total | Power (low / mid / high) | Runtime on BOW's base pack (11.1 Wh) | Runtime on 22.2 Wh (TIDE's bay) | Fits BOW? | Fits TIDE? |
|---|---|---|---|---|---|---|---|---|---|
| **A. Paraphonic** (one envelope, one VCA) | Every key sounds, octave per half, per-key drift. **One envelope:** velocity only on the first note of a phrase, every note releases together, pressure on everything | 16 | $23–30 | ≈ $395–675 | 1.5 / 2.4 / 3.2 W | 2.8 / 3.8 / 5.9 h | 5.5 / 7.7 / 11.9 h | Fits, but **it isn't BOW**: no per-note strike or lift | Fits, but **it isn't TIDE**: no per-note lifespan, and pulling a note out of HOLD clicks off |
| **B. Every key a voice + per-key pressure** | Everything in C, plus per-note swell, vibrato and drift by pressure, and BOW's thinning | — | **Blocked** | — | — | — | — | Only if floss gives up its own keys for a bought poly-pressure key surface (§3.3) | Same |
| **C1. Every key a voice, SSI2164 VCAs** | **Per-note velocity, per-note release (lift speed), per-note drift.** Pressure acts on the whole instrument | 16, SMD only | $67–78 | ≈ $440–725 | 2.2 / 3.7 / 5.1 W | 1.7 / 2.4 / 4.0 h ✗ | 3.3 / 4.7 / 8.1 h (borderline) | Board fits only double-sided SMD; **runtime fails** | ✓ |
| **C2. Same, LM13700 DIP OTAs** | Same as C1 | 15, DIP possible | $49–73 | ≈ $420–720 | 2.3 / 3.5 / 4.8 W | 1.8 / 2.5 / 3.9 h ✗ | 3.6 / 4.9 / 7.7 h (borderline) | **DIP doesn't fit** the base; runtime fails | SMD ✓; DIP is 16 % over HUSH's board |
| **D. Every key a voice, analog-switch keyers** (recommended) | Same as C1 | **12** | **$31–41** | ≈ $400–685 | **1.6 / 2.5 / 3.4 W** | 2.6 / 3.6 / 5.6 h ✗ (needs one more cell, §1.3) | **5.2 / 7.2 / 11.2 h ✓** | ✓ double-sided SMD (57 % margin; 20 % with strands) | ✓ (84 % margin) |

All figures are [calc] from [est] and [plat] inputs (§4, §7). Runtimes read worst / mid / best (high load, mid load, low load). "Mid" is the midpoint of the power range, standing in for T2's "moderate volume". The common part of every unit (Daisy, keys, strip, ensemble, battery, boards, case) is ≈ $370–645 [est]; the boards and their assembly are the biggest unknown, as on Big Energy.

**The finding that changes the picture:** floss needs **a tone generator per key** in every engine, because each half has its own octave and incoming MIDI notes can land on any key. Once each key has its own tone, giving it its own envelope costs **one more $12–15 microcontroller and about 0.1–0.2 W** (D against A). A also needs a de-click ramp on every key (or notes added under the shared envelope click), so it saves almost nothing in chips. **The classic paraphonic engine is no longer the cheap option for floss.**

### 1.2 Per-key pressure verdict

I found **no shipping instrument that gets per-key pressure from Hall-sensor or keyboard-switch keys**: every proven poly-pressure keyboard has a factory-built sensor under each key (Fatar's FSR matrix, carbon pads under foam), extra key travel in a custom action (Osmose), or a touch surface instead of moving keys (MicroFreak, QuNexus), and none of these is a part you can buy for a 25-key one-off. **The reliable choice is the platform's shared pressure strip (channel pressure).** One thing engineering opens up: when only one key is down, the firmware knows whose pressure it is, so TIDE's note-by-note planting can still be per note.

### 1.3 Trade-offs for you to decide

1. **Which engine?** Options: **D** (keyers: lowest power and chip count of the per-key engines), **C1** (SSI2164 VCAs: a textbook VCA per key, +$35, +0.7–1.7 W, SMD only), **A** (paraphonic: about the same cost as D, loses per-note strike and lift). **Recommendation: D.** Its keyer circuit is an organ-style technique, but my exact circuit needs one bench check by the builder (electronics, not keys). If it disappoints, C1 drops onto the same microcontrollers.
2. **Pressure: shared or something else?** Options: (a) **one shared strip**, as Big Energy; (b) **two strips, one per half**: same parts, so the left and right hands (or two players) press separately; (c) **embed a bought poly-pressure keyboard** (QuNexus-class): true per-key pressure, but floss loses its own keys, feel and family look. **Recommendation: (b)**, with single-key attribution in firmware (§3.4). It costs about the same as (a), and it suits the split.
3. **Keys: platform key or mass-produced magnetic switch?** Your rule is "reliable choices". Big Energy's key (Choc V2 with a magnet glued in the top, over an SS49E) is the shared-universe key, but it's Big Energy's own design and still waits for its bench test. **Low-profile magnetic Hall switches** (Gateron class, as in shipping Hall-effect keyboards) are the proven, mass-produced form of the same idea, but they need new key tops and carriers. **Recommendation:** use the magnetic switch for floss, unless Big Energy's key passes its bench test before floss's keys are ordered.
4. **BOW's battery.** The CATHEDRAL base holds 11.1 Wh, which gives D only **2.6–5.6 h** against T2's 4 h. Options: (a) **one 3000 mAh pouch cell in the lid** beside the speaker box (22.2 Wh in total, 5.2–11.2 h, +≈ 55 g in the lid, which makes lap tipping slightly worse); (b) a fifth base cell in the Daisy's slot, with the Daisy moved to the lid (13.9 Wh, 3.2–7.0 h: meets T2 only at moderate volume); (c) accept a miss of T2. **Recommendation: (a).**
5. **TIDE's size against T4.** HUSH is 290 × 186; T4 says about 290 × 135. Options: (a) keep 186 (a 51 mm miss); (b) **shrink to ≈ 160**, since floss's board is half Big Energy's (a 25 mm miss, and the speaker box still fits behind the controls); (c) meet 135 by putting the speaker box under the board where the battery is, and dropping the passive radiator. **Recommendation: (b).**
6. **Charging time with a 22 Wh pack (T3 ≤ 4 h).** The platform's 1 A charger needs **≈ 6.5–7 h** for 6000 mAh [plat]. Options: a **2–3 A single-cell charger** (a different mainstream part from Big Energy's), or accept ≈ 7 h. **Recommendation: the faster charger** for TIDE, and for BOW if it takes the lid cell.
7. **Passive radiator: slim parts or a thicker lid?** There's plenty of box **volume** in BOW's lid and TIDE's back band, but the matched pair with published data (Dayton DMA58 + DMA58-PR) is **32 and 38 mm deep**, against ≈ 17–20 mm inside. Options: (a) slim driver + slim radiator in today's depth, tuned by one acoustic measurement; (b) BOW's lid ≈ 13 mm thicker (closed ≈ 68 instead of 55) for the published pair. **Recommendation: (a).**
8. **BOW's strands: keep or drop?** With keyers they cost **+31 small SMD chips, ≈ +$11–17 and ≈ 3,300 mm² of parts**, and they still fit the base. **Recommendation: keep them if BOW is chosen.** Dropped, BOW loses its per-half colour and has only TONE, like TIDE.
9. **Targets floss beats (to note, not to decide):** tuning will be crystal-accurate, ≈ 0.1 cent and no warm-up (T9 asks ±3 cents), so any drift is only the deliberate kind. The dry-path hiss with keyers is zero from a silent key (T7).

---

## 2. Engine options (question 1)

### 2.1 What every engine has to do
- **Octave per half and MIDI notes on any key** mean each key's pitch must be set on its own. The 1974 way (12 top notes divided down) can't do that without a switch matrix of ≈ 125 analog switches (25 keys × 5 octave positions) [calc]. So **every engine generates one tone per key in a microcontroller**, as the concepts already assume.
- **Tone accuracy:** a hardware timer dividing a 150 MHz clock [chk: RP2350 "up to 150 MHz", [Raspberry Pi](https://www.raspberrypi.com/documentation/microcontrollers/silicon.html)] gives about 0.05 cent steps with a 16-bit counter, and a crystal's ±20–50 ppm is ≈ 0.03–0.09 cent [calc]. **T9 is beaten by about 30×**: no warm-up, no TUNE wait. The rear TUNE trim becomes a firmware offset.
- **Tone generators per chip:** the RP2350B has **24 PWM channels** and **12 PIO state machines** [chk, same page]. PWM channels come in pairs that share one counter, so a pair gives one frequency (RP2350 datasheet; not re-read this session [est]). That's **12 + 12 = 24 independent tones per RP2350B**, one short of 25. The 25th comes from a second microcontroller's PIO (engines C and D have one anyway) or from a spare Daisy timer (A).
  - Module: Pimoroni **PGA2350**, an RP2350B on a 25.4 × 25.4 mm, 64-pin 0.1" grid with **48 GPIO** [chk, [Pimoroni](https://shop.pimoroni.com/en-us/products/pga2350)]. Price not shown on the page; I use $12–15 [est].
  - Drift (TIDE's DRIFT) is a slow re-write of each timer's period at a period boundary, glitch-free [est].
- **Alternative:** one iCE40-class FPGA could make all 25 (or BOW's 75) tones and the 25 envelopes. That's fewer chips but a new toolchain (HDL) for a one-off. I don't recommend it [est].

### 2.2 Envelope control voltages (25 of them, engines C and D)
| Route | Parts | Notes |
|---|---|---|
| **Filtered PWM from a second RP2350B** (recommended) | 1 module + 25 two-pole RC filters | 24 PWM channels share a ≈ 146 kHz carrier at 10 bits; a 2-pole filter at ≈ 500 Hz cuts the carrier by ≈ 99 dB and still allows a ≈ 1 ms attack [calc]. 10 bits is a −60 dB smallest step, so long tails need firmware dither, or the last step of a 30 s TIDE release may be audible in silence [calc]. The same chip reads the 25 Hall sensors (its ADC is 500 kS/s [chk]) and makes the 3 BBD clocks on spare PIO |
| 8-channel SPI DACs (×4) | e.g. TI DAC60508 | Clean, 12-bit, but DigiKey shows a **26-week factory lead time** [chk, [DigiKey](https://www.digikey.com/en/products/detail/texas-instruments/DAC60508MRTET/8111103)], which is risky against T10. Price not read |
| One DAC + sample-and-hold demux | 1 DAC, 4 × CD4051, 25 caps, 7 quad op-amps | The Prophet-5 way; proven but more chips than either above [est] |

**Pins on the second RP2350B (C, D):** 25 envelope + 1 tone + 3 BBD clocks + 4 mux selects + 2 ADC (Halls via 2 × 16:1 mux) + 4 link to the tone chip + 2 UART to the Daisy ≈ **41 of 48** [calc]. The first RP2350B uses 24 tone pins + 4 link pins. The Daisy keeps the panel muxes, MIDI, audio, the Daisy shimmer modes, echo and reverb, as on Big Energy.

### 2.3 Amplitude per key: three ways
| | SSI2164 (C1) | LM13700 (C2) | **Analog-switch keyer (D)** |
|---|---|---|---|
| What it is | Quad current-mode VCA, −33 mV/dB control, needs an op-amp per channel at the output [chk, [datasheet](https://soundsemiconductor.com/downloads/ssi2164datasheet.pdf)] | Dual OTA, DIP-16, the classic DIY VCA [est] | A CMOS switch (74HC4053) steers each key's envelope voltage to a + bus or a − bus in time with that key's square wave. The output is the square at the envelope's height. Exact for squares, which is all floss makes [calc] |
| Channels per chip | 4 → 7 chips + 7 quad op-amps | 2 → 13 chips | 3 → 9 chips (one per key with strands) |
| Package | **16-lead SOP only** [chk] | DIP or SOIC [est] | DIP or SOIC [est] |
| Supply current | **±6 mA typ, ±8 max per chip** (class AB) [chk] | ≈ 3–5 mA per chip with buffers [est] | µA [est] |
| Noise | −93 to −101 dBu per channel [chk]; 25 summed ≈ −79 to −87 dBu [calc]: passes T7, less margin | Worse than SSI2164; T7 unchecked [est] | A silent key adds nothing: its tone is stopped. A sounding key adds only its envelope ripple (≈ −99 dB) [calc] |
| Price | **$4.95 each** at qty 1 [chk, [Amplified Parts](https://www.amplifiedparts.com/products/integrated-circuit-ssi2164-quad-vca-sound-semiconductor)] | ≈ $1.5–2.7 [est] | ≈ $0.3–0.5 [est] |
| Risk | Textbook | Textbook | **Needs one bench check:** (1) the + / − buses must match (1 % resistors leave the envelope's own shape at ≈ −40 dB, which could thump on 1 ms attacks; use 0.1 % or a trim); (2) switch charge injection at the tone edges is harmonic, not noise; (3) the tone must stop when the envelope reaches zero, or 25 idle keys leak at ≈ −60 dB [calc/est] |

**Precedent for keyers:** organ-style divide-down instruments keyed notes individually. The Eminent 310 had a "polyphonic (ie. every note independent of all the others) extended release", while the Solina had "a single envelope generator" and couldn't articulate notes while others were held [chk, [Sound on Sound](https://www.soundonsound.com/reviews/eminent-310-string-synthesizer)]. D is that idea with the envelope voltage set by firmware.

**Fallback:** if D's bench check fails, C1 uses the same two microcontrollers and envelope filters. It adds 14 chips, ≈ $35, ≈ 1,200 mm² of parts and 0.7–1.7 W [calc].

### 2.4 The engines in detail

| | A. Paraphonic | C1. SSI2164 | C2. LM13700 | **D. Keyers** |
|---|---|---|---|---|
| **Per-note velocity** | No: the first note of a phrase sets the one envelope | Yes | Yes | Yes |
| **Per-note release (lift)** | No: everything releases with the last key | Yes | Yes | Yes |
| **Per-note pressure** | No | No (shared strip, §3) | No | No |
| **Per-note drift, octave per half, MIDI on any key** | Yes | Yes | Yes | Yes |
| **Tones** | 1 RP2350B (24) + 1 Daisy timer | RP2350B #1 (24) + #2 PIO (1) | same | same |
| **Envelope CVs** | 1 (shared) + 25 de-click gate lines via 4 × 74HC595 | 25 filtered PWM on RP2350B #2 | same | same |
| **Amplitude** | 9 × 74HC4053 de-click keyers + 1 SSI2164 channel | 7 × SSI2164 + 7 quad op-amps | 13 × LM13700 | 9 × 74HC4053 + 1 dual op-amp |
| **Engine chips** | 16 | 16 | 15 | **12** |
| **Parts area (courtyard)**, SMD / DIP | 3,215 / 7,150 mm² | 4,675 / n.a. | 4,825 / 12,200 mm² | **3,455 / 6,650 mm²** |
| **Engine power** at 5 V | 0.23–0.42 W | 0.95–2.32 W | 1.05–2.00 W | **0.33–0.62 W** |
| **Engine cost** | $23–30 | $67–78 | $49–73 | **$31–41** |
| **Concepts** | Neither as designed: BOW and TIDE both rest on per-note articulation | BOW, TIDE | BOW, TIDE (TIDE only as DIP) | **BOW, TIDE** |

All rows [calc] from §7's part-by-part figures [est]. The common electronics (Daisy, ensemble, power, audio, MIDI, muxes, mix) add ≈ 8,250 mm² SMD or 13,450 mm² DIP-leaning [est], and 1.3–2.8 W [calc].

**T6 (key to sound ≤ 5 ms):** Hall scan at 8 kHz per key (25 keys on 2 ADC channels = 200 kS/s, under the 500 kS/s limit [chk]) + envelope filter ≈ 1 ms + Daisy codec path ≈ 1–2 ms ≈ **2–3 ms** [calc]. Passes.

---

## 3. Per-key pressure with proven parts (question 2)

### 3.1 What shipping instruments use
| Instrument | How it senses per-key pressure | Source |
|---|---|---|
| NI Kontrol S-series (Fatar keybed) | Fatar added "an FSR matrix to allow the detection of the key pressure independently" | [chk, [Native Instruments](https://www.native-instruments.com/blogs/blog/polyphonic-aftertouch)] |
| Carbon-pad aftertouch boards (replacement kit whose file is named for the Prophet T8) | A carbon dot over a gold interdigitated pattern under each key, with foam on top; sold as replacement strips because they wear | [chk, [kit instructions](https://cdn.shopify.com/s/files/1/1883/9389/files/t8_aftertouch_replacement_instructions.pdf)] |
| Expressive E Osmose | A custom action: ≈ 9 mm to a first resistance, then "at least as far again" of pressure travel on white keys | [chk, [Sound on Sound](https://www.soundonsound.com/reviews/expressive-e-osmose?amp)] |
| Arturia MicroFreak (25 keys) | No moving keys: a PCB of exposed nodes that senses "both the firmness and area" of skin contact | [chk, [Sound on Sound](https://www.soundonsound.com/reviews/arturia-microfreak)] |
| Keith McMillen QuNexus (25 keys) | "Smart Sensor" keys with polyphonic aftertouch; ≈ 10 × 3.5 × 0.5 in, 14 oz, USB-powered, CV out | [chk, [Synthtopia](https://www.synthtopia.com/content/2012/11/01/the-qunexus-smart-sensor-keyboard-controller-offers-midi-control-voltage-osc-usb-and-polyphonic-aftertouch/)] |
| ASM Hydrasynth Explorer (37 slim keys, runs on 8 AA) | "PolyTouch", "a new method of polyphonic aftertouch sensing"; method not published | [chk, [Sweetwater](https://www.sweetwater.com/store/detail/HydrasynthExp--asm-hydrasynth-explorer-8-voice-digital-polyphonic-aftertouch-keyboard-synthesizer)] |
| Ensoniq SQ-80 | A keyboard that "does not use mechanical sensors for detecting velocity and pressure" | [chk, [Wikipedia](https://en.wikipedia.org/wiki/Ensoniq_SQ-80)] |

### 3.2 Can Hall or Choc-type keys do it? Not with proven parts
- A Hall sensor under a keyswitch measures **travel**. A Choc or magnetic switch bottoms out on its housing, so once the key is down, there's nothing left to measure.
- Each way to add it is a **custom mechanism**: a compliant stop with extra travel (Osmose-style), an FSR under each switch (which means each switch floats), or per-key carbon pads. DIY forums discuss exactly these as untried ideas: measuring "the 2–3 mm of travel after the key hits the keybed" with a magnet per key, with calibration "mandatory" [chk, [MIDIbox forum](https://forum.midibox.org/t/polyphonic-aftertouch-sensors-fsr-hall-capacitive-or-optical/12288)].
- No vendor sells a 25-key mini keybed to individuals, with or without poly pressure [plat, `eng/key-sourcing.md`].
- **So by your rule (proven parts, no experiments, no key test by you), per-key pressure on floss's own keys is out.**

### 3.3 The reliable routes, and what each costs
| Route | Proven? | Cost | What it gives |
|---|---|---|---|
| **(a) One shared strip** (Big Energy's floating strip C on two FSR lanes) | The principle (one pressure strip under all keys) is how channel aftertouch is normally built [est]. Big Energy's exact construction still waits for its own spike (tests A1–A8) [plat] | ≈ +$18–33, ≈ 1 mW, 0 mm height [plat] | Channel pressure: one value for the whole instrument |
| **(b) Two strips, one per half** (opening) | Same parts as (a), cut and wired per half; the floating strip splits into two floating halves (same risk level as (a)) [est] | ≈ +$20–36 [est], +1 ADC channel | Left and right hands (or two players) press separately; matches the split and MIDI split (pressure on channel 1 and 2) |
| **(c) Embed a bought poly-pressure keyboard** (QuNexus-class) over USB | Yes: a shipping product | ≈ $130–150 [est, price not checked], less the keys and strip it replaces (≈ $56–89 [plat]) | True per-key pressure. But floss **loses its own keys**, their feel and the family look, and depends on one vendor. The RP2350 would host it over USB [est] |

### 3.4 Firmware opening: single-key attribution
The Hall sensors know which keys are fully down. **If exactly one key is down, the strip's pressure belongs to that key**, and the firmware can treat it as that note's pressure [calc]. In a chord, it falls back to pressure on everything (or on the newest note, a choice to test by ear). Cost: firmware only.

### 3.5 What each concept loses under the fallback
- **BOW:** strike (velocity = speed) and lift (release) stay **per note**. Lean becomes whole-instrument: swell turns into FILL, and vibrato acts on every note. **The "thinning unless you lean" behaviour has to go** (otherwise every chord sinks unless you press), as the concept already says. With route (b), a held left-hand chord and a right-hand melody can be leaned separately. With attribution, a single melody note can be leaned on its own. So BOW keeps 2 of its 3 per-finger gestures fully, and the third partly.
- **TIDE:** the DRIFT knob's per-key random walk is unaffected (it's firmware per tone). **Planting drift by pressure still works note by note**, because TIDE's main flow (F8) plants one note at a time: single-key attribution covers it [calc]. Only leaning into a note while others are held becomes whole-instrument.
- **Panel:** no change in either concept.

### 3.6 Keys: "reliable choices"
- **Big Energy's key** (Choc V2 silent + K&J D31 magnet in a pressed-on top + SS49E) [plat] is a Big Energy design with a bench test still listed before its board order (`velocity-and-keys-v2.md` §2.6).
- **The mass-produced form of the same idea** is a low-profile magnetic switch over a linear Hall sensor on the PCB, as in shipping Hall-effect keyboards. Example: Gateron Low Profile Magnetic Jade, 0.1–3.3 mm actuation range, rated 100 million presses, $55.95 per pack of 70 or 90 [chk, [NuPhy](https://nuphy.com/products/gateron-low-profile-magnetic-jade-switches)]. Big Energy's own key survey ranked this type first for the full instrument [plat, `eng/key-sourcing.md`].
- Its stem, and whether CATHEDRAL's carriers and HUSH's pegs fit it, are **unchecked**. That's design work, not a test of the sensing. Trade-off 3 in §1.3.

---

## 4. Fit per body with the battery (question 3)

### 4.1 Board area
| | BOW (CATHEDRAL base, 286 × 132 × 27.6) | TIDE (HUSH, 290 × 186 × 25.5) |
|---|---|---|
| Height for electronics | ≈ 11.1 mm under the plate [plat, CATHEDRAL §19.2]: top parts ≤ 6.5 mm, SMD underneath | Board top ≈ z 14; battery bay z 1.5–12.9 under it [plat, HUSH rev 6.2] |
| Board area behind the keys | ≈ 265 × 72 = 19,080 mm² (y 56–132) [calc] | Big Energy's HUSH main board was 268 × 115 = 30,820 mm² [plat] |
| Less battery strip (x 36–196, y 100–126) | −4,160 mm² [plat] | Bay under the board (no board area lost) |
| Less panel parts (4 rotaries, 9 pots, 3 buttons or toggles, 6 tabs) and I/O | −3,625 − 1,000 mm² [calc, platform rates] | ample |
| **Free board, top side / both sides** | **10,295 / ≈ 23,700 mm²** → parts capacity at 70 % fill 7,200 / 16,600 mm² [calc] | — |
| Daisy | In the rear strip, x 199–251, on the floor [plat] | On the board |

| Engine (parts courtyard needed) | BOW top side only | **BOW double-sided SMD** | TIDE (board needed vs 30,820 mm²) |
|---|---|---|---|
| A, SMD (10,315 in BOW) | ✗ −30 % | ✓ +61 % | ✓ |
| C1, SMD (11,775) | ✗ −39 % | ✓ +41 % | ✓ +67 % (268 × 69) |
| C2, SMD (11,925) / DIP (24,500) | ✗ | SMD ✓ +39 % / DIP ✗ −32 % | SMD ✓ / DIP ✗ −16 % (268 × 137) |
| **D, SMD (10,555)** | ✗ −32 % | **✓ +57 %** | **✓ +84 % (268 × 62)** |
| D + BOW strands, SMD (13,845) | ✗ | ✓ +20 % | n.a. |
| C1 + strands, SMD (15,415) | ✗ | ✓ +8 % (too tight) | n.a. |
| D, DIP-leaning (18,950) | ✗ | ✗ −12 % | ✓ +7 % (268 × 107) |

All [calc] from §7's part areas [est]. **BOW needs SMD on both sides of its base board, or a second board in the lid** beside the speaker box (≈ 20,000 mm² free there [est]), joined over the hinge as CATHEDRAL's ribbon already is. A board in the lid moves weight back (§6.3). A hand-built DIP floss only fits TIDE.

### 4.2 Battery, size, weight
| | BOW | TIDE |
|---|---|---|
| Battery space as drawn | 4 × PiShop 952540 (9.5 × 25 × 40, 750 mAh) end to end = **11.1 Wh** [plat] | Bay 130 × 66 × 11.4 for 2 × 50 × 60 pouch cells = **22.2 Wh** (2 × PiShop 755060, 7.5 mm, 3000 mAh, $15.95 each) [plat] |
| Wh needed for T2 (4 h) with D, mid / high | 12.3 / 17.2 Wh [calc] | same |
| **T2 pass?** | **✗** at 11.1 Wh (2.6 / 3.6 / 5.6 h). With one 755060 in the lid (22.2 Wh): ✓ 5.2 / 7.2 / 11.2 h | **✓** 5.2 / 7.2 / 11.2 h |
| T3 (charge ≤ 4 h) | 3000 mAh at 1 A ≈ 3.3 h ✓; with the lid cell ≈ 6.5–7 h ✗ [plat] | ≈ 6.5–7 h ✗ at 1 A [plat]; needs a 2–3 A charger |
| **T4 size** (≈ 290 × 135) | 286 × 132 ✓ (closed ≈ 55) | **290 × 186 ✗ by 51 mm**; ≈ 160 looks possible with floss's smaller board [est] |
| **T5 weight** (≤ 1.5 kg) | base ≈ 0.53–0.57 + lid ≈ 0.35–0.45 = **≈ 0.88–1.02 kg ✓** [est: CATHEDRAL's 0.40 / 0.375 kg at D 108, shell scaled to D 132, floss's contents] | **≈ 0.8–1.1 kg ✓** [est] |

---

## 5. BOW's strands (question 4)

**What BOW asks for:** each key sounds an octave below, at pitch and an octave above. Six tabs switch the strands per half.

| Route | Chips (in addition to the engine) | Area | Cost | Notes |
|---|---|---|---|---|
| **Keyers (D)**: the tone chip makes 2f per key; one CD4520 counter per key divides to f and f/2; each strand gets its own keyer switch on its own strand bus; the tabs switch **6 bus pairs**, not 75 notes | +13 CD4520, +16 74HC4053 (25 in total, one per key), +2 74HC4066 for the bus switching = **+31** | +3,290 mm² SMD / +9,350 DIP [calc] | **≈ +$11–17** [est] | **The cheapest route.** It replaces the concept's 19 × CD4066 gates. Every strand of a key shares that key's envelope |
| VCA engines (C1, C2): mix the strands before each key's VCA | +13 CD4520, +19 CD4066 strand gates = +32 | +3,640 SMD / +9,900 DIP [calc] | ≈ +$14–22 [est] | Leaves C1 at 8 % area margin in BOW: too tight |
| FPGA (all 75 tones in one chip) | −13 counters, −1 microcontroller, +1 FPGA | less | similar | New toolchain; not recommended |

- **Tone ceiling:** 2f reaches 4,186 Hz at +2 octaves (C7 main strand) [calc], easy for the timers.
- **"Rounded toward a sine":** mixing squares and letting TONE round them (the concept's choice) needs nothing more. Per-strand RC would add 75 resistor–capacitor pairs.
- **Dropped strands:** −31 chips, −$11–17, −3,300 mm². BOW loses its per-half colour (J7: cello left, violins right) and keeps only TONE, like TIDE.

---

## 6. Speaker, passive radiator and lap stability (question 5)

### 6.1 What a passive radiator needs
Reference driver with published data: **Dayton DMA58-4** (2"): Fs 165.5 Hz, Qts 0.46, Vas 0.005 ft³ (0.14 L), Sd 14.5 cm², Xmax 2 mm, **mounting depth 1.25" (32 mm)**, $13.98 [chk, [Parts Express](https://www.parts-express.com/Dayton-Audio-DMA58-4-2-Dual-Magnet-Aluminum-Cone-Full-Range-Driver-4-Ohm-295-582)]. Its matched **DMA58-PR**: Fs 39.8 Hz, Sd 14.5 cm², Xmech 7 mm, Mms 6.7 g, **depth 1.5" (38 mm)**. The rule is that the radiator should displace at least twice the driver's air [chk, [Solen](https://solen.ca/products/speakers/home-speakers/passive-radiators/dayton-audio-dma58-pr-2-dma-series-passive-radiator/)].

| Box (sealed, DMA58-4) | Fc | Qtc |
|---|---|---|
| 0.15 L | 231 Hz | 0.64 |
| 0.30 L | 201 Hz | 0.56 |
| 0.50 L | 187 Hz | 0.52 |

[calc, closed-box formulas.] A sealed box bigger than ≈ 0.3 L hardly helps: the driver's own resonance is the floor. A radiator tuned to ≈ 120–140 Hz in ≈ 0.15–0.3 L is where the gain is (≈ half an octave lower, to be simulated) [est]. Volume needed for the radiator: driver Vd = 14.5 × 0.2 = 2.9 cm³, so the radiator needs ≥ 5.8 cm³ [calc].

### 6.2 Available against needed
| | Volume available | Volume needed | Depth inside | DMA58 pair (32 / 38 mm) | Slim parts |
|---|---|---|---|---|---|
| **BOW lid** (≈ 22 deep as drawn; CATHEDRAL's lid half is ≈ 27) | ≈ 566 cm³ gross (277 × 123 × 16.6); a 200 × 100 × 16 box = 320 cm³ leaves a third of the lid for a cell or a board [calc] | 150–300 cm³ [est] | ≈ 17–22 mm | **✗** (needs a lid ≈ 13 mm thicker: closed ≈ 68 instead of 55) | **✓ volume**: e.g. Same Sky CDS-5076 driver (7.6 mm deep, T/S unpublished) [plat] with a Tectonic TEPR32-class radiator (Sd Ø 32 mm, ±5 mm, Fs 40 Hz, Mms 4.2 g [chk, [datasheet](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5336/TEPR32.pdf)]: ≈ 4 cm³ displacement against a slim driver's ≈ 1 cm³ [calc]) |
| **TIDE** (back band behind the controls, firing down) | ≈ 178 cm³ (190 × 55 × 17) at 186 deep; still fits at ≈ 160 deep [calc] | 150–300 cm³ [est] | ≈ 17–19 mm | ✗ | ✓, but **firing into a lap muffles it**: it needs feet or a foot ring with ≥ ≈ 10 mm gap [est] |

**Verdict:** both bodies have the **volume** for a passive radiator box. The **depth** rules out the parts with published matched data. The slim pairing needs **one acoustic measurement** to pick the radiator's mass (an engineering bench step, not a key test). Expect real but modest gain: a 50 mm slim driver is excursion-limited [est].

### 6.3 Does BOW tip back on a lap with the lid standing?
Model: base mass 0.53–0.57 kg with its centre at y ≈ 69; lid 0.35–0.45 kg with its centre 66 mm out along the lid; hinge axis at y 133, z 26.25 [plat, CATHEDRAL §19.6] [est masses].

| Lid angle | Combined centre of mass (from the front edge) | Margin to the rear edge (132) |
|---|---|---|
| 90° | 94–97 mm | 35–38 mm |
| 100° | 99–102 mm | 30–33 mm |
| **120° (CATHEDRAL's stand)** | **107–112 mm** | **20–25 mm** |

[calc] **On a table or bench:** stable, with the stays behind as well. **On a lap:** thighs rarely support the base's rear quarter. If they support only up to y ≈ 100, the hands must press ≈ 1 N on the keys to hold it, about the weight of resting wrists. If only to y ≈ 80, ≈ 5 N [calc]. So **it stays put while you play, and can tip back when you lift both hands**. Remedies, in order of cost: stand the lid at ≈ 100° (−9 mm), keep cells and the board out of the lid, or put the battery at the front of the base. A cell in the lid (trade-off 4a) moves it ≈ 3 mm back.

---

## 7. Power budget and runtime (question 6)

**Method:** Big Energy's (`budget-variant.md` §v1.11.2, `battery.md`): load at 5 V; ± rails made at 80 % [est]; boost 90 % at ≤ 2.4 W, falling to 85 % at 4.4 W; usable energy 90 % of nominal.

### 7.1 Loads (W at the 5 V bus)
| Block | Low | High | Basis |
|---|---|---|---|
| Daisy Seed | 0.40 | 0.80 | [plat] ESTIMATE; Electro-Smith says current "will depend on programming" [chk, [forum](https://forum.electro-smith.com/t/power-consumption/4521)]. **Measure it** |
| 25 × SS49E via a 3.3 V buck | 0.58 | 0.97 | 6 mA typ / 10 mA max each [chk, [Honeywell](https://www.farnell.com/datasheets/1676929.pdf)], 85 % buck [est]. Via Big Energy's LDO it would be 0.75–1.25 W [calc]: **use a buck** |
| BBD ensemble (3 × V3207 + clock + filters) | 0.12 | 0.44 | V3207 4–10 V, current not stated [chk, [Coolaudio](https://www.coolaudio.com/docs/COOLAUDIO_V3207_DATASHEET.pdf)]; V3102 0.5 mA [chk, [datasheet](https://cdn.mediavalet.com/aunsw/musictribe/sqqx9zK0GkyHkAXphmCw0A/jrIhIpN7R0m5p9AUoziLmQ/Original/COOLAUDIO_V3102_DATASHEET.pdf)]; op-amps dominate [est] |
| Mix, TONE, phones | 0.06 | 0.25 | [est] |
| Class-D speaker amp, moderate volume | 0.08 | 0.20 | [est]; Big Energy's LM386 would be ≈ 0.2–0.35 W |
| MIDI, muxes, LEDs, strip | 0.03 | 0.10 | [plat/est] |
| **Common subtotal** | **1.28** | **2.76** | [calc] |
| Engine A / C1 / C2 / D | 0.23 / 0.95 / 1.05 / 0.33 | 0.42 / 2.32 / 2.00 / 0.62 | §2.4 |

### 7.2 Totals and runtime
| Engine | Total W (low / mid / high) | 11.1 Wh (BOW base) | 13.9 Wh (BOW + 5th cell) | 22.2 Wh (TIDE, or BOW + lid cell) | Wh for 4 h at mid / high |
|---|---|---|---|---|---|
| A | 1.51 / 2.35 / 3.18 | 5.9 / 3.8 / 2.8 h | 7.4 / 4.8 / 3.5 h | 11.9 / 7.7 / 5.5 h | 11.6 / 16.0 |
| C1 | 2.23 / 3.66 / 5.08 | 4.0 / 2.4 / 1.7 h | 5.0 / 3.0 / 2.1 h | 8.1 / 4.7 / 3.3 h | 18.7 / 26.6 |
| C2 | 2.33 / 3.54 / 4.76 | 3.9 / 2.5 / 1.8 h | 4.8 / 3.1 / 2.2 h | 7.7 / 4.9 / 3.6 h | 18.1 / 24.9 |
| **D** | **1.60 / 2.49 / 3.38** | 5.6 / 3.6 / 2.6 h | 7.0 / 4.5 / 3.2 h | **11.2 / 7.2 / 5.2 h** | **12.3 / 17.2** |

All [calc]. **Biggest levers:** the Hall sensors (a quarter to a third of the load) and the unmeasured Daisy. Both go first in the bench measurements. **Boost:** at 3.4 W, ≈ 0.7 A at 5 V, so it needs Big Energy's ≥ 2 A boost, not the charger board's 1 A [plat].

---

## 8. Part areas and costs used (for checking)
Courtyard per item including local passives [est, at Big Energy's rates: pot 125 mm², rotary 325, button 100, Daisy 1,150]: RP2350B module 800; 74HC4053 keyer 120 SMD / 350 DIP; SSI2164 + quad op-amp + 4 channels' passives 350; LM13700 + passives 200 SMD / 700 DIP; CD4520 90 / 250; 74HC595 90 / 250; 25 two-pole envelope filters 625 / 1,500. Common SMD / DIP-leaning: ensemble 2,200 / 3,500, power 2,000 / 3,000, audio out 1,000 / 1,200, MIDI 500 / 600, panel muxes 300 / 1,000, mix 800 / 2,000, Hall muxes 300 / 1,000.

Common one-unit cost ≈ $370–645 [est]: Daisy $34.99 [plat]; keys $38–56 [plat]; strip $18–33 [plat]; panel $20–30; ensemble $20–30; battery, charger, boost and rails $50–58 [plat + est]; speaker, radiator and amp $8–38; I/O $6–10; mix and muxes $10–15; boards $75–150 [plat] + SMD assembly $30–80; case and hardware $30–60; shipping $30–50 [plat]. BOW adds strands (+$11–17) and, if chosen, a lid cell (+$15.95 [plat]).

## 9. Not covered (doesn't change which engine or concept is viable)
Exact BBD part and noise budget (V3207's S/N of 73 dB typ [chk] across three summed paths gives ≈ 77 dB, so T8 passes on paper [calc]), mux details, status lights, lift-timing firmware, and which slim driver and radiator to buy.
