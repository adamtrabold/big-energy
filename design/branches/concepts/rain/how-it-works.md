# RAIN: how it works (systems)

> **2026-11-13, keys:** the peg mount is redone in `../cathedral/how-it-works.md` §10. Stock plugs have ⅛–¼ in tenons; the 1/2 in size is the hole, not the head. The same carrier, stop and options apply here. Rev 2's shank-through-the-deck description is superseded.

Seed: **ONE SHEET** (v1.1, 276 × 180). Kind: a landscape. Point of view: **every control is a drop on still water; its rings spread until they meet the next drop's, and the meeting lines draw the panel's map.** Rule: *everything that breaks the surface ripples.* Emotion: calm. Read with `../common-how-it-works.md`, `versions/v1.1/one-sheet/how-it-works.md`, `versions/v1.1/common-how-it-works.md` and `design/jobs.md` rev 5.

**Rev 2, 2026-11-13 (round 1 scored 7; director's fixes).** Numbers marked [CHECK] are from `../branch_check.py` §7 (the current `rb.rain()` model, legends measured with OpenSCAD).

> ### R2.1 Legend and tick collisions, as the model stands now [CHECK §7]
> - **No legend overlaps.** The director's REVERB TYPE ↔ VELOCITY and ECHO TYPE ↔ OSC 3 CTL clashes don't appear in today's `rb.rain()`; they were fixed in parallel.
> - **One branch-new hit:** OSC 2's +50° tick and NOISE/EXT's −50° tick sit **0.05 mm** from the FREE / SYNC nut (rule 0.5; real nut ≈ 9.2 across corners). **Drop both** (same fix as CHAMBER).
> - **Inherited from v1.1 (in the locked ONE SHEET too):**
>   - STATUS ↔ MOD MIX legend 1.38;
>   - STATUS ↔ its LED 1.33;
>   - ±100° ticks ↔ OSC MOD / FILTER MOD / OSC 3 CTL nuts 0.22.
> - **Re-run the checker after every legend move.** Ripple decay and wider section bands move the lily pads, not the legends, so the counts should hold.
>
> ### R2.2 Making the decaying ripples (director fix 1), from what a printer can do
> - First layers face down at 0.2 mm, with a 0.4 nozzle:
>   - **depth has only two steps** (0.4 → 0.2 → 0);
>   - **a groove can't be narrower than one line** (≈ 0.4).
> - So "amplitude decays toward the seam" has to be built from:
>   1. **ring spacing that opens up** toward the seam, e.g. pitch 0.9 at the stone → ≈ 1.8 at the outer third, then none;
>   2. the **depth step** (0.4 near the stone, 0.2 outside);
>   3. the last ring stopping short of the seam, so the still band is smooth.
>
>   Still two finishes (smooth / rings). The coupon decides whether 0.2-deep rings read at all (**UNVERIFIED**).
> - **Wider section bands (fix 2):**
>   - a power diagram with weights set so a seam between sections is ≈ 3× one inside (e.g. still band ≈ 1.0 inside a section, ≈ 3.0 between);
>   - the bands are where the rings stop, not extra grooves.
>   - Check after: every legend's lily pad still sits inside its own cell (the visual designer's code computes the pads).
> - **Pitch compare (fix 5):** 0.45 is v1.1's first-layer line pitch (rings from the slicer's concentric fill, impossible per Voronoi cell). Modelled grooves can go to ≈ 0.8–0.9 at a 0.4 nozzle (groove + land ≥ 2 lines). **A 0.6 pitch would need a 0.25–0.3 nozzle: a nozzle swap at Vector Space (UNVERIFIED that they have one).**

**Rev 1, 2026-11-13, concept turn 1 (systems first).**

## 1. What changes from ONE SHEET, and what doesn't
**Unchanged:** the shell's outline and heights (276 × 180, deck z 24); the main board and every control; the I/O board on the rear wall; the speaker (bottom-firing at (240, 113)); the battery; the back panel and its 8 screws; the two finishes (smooth and rings, the owner's rule).

**Changes:**
1. **The ring field runs to every edge**, including the side walls' top chamfer. Section grooves and section headings go: **the Voronoi seams are the section marks** (director: "Courage!").
2. **Rings are modelled geometry, not a slicer pattern** (§3).
3. **Peg keys as stepping stones**; the key window becomes a deck (§2).
4. **FREE / SYNC** at (128.0, 132.7): one more stone, so it ripples. Legends beside it (common §2). With no headings in RAIN, common §2's MIXER move doesn't arise.
5. **Legends on smooth "lily pads"** cut out of the ring field.

