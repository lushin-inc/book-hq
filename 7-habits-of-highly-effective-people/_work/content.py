# -*- coding: utf-8 -*-
"""
Book HQ — content module for "The 7 Habits of Highly Effective People
(Powerful Lessons in Personal Change)" by Stephen R. Covey.

The durable artifact. build_page.py, build_pdf.py and build_docx.py all read this;
none of them hardcode content. Pass 2 is a re-render of this file, not a rebuild.

Source transcript: The 7 Habits of Highly Effective People Powerful Lessons in
Personal Change by S.txt
"""

SLUG = "7-habits-of-highly-effective-people"
TITLE = "The 7 Habits of Highly Effective People"
SUBTITLE = "Powerful Lessons in Personal Change"
AUTHOR = "Stephen R. Covey"
COVER = "img/cover.jpg"


# ---------------------------------------------------------------------------
# The argument
# ---------------------------------------------------------------------------

CENTRAL_QUESTION = "Why do the techniques for being effective with other people keep failing, and what has to be true before any of them work?"

CENTRAL_ANSWER = (
    "Because effectiveness is not a technique. Two hundred years of American "
    "success writing were almost entirely about character until the early "
    "nineteen hundreds, when the emphasis moved to personality: technique, "
    "image, how to appear to be rather than how to be. The techniques are not "
    "worthless. They are the tip of an iceberg, and they hold only as long as "
    "the mass underneath holds. What sits underneath is a set of principles "
    "that operate whether or not you believe in them, the way a farm operates. "
    "You can cram for a test, because a test is a social system with a grader "
    "in it. You cannot cram on a farm, and every part of life that actually "
    "matters is a farm. So the habits run in order. The first three win a "
    "private victory over yourself and carry you from dependence to "
    "independence; the next three win a public victory with others and carry "
    "you from independence to interdependence; the seventh renews all six. "
    "Until you are independent you cannot be interdependent, which is why "
    "every attempt to be effective with other people before you are effective "
    "with yourself comes out as manipulation, and is read as manipulation."
)


# ---------------------------------------------------------------------------
# Framework
# ---------------------------------------------------------------------------

FRAMEWORK_NAME = "The Maturity Continuum"

FRAMEWORK_INTRO = (
    "The habits are sequential, and the sequence is the whole design. Picture "
    "a line from low maturity to high with three positions on it. Dependence "
    "is the attitude of you: you take care of me, and if you do not, I blame "
    "you. Independence is the attitude of I: I can do it, I am responsible, I "
    "can choose. Interdependence is the attitude of we. The habits move you "
    "along that line in order — you cannot do calculus before algebra."
)

FRAMEWORK_STEPS = (
    ("1", "Be proactive",
     "You are the programmer. Between what happens to you and your response "
     "there is a space, and in it the freedom to choose. Work inside your "
     "circle of influence, not your circle of concern."),
    ("2", "Begin with the end in mind",
     "Write the program. Everything is created twice, mentally then "
     "physically, and the mission statement is the mental creation. Personal "
     "leadership: deciding what the first things are."),
    ("3", "Put first things first",
     "Run the program. Personal management, and the test of integrity: living "
     "by the priorities habit two identified. A compass, not a clock. Its home "
     "is Quadrant Two."),
    ("—", "Independence reached, interdependence now possible",
     "One through three constitute the private victory. Until it is real, the "
     "next three become techniques, and techniques are detected."),
    ("4", "Think win-win",
     "The habit of mutual benefit, and of abundance — there is plenty out "
     "there and to spare, so another person's strength is not a threat. The "
     "options are win-win or no deal."),
    ("5", "Seek first to understand, then to be understood",
     "The sequence is the habit. The key to influencing someone is first to be "
     "influenced by them. Feeling understood is air; until people have it, "
     "nothing else reaches them."),
    ("6", "Synergize",
     "The fruit of four and five. Differences stop being obstacles and become "
     "the raw material for a third alternative neither party arrived with. "
     "One plus one equals three, not one and a half."),
    ("7", "Sharpen the saw",
     "Renewal in four dimensions — physical, mental, spiritual, "
     "social-emotional. It surrounds the other six and makes them repeatable."),
)


# ---------------------------------------------------------------------------
# Vocabulary
# ---------------------------------------------------------------------------

VOCABULARY_INTRO = (
    "Covey builds the book on a handful of terms used with unusual precision. "
    "Several are ordinary words given a narrower meaning than usual, and the "
    "argument only holds if the narrow meaning is kept."
)

DEFINITIONS = (
    ("The character ethic",
     "The success literature of roughly 1776 to 1926: integrity, fidelity, "
     "courage, compassion, responsibility, justice, service. Effectiveness as "
     "a consequence of what a person actually is."),
    ("The personality ethic",
     "What replaced it — technique, image, public relations skill. How to "
     "appear to be rather than how to be. North Carolina's motto, to be rather "
     "than to seem, names exactly what was lost."),
    ("Principle",
     "A natural law, like gravity: universal, self-evident, changeless, "
     "operating whether or not it is believed in. We control our actions; "
     "principles control the consequences."),
    ("Paradigm",
     "The mental map you carry of the way things are, assembled out of your "
     "own conditioning and mistaken by you for reality. We do not see the "
     "world as it is; we see the world as we are."),
    ("P/PC balance",
     "Production against production capability — the golden eggs against the "
     "health of the goose. Effectiveness is the ratio, not the size of either. "
     "Covey uses effectiveness rather than success deliberately."),
    ("The emotional bank account",
     "The trust built up in a relationship. Courtesy, honesty and kept "
     "commitments are deposits; discourtesy, betrayal and broken promises are "
     "withdrawals. The balance decides how your words are heard before you say "
     "them."),
    ("Circle of influence, circle of concern",
     "The inner circle holds what you can affect; the outer holds what you "
     "cannot. Energy spent in the inner circle enlarges it; energy spent in "
     "the outer one shrinks it. A reactive person can be extremely busy in the "
     "outer circle."),
    ("Quadrant Two",
     "Important but not urgent: prevention, preparation, planning, "
     "relationship building, self-development, mission. The leadership "
     "quadrant, and the one displaced, because nothing in it announces "
     "itself."),
    ("Win-win or no deal",
     "Mutual benefit, with the honest option of agreeing to disagree agreeably "
     "when no mutual win exists. Lose-win is not win-win; being nice while "
     "being taken to the cleaners is losing."),
    ("Synergy",
     "The whole being greater than the sum of its parts — creative cooperation "
     "producing something neither party brought, and reachable only once both "
     "underlying purposes are on the table. Its negative form, where energy "
     "goes into fighting, produces less than one person working alone."),
)


# ---------------------------------------------------------------------------
# Insights
# ---------------------------------------------------------------------------

