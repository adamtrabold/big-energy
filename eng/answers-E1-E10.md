# Engineering answers to design asks E1–E10 (full version)

Status: rev 0, 2026-11-12. Answers `design/instrument/concepts/common-how-it-works.md` §7.
Ground rules: through-hole parts or ready-made modules only (owner: no SMD, no custom PCBA).
Conventions as in architecture-v2: link = sourced; **UNVERIFIED** = not confirmed this session;
**[ENG]** = engineering estimate. No look or layout calls here; where an answer constrains layout,
it is written as a **LAYOUT CONSTRAINT**.

## Summary

| Ask | Answer | Cost delta (one unit) | Risk |
|---|---|---|---|
| E1 mod depth as a VCA on the spare DAC channel | **Yes**, with an **AS3360** (DIP-14) rather than an LM13700, plus a 2nd knob mux. **Rev 1: feedthrough nulled automatically by firmware during autotune, no trimmer** | **+$8–13** | L–M |
| E2 speaker ≥ 40 mm, ≥ 60 mm from key sensors; notch | **Yes to both.** 60 mm is enough. Accept the notch; PAM8302 moves to the speaker | $0 electrical (speaker already budgeted) | L (magnetics), M (area) |
| E3 one rear USB-C: charge + USB-MIDI + firmware | **Yes**: USB-C breakout, VBUS to the charger, D± to the Pico's test pads. **Charging while MIDI works.** No PD/hub module | **+$4–6** | L–M |
| E4 key Pico firmware | **SWD from the main Pico** (fixed-body concepts); **UART A/B update** for MCUs across a joint (DOCK, DISH) | $0 | M (firmware effort) |
| E5 unipolar TO-92 Hall switch | **Yes: DRV5023 (TO-92, unipolar)**, power-gated | +$1–2 | L |
| E6 DOCK: D as 270 × 26/30 strip, battery in module, VBAT on pogo | **Battery/VBAT: yes, with 3+3 pins. D strip: not at 270 × 30 in one row**: needs ≈ 300 × 30 or 270 × 40 | +$5–10 over DOCK's own estimate | M |
| E7 DISH: dish MCU, low-profile B, ≤ 12 mm 40 mm driver | **Yes to all three**, with rules for the low-profile zone | DISH's +$25–40 holds | M–H (area) |
| E8 MOTTO speaker over left B board | **Acceptable** with the VCO cores ≥ 30 mm from the speaker and the amp at the speaker | $0–2 | L–M |
| E9 dual-gang pots for CC out | **Feasible, not recommended** (+5 mm stack, value availability) | +$15–25 | M |
| E10 strip C with all 25 x-positions | **Yes**, if footprint centres are ≥ 6.5 mm apart | ≈ $0–1 | L |

Net change to the eng baseline (E1 + E3 + E5): **+$13–21**, so first unit ≈ **$530–860** (was $515–840).
E6, E7 and E9 costs belong to the concepts that need them.

---

## E1. Mod depth as a voltage-controlled stage (J12/J13)

**Answer: yes.** Mod depth becomes a VCA in the mod path, set by the 8th MCP4728 channel. The mod wheel
becomes an MCU-read pot. That closes J12 (CC1 in sets mod depth) and J13 (the wheel sends CC1). The
jump-on-move rule applies to the wheel like any other "Yes" control.

**Where it sits.** In the original, the mod-mix amp (gain ≈ 2) drives the mod wheel pot through R57 1 k;
the wiper feeds the OSC MOD and FILTER MOD switches (CA-72 `board3-modmix.lib`, `docs/circuit/voice.md`).
The VCA replaces the wheel pot: mod-mix out → R57 → R_in → VCA → I-to-V op-amp → the same switches.
Upstream (MOD MIX pot, osc 3, noise) and downstream (switches, R52 33 k into the filter, the oscillator mod
bus) are unchanged.

