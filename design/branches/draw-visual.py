# Branches jam turn 2: visual designer's draws (real randomness, secrets.SystemRandom).
# Different decks from draw-systems.py on purpose, so the two designers aren't drawing
# from the same pool. Oblique cards used in any earlier jam are removed from the deck.
# Run: python3 -I design/branches/draw-visual.py
import secrets
r = secrets.SystemRandom()

used = {"Work at a different speed","Only one element of each kind","Cut a vital connection",
        "Use an old idea","Simple subtraction","What wouldn't you do?","Reverse",
        "Remove specifics and convert to ambiguities","What mistakes did you make last time?",
        "Decorate, decorate","Use fewer notes","State the problem in words as clearly as possible",
        "Look closely at the most embarrassing details and amplify them","Water"}
oblique = ["What would your closest friend do?","What to increase? What to reduce?","Are there sections? Consider transitions",
 "Try faking it!","Honor thy error as a hidden intention","Ask your body","Emphasize the flaws","Disconnect from desire",
 "Make a blank valuable by putting it in an exquisite frame","Turn it upside down","Abandon normal instruments",
 "Give way to your worst impulse","Repetition is a form of change","Do nothing for as long as possible",
 "The inconsistency principle","Humanize something free of error","Is the tuning appropriate?","Courage!",
 "Put in earplugs","Look at the order in which you do things","Mute and continue","Fill every beat with something",
 "Use filters","Imagine the piece as a set of disconnected events","Change instrument roles","Be dirty",
 "Retrace your steps","Distorting time","Accretion","Infinitesimal gradations","From nothing to more than nothing",
 "Discover the recipes you are using and abandon them","Gardening, not architecture","Cluster analysis",
 "The most important thing is the thing most easily forgotten","Tidy up","Be extravagant","Lowest common denominator",
 "Listen to the quiet voice","Breathe more deeply","Go outside. Shut the door.","Faced with a choice, do both",
 "Overtly resist change","Don't be afraid of things because they're easy to do","Look at a very small object, look at its centre",
 "Towards the insignificant","Balance the consistency principle with the inconsistency principle","Destroy the most important thing",
 "Only a part, not the whole","Think of the radio","Use 'unqualified' people","Spectrum analysis","Children's voices: speaking, singing",
 "Do the words need changing?","Emphasize repetitions","Give the game away","Lost in useless territory"]
oblique = [o for o in oblique if o not in used]

# Decks the systems script doesn't have.
furniture_principle = ["proportion (a governing ratio)","the honest joint","the plinth / the object lifted off the ground",
 "the reveal (a shadow gap between parts)","the stretcher (a member that holds two legs apart)","the apron",
 "the frame-and-panel (panel floats, frame holds)","the bevel that thins an edge visually","the drawer (a thing inside a thing)",
 "the foot (where it touches the world)","patina (designed to age)","the knock-down joint (wedge, tusk tenon)"]
instruments2 = ["accordion (bellows, buttons, straps)","Appalachian dulcimer (lap, fretboard, noter)","koto (moveable bridges)",
 "bagpipe (chanter + drones)","mbira in a gourd resonator","harp (frame, column, soundboard)","tabla (two drums, a pair)",
 "concertina (hexagon ends)","celesta (piano keys, bell bars)","lyre","tongue drum","marimba (bars over resonator tubes)",
 "carillon (baton keyboard, struck with fists)","clavichord (tangents, the softest keyboard)"]
tools2 = ["Japanese pull saw","spirit level (a bubble in a vial)","bookbinder's bone folder","compass (drafting)",
 "mortar and pestle","wooden plane's tote","fishing creel (wicker, strap)","field microscope","stamp / chop and ink pad",
 "pocket watch (lid, crown, chain)","surveyor's chain","lantern","picnic basket","binoculars (neck strap, two barrels)"]
art2 = ["Mondrian late (Broadway Boogie Woogie, rhythm)","Josef Albers Homage to the Square (colour nests)",
 "Louise Nevelson (one colour, many found boxes)","Donald Judd stacks (repetition, interval)","Joseph Cornell boxes (worlds in a box)",
 "Henri Matisse Jazz (cut paper, rhythm)","Eva Hesse (soft, hung, latex)","Paul Klee (taking a line for a walk)",
 "Shaker gift drawings","Lucie Rie pottery (thin walls, glaze)","Bridget Riley (op-art stripes, vibration)",
 "Alexander Girard (folk colour, pattern)","Ellsworth Kelly (one shape, one colour)","Dan Flavin (light as material)"]
emotions = ["wonder","calm","playfulness","longing","courage","tenderness","mischief","reverence","joy","nostalgia",
 "focus","awe","pride","generosity","shyness","exuberance","melancholy","belonging"]
park = ["on a bench, sharing it","on the grass, cross-legged","under a tree in dappled light","in bright midday sun",
 "at dusk, light fading","by water","with wind","carried on a walk, played in short stops","with a friend joining in",
 "on a picnic blanket next to food","a kid wanders over","hung from a branch while you rest"]
colours = ["oxblood","ochre","sage","ultramarine","persimmon","bone","forest","mustard","slate","coral","ink-black","lichen"]
branches = ["BUTTERFLY","CHAMBER","PIERCED","GROUND"]

print("== one oblique card per branch (to push it), plus one for a new branch ==")
cards = r.sample(oblique, 5)
for b, c in zip(branches + ["NEW"], cards):
    print(f"  {b}: {c}")
print("== new-branch seeds ==")
print("  furniture principle:", r.choice(furniture_principle))
print("  instrument:", r.choice(instruments2))
print("  tool:", r.choice(tools2))
print("  art:", r.choice(art2))
print("  emotion:", r.choice(emotions))
print("  park moment:", r.choice(park))
print("  accent colour:", r.choice(colours))
print("  seed concept:", r.choice(["ONE SHEET", "FOLD"]))
print("== per-branch emotion (one each) ==")
for b in branches:
    print(f"  {b}: {r.choice(emotions)}")
print("== kill test: d20 per branch; <= 4 means argue for killing it seriously ==")
for b in branches:
    print(f"  {b}: {r.randint(1,20)}")
print("== SYNC switch placement twist, d6 ==", r.randint(1, 6))
print("   1 mirror an existing toggle  2 under TIME's skirt as a scale-swap  3 on the jack wall")
print("   4 make it a ring/collar on TIME  5 where TAP is  6 a slider/lever that reveals one scale")
