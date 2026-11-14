# Panning and stereo outputs
Status: **written 2026-11-13** (systems). Per item below. Sources:
- [owner record](../../design/owner.md) 15:18–15:54;
- [CATHEDRAL §15](../../design/branches/concepts/cathedral/how-it-works.md);
- [Daisy design §6](../../eng/daisy-first-principles.md);
- [expert review](../../design/reviews/2026-11-13-audio-synth-review.md) items 2, 3, 7, 16, 17, P3, P5, P6.

## What it does (player's view)
- **Headphones and line out are stereo.** The echo and reverb spread left and right; the speaker plays one mono mix.
- **DRY PAN** moves the synth itself left or right on the stereo outputs.
- **ECHO PAN** moves the echo separately.
- **FOLLOW** makes the echo track the dry pan.
- **A mono cable in LINE OUT** still gets the whole sound.

## Owner decisions (verbatim, linked)
- 15:22 "Stereo phones is fine but I need to pan the signal into the effects" → stereo phones, **one speaker**.
- 15:23 "Stereo line out" → **stereo line out** (TRS).
- 15:24 "Left channel should be mono tho if stereo isn't plugged in" → **a TS cable carries L + R on the tip** (requirement).
- 15:44 "Yea sure on midi" → the pan **receives CC 10**.
- 15:53 "No the pan would be audio signal. Basically I'd like to pan just the delay separately from the full dry but also I'd like to be able to have the pan signals sync" → **a dry pan and a separate echo pan**, with a link.
- 15:54 "Follow dry" → linked = **the delay follows the dry, same side**.

## How it works
```
voice (mono, analog) ─► DRY PAN (dual digital pot, analog audio) ─► L sum / R sum ─► VOLUME (dual) ─┬─► PHONES (TRS, headphone driver)
        └─ FX send (placed where the dry sits, in DSP) ─► reverb in (stereo)                      ├─► LINE OUT (TRS, line driver)
           └─► ECHO ─► ECHO PAN (DSP; = DRY PAN when FOLLOW) ─┬─► L / R sums                     └─► (L+R)/2 ─► LM386 ─► speaker
                                                               └─► reverb in (stereo)
reverb out (stereo) ─► L / R sums
```
- **Summing:** two output summing nodes (one TL072): dry × pan + wet L / wet R. Wet only from the codec, no dry copy.
- **DRY PAN:** the knob is a plain pot the Daisy reads. A **dual digital pot** (MCP4251-103, UNVERIFIED part) forms two complementary dividers, L = a, R = 1 − a (**constant sum**). The audio stays analog (no converter); eng confirms headroom at 5 V (AC-coupled, mid-rail bias) and that it's acceptable in the "never switched" dry path.
- **ECHO PAN:** in DSP. It places the echo's output on the outputs **and** where it enters the reverb.
  - The reverbs take **stereo input**: PLATE / SPRING / SHIMMER get two input diffusers, ≈ +10–15 % of one reverb's load (ESTIMATE; spike measures it).
- **FOLLOW:** a 2-way toggle. FOLLOW = the echo pan takes the dry pan's value; OFF = its own knob.
- **The voice's send into the effects follows DRY PAN** (merged; no separate send pan). Review P1 found a separate send pan mostly inaudible.
- **VOLUME:** a dual-gang 9 mm pot (part and T18 spline UNVERIFIED; cheap gangs mis-track at low settings: a known trade).
- **Phones:** a stereo headphone driver (NJM4556A class, UNVERIFIED). **Line:** a stereo line driver with **470 Ω–1 kΩ build-out resistors** (review 2).
- **Speaker:** the LM386 fed (L + R)/2.

## Controls and states
| Control | Range / positions | Notes |
|---|---|---|
| **DRY PAN** | full L ↔ full R | centre detent if a 9 mm detent pot exists in T18 (UNVERIFIED), else a firmware dead zone ±3 % |
| **ECHO PAN** | full L ↔ full R | inactive while FOLLOW is on |
| **FOLLOW** | OWN / FOLLOWS DRY (panel legend "echo pan: own · follows dry") | a switch: MIDI never flips it |
| PHONES jack | TRS stereo, **switched** (speaker mute) | review 16 |
| LINE OUT | TRS stereo (see the open question on jacks) | mono-on-TS required |

**Placement (proposed, CATHEDRAL layout B effects row):** … ECHO MIX · **ECHO PAN** | REVERB … | **DRY PAN** · VOLUME, with FOLLOW in front between DRY PAN and VOLUME. [CHECK]: 0 violations; label check pending the model.

