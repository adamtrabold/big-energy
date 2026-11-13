# How it looks and feels: shared by all four concepts (visual), round 2

Read this first. Each concept's `how-it-looks-and-feels.md` only covers what's
different. This file **replaces** the round-1 version (282 mm, 276 × 70 panel,
printed/laser key ideas, "cutoff + glide" MIDI scope: all superseded).

**Checked against:**
- **owner.md**, all entries, newest included: "dont over index on OP1… it should
  feel good to use"; "id have to see mocks"; "i can make the labels myself or
  hand paint it"; "as silent as possible"; "finished instrument should be real
  parts"; "i dont want to steal a keybed"; "i want velocity"; "knobs midi cant
  control should not send midi and midi should not be able to flip switches";
  the bend/mod brainstorm (sticks, mini sticks, strips, faders, little dials).
- **eng/architecture-v2.md** §2 (11 MIDI-ownable controls), §4 (box ≈ 285 ×
  170–190 × ≤ 36), §4.1 (boards A–D), §4.2 (height), §5 (cost);
  **eng/key-sourcing.md** (buyable keys).
- **scores.md** R1–R9; `common-how-it-works.md` (systems, round 2).

## 0. Files

| What | File |
|---|---|
| Concept mocks (real proportions, 1 mm = 8–9 px) | `concepts/<slab|dock|motto|dish>/<c>-mock.png` |
| How each goes together (exploded side view) | `concepts/<c>/<c>-exploded.png` |
| Key menu | `concepts/keys/key-menu.png` |
| Controls menu (knobs, bend/mod spread, faders) | `concepts/controls/controls-menu.png` |
| Look sheet (SLAB in four looks) | `concepts/look-sheet.png` |
| Size sheet (every footprint over eng's box) | `concepts/size-sheet.png` |
| Generator | `concepts/_mockkit/`: `r2.py` (parts), `r2s_common.py`, `sheet_slab.py`, `sheet_dock.py`, `sheet_motto.py`, `sheet_dish.py`, `sheet_menus.py`, `sheet_look.py`; then `render.py <svg…>` (headless Chrome; Kalam in `~/.fonts`, Inter in system fonts) |

Round-1 files (`case/`, `archive-315mm/`, `compact*.py`) are superseded and kept
only for reference. **CASE is cut** (R2); SLAB replaces it.

## 1. Size (R1)

- Every concept is designed to feel, inside eng's box: **285 wide × 170–190
  deep × ≤ 36 thick** with pouch cells. OP-1 is a reference only.
- Exceptions, drawn honestly on the size sheet: DOCK is 300 × 237 played and
  ≈ 70 carried; DISH's base is 38 thick; SLAB and MOTTO carry at 46 with the
  lid on. Carried thickness includes the cap pocket (knobs stand 8 mm above the
  rim).

## 2. The panel (SLAB, DOCK; MOTTO is the same set bent to the curve)

- **280 × 100**, sunk 4 mm into the body. Bare PCB (mask + silk + ENIG), no
  assembly.
- **R1 minimums met:** 12 mm caps at ≥ 17 mm pitch (rotaries at 24); 26 mm
  hero; faders at 11 mm pitch, 28 mm travel; legends in Kalam at 3.6 mm
  (**cap height 2.66 mm**, Kalam capHeight 0.739 em); rotary numerals 3.4 mm
  (2.5 mm cap).
- **Order, left to right:** play (emphasis, amount, glide + on, decay, HOLD;
  cutoff hero; kbd 1/2 under it, because they act on cutoff) · control (tune,
  mod mix, osc mod, filt mod) · osc 1/2/3 (range, wave; freq 2/3; osc 3 ctl) ·
  mixer (osc 1–3 and ext/noise with their on-toggles beside; feedback, wh/pk,
  ext pad) · right block (volume, phones, TUNE button, status LED, Ø40 grille
  at the rear; the two contour fader groups below with the dotted gold
  envelope line).
- **Two tiers, as before:** the hero is the only thing in the signal colour;
  gold rules split sections.
- **New: the gold ring.** A thin gold ring printed around a cap (or a gold dot
  at the top of a fader slot) marks the **11 MIDI-ownable controls**: glide,
  tune, freq 2, freq 3, cutoff, filter A/D/S, loudness A/D/S (eng v2 §2).
  The owner learns at a glance which knobs MIDI can take. No ring = the knob
  is the sound: it never sends MIDI and MIDI can't move it. Switches are never
  ringed: MIDI can't flip them (owner.md, latest).
- **Speaker:** Ø40 driver under a Ø41 grille at the rear-right of the panel
  (SLAB, DOCK), ≥ 60 mm from the key switches. MOTTO's is the rose (rear-left);
  DISH's is in the well.

## 3. Keys and touched controls are bought parts

- Owner: real parts, nothing 3D-printed that you touch, no keybed taken from
  another product, velocity required. Eng: no bare mini keybed is sold to
  individuals. So every key is **a bought switch or pad per key**:

  | Concept | Key (key menu) | Bought | Made by a service |
  |---|---|---|---|
  | SLAB | K-B lever tops on Gateron low-profile Hall switches | switches, steel pivot rod, felt | piano-shaped tops (laser-cut acrylic or ply) |
  | DOCK | K-B with 80 mm tops | same | same |
  | MOTTO | K-B with walnut tops + bone acrylic sharps (reverse colours) | same | CNC walnut tops |
  | DISH | K-E maple button plugs on Hall switches, two rows | plugs, switches, blank caps (drilled) | none |

  The all-catalogue fallback for any straight-row concept is K-A (flat 1u caps
  on the same switches). **Open for the owner:** are service-cut key tops
  "real parts"? If not, SLAB/DOCK/MOTTO fall back to K-A.
- Knobs are bought (Davies-1900H-style skirted clone by default), fader caps
  are bought, bend/mod is two bought thumbwheel pots in the 13 mm zone by
  default (the controls menu lays out the alternatives). Glow pointers are
  luminous paint on the bought caps, not printed glow filament.
- The mocks draw the tops as piano shapes; from above, K-B looks like a
  keyboard. The exploded views show the switch under each lever.

## 4. Looks

| Concept | Look in its mock | Why |
|---|---|---|
| SLAB | Field: warm-grey felt-faced ply, black panel, orange hero | the plain, bag-friendly baseline |
| DOCK | Desk: smoked acrylic, black panel, green hero | studio object; edges glow |
| MOTTO | cork body, white panel, acid-chartreuse hero; walnut only outside the lid | round-2 draws (body: cork + white panel; "Use an unacceptable colour"); R4: off walnut-around-black |
| DISH | Proof: walnut base, cream panel, red hero | radio-telescope warmth; white dish reads as an instrument face |

- **Look sheet:** SLAB in Field, Proof, Desk and Cork (MOTTO's draw tried on
  the plain body) at real proportions, with each edge stack as cut.
- **Trade dress:** no end cheeks, no aluminium panel with dark legends, no
  script logo. Proof's walnut + big left knob is the closest to the original's
  posture: flagged on the sheet.

## 5. Legends and the owner's hand

- All legends, the wordmark ("untitled no.1"), grille patterns and paintings
  are placeholders. At 3.6 mm the owner's lettering will be scanned and
  reduced about 10–15×: bold strokes, no hairlines.
- Canvases: MOTTO's lid (285 × 195, raw birch), DISH's dish back (Ø112).

## 6. States (all concepts unless a concept overrides)

| State | Visual |
|---|---|
| asleep | everything dark |
| waking / tuning | status LED breathes in the signal colour (≈ 1.2 s) |
| ready | status LED steady |
| tune failed | status LED blinks the oscillator number (1–3) red, F for filter |
| MIDI activity | one 40 ms dip of the status LED per burst |
| MIDI owns a ringed control | per concept: SLAB one amber pip by HOLD (V-a); DOCK one amber flash, then nothing (V-b); MOTTO an amber pip beside each ringed control (V-c); DISH the amber ring around cutoff (V-d) |
| reclaim all (HOLD + TUNE) | pip(s)/ring fade out over 300 ms |
| hold latched | HOLD cap ring glows (light-pipe feasibility open, eng) |
| low battery | status LED pulses red every 10 s |
| charging / full | charge LED by the USB-C: amber / green |
| lights off | glow pointers on caps and fader caps, glow stripes on the sharps (pegs: dot on each C), lit pip/ring as above (see each LIGHTS OFF inset) |

## 7. Motion and feel

- **Knobs:** light, smooth, no detents. Rotaries: Lorlin-type 30° index, soft
  tick (the only intended mechanical sound on the panel).
- **Faders:** light drag; 7 mm caps keep the gold envelope line readable.
- **Keys:** a lever onto a linear Hall switch (K-B): ≈ 5 mm at the front, felt
  top stop, no click; velocity from travel time.
- **Opening = turning it on:** the breathing LED starts within 200 ms of the
  lid, module or dish moving.
