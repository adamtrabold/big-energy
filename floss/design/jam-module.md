# floss jam: the module (rev 2 shape)

Concept phase restart, 2026-11-22. floss is now a keyless sound module played by a carried travel keyboard over USB-C. Read `BRIEF-CONTEXT.md` (the REV 2 section), `jobs.md` (rev 2) and `../eng/module.md` first. The old `jam.md` and the round-1 `concepts/` are history: mine them, don't obey them. Each turn adds below. Don't rewrite earlier turns; argue with them.

Marks: **PROPOSAL** = systems design, not approved · **[eng]** = from `eng/module.md` · **[calc]** = my arithmetic · **UNVERIFIED** = a fact nobody has checked yet.

---

## Turn 1: product designer (systems focus)

### Real randomness (drawn with Python `secrets`, not picked)
- **Oblique Strategies:** "Look at the order in which you do things" (43 of 50). Second card: "Only one element of each kind" (4 of 50).
- **Unrelated field:** bookbinding (16 of 30). **It came up on both draws.** I kept it and drew a third from the other 29: tea ceremony utensil kits (10 of 29).
- **Twist:** "it is mostly used at night" (2 of 12).
- **Constraint:** "the cable is the handle" (10 of 10).
- **Proportion:** **3 : 1** (drawn from 1, 1.272, √2, 1.5, φ, 2, 2.5, 3).

Below, a tag such as [order], [one of each], [book], [tea], [night], [cable], [3:1] shows where a draw shaped an idea.

### 0. What's different now, in one paragraph
The keyboard is no longer floss. It belongs to someone else's design, it changes from week to week, and it may be absent. So floss stops being "a keyboard with a sound" and becomes **a mind with a sound that borrows hands**. Three things follow, and they drive everything below:
1. **The panel can face anywhere.** With no keys under it, it doesn't have to be a flat strip above a keyboard. It can be flat, standing, or folded into a book. That's the biggest new design freedom.
2. **The join between module and keyboard is now a product.** The cable, the carry and how the two sit together are designed things, and they're what job 28 makes a family standard.
3. **floss must be useful with any keyboard, a poor one, or none.** Every behaviour needs a "what if the keyboard can't" answer.

### 1. Challenging `jobs.md` rev 2
It holds up. The 28 jobs cover the new shape, and I'm not rewriting them. What I'd change at the next revision:

| # | Change | Why |
|---|---|---|
| 2 | Say **USB-C** host port, not "host socket" | Owner 12:52: "Let's do USB c". `eng/module.md` §3 still says USB-A, so eng needs a revision too (a USB-C source needs CC pull-ups [eng]). |
| 3, 28 | Add: **the carry still works with no keyboard in it** (module alone, nothing loose or rattling) | The keyboard may be borrowed, broken or left at home (job 27). A carry that only works full fails then. |
| 3 | Add: the chunky minis (Launchkey, MPK) **play but aren't carried**, unless the owner picks "all" on eng trade-off 2 | Otherwise job 3 quietly promises a 49 mm-thick pocket. |
| 6 | Add: **keyboards differ in which note their lowest key sends at the default octave** | A split fixed at note 60 sits in the middle of one 25-key board and off to the side of another. UNVERIFIED per model: eng to list each slim keyboard's default lowest note. |
| 23 | Name the **cable-length conflict**: short for a tidy solo kit, long so a friend can hold the keyboard | The flows below hit it straight away. |
| new 29 | **Find out why there's no sound from floss itself:** no keyboard, keyboard unpowered, notes not arriving, volume down, a half muted. (inferred) | With two objects and a cable, "why is it silent?" is the most common failure, and there's no screen to say so. |

Nothing to drop.

### 2. Structure of the system
Five parts. Only the first is floss. The other four are the **family standard** (job 28).

```
 [keyboard] ──cable──► [host port] ─► floss module ─► speaker / phones / line
      │                     ▲               ▲
      └──── carry ──────────┴── attachment ─┘
```

**2.1 The module (floss).** Engine, panel, battery, speaker, ports. Size is set by its parts [eng: ≈ 250–290 × 90–110 × 31–33 mm minimum] and by the kit direction (§5). It must work alone: it plays from a computer over USB-C, from TRS MIDI, or from nothing (HOLD survives an unplug, §4.6).

**2.2 The keyboard.** Any class-compliant USB-MIDI keyboard. Carried: the slim class [eng: 325–388 × 83–135 × 11–16 mm, 0.24–0.6 kg]. Played: anything floss can power at ≈ 500 mA, including a full-size keyboard at home. floss reads whatever the keyboard sends and asks nothing else of it.

**2.3 The cable.** The keyboard's own socket varies (USB-C, micro-B, mini-B; UNVERIFIED per model). So the cable belongs to the keyboard, not to floss, and travels with the keyboard. PROPOSAL for the family cable: right-angle USB-C at the module end, the keyboard's own plug at the other, **coiled, about 0.3 m relaxed and 1 m stretched**. Short when you play alone, long enough to hand the keyboard to a friend (job 23).

**2.4 The carry.** How module, keyboard and cable travel as one kit. It must take the whole slim range with no recess cut to one outline, and hold the module alone without rattling. The directions in §5 differ mainly here.

**2.5 The family standard (job 28): fix the interfaces, not the sizes.**
The obvious standard is a fixed box size that every module fits, like shipping containers. I think that's wrong. Big Energy, port-a-poly and floss will be different sizes, and a fixed box forces the leftover space the director keeps catching ("the body's leftovers are driving the layout"). The better model is **the camera tripod thread**: one small fixed interface, and any body behind it. PROPOSAL, seven parts:

| | Standard | Value (PROPOSAL unless marked) |
|---|---|---|
| S1 | Keyboard envelope the carry must take | ≤ 392 × 139 × 18 mm, ≤ 0.6 kg [eng] |
| S2 | Host port | USB-C, source role, 5 V current-limited at ≈ 550–600 mA [eng]; **on the edge that faces the keyboard, never the rear wall** |
| S3 | Cable | §2.3, owned by the keyboard |
| S4 | Attachment | **two ¼"-20 brass threaded inserts in every module's underside, at one family spacing** (spacing to be set: it must fit the smallest module). Every carry part attaches here. As a bonus, any module mounts on a camera tripod, or a mic stand through a common adapter (night gigs, home desk). |
| S5 | Plug behaviour | any order works (§3.1); unplugging releases notes on their tails; held notes survive an unplug; the port light (§4.2); the keyboard is powered only while the module is on |
| S6 | Family MIDI map | the same CC numbers mean the same musical thing on every module, so a keyboard set up once works on all of them: CC64 hold, CC1 = the lean fallback (§4.3), CC74 tone, CC11 expression, pitch bend ±2 semitones by default. A starting list; MIDI never flips switches (Big Energy rule) |
| S7 | Split rule | one rule for every module that splits (§4.1) |

Why the host port goes on the keyboard-facing edge: the cable then runs a few centimetres between the two objects, never across the hands, the speaker or the panel. The rear wall keeps charging, phones, line, TRS, TUNE, MIDI SPLIT and power: things you set once.

### 3. Flows
#### 3.1 Unpack and play (jobs 1, 2, 19, 20) [order]
"Look at the order in which you do things." I listed every order a person could do it in: power first or plug first, keyboard first or module first, volume up or down. **Rule: every order works and none needs undoing.** Then each direction in §5 gets to choose the order it *invites*, as a ritual. That's where the tea kit comes in: a chabako (tea box) unpacks in a fixed, calm order, and every utensil has one place.
1. Open the carry (direction-specific).
2. Set the module behind the keyboard, centred (§4.1 explains why centred matters).
3. Plug the keyboard's cable into the host port. Order doesn't matter: if floss is off, nothing happens until it's on.
4. Switch on. The status light comes on steady; the port light comes on when the keyboard answers (§4.2).
5. Play. Under 30 seconds from closed (PROPOSAL target).
- **States:**
  - floss on, no keyboard → silent; port light off; plays from USB-C or TRS;
  - keyboard draws too much → floss cuts its power, the port light flashes, floss keeps running; it retries a few times, then waits for a re-plug (retry policy: eng);
  - unplug mid-chord → the notes fade on their tails; held notes keep sounding;
  - keyboard plugged in but sends nothing (a dead one, or a charge-only cable) → port light steady but never blinks on a key press. That's the diagnosis for job 29.

