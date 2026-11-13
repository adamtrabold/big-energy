"""Resample an ngspice wrdata trace to a normalized 48 kHz WAV."""
import sys, numpy as np, soundfile as sf
src, dst = sys.argv[1], sys.argv[2]
d = np.loadtxt(src); t, v = d[:,0], d[:,1]
fs = 48000; tt = np.arange(0, t[-1], 1/fs)
y = np.interp(tt, t, v); y -= np.mean(y); y /= (np.max(np.abs(y)) + 1e-12); y *= 0.8
sf.write(dst, y.astype(np.float32), fs); print(dst, f"{tt[-1]:.2f}s")
