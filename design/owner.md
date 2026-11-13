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
