# floss: jobs and flows

## The jobs, short (for the owner: anything wrong or missing?)

floss is a sound module you play from a small MIDI keyboard you carry with it. **new** = a job added in this revision; **changed** = reworded in this revision (rev 3).

1. Play warm, shimmering string chords anywhere: battery, built-in speaker, no setup.
2. Plug any travel keyboard into floss's USB-C port with one cable and play: floss powers it, and any standard USB MIDI keyboard works, not one model. **changed**
3. Carry floss and a travel keyboard together as one kit, cable included, without damage, in a backpack comfortably. The kit holds the keyboard by its ends, never across its keys, takes any slim travel keyboard (325–388 mm wide), and still packs neatly with no keyboard in it. **changed**
4. Play as many notes at once as my keyboard can, every note sounding.
5. Split the keyboard on floss and set each half's octave on floss's knobs; set both the same and it's one keyboard.
6. Know where the split lands on the keyboard I brought: floss splits at a fixed note, shows where that falls with a brass marker, and says "keep the keyboard at its home octave". (inferred) **changed**
7. Shape each note by how hard I strike it.
8. Lean into notes I'm holding, and choose what leaning does, per note when my keyboard sends it.
9. Still play expressively with a keyboard that has no pressure: its mod wheel, strip or button takes over the lean. (inferred) **changed**
10. Use my keyboard's extra moves (tilt, bend, release speed) where it has them. (inferred)
11. Choose the tone colour (which octave layers sound), for each half. (inferred) **changed**
12. Choose the shimmer, analog ensemble or a digital mode, and how much.
13. Add echo and reverb; the echo follows MIDI tempo when there is one, and I can tap a tempo when there isn't.
14. Hold a chord or drone without holding the keys, building it a note at a time and pulling notes out, and keep it sounding even if the keyboard is unplugged. (inferred) **changed**
15. Hear it on the speaker; plug in headphones and the speaker goes quiet.
16. Play floss from a computer or from another keyboard, including a full-size one at home.
17. Use it with other gear over MIDI: play other things from it, split the halves onto two channels or not, and send velocity and pressure.
18. Read everything from floss's panel, with no screen, by eye or by touch, including the split, whether the keyboard is connected and whether notes are arriving. **changed**
19. Switch on with one switch and be playing within seconds, keyboard included; know the battery and the charging. (inferred) **changed**
20. Take the kit to the park and play on a bench or my lap, in sun or shade. (inferred)
21. Lots of notes don't distort, and one note doesn't sound thin. (inferred)
22. Play in tune with other instruments.
23. Share it: a friend holds the keyboard beside me on its cable while I work the knobs. (inferred) **changed**
24. See one clear point of view in the object, keyboard included, and want to play it.
25. Belong to the same family as Big Energy: same case family, parts and way of building.
26. Build it myself from proven parts and proven crafts (case, cloth, hinges), knowing every making step before I start, and open it up to fix it. **changed**
27. Swap to a different keyboard whenever I like (another model, a broken one replaced, one that goes out of production) and the plugging in and carrying still work.
28. Use the same way of carrying and connecting a keyboard on every portable sound module we build. Each module is sized by its own parts; the carry takes the keyboard. **changed**
29. When floss is silent, find out why from floss itself: no keyboard, keyboard not powered, notes not arriving, volume down, or a half turned off. (inferred) **new**
30. A module about the length of a sheet of paper, in a shape with a deliberate proportion, not necessarily a rectangle. **new**

The plan for every synths-to-go instrument: a portable sound module with a way to carry a keyboard with it, not tied to any one keyboard model.

---

