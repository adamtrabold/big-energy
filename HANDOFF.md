# Model D project — orchestrator handoff (2026-11-13)

Artifact with everything: https://claude.ai/artifact/69aSiNmeYuxmDuSoBdhpFD (slug `29b040ee-feb1-403d-ac28-c1b02ee78b94`)

Read this whole file before doing anything. You are the new **orchestrator** for Adam's synth project. You work the way his **design-buds** skill says: you run the work, brief teammates (systems designer, visual designer, design director, plus builder, reviewer and critic when needed), and talk to Adam. You make no design calls. Only work the director scores 9 or higher goes to Adam. He wants to see work early, gets asked open questions one at a time, and wants short, plain replies.

## Where the files are
- Previous sessions' files do not carry over. **Easiest:** Adam's artifact "Model D — locked v1 + handoff" holds this file, the locked sheets, all the .md notes and specs, and the render code. Use `list_files` and `read_file` (with `paths`, to save them as files) to rebuild the folder; each file's path in the artifact is its path under `model-d/`, except that the render code is stored as `.py.txt`, so drop the `.txt`. The ngspice netlists aren't in the artifact; they're in the zip. **Or** Adam brings three zips. Unzip them in the working directory:
  - `model-d-handoff.zip` gives you `model-d/`. It has all the text, code and netlists, but no images.
  - `locked-v1-fold-onesheet.zip` and `locked-v1-hush.zip` hold the locked sheet images. Unzip them into `model-d/design/little-d/locked/`.
- **Locked official versions:** `model-d/design/little-d/locked/v1-2026-11-13/`. Don't edit these. New work goes in `design/little-d/concepts/` or a new branch folder.
- **Owner record (authoritative, verbatim):** `design/little-d/owner.md`. Newest entries are at the bottom. Append every owner decision verbatim, and mirror the file to `model-d/owner-requirements-budget.md`.
- **Team notes** (start every teammate from these): `design/little-d/notes/{systems,visual,director}.md`, `scores.md`, `naming.md`, `jobs.md`, `jam.md`.
- **Engineering:** `model-d/eng/`. `budget-variant.md` (rev 14) is the master spec for the budget instrument. Other files: `daisy-first-principles.md`, `aftertouch.md`, `effects.md`, `battery.md`, `fold-answers.md`, `daisy-pin-and-audio-check.md`, `single-chip-research.md`, `cost-estimate.md`, `architecture.md`.
- **Render code:** `design/little-d/concepts/_mock-src/`. The main scripts are `r5.py` and `sheets_r5.py`; the checkers are `fold_r5_check.py`, `layout_r4_check.py` and `flat_r5_check.py`. Sheets are A3 at 4961×3508. Back up the folder before editing.
- **Not in the zips** (too big, and they can be regenerated): every non-locked PNG/SVG (rerun `_mock-src/render_all.py`), the `ref/ca-72` git history (re-clone CA-72), ngspice raw `.dat` output in `eng/sim/`, render intermediates in `_mock-src/out/`, and old `_mock-src-*-backup` folders.
- **Full instrument (paused):** `design/instrument/`. Leave it alone unless Adam brings it up.

## Status
- **Locked v1:** HUSH (290 × 187 mm), ONE SHEET (276 × 180 mm) and FOLD-105 (halves 286 × 108 mm, closes at about 50 mm). The director scored all three 9 in round 5. Key edge A ("keys at the edge").
- **Adam's lean:** he wants to move forward with **ONE SHEET or FOLD** and hasn't decided which. He noted the internals are probably the same. Mostly true: the electronics and spec are shared (see `common-how-it-works.md`), but the board split differs. FOLD carries a hinge cable between its halves; ONE SHEET is a single deck.
- **In flight at the lock:**
  - FOLD's standing angle changed from 105° to **120°** at Adam's request ("less steep so the front face catches more light"). Systems has updated `fold/how-it-works.md`: stays are 44.4 mm, tipping needs about 6.8 N (the target is 5 N or more), and it can't fall backward. **Sheet E in the lock still shows 105°.**
  - **Bend** is a one-axis, spring-to-centre mini thumbstick gated by a slot. It is not a fader. Mod is a separate knob that stays put. Adam asked whether it was a snap-to-centre fader, because the top-down drawings make it look like a fader cap. A visual designer was redrawing it to read as a joystick and re-rendering FOLD sheet E at 120°. If those files aren't in the zip, redo the task. After that, the director checks it, then it goes to Adam.
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
> Read my artifact "Model D — locked v1 + handoff" (https://claude.ai/artifact/69aSiNmeYuxmDuSoBdhpFD): use list_files and read_file on it, starting with HANDOFF.md, then design/little-d/owner.md and design/little-d/notes/director.md. Rebuild the working folder from its files. You're the new orchestrator, working as my design-buds skill describes. Tell me in 3 lines where things stand and what you need from me, then wait.
