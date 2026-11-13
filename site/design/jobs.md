# Project site: jobs and flows

Written by the product designer (systems focus), 2026-11-13, after jam turns 1–4. Folds in the director's rulings (turn 3) and the owner's answers of 11:52 and 12:06. The checker walks every job below on the build.

## The problem, in one sentence
Adam wants one link where he can look at everything the team has made for the synth, see how it changed and where the build stands, and see it update while sessions work. He talks to the team in chat, not on the site.

## Owner facts this rests on (verbatim, `owner.md`)
- "it should live update there as things from here are made and explored, and i want to be able to see the history and versions and see anything that's created (explorations, mocks, layotus, diagrams, etc). it should be shareable and minimal ui in the style of dieter rams / braun"
- "chatting here is fine; i just want there to be a site for me to view all the stuff from the team / the versions / the tests / etc as we get further down the build chain"
- "anyone that gets the link is fine to see everything"
- "it is primarily me"

## Rules every concept follows (settled)
- **Viewer only.** No feedback, decisions or chat on the site.
- **Designed for Adam first** (phone first). Others with the link see the same view. When a choice helps him or a guest, pick him.
- **One view for everyone.** Nothing hidden from link holders, owner notes and scores included.
- **The repo is the truth.** The site shows nothing the repo doesn't hold.
- **Nothing is removed, only greyed.** Dropped and archived work stays, at 40% with the word "dropped".
- **Hidden on purpose:** render code, sim `.cir`/`.log` files. These aren't things he looks at.
- Hosted as a claude.ai artifact. Signed-in viewers get live updates; signed-out viewers get the last published snapshot.

## The model (shared by all concepts)
- **Stages** (the build chain, in order): Concept → Lock → Handoff → Spec → BOM → Breadboard → Boards → Prints → Assembly. Each stage is done, now or not yet. Empty future stages are shown.
- **Kinds:** sheet · diagram · doc · test · record. Each item has one kind.
- **Item:** code · title · kind · stage (the stage it was made in) · rev · date · status · file · URL · lineage (its earlier and later forms) · the decision that caused it, if any.
- **Status:** current · locked in vN · exploring · dropped.
- **Version:** a locked set (v1, v1.1, …) with a date, one line and its contents. It never changes.
- **Round:** a burst of work (design rounds, test runs). Has dates, items, scores and an outcome.
- **Event:** time · what happened · one line · the item codes it touched. Kinds: made, revised, scored, owner decided (verbatim, with the codes it caused), locked, dropped, test ran (pass/fail), session started/ended.
- **Numbering:** sheets `CONCEPT-LETTER` (`FOLD-A`); others kind letter + number in order of arrival (`D-014`, `G-003`, `T-007`, `R-001`). Numbers are never reused or changed when a file moves. Revs are letters (`rev F`), added only when a session says the item changed.
- **Lamp:** ON (a session is working) · STANDBY (no heartbeat for 20 min, or a session ended) · SNAPSHOT (signed-out viewer; no live data).

## Jobs

| # | Job | Source | Done when |
|---|---|---|---|
| J1 | **Land and get oriented.** In about 10 seconds, without scrolling: what the project is, whether the team is working, where the build stands, and what's waiting on him. | "serves as a landing page" | Landing shows the name (or "( name to come )"), lamp state, current stage, current version and "waiting on you" on the first screen. |
| J2 | **See everything the team made**: sheets, diagrams, docs, tests and records, including explorations and dropped work. | "see anything that's created" | Every item in the register is reachable from the landing; archive items appear, greyed. |
| J3 | **See it update live** while a session works, without reloading. | "live update … as things from here are made" | A new event appears on an open page within seconds of the session writing it. |
| J4 | **See the history**: what happened, in order, and the owner's decisions in his own words, with the work each caused. Three grains: Day · Round · Version. | "see the history" | Any dated decision can be found and its caused items opened from it. |
| J5 | **See the versions**: which is current, what's in each, and what changed from the one before. | "versions" | Each version has its own page or filtered view (with its own URL) listing its contents and its one-line change. |
| J6 | **See where the build chain stands**: which stage is now, which are done, what's ahead. | "as we get further down the build chain" | The current stage is visible on the landing; every stage can be opened to its items. |
| J7 | **See the tests and their results**: pass/fail in words, the plot, the sound, and A/B between variants (golden vs. perturbed). | "the tests" | A test opens with its result, its plot or waveform, play, and an A/B switch that keeps the playhead. |
| J8 | **Share a link** to the whole site or to one item, version or day. | "shareable" | Every item, version and day has a URL that opens straight to it, signed in or not. |
| J9 | *(inferred)* **Tell current from explored from dropped.** | needed for J2 and J5 | Every item shows its status in words. |
| J10 | *(inferred)* **Compare a thing across its forms**: see an item's lineage in a row and put two forms side by side (desktop) or wipe between them (phone). Missing old forms show as a labelled gap. | "versions" is only useful if he can see the change | From FOLD-A v1.1 he can reach its v1 form in one tap and compare. |
| J11 | *(inferred)* **Know whether the team is working right now**, and on what. | "live" means nothing without it | The lamp and its line say ON with what, or STANDBY with the last event's time. |
| J12 | *(inferred)* **See what changed since he last looked.** Signed-in only, per person. | "primarily me"; he comes back between sessions | Unseen items are marked; the landing says how many. |
| J13 | *(inferred)* **Find one thing again quickly**, by stage, kind or version (one filter at a time), or by its code. | J2 at scale (90+ images today) | Any item is reachable in 4 taps or fewer from the landing. |
| J14 | *(inferred)* **Look at an A3 sheet properly on a phone**: fit, step through read-mode crops, pinch to full res, swipe to the next sheet, download the original. | sheets are 4961×3508; he reads on a phone | FOLD-A is readable at detail level on a 390 px screen. |

