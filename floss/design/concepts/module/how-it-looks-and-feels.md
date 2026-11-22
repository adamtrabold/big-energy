# floss module: how it looks and feels (shared by every carry)

Status: **rev 2, 2026-11-22**, product designer (visual focus), concept round 2, visual turn 2. Redone for the owner's printed-case principle (PRINCIPLES §7: "for now the case will be entirely 3d printed") and the director's R1–R4. **Rev 1's walnut, brass, bookcloth, brass frets and the engraved sentence are all withdrawn.** Read with `how-it-works.md` (systems, rev 2) and `floss/eng/module-r2.md`.

**Picture:** `module-1to1-A2.png` (and `.pdf`): **1 : 1 on A2**, both knob options side by side (plan, front, rear, section on the axis), plus the material story, the divider at 4 : 1 and the knob verdict. Print at 100 %: the 50 mm bar measures 50 mm. A2 because the two 280 mm plans only fit side by side at true size on A2 (a copy shop prints it; the old A3 sheet is deleted). Source: `../_src/r3.py` (`python3 r3.py module`, from `_src`). `r2.py` is history.

Marks: **[r2]** `module-r2.md` · **[calc]** my arithmetic · **PROPOSAL** · **UNVERIFIED**.

---

## 1. Draws this turn (python `secrets`)
- Oblique Strategy: **"Faced with a choice, do both."** Applied literally to the knob (drawn both ways at 1:1, as the director asked) and to the divider (a TPU strip, with a printed groove as the one-spool fallback).
- Field: **stage lighting.** Theatre gear is black so it disappears; the stage is the lit surface; floor positions are marked with spike tape; colour comes from the light. That became the material story (§2).
- Twist: **"the colour comes from the spool, never paint."** Every colour is a filament, a bought part or a light. No paint, no decals.

## 2. One material story: stage blacks and spike marks (module and every carry)
| Role | Material and colour | Where |
|---|---|---|
| **The house** (recedes) | **warm near-black matte PETG** | shell, crown, every printed carry part (FALLBOARD, SPINE, YOKE). CLOTH's coated cloth is the same near-black |
| **The stage** (where the hands work) | **cream PETG** | the sunk deck only. It's the one lit surface; black knobs on cream also read best in sun (job 20) |
| **Spike marks** (what you read or set to, on black) | **cream**: a second filament (multi-material print) or cream thread | the rail's ticks, the target, the words on the crown's rake, the wordmark, the kits' scale ticks and axis mark, CLOTH's stitched outline |
| **Touch** | **black TPU 95A** | the flush divider strips (§5) |
| **One accent** | **coral** | DEPTH only |
| **Light** | **warm amber** | TAP's ring (status) and the port light. Both the same colour: they're told apart by place and rhythm |

