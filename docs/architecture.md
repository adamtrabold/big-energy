# Architecture

An analog synth voice with one small computer beside it. The **sound is analog** from the oscillators to the outputs. A **Daisy Seed** reads the keys and knobs, tunes the oscillators, speaks MIDI, and adds **digital echo and reverb** that are mixed back in.

*Updated 2026-11-13 (evening: every feature doc written; budgets recounted) · systems designer · "Decided" means recorded in the [owner record](../design/owner.md); everything else is proposed.*

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

Panel words follow the owner's one-word rule (19:57) and the director's [vocabulary](../design/branches/concepts/cathedral/vocabulary.md); feature docs give the engineering name once, in brackets.

---

## The blocks

| Block | What it is | Feature doc |
|---|---|---|
| Voice | 3 VCOs, mixer, 4-pole ladder filter, analog contours, VCA | [voice](features/voice.md) |
| Keys | 25 silent Choc V2 keys, Hall-sensed velocity, printed or bought key heads | [keys and velocity](features/keys-and-velocity.md) |
| Aftertouch | pressure strip under the keys, touch: mod · off · filter | [aftertouch](features/aftertouch.md) |
| Bend and mod | sprung one-axis stick, mod knob, blend, mod VCA | [bend and mod](features/bend-and-mod.md) |
| Paraphonic | voices: 1 · 3 · 4 (mono / para / para+4), digital 4th oscillator | [paraphonic](features/paraphonic.md) |
| Tuning | autotune, held-note correction, drift | [autotune and drift](features/autotune-and-drift.md) |
| Effects | echo (4 types) → reverb (4 types), wet-only return | [effects](features/effects.md) |
| Echo sync | FREE / SYNC, TAP, MIDI clock | [echo sync](features/echo-sync.md) |
| Outputs and panning | stereo phones and line, one speaker, out pan, echo pan, link | [panning and stereo outputs](features/panning-and-stereo-outputs.md) |
| MIDI | played and automated from a DAW | [MIDI](features/midi.md) |
| Power | internal battery (11.1 Wh in the base), one USB-C | [power and battery](features/power-and-battery.md) |
| Firmware and gestures | updates, boot and settings gestures | [firmware update and gestures](features/firmware-update-and-gestures.md) |
| Connections | jacks, USB-C, CV / gate | [I/O](features/io.md) |
| Body | CATHEDRAL (FOLD two-half body) | [enclosure](features/enclosure.md) |

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

## Settled today (2026-11-13)
| Item | Status | Where |
|---|---|---|
| Stereo phones + stereo line out, one speaker; mono on a TS cable | **decided** (owner 15:22–15:23); the line-out jack count is owner question 4 | [panning and stereo outputs](features/panning-and-stereo-outputs.md), [I/O](features/io.md) |
| Out pan + a separate echo pan; link = the echo follows the dry | **decided** (owner 15:53–15:54); circuits proposed | [panning and stereo outputs](features/panning-and-stereo-outputs.md) |
| FREE / SYNC switch (option B), tap, MIDI clock | **decided** (feature); behaviour proposed | [echo sync](features/echo-sync.md) |
| A 4th mux (64 inputs) | proposed (review must-fix); eng confirms timing | below |
| PARA+4 path: option A, a 5th MCP4822 frees the Seed's DACs | proposed; owner question 9 | [paraphonic](features/paraphonic.md) |
| The speaker counted in the power budget | done: ≈ +0.5–0.8 W loud (unverified) | [power and battery](features/power-and-battery.md) |
| The battery in the base's rear strip (CATHEDRAL), 4 × 750 mAh, 1S4P | proposed; eng checks the board window | [power and battery](features/power-and-battery.md), [enclosure](features/enclosure.md) |
| One-word panel labels | **decided** (rule); words from the director's vocabulary | [CATHEDRAL §18.8](../design/branches/concepts/cathedral/how-it-works.md) |

---

## Budgets

One table for every shared resource.
- **Today:** the locked spec plus aftertouch.
- **Decided:** adds what the owner has approved since.
- **Proposed:** adds the team's and the review's fixes.

