# The budget instrument: what HUSH, FOLD and ONE SHEET share (systems)

Status: **rev 6, 2026-11-12 (concept round 4).** Active: HUSH, FOLD, ONE SHEET. TYPE CASE and HYMNAL are paused; their own files keep the rev 5 numbers (298 × 180, common layout with the stick column), and nothing here applies to them.

**Why rev 6.** The owner (newest in `../owner.md`):
- "the knob layout is adding extra space in front of the keyboard that's awkward, I like the keys right up to the edge, so rework the knobs to be logically split, and maybe it could get a bit narrower"
- "I'd like the enclosure to be as 'unibody' … as possible. Screws in the back instead of front"
- "One sheet and hush feel like the controls are installed from behind and then a panel screwed in on the back"
- FOLD: "a hollowed out block that the face plate with filters and keys get installed in, sort of like a guitar with pickguard"; "screw placement is malleable but yes screw from back is ideal".

What made the space. In FOLD it was the 38 mm palm rest: the lid had to be 106 deep for three rows of knobs, so the base was 106 deep too, and keys only need ≈ 50. In the flat concepts it was the 180 mm footprint: an empty band (y 52–78) between keys and knobs, plus rows set further back than they needed to be. Both came from the knob layout, as the owner said.

Read with `../jobs.md`. Each concept's `how-it-works.md` states only where it departs from this.

> ## Rev 7.4: PARA legend fits by mirroring AFTERTOUCH's (labels can't stack 3 deep there)
> - **Name:** "PARA", **left-aligned 5.6 mm to the RIGHT of the toggle**, in the strip between OSC 1 and OSC 2. It mirrors AFTERTOUCH's label, which sits right-aligned to the left of its own toggle.
> - **Positions:** shortened to **1 · P · 4** (MONO / PARA / PARA+4). These are the only words that change.
> - **ONE SHEET:** that strip is ≥ 8 mm tall across x 114–123 [CALC], so it takes two lines of 1.37 caps: "PARA" over "1 · P · 4".
> - **HUSH:** the tags narrow it to 4.3–5 mm, so there's room for one line only. "1 / P / 4" is pressed as three 1.2 mm glyphs stacked at the toggle's three throw heights (y 109 / 111.5 / 114), right beside it, and "PARA" follows at x ≈ 119.5–124.5 on y 111.5.

> ## Rev 7.3 (pre-build, 2026-11-13): switch pair
> - **AFTERTOUCH confirmed where the visual designer placed it:** VELOCITY's column, y 111.5, between the VOICE rows (FILTER MOD / AFTERTOUCH / VELOCITY). The two key-response switches stack.
> - **Its empty mirror slot is now filled by the new PARA toggle (3-way MONO / PARA / PARA+4)** at the oscillator-side switch column, y 111.5 (OSC MOD / PARA / OSC 3 CTL). ONE SHEET x 104.25, HUSH x 111.25; AFTERTOUCH ONE SHEET 171.75, HUSH 178.75.
> - **Why:** PARA decides how the keys are assigned to the oscillators, so it sits with the oscillator switches. AFTERTOUCH is how the keys respond, so it sits with VELOCITY. They mirror about the centre.
> - Checkers 0 violations, mirror 0.00.
> - **Legend check (visual):** PARA's three position words need the same treatment as AFTERTOUCH's label (right-aligned, left of the toggle). OSC MOD and OSC 3 CTL labels go above their toggles, mirroring VELOCITY and SOURCE.

> ## Rev 7.2 / DRIFT (ONE SHEET x; HUSH + 7), 2026-11-13. Supersedes 7.1's PLAY-right and back-row text. Owner: "I like the idea of drift, but I'd want it to be controllable". DRIFT is a firmware random pitch wander; fully left = rock-steady.
> - **Back row = the chain in one line**, mirrored about the centre:
>   - **DRIFT 74.5** (source, under the FREQ column)
>   - ECHO TYPE 103.5 · ECHO TIME 123.5
>   - REVERB DECAY 152.5 · REVERB TYPE 172.5
>   - **VOLUME 201.5** (out, under the loudness column)
>   - Breaks at 89 / 138 / 187.
> - **PLAY right:** ECHO REPEATS 194 · ECHO MIX 214 · REVERB MIX 234 · **TAP 256**. TAP is played in rhythm, and it mirrors the bend stick.
> - **Why:** one added knob makes the count odd, so a lone DRIFT can't be mirrored. **DRIFT ↔ VOLUME** pairs source with output; TAP moves to the PLAY row to keep that row at 4 + 3 + 4. The checkers pass with 0 violations and mirror 0.00 in every row.
> - **Cost:** VOLUME sits on the back row (≈ 78 mm behind the PLAY row), and TAP is away from TIME. Sizes are unchanged.

