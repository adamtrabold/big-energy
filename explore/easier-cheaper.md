# Easier / cheaper synth clones under our principles

Status: rev 0, 2026-11-13. Lens: **EASIER and CHEAPER while still exciting.** Principles: `principles.md`. Baseline: `../eng/budget-variant.md` (Little D, rev 13: ≈ $311–395 USB, ≈ $356–448 with the 22.2 Wh pack).

Conventions: a link means the figure was read this session. **UNVERIFIED** means I could not confirm it. **ESTIMATE** is my number. [ENG] is engineering judgement. Prices are list prices; stock was usually *not shown*.

---

## 0. The headline (read first)

**The platform costs most, not the voice.** In the Little D budget these lines stay the same whichever classic synth you clone:
- Daisy Seed: $35
- 25 Choc V2 velocity keys: $51–56
- battery and charger: ≈ $39–41
- bend/mod: $8–11
- FX controls, enclosure, speaker, jacks: ≈ $40
- shipping from about 5 vendors: ≈ $30–39
- most of the board fee: the $20 handling fee is fixed

Together that is ≈ $230–270 before any voice parts. The Model D-specific voice costs only about $60–80 in parts (3 × AS3046 $15.60, 3 tempcos $7.50, JFETs, ~13 TL072s, 23 pots, 3 rotary switches, knobs), plus its share of the 67.5 in² board.

**So the realistic saving from a simpler voice is ≈ $30–90 per unit (≈ 10–25 %), not half.** [ENG, derived from the budget-variant BOM]

The bigger win is **EASIER**:
- fewer VCOs to autotune;
- chip VCOs with on-chip temperature compensation;
- far fewer trimmers and matched parts;
- smaller boards;
- lower power, so longer runtime.

---

## 1. Candidates

