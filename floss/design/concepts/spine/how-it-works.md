# SPINE: how it works (systems)

Status: **rev 1, 2026-11-22**, product designer (systems focus), concept round 2. The one module (297 × 105 × 40 at the rim) is in `../module/how-it-works.md`; this file covers only the carry. Marks: **[r2]** · **[eng]** · **[calc]** · **PROPOSAL** · **UNVERIFIED**.

**The idea, reworked after the owner's 13:25 direction:** the director's addendum: "a book with one thin cover and one fat cover is not a book." Agreed. But bookbinders have an object for exactly this case: **the clamshell (solander) box.** It's two trays of the same outline, one deeper than the other, joined by a cloth-covered spine, closing square. SPINE becomes that:
- the **keyboard tray** (shallow);
- the **module tray** (deep);
- one **spine**.

It's still bookbinding, and it's the rival to FALLBOARD on bag space.

## 1. Structure
| Part | Size [calc] | Holds |
|---|---|---|
| **Keyboard tray** | 412 × 143 × ≈ 21 (3 mm board + 18 mm walls) | the keyboard between end blocks; the brass scale on its open edge |
| **Module tray** | 412 × 143 × ≈ 40 | **the module, front face toward the spine**; a cable strip (404 × 30) between it and the spine; a pocket each side (53.5 × 105) |
| **Spine** | 412 long × ≈ 61 (the closed thickness) | a **rigid spine board between two cloth joints, stop-at-flat** (visual, turn 5; accepted, turn 6); **open, it's the cable's gap** (§4) |

| | Value |
|---|---|
| **Closed** | **412 × 143 × ≈ 61** [r2: module 40 + keyboard 16 + board 3 + 2 air] |
| **Open flat** | 412 × ≈ 347 (143 + 61 + 143) |
| Carry weight | ≈ 0.3–0.4 kg [r2: 0.22–0.30 for one keyboard board, plus the module tray; calc] |
| **Kit weight** (module 0.67–0.93 [r2] + carry + ≈ 35 g of cable and adapter) | nanoKEY2 ≈ 1.25–1.61 · K-Board C ≈ 1.35–1.71 · Xkey 25 ≈ 1.6–1.97 kg [calc]. **T5 met with the nanoKEY2 class at the light end; missed with an Xkey** [r2] |

**Where the module sits, and why:**
- **Open:** behind the keyboard across the spine, its front face (host port, target rail) toward the spine and keyboard. The jambs sit behind their halves.
- **Packed:** face down over the keyboard, panel to keys, both protected inside. The knobs sit under the module's rim, so nothing presses a key.
- **Why:** the smallest rigid footprint, ≈ 50 % of FALLBOARD's area, which suits the owner's "fit in a backpack comfortably".

**Every square centimetre of the module tray (412 × 143 = 589 cm²) [calc]:**
| Area | cm² | Its job |
|---|---|---|
| Module | 312 | floss |
| Cable strip, 404 × 30 | 121 | packed: the cable and the C-to-A adapter; open: where the cable rises from the spine gap to the host port |
| Left pocket, 53.5 × 105 | 56 | the charger (≈ 36 inside: a ≈ 30 mm-cube charger, UNVERIFIED) |
| Right pocket, 53.5 × 105 | 56 | spare cable, strap, card |
| Walls | 44 | structure |

**Keyboard tray (589 cm²):** the keyboard plus end-block travel. A shallow keyboard's leftover strip stays empty bed.

## 2. Keyboard range (job 3, 27)
The same end blocks, track, ≥ 15 mm notch and brass scale as FALLBOARD (one family part):
- **Xkey 25:** blocks fully in.
- **325 × 83 keyboards:** blocks fully out.
- **Chunky minis:** don't fit (CLOTH).

Closed, a foam strip on the module tray's rim presses on the keyboard. **Empty:** blocks lock.

