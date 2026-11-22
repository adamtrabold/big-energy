# GNOMON: how it works (systems, idea level) — rev 3

2026-11-22. PROPOSAL (the director's idea, turn 3). Scores: 8 (rev 1), 9 (rev 2). Rev 3 folds in the owner's change to rev 2, verbatim: **"Reverse the angle on the side behind the speakers so there’s still a subtle angle when upright"**. Rev 2 folded in his 18:39 / 18:40 pose words and director fix 6.

Sizes are [calc] from `eng/module-r3.md` facts. Mass ≈ 0.8 kg and the centre of mass (COM) are ESTIMATES. Nothing is measured.

## The idea
CATHEDRAL's lid standing on its own ends. A framed slab of constant thickness, the slab eng already proved holds everything. At each end the rim carries on down into a **cheek** whose end face has **two feet**:
- the runners give the angled pose;
- the rear face, behind the speakers, gives the upright pose, now leaning back a little.

That's his first two choices, both by shape, with no parts.

## How I read his change (plain)
- In rev 2 the rear face was **square to the plate** (the corner behind the speakers was 90°), so upright the plate stood exactly vertical.
- **"Reverse the angle"**: the rear face tips the other way from square. The corner behind the speakers **closes below 90°**, so standing on that face, the plate leans back by the same amount. In the angled pose the rear face still leans in, but about half as much as before (≈ 9° from vertical, against 18.4°).
- **The literal mirror** (the rear face leaning *out* by 18.4° in the angled view) would lean the upright plate back ≈ 37°. A vertical rear face (rev 1's) would lean it ≈ 18°. **Neither is "subtle"**, so I've read his goal ("a subtle angle when upright") as the deciding words. **If he meant the literal mirror, it's one number to change** (see the table under Stability).

## Structure, from the end face
- **Slab:** T = 35, D = 105–115 [eng]. As r3.
- **Cheek outline:**
  - front face T, square to the plate;
  - plate D;
  - **rear face at (90° − φ) to the plate**;
  - the runner line closes it.
- **Two angles, both from T and D** (the rule restated; **director's call**):
  - **Angled pose, unchanged: tan θ = T / D → θ ≈ 18.4° (D 105) / 16.9° (D 115).**
  - **Upright lean, new: tan φ = T / 2D**, half the angled slope → **φ ≈ 9.5° (D 105) / 8.7° (D 115)**. The corner behind the speakers is ≈ 80.5°. A deliberate ratio from the slab's own two numbers, not a pick.
  - **The rear face's length follows:** ≈ 67.2 (D 105) / 67.7 (D 115), so ≈ 1.9T, **no longer exactly 2T**. Keeping it at 2T instead would push θ to 20.0° / 18.1° and break tan θ = T / D. I keep θ, because the angled pose is his first choice and the director accepted its rule. **The hairline at T below the plate still shows "the lid plus its own thickness".**
- **Angled pose:**
  - footprint ≈ 280 × **99 (D 105) / 110 (D 115)**, down from rev 2's 111 / 120, back to rev 1's size, so it's better in the bag;
  - the back stands ≈ 66–67, as rev 2; the front ≈ 33.
- **Upright pose:** it stands on the 280 × ≈ 67 rear face, the plate leaning back **≈ 9.5°**. The top edge is ≈ 104 (D 105) / 114 (D 115) up.
- **Underside:** open between the cheeks. No façade.

## What lives where
| Volume / surface | Job |
|---|---|
| Slab | everything electronic and acoustic |
| Cheeks | both stands; the left cheek holds the port mouth, the right cheek the jacks |
| Rear face (slab strip + cheek edges) | **the upright foot**, with TPU strips. Nothing is mounted on it any more |
| Hollow under the slab | the cable bay when packed |
| Stretcher (**only with SHOE**) | the S9 dock and the cable-bay floor; it lies on the runner line at y ≈ 20–80, **≈ 19 mm clear of the rear face** (the runner line is now ≈ 99). The cheeks' stiffness doesn't depend on it (director ruling) |

## Speaker and every port, in both poses
| Item | Where | Angled | Upright |
|---|---|---|---|
| Drivers (E) | lancet grille in the plate | fire up and forward | **fire at the player, ≈ 9.5° up** (best) |
| Port Ø 16 × 140 | along x in the slab, mouth on the **left cheek**, in the slab band (≈ 17 from the plate) | end face vertical: open | end face vertical: open |
| USB-C host | slab front face, left of centre | the face leans 18° forward: **right-angle cable** lies flat (a straight plug clears by ≈ 6.6) | the face is **the top** (tilted ≈ 9.5° back): plug from above, and the cable falls toward the keyboard (0.3–0.5 m reaches) |
| Jacks, power, device USB-C, TUNE, MIDI SPLIT | **right cheek face**, in the slab band (fix 6) | reachable | reachable |
| Lights | plate | seen | seen |

- **Visual:** the port mouth sits in the slab band, not at the cheek face's centroid. The growth rings centre on the mouth.
- **UNVERIFIED (eng):** jacks at the right end above the end cell (E puts the cells under the jambs). ≈ 8 items in a 35 × 105 band means one row on ≈ 12 mm pitch.

## Stability [calc; mass 0.8 kg, COM ≈ 17 mm from the plate inside the slab and ≈ 50 along it from the rear corner: ESTIMATES]
**Angled:** unchanged in kind. The hand on the front edge and knob presses land inside the footprint. Lap: runners one per thigh. Grass ≈ 4 kPa on the runners (the footprint is shorter, so a little more), and the angle holds.

**Upright on the ≈ 67-deep rear face, leaning back φ.** The lean moves the COM back from the player-side edge, from ≈ 17 to ≈ 25 mm. That's what his change buys. D 105 shown; D 115 is ≈ 10 % lower on every force.

| Load | rev 2 (90°) | **rev 3 (φ ≈ 9.5°)** | literal mirror reading (≈ 37°), for comparison |
|---|---|---|---|
| Pull toward the player on the top edge | 1.27 N | **1.89 N (+49 %)** | ≈ 4.1 N, but a 37° lean is not subtle |
| Press into a top-row control | 4.6 N | **4.1 N** | ≈ 4.2 N |
| Press into a lower-row control | 5.6 N | **5.3 N** | similar |
| Ground tilt before it falls forward | ≈ 19° | **≈ 28°** | |

- **Read:** the forward-pull weakness improves by about half, and presses lose ≈ 0.3–0.5 N because the foot is 3 mm shorter and the COM sits nearer the back edge.
- It's still a standing, listening, light-turning pose, not a hard-playing one. A firm press on HOLD or TAP at the top row may want a hand on the top edge (tactile-switch forces UNVERIFIED per part).
- **Grass upright:** good for listening. **Lap upright:** n/a.
- **Further help:** cells and E's box low in the slab and away from the plate (director condition b): ≈ +0.07 N of pull resistance per mm the COM moves [calc].

## Poses (his order: angled, 90, flat)
1. **Angled (θ ≈ 17–18°) on the runners:** the main pose.
2. **Upright (≈ 90°, leaning back φ ≈ 9.5°) on the rear face:** by shape, with the limits above.
3. **Flat:** not offered (he ranked it last). Laying it on its back would stand it on the cheeks' runners and front face at a slant, so it isn't a stable flat pose. Say so; don't fake it.

## Moves: bag to sound (3)
1. Out of the bag.
2. Slide the keyboard off (or take it from the bag).
3. Set it on the runners or stand it on its rear face, plug in, switch on.

- **Undock the keyboard before standing it upright:** a deep keyboard on the stretcher could reach past the rear corner and prop it (UNVERIFIED per keyboard).
- **Packing:** a wedge 280 × ≈ 99–110 (footprint) × 66–67 at the back; ≈ 81 with the keyboard docked. The docked keyboard closes the cable bay.

## States
- **No keyboard:** plays from USB or TRS.
- **Loose carry:** the cable bay is open; a printed clip holds the cable.
- **Battery and status:** unchanged.

## Making
The slab prints as r3 (one piece on a ≥ 300 bed, or split at the dividers, or NAVE bays). The cheeks print with the end caps. The stretcher is one flat print. TPU strips go on the runners and the rear face.

## Owner forks
- **"90": for playing or for standing?** (director's question) Standing: as drawn. Playing hard: better than rev 2 (forward pull ≈ 1.7–1.9 N), but still wants a hand on the top edge for firm presses.
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