### 1.1 Roland SH-101 (1982), the strongest fit
- **Voice:** 1 VCO with saw, pulse and PWM, a 4013 sub-oscillator and noise feeding a mixer. Then a 4-pole IR3109 VCF, a BA662 VCA, one ADSR and an LFO. 100-step sequencer and arpeggiator, 32 keys. **Powered by 6 C cells, 1 W** ([Roland spec](https://support.roland.com/hc/en-us/articles/201921519-SH-101-Technical-Specifications)).
- **Chips:**
  - VCO is a CEM3340, VCF an IR3109, VCA a BA662; the ADSR is discrete ([Secret Life of Synthesizers](https://secretlifeofsynthesizers.com/roland-sh-101/)).
  - The IR3109 is "four buffered transconductance op-amps plus an exponential converter" and has no on-chip resonance control ([Electric Druid](https://electricdruid.net/?p=97905)).
- **Why iconic:** it is the bass and sequence sound of acid, techno and synth-pop. It was a portable keytar-style instrument (a modulation grip was an option) and is the template for countless clones.
- **Modern parts:**

  | Original | Replacement | Price and stock | Notes |
  |---|---|---|---|
  | CEM3340 | **AS3340A, DIP-16** | $7.95 ([Tubes and More](https://www.tubesandmore.com/products/integrated-circuits?sort=sku)); €5.25, "978 in stock" on Electric Druid's dev mirror (stock may be stale, [link](https://dev.electricdruid.net/?p=2515)) | |
  | IR3109 | **AS3109** | $7.95 ([Tubes and More](https://www.tubesandmore.com/products/integrated-circuits?sort=sku)); €6.50, 408 in stock ([Electric Druid](https://electricdruid.net/?p=97392)) | **SOIC-16 only** ([Erica Synths](https://www.ericasynths.lv/shop/ics/voltage-controlled-filter-3109); [Amplified Parts "AS3109D SOIC-16"](https://www.amplifiedparts.com/products/soic-16)). No pre-soldered DIP module found |
  | BA662 | **AS3080E, DIP-8** | $9.95 US; £6.50, in stock ([Thonk](https://www.thonk.co.uk/shop/alfa-as3080e/)) | Alfa's BA662 clone is SMD-only. Electric Druid says the AS3080 can stand in when the BA662's buffer isn't used (shown for the Juno 6 resonance, [link](https://electricdruid.net/?p=97905)). Whether that holds for the SH-101 VCA is **UNVERIFIED** |
  | IR9022 | TL022CP | | Per [Secret Life](https://secretlifeofsynthesizers.com/roland-sh-101/) |

- **Rule conflict:** the AS3109 breaks the through-hole rule. There are three ways out:
  - **(a)** The owner allows one SOIC-16 on a $0.39 adapter (adapters are [$1.95 for 5](https://www.amplifiedparts.com/products/soic-16)). That is one 1.27 mm-pitch part, which is easy as SMD goes.
  - **(b)** Someone else solders it, as a "ready-made module".
  - **(c)** Build a discrete equivalent from 2 × AS3280 / LM13700 OTAs plus an expo pair. That is an approximation, not the IR3109 [ENG].
- **Verification reference:**
  - No open SPICE model of the whole SH-101 was found; nothing like CA-72 exists.
  - No SPICE macromodels were found for the AS3340 or AS3109 (searched; **UNVERIFIED that none exist**).
  - References would be the service manual (widely mirrored; e.g. [Novamod schematic](https://manualmachine.com/roland/sh101novamod/8520077-schematic)), the chip datasheets, and the Electric Druid filter write-up.
  - Eurorack clones (e.g. [101 VCO](https://modulargrid.net/e/g-storm-electro-101-vco-r2)) show the circuit is well understood.
- **Calibration:** one VCO. Autotune covers what the original's "VCO width/tune" trims did. The 3340 compensates for temperature on-chip. The VCF width (keytrack) trim can be handled by the same self-oscillation measurement planned for Little D. Remaining trims: perhaps PW symmetry and one resonance trim [ENG].
- **Parts and cost:**
  - Voice ≈ 3 synth chips + ~8 TL072s + ~14–16 pots/sliders + 2–3 switches.
  - Voice BOM ≈ $40–55, against ≈ $60–80 for Little D (ESTIMATE).
  - The board is roughly 25–35 % smaller.
  - **One unit ≈ $270–360 USB, ≈ $315–410 with the pack** (ESTIMATE).
  - The sequencer and arpeggiator cost nothing on the Daisy.
- **Portability:** the best of the set. The original was battery-native at 1 W. The voice should draw well under Little D's 2.4–4.4 W [ENG].
- **Sound:** bright, round, rubbery bass; squelchy resonance; the sub-oscillator gives weight. One VCO means no detuned fatness.
- **Legal:** "SH-101" and "Roland" are trademarks. Use your own name and do not copy panel graphics [ENG, not legal advice]. The circuits themselves are long out of patent (UNVERIFIED).

### 1.2 EDP Wasp (1978), the cheapest and most on-principle
- **Voice:**
  - 2 **digital** oscillators (osc 1 ramp/pulse, osc 2 square) plus noise.
  - A multimode filter (LP/BP/HP).
  - An LFO with sample-and-hold.
  - **25 capacitive touch keys, a built-in speaker, battery power** ([Elby Designs](https://elby-designs.com/webtek/pixie/wasp/edp-wasp.htm)).
  - The VCF is a 2nd-order state-variable filter using **CA3080 OTAs and CD4069 inverters as op-amps** ([DAFx 2022 paper](https://dafx2020.mdw.ac.at/proceedings/papers/DAFx20in22_paper_34.pdf)).
- **Why iconic:** it was the first cheap "punk" synth: black and yellow, touch keys, speaker. The filter's CMOS grit is the signature. In effect it is the ancestor of the OP-1-style portable.
- **Modern parts:** everything is jellybean.
  - The [Jasper clone](https://diysynth.wiki.dsl-man.de/wiki/spaces/DSO/pages/1147044/Jasper+Wasp+Clone) uses new TI parts, swaps the 3080s for **2 × LM13700**, and uses CD4069s, an LM386, an MCP1702 LDO and BC547/557 transistors. It runs on 8 × AA, drawing ≈ 30–40 mA idle.
  - The AS3080E, $9.95, is available for exact fidelity ([Tubes and More](https://www.tubesandmore.com/products/integrated-circuits?sort=sku)).
  - The filter runs on a single 5 V supply ([schmitzbits](https://schmitzbits.de/wasp.html)), so no ± rails are needed.
- **Verification reference:** the best of the set for discrete simulation.
  - Redrawn schematics: [Elby](https://elby-designs.com/webtek/pixie/wasp/edp-wasp.htm). Filter schematic: [schmitzbits](https://schmitzbits.de/wasp.html).
  - The Jasper clone is a complete through-hole reference.
  - The DAFx paper publishes component values and a measured CD4069 inverter model. Its simulation framework, ACME, is on GitHub.
  - An ngspice netlist would have to be written by us. The only hard part is a CD4069 SPICE model, and the paper's measured parameters help [ENG].
- **Calibration:** **none for pitch**, because the oscillators are digital. This is the purest "no rigmarole". It also creates a decision for the owner: the Daisy could generate the oscillators (the original's were digital too), or we could build CMOS counters to keep them hardware. Exactly how the original generated them is **UNVERIFIED**.
- **Parts and cost:**
  - Voice BOM ≈ $15–30 (ESTIMATE).
  - Small board with no rail converters.
  - **One unit ≈ $250–330 USB, ≈ $290–380 with the pack** (ESTIMATE).
  - Note: the Jasper PCB is 250 × 398 mm, but that is a full replica with a keyboard sensor, not our layout.
- **Portability:** perfect. The original already met our principles, and power is very low.
- **Sound:** thin, buzzy, nasal and aggressive, with lovely filter distortion. It is less "big" than a Model D, and some will find it polarizing.
- **Legal:** "Wasp" and EDP marks (Behringer sells a "Wasp Deluxe"). Use another name. The schematic copyright belongs to Chris Huggett per Elby, so redraw rather than copy (UNVERIFIED legal position).

### 1.3 Sequential Pro-One (1981), the easiest "big" sound
- **Voice and chips** ([Secret Life](https://secretlifeofsynthesizers.com/?p=305)):
  - 2 × CEM3340 VCOs (with sync), plus a third 3340 as the LFO;
  - CEM3320 filter;
  - 2 × CEM3310 envelopes;
  - CA3280 VCA;
  - Intel 8021 MCU and AD558 DAC for keys, sequencer and arpeggiator.
- **Why iconic:** it is half a Prophet-5. Its modulation matrix (filter envelope or VCO B to pitch, PW and cutoff) gives aggressive, Model D-adjacent fat leads and basses.
- **Modern parts:** every voice chip has a DIP Alfa clone.

  | Chip | Package | Price | Source | Stock |
  |---|---|---|---|---|
  | AS3340A | DIP-16 | $7.95 | [Tubes and More](https://www.tubesandmore.com/products/integrated-circuits?sort=sku) | not shown |
  | AS3320 | DIP-18 | $5.95 | [Tubes and More](https://www.tubesandmore.com/products/dip-18) | not shown |
  | AS3320 | | €3.75, "577 in stock" | Electric Druid dev mirror ([link](https://dev.electricdruid.net/?p=1980)) | may be stale |
  | AS3310 | DIP-16 | $5.85 | Tubes and More | not shown |
  | AS3280 | DIP-16 | $7.95 | Tubes and More | not shown |

  - Chips ≈ $50 for the full set. The Daisy replaces the 8021 and the DAC.
- **Verification reference:** service manual and schematics are widely available (UNVERIFIED link). No SPICE models of the CEM/AS chips were found. Verification would lean on the datasheet application circuits; with this much chip, there is less discrete circuitry to simulate [ENG].
- **Calibration:** 2 VCOs to autotune, temperature-compensated on-chip. The filter is tracked by self-oscillation. The original needed only VCO tuning through panel holes. Far fewer trimmers and matched pairs than three discrete Model D VCOs.
- **Parts and cost:**
  - Lowest discrete parts count of any 2-VCO option. Voice BOM ≈ $65–80 (ESTIMATE), about the same as Little D, but much less build and matching work.
  - **One unit ≈ $290–380 USB, ≈ $335–430 with the pack** (ESTIMATE).
- **Portability:** neutral. The original was a mains desktop with 37 keys. The voice is 6 chips plus op-amps, so it is compact.
- **Legal:** "Sequential", "Pro-One" and "Prophet" are trademarks (Sequential is active again). Use your own name.

### 1.4 Moog Prodigy (1979–84), the least new risk
- **Voice:** 2 VCOs (saw/tri/pulse), a Moog 24 dB ladder, an A/D/S envelope, an LFO (tri/square), 32 keys ([vintagesynth](https://www.vintagesynth.com/moog/prodigy)). Schematic and service manual: [elektrotanya](https://elektrotanya.com/moog_prodigy.pdf/download.html). The [emusic-diy Moog manuals](https://emusic-diy.org/moogmanuals) are an UNVERIFIED mirror.
- **Clones:** [DIY thread](https://www.sequencer.de/synthesizer/threads/moog-prodigy-clone-diy.103231/latest); [Eurorack ER-16](https://www.gearnews.com/moog-prodigy-clone-prodigy-er-16-eurorack-released-via-polish-ebay).
- **Why consider it:** it is a "Little D minus one VCO". Our ladder SPICE work and much of the Little D layout carry over. A generic ngspice ladder netlist also exists ([oyama/ladder-filter-testbench](https://github.com/oyama/ladder-filter-testbench), per [DAFx26](https://www.dafx.de/paper-archive/2026/papers/DAFx26_paper_29.pdf)).
- **Trade-offs:** the VCOs are discrete (exact VCO design UNVERIFIED), so the expo-pair and tempco work stays. Saving ≈ $20–40 (ESTIMATE). Easiest from where we are, but the least *different*.

### 1.5 Korg MS-10 / MS-20
- **Voice:**
  - MS-10: 1 VCO, a 12 dB LPF (the MS-20 design), a single-transistor VCA, hold+ADSR, an LFO, a few patch points, 32 keys. Later units used LM13600 OTAs ([Wikipedia mirror](https://kaweah.freedombox.rocks/kiwix/wikipedia_en_all_maxi_2023-10/Korg_MS-10)).
  - MS-20: 2 VCOs, Korg35 HPF and LPF, a big patch panel.
- **The Korg35:** a module of five transistors and six resistors, a transistor-biased Sallen-Key design. Very simple and SPICE-friendly ([Secret Life](https://secretlifeofsynthesizers.com/?p=976)).
- **Through-hole references:** the OTA-version [KS-20](https://kassu2000.blogspot.com/2019/07/ks-20-filter.html) is open, through-hole and on GitHub; also the [LM13700 MS-20 filter (EasyEDA)](https://easyeda.com/technoplusnl/ms-20-lm13700-filter-by-look-mum-no-computer-rene-schmitz). Service manual: [elektrotanya](https://elektrotanya.com/korg_ms-10_sm_1.pdf/download.html).
- **Cost:** cheap. The LM13700 or 2N3904s cost cents.
- **Why not top 3:**
  - The MS-10 is easy but the least exciting.
  - The MS-20's identity is the patch bay, which conflicts with "no extra patch points".
  - The VCOs are discrete Korg designs, so autotune does real work.
- **Possible future option:** a "screaming dual-filter" voice (2 VCOs, Korg35 HPF and LPF, no patch bay).

### 1.6 Roland SH-09 (1980)
1 VCO (ramp/PWM/square/noise), filter with S&H and external input, ADSR, LFO, 32 keys ([vintagesynth](https://vintagesynth.com/roland/sh-09)). Whether its filter is an IR3109 is UNVERIFIED. It is less famous than the SH-101 and has no clear advantage over it, so skip it.

### 1.7 Crumar Spirit (1983)
- **Voice:** designed by Moog, Scott and Rhea. 2 VCOs with sync, a multimode 12/24 dB filter, a ring modulator, arpeggiator, the MOD-X/SHAPER-Y modulation system, 37 keys ([vintagesynth](https://vintagesynth.com/crumar/spirit)).
- **Verdict:** very cool, but more complex than the Model D path and with fewer reference resources. Cooler, not cheaper or easier. Better suited to the "cooler" agent's list.

### 1.8 Others glanced at (UNVERIFIED, not researched in depth)
- **Yamaha CS-01:** portable, battery, breath control. Its custom Yamaha IG chips have no reissue, which Electric Druid also expects ([analog renaissance](https://electricdruid.net/analog-renaissance/)). Out.
- **ARP Axxe:** 1 VCO, ARP 4075-style ladder. A possible SH-101 alternative.
- **Moog Rogue:** 2 VCOs and a ladder, close to the Prodigy.

---

## 2. Comparison table (one unit, ESTIMATE unless cited)

| | VCOs to autotune | Key chips (all DIP?) | SPICE reference | Voice BOM | One unit, USB (pack) | Portability fit | Excitement |
|---|---|---|---|---|---|---|---|
| Little D (baseline) | 3 discrete | AS3046 ×3 (DIP) | **CA-72 (full)** | $60–80 | $311–395 ($356–448) | good | high |
| **SH-101-style** | 1 (3340) | AS3340, **AS3109 (SOIC)**, AS3080 | none; datasheets + manual | $40–55 | $270–360 ($315–410) | **best** | high |
| **Wasp-style** | **0** | LM13700/AS3080, CD4069 (DIP) | DAFx model + Jasper; easy discrete sim | **$15–30** | **$250–330 ($290–380)** | **best** | medium-high, quirky |
| **Pro-One-style** | 2 (3340) | 3 × AS3340, AS3320, 2 × AS3310, AS3280 (all DIP) | none; datasheets | $65–80 | $290–380 ($335–430) | ok | **high** |
| Prodigy-style | 2 discrete | AS3046 | reuse Little D ladder work | $45–60 | $290–370 ($335–420) | good | medium |
| MS-10/20-style | 1–2 discrete | LM13700 / 2N3904 | Korg35 is simple to simulate | $25–50 | $260–350 | ok | MS-20 high, MS-10 low |

---

## 3. Top 3 for "easier/cheaper while still exciting"

**1. SH-101-style.** It is the most loved of the cheap classics, and its original was already a battery-powered portable with a sequencer and arpeggiator, which the Daisy provides for free. One chip VCO means the easiest autotune of any "real" analog option. The voice has about half the parts of Little D. The only snag is the SOIC-only AS3109: ask the owner for a one-part exception, or use a discrete OTA approximation. Saving ≈ $40–50 against Little D, and a much easier build.

**2. Wasp-style.** It is the cheapest and simplest, and nearly a description of our principles from 1978: battery, speaker, 25 keys. It needs no pitch calibration at all and runs the filter from a single 5 V supply. It has the best verification path among the alternatives: an open through-hole clone plus a peer-reviewed filter model. It is quirkier and thinner-sounding. The owner must decide whether Daisy-generated digital oscillators count as an "analog voice" (they matched the original's architecture). Saving ≈ $60–70.

**3. Pro-One-style.** This is the "still exciting" pick: two VCOs with sync and cross-modulation give a big, Model D-adjacent sound. Every voice chip has a through-hole Alfa clone in stock at US distributors for $6–8. Few trimmers, few matched parts, and two autotuned VCOs. It is not much cheaper (≈ $20) but is much easier to build and debug than three discrete VCOs. It is the weakest of the three on portability heritage and has no SPICE golden reference.

**Recommended next step:** if the owner likes #1 or #3, first price the platform-only BOM (keys, Daisy, battery, enclosure). It dominates every option, so trimming it, for example a smaller board or fewer vendors, may save more than changing the synth being cloned.
