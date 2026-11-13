# Systems designer notes: project site

## Where things stand (2026-11-13, after concept building systems turn 2)
- Director steer 1: **D The Set killed** (parts: show changes → shared viewer; decisions register → both concepts; codes → common). **C Cabinet and E Herbarium round again.** Rulings: kinds image·doc·test·record (image sub-types render/drawing/diagram/plot/legacy sheet); stage = stage served (eng docs + sims → Spec, "early"); now = latest stage with a locked output (Lock; next Handoff); read mode gone; responsive, no size leads; legacy sheets shown as is; scrubbed state URL `#/h/round/2`; J12 conditional.
- Done this turn: `jobs.md` rev 2 (owner 12:13–12:41 folded in; responsive rule; images-only-where-needed rule; model with concept groups, stage/now rules, codes; J14 = "see everything properly on a phone" verbatim; **new J15 (inferred): see one concept as a whole**; F9 open a group; 9-frame test incl. frame 9 concept group). `common-how-it-works.md` rev 2 (D removed; codes §2; **concept group model §3**; show changes + doc text compare §6; decisions list §7; links incl. `#/g/` and `#/d`). `cabinet/how-it-works.md` rev 2. `herbarium/how-it-works.md` rev 2 (matches visual's layout). Kill note at top of `the-set/how-it-works.md`. Header of visual's common look doc edited to drop D (director asked).
- **Concept group model (key decision):** a concept folder = a group: `how-it-works.md` is the layout; images in `img/<view>.png` (no baked text, long edge ≥ 2400); **an image is an item only if a group doc points at it** (alt = title, quoted title = sub-type). Group revs = one per concept per round via one "group revised" event; only changed members get item revs. New image codes `CONCEPT-view`. Legacy folders are groups of legacy sheets (FOLD rev A archive, B v1, C v1.1). Versions freeze group revs. `succeeds:` link optional for render-replaces-sheet.
- **Cabinet reshape (mine, for visual to test):** Concept row = one wide drawer of groups (splitting a group across image/doc cells tears apart what the owner wants together); kind columns from Spec on; not-yet rows collapse to one line (director); Handoff own row as "next"; scrubber detents rounds + locks only (visual); decisions via "decisions ›" beside "history ›". Risk I named: today the "grid" is mostly a list.
- Facts found: `_mock-src/out/` IS tracked (120 files incl. _raw/_tmp/.scad); `.gitignore` points at stale `design/little-d/...` path; HANDOFF says it's not in repo. Flag for orchestrator. Site safe because unreferenced images aren't items.
- Branches round (`design/branches/concepts/{butterfly,chamber,diptych,rain}`) is the first real new-format work; docs-only so far (sketches in jam-sketches).
- J12 still unanswered.

## Earlier: after concept turn 1
- Concept turn 1 (mine, first): wrote `concepts/common-how-it-works.md` (shared data, lamp incl. Connecting + Live lost states, events/queued, J12 conditional, item viewer, lineage/compare, hash routes, shared states table, session steps) and `concepts/{cabinet,the-set,herbarium}/how-it-works.md` (structure, flows, 8-frame table with tap counts, concept states, weak spots). Visual designer's turn next.
- jobs.md went to the owner; orchestrator asked him about J12. Answer pending: concepts treat J12 as conditional (common §4 says what replaces it).
- Concept reshapes (mine): Cabinet 4 columns (records out; decisions = scrubber ticks), Lock/Handoff rows one wide cell, level line + "not yet" per row, newest strip, scrubber scrubs decisions/locks (real case Round 2: HUSH, ONE SHEET, FOLD, TYPE CASE, HYMNAL, UNDER GLASS). Set: sections = stages + Records; issue/rev/version kept apart; revision table lists locks + named issues only; Δ = unseen issue (signed out: latest issue); revision clouds from build.py pixel diffs ("unacceptable colour" draw); "go to" code field. Herbarium: decisions are specimens (words + caused items mounted); stage strip; versions = filtered set with cover; slips show 2 + "+n earlier"; one-of-each-kind row ("only one element of each kind" draw); records off main column.
- Taps frame 3: all three = 2 to v1.1, 3 to v1. Frame 5: C 2+scroll, D 3, E 2+scroll.
- Fact fix: "Switch to Daisy Seed" is 13 Nov (after the 13 Nov 09:02 entry), not 12 Nov. Corrected in jam turn 4 and concepts.
- Open for builder: how open pages move to a new artifact version ("next quiet moment") — page saves route/scroll in artifact state; fallback fetch manifest. Cloud diffs need threshold for re-render noise.

## Earlier: after jam turn 4
- Jam done (turns 1 systems, 2 visual, 3 director, 4 systems). `site/design/jobs.md` written: problem sentence, settled rules, shared model, J1–J14 with "done when", flows F1–F8, update path, backfill, the 8-frame test mapped to jobs.
- Director's rulings (turn 3): A Lab Book retired (parts absorbed: Day/Round/Version history grains, decisions verbatim at body size, lock = ruled signed line); B Shelf dropped (track list → version page; detents → C scrubber). **Three concepts: C Cabinet (structure-first), D The Set (document-first), E Herbarium (work-first).** Tests are a kind, stage renamed Breadboard. Artifact not GH Pages. Self-host subset Inter via assets. No dark mode in concepts. FAIL in words only. Region sidecars yes. Archive included, greyed. publish.sh automatic. Lineage by repetition is the compare answer.
- Owner 12:06: "anyone that gets the link is fine to see everything" (one view, nothing hidden) and "it is primarily me" (design for Adam first; tie-break rule).
- Next: designers split C, D, E and build concepts against the 8 frames; I own how each works, then coverage check per 9+ concept.

## Decisions so far and why
- **Viewer only.** Owner 11:52: chat stays for talk and decisions. No feedback UI in the core.
- **The site is a projection of the repo.** Repo is truth; `site/build.py` derives `manifest.json` + web images. Keeps it honest and rebuildable.
- **Two layers.** Checked `describe_capabilities db`: `onSnapshot` gives real live push; Claude writes with `db_write`; but `db` is null for signed-out viewers. So: baked snapshot (publish_files, works for anyone) + live db rows (events, `status/now` heartbeat) for signed-in viewers.
- **Events cheap, publishes batched.** One db row per event; publish after a set/score/lock/test run.
- **STANDBY is the main state.** Most of the time no session runs; page must be a good landing page then (stage, current version, last event, "waiting on Adam"). Heartbeat older than 20 min = STANDBY automatically (sessions don't always end cleanly).
- **Greyed, never removed** (random twist draw): dropped items stay in place.
- **History can't be git log alone.** Only 4 commits; restructure squashed earlier history. Backfill once from `owner.md` dated headings, `scores.md` rounds, `VERSIONS.md`.
- Item status set: current / locked in vN / exploring / dropped. Every item and version has a URL.
- Hidden: render code, `.cir`/`.log` sim files. Shown: plots, WAVs (tests have sound: audio player needed), metrics.

## Inventory facts (repo survey)
- ~91 PNG (A3 sheets 4961×3508, A–D per concept, FOLD has E), 18 SVG, ~126 md, 9 WAV, 7 sim plots, metrics.json; versions/v1, v1.1 full snapshots; archive/ paused + superseded; design/branches live round.

## Draws (SystemRandom; turn 1 tag e7dd76f0; turn 4: 'State the problem in words as clearly as possible' → problem sentence in jobs.md; 'museum accession register' → numbering rule)
Oblique: "Work at a different speed" (A's speed dial), "Abandon normal instruments" (C). Fields: lab notebook (A), cassette J-card (B). Constraint: one screen, no navigation (C). Twist: nothing removed, only greyed (all).

## Turn 4 additions (mine)
- Numbering rule (accession-register draw): sheets CONCEPT-LETTER (FOLD-A, FOLD113-A, TYPECASE-A); D/G/T/R + arrival number; never reused; moves keep code; revs letters, added only when a session says it changed (byte diffs don't count: v1→v1.1 HUSH PNGs differ but changelog names FOLD + bend drawing). Register in `site/numbers.json`.
- Kinds: sheet, diagram, doc, test, record. Stage of item = stage it was made in.
- Facts: rounds 1–4 sheet images were not kept (squash); lineage rows are 2–4 forms today; show "r1–r4 not kept" as a labelled gap. `archive/fold-superseded/` older FOLD-105 sheets = earlier revs of FOLD-A.
- C scrubber real case: drag to Round 2 (12 Nov): six concepts incl TYPE CASE, HYMNAL; no versions; from scores.md. Images mostly gone, so it's history of decisions not files.
- Frame 5 decision real: design/owner.md ~l.114 "Switch to Daisy Seed"; caused eng/daisy-pin-and-audio-check.md (evidence), eng/daisy-first-principles.md, budget-variant rev. Undated entry; date from section.
- Decision→work links must be authored (`caused:` codes on the event), backfilled by hand.
- Tap budget: landing → FOLD-A v1.1 ≤3, → v1 +1.
- Concept pushes: C newest item on STANDBY lamp line; D "Issue N in progress" with queued Δ rows; E build-chain strip under the lamp for J6, label fields = model.

## Director's objections
- To all three phone landings (turn 3): words and numbers lead; the work isn't the biggest thing anywhere → E created as work-first.
- C: counts grid isn't a designer's landing; empty rows must read as level; scrubber must earn its cost; does records earn a column.
- D: no-scroll vs 100-row index; must feel live; stay textual; numbering rule (done in turn 4).
- E: must prove versions, stage (J6), docs/tests as specimens, label+slips+lineage visible at landing size.

## Open questions
- Settled: sharing (everyone sees all; primarily Adam), archive (included, greyed), host (artifact).
- Held by director: "do you open it to look at newest work or see where it stands?" (concepts should answer it).
- Build-time: heartbeat timeout (20 min proposed); where per-person "last looked" is stored.
- My own: in A, how does J13 (find all of X) work without a second nav? In B, where do live events go? In C, where do decisions-in-his-words (J4) live? "As it stood then" in C needs snapshot computation from item dates/status.

## Next
- Visual redraws C and E frames 1, 2, 8 with a new-format item as newest, adds frame 9 (concept group), real-text doc tiles, tests C's collapsed not-yet line + my wide Concept row, frame 3 with show changes, frame 5 with the decisions list.
- Then director expects READY: C, E and scores. Then my coverage check per 9+ concept against jobs.md rev 2 (J1–J15; frames don't cover J2 archive, J8 item URL, J9, J13 filters).
