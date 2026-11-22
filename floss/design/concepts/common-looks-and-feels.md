# floss: what BOW, KEPT and TIDE share (visual)

Status: **rev 1, 2026-11-22**, product designer (visual focus), concept round 1. Read with `common-how-it-works.md` (systems rev 1) and `../jobs.md` (rev 1). Each concept's `how-it-looks-and-feels.md` covers only its own face and departures.

Pictures:
- `compare-faces.png`: the three plans at the same scale, plus a table of what differs.
- Per concept: `mock-A-look.png` (a 3/4 view, the idea, principles, facts) and `mock-B-real-size.png` (the plan at 1:1; print on A3 at 100%; the scale bar is 50 mm).
- Source: `_src/fl.py` and `_src/concepts.py` (run `python3 concepts.py`).
- **Fidelity:** concept-level. The 3/4 views are orthographic drawings made of stacked slices, not photoreal renders: there's no OpenSCAD or POV-Ray here. Legends use Inter as a stand-in for the family's Kalam, which isn't installed. Positions on the real-size sheets are exact to systems' maps plus the changes each concept file lists. They haven't been run through a layout checker yet.

## 1. One family, three bodies
Each concept wears a body Big Energy already has, so the choice between them is a real choice of point of view, and every option is reuse (J20). They differ in kind: body, key material, hero and speaker are all different. The labels are not the only difference.

