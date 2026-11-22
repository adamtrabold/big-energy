# FALLBOARD: how it works (systems)

Status: **rev 2.1, 2026-11-22**, product designer (systems focus). Rev 2.1 folds in `module-r3.md`: the lid gets a 1.2 mm skin on a 17.5 mm rib grid; module 0.70–0.85 kg with speaker E; the straight plug in the module's recessed host pocket; the depth if E needs 115. Rev 2: Brought to the director's R6 ("fewer notes": no gutter, one job per area, lighter lid, no lamp) and to the owner's 14:08 principle that **the case is entirely 3D printed**. The one module (280 × 105 × 35, hull) is in `../module/how-it-works.md`; this file covers only the carry. Marks: **[r2]** `floss/eng/module-r2.md` · **[calc]** · **[est]** · **PROPOSAL** · **UNVERIFIED** · **ENG**.

**The idea:** one plane, one lid. A piano puts the keys in front, the works behind and a fallboard over both. FALLBOARD is a shallow printed tray: the guest keyboard lies in a bed at the front, floss sits behind it, and one lid closes over the pair. It's the lead kit, on notice (director R6).

## 1. Structure
**Plan, front to back [calc]:**

| Band | Depth | Set by | Its one job |
|---|---|---|---|
| Front wall | 4 | structure | **the keyboard's datum:** every keyboard sits against it |
| **Keyboard bed** | **137** | the deepest slim keyboard (Xkey 25, 135) + 2 | the keyboard, between end blocks. **Behind a shallower keyboard, the bed is the plug's room** (§3) |
| **Cable lane** | **15** | a flat right-angle plug (≈ 10–15 [r2 §6]) | the cable from the host port: to the keyboard when open, to the left pocket when packed |
| **Module bay** | **105** | the module | floss, in a printed socket that follows the hull, with a **pocket on each side** |
| Rear wall | 4 | structure | with **two windows** in line with the module's port facets |

| | Value |
|---|---|
| **Footprint** | **412 × 265** (was 412 × 288 with the 35 mm gutter) [calc] |
| **Closed thickness** | **≈ 42** (floor 1.2 + module 35 + 4 clearance + lid skin ≈ 1) [calc]. ≈ 48 if the module goes to 41 (module §2.1) |
| **Carry weight** | **≈ 0.53–0.61 kg** printed with the stiffer lid (§5); ≈ 0.48–0.56 with the open-grid bed (§8). Eng ≈ 0.50–0.55 before the lid fix [r3] |
| **Kit weight** (module **0.70–0.85 with speaker E** [r3] + carry + cable and adapter ≈ 35 g) | nanoKEY2 ≈ 1.51–1.74 · K-Board C ≈ 1.61–1.84 · Xkey 25 ≈ 1.87–2.10 kg [calc]. Add ≈ 0.06–0.1 if the charger rides along (product UNVERIFIED). T5 withdrawn: reported, lighter is better |

**What sets the outline (director R6.5):**
- **412** = the bed's 404 inside (the Xkey's 388 + two end blocks fully in at 8 each) + two 4 mm walls.
- **265** = 4 + 137 + 15 + 105 + 4. **If speaker E needs the module at ≈ 115 deep** (module §2.2), FALLBOARD becomes 412 × 275 (25 mm clear in a 300 pack). With knob B, the closed thickness grows 7.
- **Neither is a multiple of the module's 35 mm unit, and I haven't forced one** (412 ≈ 11.8 units, 265 ≈ 7.6). Where it costs nothing, the unit shows: the lid's ribs and the open bed's grid are on a 35 mm pitch.

**Where the module sits, and why:** behind the keyboard, in the same plane, open and packed.
- **One rigid board:** on a lap it doesn't fold (job 20).
- **The per-half mapping holds:** the module is centred behind a centred keyboard, so each jamb sits behind its half (job 18).
- **The shortest cable path of any kit.**

**Every area of 412 × 265 (1,092 cm²) and its one job [calc]:**

