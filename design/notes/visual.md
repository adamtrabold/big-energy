# Visual designer notes (instrument; working name retired)

## CATHEDRAL lid, director's 9 condition (2026-11-13 evening)
- "filter" heading (21.0, d 66.5, HS 3.0) + rule (x 43.5, d 31.0–58.5) for the kbd / filt mod column, mirroring "out" (262.5, 66.5) / rule (242.5, 7–58.5). FILT MOD → (23.5, d 35.0). Constants `NV_FILT_MOD_D`, `NV_FILTER_HEAD`, `NV_FILTER_RULE` in `rb.py`, applied in `nv_overrides`.
- `/tmp/scr/nv_kalam.py` now takes control positions from `nv_overrides` (it was using the checker's stale FILT MOD).
- Checks 0 / 0. Re-rendered lid top, full top, standing. Positions sent to systems for the checker (with the earlier real-Kalam overrides).


## CATHEDRAL, steer 3 fixes (2026-11-13 evening): director's 8 on the lid
- Systems b3e5525: band B mirrored (filter at 63.5 / 83.5 / 103.5, KBD + FILT MOD column at x 23.5), VCO spacing 20 / 25, my numbered legends + "osc 3 ctl" + contour headings in the checker, HS 3.0.
- **rb.py:** `nv_overrides` stripped of numbering / contour split (systems own them); now holds only real-Kalam fits: contour headings d 67.5, osc|mixer break from 70.5, oscillators / mixer +0.4, reverb heading +2 x, FOLLOW words beside (off · follow, gap 6.4). `NV_UD_GAP` / `NV_UD_SZ` env-tunable (1.75 / 1.69).
- **Checks:** nv_check3 (systems' rules + my overrides, with the beside / updown shifts simulated) 0; nv_kalam 0.
- **Re-rendered:** `rb_nv_lidtop`, `rb_nv_top`, `rb_nv_stand` → `img/cathedral-lid-signal-order-8.7px-per-mm.png`, `img/cathedral-nave-top-8.3px-per-mm.png`, `img/cathedral-nave-standing.jpg` (scripts `/tmp/scr/s3_figs.py`, `/tmp/scr/lid_fig.py`). Closed side, window drawing, keys unchanged.
- **Doc:** rev 5.1; steer-2 "superseded" captions removed; "big energy" on the plate (owner 17:37).
- **Open:** the filter switch column may read orphaned (bracket / break option); systems to fold FOLLOW beside + heading nudges.


## CATHEDRAL, steer 3 (2026-11-13 ~18:40): the lid in signal order (systems §17 P)
- **Owner 18:00** (verbatim in director.md / brief; screenshot `design/owner-refs/2026-11-13-1800-top-panel.png`): no logical grouping; effects at the top confuse; signal order synth → fx → output.
- **Systems P:** band A sources (oscillators by VCO ‖ mixer), A' their switches; band B contours (filter left, loudness right) with B' switches; band C echo (+FREE/SYNC) · window · reverb; out column DRY PAN / FOLLOW / VOLUME at x 262.5. All in `layout_check.py` (BREAKS, SECTIONS, "right" / "updown" legends).
- **rb.py:** `Nave.lid_face` rewritten to read lid / BREAKS / SECTIONS / legend placements from the checker; `nv_overrides(lc)` holds my changes: "filter contour" / "loudness contour" headings flush left at d 65.5 (replacing "contours"); "osc 3 ctl"; range / wave numbered by VCO; A-row headings +0.5; osc|mixer break from d 68. `NV_UD_GAP` 1.75 for up/down words; ticks under up/down words and into the window dropped (extra nuts). Job `rb_nv_lidtop` (px_per_mm 15 → measured 8.7). "big energy" now drawn in the lozenge.
- **Checks:** `/tmp/scr/nv_check3.py` (systems' rules on my overrides): 0. `/tmp/scr/nv_kalam.py` (real Kalam, ticks, window, pegs): 0.
- **Image:** `img/cathedral-lid-signal-order-8.7px-per-mm.png` (only render this pass; composed by `/tmp/scr/lid_fig.py`). Steer 2 standing / top captions marked superseded.
- **Doc:** rev 5, new top section with the signal walk paragraph, figure, my overrides, opens (heading size 2.0 < legends 2.35; standing re-render after approval; systems to fold overrides).
- **Not published** (wait for the director's 9).


## Name (2026-11-13, after turn 6): "Big Energy"
- Owner: "name to come -- we're calling it big energy" (owner.md, naming.md).
- My call: lowercase "big energy" in Kalam 2.0 inside the 16 × 5 lozenge under the window (`Nave.NAME`, drawn in `name_mark`), ≈ 9.2 wide in the 15.2 × 4.2 field. In the doc (§6). Option later: a cast-brass plate, raised letters ≥ 0.5.
- **Not rendered yet** (coordinator): it goes into the next render pass after his CATHEDRAL answer. The current images show the lozenge blank.


## CATHEDRAL, turn 6 (2026-11-13 ~17:30): director's 8 → fixes 2 and 4, plus systems' 1 and 3 rendered
- **Director scored 8:** (a) FX row off-centre, (b) R3 empty knob, (c) no lid section names, (d) hinge ear lobe past the back.
- **Systems** re-centred the FX row (`FX_DX` −18.5, `FX_BREAKS` in layout_check.py) and removed R3 (base right MOD MIX 199 · DRIFT 230 · TAP 261). `Nave` now reads `FX_DX` / `FX_BREAKS` / the toggles' positions live; breaks left of the row are skipped.
- **Mine:**
  - section names restored at d 67.5 (`NV_SECTION_D`), Kalam 2.4, oscillators x 14 left / mixer x 143 / contours x 272 right.
  - the name lozenge moved under the window (d 2.2–7.2, axis): at d 94.6 it sat in REVERB TYPE's fan after the re-centre.
  - hinge ear: `Nave.EAR_R = 3.0`, a small ear hulled to a 1 mm web stub (the rev 1–4 r 5.2 lobe stays for `Cathedral`). Pushed back with a proof: flat-open needs Ay ≥ 108 (109 with the seam), so the ear can't be fully inside; ≈ 4 mm nub remains. Options for systems: offset pivot + rabbet, or knuckles.
  - doc honesty: Ø 10 vs 14.9 knobs; 55.2 conditions (else 56.7–58.8); R-TALL offered.
- **Checks:** nv_check (layout_check rules + my legend changes) 0; nv_kalam (real Kalam, ticks, window, pegs) 0. Lozenge not in either checker (ink outline, clear by eye: 1.8 below the window's lowest slot tip).
- **Re-rendered:** `rb_nv_stand`, `rb_nv_top`, `rb_nv_closed_side`; figures via `/tmp/scr/nv_figs.py`. Window drawing and keys unchanged.
- **Next:** director checks by eye; publish only after a 9.


## CATHEDRAL, turn 5 (2026-11-13 ~17:10): steer 2 "nave and rose" rendered from systems §16
- **Owner 16:52** (verbatim in director.md steer 2): off-centre is bad, the gap is unresolved, size the speaker for sound, moving components is OK, more brass than black.
- **Look doc → rev 4**: opening answers his three complaints; "The whole" (standing, top, closed side); §1 keys A lead / C alt; §2 played row (low gold knobs: "what the hands play is brass-toned, what you set is black"); §3 window Ø 46; §4 texture; §5–7 kept; Open rewritten. Removed §2 (A/B) and §2b (tower / off-centre circle).
- **Images now (5, all linked):** `cathedral-nave-standing.jpg`, `cathedral-nave-top-8.3px-per-mm.png`, `cathedral-nave-closed-side-14px-per-mm.png` (55.2 dimension), `cathedral-nave-speaker-window-20px-per-mm.png` (front + section), `cathedral-keys-brass-A-C.jpg` (POV-Ray). **Deleted:** A/B standing, closed-with-book, grain detail, speaker options, brass-keys-metal, grille options.
- **Code:**
  - `rb.py`: class `Nave(Cathedral)` reads `design/branches/concepts/cathedral/layout_check.py` live (`_lc()`): lid rows / legends / window / base row. `low_knob` (Tayda Ø 10 × 8 gold, seat 1.0), `stick_low` (cap −3.6), `GOLD_K`, `NV_SW_LS` 1.55 (switch legends beside), `NV_BEHIND_EXTRA` 1.0. Route R-LOW lifts the lid face +2.5 (AXZ +1.25); R-TALL +7.0. `window_slots` / `speaker_window` (Ø 46, 1.8 / 3.0 → 15 slots, 945 mm²). `sync_toggle(..., gap=)`. Base end grooves removed (stray slashes). Cathedral default palette now `brass-black`; `tap_style` brass whenever brass is in the palette. Jobs `rb_nv_stand`, `rb_nv_top`, `rb_nv_closed_side`, `rb_nv_closed`.
  - `ct_brass.py`: `BlackPlated` material; `board(knobs=False, nat_override=)`; jobs `ct_keys_A`, `ct_keys_C`, `ct_keys_A_macro`.
  - Figures composed by scratch scripts `/tmp/scr/nv_figs.py` (standing / top / side / window drawing, with `brassify()`) and `/tmp/scr/ct2_figs.py keys` (not in repo).
- **Checks:** `/tmp/scr/nv_check.py` (layout_check rules with my two legend changes): 0. `/tmp/scr/nv_kalam.py` (branch_check collide, real Kalam, ticks, window, pegs): 0. Before the changes: 8 legend-tick clashes (behind legends on top ticks) and 4 switch-legend clashes.
- **Decisions:** keys A lead (more brass, normal reading); black sharps drawn as black-rhodium brass (systems' pick: same mass, one velocity calibration); gold low knobs (with the honest anodised-vs-cast risk; buy one of each); switch legends beside toggles; no lid section names for now; R-TALL not rendered (same from above).
- **Open:** director scores; ⚑ moves + R3; systems to fold my legend changes into layout_check; maker buys (plugs, Sculpteo quote, gold / black knob, groove patch, bench the window).
- **Don't publish until a 9** (director). Committed my files only, as Adam.


## CATHEDRAL, turn 4 (2026-11-13): speaker round 2 image (owner: no key-side speaker, no eye; "lines up and down" or off-centre circle)
- **Image:** `img/cathedral-speaker-options-standing.jpg` (2424 × 1697): top row, standing B with the pipe tower (left) and the off-centre circle (right); bottom row, close band views. Linked in look doc §2b. P1a (rounded rect) and P2 (façade) were dropped at the owner's steer (rendered P1a / P2 / P2_back in out/, not published).
- **rb.py:** `Cathedral(speaker=None|"P1a"|"P1b"|"P1c"|"P2", centre_play=False)`; `rrect_slots`, `tower_slots` (TOWER 8→18→8, foot d 28.7, no foot rule: it hit "mixer"), `vcircle_slots` (P1c: R 10.9 + ring to 12.5 at (160, d 37), systems' spot); P2 slots in the 7 centre pipes; `play_dx()` hook in Branch (stick well, breaks) + Cathedral (row, names): +47 when centred; `tap_style()` hook, `r5.tap_cap` wrapped for "brass" (TAP = sharps' head); `stand_point()` for close cameras; jobs `rb_ct3_{P1a,P1b,P1c,P2}`, `rb_ct3_{P1b,P1c}_band`, `rb_ct3_P2_back`.
- **Checks:** scratch `/tmp/scr/ct3_check.py` (branch_check §7 on B + centred PLAY row + grille as obstacles): P1b, P1c 0. Precise tower capsule check: min 1.68 ("mixer"). Circle sweep `/tmp/scr/circle_fit.py`: with ring, a circle fits only x 158–176 (Ø 22 field); agrees with systems.
- **Brass in OpenSCAD views:** `brassify()` in `/tmp/scr/ct3_fig.py` re-maps brass-hue pixels' shading onto a metal ramp (not ray-traced). Good enough at this scale; POV-Ray (`ct_brass.py`) is the true look.
- **Base end:** I recommend re-centring the PLAY row on x 143 (systems option 2), ⚑ D+O. Rejected VOLUME / TAP back (undoes "together") and lozenge / lights (ornament).
- **Pick:** tower (axis rule, "up and down", CATHEDRAL). Circle: OK only at its one spot.
- **Next:** owner picks the speaker; then the re-render pass (closed, standing, keys) once layout and back slot are settled.


## CATHEDRAL, turn 3 (2026-11-13): director steer 1 team rulings applied; no final re-render (waits for owner's layout answer)
- **Look doc → rev 3** (`design/branches/concepts/cathedral/how-it-looks-and-feels.md`): header lists the rulings; §1 now shows brass ray-traced; §2 B label fix; §3 ruled; §4 texture BUILT (spec); §5 slot finished dark if open (director S1); §6/§7 ruled; Open rewritten.
- **Images:** +1 `img/cathedral-brass-keys-metal.jpg` (2 × 2, 2424 × 1584: A / B / C / macro of polished vs aged-unlacquered brass). **Deleted** `cathedral-peg-colours-real-parts.jpg` (flat yellow, against ruling 9). Total linked images: 6.
- **New renderer:** `design/concepts/_mock-src/ct_brass.py` (POV-Ray, installed via apt this turn). Studio sky sphere + area light + white back strip for reflections. Jobs ct_brass_{A,B,C,macro}; `--test` for 800 px. Simplified scene (keys, plate R 7.7, block R 12, PLAY knobs, red CUTOFF; no joystick). It can be extended for the final standing / closed views if the director wants brass believable there too. Grid composed by `/tmp/scr/ct2_figs.py brass` (not in repo).
- **rb.py changes:**
  - **Fixed a bug I introduced in turn 2:** a string replace had also changed Branch / Chamber `lid_back` to use an undefined `screw`. Restored; all models build.
  - `Cathedral` defaults now `palette="black-brass", spine="none", grain=True`.
  - **Grooves (ruling 4):** `GROOVE_W/D` 0.4 / 0.25; `arch_lines` (7 nested parabolic arches), `side_lines`, `ring_arcs`, `grooves_on(lines, clip2d, M, col, minus2d)` via multmatrix; `Cathedral.grooves_base` (underside, front, hinge side, ends; right end y < 58 clear of USB / MIDI) and `grooves_lid` (back minus `FACADE_FIELD` (30, 8, 256, 86), apex at x ≈ 262; far wall z ≥ 13 above I/O; ends). Render stand-in = 0.03 strip in darker walnut (`GROOVE_COL`).
  - `rb_ct_closed` no longer runs the `cathedral_grain` post-process (grooves are modelled).
  - **B labels:** `rows_branch(..., back=)`; `Branch.behind_names()` / `sync_dy()`; Cathedral B: behind offset on, REPEATS behind, `SYNC_DY_B = 1.5`. `branch_check.py`: A 0, B 0, TOTAL fails 0.
- Groove look checked only in low-res scratch renders (deleted): reads on the underside as nested arches; on the lid back only in the margins around the field (by design).
- **Open:** owner's four answers; re-render pass after layout answer (closed, standing, keys; maybe via POV-Ray); groove-depth coupon (0.25 / 0.35); H measurement; brass head mass test; Sculpteo quote.


## CATHEDRAL, turn 2 (2026-11-13, NEW visual designer; previous session ended): real-part keys, no machining, no spine, brass
**Inputs this turn:**
- Systems `cathedral/how-it-works.md` §10–11: Cherry Tree Toys 3/8" mushroom plug (head 12.7, tenon 9.53 × 3.2; birch SKU 31 / oak 31-O; head height unpublished) on a printed PETG carrier (cup Ø 9.6 × 3.3, neck Ø 11.2, 2.8 mm neck showing, deck hole Ø 12, felt stop moved under the deck); printed pegs allowed; stays / hinge leaves → printed 316L (JLC3DP) or PETG.
- Owner 14:30–14:34: no machining; printed or bought keys; external / metal printing OK.
- **Owner 14:40 (came mid-turn via the coordinator):** "I don't want a spine can we route cables through a hinge. Engraving texture I meant fine line texture — I'll probably do a design for the pipe lines. And what about brass and black keys? Or all brass? Could 3d print and reminds me of a cathedral".

**Done:**
- `design/branches/concepts/cathedral/how-it-looks-and-feels.md` → **rev 2**. Rewrote the header, POV table, §1 (keys), §4 (texture confirmed, façade = placeholder, constraints for his façade), §5 (no spine), §6, **new §7 (metal)**, Open. §2 / §3 kept (captions on the rev 1 renders now say what's stale).
- **Image:** one new, `img/cathedral-peg-colours-real-parts.jpg` (2 × 3 grid, 2424 px square, six options A–F). **Deleted** the superseded `cathedral-peg-colours-2x2.jpg`. Every remaining image is linked with a caption.
- **Code (`design/concepts/_mock-src/rb.py`):** `PEGS` dict (head / neck colours per row), `METALS` (brass / steel), `Cathedral(..., metal=)`, `Cathedral.peg_real()` (§10.2 geometry: hole ring Ø 12, neck Ø 11.2 to deck + 2.8, head 1.2 rim + dome, top deck + 6.8, H drawn 4.0), stays colour reads `METALS` via `getattr(self, "metal", "brass")` in `Branch.stand_extra`. Jobs `rb_ct2_col_<peg>` (7 incl. birch-birchblack, not published) and `rb_ct2_closed_steel` (rendered, **not published**: steel became the fallback once he asked for brass). Grid composed by `/tmp/scr/ct2_figs.py` (not in repo; it just tiles the six PNGs in order brass-black, black-brass, brass, birchblack-birch, birch, printed-black-cream at 1200 px with 24 px gutters, JPEG q88). Backup of the pre-turn rb.py at `/tmp/rb.py.bak`.

**Decisions and why:**
- **Keys: recommend B = black naturals + cast-brass sharps.** Black joins the knobs (one family), brass is the accent and repeats the case's brass; palette stays walnut / cream / black / red / brass, no brown. A (brass naturals) makes the keyboard loud vs CUTOFF; C (all brass) most cathedral but competes with red; see real brass before choosing. D / E birch (pale, near the cream under a non-ambering clear; dye wears pale on crowns); F printed (exact colours, least instrument-like).
- **One interface for every head:** the carrier cup takes the plug's 9.53 × 3.2 tenon, so cast brass / printed heads are made with that tenon and are swappable after the build.
- **Carrier neck in matte black** (reads as the hole's shadow; heads float like drawknobs).
- **Brass routes:** cast brass via Sculpteo lost-wax from printed wax (80/15/5 alloy; raw / mirror / gold / black rhodium; min wall 0.8; max 125 × 125 × 100; 7–9 business days; price on upload; checked on pro.sculpteo.com this turn) vs brass-fill PLA (colorFabb brassFill named as an example, UNVERIFIED). Feel table in §1: cast = cold, heavy (≈ 5 g solid [CALC], ≈ 2.5–3 g hollow-cup ESTIMATE), worn shine on crowns, tarnished brass reads brown; fill = cool, lighter, satin. Same-feel alternative: all 25 cast, naturals black-rhodium (wears through to brass).
- **Metal:** printed 316L reads matte grey steel → a second metal next to brass keys. Recommend **cast-brass stays**, PETG black 5 × 8 fallback (not grey), 316L only for the hidden hinge leaves. Steel everywhere is a fallback (organ pipes are tin), not a parallel option.
- **TAP:** takes the sharps' material (brass in B).
- **Spine:** gone. Asked that, if the slot stays open, its inner faces print walnut-tone.
- **Fine line texture:** confirmed = case body texture → cathedral grain stays; first print plain. Façade is the owner's to design; gave him the field (x 34.8–251.2), axis screws, push-outs.

**Director's objections:** none received for CATHEDRAL yet.

**Open:**
- Owner: keys A–F; reversed reading; lacquered or not; A / B layout (⚑).
- Systems / eng: brass head mass on Choc V2 silent (return + velocity fit, test one hollow-cup head first); cast-brass stay strength; back slot + cables through the hinge; `branch_check.py` labels on `Cathedral("B")`; B's rose vs the Daisy.
- Maker: buy one birch pack and measure head height H (sets key height; drawn 4.0); one Sculpteo quote (hollow-cup head + stay).
- **Re-render later, not now:** closed view + both standing views (they show the retired spine and rev 1 keys) once systems settles the slot. Use `Cathedral(layout, "black-brass", spine="none")`.

**Next:** director steers (keys, A / B). Then the re-renders above, or the handoff looks once approved.


## CATHEDRAL, turn 1 (2026-11-13): owner 14:12–14:18, CHAMBER x FOLD v1.1; rounds reset; RAIN parked
**Owner's notes:**
- spine probably unnecessary;
- hidden hinges;
- the speaker gap; FX & out far from echo / reverb;
- feet = screws;
- a woodier but subtle engraving;
- consistent plate rounding;
- fewer peg colours, the brown out of place;
- grille rounding (tapered or circular);
- "cathedral" is a better point of view than chamber.

**Systems wrote `cathedral/how-it-works.md`:** side pivots, A / B speaker options, screw-feet, R 7.7 corners, spine dark or none.

**Done this turn:**
- **Doc:** `design/branches/concepts/cathedral/how-it-looks-and-feels.md`, with `<figure>` images all linked.
- **Code:** `rb.py` class `Cathedral(layout, palette, spine)`.
  - Hooks added to `Branch`: `peg_plate2d`, `play_row`, `lid_rows`, `fx_breaks`, `voice_rule_end`, `sync_pos`, `behind` (None = legends stay in front), `grille`; Chamber's `vel_gap`.
  - New helpers: `vesica_slots`, `rose_slots`, `cathedral_grain` (a post-process on walnut pixels), `PALETTES`, `B_FX`.
  - Jobs: `rb_ct_col_<palette>` ×4, `rb_ct_A_stand`, `rb_ct_B_stand`, `rb_ct_closed`, `rb_ct_top_A/B` (tops are for checking only, not published).
  - **Gotcha:** a "glob*" job argument only expands when it's the only argument.
- **Images (6):** peg colours 2×2; A standing; B standing; closed with book (grain, spine, feet); grain detail; grille options drawing at 20 px/mm. All figure composition was done in a scratch script (`/tmp/scr/ct_figs.py`, not in the repo; re-creatable from the doc's list).

**Decisions and why:**
- **Point of view:** "a small cathedral: organ front for the listener, nave for the hands, the wood's own arches." Every curve does a job; costume watch: no tracery.
- **Colours:** recommend **ebony naturals + maple sharps** (organ convention, black = knobs, no brown, no new colour); fallback maple / ebony; the one-colour options shown. Ebony plugs aren't stock (UNVERIFIED), so the route is ebonised maple.
- **Grille:**
  - A = **vesica 66 × 16 at (143, d 37.6)**. Systems' Ø 34 circle overlapped the NOISE / EXT legend and the mixer heading; the real clear depth is ≈ 22 mm.
  - B = tapered circle Ø 27 at (228, 68).
  - Tapered slots preferred over concentric arcs (continuity with v1.1, "same rule as the façade turned 90°").
- **Woody:** my reading is the body's line texture, so **cathedral grain** (flat-sawn figure) at the old line count. Real walnut: pick flat-sawn stock. Print: leave plain. **Confirm with the owner** whether he meant the façade lines.
- **Spine:** keep, **walnut-matched #5a3923**; a near-black spine read as the opening in the render. Runs wall to wall (no knuckles). Oxblood retired.
- **B labels:**
  - V2 toggle legends moved below their toggles (`vel_gap` −8.4);
  - the left voice rule ends at dV2 + 5.5;
  - "free" vs FREQ 3's MIDI dot ≈ 1 mm: systems to check (model exists now).
- **A's base heading:** "effects" (VOLUME left in 7.2).

**Open:**
- **Owner:** colours, the meaning of "engraving", spine.
- **⚑ D+O:** A vs B. My visual read: B is the better CATHEDRAL; reach is the cost.
- **Systems:** checker on `Cathedral("B")`; acknowledge the vesica replacing the Ø 34.
- **Eng:** B base speaker vs the Daisy; side-pivot strength; screw-foot part.

**Next:** the director steers A / B and scores. Then fix, or write the handoff looks.

## BRANCHES, round 2 (2026-11-13): CHAMBER and RAIN fixes (scores r1: CHAMBER 8, RAIN 7; BUTTERFLY retired, DIPTYCH killed)
**Where things stand:**
- Two live concepts: **CHAMBER** (FOLD) and **RAIN** (ONE SHEET). Docs:
  - `design/branches/concepts/{chamber,rain}/how-it-looks-and-feels.md` (rev 2);
  - images in `<figure>` with `<figcaption>`, in reading order;
  - every image in `img/` is linked; stale ones were deleted (chamber-flat-from-above, chamber-closed-printed, rain.jpg, rain-stepping-stones, the old 2-way compare).
- BUTTERFLY and DIPTYCH folders are left as they were (retired / killed); I didn't touch them.

**Owner rules this round:**
- images only where they must be visual, words in HTML;
- images responsive for the site;
- **"dont render a bunch of images unnecessarily"**: render only what a fix needs.
- Director ruling: in-image labels only for geometry (dimensions, scale bars); no "real size" claims on screen.

**CHAMBER fixes done (director's 1–6):**
1. Standing lid re-lit: `relight()` scales the lid plate's median grey to (241, 236, 224), lid region only (ymax 0.6), to keep the ground shadow.
2. Spine (systems R2.1), oxblood bookcloth #6b2c23:
   - closed: `spine_closed()` runs up over the lid plate's edge, so no white line shows;
   - standing: `spine_stand()` drapes in the opened joint.
3. Fallback pegs: `Chamber(fallback=True)` → `chamber-pegs-fallback-colours.jpg`.
4. Façade pitch 8.75, with Ø 4 push-out holes as the mouths of the pipes at x 108 / 178, d 28.3 (systems R2.2). PARA "mono / para / +4" above its toggle. **Kalam is installed** (systems, `~/.local/share/fonts/kalam`); HAND = Kalam.
5. Artefacts:
   - the peg streak was a mesh crack: each head is now one hull (RAIN too);
   - the "pale band" was OpenSCAD's near clip plane: the close-up camera moved to dist 300.
6. Plugs: Woodpeckers 1/2" walnut button plug $0.35 ($0.32 at 25+); Midwest via Zoro $43.55 per 100. Shank dimensions unstated (UNVERIFIED fit). Fallback: maple stained dark.

**RAIN fixes done:**
1. Decay = deep rings (0.9 pitch) in an inner zone (≥ 2.4 mm past the ring start, or half the span), shallow rings (1.8 pitch, lighter tone) out to 14 % short of the band (systems R2.2's printable route).
2. Bands 1.0 inside a section, 3.0 between. `_cell()` pulls each internal half-plane back by half its band; sections come from `rain_section()`.
3. Warm palette: shell #ddd3c1, rings #b9ab93 / #cbbfaa, pegs #aaa192 / #6e675b, mustard CUTOFF. The field runs to the outline over the chamfer. Vertical walls can't carry modelled rings (face-down print = layer lines) — say so if asked.
4. 0 collisions (checker §7).
5. 3-way pitch drawing, no words in it.
6. Re-rendered at arm's length and close.

**Set-wide label fixes (branch renders only; r5 / the locks untouched; patched at import in rb.py):**
- `r5.type_fan` replaced by `_type_fan`: inner row 3.8, outer Kalam 7.2 / Inter 6.6;
- knob ticks dropped wherever they run under a toggle nut (`_ticks_clear`, nut r 4.6 + 0.5);
- "free" / "sync" 0.5 behind the toggle centre;
- RANGE "lo" / "2'" at ±138°, r 10.4;
- VEL legend at 7.7 (CHAMBER);
- STATUS legend beside its hood.
- **Checker result: CHAMBER 0, RAIN 0** (inherited v1.1 clashes included; TOTAL fails 0).

**Renders this round (only what the fixes needed):**
- CHAMBER: main, closed, stand, stand_back, keys, keys_fallback, top;
- RAIN: far, near, top.
- Then `figs_rb.py` exports (it now takes only the current files).

**Open:**
- **Owner:** reversed keys vs the fallback; the TIME dead 15° (director's list).
- **Eng / maker:** spine flex life; the ribbon loop in the seam gap; relief / engraved fill coupon; plug shank fit; RAIN coupon (does 0.2 deep read?); 0.25–0.3 nozzle for 0.6 pitch.
- RAIN's busiest zone is the rear band at arm's length; if the director objects, the next lever is fewer type-name pads (the fans could lose their outer names to a legend line).

**Next:** the director re-scores CHAMBER and RAIN. On approval, write "How it looks and feels" in `handoff.md`.

## BRANCHES, concept turn 1 (2026-11-13): looks for CHAMBER, RAIN, BUTTERFLY, DIPTYCH + site images
Context: the director closed the jam (turn 3). PIERCED and GROUND are killed (GROUND's donors went to every branch: status hood, high-contrast type). Four concepts, each with a "must prove" list. Systems wrote jobs rev 5, `common-how-it-works.md` and four `how-it-works.md` files, checked with `branch_check.py`.

**Owner rules on images, new this turn (all in `design/owner.md`):**
- no A3 sheets;
- not phone-first either: images that look great on the project site at any width;
- **images only for what must be visual** (renders, drawings, diagrams, sections);
- words stay in markdown;
- labels in an image only where the drawing needs them (dimensions, part callouts);
- **an image shows on the site only if a concept doc links it**, in reading order, with a caption.

**Done this turn:**
- **Models:** `design/concepts/_mock-src/rb.py`.
  - Classes `Branch(Fold)`, `Chamber`, `Diptych`; functions `butterfly()`, `rain()` with `rain_field()` (a power-diagram ring field computed from the real layout).
  - Shared helpers: `sync_toggle`, `time_dial`, `status_hood`, `rows_branch` (TIME / DECAY legends behind, OSC 2 / NOISE top ticks dropped), `relight` (lifts the standing lid's grey), `hanging`.
  - Run `python3 rb.py` (≈ 3 min, all jobs) or `python3 rb.py "rb_ch*"`.
- **Web figures:** `figs_rb.py` → `design/branches/concepts/<c>/img/`.
  - Renders as JPEG q90 at ≤ 2400 px.
  - Exact views as PNG, **with the measured px/mm in the file name** (top4's real scale is 11.49–14.48 px/mm, not the requested 12/14; it's measured from the crop).
  - Detail crops are native-resolution with a 10 mm bar.
  - Dimensioned drawings: DIPTYCH standing side, CHAMBER closed front, RAIN ring-pitch compare, BUTTERFLY rear section.
- **Docs:** `design/branches/concepts/{chamber,rain,butterfly,diptych}/how-it-looks-and-feels.md`. Every image is linked in order with a caption; the must-prove tables give my honest read.
- **Environment:** installed OpenSCAD + Xvfb (apt), EB Garamond, a handwriting stand-in (DkgHandwriting Bold).
  - **Kalam is not installable here** (GitHub fonts URL blocked by the proxy policy). CHAMBER's hand-lettering is a stand-in that runs wider than Kalam. **Re-render with Kalam before the owner sees final art.**

**Accepted from systems, and why:**
- FREE / SYNC thrown left / right ("the lever points at the word"): there's no room for words fore / aft.
- TIME / DECAY legends behind their knobs.
- TIME printed over ±135° with a firmware clamp: the scale tells the truth.
- MIXER heading to y 136 (flat).
- BUTTERFLY as a 6 mm walnut top over the printed apron, v1.1 jacks below, joint at y 165, end match: honest furniture.
- DIPTYCH's fold-out feet: physics (0.8 N without them).

**Pushed back or found:**
1. **"free" / "sync" sit on OSC 2's and NOISE / EXT's top ticks.** Systems' label check doesn't count tick rings. Fixed set-wide: the top tick is dropped; DIPTYCH's graduations stop ±35° from the top. The checker should model tick rings.
2. **v1.1's 32 × 6 name lozenge no longer fits** between the moved TIME and DECAY legends. It's now 16 × 5 on the axis at lid d 94.6 (CHAMBER lozenge; DIPTYCH notched red cartouche).
3. **CHAMBER:**
   - RANGE feet set round the knob collided at 20 pitch, so I went to fan rows (16'/8' low, 32'/4' high, lo/2' under the end ticks). Section names moved up to dV1 + 17.5.
   - PARA's legend moved above its toggle, shortened to "mono / para / +4" (wording: systems / owner).
   - v1.1's push-out holes (x 110 / 176, d 54) land on pipes; proposed d 90.
   - **v1.1's lid model is open on the hinge side**: closed, seen from behind, you see the knobs. Systems: spine wall or real slot?
   - Closed, seen from the front, the façade's pipes point toward you: the price of facing the listener when standing.
4. **RAIN:**
   - full "ECHO TIME" / "REVERB DECAY" behind ran into the type-name fans, so the back row is ECHO TYPE / REVERB TYPE in front and TIME / DECAY behind;
   - the field doesn't cover the side chamfer yet (the director asked for every edge).
5. **BUTTERFLY:** the butterfly shrank to 16 × 8 (clears PHONES by ≈ 1.6). The live edge drawn with an axis crown so POWER sits behind the butterfly; with a real offcut, pick it or engrave POWER at y 178.
6. **DIPTYCH:**
   - **the cord as modelled is 38.4°, not 37.4°**; the drawing says so; systems to reconcile;
   - the stand (2 cords + 2 feet + 4 eyes, order-dependent) is the concept's weakest part. Alternative for the director: v1.1 stays, no cords. My view: the faces (dial, graduations, red / black, roman caps) carry DIPTYCH.
   - **It separates from CHAMBER:** dark outside + hand vs engraved red/black inside, pegs vs flat keys.

**Visual decisions per concept (detail in each doc):**
- **CHAMBER:**
  - façade = 25 pipes as 0.6 mm brass-tone line work (relief + wax fill on the first print);
  - walnut naturals / maple sharps on 14 mm felt washers;
  - closed 52.7;
  - serif only on RANGE and the name.
- **RAIN:**
  - stone #d9d6ca, grooves 0.45 at 0.9 pitch, 0.64 smooth seams, lily pads (0.85 margin, R 1.2);
  - mustard 1083 CUTOFF, the only colour; two stone-grey pegs;
  - no grooves, no headings;
  - optional power-on "drop".
- **BUTTERFLY:**
  - matte bone #e2dacb + oiled walnut, sapwood band kept;
  - jack legends engraved, located from the joint;
  - hung tree side up.
- **DIPTYCH:**
  - EB Garamond caps, red italic section names, thin red rules;
  - 31 red hairlines + 11 black majors on every knob;
  - TIME: black ms with "20" / "2s", red divisions with 1/16, 1/8, 1/4, 1/2;
  - red braid cords, brass feet;
  - two swaps.

**Director's objections:** none on concepts yet (first build turn).

**Open:**
- Kalam re-render.
- Coupons: RAIN grooves + pad under a tree; DIPTYCH TIME dial at 1:1; CHAMBER relief fill on wood-fill; BUTTERFLY bone print beside a real oiled offcut.
- RAIN on the chamfer.
- Systems' items above.

**Next:** the director scores the four. Then fix what's objected to. After an approval, write "How it looks and feels" in `handoff.md`.

## BRANCHES, jam turn 2 (2026-11-13): personality + point of view; FREE/SYNC placed
Context: the owner wants branched creative rounds from v1.1 (he leans ONE SHEET or FOLD) with more personality and a whole point of view. His sources: furniture, instruments, tools, art, emotion; "take this to the park and be inspired". Pegs are loved, "organ like" is an example only. **Owner decided echo sync option B (11:58): a FREE / SYNC toggle near TIME, in every branch.** Shared rule (systems, accepted): the board is the constant, only the outside changes.
- **My turn:** `design/branches/jam.md` "Turn 2". Draw script `design/branches/draw-visual.py` (my own decks; every earlier-used Oblique card removed); results recorded in the jam §1.
- **Sketches:** `design/branches/concepts/jam-sketches/`, source `sketch_turn2.py` (layout read live from `fold_r5_check.py`):
  - `t2-rain-top.png`: computed ripple field;
  - `t2-chamber-closed-facade.png`;
  - `t2-ground-horn-section.png`;
  - `t2-butterfly-real-rail.png`.
- **Decisions and why:**
  - **BUTTERFLY (ONE SHEET), reshaped, "from tool to tree".**
    - Killed the printed scanned live edge: fake, and the first idea.
    - The rear band is a real live-edge walnut rail. One straight joint at y 160 (153.5 sat on the back-row knob edges), one butterfly on axis x 138; the jacks are drilled in the wood.
    - Precision runs as a spectrum from front to back (draw: "Spectrum analysis"). Emotion: longing. The French cleat stays.
  - **CHAMBER (FOLD), pushed, "closed an organ case, open a console".**
    - The façade goes on the lid's back: the closed top, and what the friend across from you sees when it's standing. The speaker stays put.
    - 25 pipe lengths ∝ 2^(−n/12), laid out the organ builders' way (alternating from a centre tower). Draw: "Humanize something free of error".
    - Reverse pegs, naturals in body walnut. Brass screws as impost rivets. RANGE in feet, in serif. Emotion: joy.
  - **PIERCED, killed as a branch** (+55 mm for a gesture is the wrong way on cost and portability). Draws: "Disconnect from desire", shyness. The carry job moved into GROUND as a felt-lined finger pocket. A +32 mm slot middle path was tried and dropped.
  - **GROUND (either), "calm on top, loud underneath; the wedge is a horn".**
    - The speaker fires into a folded horn inside the wedge; mouth at the rear and sides. Draw: "Listen to the quiet voice". Horn gain UNVERIFIED.
    - Persimmon underside (exuberance), finger pocket, high-contrast type, a hood over the status light.
    - 12° over 180 ≈ 37 mm (systems' rough figure was 15–25); 8° ≈ 25.
  - **NEW: RAIN (ONE SHEET), "a pond after rain".**
    - The v1.1 rings with no outer radius. Fields meet at smooth Voronoi seams that draw the sections, so the grooves go. It keeps his two-finish rule.
    - Pegs become stepping stones that also ripple ("everything that breaks the surface ripples"). Legends sit on smooth "lily pads".
    - Mustard CUTOFF = a ginkgo leaf; pale wet-slate shell.
    - Draws: Riley, calm, under a tree in dappled light, mustard, "Don't be afraid of things because they're easy to do". Unused: stretcher, concertina, binoculars (TRAY held in reserve: a worn neck-strap tray).
  - **FREE/SYNC (all branches): in front of TIME, in the pot's dead zone.**
    - FOLD (≈133, d ≈71); ONE SHEET (≈128, y ≈133).
    - Fore-aft throw: toward the player = free, toward TIME = sync.
    - TIME gets two scales: inner ms ("20 ms", "2 s"); outer 9 division marks with only 1/16, 1/8, 1/4, 1/2 written, a dot for dotted, a triangle for triplet.
    - No mirror partner (the reason: echo is the only effect that cares about time).
    - The beside-TIME spot is ruled out by margins (7.05 to the break; 5.1 gap vs ≈ 12.2 needed). The behind-TIME spot collides with the ECHO heading and type fan.
    - d6 "jack wall" tested and rejected on B-J13 (not visible from the seat).
    - **My check was by margins only, in scratch (`/tmp`), not in the repo. Systems must run it with labels.**
- **Open questions:**
  - Owner: reversed key colours; pegs cost ONE SHEET ≈ +8 mm of width (the last peg is 0.65 from the 276 edge) and FOLD closed height.
  - Eng: horn gain; wood/PETG joint movement; engraved fill on wood-fill PLA; ring grooves ≥ 0.9 pitch face down.
  - Systems: SYNC label check; BUTTERFLY depth; GROUND rake; mouth/pocket layout.
  - Maker: the ring coupon now also decides RAIN (view it under a tree).
- **Director objections:** none yet on branches (first steer pending).
- **Next:** the director steers. Then build concepts with systems in `design/branches/concepts/<name>/`: real r5-based renders (A look + park scene, B 1:1), not sketches. RAIN first if chosen: its idea only shows in a render with raking light.

## S2: 120° stand + bend reads as a joystick (2026-11-13, new visual designer; owner: "oh do those first")
Context: the owner locked HUSH / ONE SHEET / FOLD-105 as v1 (`versions/v1/`, untouched by me). These two fixes were in progress at lock time. The sheets in `concepts/<concept>/` are the post-lock S2 redraws; they were locked as `versions/v1.1/` (owner, 2026-11-13).
- **Owner's words:** "the fold's angle should be a bit less steep so the front face catches more light. also i want the bend slider to be a joystick (is it a snap to center fader or what?...)".
- **Diagnosis:** the round-5 top views drew the bend as a black ball over a long dark slot on a pale rectangle (FOLD, ONE SHEET) or a vertical pill tag (HUSH). Seen from above, that's a fader cap in a track. The mechanism was always a spring-to-centre one-axis thumbstick (#2765 class); only the drawing was wrong.
- **What the stick is now (`joystick()` in r5.py; I kept the previous designer's version and fixed what surrounded it):**
  - Part: 3.2 stem standing clear of the plate; a flared 10 mm cap with a grip rim and a sunk dish (cap top z + 12.6, was 13.5, so clearances only improve). In 3/4 and front views it reads as a stem + cap, i.e. a stick.
  - Ink: a round gate ring (Ø 15 / 13.4) with two bezel pointers at 12 and 6 o'clock: the tilt axis, the watch-bezel idea. Two pointers, not four, say "one axis".
  - Slot: short (4 × 11.2, stem + throw), nearly hidden under the cap; just a sliver shows fore and aft.
  - **Surround, per concept (my change):** every rectangle/pill that framed the stick is now round:
    - FOLD: the pale square is a round well tone Ø 18.6 (flush, R4 ✓);
    - ONE SHEET: the Delrin gate plate is a round disc Ø 18.6, **and it's now centred on the stick** (the old square sat at x 15 while the stick is at 20: a pre-existing bug);
    - HUSH: the pill tag is a round tag Ø 18.6 with the usual label tongue. The ring and pointers print on the tag, because felt can't hold a fine mark (principle 4).
- **Sheet B callout (all three), "BEND IS A JOYSTICK, NOT A FADER" (`stick_callout()` in sheets_r5.py):** a plain-words answer to the owner's question, plus three 1:1 side views: pull = bend down, let go = springs to centre, push = bend up. Panel slot drawn 11.2 long. The text also says MOD is a knob that stays put. Parts lists gained a "Bend" line.
- **120° stand (systems rev 5.7), sheet E:** `Fold.STAND = 60`, `Fold.STAY_L = 44.4` (stowed groove d 30–74.4). The side elevation frame is widened to y D + 84 (the lid was cropped), and the stand shot's shadow footprint is D + 64.
  - The angle is now drawn as an arc from the base plane to the lid. Labels moved clear of the knuckle and stay.
  - The tip lands 59 behind the base, matching systems. Reach is ≈ 100 up / 80 behind PLAY (systems: 99 / 79). The lid's cream plate renders visibly lighter than in the 105° sheet, as the owner wanted.
- **Checkers:** fold_r5_check 0, flat_r5_check 0, layout_r4_check runs. Ink clearances hand-checked: ring to MOD ticks ≈ 5.5, BEND label to bottom pointer ≈ 2.0, HUSH stick tag to MOD tag 3.1.
- **Re-rendered (4961 × 3508):**
  - fold: A-105, B-105, C-105, D-105, E-105;
  - hush: A, B, C, D;
  - one-sheet: A, B, C, D.
  - C changed only in the footer (no stick in its sections). I opened every one, with 1:1 crops of the stick in B, D and E.
  - FOLD-113 is dropped and not re-rendered; its stale sheets and round 4's unsuffixed FOLD sheets are still in `fold/` (delete when convenient). `mock-E-standing-105-r5old.png` is kept for comparison.
### S2b: director fixes (same day)
- **Slot gone:** the panel opening under the stick is now a **round dark hole Ø 7.5** (stem 3.2 + its ± 2.1 sweep at panel level + clearance) in every view. The one-axis gate is under the panel. The callout's side views cut the panel at ± 3.75 to match. Checked in 1:1 crops of A (all three) and E.
- **FOLD MIDI IN drawn** (systems rev 5.6 does list it): base right end face, MIDI IN y 70, MIDI OUT y 80, USB-C y 90–99 (`FO_MIDI_IN_Y`, `FO_MIDI_Y`, `FO_USB_Y` in r5.py). Labelled under the open end view on D. Notes on C, D and E corrected. My earlier "rev 5.6 lists no MIDI IN" was wrong.
- **Re-rendered:** hush A, B, D; one-sheet A, B, D; fold A, B, C, D, E (all -105). Checkers 0.
- **Open:**
  1. #2765 cap size and height still UNVERIFIED in hand (drawn 10 / 12.6).
  2. `fold/`, `hush/` and `one-sheet/` `how-it-looks-and-feels.md` don't yet describe the gate ring / round surround or 120°. Add these when handoff starts.
  3. Whether the S2 sheets replace the locked v1 copies is the orchestrator's / owner's call.

## S1 label pass + pre-build fixes (2026-11-13, after the director's round-5 scores: HUSH / ONE SHEET / FOLD-105 at 9 pending S1)
- **Back row legends are short, under section headings:** ECHO over type · time, REVERB over decay · type (`LAB`, `FX_HEADS`, `fx_heads()` in r5.py). Headings sit above the type-name fan, centred on each pair. HUSH: pressed, 2.0, like MIXER. ONE SHEET: dark, 1.8. FOLD: Kalam 2.0, kept small so it clears the plate edge.
- **Clearances (all ≥ 1.5 mm label–label and label–knob, checked with a font-metric bbox script, then in 1:1 crops of every top view):**
  - outer type names raised: row 5.6 → 6.2 (Inter) / 6.5 (Kalam);
  - legends above toggles at 7.4 (was 8.4); OSC 3 CTL's legend now goes above its toggle too, mirroring VELOCITY;
  - switch-pair legends 6.2 from the toggle (was 5.6);
  - MIXER no longer crowds: the short labels leave ≈ 6 mm.
- **Depth change: HUSH 186 → 187** (+1 mm, owner's "grow the panel"), so the headings clear the rear band rule. ONE SHEET (180) and FOLD (108 / 129) are unchanged. FOLD-113's headings are 0.9 from the plate edge; it isn't offered, so I left it.
- **Pre-build fixes from systems (common 7.3, fold 5.6), drawn:**
  - **PARA toggle (MONO / PARA / PARA+4)** mirrors AFTERTOUCH. Flat: (TL + dx, 111.5). FOLD: PARA (93.9, d 26), AFTERTOUCH moved to (192.1, d 26), legends outward (the breaks sit inboard).
  - FOLD I/O: power switch + 6 jacks in the lid's far wall (x 66, then 90–215 at 25 pitch). USB-C (y 94) + TRS MIDI out (y 83) in the base's right end face. The lid end faces carry only the stays, so the stay FLAG on D and E is now marked resolved.
  - Daisy Seed is in the base, rear right (`Fold.fx_shield()` now returns base coordinates). It's gone from the lid plan and exploded view; a far-wall I/O board is drawn instead.
- **FLAG (systems): there's no room for PARA's legend in the flat concepts.** It's drawn bare, with a flag on sheet B. There's 2.3 mm between its nut and OSC 2's legend, and the break is 3 mm to its left. The three words need ≈ 15. It needs a new spot or fewer words.
- ~~Open (systems): rev 5.6 lists no MIDI IN~~: wrong, rev 5.6 adds it; drawn in S2b.
- **Perspective views (A):** in the 3/4 views, front knobs still hide parts of some back-row legends. Short labels reduce this but can't remove it, and the top and front views are exact.

## Where things stand (end of concept round 5, 2026-11-13; new visual designer this round)
- **Active: HUSH, FOLD (two variants), ONE SHEET.** TYPE CASE and HYMNAL are paused; UNDER GLASS was killed in round 2.
- **Round-5 sheets (300 dpi A3, tag "round 5")** are drawn to systems' round-5 final (common 7.1) + DRIFT (fold 5.4) + standing lid (fold 5.5). Every PNG was opened, and the back rows were checked in 1:1 crops.
  - `hush/` and `one-sheet/`: `mock-A-look`, `mock-B-real-size`, `mock-C-construction`, **`mock-D-front` (new)**. These overwrite round 4.
  - `fold/`: `mock-A-look-105/113`, `mock-B-real-size-105/113`, `mock-C-construction-105/113`, **`mock-D-front-105/113` (new)**, **`mock-E-standing-105/113` (new)**. Round 4's unsuffixed FOLD sheets are still in the folder; delete them once the director has seen round 5.
- **Sizes drawn:**
  - ONE SHEET 276 × 180 × 24, whites 26.5;
  - HUSH 290 × 187 × 25.5 (186 until the S1 pass);
  - FOLD-105 halves 286 × 108 (open 218 incl. the 2 mm seam);
  - FOLD-113 halves 286 × 129 (open 260); closed ≈ 50.1.
- **Docs rewritten:** `concepts/<hush|one-sheet|fold>/how-it-looks-and-feels.md` (round 5). `concepts/common-looks-and-feels.md` is still round 2/3, so treat it as superseded; it needs a refresh or a banner.

## Generator (round 5): `concepts/_mock-src/`
- `r5.py`: geometry and renders. Run `python3 r5.py [jobs]`; all ≈ 45 jobs take ≈ 8 min (`--test` for low-res; `python3 r5.py r5_fo105*` runs a prefix).
  - **The layout is read live from `fold_r5_check.py`** (the `F.play`, `F.v1`, `F.v2`, `F.fx` lists, breaks `F.vb_play`, `F.vb_fx`), shifted by dx (ONE SHEET −5, HUSH +2, FOLD 0). When systems edits the checker, re-render; no coordinates are duplicated. Only the section-name spots and the HUSH/FOLD text positions are hand-placed.
  - It reuses r4 primitives (`pebble`, `pg_layers`, `knob_black`, `halo`, `feltfill`, `woodfill`, `top4`, `shot4`).
  - New pieces:
    - `item5` (TYPE rotary kind "y" with `type_fan`; TAP kind "b" with `tap_cap` in 3 styles: peg / acryl / proof);
    - `keys_raised` (skirt option);
    - `one_sheet(edge)`, `hush(edge)`, `hush_body(edge)` (r 4 front via hull with side pucks at y 44);
    - `class Fold(v)`, which holds the variants' depths, lid face, exploded, `fx_shield()`, `stays()` and `model("stand")`;
    - **`shot_ortho()`**: exact-scale orthographic front / right-end elevations, cropped by magenta markers. The ortho distance must be (frame height + 20) / (2·tan 11.25°) with the camera centre on the object plane.
- `sheets_r5.py`: sheets A–E. Run `python3 sheets_r5.py [hush one-sheet fold105 fold113] [A B C D E]` (≈ 20 s).
- Round-4 code (`r4.py`, `sheets_r4.py`) is untouched.

## Decisions this round, and why
### All three
- **Layout:** systems' balanced, mirrored layout + DRIFT, drawn exactly (back row DRIFT | ECHO TYPE, TIME | REVERB DECAY, TYPE | VOLUME; TAP at the end of the PLAY row).
- **Type names:** the TYPE switches' detents fan over the top at −60 / −20 / +20 / +60°, and the four names sit in a straight row above, each over its detent. The inner two are lower and the outer two higher, so they never collide.
  - Echo: tape / bbd / clean / ping-pong. Reverb: plate / hall / spring / shimmer.
  - First try: a wide fan, −90…+90. It collided with break rules and neighbours.
- **TAP is made of the key material** in each concept (a maple peg in HUSH, white acrylic in ONE SHEET, a cream cap in a black bezel in FOLD), because it's played in rhythm like a key.
- **Tempo feedback (proposal, not in systems' spec):** the status light flashes the tempo 4 times after a tap. No second light (H7).
- **Key mechanism is drawn on every D sheet:** switch, stem, top, magnet / Hall, rest vs pressed. Stated plainly: a ≈ 3 mm button (HUSH: 2.5 to the felt collar), not a pivoting key.
- **Front views (D):** exact 1:1 orthographic renders from the same models. For the flat concepts: front A, front B, right-end A and B, then the edge and press.

### HUSH
- Edge A drawn as the hero (r 4 front, pegs y 13.5); B in the close-up and on D.
- **TYPE tags grow a bib** behind the knob that carries the type names, because felt can't hold a fine mark (principle 4).
- **The plinth outline was tried and burned:** it crossed MIXER, and the back row's rules already define the row.
- MIXER heading at (145, 134.6), size 2.0, in the clear strip between the tags.
- Random draw: "Look closely at the most embarrassing details and amplify them" + architecture (plinths). The awkward detail: pegs stand 6.5 mm proud, not 2–3, so the peg is leaned into, and TAP becomes a peg.

### ONE SHEET
- **Two finishes only:** smooth, plus rings round every rotary (r 7.75 → 9.25; CUTOFF 10.9 → 12.5), drawn at 1.1 pitch (2.5× coarse, labelled), with a true-scale swatch in the A inset.
- New principle 2: **"Still water, ripples where it turns"** (if it turns, it ripples; TAP, toggles, lights and the stick are smooth).
- Legends and names in one dark (#2e2924), because one swap means one colour.
- Random draw: "Water" + weaving. Neighbouring ripple fields never cross: 1.5 mm of smooth between them.
- Edge A as the hero; B on the A close-up and D.

### FOLD
- **Balance made visible (new principle 3, "Three columns and one axis"):**
  - the column rules x 101.5 / 184.5 run on both pickguards and line up across the seam;
  - everything single sits on x 143 (EMPHASIS, status, grille, the back-row centre break, the name lozenge);
  - a brass pin on the front rim and a tick on the far rim mark the axis.
- Signal map and row-end words burned. Random draw: "Bridges — build / burn" + sailing rigging (a boat's centreline is marked).
- **FOLD-113 is drawn honestly as failing the gap** (75.45 vs ≈ 60); every 113 sheet says so.
- **Digital module (flagged, purple dashed, sheet C plan + exploded):** the owner switched to a **Daisy Seed** (51 × 18, codec on board), so the FX shield is gone. Drawn under the lid's left far strip (x 18–69, d V2 + 12 … + 30), left of DRIFT.
  - Footprints [CALC]: Pico + shield ≈ 2,170 mm² vs Daisy ≈ 920, so the lid board gains area. My earlier "≈ 1,100 mm² short" finding is void. Eng confirms lid vs base.
- **MIDI OUT (owner):** added beside MIDI IN on every jack edge. HUSH: 8 ports at 19 pitch, x 76–209. ONE SHEET: 8 at 15.5 pitch, x 152–260.5. FOLD: lid right wall, 8 at 10 pitch, d 15–85.
- **AFTERTOUCH toggle (owner; systems hadn't placed it, so the placement is mine, pending systems):** VELOCITY's column. Flat concepts at y 111.5 between the voice rows (FILTER MOD / AFTERTOUCH / VELOCITY); FOLD at d 26, just behind FILTER MOD (mid-band would land on CONTOUR AMT closed). All checked against the checker's rules. Cost: one empty mirror slot. Labels: AFTERTOUCH to the left of its toggle; in the flat concepts VELOCITY and SOURCE labels go above their toggles.
- **Key lift:** `R5_KEY_LIFT` env var (default 0) raises keys / pegs for eng's possible 1–2 mm compliant aftertouch layer.
- **FLAG (systems): FOLD's right stay groove (d 30–82.4, z 2–10) runs through the lid-wall jacks (d 15–85, z ≈ 8).** Flagged on D and E. Fix options: jacks up the wall, I/O to the left wall, or relocate the right stay.
- **Standing lid (sheet E, both variants):** 105° on two brass stays (3 × 8 × 52.4), drawn from systems' rev 5.5.
  - My renders put the tip at y 161 (105) / 182 (113), ≈ 53 behind the base, with the stay at ≈ 68° to the table (systems: 162 / 183, 54, 65°; the difference is the rubber tip's height).
  - Stowed, the stays are brass lines on the lid's end faces in every view.
  - Finish proposal: brushed + waxed brass, domed rivet pin, 6 mm finger scoop.
- Knuckles narrowed to 10 wide (systems).

## Director (last scores: round 4) and status
- HUSH 9; FOLD 7 (blocker: mid-deck gap, now fixed in 105: 54.45 ✓); ONE SHEET 8 (blocker: the coupon, still unprinted; it's now two patches).
- The director hasn't scored round 5 yet.

## Findings to pass on
1. **Systems/eng:** the tempo flash on the status light (or no tempo feedback at all).
2. **Systems:** ONE SHEET's MIXER heading is crowded (≈ 3 mm to the REVERB DECAY label). Options: shorter labels (TIME / DECAY), or drop the VOICE headings.
3. **Eng:** FOLD Daisy Seed placement (above); standing-lid weights and boss strength.
3a. **Systems:** FOLD right stay vs the jacks (above).
3b. **Systems:** accept or re-place AFTERTOUCH (mirror cost); add it to the checkers. **Eng:** the FOLD-105 bridge under it; AT positions; key lift.
4. **Maker:** the HUSH corner blocking test now needs the r 4 front edge (option A).
5. Renders: OpenSCAD's light makes front faces and the standing lid's plate read darker than they are (the cream plate looks grey). The colours in the docs are the intended ones.

## Open questions
1. **Owner:** key edge A or B (HUSH, ONE SHEET; my lean is A for both); FOLD-105 vs 113 (recommend 105).
2. **Systems:** cream KN1250 on A-5518 round-shaft pots (HUSH, ONE SHEET), still unruled; FOLD's brass axis pin (drop it if it reads fussy).
3. Maker tests: the ONE SHEET coupon (smooth + rings); a pressed-felt offcut; a wood-fill walnut swatch; the HUSH corner (r 4 + r 12).
4. Refresh or retire `concepts/common-looks-and-feels.md`.

## What comes next
- The director scores round 5 (HUSH, ONE SHEET, FOLD-105; FOLD-113 is context).
- Eng confirms the Daisy placement; systems resolves the stay/jack clash. Redraw with `python3 r5.py r5_fo*` once the numbers change (stays: `Fold.lid()` and `Fold.stays()`; jacks: `Fold.lid()`).
- After the owner's pick: write "How it looks and feels" in `handoff.md`:
  - finishes;
  - type sizes (the docs list them);
  - every state with light colours and timings;
  - the knob and cap part list;
  - stay and finger-scoop details for FOLD.
