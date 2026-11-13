# Keys from first principles (systems), 2026-11-12

**Owner (verbatim):** "Rethink the keys from first principles with out discoveries in mind"

**Serves both instruments, Little D first.** Coordinator, 2026-11-12: the
full version is paused, and Little D is the focus, where cost matters most.
§0 and §5 lead with Little D. The full-version notes stay for when it
resumes. The Little D team (`design/little-d/`) reads this file.

**Read with:** `discoveries.md` (constraints), `owner.md`, `jobs.md` J1/J10/J16,
`eng/key-sourcing.md`, `eng/budget-variant.md` §v1.4b. The old menu
(`how-it-works.md`) is history.

**Marks:** **[ENG]** = eng's figure or price, cited. **ESTIMATE** = mine, not
priced. **[CALC]** = my arithmetic, shown.

---

## 0. Bottom line

- **Hall sensing already solved the hard part.** A magnet over a linear
  Hall sensor gives velocity, makes no sound and needs no contacts. That
  frees the mechanism completely. **What's left to design is only: the
  surface, what guides it, what returns it, and what stops it quietly.**
- **Today's default spends a computer-keyboard switch on those four jobs.**
  It does two of them well (return, quiet stops) and two badly: it guides a
  long key top poorly (it rocks), and it *is* a keyboard switch, which is the
  feel the owner ruled out.
- **Cost doesn't pick the winner.** Sensors, magnets and tops are a fixed
  floor of ≈ $32 for every Hall option [ENG prices, §4]. The four mechanisms
  below all land at **≈ $45–70 for 25 keys**. So choose on feel, silence and
  build.
