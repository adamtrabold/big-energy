# CATHEDRAL: how it looks and feels (visual, rev 5.1: steer 3, the lid in signal order, after the director's 8)

Seed: CHAMBER rev 2 + FOLD-105 v1.1. Owner record: `design/owner.md` (14:12 → 16:52). Read with `how-it-works.md`, where systems owns the geometry; **§16** is this revision's layout, closing routes and acoustics. The director's steer 2 is in `design/notes/director.md`.

## Steer 3: the lid in signal order (owner, 18:00)
Read the lid like a page, top to bottom, and you follow the sound. **Top row:** the three oscillators, each its own little run (range, freq, wave), with wider gaps between them, then the mixer, osc 1 · osc 2 · osc 3 · noise / ext, levelling them into one signal. The switches that change them sit under them: para, osc mod and osc 3 ctl under the oscillators, source under the mixer. **Middle row:** the two contours that shape that signal, mirrored either side of the speaker window: filter on the left, with its two switches (kbd, filt mod) in a column at the left edge, and loudness on the right, with velocity, touch and decay beneath it. **Bottom row:** the effects, in the order the sound passes through them: echo on the left (type, time with its free / sync, repeats, mix, then delay pan, its hand-off), reverb on the right. **Right-hand column:** out, dry pan → follow → volume, ending in the bottom-right corner, just above TAP and the keys. The effects have left the top. Volume is the last control on the page and the nearest to the hand.

<figure>
<img src="img/cathedral-lid-signal-order-8.7px-per-mm.png" alt="Exact top view of the CATHEDRAL lid. Top row: eight oscillator knobs and four mixer knobs, with four toggles beneath. Middle row: three filter-contour knobs on the left and three loudness-contour knobs on the right, with their toggles beneath, either side of a round window of vertical slots. Bottom row: echo knobs on the left with a toggle, reverb knobs on the right. A right-hand column holds dry pan, a toggle and volume. A small plate reading big energy sits under the window.">
<figcaption><b>The lid, exact, from above</b> (scale bar 20 mm), arrangement P from systems' §17. Groups, in signal order: oscillators ‖ mixer (top), filter contour · window · loudness contour (middle), echo · window · reverb (bottom), out (right column). One handwritten heading per group, each group's switches beneath its knobs, engraved breaks between oscillators and mixer and before the out column, nothing raised. The plate under the window now reads "big energy".</figcaption>
</figure>

**After the director's 8** (systems b3e5525: middle row mirrored, VCOs grouped by spacing, 20 mm within an oscillator and 25 between; my legends and contour headings now live in the checker):
- **Headings read first:** Kalam 3.0 against the 2.35 legends, one per group: oscillators, mixer, filter contour, loudness contour, echo, reverb, out.
- **Real-Kalam fits** (in `rb.nv_overrides`; Kalam's glyphs run taller and wider than the checker's estimate): the contour headings sit at d 67.5 and the oscillators ‖ mixer break starts at 70.5; "oscillators" / "mixer" are 0.4 higher; "reverb" is 2 mm right of REVERB TYPE's fan. **FOLLOW's words sit beside it** (off · follow): above and below, squeezed between DRY PAN and VOLUME, "follow" sat 1.2 from DRY PAN at any workable size. Up / down words on FREE / SYNC sit 1.75 from the toggle.
- **Checks:** systems' rules with these: 0. Real Kalam metrics, ticks, window, pegs: 0.

**Open, for the director:**
- The filter's switch column (kbd, filt mod) at the left edge belongs to the filter contour by row and by mirroring the out column, but it sits 40 mm from its heading. If it reads as orphaned, a short engraved bracket or a break right of the column could tie it.
- **Systems:** FOLLOW "beside" and the heading nudges are visual-only for now; fold them into `layout_check.py`.

