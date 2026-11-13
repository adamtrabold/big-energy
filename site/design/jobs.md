# Project site: jobs and flows

Written by the product designer (systems focus), 2026-11-13. Rev 2 (concept building, systems turn 2): folds in the owner's messages of 12:13–12:41 and the director's steer 1 (D killed; kinds, stage and "now" ruled; concept groups). The checker walks every job below on the build.

## The problem, in one sentence
Adam wants one link where he can look at everything the team has made for the synth, see how it changed and where the build stands, and see it update while sessions work. He talks to the team in chat, not on the site.

## Owner facts this rests on (verbatim, `owner.md`)
- "it should live update there as things from here are made and explored, and i want to be able to see the history and versions and see anything that's created (explorations, mocks, layotus, diagrams, etc). it should be shareable and minimal ui in the style of dieter rams / braun"
- "chatting here is fine; i just want there to be a site for me to view all the stuff from the team / the versions / the tests / etc as we get further down the build chain"
- "anyone that gets the link is fine to see everything" · "it is primarily me"
- "i just need to see everything properly on my phone."
- "why make anything on a3 at all? im not in europe and im not printing"
- "dont do phone first -- do images that will be great on the site that i can view responsively"
- "i really only want images for things that need to be images -- text should be html and stuff"

## Rules every concept follows (settled)
- **Viewer only.** No feedback, decisions or chat on the site.
- **Designed for Adam first.** Others with the link see the same view. When a choice helps him or a guest, pick him.
- **One view for everyone.** Nothing hidden from link holders, owner notes and scores included.
- **Responsive; no size leads.** Phone, tablet and desktop are all first-class. Every screen works properly at 390 px (J14) and makes good use of a wide screen.
- **Images only for what has to be visual** (renders, drawings, diagrams, plots). All text (labels, principles, specs, notes, tables, scores, version notes) is HTML. The old A3 sheets are shown as they are, labelled `legacy sheet`; nothing new is made as a sheet.
- **The repo is the truth.** The site shows nothing the repo doesn't hold.
- **Nothing is removed, only greyed.** Dropped and archived work stays, at 40% with the word "dropped".
- **Hidden on purpose:** render code and its by-products (`.scad`, `_raw`, `_tmp` images, anything in `_mock-src/out/` that no doc points at), sim `.cir`/`.log` files.
- Hosted as a claude.ai artifact. Signed-in viewers get live updates; signed-out viewers get the last published snapshot.

## The model (shared by all concepts; detail in `concepts/common-how-it-works.md`)
- **Stages** (the build chain, in order): Concept → Lock → Handoff → Spec → BOM → Breadboard → Boards → Prints → Assembly. Each is done, now, begun early, or not yet. Empty future stages are shown.
- **Stage of an item = the stage it serves**, not the one it was made in. The 19 eng docs serve Spec and show as "early" (begun before Handoff). Circuit sims serve Spec; bench tests serve Breadboard.
- **"Now" = the latest stage with a locked output, until the next one starts.** Today: **Lock** (v1.1); next: Handoff (starts when Adam picks ONE SHEET or FOLD).
- **Kinds:** **image · doc · test · record.** An image has a sub-type on its label: render, drawing, diagram, plot, legacy sheet.
- **Item:** code · title · kind (+ sub-type) · stage · rev · date · status · file · URL · lineage (its earlier and later forms) · the group it belongs to, if any · the decision that caused it, if any.
- **Concept group:** one concept's work as a whole: its images and its docs at a given group rev (`FOLD rev D`), with its own URL. The group's main doc is its layout: images appear in the order the doc places them. This is how new work arrives and how the site shows a concept.
- **Status:** current · locked in vN · exploring · dropped.
- **Version:** a locked set (v1, v1.1, …): the group revs and shared docs it froze, a date and one line. It never changes.
- **Round:** a burst of work (design rounds, test runs) with dates, items, scores and an outcome.
- **Event:** time · what happened · one line · the codes it touched. Kinds: group revised, item made/revised, scored, owner decided (verbatim, with the codes it caused), locked, dropped, test ran (pass/fail/ran), session started/ended.
- **Codes:** groups `CONCEPT` (`FOLD`); legacy sheets `CONCEPT-LETTER` (`FOLD-A`); new images `CONCEPT-view` (`FOLD-main`, `FOLD-joint`); others kind letter + number in order of arrival (`D-014`, `T-007`, `R-001`). Never reused, never changed when a file moves. Revs are letters, added only when a session says the thing changed.
- **Lamp:** ON · STANDBY (no heartbeat for 20 min, or a session ended) · SNAPSHOT (signed-out viewer).

