# RAIN: how it looks and feels (visual)

Seed: ONE SHEET (v1.1, 276 × 180). Kind: a landscape. **Point of view: every control is a drop on still water; its rings spread until they meet the next drop's, and the meeting lines draw the panel's map.** Rule: *everything that breaks the surface ripples.* Emotion: calm. Read with `how-it-works.md` (systems rev 1) and `../common-how-it-works.md`.

**Rev 1, 2026-11-13, concept turn 1 (visual).** Images in `img/` (from `_mock-src/rb.py` + `figs_rb.py`). The ring field is computed from the real layout, not drawn by hand.

## Images
| | |
|---|---|
| The look (3/4) | `img/rain.jpg` |
| Arm's length (director's test a) | `img/rain-arms-length.jpg` |
| Close (test a) | `img/rain-close.jpg` |
| Stepping stones | `img/rain-stepping-stones.jpg` |
| True-scale top view | `img/rain-top-12.70px-per-mm.png` (12.70 px per mm: at that ratio it shows at real size) |
| TIME, FREE / SYNC and lily pads, native resolution | `img/rain-time-and-pads-12.70px-per-mm.png` |
| Pegs, native resolution | `img/rain-pegs-12.70px-per-mm.png` |
| Ring pitch vs v1.1, at 40 px per mm (test c) | `img/rain-ring-pitch-compare-40px-per-mm.png` |

## Principles
1. **Everything that breaks the surface ripples.**
   - Knobs, CUTOFF, the TYPE switches, toggles, the stick, TAP, the status hood, the 25 pegs and FREE / SYNC: each starts its own rings just outside its skirt or washer.
   - *Because* one sentence then decides the whole face.
2. **Where two ripples meet, the water is still.**
   - Each element's rings are clipped to its cell (a power diagram of the elements, weighted by size), with a 0.64 mm smooth seam where cells meet.
   - **The seams are the only section marks:** no grooves, no headings (director: "Courage!"). The sketch's promise holds in the render: the rows and the three columns read from the seam web alone.
3. **Words float on lily pads.**
   - Every printed word sits on a smooth rounded pad cut out of the field (0.85 mm margin, R 1.2).
   - *Because* type on ripples is unreadable, and a pad says "this is a word" without a box.
4. **Two finishes, still.** Smooth and rings, his rule. RAIN just lets the rings run to every edge.
5. **One leaf.** CUTOFF in mustard (a 1083 hero knob in mustard) is the only colour on a stone pond. No second accent (director).

## Look
- **Shell:** pale wet-slate stone PETG (#d9d6ca drawn), printed face down on smooth PEI. One filament, one swap (legends dark #2e2924).
- **Rings:** modelled grooves 0.45 wide at **0.9 pitch** (systems §3), drawn at true pitch in every render. Groove tone #b4b0a1 (a sheen difference in reality, not a colour).
  - 1:1 compare: v1.1's first-layer rings (0.45) are finer and silkier; RAIN's 0.9 grooves read as a deliberate engraving, nearer a record than a silk.
  - **My call:** at 0.9 it's still "rings", not "record grooves", because the rings stop at the seams and never run long. The coupon decides.
- **Ring starts:**
  - knobs r 7.75 (just under the KN1250 skirt);
  - CUTOFF 10.9;
  - toggles and hood 3.7;
  - stick 9.3 (outside its gate ring);
  - TAP 7.6;
  - pegs 7.3 (outside the 14 mm felt washer).
- **Knobs:** cream KN1250 ×31 + MOD; CUTOFF **mustard** 1083 (#c9a032 drawn) with a dark line.
- **Pegs (stepping stones):** HUSH's 12.7 button plugs in two stone greys: naturals #a19e94, sharps #66645e. Each sits on a dark felt washer in the deck.
  - The key window closes into a deck (systems §2): whites y 14, sharps y 36.5, x 12 + 18n. **Width stays 276** with the 14 mm washer (systems).
- **Legends:**
  - v1.1 ONE SHEET type (Inter SemiBold caps, 1.9);
  - with no section headings, the back row says what it is in front: **ECHO TYPE / REVERB TYPE**;
  - TIME and DECAY (short) sit behind their knobs (common §2);
  - I tried the full "ECHO TIME" behind first; it ran into the type-name fans, so it's back to TIME / DECAY.
- **FREE / SYNC:** one more stone, so it ripples; "FREE" left, "SYNC" right, on pads.
- **TIME:** two scales over ±135°: ms ticks inner, division marks outer (tick, dot = dotted, triangle = triplet), no numbers.
- **Jacks:** rear wall as v1.1; the legend row on pads in the field.
- **Status light:** hooded (common §3), and rippled like everything else.

## Motion, feedback, sound
- Pegs ≈ 2.5 mm onto felt, silent.
- The light: as v1.1 (H7 tempo flash).
- **A single soft "drop" at power-on**, when the status light reaches ready: firmware, $0, off by a key combo (systems §4: power-off is impossible on the hard switch). Optional.

## What it had to prove (director)
| Must prove | Where | Status, my honest read |
|---|---|---|
| (a) calm at arm's length, alive up close | `rain-arms-length.jpg`, `rain-close.jpg` | Close: yes, the rings catch the light round every knob and the seams draw the map. At arm's length the field reads as a soft texture with a visible web. It's busiest at the rear, where the type-name pads, the jack pads and the back row crowd into one band. Not dizzy in these renders, but renders flatten sheen, so **the coupon under a tree is the real test.** |
| (b) legends on pads readable at S1 sizes, in sun | `rain-time-and-pads-…png` | Readable at 1:1 on screen. The smallest (TYPE names, 1.05) sit on the tightest pads. Sun: UNVERIFIED (coupon). |
| (c) 0.9 pitch still looks like the rings he loved | `rain-ring-pitch-compare-40px-per-mm.png` | Coarser, honestly. Shown side by side so he can judge. A 0.6 pitch would sit between (render: `RB_RAIN_PITCH=0.6 python3 rb.py rb_rn_main`), if the groove can be printed. |
| (d) pegs on ONE SHEET, white / black kept | `rain-pegs-…png`, `rain-stepping-stones.jpg` | Width 276 kept (systems). Two greys read as two rows; the contrast is gentle on purpose. |
| (e) mustard earns its place as the only leaf | `rain.jpg` | It's the one warm thing on the pond, on the instrument's most important knob. Nothing else is coloured. |

## Open
- **The coupon** (smooth + 0.9 grooves + a seam + a lily pad) under a tree. It decides RAIN.
- **The field doesn't yet run over the side walls' top chamfer** in the model (top face only). The director asked for it to run to every edge, chamfer included; to add.
- One-piece print on a 350 bed (systems §3): the field must be unbroken.
- Render-time note: the full grooved face renders in seconds as 2D geometry; the STL for printing will be heavier (UNVERIFIED).
