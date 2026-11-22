# floss: what BOW, KEPT and TIDE share (systems)

Status: **rev 1, 2026-11-22**, product designer (systems focus), concept round 1. Read with `../jobs.md`. Each concept's `how-it-works.md` states only where it departs from this file.

Marks: **[ENG]** an eng figure from the Big Energy records; **[CALC]** my arithmetic; **UNVERIFIED** a part or figure not yet checked; **PROPOSAL** systems design, not approved.

## 1. Engine: every key is a voice (structure B)

```
key Hall sensor ─► firmware ─► per-key envelope CV ─┐
MCU tone (per key) ──────────────────────────────────► per-key VCA ─► half bus L / R ─► registers / TONE ─► ensemble (analog BBD or Daisy mode) ─► Daisy echo + reverb ─► VOLUME ─► speaker / phones / line
```

- **One tone per key**, generated from a crystal. So it's in tune at power-on, with no tuning wait (J14). Octave per half is just arithmetic in the tone source (J3).
- **One small VCA per key** (25), each with its own firmware envelope. This is what makes velocity, pressure and lift act **per note** (J4–J6). Eng sizes the VCA (OTA pair per chip, ≈ 13 dual chips: **PROPOSAL**, cost and battery UNVERIFIED).
- **Two half buses.** Key outputs sum into a **left-half bus** and a **right-half bus**. That's what lets a half have its own registers (KEPT's bass, BOW's strands), lets a half be muted, and lets MIDI split route by half. The buses join before the ensemble.
- **Incoming MIDI notes** are assigned to the 25 VCA slots (oldest note first if all are busy), so MIDI can play pitches outside the keys' range.
- **The honest sentence (every concept):** floss's tones start in a microcontroller, one per key, the way the 1974 Solina's started in divider chips. Everything that shapes them is analog: each key's own amplifier, the register mix, the tone filter and the bucket-brigade ensemble. The Daisy modes, echo and reverb are digital, and each is a choice you can switch off.

## 2. Shared behaviours

