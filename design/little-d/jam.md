# Little D: jam

Owner (verbatim, 2026-11-12): "Pause the designers on the full instrument and let's focus on the budget one for now. I want designs for the budget one and I want the enclosure to be coherent in form with some clear perspective. Design principles with a solid basis of logic in the idea of the thing. Get creative here."

---

## Turn 1: product designer (systems focus)

Read: `little-d/owner.md`, `instrument/owner.md`, `eng/budget-variant.md` Part 1 (rev 6/7), `instrument/concepts/keys/discoveries.md` and `first-principles.md` (landed). Jobs below were drafted from the owner's words before reading the eng spec, then checked against it.

Marks: **stated** = owner's words in owner.md. **inferred** = mine. **[ENG]** = eng's figure. **[CALC]** = my arithmetic, shown. **ESTIMATE** = mine, unpriced.

### 1. Jobs

| # | Job | Source |
|---|---|---|
| J1 | **Play notes on 25 keys that feel like an instrument**: real travel, silent, no click, velocity. Not necessarily a traditional keybed. | stated ("feel like an instrument", "as silent as possible", "i want velocity", 25 minimum) |
| J2 | **Bend pitch with a stick that springs back (one direction) and set mod depth with a control that stays put**, using the hand that isn't on the keys. | stated (owner decisions; locked in eng §v1.5b) |
| J3 | **Shape the sound live**: reach every control of the voice (23 pots, 3 rotaries, 6 toggles, MOD dial), one control per function, while playing. | stated (control set settled); "while playing" inferred |
| J4 | **Read the patch from the panel**: knob positions *are* the state; no screens, no encoders. | stated ("no endless encoders, no LED rings/screens", confirmed) |
| J5 | **Hear it** from the built-in speaker, and from phones/line out. | stated |
| J6 | **Carry it** (small, portable) **and have it survive a bag**: knobs, stick, keys, jacks. | carry stated ("portable … which means small"); survive inferred |
| J7 | **Power it** from a USB bank or internal LiPo; charge it; play while charging; know the charge. | power stated (LiPo open, eng recommends in); the rest inferred |
| J8 | **Play and control it from MIDI** (USB + TRS): notes, bend, mod, MIDI-controllable params with jump-on-move; **know when a knob is not in control** (indicator open, owner undecided). | stated |
| J9 | **Patch it**: pitch CV out, gate out, filter CV in, EXT audio in. | stated (no extra patch points) |
| J10 | **Stay in tune with no rigmarole**, and know when it's tuning or ready. | stated (autotune, no manual cal) |
| J11 | **Build it himself**: hand-solder through-hole + plug-in modules, cut the enclosure and key tops at Vector Space, real bought parts for everything touched, at the lowest cost. | stated |
| J12 | **See one clear idea in the object**: every form decision traceable to explicit principles that follow from what the thing *is*. | stated ("coherent in form", "clear perspective", "design principles with a solid basis of logic in the idea of the thing") |
| J13 | **Label or paint it by hand** once the look is chosen. | stated ("i can make the labels myself or hand paint it") |
| J14 | **Open it to service it**: battery, one key, reflash the Pico (BOOTSEL), fix a solder joint. | inferred (kit, test unit) |
| J15 | **Play it where he is**: table, lap, couch; works tilted. | inferred (portable) |
| J16 | **Find the main controls and keys without looking**, in a dim room. | inferred (carried from the full-instrument jobs) |
| J17 | **Use the build as the proof of the full version's keys** (RAIL keys built once, here). | inferred from keys first-principles; not owner-confirmed |

**Constraint I'm treating as binding, flagged:** shared history says "design as if it may be sold: … no Moog name/trade dress." Not restated for Little D. I'm applying it: **inherit the Model D's logic, not its appearance** (no walnut-cheeked wedge pastiche). Director/owner to confirm.

### 2. Structure: what has to fit, and the arithmetic that boxes the ideas in

