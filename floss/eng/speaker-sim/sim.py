"""
floss speaker: lumped-parameter simulation from published Thiele/Small data only.

Model (classic small-signal analogue circuit, as in Small 1972-73 / Beranek):
  electrical:  Ze = Re + jwLe + Bl^2 / Zm_total
  mechanical:  Zm = Rms + jwMms + 1/(jwCms)   (Mms as published, i.e. incl. air load)
  back load:   Zm_total = Zm + Sd^2 * Z_load
  Z_load = Z_box || Z_vent  (acoustic impedances, Pa*s/m^3)
     Z_box  = Ral || 1/(jwCab),   Cab = Vb/(rho c^2),  Ral = QL/(w_ref Cab)  (leak + absorption lumped)
     Z_vent = passive radiator: (Rmp + jwMmp + 1/(jwCmp)) / Sp^2   (n identical PRs in parallel)
              port:             jw rho Leff/Sp + small R
  driver volume velocity Ud = Sd * Bl * i / Zm_total
  vent volume velocity  Uv = -Ud * Z_load / Z_vent        (box rarefies when the cone moves out)
  radiated              U  = Ud + Uv
  SPL at 1 m, half space (module on a table): p = rho * w * |U| / (2 pi r)

Not in the model (see module-r2.md 1.6): cone break-up, baffle diffraction, front cavity and grille,
box wall flex, real stuffing behaviour, PR rocking, port turbulence/compression, temperature, the lap.

Run:  python3 -I sim.py      (writes PNG + summary.csv next to this file)
"""
import csv
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
RHO, C = 1.18, 343.0
RHOC2 = RHO * C * C
F = np.logspace(np.log10(40), np.log10(5000), 600)
W = 2 * np.pi * F

# ---------------------------------------------------------------- published data
# Every number below is copied from the cited source; [derived] marks arithmetic from them.
DRIVERS = {
    "TEBM28C10-4B": dict(  # Tectonic datasheet (datasheet.sic-components.com/TEBM28C10-4B.pdf)
        Re=3.8, Le=0.10e-3, Bl=2.9, Mms=1.19e-3, Cms=1.0e-3, Rms=0.31, Sd=8.55e-4,
        xmax=1.4e-3,   # "Max Linear Excursion 2.8 mm peak to peak"
        P=10.0, depth=24.0, od=55.0, disp=13e-6, mass=58, label="Tectonic TEBM28C10-4B (24 mm deep)"),
    "DMA58-4": dict(  # Dayton spec via soundimports.eu/en/dma58-4.html
        Re=3.55, Le=0.20e-3, Bl=3.67, Mms=2.05e-3, Cms=0.45e-3,
        Rms=2 * np.pi * 165.5 * 2.05e-3 / 2.4,  # [derived] from Fs 165.5, Qms 2.4
        Sd=14.5e-4, xmax=2.0e-3, P=15.0, depth=31.75, od=55.88, disp=15e-6, mass=None,
        label="Dayton DMA58-4 (31.75 mm deep)"),
    "AS05804PS": dict(  # PUI datasheet AS05804PS-X-R + puiaudio.com product page (height 33.8)
        Re=3.62, Le=0.142e-3, Bl=3.72, Mms=2.26e-3,
        Cms=1 / ((2 * np.pi * 145) ** 2 * 2.26e-3),          # [derived] from Fs 145, Mms
        Rms=2 * np.pi * 145 * 2.26e-3 / 6.719,                # [derived] from Qms 6.719
        Sd=None, Vas=0.108e-3,                                # Sd [derived] from Vas below
        xmax=4.5e-3, P=10.0, depth=33.8, od=58.2, disp=18e-6, mass=92,
        label="PUI AS05804PS-X-R (33.8 mm deep)"),
}
d = DRIVERS["AS05804PS"]
d["Sd"] = np.sqrt(d["Vas"] / (RHOC2 * d["Cms"]))             # [derived] ~12.1 cm^2

