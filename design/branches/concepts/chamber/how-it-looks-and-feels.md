# CHAMBER: how it looks and feels (visual)

Seed: FOLD-105 (v1.1). Kind: an instrument case. **Point of view: closed, it's an organ case; open, it's a console.** Emotion: joy. Read with `how-it-works.md` (systems rev 1) and `../common-how-it-works.md`.

**Rev 1, 2026-11-13, concept turn 1 (visual).** Images in `img/`, made by `design/concepts/_mock-src/rb.py` (models) and `figs_rb.py` (web figures). Words live here, not in the images (owner).

## The three states, in the order you use them
Closed, you carry the façade. Flat, it's just a console and the façade is face down. Standing, the façade faces the listener and the console faces you.

| State | Image |
|---|---|
| Closed, beside a 400-page hardback (real walnut, seen from behind so the pipes stand upright) | `img/chamber-closed-with-book.jpg` |
| Closed, first print (walnut-tone wood-fill) | `img/chamber-closed-printed.jpg` |
| Open flat: the console | `img/chamber-open.jpg`, `img/chamber-flat-from-above.jpg` |
| Standing at 120°: the console side | `img/chamber-standing.jpg` |
| Standing at 120°: what the friend on the bench sees | `img/chamber-standing-from-behind.jpg` |

## Principles (each follows from the idea)
1. **The façade is the instrument's own scale.**
   - 25 pipes, one per key, C to C. Each length is 66 × 2^(−n/12) mm, so the longest is four times the shortest.
   - They're laid out the organ builders' way: the tallest on the axis, then alternating outward.
   - *Because* decoration that comes from the keyboard's numbers is information, not costume.
2. **Line, not picture.**
   - The pipes are single engraved lines (0.6 mm) with a brass-tone fill: conical foot, mouth, body, flat top. No shading, no fake 3D, no tracery (director).
   - *Because* brass on dark walnut tips into steampunk the moment it's drawn as an object instead of as a drawing.
3. **Outside dark, inside light, and the keys rhyme with both.**
   - Outside: dark walnut with light lines. Inside: a light plate with dark knobs.
   - The keys sit between: walnut naturals cut from the same walnut as the body, maple sharps.
   - *Because* that makes it read as one object with two faces, not a box with a sticker.
4. **Brass is the case hardware.**
   - Stays, hinge pins, and the six back screws. The screws sit on the façade's plinth band as its rivets, so they become part of the drawing instead of interrupting it.
