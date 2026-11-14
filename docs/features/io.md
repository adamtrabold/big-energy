# I/O
Status: per item below · last updated 2026-11-13 · sources: [owner.md](../../design/owner.md), [panning and stereo outputs](panning-and-stereo-outputs.md), [MIDI](midi.md), [eng/architecture.md](../../eng/architecture.md) §5, §5b (levels, protection), [eng/daisy-first-principles.md](../../eng/daisy-first-principles.md) §5, [jobs](../../design/jobs.md) (F-flows with cables), [cathedral §6, §14, §15](../../design/branches/concepts/cathedral/how-it-works.md), [audio / synth review](../../design/reviews/2026-11-13-audio-synth-review.md) items 2, 7, 9, 16

## What it does (player's view)
- **Headphones:** stereo, and plugging in mutes the speaker.
- **Line out:** stereo to a mixer, recorder or interface. A plain mono cable still gets the whole sound (how depends on owner question 4).
- **One USB-C** on the back: charging, USB-MIDI to a computer, and firmware updates, all on the one port.
- **MIDI in and out** on 3.5 mm TRS jacks, for other gear.
- **A small set of patch jacks** for a eurorack or another synth: **pitch CV out** and **gate out** (play other gear from these keys), **filter CV in** (move the cutoff from outside), and the **input** that the mixer's **source: input** setting picks up.
- **The speaker** plays a mono mix of everything when nothing is plugged into phones.

## Owner decisions (verbatim, linked to owner.md)
- Base spec: "Built-in speaker (LM386) + outputs. No additional patch points beyond pitch CV/gate out + filter CV in."
- Base spec: "MIDI: USB-MIDI + 3.5 mm TRS MIDI in".
- "Add MIDI out" (TRS out, free in pins).
- "Stereo phones is fine but I need to pan the signal into the effects" and "Stereo line out." → stereo PHONES and stereo LINE OUT (TRS), one speaker.
- "Left channel should be mono tho if stereo isn't plugged in." → a mono cable in line out must carry the full mix.
- "the workflow im much more interested in is controlling it from another device or mainly a DAW" → USB-MIDI first ([MIDI](midi.md)).

