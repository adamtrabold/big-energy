# YOKE: how it works (systems)

Status: **rev 1, 2026-11-22**, product designer (systems focus). YOKE became a concept in the director's steer 2 (S1), and **it absorbs CLOTH** (its wrap and its grass mat become YOKE's options; `../cloth/` is retired). It answers the owner's words: "The carry should fit a portable MIDI controller but the case does not need to surround it just have an attachment point. I'm just saying don't assume not making a rule." The module is in `../module/how-it-works.md` (rev 3: 280 × 105 × 35, knob A, speaker E); this file covers only the carry. Visual's sketch: `how-it-looks-and-feels.md`, `yoke-A-carry-and-play.png`.

Marks: **[r3]** `floss/eng/module-r3.md` · **[calc]** · **[est]** · **PROPOSAL** · **UNVERIFIED** · **ENG**.

**The idea:** the module is the carry, and its attachment points are the two ¼"-20 inserts it already has (S4). Two printed arms hang on them. Each arm holds a cup that grips one end of the keyboard.
- **Carry:** the keyboard hangs keys-up under the module.
- **Play:** the arms swing forward and the keyboard sits in front.

The keyboard never flips. A stage-light yoke holds its fixture the same way: by its two ends, and it lets it swing.

---

## 0. What changed from visual's sketch, and why (systems findings)
Working the sketch through at 1:1 [calc] turned up three things it didn't solve. The mechanism below answers each:
1. **The arms crossed the end keys in play.** The pivots (x ±80) sit inside the keyboard's width (±162–194). An arm swung to a fixed angle and reaching the middle of the keyboard's end passes over the rear corner of the end octave.
   - **Fix:** each cup is hung **at the keyboard's rear corner**, and the cup reaches forward along the end. The arm arrives behind and outside the keyboard and never passes over it.
2. **In play the keyboard stays at its carry height under the arms**, so the arms are ≈ 27 mm up and the module's underside ≈ 37 mm off the bench. Held only by the arms at y 30, it tips backward: its centre of mass is at y ≈ 50.
   - **Fix:** **the cap becomes the module's rear foot in play** (director S1.1: a cap needs a second job). Flipping the cups instead would put the arms under the keyboard.
3. **A fixed play detent doesn't fit every keyboard width** (the arm angle runs 20–26° across the slim range). **Fix:** the arm is clamped at any angle by the module's own thumbscrew. **The keyboard is the jig:** you place the keyboard, and the cups follow it.

## 1. Parts
| Part | What | Size [calc] |
|---|---|---|
| **2 arms** (mirror pair) | a pivot disc (Ø 30, under the module's insert) and a T-section bar (4 mm plate + 6 mm rib, 10 tall, 22 wide) with a **45 mm slot** near its tip. Printed clip on the rib: left arm = cable coil, right arm = C-to-A adapter | ≈ 165 long; fits a 220 bed |
| **2 cups** | a C-section, 40 long, along the keyboard's end: a **lower jaw** (3 thick, 30 deep under the keyboard), an **end wall**, and an **upper lip reaching ≤ 8 mm over the end cap**. Both jaws carry 5 mm closed-cell foam; the gap is 21. A lug outside the end wall carries the swivel pin | ≈ 40 × 45 × 27 |
| **1 cap** | covers the module: a plate over the rim (1.5) + a skirt down the module's sides (35), with a notch for the cable at the host pocket. **Carry:** it protects the panel, crown, facets and front face. **Play:** it's the module's rear foot (§3) | the module's hull outline, 36.5 tall |
| Bought | the module's two ¼"-20 thumbscrews (pivots); **2 M4 thumbscrews** (each locks its cup's slot and swivel), 2 M4 heat-set inserts; foam pads | — |

**Carry weight ≈ 0.14–0.20 kg** (ASA ≈ 127 cm³ ≈ 0.14 kg + hardware) [calc/est]. That's the lightest carry by 0.25–0.45 kg.

## 2. Geometry [calc]
Module coordinates: axis x = 0, front face y = 0, keyboard on the −y side. Pivots at the inserts (±80, 30). **If the module's S4 inserts move in y** (module §2.3), every y below moves with them; nothing else changes. The swivel pin sits at the keyboard's rear corner, 12 mm outside its end.

