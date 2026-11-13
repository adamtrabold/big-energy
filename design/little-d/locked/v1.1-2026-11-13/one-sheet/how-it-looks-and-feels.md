# ONE SHEET: how it looks and feels (visual, round 5)

Kind: **an economy**. Pole: designed for use. Body: **one printed shell, one filament, one swap; unibody, opened from below.** Read with `how-it-works.md` (rev 5.1) and `../common-how-it-works.md` (rev 7.1). Layout: systems' round-5 final + DRIFT (ONE SHEET x = FOLD x − 5; checkers 0 violations).

Mocks (300 dpi A3, tag "round 5"):
- `mock-A-look.png`: 3/4 view (edge A), close-ups of edge A and B, principles, the two-finish inset (magnified and true scale), facts;
- `mock-B-real-size.png`: 276 × 180 at 1:1 (edge A);
- `mock-C-construction.png`: a section with all four rows, the underside, the build order, a 3:1 "ripple in section";
- `mock-D-front.png` (NEW): front elevations at 1:1 for A and B, right-end profiles for A and B, the key edge and press at 2.3:1.

Sources: `../_mock-src/r5.py`, `../_mock-src/sheets_r5.py`.

## What the owner asked for, and where it shows
| Owner (round 5) | On the sheets |
|---|---|
| "I love the rings texture — only use no texture and that texture" | Exactly two finishes: smooth, and concentric rings round every rotary. The ±45° checkerboard is gone. A inset; B at 1:1. |
| keys "somewhat raised" / at the edge, "Show me both" | Whites 26.5 (2.5 above the 24 face), sharps 28.5. Edge **A**: skirted tops to the front, wall under them at z 17.5, a 4 mm shadow slot. Edge **B**: a 2.4 mm lip to z 25.5 (R 1.2), 1 mm below the key tops. A close-ups, D. |
| "draw the mechanism" | D bottom row: Choc V2 on strip C, stem, pressed-on top, magnet over a Hall sensor; ≈ 3 mm straight down, rest vs pressed, for A and B. |
| front views | D. |
| echo + reverb, full 8; drift | PLAY right: REPEATS, ECHO MIX, REVERB MIX, TAP. Back row (y 146): DRIFT, ECHO TYPE, ECHO TIME, REVERB DECAY, REVERB TYPE, VOLUME. |

## The idea
One closed shell, printed face down in one filament with one swap. **The face has only two finishes: still, and rippled where something turns.**

