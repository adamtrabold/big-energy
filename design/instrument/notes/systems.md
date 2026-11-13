# Systems designer notes: instrument form factor

## Where things stand (round-2 FIX PASS done, systems part)

**Director's round-2 scores:** SLAB 8, MOTTO 8, DISH 7, **DOCK retired**.
This is a fix pass only, with no new ideas. I applied F1–F5, S1–S2, M1–M4
and D1–D5 to how each concept works.

**Files updated:**
- `concepts/common-how-it-works.md`;
- `slab/`, `motto/`, `dish/how-it-works.md`;
- `keys/how-it-works.md` (rebased on the visual's K-A to K-F with route (b));
- `controls/how-it-works.md`;
- `dock/how-it-works.md` (marked RETIRED).

**Key decisions this pass:**
- **Mod is MIDI-ownable (coordinator's correction to director F4).** The
  owner confirmed J12/J13, and E1's AS3360 delivers it.
  - The mod fader is Pico-read, CC1 in and out, with jump-on-move.
  - **That makes 12 ownable controls:** gold rings on 12, MOTTO has 12 pips,
    DISH gives the mod fader its own pip beside the bullseye.
  - **Tell the director:** F4's "no ring on mod" is overridden.
- **Keys:** Choc V2 silent + key-top magnet + standing TO-92 is the default
  (route (b)), with the sensor *beside* the switch. Gateron is the fallback,
  pending the bench test.
  - **K-B lever tops hinge on a 2 mm steel rod**, so the front travels
    ≈ 5 mm.
- **Left zone:** 22 mm, with the #2765 stick slot-gated front–back plus the
  mod slide pot. Width 292. Felt-lined slot ends.
- **E2 forced a sleep-sensor move everywhere** (≥ 50 mm from the speaker
  magnet):
  - SLAB: lid switch to the rear-left;
  - MOTTO: to the right end's rear rim;
  - DISH: to the well's left edge.
- **MOTTO:**
  - M1 option (a): the rose stays top-left, **the VCO cores go on the right B
    board**, with E8's conditions.
  - M2: spine panel 115 → 110, so it's 190 deep.
- **DISH:**
  - The fork pivot is at the well's rear, 70° stop (director accepted the
    visual's move).
  - D1: EMPHASIS at the left wing's inner edge with the second-largest cap.
    The span is **≈ 100 mm, estimated; the visual must measure it.**
  - D2: ≥ 1.0 N·m at the dish axle against 15 N at r 41; hard stops at 70°
    (fork) and 75° (dish); ≤ 0.5 mm lateral play at 5 N via a cross-tie.
  - D3: a silicone service loop at the fork pivot, a **slip ring at the dish
    axle** (twist cable rejected: ≈ 2,300°/m). Life target ≈ 37,000 cycles;
    part ratings UNVERIFIED.
  - Cost goes from +$25–40 to **+$40–60**.
- **F1 one-unit prices:**
  - SLAB ≈ $530–860;
  - MOTTO ≈ $565–920;
  - DISH ≈ $570–920.
  - (Eng base ≈ $530–860 after E1/E3/E5.)
  - **Agree DISH's figure with visual** (their round-2 sheet said +$30–50).

**The coverage check (J1–J19) is still due** on each 9+ concept, once the
director scores the fix pass.

---

## History: round-2 first pass (below, kept)

## Where things stood (end of concept round 2, systems turn)

I took over from the round-1 systems designer and applied R1–R9 to how each
concept works.

**Written this turn:**

| File | What |
|---|---|
| `concepts/common-how-it-works.md` | **Rewritten** on eng v2. Boards A–D; the joint rule; the height stack; the mod wheel resolved; R1 panel area; the MIDI scope table; light variants; speaker placement; one USB-C; asks E1–E10 |
| `concepts/slab/how-it-works.md` | **New.** Replaces CASE |
| `concepts/dock/how-it-works.md` | Rewritten. Carries the R1 × R3 conflict finding |
| `concepts/motto/how-it-works.md` | Rewritten. Bentside panel, rose in the panel |
| `concepts/dish/how-it-works.md` | Rebuilt per R5. Ø 112, a 38 mm base |
| `concepts/keys/how-it-works.md` | **New.** Key menu K1–K6 plus modifier M1, serving the full version and Little D |
| `concepts/controls/how-it-works.md` | **New** (coordinator / owner "250 feels high… creative knob / wheel styles"). C1–C9. **Finding:** controls are ≈ $21 of Little D, so clever choices save ≈ $6–10, not the gap to $150. Recommend C1 printed caps, C3 edge wheels (+8 mm width, not +40), C8 zipper-detent RANGE. Draws: abacus beads → C6, zipper → C8, "Is there something missing?" → C3 |
| `jobs.md` | Targeted round-2 edits: J6 one variant, J12 risk, J13 scope, the I/O count, F11, states |
| `concepts/case/how-it-works.md` | Marked CUT |

**Not done yet:**
- **The coverage check (J1–J19 per concept) is still not done.** It's due
  for every concept scoring 9 or more, before the owner sees anything.
- **The mocks are stale.** Visual has to redraw at R1 sizes using the
  numbers below.

## Concept numbers (round 2)

| Concept | Played (mm) | Carried (mm) | Key | Light | Δ cost vs SLAB | Steps |
|---|---|---|---|---|---|---|
| **SLAB** | 285 × 185 × 34, 8° on the folded-lid stand | 285 × 185 × 46 | K1 | V-a, 1 pip | 0 | 12 |
| **DOCK** | **285 × 236 × 33** (over the box) | **285 × 136 × ≈ 70** | K1-long | V-b, none | +$15–25 | 14 |
| **MOTTO** | 285 × 195 (spine) → 165 (right) × 34 | same × 46 | K3 | V-c, 11 pips | +$35–60 | 15 |
| **DISH** | 285 × 188 × **38** | same, flat, no lid | K4 | V-d, bullseye | +$25–40 | 17 |

## Decisions and why

1. **Mod wheel: analog, per eng v2 §2 ("Knob only").** Round-1 common §2 had
   made it digital; I withdrew that.
   - **Consequences:** the wheels mount to the rigid body with a shielded
     lead to B. J12 (CC1 in) and J13 (wheel out) are gaps.
   - **Proposed E1:** mod depth via one LM13700 half plus the spare 8th
     MCP4728 channel. That fixes both gaps and lets DOCK put the wheels on
     its module.
2. **Speaker placement is a set-wide problem.** No eng board plan leaves room
   for a ≥ 40 mm driver ≥ 60 mm from the keys.
   - SLAB, DOCK and MOTTO: a 48 × 48 notch in A/B (E2).
   - DISH: under the rear of the well.
3. **SLAB's stand:** the lid is two 12 mm leaves on a sewn strip. Z-folded,
   it gives 24 mm under the rear, so **≈ 8°**.
   - A one-piece lid gives only 3–5°.
   - A **unipolar Hall switch** keeps a lid folded underneath from putting
     the unit to sleep.
4. **DOCK can't meet R1 and R3 together.**
   - The module must be as deep as the 100 mm panel it covers.
   - Board D must sit with B (it carries ±10 V and the CVs), so it needs a
     30 mm rear strip (E6).
   - The battery moves to the module, with VBAT on paired pogo pins, gated
     dead until docked. That makes it power-by-dock.
   - **Carried floor is 56 mm, realistically ≈ 70. R3.2's < 45 can't be
     reached.**
   - **Draws:** "Use an old idea" became full-depth keys, DOCK's feel
     advantage. "Harp pedal notches" became notched cleats instead of cones.
5. **MOTTO: I accepted visual's tail hinge and standing lid,** and withdrew
   the mirror.
   - Under R1 a separate tail would make it 225 deep. Instead **the panel is
     the bentside** (115 deep → 85), and the rose speaker sits in the panel
     at the rear-left.
   - A 110 mm piano hinge at the spine plus a stay at the right.
   - The jacks follow the curved rear edge. USB-C is on the spine face.
6. **DISH:**
   - The dish holds exactly the 14 MCU-read controls, including the 6
     contours as knobs. All toggles are on the wings.
   - **A dish MCU plus UART is the only thing crossing the pivots.**
   - **Ø 112, not 130–140**, because the well counts toward depth (135 would
     make it 211 deep).
   - **A 38 mm base**, so the wing caps sit below the rim and it needs no lid.
   - A low-profile B extension under the well floor covers the area the well
     takes. **This is the tightest board plan of the four.**
7. **Keys:**
   - The two-row pegs work on one straight sensor line, using interleaved
     tongues.
   - **Delrin doesn't glue**, so tops are pegged on.
   - **K6 rockers** came from two real draws (light-switch rocker, then
     sewing-machine treadle). One sensor per two notes. It suits a mono
     voice, and it's the cheapest option with travel, which makes it a
     Little D candidate.
   - **M1 magnetic let-off** came from a draw (piano escapement).
   - **phase8:** the manual describes "8 keys" as voice triggers or step
     buttons, with no mechanism or velocity stated, so only the visual idea
     was borrowed.
   - **K5 (OP-1-style)** is offered honestly, and rated lowest on
     "instrument". **K2 (pads in a key layout)** is the quietest.
8. **Switch-type controls stay physical truth;** they're not covered by the
   light (R7).

## Director's round-1 objections and how they were answered

| Ruling | Answer |
|---|---|
| R1 | Done everywhere, with arithmetic. **Exceptions flagged:** DOCK over on depth and carry; DISH +2 mm thick |
| R2 | SLAB |
| R3 | K1-long done, speaker done. **Carry < 45 is infeasible (shown).** Dock feel: cleats, magnets, pogo pins. Panel edge when the module is away: nothing, because the body is unpowered |
| R4 | Walnut only on the lid's outside (visual does the material). Abstract placeholder: visual. Speaker ≥ 40 mm, reflector "unverified". 11 pips. Dials cut. K3 |
| R5 | Rebuilt. Finding: Ø 112, not 130–140 |
| R6 | Key menu written |
| R7 | Scope table plus the variants. Mod wheel resolved via eng's doc, with the E1 proposal |
| R8 | Δ cost and steps in every file |
| R9 | Visual's |

## Open questions

**Director:**
- DOCK over the box: accept or retire? My view: not a 9 without E1.
- DISH at 38 thick and Ø 112.
- SLAB's tilt at 8°, or a thicker lid for 12°.

**Eng: E1–E10** (listed in common §7). The most important:
- E1 (mod VCA);
- E2 (speaker notch);
- E3 (one USB-C);
- E6 (DOCK's D strip, VBAT over pogo);
- E7 (DISH board area and the thin driver).

**Owner:**
- Should knob-only controls send CC? (Dual-gang pots; I recommend not.)
- Does MIDI need to flip switches? (I recommend not.)
- Which light variant? (He picks from the mocks.)
- **The key samples** (≈ $50–80, keys menu), plus one C3 edge wheel and one C8 rack (≈ $2).

**Visual:**
- Redraw all four at these sizes.
- The MOTTO curved jack row.
- The DISH ring legends at a 2.5 mm cap height on Ø 112.
- The SLAB stand shown in a mock (R2).

**Unverified:**
- the speaker chamber volumes, and "incredible";
- the MOTTO reflector;
- pogo current rating;
- the TO-92 unipolar Hall part;
- a thin 40 mm driver;
- the silicone kit's Shore hardness;
- the flexure force numbers.

## What comes next
1. **Visual:** looks plus R1-size mocks for SLAB, DOCK, MOTTO and DISH, the
   key sheet, and the look sheet on SLAB.
2. **Director:** steer and score. Rule on DOCK and the DISH exceptions.
3. **Then me:** the coverage check (J1–J19) on each 9+ concept, and react
   to visual's changes.
4. **Orchestrator:** send E1–E10 to eng, and the key-sample action to the
   owner.

---

## 2026-11-12: keys from first principles (systems designer, new to this folder)

**Task:** owner: "Rethink the keys from first principles with out discoveries in mind."
**Mid-task priority change (coordinator):** the full instrument is paused and
Little D is the focus, with cost first. A new Little D team works in
`design/little-d/` and reads `concepts/keys/first-principles.md`.

**Written:** `concepts/keys/first-principles.md`, which supersedes the R6 key
menu and visual's K-A…K-F as the decision basis. Those stay as history.

**Core reasoning:**
- Hall sensing (SS49E + magnet) already gives velocity and silent sensing,
  so only four things are left to design: the surface, guide, return and
  stops.
- The Choc switch does guide and return badly for long tops (they rock),
  and it *is* the keyboard-switch feel the owner ruled out.
- **Cost doesn't discriminate:** every option costs ≈ $45–70 for 25 keys,
  against a fixed ≈ $32 floor (sensors, magnets, acrylic).

**Four mechanisms, different in kind:**
- A. SWITCH: today's route (b), $50–55 [ENG].
- **B. RAIL:** U-channel acrylic keys (two blades on edge, solvent-welded top)
  on one Ø 3 rod, with silicone-tube pieces as spring and soft bottom stop,
  felt under the case lip as the top stop, damping grease at the pivot and a
  felt-lined guide comb. Lean cost $45–55; RAIL-M adds a magnetic breakaway
  (+$8–13).
- C. COMB: Delrin flexure, one octave per piece. **2 mm Delrin works**
  (calc: a 4 × 20 mm neck gives ≈ 40 gf, ≈ 10 MPa). The CNC router sidesteps
  the laser thickness limit.
- D. FLOAT: square tops on foam in a frame. Cheapest and thinnest; pad feel.

**Geometry:** key run 270 mm (15 × 18). The rear is 12 equal stems per octave,
so 10.5 mm, and **all 25 sensors sit in one even line at 10.5 mm** for RAIL
and COMB.

**Draws (secrets.choice):**
- typewriter → RAIL's structure;
- "only one element of each kind" → one rod, one tube stock, one felt rail.
  It also showed a single SoftPot for all keys fails legato;
- "water" → damping grease;
- harpsichord jack → magnetic return (RAIL-M);
- stapler → metal springs, rejected.

**Recommendation:**
- Little D: **1 lean RAIL, 2 FLOAT, 3 SWITCH, 4 COMB.** RAIL is gated on
  thickness (≈ 18–20 mm stack vs Little D's ≤ 8 mm under-key limit, E-K2);
  if that fails, FLOAT.
- The cheaper floor (overseas sensors and magnets, scrap acrylic) is the
  real cost lever: ≈ −$20–25.
- Full version (paused): 1 RAIL, 2 COMB, 3 SWITCH, 4 FLOAT.

**The honest physical check:** build the real first two keys (C, C♯) and
press them (tube force), plus eng's planned $8 Hall bench test. No samples.

**Open questions:**
- **Eng E-K1–E-K6**, most urgent first:
  - E-K2: thickness;
  - E-K3: SS49E saturation gap;
  - E-K1: scan rate and velocity method;
  - E-K5: real prices for rod, tube, grease and Delrin.
- **Owner O-K1–O-K3:**
  - first-keys check instead of samples;
  - Delrin at Vector Space (only if COMB stays);
  - piano tops or buttons for Little D.
- **Director:** reword J1 to add velocity and drop "lever action". I did not
  edit jobs.md.

**Not done:**
- coverage check against jobs.md (RAIL meets J1, J10 and J16 on paper; the
  real walk is due when a concept is chosen);
- handoff;
- the Little D folder exists (concepts/, notes/, owner.md, jobs-full-instrument-reference.md); I did not read it, so check what the
  new team has written.

**Next:** the Little D team's visual designer draws lean RAIL (square and
piano tops) and FLOAT at Little D's size. Eng answers E-K2 first, since it
decides RAIL vs FLOAT.
