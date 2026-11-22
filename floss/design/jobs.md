# floss: jobs and flows

## The jobs, short (for the owner: anything wrong or missing?)

1. Play warm, shimmering string chords anywhere: battery, built-in speaker, no setup.
2. Play as many keys at once as I like, with every note sounding.
3. Split the 25 keys and set each half's octave on its own; set both the same and it's one keyboard.
4. Shape each note by how hard I strike it.
5. Lean into notes I'm holding, and choose what leaning does.
6. Shape how each note ends by how I lift off. (inferred)
7. Choose the tone colour (which sounds or layers play), per half where it makes sense. (inferred)
8. Choose the shimmer, analog ensemble or a digital mode, and how much.
9. Add echo and reverb; the echo follows MIDI tempo when there is one, and I can tap a tempo when there isn't.
10. Hold a chord or drone without holding the keys. (inferred)
11. Hear it on the speaker; plug in headphones and the speaker goes quiet.
12. Use it with other gear over MIDI: play it, play other things from it, split the halves onto two channels or not, and send velocity and pressure.
13. Read everything from the panel, with no screen, by eye or by touch, including how the keyboard is split.
14. Switch on and be playing within seconds; know the battery and the charging. (inferred)
15. Take it to the park and play it on a bench or my lap, in sun or shade. (inferred)
16. Lots of notes don't distort, and one note doesn't sound thin. (inferred)
17. Play in tune with other instruments. (inferred)
18. Hand a friend the other half and play together. (inferred)
19. See one clear point of view in the object, and want to play it.
20. Belong to the same family as Big Energy: same case family, parts and way of building.
21. Build it myself and open it up to fix it. (inferred, from Big Energy)

---

Status: **rev 1, 2026-11-22**, product designer (systems focus). It comes from the owner's floss words (`design/owner.md` 2026-11-21 onward, `BRIEF-CONTEXT.md`) and the closed jam (`jam.md` turns 1–6). Big Energy's `design/jobs.md` was used as reference only.

**"Inferred"** means the owner didn't say it; the team inferred it. A concept may answer an inferred job weakly, but it must say so. A stated job that a concept can't do sends it back.

## Jobs in detail

