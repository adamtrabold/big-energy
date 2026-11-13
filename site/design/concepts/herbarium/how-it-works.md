# E · Herbarium — how it works

Product designer (systems focus). Rev 2, concept building systems turn 2, 2026-11-13. Rewritten to match the visual designer's reshaped layout (`how-it-looks-and-feels.md`) and the director's steer 1. Shared viewer, codes, concept groups, lamp, links and states: `../common-how-it-works.md`. The word "herbarium" never appears on screen.

**The idea:** every piece of work is shown as itself, as large as its shape and the screen allow, with one label in the same place and the same fields for every kind. Revisions are slips on that label. Work first.

**Changed since rev 1:**
- The 600 px column is gone (visual: it wasted desktop and shrank images; owner 12:39 "images that will be great on the site that i can view responsively"). No standard mount shape: the label is the standard, not the box.
- Newest of each kind is three tiles (image · doc · test); the doc tile is **real text** (code, title, one line), never a shrunk page.
- Stage is a level strip.
- Decisions use the shared decisions list (common §7), not doc cards or decision specimens.
- **The newest work is usually a concept group**, not a single sheet.

## Structure

**What "the newest work" is.** The subject of the newest event: for a group revised event, the **group**, shown by its lead image (the first image its main doc places); otherwise the item (an eng doc, a test, a diagram). A group's label is the group's: `FOLD · rev D · Concept · exploring`, its one line; its slips are group revs. Tapping opens the group (F9). Legacy sheets never lead unless a session revises one, and nothing new is made as a sheet.

**Landing**, top to bottom (layout per size below):
1. Lamp line (common §4).
2. Name; "a portable Model D · v1.1 current" (v1.1 links to the version).
3. Waiting on you: "ONE SHEET or FOLD".
4. **Level strip**: nine segments: done (ink), now (ink + underline), early (outline), not yet (rule grey); line under it: "Lock · 2 of 9 · Spec begun early · next Handoff". Tap a segment → filter by that stage.
5. **The newest work**: lead image at its own shape, full available width, height capped ~60% of the viewport. A docs-only group shows its doc's opening text on paper ground at readable size instead.
6. **Label**: code + title; kind/sub-type · stage · status; then **slips**: top slip filled ("rev D · 14:02 · round 6 · stands at 120°, new hinge"), next in ink 2 ("rev C · 13 Nov · v1.1"), then "+ rev B, A · r1–r4 not kept".
7. "+ 6 more since you last looked ›" (J12; "+ 6 more today" if J12 goes) → the list filtered to those.
8. **Newest of each kind**: image tile, doc tile (real text), test tile (waveform + result word).

Below the fold: everything else, newest first, **one entry per group or loose item** at its latest rev (a group appears once, not once per image). Dropped things appear at their drop date, greyed.

**Filter row** (sticks to the top once scrolled): `all · stage · kind · version · decisions · history`. One at a time, each with its own URL. `kind → image` lists images individually, for finding one picture. `history` = the three grains (Day · Round · Version switch), locks as ruled signed lines, decisions inline. `decisions` = the shared list.

**Group open (F9, frame 9):** group label (code, rev, stage, status, one line, slips) → the **main doc rendered as HTML, with its images where the doc places them**, each at its own shape → further docs (looks-and-feels, coverage) as text sections, collapsed after their first paragraph on phone → **group rev row**: rev D · C · B · A · "r1–r4 not kept"; tap one → the group as it was (legacy revs show their sheets) → tap any image → image viewer with its own lineage, compare and "show changes".

**Item open:** the work as large as it goes, label beside (desktop) or under (phone, tablet) with all slips unfolded, lineage row, compare (common §6).

