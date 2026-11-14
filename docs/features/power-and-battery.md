# Power and battery
Status: per item below · last updated 2026-11-13 · sources: [owner.md](../../design/owner.md), [eng/battery.md](../../eng/battery.md), [eng/budget-variant.md](../../eng/budget-variant.md) (rev 12 power table, FOLD band cells), [eng/daisy-first-principles.md](../../eng/daisy-first-principles.md) §1.5, §7, [eng/architecture.md](../../eng/architecture.md) §4, [eng/answers-E1-E10.md](../../eng/answers-E1-E10.md) (E5 lid switch), [cathedral §16.2](../../design/branches/concepts/cathedral/how-it-works.md)

## What it does (player's view)
- **It runs on its own battery**, inside the base, for roughly **2–4 hours** of playing as specified today, longer with the two power savings below. Plug a USB-C charger into the back to charge it, and you can keep playing while it charges.
- **Hold TAP for 1.5 s** and the **status** light shows how full the battery is. It also flashes once after "ready" at power-on.
- When the battery runs low, the status light warns you. Near empty, the effects fade out first, so the synth keeps sounding for the last minutes.
- **Close the lid** and it goes to sleep (proposed).

## Owner decisions (verbatim, linked to owner.md)
- "What do you mean there's no battery thing enough we are designing this" → recorded as: **an internal battery is expected; the enclosure is designed around one** ("completely portable").
- "Show me both" (big 22 Wh pack with taller halves, or the slim 11 Wh pack with 105 mm halves): no choice yet. CATHEDRAL carries the **slim pack**.
- Base spec: "Power: USB power bank or internal LiPo (open; ~+$21 for internal)", since superseded by the line above.

## How it works
```
USB-C (rear) ─► VBUS ─► bq25185 charger + 5 V boost (Adafruit #6106; load-sharing) ◄─► 4 × 750 mAh pouch cells, 1S4P (11.1 Wh)
                          │ 5 V
                          ├─► ±rails for the analog voice (boost / inverter + LDOs, eng)
                          ├─► Daisy Seed (3.3 V) ─► DACs, muxes, MIDI, LEDs
                          ├─► Hall key sensors (own 3.3 V regulator; group-gated, proposed)
                          └─► LM386 speaker amp (enabled by the Daisy; muted when phones are in)
cell voltage ─► divider ─► mux D ─► Daisy (gauge, warnings)
```
- **Cells:** **4 × PiShop 952540** (9.5 × 25 × 40 mm, 750 mAh, with protection, $7.95 each, listed in stock), wired **1S4P**: **11.1 Wh**. A star harness with a 2 A fuse, and an optional ≈ 1 A PTC per cell lead (budget-variant rev 12).
- **Where (CATHEDRAL):** the **base's rear strip** (y ≈ 80–106, x ≈ 15–185, under-plate height 11.1 ≥ 9.5), beside the Daisy. The lid's plate no longer has room after steer 2 (cathedral §16.2). The base gets heavier and the lid lighter, so the standing tip threshold rises from ≈ 6.9 N to **≈ 8.4 N** [CALC].
- **Charger:** the bq25185 board charges at 1 A by default and feeds the load first, then the cells. One rear USB-C does both power and the Daisy's USB data (DFP §0, row 5).
- **Boost headroom (must-fix):** the Daisy-era load reaches ≈ 4.4 W, ≈ 0.88 A at 5 V, against the board's 1 A boost. **Fix: a ≥ 2 A 5 V boost module, ≈ +$6–12** (ESTIMATE; budget-variant).
- **Gauge:** the cell voltage goes through a 100 k / 100 k divider onto mux D (moved off D20 for the 4th mux), oversampled. The firmware corrects for its own load (DFP §7.3). Optional: charger STAT and VBUS-present for "charging / charged / on USB".
- **Sequencing:** the sensor regulator is enabled last, and the boost starts soft, because the boost stalls above ≈ 200 mA at a hard start (battery.md). The LM386 has its own enable.

## Controls and states
| State | What you see | Behaviour |
|---|---|---|
| Normal | status light off after "ready" | — |
| Battery query (hold TAP ≥ 1.5 s while playing) | status light shows the level | that press isn't a tempo tap ([firmware and gestures](firmware-update-and-gestures.md)) |
| Low (≈ 3.5 V per cell) | status light warns | plays on |
| Near empty (≈ 3.3 V) | status light flashes | effects fade out over 2 s, then the voice runs to the boost's cutoff ([effects](effects.md)) |
| Charging, instrument on | (STAT, if fitted) | charging is slow or stalls while you play, unless the supply gives ≥ 2 A |
| Lid closed | — | sleep (proposed, E5 lid Hall switch) |

