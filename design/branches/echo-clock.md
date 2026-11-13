# Echo under MIDI clock: how it behaves (systems, branches turn 1, 2026-11-13)

> **Rev 1.1 (2026-11-13, concept turn 1).** Owner chose **option B** (11:58, `design/owner.md`). Placement checked with labels (`concepts/common-how-it-works.md` §2):
> - ONE SHEET frame (128.0, 132.7); FOLD lid (133.0, d 70.6).
> - **Throw left / right** ("free" left, "sync" right). Fore / aft has no room for its words.
> - TIME's and DECAY's legends move behind their knobs.
> - TIME's two scales are printed over **±135°**; firmware clamps the last 15° at each end.

Applies to every branch and, if the owner wants, to the v1.1 concepts as a firmware + one-switch change (the locks themselves are not edited). Same firmware for ONE SHEET and FOLD; only where a new switch would sit differs.

Owner (verbatim): "also i want to make sure the delay can be timed to the midi if there is midi tempo control" · follow-up: "am i missing a control to turn that tempo sync on / off?"

**Short answer to the follow-up: yes, you are.** The spec reads MIDI clock but has no visible way to choose "follow the clock" or "ignore it". Eng's research note proposed a hidden gesture (hold TAP + turn TIME, `eng/single-chip-research.md` §5.2), which never reached the panel spec. Below are the two honest options. **Option B adds a control, so it's an owner decision.** Systems recommends B.

Marks: **[ENG]** = from the eng docs. **[CALC]** = my arithmetic. **PROPOSAL** = systems design, not yet approved.

---