- **For Little D, I put forward lean RAIL, at ≈ $45–55:** laser-cut
  acrylic keys on one bought steel rod, each sprung by a short piece of
  bought silicone tube, stopped by felt under the case lip.
  - It's the old idea a typewriter and a piano share, built from three bought
    parts.
  - It gives real travel (≈ 5 mm, about 1.8× the Choc's), no rocking and no
    switch feel.
  - **It costs the same as today's switch keys (≈ $50–55)** and about the
    same as the cheapest option, FLOAT (≈ $45–56).
  - "Lean" means scrap acrylic and plumber's grease, not damping grease (§4).
- **FLOAT is the cost-and-thickness fallback.** Tops float on foam: the
  cheapest, the thinnest and the easiest to build. It's pads, not keys, so
  it loses on "feel like an instrument".
- **The real cost lever for Little D isn't the mechanism. It's the ≈ $32
  floor** of sensors, magnets and tops. Overseas sensors and magnets could
  cut it to ≈ $20 (eng's tariff call).
- **When the full version resumes,** the same RAIL lever takes any touched
  surface: piano tops, walnut, maple pegs or square OP-1-style buttons. So
  Little D's keys double as its proof.
- **"No samples" handled honestly:** the first two keys of the real build
  are the check.

---

## 1. What a key has to do (the jobs under J1)

I wrote these from the owner's words before reading the specs.

| # | Key job | Source |
|---|---|---|
| K1 | A note sounds where the finger expects it: piano order, 25 keys, ≈ 18 mm white pitch | stated (25 keys, 280–292 mm) |
| K2 | **Real travel that feels like an instrument**, not a computer key | stated ("feel like an instrument"; no "clicky computer-keyboard") |
| K3 | **Silent**: no click on the way down, no clack on the way back | stated, hard criterion |
| K4 | **Velocity** | stated ("i want velocity") |
| K5 | Fast repeats and trills keep up | inferred: playing |
| K6 | Legato: two keys overlap cleanly, so glide and single-trigger work (low-note priority) | inferred from J10 |
| K7 | Build it at Vector Space plus bought parts, with no SMD, no printing and no harvested keybed; fix one key without rebuilding all 25 | stated (J6, discoveries) |
| K8 | Survives a bag and a lap; works tilted | inferred from J3, J16 |

**A scope note on jobs.md J1:** it says "a lever action" (that pre-decides a
mechanism) and leaves out **velocity**, which the owner has since made
required. I propose rewording J1 to: *"Play notes on keys that feel like an
instrument: real travel, silent, no click, velocity. They don't have to be a
traditional keybed."* I haven't edited jobs.md; that's for the director to
OK.

### The seven parts of a key, and what our constraints say about each

| Part | What the constraints allow | Consequence |
|---|---|---|
| **Surface** | bought or owner-cut sheet (acrylic, ply, walnut, Delrin*), or bought wood (maple plugs); never printed | Acrylic **solvent-welds** (strong and easy); Delrin glues to nothing |
| **Guide** (one degree of freedom) | a pivot, a flexure, a slider (switch), or nothing (floating) | **Sliding clearance is the main rattle source.** Pivots and flexures guide long keys; sliders only guide short ones |
| **Return** | a spring, an elastomer, the flexure itself, a magnet, gravity | Metal springs can ping. Elastomers and magnets can't |
| **Stops** (top *and* bottom) | felt, silicone, foam | **The return clack is often louder than the down stroke.** Both ends need soft stops |
| **Sensing** | settled: SS49E TO-92 + 5 × 2 mm magnet [ENG] | One straight sensor line on strip C, centres ≥ 6.5 mm apart (E10) |
| **Mount and alignment** | laser-cut frames, screws, the case itself | **The case lip can be the top stop** (as a piano's key slip is) |
| **Build and fix** | owner-cut, hand assembly | A broken key should cost one key, not a comb |

\*Delrin permission and thickness at Vector Space are **unverified** (another
makerspace limits it to ≤ 2 mm on the laser).

### What every option shares: the firmware states

Hall sensing makes these the same for every mechanism. Only the mechanical
column differs, and each concept states that.

| State | What happens (all options) |
|---|---|
| **Rest** | The key's reading sits at its learned rest value. The firmware re-learns rest at every wake (F1) |
| **Travel** | Position is read continuously. **Velocity = time between two depths** (e.g. 20 % and 70 % of travel) |
| **Bottom** | Note on (if not already). Depth past the gate is available as pressure, unused for now |
| **Release** | Note off at a **re-arm depth partway up** (≈ 40 %), with hysteresis, so there's no chatter at the threshold |
| **Fast repeats** | **The key needn't return fully** to re-trigger: past the re-arm depth it fires again. That's a piano's double escapement, done in firmware, and faster than any switch contact |
| **Legato / glide** | Every key reports on/off on its own, so the note list sees overlaps. Lowest-note priority, single trigger and glide work unchanged (J10). The mechanism only has to let two keys go down together, which all four do |
| **Crosstalk** | Neighbouring magnets are fixed relative to their own sensors, so they're calibrated out. Only a *moving* neighbour can disturb a reading, and at ≥ 10.5 mm its share is small (ESTIMATE; confirm in eng's bench test) |

**Velocity resolution grows with travel time.** The time is set by how far
the *fingertip* travels, so 5 mm of travel gives ≈ 1.8× the timing spread
of 2.8 mm at the same scan rate [CALC: 5 / 2.8]. That makes travel a velocity
argument as well as a feel argument.

### Geometry every option uses

- **Key run ≈ 270 mm:** 15 whites × 18.0 mm. That leaves the 22 mm left zone
  for the bend stick in a ≈ 292 mm body (director F3) [CALC].
- **Octave = 126 mm** (7 × 18), about 77 % of a piano's.
- **The rear of a keyboard is 12 equal stems per octave** (the standard
  trick: 7 equal whites at the front, 12 equal stems at the back). Here
  that's **126 / 12 = 10.5 mm** [CALC].
  - **So in RAIL and COMB, everything mechanical lives on one 10.5 mm grid:**
    the rod bearings, the springs, the guide slots, and **the 25 sensors, in
    one perfectly even straight line** on strip C (E10 satisfied).
  - Only the touched tops break the grid.

---

## 2. Draws (real randomness)

`secrets.choice` gave me three fields, **stapler, typewriter typebar and
harpsichord jack**, and two Oblique Strategies, **"Only one element of each
kind"** and **"Water"**.

| Draw | What it gave |
|---|---|
| **Typewriter typebar** | Key levers stand **on edge as thin blades** on one common fulcrum rod, guided at the front by a **slotted comb**, with felt-lined stops. → RAIL's structure |
| **"Only one element of each kind"** | One rod for all 25 pivots, one tube stock for all 25 springs, one felt rail for all 25 top stops: **three bought parts do the 25 switches' job**. Pushed further, *one sensor for all keys* (a single SoftPot under the row) **fails**: two held keys read as one midpoint, which breaks low-note priority and legato (K6). Rejected; it told me where "one" stops |
| **Water** | Viscous damping. **Silicone damping grease on the pivot rod** fills the bearing clearance, so it can't rattle, and it adds the velvet resistance a camera focus ring has. → RAIL's pivot |
| **Harpsichord jack** | Return by gravity, with no spring. Gravity fails on a lap or tilted (K8), so I swapped weight for a **magnet pulling toward a steel strip**: return with no spring that works in any orientation. → RAIL-M, an option |
| **Stapler** | A leaf spring per lever. Considered as bought music wire per key; rejected because metal springs can ping and need a hook per key. The silicone tube does the job silently |

---

## 3. Four mechanisms that differ in kind

| | Guide | Return | Kind |
|---|---|---|---|
| **A. SWITCH** | a bought slider | the switch's spring | a keyboard switch carries the top (today's default; kept for comparison) |
| **B. RAIL** | a pivot on one rod | silicone tube pieces | a keybed: typewriter / piano lever |
| **C. COMB** | a flexure (the material bends) | the flexure itself | one cut sheet is all 25 bearings and springs |
| **D. FLOAT** | none: the elastomer is the guide | a foam pad | drum pads / OP-1 buttons: the top floats on a cushion |

---

### A. SWITCH: Choc V2 silent + key-top magnet + standing TO-92 (eng route b, today's default)

**How it works:**
- A Kailh Choc V2 silent switch is soldered to the key strip under each key.
- An owner-cut acrylic top presses onto its stem. A 5 × 2 mm magnet sits in a
  pocket beside the stem, over a standing SS49E [ENG §v1.4b].
- The switch contacts are unused.

| State | Mechanical behaviour |
|---|---|
| Rest | held up by the switch spring |
| Travel | 2.8 mm total [ENG]. Linear |
| Bottom | the switch's built-in dampener |
| Release | the dampened upstroke |
| Fast repeats | good: a light spring and a short throw |
| **The weak point** | **A long white top on one 1u stem rocks** when it's pressed at the front (eng's own worry, §v1.4b). Square tops are fine |

