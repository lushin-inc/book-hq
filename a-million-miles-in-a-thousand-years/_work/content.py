"""Content module — the durable artifact.

The page, the PDF and the docx all read from this. None of them hardcode
content, which is what makes a rebuild a re-render.

The Insights + Action Guide PDF is still produced and still ships in the
folder — it just is not linked from the page.
"""

BOOK = {
    "title": "A Million Miles in a Thousand Years",
    "author": "Donald Miller",
    "subtitle": "What I Learned While Editing My Life",
    "cover": "img/cover.jpg",
    "links": [
        {
            "mark": "↓",
            "label": "Spoken companion",
            "href": "Spoken_Companion.docx"
        }
    ],
    "argument": {
        "question": "Why does a life in which plenty happens still feel like nothing is happening — and what would make it mean something?",
        "answer": "A story is a character who wants something and overcomes conflict to get it. That is not only how films work; it is the only structure under which a human life stops reading as noise. Most people never choose an ambition, so their scenes never accumulate, and the ambitions they absorb by default — the car, the condo, the better dishwashing liquid — would not hold an audience for ten minutes. Meaning is not a conclusion you reach by thinking. It is a sensation available only while you are inside a story: wanting something difficult, ideally something that costs you and serves somebody else, forcing yourself through a door you cannot walk back through, and letting the conflict make you into somebody else. There is no climax waiting at the end. What you get is the character you became, and the people the pain bound you to."
    },
    "framework": {
        "name": "Editing your life",
        "intro": "The book is built in five parts, and the parts are one sentence assembled a phrase at a time — the definition of a story, applied to a person. Each element is a question you can put to your own life today.",
        "steps": [
            {
                "mark": "01",
                "term": "A character",
                "gloss": "A character is what they do. Not what they think, feel, wish or intend. Everyone watching your life — your spouse, your children, your friends — sees only the footage."
            },
            {
                "mark": "02",
                "term": "…who wants something",
                "gloss": "The ambition decides what the story is about. A story about a man who wants a Volvo is a bad story on a screen and a bad story in a life. The ones that go epic are very difficult and sacrificial."
            },
            {
                "mark": "03",
                "term": "The inciting incident",
                "gloss": "Characters do not change because they want to. They have to be forced. Something has to happen that makes staying put worse than going — a doorway through which you cannot return."
            },
            {
                "mark": "04",
                "term": "…and overcomes conflict",
                "gloss": "The middle is longer and harder than the version you signed up for, and it is the only thing that changes anybody. Joy is what you feel when the conflict is over. Conflict is what makes you somebody else."
            },
            {
                "mark": "05",
                "term": "…to get it",
                "gloss": "Not a climax. Nothing on this side of the grave resolves everything. What resolves is the character, and what remains is the people the story bound you to."
            }
        ]
    },
    "insights": [
        {
            "id": "insight-1",
            "title": "Without the principles of story, life is just random experiences",
            "lede": [
                "A life does not feel meaningless because too little happens in it. It feels meaningless because the things that happen do not add up. Play a recording of a garbage truck backing up with a jackhammer in the distance and you have sound, but you will not be humming it a week later; music is sound that obeys scales and harmonics. A life obeys the principles of story — a character, an ambition, conflict, change — or it stays a set of scenes that happen to be adjacent."
            ],
            "evidence": "Two filmmakers came to Portland to turn Donald Miller's bestselling memoir into a screenplay and immediately began inventing a fictional Don who worked in a factory. When Miller asked what was wrong with the real one, the cinematographer answered him between olives: your real life is boring. Miller protested — he had jumped off a bridge once, he had seen a bear. The director agreed with the cinematographer, and then softened it in the only way that mattered: nobody is talking about you, Don. It is kind of true for all of us.",
            "operative": "When your life feels like noise, resist asking what is missing from it. Ask instead what you want, what stands in the way of getting it, and what you would have to become in order to get it. If none of the three has an answer, that is the diagnosis.",
            "plate": "img/insight-01.png",
            "alt": "Scattered ink marks across a sheet; a hand draws five staff lines through them and the marks stand up into musical notes where the lines have passed. Labelled Noise and Music."
        },
        {
            "id": "insight-2",
            "title": "A character is what they do",
            "lede": [
                "The story you tell yourself and the story you are telling the world are two different stories, and only one of them is being watched. In a book you can climb inside a person's head. In a film you cannot, and a life runs like a film. Your intentions, your private affection, your quiet resolve — none of it is on the screen. What is on the screen is the footage.",
                "The character of the character matters just as much as what he achieves. Screenwriters call it saving the cat: in the first twenty minutes the protagonist has to do something good, or the audience will not care whether he wins."
            ],
            "evidence": "A friend told Miller he had never loved his wife more — she had had their baby and he saw her completely differently. Miller asked how she had taken the news. He had not mentioned it to her. She knows I love her, he said. From her seat in the audience she was still watching a man preoccupied with work. The counter-case was on the news at the time: Bernie Madoff was a character who wanted something and overcame conflict to get it, and the story is worthless, because of the kind of character he was. The story he told himself was not the story he was telling.",
            "operative": "Take the reel. If a camera followed you for a month with no access to your thoughts, what would the footage say you wanted, and who would it show you loved? Wherever the footage and the intention disagree, the footage is the story you are actually telling.",
            "plate": "img/insight-02.png",
            "alt": "A movie camera on a tripod with dotted lines marking what it can see; a man types inside that wedge while his thought balloon floats outside it, beyond the camera's reach."
        },
        {
            "id": "insight-3",
            "title": "The ambition is the story — and if you do not pick one, one gets installed",
            "lede": [
                "What the character wants determines whether the story is worth living. Nobody weeps at the end of a film about a man who worked for years to buy a Volvo and finally drove off the lot testing the windshield wipers, and being inside the life rather than watching it does not change the verdict. If it would not work in a movie, it will not work in a life.",
                "Advertising is the elements of story turned against you. Convince the character he is miserable. Introduce the product as the resolution. Cut to a life in which the hair is done, the kids are doing homework and the husband is back. That is an inciting incident and a climax sold in thirty seconds, and the average American absorbs about three thousand of these messages a day."
            ],
            "evidence": "Asked by his accountant to highlight twelve months of bank statements for write-offs, Miller found a robotic vacuum cleaner he had turned on twice and then replaced with a broom, a new truck, a nicer condo — and realized that what he was highlighting was the sum of his ambitions. He put the condo on the market. The comparison that moved him was a conference of roughly five hundred millionaires organized around giving their money away, building schools and orphanages and drilling wells; one ran a company bringing in two hundred and fifty million a year and lived on a fixed salary of a hundred and twenty thousand. They were the happiest people Miller had met, and they described themselves as people who fund stories.",
            "operative": "Read your own statement the way a screenwriter would read it — as the record of what this character actually wanted — and write the one-sentence logline it implies. Then ask whether you would sit through it.",
            "plate": "img/insight-03.png",
            "alt": "An arm reaching out of a television screen to post a small car through a hinged flap in a smiling man's head, while a dotted line leads his feet toward a car lot."
        },
        {
            "id": "insight-4",
            "title": "Characters do not change because they want to. They have to be forced",
            "lede": [
                "Wanting a better story does not produce one. People are built to seek comfort and order, and once they have it they plant, even when the comfort is not comfortable — because a bad situation you can predict beats a better one you cannot. This is a rule of screenwriting because it is a fact about people, which means the useful question is never how badly you want it. It is what you are willing to make impossible to avoid."
            ],
            "evidence": "Watching Lance Armstrong win his sixth Tour de France, Miller sat in a chair, lifted his legs and made a circular motion with his feet. The sticky note carrying his father's Social Security number sat on the kitchen counter for a week while he mowed the lawn, trimmed the hedges and ran an extension cord out to a tree. What finally moved him was accidental: trying to sound impressive at a bar, he announced he was hiking the Inca Trail and invited along a girl he had been afraid to ask out. She said yes. Then he read that the trail climbs to fourteen thousand feet. He joined a gym the next day.",
            "operative": "Stop taking the temperature of your motivation and start building the doorway. An inciting incident is any event that makes not doing the thing worse than doing it: a deposit paid, a date announced, a person invited who would be let down.",
            "plate": "img/insight-04.png",
            "alt": "A man pedalling the air in an armchair whose legs have grown thick roots through the floorboards, with an untouched cobwebbed bicycle leaning against the wall."
        },
        {
            "id": "insight-5",
            "title": "Conflict is the only thing that changes anybody",
            "lede": [
                "The middle of a story is long, and it is longer than the version you signed up for. The far shore stops getting closer, the shore behind you stops getting smaller, and the strokes that used to move you now only rock the boat. That stretch is not the price of the story. It is the story. Joy is what you feel once the conflict is over; it is the conflict that makes you into somebody else.",
                "This is also where nearly everybody quits, and quitting there feels like wisdom rather than surrender — as though the flatness were evidence you had chosen the wrong story rather than evidence you had reached its middle."
            ],
            "evidence": "A guide on the Inca Trail explained why pilgrims were made to take the four-day mountain route to Machu Picchu when the river route took six hours: the emperor knew that the more painful the journey, the more the traveler would appreciate the city. Nobody in the group wanted the short route. The screenwriters of Friday Night Lights had two seasons to choose from — the year Odessa won the state championship and the year they were stood up on the goal line as time ran out — and chose the loss, because that was the year the team tried harder and the story was about the cost.",
            "operative": "Expect the middle and name it out loud when you are in it. Reward per unit of effort collapses in the middle of everything worth doing. The people who finish are not the ones who suffer less; they are the ones who were told the middle was coming, and who had somebody else in the boat.",
            "plate": "img/insight-05.png",
            "alt": "A kayak dead centre of a channel, an identical tree on each shore both labelled Same size, and an enormous trail of paddle splashes running off the edge of the frame."
        },
        {
            "id": "insight-6",
            "title": "There is no climax, and waiting for one is what ruins the story",
            "lede": [
                "The moment when all tension resolves and everything afterward is fine does not happen in a human life. It happens constantly in films, which is part of why we watch them. Expecting it — through the marriage, the promotion, the house, the conversion — turns every real satisfaction into a disappointment, because it gets measured against a resolution that was never on the schedule.",
                "There are smaller climaxes. A kid makes the football team; a woman gets the ring. Then the kid discovers football is hard and the woman wakes up three months in still lonely, and both risk taking the end of a sub-story for the end of the human story."
            ],
            "evidence": "A study ranking the happiest countries put Denmark on top, and the explanation offered was low expectations — Danes do not expect products to fulfil them or relationships to end their problems. Told that Americans would want to move there on hearing the news, one Dane replied without missing a beat that they would probably be let down. Susan Isaacs, asked in front of a live audience with her husband in the room whether there is one true love for every person, said no: she had married a guy, he was just a guy, and knowing that freed her to love him as a guy rather than as an ultimate problem solver.",
            "operative": "Take people, things and God off resolution duty. When you stop expecting people to be perfect you can like them for who they are; when you stop expecting possessions to complete you they become pleasant; when you stop expecting God to end your troubles you find you enjoy his company. Miller holds that all wrongs are finally made right — at a wedding, with a feast — and that the error is expecting delivery on this side of it.",
            "plate": "img/insight-06.png",
            "alt": "A man on a hilltop holding a measuring stick up against a mountain peak drawn only in dotted outline, his back turned to the path of small good things behind him."
        }
    ],
    "actions": [
        {
            "id": "action-1",
            "title": "Read your bank statement as a plot summary",
            "lede": [
                "Print twelve months and read them the way a screenwriter would: as the record of what this character actually wanted. Not what he said he wanted, not what he intended — a character is what they do, and purchases are actions. Then write the one-sentence logline your statement implies and decide whether you would sit through it.",
                "When: once a year, and any time life feels vaguely unsatisfying in a way you cannot name."
            ],
            "operative": "It is working when you can say in one sentence what your money says you want, and you either endorse that sentence or you have changed something because of it.",
            "caveat": "This is not an argument for frugality. The man living on a hundred and twenty thousand out of two hundred and fifty million was not treating spending as a sin; he had decided money was the thing that pays for stories, and he was buying them.",
            "plate": "img/action-01.png",
            "alt": "A bank statement unrolling and turning into a strip of film whose frames hold a robot vacuum, a truck, a sofa and a television, held up to the light and inspected."
        },
        {
            "id": "action-2",
            "title": "Build a door you cannot walk back through",
            "lede": [
                "Take the thing you keep not doing and attach a cost to not doing it. Pay the deposit. Announce the date. Invite the person you would be humiliated to disappoint. Sitting in a hotel in Chicago on his last day, having failed to call his father two nights running, Miller texted ten close friends and asked them to ask him the next night how the meeting had gone. Then he had to go.",
                "When: any ambition you have been carrying as an intention for more than a month."
            ],
            "operative": "It is working when the thing stops being a decision. You are no longer choosing whether; you are managing how.",
            "caveat": "Do not manufacture one until you have actually decided you want the thing. Courage spent on the wrong story is still spent.",
            "plate": "img/action-02.png",
            "alt": "A man stepping through a doorway with the floorboards fallen away behind him and ten hands reaching in from the edges, each with a question mark above it."
        },
        {
            "id": "action-3",
            "title": "Point at the horizon every single day",
            "lede": [
                "Asked what it takes to lead fifty lawyers who free people from slavery and the sex trade, Gary Haugen said his main job is to show up each day and remind them what the story is about. That is the same job at home, on a team, in a marriage and in your own training — not a speech, but the same simple thing said again. Miller's trainer supplied the other half: twenty minutes of mild exercise five days a week counts as a workout, and everything past that is icing. Progress, however slow, is all that matters.",
                "When: daily, for any ambition longer than a few weeks."
            ],
            "operative": "It is working when the people in your story — including you — can say what it is about without being asked.",
            "plate": "img/action-03.png",
            "alt": "A man pointing at a distant flag with four fainter copies of himself repeating the gesture behind him, over ground drawn as many identical short dashes."
        },
        {
            "id": "action-4",
            "title": "Give somebody a better story to be in",
            "lede": [
                "People live the best story available to them. If nobody has offered one, they take whichever is nearest, and a bad story containing risk and belonging beats no role at all. Finding marijuana in his thirteen-year-old daughter's closet and a boyfriend he could not stand, Miller's friend Jason stopped grounding her and called a family meeting to announce that the family — freshly into a second mortgage — was going to build a twenty-five-thousand-dollar orphanage. Nobody spoke to him for a day. Then his wife told him she was proud of him, and a few days later his daughter climbed into their bed to ask whether they could go to Mexico and whether she could raise money on her website. She broke up with the boyfriend that month.",
                "When: whenever somebody you are responsible for is drifting into a story you would not choose for them."
            ],
            "operative": "It is working when they behave differently without having been told to behave differently.",
            "caveat": "The role has to carry real want and real risk. A title with no ambition attached is a chore, and people can tell instantly. Catherine's Prison Entrepreneurship Program addresses inmates not by their numbers but as the chief financial officer of Company B, and runs a recidivism rate under three per cent against a national rate above two-thirds — because the role came with a business to build.",
            "plate": "img/action-04.png",
            "alt": "A man in a torn costume taken from the one hook within reach, while a rack of better costumes stands out of reach behind a counter and a second figure holds one out."
        },
        {
            "id": "action-5",
            "title": "Build a memorable scene on purpose",
            "lede": [
                "Good stories do not take place in coffee shops, and neither do good lives. Watching SportsCenter while his daughter modelled her prom dress, Miller's friend Randy told her it was a nice colour — then went to his closet, put on his suit, knocked on her bedroom door and asked his wife to take a picture of the two of them. They danced in the living room until one in the morning. When Miller's group of kayakers pushed off from the Goff family's dock, the whole family took three steps and jumped into the water fully dressed, in shoes and jackets, to wave goodbye.",
                "When: any occasion you would otherwise mark with coffee, and any relationship that has gone quiet."
            ],
            "operative": "It is working when somebody else brings the scene up years later without being prompted.",
            "caveat": "Memorable scenes cost something, which is why they are remembered — and part of the cost is sometimes paid by other people. Miller's rooftop fireworks party cost him a neighbour's trust, and he never decided whether it was worth it. Do enough of that and your character becomes suspect.",
            "plate": "img/action-05.png",
            "alt": "A dock lined with identical coffee cups fading into dotted outlines, and at its end a family in coats and shoes caught mid-jump above the water."
        }
    ],
    "vocabulary": {
        "intro": "Most of this is screenwriting vocabulary, borrowed intact. The argument of the book is that the terms describe people as accurately as they describe protagonists.",
        "terms": [
            {
                "id": "v-story",
                "term": "Story",
                "def": "A character who wants something and overcomes conflict to get it. Miller sat through a thirty-six-hour seminar without getting it; his roommate, half-watching a Seinfeld rerun, gave him the sentence in one go."
            },
            {
                "id": "v-inciting-incident",
                "term": "Inciting incident",
                "def": "The event that forces a character out of comfort and into the story. James Scott Bell's definition: a doorway through which the protagonist cannot return."
            },
            {
                "id": "v-turns",
                "term": "Positive and negative turns",
                "def": "Events that move the protagonist toward or away from the ambition. Every real story has both, and a story with no negative turn is not interesting. A protagonist who knows this does not quit when one arrives."
            },
            {
                "id": "v-character-arc",
                "term": "Character arc",
                "def": "The change in the protagonist between the first page and the last. If the character has not changed, the story has not happened yet."
            },
            {
                "id": "v-save-the-cat",
                "term": "Save the cat",
                "def": "A screenwriter's rule: early on, the protagonist must do something good, or the audience will not care whether he gets what he wants. The character of the character decides whether the story is worth anything."
            },
            {
                "id": "v-practice-story",
                "term": "Practice story",
                "def": "A smaller story lived deliberately in order to learn how, and to get the taste. Miller's were a hike in Peru, a bicycle and a girl. Each one made the next one bigger, until he could not go back to normal."
            },
            {
                "id": "v-resistance",
                "term": "Resistance",
                "def": "Steven Pressfield's term for the force that comes against you the moment you point at a distant horizon. Pressfield's claim, which Miller takes seriously and reads as spiritual: the harder the resistance, the more important the task."
            },
            {
                "id": "v-the-writer",
                "term": "The writer who is not you",
                "def": "Miller's name for the voice suggesting a better story than the one he is playing — hold your tongue, forgive the friend you have not called, go and see your father. He identifies it as God and treats his own conscience as the pen."
            },
            {
                "id": "v-whimsy",
                "term": "Whimsy",
                "def": "Bob Goff's answer when asked the key to living a great story: the nagging idea that life could be magical, could be special, if you were only willing to take a few risks."
            },
            {
                "id": "v-epic",
                "term": "Epic",
                "def": "A story raised to the next level by two conditions, both of them about the ambition: it has to be very difficult to attain, and it has to be for the sake of somebody else."
            }
        ]
    },
    "quickReference": [
        {
            "kind": "line",
            "label": "The question",
            "text": "Why does a life in which plenty happens still feel like nothing is happening?"
        },
        {
            "kind": "line",
            "label": "The definition",
            "text": "A story is a character who wants something and overcomes conflict to get it."
        },
        {
            "kind": "line",
            "label": "The character test",
            "text": "A character is what they do. Judge by the footage, not the intention."
        },
        {
            "kind": "line",
            "label": "The ambition test",
            "text": "If it would not work in a movie, it will not work in a life."
        },
        {
            "kind": "line",
            "label": "The movement rule",
            "text": "Characters do not change because they want to. Build the door you cannot walk back through."
        },
        {
            "kind": "line",
            "label": "The middle",
            "text": "Joy is what you feel when the conflict is over. Conflict is what changes you."
        },
        {
            "kind": "line",
            "label": "The two epic conditions",
            "text": "Very difficult to attain, and for the sake of somebody else."
        },
        {
            "kind": "line",
            "label": "The ending",
            "text": "There is no climax. What resolves is the character, and the people the story bound you to."
        },
        {
            "kind": "list",
            "label": "Five moves",
            "items": [
                "Read twelve months of statements as a plot summary.",
                "Attach a cost to not doing the thing you keep not doing.",
                "Point at the horizon daily; twenty minutes counts.",
                "Give somebody a role with real want and real risk in it.",
                "Build one scene nobody could have had over coffee."
            ]
        }
    ],
    "closingLine": "Nobody gets to watch the parade."
}


