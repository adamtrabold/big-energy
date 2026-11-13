# DISH: how it works (systems), round-2 fix pass

**Kind:** sauce. **Idea:** a circle cut from the panel becomes a round dish on
a fork, tilting toward the player like a radio telescope. **The dish is the
MIDI-reachable instrument; the wings are the analog tone you set.** The dish
rises out of the speaker well.

Read `../common-how-it-works.md` first.

**Checked against:**
- **owner.md:**
  - "real parts";
  - "i want velocity";
  - "as silent as possible";
  - the knob/MIDI rule;
  - "joystick… one direction" / "even a fader";
  - "portable… small".
- **eng:**
  - v2 §2, §4.1, §4.2;
  - answers-E1-E10: E1 (mod VCA), E2 (speaker spacing), E4 (UART update
    to the dish MCU), E5, E7 (dish MCU, low-profile B, PUI AS04008MR
    driver);
  - budget §v1.4b route (b).
- **scores.md:**
  - round 2: D1–D5, F1–F5;
  - the pivot move (fork at the well's rear, 70°; dish at 50°; 75°
    standing detent), accepted.

**Fix pass:**
- **D1:** emphasis next to cutoff.
- **D2:** rigidity spec.
- **D3:** cable method and life.
- **D4:** lights off.
- **D5:** 38 mm accepted.
- **Plus:** the sleep sensor moved for E2, and a pip for the mod fader.

## The split (eng v2 §2, plus E1)

| Where | Controls | Electrical |
|---|---|---|
| **Dish (14)** | CUTOFF hero at the centre; a ring of 13: GLIDE, TUNE, RANGE 1, RANGE 2, FREQ 2, RANGE 3, FREQ 3, filter A/D/S, loudness A/D/S | All MCU-read, through a 4067 to the dish MCU (RP2350 module, E7). **4 wires cross** (5 V, GND, TX, RX), UART at 1 Mbaud. Firmware updates over the same UART (E4) |
| **Left zone** (22 mm, far left) | bend stick (slot-gated), **mod fader** | Pico-read. The mod fader is MIDI-ownable (E1), so **it gets its own pip** beside it |
| **Left wing** | **EMPHASIS at the wing's inner edge (D1)**, CONTOUR AMT, MOD MIX; OSC MOD, FILTER MOD, OSC 3 CTRL, glide-on; HOLD, TUNE, status LED | In-circuit pots; switches read by the main Pico. No MIDI on any of them (owner) |
| **Right wing** | mixer × 5 + on/off, WAVE × 3, W/P, EXT pad, FEEDBACK; KBD 1/2, DECAY; VOL, PHONES | In circuit |

- **What a player learns:** "turn it on the dish and MIDI can take it
  (plus the mod fader, which has its own pip); everything else is the tone
  you set."
- **V-d:** the bullseye ring glows when any of the 11 dish continuous
  controls is owned by MIDI and differs from its knob. RANGE is physical
  truth and isn't covered.

## D1. Cutoff and emphasis, reunited
- **EMPHASIS moves to the left wing's inner edge,** as close to the well as
  the fork allows: ≈ 6 mm clear of the raised fork's left arm.
- It gets **the second-largest cap on the instrument** (≈ Ø 20, bought).
- **Span, estimated from this geometry** (fork pivot at the well's rear,
  arms ≈ 60 mm at 70°, dish at 50°):
  - the dish centre ends up ≈ 165 mm from the front edge and ≈ 90 mm above
    the table;
  - EMPHASIS sits ≈ 120 mm from the front edge, on the panel (≈ 30 mm high),
    ≈ 66 mm left of the dish centre.
  - **Thumb on EMPHASIS to fingertip on the CUTOFF ring ≈ 100 mm**
    (√(66² + 45² + 60²)).
  - **That's under the director's 120 mm line**, but it's an estimate:
    **the visual's raised side view decides it, and the mock should state
    the measured span.** If the drawn span is over 120 mm, we say so.
- CONTOUR AMT sits just outside EMPHASIS on the same wing, so the left hand
  can sweep across it.

## D2. Dish rigidity spec

