# floss

The string machine: a portable analog string machine. Named by Adam on 2026-11-21: "Call string machine floss".

Status: **next up for build plans**, made the Big Energy way (design loop, first principles, spec, verification) while proving out the shared platform. Which instrument gets built first is undecided.

## What Adam has said (verbatim, 2026-11-21)
- What draws him: "Analog voices, shimmer and warmth"
- "String machine and analog poly are way more inspiring than model d.  We could go back to first principles with string machine too while still proving out the platform"
- "No build decisions is wrong. I want to make build plans like big energy idk what I'll build first is all"

## Decided (Adam, 2026-11-21 22:38)
- **Keys: 25 or fewer.** No extended keyboard: "Portable means 25 or less."
- **Split with octave select for each half:** "it would be nice to octave select each half of the keyboard"
- **Velocity:** "it would be cool to innovate on the original string synth with velocity"
- **Pressure:** look into per-key pressure instead of Big Energy's shared strip ("Yes let’s look to innovate"). Feasibility comes first; it isn't decided yet.
- **Pressure destination is selectable:** "Would be cool to select what the pressure strip does"
- **Battery powered:** "I want to keep it battery powered". Pack size and runtime wait for a power budget, after the voice and shimmer choices.
- **One speaker, muted by headphones**, as on Big Energy: "Yeah one speaker unless headphones just as on big energy". Stereo is for headphones and outputs.
- **Look into a passive radiator** with the speaker ("Passive radiator would be cool"). It needs a sealed air space in the case; to be checked with the enclosure.
- **Shimmer: an analog mode plus Daisy modes:** "Analog mode on shimmer but modes to use the daisy too". Echo and reverb stay on the Daisy.
- **MIDI: Big Energy's rules**, plus a **MIDI split you can turn on or off** (one channel per half), and **velocity and pressure over MIDI** (polyphonic aftertouch if per-key pressure works out).
- **Try it without screens or encoders**, using real bought knobs and keys ("Let’s try without"). The designers have to be strict about which choices get a control.
- **Enclosure: a shared universe with Big Energy, reusing as much as possible:** "Yes let’s make these as a shared universe and reuse as much as we can".

## How string machines work (checked in chat, 2026-11-21)
- A master clock of several MHz feeds a top-octave divider (12 notes), then flip-flops halve each note for every lower octave. Every key has a tone running, so every key can sound at once.
- All notes share one filter and, usually, one envelope. That makes it paraphonic: a new note doesn't get its own attack.
- The raw tone is square-based and thin. A multi-stage bucket-brigade (BBD) ensemble with slow LFOs makes the string shimmer.
- Precedents: Eminent/ARP Solina (1974), Roland RS-202, Elka, Crumar Trilogy (combo synth plus strings). Behringer sells a Solina clone today (~$259).
- Per-note articulation exists (the Polymoog had a VCF/VCA/EG board per note), but it is costly.
- The classic top-octave chips are vintage parts. Modern DIY builds often generate the tones on a microcontroller.

## Ideas discussed, none decided
- Its own instrument, or a minimal "strings" layer inside Port-a-poly (one level knob).
- Ideas for something new: per-key swells, pressure-controlled bowing, drift between notes, sine stacking like the Antiphon.

## Budget
- No fixed ceiling: "Budget ceiling should be what we can to hit the desired goal." Everything still gets costed.

## Design work
- Build-plans design loop started 2026-11-22: `floss/design/`.
