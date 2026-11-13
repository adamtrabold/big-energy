# Director scores: instrument physical form

## Concept building, round 1: steering scores (NOT passed to the owner)

**Verdict: no concept is at 9. Send the designers round again.** These are
steering scores, kept so that later rounds can show what really changed. Each
concept is scored on the idea and judged against its own kind (designed for
use or sauce), not on polish.

Based on: `concepts/{case,dock,motto,dish}/*-mock.png`,
`look-sheet.png`, `size-sheet.png`, `common-how-it-works.md`,
`common-looks-and-feels.md`, each concept's `how-it-*.md`, jobs.md,
owner.md (all entries), and eng/architecture-v2.md §2–4.

| Concept | Kind | Score | One line |
|---|---|---|---|
| CASE | designed for use | **6** | It works, but it's the thickest closed (≈ 50 mm), has a hinge, a cable and a leg, and its top view is identical to DOCK's. **Replace it** (see R2). |
| DOCK | designed for use | **7** | The best designed-for-use idea: one flat 30 mm slab when played, the most OP-1 in spirit. Held back by the cramped panel, pillow keys that risk reading as "pads", and 52 mm when carried. |
| MOTTO | sauce | **7** | The strongest identity in the set. The painted lid standing behind the panel like an altarpiece fits his "hand paint it", and the bentside silhouette is the instrument's own. Held back by the cramped panel, wrong MIDI-light scope, an all-walnut-plus-black-panel read drifting toward "wood synth", and an unverified reflector. |
| DISH | sauce | **6** | The most original. But **as drawn it doesn't work electrically**: the dish carries the mixer, waveforms, emphasis and mod mix, which eng §2 keeps as analog pots in the audio path. So ±10 V and audio would cross the pivot, and its own doc calls that "not viable". The speaker in the bullseye is too small to be "incredible". It's fixable, and the fix makes it better (see R5). |

### Likely owner objections, set-wide
1. **"It looks cramped. I said feel outranks OP-1."** Every panel was squeezed
   into 276 × 70 mm: 10 mm mixer caps at a 14 mm pitch, **6 faders at a
   7.5 mm pitch**, and legends he'd have to hand-letter at 1.4–2.4 mm. He said
   "dont over index on OP1… it should feel good to use", and eng's
   realistic box is ≈ 285 × 180 × 32–36 mm. **Highly likely.**
2. **"These all look like the same synth."** CASE, DOCK and MOTTO share an
   identical panel, and the mocks invite a spot-the-difference reading. CASE
   and DOCK are near-twins from above. **Likely.**
3. **"Pads, not keys"** (DOCK's TPU pillows), and **"a toy"** (DISH's round
   buttons). Neither can be judged from a picture. **Likely, unless samples
   exist.**
4. **"The MIDI light only covers cutoff and glide?"** The concepts assume only
   cutoff and glide are MIDI-ownable. Eng v2 §2 says: notes, bend, glide,
   TUNE, osc 2/3 FREQ, cutoff, and **both envelopes' A/D/S**. That's 11
   continuous controls, 6 of them the faders. MOTTO's 2 pips and DISH's
   cutoff-only bullseye answer the wrong question. **Certain once he reads
   them.**
5. **"Is that speaker incredible?"** 36 mm (CASE, DOCK), the rose (MOTTO,
   size unclear) and 22–28 mm (DISH) don't add up to "incredible". **Likely.**
6. **Trade dress:** CASE in Proof (a walnut surround with a tilted panel behind
   the keys) and MOTTO (a walnut body around a black panel with a big knob
   at the left) drift toward the original's posture and materials. **Possible.**
7. **Cost:** he reset the budget. Hinges, forks, pogo pins, walnut and lids
   all cost money, and no concept states its delta. **Possible.**

### Fixes for round 2 (numbered rulings)

**R1. Size: design to feel, inside eng's box, for all concepts.**
- Target ≈ **285 wide × 170–190 deep (played) × ≤ 36 mm thick**, with pouch
  LiPo cells (eng §4.2).
