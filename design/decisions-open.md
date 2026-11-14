# Waiting on you

Decisions only you can make, newest first. The team keeps working around them; each answer unblocks the part named. When you answer in chat, the orchestrator records it in the owner record and removes it from here.

---

## 1. CATHEDRAL: approve it, or send it back
**Scored 9 by the director; passes every job.** Your 18:00 note is resolved: the lid now reads in signal order, synth → effects → out, top to bottom, with every switch under the group it changes.

- **Lid, top band:** oscillators 1 · 2 · 3 (spaced into groups; osc mod, osc 3 ctl, para under them), then the mixer in order (osc 1, 2, 3, noise/ext; source under it).
- **Lid, middle band:** filter contour (kbd, filt mod in their own "filter" column at the left edge) · speaker window · loudness contour (velocity, touch, decay under it). Mirrored across the centre line.
- **Lid, bottom band (by your hands):** echo (type, time with free/sync, repeats, mix, delay pan) · window · reverb (type, decay, mix) · **out** column at the right (dry pan, follow, volume); volume is the last control, above TAP.
- **Speaker:** Ø 46 mm round window on the centre line, 15 vertical slots, ≈ 75 % of the cone open, sealed back box; "big energy" on the plate beneath.
- **Base row:** symmetric: bend stick far left, TAP far right, CUTOFF centred.
- **Keys:** brass naturals, black-plated brass sharps (lead); all brass (alternate).
- **Closed thickness:** ≈ 55.2 mm, *only* with snap-in pots and the bend stick seated 3.6 mm lower (otherwise 56.7–58.8). Played-row knobs Ø 10 gold. Keeping the big knobs: ≈ 59.7 mm.
- **Hinge:** hidden pins; a 4 mm round bump shows at each back corner from the side.
- **Costs:** batteries move to the back of the base (board window, eng check); stand tip force ≈ 6.9 → 8.4 N.

![Lid top view, true scale: oscillators → mixer, filter contour · window · loudness contour, echo · window · reverb · out](branches/concepts/cathedral/img/cathedral-lid-signal-order-8.7px-per-mm.png)
![Standing](branches/concepts/cathedral/img/cathedral-nave-standing.jpg)
![Full top, lid and base](branches/concepts/cathedral/img/cathedral-nave-top-8.3px-per-mm.png)
![Closed, side: 55.2 mm](branches/concepts/cathedral/img/cathedral-nave-closed-side-14px-per-mm.png)
![Speaker window, front and section](branches/concepts/cathedral/img/cathedral-nave-speaker-window-20px-per-mm.png)
![Keys A (brass naturals) and C (all brass), ray-traced](branches/concepts/cathedral/img/cathedral-keys-brass-A-C.jpg)

**Also yours within it:** keys A or C; small knobs (55 mm) or big knobs (60 mm).

---

## 2. CATHEDRAL back opening, now there's no spine
Closed, there's a 22 × 266 mm opening along the back where the knobs inside show.

- **Leave it open, inside finished dark,** so the knob tops read as shadow. *Team recommends.*
- **Deal with it later** with a sleeve or case.

---

## 3. Buy-and-test (cheap, before building)
- **T1:** one pack of [Cherry Tree Toys 3/8" plugs](https://cherrytreetoys.com/3-8-mushroom-plugs/): measure head height and tenon on 5.
- **T2:** one hollow cast-brass key head on one switch: 20 presses slow and fast next to a wood plug; pass = no clack, wobble or sticking.

---

## 4. Line-out jacks (from the expert review)
**Unblocks:** the output circuit.
The mono-cable detection on LINE OUT can't work as drawn.

- **Two jacks, L/MONO and R:** the standard synth answer. A mono cable in L/MONO gets the full mix automatically, with no firmware. Adds one hole.
- **Keep one stereo jack and rework the detection circuit:** fewer holes, more parts, and it needs a bench test. A stereo cable into an audio interface can still go quiet.

Two jacks also give back a Daisy pin (pins are now at 30–31 of 31). *Team recommends two jacks.*

**Also:** should plugging into line out turn the speaker off? Most players expect it to, so the speaker doesn't feed back through a PA.

---

## 5. MIDI (see Features → MIDI for the full page)
- Should the dry pan stay on CC 10? DAWs send "pan = centre" on CC 10 every time a project opens, so the pan would jump to centre on its own. The team recommends moving it to an unused number.
- Should a DAW be able to automate the echo and reverb amounts? Those two knobs would get the MIDI dot and the "held by MIDI" light.
- Channel 1, or respond on any channel (omni)?
- Should the knobs ever send MIDI (off by default), or receive only?

---

## 6. Aftertouch switch label
**Unblocks:** the panel legend.
The pressure switch adds modulation amount: vibrato when OSC MOD is on, a filter wobble when FILTER MOD is on, or a brighter filter on FILT.

- **MOD / OFF / FILT:** says what it really does. *Team recommends.*
- **VIB / OFF / FILT:** your earlier word, but it's only vibrato when OSC MOD is on.

---

## 7. Filter keyboard tracking switch (KBD)
**Unblocks:** the KBD legend on the base.
The Model D reaches full tracking (both of its switches on). Ours is one 3-way switch, so it has three settings, not four.

- **off · 1/3 · 2/3:** as specified today. Full tracking isn't available.
- **off · 1/2 · full:** the firmware sets the amounts (the tracking voltage is already digital), so full is there for playing the filter as a tone. *Team recommends; eng to confirm.*