Status: **rev 3, 2026-11-22**, product designer (systems focus). It follows the closed module jam (`jam-module.md`, turns 1–6 and the director's addendum) and the owner's direction at 13:25 ("The module does not have to match keyboard width") and 13:29 ("It needs to fit in a backpack comfortably. Ideally like the size of a sheet of paper length wise. But it also does not have to be a rectangle. It should be a thoughtful ratio base"). Rev 2 (12:26, the module shape) and rev 1 (built-in keys) are superseded.

**"Inferred"** means the owner didn't say it. A concept may answer an inferred job weakly but must say so. A stated job a concept can't do sends it back.

## What changed from rev 2, and why
| Job | Change | Why |
|---|---|---|
| 2 | Host port is **USB-C**, on the module's keyboard-facing edge | Owner 12:52 ("Let's do USB c"); jam S2 |
| 3 | Held **by the ends, nothing across the keys**; slim range 325–388 × 83–135 × 11–16; packs neatly **empty**; **backpack comfortably**; one place for the cable | Director turn 3 (orchestral-case end blocks); systems turn 1; owner 13:29 |
| 3 | Chunky minis play but aren't carried, except by CLOTH | eng trade-off 2, still the owner's call |
| 6 | Rule: **fixed split B3 \| C4, a brass target shows where it lands**, "keep the keyboard at its home octave" engraved | Director ruling (turn 3); a learned split per keyboard was rejected (invisible state) |
| 9 | The lean ladder: poly AT → channel pressure → CC1 → nothing | Systems turn 1 §4.3, accepted |
| 11 | Colour per half = octave layers (strands: low · main · high) | The one voice (turn 4, accepted turn 6) |
| 14 | **Plant and tend:** add notes, re-strike to pull one out, held notes survive the keyboard | The one voice. Its scope (all, or the left half when split) is an owner proposal |
| 18 | Adds the **port light** (connected, blink per note, fault) and the brass target | Turn 3 rulings |
| 19 | **One power switch**, on the module | Turn 3 ruling 5 |
| 23 | The cable is 0.3–0.5 m [eng `module-r2.md`]: a friend beside you; an optional coiled cable for a separate lap | Systems turn 1; `module-r2.md` §6 |
| 26 | Every concept **lists its non-electronic making steps** with the craft and a source; a step needing trial or measuring says so | Director, turn 6 §4 item 11 |
| 28 | **Module sized by its own parts; the carry takes the keyboard.** The family standard fixes interfaces (S1–S7), not a module size | Owner 13:25: S8 ("400 wide") not adopted |
| 29 | **New:** why is it silent? | Systems turn 1; director ruling 6 |
| 30 | **New:** paper length, deliberate ratio, any shape | Owner 13:29; T4 updated |

## Jobs in detail
| # | Job | Source | What a concept must show |
|---|---|---|---|
| 1 | Strings anywhere | stated | sounds like strings on its own speaker from battery, with only the keyboard plugged in |
| 2 | One cable, floss powers the keyboard, any class-compliant USB MIDI keyboard | stated (owner 12:26, 12:28, 12:52) | a **USB-C host port on the module's keyboard-facing edge**, current-limited 5 V (≈ 550–600 mA [eng]); works with the K-Board C, Xkey 25 and velocity-only keyboards; cold socket (VBUS only when a keyboard is detected); cable 0.3–0.5 m, C-to-C, or the keyboard's own cable on **one C-plug-to-A-receptacle adapter** carried in every kit [`module-r2.md`] |
| 3 | Carry module + keyboard + cable as one kit, in a backpack | stated ("carried with the module"; "not reliant on a single model"; 13:29 "fit in a backpack comfortably") | where the keyboard, module and cable go packed; **held by the keyboard's ends, nothing across a key**; takes 325–388 wide, 83–135 deep, 11–16 tall (eng's slim class; end blocks: 8 mm in, 32 mm travel each, ≈ 404 inside); **packs with no keyboard** (blocks lock, nothing rattles); the cable path accepts a socket **anywhere along the keyboard's rear edge or either end** (≈ 25–35 mm for a straight plug; ≥ 15 mm notch in each end block [`module-r2.md` §6]); one pocket for the cable and adapter; closed size and weight (T5) beside a backpack's main compartment. Chunky minis: CLOTH only, unless the owner says otherwise |
| 4 | Every note sounding | stated (T1) | 25 voices: **12 serve the left half, 13 the right**; oldest stolen within a half; a 25-key keyboard played live never steals |
| 5 | Split and octaves on floss | stated (settled) | OCTAVE L and OCTAVE R; equal = one keyboard; a held note keeps its pitch through an octave change |
| 6 | Where the split lands | inferred | split fixed at B3 \| C4 (note 59 \| 60); a **brass target** on a graduated rail, set once over the keyboard's B \| C; "keep the keyboard at its home octave" engraved by it; one line on why floss can't know which key is which (it only receives note numbers) |
| 7 | Velocity per note | stated (settled) | **velocity = speed**: soft bows in slowly, hard speaks at once, inside ATTACK's range |
| 8 | Pressure per note, selectable | stated (settled) | the PRESSURE selector (swell · drift · tone · shimmer); per note with poly AT / MPE; on every note with channel pressure |
| 9 | Expressive with no pressure | inferred | the lean ladder: poly AT / MPE → channel pressure → **CC1** → nothing; the panel doesn't change |
| 10 | Tilt / bend / release speed | inferred | bend ±2 semitones (per note with MPE); release velocity sets the tail where sent, RELEASE's value where not |
| 11 | Colour per half | inferred | three strand tabs per half (low · main · high); all off = that half silent (a mute, visible) |
| 12 | Shimmer | stated (settled) | analog BBD mode + Daisy modes; DEPTH (coral, on the axis); fully off possible |
| 13 | Echo, reverb, tempo | stated (Big Energy rules); tap inferred | ECHO (level and repeats together), TIME, FREE / SYNC, TAP; REVERB (decay grows with amount); clock from USB or TRS |
| 14 | Hold | inferred | HOLD **plants**: notes add, a re-strike pulls one out (its velocity sets the fade); off = all fade; **held notes survive an unplug**; CC64 = ordinary sustain on every note. **Owner proposal:** HOLD plants everything when the octaves are equal, the left half only when they differ |
| 15 | Speaker; headphones mute it | stated (settled) | as rev 1 |
| 16 | Play from a computer or another keyboard | stated in part | USB-C device port and TRS in both play floss; host and device at once is unverified [eng], with TRS to the computer as the fallback |
| 17 | MIDI out to other gear | stated (settled) | re-sends notes, split onto channels 1 / 2 when MIDI SPLIT is on, with velocity and pressure |
| 18 | Read the state, keyboard included | stated (no screens); connection inferred | knob and tab positions are the state; **port light** beside the host port: off / steady (connected) / a blink per note received / fast flash (power fault); **status light**: steady fine / slow pulse charging / flash low battery; the brass target |
| 19 | Playing within seconds | inferred | **one power switch on the module**; power on → keyboard powered → play, no pairing |
| 20 | The kit in the park | inferred (T2) | open on a bench and **on a lap**; the cable doesn't cross hands, speaker or panel; readable in sun |
| 21 | Many notes vs one | inferred | the fixed breath |
| 22 | In tune | stated (T9) | TUNE trim on the rear wall; ±3 cents |
| 23 | Share it | inferred | on the 0.3–0.5 m cable the friend sits beside you holding the keyboard (an optional coiled cable reaches a separate lap); you hold the module; a second keyboard via TRS in, with MIDI SPLIT giving each player a half |
| 24 | Point of view, keyboard included | stated (Big Energy J20) | the kit owns the outline and hosts the keyboard (visual rule); the module has its own face |
| 25 | Big Energy family | stated (settled) | as rev 1 |
| 26 | Build from proven parts and crafts; fix | stated (reliable choices; measures nothing) | parts with published specs; **every non-electronic making step listed with its craft and a source**; steps that need trial or measuring are named; battery, firmware flash and host port reachable |
| 27 | Swap keyboards | stated | nothing in floss depends on one keyboard's size, socket or features; the carry takes the whole slim range |
| 28 | One carry-and-connect system for every module | stated (12:28; 13:25) | the carry and connection are **family interfaces**: S1 keyboard envelope, S2 host port, S3 cable, S4 two ¼"-20 inserts, S5 plug behaviour, S6 CC map, S7 split rule and target. The keyboard bed and end blocks are family parts. **Module size is each instrument's own** |
| 29 | Why is it silent? | inferred | from the panel alone: port light off (no keyboard / no power), steady with no blink (notes not arriving: dead keyboard or charge-only cable), blinking (notes arriving: check VOLUME, the strand tabs, headphones) |
| 30 | Module size and shape | stated (13:29; T4) | the module's long side ≈ a sheet of paper (Letter 279 / A4 297 mm); a **stated ratio** the proportions come from; any outline, provided the controls, ports and speaker fit (sealed TEBM28C10-4B, body ≈ 32, ≈ 40 at the rim [`module-r2.md`]). Concepts propose 297 × 105, 2√2 : 1 (module file §2) |