INSIGHTS = (
    dict(
        n=1,
        title="The techniques are the tip of an iceberg",
        lede=(
            "Covey went back two hundred years into the popular success "
            "literature of the United States. For the first hundred and fifty "
            "years, almost the entire focus was on character: integrity, "
            "fidelity, courage, compassion, responsibility, justice, service. "
            "Then, in the early nineteen hundreds, the emphasis moved to "
            "personality — technique and image, how to appear to be rather "
            "than how to truly be."
        ),
        evidence=(
            "A student asked Covey how he was doing in the class. Covey said, "
            "you know that far better than I do — how are you doing? The "
            "student admitted he had had a rough time and had not applied "
            "himself. He had come, Covey pointed out, to find out how well he "
            "had psyched out the system, when he already knew in his heart how "
            "he was doing."
        ),
        operative=(
            "The techniques are not fraudulent and not useless. They are the "
            "part of the iceberg above the water, and they hold exactly as "
            "long as the mass below holds. Most development effort goes into "
            "the tip, because the tip is what other people can see. The seven "
            "habits run inside out: character first, then technique. Covey "
            "notes the shift is now running back toward character on pragmatic "
            "rather than moral grounds."
        ),
        img="img/insight-01.png",
        alt=(
            "An iceberg. On the small tip above the waterline, labelled SEEN, "
            "a stick figure kneels polishing the surface with a cloth, a "
            "bucket beside it and shine marks coming off the spot. The far "
            "larger mass below the water, labelled HOLDS IT UP, is untouched, "
            "with a crack running up through it toward the base of the tip."
        ),
    ),
    dict(
        n=2,
        title="You can cram for a test but not on a farm",
        lede=(
            "Ask a room of adults whether they crammed in school and the "
            "hands go up. Ask whether they got good at it and they stay up. "
            "Now ask whether anyone has crammed on a farm — forgotten to plant "
            "in the spring, coasted all summer, then worked frantically in the "
            "fall for a harvest. The question is absurd, and everyone knows "
            "instantly why."
        ),
        evidence=(
            "A farm is a natural system, governed by principles rather than "
            "social convention. School is a social system with a grader in it, "
            "which is why cramming works there — you can get a degree without "
            "getting an education. Covey's claim is that a mind, a body, a "
            "marriage, a character and a reputation are all farms rather than "
            "tests, however much they get graded like tests along the way."
        ),
        operative=(
            "This is what makes the habits unfakeable, and it relocates "
            "control. The popular language says you are the master of your own "
            "destiny. Covey's version is narrower: we control our actions, but "
            "the consequences that flow from them are controlled by "
            "principles, and accepting that is the only sense in which anyone "
            "is master of anything. It also changes what is worth teaching — "
            "a practice expires when the situation changes; the principle "
            "underneath it keeps applying."
        ),
        img="img/insight-02.png",
        alt=(
            "One long ground line with four stick figures along it, labelled "
            "SPRING, SUMMER, FALL and NOW. The first three stand idle with "
            "their arms up; the fourth is on its knees digging frantically "
            "with a shovel, motion lines flying off it. Nothing grows anywhere "
            "along the line, and at the far right an empty woven basket lies "
            "tipped on its side."
        ),
    ),
    dict(
        n=3,
        title="You are always describing yourself",
        lede=(
            "A paradigm is the mental image you carry of the way things are, "
            "assembled out of your background and experience. It is not an "
            "opinion sitting on top of reality; it is what you take reality to "
            "be. We all think we see the world as it is. In fact we see the "
            "world as we are, and when you describe a person or a situation as "
            "though describing it as it is, you are describing your own frame "
            "of reference and projecting it outward."
        ),
        evidence=(
            "Covey was on a subway one quiet Sunday morning when several "
            "children ran on, followed by their father. The children were wild "
            "— up and down the car, shoving people's newspapers aside. The "
            "father sat down beside Covey and did nothing at all. Covey held "
            "it in for a few minutes, then said, sir, do you think you could "
            "control your children a little, they're very upsetting to people. "
            "The man lifted his head as though he had only just arrived. Oh, "
            "yes, I guess I should. We just left the hospital and their mother "
            "died about an hour ago. I don't know how to take it, and frankly "
            "I don't think they do either."
        ),
        operative=(
            "Nothing on that car changed. One sentence of new information "
            "arrived, and Covey's irritation was replaced by a wish to help — "
            "no effort applied to his attitude, none to his behavior. Attitude "
            "and behavior are downstream of the paradigm, which is why most "
            "development programs work on the two things that move last. The "
            "fastest way to change someone's behavior is to change how they "
            "see their own role. Anyone who has become a parent, or a manager "
            "for the first time, has watched the world reorganize overnight "
            "with no effort spent on attitude."
        ),
        img="img/insight-03.png",
        alt=(
            "A stick figure whose head contains a projector lamp, casting a "
            "beam labelled MINE onto a large screen labelled REALITY. Inside "
            "the screen, three small stick-figure children run with their arms "
            "up while a seated adult sits with its head down. On the floor "
            "below the screen lies a slip of paper reading MOTHER DIED, face "
            "up and unread."
        ),
    ),
    dict(
        n=4,
        title="Every result is drawn against a capacity you cannot see",
        lede=(
            "Aesop's farmer finds a golden egg beside his goose, then another, "
            "and another, and becomes wealthy — and impatient. He wants them "
            "all now, so he kills the goose to get at them, and finds none. "
            "That fable contains Covey's whole definition of effectiveness: "
            "getting what you want, and getting it in a way that lets you get "
            "it again and again. He calls it P/PC balance. P is production, "
            "the golden eggs. PC is production capability, the health of the "
            "goose."
        ),
        evidence=(
            "Covey describes a clam chowder house so popular you could barely "
            "get near it between eleven and two. New management arrived, kept "
            "the name, and watered down the chowder. The bottom line rose for "
            "a month or so, because all the cost of the quality had been "
            "saved. Then the customer base liquidated itself, and people would "
            "not come back or believe it was the same chowder — the violation "
            "of trust outlasted the change in recipe."
        ),
        operative=(
            "The asymmetry is what makes this hard to catch in time: cutting "
            "capability raises production first and lowers it later, so the "
            "early evidence always argues for continuing. Cut training, "
            "selection, research and every other form of people development, "
            "and you can double an organization's bottom line for a quarter or "
            "two. The same balance runs through a body, a mind and a marriage. "
            "Covey asks whether a man who went from nothing to hundreds of "
            "millions with a bankrupt family was effective — in the business "
            "sense perhaps, in the sense that matters on a deathbed, no."
        ),
        img="img/insight-04.png",
        alt=(
            "Columns of stacked eggs rising left to right like a bar chart. At "
            "the left, beside the shortest column, a goose stands upright on "
            "the baseline. Beneath the tallest column, labelled THIS QUARTER, "
            "the same goose lies dead. To the right of it the baseline runs on "
            "bare, labelled NEXT."
        ),
    ),
    dict(
        n=5,
        title="The circle you work in is the circle that grows",
        lede=(
            "Between what happens to us and our response there is a space, "
            "and in that space lies the freedom to choose. Covey draws the "
            "practical version as two circles. The outer one, the circle of "
            "concern, holds everything you can do nothing about — the weather, "
            "world events, another person's temperament. The inner one, the "
            "circle of influence, holds what you can affect. Proactive people "
            "work in the inner circle; reactive people work in the outer one."
        ),
        evidence=(
            "Covey spent four years as assistant to a president who was "
            "visionary, talented and dictatorial, whose staff felt treated as "
            "errand runners and sat in the corridor trading stories about him. "
            "One man, Ben, did not: the president's weaknesses were in his "
            "circle of concern, not his circle of influence. Sent for data, he "
            "anticipated the need, analysed it, added recommendations, and "
            "delivered it in a form the president could take to the board. "
            "Inside four years Ben was the second person in the organization."
        ),
        operative=(
            "The paradox is that the inner circle is not a limit but a lever. "
            "Every hour spent inside it makes it larger; every hour spent in "
            "the outer circle — accurately, articulately, and about real "
            "faults — makes the inner one wither. Viktor Frankl, imprisoned in "
            "the Nazi death camps, called this the last of the human freedoms: "
            "the power to choose your response to any condition."
        ),
        img="img/insight-05.png",
        alt=(
            "Two concentric circles. A stick figure inside the inner one leans "
            "hard against its boundary with both arms, and the boundary bulges "
            "outward at that point, arrowed NOW; the bulge has already taken "
            "in a small house and a tree. Behind the figure, several earlier "
            "boundary lines curve away like tree rings, arrowed THEN. Out in "
            "the ring beyond, a cloud, a lightning bolt and a newspaper float "
            "untouched."
        ),
    ),
    dict(
        n=6,
        title="The balance decides what your words mean",
        lede=(
            "The emotional bank account is the trust built up in a "
            "relationship. Courtesy, kindness, honesty and kept commitments "
            "are deposits. Discourtesy, overreacting, cutting someone off, "
            "betraying a confidence and failing to keep commitments are "
            "withdrawals. With a reserve you can make mistakes and they are "
            "absorbed, because the other person already knows you care."
        ),
        evidence=(
            "Now consider the overdrawn account. Communication stops working "
            "even when it is perfectly clear. People read between the lines, "
            "look for hidden agendas, ask how he is manipulating me. A small "
            "mistake gets blown out of all proportion. Covey describes the "
            "climate as walking on minefields and measuring every word — "
            "families and organizations living in memo haven."
        ),
        operative=(
            "The account is why technique cannot be lifted out of context. The "
            "same sentence from the same person means opposite things at "
            "opposite balances, so a skill learned in isolation reads as a "
            "manoeuvre. And it moves in unglamorous currency: in relationships "
            "the small things are the big things. One deposit comes before all "
            "the others — understanding the other person from within their own "
            "frame of reference. Until you know what counts as a deposit to "
            "them, you will keep spending your own currency and wondering why "
            "the balance is not moving."
        ),
        img="img/insight-06.png",
        alt=(
            "Two stick figures facing each other with a tall ledger standing "
            "open on its edge between them, spine lettered BALANCE and both "
            "pages ruled with minus signs. A line from the left figure's mouth "
            "reading CAN WE TALK runs straight and level into the near page, "
            "and leaves the far page as a jagged zigzag carrying the same "
            "words, reaching the right figure, whose arms are thrown up."
        ),
    ),
)


