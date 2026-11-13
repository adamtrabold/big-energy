# DISH: how it looks and feels (visual), round 2

Read `../common-looks-and-feels.md` first. Mock: `dish-mock.png`; how it goes
together: `dish-exploded.png`.

**Checked against:** owner.md (all entries; Critter and Guitari reference;
"real parts"; "i want velocity"; MIDI entries; silence); eng v2 §2 (dish = the
"Yes" rows only), §4.1, §4.2; scores.md R1, R5–R8; `dish/how-it-works.md`
(Ø112, 38 base, the split).

## The idea, as it should read

A radio telescope on a desk. The round dish rises out of its well and tilts
toward the player: it is everything the MCU reads (cutoff at the centre; glide,
tune, freq, range and both contours around the rim). The wings are the analog
tone you set and leave. When MIDI owns any dish control, the ring of light
around cutoff glows.

## Visual's geometry change (for systems to confirm)

At the round-1/systems geometry (fork pivot at the well's front edge, fork
vertical, dish at 50°), the dish's lower rim hangs **36 mm forward at 7 mm
above the base**, right over the sharps. The side view draws this in red.

- **Fix:** the fork pivots at the well's **rear** edge and leans **70°**
  toward the player (arms 58 mm). The dish centre sits ≈ 54 mm up, its lower
  rim ≈ 12 mm above the well, its top 12 mm behind the base. Reach from the
  keys to cutoff ≈ 150 mm, like a far panel row.
- **Speaker:** moves to the **well centre** (Ø40, ≤ 12 mm deep): ≥ 60 mm from
  the sharps' switch row. The dish lifts off it; its lower rim hangs over the
  grille's rear half like the lip of a horn.

## Looks

- **Proof look:** walnut base, cream wings and dish face, black caps, red hero.
- **Dish face (Ø112):** gold rim line; 13 ring controls at r 38 (chord
  18.3 mm); legends around the rim at 3.4 mm, flipped on the lower half so all
  read upright; the bullseye light ring at r 16.6 around the 26 mm hero. Range
  switches have ticks, numerals on the rim (owner letters them). Ownable knobs
  carry the gold ring like the panel.
- **Wings:** sunk 8 mm, low caps; left "set the tone" (mod mix, osc/filt mod,
  osc 3 ctl, glide on, decay, emphasis and amount as 16 mm caps nearest the
  hand, HOLD, TUNE, LED, kbd 1/2); right "waveforms · mixer · out".
- **Keys:** K-E maple button plugs, two rows, felt collars; a dot below each C.
- **Brass:** fork arms and the axle tube.

## Feel and motion, by state

| State | What you see / feel |
|---|---|
| stowed | dish face-down in the well, fork in its channels; flat 38 mm, no lid |
| raising | lift the rim: the fork swings to its 70° detent, the dish turns on the axle to 50° (detent) or 75° |
| playing | bullseye dark when every dish control is owned by its knob |
| MIDI owns a dish control | the amber ring around cutoff glows (V-d) |
| pressing a rim knob | detents hold 15 N; a harder push steps to the next detent, never crushes |
| dish link lost | dish controls hold; status LED shows "dish lost" |
| lights off | dish pointers + lit bullseye float above the dark base (inset) |

## Why

- R5's rule makes V-d exact; the owner's latest MIDI rule (MIDI can't flip
  switches) means the range switches on the dish are MCU-read but never owned,
  so the bullseye covers the 10 ring knobs + cutoff.
- Button plugs are a real woodworking part: the Critter and Guitari warmth
  with no service-cut parts at all.

## Open

- Systems: confirm the rear pivot and the speaker move; board area under the
  wings (E7) gets slightly easier (B extension now in front of and behind the
  speaker).
- Cable life through two pivots.
