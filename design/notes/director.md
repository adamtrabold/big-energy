# Director notes: Little D (budget instrument), physical design

## Steer 5 fixes 2, scores (2026-11-13 ~22:30; bar 10; NEW DIRECTOR): READ THIS FIRST
- **Handover.** Took over from the previous director, using its notes as history. Judged: P5R / P5O full tops (4aeda69, 9.9 px/mm), §19 (f8ba494), look doc rev 9.1, standing and spine renders.
- **Renders are stale (blocker for both).** `P5R-standing.jpg`, `spine-standing.jpg`, `closed-spine.jpg` and `spine-flat.jpg` are from 65a65ed (21:55); `P5O-standing.jpg` and both `lid-top-10.2` are from fe25ac1 (21:06).
  - P5R standing still shows the old layout: voices/mod in a left column, VCO order octave · pitch · wave.
  - spine-standing shows P5O with octave · pitch · wave.
  - The look doc shows P5R-standing next to the new tops, so he sees two different P5Rs. P5R's alt text is stale too ("middle row of voices and mod switches").
- **P5R: 9 (unchanged). The work changed:** the switch fix landed (voices / mod / track centred under VCO 1/2/3 on one line). That fixes the last round's blocker. Still short of 10:
  1. **Reverb heading:** it sits at fan-word height, pushed right off its group's centre. "shimmer" ends ≈ 3 mm before "reverb" on the same line, so it reads as **"shimmer reverb"**, a real effect name: a first-time-walk fail. ("pingpong … echo" is ≈ 20 mm apart, OK.)
  2. **Envelopes 5.9 mm off the window axis** (systems' stated compromise, because keys share the right side). Owner, 16:52, verbatim: "off center in that middle section is bad looking". A likely objection.
  3. **Row C gutters are 41.9 against row A's 22.6 / B's ≈ 22.6.** That passes the gap rule per row, but fails the proportion check: the rows don't share one rhythm, and the echo cluster then two voids reads as holes.
  4. Stale standing render (above).
  - VCO 4 doesn't fit P5R (−32.1 mm). That's the choice between the options, not a flaw in P5R. Stated in the doc.
- **Ruling: P5R doesn't need top-left headings.** Each option keeps one heading rule, applied everywhere: P5R centred, P5O top-left. P5R's reverb breaks its own rule (off-centre), so "centred" has to become true: every row-C heading centred over its group, on one heading line *above* the fan words.
- **P5O: 8 (unchanged). The work changed:** headings top-left, tuning pair, out slot, VCO 4 cost caption (present in the look doc). The new top-left headings created collisions, and the biggest owner miss was never addressed:
  1. **Amp is a column, not "going left to right in the top row".** Owner, 20:43, verbatim: "…then amp controls going left to right in the top row on the top case". My predecessor's steer-5 fix re-cast amp as a column mirroring filter, which overrode his literal words. On his own layout, he'll check his words first. Most likely objection.
  2. **Headings land on fan-word lines:** "tape **echo** pingpong" and "plate **reverb** shimmer" read as the names "tape echo" / "plate reverb". First-time-walk fail.
  3. **Headless switch bank:** voices / mod / track sit under a bare hairline, separated from VCO 2/3 by tuning. "mod" and "track" of what? (The base also has a "track", under "filter".) First-time-walk fail.
  4. **The right block is vertically cramped:** free·sync legend → reverb heading ≈ 5 mm; reverb "type" → out heading ≈ 4 mm. Echo legends are mixed: type below; time, repeats and pan above. "cramped" is his word.
  5. The stick lowered to 9.0 (cost captioned; engineering risk stays).
- **Fixes (numbered):**
  - **P5R:**
    - R1: move keys (velocity · touch) out of row B to the start of row C (keys | echo | reverb | out). Row B becomes filter | window | amp, symmetric about x 143: (247.4 − 2×54.9 − 46)/4 ≈ 22.9 gutters ≈ row A's 22.6. Row C: ≈ (247.4 − 89.9 − 35 − 39 − keys ≈ 30)/3 ≈ 17.8, which must be ≥ 15. Reading order wraps from amp to keys, which feed amp/filter. Fallback: keys on the A' switch line under tune / drift, which fixes B but leaves C at 41.9. Systems shows both with numbers; I pick by eye.
    - R2: the row-C headings centred over their groups, on one heading line above the fan words (≈ d 40, clear of the window circle and the name).
    - R3: re-render the standing view, and fix the alt text.
  - **P5O:**
    - O1: amp attack · decay · sustain as a left-to-right row on R1, per his words. Suggestion: centred on the window axis (≈ 123 / 143 / 163), right above the window. Systems re-lays the rest and reports with numbers what moves (the switches, tuning, echo) and what it costs. If it can't pass, show why, and the orchestrator asks him one question (below).
    - O2: each oscillator switch beside or under its own VCO, or all three under a real heading. "track" must read as VCO 3's.
    - O3: headings in a heading zone above the fan words, never on their line.
    - O4: right block: one legend side per group; ≥ 1M between a legend zone and the next heading.
    - O5: re-render the standing and spine views.
  - **Both:** a checker phrase rule: no heading may share a baseline band (± 1.5 mm) with another word within 8 mm horizontally. Then checker 0, re-render the full tops and standing views, and I check by eye.
- **Question for the owner (cheap, ask alongside):** "By 'amp controls going left to right in the top row', do you mean the amp envelope (attack · decay · sustain)?" Volume moved to the base by his 20:29 words, so the envelope is the only amp control left on the lid.
- **What keeps blocking a 10 (across rounds):**
  - (a) Words that don't overlap but sit on one line close together read as one phrase. The checker tests box overlap, not reading adjacency, so every heading move makes a new near-miss (track/envelopes before; shimmer reverb and tape echo now).
  - (b) Proportion is checked per row, never across the plate, so rows can each pass and still disagree.
  - (c) On P5O, the team (and the last director) re-interpreted the owner's literal words instead of drawing them first and asking.
- **Watch:** "out" heads groups on both halves (lid pan/link, base volume). That's acceptable under the different-heading rule; it's flagged only if he or the expert misreads it.

## Steer 5 fixes, scores (2026-11-13 ~21:40; bar 10): READ THIS FIRST
- **Judged:** P5R and P5O full tops (a80d7c / 65a65ed), spine standing render. The owner has already seen these drafts on the Designs page.
- **Shared base: passes.**
  - Equal gutters in both rows (≈ 25–30 mm).
  - Read across x it runs controllers → mixer → filter → effects → out → tempo.
  - The controllers heading spans release/blend + bend/mod/glide.
- **P5R 9.** Calm and the clearest. One blocker: voices / mod float in a headless left column ≈ 20 mm below the oscillator row, while track sits under VCO 3. The same family is placed two ways.
  - **VCO 4 doesn't fit P5R** (32 mm short, systems).
- **P5O 8.** Strong symmetry (filter column | window | amp column) and the only layout with VCO 4 room. Blockers:
  - (a) headings are inconsistent: oscillators/filter/amp sit on top, while echo/reverb/out sit at their groups' right ends or between groups;
  - (b) the out group is cramped (heading squeezed between reverb decay and pan);
  - (c) drift is an odd 4th knob only in VCO 1's row;
  - (d) the VCO 4 cost (stick lowered to 9.0, or 58.8 closed) must be stated wherever VCO 4 is shown.
- **Spine:** the standing render reads as a soft book joint, as he wants. Accepted; his call.
- **Fixes:**
  - P5R: (1) all three oscillator switches on one line directly under the oscillator row (voices under VCO 1, mod under VCO 2, track under VCO 3); keys keep a side column; re-run the gap rule and redistribute the envelope groups / columns so no empty area exceeds a gutter; out stays at the end of row C.
  - P5O: (2) every heading top-left of its group (one rule panel-wide); (3) out gets a full slot (pan + link with the standard gutter); (4) drift and tune become a "tuning" pair with their own heading inside the oscillator block (or another regular placement); (5) a caption states the VCO 4 cost.
  - Both: checker at 0 incl. the gap rule; re-render the full tops only.


## Steer 5 scores (2026-11-13 ~21:10; bar 10): READ THIS FIRST
- **Judged:** P5R and P5O full tops (9.9 px/mm), closed spine render, §19.
- **The work really changed:** the rule, a two-row base, D 132, the 5 mm module, lines over dots.
- **Owner since:**
  - "Don't stop the other exploration tho I wanna see what they came up with too" (show both);
  - "I think we can bring the spine back if we can make it look good";
  - "I kinda want the corners to be softer and to be more architectural like how Apple does theirs".
- **Scores (first-time walk + proportion check):**
  - **P5R 8.** The lid reads in order: oscillators + tuning → envelopes (filter | window | amp) → echo → reverb, with keys and out as side columns. Labels are clean. Blockers:
    - the empty bottom-right corner of the lid;
    - the shared base's holes (below).
  - **P5O 6.** No single reading order: headings sit above some groups and at the feet of others (filter, keys, reverb, out); the right half scatters; amp sits above the filter.
  - **Shared base 7.** Two holes:
    - front row, between envelope and volume (≈ 50 mm);
    - rear row, between source and echo (≈ 50 mm).
    - Groups are packed left, not distributed. "release" sits alone at the rear left with no heading over it.
- **Fixes (relayed as briefs):**
  - base: groups spread so the gutters are equal across each row; the controllers heading spans both rows (release + bend as one column); rear row order mixer → effects, then the lights;
  - P5R: out moves to the end of the bottom row (echo → reverb → out, true to signal), so no corner is left empty; keys/tuning re-balanced so no empty area exceeds a group gutter;
  - P5O: re-cast as left-to-right columns (oscillators 3 rows | filter column | window | amp column mirroring filter | echo → reverb → out on the right), all headings on top, keys under the window or beside amp;
  - shared: pivots inboard of the superellipse corners; the spine kept and rendered closed, standing and flat (brass bands on the façade impost lines); lines grille accepted.
- **New test added:** row distribution. Groups fill a row margin to margin with equal gutters; an empty area larger than one group gutter is a fail.
- **CORRECTED (orchestrator):** a 4th ANALOG VCO with its own controls IS a live owner question. Verbatim 20:33: "See if we can fit a fourth oscillator", then "I still think the fourth voice would need octave and pitch controls right?" (after hearing the Matriarch has four analog VCOs). Adding it is his call. My earlier note dismissing it was wrong.
  - P5O must keep the space for VCO 4 (octave · pitch · wave + mixer 4 on the base) in its column re-cast.
  - Next score: say whether P5R can take VCO 4 after the redistribution, with numbers.


## CATHEDRAL steer 5: both halves (2026-11-13 ~20:45; bar 10): READ THIS FIRST
- **Owner (verbatim, owner.md bottom):** "I'm fine with another oscillator but we're getting really cramped in the top case. I also feel like master tuning controls should be closer to the oscillators and volume/mixer controls on the bottom case. I'm not sure how much physical space each pot actually needs but I think we should keep pushing the organizational logic in the cases. Also there needs to be a more harmonious / proportional approach to spacing from the knobs to the edge of the case inclusive of clear labeling. And I like the speaker grille but what's better lines or a cool grid of dots?"
- **Another oscillator = PARA+4's 4th voice** (a 5th DAC). No panel control.
- **Why he hasn't approved (calibration):**
  - he now judges the whole instrument's logic across halves;
  - "cramped" + proportion = he wants a visible spacing system, not minimum clearances.
  - My 10 was against the lid's labels; I didn't test proportion or cross-half logic.
  - **New test:** every distance comes from one stated module; margins to the case edge read as deliberate.
- **Director's organising rule (proposal, systems to test):**
  - **LID = what the sound is** (set and leave): oscillators + tuning (tune, drift beside them), envelopes, keys response, effect settings (types, time, repeats, decay, FREE/SYNC).
  - **BASE = how much you hear, as you play it, in signal order left → right:** controllers | mixer (1 2 3 extra, source) | filter (resonance, CUTOFF, envelope, track, mod) | effect amounts (echo mix, reverb mix, pans + link) | out (volume) | tap.
  - Every level/amount lives with the hands; every "what kind / how it moves" lives on the lid.
  - Base likely needs a second row (≈ 15 knobs + stick + TAP at ≥ 20 pitch ≈ 340 mm > ≈ 255 available). Systems tests a second low (R-LOW) row in the landing strip vs a deeper base (watch FOLD's coupled depth / gap rule), with numbers.
- **Spacing system:** one module from the real parts (knob Ø, pot body, label cap height, legend gap); pitch, gutters (= 1 module?), group gutters, edge margins ≥ group gutter, fixed label zones above/below; the same row pitch on both halves where possible.
- **Grille:** lines vs a dot grid, at equal plate (2.5, thinned locally) and equal web. Open area % of Sd, hole/slot size vs λ (≈ 34 mm at 10 kHz), duct length (depth/diameter), printability face-down, looks. Then a recommendation; visual shows both at 1:1 crop.
- **Keep:** signal order, one-word labels, throw-order switches, ≥ 2.0 closing clearance (R-LOW), Ø 46 window centred over CUTOFF, FREE/SYNC by TIME, link + pans, no dead band, nothing raised, no machining, checker 0.


## CATHEDRAL lid: 10 CONFIRMED (2026-11-13 ~20:30): READ THIS FIRST
- **Eye check, lid top:** VCO 3's "track" switch (x 121) sits directly under the VCO "3" numeral, the start of the VCO 3 group, so it reads as VCO 3's. Its legend on the left keeps it clear of "envelopes". The first-time walk passes every label and switch position. Systems' checker addition for the moved legend: pending (not re-run by me).
- **Lid → owner, on the site.**
- **Watch item:** the "track" legend extends left under wave 2. If the owner or the expert reads it as VCO 2's, a short engraved bracket from the "3" numeral is the fix.
- If he turns it down, record his reasons.


## Vocabulary round check (2026-11-13 ~20:20; bar 10): READ THIS FIRST
- **First-time walk on the re-rendered full top:** every label is one word and reads without the manual. Passes:
  - octave / wave / pitch with VCO numerals; voices 1 · 3 · 4; mixer 1 2 3 extra + source noise · input · loop;
  - envelopes with filter | amp, release centred; keys velocity / touch;
  - echo type / time / free · sync / repeats / mix / pan•; reverb type / decay / mix; out pan / link• / volume;
  - base controllers | filter (resonance, cutoff, envelope, track, mod) | tuning | tempo tap; midi / status lights.
- **Not 10 yet, one blocker:** VCO 3's "track" switch sits at x 163.5, beside the "envelopes" heading, outside the oscillator group. It reads as an envelope (or amp) switch, the misgrouping the expert flagged.
  - Fix: put it under VCO 3 (≈ x 104–124, the switch line under octave 3 / pitch 3), as voices/mod sit under VCO 1–2.
  - If the checker forbids that, systems says why and proposes the nearest spot inside the oscillator group.
  - Checker 0, re-render the lid top / full top / standing, then I check by eye → 10.


## Panel vocabulary, owner rule (2026-11-13 ~20:05): READ THIS FIRST
- **Owner, verbatim:** "Labels should only be one word and follow best practices with obvious tweaks for understanding if there's a better word than the jargon".
- **Rules I set:**
  - headings carry the context;
  - a word may repeat only under different headings (type, mix, pan, decay, track, mod);
  - plain over jargon only where the jargon is clearly worse (emphasis → resonance, range → octave, freq → pitch, para → voices, bbd → dark, kbd → track, osc 3 ctl → track, mod mix → blend, contour amt → envelope, contour → envelope);
  - keep the standard words that are already plain (cutoff, glide, repeats, decay, wave, attack, sustain, tap, drift, volume).
- **Exceptions, stated:** FREE/SYNC's ms/beat scales and the type fans keep their marks; "pingpong" is written as one word.
- **Full table:** in my reply to the orchestrator (relayed to systems for the checker and to visual for the render). It supersedes the small label fixes 3 and 4; fixes 1, 2 and 5 (FOLLOW on the column line, the lights labelled, touch clear of the fan) still stand.
- **Owner item it creates:** "voices 1 · 3 · 4" replaces mono/para/+4. Check he reads it as intended.


## CATHEDRAL lid, score after steer 4 fixes (2026-11-13 ~19:55; bar 10): READ THIS FIRST
- **First-time walk passes on:**
  - every toggle throwing left/right with positions in throw order;
  - "release · both contours · off · = decay";
  - FOLLOW as one label "echo pan · own · follows dry";
  - echo tap behind its own rule;
  - KBD per spec (full tracking via firmware = owner item).
- **The work really changed. Score 9/10.** What still needs the manual or looks off:
  1. FOLLOW sits off the out column's centre line (x 255), visibly left of dry pan / volume. Restore it on-line (systems checking).
  2. The two lights by CUTOFF (cream, green) are unlabelled. A first-timer can't tell status from "not in control". Label them (e.g. "status" · "midi").
  3. Base "amount" doesn't say of what (the filter contour is up on the lid). Make it "contour amt".
  4. SOURCE "fb" is cryptic. Use "fdbk" or "feedback" if it fits.
  5. The touch legend crowds echo TYPE's "tape / ping-pong" fan names, so they read as one cluster. Give ≥ 3 mm or move touch up.
- Then the checker at 0 with these words, re-render lid top / full top / standing → I check by eye → 10 → publish.


## CATHEDRAL lid, score after steer 4 (2026-11-13 ~19:40; bar 10): READ THIS FIRST
- **Judged:** lid top + full top (re-rendered); first-time player walk, every label and every switch.
- **The work really changed:** every review item is addressed (positions on all toggles, SOURCE under noise/ext, PARA + OSC MOD left, base controllers | filter | tune, KBD/FILT MOD beside CUTOFF, release, echo pan + "(off if follow)", keys, detune, reverb "tail").
- **Score: 8 / 10.** The first-time walk still fails at these points:
  1. **Which word is which lever position?** Positions are printed in one line beside a vertically throwing toggle. "mono · para · +4" left→right can't be mapped to lever down/mid/up without the manual. FREE/SYNC (above/below) and FOLLOW (left/right) use two other conventions, so there are three conventions on one panel.
  2. **The out column misreads.** FOLLOW's name "echo pan" sits directly above the VOLUME knob, so a first-timer reads VOLUME as "echo pan".
  3. **"release · off · on"** doesn't say which contours or what "on" does. The owner's item 6 asked for both.
  4. **"echo tap" sits under the "tune" heading.** A heading contradicting its control is the reviewer's own item-4 pattern.
  5. **KBD "off · 1/3 · 2/3":** the Model D reaches full tracking (1/3 + 2/3). Is full available here? If so, the legend lies by omission.
- **Fixes:**
  1. **Mount every toggle with a left/right throw** (same part, rotated 90°: $0, no clearance change, since height is the same) and print the positions in throw order on one line: left word · middle · right word. FREE/SYNC becomes "free · sync" beside it. One convention panel-wide. Systems re-checks label clearance.
  2. FOLLOW's legend as one unit beside the switch: "echo pan: own · follows dry". Nothing between the switch and VOLUME.
  3. Release: "release (both contours) · off · = decay", or "release: off · = decay" with "both" in the heading line between the contours.
  4. A break rule (or gap ≥ section break) between drift and echo tap, so echo tap stands alone at the end mirroring bend; or the heading becomes "tune · tempo".
  5. Systems confirms KBD's real positions (off / 1/3 / 2/3 / full?) and the legend matches the spec exactly.
  6. Checker covers all new words → 0; re-render the lid top, full top and standing only.
- **Visual's open point (one line under the name vs both ends):** accepted as one line, but only with fix 1 (the line order must match the throw).
- **Lesson:** a position legend is only readable if its spatial order matches the lever's motion. Check the mapping, not just the presence.


## CATHEDRAL lid, steer 4: BAR IS 10 (2026-11-13 ~19:15): READ THIS FIRST
- **Score reopened.** Synth expert: 7/10 for understanding (`design/reviews/2026-11-13-lid-layout-review.md`). Owner, verbatim: "Yes but make it a 10 not a 9".
- **My miss:** I checked grouping by headings and spacing, but never read a switch position the way a player must. Bare toggle words, SOURCE under the wrong knob, base headings contradicting their controls: all were visible in images I passed.
- **New test (mandatory before any score):** a first-time player walk. For every control:
  - what does it do?
  - which group does it belong to?
  - for every switch, what does each position do, read from the panel alone?
  - Any "I'd need the manual" = not a 10.
- **Round fixes all 7 items + both nice-to-haves:**
  1. position legends on every toggle;
  2. SOURCE under NOISE/EXT;
  3. PARA + OSC MOD grouped at the left, OSC 3 CTL under VCO 3;
  4. base regrouped as controllers | filter | tune, with "echo tap";
  5. KBD / FILT MOD beside CUTOFF on the base if closing allows, else under the filter contour; no lone heading;
  6. DECAY switch → "release", saying which contours;
  7. "echo pan" + FOLLOW "own · follows dry" + a cue at the knob;
  - nice-to-haves: a "keys" label over VELOCITY/TOUCH; "detune" on FREQ 2/3.
- **Director rulings for the round:**
  - every legend matches the spec's real positions (systems confirms from how-it-works; no invented positions);
  - one word per concept panel-wide (echo, never delay);
  - no duplicate words for different things (decay knob vs release switch; osc 3 level vs osc 3 ctl);
  - headings name what's under them.
- **10 also needs:** 0 checker violations incl. the new legends; the R-LOW closing clearance re-checked for any toggle moved to the base; the stale views re-rendered.
- **Out column starting beside the contours:** left as is (reviewer: "fine as is").


## CATHEDRAL lid: 9 CONFIRMED (2026-11-13 ~19:00): READ THIS FIRST
- Checked by eye, `cathedral-lid-signal-order-8.7px-per-mm.png`:
  - the "filter" heading and rule mirror "out", so KBD / FILT MOD read as a group;
  - "filt mod" sits ≈ 4.5 mm clear of echo TYPE's fan names;
  - systems' checker is at 0 with all tweaks (2f99f96, not re-run by me).
- **Lid → owner, on the site.**
- An independent synth expert review of the lid is running (owner's request). If it finds real comprehension problems, treat its findings as owner-level objections and re-open the score rather than defending it.


## CATHEDRAL lid fix check (2026-11-13 ~18:50): READ THIS FIRST
- **Checked by eye:** lid top (P) and standing 3/4 (re-rendered; consistent with the lid).
  - VCO 1 / 2 / 3 spacing groups read ✓;
  - headings at 3.0 over 2.35 legends ✓;
  - the middle row mirrored about the window ✓;
  - the signal still traces osc → mixer → filter contour → loudness → echo → reverb → out ✓;
  - the name "big energy" is approved (owner 17:37) ✓.
- **9, CONDITIONAL on two items (I check by eye, no re-score; then publish):**
  1. The left-edge KBD / FILT MOD column reads orphaned, as visual flagged, and "filt mod" crowds echo TYPE's "tape / ping-pong" fan names.
     - Fix: make it a named group that mirrors the out column: a "filter" heading at the "out" heading's height, plus a vertical rule like the out column's (both switches are filter settings; the filter itself is on the base).
     - Move "filt mod" up so it reads clearly apart from the echo fan names.
  2. Systems adds visual's font-fit tweaks to `layout_check.py`: contour headings, the osc/mixer break, "reverb" +2 mm, FOLLOW's words, and the new filter heading → 0.
- If the owner turns it down, record why.


## CATHEDRAL lid, score after steer 3 (2026-11-13 ~18:30): READ THIS FIRST
- **Judged:** `img/cathedral-lid-signal-order-8.7px-per-mm.png` (P) and §17 (concept table, 9 cited references, P vs S).
- **The work really changed:** a new arrangement, not a restyle.
- **Signal traced on the image:**
  - top band: oscillators → mixer (osc 1, 2, 3, noise in order, source under it) ✓;
  - middle band: filter contour → [window] → loudness contour (velocity, touch, decay under it) ✓;
  - bottom band: echo (type, time, FREE/SYNC, repeats, mix, delay pan) → [window] → reverb ✓;
  - out column at the right edge: dry pan / FOLLOW / volume ✓;
  - effects off the top ✓;
  - every switch under its own group ✓;
  - S rightly rejected (echo stays at the top, needs the window off-axis).
- **Score: 8.** Likely owner objections:
  - (a) a blank patch in the middle band between the filter contour (hugging the left edge) and the window, while the loudness contour hugs the window on the right. That's a gap and an imbalance again, his two triggers;
  - (b) group headings are smaller than the knob legends, so the hierarchy is inverted and the grouping he asked for doesn't read first;
  - (c) the 8 oscillator knobs run as one even row (range 1 wave 1 range 2 freq 2 wave 2 …), so VCO 1 / 2 / 3 aren't visible as groups;
  - (d) ~~name plate~~: not an objection. He named it "big energy" at 17:37; my notes had missed that entry.
- **Fixes (I check by eye):**
  1. Band B symmetric about the window, no blank patch. E.g. the filter contour mirrors the loudness contour about x 143, with the filter's two switches (kbd, filt mod) as a left-edge column mirroring the out column. Systems checks it.
  2. Headings clearly above the legends (larger/bolder in Kalam), one per group, placed at the group's start or centre consistently.
  3. VCO 1 / 2 / 3 read as three groups: extra spacing between them if the checker allows it, or else short engraved underlines per VCO.
  4. ~~Name plate blank~~ WITHDRAWN: the owner named it at 17:37 ("name to come -- we're calling it big energy"; owner.md, naming.md). "big energy" on the plate stays.
  5. Add visual's new legends (numbered range/wave, the contour headings, "osc 3 ctl") to `layout_check.py` → 0.
- **Before he sees it:** re-render (not remove) the full top view (lid + base) and the standing 3/4 in P, so nothing on the site contradicts the new lid. The closed side, speaker drawing and keys images stay as they are.


## CATHEDRAL top panel, steer 3 (2026-11-13 ~18:05): READ THIS FIRST
- **Owner did NOT approve the 9.** Verbatim (screenshot design/owner-refs/2026-11-13-1800-top-panel.png): "lets focus on top panel first -- the items do not appear to be grouped or ordered in a way that makes logical sense. have the team break down which concepts belong together, and reorient accordingly.  there are tons of examples on the internet of good organization beyond the model d itself for the add'l functionality. also i dont like the effects controls at the top ... when i think of signal order it's synth stuff -> fx stuff -> output stuff like volume. so it at the top of the layout is confusing"
- **His reasons (what a 9 means to him):** panel logic = signal order and whole groups, not just symmetry and geometry. I scored balance, the band and acoustics; I didn't test "can he read the signal path at a glance". **New test for every layout from now on:** trace the signal on the image; every group must be contiguous and in signal order.
- **My diagnosis of the screenshot:**
  1. FX at the top: standing or flat, the lid reads top → bottom, so FX reads first.
  2. The mixer is split round the window and out of order (osc 2 top-left, osc 1 bottom-left, noise top-right, osc 3 bottom-right).
  3. The switch line mixes four groups (source = mixer, filt mod = filter, velocity, touch = aftertouch).
  4. The two contours are unlabelled as filter vs loudness, and sit far from the filter (base).
  5. The "osc 3" toggle vs the "osc 3" level: same words for different things.
  6. The decay/kbd toggles are isolated at the far right.
- **Fixed constraint I found:** the window must stay at CUTOFF's closed landing (143, d ≈ 32–40), because CUTOFF is the base's one tall knob (R-LOW). So any arrangement flows around a fixed centre window, unless CUTOFF gets a low hero (none bought exists).
- **Director's lead proposal ("page order") for systems to test against 1–2 alternatives:**
  - upper two rows = synth, left → right: OSCILLATORS (block) → MIXER (osc 1, osc 2, osc 3, noise/ext in order, top row centre, over the window) → CONTOURS (filter then loudness, labelled), with each group's switches inside it;
  - bottom row (nearest the hinge) = ECHO (left of the window, FREE/SYNC by TIME) → REVERB → OUT (pans, FOLLOW, volume) right of the window;
  - reads top-left → bottom-right like a page; FX next to the hands; output ends at the corner beside TAP.
- **Briefs sent via the orchestrator** (systems: concept breakdown + references + 2–3 arrangements with checks; visual: lid top view of the chosen one only). Then I score.


## CATHEDRAL fix check (2026-11-13 ~17:40): READ THIS FIRST
- **CATHEDRAL 9 CONFIRMED → publish and show the owner.** Checked by eye on the re-rendered nave-top, nave-standing and nave-closed-side.
  - Fix 1: FX row centred on the axis. ✓
  - Fix 2: section names back, name plate under the window. ✓
  - Fix 3: R3 gone; base right reads MOD MIX, DRIFT, TAP, balanced against the left. ✓
  - Fix 5: 0 label collisions on the real model (systems). ✓
  - Fix 6: conditions stated in §16 (systems; not re-read by me).
- **Fix 4, hinge ear: accepted as is, not a blocker.**
  - With the lid flat and the seam closed, the axis sits at or behind the back face, so a ≈ 4 mm round ear remains at each rear corner (down from 6). It's only visible from the side/back.
  - He said "if not these are fine" about knuckles, and this is quieter than knuckles.
  - **Tell him plainly on the site:** the pins are hidden; a 4 mm ear remains; the alternative is knuckles or a pivot redesign (his call if he minds it). A form change goes to him only if he asks.
- **Carry to the owner with the 9:**
  - closed ≈ 55.2 depends on snap-in pots/counterbore + the lowered stick (else 56.7–58.8; R-TALL 59.7 keeps the big knobs);
  - played-row knobs Ø 10 gold;
  - moved controls (mixer around the window, CUTOFF on the axis, MOD MIX and DRIFT to the base);
  - the 4 mm hinge ear;
  - buy-and-test T1/T2.
- **If he turns it down, record his reasons here.**


## CATHEDRAL, score after steer 2 (2026-11-13 ~17:20): READ THIS FIRST
- **Judged:** how-it-works §16 and look rev 4 images (nave-standing, nave-top, nave-closed-side, speaker window + section, keys A/C).
- **The work really changed.** It's a re-architecture, not restyling:
  - the band is gone: three lid rows at an even 35.05 pitch, one switch line, the only knob-free area is the window;
  - root cause stated;
  - R-LOW: low Tayda gold Ø 10 × 8 knobs on the played row, stick lowered, closed ≈ 55.2 (R-TALL 59.7 as the fallback);
  - Ø 46 window, vertical slots, ≈ 73–83 % of Sd open, gasket, sealed stuffed 20–25 cc back box, honest +3–6 dB at 1–5 kHz;
  - centred on x 143 over CUTOFF (CUTOFF ↔ EMPHASIS swapped), mixer symmetric ± 39.5;
  - battery to the base rear strip (tip threshold up to 8.4 N);
  - keys A (brass naturals, black-plated brass sharps, one velocity calibration);
  - base row mirrored, stick ↔ TAP.
- **Score: CATHEDRAL 8.** Not a 9, because of these likely owner objections, all visible in the images:
  - (a) the FX row runs x 62.5–260.5, so the lid's top-left corner is empty (DRIFT left). That's an off-centre gap of exactly the kind he just objected to;
  - (b) R3 is a knob with no function or legend;
  - (c) the lid lost its section names (oscillators / mixer / contours);
  - (d) closed side view: the side-pivot ear projects as a lobe past the back outline. "Hidden" hinges shouldn't add a bump.
- **Fixes (I check by eye, no re-score; then publish):**
  1. Re-centre the FX row about x 143 (groups and breaks kept; FREE/SYNC and FOLLOW move with it).
  2. Restore the lid section names in the hand.
  3. Remove R3. Re-space the base right section (MOD MIX, DRIFT, TAP) so stick ↔ TAP still mirrors and nothing reads as a missing knob.
  4. Keep the pivot ear inside the block outline (axis or ear within the rear radius, or the rear radius enclosing it). Re-render the closed side.
  5. Re-run the label check on the visual model (systems' 0 used estimated label sizes) → 0.
  6. Doc honesty:
     - 55.2 depends on snap-in pots or a counterbore plus the lowered stick (else 56.7–58.8);
     - the played row's knobs are now Ø 10 (from 14.9): say so, offer R-TALL as his alternative.
- **Watch items (not blockers):** small Ø 10 knobs on the played row (feel); loudness from a 50 mm driver is still modest; mixer, switches, CUTOFF/EMPHASIS, MOD MIX and DRIFT all moved (he allowed moving components).
- **Lesson:** a re-flow that removes a control from a row leaves a hole at the row's end. Check every row's extent against the axis after moves.


## CATHEDRAL, steer 2 (2026-11-13 ~16:55): READ THIS FIRST
- **Owner, verbatim (16:52):** "ok i dont think you're really thinking here — off center in that middle section is bad looking. aso consider the sound of the speaker and the shape... which will work best and give me the best sound out of the chosen speaker. in fact none of my feedback on why it's a problem have been addressed. there's a massive horizontal gap -- the speaker doesnt feel resolved. this may mean moving components. i'd rather have more brass than black re: keys too."
- **What went wrong (mine as much as the team's):** since 14:18 we offered grille shapes that fit leftover band space. My steer 1 even ruled on grille shapes instead of the band. **Lesson:** when the owner names a gap, find what forces the gap before styling what fills it.
- **Root cause:**
  - closed, base y lands on lid d = 108 − y;
  - the PLAY row (y 68; knob tops z 29.1, CUTOFF 27.75) lands at lid d ≈ 40, where lid knobs reach down to z ≈ 24;
  - overlap ≈ 5.1 + 2.0 clearance, so nothing tall can live there, which makes the band 37.55 clear vs ≈ 8.5 between other rows;
  - the base landing strip is the mirror case for V1.
- **Direction ("nave and rose"):**
  1. **R-LOW (primary):** bought low-profile knobs on the base PLAY row (≤ ~9 mm above the plate; CUTOFF a wide, low hero dial). Lid knobs can then land over them with ≥ 2.0 clearance, closed ≤ ~56. Lid rows re-spaced evenly, so there's no knob-free strip wider than a row gap except the speaker window. Shrink the landing strip / halves if possible.
     - **R-TALL (fallback):** today's knobs plus ≈ +7 closed (≈ 60). Systems gives the numbers for both; I choose.
  2. **Speaker from acoustics:**
     - one round opening concentric with the 50 mm CDS-5076-1SP, Ø ≈ cone + surround (≈ 42–46);
     - open area ≥ 50 % of Sd, target ~60 % (today 265–440 mm² ≈ 20–35 %: choked);
     - vertical slots (his preference) ≥ 1.5 wide, or holes; web thinned to ≤ 1.2;
     - front gasket; sealed, stuffed printed back box; magnet distances kept.
  3. **Placement:** centred on the axis x 143 in the lid. The mixer column widens symmetrically around it (pairs flanking; switches re-flowed). The window sits directly above CUTOFF/EMPHASIS, giving one vertical axis.
  4. **Base PLAY row symmetric:** stick at the left end ↔ TAP at the right end, hero on the axis, no empty right end.
  5. **Keys:** A (brass naturals, black sharps; normal reading, more brass) as the lead; C (all brass) as the alternate; metal shader. Systems picks the sharps' material (black-plated brass vs printed black + per-group velocity curve).
  6. **Keep:** the effects row on the lid back with the pans/FOLLOW/VOLUME, FREE/SYNC, stereo out, nothing raised among the knobs, no screens, closing ≥ 2.0, no machining, side pivots, no spine, R 7.7, screw-feet, woody relief, the palette.
- **Deliverables asked:**
  - systems: how-it-works §16 (root cause, route numbers, clearance table, new x/d table, acoustics) and checker 0 incl. labels;
  - visual: rev 3 with open 3/4, standing 3/4, exact top, exact closed side elevation, speaker top + section, keys A/C; an opening paragraph answering his three complaints; HTML captions.
  - Publish (site/publish.sh) only after a 9. Commit specific files only, as Adam Trabold, no Claude credit (HANDOFF).
- **Status:** I could NOT deliver these briefs. SendMessage to ac0e7aeee47bf1a1b (systems) and a26f3d36a52e6b5d4 (visual) failed: "only the main conversation can resume" them. The orchestrator must relay this section to both (it's written to be sent as is).
- **Not scored:** no new work exists yet.
- **Likely objections when scored:**
  - low PLAY knobs change the played row's feel (R-LOW) / thicker body (R-TALL);
  - re-flowing the mixer moves controls he has learned;
  - brass mass and velocity;
  - loudness still modest from a 50 mm driver (honest numbers needed).


## CATHEDRAL, steer 1 (2026-11-13; round counts reset): READ THIS FIRST
- **Owner (owner.md 14:12–14:41):**
  - lock in on CATHEDRAL (= CHAMBER, renamed as the point of view) with FOLD v1.1 as the middle ground;
  - no spine; hidden hinges if possible; the speaker gap; FX together with echo/reverb; feet = screws; woodier fine line texture (he designs the pipe lines himself);
  - consistent plate rounding; fewer colours (the brown pegs out of place); a rounded grille;
  - no machining (keys printed or bought; external and metal printing OK); brass + black or all-brass keys; bought wood caps on a shaft also OK.
  - RAIN parked.
- **Judged:** how-it-works (§0–13) and how-it-looks-and-feels rev 2, plus images (6 key colours, A/B standing, grille options).
- **Not scored.** Two reasons:
  1. the standing and closed renders still show the retired spine and rev 1 keys;
  2. four owner decisions change the form (layout, hinge, back slot, keys).
  - I score after his answers and one re-render pass. Nothing to him at a score yet; the decisions go now.
- **Team rulings (no owner needed):**
  1. All 8 plate corners R 7.7: yes.
  2. Screw-through rubber feet at the 4 corner screws; the axis screws stay flush brass (no impost clash): yes.
  3. Grille: tapered horizontal slots (his first option). Vesica 66 × 16 in A (the Ø 34 circle hits labels); Ø 27 circle in B. Concentric arcs dropped.
  4. **Fine-line woody texture is built, not deferred.** Visual's "leave the print plain" doesn't deliver his ask on the only build he'll make (real walnut = machining, now out).
     - Model sparse cathedral-grain arches as shallow relief/grooves on the printed walnut-tone body (sides, base underside, lid-back field), at about the old line count.
     - The lid back's figure waits for his façade, so leave the field ready.
  5. One visible metal: brass. Stays cast brass from the keys' service (fallback: matte-black PETG 5 × 8, never grey 316L in view). Hidden hinge leaves 316L. Axis screws brass. Feet black.
  6. Palette: walnut, cream, black, red CUTOFF, brass. No other colour; TAP is made of the key material.
  7. Option A heading → "effects".
  8. Keys use one carrier interface (Ø 9.6 cup / 9.53 × 3.2 tenon) so the head choice stays swappable after the build.
     - Buy one Cherry Tree Toys pack and measure head height H before fixing the lid height.
     - Test one hollow cast-brass head (2.5–3 g) on one Choc V2 before ordering.
  9. **Brass can't be judged from a flat-yellow render** (it reads as mustard plastic). Before he chooses keys, show brass with a metal shader/specular, or a real photo of polished brass domes as reference.
- **Owner decisions (worded in my reply):**
  - Q1 layout A vs B (moves controls; the gap itself can't go because it's where the base knobs sleep closed; B leaves the band plain; B costs reach for the FX amounts and TAP);
  - Q2 hidden pins vs cables-through-hinge (mutually exclusive);
  - Q3 the back slot with no spine;
  - Q4 keys (B reversed: black naturals + brass sharps, rec; A normal-reading: brass naturals + black sharps; C all brass).
  - **Recommendations:** B layout, hidden pins, slot left open but finished dark inside (S1), keys B.
- **Likely objections when scored:**
  - B: the FX amounts and TAP are far from the hands while playing; the band stays blank.
  - A: the split remains.
  - Brass looking toy-like in renders.
  - +2.6–4 mm closed with pegs, depending on H.
  - The open back slot.
- **Next:**
  - Designers, in parallel with the owner's answers: radii, feet, grille, woody relief, the brass material look, measure H, one brass head test.
  - After his answers: re-render closed, standing (chosen layout) and keys, with no spine; then I score.


## BRANCHES, R1' check (2026-11-13): READ THIS FIRST
- **RAIN 9 CONFIRMED.** Checked by eye on the re-rendered `rain/img/rain-arms-length.jpg` (look doc rev 2.2).
  - Rings stop ≈ 7 mm out (deep to 3.5, shallow to 7), and the far-field hatching is gone.
  - Big rear and corner cells are now still pools. It reads as drops on still water: the calmest, truest version.
- **Watch item for the owner's reaction, not a blocker:** at arm's length RAIN now sits closer to v1.1 ONE SHEET.
  - The section map comes from still lanes and clustering, not seams.
  - What differs is the whole point of view: every element ripples (keys as stones, toggles, stick, TAP), no grooves or headings, the warm stone, and the one mustard leaf.
  - If he says "this is just ONE SHEET", that's the reason.
- **Both concepts go to the owner: CHAMBER 9 (FOLD) and RAIN 9 (ONE SHEET),** with the 7 questions in the round-2 section below.


## BRANCHES, R1 check (2026-11-13): READ THIS FIRST
- **RAIN's 9 is WITHHELD.** R1 was checked by eye on the re-rendered `rain/img/rain-arms-length.jpg` (look doc rev 2.1).
- **What changed:** only a 1.5 mm still margin at the outline.
- **What didn't change:** the rear corners and the band behind the back row still show the same straight far-field hatching, the thing R1 was for. My R1 wording ("the decay finishes everywhere") was read as "the edge too". The real problem is that the far-field rings never finish.
- **Re-issued fix (R1'):**
  - cap each element's ring field at a fixed reach beyond its ring start: ≈ 6–8 mm (≈ 3 deep + 2–3 shallow rings);
  - still water beyond, whatever the cell size, so big rear and corner cells become still pools instead of hatching;
  - re-render arm's length only;
  - I check by eye. If the hatching is gone, the 9 stands with no re-score.
- **CHAMBER 9 stands.** It can go to the owner now, or wait to travel with RAIN. Systems' coverage says both pass every job (coverage.md); I didn't audit it.
- Questions to carry: unchanged (round-2 section below).


## BRANCHES, round 2 scores (2026-11-13): READ THIS FIRST
- **Judged:** CHAMBER and RAIN looks docs rev 2 and how-it-works rev 2, plus the re-rendered images.
  - CHAMBER: standing, closed-with-book, fallback pegs.
  - RAIN: arm's length, close, 3-way pitch compare.
  - `branch_check.py` §7/§8 reports 0 legend/tick collisions and 0 fails (systems; I didn't re-run it).
- **The work really changed in both.** Each fix shows in the images, not only in the text, so the higher scores are earned.
- **CHAMBER 9 → to the owner.**
  - **Standing lid now reads cream.** A render correction, disclosed; the real plate is cream.
  - **Hinge slot closed by a flexible oxblood bookcloth spine.**
    - Taut closed, it's the case's back panel. Open, it folds into the seam gap, so R4 holds. Standing, it shows as a soft drape.
    - It reads as a book joint, and it gives the case its one warm cloth note.
  - **Fallback peg colours are drawn**, so his answer on reversed keys can't sink it.
  - **The push-outs became two real pipe mouths** (pitch 8.75), so the decoration now does a job.
  - Kalam throughout; both artefacts gone; walnut plugs sourced (~$0.32 each, shank fit UNVERIFIED).
  - **Remaining owner objections (not likely enough to hold it):**
    - 52.7 closed (+2.6 over v1.1);
    - reversed keys (fallback ready);
    - spine wear.
  - **Pre-build checks, not score blockers:** plug shank fit (one sample), spine flex life, the ribbon loop sharing the seam gap, engraved/relief fill on wood-fill PETG.
- **RAIN 9, conditional on one fix I check by eye (no re-score) → then to the owner.**
  - **Decay works:** deep 0.4 rings hug each control, then shallow 1.8-pitch rings, then still water. Close up it reads as ripples dying out.
  - **Section lanes** (3.0 between sections vs 1.0 inside) now draw the map at arm's length.
  - **Palette** is warm stone with one mustard leaf; no longer concrete.
  - **0 legend collisions.** The 3-way pitch compare is honest about 0.9 vs the loved 0.45.
  - **Condition R1:** remove the "rings continue to the panel edge" exception. Let the decay finish everywhere, so the edge is still water like every seam.
    - At arm's length the far-field rings at the rear corners and the rear band read as straight hatching, the busiest part of the face.
    - This came from my round-1 "run to every edge" note, which conflicts with my own decay fix. The decay rule wins: one rule, no exceptions.
    - Re-render arm's length only.
  - **Pre-build checks:** the ring coupon (0.4/0.2 depths, seams, lily pads, under a tree), a one-piece print on a 350 bed, peg survival in a bag (case work is still his deferred topic), sun legibility.
- **What kept blocking a 9 across rounds (branches):**
  1. renders contradicting the concept (grey lids, an un-mirrored edge, snag cords);
  2. legend collisions;
  3. ideas living in a small part of the object (BUTTERFLY, DIPTYCH; both cut).
  - Now: (1) is fixed by checking each view type; (2) is fixed by the checker counting legends; (3) is fixed by cutting.
  - **New lesson:** my own round notes can conflict (edge vs decay), and the designers follow both literally. When I add a fix, re-read my earlier instructions for clashes.
- **Questions to carry to the owner with the two concepts:**
  1. Reversed keys or the fallback (CHAMBER, both drawn)?
  2. Pegs worth +2.6 mm closed on FOLD (zero width cost on ONE SHEET)?
  3. How long is a park session (battery)?
  4. Send the tapped tempo out as MIDI clock?
  5. The furniture book's title and author?
  6. TIME has a dead 15° at each end to keep its scale honest: OK?
  7. (RAIN) Does Vector Space have a 0.25–0.3 mm nozzle? It allows 0.6 mm rings, nearer the 0.45 he loved; otherwise 0.9.
- **Next:** check RAIN R1 by eye → both go to the owner (CHAMBER for FOLD, RAIN for ONE SHEET). If he turns down either, record his reasons here: they are the best signal of what a 9 means to him.


## BRANCHES, steer 1 + first concept scores (2026-11-13): READ THIS FIRST
- **Owner since my jam turn (format):** no A3, nothing printed; images made to look great on the site, viewed responsively (not phone-first); **images only for what must be visual, all text in HTML.** So concepts are now markdown + separate images; sheets are retired for new work.
  - My ruling: labels that point at geometry (dimensions, scale bars) may stay inside a drawing. Captions, principles, notes and comparisons ("v1.1 · 0.45 mm") go in the HTML.
  - True-scale "px per mm" files are fine as references, but never claim "real size" on a screen.
- **What I judged:** each branch's how-it-works + how-it-looks-and-feels and its images (looked at the 3/4s, states, close-ups, 1:1 crops, the DIPTYCH side elevation). Not the designers' notes.
- **Kill: DIPTYCH (my own; the d20 had said 15, judgement overrides).**
  - Its spine failed physically: cords alone tip at 0.8 N, while a knob turn pushes 1–3 N.
  - The fix (fold-out brass feet + 4 eyes + a feet-before-cords order, which tips if done wrong) is worse than v1.1's two stays that do both jobs. That's a regression on cost, simplicity and his "blend into the case" stand.
  - Without the cords, at arm's length it's v1.1 FOLD with serif type and red hairlines: a graphics variant, not a point of view.
  - The 3/4 also drew the cords at the snag geometry (to the base front corner), contradicting the s 60 elevation, and the standing lid rendered grey.
  - **Donor:** the red/black TIME dial with written divisions (1/16, 1/8, 1/4, 1/2) is the best TIME dial in the set. Any branch may adopt it.
  - Its open points (cords vs stays, 38.4° vs 37.4°) are moot.
- **READY: CHAMBER, RAIN, BUTTERFLY. Scores (concept phase, judged on the idea):**
  - **CHAMBER 8.**
    - The idea holds. The façade from the keyboard's numbers reads as pipes in plain line work, not costume. The three states work. The reverse pegs make the standing view read as a chamber organ, the best picture in the set.
    - Below 9 because of likely owner objections:
      - (a) the standing lid face renders grey, the exact thing he asked about (FOLD's face should catch light);
      - (b) closed, the hinge-side slot shows the knobs and keys, so the "case" doesn't read as closed;
      - (c) reversed colours: an owner question that could sink the concept on one answer;
      - (d) +2.6 mm closed (52.7): minor.
  - **RAIN 7.**
    - Close up it's beautiful (raked garden, rings, lily pads). At arm's length it reads as crazed or cracked grey stone, not still water.
    - Grey shell, grey stones, grey walls, grey bats: calm becomes drab.
    - Every knob is its own cell, so a seam inside a section looks the same as one between sections. The seams don't yet draw the *map*.
    - Legends collide (REVERB TYPE/VELOCITY, ECHO TYPE/OSC 3 CTL): the set lesson again.
    - The 0.9 grooves are coarser than the 0.45 he loved.
  - **BUTTERFLY 6: replace (retire), not fix.**
    - The point of view governs a 15 mm, 6 mm-thick strip. The rest is v1.1 ONE SHEET in bone, so the owner's line will be "ONE SHEET with a plank".
    - The branch rule (the board is constant, legends reach y 165) caps it: there's no honest way for "tool to tree" to reach the face.
    - The 3/4 and from-behind renders also show an un-mirrored edge, contradicting the end-match.
    - **Donors:** the tabletop-over-apron rear (jacks sheltered under an overhang), and the wall elevation's live edge reading as a horizon.
    - I'm not replacing it: CHAMBER (FOLD) + RAIN (ONE SHEET) cover both of his leans.
- **Rulings on open points:**
  - FREE/SYNC left/right throw (systems' fix; "the lever points at the word") accepted over my fore-aft.
  - ±135° printed sweep + firmware clamp accepted (dead 15° at each end; tell him).
  - Set-wide: drop the top ticks of OSC 2 / NOISE-EXT under "free"/"sync"; the checker counts tick rings and legend-vs-legend.
  - CHAMBER: "mono / para / +4" accepted; push-out holes to d 90 accepted if clear of the d 96 screws (systems); a spine wall or lid lip closes the hinge slot (systems to say whether the slot is real).
  - RAIN: power-on drop sound optional (power-off is impossible on the hard switch).
- **Fixes for round 2:**
  - **CHAMBER:**
    1. re-light the standing renders so the lid face reads cream (check like v1.1 E);
    2. close the hinge-side slot (spine wall / lip) and re-render closed;
    3. one image of the fallback peg colouring (maple naturals, walnut sharps), so his answer on reversed keys can't sink the concept;
    4. push-outs to d 90, PARA legend, Kalam (not the stand-in) before he sees it;
    5. fix the white streak artefact on the walnut pegs and the pale band on the base front face in the close render;
    6. the walnut button-plug source (or maple stained dark as the fallback, priced).
  - **RAIN:**
    1. **the ripples decay**: groove depth/width taper to nothing toward each seam (real ripples lose amplitude with distance; still two finishes), so seams are still-water bands, not drawn lines;
    2. **sections are wider still bands**: weight the power diagram so a seam between sections is ≈ 3× a seam inside one, which makes the map;
    3. warm the palette off concrete (pale wet stone with warmth; the walls carry the field over the chamfer; keep two stone greys and the one mustard leaf);
    4. fix every legend collision, with the checker counting legend-vs-legend;
    5. a 3-way pitch compare (0.45 / 0.6 / 0.9) in HTML, with only the drawing as the image;
    6. re-render at arm's length and close.
- **What keeps blocking a 9 (carried from v1 rounds and now in the branches):**
  - (1) an idea that lives in a small part of the object (ONE SHEET r1–4, BUTTERFLY now; DIPTYCH's faces);
  - (2) renders inheriting old geometry or lighting that contradicts the concept (the joystick slot in v1.1; now the un-mirrored edge, the snag cords, the grey lids);
  - (3) legend collisions whenever text changes.
  - Why it keeps happening: the render pipeline is shared and models are reused across branches, so each view type needs its own check against the concept's words.
- **Owner questions (from the jam, still open):** reversed keys; pegs worth +2.6 mm closed on FOLD (width on ONE SHEET is now 0 with the 14 mm washer); park session length; tap tempo as MIDI clock out; the book's title. **Plus new:** TIME has a dead 15° at each end (to keep its scale honest): OK?
- **Next:** CHAMBER and RAIN round 2 on the fixes above, then I re-score both. Nothing goes to the owner below 9.


## BRANCHES, jam turn 3 (2026-11-13, new director taking over): READ THIS FIRST
- **Task:** the owner's branched creative rounds (owner.md 11:47). He wants more personality and a holistic point of view; sources: furniture principles, instruments, tools, art, emotion, "take this to the park". He loves the pegs; "organ like" on FOLD is an example only. **Echo sync DECIDED: B, a FREE / SYNC toggle near TIME** (11:58). The v1.1 locks are never edited.
- **My turn:** the bottom of `design/branches/jam.md`. Draws: `design/branches/draw-director.py` (fresh decks; used Oblique cards removed). Results:
  - director: "Be extravagant", sundial / gnomon, wonder, a bandstand;
  - per branch: BUTTERFLY "lighter than it looks" / "From nothing to more than nothing"; CHAMBER "a place for your own mark" / "Look at the order in which you do things"; GROUND "tell it from 30 m" / "Lost in useless territory"; RAIN "makes a sound when you close it" / "Courage!";
  - d20 kill test: BUTTERFLY 9, CHAMBER 11, GROUND 2, RAIN 7, DIPTYCH 15;
  - unused: coffee grinder.
- **Kills:**
  - **PIERCED, upheld:** +55 mm for one gesture, against cost and portability.
  - **GROUND, killed by me:**
    - a posture is a stand, not a point of view;
    - +25–37 mm at the back against the ≈ 36 body;
    - the horn is unverified;
    - FOLD's lid already tilts.
  - GROUND's donors: the status-light hood (now set-wide), high-contrast sun type, the felt finger pocket, and "the bottom is as designed as the top".
- **Going to concepts (4), each with a "must prove" list in the jam §3:**
  - **CHAMBER (FOLD):** the strongest branch, so held hardest.
    - The order of use is the concept: closed façade → flat console → standing façade to the listener.
    - Flush nameboard cartouche on the axis for his maker's mark.
    - **Costume watch:** line work only, serif only on the RANGE feet and the nameboard.
    - The sketch's "little d" must go (the owner hates the name).
    - Must prove: the closed bar reads as an organ case, the closed height with pegs, reversed pegs at 1:1, engraved fill vs printed relief, a standing view from behind.
  - **RAIN (ONE SHEET):** the most generative.
    - "Courage!": drop the section grooves and let the Voronoi seams be the only section marks; the field runs to every edge.
    - Optional: a power-off "drop" sound ($0, firmware).
    - Must prove: calm at arm's length and alive up close, legends on the lily pads, 0.9-pitch rings that still feel like v1.1's, peg width (+8 mm), one mustard accent only.
  - **BUTTERFLY (ONE SHEET):**
    - The butterfly must do a job, so the rail is **two bookmatched live-edge offcuts joined by the butterfly on the axis**. That makes the joint honest, uses cheaper short pieces, and mirrors the wild edge, which gives it balance.
    - Rail ≈ 20 mm of wood, "lighter than it looks".
    - The set's flat-key branch.
    - Must prove: printed cream beside real walnut reads as intended, not a kit (biggest risk; try a matte bone/stone filament); joint depth; slotted screws and the drilling jig; the cleat hanging.
  - **DIPTYCH (FOLD), my own:** a Nuremberg diptych sundial.
    - Cords at the end faces are the stay. They replace the brass stays and remove v1.1's stay-groove/jack clash.
    - The cords are set at Lynchburg's latitude, 37.4° [CALC rough: anchor ≈ 68 mm forward of the hinge, cord ≈ 154 mm, at the approved 120°].
    - TIME's two scales are its "two hour systems" (the FREE/SYNC feature becomes the hero).
    - Red and black engraved graduations on the white leaves; the walnut stays.
    - **I'm hard on it:** if it can't separate from CHAMBER at concept stage, cut DIPTYCH, not CHAMBER. Cord snag risk near the stick and TAP.
- **Set-wide rulings:**
  - FREE/SYNC placement accepted: in front of TIME, in the dead zone, fore-aft throw (toward TIME = sync), two scales, no mirror partner. Pending systems' label check.
  - **H7 stands** (no lit TAP); a hooded or light-piped status light in every branch.
  - No name on any branch.
  - The board is the constant; no branch moves a control.
- **Calibration carried from my predecessor:** a 9 = every visible choice traces to one idea, the owner rules are met, there's a lean cost default, the owner's hand has a place, and it's the most interesting version of itself.
  - For the branches I add: **a whole point of view (one sentence decides form, material, graphics, making and feel), and a picture that makes him want to take it to the park.** A nice detail isn't a point of view.
  - The owner has paused 9s (TYPE CASE, HYMNAL) to narrow the set, but he has never sent one back on quality. His pattern: he reacts to specific physical annoyances (dividers, lip, slot-as-fader, balance) and to cost and name; he rewards texture he can feel (rings, pegs, felt).
- **Likely owner objections, by branch:**
  - CHAMBER: costume, +4 mm closed, reversed keys;
  - RAIN: busy or dizzy, +8 mm width;
  - BUTTERFLY: plastic next to real wood looks cheap, "just a plank on ONE SHEET";
  - DIPTYCH: too close to CHAMBER, fussy scales, cords in the way.
- **Owner questions (in the jam §6):**
  1. CHAMBER's reversed keys OK?
  2. Pegs worth +8 mm width (ONE SHEET) / +4 mm closed (FOLD)?
  3. Park session length (battery)?
  4. Tapped tempo sent out as MIDI clock?
  5. The furniture book's exact title and author?
- **Not scored yet.** **Next:** visual leads the concept builds, with systems on the geometry in parallel. I steer after every pair of their turns, then score all four in one pass and name the owner objections first.

## Status (fix check, 2026-11-13 ~11:35): READ THIS FIRST
- Both must-fixes verified by eye: the slot is gone. A round opening now shows in the 3/4 views (A on all three, FOLD E). FOLD D's end view shows three ports (MIDI IN, MIDI OUT, USB-C), and its note is corrected. I saw no regressions in the changed sheets: labels, stand and callouts are unchanged.
- **HUSH 9, ONE SHEET 9, FOLD-105 9 hold.** The 3/4 joystick reads unmistakably now. Next: the owner picks a concept, then I check handoff.md. The nice-to-haves below are still open.

## Status (CHECK after the 120° stand + bend-joystick redraw, 2026-11-13, new director): READ THIS FIRST
- Scope: a check, not a round. Owner asked: FOLD lid less steep so the face catches more light; bend must be a joystick. Change: FOLD stand 105° -> 120° (spec rev 5.7, stays 44.4, tip 6.8 N) + bend redrawn (stem, flared cap, round ring with 2 pointers, round tag, B-sheet callout "BEND IS A JOYSTICK, NOT A FADER").
- **Scores hold: HUSH 9, ONE SHEET 9, FOLD-105 9**, conditional on must-fix 1 (drawing only; I check it, no re-score). Work changed in the stick and the stand (plus footers); I saw no other regressions by eye (pixel-diff boxes vs versions/v1 are large, so this is a visual check, not a proof).
- **Stand (sheet E): passes.** Side view measures right: lid 60° to table (=120°), stay ≈ 44 mm at ≈ 60-62°, pivot d ≈ 31 from the hinge, tip 59 behind. 3/4 visibly leans back and the panel now reads cream, not grey: the owner's "catches more light" is shown. Believable.
- **Joystick: B sheets pass** (plan = round well + cap + 2 pointers; callout clear, push/pull directions consistent). **3/4 views (A x3, FOLD E) half-fail:** stem + flared cap read as a stick, BUT the round ring contains a dark elongated slot along the bend axis. That slot is the fader cue the owner reacted to, and it contradicts B and the callout ("gate under the panel"). Front elevations (D): T-silhouette OK on FOLD/ONE SHEET; HUSH's is hidden behind pegs (acceptable for an elevation).
- **Must-fixes:**
  1. A (HUSH, ONE SHEET, FOLD) + FOLD E: replace the visible slot with a round aperture (round hole/boot, Ø ≈ ring inner), matching B. Gate stays under the panel.
  2. FOLD D: the purple note says "rev 5.6 lists no MIDI IN", but how-it-works rev 5.6 adds MIDI IN (y 70) beside MIDI OUT (y 80) + USB-C (y 90-99). Draw the 3rd jack on the base's right end and fix the note. (Pre-existing, not caused by this change, but it now contradicts the spec.)
- **Nice-to-have (not blocking):** E headline "FOLD-105 ... standing at 120°" invites confusion; add "(105 = half depth)". FOLD how-it-works line ~58 still says stay 52.4 mm (superseded by rev 5.7 header; tidy). E side view omits the lid's knobs (pre-existing). HUSH B PARA-legend flag still open (pre-existing).
- **Owner state:** all three LOCKED as v1 (versions/v1/); he leans ONE SHEET or FOLD; his creative-rounds request was withdrawn ("forget i said that"). No new round.
- **Next:** check fixes 1-2 by eye; then the owner picks -> handoff.md check against the approved concept + owner.md.
- **Lesson added:** when a control's identity is the owner's complaint, check it in every view type (plan, 3/4, elevation): renders inherit old geometry (the slot) even after the plan is redrawn.

## Status (after round 5 scoring, 2026-11-13): READ THIS FIRST
- **Round 5: HUSH 9, ONE SHEET 9, FOLD-105 9.** All three go to the owner after **S1**, a shared label-clearance pass. S1: short labels under section headings (echo: type · time; reverb: decay · type), ≥ 1.5 mm between legends and between legends and skirts, grow the depth up to ≈ 10 mm if needed (owner: "grow the panel"). I check S1 only; no re-score.
- **FOLD-113 is not offered:** it fails the gap (75.45). For more runtime, use a bigger cell in the same footprint, not deeper halves.
- **Must-fix / test before handoff:**
  - FOLD: the right stay groove clashes with the lid-wall jacks (prefer moving the I/O to the left end face). Systems also confirms the AFTERTOUCH toggle and the Daisy Seed placement.
  - HUSH: the steam-blocking corner test (now incl. edge A's r 4 front).
  - ONE SHEET: the rings coupon, now a pre-build check, not a score blocker. The fallback is per-volume bottom patterns in the 3MF.
- **Owner's latest asks (all reflected):** echo + reverb on a Daisy Seed with the full 8 FX controls; DRIFT; MIDI out; aftertouch with its own switch; key edge A/B (show both); front views; FOLD standing lid at one fixed angle (105° on flush brass stays); ONE SHEET smooth + rings only. Paraphonic mode is pending his key-tracking question (eng).
- **Lesson:** feature additions break legends before they break knob pitch. Add a legend-clearance check to every layout change. FOLD still needs the open-depth check on every change.
- **Next:** S1 → owner picks (and chooses key edge A/B) → handoff.md check against the approved concept + owner.md.

## Earlier status (after round 4 scoring, 2026-11-12): READ THIS FIRST
- **The owner paused TYPE CASE and HYMNAL** (both 9, on file). Active: HUSH, FOLD, ONE SHEET.
- **His round-4 brief:** unibody, screws from the back (ideal, flexible); HUSH organically rounded; FOLD = Proof walnut + white, rounded edges with flat top and bottom, block + pickguard; HUSH and ONE SHEET loaded from behind; keys to the front edge, knobs logically split, narrower; no case work; internal battery required.
- **Round 4 scores:**
  - **HUSH 9**, to the owner. Must test: steam-blocking felt directly on a PLA/PETG shell risks warping (≈ 100 °C steam). The corner test decides; the fallback is blocking over a separate form. Also the I/O board x ≈ 60–230 and the speaker x ≤ 243.
  - **FOLD 7.** Blockers:
    1. the ≈ 119 mm mid-deck gap (open 286 × 234). Fix: slim cells (≈ 8 × 30 × 40 class) in the existing 31 mm lid band, halves back to ≈ 86–90, PLAY→VOICE ≤ ≈ 60, open ≤ ≈ 185;
    2. EMPHASIS split from CUTOFF across the hinge. Eng: can it cross the ribbon? Otherwise it's an owner decision;
    3. black section names, not ochre.
  - **ONE SHEET 8, unchanged.** The coupon is still unprinted. Print it: reads → 9, doesn't → drop.
- **New lesson:** FOLD couples its halves' depths. Any added depth shows up twice, so check the open depth after every change.
- **Next:** HUSH to the owner. FOLD redraw after systems/eng answer the battery and EMPHASIS questions. ONE SHEET waits on a physical coupon. If the owner turns down a 9, record his reasons here.

## Earlier status (after round 3 scoring, 2026-11-12): READ THIS FIRST
- **Round 3:**
  - **HUSH 9** (cream knobs, "Nothing shouts"; NOT black as the coordinator said).
  - **FOLD 9**: one white panel, black knobs, walnut palm rest, 12 mm panel shift, closed 51 shown beside a book. **Must-fix before handoff:** TUNE collides with the bend stick when closed (a ≈ 6 mm well or a lower cap). Systems also confirms the shift, the 18T pot shafts and the black knob's price.
  - **ONE SHEET 8**: "toolpath is the finish" is the right idea, but it's unproven. It needs a photographed test coupon (≈ 80 × 80, three regions, smooth PEI) on sheet A. Coupon reads → 9. It doesn't → drop the concept.
- **With the owner at 9:** TYPE CASE, HYMNAL (round 2), HUSH, FOLD (round 3). The owner was waiting on HUSH and FOLD before approving.
- **Carry to the owner:** FOLD at 51 closed (≈ 44–47 floor) vs HYMNAL's 38; names from `naming.md`.
- **Next:** the owner picks a concept, then handoff.md. Check handoff.md against the approved concept and owner.md, and send back any drift. If the owner turns down any 9, record his reasons here.

## Earlier status (after round 2 scoring, 2026-11-12): READ THIS FIRST
- **Owner context:** the budget instrument is now THE instrument ("the most interesting thing overall"). He liked TYPE CASE, HUSH and HYMNAL. "Little D" is dropped as a name (`../naming.md` has candidates; WALLOP is ★). His hard rules: nothing raised among the knobs, nothing raised between the keys and the controls, and tactile section separation only if it doesn't get in the way. 3D-printed enclosures are welcome; knobs and keys must still be bought. He asked for printed ONE SHEET, printed HUSH + felt, and FOLD (two parts, controls on top, a white panel in a dark surround, printable first, walnut later). He saw the round-2 A sheets unscored.
- **Round 2 scores** (`../scores.md`):
  - **TYPE CASE 9** and **HYMNAL 9**: these go to the owner.
  - HUSH 8: blocker is the yellow knobs (loud and toy-like on the "hush" concept). Fix: cream.
  - FOLD 7: fixes are one white panel in two plates (not five), redraw at closed ≈ 51 plus show the ≈ 44 floor, give the palm rest a job and a surface, show scale when closed.
  - ONE SHEET printed 7: its idea lives in the making, not the object. Either make the print visible on the face, or retitle it as the plain baseline.
  - **UNDER GLASS 6: killed.** Parallax hides the windows, it's over cost, and the owner never asked for it.
- **New rulings:**
  - **R5:** a knob colour must follow from the concept's idea; repeating a colour is fine. This replaces my round-1 "different colour per concept".
  - **R6:** five concepts maximum in front of the owner.
- **Still in force:** R2 (pitch ≥ 20, IV's played row 25/24, ≥ 7 mm to a section break), R3 (≈ 36 body / ≤ 40 to knob tops; FOLD closed is the exception, for the owner to decide), R4 (flush).
- **Owner questions to carry with the passes:** FOLD at 44–51 closed vs HYMNAL at 38? Any name from `naming.md`?
- **Next:** one quick round (HUSH colour, FOLD fixes, ONE SHEET choice), then re-score. If the owner turns down a 9, record his reasons here: they are the best signal of what a 9 means to him.

## What a 9 has meant so far (my calibration)
- Every visible choice traces to one idea, the round's owner rules are met, there's a lean cost default, and the owner's hand has a place. Plus, from round 2: it has to be the most interesting version of itself, not just a tidy one.
- My blind spot: economy and process ideas (ONE SHEET, my own) don't make a form by themselves. Device rules I add for the set (knob colours) mustn't override a concept's own logic.

## Earlier status (after round 1 scoring, 2026-11-12) — READ THIS FIRST
- Round 1 scored (`../scores.md`): **TYPE CASE 8, HYMNAL 8, HUSH 7, ONE SHEET 6 → replaced by UNDER GLASS.** Nothing at 9; nothing to the owner yet.
- Rulings: **R1** lip rule H3 retired (bought Choc V2 switches; lip no longer mechanical) → H3' "key edge": comes from the idea, hides switch housings/strip C, prevents snags; section kept as fit check only. **R2** knob gaps: 4 mm rejected; keep Tayda KN1250; min 20 mm pitch, 24 mm for IV's played row (CUTOFF/EMPHASIS/CONTOUR AMT); take width from section gaps; never shrink the knob. **R3** thickness vs owner's ~36 body / ≤40 knob tops; all depend on eng E-L2 (thin speaker) — must be answered before round 2.
- New owner answers absorbed: show BOTH self-protecting and sleeve (UNDER GLASS = sleeve now, the other three self-protecting); velocity LOUD/BOTH/FILT toggle; bend up+down; "Nods are fine but I want to see breadth of explorstion"; ~36 mm body; standard printed board; show BOTH flat tops and pegs (HUSH pegs, rest short flat tops); no custom keys → Choc V2 silent + pressed tops (eng velocity-and-keys-v2.md; short tops S1 default, piano tops +$29.85 stabs).
- Owner is impatient ("Where do I see these?"). One fast fix round, then show all four together.

## Round 1 record
- TYPE CASE 8: right idea, use-pole done well. Blockers: rim 40 reads chunky; knob crowding; grey blank cards. Fixes: R2, rim ≤38 + edge chamfer, real card content, thumb-at-wall view, ≤$15 India ink.
- HYMNAL 8: best vibe picture; patch chart in lid; drop-front palm rest. Blockers: cost (+$15–34 enclosure + $29.85 stabs), retro costume (red knobs, script label). Fixes: short tops default (piano as +$30 inset), lean ≤$20, modern neutral panel, label as the owner's own placeholder, show drop-front latch.
- HUSH 7: most distinct form (maple pegs through felt). Blocker: cost $59–63 wool / $30–40 blend. Fixes: ≤$30 version (felt on deck/panel only, flap optional), one hard-plate material, eng check felt bottom stop vs velocity, wear inset.
- ONE SHEET 6 (my own idea; cut it hard): idea invisible in the 3/4, reads as TYPE CASE without walls / default laser slab; all-birch keys lose white/black; lip ruler has no job; fails "breadth". Its making rules survive as an option for ply concepts.
- UNDER GLASS (new for round 2): printed board under reverse-painted clear acrylic with windows; aluminium U-channel rails; sleeve body; different knob colour; ≤$20.
- Set-level blocker: **breadth** — one footprint, one layout, cream knobs. Fix through materials, knob colour, hero camera state.

## Updated blocker hypotheses
1. Cost vs vibe (confirmed: HYMNAL and HUSH lose their 9 on cost).
2. Sameness across the set (new; owner explicitly wants breadth).
3. Thickness depends on unanswered E-L2.


## Earlier status (end of jam, Turn 3, 2026-11-12) — partly superseded above
- Phase: concept jam has CLOSED with READY. **No scores yet.** The first scores will be provisional because no brand or visual foundation exists.
- Full-instrument design is PAUSED (owner). Its director notes are in `archive/full-instrument/notes/director.md`; I kept consistent with them: hero CUTOFF, one light, no Moog cheeks, cost/rigmarole as the recurring risk.
- Concepts going forward: **TYPE CASE, ONE SHEET, HYMNAL, HUSH.**

## The owner's tests for this work (his words → my judging tests)
1. "coherent in form with some clear perspective": a single idea has to generate the silhouette, material, graphics and making. Visual's four-part test is the one I'll use.
2. "Design principles with a solid basis of logic in the idea of the thing": every principle needs a "because" that traces back to what Little D *is* (budget, hand-built, portable and complete, a reduction of the Model D, silent keys).
3. "Get creative" plus the earlier "expected / highly designed for use … and others with more sauce / vibe": the set has to span both kinds.
4. Cost is his main concern ("250 feels high"). Anything that adds cost has to earn it.
5. "it should feel good to use": OP-1 is a loose size reference only.
6. He needs to see mocks to judge looks, so a believable 3/4 picture per concept is mandatory.

## Key facts that bind the box
- From `eng/keys-answers.md` (arrived mid-turn): slim RAIL keys at ≈ 22 mm, lip ≈ 26 mm, control zone ≈ 30 mm, box ≈ 180 mm deep (was 170). Rod support combs every 3–4 keys, hung from the lip. RAIL ≈ $52–58 ($35–46 on scrap).
- My reading: **the lip is the spine** (top stop + rod carrier + step). This became house rule H3. It's the strongest form-logic hook we have, and it's shared across concepts.
- Envelope ≈ 290 × 180 mm; ≤ 36 mm with knobs; 40 mm ceiling pending the owner.

## Rulings (Turn 3)
- SPREAD merged into TYPE CASE (same kind; SPREAD's enclosure is just a tray). Numerals I–V carried over; emblems optional, no occult imagery.
- RADIO and UNDER GLASS are donors (bottom speaker, kerf band; reverse-painted acrylic). STRATA is dead.
- HYMNAL must resolve book vs cigar box (cigar-box guitar = the folk lineage of cheap hand-built instruments; from my random draw).
- HUSH pairs with DISH maple-plug keys (owner cited Critter & Guitari), if velocity and feel hold.
- ONE SHEET is my own new direction (cost as the idea; one 12 × 24 in sheet; nest arithmetic ≈ 72 % for the shell). **My favourite, so be hard on it.** Its kill risks: the laser-craft / Etsy look, nest-forced proportions, the story staying invisible or turning into a gimmick.
- House rules H1–H9 in jam.md §4: inherit logic not looks; prune don't shrink; lip is the spine; one hero knob (CUTOFF) plus one bought knob family; cost discipline (enclosure > $15 needs a named saving); machine marks exact / hand marks meant; one status light, not-in-control light by CUTOFF, guarded power switch; envelope; jacks on one edge, never the stick end.
- Deliverables per concept: jam.md §5 (3/4 picture, top view in mm, H3 section, carry/play states, principles with "because", cost/hours/thickness, six axes).

## Likely owner objections (watch for these when scoring)
- **Cost creep**: HYMNAL (+$10–20) and HUSH (+$15–30 felt) in particular. The biggest risk, given his history.
- **"Laser-cut craft / Etsy"** look: TYPE CASE (tray), ONE SHEET (ply box).
- **Costume**: HYMNAL going "olde", HUSH reading as a tech sleeve, tarot remnants.
- **Too thick**: TYPE CASE ≈ 34–36, HYMNAL ≈ 40 closed.
- **Durability/grime**: felt pilling, bookcloth hinge wear.
- Anything Moog-looking (cheeks, wedge). Note that eng's "key step in front of control zone" is a step, not a wedge; keep it from reading as a wedge.
- Fiddly use: TYPE CASE knobs near cell walls; HUSH roll flap as rigmarole.

## Open questions
- With the owner: trade dress for Little D; bend up-only vs one axis; bare vs printed board; self-protecting or sleeve; 35–40 mm OK; **(new) +$10–20 for self-protection vs ~$12; (new) flat key tops vs maple pegs.**
- Non-owner: Vector Space laser bed size and sheet stock (ONE SHEET depends on it); knob family from real Tayda/US stock (visual, before mocks); DISH velocity/feel (keys/eng); wool felt price per real area; bottom-speaker loudness on a lap.

## What's blocking a 9
Nothing scored yet. My hunch for the recurring blocker: **cost vs vibe**. The sauce concepts get their charm from added material, and the owner's first concern is cost. The second hunch is **laser-craft genericness**: proportions and joinery that read as "made on a laser" rather than as an instrument.

## Next
Concept building (systems + visual) on the four, against H1–H9 and the §5 deliverables. I steer after every pair of their turns. Then I score all four in one pass, naming the owner objections first. Kill and replace any concept that can't reach 9; ONE SHEET gets no favours.
