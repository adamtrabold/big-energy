# What we've learned about keys (orchestrator's factual summary, 2026-11-12)
Owner requirements (all verbatim in owner.md):
- 25 keys minimum (two octaves) across roughly 280–292 mm; doesn't have to be a traditional keybed.
- Must "feel like an instrument"; no clicky computer-keyboard feel.
- As silent as possible (hard criterion).
- Velocity REQUIRED.
- Real bought parts for anything touched; NO 3D-printed keys/knobs; laser/CNC-cut parts are fine and the owner will cut them himself at Vector Space (CO2 lasers 100 W / 150 W, CNC router; Delrin permission/thickness at Vector Space UNVERIFIED — another makerspace limits Delrin to ≤2 mm).
- NO harvesting a keybed from another product.
- Through-hole soldering only; ready-made modules OK; no SMD.
- Cost is the owner's main concern. Keys must not drive main PCB size.
- Liked references: Critter & Guitari maple peg keys, OP-1 flat keys, Korg phase8 button keys, drum-pad style pads in a key layout.
Engineering/sourcing findings (eng/key-sourcing.md, eng/budget-variant.md §v1.4b):
- No bare new 25-key mini keybed is sold to individuals; Fatar (via Doepfer) is full-size only (~350 mm for 25 keys) and the 2-octave model is discontinued.
- Commercial piano-shaped keycaps: none found.
- Contactless sensing is cheap: SS49E-class linear Hall sensor, TO-92 through-hole, ~$0.10 each; small neodymium magnets ~$0.15–0.30 each. Analog position → velocity by timing between two thresholds; firmware self-learns each key's range (no trimming).
- Current default (switch-per-key): Kailh Choc V2 silent switch (~$0.70) for guidance/return + magnet in an owner-cut key top + TO-92 Hall beside it, ≈ $50–55 for 25 keys. Choc travel is only 2.8 mm. Long key tops on one stem may rock.
- Gateron low-profile Hall switches (~$0.84) — sensor fit through-hole unconfirmed.
- Speaker magnet must sit ≥60 mm from key sensors (field shift small at that distance, calibrated out).
- The synth is monophonic (one note at a time, low-note priority, single trigger), so the key system never needs real polyphony.