## Jobs

| # | Job | Source | Done when |
|---|---|---|---|
| J1 | **Land and get oriented.** In about 10 seconds, without scrolling: what the project is, whether the team is working, where the build stands, and what's waiting on him. | "serves as a landing page" | At every size, the first screen shows the name (or "( name to come )"), lamp state, current stage, current version and "waiting on you". |
| J2 | **See everything the team made**: images, docs, tests and records, including explorations, legacy sheets and dropped work. | "see anything that's created" | Every item in the register is reachable from the landing; archive items appear, greyed. |
| J3 | **See it update live** while a session works, without reloading. | "live update … as things from here are made" | A new event appears on an open page within seconds of the session writing it. |
| J4 | **See the history**: what happened, in order, and the owner's decisions in his own words, with the work each caused. Three grains: Day · Round · Version. | "see the history" | Any decision can be found in the decisions list and its caused items opened from it. |
| J5 | **See the versions**: which is current, what's in each, and what changed from the one before. | "versions" | Each version has its own URL listing its contents and its one-line change. |
| J6 | **See where the build chain stands**: which stage is now, which are done or begun early, what's ahead. | "as we get further down the build chain" | The current stage is visible on the landing; every stage can be opened to its items. |
| J7 | **See the tests and their results**: result in words, the plot, the sound, and A/B between variants (golden vs. perturbed). | "the tests" | A test opens with its result, its plot or waveform, play, and an A/B switch that keeps the playhead. |
| J8 | **Share a link** to the whole site or to one group, item, version or day. | "shareable" | Every group, item, version and day has a URL that opens straight to it, signed in or not. |
| J9 | *(inferred)* **Tell current from explored from dropped.** | needed for J2 and J5 | Every item and group shows its status in words. |
| J10 | *(inferred)* **Compare a thing across its forms**: see an item's lineage in a row, put two forms side by side (desktop) or wipe between them (phone), and optionally mark where an image changed ("show changes"). Missing old forms show as a labelled gap. | "versions" is only useful if he can see the change | From FOLD-A v1.1 he can reach its v1 form in one tap and compare. |
| J11 | *(inferred)* **Know whether the team is working right now**, and on what. | "live" means nothing without it | The lamp and its line say ON with what, or STANDBY with the last event's time. |
| J12 | *(inferred; owner asked, answer pending)* **See what changed since he last looked.** Signed-in only, per person. | "primarily me"; he comes back between sessions | Unseen items are marked; the landing says how many. If he says no: newest first is enough, no marks. |
| J13 | *(inferred)* **Find one thing again quickly**, by stage, kind or version (one filter at a time). Links by code also work. | J2 at scale (90+ images today) | Any item is reachable in 4 taps or fewer from the landing. |
| J14 | **See everything properly on a phone**: every kind (image, doc, test, record, and a whole concept group) is fully viewable and usable on a phone. Owner (verbatim): "i just need to see everything properly on my phone." | owner, 12:13 | Every kind of item and every screen works at 390 px; images zoom to full detail; docs and tables read without pinching (wide tables scroll inside their own box). |
| J15 | *(inferred)* **See one concept as a whole**: its images large at their own shapes and its words as real text, at its latest rev or any earlier one. | owner 12:41 ("images only for things that need to be images -- text should be html") + "explorations, mocks, layouts" | A concept group opens at its own URL with its images and HTML docs; its earlier revs are one tap away. |

Not jobs: giving feedback, approving, deciding, chatting (owner, 11:52).

## Flows

**F1 Arrive** (J1, J3, J6, J11, J12)
Open the link → the landing, no scroll, at any size: lamp line (ON + what / STANDBY + last event + time / SNAPSHOT + publish time) → name → current stage and version → "waiting on you" → the newest work shown, and what's new since last look (count). If ON, new events arrive while he watches.

**F2 Browse what's made** (J2, J9, J13)
From the landing → pick one axis: stage, kind or version → items, newest first, each with code, rev and status; images grouped by concept → dropped items greyed in place.

**F3 Open an item** (J7, J14, J8)
- Image → at its own shape, full available width → pinch / zoom to full detail → next image in its group → download original. Legacy sheets the same, labelled `legacy sheet`.
- Doc / record → HTML text, one column; long docs get a heading jump list; wide tables scroll inside their own box.
- Test → result in words, numbers, sound with play and A/B (keeps the playhead), plots as images. One sound at a time.
Every item shows its label (code · title · kind · stage · rev · date · status, and its group) and has a copyable URL.