## How it works
| Jack / port | Type | Signal | Path | Status |
|---|---|---|---|---|
| **PHONES** | 3.5 mm TRS, switched | stereo, headphone level | L / R sums → VOLUME → headphone driver (NJM4556A class, UNVERIFIED); the jack's switch mutes the speaker and powers the driver only when a plug is in (review 16) | decided (stereo); circuit proposed |
| **LINE OUT** | 3.5 mm TRS (or two jacks, L / MONO + R: owner question 4) | stereo, line level | second half of the summing TL072 → line driver with 470 Ω–1 kΩ build-out (review 2) | decided (stereo); mono-on-TS fix open |
| **USB-C** (rear) | USB 2.0 FS device | USB-MIDI, DFU, 5 V in | VBUS → charger; D± → the Daisy Seed's own USB port through a cut cable (DFP §5.3) | proposed |
| **MIDI IN** | 3.5 mm TRS (Type A wiring, eng to confirm) | MIDI | optocoupler → USART1 RX (PB7, 5 V-tolerant) | decided |
| **MIDI OUT** | 3.5 mm TRS | MIDI (channel pressure today) | USART1 TX | decided |
| **PITCH CV OUT** | 3.5 mm TS | 1 V/oct, 0–5 V | Seed DAC1_OUT2 (freed by the PARA+4 option A) → buffer / scale; ≈ 1.5 cents per step [CALC] | decided (jack); channel proposed |
| **GATE OUT** | 3.5 mm TS | V-gate, 0 → +5 V | GPIO → transistor driver | decided |
| **FILTER CV IN** | 3.5 mm TS | ± 5 V CV | the original external control input (100 k into the filter control node); analog, so audio-rate filter FM works | decided |
| **INPUT** (EXT IN) | 3.5 mm TS | audio, line / instrument level | the original 1 M level + gain-of-200 preamp → mixer bus, picked by **source: input**, level on **extra** | proposed (jobs F flows; the Model D's external input) |

- **Protection on every input:** a series resistor (≥ 1 k) and clamps to the rails, so a eurorack ± 12 V on any jack is survivable indefinitely (eng §5b).
- **Pops:** phones and line out have a shunt mute held at reset and released after boot calibration + 200 ms. It shares the LM386 enable pin (review 7).
- **Ground loops:** with USB and line out into the same computer, there may be hum. Footprints for a ferrite on the USB shield / ground; the manual says "run on battery or use an isolator to record" ([panning and stereo outputs](panning-and-stereo-outputs.md)).
- **CATHEDRAL placement:**
  - **USB-C and the two MIDI jacks** sit on the **base's right end face**, below the plate (USB-C at y 90–99, z 4.8–8.2), clear of the hinge ear (cathedral §6; closed side drawing).
  - **The audio and CV jacks** sit on the **lid's far wall** on its I/O board (x 60–230, d 92–104; cathedral §14). That's the top edge when standing, so cables leave upward, away from the hands.

## Controls and states
| Situation | What happens |
|---|---|
| Phones plugged in | speaker off; phones on |
| Line out plugged in | speaker stays on (owner question 4 also asks whether it should go off) |
| Mono (TS) cable in line out | the full mix on the tip (needs the two-jack answer, or the reworked detection) |
| Mono (TS) plug in phones | left only: accepted (TS headphones are rare) |
| USB to a computer | USB-MIDI device; charging; DFU only after the update gesture |
| Nothing in INPUT, source on input | silence on that mixer channel |
| Pitch CV / gate out | follow the played note (mono) or the lowest note (para), including bend and glide |

## Edge cases
- **Eurorack levels into INPUT:** a 10 Vpp signal clips the gain-of-200 preamp unless **extra** is near zero. That's how the Model D behaved. A eurorack-level pad is an option (eng §5b).
- **Filter CV in left unplugged:** the jack grounds the input, so nothing changes.
- **MIDI out and the DAW:** only channel pressure is sent today, so no feedback loops from a DAW's MIDI thru ([MIDI](midi.md)).
- **USB enumeration without VBUS on the Seed's connector:** a bench risk; the fix is a Schottky diode feed ([firmware and gestures](firmware-update-and-gestures.md)).

## Interactions with other features
- **Panning and stereo outputs:** all output wiring and the mono-on-TS question live there ([panning and stereo outputs](panning-and-stereo-outputs.md)).
- **MIDI:** the TRS in / out and USB-MIDI behaviour ([MIDI](midi.md)).
- **Paraphonic:** pitch CV out carries the lowest note; its channel exists only with option A ([paraphonic](paraphonic.md)).
- **Power:** USB-C is the only charging input; phones save the speaker's power ([power and battery](power-and-battery.md)).
- **Voice:** source "input" and filter CV in enter the original analog paths ([voice](voice.md)).

## MIDI
- USB-MIDI and TRS MIDI in are merged (MIDI doc). MIDI out carries channel pressure.

## Budget (pins / mux / DAC / power / cost)
- **Pins:** USART1 TX / RX (MIDI), 1 gate GPIO, Seed DAC1_OUT2 (pitch CV), the shared mute / LM386 enable. USB uses no header pins.
- **Mux:** PHONES sense +1, TS sense +1 (0 with two line jacks) ([architecture](../architecture.md)).
- **Cost (ESTIMATE):** USB-C breakout $3.45 (Adafruit #4090); 3.5 mm jacks ≈ $0.50–1 each × 8–9; MIDI optocoupler and parts ≈ $2; output stage ≈ $3–5 ([panning and stereo outputs](panning-and-stereo-outputs.md)).

## Open questions
1. **Line out: two jacks (L / MONO + R) or one reworked jack**, and should line out mute the speaker? (Owner question 4; team recommends two jacks.)
2. **INPUT jack:** keep it (it's the Model D's external input, and source "input" uses it), or drop it to hold the "no additional patch points" line strictly? Team view: keep it. It's the only way into the mixer from outside, and the "loop" source doesn't need it.
3. **TRS MIDI wiring:** Type A (the MIDI doc's choice for out); eng confirms the input matches.
4. **The lid's I/O board vs row A's pot bodies** (d 92–104 vs the knobs at d 84.55): eng checks the clearance.

## Status (decided / proposed / open, item by item)
| Item | Status |
|---|---|
| Speaker; stereo phones; stereo line out; mono on a TS cable | decided |
| Pitch CV out, gate out, filter CV in; nothing else beyond these | decided |
| USB-MIDI, TRS MIDI in, TRS MIDI out | decided |
| One rear USB-C to the Seed's port; charging on the same port | proposed |
| INPUT jack (EXT IN) | proposed / open (question 2) |
| Protection, mute, ground-loop footprints | proposed (eng / review) |
| Line out two jacks vs one; line out mutes the speaker | open (owner) |
| CATHEDRAL placement (base end face, lid far wall) | proposed |
