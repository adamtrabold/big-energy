# Control taxonomy: what every control is for, before any layout
Status: **proposed** (team), for the owner to correct · revised 2026-11-19 after director 8 / critic 8 · sources:
- [owner.md](../design/owner.md) (the 2026-11-19 14:36 ask);
- the Minimoog Model D manual ([`design/owner-refs/Minimoog_Model_D_Manual.pdf`](../design/owner-refs/Minimoog_Model_D_Manual.pdf), "Features & Controls", pp. 15–33);
- the [feature docs](README.md);
- the current panels (P5RS, `design/branches/concepts/cathedral/layout_check.py`).

**The owner's request (14:36, verbatim):** "let's start by doing a tree map or something first and just define the categories of controls and what controls belong in those categories before laying anything out."

This page lays nothing out. It covers:
- every **panel control** and what it's for;
- how the controls group;
- which half each group belongs on, under his stated rules;
- what's not on the panel;
- what the spec hasn't decided yet;
- his questions, each with the team's default.

**The count: 53 panel controls with VCO 4, 49 without.** The keys and the touch strip are the playing surface. Jacks, the speaker, the status light and the "• midi" print aren't panel controls. All of those are listed in §6.

## 1. The four jobs a control serves
| Job | Meaning | Example |
|---|---|---|
| **set once** | set before playing (or per patch / song), then left alone | octave, source, voices |
| **shape** | sculpt the sound between phrases: turned often, rarely during a note | envelopes, wave, echo type |
| **play** | moved *while* notes sound, with a hand off the keys | bend, mod, cutoff, release, tap |
| **level** | how loud, where it goes | mixer, volume, pan, effect levels |

Many controls do two jobs ("shape / play"). The job decides which half a control goes on, so a control that is ever **played** counts as play first.

## 2. The tree
The first five branches are the Model D's own panel sections, in its left-to-right order: Controllers · Oscillator Bank · Mixer · Modifiers · Output.
- The manual puts the wheels, the glide switch and the DECAY switch on the **left-hand keyboard panel**, and the jacks on the **top patch panel**.
- Big Energy adds one branch, **Effects**, between the amp and the output (its place in the signal).
- ★ marks an addition to the Model D. Counts are in brackets.

```
Big Energy: 53 panel controls (49 without VCO 4)
├── 1 CONTROLLERS (10)          Model D: Controllers panel + left-hand panel
│   ├── 1a Performance (4):      bend (stick) · mod · glide · release
│   ├── 1b Modulation (3):       blend · pitch · filter        (where the wobble comes from and goes)
│   └── 1c Keyboard setup (3) ★: voices · velocity · touch     (the owner's "key controls")
├── 2 OSCILLATOR BANK (14 / 11)
│   ├── 2a Oscillator 1 (2):     octave · wave
│   ├── 2b Oscillator 2 (3):     octave · wave · pitch
│   ├── 2c Oscillator 3 (4):     octave · wave · pitch · track 3
│   ├── 2d Oscillator 4 (3) ★:   octave · wave · pitch          (optional analog VCO 4)
│   └── 2e Tuning (2):           tune · drift ★                 (Model D: TUNE is on Controllers; see §4)
├── 3 MIXER (6 / 5):             1 · 2 · 3 · (4 ★) · extra · source
├── 4 MODIFIERS (10)
│   ├── 4a Filter (4):           cutoff · resonance · envelope · track
│   ├── 4b Filter contour (3):   attack · decay · sustain
│   └── 4c Loudness contour (3): attack · decay · sustain
├── 5 EFFECTS (10) ★
│   ├── 5a Echo (6):             type · time · free/sync · repeats · pan · level
│   ├── 5b Reverb (3):           type · decay · level
│   └── 5c Tempo (1):            tap  (its ring is the status light: never cover or crowd it)
└── 6 OUTPUT (3)
    └── 6a Master (3):           volume · pan ★ · link ★
```

