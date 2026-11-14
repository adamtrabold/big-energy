# Little D: jobs and flows

Status: **rev 5, 2026-11-13 (branches)**: J20–J28 and flows F13–F15 added for the branches work (personality and emotion, the park, MIDI-synced echo with the owner's FREE / SYNC decision "B"); J19 now points at F13/F14. Everything in rev 4 stands. rev 4, 2026-11-13 (J19 echo + reverb added; all three concepts share common rev 7's balanced layout). Rev 3, 2026-11-12, systems designer (round 4: active concepts HUSH, FOLD, ONE SHEET; common rev 6 PLAY row + VOICE layout; owner deferred case work for HUSH and ONE SHEET). Rev 2: owner answers and director round 1; keys are bought Choc V2 switches with short tops. Drawn from the owner's words (`owner.md`, `instrument/owner.md`), the jam (`jam.md`, director's rules H1–H9), `eng/budget-variant.md` Part 1 and `eng/keys-answers.md`.

Marks: **stated** = owner's words. **inferred** = mine (scope questions, not demands). **[ENG]** = eng figure. **[CALC]** = my arithmetic.

The checker walks every job below on the build. A job passes only if every step of its flow can be done with the controls and parts named.

---

## Jobs

| # | Job | Source |
|---|---|---|
| J1 | **Play notes on 25 keys that feel like an instrument**: real travel, silent, no click, velocity. Not necessarily a traditional keybed. | stated. Velocity → loudness / filter / both via the VEL toggle (owner: "Both, with a switch") |
| J2 | **Bend pitch with a stick that springs back to centre, moving in one direction, and set mod depth with a dial that stays put**, with the hand that isn't playing. | stated: up and down on one axis, springs to centre (owner) |
| J3 | **Shape the sound live**: reach every control of the voice, one control per function, while the other hand plays. | stated (control set settled); "while playing" inferred |
| J4 | **Read the patch from the panel** (knob positions are the state; no screens, no encoders), **and keep a patch he likes** (no recall, so: on paper). | first half stated; "keep a patch" inferred from "i dont think recall is important" + Model D patch-chart habit |
| J5 | **Hear it** from the built-in speaker (on a table *and* on a lap) and from phones/line out. | stated; lap inferred |
| J6 | **Carry it** (small, portable) **and have it survive a bag**: knobs, stick, keys, jacks. | carry stated; survive inferred. **Round 4: owner deferred case/sleeve work for HUSH and ONE SHEET** ("Let's not worry about a case for hush or one sheet yet"): their bag survival is marked deferred, not failed. FOLD self-protects |
| J7 | **Power it** from internal LiPo or a USB bank; charge it; play while charging; know the charge; it can't switch on by itself in a bag. | power stated; the rest inferred |
| J8 | **Play and control it from MIDI** (USB + TRS): notes, bend, mod depth, and the MIDI-controllable params with jump-on-move; **know when a knob isn't in control and take it back**. | stated; indicator light open (owner undecided) |
| J9 | **Patch it**: pitch CV out, gate out, filter CV in, EXT audio in; cables don't cross the keys or the stick. | stated (no extra patch points) |
| J10 | **Stay in tune with no rigmarole**, and know when it's tuning, ready, or failed. | stated |
| J11 | **Build it himself**: hand-solder through-hole + plug-in modules, cut the enclosure and key parts at Vector Space, bought parts for everything touched, at the lowest cost. | stated |
| J12 | **See one clear idea in the object**: every form decision traceable to 3–5 explicit principles that follow from what the thing *is*. | stated ("coherent in form… clear perspective… design principles with a solid basis of logic in the idea of the thing") |
| J13 | **Label, letter or paint it by hand** where it's meant, never where it must be exact (H6). | stated ("i can make the labels myself or hand paint it") |
| J14 | **Open it to service it**: battery, one key, reflash the Pico (BOOTSEL), a solder joint; without destroying anything. | inferred (kit, test unit) |
| J15 | **Play it where he is**: table, lap, couch; tilted. | inferred (portable) |
| J16 | **Find the main controls and keys without looking**, in a dim room. | inferred |
| J17 | ~~Prove the full version's keys by building RAIL here once.~~ **Retired:** owner doesn't want to build custom keys; keys are bought switches | — |
| J19 | **Add echo and reverb while playing**: set echo time and repeats, reverb amount, and the wet/dry mix with the free hand; choose the echo type and the reverb type, set the tempo by tapping (or follow MIDI clock), use echo, reverb or both; turn it fully off (mix at zero leaves the dry sound untouched); hear it on the speaker and the phones/line out. | stated ("Is there a way for us to build in some effects, mainly a delay and echo?"; "I want echo and reverb"); "while playing" and "fully off" inferred. Round 5 final (common rev 7.1, FOLD 5.3): echo TYPE (TAPE/BBD/CLEAN/PING-PONG), reverb TYPE (PLATE/HALL/SPRING/SHIMMER), TIME, REPEATS, ECHO MIX, DECAY, REVERB MIX, TAP (owner: "Full 8"). Amounts (REPEATS, both MIXes, VOLUME) in the PLAY row; kinds and times + TAP in the FX row. Steps: turn ECHO MIX up → set TYPE/TIME (or TAP in tempo) → REPEATS → REVERB TYPE/DECAY → REVERB MIX; both MIXes at zero = dry. Chip: Pico 2 core 1 + Teensy Audio Shield (eng `single-chip-research.md`). **Rev 5:** chip is the Daisy Seed (owner); tempo, clock and the FREE / SYNC toggle are J23–J27, flows F13–F14 |
| J18 | **Keep it out where it gets played** (hang on a wall or stand on a shelf), where the concept has a finished bottom. | inferred (director's donor); optional, not a blocker |
| **J20** *(new, branches)* | **Feel one point of view in the object, and want to play it**: one idea drives form, material, graphics, making and feel, drawing on furniture, instruments, tools, art and emotion; the object has personality and puts him in a mood. Goes beyond J12 (logic) to feeling. | stated ("more personality"; "holistic *point of view* / concept"; "principles of design of furniture… instruments, tools… artistic inspirational forms and emotion"; "be inspired") |
| **J21** *(new)* | **Play keys with character.** His example: HUSH's pegs; on FOLD maybe "organ like". An example, not a direction: a branch may answer it with flat keys. | stated as example ("i *love* the peg keys on the hush") |
| **J22** *(new)* | **Take it to the park and play it there.** Its parts, all inferred: (a) carry it on a walk and be playing within a minute of sitting; (b) play on grass cross-legged, a bench or a lap, without sliding or tipping, damp grass no problem; (c) read the panel and the status light in bright sun and dappled shade; (d) hear it outdoors (no walls) or on phones; (e) last an afternoon on battery and know what's left; (f) survive sun on the body, grass, dust, a drop on turf, water nearby; (g) share it: a friend on the bench sees, hears, has a go. Stretches J5, J7, J15. | stated ("i want to take this to the park and be inspired"); (a)–(g) inferred. Session length: **owner question open** |
| **J23** *(new)* | **The echo follows MIDI tempo when a clock is present**, from USB or TRS MIDI IN. | stated ("make sure the delay can be timed to the midi if there is midi tempo control") |
| **J24** *(new)* | **Turn tempo sync on and off, and see which it's in**: the FREE / SYNC toggle by TIME; its position is the state. | stated (follow-up: "am i missing a control to turn that tempo sync on / off?"); **owner decision 11:58: "B"** |
| **J25** *(new)* | **Pick the echo's note division in SYNC; set a free time in FREE**: TIME read on two printed scales (ms; 9 divisions). | stated by decision B ("SYNC: TIME picks a note division") |
| **J26** *(new)* | **Nothing jumps or clicks** when the clock starts, stops, drops out or changes tempo. | inferred |
| **J27** *(new)* | **Keep a tempo with no clock** (the park has no DAW): tap it on TAP and see it confirmed. | inferred (J19 already has TAP; the "see it" part is new) |
| **J28** *(new)* | **Choose ONE SHEET or FOLD late** without the branch work being wasted: the board is the constant, the outside is the branch. | inferred ("the internals are probably the same eh?") |

### Scope notes
- **Rev 5 (branches):** J20–J28 apply to the branch concepts in `design/branches/concepts/`. J23–J27 (echo sync) apply to whichever concept is built (owner: "B"). J22's parts are inferred; a branch may answer some weakly but must say which.
- J4's "keep a patch on paper" and J18 are inferences; a concept may skip them without failing, but must say so.
- J6's "survive a bag" without a separate sleeve is pending the owner (A4). Concepts that rely on a sleeve must say which sleeve and its cost.

---

## Assumptions while owner questions are pending

Designers proceed on these; each concept names any it depends on.

| # | Pending question | Working assumption | What changes if the answer differs |
|---|---|---|---|
| A1 | No Moog trade dress? | **ANSWERED:** "Nods are fine but I want to see breadth of exploration" | Subtle nods allowed; breadth across concepts is the priority |
| A2 | Bend axis | **ANSWERED: up and down**, one fore-aft axis, centre-sprung | — |
| A3 | Board finish | **ANSWERED: standard printed** (mask + silkscreen) | UNDER GLASS shows it |
| A4 | Self-protecting body vs sleeve | **ANSWERED: "Show me both"** | TYPE CASE, HYMNAL self-protect; UNDER GLASS and HUSH (default) use a sleeve |
| A5 | Thickness | **Working decision:** ≈ 36 mm body, ≤ 40 mm to knob tops (orchestrator's recommendation, owner not objecting) | All depend on eng E-L2 (speaker depth) |
| A6 | Velocity routing | **ANSWERED: "Both, with a switch"** → VEL toggle LOUD / BOTH / FILT in IV [ENG v2] | — |
| A7 | Flat tops vs maple pegs | **ANSWERED: "Show me both"** → short flat tops in three concepts, maple pegs in HUSH | Piano-length tops = +$29.85 variant [ENG S2] |

---

## Flows

Each flow lists its steps and the control or part each one uses. Concept-specific steps (open, close, unroll) are marked **[concept]**; each `how-it-works.md` fills them in.

### F1 Grab and play (J6, J7, J10, J15)
1. Take it out of the bag. **[concept]** open / unroll / nothing.
2. Set it on a table or lap (feet / soft base / cover as rake **[concept]**).
3. Power switch (recessed, H7) → on.
4. Status light: **tuning** (autotune at boot, a few seconds [ENG]).
5. Status light: **ready**. Or **tune failed** (blink count = VCO number) → power-cycle; if it repeats, F9.
6. Play: keys + stick + MOD dial.

### F2 Build a sound from scratch (J3, J4, J16)
Reading order (CATHEDRAL steer 3, cathedral §17): **the lid top → bottom in signal order, left → right in each band: oscillators ‖ mixer → filter contour · loudness contour (their switches beneath) → echo · reverb ‖ out (DRY PAN, FOLLOW, VOLUME last, bottom right); then over the hinge to the PLAY row: controllers → filter (with KBD / FILT MOD beside CUTOFF) → tune (TUNE, DRIFT, echo tap); every toggle shows its positions (cathedral §18).** (Common rev 6 §1, superseded for CATHEDRAL: the VOICE back two rows left → right, then the PLAY row.) (Rev 5 order, for the paused concepts: left → right by section I–V, front → back.) The step list below names controls by function; it holds in either layout.
1. I CONTROLLERS: TUNE centre, GLIDE off, MOD MIX, OSC MOD / FILTER MOD toggles off.
2. II OSCILLATORS: per VCO, RANGE (6 marked positions, no click [ENG]), WAVE (6-way rotary), FREQ (VCO 2, 3); OSC 3 CONTROL toggle.
3. III MIXER: OSC 1–3 levels, NOISE/EXT level, SOURCE toggle (noise / ext / feedback).
4. IV MODIFIERS: CUTOFF (hero), EMPHASIS, CONTOUR AMT, KEYBOARD CONTROL toggle; filter A/D/S; VEL toggle; loudness A/D/S; DECAY toggle.
5. V OUTPUT: VOLUME.
6. Play to hear it; adjust.

### F3 Perform (J1, J2, J3, J5)
1. Right hand on keys (velocity per the VEL toggle: loudness / both / filter).
2. Left thumb on the bend stick (springs back); left fingers set MOD dial (stays put). Rev 6: both sit at the left end of the PLAY row, behind the low keys, not beside them.
3. Left hand leaves to ride CUTOFF / CONTOUR AMT / EMPHASIS (all in the PLAY row, the row nearest the keys), returns to the stick. **Measured reach stick → CUTOFF = 120 mm** in common rev 6 [CALC] (was ≈ 196 in rev 5).
4. Glide and legato: hold one key, play another; low-note priority, single trigger [ENG].

### F4 Keep a patch (J4, inferred)
1. **[concept]** where the paper lives (HYMNAL: endpaper; others: a printed patch-chart card the size of the panel, kept in the bag or a slot).
2. Pencil the knob positions; later, set knobs by eye from the chart.

### F5 Pack (J6, J7)
1. Unplug cables (or leave them: jacks are on one edge, H9).
2. Power off; the recessed switch can't be knocked on in a bag.
3. **[concept]** close / roll / sleeve.
4. Into the bag. Nothing proud of the outline snags; nothing pressed can break (a pressed key travels into silicone, harmless when off).

### F6 Charge, and play while charging (J7)
1. Cable into the USB-C (or the single USB, if eng ties Pico VBUS to the charger).
2. Status light shows **charging** (off or on); **charged** when full.
3. Plays meanwhile (load-sharing [ENG]).
4. **Low battery**: status light warns before the boost stalls.

### F7 MIDI (J8)
1. USB to a computer, or TRS MIDI in from a controller.
2. Notes, bend, mod depth (CC1), and MIDI-controllable params arrive.
3. A MIDI-set param holds its value; its knob doesn't move.
4. **Which knobs can be overridden** is machine-marked on the panel (a small engraved dot by each Pico-read knob: RANGE ×3, FREQ ×2, TUNE, GLIDE, CUTOFF, MOD) (H6).
5. If adopted: the **"not in control" light** beside CUTOFF is lit while any marked knob is under MIDI's value.
6. Move a marked knob → it takes over (jump-on-move); the light goes off when none are overridden.
7. ~~Knobs send CC out over USB~~ **(superseded 2026-11-13: a team inference, not an owner decision; see `docs/features/midi.md`. Today only channel pressure sends.)** Unmarked (knob-only) controls send nothing; MIDI never flips toggles (stated).

### F8 Patch (J9)
1. Cables into PITCH CV out, GATE out, FILTER CV in, EXT in (with SOURCE = ext and NOISE/EXT up).
2. All jacks on one edge **[concept]**; cables leave away from the keys and the stick (H9).
3. Play while patched; cables don't block any control.

### F9 Build (J11)
1. Cut all enclosure parts **[concept: material, sheets]** and key parts (acrylic) at Vector Space.
2. Solder the main board (280 × 100) and strip C (key strip), including 25 Choc V2 silent switches and 25 flat SS49E sensors [ENG v2].
3. Cut a test strip of MX cross-pocket widths; cut the 25 tops; glue a D31 magnet in each; press the tops on [ENG v2].
4. (HUSH: glue maple pegs onto hidden caps.)
5. Fit the stick through its gate plate, **then** its cap [ENG §v1.5b].
6. Mount the board, battery, speaker; close the body **[concept]** with visible screws on the closing face.
7. First boot: autotune; keys self-learn rest [ENG].

### F10 Service (J14)
1. **[concept]** open the closing face (screws only; nothing glued shut across a service path).
2. Battery: unplug the JST, swap.
3. One key: pull the top off; if the switch failed, desolder its 2 pins and replace it.
4. Reflash: BOOTSEL reachable (button hole or with the closing face off **[concept]**).

### F11 Label (J13)
1. Machine marks (laser, in the cutting job): RANGE positions, pot scales, jack legends, MIDI dots, toggle positions.
2. Hand marks **[concept]**: section names, numerals, title, figures — painted, lettered, printed or embroidered.

### F12 Keep it out (J18, optional)
1. **[concept]** hang from a keyhole slot / stand on a shelf; or say why not.

### F13 Echo in time with a MIDI clock (J23, J24, J25, J26) *(new, rev 5)*
Spec: `design/branches/echo-clock.md` (option B, owner-approved).
1. Connect the clock: rear USB-C to a computer/DAW, or TRS MIDI IN from a drum machine or sequencer.
2. FREE / SYNC toggle → **sync**.
3. Start the clock. Status light: 2 green flashes = locked (after one beat, 24 ticks).
4. ECHO MIX up; pick a division on TIME's **outer** scale (1/16 … 1/2; dotted marked by a dot, triplets by a triangle); REPEATS to taste.
5. Change the tempo at the source: the echo follows. TAPE / BBD glide (≈ 150 ms, like a tape motor), CLEAN / PING-PONG crossfade (≈ 50 ms).
6. Stop the clock (or it drops out for 500 ms): tails ring on; the echo holds the last tempo; 2 amber flashes.
7. Free time again: toggle → **free**; TIME reads its **inner** scale (≈ 20 ms – 2 s); the clock is ignored.

### F14 Tap a tempo with no clock (J27, J22) *(new, rev 5)*
1. Toggle → **sync**. Tap TAP 2–4 times on the quarter note (taps > 2.5 s apart start over).
2. The status light flashes the tempo 4 times (green, 40 ms). Pick a division on TIME.
3. Or toggle → **free** and tap the echo length itself; moving TIME takes back over (jump-on-move).
4. With a clock running in sync, TAP doesn't change the tempo: 1 short amber flash says the clock has it.

### F15 A park session (J22, J20) *(new, rev 5)*
1. **[concept]** carry: how it's held or bagged on a walk.
2. **[concept]** sit: grass cross-legged, a bench, a lap; what touches the ground; how it's tilted to the eye.
3. Power on (recessed switch); status light **ready**, readable in sun (the light sits under a short hood / light pipe, every branch).
4. Play on the speaker (**[concept]**: which way it fires outdoors) or phones.
5. Tap a tempo (F14); the echo is in time.
6. A friend has a go: keys and stick reachable from beside; **[concept]** what the friend sees.
7. Low battery warns before it stops (status light); power off; **[concept]** pack and walk.

---

## States the hardware must show

| State | Where | How |
|---|---|---|
| Off | status light | dark |
| Tuning | status light | slow pulse |
| Ready | status light | steady, dim, warm |
| Tune failed | status light | blink count = VCO number, repeating |
| Low battery | status light | slow flash, different colour |
| Charging / charged (on or off) | status light | pulse / steady |
| A knob not in control (MIDI holds it) | optional 2nd light beside CUTOFF | lit while any marked knob is overridden |
| Which knobs MIDI can override | panel | engraved dot by each (permanent) |
| RANGE position | panel | engraved 6-position scale (no detent click [ENG]) |
| Bend at rest | stick | centred by its spring, visibly in the middle of its slot |
| Mod depth | MOD dial | its pointer |
| Carry vs play | body | **[concept]** closed / open, rolled / unrolled |
| **Echo free or synced** *(rev 5)* | FREE / SYNC toggle by TIME | lever position (left = free, right = sync, legends beside it) |
| **Which TIME scale to read** *(rev 5)* | TIME | inner ring = ms, outer ring = divisions; printed over 270°, the last 15° at each end clamp (firmware) |
| **Clock locked / lost** *(rev 5)* | status light | 2 green flashes on the beat / 2 amber flashes (low priority: tune-failed and low battery win) |
| **Tempo after a tap** *(rev 5)* | status light | 4 green flashes at the tempo |
| **TAP ignored (clock has the tempo)** *(rev 5)* | status light | 1 short amber flash |
