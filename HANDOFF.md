# Orchestrator handoff — CURRENT STATUS (2026-11-21). Read this section first.

**The project pivoted on 2026-11-21.** The Model D voice is no longer the instrument. Everything below the line "Earlier handoff" describes the Model D / Big Energy work as of 2026-11-13; treat it as history and as a platform to reuse, not as the plan. The owner's exact words are at the bottom of `design/owner.md` (entries dated 2026-11-21).

## What Adam wants now
- Two new instruments, both more inspiring to him than the Model D: a **string machine** and a **portable analog poly** named **Port-a-poly** (working name). A Model D build may come back later.
- What draws him: **"Analog voices, shimmer and warmth"**. He likes blending several oscillators per voice, the Juno's chorus and warmth, and he built a Dreadbox Antiphon (8 analog sine oscillators, spring reverb). Portability matters.
- **Next work: build plans for the string machine, the Big Energy way** (design loop, first principles, spec, verification), while proving out the shared platform. Port-a-poly plans come after. **Which one gets built first is undecided — don't ask him to pick yet.**
- He was skeptical of mixing analog and digital voices inside one chord ("if it hasn't been done before it may be for a reason").

## How to work with him (unchanged)
- Work as his design-buds skill says. You are the orchestrator; no design calls by you.
- Open questions one at a time, short and plain replies, no flattery.
- Append every owner decision verbatim to `design/owner.md`. Commit as Adam Trabold <adamtrabold@users.noreply.github.com>, never credit Claude, and run `bash site/publish.sh` after committing.

