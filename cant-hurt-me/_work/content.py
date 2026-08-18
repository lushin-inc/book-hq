# -*- coding: utf-8 -*-
"""
Book HQ durable content artifact — Can't Hurt Me (David Goggins).

Every deliverable reads from this module: the Spoken Companion (.docx),
the Insights + Action Guide (.pdf), and index.html. Nothing downstream
hardcodes content. Pass 2 is a re-render, not a rebuild.

Source: audiobook transcript, Audible / Lioncrest, read by David Goggins
and Adam Skolnick.
"""

SLUG = "cant-hurt-me"
TITLE = "Can't Hurt Me"
SUBTITLE = "Master Your Mind and Defy the Odds"
AUTHOR = "David Goggins"
COVER = "cover.jpg"

# Book shape chosen during the build: sequenced argument with a named
# toolbox. The memoir is ordered so each story earns one tool, and the
# tools stack. Sections are named for the idea, not the chapter.
SHAPE = "sequenced argument, tool per stage"

CENTRAL_QUESTION = (
    "How much of what stops you is real?"
)

CENTRAL_ANSWER = (
    "Almost none of it. The mind runs a governor that shuts you down at "
    "roughly forty percent of capacity, and it does it in the language you "
    "find most persuasive — pain, exhaustion, fear, the story you already "
    "tell about yourself. The governor cannot be argued down and it cannot "
    "be removed. It can only be pushed, in small increments, by voluntarily "
    "doing hard things on a schedule, forever. That work begins with saying "
    "out loud, to your own face, exactly where you are."
)

FRAMEWORK_NAME = "The Indestructible Toolbox"

FRAMEWORK_INTRO = (
    "A disadvantaged life forced the construction of a mental toolbox that "
    "theory could not supply. Each tool was earned in a specific place, "
    "under load, and each one stacks on the last."
)

FRAMEWORK = [
    {
        "name": "The Accountability Mirror",
        "line": "Say the true thing out loud, to your own face, every day. "
                "Tag the mirror with the next small step, not the dream.",
    },
    {
        "name": "The Calloused Mind",
        "line": "Repetition, not revelation. Do something that sucks every "
                "day until the doing of it stops being a decision.",
    },
    {
        "name": "The Armored Mind",
        "line": "Go back to the source of the fear and own it. A callus on a "
                "cracked foundation still collapses.",
    },
    {
        "name": "Taking Souls",
        "line": "Bring your very best at the hour you feel your worst. The "
                "advantage is tactical, and it is mostly played on yourself.",
    },
    {
        "name": "The Cookie Jar",
        "line": "Stock your past victories on purpose. Mid-effort, reach in "
                "and re-enter the feeling of one — not the memory of it.",
    },
    {
        "name": "The 40% Rule",
        "line": "The stop signal arrives at forty percent. Take the next five "
                "percent, then the next, and the ceiling moves.",
    },
    {
        "name": "The After Action Report",
        "line": "Write the live autopsy longhand. Positives first, then the "
                "mindset audit, then the date of the next attempt.",
    },
    {
        "name": "What If",
        "line": "The answer to every ceiling somebody else sets for you, and "
                "to every one you set for yourself.",
    },
]

# ---------------------------------------------------------------------------
# INSIGHTS — six maximum. Continuous prose under a title; never labeled subheads.
# ---------------------------------------------------------------------------

