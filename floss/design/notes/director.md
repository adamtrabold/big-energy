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

---

## Concept round 1: steer, READY and scores (2026-11-22)
Judged: `concepts/compare-faces.png`, `bow/mock-A-look.png`, `tide/mock-A-look.png`, all six concept docs and both common docs. KEPT judged from compare-faces plus its docs (its mock-A not opened). I didn't read `jobs.md` in full.

### Rulings on the open calls
1. **BOW's coral stays on the pressure selector, not on the collars.** "One coral control per concept" is a clean family rule, and 25 coral collars break it. Coral felt also soils in a park. The selector names what a lean does, so it's the right word for "life in the finger".
2. **The middle-C rim tick is enough,** as long as it can also be felt (a small notch at the rim, not just ink: eyes-closed rule). Middle C belonging to the upper half is the usual convention on split keyboards. **24 keys is closed;** it doesn't go to the owner.
3. **BOW's 2.6 mm tab clearance:** move the strand columns back 3 mm (y 58–92). No knob sits in the column's x span, so that's free. Keep the collars Ø 16.7 on every key, so the lean feels the same everywhere.
4. **TIDE's empty back third:** don't fill it with controls. Its depth has to come from something: the board plus the speaker box, then a proportion check (the owner wanted the case ratio "derived from the dimensions of the device" on Big Energy). The lantern field is TIDE's face, so size it as a deliberate window worked out from the driver, and let the pebble shrink to fit. Felt left over from HUSH's old board is not a reason.

