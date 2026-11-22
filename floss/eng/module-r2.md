# floss sound module: engineering rev 2 (2026-11-22)

Status: **rev 2**, by the engineer who took over from `module.md` (rev 0, unchanged). It answers the designers' and director's questions from `design/jam-module.md` turns 2–3, and the owner's two process rules:
- "I don’t want to measure anything. I’m truly to see how far agents alone can get me"
- "Also note you could model the speaker setup to test virtually"

Everything here rests on published data (datasheets, distributor listings, the Type-C spec as quoted by vendors) plus a simulation written for this note. Nothing was measured. Engineering supplies numbers and constraints; looks and layout stay with the designers, and decisions stay with Adam.

**Marks:** **[chk]** checked against the linked source · **[calc]** my arithmetic or the simulation · **[est]** my estimate · **[plat]** from Big Energy or `module.md` records · **UNVERIFIED** = no published source found; designed around.

---

## 0. Summary

**Speaker (task 1).**
- **No slim speaker can be designed from published data alone.** Every driver of about 50 mm that I found under ≈ 20 mm deep publishes only Fs: no Qts, Vas or BL. That includes the CDS-5076 used before and the Visaton K 50 FL / FLS. So `module.md`'s ≈ 20 mm-deep radiator box really did need a measurement.
- **The thinnest driver with a full published parameter set is the Tectonic TEBM28C10-4B.** It's 55 mm across and 24.00 mm deep, $25, with 135 in stock at DigiKey [chk]. That sets the body at **≈ 32 mm** without knobs (≈ 40 with knobs) [calc/est], about 7–9 mm thicker than `module.md`'s 23–25.
  - The DMA58 path is ≈ 40 mm.
  - The published matched pair (DMA58-4 + DMA58-PR) is ≈ 46 mm.
- **A virtual model replaces the hand calculation** (`eng/speaker-sim/`). It's a lumped-parameter model built from the published parameters, and it covers sealed, ported and passive-radiator boxes for three drivers and three radiators in each module shape. Each candidate is run 300 times with the parameters varied across their tolerances (see §1.5).
- **Results, TEBM28C10-4B, 1 W at 1 m** [calc]:

  | Box | Volume | −3 dB | Level at 100 Hz vs mid-band |
  |---|---|---|---|
  | Sealed | any volume ≥ ≈ 80 cm³ | ≈ 255 Hz | −12 dB |
  | Ported (Ø 12 mm port) | 217 cm³ (RAIL) | ≈ 115 Hz | −6 dB |
  | Ported | 410 cm³ (SLAB) | ≈ 103 Hz | −3 dB |
  | Best slim passive radiator | | ≈ 236–239 Hz | −10 to −11.5 dB |
  | Published DMA58 pair | 46 mm body | ≈ 247 Hz | −10.5 dB |

- **Pick, most robust to the unknowns: sealed TEBM28C10-4B in ≥ 60–100 cm³ net.**
  - Box losses, volume and stuffing barely move its response. In the tolerance runs, its 10–90 % band is **1.0 dB wide** between 90 and 400 Hz.
  - It needs no tuning part, and its suspension limits cone travel by itself.
  - The box is only about **62 × 75 × 27 mm inside**, so it frees space compared with the 150–300 cm³ assumed before.
  - **Ported is the "more bass" option.** It gives about an octave more extension and +6 dB at 100 Hz, but its port noise at loud bass can't be modelled.
  - **Passive radiator: not recommended at this size.** The radiators with published data gain only 1–4 dB at 100 Hz. The thin PUI radiator has no published excursion and the widest spread of any option (up to 5 dB).

