# MIDI
Status: **written 2026-11-13** (systems). Per item: decided / proposed / open (§10). Sources:
- owner record [`../../design/owner.md`](../../design/owner.md);
- [`../../eng/daisy-first-principles.md`](../../eng/daisy-first-principles.md) §3.2, §5 (DFP);
- [`../../eng/aftertouch.md`](../../eng/aftertouch.md) §4.2;
- [`../../eng/budget-variant.md`](../../eng/budget-variant.md);
- [`../../design/branches/echo-clock.md`](../../design/branches/echo-clock.md);
- [`../../design/branches/concepts/cathedral/how-it-works.md`](../../design/branches/concepts/cathedral/how-it-works.md) §15;
- expert review [`../../design/reviews/2026-11-13-audio-synth-review.md`](../../design/reviews/2026-11-13-audio-synth-review.md) items 9, 11, 13–15, 18, 21, P8.

**Organising principle (owner):** design for **being played and automated from a DAW** (or another device). It is **not a MIDI controller**. Sending is a "free extras" section: explored only where it costs nothing and creates no echo loops.

## What it does (player's view)
- Plug the rear USB-C into a computer (class-compliant USB-MIDI, no driver), or a TRS MIDI cable into MIDI IN.
- From the DAW you can:
  - **play it** (notes, velocity, pitch bend, mod, pressure);
  - **automate the knobs that carry a MIDI dot**;
  - **lock its echo to the DAW's tempo**.
- The panel stays honest: a knob the DAW is holding lights the **not-in-control** light until you move it.
- The instrument keeps working fully on its own, with no MIDI at all.

## Owner decisions (verbatim, linked)
- 2026-11-12, "Decisions already made": "MIDI: USB-MIDI + 3.5 mm TRS MIDI in; MIDI-controllable params per eng; **knob-only controls send no MIDI; MIDI never flips switches**." "mod depth MIDI-controllable (jump-on-move)."
- 2026-11-13: "Add MIDI out" (TRS MIDI OUT jack). Aftertouch: "i think it needs its own switch but yes now i want it". Recorded as "sent over MIDI out too".
- 2026-11-13 11:58: echo sync option "B" (FREE / SYNC; tempo from MIDI clock, USB or TRS, if present).
- 2026-11-13 15:44: "Yea sure on midi" → the pan **receives CC 10**.
- 2026-11-13 16:21: "sorry i didnt mean is usbmidi capable of send, but rather are we already doing send. if we do send then we gotta think about ALL of the features, and this is pretty definitively not a midi controller. though if it's free it could be."
- 2026-11-13 (latest): "the workflow im much more interested in is controlling it from another device or mainly a DAW. im not so worried about using it as a controller for other things. but if it's free we could explore it"

## How it works
- **Transports:**
  - USB-MIDI on the Seed's own port (rear USB-C, DFP §5.3 U1);
  - TRS MIDI IN through a 6N138 on USART1 RX (D14);
  - TRS MIDI OUT on USART1 TX (D13, type A).
- **Both inputs merge into one stream.** Same channel rules; clock from either (USB wins while ticking; `echo-clock.md`).
- **Parsing:** the control loop at 1 kHz; notes and clock with ≤ 1 ms latency [ENG]. Running status handled; active sensing ignored (proposed).
- **Parameters:**
  - a MIDI value is applied through the same path as the knob: the knob's firmware value, smoothed;
  - the knob goes "not in control" (**jump-on-move**, decided);
  - moving it > 1.5 % takes it back.
- **What's sent today:** **only channel pressure** (aftertouch §4.2: on change, ≤ every 5 ms, a final 0 on release, all switch positions, can be disabled).
  - Nothing else is specified to send.
  - **`design/jobs.md` F7 step 7 ("knobs send CC out over USB") was a team inference, not an owner decision.** It's superseded by this doc; the owner's stance governs.