# ---------------------------------------------------------------------------
# Actions
# ---------------------------------------------------------------------------

ACTIONS = (
    dict(
        n=1,
        title="Write the mission statement, and write it as though it can never change",
        lede=(
            "Take several weeks, not an afternoon. Write a statement of what "
            "your life is about, carrying vision — the picture of what you are "
            "about — and principles, how you go about it. Then hold it against "
            "four criteria. Timeless, so no goals in it: goals change with the "
            "situation and the mission statement is the part that does not. "
            "Both ends and means, since a worthy end cannot be reached by an "
            "unworthy one. All four human needs — to live, to love, to learn, "
            "to leave a legacy. And every role you hold, so no part of your "
            "life is left out of your own plan."
        ),
        operative=(
            "Do the same for the family, and treat it as the more important of "
            "the two. Covey's family developed theirs over eight months with "
            "everyone participating, and used it afterwards as a family "
            "constitution, kept in the family room and returned to. He said "
            "the process mattered as much as the words. Three refusals are "
            "part of the method: do not rush it, do not announce or install "
            "it, and do not ignore it once written."
        ),
        caveat=(
            "You do not invent a mission, Covey says, quoting Frankl — you "
            "detect it. So the work is listening rather than composing. A "
            "statement written quickly out of impressive words reads "
            "impressively and does nothing, because you will not recognise "
            "yourself in it when a real decision arrives."
        ),
        img="img/action-01.png",
        alt=(
            "Two panels. In the first, a stick figure at a slanted drafting "
            "table pencils a house in outline on a large sheet marked at its "
            "four corners TIMELESS, ENDS AND MEANS, FOUR NEEDS, ALL ROLES. In "
            "the second, the house stands built with its door open, a stick "
            "figure in the doorway, and the same sheet pinned to the wall just "
            "inside where it can be seen."
        ),
    ),
    dict(
        n=2,
        title="Plan the week from your roles, and let the calendar stay soft",
        lede=(
            "Six steps, in order. Connect to your mission — the burning yes "
            "that gives you the ability to say no. Review the roles of your "
            "life; most are relationships. Select one or two goals for each "
            "role. Organize weekly: the week is the right unit, large enough "
            "for perspective and small enough to see how each day contributes, "
            "where a day is small enough that you end up prioritizing crises. "
            "Exercise integrity in the moment of choice — hard on principles, "
            "soft on scheduling. Then evaluate and adjust."
        ),
        operative=(
            "The point of doing it by role is what lands in the week. Ask the "
            "two questions Covey asks audiences: name one activity in your "
            "personal life that you know, if done consistently and superbly "
            "well, would produce marvellous results, then name one for your "
            "work. The answers barely vary — preparation, prevention, "
            "planning, relationship building, deep communication with the key "
            "people. All of it is Quadrant Two, which is exactly why none of "
            "it is happening."
        ),
        caveat=(
            "The reason to schedule the important things is not control, it is "
            "permission. Once your daughter's evening and your exercise are on "
            "the week, you can decline the urgent-but-unimportant without "
            "negotiating with yourself each time, and people who sense that "
            "orientation stop bringing you those requests. If it is your boss "
            "asking, note Covey's rule: what is important to another person "
            "must be as important to you as that person is to you — which "
            "promotes it rather than exempting you."
        ),
        img="img/action-02.png",
        alt=(
            "Three panels. A stick-figure hand holds a compass whose needle "
            "swings toward a hanging tag reading MISSION. Next, four tags hang "
            "in a column — FATHER, MANAGER, NEIGHBOR, SELF — each with a solid "
            "black block beside it. Last, seven tall columns like the days of "
            "a week, with those four blocks set in first and small circles "
            "filling the space left around them."
        ),
    ),
    dict(
        n=3,
        title="Delegate the result, never the method — in five parts",
        lede=(
            "Set the agreement in five elements. A clear description of "
            "desired results, visual if possible, given real time. Guidelines, "
            "including the known failure paths — tell people where the "
            "quicksand is, but not which route to walk. Resources: who and "
            "what they can call on. Accountability: when you will review, and "
            "against what. And consequences, intrinsic or extrinsic, following "
            "from that accountability."
        ),
        operative=(
            "Covey's illustration is his young son and the lawn. The job was "
            "green and clean — not watering, which is a method. Two weeks of "
            "training to establish what green and clean looked like. Who is "
            "your boss, son? You boss yourself. Who judges you? I judge "
            "myself. Then a fortnight of nothing: yellowing grass, garbage on "
            "the lawn. Covey wanted to order him out there and knew the cost — "
            "the moment you do, you kill the goose, and what happens tomorrow "
            "when you are not there? He bit his tongue and reaffirmed his "
            "purpose: raise boys, not grass. On the walk around the yard the "
            "boy broke down and asked for help; they filled two sacks. He "
            "asked twice more all summer, and the yard was better kept than it "
            "had ever been under Covey."
        ),
        caveat=(
            "You cannot hold people responsible for results if you supervise "
            "their methods. That is the whole trade, and it means the hard "
            "part is not the setup but the fortnight of watching it not "
            "happen. Do not set the agreement in a rush, and never delegate "
            "when you are angry. Covey's experience was that where the "
            "relationship is good, people are twice as tough on themselves as "
            "you would dare to be."
        ),
        img="img/action-03.png",
        alt=(
            "Two panels. In the first, a tall and a short stick figure hold a "
            "card between them reading GREEN AND CLEAN, ticked down its right "
            "edge RESULT, LIMITS, HELP, CHECK-IN, PAYOFF, while the tall "
            "figure holds a coiled hose in its other hand, away from the card. "
            "In the second, the short figure stands on a mown lawn holding the "
            "same card overhead, with a hose, a bucket and a rake laid out "
            "beside it, and the tall figure standing well back at the edge."
        ),
    ),
    dict(
        n=4,
        title="Listen until they would say you got it, then ask for your turn",
        lede=(
            "In your next difficult conversation, do not prepare a reply while "
            "the other person talks. Lay aside your own views long enough to "
            "enter their world, and stay there until they would agree you have "
            "understood — their meaning, not your paraphrase of it. Then, and "
            "only then, ask to be understood in return. The sequence is the "
            "habit, and most people reverse it without noticing, because the "
            "tendency is to listen with the intent to reply."
        ),
        operative=(
            "Covey's argument for why it works is physical. Take the air out "
            "of the room you are in and your interest in everything else "
            "vanishes instantly; get it back and it stops motivating you at "
            "all. A satisfied need no longer motivates. The emotional "
            "equivalent of air is feeling understood, and until a person has "
            "it, nothing else you offer will land. This is also the whole of "
            "influence: the key to having influence with another person is "
            "that they have had influence with you."
        ),
        caveat=(
            "It cannot be run as a technique, and the failure is instructive. "
            "A professor friend of Covey's, desperate about a rebellious son, "
            "took the class and went home to say he wanted to understand. You "
            "have never understood me, the son said, and walked out. Covey "
            "told him the boy was testing his sincerity and had found the "
            "answer: you don't want to understand your boy, you want your boy "
            "to shape up. He went back to work on himself until it made no "
            "difference what the response was. What opened the door was not a "
            "listening move but an apology for having embarrassed the boy in "
            "front of his friends. The next day the father said, last night I "
            "found my son again."
        ),
        img="img/action-04.png",
        alt=(
            "Three panels of the same two seated stick figures. In the first, "
            "the listener holds a large cone to its own head aimed at the "
            "speaker, mouth closed, a folded note in its other hand, and the "
            "speaker's chest is drawn narrow. In the second the cone is still "
            "aimed and the speaker's chest is full and round, arrowed AIR. In "
            "the third the cone is gone, the listener holds the note open, and "
            "the speaker leans forward toward it."
        ),
    ),
    dict(
        n=5,
        title="Sharpen the saw in four dimensions, before the blade goes",
        lede=(
            "Renew four dimensions on a regular schedule. Physical is "
            "exercise, nutrition and stress management. Mental is reading and "
            "writing — Covey suggests a book a month working up to a book a "
            "week, read outside your comfort zone, plus a journal and letters. "
            "Spiritual is private and everyone does it differently: working "
            "the mission statement, time in nature, the literature that "
            "inspires you, renewing your commitments. Social-emotional happens "
            "largely at home, in shared meals, traditions, laughter and "
            "listening."
        ),
        operative=(
            "The leverage is the argument. A few hours out of a week of a "
            "hundred and sixty-eight affect the quality of every other hour. "
            "Covey says the main benefit of physical exercise is not fitness "
            "but what it does to your self-esteem and your sense of being in "
            "control, and the spillover into the other three dimensions. He "
            "argues, in the language of the stress researcher Hans Selye, that "
            "meaningful work produces eustress rather than distress, and that "
            "the stress of a repeatedly violated conscience far exceeds the "
            "stress of deadlines. The most powerful single move he names in "
            "the social-emotional dimension is to begin rebuilding one broken "
            "relationship — reach for the one that tests you most."
        ),
        caveat=(
            "Habit seven sits in Quadrant Two, which is precisely why it is "
            "the first thing dropped: it never acts on you, so you must act on "
            "it. The man sawing the tree has been at it three hours; asked why "
            "he does not sharpen the saw, he says he is too busy sawing. "
            "Nothing about that answer is stupid. It is what urgency does to "
            "anyone who has not scheduled the alternative."
        ),
        img="img/action-05.png",
        alt=(
            "Two panels. In the first, a stick figure grips a saw whose four "
            "teeth are visibly different lengths, arrowed BODY, MIND, SPIRIT "
            "and PEOPLE, and its cut into the log has stalled at the depth the "
            "shortest tooth reaches. In the second, the same figure runs a "
            "file along the teeth, now all filed to equal length, and the log "
            "lies cut clean through in two pieces."
        ),
    ),
)


