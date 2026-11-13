# Director notes: Little D (budget instrument), physical design

## CATHEDRAL top panel, steer 3 (2026-11-13 ~18:05): READ THIS FIRST
- **Owner did NOT approve the 9.** Verbatim (screenshot design/owner-refs/2026-11-13-1800-top-panel.png): "lets focus on top panel first -- the items do not appear to be grouped or ordered in a way that makes logical sense. have the team break down which concepts belong together, and reorient accordingly.  there are tons of examples on the internet of good organization beyond the model d itself for the add'l functionality. also i dont like the effects controls at the top ... when i think of signal order it's synth stuff -> fx stuff -> output stuff like volume. so it at the top of the layout is confusing"
- **His reasons (what a 9 means to him):** panel logic = signal order and whole groups, not just symmetry and geometry. I scored balance, the band and acoustics; I didn't test "can he read the signal path at a glance". **New test for every layout from now on:** trace the signal on the image; every group must be contiguous and in signal order.
- **My diagnosis of the screenshot:**
  1. FX at the top: standing or flat, the lid reads top → bottom, so FX reads first.
  2. The mixer is split round the window and out of order (osc 2 top-left, osc 1 bottom-left, noise top-right, osc 3 bottom-right).
  3. The switch line mixes four groups (source = mixer, filt mod = filter, velocity, touch = aftertouch).
  4. The two contours are unlabelled as filter vs loudness, and sit far from the filter (base).
  5. The "osc 3" toggle vs the "osc 3" level: same words for different things.
  6. The decay/kbd toggles are isolated at the far right.
- **Fixed constraint I found:** the window must stay at CUTOFF's closed landing (143, d ≈ 32–40), because CUTOFF is the base's one tall knob (R-LOW). So any arrangement flows around a fixed centre window, unless CUTOFF gets a low hero (none bought exists).
- **Director's lead proposal ("page order") for systems to test against 1–2 alternatives:**
  - upper two rows = synth, left → right: OSCILLATORS (block) → MIXER (osc 1, osc 2, osc 3, noise/ext in order, top row centre, over the window) → CONTOURS (filter then loudness, labelled), with each group's switches inside it;
  - bottom row (nearest the hinge) = ECHO (left of the window, FREE/SYNC by TIME) → REVERB → OUT (pans, FOLLOW, volume) right of the window;
  - reads top-left → bottom-right like a page; FX next to the hands; output ends at the corner beside TAP.
- **Briefs sent via the orchestrator** (systems: concept breakdown + references + 2–3 arrangements with checks; visual: lid top view of the chosen one only). Then I score.


## CATHEDRAL fix check (2026-11-13 ~17:40): READ THIS FIRST
- **CATHEDRAL 9 CONFIRMED → publish and show the owner.** Checked by eye on the re-rendered nave-top, nave-standing and nave-closed-side.
  - Fix 1: FX row centred on the axis. ✓
  - Fix 2: section names back, name plate under the window. ✓
  - Fix 3: R3 gone; base right reads MOD MIX, DRIFT, TAP, balanced against the left. ✓
  - Fix 5: 0 label collisions on the real model (systems). ✓
  - Fix 6: conditions stated in §16 (systems; not re-read by me).
- **Fix 4, hinge ear: accepted as is, not a blocker.**
  - With the lid flat and the seam closed, the axis sits at or behind the back face, so a ≈ 4 mm round ear remains at each rear corner (down from 6). It's only visible from the side/back.
  - He said "if not these are fine" about knuckles, and this is quieter than knuckles.
  - **Tell him plainly on the site:** the pins are hidden; a 4 mm ear remains; the alternative is knuckles or a pivot redesign (his call if he minds it). A form change goes to him only if he asks.
- **Carry to the owner with the 9:**
  - closed ≈ 55.2 depends on snap-in pots/counterbore + the lowered stick (else 56.7–58.8; R-TALL 59.7 keeps the big knobs);
  - played-row knobs Ø 10 gold;
  - moved controls (mixer around the window, CUTOFF on the axis, MOD MIX and DRIFT to the base);
  - the 4 mm hinge ear;
  - buy-and-test T1/T2.
