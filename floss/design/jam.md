# floss jam

Concept phase, 2026-11-22. Read `BRIEF-CONTEXT.md` first. Each turn adds below; don't rewrite earlier turns, argue with them.

---

## Turn 1: product designer (systems focus)

### Real randomness (drawn with Python `secrets`)
- **Oblique Strategy:** "Work at a different speed" (card 42 of 50). Second draw: "Do the washing up".
- **Unrelated field:** bell ringing / change ringing (3 of 25).
- **Twist:** "it is designed for two players" (5 of 10).

How I used them is marked [speed], [bells], [duet], [washing up] below.

### Jobs (written from the owner's words before reading any spec)

| # | Job | Source |
|---|---|---|
| J1 | **Play warm, shimmering string chords away from a desk**: battery, built-in speaker, no setup. | stated ("portability", "analog voices, shimmer and warmth", battery) |
| J2 | **Play as many keys at once as I like**, every note sounding. | stated ("polyphonic would be amazing") |
| J3 | **Play two parts at once on a split**, each half in its own octave, e.g. low cello line on the left, violins on the right. | stated (split, octave per half) |
| J4 | **Shape each note by how I strike it** (velocity), which the 1974 machines couldn't. | stated ("innovate ... with velocity") |
| J5 | **Lean into notes I'm holding** (pressure) **and choose what that does.** | stated (per-key pressure to explore; selectable destination) |
| J6 | **Choose and set the shimmer**: the analog ensemble, or a Daisy mode; how much. | stated |
| J7 | **Add echo and reverb**, synced to MIDI clock when there is one. | stated (Big Energy rules carry over) |
| J8 | **Hear it** on the speaker; **go private** with headphones, which mute the speaker. | stated |
| J9 | **Use it with other gear over MIDI**: play it, play others from it, split channels on/off, send velocity and pressure. | stated |
| J10 | **Pick the tone colour**: which registers (string sections) sound. | inferred: every string machine has registers; the owner hasn't named any |
| J11 | **Read its whole state from the panel**: no screen, so knob and switch positions are the state; the split and both octaves visible at a glance. | stated rule (no screens); "at a glance" inferred |
| J12 | **Be playing within seconds of switching on**; know battery, know charging. | inferred (portable, battery) |
| J13 | **Carry it and take it to the park**; play on a bench or lap, in sun. | inferred, carried from Big Energy's J22 and his "take this to the park" |
| J14 | **Hold a chord or drone without holding the keys**, so one hand is free (or both, to ride the shimmer). | inferred (pads and drones are what string machines get used for; the split makes it more useful) |
| J15 | **Play many notes without it distorting, and one note without it being thin or quiet.** | inferred (classic string machines just sum every key) |
| J16 | **Share it**: a friend sits beside me and plays the other half. | inferred, from the [duet] draw plus Big Energy J22(g) |
| J17 | **See one point of view in the object** and want to play it. | stated (carried from Big Energy J20) |
| J18 | **Play in tune with others** (an acoustic guitar in the park, a track). | inferred |

Two things I checked after writing these: the owner's floss record (`design/owner.md` 2026-11-21 onward) adds no job I missed. Big Energy's `design/jobs.md` J14 (open it to service) and J11 (build it himself) apply too; I'll carry them into `jobs.md`, not the jam.

### The structural question everything hangs on: where does a note live?

Velocity and pressure *per note* (J4, J5) are impossible on a classic string machine, because every note shares one envelope and one VCA. So the voice architecture is a design question, not just eng. Three structures, and what each does to the jobs:

| | **A. Classic divide-down, shared envelope** | **B. Every key is a voice** | **C. Allocated voices (a small poly)** |
|---|---|---|---|
| How | One master clock, dividers, one shared filter and VCA (Solina) | One tone per key from a microcontroller (any pitch, so octave per half is just arithmetic), **one small VCA per key** with its own envelope from firmware, then shared registers, filter, ensemble | N analog voices (6–8) assigned to keys |
| Velocity per note | No: global only | **Yes** | Yes |
| Pressure per note | No | **Yes**, if the keys can sense it | Yes |
| Every key at once (J2) | Yes | **Yes, 25 by construction** | No: N notes |
| Cost | Lowest | 25 VCAs (≈ 13 dual chips) plus envelope CVs | Highest; that's port-a-poly's job |
| Verdict | Fails J4/J5 | **My starting point** | Wrong instrument |

**B is a Polymoog idea on 25 keys.** It needs no voice stealing on the keys. MIDI notes from outside get assigned to the 25 slots. Per-note things the firmware gives almost free: level, pitch (vibrato, **drift between notes** per key), and pulse width (timbre per note). Shared, global-only things: the register filters, the ensemble, echo, reverb. That split matters for the pressure selector (below).

Note on "analog voices": the Solina's tones were digital logic too. What makes it analog is everything after the tone: VCAs, filters, the BBD ensemble. B keeps that true, and every note is made the same way, so it avoids the analog-and-digital-in-one-chord mix he's skeptical of. **Eng to check:** 25 VCAs, battery draw, board area in a ONE SHEET-size body.

### Structure ideas