### 2.1 The split = two OCTAVE knobs (J3, J13)
- **OCTAVE L** at the far left end of the panel, **OCTAVE R** at the far right end. Each is a **5-position stepped rotary, −2 · −1 · 0 · +1 · +2**, with a firm detent (visual's feel note). RS16211-class part, as Big Energy's TYPE switches (body height UNVERIFIED, as there).
- **At 0 / 0 the keys run C3 to C5, and the centre key is middle C (C4).** Left at −2 plays C1–B1 (contrabass territory); right at +2 plays C6–C7. [CALC]
- **Equal = one keyboard. Different = split.** The pointers read as parallel or apart; the difference between the numbers is the interval. No split mode, no split light.
- **The split point is fixed: B3 | C4.** Middle C belongs to the right half. It sits under the panel's centre gutter (visual turn 6), and a coral tick on the front rim marks the B|C edge.
- **Rule:** a held note keeps its pitch when its half's octave changes. The next press uses the new octave. Turning the knob while holding never makes a jump.

### 2.2 Strike, lean, lift: per-note articulation (J4, J5, J6)
- **Strike → attack.** Velocity (time between two Hall thresholds going down [ENG]) places each note's attack inside the range set by **ATTACK**. What velocity *means* differs by concept (BOW: speed; KEPT: loudness; TIDE: lifespan).
- **Lean → PRESSURE destination.** Per-key pressure, if eng proves it, acts on that key's note. Otherwise a shared strip acts on all.
- **Lift → tail.** Lift speed (time between two thresholds going up) places each note's release inside the range set by **RELEASE**. A slow lift = long tail; a quick lift = short. **Limit:** a lift faster than the Choc V2's spring return reads as "fastest", so the short end belongs to the spring [ENG test needed].
- **Held notes (HOLD, MIDI sustain)** have no finger on them: they use the knob values and ignore per-note pressure. Whole-instrument pressure destinations still act on them.

### 2.3 PRESSURE selector (J5)
- **4-way rotary.** BOW and KEPT: **swell · vibrato · tone · shimmer**. TIDE: **drift · swell · tone · shimmer**.
- **Per note:** swell (that note's level grows as you lean), vibrato (that note's pitch wavers), drift (TIDE: that note's wander, remembered when held).
- **Whole instrument:** tone (opens the TONE filter) and shimmer (raises the ensemble depth). Both follow the **hardest-pressed key**.
- **Shared-strip fallback:** the same four positions. Swell becomes FILL (the whole instrument swells), with the same label and the same feel under the hand. No panel change.
- **Rule:** pressure adds to the knob; it never goes below the knob's setting. Releasing pressure returns to exactly where the knob is.
- **Signal order:** the selector belongs to the **TOUCH group** (ATTACK, RELEASE, PRESSURE), the first stage, because the hand is where the signal starts.

### 2.4 The breath (J16)
- Fixed, no control: the summed level grows with about the square root of the number of keys sounding, not linearly. It recovers over ≈ 200 ms as keys lift. No pitch sag.
- So one note isn't thin and 25 don't clip. Owner question for later: does he miss "louder with every key"?

### 2.5 HOLD (J10)
- **A latching on/off.** It has a dot that's lit while on, and no armed state.
- While it's on, notes in HOLD's area keep sounding after you lift. Each concept defines the area and what a new chord does (BOW and KEPT: left half, new chord replaces; TIDE: whole keyboard, notes add up and a re-strike pulls one out).
- Off: every held note fades on its own tail.
- **MIDI sustain (CC 64)** holds every note, in every concept, whatever HOLD's area.

### 2.6 Register tabs and silence (settles "all tabs off")
- **A half with all its register tabs off is silent. That's allowed, and it's a feature:** muting a half. The tabs show it (all down), so there's nothing hidden.
- Use: mute the right half while the left holds a drone; give a friend the right half and turn yours off (J18).
- With MIDI split on, notes arriving on a muted half's channel are silent too, and the panel still shows why.
- TIDE has no tabs, so this doesn't arise there.

### 2.7 Echo, reverb, tempo (J9)
- Big Energy's settled answer (owner's option "B", `design/branches/echo-clock.md`): a **FREE / SYNC toggle by TIME**.
  - FREE: TIME is milliseconds; TAP sets a length.
  - SYNC: TIME picks a note division of the tempo. The tempo comes from MIDI clock if one is present (USB or TRS), otherwise from TAP.
- **Echo:** ECHO (amount), TIME, REPEATS, FREE / SYNC, TAP. **Reverb:** REVERB (amount); its decay grows with the amount (PROPOSAL, to save a knob; TIDE departs). Both at zero = dry.
- **TAP sits on the panel's axis** (Big Energy rev 7.1 precedent: "on the axis: it's shared").
- No jumps or clicks when the clock starts, stops or drops out (Big Energy J26).

### 2.8 Shimmer (J8)
- **SHIMMER**, a 4-way mode rotary: **analog** (the 3-path BBD ensemble: two LFOs ≈ 1 Hz and ≈ 6 Hz at 0 / 120 / 240°, per Sound on Sound) plus three Daisy modes.
  - Working functions for the Daisy modes: a wider many-voice ensemble; an octave-up glassy shimmer; a slow tape wobble.
  - Plain one-word names are visual's to test. TIDE defaults to analog.
- **DEPTH** sets how much. Fully left = no shimmer: a dry, still tone.
- **Stereo:** the three ensemble paths spread left / centre / right on phones and line. The speaker gets the mono sum (settled).
- **State:** at full depth, analog mode has audible BBD hiss. Eng sets the noise floor.

### 2.9 Status light (J13, J14)
- One light on the axis, with three meanings: **steady = fine**, **slow pulse = charging**, **flashing = low battery**.
- **"Knob not in control" (settled for floss): no indicator.** Settings moved by MIDI follow Big Energy's jump-on-move rule: the knob takes over the moment it's turned. You hear the takeover. The light keeps its three meanings, which the director asked for. If the owner misses Big Energy's indicator, the cheapest place for it is one short blink on the same light. I didn't take that because it makes four meanings.

### 2.10 MIDI (J12)
- Big Energy's rules: USB-MIDI and TRS in and out; settings controllable; MIDI never flips switches; knob-only controls send nothing; echo follows clock in SYNC.
- **MIDI SPLIT** is a slide switch on the rear wall (set-and-forget). On: the left half sends and receives channel 1, the right half channel 2. Off: one channel, with incoming notes landing by pitch.
- **Out:** note, velocity, pressure. Polyphonic aftertouch if per-key pressure is proven; otherwise channel pressure. Release velocity (lift speed) goes out too (MIDI note-off velocity), and incoming note-off velocity sets the tail.

### 2.11 Tuning (J17), settled
- **TUNE, a small trim on the rear wall**, ±50 cents with a centre detent. It's for an acoustic guitar in the park. Set it once and leave it; it doesn't earn a face slot. Also settable over MIDI (master tune).

### 2.12 Power, speaker, phones (J1, J11, J14)
- **Battery** (pack size from the power budget, once the VCA count and the shimmer are known). Charge over USB-C; play while charging.
- **Power:** BOW switches on with its lid (concept file). KEPT and TIDE use the family's recessed rear slide switch. None can switch on in a bag.
- **One speaker; headphones mute it.** On unplug, the speaker returns at VOLUME's setting.
- Passive radiator per body (concept files).

## 3. The panel grammar (structure, not looks)
- **Per-half controls sit over their half. Shared controls fill the rest, in signal order: TOUCH → registers → TONE → SHIMMER → ECHO → REVERB → VOLUME.** Amounts go nearest the hand, kinds and times behind (Big Energy's split rule).
- **The centre gutter** (one key wide, over middle C, x = axis ± 9) carries only shared, whole-instrument things: the status light, TAP, and in each concept its own centre item (BOW: strand names; TIDE: HOLD and DRIFT).
- **OCTAVE knobs sit at the two outer ends,** as far apart as the hands that use them.

## 4. Coverage of jobs common to all three
Every concept covers these through this file; the concept files cover the rest and any departures.

| Job | Where |
|---|---|
| J2 every key sounds | §1 (25 VCAs) |
| J3 split, octave per half | §2.1 |
| J4 / J5 / J6 strike, lean, lift | §2.2, §2.3 (velocity's meaning per concept) |
| J8 shimmer | §2.8 |
| J9 echo, reverb, tempo | §2.7 |
| J10 hold | §2.5 (area per concept) |
| J11 speaker, phones | §2.12 |
| J12 MIDI | §2.10 |
| J13 read the state | §2.1, §2.6, §2.9, §3 |
| J14 instant start, battery | §1, §2.9, §2.12 |
| J16 many notes vs one | §2.4 |
| J17 tuning | §2.11 |

## 5. Open, for eng
1. 25 per-key VCAs: part, cost, current, board area.
2. Lift timing at the Choc V2's spring return (one test key).
3. Per-key pressure past the bottom of the key (FSR per key under a felt collar?). The fallback is a shared strip (Big Energy's floating strip C).
4. Three BBD paths: part and noise.
5. Mux count for about 17–22 panel controls plus 25 Hall sensors.
