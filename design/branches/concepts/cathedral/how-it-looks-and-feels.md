# CATHEDRAL: how it looks and feels (visual, rev 3)

Seed: CHAMBER rev 2 (`../chamber/`) + FOLD-105 v1.1. Owner, 14:12–14:41 (`design/owner.md`). Read with `how-it-works.md` (systems), which owns hinges, feet, plate radii, the slot, options A / B, and the key carrier and no-machining parts in §10–11. The director's steer 1 (`design/notes/director.md`) is applied here.

**Rev 3, 2026-11-13.** Rev 2 brought real-part keys, no spine, the confirmed fine-line texture and brass as the one metal. Rev 3 applies the director's team rulings:
- **Built into the model now** (`design/concepts/_mock-src/rb.py`, class `Cathedral`): R 7.7 on all eight plate corners; screw-through feet at the corner screws with the axis screws flush brass; tapered-slot grilles (vesica in A, Ø 27 circle in B); the "effects" heading in A; **the woody fine-line texture as real shallow grooves** (§4); brass as the only visible metal; the five-colour palette; no spine. Defaults: keys B, no spine.
- **Brass shown as metal** (ruling 9): a new ray-traced study replaces rev 2's flat-yellow key grid (§1).
- **Option B labels fixed** (systems' check): TIME and REPEATS legends behind their knobs; "free" / "sync" 1.5 mm behind the toggle centre (0.5 left "free" 0.64 mm from FREQ 3). `branch_check.py`: A 0, B 0, TOTAL fails 0.
- **Final views are not re-rendered yet:** they wait for the owner's layout answer (coordinator). The rev 1 renders below are marked where they're stale.

## What CATHEDRAL does to the ideas
**One sentence: a small cathedral, an organ front for the listener, a nave for the hands, and the wood's own arches.** It answers several of his notes at once:

| His note | What CATHEDRAL makes of it |
|---|---|
| "the screen" should have more rounding | **The grille becomes a window.** In A, a vesica (the pointed lens of church windows) fits the band's real room. In B, a round rose window. Both use his tapered lines: shortest at the top and bottom, longest through the middle. |
| fine line texture "more woody", but subtle, not straight woodgrain | **Cathedral grain**: woodworkers' name for the nested arches in flat-sawn wood. The case's line texture becomes arches at about the same sparse line count. The material is already the point of view. |
| too many colours, the brown is out of place; "brass … reminds me of a cathedral" | **Black and brass, the colours of an organ console's stop knobs and its brass fittings.** Black keys join the 30 black knobs; brass joins the brass already on the case. The keys add no colour of their own, and the brown goes. |
| faceplate rounding inconsistent | **Every corner arched** (R 7.7, concentric with the walnut block): the two plates read as two rounded leaves meeting at the seam. |
| hidden hinges; feet one with the screws; no spine | **A case with no visible hardware** except the brass that means something: the keys, the stays, two axis screws. Knuckles gone (side pivots), feet are the screws, no spine. |

**Costume watch** (the director's rule, stricter now that the word is "cathedral"): no gothic tracery, no pointed arches as ornament, no stained-glass colour. The vesica appears only because it's the shape that fits the band. Every curve does a job: plate corners, window, grain, key domes.

---

## 1. Key and button colours (fewer colours, no brown, real parts)
**Every option is made from parts that exist** (systems §10). The owner is choosing between A, B and C (brass); D, E and F (birch and printed) stay as alternatives on the same carrier, described in words only. All of them share one interface: a **printed carrier** whose top cup (Ø 9.6 × 3.3) takes a **9.53 × 3.2 tenon**, the tenon of the Cherry Tree Toys 3/8" mushroom plug. So a bought birch plug, a cast brass head and a printed head are interchangeable on the same switches, and the choice can change after the build.

**What shows under each head:** the carrier's 2.8 mm neck (Ø 11.2) and a thin dark ring of deck hole (Ø 12.0). **Print the carriers in matte black.** The neck then reads as the hole's shadow and every head seems to float a little above the deck, like a drawknob on its stem. (A one-piece printed peg has a neck in its own colour; see option F.) The felt washers on the deck are gone: the stop moved under the deck (systems §10.2).

<figure>
<img src="img/cathedral-brass-keys-metal.jpg" alt="Four ray-traced views of the key corner of the base. Top left: polished brass naturals with black sharps. Top right: black naturals with polished brass sharps. Bottom left: all polished brass. Bottom right: a close view with two brass sharps between black naturals, the left one aged and darkened with a bright crown, the right one freshly polished.">
<figcaption>Brass as metal, ray-traced (POV-Ray: reflections and a soft studio light, which OpenSCAD can't do). The head is drawn 4.0 tall (top at deck + 6.8) because the plug's head height isn't published yet. <b>Top left (A):</b> brass naturals, black sharps. <b>Top right (B):</b> black naturals, brass sharps (recommended). <b>Bottom left (C):</b> all brass. <b>Bottom right:</b> close up, two brass sharps between black naturals. The right one is freshly mirror-polished; the left one is unlacquered after handling: dark gold-brown on the body, bright where fingers rub the crown. The walnut and joystick are simplified in this study; it's here to judge the key materials only.</figcaption>
</figure>

### My pick: B, black naturals and brass sharps
- **Why:** the 15 naturals are the big field, and in black they join the knobs, so the playing side reads as one black family on cream. The 10 brass sharps become the accent, the way brass fittings sit on a dark organ console, and they repeat the case's other brass (stays, axis screws). The palette stays at **walnut, cream, black, red, brass**: five, nothing new, no brown.
- **It keeps the light / dark split** a player reads by, reversed like an organ. The reversed-reading question from rev 1 stays open for him.
- **A (brass naturals)** puts the loudest material in the biggest field. In the study, the bright row in front pulls the eye away from CUTOFF and the knobs. I'd only pick it if he wants the keyboard to be the hero.
- **C (all brass)** is the most "cathedral" and the most jewellery-like. The two rows then differ only by position and height, and 25 brass domes compete with the red CUTOFF. Polished, the 25 reflections make the keyboard read as a single shining field, more jewellery box than console.
- **D / E (birch)** are the cheapest real route: one pack of 50 covers both rows. Birch is pale, close to the plate's cream: under a **water-based, non-ambering clear** it stays near it, and an oil finish would turn it yellow. D's black dye covers birch's blotchiness only at full black. **Honest wear note:** dye sits in the surface, so the crown of the most-played naturals will wear pale over time. A hardwax-oil topcoat slows it down.
- **F (printed)** gives exact colours: black to match the knobs, the plate's own cream filament. It feels the least like an instrument (systems §10.3: cooler, slicker, lighter, faint terraces on the dome unless it's resin-printed).

### Brass, two ways to make it (neither is machining)
| | **Cast brass** (3D-printed wax, lost-wax cast by a service) | **Brass-filled filament** (printed by him) |
|---|---|---|
| What it is | Real brass. Sculpteo prints the model in wax and casts it in 80/15/5 copper/zinc/tin; finishes include raw, mirror polish and gold or black rhodium plating; min wall 0.8 mm; max 125 × 125 × 100 mm; 7–9 business days; priced on upload (not checked). | PLA with brass powder (e.g. colorFabb brassFill; product UNVERIFIED this session). Prints dull, polishes to a soft gold with sandpaper and metal polish by hand. |
| In the hand | **Cold at first touch**, then warms. **Heavy**: a solid head ≈ 5 g [CALC: ≈ 620 mm³ × 8.5 g/cm³]; with an open cup underneath, ≈ 2.5–3 g (ESTIMATE). A printed peg is ≈ 0.8 g. | Cool, not cold; warms fast. Heavier than plastic but well short of metal (density UNVERIFIED). Softer edges, a satin glow, not a mirror. |
| Over time | **Worn shine:** unlacquered brass tarnishes to a dark gold-brown everywhere except where fingers rub, so the crowns stay bright, like a church door handle. Lacquered, it stays bright until the lacquer wears off the crowns. Note: an all-tarnished key reads brown, the thing he called out. Keep it handled or polish it now and then. | Dulls slowly; re-polish by hand. Can't take a real shine back once scratched deep. |
| Cost | Per-piece service price, ×10 (B) or ×25 (C): UNVERIFIED; quote by upload. | Pennies of filament. |

- **Recommendation:** **cast brass for the sharps in B** (10 pieces; the real metal is the point), mirror-polished and left unlacquered so the crowns earn their shine. The black naturals: printed matte black heads on the same carriers, or D's black-dyed birch plugs.
- **If he wants both rows to feel the same in the hand:** cast all 25 in brass and have the naturals **black rhodium plated** (1 µm). Same weight and coldness on every key. 1 µm will wear through at the crowns with play, and brass will show through the black, slowly. That's either the best thing about it or a fault: his call.
- **⚑ Eng / systems: key mass.** A 2.5–5 g brass head sits on a Choc V2 silent switch. Whether that spring still returns the key briskly, and whether the extra mass changes the velocity fit, is **UNVERIFIED**. Test one cast head on one switch before ordering 10–25. The hollow-cup head (≈ 2.5–3 g) is the one to try first.

### TAP
TAP keeps the rule that it's made of the key material, because it's played in rhythm like a key. With B, **TAP is a brass dome** (the same cast head, on a printed cap that fits TAP's switch; part UNVERIFIED) in its black bezel. With D / E, it's a birch plug; with F, printed cream.

## 2. A vs B (the speaker and "effects & out")
Layout is systems' (option B moves controls, so it needs the director, then the owner). These are just the two looks, standing at 120°.

<figure>
<img src="img/cathedral-A-standing.jpg" alt="CATHEDRAL option A standing: the lid's band carries a lens-shaped grille of tapered slots; effects amounts stay in the base row">
<figcaption><b>Option A:</b> nothing moves. The band between the voice rows carries one vesica window of tapered slots, centred on the axis. The base row's heading is corrected to "effects", because VOLUME left that section in rev 7.2. Echo and reverb stay split between the lid's back row and the base. <i>Rendered in rev 1: it still shows the retired spine in the joint and rev 1's keys; the stays are brass, as recommended in §7.</i></figcaption>
</figure>

<figure>
<img src="img/cathedral-B-standing.jpg" alt="CATHEDRAL option B standing: all effects and volume on the lid's top row, a round tapered-slot grille at the base's right end, the lid band left plain">
<figcaption><b>Option B:</b> the lid's top row holds every effect in one line, read as the choir: drift | echo (type, time, repeats, mix, tap) | reverb (type, decay, mix) | volume. The speaker moves to the base's right end as a round rose window on the PLAY row's own line. The lid's band is left as a quiet rest. <i>Rendered in rev 1: retired spine and rev 1's keys, as in A.</i></figcaption>
</figure>

**How each looks, my read:**
- **A** fixes the "odd gap" as a picture: the band now has one centred figure instead of a grille island. It doesn't fix the split, which is his other complaint.
- **B** looks the most resolved: each half has one job (hands' row in front, the whole sound chain behind). The rose window fills the place the FX amounts left, and the band reads as intended rest, not leftover space. Visually, B is the better CATHEDRAL. The reach cost (FX amounts ≈ 126 mm further away) is systems' and the owner's to weigh, not a look question.
- **B labels (fixed in rev 3; `branch_check.py` §7 on `Cathedral("B")`: 0 collisions):**
  - FREE / SYNC at (96, d 69) sat on "osc 3 ctl". In B the band below is empty, so **the V2 row's three toggle legends (osc 3 ctl, source, velocity) move under their toggles.**
  - The left voice rule ends at dV2 + 5.5 so it stops short of "sync".
  - Systems' check found the REPEATS legend under the toggle by 1.7 mm. **TIME and REPEATS legends now sit behind their knobs** (d + 13.05, like TIME / DECAY in A).
  - **"free" / "sync" sit 1.5 mm behind the toggle centre** (0.5 left "free" 0.64 mm from FREQ 3; 1.5, 2.0 and 2.5 all check 0).
- **A, a correction to systems' §2 / §5:** a Ø 34 round window fits the band's depth but overlaps the NOISE / EXT legend and the "mixer" heading. **The band's real clear depth between those labels is ≈ 22 mm.** Hence the vesica: **66 × 16, centred at (143, d 37.6)**, ring clear of both labels. Open area ≈ 700 mm² vs v1.1's 900 (−22 %, acoustics UNVERIFIED).

## 2b. The speaker, round 2 (owner: no speaker on the key side, no eye shape; "lines going up and down", or "a circle and maybe not centered")
Systems §14: B's single effects row stays on the lid, and the speaker stays in the lid band, where v1.1 had it (P1). Nothing else moves for the speaker. The other placements are dropped at the owner's steer: the rounded rectangle (lines run sideways) and firing through the façade (P2: muffled flat on a table, and quieter for the player).

<figure>
<img src="img/cathedral-speaker-options-standing.jpg" alt="Two standing views of CATHEDRAL layout B side by side, with a close view of each lid band below. Left: the band grille is eleven vertical slots stepping up to the middle and down again, standing on one line like an organ-pipe tower. Right: a small circle of vertical slots sits off-centre, to the right of the mixer heading. In both, the base row is centred on the instrument and the sharps and TAP are brass.">
<figcaption><b>Left, the pipe tower:</b> 11 vertical slots, 2 wide at 5 pitch, lengths 8 → 18 → 8, all standing on one foot line (a gable, not a lens), centred on the axis over the speaker. <b>Right, the off-centre circle:</b> vertical slots tapered to a circle, Ø 25 overall with its ring, at (160, d 37), 17 mm right of the axis and still over the speaker. Below each, the same band up close. Both use layout B's effects row and keys B (black naturals, brass sharps, brass TAP). <b>The base's freed right end:</b> the PLAY row (pitch and filter) moves 47 mm right so it's centred on the instrument's axis, with equal margins at both ends. Brass here is a tone re-map of the OpenSCAD render, not ray-traced (see §1 for the true metal look).</figcaption>
</figure>

**Both fit the band.** Label check: the tower's slot tips clear "mixer" by 1.68 mm and "noise / ext" by 1.9. The circle's ring clears every label by ≥ 1.5 only in x 158–176 (my sweep), which agrees with systems' best spot. The centre is the worst spot for a circle (≈ 19 mm max). The full model check for both, with the PLAY row centred, finds 0 collisions.

**My read:**
- **The tower** answers "lines going up and down" most directly, and it's the most CATHEDRAL: a small pipe tower inside, echoing the façade outside. It sits on the axis, so it keeps FOLD's "everything single sits on x 143" rule. It looks like a designed figure, not a hole. This is my pick.
- **The off-centre circle** is calmer and smaller. Off-centre, it reads as placed on purpose, like a sound hole beside the mixer, not a target. The cost is the axis rule: it's the one single element off the centreline, and only 17 mm off, so it can look slightly mis-placed rather than clearly asymmetric. If he likes the circle, I'd keep it exactly where it is: it's the only place it fits.
- **Loudness:** open area is the tower ≈ 290 mm² vs the circle ≈ 265, both ≈ 35–40 % below today's 440 (systems; loudness UNVERIFIED). Widening the tower's slots to 2.5 brings it to ≈ 340 [CALC: 136 mm of slot length × 2.5] with almost the same look.

**What I put in the empty base end, and why:** with the effects on the lid and the speaker out of the base, x 186–270 is empty. **I'd re-centre the PLAY row on the axis** (systems' option 2): the stick moves to x 72 and AMOUNT to 214, with the breaks and headings moving with them. The hands' row then sits centred under the choir, like the nave under the crossing, and the empty space becomes two equal margins instead of one hole.
- **Rejected:** bringing VOLUME and TAP back to the base (option 1) undoes his "together" for the out control. The lozenge and lights (option 3) would be ornament filling a gap.
- **⚑ D+O:** it moves controls. The stick ends up 47 mm further from the left end; with the keys running full width, that's still under the left hand.

## 3. The grille ("the screen")
<figure>
<img src="img/cathedral-grille-options-20px-per-mm.png" alt="Three grille patterns at true proportion with a 10 mm bar: a lens of horizontal tapered slots, a circle of horizontal tapered slots, a circle of concentric arc slots">
<figcaption>Grille patterns, 20 px per mm. <b>Left:</b> the vesica, 66 × 16 (option A). <b>Middle:</b> tapered slots in a Ø 27 circle (option B). <b>Right:</b> concentric arcs in a Ø 27 circle, his "circular" alternative. All slots are 1.25 wide at 2.3 pitch.</figcaption>
</figure>

- **Ruled (director): tapered slots (left / middle), his first option.** Vesica 66 × 16 in A, Ø 27 circle in B. Concentric arcs are dropped. Both are in the model.
  - They keep the v1.1 grille's language (horizontal bars) and simply round its silhouette.
  - Outside, the façade is a tower of vertical pipes whose lengths rise toward the middle. Inside, the window is a stack of horizontal lines whose lengths rise toward the middle. Same rule, turned 90°. (That rhyme holds only if his own façade keeps vertical pipes; the slots stand on their own if it doesn't.)
- **Concentric arcs** read more like a speaker cone and need bridges (four drawn) to hold the centre. They're more "hi-fi" than "cathedral".
- A thin warm-grey ring (the plate's rule colour) frames each window, so it reads as a window, not a hole pattern.

## 4. A woodier fine line texture, same subtlety
**Confirmed** (owner 14:40: "Engraving texture I meant fine line texture"): it's the faint line texture on the walnut body. He liked how few lines there were; he wants them to read as wood. **The pipe façade is a placeholder:** he'll design the pipe lines himself, so nothing below judges the façade.

<figure>
<img src="img/cathedral-closed-with-book.jpg" alt="CATHEDRAL closed beside a hardback, seen from behind: walnut with faint arched grain, a placeholder pipe façade, corner screw-feet, and a spine that has since been dropped">
<figcaption>Closed, seen from behind: cathedral grain at about the old line count (here a 2D post-process; the modelled grooves replace it in the next pass), four screw-feet at the corners (the case screws), two flush brass axis screws. <i>Rendered in rev 1:</i> the pipe façade is a placeholder for his own design, and <b>the spine shown is retired</b>; the back slot is waiting on systems' answer.</figcaption>
</figure>

<figure>
<img src="img/cathedral-grain-detail.jpg" alt="Close crop of the lid back: sparse nested arched grain lines under the placeholder pipe façade">
<figcaption>Detail: the arches are low-contrast and spaced about as widely as the straight streaks were, so the grain stays ground under whatever figure goes on the lid back.</figcaption>
</figure>

**Built (director ruling 4), not deferred:** real walnut would mean machining, so the printed walnut-tone body is the build, and the texture goes into the print.

- **What it is:** sparse **cathedral-grain arches**, the nested arches of flat-sawn wood, as **U-grooves 0.4 wide × 0.25 deep** in the printed body, at about the old line count.
  - **Base underside and lid back:** 7 nested arches whose axis runs along the case's length. Their spacing opens out a little toward the outside, and the outer ones run off the edges as long, nearly straight lines, as on a real board.
  - **The lid back leaves his façade field empty** (x 30–256, d 8–86). The first arch's apex peeks into the right margin (x ≈ 262), and the arches' tails run out through the bands above and below the field. The grain frames his design without entering it.
  - **Long sides:** the arches' tails, one gentle line across the base's flat band (z 6.2–12.4), two on the lid's far wall above the I/O (z ≥ 13).
  - **End faces:** end grain, so two or three growth-ring arcs. The base's right end keeps its arcs at y < 58, clear of USB-C and MIDI.
- **Printing it:** grooves on the underside and lid back print face-down as clean first-layer channels. On the vertical sides they're cut across layer lines; at 0.25 deep they'll read softly, which is what he asked for (subtle). **UNVERIFIED** that 0.25 reads at arm's length: add a 60 × 40 groove patch to the next coupon print. If it's too faint, go to 0.35.
- **In the model:** `Cathedral(grain=True)` draws them from the same polylines the body CAD will use (`arch_lines`, `side_lines`, `ring_arcs` in `rb.py`). The rev 1 images below used a 2D post-process instead. They show the idea, not the modelled grooves; the next render pass shows the real ones.
- **Real walnut, if it ever happens:** cathedral figure is how flat-sawn boards look, so it costs nothing. **Pick flat-sawn stock and run the arches along the case's length**, apex toward the hinge. Quarter-sawn (straight) grain is what to avoid: that's his "straight woodgrain would be too detailed".
- **For his façade design:** the lid back's free field is x 34.8–251.2 (systems §3), clear of the four corner feet; the two axis screws sit on x 143 at d 12 / 96; the two Ø 4 push-out holes (x 108 / 178, d 28.3) are fixed by the construction (CHAMBER rev 2 drew them as two pipe mouths). His design has to keep them, or tell systems if it moves them.

## 5. No spine
- **Owner 14:40: "I don't want a spine."** It's gone from CATHEDRAL. The walnut-matched spine of rev 1 is withdrawn.
- What it was solving: closed, a 21.9 × 266 mm slot along the back shows the lid's V1 knobs 7 mm inside it (systems §6). **Systems is answering that, and whether cables can run through the hinge.** Visually, the slot is the one thing that would read as unfinished on an otherwise closed walnut block. If it stays open (the director's recommendation S1), finish it dark inside so it reads as a shadow line, not a hole. The black knobs inside then disappear into it.

## 6. Small things in every render (all ruled, all in the model)
- **Hinges:** systems' side pivots. A round "ear" at each rear corner inside the wall's thickness, with a flush walnut plug over the blind pin. The knuckles are gone. The leaves are hidden inside the walls, so their material doesn't show (see §7).
  - Honest: the axis sits 1 mm behind the base's back face, so each ear still shows as a small round boss at the rear corners when closed, quieter than a knuckle.
- **Feet:** four screw-through rubber feet (Ø 12, black, cap plug) at the corner screws; the two axis screws stay flush brass (no impost clash).
- **Plates:** R 7.7 on all eight corners.
- **Headings:** A reads "effects" (not "effects & out"); B drops the base heading over the speaker. The lid's back row in B carries "echo" and "reverb" over their groups.

## 7. Metal: what "brass" is now that nothing is machined (ruled: brass is the only visible metal)
Rev 1's brass was cut from bar. Systems §11 made the visible metal **printed 316L stainless** (JLC3DP binder jet) or thicker PETG. Here's what that looks like, and the ruling (director 5, as recommended in rev 2).

- **Printed 316L reads as steel, not brass:** a matte, slightly grainy mid-grey, like sintered metal, polishable to a satin silver. Beside brass keys and brass axis screws, two grey stays would be a second metal. **Two metals is a palette change I'd avoid:** with B or C keys, brass is now the instrument's one metal.
- **So, by part:**

| Part | Seen? | Recommend | Looks like |
|---|---|---|---|
| Keys (B: sharps; C: all) | always | cast brass (§1) | polished brass, worn shine on the crowns |
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
1. **Owner (being asked now, one at a time):** speaker: pipe tower or off-centre circle (§2b; my pick: tower), and the re-centred PLAY row (⚑); hidden pins vs cables through the hinge; the back slot; keys A / B / C (my pick: B, black naturals + cast-brass sharps; reversed reading).
2. **Owner, after keys:** if brass, unlacquered (crowns stay bright, the rest darkens) or lacquered (bright until it wears)?
3. **Systems / eng:**
   - brass head mass (2.5–5 g) on the Choc V2 silent switch: return and velocity fit; test one hollow head first;
   - cast-brass stays: strength at 3 × 8 (or the black PETG 5 × 8 fallback);
   - B's base rose (Ø 27) vs the Daisy (eng).
4. **Maker / to buy:** one pack of Cherry Tree Toys 3/8" birch plugs (measure head height H: it fixes the key height); one Sculpteo quote by upload (hollow-cup brass head, a stay); a groove patch (0.25 and 0.35 deep) on the next coupon; the vesica's open area (acoustics).
5. **Re-render pass after his layout answer** (coordinator relays it): closed, standing (chosen layout) and keys, no spine, modelled grooves, chosen key colours. The standing and closed views can then come from POV-Ray too, if the director wants the brass believable in them as well. Keep it to those three.
