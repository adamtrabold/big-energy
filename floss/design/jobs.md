# floss: jobs and flows

## The jobs, short (for the owner: anything wrong or missing?)

floss is now a sound module you play from a small MIDI keyboard you carry with it. **new** = a job the module creates; **changed** = reworded since the last list.

1. Play warm, shimmering string chords anywhere: battery, built-in speaker, no setup.
2. Plug in any travel keyboard with one cable and play: floss powers it, and any standard USB MIDI keyboard works, not one model. **new**
3. Carry floss and a travel keyboard together as one kit, cable included, without damage, and the carry fits any travel keyboard in a size range, not one model. **new**
4. Play as many notes at once as my keyboard can, every note sounding. **changed**
5. Split the keyboard on floss and set each half's octave on floss's knobs; set both the same and it's one keyboard. **changed**
6. Pressing the keyboard's own octave buttons doesn't break the split. (inferred) **new**
7. Shape each note by how hard I strike it.
8. Lean into notes I'm holding, and choose what leaning does, per note when my keyboard sends it. **changed**
9. Still play expressively with a keyboard that has no pressure. (inferred) **new**
10. Use my keyboard's extra moves (tilt, bend, release speed) where it has them. (inferred) **changed**
11. Choose the tone colour (which sounds or layers play), per half where it makes sense. (inferred)
12. Choose the shimmer, analog ensemble or a digital mode, and how much.
13. Add echo and reverb; the echo follows MIDI tempo when there is one, and I can tap a tempo when there isn't.
14. Hold a chord or drone without holding the keys. (inferred)
15. Hear it on the speaker; plug in headphones and the speaker goes quiet.
16. Play floss from a computer or from another keyboard, including a full-size one at home. **new**
17. Use it with other gear over MIDI: play other things from it, split the halves onto two channels or not, and send velocity and pressure.
18. Read everything from floss's panel, with no screen, by eye or by touch, including the split and whether the keyboard is connected. **changed**
19. Switch on and be playing within seconds, keyboard included; know the battery and the charging. (inferred) **changed**
20. Take the kit to the park and play on a bench or my lap, in sun or shade. (inferred) **changed**
21. Lots of notes don't distort, and one note doesn't sound thin. (inferred)
22. Play in tune with other instruments.
23. Share it: a friend plays the keyboard while I work the knobs. (inferred) **changed**
24. See one clear point of view in the object, keyboard included, and want to play it. **changed**
25. Belong to the same family as Big Energy: same case family, parts and way of building.
26. Build it myself from proven parts, and open it up to fix it. **changed**
27. Swap to a different keyboard whenever I like (another model, a broken one replaced, one that goes out of production) and the plugging in and carrying still work. **new**
28. Use the same way of carrying and connecting a keyboard on every portable sound module we build. **new**

The plan for every synths-to-go instrument: a portable sound module with a way to carry a keyboard with it, not tied to any one keyboard model.

Dropped since the last list: the built-in keys themselves. "Shape how each note ends by how I lift off" is now part of job 10, because only some keyboards send it.

---

Status: **rev 2, 2026-11-22**, product designer (systems focus). It follows the owner's 12:26 change and his addition ("This is the plan for all modular portable synths that we build — portable sound modules with a way to carry a keyboard with it. It should be flexible and not reliant on a single model of keyboard."). The 12:26 change: "I like the idea of focusing on the sound module now and making it so a travel MIDI controller can be carried with the module". It's drawn from `floss/REQUIREMENTS.md` rev 2, `design/owner.md` (2026-11-22 entries) and `floss/eng/controller.md` rev 0. Rev 1 (built-in keys) is superseded; its jam reasoning still holds where it doesn't depend on keys.

**"Inferred"** means the owner didn't say it. A concept may answer an inferred job weakly but must say so. A stated job a concept can't do sends it back.

## What changed from rev 1, and why
| Rev 1 | Rev 2 | Why |
|---|---|---|
| J2 every key sounds (25 keys) | **4**: as many notes as the controller plays (target T1: 25) | No keys; voices are now allocated to incoming notes (eng `controller.md` §5) |
| J3 split on the keys | **5**: the split and octaves live in floss for any controller; **6** is new | Split is floss's firmware (REQUIREMENTS rev 2). Eng's catch: the controller's octave buttons move the split point |
| J5 per-key pressure from the keys | **8**: per note when the controller sends poly aftertouch / MPE, channel pressure otherwise; **9** new: no pressure at all | Pressure now depends on the controller. The nanoKEY2 class sends velocity only (eng §2) |
| J6 lift speed per note | folded into **10** | Only the Seaboard Block M lists lift among the controllers checked (eng §5) |
| J13 read the state | **18** adds "is the keyboard connected" | A second object, a cable and a power port are now part of the state |
| J14, J15 start-up, park | **19, 20** include the keyboard | Two pieces to set up and carry |
| J18 duet on two halves | **23**: one plays, one tends the knobs | One controller; a second player on a second keyboard is possible via TRS MIDI in (see 16), but it isn't the main case |
| J19 point of view | **24** includes the keyboard | The controller's look isn't floss's (eng trade-off 2) |
| J21 build it himself | **26** adds proven parts; SMD allowed | Owner 09:2x: "reliable choices", SMD fine; he measures nothing |
| — | **2, 3, 16, 27, 28** new | Plugging in, carrying (a size range, not one model), other sources, controller swap, one family system |