Not jobs: giving feedback, approving, deciding, chatting (owner, 11:52).

## Flows

**F1 Arrive** (J1, J3, J6, J11, J12)
Open the link → the landing, no scroll: lamp line (ON + what / STANDBY + last event + time / SNAPSHOT + publish time) → name → current stage and version → "waiting on you" → what's new since last look (count, and the newest item named or shown). If ON, new events arrive while he watches.

**F2 Browse what's made** (J2, J9, J13)
From the landing → pick one axis: stage, kind or version → a list or grid of items, newest first, each with code, rev and status → dropped items greyed in place.

**F3 Open an item** (J7, J14, J8)
- Sheet → fit-width map → read-mode crops (where a regions sidecar exists) → pinch to full res → swipe to the next sheet in the set → download the original.
- Doc → readable text, first heading up top.
- Test → result in words, plot or waveform, play/stop, A/B variant switch that keeps the playhead. One sound at a time.
- Diagram → the image, zoomable.
- Record → readable text.
Every item shows its label (code · title · kind · stage · rev · date · status) and has a copyable URL.

**F4 Walk history** (J4)
From the landing → history → pick a grain: Day (every event), Round (one entry per round: what went in, scores, outcome), Version (locks and stage changes only) → a decision appears verbatim, with the items it caused under it → tap an item to open it (F3). Locks are ruled, signed lines.

**F5 Open a version** (J5)
From the landing (current version) or history → the version: date, one line, what changed from the previous version, its contents as a track list (by concept, then sheet) → tap any item (F3).

**F6 Compare** (J10)
From an item → its lineage row (same item, small, in order; gaps labelled, e.g. "r1–r4 not kept") → tap a form to swap → compare: side by side on desktop, a wipe on phone. Target: landing → FOLD-A v1.1 in ≤3 taps, → its v1 form in +1.

**F7 Share** (J8)
From any item, version or day → copy link → the link opens straight there. Sharing the whole site is done by Adam in claude.ai.

**F8 Come back with nothing running** (J1, J11, J12)
Open the link while no session works → STANDBY: a complete reading (stage, version, last event and when, waiting on you, unseen count). Never an empty or "loading" state as the default.

## Update path (what a session does; every concept assumes it)
A shared script (`site/publish.sh`) plus a line in HANDOFF's after-each-step list, so it happens every time:
1. Session starts → write `status/now` (working, what, since). Lamp ON.
2. Item made or revised → commit → `build.py` (repo → manifest + web images + register) → publish changed files → write an event naming the codes.
3. Score, owner decision (verbatim, with caused codes), drop → event row only.
4. Lock → commit → build → publish → "locked vN" event.
5. Test ran → build plots and waveforms → publish → event with pass/fail.
6. Session ends → `status/now` = not working, last event, waiting on Adam. Lamp STANDBY. If the session dies, the 20-minute heartbeat timeout does the same.
Events are cheap (one row); publishes are batched. An event naming an item not yet published shows as queued until its images arrive.

## Backfill (one time, before launch)
- Register every existing file per the numbering rule; older FOLD-105 sheets in `archive/fold-superseded/` become earlier revs of `FOLD-A`… (not new items); FOLD-113 sheets are `FOLD113-*`.
- History from `owner.md` dated sections, `scores.md` rounds 1–5, `VERSIONS.md` and git (only 8 commits, from 13 Nov 11:41).
- Decision → work links added by hand for dated decisions. Some entries (e.g. "Switch to Daisy Seed") have no time of their own; date them from their section.

## The concept test (director, turn 3): 8 frames, phone 390 × 844 with real content, plus one desktop
1. Landing, STANDBY (waiting on you: "ONE SHEET or FOLD"; name to come). — J1, J6, J11, F8
2. Landing, ON, the moment "FOLD sheet D rev H" lands. — J3, J11, J12
3. Landing → FOLD-A v1.1 → its v1 form, taps counted. — J10, J13, J14, F6
4. Bass pluck · golden vs perturbed, A/B. — J7
5. Find "Switch to Daisy Seed" and the work it caused (`eng/daisy-pin-and-audio-check.md`, `eng/daisy-first-principles.md`, spec rev). — J4
6. What's in v1.1. — J5
7. The landing as a signed-out snapshot. — J8, SNAPSHOT
8. Desktop landing. — J1 at a different size

Not covered by a frame (check in the concept docs instead): J2 (archive greyed), J8 (item URL), J9 (status in words), J13 (find by code).

## Open
- None blocking. For the build: "since you last looked" storage (artifact/user state); how long the heartbeat timeout should be (20 min proposed).
