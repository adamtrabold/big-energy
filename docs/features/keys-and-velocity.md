# Keys and velocity
Status: **written 2026-11-13** (systems). Per item below. Sources:
- [owner record](../../design/owner.md);
- [velocity and keys v2](../../eng/velocity-and-keys-v2.md);
- [keys answers](../../eng/keys-answers.md);
- [Daisy design §1](../../eng/daisy-first-principles.md);
- [aftertouch §8](../../eng/aftertouch.md);
- [CATHEDRAL §10, §13, §16.5](../../design/branches/concepts/cathedral/how-it-works.md);
- [expert review](../../design/reviews/2026-11-13-audio-synth-review.md) item 5.

## What it does (player's view)
- **25 keys, two octaves C to C**, running right to the front edge. Each key goes down about 2.8 mm, silently, and lands softly.
- **How hard you strike sets the velocity**: loudness, filter, or both, chosen on the VELOCITY switch.
- In CATHEDRAL the keys are **round brass heads**: brass naturals with black sharps, or all brass.

## Owner decisions (verbatim, linked)
- Keys feel like an instrument: real travel, silent ("as silent as possible"), velocity. Velocity: "Both, with a switch" → LOUD / BOTH / FILT.
- Key edge: "A: keys at the edge".
- He doesn't want to build custom keys; keys are bought switches.
- 14:33 "I don't know how to machine — the keys need to be printed or purchasable" → **printed key tops allowed**; **no machining**.
- 14:34 "They can be printed externally too - I know you can get metal prints".
- 14:40 "what about brass and black keys? Or all brass?" · 14:41 "Premade wooden caps on a shaft that also is premade or part of the key is fine too just thinking" (an option, not a decision).
- 16:52 "i'd rather have more brass than black re: keys too".

## How it works
- **Switch:** 25 × **Kailh Choc V2 silent** (Deep Sea Mini): 2.8 ± 0.25 mm travel, actuation 1.3 mm, damped both ways, **MX cross stem** (eng v2 §2).
- **Sensing:** a **D31 magnet** (4.76 × 1.59 mm N42) in each key's carrier, over an **SS49E Hall sensor** on strip C.
  - Rest gap 5.6 mm, bottom gap 2.8 mm (≈ 154 → 573 G, linear over the travel tolerance) [ENG].
- **Scan:** 3 muxes; keys on **ADC1 + ADC2, sampled together**, timer-paced at **8–10 kHz with 4× oversampling** (DFP §1).
- **Velocity:** a least-squares slope of linearised depth against time over **15–75 % of the stroke** (0.4–2.1 mm). Per-key rest / bottom learning, a per-key field-curve table, and a supply-ratio correction.
  - Velocity error ≈ 0.35 MIDI steps at full strike (ESTIMATE).
- **Hall group power-gating** (bench-gated): ≈ −0.45 to −0.95 W.
- **Velocity routing:** the **VELOCITY toggle (LOUD / BOTH / FILT)**. The velocity CV goes to the VCA's velocity input and / or adds a step to CUTOFF.
  - Review 21: slew that step 2–5 ms (proposed).
- **Key heads (CATHEDRAL, proposed):** one **printed PETG carrier** per key (§10.2):
  - an MX cross socket on the stem;
  - the magnet pocket at the v1.1 height (so velocity is unchanged);
  - a **Ø 9.6 × 3.3 cup** that takes any head with a **9.53 × 3.2 tenon**.
  - The head choice stays swappable after the build.
