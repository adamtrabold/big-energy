# Control taxonomy: what every control is for, before any layout
Status: **proposed** (team), for the owner to correct · written 2026-11-19 · sources: [owner.md](../design/owner.md) (2026-11-19 14:36 ask), the Minimoog Model D manual ([`design/owner-refs/Minimoog_Model_D_Manual.pdf`](../design/owner-refs/Minimoog_Model_D_Manual.pdf), "Features & Controls", pp. 15–33), the [feature docs](README.md), the current panels (P5RS, `design/branches/concepts/cathedral/layout_check.py`).

**The owner's request (14:36, verbatim):** "let's start by doing a tree map or something first and just define the categories of controls and what controls belong in those categories before laying anything out."

This page lays nothing out. It names every control, says what it's for, and groups the controls. The last sections say which half each group belongs on under his stated rules, and list where those rules don't decide it.

## 1. The four jobs a control serves
| Job | Meaning | Example |
|---|---|---|
| **set once** | set before playing (or per patch), then left alone | octave, wave, source, voices |
| **shape** | sculpt the sound between phrases: often turned, rarely while playing a note | envelopes, resonance, echo type |
| **play** | moved *while* notes sound: a hand off the keys, or the keys themselves | bend, mod, cutoff, tap, keys |
| **level / out** | how loud, where it goes | mixer, volume, pan, effect levels |

## 2. The tree
The first five branches are the Model D's own panel sections, in its left-to-right order: Controllers · Oscillator Bank · Mixer · Modifiers · Output. The manual also puts the wheels, glide switch and DECAY switch on the **left-hand keyboard panel**, and the jacks on the **top patch panel**. Big Energy's additions get two new branches (**Effects**, **Connections & system**) and slot into the Model D's sections elsewhere. A ★ marks an addition.

```
Big Energy
├── 1 CONTROLLERS (Model D: Controllers panel + left-hand panel; the hands)
│   ├── 1a Performance: bend (stick) · mod · glide
│   ├── 1b Modulation: blend · mod→pitch · mod→filter
│   └── 1c Keyboard: keys (25) · touch strip ★ · release · voices ★ · velocity ★ · touch ★
├── 2 OSCILLATOR BANK
│   ├── 2a Oscillator 1: octave · wave
│   ├── 2b Oscillator 2: octave · wave · pitch
│   ├── 2c Oscillator 3: octave · wave · pitch · track 3
│   ├── 2d Oscillator 4 ★ (optional analog): octave · wave · pitch
│   └── 2e Tuning: tune · drift ★          (Model D: TUNE sits in Controllers; see §4)
├── 3 MIXER: 1 · 2 · 3 · (4 ★) · extra · source (noise · input · loop)
├── 4 MODIFIERS
│   ├── 4a Filter: cutoff · resonance · envelope (amount) · track
│   ├── 4b Filter contour: attack · decay · sustain
│   └── 4c Loudness (amp) contour: attack · decay · sustain
├── 5 EFFECTS ★ (after the amp, before the output: signal order)
│   ├── 5a Echo: type · time · free/sync · repeats · pan · level
│   ├── 5b Reverb: type · decay · level
│   └── 5c Tempo: tap (its ring is the status light)
├── 6 OUTPUT
│   ├── 6a Master: volume · pan ★ · link ★
│   └── 6b Destinations: phones · line out · speaker
└── 7 CONNECTIONS & SYSTEM ★ (Model D: top patch panel)
    ├── 7a Ports: USB-C · MIDI in · MIDI out · pitch CV out · gate out · filter CV in · input
    ├── 7b Indication: status light (in tap's ring) · "• midi" dots (print, not a control)
    └── 7c Power and settings: power-on gestures (no power control is defined yet, see Q9)
```

