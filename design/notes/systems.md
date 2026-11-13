# Systems designer notes — Little D

# BRANCHES — coverage check (2026-11-13): CHAMBER 9, RAIN 9 (pending R1)
- Wrote `design/branches/concepts/{chamber,rain}/coverage.md` against jobs rev 5 (J1–J28). Re-ran `branch_check.py`: 0 fails, 0 legend/tick collisions in both.
- **CHAMBER: no unsupported jobs.** Weak spots: J22 park parts (sun, outdoor level, battery length, stays on soft grass), J11 (plug shank fit, relief fill, big printer), J4 paper card. The hinge slot (v1.1's J6 weakness) is closed by the spine.
- **RAIN: no unsupported jobs, conditional on R1** (it only touches J20's look). Weak spots: bottom speaker (J5 / J15 / J22d), bag with exposed pegs (J6, owner-deferred), one-piece print (J11), sun/battery (J22c/e), J18 not taken (a free keyhole slot would fix it).
- Next: re-run the checker after R1's re-render if any geometry moves; answer the builder after the owner picks.

---

# BRANCHES — round 2 geometry (2026-11-13): CHAMBER 8, RAIN 7, BUTTERFLY retired, DIPTYCH killed

## Where things stand
- Director steer + scores: `design/notes/director.md` top, `design/scores.md`. Live: **CHAMBER, RAIN**.
- `branch_check.py` now has:
  - **§7:** instruments `rb.py`, records every txt and tick on the playing faces, measures text ink boxes with OpenSCAD (cache `/tmp/branch_check_textbox.json`), checks legend-legend ≥ 1.5, legend-tick ≥ 1.0, legend-control ≥ 1.5, tick-control ≥ 0.5, and tags clashes also in locked v1.1;
  - **§8a:** the slot; **§8b:** the push-outs.
  - TOTAL fails 0; the collisions are listed, not failed. v1.1 checkers still 0.
- **Kalam Bold installed** (`~/.local/share/fonts/kalam/`, from raw.githubusercontent google/fonts; jsdelivr and gstatic are blocked). The checker substitutes it for rb.py's stand-in. The visual designer can render with it now.

## Findings (why)
- **CHAMBER slot is real** (v1.1 has no lid hinge wall, because of R4): 21.9 × 266. A rigid wall or lip breaks R4 open.
  - **Fix: a flexible book spine**, 21.9 wide, bookcloth/leather on 0.8 TPU, glued along the base rear-top edge and the lid hinge-top edge.
  - It folds into the 2 mm seam gap open (loop ≈ 9.9 deep) and is taut closed.
  - Eng: shared gap with the ribbon loop (x 176–227); flex life.
- **Push-outs at d 90:** clear the d 96 screws (27.8) and the pipes, but land behind the TYPE rotaries' tails and next to the I/O board. Rejected.
  - Proposed: façade pitch 8.75, holes Ø 4 as the mouths of pipes at x 108 / 178 (d 28.3), on the bare board bridges like v1.1.
- **Collisions (Kalam):**
  - CHAMBER: 17 near-misses, 0 overlaps, 9 inherited. New: free/sync vs knobs (move 0.5 behind), the ±50° ticks under the toggle nut (drop), RANGE "lo"/"2'" vs "range", VEL above-legend, REVERB fan.
  - RAIN: one new hit (±50° ticks, 0.05); the rest inherited. The director's RAIN legend clashes are gone in today's model.
- **Render understates toggle nuts** (Ø 6 drawn vs ≈ 9.2 spec): ticks look clearer than they are.
- **RAIN ripple decay** must be built from printable steps: 2 depth levels (0.2 layers), groove ≥ 1 line, so the decay comes from ring spacing opening toward the seam. Section bands ≈ 3× via power weights. A 0.6 pitch needs a smaller nozzle (UNVERIFIED at Vector Space).

## Open questions
- Eng: spine vs ribbon loop; TYPE rotary body size (RS16211); flex life; nozzle availability.
- Visual: accept pitch 8.75 + mouth push-outs; the spine's colour; Kalam re-render; the tick and legend fixes in chamber rev 2 §R2.3.
- Owner (via director): reversed keys (fallback geometry identical), +2.6 closed, TIME's dead 15°, park session, clock out, the book.

## Next
- Re-run `branch_check.py` §7 after the visual designer's round-2 renders. Then the coverage check vs jobs rev 5 for any concept scored 9+.

---

# BRANCHES — concept turn 1 (2026-11-13): jam closed, 4 concepts started

## Where things stand
- Jam closed (director turn 3): **CHAMBER (FOLD), RAIN (ONE SHEET), BUTTERFLY (ONE SHEET), DIPTYCH (FOLD)**. Killed: PIERCED, GROUND (donors: status-light hood, high-contrast legends, finger pocket, "bottom as designed as the top").
- **Owner decision 11:58: echo sync option "B"** (FREE / SYNC toggle by TIME). Recorded in `design/owner.md`; `echo-clock.md` rev 1.1.
- `design/jobs.md` **rev 5**: J20–J28, F13–F15 and new state rows added; rev 4 kept.
- Concept files (systems, first): `design/branches/concepts/common-how-it-works.md` + `{chamber,rain,butterfly,diptych}/how-it-works.md`.
- Checker: `design/branches/concepts/branch_check.py` (imports v1.1 `fold_r5_check.py` read-only). TOTAL fails 0, plus one expected finding (DIPTYCH tips with cords alone). v1.1 checkers still 0.

## Decisions and findings (why)
- **FREE / SYNC:** ONE SHEET (128.0, 132.7), FOLD lid (133.0, d 70.6). The windows are ≈ 1 mm deep (control rules), so it's the only legal spot.
  - TIME's legend was right under the toggle (v1.1 legends sit in front of their knobs), so TIME and DECAY legends move behind their knobs.
  - The throw changes to left / right with words beside it (the visual designer's fore / aft has no room for words).
  - ONE SHEET's MIXER heading moves to y 136.
  - TIME's scales are printed over ±135° with a firmware clamp (at ±150° the end ticks hit the nut).
- **BUTTERFLY:**
  - the joint must be at y ≥ 164.9 → 165 (y 160 cuts four fan names);
  - jacks can't go through the wood (plug reach, irregular face), so the walnut becomes a 6 mm top in a rebate overhanging the printed rear wall (tabletop over apron);
  - jacks stay as v1.1, legends are lasered into the walnut;
  - the leaves meet end-to-end (grain along x), so it's a butt match and the butterfly really carries it.
- **RAIN pegs:** a 14 mm felt washer keeps 276 width (HUSH's 19 mm collar needs +5, not +8). Strip C limits the whites to y ≈ 14.
  - No grooves, so the print split at x 122.5 has nowhere to hide: print in one piece on a 350 bed (UNVERIFIED), or split along a Voronoi seam.
  - A power-off sound is impossible (hard switch); a power-on "drop" is free.
- **CHAMBER:** pegs need +2.6 mm of lid wall → closed ≈ 52.7 (director estimated +4).
  - Façade: 25 pipes, L 66 → 16.5, tower pitch 10, impost at d 18 on the d 12 screws.
  - v1.1 front lid-back feet (d 30) land on pipes → move to d 6.
  - The nameboard strip above the keys is ≈ 3 mm tall → use the lid lozenge.
- **DIPTYCH:** cords alone tip at 0.8 N (model matches v1.1's 6.8 N with stays: 6.9). Needs base feet reaching ≥ 45 mm behind (proposal 59 → 6.9 N).
  - Latitude cord at s 100 (director's) passes 24 mm above the base top in the stick hand's zone → pick s 60: anchor y 53, 110 mm, 13 N per cord.
  - Feet-before-cords order hazard; proposed interlock slot.
  - Red + black fills = two swaps.

## Director's objections so far
- None on systems' concept files yet (they're new). From turn 3: CHAMBER costume watch; DIPTYCH is cut first if it can't separate from CHAMBER.

## Open questions
- Owner: CHAMBER reversed keys; pegs' cost (now +0 width on ONE SHEET with washers, +2.6 closed on FOLD); park session length; tapped tempo out as clock; the furniture book's title.
- Director: DIPTYCH cords + feet (one more part) vs keep v1.1 stays and lose the cords.
- Visual: accept the left / right throw and moved legends? TIME dial numerals in the tight annulus; MIXER heading move; façade feet move; BUTTERFLY joint at 165.
- Eng: strip C vs the main / base board line with pegs (both peg branches); walnut button plugs; engraved fill on wood-fill PETG; cord creep; feet pivot in PETG; Voron 350 at Vector Space; toggle lever height; outdoor speaker level; LiPo in sun.

## Next
- Visual's concept turn (looks, renders, the "must prove" lists).
- React to the visual designer's changes to how things work. Then, for each concept the director scores 9+: a coverage check against jobs rev 5 (J1–J28), before the owner sees it.

---

# BRANCHES (started 2026-11-13): personality, a whole point of view, the park, MIDI-synced echo

## Where things stand (after jam turn 1)
- Task: owner's 2026-11-13 11:47 entry (`design/owner.md`). Branched creative rounds from the v1.1 locks (never edited); new concepts go in `design/branches/concepts/`. Shared brief: `design/branches/BRIEF-CONTEXT.md`.
- I took jam turn 1 (`design/branches/jam.md`): branch jobs B-J1–B-J17, draws, shared structure, flows F13–F15, four branch directions, echo-under-clock spec.
- Draw script: `design/branches/draw-systems.py` (extends the old list with furniture / instruments / tools / art / emotions / park moments). Two first-run oblique cards repeated earlier jams by chance; redrawn excluding all earlier cards. Draws are recorded in the jam.
- Echo spec: `design/branches/echo-clock.md`.

## Decisions so far and why
- **The board is the constant; the outside is the branch** (B-J17: he may pick ONE SHEET or FOLD late, "internals are probably the same"). Branches change enclosure, key tops (bought), underside, handle/hole outside the board outline, graphics, jack wall; not rows, Daisy, mux plan.
- **Sync on/off = "does TIME read in ms or beats?"** Option B (FREE / SYNC mini toggle, TIME with two machine-marked scales, 9 divisions) recommended over Option A (automatic + hidden hold-TAP+TIME gesture). B is a new control → **owner decision, not settled.** Under clock TAP has no tempo job; clock lost → hold last tempo; TAPE/BBD glide, CLEAN/PING-PONG crossfade; 500 ms loss timeout; USB wins over TRS while ticking (proposal). Feedback on the one status light (H7); a lit TAP is the alternative (director's call).
- Pegs are portable to any branch (HUSH's bought button plug + arm), but stand ≈ 6.5 proud: they can't meet R4's 3 mm, and on FOLD they cost closed height.

## Branch directions proposed (visual may reshape or kill)
1. BUTTERFLY (ONE SHEET; furniture): true playing edge, live rear edge, butterfly key across the x 122.5 print seam, French cleat to hang. Grows ≈ 10–15 mm deep.
2. CHAMBER (FOLD; organ): RANGE in organ feet as heritage, reverse keyboard in walnut/maple pegs, grille as pipe façade on the standing lid. Pegs vs closed height open.
3. PIERCED (HUSH drawn, show on ONE SHEET; carried tool): 40 mm through-hole at the right end to carry/hang, throws light; one brass ring. Costs ≈ +55 mm length. Carry handle, not a play grip.
4. GROUND (either; posture): designed wedge underside for playing on grass, sun-first status light and legends. Speaker path conflict on ONE SHEET.

## Director's objections
- None yet (turn 1).

## Open questions
- Owner: sync Option A vs B; tapped tempo as clock out?; park session length (FOLD-105's ≈ 11 Wh → ≈ 1.9–3.9 h [CALC]); reversed key colours OK (CHAMBER)?
- Eng: pegs on FOLD closed height; FREE range 20 ms–2 s and the divisions; tempo limits 30–300 BPM; PLA vs PETG/ASA in sun; mux channel 46 per concept.
- Director: H7 vs lit TAP (sun readability).
- Unconfirmed: which "principles of design" book he means. Don't attribute content to it.

## What comes next
- Visual's turn on the branches; then react to their changes to how things work.
- After the jam: `design/jobs.md` rev 5 (add B-J1–B-J17 marked stated/inferred, F13–F15, sync states table rows), then concepts in `design/branches/concepts/<name>/`.
- Coverage check for each 9+ branch against jobs rev 5 (park jobs and sync jobs included).

---


# UPDATE for visual — FOLD standing angle (2026-11-13). DRAW
- **The lid now stands at 120°** (panel 30° up; was 105°).
- **Brass stays:** shorter, **44.4 mm**, same pivot (d 30). They stand at 60° to the table, with tips 59 mm behind the base.
- Redraw the standing views for both variants. Spec in `fold/how-it-works.md` rev 5.7.

# UPDATE for visual — label pass follow-ups (2026-11-13). DRAW
- **PARA legend (flat concepts):** "PARA" goes to the RIGHT of the toggle, left-aligned 5.6 mm, mirroring AFTERTOUCH's label. Positions read **1 · P · 4**.
  - ONE SHEET: two lines.
  - HUSH: three pressed glyphs stacked beside the toggle at y 109 / 111.5 / 114, then "PARA" (x ≈ 119.5–124.5).
- **FOLD base right end face:** MIDI IN (y 70) · MIDI OUT (y 80) · USB-C (y 90–99).

# UPDATE for visual — pre-build fixes (2026-11-13). DRAW
- **FOLD I/O:**
  - The audio/CV jacks + power switch go to the **lid's far wall** (x 60–230).
  - **USB-C + MIDI out** go in the **base's right end face** (y 80–100).
  - Neither lid end face carries I/O, so the stays stay symmetric. Moving to the left end wouldn't help: both ends have stays.
- **PARA toggle (MONO / PARA / PARA+4)** mirrors AFTERTOUCH:
  - **Flat concepts:** PARA (104.25, 111.5) in the oscillator switch column, AFTERTOUCH where you placed it (ONE SHEET x; HUSH + 7).
  - **FOLD:** PARA (93.9, d 26), AFTERTOUCH moved to (192.1, d 26). Your spot's mirror landed 2 mm from CUTOFF when closed.
- **Daisy Seed:** FOLD base, rear right, on the floor in a board cutout.
- Checkers 0 violations. Legend check for the PARA position words.

# UPDATE for visual — FOLD standing lid (2026-11-13). DRAW
- **One standing angle: 105°** (15° back). Two **brass lid-stays** (3 × 8 × 52.4) are set flush in grooves in the lid's end faces (pivot at d 30, lid back edge). Deployed, they stand at 65° to the table, with rubber tips 54 mm behind the base.
- They're flush when flat and when closed: just brass lines on the ends.
- Draw a standing view for both FOLD variants. Spec in `fold/how-it-works.md` rev 5.5.

# UPDATE for visual — round 5 final + DRIFT (2026-11-13). CHANGE TO DRAW
- **Back row now:** DRIFT | ECHO TYPE, TIME | REVERB DECAY, TYPE | VOLUME. Mirrored, breaks between the groups (FOLD x: 79.5 | 108.5, 128.5 | 157.5, 177.5 | 206.5; breaks 94 / 143 / 192; ONE SHEET −5, HUSH +2).
- **PLAY right now:** REPEATS, ECHO MIX, REVERB MIX, **TAP** (at the old VOLUME slot).
- Sizes unchanged. Checkers 0 violations.

# UPDATE for visual — round 5 final (2026-11-13). DRAW TO THESE NUMBERS; supersedes the two round-5 blocks below where they differ
- **FX = full 8** (owner). Rule: **amounts in front, kinds and times behind.**
  - **PLAY right:** REPEATS, ECHO MIX, REVERB MIX, **VOLUME (back on the panel)**.
  - **New FX row, a centred "plinth" 23 behind the VOICE back row:** ECHO TYPE, TIME | TAP on the axis | DECAY, REVERB TYPE, with its own breaks ±13 round TAP.
  - Side wheel and wall toggles dropped.
- **Coordinates:** common rev 7.1 (flat concepts), FOLD rev 5.3.
- **Checkers:** `flat_r5_check.py` and `fold_r5_check.py`, 0 violations, mirror 0.00 in every row.
- **Sizes:**
  - ONE SHEET **276 × 180**;
  - HUSH **290 × 186**;
  - FOLD-105 halves **286 × 108** (open 216, gap 54.45 ✓);
  - FOLD-113 halves **286 × 129** (open 258, **gap 75.45 ✗**). Recommend FOLD-105; show 113 as the reason.
  - Closed FOLD ≈ 50.1; heights unchanged.
- **Key edge A/B:** unchanged in all three.
- **ONE SHEET finish:** rings round all rotaries (incl. the TYPE switches), smooth elsewhere.
- **Open (eng):**
  - where FOLD's FX shield goes (the Pico is in the lid; in the lid it would make FOLD-105 D ≈ 113);
  - the base mux is at 33/32;
  - TAP and thumb parts;
  - RS16211 height.

# UPDATE for visual — round 5 HUSH/ONE SHEET (+ FOLD rev 5.2), 2026-11-13. DRAW TO THESE NUMBERS
- **One layout for all three:** FOLD rev 5.1's balanced layout, shifted.
  - ONE SHEET x = FOLD − 5 (centre 138, breaks 96.5 / 179.5); HUSH x = FOLD + 2 (centre 145, breaks 103.5 / 186.5).
  - Rows y 68 / 100 / 123. Coordinates in `concepts/common-how-it-works.md` rev 7.
  - Checkers: `_mock-src/flat_r5_check.py` and `fold_r5_check.py`, 0 violations, mirror 0.00.
- **FX (owner: echo + reverb):** the PLAY row's right section = ECHO TIME, ECHO REPEATS, REVERB, FX MIX (4 slots).
  - **VOLUME → a thumbwheel in the right wall** (FOLD: the lid's right wall). That's the trade.
  - The FX MODE toggle goes on the rear wall (FOLD: lid right wall).
  - For 5 knobs: a dual-concentric MIX, or a centred third row (flat concepts only).
  - The FX circuit grows the flat bodies at the back (≈ 276 × 178, 290 × 184, ESTIMATE). In FOLD it goes on the base board (no depth change).
- **Key edge A/B:** both raise the keys to 2.5 above the panel.
  - ONE SHEET: A = skirted keys to the front, wall at z 17.5, 4 mm shadow slot; B = lip at z 25.5, 1 below the keys.
  - HUSH: A = front round-over r 12 → r 4, pegs forward 6 (y 13.5); B = the round-4 r 12 brow. Pegs are 6.5 proud by mechanism.
  - FOLD: already B (4 mm rim, keys 1.9 proud).
- **ONE SHEET finish:** only rings (round every rotary, r 9.25; CUTOFF 12.5) and no texture (everything else). Sections read by the grooves and black names.
- **jobs.md rev 4:** J19 echo + reverb.
- **Open:** the reverb chip and control count; the thumbwheel pot part; FX board area; the HUSH r 4 front edge in the blocking test.

# UPDATE for visual — FOLD round 5 (rev 5.1, 2026-11-12, new systems designer). DRAW TO THESE NUMBERS
Spec: `concepts/fold/how-it-works.md` rev 5.1. Checker: `concepts/_mock-src/fold_r5_check.py` (0 violations both variants; mirror offset 0.00).

**Two variants (owner: "Show me both"):**
- **FOLD-105:** halves **286 × 106** (eng's 105 rounded down left the lid board 112 mm² short). 4 × 952540 slim cells, 11.1 Wh. Open 212. Rows PLAY → V1 → V2 = **52.45 / 52.45**.
- **FOLD-113:** halves **286 × 114** (113 was 26 mm² short). 2 × 50 × 60 cells, 22.2 Wh. Open 228. Rows = **60.45 / 68.0**: the 52 mm cell window forces V2 back.
- Closed ≈ 50.1 for both.

**Gap fix:** V1 sits at lid **d 14.45** and lands closed on the base's empty **landing strip** behind the PLAY row. V2 lands over the keys. The PLAY row lands under the lid **band** between V1 and V2, and the band holds the cells + a **speaker centred on x 143**.

**Balance (owner: "doesn't feel balanced"):** FOLD has its own x layout now.
- Every row mirrors about **x 143**.
- **The same breaks on both halves, x 101.5 / 184.5**, giving three columns: PITCH under OSCILLATORS, FILTER under MIXER, ECHO+OUT under CONTOURS.
- **Base PLAY y 68:**
  - stick 25, MOD 47, **TUNE 67**, GLIDE 87
  - CUTOFF 119, **EMPHASIS 143**, CONTOUR AMT 167, lights (131, 81) / (155, 81)
  - **FX TIME 199, REPEATS 219, MIX 239**, VOLUME 261
- **Lid, both rows at x:** 23.5 / 43.5 / 63.5 / 83.5 | 109.25 t / 123 / 143 / 163 / 176.75 t | 202.5 / 222.5 / 242.5 / 262.5 t
  - **V1:** RANGE 1–3, FREQ 2 | OSC MOD, OSC 1, OSC 3, MOD MIX, FILTER MOD | F A/D/S, KBD CTRL
  - **V2:** WAVE 1–3, FREQ 3 | OSC 3 CTL, OSC 2, NOISE, SOURCE, VEL | L A/D/S, DECAY
- No holes.

**Moved:**
- TUNE → base;
- MOD MIX, OSC MOD, FILTER MOD, KBD CTRL, VEL → lid;
- ladder → base (EMPHASIS beside CUTOFF, eng).

Osc 3 is off the ribbon; the 40-way carries 21 signals + FX reserve pins 17–19.

**Other:** knuckles narrowed to 10 wide; section names black; name inlay centred in the far strip; signal map optional, in the band.

**Open:** eng (the echo circuit and mux count, TUNE analog?, ribbon order, the lid IDC 1.2 mm in front of V1, the 105's 10 mm board bridges, the lid-board margins +150 / +236 mm²); maker (10 mm knuckle lugs, measure the cells); owner (105 vs 113; the moved controls; V1 7 mm inside the back slot; a 4th FX control needs a trade).

**Next:** visual draws both → director scores → if 9+, re-walk `fold/coverage.md` (still round 4) and add the echo job to `jobs.md` once eng scopes it. HUSH and ONE SHEET still need an FX home (common layout, separate pass).

# UPDATE for visual — internal battery in all three (rev 7.2, 2026-11-12). OVERRIDES 7.1 WHERE THEY DIFFER
- Owner requires an internal battery.
- **ONE SHEET** (276 × 170, unchanged): bay x 20–150, y 100–166, 11.4 clear, under the main board; a 1.5 mm pocket in the back panel. Access: back panel off.
- **HUSH** (290 × 176, unchanged): bay x 27–157, y 106–172, same build.
- **FOLD: halves now 286 × 116** (closed ≈ 50 thick; open 286 × 234).
  - Bay in the lid band: x 22–152, d 3–55, 10.6 clear.
  - Lid VOICE rows at d 68.65 / 91.65; EMPHASIS at lid (169, d 48); speaker x 205–265, d 2–32.
  - Base: a flush strip y 82–112 behind the PLAY row.
  - The base can't take a cell without making it ≈ 67 closed.
- **Cell for eng:** 2 pouches ≤ 9.5 × 50 × 60 (≈ 3000 mAh each, ≈ 22 Wh); confirm the part and the series/parallel wiring.

# UPDATE for visual — eng round 4 applied (rev 7.1, 2026-11-12). DRAW TO THESE NUMBERS
Source: `/home/claude/model-d/eng/round4-answers.md`. Files: common rev 6.1, one-sheet rev 4.1, hush rev 6.1, fold rev 4.1 (a box at the top of each).
- **ONE SHEET 276 × 170. HUSH 290 × 176.**
  - The main board needs ≈ 268 × 115, so the bodies grow **at the back only**. Keys, the PLAY row (y 68), the break (85.4) and the VOICE rows (100 / 123) are unchanged.
  - The new ≈ 30 mm behind the back row is a **flush rear band**: name/wordmark, jack legends; no controls.
- **FOLD: halves 286 × 100** (were 86). Closed 286 × 100 × ≈ 50; open 286 × 202.
  - Base: unchanged up to the PLAY row, then a flush 18 mm strip of white plate behind it.
  - Lid VOICE rows at **d 52.65 / 75.65** from the hinge edge (open y 154.65 / 177.65).
  - **EMPHASIS moves to the lid at (169, d 32)** = open (169, 134), straight behind CUTOFF. The base PLAY row keeps an **empty slot at x 169**; closed, EMPHASIS drops into it.
  - Rectangular speaker grille at **x 205–265, d 2–32**; name inlay in the band's left part.
  - **No battery** (USB power bank).
- **Knobs everywhere: 18T push-on, 14.5 Ø × 13.5 tall** (T18 spline pots). KN1250 is out (set-screw, round bore). Knob tops rise ≈ 3 mm: ONE SHEET ≈ 37.5, HUSH ≈ 39, FOLD unchanged (already black 18T). Cream 18T for HUSH/ONE SHEET: availability unverified; pick a stocked colour or flag it. The WAVE panel hole is 9.5.
- **Unchanged:** all x coordinates; HUSH edge radii and corners (rear R 44 now on a deeper body); FOLD heights; screws only on hidden faces.
- **Eng items left:** measure the WAVE rotary and toggle body heights (may be > 7 mm, affects panel z); FOLD ribbon flex test; capeline sourcing and the HUSH corner test.


# UPDATE rev 7 — concept round 4: HUSH, FOLD, ONE SHEET only (2026-11-12, new systems designer)

**Owner this round (verbatim in `owner.md`):**
- Pause all but HUSH, FOLD, ONE SHEET.
- Unibody, screws from the back.
- HUSH organically rounded so the felt wraps seamlessly.
- FOLD back to walnut + white ("Proof").
- Keys right to the edge, knobs "logically split", maybe narrower.
- No case work.
- Then three mid-round notes:
  - (a) FOLD = "hollowed out block … face plate with filters and keys installed in, like a guitar with pickguard", rounded edges with flat top and bottom.
  - (b) "screw placement is malleable but yes screw from back is ideal".
  - (c) "One sheet and hush feel like the controls are installed from behind and then a panel screwed in on the back".

**Diagnosis:** the "space in front of the keyboard" was FOLD's 38 mm palm rest (the lid needed 106 for three rows; the base matched it), and in the flat concepts the empty 26 mm band at y 52–78 plus rows set too far back. Both came from the knob layout.

**Decisions (files updated: `concepts/common-how-it-works.md` rev 6; `hush/how-it-works.md` rev 6; `fold/how-it-works.md` rev 4; `one-sheet/how-it-works.md` rev 4; coverage.md ×3 (one-sheet's is new); `jobs.md` rev 3):**

1. **Layout = PLAY row + VOICE** (common §1–2, script-checked, 0 rule violations; checker kept at `concepts/_mock-src/layout_r4_check.py` (ONE SHEET frame; HUSH +7, FOLD +5)).
   - **PLAY row y 68**, nearest the keys, pitch → tone → level:
     - BEND 20, MOD 42, MOD MIX 62, OSC MOD 78, FILTER MOD 92, GLIDE 108
     - break 122.5
     - CUTOFF 140, light (152, 79), EMPHASIS 164, CONTOUR AMT 188, KBD CTRL 204, VEL 220
     - break 228
     - VOLUME 243, status 262
   - **Horizontal break y 85.4.**
   - **VOICE y 100 / 123:**
     - TUNE 18.5; VCO columns 38.5 / 58.5 / 78.5 (RANGE front, WAVE back); FREQ 98.5; OSC3 CTL 114.5 (back)
     - break 122.5
     - mixer 137 / 157, SOURCE 173
     - break 181
     - contours 197 / 217 / 237 (filter front, loudness back), DECAY 253
   - Why: stick and MOD leave the key zone, so the body is keys-wide (276) and keys run to the front edge; reach stick → CUTOFF 196 → 120 mm; in FOLD the PLAY/VOICE line is the fold line. Cost: the strict Model D panel sentence (TUNE moved into oscillators).
2. **Sizes:**
   - ONE SHEET 276 × 140 (frame).
   - HUSH 290 × 144 (+7 x; 12 mm round-over needs pegs and knobs on the flat).
   - FOLD 286 × 86 per half, closed ≈ 50.1, open 286 × 174 (+5 x; lid side rims need 12 mm from knob edges).
3. **ONE SHEET / HUSH build:**
   - Closed-top shell; everything loaded from underneath.
   - Pots and toggles board-mounted, no top nuts: the board is screwed UP to 10 bosses, with anti-rotation slots.
   - Strip C screwed up; key tops, pegs, knobs and the stick cap fitted last from above.
   - Back panel 8 × M3 from underneath.
   - I/O board inside the rear wall (no outside nuts).
4. **Print:**
   - ONE SHEET one piece if the Voron is 350 (UNVERIFIED); TAZ 6 280 is marginal; else split at x 122.5 inside the break groove.
   - HUSH split at x 129.5 (felt hides it).
   - FOLD blocks one piece on the big printer (else a visible lap joint at x 127.5); plates split at x 127.5 on break lines.
5. **HUSH:**
   - Plan corners front R 20 / rear R 44; edge r 12 top, r 6 bottom.
   - Pegs centred over stems (eng E-L5 best case), whites y 19.5, sharps y 42.
   - Collars: F3 rings in 1 mm counterbores.
   - **Skin = steam-blocked wool felt hat hood (capeline), the shell is the hat block** (my forced connection: millinery). Flat F3 can't do compound corners: ≈ 25 % excess at the front corners [CALC]. Fallback F3 with 4 hidden corner darts.
   - Felt ends only underneath, clamped by a separate binding ring, so the back panel opens without releasing it.
   - Test: a corner coupon.
6. **FOLD:**
   - Base = keys + PLAY row; lid = VOICE (d 38.65 / 61.65 from the hinge edge) + a 31 mm band holding a rectangular speaker that fires up (PUI ASE06008MR-LW150-R; closes E-L6) and the name inlay.
   - Closed, lid knobs land in front of the base's PLAY knobs (3 mm plan gap): front row over sharps (2.0 mm), back row over whites.
   - Pickguards fixed by 6 × M3 from the back into standoffs, with push-out holes; optional 4 intentional corner screws (owner allows).
   - 34-way ribbon (≈ 19 analog lines: E-L9b).
   - Battery has no home except the band: needs a ≤ 30 mm-wide pouch (E-L10).
   - Back slot 19 mm when closed (no hinge-edge wall, R4), stated.
   - Proof colours = visual's.

**Random draws used:** bookbinding (→ "casing-in" retained from behind; spine idea tried for FOLD's back slot and rejected: an 18.5 mm spine would open an 18.5 mm gap between the PLAY row and the VOICE) and "Remove specifics and convert to ambiguities" (→ one fixing method for all three: screws only on the hidden face).

**Rejected, and why:**
- FOLD with all controls on the lid (base 64 vs lid 82 → a band behind the keys again).
- FOLD long piano tops to fill the base (+$30 stabilisers, noise, doesn't answer "rework the knobs").
- FOLD "Pico row" base (only MIDI-read controls in the base): the lid then can't hold the rest in the 2 rows that closing allows.
- Moving the stick into a 4th row (deeper than it saves).
- 17.5 mm key pitch to fit the TAZ 6 (feel and crosstalk cost).

**Open questions:**
- **Eng:** E-L9 (main board ≈ 268 × 85 in the flat concepts; FOLD base board 270 × 78 + lid board 262 × 50); E-L9b (FOLD analog over the ribbon); E-L10 (FOLD battery); speaker (240, 113) ≥ 30 mm from the ladder; E-L8; #2765 cap in hand.
- **Vector Space:** Voron size, TAZ 6 bed, Gigabot.
- **Owner:** Q-FO3 hidden vs intentional plate screws; closed ≈ 50.
- **Maker:** the HUSH corner blocking test; capeline sourcing.

**What comes next:** the visual designer draws the three on rev 6. Then react to their changes. Then the director scores; for any 9+, re-walk coverage.


# UPDATE rev 6 — FOLD answers to visual r3; coverage (2026-11-12)
- Coverage done: TYPE CASE, HYMNAL, HUSH, FOLD → `concepts/<c>/coverage.md`. **No unsupported jobs.** Shared weak spot: bottom/lid speaker on a lap.
- **FOLD (rev 3), for visual:** 12 mm shift **adopted**. **Stick collision fixed by layout, not a well** (no 6 mm exists under strip C): section I in FOLD = toggles at x 12.5 (mid/back rows; **front slot empty**), knobs at x 27.25 (TUNE/GLIDE/MOD MIX); stick moved to (12, 60). Closed, the empty slot sits over the stick (≈ 15 mm air); TUNE lands over key C, 2 mm clear of the cap in plan (cap ≤ 12 mm, check in hand). **Visual: redraw section I this way.** Floor corrected: 51 drawn / ≈ 47 lean with black knobs / ≈ 46 KN1250 + 1083 / ≈ 44 only with every knob ≤ 10.45 incl. a lower CUTOFF. Black knobs: push-on 18T on eng's knurled 9 mm pots (spline UNVERIFIED); WAVE rotary shaft unknown → set-screw black knob fallback (E-L8).


# UPDATE rev 5 — visual round 2 adopted (2026-11-12)
- **Adopted from visual:** panel z 24 everywhere (eng E-L2: 50 mm Same Sky CDS-5076, 7.6 mm deep; panel 22.7–24.2); knob tops ≈ 35, CUTOFF 36.65. **Visual's layout** (≥ 7 mm knob→break, 3 mm toggle side; breaks x 41.5 / 121 / 172.9 / 264.5; CUTOFF (192, 104); IV columns 192/217/241, toggles 257; V at 280.5; "not in control" light (205.5, 93)); reach ≈ 196. **Print split x = 121** for all printed parts. **FOLD five faceplates** with mullions 0.5 mm below the plate faces (R4 ✓, V-groove tactile). TYPE CASE **sunk rules** (1 mm below face), rim 36.7. HYMNAL box 35 / closed 38 (2–2.5 mm lid pocket over CUTOFF stays). HUSH deck = panel 25.5, printed tag per knob. UNDER GLASS speaker (150, 150), white knobs (no black KN1250).
- **Eng applied:** E-L2 (50 mm speaker, ≈ 54 mm lead-free keep-out, ≥ 30 mm from ladder/expo); E-L4 (window parts ≤ 6.5 mm, heat/digital ≥ 25 mm away); E-L5 (hidden arm works; **felt must not touch the moving peg shank: ≥ 0.5 mm radial, head overlaps the hole, lands on a stationary collar**) — HUSH text fixed.
- **FOLD CUTOFF check:** with visual's numbers (closed plate face 31.5) CUTOFF bottom 19.35 vs D♯ top 19.5 → **collision**. Fix adopted: lid housing +3 mm (axis 25.5, closed ≈ 51), CUTOFF clears by 2.85, KN1250s by 4.55; open geometry unchanged. Alternative: flat sharps + lid +1 → closed ≈ 49. **Visual: redraw FOLD closed at ≈ 51 and the lid walls +3.**
- **FOLD speaker:** needs a ≈ 54 mm board cutout in the lid (E-L6, eng to confirm).
- No disagreements with visual this round.


# UPDATE rev 4 — owner clarified "raised" (2026-11-12). FOR THE VISUAL DESIGNER: redraw against this
- Owner: "what i was talking about was the dividers that got in the way of the knobs" + "That includes the separator between keys and controls too".
- **Rule R4 (common rev 4), binding on every concept:** (a) nothing stands proud of the panel among the knobs: no dividers, walls, ridges or raised plates; separation is flush (engraving, inlay, flush divider edge, colour change). (b) nothing rises between keys and controls: no front rail, lip or separator; white keys within ≈ 3 mm of the panel (strip C on taller spacers: keys ≈ 24, sharps ≈ 26, panel 26–27). Side/rear rims OK, ≥ 12 mm from any knob edge.
- (A brief detour withdrew R4 for a few minutes; the owner's follow-up reinstated it. Files now all say R4.)
- **TYPE CASE (rev 4), visual must change:** interior walls are **flush with the panel** — the egg-crate rises through slots in the panel and is sanded flush, showing as **pale ply edge lines in the ink-dyed floors** (principle 1: "real walls, seen end-on"). **No front rail rising**: the front rail is a flat strip at panel height over the switch backs. **Rim on sides and rear only** (open front). **Cards flat in 2 mm pockets under flush 1 mm clear acrylic strips** in each compartment's front band. Keys at 24. Worst-knob drawing no longer needed. Cost: J16 blind-find advantage lost; J6 weaker at the open front (stated).
- **HYMNAL:** keys 24–26, edging strip at 26 = panel (no step). **HUSH:** birch rings flush in the felt; deck 25 → panel 27 ramp. **UNDER GLASS:** keys ≈ 22–24, glass 24, glass edge is the key edge. **ONE SHEET printed:** keys 24, top surface continues at panel height. **FOLD:** flush by opening flat; no wall on the lid's hinge edge; corner hinges only.


# UPDATE — owner feedback on round 1 (rev 3, 2026-11-12)
- **Owner:** liked TYPE CASE, HUSH, HYMNAL. "The filter sections should not be raised. That would make the knobs hard to access." Wants ONE SHEET as a 3D-printed enclosure; HUSH as printed + wool felt; a new two-part **FOLD** (controls on the lid, white panel screwed into a darker surround), first as 3D-printable (walnut later possible). Printed enclosures now welcome (real-parts rule = touched controls only).
- **R4 flush deck (my rule, in common rev 3):** key surface within ≈ 3 mm of the panel; nothing rises above the panel between keys and controls or along the panel's front; side/rear rims allowed. Done by lifting strip C ≈ 6.5 mm (keys 17.5 → 24; sharps 26) against panel 26–27. FOLD meets it by opening flat.
- **Sweep results:** TYPE CASE front rail was rising to the 38 rim between keys and compartments (that's what the owner saw as "raised") → now flat at panel height; cards lie flat in pockets; rim sides + rear only (bag protection weaker at the open front, said so); (superseded by rev 4: dividers now flush.) HYMNAL: edging at 26 = panel; OK. HUSH: deck 25 → panel 27 ramp; OK. UNDER GLASS: keys lifted to ≈ 22 vs glass 24; OK. ONE SHEET ply version had a step at y 78 (record only).
- **New files/sections:** `concepts/fold/how-it-works.md`; ONE SHEET printed (end of `one-sheet/how-it-works.md`, banner says reinstated); HUSH printed variant (in `hush/how-it-works.md`).
- **FOLD key numbers:** closed 298 × 106; open 298 × 212; base = palm rest (battery under) + keys + hinge band; lid = dark surround (sides + far edge, **no wall on the hinge edge**) + white panel 292 × 99 screwed in + main board + jacks right wall + charger; speaker on lid back (fires down when open) needs an ≈ 80 mm board cutout (**E-L6**). Hinge axis ≈ 24 mm so the lid lies flat at 180° with panel ≈ 16–17 = keys 17.5. **Two end knuckle hinges** (M4 shoulder bolt pins), no full-width barrel (would be a ridge). **10-way ribbon** across: 2 mux outs, 4 selects, sensor 3.3 V + GND, battery ± (muxes moved onto strip C); fallback 2nd Pico + UART (eng E7 design). Closed ≈ 44–48 (over 40: owner choice). Printing: lid, panel and base each split at x ≈ 131–133; panel legends by one filament swap (face-down, first 0.6 mm white with cut-outs, then dark). ≈ $17–23, ≈ 18–24 h printing.
- **Printed ONE SHEET:** idea = "the bed sets the split; one filament, one swap; the file is the drawing". 2 halves at x ≈ 131, panel face down on textured PEI, 2.4 mm walls, 2.5 mm panel, ≈ 20 M3 inserts, laser-cut bottom bridges the seam, ≈ 210–220 g ≈ $5–6, enclosure ≈ $10–13 (cheapest). Sleeve.
- **Printed HUSH:** shell printed fast/plain (felt hides top and seam), sides visible in matte grey; rings printed with the swap (one hard material = the print); ≈ 190–225 g ≈ $4–6; enclosure ≈ $31–41 (felt is the cost).
- **New eng questions:** E-L6 (FOLD speaker cutout), E-L7 (mux outputs over a 60 mm ribbon vs UART fallback). Still open: E-L1, E-L2, E-L4, E-L5.
- **Set now:** TYPE CASE, HYMNAL, HUSH (+ printed), ONE SHEET printed, FOLD, UNDER GLASS (not yet shown to owner; director's call whether it stays in the set).


## Where things stand (round 1 fixes, 2026-11-12)
- Director round 1 (`scores.md`): TYPE CASE 8, HYMNAL 8, HUSH 7, ONE SHEET 6 → **replaced by UNDER GLASS**. Nothing at 9 yet. One fast fix round, then owner.
- Done this turn:
  - `concepts/common-how-it-works.md` → rev 2 (bought Choc keys, H3′ key edge, R2 spacing, VEL toggle, R3 thickness).
  - `concepts/under-glass/how-it-works.md` → new.
  - `concepts/type-case|hymnal|hush/how-it-works.md` → rev 2 with the director's structural fixes.
  - `concepts/one-sheet/how-it-works.md` → marked REPLACED.
  - `jobs.md` → rev 2 (owner answers A1–A7, J17 retired, F3/F9/F10 updated for switches + VEL).
- Visual is redrawing in parallel.

## Big changes since the jam (why)
- **Owner: "I don't want to build custom keys"** → RAIL/FLOAT/COMB out. Keys = 25 Kailh Choc V2 silent + short pressed-on tops (S1, ≤ 1.75u, no stabilisers) + K&J D31 magnet in the top over a flat SS49E (eng `velocity-and-keys-v2.md`). Whites ≈ 30 × 17.2 front row, sharps 16 × 14 rear row +2 mm. White surface z ≈ 17.5. Piano-length tops = +$29.85 stabilisers + plate (variant only).
- **H3 (lip is the spine) retired → H3′ key edge:** where keys meet the body, from the idea; hides switch housings + strip C back; stops snags. TYPE CASE = front rail; HYMNAL = paper-edged strip; HUSH = felt deck; UNDER GLASS = the glass's polished front edge.
- **Owner answers:** nods OK, breadth wanted; bend up and down; standard printed board; show both self-protecting and sleeve; velocity "both, with a switch" → VEL toggle LOUD/BOTH/FILT (eng: AS3360 spare half for loudness, firmware for filter, ≈ +$2); show both flat tops and pegs; thickness ≈ 36 body / ≤ 40 knob tops.

## Shared layout (rev 2)
- 298 × 180 kept (one footprint). Short tops need only ≈ 52 mm key zone → ≈ 20 mm slack band (UNDER GLASS uses it for windows; could shrink to ≈ 160 later).
- KN1250 knobs 14.9 mm; pitch 20 (IV front row 24); front-back 23; rows y 104/127/150.
- Sections x: I 12.5–47.5, II 57–124, III 133.5–168.5, IV 178–256, V 265.5–285.5; 9.5 mm gaps. CUTOFF (188, 104), 1083 hero 20.8 mm. Reach stick → CUTOFF ≈ 193.
- 26 rounds (25 panel + MOD), 7 toggles (incl. VEL in IV mid row, right).
- Panel z ≈ 26–27 assumes thin speaker (E-L2); knob tops ≈ 38.

## Per concept (rev 2 decisions)
- **TYPE CASE:** rim 38 = knob tops, 1–2 mm chamfer; CUTOFF shaft trimmed 2 mm to sit at 38; interior walls **lowered to 4–5 mm** above panel (knob edge is only 3.25 mm from a wall at KN1250 + 9.5 mm gaps); cards 12 mm tall; India ink default, ≈ $10–15; one-sheet making rule optional.
- **HYMNAL (cigar box):** short tops default; lean ≈ $15–20 (oil, cloth-tape hinge on drop front); **drop front held shut by a batten on the lid's underside** (open lid first, then drop front); lid held by 2 magnets in front corners over steel washers; **band dropped**; neutral/black knobs, cream CUTOFF, red only numerals; owner's own label (placeholder). Box 37, closed 40. Jacks right wall.
- **HUSH:** default **felt top only** from one 12 × 12 F3 sheet (offcut = palm strip + spare collars), oiled ply sides/bottom, sleeve; flap option +$32–35; default ≈ $27–30. **Birch only** visible hard material (Delrin gate hidden under a birch plate with a wider slot). **Felt contact at 2.5 mm of 2.8 travel** → after velocity window (≤ 2.1) and note-on (1.96) [CALC]. Jacks moved to rear (no flap root by default). **E-L5:** 1u cap can't carry the magnet 10.5 mm off stem → hidden 1.75u cap with the peg at its front end.
- **UNDER GLASS:** clear 3 mm acrylic glass over the printed board, mirrored engraving back-filled then reverse-painted by the owner; windows over 3 × AS3046 + tempcos (II) and ladder pairs (IV) in the front band y 80–96 (**E-L4**: board layout must put them there); aluminium U-channel rails (1 in rear, 1/2 in front, front rail below keys); acrylic end plates; jacks right end plate; LEDs through unpainted dots; black KN1250. Body 25.4, knob tops ≈ 35 (thinnest); only ≈ 8 mm under the board → speaker ≤ 8 mm deep or board cutout (E-L2). ≈ $26–45, lean $20–30 (over $20 target; named saving: scrap key tops). Sleeve. Weakest J16 (smooth glass).

## Director's objections to watch
- R1 (lip retired), R2 (spacing), R3 (thickness). Breadth: different knob colours per concept, different camera states.
- H5 cost: UNDER GLASS slightly over $20; HUSH at $30 default.

## Open questions
- **Eng:** E-L1 stick/MOD on strip C extension or wired; **E-L2 speaker depth (gates every height)**; E-L4 UNDER GLASS window parts placement; E-L5 HUSH cap/magnet geometry; KN1250 set-screw on knurled shafts (visual's Q).
- Director: Q-TC1 wall height 4–5 mm OK?
- Visual: UNDER GLASS legend size through 3 mm acrylic (parallax); worst-knob thumb drawing (TYPE CASE).
- Owner: UNDER GLASS board mask colour.

## What comes next
- Visual's redraws land → react, follow or say why not.
- Director scores round 2 → for each 9+ concept, full coverage walk against `jobs.md` (per job, supported or not, where) before the owner sees them.
