# Owner answers

## 2026-11-12 — Q1 (printer / bed size)
Owner (verbatim): "idk what printer i have here's the maker space i belong to https://vector-space.org/wiki/Main_Page"

Orchestrator research from the Vector Space wiki (Tool User Guides, 3D printer and laser guides):
- FDM printers: Lulzbot Mini 2, Lulzbot TAZ6, Gigabot GB2, Prusa Core One (several), Prusa MK3/MK3S+/MK4/MK4S, Voron Trident, Voron 2.4r2. Build volumes are not listed on the wiki. Typical manufacturer volumes (UNVERIFIED for these specific units): Prusa MK4 ~250x210x220 mm, Core One ~250x220x270, TAZ6 ~280x280x250, Voron 2.4/Trident built in 250/300/350 mm sizes, Gigabot is large-format (~590 mm class). So a ~300 mm part is likely printable on the TAZ6/Gigabot/Voron, but the common machines are ~250 mm.
- Filaments: PLA, ABS, PETG, NinjaFlex (TPU), HIPS. No multi-material system mentioned.
- Also available: resin printer, 100 W and 150 W CO2 laser cutters (wood, plywood, acrylic, Delrin, leather, felt, cork), fiber laser (can mark stainless/aluminium), CNC router, Tormach CNC mill, vinyl cutter, powder coating, letterpress, screen printing, sewing machines incl. industrial and embroidery, large format printer.
- Owner has separately worked with walnut (furniture/built-ins).
Implication: enclosure options go beyond FDM printing — laser-cut ply/acrylic, CNC'd wood, fiber-laser-marked aluminium panels, sewn/leather cases are all on the table.
Q2–Q5: not yet answered.