### Kill: KEPT
It can't get to 9. Its point of view is "look 1974, feel new", and it fails both halves. Visual's own note: ONE SHEET's staggered Choc caps read as a modern mini keyboard, so the face is 1974 in layout only. Systems (rightly) moved velocity to loudness, so its touch is what any modern keyboard does: loud strike, vibrato lean. Making 1974 visible would need materials outside the family, which breaks the shared universe. The owner asked to "innovate on the original string synth", and he left the Model D because it wasn't inspiring. BOW does everything KEPT does and more, and KEPT's only edge (cheaper, slimmer) isn't the owner's priority (no budget ceiling).
**Salvage:**
- the bass voicing on the left-half bus (a cheap fallback if BOW's strands prove too costly);
- velocity as loudness, as a firmware curve option in BOW;
- "ensemble" as a plain label if the owner reads "shimmer" as an effect name.

### READY: BOW, TIDE

### Scores (concept phase: the idea)
**BOW: 8.** The most complete idea. The lid has a job, which answers "smaller CATHEDRAL?". Strands per half are what "floss" means and close to the Antiphon. Strike, lean and lift make a whole bow stroke. Likely owner objections:
- (a) **Signal order:** shimmer and depth (an effect) sit in the left region, before the strands and the voice. That breaks his "synth → fx → output" rule from Big Energy.
- (b) **A visible blank slot** (rear right, a dashed circle) at one end. It's asymmetric, and he dislikes gaps.
- (c) **Dark naturals:** the reversed key colours are an open owner question on Big Energy.
- (d) **Lap tipping** with a speaker box in the standing lid.
- (e) **Chip count:** 25 VCAs, 13 counters and 19 CD4066s, about 57 DIP chips plus the Daisy, in a 286 × 132 base with the battery. Build effort is J21.

Fixes:
1. Put the ensemble (shimmer, depth) after the voice in signal order: in the right ("room") region with echo and reverb. Then rebalance. Or argue it on the panel with a heading that makes the ensemble part of the voice. I prefer moving it.
2. No blank slot: rebalance both rows so the face is symmetric about the gutter, with no dashed circle.
3. Eng: the centre of mass at 120° on a lap. Show the lap pose, or a lower stand angle.
4. Show the normal key colouring beside the dark one, so the owner sees the choice. Bundle it with Big Energy's open question.
5. Eng: board area for the 25 VCAs, 13 counters, 19 switches and the battery under CATHEDRAL's base. If it doesn't fit, say where the strands fall back (the bass-bus voicing from KEPT).
6. Move the tab columns back 3 mm (ruling 3).
7. "Thinning without pressure": keep it, but label it a test-key item. If it annoys, it goes.

**TIDE: 7.** The most distinctive idea. Plant-and-tend HOLD, with a re-strike to pull a note out, is genuinely new. So are inverted velocity and pressure that plants drift. It's the strongest fit for "take this to the park and be inspired". But the face contradicts the idea: 16 round controls plus HOLD is as many as BOW, on the concept that's meant to be quietest. Likely owner objections:
- (a) The panel is busy for a "quiet" instrument.
- (b) An empty back third.
- (c) Felt in a park: dirt, damp, pilling, sun fade.
- (d) Grey felt sits outside the family's walnut and cream.
- (e) No registers. The split he asked for (two parts, an octave each) matters less here.
- (f) Which notes are held is invisible (honest, and minor).

Fixes:
1. Make the panel visibly the leanest, at 13 or fewer round controls. For example, one LENGTH knob replaces ATTACK and RELEASE (velocity places each note within it). Keep the settled echo sync.
2. Size the depth from the board plus the speaker, and make the lantern field the deliberate back face (ruling 4).
3. Answer the felt question: a removable, washable skin, or a tougher wool blend, said plainly.
4. Bring the felt into the family's palette (oatmeal or warm cream rather than mid-grey), or show why grey belongs.
5. Show the split's job in TIDE: a flow and a picture of two planted parts (left low, right high).
6. Make the HOLD peg unmistakable from a key by touch, not only by size.
7. Test swatch: the lantern through Ø 1.7 holes in felt, in shade.

**KEPT: 6, killed** (reasons above).

### What keeps blocking a 9 (first scored round, a pattern to watch)
**The body's leftovers are driving the layout.** Every concept wears an inherited family body, and its spare dimensions have turned into blank slots (BOW, KEPT, TIDE), an empty back third (TIDE) and a face larger than its idea (TIDE). That's Big Energy's lesson again: "when the owner names a gap, find what forces the gap before styling what fills it." Dimensions must come from the instrument's needs, not the borrowed shell's.
The convergence worry didn't recur: BOW and TIDE differ in kind.

### Next
Round 2 on BOW and TIDE with the fixes above. Eng sizing (strand chips, lid box and lap, TIDE's depth) is the gate for BOW's next score.

---

# REV 2: the module (concept phase restarted, round counts reset), 2026-11-22
The owner turned floss into a keyless sound module played by a carried travel keyboard over USB-C. It's a family principle (Big Energy changes too). There are no built-in buttons, and proportions are open. Process: requirements first (`floss/REQUIREMENTS.md` rev 2, T1–T12 baseline; any beat or miss is a trade-off for him), then an engineering gate (`floss/eng/module.md`). **He measures nothing:** choices rest on published evidence. SMD is allowed. Round-1 BOW / TIDE scores are history (they assumed built-in keys).

## Jam-module pass 1, my turn 3
- Read: the REV 2 brief section, owner.md 09:22 onward, REQUIREMENTS rev 2, the jobs rev 2 table, the eng/module.md highlights, both jam turns, sketch 2a (FALLBOARD). Sketch 2b not opened.
- Randomness: "Is the tuning appropriate?" (15/20); field: orchestral instrument cases (6/12).
- **Key insight:** with a borrowed keyboard, floss no longer owns the finger. Lean and lift depend on the guest's sensors. floss owns time and the panel. TIDE's ideas strengthen and BOW's weaken.
- **Rulings:**
  - Concepts differ on the **kit only**. **One floss voice** across all kits (systems to write it): TIDE's plant-and-tend HOLD, DRIFT and unplug-proof HOLD; BOW's strands per half; velocity = speed; the PRESSURE fallback ladder. No kit × voice pairing.
  - **Forward:** FALLBOARD (lead: a rigid bed for the lap, the best lid), SPINE (rival: smallest closed footprint, 400 × 140 × ~55–60), CLOTH (the two-package test; module 270 meets T4).
  - **Killed:** LAMP (light folded into FALLBOARD and SPINE), TETHER (strap = accessory on the S4 inserts), BACKBONE.
  - **S8** (every module / kit 400 wide): yes, as a PROPOSAL **for the owner** (a family decision). Pitch: "floss adds no width to the keyboard you already carry." CLOTH's BLOCK is the exception.
  - Split = fixed note (rule A) + brass target. Learned split (B) rejected.
  - Two lights (status and port). One power switch on the module (SPINE's open = on dropped). Add job 29.
  - RAIL one row: keep, but grouped by countable gaps; HOLD with touch; strands as 3 tabs at each end if they survive.
- **Push:** end blocks hold the keyboard by its ends (no bands across keys; from the orchestral case); an accessory pocket for the cable; "own the outline, host the keys" for every kit; host port centred in the gutter; S4 inserts.
- **Likely owner objections:**
  1. 400 vs 290 width;
  2. weight near T5;
  3. **eng's slim radiator "needs one acoustic measurement"**, which breaks "measures nothing". Assume a published-data speaker (32–38 mm body) unless eng finds published pairing data. Flagged to the orchestrator for eng now;
  4. hand-craft steps (bookcloth, sewing, struts) listed honestly;
  5. a quiet rail reading as an accessory;
  6. bands over keys (fixed);
  7. an ungrouped row (fixed).
- **Watch:** the bed's spare width (67 mm with a 325 mm keyboard) must stay a frame, never a place to put things. The leftover-space pattern from round 1 again.
- **Owner questions to hold:** S8 / 400 wide; one package or two; slim class only or all (CLOTH carries all).
- **Next:** pass 2, systems first (the one voice, RAIL fit, end-block range, speaker flag), then visual (the redrawn kits and a closed-kit comparison sheet), then I end the jam and call concepts.
