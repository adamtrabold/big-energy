# CHAMBER: jobs coverage (systems, 2026-11-13, after round 2, director 9)

Checked against `../../../jobs.md` **rev 5** (J1–J28), `how-it-works.md` rev 2, `../common-how-it-works.md` rev 2, `../../echo-clock.md` rev 1.1 and the v1.1 FOLD-105 it keeps inside (`versions/v1.1/fold/how-it-works.md` rev 5.7). Geometry: `../branch_check.py`, re-run for this check: TOTAL fails 0; legend / tick / control collisions 0 (Kalam).

✓ supported · ◐ supported, with a stated weakness · ✗ not supported · ⏸ deferred by the owner · — retired.

| Job | Status | Where / how |
|---|---|---|
| J1 25 keys, travel, silent, velocity | ✓ | Choc V2 silent + Hall velocity (unchanged), under reverse **pegs** (walnut naturals, maple sharps) centred on the stems. 14 mm felt washers are the silent bottom stop. Edge A: naturals y 13.5, sharps y 36 (HUSH geometry). The fallback colouring is drawn and geometry-identical |
| J2 Bend (one axis, springs back) + MOD stays put | ✓ | Base PLAY row unchanged: stick (25, 68), MOD (47, 68) |
| J3 Shape the sound live | ✓ | Every v1.1 control in place (branch rule): PLAY row in the base behind the keys, VOICE on the lid; reach stick → CUTOFF unchanged |
| J4 Read the patch; keep one on paper | ◐ | Both plates are the state; legends 0 collisions [CHECK]. Paper is still a separate card (inferred job) |
| J5 Hear it (table, lap; phones/line) | ✓ | Lid speaker in the band fires at the player open and standing; phones/line on the lid's far wall |
| J6 Carry; survive a bag | ✓ | Closed clamshell ≈ 286 × 108 × **52.7**; pegs 2.0 clear under the lid [CHECK]. **The hinge-side slot is now closed by the bookcloth/TPU spine** (rev 2 §R2.1); v1.1 had it open. Spine flex life UNVERIFIED (pre-build) |
| J7 Power, charge, know it, no accidental on | ✓ | Internal slim pack (FOLD-105, ≈ 11 Wh), rear USB-C on the base's right end, recessed power switch on the lid's far wall, status light (hooded) |
| J8 MIDI; know a knob isn't in control | ✓ | USB + TRS IN/OUT on the base's right end; engraved MIDI dots; not-in-control light by CUTOFF (unchanged) |
| J9 Patch | ✓ | CV/gate/EXT on the lid's far wall, away from the keys and the stick |
| J10 Tune; know the state | ✓ | Autotune; status light (hooded) |
| J11 Build himself, low cost | ◐ | Bought walnut plugs ≈ $0.32 each (director; shank fit UNVERIFIED, one sample), spine ≈ $2–5, façade as printed relief first. The one-piece blocks still want a big printer or v1.1's lap joint. Pre-build: relief/fill on wood-fill PETG |
| J12 One clear idea, principles | ✓ | "Closed an organ case, open a console": the pipes come from the keyboard's own 2^(−n/12); the order of use is the concept (director 9) |
| J13 Hand marks where meant | ✓ | Blank name lozenge on the lid axis (d 94.6) for his mark; everything exact is machine-marked |
| J14 Service | ✓ | As v1.1: back screws → push the pickguard out. **The push-outs are the two pipe mouths** (Ø 4 at (108 / 178, d 28.3)), landing on the bare board bridges [CHECK §8b]. A peg pulls out by hand; a switch is desoldered as before |
| J15 Table, lap | ✓ | Open flat on a table or lap; standing at 120° on the v1.1 stays (tip ≈ 6.8 N) |
| J16 Find controls without looking | ✓ | Pegs are tall and round (naturals and sharps on two rows); PLAY row alone on the base; CUTOFF is the big knob |
| J17 | — | retired |
| J18 Keep it out (optional) | ✓ | Closed, it stands on its end with the façade out (v1.1: "closed, on its left end") |
| J19 Echo + reverb while playing | ✓ | Full 8 FX controls unchanged; tempo by TAP or clock (J23–J27) |
| **J20** One point of view; want to play it | ✓ | One sentence decides form (case + console), material (walnut, brass line work, cloth spine), graphics (pipes from the scale, RANGE in feet), making and feel (pegs). Director 9 |
| **J21** Keys with character | ✓ | Reverse peg keys; fallback drawn (owner question 1) |
| **J22** Park | ◐ | (a) **carry ✓**: a closed bar, nothing proud. (b) **sit ✓/◐**: open on a lap or bench ✓; standing on grass relies on the stays' rubber tips on soft turf (UNVERIFIED). (c) **sun ◐**: hooded status light, lid tilted to catch light; legibility in midday sun UNVERIFIED. (d) **hear ◐**: speaker faces the player; outdoor level UNVERIFIED. (e) **battery ◐**: ≈ 1.9–3.9 h [CALC]; session length is an open owner question. (f) **survive ✓/◐**: closed it self-protects, spine shut; PETG / wood-fill PETG in sun; drop untested. (g) **share ✓**: standing, the façade faces the friend |
| **J23** Echo follows MIDI clock (USB / TRS) | ✓ | Firmware (`echo-clock.md`), both transports parsed (eng §5.4) |
| **J24** Sync on/off, and see which | ✓ | FREE / SYNC toggle at lid (133, d 70.6), "free" / "sync" beside it; label- and tick-checked [CHECK] |
| **J25** Division in SYNC, free time in FREE | ✓ | TIME's two printed scales over ±135° (firmware clamps the last 15°: owner question 6) |
| **J26** No jumps or clicks | ✓ | Firmware: glide (TAPE/BBD), crossfade (CLEAN/PING-PONG), hold the tempo on loss, tails on STOP. Hardware-unverified until the spike |
| **J27** Tempo with no clock, and see it | ✓ | TAP; status light flashes the tempo ×4 |
| **J28** Choose ONE SHEET or FOLD late | ✓ | FOLD-105 internals unchanged (boards, rows, Daisy, mux). Outside-only changes: lid walls +2.6 and hinge axis +1.3, spine, façade, pegs. **Stated:** pegs move strip C (the key board) to HUSH's peg layout; the main boards don't change |

## Verdict
**Unsupported jobs: none. CHAMBER passes.**

**Weak spots, named:**
- J22's park parts: sun, outdoor level, battery length, the stays on soft grass. Owner questions and pre-build tests, not design gaps.
- J11: plug shank fit, relief fill, big-printer blocks.
- J4: paper card.

**Pre-build checks that touch jobs:**
- spine flex life (J6);
- the ribbon loop sharing the seam gap with the spine (J6, J14);
- strip C vs the base board line with pegs (J1, eng).
