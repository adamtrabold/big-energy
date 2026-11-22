# floss module: how it works (shared by FALLBOARD, SPINE and YOKE)

Status: **rev 3, 2026-11-22**, product designer (systems focus). It folds in:
- the director's steer 2 (S1 YOKE takes CLOTH's place; S2 knob A is the baseline, with B as a column);
- `floss/eng/module-r3.md` (the stack, the knob, the driver, print, cables, and **speaker option E, adopted as the baseline** per the owner's "Speaker let's figure out what will sound best idc method");
- the owner's "25 is good for the string machine" (25 voices, decided).

Rev 2's tables are superseded where this file differs. Read with `../../jobs.md` (rev 3.2), `how-it-looks-and-feels.md` (visual) and `module-r3.md`.

Marks: **[r3]** / **[r2]** from the engineering files · **[calc]** my arithmetic · **PROPOSAL** systems design, not approved · **UNVERIFIED** · **ENG** needs engineering (collected in §11).

---

## 1. What the module is
**floss is a sound module.** It has 25 voices allocated from incoming MIDI, a bucket-brigade ensemble plus Daisy modes, echo and reverb, a 22.2 Wh battery, **two speakers in one ported box** and a panel. It's played by any class-compliant USB-MIDI keyboard on its USB-C host port, which powers the keyboard.
- **It sits in every kit unchanged**, held by its two ¼"-20 inserts underneath (S4). It also works alone (desk, tripod) and with no keyboard (computer, TRS, a planted chord).
- **The case is printed** (owner 14:08): **ASA** recommended [r3 §6] (survives a parked car's seat and sun; it needs an enclosed printer or a service), with PETG as the easier fallback (keep it out of hot cars). The house colour is warm walnut-brown, from the spool (director S3; visual's call). Bought parts: electronics, knobs, switches, jacks, drivers, the threaded inserts and fasteners.

**The honest "analog voices" sentence:** floss's tones start in a microcontroller, one crystal-timed tone per voice, the way the 1974 Solina's started in divider chips. Everything that shapes them is analog: each voice's own keyer and envelope, the octave strands and their mix, the tone filter and the bucket-brigade ensemble. The Daisy modes, echo and reverb are digital, and each one can be switched off.

## 2. Size, ratio and outline (job 30)
"It just needs to be portable and make sense and be harmonious" (owner 13:51). PRINCIPLES §2: sizes come from the parts, and a deliberate ratio tunes them.

**Baseline: 280 × 105 × 35 with knob A and speaker E. The depth is conditional (§2.2).**

| Need | From | Knob **A** (Ø 10 × 8): baseline | Knob **B** (Ø 14.5 × 13.5): for the owner |
|---|---|---|---|
| Panel width | the map (§3): two 34 mm jambs + seven 22 mm columns + six 7 mm gaps = 264, + 8 each end | **280** | 280 |
| Height | rim = deck 25 + seat 1 + knob + 1 [r3 §1] | **35** (knob tops at 34) | **≈ 40–42** [r3: ≈ 40–41; director: 42] |
| Rows | front row y 14; rear row 7 mm behind its edge | **y 14 / 31** | y 14 / 35.9 |
| Crown foot (5 mm finger room) | rear knob edge + 5 | **y 41** | y 48.4 |
| Depth on the axis | the speaker box behind the rear row (§2.2) | **105** (E, ≈ 4 % margin) · **≈ 115** if the margin doesn't hold | ≈ 112 (director) to ≈ 120 with E [calc: B's foot is 7.4 mm further back] |
| Ratio | | **8 : 3 : 1 on one 35 mm unit**, if 105 holds | restated after the fact (the director's objection to B) |

- **Ratio sentence for the owner (A, 105):** "the parts set 280 × 105 × 35; it falls on one 35 mm unit, 8 : 3 : 1, a fourth for each half."
- **If E needs 115:** 280 × 115 × 35 is **8 : 1 in length to height, with the depth set by the speaker**. It is not on the unit, and I'd say so rather than invent a new ratio (director R1: "we don't fake 35").

**The hull outline (plan):**
- **Front edge:** straight, full length (rail, host port, port light). Corners r 10.
- **Ends:** straight, 70 deep. You pick it up by them.
- **Rear:** one fair arc from 70 at the ends to the full depth on the axis, with **exactly two flat port facets** on it (director S4.2: no polygonal chamfers).
- Symmetric about the axis.

**Section:**
- a sunk deck at **25**, the rim at 35 all round;
- a **crown ≈ 125 wide** on the axis, top level with the rim, holding **two grilles** symmetric about the axis (E) [r3 §8];
- the crown's front **raked ≥ ≈ 63°** from its foot at y 41, so the drivers' frames clear it [r3 §3];
- the wordmark on the crown's rear face, between the facets.
- **The cream stage ends a few mm behind the rear row; the house colour rises behind it as the roof to the rim, with the crown in the roof** (director S4.1; visual draws it). Systems note: the roof is the speaker box's lid, so it isn't decoration.

### 2.1 Knob: A is the baseline (director S2)
- **A: Tayda aluminium 3010, Ø 10 × 8, 6 mm 18T, $0.59** [r3, chk]. **Gold: 186 in stock; black out of stock until 3 Jan 2027** [r3]. The colour is visual's (the black / coral question).
- **B: the family 18T push-on, Ø 14.5 × 13.5.** Kept as a column for the owner (above).
- No Ø 14–15 knob ≤ 9 mm tall with a published height exists [r3 §2].
- **The 22 mm pitch stays with A** (a rule for the hand; director S2). The width doesn't reopen.
- **Pots** [r3 §1]: PCB to shaft tip ≤ ≈ 21 mm. Bourns PTV09A-3 is the candidate (its L reference plane is UNVERIFIED). Bushingless pots are held by the board, so the board is fixed to the shell on standoffs and the deck has clearance holes.

### 2.2 Speaker: E is the baseline, D the fallback (owner: "what will sound best"; eng r3 §8)
| | **E (baseline)** | **D (fallback)** | C | A (rev 2) |
|---|---|---|---|---|
| What | **2 × TEBM28C10-4B, mono, one class-D channel each, one ported box ≈ 190 cm³ net**, port Ø 16 × ≈ 140 flared, Fb ≈ 145 Hz, speaker feed high-passed ≈ 115 Hz | the same pair, sealed, 150 cm³ | 1 × TEBM28, ported, 120 cm³ | 1 × TEBM28, sealed, 76 cm³ |
| Gain over A [r3] | **+5.4 dB/W across 150–800 Hz** (80 dB at 1 m for 0.48 W, not 1.66); **+11 / +8 dB** clean headroom; f3 ≈ 152 Hz | +3 dB/W, +6 dB headroom; most robust | f3 140, +6 dB at 100–200 | — |
| Module | **all of the rear region behind the rear row is the box**: cells move to the ends under the jambs; electronics become **two stacked boards in the front band**. **105 holds with ≈ 4 % volume margin; safe at ≈ 115** | crown ≈ 125 wide; holds 280 × 105 × 35 | crown + wings; holds 105 | as rev 2 |
| Cost | +1 driver, 2-channel amp, ≈ +$27–30, ≈ +63 g [r3] | +1 driver | — | — |

- **I draw E at 105 and say plainly that it's conditional.** A 4 % margin on a printed airtight box with a gasketed driver seat, a flared port and ribs is thin. **If eng's detailed box loses more than ≈ 8 cm³ net, the module goes to ≈ 115** (all kits +10 mm in depth; the ratio is restated as in §2), **or the owner takes D at 105.** ENG to settle.
- **What moves with E:** the crown widens to ≈ 125 with two grilles; the rear region becomes one box (no board, no cells behind the rear row); the cells move under the jambs; the board becomes two stacked boards in the front band.
- **Grille:** each driver gets **a Ø 46 field of Ø 2.0 holes on a 2.6 pitch**, ≈ 770 mm² nominal, ≥ 620 even if the holes print 0.2 mm small [r3 §3]. The drawn Ø 1.8 / Ø 43 field fails.
- **The box is its own airtight printed part** (≤ 250 long), with gasketed driver seats [r3 §5, §8].
- **Speaker feed only** is high-passed; phones and line stay full range.
- **No passive radiator** (none publishes its excursion [r3]). The owner's "passive radiator would be cool" is answered by E's port.

### 2.3 Cells, inserts and the family's S4 spacing, ENG + FAMILY CALL
- **E puts the cells under the jambs at the ends.** Eng needs **≥ 2 mm printed-part margins** on every side [r3 §1]. Rev 2's placement beside the crown is withdrawn.
- **The S4 inserts at x 60 / 220 (160 apart) sit close to end-mounted cells** [r3 §8]. Something gives a few mm: the inserts, the cells, or the family's 160 mm spacing.
- **Systems' proposal: keep the family's 160 mm spacing and let the module's insides give way** (the inserts may move in y, and the cells shift). S4 is the interface every carry, every module and a tripod attach to. Changing it changes Big Energy and port-a-poly too, while moving a cell changes only floss. **Director / owner call** (PRINCIPLES §3: the carry and connection are one family standard).
- **Insert bosses Ø 16–18** (Ø 13.5 is the minimum for a standard ¼"-20 heat-set insert, OD 9.5, length 9.5–12.7; Prusa / CNC Kitchen 20-pack $11.99 [r3 §5, chk]).
- **Everything that attaches by S4** (FALLBOARD's and SPINE's thumbscrews, YOKE's arms, a tripod) follows wherever the inserts land. Only the y coordinate would change if the spacing holds.

## 3. Panel map (two rows, family pitch; knob A)
**Rules:**
- **Pitch** 22 mm within a group; ≥ 7 mm between knob edges.
- **Group gaps** add 7 mm, with a **flush divider** at each gap's centre: pressed-in black TPU 95A strip, or a printed groove as the fallback (director S3).
- **Each end owns its half.** Coral on DEPTH, on the axis.
- **Amounts in the front row; kinds, times and set-then-left in the rear row.**

x from the left end, **axis x = 140**. **Front row y = 14, rear row y = 31** (A).

| Group | x | Front row | Rear row |
|---|---|---|---|
| **Jamb L** | 25 | OCTAVE L (5 steps, −2 … +2) | strand tabs **low · main · high** (3 mini rockers, 34 wide) |
| *divider* | 45.5 | | |
| **Touch** | 60 | **HOLD** (latching) | **PRESSURE** (4 steps: swell · drift · tone · shimmer) |
| *divider* | 74.5 | | |
| **Voice** | 89 | ATTACK | RELEASE |
| | 111 | TONE | DRIFT |
| *divider* | 125.5 | | |
| **Shimmer (axis)** | **140** | **DEPTH (coral)** | SHIMMER mode (4 steps: analog · wide · glass · tape) |
| *divider* | 154.5 | | |
| **Echo** | 169 | ECHO (level and repeats) | TIME |
| | 191 | **TAP** (its lit ring is the status light, §7) | FREE / SYNC (toggle) |
| *divider* | 205.5 | | |
| **Out** | 220 | VOLUME | REVERB |
| *divider* | 234.5 | | |
| **Jamb R** | 255 | OCTAVE R | strand tabs **low · main · high** |

- **Width:** 222 + 42 = 264, + 2 × 8 = **280**. The dividers mirror.
- **Rear row:** the tabs (15 deep) span **y 23.5–38.5**. The rear knobs' rear edges are at 36, and the crown foot is at 41.
- **Count:** 13 round controls, HOLD, TAP, FREE / SYNC, 6 tabs, 2 lights.
- **Stepped controls are now firmware-stepped 9 mm pots** [r3 §1]. 16 mm rotary switches don't fit under a 25 mm deck. This applies to OCTAVE ×2, PRESSURE and SHIMMER, read in steps as on Big Energy's RANGE.
  - **The cost: no tactile detent.** You see the step from the pointer and the tick ring, and hear it, but don't feel it. That's a feel trade-off for the owner (§13).
  - The family tick ring stays as the only marking of steps.
- **Knob B column:** rows y 14 / 35.9, tabs y 28.4–43.4, crown foot y 48.4.

### 3.1 Dividers (flush)
Flush with the deck; you find the groups by the 7 mm wider gap and the strip's different feel. Making them: press a printed TPU strip into a printed slot, or print a groove (job 26). The look is visual's.

### 3.2 Where the print splits (if it isn't one piece)
**The shell splits at the divider lines x 74.5 and 205.5** into 74.5 + 131 + 74.5 [r3 §5], so the seams hide in the divider slots and the crown stays whole. **The speaker box is a separate airtight part.** A one-piece 280 shell needs a bed of ≥ ≈ 300 mm or a service; a 256 bed can't take it at any angle [r3].

## 4. Front face (toward the keyboard)
- **Target rail:** a printed rail along the top front edge, ≥ 264, with a printed target. Printed graduation (10 mm, longer centre mark). **No sentence on the module**; the home-octave line is on the 1:1 card and the site.
- **USB-C host port**, on the axis, in a **recessed pocket ≈ 25–30 mm deep** (PROPOSAL from [r3 §7]).
  - The module end takes a **straight** plug that sits inside the pocket, so nothing sticks out and the YOKE cap and the kits' lids close over it.
  - The kit cable needs a right angle only at the keyboard end (§9 S3).
  - The pocket takes space at the front-centre, where E's stacked boards are. ENG to fit.
  - Cold socket: VBUS only once a keyboard is detected, ≈ 550–600 mA.
- **Port light** beside the pocket.
- **Two USB-C sockets a body apart:** the host on the front, charging and computer on the rear facet.

## 5. Rear facets and underside
- **Plan-left facet, set once:** POWER (recessed slide) · USB-C (charging and computer) · TUNE · MIDI SPLIT.
- **Plan-right facet:** PHONES · LINE · MIDI IN · MIDI OUT.
- Jack and socket centres sit at z ≈ 14–19 [r3 §1], which sets the facet openings and the kits' windows.
- **Underside:** the two ¼"-20 inserts (S4; §2.3), bosses Ø 16–18, and four feet.

## 6. The voice (unchanged from rev 2, except that the count is decided)
| | Behaviour |
|---|---|
| **Voices** | **25 (owner: "25 is good for the string machine")**, in fixed pools: 1–12 left half, 13–25 right; oldest stolen within a half; a 25-key keyboard played live never steals. Pools: eng to confirm |
| **Split** | Fixed at B3 \| C4 (note 59 \| 60); OCTAVE L / R add −2 … +2; equal = one keyboard; a held note keeps its pitch through an octave change |
| **Velocity** | Speed (soft bows in slowly, hard speaks at once) inside ATTACK's range |
| **Release velocity** | Sets the tail inside RELEASE's range (to ≈ 30 s) when sent |
| **Strands** | Octave below · at pitch · octave above; three tabs per half; all off = that half silent |
| **DRIFT** | Each voice's own slow random walk, 0 to ≈ ±25 c (PROPOSAL) |
| **Lean (PRESSURE)** | swell · drift (a full lean becomes a ≈ 5–6 Hz vibrato) · tone · shimmer; adds to the knob and returns to it |
| **Lean source** | poly AT / MPE → per note; channel pressure → every note; CC1 → every note; nothing → velocity still works |
| **Bend** | ±2 semitones; per note with MPE |
| **HOLD** | Plant and tend: notes add, a re-strike pulls one out (its velocity sets the fade); held notes survive the keyboard. Scope (owner proposal): everything when the octaves are equal, the left half when split |
| **CC64** | Ordinary sustain |
| **Breath** | Sum grows ≈ √(voices), recovering over ≈ 200 ms |
| **Shimmer** | analog (3 × V3207, LFOs ≈ 1 / 6 Hz at 0 / 120 / 240°) · Daisy wide · glass · tape; DEPTH 0 = dry. Paths spread L / C / R on phones and line; **the speakers get the mono sum, high-passed at ≈ 115 Hz (E)** |
| **Echo, reverb** | ECHO = level + repeats; TIME ms (FREE) or division (SYNC: clock, else TAP); REVERB decay grows with amount |
| **MIDI** | Big Energy's rules; MIDI SPLIT → channels 1 / 2; velocity, pressure and release velocity go out; family CC map with jump-on-move |
| **Keyboard power** | 5 V cold socket, ≈ 550–600 mA, only while on |

## 7. Lights (two)
| Light | Where | Meanings |
|---|---|---|
| **Status** | TAP's lit ring | steady = fine · slow pulse = charging · fast flash = low battery · tempo blink (SYNC, no MIDI clock) |
| **Port** | beside the host pocket | off = nothing · steady = connected · a blink per note received · fast flash = fault |

**Status priority:** low battery > tempo blink > charging > steady. Both lights amber (visual, as the director accepted).

## 8. States
| State | What happens | What you see / hear |
|---|---|---|
| Off | host socket cold | dark |
| On, no keyboard | silent, ready; plays from USB-C or TRS | ring steady; port off |
| Keyboard plugged in | detected → VBUS on → enumerated | port steady |
| Playing | notes sound | port blinks per note |
| **Silent, keyboard connected** (job 29) | — | steady with no blink → notes not arriving (dead keyboard, charge-only cable); blinking but silent → VOLUME, tabs, phones |
| Port off with a keyboard plugged | non-compliant cable / not detected | use the C-to-A adapter with the keyboard's own cable |
| Over-current / charger in the host socket | keyboard power cut; floss runs on | port fast flash |
| Unplugged mid-chord | unheld notes fade; **held notes keep sounding** | port off |
| HOLD on, keyboard gone | the drone goes on; knobs work | HOLD latched; port off |
| A half full (12 / 13 planted) | the next replaces its oldest | — |
| A half with all tabs off | silent in and out | tabs show it |
| Lean source = nothing | PRESSURE has no effect | — |
| SYNC, no clock | echo at the last tempo (120 BPM at power-on, PROPOSAL); TAP sets it | ring blinks the tempo |
| SYNC, clock present | follows the clock | ring steady |
| Charging while playing | normal | slow pulse, unless the tempo blink applies |
| Low battery | warning before it stops | fast flash over everything |
| Headphones in | **both speakers mute** | — |
| Very loud bass on the speakers | the ≈ 115 Hz high-pass keeps the drivers inside their excursion below the port tuning [r3] | — |
| Stepped control between steps | the firmware holds the nearest step (with hysteresis), so it never flickers between two (PROPOSAL) | the pointer sits on a tick |
| Computer and keyboard together | merge if host and device work at once (unverified); else TRS | — |
| Big home keyboard | plays if ≤ ≈ 500 mA; a half can steal | — |

## 9. Family interfaces (job 28)
| | Interface | floss's value |
|---|---|---|
| S1 | keyboard the carry takes | **25-key portable controllers** (owner: "The carry should fit a portable MIDI controller"); slim class 325–388 × 83–135 × 11–16, ≤ 0.6 kg [eng]. Chunky minis per kit |
| S2 | host port | USB-C, cold socket, ≈ 550–600 mA, front face on the axis, **in a recessed pocket ≈ 25–30 deep** |
| S3 | cable | **C-to-C, straight at the module (into the pocket), flat sideways right-angle at the keyboard**. A reversible plug exits left or right by flipping. Checked product: Pimoroni flat sideways right-angle, **0.2 m (too short) or 1 m (coils in the kit)** [r3 §7, chk]. A 0.3–0.5 m version is a marketplace item (UNVERIFIED). Non-C keyboards: their own cable on **one C-to-A adapter**, in every kit. Old micro-B Xkey: adapter + StarTech A-to-angled-micro-B [r3] |
| S4 | attachment | two ¼"-20 inserts, **160 apart** (§2.3: keep the spacing), bosses Ø 16–18 |
| S5 | plug behaviour | §8 |
| S6 | CC map | CC64, CC1 lean fallback, CC74 tone, CC11, bend ±2 |
| S7 | split | fixed B3 \| C4 + target rail; the line on the card and the site |

## 10. Making steps outside the electronics (job 26)
| Step | Craft | Source or method | Trial or measuring? |
|---|---|---|---|
| Shell (deck, roof, crown, rail, target): **ASA** (PETG fallback) | 3D printing | our files; **one piece on a ≥ 300 bed or a service, or three pieces split at x 74.5 / 205.5** [r3] | no |
| Speaker box, a separate airtight part with gasketed driver seats and a flared Ø 16 port | printing + a bought gasket | our files | no |
| Dividers | pressed-in printed TPU strip, or a printed groove | our files | no |
| Shell joints (if split) | keyed laps in the divider slots + M3 screws into heat-set inserts | standard practice | no |
| ¼"-20 inserts | heat-set with a soldering iron, in Ø 16–18 bosses | Prusa / CNC Kitchen pack [r3, chk] | no |
| Board standoffs (bushingless pots) | printed bosses + screws | our files | no |
| Feet | bought | — | no |

## 11. Engineering questions (open after r3)
1. **E's box at 105:** does the detailed box keep ≥ 190 cm³ net (a 4 % margin) with ribs, gaskets, the port and the host pocket? If not: 115, or D.
2. **The host-port pocket (25–30 deep) and E's stacked front-band boards:** do they fit together at the front-centre?
3. **Cells under the jambs** with ≥ 2 mm margins, **and S4 kept at 160 apart** (§2.3): where do the inserts land in y?
4. **The PTV09A-3's L reference plane** (≤ 21 mm PCB to tip).
5. **Two drivers' frames under a ≥ 63° rake** at the crown foot y 41 (r3 checked one driver at y 73; E's pair sits side by side at ≈ 62 mm centres).
6. **Weight:** module ≈ 0.70–0.85 kg with E, PETG [r3]; ASA ≈ 40 g lighter.
7. **A 0.3–0.5 m flat sideways right-angle C-to-C cable** with a published listing.

## 12. Coverage (against `jobs.md` rev 3.2)
| Job | Where |
|---|---|
| 1 strings anywhere | §1, §2.2, §6 |
| 2 one cable, USB-C, any keyboard | §4, §9 S2 / S3 |
| 4 every note (25, decided) | §6 |
| 5 split and octaves | §3, §6 |
| 6 where the split lands | §4 |
| 7–10 velocity, lean, no pressure, extras | §6 |
| 11 colour per half | §3, §6 |
| 12 shimmer | §3, §6 |
| 13 echo, reverb, tempo | §3, §6, §7 |
| 14 hold | §6 |
| 15 speaker / phones, **the best sound** | §2.2 (E), §8 |
| 16, 17 computer, MIDI | §5, §6, §8 |
| 18 read the state | §3 (stepped pots read by pointer and ticks), §3.1, §4, §7 |
| 19 one switch, battery | §5, §7, §8 |
| 21 many vs one | §6 |
| 22 in tune | §5 TUNE |
| 26 printed, proven parts, fix | §1, §10 |
| 29 why silent | §7, §8 |
| 30 portable, makes sense, harmonious | §2 (105 conditional on E's margin) |
| 3, 20, 23, 24, 25, 27, 28 | §9 + each kit's file |

**At risk:** job 30's 105 (E's margin); job 18's feel of steps (no detents, which only weakens it; the steps can still be read by eye).

## 13. Owner trade-offs
1. **Speaker: E** (best: +5 dB/W, f3 152, +8–11 dB headroom; 105 with a thin margin, or 115) / **D** (robust pair, sealed, 105) / C / A. Systems draws E; D is the fallback.
2. **Knob: A** Ø 10 × 8 (35 tall, keeps 8 : 3 : 1) / **B** Ø 14.5 (≈ 42 tall, ≈ 112–120 deep, kits +7). Director recommends A.
3. **Stepped controls:** firmware-stepped pots (no detent you can feel) / rotary switches (≈ +5 mm height) [r3].
4. **Filament:** ASA / PETG.
5. **Print:** one piece (≥ 300 bed or a service) / three pieces at the dividers.
6. **S4 spacing:** keep 160 (the module's insides move) / change the family spacing (§2.3).
7. Split-scoped HOLD; fixed voice pools.
