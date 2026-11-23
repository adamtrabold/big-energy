# TRIANGLE: how it works (systems, idea level) — rev 1

2026-11-23, round 3. PROPOSAL (director's round 3 steer). **Owner, verbatim:** "I want options. Do one that’s a triangle too"; "The end view I’d not a triangle" (EASEL's front face cuts it). Also used: "Make the base and the back 90 degrees when sitting flat" (19:02); "Drop to one speaker".

**Marks:** [calc] = my arithmetic (section search over angle and size; knob band ≈ 22 behind the plate; TEBM28C10-4B Ø 55 × 24 deep, ≈ 28 behind the plate with its gasket; walls 2). Mass ≈ 0.8 kg and the centre of mass (COM) are ESTIMATES. UNVERIFIED = eng or a trial.

## Three faces, and what they force
- Plate, base and back only. No front face, so the plate starts at the table.
  - **The lowest knob row has to sit ≥ 20 up for fingers.**
  - **The speaker loses EASEL's foot.** A flat driver in the foot needs either slots in the plate's bottom strip (masked by the keyboard) or a duct, and the duct runs right through the first row's pots. Killed.
- **Speaker home, compared:**
  - **Back face: killed.** It fires 180° from the player, which is the weakest case in a park.
  - **End face:** a Ø 55 frame needs an inscribed circle ≥ Ø 59 in the end view, so an equilateral side ≥ ≈ 104 or a right triangle with a hypotenuse ≥ ≈ 142. That's *bigger* than the plate option. It's also 90° off-axis: the datasheet claims only "wide directivity" and its polar plot gives no readable numbers, so the shimmer-band loss is UNVERIFIED.
  - **A grille in the plate, recommended.** It fires straight at the player, its on-axis response is the only one that's published, and it gives the smallest section.
- **Layout that makes it small: the grille *between* the two half-groups.** Each row is 5 | grille | 5 (10 | 10 = 20 controls), with **TAP + lights on the axis just above the grille** (TAP's ring = tempo / status). That's 21 controls, mirrored, in signal order as rev 2.4's rows. Width: 98 + 61 + 98 ≈ 257 of ≈ 260 usable. **Tight:** 290 wide if eng wants margin.
  - The grille's bottom edge sits ≥ 18 up (above a slim keyboard) and ≥ 31 from the base (the driver's depth).

## Which triangle [calc]
| | (a) Equilateral | **(b) Right, base ⟂ back, recommended** |
|---|---|---|
| Plate angle | 60° | **45°**: the parts don't choose (the section varies < 7 % from 35° to 60°), so the deliberate ratio does: **base = back** |
| Size (280 wide) | 108 deep × 94 tall, ≈ 5,050 mm² | **≈ 91 × 91, ≈ 4,160 mm², ≈ 1.16 L** |
| Rows (z) | 34 / 49 | **36 / 48** |
| TAP / lights | z ≈ 74 | z ≈ 69 |
| Spare plate under the apex | ≈ 6 after the r 6 apex | ≈ 8 after the r 6 apex (a 45° apex rounds off more) |

- **(b) is ≈ 18 % smaller in section,** uses his own 19:02 rule, and its vertical back carries the jacks naturally.
- Narrower alternatives in (b): 55° gives 75 × 107, 60° gives 69 × 119 (taller, weaker to a top pull).
- **(a) is not "EASEL minus 37":** removing the front face makes the triangle bigger (108 × 94 vs EASEL's 79 × 80), because the front face was where the driver lived.

## Inside (b)
- The driver sits behind the grille (s ≈ 32–87). The box is the volume behind it (plenty).
- Cells flat on the floor at the ends; two pot boards flanking the driver; one small board for TAP and the lights.
- **Host USB-C: low on the left end** (≈ y 35, z 10), near the base and the front corner, so a tug pulls it sideways, not over.
- **Port mouth:** left end, at the end grain's centroid (≈ y 61, z 30), ≈ 20 clear of the host.
- **Jacks:** one row low on the vertical back.
- **Power / TUNE / SPLIT:** recessed pocket on the right end (as EASEL rev 2.4).

## Stability (b) [calc; ESTIMATES: mass 0.8 kg, COM ≈ 55 back, 35 up]
| Load | Result |
|---|---|
| Knob press (rows, square to the plate) | tips only above ≈ 39 N, and slides first at ≈ 44 N: never in use |
| **TAP press (z ≈ 69)** | **tips back at ≈ 7 N**: 2–3× a tact switch (UNVERIFIED), fine for tapping, not for thumping |
| Pull toward you at the apex | ≈ 3.5 N (the apex is over the back edge) |
| Palm on the apex | vertical: safe to ≈ 60 N (≈ 4 mm behind the tipping edge) |
| Lap / grass | 91-deep base, fine on still thighs; ≈ 0.3 kPa |

## Packing
A prism 280 × 91 × 91. SHOE in the base (91 ≥ 60). The plate faces out with the rim 1 mm over the knobs (job 33 weak); same packing line as EASEL.

## Costs on the trade line
- Bigger than EASEL (91 × 91 vs 79 × 80).
- The face carries a grille (no longer all controls).
- Width is tight (257 of 260).
- TAP tips at ≈ 7 N.
- Steep, so it isn't flat or slightly angled (scope, as EASEL).

## UNVERIFIED
Mass and COM; the plate-grille box (eng re-picks); the width fit; TEBM28 off-axis (Fig. 3.3.1 not readable); tact-switch forces.
