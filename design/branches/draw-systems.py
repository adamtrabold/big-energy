# Branches jam: systems designer's draw (real randomness, secrets.SystemRandom).
# Extends design/concepts/jam-visual-draw.py with the owner's new sources:
# furniture, instruments, tools, artistic forms, emotion, and the park.
# Run: python3 -I design/branches/draw-systems.py
import secrets
r = secrets.SystemRandom()

oblique = ["Use an old idea","State the problem in words as clearly as possible","Only one element of each kind","What would your closest friend do?","What to increase? What to reduce?","Are there sections? Consider transitions","Try faking it!","Honor thy error as a hidden intention","Ask your body","Work at a different speed","Look closely at the most embarrassing details and amplify them","Emphasize the flaws","Disconnect from desire","Use fewer notes","Reverse","Make a blank valuable by putting it in an exquisite frame","Turn it upside down","Abandon normal instruments","Give way to your worst impulse","Repetition is a form of change","Do nothing for as long as possible","Remove specifics and convert to ambiguities","The inconsistency principle","Water","Decorate, decorate","Humanize something free of error","Is the tuning appropriate?","Courage!","Simple subtraction","Put in earplugs","Look at the order in which you do things","Mute and continue","Fill every beat with something","Use filters","Imagine the piece as a set of disconnected events","Change instrument roles","Be dirty","Retrace your steps","Distorting time","Accretion","Infinitesimal gradations","From nothing to more than nothing","Discover the recipes you are using and abandon them","Gardening, not architecture","Cluster analysis","The most important thing is the thing most easily forgotten","Tidy up","What wouldn't you do?","Be extravagant","Lowest common denominator","Cut a vital connection","Listen to the quiet voice","Breathe more deeply","Go outside. Shut the door.","Faced with a choice, do both","Overtly resist change","Don't be afraid of things because they're easy to do","Look at a very small object, look at its centre"]

# Unrelated fields, now weighted toward the owner's sources.
furniture = ["Windsor chair (steam-bent spindles into a solid seat)","Shaker peg rail","Danish modern teak sideboard","Gerrit Rietveld Red-Blue chair","campaign furniture (folds, brass corners, travels)","Thonet bentwood No. 14 (flat-packed, 6 parts)","Japanese tansu (stepped chest, iron pulls)","Nakashima live-edge slab","Prouve folding/standard chair","Eames LCW (moulded ply)","writing slope / lap desk","Arts and Crafts Morris chair","sawbuck table","piano bench (lid lifts, music inside)"]
instruments = ["pipe organ (stops, ranks, pull-knobs)","harmonium / shruti box (bellows)","kalimba (tines on a box)","hammered dulcimer","autoharp (chord bars)","music box (pinned cylinder, comb)","steel pan","hurdy-gurdy (crank, keyed tangents)","glockenspiel (bars on a frame)","melodica (breath)","theremin (no touch)","handpan","bandoneon (buttons both ends)","zither"]
tools = ["Japanese hand plane","surveyor's theodolite","carpenter's folding rule","fly reel","sextant","letterpress composing stick","bento box","Opinel knife (one lock ring)","field easel / pochade box","plein-air watercolour tin","garden trug","pocket sundial","bicycle bell","darkroom timer"]
art = ["Calder mobile (balance, movement)","Noguchi Akari lamp (paper, light)","Agnes Martin grid (quiet repetition)","Isamu Noguchi garden stones","Rothko colour field (emotion by area)","Ruth Asawa wire forms (woven, see-through)","Brancusi Endless Column (repetition, rhythm)","Sol LeWitt wall drawing (instructions as art)","Hilma af Klint diagrams","Japanese wabi-sabi tea bowl (kintsugi, wear)","Bauhaus weaving (Anni Albers)","Barbara Hepworth pierced form (hole as figure)","Matisse cut-outs","Andy Goldsworthy (made from the site)"]
emotions = ["wonder","calm","playfulness","longing","courage","tenderness","mischief","reverence","joy","nostalgia","focus","awe"]
park = ["on a bench, sharing it","on the grass, cross-legged","under a tree in dappled light","in bright midday sun","at dusk, light fading","by water","with wind","carried on a walk, played in short stops","with a friend joining in","on a picnic blanket next to food"]
twists = ["it has no visible screws","it is mostly one colour","it closes","it is held, not set down","it has a front and a back with different personalities","everything is round","the keys are the most beautiful part","it is meant to be written on","it wears in, and should show it","it can hang on a wall","the case is soft","it is asymmetric on purpose","light passes through it","it is made of two materials only, one hard, one soft","the bottom is as designed as the top","it looks like it was found, not bought","it has a handle","it makes a sound before you play it","the controls are where you'd least expect","it tells time","it is a pair","it sits on the ground"]
seeds = ["ONE SHEET","FOLD","HUSH"]

print("oblique:", r.sample(oblique, 3))
print("furniture:", r.choice(furniture))
print("instrument:", r.choice(instruments))
print("tool:", r.choice(tools))
print("art:", r.choice(art))
print("emotions:", r.sample(emotions, 2))
print("park moment:", r.sample(park, 2))
print("twists:", r.sample(twists, 3))
print("seed concept for branch 1..3:", [r.choice(seeds) for _ in range(3)])
print("d6 echo-sync twist index:", r.randint(1, 6))