> ## Rev 7.1 (round 5 final, 2026-11-13): FULL FX (owner: "Full 8, grow the panel"). SUPERSEDES REV 7'S FX AND VOLUME TEXT
> - **Chip:** Pico 2 core 1 + Teensy Audio Shield (eng `single-chip-research.md`). **Controls:** echo TYPE (4-way rotary), TIME, REPEATS, ECHO MIX, reverb TYPE (4-way rotary), DECAY, REVERB MIX, TAP.
> - **The split rule: amounts in front, kinds and times behind.**
> - **PLAY row, right section ("how much", played during a note):** ECHO REPEATS 194 · ECHO MIX 214 · REVERB MIX 234 · **VOLUME 256 (back on the panel)**. ONE SHEET x; HUSH + 7.
>   - The PITCH ↔ AMOUNT mirror holds (the stick 22 pitch ↔ VOLUME).
>   - The rev 7 side-wall wheel and wall MODE toggle are **dropped**.
> - **FX row, its own section ("what kind, how long"): a third panel row at y 146**, 23 behind the VOICE back row, centred on the axis:
>   - ECHO TYPE 90.5 · ECHO TIME 110.5 | **TAP 138 (on the axis: it's shared)** | REVERB DECAY 165.5 · REVERB TYPE 185.5. ONE SHEET x; HUSH + 7.
>   - **Mirror meaning:** TYPE ↔ TYPE, TIME ↔ DECAY (each effect's time scale).
>   - **Own breaks at x 125 / 151** (HUSH 132 / 158), isolating TAP. The VOICE's vertical breaks (96.5 / 179.5) stop at the VOICE back row.
>   - **Balance:** the deck becomes three full columns (PLAY + VOICE) on a centred FX "plinth" behind them, and the empty rear corners frame it.
>   - TAP: a 12 mm momentary cap (part UNVERIFIED). The TYPE rotaries are RS16211 (body height risk as with WAVE).
> - **Checked:** `_mock-src/flat_r5_check.py`, 0 violations, mirror 0.00 in all four rows.
> - **New sizes** (rows unchanged; growth at the back; board ≈ 268 × 122 with the shield, ESTIMATE):
>   - **ONE SHEET 276 × 180** (FX edge 153.45, rear band 26.5 for jack legends and name);
>   - **HUSH 290 × 186** (FX edge + 12 flat inset = 165.45; rear band for the pressed jack legend).
>   - Body heights and knob tops unchanged.
> - **Mux (eng §5):** 8 new channels, ≈ 45 of 48.
> - **Key-edge options A/B unchanged** (see each concept's file).

> ## Rev 7 (round 5, 2026-11-13): one balanced layout for all three, and an FX group. SUPERSEDES §1–2 BELOW FOR HUSH AND ONE SHEET
> **Why:**
> - Owner: FOLD "doesn't feel balanced yet"; "Is there a way for us to build in some effects, mainly a delay and echo?"; then "I want echo and reverb".
> - Common rev 6 had no room for an FX group: its PLAY row was full, and its VOICE rows had holes in different places.
> - FOLD rev 5.1's balanced layout fits the flat frames unchanged, with **0 violations**: `_mock-src/flat_r5_check.py`. So **all three concepts now share one layout.** The balance logic (B1–B7) is in `fold/how-it-works.md` §1.
>
> **Frames:**
> - ONE SHEET x = FOLD x − 5 (centre 138);
> - HUSH x = FOLD x + 2 (centre 145).
>
> Rows stay at y 68 / 100 / 123, the horizontal break at 85.4, and the keys as before. Every row mirrors about the centre (worst offset 0.00).
>
> **ONE SHEET x** (HUSH: + 7):
> - **Vertical breaks: x 96.5 / 179.5 in all rows** (HUSH 103.5 / 186.5). The old 122.5 / 228 / 181 are retired.
> - **PLAY y 68:**
>   - **PITCH:** BEND stick 20, MOD 42, **TUNE 62**, GLIDE 82
>   - **FILTER:** CUTOFF 114, **EMPHASIS 138**, CONTOUR AMT 162; lights not-in-control (126, 81) and status (150, 81)
>   - **FX:** **ECHO TIME 194, ECHO REPEATS 214, REVERB 234, FX MIX 256**
> - **VOICE, x for both rows:** 18.5 / 38.5 / 58.5 / 78.5 | 104.25 t / 118 / 138 / 158 / 171.75 t | 197.5 / 217.5 / 237.5 / 257.5 t
>   - **Front (y 100):** RANGE 1–3, FREQ 2 | OSC MOD, OSC 1, OSC 3, MOD MIX, FILTER MOD | F ATTACK, F DECAY, F SUSTAIN, KBD CTRL
>   - **Back (y 123):** WAVE 1–3, FREQ 3 | OSC 3 CTL, OSC 2, NOISE/EXT, SOURCE, VEL | L ATTACK, L DECAY, L SUSTAIN, DECAY
> - **Moved from rev 6:**
>   - TUNE goes to the PLAY row;
>   - MOD MIX and the four set-before-playing switches (OSC MOD, FILTER MOD, KBD CTRL, VEL) go to the VOICE;
>   - reach stick → CUTOFF drops to 94.
>
> **FX group: echo + reverb (chip research pending; plan for 4–5 controls)**
> - **On the face: the PLAY row's right section, 4 knobs.** ECHO TIME, ECHO REPEATS, REVERB (size/decay), FX MIX, in signal order: echo feeds the reverb, then the mix.
>   - The FX group sits under the hand, because throwing an echo or swelling a reverb is played.
>   - It mirrors the PITCH group.
> - **VOLUME leaves the face.** It becomes **a thumbwheel in the right end wall**, just behind the keys (ONE SHEET: right wall at y ≈ 60–75, z ≈ 12, slot 4 × 16; HUSH: punched through the felt).
>   - It sits next to the right hand, the way portable gear does it.
>   - This is the trade that keeps 4 + 3 + 4 balanced and gives the FX 4 face slots. The thumbwheel pot part is **UNVERIFIED** (eng).
> - **The FX MODE toggle (ECHO / BOTH / REVERB, if the chip needs one)** goes **on the rear wall with the jacks and the power switch**, where the set-and-forget choices live.
> - **If research lands on 5 knobs:** no legal face slot is left. The trades, in order of preference:
>   1. a dual-concentric FX MIX: inner = echo level, outer = reverb level (part UNVERIFIED in 9 mm T18);
>   2. REPEATS doubles as reverb decay in REVERB mode;
>   3. a third rear row in the rear band (HUSH and ONE SHEET only). It's centred, ±2 slots about the centre, but it breaks consistency with FOLD and adds depth.
> - **If research lands on 3:** leave the 234 slot blank; don't reflow the row.
> - **Board (eng `effects.md` §2.5):**
>   - The PT2399 alone adds ≈ +1,600–2,000 mm², ≈ +6–8 mm of depth at the back. Reverb adds more (pending).
>   - So the bodies grow at the back only: ONE SHEET ≈ 276 × 178, HUSH ≈ 290 × 184 (ESTIMATE). Keys and rows don't move.
>   - Keep the PT2399 / reverb chip ≥ 30 mm from the ladder, the expos and the Hall harness.
>
> **Key-edge options (owner wants to see both; keys must be "somewhat raised so you can feel them"):** each concept's file gives its geometry. Both options raise the white key surface to **2.5 above the panel**, with sharps a further 2: strip C on spacers 2.5 mm taller (R4: ≤ 3 ✓).

> **Rev 6.1, same day: eng round-4 answers applied** (`/home/claude/model-d/eng/round4-answers.md`). Supersedes the numbers below where they differ:
> - **Main board needs ≈ 268 × 115** (dense build: 1/8 W standing resistors, top parts ≤ 6.5 mm, Pico on the underside, ≤ 8 mm stack), not 268 × 85. As §3 said it would, **the body grows at the back; rows and keys don't move.**
>   - **ONE SHEET 276 × 170. HUSH 290 × 176.**
>   - The extra ≈ 30 mm sits behind the VOICE back row (last knob edge y 130.45 → back edge 170): a flush **rear band** for the name/wordmark and jack legends. No controls go there, and it's behind the hands, not in front of the keys.
>   - If eng's mux-on-strip-C saving works at layout (≈ 268 × 100), it drops to ≈ 155 deep.
> - **Knobs:** pots become **Tayda A-5622 T18 spline** ($0.59). Knobs are **18T push-on, 14.5 × 13.5**. KN1250 is a round-bore set-screw knob, so it's out on these shafts. Knob tops rise ≈ 3 mm: ONE SHEET ≈ 37.5, HUSH ≈ 39 (≤ 40 ✓, tight). Cream 18T push-on knobs for HUSH and ONE SHEET: availability UNVERIFIED (visual/eng). The RS16211 WAVE panel hole is **9.5 mm**; its shaft is 6 mm spline (18T likely).
> - **Height risk (eng):** the WAVE rotary body (Ø 16) and the toggle bodies may be > 7 mm under the shell. Measure them before freezing panel z; if they're taller, they need a board cutout or a local spacer.
> - **Speaker:** ladder, expo pair and emphasis loop must stay **≥ 55 mm from the speaker centre** (240, 113). The natural ladder spot (x 135–180, y 75–100) gives ≈ 38 mm edge clearance ✓. The LM386 goes by VOLUME.
> - **Power:** recounted at ≈ 2.0–3.6 W, so an internal #2011 lasts ≈ 1.8–3.3 h. Optional 3000 mAh pouch under the main board (eng §3.1). FOLD defaults to a USB power bank.

Coordinates: origin at the **front-left outer corner**, x right, y away from the player, z up from the table (bottom face = 0). mm. **[ENG]** eng figure, **[CALC]** mine, **ESTIMATE** unpriced, **UNVERIFIED** source exists but figure not checked.

---

## 1. The logical split: a PLAY row and the VOICE

**Rule (rev 6): the row nearest the keys is the PLAY row — everything the left hand works while the right hand plays. Behind it, the VOICE: the patch, left → right in signal order.**

- **PLAY row**, read left → right as **pitch → tone → level**:
  - **P1 Pitch & modulation:** BEND stick, MOD dial, MOD MIX, OSC MOD and FILTER MOD toggles, GLIDE. (The Model D's own "controllers" group: the wheel, its routing and glide, together.)
  - **P2 Tone:** CUTOFF (hero), EMPHASIS, CONTOUR AMT, KBD CTRL toggle, VEL toggle (velocity → loudness / both / filter: it sits between tone and level, which is what it switches between).
  - **P3 Level:** VOLUME, status light.
- **VOICE**, two rows, read section by section left → right, **front then back in each column**:
  - **II Oscillators:** TUNE; then a column per VCO: RANGE (front), WAVE (back); then a FREQ column (FREQ 2 front, FREQ 3 back); OSC 3 CONTROL toggle beside FREQ 3.
  - **III Mixer:** OSC 1 / OSC 2, OSC 3 / NOISE·EXT, SOURCE toggle beside NOISE.
  - **IV Contours:** filter contour A D S (front row), loudness contour A D S (back row), DECAY toggle.

**Why this split (reasons, not looks):**
1. **It frees the front.** The bend stick and MOD dial move out of the key zone into the PLAY row, so the keys run the full width and right to the front edge. Nothing sits beside or in front of the keys.
2. **It narrows the instrument.** The 22 mm stick column is gone: the body is the keys plus walls. ONE SHEET 298 → **276** wide.
3. **It shortens the reach.** Stick → CUTOFF was ≈ 196 mm; now **120 mm** [CALC]. The left hand never crosses the right.
4. **For FOLD it is the fold line** (FOLD file): the PLAY row lives in the base with the keys; the VOICE goes on the lid. That is what removes the palm rest.

**What it gives up:** the strict Model D left-to-right panel sentence (controllers · oscillators · mixer · modifiers · output across one panel). The VOICE keeps signal order; the PLAY row pulls the hand controls out of it. TUNE moves into the oscillator section, where it acts.

## 2. Plan and coordinates (ONE SHEET frame: 276 wide)

HUSH uses the same layout shifted **+7 in x** (body 290); FOLD **+5 in x** (286) and its own y for the VOICE (FOLD file). Every number below was checked by script (no rule violation): knob pitch ≥ 20, 24 between CUTOFF / EMPHASIS / CONTOUR AMT, ≥ 7 mm from any knob edge to a section break, ≥ 3 mm from a toggle nut to a break, ≥ 10 mm from any control's edge to the outer body edge.

**Parts used for the check:** KN1250 knob 14.9 dia; CUTOFF Tayda 1083 20.8; toggle nut ≈ 9.2 across corners; stick cap ≤ 12 (check #2765 in hand); status LED 5 mm, "not in control" LED 3 mm.

### Keys
- 25 Choc V2 silent, short tops (eng S1). 15 whites at 18 mm pitch, **x 3–273**.
- **Whites y 3–33** (30 × 17.2). **Sharps y 35–49** (16 × 14, rear row, +2 mm). Key fronts **3 mm** from the front face: just the shell's front wall, flush with the key surface (it protects the key fronts in a bag and is the "unibody" edge). No palm rest, no deck, no band.

### Rows
| Row | y | Content |
|---|---|---|
| PLAY | **68** | sections P1 / P2 / P3 |
| horizontal break | **85.4** | flush, full width (sunk groove; in FOLD the hinge seam) |
| VOICE front | **100** | |
| VOICE back | **123** | |
| last knob edge | 130.45 | + 10 to the edge → ONE SHEET depth **140** |

Sharps end 49 → CUTOFF's front edge 57.6 (8.6 mm clear), the other PLAY knobs 60.55 (11.5 clear).

### PLAY row (y 68)
| x | Control | Notes |
|---|---|---|
| 20 | **BEND stick** (#2765) | fore-aft gate slot along y, up and down, springs to centre; Delrin gate |
| 42 | MOD dial | thumb on the stick, fingers on MOD |
| 62 | MOD MIX | |
| 78 | OSC MOD toggle | |
| 92 | FILTER MOD toggle | |
| 108 | GLIDE | MIDI dot |
| **122.5** | **break P1 \| P2** | continues straight back through the VOICE as the II \| III break |
| **140** | **CUTOFF** (1083 hero) | MIDI dot |
| (152, 79) | "not in control" light | behind and right of CUTOFF |
| 164 | EMPHASIS | 24 from CUTOFF |
| 188 | CONTOUR AMT | 24 |
| 204 | KBD CTRL toggle | |
| 220 | VEL toggle (LOUD / BOTH / FILT) | |
| **228** | **break P2 \| P3** | PLAY row only |
| 243 | VOLUME | |
| 262 | status light | |

### VOICE (front y 100, back y 123)
| x | Front (100) | Back (123) |
|---|---|---|
| 18.5 | TUNE (MIDI dot) | — |
| 38.5 | RANGE 1 | WAVE 1 |
| 58.5 | RANGE 2 | WAVE 2 |
| 78.5 | RANGE 3 | WAVE 3 |
| 98.5 | FREQ 2 | FREQ 3 |
| 114.5 | — | OSC 3 CONTROL toggle |
| **122.5** | **break II \| III** | |
| 137 | OSC 1 | OSC 2 |
| 157 | OSC 3 | NOISE / EXT |
| 173 | — | SOURCE toggle |
| **181** | **break III \| IV** | VOICE only |
| 197 | filter ATTACK | loudness ATTACK |
| 217 | filter DECAY | loudness DECAY |
| 237 | filter SUSTAIN | loudness SUSTAIN |
| 253 | — | DECAY toggle |

- **Counts:** 26 round controls (25 + MOD) ✓, **7 toggles** ✓, bend stick ✓.
- **MIDI dots** (F7): RANGE ×3, FREQ ×2, TUNE, GLIDE, CUTOFF, MOD.
- **Breaks:** one horizontal (y 85.4) and three vertical (x 122.5 through everything; 228 in PLAY; 181 in VOICE). All flush (rule R4).
- **Edges:** leftmost control edge 11.05 (TUNE), rightmost 264.5 (status light), last knob edge y 130.45.
- **F3 reach:** stick (20, 68) → CUTOFF (140, 68) = **120 mm** [CALC].

### Outer sizes (rev 6 vs rev 5)
| Concept | rev 5 | **rev 6** | Why the difference between them |
|---|---|---|---|
| ONE SHEET | 298 × 180 | **276 × 170** (rev 6.1; 140 before eng) | keys + 2.4 walls; rows pulled up behind the keys; +30 at the back for the main board (eng) |
| HUSH | 298 × 180 | **290 × 176** (rev 6.1) | the felt's 12 mm round-over: pegs and knobs must sit on the flat; +32 at the back for the board |
| FOLD (closed) | 298 × 106 × 51 | **286 × 100 × ≈ 50** (rev 6.1; 86 before eng) | the lid's side rims need ≥ 12 mm from knob edges; +14 per half for the lid board |
| FOLD (open) | 298 × 212 | **286 × 202** | |

## 3. Boards (eng question E-L9)

- **Main board** under the panel: about **268 × 85** (y ≈ 52–137) in the flat concepts, down from 280 × 100 (≈ 35 in², −19 %). It now also carries the stick and MOD (both are in the panel), so **E-L1 closes**: nothing hangs off strip C except keys.
- **Strip C** under the keys only, 270 wide, y ≈ 3–50.
- **E-L9 (eng):** does the voice fit on ≈ 268 × 85? If not, the body grows at the **back** (rows unchanged; the extra depth goes behind the back row, where it costs nothing at the keys). FOLD has its own split (FOLD file).

## 4. Heights and section

| Part | z |
|---|---|
| Back panel (bottom) | 0–3 |
| Speaker (50 mm CDS-5076, 7.6 deep) on the back panel's inner face | 3–10.6 |
| Main board (lead-free keep-out over the speaker and battery) | top ≈ 14.5 |
| Pot body (7 [ENG]) against the shell's underside | 14.5–21.5 |
| **Top face (shell, 2.5)** | **21.5–24** |
| White key surface / sharps | **24 / 26** (strip C on spacers, R4: level with the panel) |
| Knob tops (KN1250 10.45) / CUTOFF (12.15) | ≈ 34.5 / 36.1 |

Inside R3 (≈ 36 body, ≤ 40 to knob tops) with margin. FOLD and HUSH state their own.

**Speaker** (eng E-L2): bottom-firing, centre **(240, 113)** in the ONE SHEET frame. Why there: ≥ 60 mm from the nearest Hall sensors (sharps' magnets at y ≈ 50), and inside the outline (radius 25 → y 88–138). **Eng to confirm ≥ 30 mm from the ladder and expo arrays** at layout (the ladder now sits under the IV / P2 area). FOLD: a rectangular speaker on the lid, firing up (FOLD file).

**Jacks (H9):** 6 × 3.5 mm + USB-C + micro-USB (7 with eng's single-USB option) on an **I/O board screwed to the inside of the rear wall** (bosses inside; the jack barrels sit flush in the wall holes; no outside nuts). One cable to the main board. Rear wall x 150–270. FOLD: lid's right wall.

**Power switch:** recessed slide switch on the I/O board, in the rear wall (H7).

## 5. Unibody: how the flat ones are built (HUSH, ONE SHEET)

**The owner's picture: "the controls are installed from behind and then a panel screwed in on the back."** So:

- **The shell is one closed-top body**: top face, the rounded edges and the four walls in one piece. The top has only holes: pot bushings, toggle bushings, the stick slot, the LEDs, and the key window.
- **Everything goes in from underneath**: main board, strip C, I/O board, battery, speaker.
- **A back panel closes it**, screwed from underneath. **No fastener on the top or the walls.**

### Retaining pots and toggles without top nuts
- Pots and toggles are **board-mounted**. The main board is screwed **up** to printed bosses in the shell: **10 × M3 into heat-set inserts**, placed on the break lines and between rows so every row has a boss within ≈ 30 mm. Screwing the board up pulls each pot body tight against the shell's underside.
- **Anti-rotation:** each 9 mm pot's anti-rotation tab drops into a 1 mm slot printed in the underside of the shell, so turning a knob can't twist the pot. The board takes the push of a knob through the bosses.
- **Bushings** come up ≈ 2.5 mm above the face, hidden under the knob skirt. No nut, no washer on top. If a pot wobbles in a print, a thin flush nut in a 1.2 mm counterbore is the fallback (still under the knob, so it never reads as a screw).
- **Toggles:** the same way, with a printed anti-rotation key. Their bats stand up through 6.5 mm holes.

### Keys through the top face
- Strip C (with 25 switches and sensors) screws **up** to four bosses under the key zone. The switch stems stand in the **key window**: one opening x 3–273, y 3–49.5, with the 2.4 mm front wall in front of it.
- **The key tops go on last, from above**, pressed onto the stems through the window (they're the only parts fitted from the top). A top comes off with a fingernail.

### The stick
- The Delrin gate plate drops into a pocket on the shell's underside and is held by the main board. The stick rises through the slot, and **its cap goes on after** (eng §v1.5b order).

### Assembly order (F9)
1. Shell face down on a towel.
2. Press in the heat-set inserts.
3. Gate plate into its pocket.
4. Main board in: shafts, bushings and stick up through their holes; screw it up (10 × M3).
5. Strip C onto its 4 bosses.
6. I/O board onto the rear-wall bosses; plug its cable into the main board.
7. Battery (on a strap on the back panel) and speaker (glued to the back panel) on their JST leads; plug in.
8. Back panel on: **8 × M3 from underneath** into the shell's bottom rim. Feet go on the panel.
9. Flip it over. Press the key tops on, push the knobs on, fit the stick cap.

### Service (F10)
- **Back panel off (8 screws):** battery, speaker, BOOTSEL (the Pico faces down on the board) and every solder joint on the board's underside are reachable.
- **Board out:** pull the knobs and the stick cap, undo 10 screws, lower the board.
- **One key:** pull its top from above. A switch: strip C out from below (4 screws).

### The print and the "unibody" question (Vector Space printers)
- **The shell must print face down** (best surface, legends by one filament swap; and ONE SHEET's whole idea is the face-down first layer).
- **One piece needs a bed ≥ ≈ 285 mm** (ONE SHEET 276 × 140; HUSH 290 × 144):
  - Prusa MK3 / MK4 / Core One: ≈ 250 × 210 → **no**, even diagonally [CALC].
  - TAZ 6: 280 × 280 (UNVERIFIED at Vector Space) → ONE SHEET fits with ≈ 2 mm a side and no brim: **marginal**. HUSH: no.
  - Voron 2.4 / Trident: comes in 250 / 300 / 350 sizes; which one Vector Space has is UNVERIFIED. 350 fits both.
  - Gigabot: ≈ 590 class (UNVERIFIED) fits both.
- **Recommendation:**
  - **ONE SHEET:** print in one piece on the Voron if it's the 350 (ask Vector Space); otherwise the split below.
  - **HUSH:** split. The felt covers the seam completely, so there's no reason to queue for a big printer.
- **Split that doesn't read as a seam:** at **x = 122.5**, the one break line that runs straight through the whole panel. The face's sunk break groove (0.6 × 1.2 mm) is centred on the joint, so the joint sits at the bottom of a groove you'd see anyway. Inside: a 10 mm printed lap along the joint with 3 × M3 from inside; the back panel spans the joint and stiffens it. Parts: left 122.5 × 140, right 153.5 × 140 → both fit a 250 × 210 bed ✓. On the walls the joint shows only on the front wall (a 3 mm-tall line under key E-F, in the shadow of the key fronts) and the rear wall.

## 6. Shared interaction details (unchanged unless stated)

- Status light: one bicolour LED at (262, 68), states per `jobs.md`.
- Stick gate: Delrin, fore-aft slot, stem + 0.3 mm, full throw (up and down).
- VEL toggle: ON-OFF-ON, LOUD / BOTH / FILT, read through a spare CD4067 channel [ENG]; three-word scale.
- RANGE: engraved 6-position scale (LO, 32', 16', 8', 4', 2') [ENG].
- Keys: short tops (S1) everywhere. Piano-length tops = +$29.85 stabilisers, variant only.

## 7. Rule R4 (still binding)
- Nothing stands proud of the panel among the knobs (no dividers, walls, ridges, raised plates); separations are flush.
- Nothing rises between keys and controls; white keys within ≈ 3 mm of the panel.
- Side and rear rims allowed only ≥ 12 mm from any knob edge (this is why FOLD is 286, not 276).

## 8. Eng questions raised by rev 6
- **E-L9** main board ≈ 268 × 85 (flat concepts): does the voice fit? FOLD's two-board split: see FOLD.
- **E-L1** closed (stick and MOD on the main board).
- Speaker (240, 113): ≥ 30 mm from the ladder/expos at layout?
- Still open from before: E-L8 (18T push-on knobs on the pots, WAVE shafts), #2765 cap ≤ 12 mm in hand.