INSIGHTS = [
    {
        "id": "insight-01",
        "image": "insight-01.png",
        "title": "The Governor Is Set at Forty Percent",
        "body": (
            "A stock car has a governor bolted into it — a device that "
            "restricts fuel and air so the engine never runs hot enough to "
            "destroy itself. Remove it and the car goes far faster than the "
            "factory ever advertised. Human beings have one too, except it is "
            "not hardware. It is software, buried in the mind, wound into "
            "identity. It has read your whole life story. It knows what you "
            "love, what you fear, and precisely which excuse you will accept, "
            "and it delivers its verdict in the only currencies you cannot "
            "ignore: pain, exhaustion, fear, insecurity.\n\n"
            "Most people quit at around forty percent of maximum effort. Not "
            "forty percent of what they think they can do — forty percent of "
            "what is actually there. Even at the moment that feels like the "
            "absolute limit, sixty percent is still in the tank. This is the "
            "forty percent rule, and Goggins is careful to say he made it up. "
            "It came out of a hundred-mile trail race in the mountains above "
            "Honolulu, run by a road runner who had never set foot on a trail, "
            "in running shoes with almost no tread, on a course with "
            "twenty-four thousand five hundred feet of climbing. On the fourth lap, with the tank apparently empty, the "
            "move that worked was not a burst of willpower. It was shrinking "
            "the race: get to that crest, then quit. Get to the next landmark, "
            "then quit. Each of those little bargains bought back about five "
            "percent, and five percent at a time is how the ceiling moves.\n\n"
            "The catch is that the governor cannot be disabled the way a "
            "mechanic disables one. There is no download. It takes twenty "
            "years to gain twenty years of experience, and the only method is "
            "to chase discomfort day after day until the mind learns, through "
            "sheer accumulated evidence, that it survives things it swore it "
            "would not. In practice this changes what the stop signal means. "
            "It stops being a verdict and becomes a data point — the "
            "governor talking, right on schedule, at forty percent."
        ),
    },
    {
        "id": "insight-02",
        "image": "insight-02.png",
        "title": "Denial Is the Ultimate Comfort Zone",
        "body": (
            "Cheating started in the third grade and, by his own count, ran a "
            "good eight years. "
            "Copied homework, scanned neighbors' tests, answers lifted even on "
            "standardized tests that did not affect a grade. It worked — "
            "scores rose, the calls home stopped, and the whole thing felt "
            "like a system being gamed. It was not. It was a fourth-grade "
            "reading level being carried, undetected, toward a senior year, "
            "and the bill came due in a single envelope: over a quarter of the "
            "school year missed, a D average, no graduation without "
            "significant improvement.\n\n"
            "What happened that night is the first tool in the book and the "
            "one everything else is built on. Steam wiped off a corroded "
            "bathroom mirror, and then a conversation held out loud, at "
            "volume, with the reflection. You read like a third grader. You "
            "stand for nothing. Nobody is coming to save you — not your "
            "mother, not anyone. This is not a self-love exercise and it will "
            "not work if you soften it. The tone is the active ingredient. "
            "Massage the ego and the mirror tells you nothing you did not "
            "already want to hear.\n\n"
            "The mechanism that makes it operational is smaller than the "
            "speech. Goals go on sticky notes, on the actual glass, and they "
            "are broken down until they are boring. Not lose forty pounds — "
            "lose two pounds this week. When that note comes down, the next "
            "one goes up. The mind runs to the path of least resistance by "
            "default, which is why the reminder has to be physical, in the "
            "room, at eye level, every morning. Denial is comfortable. That is "
            "the entire problem with it, and the reason it has to be attacked "
            "somewhere as unforgiving as a mirror."
        ),
    },
    {
        "id": "insight-03",
        "image": "insight-03.png",
        "title": "Motivation Is Crap",
        "body": (
            "Motivation is kindling. It burns bright, it burns out, and it is "
            "gone the first genuinely bad morning. Picture a December day in "
            "Chicago, the windchill hitting your face at the door, and a run "
            "scheduled. A motivated "
            "person opens the door, feels the cold, closes the door and sits "
            "back down. A driven person opens the door, feels the cold, closes "
            "the door — and goes to put on warmer clothes. Same weather. Same "
            "door. The difference is not feeling. It is whether the decision "
            "was ever open for discussion.\n\n"
            "This is why self-discipline is the only thing that scales. In "
            "under three months, one hundred and six pounds had to come off a "
            "two-hundred-and-ninety-seven-pound body, and a test that had once "
            "been scored a twenty out of ninety-nine had to be passed at a "
            "much higher standard. The method was not inspiration. It was a "
            "clock: up at four-thirty, two hours on a cheap stationary bike "
            "with study books propped on a folding table, two hours in a pool, "
            "a gym circuit built on hundreds of light reps because bulk was "
            "the enemy, two more hours on the bike, one real meal, two more "
            "hours on the bike. Weighed twice a day. Repeated.\n\n"
            "The standard inside that schedule matters more than the schedule "
            "itself. One night, after a six-mile run, a swim and three hours "
            "of lifting, a max set of pull-ups came up one short of the number "
            "called — eleven instead of twelve. It gnawed through dinner. The "
            "answer was to drive back to the gym and repeat the entire pull-up "
            "workout, another two hundred and fifty reps, to pay for the one. "
            "The logic is worth keeping: physical suffering tonight is cheaper "
            "than lying awake later wondering whether the rep you skipped is "
            "the reason you missed."
        ),
    },
    {
        "id": "insight-04",
        "image": "insight-04.png",
        "title": "Bring Your Best When You Feel Your Worst",
        "body": (
            "Wednesday is the worst day of Hell Week, and everyone in Navy "
            "SEAL training knows it, which is part of why it is true. Men "
            "arrive tired on schedule because seventy years of lore told them "
            "Wednesday is when you get tired. By that point the class had been "
            "awake for days, skin rubbed raw, a knee swollen to the size of a "
            "grapefruit, and the boat raises had gone from crisp to dragging. "
            "Nine instructors stood on the beach, warm, holding coffee, "
            "watching it happen.\n\n"
            "The move was to stop lifting the boat and start throwing it — up, "
            "caught overhead, tapped to the sand, up again — with the crew "
            "chanting that you can't hurt Boat Crew Two. Instructors' mouths "
            "came open. Some looked away. The point was never the boat. It was "
            "to occupy real estate in the heads of men who were, at that "
            "moment, silently comparing this class to their own worst night. "
            "Show them your best at the exact hour that was their worst, and "
            "something cracks in them instead of in you.\n\n"
            "Two things keep this from being a stunt. The first is that the "
            "game is mostly played on yourself — outside physical competition, "
            "the opponent never needs to know it is happening, and the real "
            "measure is stringing seconds together until you last longer than "
            "your opponent thinks you can. "
            "The second is timing, learned by getting it wrong. At a "
            "three-day stage race in Hawaii, the front of a double marathon "
            "was run fast on purpose so rivals would hear the splits and give "
            "up. They did not. One of them simply waited, held his own pace, "
            "and collected the win by ten minutes. You take a soul at the end "
            "of the race, not the beginning. And in a workplace rather than a "
            "surf zone, it is done with humility or it curdles into something "
            "that makes people hate you."
        ),
    },
    {
        "id": "insight-05",
        "image": "insight-05.png",
        "title": "The Cookie Jar",
        "body": (
            "However broke the family got, the cookie jar stayed stocked — "
            "wafers, Oreos, Milanos, all dumped in together, and "
            "choosing one was a small treasure hunt. That jar got rebuilt "
            "internally and filled with something else: past victories, "
            "catalogued on purpose, available for withdrawal under load.\n\n"
            "The distinction that makes it work is easy to miss. This is not a "
            "highlight reel and it is not a memory file. Reaching in means "
            "re-entering the emotional state of the win — what it actually "
            "felt like in the body at the moment of overcoming — not merely "
            "recalling that it happened. Done that way, he says, it reaches "
            "the sympathetic nervous system: adrenaline arrives, the pain "
            "recedes for a while, the pace lifts. Done as a list, it does "
            "nothing.\n\n"
            "What goes in the jar is broader than trophies. Obstacles count — "
            "quitting smoking, coming through a depression, beating a "
            "stutter. So do the small wins on the way to a big one, because "
            "nobody drops a hundred pounds without first losing five in a "
            "week, and nobody learns to read at grade level without first "
            "understanding every word in a single paragraph. And the jar has "
            "to be stocked before you need it, because the moment you need it "
            "is not a moment when you can think clearly. That is the whole "
            "reason it exists: life does not pick you up when you fall, so you "
            "build the system that reminds you, mid-fall, exactly who you are "
            "when you are at your best."
        ),
    },
    {
        "id": "insight-06",
        "image": "insight-06.png",
        "title": "Failure Is the Only Honest Data",
        "body": (
            "The military fills out an after action report following every "
            "mission and every field exercise, win or lose. Applied to a "
            "personal failure it becomes a live autopsy, written longhand — "
            "not typed, not held in the head — and it has a specific order "
            "that most people get backwards. It opens with everything that "
            "went right. Be detailed and be generous; it is rarely all bad, "
            "and starting with the obvious wound guarantees you never see the "
            "rest of the body.\n\n"
            "A twenty-four-hour pull-up record took three attempts. The first "
            "ended at two thousand five hundred reps on a television set, on a "
            "bar with too much give, after a ten-minute break that never "
            "closed. The second ended at roughly three thousand two hundred in "
            "a Nashville gym, both palms filleted open to the dermis. The "
            "report written after that second failure did not start with the "
            "hands. It started with what worked — the gym, the tape and chalk, "
            "the seven hundred additional reps the harder bar had bought, the "
            "fact that no one had been blamed. Only then came the audit that "
            "mattered: preparation and determination had never wavered, but "
            "belief had been shakier than was comfortable to admit.\n\n"
            "That audit produced three changes and one decision. Start slower "
            "to go further. Cap any break at four minutes, because the wall "
            "arrives near hour ten and both failures had involved longer "
            "stops. Change the only variable left — hand protection — with "
            "custom foam pads. And decide, in advance, that the record was "
            "already owned; the only open question was the date. Two months "
            "later it fell at four thousand and thirty. The report is the "
            "reason. Written honestly, failure is the only feedback in your "
            "life that cannot be faked, flattered, or negotiated with."
        ),
    },
]

