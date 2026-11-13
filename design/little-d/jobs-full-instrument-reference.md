# Jobs and flows: the instrument's physical form

**Sources:**
- the owner's words (owner.md, quoted where it matters)
- jam.md (closed after director Turn 6)
- eng/architecture.md (zero-cal, I/O), **superseded where they differ by eng/architecture-v2.md** (round 2: boards A–D, modules, pouch cells, MIDI scope §2)

**Marks:**
- **stated** = the owner said it
- **inferred** = we derived it; the reason is given

Later rounds walk every job here against each concept and against the build.

## Jobs

| # | Job | Source |
|---|---|---|
| J1 | **Play notes on keys that feel like an instrument**: real travel, a lever action, silent, no click. They don't have to be a traditional keybed. | stated: "keys would be amazing, but they don't have to be like a trad keybed"; "i dont think click would make sense… i want it to feel like an instrument" |
| J2 | **Shape the sound live** with one control per function, reachable while the other hand plays. | stated (a Model D clone); "while playing" is inferred |
| J3 | **Carry it anywhere, and play it with no table, mains or cables** (lap, couch, desk). | stated: "completely portable"; lap/couch is inferred |
| J4 | **Run on battery, recharge it, play while charging, and know the charge.** | stated (battery); the rest is inferred |
| J5 | **Hear it from a built-in speaker, and from headphones and line out.** | stated: "built in speaker would be incredible but it needs outs" |
| J6 | **Build it**: one variant, hand-soldered through-hole boards plus plug-in ready-made modules, enclosure included, "IKEA"-simple. | stated. Round-2 update from owner.md 2026-11-12 ("let's use readymade modules"), which overtook the two-variant wording |
| J7 | **Get the enclosure made**: laser-cut, CNC'd or printed at Vector Space, or ordered. | stated: "i can 3d print one, or we could order one"; makerspace answer |
| J8 | **Stay in tune with no rigmarole**, and know that it worked or what failed. | stated: "not interested in a bunch of testing" |
| J9 | **Bend pitch and add modulation** with performance controls beside the keys. | inferred: core to playing a Model D |
| J10 | **Glide and play legato** with Model D semantics (lowest-note priority, single trigger). | inferred |
| J11 | **Run external audio through the filter** (EXT IN to the mixer), including eurorack-level sources. | stated: "pass things into the filters and whatnot" |
| J12 | **Play it from MIDI**: notes, bend, mod, hold. USB and TRS. | stated: "control via midi". **Round-2 risk:** eng v2 §2 keeps the mod wheel as an analog pot, so incoming CC1 can't set mod depth unless eng accepts E1 (common §2) |
| J13 | **Control its parameters from MIDI** (the 11 continuous controls in eng v2 §2), **and send its keys, knobs and wheels out as MIDI** (knob-only controls send CC only with dual-gang pots: owner question, common §4). | stated: "controlling it in midi is good… i'd want to use the knobs to control the midi" |
| J14 | **Knob vs MIDI: the last one touched wins.** A MIDI value holds until the knob physically moves, then the knob's value takes over (jump-on-move). No motorised knobs, no recall, no screens, no endless encoders. **Know which knobs aren't in control, and take control back.** | stated (behaviour; no encoders or screens confirmed). "Know / take back" is inferred. The indicator light is **open**: the owner is "not sold either way but its not a bad idea" |
| J15 | **Patch it with the eurorack**: pitch/gate in and out, filter CV in, loudness CV in. | inferred from "and whatnot" plus his eurorack. Eng's default includes them. **Scope question** |
| J16 | **Protect it in a bag**: knobs, faders, keys and jacks survive being carried. | inferred from J3 |
| J17 | **Open it to service it or swap the battery** without destroying the enclosure. | inferred: kit serviceability |
| J18 | **Hold or drone a sound hands-free** (HOLD replaces A-440). | inferred; director-approved |
| J19 | **Find the main controls and keys without looking**, in a dim room. | inferred from the director's "works in the dark" test |

### The control inventory every concept must place

Counted from eng §8 and the director's common spec. **The owner said "~30".
The honest count is about 46.**

