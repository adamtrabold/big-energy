# floss: playing it from a bought MIDI controller (rev 0, 2026-11-22)

Status: **rev 0**, by the engineer, for Adam. Published evidence only; nothing measured. No other eng file is edited.

Adam (verbatim):
- "It feels like the keyboard is the most expensive part. What if instead we made it Bluetooth MIDI or usb MIDI capable and just used a portable MIDI controller for the keyboard like the Korg nano key"
- "I'm getting curious now about stealing a keyboard from an existing controller"
- "Yeah research the options"

Standing rule: he measures nothing.

**Marks:** **[chk]** checked against the linked source · **[plat]** from Big Energy's eng records · **[calc]** my arithmetic · **[est]** my estimate.

---

## 1. Summary for Adam

**Recommendation: A, a separate controller over USB.**
- **Hardware:** floss gets one USB host socket that powers the controller.
- **Donor of choice:** the **K-Board C** (25 pads, velocity, poly aftertouch and MPE, USB-C bus-powered, $139, in stock).
- **Any class-compliant USB-MIDI keyboard works**, so the donor can be swapped.
- **Not recommended:** the transplant (no published teardowns, and the sensor is bonded to its board) and Bluetooth (slower than T6, fewer donors, an extra radio).

**Honest cost point:** after the silicone pass, the keyboard is no longer floss's most expensive part. A $139 controller costs about the same as the ≈ $135–155 silicone surface. The case, boards, battery and Daisy dominate either way.

| Route | One unit | Per-key pressure | Latency | One object? |
|---|---|---|---|---|
| **A. USB controller (K-Board C)** | **≈ $490–765** | Yes (poly aftertouch / MPE) | USB ≈ 1 ms | No: two pieces |
| A with nanoKEY2 | ≈ $400–665 | No (velocity only) | USB | No |
| Dock: the whole controller in a recess | ≈ $500–785 | Yes | USB | Yes, but floss becomes **≥ ≈ 335 mm wide** (T4 is ≈ 290) |
| C. Transplant (board out of its case) | ≈ A | Yes | USB | Yes. **Not recommended:** needs disassembly and measuring |
| B. Bluetooth MIDI | ≈ $730–1,000 | Seaboard Block M only | "< 10 ms under certain conditions" (T6 ≤ 5) | No |
| *For reference: silicone pads* (`silicone.md`) | ≈ $480–750 | Yes | Internal | Yes |

**Decisions for you:**
1. **Two pieces (A) or one (silicone pads, or a dock with a wider case)?**
2. **Donor:** K-Board C (pressure, $139) or nanoKEY2 (velocity only, cheaper)?
3. **If A:** floss becomes a keyless box. The designers re-form BOW and TIDE around that.
4. **Voices:** keep 25 voices (recommended; meets T1), or 12 to save one chip.

---

