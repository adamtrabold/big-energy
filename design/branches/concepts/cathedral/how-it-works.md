# CATHEDRAL: how it works (systems, turn 1, 2026-11-13)

> ## Team rulings in force (director, CATHEDRAL steer 1; these supersede the options below where they differ)
> 1. **All 8 plate corners R 7.7** (§4).
> 2. **Feet:**
>    - screw-through rubber feet at the **4 corner screws** (16 / 270, d 12 and d 96), black;
>    - the **2 axis screws (143, d 12 / 96) stay flush brass**, so they don't clash with the impost line (§3).
> 3. **Lid stays: cast brass** from the keys' service (lost-wax, from a printed pattern). **Fallback: matte-black PETG, 5 × 8** (end-face groove 5.5). Never grey 316L in view.
> 4. **Printed 316L steel only for the hidden hinge leaves** (out of sight).
> 5. **One key interface for every head:**
>    - the printed carrier's **Ø 9.6 × 3.3 cup** takes a **9.53 × 3.2 tenon**;
>    - wood plug, cast-brass head, printed head and a cap on a shaft all carry that tenon, so the choice stays swappable after the build (§10.2, §13).
> 6. Grille: tapered horizontal slots (vesica 66 × 16 in A; Ø 27 circle in B). Option A's base heading reads **"effects"**. Palette: walnut, cream, black, red CUTOFF, brass. Fine-line woody relief is built (visual).
>
> ### Two buy-and-test checks for the owner (before the lid height and the key order are fixed)
> | # | Buy | Do | Pass / what it sets |
> |---|---|---|---|
> | T1 | **One pack of Cherry Tree Toys 3/8" mushroom plugs** (birch SKU 31, https://cherrytreetoys.com/3-8-mushroom-plugs/, 50 pcs) | Measure, with calipers or a ruler on 5 plugs: **head height H** (top to the tenon shoulder), head Ø, tenon Ø and length | Sets the key height: head top = deck + 2.8 + H. **H ≤ 4.0 → closed stays ≈ 52.7 mm**; every mm over 4 adds a mm to the lid. Tenon ≈ 9.53 × 3.2 confirms the carrier's cup |
> | T2 | **One hollow cast-brass head** (2.5–3 g, wall 0.8–1.0, with the 9.53 × 3.2 tenon) from the cast-brass service, **one printed carrier**, **one Kailh Choc V2 silent switch** | Glue the head on the carrier, push it onto the switch, press and release 20 times slow and fast; listen at the top-out; compare with a bare plug on a second carrier | **Pass:** no audible top-out clack beyond the bare plug's, no wobble, no sticking. If it fails: thinner wall, or brass-look print. (Velocity calibration comes later, on the board) |
>
> ### Layout B label check on the render model (`branch_check.py` §7, rb.Cathedral("B"), Kalam)
> - **Layout A:** 0 collisions.
> - **Layout B:** 3 hits:
>   - **"repeats" overlaps the FREE / SYNC toggle by 1.7**: REPEATS' legend sits in front of its knob, where the toggle is;
>   - "repeats" ↔ "sync" 1.15 (rule 1.5);
>   - "free" ↔ FREQ 3 0.64.
> - **Fix (geometry):**
>   - in B, **TIME's and REPEATS' legends go behind their knobs** (the toggle sits between them, in front);
>   - "free" / "sync" sit **0.5 behind** the toggle centre, as CHAMBER's fix.
>   - Re-run after the visual designer applies it.
> - The CHAMBER model in rb.py currently raises an error (`screw` undefined in `lid_back`, the visual designer's file mid-edit), so that run was skipped. The Cathedral models ran.

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
- **Owner's call:** no spine (slot back, as v1.1) / body-colour spine / oxblood. **→ Owner 14:4x: no spine.** See §12.2 for what answers the slot instead.

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

## 10. Keys, redone around real parts; and no machining anywhere (owner 14:30–14:34)

**Owner:**
- "The Wooden ones you linked do not have shafts that match the prototype";
- "I don't know how to machine — the keys need to be printed or purchasable";
- "They can be printed externally too - I know you can get metal prints".

**What was wrong:**
- From HUSH v1.1 through CHAMBER, the peg was a "1/2 in button plug" whose shank reached down through a felt collar and the deck into an acrylic arm.
- Stock mushroom plugs have a **⅛–¼ in tenon**, and the size names the **hole, not the head**.
- **This affects HUSH, CHAMBER / CATHEDRAL and RAIN alike** (one key mechanism; RAIN's and HUSH's files still describe the old shank).

### 10.1 The bought part (a supplier that publishes all three dimensions)
- **Cherry Tree Toys 3/8" mushroom plug.**
- **Published dimensions:** head ("overall diameter") **1/2" = 12.7 mm**, tenon **3/8" = 9.53 mm**, tenon length **1/8" = 3.2 mm**, package of 50.
- **Species:**
  - birch, SKU 31 (https://cherrytreetoys.com/3-8-mushroom-plugs/);
  - oak, SKU 31-O (https://cherrytreetoys.com/3-8-oak-mushroom-plugs/), same dimensions;
  - a 3/8" **cherry** plug ($5.35 / 50, on https://cherrytreetoys.com/wood-plugs/). Its dimensions aren't published; assumed the same family, **UNVERIFIED**.
  - Their only walnut mushroom plug is 1/4" (head ≈ 3/8", too small).
- **Not published anywhere I checked: head height.** Order one pack and measure; it sets the key height below.
- **Others checked:**
  - Craftparts publishes head 5/8" for its 1/2" plug, with tenon length "typically 1/4"" and no tenon diameter.
  - Bear Woods lists maple and walnut, says the standard tenon is 1/4" (long-shank SKUs exist) and gives no head or tenon diameters.
  - Woodpeckers and WidgetCo publish only the hole size.
  - So Cherry Tree Toys is the only one with all three.
- **Colour note:** the head now matches the old 12.7 mm design. Birch or oak is pale, so the reverse-walnut naturals become a stain or a printed choice, which suits his "too many colours / brown feels out of place" (visual).

### 10.2 The new interface: a printed keycap carries the plug (no shank through the deck)
**Printed peg carrier, one per key, PETG.** Printed parts are now allowed; it's a keycap, not a mechanism. It does what the acrylic arm did:
- **Bottom:** an MX cross socket onto the Choc V2 stem (the switch has an MX cross stem, `velocity-and-keys-v2.md` §2).
- **Arm:** a pocket for the D31 magnet, **10.5 behind the stem at the same height as v1.1** (face 7.6 above strip C at rest). So the magnet's rest / bottom gaps (5.6 / 2.8) and the velocity fit are unchanged.
- **Top:** a **cup Ø 9.6 × 3.3 deep** for the plug's tenon, glued with wood glue. The tenon tapers slightly (Bear Woods), so it seats tight. Cup wall 0.8 → **neck Ø 11.2**.

**The deck hole clears the neck, not a shank:** hole Ø 12.0 (0.4 a side).

**The felt stop moves down, off the deck.** A felt ring on the deck can't work any more: under a 12.7 head, an 11.2 neck leaves a 0.75 mm landing.
- **Stop:** a **bought keyboard O-ring dampener** on the carrier's stem, or a punched felt ring (Ø 14) on the switch top. The carrier's skirt lands on it **at ≈ 2.5 of the 2.8 ± 0.25 travel**, as HUSH's collar did.
- The O-ring / felt **thickness is the tuning knob** (≈ 0.3–0.5).
- The fit window for velocity (15–75 % of the stroke) ends at 2.1 mm, well before the stop at 2.5 → **velocity unaffected** [CALC].
- The Choc silent switch damps both strokes on its own; the ring keeps it off hard bottom.

**Height** (H = the plug's head height, unpublished):
- head underside at rest = deck + **2.8** (travel to the stop + 0.3 margin);
- head top = deck + 2.8 + H.
- H ≈ 4 → **6.8** (v1.1 pegs 6.5: +0.3).
- H ≈ 5 → 7.8 (+1.3, and FOLD's closed height then needs ≈ +1.3 more: ≈ 54.0) [CALC].
- **Measure H before the lid height is fixed.**

**What shows:** a 2.8 mm printed neck under each wooden head, with a dark ring of deck hole round it. CATHEDRAL reading: an organ's drawknob on its stem.

**Felt:** the punched rings only need a hand punch (bought tool), or buy pre-cut felt washers. Not machining.

### 10.3 Printed pegs (allowed now): a real option
- **One piece per key** (head + neck + arm + MX socket), FDM.
- **Orientation:** print **upright, socket down on the bed**, so the cross socket's walls are vertical and accurate. The dome comes last, at 0.12 mm layers; its top shows faint terraces (a matte filament hides them).
  - Head-down is smoother on top, but it needs supports in the socket, which spoil the fit. Rejected.
- **Fit:** the MX cross needs a tolerance coupon (three sockets at −0.05 / 0 / +0.05 mm). The magnet press-fits into a printed pocket and is glued.
- **Feel against the wood plugs:** printed PETG/PLA feels cooler, slicker and lighter than birch. A wood-fill or matte filament narrows the gap; it won't feel like turned wood.
- **What it does for his colour note:** pegs and TAP can be the same filament, so one less colour.
- **Same carrier geometry as 10.2.** The bought-plug and printed-peg versions are interchangeable on the same switches.
- **Externally printed** (resin or SLS) gives a smooth dome with no terraces. Cost **UNVERIFIED**: quote by upload.

### 10.4 Options, plainly (not picking)
| | Head | Who makes it | Feel | Notes |
|---|---|---|---|---|
| A. **Bought plug on a printed carrier** | Cherry Tree Toys 3/8" (12.7 head, 9.53 × 3.2 tenon) | buy plugs; print carriers | turned wood | head height unpublished: measure; pale species only (birch / oak / cherry) |
| B. **Printed peg, one piece** | printed | print | plastic; matte or wood-fill helps | best colour control; FDM terraces on the dome |
| C. **Externally printed pegs** (resin / SLS) | printed | order | smooth plastic | cost UNVERIFIED |
| E. **Bought wood cap on a shaft** (owner, thinking aloud: "Premade wooden caps on a shaft that also is premade or part of the key is fine too") | a turned wood knob or furniture button with a bored hole, **≤ Ø 16** (18 mm pitch leaves ≥ 2 mm between heads) | buy caps; the shaft is either a **bought dowel** (e.g. 1/4" = 6.35, glued into the cap and into a Ø 6.4 socket in the printed carrier) or **printed into the carrier** (a Ø 6 printed stem: snug, glued) | turned wood | needs a cap supplier that publishes head Ø, height and bore Ø × depth (**none checked yet**); a dowel adds a glue joint. The carrier, stop and velocity are as §10.2 |
| D. **Flat tops** (v1.1 FOLD) | printed or laser-cut | print, or laser at Vector Space (allowed, not leaned on) | flat key | no peg height cost; closed back to ≈ 50.1 |

## 11. No machining: every part CATHEDRAL had him cut or drill
| Part | Was | Now | Cost (rough) |
|---|---|---|---|
| **Lid stays** (2) | cut + drilled from 3 × 8 brass bar | **(a) metal-printed 316L stainless by a service** (JLC3DP BJ-316L: "From $5.0", max 100 mm, walls > 1.5, tolerance ±0.3 mm, checked on jlc3dp.com). The stay is 3 × 8 × 44.4, inside every limit. The pivot hole prints undersize, then a bought shoulder screw. **(b) printed PETG at 5 × 8** (the 3 mm section is too slender in plastic; the end-face groove widens to 5.5) | (a) ≈ $5–15 each + shipping, **UNVERIFIED** beyond "from $5"; (b) pennies |
| **Hidden-hinge brass leaves** (4, §1) | cut from flat bar | **(a) metal-printed 316L** (2 × 10 × 20 is ≥ the 1.5 wall and 5 mm minimum) or **(b) printed in the wall** (PETG, strength UNVERIFIED), with a **bought** Ø 3 dowel pin or M3 shoulder screw. Or the **knuckles** (printed lugs + a bought M4 shoulder bolt, as v1.1: no machining) | (a) ≈ $5 each, **UNVERIFIED** |
| Hinge "brass sleeve fallback" (v1.1) | tube cut to length | **bought oilite bronze bushing** (sized, off the shelf) | ≈ $1, UNVERIFIED |
| Acrylic peg arms | laser-cut | **printed carriers** (§10.2) | pennies |
| Felt collars / rings | punched | hand punch (bought tool) or **bought pre-cut washers** | — |
| Inserts, magnets, screws, feet, pins | — | all bought; heat-set inserts go in with a soldering iron (not machining) | — |
| "Real planed walnut later" (FOLD's long-term idea) | planed and routed blocks | **machining: flag.** Stays a future option only, by a woodworker; the build is printed (wood-fill / walnut-tone) | — |
| Spine (if kept) | bookcloth cut with scissors | as is (not machining) | — |

**Metal-printed brass or bronze:** I couldn't check a service's price or availability this session, so **UNVERIFIED**. 316L at JLC3DP is the one I checked. It's stainless, not brass-coloured: a brass look would be paint or plating, or brass from a service once checked.

## 12. No spine: routing cables through the hinge, and what answers the back slot (owner 14:4x)
**Owner:** "I don't want a spine can we route cables through a hinge."

### 12.1 Through the hinge: not the ribbon; possible with round cables through hollow corner knuckles, at a cost
**The 40-way ribbon can't go through any hinge.**
- It's 50.8 mm wide and flat, and it crosses the seam at x 176–227 in a rolling loop.
- A flat ribbon can't twist 180° in a knuckle's ≈ 9 mm length.

**What a through-hinge needs:**
- The ribbon replaced by **two round multi-core cables**, one through each rear-corner knuckle, along the axis (z 26.3).
- The ribbon list is 21 signal lines plus grounds (v1.1 §Hinge ribbon), so each cable carries ≈ 12–20 cores, **≤ ≈ 5 mm OD** (part UNVERIFIED).
- **Pin 39** (mixer bus → ladder, the sensitive line) goes in its own **shielded** core, and eng's noise test (pass ≤ −70 dB) has to be redone.
- **A hollow pin.** Bought: unthreaded round spacers / standoffs with a clear bore (Ø 10 OD × ≈ 5.3 ID class, UNVERIFIED stock), cut by the maker, not by him. Or **metal-printed 316L** (JLC3DP: walls > 1.5, so Ø 8.5 × 5.5 bore, ≤ 100 long ✓; from $5, UNVERIFIED beyond that).
- **Bigger knuckle barrels:** Ø 9.6 → **≥ Ø 13–14** to hold that pin. Open, the corner barrels rise to z ≈ 33 (were 30.9). That's **more visible, not less**.
- **Twist:** 180° of rotation over ≈ 9 mm of axis won't do. Each cable needs a **service loop inside both halves** behind the knuckle. Space at the rear corners is UNVERIFIED (base: landing strip above, Daisy rear right).
- **Headers move to the corners on both boards:** a board change (eng).

**Against my hidden side-pivot (§1):** incompatible. The pivot lives in 4 mm walls, with no room for a bore. **It's one or the other:**
- **hidden pins** (cables stay in the seam), or
- **hollow knuckles** (cables in the hinge, barrels a bit bigger).

**Printed hollow hinges** (print-in-place or a printed barrel) exist in PETG. At Ø 13 with a 5.5 bore the wall is 3.75, but strength under the stand load and the lid's weight is **UNVERIFIED**, so I'd use a 316L or bought pin inside a printed barrel.

**⚑ D+O and eng:** cables-through-hinge changes both boards' headers and the cable spec. It's worth it only if the owner prefers it to hidden pins.

### 12.2 With no spine: the back slot (21.9 × 266, closed) — options, not picking
| | What | Answers | Costs |
|---|---|---|---|
| S0 | **Leave it open** (v1.1 as locked) | nothing; J6 ◐ (grit, knobs visible 7 mm inside) | $0 |
| S1 | **Design it as an arcade:** dark interior behind the slot; the visible tops of V1's knobs read as a row of columns. CATHEDRAL: the clerestory | how it looks, not grit | $0 (paint the lid's hinge-edge interior) |
| S2 | **Cables through the hinge (12.1)**, so the ribbon loop no longer shows in the slot either | removes the cable from view | board and cable changes; bigger knuckles; loses hidden pins |
| S3 | **A sleeve** (case work) | grit and protection | his "case" topic was deferred for HUSH / ONE SHEET; FOLD was meant to self-protect |
| S4 | A rigid lip or flap | — | **can't**: raised among the knobs when open (R4), §1 |
| S5 | The spine | full closure | **declined by the owner**; listed only because it's the only full closure |

## 13. Brass / black keys, or all brass (owner: "Could 3d print and reminds me of a cathedral")
**Form:** a **hollow cap** over the printed carrier (§10.2) replaces the wood plug head. Same Ø 12.7 dome, wall ≈ 0.8–1.0, glued onto the carrier's cup.

| Option | How | Mass per cap [CALC, ESTIMATE] | Cost × 25 | Wear |
|---|---|---|---|---|
| **Cast brass** (wax print, lost-wax cast by a service) | i.materialise brass (checked: cast from printed wax; min wall 0.6, detail 0.35, max 88 × 88 × 125; finishes natural PU-coated, gold, **black colour-plated**, chrome; electroplating adds €5–9 per model; base price not published) | hollow ≈ 2–3 g; solid head ≈ 4–5 g (brass ≈ 8.5 g/cm³) | **UNVERIFIED**: quote by upload. Plating alone adds €125–225 for 25 | uncoated brass darkens / greens; PU coat wears at touch points (uneven patina); black plating wears through to brass where fingers land (a "worn organ stop" look, or a flaw) |
| **Metal print 316L** (JLC3DP) | steel, not brass-coloured (plate or paint for brass / black) | ≈ same as brass (7.9 g/cm³) | ≥ 25 × $5 = **≥ $125 UNVERIFIED** (only "from $5" checked) | steel doesn't patina; plating wears as above |
| **Brass-look printed** | brass/copper-filled PLA (hand-polishes to a metal sheen, no machining) or silk-gold PLA; black PETG for sharps | metal-fill ≈ 0.8–1.2 g; silk ≈ 0.5 g | pennies (filament) | metal-fill burnishes and darkens like metal; silk PLA scuffs |

**Feel on a Choc V2** (≈ 35–43 gf per switch, eng `velocity-and-keys-v2.md` S3):
- A 2–3 g hollow brass cap is ≈ 5–8 % of the spring force: it feels slightly lighter at the top. Negligible.
- A **solid 4–5 g head is ≈ 10–14 %**: noticeably lighter, and a firmer top-out on release.
- The **silent Choc damps both strokes**, so bounce shouldn't become audible (**UNVERIFIED**: test one key).
- **Recommend hollow caps if metal.**

**Velocity:**
- **Brass is non-magnetic** (copper-zinc, μr ≈ 1). It doesn't bend the D31's field. The magnet sits in the carrier's arm 10.5 behind the stem anyway, not under the cap.
- Eddy-current drag at key speeds near a 4.76 mm magnet: negligible (ESTIMATE).
- A heavier cap slows the stroke for the same finger force, so velocity reads slightly lower. **If every key has the same cap mass, one calibration covers it.**
- **Mixing brass naturals with plastic sharps** gives two masses, so the firmware needs a per-group velocity curve (eng: trivial, but note it). Black-plated brass sharps avoid it.
- **316L steel is weakly magnetic after printing** (austenitic, but printed/sintered parts can show some ferromagnetism, ESTIMATE). Near the magnet arm it could pull the field slightly. Brass doesn't.

**Height:** a hollow cap can be shallower than a wood head (it isn't limited by plug stock). With dome height ≈ 4, the head top = deck + 2.8 + 4 = **6.8**, and FOLD's closed height stays as CHAMBER's 52.7 [CALC].

**CATHEDRAL reading:**
- **All brass** rhymes the keys with the façade's brass line work: **one metal, fewer colours**, his ask.
- **Brass + black** reads as organ stops and pipes.
- Colour is the visual designer's call; the numbers above hold for both.

## 14. Speaker placement, round 2 (owner: "I don't like the speaker on the key side but I also don't like the eye shape")
**Kept:** B's single effects row on the lid's back row (his "FX together" ask stands). **Ruled out:** a speaker grille on the base's top face (key side), and any lens or vesica.

**The space facts** (v1.1 FOLD-105):
- the lid's under-plate depth is **10.6 mm** (speaker 60 × 30 × 10.3 lies flat; it can't stand on edge);
- the band is d 21.9–59.45, with **≈ 22 mm clear for a grille** between the "mixer" heading and V2's legends (visual's figure);
- the lid end faces carry the stays (d 30–74.4);
- the far wall carries the I/O board (x 60–230, d 92–104);
- base under-plate space is ≈ 11.1.

| | Placement | Sound path | Table / lap / grass | What moves | Checks |
|---|---|---|---|---|---|
| **P1. Band, fires up, non-lens grille** | the speaker stays where v1.1 has it: x 113–173, d 26.7–56.7, under the band plate. The grille is **(a) a rounded rectangle ≈ 56 × 18, r ≈ 6** or **(b) an arcade of vertical slots** (≈ 11 slots, pitch 5, width 2, lengths stepping ≈ 8 → 18 → 8: a pipe-tower silhouette, not a lens) | up through the lid plate. **Open flat:** straight up, at the player's chest. **Standing 120°:** the panel faces 30° up, so the speaker faces the player | best of the set: unobstructed in all three. On grass the lid is clear of it | **nothing** (speaker, board windows and ribbon as v1.1) | grille open area: (b) ≈ 290 mm² vs today's ≈ 440 (fewer slots → ≈ −35 %, UNVERIFIED acoustically; widen slots to 2.5 to recover); grille vs V2 legends and the mixer heading (§7 checker once modelled) |
| **P2. Through the lid back (the façade speaks)** | the same speaker, same x / d, flipped: it fires **out through the lid back**. The openings are slots set into the façade, inside x 113–173, d 26.7–56.7, i.e. within the centre pipes (the owner draws the pipes; the openings follow his lines) | **Standing 120°:** the lid back faces back and up, so it fires at the listener across from you. The organ speaks from its façade; the player hears it by reflection. **Open flat:** the lid back sits on its feet (≈ 3 mm gap), firing into the table. **Closed:** faces up (off anyway) | standing: loud to the listener, softer to the player. Flat on a table: muffled and dark (boundary-loaded through a 3 mm gap, like ONE SHEET's bottom speaker). Lap: muffled. Grass: absorbed | **no controls.** The speaker mounts to the lid back's inner face instead of under the plate. The band plate becomes plain (no grille at all) | openings vs his pipe lines; dust/water path through the façade; feet height raised to ≥ 6 so flat-open isn't choked (UNVERIFIED gain) |
| **P3. Base underside, fires down** | the speaker in the base's freed right end (B: x 186–270, y 55–82), lying on the floor, firing **through the base bottom**; nothing on the base top | down into whatever it's on, out through the feet gap | table: muffled and dark (as P2 flat). Lap: smothered. Grass: absorbed. **Weakest outdoors** | no controls. **Base board change** (speaker window); the **Daisy (rear right) clash is UNVERIFIED** | is "key side" visual (grille on top) or the base half at all? If the latter, P3 is out too |

**P1c. An off-centre circle in the band** (owner: "go back to a circle and maybe not centered?"; he prefers lines running up and down).
- **Method:** measured on rb.Cathedral("B") with Kalam (`/tmp/circ.py` uses `branch_check.py` §7's machinery). Largest circle clear of every legend (≥ 1.5), every V1 / V2 / switch control (≥ 1.5) and every tick (≥ 1.0) [CHECK].
- **Largest circle by position along the band:**

  | Position (x) | Largest Ø | At depth d |
  |---|---|---|
  | 158–176 | **≈ 25–27** | ≈ 36.5 |
  | 116–128 | ≈ 24 | ≈ 36 |
  | 230–236 | ≈ 25 | ≈ 35 |
  | 80–110 and 194–206 (the switch columns) | ≈ 11–17 | — |
  | the axis, 134–152 | ≈ 18.5–20 (the "mixer" heading and NOISE / EXT's legend crowd it) | — |

- **So the centre is the worst place for a circle and off-centre is the best.**
- **Pick that keeps the speaker where it is** (window x 113–173, d 26.7–56.7):
  - **centre (160, d 37), Ø 25**, 17 mm right of the axis, still entirely over the cone (x 147.5–172.5);
  - mirror at (126, d 36), Ø 24, if he prefers left.
  - **Nothing moves.**
- **Further out** (x ≈ 233, Ø 25) means swapping the speaker with the right-hand cells: a lid board window change (eng). Not needed.
- **Closed:** the band lands over the base PLAY row, but a grille is flush and the speaker depth is unchanged, so **there's no closing clearance issue anywhere in the band.**
- **Open area** (vertical slots, pitch 2.3, width 1.25, ≈ 54 % open) [CALC]:
  - circle Ø 25 ≈ **265 mm²** (Ø 27 ≈ 310);
  - the vertical-slot tower ≈ 290;
  - today's grille ≈ 440.
  - Circle and tower are within ≈ ±10 % of each other, and both ≈ 35–40 % below today (loudness UNVERIFIED; wider slots recover some).

**Rejected, with reasons:**
- **Lid end walls:** the speaker would have to stand on edge (30 > 10.6 under the plate), and the end faces carry the stays' grooves.
- **Lid far wall:** the I/O board and jacks fill x 60–230; behind the wall are the FX pots.
- **Hinge zone / base rear wall:** open, it faces the lid's hinge wall across a 2 mm gap.
- **Two small speakers:** quieter in total, and no space either side of the band's cells.

**A consequence of B with the speaker not in the base:** the base PLAY row's right end (x 186–270) is **empty**. ⚑ D+O, options:
1. **VOLUME and TAP come back to the base right** (TAP is played in rhythm; VOLUME is "out"). The lid row is then DRIFT | echo ×4 | reverb ×3, and FREE / SYNC stays by TIME. His "together" holds for every effect control; out and tempo sit with the hands.
2. **The PLAY row is re-centred** across 286 (pitch | filter only), leaving equal margins.
3. **The maker's lozenge and the two lights** go there.

**My read (not a pick):** P1 is the only placement that's as loud as today in every place he plays, and it moves nothing. P2 is the CATHEDRAL idea (the façade speaks) but trades the player's sound and flat-table loudness for the listener's. P3 is the quietest.

## 15. Stereo (owner: "the verb and delay are stereo…should we have two? Also is there stereo output?")
**Today:**
- One mono output path: VCA → output mixer → VOLUME → LM386 → speaker, with phones / line from the LM386 through a series R (`budget-variant.md`).
- FOLD's far wall has **PHONES and LINE OUT** as two jacks; ONE SHEET has one PHONES jack.
- The Daisy already computes **wet L / R** and its codec is **stereo out**. Eng drew "stereo to phones optional" (`daisy-first-principles.md` §6.2).
- The effects that are truly stereo: PING-PONG, and reverb width (eng's libraries are stereo plate / ping-pong, `single-chip-research.md` §3).

### 15.1 Stereo output: cheap, no new jacks
**What it takes:**
- **Daisy and codec: nothing new.** Both codec outputs are already wired as wet L / R. 0 pins.
- **Two output summing nodes** (one TL072: dry + wet L, dry + wet R).
  - **The dry voice is mono, so it sits in the centre of both channels.** One VCA can't be stereo.
  - Only the echo and reverb spread.
- **VOLUME becomes a dual-gang 9 mm pot** (same knob, same place; part / spline UNVERIFIED). The other route is the dry level on one gang plus the Daisy scaling the wet by reading VOLUME's wiper, but then the wet and dry tapers must match (eng).
- **A stereo headphone driver** replaces "phones from the LM386 through a series R": a DIP dual op-amp that drives 32 Ω (NJM4556A class, UNVERIFIED part and price).
- **The LM386 stays for the speaker**, fed the mono sum (L + R)/2. PING-PONG in mono becomes CLEAN with alternating tone, as eng's table already says.
- **Jacks: none added.** FOLD's PHONES and LINE OUT become **TRS stereo**, as does ONE SHEET's PHONES. **His "no extra patch points" holds.**
  - A **mono plug in a stereo jack hears L only** (R shorts to sleeve through its series R), so a mono cable loses the right-hand ping-pong repeats.
  - The fix is a switched TRS jack that sums to mono when a mono plug goes in (UNVERIFIED part).
- **Cost:** ≈ **$3–5** (TL072 + headphone driver + dual pot + passives; ESTIMATE, UNVERIFIED). **Power:** a few mA, only with phones in.
- **⚑ D+O:** it changes the output stage, VOLUME's part and the jacks' wiring. **No control moves.**

### 15.2 Two speakers: honest answer, not worth it here
**Audible?**
- Two drivers ≈ 200–250 mm apart, at 0.5–0.6 m (seated, playing), span ≈ 20–25° [CALC]. That's laptop-speaker stereo: a little width close up, and PING-PONG audible as left / right.
- At a bench friend's 1–2 m, and outdoors (no reflections), it **collapses to near mono**.
- Small 60 × 30 drivers have no bass either way. **Two drivers mostly buy loudness** (≈ +3 dB), **not stereo.**

**Where (his rules: not on the key side, no eye shape; vertical lines or an off-centre circle in the band):**
- To be 200 mm apart they'd sit at x ≈ 40 and ≈ 245, **over the battery cells** (FOLD-105's four cells fill x 15–103 and 183–271 under the band; the lid has 10.6 mm under the plate and nowhere else).
- That means **giving up cell space**, on a battery already ≈ 1.9–3.9 h [CALC].
- The band's clear circles there are uneven: Ø ≈ 18–20 at x ≈ 40–44, Ø ≈ 23–25 at x ≈ 236–242 [CHECK, §14]. So two matching round grilles would be ≤ Ø 18.

**Cost and power:**
- ≈ +$2–3 (a second speaker; a stereo amp or a second LM386; eng's basis: speaker + LM386 ≈ $2.20).
- A little more draw at the same loudness per driver.
- The real cost is **battery capacity and a lid board change**.

### 15.3 Recommendation (superseded in part by 15.4: decided stereo phones + stereo line out, one speaker)
- **Yes to stereo output, no to a second speaker.**
- Stereo phones and line out give him the real stereo echo and reverb wherever stereo can be heard (headphones, a recorder, a PA), for ≈ $3–5, with no new jack and no control moved.
- A second speaker in this box gives little stereo beyond arm's length, nothing outdoors, and costs battery he may need in the park.
- **Spec change for the director, then the owner:** stereo TRS outputs + dual-gang VOLUME + a headphone driver. The speaker stays mono (P1 / circle per §14).

### 15.4 Owner decision and the FX pan (owner: "Stereo phones is fine but I need to pan the signal into the effects")
**Decided:** stereo **phones**, **one speaker**.
**Decided (owner: "Stereo line out"):** **stereo PHONES and stereo LINE OUT (both TRS), one speaker.** No new jacks; LINE OUT gets its own stereo line driver (the second half of the summing TL072 pair, or a second TL072: ESTIMATE ≈ +$0.50).

**Mono on a TS cable (owner: "Left channel should be mono tho if stereo isn't plugged in"): LINE OUT, required.**
- **Why a switched jack can't do it alone:** a jack's normal contacts open for *any* plug. A TS plug differs only in that its sleeve **grounds the ring contact**. So the jack can't tell TS from TRS mechanically; the circuit has to sense the grounded ring.
- **Sensing (proposal):**
  - The ring is driven through its usual series resistor (≈ 100 Ω, so a short is harmless).
  - On the jack side, a **1 MΩ bias to 3.3 V** goes through a **100 k / 1 µF low-pass** (≈ 0.1 s, strips the audio) into a **spare mux channel** (an ADC read, 0 Daisy pins) or a spare ADC pin.
  - Readings [CALC]: **TS plug ≈ 0 V**; TRS into an AC-coupled input or an empty jack ≈ 3.3 V; TRS into a DC-coupled 10 k input ≈ 33 mV.
  - **Threshold ≈ 10 mV, 50 ms debounce, with hysteresis.** The 1 MΩ bias puts at most ≈ 33 mV of DC into someone's DC-coupled input; a stronger bias would read more cleanly but leak more DC.
  - **UNVERIFIED** (eng: bench it with a real TS and a real TRS cable into a mixer and an interface).
- **Action:** on TS, the Daisy sends the wet as **(L + R)/2 on both codec outputs**. The tip (L = dry + wet) then carries the full mono mix; the ring is shorted and silent.
  - Cost: the stereo phones go mono too while a TS cable sits in LINE OUT (they share the wet outputs). That's a firmware-only route.
  - The analog alternative that keeps the phones stereo: a **74HC4053** analog switch (generic part, ≈ $0.50, UNVERIFIED stock) adds R into the LINE OUT's left driver when the sense trips. The Daisy flips it from the same reading (1 GPIO via the 74HC595 latch, eng).
- **Jack:** any 3.5 mm stereo (TRS) PCB jack; switches aren't needed for this. For example **CUI Devices SJ1-3523N** (part number not checked this session: **UNVERIFIED**), the same part as PHONES.
- **Phones: not applied.** A 32 Ω headphone on the ring looks like a short to this sensor, so it can't tell TS from TRS. Mono TS headphones are rare. With a TS plug in PHONES you hear L only (dry + wet L); the FX PAN's centre still puts the effects in L.
- **⚑ D+O:** part of §15's output-stage change.

**FX PAN ⚑ D+O (adds one control):**
- **Where the pan happens: in the Daisy, on the effects input.**
  - The FX send is mono: the post-VCA voice into codec IN L (`daisy-first-principles.md` §6.2).
  - The DSP places it in the stereo field **before** echo and reverb.
  - Cost: **one 9 mm pot on one mux channel**, 0 Daisy pins. In layout B the four moved controls already shift mux load from base to lid (base −4, lid +5 with PAN), so **eng to confirm the lid mux count**. PAN can be read on a base mux channel through a ribbon spare if the lid mux is full.
  - **Analog pan rejected:** the dry voice never enters the DSP, and panning it would need a stereo analog path after a mono VCA (a pan pot feeding the two summing nodes). That's more parts, and it isn't what he asked for: "pan the signal **into the effects**".
- **What it pans:** **only the effects send.**
  - The dry voice stays centred on the phones (mono VCA).
  - What moves is where the echoes and reverb start: PING-PONG's first repeat, and the reverb's image.
- **Pan law: constant sum (L + R = 1, −6 dB at centre).**
  - **The speaker hears no change of effect level as he pans**, because it plays the mono sum.
  - On phones the centre sounds ≈ 3 dB quieter than an equal-power law would. Eng can soften it to −4.5 dB; that's a firmware constant.
- **Range and centre:**
  - full left ↔ full right;
  - **centre detent:** a 9 mm centre-detent pot if one exists in the T18 spline (**part UNVERIFIED**);
  - otherwise a **firmware dead zone of ±3 % at centre**, no part needed.
  - Fully left or right: the send enters one side only, so on PING-PONG the repeats then alternate from that side.
- **MIDI (owner: "Yea sure on midi"): FX PAN receives CC 10, jump-on-move as usual.**
  - It joins the MIDI-controllable set, so it gets the engraved MIDI dot and lights the not-in-control light while CC 10 holds it. **Whether it also sends CC 10 when moved is open with the owner** (jobs F7 step 7 assumed knobs send; he hasn't confirmed). §15.5 moves CC 10 to DRY PAN.
  - The Daisy reads it anyway, so it costs firmware only.
  - **What it pans** (owner asked: "is it sending the delay through the pan too or just the dry"): **the send into echo and reverb.** The repeats and the reverb come out panned; the dry voice stays centred.
    - The reverb is stereo, so its tail **spreads around** the panned position rather than sitting hard on one side.
    - PING-PONG starts on the panned side and then alternates.
- **Where it sits (layout B's effects row, d 83.85):** **FX PAN 240 | VOLUME 260**, one "where it goes" group after the reverb break (225.5).
  - The logical spot, the start of the chain before ECHO, has no room: it would shift the echo group +10 and push FREE / SYNC onto OSC 3 CTL (−0.4).
  - **[CHECK §9, second run]: 0 violations** (pitch, gaps, breaks, edges, far rim, closed landing over pegs). VOLUME's edge sits 18.55 from the outside (rule ≥ 16).
  - **Labels:** "pan" (legend in front, d ≈ 73) clears L SUSTAIN's knob by ≈ 3.7 and the DECAY toggle by more [CALC]. The model needs PAN added so §7 can measure it (visual).
  - Legend: **"fx pan"**, so nobody reads it as a master pan.
- **Consequence:** the base PLAY row's right end (x 186–270) is still empty (§14 options 2–3). Option 1 (VOLUME and TAP back to the base) would split PAN from VOLUME.

### 15.5 Dry pan, delay pan, and FOLLOW ⚑ D+O (owner: "No the pan would be audio signal… pan just the delay separately from the full dry… have the pan signals sync"; then "Follow dry")
**What he wants:**
1. a pan for the **full dry voice on the outputs**;
2. a **separate pan for the delay**;
3. a link so the **delay pan follows the dry pan, same side**.

No tempo auto-pan (the earlier draft is withdrawn).

**Signal flow:**
```
voice (mono, analog) ─► [DRY PAN: dual digital pot, analog audio] ─► L sum / R sum ─► phones, line out (stereo), speaker (mono sum)
            └─ FX send (follows DRY PAN in DSP) ─► reverb in (stereo)
               └─► ECHO ─► [DELAY PAN, DSP; = DRY PAN when FOLLOW] ─┬► L / R sums (ECHO MIX)
                                                                     └► reverb in (stereo)
reverb out (stereo) ─► L / R sums (REVERB MIX)
```

**1. DRY PAN: analog audio, set by the Daisy (recommended route).**
- The **knob is a plain control pot on a mux channel** (DC, read by the Daisy). The **audio goes through a dual digital potentiometer** wired as two complementary dividers into the L and R summing nodes: L = a, R = 1 − a, a **constant-sum law**.
- **Part:** Microchip **MCP4251-103** (dual 10 k, 257 steps, SPI, DIP-14). **UNVERIFIED** this session (part, price ≈ $1.5, stock).
  - It runs at 5 V, so the audio is AC-coupled and biased at mid-rail (eng: headroom, THD, wiper noise).
  - One SPI chip-select: a spare Daisy pin or the 74HC595 latch (control rate is fine).
- **The dry stays analog.** No converter touches it; the digipot is a resistor network. It does add a part in the dry path, so eng should confirm it meets "the dry path analog and never switched" (`daisy-first-principles.md` §6.1) in spirit.
- **Why not a passive pan pot:**
  - a passive pot (a dual-gang: one gang audio, one gang DC so the Daisy knows its position for FOLLOW) works, but **can't take MIDI**;
  - the pan's CC 10 was already decided. The digipot gives CC 10, FOLLOW and jump-on-move from one knob.
  - **Fallback:** the passive dual-gang, knob-only, with FOLLOW still possible.

**2. DELAY PAN: in the DSP.**
- It places the echo's output on the outputs **and** where it enters the reverb, so the reverb image follows the repeats.
- Reverbs take **stereo input** (PLATE / SPRING / SHIMMER get two input diffusers: ≈ +10–15 % of one reverb's load, ESTIMATE). The pans cost nothing measurable.
- **PING-PONG:** the repeats alternate starting on the pan's side.

**3. FOLLOW: one 2-way toggle, OFF / FOLLOW.**
- **FOLLOW:** the delay pan takes the dry pan's position (same side, his answer). The DELAY PAN knob is inactive.
- **OFF:** the delay pan goes back to its own knob. The toggle's position shows the state; no jump surprises beyond that.
- **The old VOICE PAN** (the send into the effects) **merges into DRY PAN.** The Daisy places the voice's send where the dry sits, so the dry's reverb starts on its side. No extra knob.

**What each output hears** (constant-sum laws throughout):
- **Speaker** (mono sum (L + R)/2): **no level change** as either pan moves.
- **Phones / line out with a stereo plug:** both pans as set.
- **LINE OUT with a TS (mono) plug:** the tip must carry L + R. With the dry now panned in analog, the firmware wet-mono trick (§15.4) **isn't enough** (a dry panned right would vanish from the tip). So the **74HC4053 analog-switch route becomes required**: on TS it sums R into the LINE OUT's left driver. Generic part ≈ $0.50, UNVERIFIED.
- **Phones with a TS plug:** L only, as stated in §15.4 (a dry panned right is quiet there). Accepted.

**MIDI:**
- DRY PAN **receives CC 10**, jump-on-move (the digipot makes this possible).
- DELAY PAN **receives CC 102** (proposal, undefined CC), jump-on-move.
- **FOLLOW is a switch: MIDI never flips switches**, as the rule says.
- **Whether moving these knobs (or any MIDI-controllable knob, or the keys) *sends* MIDI is open with the owner.** It's not assumed here.

**Placement (layout B's effects row, d 83.85) [CHECK §9, fourth run: 0 violations]:**
- **DRIFT 33.5 | ECHO: TYPE 62.5 · TIME 82.5 · REPEATS 102.5 · MIX 122.5 · DELAY PAN 142.5 | REVERB: TYPE 171.5 · DECAY 191.5 · MIX 211.5 | DRY PAN 240.5 · VOLUME 260.5**;
- **FOLLOW toggle at (250.5, d 73)**, in front, between DRY PAN and VOLUME (nearest: L SUSTAIN 2.50, DRY PAN 2.71, VOLUME 2.71);
- breaks 48 / 157 / 226; FREE / SYNC unchanged.
- **DRY PAN and VOLUME legends go behind their knobs** (the toggle sits where their legends were); words "off" / "follow" beside the toggle.
- The model needs these for §7's label check (visual).
- **TAP moves back to the base, x 261** (v1.1 spot) ⚑.

**Cost, power, mux (ESTIMATE, UNVERIFIED):**
- digipot ≈ $1.5, two pots + knobs ≈ $1.8, toggle ≈ $0.5, 74HC4053 ≈ $0.5: **≈ $4–5** over §15.1's stereo stage.
- Mux: **+3 channels** (2 pots, 1 toggle) on top of B's moves (eng: lid mux count).
- 1 SPI chip-select. A few mA.

## 16. Steer 2: resolving the band (owner 16:52: "there's a massive horizontal gap -- the speaker doesnt feel resolved. this may mean moving components")
Checker: `layout_check.py` (this folder), now with the visual designer's two legend rules (switch-line legends beside their toggles at 1.55; behind-legends 1.0 further back) and an FX-row centring rule: **0 violations**. On the visual model with real Kalam text (`branch_check` §7 collide on `rb.Nave`): **0** legend, tick and control collisions. Numbers marked [CHECK] come from these.

### 16.1 Root cause (what forces the gap)
- Closed, a base point at y lands under lid d = 108 − y. The base PLAY row (y 68) lands at **lid d ≈ 40**.
- The PLAY knobs stand 13.5 above the plate (CUTOFF 12.15, the bend stick 12.6), and lid knobs reach down 13.5 from the lid face (closed z 37.6). They'd overlap by ≈ 5 mm, plus the 2.0 clearance rule.
- So no lid knob can sit over the PLAY row. That's the 37.55 mm knob-free band (other rows are ≈ 8.5 apart edge to edge).
- **The speaker was put in the band because the band was empty. It never caused it.**

### 16.2 The new arrangement (both routes share it)
**Lid: three evenly spaced rows, one switch line, one round opening on the axis.**

| Row (lid d) | Left (x) | Centre | Right (x) |
|---|---|---|---|
| **V1, d 14.45** | RANGE 1–3 23.5 / 43.5 / 63.5 · FREQ 2 83.5 · **OSC 1 103.5** | (opening) | **OSC 3 182.5** · F ATT / DEC / SUS 202.5 / 222.5 / 242.5 · KBD CTRL (t) 262.5 |
| **switch line, d 32** | OSC MOD 23.5 · OSC 3 CTL 43.5 · PARA 63.5 | **Ø 46 opening, centre (143, d 32)** | SOURCE 182.5 · FILTER MOD 202.5 · VELOCITY 222.5 · AFTERTOUCH 242.5 |
| **V2, d 49.5** | WAVE 1–3 · FREQ 3 83.5 · **OSC 2 103.5** | (opening) | **NOISE / EXT 182.5** · L ATT / DEC / SUS · DECAY (t) 262.5 |
| **FX, d 84.55** (re-centred on x 143: span 44–242) | ECHO TYPE 44 · TIME 64 · REPEATS 84 · MIX 104 · DELAY PAN 124 | | REVERB TYPE 153 · DECAY 173 · MIX 193 · DRY PAN 222 · VOLUME 242 |
| FX toggles, breaks | FREE / SYNC (77.5, d 69.7) · breaks 29.5 / 138.5 / 207.5 | | FOLLOW (232, d 73) |

- **Row pitch is 35.05 everywhere** (V1 → V2 → FX). The switch line sits midway between V1 and V2.
- **The only knob-free area wider than a row gap is the round opening.**
- **The mixer is symmetric around the opening:** OSC 1 / OSC 2 on the left, OSC 3 / NOISE on the right, mirrored about x 143 (± 39.5).
- **Legends:** V1 in front; V2 behind; switch toggles above; TIME, REPEATS, DRY PAN and VOLUME behind; FREE / SYNC and FOLLOW words beside.

**Base PLAY row, symmetric about x 143:**
- **BEND 25 · MOD 47 · TUNE 67 · GLIDE 87 | EMPHASIS 119 · CUTOFF 143 (hero, on the axis) · CONTOUR AMT 167 | MOD MIX 199 · DRIFT 230 · TAP 261**;
- the right group's three controls are spaced evenly over the same extent as the left group's four (25–87 ↔ 199–261), so nothing reads as a missing knob. **R3 is removed** (director);
- the stick and TAP mirror each other;
- **CUTOFF moves to the axis** (it was at 119; EMPHASIS takes 119), so CUTOFF lands **entirely under the opening** when closed. EMPHASIS and CONTOUR AMT land partly under it [CHECK].

**Moves (⚑ director, then owner; the R3 knob and the off-centre FX row are fixed):**
- the mixer re-flowed round the opening;
- the switches into one switch line;
- **CUTOFF ↔ EMPHASIS** swapped;
- **MOD MIX** (lid → base, beside the pitch controls it feeds) and **DRIFT** (lid FX row → base) moved;
- **R3 removed** (it had no function).
- **The effects row is re-centred on x 143 ± 99 → 44–242**, so the lid's top-left corner isn't left empty after DRIFT moved (director fix 1).

**The battery moves to the base.**
- With rows evenly spaced, the under-plate clear zone between V1 and V2 shrinks from 37.55 to ≈ 21. FOLD-105's four 25 × 40 × 9.5 cells (PiShop 952540) no longer fit under the lid plate.
- They go to the **base's rear strip** (y ≈ 80–106, x ≈ 15–185, under-plate height 11.1 ≥ 9.5) beside the Daisy (rear right).
- **Eng:** the base board needs a window there, and the hinge ribbon's base header (now under the landing strip) moves.
- **Bonus:** the base gets heavier and the lid lighter, so the standing tip threshold rises from ≈ 6.9 N to **≈ 8.4 N** [CALC, cells ≈ 90 g ESTIMATE].

### 16.3 The two routes for closing [CHECK]
**In plain words for the owner:**
- **≈ 55.2 mm closed (R-LOW) holds only if two things are true:**
  - the played row's pots are snap-in types (no nut above the plate), or the plate is counterbored over the nuts;
  - the bend stick is seated 3.6 mm lower.
- Otherwise it's **56.7 mm** (knobs sitting on nuts) up to **58.8 mm** (stick as is).
- **R-LOW also shrinks the played row's knobs from Ø 14.9 to Ø 10** (8 mm tall). CUTOFF stays the big hero.
- **His alternative is R-TALL:** keep today's big knobs everywhere and close at **≈ 59.7 mm**.

Every lid item landing within 3 mm (plan) of a base item must clear it by 2.0. Today the lid face sits at closed z 37.6 (closed 52.7).

| Route | Base row parts | Binding pair | Lid face | **Closed** |
|---|---|---|---|---|
| **R-TALL (fallback)** | today's knobs (13.5) | WAVE 2 over MOD | 44.6 (+7.0) | **≈ 59.7 mm** |
| R-LOW, stick as is | low knobs (9.0 incl. 1.0 seat), stick 12.6 | WAVE 1 over the BEND stick | 43.7 (+6.1) | ≈ 58.8 (barely better: the stick binds) |
| **R-LOW (primary)** | low knobs (9.0), **stick cap top lowered to plate + 9.0** | WAVE 1 over the stick | **40.1 (+2.5)** | **≈ 55.2 mm** |
| R-LOW, nut under the knob | low knobs on a nut (10.5), stick 9.0 | WAVE 2 over MOD | 41.6 (+4.0) | ≈ 56.7 |

- **The low knob (a real part):** Tayda aluminium knob **Ø 10 × 8 mm, 6 mm 18T**, $0.59. **Black** (https://www.taydaelectronics.com/aluminum-d-shaft-knob-3010-black-6-x-18t.html; the page lists shaft hole 6 mm × 18T) or **gold**, a brass-tone match for the keys (https://www.taydaelectronics.com/aluminum-gold-knob-3010-black-6-x-18t.html). Silver exists too.
- Checked and **not** better: Thonk Stubby T18, Ø 9.85 × 11 (https://www.thonk.co.uk/shop/stubby-knobs-t18/).
- **No wide, low hero exists as a bought part** in what I checked. Tayda's ≥ 20 mm knobs are all ≥ 15 tall; Multicomp KMK25 is 25 × 15 (https://my.element14.com/multicomp-pro/fc7253/round-knob-kmk25-black-6mm-spline/dp/2473097).
  - So **CUTOFF keeps a tall hero** and sits under the opening instead. That's why it moves to the axis.
- **What R-LOW depends on (UNVERIFIED, eng):**
  1. **Seat height.** A 9 mm pot's threaded bushing and nut stand ≈ 2–2.5 above a 2.5 mm plate. With a nut, the knob sits on it (10.5) → 56.7. A bushing-less (snap-in) 9 mm pot, or a plate counterbore over the nut, gives ≈ 1.0 → 55.2.
  2. **Shaft length bought to fit** (no cutting: owner, no machining). The 8 mm knob needs ≈ 7 mm of T18 shaft above the plate.
  3. **The bend stick lowered** ≈ 3.6 mm (module seated deeper in a board cut-out) with enough cap left to thumb. If the stick can't go lower, R-LOW gives only ≈ 58.8, and **R-TALL's simplicity wins**.
- **Feel cost of R-LOW:** the played row gets small 10 mm metal knobs (from 14.9). CUTOFF stays big.
- **Both routes:** the hinge axis rises by half the lid-face change. Standing geometry is otherwise unchanged; the stays work as before.

### 16.4 The speaker, from acoustics
- **Driver:** the 50 mm CDS-5076-class (7.6 deep), concentric under the opening at lid (143, d 32). Sd ≈ 12.6 cm² for an effective cone ≈ Ø 40 (ESTIMATE; datasheet Sd UNVERIFIED).
- **Opening Ø 46** (cone + surround), the plate's only hole there. With **vertical slots 1.5 wide on 2.7 pitch (webs 1.2)**, it's **≈ 56 % open → ≈ 920 mm² ≈ 73 % of Sd**. With 2.0 slots / 1.2 webs, ≈ 63 % → ≈ 1,040 mm² ≈ 83 % of Sd [CALC].
  - Today's grilles were 265–440 mm² (≈ 21–35 % of Sd): choked.
- **Slots run vertically** (his preference), so they read as **lancets inside a rose**. The slot lengths follow the circle; plate 2.5 thick. Keep the **cone-to-plate gap ≥ 1.5 mm**, so the front cavity's resonance stays high (≈ > 8 kHz, ESTIMATE).
- **Front gasket:** a 1 mm adhesive foam ring between the driver frame and the plate's underside, so the front can't leak to the back.
- **Sealed, stuffed back box:** printed PETG, glued behind the driver, ≈ 60 × 60 × 10 mm outside, **≈ 20–25 cm³ net**, lightly filled with polyester fibre (worth ≈ +15 % effective volume).
  - **This matters most.** Without it the rear wave cancels the front through the lid hollow, and bass and mids collapse.
  - It fits under the lid plate (10.6 deep). It clears V1 / V2 pot bodies (x 103.5 / 182.5) and the ribbon header (x 176–227, d 2.5–8.5) [CALC].
- **Honest loudness:** a small sealed box raises the driver's low cut-off (≈ 600–900 Hz, UNVERIFIED). Expect clear mids and modest level; it's a monitor, not a PA.
  - The gain over today comes from the open area and the seal, roughly **+3–6 dB in the 1–5 kHz range** (ESTIMATE). Bench it.
  - PAM8302 class-D (review 20) stays the louder-amp option.
- **Magnet distances:**
  - open, the speaker sits ≥ 74 mm from the base PLAY row and ≥ 92 mm from the key Hall sensors;
  - keep ≥ 30 mm from the lid's expo pairs at layout (eng).
  - Closed it doesn't matter (off).

### 16.5 Keys: more brass (owner: "i'd rather have more brass than black")
- **Lead A:** brass naturals, black sharps. **Alternate C:** all brass.
- **Sharps' material (systems pick): black-plated cast brass**, the same mass as the naturals, so **one velocity calibration** covers all keys. Printed black sharps would be lighter and need a per-group velocity curve (§13).
- The gold Tayda low knobs (R-LOW) would echo the brass on the played row (visual).

## 17. Steer 3: the lid in signal order (owner: "synth stuff -> fx stuff -> output stuff like volume")
Owner, in full: "the items do not appear to be grouped or ordered in a way that makes logical sense … i dont like the effects controls at the top … when i think of signal order it's synth stuff -> fx stuff -> output stuff like volume. so it at the top of the layout is confusing."

Checker: `layout_check.py` now holds two arrangements: **P** (live, recommended) and **S** (the alternative, run with `layout_check.py S`). It also measures what the renders print that the old check ignored: the TYPE knobs' name fans, TIME's note scale and ring, and the group headings. **Both arrangements: 0 violations, labels included.** Closing doesn't change: R-LOW ≈ 55.2, R-TALL ≈ 59.7 (now the filter contour binds over the stick and MOD, where WAVE 1 / 2 did). The base PLAY row doesn't change.

### 17.1 What goes with what (every lid control)
Signal stage: 1 sources → 2 mixer → (filter: CUTOFF / EMPHASIS / CONTOUR AMT, on the base) → 3 contours → 4 echo → 5 reverb → 6 out.

| Control | Group | Stage | Its switches | Steer 2 had it | Where it belongs, and why |
|---|---|---|---|---|---|
| RANGE 1–3, WAVE 1–3, FREQ 2, FREQ 3 | oscillators | 1 | OSC 3 CTL (VCO 3 keyboard on/off), PARA (MONO / PARA / PARA+4), OSC MOD | split over two rows, mixed with mixer knobs | one row, by VCO (1: range, wave · 2: range, freq, wave · 3: range, freq, wave). Model D order. |
| OSC MOD | oscillators | 1 | it's a switch | switch line, left | It turns the wheel's modulation on for the **oscillators' pitch**, so it sits under the oscillators. |
| PARA | oscillators (voices) | 1 | it's a switch | switch line, left | It sets how many oscillators play notes, so it goes with the oscillators. Under VCO 1, the first switch of the voice. |
| OSC 1, OSC 2, OSC 3, NOISE / EXT | mixer | 2 | SOURCE (noise / ext / feedback) | **split around the window** (2 left, 2 right; the owner's screenshot) | one row of four, in order, straight after the oscillators. SOURCE sits under it: it picks what the NOISE / EXT knob sets (the Pro-One's shared noise/ext knob was "both a blessing and a curse"; §17.3). |
| F ATTACK / DECAY / SUSTAIN | filter contour | 3 | KBD CTRL, FILTER MOD | V1 right | Left of the window. **KBD and FILT MOD both move the cutoff** (keyboard tracking, wheel), so they sit under the filter contour. |
| L ATTACK / DECAY / SUSTAIN | loudness contour | 3 | DECAY (release = decay) | V2 right | Right of the window. DECAY changes this contour's release, so it sits under it. |
| VELOCITY (loud / both / filt) | key response | 3 | it's a switch | switch line, right | It sends key velocity to the **contours** (loudness, filter, or both), so it belongs with them. Its default is loudness, so it sits under the loudness contour. |
| TOUCH (mod / off / filt) | key response | 3 | it's a switch | switch line, right | It sends pressure to mod amount or cutoff. Keep it beside VELOCITY: they're the "how the keys respond" pair (aftertouch.md). MicroFreak shows the cost of hiding this (§17.3). |
| ECHO TYPE, TIME, REPEATS, MIX | echo | 4 | FREE / SYNC | FX row at the far edge | the first effect: kind → time → repeats → amount. FREE / SYNC belongs to TIME. |
| DELAY PAN | echo → reverb | 4→5 | (FOLLOW) | FX row | It pans the echo into the reverb, so it's the echo's last control, the hand-off to the reverb. |
| REVERB TYPE, DECAY, MIX | reverb | 5 | none | FX row | the second effect, after the echo. |
| DRY PAN | out | 6 | FOLLOW (delay pan follows dry) | FX row | It places the dry sound in the stereo output, so it's an output control. |
| FOLLOW | out | 6 | it's a switch | beside VOLUME | It links DELAY PAN to DRY PAN, so it sits with DRY PAN. |
| VOLUME | out | 6 | none | FX row, at the top | **The last thing in the chain**, so it goes last on the page, nearest the hand. |

Where the contour, velocity and touch switches belong:
- **Contour switches:** each sits under the contour it changes.
- **VELOCITY and TOUCH:** together, as a pair, under the loudness contour. They act on the contours (and TOUCH on mod), not on the effects or the oscillators.
- In steer 2, all of these shared one switch line with the oscillator switches, with nothing to say whose they were. That was the "no logical sense" the owner saw.

### 17.2 Reading direction (both positions read the same)
- **Flat:** the lid lies behind the base (hinge at the base's back edge). A lid point at d sits d beyond the hinge, so the lid's far edge is the farthest thing from the player: the top of what they see.
- **Standing:** d is height above the hinge, so the far edge is again the top.
- So in both, **top = far edge (d ≈ 84), bottom = the hinge (d ≈ 14)**. The owner's screenshot shows it (FX across the top).
- **The eye reads top → bottom, left → right in each band** (like a page). Then it drops over the hinge to the base PLAY row (bend, mod, tune, glide | emphasis, CUTOFF, amount | mod mix, drift, TAP), then the keys.
- So the lid's bottom band, next to the base, is both **the end of the sound** and **the nearest to the hand**. Effects and VOLUME are ridden live; oscillators are set and left. That's why page order is also the right reach order (§17.4).

### 17.3 References (verified, quoted; links checked 2026-11-13)
| Instrument | What the source says | What we take |
|---|---|---|
| **Minimoog Model D** | "The familiar left-to-right layout of Controllers, Oscillator Bank, Mixer, Modifiers and Output sections" ([vintagesynth.com](https://vintagesynth.com/moog/minimoog)). The manual: "The front panel groups these elements and controls together by type—CONTROLLERS, OSCILLATOR BANK, MIXER, MODIFIERS, OUTPUT" (p. 15); "The combined output of the Mixer next passes through the Filter and finally arrives at the audio output" (p. 26). The A-440 is in the OUTPUT section (p. 32) ([Model D manual](https://cdn.inmusicbrands.com/Moog/Model%20D/Minimoog_Model_D_Manual.pdf)). Its panel "can lay flat or propped up" (vintagesynth). | Group by stage, in signal order, with output last. The Model D reads left → right; our window blocks two-thirds of a column flow (§17.4 S), so we read top → bottom instead. |
| **Moog Grandmother** | The spring reverb is "a single-knob affair placed in the right hand corner of the dash"; the panels "are laid out to mimic a modular workflow" ([AudioTechnology](https://www.audiotechnology.com/reviews/moog-grandmother)). The manual: "The VOLUME knob is placed after the SPRING REVERB MIX knob in the signal path" (p. 21, [manual](https://analoguehaven.com/moog-music/grandmother/manual.pdf)). | The effect sits at the end of the panel, next to the output, with volume after it. |
| **Moog Matriarch** | "The penultimate stage in the internal signal path is a pair of BBD delays … At the end of the signal path, the internally routed audio reaches the Output section"; "the VCAs themselves lie between the filters and the delays"; the output section is "to the right of the control panel" ([Sound On Sound](https://www.soundonsound.com/reviews/moog-matriarch)). "The signal then passes into the dual filter, then moving right along to a stereo VCA and stereo analog delay" ([Perfect Circuit](https://www.perfectcircuit.com/signal/moog-matriarch-spotlight)). | Stereo delay after the loudness stage, output after the delay: exactly our order (echo → reverb → out), even with stereo pans. |
| **Korg minilogue xd** | The manual's panel callouts run 1 MASTER … 4 MIXER, 5 FILTER, 6 AMP EG / EG / LFO, **7 EFFECTS**, then display and sequencer (p. 5, [manual](https://cdn.korg.com/us/support/download/files/a5bba576f00973bf63c78cdeff83a7f7.pdf); numbering only, not positions). Effects: "use two levers to select your type and the dials to the right define its impact" ([MusicTech](https://musictech.com/reviews/hardware-instruments/korg-minilogue-xd/)). Voice mode "more intuitively located adjacent to the Oscillator section" ([AudioTechnology](https://audiotechnology.com/?p=38690)). | Effects come after the envelopes. Within an effect, kind first, then amount (our TYPE → … → MIX). The voice-mode switch goes with the oscillators (our PARA). |
| **Sequential Take 5** | "a fabulous large Filter Cutoff dial in the centre of the synth"; "over on the right are two Effects blocks. The lower one is a dedicated reverb" ([MusicRadar](https://www.musicradar.com/reviews/sequential-take-5)). "Most controls are single function" ([Recording](https://www.recordingmag.com/resources/featured-reviews/october-2022-sequential-take-5/)). | The hero cutoff goes on the axis (ours, on the base). Effects form a block at the end, with reverb after the other effect. This is the model for arrangement S. |
| **Waldorf Iridium** | "The front panel retains the full‑colour touchscreen at the centre, surrounded by the most useful controls for oscillators, filters, envelopes, LFOs and effects" ([Sound On Sound](https://www.soundonsound.com/reviews/waldorf-iridium-keyboard?amp)). | A central object with the groups around it works. Our window is that object: the two contours and the two effects flank it. |
| **Elektron Digitone** | The parameter keys run "TRIG, SYN1, SYN2, FLTR, AMP, LFO"; "[AMP] takes you to the AMP page, where you find parameters for the amplitude envelope and effect sends"; delay and reverb sit on FLTR's and AMP's second functions (p. 12, [manual](https://cdn.www.elektron.se/media/downloads/digitone/Digitone_User_Manual_ENG_OS1.40_220929.pdf)). Digitone II: "all parameters have been reorganised in a much more intuitive layout, especially the effects" ([Sound On Sound](https://www.soundonsound.com/reviews/elektron-digitone-ii)). | Page order = signal order, and the effect sends live right after the amp (loudness) stage. That's arrangement P: loudness contour, then echo. |
| **Pro-One (counter-example)** | The modulation section is at the panel's left ("The modulation section (left)", [Electronics & Music Maker via muzines](https://www.muzines.co.uk/articles/sequential-circuits-pro-one/4225)). Its reissue's modulation "takes a little getting used to" ([MusicTech](https://www.musictech.net/reviews/hardware-instruments/behringer-pro-1-review/)). "The noise volume control also doubles as the external input level … both a blessing and a curse" ([Sound On Sound](https://www.soundonsound.com/reviews/sci-pro1)). | Switches placed away from what they change cost learning; a dual-meaning knob needs its selector beside it. So OSC MOD goes under the oscillators, FILT MOD under the filter contour, and SOURCE under NOISE / EXT. |
| **Arturia MicroFreak (counter-example)** | "It turns out that there are some patch settings in a Utility menu … it's not immediately apparent how to harness velocity"; the envelope "has a linked decay/release time" ([Sound On Sound](https://www.soundonsound.com/reviews/arturia-microfreak)); "control of the Decay and Release times is ganged on a single Decay/Release control which purists may criticise" ([AudioTechnology](https://audiotechnology.com/?p=39980)). | Key response hidden away goes unused, so VELOCITY and TOUCH stay on the panel, by the contours. Our DECAY switch (release = decay) is the Model D's honest form of that ganging; it sits under the loudness contour, so it's clear what it ties. |

Not found in any source checked: a description of the Take 5's or minilogue xd's exact left-to-right section map. Above I use only what's quoted.

### 17.4 Arrangements (both pass the checker; same 28 knobs, 11 toggles, same window, same base)
**P: page order (the director's lead).** Three bands, top → bottom = signal order:
```
 far edge (top)
 A  d 84.55  range1 wave1  ·  range2 freq2 wave2  ·  range3 freq3 wave3  ‖  osc1 osc2 osc3 noise   <- oscillators ‖ mixer
 A' d 70     para            osc mod              osc 3 ctl                source
 B  d 49.5   kbd | f.attack decay sustain  (  window  )  l.attack decay sustain ‖ dry pan         <- contours, mirrored ‖ out
 B' d 33–35  filt mod                      (   Ø 46   )  velocity touch decay    ‖ follow
 C  d 14.45  type time [free/sync] repeats mix delaypan ( ) type decay mix        ‖ volume          <- echo · reverb ‖ out
 hinge (bottom) — base: bend mod tune glide | emphasis CUTOFF amount | mod mix drift TAP
```
- **Groups:**
  - each group is one run of knobs, with its switches 14.5–14.55 mm beneath. That's 6 mm closer to their own knobs than to the next row (20.5), so they read as belonging (proximity);
  - two engraved breaks: oscillators ‖ mixer (x 183, band A), and the out column (x 242.5, bands B–C).
- **Signal-path breaks (where the eye's path departs from signal order):**
  1. Two line wraps, as in any page: mixer (row A's right end) → filter contour (row B's left), and loudness contour → echo.
  2. The filter itself (CUTOFF, EMPHASIS, CONTOUR AMT) is on the base, not between mixer and contours. Unchanged since steer 2: the base is the played row.
  3. The out column starts at band B's height (DRY PAN beside the loudness contour), behind a break line. It reads top → bottom: DRY PAN, FOLLOW, VOLUME.
  4. TAP (base right) is ≈ 208–226 mm from echo TIME / FREE / SYNC (lid bottom left). It was 217–236 in steer 2, so no worse, but still apart. Open item V3.
- **Reach** (path from the base control over the hinge, lid unfolded; steer 2 → P):
  - VOLUME from TAP 132 → **60**;
  - ECHO MIX from CUTOFF 136 → **77**;
  - REVERB MIX 140 → **100**;
  - ECHO TIME 153 → **116**;
  - FREE / SYNC 133 → **101**.
  - Set-and-leave controls move away: OSC 1 72 → 141, F ATTACK 85 → 153, RANGE 1 134 → 174.
  - **The live controls come ≈ 30–70 mm closer; the patch-building ones go ≈ 40–70 further.**
- **Checks:** 0 violations (pitch, gaps, breaks, window, edges, seam, far rim, legends, TYPE fans, TIME scale, headings). Closed: R-LOW 55.2 / R-TALL 59.7, unchanged.

**S: left-to-right stages (differs in kind; Take 5 / Grandmother "effects on the right").** Synth across the left two-thirds; effects + out as a 4-column block on the right:
```
 A  d 84.55  range wave range freq wave range freq wave (VCO 1 2 3)  ‖  echo: type time repeats mix
 A' d 70       para          osc mod   decay*       osc 3            ‖     free/sync
 B  d 49.5   osc1 osc2 ‖ f.att dec sus   ( window )                  ‖  delay pan · rev type decay mix
    d 32       src       kbd fm vel tch  (  Ø 46  )
 C  d 14.45  osc3 noise ‖ l.att dec sus  (        )                  ‖  dry pan  follow  volume
```
- **Signal-path breaks:**
  1. **The echo is still across the top** (band A, right): half the owner's complaint stays.
  2. The mixer becomes a 2 × 2 square split over two rows (OSC 3 and NOISE under OSC 1 / 2).
  3. Four contour and key switches squeeze into one line between the contour rows. Their legends shrink to **kbd / fm / vel / tch**.
  4. **DECAY\* has no room by its contour** and has to sit among the oscillator switches. That's exactly the kind of misplacement the owner objected to.
- **Reach:**
  - DRY PAN 72 and FREE / SYNC 121 from TAP are better than P's.
  - But ECHO MIX 176 and REVERB MIX 153 from CUTOFF are worse than P's (77 / 100), and worse than steer 2's (136 / 140).
- **Checks:** 0 violations, but only with abbreviated legends and DECAY moved. Closed: same routes.
- **Why it can't do better:** the window takes the middle of bands B and C, so a right-hand effects block leaves the synth 18 knob slots for 18 knobs, with no slot for a break or a switch. **Left-to-right flow needs the window moved off-axis.** That reopens steer 2 (CUTOFF on the axis under it), so S is shown for comparison only.

### 17.5 Recommendation: P
- **It answers the owner directly:**
  - effects leave the top;
  - the order down the page is synth → effects → out;
  - VOLUME is the last control on the page, in the bottom-right corner, above TAP.
- **Every switch sits under the group it changes.** Nothing shares an anonymous switch line.
- **The window earns its place:**
  - between the two contours (filter left, loudness right; one "contours" heading over it);
  - between the two effects (echo left, reverb right).
- **The live controls (effects, pans, VOLUME) move nearest the hand.**
- Cost: the oscillators move farthest away. They're the set-and-leave group; the Model D's oscillator bank is likewise not its played row.

### 17.6 New x / d table (P, live in `layout_check.py`; score-8 fixes 1, 3, 5 and the visual's 9-condition tweaks, f4099ab, applied)
| Band (lid d) | Left edge column (x 23.5) | Left of the window (x) | Centre | Right of the window (x) | Out column (x 262.5) |
|---|---|---|---|---|---|
| **A, d 84.55** (legends behind, numbered) | RANGE 1 "range 1" | WAVE 1 43.5 ·· RANGE 2 68.5 · FREQ 2 88.5 · WAVE 2 108.5 ·· RANGE 3 133.5 · FREQ 3 153.5 · WAVE 3 173.5 | | **break x 188.0 (d 70.5–93.5)** · OSC 1 202.5 · OSC 2 222.5 · OSC 3 242.5 | NOISE / EXT |
| **A', d 70** (legends right) | | PARA 33.5 · OSC MOD 88.5 · OSC 3 CTL 153.5 ("osc 3 ctl") | | SOURCE 242.5 | |
| **B, d 49.5** (legends behind) | **KBD CTRL (toggle)** · **rule x 43.5 (d 31–58.5)** | F ATTACK 63.5 · F DECAY 83.5 · F SUSTAIN 103.5 | Ø 46 window (143, d 32), unchanged | L ATTACK 182.5 · L DECAY 202.5 · L SUSTAIN 222.5 | **break x 242.5 (d 7–58.5)** · DRY PAN |
| **B', d 35** (legends right; FOLLOW d 32.8) | **FILTER MOD (d 35)** | (none) | | VELOCITY 178.5 · TOUCH 199.5 · DECAY 222 (d 35) | FOLLOW (d 32.8; "off" left, "follow" right, at ± 6.4) |
| **C, d 14.45** (legends in front) | ECHO TYPE | TIME 43.5 · FREE / SYNC 62 ("sync" above, "free" below; 1.75 from the toggle, size 1.69) · REPEATS 76 · MIX 96 · DELAY PAN 116 | | REVERB TYPE 182.5 · DECAY 202.5 · MIX 222.5 | VOLUME |
| **Headings** (Kalam 3.0, above the 2.35 legends) | "filter" (21.0, d 66.5) | "oscillators" (98.5, d 101.45) · "filter contour" flush left at x 56.05, d 67.5 · "echo" (69.5, d 26.5) | | "mixer" (232.5, d 101.45) · "loudness contour" flush left at x 175.05, d 67.5 · "reverb" (204.5, d 26.5) | "out" (262.5, d 66.5) |

- **Fix 1 (band B balance):**
  - every band-B x mirrors about the axis (23.5 / 63.5 / 83.5 / 103.5 ↔ 262.5 / 222.5 / 202.5 / 182.5); the checker confirms;
  - the filter contour's two switches form a left-edge column (KBD at d 49.5, FILT MOD at d 35), opposite the out column (DRY PAN at d 49.5, FOLLOW at d 32.8);
  - per the visual (f4099ab), the column has its own "filter" heading and a rule at x 43.5 (d 31–58.5) that mirrors the out column's heading and rule;
  - FILT MOD moved up to d 35, clear of ECHO TYPE's fan.
- **Fix 3 (VCO groups):** 20 mm pitch inside a VCO, 25 mm between VCOs (edge gaps 5.1 vs 10.1), using the row's full width. The legends carry the VCO number. Underlines aren't needed; the visual can add them if the spacing doesn't read in the render.
- **Fix 5 (labels):** "range 1…3" / "wave 1…3", "osc 3 ctl" and the two contour headings are now in the checker. **0 violations, with headings at 3.0.** Closing is unchanged (R-LOW 55.2 / R-TALL 59.7).
- **For the visual (rb.py `nv_overrides`):** the checker now carries every f4099ab tweak itself:
  - FILT MOD at d 35;
  - the "filter" heading and rule;
  - contour headings at d 67.5; the osc | mixer break from d 70.5;
  - "oscillators" / "mixer" at d 101.45; "reverb" at x 204.5;
  - FOLLOW's words beside at ± 6.4;
  - up / down words 1.75 from the toggle.
  
  Make `nv_overrides` a pure pass-through. Otherwise the d + 0.4 and x + 2.0 nudges apply twice, and the "filter" heading and rule are drawn twice.
- FREE / SYNC: moved from beside TIME to the right of TIME's printed scale ("1/4" reaches to x ≈ 56; the toggle edge is at 57.4).
- **Eng:** the 60 × 60 back box (x 113–173) needs its lower-left corner chamfered ≈ 18 × 18 to clear DELAY PAN's pot (x 116, d 14.45). That costs ≈ 1.6 cm³, so ≈ 19–24 cm³ net [CALC]. The lid harness and mux allocation don't change.

### 17.7 Open (steer 3)
- **V1 (visual):** rb.py to the new table: breaks, headings, "right" / "updown" legends. Then the real-Kalam check.
- **V2 (director):** P as recommended, or S for comparison.
- **V3 (team):** TAP (base right) sits far from echo TIME (lid bottom left). Options:
  - leave it (TAP is a tap, not a look-at);
  - or a later base swap of TAP with the stick side (breaks steer 2's symmetry). Not proposed now.
- **E1 (eng):** the back-box chamfer for DELAY PAN's pot; check the real pot body against the box.

## 18. Steer 4: the panel explains itself (review 2026-11-13, 7/10 for understanding; owner: "make it a 10")
Source: `design/reviews/2026-11-13-lid-layout-review.md`. The arrangement (P, §17) stays. Fixed: all seven items and both nice-to-haves. `layout_check.py` now also checks **the base row** (gaps, pitch, every legend as R-LOW draws it, the LEDs, the group headings, the stick ↔ TAP mirror). It also measures every new legend: each toggle's name and position words, the "keys" lead-in, the echo pan cue, FOLLOW's name, and the "para: detune" notes. **0 violations.**

### 18.1 Position legends, from the spec (review 1)
- **Convention (score-8 fix 1, supersedes lever-down → lever-up):** every toggle, lid and base, is mounted to **throw left / right** (the same part rotated 90°, $0, same height). Its position words read **left · middle · right**, so the line's order is the lever's motion.
- Each toggle prints its name, with its positions in a smaller line (Kalam 1.3) under it, beside the toggle (base: under it). FREE / SYNC prints "free · sync" in one line under its toggle; there's no room beside it, between TIME's scale and REPEATS.

| Toggle | Positions (in order) | Panel legend | Source | Spec clear? |
|---|---|---|---|---|
| PARA | MONO / PARA / PARA+4 | "mono · para · +4" | owner.md (paraphonic approved); paraphonic.md | Yes, but PARA+4's audio path is open (paraphonic.md option C would make it 2-way: "mono · para"). |
| OSC MOD | off / on | "off · on" | Model D manual p. 19 ("When this switch is set to ON, the Oscillators can be modulated by Oscillator 3, Noise, Filter Contour"); eng/architecture §1.8 (mod bus onto the VCOs) | Yes. On sends the mod mix (osc 3 ↔ noise, scaled by the wheel) to all three VCOs. |
| OSC 3 CTL | off (free) / on (keys) | "free · keys" | Model D manual p. 19 ("Turning the orange rocker switch to OFF releases OSCILLATOR–3 from keyboard control") | Yes |
| SOURCE | noise / ext / feedback | "noise · ext · fb" | jobs F2.3; eng/budget-variant (3-way toggle) | Yes |
| VELOCITY | LOUD / BOTH / FILT | "loud · both · filt" | keys-and-velocity.md (decided) | Yes |
| TOUCH | MOD / OFF / FILT | "mod · off · filt" | aftertouch.md (decided switch; positions eng) | Yes. The word "mod" vs "vib" is owner question 6 (decisions-open). |
| KBD (KEYBOARD CONTROL) | off / ⅓ / ⅔ | "off · 1/3 · 2/3" (spelled out: Kalam has no ⅓ ⅔) | eng/budget-variant (3-way: off / ⅓ / ⅔); eng/velocity-and-keys-v2; Model D manual p. 30 (KBD 1 = ⅓, KBD 2 = ⅔, both = full) | **Matches the spec, but full isn't reachable** (§18.6). |
| FILT MOD | off / on | "off · on" | Model D manual p. 29 ("When this switch is on, the Filter Cutoff Frequency can be modulated by the Noise Generator, Filter Contour"); eng/architecture §1.8 (onto the filter node via 33 k) | Yes |
| RELEASE (was DECAY) | off / on (= decay) | name "release · both contours", positions "off · = decay" | eng/architecture §1.6 (on: release follows DECAY; off: the cap is dumped on key-up); Model D manual pp. 30–31 | Yes. **It acts on both contours**, and the name says so. |
| FREE / SYNC | free / sync | "free · sync", one line under the toggle | echo-sync.md (owner option B) | Yes |
| FOLLOW | own / follows dry | name "echo pan", positions "own · follows dry", as one unit beside the switch | panning-and-stereo-outputs.md (FOLLOW = echo pan takes the dry pan's value) | Yes |

### 18.2 What moved on the lid (new x / d; everything else as §17.6)
| Item | Was | Now | Why |
|---|---|---|---|
| PARA | (33.5, d 70) | **(23.5, d 70)**, legend "para / mono · para · +4" | PARA and OSC MOD act on the whole bank, so they sit together at its left (review 3) |
| OSC MOD | (88.5, d 70), under VCO 2 | **(50.0, d 70)**, "osc mod / off · on" | the same; x 50 per the visual (PARA's positions reached it at 48) |
| OSC 3 CTL | (153.5, d 70) | **(133.5, d 70)**, under RANGE 3, "osc 3 ctl / free · keys" | stays VCO 3's own switch |
| SOURCE | (242.5, d 70), under OSC 3 | **(262.5, d 70)**, under NOISE / EXT, "source / noise · ext · fb" | the selector beside the knob it re-points (review 2) |
| KBD, FILT MOD | lid column x 23.5, "filter" heading, rule x 43.5 | **base filter group** (§18.4); heading and rule **removed** | review 5, best option |
| DECAY switch | (222, d 35), under the loudness contour | **RELEASE at (143, d 61.5)**: on the axis, between the two contours, over the window; "release · both contours / off · = decay" | it acts on both contours (review 6; director fix 3) |
| VELOCITY, TOUCH | (178.5 / 199.5, d 35), under the loudness contour | **a "keys" column at the middle band's left** (visual, c38bf1f): VELOCITY (48, d 49.5), TOUCH (48, d 35); legends left of the toggles; heading **"keys"** (37, d 58), the mirror of "out" | fills the blank x 16–56 left by KBD / FILT MOD; band 2 reads keys → filter contour → release → loudness contour → out. Not at x 23.5: closed, both would land over the bend stick (R-LOW 58.8) |
| DELAY PAN | "delay pan" (116, d 14.45) | **ECHO PAN**, "echo pan", same place. Cue **"(off if follow)"** centred at (108, d 25.05), just above-left of the knob | one word per concept (review 7). The cue tells the player the knob is overridden when FOLLOW is on. |
| FOLLOW | "off / follow" | **"echo pan / own · follows dry"**, one unit to the right of the switch (ends x 279.8); nothing between the switch and VOLUME | names both ends and what it links (review 7; director fix 2) |
| FREQ 2, FREQ 3 | — | secondary **"detune"** (Kalam 1.3, light) right of each legend, d 96.5 | they become fine detune in PARA (owner.md paraphonic entry; review 9) |
| REVERB DECAY | "decay" | **"tail"**, same place | one word per concept: "decay" now means only the contours' decay (visual; effects.md updated; the MIDI CC map has no reverb-length entry) |
| FREE / SYNC | "sync" above, "free" below | **"free · sync" under it**, throwing left / right | one convention (director fix 1) |
| Contour headings | flush left at the first knob | **mirrored about the axis:** "filter contour" flush right at x 110.95, "loudness contour" flush left at 175.05 (d 67.5) | flush left, "filter contour" ran into OSC MOD |
| "out" heading | (262.5, d 66.5) | **(249.0, d 58.0)**, the column's top left, just above its break line | SOURCE now takes d 66–71 at x 262.5 |

**What echo pan does (one line):** it places the echo's output on L / R **and** where the echo enters the reverb, both together (panning-and-stereo-outputs.md: "It places the echo's output on the outputs **and** where it enters the reverb"). "Echo pan" is now the name everywhere in docs/; earlier sections of this file keep "delay pan" as history.

### 18.3 The base regrouped (review 4)
| Group (heading at y 85, left-aligned, Kalam 2.4) | Controls (x, all at y 68) |
|---|---|
| **controllers** (x 14) | BEND stick 25 · MOD 47 · **MOD MIX 67** · GLIDE 87 |
| **filter** (x 105) | **EMPHASIS 112.5** · **KBD (toggle) 126.4** · CUTOFF 143 (hero, axis) · **FILT MOD (toggle) 159.6** · **AMOUNT 173.5** |
| **tune** (x 191.5) | **TUNE 199** · **DRIFT 222** ‖ **break x 242.2 (y 56–80)** ‖ TAP 261, legend **"echo tap"**, alone at the end (director fix 4) |

- **Groups:** MOD MIX moved next to the wheel it feeds, and TUNE moved to the tune group (they swapped places: 67 ↔ 199).
- **Mirror:** the stick ↔ TAP mirror (25 ↔ 261) and the hero on the axis are kept.
- **Filter group:** EMPHASIS (119 → 112.5) and AMOUNT (167 → 173.5) open out by 6.5 each way to seat the toggles. Gaps hold for both R-LOW (Ø 10) and R-TALL (Ø 14.9) knobs. Group gaps: 87 → 112.5 and 173.5 → 199, both 25.5.
- **Toggle legends** sit under each toggle: "kbd / off · 1/3 · 2/3", "filt mod / off · on". They clear the "emphasis", "cutoff" and "amount" legends and the two LEDs at y 81.
- **Closing (re-run):**
  - re-run with every moved knob and the two toggles (bat 15.0, ESTIMATE): the numbers don't change. **R-LOW 55.2, R-TALL 59.7.** Binding: F ATTACK over MOD MIX (MOD MIX now at TUNE's old x 67). EMPHASIS (112.5) now lands under F SUSTAIN's edge and AMOUNT (173.5) under L ATTACK and VELOCITY, at the same heights as the binding pairs, so the face needed stays 40.1 / 44.6;
  - **New finding:** with KBD gone from the lid's left edge, nothing on the lid sits over the bend stick. R-LOW reaches 55.2 **with the stick as is** (12.6). **The stick no longer needs lowering**, which drops one of R-LOW's two conditions (§16.3).

### 18.4 KBD and FILT MOD beside CUTOFF: the closed-lid check (review 5)
- Closed, a base point lands under lid d = 108 − y. Both toggles (y 68) land at **lid d 40**: (126.4, 40) and (159.6, 40).
- That's **4.6 mm inside the Ø 46 window**, under the slotted grille. **No lid knob or toggle is within 3 mm in plan.** The nearest is F SUSTAIN at 12.7 mm (KBD side) and VELOCITY at 10.4 mm (FILT MOD side).
- So the only thing over each bat is the lid face. The back box is behind the grille, inside the lid, not below the face.

| Route | Lid face z | Free height above the base plate (z 15.6) | Clearance with a 15.0 mm bat (ESTIMATE) | Largest bat that keeps 2.0 |
|---|---|---|---|---|
| R-LOW | 40.1 | 24.5 | **9.5 mm** ✓ | 22.5 mm |
| R-TALL | 44.6 | 29.0 | **14.0 mm** ✓ | 27.0 mm |

- **The 15.0 mm bat is an estimate**: a mini toggle on a low nut, part UNVERIFIED. Even a long-bat toggle (≈ 20 mm) keeps ≥ 2.0 under R-LOW. Eng picks the part.
- **A condition I'm surfacing (it was already true in steers 2–3):** the closing check assumes every lid item hangs 13.5 mm, toggles included.
  - Three lid toggles land over base knobs: VELOCITY and TOUCH (keys column, x 48) over MOD / MOD MIX, and FOLLOW over TAP.
  - A lid toggle bat of 15 mm would need a face of 41.6, so **R-LOW becomes ≈ 56.7** unless the lid toggles stay ≤ 13.5 mm proud of the face (e.g. short-bat mini toggles).
  - Eng picks the part with that limit.
- **Fallback (not needed):** under the filter contour knobs, mirroring the loudness side's switches.

### 18.4b Visual's render fits, folded into the checker (c38bf1f, look doc rev 6)
- **Keys column:** as above.
- **Release:** "off · on" (now superseded by fix 3's "off · = decay" with "both contours" in the name).
- **Reverb:** "tail".
- **Notes:**
  - "detune" right of FREQ 2 / 3;
  - the "keys" lead-in note is gone.
- **Two-line legends, real-Kalam leading:**
  - lid: name at d + 1.1, positions at d − 1.25;
  - base: block top at y − TGL − 2.1, 0.9 between the lines.
- **Base knob legends** at y − 10.95, clear of the R-LOW tick ring (r 7.0, now measured).
- **CUTOFF's ± 90° ticks** are dropped (they ran into the KBD / FILT MOD bats).
- **Fractions:** spelled out, "1/3 · 2/3".
- **Result:** 0 violations, closing unchanged.

### 18.6 Score-8 fixes (director, steer 4): one switch convention, echo tap alone, KBD's real positions
- **Fix 1, every toggle throws left / right.**
  - It's the same part rotated 90° on its bushing: $0, same height.
  - **Clearance re-checked:** a ≈ 10 mm bat at ± 20° tips ≈ 3.4 mm off its axis (ESTIMATE, part UNVERIFIED). That stays inside the 4.6 mm nut circle every open-layout and closing check already uses. So legends, gaps and closing don't change: R-LOW 55.2 (stick as is), R-TALL 59.7. The base toggles still keep 9.5 / 14.0 mm under the window.
  - Words in throw order everywhere: "mono · para · +4", "off · on", "free · keys", "noise · ext · fb", "loud · both · filt", "mod · off · filt", "off · = decay", "free · sync", "own · follows dry", "off · 1/3 · 2/3".
  - Wiring: the middle position must be the middle word, so eng wires each 3-way so that left / right match the words.
- **Fix 2 (FOLLOW) and fix 3 (release)** are in the checker as one-unit legends beside the switch: "echo pan / own · follows dry" and "release · both contours / off · = decay". The visual owns the final wording; any change goes back through the checker.
- **Out column line restored (visual 4e52223):**
  - at x 262.5, FOLLOW's "own · follows dry" (≈ 13.8 wide in real Kalam) ran under the rim, so the visual moved FOLLOW alone to x 255;
  - instead, the **whole out column** (DRY PAN, FOLLOW, VOLUME) moves to **x 255** and its break to **x 238.75** (7 from REVERB MIX / L SUSTAIN's edge and from the column);
  - so the column is in line again, and the legend ends at x ≈ 275;
  - "out" heading at (249.5, d 66.5);
  - VOLUME now sits 6 mm left of TAP's x (255 vs 261);
  - closing unchanged.
- **Real-Kalam spacing (visual):**
  - two-line legends: name at d + 1.2, positions at d − 1.3;
  - "free · sync" 2.0 under its switch;
  - both in the checker, which gives 0 violations.
- **Fix 4, echo tap alone:** DRIFT 230 → **222**, and a **break at x 242.2** (y 56–80). It's 12.8 mm from DRIFT's edge and 12.8 from TAP's, both ≥ 7. TAP ("echo tap") now stands alone at the end, mirroring the bend stick at the start. Closing re-run: unchanged.
- **Fix 5, KBD's real positions:**
  - **What the spec gives:** a 3-way toggle, off / ⅓ / ⅔ (eng/budget-variant; eng/velocity-and-keys-v2). Architecture open item 7 says it "can't reach full". The Model D reaches full with both of its switches on (manual p. 30). Our one 3-way switch has three states, not four.
  - **The legend matches that spec exactly:** "off · 1/3 · 2/3". So, today, full isn't available.
  - **Proposed (eng to confirm; owner question 7 added):** filter keytrack is already a DAC CV (MCP4822 #4). Read the KBD toggle on a spare channel of mux D (it has 4 spare) and scale the CV in firmware. The three positions could then be **off · 1/2 · full**: full = 1 V/oct, for playing the self-oscillating filter, the main use of full tracking. The legend changes with the decision.
- **Checker:**
  - `layout_check.py` measures every new word: the throw-order lines, "free · sync" under its toggle, FOLLOW's and release's one-unit legends;
  - and the base break (≥ 7 from controls, legends ≥ 1.5).
  - **0 violations** (P; S unchanged).

### 18.7 Score-9 fixes (director: first-time walk passes every switch)
1. **FOLLOW on the out column's line:** done in 51be8ff. The whole column (DRY PAN, FOLLOW, VOLUME) sits at x 255, break at 238.75.
2. **The two lights by CUTOFF are named:**
   - **"midi"** at (131, y 86.0): the not-in-control light (coverage J8);
   - **"status"** at (155, y 86.0): the one status light (echo-sync.md).
   - Kalam 1.55, behind each light, clear of the "filter" heading and CUTOFF.
3. **Base:** "amount" → **"contour amt"** (167.0–180.0, 4.3 clear of "filt mod / off · on").
4. **SOURCE:** "fb" → **"fdbk"**; "feedback" doesn't fit inside the rim. SOURCE moves from 262.5 to **x 258** so "source / noise · ext · fdbk" ends at x ≈ 278.8 in real Kalam. The toggle is still under NOISE / EXT (its edge spans 255.05–269.95).
5. **TOUCH** moves up to **d 36.5**. Its legend is now **5.0 mm** from "ping-pong" (8.7 from "clean"; the rule needs ≥ 3.0, and the checker now enforces it).
- **New checker rule: the rim.** Every legend ends ≥ 1.5 inside the plate's inner edge (x 4.3–281.7, rb `lid_plate2d`), with widths × 1.25 for real Kalam. At x 262.5, SOURCE's line would fail (ends at 283.3); at 258 it passes.
- **Result:** 0 violations. Closing unchanged (R-LOW 55.2, R-TALL 59.7).

### 18.8 One-word labels (owner rule 19:57; director's `vocabulary.md`, supersedes the 18.7 fixes 3 and 4)
Owner, verbatim: "Labels should only be one word and follow best practices with obvious tweaks for understanding if there's a better word than the jargon". `layout_check.py` uses every word in `vocabulary.md` and re-measures each one: **0 violations**, rim and the touch ≥ 3 mm rule included. Closing is unchanged (R-LOW 55.2 with the stick as is, R-TALL 59.7).

| Where | Words now (positions left · middle · right) | Geometry change |
|---|---|---|
| oscillators | octave · wave · pitch; numerals **1 · 2 · 3** | **Numerals lead each VCO group at knob height** (x 10 / 56 / 121, d 84.55, Kalam 2.35), in the gaps before each group's first knob. There's no room *over* the groups: 2.1 mm between the legends' top (97.5) and "oscillators" (100.2) |
| oscillator switches | **voices: 1 · 3 · 4**, **mod: off · on**, **track: off · on** | track moves 133.5 → **163.5**, still under VCO 3, clear of the "envelopes" heading |
| mixer | **1 · 2 · 3 · extra**; **source: noise · input · loop** | SOURCE 258 → **257.5**, so its line ends inside the rim (≈ 280.0 in real-Kalam width) |
| envelopes | heading **"envelopes"** (3.0) on the axis at d 69.8; sub-heads **"filter"** and **"amp"** centred over their groups (x 83.5 / 202.5) on the heading line, Kalam 2.35 at d 68.5 (visual fec6093; lower down they read as "filter sustain" / "amp attack"). Light names sit 1.8 behind the lights; attack · decay · sustain under each | the two contour headings are replaced |
| release | **release: off · on**, centred on the axis at (143, d 61.5), under "envelopes" and between the groups. Its place says "both"; the manual says "on" = release follows decay | — |
| keys | **velocity: amp · both · filter**, **touch: mod · off · filter** | touch stays at d 36.5: 5.0 mm from "pingpong" |
| echo | type (**tape · dark · clean · pingpong**) · time (**free · sync** under its switch) · repeats · mix · **pan** | the "(off if follow)" cue goes; a **dot** (Ø 1.2) sits right of "pan" at (120.0, d 3.5) |
| reverb | type · **decay** · mix | — |
| out | **pan · link: off · on · volume**; heading "out" moves to (248.5, d 66.5) | the matching **dot** at (268.5, d 34.0), right of "link"'s legend |
| base | controllers (bend · mod · **blend** · glide) · filter (**resonance** · **track: off · 1/3 · 2/3** · cutoff · **mod: off · on** · **envelope**) · **tuning** (tune · drift) ‖ **tempo** (**tap**) | heading **"tempo"** at (255, y 85), left-aligned over TAP behind its break; "tune" → **"tuning"** |
| lights | **midi** (131), **status** (155) | kept at their spec positions: the not-in-control light is at 131 (coverage J8). The vocabulary lists them as "status · midi" without positions |

- **"detune" is gone.** The manual covers what pitch 2 / 3 do in para.
- **Docs mirrored:** effects, echo-sync, panning-and-stereo-outputs, midi (CC map: OCTAVE 1/2/3 was RANGE, PITCH 2/3 was FREQ), aftertouch, paraphonic, firmware-update-and-gestures (RESONANCE), architecture and README now use resonance, echo / out PAN, LINK, DARK, PINGPONG, reverb DECAY, oscillator 3 TRACK, VOICES, EXTRA and SOURCE noise / input / loop. Mode names (mono / para / para+4) stay where they name the feature.

### 18.5 Open (steer 4)
- **Eng:**
  - KBD amounts (§18.6);
  - the toggle part and its bat height (base and lid);
  - the back-box corner chamfer for ECHO PAN's pot (§17.6).
- **Visual:** rb.py to the new tables. In detail:
  - drop the "filter" heading and rule overrides;
  - draw the two-line toggle legends (`legend2`), `NOTES`, `BASE_TOGGLES`, `BASE_LEGEND` and `BASE_SECTIONS`;
  - the base now has two toggles, and TAP's legend is "echo tap".
- **Arrangement S (§17.4)** isn't updated for steer 4; it stays only as the steer-3 comparison.

## 9. Open questions
1. **⚑ D+O:** option B (all FX + VOLUME on the lid back row, speaker in the base PLAY row: costs reach and v1.1's "amounts in front") or option A (layout as is; the gap becomes a rose-window band)?
2. **Owner:** spine: none, body colour, or oxblood?
3. **Eng:** side-pivot strength in PETG with brass leaves; screw-through foot part; base speaker vs the Daisy's place; ribbon changes in B.
4. **Visual:** with B chosen, a model so the checker can run labels (§7 of `branch_check.py`).
5. **Owner:** keys A / B / C / D (§10.4). Before A: buy one pack and measure the head height.
6. **Owner:** stays and hinge leaves metal-printed (316L) or printed PETG; brass colour by plating/paint, or a checked brass service.
7. **Owner ⚑ D+O:** hidden pins (cables in the seam) or hollow knuckles (cables through the hinge, bigger barrels, board change)? And the back slot: S0–S3 (§12.2).
8. **Owner:** keys in cast brass (hollow), 316L, or brass-look print; all brass or brass + black (§13). A one-key feel test before ordering 25.

NEXT: product designer (visual focus) — the colours, the woody engraving, the grille pattern and the plate rounding are theirs, and options A/B need their look before the director weighs ⚑ B.