- **Parts you buy:** 25 Choc V2 silent switches, 25 magnets, sensors, acrylic.
- **The owner cuts:** the key tops, with a cross hole for the stem or glued to
  a blank cap.
- **Cost (25):** **≈ $50–55** [ENG §v1.4b].
- **Silence:** 4/5, dampened both ways [ENG].
- **Feel:** 2/5. It's short, linear and **literally a computer-keyboard
  switch**, made quiet. That's the closest thing on this list to what the
  owner ruled out.
- **Velocity:** Hall, but the 2.8 mm throw gives the narrowest timing spread
  of the four.
- **IKEA:** 4 steps: solder the switches and sensors, glue in the magnets,
  press on the tops. Easy.
- **Width:** 18 mm Choc spacing → 270 mm ✓. The switches widen strip C to
  hold two rows of footprints.
- **Risks and checks:**
  - Rocking: a press-fit cross in laser-cut acrylic can crack.
  - Check: eng's planned **$8 bench test** of 2 Choc + SS49E [ENG]. It's
    unavoidable and cheap.

---

### B. RAIL: acrylic levers on one rod, silicone-tube springs, felt under the case lip ★ recommended

**Section (front to back):**

```
  finger
    v          (visible white ≈ 52)           | under the panel lip (≈ 20) |
  [==== top 3 mm acrylic, solvent-welded on the blades =========]          |
   \_ blade 3 mm on edge, ×2 per key (inverted U) ________________________o  <- rod Ø3, on the 10.5 grid
        |guide tab|        (tube)     (magnet)            felt ^ (top stop, under the lip)
   [felt][comb slot]  [ silicone tube piece ]  [ SS49E on strip C ]
  y from rod:  ~48           ~45             ~30                  ~12     0
```

