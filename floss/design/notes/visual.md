# floss: visual designer notes

## Where things stand (2026-11-22, concept round 1, my first concept turn)
- The jam is closed (turns 1–6). Systems wrote `jobs.md` rev 1 (sent to the owner), `concepts/common-how-it-works.md` and `concepts/{bow,kept,tide}/how-it-works.md` (rev 1).
- **I wrote:**
  - `concepts/common-looks-and-feels.md`;
  - `concepts/{bow,kept,tide}/how-it-looks-and-feels.md`;
  - per concept: `mock-A-look.png` (3/4 view + idea + principles + facts + a secondary view) and `mock-B-real-size.png` (1:1 plan on A3; scale bar 50 mm);
  - `concepts/compare-faces.png` (three plans at the same scale plus a table of what differs).
  - Every image was opened and checked.
- **Source:** `concepts/_src/fl.py` (a tiny orthographic slice-stack renderer, plan drawer and marking system) and `concepts/_src/concepts.py` (geometry of all three, sheets). Run `cd concepts/_src && python3 concepts.py [bow kept tide compare]`. It needs matplotlib, and it doesn't work under `python3 -I`, because it imports `fl` from its own folder.
- **Fidelity limits:** no OpenSCAD or POV-Ray here, so these are slice-stacked orthographic drawings, not renders. Legends are in Inter, standing in for Kalam (not installed). Not yet run through a layout checker.
- Next: the director steers after this pair of turns (systems and me).

## The family's visual language (what floss inherits)
- **CATHEDRAL:**
  - case: walnut FOLD-format; superellipse corners (case 28.3, plates 24); cream plates;
  - colour: brass and black; the low base knob is Tayda alu Ø 10 × 8;
  - lid knobs: Ø 14.9 black;
  - keys: mushroom-plug keys Ø 12.7 on an interchangeable carrier (tenon 9.53 × 3.2);
  - lid stands at 120° on brass stays; TAP's lit bezel is the status light (round 6);
  - marking system: one tick ring at r + 1.7, ticks 0.35 wide, major 1.0 / minor 0.55, 11 ticks over 300°, stepped knobs show detents only; words above controls; one word per label.
- **ONE SHEET:** a cream PETG shell, one filament, one swap; rings round rotaries ("if it turns, it ripples"); sunk grooves 0.6 × 1.2; keys at the edge (edge A).
- **HUSH:** a felt pebble 290 × 186, rear R 44; maple pegs on felt collars; pressed words; tags under knobs.
- **Owner taste (Big Energy):** off-centre bad; logical grouping first; signal order; one plain word; one accent; loved pegs; reversed key colours asked but unanswered; "more brass than black" (CATHEDRAL).

## Decisions so far (mine, unless noted)
- **Three concepts, three family bodies:** BOW = CATHEDRAL base with the lid as soundbox; KEPT = ONE SHEET slab; TIDE = HUSH pebble. (Director turn 5 sent these three forward; the bodies were my turn 6, and systems adopted them.)
- **The split:** the axis runs through middle C; an 18 mm gutter (TIDE 28); 126 mm each side; the coral rim tick B|C is the only mark. Systems adopted it (common §2.1). The director hasn't ruled on whether the tick is enough.
- **Coral marks where the life lives:** BOW pressure, KEPT ensemble depth, TIDE drift. No coral part checked yet (fallbacks: orange anodised, a coral cap insert, a coral line).
- **The status light = TAP's lit ring** in BOW and KEPT (CATHEDRAL precedent). TIDE: a separate LED behind DRIFT. This is a change to systems' common §2.9 (light only).
- **Names (my proposals):**
  - Daisy shimmer modes *wide · glass · tape* (analog first);
  - strands *low · main · high*, printed once in BOW's gutter, low nearest the keys;
  - octave *−2 … +2*.
- **BOW:**
  - Ø 10 × 8 black low knobs (CATHEDRAL's base part); octave Ø 14 × 8 (part open);
  - dark naturals and bone sharps on warm-grey felt collars;
  - lid inner face: plain oatmeal cloth plus one coral thread, no motif; lid back: brass impost lines plus a blank field for the owner's façade;
  - keys moved to y 22 / 44 for the corner clearance (this costs 3 mm of tab clearance: flagged to systems).
- **KEPT:**
  - depth 140 → 148 (grille slots y 124–140 clear the rear words);
  - map changes: attack and release to the rear, ensemble behind depth, volume front, blank rear-left;
  - strings and brass stay in the left region, the Solina's way, with a groove under OCTAVE L + bass only to mark the left half's own.
- **TIDE:**
  - rebalanced map 4 | 4 front, 3 (+ blank) | 4 rear; TAP front; tempo beside TIME;
  - HOLD a Ø 16 push-push maple peg; DRIFT Ø 24 coral; status LED behind DRIFT;
  - lantern through a punched field ≈ 84 × 30 at y 156.

## Push / reshape / kill (round 1)
- **No kill.** All three differ in kind, and every one covers every stated job. Weak inferred jobs: KEPT J18; TIDE J7 and its held-note visibility (J13 gap).
- **BOW:** lead. Reshape question for the director: coral on a selector you *set* (pressure) is indirect. Alternative: coral felt collars under all 25 keys. Not drawn.
- **KEPT:** keep. Honest weakness: Choc two-row caps read "modern mini keyboard", so it's 1974 in layout only. A real keyboard silhouette would break the family's key strip. Named, not recommended.
- **TIDE:** push. The most distinctive. Weaknesses: the empty back third (shrink to ≈ 160 if eng's board allows) and sun (a dusk-and-shade object).

## Director's objections so far
- Turns 3 and 5 (jam): convergence; the rose; off-centre; jargon; "smaller CATHEDRAL?"; settled asks going idle. All answered in the jam. Round 1 scores: none yet.

## Open questions
1. **Director:** is the rim tick enough for middle C? Coral on pressure, or on BOW's collars?
2. **Systems:**
   - BOW tab clearance (2.6 mm after the key move): move the tabs back 3, or collars Ø 15;
   - accept the status light = TAP's ring;
   - accept the KEPT and TIDE map changes.
3. **Eng:**
   - BOW lid box (driver + radiator in ≈ 22), leads through the hinge, Hall power switch, lap centre of mass;
   - KEPT's sealed volume;
   - TIDE's radiator direction and foot ring;
   - whether felt collars help or blur per-key pressure;
   - the octave Ø 14 × 8 knob part clearing BOW's closed lid;
   - the HOLD peg push-push mechanism.
4. **Owner (later):** BOW's reversed key colours; open-lid = on.
5. **Parts:** a coral knob (Ø 10, Ø 14.9, Ø 24); bone sharps (printed or pale wood).
6. **Tools:** Kalam source; a layout checker run; real renders for the concept that goes forward.

## Next
- Read the director's steer and scores. Fix what's objected to.
- For the concept(s) going forward: a checker run, real renders (standing, closed, in a hand, in sun), the key edge section, and state sheets.