RADIATORS = {
    "APR050SO-R": dict(  # PUI datasheet APR050SO-R (Mouser) + product page: 50 x 37 x 3.35 mm
        Mmp=4.06e-3, Cmp=0.928e-3, Rmp=0.81, Sp=8.7e-4, xmax=None,  # excursion NOT published
        depth=3.35, foot=(50, 37), label="PUI APR050SO-R (3.35 mm thick)"),
    "TEPR32": dict(  # Tectonic TEPR32 datasheet (DigiKey)
        Mmp=4.2e-3, Cmp=3.6e-3, Rmp=0.27, Sp=np.pi * 0.016 ** 2, xmax=5.0e-3,
        depth=None, foot=(40, 40), label="Tectonic TEPR32 (depth unpublished)"),
    "DMA58-PR": dict(  # Dayton spec via soundimports.eu/en/dma58-pr.html
        Mmp=6.7e-3, Cmp=2.40e-3, Rmp=2 * np.pi * 39.8 * 6.7e-3 / 3.93,  # [derived] from Qms 3.93
        Sp=14.5e-4, xmax=7.0e-3, depth=38.1, foot=(56, 56), label="Dayton DMA58-PR (38.1 mm deep)"),
}

AMP_W_MAX = 2.0     # [est] a 5 V class-D into 4 ohm, e.g. PAM8302 class, at low distortion
PR_XMAX_GUESS = 1.0e-3  # APR050SO-R excursion is unpublished: shown only as a dashed what-if

# ---------------------------------------------------------------- shapes and boxes
# Inner box footprint (mm) left after board + battery, from module-r2.md section 3.
SHAPES = {
    "RAIL 400x80":  dict(L=128, Wd=70),
    "SLAB 400x133": dict(L=150, Wd=110),
    "BLOCK 270x100": dict(L=60, Wd=93),
}
FLOOR, DECK, CLEAR = 2.4, 2.5, 3.0     # mm [plat floor/deck; est clearance behind the magnet]


def body_for(depth_mm):
    """Body thickness (without knobs) needed for a part of this depth hung under the deck [est]."""
    return depth_mm + DECK + CLEAR + FLOOR


def net_volume(shape, drv, prs, body):
    s = SHAPES[shape]
    h = body - FLOOR - DECK
    gross = s["L"] * s["Wd"] * h * 1e-9                    # m^3
    pr_disp = sum(15e-6 if p == "DMA58-PR" else 3e-6 for p in prs)   # [est]
    return 0.95 * gross - DRIVERS[drv]["disp"] - pr_disp    # 5 % for braces / wiring [est]


