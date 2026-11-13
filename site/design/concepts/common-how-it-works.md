# How it works: shared by every concept (C Cabinet, D The Set, E Herbarium)

Product designer (systems focus), concept turn 1, 2026-11-13. Each concept's own `how-it-works.md` covers its landing, its way in and its history. Everything here is the same in all three, so the director can score the concepts on how they differ, not on this.

Source of truth for jobs: `site/design/jobs.md`. Settled rules and model are there; not repeated here.

## 1. Data the page runs on
- **Snapshot** (baked into every publish, works for anyone): `manifest.json` = project (name, one line, current stage, current version, waiting on Adam), stages, versions, rounds, items (code, title, kind, stage, status, revs with date + one line + file paths + which version holds each rev, lineage, caused-by), events up to publish time. Plus web images per rev: 1600 w and 3200 w WebP, waveform SVGs for WAVs, the original on download.
- **Live** (`db`, signed-in only): `status/now` (working, what, since, heartbeat), `events/*` (rows written after the last publish), `data/users/<id>/lastSeen` (per person, for J12).
- On load the page renders from the snapshot at once. When `db` resolves it merges newer events and lights the lamp. Nothing waits on `db`.

## 2. Lamp (J3, J11) — same logic, each concept places it
| State | When | Shows |
|---|---|---|
| ON | `status/now.working` and heartbeat < 20 min | "On · <what> · since 14:02" |
| STANDBY | not working, or heartbeat ≥ 20 min | "Standby · last <event> · 14:02" (+ "waiting on you: …" where the concept puts it) |
| SNAPSHOT | `db` is null (signed out, or no answer in 10 s) | no lamp; "Snapshot · 13 Nov 14:02" (publish time) |
| Connecting | first ≤ 10 s while `db` resolves | the snapshot line in ink 2, no lamp yet. Never shows STANDBY before it knows. |
| Live lost | `db` was live, then subscription errors | lamp off, "Live paused · last 14:02". Falls back to what it had; never pretends ON. |

Heartbeat: a session writes `status/now` at start, with every event, and at least every 10 min while working. A session that dies goes STANDBY after 20 min with "last seen 14:02".

## 3. Events while the page is open (J3)
- New event row → the concept's "new" mark appears on the item and the count updates; the lamp dips once.
- Event names an item **already in the snapshot** (e.g. a score) → shown in full.
- Event names an item **not yet published** (images still to come) → shown as **queued**: code, title and the event's line, no image, "arriving with the next publish". When the publish lands, the queued item fills in. Mechanism: the platform moves open pages to a new version "at their next quiet moment" (publish tool docs), so the page should keep its place across that move: it saves route + scroll + open item in `artifact` state and restores them, so the update reads as the item filling in, not a reload. Builder to verify how the move behaves; fallback is fetching `manifest.json` from the new version when an event says `published: true`.
- Many events at once (a sheet set of 5): grouped into one line "5 sheets · FOLD rev H" rather than five dips.

## 4. "Since you last looked" (J12) — conditional on the owner's answer
- If kept: `lastSeen` = time of the last visit that stayed open ≥ 5 s. Items with a rev or event after it are marked unseen. Opening the item clears its mark. Leaving the page moves `lastSeen` to now.
- First visit, or signed out: no marks, no count. (Not "everything is new".)
- If he says it isn't needed: the marks go; the landing's "what's new" becomes "newest" (last 24 h), same place.

## 5. Opening an item (F3; J7, J14, J8)
Same viewer in every concept; the concepts differ in how you get here.
- **Label** on every item, same fields, same order: code · title · kind · stage · rev · date · status. Plus "caused by: <decision, verbatim, date>" when there is one.
- **Sheet:** fit-width → **read mode** steps numbered crops (where a regions sidecar exists; FOLD-A is assumed to have one; otherwise read mode is hidden, not greyed) → pinch to 3200 px anytime → swipe/‹ › to the next sheet in the same concept and rev set (A → B → C…) → landscape = edge to edge → "download original" (the PNG).
- **Diagram:** the image, pinch, download. SVGs stay vector.
- **Doc / record:** rendered markdown, one column, measure ≈ 66 characters. Long docs get their `##` headings as a jump list at the top. Links to other repo files that are items become links to those items; links to non-items (render code) show as plain text.
- **Test:** result in words (PASS / FAIL / RAN, with what was measured from `metrics.json`), then plots as small sheets, then sounds: play/stop, static waveform, playhead, time. **A/B** between variants (golden · perturbed · worst · guarded, whichever exist for that test) swaps the file and keeps the playhead. One sound plays at a time across the whole page; opening another item stops it.
- **Lineage row** (F6, J10) under every item: the same item small, in order, oldest left; each form labelled with its rev and where it lives (v1, v1.1, current, archive). Missing old forms are **one labelled gap**: "r1–r4 not kept", not a blank tile per round. Tap a form → the viewer swaps to it, label updates. **Compare:** desktop = two forms side by side, synced zoom/pan; phone = a wipe (drag a vertical hairline). Compare is offered only between forms of the same size; otherwise side by side, no wipe.
- **Share:** "copy link" on the label. Copies `…#/i/FOLD-A@F` (code + rev). Without `@rev` the link opens the current rev.
- **Dropped item:** opens normally; the label says "dropped · <date> · <reason from the event, if any>". Its image is at full strength once opened (greying is for lists, so it can still be read).

## 6. Links (J8)
Hash routes, the same in all concepts, so one link format survives whichever concept wins:
`#/` landing · `#/i/<code>[@rev]` item · `#/v/<version>` version · `#/h/<grain>/<date|round>` history at a day/round/version · `#/s/<stage>` stage · `#/k/<kind>` kind. Unknown code or rev → the landing with one line: "FOLD-Z isn't in the register" (never a blank page).

## 7. States every concept must draw or answer in its doc
| State | Rule |
|---|---|
| Empty stage (Boards today) | Shown, labelled, says "not yet". Opening it says what will go there in one line ("PCB layouts, board photos, test results"). |
| Empty kind in a stage | Shown as empty in whatever form the concept uses; not tappable. |
| Labelled gap | Lineage and history show what wasn't kept as one labelled gap. |
| Queued item | §3. |
| Dropped / archived | Greyed in lists with the word "dropped"; never hidden; sorted after current items within a group. |
| Test FAIL | "FAIL" in words, 700 weight; first in its group so it isn't missed. No colour. |
| Audio won't load | Row shows "sound didn't load · download WAV" link. Waveform still shows (it's an SVG). |
| Image won't load | Label stays, image area says "image didn't load · download original". |
| No project name | "( name to come )". |
| Nothing waiting on Adam | The line reads "nothing waiting on you", not removed (so its absence isn't read as a bug). |
| Very long title / code | Titles wrap to 2 lines then ellipsis in lists; full in the label. |
| Reduced motion | All motion instant. |
| Sizes | Phone 390 portrait (primary), phone landscape (sheet viewer goes edge to edge), tablet and desktop (each concept says its layout). |

## 8. What a session does (summary; detail in jobs.md "Update path")
Start → `status/now`. Item made/revised → commit → `build.py` → publish changed files → event with codes. Score / decision (with `caused`) / drop → event. Lock → build → publish → event. Test → build plots + waveforms → publish → event with result. End → `status/now` off with last event and waiting-on. All via `site/publish.sh`.
