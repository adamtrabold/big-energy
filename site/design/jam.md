# Project site jam (started 2026-11-13)

Read `site/design/BRIEF-CONTEXT.md`. Turns are added below, newest at the bottom. Each ends with `NEXT: <role> — <why>`.

---

## Turn 1 — product designer (systems focus), 2026-11-13

### 1. Jobs (written from the owner's words before I read any records)

The owner wants to **look**, not talk. Chat stays the place to talk and decide. The site is a viewer.

| # | Job | Source |
|---|---|---|
| J1 | Land on the project and know in 10 seconds what it is, where it stands, and what's waiting on him. | "serves as a landing page" |
| J2 | See everything the team made: explorations, mocks, layouts, diagrams, tests, docs. | "see anything that's created" |
| J3 | See it change while work happens, without asking or reloading. | "live update … as things from here are made" |
| J4 | See the history: what happened, in what order, and why (decisions). | "see the history" |
| J5 | See the versions: what's in each locked set, and which one is current. | "versions" |
| J6 | Follow the build chain: concept, lock, handoff, spec, BOM, tests, boards, prints, assembly. Know which stage we're in. | follow-up: "as we get further down the build chain" |
| J7 | See the tests and their results (pass, fail, the plot, the sound). | follow-up: "the tests" |
| J8 | Share it: send a link to the whole thing or to one item. | "shareable" |
| J9 | *(inferred)* Tell what's current and chosen from what was explored and dropped. | needed for J2 + J5 to make sense |
| J10 | *(inferred)* Compare a thing across versions (FOLD sheet D in v1 vs v1.1). | "versions" is only useful if you can see the change |
| J11 | *(inferred)* Know whether the team is working right now, or idle. | "live" is meaningless without it |
| J12 | *(inferred)* See what changed since he last looked. | phone reader, comes back between sessions |
| J13 | *(inferred)* Find one thing again quickly (deep link, or a short list by kind). | J2 at scale: there are 90+ images already |
| J14 | *(inferred)* Look at an A3 sheet properly on a phone (zoom into detail). | sheets are 4961×3508 |

**Not jobs:** giving feedback, making decisions, chatting. (Owner, 11:52.) If comments come later it's an add-on, not the core.

### 2. What the site has to hold (repo survey, shallow)

- **Sheets** (the core design artifact): A3 PNG mocks, 4961×3508, A–D per concept (FOLD has E). ~91 PNGs in the repo across concepts, versions and archive. Huge files: need web-size copies plus full-res on demand.
- **Sketches and diagrams:** PNG/SVG (`jam-visual-sketches.*`, `draw-systems.py` outputs in branches).
- **Docs:** ~126 markdown files: how-it-works, looks-and-feels, coverage, engineering research (`eng/` ~19 notes, master spec `budget-variant.md` at rev 14), side explorations (`explore/`).
- **Records:** `owner.md` (dated decisions), `scores.md` (rounds 1–5, dated), `jam.md`, `jobs.md`, `notes/`, `naming.md`. These *are* the history.
- **Tests:** circuit sims in `eng/sim/`: 467 `.cir`, 425 `.log` (noise, never shown raw), and the real results: 7 plots (filter AC, VCO tracking, self-oscillation…), **9 WAV files** (VCO waveforms, bass pluck, resonant sweep), `metrics.json`. Tests have *sound*. The site must play audio.
- **Versions:** `versions/v1`, `versions/v1.1`: full frozen snapshots of every sheet and doc at lock. `VERSIONS.md` is a clean table (version, date, one line). Locks are the backbone.
- **Live rounds:** `design/branches/` (a creative round starting now), plus `site/design/` (this work).
- **Archive:** paused and superseded concepts (FOLD-113, TYPE CASE, HYMNAL, full-instrument). Dropped, not deleted.
- **Render code** (`_mock-src/`, `*.py`): not something he views. Hidden.
- **Git history is thin:** 4 commits, all 2026-11-13; the restructure squashed everything before. **The real history before today lives in the records** (dated headings in `owner.md`, round headings in `scores.md`, version table). The site's history can't be "just git log"; it has to be built from records + git, and backfilled once.

How things change over time: rounds (1–5, branches) produce sheets → director scores → owner reacts → lock copies a set into `versions/vN` → work continues in `design/`. Concepts get dropped to `archive/`. Engineering spec revs in place (rev 14). Tests get re-run with variants (`golden`, `fold_emph_worst`, `fold_emph_guarded`, `example_perturbed`).

