# Docs: architecture and feature sets

Owner (2026-11-13 16:21, `../design/owner.md`): "we need on that site architectural documentation and clear docs for each featureset. lets start defining this stuff and writing it down 1 by 1 in an easily delineated fashion, so we can make sure the architectural decisions are sound across the device."

**How these docs work:**
- **`architecture.md`** is the whole device on one page: signal paths, control and data flow, power, **one recounted budget table** (pins, mux, DACs, power), the decisions log and the open items.
- **`features/`** has one file per feature set, all with the **same headings** (template below). They're written one at a time; a stub says "not yet written".
- **Status words are strict.** Only a decision recorded in `../design/owner.md` is **decided**. Anything the team proposes is **proposed** until he answers. Unknowns are **open**.
- Sources are linked, not copied: eng files in `../eng/`, design files in `../design/`.

## Index
| Doc | What it covers | Status |
|---|---|---|
| [architecture.md](architecture.md) | system overview, signal paths, control/data flow, power, budgets, decisions log, open items | started 2026-11-13 |
| [features/voice.md](features/voice.md) | 3 VCOs, mixer, ladder filter, contours, VCA, SOURCE, filter TRACK | **written 2026-11-13** |
| [features/keys-and-velocity.md](features/keys-and-velocity.md) | 25 Choc V2 keys, Hall sensing, velocity, key tops / pegs | **written 2026-11-13** |
| [features/aftertouch.md](features/aftertouch.md) | FSR strip, floating strip C, MOD / OFF / FILTER | **written 2026-11-13** |
| [features/bend-and-mod.md](features/bend-and-mod.md) | bend joystick, MOD knob, mod VCA | **written 2026-11-13** |
| [features/paraphonic.md](features/paraphonic.md) | VOICES 1 / 3 / 4 (mono / para / para+4), allocation, the digital 4th oscillator | **written 2026-11-13** |
| [features/autotune-and-drift.md](features/autotune-and-drift.md) | TIM5 counting, coarse + fine DACs, held-note loop, DRIFT, filter cal | not yet written |
| [features/effects.md](features/effects.md) | echo (4 types), reverb (4 types), wet-only return, send gating | **written 2026-11-13** |
| [features/echo-sync.md](features/echo-sync.md) | FREE / SYNC, TAP, MIDI clock, divisions | **written 2026-11-13** |
| [features/panning-and-stereo-outputs.md](features/panning-and-stereo-outputs.md) | out pan, echo pan, LINK, stereo phones / line, mono-on-TS, speaker sum | **written 2026-11-13** |
| [features/midi.md](features/midi.md) | MIDI in from a DAW or another device; free extras | **written 2026-11-13** |
| [features/power-and-battery.md](features/power-and-battery.md) | LiPo, charger, boost, rails, gauge, runtime, Hall gating | **written 2026-11-13** |
| [features/firmware-update-and-gestures.md](features/firmware-update-and-gestures.md) | DFU, boot gestures, settings gestures, TAP | **written 2026-11-13** |
| [features/io.md](features/io.md) | jacks, USB-C, CV / gate, EXT in, jack switching, mutes | **written 2026-11-13** |
| [features/enclosure.md](features/enclosure.md) | CATHEDRAL / FOLD body, hinge, stays, feet, plates, grille, façade | **written 2026-11-13** (CATHEDRAL) |

## Template (every feature doc uses these headings, in this order)
```
# <Feature set>
Status: decided / proposed / open (per item below) · last updated <date> · sources: <links>

## What it does (player's view)
## Owner decisions (verbatim, linked to owner.md)
## How it works
## Controls and states
## Edge cases
## Interactions with other features
## MIDI
## Budget (pins / mux / DAC / power / cost)
## Open questions
## Status (decided / proposed / open, item by item)
```