## 3. The spine and its states
| State | Angle | For |
|---|---|---|
| **Closed** | 0° | carry; a strap round the box (bought) |
| **Standing** | ≈ 110° | a table: the module stands behind the keys, panel and speaker toward you. The optional lamp (FALLBOARD's AAA strip) clips to the module tray's top edge |
| **Open flat** | 180°, **stops** | **a lap or bench:** the spine runs left to right across both thighs, and each tray spans the gap (visual, turn 5). The stop-at-flat spine won't fold downward under a keypress |

- **Honest:** whether the stop-at-flat spine holds a keypress load can't be worked out from published data. It's bookbinding practice: a hinge that stops against bevelled boards.
  - **The first build needs one trial:** open flat, press the end keys, look for give.
  - If it gives, use a thicker spine board (the director ruled out the slat).
  - This is the one trial step in this kit (job 26).
- Lifted by its ends, or across a gap, the joints can still fold upward. Don't play it bridged.

## 4. Cable path
- **Open,** the keyboard's rear edge faces the spine. **The 61 mm spine gap is the gutter:** a straight plug from any rear socket position (25–35 mm [r2]) fits in it.
  - End sockets pass the end block's notch.
  - The 0.3–0.5 m cable [r2] rises through the cable strip into the **host port on the module's front face**, which also faces the spine.
- It never crosses hands, speaker or panel.
- **The cable is in the handle:** you carry the closed box by its spine (the jam constraint, surviving).
- **Packed:** the cable stays in the host port, coiled in the cable strip with the adapter.
- **Friend:** as FALLBOARD (0.5 m beside you; optional coiled cable).

## 5. The split target and the line (job 6)
The module's target rail faces the spine, readable from the playing position across the open spine. The line is engraved on the module; the 1:1 card inside the keyboard tray repeats it.

## 6. Flows
**Unpack and play:**
1. Lay the box down, spine away from you. Undo the strap.
2. Swing the module tray over to flat (lap) or standing (table).
3. Lift the cable from the strip and plug in the keyboard (adapter if needed).
4. Switch on.
5. Play.

**Pack:**
1. Switch off; unplug the keyboard end.
2. Coil the cable into the strip.
3. Blocks locked.
4. Close the module tray over the keyboard.
5. Strap. Into the backpack, spine up.

**Keyboard missing:** close it empty, blocks locked. **Swap:** as FALLBOARD. **Home:** two thumbscrews.

## 7. States (carry)
| State | What happens |
|---|---|
| Closed, keyboard in | rim foam pins the keyboard |
| Closed, empty | blocks locked |
| Open flat on a lap | stiff in the loaded direction (stop-at-flat; one trial) |
| Bridged or lifted by the ends | joints can fold upward: don't |
| Standing | panel and speaker toward you; optional lamp |
| Friend | the cable leaves the spine gap |

## 8. Making steps outside the electronics (job 26)
| Step | Craft | Source or product | Needs trial or measuring? |
|---|---|---|---|
| Two trays in binder's board or thin ply, covered in bookcloth | bookbinding: **the clamshell (solander) box**, a standard project with many published guides (specific guide UNVERIFIED) | binder's board, bookcloth, PVA; **our 1:1 templates** | no |
| Rigid spine board between cloth joints, bevelled tray edges | bookbinding | as above | **yes: one fit trial** (§3) |
| Module cut-out, pocket dividers | cutting | templates | no |
| End blocks, track, notch, foam, brass scale | as FALLBOARD | as FALLBOARD | no |
| Strap, brass book corners | sewing / fitting bought parts | UNVERIFIED | no |
| Lamp clip (optional) | fitting | as FALLBOARD | no |

**Honest load:** a clamshell box is a weekend of bookbinding; the spine trial is the risk. Less hardware than FALLBOARD.

## 9. Owner objections and trade-offs, up front
1. **Size:** closed 412 × 143 × 61, ≈ 3.6 L [calc], like a thick hardback a little wider than a keyboard. The smallest rigid kit. It stands in a daypack's main compartment (≥ ≈ 420 tall inside; general sizes UNVERIFIED).
2. **Weight (trade-off):** T5 only with the lightest keyboards; an Xkey misses [r2]. Eng's lighter-shell levers apply to the module.
3. **Craft:** §8; one trial step.
4. **Home octave:** module §4.
5. **Lamp:** clip-on, optional.
6. **Speaker:** sealed, published [r2].

## 10. Family reuse (job 28)
- **Unchanged:** the keyboard tray (bed, blocks, scale), the spine construction, the strap, the thumbscrews.
- **Per instrument:** the module tray's depth (it equals the module's height) and its pockets. A module deeper than ≈ 135 needs a deeper box; both trays grow together, so the box still closes square.

## 11. Coverage (kit jobs)
| Job | Supported? | Where |
|---|---|---|
| 3 one kit, backpack | **yes; T5 at risk** | §1, §9 |
| 3 by the ends; packs empty; cable place | yes | §2, §1 |
| 20 bench and lap | yes (lap flat with one trial; standing on a table) | §3 |
| 23 share | yes | §4 |
| 24 one point of view | yes: a clamshell box owns the outline | §1 |
| 25 family | yes: bookbinding is new to the family, but walnut and brass carry over | §8, §10 |
| 26 making steps | yes, one trial named | §8 |
| 27 swap | yes, any socket position | §2, §4 |
| 28 one system | yes | §10 |
| 30 module paper-length | yes (module §2) | — |

**Unsupported jobs: none. At risk:** T5; the stop-at-flat spine until tried.
