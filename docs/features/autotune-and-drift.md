# Autotune and drift
Status: per item below · last updated 2026-11-13 · sources: [owner.md](../../design/owner.md), [eng/daisy-first-principles.md](../../eng/daisy-first-principles.md) §2, §4.3, §8, [eng/architecture.md](../../eng/architecture.md) §3 (zero-calibration strategy, every original trimmer), [audio / synth review](../../design/reviews/2026-11-13-audio-synth-review.md)

Panel words follow the one-word vocabulary: **drift** and **tune** sit in the base's **tuning** group; the **status** light reports a tuning failure.

## What it does (player's view)
- **You never tune or calibrate it.** At power-on it checks its own oscillators in about a third of a second, and re-learns them fully when it needs to.
- **It stays in tune while you play.** On a held note, it nudges each oscillator back on pitch so slowly you can't hear it. It never locks the oscillators together, so they still beat against each other like real analog.
- **drift** gives the wander back on purpose: a slow, random pitch movement, separate for each oscillator. At **0** it's rock steady; turn it up for a looser, older-synth feel.
- **tune** moves everything up or down together, as on the Model D.
- **The filter is tuned too:** its keyboard tracking is set automatically, so a self-oscillating filter plays in tune as far as the **track** switch allows.

## Owner decisions (verbatim, linked to owner.md)
- Base spec: "… autotune (no manual calibration)."
- "I like the idea of drift, but I'd want it to be controllable" → a **drift** knob; 0 = rock steady.

## How it works
- **Measuring (TIM5):** each VCO's square edge goes to one channel of the Daisy's 32-bit TIM5 (CH1–3, D25 / D24 / D28). All three are measured at once, continuously, at about **0.03 cent per single period** at 4 kHz; averaging improves that (DFP §2.2). The mixer levels are analog and can't mute an oscillator, so all three are measured, always.
- **Writing pitch:** each VCO has a **coarse + fine** DAC pair (MCP4822). The fine channel sums in at 1/64, a step of ≈ 0.036 cent (DFP §4.3). Every pitch input (keys, MIDI, bend, glide, tune, octave, pitch knobs, drift) is summed in firmware, mapped through that VCO's table and written to its pair.
- **The table:** a monotonic piecewise volts → octaves map per VCO, built by stepping the DAC across the range and measuring. It absorbs expo scale and offset, high-frequency droop, DAC error and reference drift (eng §3.1).
- **At power-on:** the tables live in the Seed's flash. Boot runs a **3-point verify (≈ 0.3 s)** and only does a full re-sweep (≈ 2–4 s) if the verify fails, or if you hold **tap** while switching on (DFP §2.3; [firmware and gestures](firmware-update-and-gestures.md)).
- **While playing (held-note loop):** while a note is held, TIM5 averages ≥ 50 ms of periods per VCO, and the firmware trims that VCO's fine DAC toward its target **plus its drift offset**. τ ≈ 2 s, steps < 0.1 cent: inaudible. Each VCO tracks its own target, so they never pull together (DFP §2.3).
- **Freeze rule:** the loop freezes when the period jitters (FM from osc 3, glide or bend moving), detected from the measurements themselves (DFP §2.3).
- **Drift:** a firmware **random walk on each VCO's fine channel**, independent per oscillator, inside the loop. So the loop holds the wander exactly where drift puts it, and drift 0 is truly locked (DFP §4.3, §8). The fine DAC is why it doesn't staircase: drift is "a slow wander of a few cents", which 2.3-cent coarse steps would make audible (DFP §4.1).
- **Filter tracking:** the codec's free right input listens to the ladder output (pre-VCA). At calibration (resonance fully up at power-on), the firmware finds the self-oscillation peak at several keyboard-CV points, even with oscillators audible, because TIM5 already knows their frequencies. It sets the filter track channel's gain for 1 V/oct at full tracking. Precision ≈ 0.004 cent against a ± 10-cent need (DFP §2.2).
- **VCA balance:** the codec's left input (the FX send, post-VCA) watches for the envelope's "thump", and the firmware nulls it with the VCA balance PWM (DFP §2.2; method UNVERIFIED, DC-sense fallback footprint kept).
- **The original's trimmers:** each of the Model D's 16 adjustments is either replaced by these loops or fixed by design. One isn't auto-adjusted: **REGEN CAL** (resonance onset), set by a resistor chosen by Monte Carlo, so onset lands at 7.5 ± 1 on the dial (eng §3.2).