#### 3.2 Keyboard missing (jobs 1, 16, 27, new 29)
Forgotten, broken, or a friend has it.
1. The carry still closes around the module alone (job 3 change).
2. **Play from elsewhere:**
   - a computer over USB-C (floss as a USB-MIDI device);
   - a phone with a MIDI keyboard app over USB-C (UNVERIFIED: phone host support and floss's device port need checking);
   - any keyboard with TRS or DIN out, through TRS in.
3. **Play from nothing:** a chord held with HOLD before the keyboard left keeps sounding. Turn the knobs while it drones (§4.6).
4. **Borrow a keyboard:** any class-compliant one works. It doesn't have to fit the carry to play.

#### 3.3 Swapping keyboards (jobs 6, 8, 9, 10, 27)
1. Unplug the old one. Its held notes keep sounding; unheld ones fade.
2. Plug the new one in. The port light comes on.
3. floss reads what the new one sends. Pressure, tilt and release speed start working if it has them. If it doesn't, the lean falls back (§4.3). **Nothing on the panel changes, and nothing has to be set.**
4. The split: if the new keyboard's lowest key sends a different note, the split lands somewhere else on its keys. The S7 rule (§4.1) decides what happens.
5. Carry: the new keyboard goes into the same carry, because the carry takes the range.

#### 3.4 A friend plays (job 23)
1. Hand over the keyboard. The coiled cable stretches to about 1 m (PROPOSAL), so the friend can sit beside you on a bench.
2. You keep the module on your lap or the bench, facing you: OCTAVE, PRESSURE, SHIMMER, the room.
3. **Plant and tend** (TIDE's idea, now with two people): the friend plants notes with HOLD on; you shape them.
4. **Two keyboards:** the second goes into TRS in (it needs a TRS or DIN out). With MIDI SPLIT on, channel 1 plays the left voice and channel 2 the right, so each player owns a half. One USB keyboard is the limit (no hub [eng]).
- **Tension:** per-half controls sit "over their half" only when the module is centred behind the keyboard. Once the friend takes the keyboard away, OCTAVE L and R still read left and right, but they no longer sit above the hands. That's acceptable; say so.

#### 3.5 Home (jobs 16, 17, 19)
1. floss on the desk, on wall power through USB-C (it plays while charging [eng]).
2. A full-size keyboard into the host port if it draws ≤ 500 mA (most bus-powered ones should; UNVERIFIED per model). Otherwise into TRS in.
3. Line out to monitors; phones mute the speaker.
4. A computer over USB-C, if host and device work together (UNVERIFIED [eng]). Fallback: TRS to the computer's interface.
5. Optional: floss on a stand or tripod through the S4 inserts, beside the keyboard.
- On a 49- or 61-key keyboard, note 60 is near the middle (if the default puts C4 at middle C; UNVERIFIED per model), so the fixed split behaves like a classic split keyboard.

### 4. What lives on the module panel now
**Principle: the panel holds what turns notes into floss, and nothing the keyboard already has.** No pitch wheel, mod wheel, octave buttons or transport. [one of each] "Only one element of each kind" becomes a test for every control: if a keyboard already has one of these, floss doesn't get a second.

The round-1 panel survives almost whole: OCTAVE L, OCTAVE R; the TOUCH group (ATTACK, RELEASE, the PRESSURE selector); registers or TONE (depending on the voice character, §6); SHIMMER mode and DEPTH; ECHO, TIME, FREE / SYNC, TAP; REVERB; VOLUME; HOLD; the status light. Signal order stays TOUCH → registers → TONE → SHIMMER → ECHO → REVERB → VOLUME (the owner's synth → fx → output rule; round-1 BOW fix 1 applies: ensemble after the voice). What's new or changed:

**4.1 The split (jobs 5, 6, 18; standard S7).** Two OCTAVE knobs, equal = one keyboard, as before. The question is how the split stays in the right place on any keyboard. Three rules, which differ in kind:
- **A. Fixed note.** The split is at B3 | C4 (note 59 | 60). The keyboard's own octave buttons move it on the keys. Printed on the module: keep the keyboard at its home octave. Honest, simple and readable. It's the minimum. **My pick for the standard.**
- **B. Learned per keyboard.** Hold HOLD and press a key: the split moves to that key, and floss remembers it for that keyboard by its USB ID. Smart, but the split becomes invisible state, which breaks "read everything from the panel" (job 18) unless something shows it.
- **C. The ribbon** [book]. A bookbinding ribbon marker, anchored to the module's front edge, laid across the keyboard between the two split keys. It's a physical record of the split on *any* keyboard, by eye and by touch, at night too. It works with A (laid once at B | C) or makes B readable.
  - **PROPOSAL: A + C.** The rule is fixed; the ribbon shows where it lands on today's keyboard. B goes to the director as an option if the owner wants keyboards that start somewhere else.
- **Spatial rule:** per-half controls read as "over their half" only with the module centred behind the keyboard. So the directions that keep the pair in that relation (§5) score better on job 18.

**4.2 Port light (jobs 18, new 29).** A small second light next to the host port:
- off = nothing connected;
- steady = keyboard connected and powered;
- **a short blink on every note received** = notes are arriving (the "why is it silent?" answer);
- fast flash = power fault.

The status light keeps its three round-1 meanings (fine, charging, low battery). "One element of each kind" argues for a single light. I'd keep two because they answer different questions and sit in different places; the director can rule.

**4.3 The lean falls back (jobs 8, 9).** The PRESSURE selector chooses what a lean does (swell, vibrato, tone, shimmer, or TIDE's drift). What drives it depends on the keyboard:
- poly aftertouch or MPE → per note;
- channel pressure → every note;
- otherwise **CC1** (the mod wheel, strip or button most travel keyboards have; S6) → every note;
- otherwise nothing; velocity still does its job.

floss notices which source the keyboard sends and uses the best one. The panel doesn't change. Velocity-only players get the selector back through their mod control, which answers job 9 properly instead of "nothing breaks".

**4.4 Tilt and bend (job 10).** Pitch bend is ±2 semitones by default (S6); MPE bend is per note. Release velocity sets the tail where the keyboard sends it; otherwise RELEASE's knob does. No control for any of this. A keyboard's extras are bonuses, never requirements.

**4.5 Keyboard knobs.** A keyboard with knobs (some have them) can move floss's settings through the S6 map, with Big Energy's jump-on-move rule: the panel knob takes over the moment it's turned.

**4.6 HOLD survives the keyboard.** Held notes don't depend on the keyboard being there. Unplug, swap, or hand it over and the drone stays. That's the "play from nothing" case in §3.2. It's also where floss is most itself without hands: a held chord that you tend.

**4.7 Night** [night]. "It is mostly used at night" was the twist. Every control must read by touch (round 1's eyes-closed rule stays), the lights must be dim, not glaring, and one direction (§5.3) goes further.

### 5. Creative directions for the pair and its proportions
I threw away the first idea: a slab case with a keyboard-shaped recess, which is any AI's answer and is also ruled out (no fitted dock). The four below differ in **what kind of thing the kit is**: one hinged object, a soft wrap around two objects, a standing lit object, and a worn strap. Each says how it meets the standard (S1–S7). **3 : 1** [3:1] runs through them as a proportion to test, not a rule.

**3:1 sizes, for reference** [calc]:
- 270 × 90 mm: exactly inside eng's minimum footprint (250–290 × 90–110). The smallest honest module.
- 390 × 130 mm: the largest slim keyboard's footprint (Xkey 25 is 388 × 135 [eng]). A module this size matches the keyboard. The spare area can go to a bigger sealed speaker box (≈ 150 × 110 × 20 mm ≈ 330 cm³, the top of eng's ≥ 150–300 cm³ range), which is a sound reason, not leftover space.

#### 5.1 SPINE: the kit is a book [book] [cable] [order]
- **What it is:** two boards joined by a cloth spine.
  - Back board = **the module**, 390 × 130 mm (3:1).
  - Front board = **a keyboard board**, ≈ 395 × 140 × 3 mm, with four sliding elastic corners (like photo corners) that hold any slim keyboard.
  - Spine = bookcloth over a flexible core, about 55 mm wide.
- **The cloth spine folds both ways**, as a real book's hinge does, which gives three states:
  - **open flat (180°):** keys in front, panel behind, centred. One instrument, 395 × ≈ 275 mm: lap- and bench-sized (job 20);
  - **standing (≈ 110°):** the module stands behind the keys like a lectern, panel facing you; for a table at night;
  - **closed:** face to face. The 55 mm spine leaves ≈ 2 mm between the knob tops and a 16 mm keyboard [calc: module 33 + keyboard 16 + board 3 + 2 air ≈ 54]. Panel and keys are protected inside; flat boards outside.
- **The cable lives in the spine** [cable]: a short USB-C lead runs through a channel in the spine from the host port to the keyboard's end. The spine is also where you hold it: **the cable is in the handle.**
- **Order** [order]: opening the book is the first act, so opening could switch it on (BOW's lid = power, rescued with a real reason). Risk: the module also has to work without the board (home, a big keyboard), so it needs its own switch as well. That's two ways to turn it on; the director may prefer one.
- **Standard:** the spine fixes to the module's S4 inserts, so Big Energy gets the same keyboard board on its own module.
- **Strong:** jobs 3, 18 (the pair always sits centred), 20, 24 (it reads as one object even though the keyboard isn't ours).
- **Weak:**
  - misses T4 (≥ 390 mm wide; eng says any one-package carry does);
  - weight: a bigger module plus the Xkey is at T5's edge [eng: 0.87–1.51 kg];
  - a keyboard with its socket on the back edge needs the cable to bend round the spine (UNVERIFIED socket positions);
  - wear on the cloth hinge.

#### 5.2 CLOTH: the kit is a wrapped tea set [tea] [order]
- **What it is:** two loose objects and a cloth.
  - Module small: **270 × 90 mm** (3:1, the minimum), meets T4.
  - The family part is **a quilted furoshiki**, ≈ 80 cm square (PROPOSAL; furoshiki are traditional Japanese square wrapping cloths). A sewn sleeve at one corner holds the module, and a sewn pocket holds the cable. The rest of the cloth wraps any keyboard, **the chunky minis included**: the only direction that carries the whole range, not just the slim class (eng trade-off 2).
- **The unpack is a ritual, in a fixed order, like a tea box:**
  1. untie the knot;
  2. spread the cloth: it's the playing mat, non-slip on a lap or a bench, with a woven layout showing where the module goes (behind) and the keyboard (in front), and a woven centre line where the split usually lands;
  3. cable from its pocket;
  4. plug in, switch on.
  - Repack in reverse. Nothing has a wrong place.
- **Night:** reflective thread at the cloth's edge and on the centre line.
- **Standard:** the cloth is the family part. It fits any module that fits its sleeve (the sleeve's size is a family number), and the S4 inserts can take a stiff base plate if a module needs one.
- **Strong:** jobs 3 (any keyboard, any size), 27, 28 (the most flexible), T4, cost.
- **Weak:**
  - impact protection: a cloth doesn't stop a knob snapping in a bag, so the module must guard its own knobs (raised rails, or knobs below a rim);
  - dirt and damp: the cloth must be washable, with the module sleeve removable (the felt lesson from round-1 TIDE);
  - two loose objects on a lap.

#### 5.3 LAMP: the module stands and lights the keys [night] [3:1]
- **What it is:** a standing module.
  - Its cross-section is a wedge: front face sloped toward the player, carrying the panel; 270 mm wide × ≈ 90 mm tall (3:1 face). The board stands inside the wedge; the speaker fires forward.
  - Its front foot is a lip the keyboard's back edge tucks under, which works for any keyboard depth.
- **It's a lamp** [night]: a warm, dim LED strip under the wedge's top edge throws light down across the keyboard.
  - **The light shows the split:** two zones meeting at the module's centre. With the keyboard centred, that's where the split usually lands. When OCTAVE L ≠ OCTAVE R, the two zones differ in warmth.
  - So the state shows *on the borrowed keyboard itself*: floss makes whatever keyboard you bring look like floss's (job 24).
  - Power: tens of milliwatts (PROPOSAL; eng to confirm against T2).
- **Carry:** the wedge lies on its back on top of the keyboard, joined by a family strap through the S4 inserts. This is the weakest part: the visual designer should push it.
- **Strong:** jobs 18 (the split is shown on the keys), 24, table use and night.
- **Weak:**
  - job 20 on a lap: a standing wedge has nowhere to stand on thighs;
  - the light can't know where middle C physically is on a given keyboard; it's right only when the keyboard is centred and its default octave puts C4 at the middle;
  - sun makes the lamp pointless (it's a night object, honestly).

#### 5.4 TETHER: the kit is a strap [cable] [order]
- **What it is:** **the cable is the handle**, taken literally.
  - The family part is a strap, like a camera strap.
  - One end anchors to the module's S4 inserts. The keyboard cable runs **inside** the strap, emerging as two short slack pigtails: one into the host port, one into the keyboard. The strap's anchors take all the load, the plugs none.
  - The keyboard end has a cinch that loops round any keyboard, including the chunky ones.
  - The cable slides out of the strap's channel, so a worn cable is a cheap swap.
- **Carry:** crossbody, module at the hip, keyboard cinched against it. Or a bag, with the strap wound round both.
- **Play:** uncinch. The keyboard stays joined by up to ≈ 1 m of strap (USB 2.0 allows far more [general USB spec]), so a friend can hold it, or you can stand with the keyboard on your forearm and floss at your hip. **This is the only direction you can play walking.**
- **You can't forget the cable,** because it's the strap.
- **Standard:** strap plus inserts. The module can be any size; it's the most minimal standard.
- **Strong:** jobs 2, 23 (built for two people), 27, 28; a new way to play (standing, moving).
- **Weak:**
  - job 3's "without damage": nothing covers the knobs or the keys, so each object needs its own cover, and then it starts becoming CLOTH;
  - job 18's spatial mapping is lost (the halves aren't under the knobs);
  - a strap with a cable inside is a custom-made part (sewing, routing), which matters for job 26.

#### Inverted, and why I'd kill it: BACKBONE
"The keyboard carries the module": a 390 × 65 mm bar clamps to the keyboard's rear edge with a capo-like jaw, making one rigid instrument. Same area as eng's minimum footprint, ratio 6:1. **Proposed kill:**
- it's SPINE's open state without the closed one, so there's no protection;
- a jaw has to grip unknown edges (11–49 mm thick), which comes close to a fitted dock;
- it risks the owner's keyboard.

### 6. What carries over from round 1, and the question for the director
Kept for every direction (they don't depend on keys):
- engine D's 25 allocated voices [eng];
- the breath;
- the octave knobs as the split, with a held note keeping its pitch;
- the PRESSURE selector;
- HOLD;
- FREE / SYNC with TAP;
- the TUNE trim and MIDI SPLIT on the rear;
- signal order;
- per-half controls over their half;
- the honest "analog voices" sentence (reworded: "one tone per voice" instead of "per key").

Dropped: everything about physical keys (lift timing on the spring, collars, pegs, key colours, the gutter over middle C). BOW's per-note thinning in swell runs **only when per-note pressure is arriving**; with any other source it's off, or it would sink every note (rule, PROPOSAL).

**The new jam has two axes, and the round-1 jam didn't:**
1. **the kit** (what the pair is: SPINE, CLOTH, LAMP, TETHER);
2. **the voice's life** (BOW = life in the finger: strands, velocity as speed; TIDE = life in time: drift, add-and-pull HOLD).

They're independent: either voice can live in any kit. **Proposal for the director:** let concepts differ on the kit (that's what's new and what job 28 asks for), and pair each with the voice that suits it, rather than crossing every combination. My pairings:
- SPINE + BOW (one instrument, a bow stroke per finger);
- CLOTH + TIDE (ritual, slow, planted);
- LAMP + TIDE or a quieter BOW (night);
- TETHER + BOW (played moving, every touch counts).

### 7. Open questions
1. **Eng:**
   - revise §3 for the USB-C host port;
   - each slim keyboard's default lowest note (for the S7 split);
   - its socket position and type (for the cable path);
   - a full-size keyboard's draw at 500 mA;
   - phone-as-host over floss's USB-C;
   - the over-current retry policy;
   - lamp power against T2;
   - SPINE's mass on a lap.
2. **Director:**
   - which kits go forward (and the kill on BACKBONE);
   - the two-axes proposal;
   - one light or two;
   - split rule A + ribbon vs B;
   - SPINE's open = on.
3. **Owner (later):**
   - the slim class only, or all (CLOTH changes this answer);
   - one package (SPINE) or two (CLOTH, LAMP, TETHER), which is eng trade-off 3;
   - the job 29 addition.

NEXT: product designer (visual focus) — four kits that differ in kind (book, wrapped cloth, standing lamp, strap) are on the table with numbers. Their proportions, faces and the weak carry in LAMP are form questions first, and the director should steer once both designers have pushed.

---

## Turn 2: product designer (visual focus)

Sketches (rough 2-D, to scale, opened and checked):
- `sketches/visual-module-jam2a-fallboard.png`: FALLBOARD in plan with an Xkey 25 and a nanoKEY2, and side sections in three states.
- `sketches/visual-module-jam2b-proportions-shelf.png`: three module proportions behind the keyboard envelope, the family on a shelf, and the kit verdicts.
- Source: `sketches/visual_module_jam2a.py`, `visual_module_jam2b.py` (matplotlib).

### Real randomness (Python `secrets`, not picked)
- **Oblique Strategies:** "Abandon normal instruments", then "Remove specifics and convert to ambiguities".
- **Unrelated fields:** harmonica in its case; surveying instruments (theodolite, rod and target, the surveyor's box).
- **Twist:** "it lives on a shelf as an object between uses".
- **Proportion:** **3** again, from a list of ten, and drawn independently of systems' 3 : 1. I kept it where the parts agree (SLAB) and broke it where they don't (RAIL, 5 : 1), and I say so each time.

Tags: [abandon], [ambiguity], [harmonica], [survey], [shelf], [3].

### 1. How floss looks when the keyboard is someone else's product
The keyboard is silver, black or white plastic, with someone else's logo, buttons and LEDs, and it changes from week to week. Trying to match it is hopeless; hiding it would also hide its octave buttons and mod strip. So these are the rules I'd hold every kit to:

1. **Own the outline, host the keys** [harmonica]. The kit's outer edge is always floss's: walnut rail, tray lip and cover. The keyboard sits *inside* it, as a guest, the way a harmonica lies in its case or a theodolite in its box. A picture frame is the same idea: different pictures, the same frame.
2. **Width is ours.** The module is at least as wide as every slim keyboard: **400 mm ≥ 325–388** [eng]. The guest never sticks out past floss. This is the one size the keyboard sets for us, and it's a real reason, not leftover space.
3. **A dark bed** [ambiguity]. The keyboard lies on near-black brown coated bookcloth (wipeable, the library-binding kind; product UNVERIFIED). A black keyboard's edge vanishes into it. A white or silver one floats on it like ivory on felt. Either way, the keyboard's specifics (its edge, its colour, its logo) fade, and what reads from two metres away is floss with a field of keys.
4. **Don't hide their controls; do hide their logo when packed.** Every kit closes over the keyboard, so the packed object is only floss.
5. **floss's marks go only on floss**: the brass split target, the wordmark on the rail end, the spine label. Nothing is stuck onto the guest.
6. **Materials, not colour-matching.** Walnut, cream and brass sit beside any plastic, the way a wooden case holds any metal instrument. This keeps the round-1 family palette (CATHEDRAL, BOW) with no new colour. Coral still marks where the life lives (PRESSURE).

### 2. The family standard: add one size to "fix the connections"
Systems' tripod-thread principle (S1–S7) is right that a fixed box is wrong. But fixing *no* size means the keyboard bed, the hinge and the cover get redesigned for every instrument. [shelf] "It lives on a shelf between uses" gave me the sharper version: **books on a shelf share a height and differ in thickness.**

- **PROPOSAL S8: every module is 400 wide** (the S1 keyboard envelope, 392, plus a 4 mm lip each side). Depth and thickness come from each instrument's own parts.
- So the keyboard bed, the cover hinge, the split-target rail and the cable gutter are **the same part on floss, Big Energy and port-a-poly.** Only the module (and in FALLBOARD the lid, see the weak points) changes.
- **Every rigid kit closes to an object 400 tall when stood on end, spine out**: brass corners (the surveyor's box), a cream spine label, one accent colour per instrument (floss coral, Big Energy brass, port-a-poly black: illustrative). The family is a row of books on the shelf (sheet b). This is also job 24 answered between uses: the kit is a handsome object when nobody's playing it.
- This answers the director's standing objection ("the body's leftovers are driving the layout"): the width comes from the keyboard, and the depth from the parts.

### 3. Proportions, against the keyboard (sheet b, A)
Three module shapes, each drawn behind the slim envelope:

| | Size | Ratio | Panel | Fits |
|---|---|---|---|---|
| **SLAB** | 400 × 133 | 3 : 1 [3] | two rows; spare area → speaker box ≈ 330 cm³ (systems' calc) | SPINE (boards the same size) |
| **RAIL** | 400 × 80 | 5 : 1 | **one row** of up to 14 at 25.5 pitch, or 16 at 22; grille strip behind | FALLBOARD |
| **BLOCK** | 270 × 100 | 2.7 : 1 | two rows | CLOTH; meets T4; the guest sticks out both sides |

**RAIL is the new idea** [abandon] [harmonica]. "Abandon normal instruments" means stop drawing a synth (a box with a grid of knobs). A harmonica is a bar with one numbered row of holes. So RAIL is **one line of controls parallel to the keys**: OCTAVE L at the left end over the left hand, OCTAVE R at the right end, and between them the voice and the room in signal order: attack, release, PRESSURE (coral), tone, shimmer, depth, echo, time, TAP, reverb, volume, HOLD.
- **It reads by counting from either end, eyes closed.** That's round 1's touch rule and systems' "night" twist.
- **It still reads when a friend takes the keyboard away** (systems' §3.4 tension): a line still runs left to right; it never depended on sitting over the hands.
- **Fit** [calc, eng to check]:
  - eng's board is ≈ 200 × 80 double-sided (16,000 mm²) [eng] → the same area as ≈ 260 × 62, inside a 400 × 80 rail;
  - speaker box ≈ 120 × 62 × 22 ≈ 164 cm³, at the low end of eng's ≥ 150–300;
  - battery under the board.
  - It's tight. If it fails, RAIL goes to ≈ 400 × 95.
- **It pairs with the voice axis:** TIDE's leaner panel (director round 1: ≤ 13 controls) fits one row comfortably. BOW's strand tabs don't fit; they push toward SLAB. That's one more reason for systems' pairings, but it flips one: **FALLBOARD + TIDE, SPINE + BOW.**

### 4. New kit: FALLBOARD, the piano form (sheet a) [abandon] [survey] [shelf]
I threw away my first idea, a hard shell clamshell like a harmonica case, because it's SPINE in plastic. The second, a sleeve, is CLOTH. The idea that differs in kind is: **don't stack the two objects, lay them in one plane with one lid over both**, the way a piano puts the keys in front, the works behind and a fallboard over the keys.

- **Parts:**
  - RAIL module, 400 × 80 × ≈ 33 with knobs;
  - a keyboard bed in front of it, 400 × 150: a dark bookcloth bed with a walnut lip, a **12 mm cable gutter** against the rail, and two elastic bands across (adjustable for 83–135 deep and 11–16 tall; the rail's front face is the back stop);
  - **one lid** over both, hinged at the rail's rear top edge.
- **Closed: 400 × ≈ 230 × ≈ 38** [calc]: the lid clears the keyboard by 12 mm and the knobs by 4. That's one thin flat board, close to a 16-inch laptop's footprint (≈ 356 × 248 × 17), wider and about twice as thick, so it goes where a laptop goes.
- **Open, three lid states:**
  - **standing at ≈ 100°:** a music or lyric stand, and partial shade for the panel when the sun is low in front of you (job 20; honest: it's a laptop-screen shade, not a parasol);
  - **at night:** a dim warm strip along the lid's top edge lights the keys. That's LAMP's best idea, with no wedge and no lap problem (power: tens of mW, systems' PROPOSAL, eng to confirm);
  - **flat back or lifted off** (pin hinge): a 400 × 460 lap board, or the bare pair on a desk.
- **Split** [survey]: a **brass target slides on a graduated rail** along the module's front edge. Slide it over B | C once for today's keyboard. It's a sharper version of systems' ribbon (§4.1 C): precise, it doesn't flop, it can be read by touch through a raised notch, and it can sit off-centre when the keyboard does. Surveyors use the same thing: a levelling rod and its sliding target. It works with rule A (fixed note) as systems proposed.
- **Host port: centre of the rail's front face, in the gutter.** Keyboard sockets sit anywhere along their back edges (UNVERIFIED per model), and the centre gives the shortest worst-case reach. The coiled cable lies in the gutter, never across the hands or the speaker.
- **Port light** (systems §4.2): in the gutter beside the host port, so it's where your eye already goes when you check the cable. I'd keep two lights for that reason: they live in different places and answer different questions.
- **A printed card inside the lid** [survey: the surveyor's box carries its instructions in the lid]: the family MIDI map (S6) and "keep the keyboard at its home octave" (job 6, job 18).
- **Strong:**
  - job 24: the pair always reads as one instrument, piano-shaped, whatever the keyboard;
  - job 20: thin and lap-sized when open (400 × 230 with the lid off);
  - job 3: one thin board;
  - jobs 6 and 18: the split target and the card;
  - jobs 27 and 28: the bed is a family part (S8).
- **Weak:**
  - 230 deep is a large footprint, though thin;
  - the lid's depth = rail + bed, so it changes per module: the lid isn't one family part (the bed, hinge and target rail are);
  - the chunky minis (39–49 mm tall) play but don't pack;
  - hinge, strut and lamp add three parts to build (job 26);
  - weight: module + bed + lid + Xkey near T5's edge (eng).

### 5. Systems' kits: sharpen, keep or kill
- **SPINE: keep, sharpen.**
  - **Boards:** SLAB boards, both the same size, so the book closes square.
  - **Shelf:** brass book corners, plus a spine label so it stands on the shelf.
  - **Inside:** the printed card inside the front cover; the brass split target instead of the ribbon.
  - **Straps, not corners:** two adjustable straps across the keyboard board instead of four sliding photo corners. That's fewer parts, it takes 83–135 depth without fiddling, and sliding corners would rattle with the module alone (systems' own job 3 addition).
  - **Its gift** is the closed stack, 400 × ≈ 140 × 55, the smallest rigid footprint.
  - **Its doubt:** the both-ways cloth hinge on a ≈ 0.9–1.5 kg kit, and the cable bend round the spine. FALLBOARD vs SPINE is "laptop vs book". I lean FALLBOARD; the director should see both.
- **CLOTH: keep, as the two-package answer** (eng trade-off 3).
  - **The module:** BLOCK, with **every knob top below a raised walnut rim** (harmonica holes are recessed in the comb), so a soft carry can't snap one. That answers systems' own impact weakness in the module's form, not with a second cover.
  - **The cloth:** spread, it's the frame: it owns the outline when open, as FALLBOARD's bed does. Coated bookcloth outside, a washable quilted liner inside (round-1 TIDE felt lesson).
  - **Range:** the only kit that carries the chunky minis.
  - **Honest:** it isn't a shelf object, and the two loose pieces on a lap remain.
- **LAMP: kill as a kit, keep the light.** The wedge has nowhere to stand on a lap, and its carry was never solved. The light that falls on the keys moves into FALLBOARD's lid and SPINE's standing state.
- **TETHER: kill as a kit, keep the strap.** Two bare objects with no protection and no spatial mapping; protecting them turns it into CLOTH, as systems said. The strap becomes an accessory on any kit's S4 inserts (crossbody carry for FALLBOARD's board or SPINE's book). The cable-in-the-handle idea stays in SPINE's spine.
- **BACKBONE: agree with the kill.** A jaw on unknown edges is a fitted dock by another name.

That leaves **three kits that differ in kind**:
1. FALLBOARD: one plane, one lid.
2. SPINE: two boards stacked face to face.
3. CLOTH: two objects in a soft frame.

### 6. Where I disagree with turn 1
- **"Fix the interfaces, not the sizes."** Fix the interfaces *and the one size the keyboard sets* (S8, 400 wide). Without it, every family carry part is bespoke.
- **The ribbon (§4.1 C)** is lovely, but it flops, curls and moves when the kit's carried. A brass target on a rail does the same job, stays put, and is a family part.
- **Pairings:** FALLBOARD + TIDE (the leanest panel fits the one row), SPINE + BOW (strands need SLAB's two rows), CLOTH + either.

### 7. Open questions
1. **Eng:**
   - RAIL fit (board ≈ 260 × 62, speaker box ≈ 164 cm³);
   - FALLBOARD's total weight with an Xkey;
   - lid lamp power;
   - each slim keyboard's socket position (for the centre host port);
   - the coated bookcloth product.
2. **Director:**
   - S8 (400 wide) as a family standard;
   - FALLBOARD vs SPINE as lead;
   - the LAMP and TETHER kills (folded into the other kits);
   - RAIL's single row;
   - the brass target vs the ribbon.
3. **Owner (later):**
   - laptop-shaped board (FALLBOARD) or book (SPINE) or cloth;
   - is a 400 mm wide kit acceptable (T4 was 290; open while proportions are riffed).

NEXT: design director — three kits that differ in kind (FALLBOARD, SPINE, CLOTH), three proportions and a proposed eighth family standard are on the table, with two kills folded into survivors; nobody has steered yet, and the lead (FALLBOARD vs SPINE) and the S8 standard are the director's calls before either designer builds concepts.

---

## Turn 3: design director

### Real randomness (Python `secrets`)
- **Oblique Strategy:** "Is the tuning appropriate?" (15 of 20).
- **Unrelated field:** orchestral instrument cases (6 of 12).
(A stray first number printed before the draws; I ignored it.) Tagged [tuning] and [case] below.

### 0. One thing both turns missed, which changes the voice axis
With built-in keys, round 1's BOW put floss's life in the finger, and floss owned the finger. **Now the finger belongs to someone else's product.** Lean works only if the guest sends poly aftertouch (Xkey yes, nanoKEY2 no). Lift works only on the Seaboard-class. CC1 fallback, as systems wrote it, is a good save, but it's a mod strip, not a bow. What floss still owns, with *any* keyboard, is **time and the panel**: HOLD that survives an unplug, drift, plant-and-tend, the split, the strands, the room. TIDE's ideas got stronger when the keys left; BOW's got weaker.

So I'm **not** taking the two-axes pairing (SPINE + BOW, FALLBOARD + TIDE, and so on). Paired, the owner can't tell whether he likes a kit or a voice. Ruling for pass 2:
- **Concepts differ on the kit.** That's what's new, and it's what job 28 asks for.
- **floss has one voice, shown the same in every kit.** Systems, write it in pass 2 from both round-1 voices. My steer:
  - TIDE's spine: plant-and-tend HOLD (add, re-strike to pull out), DRIFT, HOLD surviving the keyboard;
  - BOW's strands per half (they give the split a colour as well as an octave, and they're what "floss" means);
  - velocity as speed, because it works on every velocity keyboard. TIDE's inverted lifespan was a trick for one concept;
  - the PRESSURE selector with systems' fallback ladder (poly AT → channel → CC1 → nothing).
- If systems thinks one voice loses something the owner should choose, argue it in pass 2. Don't pair it with a kit.

### 1. Kits: what goes forward to concepts
**FALLBOARD, SPINE and CLOTH go forward.** They differ in kind: one plane under one lid; two boards stacked face to face; two objects in a soft frame. Lead: **FALLBOARD**, with SPINE as its real rival.
- **Why FALLBOARD leads:** its bed is rigid. Open on a lap it's one stiff board (job 20). SPINE, open flat on a lap, rests on a cloth hinge, so the two boards will sag between your thighs. FALLBOARD also has the best lid in either jam: it shades, stands as a music stand and lights the keys at night.
- **Why SPINE stays:** closed, it's 400 × 140 × ≈ 55–60, the smallest rigid footprint, and almost T4's depth. If the owner's "portability factor" means bag space, SPINE wins. He should see both.
- **Why CLOTH stays:** it's the two-package answer (eng trade-off 3) and the only one where the module alone meets T4. It's also the honest test of whether the owner cares more about the module's size or the kit's.

**Kills (agreed):**
- **LAMP** as a kit. The wedge has no lap and no carry. Its light moves into FALLBOARD's lid and SPINE's standing state.
- **TETHER** as a kit. Its strap becomes an accessory on the S4 inserts, for any kit. "The cable is in the handle" survives in SPINE.
- **BACKBONE.** A jaw on unknown edges is a fitted dock.

### 2. Rulings on the open calls
1. **S8, "every module is 400 wide": yes, as a PROPOSAL for the owner, worded as a kit rule.** The width comes from the guest, not from leftover space: 392 envelope + a 4 mm lip. That answers my round-1 pattern. But it's a family decision that changes Big Energy too, so it goes to the owner, not into the standard by us. Word it the way he'll hear it: **"floss adds no width to the keyboard you already carry."** That's the honest answer to the 290 mm objection (§4). CLOTH's BLOCK (270) is the deliberate exception: two packages, no shared bed.
2. **[tuning] Is 400 tuned right?** For the Xkey 25 (388) yes. For the K-Board C or nanoKEY2 (325), 67 mm of bed shows. Visual's dark bed makes that a frame, not a gap, and I accept it. But don't let the bed's spare width tempt anyone into putting things there. The bed holds a guest, nothing else.
3. **Split: rule A (fixed note) plus the brass target. B is rejected** (invisible state per keyboard breaks job 18). Target over ribbon, agreed: it stays put and it's a family part. Print "keep the keyboard at its home octave" on the lid card (FALLBOARD) or inside the cover (SPINE); CLOTH needs its own answer.
4. **Two lights: yes.** "One element of each kind" is a test against duplicating what the keyboard has, not a ban on two answers to two questions. Status light: fine / charging / low battery. Port light, beside the host port: off / connected / blink per note / fault.
5. **One power switch, on the module.** SPINE's "open = on" is dropped: the module also lives without the book (home, a big keyboard), so it needs its own switch anyway, and two ways to switch on is one too many.
6. **Job 29 ("why is it silent?"): add it.** The blink-per-note port light is the right answer.
7. **RAIL's one row: keep, with grouping.** Fourteen identical knobs in a line is a mixer strip, and the owner's biggest Big Energy note was "the items do not appear to be grouped or ordered in a way that makes logical sense." Group by gaps you can count with your eyes closed: octave | touch | voice | shimmer | room | out | octave. HOLD belongs with touch (it's played), not between volume and OCTAVE R as sketched. If the strands survive in the voice, try three tabs at each end of the rail beside each octave knob, so each end owns its half. Then check that the row still fits at the family pitch.

### 3. Push
- **[case] Hold the keyboard by its ends, not across its keys.** In sketch 2a the elastic bands cross the Xkey's first and last keys, which is where you play. An orchestral case holds a violin by padded blocks at its ends and neck, never across the strings. So: **two sliding end blocks** in the bed (FALLBOARD) or on the keyboard board (SPINE). Each block is padded, with a lip over the keyboard's end caps, and slides to take 325–392. Nothing crosses a key. The end blocks are the family part, not the bands.
- **[case] Cases have an accessory pocket.** Every violin case has a compartment for rosin and strings. floss's kit needs one place for the cable, plus a spare cable or a USB-C charger. In FALLBOARD it's the gutter, extended; in SPINE, the spine; in CLOTH, the sewn pocket. Show it.
- **"Own the outline, host the keys"** (visual rule 1) is the best idea of this jam, and it's what lets a borrowed keyboard read as floss. Keep it for every kit, CLOTH included: spread, the cloth is the frame.
- **The host port faces the keyboard** (systems S2), centred in the gutter (visual). Agreed, for all three.
- **The S4 ¼"-20 inserts** are a cheap family interface (tripod, strap, carry). Keep them.

### 4. Owner objections to answer before concepts are drawn
1. **"400 mm? I said portable, and T4 was 290."** Answer with "floss adds no width to the keyboard you carry", show the closed kit next to a 16-inch laptop and a book, and show CLOTH as the option where the module alone is 270.
2. **Weight near T5 (1.5 kg)** with an Xkey, plus bed, lid or boards. Eng's total is needed before scoring.
3. **"He measures nothing" vs eng's speaker.** `eng/module.md` recommends a slim driver plus passive radiator that "needs one acoustic measurement". That breaks his rule. Unless eng finds a published pairing, **assume the published-data speaker path (a 32–38 mm deep body).** That moves RAIL's fit, SPINE's closed thickness (≈ 60 mm) and FALLBOARD's lid clearance. Orchestrator: this goes to eng now, not after concepts.
4. **Build craft.** Bookcloth hinges, sewn furoshiki, end blocks and lid struts are hand work he must want to do. He's building it himself with proven methods. Bookbinding and case-making are proven crafts, but each concept must list its non-electronic making steps honestly.
5. **"Why is floss so plain?"** A one-row rail on a dark bed is quiet. Make sure the module still has a face (wordmark, coral, the family's walnut and brass) and doesn't read as a keyboard accessory.
6. **Elastic over the keys:** solved by the end blocks (§3).
7. **A one-row panel without grouping:** solved by gaps (§2.7).

### 5. What I want from pass 2 (short)
- **Systems:**
  - the one voice (§0) and its panel count;
  - can RAIL hold it in one grouped row at the family pitch, or does floss need SLAB?
  - the end-block range numbers;
  - flag the speaker path to eng.
- **Visual:**
  - FALLBOARD with end blocks, the grouped rail and the accessory pocket;
  - SPINE's closed and open-on-a-lap section (the sag question);
  - CLOTH's frame when spread;
  - one sheet comparing the three closed kits with a laptop and a book.

NEXT: product designer (systems focus) — the one-voice ruling and whether it fits a one-row RAIL are systems questions first, and the speaker-path issue needs flagging to eng before the visual designer redraws the kits.

---

## Turn 4: product designer (systems focus), pass 2

Answers the director's §5 asks: the one voice and its count, whether RAIL holds it, the end-block numbers, and `jobs.md` rev 3. Every speaker-dependent number is marked **[spk]**: it waits on `eng/module-r2.md` (the published-data speaker path, which the director's §4.3 asks eng to assume).

No new randomness this turn: it's convergence work. I reused one earlier draw on purpose. "Only one element of each kind" (turn 1) is the test I used to cut the voice down.

### 1. The one floss voice
I took the director's steer and checked it for losses (§1.4). Nothing below depends on which kit it's in.

#### 1.1 Behaviours
| | Behaviour | From |
|---|---|---|
| **Velocity** | **Speed.** A soft strike bows in slowly, a hard one speaks at once, inside ATTACK's range. Loudness doesn't change (velocity as loudness stays a firmware curve option, KEPT's salvage, with no control). | BOW |
| **Release velocity** | Sets the tail inside RELEASE's range when the keyboard sends it; otherwise RELEASE's value. RELEASE runs out to ≈ 30 s (TIDE, PROPOSAL), so a planted chord can fade over half a minute. | BOW, TIDE |
| **Strands** | Each note sounds up to three strands (octave below, at pitch, octave above). Three tabs per half: **low · main · high**. All three off = that half silent (round-1 rule: a mute). | BOW |
| **DRIFT** | Each voice wanders on its own slow random walk; the knob sets how far (0 = steady, full ≈ ±25 c, PROPOSAL). | TIDE |
| **Lean** (PRESSURE selector, 4 positions) | **swell · drift · tone · shimmer.** swell and drift act per note; tone and shimmer act on everything and follow the hardest lean. Leaning on **drift** widens *that* note's wander, and **its rate rises with the lean, so a full lean becomes a vibrato** (≈ 0.3 Hz → ≈ 5–6 Hz, PROPOSAL). So vibrato is no longer a separate position: one position covers both, which is the "one element of each kind" test. A planted note keeps the drift it was planted with. | BOW + TIDE |
| **Lean source** | The ladder: poly aftertouch / MPE → channel pressure → CC1 → nothing (turn 1 §4.3, the director's steer). With anything below poly AT, swell and drift act on every note. | turn 1 |
| **HOLD** | **Plant and tend.** While HOLD is on, every note you play joins the held set. Strike a held note again to pull it out; the re-strike's velocity sets its fade (soft = long). HOLD off: everything fades on its own tail. **Held notes survive the keyboard** (unplug, swap, hand it over). CC64 from a pedal or keyboard is ordinary sustain on every note. | TIDE, turn 1 |
| **HOLD's scope** (new, PROPOSAL) | **When the two octave knobs are equal (one keyboard), HOLD plants everything. When they differ (a split), HOLD plants the left half only, and the right half plays live.** No new control: the scope follows a state you can already see (are the pointers parallel?). This brings back BOW's "drone left, play right" without a second HOLD. Notes already planted stay planted when the scope changes; only new notes follow the new rule. | new |
| **Breath** | Fixed, no control (round 1). | WIND |
| **Shimmer, echo, reverb** | As round 1 (common §2.7–2.8), with two ties (§1.2). | common |

#### 1.2 What I cut, and why
- **REPEATS knob:** gone. **ECHO** turns up the level and the repeats together (more = louder and longer), the same tie round 1 used for reverb decay. That's a common pairing, but it's a loss for anyone who wants loud, short echoes. Flagged; not an owner question unless he asks.
- **The vibrato position:** folded into drift (§1.1).
- **BOW's "thinning in swell without pressure":** gone. The finger is the guest's now (director §0).
- **TIDE's inverted velocity:** gone (director's ruling).

#### 1.3 Count
| Kind | Controls | n |
|---|---|---|
| Stepped rotaries | OCTAVE L, OCTAVE R, PRESSURE (4), SHIMMER (4) | 4 |
| Pots | ATTACK, RELEASE, DRIFT, TONE, DEPTH, ECHO, TIME, REVERB, VOLUME | 9 |
| Buttons | HOLD (latching, played: larger), TAP | 2 |
| Toggle | FREE / SYNC | 1 |
| Tabs | low · main · high × 2 halves | 6 |
| Lights | status; port (by the host port, in the gutter) | 2 |

**13 round controls + 3 small + 6 tabs + 2 lights.** That meets the director's round-1 bar for the lean concept (≤ 13 round). It matches eng's panel estimate (≈ 16 controls + 6 tabs [eng §6]).
- **Rear wall:** power switch (the one switch, director ruling 5), USB-C (charge and computer), phones, line, TRS in and out, TUNE trim, MIDI SPLIT.
- **Front face, in the gutter:** the USB-C host port and the port light (S2).

#### 1.4 Does one voice lose anything the owner should choose?
I looked for it, honestly. Four candidates:
1. **BOW's replace-latch** (a new chord replaces the old). Plant-and-tend changes a chord by HOLD off → on (two presses) or by pulling notes. A CC64 pedal gives the classic behaviour. Small loss.
2. **Left-only HOLD:** recovered by the split-scoped HOLD (§1.1).
3. **Vibrato as its own position:** recovered as full-lean drift.
4. **TIDE's lifespan velocity:** a trick, as the director said.

**One thing goes to the owner: the split-scoped HOLD.** It's a rule he'll either find natural or find surprising, and it's cheap to change in firmware. Everything else, I'd decide.

#### 1.5 An engine catch the old voices hid: strands need fixed voice pools per half
- **Round 1:** each key was a voice, so a key's half never changed, and BOW's strand gates needed only 6 control lines (3 strands × 2 halves).
- **Now voices are allocated:** a voice can play a left note and then a right one. Its strand gates (and its half-bus routing) would then need per-voice control, meaning 75 gate lines, not 6.
- **PROPOSAL:** **fixed pools: voices 1–12 serve the left half (12 keys on a 25-key keyboard), 13–25 the right half (13 keys).** Allocation and stealing happen within a half.
  - That gets back the 6 lines and the fixed half buses that eng's signal path already assumes [eng §4: "keyers → half buses"].
  - A 25-key keyboard played live never steals.
  - Only a big home keyboard, or many planted notes in one half, steals inside that half (oldest first).
- **Eng to confirm** in `module-r2.md`. The strands' cost stands [eng trade-off 7: +31 chips, ≈ $11–17]. If the strands fall, the fallback is KEPT's bass voicing on the left bus, and the tabs go.

### 2. Does RAIL hold it in one grouped row at the family pitch?
**No. A front row of amounts plus a short back line of "kinds" does.**

**Assumptions [calc]:**
- **Family pitch:** ≥ 20 mm (Big Energy R2), ≈ 22 comfortable.
- **Group gap:** a group break adds 8–10 mm. That's countable with eyes closed: 28–32 between groups vs 20–22 inside one.
- **Slot widths:** a tab column (mini rockers turned 10 mm deep, 15 mm wide, stacked low / main / high front to back, ≈ 34 mm deep) takes one slot. The toggle takes 12; TAP, 16.
- **End margins:** 8 mm, so 384 mm is usable on a 400 rail.
- **Groups (director ruling 7):** octave + tabs | touch | voice | shimmer | room | out | tabs + octave. HOLD sits with touch.

| Layout | pitch 20, break +8 | pitch 22, break +8 | pitch 22, break +10 |
|---|---|---|---|
| **A.** Full voice, one row | 396 / 384 **✗** (−12) | 428 **✗** | 440 **✗** |
| **B.** No strands, one row | 356 ✓ | 384 ✓ (0 spare) | 396 ✗ |
| **C.** Strands kept, ATTACK + RELEASE merged into LENGTH, FREE / SYNC moved to the rear | 364 ✓ | 394 ✗ | 406 ✗ |
| **D.** Front row of amounts + back line of kinds | 344 ✓ | **372 ✓ (+12)** | 384 ✓ (0) |

**My recommendation: D, on a rail ≈ 400 × 95** (visual's own fallback depth, turn 2 §3).
- **Front row, in signal order:**

  `OCTAVE L · [low main high] | ATTACK · RELEASE · HOLD | DRIFT · TONE | DEPTH | ECHO · TIME · TAP · REVERB | VOLUME | [low main high] · OCTAVE R`

- **Back line, three items only, each directly behind the amount it qualifies:** PRESSURE behind ATTACK / RELEASE; SHIMMER mode behind DEPTH; FREE / SYNC behind TIME.
  - This is Big Energy's own rule: amounts nearest the hand, kinds and times behind.
  - All three are set-then-left, and they're the three stepped or switched "kind" controls, so the back line has one meaning.
  - The rest of the back strip stays free for the grille [spk].
- **It's still one line in the sense that matters:** it reads left to right, counts by groups from either end, and still works when a friend has the keyboard away.
- **Why not the others:**
  - **A** doesn't fit at even the minimum pitch.
  - **B** drops the strands, which the director wants and which give the split a colour.
  - **C** fits only at the minimum pitch with 8 mm between knob edges, merges ATTACK and RELEASE (losing "slow in, short out"), and puts a performance switch on the rear wall.
- **Coincidence worth knowing:** if the kit widens to 412 for the end blocks (§3), layout A fits at exactly the minimum pitch with zero spare (396 / 396). Too tight to recommend; D still reads better.
- **[spk] Depth check for D:**
  - eng's board ≈ 200 × 80 double-sided [eng] fits under a 400 × 95 rail with room;
  - the speaker box then has ≈ 120–150 × 75 mm of footprint;
  - the published-data path wants a 32–38 mm deep body (director §4.3), which on that footprint gives ≈ 300–400 cm³ [calc]: at or above eng's ≥ 150–300.
  - So the thicker body helps RAIL rather than hurting it. **FALLBOARD closed grows ≈ 38 → ≈ 43–45 mm and SPINE closed ≈ 55 → ≈ 60 [calc, spk].** Eng confirms in `module-r2.md`.
- SLAB (400 × 133, two full rows) also holds the voice easily. It stays SPINE's board size if the visual designer prefers SPINE's two boards to match.

### 3. End blocks: the range
The director's case rule: hold the keyboard by its ends, never across its keys.

**Published widths:** slim keyboards are **325–388 mm** [eng]. The Xkey 25 alone sets the top; the other three are 325.

**Each block (PROPOSAL):**
- a carriage on a track in the bed;
- a padded inner face that compresses ≈ 2 mm;
- a lip over the keyboard's end cap, with ≈ 6 mm of foam under it, so it presses down on any keyboard from 11 to 16 mm tall;
- a thumb lock, so it stays put with or without a keyboard (turn 1's "carry works empty").

| | Value |
|---|---|
| Block width, fully in | **8 mm** (6 mm body + 2 mm compressed pad) |
| Travel, each block | **32 mm** ((388 − 325) / 2 = 31.5) |
| Block width, fully out | **≈ 40 mm** |
| Inside width of the bed | **404 mm** (388 + 2 × 8) |
| Kit width with 4 mm walls | **≈ 412 mm** |

- **Both blocks move by the same amount, so the keyboard stays centred.** Centring matters: per-half controls over their half (job 18), and the brass target's home position.
  - The bed carries **the same graduation as the brass target's rail**. Set both blocks to the same number: one scale for the whole kit.
  - A self-centring linkage (both blocks on one left-and-right-hand screw, like a centring vice) is neater but adds a mechanism. Visual / eng to weigh it; the scale is the reliable default.
- **This changes S8: 400 doesn't hold real blocks.** At 400 the Xkey leaves 2 mm per end: room for felt, not for a block. **PROPOSAL: S8 becomes ≈ 412** (or the slim class tops out below the Xkey, which drops the one slim keyboard with poly AT under $100; I wouldn't).
  - The owner wording still works, made honest: **"floss adds about an inch to the widest travel keyboard"** (412 vs 388), and nothing in depth beyond the rail.
- **Front to back:** the keyboard's back edge stops against the rail's front face (visual). A shallow keyboard (83 mm) leaves ≈ 55 mm of bed in front of it, held only by the blocks' grip. **When packed, a foam strip on the lid's underside presses on the keyboard's top** (lid clearance 12 mm → a 13–14 mm strip compressing onto 11–16 mm keyboards [calc]), so nothing moves in the bag. In SPINE, the facing board does the same job.
- **SPINE:** the same blocks on the keyboard board, so SPINE's boards go to 412 as well. **CLOTH:** no blocks. The cloth wraps, and the BLOCK module's rim guards its knobs (visual).

### 4. The accessory pocket (director's push)
- **FALLBOARD:** the 12 mm gutter, along the bed's 404 mm, ≥ 12 mm deep. It holds the coiled cable relaxed (coil Ø ≈ 10–12 mm: UNVERIFIED, product not chosen) plus one flat spare cable.
  - A USB-C charger brick (≈ 30 mm cube class) doesn't fit any rigid kit at FALLBOARD's thickness. **Honest answer: the rigid kits carry cables, not a charger.** If the owner wants the charger in the kit, it's a lid pouch, which costs thickness.
  - The host port and the port light sit in the gutter's centre.
- **SPINE:** the spine's channel (cable) plus a flat sleeve inside the front cover (spare cable, the card).
- **CLOTH:** the sewn pocket takes everything, charger included.

### 5. `jobs.md` rev 3: proposed changes
Held from turn 1 (1–6), then from the director's rulings (7–14). I'll write rev 3 when the jam closes, unless the director wants it sooner.

| # | Job | Change |
|---|---|---|
| 1 | 2 | Host port is **USB-C**, on the module's keyboard-facing edge (owner 12:52; S2) |
| 2 | 3, 28 | The carry **works with no keyboard in it**: blocks lock, nothing rattles |
| 3 | 3 | **Chunky minis play but aren't carried** in the rigid kits (CLOTH carries them); owner trade-off 2 decides |
| 4 | 6 | Keyboards differ in which note their lowest key sends at default; **rule: fixed split B3 \| C4, a brass target shows where it lands, "keep the keyboard at its home octave" printed in the kit** (director ruling 3; CLOTH needs its own place for the line) |
| 5 | 23 | Name the cable-length conflict; **answer: a coiled cable ≈ 0.3 m relaxed to 1 m stretched** |
| 6 | **29 new** | **"When floss is silent, find out why from floss itself": no keyboard, keyboard unpowered, notes not arriving, volume down, a half muted.** (inferred; director ruling 6). Must show: the port light (off / steady / blink per note / fault) plus the visible tabs and VOLUME |
| 7 | 3 | **Holds the keyboard by its ends; nothing crosses a key;** takes 325–388 wide, 83–135 deep, 11–16 tall (director's end-block push) |
| 8 | 3 | **One place for the cable** (and the spare) in every kit; the charger only where the kit can take it |
| 9 | 3, 28 | **S8 as an owner proposal:** every rigid kit is one family width (≈ 412 with end blocks, §3), "floss adds about an inch to the widest travel keyboard"; CLOTH's module is the deliberate exception |
| 10 | 9 | What a velocity-only keyboard gets: the lean ladder, so the selector runs from the mod control (CC1) |
| 11 | 14 | HOLD = **plant and tend** (add, re-strike to pull out); it survives the keyboard; its scope follows the split (owner to confirm, §1.4); CC64 = sustain on everything |
| 12 | 18 | Add the **port light** and the **brass target** to what a concept must show; the status light keeps three meanings |
| 13 | 19 | **One power switch, on the module** (director ruling 5) |
| 14 | 26 | Every concept **lists its non-electronic making steps** (bookcloth hinge, sewing, end blocks, lid strut) with the craft each needs (director objection 4) |

Unchanged: the other jobs. Job 24 gains "own the outline, host the keys" as a must-show line if the director wants it in the jobs (it's a concept rule more than a job; I'd keep it in the concept brief).

### 6. Flags to eng (`module-r2.md`)
1. **[spk]** Body depth on the published-data speaker path, and therefore: RAIL's speaker volume, FALLBOARD's closed thickness (≈ 43–45?), SPINE's (≈ 60?).
2. **Fixed voice pools per half (12 / 13)** for the strand gates and half buses (§1.5).
3. **Kit weights at 412 wide** (rail + bed + blocks + lid + Xkey vs T5's 1.5 kg).
4. **Lid lamp power** against T2.
5. **Coiled cable products:** coil diameter, and whether right-angle USB-C coiled cables exist off the shelf for each keyboard socket.

### 7. Open questions
1. **Director:**
   - D (front row + back line of kinds, rail ≈ 400–412 × 95), or SLAB for every kit?
   - S8 at ≈ 412?
   - the self-centring linkage vs the scale?
   - REPEATS tied to ECHO?
2. **Owner (later):**
   - the split-scoped HOLD;
   - S8 at ≈ 412 ("about an inch over the widest keyboard");
   - charger in the kit or not.

NEXT: product designer (visual focus) — the voice, the row (layout D on a ≈ 400–412 × 95 rail), the end blocks (8–40 mm, kit ≈ 412) and the pocket are now numbers, and FALLBOARD, SPINE and CLOTH need redrawing around them (end blocks, grouped row with its back line of kinds, lid foam strip, the closed-kit comparison sheet) before the director steers.

---

## Turn 5: product designer (visual focus), pass 2

Answers the director's §5 visual asks and draws systems' turn-4 numbers. This is the last jam turn before concepts.

**Sketches** (rough 2-D, to scale, each opened and checked):
- `sketches/visual-module-jam3a-fallboard.png`: FALLBOARD with end blocks, the grouped rail and the gutter pocket; closed sections for both speaker paths; an end-block section.
- `sketches/visual-module-jam3b-spine-cloth.png`: SPINE closed (cover and both thicknesses) and on a lap (the sag question); CLOTH spread as a frame.
- `sketches/visual-module-jam3c-closed-kits.png`: the three closed kits beside a 16-inch laptop and a hardback book, plans and end views, with a table.
- Source: `sketches/visual_module_jam3.py` (`python3 visual_module_jam3.py [a b c]`).

**Speaker:** `eng/module-r2.md` doesn't exist yet. Every thickness is drawn twice: the slim driver-and-radiator path and the published-data path (body 32–38). Numbers marked [spk] wait on it.

### Real randomness (Python `secrets`)
- Oblique Strategy: **"Change instrument roles."** Field: **pipe-organ stop knobs.** I used it on the director's objection 5 ("why is floss so plain?"), the one open face question.

### 1. FALLBOARD, redrawn (sheet a)
**Width:** S8 at ≈ 412, systems' end-block number. The row still fits: **front row 388 long at pitch 22, with 10 extra between groups, on a 412 rail: +4 spare** [calc].

**The rail, 412 × 95, layout D:**
- **A sunk channel.** The cream deck sits 6 mm under the walnut rim (deck at 24, rim at 30 on the slim path). All controls live in the channel. The grille strip runs along the back.
- **The wordmark is centred in the grille**, where a piano puts its nameboard. It's centred, never off to one side.
- **Front row, in seven groups:** `octave · stops | attack release HOLD | drift tone | depth | echo time TAP reverb | volume | stops · octave`.
  - Within a group, pitch 22; between groups, 32, with **a 1 mm raised brass fret across the channel**. Count frets from either end with eyes closed (director ruling 7).
  - HOLD sits with touch: brass, larger, a latching push.
  - TAP keeps round 1's lit ring as the status light.
- **Back line of three kinds,** each behind the amount it qualifies, at Ø 10, smaller than the amounts at Ø 14.9 so the hand meets amounts first:
  - PRESSURE (coral) behind attack / release;
  - SHIMMER mode behind depth;
  - FREE / SYNC behind time.
- **The ends are organ stop jambs** [roles] [organ]. Each end holds its half's OCTAVE plus three **stop tabs** (low · main · high, front to back). Theatre organs use exactly this: rocker stop tabs, engraved, grouped at the sides of the manual. Each end owns its half, and the instrument gets two "shoulders" with a quiet line between.
  - This is my answer to objection 5: the face is the two jambs, the brass frets, the nameboard wordmark and one coral knob, on walnut and cream. It's not a keyboard accessory.
- **Knobs in a channel pay off on the published speaker path.** Knob tops at 32 sit under a 32–38 rim, so the thicker body costs only its own depth: **closed ≈ 38 (slim) / ≈ 40–46 (published)** [calc, spk]. Without the channel it would be ≈ 48–54.

**The bed, 412 × 155:**
- **End blocks** (systems' numbers: 8 mm in, 40 out, 32 travel, inside 404). Each is 80 deep, set at the back against the gutter, so an 83-deep keyboard is fully held and a 135-deep one by its rear 80.
  - Each block has a padded face, a lip with 6 mm of foam over the end cap, a thumb lock and a brass knob.
  - **Nothing crosses a key.** The section is drawn at 2 : 1.
- **One brass scale:** graduated 0–32 each side on the bed's front lip, and the same graduation on the target rail. Set both blocks to the same number. I'd stay with the scale rather than a self-centring linkage: it has no mechanism, and one scale reads across the whole kit.
- **The pocket is the gutter:** 404 long × 12 wide × ≈ 30–36 tall (bed floor to lid).
  - It holds the coiled cable and a flat spare. The host port and port light sit at its centre.
  - **No charger** (agreeing with systems: honest).
- **A foam strip under the lid** pins the keyboard when closed: ≈ 14–20 mm, more on the published path.
- **Footprint:** 412 × 250, open or closed.

### 2. SPINE (sheet b)
- **Closed:**
  - **Cover:** a book: 412 × 145, brass book corners, a cream label with the wordmark, one coral line. The spine is on the far edge.
  - **Thickness:** **≈ 54 (slim) / ≈ 56–62 (published)** [calc, spk], as a stack of keyboard board 4, keyboard 16, foam and air 4, then the module face down with its knobs in the channel.
  - **Room to spare:** a 412 × 145 module board holds layout D with ≈ 50 mm to spare, which goes to the speaker box, useful on the published path.
- **The sag question: mostly a false alarm on a lap, and a real problem off it** [geometry].
  - **On a lap it's supported.** The spine runs left to right, *across both thighs*. Each rigid board spans the gap between the thighs, and the spine rests on both. Seen from the side, the thighs slope gently to the knees and the whole kit lies along them.
  - **It folds where nothing is under the spine:** knees apart with the kit across them, a gap between bench slats, or lifted by its two ends. Then both joints dip, and pressing keys makes it worse. That's a joint problem, not a board problem.
  - **Fix (PROPOSAL): a spine that stops at flat.** A rigid spine board between two cloth joints, with the boards' inner edges bevelled to bear on it at 180°. It folds *up* to close or stand, never *down*. Open, it's one stiff board in the direction gravity loads it. It's bookbinding craft (a making step to list, job 26).
  - **If the director wants zero risk:** a 3 mm slat stowed in the spine slides across both joints to lock them.
- The director's lap objection to SPINE is weaker than it looked. Its real costs are the closed thickness (≈ 2–2.5 laptop volumes, ≈ 3.2–3.6 laptop thicknesses) and the hinge craft.

### 3. CLOTH spread as a frame (sheet b)
- **An 800 mm square cloth, dark slate green** (CLOTH's own colour; the module stays walnut and brass).
- **Woven in pale thread: the family outline, 412 × 250, the same as FALLBOARD's footprint**, plus a dashed centre line. "Own the outline, host the keys" holds in the soft kit too: the module sits in the back of the frame and the keyboard in the front.
- **Woven beside the centre line: "keep the keyboard at its home octave".** That's CLOTH's answer to the director's ruling 3 (it has no lid card).
- **BLOCK module,** 270 × 100, with its knobs below a raised rim. It meets T4. Its split target rail spans 270, which covers the middle, where B | C lands on a centred keyboard.
- **A sewn pocket** for the cable, a spare and the charger (the only kit that takes a charger). **A removable, washable module sleeve.**
- **Brass weights at the four corners:** they keep it flat outdoors and give the knot its corners.
- **Honest:** on a lap an 800 cloth drapes and stops being a frame. CLOTH is a bench-and-table kit.

### 4. The closed kits compared (sheet c)
All at one scale, with a 16-inch laptop (≈ 356 × 248 × 17, the MacBook Pro 16 class, rounded) and a hardback novel (≈ 156 × 234 × 35, illustrative). [calc] throughout; thickness is slim / published.

| Kit closed | Footprint | Thick | Volume (L) | vs laptop |
|---|---|---|---|---|
| FALLBOARD | 412 × 250 | 38 / 46 | 3.9–4.7 | 2.6–3.2× |
| SPINE | 412 × 145 | 54 / 62 | 3.2–3.7 | 2.1–2.5× |
| CLOTH (Xkey) | ≈ 400 × 150 | ≈ 56 / 64 | 3.4–3.8 | 2.2–2.6× |
| CLOTH (nanoKEY2) | ≈ 335 × 110 | ≈ 56 / 64 | 2.1–2.4 | 1.4–1.6× |
| 16-inch laptop | 356 × 248 | 17 | 1.5 | — |

**Read:**
- **FALLBOARD** has a laptop's footprint: 56 mm wider and 2.2–2.7 times as thick. It's the only kit that opens and plays with a lid that works.
- **SPINE** covers ≈ 40 % less area and wins on bag space.
- **CLOTH's** bundle is SPINE-sized with a big keyboard and smaller with a small one, but soft. Its module alone is the only thing under T4.
- **No one-package kit meets T4.** S8 ("floss adds about an inch to the widest travel keyboard") is the honest answer to the owner's 290 mm objection.
- **Weights are eng's** (T5).

### 5. Agreements and small pushes on turn 4
- **Agree:**
  - layout D;
  - S8 at ≈ 412 (it also gives the row its +4);
  - the end-block numbers;
  - the gutter as pocket with no charger;
  - the lid foam strip;
  - the split-scoped HOLD going to the owner (it reads well on the rail: the two octave pointers, parallel or not, sit at the two jambs, so you can see the scope from the ends).
- **Push: the stop-tab words.** low · main · high (plain, the owner's one-word rule, my default) vs the organ's 16′ · 8′ · 4′, which is what the tabs literally are, but it's jargon (the director's round-1 objection). Default plain; the director can rule.
- **Push: frets.** Brass (the family, and they count by touch) vs a walnut ridge (quieter). I'd keep brass, but it's six more bought or cut parts.
- **The tab column is ≈ 34 deep**, so it reaches into the back line's band at each end. That's fine because no back-line control sits at the ends. Noted so nobody moves PRESSURE outward later.

### 6. Open questions
1. **Eng (`module-r2.md`) [spk]:**
   - which speaker path;
   - the rail body depth (32–38) and therefore every closed thickness above;
   - the speaker box in a 412 × 95 rail with a 6 mm channel over the front 58 mm;
   - kit weights at 412 (T5);
   - coiled-cable coil diameter vs the 12 mm gutter.
2. **Director:**
   - FALLBOARD's face (stop jambs + frets + nameboard);
   - the stop-tab words;
   - brass frets;
   - SPINE's stop-at-flat spine as the sag fix (or the slat too);
   - CLOTH as a bench kit only;
   - whether sheet c is the right form to show the owner.
3. **Owner (later):**
   - board, book or cloth (sheet c);
   - S8 at ≈ 412;
   - the split-scoped HOLD;
   - charger in the kit (only CLOTH).

NEXT: design director — every visual ask from turn 3 is drawn to systems' turn-4 numbers (FALLBOARD with end blocks, the grouped rail and the pocket; SPINE closed and on a lap; CLOTH as a frame; the closed-kit comparison). The face answer and the sag finding need the director's ruling, and this was the last jam turn, so it's time to close the jam and send the three kits into concepts.