- **If he turns it down, record his reasons here.**


## CATHEDRAL, score after steer 2 (2026-11-13 ~17:20): READ THIS FIRST
- **Judged:** how-it-works §16 and look rev 4 images (nave-standing, nave-top, nave-closed-side, speaker window + section, keys A/C).
- **The work really changed.** It's a re-architecture, not restyling:
  - the band is gone: three lid rows at an even 35.05 pitch, one switch line, the only knob-free area is the window;
  - root cause stated;
  - R-LOW: low Tayda gold Ø 10 × 8 knobs on the played row, stick lowered, closed ≈ 55.2 (R-TALL 59.7 as the fallback);
  - Ø 46 window, vertical slots, ≈ 73–83 % of Sd open, gasket, sealed stuffed 20–25 cc back box, honest +3–6 dB at 1–5 kHz;
  - centred on x 143 over CUTOFF (CUTOFF ↔ EMPHASIS swapped), mixer symmetric ± 39.5;
  - battery to the base rear strip (tip threshold up to 8.4 N);
  - keys A (brass naturals, black-plated brass sharps, one velocity calibration);
  - base row mirrored, stick ↔ TAP.
- **Score: CATHEDRAL 8.** Not a 9, because of these likely owner objections, all visible in the images:
  - (a) the FX row runs x 62.5–260.5, so the lid's top-left corner is empty (DRIFT left). That's an off-centre gap of exactly the kind he just objected to;
  - (b) R3 is a knob with no function or legend;
  - (c) the lid lost its section names (oscillators / mixer / contours);
  - (d) closed side view: the side-pivot ear projects as a lobe past the back outline. "Hidden" hinges shouldn't add a bump.
