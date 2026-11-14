# Aftertouch
Status: **written 2026-11-13** (systems). Per item below. Sources:
- [owner record](../../design/owner.md);
- [aftertouch spec](../../eng/aftertouch.md) rev 0 (master spec rev 14);
- [Daisy design](../../eng/daisy-first-principles.md);
- [CATHEDRAL §10, §16](../../design/branches/concepts/cathedral/how-it-works.md);
- [expert review](../../design/reviews/2026-11-13-audio-synth-review.md) item 5.

## What it does (player's view)
- Press harder on a held key and the sound changes: **more vibrato or filter wobble** (MOD), or **a brighter filter** (FILTER).
- The **AFTERTOUCH** switch chooses MOD, OFF or FILTER. It reacts only while a key is held down.
- Nothing to calibrate: it learns how heavily you rest your fingers.

## Owner decisions (verbatim, linked)
- "i think it needs its own switch but yes now i want it". Recorded as: add channel aftertouch, its **own** destination switch (separate from VELOCITY), **sent on MIDI out too**.
- "Add MIDI out" (TRS MIDI OUT).

## How it works
- **Sensor:** two **Interlink FSR UX 408** strips (300 mm, trimmed to ≈ 240), one lane under each key row, wired in parallel, so the reading is the total force wherever you press.
- **Mechanism:**
  - **strip C (the key board) floats on the two lanes**, held down by 4 springs (≈ 4 N preload in total);
  - the lanes carry all key force after bottom-out;
  - the stack moves ≈ 10–50 µm at 20 N (ESTIMATE), so **no extra key travel**;
  - **0 mm added height** nominal (the stack fills the existing ≈ 8 mm gap under strip C).
- **Electronics:** FSRs → 10 k / 100 nF divider → mux B ch 15 (ADC2). The toggle is a resistor ladder on mux B ch 14. Sampled at the 8–10 kHz frame → 1 kHz → τ 10 ms.
- **Firmware** (aftertouch §3):
  - **pressure = 0 unless a key is bottomed** (Hall depth ≥ 0.9);
  - a **self-learning dead zone** above normal holding force: max(1.5 N, 1.3 × the median resting force) + 0.5 N per extra key held;
  - 30 ms blank after each note-on;
  - **auto-zero** whenever no key is held;
  - full scale 8 N, curve γ ≈ 1.5;
  - release ramps to 0 in 20 ms.
- **Destinations:**
  - **MOD** adds to the mod-depth CV (+50 % of MOD's range at full pressure): vibrato with the oscillators' MOD switch on, filter wobble with the filter's MOD switch on.
  - **FILT** adds up to +2 octaves to the CUTOFF CV (MCP4822 #4 B).
  - Velocity and pressure add on CUTOFF.
- **FOLD / CATHEDRAL:** the base board **splits** into a floating key strip and a fixed PLAY board, joined by a short ribbon (aftertouch §8.5). The printed base floor under the keys must be flat (a 3 mm acrylic base strip glued in).

## Controls and states
| Control | Positions | Status |
|---|---|---|
| **AFTERTOUCH** toggle (ON-OFF-ON) | **MOD / OFF / FILTER** (OFF in the centre: there's no amount knob) | decided (own switch); positions eng |
| Span and curve | settings (power-on: hold the top key, then keys 6–10) | proposed (gestures doc) |

**Placement:** CATHEDRAL puts AFTERTOUCH on the lid's switch line at (242.5, d 32), beside VELOCITY at 222.5, as a "how the keys respond" pair (proposed).

## Edge cases
- **Force bypass:** anything but the lanes touching strip C steals pressure. **Keep ≥ 1 mm clearance round every key** (strip C can shift ± 0.5 mm).
  - With CATHEDRAL's printed carriers, the **deck holes go to Ø 13.2** round the Ø 11.2 necks (review 5, a must-fix; [keys and velocity](keys-and-velocity.md)).
  - The harness needs a slack loop; nothing in the shell may touch strip C.
- **Handling with no key held:** forced 0. Bumps with a key held stay under the dead zone.
- **Re-strike under held pressure:** the 30 ms blank stops glitches.
- **Brass heads:** the extra 2–3 g per head sits inside the 1.5 N dead-zone floor (ESTIMATE).
- **Spike tests A1–A8** (trim the strip, force spread across positions, false triggers, handling, creep, latency, feel) gate the hardware before layout.
- **Mod-depth CV path:** with the proposed **5th MCP4822** (PARA+4 path, [paraphonic](paraphonic.md)), mod depth moves from the Seed DAC to that chip. MOD's routing is unchanged.

## Interactions with other features
- **Keys:** the clearance rule; the Hall "bottomed" gate.
- **Bend and mod:** MOD adds to the MOD knob's depth (and to CC 1 from MIDI).
- **Autotune:** the held-note pitch loop freezes on period variance, so aftertouch vibrato can't fight it.
- **Velocity:** both can add to CUTOFF.
- **Enclosure:** the floating strip, the flat base floor, the board split in FOLD.

## MIDI
- **Out:** channel pressure on USB and TRS. On change, at most every 5 ms, a final 0 on release, in all switch positions. Can be disabled in settings. **This is the only MIDI the instrument sends today.**
- **In:** channel pressure drives the same destination: max(local, MIDI). It decays to 0 50 ms after the last MIDI note-off. Optional: poly pressure for the sounding note (proposed).

## Budget (pins / mux / DAC / power / cost)
- **Mux:** 2 channels (FSR, toggle), in the 48 baseline.
- **Pins:** 0.
- **DAC:** shares the mod-depth and CUTOFF channels.
- **Power:** ≤ 1 mW.
- **Cost:** ≈ +$18–33 (FSRs $9.98, shipping, toggle, silicone, springs; acrylic from scrap).

## Open questions
1. **Switch label: MOD or VIB?** Eng's note: "MOD" is honest (it adds modulation amount: vibrato *or* filter wobble, depending on the oscillators' / filter's MOD switches); "VIB" matches your earlier word. *Team recommends MOD.* (Added to the decisions page.)

## Status (item by item)
| Item | Status |
|---|---|
| Channel aftertouch, own destination switch, sent on MIDI out | decided |
| FSR lanes under a floating strip; firmware gate, dead zone and auto-zero | eng design (rev 14) |
| MOD / OFF / FILT, depths +50 % / +2 oct | eng design |
| Base-board split in FOLD | eng design |
| ≥ 1 mm key clearance → deck holes Ø 13.2 | proposed (review must-fix) |
| Settings gestures | proposed |
| Label MOD vs VIB | open (owner) |
| Poly pressure in | proposed |