## 1. What the hardware can already do [ENG]
- Clock arrives on **both transports**: USB-MIDI (Seed's own port via the rear USB-C) and TRS MIDI IN (6N138 → USART1_RX). "Both transports are parsed on the control path and feed the FX tempo. 0 pins." (`daisy-first-principles.md` §5.4.)
- The echo runs in DSP, wet only, mixed in DSP; "MIDI-synced repeats" and click-free crossfades are listed as reasons for DSP mixing (§6.2).
- Long buffers live in the Seed's SDRAM (§6.2). A 10 s stereo float buffer is 10 × 48,000 × 2 × 4 B ≈ 3.8 MB [CALC], a small slice of the 64 MB. **Buffer length is not a limit** on synced divisions.
- Panel parts in force: echo TYPE (4-way rotary), TIME (pot, no detents), REPEATS, ECHO MIX, TAP (momentary), one bicolour status light (H7). All read through the mux, ≈ 45 of 48 channels used (`single-chip-research.md` §5.2). **One spare-ish mux channel is enough for one more switch** (46 of 48).
- TAP already carries gestures: hold at power-on = full autotune / DFU; EMPHASIS full + hold TAP = filter cal; hold TAP = battery % query (`daisy-first-principles.md` §3.2, §7.3).
- Rules that bind: "knob-only controls send no MIDI", "MIDI never flips switches". FX controls are not MIDI-controllable in the spec.

## 2. The question, stated plainly (draw: "State the problem in words as clearly as possible")
Sync on/off is really one question: **does TIME mean milliseconds or beats?**
- In milliseconds, the echo is free: TIME sets a length, TAP sets a length.
- In beats, TIME picks a **note division** of a tempo, and the tempo comes from the MIDI clock if there is one, or from TAP if there isn't.

So the control isn't "MIDI on / off". It's **which scale TIME is read on**. That makes the panel tell the truth (J4: the knob positions are the state).

## 3. Option A: no new control (automatic + hidden override). $0
- Clock present → the echo follows it; TIME becomes a division picker.
- Clock absent → free milliseconds.
- To stay free while a clock is running: hold TAP and turn TIME (eng's gesture). Release: the status light confirms with 2 flashes.
- **Cost:** $0, no panel change.
- **Against:** the mode lives in memory, not on the panel. In a DAW that sends clock all the time, the echo silently changes meaning when he plugs in, and the TIME knob's position stops matching what he hears. It overloads TAP (already 3 gestures). His own question shows he expected a switch.

## 4. Option B: a SYNC switch, FREE / SYNC. ≈ $1 · **OWNER CHOSE B (2026-11-13 11:58)**
**Part:** the same mini toggle as the panel's others (one element of each kind), ON-ON, 2 positions. One mux channel (→ 46 / 48). Cost ≈ $1 with nut (ESTIMATE, same part family as VEL/PARA). Placement: the visual designer's call per concept; systems' constraint is **near TIME and readable from the playing position**, on the panel or on the jack wall. On the panel it breaks the current mirror, so each branch must find its partner or its reason.

**TIME carries two printed scales**, one per switch position (machine-marked, H6):
- **FREE:** ≈ 20 ms → 2 s, log taper (PROPOSAL; the range isn't in the spec yet).
- **SYNC:** 9 zones, short → long, ≈ 30° each with hysteresis so a zone never flickers:
  `1/16 · 1/8T · 1/16. · 1/8 · 1/4T · 1/8. · 1/4 · 1/4. · 1/2` (PROPOSAL). Dotted eighth sits near the middle, where the dub throw lives.

### Behaviour table (PROPOSAL)

| SYNC switch | MIDI clock | TIME means | TAP does | Echo length |
|---|---|---|---|---|
| FREE | absent | ms | tap 2+ times: echo length = the tap interval | TIME, or the last tap until TIME moves (jump-on-move) |
| FREE | present | ms | same as above; **the clock is ignored** | same |
| SYNC | absent | division | tap 2+ times: sets the **tempo** (the tap is the quarter note) | division × tapped tempo (default: last tempo, kept in flash; 120 BPM on first ever boot) |
| SYNC | present | division | **nothing to the tempo**: the clock has it. Status light gives 1 short amber flash to say so | division × clock tempo |

### Clock handling (firmware)
- **Lock:** after 24 ticks (one beat) with stable spacing. Tempo = rolling average over the last 24 ticks, then smoothed; the echo updates only when the smoothed tempo moves > 0.5 %, so USB jitter never makes TAPE warble.
- **Lost:** no tick for 500 ms (that covers tempos down to 60 / (24 × 0.5) = 5 BPM [CALC]). The echo **holds the last tempo**; nothing jumps. TAP becomes live again.
- **START (0xFA):** no effect on the echo (a delay line has no bar position). **STOP (0xFC):** tails keep ringing; the echo is never cut.
- **Both transports sending:** USB wins while it's ticking; TRS takes over after USB has been silent 500 ms. (PROPOSAL; eng may prefer "first to arrive wins". Low stakes.)
- **Tempo or division changes:** TAPE and BBD **glide** (≈ 150 ms, like a tape motor changing speed: the pitch bend is the character). CLEAN and PING-PONG **crossfade** between two read heads (≈ 50 ms), so there's no pitch artefact.
- **PING-PONG:** the division is per side (L, then R).
- **Longest echo:** 1/2 note. At 40 BPM that's 3 s [CALC]; inside the buffer.
- **ECHO MIX at 0:** the echo still tracks tempo, so bringing it up lands in time.

### Feedback (status light, H7 kept)
Low-priority flashes; tune-failed and low-battery always win.
- After a tap tempo: the light flashes the tempo 4 times (green, 40 ms), then returns to normal. (This is the visual designer's v1.1 proposal; systems adopts it.)
- Clock locks while in SYNC: 2 green flashes on the beat. Clock lost: 2 amber flashes.
- TAP pressed while the clock has it: 1 short amber flash.
- **Alternative for the director/owner:** a lit TAP cap blinking the echo tempo all the time (the pedal convention). Clearer, especially in sun, but it's a second light and breaks H7.

### What doesn't change
- No MIDI CC for TIME or the switch ("knob-only controls send no MIDI"; "MIDI never flips switches").
- Little D does **not** send clock out. **Scope question for the owner:** would he want the tapped tempo sent as clock on USB/TRS OUT, to drive a drum machine in the park? Firmware only, but it's new behaviour.

## 5. Flow: F13 Echo in time with a MIDI clock (job J19b–d)
1. Connect the clock source: USB-C to a computer/DAW, or TRS MIDI IN from a drum machine or sequencer.
2. (Option B) SYNC switch → SYNC. (Option A: nothing.)
3. Start the clock. Status light: 2 green flashes = locked.
4. Turn ECHO MIX up; pick a division on TIME's SYNC scale (e.g. 1/8.); REPEATS to taste.
5. Change tempo on the source: the echo follows (TAPE glides, CLEAN crossfades).
6. Stop the clock: tails ring; the echo holds the tempo (2 amber flashes).
7. Want free time back: SYNC switch → FREE; TIME reads milliseconds again. (Option A: hold TAP, turn TIME.)

## 6. Flow: F14 Tap tempo with no clock (the park case)
1. SYNC → SYNC. Tap TAP 2–4 times on the quarter note (taps > 2.5 s apart start over).
2. Light flashes the tempo 4 times. Pick a division on TIME.
3. Or SYNC → FREE and tap the echo length itself.

## 7. Open, for eng (none blocks the design)
- FREE range (20 ms–2 s) and the 9 divisions: confirm against the echo models.
- Tap-interval and clock-tempo limits (proposal: 30–300 BPM).
- Mux channel 46 confirmed free on the right mux for each concept (FOLD's base mux was at 33/32 before the 3rd mux).
