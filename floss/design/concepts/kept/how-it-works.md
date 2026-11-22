# KEPT: how it works (systems)

Status: **rev 1, 2026-11-22**, concept round 1. Read `../common-how-it-works.md` first; this file states only KEPT's own parts and departures.

**Life lives in history.** A faithful string-machine panel, in the order a Solina player knows, with every innovation under the fingers. It tests whether the owner wants floss to *look* new or *feel* new.

**Draws on:** KEPT (director, turn 3), the Solina fact the director checked (bass registers only on the low region; crescendo and sustain sliders), DISH RACK as the benchmark for fewest controls (turn 1), STOPS merged in (turns 2–3), and visual turn 6's ONE SHEET face.

## 1. Structure

### 1.1 Body
- **ONE SHEET**: one printed shell, 276 wide (Big Energy common rev 7.1 [ENG]). It's the slimmest and most portable body.
- **Two rows** (front y 68, rear y 100), so it's shallower than Big Energy's three-row ONE SHEET. Depth is set by the board, which eng sizes; Big Energy's 276 × 140 before the board grew is the floor.
- **Power:** the family's recessed rear slide switch.
- **Passive radiator: probably not** (visual turn 6). The sealed volume competes with the battery in a slab. KEPT trades the fullest sound for the smallest body, and says so.

### 1.2 Panel map (PROPOSAL; visual places it)
The centre gutter sits over middle C (axis 138 in ONE SHEET's frame).

| | Left region (over the left half) | Gutter | Right region (over the right half) |
|---|---|---|---|
| **Front y 68** | OCTAVE L · **bass** tab · HOLD · ATTACK · RELEASE | status light | **strings** tab · **brass** tab · **DEPTH** (coral) · VOLUME · OCTAVE R |
| **Rear y 100** | PRESSURE · ENSEMBLE mode | TAP | ECHO · TIME · FREE / SYNC · REPEATS · REVERB |

- **The Solina's order across the front:** registers, then crescendo / sustain (ATTACK / RELEASE), then ensemble, then out.
- **The bass tab sits over the left half because it only sounds there** (visual turn 6). That's a spatial truth, not decoration.
- **Rear:** touch and the ensemble's kind on the left; the room on the right.
- **Count:** 14 round controls or toggles + 3 tabs + TAP + light. Some front slots carry tabs, so the front row is denser than the rear on the left. Visual to balance.
- **No TONE knob.** The Solina had none: its colour came from the register voicings. **KEPT is the smallest panel of the three that still covers every stated job.**

## 2. Engine (KEPT's departures)

### 2.1 Registers: the Solina's answer
- **One tone per key** (25 outputs). No strands.
- **Three fixed voicings (shared filters):** **strings** and **brass** on the summed signal; **bass** taps the **left-half bus only** (common §1) through a darker voicing. That's three filters, cheap.
- **bass only sounds on the left half.** With both octaves at 0, that's C3–B3; turn OCTAVE L down and the bass goes down with it. The Solina's fixed region (contrabass and cello on C2–G3), made movable.
- **Muting differs from common §2.6:** strings and brass act on both halves, so KEPT can't mute only the left. **bass on alone = left half only** (the right is silent). All three off = silent.

### 2.2 Velocity means loudness (I'm reshaping the director's table here)
- The director's table said "the Solina's crescendo, made per note". Crescendo *is* attack time, so that makes KEPT's velocity the same as BOW's (speed). The two concepts would then differ in name only, which is the convergence the director warned about.
- **So KEPT uses the meaning every keyboard player already has: hard = louder and a touch brighter.** ATTACK is the Solina's crescendo for every note, set by the knob.
- That fits KEPT's idea exactly: it looks like 1974 and plays like a modern keyboard, with nothing to relearn. BOW is speed, KEPT is loudness, TIDE is lifespan: three different answers for the owner to choose between.

### 2.3 Pressure
- **swell · vibrato · tone · shimmer**, default **vibrato**: the most "string section" gesture on a familiar-feeling instrument.
- **"tone" with no TONE knob:** it opens the register voicings' brightness from their fixed setting. The rule "pressure adds, never goes below" still holds.
- No thinning behaviour (that's BOW's).

### 2.4 HOLD: left half, new chord replaces (as BOW)
Why the same as BOW: in KEPT the left half is the bass region, and holding a bass drone under right-hand strings is the classic use.

### 2.5 ENSEMBLE, not SHIMMER, as the label
- On KEPT the mode knob is labelled **ensemble**, the Solina's word and a plain one. The analog mode is its default.
- **Coral goes on DEPTH:** the ensemble is KEPT's 1974 soul (visual turn 6).

## 3. Flows (KEPT-specific)

**F1 Grab and play.**
1. Rear switch on: steady light, ready.
2. strings is on by default (the tabs stay where you left them).
3. Play.

**F2 Split.** Common. Turn OCTAVE L down with **bass** on: a moving bass under strings on the right. That's the Solina's own split, made movable.

**F3 Play expressively.**
1. Strike: louder or softer.
2. Lean: vibrato on that note.
3. Lift: the tail (common).

**F5 Colour.**
1. strings, brass, bass tabs.
2. bass alone = left only.
3. All off = silent.

**F14 Pack.** ONE SHEET has no lid. Bag survival needs a sleeve, as Big Energy's ONE SHEET did (the owner deferred case work there). The cost goes in the concept.

## 4. States (beyond common)
| State | What happens | What you see |
|---|---|---|
| bass only on | right half silent; left plays bass | only the bass tab up |
| strings and brass off, bass on, octaves equal | the lower 12 keys sound, the upper 13 don't | tabs |
| all tabs off | silent | all tabs down |
| pressure on "tone" | brightens above the fixed voicing | — |
| no radiator | thinner low end on the speaker than BOW or TIDE | — (heard) |

## 5. Coverage against `jobs.md` (round 1)
| Job | Supported? Where |
|---|---|
| J1 | yes: battery, speaker; sound thinner without a radiator |
| J2, J3, J6, J8, J9, J11, J12, J16, J17 | yes: common |
| J4 velocity per note | yes: loudness (§2.2) |
| J5 pressure + selector | yes (§2.3) |
| J7 colour | yes: bass left-only, strings, brass (§2.1); per half only for bass |
| J10 hold | yes: left half |
| J13 read state | yes: tabs, pointers, light |
| J14 | yes: rear switch, instant |
| J15 park | yes: the lightest and flattest; a lap is fine; **needs a sleeve** for the bag |
| J18 duet | **weak:** the right player gets strings / brass / depth / volume / octave, but the tabs act on both halves, so they share the colour. Honest, not blocking (an inferred job) |
| J19 point of view | yes: "1974 on the outside" |
| J20 family | yes: ONE SHEET |
| J21 build / fix | yes: the fewest chips of the three (no strands) |

## 6. Push, risks, open
- **Push:** KEPT is the cheapest and simplest build and the slimmest body. It's the conventional answer allowed to win.
- **Risk:** it may feel like "a Solina clone with velocity" to an owner who wants a point of view. The answer is that the innovation is in the hands; the director accepted that framing.
- **Open:**
  - Is three tabs enough, or does the owner want the Solina's six?
  - Sleeve cost (visual / eng).
