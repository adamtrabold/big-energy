# Explore: polyphonic and hybrid clones now that a Daisy Seed is in the design

Status: rev 0, 2026-11-13. Lens: **polyphonic + hybrid**. Inputs: `explore/principles.md`, `eng/budget-variant.md` rev 13 (§v1.2, §v1.11), `eng/daisy-first-principles.md` (codec use), `eng/battery.md`.
Conventions (same as eng/): link = read this session. **ESTIMATE** = my number, not checked. **UNVERIFIED** = source exists or is a recollection, but I could not confirm it. [ENG] = engineering judgement.

Baseline to beat (Little D rev 13): one analog voice, 3 VCOs; ≈ **$311–395 USB / $356–448 with the 22 Wh pack**; ≈ **2.4–4.4 W** (voice rails 1.2–1.9 W); main board ≈ 268 × 120–126 mm; 26 of 31 Seed GPIO used; codec out L/R = FX wet stereo, codec in R free.

---

## 1. Bottom line

| Rank | Candidate | Δ cost vs Little D | Scope risk | Why |
|---|---|---|---|---|
| **1** | **Little D "Para": 3-note paraphonic + duo mode + Daisy "osc 4"** (a firmware mode of the current build, not a new clone) | **≈ +$1–5** | **Very low** | Every VCO already has its own MCP4822 pitch channel and its own autotune counter. Paraphony is assigner firmware. Gets Mono/Poly-, Matriarch- and Odyssey-duo-style playing for ~nothing |
| **2** | **"Little J": 4-voice Juno-60-style DCO poly**, AS3109 filter, Daisy envelopes/LFO, Daisy stereo chorus | ≈ **$350–520** total one unit (ESTIMATE); a **separate instrument** | **High** (≈ 2× the soldering of Little D) | DCOs need no pitch autotune; open DCO/chorus references exist. Blocker to resolve first: **AS3109 package (DIP vs SOIC conflict)** |
| **3** | **4-voice "Prophet-600-ish"**: 2× AS3340 + 1× AS3372E per voice (all DIP, in stock) | ≈ **$380–560** (ESTIMATE); separate instrument | **High**, plus 8-VCO autotune and **no SPICE golden reference** for the CEM-type chips | Fewest chips per voice of any VCO poly; the "real Prophet" sound family |

Not ranked: exact Juno-106 (80017A clone = $250/6, no saving), Polysix/Mono-Poly (filter chip not through-hole), OB-X-ish (discrete SVF voices, trims, no open sim found), standalone ARP Odyssey (same scope as Little D; its duophony is free in rank 1). AS3394E voice-chip poly is the **cheapest per voice** but **out of stock** at both vendors checked (§3.5).

**Honest scope note:** any true poly is a *second* instrument roughly the size of Little D's whole voice section *again*, multiplied by the voice count, and it would be the owner's first poly with a "no rev 2" rule. Rank 1 adds the poly-ish fun to the build already designed, at near-zero risk. If the owner wants a second build after Little D, rank 2 is the most interesting; do it only after Little D's spike and build prove the Daisy control stack.

---

## 2. What the Daisy changes for poly/hybrid (shared facts)

