#!/usr/bin/env python3
"""A/B comparison of two harness result dirs (golden vs DUT) -> pass/fail table.

  python3 compare.py out/golden out/ours [--json out/ab_ours.json]

Thresholds are the provisional pass/fail limits defined in REPORT.md section 5. Each check
reports the measured difference, the limit and PASS/FAIL; a missing measurement is FAIL.
"""
import argparse, json, sys
from pathlib import Path
import numpy as np

LIM = {
    "track_cents": 1.0,          # DUT curve - golden curve, keyboard range, after each's own cal
    "track_hf_cents": 3.0,       # above the keyboard (to ~11 kHz)
    "harm_db": 1.0,              # per harmonic h1..h20 where golden is above -50 dB re h1
    "harm_db_low": 3.0,          # harmonics below -50 dB re h1
    "duty_abs": 0.02,
    "level_rel": 0.05,           # waveform p-p / rectangle levels
    "fc_cents": 25.0,            # filter -3 dB corner
    "slope_db": 1.0,             # dB/oct
    "mag_db": 0.5,               # |H| difference where golden within 40 dB of its peak, 10 Hz-20 kHz
    "onset_dial": 0.5,
    "lowosc_rel": 0.15,
    "time_rel": 0.15,            # contour times
    "overshoot_rel": 0.05,
    "peak_v": 0.1,
    "lsd_db": 2.0,               # voice log-spectral distance (provisional; set from golden MC spread)
    "env_db": 1.0,               # voice envelope RMS difference
    "osc_cents": 1.0,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("golden"); ap.add_argument("dut"); ap.add_argument("--json")
    a = ap.parse_args()
    G, D = Path(a.golden), Path(a.dut)
    g = json.loads((G / "metrics.json").read_text()); d = json.loads((D / "metrics.json").read_text())
    rows = []

    def chk(block, name, diff, lim):
        ok = diff is not None and np.isfinite(diff) and abs(diff) <= lim
        rows.append({"block": block, "check": name, "diff": None if diff is None else float(diff),
                     "limit": lim, "result": "PASS" if ok else "FAIL"})

    # ---- VCO tracking
    try:
        gp = {(p["range"], p["key"]): p["hz"] for p in g["vco_tracking"]["points"]}
        dp = {(p["range"], p["key"]): p["hz"] for p in d["vco_tracking"]["points"]}
        kb = [1200 * np.log2(dp[k] / gp[k]) for k in gp if k in dp and k[1] <= 42]
        hf = [1200 * np.log2(dp[k] / gp[k]) for k in gp if k in dp and k[1] > 42]
        chk("vco", "tracking max |dut-golden| keyboard range (cents)", max(np.abs(kb)) if kb else None, LIM["track_cents"])
        chk("vco", "tracking max |dut-golden| above keyboard (cents)", max(np.abs(hf)) if hf else None, LIM["track_hf_cents"])
    except KeyError:
        chk("vco", "tracking", None, 0)
    # ---- VCO waveforms
    for pitch, gv in g.get("vco_waves", {}).items():
        dv = d.get("vco_waves", {}).get(pitch, {})
        for w in ("square", "wide_m1v5", "narrow_m2v5"):
            gw, dw = gv.get(w, {}), dv.get(w, {})
            if "rect_duty_high" not in gw or "rect_duty_high" not in dw:
                chk("vco", f"{pitch} {w}", None, 0); continue
            chk("vco", f"{pitch} {w} duty", dw["rect_duty_high"] - gw["rect_duty_high"], LIM["duty_abs"])
            sw = gw["rect_hi_v"] - gw["rect_lo_v"]
            chk("vco", f"{pitch} {w} rect swing rel", (dw["rect_hi_v"] - dw["rect_lo_v"]) / sw - 1, LIM["level_rel"])
            waves = ["rect"] + (["saw", "tri"] if w == "square" else [])
            for wv in waves:
                gh, dh = np.array(gw[f"{wv}_harm_db"]), np.array(dw[f"{wv}_harm_db"])
                hi = gh > -50
                chk("vco", f"{pitch} {w} {wv} harmonics (>-50 dB) max dB", np.max(np.abs(dh - gh)[hi]), LIM["harm_db"])
                if (~hi).any():
                    chk("vco", f"{pitch} {w} {wv} harmonics (<-50 dB) max dB", np.max(np.abs(dh - gh)[~hi]), LIM["harm_db_low"])
            if w == "square":
                for k in ("saw_pp_v", "tri_pp_v"):
                    chk("vco", f"{pitch} {k} rel", dw[k] / gw[k] - 1, LIM["level_rel"])
    # ---- filter AC
    gc = np.load(G / "filter_ac_curves.npz") if (G / "filter_ac_curves.npz").exists() else {}
    dc = np.load(D / "filter_ac_curves.npz") if (D / "filter_ac_curves.npz").exists() else {}
    for c, gv in g.get("filter_ac", {}).items():
        dv = d.get("filter_ac", {}).get(c)
        if not dv:
            chk("vcf", f"cut {c}", None, 0); continue
        chk("vcf", f"cut {c} fc (cents)", 1200 * np.log2(dv["fc_minus3db_hz"] / gv["fc_minus3db_hz"]), LIM["fc_cents"])
        for sk in ("slope_db_per_oct_1to3oct_above_fc", "slope_db_per_oct_3to5oct_above_fc"):
            if gv.get(sk) is not None:
                chk("vcf", f"cut {c} {sk}", (dv.get(sk) or np.nan) - gv[sk], LIM["slope_db"])
        for e in gv["emphasis"]:
            if not gv["emphasis"][e].get("valid_small_signal"):
                continue   # small-signal AC beyond onset is not meaningful
            key = f"c{int(c):+d}_e{e}"
            if key in gc and key in dc:
                f, ga, da = gc[key][:, 0], gc[key][:, 1], np.interp(gc[key][:, 0], dc[key][:, 0], dc[key][:, 1])
                m = (f >= 10) & (f <= 20e3) & (ga >= ga.max() - 40)
                chk("vcf", f"cut {c} emph {e} |H| max dB", np.max(np.abs(da - ga)[m]), LIM["mag_db"])
            else:
                chk("vcf", f"cut {c} emph {e} |H|", None, 0)
    for k, gv in g.get("filter_selfosc", {}).items():
        dv = d.get("filter_selfosc", {}).get(k, {})
        if k == "lowest_selfosc_emph10":
            a_, b_ = gv.get("lowest_oscillating_freq_hz"), dv.get("lowest_oscillating_freq_hz")
            chk("vcf", "lowest self-osc freq rel", (b_ / a_ - 1) if (a_ and b_) else None, LIM["lowosc_rel"])
        elif gv.get("onset_dial") is None:
            ok = dv.get("onset_dial") is None
            rows.append({"block": "vcf", "check": f"onset {k}: golden does not oscillate; dut must not either",
                         "diff": None, "limit": None, "result": "PASS" if ok else "FAIL"})
        else:
            chk("vcf", f"self-osc onset {k} (dial)", (dv.get("onset_dial") or np.nan) - gv["onset_dial"], LIM["onset_dial"])
    # ---- contours
    for case, gv in g.get("contour", {}).items():
        dv = d.get("contour", {}).get(case, {})
        for ch in ("filter", "loudness"):
            gm, dm = gv.get(ch, {}), dv.get(ch, {})
            for k in ("trigger_delay_s", "attack_10_90_s", "decay_tau63_s", "release_90_10_s", "release_90_50_s"):
                if gm.get(k) and gm[k] > 2e-4:
                    chk("contour", f"{case} {ch} {k} rel", (dm.get(k) or np.nan) / gm[k] - 1, LIM["time_rel"])
            for k in ("peak_v", "sustain_v_before_release"):
                if k in gm:
                    chk("contour", f"{case} {ch} {k} (V)", dm.get(k, np.nan) - gm[k], LIM["peak_v"])
            k = "overshoot_ratio_peak_over_sustain10"
            if k in gm:
                chk("contour", f"{case} {ch} overshoot ratio rel", dm.get(k, np.nan) / gm[k] - 1, LIM["overshoot_rel"])
    # ---- voice
    for name, gv in g.get("voice", {}).items():
        dv = d.get("voice", {}).get(name, {})
        fg, fd = G / f"wav/voice_{name}_features.npz", D / f"wav/voice_{name}_features.npz"
        if not (fg.exists() and fd.exists()):
            chk("voice", f"{name}", None, 0); continue
        A, B = np.load(fg), np.load(fd)
        n = min(A["S"].shape[1], B["S"].shape[1])
        Sa, Sb = A["S"][:, :n], B["S"][:, :n]
        band = (A["f"] >= 20) & (A["f"] <= 16000)
        ref = Sa[band].max()
        la = 20 * np.log10(np.maximum(Sa[band], ref * 1e-4))   # floor at -80 dB re max
        lb = 20 * np.log10(np.maximum(Sb[band], ref * 1e-4))
        lsd = float(np.mean(np.sqrt(np.mean((la - lb) ** 2, axis=0))))
        chk("voice", f"{name} log-spectral distance (dB)", lsd, LIM["lsd_db"])
        m = min(len(A["env"]), len(B["env"]))
        ea, eb = A["env"][:m], B["env"][:m]
        on = ea > ea.max() * 0.01
        chk("voice", f"{name} envelope RMS diff (dB)",
            float(np.sqrt(np.mean((20 * np.log10(eb[on] + 1e-12) - 20 * np.log10(ea[on])) ** 2))), LIM["env_db"])
        if gv.get("osc_hz") and dv.get("osc_hz"):
            chk("voice", f"{name} pitch (cents)", 1200 * np.log2(dv["osc_hz"] / gv["osc_hz"]), LIM["osc_cents"])
    # ---- print
    nf = sum(r["result"] == "FAIL" for r in rows)
    w = max(len(r["check"]) for r in rows)
    for r in rows:
        dd = "   n/a" if r["diff"] is None else f"{r['diff']:+9.4f}"
        print(f"{r['result']:4}  {r['block']:7} {r['check']:<{w}}  {dd}  (limit {r['limit']})")
    print(f"\n{len(rows) - nf}/{len(rows)} PASS, {nf} FAIL")
    if a.json:
        Path(a.json).write_text(json.dumps({"golden": str(G), "dut": str(D), "limits": LIM, "rows": rows,
                                            "n_fail": nf}, indent=1))
    sys.exit(1 if nf else 0)


if __name__ == "__main__":
    main()
