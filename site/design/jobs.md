# Project site: jobs and flows

Written by the product designer (systems focus), 2026-11-13. Rev 3 (16:30): hosting moves to **GitHub Pages** (owner 16:23–16:24); `docs/` and `design/reviews/` become first-class content; prototypes are items (13:20); the live lamp becomes "last pushed". Rev 2 folded in 12:13–12:41 and the director's steer 1. The checker walks every job below on the build.

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
- "prototypes should go on that webpage i am having you build" (13:20)
- "we need on that site architectural documentation and clear docs for each featureset" (16:21)
- "im going to put the github on github pages so i can easily access it from there instead of here. i want all review and logs and documents there, not here" (16:23) · "ok thats fine if its not private" (16:24)
- "i dont understand the nav here" (13:43, on the Herbarium prototype; specifics pending)

## Rules every concept follows (settled)
- **Viewer only.** No feedback, decisions or chat on the site.
- **Designed for Adam first.** Others with the link see the same view. When a choice helps him or a guest, pick him.
- **Public, one view for everyone.** The site is a public GitHub Pages site; anyone with the address sees everything, owner notes and scores included.
- **Responsive; no size leads.** Phone, tablet and desktop are all first-class. Every screen works properly at 390 px (J14) and makes good use of a wide screen.
- **Images only for what has to be visual** (renders, drawings, diagrams, plots). All text (labels, principles, specs, notes, tables, scores, version notes) is HTML. The old A3 sheets are shown as they are, labelled `legacy sheet`; nothing new is made as a sheet.
- **The repo is the truth.** The site shows nothing the repo doesn't hold.
- **Nothing is removed, only greyed.** Dropped and archived work stays, at 40% with the word "dropped".
- **Hidden on purpose:** render code and its by-products (`.scad`, `_raw`, `_tmp` images, anything in `_mock-src/out/` that no doc points at), sim `.cir`/`.log` files.
- **Hosted on GitHub Pages, static.** The site changes only when a session pushes. No claude.ai artifact, no `db`, no sign-in. Every viewer sees the same build.
- **Everything goes in the repo, nothing only in chat** (owner 16:23): reviews, logs and documents are files the site shows.

## The model (shared by all concepts; detail in `concepts/common-how-it-works.md`)
- **Stages** (the build chain, in order): Concept → Lock → Handoff → Spec → BOM → Breadboard → Boards → Prints → Assembly. Each is done, now, begun early, or not yet. Empty future stages are shown.
- **Stage of an item = the stage it serves**, not the one it was made in. The 19 eng docs serve Spec and show as "early" (begun before Handoff). Circuit sims serve Spec; bench tests serve Breadboard.
- **"Now" = the latest stage with a locked output, until the next one starts.** Today: **Lock** (v1.1); next: Handoff (starts when Adam picks ONE SHEET or FOLD).
- **Kinds:** **image · doc · test · record · prototype.** An image has a sub-type on its label: render, drawing, diagram, plot, legacy sheet. A doc has a sub-type when it belongs to a set: architecture, feature, review. A prototype is a working page or file the site runs or links to (owner 13:20).
- **Doc sets (first-class):** **Docs** = `docs/README.md` (index), `docs/architecture.md`, `docs/features/*.md`, one file per feature, same headings, each with a status word (decided / proposed / open; stubs say "not yet written"). **Reviews** = `design/reviews/*.md` (critic and expert reviews, dated). Both have their own place on the landing and their own URLs, not just a kind filter.
- **Item:** code · title · kind (+ sub-type) · stage · rev · date · status · file · URL · lineage (its earlier and later forms) · the group it belongs to, if any · the decision that caused it, if any.
- **Concept group:** one concept's work as a whole: its images and its docs at a given group rev (`FOLD rev D`), with its own URL. The group's main doc is its layout: images appear in the order the doc places them. This is how new work arrives and how the site shows a concept.
- **Status:** current · locked in vN · exploring · dropped.
- **Version:** a locked set (v1, v1.1, …): the group revs and shared docs it froze, a date and one line. It never changes.
- **Round:** a burst of work (design rounds, test runs) with dates, items, scores and an outcome.
- **Event:** time · what happened · one line · the codes it touched. Kinds: group revised, item made/revised, scored, owner decided (verbatim, with the codes it caused), locked, dropped, test ran (pass/fail/ran), session started/ended.
- **Codes:** docs in `docs/` keep their file names as codes (`architecture`, `features/voice`); reviews are `RV-` + date + slug. Otherwise: groups `CONCEPT` (`FOLD`); legacy sheets `CONCEPT-LETTER` (`FOLD-A`); new images `CONCEPT-view` (`FOLD-main`, `FOLD-joint`); others kind letter + number in order of arrival (`D-014`, `T-007`, `R-001`). Never reused, never changed when a file moves. Revs are letters, added only when a session says the thing changed.
- **Last pushed** (replaces the lamp): "Updated 14:02 · <what the push was>", plus "Working · <what> · since 13:40" only when the session's last pushed status says working and is under 30 min old (common §4). Never claims live.

