# Cost estimate: portable Model D-style voice, two build versions

Prepared 2026-11-12 for the owner (Lynchburg, VA). Scope: **Tier 1** MIDI control (architecture.md section 5e.3), Hall-sensed 25-key Delrin flexure keyboard, ~50 mm speaker, 2x 18650, ~300x210 mm laser-cut stack body (jam.md Turns 5-6).

**Read this first**
- **Version A (factory-assembled): about $1,644-3,531.** **Version B (hand-soldered kit): about $1,152-2,472.** Planning figures (about 40% of the way up each range): A ~$2,399, B ~$1,680. These exclude tools, makerspace usage fees and sales tax.
- Every line says where its price came from. **ESTIMATE** means I could not retrieve a live price; the basis is stated. Well over half of the dollars are ESTIMATE-grade, because JLCPCB's quote tool and DigiKey/Mouser pages could not be read from here. The firm numbers are in the tariff section and a handful of parts.
- Before ordering anything, run the final Gerbers/BOM through JLCPCB's instant quote. That one step replaces most ESTIMATE lines with real numbers.
- **Version A still needs a soldering iron.** JLC assembles only SMD (and can hand-solder catalogue through-hole parts at $0.0164/joint, but not the owner's chosen pots/jacks/faders unless they are consigned). The panel parts (~250 joints), the Pico 2 module and, unless consigned, the AS3046D arrays are hand-installed. See sections 3 and 7.

## 1. Assumptions (change these and the totals move)

| Item | Assumption | Basis |
|---|---|---|
| Boards, A | Core ~110x85 mm 4L; voice/panel ~290x170 mm 4L (SMD on back, through-hole panel parts on front, per systems.md S3); keyboard ~285x55 mm 2L (25 keys at 18 mm pitch = ~270 mm) | Sizes are my ESTIMATE from the form factor; no board outlines exist yet |
| Boards, B | Same core; voice board through-hole 290x170 mm (2L low, 4L high); keyboard 2L with TO-92 Hall sensors; plus a ~60x45 mm castellated 'control module' (8 digipots, muxes) that JLC assembles, per architecture.md section 5e.3 | architecture.md 4.4, 5e.3 |
| Quantities | JLC bare-board minimum 5 of each; PCBA assumed minimum 2 of each (ASSUMED: JLC's capabilities page states a 2-50 range only for Economic; verify the standard-PCBA minimum at quote time) | https://jlcpcb.com/capabilities/pcb-assembly-capabilities (2026-11-12) |
| MIDI tier | Tier 1: 7-8 high-voltage digipots, a second DAC8568, MCU-rendered contours. No analog contour board, no PhotoMOS | architecture.md 5e.3 |
| Sourcing | JLC places only parts in its/LCSC's catalogue or Global Sourcing; others are consigned (A: AS3046D) or hand-soldered | https://jlcpcb.com/help/article/consignment-part-terms-conditions (2026-11-12) |
| Not included | Tools (section 7), makerspace laser/printer fees (unknown), Virginia sales tax, your time, firmware, a rev 2 | |

Two inconsistencies in architecture.md that affect cost: section 5b adds a **MCP4822** as the second DAC while section 5e.3 adds a **second DAC8568** (+$17). I priced the DAC8568 (the higher number). Section 4 specifies a Pico 2 *module* on the core board; JLC cannot place a module unless consigned, so I priced hand-soldering it. A bare RP2350 + flash + crystal on the core board (about $2-3 of parts) would let JLC place the MCU and is worth an eng decision.

## 2. US import tariffs on China PCBs and PCBA, as of 2026-11-12

The rules changed repeatedly in 2026. Sources are secondary (law-firm/trade-compliance/PCB-vendor write-ups); the Federal Register notice itself blocked my fetch, so the PCB-specific coverage of the November extension is inferred and marked as such.

| Layer | Status | Source (checked 2026-11-12) |
|---|---|---|
| De minimis | Suspended; do not assume $800 duty-free. JLC also says US orders do not go by post, so value does not matter | https://www.ourpcb.com/blog/china-us-pcb-tariffs-2026 (Jun 2026); https://jlcpcb.com/news/logistics-update-us-china-tariff |
| IEEPA 'reciprocal' + fentanyl tariffs | Struck down by the Supreme Court on 2026-02-20; JLC removed them 2026-02-24 | https://octopart.com/pulse/p/tariff-reset-pcb-workarounds (2026-04-14); https://www.atlaspcb.com/news/news-pcb-tariff-section-301-exclusion-expiry-november-2026/ (2026-08-21) |
| Section 122 10% surcharge | 2026-02-24 to 2026-07-24, then expired (150-day limit) | same two sources; https://www.morganlewis.com/zh-cn/pubs/2026/07/us-administration-rebuilds-global-tariff-program-under-section-301 |
| **New Section 301 'forced-labor' tariff** | **12.5% on China, in force since 2026-07-24**, additive to legacy 301 duties. No sunset found | https://zonos.com/docs/guides/country-guides/united-states/section-301-forced-labor |
| **Legacy Section 301 (lists 1-3/4A)** | 25% on bare PCBs (HTS 8534.00) **unless excluded**. 2- and 4-layer rigid boards are excluded (HTS 9903.88.69). **PCBA with parts is not eligible**, so it pays 25% | AtlasPCB (above); https://www.ourpcb.com/blog/china-us-pcb-tariffs-2026 |
| Exclusion expiry | Was 2026-11-09. **USTR extended all 178 exclusions on 2026-11-10 to 2027-01-09** (entries from 2026-11-10 through 11:59 pm ET 2027-01-09). The sources do not name PCBs; I infer 2/4-layer boards are included because the extension covers all of 9903.88.69 | https://www.ghy.com/trade-compliance/ustr-extends-section-301-product-exclusions-china ; https://gingercontrol.com/briefings/ustr-extends-178-china-section-301-exclusions-under-9903-3888a94e ; FR notice 2026-22925 (not readable here) |
| **Resulting legal rate** | Bare 2/4-layer boards: **12.5%** until 2027-01-09, then **37.5%** if not renewed. **PCBA: 37.5%** (25% + 12.5%) | derived; classification (HTS 8537/8543/8473) of this PCBA is unconfirmed |
| **What JLC actually collects** | DDP prepay at an average rate by product: **PCB 35%, SMT (PCBA) 35%**, stencil 90%; 'for orders charged in the 35%-90% range we will not refund or charge the difference'. JLC's FAQ also lists a 'Section 122 12.5%' line dated 2026-07-24 that contradicts the sources above, and its rate table is an image I could not read. The page is dated 2026-10-29 but the PCB/SMT rates are from 2026-03-17 | https://jlcpcb.com/news/logistics-update-us-china-tariff ; https://jlcpcb.com/help/article/us-tariff-policy-faq |

**Planning rule used above:** 35% (low) to 40% (high) of the JLC order value, which includes the parts JLC supplies, because PCBA duty applies to the whole assembled value (a maker write-up states the same; https://pamfinds.pages.dev/guides/pcb-tariffs-us-makers-2026/, 2026-04/05). Shipping is normally outside the dutiable value but JLC's base is not documented; this is a risk to the low end.

Sensitivity of duty alone, on the JLC subtotal:

| Rate | Version A duty | Version B duty |
|---|---|---|
| 12.5% (bare boards only, exclusion holds) | $105-194 | $54-101 |
| 25% | $210-387 | $109-203 |
| 35% (JLC prepay) | $295-542 | $152-284 |
| 37.5% (legal PCBA stack) | $316-581 | $163-304 |
| 50% (tail risk, e.g. semiconductor-type action) | $421-775 | $218-405 |

Tariff levers, in order of usefulness: (1) the design is not frozen, so boards will almost certainly be entered after 2027-01-09, so plan for 37.5% on bare boards too unless USTR extends again; (2) ship via your own DHL/FedEx account (non-DDP), where CBP charges the legal rate rather than JLC's flat average, which could help bare boards (12.5%) but adds brokerage fees (JLC says self-use accounts were unaffected by its DDP policy; https://jlcpcb.com/news/logistics-update-us-china-tariff); (3) keep the JLC order small: only boards that truly need SMD assembly go to JLC, and hand-solderable boards use bare PCBs. That is why B's duty is about half of A's. Also watch Section 232 semiconductor actions as a tail risk (Octopart notes up to 50% on China semiconductors, which applies to chips, not obviously PCBA).

## 3. Version A: factory-assembled (JLC PCBA on all boards; owner installs panel parts and enclosure)

| Line item | Qty | Total (low-high) | Source and date checked, or ESTIMATE basis |
|---|---|---|---|
| **JLCPCB order (China-origin; tariff applies)** | | | |
| PCB fab: core board 110x85 mm, 4-layer | 5 pcs | $18-35 | ESTIMATE (JLC live quote needs Gerbers). Basis: list ~$70.6/m2 4-layer https://jlcpcb.com/blog/special-discount-on-quality-4-layers-pcbs (2024-03) x small-lot multiple + eng/setup |
| PCB fab: voice/panel board ~290x170 mm, 4-layer | 5 pcs | $60-150 | ESTIMATE. Basis as above; 0.25 m2 total area; >100x100 loses the promo price; JLC Aug-2026 notice says prices in effect but gives no table https://jlcpcb.com/news/jlcpcb-fr4-pcb-price-adjustment-august2026 (2026-11-12) |
| PCB fab: keyboard board ~285x55 mm, 2-layer | 5 pcs | $12-30 | ESTIMATE. Basis: 2-layer list ~$43/m2 at volume https://jlcpcb.com/blog/jlcpcb-discounts-for-large-pcb-orders (2024-07) x small-lot multiple |
| PCBA fees: core (setup, stencil, fixtures, loading, joints) | 2 pcs | $90-160 | Fee schedule https://jlcpcb.com/help/article/pcb-assembly-price (2026-11-12): std setup $25.56/$51.12 (1/2 side), stencil $8.21/$16.42, fixtures $16.42 (<30 pcs), loading $1.53 per part (ambiguous: extended-only vs all unique parts), SMT $0.0016/joint. Part counts ESTIMATE |
| PCBA fees: voice/panel (double-sided assumed) | 2 pcs | $180-370 | Same schedule. ~150 unique parts (~60 extended) x $1.53 = $92 low, all 150 = $230 high, + $51.12 setup + $16.42 stencil + $16.42 fixtures + joints (~2,000/board) + handling. Max PCBA single-board 460x500 mm OK https://jlcpcb.com/capabilities/pcb-assembly-capabilities |
| PCBA fees: keyboard board | 2 pcs | $60-95 | Same schedule; ~15 unique parts, single-sided |
| SMD parts: core (2x DAC8568, ADC, TPS65131, charger, 2 LDOs, buck, class-D, MIDI opto, USB-C, passives) | 2 boards | $138-198 | DAC8568 $17.3811 qty 1, 633 in stock https://www.lcsc.com/product-detail/C524819.html (2026-11-12). Other ICs/passives ESTIMATE ($28-50 + ADC $6-14 per board); architecture.md part choices are mostly UNVERIFIED. Pico 2 excluded (hand-soldered, below) |
| SMD parts: voice board (8 digipots, op-amps, LSK489 x3, mux, comparators, ~65 transistors, ~330 R, ~120 C, LDO/ref) | 2 boards | $240-428 | ESTIMATE ($120-214 per board). Digipots 8 x $6-9 = $48-72/board: AD5293 is $3.91 @1k per ADI (via architecture.md) but qty-1 price could not be retrieved; LCSC AD5293 C578171 is out of stock https://lcsc.com/product-detail/Digital-Potentiometers_Analog-Devices-AD5293BRUZ-50_C578171.html (2026-11-12); MCP41HV51 $3.3113 but only 21 in stock https://www.lcsc.com/product-detail/C637063.html (2026-11-12). Parts not at LCSC need JLC Global Sourcing (no service fee listed, price markup unknown) |
| SMD parts: keyboard board (27 SOT-23 Hall sensors, 2x 16-ch mux, RP2040/flash/xtal, passives) | 2 boards | $44-84 | ESTIMATE. Hall: SS49E $0.2796 https://lcsc.com/product-detail/Hall-Sensor_Honeywell-SS49E_C85697.html and DRV5055A4 $0.356 https://www.lcsc.com/product-detail/Linear-Hall-Sensors_Texas-Instruments-DRV5055A4QLPGM_C266125.html (both TO-92, 2026-11-12); SOT-23 variants assumed $0.45-0.9 ea (not checked) |
| *Subtotal, JLC order (tariff base)* | | *$842-1,550* | |
| **US import duty prepaid by JLC (DDP)**: 35% low / 40% high of the JLC subtotal | | $295-620 | JLC table: PCB 35%, SMT 35% https://jlcpcb.com/news/logistics-update-us-china-tariff (2026-11-12, rates dated 2026-03-17). High = 37.5% legal stack, rounded up. See section 2 |
| **Other electronics sourced outside JLC** | | | |
| AS3046D SOIC-14 transistor arrays (6/board, 2 boards + 2 spares). Not stocked by LCSC/JLC | 14 ea | $80-238 | Low: ~$5-7 ea (Electric Druid AS3046 is EUR 4.50 ex-VAT qty 1-9 https://electricdruid.net/product/as3046-matched-transistor-array/ , 2026-11-12; SOIC price from Erica Synths not shown) + owner hand-solders 12 SOIC-14 (breaks 'factory-assembled'). High: consign to JLC: $85 per <=50 part numbers (https://jlcpcb.com/help/article/consignment-part-terms-conditions, 2026-11-12) + ~$55 ESTIMATE shipping to Shenzhen; consigned parts cannot ship with the PCBs |
| Pico 2 module (hand-soldered castellated, 1 + 1 spare) | 2 ea | $6-12 | $5.75 https://www.sparkfun.com/raspberry-pi-pico-2.html (2026-11-12). JLC can't place it unless consigned |
| **Panel hardware (same in both versions)** | | | |
| Rotary pots, 9 mm PCB (15 panel + 2 wheel) | 17 ea | $11-37 | Low: Tayda $0.67 ea https://www.taydaelectronics.com/10k-ohm-linear-taper-potentiometer-round-knurled-plastic-shaft-pcb-9mm.html (2026-11-12). High: ESTIMATE ~$2.2 ea for genuine Alpha/Mouser-class parts; 1 MΩ audio ext-in pot included |
| Contour faders, PCB-mount ~30 mm, M2 threaded | 6 ea | $12-27 | ESTIMATE $2-4.50 ea. Basis: Tayda's only listed fader is a $2.30 60 mm dual with stock of 1 (2026-11-12, https://www.taydaelectronics.com/catalogsearch/result/?q=slide+potentiometer+45mm); TT PS30/PS45 class on DigiKey/Mouser not price-checked (DigiKey fetch blocked) |
| Knobs / fader caps (15 rotary; 6 fader caps printed; 2 wheels printed in item below) | 15 ea | $10-40 | ESTIMATE $0.6-2.6 ea (plastic Tayda-class to machined). No live knob listing retrieved |
| Rotary switches 6-pos (range x3, waveform x3) | 6 ea | $9-24 | ESTIMATE $1.5-4 ea; not price-checked |
| Toggle/slide switches, mini SPDT PCB-mount | 16 ea | $11-40 | Low: Tayda $0.68 ea https://www.taydaelectronics.com/mini-toggle-switch-spdt-on-off-on-pc-thru-hole.html (2026-11-12). High: ESTIMATE ~$2.5 ea (C&K/E-Switch class) |
| 3.5 mm jacks (12 mono + 3 stereo: phones, MIDI in/out TRS) | 15 ea | $8-14 | Thonk Thonkiconn mono GBP 0.38 (GBP 0.31 at 50+), stereo GBP 0.49 https://www.thonk.co.uk/shop/thonkiconn (2026-11-12); converted ESTIMATE ~$0.5-0.9 ea. UK vendor: see duty/shipping line |
| Power slide switch, TUNE button, RGB/charge LEDs | lot | $3-8 | ESTIMATE |
| **Keys** | | | |
| Neodymium disc magnets 3x1 mm (25 + spares) | 1 x 100-pk | $7 | https://www.apexmagnets.com/3mm-x-1mm-disc-neodymium-magnet (2026-11-12) $6.99/100, N48. Magnet size must match the Hall design; ESTIMATE-level until the sensor/magnet CAD is frozen |
| Delrin (acetal) sheet for flexure comb, ~12x24 in | 1 sheet | $18-40 | ESTIMATE. McMaster product pages (e.g. 8573K13) show no price in fetch (2026-11-12). Thickness is not specified in jam.md; Vector Space wiki lists Delrin for its CO2 lasers but another makerspace wiki says <=2 mm only and messy (https://wiki.acemakerspace.org/laser-cutter-materials/). SendCutSend Delrin only in 1/8 in and 0.27 in (https://sendcutsend.com/materials/woods) |
| Felt / TPU stop material, key-comb screws, key-top finish | lot | $4-12 | ESTIMATE |
| Thumbwheels + fader caps, FDM at makerspace | filament | $2-5 | ESTIMATE; Vector Space has PLA/PETG/TPU per owner-requirements.md |
| **Speaker** | | | |
| Speaker, Dayton Audio CE54N-4 (2 in, 4 ohm) | 1 ea | $13-23 | $12.98 https://parts-express.com/Dayton-Audio-CE54N-4-2-Dual-Neo-Full-Range-1VC-15W-4-ohm-285-167 (2026-11-12, 691 in stock; Fs 168 Hz, 84 dB). High adds ~$8-10 shipping. Mechanical fit (frame/cutout) not confirmed from the page |
| Grille cloth, gasket felt, speaker wire | lot | $4-10 | ESTIMATE |
| **Battery** | | | |
| Samsung INR18650-35E cells (2P) | 2 ea | $14-20 | $6.99 ea unprotected https://www.18650batterystore.com/products/samsung-35e-18650-3500mah-8a-battery (2026-11-12). Architecture requires protector on core board. High adds shipping |
| Keystone 1049 2-cell 18650 holder | 1 ea | $6-10 | $6.35 qty 1 https://www.digikey.com/en/products/detail/keystone-electronics/1049/2745670 (2026-11-12); fit vs. core-board pads not checked |
| **Enclosure, fasteners, wiring** | | | |
| Enclosure material, laser stack at Vector Space (Baltic birch -> walnut ply + acrylic), glue, finish | ~14 layers | $45-120 | ESTIMATE. Basis: Rockler Baltic birch 1/8 in 30x30 $14.99, 1/4 in $21.99 https://rockler.com/baltic-birch-plywood-choose-thickness (2026-11-12): ~6 layers of 300x210 per 30x30 sheet; walnut ply/acrylic priced higher. Makerspace laser time/fees NOT included |
| Fasteners: M3 through-bolts/standoffs/nuts, M2 fader screws, feet, tripod insert | kit | $15-35 | ESTIMATE |
| Wire, headers, board-to-board + hinge cable, heat-shrink, misc. | lot | $10-25 | ESTIMATE |
| **Shipping** | | | |
| JLC DHL shipping to Lynchburg, VA (~1.5-2 kg: 5+5+5 bare boards plus assembled) | 1 | $35-75 | ESTIMATE. JLC shows US shipping only in its quote tool https://jlcpcb.com/help/article/how-much-does-shipping-cost (2026-11-12); a 2026 maker write-up shows $16 DHL for a tiny 5-board order https://pamfinds.pages.dev/guides/pcb-tariffs-us-makers-2026/ (2026-04/05) |
| Other vendors: shipping + duties/brokerage (US: Mouser/DigiKey/Tayda/McMaster/Parts Express/Apex; UK/EU: Thonk, Electric Druid) | ~6 orders | $35-80 | ESTIMATE. De minimis suspended for all origins; foreign-vendor parcels (Thonk, Electric Druid) can attract duty/brokerage. Buying jacks from a US vendor avoids one |
| *Subtotal before contingency (incl. duty)* | | *$1,494-3,071* | |
| **Contingency**: 10% low / 15% high | | $149-461 | Judgement: unpriced footprint/stock substitutions, one lost board, price drift |
| **TOTAL (excl. tools, makerspace fees, sales tax)** | | **$1,644-3,531** | |

Of the above, the shared non-electronics block (panel hardware, keys, speaker, battery, enclosure) is $203-497 in both versions.

## 4. Version B: hand-soldered kit (through-hole voice board; JLC builds core + control module)

| Line item | Qty | Total (low-high) | Source and date checked, or ESTIMATE basis |
|---|---|---|---|
| **JLCPCB order (China-origin; tariff applies)** | | | |
| PCB fab: core board 110x85 mm, 4-layer (identical to A) | 5 pcs | $18-35 | ESTIMATE, as A |
| PCB fab: 'control module' (8 digipots + muxes, castellated) ~60x45 mm | 5 pcs | $8-16 | ESTIMATE. <=100x100 mm promo-class pricing; castellated-hole surcharge not found |
| PCB fab: keyboard board ~285x55 mm, 2-layer (hand-soldered TO-92) | 5 pcs | $12-30 | ESTIMATE, as A |
| PCB fab: voice board THT ~290x170 mm (low 2-layer, high 4-layer) | 5 pcs | $35-150 | ESTIMATE. 2-layer ~$35-70 / 4-layer $60-150 (same basis as A). Layer count is an engineering decision (noise); not specified for THT variant in architecture.md |
| PCBA fees: core (identical to A) | 2 pcs | $90-160 | As A |
| PCBA fees: control module | 2 pcs | $35-70 | https://jlcpcb.com/help/article/pcb-assembly-price (2026-11-12): economic setup $8.18, stencil $1.53, extended-part loading $3.07; standard alternative $25.56+$8.21+$16.42. ESTIMATE of ~6 unique parts |
| SMD parts: core (identical to A, ex-Pico) | 2 boards | $138-198 | As A |
| SMD parts: control module (8 digipots + muxes + passives) | 2 modules | $100-152 | ESTIMATE ($50-76 per module); digipot sourcing risk as A |
| *Subtotal, JLC order (tariff base)* | | *$436-811* | |
| **US import duty prepaid by JLC (DDP)**: 35% low / 40% high of the JLC subtotal | | $152-324 | JLC table: PCB 35%, SMT 35% https://jlcpcb.com/news/logistics-update-us-china-tariff (2026-11-12, rates dated 2026-03-17). High = 37.5% legal stack, rounded up. See section 2 |
| **Other electronics sourced outside JLC** | | | |
| AS3046 DIP-14 (6 + 2 spare) | 8 ea | $40-48 | EUR 4.50 ex-VAT qty 1-9 https://electricdruid.net/product/as3046-matched-transistor-array/ (2026-11-12, 546 in stock); USD conversion ESTIMATE. Tayda's CA3046 is out of stock and not the intended part https://www.taydaelectronics.com/ca3046-npn-transistor-array.html |
| THT transistors (~65 x 2N3904/3906/BC550C + 20% spares), diodes (~25) | ~100 | $7-14 | ESTIMATE |
| Resistors: ~290 x 1% metal film + ~40 x 0.1% + 3 tempco | ~330 | $22-68 | ESTIMATE (0.1% parts dominate: ~$0.4-1.2 ea) |
| Capacitors: ~12 film (PP/PPS) timing + ladder, ~100 ceramic/electrolytic | ~110 | $28-70 | ESTIMATE |
| DIP ICs (op-amps, NJM4556A, LM393, 4051, LM4040) + ~16 sockets | ~25 | $23-42 | ESTIMATE |
| LSK489 TO-71 dual JFET (3 + 1 spare) | 4 ea | $24-48 | ESTIMATE $6-12 ea; TO-71 variant availability per architecture.md §2.2 (Linear Systems) |
| Headers/connectors (board-to-board, key matrix, battery, speaker) | lot | $8-15 | ESTIMATE |
| Keyboard board parts: 28 TO-92 Hall, 2x DIP-24 mux, RP2040 board, headers | lot | $19-31 | Hall $0.28-0.36 each (LCSC C85697 / C266125, 2026-11-12); rest ESTIMATE |
| Pico 2 module for core board (hand-soldered castellated, 1 + 1 spare) | 2 ea | $6-12 | $5.75 https://www.sparkfun.com/raspberry-pi-pico-2.html (2026-11-12) |
| **Panel hardware (same in both versions)** | | | |
| Rotary pots, 9 mm PCB (15 panel + 2 wheel) | 17 ea | $11-37 | Low: Tayda $0.67 ea https://www.taydaelectronics.com/10k-ohm-linear-taper-potentiometer-round-knurled-plastic-shaft-pcb-9mm.html (2026-11-12). High: ESTIMATE ~$2.2 ea for genuine Alpha/Mouser-class parts; 1 MΩ audio ext-in pot included |
| Contour faders, PCB-mount ~30 mm, M2 threaded | 6 ea | $12-27 | ESTIMATE $2-4.50 ea. Basis: Tayda's only listed fader is a $2.30 60 mm dual with stock of 1 (2026-11-12, https://www.taydaelectronics.com/catalogsearch/result/?q=slide+potentiometer+45mm); TT PS30/PS45 class on DigiKey/Mouser not price-checked (DigiKey fetch blocked) |
| Knobs / fader caps (15 rotary; 6 fader caps printed; 2 wheels printed in item below) | 15 ea | $10-40 | ESTIMATE $0.6-2.6 ea (plastic Tayda-class to machined). No live knob listing retrieved |
| Rotary switches 6-pos (range x3, waveform x3) | 6 ea | $9-24 | ESTIMATE $1.5-4 ea; not price-checked |
| Toggle/slide switches, mini SPDT PCB-mount | 16 ea | $11-40 | Low: Tayda $0.68 ea https://www.taydaelectronics.com/mini-toggle-switch-spdt-on-off-on-pc-thru-hole.html (2026-11-12). High: ESTIMATE ~$2.5 ea (C&K/E-Switch class) |
| 3.5 mm jacks (12 mono + 3 stereo: phones, MIDI in/out TRS) | 15 ea | $8-14 | Thonk Thonkiconn mono GBP 0.38 (GBP 0.31 at 50+), stereo GBP 0.49 https://www.thonk.co.uk/shop/thonkiconn (2026-11-12); converted ESTIMATE ~$0.5-0.9 ea. UK vendor: see duty/shipping line |
| Power slide switch, TUNE button, RGB/charge LEDs | lot | $3-8 | ESTIMATE |
| **Keys** | | | |
| Neodymium disc magnets 3x1 mm (25 + spares) | 1 x 100-pk | $7 | https://www.apexmagnets.com/3mm-x-1mm-disc-neodymium-magnet (2026-11-12) $6.99/100, N48. Magnet size must match the Hall design; ESTIMATE-level until the sensor/magnet CAD is frozen |
| Delrin (acetal) sheet for flexure comb, ~12x24 in | 1 sheet | $18-40 | ESTIMATE. McMaster product pages (e.g. 8573K13) show no price in fetch (2026-11-12). Thickness is not specified in jam.md; Vector Space wiki lists Delrin for its CO2 lasers but another makerspace wiki says <=2 mm only and messy (https://wiki.acemakerspace.org/laser-cutter-materials/). SendCutSend Delrin only in 1/8 in and 0.27 in (https://sendcutsend.com/materials/woods) |
| Felt / TPU stop material, key-comb screws, key-top finish | lot | $4-12 | ESTIMATE |
| Thumbwheels + fader caps, FDM at makerspace | filament | $2-5 | ESTIMATE; Vector Space has PLA/PETG/TPU per owner-requirements.md |
| **Speaker** | | | |
| Speaker, Dayton Audio CE54N-4 (2 in, 4 ohm) | 1 ea | $13-23 | $12.98 https://parts-express.com/Dayton-Audio-CE54N-4-2-Dual-Neo-Full-Range-1VC-15W-4-ohm-285-167 (2026-11-12, 691 in stock; Fs 168 Hz, 84 dB). High adds ~$8-10 shipping. Mechanical fit (frame/cutout) not confirmed from the page |
| Grille cloth, gasket felt, speaker wire | lot | $4-10 | ESTIMATE |
| **Battery** | | | |
| Samsung INR18650-35E cells (2P) | 2 ea | $14-20 | $6.99 ea unprotected https://www.18650batterystore.com/products/samsung-35e-18650-3500mah-8a-battery (2026-11-12). Architecture requires protector on core board. High adds shipping |
| Keystone 1049 2-cell 18650 holder | 1 ea | $6-10 | $6.35 qty 1 https://www.digikey.com/en/products/detail/keystone-electronics/1049/2745670 (2026-11-12); fit vs. core-board pads not checked |
| **Enclosure, fasteners, wiring** | | | |
| Enclosure material, laser stack at Vector Space (Baltic birch -> walnut ply + acrylic), glue, finish | ~14 layers | $45-120 | ESTIMATE. Basis: Rockler Baltic birch 1/8 in 30x30 $14.99, 1/4 in $21.99 https://rockler.com/baltic-birch-plywood-choose-thickness (2026-11-12): ~6 layers of 300x210 per 30x30 sheet; walnut ply/acrylic priced higher. Makerspace laser time/fees NOT included |
| Fasteners: M3 through-bolts/standoffs/nuts, M2 fader screws, feet, tripod insert | kit | $15-35 | ESTIMATE |
| Wire, headers, board-to-board + hinge cable, heat-shrink, misc. | lot | $10-25 | ESTIMATE |
| **Shipping** | | | |
| JLC DHL shipping to Lynchburg, VA (~1.2-1.8 kg) | 1 | $30-60 | ESTIMATE, as A |
| Other vendors: shipping + duties/brokerage (more parts orders than A) | ~8 orders | $50-110 | ESTIMATE |
| *Subtotal before contingency (incl. duty)* | | *$1,047-2,149* | |
| **Contingency**: 10% low / 15% high | | $105-322 | Judgement: unpriced footprint/stock substitutions, one lost board, price drift |
| **TOTAL (excl. tools, makerspace fees, sales tax)** | | **$1,152-2,472** | |

## 5. Spares, minimum quantities and the tier-2 delta

- **Bare boards:** the 5-piece minimum leaves **3-4 unassembled spares of every design**. Their share of the bare-board fees is about $55-130 in A and $45-140 in B before duty. Keep them: a wrecked voice board or a bad flexure sensor board otherwise costs a full re-order plus duty.
- **Assembled spare set (2-piece PCBA minimum, ASSUMED):** forces a second set of SMD parts. Marginal cost of that second set including duty: **A about $285-497** (core, voice, keyboard), **B about $160-245** (core, control module). If JLC accepts a quantity of 1 for standard PCBA, subtract those amounts from the totals.
- **Parts with stock risk:** MCP41HV51 shows 21 in stock and AD5293 0 at LCSC (2026-11-12); DAC8568 633. Sixteen digipots (two sets) would use most of the 21 MCP41HV51 in stock, and AD5293 would have to come via Global Sourcing. Confirm stock on the order day.
- **Cheaper digipot lever:** MCP41HV51 ($3.31 qty 1) in place of AD5293 saves roughly $25-45 per set, at 8-bit instead of 10-bit resolution (architecture.md 5e.4 calls 8-bit marginal near emphasis onset).

**Tier-2 delta** (waveform x3, pulse width, noise colour, osc/filter mod, feedback, mixer on/off via 4-6 DG4xx-class switch ICs; architecture.md 5e.3 says +$15-30 per unit, UNVERIFIED):

| Version | Added parts incl. JLC loading fees | With duty and contingency |
|---|---|---|
| A (on voice board, 2 assembled) | $37-96 | **$54-155** |
| B (on control module, 2 assembled; module may need a larger outline) | $37-96 | **$54-155** |

Basis: ESTIMATE $3-6 per ADG/DG-class IC at qty 1 (no live price retrieved), 2 boards, plus $8-15 passives. The architecture's per-unit figure ($15-30) covers one unit's parts only; the 2-board minimum, duty and contingency roughly triple it.

## 6. Enclosure alternative: order the laser cutting

Makerspace route is priced above as material only ($45-120). Ordering from SendCutSend or Ponoko instead (ESTIMATE: 14 layers of 300x210 mm 1/8 in ply or acrylic at roughly $15-35 per layer after cut-length pricing, plus $15-30 shipping, so **$215-480**) changes either total by about **+$170 to +$360**. I could not get an instant quote because it needs the DXFs; SendCutSend offers birch ply (1/8, 1/4, 9 mm, 12 mm), acrylic in 10 colours and Delrin only in 1/8 in and 0.27 in (https://sendcutsend.com/materials/woods, 2026-11-12). Their Delrin options are thicker than a typical flexure comb, so the key comb likely stays a makerspace/CNC job. **Check with Vector Space** that Delrin is allowed on their CO2 lasers and at what thickness: another makerspace's wiki allows only <=2 mm and calls it messy (https://wiki.acemakerspace.org/laser-cutter-materials/).

## 7. Tools the owner must buy if he has none

Needed for **B** (~1,500-1,700 through-hole joints) and, in smaller form, for **A** (panel parts, Pico 2, possibly AS3046D). The makerspace may have benches; I have no evidence either way, so these are priced as if it does not.

| Tool | Low-high | Source / basis |
|---|---|---|
| Soldering iron: Pinecil V2 (low) or Hakko FX-888DX station (high) | $57-130 | Pinecil $41.95 https://ameridroid.com/products/pinecil-v2-soldering-iron (2026-11-12) + ESTIMATE $15 USB-C PD supply; Hakko $129.95 https://www.sparkfun.com/hakko-fx-888dx-soldering-station.html (2026-11-12) |
| Solder, 0.8 mm (leaded 63/37 or SAC305), ~1/2 lb | $15-30 | ESTIMATE |
| Flush cutters + fine tweezers | $13-32 | ESTIMATE |
| PCB holder / third hand + lead-bending aid | $15-40 | ESTIMATE |
| Desoldering braid + solder sucker + flux pen | $20-40 | ESTIMATE |
| IPA, brushes, tip cleaner, safety glasses | $14-30 | ESTIMATE |
| Basic multimeter (continuity and rail checks; not calibration) | $20-50 | ESTIMATE |
| Fume extractor (optional; makerspace may have ventilation) | $0-45 | ESTIMATE |
| **Total for B** | **$154-397** | |
| **Minimum kit for A** (iron, solder, cutters, basics) | **$99-222** | subset of the above |

## 8. Estimated build hours (ESTIMATE, first-time builder, excludes design and firmware development)

| Task | A | B |
|---|---|---|
| Sorting/checking parts and BOM | 1 | 3-4 |
| Soldering electronics (A: panel parts, Pico 2, optionally 12 SOIC-14; B: ~1,600 joints plus keyboard board, headers) | 4-7 | 14-23 |
| Delrin comb cut, magnets, sensor alignment, key calibration | 3-5 | 3-5 |
| Laser-cut body at makerspace (incl. safety/booking), sanding, finish, glue-up | 6-11 | 6-11 |
| Print wheels and caps, fit speaker and battery, cabling, final assembly | 3-5 | 3-5 |
| Flash firmware, power-up, self-tune boot | 1-2 | 1-3 |
| **Total** | **18-31 h** | **30-51 h** |

## 9. What drives the range

1. **JLC assembly of the voice board (A only):** parts ($240-428 for two boards, of which the 8 digipots per board are about a third), assembly fees ($180-370; the biggest swing is whether JLC bills $1.53 per unique basic part), and the 2-piece minimum doubling it all. This is why A costs roughly $500-1,100 more than B.
2. **Tariff on everything JLC ships:** about $295-620 for A and $152-324 for B at 35-40%. Each 10 points of rate is about $84-155 on A and $44-81 on B. If only the bare boards fell to the 12.5% rate (exclusion holds and JLC reprices), the saving would be small, because PCBA parts and fees dominate the JLC order.
3. **Large-board fabrication and layer count:** a 290x170 mm board is ~5x the area of the 100x100 mm 'promo' size, and 4-layer pricing is not published for that size. Voice-board fab is a $35-150 spread in my ESTIMATE; the real quote is one click away once Gerbers exist.
4. **Single-source and unlisted parts:** AS3046 (A: $80-238 depending on hand-solder vs consign), LSK489, digipots (stock 0 or 21 at LCSC), DAC8568 x2 ($35 per board).
5. **Enclosure route:** makerspace material only ($45-120) versus ordered cutting (+$170-360).
6. **Panel hardware quality tier:** $64-190 between Tayda/Thonkiconn-class and Alpha/machined-knob-class parts.

**Not resolved:** JLC's true tariff base and rate at checkout; JLC PCBA minimum quantity; whether Hall-sensor/magnet CAD settles on 3x1 mm magnets; Delrin thickness; digipot stock; Vector Space Delrin policy.
