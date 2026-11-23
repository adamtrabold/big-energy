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

## Jam-module pass 2, my turn 6 (jam closed)
- Read turns 4 (systems) and 5 (visual). Checked sheets 3a and 3c by eye; 3b taken from the text. `eng/module-r2.md` is still pending (speaker by virtual model from published data, USB-C host, fit, weights).
- **Kits to concepts:** FALLBOARD (lead), SPINE (rival; the sag was mostly a false alarm, since the spine runs across both thighs on a lap), CLOTH (labelled a bench-and-table kit; the two-package / T4 / charger / chunky-mini test).
- **Accepted:**
  - the one voice (turn 4 §1);
  - REPEATS tied to ECHO;
  - fixed voice pools 12 / 13 (eng to confirm);
  - layout D for every kit;
  - S8 ≈ 412 as an owner proposal ("floss adds about an inch to the widest travel keyboard");
  - end blocks with one brass scale, no linkage;
  - tab words low · main · high;
  - brass frets;
  - SPINE's stop-at-flat spine, no slat;
  - the gutter as pocket, no charger in the rigid kits;
  - sheet c as the owner's comparison, plus weights and lap views.
- **Split-scoped HOLD:** goes to the owner as a proposal.
- **New rulings:**
  - **coral moves to DEPTH**, with the shimmer group on the exact axis (the wordmark above, host port and target home below). The lean is the guest's now; shimmer is the owner's stated draw;
  - **FALLBOARD and SPINE share the same panel.** SPINE's extra depth goes to the speaker, not to controls. CLOTH must prove the same controls fit 270.
- **Must-shows for concepts:** turn 6 §4 (13 items: bench and lap, closed with weight, packing, panel 1:1, keyboard range, cable path, split target and home-octave line, rear wall, states incl. job 29, family reuse, making steps with sources, thickness on both speaker paths until eng lands, the analog sentence).
- **Owner objections to pre-empt:** size (FALLBOARD ≈ 3 laptop volumes), weight T5, craft load, the "home octave" instruction, the lid lamp, the speaker path.
- **Owner questions held for the concept send:** board / book / cloth; S8 412; split-scoped HOLD; charger; slim only or all.
- **Next:** systems writes jobs.md rev 3, then the concepts. I score concepts when both designers have built them, judging the idea per the brief, harder on FALLBOARD because it's the favourite I helped shape.

## Owner 13:25, folded into the closing rulings (addendum to turn 6)
- Owner, verbatim: "The module does not have to match keyboard width." That's direction; I'm not re-arguing it.
- **Withdrawn:**
  - S8 ≈ 412 (the 412 now belongs only to the carry: 404 inside, end blocks);
  - layout D (it only existed for the single-row rail; a ≈ 270–290-wide body takes two rows);
  - the owner question about S8.
- **New:** **one floss module in all three kits**, sized by its parts (eng minimum ≈ 250–290 × 90–110, thickness from module-r2). The concepts are now three carries for one module. That fits job 28 / systems' "fix the connections, not the sizes" (S1–S7, the S4 inserts).
- **Kept:** the one voice; split-scoped HOLD (owner proposal); REPEATS tied to ECHO; pools 12 / 13; groups countable by touch; low · main · high; each end owns its half (octave + tabs); coral on DEPTH with shimmer on the exact axis; end blocks + one scale; pocket; no measured speaker; one switch; two lights; job 29.
- **Rework per kit:**
  - FALLBOARD: what sits beside a narrower module in a 412 bed. Only a real job (pocket, charger) or nothing. No walnut cheeks to make up the width: watch the leftover pattern.
  - SPINE: boards no longer match, so rework it or drop it honestly.
  - CLOTH: gains (its module is the family module).
  - Each kit chooses and justifies how the module relates to the keyboard, open and packed.
- **Must-shows amended:** the panel drawn once, shared; each concept accounts for every area of the carry outside the keyboard and module.
- **Objection 1 eases:** "the module is about the size you asked for; the kit is the size of the keyboard you bring."
- **Watch next round:** SPINE may not survive the change. If its rework is a book with mismatched covers, it scores low and should be replaced or dropped rather than patched.

---

# Director handover: new director, concept round 2 steer 1 (2026-11-22)
I took the seat from here. Everything above is history: I use it to stay consistent and I don't defend its scores. Round-1 BOW / TIDE / KEPT scores belong to the keyed instrument and don't carry over.

## What I read
- `PRINCIPLES.md` (new today; binding), the REV 2 part of `BRIEF-CONTEXT.md`, `REQUIREMENTS.md` rev 2, `jobs.md` rev 3, `design/owner.md` from 09:22 to 13:55, the notes above (REV 2 and the 13:25 addendum).
- Concept round 2, both designers: `concepts/module/how-it-works.md` (still at 297 × 105 × 40) and `how-it-looks-and-feels.md`; the three kits' how-it-works and how-it-looks-and-feels files; `eng/module-r2.md` (summary, fit, weights).
- **Images opened and judged:** `module-1to1-A3.png`; `fallboard-A-in-use.png`, `fallboard-B-closed-and-packing.png`; `spine-A-in-use.png`, `spine-B-closed-and-packing.png`; `cloth-A-in-use.png`, `cloth-B-closed-and-packing.png`.
- I haven't read the jam in full; I worked from the turn-6 rulings and the addendum above.

## Randomness used (real draw: `python3` SystemRandom)
- Oblique Strategy: **"Use fewer notes."** Field: **sailing (dinghy fittings).**
- How I applied them: every part of every kit has to earn its place, or it goes (the lamp, filler pockets, the gutter, the engraved sentence, two-shade cloths). From the dinghy: fittings do one job each and sit where the load is. The hull is already sailing; I don't want more nautical styling than that.

## Rulings

### R1. The module: 280 × 105 × 35, 8 : 3 : 1 on a 35 mm unit, hull outline. ACCEPTED.
- **Why:** each size comes from a part. The panel gives 264 + 2 × 8 = 280, the speaker crown gives 105 and the driver body gives 32 + 3 = 35. The ratio then tunes those sizes rather than inventing them. That's the order PRINCIPLES §2 asks for ("derived from the dimensions of the device"; "make sense and be harmonious"). The halves are 4 : 3 each and the split axis falls between them, so the proportion shows the instrument's real structure, which is better than a story laid on top. The 297 version was anchored on paper, and the owner withdrew paper (13:51).
- **The hull:** every edge has a job: the straight front faces the keyboard and carries the rail, the 70-deep ends are where you pick it up, and the arc gives depth only where the speaker needs it. It's symmetric about the axis (§6) and it isn't a slab (owner 13:29). Accepted.
- **Conditions (the ratio has to stay honest):**
  1. 35 depends on eng confirming the deck-26 stack with the cells beside the crown. **If eng can't confirm it, the height goes to whatever the parts need and we restate the ratio. We don't fake 35.**
  2. Name the knob part with a published height, and derive the deck from it. Knob tops 8 mm above the deck may be too low to grip; if the knob needs more, the deck drops or the rim rises, and that is said openly.
  3. **Finger room behind DRIFT, SHIMMER and TIME:** the crown's raked foot (y 47) sits 0.5 mm behind those knobs' rear edges (y 47.5). Give at least 5 mm clear: move the crown foot back, steepen the rake, or reposition the driver (eng's call). Don't shrink the knobs.
  4. Grille open area ≥ 620 mm² (a Ø 46 field, or Ø 1.9 holes).
- **Systems must update `module/how-it-works.md` and every kit file:**
  - 280 wide; every x moves −8.5 (axis 140; frets 45.5 · 74.5 · 125.5 · 154.5 · 205.5 · 234.5); inserts at x 60 and 220 (still 160 apart);
  - rim and crown at 35 (not 40), deck 26, sunk deck, crown 70 wide on the axis with its raked front; the cells beside the crown (eng to confirm); the U-shaped board around the crown;
  - **§2: delete the 2√2 / paper argument and the Letter alternative.** Use visual's §1 table as the derivation;
  - the rear is **two flat port facets on the arc**, replacing "the rear wall stays flat";
  - every kit's closed thickness: FALLBOARD 43, SPINE 56, CLOTH about 5 mm thinner; the pockets beside the module ≈ 59 × 105 (before R6's changes);
  - **`jobs.md` job 30 still says "paper length":** rewrite it as "portable, makes sense, harmonious; a ratio derived from the parts; any outline" (owner 13:51, PRINCIPLES §2). Fix the rev-3 change table too;
  - job 6: drop the engraved line (R4).

