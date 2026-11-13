# Effects
Status: **written 2026-11-13** (systems). Per item below. Sources:
- [owner record](../../design/owner.md) 2026-11-12 22:30 → 11-13;
- [Daisy design §6](../../eng/daisy-first-principles.md);
- [single-chip research §1–5](../../eng/single-chip-research.md);
- [Daisy pin & audio check](../../eng/daisy-pin-and-audio-check.md);
- [master spec](../../eng/budget-variant.md);
- [expert review](../../design/reviews/2026-11-13-audio-synth-review.md) items 8, 19, 21, P3, P6.

## What it does (player's view)
- An **echo** feeds a **reverb**, both digital, both with four characters.
- Turn **ECHO MIX** or **REVERB MIX** up from zero and the effect fades in under the dry sound. At zero the synth is purely analog.
- Echo: **TIME** (how far apart the repeats are), **REPEATS** (how many, up to a controlled runaway on TAPE) and **TAP**.
- Reverb: **DECAY** (how long it rings).
- Tails ring on after you lift a key.

## Owner decisions (verbatim, linked)
- "Is there a way for us to build in some effects, mainly a delay and echo?" (2026-11-12 22:30).
- "I want echo and reverb" · "Delay and verb can be digital" · "I would want great models tho — would be cool if digital could do more than one type."
- FX controls: "Full 8, grow the panel".
- "Check the pin thing. Audio feels the most important since we're introducing digital stuff" → "Switch to Daisy Seed".
- 15:18–15:54: stereo outputs, dry pan, delay pan, FOLLOW (see [panning and stereo outputs](panning-and-stereo-outputs.md)).

## How it works
- **Chip:** Daisy Seed (STM32H750 at 400 MHz, 64 MB SDRAM, stereo codec). The same chip runs control, tuning and MIDI.
- **Signal path:**
  1. The post-VCA voice goes to a TL072 (gain to −6 dBFS peak, diode soft clip, RC anti-alias) → **codec IN L**.
  2. In the DSP: **ECHO → REVERB** (series).
  3. **Wet only** returns: codec OUT L / R → summing resistors → the output sums.
  - The dry path is analog and never switched, so there's **no comb filtering** from converter latency (DFP §6.2).
- **ECHO MIX and REVERB MIX are wet levels in DSP.** With both at 0 the codec outputs digital silence, and the instrument is electrically the analog voice alone.
- **Echo types:**
  - **TAPE:** wow / flutter, saturation, darkening repeats; runaway controlled;
  - **BBD:** dark, short-range character, no clock noise;
  - **CLEAN;**
  - **PING-PONG:** alternates sides on stereo outputs; on the mono speaker it's CLEAN with alternating tone.
- **Reverb types:**
  - **PLATE** (Dattorro);
  - **HALL** (FDN / CloudSeed class);
  - **SPRING;**
  - **SHIMMER.**
  - DECAY scales size and damping together, per type.
- **Stereo:**
  - The echo is a mono line; **DELAY PAN** places it.
  - **The reverbs take stereo input** (proposed; review P6): PLATE / SPRING / SHIMMER need two input diffusers (≈ +10–15 % of one reverb's load, ESTIMATE). HALL is stereo-in already.
- **DSP load:** echo + a CloudSeed-class reverb ≈ **40–60 %** at 400 MHz (eng, `daisy-pin-and-audio-check.md` §3.4). Long buffers in SDRAM, dense taps in SRAM. The spike measures it.
- **Send gating (proposed; review 8):** the input opens on **gate or signal level** (> −60 dBFS at codec IN L), holds ≈ 300 ms after the signal drops, then fades over ≈ 20 ms.
  - This replaces DFP's gate-only mute, which would cut echoes of a note's analog release.
  - It keeps codec noise out between notes.
- **Protection (proposed; review 19):**
  - a **soft limiter** on the wet bus before the codec (runaway TAPE into SHIMMER builds fast);
  - a **≈ 60–80 Hz high-pass on the send** (VCA thump residue and low-end mud).
- **Low battery (proposed; review 21):** the effects **fade over ≈ 2 s** at the cut-off, not instantly.

## Controls and states
| Control | Part | What it does | Status |
|---|---|---|---|
| ECHO TYPE | 4-way rotary (RS16211) on a resistor ladder | TAPE / BBD / CLEAN / PING-PONG; click-free crossfade on change | decided (Full 8) |
| ECHO TIME | 9 mm pot | ms in FREE, a note division in SYNC (see [echo sync](echo-sync.md)) | decided |
| ECHO REPEATS | 9 mm pot | feedback; controlled runaway on TAPE | decided |
| ECHO MIX | 9 mm pot | echo wet level | decided |
| REVERB TYPE | 4-way rotary | PLATE / HALL / SPRING / SHIMMER | decided |
| REVERB DECAY | 9 mm pot | size and damping together | decided |
| REVERB MIX | 9 mm pot | reverb wet level | decided |
| TAP | momentary | tap tempo / echo length (see [echo sync](echo-sync.md)) | decided |
| FREE / SYNC | toggle | see [echo sync](echo-sync.md) | decided |
| DELAY PAN | 9 mm pot | see [panning](panning-and-stereo-outputs.md) | decided feature |

**Placement:** CATHEDRAL layout B puts every effect control on the lid's back row (proposed, pending the owner's layout answer).