| Keyboard | Pose | Pin at | Reach | Arm angle |
|---|---|---|---|---|
| 325 wide (nanoKEY2, K-Board C) | carry (keyboard's rear edge at y 105) | (174.5, 105) | 121 | 38° back |
| | play (keyboard's rear edge at y −15) | (174.5, −15) | 105 | 26° forward |
| 388 wide (Xkey 25) | carry | (206, 105) | 147 | 31° back |
| | play | (206, −15) | 134 | 20° forward |

- **One 45 mm slot covers 105–147** for the whole slim range. Each arm swings 51–64° between carry and play.
- **The cup grips the same 40 mm of the keyboard's end in both poses** (from the rear corner forward), so it never moves on the keyboard. It swivels on its pin, because the keyboard sets its direction.
- **Play:** the keyboard's rear edge is 15 mm in front of the module's face. That's room for the flat right-angle plug at a rear socket; the module end is a straight plug inside the recessed host pocket (module §4).
- **Narrow keyboards:** the arm's tip runs ≈ 25 mm past the cup in carry, so the bundle is ≈ 395 wide whatever the keyboard.

### 2.1 The stack
| | Carry (bottom → top) | Play |
|---|---|---|
| Keyboard | on the cup's lower jaw (3) → keyboard 11–16 | on the bench, ends on the lower jaws (3 mm: about a rubber foot) |
| Air over the keys | **≥ 9 mm** to the arm's rib (nothing touches a key) | keys open; nothing over them |
| Arms | z 27–37 | z 27–37, supported by the cups |
| Module | underside at 37 → rim 72 | underside at ≈ 37 at the pivots, rear on the cap (36.5): **level within 1 mm** |
| Cap | over the rim → **≈ 74 overall** | under the module's rear, behind the arm discs |

- **Carried size:** ≈ 395 × 135 × 74 with an Xkey (≈ 3.9 L); ≈ 395 × 105 × 69 with an 11 mm keyboard [calc].
- This is thicker than visual's 64. The difference is the arm's 10 mm stiffening rib and the cap; both are needed (§5, §3).
- **Knob B adds ≈ 7** (a 42 tall module and a 43.5 cap).
- **E at 115 deep** adds 10 to the depth only.

## 3. The cap: one part, two jobs (director S1 condition 1)
- **Carry:** it clips over the module's rim and covers the panel, the crown's grilles, both facets and the front face. A book in the bag can't press a knob. The keys are under the module's underside, 9 mm clear.
- **Play:** the cap stands rim-down on the bench (or your thighs) **behind the arm discs (from y ≈ 47)**. The module's rear underside rests on its plate at 36.5, so the module stands **level on three points: the two cups in front and the cap behind** (centre of mass at y ≈ 50, inside them).
  - **On a lap it's one piece:** two printed pegs on the cap's plate drop into two of the module's foot sockets (PROPOSAL; the feet become printed sockets, a free change in a printed shell).
- **It doesn't tilt the panel toward you;** that would need the cap taller than the module. Said plainly. In play the cap sticks out ≈ 47 mm behind the module.
- **The cap is required, not optional:** without it the module tips back in play. The wrap (§6) is the option.

## 4. The cup grip (director S1 condition 2)
- **It grips the thickness, not the shape.** The lower jaw goes 30 mm under the keyboard's bottom face and the lip ≤ 8 mm over its top face at the end, with the end wall behind. The end face's shape (square, rounded, chamfered) only meets the end wall's foam. End shapes are unpublished, so the grip relies on none.
- **11–16 mm in one cup:** a 21 mm gap with 5 mm of closed-cell foam on each jaw. That's 11 free, and 50 % compression at 16 (closed-cell foam's working range [est]; foam product UNVERIFIED).
- **Locked:** one M4 thumbscrew through the arm's slot into the cup's swivel boss. Tightened, it locks both the reach (slot) and the swivel. So each side has two screws: the pivot (module thumbscrew) and the cup.
- **Assumption shared with every kit:** the lip's 8 mm over the end cap assumes ≥ 8 mm from the end face to the first key (UNVERIFIED per model, the same as FALLBOARD's and SPINE's end-block lips). If a keyboard has keys closer, the lip sits on the end face only and the foam does the work.
- **End sockets:** the end wall has a ≥ 15 mm notch (as the end blocks) for a plug in an end socket.

## 5. Arms (director S1 condition 3, ENG)
- **T-section, 10 tall:** with a 4 mm flat plate (visual's), a 5 N load at 134 mm reach bends the tip ≈ 15 mm [calc, PETG E ≈ 2 GPa]. With the rib, ≈ 1–2 mm.
- **Loads:**
  - carry: the keyboard's weight on the cups, ≈ 3 N per side;
  - play: the module's front share, ≈ 3–4 N per side;
  - a keypress goes through the keyboard into the bench or your thighs, not into the arms.
- **ENG:** arm stiffness and the rib with published ASA / PETG properties; the ¼"-20 thumbscrew's hold at any angle (a printed index ring on the disc shows equal angles, so the keyboard sits centred); no rattle in carry.

## 6. Options from CLOTH (director S1)
- **The wrap:** CLOTH's near-black, coated, quilted square, ≈ 800 × 800, knotted round the yoked module and keyboard.
  - It adds soft protection for the keyboard's exposed front and back edges.
  - **Its sewn pocket holds the charger**, so with the wrap, the charger isn't loose.
  - ≈ 0.23–0.36 kg [r2].
  - Sewing; the owner allows a wrap around a printed core.
- **The mat on the grass:** spread the wrap coated side down, outline away from you. The yoked instrument sits on the far part; you sit on the near ≈ 435 mm. The drivers fire up through the crown, so grass doesn't muffle them.
- **The outline:** stitched at the family footprint, 412 × 265, with the centre line.

## 7. Cable, adapter, charger (job 2, 3; director S1 condition 4)
- **The kit cable stays in the module's recessed host pocket** (straight plug, inside the module). It's flat C-to-C with a sideways right-angle plug at the keyboard end (module §9 S3).
  - **Carry:** the keyboard end is unplugged, and the cable is coiled into the **left arm's clip**. The checked product is the Pimoroni 1 m [r3]; a 0.3–0.5 m one is UNVERIFIED. The 1 m length suits sharing (§9).
- **The C-to-A adapter clips to the right arm.**
- **The charger rides loose in the bag** (stated): it's any USB-C charger, the one already there. With the wrap, it lives in the wrap's pocket.
- **Play:** the cable from the host pocket runs 15 mm to the keyboard's rear socket. End sockets pass the cup's notch. It never crosses hands, speaker or panel.

## 8. Keyboard range (job 3, 27; director S1 condition 5)
- **Every 25-key portable controller in the slim class, 325–388 wide, 11–16 tall** (owner: the carry "should fit a portable MIDI controller").
- **Chunky minis (up to 406 × 192 × 49): out of the yoke.** A cup that takes 49 would push the carry stack to ≈ 110 and the module ≈ 70 off the bench in play.
  - **With the wrap, a chunky mini can be bundled beside the module** (CLOTH's old bundle). In play it's two objects on the cable. Stated, not hidden.

## 9. Flows
**Unpack and play:**
1. (Wrap: untie; spread it as the mat if you're on the ground.)
2. Unclip the cap from the rim.
3. Loosen the two cup screws and the two pivot thumbscrews (a quarter turn each).
4. Slide the keyboard out forward. Swing the arms forward with it until its rear edge is ≈ 15 mm in front of the module's face, with equal marks on both index rings. Tighten the four screws.
5. Stand the cap behind the arm discs, under the module's rear, and peg it into the feet.
6. Unclip the cable's coil; plug the keyboard end in (adapter from the right arm if needed).
7. Switch on (rear facet). Play.

**Pack:** the reverse. Unplug the keyboard end and clip the coil, cap off the bench, slide the keyboard back under the module until its rear edge is under the module's rear, swing the arms back, tighten, cap onto the rim, (wrap).

**Keyboard missing:** take the arms off (the two pivot thumbscrews) and cap the module. The module and cap are the bundle; the arms ride in the bag or stay home. **The module alone is 280 × 105 × 37, the smallest of any kit.**

**Swap:** loosen the cups, change the keyboard, and let the cups find the new ends (the keyboard is the jig). No numbers to set. Re-set the split target.

**Share:** unplug nothing. Loosen the cups and hand the keyboard over on the cable (1 m reaches a friend's lap; module §9).

**Home:** two thumbscrews and the arms are off. The module stands on its own feet.

## 10. States
| State | What happens |
|---|---|
| Carry, keyboard in | keyboard keys-up under the module, ≥ 9 mm clear; cups and pivots tight; cap on |
| Carry, empty | arms off; module + cap |
| Bench | three points: two cups + cap; level |
| Lap | one rigid piece (cap pegged in); keyboard and cap on your thighs |
| Ground | on the grass or on the wrap's mat |
| Friend | cups open; the keyboard goes over on the cable |
| Chunky mini | not in the yoke; in the wrap beside the module |
| Wind, rain | (wrap) corner weights; the coated side out |

## 11. Making steps (job 26)
| Step | Craft | Source | Trial or measuring? |
|---|---|---|---|
| 2 arms, 2 cups | 3D printing (ASA) | our files; each fits a 220 bed | no |
| Cap | printing | our files. **It's the module's size, so it needs a ≥ 300 bed or a service, or three pieces split at x 74.5 / 205.5 like the shell** [r3] | no |
| M4 heat-set inserts in the cups | soldering iron | standard | no |
| Foam pads on the jaws | cutting bought closed-cell foam at a stated thickness | UNVERIFIED product | no |
| Clips on the arms | printed with the arms | our files | no |
| (Option) the wrap | sewing: CLOTH's template, pocket and corner weights | CLOTH rev 2's making steps | no |

**Honest load:** five prints (seven if the cap is split), four screws, some foam. The lightest craft list of the three.

## 12. Owner objections, up front
1. **Exposure:** the keyboard's front and back edges face the bag (the wrap fixes it); the panel is capped.
2. **The charger is loose** (unless wrapped).
3. **Four screws to set it up** (a quarter turn each), against FALLBOARD's lid or SPINE's open-flat.
4. **The cap is a part you place** in play.
5. **No tilt and no shade.**
6. **Chunky minis are out** of the yoke.
7. **Weight: the lightest kit.**

| Kit weight (module 0.70–0.85 with E [r3] + carry 0.14–0.20 + cable ≈ 0.035) | nanoKEY2 ≈ 1.12–1.33 · K-Board C ≈ 1.22–1.43 · Xkey 25 ≈ 1.48–1.69 kg. With the wrap, + 0.23–0.36 |
|---|---|

## 13. Family reuse (job 28)
**YOKE attaches to S4 only, so every family module of any size gets it unchanged**, with the cap as the only per-module part. That's the strongest family answer of the three, because it reuses the interface, not a size.

## 14. Coverage (kit jobs, against `jobs.md` rev 3.2)
| Job | Supported? | Where |
|---|---|---|
| 3 one kit, backpack comfortably, no damage | yes: 395 × 135 × 74; panel capped; keyboard edges exposed unless wrapped (named) | §2, §3, §6 |
| 3 fits a portable controller; an attachment point, not a surround | yes: that's the concept | §0, §8 |
| 3 held by the ends, nothing across a key | yes: cups at the ends; arms ≥ 9 mm over the keys in carry, never over them in play | §2, §4 |
| 3 packs empty | yes: arms off, module + cap | §9 |
| 3 cable and adapter one place each; charger | cable on the left arm, adapter on the right; **charger loose (stated)** or in the wrap's pocket | §7 |
| 20 park: bench, lap, ground | yes: three points on a bench; one piece on a lap; ground or mat | §3, §6, §10 |
| 23 share | yes: on the 1 m cable | §9 |
| 24 one point of view | yes: the module is the instrument and the yoke is its hands; no frame around anything | §0 |
| 25 family | yes: printed; S4 | §11, §13 |
| 26 printed; making steps | yes: no trial steps | §11 |
| 27 swap | yes: the keyboard is the jig | §9 |
| 28 one system | **yes, strongest**: S4 only | §13 |
| 30 module | yes (module §2) | — |

**Unsupported jobs: none.** **Weak:** job 3's protection of the keyboard's edges without the wrap; the charger. **At risk:** arm stiffness and the thumbscrew's hold (ENG); the lip-over-end-cap assumption (shared).
