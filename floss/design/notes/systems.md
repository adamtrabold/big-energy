# floss: systems designer notes

## Where things stand (2026-11-22, round 2: the systems turn after the director's steer 2, plus eng r3)
- **New input:**
  - **Director steer 2** (`director.md`): **S1** YOKE becomes a concept and absorbs CLOTH (the wrap and the grass mat become YOKE options); **S2** knob A is the module baseline, with B as a column for the owner; **S3** the house colour is walnut-brown (visual's); S4 face fixes (visual's); S5 SPINE's area overlap is mine to fix. Going on: **FALLBOARD, SPINE, YOKE**.
  - **Owner:** "The carry should fit a portable MIDI controller but the case does not need to surround it just have an attachment point. I'm just saying don't assume not making a rule" / "25 keys idk about voices" / "25 is good for the string machine" (**25 voices, decided**, per the coordinator) / "Speaker let's figure out what will sound best idc method".
  - **`eng/module-r3.md` landed:**
    - **speaker E** (2 × TEBM28, one ported box ≈ 190 cm³, a flared Ø 16 × 140 port, Fb ≈ 145, a ≈ 115 Hz high-pass): **105 deep with ≈ 4 % margin, safe at ≈ 115**; cells to the ends; two stacked boards in the front band; ≈ 125 crown with two grilles; D (the pair, sealed) is the fallback;
    - deck 25; firmware-stepped 9 mm pots (no rotary switches);
    - cell margins ≥ 2 mm; rake ≥ 63°; grille Ø 46 field, Ø 2.0 holes at 2.6 pitch;
    - ASA; split at the dividers (x 74.5 / 205.5) with the speaker box as its own airtight part;
    - bosses Ø 16–18;
    - FALLBOARD's lid needs a 17.5 grid / 1.2 skin;
    - a recessed host pocket ≈ 25–30 deep;
    - SPINE knuckles fine;
    - Pimoroni flat sideways right-angle C-to-C exists at 0.2 / 1 m only.