## His three complaints (16:52), answered
1. **"off center in that middle section is bad looking … consider the sound of the speaker and the shape."** The speaker window is now **one round opening, centred on the instrument's axis, concentric with the driver, and sized by it**: Ø 46 (the cone plus its surround). Its 15 vertical slots open **≈ 945 mm², about 75 % of the cone's area**, against 265–440 mm² (≈ 20–35 %, choked) in every grille we showed before. Behind it: a foam gasket and a sealed, stuffed back box. It sits directly above CUTOFF, so the window, the hero dial and the keyboard's centre share one vertical line. The shape follows from the sound, not from leftover space.
2. **"there's a massive horizontal gap -- the speaker doesnt feel resolved."** The gap was never the speaker's. Closed, the base's played row lands under the lid's middle, and the knobs were too tall for anything to sit over them. So the played row now uses **low knobs (Ø 10 × 8, bought)**, and the lid's rows are **evenly spaced, 35 mm apart**, with one switch line between the voice rows. **The only open area left on the lid is the round window itself.** The mixer is mirrored around it: osc 1 / osc 2 on the left, osc 3 / noise on the right.
3. **"i'd rather have more brass than black re: keys."** The lead is now **brass naturals with black sharps** (15 brass, 10 black). The alternate is **all brass**. Both are shown in real metal below. The played row's small knobs are gold aluminium, so what the hands play reads as brass, and what you set on the lid reads as black.

**Moves this costs (⚑ director, then owner):** the mixer re-flowed round the window; CUTOFF and EMPHASIS swapped, so CUTOFF sits on the axis; MOD MIX and DRIFT down to the base; the switches gathered into one line; the effects row re-centred on the axis (x 44–242).

**What it costs in feel and size, plainly:** the played row's knobs shrink from Ø 14.9 to **Ø 10** (bought low knobs), and closed grows to **≈ 55.2 mm**. That 55.2 holds only if the played row's pots are snap-in or counterbored (a 1.0 seat) *and* the bend stick seats 3.6 deeper; otherwise it's **56.7–58.8** (systems §16.3). **If he'd rather keep today's full-size knobs, R-TALL does it at ≈ 59.7 closed**; from above it looks the same apart from the knob size, so it isn't rendered.

## The whole
<figure>
<img src="img/cathedral-nave-standing.jpg" alt="CATHEDRAL standing at 120 degrees: the lid holds three evenly spaced rows of black knobs, a line of small toggles, and a centred round window of vertical slots; the base holds a row of small gold knobs either side of a red CUTOFF dial on the axis, the bend stick at the left end and a brass TAP at the right, above brass natural keys and black sharps.">
<figcaption><b>Standing, 120°.</b> Lid in signal order (steer 3): oscillators ‖ mixer at the top, the contours either side of the window, echo and reverb at the bottom, out down the right edge. The Ø 46 window is centred over CUTOFF. Base: the played row is symmetric, with the bend stick at the left end and TAP at the right, and CUTOFF (the one tall, red dial) on the axis. The small gold knobs are the low-profile route (R-LOW). The effects row is centred on the axis (x 44–242), so neither top corner is empty, and the base's right section is MOD MIX · DRIFT · TAP: TAP mirrors the stick and MOD MIX mirrors GLIDE about CUTOFF (the left section has one knob more, so DRIFT sits between, not opposite TUNE). Brass is a tone re-map of the OpenSCAD render; see §1 for the true metal.</figcaption>
</figure>

<figure>
<img src="img/cathedral-nave-top-8.3px-per-mm.png" alt="Exact top view of CATHEDRAL open flat: the lid above with evenly spaced rows and the centred slotted window, the base below with the symmetric played row and the keys.">
<figcaption><b>From above, open flat, exact</b> (scale bar 20 mm). Every legend sits where the checker measures it. The section names (oscillators, mixer, contours) are back, in the hand, on one line between the voice block and the effects row, with "mixer" on the axis over the window. The maker's lozenge sits on the axis under the window, just above the seam (blank in this render; see §6 for the name). Switch-line legends sit beside their toggles, not above: above, they read as the names of the knobs over them. Labels check 0 against systems' rules and 0 with the real Kalam metrics, including ticks.</figcaption>
</figure>

<figure>
<img src="img/cathedral-nave-closed-side-14px-per-mm.png" alt="Exact side elevation of CATHEDRAL closed, from the right end: the lid on top with three nested arched grain grooves on its end face and the stowed brass stay, the base below with USB-C and two MIDI jacks, overall body height dimensioned 55.2 mm.">
<figcaption><b>Closed, right end, exact.</b> 55.2 mm body (R-LOW), plus the screw-feet. The lid's end face carries the arched grain grooves (three nested growth-ring arcs) and the stowed brass stay. At the hinge corner, the side-pivot ear is now the smallest that holds a Ø 3 pin. It still stands ≈ 4 mm past the back (§6 says why it can't go fully inside). The base end shows USB-C and the two MIDI jacks; its 6 mm flat band is left plain (arcs clipped that small read as stray marks).</figcaption>
</figure>

