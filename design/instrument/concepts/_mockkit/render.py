"""Render SVG files to PNG with headless Chrome (fonts: Kalam/Inter via fontconfig)."""
import sys, pathlib, re
from playwright.sync_api import sync_playwright


def render(svg_paths, scale=1.0):
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        for sp in svg_paths:
            sp = pathlib.Path(sp).resolve()
            head = sp.read_text()[:400]
            w = int(float(re.search(r'width="([\d.]+)"', head).group(1)))
            h = int(float(re.search(r'height="([\d.]+)"', head).group(1)))
            pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=scale)
            pg.goto(sp.as_uri())
            pg.wait_for_timeout(300)
            out = sp.with_suffix(".png")
            pg.screenshot(path=str(out), full_page=False)
            pg.close()
            print("wrote", out)
        b.close()


if __name__ == "__main__":
    render(sys.argv[1:])
