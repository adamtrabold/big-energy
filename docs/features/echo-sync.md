# Echo sync
Status: **written 2026-11-13** (systems). Per item below. Sources:
- [owner record](../../design/owner.md) 11:47, 11:58;
- [echo-clock spec](../../design/branches/echo-clock.md) rev 1.1;
- [CATHEDRAL §2, §15–16](../../design/branches/concepts/cathedral/how-it-works.md);
- [Daisy design §5](../../eng/daisy-first-principles.md);
- [expert review](../../design/reviews/2026-11-13-audio-synth-review.md) item 6.

## What it does (player's view)
- One switch, **FREE / SYNC**, decides what the echo's **TIME** knob means.
  - **free:** TIME is a length in milliseconds.
  - **sync:** TIME picks a note value (1/16 … 1/2). The tempo comes from MIDI clock (a DAW over USB, or a drum machine over TRS) if there is one, otherwise from **TAP**.
- Change the tempo at the source and the echo follows, without clicks.

## Owner decisions (verbatim, linked)
- 11:47: "also i want to make sure the delay can be timed to the midi if there is midi tempo control".
- Follow-up: "am i missing a control to turn that tempo sync on / off?"
- 11:58: echo sync **option "B"**: a **FREE / SYNC toggle by TIME**.
  - FREE: TIME ≈ 20 ms – 2 s, clock ignored.
  - SYNC: TIME picks a note division; tempo from MIDI clock (USB or TRS) if present, else TAP.

## How it works
- **Clock in:** USB-MIDI and TRS MIDI IN are both parsed on the Daisy's control path (DFP §5.4, 0 pins).
  - **Lock:** after 24 ticks of stable spacing.
  - **Tempo:** a 24-tick average, then smoothed. It updates only when the change is > 0.5 %, so USB jitter can't make TAPE warble.
  - **Lost:** no tick for 500 ms. The echo holds the last tempo.
  - **Both transports sending:** USB wins while it's ticking; TRS takes over after 500 ms of USB silence.
- **START:** no effect (a delay has no bar position). **STOP:** tails keep ringing.
- **Tempo or division changes:** TAPE and DARK **glide** (≈ 150 ms, like a tape motor); CLEAN and PINGPONG **crossfade** two read heads (≈ 50 ms).
- **TIME's two printed scales:**
  - inner = ms (≈ 20 ms – 2 s, log);
  - outer = 9 divisions: 1/16 · 1/8T · 1/16. · 1/8 · 1/4T · 1/8. · 1/4 · 1/4. · 1/2;
  - printed over **±135°** (not the pot's ±150°). **Firmware holds the last 15° at each end at min / max**, so the scale never lies and no tick sits under the FREE / SYNC nut.
  - Division zones are ≈ 30° each with hysteresis.
- **TAP:** 2–4 taps on the quarter note. Taps > 2.5 s apart start over.
  - In FREE, the tap interval *is* the echo length; moving TIME takes back (jump-on-move).
  - In SYNC with a clock running, TAP doesn't change the tempo (one short amber flash says the clock has it).
- **Longest echo:** 1/2 note; at 40 BPM that's 3 s. The SDRAM buffer isn't a limit.
- **With ECHO MIX at 0** the echo still tracks tempo, so bringing it up lands in time.

## Controls and states
| Control / light | States | Status |
|---|---|---|
| **FREE / SYNC** toggle (left / right throw, words beside) | free · sync | decided (toggle); throw and placement proposed |
| TIME | ms (free) / 9 divisions (sync), ±135° printed + clamp | division set and clamp proposed |
| TAP | taps; held ≥ 1.5 s = battery level (gestures doc) | decided feature; timing proposed |
| Status light | 4 green flashes at the tempo after a tap · 2 green on clock lock · 2 amber on clock loss · 1 short amber when TAP is ignored | proposed (H7: one light) |

**Placement (CATHEDRAL, proposed):**
- FREE / SYNC at lid (77.5, d 69.7), between TIME (64) and REPEATS (84) on the re-centred effects row;
- TAP at the base row's right end (x 261), mirroring the bend stick;
- TIME's and REPEATS' legends sit behind their knobs.

## Edge cases
- **Clock appears mid-note:** the tempo glides (TAPE / DARK) or crossfades (CLEAN / PINGPONG); no click.
- **Clock jitter (USB):** smoothed; it only updates on > 0.5 % change.
- **Clock stops or the cable is pulled:** the echo holds the tempo, and tails ring on.
- **Two clocks:** USB wins while ticking.
- **TAP live vs gestures:** tapping never triggers a gesture. Hold ≥ 1.5 s shows the battery level and doesn't count as a tap. Power-on TAP gestures are separate (review item 6; [firmware update and gestures](firmware-update-and-gestures.md)).
- **FREE with a clock present:** the clock is ignored (that's what FREE means).

## Interactions with other features
- **Effects:** the echo types decide glide vs crossfade.
- **Panning:** none (no tempo auto-pan; the owner's pans are audio).
- **MIDI:** clock in from both transports. **Clock out** from TAP is a free extra (off by default, sent only when no clock is received; see [MIDI](midi.md)).
- **Gestures:** TAP's live and power-on uses ([firmware update and gestures](firmware-update-and-gestures.md)).
- **Status light:** shares the one light (tune-failed and low-battery always win).

## MIDI
- **Receive:** clock (0xF8), START (0xFA), STOP (0xFC) on USB and TRS. Song position is ignored.
- **Send:** nothing by default. Clock out from TAP is an open free extra.

## Budget (pins / mux / DAC / power / cost)
- **Mux:** FREE / SYNC 1 channel (mux D, architecture); TAP and TIME are in the baseline.
- **Pins:** 0 (clock parsing is on the existing MIDI pins).
- **DAC:** 0. **Power:** negligible.
- **Cost:** ≈ $1 (toggle + nut, ESTIMATE).

## Open questions
1. *(For the owner, already in [MIDI](midi.md))* Send TAP's tempo out as MIDI clock (a drum machine on a park bench)? Free; off by default.

## Status (item by item)
| Item | Status |
|---|---|
| Echo follows MIDI clock (USB + TRS) | decided |
| FREE / SYNC toggle by TIME | decided (option B) |
| FREE: ms ≈ 20 ms – 2 s, clock ignored; SYNC: divisions, tempo from clock else TAP | decided |
| Lock / loss timing, smoothing, glide vs crossfade, START / STOP handling, USB priority | proposed |
| 9 divisions; ±135° printed with a firmware clamp | proposed (director accepted the clamp) |
| Status-light flashes | proposed |
| Placement (CATHEDRAL) | proposed |
| Clock out from TAP | open (free extra) |
