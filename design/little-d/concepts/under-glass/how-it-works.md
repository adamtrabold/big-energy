# UNDER GLASS: how it works (systems)

Kind: **an exposure**. Pole: middle (designed for use, with character). Body: **sleeve-carried** (owner: "Show me both"). Replaces ONE SHEET (`../../scores.md`). Read with `../common-how-it-works.md` and `../../jobs.md`.

## The idea
A pinball machine puts its mechanism under glass, and its art is painted on the back of that glass, so play never wears it off. Little D is the owner's first build and the proof of the whole project, on a **standard printed board** (owner: mask + silkscreen). So: **the board is the playfield, and a clear acrylic sheet is the glass over it, reverse-painted by the owner, with clear windows left over the parts of the circuit that are the instrument's reason to exist.**

## Design principles (each follows from the idea)
1. **Show the proof, frame it.** The glass is painted opaque except for windows over the VCO cores (the three AS3046 expo arrays + tempcos) and the ladder filter's matched pairs. *Because* a playfield shows what's in play, not the wiring underneath; these are the parts that make it a Model D-style voice and the parts the owner hand-matched.
2. **The art is under the glass.** All paint and legends are on the underside, viewed through 3 mm of clear acrylic. *Because* that's how backglass and playfield art survives hands; the top is one clean gloss sheet that can be buffed if scratched, and the paint can't wear.
3. **The machine marks the exact, the hand paints the meant, in that order.** Legends and scales are laser-engraved **mirrored into the underside** and back-filled first; the owner then paints the colour fields over them; windows stay clear. *Because* reverse painting goes on last-detail-first; H6 becomes the painting order itself.
4. **Rails, not cheeks.** Bought aluminium U-channel along the front and back carries the structure and is where hands rest. *Because* a pinball's lockdown bar and side rails are the hand's place; and rails along the length avoid the Model D's end cheeks (H1).
5. **Light comes from below.** The status light and the "not in control" light are LEDs on the board, seen through small unpainted dots in the paint. *Because* under glass, nothing pierces the glass that doesn't have to; the light is part of the playfield.

## Structure

**Plan:** common layout, 298 × 180. **White KN1250 knobs** (visual: no black KN1250 exists; a black option needs a second knob family); cream CUTOFF hero.

| Part | Size / position | Material |
|---|---|---|
| **Glass** | 292 × 125, y 52–177, x 3–295 | 3 mm **clear cast acrylic**, underside engraved + back-filled + reverse-painted |
| **Rear rail** | 298 long, at y 177–180 + flanges | aluminium U-channel **1 in × 1/2 in × 1/16 in** (25.4 tall, opening inward), capping the glass and bottom edges |
| **Front rail** | 298 long, at y 0–3 | aluminium U-channel **1/2 × 1/2 in**, capping the bottom's front edge; top at z ≈ 12.7, **below the keys (≈ 22)**: a front guard, not a fallboard |
| **End plates** | left and right, profile = the body's side section | 3 mm acrylic (same sheet as the glass, painted or smoked) |
| **Bottom** | 298 × 180 | 3 mm acrylic or ply (black), speaker grille, feet 6 mm, keyhole slot |
| **Stick plate** | stick column, at key level | black Delrin gate plate (the gate *is* the plate) |
| **Board** | main 280 × 100 (standard printed, black mask suggested), strip C under keys | — |

**The windows (board layout constraint, eng E-L4):** in the band between the key edge and the front row of knobs (y ≈ 80–96, 16 mm tall), the playfield has its two windows:
- **VCO window** over x ≈ 60–122: the three AS3046 DIP-14 (≈ 19 × 7.6 mm each) laid in a row with their tempcos. Three chips in a row = the three oscillators, visible.
- **Ladder window** over x ≈ 180–254: the matched transistor pairs and film caps of the ladder.
- **Eng must place these parts in that band** on the main board (front edge y 77–96). If the layout can't, windows move to wherever the parts land, and the frame follows the circuit (principle 1 says so).

**Key edge (H3′): the glass edge.** The glass's front edge at y ≈ 52, z ≈ 25, overhangs the back of the switch housings and strip C; polished edge, the glass's thickness visible as a line of light. It's the one place the glass meets the keys.

**Section (fit check):**