### 3. Draws (real randomness, Python `random.SystemRandom`, seed tag e7dd76f0)

| Draw | Result | Fed |
|---|---|---|
| Oblique Strategy 1 | "Work at a different speed" | Direction A's time dial (three speeds of history) |
| Oblique Strategy 2 | "Abandon normal instruments" | Direction C: the site as a device panel, not a website |
| Unrelated field 1 | a lab notebook | Direction A: dated bound entries, figures pasted in, signed pages |
| Unrelated field 2 | a cassette J-card | Direction B: versions as spines on a shelf, contents as a track list |
| Constraint | one screen, no navigation | Direction C (and pushes A: one control only) |
| Twist | nothing is ever removed, only greyed | Rule for every direction: dropped work stays in place, greyed |

### 4. Structure (shared by every direction)

The site is a **projection of the repo**. The repo is the truth; the site never holds anything the repo doesn't. That keeps it honest and rebuildable.

Objects:
- **Project** (one): name, one-line, current stage, current version, "waiting on Adam" (from HANDOFF "Next decisions that are Adam's").
- **Stage** (the build chain, ordered): Concept → Lock → Handoff → Spec → BOM → Tests → Boards → Prints → Assembly. Each has status: done / now / not yet. Stages with nothing yet are shown, empty, so he sees the road ahead.
- **Version** (locked set): v1, v1.1… with date, one line, contents. Immutable.
- **Round** (a burst of work): design rounds 1–5, the branches round, the site round, a test run. Has a start, items, scores, an outcome.
- **Item** (anything made): kind = sheet / sketch / diagram / doc / test / record. Has a title, a stage, a round, a status, a file, a permalink, and a **lineage** (the same thing's earlier and later forms: FOLD sheet D r3 → r4 → r5 → v1 → v1.1).
- **Event** (the history unit): time, what happened, one line, the items it touched. Kinds: made, revised, scored, owner decided, locked, dropped, test passed/failed, session started/ended.

Item status (one set, used everywhere): **current** · **locked in vN** · **exploring** · **dropped** (greyed, never hidden: the twist draw).

Every item and every version has its own URL (hash route) so a link can point at one sheet. That's J8 at the item level.

### 5. The update path: from a session to the page

Checked: the page's `db` capability has `onSnapshot` (rows push to an open page live) and Claude writes rows with `db_write`. **But `db` is null for signed-out viewers.** So a shared link opened by someone not signed in gets no live data. That forces a two-layer design:

**Layer 1 — the snapshot (always works, anyone).** A build script (`site/build.py`) reads the repo (VERSIONS.md, scores.md, owner.md headings, git log, folders) and writes `manifest.json` + web-size images (sheets at ~1600 px, full-res on tap). A session publishes it with `publish_files` (patch mode: only changed files). The page renders from the manifest baked into it. A shared link always shows the project as of the last publish.

**Layer 2 — the live wire (signed-in owner).** Small rows in `db`: `events/*` and `status/now` (heartbeat). The page subscribes; new events slide in without a reload.

What a session does, per event:

| Event in the session | Session does | Owner sees |
|---|---|---|
| Session starts work | write `status/now` = {working: true, what: "Round 6 sheets", since} | Light goes ON; line says what's being worked on |
| An item is made or revised (sheet, doc, sketch) | commit → `build.py` → `publish_files` (patch) → write an `events` row | Item appears at the top of "now", marked new |
| Director scores | event row ("FOLD 9") | Score appears on the round |
| Owner decides (in chat) | append owner.md → event row with his words | Decision lands in history, verbatim |
| Lock vN | commit → build → publish → event "Locked v1.2" | New version appears; previous one moves down |
| Test run finishes | build plots/WAV → publish → event "VCO tracking: pass" | Test result with plot and a play button |
| Concept dropped | event "dropped"; item greys in place | Greyed, still there |
| Session ends cleanly | `status/now` = {working: false, last, next: "waiting on Adam: ONE SHEET or FOLD"} | STANDBY |
| Session dies (no clean end) | nothing | Heartbeat older than 20 min → page shows STANDBY "last seen 14:02" automatically |

Key rule: **events are cheap (one db row), publishes are batched** (after a sheet set, a score, a lock; not every file). Event rows carry text; images only arrive with a publish. The page can say "3 new items, arriving with the next publish" if an event points at an item not yet in the snapshot.

**When nothing is running (STANDBY):** the page is a calm landing page: the project, the stage strip with "now" marked, the current version, the last event and when, and **what's waiting on Adam**. This is the default state most of the time, so it has to be the best state, not an empty one.

Make it automatic, not a discipline: a small `site/publish.sh` (or a line in the HANDOFF "after each step" list) so every session does it the same way. Without this, live-update rots in a week. Note for the builder: once Adam has tags in GitHub, they're a second source for locks.

### 6. Flows (draft)

- **F1 Arrive (J1, J11, J12):** open link → see project name, ON/STANDBY light, stage strip, current version, "waiting on you", and "since you last looked: N new". (Per-person "last looked" via `artifact` state.)
- **F2 Browse what's made (J2, J9, J13):** filter by one axis at a time: stage, or kind, or version. Dropped items shown greyed.
- **F3 Open an item (J14, J7):** sheet → zoomable full view; doc → readable text; test → plot + play + pass/fail + which variant.
- **F4 Walk history (J4):** reverse-chronological events, grouped by day, with decisions in his words.
- **F5 Open a version (J5):** version page: date, one line, what changed from the one before, its contents.
- **F6 Compare (J10):** from an item, step through its lineage, or put two forms side by side / overlay-swipe.
- **F7 Share (J8):** every item, version and day has a copyable link. Whole-site sharing is done by Adam in claude.ai.

### 7. Three directions (different in kind, not styling)

**A. The Lab Book** (lab notebook + "work at a different speed")
The site is one bound, dated notebook. Each entry is a page: date, what was tried, the result, the figures pasted in (sheets, plots, a sound). Locks are "signed and witnessed" pages. One control only: a **speed dial** with three detents: **Day** (every event), **Round** (one entry per round: what went in, scores, outcome), **Version** (only locks and stage changes: the whole project on one screen). Same content, three grains of time. Strength: history *is* the interface, so J4 and J3 are free; J1 is the top of the book. Risk: finding "all sheets of FOLD" (J13) needs a second way in. Lineage links inside an entry ("this sheet's earlier forms") cover J10.

**B. The Shelf** (cassette J-card)
Versions and rounds are **spines** stacked on a shelf, newest on top. One spine is "in the deck": the current one, open, its contents listed like a track list (A sheets, B sheets, spec, tests). Exploration rounds are demo tapes (a different, lighter spine). Dropped ones stay on the shelf, greyed. Strength: J5 and J9 are the first thing you see; very compact on a phone (a spine is one line). The J-card's track list is a nice form for "what's in this version." Risk: live events (J3) have nowhere obvious to go; needs a "now playing" strip at the top. Risk of costume: must stay abstract (a row is a spine; no cassette graphics). Owner is a musician, so the metaphor lands, but it shouldn't be decorated.

**C. The Panel** (abandon normal instruments + one screen, no navigation)
The site is a device front panel, not a website. One screen. Top: power light (ON/STANDBY) and the project name. A **stage selector**: the build chain as a row of positions, like a Braun selector switch; the current stage lit. Below it, what that stage holds. And a **time slider** like a tape counter: drag back and the whole panel shows the project *as it stood then* (versions are detents on the slider). View = stage × time. Strength: J1, J6, J11 in one glance; the Braun fit is literal (less, but better; every control does one thing). History becomes "go back to a moment" rather than reading a log. Risk: a log of decisions in his words (J4) doesn't fit a slider well; the "as it stood" model needs the builder to compute snapshots from the manifest (doable: items have dates and statuses). Phone: selector becomes a horizontal strip.

**Inversion I'm putting on the table** (not a full direction yet): the landing page shows **only what changed since you last looked**, and everything else is one step behind it. "Less, but better" taken literally. Could be the F1 layer on top of any of A/B/C. I'd fold it in rather than make it a fourth concept.

**Rule for all:** greyed, never removed (twist draw). Render code and sim logs never shown. Each item has one URL.

### 8. Open questions (for the owner, one at a time, via the orchestrator)

1. **Who will you share it with?** If people who aren't signed in to claude.ai, they see the last published snapshot, not live updates. If it goes outside the team, should private records (owner notes, scores) be hidden from them?
2. Should the site also cover the paused work in `archive/` (full-instrument clone, paused concepts), or start from Little D round 1?
3. (For the team, not the owner) Artifact vs. GitHub Pages: the artifact gets `db` live updates and claude.ai sharing; GitHub Pages would be public by default and couldn't do the live wire without a backend. I lean artifact. Visual designer / director: object if you see otherwise.

NEXT: product designer (visual focus) — the three directions differ in how they *work*; they need a look-and-feel pass (Braun panel vs. notebook vs. shelf, and the ON/STANDBY light) before the director can steer which to push.
