# Architecture: the whole device on one page
Status: **started 2026-11-13** (systems) · sources:
- owner record: [`../design/owner.md`](../design/owner.md);
- master spec: [`../eng/budget-variant.md`](../eng/budget-variant.md) rev 14;
- Daisy design: [`../eng/daisy-first-principles.md`](../eng/daisy-first-principles.md) (DFP);
- [`../eng/aftertouch.md`](../eng/aftertouch.md);
- [`../design/branches/echo-clock.md`](../design/branches/echo-clock.md);
- CATHEDRAL: [`../design/branches/concepts/cathedral/how-it-works.md`](../design/branches/concepts/cathedral/how-it-works.md);
- expert review: [`../design/reviews/2026-11-13-audio-synth-review.md`](../design/reviews/2026-11-13-audio-synth-review.md).

Words: **decided** = recorded in owner.md · **proposed** = team or review, awaiting the owner · **open** = unknown or unchosen. **[ENG]** eng figure · **[CALC]** arithmetic · **UNVERIFIED**.

---

## 1. System overview
A portable, battery-powered **analog Model D-style mono / paraphonic synth** with **one digital brain** (Daisy Seed) for control, tuning, MIDI and **digital echo + reverb**. The dry voice is **analog and never converted**. The effects return wet-only and are mixed back in analog.

```
 keys (Hall) ─┐                     ┌─► MCP4822 ×4 ─► VCO 1–3 pitch (coarse+fine), keytrack, CUTOFF CV
 pots/switches┼─► 3 (→4) muxes ─► Daisy Seed ─┼─► Seed DACs ─► velocity CV, mod-depth CV
 FSR (AT) ────┘   (ADC1/2/3)       │  ▲        ├─► gate out, LEDs, enables
 VCO 1–3 ───────────────► TIM5 ────┘  │        └─► USB-MIDI / TRS MIDI out
 MIDI in (USB, TRS) ──────────────────┘
                                      codec IN L ◄── post-VCA send      codec IN R ◄── ladder tap (filter cal)
 VCO 1–3 + noise/EXT ─► mixer ─► ladder ─► VCA ─┬─► dry ─► output sums ─► VOLUME ─► phones / line / LM386 + speaker
                                                └─► FX send ─► Daisy: echo → reverb ─► codec OUT L/R (wet) ─┘
```

## 2. Signal paths
| Path | Route | Status |
|---|---|---|
| **Analog voice** | 3 VCOs (AS3046 expo) → mixer (OSC 1–3, NOISE / EXT, SOURCE) → 4-pole ladder → AS3360 VCA (analog contours) | decided (locked spec) |
| **Dry** | VCA out → output sums, **never switched, never converted** | decided (DFP §6.1, owner: "Delay and verb can be digital") |
| **FX send** | post-VCA → TL072 (−6 dBFS, soft clip, AA) → codec IN L. **Gate-aware mute** (DFP §6.2) → **review item 8: gate on level instead** (proposed) | send decided; gating proposed |
| **FX** | echo (TAPE / BBD / CLEAN / PING-PONG) → reverb (PLATE / HALL / SPRING / SHIMMER), stereo wet out | decided ("Full 8") |
| **Wet return** | codec OUT L/R → summing R → output sums. **Wet only** (no dry copy, so no comb filtering) | decided (DFP) |
| **Outputs** | stereo **phones** + stereo **line out** (TRS); **one speaker** (mono sum via LM386) | decided (15:22, 15:23) |
| **Mono on TS** | a TS plug in the stereo outputs carries L + R on the tip | decided as a requirement (15:24); method **open** (open item O2) |
| **Pans** | **dry pan** on the analog dry (digipot, proposed), **delay pan** in DSP, **FOLLOW** link (delay follows dry) | pans and FOLLOW decided (15:53, 15:54); implementation proposed (cathedral §15.5) |
| **Filter cal** | ladder tap → codec IN R | decided (DFP §2) |
| **PARA+4 4th oscillator** | **no audio path specified** | **open (O3, review MUST)** |
| **PITCH CV OUT** | **no DAC channel assigned** | **open (review item 9)** |

