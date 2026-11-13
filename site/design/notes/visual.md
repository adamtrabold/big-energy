# Visual designer notes: project site

## Where things stand (13 Nov ~16:35, the public site) — read this first
- The Herbarium build is now the public site (gh-pages). Owner: "i dont want a bunch of .md docs, i want this stuff on website". `build.py` now also renders **Docs** (`#docs` index from `docs/README.md`, `#doc-architecture`, `#doc-<feature>` for all 14 feature docs, stubs marked "not yet written") and **Reviews** (`#reviews`, `#review-<file>` from `design/reviews/`). decided / proposed / open are tagged in table cells and bold runs (filled / outlined / dashed), counted per doc on the index, with a legend. Markdown stays the source.
- Links are resolved by path (relative to the source file, then repo-root): docs ↔ features ↔ reviews ↔ eng items ↔ owner record all go to `#hash` views; no unresolved internal hash (138 checked).
- Phone tables stack as label/value rows (data-label from the header); ASCII diagrams shrink to fit down to 9.5 px, then scroll with a hint; mermaid renders via jsdelivr (falls back to source text offline).
- The lamp, the simulated ON, the signed-out toggle and the prototype bar are gone. The header carries "Updated <last commit time> · <subject>" (jobs rev 3), taken from git at build time.
- Nav simplified until the owner says how: **Latest · Docs · Reviews · Decisions · History · Versions**; kind and stage chips live inside Latest. The landing adds two cards under the newest work: Docs and Reviews.

## Earlier: E Herbarium prototype
- E scored 9 and passed coverage. The owner saw the frame images: "i dont understand why is this an image and not a webpage", "dont render a bunch of images unnecessarily", then "prototypes should go on that webpage i am having you build". **So: no more frame images. Site concepts are shown as working pages, and "prototype" is a kind of item the site hosts.**
- **Built:** `site/design/concepts/herbarium/prototype/`: `build.py` (repo → `index.html` + `media/`), `app.html` (template: inline CSS + JS, data injected as JSON), `index.html` (output, ~0.7 MB), `media/` (63 files: downscaled JPG copies + thumbs, 16-bit WAVs). Total ≈ 9.3 MiB. Rebuild: `python3 build.py` (≈ 8 s; deletes stale media).
- **Real:** branch groups (CHAMBER newest, RAIN exploring; BUTTERFLY retired and DIPTYCH killed, both shown as dropped, per the branches director 13:09), with images **placed by each group's own `how-it-looks-and-feels.md`** (they do have `![…](img/…)` lines, and the alt text is the caption); v1.1 legacy sheets (FOLD, HUSH, ONE SHEET) + archive A sheets (FOLD113, TYPE CASE, HYMNAL, UNDER GLASS); FOLD-A rev A/B/C and HUSH-A A/B lineage with show-changes clouds from the pixel diff; 7 sims (T-001…T-007) with plots, the golden/perturbed WAVs for T-004 and T-005 (A/B keeps the playhead) and the saw WAV for T-002; 49 decisions parsed verbatim from `design/owner.md` (caused links hand-mapped for Daisy, MIDI out, aftertouch, drift, angle, echo); rounds 1–5 parsed from `scores.md` plus branches round 1; v1 / v1.1; docs and records rendered as HTML (tables scroll inside their own box); P-001 = the prototype itself as a "prototype" item (site · Concept · exploring) with a real/faked list.
- **Faked or simplified:** no db (lamp Standby; the "Replay" control simulates ON while CHAMBER rev A lands, then fades back); signed-out is a toggle; "since you last looked" uses localStorage plus a "pretend my last visit was before the branches round" control; codes and rev letters are illustrative; only FOLD-A and HUSH-A carry earlier forms; some events have no recorded time (times otherwise from git); the full-instrument archive isn't included; Inter loads from Google Fonts (falls back to the system font offline).
- **Checked in headless Chrome (DOM only, no screenshots):** all 34 routes at 1440 and 390 with no JS errors and no horizontal overflow; A/B keeps the playhead; clouds toggle; simulated ON; snapshot; unseen marks. At 390 × 664 the landing's image, label and "+ n more" sit above the fold; the prototype bar folds to one "Prototype ▴" button under 900 px.
- Routes: `#home`, `#f-all|image|doc|test|record|prototype`, `#s-<stage>`, `#decisions`, `#history-day|round|version`, `#version-v1-1|v1`, `#g-<GROUP>`, `#i-<CODE>[-rev-X]`, `#compare-<CODE>[-rev-X-Y]`.
- **Fix (13 Nov, after round 2 branches):** `build.py` now reads image links from each group's `how-it-looks-and-feels.md` in both styles, `![alt](img/…)` and `<figure><img src="img/…">…<figcaption>`, in doc order; the figcaption is the caption; no hard-coded file lists. CHAMBER and RAIN are rev B (round 2 fixes, re-score pending). The landing leads with CHAMBER-closed-with-book (the doc's first figure). 11 CHAMBER + 6 RAIN images; total ≈ 9.5 MiB.
- Note for the orchestrator: the branches team is mid-round and files in `design/branches/concepts/*/img/` are changing (some deleted or re-rendered). The build takes whatever is on disk and skips refs to missing files. Rebuild just before publishing.