# ---------------------------------------------------------------------------
# ACTIONS — five maximum.
# ---------------------------------------------------------------------------

ACTIONS = [
    {
        "id": "action-01",
        "image": "action-01.png",
        "title": "Build the Accountability Mirror",
        "what": (
            "Write your bad hand out first — in a journal, in full, in minute "
            "detail. What you contended with growing up, and what is limiting "
            "you right now, including the ways you are standing in your own "
            "way. If your limitation is that you had it easy and were never "
            "pushed, write that. Then move to the mirror itself, which is not "
            "optional and not digital: sticky notes on the actual glass. Put "
            "your insecurities, your goals and your next required step on "
            "them, and speak to your reflection out loud, at volume, without "
            "softening anything. Break every goal down until the note is "
            "almost embarrassingly small — not lose forty pounds, but lose two "
            "pounds this week. Take that note down when it is done and put up "
            "the next one."
        ),
        "when": (
            "Every day, at the same point in your routine — shaving, brushing "
            "teeth, whatever already happens in front of that mirror. Do the "
            "written inventory once, then revisit it whenever the notes stop "
            "producing discomfort."
        ),
        "success": (
            "A note comes down roughly every week, and the one that replaces "
            "it is harder. You can state your actual position out loud without "
            "flinching or negotiating with it."
        ),
        "caution": (
            "The tone is the tool. Kept kind, this becomes affirmation and "
            "does nothing. Kept cruel with no next step attached, it becomes "
            "self-punishment, which also does nothing. Every hard truth on "
            "that glass needs a small, dated action beside it."
        ),
    },
    {
        "id": "action-02",
        "image": "action-02.png",
        "title": "Schedule One Thing That Sucks, Daily",
        "what": (
            "List everything you avoid, with a mark beside the items you know "
            "are good for you. Pick one. Do it. Do it again tomorrow. Keep it "
            "at the micro level — make the bed properly, do the dishes, iron "
            "the shirt, get up before dawn and run two miles — and only "
            "escalate once the current version has stopped costing anything. "
            "Then put it on a clock. Map your day in blocks, including the "
            "dead space, and place the uncomfortable thing inside a block with "
            "a start time, the way you would place a meeting you cannot move."
        ),
        "when": (
            "Daily, without exception, and hardest on the days you least want "
            "to. Rebuild the block map for about three weeks until the "
            "schedule holds without sacrificing sleep."
        ),
        "success": (
            "The discomfort is no longer a decision you make each morning, and "
            "the item that felt hard six weeks ago now reads as a warm-up. "
            "Skipping one starts to bother you all day."
        ),
        "caution": (
            "This is not a transformation on a deadline. It is the needle "
            "moving a little at a time, sustainably. Going from nothing to "
            "everything in a week is how people injure themselves and quit."
        ),
    },
    {
        "id": "action-03",
        "image": "action-03.png",
        "title": "Stock the Cookie Jar Before You Need It",
        "what": (
            "Open a journal and write out your wins — but not as a trophy "
            "list. Include obstacles you overcame, not just achievements. "
            "Include the things you failed at first and got on the second or "
            "third attempt. Include small wins that were steps toward "
            "something larger. For each one, sit with it long enough to "
            "remember what it felt like in your body to come through it, "
            "because the feeling is the thing you will withdraw later, not the "
            "fact. Then use it deliberately: set an ambitious target for your "
            "next hard session, and when the pain or boredom or doubt arrives "
            "and tries to stop you short, reach in, pull one out, and let it "
            "carry the next stretch."
        ),
        "when": (
            "Stock it on a calm day. Use it at the exact moment you decide you "
            "are done — which is the moment you will be least capable of "
            "generating it from scratch."
        ),
        "success": (
            "Mid-effort, you can name a specific past victory and feel a "
            "measurable lift from it. Over time the jar fills faster than you "
            "empty it, because each hard thing you finish goes in."
        ),
        "caution": (
            "This is not a session of congratulating yourself. The purpose is "
            "not to feel good about the past; it is to convert the past into "
            "usable energy for something happening right now."
        ),
    },
    {
        "id": "action-04",
        "image": "action-04.png",
        "title": "Take the Next Five Percent",
        "what": (
            "Before the attempt, rehearse it. Picture what success looks and "
            "feels like — and then, just as deliberately, picture every specific "
            "obstacle likely to arrive and decide in advance how you will "
            "answer each one, because the unaccounted-for problem is the one "
            "that ends you. Have your answer to the simple "
            "question ready before you need it: why am I doing this? Then, in "
            "the effort itself, go to the point where your mind is asking you "
            "to stop, and add five to ten percent. A hundred push-ups becomes "
            "a hundred and five. Thirty miles a week becomes thirty-three. "
            "That number is now your baseline, and next week you add another "
            "five percent to that."
        ),
        "when": (
            "In physical training first, because the feedback is immediate and "
            "unarguable, and the inner dialogue you learn to command there "
            "transfers to work and school."
        ),
        "success": (
            "Your stopping point keeps moving, injury-free, and the first "
            "surge of pain starts registering as information arriving on "
            "schedule rather than as a verdict."
        ),
        "caution": (
            "Goggins is emphatic that this is the one place not to copy his "
            "method: he arrived at the rule by destroying his own body, and "
            "spent years taping and wedging his feet to keep running. Five to "
            "ten percent, gradually, is the instruction. Zero to a hundred "
            "will hurt you. And you will never reach a hundred percent — "
            "that is the point of it."
        ),
    },
    {
        "id": "action-05",
        "image": "action-05.png",
        "title": "Write the After Action Report by Hand",
        "what": (
            "Take your most recent failure and your most painful one. Longhand "
            "in a journal, not on a screen. Start with everything that went "
            "well, in detail and generously. Then write how you handled the "
            "failure afterward and what it cost your life and relationships. "
            "Then audit your mindset separately in preparation and in "
            "execution, because that is where most people actually fall short. "
            "Then list what can be fixed, with no softening. Then open your "
            "calendar and schedule the next attempt. If the failure is old and "
            "cannot be repeated, write the report anyway — the findings "
            "transfer to whatever you attempt next."
        ),
        "when": (
            "As soon as the sting is real but before the story hardens — "
            "within days, not months. Keep the report beside you while you "
            "prepare for the retry, and make the corresponding changes on your "
            "accountability mirror."
        ),
        "success": (
            "The retry has specific, named changes traceable to the report, "
            "and you can describe the failure without either blaming anyone or "
            "flinching from your own part in it."
        ),
        "caution": (
            "Skipping straight to what went wrong feels efficient and ruins "
            "the exercise. The positives are not a consolation prize; they are "
            "the assets you will build the next attempt on."
        ),
    },
]

