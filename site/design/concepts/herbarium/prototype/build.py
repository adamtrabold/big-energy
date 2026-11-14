#!/usr/bin/env python3
"""Build the E Herbarium prototype (throwaway, real content) from the repo.

    python3 build.py            -> index.html + media/ next to this file

What it does: reads the repo (branch groups and their img/, v1.1 legacy sheets, eng sims plots and WAVs,
design/owner.md decisions, scores, VERSIONS.md, a few docs), writes web-sized COPIES of existing images
(no new renders), converts the WAVs to 16-bit PCM, computes the FOLD-A / HUSH-A change areas from a pixel
diff, and writes one index.html with the data embedded as JSON and the app inline (CSS + JS).
The real site's build.py will do the same job from site/numbers.json; codes here are illustrative.
"""
import os, re, json, io, html, warnings, hashlib
import numpy as np
from PIL import Image, ImageChops
from scipy import ndimage
from scipy.io import wavfile
import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "../../../../.."))
MEDIA = os.path.join(HERE, "media")
os.makedirs(os.path.join(MEDIA, "t"), exist_ok=True)

def P(*a): return os.path.join(ROOT, *a)
def rd(p): return open(P(p), encoding="utf-8").read()

# ------------------------------------------------------------------ media (copies only)
USED = set()
def jpg(src, name, long=1400, q=78):
    USED.update({name + ".jpg", "t/" + name + ".jpg"})
    out, th = os.path.join(MEDIA, name + ".jpg"), os.path.join(MEDIA, "t", name + ".jpg")
    im = Image.open(P(src)).convert("RGB")
    W, H = im.size
    if not (os.path.exists(out) and os.path.getmtime(out) > os.path.getmtime(P(src))):
        a = im.copy(); a.thumbnail((long, long), Image.LANCZOS); a.save(out, "JPEG", quality=q, optimize=True, progressive=True)
        b = im.copy(); b.thumbnail((560, 560), Image.LANCZOS); b.save(th, "JPEG", quality=70, optimize=True)
    a = Image.open(out)
    return {"src": "media/" + name + ".jpg", "thumb": "media/t/" + name + ".jpg", "w": a.size[0], "h": a.size[1], "orig": f"{W} × {H}", "path": src}

def wav(src, name):
    USED.add(name + ".wav")
    out = os.path.join(MEDIA, name + ".wav")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        rate, d = wavfile.read(P(src))
    d = d.astype(np.float64)
    if d.ndim > 1: d = d.mean(axis=1)
    peak = float(np.max(np.abs(d)))
    if not os.path.exists(out):
        wavfile.write(out, rate, (d / max(peak, 1e-9) * 0.89 * 32767).astype(np.int16))
    seg = np.array_split(np.abs(d), 240)
    return {"src": "media/" + name + ".wav", "dur": round(len(d) / rate, 2), "peak_v": round(peak, 2),
            "peaks": [round(float(s.max()), 3) for s in seg]}

def clouds(a, b):
    A = Image.open(P(a)).convert("L"); B = Image.open(P(b)).convert("L")
    if A.size != B.size: return []
    d = np.array(ImageChops.difference(A, B)) > 24
    H, W = d.shape; g = 48; gy, gx = H // g, W // g
    m = d[:gy * g, :gx * g].reshape(gy, g, gx, g).mean(axis=(1, 3)) > 0.002
    m = ndimage.binary_dilation(m, iterations=2)
    lab, n = ndimage.label(m)
    return [[round(s[1].start * g / W, 4), round(s[0].start * g / H, 4), round((s[1].stop - s[1].start) * g / W, 4), round((s[0].stop - s[0].start) * g / H, 4)]
            for s in ndimage.find_objects(lab)]

# ------------------------------------------------------------------ markdown -> HTML
DOCMAP = {}  # basename -> code, filled below (fallback only)
PATHMAP = {}  # repo-relative path -> "#hash" (exact; filled before docs are rendered, see LINKS below)
def resolve(href, src):
    p = href.split("#")[0]
    if not p or p.startswith("http"): return None
    cands = []
    if src: cands.append(os.path.normpath(os.path.join(os.path.dirname(src), p)))
    cands.append(os.path.normpath(p.lstrip("./")))
    for c in cands:
        if c in PATHMAP: return PATHMAP[c]
    base = os.path.basename(p)
    if base in DOCMAP and sum(1 for k in PATHMAP if os.path.basename(k) == base) <= 1: return "#i-" + DOCMAP[base]
    return None
_COPYSRC = [None]
def copied(href, src):
    """downscaled copy of an image a doc links (path relative to the doc); None if not on disk"""
    if not href or href.startswith("http"): return None
    base_dir = os.path.dirname(src or _COPYSRC[0] or "")
    rel = os.path.normpath(os.path.join(base_dir, href))
    if not os.path.exists(P(rel)): return None
    name = "X-" + re.sub(r"[^A-Za-z0-9]+", "-", os.path.splitext(rel)[0].replace("design/branches/concepts/", "")).strip("-")
    sub = "drawing" if "px-per-mm" in rel or rel.endswith(".png") else "render"
    return jpg(rel, name, 1600 if sub == "drawing" else 1400, 82 if sub == "drawing" else 80)
STATUS_WORDS = r"(decided|proposed|open|not yet written|written|started)"
def mark_status(h):
    """make decided / proposed / open visible: tag them inside table cells and bold runs"""
    def cell(m):
        inner = re.sub(r"\b(decided|proposed|open)\b", r'<span class="st st-\1">\1</span>', m.group(2))
        return m.group(1) + inner + "</td>"
    h = re.sub(r"(<td[^>]*>)(.*?)</td>", cell, h, flags=re.S)
    h = re.sub(r"<strong>(decided|proposed|open)</strong>", r'<span class="st st-\1">\1</span>', h)
    return h
def label_cells(h):
    """data-label on each td from its table's header, so tables can stack on a phone"""
    def table(m):
        t = m.group(0)
        heads = [re.sub(r"<[^>]+>", "", x).strip() for x in re.findall(r"<th[^>]*>(.*?)</th>", t, flags=re.S)]
        def row(r):
            i = [0]
            def td(c):
                lab = heads[i[0]] if i[0] < len(heads) else ""; i[0] += 1
                return f'<td data-label="{html.escape(lab)}"' + c.group(1) + ">"
            return re.sub(r"<td([^>]*)>", td, r.group(0))
        return re.sub(r"<tr>.*?</tr>", row, t, flags=re.S)
    return re.sub(r"<table>.*?</table>", table, h, flags=re.S)
