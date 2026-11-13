# Little D: engineering answers, design round 4 (E-L9, E-L9b, E-L10, speaker, E-L8)

Status: rev 0, 2026-11-12. This answers `design/little-d/notes/systems.md` (rev 7 open questions),
`concepts/common-how-it-works.md` (rev 6) §3 and §8, `fold/how-it-works.md` (rev 4), `hush/how-it-works.md` (rev 6)
and `one-sheet/how-it-works.md` (rev 4).

Conventions are as in `budget-variant.md`:
- link = read this session;
- **ESTIMATE** = my number;
- **UNVERIFIED** = a source exists but I couldn't confirm the figure;
- **[ENG]** = engineering judgement;
- **[CALC]** = arithmetic shown.

This doc states constraints only. Where things go on the panel and how they look stay with the design team.
Spec changes are in `budget-variant.md` **rev 10**.

## 0. Bottom line

- **E-L9, flat concepts (HUSH / ONE SHEET): no, the voice and digital do not fit on 268 × 85.**
  - Even built dense, it needs **≈ 268 × 100–120**. Plan on **268 × 115**, so the body grows **≈ +30 mm at the back**, as common §3 allows.
  - "Dense" means:
    - 1/8 W resistors standing at 2.54 mm pitch;
    - every top-side part ≤ 6.5 mm;
    - the Pico on the underside.
  - Built with ordinary 1/4 W horizontal resistors, it needs ≈ 268 × 170.
  - The old 280 × 100 figure in `budget-variant.md` was never checked part by part, and it was optimistic too.
- **E-L9, FOLD: the base works; the lid doesn't.**
  - **Base board 270 × 78: fits.** It carries the keys, the PLAY row, 2 muxes and the sensor LDO. The PLAY strip runs at ≈ 46 % courtyard fill.
  - **Lid board 262 × 50: short by ≈ 9,000–12,000 mm².** It needs ≈ 262 × 82–95. The band can't help, because the speaker and battery fill its full 10.6 mm height.
  - The design team needs to find that area (§1.4 lists the options and what each costs).
- **E-L9b: everything except EMPHASIS can cross the ribbon, with ground guards.**
  - **EMPHASIS should stay on the same half as the ladder**, and the ladder stays in the lid next to the passive mixer.
  - So either the EMPHASIS knob goes in the lid, or it stays in the base with a buffered crossing *and* a bench test before boards are ordered (risk: scan-rate whine at high emphasis).
  - **VOLUME can cross** (low-impedance, line level, guarded). Nothing should move to the base.
  - Ribbon size: **34-way is enough if EMPHASIS stays in the lid; 40-way if it crosses.**
- **E-L10:**
  - I found **no US-stocked LiPo ≤ 30 mm wide with useful capacity**. The only verified one is Adafruit #1578: 29 mm wide, 500 mAh, about 25–40 min of play.
  - A ≈ 7 × 30 × 120 mm pouch would hold ≈ 3,000+ mAh [CALC], but I can't source one (UNVERIFIED).
  - **FOLD default: a USB power bank.**
  - **Bigger finding:** my recount of the power budget is **≈ 2.0–3.6 W at 5 V**, not 1.0–1.5 W. The internal #2011 therefore lasts **≈ 1.8–3.3 h**, not 3.5–7 h (§3).
- **Speaker (240, 113): OK.** Keep every ladder part, the expo pair and the emphasis loop **≥ 55 mm from the speaker centre** (25 mm radius + 30 mm). The natural ladder spot, between EMPHASIS and the mixer, gives ≈ 32–40 mm edge clearance.
- **E-L8: the BOM pot doesn't take 18T knobs.**
  - Tayda A-5531 has a **40-tooth** fine-knurl shaft.
  - **Switch to Tayda A-5622, a T18 spline pot at $0.59** (+$3.22 across 23 pots), with black 18T push-on knobs.
  - KN1250 is a **set-screw knob with a 6.4 mm round bore**, not a push-on.
  - The WAVE rotary has a 6 mm spline shaft (18T likely, UNVERIFIED).
  - **New risk:** the rotary body (Ø 16) and the toggle body heights may exceed the 7 mm under-panel space. Measure them before freezing panel z.

