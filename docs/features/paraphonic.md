# Paraphonic
Status: per item below · last updated 2026-11-13 · sources: [owner.md](../../design/owner.md) (paraphonic entries), [audio / synth review](../../design/reviews/2026-11-13-audio-synth-review.md) items 4, 9, 11, 18, [architecture](../architecture.md) open item 3

Panel words follow the one-word vocabulary: the switch reads **voices: 1 · 3 · 4**. The engineering names (MONO / PARA / PARA+4) are used below where they name the modes.

## What it does (player's view)
- **voices 1** (mono): one note at a time, all three oscillators stacked, low-note priority. The Model D.
- **voices 3** (para): up to **three notes at once**, one oscillator each, through the **one filter** and the **shared envelopes**. Chords and pads on a Model D voice.
- **voices 4** (para+4): adds a **digital fourth oscillator** from the Daisy, so four-note chords. It goes through the same analog filter and amp as the others.
- In para, **pitch 2 and 3 become fine detune** (each note is in tune, slightly apart), and the oscillators all play in **octave 1**'s octave.

## Owner decisions (verbatim, linked to owner.md)
- "would love to add it but how would keytracking work with the different oscillators?" → explained (each note tracks; the filter follows the highest note by default; shared envelopes).
- "how does it know what note to send to what oscillator" → explained; then "yeah so firmware could even improve the paraphonic control over time right?" → yes.
- **Recorded as: PARAPHONIC MODE APPROVED (MONO / PARA / PARA+4 toggle). Firmware is updatable and expected to evolve.**
- "Labels should only be one word…" (19:57): the switch reads **voices: 1 · 3 · 4**.

## How it works
**Allocation (firmware, recorded in owner.md 124):**
- A new note goes to the **next free oscillator**.
- With fewer notes than oscillators, the spare oscillators **double the lowest note**, so a single note in para still sounds full.
- When all are busy, the **oldest note is stolen**.
- Oscillator 3 with **track: off** (drone / modulator) is **left out of allocation** (review 11): para then has two voices (three with +4).

**Pitch:**
- Each oscillator's coarse + fine DAC gets its own note.
- **octave 1 sets the octave for all** (octave 2 and 3 are ignored in para; review 18, proposed), so a chord doesn't scatter across octaves.
- pitch 2 / 3 act as **fine detune** (owner.md 124).
- Bend, glide and drift apply to every note.

**Filter and envelopes:**
- One ladder. Its keyboard CV follows the **highest note** by default; a key combination changes that (owner.md 124; the combination is in [firmware and gestures](firmware-update-and-gestures.md), to be defined).
- The two envelopes are shared and analog. In para they **retrigger on each new note-on** (review 18, proposed), so a note added to a decayed chord still sounds.

### The PARA+4 audio path (review must-fix, architecture open item 3)
**Problem:**
- PARA+4 (approved) uses a **digital 4th oscillator** on the Daisy.
- Both codec outputs are the stereo wet return, which joins **after** the VCA and filter.
- So the 4th note has no way into the analog filter and VCA. As drawn, it can't sound like the other three.

**Options:**

| | Route | Behaviour change | Cost / budget |
|---|---|---|---|
| **A. A dedicated DAC for the 4th oscillator (recommended)** | Move **velocity and mod-depth CVs** onto a **5th MCP4822** (both are slow CVs). That frees the **Seed's two internal 12-bit DACs** (DAC1_OUT1 / OUT2, DMA-driven at 48 kHz). DAC1_OUT1 then plays the band-limited 4th oscillator → RC reconstruction filter → a fixed resistor into the **ladder's input summing node in the base** (after the hinge ribbon, so no ribbon change) | **none**: effects stay stereo, NOISE / EXT stays free. Its level is set in firmware to match a full-up oscillator; the mixer pots don't control it (they're analog, and the firmware can't see them) | +1 MCP4822 (≈ $4, UNVERIFIED) + 1 chip-select pin. Pins go to 30–31 of 31 (fine if line out uses two jacks, which frees the 4053 pin). Seed DAC quality ≈ 11 ENOB (ESTIMATE): fine for an oscillator that goes through the filter |
| B. Codec OUT R → the mixer's input (EXTRA, SOURCE = input) | a 74HC4053 steers OUT R to the mixer's EXT input while PARA+4 is on; the wet return goes mono (OUT L to both sums) | **yes:** effects go mono in PARA+4 and SOURCE must sit on EXT. **Owner** | +1 4053 section, 1 control pin |
| C. Make the toggle 2-way (MONO / PARA) until a path exists | — | **yes:** PARA+4 disappears. **Owner** | 0 |

