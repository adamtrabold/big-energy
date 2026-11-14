# Paraphonic
Status: **partly written 2026-11-13** (the PARA+4 audio path, review must-fix O3). The rest is to be written · sources: ../../design/owner.md (2026-11-13 paraphonic entries), ../../design/reviews/2026-11-13-audio-synth-review.md items 4, 18

## What it does (player's view)
_To be written._

## Owner decisions (verbatim, linked to owner.md)
_To be written._

## How it works
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
_To be written._

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
