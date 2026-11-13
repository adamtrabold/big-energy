# How it works: shared by all three concepts (systems), round-2 fix pass

The concepts are **SLAB** (designed for use), **MOTTO** and **DISH** (sauce).
**DOCK is retired** (scores.md, round 2). Everything in this file is the same
in all three, so each concept file only covers what's different.

**Checked against:**
- **owner.md, newest entries first:**
  - "lets do the joystick… i need both behaviors. joystick is great if we
    can go one direction";
  - "even a fader could be sweet";
  - "i want velocity.";
  - "knobs midi cant control should not send midi and midi should not be
    able to flip switches…";
  - "yes finished instrument should be real parts";
  - "i dont want to print knobs and keys";
  - "i guess i could cut at vector space";
  - "i dont want to steal a keybed";
  - "i do want them to be as silent as possible";
  - "readymade modules… small";
  - "dont over index on OP1… feel good to use";
  - the MIDI-control entry (jump-on-move);
  - "all of this yes" (J1–J19, including J12/J13).
- **eng, with revisions:**
  - architecture-v2.md rev 0: §2, §4.1, §4.2, §5b;
  - **answers-E1-E10.md** (E1 rev 1, E2, E3, E5, E7, E8, E10);
  - budget-variant.md §v1.4b (rev 6, key route (b)) and §v1.5–v1.5b (rev 7, stick).
- **scores.md, round 2:** F1–F5, S1–S2, M1–M4, D1–D5, plus the
  coordinator's correction on mod (§2 below).

## 1. Electrical blocks (eng v2 §4.1, as amended by E2/E3/E7)

| Board | Contents | Placement rule |
|---|---|---|
| **A: panel/control** | Pots, rotaries, toggles, LEDs; jacks along its back edge | Under the panel (≈ 280 × 95–100) |
| **B: voice** | VCOs, ladder, VCAs, contours, LDOs, **plus the E1 AS3360 mod VCA** | Under A on headers. DISH adds a rigid low-profile B extension under its well (E7) |
| **C: key strip** | 25 standing TO-92 SS49E in one straight line, footprints at all 25 x-positions (E10: centres ≥ 6.5 mm apart) | Under the keys |
| **D: digital/power** | 2 × Pico 2, DACs, charger, boosts, DCWN06A. **The PAM8302 is no longer here: it mounts at the speaker** (E2) | Under the keys, in the same rigid body as B (the ribbon carries ±10 V and the CVs) |
| **Battery** | 2P LiPo pouch, ≈ 8 mm | Under the keys |
| **Speaker** | ≥ 40 mm driver + PAM8302 (≤ 50 mm leads, twisted) + its own battery pair (E2) | ≥ 60 mm from the key sensors, **≥ 50 mm from the lid Hall switch** (E2), ≥ 30 mm from the VCO cores (E8) |

**Joint rule:** only power plus UART crosses a moving joint.
- SLAB and MOTTO have no electrical joint.
- DISH: 5 V, GND, TX and RX through two pivots, to the dish MCU (E7).

**Height (eng §4.2):**
- control section 28–32 mm;
- key section 31–36 mm;
- caps ≤ 8 mm above the body rim (panel sunk 4 mm).
- **Lids need a 12 mm leaf:** 3 mm skin + 1 mm felt lining (S2) + 8 mm clearance.

## 2. Left zone, keys, and the mod correction

### Width: 292 mm (F3)

| Section | mm |
|---|---|
| Left zone (stick + mod fader) | **22** |
| Key run | 261 (15 naturals at 17.4) |
| Walls | 2 × 4.5 |
| **Total** | **292** |

- The keys don't shrink (director F3).

### Left zone (F3, eng §v1.5b)
- **Bend: Adafruit #2765 mini thumbstick** (17.5 × 17.4 × 12 mm,
  through-hole, $2.50).
  - Its Y axis only is read.
  - A **front–back slot** in the panel (the stick's own width × ≈ 18 mm
    long) gates it to one axis. It springs back to centre: push away to bend
    up, pull toward you to bend down.
  - **The slot ends are lined with 1 mm felt,** so the stick never clacks
    against hard edges (owner: silence).
  - It's mounted on a small carrier so its cap tops out ≤ 8 mm above the
    rim, which keeps it under the lid.
- **Mod: a slide pot ("fader") behind the stick,** running front–back.
  - ≥ 20 mm travel, cap ≤ 8 mm above the rim, **no spring** (it stays put).
  - Bought part. It's the owner's "even a fader could be sweet".
- **Both are bought parts** (owner: real parts). No printed wheels.

### Mod depth is MIDI-controllable (coordinator's correction to director F4 / controls ruling 3)
- **The owner confirmed J12/J13 ("all of this yes"):** mod in from MIDI, and
  the wheel sends MIDI out.
- **Eng E1 (rev 1) delivers it:**
  - the mod fader is **read by the Pico**;
  - an **AS3360 VCA** in the mod path sets the depth from the 8th MCP4728
    channel;
  - feedthrough is **auto-nulled during autotune** (no trimmer).
- **The owner's "no MIDI" rule** ("knobs midi cant control should not send
  midi") covers controls MIDI *can't* control. The mod fader *is*
  controllable, so it **sends and receives CC1, with jump-on-move.**
- **This makes 12 MIDI-ownable continuous controls,** not 11. Every
  "11" from round 2 becomes **12**:
  - gold rings;
  - MOTTO pips;
  - DISH (see its file: the mod fader gets its own pip).
  - **Director: this overrides F4's "no ring on mod"** per the
    coordinator. No ring on RANGE or bend.