# ---------------------------------------------------------------------------
# Quick reference
# ---------------------------------------------------------------------------

QUICK_REFERENCE = (
    ("The shape",
     "1–3 are the private victory, dependence to independence. 4–6 are the "
     "public victory, independence to interdependence. 7 renews all six. The "
     "order cannot be swapped."),
    ("Effectiveness",
     "P/PC balance — the golden eggs against the health of the goose. Getting "
     "it in a way that lets you get it again."),
    ("Habits 1–3, the private victory",
     "Be proactive: between stimulus and response is a space; work the circle "
     "of influence. Begin with the end in mind: everything is created twice, "
     "so write the mission statement. Put first things first: compass, not "
     "clock; live in Quadrant Two."),
    ("Habits 4–6, the public victory",
     "Think win-win: abundance, and win-win or no deal. Seek first to "
     "understand: feeling understood is air. Synergize: get to the underlying "
     "purposes, then invent the third alternative."),
    ("Habit 7 — Sharpen the saw",
     "Physical, mental, spiritual, social-emotional. A few hours a week "
     "improve the other hundred and sixty."),
    ("Four mission-statement criteria",
     "Timeless, so no goals in it. Ends and means. All four needs — live, "
     "love, learn, leave a legacy. Every role you hold."),
    ("Six-step weekly plan",
     "Connect to mission. Review roles. Set goals per role. Organize the week. "
     "Integrity in the moment of choice. Evaluate."),
    ("Five parts of a stewardship agreement",
     "Desired results. Guidelines and known failure paths. Resources. "
     "Accountability. Consequences. Delegate the result, never the method."),
    ("Deposits that count most",
     "Understand their frame of reference first. Promises sparingly made. "
     "Small kindnesses. Clear expectations. Loyalty to the absent. I-messages, "
     "not you-messages. Apology. Forgiveness."),
)