| Area | cm² | Its one job |
|---|---|---|
| Keyboard bed, 404 × 137 | 553 | the keyboard (273–524 cm²) + end-block travel; behind a shallow keyboard, the plug's room |
| Cable lane, 404 × 15 | 61 | the cable's run |
| Module (hull) | 262 | floss |
| **Left pocket**, 62 × 105 + the crescent behind the module's shoulder (≈ 16) | ≈ 81 | **the cable's coil and the C-to-A adapter** |
| **Right pocket**, the same | ≈ 81 | **the charger** and its cable (a compact USB-C charger, ≈ 30 mm cube class, fits 62 × 105 × ≈ 35 inside; product UNVERIFIED) |
| Walls | ≈ 54 | structure |

- **No gutter, no spare pocket, no lamp, no strap, no card pocket.** The 1:1 card (CC map, the home-octave line) lies flat in the right pocket under the charger. It's paper and needs no place of its own.
- **Why the gutter could go:** the narrower module left a pocket at each end, so the coil moved there (director R6); and the flat right-angle cable (§3) needs only the 15 mm lane.

## 2. Keyboard range (job 3, 27)
| Keyboard | W × D × H [eng] | End blocks | Room behind it (bed + lane) |
|---|---|---|---|
| CME Xkey 25 (largest) | 388 × 135 × 16 | **fully in, 8 mm each** | 17: **flat right-angle plug** |
| K-Board C / nanoKEY2 / QuNexus (smallest) | 325 × 83–84 × 11–16 | **fully out, ≈ 40 mm each** | **68–69**: a straight plug, or the adapter |
| Chunky minis | up to 406 × 192 × 49 | — | **don't fit**: they play beside the kit (YOKE's wrap option can bundle one) |

**The keyboard sits against the front wall (PROPOSAL; this reverses rev 1's "keyboard against the gutter, empty strip in front").**
- **Why:** the strip a shallow keyboard leaves then falls behind it, where the plug is, so it has a job. Every keyboard packs to the same datum.
- **Cost:** a shallow keyboard's rear edge is up to 52 mm further from the module's front row than an Xkey's. The reach is still short (≈ 84 mm from the keyboard's rear edge to the front row) [calc].

**End blocks (printed):**
- Each block is a printed carriage running in a T-slot printed into the bed floor, 80 deep from the front wall.
  - It has a padded face (bought closed-cell foam, ≈ 2 mm give), a lip with ≈ 6 mm of foam over the end cap, and a bought thumbscrew lock.
  - **Each block has a ≥ 15 mm notch at its back corner** [r2], so a plug in an end socket passes the block and turns into the room behind the keyboard.
