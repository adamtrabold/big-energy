# YOKE: an attachment-point answer (visual sketch, not yet a concept)

Status: **sketch, 2026-11-22**, product designer (visual focus). Prompted by the owner's correction, relayed by the coordinator (verbatim): *"The carry should fit a portable MIDI controller but the case does not need to surround it just have an attachment point. I'm just saying don't assume not making a rule"*. It's **not a rule**: it removes the assumption that the carry encloses or wraps the keyboard, which all three kits made. **The director decides whether YOKE becomes a concept.** Systems hasn't seen it; every number here is visual's [calc] or [est].

**Picture:** `yoke-A-carry-and-play.png` (source `../_src/r3.py`, `python3 r3.py yoke`): play plan, carry plan (X-ray, the module dashed), carry end view with the stack, end views against SPINE and FALLBOARD, one arm, and a comparison table.

## 1. The idea
**The module is the carry; the attachment points are the ones it already has.** Every family module has two ¼"-20 inserts underneath, 160 mm apart (S4). YOKE adds **two printed arms**, one on each insert under its thumbscrew. Each arm carries a **swivel cup** that slides along a slot and holds one **end** of the keyboard.
- **Carry:** the arms swing out sideways; the keyboard hangs **keys-up under the module**, held by its two ends, ≥ 6 mm of air between the keys and the arms/module. Nothing touches a key; the module's flat underside is the keys' lid.
- **Play:** loosen the thumbscrews, swing both arms forward-and-out to their detent, slide the cups, and the keyboard sits **in front of the module, keys still up**, 15 mm from the host port. One rigid instrument on a bench or a lap. The keyboard never flips.
- **Name:** a stage light hangs in a **yoke** that holds the fixture by its two ends and lets it swing (this turn's draw: stage lighting).

## 2. How it looks
- **Two black PETG arms**, ≈ (reach + 14) × 22, 4 mm plate rising to a 14 mm cup boss, mirror pair; the pivot disc doubles as the module's foot. A black, foam-lined cup with a lip over the keyboard's end cap and a 15 mm notch for an end socket.
- **Nothing else.** In carry, from above, you see floss's cream deck, and below it the keyboard's two ends in black cups: a module with a keyboard slung under it. In play, the arms are hidden under the module and keyboard except two short black wedges and the cups at the keyboard's ends.
- Same story as the family: black house, the cream stage, the cups as the only new parts.

## 3. Numbers [calc/est]
| | YOKE |
|---|---|
| Reach from pivot to cup | 89 (nanoKEY2 carry) to 165 (Xkey play): one 95 mm slot covers 325–388 keyboards both ways |
| Carry stack | cup floor 3 + keyboard 16 + air 6 + arm plate 4 + module 35 = **≈ 64** (option B: 71) |
| Carried size | **396 × 135 × 64** with an Xkey ≈ 3.4 L; ≈ 333 × 105 × 59 with a nanoKEY2 |
| Carry parts | **≈ 0.08–0.12 kg** [est: 2 arms + 2 cups in PETG + foam] |
| Kit + Xkey | ≈ module 0.67–0.93 + 0.1 + keyboard ≈ 0.6 + cable ≈ 1.4–1.7 kg [est] |
| Makes | 4 small prints, all on a 220 bed; two bought ¼"-20 thumbscrews (the module's own) and two pins |

## 4. How it compares
| | YOKE | FALLBOARD | SPINE | CLOTH |
|---|---|---|---|---|
| Carry parts | ≈ 0.08–0.12 | 0.47–0.60 | 0.42–0.52 | 0.23–0.36 |
| Closed (Xkey) | 396 × 135 × 64 | 412 × 265 × 42 | 412 × 148 × 59 | ≈ 400 × 150 × 65, soft |
| Keys protected by | the module, 6 mm above | lid | module tray | quilted sleeve |
| Module panel protected by | its own rim only | lid | keyboard tray | sleeve |
| Cable, adapter, charger | cable stays plugged; adapter on a clip on one arm (PROPOSAL); **charger loose in the bag** | pockets | bays | pocket |
| Bench | rigid pair, no stand | lid as stand and shade | flat | framed on the cloth |
| Lap | **one rigid piece** | one board | flat, stopped | two objects |
| Ground | sits on the grass as is | board | flat box | the mat |
| Family reuse | **any module with S4**, whatever its size | bed, blocks, lid | trays, spine | cloth, outline |

**Where it's strongest:** weight (the lightest by 0.15–0.5 kg), simplicity (4 prints), and the family argument: it attaches to the S4 interface every module already has, so Big Energy and port-a-poly get it free whatever their size. It's also the only answer whose carry pose *is* nearly its play pose.

**Where it's weakest (said plainly):**
1. **Exposure:** the keyboard's front and back edges and the module's panel face the bag. The rim keeps things off the knobs, but nothing stops a book pressing a knob sideways.
2. **No home for the charger**, and the adapter needs a clip; job 3's "one place for the cable" is met only by the cable staying plugged.
3. **"Every area has one job"** is trivially met (there is no area), but the director's rule was written for enclosing kits.
4. **Lap rigidity** rests on two thumbscrews and the arms' stiffness under a keypress (ENG); on a bench or the grass it's irrelevant.
5. **Chunky minis:** cups up to 49 tall would be needed; not drawn.
6. **Job 3 "without damage"** is weaker than in any enclosing kit; a padded sleeve would fix it but brings back a "case".

## 5. Open questions
1. **Director:** does YOKE become a concept, replace one, or stay a sketch? (My reading: it beats SPINE on weight and family reuse and loses on protection; it could also ride with CLOTH, wrapped.)
2. **Systems:** the cup's swivel and slot as a mechanism; detents; whether the keyboard's end caps take a cup's grip on every slim model (end shapes unpublished: UNVERIFIED).
3. **Eng:** arm stiffness at 4 mm PETG with a 165 mm reach; thumbscrew torque holding the play angle.
4. **Owner:** is an exposed panel and a loose charger an acceptable price for ≈ 0.1 kg of carry?
