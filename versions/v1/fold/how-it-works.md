# FOLD: how it works (systems)

Kind: **a hinge** (two parts that close on each other). Pole: designed for use. Body: **self-protecting** (closed it's a clamshell). **Rev 5.1, 2026-11-12 (FOLD round 5).** Read with `../common-how-it-works.md` (rev 6.1) and `../../jobs.md`.

> **Rev 5.7 (2026-11-13): standing angle 105° → 120°.** Owner: "a bit less steep so the front face catches more light". Supersedes rev 5.5's angle and stay numbers; the mechanism is unchanged.
> - **Angle: 120° from the base**, so the panel faces 30° up.
>   - **Light:** the panel catches ≈ 1.9× the overhead light it got at 105° (cos 60° vs cos 75°).
>   - **Legends:** a seated player looks down at ≈ 30–40°, so 120° puts the panel close to square-on to the eye.
>   - **Reach:** the back row moves from y 126 / z 107 to y 147 / z 99, ≈ 79 mm behind the PLAY row: still a short reach.
>   - **Why not 125°:** it adds only 0.3× more light, but moves the back row 6 mm further away and brings more lamp glare on the face.
> - **Stays, re-done** [CALC]: same pivot (d 30, lid back edge).
>   - **Length 44.4 mm** (stows at d 30–74.4); swing 120° to the hard stop; 60° to the table.
>   - **Rubber tip at y 167**, 59 mm behind the base (FOLD-113: 188).
> - **Tipping:**
>   - **Push** (normal to the panel, at a back-row knob tip): **≈ 6.8 N to tip (FOLD-113: 6.0 N), ≥ 5 ✓.** At 120° the push runs more downward, which helps.
>   - **Backward:** the combined centre of gravity (y ≈ 97) sits 70 mm in front of the stay tips, so it can't fall back.
>   - **Forward:** the lid's own centre of gravity is behind the hinge axis, so it rests on the stays.
>   - Weights are still ESTIMATE (base 0.40, lid 0.35–0.40 kg).
> - **Clearance:** V1's knob tips sit ≈ 24 mm above the base's rear rim.

> **Rev 5.6 (pre-build, 2026-11-13). Supersedes the I/O, AFTERTOUCH and digital-placement text below.**
> - **1. I/O vs the stay groove.**
>   - **Moving the jacks to the lid's left end doesn't fix it:** there's a stay in *both* end faces, at the same d 30–82.4, by design. Raising the jacks above the groove doesn't work either: under the lid plate there's only 10.6 mm (z 2–12.6), and the groove takes z ≈ 1–10.
>   - **Fix: split the I/O by where its circuit lives.**
>     - **(a) The audio and CV jacks + power switch move to the lid's far wall** (phones, line out, EXT in, filter CV in, pitch CV out, gate out), x ≈ 60–230, clear of the corner magnets.
>       - Flat, that's the instrument's rear: cables leave away from the keys (F8 ✓). Standing, they leave the top edge and hang behind. Closed, they're on the bar's front face.
>       - The I/O board stands inside the far wall at d ≈ 92–104. The FX row's pot pins must face the hinge, which leaves ≈ 2 mm clear.
>     - **(b) Base right end face, straight off the Daisy Seed: MIDI IN (TRS) at y 70, MIDI OUT (TRS) at y 80, USB-C at y 90–99** (10 mm pitch).
>       - **MIDI IN was missing; it's now added.**
>       - Jack bodies occupy x ≈ 272–286, clear of TAP (261, 68; footprint to x 267).
>       - Low-profile THT jacks on the base board (centre z ≈ 9, under the 13.1 plate underside). USB-C sits on the Seed in its floor cutout (z ≈ 4–7).
>       - All three sit behind the key zone (y ≥ 52) in the 15.6 wall.
>   - **The stays stay symmetric.** Neither end face of the lid carries I/O.
> - **2. AFTERTOUCH re-placed in FOLD** (flat concepts keep the visual designer's spot):
>   - The visual designer's (176.75, d 26) passes on its own. But its mirror slot (109.25, d 26), where the new PARA toggle belongs, lands 2.06 mm from CUTOFF when closed (rule ≥ 3), so the pair can't mirror there.
>   - **So the pair moves outward: PARA (93.9, d 26)**, at the end of OSCILLATORS beside FREQ 2, **and AFTERTOUCH (192.1, d 26)**, at the head of CONTOURS beside F ATTACK.
>   - Mirrored, 3.0 from the breaks, 3.5 from the neighbouring knobs. Closed, they land on the landing strip (plan gaps 3.56 to GLIDE / ECHO REPEATS).
>   - Checker 0 violations for both variants.
>   - **Visual:** move FOLD's AFTERTOUCH and add PARA; legends right-aligned to their toggles (legend check).
> - **3. Daisy Seed: the base**, confirming eng (`daisy-switch-notes.md` §7: "put the Seed and wet path in the base").
>   - **Position:** the base rear strip at x ≈ 200–272, y 80 to D − 4. That's ≥ 30 mm from the ladder (x ≤ 170) and from the Hall sensors (y ≤ 51), as §5 requires.
>   - **USB-C** faces the right end face.
>   - **Height:** under the base plate there's 7 mm above the board, so the Seed sits **in a base-board cutout on the floor**, with 11.1 mm from floor to plate. Seated height is UNVERIFIED (8–8.4 + socket); **the spike must measure it.** If it's > 11, there's no FOLD half that takes it without +mm.
>   - **This moves all digital to the base.** The ribbon list (rev 5.1) must be redone by eng from `daisy-first-principles.md`: pitch/CV DAC outputs cross to the lid; MIDI/USB no longer do.
> - **4. PARA toggle:** as item 2 (FOLD) and common rev 7.3 (flat concepts).

> **Rev 5.5 (2026-11-13): standing lid. Owner: "some sort of method for the top case to stand up … should blend into the case"; "It is not a requirement that you can change the angle".**
> - **One standing angle: the lid opens to 105°, leaning 15° back from vertical.** The lid also keeps flat (180°) and closed.
> - **Why 105° and not 90°:**
>   - At 90° the lid's weight sits right over the hinge axis, so a knock tips it either way.
>   - At 105° its weight leans back onto the stop, so it holds itself up with no detent or friction hinge.
>   - The panel tilts toward a seated eye line.
>   - Reach is fine: the back row sits ≈ 106 mm up (FOLD-113: 127), about 98 mm from the PLAY row.
> - **The tip-over finding [CALC; weights ESTIMATE 0.40 kg base, 0.35–0.40 kg lid]:** a hinge stop alone isn't enough.
>   - Upright, the lid's weight is over the base's rear edge, so a **≈ 1.5–1.8 N push** on a back-row knob would tip the whole instrument backwards.
>   - A stop must carry the push *to the table*, not just lock the hinge.
> - **Mechanism: two brass lid-stays set into the lid's end faces** (writing-box stays, matching the brass back screws).
>   - **Part:** each stay is a 3 × 8 mm brass flat bar, **52.4 mm long**, pivoting on a pin at **d 30 from the hinge edge, at the lid back's edge**.
>   - **Stowed:** it lies flush in a 3.5 mm groove in the end face, running toward the far edge (d 30–82.4). The end wall there is ≥ 8 mm thick locally; the board starts at x 12.
>   - **Deployed:** it swings out 140° to a **hard stop in its pivot boss** and stands at 65° to the table. Its **rubber tip** lands at y 162 (FOLD-113: 183), 54 mm behind the base.
>   - Lid + stay + table form a triangle. A knob push compresses the stays into the table.
>   - **Tip threshold rises to ≈ 5 N.** Turning a knob pushes ≈ 1–3 N.
>   - **Stall-free:** the lid's weight keeps it on the stays.
>   - The hinge stays a plain pin; the knuckles are unchanged.
> - **Flows:**
>   - **Stand:** open past 120°, flip both stays out, lower the lid onto them.
>   - **Flat:** lift the lid, fold the stays into the end faces, lower it flat; it works as before, with nothing proud.
>   - **Closed:** the stays are flush. They show only as brass lines on the ends.
> - **Clearances:** standing, V1's knob tips sit ≈ 15 mm above the base's rear rim, and the PLAY row is 40 mm in front of the axis.
> - **J15/J3:** adds a standing play state.
> - **Eng/maker:** confirm the weights and the pivot boss strength in PETG (or a brass insert); choose the rubber tip.

> **Rev 5.4 / DRIFT (2026-11-13). Supersedes 7.1's PLAY-right and back-row text.** Owner: "I like the idea of drift, but I'd want it to be controllable". DRIFT is a firmware random pitch wander; fully left = rock-steady.
> - **Back row = the chain in one line**, mirrored about the centre:
>   - **DRIFT 79.5** (source, under the FREQ column)
>   - ECHO TYPE 108.5 · ECHO TIME 128.5
>   - REVERB DECAY 157.5 · REVERB TYPE 177.5
>   - **VOLUME 206.5** (out, under the loudness column)
>   - Breaks at 94 / 143 / 192.
> - **PLAY right:** ECHO REPEATS 199 · ECHO MIX 219 · REVERB MIX 239 · **TAP 261**. TAP is played in rhythm, and it mirrors the bend stick.
> - **Why:** one added knob makes the count odd, so a lone DRIFT can't be mirrored. **DRIFT ↔ VOLUME** pairs source with output; TAP moves to the PLAY row to keep that row at 4 + 3 + 4. The checkers pass with 0 violations and mirror 0.00 in every row.
> - **Cost:** VOLUME sits on the back row (≈ 78 mm behind the PLAY row), and TAP is away from TIME. Sizes are unchanged (FOLD-105 108, FOLD-113 129). The back row is the lid's third row, landing over the whites. DRIFT is firmware on the Pico (DAC offsets); its pot needs one lid mux channel. **Eng.**

> **Rev 5.3 (round 5 final, 2026-11-13): full FX. SUPERSEDES 5.2 AND THE DIMENSIONS BELOW WHERE THEY DIFFER**
> - **Base PLAY right:** ECHO REPEATS 199 · ECHO MIX 219 · REVERB MIX 239 · **VOLUME 261 (back on the face; the lid wheel and wall toggle are dropped)**.
> - **Lid FX row = a third lid row 23 behind V2**, landing over the whites when closed (4.0 clear): ECHO TYPE 95.5 · ECHO TIME 115.5 | TAP 143 | REVERB DECAY 170.5 · REVERB TYPE 190.5, own breaks 130 / 156.
> - Checker `fold_r5_check.py`: 0 violations, mirror 0.00 in all rows.
> - **Why a third lid row and not elsewhere:**
>   - the band can't hold controls (the PLAY row parks under it);
>   - the base's landing strip is V1's.
>   - Lid rows can only land between base y 23.45 (far-rim margin) and 54.6, so V2 + FX at 23 pitch is the only fit.
> - **FOLD-105 → halves 286 × 108** (open 216, closed ≈ 50.1):
>   - rows d 14.45 / 60.85 / 83.85;
>   - **PLAY → V1 54.45 ✓**, V1 → V2 46.4, V2 → FX 23;
>   - band under the plate 32.4: cells (x 15–103, 183–271) + speaker centred (x 113–173);
>   - lid board 262 × 102 − 4,750 − 1,800 = 20,174 ≥ 19,500 ✓ (+674).
> - **FOLD-113 → halves 286 × 129** (open 258):
>   - rows d 14.45 / 82.45 / 105.45;
>   - **PLAY → V1 75.45 ✗ (breaks the director's ≤ 60 blocker).** The 52 mm bay forces V2 to 82.45, the FX row adds 23, and the far rim adds 23.45, so D ≥ 129.
>   - **Gap, 22 Wh and full FX can't all hold in FOLD.** Recommend FOLD-105 as *the* FOLD. Show FOLD-113 only so the owner can see why.
> - **FX module:** eng says it "lives with the Pico (base)", but in FOLD the Pico is on the lid board. **Eng to resolve:**
>   - (a) shield in the lid: +1,800 mm², so FOLD-105 → D ≈ 113 (gap 59.45, still ✓);
>   - (b) shield in the base, with I2S crossing (about 5 fast digital lines on the ribbon's digital edge);
>   - (c) Pico + shield both in the base.
>   - **Dimensions above assume the shield in the base, (b)/(c).**
> - **Base mux:** keys + stick + MOD + GLIDE + CUTOFF + TUNE = 30, + REPEATS, ECHO MIX, REVERB MIX = **33 > 32**. So a 3rd CD4067 in the base (≈ $1), or read the 3 on the lid mux via the ribbon spares. **Eng.**
> - **Ribbon:** VOLUME lines return to pins 31–34 as in rev 5.1, plus the FX send/return (eng: 2 guarded analog lines) on pins 17–19.
> - **Key edge:** unchanged (FOLD = option B; A possible).

> **Rev 5.2 (2026-11-13): echo + reverb. Supersedes the FX and VOLUME text below.**
> - **Owner:** "I want echo and reverb", so plan for 4–5 controls.
> - **The PLAY row's right section is now the FX group:** ECHO TIME 199, ECHO REPEATS 219, REVERB 239, FX MIX 261. The slots are unchanged and the mirror still holds (checker relabelled, 0 violations).
> - **VOLUME leaves the face.** It becomes a **thumbwheel in the lid's right wall** beside the phones jack, at d ≈ 10–20 (open y ≈ 120, by the right hand), z ≈ 20–30 open.
>   - VOLUME then never crosses the ribbon.
>   - This is the trade that gives the FX 4 face slots and keeps 4 + 3 + 4. Part UNVERIFIED.
> - **The FX MODE toggle (ECHO / BOTH / REVERB, if the chip needs one)** goes on the lid's right wall with the jacks.
> - **5 knobs:** see the trades in `../common-how-it-works.md` rev 7. FOLD has no rear band, so the third-row option isn't available here.
> - **The echo/reverb circuit goes on the base board, not the lid.**
>   - Eng's `effects.md` assumed the lid, which would add ≈ 6–8 mm of depth. The base has room (≈ 31–36 % fill), and TIME stays local, which answers eng's pin-6 worry.
>   - Proposal: PT2399 + reverb at x ≈ 200–272, y ≥ 80 (≥ 30 mm from the Hall strip and from the ladder at x ≤ 170). The muxes/LDO move to x ≈ 15–60. Eng to confirm the select routing.
> - **Ribbon:**
>   - pin 31 = VCA out → FX (base);
>   - pin 33 = FX out → VOLUME wheel (lid);
>   - pin 34 GND;
>   - pins 17–19 = MODE control lines from the wall toggle.
> - **Key edge:** FOLD already has keys 1.9 above the base plate, behind a 4 mm rim flush with the plate. That reads as option B, a low lip.
>   - Option A for FOLD: keys up 0.6 (to 18.1, 2.5 proud), with a skirted front over a 2.4 wall at z ≈ 11 (as ONE SHEET A).
>   - **Default: B.** It's the base's R3 meeting edge, and it protects the keys when closed.

**Why rev 5 / 5.1:**
- **Owner:**
  - On the battery and depth: "Show me both". So FOLD comes in **two variants**, FOLD-105 (slim battery) and FOLD-113 (big battery).
  - "there's still something off about the controls layout that doesn't feel balanced yet". So **balance is now an explicit design goal**, with its logic stated below.
  - He wants a built-in delay/echo (eng is scoping it, likely 3 controls). So **an FX group has a fixed, balanced home now**, so it doesn't re-break the layout later.
- **Director (round-4 FOLD fixes, `../../scores.md`):**
  - the mid-deck gap is a blocker (≤ ≈ 60 between rows when open);
  - CUTOFF and EMPHASIS side by side;
  - section names black;
  - the signal map only if a strip remains.
- **Eng (`/home/claude/model-d/eng/fold-answers.md`):**
  - the ladder moves to the base: EMPHASIS beside CUTOFF, the lid needs ≈ 2,000 mm² less board, and the mixer bus crosses on the far, guarded edge of the ribbon;
  - **recount:** rev 4.2's lid board was ≈ 20,260 mm², under the 21,500 minimum. Fixed below.

**Settled and kept:**
- the walnut + white Proof look;
- block and pickguard, screws from behind;
- the PLAY (base) / VOICE (lid) split;
- heights, so closed is still ≈ 50.1;
- the I/O on the lid's right wall;
- the magnets.

**What rev 5.1 changes on purpose:** FOLD now has **its own x layout** (no longer the common x + 5), because balance needs it. The common layout still governs HUSH and ONE SHEET.

---

## 1. Balance: the logic, stated

What felt off in rev 4.x, read structurally:
1. **Ragged rows.**
   - The lid rows had holes in different places: V1 was empty at x 119.5 / 178 / 258, and V2 at 23.5 (TUNE had no partner).
   - V1 also ended 33 mm short on the right, while V2 started 20 mm late on the left.
   - So the lid's mass leaned diagonally.
2. **Breaks that didn't line up across the hinge.** The PLAY row broke at 127.5 / 233 and the VOICE at 127.5 / 186, so the sections didn't stack.
3. **CUTOFF 2 mm off centre, in a row whose groups had unequal masses** (6 | 6 | 2 items). The hero knob sat in the middle of nothing in particular.
4. **Uneven gaps:** PLAY → VOICE 119 mm, then rows 23 apart.

**The rules rev 5.1 follows:**
- **B1. Mirror across the width.** Every row is mirror-symmetric about the instrument's centreline, **x 143**: *slot* positions mirror exactly (the checker prints 0.00 mm worst offset for all three rows). *Contents* follow signal flow left to right, so the symmetry is in mass, not meaning.
- **B2. One set of break lines for both halves: x 101.5 and 184.5** (symmetric about 143). Open, each base section sits directly under its lid section, and the sections read as three columns down the whole deck:

  | Column | Left (x 16–101.5) | Centre (101.5–184.5) | Right (184.5–270) |
  |---|---|---|---|
  | Lid (VOICE) | **OSCILLATORS** | **MIXER** (+ the routing switches at its two edges) | **CONTOURS** |
  | Base (PLAY) | **PITCH**: bend, mod, tune, glide | **FILTER**: CUTOFF, EMPHASIS, CONTOUR AMT | **ECHO + OUT**: time, repeats, mix, volume |

  Each column is a stage: source → shape → output. The centre column is the filter, fed by the mixer straight above it (the mixer bus → ladder is also the shortest wire).
- **B3. The hero on the axis.** EMPHASIS sits exactly on x 143, with CUTOFF and CONTOUR AMT at ± 24. The two lights (not-in-control, status) flank EMPHASIS at ± 12, behind the row. **CUTOFF is the big red knob at the left of the filter pair, where the right hand lands first from the stick** (reach 94, was 120).
- **B4. No holes.** Every lid column holds two controls (front and back), so both VOICE rows have **13 slots at identical x**. The base row has 11 knobs + the stick.
- **B5. One rhythm of rows.** Open, the rows step back at **one pitch**:
  - **FOLD-105:** PLAY → V1 → V2 = **52.45 / 52.45**.
  - **FOLD-113:** **60.45 / 68.0**. This is deliberately weighted: the big cells set the second step, and the larger band is where the battery and the grille live.
- **B6. Empty areas fall in bands, full width, each with a job.** No corner voids, nothing lopsided:
  1. the **landing strip** (base, behind the PLAY row): V1 parks there when closed;
  2. the **band** (lid, between V1 and V2): the battery under it, with **the speaker grille centred on x 143**;
  3. the **far strip**: the name, centred.

  Open, the deck reads in alternating layers, controls / band / controls / band, symmetric about the centreline.
- **B7. Mass between the halves.** The base carries the keys (full width, the heaviest mass) plus one full row. The lid carries two full rows. The fold pairs them as interlocking teeth, not as mirror images: mirroring about the seam is impossible by construction, because a lid control at the mirror position of a base control lands right on it when closed. So **the halves balance by rhythm (B5) and by shared columns (B2), not by reflection.**

**What balance cost:**
- **TUNE moves to the base** (PITCH group, beside bend and glide, as in the Model D's controllers).
- **MOD MIX moves to the lid** (centre column, beside the mixer).
- The **four set-before-playing switches leave the base** for the lid's switch slots: OSC MOD, FILTER MOD, KBD CTRL, VEL.

The base row becomes purely **what the hands do during a note**, and the echo controls join it, because throwing the echo is played.

**What balance gained, functionally:**
- reach stick → CUTOFF 94 (was 120);
- osc 3 no longer crosses the ribbon (MOD MIX and OSC MOD are now on the lid with the oscillators), so the worst aggressor is off the hinge;
- the ribbon core shrinks from 37 to 21 signal lines (§4).

**Random draw** (real RNG): "Change instrument roles" + surveying.
- *Roles:* the filler strip behind the PLAY row becomes the landing for V1, and the switches swap halves with the echo.
- *Surveying:* every row is reported as a station with its open position and closed landing (the survey tables). And the centreline x 143 is the datum every row is set out from, which is where B1 came from.

---

## 2. The move that closes the mid-deck gap

- **The geometry.** Closed, a lid control at distance d from the hinge lands at base y = D − d.
  - In rev 4.2 every lid row had to land *in front of* the PLAY row, so the gap was ≈ 2D − 115. Every mm of depth counted twice: 119 mm at D 116.
- **Rev 5: V1 lands *behind* the PLAY row,** on the base's landing strip, the plate the extra depth created.
  - So V1 sits at **d 14.45**: knob edges 7 mm from the seam (the R2 break margin, since the seam *is* the PLAY|VOICE break).
  - The gap becomes D + 14.45 − 68.
- **V2 still lands over the keys.**
- **The base's PLAY knobs land under the band between V1 and V2.** So the band is forced, and its width is set by the battery.

---

## 3. Side by side

| | **FOLD-105 (slim battery)** | **FOLD-113 (big battery)** |
|---|---|---|
| Battery | 4 × PiShop 952540 (9.5 × 25 × 40, 750 mAh, PCM), 1S4P, **11.1 Wh** | 2 × 755060-class (≤ 9.5 × 50 × 60, ≈ 3000 mAh), **22.2 Wh** |
| Runtime at 2.0 / 3.6 W (eng ESTIMATE) | **≈ 4.5 h / 2.4 h** | **≈ 9.0 h / 4.7 h** |
| Charge at 1 A [CALC] | ≈ 3.3 h | ≈ 6.6 h |
| **Each half** | **286 × 106** | **286 × 114** |
| Closed / open | 286 × 106 × ≈ 50.1 / 286 × 212 | 286 × 114 × ≈ 50.1 / 286 × 228 |
| **PLAY → V1 (centres)** | **52.45** ✓ | **60.45** (≈ 60, 0.45 over the literal target) |
| V1 → V2 pitch / clear band | **52.45 / 37.55** (even rhythm) | 68.0 / 53.1 (weighted by the battery) |
| Landing strip (CUTOFF edge → V1 knob edge) | 34.6 | 42.6 |
| Far strip (V2 edge → rim) | 27.65 | 20.1 |
| Key front → back row | 172.9 | 196.45 |
| Lid board [CALC; eng's formula, ladder in base] | 262 × 100 − 4,750 − 1,800 = **19,650 ≥ 19,500 ✓** | 262 × 108 − 6,760 − 1,800 = **19,736 ≥ 19,500 ✓** |
| Battery cost (eng) | $40.75 (+ ≈ $0.50–1.70 fuse/PTCs) | $40.85 |

**Why 106 and 114, not 105 and 113:** eng's formula, D ≥ 6 + (21,300 + A)/262, gives 105.43 and 113.10. Rounded down, the lid board would be short:
- 112 mm² at 105 (19,388);
- 26 mm² at 113 (19,474).

That's the rev 4.2 slip again, so I rounded up. The names stay as the owner heard them. The margins are thin and rest on eng's ≈ 2,000 mm² ladder saving (an ESTIMATE).

For comparison: rev 4.2 had PLAY → VOICE 118.65 and open 234; the flat concepts have PLAY → V1 32.

**Layout check: `../_mock-src/fold_r5_check.py`, 0 violations for both variants.**
- **Same rules as `layout_r4_check.py`:** pitch 20, 24 within CUTOFF/EMPHASIS/CONTOUR AMT, gaps ≥ 1.5, knobs ≥ 7 and toggles ≥ 3 from breaks.
- **Added:**
  - the seam as the horizontal break (≥ 7);
  - base edges ≥ 10, lid rims ≥ 12 (they rise);
  - knuckles ≥ 5;
  - the far rim;
  - **closed landing:** every lid control ≥ 3 in plan from every base control, and ≥ 2.0 above what it lands on;
  - **mirror symmetry**: 0.00 mm worst offset in all rows.

---

## 4. Coordinates (both variants; FOLD x, 286 wide)

### Base PLAY row, y 68: what the hands do during a note
| Section | Items (x) |
|---|---|
| **PITCH** (x 16–101.5) | BEND stick 25 · MOD 47 · **TUNE 67** · GLIDE 87 |
| *break 101.5* | |
| **FILTER** (101.5–184.5) | **CUTOFF 119** (red 1083) · **EMPHASIS 143** (axis) · CONTOUR AMT 167 · lights: not-in-control (131, 81), status (155, 81) |
| *break 184.5* | |
| **FX** (184.5–270) | **ECHO TIME 199 · ECHO REPEATS 219 · REVERB 239 · FX MIX 261** (rev 5.2: VOLUME is now a wheel in the lid's right wall) |

- **Mirror pairs:** 25 ↔ 261, 47 ↔ 239, 67 ↔ 219, 87 ↔ 199, 119 ↔ 167, 131 ↔ 155.
- **Pitches:**
  - 22 between the stick and MOD, mirrored by MIX → VOLUME;
  - 20 elsewhere;
  - 24 in the filter trio;
  - 32 across each break (knob edges 7 from the break).

**The FX group:**
- **Three slots now.** Until eng confirms, a printed plate legend can mark them as reserved, or they can be fitted blank.
- **If eng lands on 2 controls**, VOLUME moves to 239 and the 261 slot is left blank. Never reflow the row.
- **If eng wants a 4th** (for example a delay/echo character switch), there's no free legal slot: every row is full and symmetric. The cleanest trade would be to fold the echo's MIX into a push-pull on VOLUME, or to drop the VEL toggle to a menu. That's an owner/eng decision, stated now so it doesn't surprise anyone later.
- Signal flow is VCA → echo → VOLUME, so the knob order follows it.

### Lid VOICE: two rows, 13 slots each, identical x
| x | 23.5 | 43.5 | 63.5 | 83.5 | *101.5* | 109.25 (t) | 123 | **143** | 163 | 176.75 (t) | *184.5* | 202.5 | 222.5 | 242.5 | 262.5 (t) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **V1 (front)** | RANGE 1 | RANGE 2 | RANGE 3 | FREQ 2 | | OSC MOD | OSC 1 | OSC 3 | MOD MIX | FILTER MOD | | F ATTACK | F DECAY | F SUSTAIN | KBD CTRL |
| **V2 (back)** | WAVE 1 | WAVE 2 | WAVE 3 | FREQ 3 | | OSC 3 CTL | OSC 2 | NOISE/EXT | SOURCE (t) | VEL | | L ATTACK | L DECAY | L SUSTAIN | DECAY |

**Section logic:**
- **OSCILLATORS:** one column per VCO (RANGE over WAVE), then FREQ 2 / FREQ 3.
- **MIXER:** 4 levels around the axis, plus MOD MIX (it mixes the modulation sources) next to SOURCE (which picks the noise/ext source).
  - **Switches sit on the edge of the section they act on.** OSC MOD and OSC 3 CTL are on the oscillator side, at 109.25. FILTER MOD and VEL are on the contours/filter side, at 176.75.
- **CONTOURS:**
  - front row = **how the filter follows the note**: F A, F D, F S + KBD CTRL (keyboard tracking);
  - back row = **how loudness follows the note**: L A, L D, L S + DECAY (release).
- **Toggle slots** are minimum-legal: 1.7 mm to the neighbouring knob, 3.15 to the break.

**Mass, stated:** the lid's right end is a toggle column, while its left end is a knob column (RANGE 1 / WAVE 1), so the right is lighter. **Deliberately weighted:** directly in front of it is the base's VOLUME, the heaviest knob in the echo group, and the FOLD-105 grille is now centred, so nothing else pulls right.

---

## 5. FOLD-105 (slim battery)

**Halves:**
- **Base** 286 × 106 × 15.6;
- **lid** 286 × 106 × 34.5.

**Closed** 286 × 106 × ≈ 50.1. **Open** 286 × 212.

**Base, y from the front edge:**
| y | Zone |
|---|---|
| 0–4 | front rim, flush, R 3 |
| 4.5–34.5 / 36.5–50.5 | whites (17.5) / sharps (19.5) |
| 52–102 | base plate, face 15.6 |
| **68** | **PLAY row** |
| 78.4–102 | **landing strip**: flush. Closed, V1 parks at y 84.1–99.0 |
| 102–106 | rear rim, flush |

**Lid, d from the hinge edge (open y = 106 + d):**
| d | Zone |
|---|---|
| 0–7 | seam margin (no wall: R4) |
| **14.45** | **V1** (open y 120.45) |
| 21.9–59.45 | **band**, 37.55 clear. Closed, the PLAY row sits under it (CUTOFF spans d 27.6–48.4). Cells and speaker are under it; the **grille is centred on x 143** |
| **66.9** | **V2** (open y 172.9) |
| 74.35–102 | far strip, 27.65: **name inlay centred on x 143** |
| 102–106 | far rim (V2 edge → rim inner face 27.65 ≥ 12 ✓) |

**Closed survey:**
| Row | Open y | Lands at base y | Over | z clearance | Plan gap |
|---|---|---|---|---|---|
| V1 | 120.45 | 91.55 (84.1–99.0) | landing strip | **5.9** | 5.7 to CUTOFF's rear edge |
| V2 | 172.9 | 39.1 (31.65–46.55) | sharps (and whites) | **2.0** | 11.05 to CUTOFF's front edge |
| PLAY | 68 | under band d 38 | lid plate 35 | **5.9** (CUTOFF 7.25) | — |

- **Stick:** under the band, as before (cap ≤ 17.4 above the plate; check the #2765 in hand).
- **TUNE:** now in the base, so the old TUNE/stick clash is gone for good.

**Battery bay, speaker, board: laid out symmetrically**
- Under the band (it has 38.45 under the plate, d 22.45–60.9):
  - **cells in two pairs:** x 15–103 and 183–271, d 28.2–55.2 (each pair 88 × 27);
  - **speaker** (PUI ASE06008MR-LW150-R, 60 × 30 × 10.3) **centred**: x 113–173, d 26.7–56.7, open centre (143, 147.7).
- **Pot footprints** (ESTIMATE; eng to confirm from the A-5622 drawing): 8 mm on the pin side, 6 on the other.
  - V1 pins face the band (they reach d 22.45);
  - V2 pins face the far rim.
- **Lid board:** one piece with **three windows** (cells / speaker / cells). The strip under V1 joins the rest through two **10 mm bridges** (x 103–113 and 173–183), which carry V1's 13 controls.
  - **Eng check:** ≈ 40 traces per bridge over 2 layers.
  - Fallback: a separate V1 strip board on a short jumper.
- **Height:** cells 9.5 in 10.6, so 1.1 swell. Measure one first; if it's > 9.6, use 3 × USE-803048-class (eng §1.4.6).
- **Holding and wiring:**
  - printed cradles screwed to the lid floor (2 × M2.5 each), with foam pads (no compression);
  - a star harness, then a 2 A fuse, then **one JST-PH** to the bq25185 by the right-wall I/O board;
  - XH → PH adapter; optional ≈ 1 A PTC per cell.
- **Access:**
  1. Undo the 6 screws on the lid's back.
  2. Push the pickguard out.
  3. Lift it ≈ 20 mm and unplug the PH plug.
  4. Lift the pickguard out. The cells are in their cradles.
- **No hatch:** the block stays unibody.
- The speaker is far from the ladder (which is in the base), so the ≥ 55 mm rule is met.

---

## 6. FOLD-113 (big battery)

**Halves:**
- **Base** 286 × 114 × 15.6;
- **lid** 286 × 114 × 34.5.

**Closed** 286 × 114 × ≈ 50.1. **Open** 286 × 228.

**Base:** as FOLD-105 up to the PLAY row, then the plate runs 52–110, the **landing strip** 78.4–110 (V1 parks at y 92.1–107.0), and the rear rim 110–114.

**Lid (open y = 114 + d):**
| d | Zone |
|---|---|
| 0–7 | seam margin |
| **14.45** | **V1** (open y 128.45) |
| 21.9–75.0 | **band**, 53.1 clear. Closed, the PLAY row sits under it (CUTOFF spans d 35.6–56.4). Cells and speaker are under it; the grille is centred on x 143 |
| **82.45** | **V2** (open y 196.45) |
| 89.9–110 | far strip, 20.1: name, centred |
| 110–114 | far rim (20.1 ≥ 12 ✓) |

**Why V2 sits at d 82.45 (not 66.85, the knob-rule minimum):**
- Each 50 mm-wide cell needs a 52 mm-deep window clear of pot footprints, d 23.45–75.45. That pushes V2's footprint to 76.45, so V2 sits at 82.45.
- There's no other home:
  - the far strip has ≈ 20 under the plate;
  - the base's rear strip is ≤ 35 deep;
  - under the keys there's 2.5 mm.
- **So the big pack costs 8 mm of depth *and* a weighted rhythm (60.45 / 68) with a 53 mm band.**

**Closed survey:**
| Row | Open y | Lands at base y | Over | z clearance | Plan gap |
|---|---|---|---|---|---|
| V1 | 128.45 | 99.55 (92.1–107.0) | landing strip | **5.9** | 13.7 to CUTOFF's rear edge |
| V2 | 196.45 | 31.55 (24.1–39.0) | whites, sharp fronts | **4.0 / 2.0** | 18.6 |
| PLAY | 68 | under band d 46 | lid plate 35 | **5.9** | — |

**Bay, speaker, board (symmetric):**
- **cells** one each side: x 15–80 and 206–271, d 23.45–75.45 (each 65 × 52; together eng's 130 × 52);
- **speaker centred:** x 113–173, d 34.45–64.45, open centre (143, 163.45);
- **lid board:** one piece, with windows for cell / speaker / cell and **33 mm bridges** at x 80–113 and 173–206 (comfortable).

Holding, harness and access are as FOLD-105.

---

## 7. Shared by both variants

### What sits where in the base (eng to confirm placement)
- **Ladder filter:** on the base board, behind the FILTER section, x ≈ 95–170, y 75 to D − 11.
  - CUTOFF, EMPHASIS and CONTOUR AMT are all local.
  - No wire of the emphasis loop crosses the hinge.
- **The rest of the board:**
  - **2 × CD4067 + LD1117** at x ≈ 230–272, next to the ribbon's digital edge, ≥ 30 mm from the ladder;
  - **ribbon header** at x 176–227, y D − 9.5 to D − 3.5.
- **Base board** 270 × (D − 8), so 270 × 98 / 270 × 106. Behind the keys it has ≈ 13,800 / 15,900 mm², so the ladder's tight 66–70 % fill becomes **≈ 36 % / 31 %** [CALC].
- **Room for the echo circuit too.** Keep any clocked delay chip (PT2399-class) ≥ 30 mm from the ladder and its expo pair.
- **Base mux channels:** the keys, stick, MOD, GLIDE and CUTOFF stay; VEL leaves; TUNE joins if it's read digitally. That's 30 of 32.
  - **The FX pots can't also be muxed** (that would make 33). Either they're analog pots on the echo chip, or a third mux is needed. **Eng.**
- **Heights (eng):**
  - 7 mm under the base plate;
  - electrolytics lie flat;
  - film caps ≤ 6.5 mm;
  - nothing on the underside.

### Hinge ribbon: 40-way, 1.27 mm (50.8 wide), ≈ 80 mm rolling loop under the TPU flap, crossing at x 176–227
Moving MOD MIX, OSC MOD, FILTER MOD and KBD CTRL to the lid, next to their sources, **takes osc 3 off the ribbon** and leaves **21 signal lines**.
- **Headers:**
  - base: on the landing strip's underside;
  - lid: along the hinge edge **in front of V1's pots**, d 2.5–8.5. V1's pot bodies start at 9.7, so the gap is 1.2 mm (tight).
- **The IDC must be low-profile** (7 mm under the plate). If it isn't, use an IDC without strain relief, or 2 × 20-way. **Eng.**

| Pins | Lines |
|---|---|
| 1–4 | +5 V, +5 V, GND, GND (sensor LDO in the base) |
| 5–8 | mux selects S0–S3 |
| 9 | GND |
| 10–11 | MUX A, MUX B out |
| 12 | GND |
| 13–14 | LEDs: status, not-in-control |
| 15–16 | GND, GND |
| 17–19 | **reserved for FX** (TIME / REPEATS / MIX wipers), used only if eng puts the echo circuit on the lid board |
| 20 | GND |
| 21 | spare |
| 22 | keytrack CV (already switched by KBD CTRL in the lid) |
| 23 | CUTOFF + velocity CV (DAC → ladder summer) |
| 24 | filter contour CV (→ CONTOUR AMT) |
| 25 | filter mod CV (already switched by FILTER MOD in the lid) |
| 26 | TUNE wiper (if TUNE is analog; else GND) |
| 27 | AGND |
| 28–29 | +9 V, −9 V (ladder bias ≈ 5–10 mA) |
| 30 | AGND |
| 31 | VCA out → echo → VOLUME |
| 32 | GND |
| 33 | VOLUME wiper → output stage |
| 34 | GND (VOLUME's ground leg) |
| 35 | filter out → VCA (≈ 1 V, ≈ 1 k) |
| 36–38 | GND × 3 |
| **39** | **mixer bus → ladder input**: the sensitive line (eng's `emi` rules). 31 conductors from S3, ground on both sides |
| 40 | GND |

- **Eng to confirm:**
  - this order;
  - whether TUNE is analog;
  - the bench test on pin 39 (pass ≤ −70 dB, `fold-answers.md` §2.6).
- **A 34-way would carry the core.** The 40-way keeps the FX reserve and the guard spacing.

### Hinge
- Knuckles at the rear corners, **narrowed to x 0–10 and 276–286** (were 0–14).
  - V1 now sits at the hinge edge: RANGE 1's edge (16.05) gets 6.05 (≥ 5).
  - On the right, KBD CTRL's edge (267.1) gets 8.9.
- M4 shoulder bolt, axis at z ≈ 25: the lid lies flat at 180°.
- **Lugs:** ≈ 4.5–5 mm each in 10 mm. **Maker check** in PETG; a brass sleeve is the fallback.
- **Swing [CALC]:** V1's nearest point is ≈ 8 mm from the axis and swings over the top. It only comes down at landing (z 21.4, over the landing strip). The base controls are ≥ 27 mm from the axis.
- **Latch:** two 6 mm magnets in the lid's far corners over washers in the base's front corners.

### Heights (unchanged)
| Part | z |
|---|---|
| Base block | 15.6 (floor 2; board top 6.1; pot bodies 7; plate 2.5) |
| Whites / sharps | 17.5 / 19.5 |
| Base knob tops / CUTOFF | 29.1 / 27.75 |
| Lid block | 34.5 (hollow 19.4 + plate 2.5 + pots 7 + board 1.6 + tails 2 + back 2) |
| Under the lid plate | 10.6 (cells 9.5, speaker 10.3) |
| **Closed** | **≈ 50.1** (lean ≈ 49.2) |
| Open: lid plate / lid rims | 15.1 (flush seam, 0.5 below the base plate) / 34.5 (19.4 above, ≥ 12 from every knob edge) |

### Closed from the back
- There's still **no wall on the lid's hinge edge** (R4), so closed there's a **19.4 mm slot** between the knuckles (x 10–276).
- **New:** V1's controls sit **7 mm inside it** (were ≈ 18). That's the price of the gap fix. Stated for J6.

### Unchanged from rev 4 (in force)
- **Idea:** two halves that protect each other. Each half is a hollowed walnut block with a white pickguard dropped in. Keys and what you play in one half, the voice in the other. It folds like a book laid open flat.
- **Principles:**
  1. Open flat, never raised.
  2. **Each half guards the other.** Closed, V1 parks behind the PLAY row, V2 sits over the keys, and the PLAY row sits under the band.
  3. Block and pickguard.
  4. **The fold line is the logic line.** The base holds what the hands do during a note (now including the filter circuit and the echo); the lid holds the voice and the switches you set beforehand.
  5. One cable crosses, and the hinges sit at the ends.
  6. **New: one centreline, three columns** (B1–B2): the deck is set out from x 143, with the same breaks on both halves.
- **Build:**
  - Blocks are printed trays: plan corners R 12, outer edges R 6, meeting edges R 3, with a 2 mm plate ledge.
  - Plates are 2.5 mm white, printed face down, legends by one swap.
  - **6 × M3 from behind** into standoffs, plus 2 push-out holes. No fastener on the white face.
  - The I/O board is inside the lid's right wall.
  - Key tops and knobs go on last.
- **Assembly (F9):**
  1. Print.
  2. Press in the inserts.
  3. Screw the boards to the plates.
  4. Lid only: fit the cradles, cells and speaker.
  5. Lay each plate assembly in its block.
  6. Plug the ribbon, the I/O cable and the battery plug.
  7. 6 screws from behind.
  8. Fit the key tops and knobs.
  9. Pin the hinges.
- **Service (F10):** 6 screws, push out, lift. The battery is as above. A key: pull its top.
- **Print:**

  | | FOLD-105 | FOLD-113 | One piece needs | Fallback |
  |---|---|---|---|---|
  | Blocks | 286 × 106 × 15.6 / 34.5 | 286 × 114 × 15.6 / 34.5 | Voron 350 / Gigabot (UNVERIFIED) | lap joint at x 101.5 or 184.5 (now on the break lines) |
  | Plates | ≈ 278 × 98 | ≈ 278 × 106 | ≥ 285 | split at x 143? **No:** that cuts through EMPHASIS/OSC 3/NOISE. Split at **x 184.5** (pieces ≤ 180.5 wide: needs a ≥ 185 bed, so Prusa MK4 ✓) |

  Filament ≈ $8–10 / $9–11 (ESTIMATE).
- **States:**
  - carry: closed walnut bar;
  - play: open flat, reading keys → PLAY → landing strip → seam → V1 → band (grille) → V2 → far strip (name);
  - lap;
  - shelf on its left end;
  - service.
- **Flows:**
  - F1: open → lid flat → power (right wall) → play.
  - F5: power off → fold → magnets.
  - F8: cables on the lid's right wall.
  - F11: hand marks on the centred name inlay.
- **R4:**
  - keys 1.9 above the plate; rims flush;
  - flush seam, no hinge-edge wall;
  - lid rims on the sides and far edge only, ≥ 12 from knobs;
  - knuckles only at the corners.
- **Cost (ESTIMATE):** enclosure, hardware, 40-way ribbon and speaker ≈ $21–26, plus the battery ($40.75 / $40.85). The echo circuit is eng's to cost.

---

## 8. For the visual designer (structure → look; your calls flagged)
1. **Draw to the coordinates in §4–6.** It's a new x layout: mirror about x 143, breaks at 101.5 / 184.5 on both halves.
2. **Make the three columns legible across the hinge** (B2): the same break lines on both plates, and section names black, one swap. The column reading (PITCH under OSCILLATORS, FILTER under MIXER, ECHO + OUT under CONTOURS) is the balance; let the type show it.
3. **The band** (lid, between V1 and V2): the grille is centred on x 143. The rest is cream over the cells.
   - **This is the strip the signal map could use** (a strip remains, and it has a job). Or use column ticks tying RANGE to WAVE across the band in FOLD-113, where the rows are 68 apart. Your call.
4. **The landing strip** (base): flush. A fine parking line for V1 is optional.
5. **The FX slots** (199 / 219 / 239): until eng confirms, draw them as real knobs labelled time / repeats / mix.
6. Name inlay centred in the far strip. Knuckles are 10 wide. EMPHASIS is a plain black knob on the axis; the two lights flank it.

## 9. Open questions
- **Eng:**
  - the echo circuit: which part, base or lid board, analog pots or muxed (a 3rd mux)?
  - TUNE analog or digital;
  - the 40-way order;
  - the lid IDC (1.2 mm in front of V1, height under 7 mm);
  - the pot footprint (8 / 6 ESTIMATE);
  - FOLD-105's 10 mm board bridges;
  - the base placement;
  - the lid-board margins (+150 / +236 mm²);
  - the pin 39 bench test.
- **Maker:**
  - the 10 mm knuckle lugs;
  - measure one 952540 (≤ 9.6);
  - Vector Space bed sizes.
- **Owner (via the orchestrator):**
  - FOLD-105 vs FOLD-113: ≈ 4.5 h / 2.4 h with an even rhythm, against ≈ 9 h / 4.7 h with +8 mm and a weighted rhythm (53 mm band);
  - he hasn't seen TUNE in the base or the switches moved to the lid; that follows from his "balanced" note;
  - V1 now shows 7 mm inside the closed back slot;
  - a 4th echo control would need a trade (§4: a push-pull on VOLUME, or VEL to a menu).
- **Cross-concept:** HUSH and ONE SHEET will also need an FX home. They still use the common layout, so that's a separate pass.
- **Coverage:** `coverage.md` is round 4. Re-walk it when rev 5.1 scores 9+. Expected changes:
  - J3 ✓ (EMPHASIS beside CUTOFF, reach 94);
  - J7 ✓ (internal battery);
  - J6 ◐ (back slot);
  - J16: likely stronger (one row in the base; 3 aligned columns);
  - a **new job** for the owner's echo request, to add to `jobs.md` once eng scopes it.
