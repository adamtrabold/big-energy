# RAIN: jobs coverage (systems, 2026-11-13, after round 2, director 9 pending R1)

Checked against `../../../jobs.md` **rev 5** (J1–J28), `how-it-works.md` rev 2, `../common-how-it-works.md` rev 2, `../../echo-clock.md` rev 1.1 and the v1.1 ONE SHEET it keeps inside. Geometry: `../branch_check.py`, re-run for this check: TOTAL fails 0; legend / tick / control collisions 0 (current `rb.rain()`).

**R1** (the decay finishing at the panel edge) changes only the ring field, not controls, legends or parts. It affects no job below except as noted under J20.

✓ supported · ◐ supported, with a stated weakness · ✗ not supported · ⏸ deferred by the owner · — retired.

| Job | Status | Where / how |
|---|---|---|
| J1 25 keys, travel, silent, velocity | ✓ | Choc V2 silent + Hall velocity under grey **peg stepping stones** centred on the stems; 14 mm felt washers in 1 mm counterbores (width stays 276) [CHECK]; whites y 14, sharps y 36.5 |
| J2 Bend + MOD | ✓ | PLAY row unchanged: stick in its gate disc, MOD beside it |
| J3 Shape the sound live | ✓ | Every v1.1 control in place (branch rule); PLAY row nearest the keys |
| J4 Read the patch; keep one on paper | ◐ | Panel is the state; legends on smooth lily pads, 0 collisions [CHECK]. Paper is still a separate card |
| J5 Hear it | ◐ | Bottom-firing speaker (240, 113), as v1.1: muffled on a lap; jacks rear |
| J6 Carry; survive a bag | ⏸ | Carry ✓ (276 × 180, deck z 24). Bag survival is the owner's deferred case topic. **New exposure:** pegs stand 6.5 proud, so side loads in a bag are untested (stated in how-it-works §2) |
| J7 Power, charge, know it, no accidental on | ✓ | As v1.1 ONE SHEET: internal LiPo, rear USB-C, recessed switch, hooded status light |
| J8 MIDI; know a knob isn't in control | ✓ | Rear wall; MIDI dots; not-in-control light by CUTOFF |
| J9 Patch | ✓ | Rear wall, away from the keys and the stick |
| J10 Tune; know the state | ✓ | Autotune; status light |
| J11 Build himself, low cost | ◐ | One shell, modelled ring geometry (OpenSCAD), bought pegs and felt. **No grooves to hide the print split**, so it needs a one-piece print on a 350 bed (UNVERIFIED at Vector Space) or a Voronoi-seam lap joint. The ring coupon is a pre-build check |
| J12 One clear idea, principles | ✓ | "Everything that breaks the surface ripples": finish, section map, legend pads and keys from one rule (director 9) |
| J13 Hand marks where meant | ✓ | Optional; every exact mark is machine-made in the one swap |
| J14 Service | ✓ | As v1.1: back panel off (8 screws): battery, speaker, board underside. A peg pulls out from above |
| J15 Table, lap | ◐ | Table ✓; lap ✓ but the speaker is muffled |
| J16 Find controls without looking | ✓ | Better than v1.1: rings around every control and smooth still lanes between sections can be felt; pegs are tall and round; CUTOFF is the big (mustard) knob |
| J17 | — | retired |
| J18 Keep it out (optional) | ◐ | Not taken (how-it-works §5 says so). A keyhole slot in the back panel, as v1.1, would cost nothing. Optional job: not a blocker |
| J19 Echo + reverb while playing | ✓ | Full 8 FX unchanged; tempo by TAP or clock (J23–J27) |
| **J20** One point of view; want to play it | ✓ | One rule decides finish, map, type and keys; calm at arm's length (director 9). **Conditional on R1** (edge as still water) |
| **J21** Keys with character | ✓ | Peg stepping stones (HUSH's pegs he loves), two stone greys |
| **J22** Park | ◐ | (a) **carry ◐**: in a bag, pegs exposed (J6). (b) **sit ✓**: flat on a lap, bench or grass. (c) **sun ◐**: hooded status light and lily-pad legends; midday legibility UNVERIFIED. (d) **hear ◐**: speaker fires down into grass, weak outdoors (UNVERIFIED). (e) **battery ◐**: ONE SHEET's pack as v1.1; session length is an open owner question. (f) **survive ✓/◐**: PETG in sun; drop and grass untested. (g) **share ✓**: the panel is open to a friend beside you |
| **J23** Echo follows MIDI clock | ✓ | Firmware (`echo-clock.md`), USB + TRS |
| **J24** Sync on/off, and see which | ✓ | FREE / SYNC toggle (128.0, 132.7), one more rippling stone; "FREE" / "SYNC" beside it [CHECK] |
| **J25** Division in SYNC, free time in FREE | ✓ | TIME's two printed scales over ±135° + firmware clamp |
| **J26** No jumps or clicks | ✓ | Firmware: glide / crossfade, hold on loss, tails on STOP. Hardware-unverified until the spike |
| **J27** Tempo with no clock, and see it | ✓ | TAP; status light flashes the tempo ×4 |
| **J28** Choose ONE SHEET or FOLD late | ✓ | ONE SHEET internals unchanged. **Stated:** pegs move strip C to the peg layout; the main board is unchanged (eng to confirm the board line, E-L9) |

## Verdict
**Unsupported jobs: none. RAIN passes, conditional on R1** (it only touches J20's look).

**Weak spots, named:**
- J5 / J15 / J22d: the bottom speaker outdoors and on a lap.
- J6: bag, owner-deferred, now with exposed pegs.
- J11: one-piece print or seam joint.
- J22c / e: sun and battery, owner question and test.
- J18: not taken.
