> **RETIRED in round 2 (scores.md). Kept for history. Its long-key idea lives on as a note on K-B in the key menu.**

# DOCK: how it works (systems), round 2

**Kind:** designed for use. **Idea:** the keyboard is a separate module. It
docks against the body's front to play, and turns face-up onto the panel to
be the lid (Polaroid SX-70: the camera is its own case).

Read `../common-how-it-works.md` first.

**Checked against:**
- **owner.md:**
  - "portable… which means small";
  - "dont over index on OP1… should feel good to use";
  - "two octaves… shouldn't effect pcb size";
  - ready-made modules;
  - MIDI-control entry;
  - "as silent as possible".
- **eng v2:** §4.1 (D must sit with B; the ribbon carries ±10 V and CVs),
  §4.2 (height), §5b (battery current 2.9 A worst case), §2.
- **scores.md:** R1, R3, R7, R8.

## Systems finding first: R1 and R3 can't both hold for DOCK as defined

**1. The module has to be as deep as the panel it covers.**
- R1 grows the panel to 95–105 mm deep.
- The module is the lid, so it must be ≥ 100 deep. In round 1 it was
  76 mm, over a 70 mm panel.
- **Consequence:** played depth = module (≥ 100) + body (≥ 100 panel +
  what else lives in the body).

**2. The body has to hold board D, and it has nowhere to put it.**
- Eng §4.1: D is linked to B by a ribbon carrying ±10 V and the DAC CVs,
  so D can't go in the module (joint rule).
- In every other concept D and the battery live under the keys. In DOCK the
  keys are the module.
- D can't stack under B: 28–32 + 14 = 42–46 mm, against R1's ≤ 36.
- **Best fit:** eng reshapes D as a **270 × 30 strip** (≈ 8,100 mm²; E6)
  behind A/B.
  - Pico 2 (21 mm wide), DCWN06A (20 mm) and the bq24074 (≈ 28 mm) all fit
    in one row.
  - The charger stays in the body, next to the single USB-C (E3). Only its
    BAT output crosses the dock, as VBAT.

**3. The battery moves to the module.**
- VBAT then crosses the dock. That's allowed: it's power. Worst case is
  2.9 A (eng §5b), so it uses **2 VBAT pins and 2 GND pins**. The pogo
  rating per pin is UNVERIFIED and must be ≥ 2 A.
- **The module's exposed pads are dead until docked.** A P-MOSFET in the
  module only connects the battery when the body grounds DETECT, so keys or
  coins in a bag can't short the pack.
- **Side effect, and a good one: power-by-dock.** (The body's charger can
  still run on USB with the module away, but the system load sits on the
  battery node, eng §6, so the body is treated as off.)
  - Module away or on top: the body has no power, so it's asleep. No Hall
    sensor is needed.
  - **Lost:** round 1's "module set aside, body plays from MIDI" state. It
    was never a job (J12 still works with the module docked).

**4. Carried thickness can't get below ≈ 56 mm; R3.2 asked for < 45.**

| Layer | mm |
|---|---|
| Body control stack (eng §4.2 floor) | 28 |
| Caps above the body rim (panel sunk 4) | 8 |
| Thinnest possible key module (no battery: comb, strip, shells) | 20 |
| **Floor** | **56** |
| **Realistic, with the battery in the module (33 mm)** | **≈ 70** |

- A shoulder or skirt around the panel can hide the 8 mm gap from view.
  It can't remove it.
- **< 45 is not reachable** without breaking eng's stack.

### Draws (real randomness, `secrets.choice`)
- **Oblique Strategy: "Use an old idea."**
  - Since the module must be ≥ 100 deep anyway, DOCK takes the oldest idea
    in keyboards: **full-depth keys.**
  - Its lever whites are ≈ 78 mm visible, the longest in the set and close
    to a real keyboard's pivot-to-front ratio.
  - **This turns the depth penalty into DOCK's feel advantage** (owner:
    "feel good to use").
- **Unrelated field: harp pedal notches.**
  - The module locates on **two notched cleats** on the body's front face.
    It drops down into the notch, like a harp pedal falling into its slot.
  - It replaces round 1's cones: you feel the seat, and gravity plus the
    magnets hold it.
  - The cleat faces carry felt, so the seat is silent.

## Structure (honest numbers)

| Part | Holds | Size (mm) |
|---|---|---|
| **Body** | Panel zone: A over B, with the speaker notch at the rear right. Behind A/B: the D strip (E6), including the charger. The I/O sits on the rear face, above the D strip. The front face has 6 pogo pins (VBAT × 2, GND × 2, TX, RX), DETECT on a shorter pin, and 2 cleats. **The wheels** sit at the front-left corner (see below). | **285 × 136 × 32** |
| **Module** | Long lever keys (K1-long). Strip C. The key Pico. The 2 pouch cells under the keys. **No ports on the module:** the body's charger (USB-C, E3) charges the cells across VBAT. ENIG pads on the rear face. | **285 × 100 × 33** |

