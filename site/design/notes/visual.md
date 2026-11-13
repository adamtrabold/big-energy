# Visual designer notes: project site

## Where things stand (2026-11-13, after jam turn 2)
- Concept phase. Jam turn 1 (systems) gave jobs J1–J14, structure, update path, directions A Lab Book / B Shelf / C Panel.
- My jam turn 2 (in `site/design/jam.md`): shared visual system, look-and-feel for each direction, B dropped, C reshaped into Panel + Cabinet, new D The Set (drawing register). Sketches: `site/design/concepts/jam-sketches/visual-jam2.png` (source `visual-jam2.py`; renders with real FOLD sheet A v1.1 and the golden `voice_bass_pluck.wav`).
- Handed to the design director to steer which directions go to concepts.

## Decisions so far and why
- **Rams as principle, not costume.** No fake knobs, metal, cassette art. Owner is a design director; he'd see through decoration.
- **The frame recedes; the work carries colour.** The sheets have cream ground, red-orange accent, Inter. Site ground is a warm light grey `#E6E4DF` (a step darker than the sheets' cream so a sheet's edge shows with no border/shadow). No red/orange in the frame.
- **Palette** (WCAG checked): ground `#E6E4DF`, cell `#EFEDE9`, rule `#C4C1BA`, ink 2 `#5F5D58` (5.2:1), ink `#1B1B19` (13.6:1), ON `#23863F` (3.6:1, non-text). First picks for ink 2 and green failed contrast; changed.
- **One signal colour, one meaning:** green = ON only (random hue draw 131). Unseen = 6 px ink dot (or Δ in D). Dropped = 40% opacity + the word "dropped".
- **Type:** Inter, self-hosted subset, tabular figures always. Reason: the sheets' own face (`_mock-src` uses Inter). Phone sizes 27 (his words, A only) / 22 / 15 / 12.5 + 10.5 caps label. Weights 400–700.
- **Grid:** 8 px base; phone 16 px margins, 56 px gutter where needed; desktop 12 col, max 1280.
- **Lamp: three states, never a lie.** ON (steady green, one 600 ms dip when an event lands, no pulsing at rest); STANDBY (hollow ring, 1 s fade from ON); SNAPSHOT for signed-out viewers (no lamp, "Snapshot · date time").
- **A3 on phone:** fit-width map → Read mode crops (hero, principles, spec strip) from a renderer-written region sidecar (`*.regions.json`; `sheets_r5.py` places blocks at explicit mm coords so this is feasible) → pinch to full-res. WebP 1600 w / 3200 w / original PNG on download. Desktop: sheet full content width, ← → and Z for 1:1. Compare: side by side on desktop, wipe on phone.
- **Audio:** cell-grey row, 44 px round play, static peak-line waveform pre-drawn by build.py, hairline playhead, A/B golden|perturbed keeps playhead, one sound at a time, no volume slider.
- **Motion list (complete):** row insert 180 ms ease-out + fade; scrubber detent snap (+haptic where supported, not iOS Safari); lamp dip; lamp fade. Reduced motion → instant.
- **Pass/fail in words** (PASS 500 / FAIL 700), no traffic lights.
- **Directions:** keep A (time-first), C Panel+Cabinet (structure-first, 9 stages × 5 kinds, no-scroll, scrubber), D The Set (document-first: title block, revision table, sheet index, Δ = changed since you looked). Drop B; its track list → version page, spine rows → D's revision table, version detents → C's scrubber.
- **Not proposing** a three-tab hybrid; a winner may absorb one part of another later.
- Lean: C strongest Rams fit and best landing; D dark horse (his professional language, revisions native); A best read, most exposed if shared widely.

## Draws (SystemRandom, tag cd6dbb85)
Direction first: C. Oblique: "Remove specifics and convert to ambiguities" (counts not titles on landing); duplicate drawn, redrawn "Distorting time" (A fisheye rail; C scrubber spaced by event). Fields: sundial (time as a position; STANDBY is a complete reading), pharmacy drawer cabinet (C's grid). Constraint: no scrolling on landing (all). Twist: owner's words largest type (A's spine). Hue 131 → green ON.

## Notes for systems
- "Tests" is both a stage and a kind; sims exist at Concept. Suggest tests = kind only; rename the stage "Breadboard".
- D needs a stable numbering rule (concept prefix + sheet letter; D-numbers for docs, T-numbers for tests).

## Director's objections
- None yet (first visual turn).

## Open questions
1. Owner: who sees the link? Decides A (his verbatim words as headline type) and whether private records show.
2. Team: can the artifact page self-host a woff2 (assets/files/inline)? Fallback system stack (SF on iPhone) loses the shared face with the sheets.
3. Owner (later): colour for FAIL? I'd hold to none.
4. Team: dark mode via prefers-color-scheme (charcoal `#1F1F1D`)? Lean yes.
5. Systems: region sidecars from the sheet renderer: worth the change? I think yes.

## Next
- Director steers. Then systems writes `jobs.md`; we build concepts in `concepts/<name>/` (systems: how it works; me: how it looks and feels). C and the sheet viewer probably need a clickable prototype (scrubber feel, read-mode crops, A/B audio only show when used).
