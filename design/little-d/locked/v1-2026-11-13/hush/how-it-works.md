# HUSH: how it works (systems)

Kind: **a material**. Pole: sauce. **Rev 6, 2026-11-12 (concept round 4).** Printed shell + wool felt only (the ply tray is retired). Read with `../common-how-it-works.md` (**rev 6**) and `../../jobs.md`.

> **Rev 7.4: PARA legend fits by mirroring AFTERTOUCH's** (labels can't stack 3 deep there).
> - **Name:** "PARA", **left-aligned 5.6 mm to the RIGHT of the toggle**, in the strip between OSC 1 and OSC 2. It mirrors AFTERTOUCH's label, which sits right-aligned to the left of its own toggle.
> - **Positions:** shortened to **1 · P · 4** (MONO / PARA / PARA+4). These are the only words that change.
> - **ONE SHEET:** that strip is ≥ 8 mm tall across x 114–123 [CALC], so it takes two lines of 1.37 caps: "PARA" over "1 · P · 4".
> - **HUSH:** the tags narrow it to 4.3–5 mm, so there's room for one line only. "1 / P / 4" is pressed as three 1.2 mm glyphs stacked at the toggle's three throw heights (y 109 / 111.5 / 114), right beside it, and "PARA" follows at x ≈ 119.5–124.5 on y 111.5.

> **Rev 7.3 (pre-build, 2026-11-13): switch pair.**
> - **AFTERTOUCH confirmed where the visual designer placed it:** VELOCITY's column, y 111.5, between the VOICE rows (FILTER MOD / AFTERTOUCH / VELOCITY). The two key-response switches stack.
> - **Its empty mirror slot is now filled by the new PARA toggle (3-way MONO / PARA / PARA+4)** at the oscillator-side switch column, y 111.5 (OSC MOD / PARA / OSC 3 CTL). ONE SHEET x 104.25, HUSH x 111.25; AFTERTOUCH ONE SHEET 171.75, HUSH 178.75.
> - **Why:** PARA decides how the keys are assigned to the oscillators, so it sits with the oscillator switches. AFTERTOUCH is how the keys respond, so it sits with VELOCITY. They mirror about the centre.
> - Checkers 0 violations, mirror 0.00.
> - **Legend check (visual):** PARA's three position words need the same treatment as AFTERTOUCH's label (right-aligned, left of the toggle). OSC MOD and OSC 3 CTL labels go above their toggles, mirroring VELOCITY and SOURCE.

> **Rev 7.2 / DRIFT (2026-11-13). Supersedes 7.1's PLAY-right and back-row text.** Owner: "I like the idea of drift, but I'd want it to be controllable". DRIFT is a firmware random pitch wander; fully left = rock-steady.
> - **Back row = the chain in one line**, mirrored about the centre:
>   - **DRIFT 81.5** (source, under the FREQ column)
>   - ECHO TYPE 110.5 · ECHO TIME 130.5
>   - REVERB DECAY 159.5 · REVERB TYPE 179.5
>   - **VOLUME 208.5** (out, under the loudness column)
>   - Breaks at 96 / 145 / 194.
> - **PLAY right:** ECHO REPEATS 201 · ECHO MIX 221 · REVERB MIX 241 · **TAP 263**. TAP is played in rhythm, and it mirrors the bend stick.
> - **Why:** one added knob makes the count odd, so a lone DRIFT can't be mirrored. **DRIFT ↔ VOLUME** pairs source with output; TAP moves to the PLAY row to keep that row at 4 + 3 + 4. The checkers pass with 0 violations and mirror 0.00 in every row.
> - **Cost:** VOLUME sits on the back row (≈ 78 mm behind the PLAY row), and TAP is away from TIME. Sizes are unchanged.

> **Rev 7.1 (round 5 final):**
> - **Layout:** common rev 7.1 + 7.
>   - PLAY right: REPEATS 201, ECHO MIX 221, REVERB MIX 241, **VOLUME 263**.
>   - FX row y 146: ECHO TYPE 97.5, TIME 117.5 | TAP 145 | DECAY 172.5, REVERB TYPE 192.5. Breaks 132 / 158.
> - **Body 290 × 186.** The FX row clears the rear R 44 corners (all FX x between 44 and 246). The bay moves back with the board.
> - No side-wall wheel. Tags on every control.
> - Key edge A/B as rev 7.

