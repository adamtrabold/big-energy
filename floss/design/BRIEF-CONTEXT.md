# floss design loop: brief context, REV 2 (orchestrator, 2026-11-22 12:55)

## READ THIS FIRST: what changed
floss is now a **keyless portable sound module played by a travel MIDI keyboard over USB-C**. floss is the USB host and powers the keyboard, and **floss is designed so a keyboard can be carried with it**. It's a **family principle** for every synths-to-go instrument, Big Energy included later: "This is the plan for all modular portable synths that we build — portable sound modules with a way to carry a keyboard with it. It should be flexible and not reliant on a single model of keyboard." / "I’m saying big energy has to change too yes this is a systems philosophy decision". No built-in buttons: "No hybrid." Proportions are open: "Let’s do USB c and we can riff on the dimension ratios".

What this supersedes below: everything about built-in keys, Hall keys, pads, per-key pressure sensing and the key strip; the "25 keys or fewer" line now applies to the keyboard floss is carried with. BOW and TIDE as drawn (round 1) assumed built-in keys. KEPT is dead.

Read these, in this order:
- `floss/REQUIREMENTS.md` (rev 2): decisions and targets T1–T12. T4 (size) is open while proportions are explored.
- `floss/design/jobs.md` (rev 2, 28 jobs, including carrying and swapping keyboards and job 28's family carry standard).
- `floss/eng/module.md`: the engineering baseline. 25 voices allocated from MIDI, an analog ensemble plus Daisy modes, a USB host port (now USB-C) at 500 mA, a 22.2 Wh battery, a minimum body of ≈ 250–290 × 90–110 × 30–35 mm, and slim travel keyboards 325–388 mm wide, 83–135 deep and 11–16 tall.
- `design/owner.md`: the entries from 2026-11-21 onward, verbatim.

Process rules from Adam: he builds it himself; he measures nothing ("I’m truly to see how far agents alone can get me"); reliable choices only, on published evidence.

---

# floss design loop: brief context (orchestrator, 2026-11-22)

Every teammate gets this file. It holds the owner's words, his direction, what's settled versus open, and the paths to everything. Teammates can't see the chat with the owner.

All paths are relative to the repo root: `/home/claude/big-energy` (GitHub: adamtrabold/synths-to-go, renamed from big-energy). The work folder is `floss/design/`.

## The work
Build plans for **floss**, the string machine in **synths-to-go** (working title). synths-to-go is a family of portable instruments by Adam (the owner): big energy (a Model D clone with 4-voice paraphony, the first instrument, its design largely done), port-a-poly (a true analog poly, not started), and floss. "Build plans the Big Energy way" means the same path Big Energy took: design loop, first principles, spec, verification. This loop is the concept phase for floss as an instrument: what it is, how it works, how it looks and feels.

## The owner's words for the task (verbatim)
- "I like the synths you mentioned more than the model d sound wise. Just chose model d for simplicity. Polyphonic would be amazing."
- "I'm more thinking the portability factor."
- What draws him: "Analog voices, shimmer and warmth"
- "String machine and analog poly are way more inspiring than model d.  We could go back to first principles with string machine too while still proving out the platform"
- "No build decisions is wrong. I want to make build plans like big energy idk what I'll build first is all"
- "Call string machine floss"
- "Budget ceiling should be what we can to hit the desired goal. Let’s go on the design loop"

The full verbatim record, newest at the bottom, is `design/owner.md`. Read every entry from **2026-11-21** onward. Earlier entries are Big Energy history: useful for his taste, but not floss decisions.

## Settled by the owner (2026-11-21 / 22). Don't reopen these; design within them.
- **Keys: 25 or fewer.** "Portable means 25 or less." No extended keyboard.
- **Split with independent octave select for each half:** "it would be nice to octave select each half of the keyboard"
- **Velocity, as an innovation on the classic string machine:** "it would be cool to innovate on the original string synth with velocity"
- **Pressure:** look into **per-key pressure** ("Yes let’s look to innovate"), and the player **selects what pressure does** ("Would be cool to select what the pressure strip does"). Per-key pressure must still prove feasible with the Hall-sensor keys. Design so the concept still works with a shared strip.
- **Battery powered.** Pack size and runtime come later, from a power budget.
- **One built-in speaker, muted by headphones,** as on Big Energy. Stereo is for headphones and outputs. **Look into a passive radiator** ("Passive radiator would be cool"); it needs a sealed air space.
- **Shimmer: an analog mode (bucket-brigade ensemble) plus Daisy (digital) modes:** "Analog mode on shimmer but modes to use the daisy too". Echo and reverb stay on the Daisy (Electrosmith Daisy Seed), as on Big Energy.
- **MIDI:** Big Energy's rules (USB-MIDI plus 3.5 mm TRS in and out; synth settings controllable over MIDI; MIDI never flips switches; knob-only controls send no MIDI; echo syncs to MIDI clock), plus a **MIDI split you can turn on or off** (each half on its own channel), plus **velocity and pressure sent over MIDI** (polyphonic aftertouch if per-key pressure works).
- **No screens, no encoders; real bought knobs and keys** ("Let’s try without"). Every choice that needs a control has to earn its place on the panel.
- **A shared universe:** "Yes let’s make these as a shared universe and reuse as much as we can". Reuse Big Energy's enclosure family, parts and construction wherever floss's needs allow.
- **No fixed budget ceiling.** Cost everything honestly anyway.
- Build order between the instruments is undecided. Don't design floss as "first" or "second".

## Open: the team's to explore
Everything else. That includes:
- what makes floss *floss*: its point of view and character;
- the voice architecture (how tones are made, divide-down or otherwise, and how velocity and pressure reach each note);
- which registers or sections it has;
- what the panel holds and how it's laid out;
- which enclosure format from the family it uses and how it adapts;
- what's new about it versus a 1974 Solina.

Ideas floated in chat but not decided (treat as material, not requirements): per-key swells, pressure-controlled bowing, drift between notes, sine stacking like Adam's Dreadbox Antiphon, a "strings" layer inside port-a-poly (one level knob).

## His taste and context (not decisions)
- He likes blending several oscillators per voice, the Juno's chorus and warmth, and the Dreadbox Antiphon (8 analog sine oscillators, spring reverb).
- He's skeptical of mixing analog and digital voices inside one chord.
- He's a designer, musician and visual artist (MFA). He wants concepts with a real point of view, drawing on furniture, instruments, tools and art. From the Big Energy record: "follow principles of design of furniture ... instruments, tools, but also artistic inspirational forms and emotion. i want to take this to the park and be inspired."
- He liked the peg keys on Big Energy's HUSH concept ("organ like" feel). CATHEDRAL is Big Energy's current case design.

## Files
- Facts and the floss record: `floss/README.md` (how string machines work, checked facts, ideas discussed, decisions).
- Owner record: `design/owner.md` (2026-11-21 onward for floss).
- Big Energy, the shared universe:
  - Design: `design/concepts/common-how-it-works.md`, `design/concepts/common-looks-and-feels.md`, `design/concepts/one-sheet/`, `design/concepts/fold/`, `design/concepts/hush/`.
  - Big Energy's jobs (as reference only): `design/jobs.md`.
  - Panel and branch work, including CATHEDRAL: `design/branches/`.
  - Engineering spec: `eng/budget-variant.md` (Daisy, Hall keys, battery, speaker, power).
  - Locked set: `VERSIONS.md` and `versions/`.
- Poly and hybrid research: `explore/poly-hybrid.md`.
- This work: `floss/design/jam.md`, `floss/design/jobs.md`, `floss/design/concepts/`, `floss/design/scores.md` (the orchestrator writes it), `floss/design/notes/<role>.md`.

## Rules
- Write in plain English. Images go in the work folder as files.
- Don't commit or push; the orchestrator does.
- If facts matter (part availability, chip specs, how a classic instrument worked), check them and say which you checked.
- Use real randomness where the role brief says so.
