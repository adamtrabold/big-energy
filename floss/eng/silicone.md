# floss: a soft silicone playing surface, costed (rev 0, 2026-11-22)

Status: **rev 0**, by the engineer, for Adam. Desk research and arithmetic only. It doesn't edit the other eng files. It replaces `pads.md`'s cost picture: Adam called the $350–420 Interlink route "egregious compared to the market", and he's right.

Adam (verbatim): "The cost of pads seems egregious compared to the market" / "I don't feel like the layered boards would feel very good" / "I like the soft silicone idea if we're not going button or classic keys".

**Marks:** **[chk]** checked against the linked source · **[plat]** from Big Energy's eng records · **[calc]** my arithmetic · **[est]** my estimate.

---

## 1. Summary for Adam

**Recommendation:** one cast silicone mat with 25 raised pads, over **25 generic thin-film force sensors** (DFRobot RP series, ≈ $3 each) on a small pad board.
- **Cost:** ≈ **$75 of sensors**, ≈ $40 of silicone.
- **What you get:** velocity and per-pad pressure (engine B), with a datasheet, sold by mainstream distributors.
- **Repair:** any pad's sensor can be swapped.
- **Cheaper fallback:** conductive rubber over gold PCB pads (≈ $30–60). It's how pressure-sensitive game-controller buttons work, but its pressure is coarser.

| Option | Sensing + silicone, 25 pads | Velocity | Pressure | Life |
|---|---|---|---|---|
| **Generic thin-film FSR** (recommended) | **≈ $115–130** | Good* | Good | > 1 M presses |
| Conductive rubber on PCB pads | **≈ $30–60** | Good | Coarse | > 5 M (carbon pills) |
| Capacitive under thin silicone | ≈ $20–55 | Good | A proxy (touch area) | No wear |
| Interlink FSRs (`pads.md` P1) | ≈ $340–350 | Good | Good | 10 M |
| Custom FSR sheet | ≈ $300–800 (quote) | Good | Good | Millions |
| *Baseline:* slim keys or buttons | ≈ $20–60, or a $199 controller to gut | Yes | **None per key** | — |

*The generic sensor's datasheet lists a "< 10 ms" response. FSRs are physically fast, but check one sensor against velocity before buying 25.

**Market check:**
- An Akai MPD218 (16 velocity and pressure pads) sells for **$79** whole [chk].
- A Novation Launchpad X (64 pads with poly aftertouch) sells for **$229.99** [chk].
- **Target: sensing + silicone ≤ ≈ $100.** Conductive rubber and capacitive hit it; generic FSRs are just over; Interlink misses by 3×.

**One-unit total with the recommendation:** ≈ **$480–750** (it was ≈ $695–1,015 with Interlink pads) [calc].

**Decisions for you:**
1. **Generic FSRs (recommended) or conductive rubber** (cheapest, coarser)?
2. **Silicone hardness:** soft (Shore 10A, squishy) or firmer (≈ 30A, crisper strikes)? Recommendation: ≈ 20–30A.
3. **One sealed mat or 25 separate caps?** Recommendation: one mat. It keeps water and grit out in the park.
4. **Baseline check:** pads over keys or buttons, which can't give per-key pressure.

---

## 2. Options in detail