| # | Job | Source | What a concept must show |
|---|---|---|---|
| J1 | Play warm, shimmering string chords anywhere | stated: "portability factor", "Analog voices, shimmer and warmth", battery, one speaker | it sounds like strings on its own speaker, from battery, with nothing plugged in |
| J2 | Every key can sound at once | stated: "Polyphonic would be amazing" | all 25 keys sound together; incoming MIDI notes too, up to the voice count |
| J3 | Split, with each half's octave set separately | stated (settled): "octave select each half" | two octave controls; equal settings give one continuous keyboard; the split point is fixed between B and middle C |
| J4 | Each note responds to how hard it's struck | stated (settled): "innovate ... with velocity" | velocity acts **per note**; the concept says what velocity means (BOW: hard = fast bite; KEPT: the Solina's crescendo per note; TIDE: soft = longest, most wandering) |
| J5 | Lean into held notes; choose what leaning does | stated (settled): per-key pressure to explore, selectable destination | a pressure selector (swell · vibrato · tone · shimmer). The concept must still work if pressure ends up on one shared strip (then swell fills the whole instrument) |
| J6 | Shape each note's ending by how I lift | inferred (jam turns 3–5) | lift speed sets each note's tail within the release range. Firmware only; a fast lift is limited by the key's spring |
| J7 | Choose the tone colour, per half where it makes sense | inferred: every string machine has registers; the Solina split them by keyboard region | BOW: strands low · main · high per half. KEPT: bass · strings · brass, with bass on the left half only. TIDE: one tone knob |
| J8 | Choose and set the shimmer | stated (settled): analog mode plus Daisy modes | a mode choice (analog bucket-brigade ensemble or Daisy modes) and a depth; it can be turned fully off |
| J9 | Echo and reverb; MIDI tempo; tap tempo | stated (Big Energy rules carry over); tap inferred (Big Energy J27) | amounts while playing; echo syncs to MIDI clock; a tempo can be tapped with no clock; both at zero = dry. How sync is turned on and off is the concept's to show |
| J10 | Hold a chord or drone hands-free | inferred (pads, drones, the park, the split) | HOLD: a latching on/off. BOW and KEPT hold the left half; TIDE holds the whole keyboard |
| J11 | Speaker, and headphones that mute it | stated (settled) | one speaker; headphones mute it; stereo on headphones and outputs |
| J12 | MIDI with other gear | stated (settled): Big Energy's rules plus the split and velocity/pressure | USB-MIDI and TRS in and out; settings controllable; MIDI never flips switches; knob-only controls send nothing; MIDI split on/off (two channels / one); velocity and pressure out (poly aftertouch if per-key) |
| J13 | Read the whole state from the panel, by eye or touch | stated (no screens, no encoders); touch inferred (director's "eyes closed") | knob and tab positions are the state; the two octave pointers show the split (parallel = one keyboard); one status light with three meanings |
| J14 | Playing within seconds; know battery and charging | inferred | no tuning wait (the tones come from a crystal); battery low and charging shown on the status light |
| J15 | Park: bench, lap, sun, shade | inferred (Big Energy J22, "take this to the park") | it sits stable on a lap or bench; it's readable in sun; it lasts an afternoon (runtime from the power budget) |
| J16 | Many notes don't distort; one isn't thin | inferred | the fixed "breath" in every concept: loudness grows roughly with the square root of the keys held, recovering over ≈ 200 ms, no pitch sag, no control |
| J17 | Play in tune with others | inferred | a way to trim tuning, or a stated reason not to (open) |
| J18 | Share it with a friend | inferred (jam turn 1 draw, Big Energy J22g) | each half's controls sit over that half, so a second player has their own |
| J19 | One point of view; want to play it | stated (Big Energy J20, carried) | one idea drives the engine, the panel, the body and the keys |
| J20 | Same family as Big Energy | stated (settled): "a shared universe ... reuse as much as we can" | it uses a family body (CATHEDRAL, ONE SHEET or HUSH), the family's key strip, parts and construction; it says what changed and why |
| J21 | Build it himself; open it to fix | inferred (Big Energy J11, J14) | hand-buildable parts, or a plain statement where it isn't (e.g. if BOW's strands need an FPGA or CPLD); battery, a key and a firmware flash reachable without damage |

**Settled constraints every job lives inside:** 25 keys or fewer; no screens or encoders; real bought knobs and keys; battery powered; echo and reverb on the Daisy; no fixed budget, costed honestly.

## Flows

Each flow says which jobs it serves. Where the concepts differ, it says so.

### F1 Grab and play (J1, J14)
1. Take it out of the bag. Open the lid (BOW) or set it down (KEPT, TIDE).
2. Switch on. It's ready at once: no tuning. The status light goes steady.
3. Play a chord: strings sound from the speaker.
- **States:** steady = fine; slow pulse = charging; flashing = low battery. If the battery is too low to start, the light flashes and nothing sounds.

### F2 Make a split (J3, J13)
1. Both octave knobs are the same: one continuous keyboard (pointers parallel).
2. Turn the left octave down: the left half now plays lower. The pointers splay apart, and the difference between the numbers is the interval.
3. Play a low line with the left hand and chords with the right.
4. Turn them back to equal: one keyboard again.
- **Rule:** a note you're holding keeps its pitch when its half's octave changes. The next press uses the new octave.
- **Middle C** belongs to the right half. It's marked by the rim tick (visual, turn 6; director to rule).

### F3 Play expressively: strike, lean, lift (J4, J5, J6)
1. Strike: each note's attack follows how hard you struck it, inside the attack knob's range (what velocity *means* differs by concept).
2. Lean on a held key: the chosen pressure destination moves (per note for swell and vibrato; the whole instrument for tone and shimmer, following the hardest-pressed key).
3. Lift: a slow lift gives a long tail, a quick lift a short one, inside the release knob's range.
- **TIDE:** strike and lean set the note's future (how long it lasts, how far it drifts once held).

