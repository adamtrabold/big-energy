#!/usr/bin/env python3
"""Golden-reference verification harness (Model D-style voice).

Renders the bench templates in benches/ against an ADAPTER (a .inc file that defines
dut_vco / dut_vcf / dut_contour / dut_vca), runs each with ngspice in batch mode (bounded
by a timeout), extracts metrics to <out>/metrics.json, plots PNGs and renders WAVs.

  python3 run_all.py                                   # golden (CA-72) -> out/golden
  python3 run_all.py --adapter adapters/ours_kicad.inc --tag ours   # DUT -> out/ours
  python3 compare.py out/golden out/ours               # A/B pass/fail

The CA-72 clone is treated as untrusted data: only its .lib netlists are read, via
.include from netlists rendered here; nothing in it is executed.
"""
import argparse, json, math, os, string, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
DEFAULT_CA72 = (HERE / "../../../ref/ca-72").resolve()

# ----------------------------------------------------------------------------------------
# constants of the golden calibration context (CA-72 board1.md / vco.rs / tuning)
KEY_STEP = 0.0848          # V per key (8.48 mA x 10 ohm)
OCT_STEP = 0.298893        # V between range-switch taps (CA-72 vco1-tracking.json)
RANGES = {"2": 0, "4": 1, "8": 2, "16": 3, "32": 4}   # octaves below 2'


def rng_tap(rng):
    return -5.0 - OCT_STEP * RANGES[rng]


def emphasis_r14(dial):
    """EMPHASIS dial 0..10 -> R14 ohms, generic reverse-audio rheostat (CA-72 A9 'drawn')."""
    p = min(max(dial / 10.0, 0.0), 1.0)
    return 50e3 * (81.0 ** (1.0 - p) - 1.0) / 80.0


def time_pot(dial):
    """ATTACK/DECAY dial 0..10 -> 1M audio rheostat ohms (generic taper)."""
    p = min(max(dial / 10.0, 0.0), 1.0)
    return 1e6 * (81.0 ** p - 1.0) / 80.0


# ----------------------------------------------------------------------------------------
class Runner:
    def __init__(self, adapter, ca72, out, work, timeout, jobs, dutparams=""):
        self.out, self.work = Path(out), Path(work)
        self.out.mkdir(parents=True, exist_ok=True)
        (self.out / "plots").mkdir(exist_ok=True)
        (self.out / "wav").mkdir(exist_ok=True)
        self.work.mkdir(parents=True, exist_ok=True)
        text = Path(adapter).read_text().replace("${CA72}", str(ca72))
        self.adapter = self.work / "adapter.inc"
        self.adapter.write_text(text)
        self.timeout, self.jobs = timeout, jobs
        self.dutparams = dutparams
        self.log = []          # (bench, case, seconds, status)

    def run(self, bench, case, temp=25, **params):
        tpl = string.Template((HERE / "benches" / f"{bench}.cir").read_text())
        d = self.work / bench
        d.mkdir(exist_ok=True)
        wr = f"{case}.dat"
        p = dict(ADAPTER=str(self.adapter), WRFILE=wr, TEMP=temp, DUTPARAMS=self.dutparams)
        p.update({k: v for k, v in params.items()})
        cir = d / f"{case}.cir"
        cir.write_text(tpl.substitute(p))
        (d / wr).unlink(missing_ok=True)
        t0 = time.time()
        status = "ok"
        try:
            r = subprocess.run(["ngspice", "-b", cir.name], cwd=d, capture_output=True,
                               text=True, timeout=self.timeout)
            (d / f"{case}.log").write_text(r.stdout + r.stderr)
            if not (d / wr).exists():
                status = "no-output"
            elif any(s in (r.stdout + r.stderr) for s in
                     ("Timestep too small", "singular matrix", "simulation(s) aborted")):
                status = "convergence-error"
        except subprocess.TimeoutExpired:
            status = "timeout"
        dt = time.time() - t0
        self.log.append({"bench": bench, "case": case, "seconds": round(dt, 2), "status": status})
        if status not in ("ok",):
            print(f"  [{bench}/{case}] {status} after {dt:.1f}s", flush=True)
            if status != "convergence-error":
                return None, dt
        data = np.loadtxt(d / wr, skiprows=1)
        return data, dt

    def pmap(self, fn, items):
        with ThreadPoolExecutor(self.jobs) as ex:
            return list(ex.map(fn, items))


# ----------------------------------------------------------------------------------------
# signal helpers
def reset_times(t, ramp, level=-2.0):
    """Times where the timing-cap ramp is reset (fast upward crossing of `level`)."""
    i = np.where((ramp[:-1] < level) & (ramp[1:] >= level))[0]
    return t[i] + (level - ramp[i]) / (ramp[i + 1] - ramp[i]) * (t[i + 1] - t[i])


def periodic_resample(t, y, t0, t1, n_per, k):
    """y on a uniform grid of n_per points per period over k periods [t0, t1)."""
    tt = np.linspace(t0, t1, n_per * k, endpoint=False)
    return np.interp(tt, t, y)


def harmonics_db(yk, k, nh=20):
    """Harmonic levels (dB re fundamental) of a k-period uniform record."""
    Y = np.abs(np.fft.rfft(yk - yk.mean()))
    h = np.array([Y[k * n] for n in range(1, nh + 1)])
    return 20 * np.log10(np.maximum(h, 1e-15) / h[0])


