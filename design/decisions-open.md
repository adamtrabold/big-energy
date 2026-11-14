# Waiting on you

Decisions only you can make, newest first. The team keeps working around them; each answer unblocks the part named. When you answer in chat, the orchestrator records it in the owner record and removes it from here.

---

## 1. CATHEDRAL layouts: every option, side by side
**Your call:** which layout. In practice it comes down to **three oscillators (P5R)** or **four, with your stacked layout (P5OB-D)**. Nothing is approved yet.

| | Director | Synth-player critic |
|---|---|---|
| **P5R** (3 oscillators, 132 mm) | **10** | **8**: oscillators in one long row, filter envelope far from cutoff |
| **P5OB-D** (4 oscillators, 145 mm) | **9**: empty plate on the right; drift split from tune | **10**: "I'd play it and defend every control" |

**P5R: team rows, three oscillators, 132 mm deep.**

![P5R: full top, 1:1 at 9.9 px/mm](branches/concepts/cathedral/img/cathedral-s5-P5R-top-9.9px-per-mm.png)
![P5R: standing](branches/concepts/cathedral/img/cathedral-s5-P5R-standing.jpg)

**P5OB-D: your layout, four oscillators, 145 mm deep.** Oscillators are stacked on the left, the amp envelope is the top row, and the filter envelope is a row beside the speaker, right above cutoff.
- **Costs:** both halves are 13 mm deeper (each half 286 × 145 mm, about 10% more area). Closed thickness is unchanged. It weighs about 55 g more. The 4th oscillator adds about $20–30 and 0.4 W.
- **Compromise 1:** drift sits under oscillator 2, joined to tune by a printed "tuning" line. Putting them side by side would force the bend stick to be lowered.
- **Compromise 2:** about 50 mm of empty plate right of echo and reverb. Filling it would mean moving the effect levels from the base onto the lid.

![P5OB-D: full top with 4 oscillators, 1:1 at 9.9 px/mm](branches/concepts/cathedral/img/cathedral-s8-P5OBD-study-top-9.9px-per-mm.png)
![P5OB-D: standing](branches/concepts/cathedral/img/cathedral-s8-P5OBD-study-standing.jpg)

**Your layout at 132 mm (study).** Three oscillators, amp envelope on top, filter row below. It fits, but the right side can't be filled without moving the effect levels or out onto the lid.

![P5OB study at 132 mm](branches/concepts/cathedral/img/cathedral-s7-P5OB-study-top-9.9px-per-mm.png)

All three share softer corners, the spine back, a line grille, no name on the panel, one knob-marking system, and dots on the knobs that take MIDI. The full reviews are under Reviews (player review, rounds 1–6).

---

## 2. CATHEDRAL back opening, now there's no spine
Closed, there's a 22 × 266 mm opening along the back where the knobs inside show.

- **Leave it open, inside finished dark,** so the knob tops read as shadow. *Team recommends.*
- **Deal with it later** with a sleeve or case.

---

## 3. Buy-and-test (cheap, before building)
- **T1:** one pack of [Cherry Tree Toys 3/8" plugs](https://cherrytreetoys.com/3-8-mushroom-plugs/): measure head height and tenon on 5.
- **T2:** one hollow cast-brass key head on one switch: 20 presses slow and fast next to a wood plug; pass = no clack, wobble or sticking.

---

## 4. Line-out jacks (from the expert review)
**Unblocks:** the output circuit.
The mono-cable detection on LINE OUT can't work as drawn.

- **Two jacks, L/MONO and R:** the standard synth answer. A mono cable in L/MONO gets the full mix automatically, with no firmware. Adds one hole.
- **Keep one stereo jack and rework the detection circuit:** fewer holes, more parts, and it needs a bench test. A stereo cable into an audio interface can still go quiet.

Two jacks also give back a Daisy pin (pins are now at 30–31 of 31). *Team recommends two jacks.*

**Also:** should plugging into line out turn the speaker off? Most players expect it to, so the speaker doesn't feed back through a PA.

---

## 5. MIDI (see Features → MIDI for the full page)
- Should the dry pan stay on CC 10? DAWs send "pan = centre" on CC 10 every time a project opens, so the pan would jump to centre on its own. The team recommends moving it to an unused number.
- Should a DAW be able to automate the echo and reverb amounts? Those two knobs would get the MIDI dot and the "held by MIDI" light.
- Channel 1, or respond on any channel (omni)?
- Should the knobs ever send MIDI (off by default), or receive only?

---

## 6. Aftertouch switch label
**Unblocks:** the panel legend.
The pressure switch adds modulation amount: vibrato when OSC MOD is on, a filter wobble when FILTER MOD is on, or a brighter filter on FILT.

- **MOD / OFF / FILT:** says what it really does. *Team recommends.*
- **VIB / OFF / FILT:** your earlier word, but it's only vibrato when OSC MOD is on.

---

## 7. Filter keyboard tracking switch (KBD)
**Unblocks:** the KBD legend on the base.
The Model D reaches full tracking (both of its switches on). Ours is one 3-way switch, so it has three settings, not four.

- **off · 1/3 · 2/3:** as specified today. Full tracking isn't available.
- **off · 1/2 · full:** the firmware sets the amounts (the tracking voltage is already digital), so full is there for playing the filter as a tone. *Team recommends; eng to confirm.*

---

## 8. Bend range
**Unblocks:** the bend stick's firmware setting.
How far the stick bends the pitch at full push, up or down.

- **± 2 semitones:** a whole tone each way, the same as the MIDI default. *Team recommends.*
- **Wider (e.g. ± 5 or ± 7):** bigger dives, less fine control near the centre.

## 9. The 4th note in "voices: 4"
**Unblocks:** the voice board (one chip and one pin).
The 4th note comes from the Daisy, and it needs a way into the real filter.

- **A. A 5th small DAC chip (≈ $4):** the 4th note goes through the filter like the others; nothing else changes. *Team recommends.*
- **B. Borrow the effects' right channel:** no new chip, but the effects go mono while "voices: 4" is on, and the mixer's extra source must sit on "input".
- **C. Drop the 4th note for now:** the switch becomes 1 · 3 only.

## 10. Which note the filter follows when playing chords
**Unblocks:** the paraphonic firmware.
With one filter for up to four notes, its tracking follows one of them.

- **Highest note:** chords stay bright on top. *Team recommends (the default already explained to you).*
- **Lowest note:** matches the mono behaviour (lowest-note priority).
- Either way, a key combination switches between them (to be defined in Firmware and gestures).

## 11. How much drift at full
**Unblocks:** the drift knob's firmware range.
Drift makes each oscillator wander slowly on its own; at 0 it's rock steady.

- **Subtle (up to ± 5 cents):** barely there, a hint of life.
- **Vintage (up to ± 15 cents):** an old synth warming up. *Team recommends.*
- **Wild (up to ± 30 cents):** clearly out of tune at full; a sound effect.

Firmware can change it later.
