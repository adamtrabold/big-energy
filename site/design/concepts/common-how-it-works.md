# How it works: shared by every concept (C Cabinet, E Herbarium)

Product designer (systems focus). Rev 2, concept building systems turn 2, 2026-11-13. Each concept's own `how-it-works.md` covers its landing, its way in and its history; everything here is the same in both, so the director scores them on how they differ.

Source of truth for jobs: `site/design/jobs.md` (rev 2). Settled rules and the model summary are there.

**D · The Set was killed** (director steer 1). Where its parts went: "show changes" (revision clouds from a real diff) → the shared viewer, §6. The decisions register → the "decisions" view in both concepts, §7. Codes and the numbering rule → §2. Issues and Δ marks: dropped (versions and days cover it; the dot is the one "unseen" mark). The "go to" code field: not carried (he doesn't know codes); links by code still work.

**Changed since rev 1:** read mode and region sidecars removed (owner 12:13); kinds are image · doc · test · record (director); stage = the stage an item serves; "now" defined; responsive, no size leads (owner 12:39); text is HTML, images only where they must be (owner 12:41); concept groups are the new-work model (§3).

## 1. Data the page runs on
- **Snapshot** (baked into every publish, works for anyone): `manifest.json` = project (name, one line, now stage, current version, waiting on Adam), stages, versions, rounds, groups (code, title, revs, members per rev), items (code, title, kind, sub-type, stage, status, group, revs with date + one line + file + which version holds each rev, lineage, caused-by), decisions, events up to publish time. Plus, per image rev: WebP at 1200 w, 2400 w and 3600 w (the page picks by screen width × pixel ratio), the original on download; per WAV a waveform SVG. Docs are converted to HTML at build (markdown → HTML, sanitised), images in them rewritten to the web copies.
- **Live** (`db`, signed-in only): `status/now` (working, what, since, heartbeat), `events/*` (rows written since the last publish), `data/users/<id>/lastSeen` (J12, per person).
- On load the page renders from the snapshot at once. When `db` resolves it merges newer events and lights the lamp. Nothing waits on `db`.

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

**Example: a new FOLD round arrives.** Session renders `main`, `top`, `joint`, `rear` into `design/concepts/fold/img/`, updates `how-it-works.md` (which places all four) → commit → `build.py` → publish → event `{kind: group_revised, group: FOLD, rev: D, line: "stands at 120°, new hinge", changed: [FOLD-main@A, FOLD-top@A, FOLD-joint@A, FOLD-rear@A, D-0xx@H]}`. The site shows **FOLD rev D** as the newest work; the four renders are new items (rev A each); the doc is rev H.

**Legacy groups.** Each existing concept folder (HUSH, ONESHEET, FOLD, FOLD113, TYPECASE, HYMNAL, UNDERGLASS, the full-instrument concepts in `archive/`) is a group whose images are its sheets, sub-type `legacy sheet`. Their group revs come from where copies live: FOLD rev A = round 5 archive forms, B = v1, C = v1.1. A legacy sheet has no "successor" link to new renders by default; if a session wants to say "FOLD-main replaces FOLD-A", it writes `succeeds: FOLD-A` and the viewer shows "replaces FOLD-A (legacy sheet)" on the label.

**Versions** freeze group revs: v1.1 = `HUSH@B`, `ONESHEET@B`, `FOLD@C` + shared docs (`common-how-it-works`, `common-looks-and-feels`) + spec rev 14 + records at the time. A future lock copies a group's folder into `versions/vN/<concept>/` as today; the build maps the copies back to the same codes.

**Branches round (live now)** is the first real new-format work: `design/branches/concepts/{butterfly,chamber,diptych,rain}/` each have `how-it-works.md`, sketches in `jam-sketches/`. They become groups `BUTTERFLY` etc., status exploring. Their sketches become items when a group doc points at them.

## 4. Lamp (J3, J11)
| State | When | Shows |
|---|---|---|
| ON | `status/now.working` and heartbeat < 20 min | "On · <what> · since 14:02" |
| STANDBY | not working, or heartbeat ≥ 20 min | "Standby · last <event> · 14:02" |
| SNAPSHOT | `db` is null (signed out, or no answer in 10 s) | no lamp; "Snapshot · 13 Nov 14:02" (publish time) |
| Connecting | first ≤ 10 s while `db` resolves | the snapshot line in ink 2, no lamp yet. Never shows STANDBY before it knows. |
| Live paused | `db` was live, then the subscription errors | lamp off, "Live paused · last 14:02". Never pretends ON. |

Heartbeat: a session writes `status/now` at start, with every event, and at least every 10 min while working.

## 5. Events while the page is open (J3)
- New event → the concept's "new" mark appears and counts update; the lamp dips once.
- A **group revised** event is the main live moment: the group becomes the newest work. If its images are already published, they show; if not, the group shows as **queued**: its code, rev, one line and changed codes, image areas saying "arriving with the next publish" (no stand-in picture).
- Many events at once are grouped ("FOLD rev D · 4 images · 1 doc"), one dip.
- When a publish lands, the platform moves open pages to the new version "at their next quiet moment". The page saves route, scroll and open item in `artifact` state and restores them, so the update reads as things filling in, not a reload. Builder to verify; fallback: fetch the new `manifest.json` when an event says `published: true`.

## 6. Opening an item (F3; J7, J10, J14, J8)
- **Label** on every item, same fields, same order: code · title · kind (sub-type) · stage · rev · date · status · group. Plus "caused by: <decision, verbatim, date>" and "replaces <code>" when they apply. HTML text, never part of an image.
- **Image** (any sub-type, legacy sheets included): at its own shape, full available width, height capped so it fits the screen → pinch / double-tap / `Z` to zoom to full detail (3600 w copy; original on download) → next/previous image in its group (swipe, ← →) → phone landscape = edge to edge.
- **Doc / record:** HTML, one column; heading jump list for long docs; **wide tables and code blocks scroll sideways inside their own box** (`budget-variant.md` has wide tables); images inside a doc show at column width and open in the image viewer. Links to other items become item links; links to non-items show as plain text.
- **Test:** result in words (PASS / FAIL / RAN, FAIL first in its group), numbers from `metrics.json` as one line, sound (play/pause, static waveform, playhead, time), A/B between the variants that exist (golden · perturbed · worst · guarded), switching keeps the playhead, one sound at a time across the page; plots follow as images.
- **Lineage row** under every image and doc: the same item small (docs: rev letter + one line), oldest left, each labelled with rev and where it lives (archive, v1, v1.1, current). Missing old forms are **one labelled gap** "r1–r4 not kept". Tap a form → the viewer swaps to it.
- **Compare:** desktop side by side (synced zoom and pan); phone wipe. **"Show changes"** (from D): a toggle, off by default, that draws ink scallops around the areas that changed between the two forms. `build.py` computes them at publish for consecutive revs of the same image **at the same pixel size**: per-tile difference above a threshold, merged into boxes, capped at 12 boxes ("too many changes to mark" above that, toggle disabled with that line). Not offered when sizes differ or a form is missing. **Docs** compare as text: changed paragraphs marked in the margin with a 2 px ink bar; removed text listed under "removed" at the end (no red/green).
- **Share:** "copy link" on the label → `#/i/FOLD-A@C`. Without `@rev`, the current rev.
- **Dropped item:** opens at full strength; label "dropped · <date> · <reason if the event gave one>".

## 7. Decisions (J4; D's register, in both concepts)
One list, newest first: **date · his words verbatim (body size) · what it caused** (codes as links, "before" for evidence that led to it, "after" for work it caused). The question asked appears above his words in ink 2 when the record has it. Undated entries say "time not recorded". URL `#/d` and `#/d/<n>`. Both concepts reach it in one tap from the landing (each says where).

## 8. Links (J8)
`#/` landing · `#/g/<group>[@rev]` concept group · `#/i/<code>[@rev]` item · `#/v/<version>` version · `#/h/<day|round|version>/<key>` history (Cabinet's scrubbed view uses `#/h/round/2`) · `#/d[/<n>]` decisions · `#/s/<stage>` stage · `#/k/<kind>` kind. Unknown code or rev → the landing with "FOLD-Z isn't in the register" (never a blank page).

## 9. "Since you last looked" (J12) — waiting on the owner
- If kept: `lastSeen` = the last visit that stayed open ≥ 5 s. Items or groups with a rev or event after it carry the dot; opening one clears it; leaving moves `lastSeen` to now. First visit or signed out: no marks, no count.
- If not: no dots; "+ n more since you last looked" becomes "+ n more today", same place.

## 10. States both concepts must draw or answer
| State | Rule |
|---|---|
| Empty stage (Boards today) | Shown, labelled "not yet"; opening it says what will go there ("PCB layouts, board photos, test results"). |
| Stage begun early (Spec today) | Shown as "early" with its items; not "now". |
| Empty kind in a stage | Shown empty in the concept's form; not tappable. |
| Labelled gap | Lineage and history show what wasn't kept as one labelled gap. |
| Queued group or item | §5. |
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
Start → `status/now`. Concept work → `img/` + markdown → commit → `build.py` → publish → one "group revised" event. Other items → commit → build → publish → event. Score / decision (with `caused`) / drop → event. Lock → build → publish → event. Test → plots + waveforms → publish → event. End → `status/now` off. All via `site/publish.sh`.
