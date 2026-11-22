# floss: systems designer notes

## Where things stand (2026-11-22, jam closed; jobs.md rev 1 written)
- **The jam closed after six turns.** Turn 5 (director) killed WIND, put TIDE forward on a condition (velocity and pressure must matter in TIDE), and named the SWELL word clash. Turn 6 (visual) gave the faces:
  - BOW = CATHEDRAL with the lid as soundbox, dark naturals, coral pressure selector;
  - KEPT = ONE SHEET, white and black keys, coral ensemble;
  - TIDE = HUSH, a felt pebble with maple pegs, coral DRIFT on the axis, the lantern.
  - Off-centre split: a one-key gutter over middle C carrying the shared controls, plus a coral rim tick at B|C (director to rule).
  - Words: attack / release knobs; pressure swell · vibrato · tone · shimmer; strands low · main · high; octave numbers −1 · 0 · +1 · +2; KEPT tabs bass · strings · brass.
- **`../jobs.md` rev 1** opens with a short owner-facing list of 21 jobs, then a detail table (J1–J21 with concept requirements) and flows F1–F15. It goes to the owner as "anything wrong or missing?".
- **Next: concepts**, with me going first: how each of BOW, KEPT and TIDE works (structure, flows, states).
- Things to settle in the concepts:
  - what "all tabs off" does;
  - how echo sync is turned off;
  - a tuning trim (J17);
  - where "knob not in control" shows;
  - whether BOW's three-deep strand column fits CATHEDRAL's base depth (visual's question to me).
- Read: `BRIEF-CONTEXT.md`, `floss/README.md`, `design/owner.md` from 2026-11-21 on, `design/concepts/common-how-it-works.md`, and skims of `design/jobs.md` and `eng/budget-variant.md` (keys, velocity, aftertouch).

## Randomness drawn
- Turn 1 (mine): "Work at a different speed", "Do the washing up"; bell ringing; "designed for two players".
- Visual turn 2: "Use an old idea", "Go slowly all the way round the outside"; lighthouse, kite; child's hands; coral.
- Director turn 3: "Give way to your worst impulse"; pipe organ; eyes closed.

## Facts checked
- Ensemble: three modulated delay paths, two LFOs (≈ 1 Hz, ≈ 6 Hz), phases 0 / 120 / 240° (Sound on Sound, "More creative synthesis with delays"). Closes the director's check; the lantern can follow three phases.
- Director checked (Zoë Blade's Solina guide): the Solina's contrabass and cello sounded only on the low region (C2–G3); its crescendo and sustain sliders set attack and release.

## Decisions so far and why
- **Engine: structure B** (one tone per key from an MCU, a VCA and firmware envelope per key, then the shared filter, ensemble and FX). Agreed by the whole team. It's the only structure that gives per-note velocity and pressure with every key sounding.
- **Per-note articulation, no new controls:** strike → attack time (inside SWELL's range); lean → the pressure destination; lift speed → tail (inside RELEASE's range). Lift timing is firmware only; the fast end is limited by the Choc V2's spring return (eng to test).
- **The split = two OCTAVE knobs**, no mode. Pointers parallel = continuous (visual's reading, endorsed by the director). Fixed split B|C. A held note keeps its pitch across an octave change.
- **Per-half controls sit over their half** (visual; the director made it a rule).
- **MIDI split ON/OFF on the rear wall.**
- **Signal order on the panel:** TOUCH (SWELL, RELEASE, PRESSURE selector) → strands / registers → TONE → SHIMMER → ECHO → REVERB → VOLUME.
- **PRESSURE positions:** SWELL, VIBRATO (per note), TONE, SHIMMER (global, following the max pressure). On a shared-strip fallback, SWELL behaves as FILL (whole-instrument swell), with the same label.
- **Breath (from WIND), fixed in every concept:** the sum grows roughly with √(keys down), recovering over ≈ 200 ms; no pitch sag; no control. This answers J15.
- **HOLD** (was SET): a latching toggle; a new chord after all keys are up replaces the old one; off releases with tails. No armed state. Scope per concept: BOW left half, TIDE everything, KEPT left half.
- **Registers differ per concept:**
  - BOW: strands of pitch (−8va, unison, +8va, sine-rounded); 6 tabs (3 per half), names printed once between the rows.
  - KEPT: the Solina way (shared timbre tabs plus a low register on the left half only).
  - TIDE: none, just TONE.
- **The honest "analog voices" sentence** is in jam turn 4 §8.

## My kills and proposals in pass 2
- **Killed WIND as a concept:** same hardware as BOW, so it would only be a firmware switch. It survives as the fixed breath and as FILL.
- **Killed the swell-box lid.**
- **Proposed TIDE** for the third slot ("life lives in time": per-key drift on a DRIFT knob, HOLD for everything, long lift-set tails). Its risk: it overlaps with the Daisy reverb and shimmer modes, so it has to stay analog-first.
- **Dropped the fifth strand.**
- **24 keys:** shown as an owner-visible option that centres the split (7 + 7 whites), not recommended. The 25-key split sits 9 mm left of centre.

## Director's objections and how I answered them
- "One concept, four names": answered by giving the registers, HOLD scope and engine emphasis a different answer per concept, and by proposing TIDE.
- Analog honesty: answered with the sentence.
- Jargon: SET → HOLD; BRIGHT → TONE. Strand labels are still to be named in plain words (visual).
- Off-centre: offered the 24-key option; my preference is that the axis follows the split (visual's call).
- BOW/WIND as one instrument: argued yes, and killed WIND.

## Open questions
1. Eng: 25 per-key VCAs (cost, battery, board); 75 tone outputs for strands; lift timing at the spring's return; the BBD part; per-key pressure past the bottom (FSR per key? a felt collar?), keeping the shared-strip fallback.
2. Director: TIDE or keep WIND in the third slot?
3. Owner later: is the fixed breath OK? Velocity as speed only? Fixed centre split OK? 24 vs 25 keys?
4. TUNE trim on the rear, or none?
5. Status light: the director cut it to three meanings. Where does "knob not in control" go, if anywhere? (Big Energy's J8 needed it.)

## Next
- Fold the owner's answer on the jobs list into `jobs.md` rev 2.
- Concepts: write how-it-works for BOW, KEPT and TIDE in `../concepts/<name>/`, starting with the shared rules (the split, the half-map, the TOUCH group, the breath, lift, the status light), then check each against `jobs.md`.