**F4 Walk history** (J4)
From the landing → history → pick a grain: Day, Round, Version → decisions verbatim with the items they caused → tap one (F3). Or → **decisions**: one list, date · his words · what it caused. Locks are ruled, signed lines.

**F5 Open a version** (J5)
From the landing (current version) or history → the version: date, one line, what changed from the previous one, its contents grouped by concept (the group revs it froze, then shared docs) → tap a group (F9) or an item (F3).

**F6 Compare** (J10)
From an item → its lineage row (gaps labelled, e.g. "r1–r4 not kept") → tap a form → compare: side by side on desktop, wipe on phone → "show changes" marks the changed areas (images of the same size only). Target: landing → FOLD-A v1.1 in ≤3 taps, → its v1 form in +1.

**F7 Share** (J8)
From any group, item, version or day → copy link → opens straight there. Sharing the whole site is done by Adam in claude.ai.

**F8 Come back with nothing running** (J1, J11, J12)
Open the link while no session works → STANDBY: a complete reading (stage, version, newest work, last event and when, waiting on you, unseen count). Never an empty or "loading" state as the default.

**F9 Open a concept group** (J15, J14, J10)
From the landing (newest work), a version, or a stage → the group at its current rev: its images large in the order its doc places them, its docs as HTML beside (desktop) or under (phone) → group rev list (rev D · rev C · …) → tap an earlier rev to see the group as it was → tap any image for F3/F6.

## Update path (what a session does; every concept assumes it)
A shared script (`site/publish.sh`) plus a line in HANDOFF's after-each-step list, so it happens every time:
1. Session starts → write `status/now` (working, what, since). Lamp ON.
2. Work made or revised in a concept → images into the group's `img/` folder, text into its markdown → commit → `build.py` → publish changed files → **one "group revised" event** naming the group rev and the codes that changed.
3. Item made or revised outside a group (an eng doc, a record) → commit → build → publish → event.
4. Score, owner decision (verbatim, with caused codes), drop → event row only.
5. Lock → commit → build → publish → "locked vN" event.
6. Test ran → build plots and waveforms → publish → event with the result.
7. Session ends → `status/now` = not working, last event, waiting on Adam. Lamp STANDBY. If the session dies, the 20-minute heartbeat timeout does the same.
Events are cheap (one row); publishes are batched. An event naming something not yet published shows as queued until its images arrive.

## Backfill (one time, before launch)
- Register every existing file per the codes rule. Each existing concept folder becomes a group; its sheets are legacy-sheet images. Older FOLD-105 sheets in `archive/fold-superseded/` are earlier revs of `FOLD-A`… (group FOLD rev A = round 5 archive, B = v1, C = v1.1). FOLD-113 is group `FOLD113`.
- History from `owner.md`, `scores.md` rounds 1–5, `VERSIONS.md` and git (from 13 Nov 11:41).
- Decision → work links added by hand. Undated entries are dated from their place (e.g. "Switch to Daisy Seed" falls after the 13 Nov 09:02 entry: 13 Nov, time not recorded).

## The concept test (director): 9 frames, each at phone (390 × 844) and desktop (1440 × 900), real content
1. Landing, STANDBY (waiting on you: "ONE SHEET or FOLD"; name to come), **newest work = a new-format image**. — J1, J6, J11, F8
2. Landing, ON, the moment a group rev lands (e.g. "FOLD rev D"). — J3, J11, J12
3. Landing → FOLD-A v1.1 (legacy sheet) → its v1 form, taps counted, "show changes" on. — J10, J13, F6
4. Bass pluck · golden vs perturbed, A/B. — J7
5. Find "Switch to Daisy Seed" in the decisions list and open the work it caused (`eng/daisy-pin-and-audio-check.md`, `eng/daisy-first-principles.md`, spec rev). — J4
6. What's in v1.1. — J5
7. The landing as a signed-out snapshot. — J8, SNAPSHOT
8. Desktop landing. — J1 at a different size
9. **A concept group in the new format** (e.g. FOLD rev D: renders large at their own shapes, its principles/spec as HTML). — J15, J14

Not covered by a frame (check in the concept docs instead): J2 (archive greyed), J8 (item URL), J9 (status in words), J13 (find by filter).

## Open
- J12 waiting on the owner.
- For the build: heartbeat timeout (20 min proposed); how an open page behaves when the platform moves it to a new version.