| State | Footprint (mm) | Volume |
|---|---|---|
| **Played** | **285 × 236 × 33**, one flat slab | — |
| **Carried** | **285 × 136 × ≈ 70** | ≈ 2.7 L; SLAB is 2.4 L |

- **Played depth is ≈ 45 mm over R1's 190.** That's the honest cost of
  module-as-lid at R1 panel depth.

### Wheels
- With the mod wheel analog (eng v2 §2), the wheels **can't live on the
  module.**
- They sit on the **body's front-left corner**, standing 8 mm above the
  panel (inside the module's cap pocket when carried).
- Played, they're behind and to the left of the lowest keys, ≈ 100 mm back
  from the key fronts. That's a worse reach than SLAB.
- **If eng accepts E1** (mod depth as a VCA), the wheels move onto the
  module, beside the keys, where they belong. **DOCK benefits from E1 more
  than any other concept.**

## Geometry
- **Playing:** the module drops onto the cleats against the body's front
  face. The end magnets pull it the last few mm, and DETECT closes, so the
  unit powers and tunes.
- **Carry:** lift the module (power drops: notes off, sleep), turn it over,
  and lay it on the body.
  - Its flat underside covers the panel.
  - A 9 mm skirt on the module's underside rim sleeves over the body's top
    edge, hiding the cap gap and locating it.
  - End magnets hold it.
  - The keys face up, inside a rim 2 mm proud of the sharps.

## Panel
- It's the same layout as SLAB (`../slab/how-it-works.md`, Panel), but the
  play group shifts right by the 16 mm wheel pod at the front-left.

## Placement against the rules

| Rule | Check |
|---|---|
| **Speaker ↔ sensors** | The speaker is at the body's rear right. The module's sensor line is ≈ 60 mm from the module front, so the distance is **≈ 150 mm** ✓ |
| **Dock magnets** | At the module ends, outside the 261 mm key run ✓. Lid magnets likewise |
| **I/O** | The rear face is 285 mm ✓. When the module lies on top it doesn't cover the rear face |

## Flows (deltas)

| Flow | Steps |
|---|---|
| **F1** | Lift the module off the top, set it in front, and let it drop onto the cleats. It powers, tunes, and the LED goes steady. |
| **F4** | Lift the module (sleep), flip it, lay it on the body. |
| **F5 charge** | Charge through the body's USB-C. **The module must be docked or lying on top to charge.** Docked or on top: the DETECT path must exist in both, so **the module's top-side rim also carries 2 sprung contacts that meet pads on the body rim** when stowed. That puts charging and power on the same 4 lines. **Open (eng):** the alternative is charging only when docked. Simpler, but "charge it in the bag" goes away. |
| **F8 MIDI** | Works only with the module docked. |

## Interaction patterns
- **V-b, no persistent light.**
  - One amber flash when MIDI first takes any of the 11 ownable controls.
  - HOLD + TUNE reclaims all.
  - This is the "less is more" option for the owner.
- **Docking can't be done wrong.** The cleats only take the module keys-up
  and facing the right way: the cleat notches are asymmetric.

## States

| State | What happens |
|---|---|
| module docked | on |
| module on top | off (no DETECT); charging if USB-C is plugged in and the rim contacts are fitted |
| module away | body off; the module's pads are dead |
| contact bounce | serial quiet > 50 ms → all notes off. A power drop is held up by bulk caps for ≈ 20 ms (eng to size), otherwise it's a full reboot and re-tune. **Risk** |

## Build and cost (R8)

| Item | Detail |
|---|---|
| **Laser** | ≈ 9 body layers, ≈ 5 module layers, the grille, 2 cleats |
| **FDM** | key tops, wheels, caps, the pogo carrier |
| **Bought** | 7 pogo pins (≥ 2 A rated), a P-MOSFET plus a resistor, 4 magnets |
| **Steps after soldering** | **14** |
| **Cost vs SLAB** | **+$15–25** (pogo pins, the gating MOSFET, ENIG pad board, cleats; minus SLAB's lid) |

## Risks / open
1. **It's over R1's box (played 236 deep, carried ≈ 70 thick).** Director's
   call: accept DOCK as "the long-key one" over the box, or retire it.
   - **My view:** its carry volume matches SLAB's, and its keys are the best
     in the set.
   - But it's 51 mm deeper played than SLAB, and its wheels are badly
     placed unless E1 lands.
   - I wouldn't promise it a 9 without E1.
2. **VBAT across pogo pins at 2.9 A worst case.** Use paired pins and verify
   the pin rating (E6).
3. **Brown-out on a knocked dock** forces a reboot and re-tune (2–4 s).
   The cleats and gravity make a knock unlikely. Bulk hold-up is an eng
   sizing question.
4. **The D strip reshape (E6)** is eng's to accept.