1. **[washing up] The split isn't a mode; it's two octave controls.** Left half and right half each get an OCTAVE control. Set both the same and the keyboard is continuous; set them apart and it's split. No SPLIT switch, no hidden state, and the panel shows the split exactly. Split point fixed at the middle: 25 keys C to C, so left 12 (C–B) and right 13 (C–C). *Open:* is a fixed point enough? I think yes for 25 keys.
2. **Rule: a held note keeps its pitch when its half's octave changes.** The next press uses the new octave. No jumps mid-chord.
3. **MIDI split ON/OFF is set-and-forget**, so it goes on the rear wall with the jacks (Big Energy's precedent for set-and-forget choices). With split on, left is channel 1, right is channel 2.
4. **Pressure: one selector, and its choices are honest about per-note vs global.** Candidates: SWELL (per note), VIBRATO (per note), BRIGHT (global: the shared filter follows the hardest-pressed key), SHIMMER (global: ensemble depth). A 4-way rotary, like Big Energy's TYPE switches. If pressure ends up on a shared strip, the same four still work, just globally.
5. **Hold (J14): [bells] "SET".** A bell ringer "sets" a bell: balances it mouth-up so it stays until pulled again. A latch that holds what's down on the **left half** (the drone side) until you play there again. One momentary button plus its light. Set-and-forget it isn't; it's played, so it lives by the keys.
6. **The panel budget (strawman, to be cut, not grown):** OCTAVE L, OCTAVE R · 3–4 register levels · TONE · SWELL (attack) and RELEASE · SHIMMER mode + DEPTH · ECHO and REVERB (amounts in front, kinds behind, per Big Energy's split rule) · PRESSURE → selector · VOLUME · SET · status light. That's about 16–18 controls, against Big Energy's ≈ 34. The space it frees is the next idea.
7. **The freed depth becomes the speaker box.** Fewer controls means less board area under the panel. That empty volume is the sealed air space a passive radiator needs. Floss's body is a soundbox with keys on it, like a zither or a psaltery. That's a real reason for its shape, not just styling. (Speaker ≥ 55 mm from the BBDs and ≥ 60 mm from the Hall sensors, per Big Energy's rules.)

### Interaction ideas

- **[speed] Velocity sets the bow's speed, not just its loudness.** Soft touch: the note blooms in slowly (a swell). Hard touch: it bites in fast. In a chord played unevenly, each note arrives at its own pace. No string machine has done this, and it's the most string-like thing velocity can do. Global SWELL sets the range; velocity places each note inside it. (Loudness can ride along with it. Whether the owner wants a LOUD / SPEED / BOTH switch like Big Energy's VEL is an open question. I'd rather not spend a switch.)
- **[speed] Pressure as bow pressure (the SWELL choice):** holding a key without pressure lets the note thin and fade slowly; leaning in keeps it full or grows it. A held chord becomes something you *play* the whole time, not just hold.
- **Many notes vs one (J15):** a soft gain stage that pulls the sum down as more keys sound, so 1 note and 12 notes land at similar loudness. A real design choice: classic machines get louder with every key, and some players like that. *Open question.*
- **No tuning wait.** Tones come from a crystal, so it's ready at power-on (unlike Big Energy's autotune). J18: a small TUNE trim (±50 cents) for playing with acoustic instruments. It earns a place only if it's a rear trim, I think.
- **States to design for:** ready; low battery; charging; headphones in (speaker muted); MIDI moved a knob's setting (the knob is "not in control"); MIDI split on; SET holding; all 25 keys held; pressure at full on every key; shimmer analog mode with its BBD hiss at full depth.

### Creative directions (they differ in kind, not styling)

1. **BOW** [speed]. Every key is a bow. Velocity is bow speed, pressure is bow pressure, release is lifting the bow. Its point of view: the slowest, most touch-alive string machine. The panel almost disappears; the keys do the work.
2. **SIX STRANDS** (from the name). Embroidery floss is six strands twisted together, and you split them apart to stitch. Floss's voice is strands (registers) you can separate: the left half and the right half each take a different mix of strands, so the split is in timbre as well as octave (cello strands left, violin strands right). The silk sheen is the shimmer. The cost: a register mix per half doubles those controls, unless each strand gets a 3-way L / BOTH / R switch instead of a level.
3. **BELFRY** [bells + duet]. Floss as a band of two. The halves face two players (one sits on each side; maybe the speaker faces between them). "SET" latches a drone; **ROUNDS** re-strikes a held chord one note at a time in a permutation order, as change-ringers do, so a pad breathes in rhythm, tapped or clocked to MIDI. Social and rhythmic; the riskiest one for panel economy.
4. **DISH RACK** [washing up]. The radically plain one: about 8 controls, everything else fixed at well-judged defaults, like a lunchbox Solina. Its point of view is that a string machine should be an appliance for one feeling. Use it as the provocation that every other concept's controls have to beat.

My pick to push: **BOW as the engine** (structure B plus velocity-as-speed); **SIX STRANDS or BELFRY as the face**. The visual designer may see it the other way round.

### Open questions (for the team, and eng later)
- Can 25 per-key VCAs fit the board, the battery and the cost? (Eng.) If not, BOW collapses to A plus global velocity, and J4 weakens.
- Per-key pressure with Choc V2 + Hall: the sensor reads travel only to the bottom. Is pressure past the bottom possible (FSR lanes under each key, or overtravel)? Big Energy's floating strip C on FSR lanes gives one shared reading, not per key. (Eng; the brief requires a shared-strip fallback.)
- Velocity: does it set speed, loudness, or both, and does that need a switch?
- Should the sum-compression (J15) be on, off or switchable?
- Is a fixed centre split right, or does the owner expect to move it?

NEXT: product designer (visual focus) — SIX STRANDS, BELFRY and the soundbox body are form ideas as much as systems ones, and the face of BOW is theirs to shape before the director steers.

---

## Turn 2: product designer (visual focus)

Sketch: `sketches/visual-jam1-sail.png` (source `sketches/visual_jam1.py`). It's rough on purpose: it shows the ideas, not a layout.

### Real randomness (drawn with Python `secrets`)
- **Oblique Strategies:** "Use an old idea" (1 of 50), then "Go slowly all the way round the outside" (16 of 50).
- **Unrelated fields (30):** lighthouse optics (11), kite making (17).
- **Twist (10):** "it is designed for a child's hands" (5).
- **floss's thread colour (16 thread colours):** **coral** (9).

How each one was used is tagged [old], [outside], [lighthouse], [kite], [child] and [coral] below.

### Thrown away first
- **The first idea any AI would have: a smaller CATHEDRAL.** Walnut, cream, brass, black knobs, same everything. "Shared universe" means a family, not a copy. floss keeps the family's construction and grammar, and gets its own material idea and one colour of its own. Dropped.
- **f-holes as the speaker grille.** It's the cliché for "strings": every guitar-shaped gadget has them, and two of them suggest stereo on a mono speaker. Dropped. (The rose window, below, replaces them.)
- **Cotton-candy pastels from the name.** They're cute, and they don't fit the family. Dropped, but the thread idea survives as [coral].
- **A translucent body that glows everywhere.** It shows the boards, looks cheap and fights the lantern. Dropped.
- **A literal kite (diamond) outline.** Twenty-five keys make a rectangle, and a diamond wastes volume and won't go in a bag. Dropped. Kite *construction* survives.

### What I take from turn 1
- **Structure B and BOW as the engine:** agreed. Velocity as bow speed is the best idea on the page. My visual consequence: the keys must invite a lean (see the pegs below).
- **The split is two octave controls** [washing up]: agreed, and I can make it read better (idea 2).
- **The freed depth becomes the speaker box:** agreed in principle, but I'd **move it to the lid** (idea 1). The base is where the battery, the boards and the 60 mm Hall clearance already compete for space.
- **SIX STRANDS:** I'm keeping the logic (a register mix per half) and dropping the 3-way L / BOTH / R switch. Two rows of tabs, one row over each half, says the same thing spatially (idea 2).
- **BELFRY:** the duet is worth keeping and falls out of idea 2 for free. Drop ROUNDS for now: it's a feature looking for a panel.
- **DISH RACK:** keep it as the provocation. [child] gives it a face (direction 4).

### Ideas

**1. SAIL: the lid is the soundbox, not a second panel** [kite + lighthouse + shared universe]
- floss uses **CATHEDRAL's base unchanged in kind**: the case, the keys and their carrier, the hinge, the brass stays and the superellipse corners. About 16–18 controls plus 25 keys fit CATHEDRAL's base footprint (≈ 286 × 132), which already holds about 20 controls, the keys and the stick. So the **lid needs no controls at all**.
- **The lid becomes the instrument's body:** a walnut frame with speaker cloth stretched over it (a kite's spars and skin). Inside is the sealed air space the passive radiator needs. Standing at CATHEDRAL's angle, the cloth faces the player, like a harmonium's lid or a music stand, so the sound comes at you on a park bench instead of up into the sky. Flat on a table it fires upward, which still works. Closed, the cloth face lies over the keys.
- **Open the lid = on, close it = off** (a magnet and a Hall sensor at the hinge). The crystal tones need no tuning wait (systems), so opening it is the whole start-up (J12). The first few seconds after opening are the feel moment: the lantern swells up as the sound comes ready.
- **Closed, floss and Big Energy are the same brick on a shelf.** The shared universe shows in the silhouette. Closed, floss may even be thinner, because its lid has no knobs to nest against the base's.
- **The lid's back** is a blank façade field for the owner to draw on, as with CATHEDRAL's pipes (he said he'd design those lines himself). My suggestion: six strands twisting along it.
- **Eng to check:** driver plus passive radiator in a lid ≈ 20–24 mm deep (gross ≈ 0.7–0.9 L before the frame); the speaker leads through the hinge (CATHEDRAL already routes lid wiring there); and the hinge switch.

**2. Above each half, its own; the coral thread** [outside + SIX STRANDS + duet]
- **Every control that belongs to one half sits directly above that half.** Each half's octave and its row of register tabs are in front of the hand that uses them. Shared controls (tone, swell, release, pressure, shimmer, depth, echo, reverb, volume) go on the far row.
- **A single coral line** is inlaid flush (nothing raised, per the owner's Big Energy rule) through the control rows at the split point, between B and C. Where the keyboard splits, the panel splits.
- **Each octave knob sits at the outside end of its row** [outside]: left octave at the far left, right octave at the far right, as far apart as the hands that use them. Read the state at a glance: **pointers parallel = one keyboard; pointers apart = split, and the angle between them is the interval.** No split light and no split mode. Positions printed as organ feet: *16' · 8' · 4' · 2'* [old].
- **Registers as rocker tabs, not level knobs** [old: the Solina's tabs and an organ's stops]. A tab is on or off and you can see which from across a room (J11). On costs nothing in panel words. Two rows of three (for example cello · viola · violin, though the names are systems' and eng's) let the left half be cello while the right is violins: SIX STRANDS without a 3-way switch.
- **The duet falls out of it:** a second player sits at the right half and has their own controls right in front of them (J16).
- **SET** (systems' latch) sits at the inside end of the left row, beside the split, with a coral dot that stays lit while it holds.
- **Cost to check:** six tabs and two octaves is eight controls for the halves, against systems' 3–4 register levels plus two octaves. The total stays at about 18. If the tabs have to be levels, the map still works: two rows of small knobs.

**3. The rose** [old + shared universe]
- **One six-fold rose window over the driver**, cut through the cloth frame's baffle with the cloth behind it, as in sketch C. It's a cathedral's rose window to Big Energy's lancets, a lute's rose, and six strands of floss. It's the family link, done in floss's own words.
- It works in any format: in the lid (SAIL), or in the deck of a single slab.
- **The passive radiator sits behind plain cloth** and needs no visible opening.

**4. The lantern: you can see the shimmer** [lighthouse]
- **Three warm LEDs behind the lid's cloth**, each following one phase of the ensemble's LFOs. The light drifts across the cloth the way light moves on water or a sail. Depth sets how far it moves; shimmer off leaves a still, dim glow. The colour says which mode: **amber for the analog BBD, paler for Daisy modes.** That makes his "analog mode" visibly different without a word printed on the panel.
- **Rule: the lantern never signals state.** It only shows the sound moving. States go on the one status light (idea 5). That keeps it honest as "no screen".
- **Honest limit:** behind cloth it will barely show in midday sun. It's a dusk-and-indoors delight, not something any job depends on. It costs a few mA, to go in the power budget.
- *To check:* that classic string ensembles really are three BBD lines modulated by LFOs at about 120° apart. I believe it's true of the Solina, but I haven't verified it.

**5. One status light that speaks in lighthouse "characters"** [lighthouse]
- Lighthouses tell themselves apart by rhythm (a chart writes, for example, "Fl(2) 10s"). floss's one status light uses rhythms for its states: **ready** = fixed dim green; **low battery** = two short amber flashes every 10 s; **charging** = slow equal on and off; **echo on MIDI clock** = a quick flash on each beat; **a knob not in control** = on, with one short eclipse. Each pattern is learnable and none of them is a code you have to look up. Sketch D draws them.
- It's one part for many states. That's an economy the "earn its place" rule likes.

**6. The keys are an old idea: HUSH's maple pegs on CATHEDRAL's carrier** [old]
- CATHEDRAL's key carrier already takes interchangeable heads (a 9.53 × 3.2 tenon: brass, birch or printed). **floss gets maple (or birch) heads with dark sharps; Big Energy keeps brass.** It's the same keyboard part, and the two instruments tell themselves apart at a glance. The owner loved HUSH's "organ like" pegs.
- **A felt collar under each peg** (from HUSH) means leaning in gives a little. You can feel bow pressure in your finger, and it also cushions the bottom of the press, which is where per-key pressure has to be read. **Eng:** whether a compliant collar helps or hurts per-key sensing (an FSR under the collar?).

**7. coral is floss's one colour** [coral]
- Big Energy's one accent is the red CUTOFF. **floss's is coral**, used only where floss is floss: the split line, the depth knob (the hero, since shimmer is the instrument's reason to exist), SET's dot, and one coral thread woven across the lid's cloth. Everything else is the family's palette: walnut, cream, black, and wood keys.

### Creative directions (they differ in kind)

| Direction | Kind | Format | What it's for |
|---|---|---|---|
| **SAIL** (1 + 2 + 3 + 4 + 6 + 7) | **a body that is a voice**: the object's biggest surface makes the sound and shows it moving | CATHEDRAL's case; controls on the base, soundbox in the lid | my lead: the most floss, and the most reuse |
| **LUTHIER** | **a single slab built like a violin top** [outside]: a pale top plate with a **purfling** line (the inlaid line luthiers run all the way round a top's edge), here in coral, round the outside; walnut ribs; the rose in the deck; octave knobs at the two ends | ONE SHEET format (≈ 286 × 170) | the slimmest, most "one object" option, but the sealed box shares the base with the battery and the boards, which is what makes it hard |
| **STOPS** | **a harmonium / combo organ** [old]: a row of tabs right behind the keys, everything readable from across a room; the speaker breathes out of the back like a harmonium's bellows | either | if the owner wants the "old instrument" reading turned up loud. It's mostly idea 2 pushed harder; it may merge into SAIL |
| **BIG HANDS** (DISH RACK's face) [child] | **an object a child can't get wrong**: about 8 controls, all large enough to grip with a whole hand, tabs the size of dominoes, two big octave crowns at the ends; it can't be made to sound bad | slab | the provocation every other panel has to beat; also the duet with a small player beside you |

**Push: SAIL, with idea 2 as its panel.** Kill candidate: STOPS as its own direction, since it's a dialect of SAIL rather than a different kind.

### Feel notes for systems (they belong to whichever concept wins)
- **Velocity as bow speed** needs no visual feedback: you hear each note bloom. Don't add per-key lights.
- **Opening the lid** should take one hand and stop with a firm click on the stays (CATHEDRAL's feel), followed by the lantern swelling up.
- **Octave change while holding** (systems' rule: a held note keeps its pitch): the knob needs a firm detent, so a stepped knob with a strong index.
- **SET:** a press you feel (a deep click), and its coral dot.

### Open questions
1. **Eng:** will a lid ≈ 20–24 mm deep hold a sealed box for a 50 mm driver plus a passive radiator? Can the speaker leads go through CATHEDRAL's hinge? Can a Hall sensor at the hinge switch power?
2. **Systems:** are the registers on/off (tabs) or levels? It changes the face of idea 2, not the map.
3. **Systems / eng:** what range does each octave control need (3 or 4 positions), and are organ feet the right words?
4. **Eng:** does a felt collar under each peg help per-key pressure (an FSR under it?) or blur it?
5. **Owner, later:** does "open = on" feel right, or does he want a separate power switch?
6. Is the lantern worth its mA and its parts? (It's delight, not a job.)
7. **Facts to check:** the Solina's register tabs and its three-phase ensemble (both from memory).

NEXT: design director — two designers have now pushed (BOW as the engine; SAIL plus the half-map as the face) and four directions each are on the table. The director should steer which ones go to concepts before we multiply them further.

---

## Turn 3: design director

### Real randomness (Python `secrets`, drawn this turn)
- **Oblique Strategy:** "Give way to your worst impulse" (9 of 30).
- **Unrelated field:** pipe organ building (12 of 25).
- **Twist:** "it must work with eyes closed" (1 of 10).

Tagged [worst], [organ], [eyes] below. (A stray first line of the script printed "25"; I ignored it and used the three named draws.)

### One fact checked
The 1974 Solina already split its registers by keyboard region: contrabass and cello only sounded on the lowest part of the keyboard (C2–G3), with viola, violin, trumpet and horn across the whole range, plus a separate bass volume slider. Its "crescendo" and "sustain length" sliders set attack and release, and its two effect buttons (modulation and phaser) affected all six sounds. Source: Zoë Blade's Solina guide (notebook.zoeblade.com). So **"each half has its own registers" isn't an invention; it's the Solina's own idea made movable.** That makes the half-map stronger, and it means we should say so rather than present it as new. The three-BBD, 120° ensemble is still unverified: systems, check it before anyone draws the lantern around it.

### Where the jam stands (my read)
The team agrees on the engine (structure B, every key its own VCA) and on one face (SAIL, the half-map). That's the problem. **We have one concept wearing four names.** BOW, SIX STRANDS, SAIL and STOPS are all the same answer: an orchestra of individually bowed notes, laid out by half, in CATHEDRAL's case. Concepts have to differ in kind, so pass 2 has to produce real rivals, not more features for this one.

The question I want the concepts to disagree on: **where does floss's life live?** Here are three answers that differ in kind.

### Three directions for concepts

**1. BOW: life lives in each finger** (keep; it's the lead)
Every note is its own player. This is turn 1's engine plus turn 2's SAIL face. Push it further:
- **The whole bow stroke is in the key, including the lift.** The Big Energy keys use a linear Hall sensor reading continuous travel (`eng/budget-variant.md` §v1.4b), so the firmware can time the release as well as the strike. A slow lift lets a note fade away; a quick lift cuts it off. Attack (velocity), sustain (pressure) and release (lift speed) per note, with no new controls. No string machine has done this, and it costs firmware only. Eng: confirm the release can be timed as cleanly as the strike.
- Velocity sets **speed**, not loudness, by default (agree with turn 1). Don't spend a switch on LOUD / SPEED / BOTH until the owner asks; Big Energy's VEL switch was the owner's own call there, and floss doesn't have to inherit it.

**2. WIND: life lives in a shared breath** [organ, new]
The opposite philosophy. An organ is not 25 soloists; it's one wind supply feeding every pipe. Hold one note and it speaks steadily. Hold ten and the wind sags a little, so the chord settles and breathes. Add the tremulant and everything shakes together. Applied to floss:
- **Turn 1's "many notes vs one" question (J15) stops being a compressor and becomes the character.** A modelled "wind" level, shared by every note, dips in loudness (and a few cents in pitch, if the owner wants it) as more keys go down and recovers when they lift. The more you play, the more it breathes. A harmonium or a reed organ does exactly this. It's warm, it's analog-feeling, and it answers his "shimmer and warmth" from a direction no current string synth takes.
- Velocity and pressure still work per note (the settled decision holds), but the *point of view* is collective: pressure could feed the wind (lean on any key and the whole instrument fills), which is the shared-strip fallback turned into a feature. If per-key pressure proves infeasible, WIND loses the least.
- **Wild card, probably weak, but I want it tried once [worst]:** the lid as a **swell box**. An organ's swell box is an enclosure with shutters, opened by a pedal for expression. If the lid holds the speaker (SAIL), the lid's angle, read by the hinge's Hall sensor, could set the overall swell: tilt it open and floss gets louder and brighter. You'd nudge it with the free hand while HOLD keeps a chord. My worry: you'd rarely move a lid mid-phrase, and it makes the outputs depend on furniture. If the visual designer can't make it feel natural in one sketch, kill it.
- **Keep the organ vocabulary out of the labels.** The owner's Big Energy rule is one plain word per label, and better words beat jargon. Feet (16' 8' 4'), "tremulant" and "stops" are jargon. The idea is organ; the words must not be.

**3. KEPT: life lives in history** [worst]
My worst impulse as a director is to say "just make a Solina." Taken seriously: **a deliberately faithful string-machine panel** (registers as tabs, a bass level, crescendo, sustain, ensemble, all in the order a Solina player knows) and **every innovation hidden under the fingers**: velocity, pressure, lift, the split. The panel is the smallest of the three; the keys are the newest. It's the most portable format (ONE SHEET slab, not a lid), and it's the honest version of DISH RACK: few controls not because of a gimmick but because 1974 already worked out what a string machine needs. It tests whether the owner wants floss to look new or to feel new. A conventional answer that turns out to be best is allowed to win.

### Push these (they belong to whichever concept they fit)
- **Two octave knobs are the split; no split mode** (turn 1, washing up). The best structural idea on the page. Turn 2's reading ("pointers parallel = one keyboard; apart = split; the angle is the interval") is excellent and works [eyes]: you can feel two knob pointers with your fingertips. Keep it in every concept.
- **Every half's controls sit over its half** (turn 2). It's organisational logic, which is the thing the owner pushed hardest on with Big Energy ("the items do not appear to be grouped or ordered in a way that makes logical sense"). Keep it as a rule across concepts.
- **Registers as tabs, not levels** [eyes]. A tab can be read by touch and from across a room; a level can't. But two identical rows of "cello · viola · violin" is six controls with three names. Systems, give a better answer in pass 2. Options: (a) the Solina's own answer (the low registers only play on the left half, so the rows aren't identical); (b) [organ] **registers as strands of pitch**: each key's tone at an octave below, at pitch and an octave above (maybe a fifth), softened toward a sine and mixed, which is exactly the Antiphon-style sine stacking the owner likes and costs a divide-down nothing; (c) three tabs that each pick L / both / R. Pick one per concept; concepts can differ here.
- **Signal order on the panel:** synth, then effects, then output, as the owner asked on Big Energy. Check the SAIL sketch's far row: depth (shimmer) sits in the middle with echo and reverb after it, which is right, but pressure sits among the synth controls and it's a modulation choice, not a sound source. Systems: where does the pressure selector live in that order?
- **The lid as the soundbox (SAIL).** It's the strongest form idea: real reuse of CATHEDRAL, a real reason for the shape, and a home for the passive radiator. Keep it for BOW. Eng questions are real (a 50 mm driver plus passive radiator in a lid ≈ 20–24 mm deep; a heavy lid tips the instrument backwards on a lap). At least one concept should use another format so the owner has a real choice.

### Drop these
- **ROUNDS and BELFRY as a direction.** Agreed with turn 2. The duet survives as a side effect of the half-map; don't build a concept around it.
- **STOPS as its own direction.** Merged into SAIL / KEPT.
- **BIG HANDS (the child's-hands face).** The child isn't in the owner's brief. Keep "fewest controls" only as the benchmark each concept's panel has to beat, which KEPT now carries.
- **LUTHIER (purfling, violin top).** Violin-top inlay is the cousin of the f-hole cliché turn 2 rightly threw out, and its sealed box fights the battery for the base. If a slab is needed, KEPT is the slab, built from the family's ONE SHEET without violin dress.
- **The six-fold rose as drawn.** The sketch's overlapping circles are the "flower of life" pattern, which reads as new-age decoration, not a cathedral's rose or a lute's. The owner said he'd draw CATHEDRAL's façade lines himself; give him the field, not a motif. If a rose survives, it's cut geometry worked out from the driver's size, not a stock symbol.
- **Five lighthouse rhythms on the status light.** Five patterns is a code you have to learn. Keep the economy (one light) and cut to three meanings anyone gets cold: steady = fine, slow pulse = charging, flashing = low battery. MIDI-clock flash and "knob not in control" go elsewhere or nowhere.
- **The lantern stays a maybe**, never a reason for a concept. Turn 2's rule (it never signals state) is right.
- **"SET" as the label.** The bell-ringing story is lovely and the word fails the owner's one-plain-word rule; call it what it does (hold). Also: why only the left half? In WIND the hold might latch everything. Decide per concept.

### Owner objections I can already see (so concepts answer them up front)
1. **"Are these analog voices?"** Structure B makes the tones in a microcontroller. Turn 1 is right that the Solina's tones were digital logic too, but the owner said "analog voices" first. Every concept needs one honest sentence on what's analog (VCAs, filters, the BBD ensemble) and what isn't.
2. **Off-centre.** 25 keys split as 12 + 13, so the split line (turn 2's coral thread) sits half a key left of the instrument's centre. The owner on Big Energy: "off center in that middle section is bad looking." Either the panel's axis honestly follows the split, or the line isn't drawn through the middle of the face. Visual: solve it, don't hide it.
3. **Jargon labels** (feet, cello / viola / violin used as switch names, SET). One plain word each.
4. **"Is this just a smaller CATHEDRAL?"** SAIL must earn its difference through the lid's job, not cloth and coral alone.

### Where I want pass 2 to land
Three concepts that differ in kind: **BOW** (each finger, SAIL lid), **WIND** (shared breath, format open, swell-box wild card), **KEPT** (history, ONE SHEET slab). Keep the shared rules (octave knobs as split, per-half controls over each half, tabs, one status light) common to all three so the owner is choosing a point of view, not a set of features. If the team thinks WIND and BOW are really one instrument with a switch, argue it in pass 2: that's the kill I'd most like to hear argued.

NEXT: product designer (systems focus) — WIND and KEPT are engine and behaviour questions first (the shared-wind model, lift speed per note, which registers each half has, the pressure selector's place in signal order), and the visual designer needs those answers before giving them faces.

---

## Turn 4: product designer (systems focus), pass 2

### One fact checked (closes the director's open check)
Sound on Sound's "More creative synthesis with delays" describes the classic string ensemble as **three modulated delay paths**, driven by **two LFOs (about 1 Hz and about 6 Hz)** that are phase-shifted to make modulation signals at **0°, 120° and 240°**. So the lantern can follow three phases honestly. Which BBD part to use is eng's question.

### 1. Are BOW and WIND one instrument with a switch? Yes, and it shouldn't even be a switch. Kill WIND as a concept.
- **Same hardware.** WIND's shared breath is one number in firmware, "how many keys are down", applied to every per-key amplifier (VCA) that structure B already has. Nothing in WIND needs a part BOW doesn't have, and the reverse holds too.
- So the honest answer is **one engine with two behaviours**. A switch would put a philosophy on a toggle, and the owner can't hear the difference until he's holding ten keys. That fails "earn its place".
- **What survives from WIND, in every concept:**
  - **The breath answers J15, with no control.** A fixed, mild sag: the sum grows roughly with the square root of the number of keys down, not linearly. One note isn't thin and ten don't clip. It recovers over about 200 ms as keys lift, so a chord "settles" a little. Pitch sag stays off. Owner question: is a fixed amount enough? (I think yes.)
  - **FILL becomes a pressure destination**: pressing any key fills the whole instrument. It's also what a shared pressure strip naturally does, so WIND's "loses least if per-key pressure fails" survives as the fallback.
  - **Swell-box lid: kill.** It makes loudness depend on where the lid happens to rest. Every time he sets floss down at a new angle he'd be asking why it got quieter. It also puts expressive force through the hinge, and nudging the lid mid-phrase shakes the speaker box. The lid's angle already changes the sound acoustically; that's enough.
- **WIND's slot needs a real rival that differs in kind.** I propose **TIDE**, below. Director's call.

### 2. TIDE: life lives in time (proposed rival for WIND's slot)
BOW's life is in the finger and KEPT's is in 1974. TIDE's is in **what happens after you let go**. It reworks turn 1's [speed] draw the other way: work at a *slower* speed than the player.
- **Every key's tone drifts on its own.** Structure B makes each key its own oscillator, so slow, independent detune per key is free in firmware: a held chord slowly beats against itself and never repeats. One knob, DRIFT, is the family's own control: Big Energy has DRIFT, fully left = rock steady.
- **HOLD latches the whole keyboard**, not just the left half. You lay a chord down, then your hands go to DRIFT, SHIMMER and the echo. You tend it like a garden; you don't perform it.
- **Release is long by nature.** Lift speed sets each note's tail (below), and in TIDE the range runs to tens of seconds.
- **Who it's for:** the park bench, drones, and the half of string-machine use that is pads under something else. Its format is open; it suits the slab or the lid.
- **The risk:** it overlaps with what the Daisy reverb and shimmer modes already do. TIDE has to stay analog-first (per-key drift, the BBD), or it's just a reverb with keys.

### 3. Lift speed per note (BOW): yes, firmware only, within limits
- The Hall sensor reads continuous travel, so the release is timed the same way as the strike: the time between two thresholds, now on the way up.
- **The limit:** the fast end is the Choc V2's spring return. Snatch your finger off and the key rises as fast as the spring allows. That's still clearly "short", but the fast end of the lift range is the spring's, not the player's. A slow lift is fully the player's (the finger rides the key up). The 2.8 mm travel at a 4–10 kHz scan (Big Energy's eng figures) should resolve it, but **eng must confirm with a test key**.
- **Behaviour:** RELEASE sets the range; lift speed places each note in it, mirroring how velocity places each note's attack inside SWELL's range. A latched (HOLD) note has no finger on it, so it uses the knob's value.
- So per note: **strike → attack time, lean → pressure destination, lift → tail.** No new controls.

### 4. Registers: a different answer per concept, so they really differ
- **BOW: strands of pitch** (director's option b). Each key gets three strands: an **octave below, at pitch, an octave above**, rounded toward a sine and mixed before that key's amplifier. That's Antiphon-style stacking.
  - **Tabs per half (6) are cheap here**, because turning a strand off for one half is just the firmware not generating it for those keys. No extra filters.
  - **Answer to "six controls with three names":** the two rows aren't redundant, because each row only acts on its own half's keys. Print the three names once, in the band between the rows, so the panel reads as three rows of names with one tab per half.
  - **Eng flag:** 25 keys × 3 strands is 75 tone outputs. That probably means a different tone source (shift-register outputs, a small FPGA or CPLD, or per-key mixing done digitally) rather than one MCU's pins. It's the biggest new risk in BOW.
  - **Why not a fifth:** with octaves set apart per half, a fifth stacked on chords quickly goes muddy. Leave it as an eng-cost option, not a tab.
- **KEPT: the Solina's own answer** (option a). Timbre registers (shared filters) on a shared bus, plus a **low register that only sounds on the left half**: the Solina's contrabass and cello region, made movable by the left octave knob. That's 3–4 tabs in one row, not two rows. The fact (from the director's check) goes in the concept's Why.
- **TIDE: no registers at all.** One TONE knob. The colour comes from drift and shimmer; it's the leanest of the three.

### 5. The pressure selector's place in the signal order
- **The hand is the first stage of the signal.** So the order is **TOUCH → strands / registers → TONE → SHIMMER → ECHO → REVERB → VOLUME.**
- **TOUCH holds SWELL (attack range), RELEASE (lift range) and the PRESSURE selector**: everything about how the keys respond. Big Energy grouped VELOCITY and AFTERTOUCH as "how the keys respond" for the same reason.
- PRESSURE's positions: **SWELL · VIBRATO** (per note) · **TONE · SHIMMER** (global, following the hardest-pressed key).
- **If per-key pressure fails** and floss gets a shared strip, the SWELL position quietly becomes WIND's FILL (the whole instrument swells). The label and the feel under the hand stay the same, so no panel change.
- I renamed BRIGHT to TONE so it names the knob it moves.

### 6. HOLD (renamed from SET, agreed)
- **Behaviour:** a latching toggle. When it's on, notes you play keep sounding after you lift. A new chord, played after every key is up, replaces the old one. Turning it off releases them, each with its own tail. There's no "armed" state, just on or off, and its dot shows it.
- **Scope per concept:** BOW latches the **left half only**, because the right hand's lift and pressure are BOW's point and HOLD would mute them. TIDE latches **everything**. KEPT latches the left half, the Solina-style bass region.
- **What pressure does to held notes:** nothing per note (no finger on them), but global destinations (TONE, SHIMMER) still act on them.

### 7. Off-centre split: a systems option for visual
- On a 25-key keyboard (C to C) the whites run 7 + 8, so the split line sits **9 mm left of centre** (126 vs 135 on the 270 mm key run).
- **Option: 24 keys (C to B).** That gives 7 + 7 whites and puts the split exactly on the axis. The body is 18 mm narrower. It's within "25 or fewer". What it costs: the top C, a different key strip from the family's 25, and a chord-top note players miss. **I wouldn't choose it for symmetry alone.** I'd let the axis follow the split (visual's option). Listed so the owner sees the trade.

### 8. The honest "analog voices" sentence (for every concept)
> floss's tones start in a microcontroller, one per key, the way the 1974 Solina's started in divider chips. Everything that shapes them is analog: each key's own amplifier, the strand mix, the tone filter and the bucket-brigade ensemble. The Daisy modes, echo and reverb are digital, and each is a choice you can switch off.

### Sharpen / kill summary
| Idea | Call |
|---|---|
| WIND as a concept | **Kill.** One engine; breath fixed, FILL as a pressure position |
| Swell-box lid | **Kill** |
| TIDE | **Propose** for the third slot |
| Lift speed per note | **Keep** (BOW); eng to test the spring-return limit |
| Strands of pitch | BOW's registers; eng flag: 75 tone outputs |
| Solina-style low-left register | KEPT's registers |
| Fifth strand | Drop (cost option only) |
| HOLD scope | Per concept: BOW left, TIDE all, KEPT left |
| 24 keys | Owner-visible option, not my recommendation |

### Open questions (new)
- Eng: 75 tone outputs for strands; the lift timing at the spring's return speed; BBD part (3 delay paths).
- Owner (later): is a fixed breath sag fine? Does he miss "louder with every key"?
- Director: TIDE or keep WIND?

NEXT: design director — WIND's slot needs a decision (my kill and TIDE as the rival) before the visual designer gives three concepts their faces.

---

## Turn 5: design director, pass 2

### Real randomness (Python `secrets`)
- **Oblique Strategy:** "Listen to the quiet voice" (16 of 20). Used on TIDE below [quiet].

### 1. The third slot: WIND is dead, TIDE goes forward, on one condition
- **WIND: killed. I agree with systems.** A point of view the owner can't hear until he's holding ten keys, and which needs no part BOW lacks, isn't a concept. The fixed breath (square-root sum, ≈ 200 ms recovery, no pitch sag) goes into every concept, and FILL becomes the shared-strip fallback. The swell-box lid is killed too, for the reasons systems gave (loudness depending on where the lid rests).
- **TIDE takes the slot.** It does differ in kind: BOW is played, KEPT is remembered, TIDE is *tended*. The player lays notes down and then works the sound, not the keys. That's a real way people use string machines (pads, drones, the park bench), and none of the other two serve it first.
- **The condition: TIDE can't make the settled innovations idle.** As written, HOLD latches everything and your hands leave the keys, so velocity and per-key pressure (both the owner's own asks) do nothing in TIDE's main moment. That's an objection he'd raise in the first minute. Fix: **each note remembers how you played it.**
  - **[quiet] Velocity is inverted in meaning, not wiring: the softest strike makes the longest, most wandering note.** A barely-touched key fades in slowly, drifts the most and keeps the longest tail; a hard strike is present, steadier and shorter. In TIDE the quiet voice is the one that lasts. That's the opposite of BOW (where hard = fast bite), which is exactly the kind of difference the owner should be choosing between.
  - **Pressure while laying a note down sets how far that note will drift once it's held,** and HOLD keeps it. You plant each note with its own character, then tend the whole.
  - So TIDE still uses strike, lean and lift per note; it just spends them on the future of the note rather than its present.
- **DRIFT is TIDE's hero control.** In BOW and KEPT drift is fixed and small (the per-key oscillators give it nearly free); only TIDE puts a knob on it. That keeps the three apart instead of sharing one panel with different paint.
- **TIDE's risk (systems named it):** it overlaps with the Daisy's reverb and shimmer modes. It has to stay analog-first: per-key drift and the BBD ensemble carry it, and its default shimmer mode is the analog one.

### 2. What goes to concepts (not READY yet; that's after the visual designer's pass-2 turn)
| Concept | Life lives in | Velocity means | Registers | HOLD | Format (proposed) |
|---|---|---|---|---|---|
| **BOW** | each finger | hard = fast bite, soft = slow bloom | strands of pitch: octave below, at pitch, octave above; 6 tabs, names printed once between the rows | left half | SAIL: CATHEDRAL base, lid as soundbox |
| **KEPT** | 1974 | the Solina's crescendo, made per-note | the Solina's answer: timbre tabs on one row, plus a low register that sounds only on the left half | left half | ONE SHEET slab |
| **TIDE** | time | soft = longest and most wandering | none; one TONE knob | whole keyboard | open. Visual: either a third format, or argue why it shares one |

Shared across all three: the two octave knobs are the split; each half's controls sit over that half; the TOUCH group (attack range, release range, pressure selector) first in signal order; the fixed breath; lift speed sets each note's tail; one status light with three meanings; the honest "analog voices" sentence from turn 4, which I accept as written.

### 3. Push
- **Lift speed per note: keep in all three**, with systems' honest limit (the fast end belongs to the Choc's spring). Test key first.
- **Signal order TOUCH → registers → TONE → SHIMMER → ECHO → REVERB → VOLUME:** agreed. It's the owner's synth → effects → output rule, extended back to the hand. Visual: make the panel read in that order, left to right or near to far, whichever the half-map allows.
- **Strands of pitch in BOW:** keep. It's the most Antiphon-like idea we have, and it's what "floss" (strands) actually means. But **the 75 tone outputs is now BOW's biggest risk**, and it's eng's to size before concepts are scored. If it needs an FPGA or CPLD, the concept should say so plainly; that's a build-skill question for the owner, who builds these himself.
- **Names of strands:** one plain word each, and not feet. Something like "low · root · high" or "under · main · over". Visual and systems: pick and test cold.

### 4. Drop or fix
- **Fix a word clash in turn 4:** SWELL names both the attack-range knob and a pressure position. Two controls, one word: the owner would catch it. Rename one (e.g. the knob is ATTACK, or the pressure position is LOUD). Same check for TONE, which turn 4 now uses for a knob and a pressure position. That one I'll accept, because the position literally moves that knob's parameter; say so on the panel's map, not on the face.
- **The fifth strand:** dropped, agreed.
- **Pitch sag in the breath:** off, agreed. Keep it off the owner's question list unless he asks.
- **24 keys:** I agree with systems. Keep 25: the family's key strip, the top C for chord tops, and "25 or fewer" doesn't ask for 24. **Visual owns the off-centre problem:** show the panel with its axis honestly following the split (the split line as the axis of the control layout, the case asymmetric by 9 mm on purpose, or the line not drawn through the face at all). 24 keys goes to the owner as one sentence of trade, only if the visual answer doesn't convince me.
- **Lantern:** now honest (three phases verified by systems, Sound on Sound). Still a maybe, still never a state signal. It fits TIDE best of the three, since TIDE is the one you watch.

### 5. What keeps nearly going wrong (no scores yet, so it isn't a 9-blocker list; it's a pattern)
- **Convergence.** Twice now the team has drifted toward one instrument under several names (pass 1: BOW/SAIL/STRANDS/STOPS; pass 2 nearly folded WIND into BOW with a switch). Why: structure B is so flexible that every philosophy becomes "firmware on the same engine". The guard is the table above: each concept must differ on what velocity *means*, which registers exist, what HOLD covers and which format it lives in, not just on labels.
- **Settled asks going idle.** TIDE as first written made velocity and pressure pointless. Every concept must show where strike, lean and lift matter.

### 6. Owner questions to hold for later (not now)
- Is a fixed breath right, or does he miss "louder with every key"?
- If BOW needs an FPGA/CPLD for its strands, is that within what he wants to build?
- 25 keys off centre by 9 mm vs 24 keys on centre (only if visual can't resolve it).

NEXT: product designer (visual focus) — the visual designer hasn't had a pass-2 turn yet, and this pass ends after it. Faces for BOW, KEPT and TIDE (formats included), the off-centre split resolved visually, and plain strand names.

---

## Turn 6: product designer (visual focus), pass 2 (last jam turn)

Sketch: `sketches/visual-jam2-faces.png` (source `sketches/visual_jam2.py`). It's rough: proportions and positions are placeholders for systems' layout.

### Randomness
No new draw this turn. The director's "Listen to the quiet voice" already shapes TIDE, and every direction now has its point of view. A fresh card would only add features. What I took from it is the TIDE face below: the quietest body for the quietest concept.

### 1. The off-centre split: solved, with one honest compromise
**The geometry the problem misses:** 25 keys from C to C are **7 whites, then middle C, then 7 whites.** Middle C is the centre key, so **the case's axis runs through the middle of middle C**. The split (between B and middle C) is its left edge, 9 mm left of centre.

**The answer: a gutter exactly one key wide, centred over middle C.**
- The left half's controls fill **126 mm over C–B**, and the right half's fill **126 mm over D–C**. That's the same width each side of an 18 mm gutter on the axis, so the face is symmetric.
- The left edge of the gutter is the true split. No line is drawn through the face.
- **The gutter carries what both halves share:** the status light (the family's axis rule: FOLD's brass pin, CATHEDRAL's axis), BOW's strand names, and TIDE's whole-keyboard HOLD and its hero, DRIFT. So the axis means something; it isn't just empty space.
- **The only split mark is a short coral tick on the front rim between B and C**, where the hand and the eye already are. It's tiny and at the keys, not a line across the panel.
- **The compromise, said plainly:** middle C belongs to the right half (the right octave knob moves it), but its key sits under the gutter, not under the right group. The coral tick tells you which side it's on. In continuous mode (both octaves the same) it doesn't matter at all. **Director: judge whether the tick is enough.** If it isn't, the fallback is 24 keys, as one sentence of trade for the owner.
- **Rejected:** a line through the face (that's the off-centre he dislikes); keys shifted 9 mm (makes the case 18 mm wider, or makes the keys off-centre instead); a case asymmetric on purpose (at 9 mm it reads as a mistake, not a decision).

### 2. Three faces: three of Big Energy's own bodies
**The key move:** each concept takes **a different body the family already has**. The owner chooses a point of view and a body at once, every option is reuse, and they can't drift back into one instrument (the director's convergence worry). The faces also differ in the keys, the hero and the material, not just the labels.

**One rule across all three: coral marks where the life lives.** One coral control per concept, and it's a different control each time.

| | **BOW** | **KEPT** | **TIDE** |
|---|---|---|---|
| Body | **CATHEDRAL**'s walnut case; the lid is the soundbox (SAIL) | **ONE SHEET**: one printed cream shell ("if it turns, it ripples") | **HUSH**: a felt-skinned printed pebble, grey wool, every word pressed blind |
| Keys | **dark naturals, bone sharps**: a bowed instrument's ebony fingerboard and bone nut. Felt collars, so a lean gives | **white and black**: the only one that looks like an ordinary keyboard, because KEPT's innovation is hidden | **HUSH's pale maple pegs on felt collars** |
| Coral (the life) | **pressure**: what a lean does | **ensemble**: the 1974 soul | **drift**, large, on the axis |
| Panel | half-map; the strand tabs stand in two columns of three either side of the gutter, names printed once in it; far row in signal order | one row of tabs in the Solina's order; the bass tab sits over the left half, because it only sounds there | the fewest controls; no registers; HOLD is a **maple peg on its own felt collar** on the axis, because you press it like a key and it holds every key |
| Speaker | the lid's cloth; plain, no motif | a slotted grille across the back band (ONE SHEET's language) | punched holes in the felt; **the lantern glows through the same holes as the sound** |
| Lantern | none | none | yes: TIDE is the one you watch |
| Passive radiator | yes: the lid's sealed box | **probably not**: the slab's volume is shared with the battery. An honest trade: the smallest body gives up the fullest sound unless eng finds the volume | the pebble's domed underside is the sealed box; eng to check which way the radiator fires (into a lap is bad) |

**BOW, in a sentence:** a dark-keyed, walnut-and-cloth instrument whose lid sings at you. It answers "just a smaller CATHEDRAL?" with the lid's job (no controls; it's the voice) and with its keys (dark naturals, never brass).

**KEPT, in a sentence:** it looks like a string machine from 1974, slimmer than anyone expects, and plays like nothing from 1974. It's the most conventional face, so it has to be the best-made: ONE SHEET's economy, one filament, ripples only where something turns.

**TIDE, in a sentence:** a soft grey stone you set on a bench, plant a chord in, and watch breathe, with warm light coming out of its speaker holes as the chord drifts. It's the quietest body for the quiet voice.

### 3. Words (the director's clashes, plus the strand names)
- **SWELL clash: rename the knob, not the pressure position.** The knob becomes **attack**, which pairs with **release**. Both are plain and standard, and velocity places each note inside them. **swell** stays as a pressure position, because swelling is what bow pressure does. TONE in both places is accepted (the director's ruling); the manual says why.
- **Pressure positions:** *swell · vibrato · tone · shimmer.*
- **Strand names (BOW):** heading **strands** (it's literally what floss is), positions **low · main · high**. Cold test: "strands: low, main, high" reads as three layers from low to high. "root" fails, because to a musician it means a chord's root, not the key you pressed. "under / over" is cute but vague. Under a heading, "low" can't be mistaken for an EQ band.
- **Octave positions: numbers, not feet**, for example *−1 · 0 · +1 · +2* (the range is systems'). Numbers make the parallel-pointer reading precise: the difference between the two numbers is the interval.
- **KEPT's tabs: bass · strings · brass** (the Solina's six names collapse into what they sound like; it had trumpet and horn, which is brass). This is my proposal; systems and eng own how many there are.
- **KEPT keeps the Solina's order, not its words:** attack and release, not "crescendo" and "sustain length". Its "sustain" would clash with what every synth means by sustain.

### 4. Dropped this turn
- **The rose window, in any form.** The director was right that the drawn pattern is the "flower of life". A cut rose sized from the driver would still be a motif on a cloth lid that needs no hole. BOW's lid stays plain cloth plus one coral thread. The lid's back stays a blank field for the owner's own façade lines.
- **The coral line through the face.** Replaced by the gutter and the rim tick.
- **The lantern in BOW and KEPT.** It lives only in TIDE.
- **Five lighthouse rhythms.** Cut to the director's three: steady = fine, slow pulse = charging, flashing = low battery. The light sits on the axis in every concept.
- **Organ feet, "SET" and orchestral switch names.** All gone (section 3).
- **My earlier BOW key idea (maple heads).** Maple went to TIDE, where HUSH's pegs belong. BOW's dark keys keep the three apart.

### 5. Open questions
1. **Director:** is the rim tick enough to show that middle C belongs to the right half? (If not: 24 keys as an owner trade.)
2. **Systems:** does the stacked strand column (three tabs deep) fit in CATHEDRAL's base depth, behind the keys and in front of the far row? If not, the tabs go side by side and the names go above each group.
3. **Eng:** KEPT's sealed volume (radiator or not); TIDE's radiator direction; BOW's lid box (from turn 2); and whether the lantern's light through the felt holes reads in shade (it won't in sun).
4. **Owner (later):** BOW's dark naturals with pale sharps. He was asked about reversed key colours on Big Energy and hasn't answered yet.
5. **Systems / eng:** KEPT's tab count and names.

NEXT: design director — the jam is closed. Three concepts now have engines (systems' turns) and faces (this turn), and the off-centre answer needs the director's ruling before we build the concept folders.
