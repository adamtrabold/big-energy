# Architecture

An analog synth voice with one small computer beside it. The **sound is analog** from the oscillators to the outputs. A **Daisy Seed** reads the keys and knobs, tunes the oscillators, speaks MIDI, and adds **digital echo and reverb** that are mixed back in.

*Updated 2026-11-13 · systems designer · "Decided" means recorded in the [owner record](../design/owner.md); everything else is proposed.*

---

## The device at a glance

```
        ┌──────────── CONTROL ────────────┐
 keys ──┤                                 │
 knobs ─┤  muxes ─► DAISY SEED ─► DACs ───┼──► pitch, cutoff, velocity, mod CVs
 MIDI ──┤            │    ▲               │
        └────────────┼────┼───────────────┘
                     │    │ (tuning: counts each oscillator)
        ┌──────────── SOUND ──────────────────────────────────────────────┐
        │  3 oscillators ─► mixer ─► filter ─► VCA ─┬─► dry ──────────┐   │
        │                                           │                 ▼   │
        │                         Daisy: echo → reverb ◄─ send   OUTPUTS  │
        │                                           └──► wet ───► (mix)   │
        └─────────────────────────────────────────────────────────────────┘
                                         OUTPUTS: stereo phones · stereo line out · one speaker
```

**Two rules shape everything:**
- the dry sound never passes through the computer;
- the computer never flips a switch.

---

## The blocks

| Block | What it is | Feature doc |
|---|---|---|
| Voice | 3 VCOs, mixer, 4-pole ladder filter, analog contours, VCA | [voice](features/voice.md) |
| Keys | 25 silent Choc V2 keys, Hall-sensed velocity, printed or bought key heads | [keys and velocity](features/keys-and-velocity.md) |
| Aftertouch | pressure strip under the keys, MOD / OFF / FILT | [aftertouch](features/aftertouch.md) |
| Bend and mod | sprung one-axis stick, MOD knob | [bend and mod](features/bend-and-mod.md) |
| Paraphonic | MONO / PARA / PARA+4 | [paraphonic](features/paraphonic.md) |
| Tuning | autotune, held-note correction, DRIFT | [autotune and drift](features/autotune-and-drift.md) |
| Effects | echo (4 types) → reverb (4 types), wet-only return | [effects](features/effects.md) |
| Echo sync | FREE / SYNC, TAP, MIDI clock | [echo sync](features/echo-sync.md) |
| Outputs and panning | stereo phones and line, one speaker, dry pan, delay pan, FOLLOW | [panning and stereo outputs](features/panning-and-stereo-outputs.md) |
| MIDI | played and automated from a DAW | [MIDI](features/midi.md) |
| Power | internal battery, one USB-C | [power and battery](features/power-and-battery.md) |
| Firmware and gestures | updates, boot and settings gestures | [firmware update and gestures](features/firmware-update-and-gestures.md) |
| Connections | jacks, USB-C, CV / gate | [I/O](features/io.md) |
| Body | CATHEDRAL / FOLD enclosure | [enclosure](features/enclosure.md) |

---

## How sound flows
1. **Oscillators → mixer → filter → VCA:** all analog.
2. After the VCA the signal splits:
   - **dry** goes straight to the outputs;
   - a **send** goes to the Daisy's input.
3. The Daisy runs **echo, then reverb**, and returns **only the effect** (stereo).
4. **Outputs** mix dry + effect: stereo phones, stereo line out, and a mono mix for the speaker.

Details: [effects](features/effects.md) · [panning and stereo outputs](features/panning-and-stereo-outputs.md)

## How control flows
1. **Keys, knobs and switches** → multiplexers → the Daisy's converters, about 10,000 times a second.
2. **MIDI** (USB or TRS) → the Daisy. A DAW can move any knob marked with a MIDI dot; that knob's light shows it's held until you touch it.
3. **The Daisy** → DACs → pitch for each oscillator, cutoff, velocity and mod depth. It also counts each oscillator's frequency to keep it in tune.

Details: [MIDI](features/midi.md) · [autotune and drift](features/autotune-and-drift.md)

---

## Budgets

One table for every shared resource.
- **Today:** the locked spec plus aftertouch.
- **Decided:** adds what the owner has approved since.
- **Proposed:** adds the team's and the review's fixes.

| Resource | Capacity | Today | + decided | + proposed | Action |
|---|---|---|---|---|---|
| **Mux inputs** (keys, knobs, switches) | 48 (3 muxes) | 48 | **53** | **57–59** | **Add a 4th mux → 64** (open item 1) |
| **Daisy pins** | 31 | 27 | 28 (MIDI out) | 29–30 | fits; 1 spare left |
| **Pitch / CV DACs** | 8 + 2 | 10 of 10 | 10 | 10 + digipot (dry pan) | **PITCH CV OUT has no channel** (open item 7) |
| **Codec** (stereo in / out) | 2 in, 2 out | all used | all used | — | **PARA+4 has no audio path** (open item 3) |
| **Power** | 22 Wh (11 Wh in FOLD-105) | ≈ 2.0–3.6 W, ≈ 4–8 h on 22 Wh, ≈ 2–4 h on 11 Wh | + stereo stage (few mA) | + speaker when loud (≈ 0.5–0.8 W, unverified) | count the speaker (open item 8) |

<details><summary>What fills the mux (53 → 59)</summary>

- **Decided additions:** PARA toggle, FREE / SYNC, DRY PAN, DELAY PAN, FOLLOW (+5).
- **Proposed:** OSC 3 CTL read, phones-in sense, TS sense on line out, the battery divider moved onto the mux (+4), and optionally charger STAT / VBUS (+2).
</details>

---

## Where decisions live
- **The owner's decisions, word for word:** [owner record](../design/owner.md). Nothing is "decided" unless it's there.
- **Each feature's decisions, proposals and open questions:** its feature doc (above), always under the same headings.
- **Engineering sources:**
  - [master spec](../eng/budget-variant.md);
  - [Daisy design](../eng/daisy-first-principles.md);
  - [aftertouch](../eng/aftertouch.md);
  - [echo sync](../design/branches/echo-clock.md);
  - [CATHEDRAL](../design/branches/concepts/cathedral/how-it-works.md);
  - [expert review](../design/reviews/2026-11-13-audio-synth-review.md).

---

## Open items
1. **The mux is full.** Add a 4th mux on pin D20 and move the battery reading onto it. *Eng: confirm the timing.*
2. **Mono on a TS cable can't work as drawn.** Two jacks (L / MONO + R) need the owner's OK (one more hole). The alternative is a low-bias rework that eng benches.
3. **PARA+4 has no audio path.** Route the 4th oscillator through the filter (effects go mono in that mode), or make the switch 2-way. *Owner.*
4. **Peg keys rub the floating key strip.** Widen the holes to ≥ 1 mm clearance, or slim the necks.
5. **TAP gestures collide** (one could open the bootloader). Give each its own gesture. *Owner.*
6. **Stale pin table and a ghost part** in older eng files. Mark them superseded.
7. **Missing pieces:** PITCH CV OUT needs a DAC channel; OSC 3 CTL must be read; keyboard tracking can't reach "full".
8. **Power:** the speaker isn't in the power budget; loudness outdoors is untested.
9. **Pops** in phones and line at power-on. Add an output mute.
10. **MIDI questions for the owner** (CC 10, effect-amount CCs, channel, extras): see [MIDI](features/midi.md).