## Facts already checked in chat (2026-11-21)
- **How string machines work:** a master clock of several MHz feeds a top-octave divider (12 notes), then flip-flops halve each note for every lower octave, so every key has a tone running and can sound at once. All notes share one filter and, usually, one envelope (paraphonic: a new note doesn't get its own attack). The raw tone is square-based and thin; a multi-stage bucket-brigade (BBD) ensemble with slow LFOs makes the string shimmer. Precedents: Eminent/ARP Solina (1974), Roland RS-202, Elka, Crumar Trilogy (combo synth + strings). Behringer sells a Solina clone today (~$259). Per-note articulation exists (Polymoog had a VCF/VCA/EG board per note) but is costly. Classic top-octave chips are vintage parts; modern DIY builds often generate the tones on a microcontroller.
- **Paraphony references:** Korg Volca Keys is paraphonic (3 VCOs, 1 VCF, 1 VCA, 1 EG), not a true poly.
- **Behringer Pro-800:** 8 voices, 2 CoolAudio 3340 VCOs + V3320 filter per voice; envelopes and LFO computed in firmware (checked in GliGli's open p600fw); cheap because of in-house chips, software control and factory scale.
- **Poly research already in the repo:** `explore/poly-hybrid.md` (4-voice Juno-style "Little J" ≈ $350–520 and Prophet-600-ish ≈ $380–560, one unit, estimates).

## Ideas discussed, none decided
- Poly: Juno-style DCO voices; SEM-style state-variable filter per voice; Daisy for envelopes, LFOs and voice allocation; Daisy ensemble/chorus plus reverb and echo; 4–6 voices; a mode with digital oscillators into the analog filters (Novation Peak/Summit-style).
- String machine: as its own instrument, or as a minimal "strings" layer inside Port-a-poly (one level knob). Ideas for something new: per-key swells, pressure-controlled bowing, drift between notes, sine stacking like the Antiphon.

## Open, the owner's
- What carries over from the Big Energy platform: 25 Hall-sensor velocity keys, FSR aftertouch, battery and USB-C, built-in speaker, the Daisy with echo and reverb, MIDI rules, no screens or encoders, real bought knobs and keys, the ONE SHEET / FOLD / CATHEDRAL enclosure work.
- Budget ceiling (the ~$100 Big Energy target doesn't carry over automatically). Name for the string machine.

## Prompt for Adam to paste into a new session
> Attach and clone my repo adamtrabold/big-energy. Read HANDOFF.md (the current-status section first), then the 2026-11-21 entries at the bottom of design/owner.md. You're the new orchestrator, working as my design-buds skill describes. We're making build plans for a string machine. Tell me in 3 lines where things stand and what you need from me, then wait.

---

# Earlier handoff (2026-11-13) — history

# Model D project ("big energy") — orchestrator handoff (2026-11-13)

Repo: https://github.com/adamtrabold/big-energy · Viewing page (artifact): https://claude.ai/artifact/69aSiNmeYuxmDuSoBdhpFD

Read this whole file before doing anything. You are the new **orchestrator** for Adam's synth project. You work the way his **design-buds** skill says: you run the work, brief teammates (systems designer, visual designer, design director, plus builder, reviewer and critic when needed), and talk to Adam. You make no design calls. Only work the director scores 9 or higher goes to Adam. He wants to see work early, gets asked open questions one at a time, and wants short, plain replies.

## Where the files are
- **Working home: this repo** (`adamtrabold/big-energy`, branch `main`, plain files). Clone it, then work and commit here. The artifact "Model D — locked v1.1 + handoff" (https://claude.ai/artifact/69aSiNmeYuxmDuSoBdhpFD) is only for viewing and sharing the sheets.
- **`versions/`**: locked official sets, one folder per version (`v1`, `v1.1`, …). [`VERSIONS.md`](VERSIONS.md) says what each one is. Never edit a locked version. To lock a new one, copy the current concept files into `versions/vN/`, add a line to `VERSIONS.md`, and commit with the message "Lock vN: …". Git tags couldn't be pushed from these sessions (the proxy returned 403), so Adam adds the tags in GitHub.
- **`design/`**: the instrument being built. The owner record is `design/owner.md` (authoritative and verbatim, newest entries at the bottom; append every owner decision verbatim). Team notes are in `design/notes/{systems,visual,director}.md`, along with `scores.md`, `naming.md`, `jobs.md` and `jam.md`. Concepts are in `design/concepts/{hush,one-sheet,fold}/`, plus `common-how-it-works.md` and `common-looks-and-feels.md`.
- **Render code:** `design/concepts/_mock-src/`. The main scripts are `r5.py` (3D views, written to `out/`) and `sheets_r5.py` (sheets, written into the concept folders); the checkers are `fold_r5_check.py`, `layout_r4_check.py` and `flat_r5_check.py`. Sheets are A3 at 4961×3508.
- **`eng/`**: `budget-variant.md` (rev 14) is the master spec. Research notes: `daisy-first-principles.md`, `aftertouch.md`, `effects.md`, `battery.md`, `fold-answers.md`, `daisy-pin-and-audio-check.md`, `single-chip-research.md`, `cost-estimate.md`. Simulations are in `eng/sim/`.
- **`explore/`**: side research on easier, cheaper and cooler clone ideas.
- **`archive/`**: `full-instrument/` (the paused big Model D clone, with its own owner record and brief), `paused-concepts/` (TYPE CASE, HYMNAL, UNDER GLASS) and `fold-superseded/` (FOLD-113 and older FOLD sheets). Leave all of it alone unless Adam brings it up.
- **Not in the repo** (bulky, can be regenerated): ngspice raw `.dat`, `_mock-src/out/`, and `ref/ca-72` (`ref/README.md` says how to clone it).

## The project site (GitHub Pages)
- Live at https://adamtrabold.github.io/big-energy/ (served from the `gh-pages` branch; owner: "gh pages is fine").
- After any session commits work to main, run `bash site/publish.sh` to rebuild the site from the repo and push it to `gh-pages`. Docs (`docs/`), reviews (`design/reviews/`), decisions (`design/owner.md`), versions and concept images all come from main.
- Owner rule: reviews, logs and documents go on the site (in the repo), not as files sent in chat.
- Owner rule: never credit Claude on GitHub. Commit as Adam Trabold <adamtrabold@users.noreply.github.com>, with no `Co-Authored-By: Claude` line; `site/publish.sh` already does this.

## Status
- **Locked:** HUSH (290 × 187 mm), ONE SHEET (276 × 180 mm) and FOLD-105 (halves 286 × 108 mm, closes at about 50 mm, stands at 120°). All three scored 9 in round 5 and held 9 at the v1.1 check. The current lock is `versions/v1.1/`. Key edge A ("keys at the edge").
- **Adam's lean:** he wants to move forward with **ONE SHEET or FOLD** and hasn't decided which. He noted the internals are probably the same. Mostly true: the electronics and spec are shared (see `design/concepts/common-how-it-works.md`), but the board split differs. FOLD carries a hinge cable between its halves; ONE SHEET is a single deck.
- **v1.1 (current lock):** FOLD stands at **120°** (Adam: "less steep so the front face catches more light"): stays are 44.4 mm, it tips at about 6.8 N, and it can't fall backward. **Bend** is a one-axis, spring-to-centre mini thumbstick, now drawn unmistakably as a joystick in every view: a round opening, a stem and a cap, plus a callout on each B sheet. Mod is a separate knob that stays put. FOLD sheet D now shows MIDI IN. The director checked these changes and all three concepts still score 9.
- **Adam withdrew a request** ("forget i said that"): creative rounds on personality for branched versions. Don't start that unless he brings it up again.

## Next decisions that are Adam's
1. Build ONE SHEET or FOLD.
2. ~~The name~~ — decided 2026-11-13: **Big Energy**.

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
> Attach and clone my repo adamtrabold/big-energy. Read HANDOFF.md fully, then design/owner.md and design/notes/director.md. You're the new orchestrator, working as my design-buds skill describes. Tell me in 3 lines where things stand and what you need from me, then wait.