## Controls and states
| Message (in) | What it does | Status |
|---|---|---|
| **Note on / off** (+ velocity) | plays the voice like a key. **MIDI and the keys share one note pool.** MONO: low-note priority, single trigger, legato glide as with keys. PARA: allocated as the keys are | notes in decided (locked spec); priority = eng default (**proposed** as the rule); merge **proposed** |
| Note numbers | key 1 of the 25 = **MIDI 48 (C3)** at RANGE 8'. Notes outside the keyboard still play, up to the VCOs' range, and are octave-folded beyond it | proposed |
| **Velocity** | the same velocity CV (Seed DAC) through the VELOCITY toggle (LOUD / BOTH / FILT), same curve as the keys. Release velocity ignored | proposed (keys' path decided) |
| **Pitch bend** (14-bit) | **added to the bend stick** (both centred → 0), clamped. Default **±2 semitones**; **RPN 0** (bend sensitivity) sets 0–12 | in: proposed (review 21: "not stated") |
| **CC 1 mod** | mod depth (the MOD knob's value), jump-on-move | **decided** |
| **Channel pressure** | through the AFTERTOUCH switch: max(local, MIDI); decays to 0 50 ms after the last note-off | decided feature; behaviour eng (rev 14) |
| Poly pressure | maps the sounding note's pressure to the same path | proposed (eng: $0) |
| **CC 64 sustain** | holds the gate (MONO) / allocations (PARA) while down. Common from DAWs and pedals | proposed |
| **Clock / START / STOP** | echo tempo in SYNC (option B). START: no effect; STOP: tails ring; loss 500 ms → hold tempo | **decided** (option B); details `echo-clock.md` (proposed) |
| CC 120 all sound off | release all notes **and** fade the wet in 50 ms (immediate silence) | proposed |
| **CC 121 reset all controllers** | bend → centre, pressure → 0, sustain off, **and every knob back in panel control** (LED off). It does **not** set MOD to 0 | proposed |
| CC 123 all notes off | release all notes; tails ring | proposed |
| Program change, song position, SysEx | ignored (no recall: owner, "i dont think recall is important") | proposed |

**The MIDI-dot parameters (receive CC, jump-on-move, engraved dot):**

| Knob | CC (proposal) | Why this number | Status |
|---|---|---|---|
| MOD | **1** | the mod wheel | decided (CC 1 per eng) |
| GLIDE | 5 | portamento time | proposed |
| CUTOFF | 74 | "brightness": what DAWs and controllers default to for cutoff | proposed |
| TUNE | 20 | undefined range (no GM default can grab it) | proposed |
| FREQ 2 / FREQ 3 | 21 / 22 | undefined | proposed |
| RANGE 1 / 2 / 3 | 23 / 24 / 25 | undefined. **If RANGE becomes a detented 6-way rotary (review 13), it's a switch: MIDI never flips switches, so drop these** | proposed / open |
| **DRY PAN** | **10** (decided) — see the CC 10 problem below | owner decided CC 10 for "the pan" | decided, with an open question |
| ECHO PAN | 102 | undefined | proposed |
| ECHO MIX / REVERB MIX | 103 / 104 | review P8: DAW users automate effect *amounts* more than pans. **Owner's call to add them** (it moves them into the marked set) | open |

**Channel:**
- **Proposed:** receive on **channel 1 by default** (not omni), so other tracks on the same interface don't play it.
- Set it with a **power-on key combo**: hold the lowest key at power-on, then press key n for channel n (keys 1–16); key 17 = omni. Stored in flash. It doesn't use TAP, whose gestures already collide (architecture O5).
- The same channel applies to USB and TRS.

## Edge cases (the DAW user's list)
1. **DAW and knob disagree.**
   - Last message wins (jump-on-move). An incoming CC grabs the knob and lights the LED; moving the knob > 1.5 % takes it back.
   - **While DAW automation is playing**, every new automation value grabs it again: the DAW wins until automation stops. That's normal hardware behaviour.
   - **Proposed option:** after a take-back, the knob holds control for 1 s against automation, so a quick override sticks. Owner's call.
2. **Project load.** DAWs often send a burst on load or transport start: CC 121, CC 7, **CC 10 = 64**, CC 1 = 0, bend centre, then automation chase.
   - CC 121 → every knob back to the panel (above).
   - CC 7 → ignored (VOLUME is analog).
   - Chased automation values → grab their knobs (intended).
   - **CC 10 = 64 would silently centre DRY PAN** even if the user never automated it (review 15).
   - **Open, for the owner:** keep CC 10 (the LED shows it, a nudge takes it back), or move DRY PAN to an undefined CC (e.g. 105), with an option for CC 10.
   - **Proposed recommendation:** undefined CC by default. It avoids a pan that moves on its own every time a project opens.
3. **DAW echo / MIDI thru.** Only matters if the instrument **sends** (free extras). See there: local off and echo suppression.
4. **Notes doubled.** Keys play the voice locally. If the DAW also records and echoes them back, you hear doubles. That only happens if notes are sent (free extras), so local off belongs with that extra.
5. **Stuck notes:** the gate releases on CC 123 / 120, on a USB disconnect, and on clock STOP if sustain is held.
6. **PARA from a DAW:**
   - chords allocate like keys;
   - oscillators set to zero in the mixer are silent;
   - OSC 3 in LFO mode (OSC 3 CTL, review 11) is excluded, which means firmware must read OSC 3 CTL;
   - review 18's PARA behaviour applies (RANGE 1 for all, retrigger on new notes: proposed).
7. **Pitch CV out from DAW notes** (review 9): carries the MONO note, or the lowest note in PARA; it includes bend and glide (proposed). It needs its DAC channel (architecture §5.3).

## Interactions with other features
- **Echo sync:** clock in from either transport (`echo-clock.md`). TAP is ignored for tempo while the clock runs.
- **Aftertouch:** pressure in and out (above).
- **Bend and mod:** the stick and PB sum; MOD and CC 1 share jump-on-move.
- **Panning:** DRY PAN (digipot, so MIDI-able) and ECHO PAN (DSP).
- **FOLLOW** is a switch: never flipped by MIDI.
- **Paraphonic:** shared allocation for keys and MIDI.
- **Gestures:** the channel combo avoids TAP (architecture O5).
- **Power:** USB-MIDI works on battery. Charging and MIDI share the one USB-C (decided).
- **Recording:** the **primary way to record this instrument into a DAW is its stereo line out (audio)**, decided stereo. MIDI recording of a performance is an extra (below).

## MIDI — free extras (sending), each off by default
Owner: send only "if it's free"; sending means thinking about every feature. Each extra costs **$0 in parts** (USB-MIDI and TRS OUT already exist) and is firmware only. Each has a loop risk, named.

| Extra | What it gives a DAW user | Loop / risk, and its guard | Recommendation |
|---|---|---|---|
| X1 Channel pressure out | already in the eng spec (aftertouch §4.2) | none on its own | **keep as specified** (decided feature), with its setting to disable |
| X2 Performance out: notes + velocity + bend + CC 1 + sustain | record his playing as MIDI in the DAW | DAW thru doubles the notes → needs **local off** (CC 122 in, plus a setting). With local off, the keys only send; the DAW plays the voice back | proposed, **off by default**; only with local off |
| X3 Knob CCs out (the MIDI-dot knobs) | record knob moves as automation | the DAW echoes them back and grabs the knob → **ignore an incoming CC equal to one sent in the last 200 ms** (review 14) | proposed, off by default |
| X4 Clock out from TAP | drive a drum machine from TAP (park) | two clock masters with a DAW → send only when **no clock is being received** | proposed, off by default |
| X5 Soft thru (TRS IN → TRS OUT) | chain gear | a USB → TRS loop if the DAW also echoes → thru TRS only, never USB → TRS | proposed, off by default |
| — SysEx settings / backup | — | not free (a protocol and a page to design) | not proposed |

**Settings for the extras:** power-on key combos, as for the channel (not TAP). Exact keys proposed with the gestures doc.

## Budget
- **Pins:** D13 (TRS OUT), D14 (TRS IN), the Seed USB port: all already allocated (architecture §5.2). **Mux: 0. DAC: 0.**
- **Cost:** $0 beyond decided parts (6N138 + TRS jacks: eng BOM). **Power:** negligible.
- **Firmware:** the parser, the CC map, jump-on-move (exists), channel select, RPN 0, and the extras.

## Open questions (for the owner, one at a time)
1. **DRY PAN on CC 10** (your decision) vs an undefined CC, given that DAWs send CC 10 = 64 on project load and would centre it on their own. Recommendation: undefined CC.
2. **ECHO MIX and REVERB MIX as MIDI-dot knobs** (CC 103 / 104) so a DAW can automate the effect amounts? (Review P8.)
3. **Default channel 1** with a power-on channel combo, or **omni**?
4. **The free extras:** any of X2–X5 wanted at all? (X1 pressure-out is already in the spec.)
5. **Automation vs the knob:** last message wins (standard), or the knob holds 1 s after you grab it?
6. (From the review) If RANGE becomes a detented rotary, it leaves the MIDI set. OK?

## Status (item by item)
| Item | Status |
|---|---|
| USB-MIDI + TRS IN; TRS OUT exists | decided |
| Knob-only controls send no MIDI; MIDI never flips switches | decided |
| CC 1 → mod depth, jump-on-move | decided |
| Clock in → echo (option B) | decided |
| Pan receives CC 10 (now DRY PAN) | decided; reconsideration open (Q1) |
| Channel pressure out (+ in) | decided feature; behaviour eng |
| Not a MIDI controller; send only if free; DAW-first | decided (stance) |
| Note merge, priority, note mapping, velocity path, PB ±2 + RPN 0, CC 64, CC 120 / 121 / 123 behaviour | proposed |
| CC map (5, 74, 20–25, 102–105) | proposed |
| Channel default + combo | proposed / open (Q3) |
| Extras X2–X5 | proposed, off by default / open (Q4) |
| jobs.md F7 step 7 (knobs send) | superseded by this doc |