# ---------------------------------------------------------------- the model
def simulate(drv, Vb, vent=None, QL=7.0, scale=None):
    """vent: None (sealed) | ('pr', name, n) | ('port', diam_m, Leff_m)."""
    p = dict(DRIVERS[drv])
    if scale:
        for k, v in scale.items():
            if k in p:
                p[k] = p[k] * v
    Cab = Vb / RHOC2
    Zm = p["Rms"] + 1j * W * p["Mms"] + 1 / (1j * W * p["Cms"])
    Zv = None
    if vent is not None and vent[0] == "pr":
        r = dict(RADIATORS[vent[1]])
        n = vent[2]
        mp = r["Mmp"] * (scale.get("Mmp", 1) if scale else 1)
        cp = r["Cmp"] * (scale.get("Cmp", 1) if scale else 1)
        Zv = (r["Rmp"] + 1j * W * mp + 1 / (1j * W * cp)) / (r["Sp"] ** 2) / n
        # reference frequency for the box loss: PR + box resonance
        cb_m = Cab / (r["Sp"] ** 2 * n) * n * n  # box compliance seen by n PRs moving together
        k_tot = 1 / cp + (r["Sp"] ** 2 * n) / Cab
        f_ref = np.sqrt(k_tot / mp) / (2 * np.pi)
    elif vent is not None and vent[0] == "port":
        dia, Leff = vent[1], vent[2]
        Sp = np.pi * dia ** 2 / 4
        Map = RHO * Leff / Sp
        Zv = 1j * W * Map + RHO * C / Sp * 0.02     # small port loss [est]
        f_ref = 1 / (2 * np.pi * np.sqrt(Map * Cab))
    else:
        mt = p["Mms"]
        kt = 1 / p["Cms"] + p["Sd"] ** 2 / Cab
        f_ref = np.sqrt(kt / mt) / (2 * np.pi)
    Ral = QL / (2 * np.pi * f_ref * Cab)
    Zbox = 1 / (1 / Ral + 1j * W * Cab)
    Zload = Zbox if Zv is None else 1 / (1 / Zbox + 1 / Zv)
    Zmt = Zm + p["Sd"] ** 2 * Zload
    Ze = p["Re"] + 1j * W * p["Le"] + p["Bl"] ** 2 / Zmt
    V = np.sqrt(1.0 * p["Re"])            # 1 W into Re (amplitude, RMS)
    i = V / Ze
    Ud = p["Sd"] * p["Bl"] * i / Zmt
    Uv = np.zeros_like(Ud) if Zv is None else -Ud * Zload / Zv
    U = Ud + Uv
    pr = RHO * W * np.abs(U) / (2 * np.pi * 1.0)
    spl = 20 * np.log10(pr / 20e-6)
    xd = np.abs(Ud) / (W * p["Sd"]) * np.sqrt(2)          # peak, m, at 1 W
    out = dict(spl=spl, Ze=np.abs(Ze), xd=xd, f_ref=f_ref, V=V, p=p)
    if vent is not None and vent[0] == "pr":
        r = RADIATORS[vent[1]]
        out["xv"] = np.abs(Uv) / (W * r["Sp"] * vent[2]) * np.sqrt(2)
        out["vxmax"] = r["xmax"]
    if vent is not None and vent[0] == "port":
        Sp = np.pi * vent[1] ** 2 / 4
        out["vport"] = np.abs(Uv) / Sp * np.sqrt(2)        # peak air speed, m/s, at 1 W
    # max SPL: amp power, driver xmax, PR xmax (if published), port speed <= 17 m/s (5 % of c)
    g = np.full_like(F, 10 * np.log10(min(AMP_W_MAX, p["P"])))
    g = np.minimum(g, 20 * np.log10(p["xmax"] / xd))
    if "xv" in out and out["vxmax"]:
        g = np.minimum(g, 20 * np.log10(out["vxmax"] / out["xv"]))
    if "vport" in out:
        g = np.minimum(g, 20 * np.log10(17.0 / out["vport"]))
    out["maxspl"] = spl + g
    return out


def f_at(spl, drop):
    ref = np.mean(spl[(F > 700) & (F < 1500)])
    below = np.where(spl < ref - drop)[0]
    below = below[F[below] < 700]
    return F[below[-1]] if len(below) else F[0]


def port_for(Vb, fb, dia=0.012):
    Sp = np.pi * dia ** 2 / 4
    return ("port", dia, Sp * C * C / ((2 * np.pi * fb) ** 2 * Vb))   # Leff


def best_port(drv, Vb, dia=0.012):
    """Standard small-box design by sweep: the lowest f3 whose response stays within +1.5 dB
    of the 0.7-1.5 kHz reference (no hump). Same rule a box program applies by eye."""
    fs = 1 / (2 * np.pi * np.sqrt(DRIVERS[drv]["Mms"] * DRIVERS[drv]["Cms"]))
    best = None
    for fb in np.linspace(0.5 * fs, 1.4 * fs, 60):
        v = port_for(Vb, fb, dia)
        r = simulate(drv, Vb, v)
        ref = np.mean(r["spl"][(F > 700) & (F < 1500)])
        if r["spl"].max() - ref > 1.5:
            continue
        f3 = f_at(r["spl"], 3)
        if best is None or f3 < best[0]:
            best = (f3, v)
    return best[1] if best else port_for(Vb, 0.8 * fs, dia)


