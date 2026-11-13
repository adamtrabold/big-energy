# Daisy Seed switch: what changes for the design team (2026-11-13)

Source: `budget-variant.md` rev 13 §v1.11. Seed figures marked UNVERIFIED have not been read from an official drawing; the spike measures them. Subsystem details are pending `daisy-first-principles.md`.

1. **Module footprint and socket.** Seed is 51 x 18 mm (51 and 18 appear on the datasheet drawing, labels unreadable), 2 x 20 pins at 0.6" row spacing. The Pico 2 was 51 x 21 at 0.7". Different socket, slightly smaller courtyard.
2. **Height (UNVERIFIED).** The drawing lists 8.4 and 8 mm; seated height in a socket is unknown. The 8 mm underside stack limit (flat concepts) may be exceeded. Hold z until one is measured.
3. **USB connector position (UNVERIFIED).** The Seed's USB (Seed3 USB-C) sits on the module and carries MIDI and DFU. E3's pad-wiring trick (D+/D- to Pico test pads) does not exist. Plan the rear edge for the module's connector facing out, or an extension cable, plus a service opening. A single rear USB-C may still work via header D29/D30 (spike decides). Do not tie breakout VBUS to the Seed.
4. **Power.** About 2.4-4.4 W (was 2.0-3.6). Runtime: 22.2 Wh about 3.9-7.5 h; slim 11.1 Wh about 1.9-3.7 h. The 1 A boost is too close at 4.4 W: swap to a 2 A+ boost (+$6-12, battery builds).
5. **Thermal.** The Seed adds 0.4-0.8 W in a small area. Keep it at least 30 mm from the ladder, AS3046s and tempcos, and away from the windows in UNDER GLASS.
6. **Panel.** ECHO + REVERB section: 5 pots, 2 four-way rotaries, 1 TAP button (8 controls, owner-approved) plus a DRIFT knob (placement open). Mux use about 46 of 48.
7. **Board area.** About +2,000 mm2 courtyard; main board likely 268 x 120-126. In FOLD, put the Seed and wet path in the base (about 1 mm of depth per 262 mm2 in the lid).
8. **Jacks.** Optional TRS MIDI out is now free. EXT audio in and the dry path are unchanged (dry stays analog).
9. **Cost.** About +$39-50 per unit on USB (totals about $311-395); with the 22.2 Wh pack and bigger boost about $356-448.
