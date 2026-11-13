# Eng answers to the key rethink (E-K1 to E-K6), Little D first

Status: rev 1, 2026-11-12. Answers `archive/full-instrument/concepts/keys/first-principles.md` §6.
Conventions are the same as `budget-variant.md`: a link means the price or spec was read this session (2026-11-12).
**ESTIMATE** means my number, not checked. **UNVERIFIED** means a source exists but I couldn't confirm the figure.
**[CALC]** means my arithmetic (scripts: on-axis disc-magnet formula, current-loop off-axis model and a
Monte-Carlo velocity sim, reproducible from the numbers below).

## 0. Bottom line

- **RAIL fits Little D, but not as drawn.** The drawn stack (18–20 mm above strip C) plus a corrected
  magnet gap lands at ≈ 29–31 mm with the lip, which is no margin in a 30 mm box. **A slimmed RAIL stack is
  ≈ 22 mm to the white key surface and ≈ 26 mm to the top of the lip**, leaving ≈ 4 mm spare (§1).
- **Correction to §v1.4b (it affects every Hall option, SWITCH included):**
  1. **A 5 × 2 mm magnet is too strong for the planned gaps.** At 3.3 V the SS49E stays linear only to
     ≈ 650–760 G. The planned 0.7 mm bottom gap gives ≈ 2,100 G, so about two thirds of the stroke would
     sit flat in saturation. **Use a bottom gap of ≈ 2.8 mm and a rest gap of ≈ 5.6 mm (N35)** (§2).
  2. **The SS49E has to lie flat, face up**, with its leads bent 90°. It senses the field perpendicular to
     its branded face, so standing upright under an axial magnet it would see mostly the wrong component.
- **Scan rate:** ≈ 8–10 kHz per key is possible, and I design to **≥ 4 kHz**. **Velocity method:** a
  least-squares slope fit on linearised position. That gives **< 1 MIDI velocity step RMS at both 5 mm and
  2.8 mm**, so travel is a feel argument more than a resolution one (§3).
- **Partial-release re-trigger works** with single trigger and low-note priority, and it is the original
  Minimoog behaviour. It needs a firmware minimum gate-low time of ≈ 2 ms (§4).
- **Prices:** the lean RAIL is **≈ $52–58 with bought acrylic, or ≈ $35–46 on makerspace scrap**, against
  SWITCH's $50–55. The v1.10 totals don't change (§5).
- **RAIL-M crosstalk is negligible** (≈ 0.01 G of change). The main magnets' neighbour crosstalk is ≈ 3 % of
  swing at the 10.5 mm grid and ≈ 0.4 % at 18.7 mm, both well inside the hysteresis band (§6).
- **New flags:**
  - Sensor current is 25 × 6–10 mA, which is 0.5–0.8 W and close to the Pico's 300 mA 3V3 limit. Give the
    sensors their own regulator (§3).
  - The RAIL rod needs intermediate supports (§1).
  - Velocity has **no CV destination** in the v1.2 spec (§4).

---

## 1. E-K2: does an 18–20 mm RAIL stack fit Little D?

**The ≤ 8 mm under-key limit no longer applies.** It came from the rev 2 single-board layout. v1.10 uses a
main board of 280 × 100 mm at the back and a separate key strip, so **nothing but strip C sits under the
keys**. The key zone is its own stack, which is exactly the "keys area separate from the board stack" option.

**Stack at the magnet line, measured from the outside of the bottom panel (whites)**

| Layer | As drawn (first-principles §3B) | **Proposed Little D stack** | Note |
|---|---|---|---|
| Bottom panel | 3.0 | 3.0 | 3 mm ply or acrylic |
| Lead-tail clearance under strip C | 1.5 | 1.5 | nylon spacers |
| Strip C | 1.6 | 1.6 | single-row 280 × 15 |
| Sensor | ≈ 6 (standing) | **2.0** (laid flat on bent leads) | it must lie flat anyway (§0) |
| Magnet-to-sensor gap at rest | ≈ 2.5 | **5.6** | set by saturation (§2) |
| Blade height above the key underside | 7 | **5** | the magnet is pocketed in the blade's underside |
| Top | 3 | 3 | |
| **White key surface** | ≈ 24.6 (with the §2 gap) | **≈ 21.7** | |
| Sharps | +5 riser | **+3 riser** (visible part only) → 24.7 | |
| Lip (1.5 felt + 3 lip over the key rears at white height) | ≈ 29–31 | **≈ 26.2** | |