> **Rev 7 (round 5, 2026-11-13). Supersedes the layout and front edge below.**
> - **Layout and FX:** common rev 7 in the HUSH frame (x = FOLD x + 2, centre 145, breaks 103.5 / 186.5).
>   - PLAY: stick 27, MOD 49, TUNE 69, GLIDE 89 | CUTOFF 121, EMPHASIS 145, CONTOUR AMT 169 | ECHO TIME 201, REPEATS 221, REVERB 241, FX MIX 263.
>   - The VOICE uses the common rev 7 columns + 7.
>   - **Tags:** every face control has one, including the 4 FX knobs.
>   - **VOLUME:** a thumbwheel punched through the felt in the right wall; the felt is bound round the slot.
>   - **FX MODE toggle:** rear wall with the jacks.
>   - **Body:** ≈ 290 × 184 (ESTIMATE). The rear R 44 corners and the bay move back with the board.
>   - Checked: every knob on the flat top (≥ 12 from the edges), 0 violations (`_mock-src/flat_r5_check.py`).
> - **Key edge, two options.** Peg heads stand **6.5 above the felt by mechanism**: 2.5 travel to the collar plus a ≈ 4 mm head. "2–3 proud" isn't possible with pegs; they're already well proud, so they can be felt.
>   - **A, at the edge, no lip:**
>     - The **front edge round-over tightens from r 12 to r 4** (sides and back keep r 12; the front corners blend r 4 → 12, so **add this to the corner blocking test**).
>     - The pegs move forward 6: whites at **y 13.5** (head front 7.15 from the front face; collar edge exactly on the flat at 4), sharps at y 36. Arms and strip C move forward 6 too (strip C y ≈ 2–50).
>     - The PLAY row stays at 68.
>     - In front of the heads there's only 7 mm of felt falling over a tight edge.
>   - **B, small lip:** the round-4 geometry. The r 12 felt brow is the lip: flush at 25.5 and 13 mm deep. Peg heads at y 19.5 (13.15 from the front), 6.5 above it.

