# floss module: engineering rev 3 (2026-11-22)

Status: **rev 3**, the engineer's answers to the module concept's §11 list (`floss/design/concepts/module/how-it-works.md`, rev 2: 280 × 105 × 35 hull, speaker crown on the axis, deck at 25–26), the kit questions, and the owner's speaker question. `module.md` and `module-r2.md` are unchanged; r3 supersedes r2 only where it says so.

Owner, verbatim:
- "for now the case will be entirely 3d printed"
- "Cloth wrapping is fine as long as the core is printed"
- "Speaker let’s figure out what will sound best idc method"

PRINCIPLES §7 still binds: Adam measures nothing, and choices rest on published evidence or on virtual models built from it.

**Marks:** **[chk]** checked against the linked source · **[calc]** my arithmetic or simulation · **[est]** my estimate · **[plat]** from family or earlier eng records · **UNVERIFIED** no published source found; designed around.

---

## 0. Summary

**Best sound (owner's question, §8).**
- **Recommendation: E, two TEBM28C10-4B drivers playing mono, each on its own class-D channel, in one shared ported box of ≈ 190 cm³ net.**
  - **Port:** Ø 16 × ≈ 140 mm, flared at both ends.
  - **Tuning:** Fb ≈ 145 Hz, chosen with no hump.
  - **Speaker feed:** a second-order high-pass at ≈ 115 Hz.
- **What it gains over today's single sealed crown (A)** [calc]:
  - **+5.4 dB per watt across 150–800 Hz**, where the ensemble and pads live. The same loudness takes ≈ 30 % of the battery power: 80 dB at 1 m needs 0.48 W instead of 1.66 W.
  - **+11 dB of clean headroom at 100–200 Hz and +8 dB at 200–800 Hz.**
  - **f3 ≈ 152 Hz instead of 255** (f6 131 instead of 190).
- **It keeps the 35 mm height and the 280 width.** It holds **105 deep only if the whole rear region behind the rear row becomes speaker box**: the cells move to the two ends under the jambs, and the electronics become two stacked boards in the front band. That leaves ≈ 4 % volume margin. Otherwise the module goes to **≈ 280 × 115 × 35**.
- **Fallbacks, in order:**
  - **D:** the same pair, sealed, 150 cm³. Most robust (1.1 dB tolerance spread). +3 dB per watt and +6 dB of headroom, but no extra bass.
  - **C:** one TEBM28, ported, 120 cm³. f3 140, +6 dB at 100–200 Hz, and the smallest step up.
- **Ruled out:**
  - ported inside today's crown (the port won't fold into it);
  - a passive radiator (no thin radiator publishes its excursion, and the published one is 38 mm deep);
  - the larger PUI 58 / 65 mm drivers. They're no better than the pair and need a 42–45 mm body.

**§11 answers:**