**Verdict: it fits.** The keys top out at ≈ 22–25 mm and the lip at ≈ 26 mm, inside a 30 mm box with
≈ 4 mm to spare. Alternatively the key zone can be a **lower step (≈ 26 mm) in front of a 30 mm control
zone**, which is a natural wedge for the enclosure designers. [CALC]

**Thinner still (−3.5 mm, optional):**
- Seat the SS49E in a slot in strip C, face flush (−2.0 mm). This is the route (a) trick.
- Bond strip C into a window or pocket in the bottom panel with its lead tails trimmed (−1.5 mm).
- That gives ≈ 18.2 mm to the white surface and ≈ 22.7 mm to the lip.
- **The magnetic gap, not the sensor body, sets the height.** The sensor body just occupies part of the gap.

**Checks on the slimmer geometry [CALC]**
- **Blade height of 5 mm is enough.** An inverted U (top 3 × 10.5, blades 2 × 3 × 5) has I ≈ 330 mm⁴. A 20 N
  hard strike at the front (lever arm 27 mm past the tube) gives ≈ 7 MPa, against ≈ 70 MPa for acrylic
  (≈ 35 MPa at a solvent weld, ESTIMATE). Margin ≈ 5×.
- **Move the magnet from 30 mm to ≈ 40 mm from the rod.**
  - The tube sets the angle: 3.2 mm of solid travel at 45 mm, for every key. At 30 mm the magnet swings
    only 2.1 mm, which is 13 % less signal than at 40 mm (2.85 mm, the same as a Choc).
  - A Ø5 magnet centred at 40 mm (37.5–42.5) would overlap the tube pocket (41.8–48.2), so **centre it at
    ≈ 38.5 mm**, which gives a 2.7 mm swing (rest gap ≈ 5.5 mm). That still sits behind the sharps' front
    (52 mm), so there is still one straight sensor line on the 10.5 mm grid.
- **The rod needs intermediate supports.**
  - Each pressed key pushes up on the rod with ≈ 0.6 × its finger force (moments about the rod with the
    tube at 45 mm and the finger at 72 mm).
  - A 3/32" music-wire rod over the full 290 mm, simply supported, deflects ≈ 19 mm under a 12 N hard-strike
    reaction and ≈ 0.6 mm under normal play.
  - **Add a laser-cut support comb every 3–4 keys (≈ 40 mm spans): deflection drops to ≈ 0.06 mm.** Hanging
    the supports from the lip keeps them off the bottom.
- **Depth:** the RAIL key zone is 72–75 mm, the main board is 100 mm, and the walls add ≈ 6 mm. That is
  **≈ 178–181 mm, against v1.2's 170 mm.**
  - Fix 1: grow the box to ≈ 180 mm deep.
  - Fix 2: let the lip zone (the rear 20 mm of the keys, plus the rod) overhang the main board's front edge,
    with only low parts (≤ 6 mm) in that 20 mm band. The rod supports then hang from the lip.

## 2. E-K3: SS49E saturation against magnet gap