# ---------------------------------------------------------------------------

DEFINITIONS = [
    ("The governor",
     "The mental limiter that shuts you down well before your true capacity, "
     "using pain, exhaustion, fear and identity as its levers."),
    ("The 40% rule",
     "The claim that most people stop at about forty percent of what they "
     "have, and that the remaining sixty is reachable in increments."),
    ("Accountability mirror",
     "A daily out-loud conversation with your own reflection, with the next "
     "required step written on sticky notes stuck to the glass."),
    ("Calloused mind",
     "The toughness built by repeated voluntary discomfort, the way repeated "
     "friction builds a callus on a palm."),
    ("Armored mind",
     "A calloused mind resting on a foundation that has been repaired — the "
     "past faced and owned rather than swept under the rug."),
    ("Cookie jar",
     "A deliberately stocked store of past victories, drawn on mid-effort by "
     "re-entering the feeling of one."),
    ("Taking souls",
     "Gaining a tactical advantage by performing at your best precisely when "
     "you and everyone watching expect you to be at your worst."),
    ("After action report",
     "A written, longhand autopsy of a failure — positives first, then "
     "mindset, then fixes, then the date of the next attempt."),
    ("BUD/S",
     "Basic Underwater Demolition/SEAL training: six months, three phases, "
     "with Hell Week in week three."),
    ("Hell Week",
     "About one hundred and thirty hours of continuous training on almost no "
     "sleep, the attrition point of SEAL selection."),
    ("Ultra",
     "Any foot race longer than a marathon; the events here run from one "
     "hundred kilometres to one hundred and thirty-five miles."),
    ("Uncommon amongst uncommon",
     "Standing out inside a room where everyone is already exceptional — a "
     "wolf surrounded by wolves rather than a big fish in a small pond."),
]

ALT = {
    "insight-01": "A cutaway fuel tank still two thirds full, its gauge needle hard "
                  "against E, and a screw clamp pinching the feed pipe to the engine.",
    "insight-02": "A full-length mirror under a sheet that bulges into a figure far "
                  "larger than the stick figure beside it, who holds one corner "
                  "without lifting it.",
    "insight-03": "The same wind crossing a match drawn three times as it burns down "
                  "to a stub, and a steady flame on a wick that does not go out.",
    "insight-04": "A whiteboard showing a line sloping down under the word Wednesday, "
                  "and a boat's arc rising over the top edge of the board while the "
                  "instructor's coffee spills.",
    "insight-05": "One jar between two stick figures: a calm one dropping folded slips "
                  "in, a doubled-over one pulling a slip out.",
    "insight-06": "A chain of ten links with a magnifying glass filled entirely by the "
                  "one snapped link, the nine intact links ticked and ignored outside "
                  "the lens.",
    "action-01": "A mirror covered in sticky notes, one finished note being peeled off "
                 "toward a waste basket while a fresh note goes up in its place.",
    "action-02": "A day drawn twice as a column: solid and full on the left, broken "
                 "into blocks on the right with the empty gaps exposed and one claimed "
                 "for the hard thing.",
    "action-03": "A near-bare trophy shelf above a stick figure, with an overflowing "
                 "jar of labelled slips at his feet.",
    "action-04": "A ratchet wheel with teeth numbered 100, 105, 110 and 115, a pawl "
                 "holding it against slipping back, and a hand pushing the lever one "
                 "tooth.",
    "action-05": "A handwritten report — what held, how I thought, what to fix — "
                 "ending in a circled calendar date with an arrow curving back to a "
                 "starting line.",
}

CLOSING_LINE = "How do you want your book to read at the end of your life?"

# Quick reference — rendered by the PDF only; the web page has no One page tab.
QUICK_REFERENCE = [
    {"kind": "line", "label": "The question", "text": CENTRAL_QUESTION},
    {"kind": "line", "label": "The answer",
     "text": "The stop signal arrives at about forty percent of what you have. It is "
             "the governor talking, not the tank reading empty."},
    {"kind": "line", "label": "The method",
     "text": "Voluntary discomfort on a schedule, five percent at a time, forever."},
    {"kind": "line", "label": "The starting point",
     "text": "Say the true thing out loud, to your own face, with the next small step "
             "written on the glass."},
    {"kind": "list", "label": "The toolbox", "items": [
        "Accountability mirror — truth out loud, daily; next step on a sticky note.",
        "Calloused mind — something that sucks, every day, on purpose.",
        "Armored mind — face the source; a callus on a cracked foundation collapses.",
        "Taking souls — your best at the hour you feel your worst. Late, not early.",
        "Cookie jar — stock the wins; withdraw the feeling, not the fact.",
        "The 40% rule — the stop signal is not the limit. Take five percent more.",
        "After action report — longhand, positives first, then a date for the retry.",
        "What if — the reply to every ceiling anyone sets for you.",
    ]},
    {"kind": "list", "label": "Standing orders", "items": [
        "Nobody is coming. Not family, not luck, not a mentor. That is the good news.",
        "Motivation is kindling. It will not survive a cold morning. Discipline will.",
        "Denial is comfortable, which is why it has to be attacked at a mirror.",
        "Don't race anybody — you can't find your limit running someone else's race.",
        "Visualize the obstacles, not just the win. The unrehearsed problem ends you.",
        "Quitting is not instant. The decision is made hours earlier. Catch it there.",
        "Don't do it his way. He found the rule by wrecking himself. Five percent.",
        "There is no finish line. That is the deal you are accepting.",
    ]},
]