## 3. Every control (P5RS is the panel as it stands today)
| # | Control | Branch | What it does, in player terms | Job | Half today |
|---|---|---|---|---|---|
| 1 | **bend** (joystick) | 1a | push to bend the pitch; springs back to centre | play | base |
| 2 | **mod** | 1a | how much wobble (vibrato / wah) reaches its destinations; the Model D's mod wheel as a knob | play | base |
| 3 | **glide** | 1a | how long notes slide into each other | shape / play | base |
| 4 | **blend** | 1b | what the wobble is: oscillator 3 (smooth) ↔ noise (random) | shape | base |
| 5 | **pitch** (mod → pitch) | 1b | send mod to the oscillators (vibrato) | set once | base |
| 6 | **filter** (mod → filter) | 1b | send mod to the cutoff (wah) | set once | base |
| 7 | **keys** (25) | 1c | play notes; velocity and pressure come from them | play | base |
| 8 | **touch strip** (under the keys) | 1c | pressing into a held key adds to mod or filter | play | base (hidden) |
| 9 | **release** | 1c | notes fade after you let go (the Model D's DECAY switch) | shape | base |
| 10 | **voices** 1 · 3 · 4 | 1c | one voice, three-note chords, or four with the 4th oscillator | set once | base |
| 11 | **velocity** amp · both · filter | 1c | what playing harder opens: loudness, filter, or both | set once | base |
| 12 | **touch** mod · off · filter | 1c | what pressing into a key does | set once | base |
| 13–14 | **octave 1**, **wave 1** | 2a | oscillator 1's octave and waveform | set once | lid |
| 15–17 | **octave 2**, **wave 2**, **pitch 2** | 2b | the same, plus tuning oscillator 2 against 1 (detune, intervals) | set once / shape | lid |
| 18–21 | **octave 3**, **wave 3**, **pitch 3**, **track 3** | 2c | the same; track off lets osc 3 stop following the keys (drone, slow modulator) | set once / shape | lid |
| 22–24 | **octave 4**, **wave 4**, **pitch 4** | 2d | only with the optional analog VCO 4 (§19.5); not on P5RS | set once | lid (where shown) |
| 25 | **tune** | 2e | tune the whole instrument (all oscillators) | set once | lid |
| 26 | **drift** | 2e | how much the pitch wanders like an old analog (0 = steady) | shape | lid |
| 27–29 | **mixer 1 · 2 · 3** | 3 | how much of each oscillator goes into the filter; push hard to overdrive | level | base |
| 30 | **mixer 4** | 3 | VCO 4's level (optional) | level | base |
| 31 | **extra** | 3 | level of the fourth source | level | base |
| 32 | **source** noise · input · loop | 3 | what that fourth source is: noise, the rear input, or its own output fed back | set once | base |
| 33 | **cutoff** | 4a | how bright: the hero dial | play | base |
| 34 | **resonance** | 4a | the ring at the cutoff, up to a whistle | shape / play | base |
| 35 | **envelope** | 4a | how far the filter contour sweeps the cutoff | shape | base |
| 36 | **track** off · ½ · full | 4a | how much the cutoff follows the keys (brighter up high) | set once | base |
| 37–39 | **filter attack · decay · sustain** | 4b | the shape of the filter's sweep per note | shape | lid |
| 40–42 | **amp attack · decay · sustain** | 4c | the shape of each note's loudness | shape | lid |
| 43 | **echo type** | 5a | tape · dark · clean · pingpong | shape | lid |
| 44 | **echo time** | 5a | delay length (free) or note division (sync) | shape / play | lid |
| 45 | **free · sync** | 5a | echo time by hand, or locked to tap / MIDI clock | set once | lid |
| 46 | **repeats** | 5a | how many echoes | shape | lid |
| 47 | **echo pan** | 5a | where the echoes sit, left–right | shape | lid |
| 48 | **echo level** | 5a | how much echo: also a throw at a phrase end | level / play | base |
| 49 | **reverb type** | 5b | spring · plate · hall · shimmer | shape | lid |
| 50 | **reverb decay** | 5b | how long the room rings | shape | lid |
| 51 | **reverb level** | 5b | how much reverb | level / play | base |
| 52 | **tap** | 5c | tap the tempo (echo sync); hold to show the battery; power-on gestures | play | base |
| 53 | **volume** | 6a | master loudness | level | base |
| 54 | **pan** | 6a | where the dry sound sits | level | base |
| 55 | **link** | 6a | echo pan follows the dry pan (off · on) | set once | base |
| 56–57 | **phones**, **line out** (jacks) | 6b | plug in headphones (mutes the speaker) or a mixer / recorder | level / out | rear / side |
| 58 | **speaker** | 6b | plays when phones are out (no control) | out | lid (grille) |
| 59–65 | **USB-C, MIDI in, MIDI out, pitch CV out, gate out, filter CV in, input** | 7a | charge, update, DAW; talk to other gear | set once | rear |
| 66 | **status light** | 7b | tuning faults, battery, MIDI holding a knob, mode feedback | (shows) | base (tap ring) |

## 4. Where signal order and the hands disagree
| Where | Signal order says | Hands (and the Model D) say | Which should win, and why |
|---|---|---|---|
| **Mixer** | between the oscillators and the filter | levels with the other levels (owner 20:29: "volume/mixer controls on the bottom case") | **The owner's rule** (stated). The Model D also keeps its mixer as its own panel section, not inside the oscillators. |
| **Filter: cutoff · resonance · envelope · track** | one block after the mixer, with its contour | cutoff is *played*. The Model D players ride it, and it sits on the axis under the speaker | **Hands for cutoff and resonance** (play). The contour is *shape*, so it can stay apart. Owner hasn't ruled (Q3). |
| **Modulation routing (mod → pitch / filter)** | the Model D puts each switch with its destination (OSC MOD in the oscillator bank, FILTER MOD in modifiers) | with the mod source (mod, blend) as one "where does the wobble go" group | **Hands.** One gesture, "set up the wobble", is read in one place. The Model D's split is a 1970 wiring artefact its own manual has to explain. |
| **Tune** | global: the pitch sum, before everything | the Model D puts TUNE on the Controllers panel | **Owner's rule:** "master tuning … closer to the oscillators" (20:29). It sits by the bank, as its own Tuning sub-group. |
| **Release (DECAY switch)** | belongs to both contours | the Model D puts it on the left-hand panel, with glide | **Hands / Model D:** it's a key behaviour (what happens when you let go). The owner's "key controls in one area" (13:53) points the same way. |
| **Echo / reverb levels** | after the effect, at the end | a throw gesture near the keys, beside volume | **Owner:** "i dont want those two knobs to move" (14:08). Each effect splits: character on one side, level with the levels. |
| **Tap** | a tempo source for echo (effects) | a live gesture, played near the keys | **Hands:** it's *play*. It stays with the effects category in the tree, but on the playing half. |
| **Pan / link** | output (end of the chain) | set-and-forget, with volume | **Same answer:** output, on the base with volume. |

## 5. Which half, per category
The owner's stated rules, with where each comes from:
- **R1** volume and mixer on the bottom case (20:29).
- **R2** master tuning close to the oscillators (20:29).
- **R3** the lid reads synth → effects → output (18:00).
- **R4** oscillators stacked left; filter / envelope around the speaker; the amp group in the lid's top row (20:43).
- **R5** keys controls in one area on the base, on a tighter grid (13:53, 14:08).
- **R6** echo / reverb levels stay on the base (14:08).
- **R7** the lid holds the controls, as in the first FOLD brief (owner.md line 45), later widened by the two-row base.

| Category | Half | Why (rule) | Ambiguous? |
|---|---|---|---|
| 1a Performance (bend, mod, glide) | **base** | play: beside the keys, the Model D's left-hand panel | no |
| 1b Modulation (blend, pitch, filter) | **base** | with mod (§4) | slightly: the Model D puts the switches with their destinations (Q4) |
| 1c Keyboard modes (release, voices, velocity, touch) | **base** | R5 | **yes:** does "all the key controls" include release, glide and the mod group? (Q2) |
| 2 Oscillator bank + 2e Tuning | **lid** | R4, R2 | **yes:** the tuning pair's place within the bank (beside osc 1, or its own group) is still open between P5RS-a and -b |
| 3 Mixer | **base** | R1 | no |
| 4a Filter (cutoff, resonance, envelope, track) | **base** today | play; CUTOFF under the speaker axis (steer 2) | **yes:** R4 says "filter / envelope around the speaker" on the lid. Does "filter" there mean the contour only? (Q3) |
| 4b–4c Contours | **lid** | R4 | R4 calls the amp group the "top row"; P5RS puts the filter contour there (owner's 13:53 markup), so his two statements differ (Q5) |
| 5a–5b Effects character (type, time, free/sync, repeats, pan, decay) | **lid** | R3 (synth → effects) | no |
| 5a–5b Effect levels | **base** | R6, R1 | no (decided 14:08) |
| 5c Tap | **base** | play | **yes:** R3 "synth → effects" could pull it onto the lid with echo (Q6) |
| 6a Output (volume, pan, link) | **base** | R1 | **yes:** R3 ends the lid with "output stuff like volume", but R1 puts volume on the base. Is the lid's last group effects, or should something of output be there? (Q1) |
| 6b / 7a Jacks and ports | **rear / sides** | not a panel question | which side the phones go on (Q7) |
| 7b Status light | **base** (tap ring) | it reports play states | no |

## 6. Owner questions (not resolved here)
1. **Q1:** R3 says the lid reads "synth → effects → output stuff like volume", but R1 puts volume on the base. Is it right that the lid now ends at effects and all of output lives on the base?
2. **Q2:** "All the key controls in one area" (13:53): which ones? Voices · velocity · touch only, or also release (the Model D's DECAY), glide, and the mod group (mod · blend · destinations)?
3. **Q3:** "Filter / envelope around the speaker" (20:43): the filter *contour* only, or also cutoff and resonance? Today cutoff (played) is on the base under the speaker's axis.
4. **Q4:** Modulation: keep the destination switches with mod (one "wobble" group, today), or follow the Model D and put them with the oscillators and the filter?
5. **Q5:** The lid's top row: amp group (20:43) or filter contour (your 13:53 markup)?
6. **Q6:** Tap: with the playing controls on the base (today), or with echo on the lid?
7. **Q7:** Jacks: phones on the player's side or the rear? (Not a panel question; noted so it isn't forgotten.)
8. **Q8:** VCO 4: in the tree as optional. Is it in or out of the spec for the layout we draw next?
9. **Q9 (eng + owner):** the power-on gestures say "while switching on", but no power control is defined. The lid Hall switch only gives sleep, and that is proposed. Is opening the lid "on", or is there a switch?

## 7. What this means for the next layout (no layout yet)
- **On the base:** the hands and the levels.
  - Controllers: performance + modulation + keyboard modes.
  - The filter's played pair: cutoff, resonance, with envelope and track.
  - Mixer, tap, effect levels, output.
- **On the lid:** what you set up and shape.
  - Oscillator bank + tuning.
  - Both contours.
  - The effects' character.
- The base has 2 rows today and is the tighter half. The counts are base 25 controls (26 with VCO 4), plus the keys, and lid 24 (27 with VCO 4). Any answer to Q2–Q3 that moves more onto the base needs the finer grid of §31.2.