**USB-C host port (task 2).** A USB 2.0 Type-C receptacle wired as a source only:
- Rp of 36 kΩ to 3.3 V on each CC pin, which advertises Default USB power [chk];
- the Daisy reads the CC pins and switches VBUS on only when a keyboard is attached (the spec's "cold socket" rule [chk]);
- the TPS2553 stays as the switch at ≈ 550–600 mA. Its reverse-voltage comparator protects floss if a charger is plugged into the wrong socket [chk].
- **Cables:** C-to-C for keyboards with a USB-C socket. For any other keyboard, carry one **C-plug-to-A-receptacle adapter**, which has Rd built in by spec [chk], and use the keyboard's own cable. That covers micro-B and mini-B without depending on how a given cable is built.
- **Host and device running together** is still unverified in libDaisy. The fallback is still TRS MIDI to the computer.

**Fit (task 3)**, TEBM28 sealed, body 32 mm:

| Shape | Result | Margin | Height |
|---|---|---|---|
| RAIL 400 × 80 | **Pass** with the speaker at one end. The board gets 333 × 70 mm, and the control row is limited to ≈ 333 mm (≤ 15 controls at 22 mm pitch, or ≈ 13 with grouping gaps) | Board +46 % | 32 mm body, ≈ 40 with knobs |
| RAIL, visual's sketch (board 260 × 62 + box at the end) | **Pass** for area, **fail** for a one-row panel over the board (260 mm holds ≤ 10–11 controls) | | |
| RAIL, ported (217 cm³) | Row shrinks to ≈ 267 mm | | |
| SLAB 400 × 133 | **Pass**: ≈ 23 % of the floor spare even with a single-sided board and a 400 cm³ ported box | Large | 32 / 40 mm |
| BLOCK 270 × 100 | **Pass, tight**: board 200 × 80 + box 60 × 93 | 3 mm along the length | 32 / 40 mm |

The BLOCK needs a double-sided SMD board and has no room for a passive radiator.

**Weights (task 4)** [est]:
- Modules: RAIL 0.71–0.97 kg, SLAB 0.85–1.14 kg, BLOCK 0.67–0.93 kg.
- Kits with a cable, against T5 ≤ 1.5 kg:

  | Kit | Without keyboard | With Xkey 25 | With K-Board C |
  |---|---|---|---|
  | FALLBOARD | 1.14–1.55 | **1.74–2.15 ✗** | **1.48–1.89 ✗** (passes only at the light end) |
  | SPINE | 1.10–1.47 | **1.70–2.07 ✗** | **1.44–1.81 ✗/borderline** |
  | CLOTH | 0.93–1.32 | **1.53–1.92 ✗** | **1.27–1.66 ✓ to borderline** |

- **No kit carries an Xkey 25 within T5.** The printed shell is the biggest lever: it's ≈ 0.25–0.55 kg of each module.

**Lid light (task 5).** A dim warm strip of ≈ 10 LEDs at 1–2 mA draws ≈ 0.05–0.1 W [calc/est]. Runtime with a typical keyboard goes from 6.1 / 8.6 / 14.4 h to **≈ 6.0 / 8.2 / 13.3 h: T2 still passes** [calc].

**Keyboard sockets (task 6).**
- Connector types checked:
  - nanoKEY2: mini-B;
  - K-Board C: USB-C (≈ 90 mA);
  - Xkey 25: USB-C on the current (2024) model, micro-B on earlier units (UNVERIFIED);
  - MicroLab mk3: USB-C, on the **rear**;
  - MPK Mini IV: USB-C.
- **Socket positions are mostly unpublished** (only the MicroLab's is stated). The cable channel has to accept a socket anywhere along the rear edge or on either end.
- A straight plug sticks out ≈ 25–35 mm [est], so FALLBOARD's 12 mm gutter needs right-angle plugs or ≈ 35 mm.

**Trade-offs for Adam** (§7):
1. Sealed vs ported vs passive radiator.
2. +7–9 mm of body thickness (or more for the Dayton parts) vs the measuring rule.
3. RAIL: a one-row panel vs bass (port) vs depth.
4. T5 with an Xkey: lighter shell, a lighter kit, or relax T5.
5. Cold-socket USB-C (spec-correct) vs always-on VBUS (works with non-compliant keyboards).
6. Lid light wired through the hinge vs its own cells.

---

## 1. Speaker without measuring (task 1)

### 1.1 What the rule rules out
`module.md` §6 and `feasibility.md` §6 paired the Same Sky CDS-5076 (7.6 mm deep) with a Tectonic TEPR32 radiator. The CDS-5076 publishes no Thiele/Small set, so the radiator's tuning couldn't be calculated and would have needed one acoustic measurement. That breaks the rule.

What a calculation needs from a driver: Fs, Qts (or Qes and Qms), Vas (or Sd and Cms), and for excursion and impedance also BL, Re, Mms and Xmax. From a radiator it needs Mms, Cms (or Fs), Sd and Rms (or Qms), plus its excursion limit. I searched for slim 50 mm-class drivers that publish all of these.

### 1.2 Published-data parts found
**Drivers:**

| Driver | Size, depth | Published set | Notes | Source |
|---|---|---|---|---|
| **Tectonic TEBM28C10-4B** (balanced-mode radiator) | Ø 55, **24.00 mm** seated | Fs 145, Re 3.8, Qts 0.44, BL 2.9, Mms 1.19 g, Cms 1.0 mm/N, Rms 0.31, Sd 8.55 cm², Xmax 2.8 mm p-p, 10 W, 80 dB/1 W | **$25, 135 in stock, active** | [chk, [datasheet](https://datasheet.sic-components.com/TEBM28C10-4B.pdf), [DigiKey](https://www.digikey.com/en/products/result?keywords=TEBM28C10-4B)] |
| Dayton DMA58-4 | 55.9 square, **31.75 mm** | Fs 165.5, Re 3.55, Qts 0.45, Vas 0.142 L, BL 3.67, Mms 2.05 g, Sd 14.5, Xmax 2 mm, 86.2 dB/2.83 V | Out of stock at soundimports on 22 Nov | [chk, [soundimports](https://www.soundimports.eu/en/dma58-4.html)] |
| PUI AS05804PS-X-R | 58.2 × 55.2, **33.8 mm** | Fs 145, Qts 0.536, Vas 0.108 L, BL 3.72, Mms 2.26 g, Xmax 4.5 mm (Sd derived: 12.1 cm² [calc]) | Mouser 28, DigiKey 18. **Named by PUI as a partner for its radiator** | [chk, [datasheet](https://xonstorage.blob.core.windows.net/pdf/puiaudio_as05804psxr_apr22_xonlink.pdf), [PUI](https://puiaudio.com/product/s/AS05804PS-X-R)] |
| Tectonic TEBM36S12-8A | 65 square, 29.7 mm | Full set | Deeper and larger than the TEBM28, with no gain; not simulated | [chk, [datasheet](https://doc.soundimports.nl/pdf/brands/Tectonic%20Elements/TEBM36S12-8A%20BMR/tebm36s12-8a-spec-sheet.pdf)] |
| Tectonic TEBM46C20N-4B | 68 square, 34.65 mm | Full set | Too deep | [chk, [datasheet](https://www.wagneronline.com.au/attachments/Audio-Speakers-PA/dayton/TEBM46C20N-4B.pdf)] |
| Tang Band W2-2360S ("low profile") | Ø 51, **depth UNVERIFIED** | Full set on a database page (Qms 1.16, Xmax 1.0 mm); no primary datasheet reached | Can't confirm its depth, so it can't be fitted | [[loudspeakerdatabase](https://loudspeakerdatabase.com/TangBand/W2-2360S)] |
| Visaton FRS 5 X | 46 mm cutout, depth not stated | Fs 190, Qts 0.7, Vas 0.23 L, BL 2.67; no Xmax | Depth and Xmax missing | [chk, [datasheet](https://www.farnell.com/datasheets/2330028.pdf)] |
| Visaton K 50 FL / K 50 FLS (flat) | "very compact" | **Fs only** | Not designable | [chk, [K 50 FL](https://gotron.be/media/files/Downloads/K50FL.pdf), [K 50 FLS](https://www.parts-express.com/pedocs/specs/292-726--visaton-k50fls-8-spec-sheet.pdf)] |

**Radiators:**

| Radiator | Size | Published set | Gaps | Source |
|---|---|---|---|---|
| **PUI APR050SO-R** | **50 × 37 × 3.35 mm** oval, stamped steel | Mms 4.06 g, Cms 0.928 mm/N, Qms 2.53, Rms 0.81, Sd 8.7 cm², Fs 78 Hz ±10 % ("up to 20 % variance… except for Fs") | **Excursion not published.** Stock: DigiKey 750, Mouser 385 | [chk, [datasheet](https://www.mouser.com/datasheet/2/334/APR050SO_R-1628420.pdf), [PUI](https://www.puiaudio.com/products/apr050so-r)] |
| Tectonic TEPR32 | Ø < 40 mm | Mms 4.2 g, Cms 3.6 mm/N, Rms 0.27, Sd Ø 32, Xmax ±5 mm, Fs 40 Hz ±20 % | **Depth not published.** $1.50, 34 in stock | [chk, [datasheet](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5336/TEPR32.pdf), [DigiKey](https://www.digikey.com.mx/en/products/detail/seltech/TEPR32/17028326)] |
| Dayton DMA58-PR | 55.9 square, **38.1 mm** | Mms 6.7 g, Cms 2.40, Qms 3.93, Sd 14.5, Xmech 7 mm | Threaded rod for added mass | [chk, [soundimports](https://www.soundimports.eu/en/dma58-pr.html)] |

### 1.3 The model (`eng/speaker-sim/sim.py`)
- **What it is:** the standard lumped-parameter loudspeaker model (Thiele and Small's analogue circuit), written in Python with numpy and matplotlib. No package was needed.
  - Electrical: Re + jωLe.
  - Mechanical: Rms, Mms, Cms, coupled by BL.
  - Box: compliance Vb/ρc², with a loss resistance set by QL.
  - Vent, one of: a radiator branch (Rmp, Mmp, Cmp over Sp², for 1 or 2 radiators); a port (ρ·Leff/Sp plus a small loss); or none (sealed).
  - Output: the net volume velocity of the cone plus the vent, radiated into half space at 1 m (the module on a table).
- **Outputs:**
  - SPL at 1 W;
  - impedance;
  - excursion of the cone and the radiator;
  - maximum SPL, limited by a 2 W amp [est], the driver's Xmax, the radiator's Xmax where published, and port air speed ≤ 17 m/s (≈ 5 % of c, the usual design limit [est]).
- **How the candidates are built:**
  - Each driver is placed in each shape's box, from §3. Body = driver depth + deck 2.5 + 3 mm behind the magnet + floor 2.4 [plat/est]. Net volume = 95 % of gross, minus the driver's displacement.
  - Radiators are placed on the deck beside the driver only where their footprint fits.
  - Ports are Ø 12 mm, tuned by a sweep: the lowest −3 dB point whose response stays within +1.5 dB of the mid-band. That's the standard box-program design rule.
- **Files:**
  - `shape_rail.png`, `shape_slab.png`, `shape_block.png`: SPL, impedance, excursion and max SPL for every candidate that fits that shape;
  - `tolerance_tebm28.png`, `tolerance_dma58.png`: nominal curve plus the 10–90 % band from 300 random draws;
  - `sealed_volume_sweep.png` and `.csv`: sealed f3 and Qtc against volume;
  - `summary.csv`: every number below.
- **Rerun:** `python3 -I floss/eng/speaker-sim/sim.py`.

**Hand check of the model** [calc]: TEBM28C10-4B sealed at 100 cm³.
- Vas = ρc²·Sd²·Cms = 138,800 × (8.55 × 10⁻⁴)² × 1.0 × 10⁻³ = **101 cm³**.
- Qts = Qes·Qms/(Qes + Qms), with Qes = 2πFs·Mms·Re/BL² = 0.49 and Qms = 2πFs·Mms/Rms = 3.5. So Qts = 0.43 (published: 0.44).
- α = Vas/Vb = 1.01, so Fc = Fs·√(1 + α) = 146 × 1.418 = **207 Hz** and Qtc = 0.43 × 1.418 = **0.61**. The simulation gives 207 Hz and 0.61.
- The textbook f3 for Qtc 0.61 is 1.18 × Fc = 245 Hz. The simulation gives 255 Hz because it measures against the 0.7–1.5 kHz level and includes Le. The model agrees with the closed-box formulas.

### 1.4 Results (1 W, 1 m, half space; all [calc])
Columns: body thickness without knobs; net volume; −3 / −6 / −10 dB points; level at 100 Hz relative to mid-band; maximum SPL at 100 Hz.

| Shape | Driver + box | Body | Vb | f3 / f6 / f10 (Hz) | @100 Hz | Max SPL @100 Hz | Note |
|---|---|---|---|---|---|---|---|
| RAIL | **TEBM28 sealed** | 32 | 217 | 257 / 173 / 121 | −12.4 | 70.0 | Same response at ≈ 100 cm³ (§1.7) |
| RAIL | TEBM28 + 1 × APR050SO-R | 32 | 214 | 236 / 151 / 106 | −11.5 | 71.6 | Radiator excursion 0.86 mm at 1 W: limit unpublished |
| RAIL | TEBM28 + 1 × TEPR32 | 32* | 214 | 239 / 156 / 100 | −10.0 | 72.9 | *Radiator depth unpublished |
| RAIL | **TEBM28 ported**, Ø 12 × ≈ 113 mm | 32 | 217 | **115 / 100 / 89** | **−6.1** | **76.2** | Peak port air 13.5 m/s at 1 W |
| RAIL | DMA58-4 + DMA58-PR (published pair) | 46 | 320 | 247 / 167 / 107 | −10.5 | 74.8 | |
| RAIL | AS05804PS ported | 42 | 295 | 104 / 91 / 81 | −3.7 | 77.7 | |
| SLAB | TEBM28 sealed | 32 | 410 | 262 / 171 / 115 | −11.7 | 70.0 | |
| SLAB | TEBM28 + 2 × APR050SO-R | 32 | 404 | 238 / 141 / 101 | −10.4 | 72.0 | Widest spread (§1.5) |
| SLAB | **TEBM28 ported** | 32 | 410 | **103 / 90 / 81** | **−3.4** | **78.4** | Port ≈ 74 mm long |
| BLOCK | TEBM28 sealed | 32 | 130 | 255 / 179 / 128 | −13.5 | 69.7 | No radiator fits (§3.3) |
| BLOCK | TEBM28 ported | 32 | 130 | 135 / 116 / 101 | −10.4 | 72.5 | Port Leff 151 mm: must fold |

Every row is in `summary.csv`, including the DMA58 and AS05804PS variants in each shape.

**Mid-band level:**
- TEBM28: ≈ 80 dB at 1 W, 1 m.
- DMA58: ≈ 82 dB.
- At the power budget's moderate volume (0.08–0.2 W [plat]), the TEBM28 gives ≈ 69–73 dB at 1 m [calc].

**Why the radiators gain so little here** [calc]:
- The boxes are already 1–4 × the drivers' Vas, so the sealed response is close to the driver's free-air limit. A radiator helps only below Fs, and only with enough moving area.
- The radiators with published data have 8–15 cm² of area against the driver's 8.5–14.5. The usual guide asks for a radiator displacing ≥ 2 × the driver [chk, `feasibility.md` §6.1].
- The thin PUI radiator's excursion isn't published at all.
- A port's tuning, by contrast, is set by its length, which is cut to a calculated number.

### 1.5 Robustness: what 300 random draws do
Each draw varies:
- the driver's Mms ± 10 %, Cms ± 20 %, BL ± 10 % and Rms ± 20 %, inside the tolerances printed on the Tectonic and PUI datasheets [chk];
- the radiator's Mmp and Cmp ± 20 % (PUI: "up to 20 % variance" [chk]);
- box loss QL from 3 to 15 (leaky and stuffed through to tight and bare) [est];
- volume ± 10 % (wiring, stuffing, print accuracy) [est].

The width of the 10–90 % band between 90 and 400 Hz, worst point [calc]:

| Loading | Band width | f3 spread (10–90 %) |
|---|---|---|
| **Sealed (any driver)** | **1.0–1.2 dB** | 214–305 Hz (driver Cms tolerance alone) |
| TEPR32 radiator | 1.2–1.4 dB | ≈ 190–295 Hz |
| DMA58-PR radiator | 1.4–2.0 dB | ≈ 185–300 Hz |
| Port | 2.5–3.4 dB | ≈ 105–180 Hz* |
| **APR050SO-R radiator** | **2.7–5.7 dB** | ≈ 185–300 Hz |

*The port's f3 range looks wide because its response sits in a ≈ 2 dB shelf from 110 to 300 Hz that crosses the −3 dB line. The curves themselves stay tight (see `tolerance_tebm28.png`).

### 1.6 What the model can't capture
These are the things normally measured. Each one gets a margin or a design-around:
- **Enclosure losses:** air leaks, absorption and stuffing. They're lumped as QL and swept from 3 to 15. A sealed box is barely affected; a port's bass shelf can sag by ≈ 1–2 dB. *Design-around:* seal the box (gasket, glued seams), use light stuffing or none, and prefer sealed.
- **The radiator's real mass and compliance:** the published values are ± 20 %, and the APR050SO-R's excursion isn't published. A radiator would normally be tuned by measuring and adding mass. *Design-around:* none that removes it, so **no radiator**.
- **Port noise and compression:** turbulence above ≈ 5 % of c, plus port-end losses. The model only flags air speed: ≈ 13.5 m/s peak at 1 W, under 17 m/s up to ≈ 1.6 W. *Design-around:* flared ends, a ≥ Ø 12 mm port, and the high-pass below.
- **The port's own volume** (≈ 13 cm³ in RAIL) isn't subtracted. Fb comes out ≈ 3 % high; add the port's volume to the box when it's drawn.
- **Cone break-up, front cavity, grille and diffraction,** which shape everything above ≈ 2 kHz. *Design-around:* Big Energy's grille rule, open area ≥ ≈ 73 % of Sd [plat]. For the TEBM28 that's ≥ ≈ 620 mm² [calc]. Keep ≥ 1.5 mm between the cone and the grille [plat].
- **Placement:** a lap, a bag or a table edge changes the bass by several dB. The model assumes a table (half space).
- **Each unit's actual parameters** vary within the tolerances in §1.5. The sealed box is least sensitive to them.

### 1.7 Pick and constraints for the designers
**Pick: sealed TEBM28C10-4B** [calc/est].
- **Net volume ≥ 60 cm³**: Qtc 0.71 at 60, 0.61 at 100. Above ≈ 80 cm³ the response doesn't change (`sealed_volume_sweep.csv`). A box of ≈ **60 × 62 × 27 mm inside** gives ≈ 85–95 cm³ net after the driver's 13 cm³.
- **Depth:** the driver needs a clear column Ø 56 × 24 mm under the deck, plus ≈ 3 mm behind the magnet: body **≈ 32 mm**.
  - The rest of the body could stay at `module.md`'s 23–25 if the designers want a local bulge. That's a form decision, not engineering.
  - A recessed front mount may save ≈ 1–2 mm [est].
- **Fires up through the deck** (no lap muffling). Grille ≥ 620 mm² open.
- **High-pass the speaker feed only, ≈ 100 Hz, second order** (one op-amp stage before the class-D amp; phones stay full range). At 2 W, octave-down notes below ≈ 100 Hz would otherwise reach Xmax (1.4 mm) [calc]. It's needed for a port and helpful for sealed.
- **Seal:** a foam gasket at the driver flange, glued or gasketed box seams, and a sealed cable entry.

**Option: ported TEBM28** (+6 dB at 100 Hz, f3 ≈ 105–135 Hz):
- box ≥ 130 cm³ (BLOCK) or ≈ 220 cm³ (RAIL);
- a Ø 12 mm port ≈ 110–150 mm long, which can be printed into the box wall and folded;
- the port exits on the deck or the rear wall, ≥ 113 mm² open;
- the high-pass above is required.

### 1.8 The thicker published-data path, if Adam prefers the Dayton parts
| Path | Body (no knobs) | With knobs | vs `module.md` 23–25 |
|---|---|---|---|
| DMA58-4 sealed or ported | ≈ 40 mm | ≈ 48 | +15–17 mm |
| DMA58-4 + DMA58-PR (the matched pair) | ≈ 46 mm | ≈ 54 | +21–23 mm |
| AS05804PS ported (PUI's radiator partner, best bass) | ≈ 42 mm | ≈ 50 | +17–19 mm |

What they buy over the TEBM28: about +2 dB of mid-band level (DMA58) and 1–5 dB more at 100 Hz.

---

## 2. USB-C host port (task 2)

**What changes from `module.md` §3:** the socket goes from USB-A to USB-C, CC sensing is added, and VBUS is switched on only after a keyboard is attached. The data pins, the TPS2553 and libDaisy's host stack stay the same.

**Circuit (Route A, recommended; all hand-solderable SOT-23 / 0603 parts except the receptacle):**
- **Receptacle:** a 16-pin USB 2.0 Type-C, the same part as floss's own USB-C [est].
  - Tie D+ (A6, B6) together and D− (A7, B7) together, to Seed D30 / D29 (USB_OTG_HS PB15 / PB14) [chk pins, `module.md` §3; which pin is D+ follows the STM32 convention, est].
  - ESD array on D+, D− and VBUS, e.g. USBLC6-2SC6 [est].
- **Source termination:** **36 kΩ from each CC to 3.3 V** (Default USB power; 56 kΩ if pulled to 5 V) [chk, [Infineon](https://community.infineon.com/t5/Knowledge-Base-Articles/Termination-Resistors-Required-for-the-USB-Type-C-Connector/ta-p/253544)].
  - With the keyboard's Rd of 5.1 kΩ [chk], CC sits at 3.3 × 5.1/41.1 = **0.41 V**; with nothing attached, 3.3 V [calc]. That's a clean logic low or high on a Daisy GPIO through 1 kΩ.
  - A cable with Ra on the other CC pin reads lower still, so firmware treats "either CC low" as attached.
- **Cold socket:** "5V shall be applied to VBUS only when a UFP is detected", and with nothing attached "VBUS must be 0V or vSafe0V" [chk, [Chromium Type-C notes](https://chromium.org/chromium-os/developer-library/reference/hardware/cable-and-adapter-tips-and-tricks)].
  - Firmware enables the TPS2553 when a CC pin goes low, and disables it when both are high or on FAULT.
  - The power-off rule (S5) comes for free: when floss is off, its 3.3 V rail is off, so there's no Rp and no VBUS.
- **5 V limit:** TPS2553 set at **≈ 550–600 mA**, unchanged. Default USB power tells a Type-C sink it may draw the USB 2.0 default (500 mA) [est].
  - Range 75–1700 mA; FAULT asserts on over-current and reverse voltage; SOT-23-6; active [chk, [TI](https://www.ti.com/product/TPS2553)].
  - The 5 V comes from the system boost or the BQ25895's boost, as in `module.md` [plat].
- **Daisy pins:** CC1, CC2, EN and FAULT = 4 GPIO (`module.md` had EN + FAULT). Free-pin availability is to be checked against the pin map [est].
- **Cost:** ≈ the same as the USB-A version, $3–6 [est].

**Route B (alternative):** TI **TPS25810**, a Type-C DFP (source) controller with an integrated 3 A switch.
- Its current limits are fixed at **1.7 A or 3.4 A**. It advertises STD / 1.5 A / 3 A, handles VCONN, and has FAULT and load-detect outputs. Package: **WQFN-20 4 × 3 mm**. Active [chk, [TI](https://www.ti.com/product/TPS25810)].
- It does the CC logic in hardware, but it's a QFN (factory assembly) and can't be set to 500–600 mA. A short would be held at 1.7 A, against the 0.5 A floss budgets. **Not recommended.**

**Cables and adapters:**

| Keyboard socket | Cable or adapter | Works with a cold socket? |
|---|---|---|
| USB-C (K-Board C, Xkey 25 2024, MicroLab mk3, MPK Mini IV) | C-to-C USB 2.0 | Yes, **if the keyboard has its Rd**, as a compliant Type-C device must [chk]. A non-compliant keyboard gets no VBUS: UNVERIFIED per model |
| micro-B (older Xkey, other older minis) | C-plug-to-micro-B-plug cable | Yes: by spec it carries "5.1 kΩ Rd" [chk, Chromium, spec §3.5.7] |
| mini-B (nanoKEY2) | C-to-mini-B cable | **Not covered** by the spec table I found, so whether a given cable has Rd is UNVERIFIED |
| Any socket, using the keyboard's own A-to-X cable | **C-plug-to-A-receptacle adapter** | Yes: by spec it carries "5.1 kΩ Rd" [chk, Chromium, §3.6.1]. **This is the universal fallback; carry one in the accessory pocket** |

**Wrong-socket safety:** floss has two USB-C sockets that look alike.
- A Type-C charger plugged into the host socket sees floss's Rp, not Rd, so neither side turns VBUS on [calc from the spec rules above].
- A legacy A-to-C cable from an A charger brings always-on 5 V with "56 kΩ Rp" in its plug [chk]. The TPS2553's reverse-voltage comparator then turns the switch off and raises FAULT [chk, TI], and the port light flashes.
- Marking or placing the two sockets apart is a designer task.

**Always-on fallback (trade-off 5):** a firmware mode set by holding a button at power-on (PROPOSAL). It turns VBUS on regardless of CC, for keyboards with no Rd. It's against the spec, and a source plugged in while it's on is caught only by the TPS2553's reverse protection.

**Host and computer USB at once:** unchanged from `module.md` §3. It's **unverified** in libDaisy [est]. **Fallback:** TRS MIDI to the computer, with floss's USB-C used only for charging while a keyboard is plugged into the host port.

---

## 3. Fit checks (task 3)
**Common inputs:**
- **Board:** ≈ 16,000 mm² double-sided, or ≈ 16,500 single-sided [plat, `module.md` §6].
- **Battery:** 2 × 50 × 60 × 7.5 mm, as 100 × 60 × 7.5 side by side or 50 × 60 × 15 stacked, under the board [plat].
- **Walls:** 2.5 mm, so inner = outer − 5 [est].
- **Body:** 32 mm (TEBM28) [calc/est], so the inside height is ≈ 27 mm. That also allows the stacked battery under the board: floor 2.4 + 15 + 3 + 1.6 + 6.5 + deck 2.5 ≈ 31 [calc].
- **Rear I/O:** ≈ 9 parts, which need ≈ 15 mm of depth along a wall [est].

### 3.1 RAIL, 400 × 80 (inner ≈ 395 × 75)
| Layout | Speaker | Board | Control row | Result |
|---|---|---|---|---|
| **R1: sealed box at one end** | 60 × 71 × 27 inside ≈ 97 cm³ net ✓ (f3 ≈ 255) | 333 × 70 = 23,300 mm² vs 16,000 needed: **+46 %** | ≤ 333 mm. 15 controls at 22 mm pitch with no gaps, or ≈ 13 with the director's 6 grouping gaps (≈ 8 mm each) | **Pass** |
| R2: visual's sketch (board 260 × 62, box 128 × 70) | 217 cm³ ✓ (sealed f3 257, or ported 115) | 16,100 mm², **+1 %** | Over the board, 260 mm holds **10–11 controls** at 22–25.5 mm pitch. A full row of 14–16 runs over the speaker box, so those pots would need to be panel-mounted and hand-wired, with ≈ 10 mm pot bodies taking box height | Area **pass**, one-row panel **fail** |
| R3: ported box at one end | 128 × 70 × 27, 217 cm³ ✓, port ≈ 113 mm along the box | 267 × 70 = 18,700 (+17 %) | ≤ 267 mm: ≈ 12 controls at 22 mm, or ≈ 10 with gaps | Pass with a shorter row |
| R4: speaker behind the row | Needs 20 mm (row) + 60 mm (box) = 80 mm inside | | | **Fail by 5 mm.** It passes at RAIL ≈ 400 × 85 outer |

**Strands (6 tabs) plus about 16 controls don't fit one row in any RAIL layout:** 16 × 22 + 6 × 12 = 424 mm, more than the 395 inside [calc]. That agrees with the visual designer.

**Height (RAIL R1):** body ≈ 32 mm, knobs + ≈ 8 [plat], so **≈ 40 mm overall**.

### 3.2 SLAB, 400 × 133 (inner ≈ 395 × 128 = 50,560 mm²)
- Board single-sided 16,500 (e.g. 250 × 66: friendlier to hand assembly) + ported box 150 × 110 × 27 (410 cm³, f3 ≈ 103) 16,500 + battery beside the board 6,000 = **39,000 mm²: ≈ 23 % spare** [calc].
- Two rows at 22–24 mm pitch hold 32+ controls, so the strands fit.
- **Pass, large margin.** Height ≈ 32 / 40 mm.

### 3.3 BLOCK, 270 × 100 (inner ≈ 265 × 95)
- Board 200 × 80 double-sided + sealed box 60 × 93 × 27 (130 cm³ net, f3 ≈ 255) = 262 mm of 265 length: **3 mm margin** [calc].
- Rear I/O in the 15 mm strip behind the board (95 − 80) ✓.
- Battery under the board ✓.
- **Pass, tight.**
  - The board must be double-sided SMD (no single-sided option).
  - No passive radiator fits on the deck: 95 − 56 = 39 mm, minus walls, leaves < 37 mm.
  - Ported works only with a folded Ø 12 × ≈ 145 mm port (f3 ≈ 135).
- Height ≈ 32 mm body. The raised rim over the knob tops (visual) makes it ≈ 40.

---

## 4. Weights (task 4), all [est]
**Basis:**
- **Shell:** printed PETG like CATHEDRAL [plat]: 1.27 g/cm³, 2.0–2.5 mm solid-equivalent over every face, +20 % for ribs, bosses and the speaker box.
- **Contents, the same in each shape, 418–608 g:**
  - board, parts, Daisy and two PGA2350: 120–180 g;
  - two pouch cells: 100–110 g;
  - TEBM28: 58 g [chk];
  - 16 knobs + pots: 100–190 g;
  - connectors, switches, wiring, grille, feet, fasteners: 40–70 g.
- **Path:** TEBM28 at a 32 mm body. The DMA58 path adds ≈ 70–80 g (heavier driver [est] + taller walls).

| Module | Shell | **Total** |
|---|---|---|
| RAIL 400 × 80 × 32 | 289–361 g | **0.71–0.97 kg** |
| SLAB 400 × 133 × 32 | 428–535 g | **0.85–1.14 kg** |
| BLOCK 270 × 100 × 32 (+ 8 mm rim) | 255–319 g | **0.67–0.93 kg** |

**Kit parts** (per `design/jam-module.md` turns 2–3):

| Kit | Parts | Mass |
|---|---|---|
| FALLBOARD (closed ≈ 400 × 230) | Bed 400 × 150 (3 mm birch ply + bookcloth ≈ 140 g); walnut or printed lip 30–50; two end blocks 40–60; lid 400 × 230 (3–4 mm ply + cloth ≈ 215–280); hinge, strut, lamp and wiring 30–60 | **0.40–0.55 kg** |
| SPINE (closed ≈ 400 × 140) | Keyboard board 395 × 140 (3 mm ply + cloth both sides ≈ 145); cloth spine and core 15–25; end blocks 40–60; straps 10–20; brass corners ≈ 10–25 | **0.22–0.30 kg** |
| CLOTH | 0.8 × 0.8 m quilted wrap (330–520 g/m² for outer + batting + liner ≈ 0.21–0.33 kg) + sleeve and pocket 20–30 g | **0.23–0.36 kg** |
| USB cable (any kit) | | ≈ 25 g |

**Totals against T5 (≤ 1.5 kg):**

| Kit | Module + kit + cable | + Xkey 25 (600 g [chk]) | + K-Board C (340 g [chk]) |
|---|---|---|---|
| FALLBOARD (RAIL) | 1.14–1.55 | **1.74–2.15 ✗** | **1.48–1.89 ✗** (passes only at the light end) |
| SPINE (SLAB) | 1.10–1.47 | **1.70–2.07 ✗** | **1.44–1.81 ✗/borderline** |
| CLOTH (BLOCK) | 0.93–1.32 | **1.53–1.92 ✗** (just over at the light end) | **1.27–1.66 ✓ to borderline** |

**Levers, largest first** [est]:
- shell walls 2.0 mm with ribs, or partial infill: −60 to −110 g;
- FALLBOARD's lid as bookcloth over 2 mm board instead of ply: −80 to −120 g;
- lighter knobs: −40 to −80 g;
- the 11.1 Wh battery: −55 g, but T2 fails at loud volume [plat].

Together these bring FALLBOARD + K-Board C to ≈ 1.25–1.6 kg. **No kit carries an Xkey 25 within 1.5 kg on these estimates.**

**Closed thickness with the 32 mm body** [calc]:
- **FALLBOARD ≈ 48 mm** (drawn 38): module 40 + 4 clearance + 4 lid.
- **SPINE ≈ 61 mm** (drawn 54–55; the director assumed ≈ 60): 40 + keyboard 16 + board 3 + 2 air.
- **CLOTH:** the BLOCK is ≈ 40 mm at the rim.
- With the DMA58 path, add ≈ 8 mm to each.

---

## 5. Lid light power (task 5)
- **Target** [est]: ≈ 20–50 lux on the keys, a dim reading-light level. The keys cover 0.39 × 0.135 = 0.053 m², so that's ≈ 1–3 lm on the keys, or ≈ 2–6 lm emitted at ≈ 50 % of the light landing on them.
- **Source:** ≈ 10 warm-white mid-power LEDs (2835 class) at 1–2 mA each, at ≈ 2.7 V forward. That's ≈ 30–55 mW in the LEDs; from 5 V through resistors, ≈ 50–100 mW. LED efficacy ≈ 100 lm/W at low current [est], which gives ≈ 3–5 lm. Dim it with PWM from a Daisy pin.
- **T2** [calc, `module.md` §5 method: 22.2 Wh × 0.9 usable × 0.9 boost]:

  | Case | Without the light | +0.1 W light |
  |---|---|---|
  | Typical keyboard (worst / mid / best) | 6.1 / 8.6 / 14.4 h | **6.0 / 8.2 / 13.3 h ✓** |
  | Keyboard at the full 500 mA, loud | ≈ 3.5 h | **≈ 3.4 h** (already a miss without the light) |

  Even a 0.25 W light leaves ≥ 5.7 h in the worst typical case.
- **Wiring options** (FALLBOARD's lid lifts off its pin hinge):
  - (a) two wires through the hinge to a magnetic 2-pin connector, powered by floss;
  - (b) the lid carries its own 2 × AAA (≈ 1.4 Wh, ≈ 14 h at 0.1 W, +≈ 25 g) with its own switch.
- **SPINE** lights from the module's edge, wired inside the module, with no hinge question.

---

## 6. Keyboard USB sockets and the cable channel (task 6)
| Keyboard | Connector | Position | Draw | Source |
|---|---|---|---|---|
| Korg nanoKEY2 | **Mini-B** ("USB-Mini") | UNVERIFIED | < 100 mA [plat] | [chk, [Thomann](https://www.thomannmusic.com/korg_nanokey_2_white.htm)] |
| KMI / Muse K-Board C | **USB-C**; ships with a C cable | UNVERIFIED (the manual says only "USB port") | **≈ 90 mA max** | [chk, [manual](https://files.keithmcmillen.com/downloads/k-board/K-Board-C-Manual_v1.2.1.pdf)] |
| CME Xkey 25 | **USB-C** on the current (2024) model, with a C-to-A cable; micro-B on earlier units (UNVERIFIED) | UNVERIFIED | Not published | [chk, [ESI](https://esi-audio.com/products/xkey25)] |
| Muse QuNexus | UNVERIFIED | UNVERIFIED | | |
| Arturia MicroLab mk3 | **USB-C** | **Rear**, beside the sustain jack | | [chk, [SOS](https://www.soundonsound.com/reviews/arturia-microlab-mk3?amp)] |
| Novation Launchkey Mini 25 MK4 | USB (type not stated); MIDI out on 3.5 mm TRS | MIDI ports on the **rear**; USB position UNVERIFIED | | [chk, [Thomann](https://www.thomannmusic.com/novation_launchkey_mini_25_mk4.htm)] |
| Akai MPK Mini IV | **USB-C** | UNVERIFIED | | [chk, [Thomann](https://www.thomann.co.uk/akai_professional_mpk_mini_iv_gray.htm)] |

The manuals and listings I could reach don't state where the socket sits on the slim keyboards. Photos weren't viewable as evidence here. So the channel is designed for **any position**:
- **Where a socket can be:** anywhere along the keyboard's rear edge, or on either end.
- **Gutter depth:** a straight plug plus its strain relief sticks out **≈ 25–35 mm** from the socket [est]. A right-angle plug sticks out ≈ 10–15 mm [est].
  - FALLBOARD's 12 mm gutter therefore needs right-angle plugs, or ≈ 35 mm of gutter.
  - Right-angle plugs come in up, down, left and right versions, and which one fits depends on how each keyboard's socket is turned (UNVERIFIED per model). That argues for the deeper gutter, or a cable that runs from an end socket around the end block.
- **Cable length:** host port centred on the module's front face, to a socket at the far end of a 388 mm keyboard: ≈ 200 mm along + ≈ 60 mm across + ≈ 30 mm for each plug body ≈ **0.3 m minimum**. A 0.3–0.5 m cable covers every case [calc/est].
- **End blocks** (director): leave a ≥ 15 mm notch, or a pass-through, for a plug in an end socket.

---

## 7. Trade-offs for Adam
| # | Question | Options | Engineering view |
|---|---|---|---|
| 1 | **Speaker loading** (was trade-off 6) | **Sealed** (f3 ≈ 255 Hz, the most robust, the smallest box) / **ported** (f3 ≈ 105–135 Hz, +6 dB at 100 Hz, port noise at loud bass unmodelled) / **passive radiator** (+1–4 dB at 100 Hz; the slim radiator's excursion is unpublished, and the published pair needs a 46 mm body) | **Sealed** as the baseline; ported if more bass is worth one unmodelled risk. **A passive radiator doesn't earn its place at this size** |
| 2 | **Body thickness** (new) | ≈ 32 mm with the TEBM28 / ≈ 40 with the DMA58 / ≈ 46 with the DMA58 pair / 23–25 only with an unpublished slim driver (needs a measurement, so out) | **32 mm** (or a local speaker bulge, the designers' call) |
| 3 | **RAIL's one row** (new) | Sealed box at one end: ≤ ≈ 13–15 controls / ported: ≤ ≈ 10–12 / RAIL at 85 mm deep: row and speaker side by side / SLAB | Depends on the one-voice panel count (systems, pass 2) |
| 4 | **T5 with an Xkey** (new) | Lighter shell and kit (≈ −0.2–0.3 kg) / recommend slim keyboards ≤ ≈ 350 g / relax T5 to ≈ 2 kg for the kit | Every kit with an Xkey misses 1.5 kg on these estimates |
| 5 | **USB-C VBUS** (new) | Cold socket (spec-correct; works with compliant keyboards and every adapter route) / always-on mode as a firmware fallback | **Cold socket**, with the always-on mode held in reserve, plus a C-to-A-receptacle adapter in the kit |
| 6 | **Lid light power** (new) | Wired through the hinge / its own AAA cells | Either works. T2 holds (≈ 2–8 % less runtime) |
| 7 | Host and computer USB at once (unchanged, `module.md` 9) | Rely on it / TRS fallback | Plan for both |

## 8. What changes from `module.md`
- §3: the host socket becomes **USB-C** (CC Rp, cold socket, 4 GPIO). The TPS2553 setting is unchanged.
- §6:
  - **speaker:** sealed TEBM28C10-4B, ≥ 60–100 cm³, ≈ 62 × 75 mm of footprint (was a 150–300 cm³ radiator box needing a measurement);
  - **height:** ≈ 32 mm body, ≈ 40 with knobs (was 31–33 overall).
- §5: speaker high-pass ≈ 100 Hz added. Runtime is unchanged except the lid light (≈ 2–8 % less).
- §8: trade-off 6 is replaced by trade-offs 1 and 2 above.
- Weight: the module estimate becomes ≈ 0.67–1.14 kg depending on shape (was 0.63–0.91).

## Sources
- Drivers and radiators: as linked in §1.2.
- Type-C termination: [Infineon](https://community.infineon.com/t5/Knowledge-Base-Articles/Termination-Resistors-Required-for-the-USB-Type-C-Connector/ta-p/253544).
- Cable resistors and cold socket: [Chromium Type-C notes](https://chromium.org/chromium-os/developer-library/reference/hardware/cable-and-adapter-tips-and-tricks).
- Switch and controller: [TI TPS2553](https://www.ti.com/product/TPS2553), [TI TPS25810](https://www.ti.com/product/TPS25810).
- Keyboards: as linked in §6.
- Simulation: `eng/speaker-sim/sim.py` (my code; parameters copied from the sources above).
