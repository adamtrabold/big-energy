# Enclosure (CATHEDRAL)
Status: per item below · last updated 2026-11-13 · sources: [owner.md](../../design/owner.md), [cathedral how-it-works](../../design/branches/concepts/cathedral/how-it-works.md) (team rulings, §1–§18), [cathedral how-it-looks-and-feels](../../design/branches/concepts/cathedral/how-it-looks-and-feels.md), [decisions page](../../design/decisions-open.md)

CATHEDRAL is FOLD's two-half body (v1.1) with CHAMBER's ideas, renamed and reshaped by the owner (14:12). The panel itself (every control, word and position) is in [cathedral §17–18](../../design/branches/concepts/cathedral/how-it-works.md). This page is the body.

## What it does (player's view)
- **A closed book** about **286 mm wide, 108 mm deep, ≈ 55 mm thick** (≈ 60 mm if you keep the bigger played-row knobs). It folds shut over its own knobs and keys.
- **Three ways to play:**
  - **open flat**, the lid lying behind the base;
  - **standing**, the lid propped at **120°** on two brass stays that fold away into its ends;
  - **closed** for the bag.
- **The base** holds the keys (25 brass and black pegs), the played row (bend, mod, cutoff, tap…), the battery and the Daisy. **The lid** holds the oscillators, mixer, envelopes and effects, and the round speaker window.
- **A walnut-toned body** with a cream face plate in each half, like a guitar body with a pickguard; every corner rounded; fine line "woody" texture; brass details. "big energy" on a small plate under the speaker.
- **No screws on show:** the case screws on the back are the rubber feet.

## Owner decisions (verbatim, linked to owner.md)
- "i want to lock in on cathedral and fold right now. what are the differences between them so i can find the best middle ground" → focus CHAMBER + FOLD v1.1; **the point of view is CATHEDRAL**.
- "I also liked the rounded edges of the original fold with flat top and bottom. I imagine the housing being a hollowed out block that the face plate with filters and keyed get installed in, sort of like a guitar with pickguard" → **hollowed block + face plate** construction; each half a **unibody**; screws from the back ideal, not mandatory.
- 3D-printed enclosures welcome (2026-11-12); "I don't know how to machine — the keys need to be printed or purchasable"; "They can be printed externally too - I know you can get metal prints" → **no machining anywhere**; printed or bought parts, metal prints allowed.
- "On fold, we should build some sort of method for the top case to stand up … should fit the design language of the device" → one fixed standing angle; "i think the fold's angle should be a bit less steep" → **120°**.
- "I don't want a spine" → **no spine**.
- Hinges: "is there any way we could do a more hidden hinge or hidden hinges in the gap? if not these are fine."
- "i also wonder if the protective feet couldn't be [one with the case screws]" → feet = screws.
- "Engraving texture I meant fine line texture — I'll probably do a design for the pipe lines" → he designs the pipe lines; the texture stays fine and woody.
- "the filter sections should not be raised"; "That includes the separator between keys and controls too" → **nothing raised** on the playing faces.
- "i'd rather have more brass than black re: keys" → brass naturals (lead) or all brass.

## How it works
- **Two halves, each a printed unibody shell** (PETG, walnut-tone / wood-fill) with a cream face plate inset. Boards, pots and keys install from behind; a back panel closes each half.
  - Plate inner edge x 4.3–281.7; **all 8 plate corners R 7.7**, concentric with the block's R 12 corners and 4.3 wall (team ruling 1; §4).
  - Base plate at z 15.6.
- **Hinge: hidden pins in the side walls** (§1).
  - Each rear corner has a leaf pair inside the wall (printed 316L, out of sight; team ruling 4) on a bought Ø 3 pin. The outside hole is capped.
  - No knuckles show. Closed, a ≈ 4 mm round ear stands past the back at each rear corner (the smallest that holds a Ø 3 pin; look doc). Stated to the owner as a small cost.
  - Fallback: the v1.1 knuckles ("if not these are fine").
  - The axis sits halfway up the closed hollow, so the halves can close over knobs on both sides. A hinge hidden in the seam would land the lid on the base's knobs (§1).
- **Stand:** two stays pivot at lid d 30 and stow in grooves in the lid's end faces (d 30–74.4).
  - **Cast brass** from the keys' service (lost-wax, from a printed pattern); fallback matte-black PETG 5 × 8. Never grey steel in view (team ruling 3).
  - Standing tip threshold **≈ 8.4 N**, up from ≈ 6.9 N, now the battery sits in the base (§16.2).
