# SILL: how it works (systems, idea level)

2026-11-22, round 2. PROPOSAL. Owner 19:23, verbatim: "So one arrangement that can either be flat or slightly angled is the best multiple arrangements it can be". The slab is GNOMON rev 5's (framed lid, n 5 corners, eased edges, plate drivers by default, port mouth on the left end grain, jacks on the right end, power / TUNE / SPLIT on the plate). Only the base is new. [calc] = my arithmetic; mass ≈ 0.8 kg is an ESTIMATE; UNVERIFIED = eng or a trial.

## The idea
CATHEDRAL's lid lying down, with one flush bar in its base. Flat, it's a calm slab on the table. Flip the bar down with a fingertip and the back lifts slightly. The bar is invisible from above, and nothing goes outside the outline except the bar itself, straight down under the back.

## Structure
- **Slab:** 280 × D × 35. **D 115 recommended** (see Speaker).
- **The bar:** printed, ≈ 280 × h × 3–4, in a flush recess along the base's rear band (y ≈ D − h − 2 to D). It hinges at the rear-bottom edge on printed knuckles, with short pin stubs at each end (a bought Ø 3 steel pin, or printed metal if "stuff" excludes it). A finger notch sits at its free edge.
- **Travel:** 0° (flush) to a stop a few degrees past 90°. Tilted, the bar's foot sits behind its hinge, so plate loads drive it into the stop.
- **Detents:** a printed flexure tongue presses a flat on each knuckle, at 0° and at the stop. Fatigue is UNVERIFIED; fallback: two small magnets.
- **Feet:** TPU strips along the front foot and on the bar's edge.

## The angle, from its parts
θ = asin(h / (D − 5)):

| h | D 105 | D 115 |
|---|---|---|
| **T/3 ≈ 11.7 (lean)** | **6.7°** | **6.1°** |
| T/2 = 17.5 | 10.1° | 9.2° |

Director's call. The panel is identical in both states; only the slope changes.

## States and moves
| State | How | Move |
|---|---|---|
| **Flat** | on the whole base, the bar flush | — |
| **Slightly angled** | bar down, standing under the back | **1:** a fingertip flips it until it clicks into the stop |
| **Packed** | flat, the bar held flush by its detent | — |

**Bag to sound:** out, keyboard off (SHOE) or out of the bag, set down (flip the bar if you want the slope), plug in. **3–4 moves.**

## Stability
- **Flat:** whole base. Table, lap and grass are all fine.
- **Angled:** front foot plus a full-width bar line, ≈ 280 × 100. A knob press and the hand on the front edge land inside it. Lap: two full-width lines across both thighs. Grass ≈ 3.5 kPa under the bar's edge. Nothing tips at 6–10° [calc].

## Ports and speaker
- **Unchanged from GNOMON rev 5.** Host port on the front face; jacks (one row of 5) on the right end; port mouth on the left end; drivers in the plate (default, pending his end-speaker answer).
- **Speaker E margin:** the recess takes ≈ 11–22 cm³ from E's rear-region box. **At D 105 that eats E's ≈ 4 % margin** [eng r3], so use **D 115** or a 3 mm bar at T/3 (≈ 11.5 cm³). UNVERIFIED (eng).
- **If he wants end speakers:** SILL is unchanged; only the slab's insides move (`../c-gnomon/side-speakers.md`).

## Carry
- **SHOE dock at y 10–70:** clear of the recess at y ≈ 85–105.
- With a keyboard docked, the bar can't deploy, which only happens when packed.
- Loose or the TPU band also work.
- **Packed size:** the slab, 280 × 105–115 × 35. The smallest of anything this loop.

## Making
- Slab as rev 5.
- The bar is one flat print.
- The knuckles and the flexure tongue print with the base.
- Pin stubs: bought or printed metal.
- **Named trial step:** detent feel and fatigue on the first print.

## Owner forks
- Angle: T/3 vs T/2 (director first).
- End speakers or plate (asked).
- Is a steel pin "stuff"? If not, printed metal stubs.
- Carry: SHOE / loose / band (pending as before).

## UNVERIFIED
- E's volume with the recess (eng);
- detent fatigue in ASA / PETG;
- knuckle clearance and wobble;
- the bar's stiffness over 280 mm under ≈ 0.4 kg (a 4 mm printed bar on its edge is very stiff in that direction [est]).
