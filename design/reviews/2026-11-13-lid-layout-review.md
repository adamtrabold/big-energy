# Lid layout review: CATHEDRAL, arrangement P (2026-11-13)

Reviewer: independent critic, acting as audio engineer and synth designer. Lens: **understanding**. Can a player read the panel, and is it in signal order? Looks are judged only where they hurt reading.

Based on: lid top view (8.7 px/mm), full top view open flat (8.3 px/mm), standing 3/4, the owner's 18:00 screenshot of the previous lid, how-it-works §16–17, and the opening signal walk in how-it-looks-and-feels.

## Score: 7 / 10

This is a big step up from the 18:00 lid. That lid split the mixer around the speaker, mixed oscillator and mixer knobs in one block, and put the effects across the top. The new lid reads top to bottom as oscillators → mixer → contours → effects, with out in a column, and VOLUME ends up in the corner nearest the hand. It answers the owner's complaint, and a Model D player will find the oscillators and mixer straight away.

It isn't a 9 yet. Most of the switches still can't be read, a few sit under the wrong knob, and the base's group names contradict what the controls do. These are cheap fixes (legends and small moves). The architecture is sound.

## What works

1. **Signal order down the page.** Oscillators, then mixer, then contours, then echo, then reverb, then out. It matches the Matriarch and Grandmother logic (effects after the VCA, volume last). The owner's rule is met.
2. **Oscillator bank in Model D order.** Range / freq / wave per VCO, with wider gaps between VCOs, and the mixer as one row of four in order. Any Moog player is at home.
3. **Filter contour left, loudness contour right**, mirrored about the window. That's how the Model D stacks them, turned on its side. It's clear.
4. **Echo before reverb, kind → time → repeats → mix** in each effect. This is the convention (minilogue xd, most pedals).
5. **Live controls nearest the hands.** Effects mix, VOLUME and the pans are in the bottom band, and the oscillators are farthest away. That's right for an instrument whose oscillators are set and left.
6. **Base played row.** CUTOFF as the red hero on the axis, EMPHASIS and AMOUNT either side, bend stick at the far left. That's where a Moog player's hands expect them.

## What doesn't (most important first)

1. **Most toggles have no position legends. Must fix.**
   - Only FREE / SYNC and OFF / FOLLOW show what their positions mean.
   - PARA (mono / para / para+4), VELOCITY (loud / both / filt), TOUCH (mod / off / filt), SOURCE (noise / ext / fb), KBD (how much tracking?), OSC 3 CTL, OSC MOD, FILT MOD and DECAY are bare words.
   - Several are 3-way switches where the *middle* position matters. A player can't learn these from the panel; they'll need the manual every time.
   - **Fix:** print the positions at both ends of every toggle, like FREE / SYNC. Where space is tight, use short forms (e.g. "mono · para · +4", "loud · both · filt", "off · ½ · full").

2. **SOURCE sits under OSC 3, not under NOISE / EXT. Should fix.**
   - SOURCE picks what the NOISE / EXT knob does, but the table puts it at x 242.5, the OSC 3 column.
   - Players read "switch under knob" as "switch belongs to that knob". The doc itself cites the Pro-One lesson that a shared knob needs its selector beside it.
   - **Fix:** move SOURCE to x 262.5, under NOISE / EXT.

