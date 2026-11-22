# floss: visual designer notes

## Where things stand (2026-11-22, after jam pass 2, turn 6; the jam is closed)
- I wrote jam turn 2 (pass 1) and turn 6 (pass 2, the last turn) in `../jam.md`.
- Sketches:
  - `../sketches/visual-jam1-sail.png` (pass 1: SAIL, the half-map, the rose, the lighthouse status codes; partly superseded);
  - `../sketches/visual-jam2-faces.png` (pass 2: the split about middle C, and the faces of BOW, KEPT and TIDE).
  - Sources: `visual_jam1.py` and `visual_jam2.py` in the same folder (`python3 -I <file>`; needs matplotlib). They're rough, not layouts.
- Next is the director's ruling, then concept folders in `../concepts/` with systems. Nothing in `handoff.md` yet.

## The family's visual language (what floss inherits)
- **CATHEDRAL (Big Energy's current case):**
  - case: FOLD-format walnut; superellipse corners (n = 5; 24 mm on the plates, 28.3 on the case); cream plates;
  - colour: brass and black ("an organ console's fittings");
  - keys: brass mushroom-plug keys, black sharps, on an interchangeable carrier (tenon 9.53 × 3.2);
  - lid: stands at about 120° on brass stays; slotted lancet speaker window;
  - back: a pipe façade on the lid's back (the owner draws those lines himself); a walnut bookcloth spine with brass lines.
- **ONE SHEET:** one printed cream shell, one filament, one swap; "if it turns, it ripples" (concentric first-layer rings round rotaries).
- **HUSH:** a printed pebble with one grey wool-felt skin; maple pegs on punched felt collars; words pressed blind; tags under the knobs.
- **Panel grammar:** one-word lowercase labels in Kalam, the word above its control; one tick ring per knob; stepped knobs show only their detents; one heading style; a MIDI dot.
- **Owner rules carried from Big Energy:** nothing raised in the knobs' way; off-centre in the middle reads badly; signal order synth → effects → output; one plain word per label; one accent (Big Energy's red CUTOFF); he loved HUSH's pegs ("organ like"). Reversed key colours was a question asked on Big Energy that he hasn't answered.

## Randomness used
- Pass 1: Oblique Strategies "Use an old idea" and "Go slowly all the way round the outside"; fields lighthouse optics and kite making; twist "designed for a child's hands"; thread colour **coral**.
- Pass 2: no new draw (the director's "Listen to the quiet voice" shaped TIDE's face).

## Decisions so far (proposed by me; the director hasn't ruled yet unless noted)
- **Concepts going forward (director, turn 5):** BOW, KEPT, TIDE. WIND is killed (systems and the director); the swell-box lid is killed.
- **Each concept takes a different family body:** BOW = CATHEDRAL with the lid as soundbox (SAIL); KEPT = ONE SHEET slab; TIDE = HUSH felt pebble. *Why:* they differ in kind, the choice is real, all three are reuse, and it guards against convergence.
- **Off-centre split:** the axis runs through middle C (25 keys = 7 whites + C + 7 whites). An 18 mm gutter over middle C; 126 mm of controls each side; no line through the face; a coral tick on the front rim between B and C is the only split mark. The gutter carries what's shared (the status light, BOW's strand names, TIDE's HOLD and DRIFT). Compromise: middle C belongs to the right half but sits under the gutter. Rejected: a line through the face, keys shifted 9 mm (case +18), an asymmetric case, and 24 keys (an owner trade only if the tick fails).
- **Coral marks where the life lives:** BOW = pressure, KEPT = ensemble, TIDE = drift.
- **Keys:** BOW dark naturals with bone sharps on felt collars; KEPT white and black; TIDE HUSH's maple pegs on felt.
- **Speakers:** BOW cloth lid, plain; KEPT slotted back band (radiator probably lost: an honest trade); TIDE punched felt holes with the lantern glowing through them.
- **Lantern only in TIDE.** It never signals state. Systems verified the three phases (0°, 120°, 240°; Sound on Sound).
- **Status light:** three meanings (steady = fine, slow pulse = charging, flashing = low battery), on the axis.
- **Words:** the knob is **attack** (pairs with release); **swell** stays a pressure position; pressure = *swell · vibrato · tone · shimmer*; BOW strands = heading **strands**, *low · main · high*; octave positions as numbers (*−1 · 0 · +1 · +2*, range systems'); KEPT tabs *bass · strings · brass*; KEPT uses attack and release, not "crescendo" and "sustain".

## Dropped (and why)
- Pass 1: a CATHEDRAL clone, f-holes, pastels, a translucent body, a diamond kite outline.
- Director, turn 3: ROUNDS / BELFRY, STOPS, BIG HANDS, LUTHIER, the flower-of-life rose, five lighthouse rhythms, the label SET.
- Turn 6:
  - **the rose in any form**: the lid needs no hole, and a motif fights the owner's own façade;
  - **the coral line through the face**;
  - **the lantern in BOW and KEPT**;
  - **organ feet and orchestral switch names**;
  - **maple keys for BOW** (maple moved to TIDE).

## Director's objections so far (turns 3 and 5)
- Convergence: one concept under many names. My answer: three bodies, three key materials, three heroes.
- The rose read as the flower of life: dropped.
- Off-centre: answered with the middle-C gutter, pending a ruling.
- Jargon labels: answered.
- "Smaller CATHEDRAL?" for BOW: answered by the lid's job and the dark keys.
- Settled asks going idle: that one is systems' and the director's (TIDE's per-note planting); the face supports it (HOLD as a peg; DRIFT as hero).

## Open questions
1. **Director:** is the rim tick enough to show middle C is on the right?
2. **Systems:** does BOW's stacked strand column fit CATHEDRAL's base depth? (Fallback: tabs side by side, names above each group.)
3. **Eng:**
   - BOW's lid box: driver plus radiator in ≈ 20–24 mm; leads through the hinge; a Hall-sensor power switch;
   - KEPT's sealed volume;
   - TIDE's radiator direction;
   - whether the lantern reads through the felt holes in shade;
   - whether a felt collar helps or blurs per-key pressure.
4. **Owner (later):** BOW's reversed key colours; open-lid = on.
5. **Systems / eng:** KEPT's tab count and names; the octave range.

## Next
- Read the director's ruling. Build `concepts/bow/`, `concepts/kept/` and `concepts/tide/` with systems: how each looks and feels, at a fidelity the director can judge, plus each concept's coverage of `jobs.md`.
- Render properly in the family's style (standing, closed, flat; BOW closed beside CATHEDRAL), laid out on CATHEDRAL's 5 mm module (20 mm between knobs in a group; 15 mm between groups and to the plate edge). Use Kalam in final renders: Big Energy's notes say the GitHub fonts URL was blocked here, so find another source or flag a stand-in.
