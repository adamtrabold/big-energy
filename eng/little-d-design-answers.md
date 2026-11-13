# Little D: engineering answers to the design team (E-L2, E-L4, E-L5)

Status: rev 0, 2026-11-12. Answers `design/little-d/notes/systems.md` (open questions) and the E-L items in
`concepts/common-how-it-works.md` (rev 2), `concepts/under-glass/how-it-works.md` and `concepts/hush/how-it-works.md`.
Conventions as `budget-variant.md`: link = read this session; **ESTIMATE** = my number; **UNVERIFIED** = source exists,
figure not confirmed; **[ENG]** = engineering judgement; **[CALC]** = arithmetic shown. Constraints only: where a
part goes on the panel, and what anything looks like, stays the design team's call.

## 0. Bottom line

- **E-L2:** the BOM speaker (Adafruit #1313, 3") is **25.5 mm deep**. It can't fit under any panel ≤ 40 mm, and a
  board cutout doesn't help either (3 + 25.5 = 28.5 is above a 26–27 panel). I found **no 3" (66–77 mm) speaker ≤ 10 mm
  deep** at US distributors. **Use a 50 mm thin speaker: Same Sky CDS-5076-1SP, 7.6 mm, $3.88** (alt. PUI AS05008MR-4-R,
  7.2 mm, $4.13). **No board cutout is needed.** Common panel top ≈ **22.7–24.2** (the 26–27 target holds with ≥ 2 mm
  spare). UNDER GLASS keeps the 1 in rail (body 25.4, knob tops ≈ 35) if the board keeps lead tails out of the speaker
  footprint. Cost: about 4–6 dB quieter than a typical 3" and less low end. It's fine for playing at arm's length;
  bass is for headphones/line. **Spec change: budget-variant rev 9.**
- **E-L4:** **yes, with conditions.** The band is the natural place for the ladder, which sits right in front of
  CUTOFF/EMPHASIS. It's acceptable for the three expo arrays. Parts in the window band must be **≤ 6.5 mm tall**
  (glass underside is 7 mm above the board), so the AS3046s are soldered directly or in low-profile sockets. Keep
  heat (LD1117, MC34063s, 78L/79L09, LM386) and digital (key harness, CD4067s, Pico) **≥ 25 mm** from the windows.
  Each VCO's base network must stay within ≈ 15 mm of its chip.
- **E-L5:** **works.** A hidden arm with the magnet 10.5 mm behind the stem and the peg in front is fine: a 1.75u-length
  top runs unstabilised. Tilt moves the magnet ≤ ≈ 0.1 mm, and that shows up as an offset, not a velocity error.
  **Felt contact at 2.5 mm doesn't touch the velocity measurement in any tolerance case** (§3.3). One new constraint:
  the felt must **not grip the peg shank**, because friction would make velocity uneven from key to key and slow the
  return.

---

## 1. E-L2: speaker depth

### 1.1 Candidates (US distributors, qty 1, read 2026-11-12)

| Part | Size | Depth (seated max) | Power | Range | Sensitivity | Price, stock | Fit |
|---|---|---|---|---|---|---|---|
| Adafruit #1313 (current BOM) | 3" (77.8 mm) | **25.49 mm** | 1 W | — | not given | $1.95, in stock ([Adafruit](https://www.adafruit.com/product/1313)) | **No.** Too deep for any concept |
| **Same Sky CDS-5076-1SP (pick)** | **50 mm** round | **7.6 mm** | 1 W (1.5 max) | 280 Hz–20 kHz | 102 dBA @ 1 W/0.1 m → **≈ 82 dB @ 1 W/1 m** [CALC, −20 dB] | **$3.88, 498 in stock** ([DigiKey](https://www.digikey.com/en/products/detail/same-sky-formerly-cui-devices/CDS-5076-1SP/22521367)) | **Yes** |
| PUI AS05008MR-4-R (alt.) | 50 mm | **7.2 mm** | 1.5 W (2 max) | 350 Hz–20 kHz | 92 dBA @ 0.1 W/0.1 m → ≈ 82 dB @ 1 W/1 m [CALC] | $4.13, 2,021 in stock ([DigiKey](https://azcus.digikey.com/en/products/detail/pui-audio-inc/AS05008MR-4-R/1745548)) | Yes |
| Soberton SP-5009 | 50 mm | 8.5 mm | 0.5 W | 300 Hz–8 kHz | 93 dBA @ 0.1 W/0.1 m | $3.67, **0 stock** ([DigiKey](https://www.digikey.com/en/products/detail/soberton-inc/SP-5009/8600822)) | Out of stock |
| PUI ASE06008MR-LW150-R | 60 × 30 mm rect. | 10.3 mm | 3 W | 400 Hz–20 kHz | 83 dBA @ 1 W/0.5 m | $6.51 ([DigiKey](https://azcus.digikey.com/en/products/detail/pui-audio-inc/ASE06008MR-LW150-R/4700909)) | Too deep for UNDER GLASS |
| PUI AS06608MR-R | 66 mm | 12.5 mm | 0.5 W | 380 Hz–7.5 kHz | 84 dB | DigiKey 357 ([PUI](https://puiaudio.com/product/s/AS06608MR-R)) | Too deep (panel +3.5) |
| Visaton K 70 | 70 mm | 19.7 mm | 2 W | 170 Hz–20 kHz | 85 dBA @ 1 W/1 m | ([DigiKey](https://www.digikey.ca/en/products/detail/visaton-gmbh-co-kg/K-70-8-OHM/17799849)) | Too deep |
| CB Gitty 3" low profile (2-pack) | 3.5" | 1.25" (31.8 mm) | 1 W | — | — | $8.09/2 ([CB Gitty](https://www.cbgitty.com/kits-guitar-kits-amp-kits-more/amplifier-effects-kits/amp-parts/2pc-3-inch-low-profile-8-ohm-audio-speakers/)) | No |

The search wasn't exhaustive, but every 66–77 mm part I found was ≥ 12.5 mm deep.

### 1.2 Loudness and bass with the LM386

- **Drive:** the LM386 runs on the 5 V rail (Part 2 §2.4). The LM386N-1 is rated 325 mW typ (250 mW min) at 6 V into 8 Ω
  ([Wikipedia table](https://en.wikipedia.org/wiki/LM386)), so ≈ **0.2 W at 5 V** [CALC, (5/6)² scaling; ESTIMATE].
  Both 50 mm parts are rated ≥ 1 W, so there's no risk of overload.
- **Level:** 82 dB @ 1 W/1 m − 7 dB (0.2 W) ≈ **75 dB at 1 m**, ≈ **83 dB at a 0.4 m playing distance** [CALC]. That's a
  practice level, like a handheld synth's speaker. A typical 3" paper cone is ≈ 86–88 dB @ 1 W/1 m (ESTIMATE; Adafruit
  publishes none), so the thin part is **≈ 4–6 dB quieter**.
- **Bass:** the stated low limits are 280–350 Hz. Below that the output falls ≈ 12 dB/oct, and a shallow sealed cavity
  raises it further. Bass-note fundamentals (C2 = 65 Hz, C3 = 131 Hz) are heard only through their harmonics, so low
  lines sound thin. That's acceptable for "keep the speaker" (sketching, checking a patch). It's not a bass monitor:
  phones/line carry the real sound. A 3" wouldn't get there either at 0.2 W.
- **Option, not adopted:** two CDS-5076 in parallel (4 Ω; the LM386 is specified into 4 Ω, UNVERIFIED at 5 V) give
  ≈ +3–4 dB for +$3.88 and twice the footprint. The PAM8302 route (Part 2 §5) is the other louder path.
- **Mounting:** the speaker faces down through a grille in the bottom, with feet 6–8 mm (common §3), so the desk
  acts as a boundary (≈ +3 dB in the low mids, ESTIMATE). Glue it or clamp it to the bottom sheet's inner face.

### 1.3 Resulting heights

Assumptions: bottom 3 mm; speaker on the bottom's inner face; 0.5 mm air; board 1.6 mm; THT lead tails 1.5 mm;
pot body 7 mm above the board (the design's figure; Tayda 9 mm pot body height UNVERIFIED); panel 3 mm.

| Case | Main-board underside | Board top | Panel top |
|---|---|---|---|
| **Common, speaker footprint kept free of lead tails** (traces only) | 3 + 7.6 + 0.5 = **11.1** | 12.7 | **≈ 22.7** |
| Common, lead tails over the speaker | 12.6 | 14.2 | **≈ 24.2** |
| Common with the old 3" #1313 | 30.5 | — | ≈ 42 (and 28.5 even with a board cutout): **not possible** |
| **UNDER GLASS** (board top fixed at 14 by the 1 in rail, so underside 12.4) | free height 12.4 − 3 = 9.4 | 14 | glass top 24, **body 25.4, knob tops ≈ 35, unchanged** |

- **UNDER GLASS:** 9.4 − 7.6 = 1.8 mm with a lead-free footprint (2.2 mm with the PUI). With lead tails it's 0.3 mm:
  too tight. **Constraint:** a lead-free keep-out on the board underside, ≈ 54 mm diameter (50 + 2 mm each side),
  over the speaker. **No board cutout.** The 1-1/4 in rail fallback isn't needed.
- **The other concepts:** the panel target of 26–27 holds with **2.8–4.3 mm spare**. That spare could go toward a
  thinner body if the design wants it. Whether to use it is a design call.
- **Battery:** Adafruit #2011 is 60 × 36 × **7 mm** ([Adafruit](https://adafruit.com/products/2011)), so it fits the
  same under-board space (UNDER GLASS 9.4 − 7 = 2.4 mm, with a lead-free area too).
- **Magnetic:** keep the speaker ≥ 60 mm from the Hall sensors (rule unchanged). It's a smaller magnet than the 3",
  so the margin only improves.
- **Placement constraint (E-L4 link):** keep the speaker and its leads ≥ 30 mm from the ladder and expo arrays, and
  twist the leads. Speaker current loops near a high-EMPHASIS ladder risk feedback and squeal [ENG]. The common
  position (170, 128) is ≈ 10 mm behind the ladder window's left end, so move it or confirm the clearance at layout.
  Where it goes is the design's call.

---

## 2. E-L4: UNDER GLASS window band (y ≈ 80–96, 16 mm)

### 2.1 Does it fit?

| Window | Parts | Footprint [CALC] | Verdict |
|---|---|---|---|
| **VCO, x 60–122 (62 mm)** | 3 × AS3046 DIP-14 (19.3 × 6.35 body; 20.3 mm with socket) laid along x + 3 tempcos | 3 × 20.3 = 61 mm in a row, so a **socketed row fills the window with no gap**. Soldered directly: 3 × 19.3 + 2 × 1.5 = 61 mm, still tight | **Fits for the chips + tempcos only.** Each VCO's base network (≈ 4–6 resistors) and summing op-amp can't also fit (≈ 380 mm² per VCO against 330 available). They sit just behind, within ≈ 15 mm of the chip, using the empty middle position in VCO 1's front row (x ≈ 78–92) and the gaps between pots. The chips can't stand along y: 19.3 mm > 16 mm |
| **Ladder, x 180–254 (74 mm)** | Input pair + 4 rung pairs (10 × TO-92, hand-matched pairs glued face to face), 4 film caps, filter expo pair | Pairs in one row at ≈ 13 mm pitch = 65 mm; caps in a second row; 2 rows ≈ 12–14 mm tall | **Fits well.** CUTOFF (188), EMPHASIS (212) and CONTOUR AMT (236) sit directly behind at y 104, so the feedback and CV traces are the shortest of any layout. The mixer (OSC 1 at x ≈ 140, y 104) feeds in from the left |

- **Height under the glass:** board top 14, glass underside 21, so **≤ 6.5 mm seated** in the band (0.5 mm air):
  - AS3046 soldered directly (≈ 4.5–5 mm) or in a **low-profile turned-pin socket**. A standard socket plus chip is ≈ 7 mm: UNVERIFIED, check one.
  - TO-92s pressed down to ≤ 6.5 mm.
  - Tempcos and film caps laid flat or chosen ≤ 6.5 mm (Tayda box-cap height UNVERIFIED).
  - This matches the rest of the board under the panel, which is limited by the 7 mm pot body anyway.
- **Edge clearance:** the front pots' pins reach y ≈ 97–98 and a 16 mm rotary body at y 104 reaches y 96 (RS16211
  body diameter UNVERIFIED). The band is clear, but there's no slack at its rear edge.

### 2.2 Does it hurt the layout?

| Concern | Finding | Constraint |
|---|---|---|
| **Thermal coupling (tempco ↔ expo)** | Unaffected, provided each tempco is bonded to its own AS3046 (thermal epoxy on the package top or side). The matched pair is on one die, so uniform warming of the chip cancels in the pair | Tempco touching its chip. Within the band, chips at ≥ 1.5 mm gaps |
| **Heat sources nearby** | LD1117V33 (0.43 W worst case, `velocity-and-keys-v2.md` §2.4) is placed "at the strip connector", which is probably the main board's front edge, i.e. this band. Also MC34063s, 78L/79L09, LM386 (≈ 0.2–0.3 W) | **≥ 25 mm from either window** [ENG]. Route the strip connector at a section gap or an end, not under a window |
| **Radiant heat through clear windows** (lamp or sun) | Warms the black packages. The die pair tracks, the tempco tracks if bonded, and autotune plus background re-tune absorb the rest | None beyond the bonding. Note it in the build guide |
| **Short traces** | Ladder: better than elsewhere. VCO 1: natural (its RANGE/WAVE are in the front row). **VCO 2/3:** the cores sit 23 / 46 mm in front of their own rows, so the core-to-WAVE-switch traces run ≈ 25–50 mm. These are buffered, low-impedance waveforms, fine on 2 layers [ENG] | Keep each expo base node (high impedance) within ≈ 15 mm of its chip. Long runs only on buffered outputs |
| **VCO-to-VCO coupling** (soft locking at small detune) | Three cores side by side is how the original single oscillator board was laid out, so it's not new. The risk is through shared rails and reset-pulse edges | Per-core decoupling (10 µF + 100 nF at each chip); reset/comparator traces not run past a neighbour's base node |
| **Digital noise** | The key scan is ≥ 4 kHz per key (mux edges at ≈ 100–250 kHz) and the harness comes from strip C, which is in front of this band | **Key harness, CD4067s, Pico and PWM lines ≥ 20–25 mm from the windows**; solid bottom-layer ground under both windows; no digital trace crossing the band |
| **Speaker** | §1.3 | ≥ 30 mm from the ladder and expos |

**Verdict:** feasible with no penalty to the audio path and a small benefit for the ladder. It costs layout freedom:
the band takes these parts and nothing hot or digital. If those constraints can't be met at layout, the windows
follow the parts, as the concept already allows.

---

## 3. E-L5: HUSH hidden arm, peg and magnet

### 3.1 Geometry

- **The carrier:** a blank 1.75u low-profile MX-stem cap is hard to source (UNVERIFIED). The shared method already
  works here: a **laser-cut 3 mm acrylic (or maple) arm with an MX cross pocket** (common §5). It's hidden under the
  deck, so it can be any shape. Arm ≈ 30 × ≤ 15 mm. Whites at an 18 mm pitch leave ≥ 3 mm between arms.
- **Heights (same as common):** arm top ≈ 17.5, underside ≈ 14.5. Magnet face at 13.7 = strip 6.1 + 7.6 rest gap
  (`velocity-and-keys-v2.md` §2.2), so the magnet protrudes ≈ 0.8 mm below the arm or sits on a 0.8 mm boss. Deck
  underside at 19 leaves **1.5 mm** above the arm at rest. The arm only moves down, so that's OK.
- **Peg:** shank from the arm top (17.5) through the deck (19–22) and felt (22–25); head underside at 27.5 (2.5 above
  the collar). Free shank ≈ 10 mm. The peg's shank and head dimensions are the design's (the 1/2 in plug spec doesn't
  say whether that's head or shank).
- **Magnet:** its centre is 10.5 mm from the stem. It can sit in front of or behind the stem, which is free for
  sensor placement: ≥ 18 mm to any neighbour's sensor (crosstalk unchanged from §2.2 there).

### 3.2 Lever arm, rocking and velocity

| Peg position | Press offset d from stem | Moment | Effect |
|---|---|---|---|
| **Peg centred over the stem** (arm carries only the magnet) | 0 | 0 | No rocking at all. **Mechanically best** [ENG] |
| Peg at the front end of a 30 mm arm, stem centred | ≈ 8.7 mm (15 − 6.35) | F·d | 1.75u keys (e.g. Caps Lock) are pressed this far off the stem without stabilisers in normal keyboards [ENG, not sourced]. OK |

- **Tilt:** stem-to-housing play takes up a small angle θ (Choc V2 figure UNVERIFIED; ≈ 0.5° assumed). The magnet,
  10.5 mm on the far side, moves 10.5 · tan 0.5° ≈ **0.09 mm** opposite the stroke [CALC], ≈ 3 % of 2.8 mm travel.
- **Why that doesn't spoil velocity:** a peg fixes the press point, so the tilt is the same every press. Play is taken
  up at force onset, before or at the start of travel, so it shifts the reading as an offset that rest/bottom
  learning absorbs. The slope fit over 0.4–2.1 mm sees a ≈ constant offset, not a slope change [ENG]. Pressing the
  peg-head edge (±6 mm) changes θ slightly: still an offset per press, ≲ 0.05 mm, < 1 MIDI step at the fit's
  resolution (≈ 1 step RMS budget, `velocity-and-keys-v2.md` §2.2) [ENG].
- **Head landing:** at 0.5° tilt the 12.7 mm head's edges differ by 0.11 mm, against 0.3 mm of felt compression. It
  lands evenly enough.
- **The bench test confirms it** (`velocity-and-keys-v2.md` §2.6 item 6). Add: a 30 mm arm pressed at d = 0 and at
  d = 8.7, logging rest and bottom counts.

### 3.3 Felt stop at 2.5 of 2.8 mm and the velocity window

The firmware thresholds are fractions of each key's **learned** travel b: note-on at 0.70 b, fit window 0.15–0.75 b.
Felt contact c = 2.5 ± 0.2 mm (F3 tolerance ESTIMATE, from the concept). Switch travel 2.8 ± 0.25 mm
(`velocity-and-keys-v2.md` §2.1).

| Case | Learned bottom b | Window end 0.75 b | Contact c | Margin |
|---|---|---|---|---|
| Nominal | 2.8 (switch bottoms, felt −0.3) | 2.10 | 2.5 | **0.40 mm** |
| Worst: long switch, early felt | ≤ 3.05 (felt can compress at most 3.05 − 2.3 = 0.75) | ≤ 2.29 | 2.3 | **≥ 0.01 mm**, still after the window. In practice firm F3 compresses far less than 0.75 mm, so felt becomes the stop at ≈ 2.4, b ≈ 2.4 and the window ends at 1.8 (**0.5 mm**) |
| Short switch, late felt | 2.55 (switch bottoms before the felt) | 1.91 | 2.7 (no contact) | No effect; you just lose the felt softening |

So contact always comes **after** the fit window and note-on, because 0.75 × max travel (2.29) < min contact (2.3).
**Velocity measurement is unaffected.** Per-key learning absorbs felt thickness variation. Keep the felt
tolerance at ±0.2 mm or better: at ±0.3 the worst corner crosses by 0.06 mm.

### 3.4 New constraint: no felt drag on the peg

HUSH's deck says the holes are "cut 1 mm under the peg diameter (the felt wipes each peg)". If the felt grips the
**moving shank**:
- Friction adds a force of roughly 5–20 gf (ESTIMATE). That lowers the speed reached for a given finger force, and
  it varies with each hole, so **velocity is uneven from key to key**. Position learning can't correct a speed effect.
- Against the Choc's light top-of-stroke return force, it risks a **slow or incomplete return** (switch force curve
  UNVERIFIED).

**Constraint:** the felt and ply holes must clear the moving shank (≥ 0.5 mm radial, which also covers tilt). If a
covered hole is wanted, the head can overlap the hole instead of the felt touching the shank. How it looks is the
design's call. A stationary felt collar the head lands on is fine.

---

## 4. Spec changes made in `budget-variant.md` (rev 9)

- §v1.2 VCA/output row: speaker 50 mm thin; layout keep-out.
- §v1.3 speaker line: Adafruit #1313 → **Same Sky CDS-5076-1SP, $3.88** (+$1.93); alt. PUI AS05008MR-4-R.
- §v1.8 risks: speaker keep-out, window-band rules (UNDER GLASS only), felt drag (HUSH only).
- §v1.10 totals: **+$2**, so (a) ≈ $260–325 and (b) ≈ $244–307. It rides on the existing DigiKey/US order (ESTIMATE:
  no shipping change).

## Sources
- Adafruit #1313: https://www.adafruit.com/product/1313
- Same Sky CDS-5076-1SP: https://www.digikey.com/en/products/detail/same-sky-formerly-cui-devices/CDS-5076-1SP/22521367
- PUI AS05008MR-4-R: https://azcus.digikey.com/en/products/detail/pui-audio-inc/AS05008MR-4-R/1745548
- Soberton SP-5009: https://www.digikey.com/en/products/detail/soberton-inc/SP-5009/8600822
- PUI ASE06008MR-LW150-R: https://azcus.digikey.com/en/products/detail/pui-audio-inc/ASE06008MR-LW150-R/4700909
- PUI AS06608MR-R: https://puiaudio.com/product/s/AS06608MR-R
- Visaton K 70: https://www.digikey.ca/en/products/detail/visaton-gmbh-co-kg/K-70-8-OHM/17799849
- LM386 output power: https://en.wikipedia.org/wiki/LM386
- Adafruit #2011 LiPo: https://adafruit.com/products/2011
