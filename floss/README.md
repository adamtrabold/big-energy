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

## Open (Adam's)
- What else carries over from the Big Energy platform: USB-C charging, built-in speaker, the Daisy with echo and reverb, MIDI rules, no screens or encoders, real bought knobs and keys, enclosure work.
- Budget ceiling.
