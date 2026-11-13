# Owner record: the project site (landing page + versions + live work)
Authoritative, verbatim, newest at the bottom.

## 2026-11-13 11:51 — start
Owner (verbatim): "rather than interact through here, i'd like to interact through a web interface that is built on the fly for the versioning and serves as a landing page for the project. can you have a team spec this out? it should live update there as things from here are made and explored, and i want to be able to see the history and versions and see anything that's created (explorations, mocks, layotus, diagrams, etc). it should be shareable and minimal ui in the style of dieter rams / braun"
Recorded as:
- A web interface as the project's landing page and the place he interacts with the work, "rather than interact through here".
- Built on the fly for the versioning; live-updates as work is made and explored in sessions.
- Must show history, versions, and everything created: explorations, mocks, layouts, diagrams, etc.
- Shareable.
- Minimal UI in the style of Dieter Rams / Braun.
- Ask: a team SPECS it out (concept phase first; build after approval).
- Open: how much interaction he means (viewing only, or also giving feedback and answering questions there).

## 2026-11-13 11:52 — interaction depth answered
Owner (verbatim): "chatting here is fine; i just want there to be a site for me to view all the stuff from the team / the versions / the tests / etc as we get further down the build chain"
Recorded as:
- VIEWING site. Conversation and decisions stay in chat; the site doesn't need to take feedback or decisions.
- Must show: everything from the team, the versions, the tests, and more as the project moves down the build chain (spec, BOM, breadboard tests, boards, prints, assembly).

## 2026-11-13 12:06 — sharing
Q: who gets the link; hide owner notes and scores from outside viewers? → Owner (verbatim): "anyone that gets the link is fine to see everything"
DECISION: one view for everyone; nothing hidden from link holders (owner record, scores, notes all visible).
Owner (verbatim): "it is primarily me"
Recorded as: the main viewer is the owner himself; design for him first.

## 2026-11-13 12:13 — on J14 (phone)
Owner (verbatim): "why would i need to read an a3 sheet properly on my phone? i just need to see everything properly on my phone."
Recorded as: J14 is broadened — EVERYTHING on the site must be properly viewable on a phone (sheets, diagrams, docs, tests, records). A3 sheets aren't a special job; they're one case of it. Don't over-invest in a sheet-specific reading mode.

2026-11-13 12:33 Owner (verbatim): "why make anything on a3 at all? im not in europe and im not printing"
Recorded as: drop A3 as the default format for mocks and sheets. Nothing is printed; images are viewed on screen (phone first, per the site's J14). The format is the designers' call, made for on-screen viewing. Locked versions stay as they are.
2026-11-13 12:39 Owner (verbatim): "dont do phone first -- do images that will be great on the site that i can view responsively"
Recorded as: CORRECTION to 12:33 — not phone-first. Images are made to look great on the project site and to work responsively across screen sizes (phone through desktop).
2026-11-13 12:41 Owner (verbatim): "i really only want images for things that need to be images -- text should be html and stuff"
Recorded as: images only for what has to be visual (renders, drawings, diagrams, plots). Text (principles, specs, notes, labels, tables, scores) is real HTML on the site, not baked into images. This retires the "sheet" format (text plus pictures in one image) for new work.

## 2026-11-13 13:13 — on the review images
Owner (verbatim), seeing E Herbarium as frame images: "i dont understand why is this an image and not a webpage"
Recorded as: site concepts are shown to the owner as working web prototypes, not pictures of screens. E Herbarium is being built as a clickable prototype (throwaway, real content) for his review. Approval still pending.

2026-11-13 13:13 Owner (verbatim): "dont render a bunch of images unnecessarily"
Recorded as: render an image only when it is needed to judge or show something; no image sets made by habit, no pictures of web pages.

## 2026-11-13 13:20
Owner (verbatim): "prototypes should go on that webpage i am having you build -- whats the status on that"
Recorded as: prototypes (web or otherwise) are a kind of item the site hosts and shows. Status asked.

## 2026-11-13 13:43 — on the published prototype
Owner (verbatim): "is this site on github or justhere" (answered: hosted on claude.ai; source in the repo)
Owner (verbatim): "i dont understand the nav here"
Recorded as: the Herbarium prototype's navigation (all · stage · kind · version · decisions · history, plus "+ n more") does not make sense to him. Specifics asked.

2026-11-13 16:23 Owner (verbatim): "im going to put the github on github pages so i can easily access it from there instead of here. i want all review and logs and documents there, not here"
Recorded as: the owner will publish the repo with GitHub Pages and view everything there. ALL reviews, logs and documents go in the repo (and so on the Pages site), not as files sent in chat. Hosting for the project site moves from the claude.ai artifact to GitHub Pages (static; it updates when sessions commit and push).
2026-11-13 16:24 Owner (verbatim): "ok thats fine if its not private"
Recorded as: DECISION — a public GitHub Pages site is fine (anyone with the address can see it). Hosting: GitHub Pages from the repo root or a GitHub Action (not /docs).

2026-11-13 16:28–16:29 Owner (verbatim): "re: architecture i think the way its organized is just unclear. have the systems designer take a look. is it up on pages right now? do that first" · "i dont want a bunch of .md docs, i want this stuff on website"
Recorded as: (1) put the site on GitHub Pages first — done as far as a session can: build pushed to branch gh-pages; turning Pages on is blocked from sessions (owner does it in Settings → Pages). (2) The architecture doc's organisation is unclear — systems designer to rework it. (3) Docs, architecture and reviews must be ON THE WEBSITE (rendered pages), not markdown files he has to open. Markdown stays only as the source the site builds from.
2026-11-13 16:40 Owner (verbatim): "gh pages is fine"
Recorded as: DECISION — the site keeps deploying from the gh-pages branch. Sessions rebuild and push it after changes (site/publish.sh).

2026-11-13 16:43 Owner (verbatim), on the live site: "every page here needs a point i literally have no idea what im looking at in "latest" for example. and where do i see the grille options and all of the other options"
Recorded as: every page must state its point (what it is and why you are here) up front; "Latest" does not make sense to him. The site must show the open decisions waiting on him, with their options (e.g. the grille options) and images, in one obvious place.
2026-11-13 16:44 Owner (verbatim): "FYI i have another agent running htis through impeccable to make it look better"
Recorded as: another agent (outside this session) is restyling the site with Impeccable at the same time. Coordinate: pull before editing, keep this team's site changes to content and structure, commit small and often, and publish only from main.
2026-11-13 16:45 Owner (verbatim): "yeah i dont need a latest feed. what i need to decide is valuable. architecture is valuable. featureset is valuable. history is valuable."
Recorded as: DROP the Latest feed. The site's valuable parts, in his words: what he needs to decide; architecture; feature sets; history.
2026-11-13 16:46 Owner (verbatim): "put whatever else i do need in there too im not listing everything. im sure there will need to be one for the parts modeling and physical architecture diagrams... the boards and schematics... parts list... etc etc"
Recorded as: the four sections are a floor, not the full list. Add every section the build will need, e.g. physical design (enclosure, 3D models, physical architecture diagrams), electronics (boards, schematics), parts list (BOM), tests. The team decides the set and shows empty sections honestly as "not yet".
