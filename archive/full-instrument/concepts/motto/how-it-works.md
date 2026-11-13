# MOTTO: how it works (systems), round-2 fix pass

> **Fix pass:** M1 (speaker over the VCOs, decided: option a), M2 (≤ 190 deep), M3, M4, F1–F5, the E2 lid-switch spacing, and 12 pips (common §2 mod correction).

**Kind:** sauce (the lead, per R4). **Idea:** a tiny bentside harpsichord.
The lid hinges at the tail and **stands up behind the panel**, painted inside,
facing the player like an altarpiece. It reflects the speaker's sound toward
the player. The keys are reverse-colour tongue keys.

Read `../common-how-it-works.md` first.

**Checked against:**
- **owner.md:**
  - "hand paint it… based on outcome" (Q5);
  - "portable… small";
  - "dont over index on OP1… feel good to use";
  - MIDI-control entry;
  - "explore the light thing";
  - "as silent as possible".
- **eng v2:** §4.1, §4.2, §2 (12 ownable controls incl. the mod fader, E1); answers-E1-E10 E2, E5, E8.
- **scores.md:** R1, R4, R7, R8.

**Round-1 change accepted:** I take the visual designer's layout over my
predecessor's mirror: spine on the left, tail at the back-left, the lid
hinged at the tail and standing behind. The reasons are the visual's and
they hold. The painting and the reflector both face the player, and the lid
is never over either hand. The mirror proposal is withdrawn.

## What R1 does to MOTTO, and the fix

- **The problem:** the round-1 MOTTO was 193 deep with a 70 mm panel and a
  separate tail. With R1's ≈ 100 mm panel, a separate tail would be
  5 + 70 + 100 + 50 ≈ 225 deep. That's over the box, and R1 says MOTTO
  mustn't grow.
- **Fix: the panel *is* the bentside.** The panel's depth varies along the
  curve instead of sitting on a rectangle with a tail behind it.

| Position | Panel depth | Holds | Body depth |
|---|---|---|---|
| **Spine (left)** | **≈ 110** (M2: taken from the spine) | the play group plus the rose speaker at the rear-left | 5 + 70 keys + 110 + 5 = **190** |
| **Right end** | **≈ 85** | the contour faders (36 deep) plus a toggle row (23) still fit | 5 + 70 + 85 + 5 = **165** |

- **The panel averages ≈ 100 deep**, so it meets R1, and the area is
  ≈ 280 × 100 ✓.
- **A 25 mm S-curve across the rear** still reads as a harpsichord (M2).
  The bentside ratio survives.
- **The speaker moves into the panel zone** at the rear-left, under the
  rose, in the common A/B notch (common §5, E2). There's no tail box. **The
  rose is the tail.**

## Structure

| Part | Holds | Size (mm) |
|---|---|---|
| **Body** | Left zone (22 mm): bend stick + mod fader. Front: key zone (**K-B lever tops in walnut, reverse colours, on Choc V2 silent + magnet + TO-92**; strip C; D + battery under the keys). Behind: a bentside panel zone with A/B shaped to the curve (an Edge.Cuts arc on the rear edge of each A/B board). The speaker notch sits at the rear-left under the rose. I/O on the straight rear section and the spine (see below). | **292 wide × 190 (spine) → 165 (right) × 34** |
| **Lid** | The full outline. 3 mm walnut ply outside (R4: walnut only on the lid's outside), with a 12 mm laser frame giving the cap pocket and a 1 mm felt lining. The inner face is a smooth sanded panel for painting. | outline × 12 |
| **Hinge** | Brass piano hinge, ≈ 110 mm, on the **straight rear section at the spine end** (the bentside is curved from x ≈ 115 to 292, so the hinge can only run along the first ≈ 115 mm) | — |
| **Stay** | A **captive folding brass stay** at the lid's right half, pivoting on the body's rear-right. Detent at **100°**, folds into a slot in the lid | — |

- **Why one hinge at the left plus a stay at the right:** a 110 mm hinge
  alone would let a 292 mm-wide lid rack (twist). The stay at the far end
  takes that load: two points, one each side.
- **Tipping check:**
  - The lid (≈ 0.25 kg) leaning 10° past vertical puts its centre of
    gravity ≈ 16 mm behind the rear edge.
  - The body (≈ 1.2 kg) has its centre of gravity ≈ 95 mm in front.
  - **Stable** ✓ (estimate).

### I/O edge
- **The problem:** the straight rear section is only ≈ 115 mm, and the
  hinge sits on it. The jacks need ≈ 260 mm.
- **Fix:** the jacks follow board A's curved back edge, along the
  bentside, as a gently curving row. Board-mounted jacks only need their
  fronts on the edge, and an arc of R ≈ 400 mm is fine at a 14 mm pitch.
  USB-C and the master switch go on the **spine (left) face**.
- **Check with the visual designer:** cables leaving a curve fan out
  slightly. I think that's charming, not a problem.

## Geometry
- **Open:**
  - Lift the lid's front edge and swing it up past vertical. The stay clicks
    at 100°.
  - The painted face (≈ 292 × 190) faces the player, ≈ 34 mm above the
    table at its bottom edge.
  - The rose fires upward right in front of the lid.
  - **The reflector claim is UNVERIFIED** (R4.3). A 40 mm driver firing at a
    board ≈ 40 mm behind it should throw upper-mids toward the player, but
    that's a claim until someone listens. The mock must say "unverified".
- **Closed:**
  - The lid lies on the body. Its frame clears the caps (panel sunk 4 mm,
    caps 8 mm above the rim).
  - **The lid magnet and the DRV5023 sit at the right end's rear rim** (moved
    from the spine: E2 needs ≥ 50 mm from the rose's magnet; it's now
    ≈ 250 mm away, and ≈ 130 mm from the key sensors) ✓.
  - **Carry: 292 × 190 × 46,** an irregular, recognisable outline. The stay
    is folded inside the lid's slot.

