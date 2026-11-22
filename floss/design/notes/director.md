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