# Image slots, in the order the guide illustrates them.
IMAGE_SLOTS = (
    [(i["id"], i["image"], i["title"]) for i in INSIGHTS] +
    [(a["id"], a["image"], a["title"]) for a in ACTIONS]
)

EDITORIAL_NOTES = [
    "Health, medical and physiological claims are attributed to Goggins or "
    "his doctors throughout and never carried in the companion's own voice.",
    "The ten in-book challenges are consolidated into five actions. "
    "Challenge 1 folds into the mirror, challenge 5 into the fifth-percent "
    "preparation step, challenge 8 into the daily discomfort schedule.",
    "Speech-to-text garbles in the transcript were corrected to real-world "
    "spellings: Trunnis Goggins, Wilmoth Irving, Scott Gearen, Chris Kostman, "
    "Karl Meltzer, Stephen Hyland, Nandor Tomaska, Joe Hippensteel, BUD/S, "
    "ASVAB, DEVGRU, Motrin. The Navy recruiter's surname follows the "
    "transcript's own consistent spelling, Shaljo — the one name that could "
    "not be confirmed against an outside source.",
    "The action-01 plate is the first-round drawing, kept because it reads "
    "better than its replacement; its lettering says TAG THE MIRROR.",
]


# ---------------------------------------------------------------------------
# BOOK — what pipeline/build_page.py injects into page_template.html.
# Assembled from the fields above so there is one source for every string.
# ---------------------------------------------------------------------------

def _paras(body):
    return [p for p in body.split("\n\n") if p.strip()]


def _entry(e, kind):
    n = int(e["id"].split("-")[1])
    out = {
        "id": "%s-%d" % (kind, n),
        "title": e["title"],
        "plate": "img/" + e["image"],
        "alt": ALT[e["id"]],
    }
    if kind == "insight":
        p = _paras(e["body"])
        out["lede"] = p[:1]
        out["evidence"] = p[1] if len(p) > 1 else ""
        out["operative"] = p[2] if len(p) > 2 else ""
    else:
        out["lede"] = [e["what"], e["when"]]
        out["operative"] = e["success"]
        if e.get("caution"):
            out["caveat"] = e["caution"]
    # keep key order matching the reference implementation
    order = (["id", "title", "lede", "evidence", "operative", "plate", "alt"]
             if kind == "insight" else
             ["id", "title", "lede", "operative", "caveat", "plate", "alt"])
    return {k: out[k] for k in order if k in out}


BOOK = {
    "title": TITLE,
    "author": AUTHOR,
    "subtitle": SUBTITLE,
    "cover": "img/" + COVER,
    "links": [
        {"mark": "\u2193", "label": "Spoken companion", "href": "Spoken_Companion.docx"},
        {"mark": "\u2197", "label": "Speechify",
         "href": "https://speechify.app.link/PAJaS84kG5b"},
    ],
    "argument": {
        "question": CENTRAL_QUESTION,
        "answer": CENTRAL_ANSWER,
    },
    "framework": {
        "name": FRAMEWORK_NAME,
        "intro": FRAMEWORK_INTRO,
        "steps": [
            {"mark": "%02d" % (n + 1), "term": f["name"], "gloss": f["line"]}
            for n, f in enumerate(FRAMEWORK)
        ],
    },
    "insights": [_entry(i, "insight") for i in INSIGHTS],
    "actions": [_entry(a, "action") for a in ACTIONS],
    "vocabulary": {
        "intro": "The vocabulary the book runs on. Most of it is Goggins's own, and "
                 "the words do real work — a calloused mind and an armored mind are "
                 "not the same thing.",
        "terms": [
            {"id": "v-" + term.lower().replace(" ", "-").replace("/", "-")
                          .replace("%", "pct").replace(".", ""),
             "term": term, "def": desc}
            for term, desc in DEFINITIONS
        ],
    },
    "quickReference": QUICK_REFERENCE,
    "closingLine": CLOSING_LINE,
}


# ---------------------------------------------------------------------------
# SPOKEN COMPANION — narrative body. The .docx renders from this list.
# level 1 = Heading 1 (part), level 2 = Heading 2 (section).
# ---------------------------------------------------------------------------

COMPANION_TITLE = "Can't Hurt Me"
COMPANION_FOOTER = "Can't Hurt Me — Spoken Companion"

