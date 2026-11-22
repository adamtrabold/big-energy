# TIDE: how it works (systems)

Status: **rev 1, 2026-11-22**, concept round 1. Read `../common-how-it-works.md` first; this file states only TIDE's own parts and departures.

**Life lives in time.** You plant notes, each with its own character, and then you tend the whole: drift, shimmer and space. BOW is played, KEPT is remembered, TIDE is tended (director, turn 5).

**Draws on:** TIDE (turn 4, with the director's condition in turn 5), [speed] "work at a different speed" (turn 1), [quiet] "listen to the quiet voice" (turn 5), the lantern (turn 2), BELFRY's latch (turn 1, as HOLD), WIND's breath (all concepts), and visual turn 6's HUSH face.

## 1. Structure

### 1.1 Body
- **HUSH**: a felt-skinned printed pebble with maple pegs on felt collars (visual turn 6). HUSH's frame is 290 wide [ENG]; its depth is set by the board, which eng sizes.
- **Power:** the family's recessed rear slide switch.
- **Passive radiator** in the domed underside. Eng: which way it fires. Firing into a lap would muffle it, so it may need side vents or a short foot ring to keep a gap.
- **Lantern:** three warm LEDs behind the speaker holes, following the ensemble's three phases (0 / 120 / 240°, verified). Depth sets how far the light moves; depth at zero gives a still, dim glow. Amber means the analog mode, paler means Daisy modes. **It never signals state.** It's a few mA in the power budget.

### 1.2 Panel map (PROPOSAL; visual places it)
| | Left region | Centre (axis) | Right region |
|---|---|---|---|
| **Front** | OCTAVE L · ATTACK · RELEASE · PRESSURE | **HOLD** peg (front, nearest the keys) | DEPTH · ECHO · REVERB · OCTAVE R |
| **Rear** | TONE · SHIMMER | **DRIFT** (coral, large), status light | TIME · FREE / SYNC · REPEATS · TAP · VOLUME |

- **The centre is wider than BOW's gutter.** DRIFT is the hero and larger than a standard knob (≈ 20 mm or more). TIDE's centre band widens to about 28 mm. The 9 mm off-centre honesty is unchanged: the coral rim tick still marks B|C.
- **TAP moves to the echo group** (right rear) because the centre is taken. That's fine: in TIDE, TAP serves the echo, not the axis.
- **Count:** 16 round controls or toggles + HOLD + light. No tabs.
- **The keys** are HUSH's maple pegs. HOLD is a 26th peg on its own collar, because you press it like a key and it holds every key.

## 2. Engine (TIDE's departures)
- **One tone per key, no registers.** Colour comes from TONE, DRIFT and the shimmer.
- **Default shimmer: analog.** TIDE has to stay analog-first or it becomes "a reverb with keys" (turns 4–5).

### 2.1 Per-key drift: DRIFT knob (TIDE's hero)
- Each key's tone wanders on its own slow random walk (≈ 0.02–0.5 Hz, independent per key). DRIFT sets how far: fully left = rock steady; full = about ±25 cents (PROPOSAL; eng and owner to tune by ear).
- A held chord slowly beats against itself and never repeats exactly. It's free in structure B (each key is its own oscillator).
- In BOW and KEPT, drift is fixed and tiny; only TIDE gives it a knob (director, turn 5).

### 2.2 Velocity means lifespan, inverted [quiet]
- **Soft strike = the longest, most wandering note:** slow attack, long tail, more personal drift.
- **Hard strike = present, steadier, shorter:** fast attack, shorter tail, less drift.
- ATTACK and RELEASE set the ranges. **RELEASE's range runs to ≈ 30 s** in TIDE (PROPOSAL).
- Loudness doesn't change with velocity. Every note reaches full level eventually.

### 2.3 Pressure: what you plant
- Positions: **drift** (default) · **swell** · **tone** · **shimmer**. Drift replaces vibrato, which is just fast drift.
- **drift:** leaning on a key while it's down raises *that note's* wander above the DRIFT knob. **The note remembers it when HOLD keeps it.** So you plant each note with its own character.
- swell, tone and shimmer behave as in common §2.3.

### 2.4 HOLD: whole keyboard, notes add up, re-strike pulls one out
- **While HOLD is on, every note you play joins the held set.** You build a chord a note at a time, across both halves.
- **Strike a held key again and that note lets go,** fading on a tail set by the re-strike's velocity (soft = long fade). You pull single notes out of the chord without touching anything else.
- **HOLD off:** every note fades on its own tail.
- **Up to 25 held notes.** Past that (from MIDI), the oldest note leaves.
- Held notes keep their pitch through octave changes. New notes use the new octave, so a planted chord can span more than the keys' range.
- **Why it differs from BOW and KEPT (which replace the chord):** TIDE's point is accumulation and tending. A replace-latch would make it a performance instrument again.

## 3. Flows (TIDE-specific)

**F1 Grab and play.**
1. Set the pebble on a bench and switch on (rear). The light is steady; the lantern glows dim.
2. Play.

**F8 Plant and tend (TIDE's main flow; J10, J4, J5).**
1. Press HOLD (its peg stays down or its dot lights).
2. Play a low note softly: it blooms slowly and will wander the most.
3. Play a note higher up hard: it arrives quickly and stays steady.
4. Lean into a third note (pressure on drift): it gets its own wider wander, remembered.
5. Hands off the keys. Turn DRIFT up, raise DEPTH, add echo and reverb. The lantern moves.
6. Strike one held note again to pull it out. Play a new one to add it.
7. HOLD off: it all fades, each note on its own tail.

**F2 Split.** Common. In TIDE it matters most while planting: set the left half low, plant a bass, then plant high notes on the right.

**F13 Duet.** A friend plants notes into the held set while you tend the knobs. TIDE's duet is cooperative, not two parts.

**F14 Pack.** HUSH's felt pebble has no lid; a sleeve, as Big Energy's HUSH (deferred there).

## 4. States (beyond common)
| State | What happens | What you see |
|---|---|---|
| HOLD on, nothing played yet | silent, waiting | HOLD down or lit |
| HOLD on, 25 notes | full; the next MIDI note replaces the oldest | — |
| Re-strike of a held note | that note fades (tail from velocity) | — |
| DRIFT full, many notes | slow beating, chorus-like | lantern moving (if depth > 0) |
| Battery flat during a long hold | sound stops | light flashing first (low-battery warning) |
| Depth 0 | no shimmer; lantern dim and still | lantern |
| Daisy mode | lantern paler | lantern |

## 5. Coverage against `jobs.md` (round 1)
| Job | Supported? Where |
|---|---|
| J1 | yes: battery, speaker, radiator (direction to check) |
| J2, J3, J6, J8, J9, J11, J12, J16, J17 | yes: common |
| J4 velocity per note | yes: lifespan (§2.2) |
| J5 pressure + selector | yes: drift default, 4-way (§2.3) |
| J7 colour | **weak, as designed:** TONE only, no registers. It's an inferred job, so it doesn't block, but the owner must see that TIDE has no tone colours |
| J10 hold | yes: whole keyboard, add and pull out (§2.4) |
| J13 read state | yes: pointers, HOLD, light. **Gap:** which notes are held isn't visible (no screen); you hear it. That's honest, not blocking |
| J14 | yes |
| J15 park | yes: sits on a bench, made for it; lap depends on the radiator direction |
| J18 duet | yes, cooperative (F13) |
| J19 point of view | yes: one idea (time) in the engine, HOLD, DRIFT, lantern |
| J20 family | yes: HUSH body, pegs |
| J21 build / fix | yes: no strands; the lantern adds 3 LEDs |

## 6. Push, risks, open
- **Push:** add-and-pull-out HOLD is what makes TIDE differ in kind. I'd lead the concept with F8.
- **Risk 1:** overlap with the Daisy modes. Mitigation: analog-first defaults, per-key drift (no reverb can fake that), and coral on DRIFT, not on reverb.
- **Risk 2:** no registers may read as "less instrument". The owner decides.
- **Open:**
  - Does the HOLD peg latch mechanically (a push-push) or electrically with a dot? Visual and eng.
  - DRIFT's maximum (by ear).
  - The radiator's direction.
