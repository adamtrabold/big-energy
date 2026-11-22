# BOW: how it works (systems)

Status: **rev 1, 2026-11-22**, concept round 1. Read `../common-how-it-works.md` first; this file states only BOW's own parts and departures. Visual: `how-it-looks-and-feels.md` (theirs).

**Life lives in each finger.** Every note is its own player: how you strike sets how fast it arrives, how you lean keeps it alive, how you lift lets it go.

**Draws on:** BOW (jam turns 1, 3, 5), SIX STRANDS (turn 1, as the strands of pitch, turns 3–4), SAIL (turn 2: lid as soundbox), the half-map and duet (turns 2, 6), and the visual faces in turn 6.

## 1. Structure

### 1.1 Body
- **CATHEDRAL's base** (286 × 132 [ENG, Big Energy `design/branches/concepts/cathedral/`]), with its keys, hinge and stays.
- **The lid has no controls.** It's the soundbox: the driver and the passive radiator in a sealed box behind cloth (visual turn 2). Eng: is the lid deep enough? (open since turn 2).
- **Lid = power.** A magnet and a Hall sensor at the hinge: opening past ≈ 20° switches on, closing switches off. The closed lid covers the keys, so it can't switch on in a bag (J14). No other power switch on the face. A recessed rear switch stays as a **ship-mode cutoff** (battery fully off), as in the family.

