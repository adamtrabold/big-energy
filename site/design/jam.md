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

---

## Turn 2 — product designer (visual focus), 2026-11-13

Sketch sheet: `site/design/concepts/jam-sketches/visual-jam2.png` (source `visual-jam2.py`, renders with real content: FOLD sheet A v1.1, the golden `voice_bass_pluck.wav` waveform, owner quotes verbatim). Phones drawn at 1:1, 390 × 844.

### 0. What applies (from the owner, the brief and the records)
- **Rams as principle, not costume.** Useful, honest, understandable, as little design as possible. So: no fake knobs, no brushed metal, no cassette graphics, no skeuomorphic switches. A "selector" is a row of words with one marked. If a direction only works dressed up, it's the wrong direction.
- **The frame recedes; the work carries the colour.** The sheets already have a strong look (cream ground `≈#F3EFE8`, red-orange accent, Inter, walnut/white renders). The site must not compete. That one rule sets the palette below.
- **Phone first.** He reads on a phone. The A3 sheet (4961 × 3508) and the WAVs are the hard cases, so I sketched those properly.
- **Viewing only** (11:52). No feedback UI.
- **The project has no name** ("little D is a terrible name"). The site shows `( name to come )`, same as the sheets. The title is one field in the manifest, swapped when he names it.

### 1. Draws (real randomness: Python `random.SystemRandom`, tag cd6dbb85)

