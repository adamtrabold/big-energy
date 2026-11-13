# Little D / FOLD: engineering answers to the director's round-4 FOLD fixes (2026-11-12)

Inputs: `battery.md` rev 11, `round4-answers.md` (§1.4 board area, §2 ribbon, §3 power), `budget-variant.md` rev 11, `design/concepts/fold/how-it-works.md` rev 4.2, `design/scores.md` round 4 (FOLD rulings 1–2).
Conventions: **[CALC]** arithmetic shown; **ESTIMATE** my number, not checked; **UNVERIFIED** source exists but figure not confirmed; **[SIM]** ngspice result from the files named. Prices and stock were read 2026-11-12.
I state constraints only. Layout and look are the design team's calls.

## 0. Bottom line

1. **Slim cells do fit the ≈ 31 mm band, but they don't get the halves back to 86–90.**
   - Best US-stocked fit: **PiShop 952540**, 9.5 × 25 × 40 mm, 750 mAh, with PCM, $7.95, listed in stock.
   - Four in parallel use ≈ 176 mm of band and give **11.1 Wh: ≈ 4.5 h at 2.0 W, ≈ 2.4 h at 3.6 W**. That's about half the 22 Wh pack.
   - **The depth wasn't the battery's to give back.** The halves went from 86 to 100 for **lid board area** (`round4-answers.md` §1.4; FOLD rev 4.1 says so). Only the step from 100 to 116 was the battery.
   - Under the plate the lid has 10.6 mm in total, so cells and board compete for the same plan area. Any cell in the band takes board area away.
   - Required depth [CALC, §1.3]:

     | Battery | Depth, ladder in the lid | Depth, ladder in the base |
     |---|---|---|
     | No internal cell | ≈ 95 | **≈ 87** |
     | 4 × 952540 slim pack | ≈ 113 | ≈ 105 |
     | 22 Wh pack (current) | ≈ 121 | ≈ 113 |

   - **A depth of ≤ 90 with an internal battery isn't reachable** without a stacked lid board (+10–12 mm closed) or moving more of the lid's circuitry to the base. That's the owner decision the director anticipated: tell him plainly.
2. **EMPHASIS can sit beside CUTOFF, with two wires crossing the ribbon.** Conditions are in §2.5.
   - The round-4 worry rested on a "high-impedance base node". In the CA-72 netlist, though, EMPHASIS is a two-terminal rheostat between two low-impedance nodes:
     - C10 out of the output buffer, ≈ 150 Ω;
     - R73/R76 into the bypassed input-pair bias, ≈ 0.5–1.3 kΩ.
   - **[SIM] Line length/capacitance has no effect.** A worst-case 100 mm cable model passes all 46 golden filter checks, and self-oscillation onset doesn't move.
   - **[SIM] Pickup is the real constraint.** The emphasis-input wire must see **≤ 0.05–0.1 pF** from any mux-select line, which means putting it at the ribbon edge farthest from S0–S3, with guards.
   - The ribbon goes to **40-way**.
   - The bench test from round 4 still gates the board order. Its pass level is now set (§2.6).