- **Nothing crosses a key.** Both blocks are set to the **same number on the printed scale** (0–32, printed in relief on the bed's front lip), so the keyboard is centred.
- **Empty:** both locked.
- **Closed:** a foam strip under the lid presses on the keyboard's top; the blocks clamp its ends; the front wall stops it.

## 3. Cable path (job 2, 20, 23)
- **Where sockets are:** anywhere along the keyboard's rear edge or on either end. Positions are mostly unpublished [r2 §6].
- **The kit cable** (module §9 S3, PROPOSAL): **0.3–0.5 m C-to-C with flat right-angle plugs at both ends.**
  - A USB-C plug is reversible, so a flat right-angle plug exits left or right by flipping it. The "which way does the angle point" problem that drove the 35 mm gutter [r2 §6] goes away for any USB-C keyboard whose socket is mounted flat (UNVERIFIED per model; ENG).
  - **At the module end the plug is straight and sits inside the module's recessed host pocket** (≈ 25–30 deep, module §4), so nothing sticks into the lane. At the keyboard end, a flat **sideways** right-angle plug sticks out ≈ 10–15 mm, which fits behind even an Xkey (17 mm).
  - Checked product: Pimoroni flat sideways right-angle C-to-C, 0.2 m or 1 m [r3 §7]. The 1 m coils in the left pocket; a 0.3–0.5 m one is UNVERIFIED.
- **Keyboards without USB-C** use their own cable on the **C-to-A adapter** at the host port. That's ≈ 50–60 mm out from the module's face [est]. It fits behind any keyboard ≤ ≈ 92 mm deep, which covers the nanoKEY2 (mini-B, 83 deep).
  - **Residual: a micro-B Xkey 25 (older units)** has only 17 mm. It takes the adapter plus a StarTech USB-A to right-angle or up-angle micro-B cable [r3 §7, listing titles], or plays lifted out of the bed.
- **It never crosses hands, speaker or panel:** hands over the bed, cable in the lane and behind the keyboard, panel above it, speaker on the crown.
- **Friend:** a 0.5 m cable lets a friend beside you on the bench hold the keyboard. For a separate lap, the optional coiled cable (product UNVERIFIED).
- **Packed:** the cable stays in the host port. Its tail runs along the lane, and the coil and adapter lie in the left pocket.

## 4. The split target (job 6)
The module's printed target and rail face the bed: set the target over B | C once. **No sentence on the module or the tray** (director R4). The 1:1 card in the right pocket carries the home-octave line and the CC map.

## 5. Lid
- **Printed, in four quarters** (206 × 132.5 each; each fits a 256 bed; the cross seam accepted, director S5), joined into one panel: **a 1.2 mm skin with ribs underneath on a 17.5 mm grid** (half the module's unit), 3–4 mm deep.
  - **Why:** eng found a 0.8 mm skin on a 35 mm grid sags ≈ 22–25 mm under a 20 N press and oil-cans 0.7 mm under a fingertip. The 17.5 grid halves the sag, and the 1.2 skin brings oil-canning to 0.2 mm [r3 §0, 6c]. **Cost ≈ +30–60 g.**
  - Closed, the lid also rests on the module's rim and the keyboard's foam strip.
  - The ribs sit inside the 4 mm clearance over the module's rim.
  - ≈ 0.17–0.26 kg [calc].
- **Hinges: printed lift-off knuckle hinges** (two, on the rear top edge), each with a bought steel pin fixed in one leaf. Lift the lid at "open" and it comes off.
- **Stay: a printed over-centre brace** (as on a folding chair: two printed links that lock straight at ≈ 100° and fold flat inside the lid). It's geometric, so it needs no fitting by trial.
- **Catch:** two bought magnets in printed pockets at the front edge.

| State | How | For |
|---|---|---|
| **Closed** | magnets; foam strip on the keyboard | carry |
| **Standing ≈ 100°** | the brace locks straight | a bench or table: music stand, shade when the sun is low in front |
| **Off** | lift-off hinges | **on a lap** (412 × 265 board), or a desk |

**The lamp is cut** (director R6.1): a lamp was considered and dropped. At night the module's TAP ring and port light are the only lights.

## 6. Flows
**Unpack and play:**
1. Lay the kit flat. Lift the lid off its magnets.
2. Lid to standing (bench), or off (lap).
3. Lift the cable's free end out of the left pocket and plug it into the keyboard (adapter if needed).
4. Switch on at the module's rear facet, through the window. The ring goes steady; the port light goes steady.
5. Play.

**Pack:**
1. Switch off.
2. Unplug the keyboard end. Lay the tail along the lane; coil it, with the adapter, into the left pocket.
3. Blocks locked.
4. Lid closed: the foam pins the keyboard; the magnets catch.
5. Into the backpack.

**Keyboard missing:** blocks locked, the lid closes the same. Play from a computer or TRS; a planted chord keeps sounding.

**Swap:**
1. Unlock and slide the blocks out.
2. Change the keyboard, against the front wall.
3. Slide the blocks in to the same number; lock them.
4. Re-set the target.

**Charge:** the charger from the right pocket into the module's rear USB-C, through the window.

**Home:** two thumbscrews from underneath free the module (S4).

## 7. States (carry; the module's are in its file)
| State | What happens |
|---|---|
| Closed, keyboard in | foam pins it; blocks locked; front wall stops it |
| Closed, empty | blocks locked; nothing rattles (the coil and charger sit in their pockets) |
| Bench, lid standing | play; the lid shades the panel |
| Lap, lid off | one stiff board |
| Friend | the cable leaves the room behind the keyboard at a back corner |
| Xkey (micro-B, old) | needs a right-angle micro-B-to-C cable, or plays lifted (§3) |
| Chunky mini | plays beside the kit; doesn't pack |
| Charging in the kit | the charger stays in its pocket, its lead through the rear window |

## 8. Making steps outside the electronics (job 26)
**Everything rigid is printed** (owner 14:08). Bought: hinge pins, magnets, thumbscrews, M3 screws, heat-set inserts, foam.

| Step | Craft | Source or method | Needs trial or measuring? |
|---|---|---|---|
| **Tray, in four printed quarters**, split on the axis and on the lane's centre line: front quarters 206 × 148.5 × ≈ 40, rear quarters 206 × 116.5 × ≈ 40 | 3D printing | our files. **Each quarter fits a 220 × 220 bed** [calc]. The seams fall on lines the instrument already has (its axis and the lane). **Or one piece from an outside service** with a bed ≥ 420 mm (availability UNVERIFIED) | no |
| Quarter joints | printed keyed lap joints + M3 screws into heat-set inserts along the seam ribs | standard printed-part practice | no |
| Module socket (follows the hull), pocket walls, rear windows, two floor bars under the inserts | printed with the rear quarters | our files | no |
| **Open-grid bed floor (lever, PROPOSAL):** the bed's floor as ribs on the 35 mm grid, open between; saves ≈ 50 g [calc] | printed | our files | no (ENG: lap stiffness) |
| End-block T-slots, carriages, the scale in relief | printed | our files | no |
| Lid, four quarters, ribbed | printed + the same joints | our files | no |
| Lift-off hinges, over-centre brace | printed + bought steel pins | our files | no |
| Magnets, foam pads, lid strip | fitting bought parts; cutting foam bought at a stated thickness | UNVERIFIED products | no |
| Thumbscrews | fitting | ¼"-20 | no |

**Honest load:** about eleven printed parts plus small hardware. No woodworking, no lining and no measured fitting. The print time is the cost (not estimated; ENG).

## 9. Owner objections and trade-offs, up front
1. **Size:** closed 412 × 265 × ≈ 42, about a 15-inch laptop's footprint and 2.5 times as thick.
   - **Backpack:** 265 in a ≈ 300 mm compartment leaves ≈ 35 mm (was 12). It stands on its 265 edge in a pack ≥ ≈ 420 mm tall inside (general pack sizes UNVERIFIED).
   - It's too big for a laptop sleeve.
2. **Weight:** carry ≈ 0.48–0.61 kg printed, with the stiffer lid. About rev 1's 0.5–0.7: **printing removed the bookcloth-lid lever**, and the lid fix adds back 30–60 g. The heaviest kit, ≈ 0.35–0.45 kg over YOKE.
3. **Craft:** printing only, with joints (§8).
4. **The keyboard against the front wall**, not the module (§2).
5. **Speaker:** sealed, published [r2]. Passive radiator dropped (module §13).

## 10. Family reuse (job 28)
- **Unchanged for Big Energy and port-a-poly:** the 404 × 137 bed, the end blocks and T-slot, the printed scale, the 15 mm lane, the kit cable, the lid hinge and brace, the thumbscrews.
- **Per instrument:** the module bay. A wider module means smaller pockets; a deeper module means a deeper tray and lid; a module wider than 404 doesn't fit.

## 11. Coverage (kit jobs, against `jobs.md` rev 3.1; the rest are in the module's file)
| Job | Supported? | Where |
|---|---|---|
| 3 one kit, backpack comfortably, no damage | **yes**: 265 in a 300 compartment | §1, §9 |
| 3 held by the ends, nothing across keys | yes | §2 |
| 3 packs empty | yes | §2, §7 |
| 3 cable, any socket position | **yes**, with the flat right-angle cable; **residual: an old micro-B Xkey** (§3) | §3 |
| 3 every area one job | yes | §1 |
| 20 park: bench and lap | yes | §5 |
| 23 share | yes (0.5 m beside you; coiled option) | §3 |
| 24 one point of view | yes: owns the outline, hosts the keys | §1 |
| 25 family | yes: printed, as Big Energy's case | §8, §10 |
| 26 printed case; making steps | yes: all printed, with the split stated; no trial steps | §8 |
| 27 swap | yes | §2, §6 |
| 28 one system | yes | §10 |
| 30 module | yes (module §2) | — |

**Unsupported jobs: none.** **At risk:** the cable's length (a 0.3–0.5 m flat sideways cable is UNVERIFIED; the 1 m one exists); socket orientation per keyboard; the old micro-B Xkey. The lid: fixed per eng.
