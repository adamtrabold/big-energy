# HUSH: how it looks and feels (visual, round 5)

Kind: **a material**. Pole: sauce. Body: **a printed pebble shell with one wool-felt skin; unibody, shut from below.** Read with `how-it-works.md` (rev 7.1) and `../common-how-it-works.md` (rev 7.1). Layout from systems' round-5 final + DRIFT (`../_mock-src/fold_r5_check.py`, HUSH x = FOLD x + 2; `flat_r5_check.py` 0 violations).

Mocks (300 dpi A3, tag "round 5"):
- `mock-A-look.png`: 3/4 view (edge A), close-ups of edge A and edge B, principles, the underside inset, facts;
- `mock-B-real-size.png`: 290 × 186 at 1:1 (edge A);
- `mock-C-construction.png`: a section with all four rows, the underside, the build order, a 3:1 detail of TAP;
- `mock-D-front.png` (NEW): front elevations at 1:1 for edge A and edge B, right-end profiles for A and B at 1:1, and the key edge and press at 1.45:1 (A at rest / pressed, B at rest / pressed).

Sources: `../_mock-src/r5.py` (geometry, renders, orthographic elevations) and `../_mock-src/sheets_r5.py` (sheets). Round-4 sheets were overwritten; the round-4 code (`r4.py`, `sheets_r4.py`) is untouched.

## What the owner asked for, and where it shows
| Owner (round 5) | On the sheets |
|---|---|
| "keys somewhat raised so you can feel them … I may want them at the edge" / "Show me both" | Edge **A**: front round-over tightened r 12 → r 4, pegs 6 forward (whites y 13.5, sharps y 36), 7 mm of felt in front of the heads. Edge **B**: the round-4 r 12 brow, pegs at y 19.5. Both on A (close-ups) and D (1:1 elevations + profiles + mechanism). Pegs stand 6.5 above the felt by mechanism, so they can be felt either way. |
| "draw the mechanism" | D, bottom row: switch on strip C, acrylic arm carrying the peg over the stem and the magnet over the Hall sensor, 2.5 mm straight down onto the felt collar. Caption says plainly: a button with a peg on it, not a pivoting key. |
| "front views of all of these" | D. |
| echo + reverb, digital, several types, full 8 | PLAY right: REPEATS, ECHO MIX, REVERB MIX, TAP. Back row: DRIFT, ECHO TYPE, ECHO TIME, REVERB DECAY, REVERB TYPE, VOLUME. |
| "drift … controllable" | DRIFT is the first knob of the back row (source), mirrored by VOLUME (out). |

## The idea
The material that makes it quiet is the whole outside: one seamless skin of grey wool felt blocked over a soft printed pebble, maple pegs rising through it, and every screw underneath.

## Principles
1. **One skin, no edges.** *Because* a soft object has nothing to catch or pick at. The shell is rounded so a wool hood can be blocked over it, and the felt ends only underneath.
2. **The skin is a working part.** *Because* if felt makes it quiet, the felt you see must work: each peg lands on its own punched collar, the silent stop.
3. **Nothing hard touches the hand except what plays.** *Because* pegs, knobs, stick and TAP are hard; everything else is wool. **New: TAP is a maple peg on its own felt collar,** because it's tapped like a key, so it is one. It ends the PLAY row next to the keys.
4. **Nothing shouts; even the words are pressed.** *Because* names, rules and the jack legend are blind-pressed with a hot brass die; the fine scales and the type names live on printed tags.
5. **Shut from below.** *Because* the top carries only what you play; binding ring and back panel screw on underneath.

Random draw this round (real RNG): "Look closely at the most embarrassing details and amplify them" + architecture (plinths). The awkward detail was that pegs can't be "2–3 mm proud": they're 6.5 by mechanism. So I leaned into the peg as the instrument's tactile signature and put one more among the controls (TAP). The plinth: I first drew a pressed outline round the back row as the voice's base course, then burned it. It crossed MIXER, and the back row's own rules already define the row. "Nothing shouts" won.

## Look
- **Felt:** mid-grey undyed wool, one piece; the collars a shade darker. Pressed marks read darker (the compressed fibre catches shadow).
  - Rules (1 mm, pressed): x 103.5 / 186.5 from y 56 to 133.5 (PLAY + VOICE columns); y 85.4 across the full flat (x 14–276); the back row's own breaks at x 96 / 145 / 194, y 138.5–155.5.
  - Section names (Inter Bold 2.6, pressed): PITCH, FILTER, FX & OUT at y 80.4 (left-aligned 4 mm inside each column); OSCILLATORS (left, x 16) and CONTOURS (right, x 274) at y 136.5; MIXER (2.0) centred at x 145, y 134.6, in the clear 2 mm strip between the V2 tags and the back-row tags. The back-row rules start at y 138.5, so MIXER sits clear of the centre rule.