COMPANION = [
{"level": 1, "heading": "The Bad Hand"},

{"level": 2, "heading": "Take the Inventory in Full", "paras": [
 "Life isn't fair. It was never supposed to be. Once you accept that it is coming for you one way or another, you can start preparing — and preparation begins with naming what you were actually handed, in detail, without softening it.",

 "In 1981 the Goggins family lived on one of the leafiest streets in Buffalo, New York, with a Rolls-Royce and a Mercedes in the garage. Glossy surfaces reflect much more than they reveal. The money came from a roller rink his father, Trunnis, ran in East Buffalo, worked every night by the whole family and controlled entirely by him; his mother had no bank account of her own. The violence was routine. Trunnis whipped his wife with a belt, buckle first, and when David at six jumped on his father's back and clawed at his eyes, he got the belt too.",

 "Ask Goggins why he put one particular beating in the book, and the answer turns out not to be about him. He had come home from an afternoon at a harness track, an afternoon that was supposed to have been his first Cub Scout meeting. The protocol was to undress, walk to his father's bedroom, lie across the corner of the bed in the dark and wait, because the waiting is worse than the belt. The welts ran from his neck to the backs of his knees, and he missed several days of school. He didn't cry. What he remembers is not the pain. It is his mother pulling back the covers and seeing his body, and the look on her face, which he says is still tattooed on him. He chose those beatings because they chart her destruction rather than his.",

 "She got out. Eight-year-old David arrived at his grandparents' house in Brazil, Indiana with nothing, and public housing came next: six hundred square feet, seven dollars a month. He had wet the bed nearly every night in Buffalo, and never did it again after the first night in Indiana.",

 "All of that is a fact whether he likes it or not, which is the only reason the exercise works. Once it is fact, the job is to find the power inside it. The odds stacked against you become a runway.",
]},

{"level": 2, "heading": "Denial Is the Ultimate Comfort Zone", "paras": [
 "He started cheating in the third grade and, by his own count, kept it up for a good eight years. Copied homework, scanned the tests of whoever sat next to him, lifted answers even on standardized tests that had no effect on his grade. It worked beautifully. Scores went up, the calls home stopped, and it felt like a system being gamed. It wasn't. It was a fourth-grade reading level smuggled undetected into a senior year of high school, and the bill came in a single envelope: a D average and no graduation without significant improvement.",

 "What happened that night is the first tool in the book and the one every other tool is built on. He wiped the steam off a corroded bathroom mirror and had a conversation with his reflection, out loud and at volume, while shaving his face and then his scalp. You read like a third grader. You stand for nothing. You have never tried hard at anything but basketball. Nobody is coming to save you. Not your mother, not anybody.",

 "That is not a self-love exercise and it does not work if you soften it. The tone is the active ingredient. Massage the ego and the mirror will only tell you what you already wanted to hear. The mechanism that made it operational, though, is smaller than the speech. The goals went onto sticky notes stuck to the actual glass, broken down until they were almost boring. Not lose forty pounds. Lose two pounds this week. When that note comes down, the next one goes up. The mind runs to the path of least resistance by default, which is exactly why the reminder has to be physical, at eye level, every single morning.",
]},

{"level": 2, "heading": "Motivation Is Crap", "paras": [
 "Motivation is kindling. It burns bright, it burns out, and it will not survive the first genuinely bad morning. Picture a December day in Chicago, the windchill hitting your face as you open the door, and a run on the schedule. A motivated person opens the door, feels the cold, closes it and sits back down. A driven person opens the door, feels the cold, closes it, and goes to put on warmer clothes. Same weather, same door. The difference is not how they feel. It is whether the decision was ever open for discussion.",

 "Self-discipline is the only thing that scales, because it does not depend on a mood being available. Goggins failed the military entrance exam badly as a teenager, scoring twenty out of ninety-nine against an Air Force minimum of thirty-six. A nun had worked out years earlier that he learned by repetition rather than by being labelled, and a tutor his mother found him turned that into a system: read a page of a textbook, write the whole page out longhand, then do it again, then a third time. He went from a fourth-grade reading level to a high school senior's in six months and passed the test on his third attempt.",

 "It decides who you keep around you, too: not the friends who validate you, but the people who hold you to a higher standard than you would hold yourself.",
]},

{"level": 1, "heading": "Callousing the Mind"},

{"level": 2, "heading": "The Impossible Task", "paras": [
 "He enlisted in the Air Force at nineteen weighing a hundred and seventy-five pounds. Four years later he was discharged at close to three hundred, working nights as an exterminator in the back kitchens of Indianapolis restaurants. He wore the fumigation mask partly because it made him impossible for anyone to see. Especially himself. He had walked away from the pararescue pipeline on a medical exit he could have refused, and let it stand rather than restart. On paper he had not quit. He knew the truth.",

 "What woke him was a documentary. Home from a shift, he watched a Navy SEAL training class go through Hell Week, then looked in a mirror at a man for whom mediocrity would have been a major promotion. For almost three weeks after that he called Navy recruiters across the country every morning after work, and every one of them turned him down; one office met him in person and laughed in his face. Then he reached a reserve recruiter named Steven Shaljo, who weighed him at two hundred and ninety-seven pounds against a Navy maximum for his height of a hundred and ninety-one, and told him the program that could get him to SEAL training was closing at the end of the year. He had less than three months to lose a hundred and six pounds, and he had to pass the entrance exam again at a far higher standard.",

 "He studied all day and sprayed pests all night for two weeks, took the test, and came up short in one section: a forty-four where he needed a fifty. He would have to sit the whole exam again. That is the doubt he carried into work the night the job broke him. He sprayed up through a gap under a sink into what turned out to be a nesting column, and roaches poured out of an open ceiling panel onto his neck and shoulders and head, with the floor writhing under him. He walked out, opened the dumpster to throw away the dead rodents, and a live raccoon lunged at him out of the dark. He left his gear where it lay and drove home.",

 "The first run went four hundred yards. He had set out to do four miles, hadn't run in over a year, and ended up sitting on the edge of a golf course, dizzy, then walking home to a melted milkshake and crying. What he did next was pull out a beat-up video tape and fast-forward to the fourteenth round, where Rocky is on the canvas with his trainer telling him to stay down, and gets up at the count of six and waves the champion back in. He poured out the milkshake, laced up, and went back out. The first attempt stopped at a quarter mile. The second went a full mile. The lesson from that hour is the whole book in miniature: not every physical and mental limit is real, and he had a lifelong habit of giving up far too soon.",

 "The schedule that followed was not inspiration. It was a clock. Awake at four-thirty, onto a cheap stationary bike with the exam books propped on a folding table for two hours. Two hours in a pool. A gym circuit of five or six sets of a hundred to two hundred reps, because bulk was the enemy. Two more hours on the bike, one real meal, then two more. Twenty-five pounds gone in two weeks. Some mornings he stared at his running shoes for thirty or forty minutes before he could start.",

 "One night that winter, after six miles of running, a swim and three hours in the gym, he went for a max set of pull-ups aiming at twelve and stopped at eleven. It gnawed at him through dinner, so he drove back and repeated the entire pull-up workout — another two hundred and fifty reps — to pay for the one. Physical suffering tonight is cheaper than lying awake later wondering whether the rep you skipped is the reason you missed.",

]},

{"level": 2, "heading": "Repetition, Not Revelation", "paras": [
 "The word callous is not a metaphor he reached for. His palms tore open the first day he touched a barbell, and thousands of repetitions later they were armored. The mind works the same way, and hardship is the friction. What is not automatic is where the callus lands, because the same experience can harden into resentment — suspicious, angry at the world, afraid of change — or into a mind that is hard without being closed. Choosing to stay a victim of circumstance into adulthood produces the first one.",

 "The signature act of that year was quiet. He fractured both shins during his third attempt at Hell Week and still had months of training left. So he woke at three-thirty in the morning, drove to base alone in the dark, and taped his own legs: a thick tube sock, duct tape looped from heel over ankle and back, working down the foot and up the calf, then a second sock and a second layer, then the boot laced over the top, until both lower legs were sunk into soft casts. It took about an hour. He ran off his hip flexors rather than letting his feet set the rhythm. The first thirty minutes were the worst pain of his life. The sentence that got him through was not a slogan he read anywhere. Every step you run from now until the end will only make you harder. At the forty-minute mark the tape loosened, the muscle warmed, and the pain receded to low tide. It came back through the day, but it was manageable. Then he did it again the next morning, and the morning after that.",
]},

{"level": 2, "heading": "A Callus on a Cracked Foundation", "paras": [
 "A calloused mind is not enough on its own. The counterexample is a superior natural athlete in his class who spent Hell Week grinding down his own boat crew on purpose, and who — by his own unsparing account afterward — was an insecure man whose ego made his own life harder. He rang the bell on Monday night, reporting stress fractures that were not there.",

 "He had plenty of callus. What he did not have was a foundation. Most people sweep their worst material under the rug, and when a hard season comes the rug lifts and all of it comes back out and quietly makes the decisions. Character is the foundation, and a mind hardened on top of a cracked one still collapses.",

 "The repair happened on a couch in his mother's house at what looked like the lowest point of his life: a fractured kneecap, a warning that this was his last permitted attempt at SEAL training, thirty thousand dollars in credit card debt, no address, no car, and an ex-wife who had just turned up to tell him she was pregnant. He cried for hours. His mother told him she couldn't argue with any of it, but that she knew him well enough to know he would find a way through. And that night he did the work he had avoided for twenty years. He had been telling people, including men he trained with, that his father was dead. He stopped. Accepting Trunnis Goggins as part of himself was what freed him to use where he came from as fuel. Until then he had been rejecting his past, which meant he had been rejecting himself.",
]},

{"level": 2, "heading": "Bring Your Best When You Feel Your Worst", "paras": [
 "Everyone in SEAL training knows Wednesday is the worst day of Hell Week, which is part of why it is: men arrive tired on schedule because the lore told them Wednesday is when you get tired. Don't take in what somebody else felt. Feel what you feel, and make that your reality.",

 "By that Wednesday the class had been awake for days, the skin was rubbed raw, and Goggins had a knee swollen to the size of a grapefruit. Nine instructors stood on the beach, warm, holding coffee. So his crew stopped lifting their boat and started throwing it — up, caught overhead, tapped to the sand, up again — chanting that you can't hurt Boat Crew Two. Mouths came open. Some of the instructors looked away. The point was never the boat. Those instructors were silently measuring the class against their own worst night, and showing them your best at the exact hour that was their worst cracks something in them instead of in you.",

 "Two things keep this from being a stunt. First, the game is mostly played on yourself. Outside of physical competition the other person never needs to know it is happening, and the real measure is stringing seconds together until you last longer than your opponent thinks you can. Second, timing, which he learned by getting it wrong: at a stage race in Hawaii he ran a double marathon fast at the front so his rivals would hear the splits and give up, and one of them simply held his own pace and took the overall win by ten minutes. You take a soul at the end of a race, not the beginning. And he is direct about the office version rather than the surf-zone version: do it with humility, or it curdles into something that just makes people resent you.",
]},

{"level": 1, "heading": "The Governor"},

{"level": 2, "heading": "The Cookie Jar", "paras": [
 "In November 2005 a race director he was trying to impress told him, more or less sarcastically, to go run a hundred miles at a twenty-four-hour race in San Diego that weekend and get back to him. He heard about it three days out. He had not run more than a mile in six months; he had been powerlifting. He did the arithmetic — a hundred miles in twenty-four hours is just under a fifteen-minute mile — and figured he could walk that fast. He bought his race nutrition at a big-box store the night before: a box of crackers and two four-packs of meal-replacement shakes.",

 "The course was a one-mile asphalt loop, flat except for a seven-foot rise with the pitch of a suburban driveway. He went out at the front of the pack. By the marathon mark he was past every distance he had ever run. Then his quads went, then his feet started bleeding, then his shins turned every rotation of the ankle into shock therapy, then his lungs seized. At mile sixty-nine that seven-foot rise buckled his knees and sent him reeling backward like a truck slipping into neutral, and it took him ten seconds to cover it.",

 "At mile seventy he stopped. He was seeing his wife in triplicate, severely dehydrated and stripped of sodium and potassium, and with emergency medical training of his own he knew his blood pressure was dangerously low. His socks were soaked with blood from cracked toenails and broken blisters; what he did not know yet was that his feet were slivered with stress fractures. He sent her away for painkillers so she would not see him urinating blood down his own leg into a lawn chair. Seventy miles in twelve hours, with no training. She came back with the pills, cookies, two peanut butter sandwiches and a sports drink, and laced his shoes back up for him.",

 "He walked. Twenty-minute miles, as fast as he could move, burning the margin he had banked. At mile eighty-one, close to two in the morning, she told him plainly that she did not believe he would make the time at that pace. Nineteen miles left, eight hours on the clock. He had started the race telling himself it was for fallen servicemen and their families, and standing there he admitted that it wasn't enough to move him. If he was going to make it, it had to get personal. So he shouted the answer out loud, because the voices in his head were louder than his own: why are you still doing this to yourself? Because you are one hard motherfucker.",

 "And then he reached into the cookie jar. However broke the family had been in Indiana, his mother had kept an actual cookie jar stocked, and picking one was a small treasure hunt. He rebuilt that jar internally and filled it with past victories: teaching himself to read, passing the entrance exam, dropping a hundred pounds, conquering his fear of water, graduating at the top of his class. Each lap became a victory lap for a different cookie.",

 "The distinction that makes this work is easy to miss. He is not recalling that those things happened. He is re-entering what they felt like in his body at the moment of overcoming, which he says brings the adrenaline, fades the pain and lifts the pace. Done as a list, it does nothing at all. He passed a hundred miles after nearly nineteen hours, couldn't remember whether he had counted correctly, and ran one more lap to be sure. A hundred and one miles. Years and roughly sixty ultras later, he still rates that night as the hardest thing he has ever done.",

]},

{"level": 2, "heading": "Forty Percent", "paras": [
 "A stock car has a governor bolted into it, a device that restricts fuel and air so the engine never runs hot enough to destroy itself. Take it out and the car goes far faster than the factory advertised. Human beings have one too, except ours is software rather than hardware, buried deep in the mind and wound into identity. It has read your whole life story. It knows exactly which excuse you will accept, and it delivers its verdict in the only currencies you cannot ignore: pain, exhaustion, fear, insecurity.",

 "Most people stop at around forty percent of maximum effort. Not forty percent of what they believe they can do — forty percent of what is actually there. Even at the moment that feels like the absolute end, sixty percent is still in the tank. That is the forty percent rule, and he is careful to say he made it up. It came out of a hundred-mile trail race in the mountains above Honolulu, twenty-four and a half thousand feet of climbing over five laps of rainforest, run by a road runner who had never set foot on a trail, in running shoes with almost no tread, on a course that reduced a field of nearly a hundred to twenty-three finishers.",

 "On the fourth lap, with the tank apparently empty, what worked was not a surge of willpower. It was shrinking the race. Get to that crest, then quit. Get to the next landmark, then quit. Each of those small bargains bought back about five percent, and five percent at a time is how the ceiling moves. He walked the entire fifth lap and finished ninth in thirty-three hours and twenty-three minutes. His own assessment afterward was that he had given about sixty percent.",

 "Two things follow. The first is that you cannot find your own limit while running somebody else's race; alone, you can perform a live autopsy, because there is nothing to compare against but you. The second is that the governor cannot be disabled the way a mechanic disables one. There is no download. The only method is to chase discomfort day after day until the mind accumulates enough evidence that it survives things it swore it would not.",

 "And he attaches an unusual warning to his own rule. Do not do it his way. He derived it by wrecking himself, and spent years taping his feet and wedging his shoes just to keep running. Five to ten percent more than your normal stopping point, added gradually, is the actual instruction. Zero to a hundred will injure you. You will also never reach a hundred percent, and that is the point of the thing.",
]},

{"level": 2, "heading": "The Empowerment of Failure", "paras": [
 "The military fills out an after action report following every mission and every exercise, won or lost. Applied to a personal failure it becomes a live autopsy, with a specific order that most people get backwards.",

 "The twenty-four-hour pull-up record took him three attempts. The first ended at two thousand five hundred repetitions on a television set in New York, on a bar with too much give, after a ten-minute break he could never close. The second ended in a Nashville gym at around three thousand two hundred, with both palms split open to the dermis and a doctor injecting anesthetic directly into the wounds before telling him to stop — she had diagnosed rhabdomyolysis, the breakdown of overworked muscle, and told him people can die from it. He held up the other hand for the second needle. He finished eight hundred pull-ups short, and he knew exactly what eight hundred pull-ups felt like.",


 "The report he wrote afterward, longhand, did not start with his hands. It started with everything that had gone right, in detail and generously, because it is rarely all bad and starting with the obvious wound guarantees you never see the rest of the body. The gym had been the right kind of place. The tape and chalk had worked. The harder bar had bought him seven hundred more repetitions than the first attempt. He had blamed no one. Only then came the audit that mattered: his preparation had never wavered, but his belief had been shakier than he cared to admit.",

 "He fixed the belief with a precedent. Roger Bannister was told a four-minute mile was beyond human capacity, failed repeatedly, then ran it in May of 1954 — and had his record broken six weeks later, with more than a thousand runners following since. So Goggins decided the record was already his and the only open question was the date. The tactical fixes came out of the same report: start slower to go further, cap any break at four minutes because the wall arrives near hour ten, and change the one variable left, which was hand protection.",

 "Two months later, seventeen hours in, at about three in the morning, he passed the record and finished at four thousand and thirty. He did not celebrate. And how he describes the last hours corrects the usual idea of self-talk: talking yourself up is lying to yourself if you have not put the work in. What he was actually doing on that bar was remembering the sixty-seven thousand pull-ups it had taken to get there. That was the self-talk.",
]},

{"level": 2, "heading": "What If", "paras": [
 "Late in his career an echocardiogram found an atrial septal defect — a sizeable congenital hole between the upper chambers of his heart. His doctor's explanation was that he had been supplying his muscles and organs with roughly half the oxygen they needed. He had run a hundred and one miles and graduated SEAL training on that. Two surgeries later his body stopped anyway.",

 "The part of that stretch of his life that matters most is where he was lying in bed in Chicago in the fall of 2014, thirty-eight years old, genuinely wondering if this was the end. He ran his own life like a highlight reel — beaten and abused and uneducated and obese, taught himself to swim, ran on broken legs, terrified of heights and then jumping from nineteen thousand feet, sixty-plus ultras, a world record, a stutterer who became the Navy SEALs' most trusted public speaker. And then he stopped fighting, and what he felt was gratitude. He forgave the kid who cheated, who had done it for acceptance and out of shame at not being able to read. Then he let go of the long list of haters and doubters and racists and abusers, because he could not hate them anymore. They had helped make him. He had been at war for thirty-eight years, and at what looked like the very end of it, he found peace.",

 "What if is the reply to every ceiling anyone has ever set for you, and to every one you set for yourself. It is permission to face your worst memories, accept them as part of your history, and use them.",

 "He closes with a picture he says he visualizes. There is a line to get into heaven, and God is interviewing everyone, working down a chart with every name on it. When it is his turn, God shows him the life he was supposed to have lived — and if he had never changed, if he were still the three-hundred-pound man spraying for cockroaches, he would be looking at a life he missed because he was not willing to suffer, not willing to go into the dungeon of his own soul and find more of himself. So when you get to heaven, are you really in heaven, or are you in hell?",

 "He says he now works so hard that he wants the one thing that knows everything to be up there adding to the chart as he goes — to exceed even God's expectations of what he was capable of. To have God say: I don't believe it. Not even I saw that.",

 "Peace isn't a look on your face. It's a feeling in your heart. You cannot find it without first going to war with yourself, and people want to jump to the peace before they do the war. There is no finish line, and that is the deal you are accepting. The question he leaves you with: how do you want your book to read at the end of your life?",
]},
]