> **Rev 6.2: internal battery bay (owner: "What do you mean there's no battery … we are designing this").**
> - **Bay:** x 27–157 × y 106–172, z 1.5–12.9 (**130 × 66 × 11.4 clear**). It sits under the main board at the rear-left, under the VOICE oscillators and the rear band, clear of the speaker.
> - **Holds:** 2 pouch cells of ≤ 9.9 thick × 50 × 60 (e.g. 2 × 3000 mAh ≈ 22 Wh, ≈ 5–10 h at eng's 2.2–4.2 W; cell choice and wiring with eng).
> - **The height:** 1.5 mm comes from a pocket in the back panel; the board's underside has a lead-free keep-out over the bay.
> - **Why not under the keys:** under strip C there's only ≈ 6.5 mm.
> - **Access:** the cells strap to the back panel's inner face on JST leads. Back panel off (8 screws underneath) → unplug → swap.

> **Rev 6.1 (eng round 4):**
> - **290 × 176** (was 144). The main board ≈ 268 × 115 runs y ≈ 58–173, so the body grows behind the back row. Keys, pegs and rows are unchanged.
> - The felt rear band (y ≈ 132–164 flat) is plain felt; the name can be embroidered there.
> - Rear plan corners stay R 44.
> - Knobs: 18T push-on on T18 pots, tops ≈ 39.
> - Eng confirms strip C (y 8–56) and the main board (from y 58) side by side ✓.
> - Felt flat-equivalent grows to ≈ 392 × 278 (hood size UNVERIFIED).
> - Print split at x 129.5 → 129.5 × 176 and 160.5 × 176, both ✓ on a 250 × 210 bed.

**What changed in rev 6 (owner):**
- "Hush should be more rounded around the edges, organically, so the felt can wrap seamlessly around it": a pebble-like shell; the felt now covers **top, edges and sides** and ends only underneath.
- Unibody, "controls installed from behind and then a panel screwed in on the back": closed-top shell loaded from underneath; every fastener underneath.
- Keys to the front edge, logical split, narrower: **298 × 180 → 290 × 144** (common rev 6 layout, +7 in x).
- No sleeve, flap or case this round.

## The idea
The owner's hardest feel rule is "as silent as possible", and silence is made of felt. **The material that makes it quiet is the material of the whole outside: one seamless skin of grey wool felt wrapped over a soft printed body, with maple pegs for keys rising through it.**

## Design principles (each follows from the idea)
1. **The skin is a working part.** Each peg head lands on a felt collar just before the switch bottoms: felt is the silent bottom stop. *Because* if felt makes it quiet, the felt you see must be working.
2. **One skin, no edges.** The felt runs over the top, round every edge and down every side, and ends only underneath. The body is rounded so it can. *Because* a soft object has no corners to knock and no seams to pick at (owner, rev 6).
3. **Nothing hard touches the hand except what plays.** Pegs, knobs, stick: hard. Everything else: felt.
4. **Nothing shouts / one hard material: a tag per knob** (visual r3). Grey wool, maple, cream knobs; a printed tag under every knob carries its scale, because felt can't hold a fine mark.
5. **Wear parts are separate.** Collars are punched rings, replaceable; the skin itself comes off and goes back on.

## Keys: maple pegs on Choc V2 silent
- **Pegs:** 1/2 in (12.7 mm) maple mushroom button plugs. **Each peg is centred over its switch stem** (eng E-L5: "mechanically best, no rocking"); a laser-cut acrylic arm carries the MX cross pocket under the peg and the D31 magnet **10.5 mm behind the stem**.
- **Whites:** pegs at **y 19.5**, x 19 + 18n (n = 0…14: x 19 … 271). Arm y ≈ 12–33 (stem 19.5, magnet 30).
- **Sharps:** pegs at **y 42**, at the white boundaries in piano positions. Arm y ≈ 34.5–56 (stem 42, magnet 52.5). White arm ends (33) and sharp housings (34.5) clear by 1.5 mm.
- **Strip C:** y ≈ 8–56, x 10–280. The main board starts at y ≈ 58 (PLAY pot bodies at 68 ± 5) ✓.
- **Velocity and the felt stop:** unchanged from rev 5 (eng E-L5 §3.3: contact at 2.5 ± 0.2 of 2.8 mm comes after the fit window in every tolerance case). **Holes clear the moving shank ≥ 0.5 mm radial; the head overlaps the hole** (no drag).
- **Collars:** punched 19 mm rings of 3 mm F3 felt, each in a 1 mm counterbore in the shell, so the collar top is flush with the 2 mm skin (25.5). The peg head's underside is 2.5 above the collar at rest (28); head top ≈ 32.
- **Fitting:** pegs press into their arms **from above, last** (like the key tops in common §5). A peg pulls out by hand.

## Body

| Item | Spec |
|---|---|
| **Outer** | **290 × 176** (rev 6.1); felt surface (deck = panel) at **25.5** |
| Plan corners | front **R 20**, rear **R 44** (organic: the back rounds off more than the playing edge). Front corners are limited by the end pegs: C (19, 19.5) must sit on the flat [CALC: 7.45 from the corner centre, flat radius 8] |
| **Edge section** | top round-over **r 12** all round → a short near-vertical side (≈ 7.5) → bottom round-under **r 6** → flat bottom. The felt follows all of it |
| Flat top | from 12 in at every edge: every peg, knob and tag sits on the flat (checked: front peg heads at y 13.15, last knob edge y 130.45 vs 132, side margins ≥ 12.65) |
| **Shell** | printed, closed top (2.5 thick, top surface 23.5), walls 2.4; ribs at y 85.4 and 111.5 |
| Layout | common rev 6 + 7 in x (PLAY row y 68; VOICE y 100 / 123). Sections are told apart by the tags and the felt between them (no grooves in felt) |
| Tags | printed ring + name under each knob (visual r3), set into a punched hole in the felt, flush; a sleeve on the tag presses into the shell hole around the bushing and holds it (and pins the felt). MIDI dots on the tags |
| Stick | Delrin gate in a pocket under the shell; a printed tag around the slot; cap on after |
| Lights | status (269, 68), "not in control" (159, 79): through punched holes, each in a small printed bezel tag |
| Jacks, power | I/O board inside the rear wall (common §4); the felt is cut around the 7–8 ports (small round holes, like a laptop sleeve's) |
| Speaker | bottom, centre (247, 113), through a grille in the back panel |
| Battery | on the back panel's inner face, under the main board's keep-out |

**Heights:** felt 25.5; knob tops ≈ 36, CUTOFF ≈ 37.6; peg heads ≈ 32 (R3 ✓). Board top ≈ 14, pot bodies 14–21 under the 21–23.5 shell face.

## The felt: how it wraps seamlessly

**The problem [CALC]:** a flat sheet can't follow a corner that's curved both ways (in plan and in section) without spare material. At a front corner (plan R 20, edge r 12) the sheet has ≈ 25 % too much material at the side's widest point, more as it turns under. A pressed F3 sheet can't take that up; it would pucker or need a cut.

**Default: block it like a hat.** Use a **wool felt hat hood (capeline)** and steam-block it over the printed shell, the way a milliner blocks a hat over a wooden block. **The shell is the hat block.** Wet wool felt stretches and shrinks to a compound curve, then sets dry. Hoods are made to do exactly this (crowns are much deeper curves than these corners).
- Thickness: hat felt is ≈ 1.5–2 mm (UNVERIFIED for a given hood). The shell's top sits at 23.5 for a 2 mm skin; the stop is the separate F3 collars, so skin thickness doesn't touch velocity.
- Size [CALC]: flat-equivalent ≈ 392 × 246 mm (top + both wraps + 15 mm turn-ins); a large capeline should cover it (sizes and price UNVERIFIED; ESTIMATE $15–35).
- Holes: punched from inside after blocking, **using the shell's own holes as the template**.

**Fallback: the F3 sheet** (one 12 × 12 in sheet won't reach any more: 290 + 2 × 51 = 392 > 305; it needs a 12 × 24 in or a roll). It wraps the straight edges cleanly. At each of the four corners the spare material goes into **one dart** cut from the turn-in up to the side's widest point and butted with a hidden stitch. Seen from above and from the front it's seamless; at the corners, a fine line shows on the side.

**Where the felt ends:** **underneath only.** The skin turns under the bottom round (r 6) and ends ≈ 15 mm in, lying in a 2 mm recessed land around the shell's bottom rim. A thin printed **binding ring** (290 × 144 outer, 15 wide) clamps it there with 10 × M3 from underneath. The back panel sits inside the ring with its own screws, so **opening the back never releases the felt**.

**Test before committing (one evening):** print a 100 × 100 corner of the shell (plan R 20, edge r 12). Block (a) a hood offcut and (b) an F3 square over it with steam; photograph both.

## Build and service (common §5, with these differences)
- **F9 order:**
  1. Print the shell (split at x 129.5, the full-depth break line, on Prusa beds; the felt hides the joint).
  2. Block the felt over the empty shell; dry; trim the turn-ins.
  3. Punch the holes from inside.
  4. Fit the collars, then the binding ring.
  5. Load from underneath as common §5 (gate, main board, strip C, I/O, battery and speaker on the back panel).
  6. Back panel on.
  7. Flip it; press in the tags, the pegs and the knobs; fit the stick cap.
- **F10 Service:**
  - Back panel off (8 screws): battery, speaker, BOOTSEL, board underside.
  - Board out: knobs and tags off the top (pull), 10 screws, lower it.
  - A key: pull its peg from above.
  - **Collars:** pull the peg and lift the collar out.
  - **Skin:** pull the knobs, tags and pegs, undo the binding ring, lift the skin off; re-block or replace.

## Wear plan
| Where | What wears | Replacement |
|---|---|---|
| Peg collars | compress where heads land | punched F3 rings, lift out; spares from any F3 offcut |
| Front edge (palm) | grime, pilling | the skin is one piece now (a palm strip would be a seam): brush it, steam it; replace the skin when it's done |
| Around CUTOFF and the stick | finger contact | already on printed tags and Delrin |

## States
| State | Form |
|---|---|
| Play | on its back panel's feet; a soft grey pebble with pegs |
| On a lap | felt all round, warm, silent; speaker muffled (as all) |
| Carry | **not designed this round** (owner deferred); the felt outside makes it the most bag-tolerant of the three |
| Keep it out (J18) | keyhole slot in the back panel |

## Flows that differ from common
- **F1:** out of the bag, on the table or lap, power (rear), play.
- **F4:** separate card.
- **F11 Label:** embroidered names and numerals on the skin before it's blocked? No: embroidery stretches when blocked. **Embroider after blocking**, by hand, or laser-brown the skin on the shell (the shell is flat on top). Scales on the printed tags.

## R4 check
Felt deck = panel 25.5; tags flush in the felt; nothing among the knobs; no separator between pegs and knobs (the PLAY row starts 9.25 mm behind the sharp heads) ✓.

## Cost (ESTIMATE)
Shell ≈ 160 cm³ ≈ 200 g ≈ $4–5; binding ring + tags ≈ $1; inserts ≈ $3; back panel $2–4; pegs + arms $4–8; **skin: hood $15–35 (UNVERIFIED) or F3 12 × 24 in ≈ $25–30**; collars from an offcut. **≈ $30–55** (the felt is most of it). Build ≈ 10–12 h printing + ≈ 4–5 h (blocking and drying ≈ 1 h hands-on plus overnight).

## Open questions
- **Maker/test:** the corner blocking test (hood vs F3). Decides the default skin.
- **Sourcing:** a grey wool capeline big enough (≈ 400 × 250 flat-equivalent) and its thickness (UNVERIFIED).
- **Eng:** with pegs centred over stems (E-L5's "best" case) strip C runs y ≈ 8–56, and the main board starts at y ≈ 58: confirm the two boards fit side by side at that line (E-L9).
- Bushing height through the felt: a 9 mm pot's bushing (≈ 5 mm) must clear 2.5 shell + tag; confirm with the pot in hand.