def volume_sweep():
    """Sealed box: f3 and Qtc against net volume, for each driver (the box-size question)."""
    vols = np.array([30, 40, 50, 60, 80, 100, 130, 160, 200, 250, 300, 400]) * 1e-6
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.5))
    rows = []
    for drv, dd in DRIVERS.items():
        vas = RHOC2 * dd["Sd"] ** 2 * dd["Cms"]
        fs = 1 / (2 * np.pi * np.sqrt(dd["Mms"] * dd["Cms"]))
        qes = 2 * np.pi * fs * dd["Mms"] * dd["Re"] / dd["Bl"] ** 2
        qms = 2 * np.pi * fs * dd["Mms"] / dd["Rms"]
        qts = qes * qms / (qes + qms)
        f3s, qtcs = [], []
        for V in vols:
            r = simulate(drv, V)
            f3s.append(f_at(r["spl"], 3))
            qtcs.append(qts * np.sqrt(1 + vas / V))
            rows.append(dict(driver=drv, Vb_cm3=round(V * 1e6), f3_Hz=round(f3s[-1]), Qtc=round(qtcs[-1], 2),
                             fc_Hz=round(fs * np.sqrt(1 + vas / V)), Vas_cm3=round(vas * 1e6), Fs=round(fs),
                             Qts=round(qts, 2)))
        ax[0].plot(vols * 1e6, f3s, "o-", label=dd["label"])
        ax[1].plot(vols * 1e6, qtcs, "o-", label=dd["label"])
    ax[0].set(xlabel="net box volume, cm3", ylabel="f3, Hz", title="Sealed: -3 dB point vs volume")
    ax[1].set(xlabel="net box volume, cm3", ylabel="Qtc", title="Sealed: Qtc vs volume (0.707 = flattest)")
    ax[1].axhline(0.707, color="0.6", ls="--")
    for a in ax:
        a.grid(alpha=0.3); a.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "sealed_volume_sweep.png"), dpi=110)
    plt.close(fig)
    with open(os.path.join(HERE, "sealed_volume_sweep.csv"), "w", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        wr.writeheader(); wr.writerows(rows)
    return rows


# ---------------------------------------------------------------- candidates
def candidates():
    """Every driver / loading that physically fits each shape's box (see module-r2.md 1.3)."""
    rows = []
    for shape, s in SHAPES.items():
        for drv in DRIVERS:
            dd = DRIVERS[drv]
            if dd["od"] + 2 > min(s["L"], s["Wd"]):
                continue
            body = body_for(dd["depth"])
            opts = [("sealed", None, [])]
            # passive radiators on the deck beside the driver: footprint check
            free_len = s["L"] - dd["od"] - 4
            for prn, n in (("APR050SO-R", 1), ("APR050SO-R", 2), ("TEPR32", 1), ("DMA58-PR", 1)):
                fx, fy = RADIATORS[prn]["foot"]
                fits = (min(fx, fy) * n + 2 * (n - 1) <= free_len and max(fx, fy) <= s["Wd"]) or \
                       (max(fx, fy) * n + 2 * (n - 1) <= free_len and min(fx, fy) <= s["Wd"]) or \
                       (n == 1 and min(fx, fy) <= s["Wd"] - dd["od"] - 4 and max(fx, fy) <= s["L"])
                if fits:
                    opts.append((f"PR {n}x {prn}", ("pr", prn, n), [prn] * n))
            opts.append(("ported", "port", []))
            for name, vent, prs in opts:
                b = body
                for prn in prs:
                    dep = RADIATORS[prn]["depth"] or 0
                    b = max(b, body_for(dep))
                Vb = net_volume(shape, drv, prs, b)
                if vent == "port":
                    vent = best_port(drv, Vb)
                rows.append(dict(shape=shape, drv=drv, name=name, vent=vent, Vb=Vb, body=b))
    return rows


# ---------------------------------------------------------------- tolerance study
def monte_carlo(c, n=300, seed=1):
    rng = np.random.default_rng(seed)
    curves = []
    for _ in range(n):
        sc = dict(
            Mms=rng.uniform(0.9, 1.1), Cms=rng.uniform(0.8, 1.2), Bl=rng.uniform(0.9, 1.1),
            Rms=rng.uniform(0.8, 1.2), Mmp=rng.uniform(0.8, 1.2), Cmp=rng.uniform(0.8, 1.2))
        QL = rng.uniform(3, 15)
        Vb = c["Vb"] * rng.uniform(0.9, 1.1)
        vent = c["vent"]
        curves.append(simulate(c["drv"], Vb, vent, QL=QL, scale=sc)["spl"])
    curves = np.array(curves)
    return curves


def main():
    for r in volume_sweep():
        print(r)
    rows = candidates()
    summary = []
    for c in rows:
        r = simulate(c["drv"], c["Vb"], c["vent"])
        c["res"] = r
        mc = monte_carlo(c)
        c["mc"] = mc
        band = (F > 90) & (F < 400)
        spread = np.percentile(mc, 90, axis=0) - np.percentile(mc, 10, axis=0)
        f3s = [f_at(s, 3) for s in mc]
        ref = np.mean(r["spl"][(F > 700) & (F < 1500)])
        i100 = np.argmin(abs(F - 100))
        i150 = np.argmin(abs(F - 150))
        extra = ""
        if "xv" in r:
            xv_peak = r["xv"].max() * 1e3
            extra = f"PR peak {xv_peak:.2f} mm at 1 W"
        if "vport" in r:
            extra = f"port Leff {c['vent'][2]*1e3:.0f} mm, peak air {r['vport'].max():.1f} m/s at 1 W"
        summary.append(dict(
            shape=c["shape"], driver=c["drv"], loading=c["name"],
            body_mm=round(c["body"], 1), Vb_cm3=round(c["Vb"] * 1e6),
            SPL_1W_1k=round(ref, 1), f3_Hz=round(f_at(r["spl"], 3)), f6_Hz=round(f_at(r["spl"], 6)),
            f10_Hz=round(f_at(r["spl"], 10)), rel100_dB=round(r["spl"][i100] - ref, 1),
            f3_P10_P90=f"{np.percentile(f3s,10):.0f}-{np.percentile(f3s,90):.0f}",
            spread_90_400_dB=round(spread[band].max(), 1),
            maxSPL_100=round(r["maxspl"][i100], 1), maxSPL_150=round(r["maxspl"][i150], 1),
            note=extra))
    with open(os.path.join(HERE, "summary.csv"), "w", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=list(summary[0].keys()))
        wr.writeheader()
        wr.writerows(summary)

    # ---- per-shape plots: SPL, impedance, excursion, max SPL
    for shape in SHAPES:
        cs = [c for c in rows if c["shape"] == shape]
        fig, ax = plt.subplots(2, 2, figsize=(13, 9))
        for c in cs:
            r = c["res"]
            lab = f"{c['drv']} {c['name']} ({c['Vb']*1e6:.0f} cm3, body {c['body']:.0f} mm)"
            ln, = ax[0, 0].semilogx(F, r["spl"], label=lab)
            ax[0, 1].semilogx(F, r["Ze"], color=ln.get_color())
            ax[1, 0].semilogx(F, r["xd"] * 1e3, color=ln.get_color())
            if "xv" in r:
                ax[1, 0].semilogx(F, r["xv"] * 1e3, color=ln.get_color(), ls=":")
            ax[1, 1].semilogx(F, r["maxspl"], color=ln.get_color())
        ax[0, 0].set(title=f"{shape}: SPL at 1 W, 1 m, half space", ylabel="dB SPL", ylim=(55, 95))
        ax[0, 1].set(title="Impedance magnitude", ylabel="ohm")
        ax[1, 0].set(title="Peak excursion at 1 W (solid driver, dotted radiator)", ylabel="mm",
                     ylim=(0, 6))
        ax[1, 1].set(title=f"Max SPL (amp {AMP_W_MAX:.0f} W, driver Xmax, PR Xmax if published, port 17 m/s)",
                     ylabel="dB SPL", ylim=(60, 100))
        for a in ax.flat:
            a.set_xlabel("Hz"); a.grid(True, which="both", alpha=0.3)
            for fn in (65.4, 130.8, 261.6):
                a.axvline(fn, color="0.8", lw=0.8)
        ax[0, 0].legend(fontsize=7, loc="lower right")
        fig.text(0.5, 0.005, "Grey lines: C2, C3, C4. Lumped model from published T/S data; no measurement.",
                 ha="center", fontsize=8)
        fig.tight_layout(rect=(0, 0.02, 1, 1))
        fig.savefig(os.path.join(HERE, f"shape_{shape.split()[0].lower()}.png"), dpi=110)
        plt.close(fig)

    # ---- tolerance plot: the candidates for the recommended path in each shape
    picks = [c for c in rows if c["drv"] == "TEBM28C10-4B"]
    fig, axs = plt.subplots(1, len(SHAPES), figsize=(16, 5), sharey=True)
    for a, shape in zip(axs, SHAPES):
        for c in [c for c in picks if c["shape"] == shape]:
            mc = c["mc"]
            lo, hi = np.percentile(mc, 10, axis=0), np.percentile(mc, 90, axis=0)
            ln, = a.semilogx(F, c["res"]["spl"], label=c["name"])
            a.fill_between(F, lo, hi, color=ln.get_color(), alpha=0.18)
        a.set(title=f"{shape}, TEBM28C10-4B: nominal + P10-P90 band", xlabel="Hz", ylim=(50, 90))
        a.grid(True, which="both", alpha=0.3); a.legend(fontsize=8)
    axs[0].set_ylabel("dB SPL at 1 W, 1 m")
    fig.text(0.5, 0.005, "300 draws: driver Mms +/-10 %, Cms +/-20 %, Bl +/-10 %, Rms +/-20 %; PR Mmp, Cmp +/-20 %; "
             "box loss QL 3-15; volume +/-10 %.", ha="center", fontsize=8)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(os.path.join(HERE, "tolerance_tebm28.png"), dpi=110)
    plt.close(fig)

    # same for the DMA58 path
    picks = [c for c in rows if c["drv"] == "DMA58-4"]
    fig, axs = plt.subplots(1, len(SHAPES), figsize=(16, 5), sharey=True)
    for a, shape in zip(axs, SHAPES):
        for c in [c for c in picks if c["shape"] == shape]:
            mc = c["mc"]
            lo, hi = np.percentile(mc, 10, axis=0), np.percentile(mc, 90, axis=0)
            ln, = a.semilogx(F, c["res"]["spl"], label=c["name"])
            a.fill_between(F, lo, hi, color=ln.get_color(), alpha=0.18)
        a.set(title=f"{shape}, DMA58-4: nominal + P10-P90 band", xlabel="Hz", ylim=(50, 95))
        a.grid(True, which="both", alpha=0.3); a.legend(fontsize=8)
    axs[0].set_ylabel("dB SPL at 1 W, 1 m")
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "tolerance_dma58.png"), dpi=110)
    plt.close(fig)

    for s in summary:
        print({k: (float(v) if hasattr(v, 'dtype') else v) for k, v in s.items()})


if __name__ == "__main__":
    main()
