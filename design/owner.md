# Owner direction — Little D (budget instrument)
Shared owner history for the whole project (both instruments): /home/claude/model-d/archive/full-instrument/owner.md — read it; most decisions there apply here too.

## 2026-11-12 — start of Little D design work
Owner (verbatim): "Pause the designers on the full instrument and let's focus on the budget one for now. I want designs for the budget one and I want the enclosure to be coherent in form with some clear perspective. Design principles with a solid basis of logic in the idea of the thing. Get creative here."
Recorded as:
- Full instrument design PAUSED. Little D is the focus.
- Wants designs (concepts) for Little D.
- The enclosure must be coherent in form, with a clear point of view.
- The design should rest on explicit design principles that follow logically from the idea of the thing (what it is), not decoration.
- Creative licence: "Get creative here."

## Decisions already made that bind Little D (from the shared history; see eng/budget-variant.md)
- One test unit; owner builds it. Hand-soldered through-hole only; SMD only as ready-made plug-in modules. Bare boards; prefer quantity-1 fabs.
- Voice: 3 VCOs, all original waveforms, original-style chips (modern equivalents e.g. AS3046; no vintage parts), ladder filter with mixer overdrive, 2 analog contours with overshoot, VCA, glide, autotune (no manual calibration).
- Keys: 25 minimum (two octaves); velocity REQUIRED; as silent as possible; "feel like an instrument" (not clicky); real bought parts — no 3D-printed keys/knobs/wheels; owner may laser/CNC-cut parts himself at Vector Space (key tops OK); no harvested keybeds. Key mechanism being rethought from first principles (archive/full-instrument/concepts/keys/first-principles.md when done).
- Bend/mod: bend = joystick restricted to one direction, springs back; mod = a control that stays put (dial or fader); mod depth MIDI-controllable (jump-on-move).
- MIDI: USB-MIDI + 3.5 mm TRS MIDI in; MIDI-controllable params per eng; knob-only controls send no MIDI; MIDI never flips switches.
- Built-in speaker (LM386) + outputs. No additional patch points beyond pitch CV/gate out + filter CV in.
- Power: USB power bank or internal LiPo (open; ~+$21 for internal).
- Size: portable; OP-1 is a loose reference only ("it should feel good to use"). Eng's working box ~285 × 160 × 30 mm.
- Cost is the owner's main concern (current estimate ~$239–320 one unit). Enclosure: laser-cut/CNC at Vector Space (material cost) preferred.
- Owner wants to SEE visual mocks to judge looks.

## 2026-11-12 — owner answers (asked one at a time at the owner's request: "Also ask me open qs one at a time")
Q: self-protecting body (~+$10–20) vs separate sleeve? → Owner: "Show me both" — decide after seeing mocks; keep both kinds in the set.
Q: what should velocity change? → Owner: "Both, with a switch" — a switch selects velocity → loudness / filter / both.
Q: bend up+down or up only? → Owner: "Up and down" — one axis, springs to centre (as assumed).
Q: avoid the Moog look entirely? → Owner (verbatim): "Nods are fine but I want to see breadth of explorstion" — subtle nods to the Model D are allowed (no copying); priority is a broad range of exploration across the concepts.
Q: is ~36 mm body thickness OK? → Owner (verbatim): "I have no idea you tell me. How tall is op1" → Orchestrator answered: OP-1 is 13.5 mm (TE spec); recommended ~36 mm body / ≤40 mm to knob tops for Little D (full-size knobs, key travel, jacks). Treat as the working decision unless the owner objects.
Q: bare vs standard printed board? → Owner: "Standard (printed)" — solder mask + silkscreen.
Q: flat piano tops vs maple pegs? → Owner: "Show me both".
Q: build the first two real keys (C, C#) as the one feel check? → Owner (verbatim): "I don't want to build custom keys"
Recorded as: owner does NOT want to build a custom key mechanism (this challenges RAIL / FLOAT / COMB, which are owner-built). Conflicts with earlier constraints (no harvested keybed; no bare mini keybed sold to individuals; real parts; velocity; silent). Orchestrator asking the owner to choose among the remaining routes.
Q: which key route (bought switches + snap-on tops / full-size Fatar / silicone pads / reconsider harvesting)? → Owner: "Whatever the design needs"
Recorded as: key route is the design team's call per concept, within: no custom-built key MECHANISM by the owner (no rods/tubes/flexure assemblies to build) — prefer bought mechanisms (switches, pads, bought keybed) with minimal assembly; harvesting still not chosen by owner (he didn't select it); velocity + silence still required.

