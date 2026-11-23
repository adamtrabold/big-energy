# CRADLE: how it works (systems, idea level) — rev 1

2026-11-22, round 2, turn 4. PROPOSAL (the director's lead concept, turn 3 amendment). Owner 19:23, verbatim: "So one arrangement that can either be flat or slightly angled is the best multiple arrangements it can be"; 20:27: "I do wish it was more distinctive refardless". The slab is GNOMON rev 5 / SILL's (280 × 115 × 35, speaker E, plate drivers by default). [calc] = my arithmetic from published data; mass ≈ 0.8 kg and its centre (≈ 57 back, ≈ 17 up) are ESTIMATES; UNVERIFIED = eng or a first-print trial. The owner measures nothing.

## The idea
The instrument tilts within its own cheeks. Two end blocks carry the growth rings. The slab hangs between them on pins at its front edge. **Flat:** the slab lies level with the cheek fronts. **Slightly angled:** lift the back and set it on a ledge, and the plate comes up flush with the cheek tops. One moving part (the slab itself), nothing outside the outline in either state.

**Randomness used** (Python `secrets`): field **"piano music desks"**. A grand piano's desk doesn't hold its angle with a spring. It rests on a ledge, and the weight seats it. That fixed CRADLE's main problem (below). Field **"Japanese joinery"**: the cheeks are held by wedged tenons (kusabi), with no screws. Oblique **"Give way to your worst impulse"** went to PLINTH.

## Finding 1: a detent at the pivot can't hold the angle [calc]
- Holding the slab at ≈ 9° takes ≈ **0.8 N·m** about the front pins: its own weight (7.8 N × 49 mm) plus a resting palm (≈ 15 N × 30 mm).
- A detent at an 8 mm radius would need ≈ **100 N** to resist that. At the back (r ≈ 90) it would still need ≈ 9 N, more than a printed flexure gives. It would also feel mushy and wear.
- **So the load has to go into a hard seat, not a detent.** That's the music-desk ledge.

## Structure (end view; y back from the front lip, z up)
- **Slab:** 280 × 115 × 35, as SILL. Its ends are square, because the cheeks cover them. The soft n 5 plan corners move to the cheeks' outer corners.
- **Front pins:** Ø 4, on each slab end at **(8, 8)**, bought steel or printed metal. The slab's front-bottom edge is an **r 8 arc centred on the pin**, so it rolls on the table without digging in or lifting.
  - Each pin runs in a **5 mm horizontal slot** in its cheek (blind, on the inner face).
- **Rail (the stretcher, and the ledge):** printed, ≈ 264 × 10 × 10, between the cheeks **just behind the slab** (y ≈ 116–126). **Its seat sits at T/2 = 17.5 above the table**, with a 2 mm channel along its top.
  - Flat, the slab's back stands 1 mm in front of it, so the slab can't slide back.
  - The rail's ends are tenons through the cheeks, each locked by a printed wedge driven from underneath. You can't see the wedges from the side, and they come out without tools for repair.
- **Cheeks:** printed, 12 thick (1 mm gap to the slab), ≈ 127 deep. Two outlines; see *Fork* below.
- **Overall:** **306 × 127**, height 35 at the front, 52.5 at the back (cheek A).

## The angle, from a part
The rail's seat height is T/2. θ is whatever angle puts the slab's rear-bottom edge on it: zp(1 − cos θ) + (D − 8) sin θ = T/2, so **θ ≈ 9.4°** [calc]. That's the same rule as SILL and PLINTH ("the back rises half the slab's thickness"), so the three columns compare fairly.

## States and moves
| State | Load path | Move |
|---|---|---|
| **Flat** | the whole slab base on the table; pins at the front of their slots | — |
| **Slightly angled (≈ 9.4°)** | the front r 8 arc on the table plus the slab's rear edge in the rail's channel. Every press drives it deeper into the seat | **1 gesture:** lift the back ≈ 20, push it away 5, set it down |
| Back to flat | — | **1 gesture:** lift ≈ 2, draw it toward you, lower |
| **Packed** | flat | — |

- **The front lip barely moves:** the slide back cancels the forward lean, so the lip moves **+0.7 mm** between states [calc]. The wrist edge stays where it was.
- **Rocking:** a full-width line (the arc) plus a full-width seat (the rail), so there are no four corner points to rock between. The slab is stiff, so if the rail sags it bears near the cheeks (sag in printed ASA at 10 × 10 is UNVERIFIED). A TPU strip in the channel takes up print tolerance.
- **Unseating:** a pull toward the player can't free it. The edge has to rise 2 mm out of the channel against ≈ 3.4 N of rear load. Lifting the rear with the wrist on the front lip takes ≈ 46 N [calc].

## Fork (visual and director): the cheek outline
- **A, the cheek is the angled pose (recommended for the thumbnail test).** The cheek's top runs at θ from 35 at the front to **52.5 = 1.5 T** at the back, with a vertical back and n 5 corners. **Angled, the plate lies flush with the cheek tops.** Flat, the slab rests in the cheeks, which rise up to 17.5 above the plate at the rear (≈ 4 above it at the back knob row: no finger conflict). The end view is the same soft wedge in both states: **one silhouette, unlike SILL's and PLINTH's.** Packed 306 × 127 × 52.5 ≈ 1.70 L.
- **B, a low cheek (the director's sketch).** The cheek is 35 tall, so angled, the slab's back rises ≈ 17 above the cheeks. Packed 306 × 127 × 35 ≈ 1.36 L. **Flat, its end view is a plain rounded rectangle, the same as SILL's at thumbnail size.** It fails the test in one of its two states.

## Ports, wiring, speaker
- **Nothing crosses the pivot.** Everything stays on the slab.
- **Jacks move to the front face**, because the cheeks cover the ends and E fills the rear. There's **one row of 6** (host USB-C, phones, line, MIDI in, MIDI out, device USB-C, ≈ 72 wide) on the stacked front boards. This needs a front-face flat of ≥ 12–14, so the front-top lip must be **r ≤ 12** (rev 5 has r 16) above the r 8 pin arc. Reachable in both states; cables run toward the player. UNVERIFIED (eng: connector heights, plug overmolds).
- **The port mouth** goes on the **rear face, above the rail** (z ≈ 20–34), through a flared elbow at the end of E's Ø 16 × 140 port. It's open in both states (bass doesn't care which way it points). UNVERIFIED (eng: the bend and the mouth 1–2 mm above the rail). Fallback: a kidney window in the left cheek around the end-face mouth, which moves ≈ 3 back and ≈ 8 up between states.
- **Growth rings** can centre on the pivot pin, so the rings mark what the slab turns about (visual's call).
- **E's volume:** nothing is recessed into the rear box. So **D 105 (eng's 4 % margin) is possible again**. It's drawn at 115 so the slab matches SILL.
- **End speakers (asked, unanswered):** the cheeks would cover them. They'd have to live in the cheeks, ≈ 25 thick, with a flex loop across the pivot. Not drawn.

## Stability [calc]
- **Table:** the cheeks stand on 2 × 12 × 127 at 306 wide in both states, and the slab adds its base (flat) or its arc line (angled). Every press lands inside.
- **Lap:** one cheek per thigh.
- **Grass:** ≈ 2 kPa.

## Carry
- **SHOE:** the dock is in the slab base at y 10–70, clear of the pin arc. Docked, the keyboard sits under the slab and the cheeks ride ≈ 14 above it. Packed only.
- Loose or the TPU band also work.

## Making and weight
- **Parts:** slab as r3, 2 cheeks (shelled), 1 rail, 2 wedges, 2 pins. The cheeks fit any bed.
- **Weight:** ≈ 0.79–0.97 kg (module 0.70–0.85 + cheeks ≈ 0.06–0.08 + rail ≈ 0.02) [est].
- **Named trial:** the rail channel's fit and the slot clearances on the first print.

## Owner forks
- Cheek A or B.
- Is a steel pin "stuff"? If not, printed metal.
- Jacks on the front face (a consequence of the cheeks).

## UNVERIFIED
- Mass and centre of mass.
- Rail stiffness.
- Port elbow.
- Front-face connector fit at r ≤ 12.
- Wedge-tenon tolerance.
