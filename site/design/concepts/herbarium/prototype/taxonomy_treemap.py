"""Control taxonomy treemap (HTML/CSS, no image), generated from docs/control-taxonomy.md so it stays in sync.

Reads the tree (section 2) for branch names and the per-control table (section 3) for each control's branch, job and
half. Boxes are sized by their number of panel controls: categories share a row by width, sub-categories share a
category by height, and each row's height follows its control count, so every control gets about the same area.
"""
import html
import re

JOBS = [("set once", "set"), ("shape", "shape"), ("play", "play"), ("level", "level")]   # doc wording -> css key
JOB_LABEL = {"set": "set once", "shape": "shape", "play": "play", "level": "level / output"}
ROWS = [["1", "2", "3"], ["4", "5", "6"]]       # Model D order, left to right; two rows on a desktop


def _clean(s):
    return re.sub(r"[*`]", "", s).strip()


def _job_keys(s):
    keys = []
    for part in re.split(r"\s*/\s*", _clean(s)):
        for word, key in JOBS:
            if part.startswith(word) and key not in keys:
                keys.append(key)
    return keys or ["set"]


def parse(md_text):
    tree = md_text.split("```", 2)[1] if "```" in md_text else ""
    names, star = {}, set()
    for line in tree.splitlines():
        m = re.search(r"[├└]── (\d[a-e]?)\s+([^(:]+?)\s*\(", line)
        if not m:
            continue
        code, name = m.group(1), m.group(2).strip()
        names[code] = name.capitalize() if name.isupper() else name
        if re.search(r"\)\s*★", line):
            star.add(code)
    controls = []
    sec3 = md_text.split("## 3.", 1)[1].split("\n## ", 1)[0] if "## 3." in md_text else ""
    for row in sec3.splitlines():
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) < 6 or not re.match(r"^\d", cells[0]):
            continue
        num, ctl, branch, what, job, half = cells[:6]
        a, _, b = num.partition("–")
        n = int(b) - int(a) + 1 if b else 1
        bold = re.findall(r"\*\*(.+?)\*\*", ctl)
        if len(bold) == n:
            items = [_clean(x) for x in bold]
        else:
            first = _clean(bold[0] if bold else ctl)
            parts = [p.strip() for p in first.split(" · ")]
            if n > 1 and len(parts) == n:
                head = parts[0].split(" ")
                items = [head[-1]] + parts[1:]
            else:
                items = [first]
        jobs = [j.strip() for j in _clean(job).split(" · ")]
        jobs = jobs if len(jobs) == len(items) else [_clean(job)] * len(items)
        optional = branch.startswith("2d") or "optional" in what.lower()
        for it, jb in zip(items, jobs):
            it = re.sub(r"\s*\(.*?\)$", "", it)                       # "bend (joystick)" -> "bend"
            controls.append({"name": it, "branch": branch, "jobs": _job_keys(jb), "job_text": jb,
                             "half": "lid" if half.startswith("lid") else "base", "optional": optional, "what": _clean(what)})
    return names, star, controls


