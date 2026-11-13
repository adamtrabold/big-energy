# Visual designer notes: project site

## Where things stand (2026-11-13, after concept turn 1)
- Jam: turn 1 systems (jobs, A/B/C), turn 2 me (shared visual system, B dropped, C → Panel+Cabinet, new D The Set), turn 3 director (A and B retired; C, D and a new E Herbarium to concepts; 8-frame test; settled artifact, self-hosted Inter, no dark mode, tests as a kind, Breadboard stage, archive greyed), turn 4 systems (model, numbering rule, `jobs.md`, `common-how-it-works.md`, per-concept how-it-works).
- **Concept turn 1 (me), done:** `concepts/common-how-it-looks-and-feels.md`, `concepts/{cabinet,the-set,herbarium}/how-it-looks-and-feels.md`, frames for each at phone and desktop, 1:1: `frames.png` (phone 1–7 + desktop landing; C also has an extra phone scrubbed to R2) and `frames-desktop.png` (desktop 1–7). Sources: `concepts/_frames/*.py` (`lib.py` kit; `python3 cabinet.py`, `the_set.py`, `herbarium.py`, `desktop.py`).
- **My recommendation: E first, C second, kill D.**

## Owner direction during this turn (all verbatim in `owner.md`) and what I did
1. "anyone that gets the link is fine to see everything" / "it is primarily me": one view; design for him.
2. "why would i need to read an a3 sheet properly on my phone? i just need to see everything properly on my phone." → **read mode dropped** (my own jam idea). Asked systems to remove it from common-how-it-works §5. No region sidecars.
3. "why make anything on a3 at all? im not in europe and im not printing" → A3 is **legacy**; labelled "legacy sheet"; no layout assumes a 1.414 box (E's fixed mount dropped).
4. "dont do phone first -- do images that will be great on the site that i can view responsively" → **no size leads**; every frame at phone and desktop. E's 600 px column removed on desktop.
5. "i really only want images for things that need to be images -- text should be html and stuff" → text is HTML everywhere; kinds should become image · doc · test · record; C now has 3 columns (images · docs · tests); E's newest-of-each is 3 tiles.

## Decisions so far and why
- Palette (WCAG checked): ground `#E6E4DF`, cell `#EFEDE9`, paper `#F8F7F4` (new: slips, doc pages), rule `#C4C1BA`, ink 2 `#5F5D58`, ink `#1B1B19`, ON `#23863F` (lamp only). No red or orange in the frame.
- Inter self-hosted, tabular figures. Decisions verbatim at body size (director).
- Lamp ON / STANDBY / SNAPSHOT (+ Connecting, Live paused from systems). Unseen = ink dot (D: Δ). Dropped = 40% + the word.
- **Phones drawn inside real browser chrome:** usable no-scroll area 714 px (iOS status 47 + Safari bar 83). All landings fit. Builder must measure the claude.ai artifact chrome.
- Compare: wipe on phone, side by side on desktop. Lineage row with one labelled gap "r1–r4 not kept".
- **Rev letters corrected** to the numbering rule: the test's "FOLD-D rev H" is drawn as **rev C** (FOLD-D: v1 = A, v1.1 = B). Backfill: FOLD-A/B/C/E rev A = archive r5, B = v1, C = v1.1; FOLD-D, HUSH, ONE SHEET A = v1, B = v1.1; **HUSH-C and ONE SHEET-C stay rev A** (v1 → v1.1 pixel diff 0.07%, footer only). Every v1.1 sheet differs from v1 in bytes, so byte diffs can't define revs.
- **Revision clouds are real:** a pixel diff of FOLD-A v1 → v1.1 finds 6 areas (joystick, closed view, effects text, footer). HUSH-A also changed (joystick in every view). Clouds work for any same-size image pair.
- **C:** keep. 3 columns; level line under the now stage (Lock); Spec drawn below the level as "early" (19 eng docs). Scrubber detents = rounds + locks only (45 decisions in ~30 h would put ticks 7 px apart). **Real scrubber case:** R2 scores, where FOLD 7 and ONE SHEET 7 (his two finalists today) sat under TYPE CASE 9 and HYMNAL 9 (both later set aside). Desktop is master–detail with the newest item open on the right.
- **D:** propose kill. Its anchor (sheet sets, sheet letters, clouds on sheets) is the format the owner retired twice today; desktop landing is half empty; more "spreadsheet" than C. Donate: Go to field, show-changes clouds, the Decisions register, issues by day. If kept: issues by day, Δ unnumbered.
- **E:** lead. Image alone + HTML label, same fields for every kind; slips; lineage by repetition; level strip for stage; desktop label in the bottom-right corner beside the work; doc pages are real text; a test's specimen is its sound.

## Flags for systems
1. Kinds → image · doc · test · record (sub-type on the label).
2. "Stage = made in" leaves Spec empty (eng docs land in Concept). Suggest "the stage it serves".
3. Define "now" (I drew Lock; systems' E doc said Concept).
4. Remove read mode from common-how-it-works §5.
5. C's scrubbed state URL (`#/h/round/2`)?

## Director's objections (from turn 3; how I answered)
- C "spreadsheet": 3 columns, Newest strip, newest open on the desktop's right; honest limit on the phone noted.
- C empty rows: level line, "not yet" once per row.
- C scrubber: real R2 case; kept.
- D no-scroll, live, textual, numbering: all shown; still propose kill.
- E versions / stage / docs+tests / not-a-gallery: all shown. Weak spots listed (similar-looking legacy sheets, J6 thinner than C, find-by-filter).

## Open questions
- Owner: J12 (since you last looked) still pending; every concept has a fallback line.
- Builder: claude.ai artifact chrome height on a phone.
- Director: kill D? Move D's Go to field and clouds into E (or C)?

## Next
- Director scores C, D, E against the frames. Then a second concept round on the survivors (likely E with C's scrubbed history as a grain), then the handoff's "How it looks and feels" for the approved one.
