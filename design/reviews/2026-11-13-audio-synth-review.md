# Audio / synth review — the whole instrument, plus §15 stereo and pan (2026-11-13)

Independent critic, audio engineer / synth designer hat. Reports to the owner; decides nothing.
Read: `design/owner.md`, `HANDOFF.md`, `eng/budget-variant.md`, `eng/daisy-first-principles.md`, `eng/single-chip-research.md`, `eng/aftertouch.md`, `eng/effects.md`, `design/branches/echo-clock.md`, `design/branches/concepts/cathedral/how-it-works.md` (including the §15.5 "two pans" draft that appeared while I was reviewing), `versions/v1.1/common-how-it-works.md`. No web checks were needed; nothing below depends on a datasheet figure I didn't already have from the files. Items I reasoned out but couldn't confirm against a part or a bench are marked **UNVERIFIED**.

Severity: **MUST** = will break, sound wrong or contradict itself if built as written. **SHOULD** = will surprise a player or cost you later. **NICE** = worth doing.

---

## Score

| What | Score | Based on |
|---|---|---|
| **The instrument as specified (voice, control, MIDI, power, FX)** | **6 / 10** | eng spec (budget-variant rev 14, daisy-first-principles §0–§9, aftertouch), echo-clock option B, v1.1 common panel, cathedral §10 keys and §15 |
| §15 stereo outputs + mono sensing + pans, as drafted | 5 / 10 | cathedral §15.1–§15.5 |

The core is genuinely good: a faithful Model D voice, a dry path that is analog and never switched, a wet-only return (the right call, no comb filtering), coarse + fine pitch DACs with the TIM5 closed loop, filter calibration on the spare codec input, and a FREE / SYNC behaviour table that already handles clock loss, STOP and two transports. That's a 9 voice. It's held at 6 by a set of fixable holes: the control scanner is already full and four new controls were added on top, one stereo circuit can't work as written, PARA+4 has no way to be heard, and a few gestures and parts contradict each other. Fix the MUST items and this is an 8.

---

## Gotchas and nonsense, most important first

### 1. The mux is full, and four or more new controls were added on top — MUST
- **What:** `aftertouch.md` §2 counts the three 16-channel muxes at **48 / 48, 0 spare** after aftertouch. Since then: PARA toggle (+1), FREE / SYNC (+1), FX PAN / VOICE PAN (+1), ECHO PAN (+1), the TS-sense line on LINE OUT (+1), and OSC 3 CTL, which the firmware has to read (item 11, +1). That's **≈ 54 of 48**. `echo-clock.md` §4 says "46 / 48" and cathedral §15.4 says "eng to confirm": both use stale counts.
- **Why it matters:** no free channel means no FREE / SYNC, no pan and no PARA, or a board respin.
- **Fix:** add a **4th CD74HC4067** sharing S0–S3 (≈ $0.60, +16 channels). Put it on **D20 (PC1, ADC3)** and move the battery divider onto one of its channels. ADC3 then converts two channels per step (mux C and mux D). That keeps the key ADCs (1 + 2) untouched and leaves D16 free as the last spare. (Running two ranks on ADC3 is standard STM32 practice, but eng should confirm the timing inside the 3 µs step: **UNVERIFIED**.) Then recount every channel in one table.