## 2026-11-12 — owner feedback on round-1 sheets (seen marked rough)
Owner (verbatim): "Typecase hush and hymnal are really cool. I like those. I have some feedback though. The filter sections should not be raised. That would make the knobs Hard to access. And I want to see a version of one sheet that is made from a 3-D printed enclosure. I feel like hush could similarly be made from a 3-D printed enclosure, and then the wool felt applied. That's super interesting. I also in the old diagrams, I really liked the idea of a two-part folding unit. I liked the one that was walnut with the white panel. I'd like to see something like that in this round that is foldable with the controls on the top part and with a white panel that gets screwed into a darker surrounding area. I don't think I wanna make it out of walnut, but that's a possibility. I have some at my house that I could plane. I'd like to see that first explored as 3-D printable."
Recorded as:
- LIKED: TYPE CASE, HUSH, HYMNAL.
- RULE: no raised filter section (or raised control section) — it makes knobs hard to reach. Applies to all concepts.
- ADD: a ONE SHEET version made as a 3D-printed enclosure.
- ADD: HUSH as a 3D-printed enclosure with wool felt applied over it ("super interesting").
- ADD: a two-part FOLDING unit, like the earlier full-instrument concepts (owner recalls "walnut with the white panel" — likely a mix of round-1 CASE clamshell / MOTTO; the full-instrument mocks are in archive/full-instrument/concepts/ incl. archive): controls on the top (lid) part, a white panel screwed into a darker surround. Explore FIRST as 3D-printable; walnut (owner has some at home he could plane) is a possible later material.
- 3D-printed ENCLOSURES are now welcome (earlier "real parts" rule covers knobs/keys/touched controls, not the enclosure). Vector Space printers: Prusa MK3/MK4/Core One (~250 mm beds), TAZ6, Voron Trident/2.4, Gigabot (larger; volumes unverified) — a 298 mm body needs a split or a large printer.
- UNDER GLASS (director's replacement for ONE SHEET) was not yet shown to the owner and he didn't mention it.
Owner (verbatim): "Also important to note, little D is a terrible name. It sounds like little penis. I could see big D energy or just big energy or something like that, but the name needs work."
Recorded as: DROP "Little D" as a name (working folder path stays design/ for continuity). The budget instrument needs a real name; owner floated "big D energy" / "big energy" as directions. Naming to be explored by the design team; until then call it "the budget instrument" in owner-facing material.
Owner (verbatim): "I actually think this is going to be the real instrument I'm trying to make the most interesting thing overall and it's this for me"
Recorded as: the budget instrument is now THE instrument — the main project and the one the owner most wants to make interesting. The full instrument stays paused (no decision to cancel it). Aim for the most interesting result overall.
Owner clarification (verbatim): "On the type case feedback whati was talking about was the dividers that got in the way of the knobs"
Recorded as: the "raised" complaint was about TYPE CASE's section DIVIDERS getting in the way of the knobs — remove them (e.g. flush engraved grooves/inlays, or separations that don't rise above the panel). The owner did NOT object to the front rail; the systems designer's flat-front-rail change was an over-reading — the design team may restore the round-1 front rail/lip if it served the concept (bag protection), as long as nothing gets in the way of the knobs.
Owner (verbatim): "That includes the separator between keys and controls too"
Recorded as: the separator between keys and controls (TYPE CASE's front rail) also goes — nothing raised between the keys and the controls. The systems designer's flat-front / keys-near-panel-height rule stands after all.
Owner (verbatim): "Use another method of separation if you think it's important to feel the sections"
Recorded as: if tactile section-finding matters, use a different, non-obstructing method (e.g. texture changes, shallow grooves, a different knob shape/colour per section, raised dots below the panel plane) — designers' call; nothing may rise in the way of the knobs.

## 2026-11-12 — after seeing the four 9s (HUSH, FOLD, TYPE CASE, HYMNAL)
Owner (verbatim): "Let's pause on everything but hush fold and one sheet.

On hush and one sheet — I'd like the enclosure to be as "unibody" (on each half with fold) as possible. Screws in the back instead of front, etc, where panels need to be installed. Hush should be more rounded around the edges, organically, so the felt can wrap seamlessly around it. Folds original color way was way better lets go back to that vibe. Also the knob layout is adding extra space in front of the keyboard that's awkward, I like the keys right up to the edge, so rework the knobs to be logically split, and maybe it could get a bit narrower. Let's not worry about a case for hush or one sheet yet"
Recorded as:
- ACTIVE: HUSH, FOLD, ONE SHEET. PAUSED: TYPE CASE, HYMNAL (both scored 9; kept on file).
- UNIBODY: HUSH and ONE SHEET enclosures as close to a single seamless body as possible; for FOLD, each half a unibody. Fasteners hidden — screws from the back/underside, not the front/top, wherever panels are installed.
- HUSH: rounded, organic edges all round so the felt wraps seamlessly over them.
- FOLD: return to its ORIGINAL colourway vibe (owner's words; interpretation being confirmed — likely the round-2 FOLD: white faceplates, dark housing, blue knobs, cream CUTOFF).
- LAYOUT (all three): no awkward extra space in front of the keyboard — keys run right up to the front edge. Rework the knob layout so it's logically split (e.g. rows/sections arranged to free that front space), and it may get a bit narrower.
- NO carry case/sleeve/flap work for HUSH or ONE SHEET for now.
Q: FOLD "original colourway" = round-2 blue-knob FOLD, or the old walnut + white from the full-instrument mocks? → Owner: "The old walnut + white" — the walnut-with-white-panel look from the full-instrument mockups (see archive/full-instrument/concepts/archive-315mm/, case/, look-sheet.png; owner earlier: "I liked the one that was walnut with the white panel"). Walnut-toned housing (printed in a walnut-like colour first; real planed walnut later) with a white panel.
Orchestrator note: the "walnut + white" look the owner means is almost certainly the "Proof" look (walnut ply body, cream/white panel, black knobs and legends, red CUTOFF) shown on the full-instrument look sheet: /home/claude/model-d/archive/full-instrument/concepts/look-sheet.png (top-right). FOLD should return to that vibe: walnut-toned housing (printed in a walnut-like filament first; real planed walnut later), cream/white panel, black knobs, red CUTOFF.
Owner (verbatim): "I also liked the rounded edges of the original fold with flat top and bottom. I imagine the housing being a hollowed out block that the face plate with filters and keyed get installed in, sort of like a guitar with pickguard that has controls attachdd"
Recorded as (FOLD, and a construction idea that suits the unibody brief generally):
- Keep the ORIGINAL FOLD's rounded edges with flat top and bottom faces.
- Construction metaphor: a guitar body + pickguard. The housing is a hollowed-out solid block (unibody); a faceplate carrying the controls (knobs etc. — "filters" likely means the filter/controls) and the keys installs into the hollow, like a pickguard with controls attached. The faceplate/pickguard is the white panel; the block is the walnut-toned body.
Owner (verbatim): "The screw placement is malleable but yes screw from back is ideal."
Recorded as: screws from the back are IDEAL but not mandatory — flexible where the pickguard construction needs top fixings (keep them tidy/intentional).
Owner (verbatim): "One sheet and hush feel like the controls are installed from behind and then a panel screwed in on the back"
Recorded as: ONE SHEET and HUSH construction — unibody shell open at the back/underside; controls (boards, pots, keys) install from behind through that opening, poking up through the closed top face; then a back panel screws on to close it. (FOLD uses the guitar block + pickguard logic instead.)
Owner (verbatim), on "no battery fits FOLD's lid, default to a USB power bank": "What do you mean there's no battery thing enough we are designing this"
Recorded as: an INTERNAL battery is expected — the enclosure must be designed around one ("completely portable"). The "no battery fits" finding only applied to the 30 mm lid band; find space (e.g. flat pouch cells under the key board or main board, a deeper/thicker section, the base half) in all three concepts. Battery life target not yet stated (orchestrator proposed ~4–5 h).
Q: FOLD with the ladder filter moved to the base (EMPHASIS beside CUTOFF) — big 22 Wh battery with 113 mm halves, or slim 11 Wh (4× PiShop 952540) with 105 mm halves? → Owner: "Show me both".
Pending owner answer: ONE SHEET needs a ~1 h, 80×80 mm test print at Vector Space to prove its surface finish — print it, or drop ONE SHEET?

## 2026-11-12 22:30 — owner feedback on round 4
Owner (verbatim): "On fold — there's still something off about the controls layout that doesn't feel balanced yet. On one sheet I love the rings texture — can we figure out how to reduce and only use no texture and that texture? Also I'm thinking — Is there a way for us to build in some effects, mainly a delay and echo? Also both of them have a lip after the keys — I want to make sure the keys are somewhat raised so you can feel them at minimum, and I'm not fully understanding the press mechanism, I may want them at the edge altogether depending on if they're like real keys. Can you draw the mechanism for me in a diagram. I'd also like front views of all of these so I can see the details."
Recorded as:
- FOLD: control layout still feels unbalanced — rework for visual/functional balance.
- ONE SHEET: LOVES the rings texture (the concentric rings under knobs); reduce the finish vocabulary to exactly two: no texture, and the rings texture.
- NEW FEATURE REQUEST: built-in effects, mainly a delay and echo — engineering to propose options.
- KEYS (HUSH, ONE SHEET): there's a lip/edge in front of the keys; keys should be at least somewhat raised so they can be felt; owner may want keys right at the edge with no lip, depending on whether they behave like real keys. Owner wants a diagram of the key press mechanism.
- Wants FRONT VIEWS (elevations) of all concepts to see details.
Orchestrator showed a key-mechanism side-view diagram and explained honestly: short-travel (2.8 mm) button-keys, not pivoting piano keys.
Q: keys at the front edge with no lip, standing ~2–3 mm proud of the panel? → Owner: "Show me both" (at-edge raised vs keep a small lip) — decide from front views.
Q: echo — PT2399 (cheap, ~0.5 s, no sync) vs digital delay on a 2nd Pico (sync, 4+ s)? → Owner (verbatim): "Is there a single chip that could handle all of it? We could go back to first principles a bit have an agent research"
Recorded as: research from first principles whether ONE chip can handle all of it — the delay/echo (incl. sync and longer delays) and ideally the existing digital duties (MIDI, autotune, key scanning, control CVs) — rather than adding chips. Owner wants a research agent on it.
Owner (verbatim, 2026-11-13 09:02): "I want echo and reverb"
Recorded as: effects scope = ECHO and REVERB (reverb newly in scope; earlier docs said reverb out of scope — superseded).
Owner (verbatim): "Delay and verb can be digital"
Recorded as: CONFIRMED — the delay/echo and reverb may be digital (the synth voice stays analog).
Owner (verbatim): "I would want great models tho — would be cool if digital could do more than one type."
Recorded as: effect QUALITY matters — great-sounding models (not toy delay/reverb); multiple types selectable (e.g. tape echo / clean digital delay; plate / hall / spring reverb).
Research result (eng/single-chip-research.md): existing Pico 2's second core runs echo + reverb with a Teensy Audio Shield Rev D (SGTL5000) module + 74HC595 + TL072, ≈$22–25; echo types TAPE/BBD/CLEAN/PING-PONG, reverb PLATE/HALL/SPRING/SHIMMER; MIDI clock sync; one-evening breadboard test before board order; Daisy Seed is the fallback.
Q: FX controls — full 8 (echo TYPE, reverb TYPE, TIME, REPEATS, ECHO MIX, DECAY, REVERB MIX, TAP) vs compact 5? → Owner: "Full 8, grow the panel".
Owner (verbatim): "Check the pin thing. Audio feels the most important since we're introducing digital stuff"
Recorded as: verify whether the Daisy Seed's exposed pins can handle all control duties (3 VCO frequency counts via timer input capture, key/knob mux scanning, PWM CVs, DAC buses, MIDI, FX controls). PRIORITY: AUDIO QUALITY of the digital effects is the most important factor in the Pico-vs-Daisy choice.
Owner (verbatim): "I like the idea of drift, but I'd want it to be controllable"
Recorded as: ADD a controllable DRIFT (firmware-generated slow random pitch wander per oscillator, 0 = rock steady autotuned) — a panel control (knob), placement for the design team; affects layout (+1 control).
Owner (verbatim): "On fold, we should build some sort of method for the top case to stand up, either at a full 90° or some useful angle. It should fit the design language of the device and should blend into the case"
Recorded as: FOLD's lid must also be able to stand up — at 90° or another useful playing angle (in addition to lying flat at 180°) — via a mechanism that fits FOLD's design language and blends into the case (no bolted-on prop).
Owner (verbatim): "It is not a requirement that you can change the angle"
Recorded as: one fixed standing angle is fine (plus flat/closed); no adjustable-angle mechanism needed.
Pin/audio check (eng/daisy-pin-and-audio-check.md): Daisy Seed fits all I/O (26/31 pins; TIM5 32-bit counters ×4); Pico plan fits only 26/26 and misses filter-cal counter + MIDI out. Codecs: SGTL5000 85–90 dB ADC vs PCM3060 99 dB vs TAC5242 110 dB. Daisy runs lush hall reverbs (CloudSeed) the Pico can't.
Q: switch the digital brain to the Daisy Seed? → Owner: "Switch to Daisy Seed".
DECISION: Daisy Seed (Seed3 or 65 MB Seed2 DFM, current revision; avoid used Rev 5) replaces the Pico 2 as the single digital chip (control + echo/reverb). Dry voice path stays analog. Breadboard spike before layout re-aimed at Daisy.
Owner (verbatim): "Also the key thing you need to port - go back to first principles and see if there's a better way with Daisy seed. Do this with all the things Daisy seed affects"
Recorded as: re-derive from first principles every digital subsystem the Daisy Seed touches (key scanning/velocity, autotune frequency measurement, pot scanning, CV generation, MIDI/USB, FX, power) for the best Daisy-native approach — not a straight port of the Pico design.
Daisy first-principles design: eng/daisy-first-principles.md (3 muxes on separate ADCs, Hall power-gating, TIM5 VCO counting + codec right-channel filter cal, coarse+fine pitch DACs, CUTOFF CV gap fixed, single rear USB-C, wet-only FX return, +$11–15, 27/31 pins, two-evening breadboard test).
Q: add a 3.5 mm TRS MIDI OUT jack (free in pins)? → Owner: "Add MIDI out".
Owner (verbatim), on adding channel aftertouch via a pressure strip under the key strip: "i think it needs its own switch but yes now i want it"
Recorded as: ADD channel aftertouch (pressure strip under a compliantly mounted key strip, one Daisy ADC input), with its OWN destination switch (separate from the velocity LOUD/BOTH/FILT switch) — e.g. VIBRATO (mod depth) / OFF / FILTER; sent over MIDI out too. +1 toggle on the panel.
Explore reports: explore/easier-cheaper.md, explore/cooler.md, explore/poly-hybrid.md (recommendation: stay with the Model D-based build; add paraphonic mode; Juno-60-style poly or Synthi-style lunchbox as a later instrument).
Q: add paraphonic mode? → Owner (verbatim): "would love to add it but how would keytracking work with the different oscillators?" — wants it, pending an answer on key tracking.
Orchestrator explained paraphonic key tracking (each note tracks; RANGE kept; FREQ 2/3 become fine detune in PARA; filter tracks highest note by default, changeable via key combo; shared envelopes) and voice allocation (next free oscillator; spare oscillators double, lowest note; oldest-note stealing; PARA+4 uses the Daisy's digital 4th osc).
Owner (verbatim): "how does it know what note to send to what oscillator" → answered; then "yeah so firmware could even improve the paraphonic control over time right?" → yes (USB-C firmware updates; hardware limits: one filter, shared analog envelopes, 3 analog VCOs + digital 4th).
Recorded as: PARAPHONIC MODE APPROVED (MONO / PARA / PARA+4 toggle). Firmware is updatable and expected to evolve.
Round 5 sheets (A + D for HUSH, ONE SHEET, FOLD-105; E for FOLD) sent to owner after director scored all three 9.
Q: key edge A (keys at the edge, raised, no lip) or B (small lip)? → Owner: "A: keys at the edge". DECISION: edge A for HUSH and ONE SHEET.
Q: which concept to build? → Owner (verbatim): "i think the fold's angle should be a bit less steep so the front face catches more light. also i want the bend slider to be a joystick (is it a snap to center fader or what? cant remember where we landed there)" — no pick yet.
Recorded as: FOLD standing lid should lean back further (less steep than 105°) so the panel face catches more light. Bend control must be (and read as) a JOYSTICK — orchestrator to clarify current design (spring-to-centre mini thumbstick gated by a slot to one axis, which reads like a fader).
2026-11-13 Owner (verbatim): "actually forget i said that. just lock all of these as official versions and create a way for me to get a new orchestrator involved. i just saw that you compacted."
Recorded as: HUSH, ONE SHEET, FOLD-105 (round 5, plus FOLD 120° stand spec + bend-reads-as-joystick redraw in progress) LOCKED as official v1 → versions/v1/. Owner leans toward building ONE SHEET or FOLD (undecided). The creative-rounds request in the same message was WITHDRAWN by the owner ("forget i said that") — do not act on it unless he raises it again.
2026-11-13 Owner (verbatim): "oh do those first" (the 120° stand + joystick redraw, before the git move) · repo: "heres the repo when this is done. dont assume it needs to be zipped https://github.com/adamtrabold/big-energy"
Recorded as: FOLD stand 120° + bend drawn unmistakably as a joystick (round opening, stem, cap; B-sheet callout) + FOLD sheet D MIDI IN fix → director held all three at 9 → locked as v1.1 (versions/v1.1/), superseding v1 sheets. Repo adamtrabold/big-energy is the working home (plain files).
2026-11-13 Owner (verbatim): "why in the design folder are the folders instrument and little-d? that doesn't really follow the versioning in a way that's easy to understand" → "yes and also let's resolve that verisoning thing i mentioned"
Recorded as: repo restructured: versions/ (v1, v1.1) at top with VERSIONS.md; design/ = the instrument being built (was design/little-d); archive/ = full-instrument, paused concepts, superseded FOLD sheets. FOLD files drop the -105 suffix. Locked folders are never edited; new locks go to versions/vN + a VERSIONS.md line.

## 2026-11-13 11:47 — branched creative rounds (the request is back on)
Owner (verbatim): "i think i want to move forward with one sheet and the fold (can't decide yet, but the internals are probably the same eh?). but first i'd like to take these versions and do some creative rounds (again, using the randomness principles) to explore how to add some more personality. i *love* the peg keys on the hush, for example, and those on the fold may add an "organ like" feel or something idk. im not saying that is an official direction to explore, but im saying we need to push for more of an even more holistic *point of view* / concept in some branched versions (i may still come back to these). follow principles of design of furniture (theres even a great book on this called principles of design), instruments, tools, but also artistic inspirational forms and emotion. i want to take this to the park and be inspired. also i want to make sure the delay can be timed to the midi if there is midi tempo control"
Recorded as:
- Leaning toward ONE SHEET and FOLD (still undecided). Orchestrator answered: the electronics and spec are shared; the board split differs (FOLD has a hinge cable, ONE SHEET is one deck).
- NEW WORK: branched creative rounds starting from the v1.1 versions, using real randomness (as in earlier jams), to add PERSONALITY and push each branch toward a more holistic point of view / concept. The v1.1 locks stay as they are; he may come back to them.
- LOVES HUSH's peg keys. Pegs on FOLD might give an "organ like" feel. He said that's an example, not an official direction.
- Inspiration sources: principles of furniture design (he mentioned a book called "principles of design"; which book isn't confirmed), instruments, tools, artistic forms and emotion.
- "i want to take this to the park and be inspired": playing it outdoors, away from a desk, is a use the design should serve and inspire.
- The echo must sync to MIDI tempo when MIDI clock is present. (The spec already parses USB and TRS MIDI clock into the FX tempo. What the controls do under clock isn't designed yet; the systems designer defines it.)
- All earlier owner rules and the locked spec still bind the branches unless he changes them.
2026-11-13 11:58 Q: echo sync — A (automatic, hidden hold-TAP + turn-TIME override, $0) or B (FREE / SYNC toggle by TIME, ≈ $1)? → Owner: "B"
DECISION: add a FREE / SYNC toggle near TIME (design/branches/echo-clock.md option B). FREE: TIME ≈ 20 ms–2 s, clock ignored. SYNC: TIME picks a note division; tempo from MIDI clock (USB or TRS) if present, else TAP. Applies to whichever concept is built (and the branches). Placement is the designers' call per concept.

2026-11-13 12:33 Owner (verbatim): "why make anything on a3 at all? im not in europe and im not printing"
Recorded as: drop A3 as the default format for mocks and sheets. Nothing is printed; images are viewed on screen (phone first, per the site's J14). The format is the designers' call, made for on-screen viewing. Locked versions stay as they are.
2026-11-13 12:39 Owner (verbatim): "dont do phone first -- do images that will be great on the site that i can view responsively"
Recorded as: CORRECTION to 12:33 — not phone-first. Images are made to look great on the project site and to work responsively across screen sizes (phone through desktop).
2026-11-13 12:41 Owner (verbatim): "i really only want images for things that need to be images -- text should be html and stuff"
Recorded as: images only for what has to be visual (renders, drawings, diagrams, plots). Text (principles, specs, notes, labels, tables, scores) is real HTML on the site, not baked into images. This retires the "sheet" format (text plus pictures in one image) for new work.

2026-11-13 13:13 Owner (verbatim): "dont render a bunch of images unnecessarily"
Recorded as: render an image only when it is needed to judge or show something; no image sets made by habit, no pictures of web pages.

## 2026-11-13 14:12–14:18 — CHAMBER + FOLD, toward CATHEDRAL
Owner (verbatim, 14:12): "i want to lock in on cathedral and fold right now. what are the differences between them so i can find the best middle ground"
(Orchestrator read "cathedral" as CHAMBER and sent the differences table.)
Owner (verbatim, 14:18): "i'm not sure i like the oxblood spine, it feels unnecessary. also the hunges on this... is there any way we could do a more hidden hinge or hidden hinges in the gap? if not these are fine. i also want to work on the speaker placement and design metaphors a bit.. the speaker palcement creates an odd gap between some of the elements, and the effects & out is real far from echo and reveb controls... those should be together. i also wonder if the protective feet couldn't be one with the screws that screw the case in so they aren't visible. i'd like the engraving texture in the case to be more "woody" but i do like the subtlety and relative detail (eg. number of lines and shapes... straight woodgrain would be too detailed imo). i also want to make sure the rounding of the faceplates is consistent... the front edge is squared unnecessarily. and i want to make sure that the color of the pegs and buttons go together better... i feel like there are too many colors, and the brown feels out of place. explore options there. i wish the screen had more elements of rounding... either tapered shape of lines (so top and bottom are smallest, next in is longer, next in is longer, etc) or circular. i think 'cathedral' is a better POV than chamber. see how that affects the ideas"
Recorded as:
- FOCUS: CHAMBER and FOLD v1.1 only; find the middle ground. Rename the point of view CATHEDRAL (instead of CHAMBER) and let that reshape the ideas.
- Oxblood spine: probably unnecessary — not sure he likes it.
- Hinges: explore a more hidden hinge, or hidden hinges in the gap; if not possible, current hinges are fine.
- Speaker placement: creates an odd gap between elements; rework placement and the design metaphors around it.
- FX & OUT (the FX output/jack area) is too far from the ECHO and REVERB controls; they should be together. (Exact meaning of "effects & out" to be confirmed by the team from the panel.)
- Feet: could the protective feet be one with the case screws so neither is visible?
- Engraving on the case: more "woody", keep the subtlety and amount of detail (number of lines/shapes); straight woodgrain would be too detailed.
- Faceplates: rounding must be consistent; the front edge is squared unnecessarily.
- Colours: pegs and buttons should go together better; too many colours; the brown feels out of place. Explore options.
- "the screen": wants more rounding — tapered lines (shortest at top and bottom, longer toward the middle) or circular. ("Screen" most likely the speaker grille; the team confirms.)

2026-11-13 14:30–14:32 Owner asked (verbatim): "Are these pegs sourceable?" / "What about the brass ones?" / "The Wooden ones you linked do not have shafts that match the prototype"
Recorded as: the peg keys as drawn (HUSH, CHAMBER, CATHEDRAL, RAIN) assume a plug shank that stock button plugs do not have. The peg mount must be redesigned around a real, buyable part with known head and tenon sizes, or the peg approach revisited.

2026-11-13 14:33 Owner (verbatim): "I don’t know how to machine — the keys need to be printed or purchasable"
Recorded as: NO MACHINING by the owner. Keys (and key tops) must be 3D-printed or bought. This RELAXES the earlier "keys must be real bought parts, never printed" rule: printed key tops are now allowed. It also bears on any part the design has him cut or drill from stock (e.g. brass stays and hinge leaves cut from flat bar): those must become bought or printed parts too. Laser cutting at Vector Space was allowed earlier and was not mentioned here.
2026-11-13 14:34 Owner (verbatim): "They can be printed externally too - I know you can get metal prints"
Recorded as: external print services are allowed, including metal printing (e.g. printed brass or steel parts ordered from a service). Parts may be printed by him or ordered printed.
2026-11-13 14:40 Owner (verbatim): "I don’t want a spine can we route cables through a hinge. Engraving texture I meant fine line texture — I’ll probably do a design for the pipe lines. And what about brass and black keys? Or all brass? Could 3d print and reminds me of a cathedral"
Recorded as:
- NO SPINE. Asks whether the cables (the hinge ribbon) can route through a hinge. (Implies the back slot question needs another answer.)
- "Engraving texture" = the fine line texture on the case (walnut body), not the pipe lines. The OWNER will likely design the pipe lines himself; the team leaves the façade line design to him (placeholder only).
- KEYS: explore brass + black keys, or all brass. Could be 3D printed (metal printing is allowed); brass reminds him of a cathedral.
2026-11-13 14:41 Owner (verbatim): "Premade wooden caps on a shaft that also is premade or part of the key is fine too just thinking"
Recorded as: also acceptable — bought wooden caps on a shaft that is either bought or part of the (printed) key. Thinking out loud; an option, not a decision.

2026-11-13 15:07 (layout decision) Owner (verbatim): "I don’t like the speaker on the key side but I also don’t like the eye shape"
Recorded as: neither speaker solution. Rejects B's round speaker at the base (key side) AND A's lens ("eye") window in the band. He did not reject B's effects grouping; his earlier ask that FX sit with echo/reverb stands. A third speaker answer is needed.
2026-11-13 15:12 Owner (verbatim): "I like the idea of the lines going up and down vs sideways. Or we could go back to a circle and maybe not centered?"
Recorded as: grille in the lid band (P1 area implied): prefers VERTICAL lines (up and down) over horizontal. Alternative: a circle, possibly off-centre. Both open.
2026-11-13 15:18 Owner (verbatim): "Also occurs to me that the verb and delay are stereo…should we have two? Also is there stereo output?"
Recorded as: asks whether to have two speakers (stereo) given stereo reverb/delay, and whether there is a stereo output. (Spec today: one mono PHONES/LINE jack via the LM386 and one speaker; the Daisy codec is stereo; stereo phones was noted as an optional wiring choice.) Grille choice (tower vs circle) still pending.
2026-11-13 15:22 Owner (verbatim): "Stereo phones is fine but I need to pan the signal into the effects"
Recorded as: DECISION — stereo phones: yes (one speaker; second speaker not taken). Line out stereo: not stated. NEW REQUEST: a way to pan the (mono) synth signal into the stereo effects. How (a pan control, its range, digital or analog, placement) is for the team; it likely adds a control.
2026-11-13 15:23 Owner (verbatim): "Stereo line out"
Recorded as: DECISION — line out is stereo too (TRS). Stereo phones + stereo line out, one speaker.
2026-11-13 15:24 Owner (verbatim): "Left channel should be mono tho if stereo isn’t plugged in"
Recorded as: REQUIREMENT — with a mono (TS) cable plugged in, the left/tip output carries the full mono sum (L+R), not just the left channel. Applies to the stereo outputs.
2026-11-13 15:44 Owner (verbatim): "Yea sure on midi. And is it sending the delay through the pan too or just the dry"
Recorded as: DECISION — FX PAN receives MIDI pan (CC 10). Asked what the pan affects; answered: it pans the signal going INTO the echo and reverb (so the delay and reverb come out from that side); the dry voice is not panned and stays centred.
2026-11-13 15:50 Owner (verbatim): "Run this all through a dedicated audio engineer / synth expert for gotchas and unexpected functionality that doesn’t make sense"
Recorded as: an independent expert review (audio engineer / synth designer) of the whole instrument's audio, control and MIDI behaviour, including today's additions. Reports to the owner; decides nothing. MIDI pan "send" question still open.
2026-11-13 15:50 Owner (verbatim): "I think I’d like to pan the delay into the reverb separately from the dry signal but also would want to be able to sync that"
Recorded as: wants the DELAY panned into the REVERB separately from the dry signal's pan, and wants that pan to be syncable (most likely a tempo-synced auto-pan; being confirmed). Supersedes the single FX PAN design as stated.
2026-11-13 15:53 Owner (verbatim): "No the pan would be audio signal. Basically I’d like to pan just the delay separately from the full dry but also I’d like to be able to have the pan signals sync"
Recorded as: NOT a tempo auto-pan. Wants two audio pans: (1) the full DRY signal panned on the outputs, (2) the DELAY panned separately; plus the option to have the two pans "sync" — most likely linked so they move together (exact meaning being confirmed).
2026-11-13 15:54 Owner (verbatim): "Follow dry"
Recorded as: DECISION — when the pans are synced/linked, the delay pan FOLLOWS the dry pan (same direction). MIDI send question (knobs receive-only? keys send notes?) still open.

## 2026-11-13 16:18–16:21 — expert review follow-up, MIDI, architecture docs
Owner (verbatim, 16:18): "yes but first walk me through the midi implementation" (yes = send the expert review's fixes to the team).
Owner (verbatim, 16:21): "heres what im thinking -- we need on that site architectural documentation and clear docs for each featureset. lets start defining this stuff and writing it down 1 by 1 in an easily delineated fashion, so we can make sure the architectural decisions are sound across the device. sorry i didnt mean is usbmidi capable of send, but rather are we already doing send. if we do send then we gotta think about ALL of the features, and this is pretty definitively not a midi controller. though if it's free it could be."
Recorded as:
- NEW WORK: architecture documentation plus one clear doc per feature set, written one at a time, clearly separated, so architectural decisions can be checked as sound across the whole device. These docs live on the project site.
- MIDI stance: "pretty definitively not a midi controller". Sending MIDI means thinking about ALL features, so send only "if it's free". Today the spec sends only channel pressure (aftertouch); notes and knobs sending is not specified.
- The expert review's fixes go to the team.
2026-11-13 16:22 Owner (verbatim): "the workflow im much more interested in is controlling it from another device or mainly a DAW. im not so worried about using it as a controller for other things. but if it's free we could explore it"
Recorded as: PRIMARY MIDI WORKFLOW = the instrument is CONTROLLED from another device, mainly a DAW (MIDI in). Using it as a controller for other gear is secondary; explore sending only where it is free.

2026-11-13 16:23 Owner (verbatim): "im going to put the github on github pages so i can easily access it from there instead of here. i want all review and logs and documents there, not here"
Recorded as: the owner will publish the repo with GitHub Pages and view everything there. ALL reviews, logs and documents go in the repo (and so on the Pages site), not as files sent in chat. Hosting for the project site moves from the claude.ai artifact to GitHub Pages (static; it updates when sessions commit and push).
2026-11-13 16:24 Owner (verbatim): "ok thats fine if its not private"
Recorded as: DECISION — a public GitHub Pages site is fine (anyone with the address can see it). Hosting: GitHub Pages from the repo root or a GitHub Action (not /docs).

2026-11-13 16:28–16:29 Owner (verbatim): "re: architecture i think the way its organized is just unclear. have the systems designer take a look. is it up on pages right now? do that first" · "i dont want a bunch of .md docs, i want this stuff on website"
Recorded as: (1) put the site on GitHub Pages first — done as far as a session can: build pushed to branch gh-pages; turning Pages on is blocked from sessions (owner does it in Settings → Pages). (2) The architecture doc's organisation is unclear — systems designer to rework it. (3) Docs, architecture and reviews must be ON THE WEBSITE (rendered pages), not markdown files he has to open. Markdown stays only as the source the site builds from.
2026-11-13 16:40 Owner (verbatim): "gh pages is fine"
Recorded as: DECISION — the site keeps deploying from the gh-pages branch. Sessions rebuild and push it after changes (site/publish.sh).

2026-11-13 16:43 Owner (verbatim), on the live site: "every page here needs a point i literally have no idea what im looking at in "latest" for example. and where do i see the grille options and all of the other options"
Recorded as: every page must state its point (what it is and why you are here) up front; "Latest" does not make sense to him. The site must show the open decisions waiting on him, with their options (e.g. the grille options) and images, in one obvious place.

2026-11-13 16:52 Owner (verbatim): "ok i dont think you're really thinking here — off center in that middle section is bad looking. aso consider the sound of the speaker and the shape... which will work best and give me the best sound out of the chosen speaker. in fact none of my feedback on why it's a problem have been addressed. there's a massive horizontal gap -- the speaker doesnt feel resolved. this may mean moving components. i'd rather have more brass than black re: keys too."
Recorded as: REJECTS the off-centre circle (bad looking in the middle section). Neither option resolves his real complaint: the massive horizontal gap in the lid band; the speaker does not feel resolved. Moving components is allowed to fix it. Choose the grille shape and size for the BEST SOUND from the chosen speaker, not to fit leftover space. KEYS: more brass than black.

2026-11-13 17:37 Owner (verbatim): "name to come -- we're calling it big energy"
Recorded as: DECISION — the instrument is named **Big Energy**. Replace "( name to come )" on the site and in new work; locked versions stay as they were.

2026-11-13 18:00 Owner (verbatim), with a screenshot of the CATHEDRAL lid panel (design/owner-refs/2026-11-13-1800-top-panel.png): "lets focus on top panel first -- the items do not appear to be grouped or ordered in a way that makes logical sense. have the team break down which concepts belong together, and reorient accordingly.  there are tons of examples on the internet of good organization beyond the model d itself for the add'l functionality. also i dont like the effects controls at the top ... when i think of signal order it's synth stuff -> fx stuff -> output stuff like volume. so it at the top of the layout is confusing"
Recorded as: CATHEDRAL not approved yet. Focus on the TOP (lid) PANEL first. Its controls are not grouped or ordered logically: break down which concepts belong together and reorganise. Look at well-organised synths beyond the Model D for the added functions (effects, pans, sync, etc.). Signal order must read synth → effects → output (volume etc.); effects across the top is confusing.

2026-11-13 19:20 Owner (verbatim): "run it by the audio engineer synth expert for understanding"
Recorded as: independent expert (audio engineer / synth designer) review of the new CATHEDRAL lid layout: does a player understand it?

2026-11-13 19:31 Owner (verbatim), on sending the synth expert's lid fixes to the team: "Yes but make it a 10 not a 9"
Recorded as: send ALL the expert's lid fixes to the team. The bar for this lid is a 10 from the director, not a 9.

2026-11-13 19:57 Owner (verbatim): "Labels should only be one word and follow best practices with obvious tweaks for understanding if there's a better word than the jargon"
Recorded as: RULE for panel labels: one word each, following synth labelling best practice; replace jargon with a plainer word where one is clearly better.

2026-11-13 20:29 Owner (verbatim): "I’m fine with another oscillator but we’re getting really cramped in the top case. I also feel like master tuning controls should be closer to the oscillators and volume/mixer controls on the bottom case. I’m not sure how much physical space each pot actually needs but I think we should keep pushing the organizational logic in the cases. Also there needs to be a more harmonious / proportional approach to spacing from the knobs to the edge of the case inclusive of clear labeling. And I like the speaker grille but what’s better lines or a cool grid of dots?"
Recorded as: CATHEDRAL not approved yet. (1) OK with the 4th oscillator (PARA+4 path; orchestrator noted it adds no panel control). (2) The lid feels cramped. (3) Master tuning (tune, drift) should sit closer to the oscillators; volume and mixer controls should move to the BASE. Keep pushing the organisational logic across both cases. (4) Harmonious, proportional spacing from knobs to the case edge, including clear labels. (5) Speaker grille: lines or a grid of dots — team to recommend on sound and looks. He asked how much space each pot needs.

2026-11-13 20:33 Owner (verbatim), after hearing that Moog paraphonics (Matriarch) use four analog oscillators each with its own wave control: "See if we can fit a fourth oscillator"
Recorded as: study a 4th ANALOG oscillator (Matriarch-style, its own octave, wave, pitch and mixer level) in place of, or alongside, the digital 4th voice: electronics, cost, power, board space and panel space. Orchestrator reading; to confirm with him if it matters.

2026-11-13 20:43 Owner (verbatim): "I feel like the oscillators should all be stacked on the left, then top case filter/envelope where there’s less room cuz of speaker in the middle, then amp controls going left to right in the top row on the top case"
Recorded as: lid layout direction from the owner: oscillators stacked in a block on the LEFT; filter and envelope controls in the middle area around the speaker (less room there); amp controls running left to right along the lid's top row. ("Amp controls" most likely = the amp envelope; team to confirm against the steer-5 rule that puts volume on the base.)
2026-11-13 20:43 Owner (verbatim): "Don’t stop the other exploration tho I wanna see what they came up with too"
Recorded as: keep the team's own steer-5 arrangement going AND do his layout; show both.
2026-11-13 20:44 Owner (verbatim): "I think we can bring the spine back if we can make it look good"
Recorded as: the spine (closing the back slot) is back on the table, only if it looks good. Reverses the 14:40 "I don’t want a spine" conditionally. Earlier dislikes: the oxblood colour felt unnecessary.
2026-11-13 20:45 Owner (verbatim): "I kinda want the corners to be softer and to be more architectural like how Apple does theirs"
Recorded as: corners (case and faceplates) softer, with Apple-style continuous-curvature corners (superellipse / G2 "squircle" rather than a plain circular radius).

## 2026-11-14 01:27
> I want to see all the layout options before I make a call. Yes I meant the amp envelope controls.. the amp group.

## 2026-11-14 01:29
> The top case is looking ok in p50 but the bottom is a bit less senseful

## 2026-11-14 01:32
> Also in p50 the oscillators are really far apart, the mod and track control placements feel random. As does the envelops label, the echo types and reverb types knob labels, the markings around the knobs are all inconsistent, the out pan makes no sense. This is not a 10

## 2026-11-14 01:32 (b)
> Have a synth expert who has deep understanding of playing synths be devils advocate until he or she thinks it’s good

## 2026-11-14 01:33
> Also it doesn’t need to say big energy

## 2026-11-14 09:44–09:46
> We’re getting closer. I’d like a view where I can drag around the controls / align / etc. To a grid and whatnot. What’s the best way to do this? I could do it in figma or if there’s a better app for this kind of design with an mcp
> Why is there the 5mm grid? Just curious
> Cool that’s great we have a harmonious grid. I’m curious about that scale, I might play with it. Ideally it’d be derived from the dimensions of the device as well
> Yeah I would rather base it on the face dimensions / ratio

## 2026-11-14 12:12
> Re the case dimensions is there a more pleasing and harmonious case ratio for the concept? Have the team look

## 2026-11-19 13:53
> what about a version with changes like this?

(Screenshot: design/owner-refs/2026-11-19-1353-P5R-markup.png, a markup of P5R with ratio A. Blue box "Stack" round VCO 2 and VCO 3 (and track), with an arrow to the filter-envelope position. Red box round the filter envelope, with an arrow to the top right where VCO 2/3 sit. Orange box round echo + reverb: "center?". Magenta box round keys (voices, velocity, touch), with an arrow to the base: "will probably need to be a tighter proportional grid for these if all the key controls are in one area?")

## 2026-11-19 14:08
> re: the echo and reverb levels moving.. when i said to move the keys stuff, i was hoping the grid could be altered in that section along, making the switches a bit tighter / in a proprotional multiple of the grid.
> i dont want those two knobs to move, as your analysis said

## 2026-11-19 14:36
> yeah this still isnt perfect to me. i think we should go back to the fundamentals and figure out how to make these lay out in a more logical sense. let's start by doing a tree map or something first and just define the categories of controls and what controls belong in those categories before laying anything out.

(Attached: design/owner-refs/Minimoog_Model_D_Manual.pdf)

## 2026-11-19 16:19
> yes these categories look correct. *now* let's try and lay these out

(Q0 answered yes: taxonomy categories and membership approved.)

## 2026-11-21 13:38–14:17 (chat, comparing the Behringer Pro-800, paraphony and polyphony)
> I like the synths you mentioned more than the model d sound wise. Just chose model d for simplicity. Polyphonic would be amazing.

> I'm more thinking the portability factor.

> Analog voices, shimmer and warmth

(Answer to "what grabs you most" across the OB-6, the SEM and string machines.)

> I want to pivot— I don't need a model d it's not inspiring to me

Recorded as: PIVOT APPROVED. The Model D voice is no longer the instrument. Direction: a portable polyphonic instrument with analog voices, shimmer and warmth. Open: what carries over from the current build, budget ceiling, name.

## 2026-11-21 18:09 (chat)
> String machine and analog poly are way more inspiring than model d.  We could go back to first principles with string machine too while still proving out the platform

(Context: asked whether a string machine is cheaper and easier to build first. Orchestrator's answer: easier, likely cheaper but the shared platform costs the same, partly on target since it has no individual analog voices.)

Recorded as: both the string machine and the analog poly are inspiring. Owner floated building the string machine first, from first principles, as the way to prove out the platform. Pending owner confirmation that it is the first build.

## 2026-11-21 18:10 (chat)
> Port-a-poly is an amazing name for the portable poly tho. Maybe I do a model d later

Recorded as: working name for the portable analog poly: PORT-A-POLY. A Model D build may come back later (the paused full-instrument work stays in archive/). String machine as the first build is still awaiting confirmation.

## 2026-11-21 18:19 (chat)
> No build decisions is wrong. I want to make build plans like big energy idk what I'll build first is all

Recorded as: make full build plans (the Big Energy way: design loop, specs, verification) for the string machine, and later Port-a-poly. Which one gets built first is undecided. Don't ask him to pick the first build yet.

## 2026-11-21 18:31 (chat)
> Right now I'm thinking big energy is the model d clone with 4 voice paraphony, port-a-poly is the true poly, and the string machine needs a cool name

Recorded as (current thinking, three instruments): **Big Energy** = the Model D clone with 4-voice paraphony (as specced: voices 1 · 3 · 4). **Port-a-poly** = the true analog poly. **String machine** = needs a name. This supersedes "the Model D voice is no longer the instrument" from earlier today: the Model D lives on as Big Energy. Build order still undecided.

## 2026-11-21 19:12 (chat)
> No I named big energy along the way name isn't important right now

Recorded as: no naming round for the string machine. Adam names instruments himself along the way; the name isn't a priority now.

## 2026-11-21 19:17 (chat)
> First let’s get the feedback site organized. Big energy should be a section, as should port a poly, as should this untitled steering machine. The repo should be more about the synths to go concept

Answers to follow-up questions (19:2x): rename the repo to **synths-to-go** (Adam renames it in GitHub Settings; the site moves to adamtrabold.github.io/synths-to-go); "Synths to go" is a **working title only**; run the restructure as a **tweak**.

Recorded as: the site gets an umbrella, "Synths to go" (working title), with three sections: Big Energy, Port-a-poly and the untitled string machine. The repo is reframed around the synths-to-go idea and renamed synths-to-go. Each new instrument has its own folder (`port-a-poly/`, `string-machine/`); Big Energy's files stay where they are for now.

## 2026-11-21 20:14 (chat)
> Let’s make it “synths-to-go” with a pipe next to it and a dropdown for the page selector so there aren’t stacked tabs

Recorded as: the site header reads "synths-to-go | <instrument>", where the instrument is a dropdown (Overview, Big Energy, Port-a-poly, String machine). There's only one row of tabs: an instrument's own sections, such as Big Energy's. The umbrella is written "synths-to-go".

## 2026-11-21 20:35 (chat)
> Make names and tabs all lowecase

> Call string machine floss

Recorded as: on the site, instrument names and tabs are all lowercase (big energy, port-a-poly, floss; to decide, designs, …). The string machine is named **floss**, and its folder is `floss/`.

## 2026-11-21 22:38 (chat): floss keys
> Re range it would be nice to octave select each half of the keyboard
>
> Re velocity it would be cool to innovate on the original string synth with velocity
>
> Re platform I do not want extended keyboard. Portable means 25 or less.

Recorded as: floss has **25 keys or fewer**, never an extended keyboard ("portable means 25 or less"). It has a **split with independent octave select for each half**, and it **uses velocity** to innovate on the classic string machine.

## 2026-11-21 22:41 (chat): floss aftertouch
> Yes let’s look to innovate

(Answering: keep Big Energy's shared pressure strip, or look into per-key pressure.) Recorded as: look into **per-key pressure** for floss rather than defaulting to the shared strip. It isn't decided yet: feasibility comes first (key travel, reading the bottom of the press with the Hall sensors).

## 2026-11-21 22:41 (chat): floss pressure destination
> Would be cool to select what the pressure strip does

Recorded as: the pressure destination on floss is **selectable** by the player (for example volume swell, filter or shimmer depth). This applies whether pressure ends up per-key or a shared strip.

## 2026-11-21 22:42 (chat): floss power
> I’d like to know more about power tradeoffs before making any decisions there

> I want to keep it battery powered

Recorded as: floss is **battery powered**. Pack size, runtime and the power design wait for a proper power budget, once the voice and shimmer choices are made.

## 2026-11-21 22:44–22:46 (chat): floss speaker
> Yes speaker let’s see what two would mean but I’m not sure— would we need stereo controls for the shimmer? How do other synths do it

> Is the op 1 field analog

> Yeah one speaker unless headphones just as on big energy

Recorded as: floss has **one built-in speaker**, which mutes when headphones are plugged in, as on Big Energy. Stereo is for headphones and outputs. No separate stereo controls for the shimmer were asked for.

## 2026-11-21 22:46 (chat): floss passive radiator
> Passive radiator would be cool

Recorded as: look into a **passive radiator** with floss's speaker for fuller sound. It isn't decided yet: it needs a sealed air space inside the case, so the enclosure work has to show it fits.

## 2026-11-21 22:50 (chat): floss shimmer
> Analog mode on shimmer but modes to use the daisy too

Recorded as: floss's shimmer has an **analog mode** (bucket-brigade ensemble) and **Daisy (digital) modes** as well. Echo and reverb stay on the Daisy, as on Big Energy.

## 2026-11-21 22:55 (chat): floss MIDI
> Yes. Sure midi split could be on/off and yes re the velocity and pressure.

Recorded as: floss **keeps Big Energy's MIDI rules**: USB-MIDI plus TRS in and out, synth settings controllable over MIDI, MIDI never flips switches, knob-only controls send no MIDI, and the echo syncs to MIDI clock. A **MIDI split can be turned on or off**: on, each half has its own channel; off, one channel. **Velocity and pressure go over MIDI**, with polyphonic aftertouch if per-key pressure proves feasible.

## 2026-11-22 08:27 (chat): floss panel rules
> Let’s try without

(Answering: should floss keep "no screens, no encoders, real knobs and keys"?) Recorded as: **try floss without screens or encoders**, using real bought knobs and keys, as on Big Energy. The designers must be strict about which choices earn a physical control. Read as "try without screens"; if Adam meant without the rules, this entry is wrong.

## 2026-11-22 08:29 (chat): enclosure, shared universe
> Yes let’s make these as a shared universe and reuse as much as we can

Recorded as: the synths-to-go instruments form a **shared universe**. floss (and the others) **reuse as much as possible** from Big Energy's enclosure family (ONE SHEET / FOLD formats, CATHEDRAL) and shared parts, changing only what floss's own needs require.

## 2026-11-22 08:34 (chat): floss budget, go
> Budget ceiling should be what we can to hit the desired goal. Let’s go on the design loop

Recorded as: **no fixed budget ceiling for floss.** Spend what it takes to reach the goal, while still costing everything honestly. **The floss build-plans design loop starts now.** Work folder: `floss/design/`.

## 2026-11-22 09:22–09:29 (chat): process for floss
> How is the design loop helpful right now? Is it like we design the look first then the architecture to fit? Or is the designer designing the architecture? Do we have all of the components and circuits figured out?

> Pressure test this plan with another agent

> I don’t know what the right process is with synth design

> I would imagine we’d need requirements first

> Surface mount is fine if necessary. I don’t want to test the keys they should be reliable copies

Recorded as: the order of work changes to **requirements first** (decisions plus measurable targets Adam confirms), then an **engineering gate** (2–3 engine options costed side by side, fit against each case with the battery, and per-key pressure judged on proven designs), then concepts revised and scored, then Adam picks, then the full spec. The design loop's round 2 is paused until the gate is done. **SMD is allowed for floss where necessary**, which relaxes Big Energy's through-hole rule. **No physical key test by Adam:** the keys and the pressure sensing must be reliable choices (corrected below).

> Choices *

(Correction to "reliable copies" above.) Recorded as: the keys and pressure sensing must be **reliable choices**, meaning proven parts and approaches, not experimental ones.

## 2026-11-22 09:38 (chat): requirements targets
> Sure but if we can do better or need to do worse tradeoffs should be discussed

Recorded as: targets T1–T12 in `floss/REQUIREMENTS.md` are **confirmed as the baseline.** Any place engineering could beat a target, or has to miss one, comes to Adam **as a trade-off to discuss**, not decided quietly.

## 2026-11-22 10:09–10:17 (chat): floss keys
> Let’s talk keys. Make sure we’re not assuming things. All a key has to be is something we can press that can record various pressure levels. We had ideas on big energy but not finals. We can reuse anything we do here there. Look at first principle approaches.

> I don’t like springs because they give over time and also I *am* building this so I want something feasible. Pads are fine imo

Recorded as: floss uses **pressure pads, not moving keys** (keys.md S3 family: LinnStrument/QuNexus-style pads over force sensing). No spring-key mechanism. **Adam builds floss himself**, so feasibility for a home builder is a hard requirement. Whether Big Energy adopts pads too is not decided.

## 2026-11-22 11:14–11:22 (chat): playing surface
> What about just touch pads?
> Like metal
> Can touch pads sense finger placement as well? Eg side to side wiggle?
> What about layering boards? Like a cut top board that connects traces to a bottom board
> Or what about a touch strip with predefined areas OR markings that could allow for continuous glide
> Just exploring options. The cost of pads seems egregious compared to the market
> I don’t feel like the layered boards would feel very good
> I like the soft silicone idea if we’re not going button or classic keys

Recorded as: **preferred feel is soft silicone** (LinnStrument/Seaboard-like), if floss doesn't use buttons or classic keys. The ≈ $300 of bought FSRs is **too expensive**: find cheaper reliable sensing under silicone. Side-to-side position, metal tops, layered boards and glide strips were exploration, not requirements. Layered boards are out on feel.

## 2026-11-22 11:27–11:30 (chat): no measuring, agents only
> Do more research on the response time thing

> I don’t want to measure anything. I’m truly to see how far agents alone can get me. How would an agent solve this problem? Also how do real instruments do it?

Recorded as: **Adam measures nothing.** Choices must rest on published evidence: datasheets, teardowns, papers and shipping products. This project tests how far agents alone can get. Any part whose key spec is unpublished counts as unverified.

## 2026-11-22 11:52–12:00 (chat): bought or transplanted controller
> It feels like the keyboard is the most expensive part. What if instead we made it Bluetooth MIDI or usb MIDI capable and just used a portable MIDI controller for the keyboard like the Korg nano key

> I’m getting curious now about stealing a keyboard from an existing controller

> Yeah research the options

Recorded as: research floss played by an **existing controller**, either separate (USB/BLE MIDI) or **transplanted** inside floss's case (the controller's own board and firmware kept, connected internally over USB). Rewiring bare keys is out (it needs measuring). Candidate donor: KMI QuNexus (silicone keys, velocity, poly aftertouch, tilt).

## 2026-11-22 12:23–12:26 (chat): floss becomes a sound module
> Do you think do it yourself pads will get us even close to experience parity with an existing solution? Also did the research keyboards too or just pads

> And why did the price drop so much on the keyboard you recommended

> Yeah I don’t think pads are my preferred feel they were just what we were exploring. I like the idea of focusing on the sound module now and making it so a travel MIDI controller can be carried with the module

Recorded as: **floss is a sound module with no built-in keys**, played by a **travel MIDI controller over USB** (floss is the USB host and powers it). Floss is **designed so the controller can be carried with it**. Pads were exploration, not his preferred feel. The silicone-pad and spring-key work is shelved. The split, octave per half and MIDI split live in floss's firmware and panel and work with any controller. Per-key pressure comes from the controller when it sends polyphonic aftertouch or MPE (e.g. CME Xkey 25 with slim keys, Muse Kinetics K-Board C with pads), with a fallback to channel pressure and velocity.

## 2026-11-22 12:28 (chat): family principle
> This is the plan for all modular portable synths that we build — portable sound modules with a way to carry a keyboard with it. It should be flexible and not reliant on a single model of keyboard.

Recorded as: **a synths-to-go family principle.** Every portable synth in the family is a portable sound module with a way to carry a keyboard with it. The carrying method and the connection must be **flexible and not tied to one keyboard model**: any class-compliant USB MIDI controller within a size range, with no fitted dock for one product. Whether this changes Big Energy's locked v1.1 (which has built-in keys) is open; ask Adam.

## 2026-11-22 12:29 (chat): Big Energy changes too
> I’m saying big energy has to change too yes this is a systems philosophy decision

Recorded as: **a systems philosophy decision for the whole family. Big Energy changes too:** it becomes a portable sound module with a carried keyboard, like floss. That supersedes v1.1's built-in keys and aftertouch strip; the rest of v1.1 (voice, filter, effects, panel work) is reviewed against the module shape. port-a-poly follows the same principle. When the Big Energy rework starts is open.

## 2026-11-22 12:30 (chat)
> No hybrid. We’ll go back to big energy later

Recorded as: **no built-in buttons** (no Organelle-style hybrid). The Big Energy module rework comes **later**, after floss.

## 2026-11-22 12:52 (chat): controller port, proportions
> Let’s do USB c and we can riff on the dimension ratios

Recorded as: floss's controller (host) port is **USB-C**, not USB-A. Proportions are **open for the design team to explore**: module size, how it relates to the keyboard, and one package versus two. T4's 290 mm is not a hard cap while they riff; trade-offs come back to Adam. Still to confirm (engineer's recommendations, used provisionally): the carry fits the slim class of travel keyboards; the faster charger and two-cell battery; a slim passive radiator; 25 voices.

## 2026-11-22 13:25 (chat): module width
> The module does not have to match keyboard width

Recorded as: **S8 ("every module is 400/412 wide") is not adopted.** The module's size is set by its own needs, not the keyboard's width. The carry still has to take any travel keyboard in the slim range.

## 2026-11-22 13:29 (chat): module size and shape
> It needs to fit in a backpack comfortably. Ideally like the size of a sheet of paper length wise. But it also does not have to be a rectangle. It should be a thoughtful ratio base

Recorded as: **the module fits comfortably in a backpack, ideally no longer than a sheet of paper's long side** (US Letter 279 mm / A4 297 mm). **It doesn't have to be a rectangle**; its proportions come from a **deliberate ratio**. Read as the module; the whole kit (module plus a travel keyboard up to ~390 mm) must also fit a backpack comfortably.

## 2026-11-22 13:49 (chat): weight
> I didn’t create the weight target. The principles are portable.

Recorded as: **T5 (≤ 1.5 kg) was the orchestrator's proposed number, not Adam's.** It's withdrawn as a hard target. The principle is **portable**: lighter is better, and weight is reported and weighed as a trade-off, not pass/fail.

## 2026-11-22 13:51 (chat): don't anchor on paper size
> Also don’t anchor on the page size thing. I’m just giving examples of generic things. It just needs to be portable and make sense and be harmonious

Recorded as: **the sheet-of-paper size was an example, not a target.** The module needs to be **portable, make sense and be harmonious**. Its dimensions and proportions are the team's to derive (from its parts, use and a deliberate ratio). Don't anchor on A4, Letter or A-series ratios because of that remark.

## 2026-11-22 13:54–13:55 (chat): foundational principles; site as source of truth
> In fact, let’s go back to the overall project principles here. I think we may need to do some foundational work in the GitHub. I don’t want each synth to have the core things relitigated, so let’s start documenting these core principles and goals. The size and principles about harmonious ratios are foundational things, and we have portability as a goal alongside the harmonious principles, so let’s get some good documentation there so that it’s available for every agent on this contextually

> I want the website to serve as the source of truth and guiding light for this project

Recorded as: **`PRINCIPLES.md`** at the repo root holds the family's foundational principles and goals in Adam's words, with dates. **`CLAUDE.md`** tells every agent to read it first. **The project site is the source of truth and guiding light:** it gets a "principles" page (built from PRINCIPLES.md) and leads its overview with it. Repo files feed the site, so the two stay in step.

## 2026-11-22 14:06 (chat): trim principles; analog-first
> Remove any language that isn’t necessary from the principles/mds. The sound things / shimmer and warmth things are overstated those were notes about the string machine. The goal is analog-first, but that doesn’t mean digital won’t be used or should be completely avoided.

Recorded as: PRINCIPLES.md and CLAUDE.md trimmed to what's necessary. **"Analog voices, shimmer and warmth" is floss-specific, not a family goal.** The family goal is **analog-first; digital is used where it serves.** The site and README now say "portable, analog-first synthesizers".
