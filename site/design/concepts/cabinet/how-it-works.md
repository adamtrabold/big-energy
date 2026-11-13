# C · Cabinet — how it works

Product designer (systems focus), concept turn 1, 2026-11-13. Structure-first: the landing is a reading of where the project stands. Shared viewer, lamp, links and states are in `../common-how-it-works.md`.

Draw for this turn (Python `SystemRandom`): Oblique "Only one element of each kind". Applied: **one control per question**. Where is it? the cabinet. When was it? the scrubber. Is anyone working? the lamp. Nothing else on the landing is a control. It also cut the records column (below).

## Reshaped from the jam (and why)
1. **Four columns, not five: sheets · diagrams · docs · tests.** Records leave the grid. A record (owner record, scores, jams) isn't something made *at* a stage, it's the log *of* the stages, and in a grid it's a column of 1s. Decisions are events in time, so they live on the **scrubber** as marks (one element of each kind: time lives in one place). Records as files stay reachable from the history list (J2).
2. **The Lock row isn't split by kind.** Locking makes versions, not sheets. The Lock row is **one wide drawer: "v1.1 · current · 2 versions"**. Handoff is the same (one doc when it exists). Rows that split by kind: Concept, Spec, BOM, Breadboard, Boards, Prints, Assembly.
3. **Newest item on the landing** (director push 1): one strip under the cabinet shows the single newest item small, with its label line. Not a feed; one thing.
4. **Level, not unfinished** (push 2): a 1.5 px ink **level line** under the current stage row. Above it, rows are filled; below it, rows are outlines in ink 2 with "not yet" in the first cell only, not a dot per cell. Four columns × 6 empty rows of dots read as a broken table; one word per row reads as the road ahead.
5. **Scrubber kept, narrowed** (push 3). It scrubs **decisions and locks**, not files: ticks are owner decisions, round ends and locks. Dragging back shows the cabinet as the *records* say it stood (which concepts were alive, which stages had begun, which version was current), with counts of what was kept and a plain note where files weren't. Real case: drag to **Round 2 · 12 Nov** → Concept row shows six concepts alive (HUSH, ONE SHEET, FOLD, TYPE CASE, HYMNAL, UNDER GLASS); Lock is "not yet"; the note says "sheets from rounds 1–4 weren't kept". If the director judges that too thin, the scrubber becomes a plain history link and nothing else changes. I'd keep it: it's the only concept where "see the history" is a gesture, and decisions are the history he cares about.

## Structure
Landing, phone 390 × 844, no scroll:
1. Lamp line (common §2). STANDBY text here: "Standby · last: FOLD-D rev H · 14:02".
2. Name; one line under it: "v1.1 current · waiting on you: ONE SHEET or FOLD".
3. **Cabinet**: 9 rows (stages) × 4 columns. Row label left (56 px gutter). Cells: count of items (not files: FOLD-A with 3 revs counts 1). Unseen dot in a cell's corner (J12). Lock and Handoff rows are single wide cells.
4. **Newest strip**: small image or waveform + "FOLD-D rev H · stands at 120° · 14:02". Tap → item.
5. **Scrubber** (thumb zone): line, ticks (short = decision / round end, long = lock, "now" at right end). Label above when touched: "12 Nov · Round 2 · as it stood". A "history" word at its right end opens the history list.

Inside a drawer (stage × kind): list of items, grouped by concept for sheets (current concepts first, then dropped, greyed), newest first for other kinds. Each row: code · title · rev · status. Desktop: master-detail, cabinet left 5 cols, drawer/item right 7 cols, scrubber full width at the bottom.

History list (from "history" or a tick): grain switch **Day · Round · Version** at the bottom; entries newest first; decisions verbatim at body size with caused items under them as rows; locks as ruled, signed lines. Records (owner record R-001, scores, jams, notes) are listed at the top of the history list as "the records" with their codes.

## Flows and the 8 frames
| Frame | Path | Taps |
|---|---|---|
| 1 STANDBY | Landing as above; lamp ring; "waiting on you: ONE SHEET or FOLD"; name "( name to come )". | 0 |
| 2 ON, event lands | Lamp ON "On · round 6 sheets · since 13:40" dips; Concept×sheets cell's count stays (FOLD-D already counted) but gets the unseen dot; newest strip swaps to "FOLD-D rev H". If images not published yet: strip shows "FOLD-D rev H · queued". | 0 |
| 3 FOLD-A v1.1 → v1 | Concept×sheets (1) → FOLD-A (2): opens current rev (= v1.1 form today; if a later rev exists, the v1.1 form is in the lineage row, +1) → lineage row: tap v1 (3) → compare. | 2 to v1.1, 3 to v1 |
| 4 Bass pluck A/B | Concept×tests (1) → "Bass pluck" T-00x (2) → play; A/B golden · perturbed. | 2 |
| 5 "Switch to Daisy Seed" | "history" (1) → Day grain → 13 Nov (scroll) → the decision with caused items: D-0xx daisy-pin-and-audio-check (evidence, listed as "before"), D-0xx daisy-first-principles, spec rev → tap (2). Or drag the scrubber to the tick (label shows the decision words), tap the label. | 2 + scroll |
| 6 What's in v1.1 | Lock row (1) → v1.1 (2) → track list: HUSH A–D, ONE SHEET A–D, FOLD A–E, docs, spec rev. Or tap "v1.1" in the line under the name (1). | 1 |
| 7 Snapshot | No lamp, "Snapshot · 13 Nov 14:02"; no unseen dots; everything else identical. | 0 |
| 8 Desktop | Cabinet left, newest item open on the right by default (so the big area is the work, not empty), scrubber across the bottom. | 0 |

Other jobs: J2 every item is in a drawer or the history list; archive concepts sit in Concept×sheets/docs, greyed. J8 copy link on every label; `#/s/concept` opens a row. J9 status in each row. J13 by stage+kind in 2 taps; by code: typing isn't offered (no search box on a Braun panel); links by code work.

## States specific to the Cabinet
- **Empty cell** in a started stage: outline, no number, not tappable.
- **Future stage:** outline row, "not yet" in the first cell; tapping the row label says what will go there.
- **A cell with only dropped items:** count in ink 2 with a small "dropped" under it.
- **Scrubbed to the past:** a bar under the lamp line "As it stood · 12 Nov · back to now" (tap to return). Lamp shows nothing while in the past (the lamp is about now). Unseen dots hidden. Cells that had items then but whose files weren't kept show the count from the records with "·not kept".
- **ON while scrubbed to the past:** new events don't move the view; the "back to now" bar gains "· 1 new".
- **Big counts** (100+): shows "99+"; drawers over 30 items group with headers.
- **Tablet:** desktop layout from 768 px.

## Weak spots I see
- J4 needs a second place (the history list) even though the scrubber exists; the scrubber is the gesture, the list is where you read.
- J13 by code has no input. Fine for him (he doesn't know codes); a problem only for others.
- On ON, a cell count rarely changes (revs don't add items), so liveness rests on dots, the lamp and the newest strip.