- **Tags:** light warm grey (#d8d3c9) print, flush in the felt, under every knob, toggle and TYPE switch. Knob tag r 9.6, hero r 12.4. **TYPE tags grow a bib** behind the knob (hull of r 4 at y + 4 and two r 2.8 ends at x ± 12.6, y + 12.2) carrying the four names in Inter Bold 1.05 caps, each over its detent. The detents fan over the top at −60 / −20 / +20 / +60°; the names sit at x = ± 11.85 · sin(angle), the inner two at y + r + 3.4 and the outer two at y + r + 5.6, staggered so they never touch. Echo: TAPE, BBD, CLEAN, PING-PONG. Reverb: PLATE, HALL, SPRING, SHIMMER.
- **Pegs:** pale maple whites, a darker cut for sharps; TAP is a pale peg (same as the whites) on a 17 mm collar.
- **Knobs:** cream KN1250 (DRIFT and VOLUME included); cream 1083 CUTOFF with a red line.
- **Rear band:** pressed jack legend over the rear-wall ports and a blank name line.

## AFTERTOUCH toggle (owner, new; placement is mine, pending systems)
- A third toggle in VELOCITY's column, at (178.75, 111.5): FILTER MOD (y 100) / **AFTERTOUCH** (y 111.5) / VELOCITY (y 123). It answers "next to the velocity toggle": the two key-response switches stack.
- Checked with the checker's rules: 2.30 to FILTER MOD (≥ 1.5), 3.15 to the break (≥ 3). **Cost: mirror symmetry**, since the matching slot left of the mixer is empty. Systems to accept it or re-place it.
- Labels: AFTERTOUCH in 1.37 caps, right-aligned 5.6 left of its toggle. VELOCITY and SOURCE labels move **above** their toggles (y 131.4) so the three don't stack into one ambiguous column of words.
- Positions likely VIB / OFF / FILT (eng confirming); no scale words drawn yet.
- Keys may rise 1–2 mm on a compliant layer (eng confirming). The model takes `R5_KEY_LIFT`, so the front views re-render in one command.

## Jacks (rear wall)
- PHONES, EXT IN, FILTER CV, PITCH CV, GATE, MIDI IN, **MIDI OUT** (owner, new), USB-C; 8 ports at 19 pitch, x 76–209 (power at 59), inside the straight rear run (x 44–246). The legend sits over each port in the rear band.
- The digital brain is now a Daisy Seed (owner). It sits on the main board, so nothing visible changes; one rear USB-C remains.

## Key edge, both options (sheet D)
| | A · at the edge | B · small lip |
|---|---|---|
| Front edge | r 4 round-over (sides and back stay r 12; front corners blend 4 → 12 by y ≈ 40) | r 12 brow, 13 mm of flush felt in front |
| Pegs | whites y 13.5, sharps y 36 | whites y 19.5, sharps y 42 |
| In front of the heads | 7 mm of felt falling over a tight edge | 13 mm of felt rolling away |
| Reads as | keys meeting the edge, like a hand-pan's rim | a soft brow, the round-4 look |
| My lean | **A**: it answers "at the edge" literally and the felt still wraps. Risk: r 4 is tighter for the blocking (add to the corner test). | |

## Motion and feedback (states)
- **Key:** 2.5 mm straight down; the head lands on the felt collar (silent, a soft "thup"). No visual feedback on the key itself.
- **TAP:** the same peg feel. **Proposal (needs systems/eng):** after a tap, the status light flashes the tempo 4 times (green, 40 ms on), then returns to normal. No second light (H7).
- **TYPE switches:** 4 detents; the pointer on the cream knob points at the pressed type name.
- **DRIFT:** no light; fully left is the "steady" end of the tag scale (marked by a heavier tick).

## Open questions
1. **Systems/eng:** the tempo flash on the status light (or no tempo feedback at all).
2. **Maker:** the corner blocking test must now include the r 4 front edge.
3. **Owner:** A or B (my lean A).
4. Still open from round 4: cream KN1250 on A-5518 round-shaft pots (systems hasn't ruled).
