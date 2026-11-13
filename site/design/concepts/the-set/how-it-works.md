# D · The Set — how it works

Product designer (systems focus), concept turn 1, 2026-11-13. Document-first: the site is a drawing set. Every publish is an issue; every item has a number and revs; the landing is a title block and a revision table. Shared viewer, lamp, links and states are in `../common-how-it-works.md`.

Draw for this turn (Python `SystemRandom`): Oblique "Use an unacceptable colour". The unacceptable mark in a drawing set is the **revision cloud**: the scalloped outline drawn around what changed on a sheet. Applied as a function, not a colour: **D shows where a sheet changed**, on the sheet. `build.py` diffs consecutive revs of the same sheet (same pixel size: the A3 renders are) and writes the changed regions as boxes; the viewer can draw them. That makes D the strongest J10 answer: not just "rev F" but *there*. The colour of the cloud is the visual designer's call (I'd stay in ink; the "unacceptable" part is the scalloped shape itself, in a frame with no ornament).

## Reshaped from the jam (and why)
1. **Sections are stages, not a mix.** The visual sketch had Design · Tests · Spec · BOM · Boards · Records, which mixes stages and kinds. A drawing set divides by discipline; here the discipline is the build chain. Sections: **Concept · Lock · Handoff · Spec · BOM · Breadboard · Boards · Prints · Assembly**, plus **Records** last (the set's general notes). Inside a section, rows sort by kind then code.
2. **Two numbers, kept apart.** *Issue* = a publish of the site (Issue 14). *Rev* = a change to one item (FOLD-A rev F). *Version* = a lock (v1.1). The revision table on the landing lists **versions and issues with something worth naming**, not every publish: a row per lock, plus the current issue. Issues without a named change don't get rows (otherwise 40 rows of "updated").
3. **Δ means "changed in an issue you haven't seen"** (J12). It carries the issue number, like a real set: Δ15. Signed out, Δ marks show changes in the **latest issue** instead (still meaningful to a guest, and to him if J12 goes).
4. **Rows stay textual** (director push 3). No thumbnails in the index. Images begin at the item.

## Structure
Landing, phone, no scroll:
1. **Title block** (ruled box): name "( name to come )" · project line · lamp line · "Issue 14 · 13 Nov 14:02" · "Current set: v1.1" · "Waiting on you: ONE SHEET or FOLD".
2. **Revision table** (3 rows visible): Issue 15 in progress (when ON) · v1.1 · 13 Nov · FOLD stands at 120°… · v1 · 13 Nov · first lock. "All issues" opens the full table.
3. **Sheet index, collapsed to sections** (director push 1): one row per section with item count and Δ count: "Concept · 61 · Δ3", "Lock · v1.1", "Handoff · not yet", … future sections in ink 2 with "not yet". Tap a section → its index.
Section index: rows `code · title · rev · date · status`, grouped by concept for sheets (current first, dropped greyed after), Δ at the left margin of changed rows. Desktop: the full index as one table (no · title · kind · rev · date · stage · Δ), sections as headers, title block top right as on a drawing.

Item: the common viewer, plus the item's own **revision table** (rev · date · one line · which version holds it) above the lineage row. Tap a rev row = tap the lineage form. **Clouds**: a "show changes" toggle on a sheet draws the changed regions from the previous rev; on compare, clouds show on both.

History (J4): "All issues" is the history at **Version** grain (locks + named issues). The grain switch **Day · Round · Version** sits at the top of that table. Day/Round rows list events; owner decisions as rows with his words verbatim (body size) and the caused codes as links. Decisions are also indexed in **Records → Decisions** (one row each: date · his words · codes).

## Flows and the 8 frames
| Frame | Path | Taps |
|---|---|---|
| 1 STANDBY | Title block with ring lamp "Standby · last: FOLD-D rev H · 14:02"; waiting on you; revision table; sections. | 0 |
| 2 ON, event lands | Title block lamp ON. Revision table top row appears/updates: **"Issue 15 · in progress · FOLD-D rev H"** in ink 2 (queued until published, then ink). Concept section's Δ count ticks 3 → 4. On publish, "in progress" becomes the date. | 0 |
| 3 FOLD-A v1.1 → v1 | Revision table "v1.1" (1) → v1.1 set index → FOLD-A (2) → its revision table: tap the v1 row (3) → compare, "show changes" draws the clouds. Or Concept (1) → FOLD-A (2) → v1 (3). | 2 to v1.1, 3 to v1 |
| 4 Bass pluck A/B | Concept (1) → T-00x Bass pluck (2) → play, A/B. | 2 |
| 5 "Switch to Daisy Seed" | Records (1) → Decisions (2) → the row "13 Nov · 'Switch to Daisy Seed' · D-0xx D-0xx spec" (scan) → tap a code (3). | 3 |
| 6 What's in v1.1 | Revision table v1.1 (1) → set index for v1.1: the track list as an index (concept, sheet, rev). | 1 |
| 7 Snapshot | No lamp; "Snapshot · Issue 14 · 13 Nov 14:02"; Δs = latest issue's changes; no "in progress" row. | 0 |
| 8 Desktop | Title block top right, revision table top left, full index below as a table. | 0 |

Other jobs: J2 everything is in some section index (archive in Concept, greyed). J8 copy link per row and label; issue links `#/h/version/14`. J9 status column. J13 by code is native here: codes are the row's first column and sort order; a **"go to"** field in the title block (type `FOLD-A`) is the one input, fits a register.

## States specific to the Set
- **Issue in progress with nothing queued** (session ON, no events yet): no row; the lamp alone says ON.
- **Long revision table**: the landing shows 3 rows; "All issues (n)".
- **A rev with no diff available** (first rev, or sizes differ, or old form not kept): "show changes" is hidden for that pair, with "no earlier form to compare" in the revision table.
- **Missing old forms**: revision table row "r1–r4 · not kept" (one row, ink 2).
- **Code not found in "go to"**: "No item FOLD-Z" under the field.
- **Empty section**: row "Boards · not yet"; tap says what will go there.
- **Sizes**: phone shows codes + titles, rev and date drop to a second line; tablet shows 4 columns; desktop the full table.

## Weak spots I see
- Least visual landing of the three by design; it wins only if names and revs are enough for him, which is the director's bet to test.
- "Issue" is a new number for him to learn; if he never cares about issues, they could hide behind versions entirely.
- Clouds depend on deterministic renders: if a re-render shifts pixels everywhere, the cloud is the whole sheet. `build.py` needs a threshold and a cap ("too many changes to mark").
