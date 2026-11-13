# C · Cabinet — how it works

Product designer (systems focus). Rev 2, concept building systems turn 2, 2026-11-13. Structure-first: the landing is a reading of where the project stands, with the newest work beside it. Shared viewer, codes, concept groups, lamp, links and states: `../common-how-it-works.md`. Look: `how-it-looks-and-feels.md`.

Rev 1 draw (Python `SystemRandom`): Oblique "Only one element of each kind" → **one control per question**: where is it? the cabinet. When was it? the scrubber. Is anyone working? the lamp.

**Changed since rev 1:**
- **Columns: images · docs · tests** (visual's reshape, director's kinds ruling). Records stay out of the grid (reachable from history and decisions).
- **The Concept row is one wide drawer of concept groups**, like Lock is a wide drawer of versions. New: concept work now arrives as groups (images + docs together, common §3), and splitting a group across an images cell and a docs cell would tear apart exactly what the owner asked to see together. The kind columns apply from Spec on, where items are loose (eng docs, plots, tests). The cell reads "7 concepts · 3 current · 1 round running"; the drawer lists groups (current, exploring, dropped). Visual: please draw it; if it breaks the grid's reading, say so and we go back to counts per kind with drawers grouped by concept.
- **Not-yet rows collapse into one line** in ink 2 below the level line: "BOM · Breadboard · Boards · Prints · Assembly — not yet" (director's item for visual; I agree on how it works: tapping the line expands the rows; each stage gets its own row the moment it has an item or becomes now/next). Handoff stays its own row because it's **next** ("starts when you pick").
- **Stage = the stage served.** Spec row holds the 19 eng docs and the sims (tests), marked "early". **Now = Lock.**
- **Scrubber detents: rounds and locks only** (visual: 45 decisions in ~30 hours would put ticks 7 px apart). Decisions live in the decisions list (common §7), one tap from the landing via "decisions" beside "history".
- **Scrubbed state has its own URL** (`#/h/round/2`), and shows the round's record (concepts and scores, their fate today), not a fake grid of files that weren't kept.
- **The newest work is shown, not just named**: phone, the Newest strip becomes full width under the cabinet (using the ~140 px freed by collapsing not-yet rows); desktop, it's open on the right.

## Structure
**Landing**, top to bottom:
1. Lamp line (common §4). STANDBY: "Standby · last: FOLD rev D · 14:02".
2. Name; "a portable Model D · v1.1 current" (link).
3. Waiting on you: "ONE SHEET or FOLD".
4. **Cabinet**, rows in build order:
   - Concept: wide drawer "7 concepts · 3 current · branches running" (dot if unseen).
   - Lock: wide drawer "v1.1 current · 2 versions". **Level line under Lock (now).**
   - Handoff: wide row "next · starts when you pick".
   - Spec (early): images · docs · tests counts, in ink 2 with "early".
   - One line: "BOM · Breadboard · Boards · Prints · Assembly — not yet".
5. **Newest**: the newest work (a group's lead image, or a loose item) at full width on phone, with its label line (code, rev, time, kind/stage) and "+ n unseen".
6. **Scrubber** (thumb zone): rounds short ticks, locks and now long ticks; "history ›" and "decisions ›" above its right end.

**Drawers:**
- Concept → groups, current first: each a row with its lead image small, code, rev, status, one line ("FOLD · rev C · locked in v1.1"). Tap → group (F9, common §3).
- Lock → versions, newest first, each with its lock rule and one line. Tap → version.
- Stage × kind (Spec on) → items, newest first: images as a 2-up grid, docs and tests as rows (code, title, rev, status).

**Group open (frame 9):** the shared group view (common §3): label + group rev row, the main doc as HTML with its images placed in it, further docs. Desktop: in the detail side (792 px), images at full detail width, text under each image it follows; the cabinet stays put on the left.

**History** (from "history" or a tick): grain switch Day · Round · Version; decisions verbatim with what they caused; locks as ruled, signed lines; "the records" (R-codes) listed at the top. **Decisions** (from "decisions"): the shared list.

## Sizes
| | Phone < 600 | Tablet 600–1023 | Desktop ≥ 1024 |
|---|---|---|---|
| Landing | stacked as above; Newest full width | cabinet left half, Newest right half | cabinet panel left 520 px; newest work open on the right 792 px; scrubber full width at the bottom |
| Drawer / item / group | replaces the landing, "‹ back" line | opens in the right half | opens in the right 792 px; left never moves |

## Flows and the 9 frames
| Frame | Path | Taps |
|---|---|---|
| 1 STANDBY | Landing; ring lamp; waiting on you; level under Lock; Spec early; not-yet line; Newest = a new-format group's lead render (visual picks the real one from `_mock-src/out/`). | 0 |
| 2 ON, group rev lands | Lamp dips; Concept drawer gets the dot; Newest cross-fades to "FOLD rev D · just now"; "1 unseen". Counts don't change (a rev isn't a new group). Not yet published → Newest shows the label and "images arriving with the next publish". | 0 |
| 3 FOLD-A v1.1 → v1 | "v1.1" (1) → the set: FOLD-A shown under FOLD (2) → lineage: v1 (3) → compare, "show changes". Via the cabinet: Concept (1) → FOLD (2, group at rev C) → FOLD-A (3) → v1 (4). | 2 / 3 (within budget either way) |
| 4 Bass pluck A/B | Spec·tests (1) → T-004 (2) → play, A/B. | 2 |
| 5 "Switch to Daisy Seed" | "decisions" (1) → scroll to 13 Nov · time not recorded → before D-031, after D-032, D-019 rev 13 → tap (2). | 2 + scroll |
| 6 What's in v1.1 | "v1.1" (1) → cover (lock rule, one line, changed from v1) → groups HUSH@B, ONESHEET@B, FOLD@C with their sheets, shared docs, spec rev 14. | 1 |
| 7 Snapshot | No lamp, no dots; "Snapshot · 13 Nov 14:02". | 0 |
| 8 Desktop | Cabinet left; newest group open on the right; scrubber across the bottom. | 0 |
| 9 Concept group | Newest (1) → the group. | 1 |
| extra: scrubbed | Drag to R2 → "As it stood · Round 2 · 12 Nov · back to now ›"; the round's record: TYPE CASE 9, HYMNAL 9, HUSH 8, FOLD 7, ONE SHEET 7, UNDER GLASS 6, each with its fate today; "sheets from rounds 1–4 weren't kept". URL `#/h/round/2`. | drag |

Other jobs: J2 every item is in a drawer, a group or history; archive groups sit in the Concept drawer, greyed. J6 the cabinet itself. J8 copy link on labels, groups, versions; `#/s/spec`. J9 status in every row. J13 by stage+kind in 2 taps. J14 phone layout above. J15 frame 9.

## States specific to the Cabinet
- **Empty kind cell** in a started stage: outline, no number, not tappable.
- **A stage starts** (e.g. Handoff when he picks): it gets its own row; the level line moves under the stage that has a locked output; "next" moves down one.
- **Not-yet line expanded:** each future stage as its own outline row; tapping one says what will go there.
- **Cell with only dropped items:** count in ink 2 with "dropped".
- **Scrubbed to the past:** a bar replaces the lamp line ("As it stood · Round 2 · 12 Nov · back to now ›"); no lamp, no dots; ON events don't move the view, the bar gains "· 1 new".
- **Big counts:** "99+"; drawers over 30 items get group headers.

## Weak spots
- With Concept, Lock and Handoff as wide rows and future stages on one line, today's "grid" is mostly a list; the grid earns its form only as later stages fill. Honest, but it may read as less of an instrument now than in the jam.
- J4 needs a second place (history/decisions) besides the scrubber.
- On a phone the work is below the reading, so looking at work is always one step behind where things stand.
