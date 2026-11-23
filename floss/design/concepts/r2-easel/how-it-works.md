# EASEL: how it works (systems, idea level) — rev 1

2026-11-22, round 2, turn 5. PROPOSAL (director, round 2 turn 4 + update).

**Owner, verbatim:**
- 20:46: "I do like one that sits up at an angle with a narrow footprint, I feel like that wil be most convenient for tables on the go esp with an external keyboard — like cathedral at least but without the keyboard".
- 20:46: "Why would I have two mono speakers that’s stupid. Drop to one speaker".

**Marks:** [calc] = my arithmetic from published data. Mass ≈ 0.66 kg and the centre of mass (COM) are ESTIMATES. UNVERIFIED = eng or a trial. The owner measures nothing.

## The idea
CATHEDRAL's raised lid, standing on its own. The framed plate stands at **60°**. The end faces are tall soft triangles carrying the growth rings. One fixed arrangement, no moving parts, the narrowest footprint of the four.

## Section, from the parts (end view; y back from the front, z up)
- **60°:** CATHEDRAL's lid stood at 120° to its base [`design/branches/concepts/cathedral/`]. "At least" that, so not less.
- **Plate length L ≈ 100 is set by the one driver.**
  - TEBM28 is 24 deep [eng r2], so with skin and air it needs ≈ 30 behind the plate over its magnet (Ø ≈ 25, UNVERIFIED) and ≈ 5 under its Ø 55 rim.
  - In this section the depth behind the plate peaks low and tapers to nothing at the top.
  - For L ≈ 70 the deep band is only ≈ 15 long and the magnet doesn't fit. **It first fits at L ≈ 95; L = 100 gives margin** [calc]. Driver centre at s ≈ 31 up the plate.
- **Front face f = 12:** holds the USB-C host port, low, facing the keyboard.
- **Back height:** 12 + 100 sin 60° = **98.6**, with a vertical back.
- **Footprint, two versions:**
  - **A, the director's ratio, "the footprint is half the face":** F = L/2 = **50**. A 30-60-90 section (short leg = half the long side), with a 30° apex at the top.
  - **B, footprint : height = 1 : φ:** F = 98.6 / 1.618 ≈ **61**. The extra 11 becomes a soft flat roof at the apex.
  - **I recommend B** (stability below). B also makes the triangle actually *soft*: a 30° apex with an r 8 round loses ≈ 23 mm of height, whereas B's roof corners (150° and 90°) round easily.

## What's inside (one driver; eng's option C: one TEBM28, ported, ≈ 120 cm³ net, Ø 12 × 155 port; **UNVERIFIED for this form**)
- **Box:** low behind the plate's centre, x ≈ 95–185, around the driver (the one lancet grille on the axis, as the director ruled). That's ≈ 1,800 mm² of section × ≈ 80 long. The port tube runs along x through the left bay to a **mouth on the left end face**, low (the rings centre on it).
- **Cells (2 × 50 × 60 × 7.5):** one per end bay.
  - **B:** flat on the floor at the back, z 2–9.5. **The mass sits low and back.**
  - **A:** the floor is only ≈ 46 wide, so they stand against the back wall (z 2–62), and the COM sits higher.
- **Boards:** pot boards behind the plate either side of the box (≈ 2 × 55 × 90) plus a vertical board in each bay against the back. **B ≈ 24,000 mm²** against ≈ 16,000 needed. A is tighter. That's **four boards with harnesses, against two in the slab**: more build steps. UNVERIFIED (eng).
- **Controls:** all on the plate, beside and around the grille, **no higher than s ≈ 40–45** (see stability).
  - The upper plate (s 60–100, depth 23 → 0) is too thin for pots. It carries **only the lights** (port light, battery, tempo ring) and the rim.
  - Power, TUNE and SPLIT sit on the plate low.
- **Jacks:** on the right end face, low, in **two rows** (3 + 2: phones, line, MIDI in/out, device USB-C) at z ≈ 14 / 28. Plugging in pushes along x, across the 280 width, so it never tips.
- **Host USB-C:** on the front face. Plugging pushes backward at z ≈ 6, so tipping back needs ≈ 20+ N, and it slides first.