## What CATHEDRAL does to the ideas
**One sentence: a small cathedral, an organ front for the listener, a nave for the hands, and the wood's own arches.** It answers several of his notes at once:

| His note | What CATHEDRAL makes of it |
|---|---|
| "the screen" should have more rounding; the speaker unresolved | **The grille becomes a rose window:** one round opening on the axis, sized by the driver, filled with vertical lancets (slots) whose lengths follow the circle (§3). The evenly spaced rows around it are the nave. |
| fine line texture "more woody", but subtle, not straight woodgrain | **Cathedral grain**: woodworkers' name for the nested arches in flat-sawn wood. The case's line texture becomes arches at about the same sparse line count. The material is already the point of view. |
| too many colours, the brown is out of place; "brass … reminds me of a cathedral"; "more brass than black" | **Brass and black, an organ console's fittings and stop knobs.** What the hands play is brass-toned (keys, TAP, the played row's low knobs); what you set on the lid is black. No colour is added, and the brown goes. |
| faceplate rounding inconsistent | **Every corner arched** (R 7.7, concentric with the walnut block): the two plates read as two rounded leaves meeting at the seam. |
| hidden hinges; feet one with the screws; no spine | **A case with no visible hardware** except the brass that means something: the keys, the stays, two axis screws. Knuckles gone (side pivots), feet are the screws, no spine. |

**Costume watch** (the director's rule, stricter now that the word is "cathedral"): no gothic tracery, no pointed arches as ornament, no stained-glass colour. The window is round because the driver is. Every curve does a job: plate corners, window, grain, key domes.

---

## 1. Key and button colours (fewer colours, no brown, real parts)
**Every option is made from parts that exist** (systems §10). The owner is choosing between A, B and C (brass); D, E and F (birch and printed) stay as alternatives on the same carrier, described in words only. All of them share one interface: a **printed carrier** whose top cup (Ø 9.6 × 3.3) takes a **9.53 × 3.2 tenon**, the tenon of the Cherry Tree Toys 3/8" mushroom plug. So a bought birch plug, a cast brass head and a printed head are interchangeable on the same switches, and the choice can change after the build.

**What shows under each head:** the carrier's 2.8 mm neck (Ø 11.2) and a thin dark ring of deck hole (Ø 12.0). **Print the carriers in matte black.** The neck then reads as the hole's shadow and every head seems to float a little above the deck, like a drawknob on its stem. (A one-piece printed peg has a neck in its own colour; see option F.) The felt washers on the deck are gone: the stop moved under the deck (systems §10.2).

<figure>
<img src="img/cathedral-keys-brass-A-C.jpg" alt="Ray-traced key studies. Top, wide: polished brass naturals in front with glossy black sharps behind on the cream deck. Bottom left: all 25 keys in polished brass. Bottom right: a close view of a black sharp between two brass naturals, the left natural aged dark gold-brown with a bright crown, the right one freshly polished.">
<figcaption>Keys in real metal, ray-traced (POV-Ray). The base's control row is left out because it's being redesigned with low knobs. <b>Top (A, the lead):</b> brass naturals, black sharps: normal keyboard reading, and more brass than black, as he asked (16:52). The sharps are drawn as black-rhodium-plated brass, so every key has the same weight and coldness; printed black sharps are the other route (systems' call). <b>Bottom left (C, the alternate):</b> all brass. <b>Bottom right:</b> close up. A black sharp between two naturals; the left natural is unlacquered after handling (dark gold-brown, bright where fingers rub), the right one freshly polished. Head drawn 4.0 tall until the plug's real height is measured.</figcaption>
</figure>

### Lead: A, brass naturals and black sharps (owner 16:52: "more brass than black"; director steer 2)
- **Why A over B now:** he asked for more brass. A gives 15 brass keys to 10 black, and it keeps a normal keyboard's reading (light naturals, dark sharps), so the reversed-reading question goes away.
- **How it sits with the rest:** the brass field in front is the warmest, brightest thing on the instrument, a row of organ-console fittings under the hands. The black sharps tie back to the black knobs. The red CUTOFF stays the one colour accent, because the base's row is being redesigned around it as the hero on the axis (steer 2), so it has to hold its own against the brass. Visually, the brass row and the red dial will compete less if the low-profile knobs are black and the dial sits on the axis directly above the keys' centre.
- **C (all brass)** is the alternate: the most "cathedral", one material for every key. The two rows then differ only by height and position, and 25 reflections read as a single shining field. Better for an object to look at than for a keyboard to read at a glance.
- **B (black naturals, brass sharps)**, my rev 2 pick, is now the fallback if A's brass field turns out too loud in real metal.
- **Black sharps' material:** black-rhodium-plated cast brass (same weight and coldness as the naturals; 1 µm plating wears through to brass on the crowns over time) or printed matte black (lighter, so a per-group velocity curve may be needed: systems' call).
- **D / E (birch)** are the cheapest real route: one pack of 50 covers both rows. Birch is pale, close to the plate's cream: under a **water-based, non-ambering clear** it stays near it, and an oil finish would turn it yellow. D's black dye covers birch's blotchiness only at full black. **Honest wear note:** dye sits in the surface, so the crown of the most-played naturals will wear pale over time. A hardwax-oil topcoat slows it down.
- **F (printed)** gives exact colours: black to match the knobs, the plate's own cream filament. It feels the least like an instrument (systems §10.3: cooler, slicker, lighter, faint terraces on the dome unless it's resin-printed).

