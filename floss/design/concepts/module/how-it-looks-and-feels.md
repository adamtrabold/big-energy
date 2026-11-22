# floss module: how it looks and feels (shared by FALLBOARD, SPINE and CLOTH)

Status: **rev 1, 2026-11-22**, product designer (visual focus), concept round 2. Read with `how-it-works.md` (systems) and `floss/eng/module-r2.md`. One module goes into every kit unchanged; each kit's own file covers only the carry.

**Picture:** `module-1to1-A3.png` (and `.pdf`). It shows the plan, the front, the rear and a section on the axis at **1 : 1 on A3**; print at 100 % and the 50 mm bar measures 50 mm. Source: `../_src/r2.py` (`python3 r2.py module`).

Marks: **[r2]** `module-r2.md` · **[calc]** my arithmetic · **PROPOSAL** not approved · **UNVERIFIED**.

---

## 1. Size and proportion: 280 × 105 × 35, one 35 mm unit, 8 : 3 : 1 (my call; systems follows it)
The owner, 13:29 and after: "a thoughtful ratio base", "it also does not have to be a rectangle", and then "don't anchor on the page size thing … It just needs to be portable and make sense and be harmonious" (PRINCIPLES §2).

**So the sizes come from the parts, and the ratio tunes them. Paper is out.**

| Need | From | Gives |
|---|---|---|
| The panel's width | systems' map: two 34 mm jambs + seven 22 mm columns + six 7 mm group gaps = 264 mm | ≥ 264 + an end margin |
| End margin | the jamb's tabs need only clear the rim (4) and a fingertip (4) | 8 mm each end → **280** |
| Depth at the centre | the speaker crown: driver Ø 55 behind the rear row [r2] | **105** |
| Depth at the ends | jambs only: front row + tabs to y 47.5 + rim | ≥ 56 → **70** |
| Height | the driver needs a 32 mm body [r2]; the knobs sit inside the rim | 32 + 3 margin → **35** |

