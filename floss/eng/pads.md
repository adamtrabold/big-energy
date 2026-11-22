# floss pads: buildable 25-pad designs (rev 0, 2026-11-22)

Status: **rev 0**, by the engineer, for Adam. Desk research and arithmetic only; nothing was built.

Adam's decision (verbatim, 2026-11-22): "I don't like springs because they give over time and also I *am* building this so I want something feasible. Pads are fine imo".

Hard requirement: Adam builds floss by hand. SMD is fine where necessary, and boards can be fab-assembled. This file sits beside `feasibility.md` and `keys.md` and doesn't edit them; §5 lists what changes there.

**Marks:** **[chk]** checked against the linked source this session · **[plat]** from Big Energy's eng records · **[calc]** my arithmetic · **[est]** my estimate.

---

## 1. Summary for Adam

**Recommendation: pads that sense force with force-sensing resistors (FSRs), with walnut or silicone tops, read by engine D. Engine B becomes the default: every pad is a voice with its own pressure.**
- **First build: P1, 25 bought Interlink FSRs** under your own pad tops. They're off the shelf with a datasheet, any pad can be swapped on its own, and you can wire one octave first.
- **If the 25 sensor tails are a nuisance, or you build Big Energy too:** P2, one custom 25-pad FSR sheet from a maker. That's how LinnStrument is built. One part, one connector, and quotes start at a single prototype.
- **P3** (gold PCB pads under conductive rubber, as in pressure-sensitive game-controller buttons) is the cheapest, but its pressure is coarser. I don't recommend it as the main sensor.

**What pads change, for the better:**
- **Per-pad pressure is in.** BOW's "lean to keep it alive", TIDE's planted drift and MIDI poly aftertouch all come back.
- **Battery life improves.** FSRs draw almost nothing, where the 25 Hall sensors drew ≈ 0.6–1.0 W. BOW's base pack now gives **≈ 3.7–8.7 h** (5.2 h at moderate volume), up from 2.6–5.6 h [calc].
- **Chips, board and case:** no new chips, and the board is unchanged. The pad stack is ≈ 6–8 mm against the key stack's ≈ 11–20 mm, so case height is set by the knobs, not the keys.
- **Possibly more battery:** the space freed under the pads may hold more cells (to be confirmed by design).

**What pads lose:**
- **Travel.** You press a surface that barely moves.
- **Resting your fingers costs a threshold:** a resting finger mustn't trigger a note.
- **Lift is measured more coarsely.** It's still possible, from how fast pressure falls, but expect a few distinguishable "ways to let go", not a fine scale. With per-pad pressure, easing off becomes a continuous fade under your finger, which covers the job "shape how each note ends by how I lift off" in a different way.

**Decisions for you:**
1. **P1 (bought FSRs, ≈ $300 of sensors) or P2 (custom sheet, quote needed)?** Recommendation: P1 first.
2. **Pad top:** walnut tile on a thin silicone layer (hard, family look, almost no give), or cast silicone cap (soft, ≈ 0.5–1 mm squish, easier control). Felt alone isn't recommended. Recommendation: try both on two pads; it's a feel choice and cheap to test.
3. **Lift:** accept coarse lift speed plus the continuous ease-off fade, as above. Recommendation: accept.
4. **Use the space freed under the pads for battery?** Recommendation: yes, if design confirms the height.

**The "give over time" question, honestly:** pads age too, just less, and in a way firmware can absorb.
- **FSRs:** an FSR's reading drifts less than 5 % per decade of time under a steady load, and it's rated for 10 million presses [chk]. A pad played hard every day reaches that in years [calc].
- **Silicone:** silicone takes a small permanent set, 11–22 % in the standard accelerated test [chk], mostly early in its life. That changes the pad's resting preload, not how hard you can press.
- **Firmware:** it re-learns each pad's zero every time it's untouched, so slow ageing is invisible in play. A worn pad is a $12 part you can replace.
- **For fairness:** steel springs used within their limits don't measurably give either. But pads are simpler to build, so they're the right call for a hand build.

