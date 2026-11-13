# Director notes: instrument physical form

## Status (updated after pass 2, jam Turn 5)
- **Jam is done.** Next: concept building on CASE and DOCK against the Turn 5
  common spec, with eng verifying in parallel. Still no scores.
- Owner answers so far (owner.md): Q1 he uses the Vector Space makerspace
  (Prusas at ~250 mm, laser, CNC, TPU, sewing). Q3/Q4: "i dont think click
  would make sense for a keyboard.. i want it to feel like an instrument."
  He wants a built-in speaker *plus* outs, external audio into the filter, and
  MIDI control. **Q5 (look and lettering) is still open.** I re-asked it
  as two questions in Turn 5, adding the body material.

## Pass 1 record (Turn 3)
- Phase: concept jam. Turn 3 (my first) is done. **No scores yet.** Early
  scores will be provisional because no brand or visual foundation exists.
- Five foundation questions have gone to the owner (see the end of jam.md
  Turn 3): printer/bed size, where he plays and how he carries it, tactile
  keys vs. pads, speaker, hand-lettering plus a palette (Field/Proof/Desk).

## The three tests (from the owner's words)
1. Keys he'll love ("keys would be amazing"): has to feel like keys.
2. Grab it and go ("completely portable"): backpack-safe, couch-playable,
   battery.
3. No rigmarole ("incredible without a bunch of rigmaroll", "how ikea"): judge
   by subtraction. My cutting rule: one hero, one playing surface, one kind
   of control per section, one light.

## Concepts going forward (as of Turn 3; SUPERSEDED, see Pass 2 below)
1. **CASE** (seed A): clamshell instrument case, friction hinge, lid is the
   tilted knob panel, base has 2-octave Choc keys. Risks: hinge and ribbon
   life, lid depth vs. knob height, 300 mm width vs. printer bed.
2. **DOCK** (seed E × my Polaroid draw): the keyboard module is the lid. It
   docks in front to play, and flips face-up over a sunken knob panel to
   carry. Power-by-dock (Hall sensor). One module ships, and the connector
   spec stays open for later formes (ribbon, grid, breath). Risks: contact
   reliability, rattle, scope creep. **My current favourite, so be hard on
   it.**
3. **SLATE** (seed C): one flat board, ENIG copper pads, stylus, cloth
   hardcover. The deliberate dissent. Likely to fail "keys" and "dark"
   unless the key overlay gives real travel. Replace it if it doesn't.

Killed: B Rigging (bag, bed size, not keys; the ribbon lives on as a DOCK
module) and D Concertina (reach fails J2; the grid lives on as a DOCK module).

## Rulings made
- Left-edge performance strip (cutoff, emphasis, contour amount, glide, bend, mod).
- Two knob tiers (hero cutoff plus one standard cap), not three.
- Faders for the two contours only (6). The mixer stays knobs. Eng has a veto.
- Scribble strip cut. Breath port parked. Speaker is the owner's call (I lean no).
- Yes: hold/latch, tripod insert, audible boot tuning with a quiet-boot option,
  glow-filament pointers ("must work in the dark"), internal 18650 (eng final),
  one RGB LED.
- Hand-lettered legends: I'm for it, pending the owner.

## Likely owner objections (pre-scoring, watch for these)
- "These aren't keys" (SLATE especially).
- Too many parts or decisions: rigmarole creep (DOCK modules, faders).
- Too big for his printer or his bag.
- Anything that reads as Moog (wood cheeks, silver panel, skirted knobs).
- Toy-like: a stylus, black-and-white mini keys.

## Open questions (non-owner)
- Systems/eng: 25 keys in ≤245 mm? Board-mounted faders vs. S1/S2? DOCK pogo
  contact and Hall-sensor power? CASE hinge/ribbon cycle life? Is audible
  tuning measured pre- or post-VCA? 18650 confirmed?

## What's blocking a 9
Nothing has been scored yet. My early hunch for the recurring blocker is
scope (rigmarole) vs. delight. Watch whether the designers keep adding parts.

## Next
Systems turn → owner answers → concept building (CASE, DOCK, SLATE), with
each concept showing top and side views at real mm, both carry states, and
the print seam.


## Pass 2 rulings (Turn 5), which supersede Turn 3 where they conflict
- **Accepted all of systems' Turn 4:** one PCB architecture for CASE and DOCK
  (body board plus a keyboard module talking MIDI over UART). No analog
  crosses a contact. Power-by-lid (Hall sensor sleep) plus a master switch,
  not power-by-dock. CASE gets a 4–6 wire cable through a hollow hinge
  with a ~25° hard stop. 6 faders are OK with threaded-hole fader parts.