LIST_RE = re.compile(r"^\s*([-*+]|\d+[.)])\s")
def loosen_lists(text):
    """Python-Markdown needs a blank line before a list; GitHub doesn't. Add one so lists render as lists."""
    out, fence, prev = [], False, ""
    for line in text.splitlines():
        if line.lstrip().startswith("```"): fence = not fence
        if (not fence and LIST_RE.match(line) and prev.strip() and not LIST_RE.match(prev)
                and not prev.startswith(("|", "    ", "\t")) and not prev.lstrip().startswith(">")):
            out.append("")
        out.append(line); prev = line
    return "\n".join(out)

def md(text, imap=None, src=None, status=False):
    _COPYSRC[0] = src
    h = markdown.markdown(loosen_lists(text), extensions=["tables", "fenced_code", "sane_lists"])
    def pic(m):
        attrs = dict(re.findall(r'(\w+)="([^"]*)"', m.group(0)))
        base = os.path.splitext(os.path.basename(attrs.get("src", "")))[0]
        if imap and base in imap:
            it = items[imap[base]]
            return (f'</p><figure><a href="#i-{it["code"]}"><img src="{it["src"]}" width="{it["w"]}" height="{it["h"]}" alt="{attrs.get("alt","")}" loading="lazy"></a>'
                    f'<figcaption>{attrs.get("alt","")} · {it["sub"]}</figcaption></figure><p>')
        f = copied(attrs.get("src", ""), src)
        if f:
            return (f'</p><figure><a href="{f["src"]}" target="_blank" rel="noopener"><img src="{f["src"]}" width="{f["w"]}" height="{f["h"]}" alt="{attrs.get("alt","")}" loading="lazy"></a>'
                    f'<figcaption>{attrs.get("alt","")}</figcaption></figure><p>')
        return f'<span class="ref">[image: {attrs.get("alt","")}]</span>'
    def rawfig(m):
        blk = m.group(0)
        src = re.search(r'<img [^>]*src="([^"]+)"', blk)
        base = os.path.splitext(os.path.basename(src.group(1)))[0] if src else ""
        if not (imap and base in imap):
            f = copied(src.group(1), None) if src else None
            if not f: return '<span class="ref">[image not on disk]</span>'
            cap = re.search(r"<figcaption>(.*?)</figcaption>", blk, flags=re.S)
            return f'<figure><img data-done src="{f["src"]}" width="{f["w"]}" height="{f["h"]}" alt="" loading="lazy"><figcaption>{cap.group(1).strip() if cap else ""}</figcaption></figure>'
        it = items[imap[base]]
        alt = (re.search(r'alt="([^"]*)"', blk) or [None, ""])[1]
        cap = re.search(r"<figcaption>(.*?)</figcaption>", blk, flags=re.S)
        cap = cap.group(1).strip() if cap else alt
        return (f'<figure><a href="#i-{it["code"]}"><img data-done src="{it["src"]}" width="{it["w"]}" height="{it["h"]}" alt="{alt}" loading="lazy"></a>'
                f'<figcaption>{cap} · {it["sub"]}</figcaption></figure>')
    h = re.sub(r"<figure>.*?</figure>", rawfig, h, flags=re.S)
    h = re.sub(r"<img (?![^>]*data-done)[^>]*>", pic, h).replace("<p></p>", "")
    def link(m):
        href, inner = m.group(1), m.group(2)
        if href.startswith("http"): return f'<a href="{href}" rel="noopener" target="_blank">{inner}</a>'
        if href.startswith("#"): return f'<span class="ref">{inner}</span>'
        r = resolve(href, src)
        return f'<a href="{r}">{inner}</a>' if r else f'<span class="ref">{inner}</span>'
    h = re.sub(r'<a href="([^"]*)">(.*?)</a>', link, h, flags=re.S)
    def code(m):
        r = resolve(m.group(1), src)
        return f'<a href="{r}"><code>{m.group(1)}</code></a>' if r else m.group(0)
    h = re.sub(r'<code>([^<]*?\.md)</code>', code, h)
    h = label_cells(h)
    if status: h = mark_status(h)
    h = h.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
    return h

def sections(text):
    """split a doc into (heading, markdown) chunks at ## headings; preamble first"""
    parts, cur, head = [], [], None
    for line in text.splitlines():
        if line.startswith("## "):
            parts.append((head, "\n".join(cur))); cur, head = [], line[3:].strip()
        else: cur.append(line)
    parts.append((head, "\n".join(cur)))
    return [(h, b) for h, b in parts if (h or b.strip())]

def first_para(text):
    for blk in text.split("\n\n"):
        b = blk.strip()
        if b and not b.startswith("#") and not b.startswith("|"):
            t = re.sub(r"[*`]", "", b.replace("\n", " "))
            return t if len(t) <= 240 else t[:240].rsplit(" ", 1)[0].rstrip(",;:(") + "…"
    return ""

items, groups, order = {}, [], []
def add(code, **k):
    k["code"] = code; items[code] = k; order.append(code); return k

# ------------------------------------------------------------------ docs (codes illustrative)
DOCS = [
    ("D-019", "eng/budget-variant.md", "Budget variant spec", "Spec", "current", "rev 14 · 13 Nov · channel aftertouch with its own switch"),
    ("D-031", "eng/daisy-pin-and-audio-check.md", "Pin check and audio-quality check", "Spec", "current", "rev 0 · 13 Nov"),
    ("D-032", "eng/daisy-first-principles.md", "Daisy Seed, from first principles", "Spec", "current", "rev 0 · 13 Nov"),
    ("D-034", "eng/aftertouch.md", "Aftertouch", "Spec", "current", "13 Nov"),
    ("D-003", "versions/v1.1/common-how-it-works.md", "Common how it works (as locked in v1.1)", "Lock", "locked in v1.1", "13 Nov"),
    ("D-011", "versions/v1.1/fold/how-it-works.md", "FOLD · how it works", "Lock", "locked in v1.1", "13 Nov"),
    ("D-013", "versions/v1.1/hush/how-it-works.md", "HUSH · how it works", "Lock", "locked in v1.1", "13 Nov"),
    ("D-015", "versions/v1.1/one-sheet/how-it-works.md", "ONE SHEET · how it works", "Lock", "locked in v1.1", "13 Nov"),
    ("D-040", "design/branches/echo-clock.md", "Echo clock (FREE / SYNC)", "Spec", "current", "13 Nov"),
    ("R-001", "design/owner.md", "Owner record (the instrument)", "Concept", "current", "13 Nov"),
    ("R-002", "design/scores.md", "Director scores, rounds 1–5", "Concept", "current", "13 Nov"),
    ("R-003", "VERSIONS.md", "Versions", "Lock", "current", "13 Nov"),
    ("R-004", "site/design/owner.md", "Owner record (the project site)", "Concept", "current", "13 Nov"),
]
BR = {"cathedral": ("CATHEDRAL", "D-110", "D-109"), "chamber": ("CHAMBER", "D-101", "D-102"), "rain": ("RAIN", "D-103", "D-104"), "diptych": ("DIPTYCH", "D-105", "D-106"), "butterfly": ("BUTTERFLY", "D-107", "D-108")}
_have = {p for _, p, *_ in DOCS}
ENG_TITLES = {"cost-estimate": "Cost estimate", "key-sourcing": "Key sourcing", "battery": "Battery", "effects": "Effects (eng)", "single-chip-research": "Single-chip research",
              "open-items": "Open engineering items", "architecture": "Architecture (eng, full instrument)", "architecture-v2": "Architecture v2 (eng)", "daisy-switch-notes": "Daisy switch notes",
              "velocity-and-keys-v2": "Velocity and keys v2", "fold-answers": "FOLD answers", "keys-answers": "Keys answers", "little-d-design-answers": "Little D design answers",
              "round4-answers": "Round 4 answers", "answers-E1-E10": "Answers E1–E10"}
