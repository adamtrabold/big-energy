# floss sound module: engineering baseline (rev 0, 2026-11-22)

Status: **rev 0**, by the engineer, for the designers and Adam. It consolidates `feasibility.md`, `controller.md` and the requirements' rev 2 into one baseline. Published evidence only; nothing measured. The pad and key files (`keys.md`, `pads.md`, `silicone.md`) are shelved.

Adam (verbatim):
- "I like the idea of focusing on the sound module now and making it so a travel MIDI controller can be carried with the module"
- "This is the plan for all modular portable synths that we build — portable sound modules with a way to carry a keyboard with it. It should be flexible and not reliant on a single model of keyboard."

**Marks:** **[chk]** checked against the linked source · **[plat]** from Big Energy's eng records · **[calc]** my arithmetic · **[est]** my estimate.

---

## 1. Summary

**floss is a keyless sound module with:**
- 25 analog-keyed voices (engine D);
- a 3-path bucket-brigade ensemble, plus Daisy modes, echo and reverb;
- a **USB-A host socket** that powers and reads **any class-compliant USB-MIDI controller**;
- its own USB-C for charging and MIDI to a computer;
- TRS MIDI in and out.

| | Baseline |
|---|---|
| Voices | **25**, allocated from incoming notes, oldest stolen past 25 (T1) |
| Engine | 2 × RP2350B (25 tones, 25 envelopes) + 9 analog-switch keyers; Daisy Seed for MIDI, panel, effects |
| Pressure | Poly aftertouch, MPE or channel pressure, whichever the controller sends |
| Controller port | USB-A host on Daisy D29 / D30; 5 V at **500 mA**, current-limited |
| Battery | 22.2 Wh (2 × 50 × 60 mm pouch cells) |
| Charger | 2–3 A single-cell power-path charger (TI BQ25895 class) |
| Runtime, typical controller | **6.1 / 8.6 / 14.4 h** (worst / mid / best) ✓ T2 |
| Runtime, controller at the full 500 mA | ≈ 3.5 h at loud volume ✗ |
| Minimum body | ≈ 250–290 × 90–110 × 30–35 mm incl. knobs [est]: fits T4 |
| Weight | ≈ 0.63–0.91 kg without a controller [est] |
| Cost, one unit | **≈ $355–610** without a controller; ≈ $440–700 with an Xkey 25; ≈ $490–775 with a K-Board C |

**Carrying the keyboard:**
- Slim travel controllers are **325–388 mm wide, 83–135 deep and 11–16 tall**. Chunkier minis reach 406 mm wide and 49 mm tall [chk, §6].
- **Any one-package carry is wider than T4's 290 mm.**

**Open for Adam (§8):**
1. Which controllers the carry fits: slim class only (recommended) or all.
2. One package (wider than T4) or two.
3. Charger and battery.
4. Slim passive radiator.
5. BOW's strands.
6. 25 voices.

---

## 2. Engine
**Voice allocation:**
- Each incoming note takes a free voice. Past 25, the oldest held note is stolen.
- Sustain (CC 64) and HOLD keep notes, so 25 voices covers T1 with a 25-key controller.
- More voices need a third RP2350B (+12 voices, ≈ +$12–15) [est].

**Tones:**
- Each voice is a crystal-timed square from an RP2350B timer.
- One RP2350B has 12 PWM-slice frequencies + 12 PIO state machines = 24 tones. The 25th comes from the second chip's PIO [chk/est, `feasibility.md` §2.1].
- Tuning is ≈ 0.05 cent steps, crystal-stable: T9 is beaten [calc].
- BOW's strands, if kept: the timer makes 2f, and a CD4520 counter per voice gives f and f/2 (+31 chips) [calc, `feasibility.md` §5].

**Envelope and amplitude per voice (engine D):**
- 25 filtered-PWM envelope voltages from RP2350B #2.
- Each one steers that voice's square onto ± buses through a 74HC4053 keyer.
- **Fallback:** SSI2164 VCAs on the same microcontrollers [`feasibility.md` §2.3].