- **Keys: Choc is out** (the owner rejected click and keyboard feel). In:
  a **printed lever keybed**, one flexure comb per octave, with a magnet
  plus a TO-92 Hall sensor per key. Silent, continuous travel. Velocity and
  pressure are available but off by default. Fallback is a pin pivot plus a
  spring with the same sensing. Donor keybed rejected.
- **SLATE killed** (flat pads fail "instrument" and "dark"). **Two concepts
  go forward: CASE and DOCK.** I deliberately didn't invent a third. I'll
  replace one if it dies.
- **Width ~300 × 210 mm**, with two printed thumbwheels left of the keys.
  The left panel strip now holds cutoff (hero), emphasis, contour amount and
  glide.
- **The enclosure is a laser-cut stack** from the KiCad outline. FDM is
  only for the key combs, wheels, caps and small parts (all <250 mm).
  Trade-dress guard: wood only as full laminated stripes, never end cheeks.
- **Speaker:** a 50–57 mm driver in a sealed stack chamber at the right end,
  away from the VCOs. Headphones mute it, line out doesn't. The grille is a
  brand surface (possibly his drawing). In DOCK the speaker is in the body
  and must stay uncovered when docked.
- **Patch edge (rear):** PHONES, LINE OUT, EXT IN, FILTER CV IN, PITCH/GATE
  IN, PITCH/GATE OUT, TRS MIDI IN/OUT, USB-C (MIDI plus charging), master
  switch. 3.5 mm patch jacks. Eng owns the levels.

## Open questions after pass 2
- Owner: the look (Field/Proof/Desk), body material, hand-lettering and grille.
- Eng: PETG flexure fatigue; Hall gate threshold, hysteresis and boot
  auto-calibration; mux scan; class-D amp noise near the VCOs; patch-level
  conditioning; plus the Turn 4 list (sleep current, module MCU, pogo
  choice, fader part, S4).
- DOCK-specific: can the lever keys survive face-up as a lid in a bag?
  It needs a flexure travel stop and a rim proud of the key tops.

## Updated likely owner objections
- The lever keys feel mushy or cheap, not "instrument". This is the biggest
  risk now. The feel must be verified, not asserted.
- The speaker sounds tinny, after he called it "incredible".
- Wood stack drifting toward Moog trade dress.
- Rigmarole: printing combs, gluing 25 magnets. Can magnets press-fit into a
  printed pocket with no glue?
- Still too big or heavy to grab and go.

## Recurring blocker hypothesis
It's still scope versus delight. Each owner answer adds features (speaker,
patch edge, MIDI out). Hold the line on "one element of each kind" so the
panel and the build don't bloat.

## Pass 2 addendum (Turn 6), which supersedes Turn 5 where they differ
- **Owner direction:** show both "expected / highly designed for use" and
  "randomness-driven, more sauce / vibe" concepts. **The set is four:**
  - designed for use: **CASE** and **DOCK**;
  - sauce: **MOTTO** and **DISH**.
  - **MOTTO** (draw: harpsichord + rotary phone, "Water", one-handed): a
    bentside silhouette, reverse-colour keys, and a painted lid propped on a
    stick that reflects sound from the speaker in the tail. The lid is the
    owner's canvas. Oscillator range is a finger-dial ring, which must prove
    itself or be cut.
  - **DISH** (draw: harpsichord + radio telescope, destructive action,
    furniture): a circle cut from the panel becomes a tilting round dish on a
    yoke. Radial signal flow ends at cutoff in the centre, with the speaker
    behind it. The dish stows face-down. Fader fit and radial legibility are
    risks.
- **Owner Q5:** he'll make or hand paint the labels "based on outcome", and
  he needs **mocks** to pick a look. So every concept reaching him is a visual
  mock, plus one look sheet (Field / Proof / Desk × materials). My Turn 5
  owner questions are withdrawn. No look questions until he has seen mocks.
- **Adopted systems' updates:** laser-cut Delrin flexure comb keys (over my
  printed comb) with Hall sensing, 6–8 mm travel, velocity off by default;
  the magnet separation rule (speaker ≥60 mm from key sensors); any output
  mutes the speaker; MIDI over USB plus TRS in and out; CC74 → cutoff DAC
  sum; 1–2 × 18650.
- **Scoring plan:** one 1–10 scale, but each kind is judged against its own
  kind. All four must meet the stated jobs, and sauce doesn't excuse failing
  "instrument" or "portable".
