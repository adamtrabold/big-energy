# E · Herbarium — jobs coverage check

Product designer (systems focus), 2026-11-13, before the owner sees E (director score 9). Checked against `site/design/jobs.md` rev 2 (J1–J15) using `how-it-works.md` rev 2 ("HIW"), `how-it-looks-and-feels.md` rev 2 ("HLF"), `../common-how-it-works.md` rev 2 ("common"), and the drawn frames `frames.png` (phone, "P") and `frames-desktop.png` (desktop, "D"), which I looked at.

## Verdict: PASS. Every job is supported. Nothing sends E back.
J12 is conditional (owner hasn't answered); E supports both answers.

| Job | Supported? | Where |
|---|---|---|
| J1 Land and get oriented, no scroll, any size | Yes | P1 / D1 (= frame 8): name "( name to come )", lamp line "Standby · last BUTTERFLY rev A · 14:02", level strip "Lock · 2 of 9 · Spec begun early · next Handoff", "v1.1 current", "Waiting on you: ONE SHEET or FOLD", newest work, all within 714 px on phone. HIW Structure §Landing 1–8; HLF Phone, Desktop. |
| J2 See everything made, incl. explorations, legacy, dropped | Yes (spec; dropped not drawn) | Every group or loose item is in the list below the fold, newest first (D1 "Below: everything else…"); legacy sheets in P6/D6 and P3; records under `kind → record` (HIW States). Dropped/archive greyed at their drop date: HIW Structure ("Dropped things appear at their drop date, greyed"), common §10. |
| J3 Live update without reloading | Yes | P2 / D2: lamp ON mid-dip, render cross-fades, slip "rev A · just now", unseen dot, "+ 7 more". Queued before publish: HIW frame 2, common §5. |
| J4 History + decisions verbatim with caused work; Day · Round · Version | Yes (grains not drawn) | P5 / D5: filter `decisions` → "Switch to Daisy Seed", asked line, "time not recorded", before D-031 / after D-032, D-019 rev 13, all links. Three grains: HIW filter row (`history`), common §7, jobs F4. |
| J5 Versions: current, contents, change from previous, own URL | Yes | "v1.1 current" link on every landing → P6 / D6: cover with lock rule, "locked 13 Nov", "v1, plus: FOLD stands at 120°…", groups FOLD rev C / HUSH rev B / ONE SHEET rev B with legacy sheets, shared docs D-003, D-004, D-019 rev 14, R-001. "copy link" shown. URL `#/v/v1.1` (common §8). |
| J6 Where the build chain stands; every stage openable | Yes | Level strip on P1/P2/P7, D1/D2/D5/D7 (done, now underlined, early outline, not yet). Tap a segment → filter by stage (HIW Landing 4); `#/s/<stage>`. |
| J7 Tests: result in words, plot, sound, A/B keeping playhead | Yes | P4 / D4: T-004, "RAN · no limits set · osc 110.0 Hz", env. peak line, waveform with playhead at 0:00.6, golden · perturbed (perturbed underlined), plot below. Playhead kept on switch: common §6. 1 tap from the test tile. |
| J8 Share a link to site, group, item, version, day | Yes | "copy link" on P3, P4, P6, P9 and D3, D6, D9. Routes for group, item, version, day, decisions: common §8. Links work signed out (snapshot is baked in): P7 / D7. |
| J9 Current vs explored vs dropped, in words | Yes | Every label carries status in words: "exploring" (P1), "locked in v1.1" (P3 FOLD-A), "current" (v1.1 cover). Dropped: word + 40% (common §10). |
| J10 Compare across forms; lineage; show changes; labelled gaps | Yes | P3 (wipe) / D3 (side by side): FOLD-A rev C ↔ rev B, "Show changes from rev B · 6 areas: joystick, closed view, effects text, footer" with clouds; lineage rev A · "r1–r4 not kept" · rev B · rev C; all slips unfolded. v1 reached in 1 tap from FOLD-A v1.1 (frame 3 total 3 taps). |
| J11 Team working now, on what | Yes | Lamp line: P1/D1 "Standby · last BUTTERFLY rev A · 14:02"; P2/D2 "On · branches round · since 13:40". Connecting / Live paused states: common §4. |
| J12 *(conditional)* What changed since last look | Yes, both ways | If kept: "+ 6 more since you last looked ›" (P1/D1), unseen dot on the label (P2/D2), opens filtered list (HIW Landing 7). Signed out: no marks, "+ 6 more on 13 Nov" (P7/D7). If he says no: "+ n more today", no dots (common §9). |
| J13 Find one thing again, ≤4 taps; links by code | Yes | Filter row `all · stage · kind · version · decisions · history` (D1, P5). `kind → image` lists images individually (HIW filter row). Examples: v1.1 → FOLD-A = 2 taps (P3); test = 1–3 taps (HIW frame 4). Links by code: common §8. |
| J14 Everything properly on a phone, every kind | Yes (records and wide tables not drawn) | Phone frames for every drawn screen: landing, image + compare (P3), test (P4), decisions (P5), version (P6), group with HTML doc text (P9). Records and docs render as HTML one column; wide tables scroll in their own box; images pinch to full detail (common §6). |
| J15 One concept as a whole; earlier revs one tap away | Yes (earlier-rev row not drawn) | P9 / D9: BUTTERFLY rev A: label, "6 images · 1 doc · exploring", "grew from ONE SHEET · v1.1 (legacy sheets)", its `how-it-works` as HTML with renders and a drawing placed where the doc puts them, captions as text. Group rev row: HIW §Group open (BUTTERFLY has only rev A, so nothing to show yet; FOLD rev A–C would show one). 1 tap from the landing. |

## Not drawn in any frame (supported in the docs; the checker must walk these on the build)
- `history` filter with the Day · Round · Version switch (J4).
- A dropped or archive item greyed in the list (J2, J9).
- A record (R-001) and a long eng doc with a wide table opened on a phone (J14).
- A group rev row with more than one rev, e.g. FOLD rev C → rev B (J15).
- Tapping a level-strip segment to filter by stage (J6).

## Fixed during this check
- `how-it-works.md` frame 1, 2 and 9 text named "FOLD rev D"; the frames use BUTTERFLY rev A. Doc aligned to the frames.

## Scope questions (not blockers)
- None new. J12 still waits on the owner's answer.

## Other notes
- Phone: the render takes about a third of the landing (visual's own weak spot). Doesn't block a job; the visual designer's suggestion (drop the three tiles on phone) would give the work ~100 px more.
- Desktop frame 9: the doc text sits in the right column as one block, not beside each image it follows as HIW §Sizes describes. Either is fine for J15; pick one at handoff.