### R2. Brass dividers: FLUSH. Raised is out.
- PRINCIPLES §6 is the owner's own words: "Use another method of separation if you think it's important to feel the sections." A raised fret in a 7 mm gap between Ø 14.9 knobs is exactly what catches the side of a finger turning a knob.
- **Flush brass inlay**, level with the deck. You find the groups by the wider gap (7 mm more than within a group) and by brass feeling cooler and smoother than the deck. That's the "other method".
- Making it: a strip glued into a slot printed in the deck, then sanded level. Systems lists the step with its source (job 26). No machining.

### R3. Lights: status stays on TAP's ring. No third dot.
- It's a shared universe: Big Energy's CATHEDRAL puts status on TAP's ring, so floss does too. A dot under the wordmark would be a third light (turn-3 ruling: two lights).
- **Priority, written into the states table:** low battery (fast flash) overrides tempo; tempo blink (only in SYNC with no MIDI clock, i.e. TAP tempo) overrides charging; charging pulse overrides steady.

### R4. Words on the instrument: the engraved sentence goes.
- "keep the keyboard | at its home octave" comes off the module's front face and off CLOTH's stitching. The family rule is one plain word per control, and a sentence on the face is an instruction, not a label. It's also likely an owner objection (it was already listed as one).
- It moves to the 1:1 card in the pocket and to the site. The brass target and the rail stay.
- **The wordmark leaves the grille** (in the sheet, "floss" sits on top of the holes). Put it on the **crown's rear face** between the two port facets, where it faces the room, like a nameboard turned outward. Nothing else goes on the deck.

### R5. Speaker: drawn sealed; the owner decides.
Sealed TEBM28C10-4B, with no passive radiator at this size. Eng's case is published-data and modelled. It reverses the owner's "passive radiator would be cool", so it goes to him as a trade-off (sealed / ported, with the trade-off spelled out), not decided quietly. Ported is only offered if eng shows the folded port fits the hull's crown.

### R6. Kits, "fewer notes". No kills this round; FALLBOARD is on notice.
- **All kits:**
  1. **The lamp is cut** (FALLBOARD's strip and SPINE's clip-on). It's a second electrical system serving an invented job. One line in the owner notes: "a lamp was considered and dropped".
  2. **Every area outside the keyboard and module has one job, or it's removed.** A pocket holding a "spare cable, strap and card" is filler: that's round 1's leftover pattern again.
  3. **One cloth for the bed and the pocket floors** (the near-black coated bookcloth). Pockets show by their walls, not by a second shade. That settles visual's open call (one shade apart).
  4. Kit weights in the files follow eng's levers by default (bookcloth over board instead of ply wherever stiffness allows). Lighter is better, and each file says what it gave up for it.
  5. **The kit's outline:** state plainly what sets each dimension (the keyboard envelope, the module, a wall). Where it costs nothing, relate it to the module's 35 mm unit; where it can't, say so. Don't retrofit a ratio.
- **FALLBOARD (lead, on notice):**
  - 412 × 288 "only just" fits a 300-wide compartment, by visual's own account. PRINCIPLES §1 says "comfortably", so as drawn it fails a principle.
  - **Fix: delete the 35 mm gutter.** The two pockets beside the narrower module take the coil and the adapter (left) and the charger (right): one job each, and the narrower module's spare width becomes the reason the gutter can go. Keep only the ≤ 12–15 mm channel the live run needs along the module's front face. Target ≈ 412 × 255–265 × 43. Show it in the same pack outline.
  - Also: the lid as bookcloth over board; the heaviest kit has to show it got lighter.
- **SPINE (rival):**
  - "One trial on the first build" is a test by Adam (PRINCIPLES §7: he measures nothing; anything needing a test is designed around).
  - **Make the stop-at-flat geometric:** the two trays' walls meet in compression at 180°, so a keypress loads wall on wall over the thighs and the cloth joint only hinges. No trial, no thicker-board fallback.
  - The module tray is wider than the module (130 mm) because the solander needs one outline. That's acceptable only if the side areas carry the coil, adapter and charger, one job each, which lets the 30 mm cable strip go too.
- **CLOTH (third):**
  - **Not green.** The family palette is walnut, cream and brass (shared universe, §4). Use **the rigid kits' near-black coated cloth**, with cream thread and brass weights. Then the outline is literally the family bed, made soft. Dark coated cloth hides park dirt as well as green does.
  - Add the **pose on the ground** (sitting on grass, the cloth as the mat). That's the park job (owner 2026-11-13: "take this to the park"), and it's where CLOTH beats the rigid kits. Keep the honest "two objects on a lap".
  - The stitched outline isn't FALLBOARD's 412 × 288 any more once R6 changes FALLBOARD: take whatever FALLBOARD ends at, so the family footprint is one number.