### Brass, two ways to make it (neither is machining)
| | **Cast brass** (3D-printed wax, lost-wax cast by a service) | **Brass-filled filament** (printed by him) |
|---|---|---|
| What it is | Real brass. Sculpteo prints the model in wax and casts it in 80/15/5 copper/zinc/tin; finishes include raw, mirror polish and gold or black rhodium plating; min wall 0.8 mm; max 125 × 125 × 100 mm; 7–9 business days; priced on upload (not checked). | PLA with brass powder (e.g. colorFabb brassFill; product UNVERIFIED this session). Prints dull, polishes to a soft gold with sandpaper and metal polish by hand. |
| In the hand | **Cold at first touch**, then warms. **Heavy**: a solid head ≈ 5 g [CALC: ≈ 620 mm³ × 8.5 g/cm³]; with an open cup underneath, ≈ 2.5–3 g (ESTIMATE). A printed peg is ≈ 0.8 g. | Cool, not cold; warms fast. Heavier than plastic but well short of metal (density UNVERIFIED). Softer edges, a satin glow, not a mirror. |
| Over time | **Worn shine:** unlacquered brass tarnishes to a dark gold-brown everywhere except where fingers rub, so the crowns stay bright, like a church door handle. Lacquered, it stays bright until the lacquer wears off the crowns. Note: an all-tarnished key reads brown, the thing he called out. Keep it handled or polish it now and then. | Dulls slowly; re-polish by hand. Can't take a real shine back once scratched deep. |
| Cost | Per-piece service price, ×15 (A naturals), ×25 (A with plated sharps, or C): UNVERIFIED; quote by upload. | Pennies of filament. |

- **Recommendation:** **cast brass for the naturals in A** (15 pieces; the real metal is the point), mirror-polished and left unlacquered so the crowns earn their shine. The black sharps: black-rhodium-plated cast brass (matched feel) or printed matte black heads on the same carriers.
- **If he wants both rows to feel the same in the hand:** cast all 25 in brass and have the naturals **black rhodium plated** (1 µm). Same weight and coldness on every key. 1 µm will wear through at the crowns with play, and brass will show through the black, slowly. That's either the best thing about it or a fault: his call.
- **⚑ Eng / systems: key mass.** A 2.5–5 g brass head sits on a Choc V2 silent switch. Whether that spring still returns the key briskly, and whether the extra mass changes the velocity fit, is **UNVERIFIED**. Test one cast head on one switch before ordering 10–25. The hollow-cup head (≈ 2.5–3 g) is the one to try first.

### TAP
TAP keeps the rule that it's made of the key material, because it's played in rhythm like a key. With A or C, **TAP is a brass dome** (the naturals' cast head, on a printed cap that fits TAP's switch; part UNVERIFIED) in its black bezel: more brass, and it's played like a key. In steer 2 it moves to the base row's right end, mirroring the bend stick. With D / E, it's a birch plug; with F, printed cream.