CLOSING_LINE = (
    "The Chinese bamboo shows a bulb and a shoot for four years, and in the "
    "fifth grows eighty feet. All of the early growth went below the ground."
)


# ---------------------------------------------------------------------------
# BOOK — assembled for build_page.py / build_pdf.py
# ---------------------------------------------------------------------------

def _entry(kind, d):
    e = {
        "id": "%s-%d" % (kind, d["n"]),
        "n": d["n"],
        "title": d["title"],
        "lede": d["lede"],
        "plate": d["img"],
        "alt": d["alt"],
    }
    if kind == "insight":
        e["evidence"] = d["evidence"]
        e["operative"] = d["operative"]
    else:
        e["operative"] = d["operative"]
        e["caveat"] = d["caveat"]
    return e


BOOK = {
    "slug": SLUG,
    "title": TITLE,
    "subtitle": SUBTITLE,
    "author": AUTHOR,
    "cover": COVER,
    "argument": {
        "question": CENTRAL_QUESTION,
        "answer": CENTRAL_ANSWER,
    },
    "framework": {
        "name": FRAMEWORK_NAME,
        "intro": FRAMEWORK_INTRO,
        "steps": [
            {"mark": m, "term": t, "gloss": g} for (m, t, g) in FRAMEWORK_STEPS
        ],
    },
    "vocabulary": {
        "intro": VOCABULARY_INTRO,
        "terms": [{"term": t, "def": d} for (t, d) in DEFINITIONS],
    },
    "insights": [_entry("insight", d) for d in INSIGHTS],
    "actions": [_entry("action", d) for d in ACTIONS],
    "quickReference": [{"kind": "line", "label": h, "text": b} for (h, b) in QUICK_REFERENCE],
    "closingLine": CLOSING_LINE,
    "links": [
        {"mark": "↓", "label": "Spoken Companion", "href": "Spoken_Companion.docx"},
    ],
}


# ---------------------------------------------------------------------------
# TAKEAWAY — one line per entry, 20 words maximum. Applied after BOOK is built.
# ---------------------------------------------------------------------------

TAKEAWAY = {
    "insight-1": "Technique is the tip above the water. It holds exactly as long as the character underneath holds.",
    "insight-2": "You can cram for a test because a test has a grader. A marriage does not.",
    "insight-3": "One sentence about a dying mother, and the irritation was gone. The map moves before the mood does.",
    "insight-4": "Cutting the goose raises production first and ends it later. The early numbers always argue for continuing.",
    "insight-5": "Work inside what you can affect and it widens. Work outside it and it withers.",
    "insight-6": "The same sentence is a gift at a full account and a threat at an empty one.",
    "action-1": "Write it as if it can never change: no goals, ends and means, four needs, every role.",
    "action-2": "Pick goals by role, put them on the week first, then keep the schedule soft.",
    "action-3": "Agree the result, the failure paths, the resources, the review and the consequence. Then leave the method alone.",
    "action-4": "Stay in their world until they would say you got it. Feeling understood is air.",
    "action-5": "Four dimensions, a few hours a week. It never acts on you, so you act on it.",
}

for _e in BOOK["insights"] + BOOK["actions"]:
    _e["takeaway"] = TAKEAWAY[_e["id"]]


# ---------------------------------------------------------------------------
# LETTERING — the exact hand-lettered title each image prompt asks for.
# verify_lettering.py scores each plate against every one of these.
# ---------------------------------------------------------------------------

LETTERING = {
    "insight-1": "POLISHING THE TIP",
    "insight-2": "CRAMMING THE HARVEST",
    "insight-3": "YOU ARE THE PROJECTOR",
    "insight-4": "THE QUARTER IT WENT UP",
    "insight-5": "PUSH FROM THE INSIDE",
    "insight-6": "IT ARRIVES AS THE BALANCE",
    "action-1": "BLUEPRINT BEFORE BRICK",
    "action-2": "ROLES INTO THE WEEK",
    "action-3": "GREEN AND CLEAN",
    "action-4": "AIR FIRST, THEN WORDS",
    "action-5": "FOUR TEETH ON THE SAW",
}


# ---------------------------------------------------------------------------
# COMPANION — the Spoken Companion text. build_docx.py renders this;
# the text is never written straight to a .docx.
# ---------------------------------------------------------------------------

COMPANION_FOOTER = "The 7 Habits of Highly Effective People — Spoken Companion"

