# floss: visual designer notes

## Where things stand (2026-11-22, concept round 2, visual turn 3: after the director's steer 2)
**Inputs:** the director's "Concept round 2, steer 2" (S1–S5) in `notes/director.md`; `eng/module-r3.md` (speaker E: two TEBM28C10-4B in one ported ≈ 190 cm³ box filling the rear region, a ≈ 125 crown with two grilles, 105 conditional / ≈ 115 safe, grille Ø 2.0 on 2.6 pitch in Ø 46 fields, rake ≥ 63°, ASA, knob stock: gold 3010 in stock, black out until 3 Jan 2027, stepped controls become firmware-stepped 9 mm pots, FALLBOARD lid needs a 17.5 rib grid or a 1.2 skin); systems' `module/how-it-works.md` rev 3 and `yoke/how-it-works.md` rev 1 (cups at the keyboard's rear corners reaching forward, arms clamped at any angle by the module thumbscrew, the cap required as carry cover and play rear foot, stack ≈ 395 × 135 × 74).

### Director's rulings I worked to
- S1: **YOKE is a concept and absorbs CLOTH** (wrap + grass mat are YOKE options). CLOTH killed as a standalone.
- S2: **knob A baseline**, B a column; recommendation A; no new knob images.
- S3: **house = warm walnut-brown**, not near-black. Keep the colour-from-the-spool system, cream stage and marks, one coral, amber lights, unnamed carries, one-spool deboss as a fallback (not baseline). **Drop "stage blacks and spike marks" as the story** (a draw isn't the product's idea). TPU colour is my call with one line why.
- S4: **cream stage ends a few mm behind the rear row; the brown roof rises behind it holding the crown**; **one fair arc + exactly two flat facets** (no gable).
- S5: FALLBOARD's four-panel lid with the seam cross accepted; liner-up carries to YOKE's wrap; SPINE area count is systems'.

### Decisions this turn (mine unless marked)
1. **The colour's idea, from floss itself:** a string machine is furniture you play: a warm wooden house with a lit keyboard of controls. Walnut-brown ASA/PETG house (no imitation grain); cream stage only where hands work; cream marks on brown; **gold knurled knobs** (Tayda 3010 gold in stock [r3]; the family's brass, honestly; director may overrule); **black only for what you flip or press** (tabs, HOLD, TAP, toggle) and the TPU strips; one coral; amber light. Black house = the owner's alternative, in one line.
2. **TPU dividers stay black:** the stock colour, reads as a drawn rule on cream, matches the touch parts; they hide the split-print seams at x 74.5 / 205.5 [r3].
3. **The roof:** full width behind the stage at rim height (it's E's box lid, systems); raked front edge ≥ 63° drawn as a darker band; **all rear-row words on the rake, cream on brown**; front-row words on the stage in brown.
4. **The crown:** E's airtight box part, ≈ 125 wide, set in the roof with a hairline seam; two grilles at x 140 ± 31, y 73 (A): **259 holes ≈ 814 mm² per driver** (counted).
5. **Outline:** pure arc in plan; **facets are chords under the roof's lip** (dashed in plan, flat bays from behind). Same volume as rev 2's chords; no gable. ENG: lip overhang ≈ 2–3 mm.
6. **Host port in a recessed pocket** on the front (systems from r3).
7. **YOKE in the house brown** (arms, cups, cap); cream index rings on the pivot discs; black thumbscrews; the **wrap stays near-black** (soft outer layer and mat; dirt; S1's words).
8. **FALLBOARD and SPINE recoloured in place**; FALLBOARD's closed lid shows the 17.5 rib grid ghosted (1.2 skin).
9. **Withdrawn:** rev 2's B ratio story (14 unit, 20:8:3), "stage blacks", black knobs.

### Files (all opened and checked)
- Source `concepts/_src/r3.py` (run from `_src`: `python3 r3.py [module fallboard spine yoke]`; cloth functions remain only because YOKE B reuses them).
- `concepts/module/module-1to1-A2.png` + `.pdf` (A beside B, brown, roof, E crown, smooth arc).
- `concepts/yoke/yoke-A-carry-and-play.png` (redrawn to systems' mechanism) and **`yoke-B-wrap-grass-pack.png`** (new: grass plan + side, wrapped bundle, in a pack bare / wrapped / module + cap, weights, wrap steps).
- `concepts/fallboard/fallboard-A-in-use.png`, `-B-closed-and-packing.png`; `concepts/spine/spine-A-in-use.png`, `-B-closed-and-packing.png` (recoloured; the B sheets' module row notes r3's 0.70–0.85 with E; kit totals still from systems rev 2).
- `concepts/cloth/*.png` **not updated** (retired; its looks file is marked superseded).
- Words: `module/`, `yoke/` looks-and-feels rewritten; `fallboard/`, `spine/` recoloured in place (rev 3 headers); `cloth/` marked superseded.

### Key numbers now
| | YOKE | FALLBOARD | SPINE |
|---|---|---|---|
| Carried (A knobs, Xkey) | 395 × 135 × 74 ≈ 3.9 L (wrapped ≈ 425 × 165 × 95 [est]) | 412 × 265 × 42 | 412 × 148 × 59 |
| Carry parts | 0.14–0.20 kg (+ wrap 0.23–0.36) | 0.47–0.60 | 0.42–0.52 |
| Spare in a 300 pack | 165 (wrapped ≈ 135) | 35 | 152 |
| Module | 280 × 105 × 35 (≈ 115 if E's margin fails); 0.70–0.85 kg with E [r3] | | |

### Open questions
1. **Owner:** knob A or B; brown (or black) house; gold knobs; firmware steps with no detent feel; YOKE's set-up screws and plinth-high play pose.
2. **Director:** gold knobs; the play pose's 37 mm plinth in YOKE; whether the kit sheets' kit totals should wait for systems to restate them with E.
3. **Eng:** coral DEPTH knob (none found in the 3010 range); brown ASA shade; roof lip at the facets; 105 vs 115.
4. **Systems:** kit weight totals with E's module; the module's foot sockets for YOKE's cap pegs (drawn as stated, not detailed).

### Next
The director calls READY once both turns are in (and r3 is folded in, which it is), then scores the module, FALLBOARD, SPINE and YOKE together. For the approved concept: the handoff's "How it looks and feels" for every state, 3/4 views, the print colour split (which part in which filament), and the marking system at 1:1.

---


## History: visual turn 2 (near-black "stage blacks", superseded by steer 2 S3)
I took the seat from the notes below (history, not commandment). Read: `PRINCIPLES.md` (new owner principles: case entirely 3D printed, services fine; cloth wrap fine around a printed core; analog-first not digital-free; no paper anchoring; no weight target), `jobs.md` rev 3.1, `eng/module-r2.md`, the director's "new director, concept round 2 steer 1" (R1–R6), systems' rev 2 `module/`, `fallboard/`, `spine/`, `cloth/` how-it-works.

**Mid-turn owner correction** (coordinator, verbatim): "The carry should fit a portable MIDI controller but the case does not need to surround it just have an attachment point. I'm just saying don't assume not making a rule". Not a rule; it removes the enclosing assumption. Answered with a sketch, **YOKE** (below). Director decides.

### Draws (python `secrets`)
- Oblique Strategy "Faced with a choice, do both" → the knob drawn both ways at 1:1; divider TPU strip with a groove fallback.
- Field: stage lighting → the material story, and YOKE's name.
- Twist: "the colour comes from the spool, never paint" → every colour is a filament, a bought part or a light.

### Decisions this turn (mine unless marked)
1. **One material story: stage blacks and spike marks.** Warm near-black matte PETG for everything structural, module and every carry (the house); **cream PETG deck** (the stage, the one lit surface); **cream marks** for anything read or set to on black (rail ticks, target, crown words, wordmark, kit scales, CLOTH's thread); **coral once** (DEPTH); **amber light** for both lights. Two spools + a little TPU. One-spool fallback: debossed marks. Walnut, brass, bookcloth gone. **Carries carry no name**; the name is on the module.
2. **Dividers: pressed-in black TPU 95A strip 1.6 × 2.0, flush** (felt as a softer, warmer, grippier strip, no edge). Fallback: printed groove 1.0 × 0.4.
3. **Knob both ways, my pick A.** A: Tayda alu Ø 10 × 8 → 280 × 105 × 35, unit 35, 8:3:1, deck 25, rows y 14/31, crown foot 41, finger room 5. B: family 18T Ø 14.5 × 13.5 → **280 × 112 × 42 restated as unit 14, 20:8:3** (halves 5:4, centre:end 8:5), deck 26.5, rows 14/35.9, foot 48.5, finger room 5. Kits +7 mm with B.
4. **Grille:** Ø 1.9 holes, 2.6 hex pitch, Ø 46 field on the crown top, clipped to the flat: **260 holes ≈ 737 mm²** (≥ 620), counted in code.
5. **Wordmark** cream on the crown's rear face between the facets; no words on the front face; target is a cream printed rider (a spike mark); port light amber.
6. **FALLBOARD** 412 × 265 × 42, all black; keyboard on the front wall; 15 lane; left pocket coil + adapter, right charger + card; lid on a printed over-centre brace; seams left as lines (a deliberate V-groove cross on the lid); no lamp. **35 mm spare in a 300-wide pack (17.5 a side).**
7. **SPINE** 412 × 148 × 59, all black; the stop's two beads + knuckles read as a book's raised bands (the only visible feature is the mechanism); stop drawn in section at 3:1; standing pose cut; 152 mm spare in the pack.
8. **CLOTH** near-black coated outer, near-black liner, cream thread on both faces; **spread liner-up always** (coated face meets the world), which also suits systems' grass flow; hem weights hidden; grass pose drawn (sit on the 435 mm near cloth).
9. **YOKE (sketch):** two printed arms on the module's own ¼"-20 inserts with swivel cups on slots. Carry: keyboard keys-up under the module, ≥ 6 mm air, 396 × 135 × 64 (Xkey), ≈ 3.4 L, carry ≈ 0.08–0.12 kg [est]. Play: arms swing forward, keyboard in front, keys never flip. Strong on weight, simplicity, family reuse (any S4 module); weak on exposure (panel and keyboard edges face the bag) and the loose charger.

### Files (all opened and checked)
- Source: `concepts/_src/r3.py` (run from `_src`: `python3 r3.py [module fallboard spine cloth yoke]`). `r2.py` is history.
- `concepts/module/module-1to1-A2.png` + `.pdf` (1:1 on A2, both knobs side by side; the old A3 pair is deleted).
- `concepts/fallboard/fallboard-A-in-use.png`, `fallboard-B-closed-and-packing.png`; same for `spine/` and `cloth/` (A and B each).
- `concepts/yoke/yoke-A-carry-and-play.png` (new, on the coordinator's request).
- Words: `how-it-looks-and-feels.md` rewritten in `module/`, `fallboard/`, `spine/`, `cloth/`; new in `yoke/`. Each kit file has a "how it compares with YOKE" section.

### Key numbers now
| | FALLBOARD | SPINE | CLOTH | YOKE (sketch) |
|---|---|---|---|---|
| Closed (A knobs) | 412 × 265 × 42 | 412 × 148 × 59 | ≈ 400 × 150 × 65 soft | 396 × 135 × 64 |
| With B knobs | 412 × 272 × 48 | × 66 | × 72 | × 71 |
| Carry weight | 0.47–0.60 | 0.42–0.52 | 0.23–0.36 | ≈ 0.08–0.12 [est] |
| Spare in a 300 pack | 35 | 152 | ≈ 150 | 165 |

### Open questions
1. **Owner:** knob A or B; black/cream/coral/amber replacing walnut and brass; plain unnamed carries; YOKE's exposure vs its weight.
2. **Director:** YOKE as a concept or not; both lights amber (CATHEDRAL's ring colour not found in the records; match it if it's stated somewhere); one-spool debossed fallback acceptable?; FALLBOARD's lid seam cross vs a six-panel lid.
3. **Eng:** black and coral Ø 10 × 8 knobs (UNVERIFIED colours; fallback printed coral cap); TPU slot allowance; lid foam ≈ 24–29 mm; YOKE arm stiffness and thumbscrew hold.
4. **Systems:** "liner-up always" for CLOTH; SPINE's lane/bay area overlap (62 × 30 counted twice); module rows/foot to the chosen knob; YOKE's mechanism if the director takes it.

### Next
Director rules (YOKE in or out; knob preference to send to the owner). Then, for the approved carry: the handoff's "How it looks and feels" for every state, real 3/4 views, print files' colour split (which parts in which spool), the marking system at 1:1.

---


## History: concept round 2, first visual turn (previous designer; walnut, brass, bookcloth, gutter, lamp and engraved line all superseded)
- **The jam is closed:** director turn 6 plus its addendum. Three kits go to concepts: **FALLBOARD (lead), SPINE (now a solander box), CLOTH**. **One module goes into all three.**
- **Owner direction since the jam (verbatim, `design/owner.md`):**
  - 13:25 "The module does not have to match keyboard width": **S8 is withdrawn**;
  - 13:29 "It needs to fit in a backpack comfortably … does not have to be a rectangle … a thoughtful ratio base";
  - later: "don't anchor on the page size thing … It just needs to be portable and make sense and be harmonious";
  - "I didn't create the weight target. The principles are portable": **T5 is withdrawn as a number**. Show weights, lighter is better, nothing pass/fail.
  - The project root now has `PRINCIPLES.md`, which all agents read first (see its §2 harmonious proportion, §6 separation mustn't get in the way of hands, §10 images only where needed).
- **Systems wrote** `concepts/module/how-it-works.md` (297 × 105, 2√2 : 1, speaker on the axis, two-row map) and `concepts/{fallboard,spine,cloth}/how-it-works.md`. The coordinator said the module's proportion is **my call, and systems follows it**.
- **Eng wrote** `floss/eng/module-r2.md`:
  - sealed **TEBM28C10-4B** speaker, body ≈ 32, "≈ 40 with knobs"; **no passive radiator**;
  - cold-socket USB-C with a C-to-A adapter in every kit;
  - weights;
  - lid lamp ≈ 0.05–0.1 W.

## What I did this turn
- **Draw** for the outline: "a ship hull in plan" + "Go slowly all the way round the outside" (Python `secrets`).
- **Module proportion (my call): 280 × 105 × 35 = 8 : 3 : 1 in a 35 mm unit.**
  - **From the parts:** 264 of panel + 8 per end = 280; the speaker sets 105 at the centre; the jambs need only ≈ 56 at the ends → 70; the speaker needs 32 → 35.
  - **The ratio, from string lengths:** each half is 4 : 3 (a fourth), the whole 8 : 3, centre : end = 3 : 2 (a fifth), length : height = 8 : 1.
  - **297 × 105 rejected:** paper-derived, and 17 mm longer with no part in it.
  - Systems must move every x by −8.5 (axis 140); pockets become ≈ 59.
- **Outline:** a hull in plan.
  - Straight front with the brass rail; r 10 front corners; straight 70 ends.
  - A fair rear arc to 105 (R 297.5).
  - Two flat port facets on the arc: plan-left power · USB-C · tune · split; plan-right phones · line · MIDI in · MIDI out.
- **Height PROPOSAL 35, not 40.**
  - Deck sunk to 26 over eng's flat stack, with the cells beside the crown.
  - Knob tops at 34, rim at 35.
  - A speaker crown 70 wide on the axis, its top at 35, with a raked front (y 47 → 55) carrying DRIFT · SHIMMER · TIME labels; the wordmark on the crown top.
  - Kits get thinner: FALLBOARD 43 (48), SPINE 56 (61).
- **Panel visuals:**
  - systems' two-row map;
  - PRESSURE and SHIMMER mode at Ø 10;
  - DEPTH coral on the axis;
  - brass frets (raised 1 mm, with a flush inlay as fallback per PRINCIPLES §6);
  - organ stop jambs at both ends.
- **Pictures, all opened and checked** (source `concepts/_src/r2.py`, run `python3 r2.py [module fallboard spine cloth]` from `_src`):
  - `concepts/module/module-1to1-A3.png` + `.pdf`: true 1:1 on A3 (plan, front, rear, section);
  - `concepts/fallboard/fallboard-A-in-use.png`, `fallboard-B-closed-and-packing.png`;
  - `concepts/spine/spine-A-in-use.png`, `spine-B-closed-and-packing.png`;
  - `concepts/cloth/cloth-A-in-use.png`, `cloth-B-closed-and-packing.png`.
  - **A sheets:** bench (or table) and lap, plan and side; the keyboard range (smallest and largest with end blocks; CLOTH adds a chunky MPK); the cable path and pockets enlarged; the rear wall with windows on the port facets.
  - **B sheets:** closed beside a 16-inch laptop (≈ 356 × 248 × 17, ≈ 2.1 kg) and a hardback (≈ 156 × 234 × 35); standing in an illustrative 300 × 450 daypack; end views (pale = with a 40-tall module); weights (no target); five packing steps.
- **Words:** `how-it-looks-and-feels.md` in `concepts/module/` and in each kit folder.

## Key numbers now (mine unless marked)
| | FALLBOARD | SPINE | CLOTH |
|---|---|---|---|
| Closed | 412 × 288 × 43 (48) | 412 × 143 × 56 (61) | ≈ 400 × 150 × 65 with an Xkey; ≈ 335 × 115 × 60 with a nanoKEY2 |
| Kit weight, nanoKEY2 → Xkey (systems from [r2]) | 1.45–1.91 → 1.80–2.27 kg | 1.25–1.61 → 1.60–1.97 kg | 1.17–1.56 → 1.53–1.92 kg |
| In a 300-wide pack | fits on its short edge, **only just** (288) | easily | soft |

## Kit looks (decisions)
- **FALLBOARD:**
  - walnut tray and lid; a cream label with a coral line on the lid;
  - a near-black bookcloth bed; dark-brown pocket floors;
  - brass scale, thumb locks, catch and stay;
  - the optional lamp is visible only when lit.
- **SPINE:**
  - walnut-brown bookcloth trays, a darker spine;
  - brass book corners, a cream label, a strap;
  - carried by the spine.
- **CLOTH:**
  - a dark slate green coated quilt, with the outline, centre line and home-octave words in cream thread;
  - brass corner weights;
  - a lighter green pocket and sleeve.
  - On a lap it's two objects; that's stated.

## Director's rulings (turn 3), as amended by turn 6 and its addendum (S8 and layout D withdrawn; one module; coral on DEPTH, the shimmer group on the axis)
- **One voice, the same in every kit.** Concepts differ on the kit only. Systems wrote the voice in turn 4: velocity = speed; strands low·main·high per half; DRIFT; lean selector swell·drift·tone·shimmer with the poly AT → channel → CC1 → nothing ladder; HOLD = plant-and-tend, surviving the keyboard, its scope following the split (an owner question).
- **Kits forward:** FALLBOARD (lead), SPINE (its real rival, wins on bag space), CLOTH (the two-package answer). LAMP, TETHER and BACKBONE are killed (light → FALLBOARD's lid; strap → an S4 accessory).
- **S8:** an owner proposal, worded "floss adds no width to the keyboard you carry". It's now ≈ 412 with end blocks, so the wording becomes "about an inch over the widest travel keyboard". CLOTH's 270 BLOCK is the exception.
- **Split:** rule A (fixed B3 | C4) plus the brass target (B rejected). The home-octave line goes on FALLBOARD's lid card, inside SPINE's cover, and woven into CLOTH.
- **Lights and power:** two lights (status; port, with a blink per note). One power switch, on the module; SPINE's "open = on" is dropped. Job 29 is added.
- **RAIL's row:** kept, but **grouped** (gaps you can count). HOLD goes with touch.
- **Hold the keyboard by its ends:** end blocks, nothing across a key. **Every kit has an accessory pocket.**
- **Assume the published-data speaker path** unless eng finds a published slim pairing. This is the owner's "he measures nothing" rule.

## What I added in turn 5 (pass 2)
- **Draw:** "Change instrument roles" + pipe-organ stop knobs, applied to the face.
- **FALLBOARD** (sheet `sketches/visual-module-jam3a-fallboard.png`):
  - **Rail, 412 × 95, layout D:**
    - a cream channel sunk 6 mm under the walnut rim;
    - the front row in seven groups, 388 long at pitch 22 + 10 per break (+4 spare on 412);
    - **brass frets** (1 mm raised) at each group break;
    - **organ stop jambs at each end:** OCTAVE + three stop tabs low·main·high, front to back;
    - the back line of kinds at Ø 10: PRESSURE (coral) behind attack/release, SHIMMER behind depth, FREE/SYNC behind time;
    - the wordmark centred in the grille strip (a piano's nameboard);
    - TAP's ring = the status light.
  - **Bed, 412 × 155:**
    - end blocks 80 deep at the back (8 in / 40 out / 32 travel / inside 404), with a padded face, a foamed lip over the end cap and a thumb lock;
    - one brass scale on the bed lip and the target rail;
    - the gutter pocket: 404 × 12 × ≈ 30–36 tall, holding the coiled cable and a flat spare (no charger);
    - the host port and port light at the gutter's centre;
    - a foam strip under the lid.
  - **Closed:** ≈ 38 (slim) / ≈ 40–46 (published). The channel is why the published path costs so little: the knob tops at 32 sit under the rim.
- **SPINE** (sheet `...jam3b-spine-cloth.png`):
  - **closed:** 412 × 145, brass book corners, a cream label, a coral line; ≈ 54 / ≈ 56–62 thick;
  - **sag:** on a lap the spine runs across both thighs, so it's supported. It folds only where nothing is under the spine (knees apart, slats, lifted by its ends). Fix: a spine that stops at flat (bevelled board edges bearing on a rigid spine board); optional locking slat.
- **CLOTH:**
  - an 800 slate-green square with the family outline (412 × 250) woven in pale thread, plus a centre line and the woven home-octave line;
  - the BLOCK module behind the keyboard;
  - a pocket (charger included) and a washable sleeve;
  - brass corner weights;
  - honest: a bench-and-table kit, because it drapes on a lap.
- **Comparison** (sheet `...jam3c-closed-kits.png`), slim / published thickness:

  | Kit | Footprint | Thick | Volume | vs a 16-inch laptop (356 × 248 × 17) |
  |---|---|---|---|---|
  | FALLBOARD | 412 × 250 | 38 / 46 | 3.9–4.7 L | 2.6–3.2× |
  | SPINE | 412 × 145 | 54 / 62 | 3.2–3.7 L | 2.1–2.5× |
  | CLOTH | ≈ 400 × 150 with an Xkey, ≈ 335 × 110 with a nanoKEY2 | ≈ 56 / 64 | | |

  No one-package kit meets T4.

## Turn 2 record (history; superseded where marked)
- Superseded since: the pairings (the director ruled one voice); 400 → ≈ 412 (end blocks); RAIL 80 → 95 deep (layout D); elastic bands → end blocks; one ungrouped row → seven groups with frets.

- **Draws** (Python `secrets`):
  - Oblique Strategies: "Abandon normal instruments", "Remove specifics and convert to ambiguities";
  - fields: harmonica in its case, surveying instruments;
  - twist: "it lives on a shelf as an object between uses";
  - proportion: 3 (the same as systems' draw, independently).
- **Rules for how floss looks with someone else's keyboard:**
  1. own the outline, host the keys;
  2. width is ours (400 ≥ every slim keyboard);
  3. a dark coated-bookcloth bed;
  4. don't hide their controls, hide their logo when packed;
  5. floss's marks only on floss;
  6. materials, not colour-matching (walnut, cream, brass; coral only on PRESSURE).
- **PROPOSAL S8:** every module 400 wide, so the keyboard bed, hinge, split-target rail and cable gutter are one family part. Every rigid kit stands on end 400 tall, spine out, like books on a shelf (brass corners, cream label, one accent per instrument).
- **Proportions:**
  - SLAB 400 × 133 (3 : 1, two rows, SPINE);
  - **RAIL 400 × 80 (5 : 1, one row of controls, FALLBOARD)**;
  - BLOCK 270 × 100 (eng minimum, CLOTH).
- **New kit, FALLBOARD (my lead):**
  - **Layout:** RAIL module behind a 400 × 150 keyboard bed (12 mm cable gutter, two elastic bands, the rail as back stop). One lid hinged at the rail's rear top edge.
  - **Closed:** 400 × ≈ 230 × ≈ 38.
  - **The lid:** stands as a music stand and partial shade; carries a dim warm lamp strip on its top edge at night; lies flat back or lifts off on a pin hinge.
  - **Split and port:** a brass split target slides on a graduated rail along the module's front edge. The host port sits at the centre of the rail's front face, in the gutter, with the port light beside it.
  - **Inside the lid:** a printed card (MIDI map, "keep the keyboard at its home octave").
- **Verdicts on systems' kits:**
  - SPINE: keep and sharpen (SLAB boards, brass corners, spine label, card, target, two straps instead of sliding photo corners);
  - CLOTH: keep as the two-package answer (BLOCK with every knob below a raised rim; the cloth is the frame);
  - LAMP: kill as a kit (its light moves into FALLBOARD's lid);
  - TETHER: kill as a kit (its strap becomes an accessory on S4);
  - BACKBONE: kill (agree).
- **Pairings, flipped from systems:** FALLBOARD + TIDE (the lean panel fits one row); SPINE + BOW (strand tabs need two rows); CLOTH + either.

## Files
- **Pass-2 sketches** (current): `sketches/visual-module-jam3a-fallboard.png`, `visual-module-jam3b-spine-cloth.png`, `visual-module-jam3c-closed-kits.png`. Source: `sketches/visual_module_jam3.py` (`python3 visual_module_jam3.py [a b c]` from the sketches folder; matplotlib, Inter). The rail-drawing function (`rail()`, layout D from `FRONT`) and the bed with end blocks (`bed()`) are reusable for the concept sheets.
- **Turn-2 sketches** (history): `sketches/visual-module-jam2a-fallboard.png`, `visual-module-jam2b-proportions-shelf.png`.
- **Round-1 renderer:** `concepts/_src/fl.py` + `concepts.py` (slice-stacked ortho drawings). It's reusable for 3/4 views in concepts. It must run without `-I` (it imports `fl` from its own folder).
- **Eng:** `eng/module.md` (baseline). `eng/module-r2.md` (the speaker path, weights) didn't exist yet at turn 5. A folder `eng/speaker-sim/` appeared during turn 5; I haven't read it.

## The family's visual language (still applies)
- **CATHEDRAL:**
  - walnut case; superellipse corners (case 28.3, plates 24); cream plates;
  - brass and black; low knob Tayda alu Ø 10 × 8; knobs Ø 14.9 black;
  - marking: one tick ring at r + 1.7, ticks 0.35 wide, 11 ticks over 300°; words above controls, one word per label.
- **ONE SHEET:** cream PETG; sunk grooves. **HUSH:** felt pebble, maple pegs.
- **Owner taste:** off-centre is bad; logical grouping first; signal order; one plain word; one accent; "more brass than black".
- **floss in the module era:**
  - walnut rail and lip, a cream channel, brass (frets, target, scale, HOLD, corners), black knobs, one coral (PRESSURE);
  - a dark coated-bookcloth bed;
  - CLOTH in slate green.
  - No bought coral knob has been checked yet.

## Decisions carried from round 1 that still hold
- Signal order on the panel; per-half controls at the ends (now the stop jambs).
- Status light = TAP's lit ring (drawn in pass 2). Port light in the gutter.
- Names: Daisy modes *wide · glass · tape*; octave −2 … +2; strands *low · main · high*.

## Director's objections and how they stand
- **Round 1:** leftovers driving the layout → answered by S8 + layout D (the width from the keyboard, the depth from the parts). Busy panel → 13 round controls (systems). Felt → bookcloth. The palette is kept.
- **Turn 3:**
  - (1) 400 mm vs T4 → sheet c plus the S8 wording;
  - (2) weight → eng;
  - (3) speaker → both thicknesses drawn; the channel limits the cost;
  - (4) build craft → making steps still to list per concept;
  - (5) "why so plain" → stop jambs, frets, nameboard wordmark, one coral;
  - (6) bands over keys → end blocks;
  - (7) ungrouped row → seven groups with frets.
  - SPINE's lap sag → mostly a false alarm on a lap; fix with a stop-at-flat spine.
- Not yet ruled: everything in turn 5.

## Open questions
1. **Eng:**
   - the flat stack at deck 26 with the cells beside the crown, and the U-shaped board in the 280 hull;
   - the driver under the raked crown;
   - grille ≥ 620 mm² (drawn ≈ 560: widen the field);
   - insert bosses at x 60 / 220;
   - FALLBOARD's lid foam (≈ 20–24 mm strip).
2. **Director:**
   - 8 : 3 : 1 and the hull;
   - raised vs flush frets (PRINCIPLES §6);
   - TAP's ring carrying status plus tempo;
   - the near-black bed vs the pocket shade;
   - SPINE's clip-on lamp;
   - CLOTH's green vs oatmeal.
3. **Owner (with the concepts):**
   - board, book or cloth;
   - the lamp;
   - a kit that only just fits a 300-wide pack;
   - bookbinding craft for SPINE;
   - CLOTH as a bench-and-table kit;
   - the split-scoped HOLD;
   - a charger in the kit.
4. **Systems, to follow my proportion call:**
   - the module at 280 (x map −8.5);
   - pockets ≈ 59;
   - closed thicknesses 43 / 56;
   - the rear wall as two facets on the arc (their file says a flat rear wall).
5. **Parts:** a coral Ø 14.9 knob; engraved stop-tab rockers; brass fret stock; bookcloth; brass hardware; hem weights (all UNVERIFIED).

## Next
- The director scores round 2. Fix what's objected to.
- For the approved kit: write "How it looks and feels" in `handoff.md` for every state in systems' "how it works". Then:
  - real 3/4 views (`fl.py`, adapted to the hull);
  - the knob, tab and fret parts chosen;
  - the marking system at 1:1.
- Keep images to what must be visual (PRINCIPLES §10). The images are for the site, not for print. The 1:1 sheet is the exception the director asked for.

---

## 2026-11-22 (evening): CATHEDRAL-cues form round, jam turn 2

**Where things stand:** the owner turned down the module and YOKE on shape ("I hate the shape of these"). Big Energy's CATHEDRAL is now the guide for cues, not for the form. The case is fully printed, metal included; knobs and similar bought parts are the exception. No bookcloth spine. All controls in one plane. It sits at an angle, by shape if possible (his idea; a possibility, not an anchor; CLAUDE.md item 5). Brief: `BRIEF-CATHEDRAL.md`. Jam: `jam-cathedral.md` (systems turn 1, my turn 2). Sketches: `sketches/cathedral/` (`visual_jam2.py` → `cathedral-jam2-sections.png`, `cathedral-jam2-rose.png`).

**My turn 2, in short:**
- **What lost (as shape):** the module's arched plan and its separate speaker "house"; YOKE's appendage arms. Rule for myself: **nothing hangs off the body.**
- **Cues that carry over, ranked:**
  1. the framed plate (cream in a thick walnut rim, superellipse corners);
  2. the lancet grille;
  3. cathedral-grain grooves, with growth rings on the end faces, which now *are* the silhouette;
  4. brass as the one metal, printed, used only for wear surfaces (runners, foot ring);
  5. his pipe-façade field;
  6. the panel language (black, one red hero, Kalam, the 300° system).

  Dropped: hinge, stays-as-legs, the spine.
- **Verdicts on systems' five:**
  - WEDGE → sharpened into **DROP**;
  - TRIPTYCH kept, plus a hinge-free twin, **CASKET** (pencil-tin lid as stand; absorbs SLED);
  - BAIL killed (an appendage, like YOKE);
  - SLED merged into CASKET;
  - RETABLE killed as its own direction, kept as DROP's pose 2;
  - NAVE kept, with the seams as engraved hairlines.
- **DROP** (teardrop end, 25° drawn; the pipe at the back is the speaker box, port and handle):
  - the port mouth sits at the centre of growth-ring grooves on the end face;
  - "clerestory" lancet slots across the pipe's upper front for the two drivers, so the plate is controls only;
  - brass runners as feet;
  - a rear land for a ≈ 65° pose;
  - keyboard k2 under the base.
- **ROSE** (differs in kind): a circular plan. Every control sits on one 300° arc, 7 → 5 o'clock, in signal order, round a central lancet window. It's a tilted drum on a brass foot ring. Weak on carry, height (it wants ≈ 12°, not 25°), speaker E (one driver in the centre) and family fit. It risks the same rejection as the arched plan.
- **Rocker / keel killed [calc]:** a 3 N knob press rocks it about 29° (ESTIMATE). It survives only as a gently curved belly beyond DROP's flat land.

**Randomness used:** SystemRandom drew Oblique "Abandon normal instruments" and "Water"; fields sledge runner, pencil case, font; section teardrop; angle 25°; constraint "two identical halves" (it only half landed: it pushed toward a constant extrusion).

**Director's objections:** none yet this round. Last round's lessons carried: random draws aren't the product's story (each draw here is shown as a tag, and the idea stands on its own reason), and no costume (the round forms come from the driver, the port and the knob sweep).

**Open questions:**
1. Owner: flat *and* angled, or angled only?
2. Owner: does lost-wax cast from a printed wax count as "printed metal"?
3. Eng: DROP's pipe (drivers, port, volume ≈ 1,100 cm³ gross vs E's 190 net); the board under a 25° plate; pose 2's centre of mass; ROSE's driver.
4. Director: cut DROP's pose 2? Show ROSE as the wild card or kill it on carry?
5. Systems: derive DROP's ratio from its parts (I drew numbers; I didn't derive them).

**Next:** systems' structural pass on DROP, CASKET and ROSE, then the director steers. For whichever concepts go forward: end-elevation and 3/4 views showing the framed plate, the end grain and the brass, at concept fidelity only (the owner: no deep refinement before he approves one).

---

## 2026-11-22 (late): concept sheets for DROP, GNOMON, CASKET-B

**Rulings since my jam turn 2** (director turns 3 and 5; systems turn 4):
- ROSE is dead; its 300° arc lives on as the knob marking.
- DROP's pose 2 is cut. DROP is 2 rows, ≈ 37°, 260 × 88 × 62.
- GNOMON is the director's idea: sin θ = T / D ≈ 19.5°, the back ≈ 2T.
- CASKET-B (lid under the back, ≈ 11°, closes ≈ 50). CASKET-A is dead. TRIPTYCH is one line under it.
- SHOE is the shared carry (pending the owner), with loose-in-bag and a printed TPU band as fallbacks.
- The façade goes only where it's seen: on CASKET's lid, nowhere else.

**Made:**
- `concepts/c-drop/sheet.png`, `c-gnomon/sheet.png`, `c-casket/sheet.png`, 2800 × 4000 (14 × 20 in at 200 dpi).
- **Same scales on all three:** end view 3:2, 3/4 views 1:2, bag inset 1:4.
- Each sheet has: the end view big and first; a 3/4 view playing, keyboard in front; packed with SHOE; a loose-in-bag inset. CASKET adds closed (façade) and the underside (SHOE dock y 10–70, catch groove y 80–92).
- A short `how-it-looks-and-feels.md` in each folder.
- Source: `concepts/_src/cathedral_sheets.py`, a tiny flat-shaded painter's renderer with extruded end profiles.

**Visual decisions and why:**
- **DROP:** the cream field turns over the pipe's upper front inside the same end rims, and one bead line runs round the whole end face. That's the director's "rim wraps plate and pipe as one line" test. Growth rings across the whole end, centred on the port, make the wedge and pipe read as one block.
- **GNOMON:** the end face is flush (slab and cheek one surface, rings across both). The stretcher is shown dashed in the end view and docked in the packed view, as the SHOE variant, for the director to rule.
- **CASKET:** the lid is the same walnut as the module (one slab closed, with a seam line). The angled pose shows the lid ≈ 80 behind, honestly. I drew ≈ 10° from asin(15 / 86); systems says ≈ 11°.
- **Shared:** the port mouth sits at the centre of the left end face's growth rings (systems' proposed family rule). The brass ring is drawn, marked "only if cast counts".

**Open:**
1. DROP's hair-dryer risk.
2. GNOMON's stretcher.
3. CASKET's lid-behind read, and 10° vs 11°.
4. Façade placeholder, his to design.
5. Cast metal counting as printed (owner).

**Next:** the director scores. Then fix what's objected to. Once one is approved, write the handoff's "how it looks and feels" for every state in systems' how-it-works.

---

## 2026-11-22 (night): GNOMON pass 2 (director fixes 1–6, systems rev 2)

**State:**
- Round 1 scores: GNOMON 8, CASKET-B 7, DROP 6 (killed).
- The owner then said "Honestly my preference order would be angled, 90, flat" and "Multiple angles is fine". CASKET-B retires; GNOMON carries the round.
- Systems rev 2: tan θ = T / D ≈ 18.4°; rear face 2T = 70, square to the plate; back ≈ 66; footprint 280 × 111.

**Updated in place:**
- `concepts/c-gnomon/sheet.png`, now 14 × 25 in (2800 × 5000) so the loose view fits at 1:2. Seven views:
  1. end view 3:2;
  2. playing 3/4;
  3. from behind, low (open underneath, jacks on the right end);
  4. upright 3/4;
  5. packed on SHOE;
  6. both poses as end silhouettes;
  7. loose at the same size.
- `concepts/c-gnomon/how-it-looks-and-feels.md` rev 2.
- Source: `sheet_gnomon()` in `concepts/_src/cathedral_sheets.py`. `GN_TH` is now atan(T / D). The other two sheets' functions are left as they were, and I didn't re-render their PNGs.

**Decisions and why:**
- **Hairline** at T below the plate on the end faces: the lid plus its own thickness, the face still flush.
- **Port:** grooves only, no brass. The ring was a hose fitting.
- **Lip** rounded r 16 into the plate, so it's no longer a chamfered pentagon.
- **Rear 3/4 at 12° elevation:** below θ, so the underside shows. This is the only view that can show the hollow.
- **Upright view** lit from the plate's side, so the cream doesn't render grey.
- **No brass anywhere now.**

**Director's standing objection:** the 3/4 view reads as a generic wedge. My answer: the hairline and rings show in the front 3/4, and the rear 3/4 and the upright pose carry the idea. The front 3/4 physically can't show an underside that sits on the table, and I said so in the md.

**Open:**
1. Is the front 3/4 now enough for the owner? (director)
2. "90" for playing or for standing it up? (owner)
3. D 105 vs 115 (eng).
4. Cast metal counting as printed is now moot unless brass earns a job.

**Next:** the director re-scores GNOMON alone. If it reaches 9, it goes to the owner. After approval, the handoff's "how it looks and feels" for every state (angled, upright, packed with SHOE, loose, no keyboard).

---

## 2026-11-22 (late night): GNOMON rev 3, the owner's upright lean

**State:** the director scored rev 2 at 9; the owner sent it back with one change, verbatim: "Reverse the angle on the side behind the speakers so there's still a subtle angle when upright". Systems rev 3:
- the corner behind the speakers ≈ 80.5° (tan φ = T / 2D, φ ≈ 9.5°);
- angled pose unchanged at ≈ 18.4°;
- rear face ≈ 67.2;
- footprint 280 × ≈ 99.

**Updated in place:**
- `concepts/c-gnomon/sheet.png`, with the geometry in `sheet_gnomon()`: `PHI`, the new rear-face point `Rq`, and the slab's rear-bottom corner `Hc`, which is where the hairline now ends.
- The end view shows the 80.5° arc and a dashed ghost of rev 2's square face.
- The upright 3/4 is seen more from the side, so the lean shows.
- The two-poses view has a dashed vertical marked ≈ 9.5°.
- The title says "≈ 18.4° or upright (≈ 9.5° back)".
- `how-it-looks-and-feels.md` has a rev 3 section at the top.

**Why:** a lean read off a dashed vertical makes it look deliberate without a dimension. It reads as a music stand or easel, not a radio front.

**Open:** systems' note that if the owner meant the literal mirror (≈ 37° lean), it's one number to change.

**Next:** the director re-checks; then it goes back to the owner.

---

## 2026-11-22 (late night, 2): GNOMON rev 4, base and back square

**Owner, verbatim:** "I don’t like the angle on the back when laying flat. Make the base and the back 90 degrees when sitting flat".

**Systems rev 4:**
- the back is vertical in the playing pose (square to the base);
- the corner behind the speakers is 90° − θ ≈ 71.6°;
- playing angle ≈ 18.4°; upright the plate leans back ≈ 18.4° (one angle for both poses; tan φ = T/2D dropped);
- the back ≈ 66.4; footprint 280 × ≈ 88.5; overall ≈ 100 × 66;
- stretcher at y ≈ 15–75.

**Updated in place:**
- **`sheet.png`:**
  - end view: a right-angle mark at the base/back corner, labelled "base and back: 90°"; rev 3's 80.5° arc and the ghost line are gone; the scale bar moved top right;
  - the stretcher moved;
  - the upright view and the two-poses view now show the ≈ 18.4° lean (the two-poses view with a dashed vertical);
  - title "280 × 100 × 66 mm · ≈ 18.4° or upright (≈ 18.4° back)".

  Code: `PHI = GN_TH` in `sheet_gnomon()`.
- **`how-it-looks-and-feels.md`** rewritten clean as rev 4. The stale rev 2 and rev 3 claims (2T back, square plate-to-back corner, 9.5° lean, 111 / 99 footprints) are gone.

**Visual read:** one slope for both poses reads simply. On the table the square back makes a quiet, architectural block; upright it's a music stand, not a radio front.

**Open:**
1. Upright for playing or for display (owner).
2. D 105 vs 115 (eng).

**Next:** the director re-checks, then it goes back to the owner.

---

## 2026-11-22 (late night, 3): GNOMON rev 5, CATHEDRAL's soft shape

**Owner, verbatim:** "I miss the subtle rounded shape of cathedral". His CATHEDRAL words (2026-11-13 20:45): "I kinda want the corners to be softer and to be more architectural like how Apple does theirs". The poses stay as rev 4.

**What I read:** CATHEDRAL's softness came from:
- superellipse plan corners (n 5, r 28.3 case / 24 plate, concentric);
- eased rim edges.

Rev 4 was a sharp extrusion.

**Changes:**
- n 5 plan corners at r = T/2 = 17.5 (CATHEDRAL's ≈ half-thickness proportion);
- plate field corners r 10, concentric;
- back-top r 8; base-back kept r 4 so the 90° reads;
- every end-face edge rolled 3;
- the silhouette unchanged.

**Code:** `sheet_gnomon()` now builds swept meshes from rounded cross-sections (`offset_edges`, `squircle_delta`, `roll_delta`, `mesh`). The sheet is 14 × 29 in; view 8 is CATHEDRAL's render corner beside GNOMON's.

**For systems (listed in the md):**
- the flat end face shrinks to ≈ 64 in the slab band: the port moves forward to ≈ 60, the jacks go to two rows of 4;
- the back foot's flat runs ≈ 245;
- runner flat ≈ 7 of 10;
- footprint corners rounded;
- knob rows start at 24;
- the cheek thickness of 10 is my assumption.

**Next:** systems checks those, then the director, then the owner.

---

## 2026-11-22: GNOMON rev 5, systems' check folded in
- The top-back edge goes back to r 4: it's the upright tipping edge, and r 8 cut pull-to-tip to 1.64 N.
- Jacks: one row of 5 on the right end (phones, line, MIDI in, MIDI out, device USB-C), ≈ 18.5 below the plate.
- Power, TUNE and MIDI SPLIT move onto the plate's right end (two small toggles and a small knob).
- The split-target rail is now a fine cream scale on the plate's front rim.
- `sheet.png` and the md are updated. Side speakers: assessed by systems, not recommended; nothing drawn.