| Resource | Capacity | Today | + decided | + proposed | Action |
|---|---|---|---|---|---|
| **Mux inputs** (keys, knobs, switches) | 48 (3 muxes) → **64 with the 4th mux** | 48 | **53** (voices, FREE / SYNC, out pan, echo pan, link) | **57–60** (+ osc 3 track, phones sense, battery, wave 1 for the 4th oscillator; TS sense 0 with two line jacks; STAT / VBUS optional) | **add the 4th mux** (open item 1): 4–7 spare |
| **Daisy pins** | 31 | 27 | 28 (MIDI out) | **30–31** (digipot CS, 5th DAC CS, 74HC4053 control; **30 with two line jacks**) | tight but fits; D16 the last analog spare |
| **Pitch / CV DACs** | 8 (4 × MCP4822) + 2 (Seed) | 10 of 10 | 10 | **12 + digipot** (a 5th MCP4822 takes velocity and mod depth) | frees the Seed's DACs: OUT1 → the 4th oscillator into the ladder, OUT2 → **pitch CV out** (owner question 9) |
| **Codec** (stereo in / out) | 2 in, 2 out | in L = FX send + VCA null; in R = filter cal; out L / R = stereo wet | same | **same** (option A keeps the 4th oscillator off the codec) | none |
| **Power** | **11.1 Wh** in CATHEDRAL (4 × PiShop 952540, base rear strip) | load ≈ 2.4–4.4 W at 5 V (Daisy era) → **≈ 1.9–3.7 h** | + stereo stage (few mA) | **+ speaker ≈ 0.5–0.8 W loud → ≈ 1.7–2.9 h**; − Hall gating and a 3.3 V buck (≈ 0.65–1.35 W) → up to ≈ 8.6 h | **≥ 2 A 5 V boost** (must-fix); measure the Seed and the LM386; pack size is owner "Show me both" |

<details><summary>The 4th mux (open item 1), with the recounted allocation</summary>

- **Part:** a 4th **CD74HC4067** sharing S0–S3 (PC9–PC12), its output on **D20 (PC1, ADC3)**. The battery divider moves from D20 onto mux D. ≈ $0.60.
- **Conversion:** ADC3 converts **mux C then mux D** in each mux step (scan mode, 2 ranks). The keys' ADC1 + ADC2 are untouched. Eng: confirm both conversions fit the ≈ 3 µs step (UNVERIFIED; at 1 Msps each takes ≈ 1 µs).
- **Allocation (64):**
  - **mux A** = keys 1–16;
  - **mux B** = keys 17–25, 4 controls, Hall-rail monitor, AT toggle, AT FSR;
  - **mux C** = 16 controls;
  - **mux D** = VOICES (para), FREE / SYNC, out PAN, echo PAN, LINK, oscillator 3 TRACK, PHONES sense, TS sense (or spare with two jacks), battery, charger STAT, VBUS, WAVE 1 (for PARA+4's matched waveform), **4 spare**.
- **D16** stays the last direct analog spare.
</details>

<details><summary>What fills the mux (53 → 59)</summary>

- **Decided additions:** VOICES switch, FREE / SYNC, out PAN, echo PAN, LINK (+5).
- **Proposed:** oscillator 3 TRACK read, phones-in sense, TS sense on line out, the battery divider moved onto the mux (+4), and optionally charger STAT / VBUS (+2).
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
1. **The mux is full.** Add a 4th mux on D20 and move the battery reading onto it (allocation above). *Eng: confirm the two conversions fit the 3 µs step.*
2. **Line out on a mono cable:** two jacks (L / MONO + R, team recommends) or a reworked single jack; and should line out mute the speaker? *Owner question 4.*
3. **The 4th note's path (PARA+4):** option A, a 5th MCP4822 (≈ $4, one pin), recommended; B (codec R, effects mono) or C (drop it). *Owner question 9.*
4. **Pitch CV out** comes from the Seed's DAC1_OUT2 once option A frees it (12-bit, ≈ 1.5 cents per step over 5 V, buffered to 1 V/oct).
5. **Filter track can't reach full** (one 3-way switch): off · 1/3 · 2/3 today; proposed off · 1/2 · full by re-resistoring or firmware. *Owner question 7, eng.*
6. **Power:** a ≥ 2 A boost (must-fix); measure the Seed's draw and the LM386 with the real driver; Hall gating if the SS49E settles in ≤ 50 µs. Pack size (11 vs 22 Wh) is open.
7. **Closing height condition:** three lid switches close over base knobs, so the lid toggles must stand ≤ 13.5 mm proud of the face, or R-LOW grows from 55.2 to ≈ 56.7 ([CATHEDRAL §18.4](../design/branches/concepts/cathedral/how-it-works.md)). *Eng picks the toggle part.*
8. **Battery in the base:** the base board needs a window in the rear strip and the hinge ribbon's base header moves (CATHEDRAL §16.2). *Eng.*
9. **Firmware update path:** ROM DFU on the Seed's own port without VBUS on its connector: bench check ([firmware and gestures](features/firmware-update-and-gestures.md)).
10. **Stale pin table and a ghost part** in older eng files: mark them superseded.
11. **Owner questions from the feature docs:** bend range (8), filter note in chords (10), drift depth (11), the aftertouch word (6), MIDI (5). All on the [decisions page](../design/decisions-open.md).

**Closed today:** peg necks rubbing the floating strip (deck holes Ø 13.2, [keys and velocity](features/keys-and-velocity.md)); TAP gestures colliding (split, [firmware and gestures](features/firmware-update-and-gestures.md)); power-on pops (output mute, [I/O](features/io.md)); oscillator 3 track read (mux D); the speaker missing from the power budget.