## 2. The played row: low, gold, symmetric
- **Low knobs:** Tayda aluminium Ø 10 × 8 (6 mm 18T), bought, on a 1.0 seat (systems §16.3). **Gold** (a Tayda colour) for MOD, TUNE, GLIDE, EMPHASIS, AMOUNT, MOD MIX and DRIFT. They're smaller under the fingers than today's Ø 14.9; R-TALL keeps the big knobs at +4.5 mm closed.
- **The row, anchored on CUTOFF:** BEND 25 · MOD 47 · TUNE 67 · GLIDE 87 | EMPHASIS 119 · CUTOFF 143 · AMOUNT 167 | MOD MIX 199 · DRIFT 230 · TAP 261. R3 is gone (director fix 3).
  - **Why gold:** a rule the eye can read. **What the hands play is brass-toned** (keys, TAP, the played row's knobs). **What you set on the lid is black.** CUTOFF stays the one red hero. Black low knobs are the quieter alternative, also a Tayda colour.
  - **Honest risk:** anodised gold aluminium is usually yellower and more even than polished cast brass. **Order one of each and put them beside a cast key** before committing; if the gold reads as a different metal, go black.
- **CUTOFF** keeps its tall red hero dial, because no low, wide hero exists as a bought part. Closed, it sits under the window.
- **Bend stick** at the left end, its cap lowered to plate + 9 (systems: module seated deeper). **TAP** at the right end: a brass dome in a black bezel, the mirror of the stick.
- **Two lights** either side of CUTOFF (x 131 / 155), symmetric about the axis.
- **Section names:** base: pitch | filter | mod. Lid: **oscillators | mixer | contours**, restored at d 67.5. That line is the one strip that clears both the V2 legends and the effects row, so it's where the names live: "oscillators" left-aligned at x 14, "mixer" on the axis above the window, "contours" right-aligned at x 272.

## 3. The speaker window: sized for sound, then drawn
One round opening, concentric with the 50 mm CDS-5076-class driver, centred on the axis at lid (143, d 32), above CUTOFF (systems §16.4).

<figure>
<img src="img/cathedral-nave-speaker-window-20px-per-mm.png" alt="Drawing at 20 pixels per millimetre. Left: the round window, 46 mm across, filled with 15 vertical slots whose lengths follow the circle; two dashed lines mark hidden ribs behind the plate. Right: a section through the plate, the slots, the foam gasket, the driver with its cone and magnet, and a sealed back box 10 mm deep with stuffing.">
<figcaption><b>The window, exact (20 px per mm).</b> Left: front view. Ø 46, 15 vertical slots 1.8 wide at 3.0 pitch (webs 1.2), each slot's length following the circle; the dashed lines are the two hidden ribs behind the plate. Right: section. Plate 2.5, foam gasket on the driver frame, cone gap ≥ 1.5, and a sealed back box 10 deep, lightly stuffed (systems' sizes).</figcaption>
</figure>

| | Value | Why |
|---|---|---|
| Opening | **Ø 46** (systems §16.4) | the cone plus its surround: the radiating area, no more |
| Slots | **15 × 1.8 wide at 3.0 pitch**, web **1.2** | his "lines going up and down". Odd count, so one slot sits on the axis and the window is symmetric. 1.8 reads as a line at arm's length. A 1.2 web is 3 perimeters with a 0.4 nozzle |
| Open area | **≈ 945 mm²** [CALC], 57 % of the opening, **≈ 75 % of Sd** (12.6 cm², systems ESTIMATE) | between systems' 1.5 / 2.7 (≈ 73 %) and 2.0 / 3.2 (≈ 83 %); the director's target is ≥ 50 %, ideally ~60 % |
| Rear ties | two hidden ribs, 1.2 × 1.5, behind the plate at ±11 mm | 1.2 webs over 40 mm long are flimsy on their own. The ribs stiffen them without a line on the front. They cost ≈ 65 mm² → **≈ 880 net (≈ 70 % of Sd)** |
| Ring | none | the slots' own outline is the edge; a printed ring would add a line beside CUTOFF's scale |
| Behind | foam gasket; sealed, stuffed PETG back box ≈ 60 × 60 × 10 | systems §16.4: the box matters most |

**Loudness, honestly** (systems): clear mids and modest level, roughly +3–6 dB in 1–5 kHz over today's choked grilles (ESTIMATE; bench it). It's a monitor, not a PA.
**Code:** `window_slots()` and `speaker_window()` in `rb.py` drive both the render and the area figure.

## 4. A woodier fine line texture, same subtlety
**Confirmed** (owner 14:40: "Engraving texture I meant fine line texture"): it's the faint line texture on the walnut body. He liked how few lines there were; he wants them to read as wood. **The pipe façade is a placeholder:** he'll design the pipe lines himself, so nothing below judges the façade.