- The 102 mm OP-1 depth is dropped as a target. The orange "breaks OP-1
  depth" marks on the size sheet are now wrong framing. Redraw the size sheet
  against eng's box.
- The panel grows to ≈ **95–105 mm deep**.
  - Minimums: standard caps ≥ 12 mm Ø at ≥ 17 mm pitch; faders ≥ 11 mm
    pitch, ≥ 20 mm travel.
  - Hand-lettered legends at **≥ 2.5 mm cap height**. He'll draw them, and
    they have to survive scanning.
- MOTTO (193) and DISH (189) now sit roughly **inside** the box. Their depth
  is no longer a penalty, but don't grow them further.

**R2. CASE is cut. Replace it with SLAB: "the lid becomes the stand".**
- **The problem with CASE:** its only difference from DOCK is the mechanism,
  and that mechanism is the most expensive and the thickest of the set.
- **SLAB is the conventional, best-for-the-job answer the owner implicitly
  asked for:** one rigid body with no moving joint and no cable crossing
  anything. That makes it the cheapest and the most IKEA.
  - A separate laser-stacked **lid** snaps over the panel and keys with
    magnets for carrying. That's protection (J16), and it trips the
    sleep Hall sensor.
  - To play, the lid flips underneath and becomes a **wedge stand** that
    tilts the whole unit about 8–12° toward the player. So the panel tilt
    survives without a hinge.
- It must differ from DOCK **in kind**. DOCK separates the keys, while SLAB
  only separates the cover. The mock must make that visible: show the lid
  as a stand.
- **Why replace, not refine:** no fix to CASE removes its hinge, cable and
  thickness without turning it into SLAB.

**R3. DOCK: earn the 9.**
1. **Keys:** default to the **short Delrin lever** keys (the most
   "instrument" of the four). The TPU pillow moves to the key menu (R6).
2. **Carry:** get below 45 mm carried. Can the module's rim drop into a
   shoulder around the sunken panel instead of standing on it? Show the
   section.
3. **Dock feel:** in the mock, show the magnets, the locating cones, the pogo
   pins, and what's on the panel edge when the module is away.
4. **Speaker:** ≥ 40 mm, with the 60 mm magnet rule shown.

**R4. MOTTO: keep it. It's the sauce lead.**
1. **Material read:** move away from walnut-around-black-panel.
   - Try the **Proof white panel** or a **bone/limewood-tone body**, or a
     painted body (harpsichords were painted outside too).
   - Walnut, if used at all, goes only on the lid's outside.
   - The goal: nobody says "Moog" at a glance.
2. **Lid painting placeholder:** replace the sunset with something abstract
   and clearly a placeholder (a graphic field, ruled lines, the motto ribbon
   alone). A kitsch placeholder will get judged as the proposal.
3. **Rose and speaker:** state the driver size (≥ 40 mm) and how the rose
   pattern is cut. Eng should give a rough check on the lid-reflector
   claim, or the mock should say "unverified".
4. **"Not in control":** per-control pips, but for **all 11** MIDI-ownable
   continuous controls (glide, tune, freq 2, freq 3, cutoff, 6 contour faders).
   One 3 mm-class pip beside each. Show it.
5. **Finger dials:** confirmed cut. The rose carries the telephone.
6. **Tongue keys:** keep the walnut-face-on-Delrin-core version as MOTTO's
   key, and put it on the key menu.

**R5. DISH: rebuild around eng's split. The dish is everything MIDI can
touch.**
- **The new rule:** the dish carries only **MCU-read / CV controls**:
  - TUNE, FREQ 2, FREQ 3, RANGE ×3 (MCU-read), GLIDE, and **CUTOFF at the
    centre**.
  - The 6 contour controls too, if they fit as knobs on a larger dish
    (≈ 130–140 mm Ø is now affordable under R1). Otherwise the contour faders
    stay on a wing, and the wing gets its own pip.
  - Only digital lines cross the pivot (a panel mux plus UART, which systems
    already designed). The S10 dependency is gone.
