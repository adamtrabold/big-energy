# Visual designer notes: instrument form factor

## PAUSED 2026-11-12: owner paused the full instrument mid fix pass

Stopped on the coordinator's instruction. No more drawing until it resumes.

**Done (rendered, opened and checked for legibility):**
- `slab/slab-mock.png` + `slab-exploded.png`
  - F1: price box ≈ $530–860.
  - F2: Choc V2 silent + key-top magnet + TO-92 in the text; Gateron is the fallback.
  - F3: 22 mm zone, body 292 with 3 mm edge margins (matches systems). The Adafruit #2765 body is dashed at 17.5 × 17.4, in a fore-aft gate, with the mod slide pot behind it.
  - F4 as corrected: 12 MIDI controls, mod has a gold dot, CC1.
  - F5: owner-cut at Vector Space.
  - S1: the 12° text is gone.
  - S2: the lid is in the felt-faced body material, with a felt lining drawn.
- `motto/motto-mock.png` + `motto-exploded.png`
  - F1: ≈ $565–920.
  - F2–F5 as on SLAB. 12 pips; mod's pip sits by its fader.
  - M1 (a): callout "VCO cores on the right B board (E8)".
  - M2: spine panel 110, body 190 → 165 at the right (curve amplitude 25), width 292.
  - M3: chartreuse kept, with a "swap: one cap" note.
  - M4: cardboard-lid test kept.
- Kit: `r2.py` has a new `bendmod_lead` (ZW = 22, a `pip` arg, dashed part bodies) and MOTTO panel D = 10. `r2s_common.py` has `price_box()`. Pre-fix-pass kit backup: `/tmp/mockkit_backup_r2` (tmp, may vanish).

**Not done:**
- **DISH:** `sheet_dish.py` is half-patched and NOT rendered. `dish-mock.png` is still round 2 (stale).
  - Done in code: width 292, D1 left-wing layout (emphasis Ø20 at (63.5, 52) local, amount just outside it), the cross-tie, the hand-span overlay.
  - Measured span: **≈ 100 mm 3D (81 plan)**. That's under 120 and agrees with systems' estimate.
  - Still to do in the sheet text: price ≈ $570–920 (+$40–60, slip ring), steps 18, D2 spec on the side view, D3 (service loop + slip ring, ≈ 37,000 cycles, UNVERIFIED), D4 (my call: accept the loss, one line), D5 note, the 12th pip, the K-E text. The side view also needs the emphasis→cutoff line in place of the old 150 mm reach line.
  - **Open with systems:** they put the speaker under the well's rear third (≈ 160 from the front). I drew it at the well centre (y 66 from the rear), which the director accepted. If it goes to the rear third, the raised dish sits over the grille.
- **Controls menu not redrawn.** Needed:
  - lead = #2765 named, 22 mm zone;
  - mod fader Pico-read → AS3360, gold mark, CC1;
  - RANGE: no ring;
  - leather band = option on one look only;
  - abacus: menu only;
  - delete "mod is an analog pot" text.
- **Key menu:** skipped on purpose. The keys rethink (`keys/first-principles.md`) will replace it.
- **Look sheet and size sheet not re-rendered.**
  - The look sheet picks up the new `slab_top` (292) on re-run.
  - The size sheet still shows DOCK and the 285 widths, and needs editing.
- **Docs not updated:** the how-it-looks-and-feels.md files (common, slab, motto, dish, controls).
- **Next step on resume:** finish DISH, the controls menu, the look and size sheets, then the docs. After that, the director scores the fix pass.

## Where things stand (end of concept round 2, visual turn)

**Done this turn (all PNGs opened and checked for rendering and legibility):**

| Sheet | File |
|---|---|
| SLAB mock (new, replaces CASE) | `concepts/slab/slab-mock.png` (+ `.svg`) |
| DOCK mock | `concepts/dock/dock-mock.png` |
| MOTTO mock | `concepts/motto/motto-mock.png` |
| DISH mock | `concepts/dish/dish-mock.png` |
| Exploded "how it goes together", one per concept | `concepts/<c>/<c>-exploded.png` |
| Key menu (real parts) | `concepts/keys/key-menu.png` |
| Controls menu (knobs, bend/mod lead + spread, faders) | `concepts/controls/controls-menu.png` |
| Look sheet on SLAB, 4 looks | `concepts/look-sheet.png` |
| Size sheet against eng's box | `concepts/size-sheet.png` |
| Looks-and-feels docs | `concepts/common-looks-and-feels.md`, `concepts/<slab|dock|motto|dish>/how-it-looks-and-feels.md`, `concepts/keys/…`, `concepts/controls/…` |

Every sheet carries: cost delta vs SLAB, build-step count, a "Checked against"
box (owner.md entries + eng sections + rulings), and the placeholder warning.

**Generator (round 2):** `concepts/_mockkit/`
- `r2.py`: parts at R1 minimums (panel 280 × 100 with kind slab/dock/motto,
  light variants pip/none/pips; knob/rotary/toggle/fader wrappers with 3.6 mm
  legends; key tops K-A/K-B/K-D/K-E; `bendmod_lead` = gated stick + mod fader).
- `r2s_common.py`: headers, boxes, the MOTTO palette, `exploded()` renderer,
  `frame_draw()` for open laser frames.
- `sheet_slab.py`, `sheet_dock.py`, `sheet_motto.py`, `sheet_dish.py`,
  `sheet_menus.py`, `sheet_look.py` → SVG; then `python3 render.py <svgs>`.
