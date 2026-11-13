# How it looks and feels: shared by every concept (C Cabinet, E Herbarium; D The Set killed, see common-how-it-works.md)

Product designer (visual focus), concept turn 1, 2026-11-13. Read with `common-how-it-works.md` (systems). Each concept's own `how-it-looks-and-feels.md` covers its landing and its screens; everything here is the same in all three. The shared system from jam turn 2 (palette, Inter, the lamp, greyed-never-removed, A/B that keeps the playhead) is settled and only restated where it changed.

## What changed since the jam, and why (owner, 13 Nov, all in `owner.md`)
| Owner said (verbatim) | What it changes in the look |
|---|---|
| "why would i need to read an a3 sheet properly on my phone? i just need to see everything properly on my phone." | **Read mode is dropped.** I proposed it in jam turn 2; the director allowed it. It's a feature for one kind, and he asked for every kind to work. No region sidecars needed. Pushing back on `common-how-it-works.md` §5, which still lists read mode: please remove it. |
| "why make anything on a3 at all? im not in europe and im not printing" | A3 is **legacy**, not the main shape. Existing sheets show as they are, labelled `legacy sheet`. Nothing in any layout assumes a 1.414 landscape box (E's mount was going to; it no longer does). |
| "dont do phone first -- do images that will be great on the site that i can view responsively" | **No size leads.** Every frame is drawn at phone (390 × 844) **and** desktop (1440 × 900), both at 1:1. Each concept states its layout at phone, tablet and desktop. |
| "i really only want images for things that need to be images -- text should be html and stuff" | **Text is HTML everywhere**: labels, slips, docs, records, test results, version notes. Images are only renders, drawings, diagrams, plots (and the legacy sheets). Kinds collapse to **image · doc · test · record** (see "For systems" below). |

## Frames (rev 2, all real content, 9 frames at phone and desktop)
| Concept | Phone (1–7, 9; 9 as a full scrolled page) | Desktop (1–7, 9; 8 = desktop 1) |
|---|---|---|
| C Cabinet | `cabinet/frames.png` (+ extra: scrubbed to Round 2) | `cabinet/frames-desktop.png` |
| E Herbarium | `herbarium/frames.png` | `herbarium/frames-desktop.png` |

Source: `_frames/round2.py` (with `lib.py`). The round 1 scripts (`cabinet.py`, `herbarium.py`, `desktop.py`, `the_set.py`) are kept for the record and write `*-r1` files. D's round 1 frames stay in `the-set/` as the record of a killed concept.

**The newest work in every landing is BUTTERFLY rev A**, a real new-format group from the branches round: `design/branches/concepts/butterfly/img/*.jpg|png` (made from `_mock-src/out/rb_bf_*.png` by `figs_rb.py`), with words from its `how-it-works.md`. I used a real group instead of the steer's example "FOLD rev D", which doesn't exist. Frame 2 shows the moment BUTTERFLY rev A lands. Flag for systems: the branch docs don't yet place their images (`![…](img/…)`), so under the group rule none of them is an item yet. The branches team should add the image lines, or the site has nothing to show. Real content: v1 / v1.1 / archive sheets, golden and perturbed `voice_bass_pluck.wav` (one shared scale, so the louder run looks louder), `metrics.json` numbers, `owner.md` words verbatim, `scores.md` round 2. Counts come from a repo survey on 13 Nov (approximate until backfill). D-codes are illustrative.

**Phones are drawn inside real browser chrome**: iOS status band (47 px) and Safari's bottom bar (83 px). The no-scroll area is **714 px**, not 844. Every no-scroll landing fits 714. The claude.ai artifact page may add its own chrome; **builder: measure it on a real phone** and tell us if 714 shrinks.

## The rev letters in the frames
The test script said "FOLD-D rev H". By the numbering rule, FOLD-D's real revs are v1 = A, v1.1 = B, so the next one is **rev C**. The frames use rev C so the letters agree everywhere. Backfill I used: FOLD-A/B/C rev A = round-5 archive form, B = v1, C = v1.1; FOLD-E the same (it has an older archive form); FOLD-D, HUSH, ONE SHEET: A = v1, B = v1.1. **HUSH-C and ONE SHEET-C stay at rev A**: their v1 → v1.1 pixel difference is 0.07%, the footer line only (checked). That's the systems rule working: a byte change isn't a rev.

## Shared visual system (settled; restated where it changed)
- **Palette:** ground `#E6E4DF`, cell `#EFEDE9`, paper `#F8F7F4` (new: the ground for slips and for docs shown as pages), rule `#C4C1BA`, ink 2 `#5F5D58`, ink `#1B1B19`, ON `#23863F` (lamp only). No red or orange in the frame.
- **Type:** Inter, self-hosted subset (assets), tabular figures. Phone: 22 project name · 16–17 item title · 13–15 body · 12–12.5 meta · 10.5 caps label. Desktop: 26–28 name, 17–20 titles, 13–15 body. Decisions in his words are **body size, verbatim** (director ruling), 600 weight when they're the subject of the screen.
- **Lamp:** ON (steady green, one 600 ms dip per event, drawn mid-dip in each frame 2), STANDBY (hollow ring), SNAPSHOT (a short rule, no lamp, "Snapshot · 13 Nov 14:02"), plus systems' Connecting / Live paused (ink 2 text, no lamp).
- **Unseen:** a 6 px ink dot (C, E) or a Δ (D). Never green.
- **Dropped:** 40% opacity + the word "dropped". Opened, a dropped item shows at full strength.
- **A lock** is a ruled, signed line: two 1.5 px ink rules 4 px apart above the version name.
- **Grid:** 8 px base. Phone 16 px margins. Desktop 48 px margins, 12 columns in 1344.
- **Breakpoints:** phone < 600 px (one column) · tablet 600–1023 (each concept says) · desktop ≥ 1024.

## The concept group page (frame 9; shared, drawn the same in C and E)
The screen that answers "images only for things that need to be images".
- **Top:** group label: code 15/700 + "rev A", "concept group · 6 images · 1 doc · exploring", the rev slip on paper ground, then "grew from ONE SHEET · v1.1 (legacy sheets) ›". Then its one line at 15 px.
- **Body = the group's main doc as HTML, in its own order:** `##` headings at 16/600, paragraphs and numbered lists at 14/21, and each image where the doc places it, at its own shape, full width, with its alt text and sub-type as a caption under it (11.5/500, ink 2: "the joint, close · render", "rear section · drawing · 24 px/mm"). No image carries a caption inside it.
- **Phone:** one column, text and images interleaved (drawn full length, 390 × 1900, fold marked at 761).
- **Desktop:** in E, images on the left up to 940 px, the text section beside the image it follows in the right column (372), label top right. In C, inside the 792 px work side: the label and one line, then sections, each image at full width under its text.
- **Group rev row** at the end: rev letters with dates, "r1–r4 not kept" where relevant. Tap a rev → the group as it was.
- Drawings with labels baked in (the rear section has its callouts in the image) are acceptable as *drawings*: a dimensioned section is a thing that needs to be an image. Renders carry no text.

## Doc tiles (anywhere a doc is shown small)
Paper ground `#F8F7F4` with a 1 px rule. The code (11/700, ink 2), the title (11.5–12.5/600, up to 3 lines), and one line of ink 2 text if there's room. It's never a shrunk page.

## The decisions register (frame 5; from D, shared)
Grouped by day ("13 NOV" label). Each entry: "asked: …" (12, ink 2, if the record has a question) → his words verbatim (14, ink 2; **16/600 ink for the open one**) → "after: D-019" or, when open, "time not recorded" and rows "before D-031 Pin check…" / "after D-032 …" / "after D-019 Budget variant spec · rev 13", with codes 700 and titles underlined as links. 1 px rules between entries. C reaches it with "decisions ›" above the scrubber; E with the "decisions" filter.

## The item viewer (both concepts; drawn in each frame 3 and 4)
- **Image** (render, drawing, diagram, plot, legacy sheet): shown at its own shape, full available width. Phone: pinch and double-tap to zoom to 3200 px, turn the phone for edge to edge. Desktop: full content width up to 1600 px; `Z` = 1:1 with drag-pan; ← → steps to the next image in the set. "download original" in the label's meta line.
- **Show changes (from D):** a toggle under the compare ("Show changes from rev B", a 44 × 20 ink switch; off by default) with a line naming what changed ("6 areas: joystick, closed view, effects text, footer"). On, ink scallop outlines (1–1.4 px, bump radius 3–6 px by size) mark the changed areas on both forms. The areas come from `build.py`'s pixel diff of two same-size forms (threshold, plus a cap: "too many changes to mark"). Frame 3 uses the real FOLD-A v1 → v1.1 diff.
- **Compare (J10):** phone = **wipe** (a vertical 1.5 px ink hairline with a 26 px white round handle, `‹›` in it). Desktop = **side by side**, synced zoom and pan. Labels under each: "v1.1 · rev C · current" / "v1 · rev B".
- **Lineage row:** the same image small, oldest left, each labelled with its rev; the selected form has a 2 px ink frame; **missing rounds are one dashed rule with "r1–r4 / not kept"**, never a blank tile per round.
- **Doc / record:** HTML, one column, measure ≈ 66 characters on desktop, full width on phone (≈ 45 characters at 15 px, fine). Tables in eng docs scroll sideways inside their own box (a real issue: `budget-variant.md` has wide tables); code blocks the same. `##` headings as a jump list at the top of long docs.
- **Test:** result in words first (`RAN` / `PASS` 500 / `FAIL` 700, first in its group), the numbers from `metrics.json` as one meta line, then the sound block (`cell` ground: 44 px round play/pause, static peak-line waveform, hairline playhead, time in tabular figures, **A/B as two words with a 2 px underline** under the one playing; switching keeps the playhead), then plots as images.
- **Motion (all of it):** new row/strip/slip inserts with 180 ms ease-out height + fade; the lamp dip; the lamp's 1 s fade to standby; image cross-fade 180 ms when a newer rev replaces one on screen; wipe and scrubber follow the finger with no easing. `prefers-reduced-motion` → instant.

## For systems (rev 1 flags: all ruled by the director in steer 1; kept for the record)
1. **Kinds:** with text as HTML, "sheet" and "diagram" are both just *images* to him. I'd make the kinds **image · doc · test · record**, with the image's sub-type on its label (render, drawing, diagram, plot, legacy sheet). C's cabinet is now three columns: images · docs · tests.
2. **"Stage = the stage it was made in"** puts all of `eng/` (the spec, rev 14) under Concept, leaving the Spec row empty, which reads wrong. I drew the 19 eng docs under Spec, marked "early" (begun before Handoff). Please decide the rule; I'd use *the stage the item serves*.
3. **"Now"** needs a definition. I drew **Lock** as now (v1.1 locked; waiting on his pick to open Handoff). Systems' E doc said Concept. One rule, please: probably "the latest stage with a locked output, until the next one starts".
4. Read mode out of `common-how-it-works.md` §5 (owner 12:13).

## Open questions
- Measure the claude.ai artifact chrome on a phone (does 714 px hold?).
- J12 ("since you last looked") is still waiting on the owner; every concept shows it, and every concept has a fallback ("+ 6 more on 13 Nov") if he drops it.