- **Why this replaces walnut, cream and brass:** walnut and brass were materials the printer can't honestly make. A brown "walnut" print would be imitation, which PRINCIPLES §5 rules out ("no decoration"). Black and cream are what a printer does well, and they keep the family's cream face. Black also hides print lines and park dirt, and it matches the cloth the director already chose for CLOTH, so the whole family is one story.
- **Two spools plus a little TPU.** The cream marks on black need either a multi-material printer or an outside service. **One-spool fallback:** every mark is debossed 0.6 mm in the black and reads by shadow (§9 open question).
- **Surfaces:** outward faces printed against a textured PEI plate where the geometry allows (a fine even stipple, no gloss); layer lines on the walls run horizontal. The deck's top is printed face-down on the same plate, so the stage surface is the smoothest, most even surface on the instrument.
- **Carries carry no name.** floss's name lives on floss (the crown's rear face). The closed kits are plain black objects; their only marks are their seams and their scales. (That's rule 5 from my turn 2, "floss's marks only on floss", made literal.)

## 3. Size, ratio, outline (unchanged in principle; now two options)
The director accepted 280 × 105 × 35, 8 : 3 : 1, hull (R1) on conditions. Systems found that **35 holds only with low Ø 10 knobs** (`how-it-works.md` §2.1–2.2). So the sheet shows both:

| | **A: Tayda aluminium Ø 10 × 8, 6 mm 18T** (CATHEDRAL's low knob) | **B: family 18T push-on Ø 14.5 × 13.5** (Tayda) |
|---|---|---|
| Body | **280 × 105 × 35** | **280 × 112 × 42** |
| Deck, knob tops, rim | 25 · 33 (1 mm seat) · 35 | 26.5 · 41 (1 mm seat) · 42 |
| Rows (y) | 14 / 31 | 14 / 35.9 (7 mm between rows, the family minimum) |
| Crown foot, rake | y 41, 8 mm run | y 48.5, 8 mm run |
| **Finger room** behind DRIFT · SHIMMER · TIME | **5 mm** (36 → 41) | **5 mm** (43.4 → 48.5); 112 deep gives the driver its 108–110 + 2 mm |
| Ratio | **unit 35: 8 : 3 : 1**; halves 4 : 3 (a fourth); centre : end 105 : 70 = 3 : 2 (a fifth) | **restated, unit 14: 20 : 8 : 3**; halves 140 × 112 = 5 : 4 (a major third); centre : end 112 : 70 = 8 : 5 (a minor sixth); ends 70 = 5 units. PROPOSAL: the parts asked for ≈ 110 × 41, and 112 × 42 is the nearest whole-unit fit, with 2 mm and 1 mm of margin, not faked |
| Kit thickness | FALLBOARD 42, SPINE 59, CLOTH ≈ 65, YOKE ≈ 64 | +7 each; FALLBOARD's footprint becomes 412 × 272 |

- **My pick: A.** floss's knobs are set and tended, not ridden; knurled aluminium pinches well at Ø 10; it's the family's part; every size stays traced to a part; every carry is 7 mm thinner. **The cost, said plainly:** a smaller knob under the hand and about 12 mm of air between knobs on the 22 mm grid, so the deck reads airier. The owner decides (systems' trade-off 3).
- **Outline:** unchanged. A straight front for the rail and the host port, r 10 front corners, straight 70 ends to pick it up by, a fair rear arc (R ≈ 297.5 for A [calc]) with **two flat port facets** on it (plan x 20–96 and 184–260), and the crown between them. On the 1:1 sheet the facets make the rear read as a shallow five-sided bow. That's honest: they're where the jacks need flat walls.

## 4. The panel, at 1:1
- **Systems' map, unchanged:** seven groups mirrored about the axis, the stop jambs at each end, coral DEPTH on the axis.
- **Knobs:** A: all round controls Ø 10 × 8, black anodised knurled aluminium (black finish UNVERIFIED at Tayda), cream pointer line. B: amounts Ø 14.9, kinds (PRESSURE, SHIMMER mode) Ø 10.
- **Stop tabs:** three bought black mini rockers per jamb (UNVERIFIED product), their words (low · main · high) printed on the deck above them, black on cream. Organ stops are white with black words; on a cream deck the inverse reads better.
- **HOLD:** a black rounded-square push-push latch, 12 × 12, with a small cream dot. Latched, it sits low: you feel it from the side.
- **TAP:** black, inside its amber lit ring (status, R3).
- **FREE / SYNC:** a black bat toggle.
- **Words:** one plain word above each control (family rule). On the deck they're **black on cream**; DRIFT, SHIMMER and TIME sit on the crown's black rake, so they're **cream on black**. No other print on the deck.
- **Marking:** detent ticks only on stepped knobs (octave: five; the 4-step kinds: four). Pots carry a pointer line only.

## 5. Dividers: flush, printed (director R2; my call)
**A pressed-in black TPU 95A strip, 1.6 wide × 2.0 deep, in a printed 1.6 slot in the cream deck, flush.** It runs from the deck's front edge to the crown foot at each of the six group gaps (x 45.5 · 74.5 · 125.5 · 154.5 · 205.5 · 234.5).
- **Why TPU, not a groove or a multi-material inlay:** the director's "other method" is a change you can feel with no edge. A groove has an edge (and collects grit); a PETG inlay feels exactly like the deck. TPU against hard PETG feels softer, warmer and faintly grippy under a fingertip sweeping sideways, and it's level, so nothing catches a finger turning a knob (PRINCIPLES §6). You find the groups by the 7 mm wider gap first, and the strip confirms it.
- **It looks like** a fine black rule across the cream: the panel's group lines, drawn by the material.
- **Making:** print the strips flat (or cut from a printed TPU sheet); press them into the slots by hand. TPU prints on most printers with a direct-drive extruder, or by a service. **One-spool fallback:** a printed groove 1.0 × 0.4.
- UNVERIFIED: the press fit of a 1.6 TPU strip in a 1.6 printed slot is a standard interference choice, but the exact slot allowance is a printer setting (ENG to state it as a number in the print file).

## 6. Crown, grille, wordmark
- **The crown** is black, 70 wide on the axis, its top level with the rim, its raked front carrying DRIFT · SHIMMER · TIME. On the cream deck it reads as a black stage speaker at the back of the stage. That's what it is.
- **Grille: Ø 1.9 holes on a 2.6 hex pitch in a Ø 46 field** on the crown's flat top (clipped to the flat): **260 holes ≈ 737 mm² open** [calc, counted in `r3.py`], above eng's ≥ 620 [r2] with ≈ 19 % margin, in both options. Printed through, vertical holes, no supports.
- **Wordmark "floss"** in cream on the **crown's rear face**, between the two port facets, ≈ 10 mm cap height, italic (director R4: the nameboard turned outward). Nothing on the deck but controls and their words.

## 7. Front face, rear, underside
- **Front** (faces the keyboard): black. The **graduated rail** is cream ticks inlaid in the black rim, every 10 mm, a longer one on the axis. **The target is a cream printed rider** that slides on the rim, with a pointer down the face: a spike mark. **USB-C host port** low on the axis, the **amber port light** beside it. **No words** (R4): the home-octave line is on the card and the site.
- **Rear:** two facets: plan-left power (a recessed slide) · USB-C · tune · split; plan-right phones · line · MIDI in · MIDI out. Port names in small cream marks on the facets. The two USB-C sockets are a whole body apart.
- **Underside:** two ¼"-20 heat-set inserts at x 60 / 220, y 30 (dashed on the plan); four feet.

## 8. Feel, motion and feedback (every state in systems' §7–§8)
| State | What you see or feel |
|---|---|
| Off | all dark; knobs still turn; the house disappears, the cream stage stays readable |
| Switching on | the recessed slide clicks; TAP's ring comes up **steady amber** |
| Keyboard plugged in | the port light comes on **steady amber** |
| Playing | the port light **winks once per note** |
| Silent, keyboard connected (job 29) | port steady with no wink = notes not arriving; winks but silent = VOLUME, then the tabs (all three down in a half reads as a dark block), then phones |
| Port off with a keyboard in | use the C-to-A adapter (card) |
| Keyboard fault / charger in the host socket | port light **flashes fast** |
| Unplugged mid-chord | port goes dark; held notes keep sounding |
| HOLD on | the HOLD latch sits low; its cream dot drops below the knob line. Felt from the side |
| HOLD on, keyboard gone | HOLD low, port dark, the drone continues, every knob works |
| Octaves split | the two octave pointers aren't parallel: the split (and HOLD's scope) read from the ends |
| A half with all tabs off | three black tabs down at that end |
| Charging | ring **pulses slowly** |
| Low battery | ring **flashes fast**, over everything (R3 priority) |
| SYNC, no clock | ring **blinks the tempo** (over charging, under low battery) |
| SYNC with clock | ring steady |
| Headphones in | speaker mutes; nothing visual |
| Shimmer | coral DEPTH under the right hand at the centre; no light: you hear it |