**Part choice: AS3360, not LM13700.**
- The LM13700 is hard to get in DIP. synthDIY says TI "has discontinued the DIP-16 version"; the DIP
  versions left are XINLUDA/HGSEMI via LCSC ([synthDIY wiki](https://wiki.synthdiy.com/parts/otas)).
  Tayda's LM13700N is out of stock ([Tayda](https://www.taydaelectronics.com/ic-integrated-circuits/lm13700-lm13700n-operational-amplifier-ic.html)).
- The **Alfa AS3360** (CEM3360 clone, dual VCA) is a **14-pin DIP**. Its specs:
  - ±3 to ±12 V supply, so it runs on our ±10 V;
  - linear CV input (≈ 1.7 V for full gain) and exponential CV input;
  - > 100 dB control range;
  - 5 MHz signal-current bandwidth;
  - ≈ 1 % THD typical;
  - CV feedthrough 10 mV max in 10 Vpp untrimmed ([Tubes and More](https://www.tubesandmore.com/products/integrated-circuit-as3360-dual-vca-alfa-14-pin-dip); [Electric Druid](https://electricdruid.net/?p=2517)).
  - Price and US stock: UNVERIFIED (≈ $4–6 [ENG]).
- The bandwidth matters because osc 3 at audio rate gives audio-rate FM through this path, and the VCA passes it.

**Circuit [ENG]:**
- **Control:** MCP4728 ch 8 (0–2.048 V, or 0–4.096 V at ×2) → divider to 0–1.8 V → AS3360 linear CV,
  with ≈ 1 ms RC smoothing.
  - The firmware maps wheel or CC1 to the CV through a law table, fitted to the original wheel's depth
    against position under R52 loading.
  - The original wheel pot's value and taper are UNVERIFIED: derive them from Fig. 9-12 / CA-72.
  - 12 bits gives 4096 steps, so no zipper.
- **Signal:** mod-mix out → R57 1 k → R_in ≈ 100 k → AS3360 input (virtual ground) → TL072 transimpedance
  stage. Choose R_f so full CV gives unity, which matches the original wheel at full.
- **The trap:** CV feedthrough lands in the **oscillator pitch path**. Untrimmed, 10 mV in 10 V is 0.1 % of
  full scale [ENG]. If full mod is ≈ ±2 oct, that is ≈ 5 cents of pitch shift as the wheel moves with no
  modulation.
- **Fix, rev 1 (2026-11-12): automatic firmware null, no trimmer.** The owner wants no manual trims, so
  the trimmer of rev 0 is withdrawn. A firmware servo nulls the feedthrough every time autotune runs
  (power-up, after 10 min, and on the NTC trigger), so it also tracks temperature.
  1. **Quiet the source.** An **H11F1 photo-FET optocoupler** (DIP-6, bilateral, so it handles the ±10 V
     mod signal; price and stock UNVERIFIED) shunts the midpoint of a split R_in (2 × 50 k) to ground.
     A GPIO lights its LED.
     - Why not a 2N7000: its body diode conducts on negative swings when it is meant to be off.
     - Residual: R_on ≈ 100s of Ω against 50 k gives ≈ −45 dB or better. What leaks through is AC and
       averages out (step 3).
     - The MCU can't mute the source any other way: MOD MIX, osc 3 and noise are in-circuit knobs.
  2. **Measure the VCA output, not the VCO pitch.** OSC MOD and FILTER MOD are physical switches in the
     circuit, not MCU-read, so the mod path may not reach a VCO during autotune and the frequency counter
     can't be relied on. Instead:
     - The spare half of the TL072 (the I-V op-amp's twin) amplifies the VCA output ×10.
     - It is biased to mid-scale, with 10 k + Schottky clamps to 0 V and 3.3 V.
     - It feeds a spare channel on the 2nd 4067 (18 of 32 channels used), so the RP2350 ADC sees it.
     - In normal play this stage simply clips into its clamps. That is harmless: nothing listens to it.
     - With ×10 gain, 1 ADC LSB ≈ 0.16 mV at the VCA output [ENG].
  3. **Servo.** Step the mod-depth DAC through ≈ 9 points from 0 to full. At each point, average ≈ 4,000
     ADC samples and take the *difference* from the CV = 0 reading. ADC offset and gain error cancel
     because only mV differences matter.
  4. **Inject the null.** A Pico PWM pin (12-bit, ≥ 30 kHz) goes through a 2-pole RC (≈ 100 Hz) and a
     large resistor into the I-V summing node, scaled for about ±15 mV of correction at the output.
     - The firmware stores a correction per DAC point and interpolates between points while playing.
     - It iterates the servo until every point is within < 0.5 mV of the CV = 0 value (≈ 0.25 cent at
       ±2 oct full scale [ENG]).
     - It doesn't assume feedthrough is linear in CV, so any curve shape is fine.
     - PWM ripple at the output: 3.3 V × (100 Hz / 30 kHz)² × the injection attenuation is in the
       ≈ µV range, so negligible [ENG].
  5. **Fallbacks.**
     - If a null fails (out of range), the firmware flags it on the status LED and limits the wheel law
       near 0 to hide it. No user action.
     - **Alternative topology without CV feedthrough:** a 12-bit multiplying DAC (R-2R ladder used as
       the attenuator, e.g. a DIP-8 DAC8043-class part) has no CV feedthrough, only a constant op-amp
       offset. It would also free MCP4728 ch 8. DIP availability and status are **UNVERIFIED**, and
       code-change glitches go straight into the pitch path. Kept as plan B, not chosen.
- **Spare half:** the AS3360's second VCA could later put CONTOUR AMOUNT under MIDI too (also a CV path).
  It would need another DAC channel, i.e. a 3rd MCP4728 at $7.50. Not proposed; noted as an option.

**What it consumes:**
- **The last MCP4728 channel.** "Velocity *and* pressure out" would then need a 3rd MCP4728.
- **One more analog input. Finding:** v2 §2's MCU-read analog inputs already total 17:
  - 11 pots: bend, glide, TUNE, FREQ 2/3, cutoff, A/D/S ×2;
  - 3 RANGE ladders;
  - 2 rail monitors (§5b.3).

  A single CD74HC4067 has 16 channels, so v2 was already one short. With the mod wheel it is 18. **Add a
  2nd 4067** (DIP, ≈ $1) on another of the Pico's 3 ADC pins. Switch-type controls go to GPIO.

**Cost:**
- AS3360 ≈ $4–6 (UNVERIFIED), TL072 $0.5 (both halves used), H11F1 ≈ $1–2 (UNVERIFIED), passives $1.5,
  2nd 4067 $1. No trimmer;
- the wheel pot is still needed, but it no longer has to match an audio-path value;
- **+$8–13**.

**Risk:**
- **L–M.** Character: the VCA adds ≈ 1 % THD to the *modulator*. That is inaudible on vibrato, and only
  slight extra sidebands on deep audio-rate FM. Keep the input current low (large R_in) to reduce it.
- Noise ≈ −110 dB ([Electric Druid](https://electricdruid.net/?p=2517)): negligible against osc 3 levels.
- Feedthrough is handled by the auto-null (above). Residual risk: ADC noise or DNL limits the null.
  Mitigation: ×10 gain plus averaging; the PWM correction can add dither if needed.

**Verify:**
1. **SPICE:** a behavioural VCA (B-source multiplier plus a feedthrough term) dropped into the golden
   mod path, compared against the golden with the wheel pot (once its value is known).
   - Pass: mod depth vs position within ±0.5 dB of the fitted law across 0–100 %.
   - Pass: audio-rate FM sidebands (osc 3 at 220 Hz → osc 1) within ±1 dB of golden at full depth.
2. **SPICE (auto-null):** an AS3360 behavioural model with a deliberately skewed feedthrough curve
   (±10 mV, non-linear in CV), plus the H11F1 as a switched R_on, the ×10 sense stage and the PWM + RC
   injection.
   - Run the servo in a Python loop around ngspice, using `sim/reference` conventions.
   - Pass: converges to < 0.5 mV at all 9 points within 5 iterations.
   - Pass: PWM ripple at the VCA output < 10 µVrms.
3. **Bench:** after autotune, with OSC MOD on and MOD MIX at a quiet source, OSC 1 pitch moves < 0.5 cent
   between wheel 0 and max. Repeat cold and after 30 min warm.
   - CC1 sweeps match wheel sweeps.
   - Jump-on-move works on the wheel.

**What this unlocks for layout (design call, not mine):** the mod wheel no longer needs a shielded lead to
board B. Both wheels are ordinary MCU-read pots, so DOCK may put them on its key module (read by the key
Pico, sent over UART).

---

## E2. Speaker ≥ 40 mm, ≥ 60 mm from the Hall key sensors; notch vs grow depth

**Answer: 60 mm is sufficient. Accept the 48 × 48 notch in the A/B pair**, keeping eng §6's +10–15 mm
depth as the fallback.

**Magnetics [ENG]:**
- **Static field.** Treat the speaker's motor as a dipole. A 40 mm Nd driver (e.g. N38 in the
  [CUI CMS-4021-34SP](https://www.digikey.com/en/products/detail/same-sky-formerly-cui-devices/CMS-4021-34SP-X5/18742615))
  has a magnet of roughly Ø15 × 3 mm (UNVERIFIED size), so m ≈ 0.5 A·m².
  - On-axis B = μ₀m / (2πr³) ≈ **0.5 mT at 60 mm**, and less with the steel cup. A ferrite driver is similar.
  - Key magnets swing the sensor through **≈ 20–150 mT** [ENG, magnet-dependent].
  - So the speaker adds a ≤ 2–3 % **static offset**, which the per-key rest/bottom learning absorbs.
- **Dynamic field.** The voice coil (≈ 0.7 A peak) gives ≈ µT at 60 mm: three orders of magnitude below a
  key signal. **No false notes from loud playing.**
- **Rule of thumb:** offset falls as 1/r³.
  - Below ≈ 40 mm the offset reaches ≈ 10 % and starts to eat the linear range of high-sensitivity
    sensors (DRV5053VA-class, ≈ ±9 mT span [ENG]).
  - 60 mm keeps margin with any sensor variant.

**LAYOUT CONSTRAINTS (E2):**
- Speaker magnet centre ≥ 60 mm from the nearest key sensor.
- Speaker magnet ≥ 50 mm from the lid Hall switch (E5). At 30 mm the field is ≈ 4 mT, which is near a
  switch's operate point.
- **PAM8302 mounts at the speaker** (≤ 50 mm of lead), not on board D.
  - Speaker leads short and twisted.
  - The amp gets its own battery pair (as §5b) and a line-level feed from B.
  - Reason: its filterless class-D output edges are the main EMI source; the static magnet field is not.
  - **(Changes architecture-v2 §1/§4.1.)**
- Speaker ≥ 30 mm from the VCO cores (see E8).

**Area:**
- The notch removes ≈ 23 cm² from each of A and B.
- B's usable area falls from ≈ 420 to ≈ 390 cm² against ≈ 370 cm² needed (v2 §4.1).
- Slack drops from ≈ 12 % to ≈ 5 %: **tight but acceptable.**
- The VCO block is laid out first. If it overruns, take the depth fallback.

**Drivers (40 mm):**
- **In a 28 mm notch (SLAB, DOCK, MOTTO):** 20–21 mm-deep Nd drivers fit.
  - [CUI CMS-4021-34SP-X5](https://www.digikey.com/en/products/detail/same-sky-formerly-cui-devices/CMS-4021-34SP-X5/18742615):
    4 Ω, 3 W, Fs 180 Hz, 85 dBA @ 1 W/0.5 m, 21 mm deep.
  - [Adafruit 3968](https://www.digikey.co.uk/en/products/detail/adafruit-industries-llc/3968/9745251):
    4 Ω, 3 W, 20 mm deep.
  - [PUI AS04004PR-R](https://www.mouser.com/datasheet/2/334/AS04004PR-R-270443.pdf): 4 Ω, 3 W, Fs ≈ 180–199 Hz, 86 dBA, Nd.
- **Volume:** the PAM8302 into 4 Ω from a 3.0–4.2 V battery gives ≤ ≈ 1.7 W (v2 §5b).
- **Bass:** in a 40–60 cm³ sealed chamber, the box resonance rises well above Fs. "Incredible" bass is
  not on offer from any 40 mm driver; expect a clear mid-forward sound. The Thiele-Small Vas needed to
  compute it is UNVERIFIED.

**Verify:**
1. **Magnetic:** log every key's raw ADC at rest and bottomed:
   - with the speaker removed;
   - fitted and silent;
   - fitted and driven with a full-power 20 Hz–20 kHz sweep.

   Pass: rest shift < 3 % of each key's span; dynamic ripple < 0.5 %; zero false note-ons. Optional: a
   FEMM axisymmetric model of the chosen driver's motor.
2. **EMI:** FFT of the main out with the speaker driven, compared with the speaker muted. Pass: no
   class-D spurs above −90 dBFS in band.
3. **Acoustic:** phone/measurement-mic sweep in the real chamber.

---

## E3. One rear USB-C: charging + USB-MIDI + firmware

**Answer: yes, with a plain USB-C breakout. Charging while USB-MIDI runs on the same port is feasible**,
because in USB 2.0 device mode power (VBUS) and data (D±) are independent. A PD or hub module is not needed.

**Recommended wiring (all ready-made + wire):**
- **Port:** an Adafruit USB-C breakout, downstream (#4090), on board A's rear edge.
  - $3.45, 20.4 × 14.2 × 5 mm.
  - Breaks out VBUS, GND, D+, D−.
  - **5.1 k Rd on CC**, so C-to-C chargers and laptops turn on 5 V ([PiShop](https://www.pishop.us/product/adafruit-usb-type-c-breakout-board-downstream-connection/)).
- **VBUS → bq24074 board's DC/VBUS input.** The board takes 5–10 V on USB or DC, and uses the higher if
  both are present ([Adafruit](https://www.adafruit.com/product/4755); [learn guide](https://learn.adafruit.com/adafruit-bq24074-universal-usb-dc-solar-charger-breakout?view=all)).
  The charger's own USB-C stays unused, inside.
- **D+/D− → Pico 2 TP3/TP2, with TP1 as the "close coupled ground for differential USB signals".**
  The Pico 2 datasheet: "TP1, TP2 and TP3 can be used to access the USB signals instead of using the
  micro-USB port" ([Pico 2 datasheet](https://pip-assets.raspberrypi.com/categories/1005-raspberry-pi-pico-2/documents/RP-008299-DS-3-pico-2-datasheet.pdf)).
  - Use a twisted pair plus ground, ≤ 20 cm. Full-speed (12 Mb/s) tolerates that easily [ENG].
  - The pads are on the underside of the socketed Pico; solder wires to them before socketing. Large
    pads, no SMD parts.
- **Do NOT connect the breakout's VBUS to the Pico's VBUS pin.** It would power the Pico (via its onboard
  Schottky) while the rest of the system is off, back-powering the I²C DACs.
  - The Pico stays fed only from the MiniBoost into VSYS through a Schottky, as the datasheet
    recommends for a second source.
  - USB device mode does not need VBUS sense on GPIO24: the SDK's TinyUSB forces VBUS-detect (UNVERIFIED,
    check on the bench).
- **Firmware:**
  - **Normal update:** hold TUNE at power-on → firmware calls the ROM USB bootloader → UF2 drag-and-drop.
  - **Recovery:** TP6 is BOOTSEL ("shorting it low at power-up enters USB mass-storage programming mode",
    [datasheet](https://pip-assets.raspberrypi.com/categories/1005-raspberry-pi-pico-2/documents/RP-008299-DS-3-pico-2-datasheet.pdf)).
    Wire it to a through-hole tact switch behind a pinhole, so a bad firmware can never brick the unit.

**Charging current vs the host port [ENG]:**
- The bq24074 board's default input limit is set by a 1 k ILIM resistor (≈ 1.5 A per the TI
  K_ILIM/R_ILIM relation; exact K UNVERIFIED). Default charge current is 1 A (jumpers for 0.5/1.5 A)
  ([Adafruit](https://www.adafruit.com/product/4755)).
- **USB-C hosts and chargers** usually advertise 1.5 or 3 A on CC: fine.
- **An old USB-A port via an A-to-C cable** is nominally 500 mA. The bq24074 backs off when VBUS dips
  below ≈ 4.5 V ([Adafruit](https://www.adafruit.com/product/4755)), so it self-limits on most ports.
  A host with a hard 500 mA trip could still drop the port, and MIDI with it.
- **Option (+$1, recommended):**
  - An LM393 (DIP-8) senses CC voltage: > 0.66 V means a 1.5/3 A source.
  - The bq24074's EN1/EN2 move from solder jumpers to 2 GPIOs: 500 mA mode on a default-power port,
    ILIM mode otherwise.
  - Whether EN1/EN2 have usable pads on the Adafruit board is UNVERIFIED (the guide calls them solder
    jumpers). The fallback is CE (exposed, active-low): pause charging when enumerated on a default-power port.
- **Net power:** on a 500 mA laptop port (2.5 W) while playing (≈ 4.3 W typical, v2 §5b) the battery
  still drains, about 2.4× slower. On a ≥ 1.5 A source it charges while playing (v2 §6 behaviour unchanged).

**Options rejected:**
- **USB-PD trigger (HUSB238) on the one port:** the bq24074 accepts up to 10 V, but it is linear. At 9 V
  and 1 A it would dissipate ≈ 5 W. PD only helps via v2 §5b.5's 12 V analog path, which needs more parts.
- **USB hub module:** only useful if the key Pico also needs USB (E4 option b). Otherwise it adds cost,
  power and an IC with no benefit.
- **Panel USB-C-female to micro-B-male cable into the Pico:** such adapters are non-compliant and often
  lack Rd, so C-to-C chargers give 0 V. VBUS would also have to come back out of the Pico's own traces at
  1.5 A (UNVERIFIED rating).

**Ground loop:** unchanged from v1 R29. The laptop ground joins the instrument ground on this one port.
A USB isolator *module* fixes hum but passes little power, so **with an isolator, charge from a wall
charger instead.** Document it.

**ESD:** the breakout has no stated ESD protection, and D± go straight to the RP2350.
- Mitigation: tie the connector shell to the ground star at the jack panel.
- A through-hole USB TVS is hard to find (UNVERIFIED).
- Risk L–M.

**LAYOUT CONSTRAINTS (E3):**
- The USB-C breakout sits on the rear edge (≈ 21 × 15 mm footprint plus the receptacle opening).
- A ≤ 20 cm twisted-pair run from it to the main Pico on D, and a ≥ 22 AWG VBUS/GND pair to the charger.
- A pinhole for the recovery button somewhere reachable; the location is the design team's choice.

**Cost:** breakout $3.45 + recovery switch $0.3 + wire + optional LM393/passives $1 → **+$4–6**.

**Verify (bench, no SPICE needed):**
1. Enumerate as USB-MIDI on macOS, Windows and Linux while charging: C-to-C from laptop, A-to-C from an
   old port, wall charger.
2. USB power meter: VBUS current ≤ the port's advertisement. On a 500 mA port, confirm VIN-DPM
   (or the CC-sense option) keeps it there without the port dropping.
3. 1 h bidirectional MIDI flood while charging at full rate: no drops.
4. Hold TUNE and press the pinhole: both reach the UF2 drive.
5. Hum at the main out with a laptop on its charger: compare with battery-only.

---

## E4. How the key Pico (and any other slave MCU) gets firmware

**Answer:**
- **Fixed-body concepts (SLAB, MOTTO):** the main Pico reflashes the key Pico over **SWD**.
  - Wire the key Pico's 3-pin debug header (SWCLK, SWDIO, GND) to 2 main-Pico GPIOs. The Pico 2 has a
    "3 pin debug header on the lower edge" ([datasheet](https://pip-assets.raspberrypi.com/categories/1005-raspberry-pi-pico-2/documents/RP-008299-DS-3-pico-2-datasheet.pdf)).
  - The main image carries the key image. At boot the key Pico reports its version over UART; on a
    mismatch the main Pico reflashes it.
  - SWD is hardware-level, so it cannot be bricked.
  - Cost $0. Firmware effort: an SWD host plus an RP2350 flash routine on the main Pico. Raspberry Pi's
    debugprobe has PIO SWD code; a ready standalone flasher library is UNVERIFIED.
- **MCUs across a joint (DOCK's key Pico in the module, DISH's dish MCU):** only V, GND, TX and RX
  cross, so SWD is out. Use a **UART update into a second flash slot**: the running image receives the
  new image over the existing UART, writes the inactive slot and reboots.
  - The RP2350 bootrom supports partition tables with A/B images and "try before you buy" rollback
    (from memory of the RP2350 datasheet's bootrom chapter: **UNVERIFIED this session**).
  - If that holds, a bad image falls back automatically.
  - **This requires the slave MCUs to be RP2350 boards** (Pico 2, or a smaller RP2350 module), not RP2040.
  - Last-resort recovery: open the module, use its micro-USB.
- **Option b, not recommended:** a USB hub module puts both Picos on the rear USB-C. It is simpler
  firmware, but costs ≈ $5–8 and adds power, and the second USB device confuses users.

**Verify:**
- Pull power mid-update 20 times; the unit must come up working every time.
- Bad-image test: flash a deliberately crashing key image and check the fallback.

---

## E5. Unipolar TO-92 Hall switch for SLAB's lid

**Answer: yes, the TI DRV5023** is a **unipolar** Hall switch in **TO-92-3**, open-drain, active status
([Digi-Key DRV5023AJQLPG](https://www.digikey.co.uk/en/products/detail/texas-instruments/DRV5023AJQLPG/5031904)).
It responds to one pole only, so the lid folded under (opposite pole) cannot trip sleep.
- DRV5032 TO-92 availability is not needed.
- Supply 2.5–38 V and ≈ 2.7 mA (UNVERIFIED, from memory of the datasheet), so it runs straight from the battery.

**Power gating [ENG]:**
- Always-on, 2.7 mA would drain the 18.5 Wh pack in ≈ 2½ months of storage (with the master switch on).
- Gate its supply with a 2N7000/BJT from a Pico GPIO in sleep: sample for 100 µs every 100 ms (power-on
  time tens of µs, UNVERIFIED). That gives ≈ 3 µA average.
- This needs the main Pico in a timed dormant state. Sleep current of the MiniBoost + Pico is the larger
  term; measure it.

**LAYOUT CONSTRAINT (E5):**
- ≥ 50 mm from the speaker magnet and from any key magnet's travel.
- The lid magnet's chosen pole faces the sensor's marked face when closed.

**Cost:** +$1–2. **Risk:** L.

**Verify:** closed → sleep; folded under → stays awake; speaker at full volume → no trip; Gauss margin
measured with the sensor's output at 2× and 0.5× the design gap.

---

## E6. DOCK: board D as a strip, battery in the module, VBAT over pogo pins

**Battery in the module, VBAT over pogo: yes, with changes.**
- **Pins:**
  - Mill-Max's 0906 spring pins are rated **2 A continuous, 3 A peak, 20 mΩ max**, but they are SMT
    ([Mouser](https://www.mouser.com/new/mill-max/millmax_0900_0906/)).
  - Pick a **through-hole** spring pin of ≥ 2 A. Mill-Max offers through-hole families; the exact part
    is UNVERIFIED.
  - Worst case 2.9 A (v2 §5b) with the ≥ 40 % margin rule means ≤ 1.2 A per 2 A pin, so use **3 VBAT + 3 GND**
    (0.97 A each, 48 % use), not 2 + 2.
  - Drop at 2.9 A: ≈ 2 × (20 mΩ / 3) × 2.9 ≈ 40 mV. Acceptable.
- **DETECT:** a shorter pin (last-make, first-break) gating a module P-MOSFET. Agree with DOCK's design.
  Undocking under load then opens the MOSFET before the power pins break. Verify the timing with a scope.
- **Thermistor:** the bq24074's THERM input needs the cells' NTC. Either add a 7th signal pin, or keep the
  board's fixed resistor and lose cell-temperature protection while charging. **Recommend the extra pin.**
  The cells must be protected cells either way.
- **Inrush on docking:** the body's soft-start (v2 §5b.3) sits downstream of the pogo face, so it covers it.

**Board D as 270 × 26 or 270 × 30, single row: does not fit [ENG].**
- The key Pico moves to the module, but the strip still holds:
  - Pico 2 (51 mm long, [datasheet](https://pip-assets.raspberrypi.com/categories/1005-raspberry-pi-pico-2/documents/RP-008299-DS-3-pico-2-datasheet.pdf));
  - 3 × AD5693R + 2 × MCP4728 (≈ 17.8 mm each along the strip, UNVERIFIED);
  - bq24074 (≈ 40 mm, UNVERIFIED);
  - DCWN06A (DIP-24, ≈ 32 × 20);
  - U3V40F12 (15 mm, [Pololu](https://www.pololu.com/product/4016/specs));
  - MiniBoost, LC filter, soft-start;
  - optional ADS1115.
- That is ≈ 290–310 mm with gaps (PAM8302 already moved to the speaker, E2).
- **Options:**
  - (a) **≈ 300 × 30**;
  - (b) **270 × 40** (two partial rows);
  - (c) 270 × 30 with the DACs stacked one tier over the Pico (digital over digital, ≈ +12 mm height),
    if the body height allows.
- 26 mm is too narrow for the DACs across (25.4 mm boards plus sockets).

**LAYOUT CONSTRAINTS (E6):**
- Converters (U3V40F12, DCWN06A: ≈ 1.5 W of heat in total) at the strip end **farthest from the VCO
  cores**, ≥ 60 mm away.
- The DAC end nearest B, so the CV ribbon is short.
- In DOCK the strip is adjacent to the voice, not "under the keys away from B". Autotune and the NTC
  re-tune cover slow drift, but keep the separation.

**Cost:** 2 more pogo pins + NTC pin ≈ +$3–6; larger D strip area ≈ +$2–4. So **+$5–10** on DOCK's own +$15–25.

**Verify:**
- Thermal: run 1 h at worst-case load and log VCO drift with the strip at each end.
- Docking: 500 dock/undock cycles under load, measuring contact resistance.
- Scope the DETECT-first break.

---

## E7. DISH: dish MCU, low-profile B under the well, ≤ 12 mm 40 mm driver

**Dish MCU: yes.**
- A Pico 2 (51 × 21 mm) or a smaller RP2350 module (an RP2350 is needed for the E4 update scheme) plus
  1 × CD74HC4067 reads the 14 dish controls (16 channels).
- **Link:** 5 V + GND + TX/RX through the hollow pivots, UART at 1 Mbaud with 100–220 Ω series resistors
  at both ends.
  - Bandwidth: 14 × 12 bit × 1 kHz ≈ 28 kB/s, well inside a 1 Mbaud link (≈ 100 kB/s).
  - Added latency ≈ 1–2 ms: inaudible for knobs.
- **Wire:** use finely stranded silicone wire through the pivots; ≈ 90° of rotation is gentle, but test
  flex life.
- The dish-lost behaviour in DISH's spec is easy in firmware.

**Low-profile B extension (≤ 8 mm components): yes, with rules [ENG]:**
- **Fits:**
  - unsocketed DIPs (≈ 4–5 mm) or low-profile sockets;
  - 1/4 W resistors;
  - TO-92 seated low;
  - film caps up to ≈ 0.1 µF in 5 mm-pitch boxes (≈ 6.5–8 mm tall; check each value);
  - radial electrolytics in 5 mm-height series (UNVERIFIED part series);
  - TO-220 regulators laid flat.
- **Put there:** mixer bus, noise source and filters, mod-mix amp and the E1 VCA, output/phones stage,
  logic.
- **Keep on full-height B:**
  - VCO cores (multi-turn trimmers ≈ 10 mm tall, matched pairs, tempcos, thermal coupling);
  - ladder;
  - contours (large timing caps).
- **LAYOUT CONSTRAINT (E7):** the extension joins main B rigidly (headers in the same body). No signal
  of B crosses the dish pivot.

**≤ 12 mm-deep 40 mm driver: yes.**
- **PUI AS04008MR-2-LWC80**, 40 × **5 mm**, 8 Ω, 2 W, Fs 400 Hz, 92 dB SPL @ 0.1 W/0.1 m ([RS](https://uk.rs-online.com/web/p/miniature-speakers/0807262)).
- The PAM8302 into 8 Ω from the battery gives ≈ 1 W max [ENG].
- Bass is the weakest of the four concepts (Fs 400 Hz), as DISH already notes.

**Risk:** M–H on board area (DISH's own estimate: short ≈ 7,000 mm², low-profile zone ≈ 6,500 mm²).
Lay out the VCO block first; the fallback is +15 mm of depth.

**Verify:** a component-height check in KiCad 3D against a 13 mm keep-out; a UART error-rate test with
the dish swung through its range 1,000 times.

---

## E8. MOTTO: speaker over the left B board (VCO proximity)

**Answer: acceptable with conditions.**

The speaker's **static** field does nothing to BJT expo pairs or tempcos at mT levels [ENG]. The voice
coil's AC field induces only ≈ 10 µV in a 1 cm² loop at 30 mm. Through the expo summing node that is
≈ 0.01 cent: negligible.

The real couplings:
1. the class-D output edges (E-field from the speaker leads into high-impedance VCO nodes: the timing
   cap and the expo summing node, where 1 mV ≈ 1.2 cents);
2. microphonics from the panel and chamber vibrating the VCO timing caps.

**LAYOUT CONSTRAINTS (E8):**
- VCO cores ≥ 30 mm from the speaker frame. Design's proposal (VCO cores at the front-right of the left
  B board) satisfies this.
- The PAM8302 at the speaker, leads ≤ 50 mm and twisted (as E2).
- A ground pour under the VCO cores.
- The speaker chamber is mechanically isolated (foam gasket) from board B.
- No speaker lead runs over the VCO area.

**Cost:** $0–2 (gasket, ferrite). **Risk:** L–M.

**Verify:**
- VCO pitch logged at 3 notes with the speaker at full volume (pink noise) and muted. Pass: shift
  < 0.1 cent; spurs < −90 dBFS.
- A knock test on the case near the speaker.

---

## E9. Dual-gang pots so knob-only controls send CC

**Answer: feasible; I recommend not doing it** (agreeing with design). Owner question stands.

**How:**
- The second gang is wired as a divider across 3.3 V into a 3rd CD74HC4067. The audio gang is untouched.
- The 8 pots: EMPHASIS, mixer ×5, MOD MIX, CONTOUR AMOUNT. (The mod wheel is already covered by E1.)
- Waveform rotaries need a second deck with a resistor ladder.
- Toggles send CC from a spare DPDT pole into GPIO.

**Parts:**
- Alpha 9 mm vertical dual-gang is stocked, but only in **10 k / 50 k / 100 k / 1 M**
  ([Thonk](https://www.thonk.co.uk/shop/alpha-9mm-pots-vert-t18-dual-gang/), £1.99, UK).
- US listings: [Tubes and More](https://www.tubesandmore.com/node/45342/ask).
- The circuit gang must keep the original values (25 k mixer, 5 k contour amount, etc.). **Dual-gang in
  those values is UNVERIFIED and probably special-order.** Using a different value changes the passive
  mixer's Thevenin impedance and the overdrive character that v2 keeps.

**LAYOUT CONSTRAINT (if adopted):**
- A dual-gang vertical body stacks a second deck along the shaft: ≈ +5 mm of pot body height (UNVERIFIED;
  read the datasheet).
- That raises the control section from 28–32 to ≈ 33–37 mm for the whole panel board A, or needs a
  stepped board A.

**Cost:** ≈ +$1.5–2.5 per pot × 8, plus a 4067, plus wiring → **+$15–25**.
**Risk:** M (values, height).

**Verify:** CC output monotonic and within ±3 % of travel. THD-vs-level of the mixer unchanged (±1 dB vs
golden, v1 §7.2).

---

## E10. Strip C with footprints at all 25 key x-positions (K6 populates 15)

**Answer: yes.**
- Strip C gets 25 TO-92 footprints on 2 × CD74HC4067 (32 channels, 7 spare).
- Unpopulated channels get a 100 k pull-down footprint, and a firmware "key-layout" setting masks them.
- **K6 rockers:** each rocker's magnet sits off-centre, so a linear sensor sees signed travel about a mid-field
  rest. Choose magnet and gap so both tilts stay inside the sensor's linear range. That is a mechanism-CAD item.

**LAYOUT CONSTRAINT (E10):**
- Footprint centres ≥ **6.5 mm** apart along the line: TO-92 body ≈ 4.8 mm plus clearance, leads at 2.54 mm.
- **Case 1:** both key layouts put natural sensors at natural-key centres (17.4 mm pitch) and sharps
  near the natural boundaries (≈ 8.7 mm from a natural centre). Then K6's 15 positions are a subset of
  the 25 and one line works.
- **Case 2:** a layout uses uniform semitone spacing (121.8 / 12 ≈ 10.15 mm). Then K6's natural-centre
  positions fall as close as ≈ 3 mm to semitone positions. Either:
  - put K6's 15 on a **second parallel row offset ≥ 6 mm** (strip C grows from 15 to ≈ 22 mm wide); or
  - move K6's magnet arm to reach the semitone x.
- Design gives the final x-coordinates.

**Cost:** ≈ $0–1 (pull-down resistors). **Risk:** L.

**Verify:** KiCad DRC on the footprint set. Firmware test of each layout mask with populated and
unpopulated channels: no ghost notes from floating inputs.

---

## Sources (this session)
- Raspberry Pi Pico 2 datasheet (test pads, VSYS Schottky, SWD, size): https://pip-assets.raspberrypi.com/categories/1005-raspberry-pi-pico-2/documents/RP-008299-DS-3-pico-2-datasheet.pdf
- Adafruit bq24074 #4755 product page and learn guide: https://www.adafruit.com/product/4755 · https://learn.adafruit.com/adafruit-bq24074-universal-usb-dc-solar-charger-breakout?view=all
- Adafruit USB-C breakout #4090 (PiShop): https://www.pishop.us/product/adafruit-usb-type-c-breakout-board-downstream-connection/
- OTA availability (synthDIY), Tayda LM13700N: https://wiki.synthdiy.com/parts/otas · https://www.taydaelectronics.com/ic-integrated-circuits/lm13700-lm13700n-operational-amplifier-ic.html
- AS3360: https://www.tubesandmore.com/products/integrated-circuit-as3360-dual-vca-alfa-14-pin-dip · https://electricdruid.net/?p=2517
- Speakers: https://www.digikey.com/en/products/detail/same-sky-formerly-cui-devices/CMS-4021-34SP-X5/18742615 · https://www.digikey.co.uk/en/products/detail/adafruit-industries-llc/3968/9745251 · https://www.mouser.com/datasheet/2/334/AS04004PR-R-270443.pdf · https://uk.rs-online.com/web/p/miniature-speakers/0807262
- DRV5023 (Digi-Key): https://www.digikey.co.uk/en/products/detail/texas-instruments/DRV5023AJQLPG/5031904
- Mill-Max spring pins: https://www.mouser.com/new/mill-max/millmax_0900_0906/
- Pololu U3V40F12: https://www.pololu.com/product/4016/specs
- Alpha 9 mm dual-gang: https://www.thonk.co.uk/shop/alpha-9mm-pots-vert-t18-dual-gang/ · https://www.tubesandmore.com/node/45342/ask
