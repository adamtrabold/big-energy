# Keys from first principles (rev 0, 2026-11-22)

Status: **rev 0**, by the engineer, for Adam. Desk research and arithmetic only; nothing was built.

Adam's brief (verbatim, 2026-11-22): "Let's talk keys. Make sure we're not assuming things. All a key has to be is something we can press that can record various pressure levels. We had ideas on big energy but not finals. We can reuse anything we do here there. Look at first principle approaches."

So this file starts from zero. It doesn't assume keyswitches, Hall sensors or Big Energy's current key. **A key is something you press that records how you press it:**
- the **strike**, which gives velocity;
- **continuous pressure** while it's held;
- ideally the **lift speed** too, since the floss concepts use it for each note's tail.

Everything here applies to Big Energy's 25 keys as well.

**Marks:** **[chk]** checked against the linked source this session · **[plat]** from Big Energy's eng records · **[calc]** my arithmetic · **[est]** my estimate. **"Proven"** means the sensing principle ships in products that work reliably, even if we build the key ourselves. **"Experimental"** means I found no shipping product relying on it.

---

## 1. Summary for Adam

### 1.1 The principles compared
| Principle | Velocity | Pressure | Lift speed | Proven in | Key travel and feel | Sensing parts for 25 keys | Outdoors | Verdict |
|---|---|---|---|---|---|---|---|---|
| **Displacement against a steel spring, read by Hall sensor** | Yes, from position over time | **Yes: force = spring rate × extra travel** | Yes | Hall position: millions of Hall-effect keyboards. Pressure from key depth: Osmose (shipping) | A real key with a short, firm second stage (≈ 1.5–2 mm) | ≈ $20–40 + springs [est] | **Best:** sealed, immune to light and damp | **Proven principle; we design the key** |
| Same, read by optical (infrared) reflectance | Yes | Yes | Yes | Razer analog optical switches; optical piano scanning strips | Same | ≈ $25–40 [est]; infrared LEDs draw power unless pulsed | Sunlight can blind it unless shielded | Proven principle |
| Same, read by inductive sensing | Yes | Yes | Yes | Only a proof-of-concept key module (Azoteq) | Same | Unknown | Good | **Experimental** |
| **Force-sensing resistor (FSR) under a moving key** | Not well alone (needs a second sensor, or the force's rise rate) | **Yes, at nearly zero extra travel** | Needs a second sensor | Fatar keybeds with poly aftertouch (an FSR matrix), Akai-type pads, LinnStrument | Normal key; a firm bottom with no give | ≈ $150–200 bought, or ≈ $20–60 as PCB pads + pressure film [est] | Good (−40 to +85 °C rated) | **Proven** |
| FSR pad surface (no moving key) | Yes (force rise rate) | Yes | Weak | LinnStrument (FSR sheet under 2 mm silicone), QuNexus | No travel: a firm pad | ≈ $20–60 [est] | Good if sealed | Proven, but it's a pad, not a key |
| Velostat or Linqstat sheet | Poor | Poor (hysteresis, creep) | Poor | Lab and DIY only | — | Pennies | Fair | **Experimental** |
| Capacitive contact area | Yes | **A proxy:** how much skin touches, not force | Yes | Arturia MicroFreak | No travel; false triggers from resting fingers | ≈ $10–20 [est] | **Poor:** rain and sweat | Proven, but not true pressure |
| Capacitive displacement (a surface deforming over electrodes) | Yes | Yes | Yes | Madrona Labs Soundplane | Small give | PCB + analog front end [est] | Fair | Proven, but complex to make |
| Piezo | **Yes** | **No:** it can't hold a steady pressure | No | Electronic drum pads | Pad | Cheap | Good | Proven for strike only |
| Strain gauge or load cell | Yes (needs a fast ADC) | **Yes, very repeatable** | Weak | Neotone digital handpan; every weighing scale | Nearly no travel | ≈ $75–250 + amplifiers [est] | Good | Proven, but bulky and costly per key |
| Silicone with an embedded sensor | Yes | Yes | Yes | ROLI Seaboard, Embodme Erae, LinnStrument | Soft, squishy | Needs a moulded surface (tooling) | Collects grit | Proven, but needs custom moulding |

### 1.2 Shortlist
| | **S1. Spring key, read by Hall sensor** (recommended) | S2. Moving key + FSR at the bottom | S3. Pressure-pad surface |
|---|---|---|---|
| How it works | A pivoted key on a light return spring. At the bottom of its main travel it meets a **stiff steel spring**, which gives ≈ 1.5–2 mm more for 0–8 N. A magnet in the key over a Hall sensor reads position continuously: strike, depth (= pressure) and lift all come from one sensor | A normal key. At the bottom it presses an FSR through a thin silicone pad. Velocity comes from a position sensor (Hall or optical) or the FSR's rise rate | Silicone pads over an FSR sheet or PCB pads: LinnStrument- or QuNexus-style |
| Feel | A real key with a short, firm "give" you lean into. Osmose has the same idea, with longer travel | Like a normal keyboard's aftertouch: firm bottom, no give | No travel: a firm pad |
| Pressure quality | **Set by a steel spring:** no creep, negligible hysteresis. Auto-zero at rest and at bottom-out. ≈ 100–200 usable levels [calc/est] | FSR: ±2 % on one part, ±6 % part to part, ≈ 10 % hysteresis, drift < 5 % per decade of time [chk]. Needs per-key auto-calibration | Same as S2 |
| Sensors per key | **1** | 2 (position + force) | 1 |
| Sensing cost, 25 keys | ≈ $20–40 + springs ≈ $10–20 [est] | ≈ $40–240 [est] | ≈ $20–60 [est] |
| Stack height | ≈ 18–20 mm [est] | ≈ 16–18 mm [est] | ≈ 5 mm [est] |
| Build effort | **We design the key mechanism** (printed or wooden levers, bought springs, a pivot rod). A prototype key is normal engineering, not a test by you | Key mechanism + 25 FSRs and their pads | Least: a PCB, a sheet, a silicone mat or caps |
| Outdoors (park) | Best | Good | Good if sealed |
| Reuse in Big Energy | Yes: one key serves both, and makes Big Energy's shared strip unnecessary | Yes | Yes, but Big Energy loses moving keys |

**Recommendation: S1.** It's the only shortlisted approach that gives **velocity, per-key pressure and lift speed from one cheap, sealed sensor per key**. It measures force with the most repeatable force element there is: a steel spring, which is what a load cell is inside. The principle is proven: continuous key-position sensing ships in Hall-effect and optical keyboards, and pressure from extra key depth ships in the Osmose. What isn't bought off the shelf is the key mechanism itself, which we design and prototype. **If you want a key that feels like a conventional keyboard (no give), choose S2.** S3 is the robust, thin, cheap option if you'd accept pads instead of keys.

### 1.3 Decisions for you
1. **Keys that move, or pads?** Moving keys (S1, S2) or a pressure surface (S3). Recommendation: moving keys.
2. **How should pressure feel?** A short firm give you lean into (S1, ≈ 1.5–2 mm), or a hard bottom with no give (S2). This is a feel choice, and S1 is the simpler, more reliable sensor. Recommendation: S1.
3. **Are you OK with us designing the key mechanism?** Every approach that gives per-key pressure on moving keys needs it, because no bought keyswitch or 25-key keybed offers pressure (`feasibility.md` §3). The sensing principle is proven; the mechanism is ours. Recommendation: yes. It's the same lever-and-spring work for floss and Big Energy.
4. **Share it with Big Energy?** Recommendation: yes. One key design, built twice. Big Energy's floating pressure strip and its glued-magnet Choc key would both be retired.

### 1.4 What this changes in `feasibility.md` (not rewritten here)
- **Per-key pressure becomes possible with proven principles** once the key is our own design. `feasibility.md` §1.2 and §3.2 assumed bought keyswitches; that verdict stands for keyswitches only.
- **Engine B is unblocked.** With S1 it needs **no new electronics** beyond engine D: the same Hall sensors and envelope microcontroller already read position. With S2 it adds 25 FSRs on two more mux channels.
- **BOW's "thinning unless you lean" comes back**, and so do per-note swell, vibrato and TIDE's per-note planted drift. MIDI sends polyphonic aftertouch.
- **Trade-off 2** there (shared strip versus per-half strips) and **trade-off 3** (platform key versus magnetic switch) are superseded by decision 3 here, if Adam chooses S1 or S2.
- **Power:** S1 is unchanged (the same 25 Hall sensors, 0.58–0.97 W). S2 adds ≈ 0.03 W for the FSRs.
- **Height:** S1's ≈ 18–20 mm key stack is taller than the Choc-based CATHEDRAL and HUSH keys. Body heights need checking by design.

---

## 2. The principles in detail

### 2.1 Displacement against a spring (Hall, optical, inductive)
**Physics:** force = spring rate × compression. A key with a light main spring and a **stiff second spring** at the bottom becomes a force gauge in its last millimetres, read by whatever measures position.

**Proof it works:**
- **Pressure from key depth:** the Osmose has ≈ 9 mm to a first point of resistance, then "at least as far again" of pressure travel on white keys [chk, [Sound on Sound](https://www.soundonsound.com/reviews/expressive-e-osmose?amp)]. Its sensor type isn't published.
- **Continuous position sensing:** Azoteq's inductive key module derives poly aftertouch from "the bottom region of the keystroke … starting at a programmable depth" [chk, [MIDI Association](https://midi.org/innovation-award/azoteq-full-motion-key-position-sensor-module-proof-of-concept-demonstrator)]. It is only a proof-of-concept.
- **Hall position sensing** ships in low-profile magnetic keyboard switches, rated for 100 million presses [chk, [NuPhy/Gateron](https://nuphy.com/products/gateron-low-profile-magnetic-jade-switches)].
- **Optical position sensing:** Razer's analog switches measure "the amount of infra-red light beamed to the phototransistor", with the stem acting as a shutter, and are factory-calibrated [chk, [Razer](https://www.razer.com/newsroom/featured/analog-optical-vs-hall-effect-switches)].
- **Optical on pianos:** PNOScan and the Moog PianoBar have captured piano playing optically "for decades". A research system using a 2.5 mm Vishay reflective sensor resolves ≈ 100 position levels over ≈ 1 cm of travel [chk, [PHOTON paper, NIME 2026](https://pure.uva.nl/ws/files/331830287/nime2026_85.pdf)].

**S1 numbers:**
- **Main travel and spring:** ≈ 4 mm at ≈ 0.5–0.8 N [est].
- **Second stage:** a steel leaf or compression spring of ≈ 5 N/mm gives 0–8 N over 1.5 mm [calc]. Big Energy's aftertouch used 8 N as full scale [plat].
- **Sensor:** SS49E, 1.4 mV/gauss typ, 6–10 mA, 3 µs response [chk, [Honeywell](https://www.farnell.com/datasheets/1676929.pdf)].
- **Pressure resolution:** with an assumed 150–300 gauss/mm field gradient near the bottom [est], 1.5 mm gives ≈ 0.3–0.6 V. On a 12-bit, 3.3 V ADC (0.8 mV per step) that's ≈ 400–800 steps, or ≈ 100–200 distinguishable levels after noise [calc/est]. MIDI poly aftertouch carries 128.
- **Velocity:** 25 keys at 8 kHz each = 200 kS/s, within the RP2350's 500 kS/s ADC [chk, [Raspberry Pi](https://www.raspberrypi.com/documentation/microcontrollers/silicon.html)]. That's 0.125 ms timing over a strike of ≈ 5–30 ms [est]. Lift speed comes the same way.
- **Calibration:** automatic. The firmware learns each key's rest and bottom-of-main-travel readings, which removes magnet-to-magnet variation (Razer's main criticism of Hall switches [chk, above]) and slow temperature drift [est].

**Hall against optical against inductive:**
- **Hall:** sealed and light-proof, so it's the outdoor pick. 25 × 6–10 mA is the biggest power item on floss [chk/calc].
- **Optical:** cheap sensors, but an infrared LED per key draws ≈ 5–20 mA unless it's pulsed during the scan [est], and direct sun can swamp a reflective sensor unless it's shielded [est].
- **Inductive:** no shipping key product found. Experimental.

### 2.2 Force-sensing resistors
**Proof:**
- Fatar added "an FSR matrix to allow the detection of the key pressure independently" for NI's poly-aftertouch keyboards [chk, [Native Instruments](https://www.native-instruments.com/blogs/blog/polyphonic-aftertouch)].
- LinnStrument uses two printed plastic sheets with FSR material, separated by 2 mm spacers, under a 2 mm silicone top, read through analog switches into an ADC [chk, [Roger Linn Design](https://rogerlinndesign.com/support/how-linnstruments-sensor-works)].
- A replacement kit uses carbon dots over gold interdigitated PCB pads under foam [chk, [kit instructions](https://cdn.shopify.com/s/files/1/1883/9389/files/t8_aftertouch_replacement_instructions.pdf)]. That's the "PCB + film" route, buildable with an ENIG PCB.

**Specs (Interlink FSR 400 series)** [chk, [datasheet](https://www.teachengineering.org/content/uconn_/activities/uconn-2662-contractions-calculations-force-resistance-activity/uconn-2662-contractions-calculations-FSR400series-datasheet.pdf)]:
- 0.2–20 N range;
- ±2 % repeatability on one part, ±6 % part to part;
- ≈ 10 % hysteresis;
- drift < 5 % per decade of time under load;
- 10 million taps;
- −40 to +85 °C;
- 0.3 mm thick.

**Velocity:** pad controllers take it from how fast the force rises. A keyboard (Fatar) pairs the FSR with separate velocity sensors ("multi-sensors board" [chk, same NI page]).

**Readout:** a divider or op-amp per key into the same muxes; ≈ 1 mW each [est].

### 2.3 Velostat or Linqstat (carbon-loaded film)
A lab study found "significant hysteresis", creep under a sustained 2.88 N load, no full recovery after long loading, conditioning cycles needed, and crosstalk up to ≈ 3 mm [chk, [Sensors/PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7761878)]. **Experimental:** fine for a gesture prototype, not for a reliable key.

### 2.4 Capacitive
- **Contact area:** the MicroFreak's "keys" are a PCB matrix that senses "both the firmness and area" of skin contact. The reviewer kept firing notes by accident from resting fingers [chk, [Sound on Sound](https://www.soundonsound.com/reviews/arturia-microfreak)]. This measures how much finger touches, not force, and wet fingers or rain upset capacitive sensing [est].
- **Displacement:** the Soundplane uses "continuous capacitive sensing", giving x, y and pressure at 12 bits and ≈ 1,000 samples a second [chk, [CDM](https://cdm.link/expressive-soundplane-touch-instrument-decibel-video-preorder-tour-images/)]. Proven, but its analog front end is a project in itself [est].

### 2.5 Piezo
A piezo element makes charge when force **changes**, so it reads a strike well but can't hold a steady pressure [est, physics]. Drum pads detect dynamics and hit position this way [chk, [Roland](https://www.roland.com/US/promos/innovation_of_v-drums/sensor/)]. Strike only, so it doesn't answer the brief alone.

### 2.6 Strain gauges and load cells
- The Neotone digital handpan uses custom load cells to "accurately measure striking force, pressure and position", chosen as "reliable, affordable" and built for millions of impacts [chk, [FHI/Zemic](https://fhi.nl/en/news/waarom-soundventure-ltd-rekstroken-van-zemic-gebruikt-voor-hun-digitale-handpan/)].
- **Per key:** a bridge, an amplifier and a fast ADC. Common cheap load-cell ADCs run at only 10–80 samples a second, too slow for velocity [est].
- **Power:** 350 Ω bridges at 3.3 V draw ≈ 9 mA each [calc] unless they're switched.
- **Size:** bar load cells are ≈ 12 mm tall [est].
- Proven and very repeatable, but the most costly and bulky per key.

### 2.7 Silicone with an embedded sensor
- **ROLI Seaboard:** a "sensor-embedded flexible rubber surface" giving strike and press [chk, [Wikipedia](https://en.wikipedia.org/wiki/ROLI_Seaboard)]. The RISE's silicone is "a bit firmer" than the Grand's [chk, [Sound on Sound](https://www.soundonsound.com/reviews/roli-seaboard-rise)].
- **Erae Touch:** a silicone surface that "yields and generates a Z-pressure signal" [chk, [Juno](https://www.juno.co.uk/junodaily/2023/06/16/embodme-erae-touch-review)].
- Proven, but it means a moulded surface (tooling) and a soft feel.

### 2.8 A note on the old platform ideas
- **Choc V2 or Gateron magnetic switches** read travel and then bottom out hard on their housings. **They can't give pressure** unless the whole switch floats on a sensor (Big Energy's strip idea, which gives one value for all keys) [plat].
- S1 gives the same sensor (Hall) a spring to measure against.

---

## 3. Electronics for 25 keys (S1)
- **Sensors:** 25 SS49E (or SMD equivalents) on a key PCB, through 2 × 16:1 analog muxes into 2 ADC pins of the companion RP2350B (engine D's envelope chip), scanned at 8 kHz per key [calc].
- **One chip does it all:** velocity, pressure and lift come from the same samples, so no extra pins over `feasibility.md`'s engine D.
- **Power:** a 3.3 V buck for the sensors (0.58–0.97 W) [calc, `feasibility.md` §7].
- **Daisy:** needs nothing new. It receives note, velocity, pressure and lift messages over the existing serial link.

## 4. Open items
- Field gradient and magnet placement for S1 (simulate, then one prototype key).
- Spring part numbers: leaf or compression, ≈ 5 N/mm.
- Lever material and pivot.
- Key height in CATHEDRAL and HUSH.
- Osmose's sensor type is unpublished. The Continuum's sensors weren't confirmed in what I read.