- `kit.py` changes: `txt()` now escapes `&` and `<` (two sheets broke on them);
  `pgrad(p)` gives per-palette hero/key gradients so several palettes can share
  one sheet (look sheet).
- Fonts: Kalam in `~/.fonts`, Inter in `/usr/share/fonts/opentype/inter`.
  Kalam capHeight 0.739 em → 3.6 mm font = 2.66 mm cap height.
- Round-1 code (`compact*.py`, `common_views.py`) is untouched and superseded.

## Decisions this turn and why

- **R1 panel:** 280 × 100, 12 mm caps at ≥ 17 mm pitch, rotaries at 24 mm
  pitch with Lorlin 30° index (numerals collided at ±125°), faders 11 mm pitch
  × 28 mm travel, Ø40 driver under a Ø41 grille at the rear-right. kbd 1/2 sit
  under the cutoff hero (they act on cutoff); HOLD in the play column; the pip
  (V-a) beside HOLD.
- **Gold ring = MIDI-ownable** (director's R7 idea), on the 11 controls only;
  fader slots get a gold dot. Owner's latest MIDI rule (knob-only = no MIDI,
  MIDI can't flip switches) is written on every sheet.
- **Real parts (owner, mid-turn):** no 3D-printed touched parts, no harvested
  keybed, velocity required. Eng's key-sourcing found no bare mini keybed. So:
  SLAB/DOCK/MOTTO use **K-B lever tops (service-cut) on Gateron low-profile
  Hall switches**; DISH uses **K-E bought maple button plugs on Hall
  switches**; K-A flat 1u caps is the all-catalogue fallback. K-C (Choc, no
  velocity) is out; K-D pads only with an added magnet + Hall.
- **Bend/mod (owner's pick, mid-turn):** one-way gated thumbstick for bend +
  20 mm mod fader, drawn in the 13 mm zone on every mock (DOCK: pod beside the
  panel). Controls menu shows it as LEAD with all alternatives.
- **SLAB:** Field look; stand fold sequence drawn; draw "typewriters" for the
  stand confirmed the lid-comes-off reading.
- **DOCK:** drew systems' honest numbers (300 × 237 played, ≈ 70 carried).
  **My push:** wheel/stick pod beside the panel (+15 mm width, panel
  untouched) instead of inside 285.
- **MOTTO:** round-2 draws: cork body + white panel; "Use an unacceptable
  colour" → acid-chartreuse hero; lid placeholder = ribbon alone on raw birch.
  Walnut only on the lid's outside. 11 pips drawn (2 lit). kbd 1/2 beside the
  rose. Reflector printed "UNVERIFIED".
- **DISH, geometry finding:** with the fork pivot at the well's front edge and
  the dish at 50°, the lower rim hangs 36 mm forward 7 mm above the sharps.
  **I moved the pivot to the well's rear, fork at 70°, arms 58 mm** (drawn,
  with the old geometry ghosted red). Speaker moved to the well centre (≥ 60 mm
  from the sharps' switch row). Dish ring r 38, chord 18.3 mm, legends around
  the rim (flipped on the lower half).
- **Exploded views:** side sections, front at the left, numbered by build step,
  with an assembled view at the same scale under each.

## Director's round-1 objections and how they're answered

| Ruling | Answer on the sheets |
|---|---|
| R1 size / panel / legends | 280 × 100 panel, 2.66 mm legends, box on the size sheet |
| R2 SLAB | new mock; lid-as-stand shown with the fold sequence |
| R3 DOCK | long keys (K-B 80 mm); carry < 45 not reachable (≈ 70 drawn, systems' floor 56); dock face, cleats, pogo pads drawn; Ø40 speaker |
| R4 MOTTO | cork + white panel, abstract placeholder, Ø40 rose, 11 pips, dials cut, walnut keys as service-cut tops |
| R5 DISH | rebuilt per the split; speaker in the well; Ø112 (systems: 130–140 doesn't fit) |
| R6 keys | key menu, now buyable parts; no printed samples (owner) |
| R7 MIDI scope | 11 ownable everywhere; light variants pip / none / pips / bullseye |
| R8 cost + steps | on every sheet |
| R9 look sheet | on SLAB at real proportions, 4 looks |

## Open questions

- **Owner:** are service-cut (laser/CNC) key tops "real parts"? If not, K-A
  everywhere. Which look? Chartreuse yes/no (one cap).
- **Systems:** confirm DISH rear pivot + speaker move; DOCK pod outside 285;
  bend stick + mod fader in the 13 mm zone (stick body ≈ 17 mm square: fit
  UNVERIFIED, mini stick fallback); the switch board replaces strip C's TO-92
  line (two rows of switches: sensor positions change).
- **Eng:** Gateron LP switch fit at 17.4 mm pitch; LP caps; a true single-axis
  sprung stick part; SparkFun pad pitch and Hall travel; E1 (mod as VCA) would
  let DOCK's pod move onto the module.
- **Director:** DOCK over the box; DISH 38 mm base; SLAB 8° vs 12°.

## What comes next

1. Director scores round 2 against R1–R9 (process fix met: every sheet cites
   the owner.md entries and eng sections it was checked against).
2. Systems reacts to the DISH geometry change, the DOCK pod, and the switch
   board replacing strip C.
3. Owner sees the four mocks, the exploded views, both menus and the look sheet.
4. After approval: handoff "How it looks and feels" from
   `common-looks-and-feels.md` + the concept file, every state included.
