# Round 2: what the concepts share (visual)

Status: rev 2, 2026-11-12, visual designer. Read with `common-how-it-works.md` (systems, rev 3). Mock sources: `_mock-src/` (`python3 render_all.py && python3 sheets.py`; `render_all.py --test` gives quick low-res renders).

## Owner rules applied to every sheet this round
- **No name.** Owner: "little D is a terrible name". The sheets read "concept mocks, round N · name to come" (HUSH, ONE SHEET and FOLD are round 3). Every name space (HYMNAL label, HUSH flap, FOLD plate) is blank or "( name )".
- **Nothing raised in the knobs' way** (owner, three messages): no raised dividers, and no separator between keys and controls. Side and rear rims are allowed. The keys sit flush with the panel.
- **Feel the sections without anything rising** (owner: "use another method of separation if you think it's important to feel the sections"). Each concept answers in its own material:

| Concept | How you feel a section break |
|---|---|
| TYPE CASE | **sunk rules**: the egg-crate walls stop 1 mm below the floor face, giving a 3 mm wide, 1 mm deep groove |
| HUSH | texture change: printed tag (smooth) against felt (soft), at every knob |
| ONE SHEET printed | 0.6 mm × 1.2 mm printed grooves at each section gap (by eye: first-layer line direction alternates per section, r3) |
| FOLD | r3: one white panel; 0.6 mm × 1.2 mm sunk printed grooves at x 41.5, 172.9, 264.5, and the hairline joint at 121 (the five-plate V-grooves are now only the inset alternative) |
| HYMNAL | not tactile (flat birch, red numerals); it could take TYPE CASE's grooves if the owner wants them |
| UNDER GLASS | not tactile (one smooth glass sheet): the set's weakest on J16, said plainly |

- **Printed enclosures welcome; printed knobs and keys not.** Every printed split falls at **x = 121**, the II|III gap (the oscillators | everything that mixes and shapes them). It runs as one straight line through every part: top, walls, bottom, and FOLD's lid and plates.

## Heights (eng `little-d-design-answers.md`, E-L2)
- The 50 mm Same Sky CDS-5076 speaker (7.6 mm deep) gives a panel top of 22.7–24.2. **I drew the panel at 24 everywhere** (UNDER GLASS glass top 24), with the keys at 24 (strip C lifted, R4) and sharps at +2. **Knob tops are ≈ 35, CUTOFF 36.65.** That is 3 mm thinner than round 1, and the deck is truly flush.
- Systems' docs still say panel 26–27. That is the old figure, before eng's answer. **Systems, please confirm 24.**
- FOLD has its own numbers (systems rev 2): keys 17.5, panel 16.5 when open, hinge axis 25.5, closed 51. **Visual r3:** FOLD's panel content sits 12 mm toward the lid's far edge (front-row centres 41 mm from the hinge edge, not 29), so closed every knob lands over whites or the palm rest, never the sharps. Systems to confirm.

## Panel layout (visual proposal, round 2; systems please adopt or answer)
R2 (director) holds: pitch ≥ 20 mm, IV's played row wider. My layout puts the air where the hand needs it:
- **7 mm from any knob to a section break, 3 mm on a toggle's side.** With systems' 9.5 mm symmetric gaps, a knob edge sat 3.3 mm from a wall.
- **IV's columns align across the three rows**: CUTOFF/ATTACK/ATTACK in one column, and so on.
- **CUTOFF → EMPHASIS is 25 mm** (7.2 mm gap for the 20.8 mm hero); EMPHASIS → AMOUNT is 24 mm.

| | x |
|---|---|
| I | TUNE / GLIDE / MOD MIX 18 · OSC MOD, FILTER MOD toggles 34 |
| break | 41.5 |
| II | RANGE 57.5 · FREQ 77.5 · WAVE 97.5 · OSC 3 CTRL toggle 113.5 |
| break (print split) | **121** |
| III | OSC 1–3 at 137 · NOISE/EXT knob and SOURCE toggle at 157 |
| break | 172.9 |
| IV | **CUTOFF (192, 104)**, ATTACK ×2 at 192 · EMPHASIS, DECAY ×2 at 217 · AMOUNT, SUSTAIN ×2 at 241 · KBD CTRL, VELOCITY, DECAY toggles at 257 |
| break | 264.5 |
| V | VOLUME (280.5, 104) · STATUS (280.5, 127) |
| "not in control" light | (205.5, 93), in the CUTOFF/EMPHASIS gap |

- Rows: y 104 / 127 / 150. Reach from stick to CUTOFF ≈ 196 mm. Source: `_mock-src/ld.py`.
- **UNDER GLASS:** the front-row knobs over a window have their labels in a strip at y 76.6, just in front of the window, so no label sits on the glass over the parts. Its speaker moves to (150, 150), ≥ 30 mm from both windows' parts (eng E-L4). The others keep the speaker at (170, 128).

## Knob colours (round 3, director R5: each follows from its concept's idea; repeats are fine)
KN1250 family plus the cream Tayda 1083 for CUTOFF (the one hero in every concept), except FOLD.

| Concept | Knobs | Why |
|---|---|---|
| TYPE CASE | **red** | letterpress is black and red (ink floors) |
| HYMNAL | **white** | a neutral, modern panel; the box carries the warmth |
| HUSH | **cream** (r3; was yellow) | "nothing shouts": grey wool, natural maple, cream knobs. CUTOFF is told apart by size and its red line |
| ONE SHEET printed | **cream** | matched to the one filament |
| FOLD | **black** (r3; was blue) on the white panel, **white KN1250 MOD** on the dark base | "knobs take the other half's colour"; also the look he remembered (walnut, white panel, black knobs). No black KN1250 exists: the Tayda plastic black knob, 6 mm × 18T split shaft, ≈ 14.5 × 13.5 mm, white indicator, fits only because FOLD's panel moved 12 mm (it clears the whites by 3.0 mm closed). It raises FOLD's closed floor from ≈ 44 to ≈ 47 |
| UNDER GLASS | killed (round 2) | — |

## Sheets (all six concepts)
- **A — the look:** a 3/4 view, the carry state, the principles (each with its "because"), cost, build, thickness, owner's hand, keys and bag. The insets have their own strip under the render: the HYMNAL piano variant, the HUSH wear plan, the ONE SHEET toolpath swatches (r3), and FOLD's open/closed side view with the five-plate alternative (r3).
- **B — real size:** an orthographic top view rendered from the same model, placed at 1:1 by two marker cubes. TYPE CASE's B sheet carries the worst-knob thumb check at 1:1 and 2:1.
- **C — key-edge section:** a fit check per H3′, at 1.6:1 (FOLD at 1.25:1).
- 300 dpi A3. Every PNG was opened and checked.