| # | Question | Answer |
|---|---|---|
| 1 | Stack at 35 | **Fits, with the deck at 25, not 26.** Heights: floor 0–2.0, cells 2.0–9.5, ≥ 1 mm swell gap, board top 12.1–16.5, deck 23–25, Ø 10 × 8 knob tops at 34, rim 35 [calc] |
|   | Pots and switches | The pot must measure **≤ ≈ 21 mm from the PCB to the shaft tip**. Bourns PTV09A-3 (bushingless, 6.5 mm body, 18T, L 15) fits *if* its L is measured from the PCB (UNVERIFIED drawing plane). The Tayda A-5622 (5 + 10 mm shaft) is probably too long uncut. **16 mm rotary switches won't fit under a 25 mm deck**, so the stepped controls become 9 mm pots read in firmware steps, as on Big Energy [plat] |
|   | Plan margins | ≈ 0.5–1 mm to the hull wall and 1.25 mm to a Ø 13.5 insert boss: **too tight for printed parts.** In the recommended layout the cells move to the ends anyway |
| 2 | Knob | **No Ø 14–15 knob ≤ 9 mm tall with a published height was found.** Tayda's list has none ≤ 10 mm; Sifam Ø 15.5 is 14.3 tall [chk]. **The Tayda aluminium Ø 10 × 8, 6 mm 18T, $0.59 [chk]** holds 35 with 1 mm to spare at a deck of 25. Black is out of stock until 3 Jan 2027; **gold has 186 in stock**; silver 4 [chk]. A Ø 14.9 knob (family 14.5 × 13.5) makes the module ≈ 40–41 tall |
| 3 | Driver and grille | Driver centre at y ≈ 73 on the axis, frame y 45.5–100.5 at z 8–32: 6 mm of air under the magnet. **The crown's front rake must be ≥ ≈ 63°**, rising 10 mm in ≤ 5 mm from a foot at y 41, or the frame's front edge hits the rake. **The drawn grille (Ø 1.8 holes in a Ø 43 field) gives ≈ 560 mm², which fails 620.** A Ø 46 field with Ø 2.0 holes on 2.6 pitch gives ≈ 770 mm² nominal and ≥ 620 even if holes print 0.2 mm small [calc] |
| 4 | Ported in the crown | **No, confirmed.** The crown's usable box is ≈ 76–92 cm³ net. In it, a port is Ø 12 × 192 mm (29 % of the box) or Ø 10 × 132 mm (13 m/s at 1 W: noisy). The smallest worthwhile ported box is ≈ 120 cm³ (option C) |
| 5 | Weights | **Module (PETG, 2.0 mm walls): ≈ 0.63–0.78 kg as drawn; 0.70–0.85 kg with option E.** ASA is ≈ 40 g lighter, PLA about the same as PETG. The shell is 0.17–0.30 kg depending on walls; it prints solid, so infill barely matters [calc/est] |
|   | Kits | FALLBOARD carry ≈ 0.50–0.55 kg; SPINE ≈ 0.49 kg (both agree with systems' figures); CLOTH 0.23–0.36 kg (cloth only) |
| 6a | Print bed | **A one-piece 280 mm part doesn't fit a 256 × 256 bed at any angle** [calc]. It needs a bed of ≥ ≈ 300 mm (e.g. 300 × 300 and larger machines [est]) or a service. **Better fallback than splitting on the axis:** split at the flush divider lines (x 74.5 / 205.5) into 74.5 + 131 + 74.5. The seams then hide in the divider grooves, the crown stays whole, and the speaker box is a separate printed part ≤ 250 mm long, airtight on its own |
| 6b | ¼"-20 inserts | Standard part: OD 9.5, length 9.5–12.7, hole 8.2, **minimum boss Ø 13.5** [chk, spec sheet]. Prusa / CNC Kitchen sell a 20-pack for $11.99, in stock [chk]. The concept's Ø 14 boss is at the minimum. Ø 16–18 is better for a tripod [est] |
| 6c | FALLBOARD lid | **A 0.8 mm skin with 3 mm ribs on the 35 mm grid isn't stiff on its own** [calc]: ≈ 22–25 mm sag at the centre under a 20 N press on the free span (PETG), and 0.7 mm oil-canning of the skin under a fingertip. It works only as a cover resting on the module rim and the keyboard foam (≈ 7 mm sag over the bed span). A **17.5 mm rib grid** halves the sag; a **1.2 mm skin** fixes the oil-canning (0.2 mm) |
| 6d | SPINE knuckles | **Fine at ≈ 95 N:** bearing stress ≈ 1 MPa, ring tension ≈ 0.8 MPa, against printed PETG's interlayer strength of ≈ 15–30 MPa [est]. That's > 15× margin, and ≥ 4× even if a whole palm (≈ 100 N) leans on it. Use knuckle OD ≥ 9 (3 mm wall), length ≥ 20, a printed Ø 3.3 hole for the Ø 3 rod |
| 6e | Filament | **ASA.** Sun-parked cars measured a 69 °C dashboard, 51 °C seats and 47 °C cabin air after one hour [chk, ASU]. PLA (Tg ≈ 55–60 °C) fails there; PETG (≈ 80 °C) survives a seat; ASA (≈ 95–100 °C) survives the dashboard and resists UV [est]. ASA needs an enclosed printer or a service, and the three-piece split helps against warping. Don't leave floss in a hot car whatever the filament: the lithium cells are the weaker part |
| 7 | Cables | **Flat C-to-C with one right-angle end exists:** Pimoroni, "upwards" and "sideways" versions, 0.2 m or 1 m [chk]. Because a USB-C plug is reversible, **one sideways plug exits left or right, and one upwards plug exits up or down** [calc]. **I found no published flat cable angled at both ends**, so the module end needs either a recessed host-port pocket (≈ 25–30 mm deep for a straight plug) or a marketplace double-angle cable (UNVERIFIED). Neither listed length is in the 0.3–0.5 m range (0.2 is too short; 1 m coils in the pocket) |
|   | Older micro-B Xkey | The C-to-A-receptacle adapter (Rd inside [r2]) plus a USB-A to angled micro-B cable. StarTech lists right-angle and up-angle micro-B versions [chk, listing titles]. The one C-to-micro-B right-angle cable found is the wider **USB 3.0** micro-B: the wrong connector |

**Trade-offs for Adam** (§9):
1. Speaker: E (best, needs the rear region or 115 deep) / D (robust pair, sealed) / C (one ported) / A (as drawn).
2. Knob Ø 10 (35 tall) vs Ø 15 (≈ 41 tall).
3. Filament: ASA (outdoor- and car-proof; needs an enclosed printer or a service) vs PETG (easier; keep it out of hot cars).
4. One-piece print (≥ 300 mm bed or a service) vs a three-piece split at the dividers.
5. FALLBOARD lid: denser ribs or a thicker skin (+≈ 30–60 g) vs a floppy lid that rests on its contents.

---

## 1. The stack at 35 (§11.1)
**Heights from the bottom face** [calc; the cell is 7.5 thick per its listing, plat]:

| Layer | z (mm) | Notes |
|---|---|---|
| Floor | 0–2.0 | printed |
| Cells (2 × 50 × 60 × 7.5) | 2.0–9.5 | |
| Swell / tolerance gap | 9.5–10.5 | Pouch cells grow in service; ≥ 10 % of thickness [est] |
| Board (1.6) | bottom ≥ 10.5 → **top 12.1 minimum** | No bottom-side parts over the cells. In the front band, where there are no cells, bottom parts up to ≈ 8 mm |
| Top-side parts | PCB top → ≤ 23.0 | **6.5–10.9 mm available** (as against r2's 6.5 assumption) |
| Deck (2.0) | 23.0–25.0 | **25, not 26** |
| Knob seat | 25–26 | 1 mm |
| Ø 10 × 8 knob | 26–34 | |
| Rim | 35 | 1 mm over the knob tops |

**Pots and switches:**
- **Board-height window:** a 6.5 mm-bodied pot puts the board top between 12.1 (cells) and 16.5 (body under the deck).
- **Shaft tip** has to be at ≈ 30–33, so the knob grips ≈ 4–7 mm of shaft. So **PCB to shaft tip ≈ 15–21 mm** [calc].
  - Bourns **PTV09A-3**: bushingless vertical, 6.5 mm body, 18-tooth knurl, L 15 mm [chk, [Bourns PTV09](https://www.bourns.com/data/global/pdfs/PTV09.pdf)]. It fits if L is measured from the PCB. If L is from the body top (21.5 total), the board must drop to 11.5, which is 0.6 mm into the swell gap. **UNVERIFIED:** the reference plane is in the drawing, which I couldn't read.
  - Tayda **A-5622**, the family pot: "Shaft Length: 10mm+5mm", body height not stated [chk, [Tayda](https://www.taydaelectronics.com/tayda-10k-ohm-linear-taper-potentiometer-spline-shaft-pcb-mount-9mm.html)]. That's likely ≈ 21.5 total, so it has the same problem and would need cutting (no machining).
  - **Bushingless pots are board-held:** the deck gets clearance holes, and the board is fixed to the shell with standoffs.
- **Stepped controls** (OCTAVE ×2, PRESSURE, SHIMMER): a 16 mm rotary switch's body (≈ 12–15 mm [est]) doesn't fit 6.5–10.9. Use 9 mm pots read in firmware steps (Big Energy's RANGE: "Pico-read pots, 6 firmware detents" [plat]). The cost is no tactile detent, which goes to the designers and the owner as a feel trade-off.
- **Tabs, HOLD, TAP, slides:** check each part's height against 6.5–10.9 at BOM time [est].
- **Jacks and the USB-C on the facets and front face:** their centres sit at ≈ 14–19 mm, which sets the facet openings.

**Plan, as drawn** (cells x 49–109 / 171–231, y 38–88):
- **Hull wall:** the inner wall at x 49 is y 88.7 [calc], so ≈ 0.7 mm.
- **Insert boss:** a Ø 13.5 boss at (60, 30) spans y 23.25–36.75, so 1.25 mm. A Ø 16 boss touches.
- **Speaker box:** the crown box needs ≥ 56 mm inside for the Ø 55 frame. With 1.6 mm walls its outside is x 110.4–169.6, so ≈ 0.4–1 mm to the cells.
- **Verdict: the stack fits in height, but the plan margins are below printed-part tolerance** (±0.2–0.5 [est]) plus the pouch tolerance. Give ≥ 2 mm on each side, or move the cells (as option E does, §8).

**The U-shaped board:** fine electrically. Its arms over the cells carry only low parts and the facet jacks.

## 2. Knob (§11.2)
| Knob | Size | Published height | Holds 35? | Source |
|---|---|---|---|---|
| **Tayda aluminium 3010, 6 mm 18T** | Ø 10 | **8 mm** | **Yes: deck 25, top 34, rim 35** | [chk: [black](https://www.taydaelectronics.com/aluminum-d-shaft-knob-3010-black-6-x-18t.html), out of stock to 3 Jan 2027; [gold](https://www.taydaelectronics.com/aluminum-gold-knob-3010-black-6-x-18t.html), 186 in stock; [silver](https://www.taydaelectronics.com/aluminum-silver-knob-3010-black-6x18t.html), 4] |
| Thonk Stubby, T18 | Ø 9.85 | 11 mm | No | [chk, [Thonk](https://www.thonk.co.uk/shop/stubby-knobs-t18/)] |
| Sifam S150006 collet | Ø 15.5 | 14.3 mm | No (being discontinued at RS) | [chk, [RS](https://uk.rs-online.com/web/p/potentiometer-knobs/0225710)] |
| Tayda's knob list (page 5) | Ø 13–16 | **none ≤ 10 mm** | No | [chk, [Tayda](https://www.taydaelectronics.com/hardware/knobs.html?p=5)] |
| Family 18T push-on | Ø 14.5 | 13.5 mm | No: rim ≈ 40 | [plat] |

- **Engagement:** the Ø 10 knob's bore depth isn't published (UNVERIFIED). CATHEDRAL assumed ≈ 7 mm of shaft above the plate [plat]; §1's window allows 4–7.
- **A printed Ø 15 × 8 knob** is allowed by the printing rule, but a push fit on an 18T spline needs a fitting trial, so it's UNVERIFIED. Not recommended.

## 3. Driver and grille (§11.3, §11.4)
**Driver (TEBM28C10-4B, Ø 55, 24.00 deep [chk r2]):**
- centre on the axis at y ≈ 73: frame y 45.5–100.5 against the rear wall's inside at 100.9;
- frame top at z ≈ 32: crown top 35 − 2 skin − 1 gasket;
- magnet bottom at z ≈ 8: 6 mm above the floor (≥ 3 needed) [calc].

**The rake:** the crown foot is at y 41 (Ø 10 layout, 5 mm finger room). For the rake's underside to clear the frame's front point (z 32 at y 45.5), the rake must reach z 34 by y 45.5. That means a 10 mm rise in ≤ 5 mm, about **63° or steeper** [calc]. A 45° rake would need the foot at y ≈ 36.5, which takes the finger room.

**Grille:**
- **As drawn:** Ø 1.8 holes on 2.6 pitch in a Ø 43 field: 221 holes ≈ 560 mm². **Fails** the ≥ 620 mm² rule (≥ 73 % of Sd [r2]).
- **Pass:** a **Ø 46 field with Ø 2.0 holes on 2.6 pitch**: ≈ 245 holes, ≈ 770 mm² nominal, ≥ 620 if the holes print Ø 1.8 [calc]. The field spans y 50–96, inside the crown top.
- **For option E:** two fields, each ≥ 620 mm².

**Ported in the crown (§11.5): no.**
- The crown's whole volume (y 43–101, 70 wide, 31 tall) is ≈ 129 cm³ gross, ≈ 92 net at best (76 as drawn) [calc].
- A port tuned for it is Ø 12 × 192 mm (22 cm³, 29 % of a 76 cm³ box) or Ø 10 × 132 mm (13 m/s at 1 W, ≈ 19 m/s at 2 W: audible) [calc, `best_*` / sweep].
- The smallest box where a port pays off is ≈ 120 cm³ (option C).

## 4. Weights (§11.6)
**Shell surface** [calc]: top and bottom 2 × 262 cm² (hull plan 26,210 mm²) + perimeter 712 mm × 35 = 249 cm² + crown sides 20 + inner speaker-box walls (≈ 62 as drawn, ≈ 90 for E). Total **≈ 855 cm²** (E ≈ 880), +15 % for bosses, ribs and standoffs.

Walls this thin print as perimeters and skins, effectively solid, so infill matters only in bosses.

| Walls | PLA (1.24) | PETG (1.27) | ASA (1.07) g/cm³ [est] |
|---|---|---|---|
| 1.6 mm | 195 g | 200 g | 168 g |
| **2.0 mm** | **244 g** | **250 g** | **210 g** |
| 2.4 mm (rugged) | 293 g | 300 g | 252 g |

**Contents:** ≈ 378–528 g, rev 2's 418–608 with lighter controls: 13 Ø 10 aluminium knobs and 9 mm pots, 6 tabs, 3 buttons ≈ 60–110 g [est]. Option E adds a second driver (58 g [chk]) and a second amp channel: +≈ 63 g.

| Module | PETG 2.0 | ASA 2.0 |
|---|---|---|
| As drawn (A) | **0.63–0.78 kg** | 0.59–0.74 kg |
| Option E | **0.70–0.85 kg** | 0.66–0.81 kg |

**Kits' printed carries** [calc/est, my shell model against systems' files]:

| Kit | Parts | Mass |
|---|---|---|
| FALLBOARD | tray floor 412 × 265 × 1.2 + walls ≈ 37 tall + socket and end blocks + ribbed lid (0.8–1.2 skin) ≈ 375–420 cm³ PETG, + hinges and magnets | **≈ 0.50–0.55 kg** (systems: 0.52–0.60) |
| SPINE | two trays, spine, knuckles ≈ 305 cm³ PETG + rods 46 g + end blocks + strap | **≈ 0.49 kg** (systems: 0.42–0.52) |
| CLOTH | cloth only (the core is the printed module) | **0.23–0.36 kg** [r2] |

In ASA, the printed parts are ≈ 16 % lighter.

## 5. Printing (§11.7, §11.8 and the kits)
**Bed size:**
- A 280 × 105 part can't be rotated to fit a 256 × 256 bed at any angle [calc]. At θ = 60° one side needs 295 mm.
- Typical beds [est, makers' published sizes, not re-read]:
  - 220 × 220 (Ender-3 class);
  - 250 × 210 / 250 × 220 (Prusa MK4S / Core One);
  - 256 × 256 (Bambu A1 / P1 / X1);
  - 300 × 300 (Creality K1 Max);
  - 350 × 320 (Bambu H2D);
  - 360 × 360 (Prusa XL).
- So: a ≥ 300 mm machine, or a service.

**Split:**
- **Recommended:** at the flush divider lines x 74.5 and 205.5, into three parts of 74.5, 131 and 74.5 mm.
  - It uses divider option 1 (a groove) as the seam, so the joint reads as a designed line.
  - The crown and its box stay whole.
  - Keyed lap joints + M3 screws into heat-set inserts [est, standard practice].
- **On the axis (systems' fallback):** this cuts through the crown and the speaker box, so the seam would have to be airtight. Not recommended.
- **Make the speaker box a separate printed part**, airtight on its own (≥ 3 perimeters, gasketed lid). Then shell seams can't leak. E's box is ≈ 240 mm long, which fits a 256 bed.

**¼"-20 inserts:**
- **Dimensions:** OD 0.375" (9.5 mm), length 0.375–0.500" (9.5–12.7 mm), hole 0.323" (8.2 mm), **minimum boss OD 0.531" (13.5 mm)** [chk, [heat-set insert specs](https://www.albanycountyfasteners.com/media/64/3d/5a/1764619189/heat-set-insert-specs.pdf)].
- **Product:** Prusa "Heat Set Inserts 1/4" (CNC Kitchen design), brass, 20 pieces for $11.99, in stock [chk, [Prusa](https://www.prusa3d.com/product/heat-set-inserts-1-4-20-pcs/)]. A tapered alternative is McMaster 93365A160 (min. material thickness 0.33") [chk, [drawing](https://medesignlab.me.wisc.edu/wp-content/uploads/sites/2200/2024/08/1-4-20-Heat-Set-Insert-Part-Drawing.pdf)].
- **Boss:** ≥ Ø 13.5; Ø 16–18 for tripod torque [est]. Height ≥ insert length + 1.5.

**FALLBOARD lid** [calc]: two-way plate model (Timoshenko's coefficients for a simply supported plate under a central load) with T-section ribs, E ≈ 2.0 GPa for printed PETG / ASA and 3.3 GPa for PLA [est]. Load: 20 N at the centre.

| Lid build | Free span 404 × 257 (PETG) | Over the bed 404 × 137 | Skin between ribs, 10 N fingertip |
|---|---|---|---|
| 0.8 skin + 3.0 ribs, 35 grid | 25 mm | 7.8 mm | 0.73 mm |
| 0.8 skin + 3.2 ribs, **17.5 grid** | 12 mm | 3.8 mm | 0.18 mm |
| **1.2 skin** + 2.8 ribs, 35 grid | 20 mm | 6.2 mm | 0.22 mm |
| 1.2 skin + 2.8 ribs, 17.5 grid | 12 mm | 3.7 mm | — |

- PLA is ≈ 40 % stiffer, but fails outdoors (§6).
- **What it means:** with 4 mm of rib depth, no printed lid this size is stiff on its own. It's a cover that bears on the module rim (the knobs are below it) and the keyboard foam. The 17.5 mm grid adds ≈ 30–60 g [est].

**SPINE knuckles at 95 N** [calc]:
- **Bearing:** 95 N / (3 mm × 30 mm) ≈ 1 MPa.
- **Ring tension and tear-out** with a 3 mm wall × 20 mm length: ≈ 0.8 MPa.
- **Stop face** in compression: 570 N over 412 × 5 mm ≈ 0.3 MPa.
- **Strength:** printed PETG ≈ 15–30 MPa across layers [est], so the margin is > 15×. Even a 100 N lean (≈ 475 N per knuckle) keeps ≈ 4×.
- **Spec:** OD ≥ 9 mm, length ≥ 20 mm, printed Ø 3.3 hole (a free fit; no reaming), Ø 3 steel rod.
- **Not modelled:** creep under a load held for a long time, and fatigue (UNVERIFIED). The margin is the design-around.

## 6. Filament for outdoors and the car
**Measured car temperatures, after one hour in the sun:** cabin 116 °F (47 °C), dashboard 157 °F (69 °C), seats 123 °F (51 °C). In the shade: 100 °F (38 °C), 118 °F (48 °C), 105 °F (41 °C) [chk, [ASU study](https://news.asu.edu/20180516-discoveries-asu-study-hot-cars-can-hit-deadly-temperatures-within-one-hour)].

| Filament | Glass transition [est, typical datasheets] | Hot car | Sun / UV | Printing |
|---|---|---|---|---|
| PLA | ≈ 55–60 °C | Fails on the dashboard; creeps on a seat | Degrades | Easiest |
| PETG | ≈ 80 °C | Survives a seat; marginal on the dashboard | Moderate | Easy, open printer |
| **ASA** | ≈ 95–100 °C | Survives the dashboard | **Made for outdoor UV** | Enclosed printer (warping, styrene fumes: ventilate) or a service |

**Recommendation: ASA** for the module and the rigid carries; PETG is acceptable if floss stays out of hot cars and long sun. Lithium cells shouldn't sit at dashboard temperatures in any case [est], so "not on the dashboard" is the rule whatever the filament.

## 7. Cables (§11.9)
**Flat C-to-C, right angle:**
- Pimoroni "Flat USB-C to USB-C Right Angle Cable": a regular plug on one end and an **upwards-pointing** right-angle plug on the other; 0.2 m or 1 m; USB4 [chk, [Pimoroni](https://shop.pimoroni.com/products/flat-usb-c-to-usb-c-right-angle-cable)].
- Pimoroni sideways version: a **sideways-pointing** right-angle plug [chk, [Pimoroni](https://shop.pimoroni.com/en-au/products/flat-usb-c-to-usb-c-sideways-right-angle-cable)].
- USB4 cables carry USB 2.0. The e-marker needs VCONN only for itself; data works without it [est].

**Which way it exits:** a USB-C plug works either way up, so a sideways plug exits left *or* right by flipping it, and an upwards plug exits up *or* down [calc].
- A keyboard socket on its rear face, long axis horizontal, takes the **sideways** version to run along the lane.
- The orientation of each keyboard's socket is UNVERIFIED (r2 §6).

**Gaps:**
- **No published flat cable with both ends angled.** The module end needs either:
  - a **recessed host-port pocket** ≈ 25–30 mm deep for a straight plug [est] (it costs internal space at the front-centre); or
  - a marketplace double-angle cable (UNVERIFIED).
- **Length:** 0.2 m is too short (≥ 0.3 needed [r2]); 1 m coils in the pocket.

**Older micro-B Xkey:**
- The C-plug-to-A-receptacle adapter (Rd by spec [r2]) + **StarTech USB-A to right-angle or up-angle micro-B** (listing titles [chk, [CDW right-angle](https://www.cdw.ca/product/startech.com-3-ft-91cm-micro-usb-cable-a-to-right-angle-micro-b-usb-t/2053774), [CDW up-angle 0.5 m](https://www.cdw.ca/product/StarTech.com-0.5m-Micro-USB-Cable-A-to-Up-Angle-Micro-B-USB-cable-50/3115153)]).
- The C-to-right-angle-micro-B cable I found is **USB 3.0 micro-B** [chk, [listing](https://www.newegg.com/p/181-08T5-001P2)], a wider plug that won't fit a USB 2.0 socket.

---

## 8. What will sound best (owner: "idc method")
**What "best" means here:** a string machine's ensemble and pads put their energy in **150–800 Hz**, with octave-down fundamentals at 65–130 Hz (C2–C3). It plays **outdoors**, where there's no room gain, and **on battery**. So the scores are:
- output per watt in 150–800 Hz (loudness and runtime);
- clean headroom at 100–200 and 200–800 Hz;
- extension (f3, f6);
- robustness to what the model can't see.

**Method:** `eng/speaker-sim/sim_best.py`, the r2 lumped model plus:
- the **PUI AS06504PS-X-R** (65 mm, 36.7 mm deep; Re 3.32, Fs 132, Qts 0.374, Vas 0.188 L, BL 4.283, Mms 2.658 g, Xmax 4.75 mm) [chk, [datasheet](https://cdn.components.ru/media/PDF/7681679.pdf), [PUI](https://www.puiaudio.com/products/as06504ps-x-r)];
- **pairs**: two drivers in one box, each on its own 2 W channel (modelled as their parallel equivalent).

Outputs: `best_compare.png`, `best_tolerance.png`, `best_summary.csv`. 200 tolerance draws per option.

| Opt | Speaker | Net box | dB/W 150–800 | f3 / f6 | Clean max 100–200 / 200–800 | W for 80 dB | Spread | Module-size cost |
|---|---|---|---|---|---|---|---|---|
| A | 1 × TEBM28, sealed | 76 | 77.8 | 255 / 190 | 73.2 / 81.8 | 1.66 | 1.1 | As drawn |
| B | 1 × TEBM28, ported | 76 | 80.1 | 167 / 140 | 76.9 / 83.6 | 0.97 | 2.5 | **Not buildable:** port Ø 12 × 192 mm |
| C | 1 × TEBM28, ported (Ø 12 × 155) | 120 | 79.9 | 140 / 118 | 79.4 / 83.1 | 1.03 | 2.9 | Crown + ≈ 25 mm wings each side; cells relocate. Holds 280 × 105 × 35 |
| D | 2 × TEBM28, sealed | 150 | 80.8 | 255 / 190 | 79.2 / 87.8 | 0.83 | **1.1** | Crown ≈ 125 wide (two grilles about the axis); cells and board out of the rear. Holds 280 × 105 × 35 |
| **E** | **2 × TEBM28, ported (Ø 16 × 140, flared)** | **190** | **83.2** | **152 / 131** | **84.0 / 89.5** | **0.48** | 2.7 | **The whole rear region** (≈ 323 cm³ gross behind the rear row [calc]); cells to the ends; two stacked boards in the front band. Holds 105 with ≈ 4 % margin; **safe at ≈ 115 deep** |
| E2 | 2 × TEBM28, ported | 250 | 82.8 | 138 / 117 | 85.4 / 89.1 | 0.52 | 2.9 | ≈ 280 × 120 × 35 |
| G | 1 × AS05804PS, ported | 150 | 80.2 | 129 / 108 | 80.4 / 83.4 | 0.95 | 2.8 | **Body ≈ 42** at the crown |
| H | 2 × AS05804PS, ported | 250 | 83.4 | 138 / 116 | 85.6 / 89.7 | 0.46 | 2.7 | Body ≈ 42, ≈ 280 × 120 |
| I | 1 × AS06504PS, sealed | 150 | 79.8 | 277 / 194 | 75.7 / 83.8 | 1.05 | 1.0 | Body ≈ 45, crown ≈ 74 wide, ≈ 110 deep |
| J | 1 × AS06504PS, ported | 200 | 81.9 | 135 / 117 | 81.6 / 85.1 | 0.65 | 3.1 | Body ≈ 45, ≈ 110 deep |

All [calc]. "Spread" is the 10–90 % band width (dB) between 90 and 400 Hz.

**Why E:**
- It's best or near best on every sound measure that matters for pads: the most output per watt in the low mids and the most clean headroom. Only H matches it, and H needs a 42 mm body.
- It keeps the 35 mm height and the TEBM28's wide balanced-mode dispersion, which suits listeners sitting around it outdoors.
- Two drivers halve each one's excursion for the same output, which is lower distortion on loud chords.
- **Battery:** at a typical outdoor level, the speaker's draw drops to ≈ 30 % of A's.

**What E costs:**
- **Layout:** the speaker box takes the whole rear region. The cells move under the jambs at the two ends, and the electronics become two stacked boards in the front band (each up to ≈ 260 × 36, ≈ 18,700 mm² in total against the 16,000 needed).
- **The S4 inserts at x 60 / 220** sit close to end-mounted cells, so the inserts, the cells or the family's 160 mm spacing has to give a few mm. That's a designer and family call.
- **Faces:** a ≈ 125 mm crown with two grilles, symmetric about the axis (PRINCIPLES §6 is satisfied).
- **Parts:** +1 driver ($25 [chk r2]) and a 2-channel class-D amp (e.g. 2 × 3 W into 4 Ω at 5 V, PAM8403 class [est, datasheet not re-read]). About +$27–30.
- **Weight:** +≈ 63 g.

**Designed around what the model can't capture:**
- **Port noise and compression:** flared ends (radius ≈ 8 mm, printed), and peak air speed 8.2 m/s at 1 W, ≈ 16 m/s only at full 4 W right at Fb.
- **Box losses and leaks:** conservative tuning. The sweep's no-hump rule means real losses make the bass shelf sag a little rather than boom. The box is a separate airtight printed part with a gasketed driver seat.
- **Excursion below Fb:** a second-order high-pass at ≈ 115 Hz on the speaker feed only (phones stay full range).
- **Two units that differ:** each driver's ± 20 % compliance averages out in the pair. The model's spread includes it.
- **Lobing from two drivers:** with centres ≈ 62 mm apart, no off-axis cancellation below ≈ 2.8 kHz [calc, c / 2d]. Above that there's mild comb-filtering off-axis. Pads carry most of their energy below it. **Not modelled:** the lobing itself, diffraction, and the lap or the ground.
- **No passive radiator:** the only thin one has no published excursion, and the DMA58-PR is 38 mm deep [r2].

**If E's layout is too much:**
- **D** keeps two crowns' worth of headroom with the best robustness, but no extra bass.
- **C** gives most of the bass gain with one driver.
- **A** stays the minimum.

## 9. Trade-offs for Adam
| # | Question | Options | Engineering view |
|---|---|---|---|
| 1 | Speaker | **E** (best: +5 dB per watt, f3 152, +8–11 dB headroom; rear region or ≈ 115 deep) / D (robust pair, sealed) / C (one ported, 120 cm³) / A (as drawn) | **E**; D if the layout can't free the rear region |
| 2 | Knob | Ø 10 × 8 (35 tall; gold in stock) / Ø 14.5 (≈ 40–41 tall) | Ø 10 keeps 35 |
| 3 | Stepped controls | Firmware-stepped 9 mm pots (fit 35, no detent feel) / rotary switches (need ≈ +5 mm of height) | Pots |
| 4 | Filament | ASA (outdoor- and car-proof; enclosed printer or service) / PETG (easier; keep out of hot cars and long sun) | ASA |
| 5 | Printing | One piece on a ≥ 300 mm bed or a service / three pieces split at the dividers | Either; the split at the dividers if printing at home on a 256 bed |
| 6 | FALLBOARD lid | Denser ribs or a thicker skin (+30–60 g, stiffer) / today's (a cover resting on its contents) | 17.5 mm grid |
| 7 | Cable at the module end | A recessed host-port pocket / a marketplace double-angle cable (UNVERIFIED) | Pocket |

## 10. What changes from `module-r2.md`
- **Speaker recommendation:** r2's "sealed, most robust" answered "without measuring". The owner now asks for "sounds best", so the answer is **E**, with r2's sealed box as fallback D/A.
- **Deck at 25**, firmware-stepped pots, and a pot of ≤ 21 mm from PCB to shaft tip.
- **Weights:** a printed module of 0.63–0.85 kg (r2: 0.67–0.93, a different shell model).
- **Speaker-sim:** `sim_best.py` added; `sim.py` is unchanged.
