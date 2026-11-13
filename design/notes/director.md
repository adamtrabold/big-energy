# Director notes: Little D (budget instrument), physical design

## BRANCHES, jam turn 3 (2026-11-13, new director taking over): READ THIS FIRST
- **Task:** the owner's branched creative rounds (owner.md 11:47). He wants more personality and a holistic point of view; sources: furniture principles, instruments, tools, art, emotion, "take this to the park". He loves the pegs; "organ like" on FOLD is an example only. **Echo sync DECIDED: B, a FREE / SYNC toggle near TIME** (11:58). The v1.1 locks are never edited.
- **My turn:** the bottom of `design/branches/jam.md`. Draws: `design/branches/draw-director.py` (fresh decks; used Oblique cards removed). Results:
  - director: "Be extravagant", sundial / gnomon, wonder, a bandstand;
  - per branch: BUTTERFLY "lighter than it looks" / "From nothing to more than nothing"; CHAMBER "a place for your own mark" / "Look at the order in which you do things"; GROUND "tell it from 30 m" / "Lost in useless territory"; RAIN "makes a sound when you close it" / "Courage!";
  - d20 kill test: BUTTERFLY 9, CHAMBER 11, GROUND 2, RAIN 7, DIPTYCH 15;
  - unused: coffee grinder.
- **Kills:**
  - **PIERCED, upheld:** +55 mm for one gesture, against cost and portability.
  - **GROUND, killed by me:**
    - a posture is a stand, not a point of view;
    - +25–37 mm at the back against the ≈ 36 body;
    - the horn is unverified;
    - FOLD's lid already tilts.
  - GROUND's donors: the status-light hood (now set-wide), high-contrast sun type, the felt finger pocket, and "the bottom is as designed as the top".
- **Going to concepts (4), each with a "must prove" list in the jam §3:**
  - **CHAMBER (FOLD):** the strongest branch, so held hardest.
    - The order of use is the concept: closed façade → flat console → standing façade to the listener.
    - Flush nameboard cartouche on the axis for his maker's mark.
    - **Costume watch:** line work only, serif only on the RANGE feet and the nameboard.
    - The sketch's "little d" must go (the owner hates the name).
    - Must prove: the closed bar reads as an organ case, the closed height with pegs, reversed pegs at 1:1, engraved fill vs printed relief, a standing view from behind.
  - **RAIN (ONE SHEET):** the most generative.
    - "Courage!": drop the section grooves and let the Voronoi seams be the only section marks; the field runs to every edge.
    - Optional: a power-off "drop" sound ($0, firmware).
    - Must prove: calm at arm's length and alive up close, legends on the lily pads, 0.9-pitch rings that still feel like v1.1's, peg width (+8 mm), one mustard accent only.
  - **BUTTERFLY (ONE SHEET):**
    - The butterfly must do a job, so the rail is **two bookmatched live-edge offcuts joined by the butterfly on the axis**. That makes the joint honest, uses cheaper short pieces, and mirrors the wild edge, which gives it balance.
    - Rail ≈ 20 mm of wood, "lighter than it looks".
    - The set's flat-key branch.
    - Must prove: printed cream beside real walnut reads as intended, not a kit (biggest risk; try a matte bone/stone filament); joint depth; slotted screws and the drilling jig; the cleat hanging.
  - **DIPTYCH (FOLD), my own:** a Nuremberg diptych sundial.
    - Cords at the end faces are the stay. They replace the brass stays and remove v1.1's stay-groove/jack clash.
    - The cords are set at Lynchburg's latitude, 37.4° [CALC rough: anchor ≈ 68 mm forward of the hinge, cord ≈ 154 mm, at the approved 120°].
    - TIME's two scales are its "two hour systems" (the FREE/SYNC feature becomes the hero).
    - Red and black engraved graduations on the white leaves; the walnut stays.
    - **I'm hard on it:** if it can't separate from CHAMBER at concept stage, cut DIPTYCH, not CHAMBER. Cord snag risk near the stick and TAP.