## Controls and states
| Control / state | Range | Notes |
|---|---|---|
| **drift** | 0 (steady) → full | per-VCO random walk; full depth open (question 1) |
| **tune** | ± (eng) | global, in the pitch sum |
| Power-on, normal | ≈ 0.3 s verify | then "ready" and the battery flash |
| Power-on, **tap** held | full re-sweep, ≈ 2–4 s | |
| Power-on, **resonance** full + **tap** held | filter calibration | never live |
| A VCO fails to tune | **status** light blinks *n* times (VCO *n*) | power-cycle; if it repeats, service (jobs F1) |

## Edge cases
- **Oscillator 3 as a modulator (track off, octave LO):** it's measured but not trimmed on held notes. Its target has no key note, and its very slow periods are excluded from the loop (proposed).
- **Turned-down oscillator:** still measured (the edge is taken before the mixer), so it stays in tune for when you bring it back.
- **Heavy FM or vibrato:** the loop freezes and holds the last trim; it resumes when the pitch is steady.
- **Big temperature change while playing:** the held-note loop absorbs slow drift. If a VCO's error grows past what the fine channel can reach, the next power-on's verify fails and runs a full sweep.
- **Drift with paraphonic chords:** each oscillator wanders on its own, so a held chord gently detunes and re-tunes. At 0 it doesn't.
- **Filter calibration with someone turning cutoff:** the slope comes out wrong; repeat it (only the slope is calibrated, so cutoff's position otherwise doesn't matter; eng §3.1).

## Interactions with other features
- **Voice:** owns the oscillators, filter and VCA these loops serve ([voice](voice.md)).
- **Paraphonic:** the 4th oscillator is digital and needs no tuning; the analog three keep their loops per note ([paraphonic](paraphonic.md)).
- **Bend and mod:** bend and glide freeze the loop while they move; the mod VCA's feedthrough is nulled at autotune ([bend and mod](bend-and-mod.md)).
- **Firmware and gestures:** the power-on gestures and status light ([firmware and gestures](firmware-update-and-gestures.md)).
- **MIDI:** tune is MIDI-controllable; drift isn't in the CC map (proposed: add it if he asks) ([MIDI](midi.md)).

## MIDI
- **tune:** receives (jump-on-move); CC number in [MIDI](midi.md).
- **drift:** none today.
- Autotune never sends MIDI.

## Budget (pins / mux / DAC / power / cost)
- **Pins:** TIM5 CH1–3 (D25, D24, D28); D16 freed (TIM5 CH4 kept as the comparator fallback).
- **DACs:** the 3 coarse + fine MCP4822 pairs; the filter track channel; one PWM for VCA balance.
- **Codec:** R in = ladder output (filter cal), L in = FX send (VCA null).
- **Mux:** drift and tune knobs.
- **Parts:** ≈ $0 beyond the voice's DACs: −1 comparator, +1 op-amp half (DFP §2.4).

## Open questions
1. **How much drift at full?** Proposed: up to **± 15 cents**, wandering over seconds (team recommends; firmware can change it). Owner question 11 on the [decisions page](../../design/decisions-open.md).
2. **VCA thump servo on the codec's AC-coupled input:** bench check (DFP §2.2); the DC-sense fallback is kept.
3. **Held-note loop:** a design idea, not documented in a commercial product (eng risk R15). Bench-test it on the spike.

## Status (decided / proposed / open, item by item)
| Item | Status |
|---|---|
| Autotune, no manual calibration | decided |
| Controllable drift, 0 = rock steady | decided |
| TIM5 measuring, coarse + fine DACs, flash tables, 0.3 s verify | proposed (eng) |
| Held-note loop with the freeze rule | proposed (eng; bench-gated) |
| Drift as a per-VCO random walk inside the loop | proposed |
| Filter cal on the codec R input; VCA null on codec L | proposed |
| Drift depth at full | open (owner question 11) |