## Principles
1. **One face.** *Because* in an economy you don't add a line the drawing doesn't already have.
2. **Still water, ripples where it turns.** *Because* both finishes are free from the nozzle, and the rule that places them is one sentence: **if it turns, it ripples.** Knobs, CUTOFF, both TYPE switches, DRIFT and VOLUME get rings. TAP (pressed), toggles (flicked), lights and the stick (a fore-aft slot) sit on smooth.
3. **Face down on smooth steel.** *Because* the first layer is FDM's best surface and smooth PEI shows ring sheen.
4. **One filament, one swap.** *Because* legends and section names are cut-outs in the first 0.6 mm, filled dark by one change. Names and legends are now one dark (#2e2924), as one swap implies.
5. **Opened from behind.** *Because* every screw is underneath, one M3 size into inserts.

Random draw (real RNG): "Water" + weaving. Water gave the principle's language (still / ripples) and the rule. Weaving gave the spacing: like threads, neighbouring ripples must not cross, so each field stops at r 9.25 and leaves 1.5 mm of smooth between neighbours.

## Look
- **Shell:** cream PETG (#e8dcc2 drawn), printed face down on smooth PEI.
- **Rings:** concentric first-layer lines at 0.45 mm pitch (drawn 1.1, 2.5× coarse, labelled), from r 7.75 (just under the knob skirt) to **r 9.25**; **CUTOFF r 10.9 → 12.5**. About 2 mm of ripple shows past each skirt.
- **Smooth:** everything else, including round toggles, LEDs, TAP, the key-window border and the rear band.
- **Grooves** (0.6 × 1.2, sunk): x 96.5 / 179.5 from y 52.6 to 133.5; y 85.4 full width; back-row breaks x 89 / 138 / 187, y 138.5–156.5.
- **Names** (Inter Bold 2.1, dark): PITCH, FILTER, FX & OUT at y 80.8; OSCILLATORS (left) and CONTOURS (right) at y 136; MIXER (1.8) at x 138, y 133.6. It's crowded: ≈ 3 mm to the REVERB DECAY label (open question).
- **TYPE switches:** detents at −60 / −20 / +20 / +60° over the top; the 4 names in Inter 1.05 caps above, each over its detent (inner two at y + r + 3.4, outer two at y + r + 5.6). Echo: TAPE, BBD, CLEAN, PING-PONG; reverb: PLATE, HALL, SPRING, SHIMMER. They're printed on the smooth face just outside the ring field.
- **TAP:** a white acrylic 12 mm round cap (the key-top material), on a thin warm-grey ring, at the end of the PLAY row (x 256). It's the key material because it's played in rhythm like a key.
- **Knobs:** cream KN1250 ×31 + MOD; cream 1083 CUTOFF with a red line.

## AFTERTOUCH toggle (owner, new; placement is mine, pending systems)
- A third toggle in VELOCITY's column, at (171.75, 111.5): FILTER MOD (y 100) / **AFTERTOUCH** (y 111.5) / VELOCITY (y 123). It answers "next to the velocity toggle": the two key-response switches stack.
- Checked with the checker's rules: 2.30 to FILTER MOD (≥ 1.5), 3.15 to the break (≥ 3). **Cost: mirror symmetry**, since the matching slot left of the mixer is empty. Systems to accept it or re-place it.
- Labels: AFTERTOUCH in 1.37 caps, right-aligned 5.6 left of its toggle. VELOCITY and SOURCE labels move **above** their toggles (y 131.4) so the three don't stack into one ambiguous column of words.
- Positions likely VIB / OFF / FILT (eng confirming); no scale words drawn yet.
- Keys may rise 1–2 mm on a compliant layer (eng confirming). The model takes `R5_KEY_LIFT`, so the front views re-render in one command.

## Jacks (rear wall)
- PHONES, EXT IN, FILTER CV, PITCH CV, GATE, MIDI IN, **MIDI OUT** (owner, new), USB-C; 8 ports at 15.5 pitch, x 152–260.5 (power at 135); legend type 1.5. The legend sits over each port in the rear band.
- The digital brain is now a Daisy Seed (owner). It sits on the main board, so nothing visible changes; one rear USB-C remains.

## Key edge, both options (sheet D)
| | A · at the edge | B · small lip |
|---|---|---|
| Section | wall 0–17.5 → 4 mm shadow slot → key skirt + top 21.5–26.5; front face 0.3 behind the body's front plane | wall to 25.5 with R 1.2 top; key fronts 0.6 behind it at y 3 |
| Pressed | skirt stops 1 mm above the wall | keys drop 2 below the lip |
| Reads as | a row of keys that *is* the front edge; a dark line under them | a cream rim, keys standing 1 mm proud of it |
| Bag | key fronts exposed | key fronts guarded |
| My lean | **A** for the look (and it's what "at the edge" means); B if it travels in a bag without a sleeve. | |

## Motion and feedback (states)
- Keys: ≈ 3 mm straight down (Choc V2), silent switch; no visual feedback.
- TAP: tempo feedback proposal as HUSH (status light flashes the tempo ×4). Needs systems/eng.
- TYPE switches: 4 detents, the knob line points at the type name.

## Open questions
1. **The coupon**, now two patches (smooth, rings) on smooth PEI in raking light. Still not printed.
2. Slicer route for rings (a cylinder modifier with a concentric bottom pattern is the likely PrusaSlicer route; UNVERIFIED).
3. **Owner:** A or B.
4. Tempo flash (systems/eng).
5. MIXER's heading is crowded between the back-row labels. If the director objects, the cleanest fix is shorter labels (TIME / DECAY), or dropping all three VOICE headings and letting the grooves do it.