**The ratio: one 35 mm unit, with proportions from string lengths.** floss is a string machine, so its body is proportioned the way strings are tuned (Pythagoras' intervals, which Renaissance builders also used for rooms and instruments):
- length : depth : height = **8 : 3 : 1** (280 : 105 : 35);
- **each half of the panel (140 × 105) is 4 : 3, a fourth.** The two halves are the keyboard's two halves, and the axis between them is the split;
- the whole plan, 8 : 3, is an octave plus a fourth;
- centre depth : end depth = 105 : 70 = **3 : 2, a fifth**;
- length : height = 8 : 1, three octaves.

It's harmonious in the owner's sense (PRINCIPLES §2: grids and scales derive from the device's own dimensions). Every edge is a whole number of units, and the 35 mm grid printed on the 1:1 sheet is the module's own.

**Why 297 × 105 (2√2 : 1) loses:**
- It was derived from the owner's paper example, which he has since withdrawn.
- Its extra 17 mm of length carried no part: the end margins grew from 8 to 16.5 mm to reach A4. With the speaker on the axis, 280 holds every part, so 297 is 6 % longer for nothing.
- 105 survives because the speaker sets it, not the paper.

**What changes in systems' `how-it-works.md`:**
- every x in the panel map moves **−8.5** (axis 148.5 → 140; frets 45.5 · 74.5 · 125.5 · 154.5 · 205.5 · 234.5; inserts 60 and 220);
- the module is 280 wide;
- in FALLBOARD and SPINE the pockets either side grow from 53.5 to **≈ 59 × 105**;
- closed thicknesses follow §3.

## 2. Outline: a hull in plan (draw: "a ship hull in plan" + "Go slowly all the way round the outside")
I walked the perimeter and gave each edge a job:
- **Front edge: straight, full length.** It faces the keyboard. It carries the brass target rail on its rim, the host port and port light low on its face, and the engraved line. Straight because the rail and the keyboard are straight.
- **Front corners: r 10.** Small, so the rail runs nearly corner to corner.
- **Ends: straight, 70 deep.** The jambs' shoulders; you pick the module up by them.
- **Rear: one fair arc**, from 70 at each end to 105 on the axis, over the speaker (R ≈ 297.5 [calc]). It's the hull's waterline: deep where the weight and the sound are, fine toward the ends.
- **Two flat port facets** sit on the arc, either side of the crown, so the jacks get a flat panel (and match the kit's windows):
  - plan-left: **power · USB-C · tune · split** (set once);
  - plan-right: **phones · line · MIDI in · MIDI out** (sound and MIDI).

It's not a slab, and nothing about it is decoration. The plan is symmetric about the axis, which keeps the owner's rule against off-centre in the middle (PRINCIPLES §6).

## 3. Section and height: a sunk deck, a rim, a speaker crown (PROPOSAL: 35, not 40)
[r2] gives a 32 mm body for the speaker and "≈ 40 with knobs". But only the speaker needs 32. [r2] itself allows "a local bulge … a form decision".
- **Deck at 26 mm** over eng's own flat stack (floor 2.4 + cells 7.5 + parts 3 + board 1.6 + top parts 6.5 + deck 2.5 ≈ 23.5 [eng]), with **the two cells beside the crown**, under the deck. Eng to confirm the stack and the U-shaped board.
- **Knob tops at 34**, under a **rim at 35** all round. The knobs never stand proud, which protects them in every kit (the rim takes the lid, the keyboard tray's foam, or the cloth).
- **The speaker crown** is a raised island on the axis, **70 wide (2 units)**, its top level with the rim at 35.
  - Its front face is **raked** (from the deck at y 47 to the top at y 55), like a cabin front. That gives the fingers room behind DRIFT, SHIMMER and TIME.
  - The driver fires up through a grille on the crown's top: Ø 1.8 holes at 2.6 pitch in a Ø 43 field, 221 holes ≈ 560 mm² open [calc]. That's under [r2]'s ≥ 620, so the field should widen to Ø 46 (≈ 245 holes ≈ 620 mm²) or the holes to Ø 1.9 in the concept that goes forward.
  - The sealed box inside is ≈ 60 × 55 × 27 ≈ 76 cm³ net (≥ 60 [r2]). **The driver's exact position under the rake is eng's** (its Ø 55 frame is about the crown's flat depth).
- **The cost of 35 vs 40 in the kits [calc]:** FALLBOARD closes at **43** (48), SPINE at **56** (61), CLOTH's bundle ≈ 5 mm thinner.

## 4. The panel (systems' map, drawn at 1:1)
- **Two rows.** Front row = amounts, Ø 14.9 black knobs. Rear row = kinds and set-then-left: PRESSURE and SHIMMER mode are **Ø 10**, so the hand meets the amounts first. RELEASE, DRIFT, TIME and REVERB keep Ø 14.9, because they're amounts.
- **Seven groups, mirrored about the axis:** jamb · touch · voice · **shimmer (axis)** · echo · out · jamb.
  - **Brass frets** at the group gaps, from the front rim to the crown's foot.
  - **Owner caution (PRINCIPLES §6: section separation mustn't get in the way of hands):** each fret sits in a 7 mm gap between knob edges, below the knob tops. Drawn raised 1 mm; **a flush inlay you feel by its edge is the fallback** if a raised fret catches a finger. Director to rule.
- **The jambs (draw, jam: "Change instrument roles" + organ stops):** each end holds its half's octave knob, stepped with detent ticks only, plus three **stop tabs**, low · main · high, side by side behind it. The ends play the role of an organ's stop jambs: each end owns its half, and the face has two shoulders with a quiet line between.
- **The axis:** DEPTH in **coral** (the one accent: shimmer is what floss is for). SHIMMER mode sits behind it. The crown and the **wordmark "floss"** are centred above them, where a piano puts its nameboard.
- **Words:** one plain word above each control (family rule). DRIFT, SHIMMER and TIME sit on the crown's rake. The tabs carry their words on their faces.
- **Marking:** the family's tick ring at r + 1.7 on the stepped knobs (detents only); pots carry a single white pointer line. No other print on the deck.

## 5. Colour and material
| Part | Finish | Why |
|---|---|---|
| Shell | walnut-brown PETG, matte (printed, as eng's weights assume [r2]) | the family's walnut, in the material eng costed. Real walnut is an upgrade, not the baseline (the owner doesn't machine) |
| Deck | cream panel (as CATHEDRAL's cream plates) | the family face |
| Crown | a lighter cream than the deck; grille holes in it | the speaker reads as its own body |
| Frets, target rail, target, HOLD | brass | brass marks what you touch to *set* or *play by hand* |
| Knobs | black; one coral (DEPTH) | one accent, on the axis |
| Stop tabs | warm white, words engraved | organ-tab language, plain words |
| Lights | TAP's green ring (status); a warm amber port light on the front | two lights, two places (director ruling 4) |

## 6. Front face, rear wall, underside
- **Front face** (towards the keyboard):
  - the brass rail on the rim, graduated every 10 mm with a longer centre mark;
  - the **brass target** rides it, with a pointer down the face;
  - **"keep the keyboard | at its home octave"** engraved either side of the axis;
  - the **USB-C host port** low on the axis, the **port light** beside it.
  - **Why floss can't know which key is which**, the one line for the owner: a USB keyboard sends only note numbers, and its octave button changes them without telling floss. So floss splits at a fixed number, and the target shows where that number sits on today's keyboard.
- **Rear:** the two flat facets (§2).
  - **Power** is a recessed slide, so it can't switch on in a bag.
  - **The two USB-C sockets are a whole body apart:** host on the front face, charging on the rear facet ([r2] asks to separate and mark them).
- **Underside:** two ¼"-20 brass inserts (S4) at x 60 and 220, y 30, under the control band, clear of the crown; four feet. They're drawn dashed on the plan.

## 7. Feel, motion and feedback (every module state)
It's a physical instrument: the "motion" is in the hand and in the two lights.

| State | What you see or feel |
|---|---|
| Off | all dark; the knobs still turn (no detents but the stepped ones) |
| Switching on | the slide clicks into its recess; TAP's ring comes up **steady green** |
| Keyboard plugged in | the **amber port light** comes on steady |
| Playing | the port light **winks once per note**: a heartbeat for notes arriving |
| "Why is it silent?" (job 29) | port steady but no wink on a key = notes not arriving. Winks but silent = look at VOLUME, then the tabs (a half with all three tabs down is visibly off) |
| Keyboard fault | the port light **flashes fast** |
| HOLD on | the brass HOLD stays **down** (latching), level with the deck: you can feel it from the side |
| A planted drone, keyboard gone | HOLD down, port light off, the sound goes on; every knob still works |
| Octaves split | the two octave pointers **aren't parallel**: the split, and HOLD's scope, read from the two ends at a glance |
| Charging | TAP's ring **pulses slowly** |
| Low battery | TAP's ring **flashes** |
| SYNC tempo | TAP's ring blinks the tempo (status shows between blinks; director may move status to a dot under the wordmark if that's too much) |
| Shimmer | DEPTH, coral, under your right hand's reach at the centre. No light: you hear it |

- **Hand feel:** stepped octave and selector knobs click; pots are smooth. Tabs rock with a firm detent. HOLD is a push-push latch you can operate blind. TAP is a momentary.
- **Counting by touch:** octave knob, tabs, fret, HOLD, fret, four voice knobs, fret, the centre. The right side mirrors it.

## 8. How it looks when the keyboard is someone else's (all kits)
- The module never imitates the keyboard: walnut, cream and brass sit beside any plastic.
- In the rigid kits the tray **owns the outline** and hosts the keys on a dark bed. In CLOTH the stitched outline does.
- The module's straight front edge always faces the guest, so the two read as one instrument with the split shown on floss's own rail.

## 9. Why (for the handoff's Why part)
- **8 : 3 : 1 in 35 mm units:** the parts give 280 / 105 / ≈ 32. The string-length ratios make those sizes one family of proportions, and a string machine is proportioned like strings. 297 came from paper; 280 comes from the panel.
- **The hull outline:** the owner invited a non-rectangle, and only the speaker needs depth. The arc puts depth where it's needed and gives the ends a pick-up shoulder.
- **The sunk deck and crown:** it saves 5 mm of the kits' thickness by building only what the speaker needs, and protects the knobs in every carry.
- **Stop jambs:** each half owns its end (director ruling); the organ gives the form a reason.

## 10. Open questions
1. **Eng:**
   - the flat stack at deck 26 with the cells beside the crown;
   - the U-shaped board in a 280 hull;
   - the driver under the raked crown;
   - grille open area (drawn ≈ 560; widen to ≥ 620);
   - insert bosses at x 60 / 220;
   - weight (expected about eng's BLOCK figure, 0.67–0.93 kg; not recalculated).
2. **Director:**
   - 8 : 3 : 1 and the hull;
   - raised vs flush frets (§4, PRINCIPLES §6);
   - TAP's ring carrying status plus tempo.
3. **Owner (with the concepts):**
   - the proportion story in one line: "a string machine proportioned like strings: 8 : 3 : 1, a fourth for each half";
   - the 35 mm height.
4. **Parts:**
   - a bought coral knob, Ø 14.9 (still unchecked);
   - stop-tab rockers with engraved faces (UNVERIFIED);
   - brass fret stock (UNVERIFIED).
