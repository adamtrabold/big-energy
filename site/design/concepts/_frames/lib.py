"""Shared drawing kit for the site concept frames (visual designer, concept turn 1).
Phones are drawn at 1:1 (390 x 844) with an iOS status band (47) and a Safari bottom bar (83),
so the usable no-scroll area is y 47..761 (714 px). Desktop frames are 1440 x 900 at 1:1.
Content is real: images from the repo, waveform from the golden/perturbed WAVs, words from owner.md.
"""
import os, io, base64, warnings, subprocess
import numpy as np
from PIL import Image, ImageFont
from scipy.io import wavfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "../../../.."))

# palette (settled, jam turn 2 + director turn 3)
BG = "#E6E4DF"; CELL = "#EFEDE9"; PAGE = "#F8F7F4"; RULE = "#C4C1BA"
INK2 = "#5F5D58"; INK = "#1B1B19"; ON = "#23863F"; WHITE = "#FFFFFF"
CHROME = "#D6D4CF"
F = "Inter"
FONTS = {400: "Inter-Regular.otf", 500: "Inter-Medium.otf", 600: "Inter-SemiBold.otf", 700: "Inter-Bold.otf"}
_fc = {}
def font(size, w):
    k = (round(size * 4), w)
    if k not in _fc:
        _fc[k] = ImageFont.truetype("/usr/share/fonts/opentype/inter/" + FONTS[w], size=max(1, int(round(size * 4))))
    return _fc[k]
def tw(s, size, w=400, ls=0):
    return font(size, w).getlength(s) / 4 + ls * len(s)

PW, PH = 390, 844
TOP, BOT = 47, 761          # usable area inside the browser chrome

