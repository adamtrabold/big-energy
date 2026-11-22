# floss: requirements (draft rev 0, 2026-11-22)

Status: **rev 2 (2026-11-22 12:26): floss is a keyless sound module played by a carried travel controller.** Rev 1, targets confirmed as the baseline (2026-11-22 09:38).** Adam: "Sure but if we can do better or need to do worse tradeoffs should be discussed": any target we could beat or must miss comes to him as a trade-off. "Decided" lines are Adam's (verbatim record in `design/owner.md`). "Proposed" lines are targets for him to confirm or change; engineering designs against whatever he confirms.

## Family principle (Adam, 2026-11-22 12:28)
"This is the plan for all modular portable synths that we build — portable sound modules with a way to carry a keyboard with it. It should be flexible and not reliant on a single model of keyboard."

## What it must do (decided)
- Analog voices, shimmer and warmth; a portable string machine.
- **No built-in keys (rev 2).** floss is a sound module played by a travel MIDI controller over USB; floss is the USB host and powers it. It's designed so the controller can be carried with it.
- Split with independent octave select per half, done in floss's firmware and panel for any controller (the 25-key limit now applies to the controller floss is carried with).
- Velocity, used to innovate on the classic string machine.
- Pressure that's selectable in what it does. Per-key pressure comes from the controller (polyphonic aftertouch / MPE), with a fallback to channel pressure.
- Battery powered; one built-in speaker, muted by headphones; look into a passive radiator.
- Shimmer: an analog mode plus Daisy modes; echo and reverb on the Daisy.
- MIDI: Big Energy's rules, a MIDI split you can switch on or off, velocity and pressure over MIDI.
- No screens or encoders; real knobs and keys.
- A shared universe with Big Energy: reuse as much as possible.
- Reliable choices: proven parts and approaches, no experiments. Adam measures nothing; choices rest on published evidence.
- SMD is fine where necessary.
- No fixed budget ceiling; everything costed.

## Measurable targets (proposed, to confirm)
| # | Target | Proposed | Why |
|---|---|---|---|
| T1 | Notes at once | All 25 keys sound together | String machines are fully polyphonic |
| T2 | Battery life | ≥ 4 h playing on the speaker at moderate volume | An afternoon in the park |
| T3 | Charging | Plays while charging; full in ≤ 4 h over USB-C | As Big Energy |
| T4 | Size | **Module: ideally no longer than a sheet of paper's long side (279–297 mm), not necessarily rectangular, proportions from a deliberate ratio. Kit (module + travel keyboard) fits comfortably in a backpack.** (Adam, 13:29; the module need not match keyboard width, 13:25) | Backpack portable |
| T5 | Weight | ≤ 1.5 kg | Carry it in a bag all day |
| T6 | Key to sound | ≤ 5 ms from the controller over USB | Feels instant (rules out BLE for now) |
| T7 | Hiss, dry path | Output noise ≥ 80 dB below full level (A-weighted) | Quiet on headphones |
| T8 | Hiss, analog ensemble | ≥ 70 dB below full level | Classic bucket-brigade range; some character allowed |
| T9 | Tuning | TUNE trim; holds pitch within ±3 cents once warm (any drift is a deliberate feature, not instability) | Plays with other instruments |
| T10 | Parts | Everything in stock from mainstream distributors; no vintage-only chips | Buildable and repairable |
| T11 | Build | Hand-assembled where reasonable; SMD parts or factory-assembled boards where they're the better choice | Adam: "Surface mount is fine if necessary" |
| T12 | Outputs | Stereo headphone/line out; USB-C (power + MIDI); USB host port for the controller; 3.5 mm TRS MIDI in and out | As Big Energy, plus stereo and the controller port |