| Element | Spec | How it's met |
|---|---|---|
| **Dish axle at 50°** | Holds against a **15 N push, normal to the face, on the outermost knob** (r = 41 mm), so 0.62 N·m. **Holding torque ≥ 1.0 N·m** (×1.6 margin) | **Default:** a Belleville-washer friction stack on an M5 shoulder bolt through a brass bushing in each fork arm, with the torque set by a nyloc nut (≈ $5). **Upgrade:** bought constant-torque position-control hinges (Southco/Reell class, ≈ 1–1.5 N·m, ≈ $10–15 each, UNVERIFIED) |
| **50° and 75° positions** | Findable by feel | A **nylon-ball spring plunger** (bought, quiet) drops into two dimples at 50° and 75°. **A hard stop at 75°**, so a hard push past standing goes into the stop, not the friction |
| **Fork at 70°** | A push on the dish rotates the fork toward the rear. Moment ≈ 15 N × (60 + 41) mm ≈ 1.5 N·m | **A hard stop block at 70°** takes that direction (it can't drift back). The friction stack (≥ 0.5 N·m) only holds the fork against being pulled toward the player |
| **Fork lateral play** | **≤ 0.5 mm at the dish rim under a 5 N sideways push; ≤ 1° twist under 15 N** | 12 mm-wide laser-stacked arms (walnut ply), a **cross-tie bar** joining the arms under the dish (it stows in the well floor's front groove), brass bushings reamed to the bolt |
| **Verify** | A 15 N spring scale on the outermost knob at 50°: no movement. A dial indicator at the rim under 5 N sideways | First assembly |

## D3. Cable: 4 cores through 2 pivots

| Pivot | Range | Method | Rated life |
|---|---|---|---|
| **Fork pivot** (well rear) | 0–70°, a bend, not a twist | A **service loop** of bought 4-core fine-stranded silicone cable (28 AWG class) crossing the pivot as a U-loop, bend radius ≥ 15 mm, clipped either side | Fine-stranded silicone wire at ≥ 10× bend radius, flexed 70°, is typically in the 10⁵+ cycle range. **UNVERIFIED for the chosen cable.** The need is ≈ 37,000 cycles (10 opens a day for 10 years) |
| **Dish axle** | ≈ 230° (face-down → 50/75° → face-up flat) | A **6-wire capsule slip ring** (bought, ≈ Ø 12–22 mm, Adafruit-class, ≈ $15–25), in the right fork arm's hub. 5 V and GND on 2 rings each, TX and RX on 1 each. The friction stack sits on the left arm | Vendor ratings are typically in millions of revolutions (**UNVERIFIED** for the chosen part). The need is ≈ 37,000 × 0.6 rev |

- **Brush noise on UART:** the link already frames and checks every packet.
  CRC plus resend, with ≈ 100 µF at the dish end to ride through contact
  dips. Eng's "swing 1,000 times" error-rate test (E7) covers it.
- **Why not twist cable through the axle:** 230° over a ≈ 100 mm length is
  ≈ 2,300°/m. Torsion-rated cables are typically specified around ±180°/m,
  so it would fail early.

## D4. Lights off
- The contour knobs lose the envelope picture the faders drew.
- **Systems has no objection to the visual's gold arc joining each contour's
  A/D/S pointers.** Bought knobs carry a white or glow line in the cap, and
  the arc is printed on the dish face.
- Otherwise, the loss is **accepted knowingly:** MIDI reach and the bullseye
  meaning are worth more than the shape.

## D5. Size, accepted
- **292 × 188 × 38 mm**, played and carried, flat, no lid.
- **38 against the box's 36 is accepted (D5).** The extra 2 mm sinks the
  wing caps below the rim, so it carries with nothing proud.

## Structure

| Part | Holds | Size (mm) |
|---|---|---|
| **Base** | Left zone (stick + fader). Key zone: **K-E maple button plugs, two rows, on Choc V2 silent + magnet + TO-92** (keys menu). Strip C; D + battery under the keys. Panel zone: left wing, the **well (Ø 116, 23 deep)**, right wing. A/B under the wings, and a low-profile B extension under the well's front two-thirds (E7 rules: ≤ 8 mm parts; no VCO cores, ladder or contours there). The speaker (PUI AS04008MR, 40 × 5 mm) + PAM8302 sit under the well's rear third. I/O along the rear face | **292 × 188 × 38** |
| **Fork** | Two arms plus a cross-tie, pivoting at the **well's rear edge**. Lies flat forward in channels beside the well when stowed; swings up to a 70° stop | arms ≈ 60 |
| **Dish** | A round face PCB: 14 controls, 4067, dish MCU, light ring. Back skin is the second canvas | Ø 112 × 21 incl. caps |

**Depth budget:** 5 + 62 keys + 3 + 116 well + 2 = **188**.

**Ring at Ø 112:** radius 41 mm, chord 19.7 mm between cap centres, 12 mm
caps, upright legends at r 48–52, hero ≈ Ø 28 inside a light ring at
r 15–18.

## Placement against the rules

| Rule | Check |
|---|---|
| **Speaker ↔ key sensors** | Speaker ≈ 160 mm from the front, sensor line ≈ 35 mm: **≈ 125 mm** ✓ |
| **Sleep (DRV5023 + dish rim magnet)** | **Moved to the well's left edge at mid-depth** (E2 asks ≥ 50 mm from the speaker magnet; it's ≈ 70 mm). ≈ 90 mm from the key sensors ✓ |
| **Plunger and stops** | Not magnetic ✓ |
| **I/O** | 292 mm straight rear face ✓ |
| **Thermal** | D under the keys ✓ |

## States

| State | What happens |
|---|---|
| dish face-down in the well, fork flat | asleep |
| raised (50° / 75°) or face-up flat in the well | awake |
| a hard push at 50° | it holds (D2). Past the 75° stop it can't go |
| dish link fault (slip ring, cable) | status LED shows "dish lost"; the dish controls hold their last values; wings, keys, stick, fader and MIDI all work |

## Build and cost (R8, F1)

| Item | Detail |
|---|---|
| **Laser** | ≈ 10 base layers, fork arms + cross-tie, dish rim rings, well grille |
| **Owner-cut** | K-E plug carriers (acrylic), F5 |
| **FDM** | none visible. The slip-ring hub adaptor may be printed (hidden, structural) |
| **Bought** | maple button plugs, 25 Choc V2 silent + magnets, dish MCU, 4067, slip ring, silicone cable, Belleville washers + shoulder bolts + bushings, nylon-ball plunger, stick, slide pot, knobs, PUI driver |
| **Steps after soldering** | **18** (+1 for the slip ring) |
| **Cost vs SLAB** | **+$40–60**: dish MCU ≈ $5, slip ring ≈ $15–25, pivot hardware ≈ $8, dish PCB area, low-profile B, plunger; minus SLAB's lid. The constant-torque hinge upgrade adds ≈ $20–30 |
| **Full instrument, one unit (F1)** | **≈ $570–920** |

## Risks / open
1. **Board area:** the tightest of the three (E7). The VCO layout decides
   it; the fallback is +15 mm of depth.
2. **The weakest speaker of the three** (Fs 400 Hz, E7).
3. **The D1 span is an estimate.** The visual's raised view must measure it.
4. **The slip ring and silicone-cable ratings are UNVERIFIED.** Pick the
   parts with datasheets at BOM time.