for f in sorted(os.listdir(P("eng"))):
    if f.endswith(".md") and "eng/" + f not in _have:
        slug = f[:-3]
        DOCS.append(("E-" + slug, "eng/" + f, ENG_TITLES.get(slug, slug.replace("-", " ").capitalize()), "Spec", "current", "13 Nov"))
for code, path, *_ in DOCS:
    DOCMAP[os.path.basename(path)] = code; PATHMAP[os.path.normpath(path)] = "#i-" + code
# docs/ and design/reviews/ become pages of their own
SITE_DOCS = [("architecture", "docs/architecture.md")] + [(os.path.splitext(f)[0], "docs/features/" + f) for f in sorted(os.listdir(P("docs/features"))) if f.endswith(".md")]
for slug, path in SITE_DOCS: PATHMAP[path] = "#doc-" + slug
PATHMAP["docs/README.md"] = "#docs"
REVIEWS = [(os.path.splitext(f)[0], "design/reviews/" + f) for f in sorted(os.listdir(P("design/reviews")), reverse=True) if f.endswith(".md")] if os.path.isdir(P("design/reviews")) else []
for slug, path in REVIEWS: PATHMAP[path] = "#review-" + slug
for c, (G, a, b) in {"cathedral": ("CATHEDRAL", "D-109", "D-110"), "chamber": ("CHAMBER", "D-102", "D-101"), "rain": ("RAIN", "D-104", "D-103"), "diptych": ("DIPTYCH", "D-106", "D-105"), "butterfly": ("BUTTERFLY", "D-108", "D-107")}.items():
    PATHMAP[f"design/branches/concepts/{c}/how-it-looks-and-feels.md"] = "#g-" + G
    PATHMAP[f"design/branches/concepts/{c}/how-it-works.md"] = "#i-" + b
for c, (G, a, b) in BR.items():
    pass  # branch docs share basenames (how-it-works.md); linked through their groups instead

for code, path, title, stage, status, slip in DOCS:
    t = rd(path)
    add(code, kind="record" if code.startswith("R") else "doc", sub="record" if code.startswith("R") else "doc", title=title, stage=stage,
        status=status, date="13 Nov", revs=[{"rev": "A", "line": slip}], path=path, html=md(t, src=path), lead=first_para(t),
        jump=[h for h, _ in sections(t) if h][:30])

# ------------------------------------------------------------------ branch groups (new format)
BRANCH = [  # newest first
  # status from the branches director (design/notes/director.md, 13 Nov 13:09)
    ("cathedral", "CATHEDRAL", "exploring", "CHAMBER and FOLD-105 meet: the middle ground you asked for (14:12). The current case.", "current · round in progress", []),
    ("chamber", "CHAMBER", "exploring", "closed it's an organ case; open it's a console", "branches round 1: 8", ["chamber-standing", "chamber-open", "chamber-closed-printed", "chamber-closed-with-book", "chamber-flat-from-above", "chamber-standing-from-behind", "chamber-reverse-pegs", "chamber-top-12.41px-per-mm", "chamber-pegs-12.41px-per-mm", "chamber-time-dial-12.41px-per-mm"]),
    ("rain", "RAIN", "exploring", "a pond after rain", "branches round 1: 7", ["rain", "rain-close", "rain-stepping-stones", "rain-arms-length", "rain-top-12.70px-per-mm", "rain-pegs-12.70px-per-mm", "rain-time-and-pads-12.70px-per-mm", "rain-ring-pitch-compare-40px-per-mm"]),
    ("butterfly", "BUTTERFLY", "dropped", "from tool to tree: exact at the playing edge, free at the rear", "branches round 1: 6 · retired by the branches director", ["butterfly", "butterfly-joint", "butterfly-from-behind", "butterfly-on-the-wall", "butterfly-top-11.49px-per-mm", "butterfly-rear-section-24px-per-mm", "butterfly-time-dial-11.49px-per-mm"]),
    ("diptych", "DIPTYCH", "dropped", "a scientific field instrument", "branches round 1: killed by the branches director", ["diptych-standing", "diptych-open", "diptych-closed", "diptych-standing-side-exact", "diptych-top-14.48px-per-mm"]),
]
ROUND2 = {"CHAMBER", "RAIN"}
LEAD = {"CATHEDRAL": "cathedral-s5-P5R-standing"}   # a standing 3/4 view leads the visual index
STATUS = {"CATHEDRAL": "current", "CHAMBER": "scored 9 · grew into CATHEDRAL", "RAIN": "scored 7 · re-score pending",
          "BUTTERFLY": "dropped · retired at 6", "DIPTYCH": "dropped · killed"}   # round 2 fixes landed 13 Nov; re-score pending
SEED = {"CATHEDRAL": "CHAMBER", "CHAMBER": "FOLD", "RAIN": "ONESHEET", "BUTTERFLY": "ONESHEET", "DIPTYCH": "FOLD"}
def nice(stem, G):
    s = stem.replace(G.lower() + "-", "").replace(G.lower(), "the look")
    m = re.search(r"-([\d.]+)px-per-mm", s)
    scale = f" · 1:1 at {m.group(1)} px/mm" if m else ""
    s = re.sub(r"-[\d.]+px-per-mm", "", s).replace("-", " ")
    return (s or "the look"), ("drawing" if m or "exact" in stem else "render"), scale