## Edge cases
- **Speaker:** constant-sum laws, so moving either pan doesn't change the speaker's level.
- **Mono (TS) cable in LINE OUT:** must carry L + R on the tip. **The circuit drawn in CATHEDRAL §15.4 can't work** (review 2). The choice between two working fixes is the owner's (open questions).
- **Mono (TS) plug in PHONES:** you hear L only. A dry panned right is quiet there. Accepted: TS headphones are rare, and a 32 Ω load can't be sensed.
- **Balanced inputs** (most audio interfaces' TRS line inputs) hear **L − R**: the centred dry cancels and only the effects' stereo difference is left (review 3).
  - Print **"stereo · unbalanced"** by the jack.
  - Put a **3.5 mm TRS → 2 × TS cable** in the build list.
- **PING-PONG + ECHO PAN:** PING-PONG already alternates. ECHO PAN sets **which side it starts on**; it doesn't add a second alternation (review P3).
- **Power-on pops:** phones and line get a **shunt mute** held at reset and released after boot calibration + 200 ms. It shares the LM386 enable pin (review 7).
- **Ground loop** with USB-MIDI and line out into one computer: footprints for a ferrite on USB shield/ground; the line-out ground goes to the analog star; the manual says "run on battery or use an isolator to record" (review 17, UNVERIFIED).

## Interactions with other features
- **Effects:** stereo-input reverbs; the echo stays a mono line, and its pan decides where it sits.
- **MIDI:** DRY PAN receives CC 10 (decided; see the CC 10 problem in [MIDI](midi.md)); ECHO PAN receives CC 102 (proposed).
- **Echo sync:** none (no tempo auto-pan; the owner said the pans are audio).
- **Power:** the headphone driver draws quiescent current all the time unless it's switched by the PHONES jack's switch (review).
- **Enclosure:** FOLD's far wall carries PHONES and LINE OUT; one more hole if the owner picks two line jacks.

## MIDI
- DRY PAN: **receive CC 10** (decided), jump-on-move, possible because the digipot is set by the Daisy.
- ECHO PAN: **receive CC 102** (proposed).
- FOLLOW: none (a switch).
- Sending: open (see [MIDI](midi.md)).

## Budget (pins / mux / DAC / power / cost)
- **Mux:** +3 (DRY PAN, ECHO PAN, FOLLOW), +1 PHONES sense, +1 TS sense (0 with two jacks). See [architecture](../architecture.md).
- **Pins:** +1 digipot chip-select; +1 74HC4053 control (0 with two jacks). Output mute shares D12.
- **DAC:** 0 (the digipot isn't a DAC channel).
- **Cost (ESTIMATE, UNVERIFIED):** stereo stage ≈ $3–5; pans, FOLLOW and digipot ≈ $4; 74HC4053 ≈ $0.50 or a second jack ≈ $0.50; mute ≈ $0.30.
- **Power:** a few mA.

## Open questions (for the owner)
1. **Line out with a mono cable: two jacks or one?**
   - **Two jacks, "L / MONO" and "R":** the standard synth way. Plug one cable into L / MONO and you get everything; plug two and you get stereo. It always works, never pops, needs no electronics or firmware, and avoids the silent-on-an-interface problem. **Costs one more hole on the back wall** (not a patch point, just an output).
   - **One stereo jack, made to sense a mono plug:** a reworked circuit with a tiny bias voltage and a switch chip that folds right into left. It keeps one hole, but needs a bench test before we trust it, and a stereo cable into a balanced interface input can still go quiet.
   - **Recommendation:** two jacks.
2. **Should plugging into LINE OUT mute the speaker?** Most players expect yes, to avoid feedback through a PA.
3. **DRY PAN on CC 10:** DAWs send CC 10 = 64 when a project opens, which would centre it on its own. Keep CC 10, or use an undefined CC? (Also asked in [MIDI](midi.md).)

## Status (item by item)
| Item | Status |
|---|---|
| Stereo phones, stereo line out, one speaker | decided |
| TS cable → L + R on the tip (line out) | decided requirement; **method open** (Q1) |
| Dry pan + separate echo pan; FOLLOW = same side | decided |
| Pan receives CC 10 | decided (reconsideration open, Q3) |
| Digipot dry pan, DSP echo pan, constant-sum laws, send follows dry | proposed |
| FOLLOW as a 2-way toggle; placement | proposed |
| Stereo-input reverbs | proposed |
| Switched PHONES jack mutes the speaker; output shunt mute; 470 Ω–1 kΩ build-outs; "stereo · unbalanced" label + Y cable | proposed |
| LINE OUT mutes the speaker | open (Q2) |