**Settled constraints:**
- no built-in keys; no screens or encoders; battery; echo and reverb on the Daisy;
- the keyboard carried with it is 25 keys or fewer;
- **the module is sized by its own parts, not the keyboard's width** (13:25);
- no fixed budget, costed honestly;
- targets T1–T12 are the baseline (T4 as updated 13:29), and any miss or beat is a trade-off for the owner.

## Flows

### F1 Grab and play (1, 2, 19)
1. Open the kit.
2. Plug the keyboard's cable into floss's USB-C host port (any order).
3. Switch floss on (the one switch). The status light goes steady; the port light goes steady when the keyboard answers.
4. Play: the port light blinks with each note.
- **States:**
  - no keyboard → port light off; floss still plays from USB-C or TRS;
  - the keyboard draws too much → floss cuts its power, the port light flashes fast, floss keeps running;
  - unplugged mid-chord → unheld notes fade on their tails, held notes keep sounding.

### F2 Make a split (5, 6, 18)
1. Both OCTAVE knobs equal: one keyboard.
2. Turn OCTAVE L down: the lower half plays lower.
3. A held note keeps its pitch through the change.
4. Set the brass target over the keyboard's B | C once (it stays there until a different keyboard comes in).
5. If the keyboard's own octave buttons move it, the split moves on the keys. The engraved line says why.