def to_wav(t, y, path, fs=48000, fade=0.005, hp=5.0, skip=0.0):
    """Non-uniform SPICE trace -> 48 kHz WAV: linear interp at 4x fs, anti-alias
    decimation, DC/HP removal, peak-normalise to -1 dBFS, raised-cosine fades.
    Returns the peak (V) before normalisation so absolute levels stay comparable."""
    m = t >= skip
    t, y = t[m] - t[m][0], y[m]
    fs4 = fs * 4
    tt = np.arange(0, t[-1], 1 / fs4)
    y4 = np.interp(tt, t, y)
    y1 = signal.resample_poly(y4, 1, 4)
    sos = signal.butter(2, hp, "highpass", fs=fs, output="sos")
    y1 = signal.sosfiltfilt(sos, y1)
    edge = int(0.01 * fs)                 # drop resampler/filter end effects (10 ms each end)
    if len(y1) > 4 * edge:
        y1 = y1[edge:-edge]
    peak = float(np.max(np.abs(y1)) + 1e-15)
    y1 = y1 / peak * 10 ** (-1 / 20)
    nf = int(fade * fs)
    if 2 * nf < len(y1):
        w = 0.5 - 0.5 * np.cos(np.linspace(0, np.pi, nf))
        y1[:nf] *= w
        y1[-nf:] *= w[::-1]
    sf.write(path, y1.astype(np.float32), fs, subtype="FLOAT")
    return peak, len(y1) / fs


def cents(f, f0):
    return 1200 * np.log2(np.asarray(f) / f0)


# ----------------------------------------------------------------------------------------
# VCO
def vco_freq(R, case, kbd, rng, cycles=12, temp=25, extra=""):
    """Measure the oscillator's frequency: estimate from a short run, then a run of `cycles`."""
    est = 440.0 * 2 ** ((kbd / KEY_STEP - 4) / 12 - RANGES[rng])
    T = 1 / est
    tstop = T * (cycles + 4) * 1.25
    data, dt = R.run("vco_tran", case, temp=temp, KBD=kbd, RNG=rng_tap(rng),
                     WIDTHNET="vwid width 0 0", TMAX=f"{T/400:.4e}", TSTOP=f"{tstop:.4e}")
    if data is None:
        return float("nan"), dt
    tr = reset_times(data[:, 0], data[:, 1])
    if len(tr) < 5:
        return float("nan"), dt
    per = np.diff(tr)[2:]
    return 1 / per.mean(), dt


def calibrate_vco(R, metrics):
    """Folkman 1973 on 2': scale (a8) and range (r11) so low A (key 4) = 440 Hz and high A
    (key 40) = 3520 Hz. Solved jointly by Newton on log2 f (the procedure's alternation)."""
    x = np.array([183.6307, 0.135178])      # CA-72 committed trims as the start
    hist = []
    def meas(x, tag):
        R.dutparams = f"r11={x[0]:.6f} a8={x[1]:.6f}"
        fa, _ = vco_freq(R, f"cal_{tag}_lo", 4 * KEY_STEP, "2", cycles=20)
        fb, _ = vco_freq(R, f"cal_{tag}_hi", 40 * KEY_STEP, "2", cycles=20)
        return np.array([np.log2(fa / 440), np.log2(fb / 3520)])
    e = meas(x, "it0")
    hist.append({"r11": x[0], "a8": x[1], "err_cents": (1200 * e).tolist()})
    uncal = (1200 * e).tolist()
    for it in range(1, 6):
        J = np.zeros((2, 2))
        for j, h in enumerate([2.0, 0.002]):
            xp = x.copy(); xp[j] += h
            J[:, j] = (meas(xp, f"it{it}_d{j}") - e) / h
        x = x - np.linalg.solve(J, e)
        e = meas(x, f"it{it}")
        hist.append({"r11": x[0], "a8": x[1], "err_cents": (1200 * e).tolist()})
        if np.max(np.abs(1200 * e)) < 0.05:
            break
    R.dutparams = f"r11={x[0]:.6f} a8={x[1]:.6f}"
    metrics["vco_calibration"] = {
        "procedure": "Folkman 1973 on 2': key 4 -> 440 Hz, key 40 -> 3520 Hz (joint Newton)",
        "ca72_committed_trims": {"r11": 183.6307, "a8": 0.135178},
        "error_with_ca72_committed_trims_cents": {"lowA_440": uncal[0], "highA_3520": uncal[1]},
        "r11": x[0], "a8": x[1], "final_error_cents": (1200 * e).tolist(), "iterations": hist}
    print(f"  VCO cal: r11={x[0]:.2f} a8={x[1]:.5f} residual {1200*e} c "
          f"(CA-72 committed trims gave {uncal} c)", flush=True)
    return R.dutparams