## 3. Every panel control (P5RS is the panel as it stands today)
| # | Control | Branch | What it does, in player terms | Job | Half today |
|---|---|---|---|---|---|
| 1 | **bend** (joystick) | 1a | push to bend the pitch; springs back to centre | play | base |
| 2 | **mod** | 1a | how much wobble reaches its destinations: the Model D's mod wheel, as a knob | play | base |
| 3 | **glide** | 1a | how long notes slide into each other | shape / play | base |
| 4 | **release** | 1a | notes fade after you let go (the Model D's DECAY switch): flicked mid-phrase for staccato vs tails | **play** | base |
| 5 | **blend** | 1b | what the wobble is: oscillator 3 (smooth) ↔ noise (random) | shape | base |
| 6 | **pitch** (mod → oscillators) | 1b | bring vibrato in: flipped on over a held note with mod already up | **shape / play** | base |
| 7 | **filter** (mod → cutoff) | 1b | bring wah in, the same way | **shape / play** | base |
| 8 | **voices** 1 · 3 · 4 | 1c | one voice, three-note chords, or four with the 4th oscillator | set once | base |
| 9 | **velocity** amp · both · filter | 1c | what playing harder opens: loudness, filter, or both | set once | base |
| 10 | **touch** mod · off · filter | 1c | what pressing into a key does | set once | base |
| 11 | **octave 1** | 2a | oscillator 1's octave | set once | lid |
| 12 | **wave 1** | 2a | oscillator 1's waveform (the 4th oscillator copies it) | shape | lid |
| 13–15 | **octave 2**, **wave 2**, **pitch 2** | 2b | the same, plus tuning osc 2 against osc 1 (detune, intervals) | set once · shape · shape | lid |
| 16–19 | **octave 3**, **wave 3**, **pitch 3**, **track 3** | 2c | the same; track off lets osc 3 stop following the keys (drone, slow modulator) | set once · shape · shape · set once | lid |
| 20–22 | **octave 4**, **wave 4**, **pitch 4** | 2d | only with the optional analog VCO 4; not on P5RS | set once · shape · shape | lid (where shown) |
| 23 | **tune** | 2e | tune the whole instrument | set once | lid |
| 24 | **drift** | 2e | how much the pitch wanders like an old analog (0 = steady) | shape | lid |
| 25–27 | **mixer 1 · 2 · 3** | 3 | how much of each oscillator goes into the filter; push hard to overdrive | level / shape | base |
| 28 | **mixer 4** | 3 | VCO 4's level (optional) | level / shape | base |
| 29 | **extra** | 3 | level of the fourth source | level | base |
| 30 | **source** noise · input · loop | 3 | what that source is: noise, the rear input, or its own output fed back | set once | base |
| 31 | **cutoff** | 4a | how bright: the hero dial | play | base |
| 32 | **resonance** | 4a | the ring at the cutoff, up to a whistle | shape / play | base |
| 33 | **envelope** | 4a | how far the filter contour sweeps the cutoff; ridden with cutoff as one gesture | **shape / play** | base |
| 34 | **track** off · ½ · full | 4a | how much the cutoff follows the keys | set once | base |
| 35–37 | **filter attack · decay · sustain** | 4b | the shape of the filter's sweep per note | shape | lid |
| 38–40 | **amp attack · decay · sustain** | 4c | the shape of each note's loudness | shape | lid |
| 41 | **echo type** | 5a | tape · dark · clean · pingpong | shape | lid |
| 42 | **echo time** | 5a | delay length (free) or division (sync); swept for pitch dives | **shape / play** | lid |
| 43 | **free · sync** | 5a | echo time by hand, or locked to tap / MIDI clock | set once | lid |
| 44 | **repeats** | 5a | how many echoes; ridden into self-oscillation | **shape / play** | lid |
| 45 | **echo pan** | 5a | where the echoes sit, left–right | shape | lid |
| 46 | **echo level** | 5a | how much echo; a throw at a phrase end | level / play | base |
| 47 | **reverb type** | 5b | spring · plate · hall · shimmer | shape | lid |
| 48 | **reverb decay** | 5b | how long the room rings | shape | lid |
| 49 | **reverb level** | 5b | how much reverb | level / play | base |
| 50 | **tap** | 5c | tap the tempo (echo sync); hold to show the battery | play | base |
| 51 | **volume** | 6a | master loudness: phones, line out and speaker together, as drawn today (see S5) | level | base |
| 52 | **pan** | 6a | where the dry sound sits | level | base |
| 53 | **link** | 6a | echo pan follows the dry pan | set once | base |

**The lid holds some playing controls.** These are echo time and repeats (shape / play). The lid's row nearest the player should go to them.

## 4. Where signal order and the hands disagree
| Where | Signal order says | Hands (and the Model D) say | Which should win, and why |
|---|---|---|---|
| **Mixer** | between the oscillators and the filter | with the other levels (owner 20:29: "volume/mixer controls on the bottom case") | **The owner's rule.** On the base it feeds the filter directly below it. |
| **Filter: cutoff · resonance · envelope · track** | one block with its contour | cutoff and envelope amount are *played* together. They sit on the axis under the speaker | **The hands, for the played four.** The contour is shape and can sit apart: above them (rule H, §5). |
| **Mod routing (pitch / filter switches)** | the Model D puts each switch at its destination (OSC MOD in the bank, FILTER MOD in modifiers) | with mod and blend, as one "where does the wobble go" group | **Both sides, fairly:** the Model D's way shows, module by module, what is being modulated. The grouped way reads one gesture in one place, and it's the switches you reach for blind while mod is up. **Team default: with mod** (Q5). |
| **Tune** | global: the pitch sum, before everything | the Model D puts TUNE on its Controllers panel | **The owner's rule:** "master tuning … closer to the oscillators" (20:29). Where exactly is Q1. |
| **Release (DECAY switch)** | belongs to both contours | the Model D puts it on the left-hand panel, by glide: a performance switch | **The hands:** release joins glide in 1a. |
| **Echo / reverb levels** | at the end of each effect | throws, near the keys, beside volume | **The owner:** "i dont want those two knobs to move" (14:08). Each effect splits: character on the lid, level on the base, lined up (rule H). |
| **Tap** | a tempo source for echo | a live gesture near the keys | **The hands:** filed under Effects, placed on the playing half. |
| **Pan / link** | output, at the end | set-and-forget, with volume | **The same answer:** output, on the base. |

## 5. Which half, per category
**The owner's stated rules:**
- **R1** volume and mixer on the bottom case: "volume/mixer controls on the bottom case" (20:29).
- **R2** master tuning close to the oscillators: "master tuning controls should be closer to the oscillators" (20:29).
- **R3** the lid reads synth → effects → output: "when i think of signal order it's synth stuff -> fx stuff -> output stuff like volume" (18:00).
- **R4** "the oscillators should all be stacked on the left, then top case filter/envelope where there's less room cuz of speaker in the middle, then amp controls going left to right in the top row on the top case" (20:43).
- **R5** key controls in one area on the base, on a tighter grid: his markup (13:53) and "making the switches a bit tighter / in a proprotional multiple of the grid" (14:08).
- **R6** echo / reverb levels stay: "i dont want those two knobs to move" (14:08).

**The team's layout rule (from P5OB-D, the layout that scored 10):**
- **H: a category split across the hinge lines up above itself.** With the lid standing, each half of a split category sits directly over the other: filter contour over cutoff · resonance · envelope; echo / reverb character over their levels; the oscillators over the mixer channels that carry them. P5OB-D's mixer 1–4 over the filter row and its effects over out are the worked case. A split that doesn't line up reads as two unrelated groups.

| Category | Half | Why | Ambiguous? |
|---|---|---|---|
| 1a Performance (bend, mod, glide, release) | **base** | play: by the keys, the Model D's left-hand panel | no |
| 1b Modulation (blend, pitch, filter) | **base** | with mod (§4) | the destination question (Q5) |
| 1c Keyboard setup (voices, velocity, touch) | **base** | R5 | which controls R5 covers (Q2a–d) |
| 2 Oscillator bank | **lid** | R4 | no |
| 2e Tuning | **lid** | R2 | **yes:** beside oscillator 1, or centred over the speaker (Q1) |
| 3 Mixer | **base** | R1; under the oscillators (H) | no |
| 4a Filter, the played four | **base** | play; CUTOFF on the speaker's axis | R4's "filter/envelope … around the speaker" (Q3) |
| 4b–4c Contours | **lid** | R4; over the filter (H) | which contour takes the top row (Q4) |
| 5a–5b Effects' character | **lid** | R3 | no |
| 5a–5b Effect levels | **base** | R6; under the character (H) | no (decided) |
| 5c Tap | **base** | play | R3 could pull it to the lid with echo (Q6) |
| 6a Output (volume, pan, link) | **base** | R1 | R3 ends the lid with "output" (Q7) |

## 6. Not on the panel
| Item | What it is | Where |
|---|---|---|
| **keys** (25, Choc V2, Hall-sensed) | the playing surface: notes, velocity, pressure | base |
| **touch strip** (FSR under the keys) | the pressure sensor behind "touch"; no panel presence | base, hidden |
| **phones**, **line out** | jacks | case wall (Engineering E1) |
| **USB-C** | charging, USB-MIDI, firmware updates | rear |
| **MIDI in / out** (3.5 mm TRS) | other gear | rear |
| **pitch CV out**, **gate out**, **filter CV in**, **input** | patch jacks; input feeds source: input | rear |
| **speaker** | plays when phones are out | lid, under the grille |
| **status light** | in tap's ring: tuning faults, battery, MIDI holding a knob | base |
| **"• midi" dots** | print: which knobs a DAW can move | lid's top heading line |

**Hidden settings (no knob; set by power-on gestures, [firmware and gestures](features/firmware-update-and-gestures.md), all proposed).** The layout must never assume a panel control for these:
- **Hold the lowest key at power-on:** MIDI channel 1–16, omni, MIDI extras.
- **Hold the highest key at power-on:**
  - velocity curve;
  - aftertouch span;
  - filter note in chords (highest / lowest);
  - **bend range ± 2 / ± 7 / ± 12**;
  - pressure out on / off.
- **Hold tap at power-on:** full autotune re-sweep.
- **Hold tap + bend up at power-on:** firmware update.
- **Resonance full + tap at power-on:** filter calibration.
- **Hold tap ≥ 1.5 s while playing:** battery level.

**Model D controls left out on purpose (one line each):**
- the mixer's per-source on / off switches (a level at zero does it, but the setting is lost);
- the noise colour switch (white / pink);
- the A-440 reference (autotune replaces it);
- a separate phones volume (see S5);
- the main output on / off switch;
- the glide on / off switch (see S1);
- the reissue's LFO and its two mod-source switches (blend is osc 3 ↔ noise only).

## 7. Spec gaps (listed, not added; current status from the feature docs)
| # | Gap | Current spec | Status |
|---|---|---|---|
| S1 | **Glide on / off.** The Model D has a switch; players flick glide in for one phrase. | glide time only (0 = off); no switch | not in spec (Q8) |
| S2 | **Vibrato on chords.** In PARA, osc 3 is a voice. Its FM on chords is clangy; with track off, PARA drops to two voices. So vibrato on chords means noise, or losing a voice. | the paraphonic doc notes the clang only | open (Q9). Pitch is summed in firmware, so eng could look at a firmware vibrato; not proposed here |
| S3 | **Aftertouch amount.** | no amount control: MOD adds up to +50 % of mod's range, FILTER up to +2 octaves on cutoff (firmware). Span and curve are a power-on setting | decided switch; amounts proposed (Q10) |
| S4 | **Bend range.** | ± 2 default; ± 2 / 7 / 12 as a setting | open (bend-and-mod) |
| S5 | **What volume sets.** | one dual pot after pan feeds phones, line out and the speaker together | proposed (panning diagram) (Q11) |
| S6 | **Glide and MIDI CC 65** (portamento on / off) | not handled | open, only if S1 adds a switch |

## 8. Owner questions, each with the team's default (answer "yes" to take it)
1. **Q1 Tuning:** tune · drift **centred over the speaker** as their own pair (P5RS-a), rather than beside oscillator 1's wave (P5RS-b, which leaves a 71.8 mm open space above the speaker)? *Default: yes, centred (a).* Both are drawn so you can choose by eye.
2. **Q2a** Release sits beside glide (performance), not with voices · velocity · touch? *Default: yes.*
3. **Q2b** Glide stays a knob with the performance controls (bend · mod · glide · release)? *Default: yes.*
4. **Q2c** The mod group (blend · pitch · filter) sits next to the key controls on the base, but as its own group? *Default: yes.*
5. **Q2d** "All the key controls" means voices · velocity · touch: set once, one group? *Default: yes.*
6. **Q3** "Filter/envelope around the speaker" means the two **contours** on the lid. Cutoff · resonance · envelope · track stay on the base under the speaker's axis? *Default: yes.*
7. **Q4** The lid's top row takes the **filter contour** (your 13:53 markup), with amp below it? Your 20:43 note had amp on top. *Default: yes, the filter contour (the later word).*
8. **Q5** The two mod destination switches stay **with mod**, not at the oscillators and the filter as on the Model D? *Default: yes.*
9. **Q6** Tap stays on the base with the playing controls (not on the lid by echo)? *Default: yes.*
10. **Q7** The lid ends at effects, and all of "output" (volume, pan, link) lives on the base (R1 over R3's last step)? *Default: yes.*
11. **Q8** No glide on / off switch; glide at zero is off (S1)? *Default: yes (a deliberate omission). Saying no adds one switch beside release.*
12. **Q9** Vibrato on chords comes from noise, or from turning osc 3's track off (two-voice chords) (S2)? *Default: yes, accept it for now.*
13. **Q10** Aftertouch amounts fixed in firmware, with span / curve as a power-on setting: no amount knob (S3)? *Default: yes.*
14. **Q11** Volume sets phones, line out and the speaker together (S5)? *Default: yes. Saying no adds a phones level, or fixes line out.*
15. **Q12** VCO 4: the next layout is drawn with 3 oscillators, and VCO 4 is shown as the option it is? *Default: yes.*

## 9. Engineering list (not layout questions)
- **E1:** phones jack placement: player's side or rear (enclosure).
- **E2:** the power-on gestures say "while switching on", but no power control is defined. The lid Hall switch only gives sleep (proposed). Is opening the lid "on", or is there a switch?

## 10. What this means for the next layout (no layout yet)
- **Base:** the hands and the levels.
  - Performance + modulation + keyboard setup.
  - The filter's played four.
  - Mixer, tap, effect levels, output.
  - That's 25 controls (26 with VCO 4), plus the keys.
- **Lid:** what you set up and shape.
  - Oscillator bank + tuning.
  - Both contours.
  - The effects' character.
  - That's 24 controls (27 with VCO 4). The row nearest the player goes to echo time and repeats.
- **Rule H** decides the columns: every split category lines up across the hinge.