## Jobs

| # | Job | Source | Done when |
|---|---|---|---|
| J1 | **Land and get oriented.** In about 10 seconds, without scrolling: what the project is, whether the team is working, where the build stands, and what's waiting on him. | "serves as a landing page" | At every size, the first screen shows the name (or "( name to come )"), "Updated <time>" (and "Working" when fresh), current stage, current version, "waiting on you", and the way to Docs and Reviews. |
| J2 | **See everything the team made**: images, docs, tests and records, including explorations, legacy sheets and dropped work. | "see anything that's created" | Every item in the register is reachable from the landing; archive items appear, greyed. |
| J3 | **See it update as work is pushed**, without reloading. | "live update … as things from here are made"; Pages (16:23) | After a push, an open page shows the new work within about 10 min (Pages build + CDN cache) without a reload, and every page says when it was last updated. |
| J4 | **See the history**: what happened, in order, and the owner's decisions in his own words, with the work each caused. Three grains: Day · Round · Version. | "see the history" | Any decision can be found in the decisions list and its caused items opened from it. |
| J5 | **See the versions**: which is current, what's in each, and what changed from the one before. | "versions" | Each version has its own URL listing its contents and its one-line change. |
| J6 | **See where the build chain stands**: which stage is now, which are done or begun early, what's ahead. | "as we get further down the build chain" | The current stage is visible on the landing; every stage can be opened to its items. |
| J7 | **See the tests and their results**: result in words, the plot, the sound, and A/B between variants (golden vs. perturbed). | "the tests" | A test opens with its result, its plot or waveform, play, and an A/B switch that keeps the playhead. |
| J8 | **Share a link** to the whole site or to one group, item, doc, review, version or day. | "shareable"; public is fine (16:24) | Every one has a public URL that opens straight to it. |
| J9 | *(inferred)* **Tell current from explored from dropped.** | needed for J2 and J5 | Every item and group shows its status in words. |
| J10 | *(inferred)* **Compare a thing across its forms**: see an item's lineage in a row, put two forms side by side (desktop) or wipe between them (phone), and optionally mark where an image changed ("show changes"). Missing old forms show as a labelled gap. | "versions" is only useful if he can see the change | From FOLD-A v1.1 he can reach its v1 form in one tap and compare. |
| J11 | *(inferred)* **Know when the site last changed, and whether a session said it was working.** | "live" means nothing without it | Every page shows "Updated <time> · <what>"; "Working …" appears only from a fresh pushed status. |
| J12 | *(inferred; owner asked, answer pending)* **See what changed since he last looked.** Per browser (no sign-in on Pages). | "primarily me"; he comes back between sessions | Unseen items are marked; the landing says how many. If he says no: newest first is enough, no marks. |
| J13 | *(inferred)* **Find one thing again quickly**, by stage, kind or version (one filter at a time). Links by code also work. | J2 at scale (90+ images today) | Any item is reachable in 4 taps or fewer from the landing. |
| J14 | **See everything properly on a phone**: every kind (image, doc, test, record, and a whole concept group) is fully viewable and usable on a phone. Owner (verbatim): "i just need to see everything properly on my phone." | owner, 12:13 | Every kind of item and every screen works at 390 px; images zoom to full detail; docs and tables read without pinching (wide tables scroll inside their own box). |
| J16 | **Read the architecture and feature docs as a set**: the index with each feature's status, the architecture page, and each feature doc, with status words (decided / proposed / open) visible. | owner 16:21 | Docs is one tap from the landing; the index shows every feature with its status; stubs say "not yet written"; links between docs and to eng/design sources work. |
| J17 | **See the reviews and logs**: critic and expert reviews, scores, the owner record, and the history of what each session did. | owner 16:23 ("i want all review and logs and documents there, not here") | Reviews are one tap from the landing, newest first, dated, with the score in words when there is one; logs = the history view plus records. *(What he means by "logs" is inferred; see open.)* |
| J18 | **Open the prototypes**: working prototypes run or open from the site. | owner 13:20 | A prototype is an item with a label and an "open" action that runs it (static HTML in the site) or links to it. |
| J15 | *(inferred)* **See one concept as a whole**: its images large at their own shapes and its words as real text, at its latest rev or any earlier one. | owner 12:41 ("images only for things that need to be images -- text should be html") + "explorations, mocks, layouts" | A concept group opens at its own URL with its images and HTML docs; its earlier revs are one tap away. |

