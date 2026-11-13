# C · Cabinet — how it looks and feels

Product designer (visual focus). **Rev 2**, concept building round 2, 2026-11-13. Read with `how-it-works.md` (systems, rev 2) and `../common-how-it-looks-and-feels.md`.

**Frames (rev 2, all 1:1):** `frames.png` = phone frames 1–7 and 9 (frame 9 drawn as the full scrolled page, 390 × 1900, with the fold marked), plus the extra phone scrubbed to Round 2. `frames-desktop.png` = desktop frames 1–7 and 9 (frame 8 is desktop frame 1). Source: `../_frames/round2.py` (`python3 round2.py c`). Round 1 frames are superseded; their scripts now write `frames-r1*`.

**The idea in one line:** the landing is a reading of where the build stands, with the newest work shown beside it.

## What changed in rev 2 (director steer 1, systems rev 2)
1. **New-format work leads.** The newest work is **BUTTERFLY rev A**, a concept group from the branches round. Its lead image is `design/branches/concepts/butterfly/img/butterfly.jpg` (made from `_mock-src/out/rb_bf_main.png`): a real standalone render with no baked-in text. Its label and slip are HTML. FOLD-D (legacy sheet) no longer appears on any landing. Legacy sheets show only in frames 3 and 6, labelled `legacy sheet`.
2. **The wide Concept row works** (systems asked me to test it). Concept is one wide drawer: "18 concepts · 3 locked · 4 exploring" with "11 dropped ›" (desktop) or "›" (phone). I counted the groups: 3 locked (HUSH, ONE SHEET, FOLD), 4 exploring (BUTTERFLY, CHAMBER, DIPTYCH, RAIN), 11 dropped (FOLD113, TYPE CASE, HYMNAL, UNDER GLASS, 7 full-instrument concepts). The kind columns (images · docs · tests) start at Spec, with their labels sitting just above that row, so they never float over a wide drawer. **Verdict:** it reads as a status panel more than a grid, and that's honest for today. The grid's columns grow as stages start. Keeping a group in one drawer instead of splitting it across images and docs is right: it's what the owner asked to see together.
3. **Not-yet stages on one line** (director item 4): "BOM · Breadboard · Boards · Prints · Assembly — not yet ›" in ink 2. **It holds.** The level line under Lock and "Handoff · next · starts when you pick" keep the road ahead readable, and the line frees about 140 px.
4. **The newest work at full width on a phone**, in the space that line freed: the lead render at its own shape (358 × 224), then "BUTTERFLY rev A · 14:02" and "concept group · Concept · exploring · open ›". Everything still fits the 714 px no-scroll area with the scrubber. The round 1 weak spot ("the work is a 96 px image under a table") is fixed.
5. **Frame 3:** "Show changes" clouds on the compare (shared viewer, off by default, on in the frame).
6. **Frame 5:** D's decisions register, reached by "decisions ›" above the scrubber, next to "history ›".
7. **New frame 9:** the concept group page (shared with E; see common).
8. Stage = the stage served: tests sit under **Spec (early)** (T-004 Bass pluck). Now = Lock.

## Phone (390, 714 px usable), top to bottom
Lamp line (10.5 caps) → name 22/600 → "a portable Model D · **v1.1 current**" (underlined link) → hairline → "WAITING ON YOU  ONE SHEET or FOLD" on one line (label + 15/600) → **cabinet**: Concept (wide, `cell`) · Lock (wide, `cell`, "now", 3 px ink bar, then the 1.5 px level line) · Handoff (wide, outline, ink 2) · column labels · Spec early (3 outline cells, 19 docs, 7 tests in ink 2) · the not-yet line → **Newest** label ("1 unseen" right-aligned when there is any) → the lead render at full width → code 15/700 + "rev A · 14:02" → kind line → "history ›  decisions ›" → scrubber (rounds short, locks and now long, ink handle).

## Desktop (1440 × 900)
The cabinet panel stays on the left (520 px) and never moves. The right side (792 px) holds the work: on the landing, the newest group's lead render (792 × ~470), the group label + slip at the left under it, its one line on the right, then three more of its images small and "+ 3 more images · open group ›". Drawers, items, tests, decisions, versions and the group page all open on the right side. The scrubber runs the full width with dated detents. **Tablet:** cabinet 44% / work 56%.

What showed up when I drew it: under the cabinet, the left panel's lower half is empty grey on desktop now that the rows are wide. That's acceptable (it fills as stages start). If the director wants it used, the decisions list's newest two entries could sit there. I haven't drawn that.

## Frames and taps
| # | Phone and desktop | Taps |
|---|---|---|
| 1 | Standby; newest = BUTTERFLY rev A render | 0 |
| 2 | On; lamp mid-dip; unseen dot on the Concept drawer and on Newest; "1 unseen"; Newest cross-fades in | 0 |
| 3 | FOLD-A (legacy) v1.1 ↔ v1: wipe on phone, side by side on desktop, clouds on; label + slips; lineage rev A · not kept · rev B · rev C | 3 (4 via the cabinet) |
| 4 | T-004 Bass pluck: RAN, sound block, A/B, plot | 2 |
| 5 | Decisions register → "Switch to Daisy Seed": the question asked, his words 16/600, "time not recorded", before D-031 · after D-032, D-019 rev 13 | 2 + scroll |
| 6 | v1.1: lock rule, cover line, groups FOLD@C / HUSH@B / ONE SHEET@B with legacy sheets, shared docs as rows | 1 |
| 7 | Snapshot: no lamp, no dots | 0 |
| 8 | = desktop 1 | 0 |
| 9 | BUTTERFLY rev A group page | 1 |
| extra | Scrubbed to R2 (`#/h/round/2`): the round's scores and each concept's fate today | drag |

## How it feels
An instrument with the work beside it. The lamp says whether anyone's working, the cabinet says where things stand, the scrubber says when, and the newest work is now the largest thing on both sizes.

## Weak spots
- On desktop the left panel's lower half is empty.
- On a phone the Spec row and the not-yet line are the only "grid" left; C's instrument character depends on the build moving on.
- The scrubbed past is a second visual mode (a round's record, not the cabinet).