- **Set-wide rulings:**
  - FREE/SYNC placement accepted: in front of TIME, in the dead zone, fore-aft throw (toward TIME = sync), two scales, no mirror partner. Pending systems' label check.
  - **H7 stands** (no lit TAP); a hooded or light-piped status light in every branch.
  - No name on any branch.
  - The board is the constant; no branch moves a control.
- **Calibration carried from my predecessor:** a 9 = every visible choice traces to one idea, the owner rules are met, there's a lean cost default, the owner's hand has a place, and it's the most interesting version of itself.
  - For the branches I add: **a whole point of view (one sentence decides form, material, graphics, making and feel), and a picture that makes him want to take it to the park.** A nice detail isn't a point of view.
  - The owner has paused 9s (TYPE CASE, HYMNAL) to narrow the set, but he has never sent one back on quality. His pattern: he reacts to specific physical annoyances (dividers, lip, slot-as-fader, balance) and to cost and name; he rewards texture he can feel (rings, pegs, felt).
- **Likely owner objections, by branch:**
  - CHAMBER: costume, +4 mm closed, reversed keys;
  - RAIN: busy or dizzy, +8 mm width;
  - BUTTERFLY: plastic next to real wood looks cheap, "just a plank on ONE SHEET";
  - DIPTYCH: too close to CHAMBER, fussy scales, cords in the way.
- **Owner questions (in the jam §6):**
  1. CHAMBER's reversed keys OK?
  2. Pegs worth +8 mm width (ONE SHEET) / +4 mm closed (FOLD)?
  3. Park session length (battery)?
  4. Tapped tempo sent out as MIDI clock?
  5. The furniture book's exact title and author?
- **Not scored yet.** **Next:** visual leads the concept builds, with systems on the geometry in parallel. I steer after every pair of their turns, then score all four in one pass and name the owner objections first.

## Status (fix check, 2026-11-13 ~11:35): READ THIS FIRST
- Both must-fixes verified by eye: the slot is gone. A round opening now shows in the 3/4 views (A on all three, FOLD E). FOLD D's end view shows three ports (MIDI IN, MIDI OUT, USB-C), and its note is corrected. I saw no regressions in the changed sheets: labels, stand and callouts are unchanged.
- **HUSH 9, ONE SHEET 9, FOLD-105 9 hold.** The 3/4 joystick reads unmistakably now. Next: the owner picks a concept, then I check handoff.md. The nice-to-haves below are still open.

## Status (CHECK after the 120° stand + bend-joystick redraw, 2026-11-13, new director): READ THIS FIRST
- Scope: a check, not a round. Owner asked: FOLD lid less steep so the face catches more light; bend must be a joystick. Change: FOLD stand 105° -> 120° (spec rev 5.7, stays 44.4, tip 6.8 N) + bend redrawn (stem, flared cap, round ring with 2 pointers, round tag, B-sheet callout "BEND IS A JOYSTICK, NOT A FADER").
- **Scores hold: HUSH 9, ONE SHEET 9, FOLD-105 9**, conditional on must-fix 1 (drawing only; I check it, no re-score). Work changed in the stick and the stand (plus footers); I saw no other regressions by eye (pixel-diff boxes vs versions/v1 are large, so this is a visual check, not a proof).
- **Stand (sheet E): passes.** Side view measures right: lid 60° to table (=120°), stay ≈ 44 mm at ≈ 60-62°, pivot d ≈ 31 from the hinge, tip 59 behind. 3/4 visibly leans back and the panel now reads cream, not grey: the owner's "catches more light" is shown. Believable.
- **Joystick: B sheets pass** (plan = round well + cap + 2 pointers; callout clear, push/pull directions consistent). **3/4 views (A x3, FOLD E) half-fail:** stem + flared cap read as a stick, BUT the round ring contains a dark elongated slot along the bend axis. That slot is the fader cue the owner reacted to, and it contradicts B and the callout ("gate under the panel"). Front elevations (D): T-silhouette OK on FOLD/ONE SHEET; HUSH's is hidden behind pegs (acceptable for an elevation).
- **Must-fixes:**
  1. A (HUSH, ONE SHEET, FOLD) + FOLD E: replace the visible slot with a round aperture (round hole/boot, Ø ≈ ring inner), matching B. Gate stays under the panel.
  2. FOLD D: the purple note says "rev 5.6 lists no MIDI IN", but how-it-works rev 5.6 adds MIDI IN (y 70) beside MIDI OUT (y 80) + USB-C (y 90-99). Draw the 3rd jack on the base's right end and fix the note. (Pre-existing, not caused by this change, but it now contradicts the spec.)