for folder, G, status, line, scoreline, _stems in BRANCH:
    base = f"design/branches/concepts/{folder}/"
    look = rd(base + "how-it-looks-and-feels.md")
    refs = []
    for m in re.finditer(r'!\[([^\]]*)\]\((img/[^)\s]+)\)|<figure>(.*?)</figure>|<img [^>]*src="(img/[^"]+)"[^>]*>', look, flags=re.S):
        if m.group(2): refs.append((m.group(1), m.group(2)))
        elif m.group(3):
            blk = m.group(3); src = re.search(r'src="(img/[^"]+)"', blk)
            if not src: continue
            cap = re.search(r"<figcaption>(.*?)</figcaption>", blk, flags=re.S); alt = re.search(r'alt="([^"]*)"', blk)
            refs.append((html.unescape(re.sub(r"<[^>]+>", "", cap.group(1) if cap else alt.group(1) if alt else "")).strip(), src.group(1)))
        elif m.group(4):
            alt = re.search(r'alt="([^"]*)"', m.group(0)); refs.append((alt.group(1) if alt else "", m.group(4)))
    codes, imap = [], {}
    for alt, rel in refs:
        stem = os.path.splitext(os.path.basename(rel))[0]
        title, sub, scale = nice(stem, G)
        code = f"{G}-{re.sub(r'[^a-z0-9]+', '-', title.lower())}".rstrip("-")
        if code in items or not os.path.exists(P(base + rel)): continue   # the branches team is mid-round: skip files not on disk
        m = jpg(base + rel, code, 1400 if sub == "render" else 1600, 78 if sub == "render" else 82)
        rv = "B" if G in ROUND2 else "A"
        add(code, kind="image", sub=sub, title=alt, short=title + scale, stage="Concept", status=status, date="13 Nov",
            revs=[{"rev": rv, "line": "round 2" if rv == "B" else "branches round 1", **m}], group=G, **m)
        codes.append(code); imap[stem] = code
    _, hw, lf = BR[folder]
    docs = []
    for dcode, fn, nm in [(lf, "how-it-looks-and-feels.md", "how it looks and feels"), (hw, "how-it-works.md", "how it works")]:
        if os.path.exists(P(base + fn)):
            t = rd(base + fn)
            add(dcode, kind="doc", sub="doc", title=f"{G} · {nm}", stage="Concept", status=status, date="13 Nov",
                revs=[{"rev": "B", "line": "round 2"}] if G in ROUND2 else [{"rev": "A", "line": "branches round 1"}], path=base + fn, html=md(t, imap, src=base + fn), lead=first_para(t),
                jump=[h for h, _ in sections(t) if h][:30], group=G)
            docs.append(dcode)
    if G in LEAD:
        if imap.get(LEAD[G]) in codes: codes.remove(imap[LEAD[G]]); codes.insert(0, imap[LEAD[G]])
    grevs = ([{"rev": "B", "line": "round 2 fixes · re-score pending"}] if G in ROUND2 else []) + [{"rev": "A", "line": scoreline}]
    groups.append({"code": G, "title": G, "rev": grevs[0]["rev"], "status": status, "stage": "Concept", "date": "13 Nov", "new": True,
                   "line": line, "lead": codes[0] if codes else None, "images": codes, "docs": docs, "seed": SEED[G],
                   "revs": grevs, "round": "Branches round 1", "statusLabel": STATUS.get(G, status)})

# ------------------------------------------------------------------ legacy groups (A3 sheets, images as they are)
SHEETS = {"FOLD": ("fold", "ABCDE", "C", "FOLD-105 · a hinge · walnut + white"), "HUSH": ("hush", "ABCD", "B", "nothing shouts: grey wool, natural maple, cream knobs"),
          "ONESHEET": ("one-sheet", "ABCD", "B", "one printed sheet, rings texture")}
SHEETNAME = {"A": "The look", "B": "Real size", "C": "Construction", "D": "Front", "E": "Standing"}
SHEETFILE = {"A": "mock-A-look", "B": "mock-B-real-size", "C": "mock-C-construction", "D": "mock-D-front", "E": "mock-E-standing"}
cl = {}
for G, (folder, letters, grev, line) in SHEETS.items():
    codes = []
    for L in letters:
        code = f"{G}-{L}"
        cur = jpg(f"versions/v1.1/{folder}/{SHEETFILE[L]}.png", code, 1600, 74)
        revs = [{"rev": "C" if G == "FOLD" and L in "ABC" else "B", "line": "v1.1 · bend drawn as a joystick in every view", "where": "v1.1", **cur}]
        if code in ("FOLD-A", "HUSH-A"):  # lineage in the prototype: two sheets only (size)
            v1 = jpg(f"versions/v1/{folder}/{SHEETFILE[L]}.png", code + "-v1", 1600, 74)
            revs.append({"rev": "B" if G == "FOLD" else "A", "line": "v1 · first lock", "where": "v1", **v1})
            cl[code] = {revs[0]["rev"] + revs[1]["rev"]: clouds(f"versions/v1/{folder}/{SHEETFILE[L]}.png", f"versions/v1.1/{folder}/{SHEETFILE[L]}.png")}
            if code == "FOLD-A":
                r5 = jpg("archive/fold-superseded/mock-A-look.png", "FOLD-A-r5", 1600, 74)
                revs.append({"rev": "A", "line": "round 5 · archive", "where": "archive", **r5})
        add(code, kind="image", sub="legacy sheet", title=SHEETNAME[L], stage="Lock", status="locked in v1.1", date="13 Nov",
            revs=revs, group=G, gap="r1–r4 not kept" if G == "FOLD" else "earlier revs not kept", **cur)
        codes.append(code)
    dcode = {"FOLD": "D-011", "HUSH": "D-013", "ONESHEET": "D-015"}[G]
    items[dcode]["group"] = G
    groups.append({"code": G, "title": "ONE SHEET" if G == "ONESHEET" else G, "rev": grev, "status": "locked in v1.1", "stage": "Lock",
                   "date": "13 Nov", "line": line, "lead": codes[0], "images": codes, "docs": [dcode], "legacy": True,
                   "revs": ([{"rev": "C", "line": "v1.1 · stands at 120°, joystick, MIDI IN"}, {"rev": "B", "line": "v1 · first lock"}, {"rev": "A", "line": "round 5"}]
                            if G == "FOLD" else [{"rev": "B", "line": "v1.1 · joystick in every view"}, {"rev": "A", "line": "v1 · first lock"}])})
for G, path, line in [("FOLD113", "archive/fold-superseded/mock-A-look-113.png", "FOLD at 113°, superseded by FOLD-105 in round 5"),
                      ("TYPECASE", "archive/paused-concepts/type-case/mock-A-look.png", "letterpress type case · paused after round 3"),
                      ("HYMNAL", "archive/paused-concepts/hymnal/mock-A-look.png", "cigar-box hymnal · paused after round 3"),
                      ("UNDERGLASS", "archive/paused-concepts/under-glass/mock-A-look.png", "parts under glass · killed in round 2")]:
    if not os.path.exists(P(path)): continue
    code = G + "-A"
    m = jpg(path, code, 1600, 72)
    add(code, kind="image", sub="legacy sheet", title="The look", stage="Concept", status="dropped", date="12 Nov",
        revs=[{"rev": "A", "line": "archive", **m}], group=G, **m)
    groups.append({"code": G, "title": {"TYPECASE": "TYPE CASE", "UNDERGLASS": "UNDER GLASS"}.get(G, G), "rev": "A", "status": "dropped", "stage": "Concept",
                   "date": "12 Nov" if G != "FOLD113" else "13 Nov", "line": line, "lead": code, "images": [code], "docs": [], "legacy": True,
                   "revs": [{"rev": "A", "line": "archive"}]})