| y | Part | z top |
|---|---|---|
| 0–3 | front rail (1/2 in channel) | 12.7 |
| 5–52 | keys (whites ≈ 22, sharps ≈ 24: strip C lifted, R4) | 22–24 |
| 52–177 | **glass** on the pot bushings, clamped by pot nuts + 4 standoffs to the board | **≈ 24** (the glass sits inside the rear rail's upper flange: 25.4 − 1.6 flange) |
| board | top at ≈ 14 (24 − 3 glass − 7 pot body) | 14 |
| under board | ≈ 8–9 mm (3 bottom + lead tails ≈ 1.5 → ≈ 8) for battery (≈ 7 thick) and speaker | — |
| knobs | | **≈ 35** |
| rear rail | | 25.4 |

**Thickness:** body ≈ 25.4 (the rear rail sets it), knob tops ≈ 35. **The thinnest of the set** and inside R3 with margin.
**The cost of thin:** only ≈ 8 mm under the board. **The speaker must be ≤ ≈ 8 mm deep or sit in a board cutout** (E-L2 decides). If E-L2 says ≈ 12+ mm: **1-1/4 in channel** (31.75 tall) → body 32, knob tops ≈ 41.5: **over 40**. Then the fix is a board cutout for the speaker (or a 1-1/8 in rail if one is stocked), not a taller rail.

**Pots and toggles:** PCB-mounted [ENG], shafts and levers up through laser-cut holes in the glass; the glass rests on the pot bushings' shoulders, the pot nuts clamp it. Holes engraved with their scales on the underside around them.

**Jacks:** **right end plate** (laser-cut holes in acrylic; no drilling aluminium): 7–8 ports at 12 mm in y 60–170 of the end plate's control-zone part. Power switch recessed in the same plate. Cables leave to the right, away from the stick.

**Status light:** an LED on the board in V, through an unpainted dot. **"Not in control" light:** LED by CUTOFF through a dot (≈ (200, 92)).

**Speaker:** 50 mm thin CDS-5076 (eng E-L2) at **(150, 150)** (visual; ≥ 30 mm from both windows' parts, eng E-L4), behind a laser-cut grille in the bottom sheet, feet 6 mm; ≈ 54 mm lead-free keep-out on the board underside (eng: 1.8 mm spare under the 1 in rail; no board cutout, no taller rail).

## States
| State | Form |
|---|---|
| Carry | in a sleeve (a 13 in laptop sleeve fits 298 × 180 × 36, ESTIMATE $10–15, or the owner's own) |
| Play | as is; the glass reads as one dark gloss field with two lit windows onto the circuit |
| Glass scratched | top face: buff with plastic polish; paint underneath is untouched |
| Wall (J18) | keyhole slot in the bottom; on a wall it reads as a framed playfield |

## Flows that differ from common
- **F1:** slide out of the sleeve → power (right end) → play.
- **F5 Pack:** power off → sleeve.
- **F9 Build:** laser-cut the glass (holes, outline) → **engrave mirrored legends into the underside** → back-fill (white or cream paint, wipe flush) → owner paints colour fields on the underside, masking the windows and LED dots → mount the glass on the soldered board → slide the glass-and-board assembly between the rails → end plates → bottom.
- **F10 Service:** bottom off; the board and glass come out together as one unit (glass is held by pot nuts to the board). BOOTSEL through a hole in the bottom.
- **F11 Label:** machine: engraved + back-filled legends, scales, MIDI dots. Hand: everything painted; windows left clear.

## Six axes
1 Layout: signal sentence, front band of windows. 2 Material: clear acrylic glass + aluminium rails + acrylic ends. 3 Posture: flat, thinnest. 4 Protection: sleeve. 5 Speaker: bottom. 6 Labels: engraved-and-filled under the glass, reverse-painted by hand.

## Cost and build (ESTIMATE)
- One 12 × 24 in sheet of 3 mm clear cast acrylic: glass (292 × 125) + bottom (298 × 180) + end plates fit [CALC: 125 + 180 + 2 × 26 strips ≈ 360 mm of 610] ≈ **$15–22**.
- Aluminium U-channel, 1 in and 1/2 in, ≈ 300 mm each from hardware-store lengths ≈ **$8–15**.
- Paint (owner's or ≈ $5), screws, standoffs ≈ $3.
- **≈ $26–45. Over the $20 target.** Cheaper: bottom from ply scrap (−$0–5; the sheet still covers the glass), aluminium angle instead of channel (−$3–5, ESTIMATE), owner's paint. **Lean ≈ $20–30.** H5 named saving: scrap acrylic key tops (−$12, eng v2 §2.5).
- Build: cutting + engraving ≈ 45 min; back-fill + reverse painting ≈ 2–4 h (the owner's part, by choice); assembly ≈ 1 h.

## Coverage against jobs.md (first pass)
J1 ✓ · J2 ✓ · J3 ✓ · J4 panel ✓; patch chart = separate card (no built-in place; inferred job, says so) · J5 bottom speaker (lap risk, as all) · **J6 sleeve only** (by design; owner asked to see a sleeve concept) · J7 ✓ · J8 ✓ (lights through the glass) · J9 right end ✓ · J10 ✓ · J11 ✓ (standard board, acrylic, rails) · J12 five principles ✓ · J13 reverse painting ✓ (the most hand of the set) · J14 ✓ · J15 ✓ (thin; rails as grips) · **J16 glass is uniformly smooth: weakest blind-find** (the knobs and toggles themselves are the only tactile marks) · J17 n/a (keys are bought switches now) · J18 ✓.

## R4 check
One flat glass sheet, windows and legends under it: nothing among the knobs ✓. Keys ≈ 22–24, glass ≈ 24, the polished glass edge is the key edge, within ≈ 2 mm: no separator ✓. Not yet shown to the owner.

## Assumptions and open questions
- **E-L2 (eng): speaker depth** decides the rail size (thinnest at 1 in channel needs a ≤ 9 mm speaker or a board cutout).
- **E-L4 (eng): place the three AS3046 + tempcos and the ladder pairs in the front band** (y ≈ 80–96) of the main board under the windows.
- **Q-UG1 (owner):** board mask colour (black suggested) and a cost check that "standard printed" at qty 1 is in eng's quote.
- **Q-UG2 (visual):** do engraved-and-filled legends read through 3 mm acrylic in the 3/4 (parallax ≈ 3 mm)? Small type (1.9 mm) may blur at angle; maybe 2.2 mm.
