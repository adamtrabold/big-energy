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
