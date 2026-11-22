# floss: visual designer notes

## Where things stand (2026-11-22, concept round 2, my first concept turn)
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