3. **Ladder in the base:** feasible and about neutral on conductor count, and it frees ≈ 2,000 mm² of lid board (ESTIMATE). That's the only route in §1.3 to ≈ 87 mm, and only with no internal cell. The cost:
   - the mixer bus crosses (it's 8 dB *less* pickup-sensitive than the emphasis-input wire [SIM]);
   - ±9 V crosses;
   - the base PLAY strip goes from ≈ 46 % to ≈ 70 % fill.

---

## 1. Slim pouch cells for the lid band

### 1.1 Envelope (from FOLD rev 4.1/4.2, eng rules)
- **Band:** d ≈ 0–31, full width less rims. **Cell width ≤ 29 mm** leaves ≥ 1 mm each side; a 30 mm cell is marginal.
- **Height:** inner height 10.6 mm (15.1 − 2.5 plate − 2 back). **Cell ≤ 9.5 mm** leaves ≥ 1 mm of swell (`battery.md` rule).
- **Length along x:**
  - The speaker (60 × 30 × 10.3) also lives in the band, at x 205–265.
  - That leaves ≈ **180 mm** (x ≈ 18–200) for cells, ESTIMATE, if the ribbon header isn't in the band.
  - The old bay x 22–152 is 130 mm.
  - 250 mm only if the speaker leaves the band (layout call).
- **Pitch per cell:** length + 4 mm for the PCM and lead exit (ESTIMATE).

### 1.2 Candidates (US-stocked or US-listed)

| Cell | Size (T × W × L) | Capacity, Wh | Price | Protection, notes | Fit |
|---|---|---|---|---|---|
| **PiShop 952540** ([page](https://www.pishop.us/product/lithium-ion-polymer-battery-3-7v-750mah/)) | 9.5 × **25** × 40 | 750 mAh, 2.8 Wh | **$7.95**, "IN STOCK" | PCM: overcharge, 3.0 V over-discharge, short. **No thermistor**; charge ≤ 375 mA. JST-**XH**, 22 AWG, 30 mm leads. "35C" high-rate cell | **Best fit.** Width margin 3 mm each side. Thickness exactly at the 9.5 limit: measure one |
| US Electronics **USE-803048** ([DigiKey](https://www.digikey.com.br/en/products/detail/us-electronics-inc/USE-803048-1100-mAh/17799390)) | 8 × 30 × 48 (from the size code, UNVERIFIED) | 1050 mAh (DigiKey), 3.9 Wh | price/stock not shown (UNVERIFIED) | PCM and termination not stated on the page (UNVERIFIED) | Thicker margin, **30 wide is marginal** in 31. Need the datasheet tolerance |
| PiShop SKU 440 ([page](https://www.pishop.us/product/lithium-ion-polymer-battery-3-7v-900mah/)) | 6 × 30 × 48 | 900 mAh, 3.3 Wh | $8.95, **no add-to-cart** | PCM (3.0 V cutoff, short), no thermistor, JST-PH | Same width problem; stock doubtful |
| TinyCircuits 1000 mAh ([page](https://tinycircuits.com/products/lithium-ion-polymer-battery-3-7v-1000mah)) | 8 × 30 **±2** × 40 | 1000 mAh, 3.7 Wh | $9.95 | Protected; JST-SH | **Width can be 32: reject** |
| Jauch LP503040 / LP463042 ([DigiKey list](https://www.digikey.co.uk/en/product-highlight/j/jauch-quartz/lithium-polymer-batteries)) | 5 × 30 × 40 / 4.6 × 30 × 42 | 600 / 580 mAh | ≈ £6–7 (UK listing) | PCM | Too thin for the volume: wastes half the height |
| Adafruit #1578 (`round4-answers.md`) | 4.75 × 29 × 36 | 500 mAh | $7.95, in stock | PCM | Too thin; stacking two = 9.5 with no swell room. Reject |
| Long single cell (≈ 8 × 28 × 100–170) | — | — | — | — | **None found US-stocked** (also round 4). Searched Adafruit, SparkFun, PiShop, Parts Express, DigiKey (Jauch, US Electronics); not exhaustive |

**Pick: PiShop 952540 × N, 1S-NP.** It's the only in-stock cell that clears both width and height.

### 1.3 Packs, runtime, and what they cost in depth

Runtime uses `battery.md`'s method: cell power 2.22 W (2.0 W load, 90 % boost) and 4.24 W (3.6 W, 85 %); usable energy = 90 % of nominal. All ESTIMATE.

| Pack | Band length used | Nominal | Usable | 2.0 W | 3.6 W | Footprint incl. clearance |
|---|---|---|---|---|---|---|
| 3 × 952540 | 132 mm (fits the old 130 bay barely) | 8.3 Wh | 7.5 Wh | **3.4 h** | **1.8 h** | ≈ 3,560 mm² |
| **4 × 952540** | 176 mm | **11.1 Wh** | 10.0 Wh | **4.5 h** | **2.4 h** | ≈ 4,750 mm² |
| 5 × 952540 (band ≥ 220 mm: speaker out of the band) | 220 mm | 13.9 Wh | 12.5 Wh | 5.6 h | 2.9 h | ≈ 5,940 mm² |
| (ref) current 2 × 755060 bay | 130 × 52 bay | 22.2 Wh | 20.0 Wh | 9.0 h | 4.7 h | 6,760 mm² |
| (ref) old single #2011 | — | 7.4 Wh | 6.7 Wh | 3.0 h | 1.6 h | — |

- **Cost:** 4 × $7.95 = **$31.80** + bq25185 #6106 $8.95 = **$40.75**, about the same as now ($40.85).
- PiShop now supplies both cells and harness parts; Adafruit supplies the charger.

**Depth constraint [CALC]:**
- Lid board ≥ 21,500 mm² (`round4-answers.md` §1.4).
- Lid usable plan area = 262 × (D − 6). That reproduces rev 4.1's 22,800 mm² at D = 100.
- Subtract the speaker (1,800) and the battery footprint (A).
- So **D ≥ 6 + (23,300 + A) / 262**.

| Battery | Ladder in the lid | Ladder in the base (lid needs ≈ 2,000 mm² less, ESTIMATE) | Floor if circuitry were split perfectly between halves |
|---|---|---|---|
| None (power bank) | **95** | **87** | 90 |
| 3 × 952540 | 108 | 101 | 97 |
| 4 × 952540 | 113 | 105 | 99 |
| 22 Wh bay | 121 | 113 | 103 |

The perfect-split column assumes both halves share D; base board 270 × (D − 8), base PLAY strip at 70 % fill. It works out as D ≥ (47,900 + A) / 532 [CALC].

**Notes:**
- **Check rev 4.2's own number.** At D = 116, 262 × 110 − 6,760 − 1,800 = **20,260 mm²**, not the ≈ 22,500 stated. That's ≈ 1,200 under eng's 21,500 minimum [CALC]. The design team should recount before anything else moves.
- **The coupling is plain:** every 262 mm² of cell footprint costs 1 mm of depth on **both** halves (the director's "every FOLD change needs the open-depth check").
- **Ways under 100 with an internal cell** (design team / owner choices, not mine):
  - a stacked lid board, closed +10–12 mm (§1.4 there);
  - moving more non-panel circuitry to the base: the MC34063 supplies, MIDI and the DACs are candidates. Each adds ribbon lines, and the base rear strip only exists if D > 86;
  - accepting ≈ 105 with the slim pack and the ladder in the base.

### 1.4 Safety: N cells in parallel

The `battery.md` rules all carry over (same lot, voltage-match within 0.05 V before joining, check polarity, mount flat, no compression, retire puffy cells, store at 3.8 V). Specific to 3–5 small cells:

1. **One PCM per cell stays.** Don't strip them to build a bare-cell pack: that needs a pack-level BMS, and the project rules out SMD work.
   - If one PCM trips, the rest carry the load. With 4 cells at 3.6 W, end of discharge, that's ≈ 1.4 A / 3 ≈ 0.47 A each, under 1 C. Acceptable.
2. **A star harness, not a daisy chain:** each cell has its own lead to a common pair at the charger. That keeps current sharing even.
   - Put a **2 A polyfuse or fuse at the common point** (ESTIMATE +$0.50).
   - Optionally add a **≈ 1 A PTC in each cell lead** (ESTIMATE +$0.30 each), so a shorted cell can't be fed by its neighbours. This matters more with 4–5 cells than with 2.
3. **Charge current:** 375 mA max per cell (page). The bq25185 default of 1 A over 4 cells is 0.25 A each ✓. Over 3 cells it's 0.33 A ✓.
   - **Charge time ≈ 3,000 mAh / 1 A × 1.1 ≈ 3.3 h** (4 cells).
4. **Connectors:** these are JST-**XH**, while the charger board uses JST-PH. Make one adapter harness (XH ×N → PH), and check polarity on every cell.
5. **Thermal:** no thermistor. Same rule as before: don't charge unattended in the closed case. The closed lid band sits over the base's PLAY row, away from the regulators.
6. **Swell:** cells at 9.5 nominal in a 10.6 band leave 1.1 mm. **Measure the real thickness of one cell before freezing the band height.** If it's > 9.6, use 3 cells of USE-803048 class (8 mm) after confirming its width.

---

## 2. EMPHASIS beside CUTOFF, with its wires through the hinge ribbon

### 2.1 What the circuit really is
From `ref/ca-72/circuits/boards/board4-vcf.lib`, the golden model the harness uses:
- **`emo`:** C10 (10 µF) out of node `nu`. That's R3 1 k from the output, with R7 180 Ω to a C9 100 µF-bypassed node, so a source impedance of **≈ 150 Ω**, AC-coupled (no DC through the pot).
- **`emi`:** R73 (1 k REGEN CAL trimmer) to `in30`, the input pair's second base. That node returns via R76 330 Ω to `b5`, which is bypassed by C24 220 µF. So **≈ 0.5–1.3 kΩ to AC ground**.
- **EMPHASIS = `rr14`, a two-terminal rheostat between `emo` and `emi`** (50 k reverse audio). Only **2 conductors** cross, not 3.
- **The series resistance at the ladder already exists** (R73 + R76) and stays on the lid board. There is no high-impedance node to carry across.
- Self-oscillation onset is at R14 ≈ **0.8–1.4 kΩ** (golden `metrics.json`: 100 Hz → 780 Ω, 2 kHz → 1,383 Ω). Near the top of the dial both ends are low-Z.

This replaces the "high-impedance base node" premise in `round4-answers.md` §2.1/§2.2. The ribbon guard and bench-test advice still stands.

### 2.2 Line length, capacitance, HF and self-oscillation [SIM]

**Adapters:**
- `eng/sim/fold/fold_emph_worst.inc`: 100+ mm, **20 pF per conductor to ground, 5 pF emo–emi mutual, 150 nH loop**.
- `fold_emph_guarded.inc`: 10 pF, 0.5 pF, 100 nH.

Both are golden CA-72 with the rheostat moved to the far end of the cable model.

**Run:**
```
cd eng/sim/reference
python3 run_all.py --adapter ../fold/fold_emph_worst.inc --tag fold_emph_worst --only filter --no-cal
python3 compare.py out/golden out/fold_emph_worst | grep vcf
```
**Result: 46/46 filter checks PASS** for worst case and guarded alike.
- fc Δ 0 cents at every cutoff;
- slopes Δ ≤ 0.003 dB/oct;
- |H| max Δ **0.14 dB** (cut +9 V, emphasis 7; limit 0.5), ≤ 0.06 dB elsewhere;
- **self-oscillation onset dial Δ 0.0** at 100 Hz / 200 Hz / 2 kHz;
- lowest self-osc frequency Δ 0.01 %.

**Why:**
- 20 pF against ≤ 1.3 kΩ puts a pole at ≈ 6 MHz.
- 5 pF across the 50 k rheostat at dial 0 is 1.6 MΩ at 20 kHz, ≈ 3 % of the R14 path.
- So the extra 60–100 mm of line is irrelevant to the filter's response, HF and onset.

### 2.3 Pickup [SIM]

**`eng/sim/fold/pickup.py`:**
- Aggressor: a 3.3 V, 4 kHz square (mux select class).
- It couples through Cc into the base-side end of a line. No audio in.
- Measured: the 4 kHz level at the filter output, relative to the output for a **1 V-peak 400 Hz tone through one 33 k mixer channel** (712 mV peak out). That reference level is a stand-in for a real oscillator level (UNVERIFIED for our mixer).

| Victim (where Cc lands) | Cc | Dial 0, cut +6 | Dial 7, cut +6 | Dial 7, cut +3.8 |
|---|---|---|---|---|
| `emi` (to the input pair), unguarded neighbour | 4 pF | **−38 dB** (audible) | −48 dB | — |
| `emi`, one ground guard each side (ESTIMATE 10× less C) | 0.4 pF | −58 dB | −68 dB | −67 dB |
| `emi` | 0.1 pF | −70 dB | — | — |
| `emi` | 0.05 pF | **−76 dB** | — | — |
| `emo` (from the buffer) | 4 pF / 0.4 pF | — | −68 / −88 dB | −87 dB (0.4 pF) |
| Mixer bus `ain` (relevant to §3) | 0.4 pF | −66 dB | −71 dB | −70 dB |

**Reading it:**
- `emi` is the sensitive wire. `emo` is ≈ 20 dB less sensitive.
- The mixer bus is ≈ 8 dB *less* sensitive than `emi` in this model. That reverses round 4's ranking. Caveat: the bench models the mixer as 33 k into a 5.5 k load.
- **Target ≤ −70 dB** (ESTIMATE threshold for "not heard under a note"), so **≤ 0.1 pF from any select line to `emi`**. One adjacent guard isn't enough. Distance is what gets there.
- The VCA after the filter gates the tone between notes. It's heard only under a held note or a drone.
- Osc 3 on MOD MIX (±5 V) is ≈ +3.6 dB worse per pF than a 3.3 V select [CALC]. It's harmonically related to the notes, so it's less objectionable, but keep it away too.
- Magnetic pickup at these impedances is negligible [ENG].

### 2.4 Cable options
| Option | Pickup to `emi` (ESTIMATE) | Flex life | Cost | Note |
|---|---|---|---|---|
| **40-way ribbon, EMPHASIS at the far edge:** `GND, emi, GND, emo, GND, VOLUME…`, ≥ 20 conductors (≥ 25 mm) and ≥ 3 grounds from S0–S3 | ≤ 0.05 pF → ≤ −76 dB | Same as the ribbon (≥ 2,000-fold test, `round4-answers.md` §2.2) | ≈ +$0.50 over the 34-way (ESTIMATE) | **Default.** One cable crosses |
| Separate 5-way 1.27 mm ribbon (`GND emi GND emo GND`) through the other end of the hinge | ≈ 0 (≥ 100 mm from the selects) | Same | +1 IDC pair ≈ $1–2 (ESTIMATE) | Breaks "one cable crosses" (design principle 5): design team's call |
| Shielded 2-conductor micro cable | ≈ 0 | **Worse:** foil shields crack in a flexing hinge, braid is better. Part not sourced (UNVERIFIED) | ≈ $1–3 (ESTIMATE) | Not recommended for a fold joint |

**Conductor count with EMPHASIS crossing:**
- 33 (round 4, EMPHASIS in the lid)
- \+ emo, emi
- \+ 2 extra guards
- = **37 → 40-way** (2 × 20, 50.8 mm wide). Round 4's "38" assumed 3 wires.

### 2.5 Conditions for "yes"
1. The pot is a **two-terminal rheostat** in the base. Strap its spare lug to the wiper there. C10, R73 and R76 stay on the lid board at the ladder.
2. `emi` is the outermost signal conductor at the ribbon edge farthest from S0–S3 and osc 3, with ground on both sides. `emo` comes next.
3. Base-board traces for `emo`/`emi`: from the header straight to the pot, ≤ 40 mm, guarded by ground pour. Not routed near the CD4067 select traces (ESTIMATE ≥ 10 mm away).
4. A 40-way ribbon and headers on both boards.
5. Bench test (§2.6) passes before the board order.

### 2.6 Verification
- **SPICE (done):** the two adapters + `pickup.py` above.
- **When the KiCad netlist exists:**
  - Rerun with our own `dut_vcf` adapter.
  - Use the cable C measured on a 100 mm sample of the actual ribbon: LCR meter, `emi` to S3 at the planned spacing, and `emi` to GND.
  - Feed the measured C into `pickup.py` as Cc.
- **Bench (round 4 §2.2, pass level now set):**
  - Setup: 100 mm of the real ribbon in the planned order, with the real scan running. EMPHASIS at 7 and at max; cutoff swept 1–8 kHz; one oscillator through its mixer channel at the normal level.
  - **Pass:** the scan tone at the phones output is ≥ 70 dB below the note. Spectrum analyser on the phones output; a phone app at the line out is enough to see −70 dB.
- **Fail path:** use the separate 5-way cable, or move EMPHASIS back to the lid (owner decision, as the director said).

---

## 3. Alternative: the ladder filter in the base

The base then has CUTOFF, EMPHASIS, CONTOUR AMT, KBD CTRL and the ladder. The lid keeps the oscillators, mixer, contours, VCA and output.

**What crosses** (compared with EMPHASIS crossing alone):

| Leaves the ribbon | Joins the ribbon |
|---|---|
| EMPHASIS (2) + its 2 guards | **Mixer bus → ladder input** (1, at the far guarded edge; −66 dB at 0.4 pF [SIM], same treatment as `emi`) |
| CONTOUR AMT (3) | Filter out → VCA (1; ≈ 1 V, ≈ 1 k source, low risk) |
| KBD CTRL (3) | Filter contour CV (1), CUTOFF+velocity CV from the DAC (1), keytrack CV (1) |
| FILTER MOD return (1) | **±9 V + analog GND** (3; the ladder bias draws ≈ 5–10 mA, ESTIMATE) + 2 guards |

**Net:** ≈ −11 + 10. **Still ≈ 36–38 conductors, so 40-way.** No ribbon saving.

**Gains:**
- CUTOFF, EMPHASIS and the ladder all sit on one board. No emphasis wire crosses.
- **The lid board needs ≈ 2,000 mm² less.**
  - Ladder courtyard ESTIMATE: ≈ 16 TO-92, ≈ 25 resistors, 3 trimmers, 6 film caps, 4 lying electrolytics, ≈ 1,300–1,600 mm² of courtyard at 70 % fill.
  - That's what makes ≈ 87 mm reachable (power bank only), §1.3.

**Costs and constraints:**
- **Base PLAY strip fill:** 46 % → **≈ 66–70 %**. Spare at 70 % ≈ 1,800 mm² of courtyard against ≈ 1,300–1,600 needed. **Tight.** A recount is needed before committing.
- **Heights:** 7 mm under the base plate.
  - 220 µF (C24), 100 µF (C9) and 10 µF electrolytics must lie flat.
  - .068 µF film caps must be ≤ 6.5 mm tall. WIMA MKS2-class is ≈ 6.5 mm, UNVERIFIED for the part chosen.
  - **Nothing on the underside** (1 mm of air).
- **Neighbours on the base board:**
  - The CD4067 selects and the Hall sensors: keep the ladder ≥ 30 mm from select traces.
  - The LD1117 dissipates ≈ 0.3–0.4 W [CALC: (5 − 3.3) V × 0.15–0.25 A]: keep the ladder's **expo pair ≥ 30 mm away** and away from its heat path.
  - The analog ground returns to the lid's star point on its own conductor.
- **Mixer bus crossing:** it's ≈ 100–150 mV at a few kΩ. Treat it exactly like `emi` (§2.5 item 2).
- **The speaker rule (≥ 55 mm)** is met automatically: the speaker is in the lid.

**Verdict:**
- **EMPHASIS alone crossing (§2)** is the smaller change for the director's ruling 2.
- **Ladder to the base** is worth it only if the design team needs the lid board area (§1.3), i.e. to approach ≈ 87–90 mm with a power bank, or ≈ 101–105 with the slim pack.

---

## 4. Spec changes (`budget-variant.md` rev 12)

| Where | Change | Δ cost |
|---|---|---|
| §v1.6 (FOLD only) | Band pack option: **4 × PiShop 952540 (9.5 × 25 × 40, 750 mAh, PCM) 1S4P, 11.1 Wh, ≈ 4.5 h / 2.4 h**, star harness + 2 A fuse, XH→PH adapter. Flat concepts keep the 2 × 50 × 60 pack | FOLD: $40.75 vs $40.85 (+≈ $0.50–1.70 for fuse and PTCs) |
| §v1.8 Risks | FOLD depth is set by lid board area plus battery footprint, D ≥ 6 + (23,300 + A)/262; ≤ 90 needs no internal cell and the ladder in the base | — |
| §v1.8 Risks | FOLD EMPHASIS crossing: 2-wire rheostat, `emi` at the far ribbon edge, ≤ 0.1 pF to the selects, 40-way. Bench pass ≤ −70 dB | +≈ $0.50 (40-way) |
| §v1.8 Risks | FOLD rev 4.2's lid board recount (20,260 vs 22,500 mm²) | — |

## Sources
- PiShop 952540 750 mAh: https://www.pishop.us/product/lithium-ion-polymer-battery-3-7v-750mah/
- PiShop 900 mAh (SKU 440): https://www.pishop.us/product/lithium-ion-polymer-battery-3-7v-900mah/
- US Electronics USE-803048 (DigiKey): https://www.digikey.com.br/en/products/detail/us-electronics-inc/USE-803048-1100-mAh/17799390
- TinyCircuits 1000 mAh: https://tinycircuits.com/products/lithium-ion-polymer-battery-3-7v-1000mah
- Jauch LiPo list (DigiKey): https://www.digikey.co.uk/en/product-highlight/j/jauch-quartz/lithium-polymer-batteries
- Adafruit #6106 bq25185: https://www.adafruit.com/product/6106
- CA-72 VCF netlist (local, read-only): `ref/ca-72/circuits/boards/board4-vcf.lib`
- Sim files: `eng/sim/fold/fold_emph_worst.inc`, `fold_emph_guarded.inc`, `pickup.py`; results `eng/sim/reference/out/fold_emph_{worst,guarded}/metrics.json`
