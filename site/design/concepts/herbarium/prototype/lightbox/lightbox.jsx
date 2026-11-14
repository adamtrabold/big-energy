// The site's image lightbox: Ramka (MIT, Copyright (c) 2026 Artur Bień) in a small React island.
// The page is vanilla JS. After each render it calls window.BELightbox.set(items, imgs):
//   items: [{src, alt, caption, width, height}]  (one gallery per page, page order)
//   imgs:  the page's <img> elements, same order. Each gets a Ramka Trigger overlaid on it, so tapping
//          opens the viewer and the image morphs from its place (view transitions where supported).
import * as React from "react";
import { createRoot } from "react-dom/client";
import { createPortal } from "react-dom";
import * as Lightbox from "@ramka/react/lightbox";

const handle = Lightbox.createHandle();

function Attach({ img, imageRef }) {
  // the existing page <img> bridges the open transition (its decoded pixels are the placeholder)
  React.useLayoutEffect(() => { imageRef(img); return () => imageRef(null); }, [img, imageRef]);
  return null;
}

function TriggerOverlay({ img, index, label }) {
  return (
    <Lightbox.Trigger handle={handle} id={"lbt-" + index} index={index} className="lb-trigger" aria-label={label}>
      {({ imageRef }) => <Attach img={img} imageRef={imageRef} />}
    </Lightbox.Trigger>
  );
}

function hostFor(img) {
  // a positioned wrapper around the image, holding the overlay button
  let wrap = img.parentElement;
  if (!wrap || !wrap.classList.contains("lb-wrap")) {
    wrap = document.createElement("span");
    wrap.className = "lb-wrap";
    img.replaceWith(wrap);
    wrap.appendChild(img);
  }
  let host = wrap.querySelector(":scope > .lb-host");
  if (!host) { host = document.createElement("span"); host.className = "lb-host"; wrap.appendChild(host); }
  return host;
}

function App() {
  const [st, setSt] = React.useState({ items: [], imgs: [], key: 0 });
  React.useEffect(() => {
    window.BELightbox = {
      set(items, imgs) { setSt({ items, imgs: imgs.map((im) => ({ im, host: hostFor(im) })), key: Date.now() }); },
      open(i) { handle.open(i, { triggerId: "lbt-" + i }); },
    };
    document.dispatchEvent(new Event("belightbox-ready"));
  }, []);
  const { items, imgs, key } = st;
  const n = items.length;
  return (
    <Lightbox.Root handle={handle} count={n} viewTransition loop={false} key={key}>
      {imgs.map(({ im, host }, i) => createPortal(<TriggerOverlay img={im} index={i} label={"View image " + (i + 1) + " of " + n + (items[i] && items[i].alt ? ": " + items[i].alt : "")} />, host, "t" + i))}
      <Lightbox.Portal>
        <Lightbox.Backdrop className="lb-backdrop" />
        <Lightbox.Content className="lb-content" aria-label="Image viewer" pullToClose>
          <Lightbox.Slides className="lb-slides" aria-label="Images on this page" aria-roledescription="carousel">
            {items.map((it, i) => (
              <Lightbox.Slide key={i} className="lb-slide">
                <Lightbox.Item index={i} caption={it.caption} className="lb-item" aria-roledescription="slide" aria-label={(i + 1) + " of " + n}>
                  <Lightbox.Zoom className="lb-zoom" maxZoom={4}>
                    <Lightbox.Media className="lb-media" width={it.width} height={it.height}>
                      <img src={it.src} alt={it.alt} width={it.width} height={it.height} draggable={false} />
                    </Lightbox.Media>
                  </Lightbox.Zoom>
                </Lightbox.Item>
              </Lightbox.Slide>
            ))}
          </Lightbox.Slides>
          <div className="lb-bar">
            <Lightbox.Counter className="lb-counter">{({ current, total }) => current + " / " + total}</Lightbox.Counter>
            <Lightbox.Close className="lb-btn lb-close" aria-label="Close">Close</Lightbox.Close>
          </div>
          <Lightbox.Previous className="lb-nav lb-prev" aria-label="Previous image">‹</Lightbox.Previous>
          <Lightbox.Next className="lb-nav lb-next" aria-label="Next image">›</Lightbox.Next>
          <Lightbox.Caption className="lb-caption" />
        </Lightbox.Content>
      </Lightbox.Portal>
    </Lightbox.Root>
  );
}

const mount = document.createElement("div");
mount.id = "belightbox";
document.body.appendChild(mount);
createRoot(mount).render(<App />);