### F3 Play expressively (7, 8, 9, 10)
1. Strike: velocity sets how fast the note speaks.
2. Lean: poly AT / MPE → that note; channel pressure → every note; CC1 → every note; nothing → velocity still works.
3. Tilt or bend: pitch.
4. Lift: release velocity sets the tail if sent.

### F4 Choose what pressure does (8, 9)
PRESSURE: swell · drift · tone · shimmer. A full lean on drift becomes vibrato.

### F5–F7 Colour, shimmer, echo and reverb (11, 12, 13)
Strand tabs per half; SHIMMER mode and DEPTH; ECHO, TIME, FREE / SYNC, TAP, REVERB.

### F8 Plant and tend (14)
1. HOLD on.
2. Play notes: each joins the held set.
3. Strike a held note again: it fades (a soft re-strike = a long fade).
4. Hands off; tend the knobs.
5. HOLD off: everything fades on its own tail.
- Scope (owner proposal): split → left half only; one keyboard → everything.

### F9 Go private (15)
As rev 1.

### F10 Play from elsewhere (16, 17)
1. **Computer:** over USB-C.
2. **Another keyboard:** TRS in.
3. **Both with the USB keyboard:** notes merge (if eng confirms host and device together).
4. **MIDI SPLIT** (rear switch): channels 1 / 2.

### F11 Power (19, 20)
1. Charge over USB-C; play while charging.
2. Low battery is shown first.
3. The keyboard is powered only while floss is on.

### F12 Pack and carry (3, 20, 27)
1. Switch off.
2. Unplug, coil the cable (and adapter) into the kit's pocket.
3. Keyboard into its place, held by the ends (end blocks set to the same number on the scale).
4. Close.
5. Into the backpack.
- **With no keyboard:** blocks locked, the kit closes the same way.

### F13 The park (20)
1. Sit; open the kit on the bench or your lap.
2. The cable stays in its path.
3. Play within a minute.

### F14 Share (23)
The friend takes the keyboard beside you (0.3–0.5 m cable; a coiled one for a separate lap); you keep the module.

### F15 Swap the keyboard (27, 28)
1. Plug in another class-compliant keyboard; it plays.
2. Re-set the end blocks and the brass target.
- Its features change what pressure does, and nothing else.

### F16 Build and fix (26)
Parts and making steps listed per concept; host port, battery and flash reachable.

### F17 Why is it silent? (29)
1. **Port light off:** no keyboard, or not powered → re-plug; a fast flash = it draws too much.
2. **Steady, no blink on a key:** notes aren't arriving → another cable (charge-only cables carry no data) or another keyboard.
3. **Blinking:** notes arrive → VOLUME, the strand tabs (all off = silent half), headphones plugged in.

### F18 Keyboard missing (1, 16, 27)
1. The kit still packs.
2. Play from a computer or TRS.
3. A chord planted before the keyboard left keeps sounding; tend it.

## Open questions
1. **Eng (after `module-r2.md`):**
   - host and device at once;
   - fixed voice pools per half;
   - the speaker box on the module's axis with a U-shaped board;
   - each slim keyboard's default lowest note;
   - coiled-cable products.
   - **Owner trade-offs from r2:** sealed / ported / passive radiator (radiator not recommended); body 32 / 40 mm; **T5 missed with an Xkey 25 in every kit**; cold-socket vs always-on VBUS.
2. **Concepts:**
   - the module's ratio and outline (job 30, a joint systems / visual call);
   - where the module sits against the keyboard, open and packed, per kit.
3. **Owner (with the concepts):**
   - board, book or cloth;
   - the split-scoped HOLD;
   - a charger in the kit;
   - slim keyboards only or all sizes.
