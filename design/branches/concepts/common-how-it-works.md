# Branches: shared "how it works" (systems, concept turn 1, 2026-11-13)

> **Rev 2 (2026-11-13, round 1 rulings + render check).**
> - Accepted by the director: the left / right throw, ±135° plus the clamp, and PARA's wording "mono / para / +4".
> - New from measuring the real render models in Kalam (`branch_check.py` §7):
>   - "free" / "sync" sit **0.5 behind** the toggle centre (1.92 / 1.88 to the knobs; was 1.42 / 1.38);
>   - OSC 2's **+50°** and NOISE/EXT's **−50°** ticks are dropped as well as their top ticks (0.29 / 0.05 to the toggle nut otherwise).
> - The checker now counts legend-vs-legend, legend-vs-tick, legend-vs-control and tick-vs-control on what `rb.py` actually draws, and marks clashes inherited from locked v1.1.

Read with `design/jobs.md` rev 5 (J20–J28, F13–F15), `design/branches/echo-clock.md` (owner: option "B") and the v1.1 locks in `versions/v1.1/` (never edited). Each branch folder has its own `how-it-works.md`; the visual designer adds how each looks.

Checker: `design/branches/concepts/branch_check.py` (imports the v1.1 `fold_r5_check.py`, read-only). **TOTAL fails 0.** It reports one expected finding: DIPTYCH as briefed tips over with cords alone (see `diptych/`). The v1.1 checkers still pass (`fold_r5_check.py` 0, `flat_r5_check.py` 0).

Marks: **[CALC]** my arithmetic · **[CHECK]** from the checker · **ESTIMATE** · **UNVERIFIED**.

## 1. The rule every branch keeps (J28)
**The board is the constant; the outside is the branch.** No branch moves a control, a board, the Daisy or the mux plan. A branch may change the enclosure, the key tops (bought parts), the underside, feet, graphics and finish. **One exception, shared by all four: the new FREE / SYNC toggle** (owner decision "B"), which adds one toggle and one mux channel (46 / 48) to every concept.

## 2. FREE / SYNC: placement, checked with labels [CHECK]
The visual designer's spot (in front of TIME, in the pot's dead zone) is the only legal one; nothing else fits by the margins. The label check found three things the sketch didn't show. All three are fixed below.

| | ONE SHEET frame (BUTTERFLY, RAIN) | FOLD-105 lid (CHAMBER, DIPTYCH) |
|---|---|---|
| Toggle centre | **x 128.0, y 132.7** | **x 133.0, d 70.6** (open y 178.6) |
| Legal window (control rules alone) | y 132.14–133.22 at x 128 [CALC] | d 69.99–71.07 at x 133 [CALC] |
| Nearest controls (edge gap, rule ≥ 1.5) | NOISE/EXT 1.88 · OSC 2 1.88 · TIME 1.99 | NOISE/EXT 1.92 · OSC 2 1.92 · TIME 1.94 |
| Closed landing | n/a | base y 37.4, over the sharps; z clearance 2.0 (v1.1 rule, toggle counted at knob height). With pegs: see CHAMBER |

**Fix 1: TIME's legend was in the way.** In the v1.1 render code every knob legend sits *in front of* its knob (`r4.item`: y − r − gap − 0.6). TIME's legend is exactly where the toggle goes (the visual note said nothing of TIME's was printed there). **TIME's legend moves behind its knob**, beyond its scales (ONE SHEET y ≈ 159.2; FOLD d ≈ 96.9). **DECAY's legend moves behind too**, to keep the back-row pair mirrored. Gap to the outer scale ring: 1.44 / 1.35 (rule ≥ 1.0).

**Fix 2: the throw is left / right, not fore / aft.** With a fore-aft throw, the words have to go in front of and behind the toggle. Behind is TIME's knob (no room); in front is a 5.1 mm slot between OSC 2 and NOISE/EXT (0.55 per side for "free"). Beside the toggle, like PARA and AFTERTOUCH, both words fit: **"free" to the left, "sync" to the right**, 6.2 from centre, at 0.72 × the legend size. Tightest label gap 1.59 (rule 1.5). *This changes the visual designer's "the lever points at the scale" idea. The replacement reading: the lever points at the word.*

**Fix 3 (ONE SHEET style only): the MIXER heading moves** from y 133.6 to **y 136.0**, the OSCILLATORS / CONTOURS line. At 133.6 it collides with "sync". At 136.0 it clears "sync" by 1.7 and the FX-row groove (starts y 138.5) by 1.6. RAIN may have no headings at all (see `rain/`).

**TIME's two scales (J25):**
- Inner ring = ms (≈ 20 ms … 2 s), ticks at r + 0.9 … r + 1.9 (v1.1 radius).
- Outer ring = 9 divisions, marks at r + 2.4 … r + 3.6 (PROPOSAL).
- **Printed over ±135° (270°), not the pot's ±150°.** At ±150° the end ticks land under the toggle nut (−0.7 mm). At ±135° they clear by 1.8. **Firmware clamps the last 15° at each end** (min below −135°, max above +135°), so the scale always tells the truth. $0.
- Number labels round the ring ("20 ms", "2 s", "1/16"…"1/2"): the visual designer's job. Free space is tight; ECHO TYPE's fan names sit 5–6 mm to the left.

**Behaviour:** as `echo-clock.md` option B, with one rider added here: the 270° printed sweep and the clamp.

## 3. Set-wide parts from the killed branches (director's rulings)
- **Status light hood (sun, J22c), every branch:** the 5 mm LED sits 3–4 mm down a printed tube (a recess, so nothing is raised), with a light pipe if needed. ONE SHEET style: status at (257, 81); FOLD base: (155, 81). Whether it reads in midday sun is **UNVERIFIED** until the park test. H7 stands (one light, no lit TAP).
- **High-contrast legends** at low sun angles: visual's call per branch.
- **Felt finger pocket** where an outline already has room. None of the four needs one: FOLD carries as a bar, ONE SHEET in a bag.

## 4. Things no branch has solved yet (J22, the park)
- **Battery for an afternoon (J22e):** FOLD-105's slim ≈ 11 Wh pack gives ≈ 1.9–3.9 h [CALC from `daisy-first-principles.md` §7.1]. The owner question "how long is a park afternoon?" is still open. ONE SHEET's pack: as v1.1 (capacity not restated here; UNVERIFIED).
- **Speaker outdoors (J22d):** ONE SHEET fires down through its back panel (into grass = absorbed); FOLD's lid speaker faces the player. No branch changes the speaker; outdoor loudness is **UNVERIFIED**.
- **Heat (J22f):** PLA softens at ≈ 55–60 °C (glass transition, ESTIMATE). Branches print in **PETG** (ONE SHEET style already is), FOLD branches in PETG / wood-fill PETG. Eng to confirm the LiPo's temperature in sun.
- **Power-off sound** (RAIN's "makes a sound when you close it" draw): **not possible with the hard power switch**. The Daisy loses power the instant it's switched off (`daisy-first-principles.md` §7.2: no soft latch). A "drop" at power-**on** (when status reaches ready) is free.
