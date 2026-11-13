# Systems designer notes: project site

## Where things stand (2026-11-13, after jam turn 1)
- Concept phase. I took jam turn 1 in `site/design/jam.md`: jobs J1–J14, repo inventory, structure, update path, flows F1–F7, three directions (A Lab Book, B Shelf, C Panel) plus an inversion ("only what changed since you last looked") to fold into F1.
- Handed to the visual designer. `jobs.md` not written yet (after the jam).

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

## Draws (SystemRandom, tag e7dd76f0)
Oblique: "Work at a different speed" (A's speed dial), "Abandon normal instruments" (C). Fields: lab notebook (A), cassette J-card (B). Constraint: one screen, no navigation (C). Twist: nothing removed, only greyed (all).

## Director's objections
- None yet (first turn).

## Open questions
- Owner: who will he share with (signed-out viewers miss live; hide private records?). Include archive/ or start at Little D round 1?
- Team: artifact vs GitHub Pages (I lean artifact for db live + claude.ai sharing).
- My own: in A, how does J13 (find all of X) work without a second nav? In B, where do live events go? In C, where do decisions-in-his-words (J4) live? "As it stood then" in C needs snapshot computation from item dates/status.

## Next
- Visual designer's turn on the three directions. Then director steers. Then write `jobs.md` (jobs + flows), then concepts with the visual designer, then coverage check per 9+ concept.