**Built (director ruling 4), not deferred:** real walnut would mean machining, so the printed walnut-tone body is the build, and the texture goes into the print.

- **What it is:** sparse **cathedral-grain arches**, the nested arches of flat-sawn wood, as **U-grooves 0.4 wide × 0.25 deep** in the printed body, at about the old line count.
  - **Base underside and lid back:** 7 nested arches whose axis runs along the case's length. Their spacing opens out a little toward the outside, and the outer ones run off the edges as long, nearly straight lines, as on a real board.
  - **The lid back leaves his façade field empty** (x 30–256, d 8–86). The first arch's apex peeks into the right margin (x ≈ 262), and the arches' tails run out through the bands above and below the field. The grain frames his design without entering it.
  - **Long sides:** the arches' tails, one gentle line across the base's flat band (z 6.2–12.4), two on the lid's far wall above the I/O (z ≥ 13).
  - **End faces:** end grain, so two or three growth-ring arcs. The base's right end keeps its arcs at y < 58, clear of USB-C and MIDI.
- **Printing it:** grooves on the underside and lid back print face-down as clean first-layer channels. On the vertical sides they're cut across layer lines; at 0.25 deep they'll read softly, which is what he asked for (subtle). **UNVERIFIED** that 0.25 reads at arm's length: add a 60 × 40 groove patch to the next coupon print. If it's too faint, go to 0.35.
- **In the model:** `Cathedral(grain=True)` draws them from the same polylines the body CAD will use (`arch_lines`, `side_lines`, `ring_arcs` in `rb.py`). The closed side elevation above shows the lid's end arcs. The base's end faces are left plain: their flat band is only ≈ 6 mm tall, and clipped arcs read as stray marks.
- **Real walnut, if it ever happens:** cathedral figure is how flat-sawn boards look, so it costs nothing. **Pick flat-sawn stock and run the arches along the case's length**, apex toward the hinge. Quarter-sawn (straight) grain is what to avoid: that's his "straight woodgrain would be too detailed".
- **For his façade design:** the lid back's free field is x 34.8–251.2 (systems §3), clear of the four corner feet; the two axis screws sit on x 143 at d 12 / 96; the two Ø 4 push-out holes (x 108 / 178, d 28.3) are fixed by the construction (CHAMBER rev 2 drew them as two pipe mouths). His design has to keep them, or tell systems if it moves them.

## 5. No spine
- **Owner 14:40: "I don't want a spine."** It's gone from CATHEDRAL. The walnut-matched spine of rev 1 is withdrawn.
- What it was solving: closed, a 21.9 × 266 mm slot along the back shows the lid's V1 knobs 7 mm inside it (systems §6). **Systems is answering that, and whether cables can run through the hinge.** Visually, the slot is the one thing that would read as unfinished on an otherwise closed walnut block. If it stays open (the director's recommendation S1), finish it dark inside so it reads as a shadow line, not a hole. The black knobs inside then disappear into it.

## 6. Small things in every render (all ruled, all in the model)
- **Hinges:** systems' side pivots. A round "ear" at each rear corner inside the wall's thickness, with a flush walnut plug over the blind pin. The knuckles are gone. The leaves are hidden inside the walls, so their material doesn't show (see §7).
  - **Director fix 4 asked for the ear inside the outline. It can't go fully inside, and here's why:** for the lid to lie flat open with the seam closed, the axis has to sit at or behind the back face. A lid point at y maps to 2·Ay − y, so the lid's back face lands at 2·Ay − 108, which must be ≥ 108: Ay ≥ 108 (109 with the 2 mm seam). Any ear around a pin at y 109 sticks out past y 108. The R 12 plan corners also cut the end walls back to y ≈ 102 at the very corner.
  - **What I did:** the ear is now the smallest that holds a Ø 3 pin (r 3.0, a 1.5 wall). It's a 6 mm round nub ≈ 4 mm past the back at mid-height, down from a 5.2 radius hulled to the base top (≈ 6 mm and a lobe). Its web runs inside the wall.
  - **To remove it entirely (⚑ systems / director):** an offset pivot with a rabbeted seam (the halves overlap when open, so the axis can move inboard; kinematics UNVERIFIED), or back to v1.1 knuckles across the back, the owner's "if not these are fine".
