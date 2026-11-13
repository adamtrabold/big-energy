# E · Herbarium — how it works

Product designer (systems focus), concept turn 1, 2026-11-13. Work-first: every item is mounted as itself, with one label in the same corner, revisions as slips on the label, and lineage by repetition beneath. One column, max 600 px, at every size. The word "herbarium" never appears on screen. Shared viewer, lamp, links and states are in `../common-how-it-works.md`.

Draw for this turn (Python `SystemRandom`): Oblique "Only one element of each kind". Applied: under the newest specimen, the landing shows **one of each kind**: the latest sheet, diagram, doc and test, small. So the first screen answers "is there a new test?" without scrolling a feed of sheets. (Records aren't in the row; decisions have their own way in, below.)

## Reshaped from the jam (and why)
1. **Decisions are specimens too.** A decision isn't a file, but it's the thing that explains the work. A decision specimen = his words, verbatim, on the label (body size, per the ruling), with the items it caused mounted small underneath. It sits in the column at its date like any other specimen. That answers frame 5 and keeps "history lives on the thing" honest.
2. **Stage gets a strip** (director must-prove 2): the nine stage words in one line under the lamp, the current one marked, done ones in ink, future in ink 2. Tap a word → the column filtered to that stage. It's the only stage display; it's always there.
3. **Versions are filtered sets with a cover** (must-prove 1): "v1.1" in the line under the name is a link. The v1.1 view opens with a cover label (version · date · one line · what changed from v1) then its items as small specimens grouped by concept: the track list, as specimens.
4. **Slips show 2, fold the rest** (must-prove 4): at landing size the label shows the current rev slip and one older slip, then "+4 earlier". That keeps "it's a record, not a gallery" visible without a tall label.

## Structure
Landing, phone, no scroll:
1. Lamp line (common §2).
2. Name; "v1.1 current · waiting on you: ONE SHEET or FOLD".
3. Stage strip.
4. **Newest specimen, large**: the work at column width (sheet fit-width, test as waveform with play, doc as its first page set as text, diagram as image), label in its corner: code · title · kind · stage · rev · date · status; top slip "rev H · 14:02 · stands at 120°", one older slip, "+n earlier".
5. "+ 6 more since you last looked" (J12; becomes "+ 6 more today" if J12 goes).
6. **One of each kind** row: sheet · diagram · doc · test, small, each with its code.
Scroll: the column continues, newest first, one specimen per item (an item appears once, at its latest rev; earlier revs live on its slips and lineage). Dropped items appear at the date they were dropped, greyed, labelled.

**Filter row** (sticks under the lamp line after scrolling): `all · stage · kind · version · decisions · history`. One at a time. Each has its own URL. `history` turns the column into the three-grain history: switch **Day · Round · Version** at the bottom, dividers by day / round / lock, locks as ruled signed lines, decisions as decision specimens.

Item opened: the specimen at full width, the common viewer, slips unfolded (all revs), lineage row below. Desktop: the 600 px column centred on the ground; opening a sheet widens just that sheet to the viewport (up to 1600 px) with the label staying in the column's corner; compare puts two forms side by side at that width.

## Flows and the 8 frames
| Frame | Path | Taps |
|---|---|---|
| 1 STANDBY | Ring lamp "Standby · last 14:02"; name; waiting on you; stage strip (Lock marked done, Concept current until handoff); newest specimen FOLD-D rev H; one-of-each row. | 0 |
| 2 ON, event lands | Lamp ON dips. The new rev slides in as the **newest specimen** (the old newest drops to the column), slip "rev H · just now". If not yet published: the specimen frame holds the label and "image arriving with the next publish" (no fake image). "+ 7 more since…" ticks. | 0 |
| 3 FOLD-A v1.1 → v1 | "v1.1" link (1) → FOLD-A in the set (2) → lineage row: v1 (3) → compare. | 2 to v1.1, 3 to v1 |
| 4 Bass pluck A/B | One-of-each "test" tile, if it's the latest test (1); otherwise filter kind → test (1, 2) → Bass pluck (3) → play, A/B. | 1–3 |
| 5 "Switch to Daisy Seed" | Filter "decisions" (1) → scroll to 13 Nov → decision specimen with its caused items mounted under it → tap one (2). Also: opening D-0xx daisy-first-principles shows "caused by: 'Switch to Daisy Seed' · 13 Nov" on its label. | 2 + scroll |
| 6 What's in v1.1 | "v1.1" (1) → cover + track list as specimens. | 1 |
| 7 Snapshot | No lamp; "Snapshot · 13 Nov 14:02"; no "since you last looked" line; the rest identical. | 0 |
| 8 Desktop | The column centred on wide grey; newest specimen large; nothing in the side fields. | 0 |

Other jobs: J2 all items in the column, archive greyed at their drop date. J8 copy link on every label. J9 status on every label. J13 stage/kind/version filters; by code via link only.

## States specific to the Herbarium
- **Doc as a specimen**: first heading + first ~12 lines set as text on a sheet-shaped ground, "D-014 · doc · 3 pages" on the label. Must look like a mounted page, not a text snippet.
- **Record as a specimen**: same as a doc. Records don't appear in the main column (they'd flood it each time owner.md changes); they show under `kind → record` and in history.
- **Test with no sound** (plots only): the plot is the specimen.
- **Missing old forms**: lineage row shows "r1–r4 not kept" as one gap; the slips list starts at the earliest kept rev with a slip "earlier revs not kept".
- **Empty stage tapped in the strip**: column says "Boards · not yet · PCB layouts, board photos and test results will go here".
- **Filter with nothing in it** (e.g. kind=diagram at Spec): "nothing here yet" + the filter stays.
- **Long day of events**: the column groups same-session revs of one item into one specimen (latest rev) with slips for each.
- **Wide screens**: column stays 600 px. Tablet the same.

## Weak spots I see
- J6 rests on one line of words; it never shows the level the way C does.
- Scrolling is the main way to browse; finding something old means filters, not position.
- Doc specimens may read as text boxes; the visual designer needs to prove a doc looks mounted.
- Many revs to one sheet in a session could make the column feel repetitive; grouping by item (latest rev only) is what stops it.
