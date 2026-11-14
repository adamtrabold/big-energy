# Voice
Status: per item below · last updated 2026-11-13 · sources: [owner.md](../../design/owner.md), [eng/architecture.md](../../eng/architecture.md) §1, §1.9, [eng/daisy-first-principles.md](../../eng/daisy-first-principles.md) §2, §4, [eng/budget-variant.md](../../eng/budget-variant.md), [cathedral §18](../../design/branches/concepts/cathedral/how-it-works.md) (panel words)

Panel words follow the one-word vocabulary (`design/branches/concepts/cathedral/vocabulary.md`). The engineering names are given once, in brackets.

## What it does (player's view)
- **Three analog oscillators**, each with **octave**, **wave**, and (oscillators 2 and 3) **pitch** to tune against oscillator 1. Oscillator 3 can stop following the keys (**track: off**) and become a slow modulator or a drone.
- The **mixer** sets how much of each oscillator goes on (**1 · 2 · 3**), plus one **extra** source. The **source** switch picks what that extra is: **noise**, the rear **input**, or **loop** (the Model D's feedback trick, built in).
- Push the mixer hard and the filter's input overdrives, the "fat" Model D sound.
- A **24 dB ladder filter**: **cutoff** (the big red dial), **resonance** (up to self-oscillation), **envelope** (how far the filter envelope moves it), **track** (how far the cutoff follows the keys) and **mod** (the mod wheel moves it).
- **Two envelopes**, filter and amp, each **attack · decay · sustain**, with **release** (off · on) for both. They overshoot slightly on the attack, which gives the "punch".
- **Glide** between notes, **tune** and **drift** (a slow, controllable pitch wander; at 0 it's rock steady), and **volume** at the end.
- **No calibration, ever:** the oscillators tune themselves at power-on and keep themselves in tune while you play.

## Owner decisions (verbatim, linked to owner.md)
- Base spec (binding, from the shared history): "Voice: 3 VCOs, all original waveforms, original-style chips (modern equivalents e.g. AS3046; no vintage parts), ladder filter with mixer overdrive, 2 analog contours with overshoot, VCA, glide, autotune (no manual calibration)."
- "I like the idea of drift, but I'd want it to be controllable" → DRIFT added as a knob; 0 = rock steady.
- "Both, with a switch" (velocity: loudness / filter / both). See [keys and velocity](keys-and-velocity.md).
- "Labels should only be one word and follow best practices with obvious tweaks for understanding if there's a better word than the jargon" (2026-11-13 19:57): the panel words used here.

## How it works
```
keys / MIDI ─► Daisy ─► MCP4822 coarse + fine ×3 ─► VCO 1, 2, 3 (discrete cores, AS3046 expo) ─┐
                     └─► MCP4822 #4: filter track CV, CUTOFF CV                                   │
noise (junction) ─┐                                                                                ▼
rear input ───────┼─► SOURCE ─► EXTRA level ─► passive 33 k mixer ◄─ 1 · 2 · 3 levels ◄──────────┘
loop (dry VCA out)┘                                │ (overdrive happens here, in the ladder's input pair)
                                                   ▼
                       ladder filter (4 matched pairs, 0.068 µF) ◄─ cutoff + envelope × filter env + track + mod + velocity
                                                   ▼
                                         VCA ◄─ amp envelope (+ velocity) ─► dry out (to pans, volume, FX send)
```
- **Oscillators:** the original discrete core per VCO (JFET ramp buffer, discrete reset and comparator), with an **AS3046** expo pair and a tempco resistor. Waveforms as the Model D: triangle, tri/saw, saw and three rectangles on 1 and 2; reverse saw in place of tri/saw on 3 (eng §1.2).
- **Pitch is digital, sound is analog:** every pitch input (keys, bend, glide, tune, octave, pitch knobs, drift) is summed in firmware and written to a **coarse + fine** DAC pair per VCO. The fine step is ≈ 0.036 cent (DFP §4.3).
- **Self-tuning:** TIM5 counts each VCO's period. Autotune builds a table at power-on (stored in flash, verified in ≈ 0.3 s), and a slow loop trims held notes while you play (DFP §2). Details: [autotune and drift](autotune-and-drift.md).
- **Mod path stays analog:** blend (osc 3 ↔ noise) → the mod depth VCA (the wheel's value) → the oscillators' **mod** switch and the filter's **mod** switch. Oscillator 3 at audio rate gives real FM (eng §1.8).
- **Mixer and overdrive:** passive 25 k level pots and 33 k into the ladder's input pair, exactly as the original. That input pair is where the "fatness" comes from, so it's kept at ±10 V (eng §1.4, §1.9).
- **Source "loop"** is tapped from the dry VCA out, before the effects and volume, so effect latency never enters the loop (effects review 21; proposed).
- **Filter:** the original ladder topology and values, with high-β matched NPNs and the reverse-audio resonance law (eng §1.5). Its keyboard CV comes from MCP4822 #4 and is **calibrated to 1 V/oct at full tracking**, using the codec's free right input to measure self-oscillation (DFP §2).
- **Envelopes:** two identical analog ADS circuits, verbatim, including the values that give the attack overshoot. **Release** on: release follows the decay time; off: the timing cap is dumped at key-up (eng §1.6). It acts on both envelopes.
- **VCA:** the original pair, with a static balance from one PWM (DFP §4.3). Velocity reaches the VCA through an AS3360 stage.

## Controls and states
| Control (panel word · engineering name) | Range / positions | Notes |
|---|---|---|
| **octave** ×3 (RANGE) | 32' · 16' · 8' · 4' · 2' · LO | 6-way; the MIDI map treats it as a switch if it becomes a detented rotary (midi.md) |
| **wave** ×3 (WAVEFORM) | 6 shapes | osc 3: reverse saw in place of tri/saw |
| **pitch** 2, 3 (FREQUENCY) | ± 7 semitones (eng; UNVERIFIED span) | fine detune in para mode ([paraphonic](paraphonic.md)) |
| **voices** (PARA) | 1 · 3 · 4 | see [paraphonic](paraphonic.md) |
| oscillators' **mod** (OSC MOD) | off · on | the mod mix bends all three oscillators |
| oscillator 3 **track** (OSC 3 CTL) | off · on | off: osc 3 ignores the keys (drone / modulator) |
| mixer **1 · 2 · 3** | 0–10 | passive |
| **extra** (NOISE / EXT level) | 0–10 | sets whichever source is picked |
| **source** | noise · input · loop | 3-way |
| **cutoff** | 10 Hz–20 kHz (Model D spec) | CV from MCP4822 #4 |
| **resonance** (EMPHASIS) | 0 → self-oscillation | reverse-audio law |
| **envelope** (CONTOUR AMOUNT) | 0–10 | filter envelope depth |
| filter **track** (KEYBOARD CONTROL) | off · 1/3 · 2/3 | **full isn't reachable today** (open question 1) |
| filter **mod** (FILTER MOD) | off · on | the mod mix moves the cutoff |
| **attack · decay · sustain** ×2 | Model D reissue: attack 1 ms–10 s, decay 4 ms–> 35 s, sustain 0–100 % | analog |
| **release** (DECAY switch) | off · on | both envelopes |
| **glide**, **tune**, **drift** | glide 0 → long; tune ± (eng); drift 0 = steady | firmware |
| **volume** | 0–10 | dual-gang; see [panning and stereo outputs](panning-and-stereo-outputs.md) |

## Edge cases
- **Self-oscillating filter:** at full resonance the ladder sings a sine. Its pitch follows the keys only as far as **track** allows. Without full tracking, a played filter melody goes flat as you go up (open question 1).
- **Loop runaway:** loop with extra near full can run away to a howl, as on a Model D. It's a sound, not a fault, and volume always works.
- **Track off on osc 3, octave LO:** osc 3 runs from about a click every few seconds up to audio rate. The original clicks every ≈ 4.95 s at its slowest (eng §1.2).
- **Autotune at a cold start:** the first power-on after a big temperature change runs a full sweep (≈ 2–4 s); otherwise a 0.3 s verify. If a VCO fails, the status light blinks its number ([echo-sync](echo-sync.md) status table; jobs F1).
- **Drift at 0:** truly steady. The random walk sits inside the tuning loop, so 0 means no wander at all (DFP §4.3).

## Interactions with other features
- **Paraphonic:** in para, each note gets its own oscillator; one filter and both envelopes are shared ([paraphonic](paraphonic.md)).
- **Velocity and touch:** velocity → amp / both / filter; touch → mod / off / filter ([keys and velocity](keys-and-velocity.md), [aftertouch](aftertouch.md)).
- **Bend and mod:** bend goes into the pitch sum; the mod wheel sets the mod depth VCA ([bend and mod](bend-and-mod.md)).
- **Effects:** the dry VCA out feeds the echo / reverb send, and the dry analog path is never switched ([effects](effects.md)).
- **MIDI:** cutoff, glide, tune and the pitch knobs are MIDI-controllable with jump-on-move ([MIDI](midi.md)).

## MIDI
- Receives (proposed CC numbers in [MIDI](midi.md)): cutoff, glide, tune, pitch 2 / 3, octave 1–3 (if they stay pots), mod (CC 1, decided).
- Switches never move by MIDI (owner).
- **Sends:** only channel pressure today.

## Budget (pins / mux / DAC / power / cost)
- **DACs:** 4× MCP4822 (coarse + fine ×3; filter track + CUTOFF), plus the Seed's two DACs for velocity and mod depth. A 5th MCP4822 is proposed for the PARA+4 path ([paraphonic](paraphonic.md)).
- **Timers:** TIM5 CH1–3 (VCO periods).
- **Mux:** every voice knob and switch on the control mux (ADC3). The recount is in [architecture](../architecture.md).
- **Power and cost:** see [architecture](../architecture.md); the voice is the bulk of eng's part count (eng §8).

## Open questions
1. **Filter track positions.** Today's spec: off · 1/3 · 2/3, so full tracking isn't available. The Model D reaches full with both of its switches on. **Proposed:** **off · 1/2 · full**, either by re-resistoring the same 3-way switch (two resistor values; review item 12) or by having firmware read it and scale the CV. Team recommends; eng to confirm. Owner question on the [decisions page](../../design/decisions-open.md) (item 7).
2. **Pitch knob span** (± 7 semitones, or Model D's narrower range): eng.
3. **Source "loop" tap point** (dry VCA out, pre-FX, pre-volume): eng to confirm.

## Status (decided / proposed / open, item by item)
| Item | Status |
|---|---|
| 3 VCOs with original waveforms, AS3046-era parts, ladder filter with mixer overdrive, 2 analog contours with overshoot, VCA, glide, autotune | decided (base spec) |
| DRIFT knob, 0 = rock steady | decided |
| Velocity routing switch | decided |
| One-word panel words | decided (rule); exact words from the director's vocabulary: proposed |
| Coarse + fine DACs, TIM5 tuning, held-note loop, codec filter cal | eng design (proposed) |
| SOURCE noise · input · loop, loop tapped pre-FX | proposed |
| Filter track off · 1/3 · 2/3 vs off · 1/2 · full | open (owner / eng) |
| Pitch knob span | open (eng) |