## 2. Keys: pegs on ONE SHEET (J1, J21) [CHECK]
- **Mechanism:** HUSH's: 1/2 in button plugs on acrylic arms, centred over the Choc V2 stems, magnet 10.5 behind. Whites at x 12 + 18n (HUSH x − 7). Two stone greys (white / sharp distinction kept, director).
- **Width:** the visual designer's "+8 mm" assumed HUSH's 19 mm felt collar. Checked:

  | Bottom stop | Last peg to the outside | To the flat (R 2 edge) | Width needed |
  |---|---|---|---|
  | HUSH's 19 mm felt collar | 2.5 | 0.5 | **+5 mm (281)** for ≥ 3 mm on the flat |
  | **14 mm felt washer (pick)** | 5.0 | **3.0** | **276, unchanged** |
  | head only | 5.65 | 3.65 | 276 |

  **Pick: the 14 mm washer** in a 1 mm counterbore, ringed by ripples. ONE SHEET stays 276 wide.
- **Edge A with pegs:** the washer would allow whites at y ≈ 9, but **strip C sets the limit**: in HUSH it reaches ≈ 11.5 in front of the white stems (stems y 13.5, strip C from y ≈ 2), and ONE SHEET's front wall is 2.4 thick. So whites at **y ≈ 14** (head front ≈ 7.65 from the front face) and sharps at y ≈ 36.5 [CALC]. That's HUSH's edge A, essentially.
- **The key window closes into a printed deck with 25 holes**, one per peg shank, each with its own ring field. Hole size as HUSH (**UNVERIFIED**: shank Ø not restated in HUSH's file).
- **Strip C moves to peg positions** (stems under the pegs: strip C ≈ y 2.4–50.5 [CALC from HUSH]). The main board must start behind it. **Eng (E-L9 again).**
- **Height:** heads 6.5 proud (R4's "≈ 3 mm" doesn't hold; HUSH precedent). The body height is unchanged; the heads rise above the deck.
- **Bag (J6):** the owner deferred case work for ONE SHEET. With pegs 6.5 proud, a bag's side loads land on the pegs and arms (pressed down they're harmless when off; sideways is untested). **Risk, UNVERIFIED**; a sleeve would fix it, but that's the owner's deferred topic.

## 3. Making the rings (J11)
- A slicer's concentric pattern follows a region's outline, so a Voronoi cell would get polygon rings (visual's finding, agreed). **Model the grooves**: each groove ≈ 0.45 wide at ≥ 0.9 pitch, 0.2–0.4 deep, in the first layers printed face down, generated per control as circles clipped to that control's Voronoi cell. OpenSCAD can do it (the cells' intersection is cheap); the face is ≈ 276 × 180 of grooves, so render time is long but bounded (**UNVERIFIED**).
- **The print split (common §5, x 122.5) loses its hiding place.** In v1.1 the joint sits in the bottom of the x 122.5 groove; RAIN has no grooves. Options:
  1. **Print in one piece** on a 350 bed (Voron 350 at Vector Space, **UNVERIFIED**). Recommended: the field must be unbroken.
  2. Split along a **Voronoi seam** (a jagged lap joint). It hides, but the cut path is irregular and the lap is harder to make.
- **The ring coupon** (smooth + rings, already pending for ONE SHEET) now also decides RAIN's pitch and look. The director wants it seen under a tree.

## 4. Power-on, not power-off
The director's "a drop when you close it" can't happen at power-off: the hard switch kills the Daisy instantly. **A single soft "drop" when the status light reaches ready** (firmware, $0, off by a key combo) is the honest version. Optional, not part of the concept test.

## 5. States
| State | What it is | Systems notes |
|---|---|---|
| **Closed** | n/a: ONE SHEET has nothing to close | — |
| **Carried** | in a bag | pegs exposed (risk above); jacks on the rear wall; the power switch is recessed (H7) |
| **Flat** | on a table, a lap, a bench | as ONE SHEET; pegs at the front edge |
| **Standing** | n/a (no stand; J18 optional, not taken) | — |
| **Outdoors** | grass, bench, dappled shade | the speaker fires down into the grass (weak outdoors, UNVERIFIED); status light hood (common §3); legends on lily pads: readable in sun **to be proven** by a render and the coupon |

## 6. Can't verify here
The ring pitch's look at 0.9 vs v1.1's 0.45 · Voron 350 availability · peg shank hole · strip C vs the main board · peg survival in a bag · lily-pad legibility in sun · render time of the full grooved face.
