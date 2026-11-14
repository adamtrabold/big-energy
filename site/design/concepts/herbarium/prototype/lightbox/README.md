# Lightbox island
The site's image viewer: Ramka (`@ramka/react/lightbox`) in a small React island, bundled into one static file, `../vendor/lightbox/lightbox.js`, which `build.py` copies to `media/vendor/`. No CDN.
Rebuild after changing `lightbox.jsx`: `npm install && npm run build` here, then `python3 ../build.py`.
API used by the page (vanilla JS): `window.BELightbox.set(items, imgs)` after each page render, where `items` = [{src, alt, caption, width, height}] and `imgs` are the page's `<img>` elements, in the same order.
Licences: `../vendor/lightbox/LICENSES.txt` (shown on the site at #licenses).
