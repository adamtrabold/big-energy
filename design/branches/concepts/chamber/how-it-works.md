# CHAMBER: how it works (systems)

Seed: **FOLD-105** (v1.1). Kind: an instrument case. Point of view (director, turn 3): **closed it's an organ case; open it's a console.** Emotion: joy. Read with `../common-how-it-works.md`, `versions/v1.1/fold/how-it-works.md` (rev 5.7) and `design/jobs.md` rev 5.

**Rev 1, 2026-11-13, concept turn 1 (systems first).** Numbers marked [CHECK] come from `../branch_check.py` §4b and §6.

## 1. What changes from FOLD-105, and what doesn't
**Unchanged:** both boards, every control position, the Daisy in the base, the slim battery and speaker in the lid band, the hinge and the 40-way ribbon, the brass stays (120°, 44.4 mm, tip ≈ 6.8 N), the I/O (audio/CV jacks + power on the lid's far wall; MIDI IN/OUT + USB-C on the base's right end face), the walnut block + white pickguard construction, screws from the back.

**Changes (the outside only, plus the shared FREE / SYNC toggle):**
1. **Reverse peg keys:** walnut naturals, maple sharps (§2).
2. **Lid walls +2.6 mm** for peg clearance when closed (§3).
3. **The façade on the lid back** (§4).
4. **The two front lid-back feet move** from d 30 to d 6 (§4).
5. **RANGE scales in feet** (32' … 2'), serif. Graphics only; the RANGE positions are already in feet in the spec.
6. **FREE / SYNC** at lid (133, d 70.6), a black FOLD toggle, legends beside it in the v1.1 type ("free" left, "sync" right). Serif stays on RANGE and the name only (director).

## 2. Keys: reverse pegs on FOLD (J1, J21)
- **Part and mechanism:** HUSH's, unchanged in principle: 1/2 in (12.7 mm) mushroom button plugs on laser-cut acrylic arms, each **centred over its Choc V2 stem**, D31 magnet 10.5 behind the stem over the SS49E (HUSH rev, eng E-L5). Naturals walnut, sharps maple: both are bought button plugs (walnut plugs: availability UNVERIFIED; maple is HUSH's).
- **Positions (edge A, HUSH's edge-A geometry):** naturals at **y 13.5**, x 17 + 18n (FOLD keys start x 8); sharps at **y 36**, on the white boundaries in piano positions.
- **Bottom stop:** a **14 mm punched felt washer** in a 1 mm counterbore in the base pickguard (HUSH used 19 mm collars in felt; 14 mm keeps each washer inside its 18 mm pitch with 4 mm of print between). Head underside 2.5 above the washer at rest; head top **6.5 above the plate** (z 22.1) [CHECK].
- **Strip C moves to HUSH's peg layout** (y ≈ 2–50). Strip C is its own board, so the main board is unchanged, **but** FOLD's base board must start behind y ≈ 52. **Eng to confirm** against the PLAY row's pots (CUTOFF at y 68, r 10.4).
- **Rule notes:** pegs stand 6.5 proud, so the team's R4 "whites within ≈ 3 mm of the panel" doesn't hold (HUSH precedent; the owner loves those pegs). The owner's own rule ("nothing raised between keys and controls") holds: pegs are the keys.
- **Owner question (open):** reversed colours vs sight-reading.

## 3. Closed height with pegs [CHECK]
- Closed, **14 lid items land over a peg** (V2 and back-row knobs, and the FREE / SYNC toggle).
- To keep v1.1's 2.0 mm clearance over a peg head: **lid walls +2.6 mm → closed ≈ 52.7 mm** (v1.1 ≈ 50.1). The director's estimate was +4 (≈ 54); the check gives +2.6.
- Conservative: toggles are counted at knob height, as in v1.1. Real toggle lever height: **UNVERIFIED** (the part isn't chosen).
- A pocket in the lid can't help: what lands over the pegs is knobs, not plate.
- **Open state unaffected:** the stand, the stays and the tip figure don't change (+2.6 mm of lid wall moves the lid's centre of gravity by < 1.5 mm [CALC]).

## 4. The façade (lid back) [CHECK]
**The order of use is the concept** (director): closed → you carry the façade (it's the top of the bar); flat (180°) → it's face-down on its feet, and the instrument is just a console; standing (120°) → the façade faces the listener and the console faces you.

**Geometry (proposal, the visual designer draws it):**
- **25 pipes, one per key, C to C over 2 octaves: length = L × 2^(−n/12), so the longest is 4× the shortest.** L = 66 mm → 66 … 16.5 mm.
- **Organ-builders' tower:** the longest on the axis (x 143), then alternating outward; pitch 10 → field x 18–268.
- **Pipe feet on one impost line at d 18**; tops reach d 84 at the centre.
- **Screws:** the v1.1 back screws at d 12 (x 16, 143, 270) sit on the impost line, under the pipe feet (the director's "impost rivets"). The d 96 screws sit above the tallest top. Clear [CHECK].
- **Feet: clash.** v1.1's front pair of lid-back feet (r 6 at x 40 / 246, d 30) land on pipes. **Move them to d 6**, under the impost line [CHECK clear]. The rear pair (d 78) is clear. Flat-open support spans d 6–78 instead of 30–78: fine.
- **No holes in the façade:** engraved / filled, or a printed relief in the first build. No acoustic or water path.
- **Wood-fill PETG engraving with brass-tone fill reads?** **UNVERIFIED** (eng / maker: a coupon).

## 5. Name
- The organ nameboard sits just above the keys. **On FOLD the strip above the keys is ≈ 3 mm tall** (sharps end y 54.6; CUTOFF's edge y 57.6, EMPHASIS's 60.55) [CALC]: too small for a cartouche.
- **Use the v1.1 blank lozenge on the lid axis** (behind TAP's lid line, 32 × 6). Standing, it sits above the console, where a nameboard reads. Leave it blank until the owner names it (director).

## 6. States
| State | What it is | Systems notes |
|---|---|---|
| **Closed** | the organ case: façade on top, ≈ 286 × 108 × **52.7** | pegs under the lid with 2.0 clear; stays flush in the lid end faces (v1.1) |
| **Carried** | a bar under the arm or in a bag, façade out | nothing proud; feet are flush rubber (≤ 0.6 proud, v1.1) |
| **Flat (180°)** | a console on the table; façade face-down on 4 feet | front feet at d 6 now |
| **Standing (120°)** | façade to the listener, console to you | v1.1 stays unchanged: tip ≈ 6.8 N. The lid speaker faces you |
| **Outdoors** | park bench / grass | slim pack ≈ 1.9–3.9 h [CALC]; status light under a hood (common §3); PETG / wood-fill PETG in sun; the friend across the bench sees the façade (J22g) |

## 7. Jobs this concept leans on (coverage comes at the 9+ check)
J20 (case and console), J21 (reverse pegs), J22 (bar carry, façade for the friend), J23–J27 (FREE / SYNC + firmware, shared), J28 (FOLD internals unchanged).

## 8. Can't verify here
Walnut button-plug supply · engraved fill on wood-fill PETG · real toggle lever height (closed clearance) · strip C vs base board line · sun readability of the hooded LED · outdoor speaker level.