# ── Takeaways ──────────────────────────────────────────────────────────
# One line per entry, shown under the title before the drawing, so the point
# is available in five seconds without reading the entry. Written from the
# entry's own prose — it states nothing the body does not already say.
TAKEAWAY = {
    "insight-1": "When the mind says empty, about sixty percent is still there. The signal is early, not accurate.",
    "insight-2": "You cannot fix a position you refuse to say out loud, and comfort is what keeps it unsaid.",
    "insight-3": "Motivation decides nothing on a bad morning. Discipline works because the decision was never open for discussion.",
    "insight-4": "Perform hardest at the hour you are expected to fade. The opponent you break is usually your own head.",
    "insight-5": "Past wins only help if you re-feel them, not just recall them — and only if stocked in advance.",
    "insight-6": "Written honestly, and starting with what went right, failure is the only feedback that cannot be faked.",
    "action-1": "Say your real position out loud to your reflection, then put the next small step on the glass.",
    "action-2": "Put one thing you avoid into the calendar every day, small enough to survive a bad morning.",
    "action-3": "Write your wins down on a calm day, feeling each one, so you can draw on them mid-effort.",
    "action-4": "Go to where the mind says stop, add five percent, and make that your new baseline.",
    "action-5": "After a failure, write it longhand — what went right first — then schedule the retry.",
}

for _e in BOOK["insights"] + BOOK["actions"]:
    _e["takeaway"] = TAKEAWAY[_e["id"]]