def build(md_text):
    names, star, controls = parse(md_text)
    if not controls:
        return ""
    total, opt = len(controls), sum(c["optional"] for c in controls)
    cats = {}
    for c in controls:
        top = c["branch"][0]
        cats.setdefault(top, {}).setdefault(c["branch"], []).append(c)
    E = html.escape

    def short(c):
        """the name inside its box, without what the box already says ("echo type" in Echo -> "type", "octave 1" in
        Oscillator 1 -> "octave", "mixer 4" in the mixer -> "4")."""
        nm, box = c["name"], names.get(c["branch"], "").lower()
        first = box.split(" ")[0] if box else ""
        if first and nm.lower().startswith(first + " "):
            nm = nm[len(first) + 1:]
        if nm.lower().startswith("mixer "):
            nm = nm[6:]
        m = re.match(r"oscillator (\d)", box)
        if m and nm.endswith(" " + m.group(1)) and not nm.startswith("track"):
            nm = nm[:-2]
        return nm

    def chip(c, show_half):
        j = c["jobs"]
        cls = "tm-c tm-" + j[0] + (" tm-opt" if c["optional"] else "")
        style = ""
        if len(j) > 1:
            style = f' style="--j2:var(--tm-{j[1]})"'
            cls += " tm-two"
        tip = f'{c["name"]}: {c["job_text"]}; {c["half"]}. {c["what"]}'
        half = f'<i class="tm-h">{c["half"]}</i>' if show_half else ""
        return f'<span class="{cls}"{style} title="{E(tip)}">{E(short(c))}{half}</span>'

    def box(code, items, level):
        halves = sorted({c["half"] for c in items}, key=lambda h: (h != "lid", h))
        mixed = len(halves) > 1
        n = len(items)
        n_req = sum(not c["optional"] for c in items)
        cnt = f"{n}" if n == n_req or n_req == 0 else f"{n_req} + {n - n_req}"
        opt = all(c["optional"] for c in items)
        name = names.get(code, code)
        st = " ★" if code in star else ""
        tag = " · ".join(halves)
        return (f'<div class="tm-sub{" tm-sub-opt" if opt else ""}" style="flex-grow:{n}">'
                f'<div class="tm-hd"><b>{E(code)} {E(name)}{st}</b><span class="tm-n">{cnt}</span><span class="tm-tag tm-{halves[0] if not mixed else "mix"}">{E(tag)}</span></div>'
                f'<div class="tm-cs">{"".join(chip(c, mixed) for c in items)}</div></div>')

    rows_html = []
    for row in ROWS:
        cells, row_n = [], 0
        for top in row:
            subs = cats.get(top, {})
            n = sum(len(v) for v in subs.values())
            row_n += n
            name = names.get(top, top)
            st = " ★" if top in star else ""
            if list(subs) == [top]:                       # a category with no sub-categories (the mixer)
                inner = box(top, subs[top], 1).replace(f"<b>{top} {E(name)}{st}</b>", "<b>controls</b>", 1)
            else:
                inner = "".join(box(code, items, 2) for code, items in sorted(subs.items()))
            cells.append(f'<section class="tm-cat" style="flex-grow:{n}"><h3><span>{E(top)} {E(name)}{st}</span><span class="tm-n">{n}</span></h3>'
                         f'<div class="tm-subs">{inner}</div></section>')
        rows_html.append(f'<div class="tm-row" style="--rn:{row_n}">{"".join(cells)}</div>')
    legend = "".join(f'<span class="tm-c tm-{k}">{E(v)}</span>' for k, v in JOB_LABEL.items())
    legend += '<span class="tm-c tm-shape tm-two" style="--j2:var(--tm-play)">two jobs</span><span class="tm-c tm-set tm-opt">optional (VCO 4)</span>'
    return f'''<style>
.tm{{--tm-set:#E4E4E4;--tm-shape:#BFCDD6;--tm-play:#E9A55B;--tm-level:#A9C2A4;margin:6px 0 26px}}
.tm-legend{{display:flex;flex-wrap:wrap;gap:6px 8px;align-items:center;margin:8px 0 12px;font-size:12.5px;color:var(--ink2)}}
.tm-rows{{display:flex;flex-direction:column;gap:6px}}
.tm-row{{display:flex;gap:6px;min-height:calc(var(--rn) * 11.5px)}}
.tm-cat{{flex-basis:0;min-width:0;display:flex;flex-direction:column;background:var(--paper);border:1px solid var(--rule);border-radius:6px;padding:8px}}
.tm-cat h3{{display:flex;justify-content:space-between;gap:8px;margin:0 0 6px;font-size:12px;font-weight:600;letter-spacing:.07em;text-transform:uppercase}}
.tm-subs{{flex:1;display:flex;flex-direction:column;gap:5px}}
.tm-sub{{flex-basis:auto;flex-shrink:0;display:flex;flex-direction:column;border:1px solid var(--rule);border-radius:4px;padding:5px 6px;background:var(--cell)}}
.tm-sub-opt{{border-style:dashed;background:transparent}}
.tm-hd{{display:flex;align-items:baseline;gap:6px;font-size:12.5px;margin-bottom:4px}}
.tm-hd b{{font-weight:600}}
.tm-n{{color:var(--ink2);font-size:11.5px;font-variant-numeric:tabular-nums}}
.tm-tag{{margin-left:auto;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink2);border:1px solid var(--rule);border-radius:9px;padding:0 6px;white-space:nowrap}}
.tm-tag.tm-base{{color:var(--ink);border-color:var(--ink2)}}
.tm-cs{{display:flex;flex-wrap:wrap;gap:4px}}
.tm-c{{font-size:12.5px;line-height:1.2;padding:3px 7px;border-radius:3px;background:var(--tm-set);color:var(--ink);white-space:nowrap}}
.tm-c.tm-shape{{background:var(--tm-shape)}}.tm-c.tm-play{{background:var(--tm-play)}}.tm-c.tm-level{{background:var(--tm-level)}}
.tm-c.tm-two{{box-shadow:inset -7px 0 0 var(--j2);padding-right:12px}}
.tm-c.tm-opt{{background:transparent;outline:1.3px dashed var(--ink2);outline-offset:-1.3px}}
.tm-h{{font-style:normal;font-size:10px;color:var(--ink2);margin-left:5px;letter-spacing:.04em}}
.tm-note{{font-size:12.5px;color:var(--ink2);margin-top:8px}}
@media (max-width:760px){{.tm-row{{flex-direction:column;min-height:0}}.tm-cat{{flex-grow:0!important}}.tm-sub{{min-height:0;flex-grow:0!important}}}}
</style>
<figure class="tm" aria-label="Treemap of the {total} panel controls by category">
<div class="tm-legend"><b style="color:var(--ink)">Job</b>{legend}</div>
<div class="tm-rows">{"".join(rows_html)}</div>
<figcaption class="tm-note">{total} panel controls ({total - opt} without the optional VCO 4), in the Model D's left-to-right order. Each box is sized by its number of controls; each control is coloured by its job (a second job as the stripe at its right); each box is tagged with the half it sits on today (P5RS), and a box spanning both halves names each control's half. ★ = an addition to the Model D. Generated from the table below.</figcaption>
</figure>'''