FULL = [("case", "CASE"), ("dock", "DOCK"), ("dish", "DISH"), ("motto", "MOTTO"), ("slab", "SLAB")]
for folder, G in FULL:
    base = f"archive/full-instrument/concepts/{folder}/"
    if not os.path.isdir(P(base)): continue
    pngs = sorted((f for f in os.listdir(P(base)) if f.endswith(".png")), key=lambda f: ("exploded" in f, f))
    codes = []
    for f in pngs:
        code = f"FULL-{G}-{'exploded' if 'exploded' in f else 'look'}"
        m = jpg(base + f, code, 1600, 74)
        add(code, kind="image", sub="legacy sheet", title=("exploded" if "exploded" in f else "the look"), stage="Concept", status="dropped", date="12 Nov",
            revs=[{"rev": "A", "line": "full instrument (paused)", **m}], group="FULL" + G, **m)
        codes.append(code)
    docs = []
    if os.path.exists(P(base + "how-it-works.md")):
        t = rd(base + "how-it-works.md"); dc = "D-F" + G
        add(dc, kind="doc", sub="doc", title=f"{G} (full instrument) · how it works", stage="Concept", status="dropped", date="12 Nov",
            revs=[{"rev": "A", "line": "full instrument (paused)"}], path=base + "how-it-works.md", html=md(t, src=base + "how-it-works.md"), lead=first_para(t), group="FULL" + G)
        docs.append(dc)
    if codes:
        groups.append({"code": "FULL" + G, "title": G, "rev": "A", "status": "dropped", "stage": "Concept", "date": "12 Nov", "legacy": True, "full": True,
                       "line": "the full-size Model D clone, paused when Little D began", "lead": codes[0], "images": codes, "docs": docs,
                       "revs": [{"rev": "A", "line": "full instrument (paused)"}], "statusLabel": "dropped · full instrument, paused"})
for g in groups:
    if "statusLabel" not in g:
        g["statusLabel"] = {"locked in v1.1": "locked in v1.1"}.get(g["status"], "dropped · earlier round" if g["status"] == "dropped" else g["status"])

# ------------------------------------------------------------------ tests (sims serve Spec, early)
G_ = "eng/sim/reference/out/golden/"; X_ = "eng/sim/reference/out/example_perturbed/"
met = json.load(open(P(G_ + "metrics.json"))); metx = json.load(open(P(X_ + "metrics.json")))
ab = open(P("eng/sim/reference/out/ab_example_perturbed.txt")).read().splitlines()
def abcount(cat):
    p = sum(1 for l in ab if l.startswith("PASS") and l.split()[1:2] == [cat]); f = sum(1 for l in ab if l.startswith("FAIL") and l.split()[1:2] == [cat])
    return p, f
def plot(name, code, variant="golden"):
    return jpg((G_ if variant == "golden" else X_) + "plots/" + name + ".png", code + "-" + name + ("" if variant == "golden" else "-x"), 1400, 80)
vb, vx = met["voice"]["bass_pluck"], metx["voice"]["bass_pluck"]
rs, rx = met["voice"]["resonant_sweep"], metx["voice"]["resonant_sweep"]
TESTS = [
    ("T-004", "Bass pluck", "RAN", f"no limits set · osc {vb['osc_hz']:.1f} Hz · envelope peak {vb['env_peak_time_s']*1000:.0f} ms golden, {vx['env_peak_time_s']*1000:.0f} ms perturbed",
     [plot("voice_bass_pluck", "T-004")], {"golden": wav(G_ + "wav/voice_bass_pluck.wav", "T-004-golden"), "perturbed": wav(X_ + "wav/voice_bass_pluck.wav", "T-004-perturbed")}),
    ("T-005", "Resonant sweep", "RAN", f"no limits set · osc {rs['osc_hz']:.1f} Hz · envelope peak {rs['env_peak_time_s']*1000:.0f} ms golden, {rx['env_peak_time_s']*1000:.0f} ms perturbed",
     [plot("voice_resonant_sweep", "T-005")], {"golden": wav(G_ + "wav/voice_resonant_sweep.wav", "T-005-golden"), "perturbed": wav(X_ + "wav/voice_resonant_sweep.wav", "T-005-perturbed")}),
    ("T-003", "Filter response (AC)", "PASS 40 · FAIL 6", "perturbed vs golden: emphasis 7 over the 0.5 dB limit at three cutoffs", [plot("filter_ac", "T-003")], None),
    ("T-001", "VCO tracking", "RAN", f"best-fit residual {met['vco_tracking']['bestfit_residual_cents_max_abs_keyboard_range']:.2f} cents max over the keyboard range", [plot("vco_tracking", "T-001")], None),
    ("T-002", "VCO waveforms", "RAN", "saw, triangle, square, narrow pulse at 110 / 440 / 1760 Hz", [plot("vco_waveforms", "T-002")], {"golden": wav(G_ + "wav/vco_saw_110_440_1760.wav", "T-002-saw")}),
    ("T-006", "Filter self-oscillation", "RAN", "self-oscillation at emphasis 10 from 20 Hz to 2 kHz", [plot("filter_selfosc", "T-006")], None),
    ("T-007", "Contours", "PASS 78", "perturbed vs golden: all 78 contour checks within limits", [plot("contours", "T-007")], None),
]
PEAKV = {"T-004": (vb["peak_v"], vx["peak_v"]), "T-005": (rs["peak_v"], rx["peak_v"])}
for code, title, word, line, plots, audio in TESTS:
    if audio:
        top = max(max(a["peaks"]) for a in audio.values())
        for k, a in audio.items():
            a["peaks"] = [round(x / top, 3) for x in a["peaks"]]
            a["peak_v"] = PEAKV[code][0 if k == "golden" else 1] if code in PEAKV else None
    add(code, kind="test", sub="sim", title=title, stage="Spec", status="current", date="13 Nov", early=True,
        revs=[{"rev": "A", "line": word + " · ngspice, golden + perturbed"}], result=word, line=line, plots=plots, audio=audio, path="eng/sim/")

# ------------------------------------------------------------------ the prototype itself (a prototype item)
add("P-001", kind="prototype", sub="prototype", title="Project site · Herbarium prototype", stage="Concept", status="exploring", date="13 Nov",
    revs=[{"rev": "A", "line": "first published version · real content, simulated live"}], path="site/design/concepts/herbarium/prototype/",
    lead="This site. It began as the E Herbarium concept's prototype and is now the project's public site on GitHub Pages.")

