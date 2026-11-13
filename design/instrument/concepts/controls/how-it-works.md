# Controls menu: knobs, bend and mod (systems), round-2 fix pass

This file **replaces** my round-2 draft. The owner has since ruled:
- "yes finished instrument should be real parts", so printed caps and
  printed wheels are out;
- "lets do the joystick… i need both behaviors. joystick is great if we can
  go one direction";
- "even a fader could be sweet";
- "knobs midi cant control should not send midi and midi should not be able
  to flip switches".

It follows the director's controls ruling (scores.md round 2), **with one
correction from the coordinator on mod (below).**

**Checked against:**
- eng budget-variant.md §v1.5–v1.5b rev 7 (stick, mod);
- **answers-E1-E10 E1 rev 1** (AS3360 mod VCA, auto-nulled);
- v2 §2.

Serves both instruments.

## Mod depth: MIDI-controllable (correction to director ruling 3 / F4)
- **The director's ruling** said mod is a knob-only analog pot that sends no
  MIDI, with no AS3360.
- **The coordinator corrected it:**
  - the owner confirmed J12/J13 ("all of this yes");
  - eng E1 delivers it: a **Pico-read mod control → AS3360 VCA, feedthrough
    auto-nulled during autotune**;
  - the owner's "no MIDI" rule covers only controls MIDI *can't* control.
- **So the mod fader is read by the Pico, sends and receives CC1, and follows
  jump-on-move.**
  - It's the **12th MIDI-ownable control**, with a gold ring and a pip where
    the concept uses pips.
  - The AS3360 stays in both instruments: E1 for the full version, §v1.5
    for Little D.
- **Any sheet text saying "mod sends no MIDI" should be reversed.**

## Lead (both instruments)

| Control | Part | How | Silence / robustness | Cost |
|---|---|---|---|---|
| **Bend: one-axis spring-return stick** | **Adafruit #2765** mini thumbstick, 17.5 × 17.4 × 12 mm, through-hole | Y axis read only. A **front–back panel slot** gates it to one axis (push away = up). It springs to centre. Sits in the **22 mm left zone** (body ≈ 292 wide, F3), on a carrier so its cap is ≤ 8 mm above the rim | The slot ends are felt-lined, so it never clacks. The plastic gimbal is fine at hand forces; if the slot edge is the stop, the stick's own end-stops never take load | **$2.50** |
| **Mod: slide pot that stays put** | A bought 45 mm-class slide pot, ≥ 20 mm travel, plus a bought cap | Behind the stick in the same zone, front–back. Pico-read, drives the AS3360, CC1 in and out | Silent; a felt strip under the slot against dust | ≈ $1–2 |
| **Knobs** | Bought skirted knurled caps, plus one large hero | — | Silent | ≈ $0.30–0.42 each, hero ≈ $2–4 |
| **RANGE** | Lorlin 6-way rotary, MCU-read | Physical truth; **MIDI never sets it**; no gold ring | Soft detent tick | ≈ $2–3 each |
| **Contours** | Slide pots, 11 mm pitch (SLAB, MOTTO); knobs on DISH's dish | — | Silent | ≈ $0.60–1.20 |

- **Firmware for bend:** the stick reads ±full scale. A small centre deadband
  (≈ 3 %) absorbs the spring's imperfect return. It's summed with MIDI bend.

## Also on the menu (not on the mocks)

| Option | Status |
|---|---|
| **Touch strips** (SoftPot 50 mm, $8.95) | Owner: "touch strip is cool too". Kept as an option; costs more than the stick |
| **Abacus faders** | Off the mocks (director). On the menu with **bought wooden beads** on brass rods over hidden slide pots (real parts) |
| **Thumbwheel pots** | A fallback mod control; pricing UNVERIFIED |
| **Shared / flip controls** | Not recommended: it breaks panel-as-patch |
| ~~Printed caps, printed wheels, edge wheels, zipper-detent racks~~ | **Retired:** owner "real parts" |

## Little D note
- **Same lead:** #2765 stick + slide pot + AS3360, about $8–11 for
  bend/mod (eng §v1.5).
- **Controls are still ≈ $21 of its cost.** The savings to reach a lower price
  are elsewhere (fixed costs), as before.