| Group | Controls | Count |
|---|---|---|
| Performance strip (left) | CUTOFF (hero), EMPHASIS, CONTOUR AMOUNT, GLIDE | 4 pots |
| Controllers | TUNE, MOD MIX; switches OSC MOD, FILTER MOD, OSC 3 CTRL, GLIDE on | 2 pots, 4 toggles |
| Oscillators | RANGE ×3 (rotary, MCU-read), WAVE ×3 (rotary), FREQ 2, FREQ 3 | 6 rotary, 2 pots |
| Mixer | levels OSC1/2/3/EXT/NOISE; on/off ×5; WHITE/PINK; EXT LINE/MOD pad; FEEDBACK | 5 pots, 8 toggles |
| Filter contour | ATTACK, DECAY, SUSTAIN; switches KBD CTRL 1, KBD CTRL 2 | 3 faders, 2 toggles |
| Loudness contour | ATTACK, DECAY, SUSTAIN; switch DECAY | 3 faders, 1 toggle |
| Output | VOLUME, PHONES VOLUME | 2 pots |
| System | TUNE button, HOLD button, one RGB status LED, optional "not in control" light (J14, open), master switch (on the I/O edge) | 2 buttons, 1–2 LEDs, 1 switch |
| Performance | PITCH wheel (spring-centred), MOD wheel | 2 wheels |
| I/O edge | PHONES, LINE OUT, EXT IN, FILTER CV IN, LOUDNESS CV IN, PITCH CV IN, GATE IN, PITCH OUT, GATE OUT, MIDI IN (TRS-A), MIDI OUT (TRS-A), USB-C | Round 2: eng v2 §4.1 puts ≈ 16 jacks at a 14 mm pitch (≈ 225 mm) on board A's back edge, plus **one** USB-C (common §3, E3): ≈ 260 mm |

## Flows

Each flow lists its steps and the controls used. **States** are at the end.

**F1. Open and play** (J1, J2, J3, J8)
1. Open the carry state. Each concept has its own action: the lid, the module or the dish.
2. The lid Hall sensor sees "open", and the unit wakes: the ±10 V rails come
   up and the keys calibrate their rest positions.
3. The power-on tune runs (about 2–4 s). The LED breathes while it tunes, and
   the oscillators can be heard converging if audible boot is on.
4. The LED goes steady (ready). The panel is the patch, and every parameter
   is owned by its knob.
5. Play the keys. The sound comes from the speaker unless an output is
   plugged in.
- **Quiet boot:** hold TUNE while opening. The tune runs muted.

**F2. Shape while playing** (J2, J9, J10, J19)
1. The right hand plays the keys.
2. The left hand rides the performance strip (CUTOFF, EMPHASIS, CONTOUR
   AMOUNT, GLIDE) and the wheels just below or beside it.
3. The other controls are reached between phrases, in signal-flow order.
4. The hero cutoff cap and the strip are findable by touch, and the glow
   pointers show in the dark.

**F3. Stay in tune** (J8)
1. Background re-tune runs while you play (eng §3.1; owner Q9 pending).
2. A big temperature change triggers an automatic re-cal *between notes only*.
3. Press TUNE to force a full tune, about 2–4 s, with the LED breathing.
4. **Failure:** the LED blinks the number of the oscillator that's missing
   (1, 2 or 3), or "F" for the filter. Doubles as the kit self-test (F11).

**F4. Pack away** (J3, J16)
1. Close: lid down, module flipped on, or dish stowed.
2. The Hall sensor sees "closed": all notes off, the speaker mutes, the rails
   turn off, and the MCU deep-sleeps.
3. Carry it. Knobs, faders and keys are covered, and no shaft takes a side load.
- There's no switch to remember. The master switch is only for storage and
  shipping.

**F5. Charge** (J4)
1. Plug in USB-C. The charge LED shows charging.
2. Play during charging works on a USB-C charger. A plain 500 mA port
   drains slowly (eng §4.3).
3. Fully charged: the charge LED shows full.
- Battery check: tap TUNE + HOLD together. The status LED shows the charge
  as a colour (green, amber, red).

**F6. Listen** (J5)
1. Speaker by default.
2. Plug in phones and/or line out: any plugged output mutes the speaker,
   read by the switched jack.
