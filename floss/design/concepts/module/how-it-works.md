# floss module: how it works (shared by FALLBOARD, SPINE and CLOTH)

Status: **rev 1, 2026-11-22**, product designer (systems focus), concept round 2. Read with `../../jobs.md` (rev 3) and `floss/eng/module-r2.md`. There is one floss module, and every kit carries it unchanged. Each kit's `how-it-works.md` covers only the carry.

Marks: **[r2]** from `floss/eng/module-r2.md` · **[eng]** from `floss/eng/module.md` · **[calc]** my arithmetic · **PROPOSAL** systems design, not approved · **UNVERIFIED** not checked.

---

## 1. What the module is
**floss is a sound module.** It has 25 voices allocated from incoming MIDI, a bucket-brigade ensemble plus Daisy modes, echo and reverb, a 22.2 Wh battery, one sealed speaker and a panel. It's played by any class-compliant USB-MIDI keyboard on its USB-C host port, which powers the keyboard.
- It sits in every kit unchanged, held by two ¼"-20 inserts underneath (S4).
- It also works alone (at home, on a desk, on a tripod) and with no keyboard (from a computer, TRS, or a planted chord).

**The honest "analog voices" sentence (reworded for allocated voices):** floss's tones start in a microcontroller, one crystal-timed tone per voice, the way the 1974 Solina's started in divider chips. Everything that shapes them is analog: each voice's own keyer and envelope, the octave strands and their mix, the tone filter and the bucket-brigade ensemble. The Daisy modes, echo and reverb are digital, and each one can be switched off.

## 2. Size, ratio and outline (job 30, T4)
The owner, 13:29: "Ideally like the size of a sheet of paper length wise. But it also does not have to be a rectangle. It should be a thoughtful ratio base."

