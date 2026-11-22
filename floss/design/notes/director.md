# floss design director notes

Started 2026-11-22. Concept phase, jam pass 1 (my turn 3). No scores yet.

## What I've read
- `floss/design/BRIEF-CONTEXT.md`, `design/owner.md` (2026-11-21 onward), `floss/README.md`, the jam (turns 1–2), `sketches/visual-jam1-sail.png`.
- Big Energy director notes (`design/notes/director.md`) for taste only. Owner taste from there that will bite floss:
  - Organisational logic first: grouping must make sense ("the items do not appear to be grouped or ordered in a way that makes logical sense"); he went back to a tree map of categories before layout.
  - Signal order on the panel: synth → effects → output.
  - Off-centre in the middle reads badly to him ("off center in that middle section is bad looking"). Symmetry and harmonious, proportional spacing.
  - One plain word per label; better words beat jargon.
  - He checks his own literal words first; don't reinterpret them. Draw them and ask.
  - When he names a gap, find what forces it before styling what fills it.
  - He wants real thinking ("i dont think you're really thinking here").
  - He wouldn't accept a 9 as a 10 on Big Energy; expect a high bar.

## Facts checked
- Solina: six buttons (contrabass, cello, viola, violin, trumpet, horn); contrabass and cello only on C2–G3; bass volume slider; crescendo (attack) and sustain length (release) sliders; modulation and phaser buttons. Source: notebook.zoeblade.com Solina guide. So per-half registers have a 1974 precedent.
- Big Energy keys: Choc V2 + magnet in the top over a linear SS49E Hall sensor; velocity from time between two thresholds (`eng/budget-variant.md` §v1.4b). Continuous travel means release (lift) speed is readable too (to confirm by eng).
- NOT checked: the Solina ensemble's three BBDs / 120° LFOs.

## Randomness used (jam pass 1)
- Oblique Strategy "Give way to your worst impulse" (9/30) → KEPT.
- Field: pipe organ building (12/25) → WIND, swell box, registers as pitch strands.
- Twist: "it must work with eyes closed" (1/10) → tabs over levels; octave pointers read by touch.

## My steer (jam pass 1)
- The jam had converged to one concept under four names (BOW / SIX STRANDS / SAIL / STOPS). Asked for three concepts that differ in where floss's life lives:
  1. **BOW**: each finger (per-note velocity = bow speed, pressure, lift speed); SAIL lid soundbox.
  2. **WIND**: a shared breath (modelled wind sag across held notes, collective pressure); format open; lid-as-swell-box wild card (likely weak).
  3. **KEPT**: faithful Solina-order panel, all innovation in the keys; ONE SHEET slab.
- Shared across all: two octave knobs = the split; per-half controls over each half; tabs not levels; one status light (3 meanings).
- Dropped: ROUNDS/BELFRY, STOPS (merged), BIG HANDS, LUTHIER, the flower-of-life rose, five lighthouse rhythms, the label "SET". Lantern = maybe, never a concept driver.
- Open for systems: register answer (Solina low-only / pitch strands / L-both-R), pressure selector's place in signal order, hold on left only or all.

## Owner objections to watch (all concepts)
1. "Analog voices?" with microcontroller tones: each concept needs one honest sentence.
2. Split line half a key off centre (12 + 13 keys) vs his off-centre dislike.
3. Jargon labels (feet, orchestral names on switches, SET).
4. "Smaller CATHEDRAL?" for SAIL.
5. Be hard on BOW: it's the team favourite and partly my framing.

## Next
- Jam pass 2: systems, then visual, then me. I'd like WIND vs BOW argued (are they one instrument with a switch?). Then decide what goes to concepts with READY.

---

## Jam pass 2 (my turn 5), 2026-11-22
- Systems turn 4: killed WIND (same hardware as BOW; a philosophy on a toggle), proposed TIDE, split registers by concept, verified the ensemble (Sound on Sound: three delay paths, LFOs ≈ 1 Hz and ≈ 6 Hz, 0/120/240°), flagged off-centre split (9 mm left on 25 keys) and the 24-key option, wrote the "analog voices" sentence (accepted).
- Randomness: Oblique Strategy "Listen to the quiet voice" (16/20) → TIDE's inverted velocity meaning.
- **Decisions:**
  - WIND killed; fixed breath (sqrt sum, ~200 ms recovery, no pitch sag) in all concepts; FILL = shared-strip fallback. Swell-box lid killed.
  - **TIDE takes the third slot**, on condition that touch isn't idle: soft strike = longest, most wandering note; pressure while laying a note down sets its held drift; DRIFT is TIDE's hero knob (fixed small drift in BOW/KEPT).
  - Concept table: BOW (finger; strands of pitch, 6 tabs; HOLD left; SAIL lid) / KEPT (1974; Solina tabs + low-left register; HOLD left; ONE SHEET slab) / TIDE (time; no registers, one TONE; HOLD all; format open, visual to justify).
  - Shared: octave knobs = split; per-half controls over each half; TOUCH group first in signal order (TOUCH → registers → TONE → SHIMMER → ECHO → REVERB → VOLUME); lift speed sets tails (spring limits the fast end); one status light, three meanings.
  - Keep 25 keys. Visual owns the off-centre fix; 24 keys only goes to the owner if the visual answer fails.
  - Fix word clash: SWELL is both attack knob and pressure position. TONE double use accepted (same parameter).
- **Pattern so far:** convergence (structure B makes every idea "firmware on one engine") and settled asks going idle. Guard: concepts must differ on what velocity means, registers, HOLD scope and format.
- **Biggest risk:** BOW's 75 tone outputs (strands) may need FPGA/CPLD; eng to size before scoring; build-skill question for the owner.
- **Owner questions held:** fixed breath vs louder-with-every-key; FPGA/CPLD acceptable?; 25 off-centre vs 24 centred (only if needed).
- **Next:** visual pass-2 turn, then I end the jam and decide READY (expected: BOW, KEPT, TIDE).