### F4 Choose what pressure does (J5)
1. Turn the pressure selector: swell · vibrato · tone · shimmer.
2. Lean into a held chord and hear it.
- **Shared-strip fallback:** the same selector. Swell fills the whole instrument instead of one note.

### F5 Set the colour (J7)
1. Turn tabs on or off (BOW: low · main · high for each half; KEPT: bass · strings · brass), or turn TONE (all concepts; TIDE has only that).
2. Set attack and release for the whole instrument.
- **States:** all tabs off = silence. The concept must decide whether that's allowed (and what the panel shows) or whether one tab always stays on.

### F6 Shimmer (J8)
1. Choose the mode: analog or a Daisy mode.
2. Turn depth up while a chord holds.
3. Depth to zero = dry.
- **States:** at full depth the analog mode hisses (bucket-brigade noise). The level is for eng to keep acceptable.

### F7 Echo and reverb (J9)
1. Turn the echo amount up; set the time, or tap a tempo.
2. With a MIDI clock present, the echo follows it. Nothing jumps or clicks when the clock starts, stops or drops out (Big Energy J26).
3. Turn the reverb up.
4. Both at zero = dry.

### F8 Hold a chord (J10)
1. Turn HOLD on. Play a chord in the held area (the left half in BOW and KEPT, anywhere in TIDE) and lift: it keeps sounding.
2. Play a new chord after every key is up: it replaces the old one.
3. Play with the other hand, or work the knobs.
4. Turn HOLD off: each note fades on its own tail.
- Held notes ignore per-note pressure (no finger on them); whole-instrument destinations still act on them.

### F9 Go private (J11)
1. Plug in headphones: the speaker goes quiet; stereo in the phones.
2. Unplug: the speaker comes back, at the volume knob's setting (no jump in level).

### F10 MIDI (J12)
1. **Play floss from a controller or a DAW:** notes come in on USB or TRS and sound; velocity and pressure in act as if played on the keys.
2. **Play other things from floss:** keys go out with velocity and pressure (poly aftertouch if per-key pressure works).
3. **MIDI split** (rear switch): on, left half = channel 1 and right half = channel 2; off, one channel.
4. **Settings by MIDI:** a MIDI message moves a setting. The knob no longer matches until it's turned (jump-on-move, as on Big Energy).
- **Open:** Big Energy showed "knob not in control" on its light. floss's light is cut to three meanings, so where this shows, if anywhere, is open.

### F11 Power (J14, J15)
1. Charge over USB; play while charging (slow pulse).
2. Low battery: the light flashes before it stops.
3. It can't switch on by itself in a bag.

### F12 Play in the park (J15, J1, J13)
1. Walk with it; sit on a bench or the grass.
2. Playing within a minute (F1).
3. Set it on a lap: stable; the speaker isn't muffled (TIDE: which way the radiator fires is for eng).
4. Read the panel in sun: positions are the state, so nothing depends on seeing a light.

### F13 Play together (J18)
1. A friend sits at the right side.
2. Each player sets their own half's octave and colour from the controls in front of them.
3. Shared controls (shimmer, echo, reverb, volume) stay in the middle or the far row.

### F14 Pack (J15, J20)
1. Switch off; close the lid (BOW) or bag it (KEPT, TIDE).
2. Knobs, keys and jacks survive a bag. Each concept says how (a lid, or a sleeve and its cost).

### F15 Build and fix (J21)
1. Build it from bought parts with hand soldering and Vector Space printing.
2. Open it from the back: battery, one key and a firmware flash reachable without damage.

## Open questions (carried)
1. **Eng:**
   - 25 per-key VCAs (cost, battery, board);
   - BOW's 75 tone outputs (FPGA / CPLD?);
   - lift timing against the spring's return;
   - the bucket-brigade part;
   - per-key pressure past the bottom of a key;
   - the sealed-box volume in each body.
2. **Concepts:** what "all tabs off" does; how echo sync is turned off; whether there's a tuning trim (J17).
3. **Owner (later):** a fixed breath vs "louder with every key"; whether an FPGA or CPLD is in scope to build; the 24-key fallback only if the rim tick fails.
