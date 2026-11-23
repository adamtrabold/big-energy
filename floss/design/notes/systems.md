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

---

## 2026-11-22 18:xx: CATHEDRAL form round, jam turn 1 (systems)
**Where things stand:** the owner turned down the module (280 × 105 × 35 hull) and YOKE on shape (15:15) and pointed at Big Energy's CATHEDRAL as the model for cues (17:58). This round is the module's **form** and how the keyboard comes along, concept level only. I opened `jam-cathedral.md` (turn 1) and moved `jobs.md` to **rev 4**.

**jobs.md rev 4:** changed 3 (keyboard not necessarily attached), 20 (at an angle), 24 (CATHEDRAL cues, keyboard no longer part of the object), 25 (family answer), 26 (fully printed incl. metal), 30 (dimensions free); new 31 (one plane), 32 (at an angle; shape-only is a possibility; flat too? open), 33 inferred (panel protected), 34 inferred (ports in every pose). Detail rows for 3/24/26/30 still describe rev 3.2's concepts; the short list and rev 4 table win. Detail rows for 31–34 not written yet: write them once a direction is picked.

**Randomness drawn:** "Mechanicalize something idiosyncratic", "Remove specifics and convert to ambiguities"; loom, reliquary/triptych, cast-iron skillet; twist "made of identical repeated parts"; angle 14°.

**Key finding [calc]:** angle by shape alone gives robust *angled* or *angled + upright* poses, not *flat + angled*. A two-facet bottom that rests both ways needs the COM inside a ≈ 4–5 mm window: a knife edge. So flat-and-angled needs one moving part or a second object. That's the owner's fork (open question 1).
**Second finding [calc]:** a 14° wedge over 105 deep (35 → ≈ 61 mm) adds ≈ 385 cm³, twice speaker E's ≈ 190 cm³. In a wedge the angle can be the speaker box and the plan may shrink. For eng.

**Directions proposed (differ in kind):** WEDGE (fixed section; owner's shape-only idea), TRIPTYCH (cover is the stand; owner's folding-cover idea), BAIL (printed-metal handle = stay = keyboard anchor), SLED (angle lives in the keyboard carrier; module flat), RETABLE (stands steep like a radio). Cross-cutting: NAVE (identical printed bays: fits the bed, seams at dividers, family scales by bay count). Keyboard carry kinds k1 strap, k2 back-to-back on S4, k3 on the cover, k4 carrier.

**Structurally meaningful CATHEDRAL cues:** the framed plate (rim guards knobs), the raised panel (angle without the hinge), the stay (now printed metal), soft architectural corners, pipe-line grille as speaker-box bars, bays. Not carried: bookcloth spine, the two-part fold.

**Open questions:** flat too, or angled enough (owner); is a strap "stuff" (owner); printed-metal service/cost, wedge volume, detent wear (eng); the two-facet idea worth chasing (director); which cue carries the look (visual).

**Next:** visual designer's jam turn, then the director's steer; then concepts in `concepts/c-<name>/`, and detail rows for jobs 31–34.

### 2026-11-22 pass 2 (jam turn 4, systems)
**Director's turn 3 rulings:** survivors CASKET (TRIPTYCH as a one-line hinged variant), GNOMON (constant slab, rim continues into wedge cheeks, open underneath), DROP (teardrop/pipe; pose 2 cut). Dead: ROSE, BAIL, SLED, RETABLE, plain WEDGE. NAVE = a making method only. Rules: angle from the parts; end face first; every volume and surface has one job.