COMPANION = [
    {"level": 1, "heading": "The Ground Underneath", "paras": []},

    {"level": 2, "heading": "What Was Traded Away", "paras": [
        "Start with a piece of research rather than a promise. In 1976 I set "
        "out to study the success idea in America and how it had changed, so I "
        "went into the popular success literature and read back two hundred "
        "years. The finding was clean enough to be uncomfortable. For the "
        "first hundred and fifty years, almost the entire literature was about "
        "character. Integrity. Fidelity. Courage. Compassion. Contribution. "
        "Responsibility. Justice. Service.",

        "Then, in the early nineteen hundreds and especially through the "
        "twenties and thirties, the emphasis shifted. It moved off character "
        "and onto personality — technique, image, the management of how you "
        "come across. Away from how to be, and toward how to appear to be. "
        "North Carolina's state motto names precisely what got traded: to be "
        "rather than to seem.",

        "Picture the personality ethic as the tip of an iceberg — the part "
        "above the water, the part other people can see, and there is nothing "
        "fraudulent about it. But most people give all their energy to the "
        "tip, and the tip is held up by the enormous mass underneath, which is "
        "where nobody is working. Everything in this program runs the other "
        "direction. Inside out. Character first, then technique.",
    ]},

    {"level": 2, "heading": "You Cannot Cram on a Farm", "paras": [
        "Ask yourself honestly whether you crammed in school. Most people did. "
        "Ask whether you got good at it, and most people did that too. Now ask "
        "whether you have ever crammed on a farm — forgotten to plant in the "
        "spring, flaked off all summer, then hit it hard in the fall to bring "
        "in the harvest. The question is ridiculous, and everyone knows why "
        "instantly. A farm is a natural system. It is governed by principles.",

        "So here is the real question. Is the development of your mind more "
        "like the test or more like the farm? Is it possible to get a degree "
        "and not get an education? Of course it is. Your health, your "
        "character, your marriage, your reputation — all farms, all governed "
        "by the law of the harvest rather than by whatever behavior happens to "
        "be popular.",

        "A principle is a natural law: universal, self-evident, changeless, "
        "governing whether or not you agree with it. Values are what you "
        "happen to hold; principles are how the world actually runs, and the "
        "work is aligning the one with the other. Which puts control in an "
        "uncomfortable place. The popular language says get in control, you "
        "are the master of your own destiny. But we control our actions; the "
        "consequences that flow from those actions are controlled by "
        "principles. Accept that, follow them, and you are master of your "
        "destiny in the only sense available — a humble one. People pass away, "
        "Lincoln said, but principles never will.",
    ]},

    {"level": 2, "heading": "A Man on a Subway", "paras": [
        "A paradigm is the mental map you carry of the way things are. It "
        "comes out of your background and your experience, and you do not "
        "experience it as a map. You experience it as reality. We all think we "
        "see the world as it is. We see the world as we are. When you describe "
        "another person, you are describing your own frame of reference and "
        "then projecting it outward.",

        "One Sunday morning I was on a subway in a large city. Quiet car, "
        "sedate. Then several children ran on, and their father came in after "
        "them and sat down right next to me. The children went wild — up and "
        "down the car, shoving people's newspapers aside, loud and rude. And "
        "the father did nothing at all.",

        "I sat there thinking, I can't believe this man. I kept the "
        "irritation off my face for a few minutes and then it went into my "
        "behavior anyway. Sir, I said, do you think you could control your "
        "children a little? They're very upsetting to people.",

        "He lifted his head as if he had only just arrived. Oh, he said. Yes. "
        "I guess I should. We just left the hospital. Their mother died about "
        "an hour ago. I don't know how to take it, and I guess they don't "
        "either.",

        "Nothing on that train changed. One sentence arrived, and my whole "
        "view of the situation shifted about a hundred and eighty degrees. The "
        "irritation was gone, and all I wanted was to help him.",

        "Now notice what happened, because it is the mechanism. My attitude "
        "and my behavior both changed, and I applied no effort to either. They "
        "are downstream. Paradigms are upstream, which is why most development "
        "programs go to work on the two things that move last. The fastest way "
        "to change what a person does is to change how they see their own "
        "role. Anyone who has become a parent for the first time, or a manager "
        "for the first time, has watched the whole world reorganize overnight "
        "without a single exercise in attitude.",
    ]},

    {"level": 2, "heading": "The Goose Is the Point", "paras": [
        "Aesop's poor farmer finds a golden egg beside his goose, and another "
        "the next day, and another, and becomes fabulously wealthy. He also "
        "becomes impatient. He wants all of them now, so he kills the goose to "
        "get at them, and finds nothing inside.",

        "That fable is the whole definition of effectiveness, and I use "
        "effectiveness rather than success because success carries too much of "
        "the old having-it-all baggage. Effectiveness has two parts: getting "
        "what you want, and getting it in a way that lets you get it again and "
        "again. Call it P/PC balance. P is production — the golden eggs. PC is "
        "production capability — the health of the goose.",

        "There was a clam chowder house near me so popular you could hardly "
        "get near it from eleven until two. New management came in, kept the "
        "name, and watered down the chowder. For a month or so the bottom line "
        "climbed, because all the cost of the quality had been saved. Then the "
        "loyalty of the customer base liquidated itself. They tried to bring "
        "it back, and people would not return and would not believe it was the "
        "same chowder.",

        "Notice the shape of that. Cutting capability raises production first "
        "and destroys it later, so the early evidence always argues for "
        "continuing. Cut training, careful selection, orientation, research, "
        "development, every form of people development, and you can double or "
        "quadruple the bottom line of any organization for a quarter or two. "
        "Look at all those golden eggs.",

        "The same balance runs through your car, your body, your mind and your "
        "marriage.",
    ]},

    {"level": 2, "heading": "The Account You Are Always Drawing On", "paras": [
        "Every relationship carries a balance, and I call it the emotional "
        "bank account. Courtesy, kindness, honesty and kept commitments are "
        "deposits, and a reserve lets your mistakes be absorbed, because the "
        "other person already knows you care. Discourtesy, cutting people off, "
        "overreacting, betraying a confidence, failing to do what you said — "
        "those are withdrawals.",

        "Run the account overdrawn and something specific happens: your "
        "communication stops working even when it is perfectly clear. People "
        "read between the lines and look for the hidden agenda. A small "
        "mistake gets blown out of all proportion. It is walking on "
        "minefields, measuring every word, and whole families and "
        "organizations live in that climate.",

        "The first and most important deposit is to understand the other "
        "person from within their frame of reference, because until you do you "
        "have no idea what counts as a deposit to them. The common error is to "
        "project — to assume that what lands well with you lands well with "
        "them. You are a subjective person and so are they.",

        "After that, the currency is unglamorous. Make promises sparingly and "
        "count the cost first, because the moment you make one you have "
        "created a hope, and a person holding a hope is vulnerable. Clarify "
        "expectations, particularly roles and goals: nearly every breakdown in "
        "a family or an organization traces back to expectations that were "
        "ambiguous or violated. Be loyal to the absent. And give feedback as "
        "an I-message — my concern is, my perception is — rather than a "
        "you-message, which plays judge of another person's character and "
        "turns them into a thing.",

        "Two more go deeper than technique. Apologize completely — I was "
        "wrong, that was unkind, please forgive me — without the defending and "
        "explaining that people hear a mile off. And forgive, when the apology "
        "never comes. It isn't the snake that bites us that does the serious "
        "harm; it's chasing the snake that drives the poison to the heart.",
    ]},

    {"level": 1, "heading": "The Private Victory", "paras": []},

    {"level": 2, "heading": "The Space Between", "paras": [
        "Habit one is be proactive, and it means your life is a product of "
        "your values rather than your feelings, of your decisions rather than "
        "your conditions. In the computer metaphor: you are the programmer. "
        "The opposite is reactive — your life as a function of your moods, "
        "your impulses, or how other people treated you this morning. The word "
        "is not passive; a reactive person can be extremely busy. The "
        "distinction is responsibility. Response-ability.",

        "Viktor Frankl, the Austrian psychiatrist, was imprisoned in the Nazi "
        "death camps, having been raised in a tradition holding that a person "
        "is essentially a product of childhood and can do nothing about it. In "
        "the camps he watched people in identical circumstances behave as "
        "animals and behave as saints, and he discovered what he called the "
        "last of the human freedoms: the power to choose your response to any "
        "condition.",

        "Between what happens to us and our response to it, there is a space. "
        "In that space lies our freedom and our power to choose. And in those "
        "choices lie our growth and our happiness.",

        "A man told me once that the love had simply gone out of his marriage. "
        "I said, love her. He said the feeling isn't there. I said, love her. "
        "He asked how you love when you don't love, and here is the answer: "
        "love is a verb. The feeling is the fruit of the verb. Study the great "
        "literature of any enduring civilization and show me where love is "
        "fundamentally a feeling — it is Hollywood that teaches that. Sacrifice "
        "for her. Serve her. Give of yourself. The feeling comes in the "
        "process of the serving. He did not like that, because it is much "
        "easier to be absolved by saying you don't feel it.",
    ]},

    {"level": 2, "heading": "The Circle That Grows", "paras": [
        "Draw two circles, one inside the other. The outer one is your circle "
        "of concern: the weather, world events, another person's temperament — "
        "everything you can do nothing about. The inner one is your circle of "
        "influence: your health, your family, your work, the things you can "
        "actually affect. Proactive people put their energy in the inner "
        "circle, and the inner circle grows. Reactive people put their energy "
        "in the outer circle, and the inner circle withers.",

        "I worked four years as assistant to a president who was visionary, "
        "talented and thoroughly dictatorial. Everyone around him felt treated "
        "as an errand runner, and they sat in the executive corridor swapping "
        "stories about him — cement that felt like it held them together while "
        "it quietly broke every relationship in the building.",

        "One man, Ben, put the president's weaknesses in his circle of concern "
        "where they belonged and got on with being the best errand runner in "
        "the building. Sent for data, he brought the data, his analysis, his "
        "recommendations, and a presentation ready to give to the board. "
        "Within four years he was the second person in the organization, and "
        "the president would not make a significant move without him. The "
        "corridor concluded there was favoritism.",
    ]},

    {"level": 2, "heading": "Write the Program", "paras": [
        "If habit one says you are the programmer, habit two says write the "
        "program. Don't live out someone else's and then blame them for how "
        "poor it was.",

        "Everything is created twice — first mentally, then physically. The "
        "room you are sitting in was created in detail on paper before anyone "
        "cut anything. The carpenter's rule is measure twice, cut once, which "
        "is really an instruction about making sure the first creation is what "
        "you actually want. Skip it and you spend a career climbing a ladder "
        "leaning against the wrong wall.",

        "The highest expression of habit two is a mission statement — "
        "personal, then family, then organizational. It should carry vision, "
        "the picture of what you are about, and principles, how you go about "
        "it. Four criteria make one usable. It should be timeless, which means "
        "no goals in it: goals and strategies change with the situation, and "
        "the mission statement is the part that doesn't. It should deal with "
        "both ends and means, because you cannot reach a worthy end by an "
        "unworthy means. It should address all four human needs: to live, to "
        "love, to learn, and to leave a legacy. And it should cover every role "
        "you hold, so no part of your life is quietly left out of your own "
        "plan.",

        "You don't invent your mission, as Frankl said. You detect it. So the "
        "work is listening rather than composing — to yourself, to people who "
        "see potential in you, to the lives of people you admire, asking "
        "exactly what you admire about them. Give it weeks, and give a family "
        "statement months; ours took eight, with everyone involved. Three "
        "refusals: don't rush it, don't announce or install it, and don't "
        "ignore it once it exists.",
    ]},

    {"level": 2, "heading": "A Compass, Not a Clock", "paras": [
        "Habit three is where you run the program. Habit two decides what the "
        "first things are; habit three is the discipline of living by them, "
        "which makes it the test of integrity — whether you walk your talk.",

        "The traditional paradigm of time management is scheduling, control "
        "and efficiency, and its symbol is the clock. Have you ever tried to "
        "be efficient with someone you love about a difficult issue? With "
        "people, fast is slow and slow is fast. Efficiency belongs with "
        "things; effectiveness belongs with people, and people are not things. "
        "So the symbol is a compass rather than a clock, and the first things "
        "are almost always relationships.",

        "Here is the sorting tool. Importance comes from inside you — your "
        "values, your mission. Urgency comes from the environment and is often "
        "extremely popular. Cross the two. Quadrant one is urgent and "
        "important: crises, deadlines, fires. Quadrant two is important and "
        "not urgent: prevention, preparation, planning, relationship building, "
        "self-development, mission. Quadrant three is urgent and not "
        "important. Quadrant four is neither.",

        "Now do the exercise. Name one activity in your personal life that "
        "you know, if done consistently and superbly well, would produce "
        "marvellous results, and then name one for your work. I have run this "
        "all over the world and the answers barely vary: preparation, "
        "prevention, planning, relationship building, deep communication with "
        "the key people in your life. Every one of them is in quadrant two.",

        "So why aren't you doing them? Because they are not urgent. Our "
        "culture has so thoroughly defined urgent as important that quadrant "
        "two becomes the item called other business at the end of the agenda "
        "and gets pushed off by one and three every time. The time for it "
        "comes out of three and four, which means learning to say a smiling "
        "no.",

        "Six steps, in order. Connect to your mission — that is where the "
        "burning yes lives that makes a no possible. Review your roles. Select "
        "a goal or two for each role. Organize weekly, because the week is the "
        "right unit; a day is small enough that you only prioritize crises. "
        "Exercise integrity in the moment of choice — hard on principles, soft "
        "on scheduling. Then evaluate and adjust.",

        "Built that way, the date with your daughter and the exercise and the "
        "time with your spouse are already on the week. You adapt on "
        "conscience when something arrives, but from a plan rather than from "
        "nothing.",
    ]},

    {"level": 1, "heading": "The Public Victory", "paras": []},

    {"level": 2, "heading": "Enough to Go Around", "paras": [
        "Habit four is think win-win, and its underlying principle is "
        "abundance: there is plenty out there and to spare. If you believe "
        "that, another person's strength is not a threat — you can nurture "
        "competence around you higher than your own, and share knowledge, "
        "recognition and gain.",

        "Scarcity is the other paradigm, and it is exhausting: if worth comes "
        "from how you compare, sharing anything feels like losing some of it, "
        "and you end up thinking in dichotomies. Win or lose. Tough or soft.",

        "A man told me win-win was ivory-tower idealism: they had renegotiated "
        "their mall leases on my advice, been open and conciliatory, and been "
        "taken to the cleaners. I asked why they went for lose-win. We went "
        "for win-win, he said. Didn't you just tell me they took you to the "
        "cleaners? Being nice is not win-win. Win-win is tougher than "
        "win-lose, because you have to be tough on yourself: cultivate the "
        "empathy and the openness and at the same time refuse to capitulate.",

        "The honest exit is part of the habit. Win-win or no deal: if we can't "
        "find a mutual win, we agree to disagree agreeably, and perhaps come "
        "together later on something else. Holding that option is what lets "
        "you be completely open, with no hidden negotiating technique, because "
        "there is nothing you need to extract.",

        "Where win-win becomes concrete is in agreements. I gave my young son "
        "our lawn, and the job was green and clean — not watering, which is a "
        "method. Two weeks of training to establish what green looked like and "
        "what clean looked like, and then a fortnight of yellow grass and "
        "garbage while I bit my tongue and reaffirmed the purpose: raise boys, "
        "not grass. He broke down on our agreed walk around the yard, asked "
        "for help, and we filled two sacks together. He asked twice more all "
        "summer, and the yard was better kept than it had ever been under me. "
        "Had I ordered him out there instead, he would have cleaned it up "
        "that day — and what happens tomorrow, when I'm not there?",

        "Five elements made that an agreement rather than an instruction. A "
        "clear description of desired results, visual if possible. Guidelines, "
        "including the no-nos — tell people where the quicksand is, but not "
        "which route to walk. Resources. Accountability. Consequences. "
        "Underneath all five sits one rule: you cannot hold people responsible "
        "for results if you supervise their methods. Never delegate when "
        "you're angry, and know that where the relationship is good people are "
        "twice as tough on themselves as you would dare to be.",
    ]},

    {"level": 2, "heading": "Air", "paras": [
        "Habit five is seek first to understand, then to be understood, and "
        "the whole habit is the sequence. Notice your own tendency: most of us "
        "listen with the intent to reply rather than the intent to understand.",

        "Take the air out of the room you are in right now and ask how "
        "interested you would be in anything else. Then get it back — does air "
        "motivate you now? No. A satisfied need no longer motivates. The "
        "emotional equivalent of air is feeling understood, and until people "
        "have it, nothing else you offer will reach them, because inside they "
        "are still saying he doesn't understand.",

        "That is also the whole story of influence: the key to having "
        "influence with another person is that they have had influence with "
        "you. Carl Rogers put the cost honestly — you lay aside your own views "
        "and values to enter another's world, which only someone secure enough "
        "not to get lost in there can afford to do.",

        "The barrier is efficiency. Entering your world costs me control, so I "
        "learn to look attentive — meet your eyes, tilt my head, nod — and go "
        "on preparing my reply. If I were to fault myself most on these seven "
        "habits, it would be right there.",

        "A friend of mine, a professor whose office was near mine, was "
        "wretched over a rebellious son — a boy who would walk out when his "
        "father came in to watch television, then come back and switch it off. "
        "I told him to come to my class, because my guess was his son did not "
        "feel understood. He came, caught it fast, and went home within days. "
        "Son, I need to listen to you. I don't think I understand you, and I "
        "want to. And the boy said, you have never understood me. Ever. And "
        "walked out.",

        "My friend was stunned — I made all that effort and that's how he "
        "treats me. I told him the boy was testing his sincerity and had found "
        "his answer. Listen to your own anger, I said. You don't want to "
        "understand your boy; you want your boy to shape up. You cannot run a "
        "technique on the surface over that. You have to pay a much bigger "
        "price inside yourself, until it makes no difference what his response "
        "is. You do it because it's right, not because it works.",

        "He went back to work on it, and it took far longer than a few weeks. "
        "When he tried again the boy rejected him again — and as the boy was "
        "leaving the room, my friend said, I'll say one thing, son. I'm sorry "
        "for the way I embarrassed you in front of your friends the other "
        "night.",

        "The boy spun around. You have no idea how much that embarrassed me. "
        "And he teared up. My friend told me that nothing in the training had "
        "touched him the way that did, because until that moment he had not "
        "known the boy cared. They talked until very late, and when the mother "
        "came in to say it was bedtime the son said, Mom, we want to talk, "
        "don't we, Dad. The next day in the hallway my friend said to me: last "
        "night I found my son again.",
    ]},

    {"level": 2, "heading": "The Third Alternative", "paras": [
        "Habit six is synergize, the fruit of four and five. When people "
        "genuinely open to each other's influence, something appears between "
        "them that neither brought in. The whole becomes greater than the sum "
        "of the parts — one plus one equals three, or ten. Compromise is one "
        "plus one equals one and a half, and it is not the same thing. "
        "Negative synergy is real too: enough energy into contention and two "
        "people produce less than one of them alone.",

        "Fisher and Ury describe two people fighting over a window. One wants "
        "it open, one wants it closed. He opens it, leaves; she closes it; he "
        "comes back and opens it again. There appear to be exactly two "
        "positions, plus a compromise — open halfway, or open half the time — "
        "and nobody is happy with any of them.",

        "But they don't yet understand the problem, and you cannot find "
        "solutions until you know each person's underlying purpose. So: what "
        "are you after? Fresh air, without which I feel claustrophobic. And "
        "you? The breeze scatters my working papers. Now there are not two "
        "positions in the room, there are two needs, and the question becomes "
        "what could give fresh air without a draft across that desk. Move both "
        "desks so the window can be seen and open while the papers sit out of "
        "the airflow. Neither person arrived with that.",

        "The key to habit six is to value differences — not tolerate them, not "
        "respect them because a program says to, but genuinely prize them, "
        "because the difference is where the creative material is. When "
        "someone disagrees with you, train yourself to say: good, you see it "
        "differently. Help me understand.",

        "There is a condition on this. Differences are only creative where a "
        "common vision and a shared set of principle-centred values sit "
        "underneath them; without that they produce chaos and spawn more "
        "prejudice. Which is why four, five and six rest on the integrity "
        "built in one, two and three.",
    ]},

    {"level": 1, "heading": "Renewal", "paras": []},

    {"level": 2, "heading": "Too Busy Sawing", "paras": [
        "What are you doing? Can't you see I'm sawing down this tree. I'll bet "
        "you're tired. Boy, I'll say — I've never been so tired. How long have "
        "you been at it? Two, three hours. Well, why don't you sharpen the "
        "saw? I'm too busy sawing.",

        "Habit seven is renewal, in four dimensions: the body, the mind, the "
        "spirit, and our relationships — the social and emotional side. Study "
        "history, philosophy, religion or psychology and the same four keep "
        "appearing.",

        "Physical is exercise, nutrition and stress management. The main "
        "benefit of exercise, in my view, is not fitness — it is what happens "
        "to your self-esteem and your sense of being in control, and the "
        "spillover into the other three dimensions. On stress, the most "
        "powerful idea I have encountered is having a sense of meaning and "
        "integrity around a value system. The stress of a conscience violated "
        "again and again far exceeds the stress of deadlines and a dozen balls "
        "in the air.",

        "Mental is reading and writing. A book a month working toward a book a "
        "week, read outside your comfort zone. What exercise is to the body, "
        "reading is to the mind — but writing is concentrated mental exercise, "
        "because you have to gather and distill and crystallize a thought into "
        "words for another person's mind. Keep a journal. Write letters. Most "
        "professions are estimated to have a half-life of about four years, so "
        "none of this is a hobby.",

        "Spiritual is private and everyone does it differently: working the "
        "mission statement until it settles into your core, time in nature, "
        "the literature that inspires you, renewing your commitments to what "
        "is sacred to you. Reading that edifies also educates the conscience, "
        "which is what makes it possible to say no when saying yes would be "
        "easy.",

        "Social-emotional is largely the home: meals together, traditions, "
        "playing, laughing, listening, lifting each other up. And the single "
        "most powerful step available is to begin "
        "rebuilding one broken relationship you care about — reach for the one "
        "that tests you the most. Dag Hammarskjöld said it is more noble to "
        "give yourself completely to one individual than to labour diligently "
        "for the salvation of the masses. The key to the ninety-nine is the "
        "one, because everyone is a one.",

        "Habit seven has more leverage than any other activity I know: a few "
        "hours out of a week of a hundred and sixty-eight change the quality "
        "of every other hour. And it sits in quadrant two, which is why it is "
        "the first thing dropped. It does not act upon us, so we must act upon "
        "it.",
    ]},

    {"level": 2, "heading": "Below the Ground", "paras": [
        "Teach it to someone. When you teach once you learn twice, and it "
        "unfreezes the labels people have of you.",

        "Consider the Chinese bamboo. You plant it and for four years you see "
        "a bulb and a little shoot and nothing else, while you tend it daily. "
        "In the fifth year it grows as much as eighty feet, because all the "
        "earlier growth went below the ground. The private victory of habits "
        "one, two and three is the part below the ground; four, five and six "
        "are what shows.",

        "How do you know these principles are universal? Try arguing against "
        "one. Picture a highly effective person with no sense of "
        "responsibility, no vision, no integrity, no mutual respect, no mutual "
        "understanding, no creative cooperation, no renewal. You cannot do it, "
        "which tells you that you already know all of this. As Eliot had it, "
        "we must never cease from exploring, and the end of all our exploring "
        "will be to arrive where we began and know the place for the first "
        "time.",
    ]},
]