- **Heads (options; lead from the owner's "more brass"):**
  - **A (lead):** cast-brass **naturals**, **black-plated cast-brass sharps**: hollow, ≈ 2.5–3 g each, from a print service.
  - **C:** all brass.
  - Also possible on the same carrier: Cherry Tree Toys 3/8" mushroom plugs (head 12.7, tenon 9.53 × 3.2: [birch](https://cherrytreetoys.com/3-8-mushroom-plugs/), [oak](https://cherrytreetoys.com/3-8-oak-mushroom-plugs/)); a one-piece printed head; a bought wood cap on a dowel.
- **Bottom stop:** a bought keyboard O-ring, or a punched felt ring on the switch top. The carrier lands on it at **≈ 2.5 of the 2.8 mm** travel, past the velocity window (which ends at 2.1).
- **Positions (FOLD base, edge A):** naturals y 13.5, x 17 + 18n; sharps y 36 at the piano positions.

## Controls and states
| Item | States | Status |
|---|---|---|
| Keys | 25, velocity, silent | decided |
| VELOCITY toggle | LOUD / BOTH / FILT | decided |
| Velocity curve | a setting (power-on: hold the top key, then keys 1–5) | proposed (gestures doc) |
| Key heads | A (brass + black-plated brass) / C (all brass) / plugs / printed | A or C open with the owner; options proposed |

## Edge cases
- **Peg clearance vs the floating key strip (review 5, a must-fix):**
  - Strip C floats on the aftertouch pressure lanes and can shift ± 0.5 mm. Aftertouch needs **≥ 1 mm clearance** round every key.
  - **Fix (proposed): deck holes Ø 13.2** round the Ø 11.2 neck (1.0 per side).
  - A **brass head of Ø 14** (cast, so any size) covers the hole. A 12.7 wood plug leaves a 0.25 mm dark ring.
  - Or a slimmer neck (≤ Ø 10.7 in a 12.7 hole; the cup's wall is then ≈ 0.55 mm, thin for FDM: UNVERIFIED).
- **Head mass:** a hollow brass head (2–3 g) is ≈ 5–8 % of the switch's 35–43 gf. That's negligible; a solid 4–5 g head would feel lighter at the top with a firmer return.
  - **All heads the same mass → one velocity calibration.** That's why the sharps are black-plated brass, not printed black.
- **Brass and the sensor:** brass isn't magnetic, so the field is unaffected. Printed 316L steel heads could be slightly magnetic (avoid near the magnet arm).
- **Wear:** bare brass darkens; plating wears through where fingers land.
- **Closed height:** head top = deck + 2.8 + head height. With H ≈ 4, closed stays at CATHEDRAL's figure (≈ 55.2 R-LOW / 59.7 R-TALL).
- **Magnet side-force:** adjacent magnets push the end keys ≈ 3.5 gf outward ([ENG]; felt guides). Irrelevant with carriers on switch stems.

## Interactions with other features
- **Aftertouch:** the floating strip sets the clearance rule; pressure is read only while a key is bottomed (Hall).
- **Paraphonic:** the keys feed MONO / PARA allocation.
- **MIDI:** notes from MIDI share the keys' note pool ([MIDI](midi.md)).
- **Enclosure:** the deck holes, the heads' closed clearance, the brass palette.
- **Power:** Hall gating is the biggest power saving.

## MIDI
- **Receive:** MIDI notes play like keys (shared pool, proposed).
- **Send:** notes are **not sent today**; "performance out" is an open free extra ([MIDI](midi.md)).

## Budget (pins / mux / DAC / power / cost)
- **Mux:** 25 channels (mux A 1–16, mux B 17–25).
- **Pins:** ADC1 / ADC2 inputs, selects shared.
- **DAC:** velocity CV (moves to the proposed 5th MCP4822; see [paraphonic](paraphonic.md)).
- **Power:** Hall sensors are the largest key load; gating saves ≈ 0.45–0.95 W.
- **Cost:** switches ≈ $0.70 each (keeb.io, eng); carriers pennies.
  - Brass heads: quote pending (cast-brass service; plating adds €5–9 per piece).
  - Plugs ≈ $3–5 per 50.

## Open questions
1. **Keys A (brass naturals, black-plated brass sharps) or C (all brass)?** (On the decisions page, item 1.)
2. **Buy-and-test T1 / T2** (plug dimensions; one brass head on one switch). (Decisions page, item 3.)

## Status (item by item)
| Item | Status |
|---|---|
| 25 velocity keys, silent, Choc V2, Hall sensing | decided (locked spec) |
| VELOCITY LOUD / BOTH / FILT | decided |
| Edge A | decided |
| Printed or bought key tops; no machining; external and metal printing OK | decided |
| More brass than black | decided (direction) |
| Printed carrier with a 9.53 × 3.2 tenon cup; O-ring / felt stop at 2.5 | proposed |
| Deck hole Ø 13.2 (≥ 1 mm clearance); brass heads Ø 14 | proposed |
| Sharps black-plated brass (one calibration) | proposed (systems) |
| Keys A vs C | open (owner) |
| Velocity cutoff slew 2–5 ms | proposed |