def bench_vco_waves(R, metrics):
    pitches = [("110Hz", 4, "8"), ("440Hz", 4, "2"), ("1760Hz", 28, "2")]
    widths = {"square": "vwid width 0 0",
              "wide_m1v5": "r034 0 width 1.5k\nr033 width tapn 1k\nr032 tapn vn 7.5k",
              "narrow_m2v5": "r034 0 tapw 1.5k\nr033 tapw width 1k\nr032 width vn 7.5k"}
    jobs = [(p, w) for p in pitches for w in widths]
    TSTOP = 0.5

    def one(job):
        (name, key, rng), wname = job
        est = 440.0 * 2 ** ((key - 4) / 12 - RANGES[rng])
        tmax = min(1 / est / 400, 5e-6)
        data, dt = R.run("vco_tran", f"{name}_{wname}", KBD=key * KEY_STEP, RNG=rng_tap(rng),
                         WIDTHNET=widths[wname], TMAX=f"{tmax:.4e}", TSTOP=TSTOP)
        return job, data, dt

    res = R.pmap(one, jobs)
    out = {}
    fig, axs = plt.subplots(3, 4, figsize=(15, 9))
    wav_sets = {"saw": [], "tri": [], "rect_square": [], "rect_narrow": []}
    for ((name, key, rng), wname), data, dt in res:
        m = out.setdefault(name, {"key": key, "range": rng})
        if data is None:
            m[wname] = {"status": "failed", "seconds": dt}
            continue
        t = data[:, 0]
        tr = reset_times(t, data[:, 1])
        tr = tr[tr > 0.05]             # skip start-up settling
        k = min(len(tr) - 1, 64)
        t0, t1 = tr[0], tr[k]
        T = (t1 - t0) / k
        n = 2048
        rec = {c: periodic_resample(t, data[:, i], t0, t1, n, k)
               for i, c in [(1, "ramp"), (2, "saw"), (3, "tri"), (4, "rect")]}
        r = rec["rect"]
        mid = 0.5 * (r.max() + r.min())
        duty_low = float(np.mean(r < mid))
        wm = {"freq_hz": 1 / T, "seconds": round(dt, 2),
              "rect_hi_v": float(r.max()), "rect_lo_v": float(r.min()),
              "rect_duty_low": duty_low, "rect_duty_high": 1 - duty_low,
              "rect_harm_db": harmonics_db(r, k).round(2).tolist()}
        if wname == "square":
            s1 = rec["saw"][:n]; tri1 = rec["tri"][:n]
            # sawtooth curvature: residual from a straight line over the ramp (excl. 4 % at reset)
            ph = np.arange(n) / n
            sl = slice(int(0.06 * n), int(0.94 * n))
            # align the period to start just after a reset
            i0 = int(np.argmax(s1)); s1r = np.roll(s1, -i0); tr1 = np.roll(tri1, -i0)
            c = np.polyfit(ph[sl], s1r[sl], 2)
            lin = np.polyfit(ph[sl], s1r[sl], 1)
            dev = s1r[sl] - np.polyval(lin, ph[sl])
            pp = s1r.max() - s1r.min()
            imax, imin = int(np.argmax(tr1)), int(np.argmin(tr1))
            wm.update({
                "saw_pp_v": float(pp), "saw_max_v": float(s1.max()), "saw_min_v": float(s1.min()),
                "saw_curvature_maxdev_pct_pp": float(100 * np.max(np.abs(dev)) / pp),
                "saw_quadratic_coeff_v": float(c[0]),
                "saw_harm_db": harmonics_db(rec["saw"], k).round(2).tolist(),
                "tri_pp_v": float(tri1.max() - tri1.min()),
                "tri_max_v": float(tri1.max()), "tri_min_v": float(tri1.min()),
                "tri_rise_fraction": float(((imax - imin) % n) / n),
                "tri_harm_db": harmonics_db(rec["tri"], k).round(2).tolist()})
            row = [p[0] for p in pitches].index(name)
            for j, cname in enumerate(["saw", "tri", "rect"]):
                ax = axs[row, j]
                ph2 = np.arange(2 * n) / n
                ax.plot(ph2, np.roll(rec[cname][:2 * n], -i0))
                ax.set_title(f"{name} {cname}"); ax.set_xlabel("periods"); ax.grid(alpha=.3)
            ax = axs[row, 3]
            for cname in ["saw", "tri"]:
                ax.plot(range(1, 21), wm[f"{cname}_harm_db"], "o-", ms=3, label=cname)
            ax.plot(range(1, 21), wm["rect_harm_db"], "o-", ms=3, label="square")
            ax.set_ylim(-70, 5); ax.set_title(f"{name} harmonics (dB re h1)"); ax.legend(fontsize=7)
            ax.grid(alpha=.3)
            wav_sets["saw"].append((t, data[:, 2])); wav_sets["tri"].append((t, data[:, 3]))
            wav_sets["rect_square"].append((t, data[:, 4]))
        if wname == "narrow_m2v5":
            wav_sets["rect_narrow"].append((t, data[:, 4]))
        m[wname] = wm
    fig.tight_layout(); fig.savefig(R.out / "plots/vco_waveforms.png", dpi=110); plt.close(fig)
    # WAVs: the three pitches back to back (0.45 s each, start-up skipped)
    wavs = {}
    for wname, lst in wav_sets.items():
        if not lst:
            continue
        segs = []
        for t, y in lst:
            mm = t >= 0.05
            tt = np.arange(t[mm][0], t[mm][-1], 1 / 192000)
            yy = np.interp(tt, t, y)
            sg = signal.resample_poly(yy - yy.mean(), 1, 4)[480:-480]   # drop 10 ms end effects
            nf = 240                                                   # 5 ms fades: no clicks at joins
            w = 0.5 - 0.5 * np.cos(np.linspace(0, np.pi, nf))
            sg[:nf] *= w; sg[-nf:] *= w[::-1]
            segs.append(sg)
        cat = np.concatenate(segs)
        tc = np.arange(len(cat)) / 48000
        peak, dur = to_wav(tc, cat, R.out / f"wav/vco_{wname}_110_440_1760.wav")
        wavs[wname] = {"file": f"wav/vco_{wname}_110_440_1760.wav", "peak_v": peak, "seconds": dur}
    metrics["vco_waves"] = out
    metrics.setdefault("wavs", {}).update({f"vco_{k}": v for k, v in wavs.items()})