- **Fixes (I check by eye, no re-score; then publish):**
  1. Re-centre the FX row about x 143 (groups and breaks kept; FREE/SYNC and FOLLOW move with it).
  2. Restore the lid section names in the hand.
  3. Remove R3. Re-space the base right section (MOD MIX, DRIFT, TAP) so stick ↔ TAP still mirrors and nothing reads as a missing knob.
  4. Keep the pivot ear inside the block outline (axis or ear within the rear radius, or the rear radius enclosing it). Re-render the closed side.
  5. Re-run the label check on the visual model (systems' 0 used estimated label sizes) → 0.
  6. Doc honesty:
     - 55.2 depends on snap-in pots or a counterbore plus the lowered stick (else 56.7–58.8);
     - the played row's knobs are now Ø 10 (from 14.9): say so, offer R-TALL as his alternative.
- **Watch items (not blockers):** small Ø 10 knobs on the played row (feel); loudness from a 50 mm driver is still modest; mixer, switches, CUTOFF/EMPHASIS, MOD MIX and DRIFT all moved (he allowed moving components).
- **Lesson:** a re-flow that removes a control from a row leaves a hole at the row's end. Check every row's extent against the axis after moves.


## CATHEDRAL, steer 2 (2026-11-13 ~16:55): READ THIS FIRST
- **Owner, verbatim (16:52):** "ok i dont think you're really thinking here — off center in that middle section is bad looking. aso consider the sound of the speaker and the shape... which will work best and give me the best sound out of the chosen speaker. in fact none of my feedback on why it's a problem have been addressed. there's a massive horizontal gap -- the speaker doesnt feel resolved. this may mean moving components. i'd rather have more brass than black re: keys too."
- **What went wrong (mine as much as the team's):** since 14:18 we offered grille shapes that fit leftover band space. My steer 1 even ruled on grille shapes instead of the band. **Lesson:** when the owner names a gap, find what forces the gap before styling what fills it.
- **Root cause:**
  - closed, base y lands on lid d = 108 − y;
  - the PLAY row (y 68; knob tops z 29.1, CUTOFF 27.75) lands at lid d ≈ 40, where lid knobs reach down to z ≈ 24;
  - overlap ≈ 5.1 + 2.0 clearance, so nothing tall can live there, which makes the band 37.55 clear vs ≈ 8.5 between other rows;
  - the base landing strip is the mirror case for V1.
- **Direction ("nave and rose"):**
  1. **R-LOW (primary):** bought low-profile knobs on the base PLAY row (≤ ~9 mm above the plate; CUTOFF a wide, low hero dial). Lid knobs can then land over them with ≥ 2.0 clearance, closed ≤ ~56. Lid rows re-spaced evenly, so there's no knob-free strip wider than a row gap except the speaker window. Shrink the landing strip / halves if possible.
     - **R-TALL (fallback):** today's knobs plus ≈ +7 closed (≈ 60). Systems gives the numbers for both; I choose.
  2. **Speaker from acoustics:**
     - one round opening concentric with the 50 mm CDS-5076-1SP, Ø ≈ cone + surround (≈ 42–46);
     - open area ≥ 50 % of Sd, target ~60 % (today 265–440 mm² ≈ 20–35 %: choked);
     - vertical slots (his preference) ≥ 1.5 wide, or holes; web thinned to ≤ 1.2;
     - front gasket; sealed, stuffed printed back box; magnet distances kept.
  3. **Placement:** centred on the axis x 143 in the lid. The mixer column widens symmetrically around it (pairs flanking; switches re-flowed). The window sits directly above CUTOFF/EMPHASIS, giving one vertical axis.
  4. **Base PLAY row symmetric:** stick at the left end ↔ TAP at the right end, hero on the axis, no empty right end.
  5. **Keys:** A (brass naturals, black sharps; normal reading, more brass) as the lead; C (all brass) as the alternate; metal shader. Systems picks the sharps' material (black-plated brass vs printed black + per-group velocity curve).
  6. **Keep:** the effects row on the lid back with the pans/FOLLOW/VOLUME, FREE/SYNC, stereo out, nothing raised among the knobs, no screens, closing ≥ 2.0, no machining, side pivots, no spine, R 7.7, screw-feet, woody relief, the palette.
- **Deliverables asked:**
  - systems: how-it-works §16 (root cause, route numbers, clearance table, new x/d table, acoustics) and checker 0 incl. labels;
  - visual: rev 3 with open 3/4, standing 3/4, exact top, exact closed side elevation, speaker top + section, keys A/C; an opening paragraph answering his three complaints; HTML captions.
  - Publish (site/publish.sh) only after a 9. Commit specific files only, as Adam Trabold, no Claude credit (HANDOFF).
- **Status:** I could NOT deliver these briefs. SendMessage to ac0e7aeee47bf1a1b (systems) and a26f3d36a52e6b5d4 (visual) failed: "only the main conversation can resume" them. The orchestrator must relay this section to both (it's written to be sent as is).
- **Not scored:** no new work exists yet.
- **Likely objections when scored:**
  - low PLAY knobs change the played row's feel (R-LOW) / thicker body (R-TALL);
  - re-flowing the mixer moves controls he has learned;
  - brass mass and velocity;
  - loudness still modest from a 50 mm driver (honest numbers needed).


## CATHEDRAL, steer 1 (2026-11-13; round counts reset): READ THIS FIRST
- **Owner (owner.md 14:12–14:41):**
  - lock in on CATHEDRAL (= CHAMBER, renamed as the point of view) with FOLD v1.1 as the middle ground;
  - no spine; hidden hinges if possible; the speaker gap; FX together with echo/reverb; feet = screws; woodier fine line texture (he designs the pipe lines himself);
  - consistent plate rounding; fewer colours (the brown pegs out of place); a rounded grille;
  - no machining (keys printed or bought; external and metal printing OK); brass + black or all-brass keys; bought wood caps on a shaft also OK.
  - RAIN parked.
- **Judged:** how-it-works (§0–13) and how-it-looks-and-feels rev 2, plus images (6 key colours, A/B standing, grille options).
- **Not scored.** Two reasons:
  1. the standing and closed renders still show the retired spine and rev 1 keys;
  2. four owner decisions change the form (layout, hinge, back slot, keys).
  - I score after his answers and one re-render pass. Nothing to him at a score yet; the decisions go now.
- **Team rulings (no owner needed):**
  1. All 8 plate corners R 7.7: yes.
  2. Screw-through rubber feet at the 4 corner screws; the axis screws stay flush brass (no impost clash): yes.
  3. Grille: tapered horizontal slots (his first option). Vesica 66 × 16 in A (the Ø 34 circle hits labels); Ø 27 circle in B. Concentric arcs dropped.
  4. **Fine-line woody texture is built, not deferred.** Visual's "leave the print plain" doesn't deliver his ask on the only build he'll make (real walnut = machining, now out).
     - Model sparse cathedral-grain arches as shallow relief/grooves on the printed walnut-tone body (sides, base underside, lid-back field), at about the old line count.
     - The lid back's figure waits for his façade, so leave the field ready.
  5. One visible metal: brass. Stays cast brass from the keys' service (fallback: matte-black PETG 5 × 8, never grey 316L in view). Hidden hinge leaves 316L. Axis screws brass. Feet black.
  6. Palette: walnut, cream, black, red CUTOFF, brass. No other colour; TAP is made of the key material.
  7. Option A heading → "effects".
  8. Keys use one carrier interface (Ø 9.6 cup / 9.53 × 3.2 tenon) so the head choice stays swappable after the build.
     - Buy one Cherry Tree Toys pack and measure head height H before fixing the lid height.
     - Test one hollow cast-brass head (2.5–3 g) on one Choc V2 before ordering.
  9. **Brass can't be judged from a flat-yellow render** (it reads as mustard plastic). Before he chooses keys, show brass with a metal shader/specular, or a real photo of polished brass domes as reference.
- **Owner decisions (worded in my reply):**
  - Q1 layout A vs B (moves controls; the gap itself can't go because it's where the base knobs sleep closed; B leaves the band plain; B costs reach for the FX amounts and TAP);
  - Q2 hidden pins vs cables-through-hinge (mutually exclusive);
  - Q3 the back slot with no spine;
  - Q4 keys (B reversed: black naturals + brass sharps, rec; A normal-reading: brass naturals + black sharps; C all brass).
  - **Recommendations:** B layout, hidden pins, slot left open but finished dark inside (S1), keys B.
- **Likely objections when scored:**
  - B: the FX amounts and TAP are far from the hands while playing; the band stays blank.
  - A: the split remains.
  - Brass looking toy-like in renders.
  - +2.6–4 mm closed with pegs, depending on H.
  - The open back slot.
- **Next:**
  - Designers, in parallel with the owner's answers: radii, feet, grille, woody relief, the brass material look, measure H, one brass head test.
  - After his answers: re-render closed, standing (chosen layout) and keys, with no spine; then I score.


## BRANCHES, R1' check (2026-11-13): READ THIS FIRST
- **RAIN 9 CONFIRMED.** Checked by eye on the re-rendered `rain/img/rain-arms-length.jpg` (look doc rev 2.2).
  - Rings stop ≈ 7 mm out (deep to 3.5, shallow to 7), and the far-field hatching is gone.
  - Big rear and corner cells are now still pools. It reads as drops on still water: the calmest, truest version.
- **Watch item for the owner's reaction, not a blocker:** at arm's length RAIN now sits closer to v1.1 ONE SHEET.
  - The section map comes from still lanes and clustering, not seams.
  - What differs is the whole point of view: every element ripples (keys as stones, toggles, stick, TAP), no grooves or headings, the warm stone, and the one mustard leaf.
  - If he says "this is just ONE SHEET", that's the reason.
- **Both concepts go to the owner: CHAMBER 9 (FOLD) and RAIN 9 (ONE SHEET),** with the 7 questions in the round-2 section below.


## BRANCHES, R1 check (2026-11-13): READ THIS FIRST
- **RAIN's 9 is WITHHELD.** R1 was checked by eye on the re-rendered `rain/img/rain-arms-length.jpg` (look doc rev 2.1).
- **What changed:** only a 1.5 mm still margin at the outline.
- **What didn't change:** the rear corners and the band behind the back row still show the same straight far-field hatching, the thing R1 was for. My R1 wording ("the decay finishes everywhere") was read as "the edge too". The real problem is that the far-field rings never finish.
- **Re-issued fix (R1'):**
  - cap each element's ring field at a fixed reach beyond its ring start: ≈ 6–8 mm (≈ 3 deep + 2–3 shallow rings);
  - still water beyond, whatever the cell size, so big rear and corner cells become still pools instead of hatching;
  - re-render arm's length only;
  - I check by eye. If the hatching is gone, the 9 stands with no re-score.
- **CHAMBER 9 stands.** It can go to the owner now, or wait to travel with RAIN. Systems' coverage says both pass every job (coverage.md); I didn't audit it.
- Questions to carry: unchanged (round-2 section below).


## BRANCHES, round 2 scores (2026-11-13): READ THIS FIRST
- **Judged:** CHAMBER and RAIN looks docs rev 2 and how-it-works rev 2, plus the re-rendered images.
  - CHAMBER: standing, closed-with-book, fallback pegs.
  - RAIN: arm's length, close, 3-way pitch compare.
  - `branch_check.py` §7/§8 reports 0 legend/tick collisions and 0 fails (systems; I didn't re-run it).
- **The work really changed in both.** Each fix shows in the images, not only in the text, so the higher scores are earned.
- **CHAMBER 9 → to the owner.**
  - **Standing lid now reads cream.** A render correction, disclosed; the real plate is cream.
  - **Hinge slot closed by a flexible oxblood bookcloth spine.**
    - Taut closed, it's the case's back panel. Open, it folds into the seam gap, so R4 holds. Standing, it shows as a soft drape.
    - It reads as a book joint, and it gives the case its one warm cloth note.
  - **Fallback peg colours are drawn**, so his answer on reversed keys can't sink it.
  - **The push-outs became two real pipe mouths** (pitch 8.75), so the decoration now does a job.
  - Kalam throughout; both artefacts gone; walnut plugs sourced (~$0.32 each, shank fit UNVERIFIED).
  - **Remaining owner objections (not likely enough to hold it):**
    - 52.7 closed (+2.6 over v1.1);
    - reversed keys (fallback ready);
    - spine wear.
  - **Pre-build checks, not score blockers:** plug shank fit (one sample), spine flex life, the ribbon loop sharing the seam gap, engraved/relief fill on wood-fill PETG.
- **RAIN 9, conditional on one fix I check by eye (no re-score) → then to the owner.**
  - **Decay works:** deep 0.4 rings hug each control, then shallow 1.8-pitch rings, then still water. Close up it reads as ripples dying out.
  - **Section lanes** (3.0 between sections vs 1.0 inside) now draw the map at arm's length.
  - **Palette** is warm stone with one mustard leaf; no longer concrete.
  - **0 legend collisions.** The 3-way pitch compare is honest about 0.9 vs the loved 0.45.
  - **Condition R1:** remove the "rings continue to the panel edge" exception. Let the decay finish everywhere, so the edge is still water like every seam.
    - At arm's length the far-field rings at the rear corners and the rear band read as straight hatching, the busiest part of the face.
    - This came from my round-1 "run to every edge" note, which conflicts with my own decay fix. The decay rule wins: one rule, no exceptions.
    - Re-render arm's length only.
  - **Pre-build checks:** the ring coupon (0.4/0.2 depths, seams, lily pads, under a tree), a one-piece print on a 350 bed, peg survival in a bag (case work is still his deferred topic), sun legibility.
- **What kept blocking a 9 across rounds (branches):**
  1. renders contradicting the concept (grey lids, an un-mirrored edge, snag cords);
  2. legend collisions;
  3. ideas living in a small part of the object (BUTTERFLY, DIPTYCH; both cut).
  - Now: (1) is fixed by checking each view type; (2) is fixed by the checker counting legends; (3) is fixed by cutting.
  - **New lesson:** my own round notes can conflict (edge vs decay), and the designers follow both literally. When I add a fix, re-read my earlier instructions for clashes.
- **Questions to carry to the owner with the two concepts:**
  1. Reversed keys or the fallback (CHAMBER, both drawn)?
  2. Pegs worth +2.6 mm closed on FOLD (zero width cost on ONE SHEET)?
  3. How long is a park session (battery)?
  4. Send the tapped tempo out as MIDI clock?
  5. The furniture book's title and author?
  6. TIME has a dead 15° at each end to keep its scale honest: OK?
  7. (RAIN) Does Vector Space have a 0.25–0.3 mm nozzle? It allows 0.6 mm rings, nearer the 0.45 he loved; otherwise 0.9.
- **Next:** check RAIN R1 by eye → both go to the owner (CHAMBER for FOLD, RAIN for ONE SHEET). If he turns down either, record his reasons here: they are the best signal of what a 9 means to him.


## BRANCHES, steer 1 + first concept scores (2026-11-13): READ THIS FIRST
- **Owner since my jam turn (format):** no A3, nothing printed; images made to look great on the site, viewed responsively (not phone-first); **images only for what must be visual, all text in HTML.** So concepts are now markdown + separate images; sheets are retired for new work.
  - My ruling: labels that point at geometry (dimensions, scale bars) may stay inside a drawing. Captions, principles, notes and comparisons ("v1.1 · 0.45 mm") go in the HTML.
  - True-scale "px per mm" files are fine as references, but never claim "real size" on a screen.
- **What I judged:** each branch's how-it-works + how-it-looks-and-feels and its images (looked at the 3/4s, states, close-ups, 1:1 crops, the DIPTYCH side elevation). Not the designers' notes.
- **Kill: DIPTYCH (my own; the d20 had said 15, judgement overrides).**
  - Its spine failed physically: cords alone tip at 0.8 N, while a knob turn pushes 1–3 N.
  - The fix (fold-out brass feet + 4 eyes + a feet-before-cords order, which tips if done wrong) is worse than v1.1's two stays that do both jobs. That's a regression on cost, simplicity and his "blend into the case" stand.
  - Without the cords, at arm's length it's v1.1 FOLD with serif type and red hairlines: a graphics variant, not a point of view.
  - The 3/4 also drew the cords at the snag geometry (to the base front corner), contradicting the s 60 elevation, and the standing lid rendered grey.
  - **Donor:** the red/black TIME dial with written divisions (1/16, 1/8, 1/4, 1/2) is the best TIME dial in the set. Any branch may adopt it.
  - Its open points (cords vs stays, 38.4° vs 37.4°) are moot.
- **READY: CHAMBER, RAIN, BUTTERFLY. Scores (concept phase, judged on the idea):**
  - **CHAMBER 8.**
    - The idea holds. The façade from the keyboard's numbers reads as pipes in plain line work, not costume. The three states work. The reverse pegs make the standing view read as a chamber organ, the best picture in the set.
    - Below 9 because of likely owner objections:
      - (a) the standing lid face renders grey, the exact thing he asked about (FOLD's face should catch light);
      - (b) closed, the hinge-side slot shows the knobs and keys, so the "case" doesn't read as closed;
      - (c) reversed colours: an owner question that could sink the concept on one answer;
      - (d) +2.6 mm closed (52.7): minor.
  - **RAIN 7.**
    - Close up it's beautiful (raked garden, rings, lily pads). At arm's length it reads as crazed or cracked grey stone, not still water.
    - Grey shell, grey stones, grey walls, grey bats: calm becomes drab.
    - Every knob is its own cell, so a seam inside a section looks the same as one between sections. The seams don't yet draw the *map*.
    - Legends collide (REVERB TYPE/VELOCITY, ECHO TYPE/OSC 3 CTL): the set lesson again.
    - The 0.9 grooves are coarser than the 0.45 he loved.
  - **BUTTERFLY 6: replace (retire), not fix.**
    - The point of view governs a 15 mm, 6 mm-thick strip. The rest is v1.1 ONE SHEET in bone, so the owner's line will be "ONE SHEET with a plank".
    - The branch rule (the board is constant, legends reach y 165) caps it: there's no honest way for "tool to tree" to reach the face.
    - The 3/4 and from-behind renders also show an un-mirrored edge, contradicting the end-match.
    - **Donors:** the tabletop-over-apron rear (jacks sheltered under an overhang), and the wall elevation's live edge reading as a horizon.
    - I'm not replacing it: CHAMBER (FOLD) + RAIN (ONE SHEET) cover both of his leans.
- **Rulings on open points:**
  - FREE/SYNC left/right throw (systems' fix; "the lever points at the word") accepted over my fore-aft.
  - ±135° printed sweep + firmware clamp accepted (dead 15° at each end; tell him).
  - Set-wide: drop the top ticks of OSC 2 / NOISE-EXT under "free"/"sync"; the checker counts tick rings and legend-vs-legend.
  - CHAMBER: "mono / para / +4" accepted; push-out holes to d 90 accepted if clear of the d 96 screws (systems); a spine wall or lid lip closes the hinge slot (systems to say whether the slot is real).
  - RAIN: power-on drop sound optional (power-off is impossible on the hard switch).
- **Fixes for round 2:**
  - **CHAMBER:**
    1. re-light the standing renders so the lid face reads cream (check like v1.1 E);
    2. close the hinge-side slot (spine wall / lip) and re-render closed;
    3. one image of the fallback peg colouring (maple naturals, walnut sharps), so his answer on reversed keys can't sink the concept;
    4. push-outs to d 90, PARA legend, Kalam (not the stand-in) before he sees it;
    5. fix the white streak artefact on the walnut pegs and the pale band on the base front face in the close render;
    6. the walnut button-plug source (or maple stained dark as the fallback, priced).
  - **RAIN:**
    1. **the ripples decay**: groove depth/width taper to nothing toward each seam (real ripples lose amplitude with distance; still two finishes), so seams are still-water bands, not drawn lines;
    2. **sections are wider still bands**: weight the power diagram so a seam between sections is ≈ 3× a seam inside one, which makes the map;
    3. warm the palette off concrete (pale wet stone with warmth; the walls carry the field over the chamfer; keep two stone greys and the one mustard leaf);
    4. fix every legend collision, with the checker counting legend-vs-legend;
    5. a 3-way pitch compare (0.45 / 0.6 / 0.9) in HTML, with only the drawing as the image;
    6. re-render at arm's length and close.
- **What keeps blocking a 9 (carried from v1 rounds and now in the branches):**
  - (1) an idea that lives in a small part of the object (ONE SHEET r1–4, BUTTERFLY now; DIPTYCH's faces);
  - (2) renders inheriting old geometry or lighting that contradicts the concept (the joystick slot in v1.1; now the un-mirrored edge, the snag cords, the grey lids);
  - (3) legend collisions whenever text changes.
  - Why it keeps happening: the render pipeline is shared and models are reused across branches, so each view type needs its own check against the concept's words.
- **Owner questions (from the jam, still open):** reversed keys; pegs worth +2.6 mm closed on FOLD (width on ONE SHEET is now 0 with the 14 mm washer); park session length; tap tempo as MIDI clock out; the book's title. **Plus new:** TIME has a dead 15° at each end (to keep its scale honest): OK?
- **Next:** CHAMBER and RAIN round 2 on the fixes above, then I re-score both. Nothing goes to the owner below 9.


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
