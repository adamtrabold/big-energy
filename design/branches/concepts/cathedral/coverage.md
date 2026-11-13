# CATHEDRAL: jobs coverage (systems, 2026-11-13, after steer 2, director 9)

Checked against `../../../jobs.md` **rev 5** (J1–J28), `how-it-works.md` §1–16 (current), the look doc rev 4+, and the decisions in `../../../owner.md` up to 16:52.
- **Geometry:** `layout_check.py` 0 violations (layout, closing, legends with the visual designer's rules, FX row centred).
- **Labels:** `branch_check` §7 on `rb.Nave` with real Kalam: 0 collisions.
- **Route assumed:** R-LOW (≈ 55.2 closed); R-TALL (≈ 59.7) changes no job.

✓ supported · ◐ supported, with a stated weakness · ✗ not supported · ⏸ deferred by the owner · — retired.

| Job | Status | Where / how |
|---|---|---|
| J1 25 keys, travel, silent, velocity | ✓ | Choc V2 silent + Hall velocity. Heads on the printed carrier (§10): brass naturals + black-plated brass sharps (same mass → one velocity calibration, §16.5). Bottom stop: O-ring / felt at ≈ 2.5 of 2.8. Deck-hole clearance ≥ 1 mm per side for the floating aftertouch strip (architecture open item 4) |
| J2 Bend (one axis, springs back) + MOD stays put | ◐ | stick at base x 25; MOD at 47. **R-LOW seats the stick 3.6 mm lower** (cap top at plate + 9.0). Thumb grip at that height is UNVERIFIED (try one); R-TALL keeps today's stick |
| J3 Shape the sound live | ✓ | every control present. PLAY row: pitch \| filter (CUTOFF on the axis) \| MOD MIX, DRIFT, TAP. The VOICE rows are evenly spaced; the mixer is symmetric round the speaker opening |
| J4 Read the patch; keep one on paper | ◐ | plates are the state; legends 0 collisions [CHECK]; paper is a separate card (inferred job) |
| J5 Hear it (table, lap; phones / line) | ✓ | Ø 46 opening concentric with the 50 mm driver, ≈ 73–83 % of Sd open, gasket, sealed stuffed back box (§16.4). It fires at the player, open or standing. **Stereo phones + stereo line out** (decided) |
| J6 Carry; survive a bag | ◐ | closed ≈ 286 × 108 × 55.2 (R-LOW); heads and low knobs clear by 2.0 [CHECK]. **No spine (owner), so the hinge-side slot (≈ 24 × 266 at R-LOW) is open** again, as in v1.1: grit, and V1 tops visible inside. Answer pending: S0 open / S1 finished dark inside (director's pick) / sleeve |
| J7 Power, charge, know it, no accidental on | ✓ | internal pack, **moved to the base rear strip** (§16.2); one rear USB-C; recessed switch; status light (hooded); battery level at boot and on a TAP hold (gestures doc) |
| J8 MIDI; know a knob isn't in control | ✓ | USB + TRS in / out; engraved MIDI dots; not-in-control light at base (131, 81). DAW behaviour in `docs/features/midi.md` (proposed items open with the owner) |
| J9 Patch | ✓ | CV / gate / EXT and stereo PHONES / LINE on the lid's far wall, away from the keys and the stick. Line-out jack count (one TRS vs L / MONO + R) is open with the owner (O2) |
| J10 Tune; know the state | ✓ | autotune (hold TAP at power-on for a full sweep); status light |
| J11 Build himself, low cost, no machining | ◐ | printed blocks, bought parts, no machining. R-LOW depends on snap-in pots or a counterbored plate and on a bought-to-length shaft (UNVERIFIED). Cast-brass heads and stays come from a print service (quote pending). Plug shank fit and the key-head test (T1 / T2) are pending. Board changes for eng (below) |
| J12 One clear idea, principles | ✓ | "nave and rose": evenly spaced rows, one round opening on the axis above CUTOFF; organ case outside (director 9) |
| J13 Hand marks where meant | ✓ | the façade's pipe lines are his to draw (owner); his maker's mark goes in the name lozenge; everything exact is machine-marked |
| J14 Service | ✓ | back screws → push the pickguard out (the pipe-mouth push-outs on the bare board bridges, §R2.2 — **eng to re-check against the re-flowed lid board**). Battery now under the base's back. A head pulls off its carrier |
| J15 Table, lap | ✓ | open flat or standing at 120° on the stays. Tip threshold rises to ≈ 8.4 N with the battery in the base [CALC] |
| J16 Find controls without looking | ✓ | tall round brass heads; CUTOFF the one big knob on the axis; low gold knobs on the played row vs black knobs on the lid ("what the hands play is brass-toned") |
| J17 | — | retired |
| J18 Keep it out (optional) | ✓ | closed, it stands on its end with the façade out |
| J19 Echo + reverb while playing | ✓ | all effect controls together on the lid's back row (owner's ask), re-centred; FREE / SYNC and TAP; stereo returns. **Trade, stated:** effect amounts are on the lid's top row, further from the hands than v1.1's front row |
| **J20** One point of view; want to play it | ✓ | CATHEDRAL, director 9 |
| **J21** Keys with character | ✓ | brass keys (owner: "more brass than black"); lead A, alternate C |
| **J22** Park | ◐ | (a) carry ✓ (a closed bar, nothing proud). (b) sit ✓ / ◐ (stays on soft turf UNVERIFIED). (c) sun ◐ (hooded light; UNVERIFIED). (d) hear ✓ / ◐ (opening sized for the driver; still a 50 mm driver: modest outdoors, honest +3–6 dB at 1–5 kHz). (e) battery ◐ (≈ 1.9–3.9 h on the slim pack; session length is an open owner question). (f) survive ✓ / ◐ (closed self-protects except the back slot; PETG in sun). (g) share ✓ (façade to the friend when standing) |
| **J23** Echo follows MIDI clock | ✓ | `echo-clock.md`, USB + TRS |
| **J24** Sync on / off, and see which | ✓ | FREE / SYNC at lid (77.5, d 69.7), "free" / "sync" beside it [CHECK] |
| **J25** Division in SYNC, free time in FREE | ✓ | TIME's two scales over ±135° + firmware clamp |
| **J26** No jumps or clicks | ✓ | firmware (glide / crossfade, hold on loss, tails on STOP); spike-verified later |
| **J27** Tempo with no clock, and see it | ✓ | TAP (base x 261) + status-light flashes |
| **J28** Choose ONE SHEET or FOLD late | ◐ | CATHEDRAL is the FOLD path. **Stated:** steer 2 changes boards beyond "outside only": a window in the base board for the cells, re-flowed lid pot and switch positions, the speaker back box. The shared spec changes (4th mux, 5th DAC, stereo output stage) apply to either concept. The owner allowed moving components (16:52) |

## Verdict
**Unsupported jobs: none. CATHEDRAL passes.**

**Weak spots, named:**
- **J6:** the open back slot (no spine); his answer on S0 / S1 / sleeve is pending.
- **J2:** the lowered stick's feel (R-LOW only).
- **J11:** snap-in pots or counterbore, shaft length, key-head tests.
- **J22:** park sun, outdoor level, battery length.
- **J28:** board changes.
- **J19 trade:** effect amounts are on the lid's top row.

**Before the owner sees it (checks that touch jobs):**
- the eng re-check of the pipe-mouth push-outs against the re-flowed lid board (J14);
- the base board window and ribbon header for the cells (J7, J28);
- one test stick at plate + 9.0 (J2).