5. **Serif only where the organ speaks.**
   - RANGE in feet (lo, 32', 16', 8', 4', 2') and the nameplate. Everything else stays in v1.1's FOLD hand (Kalam).

## Look
- **Body:**
  - first build: walnut-tone wood-fill PETG (#6b4429, matte);
  - later: his planed walnut, oiled.
  - Halves 286 × 108; closed **52.7** (lid walls +2.6 for the pegs; v1.1: 50.1). See `img/chamber-closed-front-exact.png` (exact front elevation, dimensioned).
- **Façade (lid back):**
  - pipe field x 23–263, feet on an impost line at d 18, a plinth line at d 10, tops up to d 84;
  - lines 0.6 wide, fill brass-tone (#e2bf6a drawn);
  - the three d 12 screws sit between the plinth and impost lines;
  - feet: the front pair moved to d 6 (systems), dark rubber; the rear pair at d 78.
  - **First build:** a printed relief, 0.4 mm proud lines on the lid back, filled with brass-tone wax. **Real-walnut version:** engraved and filled.
  - Whether engraved fill reads on wood-fill PETG is UNVERIFIED (eng / maker coupon).
- **Pickguards:** v1.1 cream (#f1ebdd), 45° bevel, black legends, warm-grey rules. Unchanged apart from what's listed here.
- **Keys:** reverse pegs (systems §2).
  - Naturals: walnut button plugs in the body's tone. Sharps: maple (HUSH's #e3c493).
  - Each sits on a 14 mm dark-grey felt washer in a counterbore. Heads 12.7, tops 6.5 above the plate.
  - The key window closes into a deck: the base pickguard runs to the front rim.
  - 1:1 detail: `img/chamber-pegs-12.41px-per-mm.png`; close render: `img/chamber-reverse-pegs.jpg`.
- **RANGE in feet:** EB Garamond 1.2 mm.
  - 16' and 8' in a low row above each knob; 32' and 4' in a higher row; lo and 2' tucked under the end ticks.
  - They follow the TYPE switches' fan rule, because at 20 mm pitch, labels set round the knob collided with the neighbour's.
  - 1:1: `img/chamber-range-feet-12.41px-per-mm.png`.
- **Section names (oscillators, mixer, contours):** moved up to d V1 + 17.5 (was + 11.3), clear of the feet labels.
- **PARA:** its legend moves *above* its toggle and shortens to "mono / para / +4". Beside the toggle it sat on RANGE 3's 4'. **Wording change: systems / owner to accept.**
- **FREE / SYNC:** a black-bat FOLD toggle at lid (133, d 70.6), "free" left and "sync" right, in the hand at 0.72 × legend size.
- **TIME's two scales** (inner ms, outer divisions, over ±135°):
  - divisions are marks only: a tick for straight, a dot beside the tick for dotted, a small triangle for triplet;
  - no numbers (CHAMBER keeps the panel quiet; DIPTYCH is the one with numbers);
  - 1:1: `img/chamber-time-dial-12.41px-per-mm.png`.
- **TIME / DECAY legends:** behind their knobs (common §2).
- **Name:**
  - v1.1's 32 × 6 lozenge no longer fits between the moved TIME and DECAY legends, so it shrinks to **16 × 5 on the axis at d 94.6**. Blank until he names it (director).
  - Systems put the nameboard on this lozenge because the strip above the keys is ≈ 3 mm.
- **Status light:** under a hood (common §3): a dark Ø 6 well with the LED deep in it.

## Motion and feedback
- Pegs: ≈ 2.5 mm down onto felt, silent. The walnut naturals and maple sharps feel the same; only the colour is reversed.
- Lid: the v1.1 brass stays, unchanged (firm click at the stop, soft knock onto both stays).
- Echo tempo: v1.1's tempo flash on the one status light (H7), with echo-clock.md's lock / loss flashes.

## What it had to prove (director), and where
| Must prove | Where | Status |
|---|---|---|
| (a) closed bar reads "organ case", not "decorated box", beside the book | `img/chamber-closed-with-book.jpg` | My read: yes, from above and behind. The tower of plain lines reads as pipes, and the brass screws as hardware. **Seen from the front, closed, the pipes point toward you** (their feet are at the hinge), so they read upside down. That's the price of facing the listener when standing. |
| (b) closed height with pegs | `img/chamber-closed-front-exact.png` | **52.7** (systems' check), drawn exactly. |
| (c) reverse pegs at 1:1 | `img/chamber-pegs-12.41px-per-mm.png`, `img/chamber-reverse-pegs.jpg` | Drawn. |
| (d) engraved fill on wood-fill | — | Eng / maker coupon. First build = printed relief + wax fill. |
| (e) standing, façade toward a viewer | `img/chamber-standing-from-behind.jpg` | Drawn: this is the friend's view. The façade is lit from behind in the render, so it reads darker than it would outdoors. |

## Findings for systems (from drawing it)
1. **Push-out holes:** v1.1's two (x 110 / 176, d 54) land on pipes. Proposal: move them to d 90, above the shorter pipes. Not drawn yet.
2. **The v1.1 lid model is open on its hinge side**, so from behind, closed, you can see the lid's knobs through the slot (visible in `chamber-closed-with-book.jpg`). If the real FOLD is like that, the "case" reads less closed. Systems: is there a spine wall, or is the slot real?
3. PARA legend: moved and shortened (above).
4. "free" / "sync" sit on the top ticks of OSC 2 and NOISE / EXT. Fixed by dropping those two ticks (set-wide). The checker should count tick rings.

## Can't verify here
- Kalam isn't installable in this environment. Renders use a handwriting stand-in that runs wider than Kalam, so some legends crowd that won't with Kalam. Re-render with Kalam before the owner sees final art.
- Engraved / relief fill on wood-fill PETG.
- Walnut button plugs (supply).
- The façade's brass tone in daylight.