Not jobs: giving feedback, approving, deciding, chatting (owner, 11:52).

## Flows

**F1 Arrive** (J1, J3, J6, J11, J12)
Open the link → the landing, no scroll, at any size: status line ("Updated 14:02 · what" / "Working · what · since" when fresh) → name → current stage and version → "waiting on you" → the newest work shown, and what's new since last look (count). If he keeps it open, pushed work appears within about 10 min.

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
Open the link while no session works → a complete reading: "Updated 14:02 · …", stage, version, newest work, waiting on you, unseen count. Never an empty or "loading" state as the default.

**F10 Read the docs** (J16)
From the landing → Docs → the index (feature · what it covers · status) → architecture or a feature → links to other docs and sources.

**F11 Read a review** (J17)
From the landing → Reviews → newest first (date · who · what it reviewed · score in words) → the review as HTML → links to what it reviewed.

**F9 Open a concept group** (J15, J14, J10)
From the landing (newest work), a version, or a stage → the group at its current rev: its images large in the order its doc places them, its docs as HTML beside (desktop) or under (phone) → group rev list (rev D · rev C · …) → tap an earlier rev to see the group as it was → tap any image for F3/F6.

## Update path (what a session does; every concept assumes it)
Pages is static: **a push is the update.** One script, `site/publish.sh`, plus a line in HANDOFF's after-each-step list:
1. Session starts → write `site/status.json` {working: true, what, since} → commit → push. (The page shows "Working" from it, aged by push time.)
2. Work made or revised → files in the repo (concept group `img/` + markdown; docs in `docs/`; reviews in `design/reviews/`; prototypes in their folder) → append an event to `site/events.jsonl` (group revised / item revised / review added / decision with caused codes / locked / dropped / test ran) → commit → push.
3. Push triggers the build (below). The built site carries `manifest.json` with the commit time and message as "Updated <time> · <what>".
4. Session ends → `site/status.json` {working: false, last, waiting on Adam} → commit → push.
Events and status are files, not database rows. Commits batch naturally; push after each meaningful step, not each file.

**Build on push: proposal (systems).** Recommend a **GitHub Actions workflow** (`.github/workflows/site.yml`: checkout → `python site/build.py` → `_site/` with `.nojekyll` → upload-pages-artifact → deploy-pages). Why: generated output (HTML, WebP at three sizes, waveform SVGs) never enters git history, so the repo doesn't grow by every image rev three times over; no session can forget to build; the site can't drift from the repo. Needs: owner sets Pages source to "GitHub Actions" once in repo settings. **Risk to check first:** pushing a file under `.github/workflows/` needs a token with workflow permission; the session proxy may refuse it (tags were refused with 403). If refused, either the owner adds the workflow file himself once, or the fallback: `build.py` runs in the session and pushes `_site/` to a **`gh-pages` branch** (Pages source = that branch). Not recommended: committing build output to `main` (history bloat, merge noise), or serving the repo root (Jekyll would render every markdown file as a page outside our design).

**Freshness.** An open page re-fetches `status.json` and `manifest.json` every 2 min (cache-busted). Pages' CDN caches files for about 10 min, so "as work is pushed" means within ~1 min build + up to ~10 min cache. The page never says "live".

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
7. The landing a guest sees from a shared public link (same as his, no unseen marks on a first visit). — J8
8. Desktop landing. — J1 at a different size
9. **A concept group in the new format** (e.g. FOLD rev D: renders large at their own shapes, its principles/spec as HTML). — J15, J14

Not covered by a frame (check in the concept docs instead): J2 (archive greyed), J8 (item URL), J9 (status in words), J13 (find by filter).

## Open
- **Nav (13:43):** "i dont understand the nav here". One question to the owner pending (orchestrator).
- J12 waiting on the owner.
- J17 "logs": inferred as history + records + review files; confirm what he means if it matters.
- Build: can a session push `.github/workflows/`? Decides Action vs. `gh-pages` branch.
- The concept test frames predate Pages, docs and reviews; E needs a Docs and a Reviews frame (J16, J17) before the next owner look.