- **The wings carry the analog tone controls,** which eng keeps in the audio
  path: mixer ×5 plus switches, waveforms ×3, emphasis, mod mix, contour
  amount, feedback, noise colour, volume.
  - Emphasis and contour amount go on the **left wing, nearest the hand**.
- **What the cut says:** *the dish is the playable, MIDI-reachable
  instrument, and the wings are the analog tone you set.* That turns an
  electrical constraint into the concept's meaning, and makes the bullseye
  light (V-d) **exactly right**: it glows when any dish control is owned by
  MIDI.
- **Speaker:** move it out of the bullseye into the **base recess the dish
  rises from** (≥ 40 mm, firing up through a grille revealed when the dish
  lifts). "The dish rises out of the speaker well." The bullseye keeps the
  light ring.
- **Keys:** keep the round two-row keys as DISH's own key, but systems must
  confirm the sensor strip can sit in two rows (eng's strip is one straight
  line).
- **Mechanism count:** the fork plus the axle is two pivots, which is fine
  for sauce. State the cost.

**R6. Keys: decouple them from the concepts. One key menu, with samples.**
- The owner said "experiment with key ideas". Make **one key sheet** with
  the four actions: Delrin short lever, TPU pillow, Delrin-core tongue with a
  walnut face, round two-row.
  - For each: a cross-section, travel, feel claim, cost, and the build
    steps.
  - Add a fifth if a real draw produces one worth showing.