### 2. The TS-cable sensing on LINE OUT (§15.4) can't work as drawn, and the obvious repair thumps — MUST
- **What:** the ring is driven by an op-amp through ≈ 100 Ω, and a 1 MΩ pull-up to 3.3 V is meant to read "≈ 3.3 V with an empty jack". But a 100 Ω source holds the ring at the op-amp's DC level (≈ 0 V); the pull-up moves it by about 0.3 mV. **It reads "TS" all the time.** It only works with a series coupling cap between driver and jack. Then that cap sits charged to 3.3 V, and plugging a TRS cable into a mixer dumps a **3.3 V step into the mixer's right input**, louder than line level. That's a thump on every plug-in.
- **Second problem:** with a TS plug the ring is shorted to the sleeve while the right driver keeps driving it (the dry voice is analog in both summing nodes, so muting the Daisy's wet R doesn't silence it). Through 100 Ω a TL072 sits in current limit. That's distortion, ground current shared with the tip's return (crosstalk and noise on the mono signal), and wasted battery.
- **Fixes (pick one):**
  - **(a) Most reliable: two jacks, L / MONO and R** (the standard synth convention). The R jack's switch normals R into L's summing node when nothing is in R. Analog, no firmware, no pops. It adds one hole on the far wall. That's your call against "no new jacks", but it isn't a patch point.
  - (b) Keep one TRS jack, but bias the ring at ≤ 50–100 mV (not 3.3 V) so the plug-in step is ≈ 30 dB smaller. Use ≥ 470 Ω–1 kΩ build-out resistors on both line outputs. When TS is sensed, **cut the R driver** with the 74HC4053 (which also handles the mono sum). Bench it: **UNVERIFIED**.
  - Either way, line outputs want **≈ 470 Ω–1 kΩ** series resistance, not 100 Ω. Line inputs are ≥ 10 kΩ, so nothing is lost.

### 3. A stereo TRS line out into a balanced input goes nearly silent — SHOULD
- **What:** most audio interfaces and mixers take **balanced TRS** on their line inputs. A 3.5 mm TRS → 1/4" TRS cable sends L to hot and R to cold. The input hears **L − R**. The dry voice is identical in both channels, so it **cancels completely**; only the stereo differences in the effects remain. Even a firmware "mono" mode (L = R) gives total silence. The TS sensing can't detect this case: the ring isn't grounded.
- **Why it matters:** "I plugged it into my interface and only hear a thin reverb" is the first support call every stereo-mini-jack synth gets.
- **Fix:** print "stereo · unbalanced" by the jack. Put a **3.5 mm TRS → 2 × TS (Y) cable** in the build list and the manual. Fix (a) in item 2 avoids this problem completely.

### 4. PARA+4's digital 4th oscillator has no audio path — MUST
- **What:** the owner approved "PARA+4 uses the Daisy's digital 4th osc". But both codec outputs are now the **stereo wet return**, which enters **after** the VCA and the filter. No eng file specifies a route for a Daisy oscillator into the analog mixer and ladder. As things stand, a 4th note would bypass the filter and envelope, or steal a wet channel (and stereo with it).
- **Fix (decide one):**
  - (a) Route the 4th oscillator through **codec OUT R into the NOISE / EXT input**, with SOURCE on EXT, so the real ladder filters it. The wet return then goes mono while PARA+4 is on. Say so on the panel or in the manual.
  - (b) Use the Seed's internal DAC. Both channels are already taken (velocity, mod depth), so this needs a re-plan.
  - (c) Drop PARA+4 to PARA until the path exists. The toggle's third position would then do nothing, so pick a 2-way or relabel.