## Jobs in detail
| # | Job | Source | What a concept must show |
|---|---|---|---|
| 1 | Strings anywhere | stated | sounds like strings on its own speaker from battery, with only the controller plugged in |
| 2 | One cable, floss powers the controller, any class-compliant USB MIDI controller | stated (REQUIREMENTS rev 2: floss is USB host and powers it; owner: "flexible and not reliant on a single model of keyboard") | a USB host socket with a cable path; a current-limited 5 V supply; works with the K-Board C and Xkey 25 (in view) and with velocity-only keyboards |
| 3 | Carry module + controller as one kit, for any travel keyboard in a size range | stated ("carried with the module"; T4; owner: "not reliant on a single model of keyboard") | where the controller and its cable go when packed, and that nothing gets damaged. **The carry must take a size range, not one model's outline: no recess cut to one keyboard.** Adjustable (straps, a sleeve, a clamp or a lid that takes a range) beats exact. Known points: K-Board C and nanoKEY2 ≈ 325 × 84 × 11–16 mm (eng §2); Xkey 25 to confirm. **Eng sets the range** from published sizes of 25-key travel controllers (PROPOSAL to check: up to ≈ 390 × 140 × 25 mm, ≈ 0.7 kg, which needs the Xkey 25's real size) |
| 4 | Every note sounding | stated (T1) | 25 voices allocated oldest-first; a 26th note steals the oldest |
| 5 | Split and octaves in floss | stated (settled, REQUIREMENTS rev 2) | OCTAVE L and OCTAVE R on floss's panel; equal = one keyboard; the split point is fixed by note number |
| 6 | Controller octave buttons don't break the split | inferred (eng §5 catch) | a stated rule for what happens: e.g. the split follows the controller's shift, or the panel says "keep the controller at its default" (a concept chooses; the honest minimum is to say so) |
| 7 | Velocity per note | stated (settled) | velocity acts per note; the concept says what it means |
| 8 | Pressure per note, selectable | stated (settled) | a pressure selector; per note with poly aftertouch / MPE; channel pressure acts on all notes |
| 9 | Expressive with no pressure | inferred | what the pressure selector does when nothing arrives (nothing breaks; velocity still does its job); a concept may give velocity-only players something extra |
| 10 | Tilt / bend / release speed | inferred (K-Board tilt, Seaboard lift, eng §5) | pitch bend (MPE per note, or global) has a destination; release velocity sets the tail where sent, and RELEASE's knob value where not |
| 11 | Tone colour, per half | inferred | as rev 1 |
| 12 | Shimmer | stated (settled) | analog BBD mode plus Daisy modes, a depth, can be fully off |
| 13 | Echo, reverb, tempo | stated (Big Energy rules); tap inferred | as rev 1 |
| 14 | Hold | inferred | a hold on floss's panel, plus MIDI sustain (CC 64) from a controller or pedal |
| 15 | Speaker; headphones mute it | stated (settled) | as rev 1 |
| 16 | Play from a computer or another keyboard | stated in part (Big Energy MIDI rules: USB device and TRS in); home keyboard inferred (eng trade-off 6) | the USB-C device port and TRS in both play floss; what happens if the controller and a computer play at once (eng: host and device together is unverified, `controller.md` §4) |
| 17 | MIDI out to other gear | stated (settled) | floss re-sends the controller's notes, split onto channels 1 / 2 when MIDI split is on, with velocity and pressure |
| 18 | Read the state, keyboard included | stated (no screens); connected-state inferred | knob positions are the state; floss shows whether a controller is connected and powered (on the status light or by sound) |
| 19 | Playing within seconds | inferred | power on → controller powered → play, with no pairing or setup |
| 20 | The kit in the park | inferred (T2: ≥ 4 h) | floss and controller fit a bench or lap together; the cable doesn't snag; readable in sun |
| 21 | Many notes vs one | inferred | as rev 1 (the fixed breath) |
| 22 | In tune | stated (T9) | TUNE trim; ±3 cents |
| 23 | Share it | inferred | one plays the controller, the other the panel; or a second keyboard via TRS in (16) |
| 24 | Point of view, keyboard included | stated (Big Energy J20) | the kit reads as one idea even though the controller isn't floss's own design |
| 25 | Big Energy family | stated (settled) | as rev 1 |
| 26 | Build from proven parts; fix | stated (REQUIREMENTS: reliable choices, SMD where necessary, measures nothing) | parts with published specs; battery, firmware flash and host port reachable |
| 27 | Swap controllers | stated (owner: "flexible and not reliant on a single model of keyboard"); eng trade-off 3 (K-Board C stock) | nothing in floss depends on one controller's size, socket (USB-A, USB-C or micro-USB via its own cable) or features; the carry takes the whole size range |
| 28 | One carry-and-connect system for every module | stated (owner: "This is the plan for all modular portable synths that we build") | the carry and the host port are designed as a family standard that Big Energy and port-a-poly could reuse: same size range, same way of attaching, same port and power rules |