- **Hand feel:** stepped knobs click, pots are smooth, tabs rock with a firm detent, HOLD is a push-push latch, TAP is momentary. **Counting by touch from the left:** octave knob, three tabs, soft strip, HOLD, soft strip, four voice knobs, soft strip, the centre. The right mirrors it.

## 9. Open questions
1. **Owner:** knob A or B (and with it 35 or 42); the material story (black, cream, coral, amber) replacing walnut and brass.
2. **Eng:** a black knurled Ø 10 × 8 and a **coral** Ø 10 × 8 knob (Tayda colours UNVERIFIED; fallback: a printed coral cap on the black knob); the TPU slot allowance; whether the crown and deck print as separate parts (my assumption: deck cream, separate; shell and crown black, one part or two).
3. **Director:** both lights amber (vs. CATHEDRAL's ring colour, which I couldn't find stated in the Big Energy records: shared universe says match it); the one-spool fallback (debossed marks) as acceptable or not.
4. **Systems:** update the module map's rows and crown foot to the option chosen; the deck words as multi-material print (or deboss).

## 10. Why (for the handoff)
- **Black and cream:** a printed case should look printed and good, not imitate wood. Black recedes and hides; cream is the family face and the lit working surface; one coral; light for state. Every colour from a spool or a part.
- **TPU dividers:** flush (PRINCIPLES §6), felt by touch, and they draw the group lines in the material.
- **Both knob options at 1:1:** the honest way to show what 35 costs; the ratio is restated for B, not stretched.