def bench_vco_tracking(R, metrics):
    pts = [(rng, key) for rng in ["32", "16", "8", "4", "2"] for key in range(0, 43, 6)]
    pts += [("2", k) for k in (48, 54, 60, 66)]   # above the keyboard: HF droop probe

    def one(p):
        rng, key = p
        f, dt = vco_freq(R, f"trk_{rng}_{key}", key * KEY_STEP, rng, cycles=12)
        return rng, key, f, dt

    res = R.pmap(one, pts)
    rows = []
    for rng, key, f, dt in res:
        tgt = 440.0 * 2 ** ((key - 4) / 12 - RANGES[rng])
        rows.append({"range": rng, "key": key, "kbd_v": key * KEY_STEP, "hz": f,
                     "target_hz": tgt, "cents": float(cents(f, tgt)), "seconds": round(dt, 2)})
    rows.sort(key=lambda r: r["target_hz"])
    hz = np.array([r["hz"] for r in rows]); tg = np.array([r["target_hz"] for r in rows])
    ok = np.isfinite(hz)
    # equivalent exponent: octaves vs control (key + range) -> best-fit line residual
    x = np.log2(tg)
    kb = np.array([r["key"] <= 42 for r in rows]) & ok
    ce = cents(hz, tg)
    fit = np.polyfit(x[kb], np.log2(hz[kb]), 1)
    resid = 1200 * (np.log2(hz) - np.polyval(fit, x))
    span_oct = float(np.log2(hz[kb].max() / hz[kb].min()))
    # compare with CA-72's committed reference points where they coincide
    cmp = []
    jp = R.ca72 / "circuits/boards/reference/vco1-tracking.json"
    if jp.exists():
        ref = json.loads(jp.read_text())
        rmap = {"R32": "32", "R16": "16", "R8": "8", "R4": "4", "R2": "2"}
        refd = {(rmap[p["range"]], p["key"]): p["hz"] for p in ref["points"] if p["range"] in rmap}
        for r in rows:
            if (r["range"], r["key"]) in refd:
                cmp.append(float(cents(r["hz"], refd[(r["range"], r["key"])])))
    in_kb = [r for r, k in zip(rows, kb) if k]
    metrics["vco_tracking"] = {
        "points": rows,
        "keyboard_span_octaves": span_oct,
        "raw_cents_error_max_abs_keyboard_range": float(np.nanmax(np.abs(ce[kb]))),
        "raw_cents_error_by_range": {rg: [round(r["cents"], 2) for r in rows if r["range"] == rg and r["key"] <= 42]
                                     for rg in RANGES},
        "bestfit_line_octaves_per_octave": float(fit[0]),
        "bestfit_residual_cents_max_abs_keyboard_range": float(np.nanmax(np.abs(resid[kb]))),
        "above_keyboard_2ft": [{"hz": r["hz"], "target_hz": r["target_hz"], "cents": r["cents"]}
                               for r in rows if r["key"] > 42],
        "vs_ca72_committed_json_cents": {"n": len(cmp),
                                         "mean": float(np.mean(cmp)) if cmp else None,
                                         "spread_pp": float(np.ptp(cmp)) if cmp else None},
        "note": "raw = vs ideal 1.0176 V/oct from the 2' calibration points; bestfit = after a "
                "gain+offset fit (what a linear autotune leaves; table autotune leaves less)"}
    fig, ax = plt.subplots(1, 2, figsize=(13, 4.5))
    for rg in RANGES:
        rr = [r for r in rows if r["range"] == rg]
        ax[0].semilogx([r["target_hz"] for r in rr], [r["cents"] for r in rr], "o-", label=f"{rg}'")
    ax[0].axhspan(-1, 1, color="g", alpha=.1); ax[0].set_xlabel("target Hz"); ax[0].set_ylabel("cents")
    ax[0].set_title("raw tracking error (cal on 2' A440/A3520)"); ax[0].legend(); ax[0].grid(alpha=.3)
    ax[1].semilogx(tg, resid, "o"); ax[1].axhspan(-1, 1, color="g", alpha=.1)
    ax[1].set_title("residual after best-fit gain/offset (keyboard range fit)")
    ax[1].set_xlabel("target Hz"); ax[1].grid(alpha=.3)
    fig.tight_layout(); fig.savefig(R.out / "plots/vco_tracking.png", dpi=110); plt.close(fig)


# ----------------------------------------------------------------------------------------
# filter
CUTS = [-9, -6, -3, 0, 3, 6, 9]
EMPH = [0, 5, 7, 7.5, 8.5]