3. **The oscillator switches read as one switch per VCO. Should fix.**
   - PARA sits under VCO 1, OSC MOD under VCO 2 and OSC 3 CTL under VCO 3. A player will read PARA as "VCO 1's switch" and OSC MOD as "VCO 2's modulation".
   - Only OSC 3 CTL is really per-oscillator. PARA and OSC MOD act on the whole bank.
   - **Fix:** keep OSC 3 CTL under VCO 3. Put PARA and OSC MOD together at the left of the switch line, under RANGE 1 / WAVE 1 (the Model D puts its oscillator modulation switch at the bank's top-left). Or draw a short engraved bracket under all three VCOs and hang those two from it.

4. **The base's group names contradict the controls. Should fix.**
   - "mod" (the wheel amount) sits under the **pitch** heading.
   - "drift" (oscillator pitch wander) sits under the **mod** heading.
   - **TAP** (echo tempo) sits under "mod" too, so it reads as an LFO tap.
   - **Fix:** regroup the base without moving the hero.
     - Left group, "controllers": bend · mod · mod mix · glide. That's the Model D controllers section plus the wheel. It keeps the wheel by the stick and puts MOD MIX next to the wheel it feeds.
     - Right group, "tune": tune · drift, then TAP labelled **"echo tap"**.

5. **The lid "filter" heading has no filter knobs under it. Should fix.**
   - The left column says "filter" but holds only KBD and FILT MOD. CUTOFF, EMPHASIS and AMOUNT are on the base under a second "filter" heading.
   - A player tracking cutoff will look for keyboard tracking next to CUTOFF, as on the Model D, where KBD CTRL and FILTER MOD sit right by cutoff.
   - **Fix (best):** put KBD and FILT MOD in the base filter group, beside EMPHASIS / AMOUNT, if a toggle bat clears the closed lid; check this under R-LOW. **Fallback:** put them under the filter contour knobs (mirroring the loudness side's switches), drop the lone "filter" heading, and title the group "filter contour · tracking".

6. **"decay" three times, and the DECAY switch is ambiguous. Should fix.**
   - The DECAY toggle sits beside the loudness DECAY knob, and reverb has a third DECAY.
   - On the Model D the DECAY switch sets release for **both** contours and sits by the player's left hand. Here, under the loudness contour, it reads as loudness-only.
   - **Fix:**
     - Rename the switch "release" with positions "off · = decay".
     - If it affects both contours, put it between them or say so in the legend.
     - Consider the base controllers group, where Moog players expect to flip it live.

7. **Echo vs delay naming, and FOLLOW far from what it links. Should fix.**
   - The group says "echo" but the knob says "delay pan". Use one word: "echo pan".
   - FOLLOW sits in the out column, about 140 mm from DELAY PAN. When it's on, the echo pan knob does nothing, and nothing near that knob says so.
   - **Fix:**
     - Label the switch "echo pan: own · follows dry", so it names both ends.
     - Or put a tiny "follow" mark by DELAY PAN.
     - Also make sure "delay pan" clearly says what it pans. The owner's words describe the echo panned separately from the dry signal. If the knob actually pans the echo *into the reverb*, players will expect a stereo position of the echo and may be surprised.

8. **VELOCITY and TOUCH are parked under the loudness contour. Nice to have.**
   - Both can route to the filter or to mod, but under "loudness contour" they read as loudness-only.
   - **Fix:** a small "keys" sub-label or a short rule over the pair. The position legends from item 1 do most of the work.

9. **Dual-meaning knobs in PARA. Nice to have.**
   - FREQ 2 / FREQ 3 become fine detune in PARA, and OSC 3 CTL interacts with voice allocation.
   - **Fix:** a small secondary legend ("detune" in a lighter weight), or note it in the quick-start.

10. **The out column starts beside the contours. Nice to have.**
    - Read by rows, DRY PAN is met before the echo. It's minor because the engraved break makes it a column.
    - **Fix:** fine as is. If space ever allows, start the column at the echo row's height.

## The owner's likely objections

- "Why are there two filter sections?" (item 5)
- "What do these switches do?" (item 1). He'll hit this the first time he tries PARA or VELOCITY.
- "Why is tap tempo in the mod section, and so far from the echo?" (item 4; open item V3)

## Suggestions

1. Position legends on every toggle (item 1). This is the single biggest gain in understanding, and it costs no layout.
2. SOURCE under NOISE / EXT (item 2).
3. PARA + OSC MOD together at the left of the oscillator switch line; OSC 3 CTL stays under VCO 3 (item 3).
4. Regroup the base: controllers (bend, mod, mod mix, glide) | filter | tune (tune, drift) + "echo tap" (item 4).
5. KBD + FILT MOD beside CUTOFF on the base, if the closed lid clears them; otherwise under the filter contour (item 5).
6. Rename the DECAY switch to "release" and say which contours it acts on (item 6).
7. "echo pan", plus a FOLLOW legend that names both ends (item 7).