- **Jam is closed.** Next is concept building, with eng verifications in parallel.
- **Watch for:** sauce concepts quietly dropping jobs (MOTTO's lid in a bag,
  DISH's fader fit), mocks that show the look but not the real proportions,
  and scope creep from the finger-dial and the second canvas.

## Concept building, round 1 (steering scores; nothing has gone to the owner)
- **Scores:** CASE 6 (replace), DOCK 7, MOTTO 7, DISH 6. Full detail and
  fixes R1–R9 are in `../scores.md`.
- **What I'd missed and have now absorbed (owner.md):**
  - OP-1 is only a loose reference, and "it should feel good to use"
    outranks it. Eng's box is ≈ 285 × 180 × 32–36.
  - At least two octaves. Keys must not drive the PCB, and he wants us to
    experiment with key ideas.
  - Ready-made modules only, one TH build variant, cost-driven.
  - MIDI-ownable controls per eng v2 §2 (pitch, glide, tune/freq, cutoff,
    both envelopes' A/D/S). Emphasis, mixer, waves, mod mix and contour
    amount are knob-only.
  - No endless encoders or screens. The "not in control" light is open.
  - A ~$100 budget instrument is separate and not this loop's concern.
- **Rulings:**
  - Size to feel in eng's box. Panel ≈ 95–105 deep, with minimum pitches and
    legends ≥ 2.5 mm.
  - **CASE cut → SLAB**: a rigid body with no joint, whose lid flips under
    as a wedge stand. It's the second designed-for-use concept.
  - DOCK goes to Delrin lever keys and must carry at < 45 mm.
  - MOTTO is the sauce lead: move off walnut-around-black, use an abstract
    lid placeholder, 11 pips, a ≥ 40 mm speaker.
  - **DISH rebuilt:** the dish = MCU/CV (MIDI-reachable) controls only and
    the wings = analog tone. The speaker moves to the base well. That turns
    the S10 problem into the concept.
  - Keys decoupled into one key menu, with samples recommended. Cost delta and
    step count go on every mock. The look sheet moves to SLAB or DOCK at the
    real size.
- **The concept set for round 2:** SLAB and DOCK (designed for use), MOTTO
  and DISH (sauce).
- **Open for systems and eng:**
  - Mod wheel: digital (common §2) or analog pot (eng v2 §2)?
  - Two-row sensor strip for DISH.
  - A larger dish carrying the envelope knobs?
  - SLAB's lid as a stand, plus the sleep sensor.
  - DOCK's carry section < 45 mm.
- **What keeps blocking a 9 (first read):** designers optimise to a
  *number* (OP-1 282 × 102) or an *assumption* (MIDI = cutoff + glide)
  instead of the owner's stated priority (feel) and eng's actual
  architecture. Both come from building before re-reading owner.md and eng
  v2. **Process fix:** each round's mocks must cite the owner.md entries
  and eng sections they were checked against. Second blocker: concepts that
  differ in mechanism but look identical from above.
- **Next:** designers' round 2 against R1–R9 → my steer → READY and full
  scoring when there are four concepts I'd defend.

## Concept building, round 2 (scored; nothing has gone to the owner yet)
- **Scores:** SLAB 8 (new), DOCK 6 (**retired**), MOTTO 8 (up from 7, real
  change), DISH 7 (up from 6, rebuilt). Nothing at 9. Full detail is in
  `../scores.md` under round 2.
- **New owner decisions absorbed (owner.md):**
  - one build variant (TH plus ready-made modules);
  - real bought parts for every touched control (no printed knobs, keys or
    wheels);
  - key tops cut by the owner at Vector Space;
  - **velocity required**, and **silence is a hard criterion**;
  - bend = a one-way spring-back stick, with a mod control that stays put;
  - knob-only controls send no MIDI, and MIDI never flips switches;
  - **cost is his main concern**;
  - no harvested keybeds, no printed samples.
- **Rulings:**
  - DOCK retired: over the box, 70 mm carried, costlier, and the knock means
    a reboot.
  - DISH rear pivot accepted.
  - SLAB stand at 8° only.
  - **Keys switch to eng route (b): Choc V2 silent + key-top magnet +
    TO-92** (quietest, with velocity). Gateron is the fallback after the bench
    test.
  - The key menu's K-C becomes the shared mechanism.
  - Bend stick = Adafruit #2765 slot-gated, which means a **22 mm left zone and
    a ≈ 292 mm body**.
  - Mod = a slide pot, analog, no MIDI, so no AS3360 is needed in the full
    version.
  - A full price on every mock.
- **The set is now three:** SLAB (designed for use), MOTTO (sauce lead), DISH
  (sauce). There's only one designed-for-use concept. Name that openly to the owner,
  as a deliberate choice: SLAB plus three looks.
- **Next:** a fix pass (F1–F5, S1–S2, M1–M4, D1–D5), then READY. I expect SLAB
  and MOTTO to reach 9 and DISH 8–9 depending on D1 and D2 (the cutoff and
  emphasis split, and dish rigidity).
- **Blockers:** (1) parts assumptions drift from eng; the process fix is that
  "checked against" cites the eng file section and revision. (2) Mechanisms
  swell size; draw honest thickness first.
- **For my own consistency:** I'm harder on DISH because I seeded it.
  MOTTO's 8 is earned by the bentside-as-panel move, not by my fondness for
  the lid.
