# synths-to-go: principles and goals

**Read this before working on any instrument.** These are Adam's foundational decisions for the whole family. They aren't reopened per instrument. Each line quotes Adam with its date; the full verbatim record is `design/owner.md`. Only Adam changes this file's substance; agents may fix wording or add a new principle he has stated, with its quote and date.

What isn't here (targets, part choices, sizes, features) belongs in each instrument's own requirements, such as `floss/REQUIREMENTS.md`. A number or feature an agent proposed is a proposal, not a principle, even after Adam confirms it as a working baseline.

## What synths-to-go is
A family of portable synthesizers that Adam designs with an agent team and builds himself.
- **The sound:** "Analog voices, shimmer and warmth" (2026-11-21).
- **The instruments so far:** big energy (a Model D-style voice with 4-voice paraphony), port-a-poly (a true analog poly) and floss (a string machine). Names are lowercase on the site (2026-11-21).

## 1. Portable
- Portability is a primary goal: "The principles are portable." (2026-11-22). There's no fixed weight number: "I didn’t create the weight target." Lighter is better, weighed as a trade-off.
- It fits comfortably in a backpack (2026-11-22).
- It's played away from a desk: "i want to take this to the park and be inspired" (2026-11-13).
- A keyboard counts as portable at 25 keys or fewer: "Portable means 25 or less." (2026-11-21)

## 2. Harmonious proportion
- Size and shape follow from the thing, in a deliberate ratio: "It should be a thoughtful ratio base", and "it also does not have to be a rectangle" (2026-11-22).
- "It just needs to be portable and make sense and be harmonious" (2026-11-22).
- Grids and scales derive from the device's own dimensions: "Ideally it’d be derived from the dimensions of the device as well" / "I would rather base it on the face dimensions / ratio" (2026-11-14). He asked for "a more pleasing and harmonious case ratio" (2026-11-14).
- **Examples aren't targets.** "don’t anchor on the page size thing. I’m just giving examples of generic things." (2026-11-22). When Adam names a generic object (a sheet of paper, an OP-1), treat it as a loose reference, never a dimension.

## 3. A sound module and a carried keyboard (the system)
- "This is the plan for all modular portable synths that we build — portable sound modules with a way to carry a keyboard with it. It should be flexible and not reliant on a single model of keyboard." (2026-11-22)
- It applies to every instrument, Big Energy included: "this is a systems philosophy decision" (2026-11-22).
- **No built-in keys or buttons on the module:** "No hybrid." (2026-11-22)
- The module is sized by its own needs: "The module does not have to match keyboard width" (2026-11-22).
- Any class-compliant USB MIDI keyboard works over **USB-C**, with the module as host ("Let’s do USB c", 2026-11-22). The way of carrying and connecting a keyboard is one family standard.

## 4. A shared universe
- "Yes let’s make these as a shared universe and reuse as much as we can" (2026-11-22). Parts, construction, interfaces and visual language carry across instruments. Work done for one is reusable by the others: "We can reuse anything we do here there." (2026-11-22)

## 5. Design from the idea of the thing
- "Design principles with a solid basis of logic in the idea of the thing." Each enclosure is "coherent in form with some clear perspective" (2026-11-12). That means a real point of view, not decoration.
- Inspiration: principles of furniture design, instruments, tools, "artistic inspirational forms and emotion" (2026-11-13).
- Explore broadly, with real randomness in creative rounds ("using the randomness principles", 2026-11-13). "Nods are fine but I want to see breadth of explorstion" (2026-11-12): nod to classics, don't copy them.

## 6. Panels make sense
- Controls are grouped and ordered by logic: "when i think of signal order it's synth stuff -> fx stuff -> output stuff like volume" (2026-11-13).
- Related controls sit together; for example, the effects controls sit with their output, and tuning sits near the oscillators (2026-11-13).
- No arbitrary asymmetry in the middle of a face: "off center in that middle section is bad looking" (2026-11-13).
- Section separation shouldn't get in the way of hands: "Use another method of separation if you think it's important to feel the sections" (2026-11-12).

## 7. Build: Adam builds it, and agents do the rest
- Adam builds every instrument himself: "I *am* building this so I want something feasible." (2026-11-22). No machining by Adam (2026-11-13).
- **Agents only; Adam measures nothing:** "I don’t want to measure anything. I’m truly to see how far agents alone can get me." (2026-11-22). Every choice rests on published evidence (datasheets, published parameters, teardowns, papers, shipping products) or on virtual models built from it ("you could model the speaker setup to test virtually", 2026-11-22). Anything that would need a measurement is unverified and gets designed around.
- Reliable choices: proven parts and approaches, no experiments (2026-11-22, "they should be reliable choices").
- "Surface mount is fine if necessary" (2026-11-22).
- Work from first principles when something is unclear: "Make sure we’re not assuming things." (2026-11-22)
- Requirements come first, then an engineering check, then design concepts (2026-11-22, "I would imagine we’d need requirements first").

## 8. Cost
- No fixed ceiling: "Budget ceiling should be what we can to hit the desired goal." (2026-11-21). Everything is still costed honestly and compared with the market ("The cost of pads seems egregious compared to the market", 2026-11-22).

## 9. How decisions are made
- Trade-offs go to Adam: "if we can do better or need to do worse tradeoffs should be discussed" (2026-11-22).
- Keep Adam's words separate from agent proposals. Label which is which; never present an agent's number as his target.

## 10. Showing the work
- Images only for what has to be visual; text is real text (HTML on the site): "i really only want images for things that need to be images" (2026-11-13). "dont render a bunch of images unnecessarily" (2026-11-13).
- Images are made to look great on the project site, viewed responsively, not printed (2026-11-13).
- Claude is never a visible collaborator on the GitHub repo: commits carry no Claude attribution (Adam's standing preference).

## Family defaults (decided on one instrument, reused unless Adam changes them)
- **MIDI:** USB-MIDI plus 3.5 mm TRS MIDI in and out; synth settings controllable over MIDI; MIDI never flips switches; knob-only controls send no MIDI; the echo syncs to MIDI clock, with a FREE / SYNC toggle (Big Energy 2026-11-12/13, kept for floss 2026-11-21).
- **No screens or encoders, real knobs:** on trial for floss ("Let’s try without", 2026-11-22).
- **Battery powered with a built-in speaker,** muted by headphones (floss 2026-11-21, as on Big Energy).
