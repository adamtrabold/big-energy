# E · Herbarium — how it looks and feels

Product designer (visual focus), concept turn 1, 2026-11-13. Read with `how-it-works.md` (systems) and `../common-how-it-looks-and-feels.md`. Frames: `frames.png` (phone 1–7, desktop landing), `frames-desktop.png` (desktop 1–7). All at 1:1. The word "herbarium" never appears on screen, and there's nothing botanical in it.

**The idea in one line:** every item is shown as itself, as large as the screen allows, with one label in the same place and the same fields for every kind. Revisions are slips on that label.

## Why it fits the owner's newest words best
"i really only want images for things that need to be images -- text should be html". E is the concept where that rule is the layout: the **image is shown alone**, and everything about it (code, kind, stage, status, every rev's one line, his words on a decision) is **HTML text on the label beside or under it**. A doc isn't a picture of a page: it's real text set on paper ground. A test's "image" is its sound.

## Reshapes
- **The 600 px column is gone on desktop.** It was the director's twist, and I drew it first (`frames.png` desktop notes keep the verdict). At 1440 it left 840 px of grey and showed a legacy sheet smaller than a phone in landscape. Owner: "images that will be great on the site that i can view responsively". Now:
  - **Desktop:** the work takes ~940 px on the left (as large as its shape allows, height-capped to the fold). The **label sits in the bottom-right corner beside it** (372 px), which is where a herbarium sheet's label sits. "Newest of each kind" fills the space above the label. Below the fold, everything else, newest first, three across.
  - **Tablet:** work full width, label below, two across under it.
  - **Phone:** work full width (358), label below, one column.
- **No standard mount shape.** Each item shows at its own shape (legacy A3 landscape, a future portrait render, a square diagram), full width, height capped at about 60% of the viewport. The standard is the **label**, not the box. (A fixed A3 mount would have built the dropped format into the layout.)
- **Newest of each kind: three tiles** (image · doc · test), was four. Kinds follow the owner's image/text rule.
- **Stage is a level strip, not a line of words** (director: J6 was E's weak spot). Nine 6 px segments: ink for done/now (Concept, Lock), an outline for begun early (Spec), rule grey for not yet; the now segment has a 2 px underline. One line under it: "Lock · 2 of 9 · Spec begun early · next Handoff". Tap → the column filtered to a stage. On desktop it sits top right with room to breathe.

## Director's must-proves
1. **Versions:** "v1.1 current" under the name is an underlined link (1 tap, frame 6). The version's cover is a label with no image: the lock rule (double ink line), "v1.1" 26/700, "locked 13 Nov · current", the one line. Then **the set as images**, grouped by concept: 2-up on a phone, 4–5 across on desktop. That's the track list you can see, with its own URL (`#/v/v1.1`).
2. **Build-chain stage:** the level strip, on every landing at every size (above).
3. **A doc and a test make good specimens:** frame 5 shows docs as pages: paper ground `#F8F7F4`, title 600, first lines in real text, cut cleanly at the edge, no fade. Three across on a phone they're notes-sized (7 px type: a glance, not a read). On desktop at 13 px they're **readable in place**. Frame 4: a test's specimen is the sound block, play + waveform at full width (phone 200 px tall, desktop 940 × 360) with A/B under it, and the plot follows as a second image. Both carry the same label as an image does.
4. **Not just a gallery:** the label + slips + lineage are visible at landing size. Under the newest image: code 15/700 + title, "legacy sheet · Concept · exploring", then **slips**: 24 px strips with a 1 px rule, newest on top on paper ground ("rev C · 14:02 · round 6"), the next one unfilled in ink 2 ("rev B · 13 Nov · v1.1 · shows MIDI IN"), then "+ rev A (v1) · r1–r4 not kept". An image with a dated record stacked on it reads as a record, not a feed of pictures. Opened (frame 3), all slips unfold and the **lineage row** repeats the same image small (rev A · not kept · rev B · rev C) so the eye catches what moved.

## Phone (390, 714 px usable), top to bottom
Lamp line → name 22/600 + "a portable Model D · v1.1 current" (link underlined) → Waiting on you label + "ONE SHEET or FOLD" 16/600 → level strip + its line → **the newest image** full width → label and two slips → "+ 6 more since you last looked ›" 13/600 → Newest of each kind (three 114 px tiles: image, doc as a page, test as a waveform; code + kind under each, 11/600). It fits 714. Scroll: the rest, one item per row at its latest rev. The filter row (all · stage · kind · version · decisions · history; the selected one 600 with a 2 px underline) sticks to the top after scrolling (shown in frames 5 and 6).

## Desktop (1440 × 900)
Top band: lamp line, name and project line left; Waiting on you centre; level strip right. A hairline, then the filter row with "+ 6 more since you last looked ›" right-aligned. Then the newest work left and Newest of each kind + label right (label bottom-aligned to the image's bottom edge). Desktop frame 3: two forms side by side across the full 1344 px, the label under the left one, lineage under the right. Frame 5: three doc pages large, the decision label in the right column.

## Frames and taps
| Frame | What it shows | Taps |
|---|---|---|
| 1 Standby | as above | 0 |
| 2 On, FOLD-D rev C lands | lamp mid-dip; the image cross-fades; a new slip "rev C · just now" lands on top, the old top slip steps down; unseen dot; "+ 7 more". If the event comes before the publish, the label and slip appear and the image area says "image arriving with the next publish" (no stand-in picture) | 0 |
| 3 FOLD-A v1.1 → v1 | wipe / side by side; slips unfolded; lineage by repetition | 3 |
| 4 Bass pluck A/B | sound as the specimen; RAN slip | 1–3 |
| 5 "Switch to Daisy Seed" | filter "decisions"; D-031, D-032 and D-019 mounted as pages; his words 17/600 on the label; "time not recorded"; the ask on a slip | 2 + scroll |
| 6 What's in v1.1 | cover label + the set as images | 1 |
| 7 Snapshot | no lamp, no dot; "+ 6 more on 13 Nov" | 0 |
| 8 Desktop | work left, label bottom-right | 0 |

## How it feels
Like walking up to a wall of work and reading the cards. Calm, and the work comes first. Updates are physical: a slip lands on the stack. It's the most enjoyable of the three to open, and it's the one he can show someone.

## Weak spots (being hard on it, as the director asked)
- **Legacy sheets all look alike at a glance.** FOLD A–E are all walnut on cream; in the v1.1 grid the codes do the telling. New screen-made images (separate renders, diagrams) will differ more, but today's archive is a lot of similar brown.
- **J6 is a strip, not C's level of detail.** It shows where the build stands, not how much is in each stage.
- **Finding old things is by filter, not by place.** There's no "where is it" map like C's cabinet. The "Go to" code field from D would help (if D is killed, I'd move it into E's filter row).
- On a phone, doc pages in a 3-up row are glances; reading means one tap.

## My lean
**E first, C second, kill D.** E answers the owner's last three messages (responsive, images only where they need to be, text as HTML) in its structure. C is the better *reading of where things stand*; if the director wants one thing from C inside E, it's the scrubbed R2 view as a history grain.