- **Bend:** Pico-read, summed with MIDI bend (no ownership). It sends bend out.

### Keys (F2, eng §v1.4b route (b))
- **Default mechanism:**
  - a **Kailh Choc V2 silent** switch (feel and return);
  - a **5 × 2 mm magnet** in a laser-engraved pocket under the key top,
    **beside the switch** along the key's length;
  - a **standing TO-92 SS49E** on strip C, face ≈ 3.5 mm below the magnet
    at rest, ≈ 0.7 mm at bottom.
- **Velocity** comes from the time between two thresholds (owner: "i want
  velocity").
- **The sensing is contactless.** The only noise is the dampened switch.
- **Gateron LP Hall switches (route (a)) are the fallback,** pending eng's
  ≈ $8 bench test.
- **Key tops:** laser-cut acrylic or wood, **owner-cut at Vector Space,
  material cost only** (F5). The magnet glues into acrylic or wood; nothing
  is Delrin now.
- **One straight sensor line for every key option:** magnets of the front
  row sit at the rear of their tops, and magnets of the rear row at the
  front of theirs (keys file).
- **Firmware:** lowest-note priority, single trigger. Velocity is on MIDI OUT;
  it's off for the voice by default.

## 3. Panel (R1 minimums, unchanged)
- Caps ≥ 12 mm Ø at a ≥ 17 mm pitch; faders ≥ 11 mm pitch with ≥ 20 mm
  travel; legends ≥ 2.5 mm.
- About 19,200 mm² is needed in a ≈ 280 × 100 panel.
- **Knobs are bought:** skirted knurled caps, plus one large hero cap
  (controls ruling 4).
- **RANGE is a Lorlin 6-way rotary, MCU-read.** It's physical truth, with
  no gold ring.
- **I/O:** ≈ 16 jacks at a 14 mm pitch along board A's back edge, plus
  **one USB-C** (E3: charging, USB-MIDI and firmware; charging works while
  MIDI runs) and the master switch.
- **Firmware entry:** hold TUNE at power-on.

## 4. MIDI ownership and the light

| Class | Controls | Rule |
|---|---|---|
| **MIDI-ownable (12)** | GLIDE, TUNE, FREQ 2, FREQ 3, CUTOFF, filter A/D/S, loudness A/D/S, **MOD (fader)** | Last touched wins, with jump-on-move. Each sends CC when moved. Gold ring |
| **Switches** | RANGE × 3, OSC 3 CTRL, DECAY, KBD 1/2, glide on, and every other toggle | **MIDI can't flip them** (owner). No CC out |
| **Knob-only** | EMPHASIS, mixer × 5, MOD MIX, CONTOUR AMT, waveforms, volumes | **Send no MIDI** (owner). E9 dual-gang pots: not needed |
| **Bend stick** | — | Summed with MIDI bend; sends bend |

- **Reclaim all:** HOLD + TUNE, CC121, or sleep and wake.
- **Deadband:** 2 % within 150 ms.

| Light | Concept |
|---|---|
| one pip (V-a) | SLAB |
| **12 pips** (V-c) | MOTTO |
| bullseye for the 11 dish controls, **plus one pip by the mod fader** (V-d) | DISH |

## 5. Speaker, sleep, magnets
- **Speaker:** a ≥ 40 mm driver.
  - SLAB and MOTTO: in the 48 × 48 A/B notch (E2, accepted; B slack falls
    to ≈ 5 %).
  - DISH: under its well (E7: PUI AS04008MR-2-LWC80, 40 × 5 mm).
- **Lid sleep:** a **DRV5023 unipolar TO-92 Hall switch** (E5), power-gated.
  - **Placed ≥ 50 mm from the speaker magnet** (E2). Each concept file says where.
- **All magnets** (lid, stand) stay ≥ 60 mm from the key sensors.

## 6. Enclosure and cost (F1)
- **Laser-cut stack** at Vector Space.
- **No printed user-touched parts** (owner). Keys, knobs, stick and fader are
  bought; key tops are owner-cut. If any printed part remains, it must be
  hidden and structural, and the concept file names it.
- **One-unit price.** The eng base first unit is **≈ $530–860** (E1 + E3 +
  E5 added: answers summary).
  - Route (b) keys are ≈ $50–55, inside eng's $45–90 keys line.
  - Stick plus fader cost about the same as the wheels they replace.

| Concept | Δ vs SLAB | **Full instrument, one unit** |
|---|---|---|
| **SLAB** | $0 | **≈ $530–860** |
| **MOTTO** | +$35–60 | **≈ $565–920** |
| **DISH** | +$40–60 (round-2 fix pass adds a slip ring for D3) | **≈ $570–920** |

- The visual's round-2 sheet showed DISH at +$30–50. **The fix-pass figure is
  +$40–60**, from the parts list in `dish/how-it-works.md`.

## 7. Eng asks: status
| Ask | Status |
|---|---|
| E1 | **Accepted** (AS3360, auto-null) |
| E2 | **Accepted** (notch; PAM8302 at the speaker; 50 mm from the lid switch; 30 mm from the VCOs) |
| E3 | **Accepted** |
| E4 | SWD from the main Pico; UART update for the DISH dish MCU |
| E5 | **Accepted** (DRV5023) |
| E6 | Moot (DOCK retired) |
| E7 | **Accepted**, with low-profile rules |
| E8 | **Accepted**, with conditions (MOTTO M1) |
| E9 | Not needed (owner: knob-only controls send no MIDI) |
| E10 | **Accepted** |