### 1.2 Panel map (PROPOSAL; visual places it by script)
The base has two rows (front y 68, rear y 93, CATHEDRAL's) and the centre gutter over middle C (x 134–152, axis 143).

**Left of the gutter is the instrument; right of it is the room.**

| | Left region (x ≈ 19–110) | Left strand column | Gutter | Right strand column | Right region (x ≈ 176–267) |
|---|---|---|---|---|---|
| **Front y 68** (played amounts) | OCTAVE L · TONE · DEPTH · HOLD | low / main / high, stacked | status light | low / main / high, stacked | ECHO · REVERB · VOLUME · OCTAVE R |
| **Rear y 93** (kinds, times, ranges) | ATTACK · RELEASE · **PRESSURE** (coral) · SHIMMER | (column continues) | TAP | (column continues) | TIME · FREE / SYNC · REPEATS · *(blank)* |

- **Reading:**
  - The rear row runs TOUCH (attack, release, pressure), then the shimmer mode, then the echo's times.
  - The front row runs colour (tone), shimmer amount and hold, then the two strand columns either side of the gutter, then echo, reverb, out.
  - The octaves sit at the outer ends.
- **Per-half controls:** OCTAVE L and R, both strand columns, and HOLD. HOLD is left-half only, so it sits at the left region's inner end, beside the left strands.
- **The blank slot** (rear, far right) stays blank. Don't reflow the row (Big Energy precedent). If anything earns it later, the candidate is reverb decay.
- **Count:** 15 round controls or switches + 6 strand tabs + TAP + status light; 16 slots, one blank.

### 1.3 Does the three-deep strand column fit? (visual's turn 6 question) **Yes** [CALC, PROPOSAL]
- **Tabs:** mini rockers ≈ 15 × 10 mm (Tayda-class "mini rocker 10 × 15", part UNVERIFIED), turned so the 10 mm side runs front to back. Pitch 12, centres at y 60 / 72 / 84, so the column runs y 55–89.
- **Clearances:** sharps end at y ≈ 49, so 6 mm clear. Each column is 15 mm wide: left x 117–132, right x 154–169, which leaves 2 mm to the gutter for the names.
- **No row knob sits in the column's x span,** so the rear row's knob fronts (y 85.75) don't meet it. The nearest knob edges in the regions: left HOLD / SHIMMER at x ≈ 101 to 110 (≥ 7 mm from 117 ✓); right ECHO / TIME at ≥ 176 (7 mm from 169 ✓).
- **Strand names** (low · main · high) print once in the gutter, at y 60 / 72 / 84. The status light goes in front of them (gutter, y ≈ 52, at the keys) or behind at y ≈ 100 with TAP at y ≈ 112. Visual to choose; both fit in 132.

## 2. Engine (BOW's departures from common §1)

### 2.1 Strands of pitch
- **Each key sounds up to three strands: an octave below, at pitch, an octave above.** Six tabs: three per half. A tab turns that strand on or off for its half's keys only.
- **How (PROPOSAL, eng to size), the 1974 way:** the tone source makes **2f per key** (25 outputs, not 75). A **CD4520 dual 4-bit counter** divides it to f and f/2: one counter per key, 13 DIP chips. That's the Solina's own divide-down trick, through-hole, and it closes turn 4's "75 tone outputs" risk.
- **Turning a strand off per half** needs a gate per strand per key: 75 analog switches (≈ 19 × CD4066, DIP), driven by 6 lines (3 strands × 2 halves).
  - Alternative: a small CPLD or FPGA does tones, division and gating in one part. Fewer chips, but not hand-solderable through-hole. That's an owner question (J21).
  - **My recommendation is the DIP route.** It's more chips, but each one is a part he can solder.
- **"Rounded toward a sine":** per-strand RC smoothing per key would be 75 more RCs. The cheaper route is to mix square strands and let the shared TONE filter round them. Start there; eng says whether it's warm enough.
- **Breath (common §2.4) counts strands:** three strands on a key is louder than one. The breath normalises the sum, so turning on more tabs thickens without jumping in level.

### 2.2 Velocity means speed
- **Hard strike = fast attack; soft = slow bloom**, within ATTACK's range. ATTACK sets the slowest bloom (the softest strike); the hardest strike arrives near instantly.
- **Velocity doesn't change loudness:** every note arrives at full level, just at its own pace. That's what makes BOW different from KEPT. If the owner wants loudness too, it's a firmware curve, not a switch.
- **Lift = tail** (common §2.2). Strike, lean, lift: the whole bow stroke.

### 2.3 Pressure (coral: BOW's hero)
- Default position **swell**: leaning on a held key keeps it full and can grow it ≈ +6 dB over its strike level (PROPOSAL).
- **BOW's held note thins without pressure:** in swell, a held note with no pressure sinks slowly to ≈ −6 dB over ≈ 4 s (bow speed fading); leaning brings it back. This is the "bowing" behaviour.
  - It applies only in **swell** and only while per-key pressure works. On the shared-strip fallback, it's off (otherwise every chord would sink unless you pressed the strip).
  - With HOLD, held notes don't thin.

### 2.4 HOLD: left half
- Common §2.5. **New chord replaces:** a new chord in the left half, played after every left key is up, replaces the held one.
- Why only the left: the right hand's lean and lift are BOW's point, and holding it would make them idle.
- With both octaves equal, HOLD still acts on the left 12 keys (C3–B3 at 0).

## 3. Flows (BOW-specific steps; others as `../../jobs.md`)

**F1 Grab and play.**
1. Bag out; open the lid. Past ≈ 20° it's on, and the status light goes steady.
2. At CATHEDRAL's stay angle, the lid's cloth faces you.
3. Play.
- Lid flat on a table: the sound fires upward; fine.
- Lid shut mid-play: the sound fades in ≈ 0.5 s, then off.

**F2 Split.** Common. The strand tabs then give each half its own colour: left low + main (cello-like), right main + high (violins).

**F3 Play expressively.**
1. Soft strike: a slow bloom. Hard: a bite.
2. Lean: the note swells (or thins without it, §2.3).
3. Lift slowly: a long tail. Snatch off: short.

**F5 Colour.**
1. Strand tabs per half.
2. TONE rounds or brightens everything.
3. All three tabs of a half off = that half silent (common §2.6).

**F13 Duet.** The friend gets OCTAVE R, the right strand column, ECHO / REVERB / VOLUME, all in front of them. You keep HOLD and TONE / DEPTH / TOUCH. That's an honest split of the panel, though the friend also gets the volume.

**F14 Pack.** Close the lid: off, and the keys are covered. The lid self-protects the face (CATHEDRAL), so no sleeve is needed.

## 4. States (beyond common)
| State | What happens | What you see |
|---|---|---|
| Lid opening | on at ≈ 20°; sound ready at once | status light steady |
| Lid closing while playing | ≈ 0.5 s fade, off | light off |
| Lid open, battery flat | no sound | light flashing, then off |
| All six tabs off | silent | all tabs down |
| One half's tabs off | that half silent (mute) | that column all down |
| Swell, no pressure, held note | sinks slowly ≈ −6 dB | — (heard) |
| HOLD on, left chord held, right playing | left sustains; right fully expressive | HOLD dot lit |
| 25 keys × 3 strands | breath normalises; no clip | — |
| Shared-strip fallback | swell = whole-instrument swell; no thinning | same panel |

## 5. Coverage against `jobs.md` (round 1, self-check)
| Job | Supported? Where |
|---|---|
| J1 strings anywhere | yes: battery, lid speaker, lid = on |
| J2 every key | yes: common §1 |
| J3 split | yes: common §2.1 |
| J4 velocity per note | yes: speed (§2.2) |
| J5 pressure + selector | yes: coral PRESSURE, swell default (§2.3) |
| J6 lift | yes: common §2.2 |
| J7 colour per half | yes: strands per half (§2.1) |
| J8 shimmer | yes: SHIMMER + DEPTH |
| J9 echo / reverb / tempo | yes: common §2.7 |
| J10 hold | yes: left half (§2.4) |
| J11 speaker / phones | yes |
| J12 MIDI | yes: common §2.10 |
| J13 read state | yes: tabs, pointers, light; lid open = on is visible |
| J14 instant start | yes: the lid is the start |
| J15 park | partly: stable on a bench; **on a lap, the lid's weight may tip it backwards** (director, turn 3). Eng: the stays' angle and the centre of mass |
| J16 breath | yes |
| J17 tuning | yes: rear TUNE |
| J18 duet | yes: §3 F13 |
| J19 point of view | yes: one idea (each note bowed) in the engine, keys and lid |
| J20 family | yes: CATHEDRAL base, key strip, hinge |
| J21 build / fix | **at risk:** about 32 more DIP chips for strands (§2.1); a CPLD route isn't hand-solderable |

## 6. Push, risks, open
- **Push:** strands in the 1974 way (counters) is both cheaper and more honest to "floss" than a big chip. I'd lead with it.
- **Risk 1:** chip count (25 VCAs + 13 counters + 19 switches). Eng: board area in a 286 × 132 base with the battery strip.
- **Risk 2:** lap tipping with a speaker in the lid.
- **Open:**
  - Does the thinning in swell (§2.3) feel alive or just annoying? It needs a test key, then the owner.
  - The status light's place in the gutter (visual).
