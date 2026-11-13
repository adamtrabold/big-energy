# E · Herbarium — how it looks and feels

Product designer (visual focus). **Rev 2**, concept building round 2, 2026-11-13. Read with `how-it-works.md` (systems, rev 2) and `../common-how-it-looks-and-feels.md`. The word "herbarium" never appears on screen.

**Frames (rev 2, all 1:1):** `frames.png` = phone frames 1–7 and 9 (frame 9 drawn as the full scrolled page, 390 × 1900, with the fold marked). `frames-desktop.png` = desktop frames 1–7 and 9 (frame 8 is desktop frame 1). Source: `../_frames/round2.py` (`python3 round2.py e`). Round 1 frames are superseded.

**The idea in one line:** every piece of work is shown as itself, as large as the screen allows, with one HTML label in the same place for every kind; revisions are slips on that label.

## What changed in rev 2 (director steer 1, systems rev 2)
1. **New-format work leads.** The newest work is the **BUTTERFLY rev A** group, shown by its lead render (`design/branches/concepts/butterfly/img/butterfly.jpg`, from `_mock-src/out/rb_bf_main.png`) at its own shape: phone 358 × 224, desktop 940 × 587. The label is the group's: "BUTTERFLY rev A", "concept group · Concept · exploring", slip "rev A · 14:02 · branches round · first rev", then "grew from ONE SHEET · v1.1 ›". On desktop the group's one line ("ONE SHEET with a walnut top: exact at the playing edge, free at the rear.") sits on the label as text. No legacy sheet appears on any landing.
2. **Doc tiles are real text** (director item 3): a paper tile with code (11/700, ink 2), title (11.5/600 on phone, 12.5/600 on desktop, up to 3 lines) and, on desktop, one line ("Every subsystem the Seed touches, re-derived."). No shrunk pages anywhere. Round 1's three doc cards in frame 5 are gone.
3. **Newest of each kind** shows new-format work: image = CHAMBER rev A's render, doc = D-032, test = T-004 (waveform + "RAN").
4. **Below the fold on desktop:** CHAMBER, DIPTYCH and RAIN lead renders, three across. The archive's look-alike walnut sheets (a round 1 weak spot) are no longer what you see first.
5. **Frame 3:** "Show changes" clouds on the compare. **Frame 5:** the shared decisions register under the "decisions" filter. **New frame 9:** the concept group page.

## Phone (390, 714 px usable), top to bottom
Lamp line → name 22/600 → "a portable Model D · **v1.1 current**" → "WAITING ON YOU  ONE SHEET or FOLD" → level strip (9 × 6 px segments: ink for Concept and Lock with Lock underlined, an outline for Spec, rule grey for the rest) + "Lock · 2 of 9 · Spec begun early · next Handoff" → **the lead render** at full width → label (1 px ink rule, code 15/700 + "rev A", kind line, one slip on paper ground) → "grew from ONE SHEET · v1.1 ›" → "+ 6 more since you last looked ›" 13/600 → Newest of each kind (three 114 × 72 tiles: render, real-text doc, waveform). It fits 714.

## Desktop (1440 × 900)
Top band: lamp and name left, Waiting on you centre, level strip right. Hairline, then the filter row (all · stage · kind · version · decisions · history) with "+ 6 more since you last looked ›" right-aligned. The work sits left at 940 px. On the right (372 px): Newest of each kind at the top, and the group label **bottom-aligned with the image**, in the corner. Below the fold: the rest, three across. **Tablet:** work full width, label below with the tiles beside it, two across below.

## Frames and taps
| # | Phone and desktop | Taps |
|---|---|---|
| 1 | Standby; BUTTERFLY rev A leads | 0 |
| 2 | On; lamp mid-dip; render cross-fades; slip "rev A · just now" lands; dot; "+ 7 more" | 0 |
| 3 | FOLD-A (legacy) v1.1 ↔ v1, clouds on; all slips unfolded; lineage | 3 |
| 4 | T-004: the sound as the specimen (phone 358 × 200, desktop 940 × 340), label beside or below, plot | 1 |
| 5 | Filter "decisions" → the register → "Switch to Daisy Seed" → caused items | 2 + scroll |
| 6 | v1.1: cover, groups with legacy sheets (7 across on desktop), shared docs as rows | 1 |
| 7 | Snapshot: no lamp, no dot, "+ 6 more on 13 Nov" | 0 |
| 8 | = desktop 1 | 0 |
| 9 | BUTTERFLY rev A group page | 1 |

## How it feels
Walking up to the newest piece of work and reading its card. On the new-format landing the render is clean, large and free of baked-in text, and every word around it is real text. It's the most direct answer to "images only for things that need to be images".

## Weak spots
- J6 is a strip: where the build stands, not how much is in each stage (C does that better).
- Finding something old is by filter, not by place.
- On a phone, the label, "+ 6 more" and three tiles take the second half of the screen, so the render is about a third of it, not more. Dropping the tiles on phone (they're one tap away under "kind") would give the render ~100 px more height. I'd try that next round if the director wants the work bigger.
