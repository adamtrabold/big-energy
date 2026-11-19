# Player review, round 9: the control taxonomy

**Date:** 2026-11-19
**Reviewer:** independent critic, playing synths for decades (Model D, Prophet, Juno, Minibrute, Grandmother, OP-1, Make Noise and Mutable modules)
**Judged:** `docs/control-taxonomy.md` (proposed, 2026-11-19), against the owner's ask ("define the categories of controls and what controls belong in those categories before laying anything out"). I also checked the bend-and-mod, paraphonic and panning feature docs to confirm what the instrument does.

**The bar:** the owner's 10. For a taxonomy, that means "a player would sort the controls this way, nothing is misfiled or missing, and every split has a reason I'd defend."

## Score: 8

The bones are right. It starts from the Model D's own panel sections, gives each control a job, puts the signal-versus-hands conflicts in one table, and leaves the owner's open calls as questions instead of deciding them. That's the right foundation. It falls short of a 10 on four counts:
- a few **job labels** are wrong in ways that will push the next layout the wrong way;
- one branch **mixes playing controls with set-up switches**;
- a handful of **things a player would ask about are missing**;
- it doesn't state the one principle that made the best layouts work: **a category split across the hinge must line up across it.**

All of these are fixable in the document, without the owner deciding anything first. With them fixed, I'd defend it as a 10.

---

## What works (keep it)

1. **Starting from the Model D's sections** (Controllers · Oscillator Bank · Mixer · Modifiers · Output), with Big Energy's additions slotted in and marked ★. Any Moog player recognises it at once, and it gives the owner a fixed reference.
2. **The four jobs** (set once · shape · play · level/out). This is exactly how hands think about a panel, and it's the right tool for deciding which half a control goes on.
3. **The conflict table (§4).** Every place where signal order and the hands disagree is written down with a reason. I agree with every resolution in it (detail below).
4. **The owner's rules with sources (§5), and the open questions (§6).** Nothing is invented and nothing is decided for him. Q5 rightly points out that his two statements about the lid's top row disagree.
5. **The player-language column in §3.** "How much wobble reaches its destinations" and "how bright: the hero dial" are how you'd explain the panel to a new player. It reads well.

---

## What doesn't work, most important first

### 1. Some job labels are wrong, and they matter for layout
The jobs decide which half a control goes on, so a mislabel becomes a misplacement.
- **release** is labelled *shape*. It's **play**. Model D players flick the DECAY switch mid-phrase: off for staccato, on for a tail. The manual puts it on the left-hand panel, by the wheels, because it's a performance switch.
- **mod → pitch** and **mod → filter** are labelled *set once*. They're at least **shape**, and often **play**. With the mod knob already up, flipping pitch on is how you bring vibrato in on a held note. These are the switches you reach for blind.
- **envelope (amount)** is labelled *shape*. On a Model D, CONTOUR AMOUNT is ridden together with CUTOFF; the two are one gesture. It's **shape / play**. It already sits with cutoff in 4a, so this only corrects the label, but it should be right, because it justifies keeping it on the base.
- **repeats** and **echo time** should both read **shape / play**. Riding repeats into self-oscillation, and sweeping time for pitch dives, are the most common live echo moves. This doesn't move them off the lid, but it should be on record that the lid holds some playing controls, so the lid's bottom row (the nearest reach) goes to them.

### 2. Branch 1c mixes playing controls with set-up switches
1c "Keyboard" holds keys, release, voices, velocity and touch. Release and the keys are played. Voices, velocity and touch are set once per patch or song. A player separates "what my left hand does while I play" from "how the keyboard is set up."

**Fix:**
- **1a Performance:** bend · mod · glide · release (and glide on/off, if added, item 3).
- **1c Keyboard setup:** voices · velocity · touch.
- The keys and the touch strip become the instrument's surface rather than "controls" in this list.

This also mostly answers Q2 ("which key controls?"). The owner's "all the key controls in one area" fits **1c**, and release joins glide in **1a**, beside it on the base. Both groups stay on the base, so nothing changes in R5's spirit.