## Panel (bentside, from left to right)

| Zone | Panel depth | Contents |
|---|---|---|
| **Play** (spine, right of the stick and fader) | 110 | CUTOFF hero front-left; EMPHASIS, CONTOUR AMT, GLIDE + glide on in an arc around it; HOLD. **Rose grille Ø 50 at the rear-left.** |
| **Controllers + oscillators** | ≈ 110–100 | TUNE, MOD MIX, 3 toggles; RANGE × 3, WAVE × 3, FREQ 2/3 |
| **Mixer** | ≈ 100–92 | levels × 5, plus 8 toggles in front |
| **Contours + out** | ≈ 92–85 | 6 faders, KBD 1/2, DECAY; VOL, PHONES, TUNE button, status LED |

- **V-c, 12 pips (R4.4, R7, plus the mod correction):** a 3 mm amber LED
  beside each of GLIDE, TUNE, FREQ 2, FREQ 3, CUTOFF, the 6 contour faders
  **and the mod fader**, always on the same side
  (upper-right of the cap, or at the top of the fader slot).
  - A pip says "**this** knob isn't in control: move it to take it back".
  - Driven by 2 × 74HC595 on board A (16 outputs, 12 used).
  - Gold rings on the same 12. None on RANGE or the stick (F4).
  - **Finger dials: cut (R4.5).** The rose carries the telephone.

## Placement against the rules

| Rule | Check |
|---|---|
| **Speaker ↔ sensors** | The rose centre is ≈ 160 mm from the front, the sensor line ≈ 30: **≈ 130 mm** ✓ |
| **Speaker over the left B board: decided, option (a) (M1)** | The rose stays top-left, where a harpsichord's is. **The VCO cores go on the right B board**, well over E8's ≥ 30 mm from the speaker frame. Also per E8: the PAM8302 at the speaker (≤ 50 mm leads, twisted), a foam-gasketed chamber isolated from B, a ground pour under the VCOs, and no speaker lead over the VCO area. **The mock notes: "eng places the VCO cores on the right board (E8)".** |
| **Lid magnet + DRV5023, stay** | Right-end rear rim, both outside the key run, ≥ 50 mm from the rose ✓ |

## Flows (deltas)

| Flow | Steps |
|---|---|
| **F1** | Lift the lid to 100° (stay clicks). The LED breathes from ≈ 20° open, the unit tunes, and you play. |
| **F4** | Lift slightly to release the stay detent. The stay folds into the lid as it comes down. The magnet seats it, and the unit sleeps. |
| **Lid off for painting** | Remove the 6 hinge screws and unhook the stay. The lid comes away whole. The owner paints it flat on a bench. **(New, inferred: "hand paint it" needs the lid off.)** |

## States

| State | What happens |
|---|---|
| lid up at 100° | awake, and the stay is locked |
| lid part-open, stay not engaged | awake. The lid's weight takes it closed unless held: the stay has no intermediate detent, deliberately, so it can't sit half-propped and fall on a hand |
| lid closed | asleep |
| lid removed (painting) | the Hall sensor sees no magnet, so the unit is awake. Playable with no lid |

## Build and cost (R8)

| Item | Detail |
|---|---|
| **Laser** | ≈ 10 curved body layers, the lid frame plus the walnut skin, the rose grille (laser-cut petals) |
| **FDM** | none (owner: real parts). Caps, stick and fader are bought |
| **Keys** | K-B tops in walnut ply, **owner-cut at Vector Space** (F5), on Choc V2 silent + magnet + TO-92 |
| **Bought** | brass piano hinge, brass stay, 12 LEDs, 2 × 74HC595, 25 Choc V2 silent + magnets, stick, slide pot, knobs |
| **Steps after soldering** | **15** |
| **Cost vs SLAB** | **+$35–60**: hinge $8–12, stay $5–10, walnut ply for the lid $15–25, pips $3, walnut key-top ply ≈ $5 |
| **Full instrument, one unit (F1)** | **≈ $565–920** |

## Risks / open
1. **The reflector is unverified** (R4.3). The cheap test, kept exactly
   (M4): a cardboard lid behind the first speaker prototype.
5. **Chartreuse hero (M3):** kept as shown. Swapping it means changing one cap.
2. **The curved jack row (visual check).**
3. **Speaker near the VCOs: decided** (M1 option a, E8 conditions).
4. **Panel depth at the right end (85).** The contours fit at the R1
   minimums, but with no slack. The visual designer should draw it.