- **Nice-to-have (not blocking):** E headline "FOLD-105 ... standing at 120°" invites confusion; add "(105 = half depth)". FOLD how-it-works line ~58 still says stay 52.4 mm (superseded by rev 5.7 header; tidy). E side view omits the lid's knobs (pre-existing). HUSH B PARA-legend flag still open (pre-existing).
- **Owner state:** all three LOCKED as v1 (versions/v1/); he leans ONE SHEET or FOLD; his creative-rounds request was withdrawn ("forget i said that"). No new round.
- **Next:** check fixes 1-2 by eye; then the owner picks -> handoff.md check against the approved concept + owner.md.
- **Lesson added:** when a control's identity is the owner's complaint, check it in every view type (plan, 3/4, elevation): renders inherit old geometry (the slot) even after the plan is redrawn.

## Status (after round 5 scoring, 2026-11-13): READ THIS FIRST
- **Round 5: HUSH 9, ONE SHEET 9, FOLD-105 9.** All three go to the owner after **S1**, a shared label-clearance pass. S1: short labels under section headings (echo: type · time; reverb: decay · type), ≥ 1.5 mm between legends and between legends and skirts, grow the depth up to ≈ 10 mm if needed (owner: "grow the panel"). I check S1 only; no re-score.
- **FOLD-113 is not offered:** it fails the gap (75.45). For more runtime, use a bigger cell in the same footprint, not deeper halves.
- **Must-fix / test before handoff:**
  - FOLD: the right stay groove clashes with the lid-wall jacks (prefer moving the I/O to the left end face). Systems also confirms the AFTERTOUCH toggle and the Daisy Seed placement.
  - HUSH: the steam-blocking corner test (now incl. edge A's r 4 front).
  - ONE SHEET: the rings coupon, now a pre-build check, not a score blocker. The fallback is per-volume bottom patterns in the 3MF.
- **Owner's latest asks (all reflected):** echo + reverb on a Daisy Seed with the full 8 FX controls; DRIFT; MIDI out; aftertouch with its own switch; key edge A/B (show both); front views; FOLD standing lid at one fixed angle (105° on flush brass stays); ONE SHEET smooth + rings only. Paraphonic mode is pending his key-tracking question (eng).
- **Lesson:** feature additions break legends before they break knob pitch. Add a legend-clearance check to every layout change. FOLD still needs the open-depth check on every change.
- **Next:** S1 → owner picks (and chooses key edge A/B) → handoff.md check against the approved concept + owner.md.

## Earlier status (after round 4 scoring, 2026-11-12): READ THIS FIRST
- **The owner paused TYPE CASE and HYMNAL** (both 9, on file). Active: HUSH, FOLD, ONE SHEET.
- **His round-4 brief:** unibody, screws from the back (ideal, flexible); HUSH organically rounded; FOLD = Proof walnut + white, rounded edges with flat top and bottom, block + pickguard; HUSH and ONE SHEET loaded from behind; keys to the front edge, knobs logically split, narrower; no case work; internal battery required.
- **Round 4 scores:**
  - **HUSH 9**, to the owner. Must test: steam-blocking felt directly on a PLA/PETG shell risks warping (≈ 100 °C steam). The corner test decides; the fallback is blocking over a separate form. Also the I/O board x ≈ 60–230 and the speaker x ≤ 243.
  - **FOLD 7.** Blockers:
    1. the ≈ 119 mm mid-deck gap (open 286 × 234). Fix: slim cells (≈ 8 × 30 × 40 class) in the existing 31 mm lid band, halves back to ≈ 86–90, PLAY→VOICE ≤ ≈ 60, open ≤ ≈ 185;
    2. EMPHASIS split from CUTOFF across the hinge. Eng: can it cross the ribbon? Otherwise it's an owner decision;
    3. black section names, not ochre.
  - **ONE SHEET 8, unchanged.** The coupon is still unprinted. Print it: reads → 9, doesn't → drop.
- **New lesson:** FOLD couples its halves' depths. Any added depth shows up twice, so check the open depth after every change.
- **Next:** HUSH to the owner. FOLD redraw after systems/eng answer the battery and EMPHASIS questions. ONE SHEET waits on a physical coupon. If the owner turns down a 9, record his reasons here.

## Earlier status (after round 3 scoring, 2026-11-12): READ THIS FIRST
- **Round 3:**
  - **HUSH 9** (cream knobs, "Nothing shouts"; NOT black as the coordinator said).
  - **FOLD 9**: one white panel, black knobs, walnut palm rest, 12 mm panel shift, closed 51 shown beside a book. **Must-fix before handoff:** TUNE collides with the bend stick when closed (a ≈ 6 mm well or a lower cap). Systems also confirms the shift, the 18T pot shafts and the black knob's price.
  - **ONE SHEET 8**: "toolpath is the finish" is the right idea, but it's unproven. It needs a photographed test coupon (≈ 80 × 80, three regions, smooth PEI) on sheet A. Coupon reads → 9. It doesn't → drop the concept.
- **With the owner at 9:** TYPE CASE, HYMNAL (round 2), HUSH, FOLD (round 3). The owner was waiting on HUSH and FOLD before approving.
- **Carry to the owner:** FOLD at 51 closed (≈ 44–47 floor) vs HYMNAL's 38; names from `naming.md`.
- **Next:** the owner picks a concept, then handoff.md. Check handoff.md against the approved concept and owner.md, and send back any drift. If the owner turns down any 9, record his reasons here.

## Earlier status (after round 2 scoring, 2026-11-12): READ THIS FIRST
- **Owner context:** the budget instrument is now THE instrument ("the most interesting thing overall"). He liked TYPE CASE, HUSH and HYMNAL. "Little D" is dropped as a name (`../naming.md` has candidates; WALLOP is ★). His hard rules: nothing raised among the knobs, nothing raised between the keys and the controls, and tactile section separation only if it doesn't get in the way. 3D-printed enclosures are welcome; knobs and keys must still be bought. He asked for printed ONE SHEET, printed HUSH + felt, and FOLD (two parts, controls on top, a white panel in a dark surround, printable first, walnut later). He saw the round-2 A sheets unscored.
- **Round 2 scores** (`../scores.md`):
  - **TYPE CASE 9** and **HYMNAL 9**: these go to the owner.
  - HUSH 8: blocker is the yellow knobs (loud and toy-like on the "hush" concept). Fix: cream.
  - FOLD 7: fixes are one white panel in two plates (not five), redraw at closed ≈ 51 plus show the ≈ 44 floor, give the palm rest a job and a surface, show scale when closed.
  - ONE SHEET printed 7: its idea lives in the making, not the object. Either make the print visible on the face, or retitle it as the plain baseline.
  - **UNDER GLASS 6: killed.** Parallax hides the windows, it's over cost, and the owner never asked for it.
- **New rulings:**
  - **R5:** a knob colour must follow from the concept's idea; repeating a colour is fine. This replaces my round-1 "different colour per concept".
  - **R6:** five concepts maximum in front of the owner.
- **Still in force:** R2 (pitch ≥ 20, IV's played row 25/24, ≥ 7 mm to a section break), R3 (≈ 36 body / ≤ 40 to knob tops; FOLD closed is the exception, for the owner to decide), R4 (flush).
- **Owner questions to carry with the passes:** FOLD at 44–51 closed vs HYMNAL at 38? Any name from `naming.md`?
- **Next:** one quick round (HUSH colour, FOLD fixes, ONE SHEET choice), then re-score. If the owner turns down a 9, record his reasons here: they are the best signal of what a 9 means to him.

## What a 9 has meant so far (my calibration)
- Every visible choice traces to one idea, the round's owner rules are met, there's a lean cost default, and the owner's hand has a place. Plus, from round 2: it has to be the most interesting version of itself, not just a tidy one.
- My blind spot: economy and process ideas (ONE SHEET, my own) don't make a form by themselves. Device rules I add for the set (knob colours) mustn't override a concept's own logic.

## Earlier status (after round 1 scoring, 2026-11-12) — READ THIS FIRST
- Round 1 scored (`../scores.md`): **TYPE CASE 8, HYMNAL 8, HUSH 7, ONE SHEET 6 → replaced by UNDER GLASS.** Nothing at 9; nothing to the owner yet.
- Rulings: **R1** lip rule H3 retired (bought Choc V2 switches; lip no longer mechanical) → H3' "key edge": comes from the idea, hides switch housings/strip C, prevents snags; section kept as fit check only. **R2** knob gaps: 4 mm rejected; keep Tayda KN1250; min 20 mm pitch, 24 mm for IV's played row (CUTOFF/EMPHASIS/CONTOUR AMT); take width from section gaps; never shrink the knob. **R3** thickness vs owner's ~36 body / ≤40 knob tops; all depend on eng E-L2 (thin speaker) — must be answered before round 2.
- New owner answers absorbed: show BOTH self-protecting and sleeve (UNDER GLASS = sleeve now, the other three self-protecting); velocity LOUD/BOTH/FILT toggle; bend up+down; "Nods are fine but I want to see breadth of explorstion"; ~36 mm body; standard printed board; show BOTH flat tops and pegs (HUSH pegs, rest short flat tops); no custom keys → Choc V2 silent + pressed tops (eng velocity-and-keys-v2.md; short tops S1 default, piano tops +$29.85 stabs).
- Owner is impatient ("Where do I see these?"). One fast fix round, then show all four together.

## Round 1 record
- TYPE CASE 8: right idea, use-pole done well. Blockers: rim 40 reads chunky; knob crowding; grey blank cards. Fixes: R2, rim ≤38 + edge chamfer, real card content, thumb-at-wall view, ≤$15 India ink.
- HYMNAL 8: best vibe picture; patch chart in lid; drop-front palm rest. Blockers: cost (+$15–34 enclosure + $29.85 stabs), retro costume (red knobs, script label). Fixes: short tops default (piano as +$30 inset), lean ≤$20, modern neutral panel, label as the owner's own placeholder, show drop-front latch.
- HUSH 7: most distinct form (maple pegs through felt). Blocker: cost $59–63 wool / $30–40 blend. Fixes: ≤$30 version (felt on deck/panel only, flap optional), one hard-plate material, eng check felt bottom stop vs velocity, wear inset.
- ONE SHEET 6 (my own idea; cut it hard): idea invisible in the 3/4, reads as TYPE CASE without walls / default laser slab; all-birch keys lose white/black; lip ruler has no job; fails "breadth". Its making rules survive as an option for ply concepts.
- UNDER GLASS (new for round 2): printed board under reverse-painted clear acrylic with windows; aluminium U-channel rails; sleeve body; different knob colour; ≤$20.
- Set-level blocker: **breadth** — one footprint, one layout, cream knobs. Fix through materials, knob colour, hero camera state.

## Updated blocker hypotheses
1. Cost vs vibe (confirmed: HYMNAL and HUSH lose their 9 on cost).
2. Sameness across the set (new; owner explicitly wants breadth).
3. Thickness depends on unanswered E-L2.


## Earlier status (end of jam, Turn 3, 2026-11-12) — partly superseded above
- Phase: concept jam has CLOSED with READY. **No scores yet.** The first scores will be provisional because no brand or visual foundation exists.
- Full-instrument design is PAUSED (owner). Its director notes are in `archive/full-instrument/notes/director.md`; I kept consistent with them: hero CUTOFF, one light, no Moog cheeks, cost/rigmarole as the recurring risk.
- Concepts going forward: **TYPE CASE, ONE SHEET, HYMNAL, HUSH.**

## The owner's tests for this work (his words → my judging tests)
1. "coherent in form with some clear perspective": a single idea has to generate the silhouette, material, graphics and making. Visual's four-part test is the one I'll use.
2. "Design principles with a solid basis of logic in the idea of the thing": every principle needs a "because" that traces back to what Little D *is* (budget, hand-built, portable and complete, a reduction of the Model D, silent keys).
3. "Get creative" plus the earlier "expected / highly designed for use … and others with more sauce / vibe": the set has to span both kinds.
4. Cost is his main concern ("250 feels high"). Anything that adds cost has to earn it.
5. "it should feel good to use": OP-1 is a loose size reference only.
6. He needs to see mocks to judge looks, so a believable 3/4 picture per concept is mandatory.

## Key facts that bind the box
- From `eng/keys-answers.md` (arrived mid-turn): slim RAIL keys at ≈ 22 mm, lip ≈ 26 mm, control zone ≈ 30 mm, box ≈ 180 mm deep (was 170). Rod support combs every 3–4 keys, hung from the lip. RAIL ≈ $52–58 ($35–46 on scrap).
- My reading: **the lip is the spine** (top stop + rod carrier + step). This became house rule H3. It's the strongest form-logic hook we have, and it's shared across concepts.
- Envelope ≈ 290 × 180 mm; ≤ 36 mm with knobs; 40 mm ceiling pending the owner.

## Rulings (Turn 3)
- SPREAD merged into TYPE CASE (same kind; SPREAD's enclosure is just a tray). Numerals I–V carried over; emblems optional, no occult imagery.
- RADIO and UNDER GLASS are donors (bottom speaker, kerf band; reverse-painted acrylic). STRATA is dead.
- HYMNAL must resolve book vs cigar box (cigar-box guitar = the folk lineage of cheap hand-built instruments; from my random draw).
- HUSH pairs with DISH maple-plug keys (owner cited Critter & Guitari), if velocity and feel hold.
- ONE SHEET is my own new direction (cost as the idea; one 12 × 24 in sheet; nest arithmetic ≈ 72 % for the shell). **My favourite, so be hard on it.** Its kill risks: the laser-craft / Etsy look, nest-forced proportions, the story staying invisible or turning into a gimmick.
- House rules H1–H9 in jam.md §4: inherit logic not looks; prune don't shrink; lip is the spine; one hero knob (CUTOFF) plus one bought knob family; cost discipline (enclosure > $15 needs a named saving); machine marks exact / hand marks meant; one status light, not-in-control light by CUTOFF, guarded power switch; envelope; jacks on one edge, never the stick end.
- Deliverables per concept: jam.md §5 (3/4 picture, top view in mm, H3 section, carry/play states, principles with "because", cost/hours/thickness, six axes).

## Likely owner objections (watch for these when scoring)
- **Cost creep**: HYMNAL (+$10–20) and HUSH (+$15–30 felt) in particular. The biggest risk, given his history.
- **"Laser-cut craft / Etsy"** look: TYPE CASE (tray), ONE SHEET (ply box).
- **Costume**: HYMNAL going "olde", HUSH reading as a tech sleeve, tarot remnants.
- **Too thick**: TYPE CASE ≈ 34–36, HYMNAL ≈ 40 closed.
- **Durability/grime**: felt pilling, bookcloth hinge wear.
- Anything Moog-looking (cheeks, wedge). Note that eng's "key step in front of control zone" is a step, not a wedge; keep it from reading as a wedge.
- Fiddly use: TYPE CASE knobs near cell walls; HUSH roll flap as rigmarole.

## Open questions
- With the owner: trade dress for Little D; bend up-only vs one axis; bare vs printed board; self-protecting or sleeve; 35–40 mm OK; **(new) +$10–20 for self-protection vs ~$12; (new) flat key tops vs maple pegs.**
- Non-owner: Vector Space laser bed size and sheet stock (ONE SHEET depends on it); knob family from real Tayda/US stock (visual, before mocks); DISH velocity/feel (keys/eng); wool felt price per real area; bottom-speaker loudness on a lap.

## What's blocking a 9
Nothing scored yet. My hunch for the recurring blocker: **cost vs vibe**. The sauce concepts get their charm from added material, and the owner's first concern is cost. The second hunch is **laser-craft genericness**: proportions and joinery that read as "made on a laser" rather than as an instrument.

## Next
Concept building (systems + visual) on the four, against H1–H9 and the §5 deliverables. I steer after every pair of their turns. Then I score all four in one pass, naming the owner objections first. Kill and replace any concept that can't reach 9; ONE SHEET gets no favours.
