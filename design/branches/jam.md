# Branches jam: more personality, a whole point of view (started 2026-11-13)

Owner's words and direction: see `design/owner.md`, the entry dated 2026-11-13 11:47. Starting points: the v1.1 locked concepts in `versions/v1.1/` (HUSH, ONE SHEET, FOLD). Locked folders are never edited; branches are new concepts in `design/branches/concepts/`.

Turns are added below, newest at the bottom. Each turn ends with `NEXT: <role> — <why>`.

---

## Turn 1 — product designer (systems focus), 2026-11-13

### 1. Jobs first (written from the owner's words before opening the spec or `design/jobs.md`)
Marks: **stated** = his words. **inferred** = mine, a scope question for him, not a demand.

| # | Job | Mark |
|---|---|---|
| B-J1 | **Feel a point of view in the object**: one idea that drives form, material, making and feel, drawing on furniture, instruments, tools, art and emotion. | stated ("holistic *point of view* / concept"; "principles of design of furniture… instruments, tools… artistic inspirational forms and emotion") |
| B-J2 | **Want to play it**: the object has personality and puts him in a mood (it inspires, not just works). | stated ("add some more personality"; "be inspired") |
| B-J3 | **Play keys with character** (his example: HUSH's pegs; on FOLD maybe "organ like"). An example, not a direction. | stated as example |
| B-J4 | **Take it to the park and play it there.** | stated |
| B-J5 | Get there: carry it on a walk, hand-held or in a bag, and be playing within a minute of sitting down. | inferred |
| B-J6 | Play without a table: on grass (cross-legged), a bench, a lap; it doesn't slide, tip, or mind damp grass. | inferred |
| B-J7 | Read the panel and the status light **in bright sun** and in dappled shade. | inferred |
| B-J8 | Hear it outdoors, where there are no walls to help the small speaker; or on phones. | inferred |
| B-J9 | Last an afternoon on battery, and know how much is left. | inferred (runtime target never stated by him) |
| B-J10 | Survive outdoors: sun on a dark body, grass, dust, a drop onto turf, near water. | inferred |
| B-J11 | Share it: a friend on the bench can see it, hear it, have a go. | inferred |
| B-J12 | **Have the echo follow MIDI tempo when a clock is present** (USB or TRS). | stated |
| B-J13 | **Turn tempo sync on and off, and see which it's in.** | stated (follow-up: "am i missing a control…") |
| B-J14 | Pick the echo's note division when synced; set free time when not. | inferred from B-J12 |
| B-J15 | Nothing jumps or clicks when the clock starts, stops or changes tempo. | inferred |
| B-J16 | Keep the tempo with no clock (the park has no DAW): tap it, and see it. | inferred |
| B-J17 | Choose between ONE SHEET and FOLD later without the branch work being wasted: the same internals carry either. | inferred ("the internals are probably the same eh?") |

**Against `design/jobs.md` rev 4:**
- Covered already: J12 (one clear idea), J15 (play where he is: table, lap, couch), J7 (power, know the charge), J5 (speaker on table and lap), J19 (echo, "or follow MIDI clock").
- **New for the branches:** emotion and personality (B-J1–3) go further than J12's "traceable to principles"; J12 asked for logic, he now asks for feeling too. The park (B-J4–11) stretches J15 to the ground, sun, walking and sharing; J5 to outdoors; J7 to a stated session length. **MIDI-synced echo has no flow and no sync on/off anywhere** (B-J12–16): J19 names it in one clause. B-J17 is a constraint on every branch: change the outside, not the board.
- I'll fold these into `design/jobs.md` (rev 5) after the jam, as the brief says.

### 2. Draws (`secrets.SystemRandom`, script `design/branches/draw-systems.py`, run 2026-11-13)
First run:
- **Oblique:** "Cut a vital connection", "Decorate, decorate", "Only one element of each kind".
- **Furniture:** Nakashima live-edge slab · **Instrument:** pipe organ (stops, ranks, pull-knobs) · **Tool:** Opinel knife (one lock ring) · **Art:** Barbara Hepworth pierced form (hole as figure).
- **Emotions:** focus, calm · **Park moments:** in bright midday sun; by water.
- **Twists:** "it can hang on a wall", "light passes through it", "it looks like it was found, not bought".
- **Seed concept per branch:** ONE SHEET, FOLD, HUSH.

Honest note: two of the three oblique cards ("Cut a vital connection", "Only one element of each kind") came up by chance in the first jam's draws (`design/jam.md` §5). I kept "Decorate, decorate" and **redrew the other two from the deck minus every card earlier jams used**: "Use fewer notes", "State the problem in words as clearly as possible". Then a separate draw for the echo-sync question, from 8 borrowed "following" systems: **a conductor (follows the beat, keeps their own phrasing)**.

(The pipe organ landing right after he said "organ like" is a coincidence of a real draw. I take it as permission, not as a direction.)

### 3. Structure: what every branch shares (B-J17)
- **The board is the constant; the outside is the branch.** Every branch keeps common rev 7.x's rows, the Daisy, the mux plan and the key mechanism of its seed. A branch may change: enclosure form and material, key tops (bought), the bottom, a handle or hole outside the board outline, graphics, finish, and where the jack wall is. That way "ONE SHEET or FOLD" stays a late choice.
- **Pegs are portable.** HUSH's peg is a bought 1/2 in button plug on a laser-cut arm over the same Choc V2 + Hall sensor (`versions/v1.1/hush/how-it-works.md` §Keys). Any branch can take pegs. **Cost of pegs:** heads stand ≈ 6.5 above the surface by mechanism, so they can't sit "within 3 mm" (R4) and, on FOLD, they eat the closed clearance. Open for eng: FOLD closed height with pegs (+≈ 4 mm, or a lid pocket over the keys).

### 4. Flows the branches add
- **F15 A park session (B-J4–11):** walk with it (handle / hole / strap / bag) → sit (grass, bench, lap) → power on → status light "ready" (must be readable in sun) → play on the speaker (or phones) → a friend has a go (keys and stick reachable from the side) → tap a tempo, echo in time → power off, pack, walk. Each branch fills in its own carry, sit and pack steps.
- **F13 Echo in time with a MIDI clock** and **F14 Tap tempo with no clock**: in `design/branches/echo-clock.md` §5–6.

### 5. The echo under MIDI clock (B-J12–16), short version. Full spec: `design/branches/echo-clock.md`
- **The owner's follow-up: yes, a control is missing.** The spec reads clock on USB and TRS (`daisy-first-principles.md` §5.4) and the DSP can sync repeats and crossfade cleanly (§6.2), but nothing on the panel says whether the echo is following. Eng's research note had a hidden gesture (hold TAP + turn TIME, `single-chip-research.md` §5.2) that never reached the panel spec.
- **Draw "State the problem clearly":** sync on/off really means **"does TIME read in milliseconds or in beats?"**
- **Option A ($0):** automatic. Clock present → follow; hidden hold-TAP + TIME gesture to stay free. The mode lives in memory, not on the panel.
- **Option B ($≈1, one mux channel, 46/48), systems recommends; OWNER DECISION:** a 2-way **SYNC toggle, FREE / SYNC**. TIME gets two machine-marked scales: ms (≈ 20 ms–2 s) and 9 divisions (1/16 … 1/8. … 1/2). In SYNC the tempo comes from the clock if there is one, else from TAP. TAP never fights the clock. Clock lost → hold the last tempo. TAPE/BBD glide to a new tempo like a tape motor; CLEAN/PING-PONG crossfade. Feedback stays on the one status light (H7): tempo ×4 after a tap, 2 green on lock, 2 amber on loss.
- **Draw "conductor":** the clock sets the beat; the player keeps the phrasing (division, repeats, type). That's why TAP has no job under clock: you don't argue with the conductor about tempo.
- **Scope question:** should Little D send its tapped tempo as clock out (USB/TRS)? A drum machine in the park would follow it. Firmware only; new behaviour.

### 6. Creative directions: branches with a whole point of view
Four ideas that differ in kind. I lead on how each works; the visual designer owns how they look, and may reshape or kill any. Each says which draws fed it.

#### BRANCH 1 — BUTTERFLY *(kind: a piece of furniture. Seed: ONE SHEET)*
*Draws: Nakashima live-edge slab, "it looks like it was found, not bought", "it can hang on a wall", calm.*
**Point of view: one board with two edges. The hands get the true edge; the world gets the natural one.**
1. **The playing edge is dead straight and exact** (edge A, keys to the front), *because* that's where precision serves the hand. **The rear edge is live**: a scanned live edge of a real walnut slab, printed in walnut-tone filament first, real planed walnut later. *Because* nothing touches it but light and the eye.
2. **The joint is the ornament.** ONE SHEET already splits at x 122.5 for printing (common §5). Nakashima closes splits with **butterfly (bowtie) keys**; so does this. One visible walnut butterfly across the seam on the face's rear band, and one on the back. *Because* honest construction shown is calmer than hidden construction.
3. **It lives on the wall when it isn't played.** A French-cleat slot in the back panel; it hangs like a small shelf (J18 becomes a real job here, not optional).
4. **One material, oiled; one colour accent** (CUTOFF).
**How it works (systems):** structure = ONE SHEET unchanged. The live edge only varies the 26.5 mm rear band; its deepest notch must keep ≥ 12 mm to the FX row's knob edges (R4 rims rule) → the body grows ≈ 10–15 mm at the back [CALC, rough]. The cleat must clear the battery strap and speaker on the back panel. Park: it reads as found, not bought; calm on grass.
**Risk:** printed "wood" can look fake; that's the visual designer's problem and the reason real walnut later is part of the idea.

#### BRANCH 2 — CHAMBER *(kind: an instrument case. Seed: FOLD)*
*Draws: pipe organ, "Decorate, decorate", calm.*
**Point of view: FOLD opens like a small chamber organ. The standing lid is the case front; the base is the console.**
1. **The Model D's RANGE is already in organ feet** (32', 16', 8', 4', 2'). The heritage is real, not costume: the three oscillators are three ranks. Graphics can say so.
2. **Reverse keyboard**: dark walnut pegs for the naturals, light maple pegs for the sharps, the baroque organ and harpsichord convention. That's his pegs-on-FOLD hint made specific, with bought button plugs and HUSH's proven arm. *Because* it changes the character of the whole object at ≈ $0 over HUSH's pegs.
3. **Decorate only where decoration works:** the speaker grille in the lid's band (centred on x 143, `fold/how-it-works.md` §5) becomes a short **pipe façade**: vertical slots with pipe mouths. When the lid stands at 120°, the façade faces the player, as an organ façade faces its listeners.
4. **Brass stays and hinge as the case hardware** (already brass in v1.1).
**How it works (systems):** FOLD-105 unchanged inside. Pegs need FOLD's base re-checked: heads ≈ 6.5 above the surface vs. FOLD's closed landing rule (lid controls ≥ 2.0 above what they land on). Likely +≈ 4 mm closed height or a shallow pocket in the lid over the keys. Edge A with pegs: HUSH shows heads 7.15 from the front face. **Owner check:** reversed key colours can slow sight-reading for a player used to a normal keyboard. A dealbreaker? His call.

