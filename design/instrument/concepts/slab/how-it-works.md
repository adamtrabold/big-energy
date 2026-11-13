# SLAB: how it works (systems), round-2 fix pass. Replaces CASE (R2)

> **Fix pass:** applies F1–F5, S1, S2, and the E2 lid-switch spacing. See common `Checked against` for the owner.md and eng revisions.

**Kind:** designed for use. **Idea:** one rigid body with no joint and no cable
crossing anything. A separate lid covers the panel and keys for carrying.
To play, the lid **folds in half and snaps under the body's rear** to become a
wedge stand that tilts the instrument toward you. The keys never separate,
only the cover does (DOCK separates the keys: different in kind, R2).

Read `../common-how-it-works.md` first.

**Checked against:**
- **owner.md:**
  - "portable… which means small";
  - "dont over index on OP1… should feel good to use";
  - "two octaves… minimum";
  - ready-made modules / cost reset;
  - MIDI-control entry;
  - "explore the light thing";
  - "as silent as possible".
- **eng v2:** §4.1 (boards A–D), §4.2 (height), §5b (power), §2 (MIDI scope).
- **scores.md:** R1, R2, R7, R8.

## Structure

| Part | Holds | Size (mm) |
|---|---|---|
| **Body** | Left zone (22 mm): bend stick + mod fader (common §2). Key zone: **K-B lever tops on Choc V2 silent + magnet + TO-92** (keys menu), strip C, and **board D plus the 2 pouch cells under the keys**. Panel zone behind: A over B. The speaker plus the PAM8302 sit in a 48 × 48 notch at the panel's **rear right**. I/O runs along the rear face. | **292 × 185 × 34** |
| **Lid** | Two leaves joined by a **sewn leather or felt hinge strip** across the full width (Vector Space has the sewing machines and leather). The **panel leaf** is 292 × 105 and the **keys leaf** is 292 × 80. Both are 12 mm laser stacks in the look's material: a frame, a 3 mm skin, and **a 1 mm felt lining inside** so the caps never scuff it (S2). There are magnets at the ends of each leaf, and a south-pole sense magnet in the panel leaf's **rear-left** corner. | 292 × 185 × 12 flat; 292 × 105 × 24 folded |

### Depth budget (front to back)

| Section | mm |
|---|---|
| Front lip | 5 |
| Key zone (K-B tops ≈ 55 mm, plus the rear rod pivot and the strip) | 75 |
| Panel zone | 100 |
| Rear wall and jacks | 5 |
| **Total** | **185** |

That's inside R1's 170–190.

### Height
- **The panel is sunk 4 mm** below the body's top. That leaves 28 mm for
  eng's control stack (§4.2 low end).
- **Caps stand 8 mm above the rim**, so the lid's 12 mm leaf (3 mm skin +
  1 mm felt + 8 mm clearance) clears them. The bend stick and fader top out
  at ≤ 8 mm too.
- **The keys' top surface sits 1.5 mm below the rim** (J16: a flat object
  can't press a key).

### Electrical
- It's eng's layout exactly: **A/B under the panel, and D plus the battery
  under the keys.**
- Nothing moves and nothing crosses a joint.
- The stick and fader sit in the left zone. Both are Pico-read (the fader
  drives the E1 AS3360), so there's no analog lead to B.

## Geometry: three states of the lid

| Lid state | How | Result |
|---|---|---|
| **Cover (carry)** | The lid lies flat on the body: the panel leaf over the panel and the keys leaf over the keys. End magnets hold it. | **292 × 185 × 46 mm**, one flat block. The sense magnet presents **south** to the DRV5023 under the **rear-left** rim, so the unit sleeps. **≈ 230 mm from the speaker** (E2 asks ≥ 50) ✓ |
| **Stand (desk play)** | Lift the lid off and fold the keys leaf under the panel leaf (a Z-fold; magnets hold the fold). Press the 24 mm block onto the body's underside at the rear: four steel discs in the base catch the leaf's magnets. | The body's rear rises 24 mm plus 3 mm feet, so it tilts **≈ 8°** toward you: atan(27/185). The block stays clear of the key zone, which keeps the stand magnets > 60 mm from the sensors. The sense magnet now faces away, the Hall sensor sees north or nothing, and the unit **stays awake**. |
| **Flat (lap, or no lid)** | The lid off and set aside, or laid flat under the whole body. | 0°. The body is rigid on a lap, and a lid under it adds a stiff 12 mm base. |

- **Why a fold and not a one-piece wedge:** a one-piece lid gives only 3–5°
  when flipped under. Two leaves stacked give 24 mm, so ≈ 8°.
  - The fold is a sewn strip with no electronics, so the **body** keeps "no
    joint".
- **One angle: 8°** (director S1). There's no second position.

## Panel (280 × 96 usable, from left to right; the rows run front to back)

