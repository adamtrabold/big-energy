# Firmware update and gestures
Status: **partly written 2026-11-13** (the TAP gesture split, review must-fix O5). The rest is to be written · sources: ../../eng/daisy-first-principles.md §2.4, §3.2, §5.3, §7.3; review item 6

## What it does (player's view)
_To be written._

## Owner decisions (verbatim, linked to owner.md)
_To be written._

## How it works
_To be written._

## Controls and states
### Gestures, split so none collides (review must-fix, architecture open item 5)
**The collisions found:**
- "hold TAP at power-on" meant **both** full autotune and the **bootloader (DFU)**;
- "EMPHASIS full + hold TAP" ran the filter calibration **live**, and EMPHASIS full is a normal playing position;
- "hold TAP" also queried the battery.

| Gesture | Does | When | Status |
|---|---|---|---|
| **Hold TAP while switching on** | full autotune re-sweep (normally a 0.3 s verify runs instead) | power-on | proposed (keeps eng's gesture) |
| **Hold TAP + hold the bend stick fully up while switching on** | **bootloader (firmware update over USB)**; status light alternates red / green | power-on | proposed. Hard to do by accident. Fallback: the Seed's own BOOT button behind the service panel |
| **EMPHASIS fully up + hold TAP while switching on** | filter-scale calibration | **power-on only** (never live) | proposed |
| **Hold TAP ≥ 1.5 s while playing** | battery level on the status light (that press doesn't count as a tempo tap) | live | proposed |
| Battery level | also flashed once on the status light right after "ready" at power-on | power-on | proposed |
| **Hold the lowest key while switching on**, then a key | MIDI channel (keys 1–16), omni (key 17); MIDI extras (see [MIDI](midi.md)) | power-on | proposed |
| **Hold the highest key while switching on**, then a key | feel settings: velocity curve (keys 1–5), aftertouch span (keys 6–10) | power-on | proposed |
| TAP taps (2–4) | tempo (or echo length in FREE): see [echo sync](echo-sync.md) | live | decided feature (option B); timing proposed |

- Every power-on gesture is checked once at boot. Live, TAP only taps or (held) shows the battery.
- Settings live in flash.

## Edge cases
_To be written._

## Interactions with other features
_To be written._

## MIDI
_To be written._

## Budget (pins / mux / DAC / power / cost)
_To be written._

## Open questions
_To be written._

## Status (decided / proposed / open, item by item)
_To be written._
