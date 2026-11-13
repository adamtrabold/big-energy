# Branches jam turn 3: director's draws (real randomness, secrets.SystemRandom).
# Decks differ from draw-systems.py / draw-visual.py. Oblique cards used in any earlier jam removed.
# Run: python3 -I design/branches/draw-director.py
import secrets
r = secrets.SystemRandom()
used = {"Work at a different speed","Only one element of each kind","Cut a vital connection","Use an old idea",
 "Simple subtraction","What wouldn't you do?","Reverse","Remove specifics and convert to ambiguities",
 "What mistakes did you make last time?","Decorate, decorate","Use fewer notes",
 "State the problem in words as clearly as possible","Look closely at the most embarrassing details and amplify them",
 "Water","Spectrum analysis","Humanize something free of error","Disconnect from desire","Listen to the quiet voice",
 "Don't be afraid of things because they're easy to do"}
oblique = ["What would your closest friend do?","What to increase? What to reduce?","Are there sections? Consider transitions",
 "Honor thy error as a hidden intention","Ask your body","Emphasize the flaws","Turn it upside down",
 "Make a blank valuable by putting it in an exquisite frame","Repetition is a form of change","The inconsistency principle",
 "Is the tuning appropriate?","Courage!","Look at the order in which you do things","Change instrument roles","Be dirty",
 "Distorting time","Accretion","Infinitesimal gradations","From nothing to more than nothing","Gardening, not architecture",
 "The most important thing is the thing most easily forgotten","Tidy up","Be extravagant","Breathe more deeply",
 "Go outside. Shut the door.","Faced with a choice, do both","Look at a very small object, look at its centre",
 "Towards the insignificant","Destroy the most important thing","Only a part, not the whole","Give the game away",
 "Emphasize repetitions","Lost in useless territory","Children's voices: speaking, singing","Mute and continue"]
oblique = [o for o in oblique if o not in used]
fields = ["beekeeping (frames, smoker, the hive box)","sailing (cleats, sheets, tiller)","letterpress (furniture, quoins, the chase)",
 "the pochade box (a painter's field easel)","picnic hamper (straps, fitted places)","sundial / gnomon","music box (comb, cylinder, lid)",
 "fly-fishing reel","kite (spars, sail, bridle)","Shaker oval box (swallowtail fingers, copper tacks)","bento (compartments, lid, wrap)",
 "herbarium press (straps, blotters)","bicycle (lugs, saddle, frame triangle)","tent (poles, guy lines, fly)","weather vane",
 "Calder mobile (balance, wire)","Noguchi Akari lamp (paper, light)","Agnes Martin grid (pencil line, near-white)",
 "Matisse cut-outs (scissors drawing colour)","Gee's Bend quilt (improvised blocks)","sashiko mending (running stitch)",
 "Morandi still life (quiet bottles)","Japanese garden stepping stones","birdhouse","hand-cranked coffee grinder"]
emotions = ["wonder","nostalgia","tenderness","playfulness","solitude","mischief","reverence","ease","anticipation","pride"]
park = ["a blanket on a slope","a picnic table with initials carved in it","a fountain's edge","a fallen log","a bandstand",
 "a bench facing a pond at dusk","under a tree in wind","on a bike's rear rack on the way there"]
twists = ["it ages visibly and gets better","you can tell it from 30 m away","a child would know how to open it",
 "it has one moving part you play with while thinking","it makes a sound when you close it","it has a place for your own mark",
 "it is mostly one colour","it is lighter than it looks","it can be repaired in the field","it has a front and a back, both public"]
branches = ["BUTTERFLY","CHAMBER","GROUND","RAIN"]
print("Director oblique:", r.choice(oblique))
print("Own-direction field:", r.choice(fields), "| emotion:", r.choice(emotions), "| park:", r.choice(park))
for b in branches:
    print(f"{b}: twist = {r.choice(twists)} | oblique = {r.choice(oblique)}")
print("Kill test d20 (<=4 argue to kill):", {b: r.randint(1,20) for b in branches})
print("Second field (forced connection):", r.choice(fields))