def bench_filter_ac(R, metrics):
    jobs = [(c, e) for c in CUTS for e in EMPH]

    def one(j):
        c, e = j
        data, dt = R.run("filter_ac", f"ac_c{c:+d}_e{e}", CUT=c, R14=f"{emphasis_r14(e):.4g}")
        return j, data, dt
    res = R.pmap(one, jobs)
    curves = {j: d for j, d, _ in res}
    secs = {j: dt for j, _, dt in res}
    out = {}
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
    for c in CUTS:
        d0 = curves[(c, 0)]
        if d0 is None:
            continue
        f, g0 = d0[:, 0], d0[:, 1]
        gmax = g0.max()
        above = np.where(g0 >= gmax - 3)[0]
        fc = float(f[above[-1]])
        sel = (f >= 2 * fc) & (f <= 8 * fc)
        slope = float(np.polyfit(np.log2(f[sel]), g0[sel], 1)[0]) if sel.sum() > 5 else None
        sel2 = (f >= 8 * fc) & (f <= 32 * fc) & (f <= 1e5)
        slope2 = float(np.polyfit(np.log2(f[sel2]), g0[sel2], 1)[0]) if sel2.sum() > 5 else None
        rec = {"fc_minus3db_hz": fc, "passband_gain_db": float(gmax),
               "slope_db_per_oct_1to3oct_above_fc": slope,
               "slope_db_per_oct_3to5oct_above_fc": slope2, "emphasis": {}}
        for e in EMPH:
            d = curves[(c, e)]
            if d is None:
                rec["emphasis"][str(e)] = {"status": "failed"}
                continue
            g = d[:, 1]
            ip = int(np.argmax(g))
            lo = np.argmin(np.abs(f - fc / 8))
            rec["emphasis"][str(e)] = {
                "r14_ohm": emphasis_r14(e),
                "valid_small_signal": bool(e <= 7.0), "peak_hz": float(f[ip]),
                "peak_db_re_passband": float(g[ip] - gmax),
                "gain_at_fc_over_8_db_re_passband": float(g[lo] - gmax),
                "seconds": round(secs[(c, e)], 2)}
            if c in (-6, 0, 6):
                axs[1].semilogx(f, g - gmax, label=f"cut {c:+d} V, emph {e}")
        axs[0].semilogx(f, g0 - gmax, label=f"cut {c:+d} V (fc {fc:.0f} Hz)")
        out[str(c)] = rec
    for a in axs:
        a.set_ylim(-80, 30); a.grid(alpha=.3, which="both"); a.set_xlabel("Hz"); a.set_ylabel("dB re passband")
    axs[0].set_title("ladder AC, EMPHASIS 0"); axs[0].legend(fontsize=7)
    axs[1].set_title("ladder AC vs EMPHASIS (generic reverse-audio law)"); axs[1].legend(fontsize=6, ncol=2)
    fig.tight_layout(); fig.savefig(R.out / "plots/filter_ac.png", dpi=110); plt.close(fig)
    np.savez_compressed(R.out / "filter_ac_curves.npz",
                        **{f"c{c:+d}_e{e}": curves[(c, e)] for c in CUTS for e in EMPH
                           if curves[(c, e)] is not None})
    metrics["filter_ac"] = out
    return out