| Draw | Result | What I did with it |
|---|---|---|
| Direction to attack first | C | Did C's pass first; it absorbed the cabinet draw |
| Oblique 1 | "Remove specifics and convert to ambiguities" | The landing shows **counts and marks, not titles**. C's cabinet is numbers in cells; specifics are one tap behind. |
| Oblique 2 | "Remove specifics…" again (duplicate draw, recorded) → redrawn: **"Distorting time"** | A's **fisheye rail** (today wide, yesterday narrower, last week a hairline). C's scrubber spaces rounds and locks **evenly by event**, not by clock time. |
| Unrelated field 1 | a sundial | Time as a *position you move to*, not a list you read (C's scrubber). And: a sundial needs no power; **STANDBY must be a complete reading on its own**, not a "nothing's happening" void. Agrees with systems' §5. |
| Unrelated field 2 | a pharmacy drawer cabinet | **C becomes a cabinet**: a grid of labelled drawers, stage × kind, each with a count; empty drawers shown, so he sees the road ahead. (Also the nearest honest Rams reference: a grid of identical modules, the 606 shelving logic, without imitating it.) |
| Constraint | no scrolling on the landing view | Applied to **all** directions: the first screen holds lamp, name, stage, waiting-on-you, and what's new. Anything else is below or behind. |
| Twist | the owner's own words are the largest type | Became **A's spine**: each Lab Book entry is headed by what he said, verbatim, at 27 px; the team's work sits under it as figures. History reads as *decisions → consequences*. |
| Accent hue (0–359) | 131 | Green. Used for **ON and nothing else**. Lucky fit: no red/orange in the frame, so it can't be mistaken for the sheets' accent. |

### 2. Shared visual system (every direction uses this; it's what makes them comparable)

**Colour** (checked against WCAG on the ground):
| Role | Hex | Note |
|---|---|---|
| ground | `#E6E4DF` | warm light grey, a step darker/cooler than the sheets' cream, so a sheet reads as a *sheet lying on the page*, edge visible with no border or shadow |
| cell | `#EFEDE9` | filled drawers, the audio row |
| rule | `#C4C1BA` | 1 px hairlines; the only dividers |
| ink 2 | `#5F5D58` | meta text, 5.2:1 on ground (my first pick, `#6B6963`, was 4.3:1: failed small text, changed) |
| ink | `#1B1B19` | text, 13.6:1 |
| ON | `#23863F` | the lamp only, 3.6:1 (non-text ≥3:1; my first pick `#2F9A4C` was 2.8:1, changed) |

No red or orange anywhere in the frame. No shadows, no cards, no rounded containers. Corners square; only the lamp and the play button are round.

**Type:** **Inter**, self-hosted (subset woff2, so the page never depends on an outside font host). Reason: it's the sheets' own face (`_mock-src` renders in Inter), so the frame and the work read as one. Tabular figures on, always (counts, times, revs line up; the scrubber's numbers don't jitter). Four sizes on the phone: **27** (his words, A only), **22** (project name), **15** (items/body), **12.5** (meta), plus a **10.5 caps, +0.9 tracking** label for section names. Weights 400/500/600/700, nothing else.

**Grid:** 8 px base. Phone: 16 px margins, one column with a 56 px left gutter where needed (A's rail, C's row names). Desktop: 12 columns, max 1280, 24 px gutters.

**The status lamp: three states, and it never lies.**
- **ON**: filled green dot, steady. Label in ink: "On · round 6 sheets · since 14:02". When an event lands, the lamp dips once (600 ms, to 40% and back). It never pulses at rest; a light that breathes all day is nagging.
- **STANDBY**: hollow ring in ink 2. Label: "Standby · last 14:02 · waiting on you". Going ON→STANDBY, the dot fades over 1 s, like a filament cooling. The only decorative motion in the whole site, and it carries meaning.
- **SNAPSHOT** (signed-out viewer, `db` is null): **no lamp at all**, a short rule in its place, label "Snapshot · 13 Nov 14:02". Showing STANDBY to someone who can't receive live data would be a lie.

**New since you last looked:** a 6 px ink dot beside the item (or in a drawer's corner, or a Δ in D). Not green: green means *live*, the dot means *unseen*. One colour, one meaning.

**Dropped:** 40% opacity **plus the word "dropped"** (opacity alone fails for low vision). Never struck through, never hidden.

**Tests: pass/fail** in words, caps, `PASS` 500 / `FAIL` 700. No traffic-light colours (see open question 3).

**An A3 sheet on a phone** (all directions; this is the hardest screen and the one he'll use most):
1. **Fit-width first.** 358 px wide is unreadable on purpose: it's the map. Caption above: "FOLD · sheet A — the look · v1.1 · rev F · 4961 × 3508".
2. **Read mode** steps through **crops**: 1 the hero, 2 principles, 3 the spec strip, each crop at full phone width, numbered boxes on the map. The crop boxes come from the sheet renderer: `sheets_r5.py` already places every block at explicit mm coordinates, so it can write a small sidecar (`mock-A-look.regions.json`) at render time. Sheets without one fall back to step 3.
3. **Pinch to full-res** anywhere, any time (tiles or a 3200 px image; the original PNG only on "download").
4. Swipe or ‹ › steps to the next sheet in the set. Turning the phone to landscape gives the whole sheet edge to edge.
Images: WebP 1600 w (≈ fit view at 3× DPR), 3200 w (zoom), original PNG (download).

**An A3 sheet on desktop:** the sheet at full content width (up to 1600 px), on the grey with no frame; caption below; ← → for the next sheet, `Z` for 1:1 with drag-pan. **Compare (J10):** desktop puts two versions side by side; phone uses a **wipe** (one image over the other, drag a vertical hairline). Same control as A/B audio below.

**A test with its sound:** full-width row in `cell` grey. One round play/stop (44 px, ink outline), the waveform as a **static peak line** pre-drawn by `build.py` (an SVG; no audio decoding to show it), a hairline playhead, time in tabular figures, title "Bass pluck · golden", meta "PASS · 48 kHz". **A/B: golden | perturbed** switches the file and **keeps the playhead**, so he hears only the difference. One sound at a time: starting one stops the other. No volume slider (the phone has buttons). Plots (filter AC, VCO tracking) are shown like small sheets.

**Motion, all of it:** a new row inserts at the top, 180 ms ease-out height + fade, no bounce. Scrubber detents snap (haptic tick where the browser supports it; iOS Safari doesn't). The lamp's dip and fade. That's the list. `prefers-reduced-motion` → all instant.

### 3. The directions, look and feel

**A · Lab Book — keep, sharpened.** *Time-first.*
- **Phone:** lamp line → name → **Waiting on you** (one line, 15/500) → the entries. Each entry: date and time small, then **his words at 27 px**, then one line of consequence ("→ branches round opened"), then figures (sheet thumbnails in pairs, captioned "fig. 1 FOLD A · new", dropped ones at 40%). **A lock is a ruled, signed page**: double 1.5 px ink rule, "LOCKED v1.1 · 13 Nov" in caps 700.
- **Fisheye rail** in the left gutter (distorting time): today's bar is long and black, yesterday shorter, older days hairlines. The page *feels* like recent work is big and old work is compressed, because it is.
- **Speed dial** (systems' Day / Round / Version) at the bottom, three words, the current one underlined. Thumb reach.
- **Desktop:** the text column at 6 of 12 columns (≈ 640 px measure, readable), figures in the right 6 at larger size, rail in the left margin.
- **Feel:** calm, literary, reads like his own notebook. Best at J4 (history) and J3 (it's a feed). Weakest at J13 (find all FOLD sheets) and J6 (stage is only a line in the header).
- **Risk:** his words as the biggest thing on a *shared* page. If the link goes outside the team, this direction exposes the most (systems' open Q1).

**B · Shelf — drop. Donate its parts.** It's the closest to a costume (a row of spines is just a list; calling it a tape adds nothing he can use), and the systems designer already found live events have nowhere to go. What's good in it lives on: **the track list** becomes how every direction shows "what's in v1.1" on the version page; **spines as one-line rows** are D's revision table; **versions as detents** are C's scrubber.

**C · Panel → Panel + Cabinet — keep, reshaped.** *Structure-first, one screen.*
- **Phone, no scroll:** lamp line → name → **the cabinet**: 9 rows (the build chain) × 5 columns (sheets · diagrams · docs · tests · records), 56 × 50 px drawers. A drawer with things in it is filled `cell` grey with a count (16/500, tabular); an empty one is an outline with a `·`; future stages read in ink 2. The current stage has a 3 px ink bar at its left. Unseen items put a dot in the drawer's corner. **Tap a drawer → it opens** (a list of its items, newest first).
- **Scrubber** at the bottom, in thumb reach: one 1.5 px line, rounds as short ticks, **versions and "now" as long ticks**, an ink block as the handle. Drag back and every count changes to what it was then; the label reads "12 Nov 22:30 · as it stood". This is the sundial: you move to a time.
- **Desktop:** the cabinet in the left 5 columns, the open drawer's contents in the right 7 (master-detail, no page changes); scrubber across the full width.
- **Feel:** an instrument. Every control does one thing. The closest honest fit to Braun, and the best 10-second landing (J1, J6, J11, J12 in one glance).
- **Weak at J4:** decisions in his words have no home in a grid. Fix inside the direction: the "records" column's drawer at the current stage *is* the decision log; and the lamp line's text shows the last decision when STANDBY.
- **Note for systems:** "Tests" is both a **stage** and a **kind** in your model, and sims already exist at the Concept stage (9 tests in my sketch sit under Tests, but some belong to Concept). I'd make tests a **kind only** and rename the stage **Breadboard** (the physical bench tests). Then the grid has no duplicate axis.

**D · The Set — new, differs in kind.** *Document-first.* Forced connection: an **architectural drawing set**. It's the language of his own profession and of the sheets themselves (A3, title row, "sheet A — the look").
- **Every publish is an Issue** ("Issue 14 · 13 Nov 14:02"). The landing is a **title block** (ruled box: name, current set, issue, status lamp) → a **revision table** (v1.1, v1, R5: rev · date · one line; current row in ink, older in ink 2) → a **sheet index**: every item with a number (FOLD-A, FOLD-B, HUSH-A…), title, current rev letter. Dropped ones stay in the index at 40%.
- **Changed since you last looked = the revision triangle** (Δ with a number), the standard drawing-set mark for "this changed in this issue". No new symbol to learn; he already reads it.
- Index sections: Design · Tests · Spec · BOM · Boards · Records. Tap a row → the sheet viewer above, with the item's own revision list (rev A → rev F) for J10.
- **Desktop:** the index as a full-width table (no · title · rev · date · stage · Δ), title block top right like a drawing's.
- **Feel:** dry, exact, professional: a good architect's office. Best at J5, J9, J10, J13 and per-item sharing (J8: "send FOLD-A rev F"). Weakest at J3/J11 *feeling* live: an issue register is a static thing by nature; the lamp and the Δs carry live.
- **Risk:** sheet numbers have to be stable across rounds. The builder would need a numbering rule (concept prefix + sheet letter, docs get D-numbers, tests T-numbers).

**Systems' inversion** ("only what changed since you last looked"): I agree it's a layer, not a concept. Each direction shows it in its own mark: A = the dot on entries plus a thin "you stopped here" rule; C = dots in drawer corners; D = Δs.

### 4. Where I land (for the director to steer)
- **Take A, C, D to concepts. Drop B.** They differ in kind: time-first, structure-first, document-first.
- My lean: **C** is the strongest Rams fit and the best landing; **D** is the dark horse because it speaks his professional language and gets versions/revisions right for free. **A** is the most enjoyable to *read*, and the one most at risk if the link is shared widely.
- I'm *not* proposing a three-tab hybrid (C home, A history, D index) yet: that's the mush risk. If the director wants one, it should come from a winner absorbing one part of another, not from stacking.

### 5. Open questions
1. (Owner, via orchestrator; it's the same as systems' Q1 and it decides A) Who sees the link? If people outside the team, his verbatim words as headline type may be wrong.
2. (Team) Can a claude.ai artifact page self-host a woff2 font (via `assets`/`files` or inlined)? If not, the fallback is the system stack, which on his iPhone is SF: fine, but the frame and the sheets stop sharing a face.
3. (Owner, later) Test failures in words only, or does he want a colour for FAIL? I'd hold to no red: red is the sheets' accent and the CUTOFF knob's.
4. (Team) Dark mode: yes via `prefers-color-scheme` (charcoal ground `#1F1F1D`, the sheets keep their own cream)? I lean yes, but it's a second palette to keep honest.
5. (Systems) Region sidecars for read mode: needs a small change to the sheet renderer. Worth it? I think so; it's the single biggest thing for phone reading.

NEXT: design director — three directions that differ in kind (A Lab Book, C Panel+Cabinet, D The Set) now each have a look-and-feel; B is proposed dropped. The director should steer which go to concepts before systems writes `jobs.md` and we build them.

---

## Turn 3 — design director, 2026-11-13

Read: the brief context, `owner.md`, turns 1–2, `visual-jam2.png`. Good work, both of you. The shared system (repo is the truth, three-state lamp, green = ON only, greyed never removed, the A3-on-a-phone viewer, A/B that keeps the playhead) is strong and **settled for every concept**. I'm not re-opening it. My job here is the directions.

### 1. What I see on the sketch sheet

Put the three phones side by side and one thing jumps out: **the landing screens are words and numbers.** A leads with a quote, C with a grid of counts, D with a table. The only screen where the *work* is the biggest thing is the shared sheet viewer, one tap in.

The owner's own list is visual: "explorations, mocks, layouts, diagrams". He's a designer with an MFA, and the thing he'll open the site for, nine times out of ten, is *what did the team make, let me look at it*. None of our directions answers that on the first screen. That's the gap. It doesn't mean all three are wrong; it means one concept has to be **work-first**, so we can tell whether he wants an instrument, a register or a wall.

### 2. Draws (real randomness, Python `random.SystemRandom`, tag 4fb023c0)

| Draw | Result | What I did with it |
|---|---|---|
| Oblique 1 | "Repetition is a form of change" | **Lineage by repetition**: show the same sheet small, in a row, r3 · r4 · r5 · v1 · v1.1. You see what changed because everything else stays still. Goes into E, and replaces "revision list" as the J10 answer in every concept. |
| Oblique 2 | "Water" | Read as *level*, not *flow*. A feed is flow (that's A). A level is a reading you take: how far down the build chain the water has risen. Backs C's stage rows as a fill level, and the rule that STANDBY is a complete reading. |
| Unrelated field | a herbarium | **Direction E** (below). A herbarium is the exact model for "keep everything, never throw away, revise without erasing": every specimen mounted on the same size sheet, one label in the same corner, and when someone re-identifies it they add a small slip on top, the old label stays. |
| Twist | everything fits in a 600 px column | E's layout: one column, max 600 px, on phone *and* desktop. On desktop that's a deliberate measure on a wide grey field, like a mounted sheet, not a narrow website. |

### 3. Rulings

**B · Shelf: dropped.** Agree with visual. A list of spines is a list; the tape adds costume, not use. Its parts are already donated (track list for the version page, detents on C's scrubber). Done.

**A · Lab Book: retired as a concept. Its parts go into the others.** Being hard on it, since it's the easiest one to like:
- A feed of dated entries is the most conventional answer here (it's a changelog), and it's not *the best* conventional answer, because a feed is worst at the two things the owner named most: versions and "anything that's created". You scroll past work, you don't look at it.
- His words at 27 px make the site about the chat, and he told us the chat is the chat (11:52). The site is for the team's work.
- On a shared link it exposes the most.
- What survives, in every concept: **the history view has three grains, Day · Round · Version** (systems' speed dial), decisions appear **verbatim at body size** with the work they caused under them, and **a lock is a ruled, signed line**. That's A's best idea and it belongs in a history view, not as the landing.

**C · Panel + Cabinet: concept.** The best 10-second Braun reading we have. Push:
1. **A grid of counts isn't a landing for a designer.** "58" under Concept/Sheets tells him nothing to look at. Keep the cabinet, but the landing must also answer *what's new and what should I look at*: either the newest drawer shows its newest item as a small image, or the lamp line names it. Prove it doesn't feel like a spreadsheet.
2. **Most of the grid is empty dots** (6 of 9 rows today). That's the honest "road ahead", but prove it reads as *level* (the water draw: filled up to here) and not as an unfinished site. Try fewer columns: does "records" earn a column, or does it live in the history view?
3. **The scrubber has to earn its cost.** "The project as it stood" means the builder computes past states. Show one real case where it tells him something he'd want: drag to r3 and FOLD-113 is still alive and HUSH has 2 sheets. If you can't find one, cut it and say so.
4. Ruling on visual's note: **tests are a kind, not a stage. The stage is renamed Breadboard.** Systems, adopt it in the model.

**D · The Set: concept.** It speaks his professional language and the sheets' own (A3, sheet letters, revs). Push:
1. **No-scroll landing vs. a 100-row index.** Prove the phone landing holds title block + revisions + *only the sections, with counts and Δs*, and the index opens per section. A wall of rows is not Braun.
2. **It must feel live.** An issue register is static by nature. Show the ON state: what changes on screen when an event lands mid-session (a row gets a Δ, the issue line ticks, "issue 15 in progress").
3. **Stay textual.** Don't add thumbnails to the index to fix #2. If D grows images it turns into E. Its bet is that exact names and revs are enough on the landing; let it win or lose on that.
4. Write the **numbering rule** (FOLD-A, D-numbers for docs, T-numbers for tests, R-numbers for records) and show it holds across the archive and the next round.

**E · The Herbarium: new concept.** *Work-first.* (The name is ours; the site never says "herbarium". No botanical anything on screen.)
- **Every item is a specimen**: the work itself, mounted on the grey ground at a standard size, with **one label in the same corner, same fields, for every kind**: number · title · kind · stage · rev · date · status. A sheet shows the sheet; a test shows its waveform or plot with play; a doc shows its first page set as text; a diagram shows the diagram.
- **Revisions are slips on the label**, not a separate page: "rev F · 13 Nov · stands at 120°" on top, "rev E · 12 Nov" under it, older ones folded. History lives on the thing.
- **Lineage by repetition** under the specimen: the same item small, in a row across rounds and versions. Tap one to swap; on desktop, two side by side.
- **Landing, no scroll:** lamp line → name → waiting on you → **the newest specimen, large**, with "+ 6 more since you last looked" as a single line. Scroll down: the rest, newest first. A filter row (stage · kind · version, one at a time) is the only control.
- **One column, max 600 px, everywhere** (the twist). Desktop = the column centred on the grey, sheets open wider on tap.
- **Must prove:** (1) where versions live and how he sees "what's in v1.1" (the track list, as a filtered set with its own URL); (2) where the build-chain stage shows, since it's weakest at J6; (3) that a doc and a test make good specimens, not just sheets; (4) that it isn't just a gallery: the label + slips + lineage are what make it a record, so they must be visible at landing size.

**Three concepts go forward: C (structure-first), D (document-first), E (work-first).** They differ in what the landing hands him first: a reading, a register, or the work.

### 4. Rulings on the open questions to the team

- **Artifact, not GitHub Pages.** Agree with systems: claude.ai sharing + `db` live wire. Signed-out viewers get the snapshot. Settled.
- **Font (visual Q2):** checked by the orchestrator: `assets` stores fonts and CSS/JS, so **self-host subset Inter**. Settled.
- **Dark mode (visual Q4): not in the concepts.** One palette, done well. Revisit at build.
- **FAIL colour (visual Q3):** hold to words only for now. Not an owner question yet; it becomes one when there's a real failing test to show him.
- **Region sidecars (visual Q5):** yes. Concepts may assume read-mode crops on FOLD sheet A; the builder adds the sidecar later.
- **Archive (systems Q2): include it, greyed, as dropped.** That's the "nothing removed" rule; we don't need to ask him.
- **Live-update has to be automatic**: `site/publish.sh` + a line in HANDOFF's after-each-step list. Every concept assumes it.

### 5. Same test for every concept (so I can score them against each other)

Each concept is a set of phone frames (390 × 844, real content) plus one desktop landing:
1. Landing, **STANDBY now**: waiting on you = "ONE SHEET or FOLD" and the name.
2. Landing, **ON**, the moment an event lands ("FOLD sheet D rev H").
3. Get from landing to **FOLD sheet A v1.1**, then to its **v1** form to compare. Count the taps.
4. **Bass pluck · golden vs perturbed**, with A/B.
5. **Find the decision "Switch to Daisy Seed"** (or the nearest real one in `owner.md`) and the work it caused.
6. **"What's in v1.1"**.
7. The same landing as a **signed-out snapshot**.
8. Desktop landing.

### 6. Questions only the owner can answer (orchestrator: one at a time, these words)

1. "Who will you send the link to? Just you, or people outside the team too? If outside, I'll keep owner notes and scores off the shared view."
2. (After concepts, only if needed) "Do you mainly open it to *look at the newest work*, or to *see where the project stands*?" — Hold this one: the concepts should answer it by showing him, not by asking.

NEXT: product designer (systems focus) — write `jobs.md` with the rulings above (tests as a kind, Breadboard stage, history grains, archive included, the 8-frame test), then the two designers split C, D and E and build concepts.

---

## Turn 4 — product designer (systems focus), 2026-11-13

Read turns 2–3 and the two new owner answers. I take every ruling. This turn turns them into one model all three concepts (C Cabinet, D Set, E Herbarium) build on, and fixes some facts the concepts will trip on.

### 0. New owner answers (12:06), and what they change
- **"anyone that gets the link is fine to see everything"** → one view for everyone. No hidden records, no shared-view filter. Drop that from the model. Signed-out viewers still get the snapshot (that's a technical limit, not a privacy one).
- **"it is primarily me"** → design for Adam first. That settles a tie-break rule for every concept: when a choice helps him or helps a stranger, pick him. Example: "waiting on you" stays on the landing even though it means nothing to a guest; "since you last looked" is his, per-person.
- This also partly lifts the director's objection to A ("exposes the most"). A stays retired for the other reasons (feed is worst at versions and at looking at work).

### 1. Draws (Python `random.SystemRandom`)
| Draw | Result | Fed |
|---|---|---|
| Oblique | "State the problem in words as clearly as possible" | The one-sentence problem at the top of `jobs.md`. Every job has to serve it. |
| Unrelated field | a museum accession register | **The numbering rule** (§3): an item gets its number the moment it arrives, the number is never reused or changed, and later changes are recorded against it. |

### 2. Model changes from the rulings
- **Stages** (the build chain, ordered): Concept → Lock → Handoff → Spec → BOM → **Breadboard** → Boards → Prints → Assembly. Tests is no longer a stage.
- **Kinds** (one per item): **sheet** · **diagram** (sketches, system drawings, plots that aren't test results) · **doc** · **test** · **record** (owner record, scores, jams, notes, naming). Five kinds. The director asked C whether records earn a column; I'd keep the *kind* (D and E need it for labels) and let C decide whether it's a column.
- **Stage of an item** = the stage it was made in. Sims made during concept rounds are stage Concept, kind test. When Breadboard starts, bench tests are stage Breadboard, kind test. A test can be re-run; each run is a rev.
- **Status** (unchanged): current · locked in vN · exploring · dropped. **Archive is included, greyed, status dropped** (ruling).
- **History has three grains**: Day · Round · Version. Decisions appear verbatim at body size with the work they caused; a lock is a ruled, signed line.
- **Lineage by repetition** replaces the revision list as the compare answer (J10) in every concept.

### 3. Numbering rule (accession register; D asked for it, E's label and C's drawers need it too)
One rule, every kind:
- **Sheets:** `CONCEPT-LETTER`: `FOLD-A`, `HUSH-C`, `ONESHEET-B`. A variant that became its own line gets its own code: `FOLD113-A`. Archive: `TYPECASE-A`, `HYMNAL-A`, `UNDERGLASS-…` (docs only).
- **Everything else:** kind letter + number, given in order of arrival, never reused: **D**-docs (`D-014`), **G**-diagrams (`G-003`), **T**-tests (`T-007`), **R**-records (`R-001` = owner record).
- **Revs** are letters on the item: `FOLD-A rev F`. A rev is added only when a session says it changed (a commit that changes the file + an event naming it). Byte differences alone don't count: `versions/v1` vs `v1.1` HUSH sheets differ in bytes though the changelog names only FOLD and the bend drawing; a re-render isn't automatically a new rev to look at. The event says what changed ("stands at 120°"), and that line becomes E's slip and D's revision table row.
- **Moves don't change numbers.** A sheet that moves from `design/` to `versions/` or `archive/` keeps its code; the path is just where it lives now.
- `site/numbers.json` holds the register (code → current path, kind, stage, revs). Only a session appends to it. Backfill once.

Holds across the archive (codes above) and the next round (branches concepts get new concept codes; a new FOLD sheet F is `FOLD-F`).

### 4. Facts the concepts must design around
1. **Old forms mostly don't exist as images.** The restructure squashed git to one commit; rounds 1–4 sheets weren't kept, except `archive/fold-superseded/` (older FOLD-105 sheets A–C + `mock-E-standing-105-r5old.png`) and the paused concepts' final sheets. So today a typical lineage row is **2–4 forms** (archive older · v1 · v1.1 · current), not r3 · r4 · r5 · v1 · v1.1. From now on every commit keeps every rev, so rows grow. **E and D: draw lineage rows with the real counts; show missing rounds as a labelled gap ("r1–r4 not kept"), not a fake.** That's honest and it's the "nothing removed" rule applied to what was already lost.
2. **C's scrubber, real case.** The records can tell past *states* even where images are gone: `scores.md` has rounds 1–5 by date with which concepts were in each; `owner.md` has dated decisions. Real case for frame-test: drag to **Round 2 (12 Nov)** → six concepts alive including TYPE CASE and HYMNAL (since dropped), FOLD still one line (113/105 split comes in round 5), no versions yet, Lock stage empty. That's real and interesting ("we had six; four were set aside"). But drawers in the past can only show what was kept, so past counts will be low. C should show the case and decide if it earns its cost; I'd keep it only if it reads as *history of decisions*, not of files.
3. **Frame 5 decision is real:** `design/owner.md` line 114: Q "switch the digital brain to the Daisy Seed?" → Owner: "Switch to Daisy Seed". Caused: `eng/daisy-pin-and-audio-check.md` (before, the evidence), `eng/daisy-first-principles.md` (after, the redesign), and the spec rev in `eng/budget-variant.md`. Note: it has **no timestamp of its own**: it sits in an undated run of entries. Backfill must date it from the surrounding section or git; the concepts can show "12 Nov" for it.
4. **Decision → work links are authored, not inferred.** A session writing an owner decision event lists the item codes it caused (`caused: [D-021, D-022]`). Backfill does it by hand for the dated `owner.md` sections. Without this, frame 5 can't work in any concept.
5. **"Since you last looked"** uses per-person state (`artifact`/`db` user data) for signed-in viewers. Signed-out: no marks (SNAPSHOT shows "as of 13 Nov 14:02" instead). Since it's primarily Adam, this is his feature.
6. **Tap budget (frame 3):** from landing to FOLD-A v1.1 in ≤3 taps, to its v1 form in +1. Frames should state the count. More than 4 total is a fail I'll flag in coverage.

### 5. Push on each concept (how it works)
- **C Cabinet:** a drawer is (stage × kind). Opening it lists items newest first, each with code + rev. On the landing the current stage's row should name its newest item (the director's push #1); I'd put it on the lamp line in STANDBY: "Standby · last: FOLD-D rev H · 14:02 · waiting on you: ONE SHEET or FOLD". Records: as a column, the Concept/records drawer *is* the decision log (opens in Round grain).
- **D Set:** the issue number is the publish counter (`Issue 14`); in ON, events since the last publish make it "Issue 15 in progress" with Δ rows queued in ink 2 until their images arrive. That answers "feel live" without thumbnails.
- **E Herbarium:** the label's fields are exactly the model: code · title · kind · stage · rev · date · status. Stage (J6) can live as a one-line **build-chain strip under the lamp** (the nine stage words, current one marked) on the landing — the only place E shows it, but it's always there. "What's in v1.1" = filter version=v1.1, own URL, shown as the track list.

NEXT: product designer (visual focus) — `jobs.md` is written; the two designers split C, D, E and start concepts against the 8-frame test.