class Canvas:
    def __init__(s, W, H):
        s.W, s.H, s.o = W, H, []
        s.n = 0
    def a(s, x): s.o.append(x)
    def uid(s):
        s.n += 1; return f"u{s.n}"
    # primitives
    def t(s, x, y, txt, size=13, w=400, fill=INK, anchor="start", ls=0, op=1, upper=False):
        if upper: txt = txt.upper()
        e = str(txt).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        s.a(f'<text x="{x:.1f}" y="{y:.1f}" font-family="{F}" font-size="{size}" font-weight="{w}" fill="{fill}" '
            f'text-anchor="{anchor}" letter-spacing="{ls}" opacity="{op}" style="font-feature-settings:\'tnum\'">{e}</text>')
    def label(s, x, y, txt, fill=INK2, anchor="start"):
        s.t(x, y, txt, 10.5, 500, fill, anchor, ls=0.9, upper=True)
    def wrap(s, x, y, txt, width, size=13, w=400, fill=INK, lh=None, maxlines=99, op=1):
        lh = lh or size * 1.45
        words = txt.split(); line = ""; n = 0
        for wd in words:
            cand = (line + " " + wd).strip()
            if tw(cand, size, w) > width and line:
                n += 1
                if n == maxlines:
                    while tw(line + "…", size, w) > width: line = line[:-1]
                    s.t(x, y, line + "…", size, w, fill, op=op); return y + lh
                s.t(x, y, line, size, w, fill, op=op); y += lh; line = wd
            else:
                line = cand
        if line: s.t(x, y, line, size, w, fill, op=op); y += lh
        return y
    def r(s, x, y, w, h, fill="none", stroke=None, sw=1, op=1, dash=None):
        st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        if dash: st += f' stroke-dasharray="{dash}"'
        s.a(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}"{st} opacity="{op}"/>')
    def l(s, x1, y1, x2, y2, c=RULE, sw=1, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        s.a(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" stroke-width="{sw}"{d}/>')
    def circle(s, x, y, rad, fill="none", stroke=None, sw=1, op=1):
        st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        s.a(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rad}" fill="{fill}"{st} opacity="{op}"/>')
    def path(s, d, fill="none", stroke=INK, sw=1.2, op=1):
        s.a(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{op}"/>')

    # images
    def img(s, key, x, y, w, h=None, op=1, crop=None, fit="width"):
        im = IMG(key)
        iw, ih = im.size
        if h is None: h = w * ih / iw
        cid = s.uid()
        s.a(f'<clipPath id="{cid}"><rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}"/></clipPath>')
        if crop:
            fx, fy, fw, fh = crop
            sc = w / (fw * iw)
            s.a(f'<image href="{URI(key)}" x="{x - fx*iw*sc:.1f}" y="{y - fy*ih*sc:.1f}" width="{iw*sc:.1f}" height="{ih*sc:.1f}" clip-path="url(#{cid})" opacity="{op}" preserveAspectRatio="none"/>')
        else:
            s.a(f'<image href="{URI(key)}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" clip-path="url(#{cid})" opacity="{op}" preserveAspectRatio="xMidYMid meet"/>')
        return h

    # shared components
    def lamp(s, x, y, state):
        if state == "on":
            s.circle(x, y, 5, ON)
        elif state == "standby":
            s.circle(x, y, 4.5, "none", INK2, 1.2)
        elif state == "dip":
            s.circle(x, y, 9, "none", ON, 1, op=0.35); s.circle(x, y, 5, ON, op=0.45)
        elif state == "snapshot":
            s.l(x - 5, y, x + 5, y, RULE, 1.5)
    def lampline(s, x, y, state, text):
        s.lamp(x + 5, y - 4, state)
        s.label(x + 18, y, text, INK if state in ("on", "dip") else INK2)
    def dot(s, x, y, fill=INK): s.circle(x, y, 3, fill)
    def delta(s, x, y, n=None, size=10):
        s.path(f"M{x},{y-size} L{x+size*0.95},{y+size*0.62} L{x-size*0.95},{y+size*0.62} Z", "none", INK, 1.2)
        if n is not None: s.t(x, y + size * 0.42, str(n), size * 0.78, 700, INK, "middle")
    def play(s, x, y, rad=22, playing=False):
        s.circle(x, y, rad, "none", INK, 1.5)
        if playing:
            s.r(x - 7, y - 8, 5, 16, INK); s.r(x + 2, y - 8, 5, 16, INK)
        else:
            s.path(f"M{x-6},{y-10} L{x+10},{y} L{x-6},{y+10} Z", INK, None, 0)
    def wave(s, key, x, y, w, h, n=None, color=INK, sw=1.3, op=1):
        pk = PEAKS(key, n or max(20, int(w / 3)))
        d = []
        for i, p in enumerate(pk):
            xx = x + i * w / (len(pk) - 1)
            d.append(f"M{xx:.1f},{y - max(0.5, p*h/2):.1f}L{xx:.1f},{y + max(0.5, p*h/2):.1f}")
        s.a(f'<path d="{" ".join(d)}" stroke="{color}" stroke-width="{sw}" opacity="{op}"/>')
    def cloud(s, x, y, w, h, bump=7, sw=1.4):
        """revision cloud: scalloped outline (D only)"""
        pts = []
        def edge(x0, y0, x1, y1):
            L = ((x1-x0)**2 + (y1-y0)**2) ** 0.5; n = max(1, int(L / (bump * 2)))
            for i in range(n):
                ax, ay = x0 + (x1-x0)*i/n, y0 + (y1-y0)*i/n
                bx, by = x0 + (x1-x0)*(i+1)/n, y0 + (y1-y0)*(i+1)/n
                pts.append(f"A{bump},{bump} 0 0 1 {bx:.1f},{by:.1f}")
        d = f"M{x:.1f},{y:.1f}"
        edge(x, y, x+w, y); edge(x+w, y, x+w, y+h); edge(x+w, y+h, x, y+h); edge(x, y+h, x, y)
        s.a(f'<path d="{d}{"".join(pts)}" fill="none" stroke="{INK}" stroke-width="{sw}"/>')

    def phone(s, x, y, title, notes, tap=None):
        s.r(x, y, PW, PH, BG)
        # chrome
        s.r(x, y, PW, TOP, CHROME, op=0.55)
        s.t(x + 30, y + 31, "9:41", 15, 600, INK)
        s.r(x, y + BOT, PW, PH - BOT, CHROME, op=0.55)
        s.r(x + 20, y + BOT + 12, PW - 40, 40, "#F4F3F0")
        s.t(x + PW / 2, y + BOT + 37, "claude.ai", 14, 500, INK2, "middle")
        s.r(x - 0.5, y - 0.5, PW + 1, PH + 1, "none", "#8f8c85", 1)
        s.t(x, y - 18, title, 17, 700)
        if tap: s.t(x + PW, y - 18, tap, 13, 600, INK2, "end")
        yy = y + PH + 28
        for n in notes:
            yy = s.wrap(x, yy, n, PW, 12.5, 400, INK2, lh=18)
    def save(s, path_noext):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
               f'width="{s.W}" height="{s.H}" viewBox="0 0 {s.W} {s.H}">' + "\n".join(s.o) + "</svg>")
        open(path_noext + ".svg", "w").write(svg)
        subprocess.run(["rsvg-convert", "-o", path_noext + ".png", path_noext + ".svg"], check=True)

# image registry (real repo files)
SRC = {
    "FOLD-A": "versions/v1.1/fold/mock-A-look.png",
    "FOLD-A@v1": "versions/v1/fold/mock-A-look.png",
    "FOLD-A@r5": "archive/fold-superseded/mock-A-look.png",
    "FOLD-B": "versions/v1.1/fold/mock-B-real-size.png",
    "FOLD-C": "versions/v1.1/fold/mock-C-construction.png",
    "FOLD-D": "versions/v1.1/fold/mock-D-front.png",
    "FOLD-E": "versions/v1.1/fold/mock-E-standing.png",
    "HUSH-A": "versions/v1.1/hush/mock-A-look.png",
    "HUSH-B": "versions/v1.1/hush/mock-B-real-size.png",
    "HUSH-C": "versions/v1.1/hush/mock-C-construction.png",
    "HUSH-D": "versions/v1.1/hush/mock-D-front.png",
    "ONESHEET-A": "versions/v1.1/one-sheet/mock-A-look.png",
    "ONESHEET-B": "versions/v1.1/one-sheet/mock-B-real-size.png",
    "ONESHEET-C": "versions/v1.1/one-sheet/mock-C-construction.png",
    "ONESHEET-D": "versions/v1.1/one-sheet/mock-D-front.png",
    "FOLD113-A": "archive/fold-superseded/mock-A-look-113.png",
    "TYPECASE-A": "archive/paused-concepts/type-case/mock-A-look.png",
    "HYMNAL-A": "archive/paused-concepts/hymnal/mock-A-look.png",
    "PLOT-pluck": "eng/sim/reference/out/golden/plots/voice_bass_pluck.png",
    "PLOT-vco": "eng/sim/reference/out/golden/plots/vco_tracking.png",
    "SKETCH": "design/concepts/jam-visual-sketches.png",
}
_img, _uri = {}, {}
def IMG(key):
    if key not in _img:
        im = Image.open(os.path.join(ROOT, SRC[key])).convert("RGB")
        im.thumbnail((1400, 1000)); _img[key] = im
    return _img[key]
def URI(key):
    if key not in _uri:
        buf = io.BytesIO(); IMG(key).save(buf, "JPEG", quality=72)
        _uri[key] = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    return _uri[key]

WAVS = {"golden": "eng/sim/reference/out/golden/wav/voice_bass_pluck.wav",
        "perturbed": "eng/sim/reference/out/example_perturbed/wav/voice_bass_pluck.wav"}
_pk = {}
def PEAKS(key, n):
    k = (key, n)
    if k not in _pk:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            _, d = wavfile.read(os.path.join(ROOT, WAVS[key]))
        seg = np.array_split(np.abs(d.astype(float)), n)
        pk = np.array([q.max() for q in seg])
        _pk[k] = pk / 1.86  # common scale (perturbed peak 1.86 V) so A/B heights are comparable
    return _pk[k]

def doc_page(c, x, y, w, h, title, lines, meta=None, size=12.5):
    """a doc mounted as a page (E's doc specimen; also used for doc tiles)"""
    c.r(x, y, w, h, PAGE)
    pad = max(8, w * 0.06)
    cid = c.uid()
    c.a(f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath><g clip-path="url(#{cid})">')
    yy = c.wrap(x + pad, y + pad + size * 1.1, title, w - 2 * pad, size * 1.2, 600, INK, lh=size * 1.5)
    yy += size * 0.4
    for ln in lines:
        if yy > y + h - 4: break
        yy = c.wrap(x + pad, yy, ln, w - 2 * pad, size, 400, INK, lh=size * 1.5)
        yy += size * 0.35
    c.a("</g>")

DAISY_FP_TITLE = "Daisy Seed, from first principles: every subsystem it touches"
DAISY_FP = ["Status: rev 0, 2026-11-13. Answers the owner, after “Switch to Daisy Seed”: go back to first principles and see if there's a better way with Daisy seed.",
            "For each subsystem the Seed touches: what the job needs; the best Daisy-native way; how it compares with the Pico-era design; a recommendation.",
            "What doesn't change. The voice stays analog: VCOs, ladder, contours, VCA, noise, and osc 3 as the LFO."]
DAISY_PIN_TITLE = "Pin check and audio-quality check: Daisy Seed vs Pico 2 + SGTL5000"
DAISY_PIN = ["Status: rev 0, 2026-11-13. Answers the owner: “Check the pin thing. Audio feels the most important since we're introducing digital stuff.”",
             "Daisy Seed fits all I/O (26/31 pins). The Pico plan fits only 26/26 and misses the filter-cal counter and MIDI out."]
SPEC_TITLE = "Budget variant (“Little D”): a ~$100 instrument with the Model D spirit"
SPEC = ["Latest rev 14 (2026-11-13): channel aftertouch with its own switch. Rev 13: Daisy Seed replaces the Pico 2 (§v1.11).",
        "The digital brain is an Electrosmith Daisy Seed, socketed. It does all control duties plus the digital echo and reverb; the dry voice path stays analog."]
