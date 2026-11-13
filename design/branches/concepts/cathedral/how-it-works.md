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
