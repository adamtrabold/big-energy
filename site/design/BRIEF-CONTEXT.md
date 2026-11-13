# Project site: shared brief context (orchestrator, 2026-11-13)

Every teammate on the site work gets this file. Repo root: `/home/claude/big-energy/`.

## The owner's words for this task (verbatim)
> "rather than interact through here, i'd like to interact through a web interface that is built on the fly for the versioning and serves as a landing page for the project. can you have a team spec this out? it should live update there as things from here are made and explored, and i want to be able to see the history and versions and see anything that's created (explorations, mocks, layotus, diagrams, etc). it should be shareable and minimal ui in the style of dieter rams / braun"

## Who and what
- Owner: Adam, Director of Product Design (and designer, musician, MFA). He often reads on a phone. He wants short, plain words. He gets asked open questions one at a time.
- The project: designing and building a portable Model D-style synth ("big energy" repo; the name is still open, see `design/naming.md`). Work is done by Claude sessions running a design team (orchestrator, designers, director, etc.) and committed to this git repo.
- Records to understand what the site must show: `HANDOFF.md` (project overview and folder map), `VERSIONS.md` and `versions/` (locked sets), `design/owner.md` (owner decisions, verbatim), `design/scores.md`, `design/jam.md`, `design/concepts/` (concept docs plus A3 mock sheets, PNG 4961×3508), `design/branches/` (a creative round starting now), `eng/` (engineering research and spec), `explore/`, `archive/`. Browse `git log` for history.
- Existing viewing page: an artifact "Model D — locked v1.1 + handoff" (https://claude.ai/artifact/69aSiNmeYuxmDuSoBdhpFD). Only for viewing sheets today.

## Where it would live: facts, checked by the orchestrator
- A claude.ai **artifact**: a hosted web page with its own URL, private to the owner until he shares it (sharing is done by him in claude.ai; Claude can't change who sees it). Claude publishes new versions of it from any session.
- No ready-made artifact type fits a project landing page (types available: Data, Design, Design System, Docs, Sheets, Slides, Whiteboard), so it would be a hand-built page. A type could still be used inside it or linked from it if that serves a job.
- Page capabilities (runtime contract 0.2.96). For details, call the `describe_capabilities` tool with a capability name if you have it; otherwise ask the orchestrator.
  - `comments`: the page's own commenting UI wired to the artifact's comment store. Claude can read comment threads the owner sends to Claude.
  - `db`: data outside the page (shared rows, per-person state, data Claude reads and writes).
  - `assets`: stored uploaded assets (images, SVG, video, PDF).
  - `files`: reads a Claude Code project's files as the viewer (needs the project's id).
  - `artifact`: the page remembers what people do with it.
  - Also `room` (who has it open now), `user` (who is viewing), `downloads`, `sample` (ask Claude), `mcp` (the viewer's connectors), `dictation`, `tts`.
- "Live update" is a real constraint: nothing changes on the page unless a Claude session publishes, writes data or uploads assets. The design must say what a session does after each event, and what the owner sees when nothing is running.
- Alternatives (GitHub Pages from the repo, etc.) are open for the team to weigh. Git tags can't be pushed from these sessions (the proxy returns 403).

## Settled vs. open
- Settled: the owner's words above. Minimal UI in the Dieter Rams / Braun style. Shareable. Shows history, versions and everything created. Live-updating. It's the project's landing page.
- Open: everything else, including how much he interacts there (view only, or also feedback, decisions and answering questions), structure, how updates flow from sessions, what "anything that's created" includes, and how it looks. The orchestrator will put the interaction-depth question to the owner; design for the range until he answers.
- The phase: CONCEPT (spec). Prototypes outside the real thing are allowed and encouraged when an idea only shows when used. Nothing is published as the real site until the owner approves a concept.

## Work files
- Folder: `site/design/`: `jam.md`, `jobs.md`, `concepts/<name>/`, `scores.md` (the orchestrator writes it), `owner.md` (owner record), `notes/{systems,visual,director}.md`.
- Commit nothing; the orchestrator commits.
