# Bend and mod
Status: per item below · last updated 2026-11-13 · sources: [owner.md](../../design/owner.md), [eng/budget-variant.md](../../eng/budget-variant.md) §v1.5, [eng/daisy-first-principles.md](../../eng/daisy-first-principles.md) §0, §4.3, [eng/architecture.md](../../eng/architecture.md) §1.8, [cathedral §18](../../design/branches/concepts/cathedral/how-it-works.md) (base row)

Panel words follow the one-word vocabulary. The base's **controllers** group reads **bend · mod · blend · glide**. The **mod** switches sit with the oscillators and with the filter.

## What it does (player's view)
- **bend:** a small joystick at the left end of the played row. Push it up or down and the pitch bends. Let go and it springs back to centre.
- **mod:** a knob that stays where you leave it. It sets how much modulation reaches the oscillators and the filter, like the Model D's mod wheel.
- **blend:** what the modulation is, from **oscillator 3** (a smooth wobble or FM) to **noise** (random).
- **Where it goes:** the oscillators' **mod** switch sends it to pitch (vibrato), the filter's **mod** switch sends it to the cutoff (wah). With both off, mod does nothing.
- **Pressing into a held key** can add to mod (touch: mod), see [aftertouch](aftertouch.md).

## Owner decisions (verbatim, linked to owner.md)
- Base spec: "Bend/mod: bend = joystick restricted to one direction, springs back; mod = a control that stays put (dial or fader); mod depth MIDI-controllable (jump-on-move)."
- "bend up+down or up only?" → "Up and down": one axis, springs to centre.
- "joystick is great if we can go one direction" (budget-variant §v1.5) → mod is a plain dial.
- "also i want the bend slider to be a joystick" → the bend must be, and read as, a joystick (round opening, stem, cap).

## How it works
```
bend stick (one axis, sprung) ─► mux ─► Daisy ─► added to every VCO's pitch sum ─► coarse + fine DACs
mod knob ─► mux ─► Daisy ─► Seed DAC1_OUT2 (or the 5th MCP4822, PARA+4 option A) ─► AS3360 mod VCA
osc 3 ─┐                                                                                    │ depth
noise ─┴─► blend (analog pot) ─────────────────────────────────────────────────────────────► AS3360 ─┬─► oscillators' mod switch ─► VCO mod bus
                                                                                                      └─► filter's mod switch ─► cutoff node (33 k)
```
- **Bend is digital:** the stick's position is read through the mux and added to each VCO's pitch value before the DACs (budget-variant §v1.5). Spring-to-centre is mechanical. Firmware takes a small dead zone at centre so "let go" is exactly in tune.
- **The stick:** an Adafruit #2765 mini two-axis thumbstick ($2.50), with **one axis used**, gated to one axis by a slot in the plate (budget-variant §v1.5, "pick for cost"). A true single-axis lever pot costs ≈ $229, so it was rejected.
- **Mod stays analog, with a digital depth:** the modulation itself (osc 3 / noise → blend) is analog, so osc 3 at audio rate still gives real FM (eng §1.8). Only its **depth** is a CV: the mod knob → firmware → a DAC → an **AS3360 VCA** in the mod path. That's what lets MIDI CC 1 and touch set the depth (budget-variant §v1.5).
- **Feedthrough null:** at autotune, the firmware measures the VCOs' pitch with mod at 0 on TIM5 and trims the AS3360's offset, so "mod at 0" really is no wobble (DFP §0, row 8; optional).
- **Height:** the stick stands 12.6 above the base plate. Since steer 4, nothing on the lid lands over it when closed, so it **no longer needs lowering** for the 55.2 mm closed height ([cathedral §18.3](../../design/branches/concepts/cathedral/how-it-works.md)).

## Controls and states
| Control | Range | Notes |
|---|---|---|
| **bend** (stick) | down ↔ centre ↔ up, sprung | **± 2 semitones** (proposed: matches the MIDI pitch-bend default; the range is open) |
| **mod** (knob) | 0 → full depth | stays put; MIDI CC 1 with jump-on-move |
| **blend** (MOD MIX) | osc 3 ↔ noise | analog pot |
| oscillators' **mod** | off · on | on: the mod bends all three VCOs |
| filter **mod** (base) | off · on | on: the mod moves the cutoff |
| **glide** | 0 → long | firmware, saturating curve like the original (eng §1.8) |

## Edge cases
- **Bend from the stick and from MIDI together:** they add, clamped (MIDI doc: both centred = 0).
- **mod knob vs CC 1:** last touched wins. After CC 1 moves the depth, the knob does nothing until it's turned past that value, and the **midi** light stays on until then (jump-on-move; [MIDI](midi.md)).
- **mod at 0 with touch on mod:** pressure still adds depth (+50 % of the knob's range at full pressure; [aftertouch](aftertouch.md)).
- **Osc 3 as the source with track on:** the wobble rate follows the keys. Turn osc 3's **track** off for a steady LFO.
- **Boot gesture:** holding TAP and the bend stick fully up while switching on opens the bootloader ([firmware and gestures](firmware-update-and-gestures.md)). During play the stick does nothing special.

## Interactions with other features
- **Voice:** bend joins the pitch sum, inside the autotune loop ([voice](voice.md)).
- **Paraphonic:** bend and mod apply to every note of a chord ([paraphonic](paraphonic.md)).
- **Aftertouch:** touch "mod" adds to the mod depth CV ([aftertouch](aftertouch.md)).
- **Firmware and gestures:** the stick is half of the bootloader gesture.

## MIDI
- **In:** pitch bend (14-bit), added to the stick; default ± 2 semitones, RPN 0 sets 0–12 (proposed). CC 1 sets mod depth (decided).
- **Out:** none (only channel pressure is sent today).

## Budget (pins / mux / DAC / power / cost)
- **Mux:** bend and mod use 2 channels, already counted ([architecture](../architecture.md)). Blend is an analog pot in the audio-rate path and isn't read.
- **DAC:** mod depth on Seed DAC1_OUT2, or on the 5th MCP4822 under the PARA+4 option A.
- **Parts:** #2765 stick $2.50 + mod pot ≈ $0.75 + AS3360 VCA ≈ $5–8 (budget-variant §v1.5): **≈ $8.25–11.25**.

## Open questions
1. **Bend range:** ± 2 semitones (proposed), or wider (the Model D's wheel is wider; eng to check)? A settings gesture could make it adjustable.

## Status (decided / proposed / open, item by item)
| Item | Status |
|---|---|
| Bend = one-axis sprung joystick, up and down; reads as a joystick | decided |
| Mod = a control that stays put; depth MIDI-controllable with jump-on-move | decided |
| #2765 stick slot-gated to one axis; AS3360 mod VCA; feedthrough null | proposed (eng) |
| Panel words bend · mod · blend · glide; mod switches on oscillators and filter | proposed (director's vocabulary) |
| Bend range ± 2 semitones | open |