## Where things stand (2026-11-13, after concept building round 2) — read this first
- **Director steer 1:** D killed. Five must-dos for visual: (1) C and E frames 1, 2, 8 with a new-format item as the newest; (2) a new frame 9, the concept group in the new format; (3) E doc tiles as real text; (4) C phone: collapse the not-yet rows, show the newest at full width; (5) both: show-changes clouds in frame 3, D's decisions register in frame 5. **All five done.**
- Systems rev 2: `jobs.md` (J15, 9 frames, each at phone and desktop), `common-how-it-works.md` §3 (concept groups: images + HTML docs, group revs, legacy groups), cabinet/herbarium how-it-works rev 2 (asked me to test C's wide Concept row).
- **Round 2 frames:** `concepts/{cabinet,herbarium}/frames.png` (phone 1–7 + 9 as a full scrolled page 390 × 1900; C adds the scrubbed-R2 phone) and `frames-desktop.png` (desktop 1–7 + 9; 8 = desktop 1). Source `concepts/_frames/round2.py` (`python3 round2.py [c|e]`). Round 1 scripts now write `*-r1`. D's round 1 frames stay as the record.
- **New-format newest = BUTTERFLY rev A** (branches round), real renders in `design/branches/concepts/butterfly/img/` (made from `_mock-src/out/rb_bf_*.png` by `figs_rb.py`): `butterfly.jpg` lead, plus joint, on-the-wall, from-behind, top drawing, rear-section drawing. I used a real group instead of the steer's example "FOLD rev D" (which doesn't exist). Newest-of-each-kind image tile = CHAMBER's render; desktop below-fold = CHAMBER, DIPTYCH, RAIN.
- Docs: `cabinet/how-it-looks-and-feels.md` rev 2, `herbarium/how-it-looks-and-feels.md` rev 2, `common-how-it-looks-and-feels.md` rev 2 (D removed; group page, doc tiles, decisions register, show changes added). `the-set/how-it-looks-and-feels.md` marked KILLED.

### Round 2 decisions and findings
- **C's wide Concept row works:** "18 concepts · 3 locked · 4 exploring" (+ "11 dropped ›" on desktop). My count: 3 locked (HUSH, ONE SHEET, FOLD), 4 exploring (BUTTERFLY, CHAMBER, DIPTYCH, RAIN), 11 dropped (FOLD113, TYPE CASE, HYMNAL, UNDER GLASS + 7 full-instrument). Kind labels sit just above the Spec row. It reads as a status panel more than a grid. That's honest; it fills as stages start.
- **C's collapsed not-yet line holds;** the newest render fits at 358 × 224 inside 714 px along with the scrubber.
- **C desktop:** the left panel's lower half is now empty grey (wide rows). Acceptable; possible use is the two newest decisions there (not drawn).
- **E:** the render is about a third of the phone screen; dropping the three tiles on phone would add ~100 px. Offered for next round.
- **Group page (frame 9, shared):** label → one line → doc as HTML in its order, images where placed, captions as text under them; desktop E puts text beside images, C stacks them in the 792 work side. Drawings with baked-in callouts (rear section) are fine as drawings; renders carry no text.
- **Flag for systems/orchestrator:** the branch `how-it-works.md` files don't place their images yet (no `![…](img/…)`), so under the group rule nothing in `img/` is an item. Someone has to add the image lines.
- Tests now T-004, stage Spec (early), per systems/director.

## Earlier state (after concept turn 1)
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

## Director's objections
- Steer 1 (concept building): every landing led with a legacy A3 sheet (FOLD-D), the thing the owner had just retired. Answered in round 2: BUTTERFLY's real render leads everywhere; legacy sheets only in frames 3 and 6, labelled.
- Turn 3 (jam), how I answered in concept turn 1:
- C "spreadsheet": 3 columns, Newest strip, newest open on the desktop's right; honest limit on the phone noted.
- C empty rows: level line, "not yet" once per row.
- C scrubber: real R2 case; kept.
- D no-scroll, live, textual, numbering: all shown; still propose kill.
- E versions / stage / docs+tests / not-a-gallery: all shown. Weak spots listed (similar-looking legacy sheets, J6 thinner than C, find-by-filter).

## Open questions
- Owner: J12 (since you last looked) still pending; every concept has a fallback line.
- Builder: claude.ai artifact chrome height on a phone.
- Director: kill D? Move D's Go to field and clouds into E (or C)?

## Open (round 2)
- Owner: J12 dot vs "newest first" (the director's question, asked via the orchestrator).
- Branch docs must place their images for the group model to show them.
- Builder: claude.ai artifact chrome height on a phone.

## Next
- Director: READY check and scores for C and E (9 frames each, both sizes). Then the handoff's "How it looks and feels" for the approved one.
- (Old:) Director scores C, D, E against the frames. Then a second concept round on the survivors (likely E with C's scrubbed history as a grain), then the handoff's "How it looks and feels" for the approved one.