#### BRANCH 3 — PIERCED *(kind: a carried tool. Seed: HUSH as drawn; transfers to ONE SHEET)*
*Draws: Hepworth pierced form (hole as figure), Opinel (one lock ring), "light passes through it", in bright midday sun, by water.*
**Point of view: it has a hole through it. The hole is how you carry it, how you hang it, and how the sun gets in.**
1. **The void is the figure.** One round through-hole (≈ 40 mm) at the right end, beyond TAP and the status light. Four fingers through it: carry it like a painter's palette or pochade box on a walk.
2. **It hangs from anything**: a branch, a hook, a peg rail.
3. **In sun it throws a disc of light** on the grass beside you. The instrument marks noon. (Optionally a thin tinted acrylic lens in the hole, a coloured spot; visual's call.)
4. **One ring:** like the Opinel's single lock ring, one turning brass ring is the only visible fastener/closure. On HUSH it holds the felt roll; on FOLD it would lock the halves.
**How it works (systems):** the board fills the current outline (≈ 268 × 122), so **the hole needs its own length: ≈ +55 mm at the right end** (40 hole + walls) [CALC, rough] → ONE SHEET ≈ 331 × 180. That is a real cost against "portable" and against print-bed size. **It's a carry and hang handle, not a playing grip**: the left hand must stay free for the stick and MOD, and the right plays. Weight sits 55 mm further right: on a lap it's fine; hung, it hangs keys-down unless the hole is centred on the mass (eng: centre of mass).
**Why HUSH:** the draw said so, and soft felt round a hole is a good hand-feel. He leans ONE SHEET / FOLD, so I'd show it on ONE SHEET.

#### BRANCH 4 — GROUND *(kind: a posture. Seed: either; systems-led)*
*Draws: "Cut a vital connection" (cut the table), "Use fewer notes", focus.*
**Point of view: made for the ground, not the desk. It sits on grass in front of you, cross-legged, tilted to your eye.**
1. **Cut the table:** every v1.1 concept assumes a table or lap. This one has a **designed underside**: a wedge base (≈ 12–15° rake) of cork or TPU that grips grass and doesn't wick damp, so seated on the ground the panel faces you.
2. **The bottom is as designed as the top:** the wedge is fixed, one piece, and it is the only thing between the instrument and the ground. Nothing to deploy.
3. **Use fewer notes:** outdoors, the PLAY row is what you touch; the VOICE is set at home. Graphics weight the PLAY row and dim the VOICE (no control removed: the spec is locked).
4. **Sun first:** status light under a short hood (light pipe recessed), legends with high contrast at low sun angles.
**How it works (systems):** structure as seed; the wedge adds ≈ 15–25 mm at the back [CALC rough] and changes the speaker path (ONE SHEET's speaker fires down through the back panel, so the wedge must open under it or the speaker moves). Strongest answer to B-J6/B-J7; weakest on personality unless the visual designer finds its voice.

### 7. Interaction ideas for any branch
- **Status light in sun (B-J7):** a 5 mm LED in midday sun is nearly invisible, and flashes are worse. Recess it under a hood or behind a light pipe; or accept that the lit TAP (echo-clock.md §4, breaks H7) is the sun-readable answer. Director's call.
- **Battery for an afternoon (B-J9):** FOLD-105 carries the slim ≈ 11 Wh pack (owner record). Halving eng's 22.2 Wh figures gives ≈ 1.9–3.9 h [CALC, from `daisy-first-principles.md` §7.1]. That may not last a park afternoon at the high-draw end. Hall gating (§1.5) is the biggest lever. **Open question for him:** how long is a park session?
- **Speaker outdoors (B-J8):** no walls, so it'll sound quieter and thinner than indoors. ONE SHEET fires down into the table; on grass that's absorbed. A branch that fires the speaker toward the player (FOLD's lid already does) wins outdoors.
- **Heat (B-J10):** a dark walnut-tone PLA body in midday sun can soften (PLA glass transition ≈ 55–60 °C) and warms the LiPo. PETG/ASA for park branches. Eng to confirm.

### Open questions (named plainly)
1. **Owner:** sync control A ($0, hidden) or B (FREE / SYNC toggle, ≈ $1)? Systems recommends B.
2. **Owner:** should the tapped tempo go out as MIDI clock?
3. **Owner:** how long is a park session (sets battery: matters for FOLD-105's slim pack)?
4. **Owner (CHAMBER):** reversed key colours OK?
5. **Eng:** pegs on FOLD (closed height); FREE range and divisions; PLA vs PETG/ASA in sun; mux channel 46 on the right mux per concept.
6. **Director:** H7 (one light) vs. a lit TAP for tempo and sun readability.

NEXT: product designer (visual focus) — four branches need their look, material and emotion pushed (and any killed), and the SYNC switch needs a home near TIME in each branch if the owner picks Option B.

---

## Turn 2 — product designer (visual focus), 2026-11-13

### 0. What applies (from the owner's words, his record, the rules)
- He asked for **personality and a point of view**, not new features. His sources: furniture, instruments, tools, art, emotion. **The park** is a place to be inspired, not just a test environment. A picture has to make him want to carry it there.
- He loves **HUSH's pegs**; "organ like" on FOLD is an example, not a direction. **ONE SHEET loved for its rings**; his rule there was "only no texture and the rings texture".
- Binding: keys and knobs are bought parts; nothing raised among the knobs or between the keys and the controls; no screens or encoders; edge A; cost first; portable; internal battery; unibody, screws from the back (flexible). The v1.1 locks stay untouched.
- **New and settled (owner, 11:58): "B".** A FREE / SYNC toggle near TIME goes in every branch. Placement is in §6.
- I accept systems' shared rule ("the board is the constant, the outside is the branch"). It's what keeps ONE SHEET vs FOLD a late choice, and it gives each branch a clean brief: *only the outside may speak.*

### 1. Draws (`secrets.SystemRandom`, `design/branches/draw-visual.py`, run once, 2026-11-13)
My decks are deliberately different from systems' (furniture *principles* rather than famous pieces, other instruments, tools, art, colours). Every Oblique card used in an earlier jam is removed from the deck before the draw.
- **One Oblique card per branch:**
  - BUTTERFLY: "Spectrum analysis".
  - CHAMBER: "Humanize something free of error".
  - PIERCED: "Disconnect from desire".
  - GROUND: "Listen to the quiet voice".
  - NEW: "Don't be afraid of things because they're easy to do".
- **New-branch seeds:**
  - furniture principle: *the stretcher*;
  - instrument: concertina;
  - tool: binoculars;
  - art: **Bridget Riley** (stripes, vibration);
  - emotion: **calm**;
  - park moment: **under a tree in dappled light**;
  - accent: **mustard**;
  - seed concept: **ONE SHEET**.
- **One emotion per branch:** BUTTERFLY longing · CHAMBER joy · PIERCED shyness · GROUND exuberance.
- **Kill test (d20, ≤ 4 = argue seriously for killing):** BUTTERFLY 5 · CHAMBER 13 · PIERCED 9 · GROUND 7. Nobody rolled a kill. BUTTERFLY came closest. I kill PIERCED anyway on judgement (below), and I say why.
- **SYNC placement twist (d6):** 3, "on the jack wall". I tested it seriously and rejected it (§6).
- **Unused, honestly:** stretcher, concertina and binoculars. I tried them: a two-barrel body with a strap, and a worn "vendor tray" played standing. Both added width or a posture he didn't ask for, so I dropped them. The tray is noted at the end in case he likes standing.

Sketches (quick, not render-grade): `design/branches/concepts/jam-sketches/` (source `sketch_turn2.py`; the layout is read live from `fold_r5_check.py`, ONE SHEET x = FOLD x − 5).

---

### 2. BUTTERFLY → keep, reshaped: **"the machine meets the tree"** *(ONE SHEET)*
Sketch: `t2-butterfly-real-rail.png`.

**What I kill: the scanned live edge printed in walnut-tone filament.** A printed copy of a tree is a souvenir. It's the first thing anyone would do, and it fails the brand's honesty: "found, not bought" can't be faked from a spool. The kill-test roll (5) agrees with me.

**What I keep and push:**
- **The rear band becomes real wood from day one.** A strip of real live-edge walnut offcut (≈ 22 mm deep plus the edge's wander, full width) replaces ONE SHEET's printed rear band.
- **It meets the printed face at one straight joint, closed by one butterfly key on the axis (x 138).** The axis sits in the back row's centre break, clear of every knob. The jacks are drilled through the wood, in their board positions.
- **Each instrument's back edge is different.** That's where *longing* comes in: it's yours, and it's the one part of the object that reminds you of a particular tree. Small live-edge walnut offcuts are a scrap product, cheap next to the shell (ESTIMATE; not priced). It's also work you're already set up for, since you work solid walnut.

**"Spectrum analysis" gives the point of view its rule. Precision is a spectrum running front to back:**
1. **The front edge is exact.** Keys at edge A; machine-straight, because the hands need it.
2. **The face is exact but soft.** Printed cream; still and rippled (v1.1's two finishes, unchanged).
3. **The joint is exact and shown.** One straight line and one butterfly.
4. **The rear is free.** The tree's own edge; nothing touches it but light.

Read from your seat, the object goes from tool to tree as it moves away from you. That's the whole idea: one sentence, and it decides every line.

- **Joint position:** I moved it to y 160 (not 153.5, the old band line). At 153.5 it would sit 0.05 mm behind the back-row knob edges and read as a crack. At 160 it's a clean 6.5 mm behind them. Systems to confirm what that does to depth.
- **Wall:** keep the French cleat. A live edge on a wall is the point: it hangs like a small shelf with the tree side up.
- **Material:** printed cream PETG face; oiled walnut; the butterfly in a contrasting wood (wenge or bog oak). One accent stays red, on CUTOFF.
- **Risks:**
  - wood moves across the grain while PETG doesn't. The joint wants slotted screw holes, not glue (eng/maker);
  - every edge differs, so the jack drilling needs a jig keyed to the straight joint, not to the live edge.

### 3. CHAMBER → keep and push hardest: **"closed, it's an organ case; open, it's a console"** *(FOLD)*
Sketch: `t2-chamber-closed-facade.png`.
- **The façade moves to the outside of the lid.** On a real organ, the façade faces the listeners, not the player. On FOLD that face is the lid's back. **Closed, it's the top of the bar you carry.** **Standing at 120° in the park, it faces whoever is across from you.** Your friend on the bench (B-J11) gets the organ front; you get the console.
  - Systems put the pipe façade in the speaker grille. I'd leave the speaker where it is (facing you; it works) and make the façade the walnut lid back, engraved or inlaid. Nothing in it is a hole, so it adds no acoustic or water risk.
- **"Humanize something free of error":**
  - *Free of error:* the 25 pipe lengths are the instrument's own scale, ∝ 2^(−n/12), C to C. The façade is a true picture of what the keys play.
  - *Humanize:* arrange the pipes the way organ builders do, alternating outward from the tallest in the centre (a tower). Then add one small hand-cut name under the impost line.
  - Exact maths laid out by a human habit. That's this branch's whole voice.
- **Joy:** the pipes are a brass-tone inlay or engraved line fill on dark walnut, the most joyful thing on any of our concepts. It's decoration that *means* something (his keyboard's scale), so it isn't costume. The Model D's RANGE in feet (32' … 2') goes on the RANGE scales in the same serif. The heritage is real.
- **Reverse pegs:** dark walnut naturals, maple sharps (systems' idea). In the sketch the keyboard strip sparkles. Next to the dark façade it makes the object's two faces rhyme: dark with light lines outside, light with dark pegs inside. I'd push it further: **the naturals are the same walnut as the body**, so the keys look carved from the case.
  - Owner check (systems already flagged it): reversed colours vs sight-reading.
- **Brass is the case hardware:** stays (v1.1), hinge pins, the six back screws laid out as the façade's "impost" rivets, so they become part of the drawing instead of interrupting it.
- **Open for eng:**
  - pegs vs FOLD's closed height (+≈ 4 mm, or a pocket in the lid; systems);
  - engraved-and-filled brass lines on wood-fill PLA: do they read, or is this real-walnut-only? The first print can carry a printed relief; the inlay is the real-wood version.

### 4. PIERCED → **kill as a branch; its carry job moves into GROUND**
- Systems' own number decides it: **+55 mm of length** (≈ 331 × 180 on ONE SHEET) for a hole. The owner's main concern is cost, then portable. That's the wrong way on both, for one gesture.
- **"Disconnect from desire":** my desire was the disc of light on the grass, a lovely image. Once I set it aside, the job left is *carry it on a walk*, and that doesn't need a hole through the instrument.
- **"Shyness":** a shy object hides its handle. So the hand-hold goes **underneath, into GROUND's wedge**: a felt-lined finger pocket in the wedge's rear face, adding zero length.
- I tried a shy middle path first: a 22 × 90 felt-lined slot needing +32 mm, a bar of light instead of a disc. It still cost length and still read as "a cutting board with a handle". Dropped.
- **What survives:** felt-lined hand places (from HUSH), and "the instrument marks noon" as a possible GROUND detail if the director wants it. I don't push it.

### 5. GROUND → keep, given a voice: **"calm on top, loud underneath; the wedge is a horn"** *(either; drawn on ONE SHEET)*
Sketch: `t2-ground-horn-section.png`.

Systems said it plainly: GROUND is the strongest on park jobs and the weakest on personality. Two draws fix that.
- **"Listen to the quiet voice."** The quiet voice is the little speaker, which outdoors (no walls, B-J8) is the weakest part of the whole park story. So the wedge isn't a block; **it's a folded horn.**
  - The speaker fires down into a throat under the panel's rear. The path folds forward and back inside the wedge and opens at a mouth in the rear and side faces. The rear mouth also faces the friend across from you.
  - Like a marimba's resonator under its bar, or a gramophone's horn folded into its cabinet: the posture and the voice are one part.
  - **Honest:** a horn this small mostly helps the mids and directivity, not bass. Any gain is UNVERIFIED until eng models it or someone prints one. If it measures as nothing, the wedge is still the posture, and the branch survives as a posture.
- **"Exuberance."** It's an underside you show when you carry it: **persimmon TPU (or PETG) underneath, calm cream on top.** On the grass you see only the calm face. Walking with it under your arm, the world sees the loud one. Like a bird's wing lining, or a sneaker sole. "The bottom is as designed as the top" stops being a rule and becomes a joke you're in on.
- **Carry:** PIERCED's finger pocket, felt-lined, in the wedge's rear face. In the sketch the pocket and the horn mouth share that face (pocket left, mouth right). Systems to place both.
- **Number check:** 12° over 180 deep is ≈ 37 mm at the back, not systems' rough 15–25. 8° gives ≈ 25 mm. Which rake reads best seated cross-legged is a body test: print a cardboard wedge and sit on the grass.
- **Sun (B-J7):** type in GROUND goes high-contrast (ink on cream, no warm grey). The status light sits under a short hood (systems' idea). That hood is a recess, so it doesn't break "nothing raised".

### 6. NEW BRANCH — **RAIN: "a pond after rain"** *(ONE SHEET; a landscape, which differs in kind from furniture, case, tool and posture)*
Sketch: `t2-rain-top.png`. That's the real round-5 layout; the ripple field is computed, not hand-drawn.
- **Point of view: every control is a drop on still water. Its rings spread until they meet the next drop's, and the lines where they meet draw the panel's map.**
  - v1.1 ONE SHEET stopped each ring field at r 9.25. **RAIN lets them run.** Where two fields meet they leave a fine smooth seam (a Voronoi line).
  - Those seams appear by themselves around every row and column; the sketch shows they already read as sections. The grooves can go.
  - It honours his rule exactly: still two finishes, smooth and rings. It just does more of the thing he said he loves.
- **"Don't be afraid of things because they're easy to do":** the method is the v1.1 rings with no outer radius. No new process, no new part. The easy move is the right one.
- **Bridget Riley:** the vibration comes from line, not colour. Op-art fields shimmer as your eye moves. **Under a tree in dappled light**, moving leaf shadows over ring sheen on smooth-PEI first layers should do the same. Calm, but alive. UNVERIFIED until the coupon is printed (the coupon ONE SHEET already needed).
- **His pegs, made part of the idea:** the 25 keys become **stepping stones**, grey pegs (HUSH's bought button plugs and arm, on ONE SHEET's mechanism), with ripples round them too. The rule becomes the most natural one in the set: *everything that breaks the surface ripples.*
- **Mustard (the drawn accent):** CUTOFF in mustard, one fallen ginkgo leaf on the pond. Everything else is pale wet-slate stone (#dddacd drawn) and cream knobs. Two colours plus the leaf.
- **Legends:** each sits on a small smooth "lily pad" (a cut-out in the ring field), so type never sits on lines. Same swap as v1.1.
- **Costs and risks, named plainly:**
  1. **Making the rings:** a slicer's concentric pattern follows a region's *outline*, so a Voronoi cell would get polygon rings, not circles. The rings have to be modelled as geometry (grooves ≥ 0.9 mm pitch, in the first 0.4 mm, face down) in OpenSCAD. That's easy, but the pitch is coarser than v1.1's 0.45 first-layer lines.
  2. **Pegs on ONE SHEET:** HUSH's 18 mm peg pitch puts the last white peg's head 0.65 mm from ONE SHEET's 276 edge. It needs ≈ +8 mm of width or a tighter pitch (systems). Pegs stand ≈ 6.5 proud, not "within 3" (systems' R4 note).
  3. **Busy?** The sketch is calm at arm's length and lively up close. A director call from a proper render.

### 7. The FREE / SYNC toggle, every branch (owner: "B")
**Where it fits (my scratch check, same margins as `fold_r5_check.py`, FOLD-105; labels not yet checked by systems):**
- **Not beside TIME in the back row.** TIME's knob edge is already only 7.05 from the centre break (rule ≥ 7). The gap to ECHO TYPE is 5.1, and a toggle needs ≈ 10.7.
- **Not behind TIME.** It fits by margins at x ≈ 119–122, d ≈ 93–96, but that's where the ECHO heading and the type-name fan live. Rejected.
- **In front of TIME: fits.**
  - FOLD x ≈ 133, d ≈ 71 (≈ 12.9 in front of TIME's centre, slightly inboard);
  - ONE SHEET x ≈ 128, y ≈ 133 (shown in RAIN's sketch).
  - Back-row legends live *above* their knobs under the section headings (S1 pass), so nothing of TIME's is printed there.
  - The front of a pot's 300° sweep is its dead zone, so **the toggle sits in TIME's dead zone**: the knob's scales arc over it, and the switch sits at its foot. Systems: please run it through the checker with labels.

**How it reads (all branches):**
- **The toggle throws fore and aft:** toward the player = **free**, toward TIME = **sync**. The lever points at the scale you're reading.
- **TIME carries two scales.** Inner ring = ms (free), short ticks, ends labelled "20 ms" and "2 s". Outer ring = divisions (sync), as 9 marks.
  - Only 1/16, 1/8, 1/4, 1/2 are written. Dotted values are a dot beside the mark; triplets are a small triangle.
  - That keeps the type ≥ 1.05 mm and the scale scannable in one glance. Legend words: "free" / "sync", in each branch's own type.
- **Mirror:** systems asked for a partner or a reason. **The reason:** echo is the only effect in the chain that cares about time, so it's the only one with a clock switch. The asymmetry is the information. I'd add no dummy partner in front of DECAY.
- **Per branch:**
  - RAIN: it's one more stone, so it ripples;
  - CHAMBER: words in the serif; the lever can be one of FOLD's black toggles, one element of each kind (no special brass lever);
  - BUTTERFLY: v1.1 ONE SHEET style;
  - GROUND: the high-contrast sun scale.
- **The d6 draw (jack wall), tested:** it fails B-J13 ("see which it's in"). From the seat you can't see ONE SHEET's rear wall, or FOLD's lid far wall at 120°. One thing survives from it: the switch's legend can state its cause, e.g. a small "clock / tap" under "sync", because the clock comes in at the jack wall.

### 8. Where the branches now stand (my view; the director decides)
| Branch | Seed | Kind | Point of view in one line | Emotion | Owner's sources it draws on |
|---|---|---|---|---|---|
| BUTTERFLY | ONE SHEET | furniture | from tool to tree, front to back | longing | Nakashima's honest joint; real wood |
| CHAMBER | FOLD | instrument case | closed an organ case, open a console | joy | pipe organ; case furniture; brass hardware |
| GROUND | either | posture + voice | calm on top, loud underneath; the wedge is a horn | exuberance | instrument resonators; tool (carry pocket) |
| RAIN | ONE SHEET | landscape | every control a drop; ripples draw the map | calm | Riley; Zen-garden raking; his love of rings + pegs |
| ~~PIERCED~~ | — | — | killed: +55 mm for a gesture; carry moved into GROUND | — | — |

Both concepts he leans to are covered: ONE SHEET ×2 (+ GROUND), FOLD ×1 (+ GROUND).

**Held in reserve:** **TRAY**, a neck strap from the two rear corners, played standing under a tree like a vendor's tray (binoculars + stretcher draws). Different in kind (worn), but it asks for a posture he never mentioned. One line here in case he plays standing.

### Open questions
1. **Owner:** CHAMBER's reversed key colours (systems' question, still open).
2. **Owner (RAIN, BUTTERFLY, CHAMBER):** pegs on ONE SHEET need ≈ +8 mm of width; pegs on FOLD need closed height. Worth it for the pegs he loves?
3. **Eng:** horn gain in a ≈ 25–37 mm wedge; wood/PETG joint movement (BUTTERFLY); engraved fill on wood-fill PLA (CHAMBER); ring grooves at ≥ 0.9 pitch face down (RAIN).
4. **Systems:** run the SYNC toggle at FOLD (133, d 71) / ONE SHEET (128, 133) through the checkers with labels; BUTTERFLY's joint at y 160 vs depth; GROUND's rake (8° or 12°) and where the horn mouth and pocket sit.
5. **Maker:** the ring coupon (smooth + rings) now also decides RAIN, ideally viewed under a tree.

NEXT: design director — four live branches (one reshaped, one pushed, one given a voice, one new) and one kill need steering before systems and I build them into concepts; the SYNC placement needs systems' label check, which can run in parallel.