- **Feet:** four screw-through rubber feet (Ø 12, black, cap plug) at the corner screws; the two axis screws stay flush brass (no impost clash).
- **Plates:** R 7.7 on all eight corners.
- **The name, "Big Energy"** (owner: "name to come -- we're calling it big energy"): it goes **in the lozenge under the window, lowercase, in the panel's hand (Kalam 2.0, "big energy")**, the same voice as every legend on the instrument. It's ≈ 9 mm wide in a 15 mm field, with the descenders inside. Nothing louder: on a cathedral the foundation stone is small and sits on the axis. It's in the model (`Nave.NAME`) and appears from the next render pass, after his CATHEDRAL answer. **Later option:** a cast-brass name plate from the keys' service, letters raised 0.5 (Sculpteo's minimum embossed detail), if he wants the name in metal.
- **Headings:** the lid's effects row carries "echo", "reverb" and "out" over its three groups (breaks at x 157 / 226). The base reads pitch | filter | mod.

## 7. Metal: what "brass" is now that nothing is machined (ruled: brass is the only visible metal)
Rev 1's brass was cut from bar. Systems §11 made the visible metal **printed 316L stainless** (JLC3DP binder jet) or thicker PETG. Here's what that looks like, and the ruling (director 5, as recommended in rev 2).

- **Printed 316L reads as steel, not brass:** a matte, slightly grainy mid-grey, like sintered metal, polishable to a satin silver. Beside brass keys and brass axis screws, two grey stays would be a second metal. **Two metals is a palette change I'd avoid:** with A or C keys, brass is now the instrument's one metal.
- **So, by part:**

| Part | Seen? | Recommend | Looks like |
|---|---|---|---|
| Keys (A: naturals; C: all) | always | cast brass (§1) | polished brass, worn shine on the crowns |
| Lid stays (2, 3 × 8 × 44.4) | standing; as lines on the lid end faces when stowed | **cast brass** from the same service as the keys (fits 125 mm; strength of the cast part at 3 × 8: systems / eng, UNVERIFIED) | brass, matching the keys |
| …fallback | | **printed PETG 5 × 8 in matte black** (systems' option b) | black, part of the knob / foot family. Not grey. |
| Hinge leaves (4) | no, inside the walls | **printed 316L** (systems' option a) | invisible, so steel is fine |
| Axis screws (2) | lid back | bought brass screws | brass |
| Feet | lid back, base | bought black rubber screw-feet | black |
| Façade fill | lid back | his design; brass-tone if he keeps line work | — |

- **If he'd rather go steel everywhere** (316L stays, stainless screws, birch or printed keys): it works and suits CATHEDRAL too, since real organ façade pipes are tin, a silver-grey metal. But it doesn't go with his brass keys, so it's a fallback, not a parallel option.
- **The palette (director 6):** walnut, cream, black, red CUTOFF, brass. No other colour. TAP is made of the key material.
- **The brass on the stays doesn't need plating or paint** if it's cast. Plating printed 316L to look like brass is possible but it's a finish that wears off a part you handle every time you stand the lid up.

## Open
1. **⚑ Director, then owner:** the steer 2 moves (mixer re-flowed, CUTOFF ↔ EMPHASIS, MOD MIX and DRIFT to the base, the switch line, the effects row centred); R-LOW (≈ 55.2 closed with snap-in pots and the lowered stick, else 56.7–58.8; Ø 10 knobs) vs R-TALL (≈ 59.7, today's knobs).
2. **Director:** the hinge ear: accept the 4 mm nub, or ask systems for the offset pivot / knuckles (§6).
3. **Owner:** keys A (lead) or C; lacquered or unlacquered brass; gold or black low knobs.
4. **Systems / eng:**
   - brass head mass on the Choc V2 silent switch; one cast head first;
   - R-LOW's dependencies (seat, shaft length, stick depth);
   - cast-brass stays at 3 × 8;
   - fold visual's legend changes into `layout_check.py` (switch legends beside at 1.55; behind-legends +1.0; section-name line at d 67.5; lozenge at d 2.2–7.2 on the axis). With them, my run of its rules: 0; real Kalam metrics with ticks: 0.
5. **Maker / to buy:** one Cherry Tree Toys birch pack (measure head height H); one Sculpteo quote (hollow brass head, a stay); one Tayda gold and one black 3010 knob, beside a cast key; a groove patch (0.25 / 0.35); bench the window + back box against today's grille.