## Where each concept stands (not formal scores; I score at READY)
- **Module:** the strongest work in the folder. With R1's conditions met, plus R2 and R4, it could be defended as is. Its weakness is the ratio's dependence on an unconfirmed stack.
- **FALLBOARD:** the idea is strong (one plane; the lid as stand and shade), but it's the heaviest, it only just fits a pack, and it has filler pockets. If the gutter fix doesn't bring it in comfortably, it drops below SPINE.
- **SPINE:** the solander answer is real (the addendum's "mismatched covers" problem is solved) and it's the best in the bag. It needs the geometric stop and an honest side area.
- **CLOTH:** the lightest; it carries everything; on the ground it's the park kit. It's off-palette and weak on a lap.

## Likely owner objections (for every concept, as of now)
1. "Comfortably in a backpack?" for FALLBOARD (288 in 300).
2. Weight: every kit is 1.2–2.3 kg with a keyboard, and the module (0.67–0.93) dominates. The printed shell is the lever (eng).
3. "Passive radiator would be cool" vs eng's sealed pick (R5).
4. 35 mm (or 40) vs the 23–25 he saw earlier, as a trade-off (eng's trade-off 2).
5. The engraved instruction (fixed by R4).
6. Craft load: bookbinding (SPINE), sewing (CLOTH), ply and hinges (FALLBOARD).
7. A ratio story that sounds like decoration. The answer is that the parts came first; keep the line to one sentence: "the parts set 280 × 105 × 35; it happens to fall on one 35 mm unit, 8 : 3 : 1, a fourth for each half".

## Owner questions, held for the concept send
- Sealed vs ported speaker (and the passive radiator reversal).
- The 35 mm module height (eng's trade-off 2).
- Split-scoped HOLD (proposal).
- Which carry: board / box / cloth.
- Slim keyboards only, or chunky minis too (only CLOTH carries those).
- Craft: is a weekend of bookbinding or sewing welcome?

## Steer to the designers (round 2, second pair of turns)
**Systems first:**
1. Rewrite `module/how-it-works.md` to R1: 280 / 35 / hull / facets / crown; delete the paper ratio; x −8.5; inserts at 60 / 220.
2. Fix jobs.md job 30 and job 6 (R1, R4).
3. States table: R3's light priority; the flush-fret making step (R2).
4. FALLBOARD: delete the gutter, give each pocket one job, new depth, cable path (R6).
5. SPINE: the geometric stop at flat, the side areas taking the coil, adapter and charger, the cable strip removed if it can go (R6).
6. CLOTH: the ground pose as a flow; the outline equal to FALLBOARD's new footprint.
7. Eng questions, together in one list: deck-26 stack with cells beside the crown; knob part and height; driver position for ≥ 5 mm finger room; grille ≥ 620; ported fit in the crown; the hull module's weight and the shell lever.

**Then visual:**
1. Module sheet: flush frets, wordmark on the crown's rear face, no engraved line, finger room behind the crown, the grille at ≥ 620, the port facets drawn in plan.
2. FALLBOARD and SPINE sheets redrawn to R6. Each closed kit in the same pack outline with its clearance in mm.
3. CLOTH in the family's near-black, plus the pose on the ground.
4. No lamp anywhere. Images only where they have to be (PRINCIPLES §10): update the existing sheets, don't add new ones.

## What keeps blocking a 9 (the pattern, carried from round 1 and still live)
**Leftover space turning into features.** The kits wrap a 280 module in a 412 frame, and the difference becomes pockets, gutters, strips and a lamp. It keeps happening because each kit starts from the keyboard's envelope and then fills what's left. The module was derived from its parts, but the carries weren't. "Use fewer notes" is the fix: start each carry from the two objects and add only what has a job.

## Did the work change since the last score?
There was no scored round under REV 2; this is the first steer of concept round 2 for me. The module changed materially (297 → 280, hull, crown), and the systems files haven't caught up.

## Next
Systems turn, then visual turn. Then I rule again or call READY and score the module plus all surviving kits in one pass. If FALLBOARD still doesn't fit a pack comfortably after the gutter fix, it's killed or demoted below SPINE at that point.

---

# Concept round 2, steer 2 (2026-11-22, after systems rev 2 and visual turn 2)
## New owner words folded in (verbatim, from the coordinator)
- "Let’s make it an overarching principle that for now the case will be entirely 3d printed" (now in PRINCIPLES.md).
- "Cloth wrapping is fine as long as the core is printed".
- "The goal is analog-first, but that doesn’t mean digital won’t be used or should be completely avoided". The analog sentence stands as written.
- "Speaker let’s figure out what will sound best idc method". Eng is on it in `eng/module-r3.md`, **not landed**. That reopens the crown and possibly the depth.
- "The carry should fit a portable MIDI controller but the case does not need to surround it just have an attachment point. I’m just saying don’t assume not making a rule". Not a rule; it removes the enclosing assumption.
- "25 keys idk about voices" / "25 is good for the string machine". I read it as 25 voices being fine. **The coordinator should confirm the reading**; systems keeps 25.

## Judged from
- `module/module-1to1-A2.png`, `yoke/yoke-A-carry-and-play.png`, `fallboard/fallboard-A-in-use.png`, `spine/spine-A-in-use.png`.
- Words: `yoke/how-it-looks-and-feels.md`, systems' `module/how-it-works.md` §2 (knob finding), the top of `notes/visual.md` (its questions only, as the coordinator asked).
- Not opened this turn: the B sheets of FALLBOARD and SPINE, and both CLOTH sheets. I took those from the words.

## Did the work change since steer 1?
Yes, and it took the steer:
- the gutter is gone (FALLBOARD 412 × 265 × 42, 35 mm clear in a 300 pack);
- the lamp is gone, and so is the engraved line;
- the wordmark is on the crown's rear face;
- flush dividers;
- grille 737 mm²;
- 5 mm finger room;
- SPINE's stop is geometric (the tray face meets the bead at 180°; the pin only hinges);
- one pocket job each.

Systems found the honest consequence of R1 condition 2: 35 holds only with a Ø 10 × 8 knob.

## Rulings
### S1. YOKE becomes a concept, and it absorbs CLOTH.
- It's the most direct answer to the owner's newest words: an attachment point, not a surround. It's also the best fit to PRINCIPLES §1 (≈ 0.1 kg of carry), §3 (one family standard: it hangs on S4, so any module of any size gets it) and §7 (4 small prints).
- Its carry pose is nearly its play pose, and the keyboard never flips.
- **CLOTH as a standalone kit is killed.** Its two real gifts become YOKE's optional parts:
  - **the wrap:** the near-black, coated, quilted square over the printed core (the owner's "cloth wrapping is fine as long as the core is printed");
  - **the mat on grass.**

  That fixes YOKE's exposure and CLOTH's two objects on a lap, together. CLOTH alone couldn't get to 9 (two objects on a lap, soft protection), and the overlap with a wrapped YOKE was total.
- **Conditions for YOKE's concept turn:**
  1. **Panel exposure without a case:** the rim alone, or one printed cap that clips over the rim. If there's a cap, it has to do a second job in play (e.g. a riser under the module's rear that tilts the panel toward you). If it can't, the wrap is the protection and there's no cap.
  2. **The cup grip has to hold whatever the end-cap shape** (end shapes are unpublished: design around it). Clamp between the cup's floor and its lip over 11–16 mm of thickness with foam take-up, and lock the cup on its slot. Nothing may rely on a particular keyboard's end.
  3. **Eng:** arm stiffness at a 165 mm reach under a keypress on a lap; thumbscrew hold at the play detent; no rattle in carry. Published PETG properties only.
  4. **The charger rides loose:** accepted and stated. It's any USB-C charger, the one already in the bag. The adapter clips to an arm.
  5. Chunky minis: say whether a taller cup takes them, or state that they're out.

### S2. Knob: both options go to the owner as a trade-off. My recommendation is A.
- **A:** Ø 10 × 8 aluminium (CATHEDRAL's low knob, already a family part). It keeps 280 × 105 × 35 and the 35 unit. **B:** Ø 14.5 × 13.5 (the family 18T); the module becomes 280 × 112 × 42 and the kits grow 7 mm.
- **Why A:** the parts-first derivation survives intact. B's restated 14-unit 20 : 8 : 3 is a ratio found after the fact, which is exactly the retrofitting R1 warned against. A is also smaller and lighter, it's already a family part, and floss's knobs are set and tended, not ridden.
- **What A costs, said plainly:** a smaller knob under the hand.
- **The 22 mm pitch stays with A** (it's a rule for the hand, not the knob). The width doesn't reopen.
- Show it to the owner at 1:1 in words plus the existing A2 sheet. No new images.

### S3. Colour and material: keep the system, change the house colour.
- **Kept:** colour only from the spool, never paint; two spools plus a little TPU; a cream deck for the stage; cream marks (target, ticks, crown words, wordmark); one coral (DEPTH); both lights amber; carries carry no name; the one-spool debossed version as a fallback for Adam's own printer, not the baseline.
- **Changed: the house is warm walnut-brown PETG, not near-black.** Reasons:
  1. "Warmth" is the owner's own word for what draws him, and near-black matte is the default colour of every synth and controller. It doesn't look like itself (§5).
  2. Shared universe (§4): the family language so far is walnut and cream, and the earlier module was already walnut-brown PETG. Black would be a family-wide language change nobody asked for.
  3. All-black kits read as black boxes on a bench (the in-use sheets prove it).
  4. Black PETG in full sun runs hottest to the touch. A park is the use case. It's a small margin over dark brown, so it's a tiebreaker, not the reason.
- **Drop "stage blacks and spike marks" as the story.** It came from a random draw and it describes theatre, not floss. Keep its structure (house dark, stage lit, marks cream) under floss's own idea. The owner sees black as the alternative, in one line.
- **Dividers:** pressed-in black TPU 95A strip, flush. Accepted; the printed-groove fallback too. With a brown house the TPU stays black or matches the house; visual's call, and one line why.

### S4. The module's face: two fixes (both from the A2 sheet)
1. **The empty cream shoulders.** With A's rows at y 14 / 31, the deck either side of the crown (from about y 40 back to the arc) is a large empty cream field. It's the leftover pattern, now on the module itself. **The cream stage ends a few mm behind the rear row; behind that, the house colour rises as the roof to the rim** (the crown sits in the roof). The lit surface is only where the hands work, which is the stage idea done properly, and the face loses its gap.
2. **The rear outline has gone polygonal** (straight chamfers, which read as a gable). Printing makes curves free. **Go back to one fair arc with exactly two flat port facets,** or say why the chamfers belong. Don't let it drift there unstated.

### S5. Visual's other questions
- **FALLBOARD's lid: the cross seam (4 panels), accepted** over six panels: fewer parts and joints, and each quarter fits a 256 bed (206 × 133). Seams are left as honest lines.
- **CLOTH liner-up:** it carries over to YOKE's wrap/mat (the coated face to the ground). Accepted.
- **SPINE lane/bay overlap (62 × 30 counted twice):** systems fixes the count.
- **Rows and crown foot:** draw for A as the baseline and keep B as a column in the tables until the owner picks.

## Kills
- **CLOTH** (as a standalone; merged into YOKE, S1).
- Concepts going on: **FALLBOARD** (board and lid: surround and stand), **SPINE** (closed box: full protection, smallest rigid), **YOKE** (attachment point, optional wrap). They differ in kind: open frame, closed box, no case.

## Likely owner objections now
1. Walnut-brown vs black: he hasn't seen the brown printed, so show it in words, with the reason.
2. A Ø 10 knob feels small.
3. The speaker is still open (r3); the crown or depth may move.
4. FALLBOARD is the heaviest carry (0.47–0.60) and the largest box (4.6 L) now that the owner has said a surround isn't needed.
5. YOKE's exposure, and its lap rigidity resting on two thumbscrews.
6. SPINE: 6 printed halves plus rods; "bridged, it folds: don't" is a use rule, not a design.

## What keeps blocking a 9
The same pattern, now visible in the module's own face: **space the parts don't use becomes a surface that has to be dressed** (cream shoulders; FALLBOARD's bed behind a shallow keyboard). The carries are better: each pocket now has one job. YOKE is the first answer with no leftover at all, because it starts from the two objects. Secondary pattern: **a turn's random draw becomes the product's story** ("stage blacks"). Draws are tools; the story has to come from floss.

## Steer to the designers (round 2, third pair of turns)
**Systems first:**
1. Write `yoke/how-it-works.md`: the arms, slot, cups, detents, carry and play states, cable, adapter clip, the wrap and mat as options, the chunky-mini answer, coverage of jobs 3, 20, 23, 24, 27, 28, and making steps (4 prints, 2 pins, the module's thumbscrews; the wrap's sewing as an option). Answer S1's conditions 1–5.
2. Retire `cloth/` (mark it superseded, pointing to YOKE).
3. Module: A as the baseline (rows y 14 / 31, crown foot 41); B kept as a column. Fold `eng/module-r3.md`'s speaker in **when it lands**, and say what moves (crown, depth, height).
4. Fix the SPINE area count.
5. jobs.md: CLOTH's job lines move to YOKE; chunky minis per S1.5.

**Then visual:**
1. Module A2 sheet: walnut-brown house, cream stage ending behind the rear row with the roof rising (S4.1), fair arc plus two facets (S4.2). Keep B beside it at 1:1.
2. YOKE: one sheet each for A (carry and play, which exists, redrawn to systems' mechanism) and B (wrapped, on the grass as the mat, in a pack). No more.
3. FALLBOARD and SPINE: recolour only (update the sheets, no new ones).
4. Every image updated in place (PRINCIPLES §10).

## Next
I call READY once both turns are in **and** `module-r3.md` has landed and been folded in. Then I score the module, FALLBOARD, SPINE and YOKE in one pass. The knob goes to the owner as a trade-off with the concepts, not before.

---

# Concept round 2: READY and scores (2026-11-22, final for the concept phase)
**Owner, verbatim (via the coordinator):** "I will look at the clamp version but the keyboard does not need to be permanently attached would just be nice for when on the go. I think weee going really hard on design before I’ve even been able to appprove a concept".
So: no more refinement rounds. Scored on the idea (brief: concepts aren't final UI). **The keyboard attachment is a nice-to-have for on the go, never permanent:** the module plays with the keyboard simply set in front of it.

**Judged from:**
- `module/module-1to1-A2.png` (rev 3: walnut, roof, speaker E, A beside B);
- `yoke/yoke-A-carry-and-play.png` and `yoke/yoke-B-wrap-grass-pack.png`;
- `fallboard/fallboard-A-in-use.png` and `spine/spine-A-in-use.png` (the earlier, near-black versions; the recolour changes nothing about the idea);
- the top sections of systems' and visual's notes, for their questions.

## Quick rulings asked for
- **Gold knobs: accepted.** They're the family's brass, done honestly with a stocked part (black is out of stock until January 2027). They read warm with walnut and cream. Black stays the alternative.
- **YOKE's 37 mm play height, cap as the rear foot, cups at the rear corners, arms clamped at any angle: accepted as the idea.** Since the attachment is now only for on the go, play never depends on the clamp holding. For the build, prefer a positive lock (printed teeth on the pivot disc) over plain friction on printed plastic.
- **S4 at 160 mm: kept** as the family standard; the module's insides give way. It's an agent proposal, so it's listed for the owner as a family interface, not a principle.
- **SPINE's 30 mm lane: accepted, described honestly.** It's the difference that matching the two trays' outlines leaves, and it holds the cable's bend; no job invented for it.
- **Kit-total text on the B sheets is still pre-E:** fix it in the handoff, not in another round.

## READY: module, YOKE. (FALLBOARD and SPINE scored, not passed.)

## Scores (concept phase: the idea)
- **Module: 9.** Every size comes from a part (panel 280, speaker 105, driver height 35) and the ratio only tunes them: 8 : 3 : 1 on a 35 mm unit, and each half is 4 : 3 with the split line between them. The hull gives depth only where the speaker is. The cream stage is only where hands work, under a walnut roof that's the speaker box's lid. The panel is mirrored about the axis in signal order (touch → voice → shimmer → echo → out), with one coral control on the axis. It's warm and looks like itself. Its open items are owner choices and eng detail, not flaws in the idea: knob A / B, detent feel, and 105 vs 115 deep (if 115, the ratio is restated, never faked).
- **YOKE: 9.** It's the owner's own idea made physical: an attachment point, not a case. The module is the carry, two printed arms hang on its own inserts, and any family module of any size gets it free. It's the lightest carry (0.14–0.20 kg) and four small prints. The wrap is optional: protection in the bag and the mat on the grass. With the attachment now only for on the go, its weakest point (does the clamp hold while playing?) stops mattering, because you can just set the keyboard down in front.
- **SPINE: 7.** A sound, well-solved closed box (geometric stop at flat, 3.6 L). But it's a case, and the owner has said a surround isn't needed. It's heavier (carry 0.42–0.52) and six printed halves plus rods, and "don't hold it bridged" is a use rule. Not passed; it's the fallback if the owner wants full protection.
- **FALLBOARD: 6.** The lid as stand and shade is lovely. But one plane plus a lid is inherently the biggest (4.6 L) and heaviest (kit 1.51–2.10 kg) answer, the surround it's built on is no longer asked for, and it can't get to 9 without ceasing to be itself. Retired.

## The owner's choices
1. **Approve the module + YOKE** (arms as an optional on-the-go attachment, never permanent; the wrap optional). SPINE is the fallback if you want a closed box.
2. **Knob:** A, Ø 10 (280 × 105 × 35, recommended) or B, Ø 14.5 (280 × 112 × 42).
3. **Stepped controls (octave, pressure, shimmer):** firmware-stepped pots with no click (fits 35) or real rotary switches (about +5 mm of height).
4. **House:** walnut-brown with gold knobs (recommended) or near-black.

## What blocked a 9 across rounds, for the record
Leftover space becoming dressed surface (round 1 bodies, then 412 frames round a 280 module, then the cream shoulders). It was fixed once each carry started from the two objects and the face started from the hands (YOKE; the roof). Late on, the pattern was conditional numbers running ahead of eng. And per the owner, we refined before he'd approved a concept: next time, send concepts at the idea stage sooner.

## Next
Owner picks. Then the handoff for the approved concept (with E kit totals, the positive arm lock, and the depth settled by eng's detailed box).

---

# CATHEDRAL-cues form round: jam turn 3 (2026-11-22, after 18:00)
**Context:** the owner turned down my two 9s (module, YOKE) at 15:15: "I hate the shape of these. Let’s take the big energy as the guide" / "Cathedral but dimensions can change." 17:58: case fully printed (metal included), bookcloth spine "feels weird", all controls in one plane, sits at an angle (by shape is a possibility), his ideas are possibilities. Concepts go to him at idea level.

## What I learned about a 9
- I scored ideas I could defend; he judges the shape first. Both rejects had **a roof on the plan** (arch + crown house) or **parts sticking out** (YOKE). What he liked in CATHEDRAL: **one calm block, soft architectural corners, one framed field**.
- New bar: from every side it reads as one framed object; no roofs, no appendages, no second house for the speaker; a silhouette he'd want. Be harder on cleverness than on calm.

## Draws (SystemRandom)
"Do nothing for as long as possible"; "Consider transitions"; hymn board; sundial gnomon; twist "the player's hand is the stand". Used for GNOMON, the angle-from-the-device rule, the pack→play move count, the lip stability rule, CASKET's ledge.

## Rulings this turn
- **Keep:** DROP (push: pipe Ø from the Ø 55 driver frame, extra volume gets a job or goes, angle derived, end face drawn big); **GNOMON** (new, mine: CATHEDRAL's lid as a constant slab whose rim continues down into wedge cheeks at the ends, open underneath); **CASKET** with TRIPTYCH as a one-line hinged variant.
- **Cut:** DROP's pose 2; **ROSE** (ignores "Cathedral", repeats the arched-plan risk, no end carry, family scaling unsolved, costs his attention); TRIPTYCH as a separate concept. Confirmed dead: BAIL, SLED, RETABLE, plain WEDGE.
- **NAVE:** a making method inside concepts, not a concept.
- **Shared problem flagged:** a ≈ 280 module can't end-hold a 325–388 keyboard without reaching past its ends (YOKE again). Options: strap (owner Q), long-edge hold under the base (changes job 3: owner Q), CASKET lid sized to the keyboard only if the extra has a job, or keyboard loose in the bag (must always work).
- **Pass-2 rules:** angle derived from the device; end face first; every volume and surface one job; idea level, one sheet per concept (end face, 3/4 play, packed); flat-too stays the owner's fork.

## Likely owner objections (pre-scoring)
1. DROP: the teardrop reads as a hair dryer / doorstop / vacuum head; CATHEDRAL never had a round mass.
2. GNOMON: reads as furniture (writing slope, lectern); less surprising.
3. CASKET: the play pose looks like a box leaning on a tray; 3 moves to play; two objects.
4. All: how the keyboard comes along without arms.

## What keeps blocking a 9 (carried over and new)
- Old: leftover space becoming dressed surface. It's back in DROP's drawn pipe (≈ 5× the box E needs).
- New: shape. I passed defensible ideas whose silhouettes he didn't want. Fix: judge the end face and the 3/4 view first, as he will.
- Watch: random draws becoming numbers in the product (14°, 25°). Draws are tools; the angle comes from the parts.

## Open questions (owner)
Flat too, or angled enough? Strap = "knobs and stuff"? Is a metal part cast from a printed wax "3D printed even metal" (my view: casting; direct metal printing is the baseline)? If no strap: may the keyboard be held by its long edges rather than its ends?

## Next
Systems structural pass on DROP, GNOMON and CASKET, plus the shared carry; then visual draws one idea-level sheet per concept; then I steer and, when the three are honest, call READY and score all three in one pass.

## Pass 2 rulings (jam turn 5, 2026-11-22)
- **DROP: 2 rows, ≈ 37°, 260 × 88 × 62.** Derived, and it fills the pipe's width. It also makes DROP a different kind of object from GNOMON (steep lectern with a grip vs low slab on cheeks). The 3-row fallback (≈ 27°) is notes only. Watch: the rim must wrap plate and pipe as one line, or it fails on shape.
- **CASKET-B (≈ 11°, closes as a ≈ 50 slab with the façade). A killed:** it closes as a wedge and plays as a weaker GNOMON. The catch step and SHOE's dovetail share the underside, and systems must place them without clashing. TRIPTYCH stays one line.
- **GNOMON: sin θ = T/D accepted** as from the parts (T from the stack and driver, D from the box and board). The back stands at 2T, a visible proportion that scales to Big Energy. It replaces my face-ratio idea, which was aesthetic.
- **SHOE (S9) accepted** as the shared carry, pending the owner. Conditions: pads only on a flat, free underside (per model, UNVERIFIED); a positive detent; a family part listed for the owner, not written into PRINCIPLES; plays with the shoe on. Fallbacks: loose in the bag (drawn for every concept), then a printed TPU band.
- **Façade only on a seen surface:** CASKET-B's lid, yes; GNOMON's underside, no (decoration); DROP none (its lancets do the job).
- The three concepts now hold whatever the owner answers on flat, strap, hold, pads and casting; each answer has a strong option (table in jam turn 5 §6).
- **Next:** visual draws one idea-level sheet per concept, all at the same scale (end face big, 3/4 play, packed with SHOE plus a loose-in-bag inset; CASKET-B closed too). Then READY and score all three in one pass, owner objections first.

---

# CATHEDRAL-cues round: concepts scored (2026-11-22)
**Judged from:** `concepts/c-drop/sheet.png`, `c-gnomon/sheet.png`, `c-casket/sheet.png` (end view at 3:2, play 3/4 at 1:2, packed, loose inset; CASKET also closed and underside), each concept's two md files, `c-shoe.md`. I scored on the idea, but **the owner judges the shape first** (he turned down my last two 9s on it), so the 3/4 view, which is what he'll look at, carries the most weight.

## Rulings on the open points
1. **GNOMON's stretcher:** only with SHOE. Its jobs are the S9 dock and the cable-bay floor. **The cheeks' racking stiffness must not depend on it**: the slab ties the cheeks, and without SHOE the underside stays open.
2. **CASKET-B's lid ≈ 80 behind:** yes, it reads as a box on a tray. The end view shows it plainly, and that's the reason for the 7.
3. **CASKET-B 10° vs 11°:** whatever the groove's position under eng's centre of mass gives. State it; don't round to match an earlier turn.
4. **DROP's end view:** hair dryer / tape dispenser, not one rim. The 3/4 is a loaf. Killed.

## Scores
- **GNOMON 8** · **CASKET-B 7** · **DROP 6 (killed)**. Reasons and objections are in `scores.md`. No 9s, so nothing goes to the owner.

## GNOMON: fixes to reach 9 (one visual pass, idea level, the same sheet updated in place)
1. **Make the slab legible on the end face** without breaking it into "box on legs": one engraved hairline (the family's section-rule mark) parallel to the plate at T below it, so the end face reads as the lid plus its own thickness (2T at the back). Keep the face flush and the rings continuous.
2. **Show the hollow:** add a **rear 3/4** (or a low 3/4 from behind) where the open underside and the raised rear face with its jacks are visible. That view is what proves it isn't a solid wedge. Draw the cheeks as thick as the rim, not as a solid infill.
3. **Shrink the brass port ring** to a flush, narrow ring, or grooves only (if cast doesn't count, it's grooves only anyway). At its current size it reads as a hose fitting, and it becomes the focal point of the end face instead of the rings.
4. **Front edge:** the lip face leans back 19.5°, which makes the end silhouette an irregular pentagon. Round the lip into the plate with the same superellipse family as CATHEDRAL's corners, so the front reads as a soft edge and not as a chamfer.
5. **Packed view:** show it docked on SHOE **and** the stretcher-less loose version at the same size, so the owner sees it isn't dependent on SHOE.

## CASKET-B: the path to 9, only if the owner says "flat too"
- Contain the lid in the footprint. The only clean way found: **TRIPTYCH**, the lid hinged at the module's rear base edge and folded under, ≈ asin(15 / 107) ≈ 8° [calc], with nothing showing behind. It costs the one moving part he hoped to avoid. The other route is for the owner to accept the overhang.
- If he says angled is enough, CASKET retires and GNOMON carries the round alone.

## What keeps blocking a 9 (this round)
- **The idea lives in the end view, but the owner sees the 3/4.** DROP's logic (pipe = box + port + grip) and GNOMON's (slab on its cheeks) are both clear in section and invisible or wrong in the object. Fix: judge every concept from the 3/4 first, as he will.
- **Angle-by-adding-something leaves a leftover** (CASKET's 80 mm of lid behind): the old "leftover space" pattern, now in the play pose.
- **Round masses** (DROP, and ROSE before it) keep landing as household objects. CATHEDRAL's language is slab and frame. Stay inside it.

## Has the work changed since my last score?
These are new concepts, scored for the first time. The turned-down module and YOKE aren't comparable.

## Next
A visual pass on GNOMON (fixes 1–5), then I re-score GNOMON alone. Ask the owner "sit flat too?" now (it's already pending): yes → a TRIPTYCH pass for CASKET; no → GNOMON alone. SHOE stays the shared carry, pending the owner's answers on pads and the underside hold.

## Plan change after the owner's answer (2026-11-22)
**Owner, verbatim (via the coordinator):** "Honestly my preference order would be angled, 90, flat". The orchestrator's reading (not confirmed): angled first, upright at 90° second, flat last; flat not required.
- **CASKET-B retires**, as planned. GNOMON carries the round.
- **GNOMON gets the 90° pose by shape, with no added parts. Fix 6 (new):** cut the **rear face square to the plate** instead of vertical. The end face then becomes a true gnomon: plate and rear face are the two legs of a right angle, and the table line is the hypotenuse. Angled pose: on the runners, θ = asin(T/D). Upright pose: stood on the rear face, the plate is exactly vertical (turn it round to face you). From the side, the rear face is battered like a buttress (it leans in toward the top by θ). That's a cathedral cue with a structural reason, not costume.
  - **Costs [calc, rough]:** the angled footprint grows by about rear height × sin θ ≈ 68 × 0.33 ≈ 23 mm, unless D gives some back.
  - **The jacks must leave the rear face**, because it's a foot in the upright pose. They move to the right cheek face (the left cheek is the port mouth); the host port stays on the lip, which is on top when upright.
  - **Systems to check (UNVERIFIED):** upright stability on a ≈ 66-deep rear face. The slab is at the plate edge, so the centre of mass sits near that edge; a knob press pushes into the footprint, and a pull on the top edge is the risk. Also that the speaker, port and every port work in both poses.
- **Visual:** add the upright pose as a small fourth view on the GNOMON sheet. Don't add a separate concept.
- **Question for the owner (clarify, don't block):** is "90" for **playing** upright (knobs on a vertical face, like a radio) or for **standing it up** (a shelf, display, storage, a friend across the table)? It changes how much the upright pose has to be tuned for hands. Note: I killed RETABLE for knobs on a steep face; his ranking overrides my taste here.
- **Re-score:** GNOMON alone, from the revised sheet, owner objections first.
- **Owner follow-up, verbatim:** "Multiple angles is fine". Folded in: it backs GNOMON having two poses by shape (angled on the runners, 90° on the square rear face). The plan stays the same: no added parts, and no adjustable mechanism is introduced on the strength of this. If the owner means a range of angles rather than several fixed poses, that's for him to say; ask it alongside the "90 for playing or for standing?" question.

# GNOMON rev 2 re-score (2026-11-22): 9
- **Judged from** the rev 2 sheet (seven views) and the rev 2 md files. **The work really changed:** fixes 1–6 all landed, so this isn't a raise for unchanged work.
- **Why 9 now:** the idea is legible (the end view's 2T hairline, the open underside from behind, the upright pose), and it meets every owner word, including his new ranking (angled, 90) and "multiple angles is fine", by shape alone. The upright view is CATHEDRAL's standing lid.
- **Hard on my own idea:** GNOMON is my proposal and the least surprising form. I checked it against the shape tests that sank the module and YOKE: no roof on the plan, nothing hanging off it, no separate speaker housing. It passes all three. The remaining risk, "it's a wedge", is the honest cost of getting the angle from shape, and the brief says not to mark down the best conventional answer.
- **tan θ = T/D accepted** over sin (2T stays on a visible, standing face).
- **Objections and handoff conditions:** see `scores.md`. The key handoff item: host port low near the rear-bottom corner of a cheek, so the keyboard cable can't tip the upright pose.
- **What blocked a 9 this round, for the record:** concepts whose idea showed in section but not in the object (DROP, GNOMON rev 1); angle-by-adding leaving leftovers (CASKET's lid behind); round masses reading as household objects. All three were fixed by staying inside CATHEDRAL's slab-and-frame language and judging from the views the owner will look at.
- **Next:** GNOMON goes to the owner at idea level, with one line each on DROP and CASKET-B and the open questions (90 for playing or standing; poses or a range; SHOE pads / underside hold; cast metal). If he turns it down, his reason is the next calibration of a 9, especially on shape.

# GNOMON rev 3 re-score (2026-11-22): 9, held
- **Owner, verbatim:** "Reverse the angle on the side behind the speakers so there’s still a subtle angle when upright". This was a direction, not a rejection: the first time a concept came back from him with its shape intact. **Calibration:** he looks at every pose as an image. A dead-vertical 90° read as less alive than CATHEDRAL's raised lid, which leaned back.
- **Ruled:** "reverse" is read by its purpose ("subtle angle when upright"), not as a literal mirror (≈ 37°), and the owner note flags that reading in one line. tan φ = T/2D is accepted (≈ 9.5°). The ≈ 1.9T rear face is accepted; the 2T claim moves to the hairline, and stale "2T" lines get cleaned in the handoff.
- **Changed since the last score:** yes (rear corner ≈ 80.5°, upright lean, footprint 99, pull-to-tip +49 %). It's held at 9 rather than raised, because 9 is the ceiling for "I'd defend it as is".
- **Objections:** the reading of "reverse"; upright pull ≈ 1.9 N; bulk; the hairline as a seam.
- **Handoff conditions:** as rev 2. (a) The host port goes low on a cheek near the rear-bottom corner; rev 3 hasn't moved it. Make depth 110 vs footprint 99 consistent.
- **Next:** back to the owner. If approved: the handoff, and I check `handoff.md` against his words, including the "reverse" reading and the host-port move.

# GNOMON rev 4 re-score (2026-11-22): 9, held
- **Owner, verbatim:** "I don’t like the angle on the back when laying flat. Make the base and the back 90 degrees when sitting flat". He's the second time fine-tuning one face of the end view, which confirms he's judging the silhouette pose by pose, as pictures. **Calibration:** he prefers right angles against the table (base ⟂ back) to derived lean angles on the back. Calm, architectural geometry wins over clever ratios.
- **Changed:** the back is vertical when playing; one angle (≈ 18.4°) serves both poses; the corner is ≈ 71.6°; the footprint is 88.5; upright pull 2.52 N. tan φ = T/2D is retired. My earlier "not subtle" objection to a vertical back is superseded by his call.
- **Objections:** (1) his two notes trade: upright now leans ≈ 18.4°, not the "subtle" ≈ 9.5°; tell him plainly; (2) upright stability under firm top-row presses; (3) more of a plain wedge (his direction).
- **Handoff condition (a) is still open:** the host port is on the top edge when upright. Move it low near the rear-bottom corner of a cheek.
- **Next:** back to the owner. If approved: the handoff; I check it against his 18:39–19:02 words, including the angle trade and the host-port move.

# GNOMON rev 5 re-score (2026-11-22): 9, held
- **Owner, verbatim:** "I miss the subtle rounded shape of cathedral"; and the idea "And w what if the speakers were on each side left and right so up or down didn’t matter".
- **Calibration:** that's the third fine-tune of the same concept. He keeps the concept and polishes its silhouette toward CATHEDRAL. Softness is part of the family face, and I let it slip when rev 4 squared the back. **Every rev must keep CATHEDRAL's n 5 corners and eased edges by default.**
- **The rounding answers his note** in plan and in the 3/4 views. The gap is the tight r 4 at the top-back (the tipping edge) and the base-to-back (his 90°), held for stability and squareness; the owner sees the trade (r 8 → pull ≈ 1.6 N).
- **Side speakers:** I concur with systems' "not recommended": the player would be off-axis in both poses, it's quieter and duller, and it loses the port, jacks and end grain. The plate drivers already face him in both poses. Give him the gains and ask what problem he sees.
- **Condition (a) revised:** the host port stays on the front face (a cheek receptacle is UNVERIFIED; a cable's weight is ≪ the pull-to-tip).
- **Watch:** panel creep (power / TUNE / SPLIT on the plate). Fine for now; the panel layout is a handoff job, not a concept feature.
- **Changed:** yes. **Objections:** the softness at the back corners, panel creep, side speakers, upright pull ≈ 2.1 N.
- **Next:** back to the owner. If approved: the handoff, checked against his 18:39–19:14 words (pose order, "reverse", base ⟂ back, the rounding, and the side-speaker answer).

# New direction: flat or slightly angled (2026-11-22, after 19:14). Round count restarts
- **Owner, verbatim:** "…So one arrangement that can either be flat or slightly angled is the best multiple arrangements it can be". The upright pose is dropped; "angled, 90, flat" is superseded. End-firing speakers are pending with the coordinator.
- **GNOMON's identity (two poses by shape) is gone.** What survives is the slab: framed plate, n 5 corners, eased edges, end grain and port mouth, jacks on the right end.
- **Shape alone can't give flat + a slight angle** (systems turn 1). One moving part or a second piece is allowed; it must earn its place, and nothing may hang off the body.
- **Draws:** paper bail; skateboard truck; "Mute and continue". So: keep the slab, redesign only the underside; a full-width foot; the pivot hidden under the deck.
- **Directions:** SILL (a flush full-width flip-down bar), TRIPTYCH revived (the cover hinged at the rear base edge, folding under within the footprint: flat or triangle), TURNING CHEEKS (the end caps as linked cams; kill fast if not simple).
- **My early lean, to be hard on:** TRIPTYCH, because its moving part does two jobs and closed it's CATHEDRAL closed. Risk: its thickness when flat, and the catch. SILL is the safest. TURNING CHEEKS is the wild card.
- **Owner objections to expect:** a hinge on a printed part rattling or failing; visible mechanism; a thicker kit with a cover; the flat pose being the default he actually uses.
- **Next:** systems first (feasibility, angles, stability, kills); then visual (one sheet per survivor); then I steer and score.

# Round 2 steer 2 (2026-11-22)
- **Kills accepted:** TRIPTYCH (needs two hinges and three states) and TURNING CHEEKS (an eccentric reads as a knob; a rod through E's box). **SILL forward.**
- **Ruled:** h = T/2 (θ ≈ 9.2° at D 115), because "slightly" must read in a picture and he accepted ≈ 9.5° as subtle. **D 115** (E's margin back). **CHOCK** as a one-line variant and inset on the SILL sheet, not a concept.
- **Expected objections:** "a slab with keyboard feet"; a printed hinge; losing the cheeks.
- **Next:** visual draws the SILL sheet; then I score SILL (CHOCK as its variant), owner objections first.

# Round 2: SILL scored 9 (2026-11-22)
- **Why 9:** flat, it's CATHEDRAL's lid (soft slab, framed plate, end grain); it packs as the slab itself (280 × 115 × 35); one move gives ≈ 9.2° from h = T/2; the panel is identical in both states; nothing outside the outline; the load goes into the stop, not the hinge; every job supported. It's the calm, square, soft object his four GNOMON send-backs pointed toward.
- **Hard on it:** it's conventional and the least distinctive concept today. Allowed, because it's the best answer to his own words. The real shape risk is the tilted end view's thin bar reading as a spindly leg; the option is printed bronze (the CATHEDRAL stay) if metal is acceptable.
- **Objections:** the thin leg in side view; "a box with a flip foot"; the printed hinge / pin; the utility cluster on the plate.
- **Handoff conditions:** E's net volume at D 115 (eng); a detent trial or magnets; owner answers (pin, SHOE, cast metal, end speakers); utilities layout.
- **What blocked 9s today, for the record:** shape seen pose by pose (module, YOKE, DROP); ideas that live in section, not in the object (GNOMON rev 1); leftovers from adding parts (CASKET); and, after approval-level fine-tuning, drift from CATHEDRAL's softness and square faces. **Lesson: start every concept from CATHEDRAL's calm soft slab and add only what a job needs.**
- **Next:** the owner. If approved: the handoff; I check it against his 17:58–19:23 words.

# Round 2 steer 3: three concepts to compare (2026-11-22)
- **Owner, verbatim:** "I can only see one version how am I supposed to judge". **Calibration:** a 9 alone isn't judgeable. He needs 2–4 concepts that differ in principle, side by side at one scale. Don't send single concepts again.
- **Draws:** drawer; toolbox handle; "The inconsistency principle". These give three different principles: SILL (a moving part of the module), PLINTH (a second piece; nothing moves; a cable drawer; stacks module / plinth / keyboard via S9), HANDLE (a flush bail, stand plus carry handle; kill if it reads as an appendage).
- **Deliverable:** one same-scale comparison sheet (flat end, tilted end, tilted 3/4, packed, one trade line each) plus each concept's own sheet.
- **Expected objections:** PLINTH, two pieces and a wedge-shaped kit; HANDLE, YOKE's appendage risk when up and a printed pivot; SILL, the thin leg in side view.
- **Next:** systems structures PLINTH and HANDLE (kill if not simple); visual draws them and the comparison sheet; then I score all three in one pass, SILL re-judged beside them (no raise for unchanged work).
- **Amendment, owner verbatim:** "I do wish it was more distinctive refardless". SILL is the calm baseline, not the answer. The new concepts must be clearly more distinctive in silhouette and idea, through one strong move of form, not detail (calm and soft still hold). Test: recognisable from the end silhouette at thumbnail size.
- **Line-up:** SILL (baseline; optional bronze bar line); **CRADLE (lead: the slab tilts on front trunnions between flat-standing cheeks; GNOMON's lineage)**; PLINTH (the slab floating on an inset wedge base with a shadow gap); HANDLE optional (only as a visible bronze line, else kill).
- **Calibration:** "conventional and the best answer" isn't enough for him. Distinctiveness is part of a 9. Re-judge SILL in the comparison; its 9 was on fit, and it's now marked down on distinctiveness by his word.

# Round 2 steer 4: EASEL (2026-11-22, after 20:46)
- **Owner, verbatim:** "I do like one that sits up at an angle with a narrow footprint … like cathedral at least but without the keyboard"; and "I do worry about the speakers being so close for steeeo sepsrstion".
- **Calibration:** he wants the steep CATHEDRAL lid pose for small tables. My RETABLE kill is overridden by his call.
- **EASEL:** the plate at ≈ 60° (CATHEDRAL's 120° lid), derived as footprint = half the plate depth; end faces as tall soft triangles (GNOMON's cheeks grown up); the narrowest footprint; stereo end drivers possible as an option.
- **Main risk:** tip-back under knob presses on a narrow footprint; weak on grass and lap. Systems states the honest cost.
- **The comparison is now four columns:** SILL, CRADLE, PLINTH, EASEL. HANDLE is dropped.
- **Owner decision, verbatim:** "Why would I have two mono speakers that’s stupid. Drop to one speaker". One driver in every concept, one grille on the axis; stereo on headphones/outputs. EASEL's stereo option is withdrawn. Eng re-picks the box (r3 option C ≈ 120 cm³ as the starting point; UNVERIFIED). The smaller box may shrink the forms.
- Quick rulings: EASEL B (1:1.618, rounded top); slabs at D 105 with derived angles; EASEL's costs stated on the comparison trade line.

# Round 2 comparison scored (2026-11-22)
- **Scores:** EASEL 8 (fixable: driver into the foot firing through the front face, plate sized to the controls, r 17.5 corners); SILL 8 (lowered from 9 on his "more distinctive regardless"; unchanged work); PLINTH 7 (flat = SILL's block; replace); CRADLE 7 (flat looks like sofa arms or bookends, jacks on the front face, biggest; kill). **No 9s.**
- **Rulings:** slab grille at the output end with utilities mirrored left (accepted); CRADLE rings on the pivot (accepted); darker plinth (accepted); EASEL corners r 8 → r 17.5.
- **Recommendation:** send the comparison as a direction check with the scores shown (his explicit process request), or hold for the EASEL fix. The orchestrator's call; this deviates from "only 9s", on the owner's own words.
- **Pattern:** distinctive ideas add a mechanism or leave dressed space; calm ones aren't distinctive. Target: a distinctive silhouette that is the structure, with no leftover (GNOMON did it; EASEL can, with the speaker in the foot).
- **Next:** either the owner picks a direction from the comparison, or a systems + visual pass on the EASEL fix, then a re-score.

# Round 2 steer 5: LOW GNOMON as the second candidate (2026-11-22)
- **Need:** a second 9 beside EASEL, so he can compare; it should answer flat-or-slightly-angled.
- **Pick:** LOW GNOMON, rev 5's soft wedge (shape = structure; the tall back is the one-driver box), slightly angled by shape at tan θ = T/2D ≈ 9.5°. Flat is only via a flush front bar, kept only if it doesn't look propped; otherwise it's offered as slightly angled only, with zero parts.
- **Why it's most likely to reach 9:** it's the shape he refined four times and never rejected (only its upright pose went). It's distinctive at thumbnail size and differs in kind from EASEL.
- **Risk:** without the flat pose it doesn't fully answer "flat or slightly angled"; with it, the propped-wedge look. His "replace or join" answer may settle it.

## Process change (owner, verbatim): "Do you have the ability to have them draw sketches somehow instead of these complex renders every time?"
- **From now on, idea-level concepts are quick line sketches:** an end view plus one or two simple views, loose line work, few labels. Fuller drawings come only after he approves one.
- **Scoring:** I score EASEL and LOW GNOMON from sketches and never mark down for sketchiness (the brief already says don't mark down unpolished concepts). I judge the idea and the silhouette.
- **Calibration:** the renders were part of the over-design he flagged at 15:11. A sketch shows the shape faster, and shape is what he judges.

# Round 2 rulings 7 (2026-11-22)
- **EASEL:** equal 60° faces (280 × 79 × 86, TPU strips). Utilities in a slim top band with the lights, on the plate (job 31, "single plane"), which also fills the old empty field. The back face goes to the owner as one line only.
- **LOW GNOMON:** angled-only; the slab ≈ 2 mm proud of the cheeks as the lid's rim (no book language: the bookcloth spine was "weird"). Flag: if it reads as SILL tilted, it's under 9; no added detail to fake distinctiveness.
- **Next:** visual line-sketches both; then I score.

---

# Director handover 2: new seat, round 2 candidates scored (2026-11-22)
I took the seat here. Everything above is history: I use it for consistency and don't defend its scores.

## Read
- `PRINCIPLES.md`, `floss/REQUIREMENTS.md`, `BRIEF-CATHEDRAL.md`, `jobs.md` rev 6, `scores.md` (all), the notes above (CATHEDRAL round onward in full), and `design/owner.md` 15:11–23:50 verbatim.
- EASEL rev 2.3 and LOW GNOMON: all md files.
- **Images opened:** `r2-sketches.png`, `r2-easel/sketch.png`, `r2-lowgnomon/sketch.png`, `r2-compare.png`.

## Calibration I carry (from his words since 15:15)
- He judges the shape pose by pose, as pictures, from the 3/4 and the end view.
- He keeps CATHEDRAL's softness and square, calm faces.
- He needs 2–4 options side by side; "distinctive regardless".
- One speaker; sketches, not renders; ask one question at a time.
- His ideas are possibilities, never anchors.
- He has objected to off-centre middles before.

## Draw (SystemRandom)
"Change instrument roles" × canoe hulls → a possible low-slot concept: **HULL**, a rockered base with two chines (flat on one, ≈ 10° rolled onto the other), one piece, zero parts. Watch the round-mass trap. Only if he says "join".

## Scores
- **EASEL rev 2.3: 8**, held.
  - **Likely objections:** (1) the face is off centre (6 | lights | 5), and the drawn count (22 + 3) is wrong; (2) the lancets at z 4–16 are masked by a 11–16-tall keyboard pushed up to the predella (a director finding; UNVERIFIED); (3) a Toblerone read (possible); (4) the knobs exposed when packed; (5) a 5 N slide from the end toggles; (6) the scope question.
  - **Fixes:** mirrored face with the true 21; slots at z ≥ 18 with the host port beside them; recessed end controls; one caption line on packed protection.
- **LOW GNOMON: 6, replace, don't send.** It reads as SILL tilted (visual agrees), does less than SILL (no flat) and is no more distinctive. It can't reach 9 without decoration.

## What keeps blocking a 9
Distinctive vs calm. EASEL escaped through the pose. The low slot keeps converging on a slab because it's been treated as "SILL plus a trick"; it needs its own principle.

## Open questions (owner, one at a time)
1. **Next to ask:** EASEL replaces or joins flat-or-slightly-angled?
2. Later: SHOE / underside hold; cast vs printed metal; packed protection for EASEL (a cover is his possibility, not ours).

## Next
1. Visual + systems do EASEL's fix pass (one redraw; eng gives one line on slot height).
2. I re-score EASEL.
3. Orchestrator asks the owner the replace-or-join question with the fixed EASEL and SILL's column.
   - **Replace:** EASEL goes at 9.
   - **Join:** a short jam for one distinctive low concept (HULL as one possibility among others), then score.

# EASEL rev 2.4 re-score (2026-11-23): 9
- **Changed:** yes. The face is mirrored 10 | TAP | 10 with the lights on the axis (the true 21, in signal order), the slots are at z 18–32 with the socket beside them, the end controls are in a flush pocket, and there's a packing caption. 280 × 79 × 81.
- **Why 9:** his 20:46 words made physical, one piece, a symmetric all-controls face, a calm end view. The remaining objections are a stated trade (5 N slide), the scope question, a possible prism read, and an UNVERIFIED slot low-pass.
- **Caption fix before sending:** "plate-down on SHOE" conflicts with SHOE in the base and puts the rim across the keys (job 3). Reword it.
- **Handoff conditions:** the eng low-pass model and listening print, the driver basket vs the 37 predella, the pocket parts, TPU strips, the tab order, SHOE pending.
- **Next:** the orchestrator sends EASEL with SILL's column and the one question (replace or join). Join → a short jam for one distinctive low concept (HULL as one possibility); LOW GNOMON is not shown. Approved alone → the handoff, which I check against his 20:46 and 23:50 words.

# Round 3 steer (2026-11-23)
- **Owner, verbatim:**
  - 00:09 "I want options. Do one that’s a triangle too"
  - 00:20 "The end view I’d not a triangle"
- **Calibration:** EASEL joins, it doesn't replace. He wants several options of both kinds every time, plus a true three-faced triangle.
- **Set:** EASEL (9, anchor; caption fix only), SILL (anchor), TRIANGLE (new), HULL (new). One same-scale four-column sketch sheet.
- **TRIANGLE:** derived. (a) equilateral vs (b) base ⟂ back. Visual draws the one that reads more clearly as a triangle and differs more from EASEL. Costs: the lowest row rises; the speaker moves to the plate, an end or the back (systems recommends one); the host port goes low on an end.
- **HULL:** a rockered underside with two facets ≈ 9–10° apart, flat and slight by shape, zero parts. Draw "Emphasize the flaws" × ceramic glazing → the curve is shown, with a glaze line between the slab top and the hull foot. Kill it if a press rocks it or it needs a detent. Watch the round-mass trap; judge it from the 3/4.
- **Next:** systems, then visual, then I score all four in one pass.