**How it works:**
- **Each key is an inverted U.** Two 3 mm acrylic blades stand on edge (cut
  as side profiles), and the touched top is **solvent-welded** across them.
  Sharps get a welded riser layer, so they stand ≈ 5 mm proud.
  - The blades' rear ends carry a Ø 3.1 mm hole. **All 50 blades thread onto
    one bought Ø 3 mm steel rod** under the panel lip.
  - Keys are spaced on the rod by laser-cut felt washers (felt is on Vector
    Space's laser list).
- **Guide:** a tab on each key's front blade runs in a **felt-lined slot of a
  laser-cut guide comb** (the typewriter draw), on the 10.5 mm grid.
  - The two blades, 8.5 mm apart, plus the front slot kill sideways wobble.
- **Return:** a **short piece of bought silicone tube** (≈ 6.4 mm OD ×
  3.2 mm ID, cut ≈ 8 mm long with scissors) sits in a laser-cut pocket rail
  under each key, ≈ 45 mm from the rod. **There's one piece per key, not one
  continuous tube,** so pressing one key can't tug its neighbours.
- **Top stop:** the tube is pre-compressed ≈ 0.5 mm. It holds the key's rear
  up against a **felt strip glued under the panel lip.** **The case is the
  stop.** The keys can't rattle at rest because they're preloaded.
- **Bottom stop:** **the tube going solid is the bottom stop.** Its two walls
  ≈ 3.2 mm give a progressive, soft, silent end, with a felt strip under the
  key fronts as the overtravel backup.
- **Pivot:** silicone damping grease on the rod (the water draw). No rattle,
  and a smooth, slightly viscous feel.
- **Sensing:** the magnet sits in a pocket in the blade ≈ 30 mm from the rod,
  over the even 10.5 mm sensor line.

**Travel [CALC]:** the tube's solid travel is 3.2 mm at 45 mm from the rod.
- Whites, with their front at 72 mm: **≈ 5.1 mm at the front**.
- Sharps, with their front at 52 mm: **≈ 3.7 mm**.
- At the sensor (30 mm) the magnet moves ≈ 2.1 mm. Moving the sensor line
  forward gives more swing if eng wants it.

| State | Mechanical behaviour |
|---|---|
| Rest | preloaded up into the lip felt: a defined height, no rattle |
| Travel | a rising, progressive force (the tube stiffens as it flattens) |
| Bottom | the tube goes solid: a soft "cushion" end, silent |
| Release | the tube pushes back quickly; the rear meets felt |
| Fast repeats | the tube is fast-recovering, and the firmware re-arms at 40 % |
| Legato | independent levers, so overlapping is free |

**The touched surface is a skin.** Because a lever moves the same however you
press it, the top can be anything cut or bought:

| Concept | Top on the same lever |
|---|---|
| SLAB | piano-shaped acrylic tops |
| MOTTO | walnut-ply whites, bone sharps. Wood welds badly, so glue it with epoxy to an acrylic layer |
| DISH | a bought maple plug glued on each lever, rising through a felt-collared hole in the skin (the C&G look without the peg-in-hole rattle) |
| a button look | square OP-1/phase8-style tops on levers: the look of buttons with the travel of keys |

**RAIL-M (option): a magnetic "touch".**
- A second magnet in each key's rear, under the lip, faces a **bought mild
  steel flat bar** set in the lip. The felt sets the gap.
- **Pull is strongest at rest and falls away as you press:** a breakaway,
  like the inertia of a real piano key. The tube is strongest at the bottom,
  where the magnet is weakest, so the two curves complement each other.
- It works upside down. It can't fatigue or ping.
- **+≈ $8–13** (25 magnets [ENG rate] + a steel bar ESTIMATE $3–5).
- **Risks:** the pull at a 0.5 mm gap is ESTIMATE (≈ 50 g at the front
  [CALC from typical 5 × 2 mm pull figures, unverified]). Moving rear magnets
  add a little crosstalk. Offer it only if the first-key check feels too
  soft or too even.

- **Parts you buy:**
  - one Ø 3 mm steel rod ≈ 300 mm (ESTIMATE $3–5, hobby music wire / drill
    rod);
  - ≈ 1 m of silicone tube (ESTIMATE $6–12);
  - silicone damping grease (ESTIMATE $8–15; plumber's silicone grease ≈ $5
    works as a lighter option);
  - felt (in eng's existing stops line);
  - 25 magnets, sensors, acrylic [ENG].
- **The owner cuts (laser):** 50 blades, 25 tops, 10 sharp risers, the guide
  comb, the tube pocket rail, two rod end blocks, felt washers and a
  **welding jig plate** that holds blade, top and riser square while the
  solvent sets.
- **Cost (25) [ENG base + ESTIMATE]:** base $32.40 + rod $3–5 + tube $6–12 +
  extra acrylic $4–8 + grease $5–12 = **≈ $50–70**. That's parity with SWITCH
  up to +$15. Strip C stays the narrow single-line strip eng specified
  (280 × 15), which is slightly cheaper than SWITCH's two-row strip.
- **Silence:** **5/5 (ESTIMATE).** Silicone at the bottom, felt at the top,
  grease at the pivot, no metal-on-metal, no spring to ping.
- **Feel:** **4/5** (5/5 with RAIL-M, judged by hand). Real travel, a lever,
  progressive.
- **Velocity:** Hall, with the longest timing spread among the realistic
  options.
- **IKEA:** 6 steps: cut, weld the 25 keys in the jig (≈ 1–1.5 h), press in
  the magnets, thread the keys and washers onto the rod, drop the rod into
  the end blocks and the tubes into their pockets, screw on the lip.
- **Fix one key:** slide the rod out and replace one key. Nothing else moves.
- **Width:** 270 mm ✓.
- **Height:** ≈ 18–20 mm from strip C to the key top [CALC: 1.6 strip + ≈ 6
  sensor + ≈ 2.5 travel + 7 blade + 3 top]. That's taller than SWITCH
  (≈ 11–13 mm, ESTIMATE). **Eng question E-K2.**
- **Depth:** 52 mm visible + 20 mm under the lip = **72–75 mm**, matching
  SLAB's 75 mm key zone ✓.
- **Risks and how to check them cheaply:**

| Risk | Check |
|---|---|
| Rod-hole fit: a laser-cut hole too loose rattles, too tight binds | A **hole coupon on scrap** (five holes at different offsets, ≈ 2 min, $0). It's a routine laser setting, not a sample |
| **Tube force: the one real unknown.** Is it ≈ 50 g at the front? | **First-key check (unavoidable, honest):** cut and build the real C and C♯ of the final build, on the real rod and tube, and press them. Tune the force by moving the pocket rail (a 3-minute recut) or changing the piece length. Nothing is wasted: those keys go into the instrument |
| Welds failing under a hard knock | Two blades per key give 2 × 150 mm² of weld. Check by pressing the first key hard |
| Tube taking a set over years | Silicone has low compression set. The pieces are replaceable for cents |

---

### C. COMB: one sheet bends (Delrin flexure, CNC-routed or lasered)

**How it works:**
- Each key is a tongue of a **Delrin comb**, cut **one octave per piece** (3
  pieces), so a broken tongue costs a third of a comb, not the whole.
- The root of each tongue is a narrow neck: the bearing and the spring in
  one. It's clamped under the lip by a screwed bar.
- Tongues sit on the 10.5 mm grid. The acrylic top is fixed with **two M2
  screws from below into a welded acrylic boss**: Delrin doesn't glue, but it
  takes screws well.
- Felt top stop under the lip, felt bottom stop under the front.
- **No preload:** the keys rest at the flexure's neutral, because Delrin
  creeps under steady load.
- **Discovery: 2 mm Delrin works,** so the "≤ 2 mm" limit elsewhere doesn't
  kill this [CALC]:
  - a 4 × 20 mm neck in 2 mm sheet (E ≈ 3 GPa) needs **≈ 0.4 N (≈ 40 gf)
    for 5 mm at the front**, with a peak stress of ≈ 10 MPa;
  - 3 mm with a 15 mm neck is ≈ 1.7 N, too stiff unless the neck narrows to
    2 mm.
  - The **CNC router** cuts Delrin at any thickness without fumes, which
    sidesteps the laser limit. Both are subject to Vector Space's rules.

| State | Mechanical behaviour |
|---|---|
| Rest | at the flexure's neutral, lightly touching the lip felt |
| Travel | linear, a woody spring |
| Bottom | felt |
| Release | quick. **Risk: the ruler twang:** a tongue can vibrate after release. Damped by meeting the lip felt |
| Fast repeats | excellent: the flexure has a high natural frequency |
| Legato | independent tongues |

- **Parts you buy:** Delrin sheet (ESTIMATE $15–35), 50 M2 screws (ESTIMATE
  $3–5), felt, magnets, sensors, acrylic.
- **The owner cuts:** 3 combs, tops with bosses, the clamp bar.
- **Cost (25):** **≈ $50–72** (ESTIMATE).
- **Silence:** 5/5 (no pivot, no sliding part).
- **Feel:** 4/5: a springy lever, less progressive than RAIL.
- **Velocity:** Hall, 5 mm of travel.
- **IKEA:** 5 steps. The fewest parts of any option.
- **Width and depth:** 270 mm, 75 mm ✓. Height ≈ 15–17 mm (ESTIMATE).
- **Risks and checks:**
  - **Permission (blocking):** ask Vector Space about Delrin on the laser and
    the router. That's free and needs no making.
  - Neck fatigue: radius every inside corner in the cut file. Stress is a
    third or less of Delrin's fatigue range (ESTIMATE).
  - Screws loosening: use thread-locking or nylon-patch screws.
  - Feel check: the first octave comb *is* the build's first part.

---

### D. FLOAT: tops floating on foam in a frame (drum pads, OP-1 buttons)

**How it works:**
- The top skin has 25 windows: square whites (≈ 17 × 17) in front, sharps
  (≈ 13 × 15) in a row behind. That's the button look of the phase8, the
  OP-1 and pads.
- Each pad is a top plate plus a **welded flange layer** larger than its
  window, so it can't come out.
- It rests on a square of bought **adhesive-backed silicone sponge or
  urethane foam** (≈ 3 mm, ≈ 2 mm usable compression, ESTIMATE). The foam
  preloads the flange up against a felt-lined underside of the skin.
- **The elastomer is the guide, the return, the stop and the damper.**
  There's no bearing at all.
- A magnet sits at each pad's centre. **Strip C needs two sensor rows**
  (allowed by E10 when a layout's positions collide).

| State | Mechanical behaviour |
|---|---|
| Rest | preloaded against felt: no rattle |
| Travel | ≈ 1.5–2 mm, a cushion |
| Bottom | the foam firms up |
| Release | foam recovery: **it must be fast-recovery foam, not memory foam** |
| Fast repeats | fine with fast foam, plus the 40 % re-arm |
| **Weak point** | **An off-centre strike tilts the pad,** so velocity varies with where you hit (drum pads share this). Long piano shapes would tilt badly, which is why it's square pads only |

- **Parts you buy:** foam (ESTIMATE $5–10), magnets, sensors, acrylic.
- **The owner cuts:** the frame skin, pads, flanges and the felt gasket.
- **Cost (25):** base $32.40 + foam $5–10 + acrylic $4 + the two-row strip
  ≈ +$4–9 (at eng's $0.61–1.22/in²) = **≈ $45–56**.
- **Silence:** **5/5,** the quietest.
- **Feel:** **2/5 as a key, 4/5 as a pad.** It's Maschine-pad-like, which he
  knows well.
- **Velocity:** Hall over ≈ 2 mm: the shortest timing spread, and
  position-dependent.
- **IKEA:** 5 steps. The easiest of the four.
- **Width:** 270 mm ✓. **The thinnest:** ≈ 10–12 mm stack (ESTIMATE).
- **Risks and checks:**
  - Tilt.
  - "Pads, not keys" against J1.
  - Foam ageing.
  - Check: one pad in a frame window.

---

## 4. Cost table (25 keys, one unit)

**Shared floor in every option [ENG §v1.4b]:**
- 30 SS49E: $11.40;
- 25 magnets: ≈ $8 (ESTIMATE; eng's cited source was sold out);
- acrylic: $8 + $5 shipping.

That's **$32.40**. **Cheaper sensors and magnets** (discoveries: ≈ $0.10
sensors, ≈ $0.15 magnets, from overseas vendors) could cut the floor to
≈ $20. That's a tariff and shipping call for eng.

| | Mechanism adds | Total | Strip C |
|---|---|---|---|
| A SWITCH | 25 Choc $17.50 [ENG] + adapters $0–5 | **$50–55** [ENG] | two rows of footprints |
| **B RAIL** | rod, tube, grease, extra acrylic | **$50–70** (ESTIMATE) | single line, 280 × 15 |
| **B RAIL, lean (Little D)** | rod $3–5, tube $6–12, plumber's silicone grease ≈ $5, blades from scrap or offcut acrylic ($0–4) | **$45–55** (ESTIMATE) | single line |
| B RAIL-M | + magnets, steel bar | $58–83 | single line |
| C COMB | Delrin, screws | $50–72 (ESTIMATE) | single line |
| D FLOAT | foam, extra acrylic, wider strip | $45–56 (ESTIMATE) | two rows |

**Finding:** the spread between mechanisms is ≈ $10–15. Against Little D's
≈ $255–320 total [ENG §v1.10], **keys are not where the money is.**

---

## 5. Ranking and recommendation

| Criterion | A SWITCH | **B RAIL** | C COMB | D FLOAT |
|---|---|---|---|---|
| Feel like an instrument (K2) | 2 | **4 (5 with M)** | 4 | 2 key / 4 pad |
| Silence (K3) | 4 | **5** | 5 | 5 |
| Velocity spread (K4) | narrow (2.8 mm) | **wide (5 mm)** | wide (5 mm) | narrowest (2 mm), position-dependent |
| Fast repeats (K5) | good | good | best | good |
| Long tops without rocking | ✗ | **✓** | ✓ | ✗ (squares only) |
| Hosts every top (piano / walnut / maple / square) | square only, really | **all** | piano / walnut / square | square only |
| Build (K7) | easiest to solder | 6 steps, weld jig | 5 steps | easiest |
| Fix one key | one switch | **one key, slide the rod** | ⅓ comb | one pad |
| Permission risk | none | none | **Delrin unverified** | foam fine |
| Height | ≈ 12 | ≈ 19 | ≈ 16 | ≈ 11 |

### Little D first (the focus; cost matters most)

**Ranked by cost:** FLOAT $45–56 ≈ lean RAIL $45–55 < SWITCH $50–55 < COMB
$50–72 (Delrin).
- The cheapest three are within ≈ $10. Little D costs ≈ $255–320 in total
  [ENG §v1.10], so **the mechanism moves the price by ≈ 3 % at most.**

**Ranked as I'd put them forward: 1 lean RAIL, 2 FLOAT, 3 SWITCH, 4 COMB.**
1. **Lean RAIL:** it ties for cheapest and beats both rivals on feel (K2),
   silence and velocity spread.
   - Its square tops give the button look of his references (C&G pegs,
     OP-1, phase8 buttons, pads), with real travel underneath. Piano tops
     are the same price.
   - **Gate:** Little D's thickness. RAIL needs ≈ 18–20 mm above strip C,
     and eng's limit is ≤ 8 mm of components under the keys (E-K2). If that
     doesn't fit, go to 2.
2. **FLOAT:** the cheapest by a few dollars, the thinnest (≈ 11 mm) and the
   easiest to build.
   - Pick it if the thickness fails, or if the owner wants pad feel. It
     honestly loses on "feel like an instrument".
3. **SWITCH:** known bought parts and the same cost. But it has the
   computer-key feel he ruled out, and long tops rock. Keep it as eng's
   fallback.
4. **COMB:** the most expensive (Delrin), and blocked until Vector Space
   permission is known. It doesn't earn its place in a cost-first
   instrument.

**If cost has to come down further, cut the floor, not the mechanism:**
- overseas SS49E and magnets: ≈ −$12 (discoveries' ≈ $0.10 / ≈ $0.15 vs
  eng's US $0.38 / ≈ $0.32; tariff and shipping per eng);
- makerspace scrap acrylic for the tops: −$8–13 [ENG acrylic + shipping].

Together that's a ≈ $25–35 RAIL.

### Full version (paused; for when it resumes)
**1 RAIL, 2 COMB, 3 SWITCH, 4 FLOAT.**
- RAIL gives real travel with any top, so SLAB (piano), MOTTO (walnut) and
  DISH (maple plugs) keep their character on one mechanism. Little D's
  build proves it.
- COMB is second if Vector Space allows Delrin.

### The one physical check, stated plainly
Every option has one unknown that only a finger can settle. For RAIL it's
the tube force.
- **No sample is needed:** build the real first two keys (C, C♯) of the
  final instrument, press them, and adjust the tube rail if needed. The
  parts stay in the build.
- Plus eng's already-planned **$8 Hall bench test**, extended to RAIL's
  ≈ 2–4.5 mm magnet gap.
- I don't think it can honestly get smaller than that.

---

## 6. Questions only engineering or the owner can answer

**Engineering:**
- **E-K1 Velocity method and scan rate.** What per-key scan rate does the key
  Pico get (full version) and the shared Pico (Little D)? Two-threshold
  timing, or a slope fit over several samples? This sets how much travel we
  actually need.
- **E-K2 Height under the keys.** RAIL's stack is ≈ 18–20 mm above strip C.
  - Does SLAB still fit board D and the pouch cells under the keys in a
    34 mm body?
  - Does Little D fit with its ≤ 8 mm under-key limit?
- **E-K3 SS49E saturation.** What's the minimum magnet-to-sensor gap at the
  bottom so a 5 × 2 mm N35 stays inside the SS49E's linear range at 3.3 V?
  It sets RAIL's sensor-line position and FLOAT's pad height.
- **E-K4 Re-arm hysteresis.** Confirm the firmware can re-trigger at ≈ 40 %
  release without upsetting single-trigger legato.
- **E-K5 Prices.** A real price for Ø 3 mm rod, ≈ 6.4 × 3.2 mm silicone tube,
  damping grease and 2–3 mm Delrin sheet, replacing my ESTIMATEs.
- **E-K6 RAIL-M.** Crosstalk from moving rear magnets, and whether a steel
  bar in the lip shifts the sensor curve beyond what calibration absorbs.

**Owner:**
- **O-K1** Is "build the first two real keys and press them" acceptable as
  the one check, in place of samples?
- **O-K2 (only if COMB stays in)** Does Vector Space allow Delrin on the
  laser and the CNC router, and how thick? (One question to the space; no
  making.)
- **O-K3** Should Little D's keys look like **piano keys or buttons**? The
  mechanism is the same (RAIL) either way, unless he picks FLOAT's pad feel.

**Director:** OK the J1 rewording in §1 (add velocity, drop "lever action").

---

## Considered and rejected

| Idea | Why not |
|---|---|
| Piezo per key (drum-pad style) | It senses the strike only, not the **hold**, so there's no note-off and legato/glide break (K6) |
| One SoftPot under all keys | Two held keys read as their midpoint, so low-note priority breaks. No velocity |
| Capacitive touch plates | No travel (K2). Velocity from touch is unreliable |
| Optical (TCRT5000-class) instead of Hall | A sensing swap, not a mechanism. Hall is already settled and cheap |
| Metal springs per key (stapler draw) | They can ping, and need a hook per key. The tube does it silently |
| Gravity return (harpsichord draw) | Fails tilted or on a lap. It became RAIL-M |
| Dual-contact rubber strips | Wrong pitch, too close to a harvested keybed [ENG §v1.4b] |
| Fatar keybed | ≈ 350 mm for 25 keys [ENG] |