## Sizes
| | Phone < 600 | Tablet 600–1023 | Desktop ≥ 1024 |
|---|---|---|---|
| Landing | one column: lamp, name, waiting on you, strip, work full width, label under, "+ n more", three tiles in a row | work full width; label under with the three tiles beside it | top band (name left, waiting on you centre, strip right); work ~940 px left; tiles above the label in the right 372 px, label bottom-aligned to the image |
| Below the fold | one per row | two across | three across |
| Group open | label, then images and text interleaved as the doc has them | same, wider | images left up to 940 px; each doc section in the right column beside the image it follows; label and slips top right |
| Item open | work, label under | work, label under | work left (up to 1600 for wide images), label right |

## Flows and the 9 frames
| Frame | Path | Taps |
|---|---|---|
| 1 STANDBY | Ring lamp "Standby · last BUTTERFLY rev A · 14:02"; waiting on you; strip at Lock; **newest work = BUTTERFLY rev A (branches round), its lead render large** (`design/branches/concepts/butterfly/img/butterfly.jpg`); label + two slips; three tiles. | 0 |
| 2 ON, group rev lands | Lamp dips; image cross-fades; slip "rev A · just now" lands on top, old top slip steps down; dot; "+ 7 more". Not yet published → label + slip + "images arriving with the next publish". | 0 |
| 3 FOLD-A v1.1 → v1 | "v1.1" (1) → in the set, FOLD's legacy sheets are shown individually under its heading: FOLD-A (2) → lineage: v1 (3) → compare, "show changes". | 2 to v1.1, 3 to v1 |
| 4 Bass pluck A/B | If it's the newest test: tile (1). Otherwise filter kind → test (1, 2) → T-004 (3). Play; A/B keeps the playhead. Stage: Spec, early. | 1–3 |
| 5 "Switch to Daisy Seed" | Filter `decisions` (1) → "13 Nov · time not recorded · 'Switch to Daisy Seed'", the ask above in ink 2, "before: D-031 · after: D-032, D-019 rev 13" → tap D-032 (2); its label shows "caused by: 'Switch to Daisy Seed' · 13 Nov". | 2 + scroll |
| 6 What's in v1.1 | "v1.1" (1) → cover (lock rule, v1.1, locked 13 Nov · current, one line, "changed from v1: …") → the set by group: HUSH@B, ONESHEET@B, FOLD@C (sheets as images, labelled legacy sheet), then shared docs and spec rev 14 as text rows. | 1 |
| 7 Snapshot | No lamp, no dots; "Snapshot · 13 Nov 14:02"; "+ 6 more on 13 Nov". | 0 |
| 8 Desktop | Top band; newest group's lead render ~940 px left; tiles + label right. | 0 |
| 9 Concept group | From the newest work (1): BUTTERFLY rev A: renders at their own shapes, its `how-it-works` as HTML beside (desktop) or between (phone) them, group rev row. | 1 |

Other jobs: J2 everything is in the list or a filter, archive greyed at its drop date. J6 strip + `#/s/<stage>`. J8 copy link on every label and group. J9 status on every label. J13 filters; links by code. J14 phone layouts above. J15 frame 9.

## States specific to the Herbarium
- **Docs-only group** (a branch with no images yet): the newest work is its doc's opening text at readable size; label says "no images yet".
- **Lead image dropped in the new rev:** the next image in doc order leads; the dropped one shows greyed in the group's rev history.
- **Records** don't enter the main list (owner.md changes too often); they're under `kind → record` and in history.
- **Test with plots only:** the plot leads.
- **Missing old forms:** slips start at the earliest kept rev with "earlier revs not kept"; lineage shows one gap.
- **Empty stage tapped:** "Boards · not yet · PCB layouts, board photos and test results will go here".
- **Filter with nothing in it:** "nothing here yet"; the filter stays.
- **Many revs of one group in a session:** one entry, latest rev, a slip per rev.

## Weak spots
- J6 is a strip: where the build stands, not how much is in each stage.
- Finding something old is by filter, not by place.
- Today's archive is mostly legacy sheets that look alike (walnut on cream); codes do the telling until new-format work builds up.