# ------------------------------------------------------------------ decisions (design/owner.md, verbatim)
CAUSED = {
    "Switch to Daisy Seed": [("before", "D-031"), ("after", "D-032"), ("after", "D-019", "rev 13")],
    "Check the pin thing": [("after", "D-031")],
    "Also the key thing you need to port": [("after", "D-032")],
    "Add MIDI out": [("after", "D-019")],
    "i think it needs its own switch": [("after", "D-019", "rev 14"), ("after", "D-034")],
    "I like the idea of drift": [("after", "D-019")],
    "It is not a requirement that you can change the angle": [("after", "FOLD-E")],
    "I want echo and reverb": [("after", "D-019")],
    "B": [("after", "D-019")],
}
decisions = []
date, time_ = "", None
for ln in rd("design/owner.md").splitlines():
    h = re.match(r"^## (2026-\d\d-\d\d)(?: (\d\d:\d\d))?", ln)
    if h: date, time_ = h.group(1), h.group(2); continue
    if ln.startswith("## "): date = ""; continue
    lead = re.match(r"^(2026-\d\d-\d\d)(?: (\d\d:\d\d))? ", ln)
    if lead: date, time_ = lead.group(1), lead.group(2)
    inl = re.search(r"\(verbatim, (2026-\d\d-\d\d) (\d\d:\d\d)\)", ln)
    if inl: date, time_ = inl.group(1), inl.group(2)
    if not date: continue
    q = re.search(r"Q: (.*?)\s*→\s*Owner[^:]*:\s*\"(.*?)\"", ln)
    o = re.search(r"Owner \(verbatim[^)]*\)[^\"]*\"(.*?)\"", ln)
    if q: ask, words = q.group(1), q.group(2)
    elif o: ask, words = None, o.group(1)
    else: continue
    cz = []
    for k, v in CAUSED.items():
        if (words == k) if k == "B" else words.startswith(k):
            cz = [{"ba": x[0], "code": x[1], "note": x[2] if len(x) > 2 else ""} for x in v]
    decisions.append({"date": date[5:].replace("11-", "") + " Nov", "iso": date, "time": time_, "ask": ask, "words": words, "caused": cz})
decisions.reverse()
for d in decisions:
    for c in d["caused"]:
        if c["ba"] == "after" and c["code"] in items:
            items[c["code"]].setdefault("causedBy", d["words"])

# ------------------------------------------------------------------ rounds + scores (design/scores.md; branches: design/notes/director.md)
rounds = []
sc = rd("design/scores.md")
for m in re.finditer(r"^## (Round \d)[^\n]*\((2026-\d\d-\d\d)\)(.*?)(?=^## |\Z)", sc, flags=re.S | re.M):
    rows = [(re.sub(r"\s*\(.*$", "", n.replace("*", "")).strip(), sc) for n, sc in
            re.findall(r"^\|\s*\*{0,2}([A-Z][^|]*?)\s*\|\s*\*{0,2}(\d{1,2})\*{0,2}\s*\|", m.group(3), flags=re.M)]
    seen, rr = set(), []
    for n, s in rows:
        n = n.strip()
        if n not in seen: seen.add(n); rr.append([n, int(s)])
    rounds.append({"name": m.group(1), "date": m.group(2)[8:] + " Nov", "scores": rr[:8]})
rounds.append({"name": "Branches round 1", "date": "13 Nov", "scores": [["CHAMBER", 8], ["RAIN", 7], ["BUTTERFLY", 6], ["DIPTYCH", 0]],
               "notes": {"BUTTERFLY": "retired", "DIPTYCH": "killed"}})

versions = [
    {"code": "v1-1", "name": "v1.1", "date": "13 Nov", "current": True, "line": re.search(r"\*\*v1\.1\*\* \(current\) \| [^|]+\| ([^|]+)\|", rd("VERSIONS.md")).group(1).strip(),
     "groups": [["FOLD", "C"], ["HUSH", "B"], ["ONESHEET", "B"]], "docs": ["D-003", "D-011", "D-013", "D-015", "D-019", "R-001", "R-002"]},
    {"code": "v1", "name": "v1", "date": "13 Nov", "line": "First official lock: HUSH, ONE SHEET and FOLD after round 5, all scored 9.",
     "groups": [["FOLD", "B"], ["HUSH", "A"], ["ONESHEET", "A"]], "docs": ["D-019", "R-001", "R-002"]},
]

# ------------------------------------------------------------------ events (history), newest first; times where the records have them
events = [
    {"d": "13 Nov", "t": "13:20", "k": "made", "line": "Herbarium prototype published as the site's first version", "codes": ["P-001"]},
    {"d": "13 Nov", "t": None, "k": "revised", "line": "CHAMBER and RAIN rev B: round 2 fixes (re-score pending)", "codes": ["CHAMBER", "RAIN"], "round": "Branches round 2"},
    {"d": "13 Nov", "t": "13:09", "k": "scored", "line": "Branches round 1: CHAMBER 8, RAIN 7, BUTTERFLY 6 (retired), DIPTYCH killed", "codes": ["CHAMBER", "RAIN", "BUTTERFLY", "DIPTYCH"], "round": "Branches round 1"},
    {"d": "13 Nov", "t": "12:29", "k": "made", "line": "Branch concepts made: CHAMBER, RAIN, BUTTERFLY, DIPTYCH (rev A each)", "codes": ["CHAMBER", "RAIN", "BUTTERFLY", "DIPTYCH"], "round": "Branches round 1"},
    {"d": "13 Nov", "t": "11:47", "k": "decided", "line": "Branched creative rounds started", "round": "Branches round 1"},
    {"d": "13 Nov", "t": "11:41", "k": "made", "line": "Repo restructured: versions/, design/, archive/"},
    {"d": "13 Nov", "t": None, "k": "locked", "line": "Locked v1.1: FOLD at 120°, joystick in every view, MIDI IN", "codes": ["FOLD", "HUSH", "ONESHEET"], "version": "v1-1"},
    {"d": "13 Nov", "t": None, "k": "locked", "line": "Locked v1: HUSH, ONE SHEET, FOLD after round 5", "codes": ["FOLD", "HUSH", "ONESHEET"], "version": "v1"},
    {"d": "13 Nov", "t": None, "k": "test", "line": "Sims ran: golden + perturbed (T-001 to T-007)", "codes": ["T-004", "T-005", "T-003"]},
    {"d": "13 Nov", "t": None, "k": "scored", "line": "Round 5 scored: HUSH 9, ONE SHEET 9, FOLD-105 9", "round": "Round 5"},
    {"d": "12 Nov", "t": "22:30", "k": "scored", "line": "Round 4 scored", "round": "Round 4"},
    {"d": "12 Nov", "t": None, "k": "scored", "line": "Round 3 scored", "round": "Round 3"},
    {"d": "12 Nov", "t": None, "k": "scored", "line": "Round 2 scored: six concepts", "round": "Round 2"},
    {"d": "12 Nov", "t": None, "k": "scored", "line": "Round 1 scored", "round": "Round 1"},
]

