# floss module: how it works (shared by FALLBOARD, SPINE and CLOTH)

Status: **rev 2, 2026-11-22**, product designer (systems focus), concept round 2, second systems turn. Brought to the director's R1–R4 (new-director steer 1) and to the owner's 14:08 principle that **the case is entirely 3D printed** (PRINCIPLES §7). Read with `../../jobs.md` (rev 3.1), `how-it-looks-and-feels.md` (visual) and `floss/eng/module-r2.md`. There is one floss module, and every kit carries it unchanged. Each kit's `how-it-works.md` covers only the carry.

Marks: **[r2]** from `floss/eng/module-r2.md` · **[eng]** from `floss/eng/module.md` · **[calc]** my arithmetic · **PROPOSAL** systems design, not approved · **UNVERIFIED** not checked · **ENG** needs engineering to confirm (all collected in §11).

---

## 1. What the module is
**floss is a sound module.** It has 25 voices allocated from incoming MIDI, a bucket-brigade ensemble plus Daisy modes, echo and reverb, a 22.2 Wh battery, one sealed speaker and a panel. It's played by any class-compliant USB-MIDI keyboard on its USB-C host port, which powers the keyboard.
- It sits in every kit unchanged, held by two ¼"-20 threaded inserts underneath (S4).
- It also works alone (at home, on a desk, on a tripod) and with no keyboard (from a computer, TRS, or a planted chord).
- **The case is printed** (owner 14:08): shell, deck, crown, rail, target and dividers. Bought parts are the electronics, knobs, switches, jacks, the threaded inserts and fasteners. Printing by an outside service is fine (owner 2026-11-13).

**The honest "analog voices" sentence:** floss's tones start in a microcontroller, one crystal-timed tone per voice, the way the 1974 Solina's started in divider chips. Everything that shapes them is analog: each voice's own keyer and envelope, the octave strands and their mix, the tone filter and the bucket-brigade ensemble. The Daisy modes, echo and reverb are digital, and each one can be switched off. (The family goal is analog-first, with digital used where it serves: owner 14:06.)

## 2. Size, ratio and outline (job 30, T4)
The owner: "It just needs to be portable and make sense and be harmonious" (13:51); "it also does not have to be a rectangle. It should be a thoughtful ratio base" (13:29). PRINCIPLES §2: proportions come from a deliberate ratio derived from the device itself.