- **Feet = screws:** screw-through rubber feet at the **4 corner screws** (x 16 / 270, d 12 / 96), black; the 2 axis screws (x 143) stay flush brass (team ruling 2; §3). Both halves' feet are the same height, so the open instrument sits level.
- **Speaker window:** one round opening on the axis, **Ø 46**, with 15 vertical slots 1.8 wide at 3.0 pitch (≈ 945 mm², ≈ 75 % of the cone). Plate 2.5, foam gasket, sealed stuffed back box ≈ 20–25 cm³ (corner chamfered for the echo pan's pot) (§16.4, §17.6).
- **Keys:** 25 Kailh Choc V2 silent switches with Hall sensing.
  - Each head sits on a printed carrier through a **Ø 9.6 × 3.3 cup for a 9.53 × 3.2 tenon**, one interface for every head (team ruling 5; §10.2).
  - **Lead A:** cast-brass naturals with black-plated brass sharps (one velocity calibration). **Alternate C:** all brass (§13, §16.5).
  - Deck holes Ø 13.2 so the floating aftertouch strip never rubs ([keys and velocity](keys-and-velocity.md)).
- **Inside:**
  - battery in the **base's rear strip** (4 cells, [power and battery](power-and-battery.md)), beside the Daisy (rear right);
  - the lid's I/O board on its far wall (x 60–230);
  - USB-C and the MIDI jacks on the base's right end face ([io](io.md));
  - one ribbon crosses the seam at x 176–227, away from the hinge corners.
- **Closing height:** **≈ 55.2 mm (R-LOW)** with Tayda Ø 10 × 8 played-row knobs on snap-in or counterbored pots. Since steer 4 the bend stick needs no lowering (§18.3). **≈ 59.7 (R-TALL)** keeps today's knobs. Binding pair: the filter envelope's attack over blend (§18.3).

## Controls and states
| State | Geometry | Notes |
|---|---|---|
| Closed | 286 × 108 per half, ≈ 55.2 (R-LOW) / 59.7 (R-TALL) thick | back opening 22 × 266 shows dark (owner question 2) |
| Open flat | lid behind the base, both feet sets on the table | reads top → bottom as the lid's signal order, then the base |
| Standing | lid at 120° on the brass stays | stays stow flush in the lid's end faces |

## Edge cases
- **The back opening when closed:** with no spine, a 22 × 266 mm slot along the back shows the knob tops inside and can let grit in (job J6 drops to partial). The team recommends leaving it open, with the inside finished dark (owner question 2).
- **Lid bats when closed:** three lid switches close over base knobs; they must stand ≤ 13.5 mm proud or the R-LOW height grows to ≈ 56.7 (§18.4).
- **Side-pivot strength:** printed-wall bosses carry the lid and stand loads. UNVERIFIED: one test print (§1).
- **Key head height:** the plug's head height isn't published. Buy-and-test T1 measures it, and it sets the key height and closed height (team rulings, T1).

## Interactions with other features
- **Power and battery:** the cells set the base's rear strip and the stand's tip force ([power and battery](power-and-battery.md)).
- **I/O:** jack positions on the base end face and the lid far wall ([io](io.md)).
- **Keys and velocity / aftertouch:** the deck, carriers and the floating strip ([keys and velocity](keys-and-velocity.md), [aftertouch](aftertouch.md)).
- **Panning and stereo outputs:** one speaker, mono sum ([panning and stereo outputs](panning-and-stereo-outputs.md)).
- **The panel:** layout, words and the checker: [cathedral §17–18](../../design/branches/concepts/cathedral/how-it-works.md).

## MIDI
- None.

## Budget (pins / mux / DAC / power / cost)
- **Pins / mux / DAC:** none, beyond what's on the panel.
- **Cost (rough, ESTIMATE):**
  - printed shells and plates at the makerspace (material);
  - stays in cast brass (or PETG);
  - 316L hinge leaves from JLC3DP ("From $5.0", checked); Ø 3 pins;
  - 4 screw-through feet (part UNVERIFIED);
  - back box, gasket, felt.
  - Exact figures are in eng's cost estimate.

## Open questions
1. **Approve CATHEDRAL, or send it back** (owner question 1, scored 10 by the director).
2. **The back opening:** leave it open and dark (team recommends), or deal with it later (owner question 2).
3. **Buy-and-test T1 / T2:** the plug's head height and one cast-brass head on a switch (owner question 3).
4. **Side-pivot strength:** one test print (eng / maker).
5. **Screw-through feet:** pick the exact part (eng).

## Status (decided / proposed / open, item by item)
| Item | Status |
|---|---|
| CATHEDRAL as the point of view; FOLD two-half body | decided (focus); approval open (question 1) |
| Hollowed block + face plate, unibody halves, no machining, printed / bought / metal-printed parts | decided |
| One fixed standing angle, 120° | decided |
| No spine | decided |
| Feet = case screws | proposed (from his question; team ruling 2) |
| Hidden side-pivot hinge, 4 mm ear | proposed (his "if not these are fine" keeps knuckles as fallback) |
| Cast-brass stays; 316L hidden leaves; R 7.7 corners | proposed (director rulings) |
| Round Ø 46 speaker window, sealed box | proposed |
| Brass naturals + black-plated brass sharps (lead) / all brass | proposed (his "more brass") |
| Closed ≈ 55.2 (R-LOW) / 59.7 (R-TALL) | proposed; the route is his choice |
| Back opening; T1 / T2 results; pivot strength; feet part | open |