## Budget: the power table, with the speaker counted (architecture open item 8)
**Load at 5 V (Daisy era, budget-variant):**
- **≈ 2.4–4.4 W** without the speaker. The biggest single item is the 25 Hall sensors at 0.6–1.25 W.
- **The speaker** (LM386, cathedral's Ø 50 driver): ≈ **0.5–0.8 W more when played loud** (architecture, UNVERIFIED); ≈ 0.02 W idle (ESTIMATE). Phones and line out add only a few mA.

**Runtime on the 11.1 Wh pack** (10.0 Wh usable; boost 90 % at the low end, 85 % at the high end; same method as battery.md) [CALC, ESTIMATE inputs]:

| Case | Low end | High end |
|---|---|---|
| As specified, no speaker (budget-variant) | **≈ 3.7 h** (2.4 W) | **≈ 1.9 h** (4.4 W) |
| As specified, speaker loud (+0.65 W) | ≈ 2.9 h | ≈ 1.7 h |
| With both savings below (≈ −0.65 to −1.35 W), no speaker | ≈ 5.1–8.6 h | ≈ 2.3–2.8 h |
| With both savings, speaker loud | ≈ 3.8–5.3 h | ≈ 1.9–2.3 h |

**The two savings (proposed, bench-gated):**
1. **Hall group power-gating:** only the key group being scanned is powered. **−0.45 to −0.95 W.** It needs the SS49E's power-on time measured (≤ 50 µs to adopt) (DFP §1.5). ≈ +$0.70.
2. **A 3.3 V buck for the Hall rail** in place of the LD1117: **−0.2 to −0.4 W** (budget-variant).

**Also:** the Daisy runs at 400 MHz with WFI between audio blocks, 48 kHz, and dims its LEDs after a few minutes idle (DFP §7.2).

**Cost:** cells $31.80 + the charger board $8.95 = **$40.75** (budget-variant); + a ≥ 2 A boost ≈ $6–12; + fuse / PTCs ≈ $1–3.

## Edge cases
- **Playing from a weak USB port:** the load (≈ 0.5–0.9 A at 5 V) can exceed what the port gives, so the battery drains slowly even when plugged in. Use a USB-C charger.
- **Charging inside the closed case:** the cells have no thermistor. Don't charge unattended in a closed bag (battery.md safety note 5).
- **One cell's protection trips:** the other three carry the load (≈ 0.6 A each at the end of discharge, ≈ 0.6 C). Fine, but replace the pack (budget-variant).
- **Cold start on a nearly empty pack:** the soft-started boost and the late sensor enable stop a boot loop (battery.md).
- **Speaker at full in the park:** the shortest runtime case above. Phones save ≈ 0.5–0.8 W.

## Interactions with other features
- **Firmware and gestures:** the battery query (hold TAP) and the power-on level flash ([firmware and gestures](firmware-update-and-gestures.md)).
- **Effects:** the low-battery 2 s fade of the wet return ([effects](effects.md)).
- **Keys:** Hall gating changes the scan timing (6.8 kHz per key, still above the 4 kHz target) ([keys and velocity](keys-and-velocity.md)).
- **Enclosure:** the cells set the base's rear strip and the stand's tip force ([enclosure](enclosure.md)).
- **I/O:** phones-in mutes the speaker, which is also the biggest power saving ([io](io.md)).

## MIDI
- None. Power state is never sent over MIDI.

## Open questions
1. **Pack size:** the slim 11.1 Wh pack (≈ 2–4 h as specified; more with the savings), or find room in the base for a bigger pack (the 22 Wh option needs 50 × 60 mm cells, which don't fit the 26 mm rear strip)? The owner said "Show me both"; CATHEDRAL shows the slim one. Eng: is there other room in the base?
2. **Speaker draw:** measure the LM386 with the real driver and box (eng).
3. **Hall gating:** adopt it if the SS49E settles in ≤ 50 µs (bench).
4. **Lid-closed sleep:** confirm the E5 lid Hall switch in CATHEDRAL's hinge (≥ 50 mm from the speaker magnet) (eng).

## Status (decided / proposed / open, item by item)
| Item | Status |
|---|---|
| Internal battery, enclosure designed around it | decided |
| 4 × PiShop 952540, 1S4P, 11.1 Wh, in the base's rear strip (CATHEDRAL) | proposed |
| bq25185 charger board, one rear USB-C, ≥ 2 A boost | proposed (eng) |
| Gauge on mux D, warnings, 2 s FX fade, hold-TAP query | proposed |
| Hall gating, 3.3 V buck for the Hall rail | proposed (bench-gated) |
| Lid-closed sleep | proposed |
| Pack size (11 vs 22 Wh) | open (owner: "Show me both") |
| Speaker draw | open (measure) |
