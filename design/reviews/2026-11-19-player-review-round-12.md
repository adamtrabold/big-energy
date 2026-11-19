# Player review, round 12: CATHEDRAL T4 vs T2
Date: 2026-11-19 · Reviewer: independent synth player (devil's advocate), fresh eyes · Reports to the owner; decides nothing.

Read: `design/owner.md` (latest entries), `docs/control-taxonomy.md`, and for each candidate the top view (9.9 px/mm) and the standing render.

## Scores
| Layout | Score | Based on |
|---|---|---|
| **T4**: three oscillators, half height 132 mm | **8 / 10** | `cathedral-s13-T4-top-9.9px-per-mm.png`, `cathedral-s13-T4-standing.jpg` |
| **T2**: four oscillators, half height 147.3 mm | **6.5 / 10** | `cathedral-s12-T2-top-9.9px-per-mm.png`, `cathedral-s12-T2-standing.jpg` |

Neither is a 10 yet. T4 is the one to finish. Four fixes, all on the lid except one heading pass, would get it to where I'd defend every control. T2 has a structural playing problem (below) that small tweaks won't fix.

## What works and what doesn't (most important first)

### 1. T2 splits the vibrato gesture across the panel (T2's dealbreaker)
The classic Model D move: left hand has the mod knob up, you flip **pitch** on over a held note, then off again. In T4, mod, blend, pitch and filter all sit in one left-hand cluster (mod front, switches just behind). That's right. In T2, mod stays front-left at x ≈ 27 mm, but blend · pitch · filter jump to the back-centre, about 70–85 mm away, above the cutoff. You have to let go of mod or take your right hand off the keys. Taxonomy §4 / Q5 says the switches live **with mod** because "it's the switches you reach for blind while mod is up". T2 puts the switches next to the mod group's label but away from the mod *knob*. Blend also lands in the filter column, between the filter contour and cutoff, which muddies that column's vertical read.

### 2. Echo time and repeats are on the farthest row in both (taxonomy §3/§10 not met)
The approved taxonomy says it twice: "The lid's row nearest the player should go to [echo time and repeats]." Both layouts put echo at the top right of the standing lid, the farthest reach on the instrument, and give the near row to reverb, which is pure set-and-forget. Echo time is the knob I sweep for pitch dives, and repeats is the one I push into self-oscillation at the end of a phrase. In the standing render (T4) my hand goes from the cutoff right up to the top corner, past reverb. Swap them: reverb on top, echo time · repeats on the near row, directly above the echo / reverb levels. Rule H gets better, not worse: the throw knob (echo level) then sits right under the knobs it works with.

### 3. Reverb is off the lid's row grid in both
T4's lid rows sit at about 20 · 37 · 54 · 71 mm from the top edge (in image px: 200 · 370 · 540 · 710). Reverb sits at about 61 mm (605 px), floating between the speaker row and the bottom row. T2 has the same fault the other way: reverb at 805 px, while osc 4 and the filter contour sit at 740. The owner has already rejected inconsistency once ("the markings around the knobs are all inconsistent… This is not a 10"). Fix #2 fixes this as well if echo's near row lands on the 710 baseline.

### 4. Oscillators over mixer (rule H): T2 meets it, T4 doesn't, and I'd still pick T4
T2 puts mixer 1–4 at the base's back-left, under the oscillator block. Rule H is met and setting osc 2's level is a straight drop down. T4 puts mixer 1–3 in the centre, under the filter contour and over resonance · cutoff · envelope. Taken strictly, that breaks the team's rule H. In the hands, I'll defend T4:
- Mixer level is also the **drive** control. Pushing mixer 1 into overdrive while riding cutoff is one gesture, and in T4 both are under one hand. The Model D puts the mixer right next to the filter for the same reason.
- Rule H is the team's rule. The owner's rule is R1, "mixer on the base", and both meet it.

The cost: the filter column now reads contour → mixer 1 2 3 → resonance · cutoff · envelope, and a first-timer may read "1 2 3" as part of the filter. The "mixer" heading needs to be as strong as "filter" (see #6).

### 5. Tuning: T4 meets R2, T2 barely does
T4 puts tune · drift directly under oscillator 3, which is what R2 asks ("closer to the oscillators"). T2 centres tuning over the speaker, about 64 mm from the oscillator block. It looks balanced, but it's the "tuning as ornament" answer. T2 also leaves a blank row between osc 3 and osc 4 (row pitch 225 px against 160 elsewhere). It reads as a missing row, not as "optional".

### 6. Headings use three styles
Big script headings (oscillators, amp, echo, mixer, effects, controllers, tempo, out); small headings with a rule line (mod, keys); and T4's "tuning" is big **with** a rule. Labels sit above the knobs on the oscillators, amp and mixer, and below on echo (even though echo is a top row), reverb, filter and tuning. My guess is the logic was "labels toward the nearest edge", but echo breaks it because of its type sub-legends. Pick one heading style and one label-side rule, and apply it everywhere.

### 7. Two "pan"s
Dry **pan** on the base and echo **pan** on the lid. Each has a heading (out / echo) to disambiguate, so this is fine under the one-word rule. Just make sure the echo pan's "•midi" dot and the base pan's dot don't read as the same CC (taxonomy: CC 10 is the dry pan).

### 8. Bend stick height
T2's stick drops to 9.0 mm so the case closes. A shorter throw is less precise for vibrato-by-hand and for landing a whole-step bend. That's a quiet point for T4.

### What's already right in both (don't touch)
- Cutoff: red, larger, centre front, on the speaker axis. It's the hero dial and it plays like one.
- Bend + mod front-left, glide + release beside them: the Model D's left-hand panel, done properly.
- Echo / reverb levels over volume / pan (the owner's fixed pair). It reads as "effects → out" and makes for good throws.
- Keys switches (voices · velocity · touch) on the tighter grid per R5. Fine for set-once controls.
- Filter contour directly over resonance · cutoff · envelope (rule H, exact in both).
- Tap with its status ring, alone in the front row: easy to find blind, never crowded.
- T4's amp contour stacked directly over the filter contour, same columns, attack over attack. That's a lovely, readable parallel. T2 loses it by sending amp to the top right, over the effects levels, where rule H implies a relationship that isn't there.

## Owner objections to expect
- **T4:** "Echo's up in the corner, I reach past reverb to ride time." (#2) · "Reverb's floating." (#3) · "Why are the mixer numbers under the filter envelope?" (#4)
- **T2:** "The mod switches are nowhere near the mod knob." (#1) · "Tuning's decorative." (#5) · "There's a hole above oscillator 4." (#5) · "Amp's sitting on top of the effects."

## Suggestions
1. **Take T4 forward; drop T2.** Draw VCO 4 as the option it is (taxonomy Q12 default). The team's finding that a four-oscillator T4 doesn't fit holds, and I wouldn't buy VCO 4 at the price of T2's mod split.
2. **T4 lid, right column, top to bottom:** reverb type · decay on the top row (20 mm). Echo type · pan on the middle row (37 mm). Echo **time · repeats** on the bottom row (71 mm, the same baseline as filter and tuning), with **free · sync** right beside time. That puts the played echo controls nearest the hand and above the echo level, and puts every lid knob on one row grid.
3. **Make "mixer" a real heading** with the same weight and treatment as "filter". Consider a faint grouping rule under mixer 1 · 2 · 3 · extra · source, so the row doesn't read as part of the filter column.
4. **One heading style and one label-side rule** across both halves. Remove the stray rule line under T4's "tuning", or give every heading one.
5. **Optional, worth a look:** osc 1 has an empty pitch slot (true to the Model D). Track 3 sits alone in a fourth column. Both are on grid, but the osc block's right edge looks ragged. Leave it unless the owner points at it again. If he does, moving track 3 to sit directly under osc 3's pitch, as a toggle on the tuning row, closes the hole without breaking R2.

With 2–4 done I'd play T4 on stage and in the studio and defend every control's place. I'd call that a 10.