## Stability [calc; mass 0.66 kg (one driver, ASA shell ≈ 0.19); COM ≈ 27–30 back, 29–33 up: ESTIMATES]
A press into a 60° face pushes mostly **backward**, so the plate tries to tip back over its rear edge. Force at which it tips back, pressing square to the plate:

| Control height up the plate | **A (F 50, cells upright)** | **B (F 61, cells flat)** | F 70 (for reference) |
|---|---|---|---|
| s 20 (low row) | ≈ 17 N | ≈ 70 N | never |
| **s 40 (top row)** | **≈ 4.6 N** | **≈ 7.5 N** | ≈ 12 N |
| s 60 (if a row went here) | ≈ 2.6 N | ≈ 4.0 N | ≈ 5.6 N |

- **Knob turning is mostly torque**, so it's fine on all versions.
- **A firm button press** (tact switches ≈ 1.6–2.6 N, fingers overshoot, UNVERIFIED) is safe on B at s ≤ 40, marginal on A.
- **A palm resting on the ridge** pushes down, ahead of the rear edge, so it steadies it: fine.
- **A pull toward you at the ridge tips it forward at only ≈ 1.5–2 N on every version.** Height is the problem, and a wider foot barely helps. Grab it low, by the ends.
- **What "narrow" honestly costs:**
  - the controls are confined to the lower ≈ 45 mm of the plate;
  - B's +11 mm foot (61 instead of 50);
  - a light pull at the top tips it.
  - At the ratio's 50, a firm press on the top row can rock it back. **Even so, B's 61 is still about half of SILL's 115.**

## Table, lap, grass
- **Café table: its best case.** 280 × 61, the keyboard in front.
- **Grass:** ≈ 0.46 kPa, so fine on firm level ground. Static ground tilt tolerance ≈ 30° back / 33° forward. On soft turf the rear edge may sink under a press (UNVERIFIED).
- **Lap: the weak case.** A tall object on a 61 mm foot on a moving lap. Steady it with a thumb on the ridge, or set it on the bench beside you.
- It has **no second pose.** Laid on its back, the panel faces away; don't.

## Packing and the keyboard
- **Prism:** 280 × 61 × 98.6 ≈ **1.08 L** (A: 280 × 50 × 98.6 ≈ 0.77 L). The smallest volume of the four, but tall. It stands calmly on its base in a bag pocket.
- **SHOE docks on the vertical back face** (98.6 ≥ 60 ✓). The S9 dock slides top to bottom, with a detent at the bottom; keys out.
  - Bundle ≈ 325–388 × 77 × 99–135 (the keyboard sets the length and height).
  - The base is too shallow for the 60-long dock.
- **The plate faces outward when packed:** protection is the rim 1 mm over the knobs only. Weakest of the four on job 33.
- **Bag to sound:** out, keyboard off, set down, plug in (3–4 moves).

## Making and weight
- **Fully printed: no pin, no metal.** The shell prints in two halves along the axis, or as three bays at the dividers, on a ≥ 300 bed or through a service.
- **Module ≈ 0.6–0.75 kg** [est].
- **Named trial:** the S9 fit on a vertical face.

## Randomness
"bookends" (`secrets`): a bookend stands tall on a narrow foot because the mass sits low on its base. Taken: the cells go flat on the floor at the back (version B).
Not taken: making the keyboard the foot. A plate under the keyboard is an appendage, and the keyboard moves while you play.

## Owner forks
- Does EASEL **replace** flat-or-slightly-angled, or join it? Job 32 as written (rev 6) says flat or slightly angled.
- A (50, the narrowest) or B (61, steadier).
- Carry: SHOE on the back / loose.

## UNVERIFIED
- The driver's magnet size.
- Box C in this section.
- The four-board split.
- Mass and COM.
- Tact-switch forces.
- Turf sinking.
