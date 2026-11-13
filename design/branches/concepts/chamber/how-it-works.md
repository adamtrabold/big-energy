# CHAMBER: how it works (systems)

Seed: **FOLD-105** (v1.1). Kind: an instrument case. Point of view (director, turn 3): **closed it's an organ case; open it's a console.** Emotion: joy. Read with `../common-how-it-works.md`, `versions/v1.1/fold/how-it-works.md` (rev 5.7) and `design/jobs.md` rev 5.

**Rev 2, 2026-11-13 (round 1 scored 8; director's fixes).** Supersedes rev 1 where they differ. Numbers marked [CHECK] are from `../branch_check.py` §7, §8a and §8b.

> ### R2.1 The hinge-side slot is real, and a spine closes it [CHECK §8a]
> - **Real, by design since v1.1** (`fold/how-it-works.md`, "Closed from the back"). The lid has no wall on its hinge edge, because open, a wall there would stand between the PLAY row and V1. That breaks the owner's "nothing raised among the knobs" (R4).
>   - In CHAMBER the slot grows with the lid walls: **21.9 mm tall × 266 wide** (x 10–276, between the knuckles). Closed: base plate z 15.6, lid plate z 37.5. The rims land on the base plate at z 15.5, because the hinge axis rises 1.3 to z 26.3, as rb.py already has.
> - **A rigid spine wall or lid lip can't work.** Fixed, it stands 22 mm above the plates when open. Folded flat, it lies on the plate. Either way it breaks R4.
> - **Fix: a flexible spine, the way a book closes** (FOLD already "folds like a book").
>   - A strip of bookcloth or thin leather on a 0.8 mm TPU core, **21.9 mm wide, x 10.5–275.5**.
>   - Glued along the base's rear-top edge (y 108, z 15.6) and the lid's hinge-top edge (open y 110, z 15.1).
>   - **Closed:** the two edges are 21.9 apart, so the spine is taut and closes the back. It becomes the organ case's back panel; colour is the visual designer's call.
>   - **Open flat:** the edges are 2.1 apart, so the spine folds down into the 2.0 mm seam gap as a loop ≈ 9.9 deep (to z ≈ 5.7). **Nothing above the plates: R4 holds.**
>   - **Standing (120°):** 12.7 apart, so ≈ 9 mm of slack shows as a soft drape in the opened gap behind the PLAY row, like a book's joint.
> - **Eng / maker:**
>   - the hinge ribbon's rolling loop shares that gap at x 176–227. Route the loop inboard of the spine; v1.1's TPU flap over the ribbon becomes part of the spine;
>   - a doubled 0.8 mm TPU loop in a 2.0 mm gap is tight;
>   - flex life of a TPU or leather spine is **UNVERIFIED** (bookbinding precedent only).
> - Cost ≈ $2–5 (ESTIMATE).
>
> ### R2.2 Push-out holes [CHECK §8b]
> - **The visual designer's d 90 clears the d 96 screws** (27.8 mm from the nearest), the pipes and the feet. **But inside the lid it lands in the wrong place.**
>   - The pin passes the lid back and meets the main board's underside behind the **ECHO TYPE / REVERB TYPE rotary switches' solder tails** (centres d 83.85; body ≥ 16 mm, ESTIMATE, so tails to d ≈ 92).
>   - It also lands 1 mm from the far-wall I/O board (d 92–104).
>   - Pushing on solder tails: **rejected.**
> - **Why v1.1 put them at (110 / 176, d 54):** that's the bare board bridges between the cell and speaker windows (x 103–113, 173–183, in the band d 21.9–59.45). CHAMBER's pipes sit there now.
> - **Proposal: the push-outs become the mouths of two pipes.**
>   - Façade pitch **10 → 8.75**, so pipes 7 and 8 stand at **x 108 / 178**, on the bridges.
>   - Their mouths (d 27–29.6) become **real Ø 4 holes at (108, d 28.3) and (178, d 28.3)**.
>   - Checked: screws 33.9 clear, feet 63.6, on the bare bridges, ≥ 5 mm past the V1 toggle bodies (ESTIMATE, d ≤ 21).
>   - New field at pitch 8.75: x 34.8–251.2, 2.35 between pipes. Feet and screws still clear [CHECK].
>   - Two pipes really speak with a mouth, and the decoration does a job. **Visual: redraw at pitch 8.75.**
>
> ### R2.3 Legends and ticks, measured on the render model in Kalam [CHECK §7]
> - **Kalam Bold is now installed** (`~/.local/share/fonts/kalam/`, OFL, from the google/fonts repo on raw.githubusercontent.com). The checker measures the final font, not the stand-in.
>   - With the stand-in (DkgHandwriting), CHAMBER showed 53 hits. **In Kalam: no overlaps, 17 near-misses under the rules, 9 of them already in locked v1.1.**
>   - **Visual: re-render with Kalam now.**
> - **New in CHAMBER, and the geometry fix for each:**
>
>   | Hit | Measured | Fix |
>   |---|---|---|
>   | "free" ↔ OSC 2 knob | 1.42 (rule 1.5) | set "free" / "sync" **0.5 behind** the toggle centre → 1.92 / 1.88; toggle gap stays 1.6 |
>   | "sync" ↔ NOISE/EXT knob | 1.38 | as above |
>   | OSC 2's +50° tick / NOISE/EXT's −50° tick ↔ FREE/SYNC nut | **0.29** (rule 0.5) | **drop these two ticks too** (OSC 2 keeps −150 −100 −50 100 150; NOISE keeps −150 −100 50 100 150) |
>   | "range" ↔ "lo" / "2'" (RANGE 1 and 3 feet) | 1.18 / 1.29 (rule 1.5) | put "lo" / "2'" at ±152° r 10.8, or "range" 0.4 lower |
>   | "velocity" ↔ VEL nut | 1.34 | its above-legend at 7.7 from centre (was 7.4) |
>   | "spring" ↔ "shimmer" (REVERB TYPE fan) | 1.36 | outer fan row 6.5 → 6.8 (both fans) |
> - **Inherited from v1.1, also in the locked model (low priority, reported):**
>   - "clean" ↔ "ping-pong" 1.20;
>   - fan names ↔ their detent ticks 0.70–0.89;
>   - ±100° ticks ↔ OSC MOD / FILTER MOD / OSC 3 CTL nuts 0.40;
>   - "status" ↔ its LED 1.25.
> - **Render note:** `ld.toggle` draws every toggle nut Ø 6. The spec's nut is ≈ 9.2 across corners, and the checker uses that. So ticks that look clear in the render sit under the real nut. Real-size nuts would make the 3/4s honest.
> - **PARA "mono / para / +4"** above its toggle: **passes** in Kalam. Accepted, as the owner and director did.
>
> ### R2.4 Unchanged from rev 1
> Pegs and closed height (+2.6 → ≈ 52.7); the feet at d 6; the lozenge for the name; the states table. The **fallback colouring (maple naturals, walnut sharps)** is geometry-identical: only the bought plugs swap.

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