### 2.1 Generic thin-film FSRs under silicone (recommended)
- **Part:** DFRobot RP series.
  - RP-C7.6: **£2.41 ex VAT** at CPC Farnell; 30 g–1.5 kg; "> 1 million" uses; drift < 5 % at 1 kg over 24 h; response "< 10 ms"; −40 to +85 °C; 0.3 mm. That page's size line is garbled [chk, [CPC](https://cpc.farnell.com/dfrobot/sen0297/rp-c7-6-st-thin-film-pressure/dp/SC21077)].
  - RP-C18.3 (18.3 mm): $6.90; 20 g–6 kg; hysteresis +10 %; > 1 million actuations [chk, [DFRobot](https://dfrobot.com/product-1846.html)].
- **Against Interlink:** Interlink's 400 series is rated for 10 million taps, ±2 % single-part repeatability and < 3 µs rise time [chk, [datasheet](https://www.teachengineering.org/content/uconn_/activities/uconn-2662-contractions-calculations-force-resistance-activity/uconn-2662-contractions-calculations-FSR400series-datasheet.pdf)], at **$11.92 each in 25s** [chk, [Pololu](https://www.pololu.com/product/2727)]. Generic film is ≈ ¼ the price with ≈ 1/10 the rated life, and repeatability isn't stated.
  - **Life in practice:** the busiest pad might reach 1 million presses in ≈ 1–3 years of daily heavy playing [est]. It's a $3 part.
- **Proven:** FSRs under pads and keys ship in Fatar poly-aftertouch keybeds [chk, [Native Instruments](https://www.native-instruments.com/blogs/blog/polyphonic-aftertouch)] and LinnStrument [chk, [Roger Linn](https://rogerlinndesign.com/support/how-linnstruments-sensor-works)]. The generic film is the same principle from a lower-cost maker.
- **Cost:** 25 × ≈ $3 = **≈ $75**; buy 30 for spares. Silicone ≈ $40, pad PCB ≈ $20–40 → **≈ $135–155** with the board [calc/est].
- **Build:**
  1. Order a pad PCB with 25 lands, divider resistors and a header per pad (fab-assembled SMD).
  2. Stick each film on its land and plug its tail in.
  3. Glue a small rigid puck on each sensor's centre.
  4. Lay the cast mat on top; the deck plate holds it at the edges.
- **Velocity:** from how fast force rises, scanned at 8–16 kHz per pad. That's within the RP2350's ADC rate [chk, [Raspberry Pi](https://www.raspberrypi.com/documentation/microcontrollers/silicon.html)] and keeps key-to-sound within 5 ms (T6) [calc, `pads.md` §2.4]. Risk: the "< 10 ms" response spec. **Test one sensor before buying 25** (an electronics bench check, not a key experiment).
- **Ageing:** < 5 % drift per day under load [chk]. Auto-zero whenever a pad is untouched, and per-pad gain learning, absorb it [est].

### 2.2 Conductive rubber over gold PCB pads (cheapest)
- **How it works:** a conductive pill under each silicone pad presses on interdigitated gold fingers on the PCB. Harder pressing means more contact area and lower resistance.
- **Proven:** the DualShock 2's pressure-sensitive buttons work this way: harder presses bring more of the conductive disk into contact [chk, [iFixit](https://www.ifixit.com/Teardown/DualShock+2+Teardown+How+It+Works/107082)].
  - Sensitronics' "ShuntMode" FSR is the same geometry: a semiconductive layer shunting interdigitated traces, good for "moderate-resolution force measurement" [chk, [Sensitronics](https://sensitronics.com/faq.html)].
  - Silicone keypad carbon pills last > 5 million cycles [chk, [N&H guide](https://www.nh-technology.de/download/Design-Guide-Silicone-Rubber-Keypad.pdf)].
- **Cost:** the fingers are part of the PCB (free); pills ≈ $5–15; silicone ≈ $40 → **≈ $30–60** [est].
- **Quality:** pressure is monotonic but less linear, and pill-to-pill spread is larger [est]. Fine for swell and vibrato; coarser for fine control. How stable it stays over years is unknown.
- **Build:** cast the mat with a pill set into each pad's underside (glue in after curing). No separate sensors to place.

### 2.3 Capacitive under thin silicone (no wear at all)
- **How it works:** copper pads on the PCB under 1–2 mm of silicone. A harder press flattens the finger and squeezes the silicone, so capacitance rises.
- **Proven:**
  - The MicroFreak senses "both the firmness and area" of skin contact [chk, [Sound on Sound](https://www.soundonsound.com/reviews/arturia-microfreak)].
  - The Soundplane's "continuous capacitive sensing" gives pressure at 12 bits and ≈ 1 kHz [chk, [CDM](https://cdm.link/expressive-soundplane-touch-instrument-decibel-video-preorder-tour-images/)].
- **Cost:** PCB + RP2350 PIO sensing or touch chips ≈ $10–15 + silicone [est].
- **Weaknesses:** it's a proxy, not force: a gloved or wet finger reads differently. The MicroFreak reviewer also kept firing notes from resting fingers [chk]. Rain upsets it [est].
- **Strength:** nothing touches, so nothing wears. That's the only option with no ageing in the sensor.

### 2.4 Custom FSR sheet
- **Makers:**
  - Sensitronics: no minimum for custom work, prototypes in 2–4 weeks [chk, [FAQ](https://sensitronics.com/faq.html)];
  - Interlink custom sensor solutions (MOQ and tooling not stated) [chk, [Interlink](https://interlinkelectronics.com/custom-sensor-solutions)];
  - Ohmite offers custom sensors [chk, [Ohmite datasheet](https://www.mouser.in/ds/2/303/ohmite_02192018_res_fsr-1288259.pdf)].
- **Price:** ≈ $300–800 for a prototype [est]; get a quote. Best quality, easiest assembly, but it misses the cost target.

### 2.5 The silicone itself
- **Process:** cast one mat in a 3D-printed mould (PLA or PETG with mould release).
- **Material:** Smooth-On Dragon Skin 10 FAST is Shore 10A, $37.50 for a 2 lb trial unit, with 8 minutes pot life and a 75 minute cure [chk, [Smooth-On](https://shop.smooth-on.com/dragon-skin-10-fast)].
- **Quantity:** 25 pads at ≈ 16 × 16 × 4 mm is ≈ 25 cm³, ≈ 27 g [calc]. One trial unit casts many mats.
- **Hardness:** 10A is very soft and squishy. ≈ 20–30A (a firmer grade, similar price [est]) gives crisper strikes.
- **Ageing:** silicone takes an 11–22 % permanent set in the standard accelerated test, and keeps its properties in sun and weather [chk, N&H]. The set shifts each pad's resting preload, which auto-zero removes.
- **Outdoors:** a single mat seals the board from rain and grit.

### 2.6 Readout (all options)
- **Resistive options (2.1, 2.2):** each pad's divider feeds 2 × 16:1 analog muxes into 2 ADC pins on engine D's envelope RP2350B. These are the same pins as `pads.md` §2.5, ≤ 27 mW [calc].
- **Capacitive option (2.3):** RP2350 PIO charge timing or 2–3 touch chips [est].
- **Daisy:** needs nothing new.

---

## 3. Baseline: classic keys or buttons
| | Cost | Velocity | Per-key pressure | Note |
|---|---|---|---|---|
| Bought mini keybed | None sold bare to individuals [plat, `eng/key-sourcing.md`] | — | — | Gutting a controller (e.g. Arturia KeyStep 37: slim keys with velocity and aftertouch, **$199 on sale** [chk, [Adorama](https://www.adorama.com/arturia-keystep-37-midi-keyboard-controller-sequencer/p/ar430221)]; type of aftertouch not stated) was ruled out for Big Energy [plat] |
| Switch keys or buttons (Choc, or Gateron magnetic + Hall) | ≈ $21–56 [plat] | Yes (Hall) | **No.** A shared strip adds channel pressure (+$18–33 [plat]) | Gateron magnetic: $55.95 per pack [chk, [NuPhy](https://nuphy.com/products/gateron-low-profile-magnetic-jade-switches)] |

**What keys or buttons lose:** per-key pressure, so engine B falls back to C/D (`feasibility.md`), and BOW's lean-to-sustain and TIDE's planted drift go per-instrument.

---

## 4. One-unit total with the recommendation
- **Calculation:** common parts ≈ $370–645, less keys and strip ($56–89) [plat/est], + engine D $31–41 + generic-FSR silicone surface $135–155 = **≈ $480–750** [calc].
- **Conductive-rubber fallback:** ≈ $395–700 [calc].
- **Power and runtime:** same as `pads.md` (BOW base pack 3.7 / 5.2 / 8.7 h).
- **Engine:** B on D, 12 chips.
- **Height:** pad stack ≈ 6–8 mm [calc].