| | BOW | KEPT | TIDE |
|---|---|---|---|
| Life lives in | each finger | 1974 | time |
| Body | CATHEDRAL base; the lid is the speaker box | ONE SHEET printed shell | HUSH felt pebble |
| Size | 286 × 132 × 27.6 base, ≈ 55 closed | 276 × 148 × 24 | 290 × 186 × 25.5 |
| Keys | dark naturals, bone sharps, felt collars | white and black caps | maple pegs on felt collars |
| Coral (one control) | pressure | ensemble depth | drift (Ø 24, on the axis) |
| Knobs | black low Ø 10 × 8 (CATHEDRAL's base part) | cream KN1250 Ø 14.9, rings round them | cream KN1250 Ø 14.9 on felt tags |
| Speaker | cloth lid, passive radiator | slots across the back band, no radiator | punched felt, the lantern, a radiator underneath |
| Carry | the lid closes over the keys | sleeve | sleeve |

## 2. Rules every concept follows

### 2.1 The split reads truthfully on a symmetric face (J3, J13)
- **The axis runs through the centre of middle C**, the 13th of the 25 keys. Each half's controls fill 126 mm either side of a centre gutter one key wide (18 mm; TIDE widens it to 28 for DRIFT).
- **The only split mark is a coral tick on the front rim between B and C** (1.2 × 3.8 mm, on the case's top face at the rim). No line is drawn through the face.
- **OCTAVE L and OCTAVE R sit at the two outer ends of the front row.** These are the two controls you feel for, so they're the biggest knobs on the face after the hero (BOW Ø 14 against Ø 10; KEPT and TIDE share one size but sit at the ends).
  - **Reading:** pointers parallel = one keyboard; pointers apart = split. The positions print above the word as *−2 · −1 · 0 · +1 · +2*, so the difference between the two numbers is the interval.
  - Detents: 5 major ticks, one per step, ±60° about twelve o'clock (CATHEDRAL's "a stepped knob shows only where it can stop").

### 2.2 Coral marks where the life lives
- **One coral control per concept, and a different one each time.** The coral also appears in the rim tick and the HOLD dot (BOW, KEPT).
- **Open:** no bought coral knob has been checked yet. Fallbacks, in order:
  1. an orange or salmon anodised knob, if one reads as coral beside walnut and cream;
  2. the concept's normal knob with a coral printed cap insert;
  3. the normal knob with a coral pointer line (Big Energy CUTOFF's red-line precedent).

### 2.3 The gutter carries only shared things
- BOW: the strand names and TAP. KEPT: TAP. TIDE: HOLD, DRIFT and the status light.
- **TAP's lit bezel is the status light in BOW and KEPT** (CATHEDRAL's precedent, round 6). That's one part instead of two, and it puts the light on the axis.
  - **Change to systems' common §2.9:** the light becomes TAP's ring instead of a separate LED. It still has the same three meanings.
  - TIDE keeps a separate light behind DRIFT, because its TAP is in the echo group.

### 2.4 Marking and type (CATHEDRAL's system, carried over)
- **Ticks:**
  - One ring at r + 1.7; ticks 0.35 wide, major 1.0 long, minor 0.55.
  - Continuous knobs: 11 ticks over 300°, the ends major.
  - Stepped knobs show their detents only: octave 5 at ±60°, the 4-way selectors at ±45° / ±15°.
- **Words:**
  - Every control's word sits **above** it. Named positions sit above the word, in step order (*swell · vibrato · tone · shimmer*; *analog · wide · glass · tape*).
  - One word per label, lowercase. That's Kalam in the family; this round's pictures use Inter.
- **The shimmer's Daisy modes are named *wide · glass · tape* (my proposal).** They're plain, one word each, and each says what you'd hear: a wider ensemble, an octave-up glassy shimmer, a slow tape wobble. "analog" names the BBD mode by what it is, which is what the owner asked for.
- **Strand names (BOW):** *low · main · high*. They're printed once, in the gutter, with low nearest the keys, so the column reads as pitch rising away from you.

### 2.5 States you can see or feel, common to all three
| State | Shown by |
|---|---|
| fine / charging / low battery | the status light: steady / slow pulse / flashing (BOW and KEPT: TAP's ring; TIDE: the light behind DRIFT) |
| split or not, and by how much | the two octave pointers, by eye or fingertip |
| a register on or off (BOW, KEPT) | the rocker's position plus an ink bar on the "on" half; readable in sun and by touch |
| HOLD on | BOW and KEPT: a latching push button sits about 1.5 mm lower when latched (feel), plus its coral dot lit. TIDE: the peg stays down (push-push) |
| a half muted (all its tabs off) | all that half's rockers off. No extra light, because the tabs are the state |
| headphones in, speaker quiet | nothing on the face. The plug in the rear jack is the sign (as on Big Energy) |
| MIDI moved a setting | nothing (systems §2.9: jump-on-move; the light keeps three meanings) |

### 2.6 Feel, common to all three
- **Octave knobs:** a firm detent, so the pointer is never between steps. Turning while holding never jumps (systems' rule). The click is the confirmation.
- **Rocker tabs:** a short, definite snap. You play them while playing.
- **HOLD:** a deep latching click. In TIDE it's a peg you press like a key.
- **Keys:** about 3 mm straight down on the family's Choc V2 / Hall carrier. With the felt collars (BOW, TIDE), the bottom of the press has a little give, so leaning in feels like bow pressure. **Eng:** does the collar help or blur per-key pressure sensing?

## 3. Changes to systems' maps, and why
| Concept | Change | Why |
|---|---|---|
| all | the status light = TAP's lit ring (BOW, KEPT) | CATHEDRAL precedent; one part; on the axis |
| KEPT | attack and release move to the rear row; volume to the front; ensemble behind depth; the blank moves to rear-left | the front row was 5 + 5 dense with tabs; kinds go behind amounts (ensemble behind depth, time behind echo) |
| KEPT | depth 140 → 148 | the back-band grille's slots (y 124–140) clear the rear row's words |
| TIDE | rebalanced: front octave L · tone · shimmer · depth \| HOLD \| echo · reverb · tap · octave R; rear (blank) · attack · release · pressure \| DRIFT \| repeats · time · tempo · volume | systems' rear row was 2 \| 5; this is 4 \| 4 front and 3 \| 4 rear. TAP is played, so it goes in front; FREE / SYNC sits beside TIME and behind TAP |

## 4. Open (visual), all concepts
1. A coral knob part (§2.2).
2. Kalam for final legends (the GitHub fonts URL was blocked for Big Energy; find another source).
3. A layout checker run on all three maps (systems' rules: pitch, edge 15 mm, ≥ 7 mm knob to break), once the director picks.
4. Real renders (standing, closed, in a hand) for the concept that goes forward.