**Sensor facts** ([Honeywell SS49E datasheet](https://atom.ubbcluj.ro/alpar/datasheets/sensors_actuators/Honeywell%20SS49E.pdf), Vs = 5 V):

| Spec | Value |
|---|---|
| Supply | 3.0–6.5 V (other datasheet revisions say 2.7 V) |
| Supply current | 6 mA typ, 10 mA max |
| Sensitivity | 1.0 / 1.4 / 1.75 mV/G (min / typ / max) |
| Linear range | ±650 G min, ±1000 G typ |
| Output span | typ 0.95 V to Vs − 0.95 V (min 1.05 V to Vs − 1.05 V) |
| Response time | 3 µs |

**At 3.3 V (UNVERIFIED: the datasheet is specified at 5 V; I assume ratiometric sensitivity and fixed
headroom):**
- sensitivity ≈ 0.92 mV/G;
- headroom above null ≈ 0.60–0.70 V;
- so the output **saturates at ≈ 650 G (min) to 760 G (typ).**
- **Design rule: ≤ 650 G at the bottom of travel**, on the side of null that the magnet polarity drives.

**Field on axis, 5 × 2 mm disc** [CALC]:
- Model: the exact on-axis formula, with N35 Br = 1.19 T and N52 Br = 1.45 T.
- The Hall element is assumed to sit 0.5 mm below the branded face. That is UNVERIFIED for the SS49E; it's
  typical of TO-92S Hall packages. Read the drawing and add the difference to every gap below.

| Face gap (mm) | 0.75 | 1.0 | 1.5 | 2.0 | 2.5 | **2.8** | 3.0 | 3.5 | 4.0 | 5.0 | **5.6** | 6.0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N35 (G) | 2055 | 1780 | 1329 | 994 | 751 | **≈ 650** | 575 | 447 | 352 | 228 | **≈ 180** | 155 |
| N52 (G) | 2504 | 2169 | 1619 | 1211 | 915 | ≈ 780 | 701 | 544 | 429 | 278 | ≈ 215 | 189 |

**Recommended gaps** (2.7–2.85 mm of magnet travel: Choc, or RAIL with the magnet at ≈ 38.5 mm)

| Magnet | Bottom gap (650 G) | Rest gap | Swing | ADC counts at 3.3 V |
|---|---|---|---|---|
| **N35 (recommended)** | **2.8 mm** | **5.6 mm** (≈ 180 G) | ≈ 470 G | **≈ 530** |
| N52 | 3.15 mm | 6.0 mm (≈ 190 G) | ≈ 460 G | ≈ 520 |
| N35, RAIL magnet at 30 mm (2.1 mm swing) | 2.8 mm | 4.9 mm (≈ 240 G) | ≈ 410 G | ≈ 465 |

- **N52 buys nothing.** The swing is capped by saturation, not by magnet strength, so N52 only needs bigger
  gaps (a thicker stack). **Use N35, the cheapest grade.**
- A slightly smaller magnet is equally fine: [K&J D31](https://www.kjmagnetics.com/proddetail.asp?prod=D31)
  is 4.76 × 1.59 mm N42 at $0.19 each, US. Re-derive the gaps for it (≈ 0.2–0.3 mm smaller, ESTIMATE).
- **Tolerance:** the SS49E min/max sensitivity spread is ±25 %, and the firmware learns each key's rest and
  bottom. If a sensor is "hot" and clips the last ≈ 0.3 mm, the note-on and velocity thresholds (≤ 70 % of
  travel) still sit in the linear part. **Set the bottom gap 2.8–3.0 mm, never under 2.5 mm.**
- **Option: SS49E at 5 V with a 2:3 output divider.** It gets the full ±1000 G typ range (bottom gap
  ≈ 2.0 mm, ≈ 860 counts), but it costs 25 × 6 mA at 5 V = 0.75 W. Not recommended for battery play.
- **The §v1.4b Choc plan (gap 3.5 → 0.7 mm) needs this change too.** As written, everything below ≈ 2.5 mm
  of gap (≈ 1.8 mm of the 2.8 mm stroke) would read flat.

## 3. E-K1: scan rate and velocity

**Hardware:**
- Pico 2: 12-bit ADC ([Tom's Hardware spec table](https://www.tomshardware.com/raspberry-pi/raspberry-pi-pico/whats-inside-the-raspberry-pi-pico-2s-rp2350)).
  The conversion time of ≈ 2 µs (500 ksps) is the RP2040-family figure, not re-read for the RP2350
  (UNVERIFIED).
- The Pico 2 brings out ADC0–2 on GPIO26–28. ADC3 reads VSYS/3
  ([Pico 2 datasheet](https://pip-assets.raspberrypi.com/categories/1005-raspberry-pi-pico-2/documents/RP-008299-DS-3-pico-2-datasheet.pdf)).
- So the **two key muxes go to ADC0 and ADC1** (and the pot mux to ADC2), sharing the 4 select lines.

**Timing per select step** [CALC]:
- settle ≈ 2 µs, then one conversion per mux at 2 µs each;
- the CD4067 at VDD = 3.3 V has an Ron of ≈ 1–2 kΩ (ESTIMATE; the datasheet only gives 470 Ω typ at 5 V);
- τ ≈ 2 kΩ × 50 pF ≈ 0.1 µs, so 12-bit settling takes ≈ 1 µs.

| Scan | Per step | 16 steps | Per-key rate |
|---|---|---|---|
| Key muxes only (2 ADC inputs) | 6 µs | 96 µs | **≈ 10 kHz** |
| Keys + pot mux (3 ADC inputs) | 8 µs | 128 µs | **≈ 7.8 kHz** |
| **Design number** (margin for ISR/DMA overhead) | | | **≥ 4 kHz** |

- Run it as the ADC round-robin plus DMA on core 1, with a timer or PIO stepping the select lines. Read the
  pots on every Nth scan.
- **The muxes must run at 3.3 V.** At VDD = 5 V the CD4067B's select inputs need VIH = 3.5 V, which the Pico
  can't drive.
- A **CD74HC4067** (Ron ≈ 70–100 Ω, 2–6 V) settles faster and is the safer DIP-24 pick (price ESTIMATE
  ≈ $0.8–1).

**Key speeds:** at mezzo forte, piano keys peak at ≈ 0.3–0.5 m/s, and *"even in forte the peak velocity does
seldom exceed 1 m/s"* ([Askenfelt, KTH](https://www.speech.kth.se/music/5_lectures/askenflt/motions.html)).
I take pp ≈ 0.05 m/s and allow 1.5 m/s on light keys (ESTIMATE).

The velocity window runs from 20 % to 70 % of travel:

| Travel at the key front | Window at 1 m/s | Window at 0.05 m/s |
|---|---|---|
| RAIL white, 5.1 mm | 2.55 ms | 51 ms |
| Choc, 2.8 mm | 1.4 ms | 28 ms |

**Velocity resolution** [CALC, Monte Carlo]:
- Assumptions: N35 at the §2 gaps (537 counts of swing, ≈ 225 in the window), ADC plus sensor noise
  3 LSB RMS (ESTIMATE, consistent with ≈ 9 ENOB), and a log velocity map over a 20:1 time range onto 127
  steps.
- The table shows the RMS error in **MIDI velocity steps**. Lower is better; < 1 means full 7-bit resolution.

| Method, scan rate | RAIL at 1.5 / 1.0 / 0.4 / 0.05 m/s | Choc at 1.5 / 1.0 / 0.4 / 0.05 m/s |
|---|---|---|
| Two thresholds, raw sample times, 4 kHz | 2.8 / 1.7 / 1.1 / 0.8 | 5.3 / 3.6 / 1.5 / 0.8 |
| Two thresholds, raw, 8 kHz | 1.7 / 1.3 / 0.9 / 0.9 | 2.8 / 1.7 / 1.1 / 0.8 |
| Two thresholds, **interpolated crossings**, 4 kHz | 0.8 / 0.7 / 0.7 / 0.8 | 0.8 / 0.8 / 0.8 / 0.8 |
| **Least-squares slope over 15–75 % depth, 4 kHz** | **0.7 / 0.6 / 0.4 / 0.1** | **1.0 / 0.7 / 0.5 / 0.2** |

**Recommendation:**
1. **Linearise each sample to depth.** Use a lookup table built from the §2 field curve, scaled to the key's
   learned rest and bottom counts. Without it the 20 %/70 % thresholds aren't at 20 %/70 % of travel.
2. **Velocity = least-squares slope of depth against time** over the samples between ≈ 15 % and 75 %. Keep it
   as running sums: a few multiply-adds per sample.
3. It **beats raw two-threshold timing by 2–5× at fast strikes.** It also **works for partial re-strikes**
   that never return to 20 % (§4), which plain two-threshold timing can't do.
4. **5 mm against 2.8 mm:** with the fit, both give full 7-bit velocity. RAIL is ≈ 1.5× finer at ff. It only
   matters much if the firmware used raw tick counts.

**Power and regulator flag:**
- 25 SS49E at 6 mA typ / 10 mA max = **150–250 mA at 3.3 V (0.5–0.8 W)**.
- The Pico 2 datasheet recommends < 300 mA total on its 3V3 pin
  ([Pico 2 datasheet](https://pip-assets.raspberrypi.com/categories/1005-raspberry-pi-pico-2/documents/RP-008299-DS-3-pico-2-datasheet.pdf) §3.1).
- **So feed strip C from its own 3.3 V LDO** (a TO-220 LD1117V33 class part, ≈ $0.5, ESTIMATE). The firmware
  re-learns rest at wake and can also track it while a key is idle, which absorbs the small ratiometric
  mismatch against ADC_VREF.
- **Check that the 1.0–1.5 W power budget in v1.2 includes this.** If it doesn't, LiPo runtime drops by
  ≈ 25–35 %.
- Power gating doesn't fit continuous velocity scanning.

## 4. E-K4: partial-release re-trigger with single trigger and low-note priority

**Per-key state machine on linearised depth d (0 = rest, 1 = bottom)**

| Transition | Rule |
|---|---|
| OFF → ON | d rises past **0.70**. Velocity = the §3 slope fit over the preceding samples |
| ON → OFF | d falls below **0.40** (a hysteresis band of 0.30) |
| Re-strike | from OFF without reaching 0.20: the next pass over 0.70 is a new ON. The slope fit uses the samples since the turnaround (≥ 0.25 of travel ≈ 0.6–13 ms of data at ≥ 4 kHz, plenty) |

**Noise margins** [CALC]:
- ADC noise is ≈ 0.6 % of swing.
- Worst-case neighbour crosstalk is ≈ 3 % per pressed neighbour (§6).
- Both are an order of magnitude below the 30 % band, so **there is no chatter.**

**Mono voice rules (unchanged logic, the original's):**
- **Pitch** = the lowest key in ON.
- **Gate/trigger** = rises only when the ON count goes 0 → 1 (single trigger).
- **Repeating one key alone:** ON → OFF (count 1 → 0, gate falls) → ON (gate rises, contours retrigger).
  This is the "double escapement" in firmware.
  - **Requirement: hold the gate low for ≥ 2 ms** (ESTIMATE; confirm against the analog contours' gate
    input in sim). A very fast re-strike can otherwise give a gate-low too short for the contour to see.
  - The firmware stretches a short low to the minimum, adding ≤ 2 ms of latency only on these fast repeats.
- **Re-striking while another key is held:** legato, no retrigger. That's correct single-trigger behaviour.
  - Edge case: if the re-struck key is the *lowest*, the pitch jumps to the next-lowest held key during the
    off interval (a few to tens of ms), and with glide on that's an audible blip.
  - The original does the same. **Optional firmware setting "re-strike holds pitch":** when the lowest key
    goes OFF, defer the pitch change until d < 0.20 or 20 ms pass. Default off.
- **Verdict: feasible, ≈ 50 lines of firmware, no hardware.**

**Flag: velocity has no destination in the v1.2 spec.**
- Both MCP4822s are full (VCO 1–3 plus filter keytrack).
- Velocity currently only reaches USB-MIDI. For it to *sound*, it needs a CV path to the VCA or contour
  amount: a Pico PWM, 2-pole RC and a TL072 half (≈ $0.3–0.5, ESTIMATE), as the AS3360 mod-depth CV does.
- The design team should name the target (loudness, filter, or both). That's a separate item for eng.

## 5. E-K5: real prices (US, quantity 1)

| Item | Pick | Price | Source |
|---|---|---|---|
| **Pivot rod** | K&S 3/32" (2.4 mm) × 36" music wire, **2-pack** | **$3.19** | [Do it Best / Hunts Hardware](https://huntshardware.doitbest.com/shop/hardware/angle-bar-and-rod-stock/plain-and-threaded-rod/music-wire/kands-332-in-x-36-in-steel-music-wire?SKU=278025); also at Ace and other hardware stores, so buy in person and pay $0 shipping. A 1/8" (3.2 mm) K&S rod is the near-3 mm choice, at a similar price (UNVERIFIED). Cut to 290 mm with a cut-off wheel (music wire is too hard for side cutters) |
| **Spring tube**, 1/8" ID × 1/4" OD silicone | Zoro Select, **70A**, 2 ft | **$4.79** | [Zoro](https://zoro.com/zoro-select-tubing-silicone-18-id-14-od-zusa-ht-1636/i/G8074474). 25 × 8 mm = 0.2 m, so 2 ft covers the build plus spares |
| | **50A** (softer, better for ≈ 50 g keys), by the foot | **$0.77/ft** | [small online shop](https://reach.dog/shop/cold-colder/products/silicone-tube-1814) (shipping not shown, ESTIMATE $4–6). Buy both durometers if unsure: the first-key check picks |
| **Pivot grease, lean** | Permatex 81150 dielectric (silicone) grease, 0.33 oz | **$6.62** | [FCP Euro](https://www.fcpeuro.com/products/dielectric-tune-up-grease-81150) ($8.25 at [Walmart](https://www.walmart.com/ip/17757472)); also at any auto-parts store |
| Pivot grease, "real damping" | Nyogel 767A, 25 g | **$39.94** | [desertcart US](https://www.desertcart.us/products/205878286-nyogel-767a-synthetic-heavy-damping-grease-by-nye-lubricant-25g.md). ≈ 6× the lean option: **not for Little D** |
| **Delrin** (COMB only) | Acetal copolymer, 12 × 12 × 1/16" (1.6 mm) | **$31.69** | [Zoro](https://www.zoro.com/usa-industrials-white-acetal-copolymer-plastic-sheet-12-l-x-12-w-x-116-thick-bulk-ps-ac-908/i/G7856753/). No 2.0 mm sheet was found at qty 1. 1/16" is the US stock size; redo the §3C flexure calc at 1.6 mm (stiffness ∝ t³, ≈ 0.5× the force). Copolymer is not Delrin-brand homopolymer, but it lasers the same (ESTIMATE). Ask Vector Space permission first |
| **Felt, thick** (bottom-stop rail) | F7 wool felt strip, 1/4" × 1/2" × 10 ft, adhesive-backed | **$3.55** | [Zoro](https://www.zoro.com/zoro-select-felt-strip-f7-14-in-t-12-x-120-in-2fjk7/i/G0791061/) |
| Felt, thin (lip top stop, washers) | 1/16"–1/8" wool or craft felt sheet, laser-cut at Vector Space | ESTIMATE $2–5 | The 1/8" Zoro strips found were discontinued. Felt is already in budget §v1.3's $5 stops line |
| (Reference) real piano front-rail punchings | ≈ 100 per set | $16.45 | [Howard Piano Industries](https://howardpianoindustries.com/front-rail-felt-punchings). Not needed: laser-cut felt does the same job |
| Magnets (option) | K&J D31, 4.76 × 1.59 mm N42 | $0.19 each → $4.75 for 25 + shipping | [K&J](https://www.kjmagnetics.com/proddetail.asp?prod=D31), US. Can replace the $8 ESTIMATE |

**Lean RAIL key cost (25 keys)** [CALC]

| Line | Bought acrylic | Scrap acrylic |
|---|---|---|
| 30 SS49E | $11.40 | $11.40 |
| 25 magnets (ESTIMATE as §v1.4b; K&J ≈ $5 + ship) | $8.00 | $8.00 |
| Acrylic: ≈ 128 in² needed (50 blades, 25 tops, comb, rail, rod supports) = 3 sheets + shipping | $17 | $0–5 |
| Rod | $3.19 | $3.19 |
| Silicone tube | $4.79 | $4.79 |
| Permatex grease | $6.62 | $6.62 |
| Sensor 3.3 V LDO (§3) | $0.50 | $0.50 |
| Zoro shipping | $0–6 (ESTIMATE) | $0–6 |
| **Total** | **≈ $52–58** | **≈ $35–46** |

**Compared with SWITCH ($50–55):**
- **RAIL is at parity with bought acrylic.** It also saves ≈ 2.8 in² of strip area (a single-row 280 × 15
  strip against 280 × 25), ≈ −$2–3.
- **The v1.10 totals don't change.** Budget §v1.10 now lists both rows.

## 6. E-K6: crosstalk, including the RAIL-M magnet "let-off"

**Main sensing magnets** [CALC, current-loop model, N35, gaps from §2]:
- A neighbour's field at a sensor is the vertical component at a lateral offset, which is **opposite in sign**
  to the own-key field. So a pressed neighbour makes a key read slightly *more released*, never pressed:
  **it can't cause a false note.**

| Neighbour spacing | Neighbour at rest | Neighbour at bottom | Δ when the neighbour is pressed | Share of own swing (470 G) |
|---|---|---|---|---|
| **10.5 mm** (RAIL/COMB sensor grid) | −0.4 G | −14.6 G | **−14 G** | **≈ 3 %** |
| 18.7 mm (white-key pitch) | −2.9 G | −4.5 G | −1.7 G | ≈ 0.4 % |

- Even two held neighbours (−6 %) sit far inside the 30 % hysteresis band and don't move the 0.70 trigger
  point meaningfully: ≈ 0.02 of depth after linearising.
- **Rest learning:** learn at wake with no keys held, and update only on keys that have been idle for more
  than 1 s while their neighbours are also idle.

**RAIL-M rear magnets** (5 × 2 N35 at ≈ 12 mm from the rod, ≈ 12 mm above the sensor plane, under a steel bar
in the lip; modelled as dipole plus steel image) [CALC]:

| Effect | Value | Verdict |
|---|---|---|
| Static field at the key's own sensor (28 mm away) | ≈ −1.0 G | Calibrated out |
| Static field at the neighbour sensors (10.5 / 18.7 mm) | ≈ −0.96 / −0.86 G | Calibrated out |
| **Change when the key is pressed** (rear magnet moves 0.85 mm) | **≈ 0.01–0.02 G (< 0.005 % of swing)** | **Negligible** |
| Steel bar in the lip, ≈ 25 mm from the main magnets | Fixed relative to the sensors, so a static shift (ESTIMATE ≤ a few G) | Calibrated out |
| **Side force between adjacent rear magnets** (parallel dipoles side by side repel) | **≈ 3.5 gf at 10.5 mm** (N35; 5.2 gf for N52), 0.35 gf at 18.7 mm | It pushes keys against their guides. It cancels in the middle of the row; the two end keys feel ≈ 3.5 gf outward. **Use felt guide slots.** Fine |
| Breakaway at the key front | Contact pull for a K&J D31-class magnet on thick steel is 0.34 kg ([K&J](https://www.kjmagnetics.com/proddetail.asp?prod=D31)). At a 0.5 mm felt gap, assume ≈ 50–60 % (ESTIMATE) ≈ 0.2 kg, × 12/72 lever ≈ **30–35 g at the front**, falling fast as the gap opens | Same order as first-principles' 50 g ESTIMATE; tune with felt thickness. Bench-check it |

**Verdict:** RAIL-M is electrically harmless at either pitch. Its only real cost is +$8–13 and a little side
load. Keep it as the "if the first key feels too soft" option.

---

## 7. What changes elsewhere

**budget-variant.md:**
- In §v1.4b, the gaps become 2.8 / 5.6 mm, the sensors lie flat, they get their own LDO, and the velocity
  method is the slope fit.
- §v1.10's keys row gains the lean RAIL cost.

**first-principles.md (for the design team):**
- RAIL height becomes ≈ 22 mm to the white surface and ≈ 26 mm to the lip.
- Move the magnet to ≈ 38.5 mm from the rod.
- Add rod support combs every 3–4 keys.
- Sharps riser goes to 3 mm.
- Box depth needs ≈ 180 mm, or overlap the lip zone with the main board.

**Bench test** (§v1.4b's $8 test, extended):
- Add the field-against-gap curve on a real SS49E at 3.3 V, so we know where it saturates.
- Build one RAIL key on scrap with both tube durometers.

## Sources
- Honeywell SS49E datasheet: https://atom.ubbcluj.ro/alpar/datasheets/sensors_actuators/Honeywell%20SS49E.pdf
- Pico 2 datasheet (3V3 load, ADC pins): https://pip-assets.raspberrypi.com/categories/1005-raspberry-pi-pico-2/documents/RP-008299-DS-3-pico-2-datasheet.pdf
- RP2350 12-bit ADC: https://www.tomshardware.com/raspberry-pi/raspberry-pi-pico/whats-inside-the-raspberry-pi-pico-2s-rp2350
- Askenfelt, key velocities: https://www.speech.kth.se/music/5_lectures/askenflt/motions.html
- K&J D31: https://www.kjmagnetics.com/proddetail.asp?prod=D31
- Prices: the links in the §5 table.