## Edge cases
- **Both MIXes at 0:** digital silence out; the dry is untouched.
- **Changing TYPE mid-note:** a click-free crossfade (DSP mixing allows it, DFP §6.2).
- **Runaway:** TAPE REPEATS near full self-oscillates in a controlled way. The limiter (proposed) catches level build-up into a long HALL or SHIMMER.
- **Release tails:** with level-based gating, echoes of an analog release survive.
- **Low battery:** FX fade over 2 s (proposed); the dry keeps playing until the boost cut-off.
- **SOURCE "feedback" in the mixer:** must be tapped from the **dry VCA out, pre-FX and pre-VOLUME** (review 21), so wet latency never enters the ladder loop. Proposed; eng to confirm the tap point.
- **PING-PONG + DELAY PAN:** DELAY PAN sets the start side; no double alternation (review P3).
- **Mono outputs:** the speaker gets the mono sum; PING-PONG becomes CLEAN with alternating tone.

## Interactions with other features
- **Echo sync:** TIME's two scales, FREE / SYNC, TAP, MIDI clock.
- **Panning and stereo outputs:** DELAY PAN, FOLLOW, the stereo-input reverbs, the mono speaker and mono-on-TS.
- **Autotune:** codec IN R is the filter-calibration input; codec IN L doubles as the VCA auto-null monitor (DFP §2).
- **Paraphonic:** if PARA+4 used the codec (option B in [paraphonic](paraphonic.md)), the wet would go mono. The recommended option A keeps it stereo.
- **Power:** the Daisy adds ≈ 0.3–1.0 W over the Pico era (ESTIMATE). Hall gating offsets it.
- **MIDI:** clock in (echo sync). FX knobs aren't MIDI-controllable today.

## MIDI
- **Today:** no FX knob receives or sends MIDI (knob-only). Clock drives the echo tempo in SYNC.
- **Proposed (open for the owner):** ECHO MIX → CC 103, REVERB MIX → CC 104, so a DAW can automate the effect amounts (review P8). DELAY PAN → CC 102 (proposed); DRY PAN → CC 10 (decided).

## Budget (pins / mux / DAC / power / cost)
- **Mux:** 8 channels (5 pots, 2 rotaries, TAP), in the 48 baseline. FREE / SYNC and DELAY PAN on mux D (architecture).
- **Pins:** codec audio pins only (dedicated).
- **DAC:** codec OUT L / R (both used by the wet).
- **DSP:** 40–60 % + ≈ 10–15 % of a reverb for stereo inputs (ESTIMATE).
- **Cost:** FX controls +$8.21 (`budget-variant.md`); TL072s and passives small; the Daisy itself is in the main BOM.
- **Power:** see Interactions.

## Open questions (for the owner)
1. **Should a DAW be able to automate ECHO MIX and REVERB MIX** (they'd gain a MIDI dot and the not-in-control light)?

## Status (item by item)
| Item | Status |
|---|---|
| Echo + reverb, digital, several great types | decided |
| Full 8 controls; Daisy Seed | decided |
| Types TAPE / BBD / CLEAN / PING-PONG and PLATE / HALL / SPRING / SHIMMER; series echo → reverb; wet-only return | eng design (adopted with the decisions above) |
| Stereo-input reverbs | proposed |
| Level-based send gating; wet limiter; send high-pass; 2 s low-battery fade; SOURCE feedback tap pre-FX | proposed |
| ECHO MIX / REVERB MIX MIDI | open (Q1) |
| DSP load, codec noise, the RS16211's height | to be measured on the breadboard spike |
