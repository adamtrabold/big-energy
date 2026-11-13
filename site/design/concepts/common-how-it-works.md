# How it works: shared by every concept (C Cabinet, E Herbarium)

Product designer (systems focus). Rev 3, 2026-11-13 16:30: **hosting is GitHub Pages** (owner 16:23–16:24: public, static, updates on push). §1, §4, §5, §8–§12 rewritten for it; §12 adds Docs, Reviews and prototypes. Rev 2 was concept building systems turn 2. Each concept's own `how-it-works.md` covers its landing, its way in and its history; everything here is the same in both, so the director scores them on how they differ.

Source of truth for jobs: `site/design/jobs.md` (rev 2). Settled rules and the model summary are there.

**D · The Set was killed** (director steer 1). Where its parts went: "show changes" (revision clouds from a real diff) → the shared viewer, §6. The decisions register → the "decisions" view in both concepts, §7. Codes and the numbering rule → §2. Issues and Δ marks: dropped (versions and days cover it; the dot is the one "unseen" mark). The "go to" code field: not carried (he doesn't know codes); links by code still work.

**Changed since rev 1:** read mode and region sidecars removed (owner 12:13); kinds are image · doc · test · record (director); stage = the stage an item serves; "now" defined; responsive, no size leads (owner 12:39); text is HTML, images only where they must be (owner 12:41); concept groups are the new-work model (§3).

## 1. Data the page runs on
Everything is static files built from the repo on each push (no claude.ai artifact, no `db`, no sign-in):
- `manifest.json`: project (name, one line, now stage, current version, waiting on Adam), stages, versions, rounds, groups, items (code, title, kind, sub-type, stage, status, group, revs with date + one line + file + which version holds each rev, lineage, caused-by), doc sets (Docs index with each feature's status word; Reviews), decisions, events, and **build info** (commit time, commit message, short hash).
- `status.json`: copied from `site/status.json` in the repo (working, what, since, last, waiting on).
- Per image rev: WebP at 1200 w, 2400 w, 3600 w (picked by screen width × pixel ratio), original on download; per WAV a waveform SVG. Docs converted to HTML at build (sanitised), images in them rewritten to the web copies.
- Events come from `site/events.jsonl` (sessions append) plus git history; decisions from `design/owner.md` and the session's `caused` lists.
- The page renders from `manifest.json` at once and re-fetches `status.json` and `manifest.json` every 2 min while open (cache-busted). Pages' CDN may serve a file up to ~10 min old.

## 2. Codes (moved in from D)
| Thing | Code | Example |
|---|---|---|
| Concept group | `CONCEPT` | `FOLD`, `ONESHEET`, `BUTTERFLY` |
| Legacy sheet | `CONCEPT-LETTER` | `FOLD-A` (the look), `HUSH-C` |
| New image in a group | `CONCEPT-view` (view slug from the file name) | `FOLD-main`, `FOLD-joint`, `FOLD-rear` |
| Doc | `D-` + number in order of arrival | `D-032` daisy-first-principles |
| Test | `T-` + number | `T-004` voice bass pluck |
| Record | `R-` + number | `R-001` owner record |
| Image outside a group (eng diagram, plot not tied to a test) | `G-` + number | `G-003` |

Codes are never reused and never change when a file moves (design → versions → archive). Revs are letters per item, and per group (§3). A rev is added only when a session says something changed: a byte or pixel change alone isn't a rev (HUSH-C v1 → v1.1 differs by 0.07%, the footer only: it stays rev A).

## 3. Concept groups: the new-work model
Owner 12:41: "images only for things that need to be images — text should be html". So a concept is no longer a set of sheets; it's **a group: its images plus its docs**.

**On disk (what a session makes):**
```
design/concepts/<concept>/            (or design/branches/concepts/<concept>/)
  how-it-works.md                      the group's main doc; the site's layout for the group
  how-it-looks-and-feels.md            further docs (each is an item, kind doc)
  coverage.md
  img/<view>.png                       web-ready images: no text baked in, any aspect,
                                       long edge ≥ 2400 px, sRGB, made to look good on screen
```
- **An image is an item only if a group doc points at it** (`![FOLD standing at 120°](img/main.png "render")`). The alt text is its title; the quoted title is its sub-type (render · drawing · diagram · plot; default render). Order in the doc = order in the group. Loose files (`_mock-src/out/*_raw.png`, `*_tmp.png`, `.scad`) are never items. (Note: `_mock-src/out/` is tracked in git today, 120 files; the `.gitignore` line for it points at an old path. Harmless for the site, because nothing unreferenced shows; flag for the orchestrator.)
- **Captions, labels, dimensions, principles** are text in the markdown, next to the image, never inside it.

**Group revs.** A group has its own rev letters (`FOLD rev D`). A group rev is a snapshot: which member items, at which revs, plus the doc text at that moment. Made when a session writes a "group revised" event at the end of a concept's turn in a round (one per concept per round, not one per file). Inside it, only the members that changed get a new item rev; new views get new codes; a view the round removed is marked dropped in that group rev (greyed in the group's history, not deleted).

**Example: a new FOLD round arrives.** Session renders `main`, `top`, `joint`, `rear` into `design/concepts/fold/img/`, updates `how-it-works.md` (which places all four) → append the event to `site/events.jsonl` → commit → push (the build runs on push) → event `{kind: group_revised, group: FOLD, rev: D, line: "stands at 120°, new hinge", changed: [FOLD-main@A, FOLD-top@A, FOLD-joint@A, FOLD-rear@A, D-0xx@H]}`. The site shows **FOLD rev D** as the newest work; the four renders are new items (rev A each); the doc is rev H.

**Legacy groups.** Each existing concept folder (HUSH, ONESHEET, FOLD, FOLD113, TYPECASE, HYMNAL, UNDERGLASS, the full-instrument concepts in `archive/`) is a group whose images are its sheets, sub-type `legacy sheet`. Their group revs come from where copies live: FOLD rev A = round 5 archive forms, B = v1, C = v1.1. A legacy sheet has no "successor" link to new renders by default; if a session wants to say "FOLD-main replaces FOLD-A", it writes `succeeds: FOLD-A` and the viewer shows "replaces FOLD-A (legacy sheet)" on the label.

**Versions** freeze group revs: v1.1 = `HUSH@B`, `ONESHEET@B`, `FOLD@C` + shared docs (`common-how-it-works`, `common-looks-and-feels`) + spec rev 14 + records at the time. A future lock copies a group's folder into `versions/vN/<concept>/` as today; the build maps the copies back to the same codes.

**Branches round (live now)** is the first real new-format work: `design/branches/concepts/{butterfly,chamber,diptych,rain}/` each have `how-it-works.md`, sketches in `jam-sketches/`. They become groups `BUTTERFLY` etc., status exploring. Their sketches become items when a group doc points at them.

## 4. Status line (J3, J11) — replaces the lamp
No live connection exists on Pages, so the site says only what the last push can prove.
| State | When | Shows |
|---|---|---|
| Updated | always | "Updated 14:02 · BUTTERFLY rev A" (build commit time + the newest event's line). Relative on the landing ("12 min ago"), absolute on hover/tap. |
| Working | `status.json.working` and its `since`/last push under 30 min old | adds "Working · branches round · since 13:40". A small filled dot is allowed (visual's call), but the word carries it. |
| Stale working | `status.json.working` but over 30 min old | drops "Working"; shows "Updated 14:02" only. A session that died never leaves "Working" up. |
| Couldn't check | a re-fetch fails (offline) | keeps what it had; adds "couldn't check for updates". |
| Build failed | the Pages build failed on the last push | the previous build stays up (Pages keeps the last good deploy); the site can't know about the failure, so the session must check the Action/branch result after pushing (publish.sh does). |
The visual designer's ON / STANDBY / SNAPSHOT lamp is retired: "SNAPSHOT" no longer differs from anyone else's view, and "ON" can't be proven live.

## 5. New work arriving (J3)
- A push carries the files and the events together, so there is **no queued state**: when the build lands, the work is there.
- While the page is open, a re-fetch that finds a newer build time: the newest work and counts update in place (route, scroll and open item kept), the "new" marks appear, and the status line changes. One update per build; a group revised event is the main moment ("BUTTERFLY rev A · 6 images · 1 doc").
- A reload or a new visit simply gets the latest build.

## 6. Opening an item (F3; J7, J10, J14, J8)
- **Label** on every item, same fields, same order: code · title · kind (sub-type) · stage · rev · date · status · group. Plus "caused by: <decision, verbatim, date>" and "replaces <code>" when they apply. HTML text, never part of an image.
- **Image** (any sub-type, legacy sheets included): at its own shape, full available width, height capped so it fits the screen → pinch / double-tap / `Z` to zoom to full detail (3600 w copy; original on download) → next/previous image in its group (swipe, ← →) → phone landscape = edge to edge.
- **Doc / record:** HTML, one column; heading jump list for long docs; **wide tables and code blocks scroll sideways inside their own box** (`budget-variant.md` has wide tables); images inside a doc show at column width and open in the image viewer. Links to other items become item links; links to non-items show as plain text.
- **Test:** result in words (PASS / FAIL / RAN, FAIL first in its group), numbers from `metrics.json` as one line, sound (play/pause, static waveform, playhead, time), A/B between the variants that exist (golden · perturbed · worst · guarded), switching keeps the playhead, one sound at a time across the page; plots follow as images.
- **Lineage row** under every image and doc: the same item small (docs: rev letter + one line), oldest left, each labelled with rev and where it lives (archive, v1, v1.1, current). Missing old forms are **one labelled gap** "r1–r4 not kept". Tap a form → the viewer swaps to it.
- **Compare:** desktop side by side (synced zoom and pan); phone wipe. **"Show changes"** (from D): a toggle, off by default, that draws ink scallops around the areas that changed between the two forms. `build.py` computes them at build for consecutive revs of the same image **at the same pixel size**: per-tile difference above a threshold, merged into boxes, capped at 12 boxes ("too many changes to mark" above that, toggle disabled with that line). Not offered when sizes differ or a form is missing. **Docs** compare as text: changed paragraphs marked in the margin with a 2 px ink bar; removed text listed under "removed" at the end (no red/green).
- **Share:** "copy link" on the label → `#/i/FOLD-A@C`. Without `@rev`, the current rev.
- **Dropped item:** opens at full strength; label "dropped · <date> · <reason if the event gave one>".

## 7. Decisions (J4; D's register, in both concepts)
One list, newest first: **date · his words verbatim (body size) · what it caused** (codes as links, "before" for evidence that led to it, "after" for work it caused). The question asked appears above his words in ink 2 when the record has it. Undated entries say "time not recorded". URL `#/d` and `#/d/<n>`. Both concepts reach it in one tap from the landing (each says where).

## 8. Links (J8)
Public URLs. Proposal: **real paths, built as static pages**, not hash routes, so a shared link opens straight to the thing and shows a proper title/preview: `/` landing · `/g/<group>/[<rev>/]` group · `/i/<code>/[<rev>/]` item · `/docs/` index · `/docs/<name>/` architecture or a feature · `/reviews/` and `/reviews/<RV-code>/` · `/v/<version>/` · `/h/<day|round|version>/<key>/` history (Cabinet's old `round/2` view folds in here) · `/d/` decisions · `/s/<stage>/` · `/k/<kind>/`. A `404.html` handles an unknown path ("FOLD-Z isn't in the register" + the landing). Hash routes still work inside a page for in-page state.

## 9. "Since you last looked" (J12) — waiting on the owner
- If kept: `lastSeen` in the browser's localStorage (per device; no sign-in on Pages). Things with a rev or event after it carry the dot; opening one clears it; leaving moves `lastSeen` to now. First visit on a device: no marks, no count.
- If not: no dots; "+ n more since you last looked" becomes "+ n more today".

## 10. States both concepts must draw or answer
| State | Rule |
|---|---|
| Empty stage (Boards today) | Shown, labelled "not yet"; opening it says what will go there ("PCB layouts, board photos, test results"). |
| Stage begun early (Spec today) | Shown as "early" with its items; not "now". |
| Empty kind in a stage | Shown empty in the concept's form; not tappable. |
| Labelled gap | Lineage and history show what wasn't kept as one labelled gap. |
| Group with no images yet (docs only, e.g. a branch's first turn) | The group shows its doc as the work, label says "no images yet". Not an empty frame. |
| Image without a doc pointing at it | Not an item; never shown. |
| Dropped / archived | Greyed in lists with the word "dropped"; never hidden; after current items in a group. |
| Test FAIL | "FAIL" in words, 700; first in its group. No colour. |
| Audio won't load | "sound didn't load · download WAV". Waveform still shows. |
| Image won't load | Label stays; image area "image didn't load · download original". |
| No project name | "( name to come )". |
| Nothing waiting on Adam | "nothing waiting on you" (not removed). |
| Long titles | 2 lines then ellipsis in lists; full in the label. |
| Wide table in a doc | Scrolls inside its own box at every size. |
| Reduced motion | All motion instant. |
| Sizes | Phone < 600 px · tablet 600–1023 · desktop ≥ 1024. Each concept states its layout at each. No size leads. |

## 11. What a session does (summary; detail in jobs.md "Update path")
Start → `site/status.json` working → commit, push. Work → files + `site/events.jsonl` line → commit, push. End → `site/status.json` not working → commit, push. Each push builds the site (GitHub Actions workflow recommended; `gh-pages` branch fallback if the session can't push workflow files). `site/publish.sh` does the status, event, commit, push and checks the build result.

## 12. Docs, Reviews and prototypes (first-class; J16, J17, J18)
- **Docs** (`docs/`): its own place, one tap from the landing in any concept. The index page is `docs/README.md` rendered as HTML, with the index table's status column shown as words (decided / proposed / open / not yet written / started) and a count line ("13 feature docs · 0 written · architecture started"). Architecture and each feature doc render as HTML with the same heading jump list; their links to `../eng/` and `../design/` files become item links. A stub shows its "not yet written" line, not an empty page. Each doc has revs (git history) and lineage as text compare (§6). Stage: Spec.
- **Reviews** (`design/reviews/*.md`): its own place, one tap from the landing. List newest first: date · reviewer (critic, expert) · what it reviewed · score in words if the file has one (e.g. "6/10"). A review opens as HTML; what it reviewed links to those items. New reviews come in with a "review added" event and get the new mark.
- **Logs:** the history view (Day · Round · Version) plus the records (owner record, scores, jams, notes) is the log. If the owner means session transcripts or command logs, those aren't in the repo today; open question.
- **Prototypes:** kind `prototype`. A static prototype (HTML/JS in the repo) is built into the site under `/p/<code>/` and opens full screen with a thin top bar (code, rev, "back"); a prototype that can't run on Pages (needs a server or claude.ai) shows its label and an external link. The Herbarium prototype published on claude.ai becomes the first one once its files are in the repo.