**Recommendation: A.**
- It keeps the approved behaviour exactly, with no mono effects and no taken input.
- It costs one bought chip and one pin.
- Eng confirms: the DMA load at 48 kHz on DAC1, and the reconstruction filter. The 4th oscillator needs a band-limited (PolyBLEP) waveform, matched to WAVE 1's position read by the firmware (UNVERIFIED that WAVE 1 is read; add it to the mux if not).
- **Bonus:** DAC1_OUT2 is freed too. Proposed for **PITCH CV OUT** (no channel today; review 9): 12-bit, ≈ 1.5 cents/step over 5 V [CALC], buffered and scaled to 1 V/oct.
- **Status: proposed** (no owner decision needed unless he objects to the cost).


## Controls and states
| Control | Positions | Notes |
|---|---|---|
| **voices** | 1 · 3 · 4 | left · middle · right (the panel's throw convention). Read on mux D |
| octave 1 | as voice | sets the octave for every note in 3 / 4 |
| octave 2, 3 | — | ignored in 3 / 4 (proposed) |
| pitch 2, 3 | ± fine | detune in 3 / 4 |
| oscillator 3 **track** | off · on | off: osc 3 leaves the allocation |
| mixer 1 · 2 · 3 | levels | **set them equal for chords** (the firmware can't see them) |
| wave 1 | shape | the 4th oscillator copies it (PolyBLEP; needs WAVE 1 on the mux, counted in mux D) |

## Edge cases
- **A turned-down oscillator is a silent note:** the mixer pots are analog and the firmware can't see them, so a chord note landing on an oscillator at 0 is lost (review 18). The manual says: set 1 · 2 · 3 equal for chords.
- **Different waveforms per note:** each oscillator keeps its own wave, so a chord's notes can differ in tone. That's a sound, not a fault.
- **Oscillators' mod on in para:** osc 3's FM lands on the other chord notes and sounds clangy (review 18). The manual covers it.
- **Velocity in para** re-scales the whole chord's loudness on each new note (shared VCA; review 18).
- **Switching voices while holding notes:** proposed: the change takes effect at the next note-on, and held notes are re-allocated without a click.
- **voices 4 with no 4th-oscillator path** (if option A isn't built): position 4 behaves as 3. Option C below makes it honest.

## Interactions with other features
- **Voice:** shares the filter, envelopes and VCA ([voice](voice.md)).
- **Keys and velocity / aftertouch:** pressure is channel-wide, so it acts on the whole chord ([aftertouch](aftertouch.md)).
- **MIDI:** notes from a DAW are allocated the same way. Channel pressure out is unchanged ([MIDI](midi.md)).
- **Pitch CV out:** carries the **lowest** note in para, matching low-note priority (review 9, proposed). It comes from DAC1_OUT2 once option A frees it.
- **Effects:** unaffected under option A (stereo stays). Under option B they go mono while voices 4 is on.

## MIDI
- Note-on / off feed the allocator; sustain (CC 64) holds every allocated note.
- The voices switch is never changed by MIDI (owner: MIDI never flips switches).

## Budget (pins / mux / DAC / power / cost)
- **Mux:** voices switch +1 (mux D), oscillator 3 track +1, wave 1 +1 (mux D, for the 4th oscillator's matched shape). See [architecture](../architecture.md).
- **DAC (option A):** +1 MCP4822 (velocity, mod depth) and +1 chip-select pin; the Seed's DAC1_OUT1 plays the 4th oscillator and DAC1_OUT2 becomes pitch CV out. Pins 30–31 of 31.
- **CPU:** one PolyBLEP oscillator at 48 kHz via DMA. Small next to the reverb (ESTIMATE; eng confirms the DMA load).
- **Cost:** ≈ $4 + passives (UNVERIFIED).

## Open questions
1. **The 4th oscillator's path:** A (a 5th DAC, recommended, no behaviour change), B (codec R into the mixer, effects mono), or C (2-way switch). The team proceeds with A unless the owner objects to the cost.
2. **The filter-tracking key combination** (highest note by default): define it in [firmware and gestures](firmware-update-and-gestures.md).
3. **octave 1 for all in para** and **retrigger on each note-on:** proposed defaults from the review. Firmware can change them later.

## Status (decided / proposed / open, item by item)
| Item | Status |
|---|---|
| Paraphonic mode, MONO / PARA / PARA+4 | decided |
| Allocation (next free, spares double the lowest, oldest stolen), filter follows the highest note, shared envelopes, pitch 2 / 3 = detune | proposed (orchestrator's answer, accepted in the approval) |
| Panel word "voices: 1 · 3 · 4" | proposed (director's vocabulary, under the owner's one-word rule) |
| PARA+4 path option A (5th MCP4822, Seed DAC1 → ladder input) | proposed |
| octave 1 for all, retrigger per note, osc 3 track off leaves allocation, pitch CV = lowest note | proposed |
| Filter-tracking key combination | open |