## 2. Donor candidates
| Controller | Keys | Pressure | Price, availability | Size, weight | Power |
|---|---|---|---|---|---|
| **K-Board C** (KMI / Muse Kinetics) | 25 pads | Velocity, **poly aftertouch, tilt, MPE** [chk, [MusicRadar](https://musicradar.com/news/keith-mcmillen-k-board-c)] | **$139, "In Stock!"** at Sweetwater [chk, [Sweetwater](https://www.sweetwater.com/store/detail/K-BoardCSn--muse-kinetics-k-board-c-smart-sensor-usb-mpe-midi-keyboard-controller-snow/reviews)]; $164 at Thomann. KMI-branded "until current inventory sells out" [chk, [Synthtopia](https://www.synthtopia.com/content/2024/09/17/following-founders-death-keith-mcmillen-instruments-rebranding-as-muse-kinetics/)] | **325 × 84 × 11 mm**, 0.34–0.4 kg [chk, [Thomann](https://thomannmusic.com/keith_mcmillen_k_board_c_snow.htm)] | USB-C bus-powered [chk]; draw not published (≤ 100 mA [est]) |
| QuNexus Galaxy (Muse Kinetics) | 25 pads | Velocity, poly aftertouch, MPE, CV | **$276, "Available in several months"** [chk, [Thomann](https://www.thomannmusic.com/muse_kinetics_qunexus_galaxy.htm)]. Continued under the new brand [chk, Synthtopia] | 325 × 84 × 11 mm, 0.31 kg [chk] | USB bus-powered [chk] |
| Korg nanoKEY2 | 25 keys | **Velocity only**; no aftertouch mentioned [chk, [Korg](https://www.korg.com/us/products/computergear/nanokey2/page_1.php)] | ≈ $50–60 [est] | 325 × 83 × 16 mm, 244 g [chk] | "Less than 100 mA" [chk] |
| ROLI Seaboard Block M | 24 keywaves | Strike, press, glide, slide, **lift**; 10 h battery, wireless [chk, [MusicRadar](https://www.musicradar.com/news/roli-launches-seaboard-block-m)] | $349.95 [chk] | Not published | Battery |
| Arturia MiniLab 3 | 25 slim keys | Velocity; **"Aftertouch: No"** [chk, [Thomann](https://www.thomann.de/be/arturia_minilab_3_black.htm)] | €90 [chk] | 355 × 220 × 50 mm, 1.5 kg [chk]: too big | USB |
| K-Board Pro 4 | 4 octaves | Poly aftertouch / MPE | Not checked | Too wide for portable | USB |
| Sensel Morph | Overlays | Pressure | **Discontinued in May 2022** (chip and ink shortages) [chk, [Synthtopia](https://synthtopia.com/?p=129666)] | — | — |
| MicroFreak's touch keyboard | 25 | Pressure | Not sold separately [est] | — | — |

**The 25-key minis are all ≈ 325 mm wide** [chk], wider than CATHEDRAL (286) and HUSH (290) [plat].

---

## 3. Three ways to connect
### A. Separate controller over USB (recommended)
- **Hardware:** floss adds a USB host socket (A or C), a 5 V current-limited load switch for the controller's power, and two wires to the Daisy. About $3–5 [est].
- **Single-source protection:** any class-compliant USB-MIDI controller plugs in.
- **Latency:** USB full-speed polls every 1 ms [est]. T6 (≤ 5 ms) holds.

### B. Bluetooth MIDI
- **Latency:** NIME 2019 measured BLE MIDI at "end-to-end … latencies of under 10ms under certain conditions" [chk, [NIME](https://nime.org/proc/nime2019_wang/)]. That misses T6.
- **Hardware:** floss would have to be the Bluetooth *central*, with an extra radio module (≈ $25–40 [est]).
- **Donors:** only battery-powered controllers qualify. The K-Board C has no Bluetooth: USB-C only [chk, Thomann].
- **Verdict:** not recommended.

### C. Transplant: the donor's board inside floss
- **No published teardowns:** I found none for the K-Board or QuNexus. Searches returned unrelated devices. So the board size, mounting and connector aren't published, and fitting it would mean Adam opening and measuring a donor, which breaks his rule.
- **The sensor is likely bonded:** KMI's patent bonds the piezoresistive sensor's traces to the PCB's I/O pads with conductive adhesive or pressure, held by heat-staked posts [chk, [US9753568](https://patents.google.com/patent/US9753568)]. If the K-Board is built that way, taking it apart may break the bond.
- **Verdict:** not recommended.

**Dock instead (one object, no measuring):** a recess in floss's top sized to the **published outer size** (325 × 84 × 11 mm, plus ≈ 1–2 mm clearance), a retaining lip and a short internal USB-C cable. The donor stays whole and swappable. **Cost:** floss becomes ≥ ≈ 335 mm wide, missing T4 by ≈ 45 mm [calc].

---

## 4. The Daisy Seed as USB host (checked in the source)
- **libDaisy supports USB host MIDI.**
  - The changelog says "Support for MIDI via USB Host has been added. (PR #611)".
  - It ships the ST `usbh_midi` class and an example, `examples/MIDI_USBH_Input` [chk, [libDaisy](https://github.com/electro-smith/libDaisy), commit 1289a00, 2026-11-03].
- **Port:** `USBHostHandle` runs on **USB_OTG_HS, pins PB14 / PB15 = Seed D29 / D30** [chk, `src/usbh/usbh_conf.c`, `src/daisy_seed.h`].
  - That fits Big Energy's pin plan, where D29 / D30 were kept spare [plat, `budget-variant.md` §v1.11.6].
  - The Seed's own USB port stays a device (`Periph::INTERNAL`) for MIDI to a computer and firmware updates [chk, `usb_midi.h`]. Running host and device at the same time is unverified [est].
- **VBUS:** libDaisy's `USBH_LL_DriverVBUS` is an empty stub [chk]. **floss must supply the controller's 5 V itself**, through a current-limited switch [est].
- **Parsing:** libDaisy parses poly key pressure, channel pressure and pitch bend [chk, `MidiEvent.h`]. MPE's per-note channels are floss's own firmware [est].
- **No USB hub support found** [est]: one controller at a time.
- **Fallback if host mode misbehaves:** a MAX3421E-class SPI host chip, or the companion RP2350 as host [est].

---

## 5. Firmware and engine with an external controller
- **Split and octave per half:** floss splits incoming notes at a fixed note number. OCTAVE L and R shift each side.
  - **Catch:** if you press the controller's own octave buttons, the split point moves with them. Keep the controller at its default octave and use floss's knobs.
- **MIDI split out:** floss re-sends each half on channel 1 or 2, as planned.
- **MPE:** each note arrives on its own channel with its own pressure and pitch bend (K-Board tilt). floss maps them to that voice, which gives per-note pressure (engine B).
- **Lift:** release velocity depends on the donor: only the Seaboard lists "Lift" [chk].
- **Engine:** voices now follow MIDI notes, so the "per-key" engine becomes a **25-voice allocated engine with identical hardware**: 25 tone generators and keyers, assigned oldest-first.
  - It fits a 25-pad controller exactly (T1).
  - **Option:** 12 voices on one RP2350B (12 tones on PIO + 12 envelopes on PWM) saves ≈ $12–15 and ≈ 0.15–0.25 W, but caps notes at 12 (TIDE's HOLD stacking) [calc/est].
- **The companion RP2350B no longer reads sensors.** The controller does that.

---

## 6. Cost, power, case
**Cost** [calc]: common ≈ $370–645, less keys and strip ($56–89) [plat/est], + engine D $31–41 + host port ≈ $5 + controller:
- K-Board C ($139–164): ≈ **$490–765**;
- nanoKEY2 (≈ $50–60 est): ≈ $400–665;
- dock: + ≈ $10–20;
- Bluetooth: + radio ≈ $25–40 and a Seaboard Block M ($349.95).

A keyless case may cost a little less [est].

**Power:** engine B on D without pad sensing (≈ 1.0–2.4 W, `pads.md`), + the controller's ≈ 0.25–0.5 W (nanoKEY2 < 100 mA [chk]; K-Board not published [est]) = **≈ 1.28 / 2.11 / 2.94 W** [calc].

**Runtime** [calc, Big Energy's method]:
| Pack | Worst / mid / best |
|---|---|
| 11.1 Wh | 3.0 / 4.3 / 7.0 h |
| 22.2 Wh | 6.0 / 8.5 / 14.1 h |

A keyless floss box has room for the 22 Wh pack [est].

**Case constraints for the designers:**
- **A:** floss holds no keys. The panel (≈ 16 controls) plus speaker box and battery set the size. Carry the controller beside it: 325 × 84 × 11 mm, ≈ 0.35 kg [chk].
- **Dock:** recess ≥ 327 × 86 × 12 mm [calc]; floss ≥ ≈ 335 mm wide.
- **Host socket:** on the rear wall, with a cable path.

---

## 7. Trade-offs for Adam
1. **One object or two:** A is two pieces and one cable; silicone pads or a dock are one object.
2. **Family look:** the controller's look isn't floss's (colours vary: the K-Board C comes in five [chk]).
3. **Single-source risk:**
   - The K-Board C stays KMI-branded only "until current inventory sells out" [chk].
   - The QuNexus is months out [chk].
   - Mitigation: design around standard USB-MIDI, so any class-compliant controller works.
4. **Feel:** K-Board and QuNexus pads are firm sensor pads, not floss's own silicone.
5. **Cost:** about the same as the silicone pads. The saving Adam hoped for is small, because the keyboard is no longer the big cost.
6. **Keys you can swap:** A lets you play floss from any keyboard later, including a full-size one at home.