---

## 2. Three buildable designs

### 2.1 How the shipping products do it
| Product | Construction | Source |
|---|---|---|
| **LinnStrument** | Two printed plastic sheets with resistor and FSR material, separated by a spacer with 2 mm separators, under a 2 mm silicone top. Each cell is read by switching row and column ends to ground, +3.3 V or the ADC; with no pressure the ADC reads 3.3 V | [chk, [Roger Linn Design](https://rogerlinndesign.com/support/how-linnstruments-sensor-works)] |
| **QuNexus** (25 pads) | "25 Smart Sensor Keys" that "detect Pressure, Location, and Velocity". Exact build unpublished | [chk, [Synthtopia](https://www.synthtopia.com/content/2012/11/01/the-qunexus-smart-sensor-keyboard-controller-offers-midi-control-voltage-osc-usb-and-polyphonic-aftertouch/)] |
| Keith McMillen's sensor patent | Piezoresistive fabric with conductive traces printed on it, bonded to a PCB's I/O pads by conductive adhesive or pressure, with heat-staked posts. Assigned to BeBop Sensors, now listed as KMI Music | [chk, [US9753568](https://patents.google.com/patent/US9753568)] |
| CNMAT fabric drum pads (research) | Eeonyx piezoresistive fabric between sewn electrode rows and columns. A 16 × 16 array scanned at ≈ 500 Hz with 7-bit pressure | [chk, [NIME 2011](https://www.cnmat.berkeley.edu/sites/default/files/attachments/2011_robust_and_reliable_fabric.pdf)] |
| Fatar poly-aftertouch keybeds | "An FSR matrix to allow the detection of the key pressure independently" | [chk, [Native Instruments](https://www.native-instruments.com/blogs/blog/polyphonic-aftertouch)] |
| DualShock 2 pressure buttons | A conductive disk whose contact area on a PCB strip grows as you press harder, so conductivity rises gradually | [chk, [iFixit](https://www.ifixit.com/Teardown/DualShock+2+Teardown+How+It+Works/107082)] |

### 2.2 The designs side by side
| | **P1. Bought FSR per pad** (recommended first) | **P2. Custom 25-pad FSR sheet** | P3. Gold PCB pads + conductive rubber |
|---|---|---|---|
| Proven? | **Yes**: the FSR per key is Fatar's method | **Yes**: LinnStrument's construction | Yes, but only for coarse pressure (game controllers) |
| Sensor | Interlink FSR 402 short: 0.2–20 N, 0.5 mm thick, ≈ 15 mm active area, **$11.92 each at 25** [chk, [Pololu](https://www.pololu.com/product/2728)] | Sensitronics: "single prototypes to production runs in the millions", **no minimum for custom work**, prototypes 2–4 weeks; ThruMode is preferred where "fine force control" matters [chk, [Sensitronics FAQ](https://sensitronics.com/faq.html)] | Interdigitated gold (ENIG) fingers on the fab-made pad PCB + a conductive-rubber pill in each pad top [est] |
| Build steps | (1) Order a pad PCB (backing board with 25 pad lands and divider resistors; fab-assembled SMD). (2) Stick an FSR on each land. (3) Plug each tail into a solderless connector. Don't solder the tails: FSR tails melt [plat, `eng/aftertouch.md`]. (4) Fit an actuator puck and pad top over each FSR. (5) Fit the deck plate that retains the pads | (1) Draw the 25-pad layout (send pad positions and tail route). (2) Order the sheet. (3) Plug one flex tail into one connector on the main board. (4) Fit pad tops and deck | (1) The pad PCB has the fingers (no extra part). (2) Cast silicone tops with a carbon pill, or glue conductive-rubber dots under them. (3) Fit deck |
| Parts cost, 25 pads | ≈ $298 sensors + ≈ $25–50 connectors + ≈ $10–30 tops + ≈ $20–40 PCB ≈ **$350–420** [calc/est] | **Quote needed**; ≈ $200–600 for a prototype [est] | ≈ **$30–60** [est] |
| Sensor thickness | 0.5 mm [chk] | ≈ 0.3–0.5 mm [est] | 0 (on the PCB) |
| Pressure quality | ±2 % repeatability on one part, ±6 % part to part, ≈ 10 % hysteresis, < 5 % drift per decade of time [chk, [Interlink 400 series](https://www.teachengineering.org/content/uconn_/activities/uconn-2662-contractions-calculations-force-resistance-activity/uconn-2662-contractions-calculations-FSR400series-datasheet.pdf)] | Similar. Sensitronics quotes "ballpark ± 10 %" absolute accuracy, with cycle-to-cycle repeatability held [chk, [Sensitronics FSR 101](https://cdn.hackaday.io/files/1653337073607072/Sensitronics%20FSR%20Datasheet.pdf)] | Coarser, less linear, and varies with the rubber [est] |
| Durability | 10 million taps (1 kg at 4 Hz); 2.5 kg standing load for 24 h [chk] | "Routinely survive millions of actuation cycles"; a LowDrift ink exists for sustained loads [chk] | Silicone keypad contacts last 10⁵–3 × 10⁷ cycles depending on type; carbon pills > 5 million [chk, [N&H guide](https://www.nh-technology.de/download/Design-Guide-Silicone-Rubber-Keypad.pdf)] |
| Repair | **Swap one pad's FSR** | Replace the sheet | Re-glue a pill |
| Reuse in Big Energy | Yes | Yes: order two sheets | Yes |

**Alternatives checked and not chosen:**
- **Tekscan FlexiForce A201:** ±2.5 % repeatability, < 4.5 % hysteresis, ≥ 3 million actuations, but $155.08 per 8-pack (≈ $485 for 25) [chk, [Tekscan](https://www.tekscan.com/flexiforce-a201-sensor)].
- **Eeonyx pressure fabric** as a sheet over PCB fingers: the stock Adafruit piece is sold as a *stretch* sensor and is "No longer stocked" [chk, [Adafruit](https://www.adafruit.com/product/3669)]. Its datasheet gives no pressure figures [chk, [TDS](https://www.electrokit.com/upload/product/41016/41016316/LTT-SLPA+TDS.pdf)].
- **Velostat:** experimental (`keys.md` §2.3).

### 2.3 Feel: what the finger presses
- **Physics:** the force reaching the FSR equals the finger's force at steady state, whatever sits in between. Soft layers change the **feel and the strike's rise time**, not the pressure reading [calc].
- **Walnut tile (3–4 mm) on 1 mm silicone:** hard, ≈ 0.2–0.5 mm give [est]. It looks like the family's wood. The strike rises fast, so velocity reads crisply.
- **Cast silicone cap (3–5 mm, Shore A ≈ 30–50):** soft, ≈ 0.5–1 mm squish [est]. That's the LinnStrument and Seaboard feel, and it's easier to control pressure finely. Cast it in a 3D-printed mould from hobby silicone [est].
- **Felt top:** soft and HUSH-like, but felt creeps and damps the strike. Use it only over silicone, not alone [est].
- **Actuator puck:** a small rigid disc smaller than the FSR's active area, centred on it, makes a press anywhere on the pad read the same [est].
- **Stack:** PCB 1.6 + FSR 0.5 + puck or silicone 1–2 + top 3–4 ≈ **6–8 mm** [calc].

### 2.4 Velocity, pressure, calibration, outdoors
- **Velocity from force rise rate:** the FSR responds in < 3 µs [chk, Interlink]. A finger's strike rises over ≈ 1–30 ms, from a tap to a slow press [est].
  - Scanning 25 pads at 8–16 kHz each is 200–400 kS/s, within the RP2350's 500 kS/s ADC [chk, [Raspberry Pi](https://www.raspberrypi.com/documentation/microcontrollers/silicon.html)]. That gives 60–125 µs timing [calc].
  - Velocity = the slope between two low thresholds, decided ≈ 1 ms after the threshold, so T6 (≤ 5 ms) still passes at ≈ 3–4 ms total [calc]. Waiting for the peak would cost a few ms more.
  - QuNexus shows velocity from pressure pads ships [chk].
- **Pressure range:** 0.2–20 N [chk]. Map ≈ 0.3–8 N to full scale, as Big Energy's aftertouch did [plat]. 7-bit poly aftertouch is easy; LinnStrument and the fabric pads ship at about that [chk].
- **Calibration (automatic, nothing for you to do):**
  - zero is re-learned whenever a pad is untouched;
  - each pad's gain is learned from your hardest presses over time;
  - a note-on threshold sits above a resting finger's ≈ 0.1–0.3 N [est].
- **Temperature:** FSRs read more resistive as temperature rises [chk, Sensitronics FSR 101]. Interlink rates −40 to +85 °C [chk]. A pad in the sun shifts its zero, and auto-zero takes it out.
- **Moisture:** standard FSRs "are not fully sealed" and can be affected by humidity; custom ones can be made moisture-resistant [chk, Sensitronics]. Seal the pad-edge gap with the silicone layer.
- **Sunlight:** silicone keeps its properties in sun and weather [chk, N&H].

### 2.5 Readout
- **Circuit:** each pad's FSR goes from 3.3 V to a divider resistor to ground; the 25 divider nodes feed 2 × 16:1 analog muxes into 2 ADC pins on engine D's envelope RP2350B.
  - That's the same pins and chips as the Hall-sensor plan (`feasibility.md` §2.2).
  - The mux resistance doesn't matter, because it reads a high-impedance node [calc].
- **Power:** ≤ 0.33 mA per pad at full press, ≈ 0 idle, so ≤ 27 mW for all 25 [calc].
- **Daisy:** needs nothing new.
- **Wiring:** individual traces (one common, 25 signals) rather than a row-and-column matrix: no ghosting, simplest code.

---

## 3. What pads lose against moving keys
| | Moving keys | Pads |
|---|---|---|
| Travel and "a key under the finger" | Yes | No: a firm surface, ≈ 0.2–1 mm give |
| Velocity | From travel time | From force rise rate: shipping (QuNexus), crisp on wood or firm silicone [chk/est] |
| **Lift (release speed)** | Fine-grained, from travel time on the way up | **Coarse:** from how fast force falls in the last few ms. The resting force before lift varies, so normalise to it. The silicone's rebound and FSR hysteresis (≈ 10 % [chk]) blur it. Expect ≈ 3–5 dependable "ways to let go" [est] |
| Ending a note by easing off | Not possible (a key is up or down) | **Possible:** with per-pad pressure, the note's level can follow your finger as you ease off, so slow lifts become a fade you shape continuously |
| Resting fingers | Free until the key moves | Needs a threshold; light resting can't trigger notes, but very light playing becomes harder [est] |
| Durability outdoors | Moving parts collect grit | No moving parts; sealable |

**Job "shape how each note ends by how I lift off":** still met, in a different way. A quick lift gives a short tail. Easing off shapes the fade directly. A fine lift-speed number is lost.

---

## 4. The engine picture with pads
**Recommended engine: B built on D.** Every pad is a voice: analog-switch keyers, per-note velocity, **per-note pressure**, per-note release. Its hardware is engine D plus the pads.

| | Engine D with Hall keys (`feasibility.md`) | **Engine B on D, with FSR pads** |
|---|---|---|
| Engine chips | 12 | **12** (+ at most 1 buffer op-amp) |
| Pad or key sensing | 25 Hall sensors 0.58–0.97 W; shared strip $18–33 | 25 FSRs ≤ 0.03 W; **no strip** |
| **Total power** (low / mid / high) | 1.60 / 2.49 / 3.38 W | **1.03 / 1.73 / 2.44 W** [calc] |
| **Runtime, BOW base 11.1 Wh** | 2.6 / 3.6 / 5.6 h ✗ | **3.7 / 5.2 / 8.7 h**: meets T2 at moderate volume [calc] |
| Runtime, 22.2 Wh | 5.2 / 7.2 / 11.2 h | **7.4 / 10.4 / 17.5 h** [calc] |
| Keys / pads cost | keys $38–56 + strip $18–33 [plat] | P1 ≈ $350–420; P2 quote (≈ $200–600 [est]); P3 ≈ $30–60 |
| **One-unit total** | ≈ $400–685 | **P1 ≈ $695–1,015 · P2 ≈ $545–1,200 · P3 ≈ $375–655** [calc] |
| Board | key strip with Halls | pad PCB, same footprint; Hall supply gone. Base fit unchanged (57 % margin double-sided; 20 % with BOW's strands) |
| **Stack under the finger** | Choc key: ≈ 2.8 mm travel + head above the deck, switch and strip below (≈ 11–20 mm in all) [plat/est] | **≈ 6–8 mm** [calc] |

- **Case height:** BOW's closed height and HUSH's height are set by the knobs (≈ 8 mm above the deck) and the board, so pads don't make the cases thinner by themselves [est].
- **Under the pad zone (CATHEDRAL y ≈ 8–56):** the floating strip and its ≈ 8 mm air gap go away [plat]. That may leave room for thin cells, e.g. 4 × 60 × 36 × 7 mm, 2000 mAh ≈ 29.6 Wh [plat cell size, `eng/battery.md`; fit est]. Design must confirm the height.
- **BOW:** the "thins unless you lean" behaviour, per-note swell and per-note vibrato come back.
- **TIDE:** planted drift per note works with chords, not only one note at a time.
- **MIDI:** sends polyphonic aftertouch, and note-off velocity from lift.

---

## 5. Earlier trade-offs (`feasibility.md` §1.3): status
| # | Trade-off | Status | Now |
|---|---|---|---|
| 1 | Which engine | **Changes** | Engine B on D (keyers + per-pad pressure). A is weaker still. The C1 fallback is unchanged |
| 2 | Pressure: shared strip, per-half strips or a bought keyboard | **Superseded** | Per-pad pressure from the pads themselves |
| 3 | Platform key or magnetic switch | **Superseded** | Pads (`keys.md`'s S1–S3 decisions are also superseded) |
| 4 | BOW's battery (lid cell) | **Changes** | Base 11.1 Wh now meets T2 at moderate volume (5.2 h). Lid cell only for loud use. Cells under the pad zone if design confirms the space |
| 5 | TIDE's size against T4 | **Stands** | Pads don't change the depth much |
| 6 | Charging time with 22 Wh | **Stands** for any 22 Wh pack; BOW's 11.1 Wh base meets T3 |
| 7 | Passive radiator: slim parts or a thicker lid | **Stands** |
| 8 | BOW's strands | **Stands** |
| 9 | Targets beaten (tuning, silent-key hiss) | **Stands**; add **T2 margin** with pads |

**New decisions from this file:** P1 or P2 (§1, decision 1), pad top (2), accepting coarse lift (3), battery under the pads (4).

## 6. Open items
- A Sensitronics (and Interlink) quote for a 25-pad ThruMode sheet.
- The FSR 402 tail termination and connector part.
- The pad pitch and shape. Design's call; the 18 mm key pitch fits a 15 mm active area [calc].
- Cast-silicone hardness for the tops.
- Height under the pad zone in CATHEDRAL and HUSH.