| Section | Front row (nearest the keys) | Middle | Rear |
|---|---|---|---|
| **Play** (left, ≈ 52 wide, directly right of the stick and fader) | GLIDE + glide on | CUTOFF hero (≈ 28 Ø cap) | EMPHASIS, CONTOUR AMT |
| **Controllers** | OSC MOD, FILTER MOD, OSC 3 CTRL toggles | TUNE, MOD MIX | — |
| **Oscillators** | FREQ 2, FREQ 3 | WAVE × 3 | RANGE × 3 (Lorlin, MCU-read, no ring) |
| **Mixer** | on/off × 5, W/P, EXT pad, FEEDBACK | levels × 5 (17 mm pitch) | — |
| **Contours** | KBD 1, KBD 2, DECAY | 6 faders, 11 mm pitch, 20 mm travel (block ≈ 70 × 40) | — |
| **Out** (right) | TUNE btn, HOLD btn, status LED, **one amber pip (V-a)** | VOL, PHONES | **speaker grille Ø 50** at the rear-right corner |

- **Gold rings (F4, as corrected):** on the 12 ownable controls, including
  the mod fader. None on RANGE or the stick.
- **Placement check:**
  - The performance group sits right next to the stick and fader: the left
    hand moves between bend, mod, cutoff and emphasis without travelling.
  - The pip sits by HOLD and TUNE, which are the reclaim buttons.
  - The grille is above the speaker notch.

## Placement against the rules

| Rule | Check |
|---|---|
| **Speaker ↔ key sensors** | The sensor line is ≈ 30 mm from the front, and the speaker centre ≈ 155 mm from the front: **≈ 125 mm** ✓ |
| **Stand magnets** | At the rear underside, under the panel zone: > 80 mm from the sensor line ✓ |
| **Lid end magnets** | Outside the key run (left zone and right wall) ✓ |
| **Lid switch ↔ speaker** | Rear-left vs rear-right, ≈ 230 mm ✓ (E2 ≥ 50) |
| **I/O** | 292 mm straight rear face, against ≈ 260 needed ✓ |
| **Thermal** | Board D (boosts, DCWN) is under the keys, away from B's VCOs (eng §4.1) ✓ |

## Flows (deltas from jobs.md)

| Flow | Steps |
|---|---|
| **F1 open** | Lift the lid. The Hall sensor loses south, so the unit wakes and tunes. Then either fold the lid into the stand and press it under the rear (2 actions), or set it aside. Play. |
| **F4 pack** | Pull the stand off the base, unfold it, and lay it on the body. The magnets seat it, and the unit sleeps. |
| **F12 service** | The base plate (4 screws) exposes D and the battery under the keys. A/B come out after the pot nuts. |

## Interaction patterns
- **V-a, one amber pip:** "some knob isn't in control."
  - Move knobs until it goes out, or press HOLD + TUNE to reclaim all.
  - It covers the 12 ownable controls (common §4).
- **The stand is the only "mechanism",** and it has no wrong way:
  - Folded wrong, it's 12 mm instead of 24, and the tilt is shallower.
  - Mounted backward, the steel discs still catch it.
  - In either case the sense magnet faces away, so it can't put the unit
    to sleep.

## States

| State | What happens |
|---|---|
| lid on | asleep |
| lid off, anywhere | awake |
| lid under as the stand (sense magnet facing down) | awake (unipolar sensor) |
| lid half-seated on top | the end magnets pull it flat. If the sense magnet is ≥ 10 mm off, the unit stays awake (fails safe: you can't carry it "off" by accident, but the master switch exists) |
| key strip cable fault | the key Pico goes silent, and the status LED double-blinks "no keys". MIDI still plays it |

## Build and cost (R8)

| Item | Detail |
|---|---|
| **Laser** | ≈ 9 body layers, 2 × 4 lid layers, the grille |
| **Sewn** | 1 hinge strip |
| **Owner-cut at Vector Space** | 25 K-B key tops (acrylic or wood), material cost only (F5) |
| **FDM** | none |
| **Bought** | 25 Choc V2 silent + 25 key magnets + a 2 mm steel pivot rod; bend stick (#2765), mod slide pot, skirted knobs; 12 lid/stand magnets, 4 steel discs, feet, DRV5023, felt |
| **Steps after soldering** | **12**: key switches + tops (2), strip C + stick/fader (1), D + battery (1), A/B into the body (2), panel + nuts (1), base (1), lid leaves (2), hinge strip (1), magnets (1) |
| **Cost** | **Baseline, $0 delta.** **Full instrument, one unit ≈ $530–860** (F1; eng E-answers summary). Lid materials ≈ $10–15, inside eng's enclosure line |
| **Ordered version** | A laser service plus JLC3DP for the small parts. Nothing over 250 mm needs printing |

## Risks / open
1. **Stand stiffness:** 4 magnet-to-disc catches must hold against a knob
   press at the rear row. Target: no slip at 20 N downward at the rear edge.
   Test on the first print.
2. **Lid switch: resolved** (E5: DRV5023 TO-92, unipolar).
3. **Speaker notch: accepted** (E2). B slack falls to ≈ 5 %; eng's fallback is +10–15 mm of depth.
4. **The fabric hinge wears.** It's a replaceable strip held by the leaf
   layers, not glued.