def h1(t):
    m = re.search(r"^# (.+)$", t, flags=re.M); return m.group(1).strip() if m else ""
readme = rd("docs/README.md")
covers = {}
for m in re.finditer(r"^\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$", readme, flags=re.M):
    covers[os.path.normpath(os.path.join("docs", m.group(2)))] = (m.group(3), re.sub(r"[*`]", "", m.group(4)))
docs_site = []
for slug, path in SITE_DOCS:
    t = rd(path); hh = md(t, src=path, status=True)
    cov, written = covers.get(path, ("", ""))
    stub = "not yet written" in t.split("\n", 3)[1] if t.count("\n") > 1 else True
    cnt = {w: len(re.findall(rf'class="st st-{w}"', hh)) for w in ("decided", "proposed", "open")}
    docs_site.append({"slug": slug, "path": path, "title": h1(t) or slug, "covers": cov, "written": written or ("not yet written" if stub else "written"),
                      "stub": stub, "counts": cnt, "html": hh, "jump": [h for h, _ in sections(t) if h][:40], "lead": first_para(t)})
reviews = []
for slug, path in REVIEWS:
    t = rd(path)
    sc = re.search(r"\*\*(\d+ / 10)\*\*", t)
    reviews.append({"slug": slug, "path": path, "title": h1(t), "date": slug[:10], "score": sc.group(1) if sc else "", "lead": first_para(t),
                    "html": md(t, src=path), "jump": [h for h, _ in sections(t) if h][:40]})
wtxt = rd("design/decisions-open.md") if os.path.exists(P("design/decisions-open.md")) else ""
wparts = re.split(r"^## ", wtxt, flags=re.M)
waiting = {"intro": md(re.sub(r"^# .*\n", "", wparts[0]).replace("---", ""), src="design/decisions-open.md") if wparts else "", "items": []}
for part in wparts[1:]:
    head, _, body = part.partition("\n")
    m = re.match(r"(\d+)\.\s*(.*)", head.strip())
    n, title = (m.group(1), m.group(2)) if m else ("", head.strip())
    unb = re.search(r"\*\*Unblocks:\*\*\s*(.+)", body)
    rec = re.search(r"([^\n]*?)\s*\*(?:Team recommends|Visual designer's pick)[^*]*\*", body)
    waiting["items"].append({"n": n, "title": title, "unblocks": unb.group(1).strip() if unb else "",
                             "html": md(body.replace("\n---", "").strip(), src="design/decisions-open.md")})
ownertests = ""
_cw = rd("design/branches/concepts/cathedral/how-it-works.md") if os.path.exists(P("design/branches/concepts/cathedral/how-it-works.md")) else ""
_m = re.search(r"### Two buy-and-test checks[^\n]*\n(.*?)(?=\n>\s*###|\n## )", _cw, flags=re.S)
if _m:
    ownertests = md("\n".join(l[1:].lstrip() if l.startswith(">") else l for l in _m.group(1).splitlines()), src="design/branches/concepts/cathedral/how-it-works.md")
import subprocess, tempfile
_tmp = tempfile.mkdtemp()
def blob(commit, path, name, long=1400):
    """downscaled copy of an image as it was at an earlier commit (git history); None if that commit isn't here"""
    out = os.path.join(_tmp, os.path.basename(path))
    r = subprocess.run(["git", "-C", ROOT, "show", f"{commit}:{path}"], capture_output=True)
    if r.returncode: return None
    open(out, "wb").write(r.stdout)
    return jpg(out, name, long, 80)
CI = "design/branches/concepts/cathedral/img/"
def step_imgs(spec):
    res = []
    for commit, f, cap in spec:
        nm = "STEP-" + (commit or "now") + "-" + os.path.splitext(f)[0].replace("cathedral-", "")
        m = (jpg(CI + f, nm, 1400, 80) if os.path.exists(P(CI + f)) else None) if commit is None else blob(commit, CI + f, nm)
        if m: res.append({**m, "cap": cap})
    return res