**What I derived [calc]:**
- **DROP:** pipe Ø 56 inside / ≈ 62 outside (driver chord + 27 mm depth). Length ≈ 260 = cell bay 65 + box 120 (≈ 250 net, eng's E2) + cell bay 65; port Ø 16 × 140 through the left cell bay to the left end face's centre. Lip ≈ 26.5 (r3 stack minus the cell layer). θ from the lip, the pipe and the plate rows: 2 rows → ≈ 37°, 260 × 88 × 62; 3 rows → ≈ 27°, 107 deep. Stable (a top-row press tips it only above ≈ 26 N). Jacks on the right end; host port on the lip.
- **GNOMON:** rule sin θ = T / D → 17.7–19.5°. Stable under the hand and knob presses; grass ≈ 3.8 kPa on the runners; best lap answer (runners one per thigh). Port through the left cheek (the hollow would choke on a lap or grass). Host port on the leaning front face needs the right-angle cable (a straight plug clears by ≈ 6.6). Jacks on the raised rear face. Hollow = cable bay, closed by the docked keyboard.
- **CASKET:** a flip-over tray can't seat the module (D_lid > D; an inside ridge hits the knobs). **A:** a wedge lid (8 → 43 walls) as a plinth, same rule ≈ 18–19.5°, but closed it's a wedge 43 → 78. **B:** a shallow lid (≈ 15) slid under the back, caught by a step on the module, ≈ 11°; closed it's a calm ≈ 50 slab. Moves: 5 vs 3 for GNOMON/DROP.
- **Keyboard:** ends and long-edge holds must reach past a 260–280 module for 325–388 × 83–135 keyboards; a band crosses the keys. **Proposal: SHOE (family S9)**, a printed plate on removable pads under any keyboard, sliding into a dovetail under each module, back to back, keys out. Fallbacks: loose in the bag (always works); a printed TPU band (printed, so no owner exception). The keyboard-length lid was rejected (dressed surface, CASKET only).

**Owner questions:** flat too; strap; cast-from-printed-wax metal; long-edge/underside hold; **new:** pads stuck under his keyboard (SHOE).
**Brass:** brass runners alone slide on a smooth table, so TPU strips do the gripping; brass only where it doesn't need grip.
**jobs.md changes queued (after the owner answers):** job 3 "ends or underside"; S9; detail row for job 32 (the angle rule).
**Next:** the director steers on DROP's rows, CASKET A/B and the angle rule; then the visual designer draws the end faces.

### 2026-11-22 concept building, turn 1 (systems)
**Director turn 5:** DROP 2 rows ≈ 37°, 260 × 88 × 62; CASKET-B ≈ 11°, closes as a calm slab (A dead; TRIPTYCH one line); GNOMON sin θ = T/D accepted (back ≈ 70 = 2T); SHOE accepted as the shared carry pending the owner (conditions: pads only on a free flat underside; a positive detent; one family part S9; the keyboard plays with the shoe on, no rocking); fallbacks loose → printed TPU band; façade only where seen (CASKET lid yes; GNOMON underside no; DROP none).
**Wrote:** `concepts/c-drop/how-it-works.md`, `c-gnomon/how-it-works.md`, `c-casket/how-it-works.md`, `concepts/c-shoe.md` (≈ a page each: structure, poses, moves, ports/speaker, owner forks, UNVERIFIED).
**Decisions in them (proposals):**
- **S9 dock slides front to back on every module**, entered from the front edge, y ≈ 10–70, with a detent at the end.
- **CASKET-B catch groove** across the base at y ≈ 80–92: 10 mm clear of the dock. Both are recesses, so the flat pose stays flat. The lid lies behind the groove and shows ≈ 75–80 mm behind the module's back while angled (footprint ≈ 190), flagged as the shape risk.
- **GNOMON gets a stretcher** (a bar between the cheeks at table level) **only if SHOE is chosen**: the 200 plate can't span the 280 runners. It also stiffens the cheeks and floors the cable bay. Needs the director's OK (it changes "open underneath").
- **Family port rule:** the port mouth is at the centre of the left end grain (DROP's end face, GNOMON's cheek, CASKET's end face).
- **SHOE rocking:** plate plus pads ≈ 5–6 mm vs the keyboard's own feet (UNVERIFIED per model); if taller, peel the plate off to play, or carry loose.
**Open:** the stretcher (director); the groove's exact y (eng, centre of mass); pad hold, dovetail tolerances, foot heights (eng); the CASKET lid-pocket fit.
**Next:** the visual designer's sheets; then my coverage check of each 9+ concept against `jobs.md` rev 4 (jobs 31–34 need detail rows first).

### 2026-11-22 round 1 scored; GNOMON rev 2 (systems)
**Scores:** GNOMON 8, CASKET-B 7, DROP 6 (killed: loaf / hair dryer). **Owner 18:39:** "Honestly my preference order would be angled, 90, flat"; **18:40:** "Multiple angles is fine". CASKET-B retires (flat isn't wanted). **Director fix 6:** GNOMON's rear face square to the plate, so it stands upright by shape; jacks move to the right cheek.
**c-gnomon rev 2 [calc, mass 0.8 kg and COM ESTIMATES]:**
- The cheek is front T, plate D, rear 2T, all square to the plate. **The angle rule restated: tan θ = T / D** → 18.4° / 16.9° (sin rule would need a 72 mm rear face). For the director to accept.
- Angled footprint 111 / 120 (+11–12, not +23); back ≈ 66–67.
- **Upright on 280 × 70:** the COM is only ≈ 15–20 mm inside the plate-side edge. **A pull toward the player on the top edge tips it at ≈ 1.0–1.5 N** (it lands on the rim); a top-row press tips it back at ≈ 4–4.6 N, a lower row at ≈ 5.5 N; ground tilt forward ≈ 17–22°. A wider rear face helps presses only; forward pull improves only by moving mass away from the plate (≈ 0.07 N per mm). So upright is for standing, listening, a shelf, a friend, light turns, not hard playing.
- Ports in both poses: speaker best upright; port mouth on the left cheek in the slab band; host port on the front face (right-angle cable angled; from the top upright); jacks on the right cheek (UNVERIFIED above the end cell).
- **Stretcher** still works: on the runner line, ≈ 30 mm clear of the rear face. Undock before standing upright.
- Flat: not offered and not faked.
**jobs.md:** a "Queued for rev 5" table added (job 32 poses in his order; 34 ports per pose; 3 and S9 pending the owner; 30 the tan rule). Not applied yet.
**Owner questions:** "90" for playing or standing; "multiple angles" as fixed poses or a range.
**Next:** the visual designer's sheet with the upright view; the director re-scores GNOMON; I do the coverage check against jobs once it's 9+.

### 2026-11-22 GNOMON 9: coverage check and jobs rev 5 (systems)
**Director:** GNOMON rev 2 = 9; tan θ = T/D accepted. Handoff conditions: (a) host port low on a cheek near the rear-bottom corner; (b) mass low and away from the plate; (c) jack row UNVERIFIED; (d) undock before upright.
**Coverage** (`concepts/c-gnomon/coverage.md`): **all 34 jobs supported, none unsupported.** 11 have stated weaknesses: 3 (SHOE's underside hold pending the owner), 6 (target rail under the r16 lip), 18/29 (condition a would move the port light out of sight, so keep it on the plate), 24 (wedge), 26 (repair access not drawn), 28 (stretcher only on GNOMON; S9 pending), 31 (power / TUNE / SPLIT on the cheek: owner clarification), 32 (upright tips at ≈ 1–1.5 N), 33 (rim 1 mm over the knobs), 34 (host-port cable vs the upright pose → condition a).
**jobs.md rev 5 applied:** 32 (poses in his order, verbatim 18:39 / 18:40), 34 (ports per pose; a foot carries nothing), 30 (tan θ = T/D), and detail rows for 31–34. Job 3's "or its underside" and S9 stay pending.
**New owner question:** does "all controls in one plane" include the set-and-forget controls (power, TUNE, MIDI SPLIT)?
**Next:** GNOMON goes to the owner. Once he approves, I write the "How it works" part of the handoff, applying handoff items 1–6 from the coverage file.

### 2026-11-22 GNOMON rev 3: the owner's change (systems)
**Owner, verbatim:** "Reverse the angle on the side behind the speakers so there’s still a subtle angle when upright".
**My reading (stated plainly in how-it-works):** the rear face tips the other way from square, so the corner behind the speakers closes below 90° and upright the plate leans back. The literal mirror (rear face leaning out 18.4° in the angled view) gives a 37° upright lean, and a vertical rear face gives ≈ 18°: neither is subtle, so his goal decides. Flagged.
**Geometry [calc]:**
- Angled θ unchanged (tan θ = T/D ≈ 18.4° / 16.9°).
- **Upright lean tan φ = T/2D ≈ 9.5° / 8.7°** (half the angled slope); corner ≈ 80.5°.
- Rear face ≈ 67.2 / 67.7 (≈ 1.9T, no longer 2T; keeping 2T would push θ to 20.0°).
- Angled footprint 99 / 110 (down from 111 / 120); back still ≈ 66–67; upright top edge ≈ 104 / 114.
- **Upright forward pull 1.27 → 1.89 N (+49 %)**; presses 4.6 → 4.1 (top row), 5.6 → 5.3 (lower row); forward tilt tolerance 19° → 28°.
- Stretcher ≈ 19 mm clear of the rear face.
**Updated:** c-gnomon/how-it-works.md rev 3; coverage.md (jobs 30, 32; verdicts unchanged); jobs.md row 30 detail.
**Director's calls:** tan φ = T/2D as the derivation; losing exact 2T on the rear face.
**Next:** the visual designer redraws the end view, the upright view and the two-poses view; the director re-scores.

### 2026-11-22 GNOMON rev 4: back square to the base (systems)
**Owner, verbatim:** "I don’t like the angle on the back when laying flat. Make the base and the back 90 degrees when sitting flat". Read as: in the playing pose (on the runners) the back is vertical.
**Geometry [calc]:**
- θ unchanged (tan θ = T/D ≈ 18.4° / 16.9°); the corner behind the speakers is 90° − θ ≈ 71.6°.
- **Upright lean = θ ≈ 18.4°** (rev 3's tan φ = T/2D is dropped; one angle, two poses).
- Rear face = back height ≈ 66.4 / 67.0.
- Playing footprint 88.5 / 99.8 (rev 3: 99 / 110); overall ≈ 100 / 110 × 66.
- Upright top edge ≈ 100 / 110.
- **Upright:** pull 2.52 N (rev 3: 1.89; rev 2: 1.27); presses 3.9 (top row) / 5.1 (lower row); tip angles ≈ 37° forward / 39° back, balanced. Grass ≈ 4.4 kPa angled.
- **Stretcher moved forward to y ≈ 15–75** (≈ 13.5 mm clear of the back at D 105; at y 20–80 it would be 8.5).
**Updated:** c-gnomon/how-it-works.md rev 4; coverage.md (jobs 30, 32; verdicts unchanged); jobs.md row 30 detail.
**Next:** the visual designer redraws the end view, the upright view and the two-poses view; the director re-scores.

### 2026-11-22 GNOMON rev 5 rounding check + side-speaker idea (systems)
**Owner:** "I miss the subtle rounded shape of cathedral" → visual's rev 5 rounding. **Checked (how-it-works rev 5):**
- port mouth at ≈ 60 OK;
- **jacks must change:** two rows clash with the deck (upper row) and the end cell (lower row). One row of 5 (phones, line, MIDI in/out, device USB-C) fits 64; power, TUNE and SPLIT move onto the plate (which also answers job 31). Fallback: cell 2 inboard and two rows at ≈ 16 / 28;
- **top-back edge r 8 must drop to r ≤ 4:** at the 71.6° corner r 8 moves the upright tipping edge ≈ 11 mm in, so it rocks at 1.64 N; r 4 → 2.08 N, r 3 → 2.19 N;
- presses ≈ 3.4 / 4.5 N; runners 6.3 kPa OK; the front-face flat ≈ 16 holds the host port, but the split target moves to the plate's front rim;
- coverage updated (jobs 6, 31, 32).

**Owner idea:** "And w what if the speakers were on each side left and right so up or down didn’t matter". → `c-gnomon/side-speakers.md`.
- Ø 55 doesn't fit the end faces; a 40 mm class (≈ 40 × 40 × 18.3, RS listing) fits only high at the back, straddling slab and cheek.
- It displaces the port (sealed), the jacks (under the eave) and the end-grain cue.
- ≈ −5.5 dB (cone area) and off-axis at the player in both poses (beams above ≈ 3 kHz).
- **Verdict: not recommended as a replacement**; the plate drivers already face the player in both poses. Gains: a controls-only plate, maybe a smaller D, sound for a circle. Best version described. Owner question: what "up or down" problem he's picturing.

### 2026-11-22 round 2, turn 1 (systems): bases for flat / slightly angled
**Owner 19:23** (verbatim in owner.md): upright dropped; "one arrangement that can either be flat or slightly angled". Speakers on the ends: asked, unanswered; plate drivers stay the default. **Director's round 2:** keep the rev 5 slab; redesign only underneath. Candidates were SILL, TRIPTYCH and TURNING CHEEKS.
**Results [calc]:**
- **SILL survives.** A full-width printed bar flush in the rear band of the base flips down to a past-90° stop, where load drives it into the stop. θ = asin(h/(D−5)): T/3 → 6.7° / 6.1°, T/2 → 10.1° / 9.2° (I lean T/3). Knuckles on pin stubs; a flexure detent (magnet fallback). Packed = the slab (280 × 105–115 × 35). **Its recess eats E's 4 % margin at D 105, so D 115 or a 3 mm bar.**
- **TRIPTYCH killed:** one hinge can't close over the plate (top edge) and fold under the base (bottom edge, 35 lower); it needs two hinges plus a catch. The rim already protects the panel.
- **TURNING CHEEKS killed:** the cam can't be the whole end cap (180° symmetric); an eccentric disc reads as a knob; the rod runs through E's sealed box.
- Offered **CHOCK** (a loose printed wedge stored in the same recess) as a second, different-in-kind choice, only if the director wants one.
**Files:** jam turn; `concepts/r2-sill/how-it-works.md`; jobs.md rev 6 (job 32 short list and detail row).
**Next:** the director steers T/3 vs T/2, D 115, CHOCK yes/no; then the visual designer draws.

### 2026-11-22 round 2: SILL checked against the sheet (systems)
**Director:** h = T/2 = 17.5, D 115, θ ≈ 9.2°; CHOCK as an inset.
**Checked:**
- Bar ≈ 236 is right: the n 5 plan corners curve the rear edge, so a straight flush bar only fits ≈ 280 − 2 × 17.5 − walls.
- **Knuckles: two (x ≈ 30 / 250), not four.** The load goes through a full-length stop, and each Ø 9 knuckle needs a ≈ 10 mm pocket, so fewer pockets means less of E's box lost (recess 16 + pockets ≈ 5 ≈ 21 cm³, affordable at D 115, UNVERIFIED).
- Centre notch OK and clear of SHOE.
- Tilted footprint ≈ 280 × 111, overall ≈ 119 × 53: matches.
- **CHOCK as drawn won't store** (6 mm taper > 3.5 recess; 280 > 236). The working version is a uniform 236 × 17.5 × 3.5 strip that presses into a slot along the recess's rear wall. Keep it only as the fallback if no pin is acceptable.
**Coverage** (`concepts/r2-sill/coverage.md`, jobs rev 6): all supported; weaknesses 3, 15, 26, 28, 33.
**Next:** the sheet fixes (knuckles, CHOCK); the director scores SILL.

### 2026-11-22 round 2, turn 4: CRADLE / PLINTH / HANDLE (new systems seat)
**Took over the seat** from the notes above. **Owner since SILL:** 20:25 "I can only see one version how am I supposed to judge"; 20:27 "I do wish it was more distinctive refardless". **Director turn 3 + amendment:** SILL is the calm baseline. The new concepts must be clearly more distinctive in silhouette and idea, through one strong move of form, calm and soft, and each recognisable from its end view at thumbnail size.

**Randomness (`secrets`):**
- "piano music desks" → CRADLE's ledge;
- "Japanese joinery" → wedged tenons for the cheeks, and S9 seen as a sliding dovetail;
- Oblique "Give way to your worst impulse" → the plinth as a bass chamber (rejected).

**Decisions (proposals) and why:**
- **Shared angle rule: the back rises T/2.** SILL 9.2°, CRADLE ≈ 9.4°, PLINTH ≈ 8.75°. Comparable columns.
- **CRADLE survives with a rail ledge, not a detent.** A detent needs ≈ 100 N at r 8 (≈ 0.8 N·m of load).
  - The geometry: rail seat at T/2 just behind the slab; pins Ø 4 at (8, 8) in 5 mm slots; front-bottom r 8 arc centred on the pin. Tilt = lift, push away 5, set down; the front lip moves 0.7 mm.
  - Consequences: jacks to the front face (lip r ≤ 12), port mouth to the rear face (elbow), 306 × 127, no E loss.
  - **Cheek A (top at θ, 35 → 52.5) recommended** for the thumbnail test; B (35 tall) fails it flat.
- **PLINTH survives.** 260 × 95, 11.7 → 26.3, S9 tongue on top (dock downhill toward the player, so gravity holds it), S9 dock below, right-end drawer. Fully printed with no metal; packed = play-ready.
- **HANDLE killed** on four counts:
  - a shallow lever at ≈ 9° (≈ 1.4 N·m → sprung toothed hubs);
  - the carry and stand pivots conflict;
  - ASA creep;
  - a 28 cm³ groove, and SILL's end view at rest.
- **Coverage:** both survivors support all 34 jobs. CRADLE's new weakness is 34 (the front-face row); PLINTH's is 32 (the second piece).

**Files:**
- `concepts/r2-cradle/{how-it-works,coverage}.md`
- `concepts/r2-plinth/{how-it-works,coverage}.md`
- `concepts/r2-handle/how-it-works.md` (kill record)
- jam turn 4

jobs.md is unchanged (rev 6 still fits).

**Open:**
- **Director:** cheek A vs B; accept the rail ledge in place of "a detent"; jacks on CRADLE's front face; D 105 vs 115 (neither survivor recesses into E).
- **Visual:** the cheek A outline and the rings centred on the pivot; PLINTH's reveal depth; front lip r ≤ 12 for CRADLE.
- **Eng:** CRADLE's port elbow on the rear face, rail stiffness (10 × 10 ASA), front-face connector row; S9 tolerance (shared); the real mass and COM.
- **Owner (with the sheet):** which column; is a pin "stuff"; is a second piece OK; SHOE / loose; end speakers (CRADLE's cheeks would cover them).

**Next:** visual draws CRADLE (A, with B as an inset), PLINTH and the same-scale comparison sheet. The director scores all three. I re-check coverage against the sheets for any 9+.

### 2026-11-22 round 2, turn 5: EASEL + one speaker (systems)
**Owner 20:46:** "I do like one that sits up at an angle with a narrow footprint … like cathedral at least but without the keyboard"; "Why would I have two mono speakers that’s stupid. Drop to one speaker" (REQUIREMENTS updated by the coordinator). **Director turn 4:** EASEL as the fourth column (60°, triangular ends, narrowest footprint); stereo end drivers withdrawn; one grille on the axis.

**EASEL** (`concepts/r2-easel/`) [calc; mass 0.66 kg and COM ESTIMATES]:
- **Geometry:** 60° from CATHEDRAL; plate L ≈ 100 set by the driver (≈ 30 depth over the magnet; it first fits at L ≈ 95); front face 12; back 98.6.
- **Footprint:** A F = 50 ("half the face") or **B F ≈ 61 (foot : height 1 : φ), recommended** (cells flat on the floor; a roundable apex).
- **Tip-back, pressing square to the plate:** at s 40, A 4.6 N / B 7.5 N; at s 60, 2.6 / 4.0. So the controls go in the lower ≈ 45 mm and the upper plate carries lights only.
- **Pull at the ridge:** ≈ 1.5–2 N forward on every version.
- **Inside:** C box low-centre; port on the left end; jacks two rows on the right end; host on the front face; four boards.
- **Packed and coverage:** packed 1.08 L; SHOE on the back face. Coverage: all jobs except 32 as worded (scope question for the owner; rev 7 wording proposed, not applied).
- **Randomness:** "bookends" → cells low and back.

**One speaker:** C box ≈ 120 cm³, so D 105 now fits SILL, CRADLE and PLINTH (notes added to each how-it-works: SILL θ 10.1°, CRADLE 306 × 117 / 10.3°, PLINTH plinth 260 × 85 / 9.6°). Below ≈ 103 needs the grille beside the rows (panel).

**Open:**
- **Director:** A or B; D 105 for all slabs; job 32 scope.
- **Eng:** re-pick the single driver and box; C in the triangle; the magnet size; four boards; tact-switch forces.
- **Owner:** does EASEL replace or join flat-or-slightly-angled.

**Next:** visual adds EASEL to the comparison sheet; the director scores the four; I re-check coverage against the sheets.