**280 × 105 × 35 mm. Each size comes from a part; the ratio then tunes them** (visual's derivation, adopted):

| Need | From | Gives |
|---|---|---|
| Panel width | the map (§3): two 34 mm jambs + seven 22 mm columns + six 7 mm group gaps = 264 | ≥ 264 + an end margin |
| End margin | the jamb's tabs clear the rim (4) and a fingertip (4) | 8 each end → **280** |
| Depth on the axis | the speaker crown: the driver's Ø 56 column behind the rear row [r2] | **105** (conditional: §2.2) |
| Depth at the ends | jambs only: front row + tabs to y 47.5 + rim | ≥ 56 → **70** |
| Height | the driver needs a 32 mm body [r2]; the knobs sit inside the rim | 32 + 3 → **35** (conditional: §2.1) |

**The ratio:** it falls on one **35 mm unit, 8 : 3 : 1**. Each half of the plan (140 × 105) is 4 : 3, one per keyboard half, with the split axis between them. Centre depth : end depth = 105 : 70 = 3 : 2. One sentence for the owner: "the parts set 280 × 105 × 35; it happens to fall on one 35 mm unit, 8 : 3 : 1, a fourth for each half."

**The hull outline (plan):**
- **Front edge:** straight, full length. It faces the keyboard and carries the target rail, the host port and the port light. Corners r 10.
- **Ends:** straight, 70 deep. You pick it up by them.
- **Rear:** one fair arc from 70 at each end to 105 on the axis (R ≈ 297.5 [calc]), deep only where the speaker is.
- **Two flat port facets** on the arc, either side of the crown (§5).
- It's symmetric about the axis (PRINCIPLES §6).

**Section:** a sunk deck, a rim at 35 all round, and a speaker crown 70 wide (x 105–175) on the axis, its top level with the rim and its front raked from the deck up to the top. The wordmark sits on the crown's rear face, between the facets (visual, director R4). The deck carries nothing but controls and their words.

### 2.1 Condition: the height stays 35 only if the knob allows it (R1 condition 2), ENG
Deck height = rim 35 − 1 clearance − knob height − ≈ 1 seat. Eng's flat stack needs the deck top at ≥ 23.5 (floor 2.4 + cells 7.5 + parts 3 + board 1.6 + top parts 6.5 + deck 2.5 [r2 §3]) [calc]:

| Knob (published height) | Deck can be at most | Holds 35? |
|---|---|---|
| Family 18T push-on, 14.5 × 13.5 (Tayda; family file `design/concepts/common-how-it-works.md`) | 19.5 | **No.** Needs a rim at ≈ 41 |
| KN1250, 14.86 × 10.45 (Tayda; `eng/round4-answers.md`). Round-bore set-screw, so it needs round-shaft pots; the family moved off it | 22.6 | **No, by ≈ 1 mm.** Needs a rim at ≈ 36.5 |
| Tayda aluminium Ø 10 × 8, 6 mm 18T (Big Energy CATHEDRAL's low knobs) | **25** | **Yes:** deck at 25, 1.5 mm to spare |

- **So "knob tops at 34, deck at 26" doesn't hold with any knob the family has named at Ø 14.9.** Eng (or visual) should look for a Ø 14–15 knob ≤ 8–9 mm tall with a published height. If there isn't one, the choice is: **Ø 10 × 8 knobs and 35 stays**, or **Ø 14.9 knobs and the height becomes ≈ 41**, with the ratio restated. We don't fake 35 (director R1).
- **Systems' preference: Ø 10 × 8**, unless a low Ø 14.9 part turns up. It's the shared-universe part (CATHEDRAL already plays a row of them), it keeps 35, and it solves §2.2. The cost is a smaller knob under the hand. Director and owner decide.

### 2.2 Condition: finger room behind the crown vs the driver (R1 condition 3), ENG
The driver's Ø 55 frame has to fit under the crown's top, from the crown foot back to the rear wall's inside (y 102.5 on the axis). The foot must sit ≥ 5 mm behind the rear-row knobs [calc]:

| Rows | Rear knob's rear edge | Crown foot ≥ | Driver needs to y | Fits 105? |
|---|---|---|---|---|
| Ø 14.9, rows at y 16 / 40 (as drawn) | 47.5 | 52.5 | 107.5 + wall | **No** (≈ 110 deep) |
| Ø 14.9, rows pulled to y 14 / 35.9 (7 mm between rows, the family minimum) | 43.4 | 48.4 | 103.4 + wall | **No, by ≈ 1 mm** |
| **Ø 10 × 8, rows at y 14 / 31** | 36 | 41 | 96 + wall | **Yes, 6.5 mm spare** |

- Even visual's drawn crown (foot at y 47) puts the frame under the knobs' edge. Visual noted that "its Ø 55 frame is about the crown's flat depth."
- **With Ø 14.9 knobs, 105 can't give 5 mm of finger room.** The module goes to ≈ 108–110 deep (and the ratio is restated), or the knobs shrink.
- A tilted driver doesn't rescue it: the crown top is only 50 mm deep behind a 52.5 foot [calc].
- **With Ø 10 × 8 knobs, 280 × 105 × 35 holds on both counts.** That's why it's systems' preference in §2.1.
- **Ø 10 knobs and the 22 mm pitch:** Ø 10 would satisfy the ≥ 7 mm rule at a 17 mm pitch, which would narrow the panel. I keep the family's 22 mm grid (R2, as on CATHEDRAL), because it's a family rule for the hand, not a knob-size rule. So 264 still comes from the family grid. **Director to confirm**, because otherwise the width reopens.

**The positions below are drawn for Ø 14.9 at y 16 / 40 (the current sheet).** If §2.1 / §2.2 go to Ø 10 × 8, the rows move to y 14 / 31, the tabs to y 23.5–38.5 and the crown foot to y 41. No x position changes.

### 2.3 Condition: the cells beside the crown, ENG
The two cells (50 × 60 × 7.5 [r2]) go under the board, either side of the sealed box: **x 49–109 and 171–231, y 38–88** [calc].
- The hull's inner wall at x 49 is at y 88.2, so the margin is ≈ 0.
- The insert bosses (x 60 / 220, y 30, Ø ≈ 14) clear the cells by ≈ 1 mm.
- Eng to confirm, along with the U-shaped board around the box.

## 3. Panel map (two rows, family pitch)
**Rules carried over:**
- **Pitch:** 22 mm within a group; ≥ 7 mm between knob edges (family R2).
- **Group gaps:** each adds 7 mm, with a **flush divider** at its centre (§3.1).
- **Each end owns its half** (the jambs).
- **Coral on DEPTH, and the shimmer group on the exact centre line.**
- **Amounts in the front row, nearest the hand. Kinds, times and set-then-left controls in the rear row.**

The groups **mirror about the axis**: jamb, a 1-column group, a 2-column group on each side. ATTACK and RELEASE sit in voice (rev 1's regrouping, unchanged).

x from the left end, **axis at x = 140**. Front row at y = 16, rear row at y = 40 (see §2.2) [calc].

| Group | x (centre) | Front row (amounts, played) | Rear row (kinds, times) |
|---|---|---|---|
| **Jamb L** (left half) | 25 | OCTAVE L (5-step, −2 … +2) | strand tabs **low · main · high**, side by side (3 mini rockers, 34 wide) |
| *divider* | 45.5 | | |
| **Touch** | 60 | **HOLD** (latching, larger) | **PRESSURE** (4-step: swell · drift · tone · shimmer) |
| *divider* | 74.5 | | |
| **Voice** | 89 | ATTACK | RELEASE |
| | 111 | TONE | DRIFT |
| *divider* | 125.5 | | |
| **Shimmer (axis)** | **140** | **DEPTH (coral)** | SHIMMER mode (4-step: analog · wide · glass · tape) |
| *divider* | 154.5 | | |
| **Echo** | 169 | ECHO (level and repeats) | TIME |
| | 191 | **TAP** (its lit ring is the status light, §7) | FREE / SYNC (toggle) |
| *divider* | 205.5 | | |
| **Out** | 220 | VOLUME | REVERB (decay grows with amount) |
| *divider* | 234.5 | | |
| **Jamb R** (right half) | 255 | OCTAVE R | strand tabs **low · main · high** |

- **Width check [calc]:** two 34 mm jambs + seven 22 mm columns = 222; six gaps × 7 = 42; total 264 + 2 × 8 = **280**. The dividers mirror: 45.5 ↔ 234.5, 74.5 ↔ 205.5, 125.5 ↔ 154.5.
- **Count:** 13 round controls (OCTAVE ×2, PRESSURE and SHIMMER stepped; ATTACK, RELEASE, TONE, DRIFT, DEPTH, ECHO, TIME, REVERB, VOLUME pots), plus HOLD, TAP, FREE / SYNC, 6 tabs and 2 lights.
- **Reading it, eyes closed:** from the left end, a stepped knob in front of three tabs, a gap, HOLD, a gap, the voice's four knobs, a gap, the coral centre. The right side mirrors it. Signal order left to right: touch → voice → shimmer → echo → out (PRINCIPLES §6).
- **Rear row:** the tabs (15 deep, centred at y 40) span y 32.5–47.5. They fit the 70 mm ends: 47.5 + rim < 70.
- **Behind the rear row:** the crown on the axis (the speaker); either side of it, a plain deck over the board and cells. No controls go there.
- **Knob sizes:** §2.1 decides. If Ø 14.9 survives, the rear row's kinds (PRESSURE, SHIMMER, FREE / SYNC) step down to Ø 10 (visual).

### 3.1 Dividers: flush and printed (director R2 + owner 14:08)
- **Flush with the deck.** Nothing stands up between knobs (PRINCIPLES §6: dividers mustn't get in the hands' way).
- **You find the groups by touch** from the 7 mm wider gap, and by a change you can feel at the divider line.
- **Printed, not brass.** The look is visual's call. Three ways to make it, each a standard printing method (job 26):
  1. **a shallow groove** printed into the deck (one material; you feel the edge);
  2. **a contrasting inlay printed in place**, using a multi-material printer, level with the deck;
  3. **a separately printed strip pressed into a printed slot**, level with the deck.
  - None needs sanding, machining or measuring.

## 4. Front face (the edge facing the keyboard)
Centred on the axis:
- **Target rail:** a graduated printed rail along the top front edge, ≥ 264 mm, with a **printed target** that slides on it. The graduation is printed (every 10 mm, with a longer centre mark).
  - Range ± 132 mm about the axis. On any centred slim keyboard, B3 | C4 falls a little left of the keyboard's centre (after 7 of 15 white keys on a C-to-C 25-key keyboard [calc]), well inside the range.
  - **No sentence on the module** (director R4). "Keep the keyboard at its home octave" goes on the 1:1 card in each kit's pocket and on the site.
- **USB-C host port** (S2), on the axis, low on the face. Cold socket: VBUS goes on only when a keyboard is detected, current-limited at ≈ 550–600 mA [r2].
- **Port light**, beside the host port.
- **The two USB-C sockets are a body apart:** host on the front face, charging and computer on the rear facet. A charger in the wrong socket is safe [r2] and flashes the port light.
- **Why floss can't know which key is which**, the one line for the owner (it goes on the card and the site): a USB keyboard sends only note numbers, and its octave button changes the numbers without telling floss. So floss splits at a fixed number, and the target shows where that number sits on today's keyboard.

## 5. Rear facets and underside
- **Two flat port facets on the arc**, either side of the crown (visual §2):
  - **plan-left, set once:** POWER (the one switch, a recessed slide, so it can't switch on in a bag) · USB-C (charging and computer MIDI) · TUNE (trim, ±50 c) · MIDI SPLIT (slide);
  - **plan-right, sound and MIDI:** PHONES · LINE · MIDI IN · MIDI OUT (TRS).
  - The rigid kits put a window in their rear wall in line with each facet, so plugs pass.
- **Underside:** **two ¼"-20 threaded inserts** (S4), **160 mm apart at x = 60 and 220, y = 30**, under the control band and clear of the crown; four feet.
  - In a printed shell these are heat-set (or press-in) inserts: fastener hardware, not a finish (product with ¼"-20 thread UNVERIFIED; ENG).
  - The rigid kits hold the module by these inserts with thumbscrews; a tripod uses one.

## 6. The voice (from jam turn 4, accepted in turn 6; unchanged)
| | Behaviour |
|---|---|
| **Voices** | 25, **in fixed pools: 1–12 serve the left half, 13–25 the right.** Stealing (oldest first) happens within a half. A 25-key keyboard played live never steals. Eng to confirm. |
| **Split** | Fixed at B3 \| C4 (note 59 \| 60). OCTAVE L and R add −2 … +2 octaves to each side. Equal = one keyboard. A held note keeps its pitch through an octave change. |
| **Velocity** | Speed: soft bows in slowly, hard speaks at once, inside ATTACK's range. Loudness doesn't change (a firmware option, with no control). |
| **Release velocity** | Sets the tail inside RELEASE's range (out to ≈ 30 s) when the keyboard sends it; otherwise RELEASE's value. |
| **Strands** | Up to three per note: octave below · at pitch · octave above. Three tabs per half. **All off = that half silent:** a mute, shown by the tabs. |
| **DRIFT** | Each voice wanders on its own slow random walk: 0 = steady, full ≈ ±25 c (PROPOSAL). |
| **Lean (PRESSURE)** | **swell** (that note's level grows), **drift** (that note's wander widens and speeds up, so a full lean becomes a ≈ 5–6 Hz vibrato; a planted note keeps the drift it was planted with), **tone** and **shimmer** (whole instrument, following the hardest lean). A lean only adds to the knob and returns exactly to it. |
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

## 7. Lights (two; director R3)
| Light | Where | Meanings |
|---|---|---|
| **Status** | **TAP's lit ring** (as on Big Energy's CATHEDRAL; shared universe) | steady = on and fine · slow pulse = charging · fast flash = low battery · tempo blink = TAP's tempo (only in SYNC with no MIDI clock) |
| **Port** | front face, beside the host port | off = nothing connected · steady = keyboard connected and powered · **a short blink per note received** · fast flash = fault (too much current, or a charger in the host socket) |

**Status priority, highest first (when two apply, the ring shows the higher one):**
1. **Low battery** (fast flash): overrides everything.
2. **Tempo blink** (SYNC, no MIDI clock, so TAP is setting the tempo).
3. **Charging** (slow pulse).
4. **Steady.**

No third light (turn-3 ruling: two lights).

## 8. States
| State | What happens | What you see / hear |
|---|---|---|
| Off | nothing; the host socket is cold | all dark |
| On, no keyboard | silent, ready; plays from USB-C or TRS; the host socket stays cold | ring steady; port off |
| Keyboard plugged in | detected → VBUS on → enumerated | port steady |
| Playing | notes sound | port blinks per note |
| **Silent, keyboard connected** (job 29) | — | port steady with **no blink** on a key → notes aren't arriving (dead keyboard or charge-only cable). Blinks but silent → VOLUME, all tabs off in a half, phones plugged in |
| Port light off with a keyboard plugged in | a non-compliant cable, or the keyboard isn't detected | use the **C-to-A adapter** with the keyboard's own cable [r2]; firmware's always-on fallback is in reserve (owner trade-off) |
| Keyboard draws too much / charger in the host socket | keyboard power cut; floss keeps running | port flashes fast |
| Unplugged mid-chord | unheld notes fade on their tails; **held notes keep sounding** | port off |
| HOLD on, notes planted, keyboard gone | the drone continues; every knob still works | HOLD latched down; port off |
| HOLD on, a half full (12 or 13 planted) | the next note in that half replaces its oldest | — |
| A half with all tabs off | silent in and out (with MIDI SPLIT) | the tabs show it |
| Lean source = nothing | PRESSURE has no effect; velocity still works | — |
| SYNC, no clock, no tap yet | echo runs at the last tempo (120 BPM at power-on, PROPOSAL) | ring blinks that tempo |
| SYNC, MIDI clock present | echo follows the clock | ring steady (no tempo blink) |
| Charging while playing | normal | ring slow pulse, unless the tempo blink applies (priority, §7) |
| Low battery | warning before it stops (eng sets the threshold) | ring fast flash, over anything else |
| Headphones in | speaker mutes | — |
| Computer and keyboard together | notes merge if host and device work at once (unverified [r2]); otherwise TRS to the computer | — |
| Big home keyboard (49–61 keys) | plays if it draws ≤ ≈ 500 mA; note 60 is near its middle (UNVERIFIED per model); a half can steal past 12 / 13 | — |

## 9. The family interfaces this module meets (job 28)
| | Interface | floss's value |
|---|---|---|
| S1 | keyboard envelope the carry takes | 325–388 × 83–135 × 11–16 mm, ≤ 0.6 kg [eng] (the carry's job) |
| S2 | host port | USB-C, cold socket, ≈ 550–600 mA, front face on the axis [r2] |
| S3 | cable | **0.3–0.5 m** [r2]. **The kit cable is C-to-C with flat right-angle plugs** (PROPOSAL): a USB-C plug is reversible, so one flat right-angle plug can exit left or right by flipping it, and it sticks out only ≈ 10–15 mm [r2 §6]. Keyboards without USB-C use their own cable on **one C-plug-to-A-receptacle adapter**, carried in every kit [r2]. A coiled cable for sharing is an optional extra (product UNVERIFIED) |
| S4 | attachment | two ¼"-20 inserts, 160 mm apart at x 60 / 220 |
| S5 | plug behaviour | §8: any order, notes release on unplug, held notes survive, port light, cold socket, keyboard powered only while on |
| S6 | CC map | CC64 sustain, CC1 lean fallback, CC74 tone, CC11 expression, bend ±2; the full list goes in the spec |
| S7 | split rule | fixed note B3 \| C4 + the target rail; the advice line on the card and the site |

- **Reused unchanged by Big Energy and port-a-poly:** S1–S7; the target rail and target; the port light's meanings; the kit cable and adapter; the keyboard bed, end blocks and printed scale (carry parts).
- **Their module size is their own** (owner, 13:25).

## 10. Making steps outside the electronics (job 26)
| Step | Craft | Source or method | Needs trial or measuring? |
|---|---|---|---|
| Shell, deck, crown, rail, target | **3D printing** (PETG, as eng's weights assume [r2]) | our print files. **280 mm long needs a printer bed of ≥ ≈ 300 mm** (common 220–256 mm beds are too small) or **an outside print service**. Fallback: split the shell on the axis, with a keyed, screwed joint (ENG; visual for how the seam reads) | no |
| Dividers | printing (§3.1: groove, multi-material inlay, or pressed-in printed strip) | the printer's own methods | no |
| Threaded inserts | heat-set with a soldering iron (standard practice for printed parts) | ¼"-20 insert product UNVERIFIED | no |
| Feet | bought stick-on feet | — | no |

## 11. Engineering questions (one list; director's steer item 7)
1. **The deck at 26 (or 25) with the cells beside the crown:** my placement is x 49–109 / 171–231, y 38–88, with ≈ 0 margin to the hull wall and ≈ 1 mm to the insert bosses (§2.3). Confirm the stack and the U-shaped board.
2. **The knob, with a published height:** is there a Ø 14–15 knob ≤ 8–9 mm tall? If not, it's Ø 10 × 8 (35 holds) or Ø 14.9 at ≈ 41 tall (§2.1).
3. **The driver position for ≥ 5 mm of finger room:** it fits 105 only with Ø 10 knobs; with Ø 14.9 the module needs ≈ 108–110 deep (§2.2).
4. **Grille ≥ 620 mm² open** on the crown top (a Ø 46 field, or Ø 1.9 holes).
5. **Ported in the crown:** a ported box needs ≥ 130 cm³ and a folded port [r2]. The crown's box is ≈ 76 cm³ (visual), so I expect **no**. Confirm, so the owner's sealed / ported trade-off is stated honestly.
6. **Weight of the printed hull** and the shell lever (walls 2.0 with ribs). I assume eng's BLOCK figure, **0.67–0.93 kg**, not recalculated.
7. **Print bed:** a one-piece 280 shell on a ≥ 300 mm bed or by a service, vs an axis split.
8. **The ¼"-20 heat-set insert** product and its boss in PETG.
9. **The flat right-angle C-to-C cable** (S3): a product, and whether slim keyboards' USB-C sockets are mounted flat (UNVERIFIED per model).

## 12. Coverage: the jobs the module answers in every kit (against `jobs.md` rev 3.1)
| Job | Where |
|---|---|
| 1 strings anywhere | §1, §6 |
| 2 one cable, USB-C, any keyboard | §4, §6, §9 S2 / S3 (flat right-angle cable; adapter) |
| 4 every note | §6 voices (pools) |
| 5 split and octaves | §3 jambs, §6 |
| 6 where the split lands | §4 (target and rail; the advice line on the card and the site) |
| 7 velocity | §6 |
| 8 lean, selectable | §3, §6 |
| 9 no pressure | §6 lean source |
| 10 extras | §6 |
| 11 colour per half | §3 tabs, §6 |
| 12 shimmer | §3 axis, §6 |
| 13 echo, reverb, tempo | §3, §6, §7 (tempo blink) |
| 14 hold | §6 |
| 15 speaker / phones | §2, §5, §8 |
| 16 computer / other keyboard | §5, §8 |
| 17 MIDI out | §6 |
| 18 read the state | §3, §3.1 (groups by touch), §4, §7 (priority) |
| 19 one switch; battery and charging | §5, §7, §8 |
| 21 many vs one | §6 breath |
| 22 in tune | §5 TUNE; crystal tones [eng] |
| 26 printed case, proven parts; fix | §1, §10; host port and battery reachable (eng's layout) |
| 29 why silent | §7, §8 |
| 30 portable, makes sense, harmonious; ratio from the parts; any outline | §2 (conditional on §2.1–2.3) |
| 3, 20, 23, 24, 25, 27, 28 | partly §9; the rest in each kit's file |

**At risk:** job 30's 35 and 105 depend on the knob decision (§2.1, §2.2). Either outcome still answers job 30, as long as the ratio is restated honestly if the sizes move.

## 13. Owner trade-offs (from `module-r2.md` and this turn)
1. **Speaker loading:** sealed (f3 ≈ 255 Hz, robust, smallest) vs ported (f3 ≈ 105–135 Hz, +6 dB at 100 Hz). The passive radiator doesn't earn its place at this size [r2], which reverses the owner's "passive radiator would be cool". **Drawn sealed** (director R5). Ported is offered only if eng shows it fits the crown (§11.5).
2. **Height 35:** vs the 23–25 he saw earlier [r2 trade-off 2]. With Ø 14.9 knobs it becomes ≈ 41 (§2.1).
3. **Knob size: Ø 10 × 8 (keeps 280 × 105 × 35) vs Ø 14.9 (≈ 280 × 110 × 41).** New this turn.
4. **Weight:** module ≈ 0.67–0.93 kg (printed, BLOCK-class [r2]). The kit totals are in each kit's file. T5 is withdrawn (owner 13:49): reported, lighter is better.
5. Fixed voice pools 12 / 13; split-scoped HOLD.
