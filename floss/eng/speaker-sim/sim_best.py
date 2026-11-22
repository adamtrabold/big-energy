"""
floss speaker, round 3: "what will sound best, any method" (owner).

Reuses the lumped model in sim.py and adds:
  - PUI AS06504PS-X-R (65 mm long-throw; datasheet via components.ru mirror, PUI product page for height)
  - two-driver pairs, mono (both drivers in one box, each on its own amp channel = parallel equivalent)
Scores each option on what matters for a string machine played outdoors on battery:
  low-mid output per watt (150-800 Hz), extension (f3/f6), max clean SPL at 100-200 Hz and 200-800 Hz,
  watts needed for 80 dB at 1 m across 150-800 Hz, and spread over parameter tolerances.

Run: python3 -I sim_best.py   (writes best_*.png and best_summary.csv)
"""
import csv
import importlib.util
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("sim", os.path.join(HERE, "sim.py"))
sim = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sim)
F, RHOC2 = sim.F, sim.RHOC2

# ---- PUI AS06504PS-X-R: Re 3.32, Le 0.202 mH, Fs 132, Qms 3.617, Mms 2.658 g, Bl 4.283, Vas 0.188 L, Xmax 4.75
fs, mms = 132.0, 2.658e-3
cms = 1 / ((2 * np.pi * fs) ** 2 * mms)                       # [derived]
sim.DRIVERS["AS06504PS"] = dict(
    Re=3.32, Le=0.202e-3, Bl=4.283, Mms=mms, Cms=cms, Rms=2 * np.pi * fs * mms / 3.617,
    Sd=np.sqrt(0.188e-3 / (RHOC2 * cms)), xmax=4.75e-3, P=10.0, depth=36.7, od=65.0, disp=22e-6,
    mass=92, label="PUI AS06504PS-X-R (65 mm, 36.7 deep)")


def pair(name):
    """Two identical drivers, same box, each on its own amp channel (mono signal): parallel equivalent."""
    d = dict(sim.DRIVERS[name])
    d.update(Re=d["Re"] / 2, Le=d["Le"] / 2, Mms=2 * d["Mms"], Cms=d["Cms"] / 2, Rms=2 * d["Rms"],
             Sd=2 * d["Sd"], P=2 * d["P"], disp=2 * d["disp"], label="2 x " + d["label"])
    sim.DRIVERS["2x" + name] = d
    return "2x" + name


pair("TEBM28C10-4B")
pair("AS05804PS")

# ---- options: (key, driver, Vb cm3, loading, amp W total, module-size note)
OPTIONS = [
    # key, driver, Vb cm3, loading, amp W total, port diameter m, module-size note
    ("A", "TEBM28C10-4B", 76, "sealed", 2.0, None, "as drawn: crown 70 wide, 35 tall, 105 deep"),
    ("B", "TEBM28C10-4B", 76, "ported", 2.0, 0.012, "crown as drawn; port 192 mm long = 22 cm3 of a 76 cm3 box: impractical"),
    ("C", "TEBM28C10-4B", 120, "ported", 2.0, 0.012, "one driver, ~1.6x the crown's box, 35 tall"),
    ("D", "2xTEBM28C10-4B", 150, "sealed", 4.0, None, "two drivers, ~2x the crown's box, 35 tall"),
    ("E", "2xTEBM28C10-4B", 190, "ported", 4.0, 0.016, "two drivers, ~2.5x the crown's box, 35 tall"),
    ("E2", "2xTEBM28C10-4B", 250, "ported", 4.0, 0.016, "two drivers, ~3.3x the crown's box, 35 tall"),
    ("G", "AS05804PS", 150, "ported", 2.0, 0.012, "body ~42 at the crown"),
    ("H", "2xAS05804PS", 250, "ported", 4.0, 0.016, "body ~42, two drivers"),
    ("I", "AS06504PS", 150, "sealed", 2.0, None, "body ~45, 65 mm square"),
    ("J", "AS06504PS", 200, "ported", 2.0, 0.016, "body ~45, 65 mm square"),
]


