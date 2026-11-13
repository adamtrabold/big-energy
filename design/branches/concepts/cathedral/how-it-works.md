# CATHEDRAL: how it works (systems, turn 1, 2026-11-13)

Seed: **CHAMBER rev B** (`../chamber/`, director 9) **+ FOLD-105 v1.1** (`versions/v1.1/fold/`). Owner, 14:12–14:18 (`design/owner.md`): lock in on these two, find the middle ground, and call the point of view **CATHEDRAL**. Read with `design/jobs.md` rev 5, `../common-how-it-works.md` rev 2 and `../../echo-clock.md`.

Marks:
- **[CHECK]** `../branch_check.py` (§8a slot, §8b push-outs, §9 option B); TOTAL fails 0.
- **[CALC]** my arithmetic · **UNVERIFIED** · **ESTIMATE**.
- **⚑ D+O** = moves a control or changes the spec, so it needs the director's view and then the owner's. Nothing marked ⚑ is settled.

No images rendered (owner, 13:13).

---

## 0. What I assumed his words point at
| His words | What it is on the object | Confidence |
|---|---|---|
| "effects & out" | **The base PLAY row's right section**, whose hand-lettered heading reads "effects & out" (x 188.5): **ECHO REPEATS, ECHO MIX, REVERB MIX, TAP**. The heading is stale: **VOLUME left that section in rev 7.2** (it's on the lid's back row now), so nothing in it is "out" | high (it's the only place those words are printed) |
| "echo and reverb controls" | The lid's **back row** (d 83.85): ECHO TYPE, ECHO TIME (+ FREE / SYNC), REVERB DECAY, REVERB TYPE. Open, they sit **≈ 124 mm** behind the "effects & out" section [CALC: open y 191.85 vs 68], across V1, the band and V2 | high |
| "the speaker placement creates an odd gap" | The speaker sits under the **band** between the lid's V1 and V2 rows (d 21.9–59.45). Its grille is a 50 mm island of slots (x 118–168, d 28–46) on an otherwise empty strip | high |
| "**the screen**" | **The speaker grille** (the only screen-like part: parallel horizontal slots). Not a display: there is none, by his rule | high |
| "faceplates", "front edge squared" | The cream **pickguard plates**. Both have **square corners on one side**: the base plate's front corners (by the keys) and the lid plate's hinge-side corners. Their other corners are R 7.7. That's the inconsistency (`r5.py` `base_plate2d` / `lid_plate2d`: front radius 0) | high |
| "protective feet" / "the screws that screw the case in" | The **4 rubber feet** and **6 brass screws** on each half's back (CHAMBER lid: feet d 6 / 78; screws d 12 / 96 at x 16, 143, 270) | high |
| "hinges" | The **knuckles** at the rear corners (x 0–10, 276–286) on an M4 shoulder bolt | high |
| "the oxblood spine" | CHAMBER rev 2's flexible spine closing the hinge-side slot | certain |

---

## 1. Hidden hinge(s) in the gap: not possible as a hidden *axis*; possible as hidden *pins in the side walls*
**Why the gap can't hide the axis (geometry, not taste):**
- A fold with knobs on both halves needs the axis **halfway up the closed hollow**: z 26.3 in CATHEDRAL (axis rises 1.3 for the pegs).
- Open, that's **10.7 mm above the plates**. The seam gap lives *below* the plates (z 0–15.6), so a hinge hidden in it would pivot at plate level. Closed, the lid would then land on the base's knobs.
- **Concealed (Soss-type) hinges** pivot in the gap, and their hidden state is when the two edges abut. That's FOLD's *open* state, so **closed, their links would show across the back**. They also need ≥ 12.7 mm of wall to mortise (UNVERIFIED for the smallest size).
- **Dual-axis (laptop 360°) hinges** leave a gap the width of the barrel between the halves when open flat. That breaks the flush seam and R4.
- A **two-link "book spine"** of rigid slats (three axes) folds into the gap, but it has 3 degrees of freedom. The lid would flop, and the closing alignment and the standing angle would be lost.