### 3. Missing items a player would ask about
- **Glide on/off.** The Model D has a GLIDE switch on the left-hand panel (the taxonomy itself mentions it), and Big Energy has none: only glide time. Players set a glide time and flick glide in for one phrase. Without the switch you have to turn the knob down and find your setting again. Either add it (+1 switch, beside release; MIDI CC 65 is the standard portamento on/off), or record it as a deliberate omission. It's an owner question, and it belongs in the tree as "★ candidate."
- **The modulation source in PARA.** Blend takes its smooth wobble from oscillator 3. In PARA, oscillator 3 is a voice unless its track is off, which drops PARA to two voices (paraphonic doc). Its "mod" is then the played note (the paraphonic doc already notes osc-3 FM sounds clangy on chords). So **vibrato on chords means noise or losing a voice.** That's the first thing a player will hit in PARA. The taxonomy is the right place to flag it: either a firmware LFO as the mod source in PARA, or a stated limitation. Put it as an owner/eng question; don't solve it here.
- **Hidden controls (settings).** 7c lists power-on gestures, but not what they set. Bend range (arch owner question 8), MIDI channel, velocity curve and aftertouch depth are all controls; they just don't have knobs. List them under 7c so the layout never assumes a panel control that doesn't exist, and so nobody forgets to give them a gesture.
- **Aftertouch amount.** TOUCH picks a destination (mod · off · filter) but nothing sets how much. For mod, the MOD knob's depth plausibly covers it. For filter there's no depth anywhere. Note it: a setting, a firmware default, or a question.
- **What VOLUME controls.** Per the panning doc, the one dual VOLUME feeds phones **and** line out. For a DAW-first instrument, many players want line out at a fixed level, with volume for phones and the speaker only. That's not a panel change yet, but it belongs in 6a as a question. If the answer is "separate phones level," it adds a control.
- **Deliberate omissions from the Model D,** listed once so the owner sees they were chosen:
  - the mixer's per-source on/off switches (turning a level to zero does it, but you lose the setting);
  - the noise colour switch (white/pink);
  - A-440 (autotune replaces it);
  - the separate phones volume.

  One line each.

### 4. One layout principle is missing: split categories line up across the hinge
§4 accepts that the filter splits (cutoff, resonance and envelope amount on the base; contours on the lid), and that the effects split (character on the lid, levels on the base). That's right. What it doesn't say is what makes a split playable: **the two halves of a split category should sit directly above one another when the lid stands.** Filter contour over cutoff. Echo and reverb character over their levels. That alignment is why P5OBD read so well (filter decay in line with cutoff), and its absence is what kept P5R at an 8. Write it into §5 or §7 as a rule derived from the taxonomy, so the next layout starts from it and doesn't rediscover it.

### 5. Smaller corrections
- **Q4's framing is a little loaded.** §4 calls the Model D's placement of the mod switches "a 1970 wiring artefact." It isn't only that: putting each switch at its destination shows, module by module, what is being modulated. I still prefer grouping them with MOD (one gesture read in one place), but state both sides fairly. The owner values evidence over convenient generalisations.
- **The bend-and-mod feature doc contradicts the taxonomy.** Its line 4 and its decisions table say "mod switches sit with the oscillators and with the filter." The taxonomy and P5RS put them with MOD. Mark one as superseded, or the next layout inherits the contradiction.
- **"touch" against "touch strip"**: one is a switch, the other is the hidden sensor. That's fine, but say plainly in §3 that the strip has no panel presence. It already says "hidden"; good.
- **Tap** is filed correctly under Effects / Tempo and placed on the base by job. Nothing to change. I'd only add that its ring is also the status light, so it must never be covered or crowded. That's a layout constraint, not a category one.

---

## The conflict table (§4): do the resolutions go the way a player wants?

| Conflict | Taxonomy's answer | Player's verdict |
|---|---|---|
| Mixer | base, with the levels (owner R1) | **Agree.** On the base it feeds the filter right below it. |
| Filter | cutoff, resonance, envelope amount on the base; contour on the lid | **Agree,** with the alignment rule (item 4). |
| Mod routing | with MOD | **Agree,** but restate Q4 fairly (item 5). |
| Tune | by the oscillator bank (owner R2) | **Agree.** For a player it's set once, so anywhere findable works. His rule decides it. |
| Release | key behaviour, base | **Agree,** but it's *play*, and it belongs with glide (items 1–2). |
| Echo / reverb levels | on the base (owner, 14:08) | **Agree.** Throws are played. |
| Tap | play, base | **Agree.** |
| Pan / link | output, base | **Agree.** |

Every resolution goes the way I'd want. The table's only gap is that it doesn't turn the filter and effects splits into the alignment rule.

---

## Suggestions (in order)

1. **Correct the jobs:**
   - release → play;
   - mod → pitch and mod → filter → shape / play;
   - envelope amount → shape / play;
   - echo time and repeats → shape / play.
2. **Re-cut branch 1:** 1a Performance = bend · mod · glide · release (+ glide on/off if added); 1b Modulation = blend · mod → pitch · mod → filter; 1c Keyboard setup = voices · velocity · touch.
3. **Add the missing items:**
   - glide on/off (★ candidate);
   - the PARA mod source;
   - the settings list under 7c (bend range, MIDI channel, velocity curve, aftertouch depth);
   - aftertouch amount;
   - what VOLUME controls;
   - one line on each deliberate Model D omission.
4. **Add the rule to §5/§7:** a category split across the halves lines up across the hinge (filter contour over cutoff; effects character over their levels).
5. **Restate Q4 fairly,** and mark the bend-and-mod doc's "mod switches on oscillators and filter" as superseded or reconcile it.
6. **New owner questions:** Q10 glide on/off; Q11 vibrato in PARA (firmware LFO, or accept the limit); Q12 line out fixed or following VOLUME.

With 1–5 in the document, I'd hand this to the owner as a 10. The categories would be the ones a player thinks in, nothing would be misfiled or silently missing, and the layout rules would fall straight out of it.