- Seed: ["ARM Cortex-M7 MCU, running at 480MHz", "x31 GPIO, x12 ADC inputs (16-bit)", "x2 DAC outputs (12-bit, DC-Coupled)", stereo 96 kHz/24-bit audio, 64 MB SDRAM](https://www.electro-smith.com/daisy/daisy). (The budget doc carries 400 MHz for its load figures; 480 MHz is the vendor's headline.)
- **What becomes possible:**
  - **Envelopes, LFOs and glide in firmware for N voices.** A poly no longer needs N analog ADSR chips; the cost moves to **CV outputs** (≈ 3–5 per voice) = DACs + sample-and-hold, as the Juno-106 did (UNVERIFIED recollection of the 106's single-DAC + 4051 demux).
  - **Stereo chorus/ensemble done digitally** in the codec, next to the existing echo/reverb, with the dry path staying analog (same wet-sum topology already in `daisy-first-principles.md` §FX).
  - **Digital oscillator modes** (wavetable, Plaits-style macro oscillators) as an extra *source* feeding the analog mixer and filter.
  - **Autotune counting** for more oscillators by muxing comparator outputs into one TIM5 counter (serial tuning) [ENG].
- **What it does not solve:**
  - **Pins.** Little D uses 26/31. A poly needs more CV channels and more timer outputs; any poly needs a ground-up pin plan, likely a **second ready-made module** (e.g. a Pico 2 as the DCO engine, as PolyKit does, §3.2).
  - **Codec channels.** Both codec outputs are already the stereo FX wet. A digital oscillator into the analog path must either take one of them (wet goes mono when it is on) or use the Seed's internal DAC (10.9 ENOB, and PA4 is provisionally the sensor-LDO enable): see §3.1.
  - **Power.** Each analog voice costs watts on battery (per-voice figures below are ESTIMATE).

---

## 3. Candidates

### 3.1 Little D "Para" (rank 1): paraphonic / duo + Daisy oscillator

**What it is:** a VOICE MODE switch (or a held-key menu) on the instrument already specified.
- **MONO:** as now.
- **DUO (ARP Odyssey-style):** VCO 1 plays the lowest held key, VCO 2 the highest; VCO 3 stays the mod source.
- **PARA 3:** VCO 1–3 each take a note (round-robin or lowest-free). The ladder, both contours and the VCA are shared, so chords are legato under one envelope. This is how Korg Mono/Poly-style paraphony works. The Matriarch offers ["Mono, duo, and 4-note paraphonic playability" with "Four analog oscillators"](https://synthtopia.com/content/2019/04/25/moog-matriarch-a-4-note-paraphonic-analog-synthesizer) (the article does not detail how voices share filter/envelopes).
- **+ OSC 4 (hybrid):** the Daisy generates a 4th oscillator (wavetable, or Plaits engines; the owner already owns Plaits and is porting its ideas elsewhere). It enters the analog mixer through the existing **NOISE/EXT** level and **SOURCE** toggle, so it is filtered by the real ladder. In PARA it becomes the 4th note → Matriarch-like 4-note paraphony. Plaits' code is open and has a Daisy port (forum thread ["Plaitsy (Plaits port for Patch)"](https://forum.electro-smith.com/t/plaitsy-plaits-port-for-patch-mutable-daisies/8982); contents not read, **UNVERIFIED** whether it runs on a bare Seed alongside the FX).

**Why it is nearly free (from `budget-variant.md` §v1.2):**
- Pitch CVs: **2× MCP4822 already drive VCO 1, 2, 3 separately** (+ filter keytrack). Osc 2/3 FREQ and RANGE are MCU-read, so the per-VCO note is just firmware arithmetic.
- Autotune: each VCO already has its own TIM5 counter and background re-tune. Nothing new to calibrate.
- Keys: the Hall scan already sees every key at once (no new hardware for chord detection).

**What it costs or breaks:**

| Item | Cost | Note |
|---|---|---|
| VOICE MODE 3-way toggle (MONO/DUO/PARA) on a spare mux channel | ≈ $1 | mux at ≈ 46 of 48; 2 spare channels left (ESTIMATE) |
| Osc-4 audio: codec **OUT R** → existing EXT input node, one resistor + one switch section | ≈ $0.50–2 | When OSC 4 is on, the FX wet folds to mono on OUT L [ENG]. Alternative: Seed internal DAC (no codec cost but 67.8 dB SNR, and the PA4 pin clash) |
| Firmware: assigner, retrigger rules, osc-4 engine | $0 | CPU: Plaits-class engine plus plate + tape echo: **UNVERIFIED**; measure in the existing spike step 5 (< 50 % CPU gate) |
| **Total** | **≈ +$1.50–5** | No board growth worth counting |

**Musical limits (honest):**
- **PARA 3 loses osc 3 as the LFO/mod source** (on the original, osc 3 *is* the LFO). Mod falls back to noise, unless a firmware LFO is added (one PWM CV into the MOD MIX node: ≈ +$0.50, ESTIMATE).
- **One envelope, one filter:** no per-note articulation; per-note velocity can't be honoured (only the first note's velocity).
- The Model D's filter keytrack has to follow one note in PARA (lowest or highest; choose in firmware).

**Through-hole / sim / portability / no rev 2:** no new chips; CA-72 golden reference unchanged; same box; zero hardware risk beyond one switch and one resistor. **Fully feasible.**

**Spike addition (10 minutes):** play 3 VCOs from 3 DAC channels on the breadboard with the background re-tune running; confirm no audible re-tune glitches on held chords.

---

### 3.2 "Little J": 4-voice Juno-60-style DCO poly (rank 2)

**Why Juno-60 and not 106:** the 106's voice is the potted **80017A** (VCF + VCA). The only clone found, the **RS80017A**, is ["$250.00"… sold "only" in sets of 6, a "hybrid VCF/VCA circuit" using "a real 3109 OTA"](https://reach.dog/shop/rosen-sound-llc/products/80017a-clone) (per-set vs per-chip and form factor not stated: **UNVERIFIED**). That is a repair part, not a cheap build path. The **Juno-60 voice** is the same idea built from parts (IR3109 filter + separate VCA; topology recollection **UNVERIFIED**, check the service manual).

**Per voice (ESTIMATE):**
- **DCO:** a crystal-derived clock resets an op-amp integrator (saw), comparator for pulse/PWM, CD4013 sub-osc, CD4066 wave mix. Amplitude compensation CV per voice (the ramp's height falls with frequency unless the charge current scales).
- **VCF:** **AS3109**, ["Alfa's modern equivalent of the famous Roland IR3109 filter chip, as used in the Jupiter 8 and SH-101", €6.50, 408 in stock](https://electricdruid.net/?p=97392).
- **VCA:** ¼ of an AS2164 (Alfa lists it ["in DIP and SOIC"](https://sdiy.info/wiki/Alfarzpp)).
- **CVs from the Daisy side:** DCO amplitude, PWM, cutoff, VCA = **4 per voice, 16 for 4 voices**: 8× MCP4822 DIP, or 2× MCP4822 + sample-and-hold demux (CD4051 + caps + TL074) [ENG].
- **DCO clocks:** **PolyKit's open pico-dco** does exactly this: ["up to 6 voices which are driven by a Raspberry Pi Pico"; "It uses PIO to generate a highly accurate frequency"; "Amplitude compensation is done by a smoothed PWM signal coming from the Pico"](https://github.com/polykit/pico-dco) (license not shown on the page: **UNVERIFIED**). A **Pico 2 module (~$5.75) as DCO engine** next to the Daisy keeps both "ready-made modules" and frees the Daisy's pins and timers. PolyKit DUO is the full 6-voice reference: ["6 voice polyphonic dual DCOs per voice… using dual Raspberry Pi Pico's"](https://github.com/craigyjp/PolyKit-DUO-polyphonic-synthesizer) (filters there are Matrix-12-style, not Juno).
- **Chorus:** Daisy stereo chorus (BBD-style: modulated delay with a band-limited, slightly noisy, companded character) on the existing codec L/R. Open references: [junologue-chorus, "Juno-60 chorus emulation for Korg Prologue, Minilogue XD and Nu:tekt NTS-1"](https://github.com/peterall/junologue-chorus/releases) (method not described; whether it models a BBD is **UNVERIFIED**) and [JunoX, a "JavaScript library that emulates the classic Roland Juno-60", GPL-3.0](https://www.github.com/pendragon-andyh/junox) (with a chorus demo). CPU is trivial next to CloudSeed-class reverb [ENG].

| Per voice | ESTIMATE |
|---|---|
| Chips | AS3109, ¼ AS2164, 3–4× TL072/074, ½ CD4013, ¼–½ CD4066 (+ shared S&H or DACs) |
| Parts cost | ≈ $18–28 |
| Board area | ≈ 50 × 70 mm (≈ 3,500 mm², ≈ 5.4 in²) → ≈ $3.50–7 at $0.61–1.22/in² |
| Power | ≈ 0.15–0.3 W (±9 V op-amps + OTA + VCA) |
| **Cost per voice** | **≈ $22–35** |

**Whole instrument, 4 voices (ESTIMATE):** voices ≈ $90–140; shared (Daisy $35, Pico 2 $6, keys/Hall strip, panel ≈ 20 sliders/pots, power, battery, enclosure) taken from Little D's lines with the 3-VCO voice removed ≈ $260–380 → **≈ $350–520**. 6 voices adds ≈ $45–70 and ≈ 7,000 mm².
**Power:** 4 voices ≈ 0.6–1.2 W + Daisy 0.4–0.8 + Pico 0.1 + Hall strip 0.6–1.25 + misc ≈ **1.8–3.5 W → ≈ 5–10 h on 22.2 Wh** (same method as `battery.md`). Fewer watts than Little D's discrete 3-VCO voice.

**Calibration (per voice):**
- **Pitch: none** (crystal timing): the biggest win over any VCO poly.
- **DCO amplitude:** a frequency → CV table per voice; auto-learnable by reading each saw's peak through a mux into a Seed ADC [ENG]. Mild.
- **VCF:** AS3109 cutoff varies chip to chip; auto-cal by driving each filter into self-oscillation and counting it (one comparator per voice → mux → one counter), the same method as Little D's filter scale cal [ENG]. Moderate firmware, no trimmers.
- **VCA offset:** auto-null as in Little D.

**Through-hole availability: the open question.**
- [Erica says "AS3109 comes in SOIC-16 case"](https://www.ericasynths.lv/shop/ics/voltage-controlled-filter-3109); [sdiy.info lists "AS3109 - IR3109 VCF in DIP and SOIC"](https://sdiy.info/wiki/Alfarzpp). **Conflict: UNVERIFIED** until a DIP part number is found in stock.
- If SOIC only, it breaks "SMD only as ready-made module", unless a pre-assembled DIP adapter is bought (none found).
- **Fallback filter, all DIP:** AS3320 (DIP-18, [$5.95 Tubes and More](https://www.tubesandmore.com/products/dip-18); [€6.50, 332 in stock at Electric Druid](https://electricdruid.net/product/as3320-vcf/)) or AS3372E (§3.3). Sounds less Juno.

**Simulation ("verification-first"):** no CA-72-equivalent open model of a Juno board was found. Partial: an LTspice-checked expo converter for an ["open source Juno 106 filter clone"](https://sinneb.github.io/p306). An IR3109 behavioural model would have to be built (4 OTA stages + buffers) and validated against published curves [ENG]. **Weaker golden reference than the Model D.**

**Portability:** 4 voices on a ≈ 268 × 130 main board plus a voice strip fits the Little D envelope [ENG]. 6 voices likely needs a second board layer (voice cards).
**No rev 2:** feasible only with discipline: one voice-card design ordered ×4 (one design, so one tooling fee if the fab allows multi-qty; ESTIMATE), plus the breadboard spike of **one complete voice** before layout.

---

### 3.3 4-voice "Prophet-600-ish": AS3340 + AS3372E (rank 3)

- **The original:** the Prophet-600 paired ["CEM3340 oscillators with a number of CEM3372's that acted as both filter *and* amplifier"](https://sonicstate.com/news/2026/06/30/cool-tech-from-1982-the-prophet-600/). Same article: ["endless auto-tuning loops"…"it's impossible to get all 12 VCO's … in tune at once!"](https://sonicstate.com/news/2026/06/30/cool-tech-from-1982-the-prophet-600/). Autotune on a VCO poly is the hard part, and a 480 MHz Daisy with per-oscillator background re-tune is exactly what fixes it [ENG].
- **Chips (all DIP, in stock):**
  - **AS3340**: ["available in a 16-pin DIP package"](https://www.amplifiedparts.com/products/integrated-circuit-as3340a-vco-alfa-16-pin-dip), [€7.50 at Electric Druid](https://www.electricdruid.net/product-category/oscillators).
  - **AS3372E**: DIP-24 ("more pins than the original (DIP-24 instead of DIP-18)"), [€6.12, 94 in stock](https://electricdruid.net/?p=17405); contains ["a two-input voltage-controlled mixer, a 4-pole lowpass filter, and a voltage-controlled amplifier"](https://electricdruid.net/?p=17405).
- **Per voice:** 2× AS3340 + 1× AS3372E + 2 TL072 + CV S&H ≈ **$28–40** parts, ≈ 3,000 mm², ≈ 0.2–0.35 W (ESTIMATE). Envelopes in firmware (no AS3310s).
- **CVs:** per voice 2 pitch, PW ×2, cutoff, resonance, VCA, mix ≈ 6–8 → 24–32 for 4 voices: heavy S&H or many DACs. **This is the real cost and pin problem** [ENG].
- **Autotune:** 8 VCOs + 4 filters; counter mux; serial background re-tune. Moderate-to-heavy firmware, no trimmers.
- **Open references:**
  - [p600fw, "a CPU/firmware remake for the SCI Prophet 600", source GPL-3.0](https://gligli.github.io/p600fw) (its tuning code would be the reference; the page doesn't mention autotune, so its contents are **UNVERIFIED**).
  - [Profree-4, an open Prophet-5-based "4 analog voices"](https://synthanatomy.com/2022/04/pikopiko-factorys-open-source-prophet-analog-poly-synth-profree-4-is-now-on-kickarter.html): CC BY-SA after development, but it uses "SMD components" and the kit is ≈ €5,151, a warning on scope.
- **Simulation:** CEM/AS chips have no public transistor-level SPICE model that I found (**UNVERIFIED**); only behavioural models are possible. **This fails the CA-72-style golden-reference principle most clearly.**
- **Prophet-5 proper** (AS3340 + AS3320 + VCA per voice) is the same shape with one more chip and more CVs. Not better for a one-unit build.

---

### 3.4 Paraphonic Model D as a *new* build (2–4 voices, shared filter)

This is rank 1 if built on Little D. As a separate design it only makes sense with a 4th VCO (Mono/Poly / Matriarch shape): one more discrete Model D VCO ≈ $10–15 + 1 DAC channel + 1 counter (ESTIMATE). **Rank 1's Daisy osc 4 gets the 4th note for ≈ $1**, so a separate build isn't justified.

### 3.5 AS3394E voice-chip poly (SCI Six-Trak style)

- **Chip:** one DIP-24 per voice. ["voice-on-a-chip intended for software control by a microprocessor system"](https://uraltone.com/as3394e-alfa-mp-controllable-synthesizer-voice-pdip-24.html), with oscillator, mixer, 4-pole LPF and VCAs, "-4 and +4 volts" control inputs, €12.00, **"Ei varastossa" (out of stock)**. Erica lists the [SOIC-24 at €13.50, "Out Of Stock"](https://www.ericasynths.lv/shop/ics/as3394e-synthesizer-voice/).
- **Assessment:** per voice the smallest board and cheapest (≈ $15–20 including CV S&H, ESTIMATE). But it has **one** VCO per voice and **8 CVs** per voice, and it is **unavailable** today. Watch it; don't plan on it.
- **Open reference:** [polyUAnalog, open source, "AS3397" per voice ("two analog oscillators, a filter, and VCA")](https://synthanatomy.com/?p=83778). But the AS3397 is ["SOIC only"](https://sdiy.info/wiki/Alfarzpp), so it isn't through-hole.

### 3.6 Korg Polysix / Mono-Poly

- The SSM2044 is gone as new stock: [Electric Druid's "original unused vintage chips"… "Our stock of these chips is now exhausted", €25](https://electricdruid.net/product/ssm2044-vcf/).
- The reissue, SSI2144, is [SSOP-16, "reprises the SSM2044", "Pin connections were revised"](https://www.electrokit.com/en/ssi2144-ssop-16-voltage-controlled-low-pass-filter): **not through-hole.**
- **Verdict:** Polysix is out. The Mono/Poly's *idea* (4 VCOs, paraphony) lives in rank 1.

### 3.7 Oberheim OB-X-ish

- **Voice:** SEM-derived state-variable filter with OTAs. The AS3080E is through-hole ([DIP-8, Thonk](https://www.thonk.co.uk/shop/alfa-as3080e/)) and an AS3350 dual SVF is listed ["in DIP and SOIC"](https://sdiy.info/wiki/Alfarzpp). Which OB-X generation used which filter is **UNVERIFIED**.
- **Verdict:** more trims per voice, no open sim or reference found this session, and VCO autotune too. Highest scope; not ranked.

### 3.8 ARP Odyssey (duophonic)

- **The instrument:** 2 VCOs; filters 4023 / 4035 / 4075 depending on revision. A modern derivative, AMSynths Athena, offers a ["4075-style low-pass filter"…"upgraded" with 4023 and 4035 options](https://www.matrixsynth.com/2013/12/new-amsynths-athena-arp-odyssey-clone.html?m=0) (commercial, not open).
- **Verdict:** a full Odyssey is a new mono build of Little D's size, with a new SPICE effort (no CA-72 equivalent found). **Its signature duophony is free in rank 1.** Interesting only if the owner wants the ARP *sound* (4075 filter, ring mod, S&H) as a separate project.

---

## 4. Comparison table (one unit, ESTIMATE unless cited)

| | Voices | Chips/voice | Board added | Cost/voice | Total one unit | Power (22 Wh runtime) | Autotune per voice | Key chips THT? | Open refs / sim | Portability | One-unit, no rev 2 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Little D Para** | 1 voice, 3–4 notes | — | ≈ 0 | — | **Little D + $1.50–5** | unchanged (≈ 3.9–7.5 h) | already done | n/a | CA-72 unchanged | same | **Yes** |
| **Little J (Juno-60-ish)** | 4 (6) | AS3109 + ¼ AS2164 + 4 jellybean | ≈ 14k mm² (21k) | $22–35 | $350–520 | 1.8–3.5 W (≈ 5–10 h) | pitch none; amp + VCF auto | **AS3109 DIP UNVERIFIED** | pico-dco, PolyKit, chorus refs; no full sim | good at 4 | Possible, high effort |
| **P-600-ish** | 4 | 2× AS3340 + AS3372E + 2 | ≈ 12k mm² | $28–40 | $380–560 | 2.0–3.8 W (≈ 4.5–9 h) | 8 VCO + 4 VCF | Yes, all DIP | p600fw, Profree-4; **no chip-level sim** | OK | Possible, highest firmware load |
| AS3394E poly | 4 | 1 + S&H | ≈ 8k mm² | $15–20 | $300–420 | ≈ 4.5–9 h | 4 VCO + 4 VCF | DIP listed, **out of stock** | polyUAnalog (uses SOIC AS3397) | good | Blocked by stock |
| Polysix | 6 | SSI2144 + … | — | — | — | — | — | **No (SSOP)** | — | — | No |
| Odyssey | 2 notes | discrete | Little D-size new build | — | ≈ Little D | ≈ Little D | 2 VCO | discrete, yes | no open sim found | OK | Same risk as Little D |

---

## 5. Top 3: short case each

1. **Little D Para (+ osc 4).** It turns the planned mono into a 3–4-note paraphonic/duo hybrid with a Plaits-style digital source through a real ladder, for about the price of a toggle. It uses only hardware already specified (3 independent DAC pitch CVs, 3 autotune counters, full-chord Hall scan) and keeps the CA-72 verification intact. **Do it inside the current build:** add the toggle, the OUT R → EXT path, and a CPU check to the spike.
2. **Little J (4-voice Juno-60-style).** The best *new* instrument through this lens. DCOs remove the poly autotune nightmare. The Daisy covers envelopes and the famous chorus, a Pico 2 runs the DCOs (open pico-dco precedent), and per-voice power is lower than Little D's voice. **First gate:** confirm a through-hole AS3109 in stock. If none, the fallback is AS3320 and it stops being a Juno sound.
3. **P-600-ish (AS3340 + AS3372E).** All key chips are DIP and in stock, with the fewest chips per VCO voice. It's the classic poly whose famous flaw (tuning) is what the Daisy fixes. Against it: 8 VCOs to autotune, ≈ 24–32 CVs, and no transistor-level golden reference, so "verification-first" is weakest here.

## 6. Scope risk vs the current Model D build

- **Soldering:** Little D's single voice is ≈ 350 resistors and 13 TL072s (`budget-variant.md` §v1.3). A 4-voice poly adds ≈ 250–350 more resistors and ≈ 20–25 ICs on top of a similar control/keys/power/FX core [ESTIMATE]. Roughly **1.7–2× Little D's hand-build time**.
- **Firmware:** the poly assigner, per-voice CV refresh/S&H timing, DCO amplitude tables and N-filter cal are all new code. Little D's firmware is still unwritten.
- **Verification:** both poly options lose the CA-72-class golden reference. That is the principle most at risk.
- **"No rev 2":** a mistake in one voice card is copied ×N. Mitigate with a full one-voice breadboard spike before layout, or don't start a poly until Little D works.
- **Recommendation:** finish Little D with the Para mode (rank 1). Treat rank 2 as the *next* project, reusing Little D's proven Daisy control, keys, battery and FX code.

## 7. Open checks

1. AS3109 DIP: find an in-stock DIP part number (Alfa datasheet / Electric Druid package field).
2. AS3394E restock date (Uraltone back-in-stock alert).
3. Plaits engine + plate + tape echo CPU on a bare Seed (spike step 5).
4. Spare mux channels after DRIFT (≈ 46/48 used) for the VOICE MODE toggle.
5. pico-dco and PolyKit licenses (not shown on the pages read).
