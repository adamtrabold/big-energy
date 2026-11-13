# Model D project ("big energy") — orchestrator handoff (2026-11-13)

Repo: https://github.com/adamtrabold/big-energy · Viewing page (artifact): https://claude.ai/artifact/69aSiNmeYuxmDuSoBdhpFD

Read this whole file before doing anything. You are the new **orchestrator** for Adam's synth project. You work the way his **design-buds** skill says: you run the work, brief teammates (systems designer, visual designer, design director, plus builder, reviewer and critic when needed), and talk to Adam. You make no design calls. Only work the director scores 9 or higher goes to Adam. He wants to see work early, gets asked open questions one at a time, and wants short, plain replies.

## Where the files are
- **Working home: the GitHub repo `adamtrabold/big-energy`** (plain files, `main`). Attach it and clone it, then work and commit there. Pushing tags from these sessions was refused (403); the `locked/` folders are the record.
- The artifact "Model D — locked v1.1 + handoff" (https://claude.ai/artifact/69aSiNmeYuxmDuSoBdhpFD) is for viewing and sharing the sheets. It's not the working copy.
- Left out of the repo (bulky, can be regenerated): ngspice raw `.dat`, `_mock-src/out/`, `_mock-src-*-backup/`, and `ref/ca-72` (clone instructions are in `ref/README.md`).
- **Locked official versions:** `design/little-d/locked/v1.1-2026-11-13/` (current; supersedes `v1-2026-11-13/`). Don't edit these. New work goes in `design/little-d/concepts/` or a new branch folder.
- **Owner record (authoritative, verbatim):** `design/little-d/owner.md`. Newest entries are at the bottom. Append every owner decision verbatim, and mirror the file to `model-d/owner-requirements-budget.md`.
- **Team notes** (start every teammate from these): `design/little-d/notes/{systems,visual,director}.md`, `scores.md`, `naming.md`, `jobs.md`, `jam.md`.
- **Engineering:** `model-d/eng/`. `budget-variant.md` (rev 14) is the master spec for the budget instrument. Other files: `daisy-first-principles.md`, `aftertouch.md`, `effects.md`, `battery.md`, `fold-answers.md`, `daisy-pin-and-audio-check.md`, `single-chip-research.md`, `cost-estimate.md`, `architecture.md`.
- **Render code:** `design/little-d/concepts/_mock-src/`. The main scripts are `r5.py` and `sheets_r5.py`; the checkers are `fold_r5_check.py`, `layout_r4_check.py` and `flat_r5_check.py`. Sheets are A3 at 4961×3508. Back up the folder before editing.
- **Full instrument (paused):** `design/instrument/`. Leave it alone unless Adam brings it up.

## Status
- **Locked:** HUSH (290 × 187 mm), ONE SHEET (276 × 180 mm) and FOLD-105 (halves 286 × 108 mm, closes at about 50 mm, stands at 120°). All three scored 9 in round 5 and held 9 at the v1.1 check. Key edge A ("keys at the edge").
- **Adam's lean:** he wants to move forward with **ONE SHEET or FOLD** and hasn't decided which. He noted the internals are probably the same. Mostly true: the electronics and spec are shared (see `common-how-it-works.md`), but the board split differs. FOLD carries a hinge cable between its halves; ONE SHEET is a single deck.
- **v1.1 (current lock):** FOLD stands at **120°** (Adam: "less steep so the front face catches more light"): stays are 44.4 mm, it tips at about 6.8 N, and it can't fall backward. **Bend** is a one-axis, spring-to-centre mini thumbstick, now drawn unmistakably as a joystick in every view: a round opening, a stem and a cap, plus a callout on each B sheet. Mod is a separate knob that stays put. FOLD sheet D now shows MIDI IN. The director checked these changes and all three concepts still score 9.
- **Adam withdrew a request** ("forget i said that"): creative rounds on personality for branched versions. Don't start that unless he brings it up again.

## Next decisions that are Adam's
1. Build ONE SHEET or FOLD.
2. The name (still open; `naming.md` top picks are HOLLER, WREN and WALLOP).

## Then
- `handoff.md` for the chosen concept. The director checks it against `owner.md`.
- Build spec and BOM. Adam places all orders; you can't pay.
- Pre-build checks still open:
  - breadboard spike: the Daisy's counters, mux scan, reverb plus echo CPU load, codec noise, FSR cutting and uniformity, Hall sensor wake time;
  - ONE SHEET texture coupon (smooth plus rings);
  - Daisy seated height in FOLD (11.1 mm of space);
  - FOLD hinge cable list, redone now that all digital parts sit in the base;
  - HUSH felt-steaming test, only if HUSH comes back.

## Locked spec in one breath
- **Voice:** 3 VCOs with all waveforms; modern equivalents of the original chips (AS3046 expo, ladder filter); analog envelopes (PWM-chopped resistor); AS3360 VCAs; autotune via the Daisy's TIM5 input capture.
- **Keys:** 25, velocity, Kailh Choc V2 silent switches with pressed-on key tops. A magnet in each top over an SS49E Hall sensor; velocity is timed between two thresholds.
- **Aftertouch:** FSR strip under the key strip, with a MOD / OFF / FILT switch.
- **Bend and mod:** bend is the one-axis joystick; mod is a knob that stays put and can be set over MIDI.
- **Switches and knobs:** velocity LOUD / BOTH / FILT; MONO / PARA / PARA+4 (paraphonic allocation is in the eng notes); DRIFT knob.
- **Effects:** digital echo (TAPE / BBD / CLEAN / PING-PONG) and reverb (PLATE / HALL / SPRING / SHIMMER) on a Daisy Seed, all 8 controls on the panel, wet-only return.
- **MIDI:** USB plus TRS in and out. Jump-on-move. Knob-only controls send no MIDI, and MIDI never flips switches.
- **Power and build:** internal LiPo battery, single rear USB-C. Unibody enclosure, 3D-printed first, screws from the back. Knobs and keys must be real bought parts, never printed, and no custom key mechanisms. Quantity-1 PCB makers.
- **Rules Adam set:** nothing raised among the knobs or between the keys and the controls; no screens or encoders. Don't say "port" for things that haven't been built.

## Prompt for Adam to paste into a new session
> Attach and clone my repo adamtrabold/big-energy. Read HANDOFF.md fully, then design/little-d/owner.md and design/little-d/notes/director.md. You're the new orchestrator, working as my design-buds skill describes. Tell me in 3 lines where things stand and what you need from me, then wait.
