# Little D internal battery: two 50 x 60 mm pouch cells, 1S2P (rev 11, 2026-11-12)

Inputs: `budget-variant.md` rev 10 (v1.6, v1.2), `round4-answers.md` §3 (load 2.0-3.6 W at 5 V, bq25185 boost 85-90 %, stalls above ~200 mA at a hard start). Prices and specs read from the vendor pages 2026-11-12, qty 1. **ESTIMATE** = my number, not checked. **UNVERIFIED** = not confirmed on a page.

## Cells (bay: two cells, each <= 50 x 60 x 9.5 mm)

| | Part | Size (mm) | Capacity | Price | Protection | Source |
|---|---|---|---|---|---|---|
| **A (22 Wh target)** | PiShop "Li-polymer 755060 3000 mAh 3.7 V", JST-PH, 24 AWG, 100 mm leads | 7.5 x 50 x 60 | 3000 mAh, 11.1 Wh | **$15.95** ea | Yes (PCM: overcharge, over-discharge cutoff 3.0 V, short) | [PiShop](https://www.pishop.us/product/lithium-ion-polymer-battery-3-7v-3000mah/). **Stock not shown on the page**; not on Adafruit/SparkFun/DigiKey/Mouser |
| **B (in stock)** | Adafruit #328 "Li-Po 3.7 V 2500 mAh", JST-PH | 7.3 x 50 x 60, 50 g | 2500 mAh, ~10 Wh (9.25 Wh at 3.7 V) | **$14.95** ea ($13.46 at 10) | Yes (overcharge, cutoff ~2.8 V, short). **No thermistor** | [Adafruit](https://www.adafruit.com/products/328), in stock |

Searched SparkFun, DigiKey, Mouser: no 50 x 60 pouch with PCM found (SparkFun's pouch cells are retired; search was not exhaustive). Adafruit #2011 (60 x 36 x 7, 2000 mAh) is the current cell and does not fill the bay.

Packs: **A x2 = 6000 mAh, 22.2 Wh, $31.90.** B x2 = 5000 mAh, 18.5 Wh, $29.90. Add the bq25185 board ([Adafruit #6106](https://www.adafruit.com/product/6106), $8.95, in stock): **$40.85 (A) / $38.85 (B)**, versus $21.45 now. Cells are 7.3-7.5 mm nominal, so 9.5 mm leaves ~2 mm for tolerance and swelling.

## Recommendation: parallel (1S2P)

- The bq25185 board is a single-cell charger and 5 V boost. 1S2P connects with a JST-PH Y-harness and nothing else changes. Series (2S, 7.4 V) would need a 2S charger with balancing and a different converter, and each cell's PCM only protects its own cell, so one trip drops the whole string with no balancing.
- Parallel cells self-balance, so no balance lead is needed.
- 1S2P doubles capacity at the same voltage. Cell current is halved, which makes the 1.2-1.4 A cell-side peak trivial (~0.2 C per pack).

## Safety notes

1. **Same part, same lot, same age** for both cells.
2. **Match voltage before joining:** measure each cell; within 0.05 V (ideally 0.02 V) or charge the lower one alone first. A big difference means an inrush current between cells.
3. **Check JST polarity with a meter on both cells** before the harness. Vendors swap red/black on PH leads. PiShop polarity is UNVERIFIED.
4. Each cell keeps its own PCM. If one PCM trips, the other carries the full load (1.4 A peak at 3.0 V, ESTIMATE), so do not rely on it. PCM current ratings are not stated on either page (UNVERIFIED).
5. **No thermistor** on the cells (Adafruit says so for #328) and none mentioned for the charger. Adafruit prefers <= 500 mA, max 1200 mA, per cell. 1 A split over two cells is ~0.5 A each, so the default is acceptable. Don't charge unattended inside a closed case.
6. Mount the cells flat, free to expand, with no component leads or screw tips on them (keep-out as in rev 9), and no compression. Retire any puffy cell.
7. Optional: ~2 A inline PTC or fuse in the harness (ESTIMATE, +$0.50).
8. Store at ~3.8 V if the unit sits for months.

## Charging with the existing charger

bq25185 default is 1 A; cutting the back jumper sets 500 mA ([Adafruit #6106](https://www.adafruit.com/product/6106)). Charge time = capacity / current x ~1.1 for the taper (ESTIMATE), powered off:

| Pack | 1 A (default) | 0.5 A (jumper cut) |
|---|---|---|
| A, 6000 mAh | **~6.5-7 h** | ~13 h |
| B, 5000 mAh | ~5.5-6 h | ~11 h |

The charger is load-sharing: the load is fed first and the remainder charges the cells. At 0.4-0.7 A of load from a USB source with an input limit near 1 A, charge current is cut and charging can take 2-3x longer, or stall at 0.7 A (the input limit isn't stated: UNVERIFIED). Charge with the instrument off, or use a >= 2 A supply.

## Runtime (ESTIMATE)

Cell power = load / boost efficiency (90 % at 2.0 W, 85 % at 3.6 W, per `round4-answers.md`): **2.0 W -> 2.22 W; 3.6 W -> 4.24 W.** Usable energy = 90 % of nominal (cutoff, rate, aging).

| Pack | Nominal | Usable (90 %) | 2.0 W load | 3.6 W load |
|---|---|---|---|---|
| A: 2 x 3000 mAh | 22.2 Wh | 20.0 Wh | **~9.0 h** (10.0 h nominal) | **~4.7 h** (5.2 h nominal) |
| B: 2 x 2500 mAh | 18.5 Wh | 16.6 Wh | ~7.5 h (8.3 h) | ~3.9 h (4.4 h) |
| Old: 1 x #2011 2000 mAh | 7.4 Wh | 6.7 Wh | ~3.0 h | ~1.6 h |

Cell current at the end of discharge (3.0 V, 3.6 W load): ~1.4 A for the pack, ~0.7 A per cell. Boost output (0.72 A at 5 V) is inside the 1 A rating; the stall rule (sensor LDO last, MC34063 soft-start) still applies.

## Cost and open items

- **Cells + charger: $40.85 (A) or $38.85 (B)** instead of $21.45. Cells from PiShop, charger from Adafruit means two orders (two shipping charges, ESTIMATE $5-8 each). Use B if the A stock cannot be confirmed.
- Open: PiShop 755060 stock and true thickness (measure one); cell polarity; JST-PH Y-harness source; bay height given the cells' real tolerance; USB input current limit of the bq25185 board.