- **Each concept shows its best-fit key, but any key fits any straight-row
  concept,** because the sensor strip is separate (owner: "shouldn't effect
  pcb size").
- Recommend the **one-octave printed or cut samples**, so feel is judged by
  hand. That goes to the orchestrator as an owner action, with a cost note.

**R7. MIDI scope everywhere: use eng v2 §2, not "cutoff + glide".**
- **11 MIDI-ownable continuous controls:** GLIDE, TUNE, FREQ 2, FREQ 3,
  CUTOFF, filter A/D/S, loudness A/D/S.
- **Switch-type** (RANGE, OSC 3 CTRL, DECAY, KBD CTRL) stays physical truth
  for the "not in control" light, per common §4. Those switch positions are
  visible, so the light doesn't cover them.
- **Knob-only:** emphasis, mixer, waveforms, mod mix, contour amount.
- Redo the four light variants against this scope:

  | Variant | Concept |
  |---|---|
  | one pip | SLAB |
  | none | DOCK |
  | 11 pips | MOTTO |
  | dish bullseye | DISH |

- **Visual idea to try:** mark the MIDI-ownable controls with a small gold
  ring on the panel. He'll learn which knobs MIDI can take at a glance.
- **Conflict for systems and eng:** common §2 makes the **mod wheel** digital
  (key-board MCU → CC1), but eng v2 §2 lists the mod wheel as a knob-only
  analog pot. Resolve this. It decides whether the wheels can live on the key
  strip, or need an analog path to the voice board.

**R8. Show cost and build steps on every mock.** Give a one-line delta
versus SLAB (hinge, pogo, fork, walnut, lid) and a step count. The owner's
budget reset makes this a design input, not a footnote.

**R9. The look sheet:** keep it, but render it on the **winner-likely
designed-for-use concept** (SLAB or DOCK), at the R1 size, so the owner
judges the looks on the panel he'd actually get.

### Whether the work changed since my last score
This is the first scored round, so there's nothing to compare. Later rounds
must show R1–R9. I won't raise any score for a mock that only changes
styling.

---

## Concept building, round 2: scored in one pass

**Verdict: nothing is at 9 yet. SLAB and MOTTO are one short fix pass away. DOCK is
retired.** The owner is impatient, so the next round is a **fix pass, not a
redesign**: the numbered fixes below are dimensional, mechanical and annotation
changes. They're not new ideas. After it I expect to call READY.

Based on: `slab/slab-mock.png` + `slab-exploded.png`, `dock/dock-mock.png`,
`motto/motto-mock.png`, `dish/dish-mock.png`, `keys/key-menu.png`,
`controls/controls-menu.png`, the concept `how-it-works.md` files,
owner.md (all entries through the bend/mod decision), eng/budget-variant.md
§v1.4b–v1.5, and eng/architecture-v2.md §2 and §4.

| Concept | Kind | R1 → R2 | One line |
|---|---|---|---|
| **SLAB** | designed for use | new → **8** | The right expected answer. One rigid body, the panel finally has room (12 mm knobs at 17+ mm pitch, 11 mm faders, 2.7 mm legends, Ø40 speaker), the lid becomes the stand, and it's the cost baseline. It's held back by two hardware mismatches: the stick doesn't fit its zone, and the switch isn't the quietest one. |
| **DOCK** | designed for use | 7 → **6, retired** | Honest numbers killed it. It's 300 × 237 played (over the 190 box) and **≈ 70 mm carried** (the thickest), it costs +$15–25 over SLAB, and a knocked dock means a reboot and re-tune. Everything it does, SLAB now does smaller, cheaper and with fewer failure points. The 80 mm keys are the only thing lost. |
| **MOTTO** | sauce | 7 → **8** | Real change, and it's the best sauce move yet: **the panel *is* the bentside** (115 at the spine to 85 at the right), so the curve costs no depth. Cork plus a white panel ends the Moog read. The raw-birch lid with the ribbon alone is a placeholder nobody will mistake for a proposal. 11 pips are correct. It's held back by the speaker sitting over the VCO board, 5 mm over the depth box, and the shared stick and switch issues. |
| **DISH** | sauce | 6 → **7** | The rebuild works electrically, and it gives the concept meaning: "the dish is everything MIDI can reach, and the wings are the tone you set". The maple button plugs are the owner's own Critter & Guitari reference. It's held back by ergonomics: **cutoff is 150 mm away and emphasis sits on a different wing**, so the Model D's core two-knob gesture is split across a well. Dish rigidity under knob pressure is also unproven. |

### Did the work really change?
- **Yes for SLAB, MOTTO and DISH.**
  - SLAB is new.
  - MOTTO's silhouette, materials, MIDI light and speaker all changed.
  - DISH was rebuilt around eng's split.
- **DOCK changed in the wrong direction.** Its honest numbers grew past the box, so its score drops.

### Likely owner objections
1. **"What's it going to cost?"** He says this is his main concern. The deltas
   over SLAB are on the sheets (DOCK +$15–25, MOTTO +$35–60, DISH +$30–50),
   but nothing shows a full-instrument price beside each mock. **Certain.**
2. **"I said as silent as possible."** All three draw **Gateron Hall
   switches**. Eng (budget-variant §v1.4b) recommends **Choc V2 silent +
   magnet in the key top + standing TO-92 SS49E** as the quietest, with
   velocity, all through-hole, and its own sensor geometry. Gateron is eng's
   *fallback*: louder, with the sensor position unverified for TH. **Likely if
   he reads the parts.**
3. **"Does the stick even fit?"** The lead bend stick (Adafruit #2765 class)
   is 17.5 × 17.4 mm, but every concept draws it in a **13 mm zone**. The mock
   promises something the part can't do. **Likely, once it's built.**
4. **"Only one expected option?"** With DOCK gone, the designed-for-use kind
   is SLAB alone. He asked for "some". I'm accepting that: SLAB plus the look sheet
   in three looks gives him breadth on the expected side, and a weak second
   option would cost his attention. **Possible.** I'll name it plainly when
   presenting.
5. **DISH: "Cutoff and resonance should be together."** **Likely** from any
   Model D player.
6. **MOTTO: chartreuse.** It's divisive, but it's one bought cap to swap. **Possible**, and acceptable for the sauce kind.

### Rulings asked for

- **DOCK over the box (237 deep, ~70 carried): retire it.**
  - It fails "portable… small" and the cost priority at the same time.
  - SLAB covers its job.
  - Its one idea worth keeping, the longest keys, goes into the key menu as a
    note: K-B can take 80 mm tops on any concept that has the depth.
- **DISH pivot move (fork at the well's rear, 70°, dish at 50°): accepted.**
  - It clears the sharps, and the speaker-well reveal is better than the
    round-1 bullseye speaker.
  - The cost is reach. That's handled by fix D1, not by moving the pivot back.
  - Keep the 75° standing detent.
- **SLAB stand angle: 8°.**
  - 12° adds 15 mm of carry for a small ergonomic gain, and carry
    thickness is the more visible cost (46 mm is already over the box's 36
    because of the lid).
  - 8° raises the rear by about 25 mm, which is enough to see the rear row and
    the faders.
  - No second angle. One position, no wrong way.
- **Gateron vs Choc V2 + key-top magnet: it matters, so switch.**
  - **The default for every switch-based key becomes eng's route (b):** Choc V2
    silent, plus a 5 × 2 mm magnet in the key top, over a standing TO-92 SS49E.
  - **Gateron stays as the fallback,** pending eng's $8 bench test of both.
  - **Effect on the concepts:** the top views don't change. The key sections,
    silence ratings, bought-parts lists and costs do (route b is about $5 more).
  - **K-B lever keys benefit most:** the long top carries the magnet along
    its length, and the steel rod pivot answers eng's worry that long tops
    rock on a single stem.

### Key menu: ruling
1. **K-C stops being a key option and becomes the mechanism.** Its "OUT: no
   velocity" badge is wrong now: with a key-top magnet plus Hall it has
   velocity and is the quietest. Restate K-A, K-B and K-E as "on a Choc V2
   silent + magnet + TO-92".
   - Silence goes to **4/5** for K-A.
   - Fix the section drawings: the sensor stands *beside* the switch,
     under the magnet, not under the switch.
2. **K-B tops are owner-cut at Vector Space, material cost only.** The owner
   answered this. Remove the "owner OK?" open question and the
   "service-cut" badge.
3. **Keep K-A, K-B, K-D and K-E.** K-F stays as a one-line honesty note.
   - K-D is the owner's own idea. Keep its velocity flagged "needs a magnet
     plus Hall per pad, UNVERIFIED".
4. **Best fit per concept:**
   - SLAB → K-B (piano-shaped levers);
   - MOTTO → K-B in walnut, reverse colours;
   - DISH → K-E (maple plugs).
   - State on the sheet that any straight-row key fits SLAB and MOTTO.
5. Add the per-key cost under route (b) to every card.

### Controls menu: ruling
1. **The lead is right, and it matches the owner's decision:** a one-way
   spring-return bend stick plus a mod control that stays put.
2. **Name the part and fit it:** Adafruit #2765 (17.5 × 17.4 mm, through-hole,
   $2.50) slot-gated to one axis, per eng §v1.5b.
   - **The left zone becomes 22 mm.** The body grows to **≈ 292 mm** wide.
   - OP-1 is a loose reference ("feel good to use" outranks it), and 7 mm
     is invisible in the hand. Don't shrink the keys to make room.
3. **Mod = a slide pot that stays put** (owner: "even a fader could be sweet").
   It's an analog pot in the mod path, so it's knob-only and **sends no MIDI**,
   per the owner's rule.
   - This simplifies eng: no AS3360 mod VCA needed in the full version,
     unless eng wants CC1 for another reason.
   - Delete any sheet text claiming the mod control sends CC1.
4. **Knobs:** the default is the skirted knurled cap plus the large hero.
   The leather band is an option to show on one look only. **Abacus faders:**
   off the mocks this round, because the mechanism is too much for the
   payoff. Keep them on the menu.
5. **RANGE:** a Lorlin rotary, MCU-read. It's a switch, so MIDI never sets it
   (owner rule). It should carry no gold ring.

### Numbered fixes for the fix pass

**Shared (all three concepts)**
- **F1.** Put a **full one-unit price range** on each mock, next to the
  existing delta. That means the full instrument, not only the difference
  from SLAB. He'll judge on this.
- **F2.** Switch the keys to **Choc V2 silent + key-top magnet + TO-92**
  (eng route b) in the parts lists, sections, silence notes and costs.
  Gateron becomes "fallback, pending bench test".
- **F3.** Use a **22 mm left zone** with the real 17.5 mm stick, slot-gated,
  and the mod fader behind it. Width ≈ 292 mm.
- **F4.** **Mod sends no MIDI.** Gold rings only on the 11 MIDI-ownable
  controls (glide, tune, freq 2, freq 3, cutoff, 6 contour). No ring on
  RANGE, mod or bend.
- **F5.** Label key tops "owner-cut at Vector Space".

**SLAB**
- **S1.** Use the 8° stand only. Delete the 12° option text.
- **S2.** Show the lid in the look's material, with felt inside so it
  doesn't scuff the caps.
- That's it. After F1–F5 and S1–S2, SLAB is a 9 unless something new
  breaks.

**MOTTO**
- **M1.** **Speaker vs. VCOs:** don't hand this to eng as "E8" and leave it.
  Pick one of two options and draw it:
  - (a) the rose stays top-left, and the mock notes that eng mirrors the VCO
    cores to the right board;
  - (b) the rose moves into the bentside's tail at the right, where the curve is
    lowest. Is the tail deep enough at 85 mm?
  - Prefer (a): the rose top-left is where a harpsichord's is.
- **M2.** Depth from 195 to **≤ 190**. Take it out of the spine. The bentside
  ratio survives.
- **M3.** Keep chartreuse as shown, with a one-line "swap: one cap" note. It
  isn't a sauce concept if every colour is safe.
- **M4.** Keep the cardboard-lid reflector test exactly as written. It's the
  right size of verification.

**DISH**
- **D1.** **Reunite cutoff and emphasis.**
  - Move EMPHASIS to the **inner edge of the left wing**, as close to the dish
    rim as the fork allows.
  - Give it the second-largest cap on the instrument.
  - Draw the left hand spanning both. If the span is over about 120 mm,
    say so honestly.
- **D2.** **Dish rigidity spec, drawn:**
  - Detent holding torque at 50°, against a 15 N push on the outermost knob
    (systems' target).
  - The fork's lateral play.
  - "A wobbly dish" is the objection that would sink this.
- **D3.** **Cable life:** 4 cores through 2 pivots. Name the method (a
  coiled or clock-spring flex, or a slip ring) and its rated cycles.
- **D4.** **Lights off:** the contour knobs on the dish lose the envelope
  picture the faders gave. Add a gold arc between the A/D/S knob pointers,
  or accept the loss knowingly in one line.
- **D5.** Base depth 188 is fine. Carry is 38 vs. the box's 36. Accept that and
  note it.

### What keeps blocking a 9 (rounds 1–2)
1. **Parts assumptions drift from eng.**
   - Round 1: the MIDI scope.
   - Round 2: Gateron instead of eng's quieter route (b), and a 13 mm zone
     for a 17.5 mm stick.
   - The pattern: the mocks are generated from the design kit's
     parametric values, but those values aren't re-synced when eng publishes
     a new part decision.
   - **Process fix:** every mock's "Checked against" box must cite the eng
     file *section and revision* for keys, the stick and the speaker. The
     designers should re-run the kit after any eng update.
2. **Mechanisms swell size.**
   - DOCK grew from 155 to 237 deep and from 52 to 70 carried once the numbers
     were honest.
   - DISH and MOTTO stay just at the edge of the box.
   - **Rule from now on:** draw honest thickness from eng §4.2 first, then
     the mechanism.
3. **Fixed: legibility and cramped panels.** R1 worked. 2.5 mm+ legends and
   17 mm pitches now hold everywhere.

### Set going forward
**SLAB** (designed for use), **MOTTO** (sauce lead), **DISH** (sauce),
plus the key menu, the controls menu and the look sheet on SLAB. Three
concepts I'd defend beat four with a filler.