### 5. The peg-key necks and the floating key strip fight each other — MUST
- **What:** for aftertouch, strip C floats and "can shift ±0.5 mm". Aftertouch §8.4 requires **≥ 1 mm clearance** around key tops, and "nothing in the shell may touch strip C or the keys". Cathedral §10.2 gives the peg neck a deck hole of **Ø 12.0 around an Ø 11.2 neck: 0.4 mm a side**.
- **Why it matters:** the necks will rub the deck. That steals force from the pressure lanes (aftertouch reads low and differs key to key), adds friction that changes velocity, and will squeak.
- **Fix:** deck hole ≥ **Ø 13.2** (neck + 2 × 1.0), or slim the neck. Check that the 12.7 head still covers the larger hole (it doesn't: Ø 13.2 > 12.7, so a dark ring shows). Alternatively, centre the strip with a positive locator that doesn't carry vertical load.

### 6. TAP gestures collide; one could drop you into the bootloader — MUST (DFU) / SHOULD (the rest)
- **What:**
  - DFP §2.3 says "hold TAP at power-on" triggers a full autotune re-sweep. §5.3 uses a "TAP-at-power-on gesture" for **reset-to-bootloader (DFU)**. **Same gesture, two very different results.**
  - "Hold TAP" also queries the battery (§7.3).
  - "EMPHASIS full + hold TAP" runs the filter calibration. EMPHASIS fully up is a normal playing position (self-oscillating filter). Holding TAP to check the battery while playing that patch would start a filter cal mid-song.
  - Velocity curve and aftertouch span settings are also "hold-TAP combinations".
  - In SYNC, TAP is also played in rhythm.
- **Fix:**
  - Give DFU a gesture nobody does by accident: e.g. hold TAP **and** move the bend stick to the top at power-on, or use the Seed's internal BOOT button behind the service panel.
  - Keep autotune on "hold TAP at power-on".
  - Make filter cal a power-on gesture too (EMPHASIS full + hold TAP **at power-on**), not a live one.
  - Battery query: double-tap-and-hold, or show it on the status light at boot.

### 7. Pops: phones and line are unmuted at power-on, power-off and during the boot VCA null — SHOULD
- **What:** only the speaker has a mute (LM386 enable, sequenced by the Daisy). The new stereo headphone driver and line drivers run from the ±9 V rails, which ramp up through the MC34063s. The boot routine also **deliberately steps the VCA's CV** to null its thump (DFP §2.2). All of that reaches phones and line.
- **Why it matters:** a loud thump in headphones at every power-on, and into a mixer or PA.
- **Fix:** a shunt mute (2 small-signal BJTs or a 4053 section) on phones L / R and line L / R, held muted by a pull-down at reset, released by the Daisy after boot calibration plus ≈ 200 ms. Use the same control as the LM386 enable. Mute again on the low-battery cut. Cost ≈ $0.30.

### 8. The "gate-aware" FX input mute will chop release tails — SHOULD
- **What:** DFP §6.2 mutes the effects input when no gate is on, to keep the codec's noise out. But the loudness contour's decay and release are **analog pots the Daisy doesn't read**. After the key lifts, the dry note keeps sounding; the send closes at gate-off, so the echo of that tail is missing, and the reverb on a plucked note cuts short.
- **Fix:** gate the send on **signal level** at codec IN L (which it already samples): open on gate or signal > threshold, hold ≈ 300 ms after the signal falls below −60 dBFS, then fade over ≈ 20 ms. No new parts.

### 9. PITCH CV OUT has no DAC channel — SHOULD
- **What:** the jack is in the locked I/O ("PITCH CV out, GATE out, FILTER CV in"). The rev 0 spec gave it an MCP4822 channel. In DFP §4.3 all eight MCP4822 channels are assigned (coarse + fine × 3, keytrack, CUTOFF) and the pitch out isn't mentioned.
- **Fix:** share the **keytrack channel** (MCP #4 A), buffered and scaled to 1 V/oct ahead of the KBD CTRL toggle. Define:
  - whether it includes glide and bend (it should);
  - which note it carries in PARA (lowest, matching low-note priority);
  - its resolution: ≈ 1.2–1.5 cents per step over a 5 V span (**[CALC]**). That's fine for notes, slightly steppy on slow glides into another synth.

### 10. Ghost parts and conflicting pin tables — SHOULD
- **What:**
  - Cathedral §15.4 drives the 74HC4053 from "1 GPIO via the 74HC595 latch". There is **no 595** in the Daisy design (DFP §0: "74HC595 / expander: not needed").
  - `budget-variant.md` §v1.11.6 still lists the sensor-LDO enable on D23 and the LM386 enable on D22. DFP §9 makes **D22 / D23 the Seed's DAC outputs** (mod depth, velocity) and moves those enables to D18 / D12.
  - DFP §3.2's mux layout overcounts by 2 (aftertouch §2 says so).
- **Why it matters:** if someone captures the schematic from budget-variant, the LDO enable lands on a DAC pin.
- **Fix:** mark §v1.11.6 superseded by DFP §9. For the 4053, use D29 or D30 (free under USB plan U1). Publish one corrected pin and mux table (with item 1).

### 11. OSC 3 CONTROL has to be read by the firmware, and it isn't — SHOULD
- **What:** VCO 3's pitch is now entirely digital: RANGE 3, FREQ 3, the key note, glide, bend and drift are summed in firmware into one coarse + fine DAC pair. So "keyboard off" can only happen in firmware. An analog toggle can't remove the key note from a DAC value without also killing RANGE 3 and FREQ 3, which you need to set the LFO rate. PARA also needs to know whether osc 3 is a voice or the LFO. The toggle isn't in any mux list.
- **Fix:** read OSC 3 CTL on a mux channel (counted in item 1). In LFO mode, firmware drops the key note, bend and glide from VCO 3 and excludes osc 3 from PARA allocation.

### 12. KEYBOARD CONTROL can't reach full tracking — SHOULD
- **What:** budget-variant §v1.2 gives the filter keytrack toggle "off / ⅓ / ⅔". The Model D has two switches (⅓ and ⅔) that together give **full**. Full tracking is what makes a self-oscillating filter playable as a fourth, in-tune sine voice: a classic Model D move, and the automatic filter-scale cal exists precisely to make it accurate.
- **Fix:** relabel and re-resistor the 3-way as **off / ½ / full** (or ⅔ / full). Same part, two resistor values.

### 13. RANGE knobs have "firmware detents" but no physical ones — SHOULD
- **What:** RANGE × 3 are plain pots mapped to 6 zones. A player can't feel 16' from 8'. In the dark, or outdoors, you will land between zones and be an octave off. With jump-on-move from MIDI, the knob can point at 8' while 2' sounds.
- **Fix:** use the same RS16211 rotary as WAVE (6 positions, stop) on a resistor ladder into the same mux channel: ≈ +$1.21 × 3, 0 pins. Drop RANGE from the MIDI-controllable set (it's a switch now: "MIDI never flips switches").

### 14. MIDI echo from a DAW will knock knobs out of control — SHOULD
- **What:** marked knobs **send** their CC when moved. Most DAWs echo incoming MIDI back out to the instrument (MIDI thru / track monitoring). Per the jump-on-move rule, an incoming CC puts the knob "not in control" and lights the LED. So every knob you turn hands itself to MIDI, has to move 1.5 % to take back control, and steps. No **local off** is specified either, so notes double through the DAW.
- **Fix:**
  - Ignore an incoming CC that matches what this knob sent in the last ≈ 200 ms.
  - Add a **local off** setting (a hold-TAP combination or a CC 122 receive).
  - Optionally add "receive CC only on channel X".

### 15. CC 10 is the wrong number for VOICE / FX PAN — SHOULD
- **What:** CC 10 is the standard channel pan. Many DAWs send CC 10 = 64 (and CC 7) when a project loads or on a reset, which grabs the knob without the player touching it. Sending CC 10 out when the knob moves will pan the next synth on TRS out, or the DAW track itself.
- **Fix:** use an undefined CC, as already proposed for ECHO PAN (CC 102). For example, CC 103 for VOICE PAN, or drop VOICE PAN (§15 section below).

### 16. Plugging in phones may no longer mute the speaker; LINE OUT's effect on the speaker is undefined — SHOULD
- **What:** rev 0 used a switched phones jack to mute the speaker. §15.4 suggests a plain TRS PCB jack ("switches aren't needed") as "the same part as PHONES" (**UNVERIFIED** part). Nothing says whether plugging into LINE OUT mutes the speaker. Into a PA, a live speaker can feed back through a vocal mic.
- **Fix:** use a **switched** TRS jack for PHONES (its switch tells the Daisy, or cuts the LM386 input). Decide LINE OUT: mute the speaker or not (most players expect yes). Only one switched jack needs to tell the Daisy.

### 17. Ground loop and switcher noise when USB and LINE OUT go to the same computer — SHOULD (UNVERIFIED)
- **What:** USB-MIDI from a laptop plus line out into that laptop's interface is a classic ground loop. The MC34063 switchers (≈ 30–100 kHz) and the boost add whine on the shared ground.
- **Fix:** mention it in the manual (run on battery, or use a USB isolator while recording). Keep the line-out ground return at the analog star. Leave footprints for a ferrite on the USB shield/ground.

### 18. Paraphonic mode surprises a player — SHOULD (behaviour to define, mostly docs)
- The mixer levels are analog pots the firmware can't see. **A note allocated to an oscillator that's turned down is silent**, so chords lose notes depending on knob positions.
- "RANGE kept" plus per-oscillator WAVE means each note of a chord can play in a different octave and a different waveform, depending on which oscillator it lands on.
- OSC MOD on in PARA means FM between chord notes: clangy.
- Shared single-trigger envelopes mean a note added late to a decayed chord (SUSTAIN at 0) is silent.
- Velocity in PARA re-scales the whole chord's loudness on each new note.
- **Fix:**
  - In PARA, firmware uses **RANGE 1 for all oscillators** (RANGE 2 / 3 ignored), and retriggers the contours on each new note-on.
  - The manual says "set OSC 1–3 levels equal for chords".
  - Exclude osc 3 when OSC 3 CTL is off (item 11).

### 19. Runaway feedback and shimmer can clip the codec — NICE
- TAPE REPEATS "to controlled runaway" into a long HALL or SHIMMER builds level fast. Add a soft limiter on the wet bus before the DAC (firmware), and a **≈ 60–80 Hz high-pass on the send**. That removes VCA thump residue and low-end mud from repeats and the reverb.

### 20. The speaker will be quiet in a park, and its draw isn't in the power budget — NICE / SHOULD
- An LM386 on 5 V into a 50–60 mm driver gives a few hundred mW at best (**UNVERIFIED** at this load). The grille open area is down 35–40 % (cathedral §14). The power table carries "LM386, mux, DACs, MIDI, LEDs ≈ 0.07–0.35 W", but loud speaker playback alone is likely ≈ 0.5–0.8 W at the 5 V rail **[ENG]**, against an already thin 1 A boost.
- Count it. Consider the PAM8302 class-D module (ready-made, rev 0 priced it at $3.95): it's more efficient and louder. Bench the loudness with the real grille before the lid is fixed.

### 21. Smaller items — NICE
- **SOURCE "feedback":** say where it's tapped. It should be the **dry VCA out, pre-FX and pre-VOLUME**. If it's taken after the output mixer, the digital wet and its latency enter the ladder loop and the feedback changes with VOLUME and the pans.
- **Velocity → FILT** is a step added to the CUTOFF CV at note-on. On legato or overlapping notes that's an audible jump in the previous tail. Slew it ≈ 2–5 ms.
- **Bend:** range not specified (suggest ±2 semitones, settable), and pitch bend in / out over MIDI isn't stated.
- **FOLD hinge ribbon:** stereo adds wet R, VOLUME's second gang, a line R driver, the sense line and a mute line. Recount the ribbon pins.
- **Low battery:** "at 3.3 V mutes the FX". Fade them over ≈ 2 s instead; a sudden dry room mid-song sounds like a fault.
- **Reach:** in layout B, REPEATS and VOLUME sit on the lid's top row. When a TAPE echo runs away, you want both under your hand. A player's note, not a rule.
- **Dual-gang 9 mm VOLUME:** cheap gangs mis-track at low settings, which shifts the stereo image. It's fine as a known trade; the part in T18 is **UNVERIFIED**.
- **Headphone driver** draws quiescent current all the time, not "only with phones in", unless it's switched.

---

## §15 stereo and the pan redesign ("pan the delay into the reverb separately from the dry signal… and sync that")

The §15.5 draft (two pans, ECHO PAN becomes a synced auto-pan when FREE / SYNC is on "sync") is a reasonable first reading. As a player and DSP designer I see these problems:

**P1. One of the two pans will barely be heard — SHOULD.** TAPE, BBD and CLEAN are mono delay lines, so whatever VOICE PAN does to the echo's input is summed away, and ECHO PAN then decides where the repeats sit. VOICE PAN is left placing the voice's direct send into the reverb. A reverb smears its input position (a plate or spring heavily so), so on most settings VOICE PAN moves almost nothing. A knob that seems to do nothing is worse than no knob.
→ **Drop VOICE PAN.** The voice enters both effects centred. Use the freed slot to bring **TAP back into the FX row**, where it belongs with FREE / SYNC and TIME.

**P2. An auto-pan whose rate equals the echo division lands the repeats wherever your note happened to start — SHOULD.** With the pan swinging once per two repeats, repeat k sits at ±sin(φ₀), where φ₀ is the swing's phase when you played the note. Play on the swing's zero-crossing and every repeat sits in the **centre**; play a quarter-cycle later and they alternate hard left and right. So the effect depends on timing you can't hear or see.
→ Do the movement **per pass, inside the feedback loop**: each repeat steps to the mirror position of the last one, starting from the knob's side. That's deterministic, always in time (it rides the echo's own clock, synced or free), and gives exactly the "delay bouncing across, blooming into the reverb" result.

**P3. It collides with the PING-PONG type — MUST (define it).** PING-PONG already alternates sides every repeat. Add an auto-pan that also flips every repeat and the two cancel: **all repeats land on one side.**
→ Pick one meaning:
- **Recommended:** the movement *is* PING-PONG. In PING-PONG, ECHO PAN sets the start side and the width. In TAPE / BBD / CLEAN, ECHO PAN is a still position.
- This needs **no switch and no FREE / SYNC coupling**. The movement is synced whenever TIME is synced (to clock or TAP) and free when TIME is free. The owner gets "panned delay into the reverb" (any type) and "moving delay in time" (PING-PONG) from **one knob**.
- Cost: movement comes with PING-PONG's clean voicing. A firmware option could give PING-PONG the tape wear (darkening, wow) so a moving tape echo exists too: **NICE**.

**P4. Riding FREE / SYNC couples two unrelated decisions — SHOULD.** Under the draft, a synced echo can't sit still off to one side (the most common dub use: echo on the left, voice in the middle), and in the park in FREE mode you can't get movement. Flipping FREE / SYNC also silently changes what the pan knob does. That's the hidden-mode problem echo-clock.md §3 rejected option A for.
→ P3's mapping removes the coupling. If the owner really wants a slow, sweeping auto-pan (a bar-length LFO, not per repeat), that's a different effect and honestly needs its own STILL / MOVE toggle. That toggle needs the 4th mux (item 1) and a slot.

**P5. A constant-sum law makes a moving pan pulse on headphones — NICE.** Constant sum (−6 dB at centre) is right for a *static* pan heard on the mono speaker. A pan that moves dips about 3 dB in power each time it crosses the centre: a tremolo at twice the pan rate on phones. With P2's stepped repeats, each repeat sits still, so the problem mostly goes away. If any continuous motion stays, use a −4.5 dB compromise law for it (the speaker sum then wobbles ≈ ±1.5 dB, which is barely audible).

**P6. The reverb must take stereo input — agree.** The draft is right: a Dattorro plate sums its input. Without separate input diffusers on PLATE / SPRING / SHIMMER, "pan the delay into the reverb" does nothing on three of four types. Budget it (≈ +10–15 % of one reverb, per the draft, **UNVERIFIED** until the spike measures it).

**P7. "Separately from the dry signal" — ask what he means — SHOULD.** If he expects to pan the **dry voice** too: it's mono analog after the VCA, so it needs a passive pan pot into the two summing nodes (≈ $0.60, no MIDI). It only affects phones and line; the speaker is mono. Ask one question: "Do you want the dry voice movable left / right, or is centred fine?"

**P8. MIDI for the pans.** ECHO PAN on CC 102 is fine. Move VOICE PAN off CC 10 (item 15), or drop it (P1). If ECHO MIX and REVERB MIX aren't MIDI-controllable but a pan is, players will find that backwards. Automating the effect *amounts* is the more common need. Consider giving the two MIX knobs CCs as well (owner's call; it doesn't break "knob-only controls send no MIDI", it just moves them into the marked set).

**P9. Mono sum and TS behaviour hold up.** Static pans vanish into the speaker's mono sum and the TS-mono tip with no level change. That's correct and a good reason for constant sum. Item 2 still has to be fixed for the TS path to exist at all.

---

## Numbered suggestions

1. Add a 4th CD74HC4067 on D20 (ADC3), move the battery divider onto it, and publish one recounted mux table (item 1). **MUST**
2. Replace the TS ring-sense with L / MONO + R jacks, or re-do it with a low bias, build-out resistors and an R-driver cut; bench it before layout (item 2). **MUST**
3. Give PARA+4 an audio path (codec R → EXT input through the ladder; wet goes mono in PARA+4), or make the toggle 2-way until it has one (item 4). **MUST**
4. Widen the peg deck holes to ≥ 1 mm clearance per side, or slim the neck, to match the floating strip (item 5). **MUST**
5. Split the TAP-at-power-on gesture: autotune ≠ DFU. Make filter cal a power-on-only gesture (item 6). **MUST**
6. Pan design: drop VOICE PAN; keep one ECHO PAN (still position for TAPE / BBD / CLEAN); make PING-PONG the moving, always-in-time type with ECHO PAN as start side and width; apply the movement per pass in the loop; stereo-input diffusers on every reverb type; bring TAP back to the FX row (§15 P1–P6). **SHOULD**
7. Ask the owner whether the dry voice should be pannable (P7). **SHOULD**
8. Output mute on phones and line, held at reset and through boot calibration (item 7). **SHOULD**
9. Level-based (not gate-based) FX send gating with a hold and a fade (item 8). **SHOULD**
10. Assign PITCH CV OUT to the keytrack DAC channel and define glide, bend and PARA behaviour (item 9). **SHOULD**
11. Read OSC 3 CTL in firmware; KBD CTRL off / ½ / full; RANGE on detented 6-way rotaries (items 11–13). **SHOULD**
12. MIDI hygiene: ignore echoed CCs, add local off, take pan off CC 10 (items 14–15). **SHOULD**
13. Switched PHONES jack for speaker mute; decide whether LINE OUT mutes the speaker; print "stereo · unbalanced" and add a TRS → 2 × TS cable to the build list (items 3, 16). **SHOULD**
14. Fix the stale 74HC595 reference and mark budget-variant §v1.11.6 superseded by DFP §9 (item 10). **SHOULD**
15. Define PARA: RANGE 1 for all, retrigger on new notes, exclude osc 3 in LFO mode; manual note on mixer levels (item 18). **SHOULD**
16. Wet-bus soft limiter, a send high-pass, a 2 s FX fade on low battery, a slewed velocity cutoff step (items 19, 21). **NICE**
17. Add speaker draw to the power budget, bench loudness with the real grille, and consider the PAM8302 module (item 20). **NICE / SHOULD**
18. Recount the FOLD hinge ribbon for the stereo lines (item 21). **SHOULD** if FOLD is built.
