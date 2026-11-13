# DIPTYCH: how it works (systems)

Seed: **FOLD-105** (v1.1). Kind: a field instrument. Point of view (director): **a pocket instrument for reading the day outdoors.** It opens, stands on its cords, and its TIME dial tells time two ways. Emotion: wonder. Flat keys (v1.1). Read with `../common-how-it-works.md`, `versions/v1.1/fold/how-it-works.md` (rev 5.7) and `design/jobs.md` rev 5.

**Rev 1, 2026-11-13, concept turn 1 (systems first).** Numbers marked [CHECK] come from `../branch_check.py` §5.

## 1. Headline finding: the cords can set the angle, but they can't stop it tipping [CHECK]
- **The model:** v1.1 weights (base 0.40, lid 0.375 kg, ESTIMATE); combined CG y 97; hinge axis y 109, z 25. The push is normal to the panel at a back-row knob tip.
- **The model checks out against v1.1:** with the brass stays (tips at y 167) it gives **6.9 N** to tip; v1.1 recorded 6.8.
- **Cords alone: 0.8 N to tip.** A cord between lid and base holds the hinge angle, but it adds no ground contact. The whole instrument still pivots on the base's rear edge (y 108), with its CG only 11 mm in front of it. Turning a knob pushes ≈ 1–3 N, so **it would fall over backwards while you play.** A real diptych dial never had a knob turned on it.
- **≥ 5 N needs ground contact at y ≥ 153: feet ≥ 45 mm behind the base.**

**Proposal: cords + base feet.**
- **Two brass feet** (the v1.1 stay part: 3 × 8 brass flat bar) pivot out of grooves **in the base underside**, near the end faces, with rubber tips at **y 167** (59 mm behind the base, as v1.1) → **6.9 N**. A 50 mm reach gives 5.7 N.
- Stowed, they're flush in the underside.
- **The cords set the 120° angle; the feet stop the tip.** That's one more part than v1.1, where the stays did both, so it's a cost to weigh. The honest alternative: keep v1.1's stays and drop the cords, which removes DIPTYCH's first principle. **Director's call.**
- **Bonus:** no stay grooves in the lid end faces, so v1.1's open must-fix (the stay groove vs the lid-wall jacks) disappears.

## 2. Cord geometry: the latitude (37.4°, Lynchburg) [CHECK]
The cord runs on each end face, from the lid end face to the base end face (anchor z ≈ 9), at 37.4° to the base.

| Lid attachment (along the lid) | Base anchor y | Cord | Tension per cord (lid weight + 5 N push) | At the PLAY row (y 68) |
|---|---|---|---|---|
| s 100 (director's, top corner) | 27.8 | 167 mm | ≈ 8 N | **24 mm above the base top**: where the left hand rests by the stick (x 25) and the right by TAP (x 261). Snag risk, high |
| **s 60 (pick)** | **53.2** | **110 mm** | **≈ 13 N** | **≈ 5 mm above the base top**, at the end face, 25 mm outboard of the stick / TAP axes |
| s 40 | 65.8 | 82 mm | ≈ 20 N | through the base top: no |

**Pick s 60:**
- The latitude angle holds (37.4°).
- The cord stays low past the hands.
- The base anchor at y 53 is 14 mm clear of MIDI IN (y 70) on the right end face.
- The lid end faces carry no I/O.
- **Hand clearance is still UNVERIFIED.** The left hand's heel may rest on the cord. Prove it with a cardboard mock and a real hand, as part of the director's (a).

**Hardware (proposal):**
- 2 mm pre-stretched polyester (or Dyneema) braid.
- Flush countersunk brass eyes on the lid end face (d 60) and on the base end face (y 53).
- The cord is fixed at the lid; its free end has a small brass snap that clips to the base eye.
- 13 N per cord is far under any 2 mm braid's break load (ESTIMATE). **Creep would drift the angle**: pre-stretched line, UNVERIFIED over months.
- The eyes go into brass threaded inserts in PETG.

**Stowage:**
- Closed, the attachment points sit ≈ 25 mm apart [CALC, rough], so ≈ 85 mm of each cord is slack.
- Unclip it and lay it in a **2 mm groove along the closed bar's end-face seam** (base / lid meeting line, 108 mm long ≥ 85). A flush pin holds the snap.
- **Maker check, UNVERIFIED.**

**It's a hidden fact, not a sundial** (director). No working dial is claimed.

## 3. TIME's two scales are the hero (J24, J25)
- **FREE / SYNC at lid (133, d 70.6)**, a black FOLD toggle, "free" / "sync" beside it (common §2).
- **TIME's dial, printed over ±135°:**
  - inner ring ms (r + 0.9 … 1.9);
  - outer ring 9 divisions (r + 2.4 … 3.6);
  - firmware clamps the last 15° at each end;
  - TIME's legend sits behind the knob (d ≈ 96.9), 1.35 behind the outer ring [CHECK].
  - Number labels and fine graduations: the visual designer's. Space outside r + 3.6 is tight (ECHO TYPE's fan names sit ≈ 5–6 mm to the left; not computed per label here). **To prove: the 1:1 crop (director's (b)).**
- **"Graduations everywhere":** fine scales on every knob are allowed by the v1.1 tick radii (r + 0.9 … 1.9). **Two fills (red + black) mean two filament swaps**, not one (v1.1 has one). That's a print-time cost, not $0 in time.

## 4. States
| State | What it is | Systems notes |
|---|---|---|
| **Closed** | the two leaves shut; ≈ 286 × 108 × 50.1 (v1.1) | cords in the end-seam grooves; feet flush in the underside |
| **Carried** | a bar, in a pocket of a bag | nothing proud: the snaps sit on their flush pins |
| **Flat (180°)** | on the table | cords unclipped and stowed; feet stowed; lid back on its feet |
| **Standing (120°)** | open past 120°, clip both cords, swing the feet out, set it down | the cords hold 120°, the feet stop tipping (6.9 N). Order: **feet first, then cords** (with the cords on and the feet in, a knob turn tips it) |
| **Outdoors** | park, bench | slim pack ≈ 1.9–3.9 h [CALC]; status hood (common §3); the lid speaker faces you; the cords at the end faces sit in your friend's sightline at the bench (they read as the instrument's "strings": visual's job) |

**The order hazard:** clip the cords with the feet still stowed, and the instrument stands but tips at 0.8 N. **Mitigation (proposal):** the cord snaps clip onto the base eyes only through a slot that the deployed foot uncovers. Feet out, then cords: an interlock with no extra part, UNVERIFIED as a mechanism.

## 5. Can't verify here
Hand vs cord (mock) · cord creep · feet pivot strength in the PETG base (brass insert) · the end-seam stowage groove · real weights (v1.1 ESTIMATEs) · the interlock slot · the TIME dial's legibility at 1:1.
