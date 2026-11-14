# Firmware update and gestures
Status: per item below · last updated 2026-11-13 · sources: [eng/daisy-first-principles.md](../../eng/daisy-first-principles.md) §2.4, §3.2, §5.2–5.3, §7.3, §8; [audio / synth review](../../design/reviews/2026-11-13-audio-synth-review.md) item 6; [owner.md](../../design/owner.md) (paraphonic firmware entry)

Panel words follow the one-word vocabulary: **tap** (under "tempo"), **resonance**, the **status** light, **bend**.

## What it does (player's view)
- **The instrument's brain is updatable.** New firmware goes in through the same rear USB-C you charge from: hold **tap** and push the **bend** stick fully up while switching on, and it waits for an update from a computer. Firmware can improve behaviour over time (paraphonic allocation, effects, settings) without opening the case.
- **Everything else you set by hand at power-on:** hold a key while switching on, then press another key to pick a setting. The MIDI channel uses the lowest key, the feel settings use the highest key. Settings stay through power-off.
- **While playing**, the only gesture is on **tap**: tap it for tempo, hold it for the battery level.

## Owner decisions (verbatim, linked to owner.md)
- "yeah so firmware could even improve the paraphonic control over time right?" → yes (USB-C firmware updates). Recorded as: **firmware is updatable and expected to evolve.**
- Base spec: "MIDI never flips switches" (so no setting changes a panel switch's meaning behind your back).
- "am i missing a control to turn that tempo sync on / off?" → the FREE / SYNC switch, option B ([echo sync](echo-sync.md)).

## How it works
- **Update path:** the rear USB-C's data lines go to the **Daisy Seed's own USB port** through a cut cable (its VBUS isn't connected; the Seed runs from the main supply). At the update gesture, the firmware resets into the bootloader (libDaisy reset-to-bootloader), and the computer flashes it over USB with a standard DFU tool (DFP §5.3). Whether the STM32's ROM DFU is reachable on that port is **UNVERIFIED** (check AN2606); the fallback is the Seed's own BOOT button behind the service panel.
- **Gesture reading:** every power-on gesture is checked once, at boot, before the voice starts. TAP is a mux channel with a pull-up and 5 ms debounce (DFP §3.2).
- **What's kept in flash (the Seed's QSPI):** the autotune tables (so boot only verifies, ≈ 0.3 s), the key calibration, and the settings below (DFP §8).
- **The status light** is the only display. Its patterns are shared: tune-failed and low-battery always win (echo-sync status table).

## Controls and states
### Gestures, split so none collides (review must-fix, architecture open item 5)
**The collisions found:**
- "hold TAP at power-on" meant **both** full autotune and the **bootloader (DFU)**;
- "**resonance** full + hold TAP" ran the filter calibration **live**, and **resonance** full is a normal playing position;
- "hold TAP" also queried the battery.

| Gesture | Does | When | Status |
|---|---|---|---|
| **Hold TAP while switching on** | full autotune re-sweep (normally a 0.3 s verify runs instead) | power-on | proposed (keeps eng's gesture) |
| **Hold TAP + hold the bend stick fully up while switching on** | **bootloader (firmware update over USB)**; status light alternates red / green | power-on | proposed. Hard to do by accident. Fallback: the Seed's own BOOT button behind the service panel |
| ****resonance** fully up + hold TAP while switching on** | filter-scale calibration | **power-on only** (never live) | proposed |
| **Hold TAP ≥ 1.5 s while playing** | battery level on the status light (that press doesn't count as a tempo tap) | live | proposed |
| Battery level | also flashed once on the status light right after "ready" at power-on | power-on | proposed |
| **Hold the lowest key while switching on**, then a key | MIDI channel (keys 1–16), omni (key 17); MIDI extras (see [MIDI](midi.md)) | power-on | proposed |
| **Hold the highest key while switching on**, then a key | feel and play settings: velocity curve (keys 1–5), aftertouch span (keys 6–10), **filter note in chords: highest (11) / lowest (12)**, **bend range ± 2 / ± 7 / ± 12 (keys 13–15)**, **pressure out on / off (16)** | power-on | proposed (11–16 new) |
| **tap** taps (2–4) | tempo (or echo length in FREE): see [echo sync](echo-sync.md) | live | decided feature (option B); timing proposed |

- Every power-on gesture is checked once at boot. Live, TAP only taps or (held) shows the battery.
- Settings live in flash.


### The status light (one light, by priority)
| Pattern | Means | From |
|---|---|---|
| blinks *n* times, repeating | VCO *n* failed to tune: power-cycle; if it repeats, service | jobs F1 |
| low-battery warning / flashing near empty | battery | [power and battery](power-and-battery.md) |
| red / green alternating | bootloader, waiting for an update | this doc |
| the battery level | after "ready" at power-on, or tap held ≥ 1.5 s | this doc |
| 4 green flashes at the tempo · 2 green · 2 amber · 1 short amber | tap tempo set · clock locked · clock lost · tap ignored | [echo sync](echo-sync.md) |

The **midi** light beside it is separate: it lights when MIDI holds a knob ([MIDI](midi.md)).

## Edge cases
- **A gesture held by accident at power-on:** the bootloader needs two hands' worth (tap **and** the stick up), so it can't happen by resting a hand. Full autotune (tap alone) is harmless; it just takes 2–4 s longer.
- **Power lost mid-update:** the bootloader is in ROM / the Seed's own loader, so the board can be re-flashed. Settings and tables are in a separate flash area and survive (proposed; eng confirms the flash layout).
- **A setting gesture with no second key:** release the held key with no other key, and nothing changes; the instrument starts normally.
- **Filter calibration needs quiet:** resonance fully up at power-on runs it; nobody should turn cutoff during that second (eng §3).
- **Settings after an update:** kept, unless the new firmware changes their layout. Then it says so on the status light (one long amber) and uses defaults (proposed).

## Interactions with other features
- **Echo sync:** tap's tempo and the status light patterns ([echo sync](echo-sync.md)).
- **Power and battery:** the battery query and level flash ([power and battery](power-and-battery.md)).
- **Keys and velocity / aftertouch:** the curve and span settings ([keys and velocity](keys-and-velocity.md), [aftertouch](aftertouch.md)).
- **Paraphonic:** the "filter note in chords" setting (keys 11 / 12; owner question 10) ([paraphonic](paraphonic.md)).
- **Bend and mod:** the stick is half of the update gesture; the bend range setting (keys 13–15; owner question 8) ([bend and mod](bend-and-mod.md)).
- **MIDI:** channel / omni and the extras ([MIDI](midi.md)).

## MIDI
- Settings aren't reachable by MIDI (no SysEx; [MIDI](midi.md) lists it as not proposed).
- A firmware update uses USB, not MIDI.

## Budget (pins / mux / DAC / power / cost)
- **Pins:** 0 extra. The update runs on the Seed's own USB port (D29 / D30 stay free); tap is a mux channel.
- **Flash:** tables and settings in the Seed's QSPI.
- **Cost:** $0 beyond the USB breakout already counted (Adafruit #4090, $3.45).

## Open questions
1. **ROM DFU on the Seed's port without VBUS** on its connector: bench check (DFP U1 risk). If needed, feed the Seed's VBUS from the breakout through a Schottky diode.
2. **Settings keys 11–16** (filter note in chords, bend range, pressure out): proposed here; they follow owner questions 8 and 10.

## Status (decided / proposed / open, item by item)
| Item | Status |
|---|---|
| Firmware updatable over USB-C, expected to evolve | decided |
| TAP's echo role (taps; FREE / SYNC option B) | decided (feature) |
| Update via the rear USB-C → the Seed's port; tap + bend up at power-on | proposed |
| The gesture split (full autotune, update, filter cal, battery, settings) | proposed (review must-fix O5) |
| Settings keys 11–16 | proposed |
| Status light priorities | proposed |
| ROM DFU without VBUS on the Seed connector | open (bench) |
