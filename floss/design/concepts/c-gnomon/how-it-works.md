# GNOMON: how it works (systems, idea level) — rev 5

2026-11-22. PROPOSAL (the director's idea, turn 3). Scores: 8 (rev 1), 9 (rev 2). **Rev 4** folds in the owner's change to rev 3, verbatim: **"I don’t like the angle on the back when laying flat. Make the base and the back 90 degrees when sitting flat"**. Rev 3 had folded in "Reverse the angle on the side behind the speakers so there’s still a subtle angle when upright". Rev 2 folded in his 18:39 / 18:40 pose words and director fix 6.

Sizes are [calc] from `eng/module-r3.md` facts. Mass ≈ 0.8 kg and the centre of mass (COM) are ESTIMATES. Nothing is measured.

## The idea
CATHEDRAL's lid standing on its own ends. A framed slab of constant thickness, the slab eng already proved holds everything. At each end the rim carries on down into a **cheek** whose end face has **two feet**:
- the runners give the angled pose;
- the rear face, behind the speakers, gives the upright pose, leaning back by the same angle as the playing pose.

That's his first two choices, both by shape, with no parts.

## His change, read plainly
- "Laying flat" / "sitting flat" means the pose on the base and runners, his playing pose.
- **In that pose, the back is now vertical: square to the table.** The corner behind the speakers becomes **90° − θ ≈ 71.6°**.
- So stood on the back, **the plate leans back by θ itself**, ≈ 18.4°.
- Rev 3's lean (tan φ = T / 2D ≈ 9.5°) is gone, and so is its rule. **One angle now serves both poses.**

## Structure, from the end face
- **Slab:** T = 35, D = 105–115 [eng]. As r3.
- **Cheek outline:**
  - front face T, square to the plate;
  - plate D;
  - **rear face vertical in the playing pose**, at (90° − θ) to the plate;
  - the runner line closes it.
- **The angle rule is unchanged: tan θ = T / D → θ ≈ 18.4° (D 105) / 16.9° (D 115).** The change forces nothing on it.
- **The upright lean is θ**, so it needs no rule of its own.
- **Rear face = the back's height:** ≈ 66.4 (D 105) / 67.0 (D 115), ≈ 1.9T.
- **Playing pose:**
  - footprint ≈ 280 × **88.5 (D 105) / 99.8 (D 115)**, down from rev 3's 99 / 110;
  - overall depth, with the front face's forward lean, ≈ 100 / 110;
  - back ≈ 66–67 (unchanged), front ≈ 33.
- **Upright pose:**
  - it stands on the 280 × ≈ 66 back, the plate leaning back **≈ 18.4°** (16.9°);
  - the top edge is ≈ 100 (D 105) / 110 (D 115) up;
  - the drivers aim ≈ 18° up.
- **Underside:** open between the cheeks. No façade.

## Rev 5: checking the visual designer's rounding
Owner, verbatim: "I miss the subtle rounded shape of cathedral". Visual's rev 5 uses n = 5 superellipse corners: plan corners r 17.5, plate r 10, top-back edge r 8, base-to-back r 4, end-face edges rolled 3, cheeks 10 thick. The poses don't change. My check [calc; UNVERIFIED where marked]:

| Effect | Verdict |
|---|---|
| End face flat ≈ 64 in the slab band; port mouth at ≈ 60 along the plate | **OK.** The mouth with its groove (≈ Ø 40) spans ≈ 40–80, inside the flat (≈ 20.5–84.5), and still inside E's rear-region box |
| **Jacks in two rows at ≈ 11 and ≈ 24 below the plate** | **Must change.** The upper row hits the deck (its underside is ≈ 12 below the plate), and the lower row hits the right end cell (≈ 25.5–33 below the plate) if the cell sits under that jamb [eng r3 stack]. Only **one row**, centred ≈ 17–20 below the plate, fits between them. **Fix:** move power, TUNE and MIDI SPLIT off the end face (onto the plate, which also answers the job 31 question), leaving **5 items: phones, line, MIDI in, MIDI out, device USB-C at ≈ 12 pitch = 60 ≤ 64: one row**. Fallback: cell 2 moves ≥ 20 inboard, and two rows at ≈ 16 and ≈ 28 below the plate. UNVERIFIED (eng) |
| **Top-back edge r 8 (the upright foot's player-side edge)** | **Must change.** At the 71.6° corner, an r 8 moves the tipping edge ≈ 11 mm inward, so upright **rocks toward the player at ≈ 1.64 N** (rev 4: 2.52). **Use r ≤ 4 there:** r 4 → ≈ 2.08 N; r 3 → ≈ 2.19 N. The other edges can stay soft |
| Base-to-back r 4 (the upright foot's far edge) | OK. The top-row press drops to ≈ 3.4 N, the lower row to ≈ 4.5 N (rev 4: 3.9 / 5.1). A firm top-row press already wanted a steadying hand |
| Back's flat contact ≈ 245 of 280 | OK. Side-to-side tipping is nowhere near critical with the COM centred |
| Runners ≈ 7 of 10 flat | OK. ≈ 6.3 kPa on grass (rev 4: 4.4), far below a footprint's pressure. TPU strips 7 wide |
| Rounded footprint corners | OK. The effective playing footprint is ≈ 81 deep after the foot radii, with the COM still near its middle |
| Front face (host port) | OK, with a note. The flat strip is ≈ 16 high (35 − lip r 16 − foot r 3). A USB-C receptacle fits (overmold clearance UNVERIFIED). **The split target rail no longer fits there too:** it moves to the plate's front rim (job 6). Director condition (a) (host port low on a cheek) needs the receptacle in a 10 mm cheek, which is UNVERIFIED; the front face is the safer home |
| Knob rows 24 in from the ends | OK. That leaves ≈ 232 of width, so ≈ 10 per row at ≈ 23 pitch for Ø 10 knobs |
| Cheek 10 thick | OK. The plan corner finishes in the slab; the stretcher fits ≈ 260 between the cheeks |

**Rev 5 upright numbers with the top-back edge at r 4** (D 105; mass 0.8 kg and COM are ESTIMATES): pull ≈ **2.1 N**; presses ≈ **3.4 N** (top row) / **4.5 N** (lower row); tip angles ≈ 32° forward / 36° back.

## What lives where
| Volume / surface | Job |
|---|---|
| Slab | everything electronic and acoustic |
| Cheeks | both stands; the left cheek holds the port mouth, the right cheek the jacks |
| Rear face (slab strip + cheek edges) | **the upright foot**, with TPU strips. Nothing is mounted on it any more |
| Hollow under the slab | the cable bay when packed |
| Stretcher (**only with SHOE**) | the S9 dock and the cable-bay floor; it lies on the runner line, **moved forward to y ≈ 15–75**, so it's ≈ 13.5 mm clear of the back at D 105 (the runner line is now ≈ 88.5). At y 20–80 the gap would be only 8.5. The cheeks' stiffness doesn't depend on it (director ruling) |

## Speaker and every port, in both poses
| Item | Where | Angled | Upright |
|---|---|---|---|
| Drivers (E) | lancet grille in the plate | fire up and forward | **fire at the player, ≈ 18° up** (best) |
| Port Ø 16 × 140 | along x in the slab, mouth on the **left cheek**, in the slab band (≈ 17 from the plate) | end face vertical: open | end face vertical: open |
| USB-C host | slab front face, left of centre | the face leans 18° forward: **right-angle cable** lies flat (a straight plug clears by ≈ 6.6) | the face is **the top** (tilted ≈ 18° back): plug from above, and the cable falls toward the keyboard (0.3–0.5 m reaches) |
| Jacks and device USB-C (rev 5: **5 items, one row**, ≈ 17–20 below the plate) | **right end face**, in the slab band | reachable | reachable |
| Power, TUNE, MIDI SPLIT | **rev 5: onto the plate** (proposal; see the rounding check) | seen | seen |
| Lights | plate | seen | seen |

- **Visual:** the port mouth sits in the slab band, not at the cheek face's centroid. The growth rings centre on the mouth.
- **UNVERIFIED (eng):** jacks at the right end above the end cell (E puts the cells under the jambs). ≈ 8 items in a 35 × 105 band means one row on ≈ 12 mm pitch.

## Stability [calc; mass 0.8 kg, COM ≈ 17 mm from the plate inside the slab and ≈ 50 along it from the rear corner: ESTIMATES]
**Playing pose:** unchanged in kind. The hand on the front edge and knob presses land inside the footprint. Lap: runners one per thigh. Grass ≈ 4.4 kPa on the runners, and the angle holds. The footprint is ≈ 88.5 deep: still well clear of tipping under the hand. The COM sits over the middle of it.

**Upright, on the ≈ 66-deep back, leaning back θ.** The COM moves ≈ 32 mm in from the player-side edge (rev 3: 25; rev 2: 17). D 105 shown; D 115 is ≈ 10–15 % lower on every force.

| Load | rev 2 (90°) | rev 3 (9.5°) | **rev 4 (18.4°)** |
|---|---|---|---|
| Pull toward the player on the top edge | 1.27 N | 1.89 N | **2.52 N** (double rev 2) |
| Press into a top-row control | 4.6 N | 4.1 N | **3.9 N** |
| Press into a lower-row control | 5.6 N | 5.3 N | **5.1 N** |
| Ground tilt before it falls forward / back | ≈ 19° / — | ≈ 28° / — | **≈ 37° / ≈ 39°**: balanced |

- **Read:** the forward-pull weakness is about half-solved, and the COM now sits near the middle of the foot.
- Presses get slightly easier to tip: the top row at ≈ 3.9 N, so a firm press on HOLD or TAP there may still want a steadying hand (tactile-switch forces UNVERIFIED).
- It's a pose for standing, listening and light turns, and now **a reasonable light-playing pose**.
- **Grass upright:** fine. **Lap upright:** n/a.
- Eng condition b (mass low and away from the plate) still adds ≈ 0.07 N of pull resistance per mm.

## Poses (his order: angled, 90, flat)
1. **Angled (θ ≈ 17–18°) on the runners:** the main pose.
2. **Upright on the back, the plate leaning back θ ≈ 18.4°:** by shape, with the limits above.
3. **Flat:** not offered (he ranked it last). Laying it on its back would stand it on the cheeks' runners and front face at a slant, so it isn't a stable flat pose. Say so; don't fake it.

## Moves: bag to sound (3)
1. Out of the bag.
2. Slide the keyboard off (or take it from the bag).
3. Set it on the runners or stand it on its rear face, plug in, switch on.

- **Undock the keyboard before standing it upright:** a deep keyboard on the stretcher could reach past the rear corner and prop it (UNVERIFIED per keyboard).
- **Packing:** a wedge 280 × ≈ 100–110 overall × 66–67, with a vertical back; ≈ 81 with the keyboard docked. The docked keyboard closes the cable bay.

## States
- **No keyboard:** plays from USB or TRS.
- **Loose carry:** the cable bay is open; a printed clip holds the cable.
- **Battery and status:** unchanged.

## Making
The slab prints as r3 (one piece on a ≥ 300 bed, or split at the dividers, or NAVE bays). The cheeks print with the end caps. The stretcher is one flat print. TPU strips go on the runners and the rear face.

## Owner forks
- **"90": for playing or for standing?** (director's question) Standing: as drawn. Playing: light playing is fine (forward pull ≈ 2.2–2.5 N); firm top-row presses (≈ 3.5–3.9 N) may want a hand on the top edge.
- **"Multiple angles": several fixed poses, or a range?** Two fixed poses by shape here. A range would need a moving part; nothing is added until he says.
- **Carry:** SHOE (with the stretcher) / loose / TPU band.
- **Cast metal:** runner ends and the port ring, or none.

## UNVERIFIED (eng)
- the real mass and COM (they set every number in the stability table);
- the overall depth with the front face's lean (visual measures it on the drawing);
- the port through the cheek wall;
- jacks above the end cell;
- the right-angle cable's length (eng found 0.2 / 1 m only);
- the stretcher's stiffness;
- tactile-switch press forces.