**What can be hidden: the pivot pins, inside the side walls.**
- **Proposal (box-maker's side pivot):**
  - Each rear corner gets a **brass leaf pair inside the wall thickness (x 0–4.05 and 281.95–286)**: a base "ear" leaf and a lid leaf.
  - A **blind pin** at the axis (y 109, z 26.3) goes in from inside. The outside hole is capped flush with a walnut plug.
  - **No barrels show.**
- **What it looks like:**
  - Open, the base ear rises to z ≈ 31 at the two rear corners. It reads as the start of the lid's side rim, which already rises 22 mm along the lid's sides.
  - Closed, each end face shows one quiet half-lap joint line around a round ear, not a knuckle.
- **Rules:**
  - Ears and leaves stay within x ≤ 4.05, so ≥ 12 mm from RANGE 1's edge (16.05): R4's rim rule is met. On the right, KBD CTRL's edge is 267.1 → 14.9 ✓.
  - Width unchanged (286).
- **Against the ribbon:** the ribbon crosses the seam at x 176–227, far from the corners. **Unaffected.**
- **Against the stays:**
  - The stays pivot at d 30 and stow in the lid end faces at d 30–74.4; the lid leaf sits at d ≈ −8 … 2. **Clear by ≥ 26 mm.**
  - The base ear (y ≈ 100–110, above z 15.6) sits over the base's right end-face I/O, all of which is below z 15.6 (USB-C y 90–99, z 4.8–8.2). **Clear.**
- **Parts:**
  - 4 brass leaves (≈ 2 mm × 10 × 20, cut from flat bar, ESTIMATE);
  - 2 hardened pins (M3 or Ø 3 dowel, ESTIMATE);
  - 2 walnut plugs.
  - Leaves are bonded into slots printed in the walls.
- **Risk:** 2 mm brass leaves in a PETG wall carry the lid's weight and the stand loads, so the pivot boss strength is **UNVERIFIED** (eng / maker: one test print). The fallback is today's knuckles (owner: "if not these are fine").

## 2. The speaker and the gap
**The gap isn't caused by the speaker. It's where the base's PLAY row sleeps when the lid is closed.**
- Closed, a lid point at d lands over base y = 108 − d. The band (d 21.9–59.45) lands over y 48.5–86.1: exactly the PLAY row (y 68, CUTOFF r 10.4).
- **The band is already as narrow as the rules allow** [CALC from the v1.1 rows]:
  - V1 lands behind the PLAY row (y 93.55, 7.7 clear of CUTOFF);
  - V2 lands in front of it (y 47.15, **3.0 clear**, the rule's minimum).
- No knob can live in it. The speaker was put there because it was the only empty, deep place.
- **So the choice is what the gap is, not whether it exists.**

**Option A, no control moves: make the gap one designed thing.**
- The speaker stays where it is. The band becomes **one full-width element** instead of a grille island on a blank strip.
- CATHEDRAL reading: **a round "rose window" grille** over the speaker's centre (Ø ≤ 34, inside the band's 37.55 depth), flanked by blind lancets or engraved arcades over the cells.
- **"the screen" gets its rounding** (§5).
- **Leaves FX split. It doesn't answer his "those should be together".**

**Option B ⚑ D+O: every effect on one row, and the speaker moves to where the FX amounts were.**
- **Lid back row** (d 83.85), one section, read left to right:
  - **DRIFT 33.5 | ECHO: TYPE 62.5 · TIME 82.5 · REPEATS 102.5 · MIX 122.5 · TAP 142.5 | REVERB: TYPE 171 · DECAY 191 · MIX 211 | VOLUME 240**;
  - breaks 48 / 156 / 225.5;
  - **FREE / SYNC at (96, d 69)**, in front of the gap between TIME and REPEATS.
  - **[CHECK §9]: 0 violations** (pitch, gaps, breaks, edges, far rim, closed landing over pegs). The toggle window is bigger than today's (nearest: FREQ 3 2.87, REPEATS 4.16).
  - **Labels are not yet checked:** no model exists for B.
  - Everything the owner called "effects & out" now sits with echo and reverb, **and VOLUME ("out") is there too**.
  - TAP sits in the echo group, because echo is the only effect that uses tempo.
- **Base PLAY row:** PITCH (stick, MOD, TUNE, GLIDE) | FILTER (CUTOFF, EMPHASIS, AMOUNT) | **the speaker**.
  - Its free area: x 186–270 (break 184.5 to the edge), y 55–82 (keys end 54.6; V1's closed landing starts 86.1).
  - A **round grille up to Ø 27** centred at (228, 68), on the PLAY row's own line. CATHEDRAL reading: the rose window at the east end of the nave.
  - Under it, the 60 × 30 speaker (or a round one ≤ Ø 36: parts UNVERIFIED).
- **The lid band** keeps only the cells. It becomes a quiet, uninterrupted band: the gap reads as a deliberate rest, not a hole around a grille.
- **Costs, named:**
  1. **The FX amounts leave the hands' row.** Throwing an echo means reaching ≈ 126 mm further (open y 194 vs 68). Standing at 120°, they're the top row of the lid. This reverses v1.1's "amounts in front, kinds behind", which the owner saw and approved.
  2. **The base board changes** (speaker window; the Daisy sits rear right "on the floor in a board cutout": a clash with the speaker is **UNVERIFIED**, eng). The lid board loses its speaker window.
  3. Standing, a base speaker fires up, not at the player (today's lid speaker faces you). Flat or on a lap, it's about the same.
  4. The ribbon gets simpler (the speaker leads leave the lid; VOLUME's wiper already crosses on pin 33), **UNVERIFIED** (eng).
- Base and lid heights, depth (108) and width are unchanged. The band stays (it's the PLAY row's nest).

**Option C (rejected): bring echo and reverb down to the base.** The base has one row only. A second row grows the base deep enough to bring back FOLD-113's gap problem.

**My recommendation:** B, if the owner accepts the reach cost (1). It's the only layout that puts echo, reverb, their amounts and the output together on a FOLD, and it gives the speaker a home that isn't a gap. Otherwise A.

## 3. Feet that are also the case screws
- **Yes:** **screw-through rubber feet**. Each foot has a recessed metal washer; the case screw passes through the foot's centre into the brass insert, so the foot is the screw head, and a rubber cap plug closes the hole. Product family exists (recessed screw-mount bumpers); **exact part UNVERIFIED** (eng: Ø ≈ 12, ≤ 3 mm proud, M3).
- **Positions (lid back):**
  - **feet at the four corner screws** (16 / 270, d 12 and d 96): visible screws drop from 6 to 2. The flat-open support widens from d 6–78 to d 12–96;
  - the two axis screws (143, d 12 / 96) stay as flush brass, or also become feet (6 feet).
  - The façade field (x 34.8–251.2 at pitch 8.75) clears the corner feet.
  - **One clash if the axis screws become feet:** a Ø 12 foot at (143, d 12) touches the impost line at d 18. Shrink it to Ø 10, or move the impost to d 19.5.
- **Base underside:** the same idea. v1.1 positions aren't restated in my docs (**UNVERIFIED**; take them from r5).
- Both halves' feet must be the same height so the open instrument sits level.

## 4. Faceplate rounding
- **Make every corner of both cream plates R 7.7.** That's concentric with the block's R 12 plan corners and its 4.3 wall (12 − 4.3 = 7.7).
- That means the base front corners and the lid hinge-side corners, which are square now. Open, the seam then shows two rounded leaves meeting.
- **Pegs clear** [CALC]: the first natural's felt washer (Ø 14 at (17, 13.5)) reaches (10, 6.5). That's 5.57 from the corner arc centre (12, 11.7), inside the plate. The last peg mirrors it.
- **Lid hinge corners:** RANGE 1's edge (x ≥ 16.05) never enters the cut-off zone (x < 12). KBD CTRL likewise.
- No control moves. **Graphics and enclosure only** (visual: one parameter in `rrect2d`).

## 5. "The screen" (the speaker grille), rounded
- **Tapered slots** (his first option): each slot's length follows a circle, so the slots are shortest at the top and bottom and longest in the middle.
  - At 2.3 mm pitch inside Ø 34 (option A) that's ≈ 14 slots; inside Ø 27 (option B), ≈ 11.
  - Field area [CALC]: a Ø 34 field ≈ 910 mm², about today's 50 × 18 (900). Ø 27 ≈ 570 mm² (−37 %): quieter, **UNVERIFIED** acoustically.
- **Circular** (his second): concentric arcs, or a rose of radial slots.
- Both are visual choices on fixed geometry. Systems' only rule: the open area should stay ≥ ≈ 35 % of the cone's area. CATHEDRAL makes the circle the natural pick (rose window).

## 6. If the spine goes: what it was solving
- **The hinge-side slot**, real since v1.1: closed, a **21.9 × 266 mm opening along the back** shows the lid's V1 knobs 7 mm inside it and lets bag grit in (J6). v1.1 accepted it as a stated weakness (J6 ◐). CHAMBER's spine closed it.
- **If it goes, J6 drops back to ◐.** No rigid lip can replace it (R4, §1).
- **Middle ground:** keep the function and lose the accent. The same flexible spine in a **body-matched colour** (walnut-dark bookcloth or leather, or black) reads as part of the case. The side-pivot hinge (§1) doesn't change the spine's geometry: same anchors, same 21.9 closed / 2.1 open.
- **Owner's call:** no spine (slot back, as v1.1) / body-colour spine / oxblood.

## 7. CATHEDRAL as a point of view: what changes in the structure
- **The console inside, the organ outside, stays.** The pipes still come from the keyboard's own 2^(−n/12) and face the listener.
- **The architecture becomes the reason for the rounding he asked for:** every plate corner arched (§4), the rose-window grille (§5), the pipes' rounded mouths. The push-outs stay as the two real pipe mouths (rev 2 §R2.2).
- **The plan reads like a church:**
  - the keyboard is the nave's long axis;
  - option B's single FX row is **the choir**: everything that colours the sound, gathered in one place at the top of the standing lid;
  - the band is the **crossing**, the quiet space between nave and choir;
  - the base speaker is the **rose window at the east end**.
  - This is a metaphor, not a constraint: none of it moves a part beyond §2's option B.
- **No change** to boards (except option B's speaker windows), the Daisy, the mux plan, the battery, the stays or the I/O.

## 8. Not mine (the visual designer's), noted for completeness
The "woodier" engraving with the same amount of detail; peg / button colours (fewer, no out-of-place brown); the spine's colour if kept; the grille's pattern.

## 9. Open questions
1. **⚑ D+O:** option B (all FX + VOLUME on the lid back row, speaker in the base PLAY row: costs reach and v1.1's "amounts in front") or option A (layout as is; the gap becomes a rose-window band)?
2. **Owner:** spine: none, body colour, or oxblood?
3. **Eng:** side-pivot strength in PETG with brass leaves; screw-through foot part; base speaker vs the Daisy's place; ribbon changes in B.
4. **Visual:** with B chosen, a model so the checker can run labels (§7 of `branch_check.py`).

NEXT: product designer (visual focus) — the colours, the woody engraving, the grille pattern and the plate rounding are theirs, and options A/B need their look before the director weighs ⚑ B.
