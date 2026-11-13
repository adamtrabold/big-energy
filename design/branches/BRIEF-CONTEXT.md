# Branches: shared brief context (orchestrator, 2026-11-13)

Every teammate on the branches work gets this file. Everything is under the repo root `/home/claude/big-energy/`.

## The owner's words for this task (verbatim)
> "i think i want to move forward with one sheet and the fold (can't decide yet, but the internals are probably the same eh?). but first i'd like to take these versions and do some creative rounds (again, using the randomness principles) to explore how to add some more personality. i *love* the peg keys on the hush, for example, and those on the fold may add an "organ like" feel or something idk. im not saying that is an official direction to explore, but im saying we need to push for more of an even more holistic *point of view* / concept in some branched versions (i may still come back to these). follow principles of design of furniture (theres even a great book on this called principles of design), instruments, tools, but also artistic inspirational forms and emotion. i want to take this to the park and be inspired. also i want to make sure the delay can be timed to the midi if there is midi tempo control"

Follow-up (verbatim): "am i missing a control to turn that tempo sync on / off?"
(Orchestrator's answer to him: no such control exists in the spec. The echo already reads MIDI clock from USB and TRS, but its behaviour under clock hasn't been designed. The systems designer designs it; if it needs a new control, that goes to the owner as a decision.)

## Owner direction and records (read these)
- `design/owner.md`: the authoritative owner record, newest entries at the bottom. Read all of it. The entry dated 2026-11-13 11:47 is this task.
- `archive/full-instrument/owner.md`: shared history. Line 28 is the origin of the "randomness principles": "it'd be cool to see some expected / highly designed for use cases, and others using more of the randomness/creative principles to drive unique outcomes that have more sauce / vibe".
- `HANDOFF.md`: the locked spec in one breath, plus the rules the owner set.
- Starting points are the v1.1 locked concepts in `versions/v1.1/{hush,one-sheet,fold}/`: `how-it-works.md`, `how-it-looks-and-feels.md` and mock sheets A–D (FOLD also has E). Shared: `versions/v1.1/common-how-it-works.md` and `common-looks-and-feels.md`.
- Earlier jam, for the randomness method: `design/jam.md` (§5 "Draws" and later "My draws": `secrets.SystemRandom` over Oblique Strategies, unrelated fields and twists). Draw script: `design/concepts/jam-visual-draw.py`. Make fresh draws; don't reuse old ones.
- Engineering: `eng/budget-variant.md` (rev 14, master spec), `eng/daisy-first-principles.md` (§5 MIDI/USB, §6 effects), `eng/single-chip-research.md` (FX types and controls).
- Scores history: `design/scores.md`. Naming candidates: `design/naming.md`.
- Render code for sheets and 3D views: `design/concepts/_mock-src/` (`r5.py` 3D views, `sheets_r5.py` sheets, checkers `fold_r5_check.py`, `layout_r4_check.py`, `flat_r5_check.py`). Sheets are A3 at 4961×3508. The owner judges looks from pictures, so concepts need believable pictures.

## What's settled vs. open
**Settled (binding unless the owner changes it):**
- The locked spec in `HANDOFF.md` and `eng/budget-variant.md`: voice, 25 velocity keys on Kailh Choc V2 silent switches with pressed-on tops and Hall sensing, aftertouch strip, bend joystick (one axis, springs to centre), mod knob that stays put, switches, DRIFT, Daisy Seed echo and reverb with all 8 controls on the panel, MIDI over USB plus TRS in and out, internal LiPo, single rear USB-C.
- The owner's rules: nothing raised among the knobs or between the keys and the controls; no screens or encoders; keys and knobs are real bought parts, never printed, and no custom key mechanism the owner has to build; 3D-printed enclosures welcome; unibody, screws from the back (ideal, flexible); keys run to the front edge (edge A); cost is his main concern; portable; internal battery.
- The v1.1 locks are never edited. Branches are new concepts in `design/branches/concepts/`.

**Open (the team's to explore):**
- Each branch's point of view: the one idea that generates form, material, graphics, making and feel, drawing on furniture design principles, instruments, tools, artistic forms and emotion.
- Personality. Peg keys (the owner loves HUSH's) and an "organ like" feel are the owner's examples, explicitly not a direction.
- What "take this to the park and be inspired" asks of the object.
- How the echo behaves under MIDI clock, and whether that needs a control (systems designer).
- Which v1.1 concept(s) a branch grows from. The owner leans ONE SHEET or FOLD, but said "take these versions".
- The book: the owner mentioned "a great book on this called principles of design". Which book isn't confirmed. Don't attribute specific content to a book you can't confirm; use furniture design principles you can stand behind.

## Work files
- Jam: `design/branches/jam.md` (append your turn at the bottom).
- Concepts: `design/branches/concepts/<name>/`.
- Jobs: `design/jobs.md` (the systems designer updates it for this work).
- Scores (the orchestrator writes): `design/scores.md`.
- Your notes: `design/notes/{systems,visual,director}.md`. Add a new dated section at the top for the branches work; keep the history.
- Commit nothing; the orchestrator commits.