**MIDI mapping (firmware):**
| Input | What floss does |
|---|---|
| Note number | A split at a fixed note (B3 \| C4, from the concepts). OCTAVE L and R add ±2 octaves to each side. A held note keeps its pitch. Keep the controller at its own default octave, or the split moves |
| Velocity | Per voice, with the meaning set by each concept (speed, loudness, lifespan) |
| Poly aftertouch | Per voice |
| MPE (per-note channel pressure, pitch bend) | Per voice; pitch bend retunes that voice's timer |
| Channel pressure only | All sounding voices (fallback) |
| Note-off velocity | Per-voice release, if the controller sends it |
| MIDI split switch | Re-sends the left half on channel 1 and the right on channel 2, out of TRS and USB-C |

**Parsing:** libDaisy parses poly key pressure, channel pressure and pitch bend [chk, `src/hid/MidiEvent.h`]. MPE zone handling is floss firmware [est].

**T6 (≤ 5 ms):** USB full-speed polling ≈ 1 ms + floss ≈ 2 ms ≈ 3 ms [est]. Each controller's own scan delay isn't published.

---

## 3. USB and MIDI ports
- **Host:** libDaisy's USB host MIDI runs on USB_OTG_HS, pins PB14 / PB15 = Seed D29 / D30 [chk, [libDaisy](https://github.com/electro-smith/libDaisy) `src/usbh/usbh_conf.c`, example `MIDI_USBH_Input`].
- **One device at a time:** no hub support found [est].
- **5 V for the controller:**
  - libDaisy's VBUS hook is an empty stub [chk], so floss powers the socket itself.
  - Use a TI TPS2553 USB power switch: current limit set from 75 mA to 1.7 A by a resistor, 2.5–6.5 V, a FAULT flag, "optimized for USB-A ports" [chk, [TI](https://www.ti.com/product/TPS2553)].
  - **Set it at ≈ 550–600 mA**, which covers a USB 2.0 device's 500 mA maximum [est]. FAULT goes to a Daisy pin, so floss can blink the status light.
- **Socket:** USB-A. Most controllers ship with a USB-A cable [est]. A USB-C host socket would also need the source-side CC resistors [est].
- **floss's own USB-C:** charging, and USB-MIDI device to a computer on the Seed's own port (`Periph::INTERNAL` [chk]). Host and device running together is **unverified** [est]. Fallback: TRS MIDI to the computer.
- **TRS MIDI in and out:** the Daisy UART (provisional D14 / D13) [plat], with an optocoupler on the input [est].

## 4. Sound path
**Signal path:** keyers → half buses → register mix and TONE → analog ensemble *or* Daisy mode → Daisy echo and reverb → VOLUME → class-D speaker amp and the phones / line driver (stereo spread on phones and line).

**Ensemble:**
- **BBDs:** 3 × Coolaudio V3207 (DIP-8, 4–10 V, S/N 73 dB typ) [chk, [Coolaudio](https://www.coolaudio.com/docs/COOLAUDIO_V3207_DATASHEET.pdf)].
- **Clocks:** from RP2350B #2's PIO, through a CMOS buffer, or V3102 drivers (0.5 mA) [chk/est].
- **LFOs:** two, at ≈ 1 Hz and ≈ 6 Hz, at 0 / 120 / 240° [concepts].
- **Noise:** the three summed paths give ≈ 77 dB, so T8 passes on paper [calc].
- **Daisy:** the Daisy Seed (65 MB) runs the Daisy shimmer modes, echo and reverb [plat]. Its spike targets apply: ≤ −95 dB codec noise, < 50 % CPU [plat].

---

## 5. Power and runtime
**Method:** Big Energy's. Boost 90 % at ≤ 2.4 W; 90 % of the battery's capacity usable.

| Load | Without controller | With a typical controller (0.25–0.5 W [est]; nanoKEY2 "< 100 mA" [chk]) |
|---|---|---|
| Total W (low / mid / high) | 1.00 / 1.70 / 2.41 | 1.25 / 2.08 / 2.91 |
| **22.2 Wh** | 7.5 / 10.6 / 18.0 h | **6.1 / 8.6 / 14.4 h** ✓ T2 |
| 11.1 Wh | 3.7 / 5.3 / 9.0 h | 3.0 / 4.3 / 7.2 h (✗ at loud volume) |

- **Worst case:** a controller drawing the full 500 mA (2.5 W) at loud volume ≈ 4.9 W → ≈ 3.5 h on 22.2 Wh [calc]. LED-heavy minis may approach it; their draw isn't published [est].
- **Where the watts go:** the Daisy 0.4–0.8 W [plat, unmeasured] and the ensemble and op-amps. The Hall key sensors are gone.
- **Battery:** 2 × PiShop 755060 (7.5 × 50 × 60 mm, 3000 mAh, $15.95 each) in parallel = 22.2 Wh [plat]; or Adafruit #328 (in stock, 18.5 Wh) [plat].
- **Charger for T3:** TI **BQ25895**: input limit up to 3.25 A, charge up to 5 A, NVDC power path (plays while charging), a 5 V boost up to 3.1 A that can also feed the controller socket [chk, [TI](https://www.ti.com/product/BQ25895)].
  - At 2 A, 6000 mAh charges in ≈ 3.3 h, ≈ 3.6 h with the taper [calc]. That needs a USB-C source of ≥ ≈ 2.5–3 A at 5 V [est]. From a 1.5 A source, ≈ 5 h.
  - Big Energy's 1 A bq25185 would take ≈ 6.5–7 h [plat].
  - 1 A per cell is within Adafruit's 1.2 A per-cell maximum for its 50 × 60 cell [plat].

## 6. Size: the module, and the controllers it carries
**Module parts** [calc/est, rates from `feasibility.md` §4 and §8]:
- **Electronics:** ≈ 11,500 mm² of parts → ≈ 16,500 mm² of board single-sided, or ≈ 8,300 mm² per side double-sided.
- **Panel:** ≈ 16 controls (4 stepped rotaries, ≈ 9 pots, 2–3 buttons or toggles; + 6 tabs for BOW) ≈ 3,600–4,500 mm². Two rows at the family's ≈ 20–24 mm pitch ≈ 180–210 × 60–70 mm.
- **Board:** **≈ 200 × 80 mm double-sided** holds both [calc].
- **Rear wall I/O:** USB-C, USB-A host, phones, line out, TRS MIDI in and out, TUNE trim, MIDI split switch, power switch (≈ 9 parts).
- **Battery:** 100 × 60 × 7.5 mm (side by side) or 50 × 60 × 15 (stacked). Can sit under the board.
- **Speaker and slim radiator:** a sealed box of ≥ 150–300 cm³ with ≥ 17–20 mm inside depth, e.g. 120 × 80 × 20 mm. The radiator pairing needs one acoustic measurement [`feasibility.md` §6].
- **Height:** floor 2.4 + cells 7.5 + underside parts 3 + board 1.6 + top parts ≤ 6.5 + deck 2–3 ≈ 23–25 mm body, + knobs ≈ 8 mm [plat] → **≈ 31–33 mm overall** [calc/est].
- **Minimum footprint:** ≈ **250–290 × 90–110 mm** [est]. That fits T4 (290 × 135), a CATHEDRAL half (286 × 132), or ONE SHEET (276 × 148) [plat]. HUSH (290 × 186) is larger than needed.

**25-key travel controllers worth supporting** (all USB bus-powered):
| Controller | W × D × H (mm) | Weight | Per-key pressure | Price | Source |
|---|---|---|---|---|---|
| Korg nanoKEY2 | 325 × 83 × 16 | 244 g | No (velocity only) | ≈ $50–60 [est] | [chk, [Korg](https://www.korg.com/us/products/computergear/nanokey2/page_1.php)] ("< 100 mA") |
| KMI K-Board C | 325 × 84 × 11 | 0.34–0.4 kg | Poly AT, MPE | $139–164 | [chk, [Thomann](https://thomannmusic.com/keith_mcmillen_k_board_c_snow.htm)] |
| Muse Kinetics QuNexus | 325 × 84 × 11 | 0.31 kg | Poly AT, MPE | $276, months out | [chk, [Thomann](https://www.thomannmusic.com/muse_kinetics_qunexus_galaxy.htm)] |
| CME Xkey 25 | 388 × 135 × 16 | 600 g | **Poly AT** on ≈ 3 mm moving keys | $88 | [chk, [Thomann](https://www.thomannmusic.com/cme_xkey_25_silver.htm), [SOS](https://www.soundonsound.com/reviews/cme-xkey)] |
| Arturia MicroLab mk3 | 406 × 125 × 39.3 | 615 g | No | $50 | [chk, [Thomann](https://www.thomannmusic.com/arturia_microlab_mk3_black.htm)] |
| Novation Launchkey Mini 25 MK4 | 338.5 × 176.8 × 49 | 0.78 kg | No (pads only) | $105 | [chk, [Thomann](https://www.thomannmusic.com/novation_launchkey_mini_25_mk4.htm)] |
| Akai MPK Mini IV | 347.5 × 192 × 45.7 | 1.05–1.1 kg | No (pads only) | £75 | [chk, [Thomann](https://www.thomann.co.uk/akai_professional_mpk_mini_iv_gray.htm)] |

**What this implies for carrying** [calc]:
- **Slim class** (nanoKEY2, K-Board C, QuNexus, Xkey): **325–388 × 83–135 × 11–16 mm, 0.24–0.6 kg**. A carry pocket for all four is ≥ ≈ 392 × 139 × 18 mm inside.
- **Chunky minis** (MicroLab, Launchkey, MPK): up to 406 wide, 192 deep and 49 tall. They play floss over USB but would double a slim carry's thickness.
- **Every one-package carry is ≥ 327 mm wide**, so T4's 290 is missed if the module and controller travel as one object. Carried side by side, the module alone meets T4.
- **T5 (≤ 1.5 kg) together:** module 0.63–0.91 + slim controller 0.24–0.6 → **0.87–1.51 kg**. The Xkey is borderline; chunky minis exceed it [calc/est].

## 7. Cost, one unit [calc]
- **Calculation:** Big Energy's common parts ≈ $370–645, less keys and strip ($56–89) [plat/est], + engine D $31–41 + USB-A host socket with TPS2553 ≈ $3–5 + charger upgrade ≈ $5–10 [est] → **≈ $355–610 without a controller**.
- **With a controller:** + Xkey 25 ($88): ≈ $440–700. + K-Board C ($139–164): ≈ $490–775. + nanoKEY2: ≈ $405–670.
- **Largest unknowns:** the boards and their assembly, and the case.

---

## 8. Open trade-offs for Adam
| # | Question | Options | Recommendation |
|---|---|---|---|
| 1 | Engine (from `feasibility.md`, still open) | D keyers / C1 SSI2164 | **D**; C1 as fallback |
| 2 | Which controllers the carry fits (new) | Slim class only (≤ 392 × 139 × 18 pocket) / all, incl. chunky minis | **Slim class**: chunky ones still plug in |
| 3 | One package or two (new) | One (≥ 327–392 mm wide: T4 miss) / two pieces (module meets T4) | Designers' call. Engineering is fine either way |
| 4 | Battery and charger (was trade-offs 4 and 6) | 22.2 Wh + BQ25895 (meets T2 and T3 with a ≥ 2.5 A source) / 11.1 Wh + Big Energy's 1 A charger | **22.2 Wh + BQ25895** |
| 5 | Controller power (new) | Supply the full 500 mA (covers any USB 2.0 controller; ≈ 3.5 h worst case) / cap lower | **500 mA**, since floss shouldn't depend on one model |
| 6 | Passive radiator (was trade-off 7) | Slim driver and radiator in ≈ 20 mm depth (one acoustic measurement) / thicker body for published-data parts (≥ 32–38 mm deep) | **Slim** |
| 7 | BOW's strands (was trade-off 8, if BOW survives as a module) | Keep (+31 small chips, ≈ +$11–17) / drop | Keep if BOW |
| 8 | Voices (new) | 25 / 12 (one fewer chip) / 37 (one more chip) | **25** |
| 9 | Host and computer USB at once (new) | Rely on it (unverified in libDaisy) / plan TRS MIDI to the computer as the fallback | Plan for both |

**Superseded from `feasibility.md` §1.3:** trade-off 2 (pressure sensing), 3 (keys), 5 (TIDE's HUSH depth: now set by the module's parts) and the lap-tipping note.

**Carried over unchanged:** T9 is beaten (crystal tuning). A silent voice adds no hiss (T7).