TIMELINE = {"CATHEDRAL": [
    {"t": "13 Nov 21:06", "name": "Steer 5 (now): both halves by one rule",
     "what": "Two lid options on one shared two-row base: P5O, your stacked oscillators on the left, and P5R, the same rule laid in rows. Softer corners, the spine back, lines for the grille.",
     "why": "You (20:29): the lid felt cramped; tuning should sit by the oscillators, mixer and volume on the bottom case. You (20:43): “I feel like the oscillators should all be stacked on the left…”",
     "score": "P5R 8 · P5O 6 · shared base 7 (bar 10)",
     "imgs": step_imgs([(None, "cathedral-s5-P5R-standing.jpg", "P5R standing"), (None, "cathedral-s5-P5O-standing.jpg", "P5O standing")])},
    {"t": "13 Nov 20:07", "name": "One-word labels",
     "what": "Every panel label cut to one word.", "why": "Your rule (19:57): “Labels should only be one word and follow best practices…”", "score": "",
     "imgs": step_imgs([("fec6093", "cathedral-lid-signal-order-8.7px-per-mm.png", "the lid with one-word labels, exact top view")])},
    {"t": "13 Nov 19:55", "name": "Steer 4: the panel explains itself",
     "what": "The synth expert's fixes: words for every switch position, release, echo pan and follow legends.",
     "why": "You (19:31), on the expert's fixes: “Yes but make it a 10 not a 9”.", "score": "8, then 9 after fixes (bar 10)",
     "imgs": step_imgs([("4e52223", "cathedral-nave-standing.jpg", "standing"), ("4e52223", "cathedral-lid-signal-order-8.7px-per-mm.png", "the lid, exact top view")])},
    {"t": "13 Nov 18:29", "name": "Steer 3: the lid in signal order",
     "what": "The lid regrouped in the order sound travels: oscillators, mixer, filter, amp, effects, out.",
     "why": "You (18:00): “the items do not appear to be grouped or ordered in a way that makes logical sense”.", "score": "9 (confirmed 19:00)",
     "imgs": step_imgs([("970a017", "cathedral-lid-signal-order-8.7px-per-mm.png", "the lid in signal order, exact top view")])},
    {"t": "13 Nov 17:27", "name": "Steer 2: the lid rebuilt",
     "what": "Three even lid rows, the speaker behind a window, brass keys in metal.",
     "why": "The speaker band had been leftover space; the director had the layout rebuilt, not restyled.", "score": "8",
     "imgs": step_imgs([("5cf16b1", "cathedral-nave-standing.jpg", "standing"), ("5cf16b1", "cathedral-nave-top-8.3px-per-mm.png", "exact top view")])},
    {"t": "13 Nov 14:12", "name": "Steer 1: CHAMBER and FOLD become CATHEDRAL",
     "what": "The middle ground of CHAMBER and FOLD-105: layouts A and B, then the speaker grille options.",
     "why": "You (14:12): “i want to lock in on cathedral and fold right now… so i can find the best middle ground”.", "score": "",
     "imgs": step_imgs([("40f9648", "cathedral-B-standing.jpg", "layout B, standing"), ("40f9648", "cathedral-A-standing.jpg", "layout A, standing"), ("40f9648", "cathedral-speaker-options-standing.jpg", "speaker grille options")])},
  ],
  "CHAMBER": [{"t": "13 Nov 14:12", "name": "Became CATHEDRAL", "what": "Merged with FOLD-105 into CATHEDRAL.", "why": "You chose CHAMBER and FOLD as the two to find a middle ground between.", "score": ""},
              {"t": "13 Nov", "name": "Rev B: round 2 fixes", "what": "The branches director's fixes to rev A.", "why": "", "score": "9"},
              {"t": "13 Nov 13:09", "name": "Rev A: branches round 1", "what": "FOLD-105 as an organ case: closed it's a case, open it's a console.", "why": "", "score": "8"}],
  "RAIN": [{"t": "13 Nov 14:12", "name": "Paused", "what": "Set aside when you focused on CHAMBER and FOLD.", "why": "", "score": ""},
           {"t": "13 Nov", "name": "Rev B: round 2 fixes", "what": "The branches director's fixes; not re-scored.", "why": "", "score": ""},
           {"t": "13 Nov 13:09", "name": "Rev A: branches round 1", "what": "ONE SHEET as a pond after rain.", "why": "", "score": "7"}],
  "BUTTERFLY": [{"t": "13 Nov 13:09", "name": "Retired", "what": "ONE SHEET with a walnut top; retired by the branches director.", "why": "CHAMBER and RAIN already covered both of your leans.", "score": "6"}],
  "DIPTYCH": [{"t": "13 Nov 13:09", "name": "Killed", "what": "A scientific field instrument; killed by the branches director.", "why": "", "score": ""}],
}
ALIAS = {"FOLD": ["FOLD", "FOLD-105"], "ONESHEET": ["ONE SHEET"], "HUSH": ["HUSH"], "TYPECASE": ["TYPE CASE"], "HYMNAL": ["HYMNAL"], "UNDERGLASS": ["UNDER GLASS"], "FOLD113": ["FOLD-113"]}
for gc, names in ALIAS.items():
    tl = []
    for r in reversed(rounds):
        for n, sc in r["scores"]:
            if n in names: tl.append({"t": r["date"], "name": r["name"], "what": "", "why": "", "score": str(sc)})
    if gc in ("FOLD", "HUSH", "ONESHEET"):
        tl = [{"t": "13 Nov", "name": "Locked in v1.1", "what": versions[0]["line"], "why": "", "score": ""},
              {"t": "13 Nov", "name": "Locked in v1", "what": "First official lock after round 5.", "why": "", "score": ""}] + tl
    if gc == "FOLD": tl.insert(0, {"t": "13 Nov 14:12", "name": "Grew into CATHEDRAL", "what": "FOLD-105 and CHAMBER became CATHEDRAL.", "why": "", "score": ""})
    if gc == "ONESHEET": tl.insert(0, {"t": "13 Nov", "name": "Seeded RAIN and BUTTERFLY", "what": "Two branches grew from ONE SHEET.", "why": "", "score": ""})
    TIMELINE[gc] = tl
for g in groups:
    g["timeline"] = TIMELINE.get(g["code"]) or ([{"t": g["date"], "name": "Full instrument, paused" if g.get("full") else "Archived", "what": g["line"], "why": "", "score": ""}])
SUMMARY = {"CATHEDRAL": "In progress: two lid options, P5O and P5R, on one shared base. Last scores: P5R 8, P5O 6 (bar 10).",
           "CHAMBER": "Became CATHEDRAL", "RAIN": "Paused · scored 7", "FOLD": "Locked in v1.1 · grew into CATHEDRAL",
           "ONESHEET": "Locked in v1.1", "HUSH": "Locked in v1.1", "BUTTERFLY": "Dropped · retired at 6", "DIPTYCH": "Dropped · killed"}
for g in groups:
    if g["code"] in SUMMARY: g["statusLabel"] = SUMMARY[g["code"]]
try:
    gl = subprocess.run(["git", "-C", ROOT, "log", "-1", "--format=%ad|%s", "--date=format:%d %b %H:%M"], capture_output=True, text=True).stdout.strip().split("|", 1)
    updated = {"when": gl[0].lstrip("0"), "what": gl[1]}
except Exception:
    updated = {"when": "", "what": ""}
docs_index = {"intro": md("\n".join(l for l in readme.split("## Index")[0].splitlines()[1:]), src="docs/README.md"),
              "template": md("## Template" + readme.split("## Template", 1)[1], src="docs/README.md") if "## Template" in readme else ""}

data = {"project": {"name": "Big Energy", "line": "a portable Model D", "waiting": "CATHEDRAL approval", "then": "then the handoff",
                    "current": "v1-1", "now": "Lock", "next": "Handoff", "published": "13 Nov 13:20", "last": "CHAMBER rev B"},
        "stages": ["Concept", "Lock", "Handoff", "Spec", "BOM", "Breadboard", "Boards", "Prints", "Assembly"],
        "groups": groups, "items": items, "order": order, "decisions": decisions, "rounds": rounds, "versions": versions,
        "events": events, "clouds": cl, "docs": docs_site, "docsIndex": docs_index, "reviews": reviews, "updated": updated, "waiting": waiting, "ownertests": ownertests}

# the lightbox: Ramka in a React island (lightbox/), bundled to vendor/lightbox/lightbox.js; copied as a static file
import shutil
VEND = os.path.join(HERE, "vendor", "lightbox")
os.makedirs(os.path.join(MEDIA, "vendor"), exist_ok=True)
shutil.copyfile(os.path.join(VEND, "lightbox.js"), os.path.join(MEDIA, "vendor", "lightbox.js"))
USED.add("vendor/lightbox.js")
data["licenses"] = [{"name": "Image viewer: Ramka (@ramka/react 0.0.2), React 18.3.1", "url": "https://ramka.dev",
                     "text": open(os.path.join(VEND, "LICENSES.txt"), encoding="utf-8").read()}]
tpl = open(os.path.join(HERE, "app.html"), encoding="utf-8").read()

js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(tpl.replace("/*DATA*/", js))
for dp, _, fs in os.walk(MEDIA):
    for f in fs:
        rel = os.path.relpath(os.path.join(dp, f), MEDIA)
        if rel not in USED: os.remove(os.path.join(dp, f))   # stale copies from earlier builds
tot = sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(HERE) for f in fs if not f.endswith(".py"))
print(f"items {len(items)} · groups {len(groups)} · decisions {len(decisions)} · rounds {len(rounds)} · total {tot/1048576:.2f} MiB")