**Settled constraints:** no built-in keys; the controller carried with it is 25 keys or fewer; no screens or encoders; battery; echo and reverb on the Daisy; no fixed budget, costed honestly; targets T1–T12 are the baseline, and any miss or beat is a trade-off for the owner.

## Flows

### F1 Grab and play (1, 2, 19)
1. Take floss and the controller out (one kit).
2. Plug the controller into floss's host socket.
3. Switch floss on: the controller gets power, and the status light says ready.
4. Play.
- **States:**
  - no controller → floss is ready and silent, and still plays from USB-C or TRS;
  - the controller draws too much → floss cuts its power, says so, and keeps running;
  - the controller is unplugged mid-chord → its notes release on their tails, no hanging notes.

### F2 Make a split (5, 6, 18)
1. Both OCTAVE knobs equal: one keyboard.
2. Turn OCTAVE L down: the lower half plays lower.
3. A held note keeps its pitch when its half's octave changes.
4. Pressing the controller's own octave button: the rule from job 6 applies.

### F3 Play expressively (7, 8, 9, 10)
1. Strike: velocity per note.
2. Lean:
   - poly aftertouch / MPE → that note;
   - channel pressure → every note;
   - no pressure → the selector does nothing, and nothing else changes.
3. Tilt or bend: per-note pitch (MPE) or global bend.
4. Lift: release velocity sets the tail if it's sent.

### F4 Choose what pressure does (8, 9)
As rev 1. Plus: with a controller that sends only channel pressure, the per-note positions act on every note.

### F5–F7 Colour, shimmer, echo and reverb (11, 12, 13)
As rev 1.

### F8 Hold (14)
HOLD on floss's panel, or a sustain pedal (CC 64) on the controller or TRS.

### F9 Go private (15)
As rev 1.

### F10 Play from elsewhere (16, 17)
1. **Computer:** USB-C device port → notes in, and floss's MIDI out to the DAW.
2. **Another keyboard:** TRS MIDI in.
3. **Both at once with the controller:** the notes merge (if eng confirms host and device together).
4. **MIDI split** (rear switch): out on channels 1 / 2.

### F11 Power (19, 20)
1. Charge over USB-C; play while charging.
2. Low battery is shown before it stops.
3. The controller is powered only while floss is on.
- Runtime includes the controller's draw (eng: ≈ 0.25–0.5 W).

### F12 Pack and carry (3, 20, 27)
1. Switch off; unplug, or leave the cable stowed with the controller.
2. Stow the controller in the kit's place for it.
3. Carry it as one thing.

### F13 The park (20)
1. Sit; controller on the lap or the bench, floss beside it (or the other way round).
2. The cable doesn't cross the hands or the speaker.
3. Play within a minute.

### F14 Share (23)
A friend takes the controller; you take floss's panel.

### F15 Swap the controller (27, 28)
Plug a different class-compliant keyboard (any in the size range, any USB socket type via its own cable) into the host socket: it plays, and it packs the same way. Its features (pressure or not) change what job 8 does, and nothing else.

### F16 Build and fix (26)
As rev 1, with the host port and its power switch added.

## Open questions
1. **Eng:**
   - USB host and device at the same time (`controller.md` §4);
   - over-current behaviour on the host port;
   - the Xkey 25's size and power;
   - the travel-keyboard size and weight range for the carry (job 3);
   - the most power the host port should supply (it sets which keyboards work, job 2);
   - whether 12 voices (one RP2350B) is acceptable against T1 (it's an owner trade-off if so).
2. **Concepts:**
   - the carry solution for a size range, as a family standard (jobs 3, 28);
   - the octave-button rule (job 6);
   - how "keyboard connected" shows (job 18);
   - what velocity-only players get (job 9).
3. **Owner (later):**
   - one object or two (eng trade-off 1);
   - does the kit's look matter when the controller isn't floss's (job 24)?
