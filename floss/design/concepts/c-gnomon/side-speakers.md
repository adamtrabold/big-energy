# GNOMON: speakers in the end faces? (systems, assessing an owner idea)

2026-11-22. Owner, verbatim: **"And w what if the speakers were on each side left and right so up or down didn’t matter"**. It's an idea, not a decision (CLAUDE.md item 5), so this assesses it against the current design: speaker E, two TEBM28 drivers (Ø 55 × 24 deep) under lancet grilles in the plate, one ported box of ≈ 190 cm³ [eng r3]. [calc] = my arithmetic; UNVERIFIED = needs eng or a datasheet read.

## 1. What problem it solves
- **"Up or down didn't matter":** the plate drivers already face the player in both poses, because the plate is the face that's turned to you. Angled, they fire up and toward you. Upright, they fire at you, ≈ 18° up.
- Side drivers would be indifferent to the pose too, but by firing *across* the player, not at them.
- **So this may answer a problem he sees that I don't.** Ask him (below).

## 2. Do drivers fit in the end faces? [calc, against rev 5's rounded faces]
| Driver | Size (published listing) | Fits? |
|---|---|---|
| TEBM28 (current) | Ø 55 × 24 [eng] | **No.** Even at the back of the end face, where it's tallest (≈ 66, ≈ 60 flat), the face has dropped to ≈ 50 flat by the centre line of a 55 circle |
| 40 mm class, e.g. PUI's 40 mm 3 W miniature speaker | **40 × 40 × 18.3 mm** ([RS listing](https://uk.rs-online.com/web/p/miniature-speakers/0276821P?gb=s)); the AS04004PR-R lists 100 Hz–20 kHz, 4 Ω, 86 dBA ([element14](https://au.element14.com/pui-audio/as04004pr-r/speaker-100hz-20khz-4ohm-86dba/dp/4412328), [datasheet](https://www.mouser.com/datasheet/2/334/AS04004PR-R-270443.pdf)) | **Only in the tall rear part of each end face**, straddling the slab and the cheek. The 10 mm cheek becomes a box wall, with ≈ 18 mm of driver plus air behind it |
| ≤ 28 mm, or rectangular "phone" drivers | — (not looked up) | they fit the slab band (≈ 29 flat high), but they're far too small for this job; not worth pursuing |

## 3. What it displaces
- **Speaker port:** gone. Two small boxes would be sealed; the end faces have no room for a port.
- **Jacks:** they live on the right end face and must move.
  - **Best new home: the slab's underside near the back, "under the eave".** Angled, it faces down into the hollow, ≈ 30–60 up, and cables run out the open back. Upright, it faces back and up.
  - That's reachable in both poses, and no foot is used. UNVERIFIED: plugging by feel.
- **Cells:** they sit at the ends under the jambs (E). They move into the rear region that E's box frees.
- **Host port:** on the front face, unaffected.
- **Growth rings and the port mouth:** CATHEDRAL's end-grain cue on the end faces gives way to grilles (lancets on the ends).

## 4. Box volume
- Each driver gets its own sealed end box. A ≈ 60–90 cm³ box fits the end bay plus the cheek [calc, rough].
- **Against E (2 × Ø 55, 190 cm³ ported, f3 ≈ 152 Hz [eng]):** a 40 mm cone has ≈ (40/55)² ≈ 0.53 of the area. At equal excursion that's **≈ −5.5 dB** [calc], with less low end in a sealed box. **UNVERIFIED** until eng models it from a full datasheet (Fs, Qts, Vas, Xmax not read).
- The fixed breath and string pads live in the low-mid range, which is where this loses most.

## 5. Sound at the player, in both poses
- **The plate drivers face the player in both poses.** The angled pose is within a few tens of degrees of on-axis, and upright is close to on-axis.
- **Side drivers put the player ≈ 90° off-axis in both poses.** A 40 mm cone starts to beam above ≈ c / (π · d) ≈ 3 kHz [calc, d ≈ 35 mm effective]. Above that, its 90° response falls (by how much is UNVERIFIED for this part).
- So the **shimmer and air of a string machine (≈ 3–10 kHz) get duller at the player.**
- **The gains:**
  - an even spread to people around it (a circle in the park);
  - a little width, with 280 mm between the drivers;
  - nothing on the plate for a hand to cover.

## 6. What it frees on the plate
- The two grille fields (≈ 2 × Ø 46, ≈ 3,300 mm² [calc]). The plate becomes controls only.
- With E's box gone from the rear region, **D could shrink** toward what two rows and the board need (≈ 75–85, UNVERIFIED). By tan θ = T / D the angle then steepens (≈ 23–25°).
- The width grows a little for the end boxes.

## 7. Verdict
**Not recommended as a replacement for the plate drivers.**
- It's quieter (≈ −5.5 dB) and thinner in the lows.
- It's duller at the player, because the player is off-axis in both poses.
- It loses the port, the jacks' home and the end-grain cue.
- And it solves "up or down", which the plate drivers already solve, since they face you in both poses.

**Its real gains:** a controls-only plate, a possibly smaller module, and sound for a circle of listeners. Those are worth naming to him.

**Best version, if he wants it anyway:**
- one 40 mm-class driver per end, high at the back of each end face, behind a lancet grille, each in its own sealed ≈ 60–90 cm³ end box;
- cells into the freed rear region;
- jacks under the eave;
- the plate controls-only, with D shrinking (and θ following tan θ = T / D);
- eng models it from full datasheets before it's drawn.

## 8. Question for the owner
What's the "up or down" problem you're picturing? The plate speakers already face you in both poses. If it's sound for people around you, or a clean plate, side speakers do that, at the cost above.