## 3. Control and data flow
- **Scan:** a timer-paced 8–10 kHz frame. Keys on ADC1 + ADC2 (simultaneous, through muxes A / B); controls on ADC3 (mux C); 4× oversampling (DFP §1, §3). Controls go through average → 1 kHz → 1-pole → deadband.
- **Jump-on-move** (decided): MIDI or a stored state takes a marked knob; the "not in control" LED lights; moving the knob > 1.5 % takes it back.
- **Owner rules** (decided): knob-only controls send no MIDI; **MIDI never flips switches**.
- **Pitch:** firmware sums key note, RANGE, FREQ, glide, bend, DRIFT and the held-note loop correction into coarse + fine DAC pairs per VCO (DFP §2.3, §4).
- **FX controls** are read by the Daisy (mux). TYPE rotaries are ladders. TAP is a mux channel (and the boot / settings gestures: open item O6).
- **MIDI:** USB-MIDI (Seed's own port via the rear USB-C) + TRS in (6N138) + TRS out (decided: "Add MIDI out"). Clock from both feeds the echo tempo. See [`features/midi.md`](features/midi.md).

## 4. Power
- Internal LiPo (decided), single rear USB-C for charge + MIDI + firmware (decided).
- **Draw** [ENG, ESTIMATE, DFP §7.1]: ≈ 2.0–3.6 W total. On the 22.2 Wh pack ≈ 6.0–7.8 h (low end) / 3.7–4.3 h (high end). **FOLD-105's slim ≈ 11 Wh** pack gives about half: ≈ 1.9–3.9 h [CALC].
- **Not yet counted:**
  - **speaker playback** (review item 20: ≈ 0.5–0.8 W loud, UNVERIFIED);
  - the stereo stage's headphone driver quiescent current (review: it runs always unless switched).
- Hall group gating (≈ −0.45 to −0.95 W, bench-gated) is the biggest saving.

## 5. Budgets — one recounted table (2026-11-13)
### 5.1 Mux channels (16 per CD74HC4067)
Baseline from `aftertouch.md` §2 (corrected tally):
- mux A = keys 1–16;
- mux B = keys 17–25, 4 controls, Hall-rail monitor, AT toggle, AT FSR;
- mux C = 16 controls.

**48 / 48 used.**

| Item | Channels | Status | Running total |
|---|---|---|---|
| Baseline (25 keys + 20 controls + Hall-rail monitor + AT toggle + AT FSR) | 48 | decided features | 48 |
| PARA toggle (MONO / PARA / PARA+4) | +1 | decided (paraphonic approved) | 49 |
| FREE / SYNC toggle | +1 | decided (11:58, "B") | 50 |
| DRY PAN pot | +1 | decided feature (15:53); pot read proposed | 51 |
| DELAY PAN pot | +1 | decided feature (15:53) | 52 |
| FOLLOW toggle | +1 | decided link (15:54); toggle form proposed | 53 |
| OSC 3 CTL read by firmware | +1 | proposed (review 11) | 54 |
| PHONES-inserted sense (speaker mute) | +1 | proposed (review 16) | 55 |
| TS sense on LINE OUT | +1 (0 if two jacks) | proposed; method open (O2) | 56 |
| Battery divider moved from D20 onto a mux | +1 | proposed (review 1) | 57 |
| Charger STAT + VBUS moved onto a mux (frees D29 / D30) | +2 | proposed, optional | 59 |
| **Capacity with a 4th mux (D20, ADC3)** | **64** | **proposed (O1)** | **57–59 of 64** |

**Not counted as channels:** RANGE as detented rotaries (same channel, review 13); VOLUME's second gang (analog).

### 5.2 Daisy Seed pins (31)
DFP §9 tally: 27 required + 3 optional + 1 spare.

| Change | Pins | Status | Total required |
|---|---|---|---|
| DFP §9 required | 27 | decided design | 27 |
| D13 TRS MIDI out (was "optional") | +1 | decided ("Add MIDI out") | 28 |
| 4th mux on D20 (ADC3); battery moves onto it | 0 net | proposed (O1) | 28 |
| Digipot CS (dry pan) | +1 (D29, if STAT goes to the mux) | proposed | 29 |
| 74HC4053 control (TS mono, fix (b)) | +1 (D30, if VBUS goes to the mux); 0 with two jacks | proposed / open (O2) | 29–30 |
| Output mute (phones / line) | 0 (shares D12 with the LM386 enable) | proposed (review 7) | 29–30 |
| **Spare** | **D16** (+ D30 if fix (a)) | | **29–30 of 31** |

### 5.3 DAC channels
| Channel | Use | Status |
|---|---|---|
| MCP4822 #1–#3 (6 ch) | VCO 1–3 pitch, coarse + fine (fine at 1/64) | decided design (DFP §4) |
| MCP4822 #4 A | keytrack | decided design |
| MCP4822 #4 B | CUTOFF (+ aftertouch FILT, + velocity FILT, summed in firmware) | decided design |
| Seed DAC1_OUT1 / OUT2 | velocity CV / mod-depth CV | decided design |
| TIM3 PWM (D4) | static VCA balance | decided design |
| **PITCH CV OUT** | **none assigned**: review 9 proposes sharing #4 A, buffered to 1 V/oct ahead of KBD CTRL | open |
| **PARA+4 4th oscillator audio** | **none**: codec OUT L/R are the wet return | open (O3) |
| Dual digipot MCP4251-103 (proposed) | dry pan (analog audio) | proposed (cathedral §15.5) |

### 5.4 Codec (stereo in / out)
IN L = FX send · IN R = filter cal · OUT L / R = wet return. **Fully used**, which is why PARA+4 has no path (O3).

## 6. Decisions log (owner.md, newest last; verbatim lives there)
| When (owner.md) | Decision |
|---|---|
| 2026-11-12, "Decisions already made" | USB-MIDI + TRS MIDI in; MIDI-controllable params per eng; **knob-only controls send no MIDI; MIDI never flips switches**; mod depth MIDI-controllable (jump-on-move) |
| 2026-11-12 22:30 → 11-13 | Echo **and** reverb, digital allowed, great models, several types; **full 8 FX controls**; **Daisy Seed**; DRIFT controllable; **MIDI out** added; channel **aftertouch** with its own switch, sent on MIDI out; **paraphonic** MONO / PARA / PARA+4 |
| 2026-11-13 11:58 | Echo sync **option B**: FREE / SYNC toggle by TIME |
| 2026-11-13 14:12–14:41 | CATHEDRAL (CHAMBER + FOLD); no spine; **no machining**; keys printed or bought; external and metal printing OK |
| 2026-11-13 15:22–15:24 | **Stereo phones + stereo line out, one speaker**; **mono on the tip with a TS cable** |
| 2026-11-13 15:44 | the (then single) pan **receives CC 10** |
| 2026-11-13 15:53–15:54 | **Dry pan + separate delay pan**; linked = delay **follows** dry |
| 2026-11-13 16:21 | **Architecture + feature docs**, one at a time; MIDI stance: "pretty definitively not a midi controller", send only "if it's free" |
| 2026-11-13 (latest) | MIDI organising principle: **played and automated from another device, mainly a DAW**; sending only if free |

## 7. Open items (must-fixes from the expert review, plus related)
| # | Item | Why | Proposed fix | Owner / eng |
|---|---|---|---|---|
| **O1** | **Mux full:** ≈ 54–59 needed vs 48 (§5.1) | no channels for SYNC, pans, PARA, sensing | **4th CD74HC4067** sharing S0–S3 on **D20 (ADC3)**, battery divider onto it. ADC3 converts mux C + D per step. ≈ $0.60. **Eng: confirm two ADC3 conversions fit the ≈ 3 µs step (UNVERIFIED)** | eng |
| **O2** | **TS sensing on LINE OUT can't work as drawn** (cathedral §15.4): a 100 Ω-driven ring never reads high; adding a coupling cap thumps a mixer on plug-in; a TS plug shorts the live R driver | the decided mono-on-TS requirement has no working circuit | **(a) two jacks, L / MONO + R** (the R jack's switch normals R into L; analog, no pops; +1 hole, not a patch point), **or (b)** one TRS with a ≤ 50–100 mV ring bias, 470 Ω–1 kΩ build-outs, and a 74HC4053 that cuts R and sums into L. Either way, line build-out 470 Ω–1 kΩ. **(a) needs the owner** (one more hole against "no new jacks") | owner (a) / eng (b) |
| **O3** | **PARA+4's digital 4th oscillator has no audio path** | an approved mode can't sound | (a) the 4th osc on codec OUT R → NOISE / EXT input (through the ladder), wet goes mono in PARA+4; (b) re-plan the Seed DACs; (c) make the toggle 2-way until a path exists | owner |
| **O4** | **Peg necks vs the floating key strip:** deck hole clearance 0.4 / side vs aftertouch's ≥ 1 mm | rubbing steals aftertouch force, changes velocity, squeaks | deck hole ≥ Ø 13.2 (the 12.7 head no longer covers it: a dark ring shows), or a slimmer neck (≤ Ø 10.7 with a Ø 12.7 hole; the tenon cup's wall is then ≈ 0.55 mm, thin for FDM, UNVERIFIED), or a positive strip locator that carries no vertical load | visual + eng |
| **O5** | **TAP gestures collide:** "hold TAP at power-on" = full autotune **and** DFU; "EMPHASIS full + hold TAP" = filter cal live; "hold TAP" = battery | an accidental bootloader; a filter cal mid-song | DFU = hold TAP + bend stick up at power-on (or the Seed's BOOT button behind the service panel); autotune keeps "hold TAP at power-on"; filter cal **at power-on only**; battery = double-tap-and-hold or shown at boot | owner (gestures) |
| O6 | Ghost 74HC595 in cathedral §15.4; budget-variant §v1.11.6 pin list superseded by DFP §9 | schematic capture could put the LDO enable on a DAC pin | mark §v1.11.6 superseded; drive the 4053 from D29 / D30 (§5.2) | eng |
| O7 | Phones / line unmuted at power-on, off and the boot VCA null | thumps in headphones and a PA | shunt mute on phones L / R and line L / R, held at reset, released after boot cal + 200 ms (shares D12) | eng |
| O8 | PITCH CV OUT unassigned; OSC 3 CTL not read; KBD CTRL can't reach full | locked I/O without a source; LFO mode and PARA can't work right | review items 9, 11, 12 | eng / owner |
| O9 | Speaker draw not in the power budget; loudness outdoors | runtime and the park | count it; bench with the real grille; consider PAM8302 | eng |
| O10 | MIDI: CC map, channel, local off, DAW echo, CC 10 at project load | DAW workflow (owner's priority) | [`features/midi.md`](features/midi.md) | owner |
