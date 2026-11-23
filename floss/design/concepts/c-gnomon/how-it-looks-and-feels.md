# GNOMON: how it looks and feels (visual, idea level) — rev 5

2026-11-22. PROPOSAL (the director's idea). Read with systems' `how-it-works.md` rev 4, which sets the geometry.

**Picture:** `sheet.png` (14 × 29 in at 200 dpi; end view 3:2, 3/4 views 1:2). **Source:** `../_src/cathedral_sheets.py`, `sheet_gnomon()`.

## The owner's words this revision follows (verbatim)
- "Reverse the angle on the side behind the speakers so there’s still a subtle angle when upright" (rev 3).
- "I don’t like the angle on the back when laying flat. Make the base and the back 90 degrees when sitting flat" (rev 4, which replaces rev 3's back angle).
- "I miss the subtle rounded shape of cathedral" (rev 5, this pass). Earlier, on CATHEDRAL (2026-11-13 20:45): "I kinda want the corners to be softer and to be more architectural like how Apple does theirs".

## Geometry, as drawn ([calc] from how-it-works rev 4; nothing measured)
- **Slab:** T 35, D 105. **Playing angle:** tan θ = T / D ≈ 18.4°.
- **Back:** vertical in the playing pose, **square to the base (90°)**. The corner behind the speakers is 90° − θ ≈ 71.6°.
- **Upright:** stood on that back, the plate leans back by the same ≈ 18.4°. One angle serves both poses.
- **Sizes:** the back is ≈ 66.4 tall; footprint 280 × ≈ 88.5; overall ≈ 280 × 100 × 66, including the front face's forward lean.
- **Stretcher (SHOE only):** y ≈ 15–75 on the runner line.
- **Flat:** not offered.


## Rev 5: what "the subtle rounded shape of cathedral" means here
**What I read in CATHEDRAL** (from its renders, `design/branches/concepts/cathedral/img/`, mainly the standing and closed views, and its look file):
1. **Plan corners:** continuous-curvature superellipse corners (n = 5), so the curve leaves the straight edge with no visible start. The case is r 28.3, the plates r 24, concentric.
2. **Soft edges:** the rim's edges are eased, so the block reads as one soft, solid object, not as a sharp-edged extrusion.
3. **A concentric frame:** the cream plate's corners follow the case's corners, so the frame stays the same width all the way round.

**What rev 4 had lost:** GNOMON was drawn as a sharp extrusion. Square plan corners, hard long edges, a square-cornered plate. The section was right; the object wasn't soft.

**What I changed (all on the surface; rev 4's poses stay as he set them):**
- **Plan corners:** the same n = 5 superellipse at all four corners of the slab and cheeks (the end faces turning into the front and the back). **r = T/2 = 17.5**, CATHEDRAL's own proportion: 28.3 on a 55.2 case is ≈ half its thickness [calc].
- **Plate:** the cream field's corners are concentric superellipses, r 10. The walnut frame shows on all four sides, ≈ 8 at the ends.
- **Long edges eased:** lip r 16 (unchanged), front foot r 3. **The top-back edge stays at r 4:** it's the upright foot's tipping edge, and systems found r 8 drops the pull-to-tip to 1.64 N (rev 5 check). **The base-to-back corner is also a tight r 4**, so his 90° still reads as square.
- **Every edge of each end face rolled 3 mm,** so the ends read as one soft block. In the end view, the lighter band is the rounding turning away and the darker field is the flat face. The growth rings and the hairline sit on the flat face.
- **Not blobby:** the end-view silhouette is unchanged, and the rounding is ≈ 6 % of the length. No round masses (the lesson of DROP).
- **On the sheet:** view 8 sets a crop of CATHEDRAL's standing render beside GNOMON's corner at 3:4, so he can judge them side by side.

**For systems to check: geometry systems owns that the rounding changes** ([calc], UNVERIFIED):
1. **End faces:** the flat end face shrinks. In the slab band it's ≈ 64 long instead of ≈ 105, because ≈ 20.5 comes off at the front and at the back.
   - **The port mouth moves forward** to ≈ 60 along the plate (was ≈ 80), so the mouth and its groove sit on the flat.
   - **Jacks (systems rev 5, drawn):** one row of 5 on the right end face, centred ≈ 18.5 below the plate: phones, line, MIDI in, MIDI out, device USB-C. **Power, TUNE and MIDI SPLIT move onto the plate,** drawn as two small toggles and a small knob at the plate's right end behind the knob rows. **The split-target rail moves to the plate's front rim,** drawn as a fine cream scale on the walnut rim in front of the field.
2. **Back (the upright foot):** the flat contact runs ≈ 245 instead of 280, with rounded ends. The TPU strips get shorter. That matters for side-to-side upright stability, not front-to-back.
3. **Runners:** the 3 mm roll on the outer edge leaves ≈ 7 of each 10 mm cheek flat, so ground pressure on grass rises (≈ 3.8 → ≈ 5.4 kPa if the cheeks are the only contact). At the very ends the runner contact also curves away with the plan corner.
4. **Footprint:** still ≈ 280 × 88.5, now with rounded corners. The front foot line is shortened at its ends.
5. **Front face (host port):** unchanged across the middle. The host port, left of centre, stays on the flat.
6. **Plate:** knob rows start 24 in from the ends (was 22) to clear the plate's r 10 corners. Layout check.
7. **Cheek thickness 10** is my assumption: the plan corner (17.5) is bigger than the cheek, so the corner finishes in the slab above it. If systems changes the cheek, the corner can stay.

## The idea, as you see it
CATHEDRAL's lid standing on its own ends. A framed slab of constant thickness. At each end the rim carries on down into a cheek, and the slab is open underneath between the cheeks.

Seen from the end, in the playing pose, it's a calm shape:
- a flat base and a **vertical back meeting it square**;
- the plate sloping down from the top of the back to a rounded front lip.

Turn it onto that back and it stands upright, with the plate offered up to you at the same angle it had on the table.

## Why the shape (not costume)
- **The slab is the instrument;** the cheeks are the rim carried down.
- **Every proportion comes from the slab's two numbers.** The angle is tan⁻¹(T / D). The back's height is the plate's rise plus the slab's thickness.
- **The square base-and-back corner is his call, and it reads well.** On the table it's a quiet, architectural profile, a block with one sloped face, not a leaning wedge. Upright, the same corner becomes the foot, and the lean comes free.
- **One angle for both poses** makes the object easy to read: it has one slope. Whichever way it sits, it's tipped toward you by the same amount.

## On the sheet
| View | What it shows |
|---|---|
| 1. End view (3:2) | The square base-and-back corner marked; the engraved hairline one slab thickness below the plate (the lid plus its own thickness); growth rings centred on the port mouth; the lip rounded into the plate; the stretcher dashed (SHOE only) |
| 2. Playing (1:2) | Angled, with the keyboard in front. The end face's hairline and rings carry the "slab on its cheek" idea in the view the owner judges |
| 3. From behind (1:2) | Low, so the open underside between the cheeks shows; the jacks on the right end |
| 4. Upright (1:2) | On its back, the plate leaning back ≈ 18.4°, facing you |
| 5. Packed on SHOE (1:2) | With the stretcher |
| 6. Two poses (1:2) | Both end silhouettes, with a dashed vertical beside the upright plate marking ≈ 18.4° |
| 7. Loose (1:2, same size) | Module and keyboard separate: no carry part, no stretcher |
| 8. The cue | A crop of CATHEDRAL's standing render beside GNOMON's corner at 3:4 |

## CATHEDRAL cues it carries
| Cue | On GNOMON |
|---|---|
| Framed plate | CATHEDRAL's lid: cream plate, walnut rim, soft corners |
| Lancet grille | Two round lancet windows in the plate, over speaker E's drivers |
| Cathedral grain | Growth rings across both end faces, centred on the port mouth (left end, slab band) |
| Section-rule hairline | On each end face, T below the plate |
| Soft architectural corners | **Superellipse plan corners (n 5, r 17.5 = T/2) and a concentric plate (r 10), as CATHEDRAL; long edges eased, end-face edges rolled 3; the lip most (r 16)** |
| Brass, the one metal | None drawn: the port is grooves, the grip strips are printed TPU |
| Black knobs, one red hero | Two rows, DEPTH in red |
| Pipe façade | None (no surface seen in normal use) |

## Ports, as drawn
- **Port mouth:** left end, slab band, ≈ 60 along the plate (moved forward to sit on the flat end face).
- **Jacks:** one row of 5 in the slab band of the right end (phones, line, MIDI in, MIDI out, device USB-C).
- **On the plate:** power, TUNE and MIDI SPLIT at its right end; the split-target rail on its front rim.
- **Host USB-C:** on the front face, which is on top when upright (not drawn at this scale).
- **Back:** the upright foot, with TPU strips and nothing mounted.

## Materials (all printed except the knobs)
- Slab and cheeks: printed walnut-brown, rings and hairline printed in.
- Plate: printed cream.
- TPU grip strips on the runners and the back.
- Knobs: bought, black, one red.
- Stretcher (SHOE only): one flat print.

## Feel
- **Angled:** a lap desk. Your wrist rests on the rounded lip, the plate is at a writing angle, and the square back gives your hand a clean edge to lift it by.
- **Upright:** a music stand. The plate is tipped back ≈ 18°, so the face is offered up to you and the drivers aim up toward the ear. It's for listening, a shelf, a friend across the table, and light knob turns; systems' stability table has the limits.

## Open
- **"90":** is upright for playing or for standing it up (owner)? Systems' rev 4 stability figures apply.
- **D 105 vs 115 (eng):** at 115 the angle is ≈ 16.9° in both poses.
