# Key menu: how each option works (systems), round-2 fix pass

This file **replaces** my round-2 draft (K1–K6, Delrin combs, rockers, let-off).
The owner has since ruled:
- "yes finished instrument should be real parts";
- "i dont want to print knobs and keys";
- "i dont want to steal a keybed";
- "i want velocity";
- "i guess i could cut at vector space" (key tops: owner-cut, material cost
  only).

The menu now follows the visual's K-A to K-F (`how-it-looks-and-feels.md`,
`key-menu.png`) and the director's key ruling (scores.md round 2, items 1–5).

**Checked against:**
- owner.md (the entries above, plus "as silent as possible", "op-1 style
  keys", "phase8… the buttons", "drum machine style pads");
- **eng budget-variant.md §v1.4b rev 6 (route (b))**, key-sourcing.md;
- answers-E1-E10 E10 (strip footprints ≥ 6.5 mm apart).

Serves both instruments: the full version (strip C) and Little D (its 3 key
strips, same sensing, one firmware).

## The mechanism under every switch-based key (was K-C; F2)
- **Kailh Choc V2 silent** switch: a dampened low-profile switch, 2.8 mm
  travel. It gives feel and return. Its contacts are unused, and its small
  steel spring is a fixed field offset that gets calibrated out.
- **A 5 × 2 mm magnet** glued into a laser-engraved pocket under the key top
  (acrylic or wood, so glue works), **beside the switch, along the key's
  length**.
- **A standing TO-92 SS49E** on the strip, face ≈ 3.5 mm below the magnet at
  rest and ≈ 0.7 mm at the bottom. It runs at 3.3 V to stay in the Pico ADC
  range (eng: confirm on the datasheet).
- **The sensor stands *beside* the switch, under the magnet, never under the
  switch.** The visual's section drawings should show it that way.
- **Velocity:** the time between two thresholds. Pressure: no (the switch
  bottoms out).
- **Silence: 4/5.** The switch is dampened and the sensing is contactless.
- **Stem fit:** Choc V2 has a cross stem. Each top carries a **laser-cut
  cross socket in a 3 mm acrylic under-layer** (owner-cut). Cut one test
  coupon first. It's a laser cut, not a printed sample.
- **Cost for 25:** ≈ $50–55 (eng §v1.4b: switches $17.50, sensors $11.40,
  magnets ≈ $8, acrylic $8, shipping $5, adapters $0–5). That's ≈ $5 more
  than route (a).
- **Fallback:** Gateron LP Hall switches with a flat-mounted TO-92S (route
  (a)), **pending eng's ≈ $8 bench test**. Louder, and the sensor position
  is unverified.
- **One straight sensor line:** every option places its magnets on one line.
  Two-row layouts put the front row's magnet at the rear of its top and the
  rear row's at the front. E10 needs footprint centres ≥ 6.5 mm apart, and
  piano x-positions give ≥ 8.7 mm ✓.

## The options

| Key | How it works | Travel | Silence | Velocity | Cost (25 keys, route b) | Build (after soldering the strip) | Fit |
|---|---|---|---|---|---|---|---|
| **K-A flat 1u caps** (OP-1-like grid; phase8 "separate buttons" look) | Square laser-cut caps (≈ 16 × 16) on the mechanism. Naturals in a front row, sharps raised in a rear row. Each magnet sits at the cap's inner edge | 2.8 mm | **4/5** | yes | **≈ $50–55** | 4 steps: seat 25 switches, cut 25 caps + sockets, glue magnets, press caps on | Flattest. Little D's first choice. Any concept |
| **K-B lever tops** | Long piano-shaped tops (naturals ≈ 55 mm visible, sharps ≈ 35) on the mechanism, **hinged on a 2 mm steel rod at the rear** (it answers eng's "long tops rock on one stem"). The switch sits under the top's middle and gives spring and stop. Pivot to switch ≈ 30 mm, pivot to front ≈ 55 mm, so **the front travels ≈ 5 mm** (2.8 × 55/30). The magnet sits near the front for the largest swing | ≈ 5 mm at the front | **4/5** (felt strip on the rod rail against tick) | yes | **≈ $55–65** (+ rod, rail, wood for walnut tops) | 6 steps: rail + rod, switches, cut tops, magnets, sockets, fit | **SLAB; MOTTO in walnut, reverse colours.** Most "instrument". **DOCK's 80 mm tops** are possible on any concept with the depth (not on these three) |
| **K-D silicone pad sheets in key layout** (owner's drum-pad idea) | A bought silicone button-pad sheet laid in a laser-cut key-shaped frame. **For velocity, each pad needs a magnet glued under it, over a Hall** (no switch) | ≈ 2 mm (**UNVERIFIED**, sheet-dependent) | **5/5**, the quietest | **only with magnet + Hall per pad: UNVERIFIED** travel and swing | pad sheet cost UNVERIFIED; + magnets ≈ $8 + sensors $11.40 | 4 steps | Familiar Maschine feel; least "keyboard" |
| **K-E maple button plugs, two rows** (Critter & Guitari reference) | Bought turned maple button plugs, each glued to a **small laser-cut acrylic carrier** on the mechanism. The carrier extends to put the magnet on the line between the rows. Felt collars in the top skin stop rattle | 2.8 mm | **4/5** with collars | yes | **≈ $55–65** (plugs ≈ $5–10) | 5 steps | **DISH** |
| K-F Fatar TP/9 | A real bought keybed | — | — | yes | — | — | **Honesty note only:** ≈ 352 mm for 25 keys, too wide |

**Any straight-row key fits SLAB and MOTTO** (K-A, K-B, K-D).
**DISH's well depth suits K-E** (62 mm zone).

## Feel without printing (owner: no printed samples)
- Eng's ≈ $8 bench buy (2 Choc V2 silent, 2 Gateron LP Hall, 5 SS49E) plus a
  few magnets and one pad sheet (visual's ≈ $12 list). Press them on a desk.
- It answers silence and velocity before the strip is ordered.

## Retired (owner rulings)
- the laser Delrin comb and the printed combs;
- rockers;
- magnetic let-off shims;
- cast silicone and printed TPU pads;
- donor or harvested keybeds;
- the OP-1 replacement keyboard.