- **Written (no git):**
  - `concepts/module/how-it-works.md` **rev 3**:
    - knob A baseline (rows y 14 / 31, tabs 23.5–38.5, crown foot 41) with a B column (≈ 42 tall, ≈ 112–120 deep);
    - **E adopted, 105 drawn and stated as conditional** (the trigger for 115: the detailed box losing > ≈ 8 cm³ net; at 115 the ratio is restated as "8 : 1 length : height, depth set by the speaker", not faked);
    - firmware-stepped pots, with "between steps" added to the states;
    - host pocket; S3 cable = straight at the module, sideways right-angle at the keyboard;
    - ASA; three-piece print;
    - **S4: keep the 160 spacing and let the module's insides move** (family call flagged);
    - 25 voices decided;
    - §11 new ENG list.
  - `concepts/yoke/how-it-works.md` **rev 1, new.** Mechanism (my findings on visual's sketch, §0):
    1. **Fixed-angle arms reaching the end's middle cross the end keys in play** → cups hang at the keyboard's **rear corner** and reach forward along the end; the arm never passes over the keyboard.
    2. **The keyboard stays at carry height, so the module stands ≈ 37 up and tips back** → **the cap is the module's rear foot in play** (S1.1); three-point stance; on a lap, the cap pegs into the module's foot sockets (PROPOSAL).
    3. **Widths need different angles** → the pivot is clamped at any angle by the module's own thumbscrew; **the keyboard is the jig**; an index ring keeps the keyboard centred.
    - Numbers [calc]: reach 105–147, one 45 mm slot; arm a T-section 10 tall (a flat 4 mm plate would bend ≈ 15 mm); cup = 21 mm gap, 5 mm foam each jaw (11–16), lip ≤ 8 mm over the end cap, one M4 locks slot + swivel.
    - **Carried 395 × 135 × 74 with an Xkey** (thicker than visual's 64: the rib and the cap).
    - Carry 0.14–0.20 kg.
    - Cable coil on the left arm, adapter on the right, **charger loose** (or in the wrap's pocket).
    - **Chunky minis out** (the wrap can bundle one).
    - Empty: arms off, module + cap.
    - No tilt, no shade (stated).
  - `concepts/cloth/how-it-works.md`: **RETIRED** banner pointing to YOKE §6 (kept as the wrap's making reference).
  - `concepts/spine/how-it-works.md` **rev 2.1**: **area fixed** (lane 280 × 30 = 84; bays 62 × 135 + crescent ≈ 100 each; sums to 404 × 135); r3 weights; knuckles cleared; lane 20 if the module is 115.
  - `concepts/fallboard/how-it-works.md` **rev 2.1**: lid 1.2 skin on a 17.5 grid (+30–60 g); r3 weights; straight plug in the host pocket; 412 × 275 if the module is 115.
  - `jobs.md` **rev 3.2**: job 3 (25-key portable controller; attachment point is enough; chunky minis out of every carry, the wrap can bundle one); job 4 (25 voices, decided); job 15 (best sound, E); job 20 (grass); job 18 (stepped pots); the owner's open questions updated.
- **Kit weights now** (module 0.70–0.85 with E):
  - FALLBOARD 1.51–2.10;
  - SPINE 1.40–2.01;
  - **YOKE 1.12–1.69** (+0.23–0.36 with the wrap).
- **Randomness:** none drawn this turn. The work was mechanism-checking a sketch, not ideation.
- **Next:** visual's turn (director's steer 2 visual list):
  - the module A2 sheet (walnut house, the roof behind the stage, fair arc + 2 facets, B beside it; **and now E's ≈ 125 crown with two grilles**);
  - YOKE A redrawn to this mechanism (cups at the rear corners, the cap as rear foot in play, the 74 stack), plus YOKE B (wrapped, on the grass, in a pack);
  - FALLBOARD and SPINE recoloured.
  - Then the director calls READY and scores. **Then my 9+ coverage check** against rev 3.2.
- **Open:**
  - **Director:** accept YOKE's three mechanism changes (§0) and the 74 mm stack; the cap as a required part; SPINE's 30 lane (still open); S4 kept at 160 (family call).
  - **Visual:** E's crown in the face; the cap's look (it's a visible part in play); YOKE's index ring.
  - **Eng:** E's box at 105 (margin) and the host pocket with the stacked boards; cells + inserts with S4 at 160; YOKE arm stiffness (T-section) and the thumbscrew's hold at any angle; foam for 50 % compression; a 0.3–0.5 m flat sideways cable.
  - **Owner (with the concepts):** E / D / C and the depth; knob A / B; stepped pots without detents; ASA / PETG; FALLBOARD, SPINE or YOKE (+ wrap); split-scoped HOLD; S4 spacing.

## Where things stand (2026-11-22, round 2 second systems turn; new systems seat)
- **New seat:** a new agent took the seat from here. Everything below is history, not commandment.
- **Owner since the last section:**
  - 13:49 T5 withdrawn ("The principles are portable");
  - 13:51 "don't anchor on the page size thing … portable and make sense and be harmonious";
  - 14:06 the family goal is analog-first, and "shimmer and warmth" is floss's own;
  - **14:08 "for now the case will be entirely 3d printed"**, then "Cloth wrapping is fine as long as the core is printed" (PRINCIPLES §7). So: no walnut, ply, bookcloth or brass on any case; hinges and stops printed or bought; state print-bed splits or a service.
- **Director (new) steer 1, R1–R6, done:** see `director.md` "Director handover".
- **Written this turn (no git):**
  - `../jobs.md` → **rev 3.1**:
    - job 30 rewritten (portable, makes sense, harmonious; sizes from parts; ratio; any outline);
    - job 6: no sentence on the module; the card and the site carry it;
    - job 26: printed case, splits stated, no trial steps;
    - job 3: flat right-angle cable as the alternative to a gutter; every area one job;
    - "brass target" → "target";
    - a printed-case constraint added;
    - a rev 3 → 3.1 change table.
  - `../concepts/module/how-it-works.md` **rev 2**:
    - 280 × 105 × 35, 8 : 3 : 1, the hull, the crown, two facets (plan-left set-once ports, plan-right sound and MIDI);
    - x −8.5 everywhere (axis 140; dividers 45.5 / 74.5 / 125.5 / 154.5 / 205.5 / 234.5; inserts at 60 / 220);
    - the paper argument and the Letter alternative deleted; visual's derivation table used;
    - dividers flush and printed (three making methods; the look is visual's);
    - TAP's ring as status, priority low battery > tempo (SYNC, no clock) > charging > steady;
    - the engraved sentence removed;
    - a printed case, with the bed size stated (≥ 300 or a service; axis split as fallback);
    - §11, one ENG list.
  - `../concepts/fallboard/how-it-works.md` **rev 2**: **412 × 265 × ≈ 42.**
    - The gutter is gone; a 15 mm lane is left.
    - **The keyboard sits against the front wall** (it reverses rev 1), so a shallow keyboard's leftover strip is the plug's room.
    - The pockets: left = coil + adapter, right = charger (+ the card, flat).
    - A printed ribbed lid (35 grid), printed lift-off hinges with steel pins, an over-centre brace stay, magnet catch.
    - Tray and lid in four quarters each (220 beds), seams on the axis and the lane; or a service.
    - No lamp.
    - Carry ≈ 0.47–0.60.
  - `../concepts/spine/how-it-works.md` **rev 2**:
    - printed trays, open toward the spine;
    - **geometric stop:** hinge axes 5 mm up; 5 mm beads on the spine meet the trays' 5 mm edge faces at 180°, full length, in compression; Ø 3 steel rods, which also tie the axis seams;
    - spine 49; closed 412 × 148 × 59 (+3 on the director's 56 for the stop face);
    - **"standing" cut** (two hinges can't hold an angle without a brace);
    - bays: left coil + adapter, right charger; the 30 mm lane stays as the cable's run (can't go: one outline set by the Xkey);
    - straight plugs fit any keyboard (49 mm gap);
    - carry ≈ 0.42–0.52 (heavier than rev 1: printing).
  - `../concepts/cloth/how-it-works.md` **rev 2**:
    - near-black coated cloth, cream thread;
    - outline 412 × 265, set 100 from the far edge, so ≈ 435 of near cloth is the seat;
    - **the ground pose** as a flow;
    - the sleeve on a stated ease (no fitting);
    - corner weights' finish is visual's;
    - no stitched sentence;
    - the core printed (owner: fine).
- **Key findings this turn (for the director):**
  1. **R1 conditions 2 and 3 are one problem: the knob.** The deck is rim − 1 − knob − 1 seat. The family's 18T 14.5 × 13.5 → rim ≈ 41; KN1250 14.86 × 10.45 → ≈ 36.5; Tayda aluminium Ø 10 × 8 (CATHEDRAL) → deck 25 and 35 holds. Finger room: with Ø 14.9 the Ø 55 driver needs ≈ 108–110 deep (even rows pulled to y 14 / 35.9 miss by ≈ 1 mm). With Ø 10 rows at y 14 / 31, the crown foot is at 41 and the driver ends at 96 (6.5 spare). **Systems prefers Ø 10 × 8, keeping the family 22 pitch** (director to confirm, or the width reopens). Visual's sheet shows Ø 14.9 / rows 16 / 40; all positions in the module file are for that, with the Ø 10 alternative stated.
  2. **The cells beside the crown:** x 49–109 / 171–231, y 38–88, ≈ 0 margin to the hull wall, ≈ 1 mm to the insert bosses. ENG.
  3. **Ported won't fit the crown** (≈ 76 cm³ vs ≥ 130). ENG to confirm.
  4. **Printing made the rigid kits no lighter:** FALLBOARD's bookcloth-lid lever is gone (≈ 0.47–0.60 vs 0.5–0.7); SPINE got heavier (0.42–0.52 vs 0.3–0.4).
  5. **Removing FALLBOARD's gutter rests on a flat right-angle C-to-C cable** (a reversible plug exits either way). Products and socket orientation are UNVERIFIED. Residual: the old micro-B Xkey.
- **Randomness used** (Python `secrets`): Oblique "Repetition is a form of change" → tray and lid from repeated quarters, seams on lines the instrument already has (axis, lane), ribs on the module's 35 grid. Fields: "folding chairs" → FALLBOARD's over-centre brace stay. "Bicycle racks" → a quick-release cam for the end blocks, **not taken** (a thumbscrew is fewer notes).
- **Next:** visual's turn:
  - the module sheet (flush printed dividers, wordmark on the crown's rear face, no sentence, finger room, grille ≥ 620, facets in plan, and **the knob question drawn both ways if it helps the director**);
  - FALLBOARD at 412 × 265 with the keyboard at the front wall, and SPINE with the bead stop, in the same pack outline;
  - CLOTH in near-black, plus the ground pose;
  - no lamp; everything printed.
  - Then the director rules or calls READY, and **I do the 9+ coverage check** against rev 3.1.
- **Open:**
  - **Director:** knob Ø 10 × 8 vs Ø 14.9 (and the 22 pitch); FALLBOARD's keyboard at the front wall; SPINE's 30 mm lane staying, closed at 59, standing cut; CLOTH's offset outline.
  - **Visual:** the dividers' printed look; the corner weights' finish; how a split seam reads if the module can't print in one piece; the bed and lid colour now the bookcloth is gone.
  - **Eng:** module §11 (stack, knob, driver, grille, ported, weight, print bed, ¼"-20 heat-set, flat right-angle cable); FALLBOARD lid stiffness at a 0.8 skin, quarter joints, print time; SPINE knuckle strength at ≈ 95 N each.
  - **Owner (with the concepts):** sealed / ported; knob size and height; board, box or cloth; split-scoped HOLD; slim only or all; charger in the kit.

## Where things stand (2026-11-22 evening): jam closed; jobs rev 3 written; concepts round 2 started (my turn done)
- **Owner direction since the jam:**
  - **13:25** "The module does not have to match keyboard width" → S8 and layout D withdrawn; **one module in all three kits**, sized by its parts.
  - **13:29** "fit in a backpack comfortably … the size of a sheet of paper length wise … does not have to be a rectangle … a thoughtful ratio base" → T4 updated.
- **Director turn 6 + addendum:**
  - the one voice accepted; split-scoped HOLD → owner; REPEATS tie and voice pools 12 / 13 accepted;
  - coral on DEPTH with the shimmer group on the axis; brass frets; tab words low · main · high;
  - end blocks + one brass scale (carry parts, 404 in / ≈ 412 out); the pocket in every kit, no charger in the rigid kits (now revisited: pockets beside the narrower module take one);
  - one power switch; two lights; job 29;
  - must-shows per concept (turn 6 §4, amended).
- **`module-r2.md` landed (eng):**
  - sealed TEBM28C10-4B, ≥ 60–100 cm³ (≈ 62 × 75 × 27 inside); body 32, ≈ 40 at the rim; **passive radiator not recommended**; ported = more bass;
  - USB-C cold socket; **one C-to-A-receptacle adapter** in every kit;
  - BLOCK fits tight; **no kit with an Xkey meets T5**;
  - sockets can be anywhere on the rear edge or ends → gutter ≈ 35 for straight plugs, end-block notch ≥ 15;
  - cable 0.3–0.5 m;
  - lamp ≈ 50–100 mW (wired or AAA).
- **Written:**
  - `../jobs.md` **rev 3**: 30 jobs. **Changed:** 2, 3, 6, 9, 11, 14, 18, 19, 23, 26, 28. **New:** 29 (why silent), 30 (paper length, ratio, any shape). r2 facts folded in.
  - `../concepts/module/how-it-works.md`: the one module.
    - **Size:** **297 × 105, 2√2 : 1** (two A6 end to end; the axis splits it into two √2 halves, one per keyboard half). Letter 279 × 98.6 is the alternative but forces the speaker under a jamb.
    - **Speaker box on the axis** in the rear band under the wordmark; U-shaped board (eng to confirm).
    - **Two-row panel map with x coordinates.** ATTACK / RELEASE regrouped into voice, so the frets mirror: jamb | touch (HOLD / PRESSURE) | voice (ATTACK / RELEASE, TONE / DRIFT) | **shimmer on the axis (DEPTH coral / SHIMMER)** | echo (ECHO / TIME, TAP / FREE-SYNC) | out (VOLUME / REVERB) | jamb. 264 of controls; frets at 54 / 83 / 134 / 163 / 214 / 243.
    - Also: front face (target rail with the engraved line, host port, port light), rear wall, ¼"-20 inserts at x 68.5 / 228.5, the voice table, lights, states, S1–S7, coverage.
  - `../concepts/fallboard/how-it-works.md`: 412 × 288 tray; bed 140; **gutter 35**; module centred in the rear band with **charger and spare pockets** either side (option B, a stepped tray, shown); lid on lift-off hinges + stay; self-powered AAA lamp; closed 48; kit 1.45–2.27 kg (**T5 only with the nanoKEY2 at the light end**).
  - `../concepts/spine/how-it-works.md`: **reworked as a clamshell (solander) box**: two trays of the same outline (412 × 143), shallow keyboard tray + deep module tray, a stop-at-flat spine whose open gap is the cable gutter; closed 61; kit 1.25–1.97; one fit trial for the spine.
  - `../concepts/cloth/how-it-works.md`: 800 quilted furoshiki, a stitched outline 412 × 288, a washable module sleeve, a pocket (cable, adapter, charger), curtain-weight corners; packed with the module at the bottom panel-up and the keyboard keys-down on the sleeve; bench kit (on a lap it's two objects); lightest kit, 1.17–1.92.
  - All three cover every job; **at risk: T5** (all, with an Xkey); SPINE's spine trial; CLOTH's lap and impact protection (weak, inferred).
- **Decisions and why:**
  - the line "keep the keyboard at its home octave" is **engraved on the module** next to the target, so no kit needs its own place;
  - the lamp is self-powered, keeping the module identical across kits;
  - the gutter is deepened to 35 so no keyboard needs a particular right-angle cable;
  - 297 over 279 because the speaker needs a 57-deep column on the axis.
- **Old round-1 folders (bow, kept, tide) and common-*.md are kept as history.**
- **Next:** visual draws the module (ratio and outline jointly with me) and the three kits per the must-shows; the director scores; then my 9+ coverage check against `jobs.md` rev 3.
- **Open:**
  - **Visual (joint):** the 2√2 ratio and outline (speaker crown option); knob sizes in the rear row; separating and marking the two USB-C sockets.
  - **Director:** TAP's ring carrying status + tempo, or a separate dot.
  - **Eng:** U-shaped board around the axis box; insert bosses; voice pools; whether a ported box fits the axis band.
  - **Owner (with the concepts):** board, book or cloth; split-scoped HOLD; charger in the kit; slim only or all; **the r2 trade-offs** (sealed / ported / radiator dropped; body 32 / 40; T5 missed with an Xkey; cold socket).

## Where things stand (2026-11-22 late): module jam pass 2, my turn 4 done
- **Jam so far:**
  - turn 1: me;
  - turn 2: visual (FALLBOARD; RAIL / SLAB / BLOCK; S8 = 400 wide; brass target; kills LAMP and TETHER);
  - turn 3: director;
  - turn 4: me.
- **Director turn 3 rulings:**
  - **one floss voice in every kit**, so concepts differ only on the kit (no pairings);
  - **FALLBOARD (lead), SPINE and CLOTH** go forward; LAMP, TETHER and BACKBONE are killed (LAMP's light goes into the lid, TETHER's strap becomes an S4 accessory);
  - S8 goes to the owner as a proposal;
  - split = rule A + brass target (B rejected);
  - two lights; **one power switch on the module** (SPINE open = on dropped);
  - job 29 added;
  - the grouped row: octave | touch | voice | shimmer | room | out | octave, with HOLD in touch;
  - padded **end blocks** (nothing crosses a key) and an **accessory pocket** in every kit;
  - **assume the published-data speaker path** (32–38 mm body). That's with eng, who is writing `floss/eng/module-r2.md` (USB-C host, RAIL / SLAB / BLOCK fit, kit weights).
- **My turn 4 (in `../jam-module.md`):**
  - **The one voice:**
    - velocity = speed; release velocity → tail (RELEASE up to ≈ 30 s);
    - strands per half (low · main · high);
    - DRIFT knob;
    - lean **swell · drift · tone · shimmer**, where a full lean on drift speeds it up into vibrato (≈ 0.3 → 5–6 Hz, PROPOSAL);
    - the lean ladder;
    - **plant-and-tend HOLD that survives the keyboard, with its scope following the split** (octaves equal = everything; different = left half only; owner to confirm);
    - CC64 = sustain;
    - **REPEATS cut** (tied to ECHO).
  - **Count:** 13 round (4 stepped + 9 pots) + HOLD, TAP, FREE / SYNC + 6 tabs + 2 lights.
  - **Engine catch:** allocated voices break the 6-line strand gating, so I proposed **fixed voice pools, 12 left / 13 right** (eng to confirm).
  - **RAIL fit [calc]:**
    - the full voice in one row doesn't fit 400 (396 needed at pitch 20 vs 384 usable; 428 at 22);
    - **recommended layout D:** a front row of amounts + a back line of three kinds (PRESSURE behind ATTACK / RELEASE, SHIMMER behind DEPTH, FREE / SYNC behind TIME) on a rail ≈ 400–412 × 95. It needs 372 at pitch 22.
  - **End blocks:** 8 mm fully in, 32 mm travel each, ≈ 40 out; bed inside 404; **kit ≈ 412**. So S8 at 400 doesn't hold real blocks; proposed ≈ 412 ("about an inch over the widest keyboard"). Also: centring by a shared scale (same graduation as the target rail); a lid foam strip holds the keyboard when packed.
  - **Pocket:** the gutter (FALLBOARD), the spine plus a cover sleeve (SPINE), the sewn pocket (CLOTH). Rigid kits carry cables, not a charger.
  - **`jobs.md` rev 3 changes: 14 proposed** (the six held + director's). Not written yet: write them when the jam closes.
- **[spk] speaker-dependent:** RAIL's speaker volume (≈ 300–400 cm³ at a 32–38 mm body: helps), FALLBOARD closed ≈ 43–45, SPINE closed ≈ 60.
- **Next:** visual redraws the kits; the director steers; then jobs rev 3 and the concepts. In the concepts I write how each kit works around the one voice (a common how-it-works for the voice and panel, plus a kit file each).
- **Open:**
  - **Director:** D vs SLAB everywhere; S8 at 412; self-centring linkage vs scale; REPEATS tie.
  - **Owner:** split-scoped HOLD; S8 ≈ 412; charger in the kit.
  - **Eng:** voice pools; body depth; weights at 412; lamp power; coiled-cable products.

## Where things stand (2026-11-22 evening): module jam, turn 1 done (new systems seat)
- **New seat:** a new agent took over the systems seat from here. The notes below this section are history, not commandment.
- **Owner direction since the notes below:**
  - 12:52: the host port is **USB-C**, and proportions are open ("we can riff on the dimension ratios"). T4's 290 mm isn't a hard cap while we explore.
  - 12:28–12:30: the family principle; Big Energy changes too (later); **no hybrid** (no built-in buttons).
  - KEPT is dead (director, round 1).
- **Wrote `../jam-module.md`, turn 1.** It covers:
  - challenges to `jobs.md` rev 2;
  - the system's structure and the family standard (S1–S7);
  - flows (unpack, keyboard missing, swap, friend, home);
  - the panel principle and its new parts;
  - four kit directions plus one proposed kill.
- **Next:** the visual designer's turn, then the director steers. After the jam: `jobs.md` rev 3 (changes listed below), then concepts.
- **Didn't touch:** `jobs.md` (changes held for rev 3), `concepts/`, git.

### Randomness drawn (module jam turn 1, Python `secrets`)
- Oblique Strategies: "Look at the order in which you do things" (43/50); "Only one element of each kind" (4/50).
- Field: bookbinding (16/30), drawn **twice**. Kept it, then drew a third: tea ceremony utensil kits (10/29).
- Twist: "it is mostly used at night" (2/12).
- Constraint: "the cable is the handle" (10/10).
- Proportion: 3 : 1.

### Decisions and proposals so far, and why
- **floss = "a mind with a sound that borrows hands."** The panel can face anywhere now; the join (cable, carry, attachment) is itself a product; every behaviour needs a "keyboard can't" answer.
- **Family standard: fix interfaces, not sizes** (the camera tripod thread, not the shipping container). Modules differ in size, and a fixed box recreates the director's "leftover space" problem. PROPOSAL S1–S7:
  - S1: keyboard envelope ≤ 392 × 139 × 18, ≤ 0.6 kg (eng);
  - S2: USB-C host, 5 V ≈ 550–600 mA, **on the keyboard-facing edge, never the rear**;
  - S3: cable owned by the keyboard (right-angle C at the module end, coiled ≈ 0.3 m relaxed to 1 m stretched);
  - S4: **two ¼"-20 brass inserts underneath at one family spacing** (spacing not set yet); every carry part attaches there, and it mounts on tripods;
  - S5: any plug order works; unplugging releases notes on their tails; **held notes survive an unplug**; the port light; the keyboard is powered only while the module is on;
  - S6: a family CC map (CC64 hold, CC1 lean fallback, CC74 tone, CC11 expression, bend ±2);
  - S7: one split rule.
- **Panel principle:** it holds what turns notes into floss, and nothing a keyboard already has ("one element of each kind" used as a test). The round-1 panel survives; signal order is unchanged, with the ensemble after the voice (director's BOW fix 1).
- **Split rule:** PROPOSAL **A (fixed B3 | C4) + C (a bookbinding ribbon laid across the keyboard at the split)**. B (learned per keyboard by USB ID, set by HOLD + key) is offered but hides state.
- **Port light** next to the host port: off / steady connected / blinks on each note received / fast flash = power fault. The status light keeps its three meanings. "One of each kind" argues against a second light; the director rules.
- **Lean fallback chain:** poly AT/MPE → channel pressure → CC1 → nothing. It's automatic, the panel is unchanged, and it gives velocity-only players the selector through their mod control (job 9).
- **BOW's per-note thinning** runs only when per-note pressure is arriving.
- **Two axes:** kit (SPINE / CLOTH / LAMP / TETHER) × voice life (BOW / TIDE). Proposal: concepts differ on the kit, each paired with one voice (SPINE + BOW, CLOTH + TIDE, LAMP + TIDE or a quiet BOW, TETHER + BOW).
- **The kits:**
  - **SPINE** (book): a 390 × 130 module plus a keyboard board with sliding elastic corners, joined by a cloth spine ≈ 55 mm wide that folds both ways: open flat / standing ≈ 110° / closed face to face (≈ 2 mm knob clearance on a 16 mm keyboard [calc]). The cable runs in the spine. Misses T4; weight is at T5's edge.
  - **CLOTH** (tea kit): a 270 × 90 module plus a quilted furoshiki ≈ 80 cm with a module sleeve and a cable pocket; the cloth is the lap mat, and the unpack is a ritual. The only kit that carries the chunky minis. Weak on impact protection, dirt, and two loose objects.
  - **LAMP** (night): a 270 × 90-face wedge standing behind the keyboard, with a lip for any depth; a warm LED strip lights the keys in two zones that show the split. Weak on the lap and the carry; it's a night object.
  - **TETHER** (cable is the handle): a strap with the keyboard cable inside it, anchored to S4, with slack pigtails; play standing or walking. Weak on protection and job 18, and the strap is a custom part.
  - **BACKBONE** (a clamp-on bar): proposed kill (no protection, near a fitted dock, risks the keyboard).

### jobs.md rev 3 changes held (fold in after the jam)
1. Job 2: USB-C host port.
2. Jobs 3 / 28: the carry works with no keyboard in it.
3. Job 3: chunky minis play but aren't carried unless the owner says "all".
4. Job 6: keyboards differ in their default lowest note (eng to list them).
5. Job 23: the cable-length conflict (solo vs friend).
6. **New job 29 (inferred):** find out from floss why there's no sound.

### Open questions (new)
1. **Eng:**
   - `module.md` §3 still says USB-A: revise for USB-C;
   - each slim keyboard's default lowest note, and its socket position and type;
   - a full-size keyboard's draw;
   - phone as host;
   - over-current retry;
   - lamp power vs T2;
   - SPINE's lap mass;
   - the S4 insert spacing.
2. **Director:**
   - which kits go forward;
   - the BACKBONE kill;
   - two axes;
   - one light or two;
   - split A + ribbon vs B;
   - SPINE open = on (it needs a second switch for use without the board).
3. **Owner:**
   - slim only vs all;
   - one package vs two;
   - job 29.

---

## Where things stand (2026-11-22 afternoon): floss is now a keyless sound module
- **Owner 12:26:** floss has no built-in keys. A travel USB MIDI controller (K-Board C, Xkey 25, or any class-compliant keyboard) plugs into floss's USB host port, is powered by floss, and is carried with it.
- **Process changed** (owner 09:2x): requirements (`floss/REQUIREMENTS.md` rev 2, T1–T12 baseline), then an engineering gate, then concepts. Adam measures nothing; choices rest on published evidence; SMD is allowed.
- **`../jobs.md` is rev 2:** 27 jobs, a short paste-ready list at the top with new / changed marks, a rev 1 → rev 2 change table, a detail table, flows F1–F16, and open questions.
  - **New jobs:** plug in with one cable (2), carry as a kit (3), controller octave buttons vs the split (6), expressive without pressure (9), play from a computer or another keyboard (16), swap controllers (27).
  - **Changed:** voices allocated (4), split and octaves on floss (5), pressure per note only when the controller sends it (8), tilt / bend / lift where available (10), "keyboard connected" as state (18), duet = one plays, one tends (23).
- **Owner addition:** "This is the plan for all modular portable synths that we build — portable sound modules with a way to carry a keyboard with it. It should be flexible and not reliant on a single model of keyboard."
  - Jobs 2, 3 and 27 now say "any travel keyboard in a size range, not one model". No recess cut to one outline; adjustable carry beats exact.
  - **New job 28:** one carry-and-connect system for every synths-to-go module (a family standard Big Energy and port-a-poly can reuse).
  - **Eng to set:** the size and weight range (my placeholder, up to ≈ 390 × 140 × 25 mm and ≈ 0.7 kg, is unverified until the Xkey 25's published size is checked), and the host port's power budget.
- **Concepts are on hold.** The director re-steers after the engineering baseline. **Don't edit `../concepts/` until then.**
- **What survives from the concepts, as I see it (for the re-steer):**
  - the breath, octave knobs as the split, the PRESSURE selector, HOLD, FREE / SYNC, the status light, the TOUCH → … → VOLUME order;
  - TIDE's add-and-pull HOLD and per-voice DRIFT;
  - KEPT's Solina registers.
- **What doesn't survive:**
  - anything about keys (Choc / Hall lift timing, pegs, key colours, the centre-gutter-over-middle-C argument, which assumed physical keys under the panel);
  - BOW's lid = power (it's still possible, but the "covers the keys" reason is gone);
  - BOW's per-key thinning in swell, which only works with per-note pressure. With a velocity-only controller it would just sink every note, so it needs a rule.
- **Eng facts used** (`floss/eng/controller.md` rev 0):
  - the K-Board C is 325 × 84 × 11 mm, ≈ 0.35 kg, poly AT / MPE / tilt, $139, KMI-branded only until stock sells out;
  - libDaisy supports USB host MIDI; host and device at the same time is unverified;
  - the engine becomes 25 allocated voices on the same hardware (a 12-voice option saves ≈ $12–15);
  - the controller's octave buttons move the split;
  - only the Seaboard sends lift;
  - the controller draws ≈ 0.25–0.5 W.

## Where things stand (2026-11-22, concept round 1: my turn done)
- Written:
  - `../concepts/common-how-it-works.md` (shared engine and behaviours, panel grammar, common coverage);
  - `../concepts/bow/how-it-works.md`, `../concepts/kept/how-it-works.md` and `../concepts/tide/how-it-works.md` (structure, panel map, engine departures, flows, states, coverage, risks).
- The owner hasn't answered on `jobs.md` yet; fold his answer in when it comes.
- **Settled in common (they were my open items):**
  - all tabs off = that half silent (a feature: mute a half);
  - echo sync = the family's FREE / SYNC toggle (Big Energy owner option B);
  - a rear TUNE trim, ±50 cents;
  - "knob not in control" = no indicator (jump-on-move is audible; the light keeps three meanings);
  - MIDI SPLIT is a rear slide switch;
  - MIDI CC 64 holds every note;
  - note-off velocity carries lift;
  - octave knobs are 5-position (−2 … +2), with 0 / 0 = C3–C5 and middle C in the centre.
- **Per-concept decisions:**
  - **BOW:**
    - strands made the 1974 way: 2f per key → a CD4520 counter per key (13 DIPs), plus 75 CD4066 gates (≈ 19 DIPs); a CPLD is the alternative (owner question, J21);
    - velocity = speed only;
    - in swell, a held note thins to −6 dB over 4 s without pressure (off with HOLD and on the shared strip);
    - lid = power (Hall at the hinge), plus a rear ship-mode cutoff;
    - three-deep strand column fits (mini rockers turned 10 deep, y 55–89, x 117–132 / 154–169);
    - left of the gutter = the instrument, right = the room.
  - **KEPT:**
    - **reshaped: velocity = loudness** (the director's "crescendo per note" would have made it identical to BOW's speed);
    - no TONE knob;
    - tabs: bass (left bus only), strings, brass;
    - label "ensemble";
    - pressure default vibrato;
    - two rows on ONE SHEET.
  - **TIDE:**
    - per-key drift on the DRIFT knob (±25 c, PROPOSAL);
    - velocity inverted (soft = longest and most wandering);
    - pressure positions drift · swell · tone · shimmer, with drift remembered when held;
    - **HOLD on the whole keyboard adds notes, and re-striking a held note pulls it out;**
    - the centre widens to about 28 mm for DRIFT, and TAP moves to the echo group.
- **Kills proposed:** none. All three differ in kind: velocity meaning (speed / loudness / lifespan), registers (strands / Solina tabs / none), HOLD (replace left / replace left / add-and-pull, everything), body (CATHEDRAL / ONE SHEET / HUSH).
- **Weak spots I flagged honestly:**
  - BOW: J21 (chip count) and J15 (lap tipping);
  - KEPT: J18 (shared colour) and the sleeve;
  - TIDE: J7 (no registers) and J13 (which notes are held is invisible).

## Where things stand (2026-11-22, jam closed; jobs.md rev 1 written)
- **The jam closed after six turns.** Turn 5 (director) killed WIND, put TIDE forward on a condition (velocity and pressure must matter in TIDE), and named the SWELL word clash. Turn 6 (visual) gave the faces:
  - BOW = CATHEDRAL with the lid as soundbox, dark naturals, coral pressure selector;
  - KEPT = ONE SHEET, white and black keys, coral ensemble;
  - TIDE = HUSH, a felt pebble with maple pegs, coral DRIFT on the axis, the lantern.
  - Off-centre split: a one-key gutter over middle C carrying the shared controls, plus a coral rim tick at B|C (director to rule).
  - Words: attack / release knobs; pressure swell · vibrato · tone · shimmer; strands low · main · high; octave numbers −1 · 0 · +1 · +2; KEPT tabs bass · strings · brass.
- **`../jobs.md` rev 1** opens with a short owner-facing list of 21 jobs, then a detail table (J1–J21 with concept requirements) and flows F1–F15. It goes to the owner as "anything wrong or missing?".
- **Next: concepts**, with me going first: how each of BOW, KEPT and TIDE works (structure, flows, states).
- Things to settle in the concepts:
  - what "all tabs off" does;
  - how echo sync is turned off;
  - a tuning trim (J17);
  - where "knob not in control" shows;
  - whether BOW's three-deep strand column fits CATHEDRAL's base depth (visual's question to me).
- Read: `BRIEF-CONTEXT.md`, `floss/README.md`, `design/owner.md` from 2026-11-21 on, `design/concepts/common-how-it-works.md`, and skims of `design/jobs.md` and `eng/budget-variant.md` (keys, velocity, aftertouch).

## Randomness drawn
- Turn 1 (mine): "Work at a different speed", "Do the washing up"; bell ringing; "designed for two players".
- Visual turn 2: "Use an old idea", "Go slowly all the way round the outside"; lighthouse, kite; child's hands; coral.
- Director turn 3: "Give way to your worst impulse"; pipe organ; eyes closed.

## Facts checked
- Ensemble: three modulated delay paths, two LFOs (≈ 1 Hz, ≈ 6 Hz), phases 0 / 120 / 240° (Sound on Sound, "More creative synthesis with delays"). Closes the director's check; the lantern can follow three phases.
- Director checked (Zoë Blade's Solina guide): the Solina's contrabass and cello sounded only on the low region (C2–G3); its crescendo and sustain sliders set attack and release.

## Decisions so far and why
- **Engine: structure B** (one tone per key from an MCU, a VCA and firmware envelope per key, then the shared filter, ensemble and FX). Agreed by the whole team. It's the only structure that gives per-note velocity and pressure with every key sounding.
- **Per-note articulation, no new controls:** strike → attack time (inside SWELL's range); lean → the pressure destination; lift speed → tail (inside RELEASE's range). Lift timing is firmware only; the fast end is limited by the Choc V2's spring return (eng to test).
- **The split = two OCTAVE knobs**, no mode. Pointers parallel = continuous (visual's reading, endorsed by the director). Fixed split B|C. A held note keeps its pitch across an octave change.
- **Per-half controls sit over their half** (visual; the director made it a rule).
- **MIDI split ON/OFF on the rear wall.**
- **Signal order on the panel:** TOUCH (SWELL, RELEASE, PRESSURE selector) → strands / registers → TONE → SHIMMER → ECHO → REVERB → VOLUME.
- **PRESSURE positions:** SWELL, VIBRATO (per note), TONE, SHIMMER (global, following the max pressure). On a shared-strip fallback, SWELL behaves as FILL (whole-instrument swell), with the same label.
- **Breath (from WIND), fixed in every concept:** the sum grows roughly with √(keys down), recovering over ≈ 200 ms; no pitch sag; no control. This answers J15.
- **HOLD** (was SET): a latching toggle; a new chord after all keys are up replaces the old one; off releases with tails. No armed state. Scope per concept: BOW left half, TIDE everything, KEPT left half.
- **Registers differ per concept:**
  - BOW: strands of pitch (−8va, unison, +8va, sine-rounded); 6 tabs (3 per half), names printed once between the rows.
  - KEPT: the Solina way (shared timbre tabs plus a low register on the left half only).
  - TIDE: none, just TONE.
- **The honest "analog voices" sentence** is in jam turn 4 §8.

## My kills and proposals in pass 2
- **Killed WIND as a concept:** same hardware as BOW, so it would only be a firmware switch. It survives as the fixed breath and as FILL.
- **Killed the swell-box lid.**
- **Proposed TIDE** for the third slot ("life lives in time": per-key drift on a DRIFT knob, HOLD for everything, long lift-set tails). Its risk: it overlaps with the Daisy reverb and shimmer modes, so it has to stay analog-first.
- **Dropped the fifth strand.**
- **24 keys:** shown as an owner-visible option that centres the split (7 + 7 whites), not recommended. The 25-key split sits 9 mm left of centre.

## Director's objections and how I answered them
- "One concept, four names": answered by giving the registers, HOLD scope and engine emphasis a different answer per concept, and by proposing TIDE.
- Analog honesty: answered with the sentence.
- Jargon: SET → HOLD; BRIGHT → TONE. Strand labels are still to be named in plain words (visual).
- Off-centre: offered the 24-key option; my preference is that the axis follows the split (visual's call).
- BOW/WIND as one instrument: argued yes, and killed WIND.

## Open questions
1. Eng: 25 per-key VCAs (cost, battery, board); 75 tone outputs for strands; lift timing at the spring's return; the BBD part; per-key pressure past the bottom (FSR per key? a felt collar?), keeping the shared-strip fallback.
2. Director: TIDE or keep WIND in the third slot?
3. Owner later: is the fixed breath OK? Velocity as speed only? Fixed centre split OK? 24 vs 25 keys?
4. TUNE trim on the rear, or none?
5. Status light: the director cut it to three meanings. Where does "knob not in control" go, if anywhere? (Big Energy's J8 needed it.)

## Next
- Fold the owner's answer on the jobs list into `jobs.md` rev 2.
- Concepts: write how-it-works for BOW, KEPT and TIDE in `../concepts/<name>/`, starting with the shared rules (the split, the half-map, the TOUCH group, the breath, lift, the status light), then check each against `jobs.md`.
