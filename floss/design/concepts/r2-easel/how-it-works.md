# EASEL: how it works (systems, idea level) — rev 2.1

2026-11-22, round 2. PROPOSAL. Rev 2 applied the director's four fixes (EASEL 8, `../../scores.md`). **Rev 2.1 is a check of rev 2 by a new systems seat: rev 2's 68 × 68 section doesn't close, so the section grows. The idea and the fixes stand.**

**Owner, verbatim (20:46):** "I do like one that sits up at an angle with a narrow footprint, I feel like that wil be most convenient for tables on the go esp with an external keyboard — like cathedral at least but without the keyboard"; "Why would I have two mono speakers that’s stupid. Drop to one speaker".

**Marks:** [calc] = my arithmetic from published data (`eng/module-r3.md`: TEBM28C10-4B Ø 55 × 24 deep; deck 10 below the rim, board 6.5–10.9 below the deck). Mass ≈ 0.68 kg and the centre of mass (COM ≈ 36 back, 30 up) are ESTIMATES. UNVERIFIED = eng or a trial.

## The idea (unchanged)
CATHEDRAL's raised lid standing on its own: a soft gable, plate at 60° in front, back at 60° behind, on a low front face (the predella) that speaks through lancet slots. Growth rings on the gable ends. One arrangement, no moving parts, no grille on the plate: the face is all controls.

## Fix 1 checked: the driver in the foot — **yes, but not in a 68 × 68 section** [calc]
- The two knob rows need a band ≈ 22 deep behind the plate's surface (deck 10 + pot and board ≈ 12). A Ø 55 × 24 driver lying flat (cone down over a 6 mm front chamber) must sit behind that band and inside the back wall.
- In rev 2's section (predella 18) the space behind the band is ≈ 37 wide at the baffle and ≈ 10 wide at magnet height: **the driver doesn't fit.** Even with the deck flush (band 13) it needs a predella ≈ 28.
- **It first fits at predella f ≈ 36** (band 20–22; driver centre ≈ 38 back). The driver's basket shape is UNVERIFIED, ± 2 mm.

## Fix 2 restated: the section [calc]
| | rev 1 B | rev 2 (as written) | **rev 2.1** |
|---|---|---|---|
| Predella | 12 | 18 | **≈ 36** (lancets low, host port above) |
| Plate | 100, top half empty | 58 | **58, two rows + lights** |
| Height | 98.6 | 68 | **≈ 86** |
| Footprint | 61 | 68 | **≈ 79** |
| Volume (envelope) | 1.08 L | 0.72 L | **≈ 1.10 L** |

- **The ratio:** a square needs height = footprint, which with two 60° faces only happens at ≈ 68. At 86 a square would need the back at ≈ 56.5° and a footprint of 86. **I recommend keeping both faces at 60° (equal pitches) as the deliberate rule:** the narrower foot is his point, and the square's extra tip margin is cancelled by sliding (below). φ is dropped, as in rev 2.
- **Honest read:** the fix removes the empty field, but EASEL ends up as big as rev 1, lower and deeper. It's still the narrowest footprint of the round (79 vs SILL ≈ 105–111).

## Stability [calc; ESTIMATES above]
Pressing square to the plate (knob height doesn't change it: the force runs along the knob's axis):

| Load | rev 2.1 tips at | slides back at |
|---|---|---|
| Lower row (s 14) | ≈ 49 N | **≈ 11.5 N on TPU strips (μ ≈ 0.8); ≈ 5.4 N on bare print (μ ≈ 0.5)** |
| **Top row (s 31)** | **≈ 12.5 N** | same |
| Lights band (s 45, no control) | ≈ 7.8 N | same |
| Pull toward you at the apex | **≈ 2.8 N** (forward) | — |
| Palm on the apex | **never, at any force**, if it pushes within ≈ 19° toward you or ≈ 30° away from vertical | — |
| Ground tilt | ≈ 50° forward / 55° back | — |

- **At 60°, a press pushes mostly backward, so sliding comes before tipping.** TPU grip strips on the foot are required, not a nicety (μ UNVERIFIED). A normal knob turn or button press (≈ 2–5 N, tact-switch forces UNVERIFIED) is fine on TPU.
- Rev 2's own figures (15 N, 2.2 N) don't follow from its stated mass and COM (I get 19.3 / 2.6); they're superseded anyway.
- The forward pull at the apex is still the weak point: lift it by the ends. Plugging into the back-face jacks pushes it forward and down: it steadies, but slides at ≈ 10 N, so hold it.
- **Lap:** fine on still thighs (79 deep). **Grass:** ≈ 0.3 kPa, fine on firm ground.

## Fix 3 checked: r 17.5 plan corners
- Two r 17.5 corners fit wherever the section is ≥ 35 deep: **below z ≈ 56 of 86.** Above that the end rounds off like a hipped roof (soft; visual's and the director's read).
- The flat gable end is ≈ 38 wide at z 10 and ≈ 26 at the port's height: enough for the port mouth and the rings, **not for a 60-wide jack row**, so the jacks stay low on the back face.

## Fix 4 checked: the box and the port
- Behind the knob band and above the cells, the section is ≈ 1,450 mm² **(≈ 290 cm³ over 200 mm)**; eng's C needs ≈ 150 gross (120 net + port + driver). The box fits with room; eng may grow it (benefit UNVERIFIED).
- **Port Ø 12 × 155** along x to a **mouth at the end grain's centroid (≈ y 32, z 30)**, where the rings centre. That point is behind the knob band, inside the box.
- **Lancets:** the front chamber is only 6 tall, so 8 slots × 8 × 12 (≈ 770 mm², ≥ 620) need a ≈ 9 mm plenum in front of the driver's frame, rising to z ≈ 16. **UNVERIFIED (eng): the slot-loaded chamber acts as a low-pass**, the main acoustic risk; an early listening test.
- Cells flat on the floor at the ends; the pot board(s) behind the plate; a second board over the cells: two boards.

## The controls, counted plainly
- **Positions:** 232 usable × 2 rows at 22 pitch = **2 × 11 = 22**.
- **The slabs' panel as drawn (19 knobs) + power, TUNE, SPLIT = 22: it fits exactly, nothing spare, no centre gutter.**
- **jobs.md's full inventory doesn't:** 12 rotaries (OCTAVE ×2, ATTACK, RELEASE, PRESSURE, SHIMMER, DEPTH, ECHO, TIME, REPEATS, REVERB, VOLUME) + 6 strand tabs + HOLD, TAP, FREE / SYNC = **21, + 3 utilities = 24, and the centre gutter costs ≈ 1 position a row.** Two short.
- **Two rows still work if** the tabs and buttons sit at ≈ 15 pitch (≈ 435 of 464 mm with the gutter) **and power / TUNE / SPLIT move to the back face beside the jacks.** That depends on his unanswered job 31 question (do set-and-forget controls count as "all controls in one plane"?). Otherwise a third row: plate +17, height ≈ +15, pull ≈ 2.4 N.

## Packing and the keyboard
- **Prism ≈ 280 × 79 × 86.** SHOE docks in the base (79 ≥ the 60 dock). The recess sits under the front chamber, so the predella grows ≈ 3.5 (UNVERIFIED) when SHOE is chosen.
- The plate faces out; the rim is 1 mm over the knobs (job 33 weak). 3–4 moves bag to sound.

## Owner forks
Replace or join flat-or-slightly-angled; utilities on the back (job 31); tabs at 15 pitch or a third row.

## UNVERIFIED
The driver basket shape and the predella height; the slot low-pass; mass and COM; TPU friction; tact-switch forces; jacks on the back face over the cell.