## 2026-11-12 — Q3/Q4 + new requirements
Owner (verbatim): "i dont think click would make sense for a keyboard.. i want it to feel like an instrument. built in speaker would be incredible but it needs outs. also would be cool to be able to pass things into the filters and whatnot. and to control via midi."
Recorded as:
- Playing surface: should not feel like a clicky computer keyboard; must "feel like an instrument". (Interpretation of what that means — real key travel/action, expressive touch, etc. — is the team's to propose; do not assume touch pads are ruled in or out beyond this.)
- Built-in speaker: YES, plus outputs (line/headphone).
- External audio input into the filter/mixer path ("pass things into the filters and whatnot") — likely also CV patch points; scope TBD with eng.
- MIDI control: YES.
Q5 (hand-lettering / look): not yet answered.

## 2026-11-12 — Q5 (lettering / look)
Owner (verbatim): "i can make the labels myself or hand paint it or something based on outcome. id have to see mocks of the ideas to tell you which look appeals"
Recorded as: open to hand-made labels or hand painting, depending on the outcome. Look direction cannot be chosen from words — owner needs visual mocks of the directions before choosing.

## 2026-11-12 — direction for the concept set
Owner (verbatim): "it'd be cool to see some expected / highly designed for use cases, and others using more of the randomness/creative principles to drive unique outcomes that have more sauce / vibe"
Recorded as: the concepts shown to the owner should span two kinds — (1) expected, highly designed-for-use concepts, and (2) concepts driven harder by the randomness/creative principles toward unique outcomes with more character ("sauce / vibe"). Both kinds should be represented.

## 2026-11-12 — MIDI control of parameters
Owner (verbatim): "i dont think recall is important, but controlling it in midi is good — im not sure how to reconcile that with the knobs because i'd want to use the knobs to control the midi... if it was set to a different state than zero on start id imagine the midi would override it but i dont need the knob to move... it should change value once i move the knob, but be using that prior setting by default if midi is controlling it at a prior setting and i haven't explicitly changed it"
Recorded as:
- No preset recall needed.
- Parameters should be MIDI-controllable (MIDI CC in), and knobs should also send MIDI ("use the knobs to control the midi").
- Knob/MIDI conflict behaviour: last-touched wins. If MIDI has set a parameter, the instrument uses the MIDI value even though the knob sits elsewhere; the knob does NOT move (no motorised pots). Once the owner physically moves the knob, the parameter takes the knob's value (jump-on-move).
- Engineering implication (orchestrator note): knobs that are MIDI-controllable must be read by the MCU, which drives the analog circuit via CV (DAC) — the audio path stays analog, but the pots are no longer directly in it. Scope (which controls, cost, sound-character risk) is for eng to propose.

## 2026-11-12 — endless encoders / screens?
Owner (verbatim): "i dont think i want a bunch of mini led screens and infinite twisting knobs so that recall can happen perfect... or do i? you tell me"
Orchestrator answered: recommended ordinary pots, no LED rings/screens (keeps the panel readable as the patch, instrument feel, battery life, kit simplicity); jump-on-move covers MIDI. Mentioned an optional single "a knob is not in control" LED as a middle ground. Owner has not yet replied — treat "no endless encoders / no screens" as the working assumption, not a confirmed decision.
NOTE: the earlier line "MIDI plays notes but can't turn the knobs" is SUPERSEDED by the MIDI-control section above — parameters ARE to be MIDI-controllable via MCU-driven CV, with jump-on-move.
Owner reply (verbatim): "yeah exactly. explore the light thing i guess im not sold either way but its not a bad idea"
Recorded as: CONFIRMED — no endless encoders, no LED rings/screens. The "knob not in control" indicator light is open: explore it, owner undecided.

## 2026-11-12 — jobs confirmed; decisions
Owner (verbatim), replying to the orchestrator's jobs list (J1–J19, with J15 eurorack patching flagged as a scope question), the THT/SMD answer, the envelope analog-vs-digital discussion and the kit-selling note: "all of this yes."
Recorded as:
- jobs.md J1–J19 confirmed as written; J15 (eurorack patching: pitch/gate in+out, filter CV in, loudness CV in) is IN SCOPE.
- Earlier owner words on build: "as long as its factory assembled. I *dont* want to do surface mount if we can avoid it i always fuck itup." → all SMD arrives factory-assembled.
- Earlier owner words on envelopes: "i want analog wherever i can generally." Orchestrator leaned toward analog CV-controlled envelopes pending eng numbers; owner's "yes" endorses that lean, final call after eng's comparison.
- Owner may want to sell the kit later ("if this is great can i sell the kit with that?") — design as if it may be sold: clean-room schematic (CA-72 only as oracle), no Moog name/trade dress, plan for FCC emissions question.

## 2026-11-12 — cost reset: ready-made modules, no factory minimums, small
Context: cost estimate came back at ~$1,150–3,530 first unit; owner: "oh wow this is way more than i expected." / "i dont want to order any factory minimums -- aren't there one-of pcb makers?"
Orchestrator proposed: no custom factory assembly at all; every custom board is a bare through-hole board the owner solders; all SMD comes as ready-made assembled modules bought from US vendors (Pico 2, charger, DAC breakouts…) that plug into sockets. Caveat stated to owner: likely reduces MIDI control to notes/bend/mod/glide/cutoff, other knobs directly in the circuit (more analog).
Owner (verbatim): "yeah let's use readymade modules. remember the size of this thing needs to be portable anyways...which means small."
Recorded as:
- DECISION: ready-made modules only; no custom PCBA; bare boards only (no factory assembly minimums). This collapses the two build variants into ONE: hand-soldered through-hole + plug-in ready-made modules.
- MIDI parameter control scope reduces to what ready-made modules allow (eng to maximize within that); jump-on-move behaviour still applies to whatever is MIDI-controllable.
- SIZE: "portable … which means small." Current concepts at ~315 mm wide are likely too big — size is now a primary constraint. Exact target not yet given (asked).
- Cost matters: owner expected much less than $1,150+.
Size target — owner (verbatim), choosing from OP-1 (~28 cm, laptop-sleeve) / Volca (~19 cm) / Pocket Operator (~12 cm): "id say op1 is probably the better size ref"
Recorded as: SIZE REFERENCE = Teenage Engineering OP-1 class (~28 cm wide; OP-1 is roughly 282 × 102 × 13 mm per orchestrator's recollection — UNVERIFIED, check). Width ~28 cm and slim/flat is the target, not ~315 mm and chunky.
Owner (verbatim): "experiment with key ideas. but two octaves from a width perspective does feel like a minimum shouldn't effect pcb size."
Recorded as: two octaves (25 keys) across the width is a MINIMUM, within the OP-1-class ~28 cm width. Experiment with key ideas. The key mechanism / key count should not drive the main PCB size (keys sensing kept off the main boards — e.g. its own thin strip or mechanical-only).
Owner (verbatim): "dont over index on OP1. thats just a reference. it should feel good to use."
Recorded as: OP-1 is a loose size reference, not a hard limit; feeling good to use outranks matching OP-1 dimensions. (~285 × 180 mm depth from eng is acceptable in principle.)
Owner (verbatim): "i'd love a version that gets to the $100 range but keeps the spirit of the device"
Recorded as: explore a ~$100 version (one-unit cost) that keeps the spirit of the instrument. Whether it replaces or sits alongside the ~$490–810 version: asked, not yet answered.
Owner (verbatim): "separately -- lets keep the expensiver one too"
Recorded as: TWO instruments, developed separately: (1) the full version (~$490–810, module-based, current concepts); (2) a ~$100 budget version that keeps the spirit. Design loop for the full version continues; the budget version gets its own spec/costing first.

## 2026-11-12 — budget instrument ("Little D") decisions
Owner (verbatim): "i dont want to build five. this is a test unit. what are hall effect keys is that in the original? what if we cut the speaker? is there a way to avoid tarrifs? i'd like to keep 3osc if possible. what if we used something other than wheels for the wheel thing like touch strips or something?"
Owner (verbatim), replying to orchestrator's proposed spec (3 osc, touch strips, keep speaker, ~$150–180 one unit): "yeah i also need all the waveforms. i dont need the additional patch poits. but i do need original chips. what about op-1 style keys? i guess i havent seen the idea, so i dont know how hte keys are designed, but they dont have to be a traditional keybed"
Recorded as (budget instrument):
- ONE test unit, not a batch of 5.
- 3 VCOs; ALL original waveforms (tri, shark, saw, square, wide & narrow rectangle).
- "Original chips": original-style expo/transistor parts (AS3046 = modern equivalent of the obsolete CA3046 used in the 1972–73 board; matched pairs) — orchestrator to confirm the owner means this, since true originals are obsolete.
- Bend/mod control: OPEN. Touch strips were the owner's "what if" option, NOT a decision (owner correction 2026-11-12: "dont assume touch strip i said it was an option"). Wheels, touch strips or other ideas all still on the table.
- Speaker kept (saves only ~$2 to cut).
- No additional patch points beyond the base spec (pitch CV/gate out, filter CV in).
- Tariff exposure small (~$6); prefer US distributors for parts.
- Keys: open to OP-1-style keys (flat, short-travel buttons in piano layout); "they dont have to be a traditional keybed". Owner hasn't seen the key ideas yet. Earlier owner words still apply: "i dont think click would make sense for a keyboard.. i want it to feel like an instrument."
Owner (verbatim): "i dont need vintage parts" → CONFIRMED: "original chips" = modern pin-for-pin equivalents (AS3046 etc.), not vintage/NOS parts.
Owner (verbatim): "maybe explroing weirder keys could be cool like on the korg phase8/critter and guitari stuff... or the op1"
Recorded as: key references the owner likes: Korg phase8 (pluckable/tappable steel resonator tines — a kalimba-like playing surface), Critter & Guitari (Organelle/Pocket Piano: rounded polished maple peg keys poking through the case, springy, tactile, no velocity), OP-1 (flat short-travel buttons). Explore weirder key ideas in this spirit, for both instruments.
Owner (verbatim): "i do want them to be as silent as possible though"
Recorded as: keys must be as silent as possible — a hard criterion for every key idea (rules against clacky pegs/tact switches unless damped; favours contactless Hall sensing with felt/TPU stops).
Owner correction (verbatim): "no the phase 8 i mean the buttons not the kalimba meta parts"
Recorded as: the phase8 reference is its row of individual button keys (one per voice, under per-key knobs), NOT the steel resonator tines. Orchestrator could only verify they're described as "individual button keys" / "touch-sensitive keys/pads"; their exact mechanism wasn't found — designers should look at product images/manual (cdn.korg.com phase8 manual) before borrowing from them.
Owner (verbatim): "or even drum machine style pads in a key form factor / layout could be cool"
Recorded as: another key idea to explore — drum-machine-style pads (soft silicone/rubber, velocity) arranged in a piano key layout.

Owner (verbatim): "dont assume touch strip i said it was an option. i *know* there are single board manufacturers who are you looking at that force 5?"
Recorded as: (1) touch strips are an OPTION only; bend/mod control is undecided. (2) Owner wants quantity-1 board fabrication; JLC's 5-board minimum is not acceptable as a default. Orchestrator found quantity-1 fabs: Advanced Circuits/4PCB BareBones (min qty 1, but no soldermask/silkscreen; $20 handling/order), AtlasPCB (1-piece MOQ, origin unverified), Ponoko (no MOQ, made in USA), Pad2Pad (from 1 PCB, USA), PCBCart standard service (no min). Prices for qty 1 need real quotes from board files.
Owner (verbatim), on the Little D one-unit cost ~$245–350 and the offer to get real board quotes: "i want to see everything first. 250 feels high. can we get creative with any of the knob / wheel styles? wheels seem to be cheapest."
Recorded as: (1) owner wants to see all the concepts/options (visuals) before committing to quotes or spend; (2) ~$250 feels high for the budget instrument — look for cuts; (3) explore creative, cheap knob and wheel styles (e.g. printed caps, thumbwheels, edge wheels) — wheels look cheapest for bend/mod; applies to the budget instrument at least.
Owner (verbatim), replying to "Would you 3D-print one-octave key samples and a few knob/wheel samples at Vector Space (~$50–80)?": "i dont want to print knobs and keys"
Recorded as: NO printed test samples. Ambiguous whether he also means no 3D-printed knobs/keys in the final build — asked. Q1 (knob-only controls send MIDI) and Q2 (MIDI flips switches) unanswered.
Owner (verbatim): "yes finished instrument should be real parts"
Recorded as: CONFIRMED — the finished instrument (both versions) uses bought, real parts for knobs, keys, wheels and other user-touched controls; no 3D-printed knobs/keys/wheels. (Enclosure may still be laser-cut/CNC at Vector Space per earlier answers; 3D printing only where invisible/structural, if at all — designers to flag any printed part.)
Owner (verbatim): "knobs midi cant control should not send midi and midi should not be able to flip switches. midi should just send the data and the instrument should control the sound except for the jump thing we talked about"
Recorded as: CONFIRMED — knob-only (non-MIDI-controllable) controls do NOT send MIDI; MIDI cannot flip switches. The panel controls the sound; MIDI only overrides the MIDI-controllable parameters under the agreed last-touched / jump-on-move rule.
Owner (verbatim): "i dont want to steal a keybed -- where to places like teenage engineeringget their keys? or like the korg nanokey?"
Recorded as: NO harvesting keybeds from other products (rules out "keybed taken from a Nektar SE25" option). Owner wants a real, purchasable key part source like the ones manufacturers use.
Owner (verbatim), on whether laser/CNC-service-cut key tops (Delrin/acrylic/wood) count as real parts: "thats fine but im concerned about cost"
Recorded as: laser/CNC-cut key tops are ACCEPTABLE as real parts. Cost remains a primary concern.
Owner (verbatim): "i guess i could cut at vector space"
Recorded as: key tops (and enclosure) can be laser/CNC-cut by the owner at Vector Space — material cost only, no cutting-service fees.
Owner (verbatim): "look at other ways to do the bend / mod... could an x / y joystick or two joysticks work? or a mini one like the switches on the phase8 that doesnt have stops"
Recorded as: explore joysticks for bend/mod — one X/Y joystick or two joysticks — and a mini control "like the switches on the phase8 that doesnt have stops" (orchestrator unsure which phase8 control he means — asked).
Owner clarification (verbatim): "theyre like little tiny joysticks. sort of like a guitar tone switch. but maybe there are mini joysticks is the thing i was getting at"
Recorded as: explore MINI joysticks (tiny levers, like a guitar pickup-selector/tone switch in feel) for bend/mod.
Owner (verbatim): "touch strip is cool too. just getting creative here."
Recorded as: touch strips remain a liked option alongside mini joysticks/thumbsticks/wheels; owner is brainstorming, not deciding.
Owner (verbatim): "even a fader could be sweet"
Recorded as: faders are another bend/mod option to explore (brainstorming).
Owner (verbatim): "little dials would even work"
Recorded as: small dials/knobs are another acceptable bend/mod option (brainstorming).
Owner (verbatim): "i want velocity."
Recorded as: velocity-sensitive keys REQUIRED (both instruments). Rules out on/off-only switches unless an added sensor provides velocity.
Owner (verbatim): "lets do the joystick. indifferent on 1 vs 2... i think the bend mod differences maybe necessitate two? can they only go single direction? or did we find a spring back dial?"
Recorded as: DECISION — joystick for bend/mod (budget instrument at least; designers to confirm for full). 1 vs 2 sticks open; owner indifferent. Spring-return dial not yet found (center-detent pots exist; not verified as spring-return).
Owner (verbatim): "i need both behaviors. joystick is great if we can go one direction"
Recorded as: BOTH behaviours required — bend springs back to centre; mod stays where it's set. Joystick preferred IF it moves in one direction only (single axis). Orchestrator's proposal pending owner OK: a single-axis spring-return stick for bend (either a true single-axis part, or a standard thumbstick constrained to one axis by a slot cut in the panel), plus a non-sprung control (dial or fader) for mod.

## 2026-11-12 — keys: rethink
Owner (verbatim): "Rethink the keys from first principles with out discoveries in mind"
Recorded as: re-derive the key mechanism from first principles using everything learned so far (see the discoveries list in concepts/keys/discoveries.md), rather than iterating on the switch-per-key approach.