**What the parts need:**
- **Panel width:** **264 mm** of controls at the family pitch (§3) [calc].
- **Speaker:** a sealed Tectonic TEBM28C10-4B, Ø 55 × 24 mm deep, in ≥ 60–100 cm³ net, a box ≈ 62 × 75 × 27 mm inside [r2]. **No passive radiator** at this size (it doesn't earn its place [r2]); **ported** is the "more bass" option (an owner trade-off, §11).
- **Height:** body ≈ **32 mm**; **≈ 40 mm at the rim**, which stands over the knob tops (visual's sunk channel; [r2] §3.3). So the knobs never stand proud, which protects them in every kit.
- **Board and battery:** eng's BLOCK (270 × 100) fits board 200 × 80 + box 60 × 93, "tight" [r2].

**Where the speaker goes decides the depth.** Eng's BLOCK puts the box at one end. Here that would put a jamb's controls over the box, needing panel-mounted, hand-wired pots [r2 §3.2]. **PROPOSAL: the box sits on the axis, in the rear band, under the wordmark,** with its driver's Ø 56 clear column behind the rear row. That needs a rear band ≈ 57 deep inside, so the module is ≈ 105 deep. The board wraps the box: under the whole control band and either side of the box (≈ 13,400 + 2 × ≈ 5,000 mm² against eng's 16,000 mm² double-sided [calc]). **Eng to confirm the U-shaped board.**

**Ratio, PROPOSAL (a joint call with the visual designer): 2√2 : 1, two A-paper rectangles side by side.**
- **Size: 297 × 105 mm.** A4's long side by A6's short side, so it's two A6 sheets laid end to end.
- **Why this ratio and not another:**
  1. It comes from paper, which is the owner's own reference: an A-series sheet is √2 : 1, and two side by side make 2√2 : 1.
  2. **The axis divides the module into two √2 rectangles, one per half of the keyboard.** The split is the proportion: each jamb owns a √2 half, and the shimmer group sits on the line between them.
  3. It lands where the parts land: 264 of controls + 16.5 margins = 297; a speaker column on the axis = 105.
- **The Letter alternative: 279 × 98.6 (the same ratio).** The panel fits with 7.5 mm margins, but 98.6 deep can't hold the speaker on the axis. The box would go to one end, under a jamb, with hand-wired pots. Worse to build, so I'd take 297 × 105.
- **Outline: free, within these systems limits:**
  - the **front edge is straight** for ≥ 264 mm (both rows, the target rail and the host port line up along it);
  - the plan is **symmetric about the axis** (the owner reads off-centre in the middle as a mistake);
  - the **ends may round off** (organ jamb shoulders), provided the tab rows keep 34 mm;
  - the **rear band may curve or taper either side of the speaker box**;
  - **the body may be thinner than 32 everywhere except over the speaker**, which [r2] §3.1 allows: "a local bulge … a form decision, not engineering". The 2√2 plan with a raised speaker crown on the axis is one way to make it not a slab;
  - the **rear wall stays flat** for 8 ports and switches.

## 3. Panel map (two rows, family pitch)
**Rules carried over:**
- **Pitch:** 22 mm within a group, Ø 14.9 knobs, ≥ 7 mm between knob edges (family R2).
- **Group gaps:** each group gap adds 7 mm, with a 1 mm brass fret at its centre, so you can count groups by touch from either end.
- **Each end owns its half** (the jambs).
- **Coral on DEPTH, and the shimmer group on the exact centre line.**
- **Amounts in the front row, nearest the hand. Kinds, times and set-then-left controls in the rear row.**

**Regrouping (PROPOSAL):** ATTACK and RELEASE move from "touch" to "voice". They're the voice's envelope ranges; touch is now what your hand does on floss (HOLD) and what the guest keyboard's lean does (PRESSURE). This makes the groups **mirror about the axis**:
- left, from the outside in: jamb, a 1-column group, a 2-column group;
- right, from the outside in: jamb, a 1-column group, a 2-column group.

So the frets sit symmetrically.

x from the left end, axis at x = 148.5. Front row at y = 16 from the front edge, rear row at y = 40 [calc].

| Group | x (centre) | Front row (amounts, played) | Rear row (kinds, times) |
|---|---|---|---|
| **Jamb L** (left half) | 33.5 | OCTAVE L (5-step, −2 … +2) | strand tabs **low · main · high**, side by side (3 mini rockers, 34 wide) |
| *fret* | 54 | | |
| **Touch** | 68.5 | **HOLD** (latching, brass, larger) | **PRESSURE** (4-step: swell · drift · tone · shimmer) |
| *fret* | 83 | | |
| **Voice** | 97.5 | ATTACK | RELEASE |
| | 119.5 | TONE | DRIFT |
| *fret* | 134 | | |
| **Shimmer (axis)** | **148.5** | **DEPTH (coral)** | SHIMMER mode (4-step: analog · wide · glass · tape) |
| *fret* | 163 | | |
| **Echo** | 177.5 | ECHO (level and repeats) | TIME |
| | 199.5 | **TAP** (its lit ring is the status light) | FREE / SYNC (toggle) |
| *fret* | 214 | | |
| **Out** | 228.5 | VOLUME | REVERB (decay grows with amount) |
| *fret* | 243 | | |
| **Jamb R** (right half) | 263.5 | OCTAVE R | strand tabs **low · main · high** |

- **Width check [calc]:**
  - slots: two 34 mm jambs + seven 22 mm columns = 222;
  - six group gaps × 7 = 42;
  - total 264, plus 16.5 margins = **297**.
  - Frets mirror: 54 ↔ 243, 83 ↔ 214, 134 ↔ 163.
- **Count:** 13 round controls (OCTAVE ×2, PRESSURE and SHIMMER stepped; ATTACK, RELEASE, TONE, DRIFT, DEPTH, ECHO, TIME, REVERB, VOLUME pots), plus HOLD, TAP, FREE / SYNC, 6 tabs and 2 lights. That's the one voice from jam turn 4, accepted in turn 6.
- **Reading it, eyes closed:** from the left end, the jamb (a stepped knob in front of three tabs), a fret, HOLD, a fret, the voice's four knobs, a fret, the coral centre. The right side mirrors it. In signal order left to right: touch → voice → shimmer → echo → out.
- **Rear row:** the tabs (15 deep, centred at y 40) span y 32.5–47.5, 9 mm behind OCTAVE's knob edge.
- **The rear band (y ≈ 48–105)** is the speaker's: the sealed box on the axis under a grille, with the **wordmark centred above the shimmer column** (visual). The band either side of the box is board, under a plain deck. No controls go there; it's not spare space.
- **Knob sizes** (visual's call): the front row at Ø 14.9. The rear row may step down for the kinds (PRESSURE, SHIMMER, FREE / SYNC). RELEASE, DRIFT, TIME and REVERB are amounts that sit in the rear only because they're set-then-left, so they keep the front row's size.

## 4. Front face (the edge facing the keyboard)
Centred on the axis:
- **Target rail:** a graduated brass strip along the top front edge, ≥ 264 mm. The **brass target** slides on it.
  - Engraved beside it: **"keep the keyboard at its home octave"**. Every kit then carries the line on the module itself.
  - Range ± 132 mm about the axis. On any centred slim keyboard, B3 | C4 falls a little left of the keyboard's centre (after 7 of 15 white keys on a C-to-C 25-key keyboard [calc]), well inside the range.
- **USB-C host port** (S2), on the axis, low on the face. Cold socket: VBUS goes on only when a keyboard is detected; current-limited at ≈ 550–600 mA [r2].
- **Port light**, beside the host port.
- **The two USB-C sockets are far apart:** the host on the front face, charging and computer on the rear wall. [r2] asks designers to separate and mark them. A charger in the wrong socket is safe [r2] and flashes the port light.
- **Why floss can't know which key is which**, the one line for the owner: a USB keyboard sends only note numbers, and its octave button changes the numbers without telling floss. So floss splits at a fixed number, and the brass target shows where that number sits on today's keyboard.

## 5. Rear wall and underside
- **Rear wall:** POWER (the one switch, recessed slide, can't switch on in a bag) · USB-C (charging and computer MIDI) · PHONES · LINE · MIDI IN · MIDI OUT (TRS) · TUNE (trim, ±50 c) · MIDI SPLIT (slide).
- **Underside:** **two ¼"-20 brass threaded inserts** (S4), PROPOSAL **160 mm apart at x = 68.5 and 228.5, y ≈ 30**, under the control band (clear of the speaker box on the axis); four feet.
  - Eng to check the bosses against the battery and board.
  - The kits hold the module by these inserts with thumbscrews; a tripod uses one.

## 6. The voice (from jam turn 4, accepted by the director in turn 6)
| | Behaviour |
|---|---|
| **Voices** | 25, **in fixed pools: 1–12 serve the left half, 13–25 the right.** Stealing (oldest first) happens within a half. A 25-key keyboard played live never steals. Pools keep the strand gates (6 lines) and the half buses [eng §4]. Eng to confirm. |
| **Split** | Fixed at B3 \| C4 (note 59 \| 60). OCTAVE L and R add −2 … +2 octaves to each side. Equal = one keyboard. A held note keeps its pitch through an octave change. |
| **Velocity** | Speed: soft bows in slowly, hard speaks at once, inside ATTACK's range. Loudness doesn't change (a firmware option, with no control). |
| **Release velocity** | Sets the tail inside RELEASE's range (out to ≈ 30 s) when the keyboard sends it; otherwise RELEASE's value. |
| **Strands** | Up to three per note: octave below · at pitch · octave above. Three tabs per half. **All off = that half silent:** a mute, shown by the tabs. |
| **DRIFT** | Each voice wanders on its own slow random walk: 0 = steady, full ≈ ±25 c (PROPOSAL). |
| **Lean (PRESSURE)** | **swell** (that note's level grows), **drift** (that note's wander widens and its rate rises, so a full lean becomes a vibrato at ≈ 5–6 Hz; a planted note keeps the drift it was planted with), **tone** and **shimmer** (whole instrument, following the hardest lean). A lean only adds to the knob and returns exactly to it. |
| **Lean source** | Poly aftertouch / MPE → per note; channel pressure → every note; **CC1** (mod wheel, strip or button) → every note; nothing → velocity still works. floss uses the best source the keyboard sends; the panel doesn't change. |
| **Bend** | ±2 semitones; per note with MPE. |
| **HOLD** | **Plant and tend.** While on, every note played joins the held set. A re-strike pulls that note out; the re-strike's velocity sets its fade (soft = long). Off: all fade on their tails. **Held notes survive the keyboard** (unplug, swap, hand-over). |
| **HOLD's scope** (owner proposal) | Octaves equal → plants everything. Octaves different (a split) → plants the left half; the right half plays live. Notes already planted stay when the scope changes. |
| **CC64** | Ordinary sustain on every note, separate from HOLD. |
| **Breath** | The sum grows with about √(voices sounding), recovering over ≈ 200 ms; no control. |
| **Shimmer** | **analog** (3 × V3207 bucket-brigade, LFOs ≈ 1 Hz and ≈ 6 Hz at 0 / 120 / 240° [eng]) · three Daisy modes (working names wide · glass · tape). DEPTH 0 = dry. Paths spread left / centre / right on phones and line; the speaker gets the mono sum, high-passed at ≈ 100 Hz [r2]. |
| **Echo, reverb** | ECHO raises level and repeats together. TIME: milliseconds in FREE, a note division in SYNC (tempo from MIDI clock if present, otherwise TAP). REVERB: amount, with decay growing with it. No clicks when the clock starts, stops or drops out. |
| **MIDI** | Big Energy's rules. MIDI SPLIT on: left half on channel 1, right on 2, in and out. Velocity, pressure and release velocity go out. Panel settings follow the family CC map (S6) with jump-on-move takeover. |
| **Keyboard power** | 5 V from a cold socket, current-limited at ≈ 550–600 mA, only while floss is on [r2]. |

## 7. Lights
| Light | Where | Meanings |
|---|---|---|
| **Status** | TAP's lit ring | steady = fine · slow pulse = charging · flash = low battery · (TAP's tempo blink in SYNC from TAP, as on Big Energy) |
| **Port** | front face, beside the host port | off = nothing connected · steady = keyboard connected and powered · **a short blink per note received** · fast flash = fault (too much current, or something wrong in the host socket) |

- **Open:** TAP's ring then carries the status meanings plus a tempo blink, as on Big Energy's CATHEDRAL. If the director finds that too many, the status light moves to a small dot on the axis, under the wordmark.

## 8. States
| State | What happens | What you see / hear |
|---|---|---|
| Off | nothing; the host socket is cold | all dark |
| On, no keyboard | silent, ready; plays from USB-C or TRS; the host socket stays cold | status steady; port off |
| Keyboard plugged in | detected → VBUS on → enumerated | port steady |
| Playing | notes sound | port blinks per note |
| **Silent, keyboard connected** (job 29) | — | port steady, **no blink** on a key → notes aren't arriving (dead keyboard or charge-only cable). Blinks but silent → VOLUME, all tabs off in a half, phones plugged in |
| Port light off with a keyboard plugged in | a non-compliant cable or keyboard not detected | use the **C-to-A adapter** with the keyboard's own cable [r2]; firmware's always-on fallback is in reserve (owner trade-off) |
| Keyboard draws too much / charger in the host socket | power cut; floss keeps running | port flashes fast |
| Unplugged mid-chord | unheld notes fade on their tails; **held notes keep sounding** | port off |
| HOLD on, notes planted, keyboard gone | the drone continues; every knob still works | HOLD lit; port off |
| HOLD on, a half full (12 or 13 planted) | the next note in that half replaces its oldest | — |
| A half with all tabs off | silent in and out (with MIDI SPLIT) | the tabs show it |
| Lean source = nothing | PRESSURE has no effect; velocity still works | — |
| SYNC with no clock and no tap | echo runs at the last tempo (120 BPM at power-on, PROPOSAL) | — |
| Charging while playing | normal | status slow pulse |
| Low battery | warning before it stops (eng sets the threshold) | status flashing |
| Headphones in | speaker mutes | — |
| Computer and keyboard together | notes merge if host and device work together (unverified [r2]); otherwise TRS to the computer | — |
| Big home keyboard (49–61 keys) | plays if it draws ≤ ≈ 500 mA; note 60 is near its middle (UNVERIFIED per model); a half can steal past 12 / 13 | — |

## 9. The family interfaces this module meets (job 28)
| | Interface | floss's value |
|---|---|---|
| S1 | keyboard envelope the carry takes | 325–388 × 83–135 × 11–16 mm, ≤ 0.6 kg [eng] (the carry's job) |
| S2 | host port | USB-C, cold socket, ≈ 550–600 mA, front face on the axis [r2] |
| S3 | cable | **0.3–0.5 m** [r2]: C-to-C for USB-C keyboards; otherwise the keyboard's own cable on **one C-plug-to-A-receptacle adapter**, which every kit carries in its pocket [r2]. A coiled 0.3 → 1 m cable for sharing is an optional extra (product UNVERIFIED) |
| S4 | attachment | two ¼"-20 inserts, 160 mm apart (PROPOSAL) |
| S5 | plug behaviour | §8: any order, notes release on unplug, held notes survive, port light, cold socket, keyboard powered only while on |
| S6 | CC map | CC64 sustain, CC1 lean fallback, CC74 tone, CC11 expression, bend ±2; the full list goes in the spec |
| S7 | split rule | fixed note B3 \| C4 + target rail and the engraved line |

- **What Big Energy and port-a-poly reuse unchanged:** S1–S7; the target rail and target; the port light's meanings; the end-block bed and its brass scale (carry parts); the cable and adapter.
- **Their module size is their own** (owner, 13:25).

## 10. Coverage: the jobs the module answers in every kit
| Job | Where |
|---|---|
| 1 strings anywhere | §1, §6 |
| 2 one cable, USB-C, any keyboard | §4, §6, §9 S2 / S3 (adapter) |
| 4 every note | §6 voices (pools) |
| 5 split and octaves | §3 jambs, §6 |
| 6 where the split lands | §4 |
| 7 velocity | §6 |
| 8 lean, selectable | §3, §6 |
| 9 no pressure | §6 lean source |
| 10 extras | §6 |
| 11 colour per half | §3 tabs, §6 |
| 12 shimmer | §3 axis, §6 |
| 13 echo, reverb, tempo | §3, §6 |
| 14 hold | §6 |
| 15 speaker / phones | §2, §5, §8 |
| 16 computer / other keyboard | §5, §8 |
| 17 MIDI out | §6 |
| 18 read the state | §3, §4, §7 |
| 19 one switch | §5, §8 |
| 21 many vs one | §6 breath |
| 22 in tune | §5 TUNE; crystal tones [eng] |
| 26 proven parts; fix | [r2] parts all published; host port and battery reachable (eng's layout) |
| 29 why silent | §7, §8 |
| 30 paper length, ratio, shape | §2 |
| 3, 20, 23, 24, 25, 27, 28 | partly §9; the rest in each kit's file |

## 11. Open, and owner trade-offs from `module-r2.md`
1. **Speaker loading (owner trade-off):** sealed (f3 ≈ 255 Hz, robust, smallest), ported (f3 ≈ 105–135 Hz, +6 dB at 100 Hz, port noise at loud bass unmodelled), or passive radiator, which **eng says doesn't earn its place at this size**. That last one reverses the owner's "passive radiator would be cool". **The module is drawn sealed.** A ported box needs ≥ 130 cm³ and a folded port [r2], which the axis box may not take. Eng to check.
2. **Body 32 / 40 with the rim** (vs the 23–25 he saw before): an owner trade-off [r2 trade-off 2]. A thinner body with a speaker crown is the form option (§2).
3. **The U-shaped board around an axis speaker box:** eng to confirm (§2).
4. **Weight:** the module is ≈ 0.67–0.93 kg (BLOCK-class [r2]). Kit totals are in each kit's file. **No kit meets T5 with an Xkey 25** [r2]: an owner trade-off.
5. Fixed voice pools 12 / 13; insert bosses; TAP's ring carrying status plus tempo.
