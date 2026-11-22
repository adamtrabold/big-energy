# floss: requirements (draft rev 0, 2026-11-22)

Status: **draft for Adam to confirm.** "Decided" lines are Adam's (verbatim record in `design/owner.md`). "Proposed" lines are targets for him to confirm or change; engineering designs against whatever he confirms.

## What it must do (decided)
- Analog voices, shimmer and warmth; a portable string machine.
- 25 keys or fewer; split with independent octave select per half.
- Velocity, used to innovate on the classic string machine.
- Pressure that's selectable in what it does; per-key pressure if a reliable, proven approach exists.
- Battery powered; one built-in speaker, muted by headphones; look into a passive radiator.
- Shimmer: an analog mode plus Daisy modes; echo and reverb on the Daisy.
- MIDI: Big Energy's rules, a MIDI split you can switch on or off, velocity and pressure over MIDI.
- No screens or encoders; real knobs and keys.
- A shared universe with Big Energy: reuse as much as possible.
- Keys and sensing are reliable choices: proven parts and approaches, no experiments.
- SMD is fine where necessary.
- No fixed budget ceiling; everything costed.

## Measurable targets (proposed, to confirm)
| # | Target | Proposed | Why |
|---|---|---|---|
| T1 | Notes at once | All 25 keys sound together | String machines are fully polyphonic |
| T2 | Battery life | ≥ 4 h playing on the speaker at moderate volume | An afternoon in the park |
| T3 | Charging | Plays while charging; full in ≤ 4 h over USB-C | As Big Energy |
| T4 | Size | No bigger than Big Energy's case family (about 290 × 135 mm footprint) | Shared universe, portable |
| T5 | Weight | ≤ 1.5 kg | Carry it in a bag all day |
| T6 | Key to sound | ≤ 5 ms | Feels instant |
| T7 | Hiss, dry path | Output noise ≥ 80 dB below full level (A-weighted) | Quiet on headphones |
| T8 | Hiss, analog ensemble | ≥ 70 dB below full level | Classic bucket-brigade range; some character allowed |
| T9 | Tuning | TUNE trim; holds pitch within ±3 cents once warm (any drift is a deliberate feature, not instability) | Plays with other instruments |
| T10 | Parts | Everything in stock from mainstream distributors; no vintage-only chips | Buildable and repairable |
| T11 | Build | Hand-assembled where reasonable; SMD parts or factory-assembled boards where they're the better choice | Adam: "Surface mount is fine if necessary" |
| T12 | Outputs | Stereo headphone/line out; USB-C (power + MIDI); 3.5 mm TRS MIDI in and out | As Big Energy, plus stereo for the ensemble |