def band(r, lo, hi, key="spl"):
    m = (F >= lo) & (F <= hi)
    return float(np.mean(r[key][m]))


def run():
    rows, curves = [], {}
    for key, drv, vb, load, amp, dia, note in OPTIONS:
        sim.AMP_W_MAX = amp
        Vb = vb * 1e-6
        vent = sim.best_port(drv, Vb, dia=dia) if load == "ported" else None
        r = sim.simulate(drv, Vb, vent)
        c = dict(drv=drv, Vb=Vb, vent=vent)
        mc = sim.monte_carlo(c, n=200)
        spread = np.percentile(mc, 90, axis=0) - np.percentile(mc, 10, axis=0)
        lm = band(r, 150, 800)
        need80 = 10 ** ((80 - lm) / 10)                      # W for 80 dB avg, 150-800 Hz
        row = dict(
            opt=key, driver=drv, loading=load, Vb_cm3=vb, amp_W=amp,
            SPL_1W_150_800=round(lm, 1), f3=round(sim.f_at(r["spl"], 3)), f6=round(sim.f_at(r["spl"], 6)),
            rel100=round(r["spl"][np.argmin(abs(F - 100))] - np.mean(r["spl"][(F > 700) & (F < 1500)]), 1),
            maxSPL_100_200=round(band(r, 100, 200, "maxspl"), 1),
            maxSPL_200_800=round(band(r, 200, 800, "maxspl"), 1),
            W_for_80dB=round(need80, 3), spread_90_400=round(float(spread[(F > 90) & (F < 400)].max()), 1),
            port=(f"D{dia*1e3:.0f} x {(vent[2]-0.73*dia)*1e3:.0f} mm, {r['vport'].max():.1f} m/s @1W" if vent else ""),
            size=note)
        rows.append(row)
        curves[key] = (r, mc)
        print(row)
    with open(os.path.join(HERE, "best_summary.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

    fig, ax = plt.subplots(1, 2, figsize=(14, 5.2))
    for key, drv, vb, load, amp, dia, note in OPTIONS:
        r, mc = curves[key]
        ln, = ax[0].semilogx(F, r["spl"], label=f"{key}: {drv} {load} {vb} cm3")
        ax[1].semilogx(F, r["maxspl"], color=ln.get_color())
    ax[0].set(title="SPL at 1 W total, 1 m, half space", ylabel="dB SPL", ylim=(55, 95))
    ax[1].set(title="Max clean SPL (amp, Xmax, port 17 m/s)", ylabel="dB SPL", ylim=(60, 105))
    for a in ax:
        a.set_xlabel("Hz"); a.grid(True, which="both", alpha=0.3)
        a.axvspan(150, 800, color="0.9", zorder=0)
        for fnote in (65.4, 130.8, 261.6):
            a.axvline(fnote, color="0.75", lw=0.8)
    ax[0].legend(fontsize=7, loc="lower right")
    fig.text(0.5, 0.005, "Shaded: 150-800 Hz, where the ensemble and pads live. Grey lines C2, C3, C4. "
             "Pairs: both drivers in one box, each on its own 2 W channel.", ha="center", fontsize=8)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(os.path.join(HERE, "best_compare.png"), dpi=110)
    plt.close(fig)

    keys = ["A", "C", "D", "E", "J"]
    fig, ax = plt.subplots(1, len(keys), figsize=(18, 4.2), sharey=True)
    for a, k in zip(ax, keys):
        r, mc = curves[k]
        a.semilogx(F, r["spl"])
        a.fill_between(F, np.percentile(mc, 10, axis=0), np.percentile(mc, 90, axis=0), alpha=0.25)
        a.set(title=f"{k}", xlabel="Hz", ylim=(55, 95)); a.grid(True, which="both", alpha=0.3)
    ax[0].set_ylabel("dB SPL, 1 W")
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "best_tolerance.png"), dpi=110)
    plt.close(fig)


if __name__ == "__main__":
    run()
