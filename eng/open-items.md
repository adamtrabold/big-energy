# Engineering open items (orchestrator log)
- [ ] Fix four §7 verification targets the golden model itself fails (from reference sim run 2026-11-12): tracking ±1 cent over full range (golden: ±2.35c over 7.5 oct, +11c @11k, +20c @16k); "-24 dB/oct measured 1–3 oct above cutoff" (not achievable even by ideal 4-pole there); self-osc onset at 20 Hz (golden never self-oscillates below ~89 Hz); DECAY-off release <10 ms (golden 44 ms). Re-derive targets from golden + MC spread.
- [ ] Reference harness gaps: VCA alone, mixer overdrive, noise, temperature sweeps, Monte Carlo; calibrate_vco() needs firmware table fit.
- [ ] Q6: Fig. 9-11 R2 = 82K variant plays 5.7 dB louder — confirm which value to capture.
- [ ] Saw ramp in model is near-straight; users report a curved ramp on this board revision — check whether it's model or reality before using saw shape as an A/B metric.
- [ ] Verify unchecked datasheet values in power chain (DCWN06A-12 ripple, Pololu 12V boost current curve).
- [ ] REPORT.md for reference harness was not written (subagent file-write restriction) — orchestrator to write from metrics.json.
