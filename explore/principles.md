# The principles we've built up (for comparing other synth clones)
Source: owner decisions across /home/claude/model-d/design/little-d/owner.md and /home/claude/model-d/design/instrument/owner.md.
- Portable, battery powered, internal battery; OP-1-ish footprint as a loose reference; feels good to use.
- Hand-soldered THROUGH-HOLE only; anything SMD arrives as a ready-made plug-in module; no custom factory assembly; bare boards, quantity-1 fab preferred.
- Analog voice (audio path analog); modern pin-compatible equivalents of original chips are fine (no vintage parts).
- Digital brain: Daisy Seed (STM32H750) for control (keys, autotune, MIDI, CVs) + great digital echo and reverb (multiple types). Autotune so there's no manual calibration ("no rigmarole").
- Keys: 25 minimum, velocity required, as silent as possible, real bought parts (Choc V2 silent switches + magnet + Hall sensor), channel aftertouch via pressure strip.
- Bend = one-axis spring joystick; mod control stays put; MIDI in/out (USB + TRS) with jump-on-move for MIDI-controllable params; controllable DRIFT.
- Enclosure: 3D-printed / laser-cut at the owner's makerspace (Vector Space), unibody, screws from the back.
- Verification-first: SPICE golden-reference simulation of the original circuit before fabrication (for the Model D we found CA-72, an open ngspice model of every board), "no rev 2".
- Cost-aware (current Model D-style build ≈ $311–448 one unit). Owner wants "the most interesting thing overall".