def growth_rate(t, y, f0, t_start):
    """Log-envelope slope (nepers per cycle) of an oscillation after t_start."""
    m = t >= t_start
    t, y = t[m], y[m] - np.mean(y[m])
    tt = np.linspace(t[0], t[-1], max(4096, int((t[-1] - t[0]) * f0 * 64)))
    yy = np.interp(tt, t, y)
    yy = yy - signal.savgol_filter(yy, min(len(yy) // 4 * 2 + 1, int(64 * 3) | 1), 1)  # remove drift
    # peak envelope per cycle
    spc = int(64)
    n = len(yy) // spc
    env = np.array([np.max(np.abs(yy[i * spc:(i + 1) * spc])) for i in range(n)])
    env = np.maximum(env, 1e-15)
    k = np.arange(n)
    # use the first part only, before saturation, and after the kick transient
    sel = slice(1, max(4, n))
    lv = np.log(env[sel]); kk = k[sel]
    sat = np.where(lv > lv[0] + np.log(30))[0]
    if len(sat):
        lv, kk = lv[:max(sat[0], 4)], kk[:max(sat[0], 4)]
    return float(np.polyfit(kk, lv, 1)[0]), env


def bench_filter_selfosc(R, metrics, ac):
    # pick CUTOFF voltages that put fc (EMPHASIS 0) near 20, 200, 2000 Hz
    cs = sorted(float(c) for c in ac)
    lf = [np.log(ac[str(int(c))]["fc_minus3db_hz"]) for c in cs]
    targets = {"20Hz": 20.0, "100Hz": 100.0, "200Hz": 200.0, "2kHz": 2000.0}
    dials = [6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 10.0]
    jobs = []
    for name, ft in targets.items():
        cv = float(np.interp(np.log(ft), lf, cs))
        for dl in dials:
            jobs.append((name, ft, cv, dl))

    def one(j):
        name, ft, cv, dl = j
        ncyc = 60
        tstop = 0.02 + ncyc / ft
        data, dt = R.run("filter_tran", f"so_{name}_d{dl}", CUT=f"{cv:.4f}",
                         R14=f"{emphasis_r14(dl):.4g}", KICKW=f"{0.25/ft:.4e}",
                         TMAX=f"{1/ft/80:.4e}", TSTOP=f"{tstop:.4e}")
        return j, data, dt
    res = R.pmap(one, jobs)
    out = {}
    fig, axs = plt.subplots(1, 4, figsize=(19, 4))
    for idx, name in enumerate(targets):
        rr = [(j, d, dt) for j, d, dt in res if j[0] == name]
        cv = rr[0][0][2]; ft = rr[0][0][1]
        rates, info = [], []
        for (n_, ft_, cv_, dl), d, dt in rr:
            if d is None:
                info.append({"dial": dl, "status": "failed", "seconds": round(dt, 2)}); continue
            t, y = d[:, 0], d[:, 1]
            g, env = growth_rate(t, y, ft, 0.001 + 0.25 / ft + 2 / ft)
            # steady-state frequency/amplitude from the last 10 cycles
            m = t > t[-1] - 10 / ft
            tt = np.linspace(t[m][0], t[-1], 8192); yy = np.interp(tt, t, y) - np.mean(y[m])
            amp = float(np.max(np.abs(yy)))
            zc = np.where((yy[:-1] < 0) & (yy[1:] >= 0))[0]
            fo = float((len(zc) - 1) / (tt[zc[-1]] - tt[zc[0]])) if len(zc) > 2 else None
            rates.append((dl, g))
            info.append({"dial": dl, "r14_ohm": emphasis_r14(dl), "growth_np_per_cycle": g,
                         "final_amp_v": amp, "final_freq_hz": fo, "seconds": round(dt, 2)})
            axs[idx].semilogy(env, label=f"{dl}")
        onset = None
        rr2 = sorted(rates)
        for (d1, g1), (d2, g2) in zip(rr2, rr2[1:]):
            if g1 < 0 <= g2:
                # refine by bisection on the sign of the growth rate (3 steps: 0.06 dial)
                lo, hi = d1, d2
                for b in range(3):
                    md = 0.5 * (lo + hi)
                    (_, _, _, _), d, dt = one((name, ft, cv, round(md, 4)))
                    gm, _ = growth_rate(d[:, 0], d[:, 1], ft, 0.001 + 0.25 / ft + 2 / ft)
                    info.append({"dial": md, "r14_ohm": emphasis_r14(md), "growth_np_per_cycle": gm,
                                 "bisection": True, "seconds": round(dt, 2)})
                    lo, hi = (lo, md) if gm >= 0 else (md, hi)
                onset = 0.5 * (lo + hi); break
        out[name] = {"cutoff_v": cv, "fc_em0_hz_target": ft, "onset_dial": onset,
                     "onset_r14_ohm": emphasis_r14(onset) if onset is not None else None,
                     "runs": info}
        axs[idx].set_title(f"{name} (CUT {cv:+.2f} V): envelope vs cycle; onset dial {onset}")
        axs[idx].legend(fontsize=6, title="EMPH"); axs[idx].grid(alpha=.3)
    fig.tight_layout(); fig.savefig(R.out / "plots/filter_selfosc.png", dpi=110); plt.close(fig)
    # lowest self-oscillation: EMPHASIS 10, CUTOFF stepped down; long runs (80 cycles)
    low = []
    def lowrun(cv):
        fe = float(np.exp(np.interp(cv, cs, lf)))
        ncyc = 80
        data, dt = R.run("filter_tran", f"so_low_c{cv:+.1f}", CUT=cv, R14=f"{emphasis_r14(10):.4g}",
                         KICKW=f"{0.25/fe:.4e}", TMAX=f"{1/fe/80:.4e}", TSTOP=f"{0.02+ncyc/fe:.4e}")
        return cv, fe, data, dt
    for cv, fe, d, dt in R.pmap(lowrun, [-9.0, -8.0, -7.0, -6.0, -5.0, -4.0]):
        t, y = d[:, 0], d[:, 1]
        m = t > t[-1] - 20 / fe
        tt = np.linspace(t[m][0], t[-1], 16384); yy = np.interp(tt, t, y) - np.mean(y[m])
        zc = np.where((yy[:-1] < 0) & (yy[1:] >= 0))[0]
        fo = float((len(zc) - 1) / (tt[zc[-1]] - tt[zc[0]])) if len(zc) > 2 else None
        low.append({"cutoff_v": cv, "fc_em0_hz": fe, "final_amp_v": float(np.max(np.abs(yy))),
                    "final_freq_hz": fo, "oscillating": bool(np.max(np.abs(yy)) > 0.05),
                    "seconds": round(dt, 2)})
    osc = [r for r in low if r["oscillating"]]
    out["lowest_selfosc_emph10"] = {"runs": low,
        "lowest_oscillating_freq_hz": min(r["final_freq_hz"] for r in osc) if osc else None}
    metrics["filter_selfosc"] = out


# ----------------------------------------------------------------------------------------
# contours
CONTOUR_CASES = {
    # name: (fa, fd, fs, la, ld, ls, decay_on, ton, toff, tstop, tmax)
    "fastest_S10": (0, 0, 1.0, 0, 0, 1.0, 1, 0.02, 0.32, 0.6, 2e-5),
    "mid_S5":      (5, 5, 0.5, 5, 5, 0.5, 1, 0.02, 3.0, 5.0, 2e-4),
    "attack_max_S10": (10, 0, 1.0, 10, 0, 1.0, 1, 0.02, 20.0, 21.0, 2e-3),
    "decay_max_S0":   (0, 10, 0.0, 0, 10, 0.0, 1, 0.02, 45.0, 46.0, 5e-3),
    "release_decayON":  (0, 4, 1.0, 0, 4, 1.0, 1, 0.02, 0.5, 4.5, 5e-5),
    "release_decayOFF": (0, 4, 1.0, 0, 4, 1.0, 0, 0.02, 0.5, 4.5, 5e-5),
}


def cross_time(t, y, level, t_from, rising=True):
    m = np.where(t >= t_from)[0]
    yy = y[m]
    idx = np.where((yy[:-1] < level) & (yy[1:] >= level))[0] if rising else \
        np.where((yy[:-1] > level) & (yy[1:] <= level))[0]
    if not len(idx):
        return None
    i = m[idx[0]]
    return float(t[i] + (level - y[i]) / (y[i + 1] - y[i]) * (t[i + 1] - t[i]))


def contour_metrics(t, y, ton, toff):
    rest = float(np.median(y[t < ton]))
    held = (t > ton) & (t < toff)
    ip = np.argmax(np.where(held, y, -1e9))
    peak, tpk = float(y[ip]), float(t[ip])
    sus = float(np.mean(y[(t > toff - 0.05 * (toff - ton)) & (t < toff)]))
    a = peak - rest
    t10 = cross_time(t, y, rest + 0.1 * a, ton); t90 = cross_time(t, y, rest + 0.9 * a, ton)
    res = {"rest_v": rest, "peak_v": peak, "t_peak_after_gate_s": tpk - ton,
           "sustain_v_before_release": sus,
           "trigger_delay_s": (t10 - ton) if t10 else None,
           "attack_10_90_s": (t90 - t10) if (t10 and t90) else None}
    # decay: time from peak until 63 % of the way to the sustain value
    if peak - sus > 0.02:
        lvl = peak - 0.632 * (peak - sus)
        td = cross_time(t, y, lvl, tpk, rising=False)
        res["decay_tau63_s"] = (td - tpk) if td else None
        lvl50 = sus + 0.5 * (peak - sus)
        td5 = cross_time(t, y, lvl50, tpk, rising=False)
        res["decay_to_half_s"] = (td5 - tpk) if td5 else None
    # release: from the held level at gate-off
    hv = sus - rest
    if hv > 0.05:
        r90 = cross_time(t, y, rest + 0.9 * hv, toff, rising=False)
        r50 = cross_time(t, y, rest + 0.5 * hv, toff, rising=False)
        r10 = cross_time(t, y, rest + 0.1 * hv, toff, rising=False)
        res["release_90_10_s"] = (r10 - r90) if (r10 and r90) else None
        res["release_90_50_s"] = (r50 - r90) if (r50 and r90) else None
    return res


def bench_contour(R, metrics):
    def one(item):
        name, (fa, fd, fs, la, ld, ls, don, ton, toff, tstop, tmax) = item
        data, dt = R.run("contour_tran", name, FA=f"{time_pot(fa):.4g}", FD=f"{time_pot(fd):.4g}",
                         FS=fs, LA=f"{time_pot(la):.4g}", LD=f"{time_pot(ld):.4g}", LS=ls,
                         DECAYON=don, TON=ton, TON1=ton + 1e-6, TOFF=toff, TOFF1=toff + 1e-6,
                         TMAX=tmax, TSTOP=tstop)
        return name, data, dt
    res = R.pmap(one, list(CONTOUR_CASES.items()))
    out = {}
    fig, axs = plt.subplots(2, 3, figsize=(15, 7))
    for ax, (name, data, dt) in zip(axs.flat, res):
        c = CONTOUR_CASES[name]
        if data is None:
            out[name] = {"status": "failed", "seconds": dt}; continue
        t = data[:, 0]
        out[name] = {"dials": {"f_attack": c[0], "f_decay": c[1], "f_sustain": c[2] * 10,
                               "l_attack": c[3], "l_decay": c[4], "l_sustain": c[5] * 10,
                               "decay_switch": "on" if c[6] else "off"},
                     "seconds": round(dt, 2),
                     "filter": contour_metrics(t, data[:, 1], c[7], c[8]),
                     "loudness": contour_metrics(t, data[:, 2], c[7], c[8])}
        ax.plot(t, data[:, 1], label="filter contour"); ax.plot(t, data[:, 2], label="loudness contour")
        ax.plot(t, data[:, 3] * 0.5, "k:", lw=.8, label="gate")
        ax.set_title(name); ax.grid(alpha=.3); ax.legend(fontsize=7); ax.set_xlabel("s")
    fig.tight_layout(); fig.savefig(R.out / "plots/contours.png", dpi=110); plt.close(fig)
    # overshoot: attack peak / sustain at SUSTAIN 10 (fastest case, held long enough to settle)
    f10 = out.get("fastest_S10", {})
    if "filter" in f10:
        for ch in ("filter", "loudness"):
            m = f10[ch]
            m["overshoot_ratio_peak_over_sustain10"] = (m["peak_v"] - m["rest_v"]) / (m["sustain_v_before_release"] - m["rest_v"])
            m["overshoot_ratio_absolute_volts"] = m["peak_v"] / m["sustain_v_before_release"]
    metrics["contour"] = out


# ----------------------------------------------------------------------------------------
# whole voice
VOICE_PATCHES = {
    # bass pluck: saw 8' A (110 Hz), cutoff -3 V, emphasis 5, filter contour amount 0.6
    "bass_pluck": dict(key=4, rng="8", wave="saw", vol=0.8, cut="vcut cut 0 -3", emph=5.0, amt=0.6,
                       fa=0, fd=4, fs=0.2, la=0, ld=5, ls=0.8, decay_on=1, ton=0.05, toff=1.2, tstop=2.0),
    # resonant sweep: square 8' A, CUTOFF ramped -6 -> +6 V while held, emphasis 7
    "resonant_sweep": dict(key=4, rng="8", wave="rect", vol=0.6, cut="vcut cut 0 pwl(0 -6 0.1 -6 1.9 6 2.0 6)",
                           emph=7.0, amt=0.0, fa=0, fd=0, fs=1.0, la=1, ld=3, ls=1.0, decay_on=1,
                           ton=0.05, toff=1.85, tstop=2.0),
}


def bench_voice(R, metrics, tmax=5e-6):
    def one(item):
        name, p = item
        data, dt = R.run("voice_tran", name, KBD=p["key"] * KEY_STEP, RNG=rng_tap(p["rng"]),
                         WAVE=p["wave"], VOL=p["vol"], CUTNET=p["cut"], R14=f"{emphasis_r14(p['emph']):.4g}",
                         AMT=p["amt"], FA=f"{time_pot(p['fa']):.4g}", FD=f"{time_pot(p['fd']):.4g}", FS=p["fs"],
                         LA=f"{time_pot(p['la']):.4g}", LD=f"{time_pot(p['ld']):.4g}", LS=p["ls"],
                         DECAYON=p["decay_on"], TON=p["ton"], TON1=p["ton"] + 1e-6, TOFF=p["toff"],
                         TOFF1=p["toff"] + 1e-6, TMAX=tmax, TSTOP=p["tstop"])
        return name, data, dt
    res = R.pmap(one, list(VOICE_PATCHES.items()))
    out = {}
    for name, data, dt in res:
        p = VOICE_PATCHES[name]
        if data is None:
            out[name] = {"status": "failed (see log)", "seconds": round(dt, 2)}; continue
        t, y = data[:, 0], data[:, 1]
        peak, dur = to_wav(t, y, R.out / f"wav/voice_{name}.wav")
        # envelope (RMS in 10 ms frames) and spectrum of the held portion
        fs = 48000
        tt = np.arange(0, t[-1], 1 / fs); yy = np.interp(tt, t, y); yy -= yy.mean()
        fr = int(0.01 * fs)
        env = np.sqrt(np.convolve(yy ** 2, np.ones(fr) / fr, "same"))
        f_, tS, S = signal.stft(yy, fs, nperseg=4096, noverlap=3072)
        out[name] = {"seconds": round(dt, 2), "wav": f"wav/voice_{name}.wav", "peak_v": peak,
                     "rms_v_held": float(np.sqrt(np.mean(yy[(tt > p["ton"] + 0.1) & (tt < p["toff"])] ** 2))),
                     "env_peak_time_s": float(tt[np.argmax(env)]),
                     "osc_hz": None}
        tr = reset_times(t, data[:, 5]); tr = tr[tr > 0.05]
        if len(tr) > 3:
            out[name]["osc_hz"] = float(1 / np.mean(np.diff(tr)))
        np.savez_compressed(R.out / f"wav/voice_{name}_features.npz", env=env[::48], f=f_, t=tS,
                            S=np.abs(S).astype(np.float32))
        fig, axs = plt.subplots(3, 1, figsize=(12, 9))
        axs[0].plot(t, y, lw=.4); axs[0].set_title(f"{name}: main out (10K load)"); axs[0].set_ylabel("V")
        axs[1].plot(t, data[:, 3], label="filter contour"); axs[1].plot(t, data[:, 4], label="loudness contour")
        axs[1].legend(); axs[1].set_ylabel("V")
        axs[2].pcolormesh(tS, f_, 20 * np.log10(np.abs(S) + 1e-9), shading="auto", vmin=-120)
        axs[2].set_ylim(0, 8000); axs[2].set_ylabel("Hz"); axs[2].set_xlabel("s")
        for a in axs: a.grid(alpha=.3)
        fig.tight_layout(); fig.savefig(R.out / f"plots/voice_{name}.png", dpi=110); plt.close(fig)
        metrics.setdefault("wavs", {})[f"voice_{name}"] = {"file": out[name]["wav"], "peak_v": peak, "seconds": dur}
    metrics["voice"] = out


# ----------------------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--adapter", default=str(HERE / "adapters/golden_ca72.inc"))
    ap.add_argument("--ca72", default=str(DEFAULT_CA72))
    ap.add_argument("--tag", default="golden")
    ap.add_argument("--timeout", type=float, default=900)
    ap.add_argument("--jobs", type=int, default=max(1, os.cpu_count() or 1))
    ap.add_argument("--only", default="cal,waves,tracking,filter,contour,voice")
    ap.add_argument("--no-cal", action="store_true", help="use the adapter's own trims")
    a = ap.parse_args()
    R = Runner(a.adapter, Path(a.ca72), HERE / "out" / a.tag, HERE / "work" / a.tag, a.timeout, a.jobs)
    R.ca72 = Path(a.ca72)
    only = set(a.only.split(","))
    mpath = R.out / "metrics.json"
    metrics = json.loads(mpath.read_text()) if mpath.exists() else {}
    metrics["meta"] = {"adapter": a.adapter, "tag": a.tag, "ngspice": subprocess.run(
        ["ngspice", "-v"], capture_output=True, text=True).stdout.split("\n")[1].strip(),
        "date": time.strftime("%Y-%m-%d %H:%M")}
    t_all = time.time()
    stages = [("cal", None), ("waves", bench_vco_waves), ("tracking", bench_vco_tracking),
              ("filter", None), ("contour", bench_contour), ("voice", bench_voice)]
    timing = metrics.get("stage_seconds", {})
    for name, fn in stages:
        t0 = time.time()
        if name == "cal":
            # calibration is needed by every VCO-using stage; re-use a stored one if skipped
            if a.no_cal:
                R.dutparams = ""
            elif "cal" in only or "vco_calibration" not in metrics:
                if only & {"cal", "waves", "tracking", "voice"}:
                    print("== VCO calibration", flush=True); calibrate_vco(R, metrics)
            else:
                c = metrics["vco_calibration"]; R.dutparams = f"r11={c['r11']:.6f} a8={c['a8']:.6f}"
        elif name in only:
            print(f"== {name}", flush=True)
            if name == "filter":
                ac = bench_filter_ac(R, metrics); bench_filter_selfosc(R, metrics, ac)
            elif name == "voice":
                bench_voice(R, metrics)
            else:
                fn(R, metrics)
        else:
            continue
        timing[name] = round(time.time() - t0, 1)
        metrics["stage_seconds"] = timing
        mpath.write_text(json.dumps(metrics, indent=1, default=float))
    metrics["sim_log"] = R.log
    metrics["total_seconds_this_run"] = round(time.time() - t_all, 1)
    mpath.write_text(json.dumps(metrics, indent=1, default=float))
    print(f"done in {metrics['total_seconds_this_run']} s -> {mpath}")


if __name__ == "__main__":
    main()