3. VOLUME sets the speaker and line. PHONES VOLUME sets the headphones.
4. "Speaker as monitor": long-press HOLD with line out plugged in, which
   un-mutes the speaker (eng §5).

**F7. External audio through the filter** (J11)
1. Patch Plaits or Rings into EXT IN, with the LINE/MOD pad on MOD for eurorack level.
2. Turn the mixer's EXT level up, and its switch on.
3. Shape it with cutoff, emphasis and the contours. The keys gate the loudness contour (or use HOLD).
- **FEEDBACK:** the switch normals LOW out into EXT IN when the jack is
  empty. A plugged cable breaks that normal.

**F8. Play from MIDI** (J12)
1. Connect the Maschine+ via TRS MIDI IN, or a computer via USB-C.
2. It follows notes (lowest-note priority, single trigger), bend, mod (CC1)
   and hold (CC64).
3. MIDI activity shows as a blink on the status LED.
- The keys still work alongside MIDI. Both feed one note list.

**F9. MIDI parameter control, knob takeover and reclaim** (J13, J14)
1. Incoming CC for a parameter: that parameter is now **owned by MIDI** and
   uses the CC value. The knob doesn't move.
2. Optionally, the "not in control" light lights while any MIDI-owned
   parameter differs from its knob (open; see the concepts).
3. Move that knob past its deadband: the parameter **jumps** to the knob's
   value and is owned by the knob again. The knob sends CC out.
4. **Reclaim all:** hold HOLD and press TUNE. Every parameter goes back to
   its knob, and the panel is the patch again. MIDI "Reset All Controllers"
   (CC121) does the same. Sleeping and waking also resets to the knobs.
5. Knobs and faders always send CC on movement. Keys send notes, and wheels
   send bend and CC1 (MIDI OUT, TRS and USB).

**F10. Patch with the eurorack** (J15)
1. Pitch out and gate out drive eurorack voices from the keys.
2. Pitch in and gate in let a eurorack sequencer play it, with 1 V/oct read
   digitally and auto-calibrated (eng §5b).
3. Filter CV in and loudness CV in take eurorack modulation, analog and
   audio-rate capable.

**F11. Build the kit** (J6, J7, J8)
1. Solder boards A, B, C and D (all through-hole). Plug the ready-made
   modules into board D's sockets (eng v2 §4.1). Round-2 update.
2. Assemble the keyboard: the key board with its sensors, then the Delrin
   key comb with magnets, the clamp bar, the felt stop and the key tops.
3. Stack the enclosure layers in numbered order, then drop in the boards.
4. The panel PCB goes over the shafts: pot nuts and fader screws.
5. Pouch cells plugged in, base plate on, master switch on, open it up.
6. **Self-test = the first tune.** Steady LED means it works. A blink count
   names the missing oscillator or the filter.
- No meter, no scope, no trimmers.

**F12. Service and battery swap** (J17)
1. Master switch off. Remove the base plate (4 screws or fewer).
2. The batteries come out of their holder without tools. The boards come
   out after the panel nuts.

**F13. Hold or drone** (J18)
1. Play a note and press HOLD: the gate latches.
2. Both hands are free for the panel.
3. Press HOLD again, or play a new note to latch it instead. Closing the lid
   always releases it.

## States the hardware must show

| State | Shown by |
|---|---|
| master off / asleep (closed) | everything dark |
| waking / tuning | status LED breathing |
| ready | status LED steady (signal colour) |
| tune failed | status LED blinks the oscillator number, or "F" for the filter |
| MIDI activity | a short blink per message group |
| hold latched | the HOLD button lit, or the status LED holds a second colour (concepts decide) |
| low battery | the status LED pulses red every 10 s; below a critical level the unit sleeps |
| charging / full | charge LED by the USB-C |
| battery level (on request) | TUNE + HOLD tap, then a colour |
| a parameter owned by MIDI and differing from its knob | optional "not in control" light (J14, open) |
| no keyboard surface (DOCK only) | round 2: DOCK is power-by-dock, so module away = off |
| dish link lost (DISH only) | status LED "dish lost" blink; the dish controls hold their last values |
| speaker muted by a plugged output | none needed (physical cause is visible) |
