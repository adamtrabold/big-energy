> **CUT in round 2 (director R2). Replaced by `../slab/`. Kept for history only.**

# CASE: how it works (systems)

**Kind:** designed for use. **Idea:** a clamshell. The lid is the panel; you
open it like a book and the panel ends up tilted behind the keys. Read
`../common-how-it-works.md` first; this file only covers what's different.

## Structure

| Part | Holds | Rough size (mm) |
|---|---|---|
| **Base** | the keyboard zone (keys, wheels, key board), 2P 18650 holder behind the key-comb root, the lid-sense magnet, rubber feet | 315 × 135 × 32 |
| **Lid** (= body) | voice board plus core board, the panel PCB, the speaker chamber at the lid's **far end, right**, the I/O edge on the lid's **hinge edge** | 315 × 135 × 30 (pot side) plus caps |
| **Hinge** | two printed or ordered pin hinges along the rear edge of the base, **a hard stop at about 165°**, a hollow pin for the cable | — |
| **Rear leg** | one laser-cut ply leg that flips out from the lid's outer face (it faces down when open) | about 70 tall |

- **Electrical split:** the lid has the core, voice and speaker; the base has
  the keys and battery.
- **Crossing the hinge:** a 4-conductor cable (VBAT, GND, TX, RX), pre-crimped
  JST at both ends, through the hollow hinge pin so it twists rather than
  bends. Strain-relief clips sit on both sides. Nothing analog crosses the
  hinge.
- **Why the battery is in the base, not the lid:** it balances the open
  instrument. The lid sits behind the hinge, the base and battery in front.
  The VBAT conductors carry the charge current (1 A or more), so 22 AWG or heavier.

## Geometry: open (playing) and closed (carry)

- **Closed:** the lid lies face-down on the base, with the knobs facing the
  keys. The panel sits in a 24 mm recess in the lid rim, so the hero cap
  clears the key tops by ≥ 2 mm. That makes the knob pocket the lid's rim
  depth. **Closed size: about 315 × 135 × 70 mm.** A magnet catch at the front
  holds it, and the Hall sensor sees it as closed.
- **Opening:** the lid rotates about 165° on the rear hinge. It ends up behind
  the keys, face-up, its far edge raised about **15°** toward the player.
  - The flip-out rear leg touches the table and takes the load. Pressing
    knobs pushes the lid toward flat, so the force goes **into the stop and
    the leg**, not into hinge friction.
  - No friction hinge is needed. There's one playing angle, which means fewer
    bought parts. (This changes the visual designer's any-angle friction-hinge
    idea. The reason: one angle is enough to play, and a stop plus a leg can't
    creep.)
- **Open footprint: about 315 × 270 mm** (the base, plus the lid behind it).
- **On the lap:** the leg can stay folded. The lid then rests at about 165°
  on the stop alone, which suits light knob use. For heavy use on the lap,
  rest the lid's far edge on your thighs or the couch.

## Placement against the rules

- **Speaker ↔ key sensors:**
  - **Open:** the speaker is at the lid's far end, at least 135 mm behind the
    hinge, so more than 60 mm away ✓.
  - **Closed:** the speaker sits over the key fronts, but the unit is asleep.
    Verify the speaker magnet doesn't pull the Delrin keys when closed (the
    small key magnets are attracted). Eng should test it; a steel shield cup
    is the fallback.
- **I/O edge:** it's on the lid's hinge edge. When open, the jacks face back
  and slightly down, and cables leave behind the instrument. When closed, they
  face the rear. The jacks never cross the hinge path.
  - About 180 mm of straight edge is available out of 315 ✓. USB-C, the master
    switch and the charge LED are at the right end.
- **Thermal (S7):** the core board (switcher, amp) sits at the lid's right
  end, by the speaker. The VCO arrays sit centre-left.

## Panel layout (lid, about 305 × 125 usable)

```
 far edge (raised)
 [range1][range2][range3]  [wave1][wave2][wave3]   (set-and-forget top row)   [ SPEAKER GRILLE ]
 [TUNE][MODMIX]   [FREQ2][FREQ3]  [mix x5 + on/off]  [F-A F-D F-S faders][L-A L-D L-S faders] [VOL][PHONES]
 ( CUTOFF )[EMPH]
 [CONT.AMT][GLIDE]        toggles row               [TUNE btn][HOLD btn] (RGB)(pip)
 hinge edge, nearest the keys
```

- The performance strip is at the **left end of the hinge edge**, so it's
  the panel's nearest-left point and directly above the wheels.

## Flows (deltas from jobs.md)

- **F1 open:** unlatch → swing the lid back to the stop → flip out the leg (optional) → wake → tune → play.
- **F4 pack:** fold the leg → close the lid → magnet catch → sleep.
- **F12 service:** the base plate holds the battery bay (4 screws). The boards are in the lid, behind its back plate (4 screws).

## Interaction patterns specific to CASE

- **The "not in control" light: variant V-a, one amber pip** beside TUNE and
  HOLD. It's lit while any knob isn't in control.

## States specific to CASE

| State | What happens |
|---|---|
| lid partly open, but not at the stop | still awake. The lid only reads "closed" when it's fully closed (Hall plus the magnet catch) |
| leg not deployed | playable. The lid rests on its stop |
| cable unplugged or broken | the key MCU goes silent, and the status LED double-blinks "no surface". MIDI still plays it |

## Build and making (rough)

- **Laser:** about 10 stack layers per half (base and lid), the leg and the grille.
- **FDM:** the hinge knuckles with a hollow pin (or bought brass tube as the
  pin), key tops, wheels and caps.
- **Bought:** the hinge pin, the cable, the magnet catch and the feet.
- **About 14 build steps** after soldering.
- **Ordered version:** a laser-cutting service plus JLC3DP for the small
  parts. Straightforward.

## Risks / open

1. The lid's cantilever when the leg is folded. Check the stop's strength by
   calculation and on a print.
2. The speaker magnet over the key magnets when closed (eng to test).
3. The closed thickness (about 70 mm) is set by the hero cap. A flatter hero
   cap (about 15 mm) saves about 5 mm.
