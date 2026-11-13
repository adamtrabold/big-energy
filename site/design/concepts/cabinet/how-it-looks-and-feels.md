# C · Cabinet — how it looks and feels

Product designer (visual focus), concept turn 1, 2026-11-13. Read with `how-it-works.md` (systems) and `../common-how-it-looks-and-feels.md`. Frames: `frames.png` (phone 1–7, desktop landing, an extra phone scrubbed to Round 2), `frames-desktop.png` (desktop 1–7). All at 1:1.

**The idea in one line:** the landing is a reading, like a meter on a panel: where the build stands, how full each stage is, and the one newest thing to look at.

## Reshapes I take, and one I add
- Systems: records out of the grid, Lock and Handoff as single wide drawers, the newest strip, the level line, the scrubber over records. **Agree with all of it.**
- **Added: three columns, not four: images · docs · tests.** Owner, 13 Nov: "text should be html", images only "for things that need to be images". Sheets and diagrams are both images to him. Three columns are wider cells (90 px on a phone), the counts read faster, and the grid stops looking like a spreadsheet.
- **Scrubber detents: rounds and locks only** (8: R1–R5, v1, v1.1, now). Decisions aren't ticks: there are 45 in about 30 hours, which would put ticks 7 px apart on a phone.

## Director's must-proves
1. **Not a spreadsheet; it says what to look at.** The Newest strip (96 × 68 image, code, rev and time, kind and stage) sits right under the cabinet on the phone. On desktop the newest item is **open on the right at 792 px wide**, so the biggest thing on the screen is the work (frame 8 / desktop 1). Three columns instead of five and "not yet" written once per empty row, not a dot per cell, take away most of the table feel. Verdict from drawing it: on desktop the cabinet reads as a panel beside the work. On a phone it's still mostly words and numbers above one small image. That's this concept's honest limit.
2. **Empty rows read as level, not unfinished.** Rows above the 1.5 px ink level line (under Lock, the "now" stage) have filled `cell` drawers. Below it: outlines, ink 2, "not yet" once. Handoff reads "next · starts when you pick", which ties the road ahead to the one thing waiting on him. Spec's 19 docs sit below the level in ink 2, marked "early": work begun out of order, shown honestly rather than raising the level.
3. **The scrubber earns its cost: a real case** (extra phone, `frames.png`, right of the desktop). Drag to **R2 · 12 Nov**. A solid ink bar replaces the lamp line: "As it stood · Round 2 · 12 Nov · back to now ›". The cabinet gives way to that round's record: TYPE CASE 9, HYMNAL 9, HUSH 8, **FOLD 7, ONE SHEET 7**, UNDER GLASS 6. Each row has its fate today ("set aside later", "locked in v1, v1.1", **"now: one of your two"**). The two concepts he's choosing between were both 7s in round 2, and both 9s were later set aside. That's worth one gesture, and it's built from `scores.md`, not lost images. Keep it.
4. **Fewer columns:** done (above).

## Phone (390, 714 px usable), top to bottom
1. **Lamp line** (10.5 caps, +0.9 tracking): ring + "Standby · last FOLD-D rev C · 14:02", or green dot + "On · round 6 sheets · since 13:40", or a rule + "Snapshot · 13 Nov 14:02".
2. **Name** 22/600 "( name to come )", then 13 ink 2 "a portable Model D · v1.1 current".
3. Hairline, then **Waiting on you** label + "ONE SHEET or FOLD" 16/600, "then the name" right-aligned in ink 2.
4. **Cabinet**: column labels (caps), 9 rows × 34 px. Stage names 13.5 in an 88 px gutter. The now row is 600 weight with a 3 px ink bar in the margin. Drawers are 90 × 28 with 1 px rule outlines; filled ones are `cell` with a 16/500 tabular count. An unseen dot sits 10 px in from a drawer's top-right corner. The level line runs under Lock, full width.
5. **Newest** strip: label, image, code 15/600, "rev C · 14:02" 13, kind and stage 12.5 ink 2, `›`. "3 unseen" right-aligned on the label line when there are any.
6. **Scrubber** in the thumb zone: 1.5 px line, short ticks for rounds, long for locks and now, a 14 × 28 ink handle, labels 12 under. "history ›" sits above its right end (frame 5's way in).

Drawer open (phone): back line "‹ Concept · images". Images show as a 2-up grid grouped by concept (current first, dropped greyed after), docs and tests as rows (code 600, title, rev, status). Item and test screens: see the common viewer.

## Desktop (1440 × 900)
Master–detail: the cabinet panel (name, waiting on you, grid at 92 × 50 px cells) fills the left 520 px. A 1 px rule divides it from the **detail side (792 px)**, which shows the newest item by default, then whatever he opens: drawer, item, test, history, version. The scrubber runs the full width at the bottom with dated labels ("R2 12 Nov"). Nothing moves on the left when the right changes. **Tablet (600–1023):** the same, cabinet 44% / detail 56%; under 600 the phone layout.

## Frames and taps (same on phone and desktop)
| Frame | What it shows | Taps |
|---|---|---|
| 1 Standby | as above | 0 |
| 2 On, FOLD-D rev C lands | lamp mid-dip; unseen dots on Concept·images and Concept·docs; Newest swaps (180 ms cross-fade) to "rev C · just now"; "3 unseen". Counts don't change: a rev isn't a new item | 0 |
| 3 FOLD-A v1.1 → v1 | phone wipe / desktop side by side; lineage row rev A (archive) · r1–r4 not kept · rev B · rev C | 3 |
| 4 Bass pluck A/B | RAN · osc 110.0 Hz · env. peak 87 / 69 ms; perturbed playing at 0:00.6; plot below | 2 |
| 5 "Switch to Daisy Seed" | history, Day grain, 13 Nov: the ask (ink 2) → the decision 17/600 "time not recorded" → "It caused": D-031 (before), D-032 (after), D-019 rev 13 | 2 + scroll |
| 6 What's in v1.1 | lock rule, "v1.1" 26/600, the one line, sheets as letter targets (44 × 38) on phone / thumbnails on desktop, docs as a list, v1 below | 1 |
| 7 Snapshot | no lamp, no dots, no unseen count; everything else works | 0 |
| 8 Desktop | master–detail, newest open | 0 |

## How it feels
An instrument. Every control does one thing: the lamp says whether anyone's working, the cabinet says where things are, the scrubber says when. It's quiet between sessions, and STANDBY is a full reading, not a waiting room. The scrubber is the one tactile moment: it follows the finger with no easing and snaps to detents, with a haptic tick where the browser supports one (not iOS Safari).

## Weak spots (said plainly)
- On a phone the work is one 96 px image. If the owner opens the site mainly to *look at what was made*, C makes him tap for it every time.
- Liveness on the phone is small: one dot, a lamp dip and a strip swap.
- The past state (scrubbed) is a different layout from the cabinet (a round's record, not the grid), because the records hold scores, not file counts. That's honest, but it's a second visual mode.

## Open
- Does the scrubbed state need its own URL (`#/h/round/2`)? I'd say yes; systems to confirm.
