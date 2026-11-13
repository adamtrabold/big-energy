# CASE: how it looks and feels (visual)

Mock: `case-mock.png`. Read `../common-looks-and-feels.md` first.

## The idea as an object

- **Closed**, it's a quiet felt block, **282 × 76 × about 50 mm**. That's
  hardcover-book-sized and fits a laptop-sleeve pocket.
  - A small brass catch on the front, three brass hinge knuckles at the
    back, and the wordmark on the lid's outer face. That's all you see.
- **Opening is the event** (theodolite case). The felt lid swings back to
  its stop, and the black panel and gold rules appear behind the keys.

## Look

- **Field:** warm-grey wool felt laminated over grey ply, a cork base, a
  black panel PCB, gold ENIG rules, warm-grey caps with glow pointers, and
  an orange cutoff.
- **The look sheet** shows CASE in Proof and Desk too.
- **Keys:**
  - Naturals are bone (#e3dfd5).
  - Sharps are warm grey (#66625b), not black. That's quieter, and it
    avoids the toy-piano black-and-white.
  - Glow strips sit on the sharp fronts.

## Sizes (from the mock)

- **Lid** (panel half) 282 × 76. **Base** (key strip) 282 × 76.
- **Open footprint** about 282 × 152 (plus the leg).
- **Lid angle** 15° on a hard stop, with a fold-out leg.

## Motion and feel

- **Open:** thumb the brass catch, then lift.
  - The lid rotates about 165° and lands on its stop with a felt-damped
    thud, never a clack.
  - The leg flips out from the lid's outer face.
  - The status LED starts breathing as soon as the lid leaves the base. The
    Hall sensor reads "open" at more than 20°.
- **Close:** fold the leg in, and the lid comes down.
  - The magnet catch pulls the last 5 mm, so it *closes itself* the way a
    good laptop does.
  - The LED fades out over 300 ms instead of snapping off.
- **Systems changed my any-angle friction hinge to a hard stop plus a leg.**
  I accept it. One angle is the right call for something you press knobs on.

## The "not in control" light: V-a, one amber pip

- **Where:** a 1.4 mm amber pip just up and right of the cutoff hero, inside
  the play section.
- **Behaviour:** soft steady glow while cutoff or glide is held by MIDI;
  never blinks.
- **Why there:** now that only about 2 parameters are MIDI-ownable, the pip
  sits where those parameters live. It's no longer a general "something
  somewhere" alarm.

## States specific to CASE

| State | Visual |
|---|---|
| lid partly open (not at the stop) | awake. Breathing or steady LED as normal |
| key cable fault | status double-blink |

## Open questions

1. **Thickness:** is about 50 mm closed acceptable against "small"? The
   floor comes from the pots, jacks and key travel (see the common file).
2. **Short keys:** 52 mm whites. Do they feel too stubby? Print a
   one-octave sample.
3. **Speaker:** the 36 mm speaker in the lid sits about 30 mm behind the
   hinge when open. Check the 60 mm magnet rule against the key strip's
   sensors (eng).
