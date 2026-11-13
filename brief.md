# Owner's words (verbatim)

> i love analog synths. im curious how far we can push ai assistance in making analog things happen. i'd love for you to try creating me a portable moog model D clone. everything from designing and getting the pcb printed to ordering the parts and getting the enclosure designed and created. i can 3d print one, or we could order one, idk go wild. fan out agents as needed, use whatever external tools you need kicad blender or 3d modeling programs or whatever etc. just go for it. start by planning it out based on what needs to be done in what order. pick the right models for the tasks.

> also figure out ways to verify as much as possible throughout each step that it sounds as it should and will be created correctly. everything from virtual circuit modeling, etc.

> let's do everything we can do avoid a rev 2 being needed. re: your questions –
> 1. [form factor / keys] idk what should we do? i think keys would be amazing, but they don't have to be like a trad keybed. give me creative ideas here.
> 2. [power] completely portable would be great.
> 3. [assembly: JLCPCB-assembled SMD vs through-hole you solder] let's do both versions and we can see how easy we can get it without having to pay someone else to solder. how "ikea" can we get the instructions.
> 4. [test board / budget] you tell me what it's gonna cost for each version. i am not interested in a bunch of testing on my own i want to challenge us to get to incredible without a bunch of rigmaroll.

# Confirmed constraints
- Sound/architecture: Minimoog Model D voice (3 VCOs, noise, mixer, 4-pole transistor ladder filter, 2 contour generators, VCA, glide, mod wheel/routing). Must not use the "Moog" name or trademarks.
- Fully portable: battery powered.
- Two build versions from one circuit: (A) SMD parts assembled by JLCPCB; (B) all through-hole, owner solders, IKEA-style instructions.
- Owner does NOT want to do testing/calibration rigmarole: minimize or eliminate manual calibration and test equipment.
- Goal: no rev 2. Verify everything virtually first (SPICE, netlist cross-checks, DRC/DFM, 3D fit).
- Owner: Adam — designer, musician, visual artist; owns a eurorack (Mutable Plaits, Rings) and a Maschine+. Can 3D print.
- Owner cannot be paid for by agents; agents prepare carts and files, owner clicks buy.

# Tools available in the workspace
KiCad 9 (kicad-cli), ngspice, OpenSCAD, CadQuery, Python. Network: package registries + GitHub; general web via WebSearch/WebFetch tools.
