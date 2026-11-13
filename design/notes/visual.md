# Visual designer notes (instrument; working name retired)

## BRANCHES, jam turn 2 (2026-11-13): personality + point of view; FREE/SYNC placed
Context: the owner wants branched creative rounds from v1.1 (he leans ONE SHEET or FOLD) with more personality and a whole point of view. His sources: furniture, instruments, tools, art, emotion; "take this to the park and be inspired". Pegs are loved, "organ like" is an example only. **Owner decided echo sync option B (11:58): a FREE / SYNC toggle near TIME, in every branch.** Shared rule (systems, accepted): the board is the constant, only the outside changes.
- **My turn:** `design/branches/jam.md` "Turn 2". Draw script `design/branches/draw-visual.py` (my own decks; every earlier-used Oblique card removed); results recorded in the jam §1.
- **Sketches:** `design/branches/concepts/jam-sketches/`, source `sketch_turn2.py` (layout read live from `fold_r5_check.py`):
  - `t2-rain-top.png`: computed ripple field;
  - `t2-chamber-closed-facade.png`;
  - `t2-ground-horn-section.png`;
  - `t2-butterfly-real-rail.png`.
- **Decisions and why:**
  - **BUTTERFLY (ONE SHEET), reshaped, "from tool to tree".**
    - Killed the printed scanned live edge: fake, and the first idea.
    - The rear band is a real live-edge walnut rail. One straight joint at y 160 (153.5 sat on the back-row knob edges), one butterfly on axis x 138; the jacks are drilled in the wood.
    - Precision runs as a spectrum from front to back (draw: "Spectrum analysis"). Emotion: longing. The French cleat stays.
  - **CHAMBER (FOLD), pushed, "closed an organ case, open a console".**
    - The façade goes on the lid's back: the closed top, and what the friend across from you sees when it's standing. The speaker stays put.
    - 25 pipe lengths ∝ 2^(−n/12), laid out the organ builders' way (alternating from a centre tower). Draw: "Humanize something free of error".
    - Reverse pegs, naturals in body walnut. Brass screws as impost rivets. RANGE in feet, in serif. Emotion: joy.
  - **PIERCED, killed as a branch** (+55 mm for a gesture is the wrong way on cost and portability). Draws: "Disconnect from desire", shyness. The carry job moved into GROUND as a felt-lined finger pocket. A +32 mm slot middle path was tried and dropped.
  - **GROUND (either), "calm on top, loud underneath; the wedge is a horn".**
    - The speaker fires into a folded horn inside the wedge; mouth at the rear and sides. Draw: "Listen to the quiet voice". Horn gain UNVERIFIED.
    - Persimmon underside (exuberance), finger pocket, high-contrast type, a hood over the status light.
    - 12° over 180 ≈ 37 mm (systems' rough figure was 15–25); 8° ≈ 25.
  - **NEW: RAIN (ONE SHEET), "a pond after rain".**
    - The v1.1 rings with no outer radius. Fields meet at smooth Voronoi seams that draw the sections, so the grooves go. It keeps his two-finish rule.
    - Pegs become stepping stones that also ripple ("everything that breaks the surface ripples"). Legends sit on smooth "lily pads".
    - Mustard CUTOFF = a ginkgo leaf; pale wet-slate shell.
    - Draws: Riley, calm, under a tree in dappled light, mustard, "Don't be afraid of things because they're easy to do". Unused: stretcher, concertina, binoculars (TRAY held in reserve: a worn neck-strap tray).
  - **FREE/SYNC (all branches): in front of TIME, in the pot's dead zone.**
    - FOLD (≈133, d ≈71); ONE SHEET (≈128, y ≈133).
    - Fore-aft throw: toward the player = free, toward TIME = sync.
    - TIME gets two scales: inner ms ("20 ms", "2 s"); outer 9 division marks with only 1/16, 1/8, 1/4, 1/2 written, a dot for dotted, a triangle for triplet.
    - No mirror partner (the reason: echo is the only effect that cares about time).
    - The beside-TIME spot is ruled out by margins (7.05 to the break; 5.1 gap vs ≈ 12.2 needed). The behind-TIME spot collides with the ECHO heading and type fan.
    - d6 "jack wall" tested and rejected on B-J13 (not visible from the seat).
    - **My check was by margins only, in scratch (`/tmp`), not in the repo. Systems must run it with labels.**
- **Open questions:**
  - Owner: reversed key colours; pegs cost ONE SHEET ≈ +8 mm of width (the last peg is 0.65 from the 276 edge) and FOLD closed height.
  - Eng: horn gain; wood/PETG joint movement; engraved fill on wood-fill PLA; ring grooves ≥ 0.9 pitch face down.
  - Systems: SYNC label check; BUTTERFLY depth; GROUND rake; mouth/pocket layout.
  - Maker: the ring coupon now also decides RAIN (view it under a tree).
- **Director objections:** none yet on branches (first steer pending).
- **Next:** the director steers. Then build concepts with systems in `design/branches/concepts/<name>/`: real r5-based renders (A look + park scene, B 1:1), not sketches. RAIN first if chosen: its idea only shows in a render with raking light.

## S2: 120° stand + bend reads as a joystick (2026-11-13, new visual designer; owner: "oh do those first")
Context: the owner locked HUSH / ONE SHEET / FOLD-105 as v1 (`versions/v1/`, untouched by me). These two fixes were in progress at lock time. The sheets in `concepts/<concept>/` are the post-lock S2 redraws; they were locked as `versions/v1.1/` (owner, 2026-11-13).
- **Owner's words:** "the fold's angle should be a bit less steep so the front face catches more light. also i want the bend slider to be a joystick (is it a snap to center fader or what?...)".
- **Diagnosis:** the round-5 top views drew the bend as a black ball over a long dark slot on a pale rectangle (FOLD, ONE SHEET) or a vertical pill tag (HUSH). Seen from above, that's a fader cap in a track. The mechanism was always a spring-to-centre one-axis thumbstick (#2765 class); only the drawing was wrong.
- **What the stick is now (`joystick()` in r5.py; I kept the previous designer's version and fixed what surrounded it):**
  - Part: 3.2 stem standing clear of the plate; a flared 10 mm cap with a grip rim and a sunk dish (cap top z + 12.6, was 13.5, so clearances only improve). In 3/4 and front views it reads as a stem + cap, i.e. a stick.
  - Ink: a round gate ring (Ø 15 / 13.4) with two bezel pointers at 12 and 6 o'clock: the tilt axis, the watch-bezel idea. Two pointers, not four, say "one axis".
  - Slot: short (4 × 11.2, stem + throw), nearly hidden under the cap; just a sliver shows fore and aft.
  - **Surround, per concept (my change):** every rectangle/pill that framed the stick is now round:
    - FOLD: the pale square is a round well tone Ø 18.6 (flush, R4 ✓);
    - ONE SHEET: the Delrin gate plate is a round disc Ø 18.6, **and it's now centred on the stick** (the old square sat at x 15 while the stick is at 20: a pre-existing bug);
    - HUSH: the pill tag is a round tag Ø 18.6 with the usual label tongue. The ring and pointers print on the tag, because felt can't hold a fine mark (principle 4).
- **Sheet B callout (all three), "BEND IS A JOYSTICK, NOT A FADER" (`stick_callout()` in sheets_r5.py):** a plain-words answer to the owner's question, plus three 1:1 side views: pull = bend down, let go = springs to centre, push = bend up. Panel slot drawn 11.2 long. The text also says MOD is a knob that stays put. Parts lists gained a "Bend" line.
- **120° stand (systems rev 5.7), sheet E:** `Fold.STAND = 60`, `Fold.STAY_L = 44.4` (stowed groove d 30–74.4). The side elevation frame is widened to y D + 84 (the lid was cropped), and the stand shot's shadow footprint is D + 64.
  - The angle is now drawn as an arc from the base plane to the lid. Labels moved clear of the knuckle and stay.
  - The tip lands 59 behind the base, matching systems. Reach is ≈ 100 up / 80 behind PLAY (systems: 99 / 79). The lid's cream plate renders visibly lighter than in the 105° sheet, as the owner wanted.
- **Checkers:** fold_r5_check 0, flat_r5_check 0, layout_r4_check runs. Ink clearances hand-checked: ring to MOD ticks ≈ 5.5, BEND label to bottom pointer ≈ 2.0, HUSH stick tag to MOD tag 3.1.
- **Re-rendered (4961 × 3508):**
  - fold: A-105, B-105, C-105, D-105, E-105;
  - hush: A, B, C, D;
  - one-sheet: A, B, C, D.
  - C changed only in the footer (no stick in its sections). I opened every one, with 1:1 crops of the stick in B, D and E.
  - FOLD-113 is dropped and not re-rendered; its stale sheets and round 4's unsuffixed FOLD sheets are still in `fold/` (delete when convenient). `mock-E-standing-105-r5old.png` is kept for comparison.
### S2b: director fixes (same day)
- **Slot gone:** the panel opening under the stick is now a **round dark hole Ø 7.5** (stem 3.2 + its ± 2.1 sweep at panel level + clearance) in every view. The one-axis gate is under the panel. The callout's side views cut the panel at ± 3.75 to match. Checked in 1:1 crops of A (all three) and E.
- **FOLD MIDI IN drawn** (systems rev 5.6 does list it): base right end face, MIDI IN y 70, MIDI OUT y 80, USB-C y 90–99 (`FO_MIDI_IN_Y`, `FO_MIDI_Y`, `FO_USB_Y` in r5.py). Labelled under the open end view on D. Notes on C, D and E corrected. My earlier "rev 5.6 lists no MIDI IN" was wrong.
- **Re-rendered:** hush A, B, D; one-sheet A, B, D; fold A, B, C, D, E (all -105). Checkers 0.
- **Open:**
  1. #2765 cap size and height still UNVERIFIED in hand (drawn 10 / 12.6).
  2. `fold/`, `hush/` and `one-sheet/` `how-it-looks-and-feels.md` don't yet describe the gate ring / round surround or 120°. Add these when handoff starts.
  3. Whether the S2 sheets replace the locked v1 copies is the orchestrator's / owner's call.

## S1 label pass + pre-build fixes (2026-11-13, after the director's round-5 scores: HUSH / ONE SHEET / FOLD-105 at 9 pending S1)
- **Back row legends are short, under section headings:** ECHO over type · time, REVERB over decay · type (`LAB`, `FX_HEADS`, `fx_heads()` in r5.py). Headings sit above the type-name fan, centred on each pair. HUSH: pressed, 2.0, like MIXER. ONE SHEET: dark, 1.8. FOLD: Kalam 2.0, kept small so it clears the plate edge.
- **Clearances (all ≥ 1.5 mm label–label and label–knob, checked with a font-metric bbox script, then in 1:1 crops of every top view):**
  - outer type names raised: row 5.6 → 6.2 (Inter) / 6.5 (Kalam);
  - legends above toggles at 7.4 (was 8.4); OSC 3 CTL's legend now goes above its toggle too, mirroring VELOCITY;
  - switch-pair legends 6.2 from the toggle (was 5.6);
  - MIXER no longer crowds: the short labels leave ≈ 6 mm.
- **Depth change: HUSH 186 → 187** (+1 mm, owner's "grow the panel"), so the headings clear the rear band rule. ONE SHEET (180) and FOLD (108 / 129) are unchanged. FOLD-113's headings are 0.9 from the plate edge; it isn't offered, so I left it.
- **Pre-build fixes from systems (common 7.3, fold 5.6), drawn:**
  - **PARA toggle (MONO / PARA / PARA+4)** mirrors AFTERTOUCH. Flat: (TL + dx, 111.5). FOLD: PARA (93.9, d 26), AFTERTOUCH moved to (192.1, d 26), legends outward (the breaks sit inboard).
  - FOLD I/O: power switch + 6 jacks in the lid's far wall (x 66, then 90–215 at 25 pitch). USB-C (y 94) + TRS MIDI out (y 83) in the base's right end face. The lid end faces carry only the stays, so the stay FLAG on D and E is now marked resolved.
  - Daisy Seed is in the base, rear right (`Fold.fx_shield()` now returns base coordinates). It's gone from the lid plan and exploded view; a far-wall I/O board is drawn instead.
- **FLAG (systems): there's no room for PARA's legend in the flat concepts.** It's drawn bare, with a flag on sheet B. There's 2.3 mm between its nut and OSC 2's legend, and the break is 3 mm to its left. The three words need ≈ 15. It needs a new spot or fewer words.
- ~~Open (systems): rev 5.6 lists no MIDI IN~~: wrong, rev 5.6 adds it; drawn in S2b.
- **Perspective views (A):** in the 3/4 views, front knobs still hide parts of some back-row legends. Short labels reduce this but can't remove it, and the top and front views are exact.

## Where things stand (end of concept round 5, 2026-11-13; new visual designer this round)
- **Active: HUSH, FOLD (two variants), ONE SHEET.** TYPE CASE and HYMNAL are paused; UNDER GLASS was killed in round 2.
- **Round-5 sheets (300 dpi A3, tag "round 5")** are drawn to systems' round-5 final (common 7.1) + DRIFT (fold 5.4) + standing lid (fold 5.5). Every PNG was opened, and the back rows were checked in 1:1 crops.
  - `hush/` and `one-sheet/`: `mock-A-look`, `mock-B-real-size`, `mock-C-construction`, **`mock-D-front` (new)**. These overwrite round 4.
  - `fold/`: `mock-A-look-105/113`, `mock-B-real-size-105/113`, `mock-C-construction-105/113`, **`mock-D-front-105/113` (new)**, **`mock-E-standing-105/113` (new)**. Round 4's unsuffixed FOLD sheets are still in the folder; delete them once the director has seen round 5.
- **Sizes drawn:**
  - ONE SHEET 276 × 180 × 24, whites 26.5;
  - HUSH 290 × 187 × 25.5 (186 until the S1 pass);
  - FOLD-105 halves 286 × 108 (open 218 incl. the 2 mm seam);
  - FOLD-113 halves 286 × 129 (open 260); closed ≈ 50.1.
- **Docs rewritten:** `concepts/<hush|one-sheet|fold>/how-it-looks-and-feels.md` (round 5). `concepts/common-looks-and-feels.md` is still round 2/3, so treat it as superseded; it needs a refresh or a banner.

## Generator (round 5): `concepts/_mock-src/`
- `r5.py`: geometry and renders. Run `python3 r5.py [jobs]`; all ≈ 45 jobs take ≈ 8 min (`--test` for low-res; `python3 r5.py r5_fo105*` runs a prefix).
  - **The layout is read live from `fold_r5_check.py`** (the `F.play`, `F.v1`, `F.v2`, `F.fx` lists, breaks `F.vb_play`, `F.vb_fx`), shifted by dx (ONE SHEET −5, HUSH +2, FOLD 0). When systems edits the checker, re-render; no coordinates are duplicated. Only the section-name spots and the HUSH/FOLD text positions are hand-placed.
  - It reuses r4 primitives (`pebble`, `pg_layers`, `knob_black`, `halo`, `feltfill`, `woodfill`, `top4`, `shot4`).
  - New pieces:
    - `item5` (TYPE rotary kind "y" with `type_fan`; TAP kind "b" with `tap_cap` in 3 styles: peg / acryl / proof);
    - `keys_raised` (skirt option);
    - `one_sheet(edge)`, `hush(edge)`, `hush_body(edge)` (r 4 front via hull with side pucks at y 44);
    - `class Fold(v)`, which holds the variants' depths, lid face, exploded, `fx_shield()`, `stays()` and `model("stand")`;
    - **`shot_ortho()`**: exact-scale orthographic front / right-end elevations, cropped by magenta markers. The ortho distance must be (frame height + 20) / (2·tan 11.25°) with the camera centre on the object plane.
- `sheets_r5.py`: sheets A–E. Run `python3 sheets_r5.py [hush one-sheet fold105 fold113] [A B C D E]` (≈ 20 s).
- Round-4 code (`r4.py`, `sheets_r4.py`) is untouched.

## Decisions this round, and why
### All three
- **Layout:** systems' balanced, mirrored layout + DRIFT, drawn exactly (back row DRIFT | ECHO TYPE, TIME | REVERB DECAY, TYPE | VOLUME; TAP at the end of the PLAY row).
- **Type names:** the TYPE switches' detents fan over the top at −60 / −20 / +20 / +60°, and the four names sit in a straight row above, each over its detent. The inner two are lower and the outer two higher, so they never collide.
  - Echo: tape / bbd / clean / ping-pong. Reverb: plate / hall / spring / shimmer.
  - First try: a wide fan, −90…+90. It collided with break rules and neighbours.
- **TAP is made of the key material** in each concept (a maple peg in HUSH, white acrylic in ONE SHEET, a cream cap in a black bezel in FOLD), because it's played in rhythm like a key.
- **Tempo feedback (proposal, not in systems' spec):** the status light flashes the tempo 4 times after a tap. No second light (H7).
- **Key mechanism is drawn on every D sheet:** switch, stem, top, magnet / Hall, rest vs pressed. Stated plainly: a ≈ 3 mm button (HUSH: 2.5 to the felt collar), not a pivoting key.
- **Front views (D):** exact 1:1 orthographic renders from the same models. For the flat concepts: front A, front B, right-end A and B, then the edge and press.

### HUSH
- Edge A drawn as the hero (r 4 front, pegs y 13.5); B in the close-up and on D.
- **TYPE tags grow a bib** behind the knob that carries the type names, because felt can't hold a fine mark (principle 4).
- **The plinth outline was tried and burned:** it crossed MIXER, and the back row's rules already define the row.
- MIXER heading at (145, 134.6), size 2.0, in the clear strip between the tags.
- Random draw: "Look closely at the most embarrassing details and amplify them" + architecture (plinths). The awkward detail: pegs stand 6.5 mm proud, not 2–3, so the peg is leaned into, and TAP becomes a peg.

### ONE SHEET
- **Two finishes only:** smooth, plus rings round every rotary (r 7.75 → 9.25; CUTOFF 10.9 → 12.5), drawn at 1.1 pitch (2.5× coarse, labelled), with a true-scale swatch in the A inset.
- New principle 2: **"Still water, ripples where it turns"** (if it turns, it ripples; TAP, toggles, lights and the stick are smooth).
- Legends and names in one dark (#2e2924), because one swap means one colour.
- Random draw: "Water" + weaving. Neighbouring ripple fields never cross: 1.5 mm of smooth between them.
- Edge A as the hero; B on the A close-up and D.

### FOLD
- **Balance made visible (new principle 3, "Three columns and one axis"):**
  - the column rules x 101.5 / 184.5 run on both pickguards and line up across the seam;
  - everything single sits on x 143 (EMPHASIS, status, grille, the back-row centre break, the name lozenge);
  - a brass pin on the front rim and a tick on the far rim mark the axis.
- Signal map and row-end words burned. Random draw: "Bridges — build / burn" + sailing rigging (a boat's centreline is marked).
- **FOLD-113 is drawn honestly as failing the gap** (75.45 vs ≈ 60); every 113 sheet says so.
- **Digital module (flagged, purple dashed, sheet C plan + exploded):** the owner switched to a **Daisy Seed** (51 × 18, codec on board), so the FX shield is gone. Drawn under the lid's left far strip (x 18–69, d V2 + 12 … + 30), left of DRIFT.
  - Footprints [CALC]: Pico + shield ≈ 2,170 mm² vs Daisy ≈ 920, so the lid board gains area. My earlier "≈ 1,100 mm² short" finding is void. Eng confirms lid vs base.
- **MIDI OUT (owner):** added beside MIDI IN on every jack edge. HUSH: 8 ports at 19 pitch, x 76–209. ONE SHEET: 8 at 15.5 pitch, x 152–260.5. FOLD: lid right wall, 8 at 10 pitch, d 15–85.
- **AFTERTOUCH toggle (owner; systems hadn't placed it, so the placement is mine, pending systems):** VELOCITY's column. Flat concepts at y 111.5 between the voice rows (FILTER MOD / AFTERTOUCH / VELOCITY); FOLD at d 26, just behind FILTER MOD (mid-band would land on CONTOUR AMT closed). All checked against the checker's rules. Cost: one empty mirror slot. Labels: AFTERTOUCH to the left of its toggle; in the flat concepts VELOCITY and SOURCE labels go above their toggles.
- **Key lift:** `R5_KEY_LIFT` env var (default 0) raises keys / pegs for eng's possible 1–2 mm compliant aftertouch layer.
- **FLAG (systems): FOLD's right stay groove (d 30–82.4, z 2–10) runs through the lid-wall jacks (d 15–85, z ≈ 8).** Flagged on D and E. Fix options: jacks up the wall, I/O to the left wall, or relocate the right stay.
- **Standing lid (sheet E, both variants):** 105° on two brass stays (3 × 8 × 52.4), drawn from systems' rev 5.5.
  - My renders put the tip at y 161 (105) / 182 (113), ≈ 53 behind the base, with the stay at ≈ 68° to the table (systems: 162 / 183, 54, 65°; the difference is the rubber tip's height).
  - Stowed, the stays are brass lines on the lid's end faces in every view.
  - Finish proposal: brushed + waxed brass, domed rivet pin, 6 mm finger scoop.
- Knuckles narrowed to 10 wide (systems).

## Director (last scores: round 4) and status
- HUSH 9; FOLD 7 (blocker: mid-deck gap, now fixed in 105: 54.45 ✓); ONE SHEET 8 (blocker: the coupon, still unprinted; it's now two patches).
- The director hasn't scored round 5 yet.

## Findings to pass on
1. **Systems/eng:** the tempo flash on the status light (or no tempo feedback at all).
2. **Systems:** ONE SHEET's MIXER heading is crowded (≈ 3 mm to the REVERB DECAY label). Options: shorter labels (TIME / DECAY), or drop the VOICE headings.
3. **Eng:** FOLD Daisy Seed placement (above); standing-lid weights and boss strength.
3a. **Systems:** FOLD right stay vs the jacks (above).
3b. **Systems:** accept or re-place AFTERTOUCH (mirror cost); add it to the checkers. **Eng:** the FOLD-105 bridge under it; AT positions; key lift.
4. **Maker:** the HUSH corner blocking test now needs the r 4 front edge (option A).
5. Renders: OpenSCAD's light makes front faces and the standing lid's plate read darker than they are (the cream plate looks grey). The colours in the docs are the intended ones.

## Open questions
1. **Owner:** key edge A or B (HUSH, ONE SHEET; my lean is A for both); FOLD-105 vs 113 (recommend 105).
2. **Systems:** cream KN1250 on A-5518 round-shaft pots (HUSH, ONE SHEET), still unruled; FOLD's brass axis pin (drop it if it reads fussy).
3. Maker tests: the ONE SHEET coupon (smooth + rings); a pressed-felt offcut; a wood-fill walnut swatch; the HUSH corner (r 4 + r 12).
4. Refresh or retire `concepts/common-looks-and-feels.md`.

## What comes next
- The director scores round 5 (HUSH, ONE SHEET, FOLD-105; FOLD-113 is context).
- Eng confirms the Daisy placement; systems resolves the stay/jack clash. Redraw with `python3 r5.py r5_fo*` once the numbers change (stays: `Fold.lid()` and `Fold.stays()`; jacks: `Fold.lid()`).
- After the owner's pick: write "How it looks and feels" in `handoff.md`:
  - finishes;
  - type sizes (the docs list them);
  - every state with light colours and timings;
  - the knob and cap part list;
  - stay and finger-scoop details for FOLD.