**Inventory every idea must place** (from eng §v1.2, §v1.5b, §v1.6):
- **Keys**: 25, run ≈ 270 mm (15 × 18 mm), key zone depth ≈ 72–75 mm. RAIL stack ≈ 18–20 mm above the key strip (E-K2 open against eng's ≤ 8 mm under-key limit — that limit was for SWITCH keys over the main board; with the board shrunk to the control area, the key zone has only the strip under it).
- **Bend stick**: #2765 in a slot gate, in the ≈ 22 mm left zone beside the keys. **MOD dial** near it.
- **Panel**: 23 pots (9 mm), 3 rotary switches (20 mm bodies), 6 toggles, power switch, MOD dial = **27 round controls + 7 levers**.
- **Speaker**: 3" (≈ 77 mm) — must sit **≥ 60 mm from the key sensor line** [ENG].
- **Jacks**: 6 × 3.5 mm + USB-C (charge) + Pico micro-USB (MIDI), unless VBUS is tied so one port does both [ENG option].
- **Board**: main ≈ 280 × 100 mm under the panel; key strip ≈ 280 × 15–25 mm under the keys.
- **Battery**: 2000 mAh LiPo + charger/boost module.
- **Body**: eng working box ≈ 290 × 170 × 32 mm.

**Panel arithmetic [CALC]:** depth left for the panel = 170 − 75 (keys) ≈ 95 mm. A 9 mm pot with a ≈ 13 mm knob wants ≈ 19–20 mm pitch. 3 rows × 20 = 60 mm + labels ≈ 75–85 mm: fits. Width: the speaker takes ≈ 80 mm out of a 290 mm row unless it moves off the panel face. With it on the face: ≈ 210 mm ≈ 10 columns × 3 rows = 30 positions for 27 rounds; toggles go between. **Tight but real.** Every idea that moves the speaker off the top face (bottom, back) buys ≈ 4 columns of breathing room. That's a structural lever, not a style choice.

**The core tension the ideas must resolve (and resolve differently):**
- The Model D panel reads **left → right in signal-flow order** (controllers, oscillators, mixer, modifiers, output). That's the instrument's grammar.
- But the controls touched *while playing* (CUTOFF, EMPHASIS, CONTOUR AMT, GLIDE, VOLUME, MOD) end up on the right, over the playing hand, while the free hand is on the left with the stick. On a 290 mm body the reach is short, so this is a mild tension, not a blocker.
- So the layout logic is a real choice: **signal flow**, **frequency of touch**, or **which hand**. Each idea below picks one on purpose.

**Six axes every concept must answer** (so concepts differ in kind, and so I can check them):
1. Layout logic of the panel (flow / touch-frequency / hand).
2. What the enclosure is made of and how it's assembled (one material? joinery? stack?).
3. Posture: how it sits on a table, lap; how it's carried.
4. Protection: how knobs, stick, keys survive a bag without a separate case.
5. Where the speaker is, and why.
6. How labels happen (engraved, hand-lettered, painted, none).

### 3. Flows (every concept must support all of these; states noted)

- **F1 Grab and play** (J6, J7, J10): take it out of the bag → (unfold/open, if the idea has a lid or stand) → power switch → status light shows *tuning* (autotune at boot, seconds) → *ready* → play. States: off / tuning / ready / tune failed (which VCO?) / low battery.
- **F2 Build a sound from scratch** (J3, J4): follow the panel's reading order. If the layout is signal flow, it's left→right; if it's touch-frequency, the idea must still give a findable "start here" (OSC 1 WAVE/RANGE).
- **F3 Perform** (J1, J2, J3): right hand on keys; left hand on stick (bend, springs back) and MOD dial; left hand leaves to ride CUTOFF/CONTOUR AMT and returns. **The reach from the stick to CUTOFF is the key measured distance in every concept.**
- **F4 Pack** (J6): power off → (close/flip/stand) → bag. Nothing proud of the outline may snag: knobs, stick cap, jack plugs left in.
- **F5 Charge / play while charging** (J7): cable into USB-C; charge state readable; plays meanwhile [ENG load-sharing].
- **F6 MIDI** (J8): USB to a computer (or TRS from a controller) → notes/bend/mod arrive → a MIDI-controlled parameter holds its MIDI value until its knob moves → (if the indicator exists) a light says "a knob isn't in control"; moving the knob clears it.
- **F7 Patch** (J9): plug CV/gate out to eurorack, filter CV in, EXT audio in. Jacks must be reachable while it's being played, cables must not cross the keys or the left-hand zone.
- **F8 Build** (J11, J17): cut all sheet parts at Vector Space → solder main board + key strip → build first two RAIL keys, press, adjust → assemble keys → mount board → close → first boot. The enclosure must be assemblable *around* a finished board, and the panel must go on after the stick (eng: fit the stick cap after the gate).
- **F9 Service** (J14): open without destroying anything (screws, not glue, on the closing face); reach BOOTSEL; slide the key rod out to fix one key.
- **F10 Label** (J13): surfaces must take laser engraving and/or paint/hand-lettering; the idea decides which.

### 4. The obvious idea, thrown away first

**The acrylic sandwich**: clear top plate, clear bottom plate, brass standoffs, board visible between, knobs on top. Every DIY synth on the internet. It's cheap (≈ $12 [ENG]) and it fits — and it says nothing, protects nothing in a bag, and has no reason for any of its proportions. Kept only as the cost floor everything else is measured against.

### 5. Draws (real randomness)

`secrets.SystemRandom` gave:
- **Oblique Strategies:** "Work at a different speed", "Only one element of each kind", "Cut a vital connection".
- **Unrelated fields:** letterpress type case, bonsai, Shaker furniture, origami.
- **Twists:** "it stands up vertically", "it must be made from exactly one sheet thickness", "the speaker is the face".

I used them as below; each idea says which draw fed it.

### 6. Candidate "ideas of the thing" → principles that follow

Five answers to *what is this object, really?* They differ in kind: an **argument**, a **container**, a **process**, a **posture**, an **exposure**. For each: the idea, the principles that follow *logically* from it (with the "therefore"), how it answers the six axes, what it costs us, and the risk.

---

#### IDEA 1 — SECOND REDUCTION: "It's the Model D's move, made again"
*Kind: an argument. Feeds: "Only one element of each kind", bonsai (prune, don't shrink). The "expected, highly designed-for-use" pole the owner asked for.*

**The idea.** The Model D was a reduction: Moog's modular, hardwired into the few connections that mattered and put in a box you could carry to a gig. Little D does the same move to the Model D: keep what makes it that instrument, cut everything else, put it in a bag. So the object should look like **an argument about what's essential** — not a shrunken Minimoog.

**Principles (and why):**
1. **The panel reads as the signal sentence, left → right** (controllers → oscillators → mixer → modifiers → output) — *because* that grammar is the part of the original that's an idea rather than an appearance. Inherit logic, not looks.
2. **One of each kind** — one board, one material, one knob style, one label method, one fastener size — *because* reduction is the point; a second kind has to earn itself.
3. **Prune, don't shrink**: nothing is a scaled-down copy; parts are full-size where hands touch (knobs, keys at 18 mm pitch) and absent where they don't — *because* a toy is shrunk, a bonsai is pruned.
4. **No bevel, no wedge, no cheeks** — *because* those are the original's appearance (and trade dress); the only inheritance allowed is the sentence.
5. **Sections are separated by space, not lines** — *because* drawing boxes around sections is decoration; grouping by gap is reduction.

**Six axes:** (1) signal flow; (2) one flat material, likely 3 mm ply or aluminium-look laser-marked panel over a simple tray; (3) flat slab, no tilt (tilt is the original's appearance); (4) low knobs, a thin sleeve/pouch — the weakest protection story of the five; (5) speaker on the face as the **output** section at the sentence's end, far right, far from the key sensors; (6) laser-engraved, one typeface, words only.

**Cost/risk:** cheapest after the sandwich. Risk: it's the least surprising; it may read as "tidy DIY" unless the visual designer finds a voice in its restraint.

---

#### IDEA 2 — TYPE CASE: "It's a case of sorts"
*Kind: a container. Feeds: letterpress type case, "Work at a different speed".*

**The idea.** A printer's type case is a shallow drawer divided into compartments; each compartment holds one sort, and **compartment size follows how often you reach for it** (the *e* box is the biggest — the California job case lay). A synth panel is a case of sorts you compose sounds from. Little D is a shallow wooden case with a real divider grid, and the controls live *in* the compartments.

**Principles (and why):**
1. **The walls are real and structural** — an egg-crate grid of slotted ply strips, which stiffens the whole case — *because* a type case's dividers aren't graphics; they hold things.
2. **Knob tops sit below the wall tops** — *because* that's what a case is for: **the grid protects the controls in a bag**, so there's no lid and no pouch (J6, F4). This is the strongest protection logic of the five.
3. **Cell size follows touch frequency** (the lay): CUTOFF gets the biggest cell; set-and-forget controls (RANGE, WAVE, DECAY toggle) get small ones — *because* that's how a compositor's case is laid out, and it puts the "work at a different speed" split in the structure: big cells are played, small cells are set.
4. **Cells are circuit sections; the grid lines are the section boundaries** — *because* one structure should carry both meanings (signal grouping and protection).
5. **Labels are like case labels**: small, at the cell's edge, hand-lettered or stamped — *because* that's how cases are marked (and the owner wants to hand-letter, J13).

**Six axes:** (1) touch-frequency lay, grouped into section cells; (2) ply tray + egg-crate grid, finger-jointed; (3) flat; its rim is the hand-rest; (4) recessed knobs, the grid is the armour; the stick sits in its own deep cell; keys protected by a rim lip; (5) speaker in its own cell, grille as a perforated cell floor; (6) hand-lettered/stamped cell labels.

**Cost/risk:** ply strips are cheap (ESTIMATE ≈ $10–15). Height: recessed knobs push the body to ≈ 34–36 mm [CALC: 3 floor + ≈ 8 clearance/battery + 1.6 board + ≈ 7 pot body + 3 panel + ≈ 11–13 low knob]. Risk: deep cells make fingers dig for knobs; cells must be wide enough to grip a 13 mm knob (≥ 24 mm). F2's "start here" must be explicit since the reading order isn't left→right.

---

#### IDEA 3 — STRATA: "It's a section through a stack"
*Kind: a process. Feeds: "exactly one sheet thickness", origami (form from one material operation), Shaker (the making is the ornament).*

**The idea.** Everything is cut from **one thickness of one sheet** and stacked. Height only exists in sheet steps. The body is a contour model — like an architect's topographic model — and its edge shows the strata. The Minimoog's tilted panel comes back not as a wedge but as **terraces**.

**Principles (and why):**
1. **One sheet thickness, everything** (body layers, panel, key frame, gate plate, even the battery pocket) — *because* the laser is the one tool, and one thickness means one material buy and one cut setting.
2. **Height comes only in whole layers** — *therefore* the panel is **terraced**, never sloped: keys lowest and nearest; the controls you play on the first terrace; set-and-forget on the higher, back terrace. (Terrace = touch frequency, like Idea 2's cells, but in section rather than plan.)
3. **Every internal part lives in a pocket cut through the layers** (board, battery, speaker, stick) — *because* in a stack, the void is the mount; no brackets, no standoffs.
4. **The edge is the face** — strata visible all round, never painted over — *because* the stack is the idea; hiding it would be lying about how it's made.
5. **Fasteners pass through the whole stack** (a few long bolts) — *because* one fastener kind, and it's how stacks are held (sandwich lamination).

**Six axes:** (1) touch-frequency by terrace (front low = played, back high = set); (2) stacked 3 or 6 mm ply (walnut-face ply would show alternating strata); (3) terraces give a natural rake toward the player; (4) back terrace rim taller than its knobs protects the set-and-forget row; front terrace knobs are the exposed ones — a weaker spot; (5) speaker in a pocket under the high back terrace, firing up through slots, max distance from key sensors; (6) laser-engraved on the terrace risers, read like contour labels.

**Cost/risk:** **material is the problem**: a hollow stack of ≈ 5–10 layers of 290 × 170 wastes most of each sheet. ESTIMATE ≈ $25–40 of ply vs eng's $12 line. Weight goes up. Mitigation: ring layers nest (cut the inner pockets as the next layer's parts). Risk: thickness grows to ≈ 36–40 mm with terraces.

---

#### IDEA 4 — RADIO: "It's a complete sound object that lives on a shelf"
*Kind: a posture. Feeds: "the speaker is the face", "it stands up vertically", Shaker oval box (one bent band), origami (living-hinge kerf bends).*

**The idea.** Little D has its own speaker and battery: unlike most synths, **it's whole on its own**, like a transistor radio. So it should behave like one: it stands upright on a shelf with its speaker facing the room, and lies down to be played. Two postures, one object.

**Principles (and why):**
1. **The speaker is the face — on the bottom.** Stand it on its back edge and the bottom becomes the front of a radio; the panel and keys face the wall, protected — *because* a whole object deserves a face, and putting the speaker on the bottom frees ≈ 4 columns of panel [§2 arithmetic].
2. **The handle is the stand**: one bent bar that's the carry handle, swings under the back to tilt it toward the player and lift the downward speaker off the table — *because* one part, two jobs, and a downward speaker needs air under it.
3. **The body is one wrapped band** — kerf-bent (living hinge) ply wraps bottom, back and top edge like a Shaker oval box or a radio cabinet — *because* a radio cabinet is a continuous skin, and kerf-bending is a laser-only operation.
4. **It's domestic, not studio**: it can sit out, so its back (seen when standing) is finished, not a service panel — *because* it lives on a shelf.
5. **Upright = listening, flat = playing** — controls only make sense in one posture, and that's legible from the form.

**Six axes:** (1) hand logic: the left half is the performance zone (stick, MOD, CUTOFF, EMPHASIS, CONTOUR AMT, GLIDE, VOLUME), the right half is setup (oscillators, contours) — breaks signal flow on purpose, *because* it's played like a radio is tuned: one hand; (2) kerf-bent band + flat panel; (3) two postures; handle-stand tilts ≈ 8–10° (ESTIMATE); (4) stood upright or carried by the handle, controls face inward; in a bag, a band lip taller than the knobs; (5) bottom, behind a laser-cut grille, ≥ 60 mm from sensors; (6) painted dial-style labels (radio dial graphics) — matches "hand paint it".

**Cost/risk:** handle is a bought part (a bent aluminium/steel bar or a drawer pull — ESTIMATE $3–8). Risks: (a) bottom speaker loudness depends on the stand; flat on a lap it's muffled — **J5 on a lap is the weak case**; (b) "stand on the back edge" puts jacks — usually on the back — on the floor; jacks must move to the side cheeks; (c) the hand-logic layout costs F2 (building a sound) clarity.

---

#### IDEA 5 — PROOF: "It's the working drawing of the full instrument, built"
*Kind: an exposure. Feeds: "Cut a vital connection" (cut the case: no box at all), and the fact that Little D is the test unit (J17).*

**The idea.** Little D is the owner's first build and the physical proof of the full version's keys, voice and firmware. A proof shouldn't hide itself. **Cut the vital connection between circuit and box: there is no box.** The one board *is* the body, held at its two ends by solid blocks; the keys are exposed levers on their rod; a single clear or smoked sheet guards the top.

**Principles (and why):**
1. **The circuit is the face** — the board is seen, so the board layout is designed to be looked at (sections laid out in signal order, traces as the diagram) — *because* it's a proof; the evidence is the point.
2. **Two end blocks, nothing else structural** — *because* a cut connection means the minimum that holds: the board and key rod span between the blocks like a bridge.
3. **Every mechanism is visible** — the RAIL keys' rod, tubes and felt are seen from the side — *because* the test unit's job is to show the full version's key works.
4. **What's hand-made is marked as hand-made** — build date, owner's mark, revision engraved — *because* it's a one-off proof, not a product.
5. **One guard sheet, not a lid** — *because* protection should be the least object that does the job.

**Six axes:** (1) signal flow (the board layout dictates it); (2) two blocks (owner's walnut offcuts, ≈ $0 [ENG]) + one acrylic guard; (3) flat; blocks are the feet and handholds; (4) guard sheet over knobs = a thin "lid" that stays on, knobs reached through cutouts — **needs a separate sleeve for bags**; (5) speaker on the guard face, visible cone; (6) none on the board if BareBones (no silkscreen) → engraved guard; with a full-spec board, silkscreen is the label, free.

**Cost/risk:** cheapest real object (walnut free, one acrylic sheet). **Trade-dress risk: two walnut end blocks = the Model D's cheeks.** Mitigation: blocks in another material (aluminium bar, ply laminate) or shaped so they read as clamps, not cheeks. Also: BareBones has no soldermask/silkscreen; this idea pushes toward a full-spec board (cost: possibly +$0–40, depends on quotes). Exposed board picks up dust and stray metal in a bag.

---

### 7. How the five differ (systems view)

| | 1 Second reduction | 2 Type case | 3 Strata | 4 Radio | 5 Proof |
|---|---|---|---|---|---|
| What it is | an argument | a container | a process | a posture | an exposure |
| Layout logic | signal flow | touch frequency (plan) | touch frequency (section) | which hand | signal flow (board) |
| Bag protection | weakest (sleeve) | **strongest (grid)** | partial (back terrace) | good (band lip / upright) | weak (sleeve) |
| Speaker | face, sentence end | its own cell | under back terrace | **bottom = face** | guard face |
| Frees panel width? | no | no | yes | **yes** | no |
| Enclosure cost vs $12 | ≈ same | +$0–5 | **+$15–30** | +$5–10 (handle) | ≈ −$5 |
| Expected ↔ sauce | expected | middle | sauce | sauce | middle |

**Combinations worth noticing (not deciding):** 2 + 3 (a terraced type case: cells in plan, terraces in section) is coherent; 4's speaker-on-bottom works under any idea; 1's "inherit logic, not looks" should probably bind all five.

### 8. Interaction details every concept must specify (systems will check these)

- **Status light** (one bicolour LED?): off / tuning / ready / tune failed / low battery / charging / charged. Where it is, per idea.
- **"Knob not in control" light** (open): if in, one LED near CUTOFF (the MIDI-controlled knob most likely to be overridden) or one per MIDI-controllable knob (cost: ≈ 8 LEDs, Pico pins). Owner undecided — each concept should show it placed and say what happens if it's left out.
- **Stick gate**: slot in the panel (or Delrin gate plate) — axis direction (bend up only? up and down? "one direction" in owner words = one *axis* in eng §v1.5b; **open question: does one direction mean bend up only, or up/down on one axis?**).
- **RANGE pots with 6 firmware detents** [ENG]: no physical click, so the panel needs printed position marks.
- **Jacks**: which edge, per posture; nothing in the left-hand zone.
- **Power switch**: recessed or guarded so it can't turn on in a bag (battery drain).

### 9. Open questions

1. Trade dress: does "no Moog trade dress" bind Little D? (I've assumed yes.)
2. Bend "one direction": one axis (up/down) or literally up only?
3. Key look (O-K3 from the keys doc): piano tops or square buttons on RAIL? It changes the key zone's character for every idea.
4. E-K2: RAIL stack (≈ 19 mm) in a ≈ 32 mm body — eng to confirm; Strata and Type case add height on top of that.
5. Vector Space laser bed size (unverified; 290 mm parts assumed fine).
6. Full-spec board vs BareBones: Idea 5 needs silkscreen to be its best.

NEXT: product designer (visual focus) — the five ideas need their look and material voice tested (which one can carry a strong form, where the "sauce" really is, and whether any should merge or die) before the director steers.

---

## Turn 2: product designer (visual focus)

Read: `little-d/owner.md`, `instrument/owner.md` (all), systems' turn 1 above, `eng/budget-variant.md` Part 1 (§v1.2, §v1.3 panel/mechanics, §v1.5b, §v1.6), `keys/first-principles.md` (§0, RAIL). Sketch sheet: `concepts/jam-visual-sketches.png` (SVG + generator `.py` beside it). Rough plans at 1 mm = 1 unit, for judging ideas, not layouts.

### 1. What applies (from the owner's words, for looks and feel)

- **"coherent in form with some clear perspective" / "solid basis of logic in the idea of the thing"** → every visible choice (silhouette, material, colour, type, how labels are made) must trace back to one idea. My test below is exactly that.
- **Span two kinds**: expected/designed-for-use AND randomness-driven "sauce / vibe". Both must be in the set the director picks.
- **Owner paints/letters by hand and needs mocks to choose.** So each idea must say what the hand does on it, and the next round must be pictures, not words.
- **Real bought parts for everything touched** (knobs, keys, stick). The knob family is therefore a *found* element, not designed; it will dominate the look (27 of them). The enclosure and labels are where the design lives.
- **Vector Space** has CO2 lasers (wood, ply, acrylic, Delrin, leather, felt, cork), fiber laser (marks aluminium), CNC, **letterpress, screen printing, industrial + embroidery sewing machines**, powder coating. Several ideas below exist only because those are there.
- **No Moog trade dress** (agree with systems' "inherit logic, not looks"). Visual corollary: no walnut cheeks, no wedge, no black-panel-with-white-Helvetica-and-blue-rockers, no Moog-style script. **Flag: the working name "Little D" itself leans on "Model D".** Fine for a test unit; if he ever sells the kit it's a naming question.

### 2. The test I applied: can the idea carry a form by itself?

A strong "idea of the thing" should *generate*, without help, all four of: a **silhouette** (what you'd recognise in outline), a **material**, a **graphic language** (how labels and marks look), and a **way of making**. If I have to bring in a style from outside to finish it, the idea isn't carrying the form.

| Systems idea | Silhouette | Material | Graphics | Making | Verdict |
|---|---|---|---|---|---|
| 1 Second reduction | — (flat slab) | "one" (any) | type only | — | **Doesn't carry form alone.** Its principles are mostly negations (no bevel, no cheeks, no boxes). Merge (below) |
| 2 Type case | yes (rimmed tray, grid) | ply | yes (cell labels, lay diagram) | yes (egg-crate) | **Keep, sharpen** |
| 3 Strata | yes (terraces) | ply | weak | yes (stack) | **Drop as a concept** (below) |
| 4 Radio | yes (two postures, band, handle) | kerf-bent ply | yes (grille, dial) | yes | **Keep, sharpen** |
| 5 Proof | weak (board + blocks) | FR4 + acrylic | silkscreen (needs a full-spec board) | — | **Merge** with a new draw (below) |

### 3. My draws (real randomness)

`secrets.SystemRandom` over my own lists (51 Oblique Strategies, 40 unrelated fields, 18 twists), `concepts/jam-visual-draw.py`:
- **Oblique:** "Use an old idea", "Simple subtraction", "What wouldn't you do?"
- **Fields:** accordion bellows, hymnals, tarot decks, pinball machines.
- **Twists:** "it looks like it was found, not bought", "the keys are the most beautiful part", "it is asymmetric on purpose".

What each did: tarot → merged into Second reduction (THE SPREAD). Pinball → merged into Proof (UNDER GLASS). Hymnal + "Use an old idea" → new HYMNAL. "What wouldn't you do?" (I wouldn't make a synth soft) → new HUSH. Accordion → **dropped fast**: its one useful truth (left hand buttons, right hand keys) is already the stick zone; the rest is bellows-and-celluloid pastiche. "Found, not bought" → steers HYMNAL and HUSH materials. "Keys most beautiful" → UNDER GLASS shows the RAIL levers. "Asymmetric" → house rule 4.

### 4. Sharpened, merged, dropped, new

#### 1+tarot → THE SPREAD *(expected pole: merged)*
**Idea.** Systems' Second reduction is right that the Model D's inheritance is its *sentence* (controllers → sources → mixer → modifiers → output). Tarot gives the sentence a positive form: **each section is a card in a spread.** The panel is five separate plates laid in a shallow dark tray, with gaps between them, numbered **I–V** in signal order.
**Principles (therefore):**
1. *One section = one plate* → grouping is by physical separation (systems' "space, not lines" made literal: the gap is the dark tray showing through).
2. *The numeral is the reading order* → "start here" is **I**, wherever the plates sit; this frees layout from strict left→right when the speaker or the stick zone demands it.
3. *Every card has one figure* → each plate carries one emblem the owner paints (e.g. I: a hand, II: three suns, III: a confluence, IV: a door, V: a mouth). This is his canvas, and it's the only decoration allowed, because a card's figure *is* its meaning.
4. *One of each kind* (kept from systems): one plate material, one knob, one typeface, one fastener.
**Form/material/graphics/making.** Flat slab, low, OP-1-like posture. Tray: 3 mm ply or black acrylic. Plates: either fiber-laser-marked anodised aluminium (crisp, cheap offcuts, ESTIMATE) **or** clear acrylic reverse-painted from behind (see UNDER GLASS), which gives the hand-painting a gloss surface it can't wear through. Numerals and scales laser-engraved; emblems painted.
**Why it's the expected pole:** signal-flow layout, flat, nothing unusual to learn, cheapest after the sandwich. The voice comes from the plates-and-numerals system, not from the shell.
**Weakness:** bag protection is a sleeve (as systems said). Gaps between plates collect crumbs; keep them ≤ 3 mm.

#### 2 TYPE CASE *(kept, sharpened)*
- **Cells = circuit sections, not one cell per knob.** Per-knob cells at 20 mm pitch leave ≈ 3 mm walls between 13 mm knobs and fingers can't grip. Section cells (5–7 of them) are honest to the case (a case of sorts has big and small boxes) and easy on the fingers. Cell size then follows content, which is uneven on its own (oscillators big, mixer narrow), so the lay comes free; I'd drop systems' "cell size by touch frequency" as a separate rule: it fights signal grouping.
- **Labels: slide-in cards** in a slot at each cell's front edge, the way case drawers carry a card in a frame. Cards letterpress-printed at Vector Space, or hand-lettered, swappable forever (J13). This is the idea's best visual: the grid plus the little white cards.
- **Speaker must leave the face** (bottom), or the walls eat the width [CALC: 290 − 12 rim − 80 speaker − ≈ 15 walls ≈ 183 mm ≈ 9 columns × 3 rows = 27 rounds, zero slack]. With it underneath, ≈ 13 columns.
- **Palette in the material:** natural ply walls, darker (stained or oiled) cell floors so knobs and cards pop. One colour of knob, light, against dark floors.
- **Terraces borrowed from Strata, optional:** the back row of cells one layer higher, for a rake without a wedge.
- Risks: ≈ 34–36 mm thick (systems' calc); "Etsy wooden tray" if the proportions are lazy. The walls should be thin and crisp (3 mm), not chunky.

#### 3 STRATA *(dropped)*
Three reasons: (a) +$15–30 of ply against a cost-first brief; (b) 36–40 mm thick against "portable … small"; (c) **looks**: stacked laser-ply edges are the most common laser-cut craft look there is, so it would read as "made on a laser", not as an instrument. Salvage: **one sheet thickness** as a house rule; **terraces** as a tool (Type case).

#### 4 RADIO *(kept, sharpened)*
- Keep the two real truths: **it's whole on its own (speaker + battery), so it has a face**; and **handle = stand**.
- **Drop the hand-split layout.** It doesn't follow from "radio"; it costs F2. What *does* follow: **a radio has one big dial.** So: one oversized knob, **CUTOFF** (the thing you "tune" while playing), everything else in signal order at normal size. One visual hierarchy, from the idea.
- **The identity lives on the speaker face**, not the panel: a big laser-cut grille pattern on the bottom, which is the face when it stands. Panel stays plain and functional. Two faces, two jobs.
- Risk: radio nostalgia → Braun T-series or TE OB-4 pastiche. Stay away from chrome, rounded-rectangle-with-dial-window, and fake tuning scales.

#### 5+pinball → UNDER GLASS *(merged)*
**Idea.** A pinball playfield is the mechanism under glass, and its artwork is painted on the glass. Little D: **the board is the playfield; a clear acrylic top sheet sits over it; the owner reverse-paints the underside** (paint goes on in reverse order, last detail first, viewed through the sheet). Opaque paint frames and labels; clear windows are left over the parts worth seeing (VCO cores and expo arrays, the ladder's matched pairs).
**Principles:** (1) *show the proof, frame it* → windows only where the circuit means something; (2) *the art is under the glass* → reverse painting, so labels never wear and the face is one clean gloss sheet; (3) *rails, not cheeks* → bought aluminium U-channel along front and back (pinball side rails / lockdown bar) instead of systems' end blocks, which kills the trade-dress risk and gives handholds; (4) *the keys are the most beautiful part* (twist) → RAIL levers seen through clear side panels.
**Why merge:** Proof alone needed a silkscreened board to look like anything. Reverse painting makes a bare BareBones board fine: the paint does the labelling.
**Weakness:** bag (sleeve needed); reverse painting is unforgiving (but it's acrylic: one sheet ≈ cheap to redo, ESTIMATE).

#### NEW → HYMNAL *(sauce: a bound book you carry)*
*Draws: hymnals, "Use an old idea", "found, not bought".*
**Idea.** A hymnal is a small hard-bound book of songs you carry to where the singing is. Little D is **bound like a book**: the instrument is the book block, inside hard covers with a cloth spine along the back edge.
**Principles (therefore):**
1. *The cover is the protection* → no bag, no sleeve. The body's rim stands taller than the knobs (the book's "squares"), the cover closes onto it.
2. *A book opens to be read* → open, the cover stands up behind the panel as a **music desk**; the inside cover (endpaper) faces the player.
3. *The ribbon is the stay* → a hymnal's ribbon marker, sewn into the spine, tethers the open cover at its angle. Folded all the way under, the cover and spine roll give a rake [CALC: ≈ 14 mm lift over 170 mm ≈ 5°].
4. *No recall, so write it down* → the endpaper is a **patch chart** (the panel printed as a diagram to pencil in settings — the Minimoog patch-book habit, made part of the object) plus room to clip a lyric or chord sheet. For a songwriter this is functional, not cute (J4).
5. *Bound things are titled on the spine* → name, revision and date blind-stamped or foil-stamped on the spine with letterpress type.
**Form/material/making.** 3 mm ply boards, bookcloth over (ESTIMATE $10–20), PVA, a cloth hinge; Vector Space letterpress for spine and patch-chart printing. Panel inside: a plain printed "page" (letterpress or screen-printed on the panel itself). Speaker on the panel's right as the page's "illustration", or underneath.
**Risks:** ≈ 40 mm thick closed [CALC: ≈ 34 body with knobs + 2 × 3 covers]; cloth hinge durability; cloth gets grubby (bookcloth is coated, partly mitigates). Cutesy if the panel graphics go "olde"; the panel must stay crisp and modern so the book reads as structure, not costume.

#### NEW → HUSH *(sauce: built from the material of silence)*
*Draws: "What wouldn't you do?" (make it soft), "found, not bought".*
**Idea.** The owner's hardest feel rule is "as silent as possible". In RAIL keys, silence is made of **felt** (top stop under the lip, washers, guide comb) and silicone. So: **the material that makes it quiet is the material of the whole.** A rigid inner tray, skinned in 3–5 mm wool felt.
**Principles (therefore):**
1. *The skin is a working part* → the felt over the panel wraps round the panel lip and **is** the strip the key tails rise into: the RAIL top stop and the enclosure are one piece of felt (sketch §4).
2. *Nothing hard touches the hand except what plays* → knobs, keys, stick are the only hard things; everything else is soft.
3. *Soft things close by rolling* → the bag protection is a felt flap that rolls over panel and keys and closes with a bought wooden toggle and elastic loop (chisel/knife-roll logic).
4. *Marks are made in the material* → labels **embroidered** (Vector Space embroidery machine) or laser-browned into the felt; fine scales (RANGE detent marks) on a thin hard plate where precision matters.
**Why it's good for J15:** on a lap it grips and is warm; on a table it's silent and won't slide.
**Risks:** grime and pilling around knobs (the felt under the knobs takes the most hand contact); felt absorbs speaker highs, so the grille must be an open window with speaker cloth, not perforated felt; reads as a "tech sleeve accessory" if the felt is thin and pastel. Push heavy undyed industrial grey.

### 5. House rules I'd bind on every concept (look and making)

1. **Inherit logic, not looks** (systems', agreed).
2. **The machine marks what must be exact; the hand marks what must be meant.** RANGE detents, pot scales and jack legends are laser-engraved/marked; names, emblems, titles can be painted or lettered. This makes "I'll hand paint it" safe: he never has to hand-paint a 6-position scale 27 times.
3. **One knob family, chosen early.** 27 bought knobs will set the character more than any shell. The knob and the 20 mm rotary switch caps need the same family. I need to pick from what Tayda/US vendors actually stock (not checked yet) before the mocks.
4. **Asymmetric on purpose:** the left 20 mm stick zone is its own visual object (cell, gate plate or inset), never disguised as part of the panel.
5. **One sheet thickness where it can be** (from Strata): one buy, one laser setting.
6. **Status light** is one small, warm point, placed where the idea says the "voice" is (SPREAD: on plate V; TYPE CASE: in the speaker/output cell; HYMNAL: on the spine end; HUSH: through a punched hole in the felt; RADIO: on the face; UNDER GLASS: under the paint, glowing through a window). The "knob not in control" light, if adopted, sits beside CUTOFF in every concept.

### 6. Recommendation for the concept set (director decides)

| | Kind | Pole | Carries form? | Protection | Enclosure cost vs $12 (ESTIMATE) |
|---|---|---|---|---|---|
| THE SPREAD | a system (card spread) | **expected** | yes, via graphics | sleeve | ≈ same to +$5 |
| TYPE CASE | a container | middle | yes | **built in** | +$0–5 |
| HYMNAL | a binding | **sauce** | yes | **built in** | +$10–20 |
| HUSH | a material | **sauce** | yes | built in (roll) | +$15–30 (wool felt) |
| RADIO | a posture | sauce | yes | handle/upright | +$5–10 |
| UNDER GLASS | an exposure | middle | yes | sleeve | ≈ same |

My pick for mocks: **SPREAD, TYPE CASE, HYMNAL, HUSH** (two designed-for-use, two sauce; three of four carry their own protection; four different kinds). **RADIO and UNDER GLASS as donors:** the bottom speaker (Radio) can go into Type case and Hymnal; reverse-painted plates (Under glass) are SPREAD's best plate finish.

### 7. Open questions

1. Does the owner want it to **carry its own protection** (no separate bag/sleeve)? It splits the set: Type case / Hymnal / Hush yes; Spread / Under glass no.
2. **Thickness tolerance:** is ≈ 35–40 mm still "portable … small"? (OP-1 is ≈ 13 mm; the RAIL stack alone is ≈ 19 mm, so ≈ 32 mm is the floor anyway.)
3. **Knob family**: which bought knobs exist at the price (needs a catalogue check before mocks).
4. **Bend direction** (systems' Q2) changes the gate plate's look: one slot or a centred slot.
5. **Speaker on the bottom** for Type case/Hymnal: loudness on a lap (systems' Radio risk applies).
6. **Name** "Little D" if it's ever sold.

NEXT: design director — six ideas on the table (four recommended for mocks); needs steering on which go forward and on Q1 (self-protecting or not) before systems and I build concepts.

---

## Turn 3: design director

Read: `owner.md` (both), this jam (Turns 1–2), `concepts/jam-visual-sketches.png`, `eng/budget-variant.md` (sizes, enclosure line, totals), `keys/first-principles.md` (RAIL), and **`eng/keys-answers.md` (new, landed during this turn)**. Prior director notes on the full instrument kept for consistency (hero CUTOFF, one light, no cheeks).

### 0. New engineering facts that change the box (from `eng/keys-answers.md`)

- **RAIL fits, slimmed:** white key surface ≈ 22 mm, **lip ≈ 26 mm** above the outside of the bottom, inside a ≈ 30 mm control zone. Eng suggests the keys as a **lower step (≈ 26 mm) in front of a 30 mm control zone**.
- **Depth grows to ≈ 180 mm** (was 170), or the lip zone overhangs the main board's front edge.
- **The rod needs a support comb every 3–4 keys, hung from the lip.**
- RAIL ≈ $52–58 (or $35–46 on scrap acrylic). Totals unchanged.

**What this means for design (my reading, and it's the most useful fact in the jam):** the lip over the key tails is now doing three jobs: it's the keys' **top stop** (felt under it), it **carries the rod** (supports hang from it), and it's the **step** between key zone and control zone. **The lip is the instrument's spine.** It's the one place where enclosure and mechanism are the same part. Every concept must make the lip the thing its idea is most about, not a strip hidden under a panel edge. (Rule H3 below.)

Working envelope for all concepts: **≈ 290 × 180 mm, key step ≈ 26 mm, control zone ≈ 30 mm + knobs.** Anything thicker must say what it buys.

### 1. My draws (real randomness, `secrets.SystemRandom`)

- **Oblique:** "Reverse", "Remove specifics and convert to ambiguities", "What mistakes did you make last time?"
- **Fields:** seed packets, surveyor's instruments, cigar boxes.
- **Twists:** "it hangs on a wall", "it is one colour only", "it must be repaired in public".

What I did with them:
- **"What mistakes did you make last time?"** taken seriously. On the full instrument the owner's sharpest reactions were to **cost** ("oh wow this is way more than I expected", "250 feels high") and to things he'd said no to being proposed again. Two of the four sauce ideas (HYMNAL, HUSH) add $10–30 to the enclosure. That's the mistake about to repeat. Rule H5 below.
- **Cigar boxes**: the cigar-box guitar is *the* folk tradition of the cheap, hand-built instrument made from a box. It confirms HYMNAL's family (a covered box with a printed label) and gives it a better argument for this owner: "the budget instrument in its own box" is older and more American than a hymnal. I'm not making it a separate concept; it's a fork HYMNAL must resolve (§3).
- **"Reverse" + "one colour only" + "repaired in public"** produced my one new direction, ONE SHEET (§2). Surveyor's instruments and seed packets I drew and dropped: the first gives fitted cases and fine scales (already TYPE CASE and house rule 2); the second gives "instructions printed on the package" (already HYMNAL's endpaper).
- **"It hangs on a wall"**: a donor, not a concept. A keyhole slot in the bottom costs nothing. An instrument that's on the wall gets played; one in a bag doesn't. Offer it in every concept that has a finished bottom.

### 2. New direction: ONE SHEET ("the budget is the form")

*Kind: an economy. The owner's first concern is cost, and this is the budget instrument. So make the budget the idea, visibly, instead of a constraint everyone hides.*

**The idea.** The entire enclosure (shell, panel, lip, rod supports, key comb, gate plate) is cut from **one standard sheet** in one laser job, and **the nest is the drawing**. Every part's proportion is decided by what fits on the sheet with the others. Arithmetic [CALC]: a 12 × 24 in (305 × 610 mm) sheet is ≈ 186,000 mm². A 290 × 180 × 32 shell (top, bottom, four walls) is ≈ 134,500 mm², ≈ 72 %, which leaves ≈ 51,000 mm² for the lip, combs and small parts. Tight, real. A sheet of 3 mm birch ply at that size costs well under eng's $12 enclosure line (ESTIMATE; designers verify Vector Space stock and bed size).

**Principles (therefore):**
1. *One sheet, one job, one colour* → the shell, panel and lip share one material and one grain direction, so the grain runs continuously across the object. Colour comes from the material only.
2. *Every hole becomes a part* → offcuts are not waste. The key window's offcut, the speaker hole's disc, the gate slot's slug each must become something (a key guard, a battery door, a foot). **Only where it really works.** An offcut is exactly the size of its hole, so it can't rest on the hole's edges; if the cascade doesn't work physically, drop it and keep principle 1.
3. *Repaired in public* → visible screws, one size, and the nest map engraved on the bottom: every part labelled with where it came from on the sheet, so a broken part can be recut from the file. It's a kit, and it says so.
4. *The machine marks everything in the same pass* → legends, scales and the owner's own marks engraved in the cutting job. Hand-painting goes on top if he wants it, never needed.

**Why it's here:** it's the only idea that comes from the owner's *main* concern rather than from a metaphor, and it's the cheapest coherent enclosure possible. **Why I'm suspicious of it (my favourite, so I'm hard on it):** (a) "made on a laser" is exactly the look visual killed Strata for; a finger-jointed ply box is the Etsy default. It must not use finger joints as its look. Kerf-bent corners (one band, from Radio) or a hidden joint, and proportions that would be right even if you didn't know the story. (b) The nest could force bad proportions; if it does, the sheet loses to the hand. (c) The story is invisible unless the nest map is shown, which can tip into gimmick.

### 3. Rulings on the six on the table

| Idea | Ruling | Why |
|---|---|---|
| **TYPE CASE** | **Forward: the designed-for-use concept** | Strongest enclosure form; protection is structural; the slide-in cards answer J13 elegantly. Cells = sections (agree with visual). |
| **THE SPREAD** | **Merged into TYPE CASE** | SPREAD and TYPE CASE are the same kind (sections made physical: gaps vs walls), so two concepts would differ in styling, not kind. SPREAD's enclosure is just a tray, which fails the owner's main ask ("enclosure coherent in form"). Its best part, **numerals I–V as reading order**, goes onto TYPE CASE's cards. Tarot emblems: optional, the owner's own figures if he wants them, no occult iconography. |
| **HYMNAL** | **Forward: sauce** | The cover-as-protection and cover-as-music-desk are real use; the endpaper patch chart answers "no recall" for a songwriter. |
| **HUSH** | **Forward: sauce** | The best-grounded idea in the jam: it comes straight from the owner's hardest feel rule (silence), and RAIL's felt top stop under the lip *is* the skin. Fits H3 better than anything. |
| **ONE SHEET** | **Forward: the rational/cost concept** | §2. |
| RADIO | Donor | Bottom speaker and the kerf-bent band go to whoever needs them. The upright posture fails on a lap (J5) and the hand-split layout costs F2. |
| UNDER GLASS | Donor | Reverse-painted acrylic is an option for TYPE CASE's cards or HYMNAL's panel. Weak in a bag; the exposure idea needs a silkscreened board (pending owner Q on board finish). |
| STRATA | Dead (agree) | Cost, thickness, laser-craft look. |

**Four concepts go forward: TYPE CASE, ONE SHEET (designed for use / cost logic), HYMNAL, HUSH (sauce / vibe).** Four different kinds: a container, an economy, a binding, a material.

**Pushes on each (what the concept must answer, beyond visual's notes):**

**TYPE CASE**
1. Signal-flow sentence left → right, cells in that order, numbered I–V on the cards. Cell size follows content. The stick gets its own deep cell at the far left (house rule 4, asymmetric).
2. **The lip is the front wall of the case.** The case's front rail over the key tails is the RAIL lip: felt under, rod combs hung from it. The case and the keyboard share their frame; show that in section.
3. Finger room: a 13 mm knob in a cell whose wall is ≈ 12 mm high must still be gripped at the cell's edge. Show the worst knob (nearest a wall) at real size, with a thumb.
4. Show the walls at 3 mm and crisp. If it reads as an Etsy tray in the mock, it fails.

**ONE SHEET**: §2, plus show the real nest (sheet outline with every part placed), the grain direction, and the object at real size. If it needs more than one sheet, say so and say which size.

**HYMNAL**
1. **Resolve the fork: book or cigar box.** Same structure (box + hinged cover + printed label). The book gives the ribbon stay, cloth spine and endpaper; the cigar box gives the folk-instrument lineage, a paper label on the lid, a simpler wooden hinge, and less cloth to get grubby. Pick one and say why, or show both as two small sketches in the concept so the owner can choose.
2. The cover must close onto a rim taller than the knobs **and** clear the lip/key step. Show the closed section with real heights (≈ 40 mm closed is the claim).
3. The panel graphics stay crisp and modern; the "old" is in the structure only.
4. **Cost:** bookcloth + boards + PVA must be priced. Over $15 for the enclosure needs a named cut (H5).

**HUSH**
1. **Pair it with DISH keys** (from the keys doc: a bought maple plug on each lever rising through a felt-collared hole). The owner named Critter & Guitari's maple keys as a reference; this is where they belong. If DISH can't do velocity at the same feel, say so; flat key tops otherwise.
2. A rigid ply or acrylic tray under the felt carries the pots and the lip; felt is the skin, not the structure. Show where hands wear it (around CUTOFF, the stick, the right-hand rest) and what replaces felt there, if anything.
3. Heavy undyed grey wool felt, not pastel, not thin. Embroidered or laser-browned labels; machine-marked hard scale plates only where precision matters.
4. Speaker window is open with speaker cloth. **Cost:** wool felt must be priced at the real area (skin + roll flap). H5 applies.

### 4. House rules (binding on all four concepts; mine to rule)

- **H1. Inherit logic, not looks.** The Model D's signal sentence yes; wedge, cheeks, black/white Helvetica panel, blue rockers no. (Owner confirmation pending; designers proceed as if yes.)
- **H2. Prune, don't shrink** (from Second reduction). Full-size where hands touch: 13 mm knobs, eng's key size. Absent where they don't.
- **H3. The lip is the spine.** Each concept shows a side section through the key zone: bottom, strip C, key, felt top stop, the lip, a rod support comb, and the step to the control zone, at eng's heights (key ≈ 22, lip ≈ 26, control zone ≈ 30 mm). The lip's form must come from the concept's idea.
- **H4. One hero knob: CUTOFF.** Everything else one standard knob from one bought family (Tayda or a US vendor, priced). Visual picks the family before the mocks; the 20 mm rotary caps must match it.
- **H5. Cost discipline.** Each concept states its enclosure cost against eng's ≈ $12 line, and build hours. Over $15 needs a named saving elsewhere or goes to the owner as a choice. The owner has said $250 feels high.
- **H6. Machine marks what must be exact; the hand marks what must be meant** (visual's rule 2, adopted).
- **H7. One status light**, warm, placed where the idea says the voice is; the "knob not in control" light (if adopted) next to CUTOFF in every concept. Power switch guarded or recessed.
- **H8. Envelope:** ≈ 290 × 180 mm; ≤ 36 mm thick including knobs in play state; 40 mm is a hard ceiling pending the owner's answer. Speaker ≥ 60 mm from the sensor line; a bottom speaker needs feet ≥ 8 mm and a lap test (say how loud on a lap).
- **H9. Jacks on one edge, never on the left (stick) end or under the keys.** The concept decides which edge and why.

### 5. What every concept delivers (the owner judges looks from pictures)

1. **One believable 3/4 picture** in real material and colour. This is what he'll react to; make it good enough to judge looks.
2. Top view at real mm, with the panel in reading order and CUTOFF marked.
3. The H3 side section.
4. Carry state and play state (closed/open, rolled/unrolled, etc.).
5. The principles, 3–5, each with its "because".
6. Enclosure cost, build hours, thickness, and where the owner's hand (paint, lettering, print) goes.
7. Answers to systems' six axes and its interaction details (§8 of Turn 1), briefly.

Things not to spend time on: final legends, exact pot positions beyond what proves the layout fits.

### 6. Questions for the owner

Added to the ones already with you (trade dress, bend direction, board finish, self-protecting, 35–40 mm thick):

1. **Enclosure budget:** would you pay ~$10–20 more for a body that protects itself (no case or sleeve), or must the enclosure stay around $12?
2. **Key look:** flat piano-shaped key tops, or round maple pegs (Critter & Guitari-like) poking through the top? Same mechanism and velocity either way.

READY: TYPE CASE, ONE SHEET, HYMNAL, HUSH — four kinds, two designed-for-use and two sauce. Systems and visual build them against house rules H1–H9 and the §5 deliverables. Eng's key facts (§0) are the starting dimensions.