---

## 1. E-L9: board area

### 1.1 Method

I summed each part's **courtyard** (body plus pads, as placed), then divided by an achievable fill for a hand-soldered,
2-layer, through-hole board: **65–75 %** for a dense layout [ENG]. Eurorack THT boards land around 60–70 %.

Part counts come from `budget-variant.md` §v1.2–v1.3: 350 resistors, 13 TL072, ≈ 50 transistors and so on.

### 1.2 Courtyard tally (whole instrument, flat concepts)

| Group | Qty | Courtyard each (mm²) | Total (mm²) |
|---|---|---|---|
| 9 mm pots (9.5–9.8 mm base, [Tayda](https://www.taydaelectronics.com/tayda-10k-ohm-linear-taper-potentiometer-spline-shaft-pcb-mount-9mm.html)) | 23 | ≈ 10 × 12.5 = 125 | 2,875 |
| WAVE rotary, Ø 16 body ([Stompbox Parts equivalent](https://stompboxparts.com/switches/1p8t-mini-rotary-switch)) | 3 | ≈ 18 × 18 | 970 |
| Sub-mini toggles (body UNVERIFIED) | 7 | ≈ 8 × 13 | 730 |
| #2765 stick | 1 | 17.5 × 17.4 | 305 |
| LEDs | 2 | — | 40 |
| DIP-8: 13 TL072, 2 MCP4822, LM386, 6N138, 2 MC34063 | 19 | ≈ 105 | 2,000 |
| DIP-14: 3 AS3046, AS3360 | 4 | ≈ 205 | 820 |
| DIP-24: 3 CD4067 | 3 | ≈ 31 × 16.5 | 1,530 |
| Pico 2 (lost on both sides: the pin rows are THT) | 1 | 51 × 21 | 1,070 |
| TO-92: transistors, JFETs, 78L/79L09 | ≈ 52 | ≈ 22 | 1,150 |
| LD1117 TO-220, laid flat | 1 | — | 200 |
| **Resistors, 1/8 W standing** ([Tayda 1/8 W range](https://www.taydaelectronics.com/resistors/1-8w-metal-film-resistors.html); body ≈ 3.3 mm, UNVERIFIED) | 350 | ≈ 8 | **2,800** |
| *(Resistors, 1/4 W horizontal at 10.16 mm)* | *350* | *≈ 37* | *(12,950)* |
| Film caps | 20 | ≈ 30 | 600 |
| Electrolytics (low-profile ≤ 6.5 mm or laid flat) | ≈ 30 | ≈ 45 | 1,350 |
| Ceramics | ≈ 60 | ≈ 15 | 900 |
| Diodes | ≈ 20 | ≈ 20 | 400 |
| MC34063 inductors | 2 | ≈ 100 | 200 |
| Headers: strip C harness (2 × 14), I/O, speaker, battery | — | — | 700 |
| Tempcos | 3 | — | 60 |
| **Total, dense** | | | **≈ 19,500** |
| *Total with 1/4 W horizontal resistors* | | | *≈ 29,700* |

**Board needed (dense):** 19,500 / (0.65–0.75) = **26,000–30,000 mm²**. At 268 wide that is **97–112 mm deep**; I plan on **115** for routing slack.

**What 268 × 85 holds:** 22,780 mm², so ≈ 14,800–17,100 mm² of courtyard at that fill. It's short by ≈ 2,400–4,700 mm² of courtyard, which is **≈ 15–35 mm of depth** [CALC].

### 1.3 Flat concepts (HUSH, ONE SHEET): constraints

- **Main board ≈ 268 × 115** (≈ 30,800 mm², 47.8 in²), y ≈ 52–167 in the ONE SHEET frame.
  - Common §3's rule applies: the extra depth goes **behind the back row**. Rows and keys are unchanged.
  - ONE SHEET then ≈ 276 × 170, HUSH ≈ 290 × 174 [CALC].
  - Where the rows sit inside that depth is the design team's call.
- **Possible saving, layout-dependent:** move the key muxes (2 × CD4067) and the LD1117 onto **strip C's underside**.
  - Under the raised strip there's ≈ 8 mm [CALC from common §4: strip on spacers, keys at 24].
  - That saves ≈ 1,200 mm² of courtyard and turns the 28-wire harness into ≈ 8 wires.
  - It might bring the main board down to ≈ 268 × 100. Only a real placement will tell.
- **Height rules on the main board** (board top 14.5, shell underside 21.5):
  - **Top side, every part ≤ 6.5 mm seated:**
    - DIPs soldered directly or in low-profile turned-pin sockets (a standard socket plus chip ≈ 7 mm, UNVERIFIED);
    - resistors 1/8 W standing (≈ 5.5–6 mm) or horizontal;
    - electrolytics 5 mm-tall types or laid flat;
    - box film caps ≤ 6.5 mm (Tayda height UNVERIFIED).
  - **Underside:** 9.9 mm from the board's underside to the back panel, minus 1.5 mm lead tails.
    - The **Pico goes on the underside with a total stack ≤ 8 mm**. A standard 8.5 mm female header + Pico doesn't fit. Use low-profile machine-pin strips or solder it directly.
    - The MC34063 inductors (≈ 10 mm tall radials, UNVERIFIED) also don't fit on top. Put them on the underside, away from the speaker and battery, or use low-profile parts.
  - **Lead tails over the speaker and battery are fine at ≤ 1.5 mm.** The common stack (board top 14.5) leaves 2.3 mm over the 7.6 mm speaker. So the contour pots and DECAY toggle above the speaker are OK electrically and mechanically.
- **HUSH's question:** strip C at y 8–56 and the main board from y 58 sit side by side with a 2 mm gap. That works. Put the harness header at the shared edge.
- **Cost:** see §6. Board area rises because the main board grows *and* strip C is now 270 × 47 (19.7 in²), not 280 × 25.

### 1.4 FOLD

**Base board 270 × 78: fits.**
- **Keys region (y 4–51):** switches and sensors, the same as strip C.
- **PLAY strip (≈ 270 × 27 = 7,300 mm²):**
  - controls: 7 pots, 4 toggles, the stick and 2 LEDs (1,630 mm²);
  - 2 × CD4067 (1,020 mm²);
  - LD1117 (200 mm²);
  - ribbon box header (≈ 270 mm²);
  - decoupling (200 mm²).
  - That's ≈ 3,300 mm², **≈ 46 % fill**.
- **Heights:**
  - board top 6.1 and plate underside 13.1 give 7 mm, so CD4067s are soldered directly or in low-profile sockets, and the LD1117 lies flat;
  - the underside has 1 mm of air after tails, so **nothing goes on the base board's underside**.

**Lid board 262 × 50 (13,100 mm²): doesn't fit.**
- The lid side needs ≈ 16,100 mm² of courtyard: the whole instrument minus what the base takes.
- That means **≥ 21,500–25,000 mm²** of board. At 262 wide that's **82–95 mm deep** against 50.
- **The band can't take it.** Its inner height is 10.6 mm, filled by the 10.3 mm speaker and the battery. A board over them leaves no room.
- **Constraint for design:** FOLD needs **≈ 9,000–12,000 mm² more board**. Ways to get it (the design team's choice) [CALC, ESTIMATE]:

| Route | What it costs |
|---|---|
| Deeper halves | Lid board ≈ 262 × 90, halves ≈ 126 deep (from 86). Closed ≈ 286 × 126 × 50 |
| Second board stacked in the lid (mezzanine) | Lid +≈ 10–12 mm, so closed ≈ 60–62. Plus one more board-to-board connector |
| Second board under the keys in the base (digital only: Pico, DACs, MIDI ≈ 3,000–3,800 mm² courtyard) | Base +≈ 9 mm, so closed ≈ 59. **Not enough on its own** (≈ 5,000 mm² of board against 9–12k needed), and it adds ≈ 10 ribbon lines (pitch CVs, count inputs, PWM CVs). Power inductors must not go under the Hall sensors (≥ 30 mm away) |
| Electronics in a separate box | Out of scope (not "unibody") |

---

## 2. E-L9b: what can cross the FOLD hinge ribbon

### 2.1 Aggressors and victims

- **Aggressors:**
  - **Mux selects S0–S3:** 3.3 V edges, switching at the scan rate. The scan is ≥ 4 kHz per key (`velocity-and-keys-v2.md`), so it puts **audible tones (4 kHz and harmonics)** onto any line it couples into.
  - **Osc 3** on MOD MIX: up to ±5 V, saw or square edges at audio rate.
- **Coupling** [ESTIMATE]:
  - 1.27 mm flat ribbon has ≈ 0.3–0.5 pF/cm between neighbours, so ≈ 3–4 pF over 80 mm.
  - A 3.3 V edge then injects Q = C·V ≈ 13 pC.
  - Into a high-impedance node of ≈ 100 pF, that's a **≈ 100 mV spike**.
  - A grounded conductor between them cuts this by roughly 10× [ENG].

| Line(s) | Signal, impedance | Sensitivity | Verdict |
|---|---|---|---|
| **EMPHASIS (3)** | Ladder output → pot → **ladder input-pair base**. The input pair sees the passive mixer at tens of mV, and the loop is regenerative near self-oscillation | **Highest in the instrument.** A tone injected here rings at the resonance, and a 4 kHz scan tone or osc-3 bleed becomes audible | **Don't cross the raw loop.** See §2.2 |
| VOLUME (3) | VCA out (op-amp, low Z, ≈ 1 V) → pot → output stage; wiper ≤ 2.5 kΩ | Low–moderate: ≈ −70 dB pickup with guards [ESTIMATE] | **Cross**, with a ground on each side |
| MOD MIX (3) | Osc 3 and noise (buffered, low Z) → wiper → mod bus | Osc 3 is an **aggressor** | Cross. Ground between osc 3 and everything else |
| CONTOUR AMT (3) | Contour CV (low Z) → wiper → filter CV summer (through a resistor) | Low. 1 mV of pickup ≈ 1.2 cents of cutoff wobble [CALC at 1 V/oct] | Cross. RC at the summer input (1 kΩ + 10 nF) |
| OSC MOD, FILTER MOD (2 + 2) | Mod bus (after the AS3360, low Z) | Low | Cross |
| KBD CTRL (3) | Keytrack CV from the buffered MCP4822 | Low (DC, low Z) | Cross |
| MUX A / B out (2) | Hall voltages to the Pico ADC | Moderate: a select edge lands during the sample | Cross, with **a ground between selects and mux outs** |
| LEDs (2), 5 V / GND, S0–S3 | — | Aggressors | Keep them at one edge of the ribbon |

### 2.2 Recommendation

1. **Keep the EMPHASIS pot on the same half as the ladder.** The ladder stays in the lid, because the passive mixer → ladder-input bus is even more sensitive than EMPHASIS and must not cross. The ladder doesn't move to the base.
2. **If the EMPHASIS knob has to stay in the base** (that's the design team's call), it can cross only like this:
   - drive the pot ends from the ladder's low-Z output buffer;
   - put the series feedback resistor **at the ladder** in the lid, so the high-impedance base node never leaves the lid board;
   - guard both conductors with grounds;
   - **bench-test before the board order:** 80 mm of ribbon between two perfboards with the real scan running, EMPHASIS at maximum, cutoff swept through 1–8 kHz. Pass = no audible scan tone at the phones output.
   - The risk if it fails is a scan-rate whine at high emphasis. Then EMPHASIS moves to the lid.
3. **VOLUME crosses.** Moving it buys nothing measurable.
4. **Nothing moves to the base.** Moving the filter or VCA there would make the mixer bus or the VCA output cross, which is worse.
5. **Power over the ribbon:**
   - The battery and charger are in the lid, so the base needs **5 V for the sensor LDO** (150–250 mA). Use **2 × 5 V and 2 × GND conductors**: 28 AWG ≈ 0.21 Ω/m, so ≈ 2 mV of drop each [CALC]. This replaces "battery + / −".
   - The LD1117 sits in the base at the strip.

**Ribbon allocation:**
- **EMPHASIS in the lid:**
  - 10 digital/power lines, 16 analog, 2 LEDs, ≥ 5 grounds (power/digital edge, around the mux outs, around osc 3, either side of VOLUME): **33**.
  - **The 34-way fits.**
- **EMPHASIS crossing:**
  - 10 + 19 + 2 + ≥ 7 grounds = **38**.
  - **Use a 40-way** (2 × 20 at 1.27 mm, ≈ 51 mm wide).
- **Order across the ribbon:**
  - **digital edge:** 5 V, GND, S0–S3, GND, mux outs, GND, LEDs;
  - **middle:** CV lines (KBD, mod, CONTOUR AMT);
  - **guarded far edge:** MOD MIX, VOLUME and (if crossing) EMPHASIS.

**Flex life** [ENG; flex life of PVC ribbon UNVERIFIED]:
- Use a rolling loop with bend radius ≥ 10× the cable thickness (≈ 10 mm).
- Clamp both ends so the IDC contacts never flex.
- Cycle-test a sample loop ≥ 2,000 folds before committing.
- Silicone flat cable is the fallback if PVC cracks.

---

## 3. E-L10: battery, and a corrected power budget

### 3.1 Power budget recount (ESTIMATE; measure at first power-up)

| Load | Basis | At 5 V |
|---|---|---|
| ±9 V voice (via ±12 V MC34063 → 78L/79L09) | 13 TL072 at ≈ 2.8 mA typ, + 3 VCO cores, ladder, contours, VCA, AS3360 ≈ **40–50 mA per rail**. 24 V × 45 mA ≈ 1.1 W at the rails; MC34063 boost ≈ 75 %, inverter ≈ 65 % [ENG] | **1.2–1.9 W** |
| 25 SS49E via the LD1117 | 150–250 mA (6 mA typ / 10 max each, Honeywell). **A linear LDO draws the same current from 5 V**, so 5 V × I, not 3.3 V × I as `velocity-and-keys-v2.md` §2.4 counted. Current at a 3.3 V supply may be lower (UNVERIFIED) | **0.6–1.25 W** |
| Pico 2 | ≈ 20–30 mA | 0.1–0.15 W |
| LM386 + speaker (average, playing) | 4 mA quiescent; ≈ 0.2 W peak out | 0.02–0.3 W |
| Muxes, DACs, MIDI, LEDs | — | ≈ 0.05 W |
| **Total** | | **≈ 2.0–3.6 W (0.4–0.7 A)** |

**From a LiPo:** the bq25185 boost (≈ 85–90 %, ESTIMATE) means ≈ 2.2–4.2 W at the cell. The #2011 holds 2000 mAh × 3.7 V = 7.4 Wh, so **≈ 1.8–3.3 h**.

That replaces the "5–7 h" in v1.2 and v1.6, and the "3.5–5 h" in rev 8. The boost's 1 A rating still covers 0.7 A.

**Consequences:**
- **Power sequencing is now mandatory.** The boost stalls above ≈ 200 mA at a hard start, and the sensors alone draw up to 250 mA. Bring the sensor LDO up last, behind a Pico-switched P-MOSFET after the rails are up [ENG]. That's +1 TO-92 FET + 2 resistors, ≈ $0.30, ESTIMATE.
- **A power bank never auto-offs at 0.4–0.7 A**, so that rev-0 risk is gone.
- **Option for the flat concepts (not adopted):** a 3000 mAh pouch, [PiShop 755060](https://www.pishop.us/product/lithium-ion-polymer-battery-3-7v-3000mah/). Size from the name is 7.5 × 50 × 60 (UNVERIFIED). It fits under the main board: 9.9 − 7.5 = 2.4 mm, keep it lead-free. That gives ≈ 2.7–5 h. A ready-made 3.3 V buck module in place of the LDO would save ≈ 0.2–0.4 W [ENG].

### 3.2 FOLD's band (x ≈ 20–165, d 2–32, ≤ 10.6 mm)

| Candidate | Size | Capacity | Runtime at 2.2–4.2 W | Status |
|---|---|---|---|---|
| Adafruit #2011 | 60 × 36 × 7 | 2000 mAh | 1.8–3.3 h | **36 wide: doesn't fit** |
| [Adafruit #1578](https://adafruit.com/products/1578) | **29 × 36 × 4.75** | 500 mAh, with PCM, $7.95, in stock | ≈ 0.4–0.8 h | Fits, but useless |
| Generic "603090 / 703090"-class pouch | ≈ 6–7 × 30 × 90 | ≈ 2,100–2,500 mAh [CALC: #2011's 132 mAh/cm³ × volume] | ≈ 1.9–4.1 h | **No US-stocked listing found** (UNVERIFIED) |
| ≈ 7 × 30 × 120 pouch | fills the band, leaving room for leads | ≈ 3,300 mAh [CALC] | ≈ 2.9–5.5 h | Not found (UNVERIFIED) |
| 18650 cell | Ø 18.5 | 2,200+ mAh | — | 18.5 tall > 10.6: doesn't fit |
| Two small pouches in parallel | — | — | — | Not recommended (paralleled protected cells) |

**Recommendation: FOLD defaults to a USB power bank** (cable at the lid's right wall).

An internal cell becomes an option only if a protected ≤ 8 × 30 × ≤ 130 mm pouch is sourced and checked in hand. Leave ≥ 1 mm of swell room, so the cell is ≤ 9.5 mm thick in the 10.6 mm band.

If an internal battery is a must for FOLD, the band would need ≥ 38 mm of clear width for the #2011. That's a layout call for the design team.

---

## 4. Speaker at (240, 113) vs the ladder (HUSH: (247, 113) in its own frame, the same point)

- The speaker covers a 25 mm radius: x 215–265, y 88–138.
- **Rule:** ladder pairs, film caps, the filter expo pair and the emphasis feedback trace all stay **≥ 55 mm from (240, 113)**.
  - That's x ≤ 185 at y ≈ 113, or x ≤ 183 at y 100.
- **The natural ladder spot satisfies it.** Between EMPHASIS (164, 68) and the mixer (137–157, 100–123), at roughly x 135–180, y 75–100, the nearest corner (180, 95) is 62.6 mm from the centre, ≈ **38 mm edge clearance** [CALC].
- The CONTOUR AMT pot (188, 68) is 69 mm away, 44 mm from the edge ✓.
- The VCO expo arrays (x 30–110) are far away ✓.
- **Output stage:** put the LM386 next to VOLUME (243, 68), ≥ 30 mm from the ladder.
  - Speaker leads go LM386 → speaker, twisted, ≤ 60 mm.
  - The LM386's 5 V supply and return go straight to the power entry (a star point), not through the analog ground under the ladder.
- **If the body grows at the back** (§1.3), the speaker may stay or move back. Both meet the rule. Keep its centre ≥ 60 mm from the nearest Hall sensor (unchanged).

---

## 5. E-L8: knobs and shafts

| Part | Shaft (read this session) | Knob that fits |
|---|---|---|
| **Tayda A-5531** (current BOM, $0.45) | Knurled plastic, **40 teeth**, 6 mm, 12.4 mm long, 9.8 mm base, 7 mm mounting hole, 2,335 in stock ([Tayda](https://www.taydaelectronics.com/tayda-10k-ohm-linear-taper-potentiometer-round-knurled-plastic-shaft-pcb-9mm.html)) | **Not 18T knobs.** A fine knurl into an 18-tooth bore keys poorly (UNVERIFIED in hand; don't count on it) |
| **Tayda A-5622 (pick)**, $0.59 | **T18 knurled spline**, 6.00 mm, 10 mm + 5 mm thread, 9.5 mm base, 7.5 mm hole, 3,968 in stock ([Tayda](https://www.taydaelectronics.com/tayda-10k-ohm-linear-taper-potentiometer-spline-shaft-pcb-mount-9mm.html)) | 18T push-on |
| Alpha A-4728 (fallback), $1.29 | T18 spline, 15 mm ([Tayda list](https://www.taydaelectronics.com/catalogsearch/result/?q=b10k)) | 18T push-on |
| Tayda A-5518, $0.59 | Round 6.35 mm ([same list](https://www.taydaelectronics.com/catalogsearch/result/?q=b10k)) | Set-screw (KN1250 class) |
| **WAVE: Tayda RS16211**, $1.21 | **6 mm spline**, 20 mm, 9 mm mounting hole (M9). Tooth count not stated ([Tayda](https://www.taydaelectronics.com/mini-rotary-switch-1-pole-8-position-alpha-rs16211-20mm.html)). Alpha's 17 mm rotary family offers an 18-tooth knurled shaft ([R1712F datasheet](https://www.mouser.com/datasheet/2/13/R1712F-1522327.pdf)), so 18T is likely (UNVERIFIED). Body Ø 16 ([Stompbox Parts equivalent](https://stompboxparts.com/switches/1p8t-mini-rotary-switch)) | 18T push-on if it's 18T; otherwise a set-screw knob |

**Knobs:**
- **[KN1250](https://www.taydaelectronics.com/kn1250-knob-yellow.html)** (the design's reference size, 14.86 × 10.45) is a **round-bore 6.4 mm set-screw** knob, $0.49, yellow at Tayda. Black is the TE Alcoswitch KN1250B variant (UNVERIFIED stock).
  - On a 6 mm spline it sits up to 0.2 mm off-centre and squeezes the split [CALC: 0.4 mm clearance].
  - It works, but it's not the right pairing.
- **Black 18T push-on:** Tayda [plastic black 15 × 14](https://taydaelectronics.com/plastic-black-knob-15x14mm-shaft-hole-6x18t.html) is actually 14.5 Ø × 13.5 tall, 6 mm × 18T bore, 328 in stock. Price wasn't shown, and the page doesn't say push-on vs set-screw (push-on assumed, UNVERIFIED).
  - It's 3 mm taller than the KN1250, so knob tops rise ≈ 3 mm unless the shafts are cut.
- **Recommendation:**
  - **All 23 pots → A-5622 (T18 spline) + black 18T push-on knobs.**
  - Confirm A-5622 is stocked in every value used: 10k, 50k, 100k. Only 10k was read; the other values are UNVERIFIED.
  - This suits the "knobs pushed on last, pulled off for service" flows.
  - CUTOFF's 1083 hero knob: check its bore type the same way.

**Shaft length and height constraints** (flat concepts; FOLD scales the same way):
- A-5622 tip = pot body top + 15. Board 14.5 + body 7 = 21.5, so the bushing top is at 26.5 (2.5 above the 24 face ✓, as common §5) and the tip at 36.5.
- **The shaft tip must sit at** (wanted knob top − knob height + bore depth). Measure the bore depth in hand.
- Cut the plastic shafts with a razor saw. Keep the knob skirt ≥ 0.5 mm clear of the bushing top.
- The RS16211's 20 mm shaft must be cut too. Its panel hole is **9.5 mm, not 7.5**.

**Stop at 6 positions:** Tayda lists no adjustable stop, and Stompbox's equivalent "stops at position 8" (UNVERIFIED whether the stop is adjustable). If it isn't, contacts 7–8 are dead (silence). Wire 7 and 8 to repeat 6, or add a mechanical stop. How a printed stop looks is the design team's call.

**New height risk:**
- The common stack gives every board-mounted control **7 mm of body height** under the shell. That's verified for nothing but the pot, and even that was the design's figure.
  - Adafruit's equivalent SP8T rotary is **25.2 × 16.2 × 16.2 mm overall, shaft included** ([datasheet](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8457/2925_Datasheet.pdf)), so the body may be > 7 mm (ESTIMATE 8–12).
  - The sub-mini toggles (Tayda non-threaded PCB) don't list a body height (UNVERIFIED; this class is often ≈ 8–9 mm, ESTIMATE).
- **Measure one of each before freezing panel z.**
- If either is taller than 7 mm, each needs a board cutout (body through the board, on short flying leads) or a local spacer under the panel. Which one is the design team's call. This applies to FOLD's base (7 mm) and lid as well.

---

## 6. Spec changes (`budget-variant.md` rev 10)

| Where | Change | Δ cost |
|---|---|---|
| §v1.2 Power | ≈ 1.0–1.5 W → **≈ 2.0–3.6 W at 5 V** (recount). LiPo runtime **≈ 1.8–3.3 h** (#2011). Sensor LDO switched on last by a P-FET | +≈ $0.30 |
| §v1.2 One board | Main board **≈ 268 × 115** (flat concepts), 1/8 W standing resistors, top-side ≤ 6.5 mm, Pico on the underside (≤ 8 mm stack) | (board line) |
| §v1.3 Resistors | 1/4 W → **1/8 W metal film** (Tayda range; price ESTIMATE same) | ≈ $0 |
| §v1.3 Pots | A-5531 (40T) → **A-5622 T18 spline, $0.59** ×23 | **+$3.22** |
| §v1.3 Knobs | 18T push-on, black (Tayda); KN1250 only on round shafts | ≈ $0 (price UNVERIFIED) |
| §v1.10 Boards | main 268 × 115 (47.8 in²) + strip C 270 × 47 (19.7 in²) = **67.5 in²** (was 54.3) → **$71–122** (was $63–106) | **+$8–16** |
| §v1.10 Totals | (a) **≈ $272–345**, (b) **≈ $256–327**. With LiPo: (a) ≈ $293–366, (b) ≈ $277–348 | +$11.5–19.5 |
| §v1.8 Risks | Control body heights vs 7 mm; FOLD lid area; FOLD ribbon EMPHASIS; power sequencing | — |

**FOLD-only:** USB power bank by default. Ribbon 34-way if EMPHASIS stays in the lid, 40-way if it crosses. 5 V (not battery) crosses to the base.

## Sources
- Tayda A-5531: https://www.taydaelectronics.com/tayda-10k-ohm-linear-taper-potentiometer-round-knurled-plastic-shaft-pcb-9mm.html
- Tayda A-5622: https://www.taydaelectronics.com/tayda-10k-ohm-linear-taper-potentiometer-spline-shaft-pcb-mount-9mm.html
- Tayda 9 mm pot list (A-4728, A-5518): https://www.taydaelectronics.com/catalogsearch/result/?q=b10k
- Tayda KN1250: https://www.taydaelectronics.com/kn1250-knob-yellow.html
- Tayda black 18T knob: https://taydaelectronics.com/plastic-black-knob-15x14mm-shaft-hole-6x18t.html
- Tayda RS16211: https://www.taydaelectronics.com/mini-rotary-switch-1-pole-8-position-alpha-rs16211-20mm.html
- Stompbox Parts 1P8T mini rotary: https://stompboxparts.com/switches/1p8t-mini-rotary-switch
- Alpha R1712F datasheet: https://www.mouser.com/datasheet/2/13/R1712F-1522327.pdf
- Adafruit #2925 datasheet: https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/8457/2925_Datasheet.pdf
- Tayda 1/8 W metal film: https://www.taydaelectronics.com/resistors/1-8w-metal-film-resistors.html
- Adafruit #1578: https://adafruit.com/products/1578
- PiShop 755060 3000 mAh: https://www.pishop.us/product/lithium-ion-polymer-battery-3-7v-3000mah/
- SS49E current (via `velocity-and-keys-v2.md`): Honeywell SS49E datasheet