# ── Takeaways ──────────────────────────────────────────────────────────
# One line per entry, shown under the title before the drawing, so the point
# is available in five seconds without reading the entry. Written from the
# entry's own prose — it states nothing the body does not already say.
TAKEAWAY = {
    "insight-1": "A life feels empty because nothing adds up, not because too little happened.",
    "insight-2": "Only your actions are on the screen. Where the footage and the intention disagree, the footage is the story.",
    "insight-3": "If you do not choose an ambition, advertising installs one. Your bank statement records which one you actually chose.",
    "insight-4": "Nobody changes because they want to. Build the doorway that makes not doing it worse than doing it.",
    "insight-5": "The flat middle is not the price of the story. It is the story, and it is where everyone quits.",
    "insight-6": "There is no moment when everything resolves. Waiting for one turns every real satisfaction into a disappointment.",
    "action-1": "Print a year of bank statements and read them as the record of what this character actually wanted.",
    "action-2": "Attach a cost to not doing it — a deposit, a date, a person you would hate to disappoint.",
    "action-3": "Say what the story is about, out loud, every day, to whoever is in it with you.",
    "action-4": "People take the best story on offer. Offer a better one instead of taking the current one away.",
    "action-5": "Good lives do not happen in coffee shops. Build the scene on purpose and someone will still be telling it.",
}

for _e in BOOK["insights"] + BOOK["actions"]:
    _e["takeaway"] = TAKEAWAY[_e["id"]]
