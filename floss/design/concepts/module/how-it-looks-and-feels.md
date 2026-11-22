# floss module: how it looks and feels (shared by FALLBOARD, SPINE and YOKE)

Status: **rev 3, 2026-11-22**, product designer (visual focus), visual turn 3. Brought to the director's steer 2 (S2 knob A baseline with B as a column; S3 walnut-brown house; S4 stage ends behind the rear row with a roof, and a fair arc with two facets), to `floss/eng/module-r3.md` (speaker E, grille, rake ≥ 63°, ASA, knob stock) and to systems' `how-it-works.md` rev 3. **Rev 2's near-black house and its "stage blacks and spike marks" story are withdrawn** (the director: a random draw isn't the product's story).

**Picture:** `module-1to1-A2.png` (and `.pdf`): **1 : 1 on A2**, A (baseline) beside B: plan, front, rear, a section through a driver; the colour idea, the divider at 4 : 1, the knob note. Print at 100 % (the 50 mm bar). Source `../_src/r3.py` (`python3 r3.py module`, from `_src`).

Marks: **[r3]** `module-r3.md` · **[calc]** · **PROPOSAL** · **UNVERIFIED**.

---

## 1. The idea the colour comes from
**A string machine is a piece of furniture you play:** a warm wooden house with a lit keyboard of controls in it (the Solina, the home organ). So:
- **The house is warm walnut-brown**, printed from the spool (ASA recommended [r3], PETG as the fallback). Warmth is the owner's word; the family is walnut and cream (director S3). It's a brown filament, not imitation wood grain: no paint, no texture pretending to be timber.
- **The stage is cream, and only where the hands work.** The cream deck now ends at the crown foot (A: y 41, 5 mm behind the rear knobs). **Behind it the house rises as the roof**, level with the rim, and carries the speaker. Rev 2's empty cream shoulders are gone (director S4.1).
- **Marks are cream on brown:** the rail's ticks, the target, the words on the roof's raked edge, the wordmark on the rear.
- **Knobs: gold knurled aluminium.** Tayda's 3010 Ø 10 × 8 is in stock in gold; black isn't until 3 Jan 2027 [r3]. Gold on cream in a walnut house brings back the family's "more brass than black" honestly, as a bought finish. **My call; the director or owner can overrule** (silver is the other listed colour, 4 in stock [r3]).
- **Black only for what you flip or press:** the strand tabs, HOLD, TAP's cap, the FREE / SYNC toggle, and the TPU dividers.
- **One coral (DEPTH). Amber light** (TAP's ring, the port light).
- **The alternative for the owner, in one line:** "the same system with a near-black house: more like every other synth, cooler-looking, and hotter in the sun."

| Part | Material and colour |
|---|---|
| Shell, roof, crown lid, every printed carry part | walnut-brown ASA (or PETG), matte. The exact filament shade is UNVERIFIED (brown ASA is sold by several makers; the print notes must name one) |
| Deck (the stage) | cream ASA/PETG; its words printed in the house brown (second filament) |
| Marks on brown | cream (multi-material print); **one-spool fallback (Adam's own printer): debossed 0.6 mm**, not the baseline (S3) |
| Knobs | gold anodised aluminium, Tayda 3010 Ø 10 × 8 [r3]; **DEPTH coral** (no coral 3010 found: a coral anodised Ø 10 from another maker, or a printed coral knob of the same envelope, both UNVERIFIED) |
| Tabs, HOLD, TAP, toggle | black (bought parts) |
| Dividers | black TPU 95A strip, flush (§4) |
| Lights | amber |

## 2. Size, ratio, outline (A baseline; B as a column)
| | **A (baseline)**: Ø 10 × 8 | **B (owner's column)**: Ø 14.5 × 13.5 |
|---|---|---|
| Body | **280 × 105 × 35**; 105 holds with speaker E's ≈ 4 % volume margin; **≈ 115 if it doesn't** (dashed on the sheet) [r3] | 280 × 112 × 42 drawn; with E systems expects 112–120 |
| Deck · knob tops · rim | 25 · 34 · 35 [r3 §1] | 26.5 · 41 · 42 |
| Rows | y 14 / 31 | y 14 / 35.9 |
| Stage ends (= crown foot) | y 41: **5 mm finger room** | y 48.4: 5 mm |
| Ratio | **8 : 3 : 1 on the 35 unit** (at 105) | found after the fact (the director's objection); rev 2's 14-unit story is withdrawn |
| Kits | as drawn | +7 mm thick; FALLBOARD 412 × 272 |

- **Outline (S4.2): one fair arc from the 70 mm ends to the full depth on the axis, and exactly two flat port facets.** The facets are now **chords set under the roof's lip**. In plan the outline stays one unbroken arc (the facets show dashed); from behind you see the arc run along the top and two flat bays beneath it holding the jacks. Rev 2 drew the facets as the outline itself, so the rear read as a gable; this keeps the flat walls the jacks need without breaking the curve. The volume between chord and arc is the same either way (≈ 4 cm³ a facet [calc]), so E's box loses nothing by it. ENG: the lip's overhang (≈ 2–3 mm) at the facets' centres.
- Front: straight, r 10 corners. Ends: straight, 70 deep. Symmetric about the axis.

## 3. The roof and the crown (speaker E)
- **The roof** is the speaker box's lid (systems: not decoration). It runs the full width behind the stage at rim height. **Its front edge is raked ≥ 63°** (rising 10 in 5 [r3 §3]); on the sheet it's a slightly darker band of the same brown, because a steep face catches less light.
- **All rear-row words sit on that raked edge, cream on brown** (low · main · high, pressure, release, drift, shimmer, time, free·sync, reverb). On a 63° face they face the playing seat. Front-row words sit on the cream stage, in brown.
- **The crown** is the speaker box's own airtight printed part [r3 §5]: **≈ 125 wide on the axis**, set into the roof with a hairline seam. Its lid holds **two grilles**, each a **Ø 46 field of Ø 2.0 holes on 2.6 hex pitch** [r3], one over each driver (x 140 ± 31, y 73). Counted in `r3.py`: **259 holes ≈ 814 mm² per driver** (≥ 620 each, and still ≥ 620 if the holes print at Ø 1.8).
- **Wordmark "floss"**, cream, on the rear face between the facets (R4).

## 4. Panel, at 1:1 (systems' map, rev 3)
- Seven groups mirrored about the axis; stop jambs at each end; coral DEPTH on the axis.
- **Knobs gold**, pointer line in the house brown. **Stepped controls are now firmware-stepped 9 mm pots** [r3 §1] (OCTAVE ×2, PRESSURE, SHIMMER). **Their tick rings are now the only sign of a step** (five ticks on OCTAVE, four on the kinds): you see and hear the step, you don't feel it. A feel trade-off for the owner (systems §13).
- **Tabs:** black mini rockers. **HOLD:** black rounded-square latch with a cream dot. **TAP:** black in its amber ring. **FREE / SYNC:** black bat.
- **Dividers: pressed-in black TPU 95A, 1.6 × 2.0, flush**, across the stage from front edge to rear edge. **Black, not brown** (the one line S3 asked for): black TPU is the stock colour, and on cream it reads as a drawn rule, the same black as the parts you touch. With a split print, the shell's seams at x 74.5 / 205.5 hide under two of them [r3 §6a]. Fallback: a printed groove 1.0 × 0.4.

## 5. Front, rear, underside
- **Front:** brown; cream ticks inlaid in the rim; the **cream target** rides it. **The USB-C host port sits in a recessed pocket** (≈ 16 × 10 opening, ≈ 25–30 deep: systems §4 from [r3 §7]), so the straight plug disappears into the module; the **amber port light** beside it. No words.
- **Rear:** the roof's arc along the top; two flat facet bays in a darker brown (shadow, same filament): plan-left power · USB-C · tune · split; plan-right phones · line · MIDI in · MIDI out; small cream port names; the cream wordmark between.
- **Underside:** the two ¼"-20 inserts (S4), bosses Ø 16–18; four feet (printed sockets, so YOKE's cap can peg in: systems).

## 6. Feel, motion and feedback (every state in systems' §7–§8)
| State | What you see or feel |
|---|---|
| Off | dark; a brown object with a cream stage; knobs turn |
| On | the recessed slide clicks; TAP's ring **steady amber** |
| Keyboard in | port light **steady amber** |
| Playing | port light **winks per note** |
| Silent, keyboard connected (job 29) | steady, no wink = notes not arriving; winks but silent = VOLUME, then the tabs (all three down = that half off), then phones |
| Fault / charger in the host socket | port light **flashes fast** |
| Unplugged mid-chord | port dark; held notes sound on |
| HOLD on | the latch sits low, its cream dot below the knob line |
| HOLD on, keyboard gone | HOLD low, port dark, the drone continues |
| Octaves split | the octave pointers aren't parallel; with firmware steps, each pointer sits on a tick |
| Charging | ring pulses slowly |
| Low battery | ring flashes fast (over everything) |
| SYNC, no clock | ring blinks the tempo (over charging) |
| Headphones in | speaker mutes |
| Shimmer | coral DEPTH at the centre; no light |

## 7. Open questions
1. **Owner:** knob A or B; walnut-brown (or black); gold knobs; firmware steps with no detent feel.
2. **Eng:** the coral DEPTH knob; the brown ASA shade; the roof lip at the facets; whether 105 holds with E.
3. **Director:** gold knobs (my call, from stock and the family's brass); the darker band on the roof's rake (same filament, shading only).

## 8. Why (for the handoff)
- **Brown house, cream stage, roof:** the lit surface is only where the hands work; the house rises to carry the speaker, which is what the box behind the controls is.
- **One arc, facets under its lip:** printing makes curves free; the jacks still get flat walls.
- **Gold knobs:** in stock, a family echo, an honest material.
