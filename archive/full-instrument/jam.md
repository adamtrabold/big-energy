# Jam: the instrument's physical form

Work: how it's played, how ~30 controls are laid out, how it's carried and
powered, and the enclosure. Sound engine is settled (Model D-style mono voice).

---

## Turn 1: product designer (systems focus)

### 1. Jobs (from the owner's words; inferred ones are marked)

| # | Job | Source |
|---|-----|--------|
| J1 | **Play notes on keys.** They don't have to be a traditional keybed. | stated: "keys would be amazing, but they don't have to be like a trad keybed" |
| J2 | **Shape the sound live** with the Model D controls, roughly one control per function, while playing. | stated (it's a Model D clone); the "while playing" part is inferred |
| J3 | **Carry it anywhere** and set it up with no table, no mains power, no cables. | stated: "completely portable" |
| J4 | **Power it from a battery and recharge it**, and know how much charge is left. | stated: battery; the "know how much is left" part is inferred |
| J5 | **Hear it**: on headphones, through line out to an amp or interface, and maybe from a built-in speaker. | inferred (open) |
| J6 | **Build it**, either as the factory-assembled SMD version or as the hand-soldered through-hole kit, including putting the enclosure together, "IKEA" style. | stated |
| J7 | **Get the enclosure made**, either 3D printed at home or ordered. | stated |
| J8 | **Stay in tune with no calibration rigmarole**: auto-tune, and see that it worked. | stated: "not interested in a bunch of testing" |
| J9 | **Bend pitch and add modulation expressively** (the Model D's wheels). | inferred: it's core to playing a Model D |
| J10 | **Glide and play legato** the Model D way (low-note priority, single trigger). | inferred |
| J11 | **Connect to his other gear**: MIDI from the Maschine+, CV/gate to and from the eurorack, and run external audio (Plaits, Rings) through the filter. The Model D mixer has an external input. | inferred from the gear he owns |
| J12 | **Protect it in a bag.** Knobs and shafts survive being carried. | inferred: it follows from J3 |
| J13 | **Open it to fix it or swap the battery** without destroying the enclosure. | inferred: a kit has to be serviceable |
| J14 | **Hold a sound hands-free** (drone or latch) so both hands can work the knobs, for example lying on the couch. | inferred, wildcard |

The Model D control inventory these jobs touch (this is the "~30"):
- 26 knobs: tune, glide, mod mix; osc 1 range and wave; osc 2 range, freq and wave; osc 3 range, freq and wave; 5 mixer levels (osc 1–3, ext, noise); cutoff, emphasis, contour amount, filter A/D/S; loudness A/D/S; volume.
- About 12 switches: mixer on/off ×5, noise white/pink, osc mod, filter mod, osc 3 control, keyboard control ×2, decay, glide on/off.
- 2 performance controls: pitch bend and mod amount.
- Model D velocity is none, and it's monophonic. **So the playing surface only ever needs one gate and one pitch.** That frees us a lot.

### 2. Structure: physical rules that keep the PCB simple

These hold whichever concept wins. I'd like the director to treat them as
guardrails, and eng to push back where they're wrong.

- **S1. Zero hand wiring.** Every pot, switch and jack is board-mounted. Wire
  harnesses are where kits go wrong and where "rev 2" comes from.
- **S2. The pots are the fasteners.** The front panel is held on by the pots'
  own nuts, so there are no extra standoffs to line up. Both build variants use
  the same through-hole pots, so the panel is identical for SMD and TH.
- **S3. The front panel is a PCB** (FR4, black mask, white silk, ENIG). It's
  cheap at JLC, gives free legends, is dead flat, and lines up exactly with the
  main board because it comes from the same KiCad file. Option: a printed panel
  for people who want colour.
- **S4. Stepped controls are pots the MCU reads, not rotary switches.**
  Osc range becomes a digital octave offset on the pitch CV. Waveform becomes an
  analog mux addressed by the MCU from a detented pot. Six-position rotary
  switches are bulky, costly, hard to solder and hard to align. Eng needs to
  confirm this keeps the waveform path clean.
- **S5. One I/O edge.** All jacks and USB-C are on one board edge, so the
  enclosure needs one cut-out wall.
- **S6. Size the enclosure for the through-hole build.** TH electrolytics and
  the battery holder are the tallest parts. Size depth for them and the SMD
  board just fits. One enclosure serves both variants.
- **S7. Thermal.** Keep the regulator, charger and speaker amp away from the
  expo converters and the ladder. Add a printed shroud over the VCO cores to
  damp air currents, which matter for pitch drift.
- **S8. Battery options for eng to rule on:**
  - (a) An internal user-swappable 18650 in a TH holder, with a USB-C charger. Robust, and kit-friendly because cells are bought separately.
  - (b) "Bring your own power bank": USB-C in only, no cell inside. Simplest board, but many power banks shut off at low current draw. Real risk.
  - My lean is (a).
- **S9. Two-board split when the form needs it:** an analog board behind the
  knobs, and a "play" board (keys, MCU, power) linked by one keyed IDC ribbon
  carrying pitch CV, gate, power and the MCU-read pot lines. Keep the split if a
  concept folds or stretches, and drop it (one board) if a concept is flat.

Layers, from the top down: knobs → panel PCB → analog board (pots, jacks) →
frame (printed or ordered) → play/power board → battery → base plate.

### 3. Flows (the physical journeys)

- **F1. Open and play.** Take it out of the bag → open or uncover it → power
  switch → LED shows battery, then "tuning" (a few seconds) → green → play.
  There's nothing to load: the panel is the patch.
- **F2. Shape while playing.** One hand plays, the other rides cutoff,
  emphasis and contour. Cutoff, emphasis and the loudness envelope must sit
  nearest the non-playing hand. Pitch bend and mod sit at the edge closest to
  that hand too, the way the wheels sit left of the keys on the original.
- **F3. Warm-up re-tune.** Analog drifts for the first few minutes. After
  about 3 minutes the tune LED pulses once as a quiet nudge. One press
  re-tunes. It never re-tunes on its own mid-note.
- **F4. Pack away.** Power off → close or cover it, so knobs are protected and
  shafts take no side load → handle or bag.
- **F5. Charge.** USB-C. It plays while charging. The charge LED is separate
  from the tune LED.
- **F6. Connect.** MIDI from the Maschine+ (TRS or USB) → it follows notes. CV/gate out to the eurorack. Plaits or Rings → ext in → filter.
- **F7. Build (kit).** Solder the board, pots from the top → drop the panel PCB
  over the shafts → nuts → board into the frame → base → battery → power on.
  Auto-tune doubles as the build check: if an oscillator isn't found, the LED
  blinks its number. **That's the "no test equipment" self-test.**
- **F8. Swap the battery or service.** Base plate off with ≤4 screws (or
  magnets), and the cell is right there.

**States the hardware must show:** off, booting, tuning, tuned, tune failed
(which oscillator), low battery, charging, charged, MIDI receiving (a blink),
hold or drone latched.
**One LED budget:** a single RGB status LED plus a tune button covers all of
these. A 4-LED battery gauge is optional.

### 4. Concept seeds: four that differ in kind, not in styling

I used real randomness to get past the first idea. A shell RNG drew three
unrelated fields (*lunchboxes, sailboat rigging, dentistry*), one Oblique
Strategy (*"Use fewer notes"*) and one constraint (*"must be playable lying in
bed"*). I've applied all of them seriously below.

**A. LUNCHBOX: a clamshell with a tilting lid**
- **Structure:** the lid is the knob panel (analog board) and the base is the
  playing surface (play board), joined by a hinge and one ribbon.
- **Playing:** open it, prop the lid at about 30°, and you have a tilted control panel above the keys. That's the ergonomic idea of the original's flip-up panel without copying its look.
- **Carrying:** closed, it's a box with a handle and the knobs are fully protected (J12 solved by the form itself).
- **Keys:** 2 octaves of **Kailh Choc low-profile switches in a staggered
  piano layout**, with printed keycaps and octave buttons. Choc switches are
  through-hole, hand-solderable and cheap, and they have a whole keyboard-builder
  ecosystem.
- **Wheels:** a spring-return thumb joystick for bend, and a detented
  thumbwheel pot for mod.
- **Risks:** the hinge and ribbon must survive many opening cycles, and it has the most enclosure parts.

**B. RIGGING: a long neck with a ribbon**
- **Structure:** a long, slim body (about 45–50 cm) played across the lap or on a strap.
- **Playing:** the main pitch surface is a **long ribbon (softpot)** with fret
  marks, plus a row of capacitive "fret pads" above it for discrete notes. A
  switch toggles quantise between continuous and snap-to-semitone. Glide plus
  ribbon is very Model D: big, vocal slides.
- **Controls:** the knob field sits at the "head" like a dense headstock. The
  non-playing hand lives there.
- **Fit to the PCB:** the ribbon is one cheap part on one ADC pin.
- **Risks:** the long board or the board split, it's awkward to bag, and it's not "keys" in the piano sense. It's the most unexpected and the most expressive.

**C. SLATE: one board, flat as a book**
- **Structure:** a single PCB does everything. The **keys are ENIG copper
  pads on the panel PCB itself** (capacitive touch), so they cost nothing and need no assembly.
- **Carrying:** a bookbinding-style slipcase or hard cover protects the knobs.
- **Parts:** the fewest of any concept. It's the cheapest and the most "IKEA",
  and the kit build is barely longer than soldering the pots.
- **Weakness:** no tactile key feel. Mitigation: a raised printed key-frame
  overlay that the finger sits in.
- Bonus: the pad area can give a rough "pressure" value to route to the filter.

**D. CONCERTINA: fewer notes, held in two hands (playable lying in bed)**
- **Structure:** held like a concertina or game controller. Each grip end has
  a small **isomorphic button grid** (Wicki-Hayden layout). About 24 buttons
  cover 2+ octaves in a palm-sized area and every key shape transposes.
- **Controls:** the knob field sits in the middle between the hands, and
  thumbs reach the nearest row (cutoff, emphasis, glide).
- **Fit to the jobs:** it answers "fewer notes" (a mono synth needs one note at a time, so don't spend 25 keys' width on it) and "lying in bed" (no table and no lap needed).
- **Risks:** a learning curve for the layout, and the knobs furthest from the grips are a reach.

**Wildcards that could attach to any concept:**
- **Breath port** (from the dentistry draw): a barbed tube fitting with one
  pressure sensor that drives the VCA or filter. Monosynths *sing* with breath,
  and it's one part.
- **Hold/drone latch** (J14): the A-440 switch on the original becomes
  "hold" here, since auto-tune makes a tuning reference less necessary.
- **Built-in speaker:** small, auto-muted by the headphone jack switch. It's a
  real couch-play win, but the Model D's bass will be thin through 40 mm. It
  adds an amp chip.

### 5. Where I lean, and what I want from the others

- **Lean:** A (Lunchbox) is the strongest all-rounder for "keys + portable +
  protected". C (Slate) wins on cost and kit ease. B and D are the bold ones
  worth drawing before we judge them. A hybrid is possible: Lunchbox form with
  Slate's copper keys in the base.
- **Visual designer:** what does each look and feel like as an object? Avoid
  Moog trade dress: no wood end-cheeks and no copy of the panel graphics. Does
  the lid or cover read as a feature or as a box? How do printed versus ordered
  enclosures change what's plausible?
- **Open questions for the owner, via the director:**
  - Size target: backpack, tote, or coat pocket?
  - Tactile keys or touch pads?
  - Speaker: yes or no?
  - Is an unusual playing surface (ribbon or isomorphic grid) welcome, or should "keys" mean piano-shaped?

NEXT: product designer (visual focus) — four concepts that differ in kind are on the table, and they need form, feel and object character before the director can steer.

---

## Turn 2: product designer (visual focus)

My own draws, from a shell RNG (`SystemRandom`) so they weren't my pick:
fields *theatre lighting desks, surveying instruments, letterpress type cases*;
Oblique Strategy *"Use an old idea"*; constraint *"must look handmade"*. I
applied each one seriously below. The first idea any AI would have here is
"a mini Model D with a small keyboard and some nice knobs". I'm throwing that out.

### 1. What applies from the brief and records

- No visual brand exists. We are making it, so it should come from the owner
  rather than from us. He is a visual artist with an MFA, and the strongest
  identity we can give the instrument is his hand.
- **Trade dress, specifically:** no wood end-cheeks, no brushed-aluminium
  panel with black-on-silver legends, no fluted black skirted knobs in the
  Model D style, no copy of the flip-up panel with its rocker switches, no
  script logotype. Keeping the Model D's left-to-right **signal-flow order** is
  fine, because it's function and not dress.
- The owner wants it to be fun: "give me creative ideas". He has a eurorack
  with Plaits and Rings, so he already knows modern, dense, legend-light
  panels. We don't need to over-explain the controls on the panel.
- Systems' S3 (the panel is a PCB) is a gift to the look. Black mask, white
  silk and **bare ENIG gold** are three "inks" that come free.

### 2. Responses to the four seeds: form and feel

**A. Lunchbox: keep, and reshape it as an instrument case.**
- The risk is that closed, it reads as a toolbox or lunchbox, and open, as a
  laptop. *Surveying instruments* answer this: a theodolite case is plain
  outside and fitted inside, and opening it is an event. So the outside is
  deliberately quiet (one material, no legends, just a small hand-lettered
  name), and the reveal is the moment.
- **Feel:** use a **friction (torque) hinge**, an off-the-shelf part, so the
  lid stays at any angle from about 20° to 70° and there's no prop to fiddle
  with. Opening it should feel like opening a good laptop, not a cooler.
- Knob height drives lid depth, so this concept needs low knobs (about 12 mm
  tall) or the closed box gets fat. Flag for systems.
- Choc keycaps are where the hand lives. Print them in the body colour with
  the "black" keys a half-tone darker and 1.5 mm higher. Don't make them black
  and white: that's a toy-piano cliché.

**B. Rigging: keep. It's the most beautiful object here.**
- It's the only seed that reads as an *instrument* rather than a gadget: it
  has a long, slim line like a lap steel or a dulcimer. Ribbon plus glide is
  where a Model D voice sounds most like a voice.
- The bag problem is real. My reshape is a **soft roll case**, like a chef's
  knife roll or a drafting-tool roll, rather than a hard box. A long thing in a
  roll looks intended. A long thing in a box looks like a mistake.
- The fret marks should be gold ENIG lines on the panel PCB, spaced as
  semitones, so the "headstock" knob field and the "neck" share one material.

**C. Slate: keep. It's the cheapest and, honestly, the most striking.**
- Gold ENIG key pads on black mask look like jewellery and cost nothing.
  That's material honesty, and it's beautiful rather than a compromise.
- **Use an old idea:** add a **stylus**, the Stylophone principle. A stylus on
  copper pads gives the tactility capacitive touch lacks. You feel each pad
  edge click past, and with glide on it's a wonderfully vocal, scratchy way to
  play a mono synth. Electrically it's a resistor ladder into one ADC (eng to
  confirm), which is even simpler than capacitive. Offer both: finger
  capacitive, and a stylus clipped into the frame edge.
- **Must look handmade + bookshelf:** the cover is a **cloth-bound hardcover**
  (bookbinding board plus book cloth) that the owner can make himself, with the
  instrument sitting in it like a book in a slipcase. It's handmade by
  construction, not by decoration.

**D. Concertina: I propose we fold it in rather than kill it.**
- As an object it reads as a game controller, and the middle knobs are out of
  reach of both thumbs. That fails J2 (shape the sound while playing) on most
  of the panel.
- Its best idea, the **isomorphic grid**, is a playing surface, not a form.
  That makes it a candidate *module* for E below.

### 3. New seed: E. CHASE (letterpress), with the playing surface as a swappable forme

In letterpress, the **chase** is the steel frame and the **forme** is
whatever type you lock into it. You change the type and keep the press.

- **Structure:** one body holds the panel and voice. A recessed bay along the
  front takes a **playing-surface module** that locks in with two magnets and
  a 4–6 pin pogo or edge connector. Systems already showed the surface only
  ever needs *one pitch and one gate*, so the interface is tiny: power, ground,
  pitch, gate, and maybe one expression line.
- **Modules (formes):** a 2-octave Choc keyboard ships first. Others fold in
  from the other seeds: B's ribbon, C's copper or stylus pads, D's isomorphic
  grid, the breath port. The owner can design and print his own later. This is
  the creative answer to "keys, but not necessarily a trad keybed": **you
  don't have to choose.**
- **Feel:** the module drops in with a magnetic *clack* and a short status-LED
  flash that confirms the new surface. Swapping should feel like changing a
  lens, not doing a repair.
- **Risks I can see:** the connector is a new failure point (rev-2 risk), and
  scope grows with every module. **Mitigation:** fix the interface early and
  ship one module. Others are later, optional work that never touches the
  main board. Systems and eng should judge whether the interface can be frozen
  safely now.

### 4. Visual principles that apply to any concept

**V1. Job-case hierarchy: size follows use.** A California job case gives
the most-used letters the biggest compartments ("e" is huge, "j" is tiny). Do
the same with the controls. Sketch: `concepts/jobcase-panel-sketch.svg`.
- **T1, one knob:** cutoff. It gets a big cap of about 40 mm, and it's the
  only element in the signal colour. It's the "e".
- **T2, played controls (about 16 mm):** emphasis, contour amount, glide, osc
  2/3 frequency, tune, volume.
- **T3, set-and-forget controls (about 10 mm):** ranges, waveforms, mod mix.
- Ruled compartment lines in gold ENIG group the sections, replacing the
  boxed outlines of the original.
- This one move makes it look nothing like a Model D, which has a uniform
  knob grid, and it makes it *play* better: you can find cutoff in the dark.

**V2. Faders for the mixer and both contours (from *theatre lighting desks*).**
- That's 11 faders and 15 knobs. **The fader caps draw the envelope shape you
  will hear**, so the sound becomes visible at a glance, and the mixer reads
  as a mixer.
- Faders sit lower than knobs, which helps the Lunchbox lid depth. They also
  break the all-knob trade-dress look decisively.
- **Open for systems and eng:** board-mounted TH slide pots exist (for
  example Alps or Bourns 30–45 mm travel). Do they keep S1 (zero hand wiring)
  and S2 (pots as fasteners)? Faders need slots, which collect dust, and they
  can't serve as panel fasteners. Is the trade worth it?

**V3. Hand-lettered legends, so it looks handmade without faking it.**
- The owner draws the panel legends, about 40 words and a few glyphs, on
  paper. We scan and vectorise them into the silkscreen.
- Add a **scribble strip** (from the lighting desk): a matte white-mask band
  under the panel he can write on in paint pen for a patch or setlist.
- No font we pick will be as specific as his hand. It also makes the identity
  impossible to confuse with anyone's trade dress, and it's a fun 30-minute
  task he'll actually enjoy, not testing rigmarole.

**V4. Three "inks", one signal colour.** The palette is the PCB's own:
black mask, white silk, bare ENIG gold. Add one signal colour, used only on
the cutoff cap and the status LED's "ready" state. The body colour is open.
Three directions:
- **Field:** warm grey body, brass heat-set inserts left visible, safety
  orange signal (surveying).
- **Proof:** bone/unbleached body, red-ink signal, legends like a printer's
  proof marks (letterpress).
- **Desk:** all black, gold rules carry everything, cool green signal (the
  lighting desk at night).

**V5. Printed enclosures should show it honestly.**
- FDM layer lines look cheap when hidden badly, and intended when designed
  in. Use a horizontal **ribbed or fluted skin** on the sides so the layers
  read as texture, and put flat faces on the bed so they come out clean.
- For the ordered option, MJF nylon dyed black (JLC3DP) has a fine grainy
  stone feel and needs no design changes.
- Either way, the panel and base are PCBs, so the printed frame only has to
  look good from the sides. This is the systems "sandwich" read as a visual
  strength: the gold edge of two PCBs shows above and below a textured band.

**V6. Hear that it worked (feel of auto-tune, J8).** On power-up, instead of
a silent LED, the three oscillators **audibly converge** on A over about 2
seconds, quietly, the way an orchestra tunes before a concert, then settle
into a soft fifth and fade out. The boot sound *is* the self-test: a missing
oscillator is audibly absent, and the LED blinks its number. **Eng question:**
is the tuning routine run through the VCA at low level, or measured
pre-VCA? If it's pre-VCA, we'd open the VCA briefly at about −30 dB.

**V7. Small wildcards**
- **1/4"-20 tripod thread** (a brass insert in the base, from surveying):
  mount it on a camera tripod or a mic-stand adapter to play standing, or on
  a desk arm. It costs one insert.
- The status LED **breathes** while tuning, holds steady when tuned, and
  blinks once per MIDI note. It's one light with a personality, not a
  dashboard.

### 5. Tension I want resolved: which hand does the knobs?

On a piano-style surface the free hand is the **left**. Model D signal flow
runs left to right and puts the filter centre-right, which is the wrong hand.
Options:
1. Flip the flow (output on the left, controllers on the right). This
   breaks muscle memory from every synth.
2. Break the flow just for the performance controls: put cutoff, emphasis,
   contour amount and glide in a **left-edge "performance strip"** beside the
   bend and mod controls, with the rest in flow order.
3. In B, D and E-with-ribbon, the hand roles differ anyway.

I lean to 2. It's job-case logic again: the most-used controls live where the
hand already is. My sketch shows the pure-flow version so the problem is visible.

### 6. Where I lean

- **Strongest set to take to concepts:** A (as an instrument case), C (gold
  pads plus stylus in a cloth hardcover) and E (Chase). B is the bold one, and
  it's worth one more look as an E module (a ribbon forme) before it's kept
  as a separate form.
- Fold D into E as a module.
- V1 to V4 apply whichever concept wins. V2 (faders) needs a systems and eng
  verdict.

**Open questions for the owner, via the director:**
- Would he enjoy hand-lettering the panel? (I think yes, but ask.)
- Is a stylus welcome, or does it feel like a toy?
- Body colour: Field, Proof or Desk, or none of them?

---

## Turn 3: design director

My own draws (shell `secrets.choice`, not picked by me): fields *Polaroid
cameras* and *kites*; Oblique Strategy *"Only one element of each kind"*;
constraint *"must work in the dark"*. Applied below. Good jam. You've both
already thrown out "a mini Model D with a small keyboard". My job now is to
cut it down to what the owner can hold in his head on a phone.

### 1. The test I'll judge everything against

The owner's words, reduced to three tests:
1. **Keys he'll love.** He said keys "would be amazing". Creative is welcome,
   but it has to *feel* like playing keys, not like using a touchscreen.
2. **Grab it and go.** Portable means it survives a backpack and plays on the
   couch, with no cables and no table.
3. **No rigmarole.** Every extra part, module, connector and choice is
   something he has to build, debug or decide. "Incredible without a bunch of
   rigmaroll" is a brief about *subtraction*.

Test 3 is the one this jam is quietly failing. Between the two turns we have
faders, three knob tiers, gold rules, a scribble strip, a stylus, swappable
modules, a breath port, a speaker and a tripod thread. Each one is good, but
all of them together is a lot. My Oblique draw, **"only one element of each
kind"**, became the cutting rule: **one hero, one playing surface, one kind of
control per section, one light.**

### 2. A catch nobody raised: printer bed size

A 2-octave Choc piano at 18 mm key pitch is 15 × 18 = **270 mm of white
keys**, so the body is about 300 mm wide. Most home printers have a 250–256 mm
bed (Bambu P1/X1/A1 are 256, Prusa MK4 is 250 × 210). So **every concept
must either fit in 250 × 250 mm or split into parts that key together
cleanly.** This drives the form more than anything aesthetic. Systems: can we
get 25 keys in ≤ 245 mm (white pitch ~16 mm, staggered black row)? Otherwise
the frame splits at a designed seam, and that seam should look intended. I'm
asking the owner which printer he has.

### 3. Rulings on what's on the table

| Seed | Ruling | Why |
|---|---|---|
| **A. Lunchbox / instrument case** | **Forward** as concept 1, named **CASE** | It passes all three tests. The theodolite-case framing (quiet outside, the reveal is the event) and the friction hinge are right. |
| **E. Chase** | **Forward**, merged with my Polaroid draw as concept 2: **DOCK** (see §4) | "You don't have to choose" is the best answer yet to "keys, but not trad". As written, though, it's a platform, and platforms are rigmarole. It has to earn its connector by solving carry too. |
| **C. Slate** | **Forward** as concept 3, the deliberate dissent | It's the cheapest and the most IKEA, and gold on black is beautiful. But flat pads fail "keys would be amazing" and fail *in the dark*. It stays only if it fixes the touch problem (see fix list). I'll be hard on it. |
| **B. Rigging** | **Killed as a form.** The ribbon survives as a *later* DOCK module | A 45–50 cm body fails the bag test and the printer bed. "Lovely object" isn't enough when the owner asked for keys. |
| **D. Concertina** | **Killed as a form.** The isomorphic grid becomes a later DOCK module | Visual's reach argument is decisive: thumbs can't reach the middle knobs, which fails J2. |

**Wildcards:**
- **Hold/latch** (A-440 → hold): **yes.** It's free in firmware and serves J14.
- **Tripod thread:** **yes.** It's one brass insert and it turns into a stage stand.
- **Audible tuning on boot (V6): yes, I love this.** It's the self-test as
  music. It needs a "quiet boot" (hold tune while powering on) for late-night
  use. Eng must confirm it's measured where it can be heard safely.
- **Breath port:** **parked.** It's a great idea but it's scope. It becomes a DOCK module if DOCK wins.
- **Speaker:** **owner's call** (question below). I lean no: the bass will be thin and it adds an amp, heat and noise near the VCOs. Headphones and line out cover it.
- **Battery:** design assumes **S8(a): internal swappable 18650 + USB-C**.
  Power banks auto-shutting off at low current is exactly the rigmarole the owner refused. Eng has the final say.

**Visual principles:**
- **V1 job-case hierarchy: yes, with two tiers, not three.** Cutoff is the
  hero (big cap, the only thing in the signal colour). Every other knob gets
  one standard cap. Small caps for set-and-forget controls make three sizes,
  and three sizes look busy and are fiddly in the dark. Ranges and waves are
  set-and-forget anyway, so their *position* can carry their tier (top row,
  out of the way) rather than their size.
- **V2 faders: only for the two contours (6 faders), not the mixer.** The
  envelope-shape-you-can-see idea is the payoff, and it only applies to the
  contours. The mixer stays knobs. Result: **one kind of control per
  section.** 6 slots is also less dust and less board area than 11. Eng
  still has a veto on board-mounted slides with S1 and S2.
- **V3 hand-lettered legends:** **strong yes from me, but it's his time,
  so I'm asking him.** Scribble strip: **cut.** "One element of each kind":
  the panel already carries his hand in the legends.
- **V4 three inks + one signal:** **yes.** I'm putting the palettes to the owner.
- **V5 honest printing (ribbed sides, MJF option):** **yes.**
- **Hand tension (§5 of turn 2): option 2, a left-edge performance strip.**
  Cutoff, emphasis, contour amount and glide sit next to bend and mod, under
  the left hand. The rest follows signal flow. That makes the hero knob a
  left-hand knob, which is right.

### 4. New direction: DOCK (Chase × Polaroid)

The SX-70 folds flat into its own case: **the camera is its own lid.** Apply
that to E. **The keyboard module is the lid.**

- **To play:** the module sits in the front bay, magnets plus a 4–6 pin
  contact, and the knob panel sits behind it, as visual described.
- **To carry:** lift the module out, flip it, and it drops face-up onto the
  knob panel. Its flat base and perimeter rim cover the knobs (sunken panel,
  so knob tops sit at or below the rim). Closed, **it still looks like an
  instrument**, keys on top, rather than a box. There's no hinge and no
  ribbon, which removes CASE's two failure points.
- **Power is the dock.** Module in the bay means on, module on the lid means
  off (a magnet and a Hall sensor). That removes the power switch and makes
  closing it *be* the pack-away step (F4). Eng to rule.
- **Swappability stays,** but it's **free, not promised.** Ship one Choc
  keyboard. The connector spec is published, so a ribbon, a grid or breath
  is something the owner *can* make one day, never something the build is
  waiting on. That's how E passes the rigmarole test.
- **The printer bed helps here:** the body and the module are two separate
  prints, each under 250 mm deep. The seam *is* the concept.
- Risks I can see: contact reliability (rev-2 risk). Also, does the module
  rattle as a lid? Magnets at both positions fix that.

### 5. "Must work in the dark" (applies to all three)

Bedroom pop gets played at night, and the owner might be on a dim stage. The
fix is cheap and it's very much his:
- **Glow pointers.** Knob-cap pointer lines and the black-key fronts are
  printed in strontium-aluminate glow filament, as a multi-material or
  inlay print. In daylight they're a quiet stripe. With the lights off you
  see the whole patch as a constellation. It costs pennies and needs no
  electronics, and it photographs beautifully, which matters to a visual
  artist.
- **Touch hierarchy:** the hero cutoff knob and the left-edge strip are findable
  by hand. Faders read by touch too. Every concept must be playable without
  looking at the panel.

### 6. What each concept must show next round

Each one needs a top view, a side view (closed and open, at real mm), the
playing surface, how it's carried, and where the printer seam falls. Plus:
- **CASE:** knob height vs. lid depth, and the hinge/ribbon solution.
- **DOCK:** both module positions, the contact, and how power-by-dock feels.
- **SLATE:** a real answer to "these aren't keys". Either the printed key-frame
  overlay gives genuine travel or click (a printed living-hinge key over each
  pad?), or the stylus has to carry the concept. If neither is convincing, I'll
  replace SLATE with something else that differs in kind.

Shared across all three: the left performance strip, cutoff as the hero, 6
contour faders, glow pointers, one RGB status LED, the tripod insert, and an
internal 18650.

---

### Questions for the owner

Five quick ones. A word or a letter each is fine.

1. **Printer:** which 3D printer do you have (or what bed size)? It decides
   whether the body is one print or two.
2. **Where do you play it most?** (a) at a desk (b) couch or bed (c) standing
   or on stage (d) all of these. And what does it travel in: a backpack, a
   tote, or a pocket?
3. **Keys:** must they physically move and click, or are touch pads (with a
   stylus option, Stylophone-style) welcome?
4. **Built-in speaker?** Yes or no. It'll sound thin on bass, and headphones
   and line out are always there.
5. **Make it yours:** would you hand-letter the ~40 panel words (about 30
   minutes on paper, we scan it)? And pick a look: **Field** (warm grey,
   brass, orange), **Proof** (bone, red ink), **Desk** (all black, gold, green),
   or "none of these".

NEXT: product designer (systems focus): needs to check the 250 mm bed
constraint against 25 keys, confirm DOCK's contact and power-by-dock idea and
CASE's hinge/ribbon, and rule on 6 board-mounted faders, before the
designers build the three concepts.

---

## Turn 4: product designer (systems focus)

There's no `eng/architecture.md` yet, so the electrical rulings are
provisional. Eng has the final word on anything electrical. The owner's
answers landed mid-turn, so read **§7 first**: it supersedes the Choc switch
choice in §1, and §8 holds the revised jobs. §1's width maths still holds for
any keyboard.

### 1. Do 25 keys fit the printer bed? Yes, but only just, and nothing fits beside them.

Width budget for one printed part, ≤ 250 mm bed:

| Item | mm |
|---|---|
| Outer width target (margin on a 250–256 bed) | 245 |
| Two walls at 3 mm | −6 |
| **Interior for keys** | **239** |
| 25 keys C–C = 15 white positions × 15.9 mm | 238.5 |

- **Key pitch: 15.9 mm white, with a staggered black row.** Black switch
  centres sit on the white boundaries. The tightest black pair (C#–D#) is one
  white pitch apart, which is still more than the switch housing.
- **Switch: Kailh Choc V1 (PG1350).** The housing is about 15 mm square
  ([deskthority](https://deskthority.net/wiki/Kailh_PG1350_series)), so
  15.9 mm leaves about 0.9 mm between housings and about 1 mm cap gaps.
  - Mount it on the PCB with no plate. It's through-hole, so it's identical in
    both build variants.
  - **Verification task for eng:** a KiCad 3D clearance check of the housings,
    the hot-swap sockets if used, and the caps at 15.9 mm, before anything is
    committed. Normal Choc spacing is 18 × 17 mm, so this is deliberately tight.
- **What it feels like:** about 68 % of a full-size white key (about
  23.5 mm). It's cramped for chords but fine for mono lines, which is all a
  Model D plays. MX switches (19.05 mm minimum) can't fit. 12 mm tact
  switches would fit easily but fail the director's "keys he'll love" test
  (very short travel).
- **The consequence nobody's drawn yet:** at 25 keys, **there is zero room
  for bend and mod beside the keys.**
  - **Ruling:** bend and mod move up into the panel's left performance strip,
    directly above the lowest keys, next to cutoff. That matches the
    director's strip, so the left hand works one column.
  - **Fallback if the owner wants wheels next to the keys:** 20 keys (F–C,
    12 whites) at 17 mm is 204 mm, which leaves about 30 mm for a
    spring-return thumbstick and a mod wheel. That's fewer notes but more
    "instrument". Either way, octave buttons cover the range.
- **Owner's makerspace answer (owner.md) changes the constraint. It doesn't
  lift it.**
  - The machines he can always get on are the ~250 mm Prusas. The
    TAZ6/Voron/Gigabot volumes are unverified and the machines are shared.
    JLC3DP ordered prints have their own limits.
  - So **245 mm stays the default for any FDM part.** It prints anywhere,
    including ordered.
  - What *is* new: CO2 laser, CNC router and Tormach mean **the enclosure
    doesn't have to be FDM at all**, and a laser-cut or CNC'd body isn't
    limited by bed size.
- **New systems option: a laser-cut layered enclosure ("stack").**
  - The frame is a stack of laser-cut ply or acrylic layers, through-bolted
    between the panel PCB and a base plate. The DXF for every layer is
    exported from the **same KiCad Edge.Cuts outline**, so knob holes, pogo
    pockets, magnet pockets and battery bay all line up by construction.
  - That's the strongest form of S3 so far. Assembly is "stack in order,
    bolt through", very IKEA. Pockets are just layers with holes, and wall
    thickness never fights print tolerance.
  - It also frees the width: **25 keys at a comfortable 18 mm Choc spacing
    (270 mm) with bend and mod beside the keys** becomes possible. That's
    about 300 mm outer.
  - So the key-pitch question becomes an owner and director trade:
    **245 mm (any FDM, 15.9 mm keys, bend and mod on the panel)** versus
    **about 300 mm (laser or CNC, 18 mm keys, bend and mod beside the keys)**.
  - **My lean: offer the stack as the enclosure method for whichever concept
    wins.** The FDM version stays as the fallback, because ordering it needs
    no makespace time.
- **Trade-dress flag:** he works in walnut, and CNC walnut is now on the
  table. Walnut is fine as a material, but **not as end cheeks on the sides**.
  That's the Model D silhouette. Use walnut as a base or a full-body stack
  instead.
- **Depth is easy.** The panel is about 120 mm (top row of ranges and waves,
  2 rows of knobs, the fader block) plus the key area at about 70 mm, so about
  200 mm. Under 250 in both concepts, as one part or two.

### 2. DOCK: the connector, and why it carries no analog. Power goes by lid, not by dock.

**Connector ruling: no analog pitch or gate across the contact.**
- Pogo contact resistance changes with dirt and pressure. A few ohms on a
  CV line is an audible pitch error, which is a rev-2 risk on a pitch-critical
  synth.
- So **the module carries its own small microcontroller and sends MIDI over
  UART** (31,250 baud, 3 bytes ≈ 1 ms). **The dock is literally a powered
  MIDI port.** The body already parses MIDI for the Maschine+, so it's one
  code path.
- Every future module (ribbon, grid, breath) is "anything that speaks MIDI".
  The interface can be **frozen now safely**, because what matters lives in
  firmware.
- **Pins (6):** 3V3, GND ×2, TX, RX (spare: future module ID or tuning
  data), DETECT.
- **Pogo pins on the body, flat ENIG pads on the module.** The module needs
  no connector part at all.
- Two magnets and two printed locating cones per position. That gives
  pressure plus alignment, and the pogo pins' travel takes up print tolerance.
- **Lower-risk option:** an off-the-shelf magnetic pogo connector pair. The
  magnets are built in and it solders to both boards, which removes the
  custom alignment risk. Eng to pick.
- **Protection:** the module's supply sits behind a polyfuse or load switch,
  so hot-plugging or a shorted pad can't brown out the body.
- **Firmware rule:** if DETECT drops or serial goes silent for more than
  50 ms, all notes off. No stuck gates unless HOLD is latched.
- **Module MCU for the TH kit:** a Pico-class board on header pins (26 GPIO)
  can read 25 keys directly with no diode matrix. That saves about 50 solder
  joints of diodes. The alternative is a DIP ATmega with a 5×5 matrix and
  25 diodes. Eng to rule.

**Power-by-dock: rejected as written. Power-by-lid instead.**
- "Module out = off" breaks three things:
  1. MIDI-only play from the Maschine+ with the module set aside.
  2. Swapping modules, which would power-cycle and re-tune every swap.
  3. Shipping and storage safety for an 18650. You want a real, zero-drain
     switch for that.
- **What keeps the director's intent ("closing is the pack-away step"):**
  - A **Hall sensor reads only the lid position** (the module flipped onto
    the knobs, with a magnet in its base).
  - **Lid on → sleep:** the MCU disables the ±rail converter (one enable
    pin) and goes into deep sleep. That's microamps, with a low-power latch
    sensor of the DRV5032 type.
  - **Lid off → wake:** rails up, then the audible tuning boot.
  - Plus a **hard master switch** on the I/O edge for storage and shipping.
    Used daily, you never touch it.
- Dock presence is not a power signal. It only says "a module is here".
- Eng to confirm the rail-enable and sleep current.

### 3. CASE: hinge and ribbon. No ribbon, and the hinge gets a hard stop.

- **No wide ribbon through the hinge.** CASE uses the same split as DOCK:
  - The **lid is the body**: analog board, MCU, panel.
  - The **base is the keyboard module plus the battery**.
  - So only power, GND, TX and RX cross the hinge. That's **4–6 conductors
    in a round silicone-jacketed cable with crimped connectors at both ends**.
    It plugs in, so S1 holds (no soldered wiring).
- **Route it through a hollow hinge axis** so it twists rather than folds.
  70° of torsion is very low fatigue. Also add a printed strain-relief clip
  on each side.
- **Hinge: a friction hinge plus a hard stop at the playing angle (about
  25°).** Pushing the hero knob or a fader on a tilted lid pushes the lid
  back. Friction alone will creep, so the stop takes the load and friction
  only matters for other angles.
  - Rough load: 5 N at 100 mm from the axis is 0.5 N·m, so two hinges rated
    at least 0.5 N·m each.
  - Put the battery in the base so the open case isn't top-heavy.
- **Net:** CASE and DOCK now share one electrical architecture: the body
  board, plus a keyboard board that talks MIDI over UART, plus power. **The
  PCB design doesn't fork, whichever concept wins.** Only the mechanical
  joint differs (hinge and cable versus magnets and pogo pins).

### 4. Six board-mounted faders under S1/S2: yes, with conditions.

- **S1 (no hand wiring):** holds. Use PCB-mount TH slide pots, the same part
  in both variants. Example: about 30 mm travel, Bourns PTA30 or Alps RS30
  class.
- **S2 (the pots are the fasteners):** extended, not broken. **Pick a fader
  with threaded mounting holes**, so M2 screws through the panel PCB clamp
  into the fader bodies. Then the faders fasten the panel too, and nothing
  floats.
- **Slots:** the panel PCB gets routed slots about 1.5 mm wider than the lever.
  Fabs route slots routinely and they come from the same KiCad file, so
  alignment comes free.
  - **Lever height** must clear panel thickness plus cap. Check the datasheet
    stack in the KiCad 3D view.
- **Dust:** 6 open slots is acceptable. It isn't for 11, so the director's
  cut to contours only is right on systems grounds too.
- **Board area:** 6 × about 14 mm pitch is about 84 × 50 mm. That fits in
  the panel band.
- **Lid depth in both concepts:** fader caps sit lower than knob caps, so
  the tallest thing is the hero cutoff cap. Design the sunken panel or lid
  depth to *that* height.

### 5. Updated flows and states (supersedes turn 1 where they differ)

- **F1 open and play:** open the lid or lift the module → the Hall sensor
  wakes it → rails up → audible tuning (or quiet boot: hold TUNE while
  opening) → LED steady → play.
- **F4 pack away:** close the lid or flip the module on → sleep. There's
  no switch to remember.
- **F9 swap module (DOCK only):** lift → all notes off, LED shows
  "no surface" → drop in a new one → DETECT → LED flash → play. No re-tune.
- **F10 MIDI only:** the module is absent or aside, and the body plays from
  TRS or USB MIDI. Fully supported.
- **New states:**
  - sleeping (lid closed)
  - no surface (module absent, MIDI still works)
  - surface connected (a flash)
  - master off
- **Still one RGB LED and one TUNE button.**

### 6. Open for eng (blocking before the concepts get dimensions)

- Rail enable plus sleep current target (µA). Is power-by-lid OK?
- Module MCU choice (Pico-class versus DIP AVR) for the TH kit.
- Magnetic pogo pair versus custom pogo pins plus magnets.
- A 3D clearance check of Choc V1 at 15.9 mm.
- Which fader part has threaded holes and a lever height that matches a
  1.6 mm panel.
- S4 (stepped controls read by the MCU) is still unconfirmed from turn 1.

NEXT: design director — the rulings change the concept rules, so the director needs to steer before the designers dimension anything: CASE and DOCK now share one PCB architecture, power is by lid not by dock, bend and mod move to the panel at 25 keys (or the owner takes 20 keys plus wheels), and 6 faders are cleared.

### 7. What the owner's answers change (owner.md, Q3/Q4 plus new requirements)

**"I don't think click would make sense… I want it to feel like an
instrument." So: Choc switches are out as the main surface.**
- Even linear Chocs feel like a laptop: 3 mm travel, short caps, and a bottom-out tap.
- "Instrument" means:
  - keys that are **levers**, with longer travel and a pivot;
  - a smooth, silent return;
  - no click or tap at the bottom.
- My proposal, fab-friendly and using the makerspace: **flexure keys plus
  contactless sensing.**
  - **The key action is a laser-cut Delrin "comb".** All 25 keys are tongues
    cut from one sheet, joined at the back by a flexure hinge. Delrin is the
    standard fatigue-resistant flexure material, and it's on the makerspace's
    CO2 laser list. It's one part, with no springs or pivot rods to assemble,
    which is very IKEA.
    - The key tops go on top: printed, laser-cut ply, or walnut veneer.
    - A felt or TPU strip is the soft bottom stop. Felt is on the laser list,
      and TPU (NinjaFlex) is in stock.
    - That gives about 6–8 mm of travel at the key front.
  - **Sensing: a magnet in each key tip over a linear Hall sensor** on the
    keyboard board. The SS49E-class sensor is TO-92, so it's through-hole in
    both builds and cheap.
    - It's silent, and nothing wears.
    - The MCU reads key *position*, so the gate threshold is adjustable in
      firmware.
    - **Velocity comes free.** The Model D has none, so it's optional and
      never a new knob. A firmware option could route velocity to the filter
      over the same DAC line as MIDI CC (below).
    - 25 analog channels means 2 × 16-channel analog muxes on the keyboard
      board. That's modest and confined to the module.
  - **Fallback:** the same comb over a silent tact switch or a conductive
    rubber pad under each key. That gives travel but no velocity. Eng and the
    director pick.
- **This removes the 15.9 mm housing limit.** Hall sensors are about 4 mm
  wide, so key pitch is set by fingers, not parts. With the laser **stack**
  enclosure (§1), a 300 mm body with about 18 mm keys and bend and mod beside
  them fits naturally. In an FDM-only body, 245 mm still means about 15.9 mm
  keys.
  - **My lean is now the stack and about 300 mm.** The flexure comb is a
    laser part anyway, so the enclosure and the keyboard share one process.
- **Flag: the Hall keys and every other magnet must be kept apart.** The
  speaker magnet, the dock magnets and the lid-sense magnet are all near Hall
  sensors.
  - Rule: the speaker sits at least about 60 mm from the nearest key sensor,
    on the body side, not in the keyboard. Dock and lid magnets go at the
    module's *ends*, outside the key row.
  - The firmware calibrates each key's rest value at boot, which absorbs
    static offsets. Eng to confirm the distances by a quick measurement.

**Built-in speaker: YES, plus outputs.**
- **Speaker:**
  - Class-D mono amp. For the TH kit, a prebuilt amp module on header pins.
  - A full-range driver of about 40–50 mm with a sealed printed or stacked
    back volume, firing up or forward through a grille.
  - The grille is a natural laser part: a perforated panel layer. Placement is
    rear-centre of the body, away from the VCO cores (S7) and the Hall keys.
- **Outputs:**
  - Headphones, through a switched jack.
  - Line out, a separate jack.
  - **Plugging into either mutes the speaker.** That's switched-jack logic,
    so no new control.
  - The lid closed (sleep) mutes everything.
  - The main volume knob sets the speaker and headphones. Line out is
    fixed-level (eng to confirm).
- **Thin bass:** a high-pass on the speaker path only stops a small driver
  farting out on Model D lows. Outputs stay full-range.
- **Power:** the speaker is the biggest new load. The battery size may grow
  from 1× to 2× 18650. Eng to size it.

**"Pass things into the filters and whatnot": external input, plus a few
patch points.**
- **EXT IN** feeds the mixer's external channel (the Model D way), so the
  existing EXT level knob sets the gain. It must accept line level up to
  eurorack level (about 10 Vpp) without clipping. Eng to set the input range.
- **Proposed minimum patch set,** on 3.5 mm eurorack-style jacks on the one
  I/O edge (S5):
  - EXT IN
  - FILTER CV IN (cutoff)
  - PITCH CV OUT
  - GATE OUT
  - PITCH CV IN and GATE IN (eurorack plays it)
  - Eng to scope it. Each jack is one board-mounted part and one hole.
- **I/O edge total:** USB-C (power plus USB MIDI), TRS MIDI IN, phones,
  line out, EXT IN, plus 4–5 CV jacks. That's about 10 parts. At a 12 mm
  jack pitch it's about 130 mm, so it fits a 245 mm or 300 mm rear edge.

**MIDI control: YES.**
- USB MIDI (on the existing USB-C) plus TRS MIDI IN. It follows notes,
  bend, mod and hold (sustain pedal CC64).
- **Honesty point for the owner:** the knobs are real pots in the analog
  path, so **MIDI can play it but can't turn its knobs.**
  - **Cheap partial fix:** one spare DAC channel summed into filter cutoff,
    driven by CC74 (and optionally by velocity from the Hall keys). That gives
    MIDI-controllable filter sweeps with one op-amp stage and no knob changes.
  - Eng to confirm there's a spare DAC channel.
- With the DOCK architecture, the keyboard module already speaks MIDI
  internally (§2). So external MIDI and the module go through one parser.

### 8. Revised jobs (the basis for jobs.md)

Changes from turn 1 are marked. This list goes into jobs.md when the jam closes.

| # | Job | Source |
|---|---|---|
| J1 | **Play notes on keys that feel like an instrument**: real travel, silent, no click. They don't have to be a traditional keybed. | **stated, sharpened** ("feel like an instrument") |
| J2 | Shape the sound live with one control per function while playing. | stated / inferred |
| J3 | Carry it anywhere, and play it with no table, mains or cables. | stated |
| J4 | Run on battery, recharge it, and know the charge. | stated / inferred |
| J5 | **Hear it from the built-in speaker; plug in headphones or line out, which mutes the speaker.** | **now stated** |
| J6 | Build it as either variant, enclosure included, IKEA-simple. | stated |
| J7 | Get the enclosure made: printed, laser-cut or CNC'd at the makerspace, or ordered. | stated, **widened** |
| J8 | Stay in tune with no rigmarole, and know that it worked. | stated |
| J9 | Bend pitch and add modulation. | inferred |
| J10 | Glide and play legato. | inferred |
| J11a | **Run external audio through the filter** (EXT IN to the mixer). | **now stated** |
| J11b | **Play it from MIDI** (USB and TRS): notes, bend, mod, hold. CC to filter is proposed. | **now stated** |
| J11c | Patch it with the eurorack (CV and gate, in and out). | inferred ("and whatnot"). **Scope question for the owner and eng** |
| J12 | Protect it in a bag. | inferred |
| J13 | Open it to service it or swap the battery. | inferred |
| J14 | Hold or drone a sound hands-free. | inferred (director approved) |

NEXT (updated): design director — the owner's answers move the key choice (from Choc to laser-cut flexure keys with Hall sensing) and tip the enclosure toward the laser stack at about 300 mm. That, plus the T4 rulings, needs steering before concepts get dimensions.

---

## Turn 5: design director (pass 2)

Systems' Turn 4 is excellent: one PCB architecture for both concepts, the
module talking MIDI so no analog crosses a contact, power-by-lid. **I accept
all of it.** But the owner's newest words (owner.md) landed after it, and they
move the ground under the keys:

> "i dont think click would make sense for a keyboard.. i want it to feel like
> an instrument. built in speaker would be incredible but it needs outs. also
> would be cool to be able to pass things into the filters and whatnot. and to
> control via midi."

### 1. Keys: Choc switches are out. Lever keys with magnetic (Hall) sensing are in.

A Choc switch, even a linear one, is a computer-keyboard part. It has 3 mm
of travel straight down, and that's not what he's asking for. What makes a
keyboard *feel like an instrument* is a **lever**: a key that pivots at the
back, a longer travel at the front, a soft return, and silence.

**Direction: a printed lever keybed.**
- Each key is a printed lever pivoting on a flexure (a living hinge) at the
  back. The keys are printed as **one comb per octave**, so there are no
  per-key hinges to assemble. Drop the comb on and screw down one clamp bar.
  That's IKEA.
- A small **magnet in each key** sits over a **Hall sensor** on the keyboard
  PCB. TO-92 linear Hall parts exist, so it's through-hole friendly, and it's
  one sensor per key read through a mux by the module MCU that systems
  already specified.
- What it gives the owner:
  - **Silent**, with no click at all.
  - **Continuous travel.** The gate fires at a set depth, and the firmware
    can read *how fast* (velocity) and *how deep* (pressure), as optional
    routes to the filter or loudness. The Model D had neither, so both ship
    **off by default** and the firmware keeps the original's character.
    They're there to grow into.
  - **The "feel" can be tuned** by changing the flexure thickness or adding a
    TPU bumper (NinjaFlex is at his makerspace). No new parts.
  - **No switch-housing pitch limit**, so 18 mm keys are easy.
- It also feeds the brand: the key comb is the part people will pick up and
  ask about. It's his own action, made at the makerspace.
- **Verification before concepts are dimensioned** (eng / systems):
  1. PETG flexure fatigue at about 4 mm key-front travel. Alternatives are a
     steel pivot pin plus a spring, or a TPU hinge strip.
  2. Hall sensor and magnet sizing for a clean gate threshold with
     hysteresis, plus per-key auto-calibration at boot. This folds into the
     tuning boot, so there's no rigmarole.
  3. Mux scan rate for 25 sensors (sub-ms is fine).
- **Fallback** if the flexure fails verification: the same Hall sensing with
  a pin pivot and a spring per key. That's more parts, but the same feel and
  the same PCB.
- **Not taking** a donor keybed from a cheap controller. It's not IKEA, not
  repeatable, and not his.

### 2. SLATE is killed

Flat pads fail "feel like an instrument" outright, and they also failed my
"works in the dark" test. The stylus idea is lovely, but it's a toy reading
of an instrument request. **Gold ENIG stays as a material** for the panel
rules and fret marks, and the cloth-bound cover idea moves to the carry
options.

**Two concepts go forward, not three.** CASE and DOCK now share the PCB and
the keys, so they differ exactly where they should: **how you play it and how
you carry it**, a tilted fixed panel versus a flat body with a lid you play
on. I'm not inventing a third concept just to have three. If one dies in
review, I'll replace it then.

### 3. Width: ~300 mm, wheels beside the keys

Systems framed the trade well: 245 mm (any FDM printer, bend and mod on the
panel) versus about 300 mm (laser-cut or CNC stack, wheels beside the keys).
"Feel like an instrument" settles it. **Two wheels to the left of the keys,
where hands expect them.** Bend is spring-centred and mod is free, both
printed thumbwheels on board-mounted pots. That frees the panel's left strip
for cutoff, emphasis, contour amount and glide only.
- About 300 × 210 mm still goes in any backpack.
- **The enclosure method becomes the stack** (Turn 4): laser-cut layers
  exported from the KiCad outline, through-bolted between the panel PCB and the
  base. He can cut it at Vector Space or order it cut. FDM is only for the key
  combs, wheels, caps and small parts, and all of those are well under
  250 mm.
- **Trade-dress guard:** stack layers can be walnut ply (he works in walnut),
  smoked or coloured acrylic, or wool felt and cork. If they're wood, the
  **whole body edge** is laminated stripes, not solid end cheeks. The striped
  edge reads as a stack, not as a Model D. I'm asking the owner below.

### 4. Speaker yes, with outs, and it should be a real feature

He said "incredible", so it can't be an afterthought speaker.
- **One full-range driver of about 50–57 mm in a sealed chamber.** The stack
  makes a sealed chamber easy: layers with a cut-out, gasketed with a felt
  layer. Put it **at the right end, away from the VCOs** (S7), firing up
  through a laser-cut grille. **The grille pattern is a brand surface.** It's
  the one place his drawing could live besides the legends.
- **Headphones mute the speaker. Line out does not.** No extra switch.
  Volume is shared.
- Eng: a class-D amp chip near the VCOs is a noise risk. Keep it at the far
  end with its own regulator, and check its idle hiss.
- In DOCK, the speaker must be in the **body**, not the module, and the
  grille must not be covered when the module is docked in front. In CASE,
  it fires from the lid's top edge or face.

### 5. Ins, outs and MIDI: a small patch edge, sized for his eurorack

"pass things into the filters and whatnot" plus "control via midi" means one
I/O edge (S5) at the back:

| Jack | Type | Purpose |
|---|---|---|
| PHONES | 3.5 mm stereo | mutes speaker |
| LINE OUT | 1/4" or 3.5 mm (eng) | to interface or amp |
| EXT IN | 3.5 mm | into the mixer's EXT channel, so Plaits or Rings go through the ladder |
| FILTER CV IN | 3.5 mm | cutoff from the eurorack |
| PITCH CV IN, GATE IN | 3.5 mm | play it from the eurorack |
| PITCH OUT, GATE OUT | 3.5 mm | the keys play the eurorack |
| MIDI IN, MIDI OUT | 3.5 mm TRS (type A) | Maschine+ in. MIDI out sends the lever keys out as a controller. |
| USB-C | device | MIDI both ways plus charging |
| Master switch | slide | storage and shipping only |

- **3.5 mm throughout** for patch jacks: that's eurorack-native, needs no
  adapters, and they're board-mount TH parts.
- Eng owns the levels: eurorack audio is about ±5 V, so EXT IN needs
  attenuation. Pitch is 1 V/oct. Gate in and out should be about 5 V and
  tolerate 10 V.
- In DOCK, the patch edge is on the body's rear, so cables don't stop the
  lid flipping on. In CASE, it's on the base's rear, so cables don't run
  through the hinge path.

### 6. Updated common spec for both concepts (supersedes Turn 3 §6)

- **Keys:** a 25-key printed lever keybed with Hall sensing, about 18 mm white
  pitch, silent, velocity and pressure off by default. Two thumbwheels on the
  left.
- **Panel:** a left strip (cutoff as the hero cap in the signal colour,
  emphasis, contour amount, glide) → oscillators → mixer knobs → 6 contour
  faders → loudness and volume. Two knob tiers. One RGB LED. One TUNE button.
  HOLD.
- **Body:** a laser-cut stack about 300 × 210 mm, with a sealed speaker
  chamber at the right, the patch edge at the back, an 18650 in the base,
  and a tripod insert.
- **Power:** power-by-lid sleep (Hall) plus a master switch (Turn 4 §2).
- **Night:** glow-filament pointers on the caps and the black-key fronts
  (PETG/PLA glow filament can go in as a separate print or an inlay; there's
  no multi-material printer at the makerspace).
- **CASE:** the lid is the body (panel, analog board, speaker). The base is the
  key comb plus the battery. A 4–6 wire cable runs through a hollow hinge,
  with a hard stop at about 25°.
- **DOCK:** a flat body. The keyboard module docks at the front over the
  MIDI-UART pogo pins, and flips face-up onto the sunken panel as the lid.
  With lever keys, check that the key combs survive as a lid: they mustn't
  get pressed in a bag. The flexure needs a travel stop, and the module
  rim must stand proud of the key tops.

Each concept must show next: top view, side views open and closed at real mm,
the key lever cross-section, the speaker and grille, the patch edge, and the
carry state.

### 7. Are the jam passes done?

**Yes.** Directions are narrowed (CASE and DOCK), the common spec is set,
and every open item left is either eng verification, which can run in
parallel with concept building, or the look (Q5), which the designers can
show as variants. Next is concept building.

---

### Questions for the owner (pass 2)

Just two. One letter each is fine.

1. **Look:** pick one, or "none": **Field** (warm grey, brass, orange),
   **Proof** (bone, red ink), **Desk** (all black, gold, green).
   **Body material:** (a) walnut ply stripes (b) coloured or smoked acrylic
   (c) felt and cork (d) surprise me.
2. **Your hand:** would you hand-letter the ~40 panel words and maybe draw
   the speaker grille pattern (about 30–45 minutes on paper, we scan it)?
   Yes / no / maybe later.

NEXT: orchestrator — the jam is done. Start concept building with both
product designers on CASE and DOCK against the Turn 5 common spec. In
parallel, get eng to verify the lever-flexure and Hall-key sensing, the
speaker amp noise, and the patch-edge levels. Send the owner the two Q5
questions above.

---

## Turn 6: design director (pass 2 addendum). Supersedes Turn 5 where they differ.

Three things arrived after Turn 5: systems' updated Turn 4 §7–8, the owner's
Q5 answer, and new owner direction on the concept set (all in owner.md).

### 1. The owner wants two kinds of concept, so the set reopens

> "it'd be cool to see some expected / highly designed for use cases, and
> others using more of the randomness/creative principles to drive unique
> outcomes that have more sauce / vibe"

In Turn 5 I cut to two concepts by subtraction. That was right for the
"designed for use" kind, but it starved the other kind. **The set going to
concept building is four: two of each kind.** The common spec still applies to
all four (keys, speaker, outs, MIDI, battery, the no-rigmarole build). Sauce
is a licence for character, **not a licence to drop the stated jobs.** If a
sauce concept fails "feel like an instrument" or "portable", it dies
regardless of vibe.

**Designed for use**
1. **CASE** (Turn 5 spec): a clamshell with the panel as a tilted lid.
2. **DOCK** (Turn 5 spec): a flat body, and the key module is the lid.

**Sauce.** I made fresh real draws (shell `secrets.choice`) and kept both
seeds as drawn:

3. **MOTTO.** Draw: *harpsichords + rotary telephones · "Water" ·
   one-handed operation.*
   - **Silhouette:** a tiny bentside. The body is asymmetric, the curve of a
     harpsichord tail trimmed into the 300 × 210 footprint, and the tail houses
     the speaker chamber. Nothing else looks like this, and it's nowhere near
     Model D dress.
   - **Reverse-colour keys:** dark naturals and bone sharps, the old
     harpsichord convention. Instantly un-toy and un-Moog.
   - **The painted lid:** Flemish harpsichord lids were painted inside, often
     with a motto. Here the lid props open on a stick and does two jobs:
     - It's a **sound reflector** for the up-firing speaker, as on a real
       harpsichord. That's acoustic function, and it answers "incredible
       speaker".
     - It's **the owner's canvas.** He offered to "hand paint it". This
       concept gives his hand the biggest surface on the instrument. Closed,
       the lid protects the knobs and the keys.
   - **Rotary telephone + one-handed:** the left performance column is built
     for one hand. Oscillator range becomes a **finger-dial ring**
     (stepped, MCU-read per S4) rather than three small knobs. Design has to
     prove that dial reads better than knobs, or it's cut.
   - **Water:** the bentside curve and the panel's flow lines should read as
     one current running from the oscillators to the tail where the sound
     comes out.
   - **Risks:** the curved stack and the lid stay and hinge. The lid must not
     sit as a sail in a bag.
4. **DISH.** Draw: *harpsichords + radio telescopes · "Make a sudden,
   destructive unpredictable action; incorporate" · looks like furniture.*
   - **Destructive action, incorporated:** cut a circle out of the rectangular
     panel. That circle becomes a **round control dish on a yoke** that tilts
     toward the player, like a radio telescope or a vanity mirror. The cut-out
     is the identity.
   - **Radial job case:** signal flow spirals inward, from oscillators on the
     outer ring through the mixer and contours to **cutoff dead centre**.
     The hero knob is the bullseye, and the speaker fires through the dish
     behind it, so the sound literally comes from the cutoff.
   - **Furniture:** a yoke and pivot in solid-looking stacked layers, so it
     reads as a small piece of furniture on the desk. The lever keys run in a
     straight row in front.
   - **Carry:** the dish rotates face-down into its own recess, the way a
     telescope stows. The knobs are protected and the back of the dish is a
     clean disc (a second canvas).
   - **Electrical:** the pivot uses CASE's solution, a 4–6 wire cable through
     a hollow axis. The dish carries the analog board and pots and the base
     carries the keys and power, which matches the shared architecture.
   - **Risks:** whether the faders fit a circle (maybe they become a short
     arc or move to the base), whether signal flow is legible radially, and
     the round panel PCB (fine at the fab).

Reconsidered and still killed: **SLATE** (flat pads fail "instrument") and
**Rigging/Concertina** as forms (bag and reach). They're beaten by MOTTO and
DISH, which carry their sauce without failing a stated job.

### 2. The look: mocks, not words. My Turn 5 owner questions are withdrawn.

> "i can make the labels myself or hand paint it or something based on
> outcome. id have to see mocks of the ideas to tell you which look appeals"

- **Every concept reaching the owner is a visual mock**, rendered top or
  three-quarter view at real proportions in a specific look. That means
  material, colour and legends, not wireframes.
- **Plus one look sheet:** a single concept (designers' pick) shown in
  **Field / Proof / Desk**, and with a body material each (walnut-ply
  stripes / coloured acrylic / felt and cork) so he can choose by eye.
- **Legends in the mocks should look hand-made but be marked as placeholder.**
  He'll make the real ones or hand paint them ("based on outcome"). MOTTO's lid
  and DISH's dish-back show where painting would go.
- No more look questions for the owner until he has seen mocks.

### 3. Systems' updated Turn 4 §7–8: rulings

- **Keys: adopt the laser-cut Delrin flexure comb** over my printed-comb
  proposal. Delrin is the right fatigue material and it shares the laser
  process with the stack. I'm keeping my requirements:
  - about 18 mm white pitch, with 6–8 mm travel at the front;
  - a felt or TPU soft stop;
  - Hall sensing, with velocity available but **off by default**;
  - per-key rest calibration folded into the tuning boot.
  - The silent-tact/rubber fallback is acceptable only if Hall fails
    verification.
- **Magnet separation rule (systems):** accepted. Every concept must show the
  speaker at least 60 mm from the nearest key sensor, and dock and lid magnets
  outside the key row. This constrains MOTTO's tail and DISH's centre speaker:
  DISH's dish must sit far enough behind the keys.
- **Outs:** systems' version wins over mine. **Any plugged output mutes
  the speaker**, a high-pass sits on the speaker path only, and line out is
  fixed level.
- **MIDI:** USB plus TRS in **and out**. MIDI out sends the Hall keys to the
  Maschine+. **Yes to the CC74 → cutoff DAC sum**, and the owner must be told
  plainly that MIDI plays notes but can't turn the knobs.
- **Speaker placement:** concept-specific (CASE: lid; DOCK: body rear; MOTTO:
  tail under the lid; DISH: dish centre). Every placement must respect the
  60 mm rule and S7.
- **Battery:** 1 or 2 × 18650, eng to size. Concepts must leave room for 2.
- **J11c CV patching:** the patch edge from Turn 5 §5 stands as the design
  default. Eng can trim it.
- **Jobs (systems §8):** approved for jobs.md as written.

### 4. What each concept must show (all four)

- A visual mock in a named look. Top or three-quarter view, real proportions.
- Side views, open or playing and closed or carry, in mm.
- The key area, the speaker with its grille, and the patch edge, with the
  60 mm magnet rule visibly met.
- How it's made: which parts are laser-cut, printed or ordered, and roughly
  how many build steps.
- Plus one look sheet (Field / Proof / Desk) on one concept.

I'll score the designed-for-use pair and the sauce pair on the same 1–10
scale, but against their own kind. A sauce concept doesn't need to be the
most ergonomic, and a designed-for-use concept doesn't need to be the most
surprising. All four must meet the stated jobs.

### 5. Jam status

**The jam is done.** Four concepts are seeded with clear briefs, the common
spec is set, and the look will be resolved by mocks. Open items are eng
verification (flexure, Hall, magnet distance, amp noise, levels, battery) and
run in parallel.

### Questions for the owner

None right now. The Turn 5 questions are withdrawn, and his next input should
be reacting to mocks.

NEXT: orchestrator — the jam is done. Start concept building: four concepts,
two designed for use (CASE, DOCK) and two sauce (MOTTO, DISH), each as a
visual mock against the Turn 6 spec, plus one look sheet. Kick off the eng
verifications from Turn 6 §3 in parallel.
