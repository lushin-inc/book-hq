# -*- coding: utf-8 -*-
"""
Book HQ — content module for "The Confident Mind (A Battle-Tested Guide to
Unshakable Performance)" by Nathaniel Zinsser.

The durable artifact. build_page.py, build_pdf.py and build_docx.py all read this;
none of them hardcode content. Pass 2 is a re-render of this file, not a rebuild.

Source transcript: The Confident Mind (A Battle-Tested Guide to Unshakable
Performance) Nate Zinsser.txt
"""

SLUG = "confident-mind"
TITLE = "The Confident Mind"
SUBTITLE = "A Battle-Tested Guide to Unshakable Performance"
AUTHOR = "Nathaniel Zinsser"
COVER = "img/cover.jpg"


# ---------------------------------------------------------------------------
# The argument
# ---------------------------------------------------------------------------

CENTRAL_QUESTION = "Where does the certainty you need at the moment of truth actually come from?"

CENTRAL_ANSWER = (
    "Not from what has happened to you. From how you have been thinking about "
    "what has happened to you. Confidence is not a trait, a mood, or a reward "
    "for a good week. It is a running total — the sum of every thought you "
    "have entertained about yourself and your work, changing with each new "
    "entry, and therefore something you deposit into or withdraw from every "
    "hour of every day. That is why a defensive end with ten sacks in ten games "
    "can believe he is terrible, and why a figure skater can fall through his "
    "warm-up and skate a gold-medal program twenty minutes later. Nothing that "
    "happens enters the account directly. A thought about it does, and the "
    "thought is yours to choose. The practical definition follows from this: "
    "confidence is a sense of certainty about your ability that lets you bypass "
    "conscious thought and execute unconsciously. Not a feeling added on top of "
    "the skill — the absence of everything that would get in the skill's way."
)


# ---------------------------------------------------------------------------
# Framework
# ---------------------------------------------------------------------------

FRAMEWORK_NAME = "The Mental Bank Account"

FRAMEWORK_INTRO = (
    "One metaphor carries the whole book, and it is meant literally rather than "
    "poetically. A balance rises and falls by deposits and withdrawals; so does "
    "a sense of certainty. What follows is the account's full operation — what "
    "it sits on, the three sources you fund it from, how it is defended, and "
    "how it is spent. The order matters. You cannot open the vault on game day "
    "and find money you never put in."
)

FRAMEWORK_STEPS = (
    ("1", "The four foundations",
     "Four realities you stop arguing with before any of the rest works: your "
     "thoughts drive your physical state, you will never be perfect, your "
     "nervous system will fire up before anything that matters, and practice "
     "pays out late and unevenly."),
    ("2", "Deposits from the past",
     "Your memory is a video library and you are the editor. The Top 10 list "
     "mines the whole career; the daily ESP entry banks one moment of effort, "
     "one success and one instance of progress; the immediate progress review "
     "carries the best rep of the last drill into the next one."),
    ("3", "Deposits in the present",
     "Affirmations — statements about the reality you want, phrased as if it is "
     "already here. First person, present tense, positive, precise, powerful. "
     "Hung on a trigger you meet constantly, so the count runs into the "
     "thousands rather than the dozens."),
    ("4", "Deposits on the future",
     "Envisioning: a controlled, multi-sensory, emotionally genuine rehearsal "
     "run from inside your own body. Detailed enough that the real arena feels "
     "like a return rather than an arrival."),
    ("5", "Anti-theft",
     "Explain every setback as temporary, limited and non-representative. Get "
     "in the last word on your own negative self-talk — acknowledge it, stop it, "
     "replace it. Then go further with the shooter's mentality, where a miss "
     "makes the next hit feel more likely rather than less."),
    ("6", "Opening the vault",
     "The pre-performance routine: take stock of what is actually in the "
     "account, take stock of the situation — the task, the hidden opponent, the "
     "room — and then decide that you have enough. Saver to spender. Workhorse "
     "to racehorse."),
    ("7", "Spending it, engagement by engagement",
     "CBA before every rep, pitch, shift, patient or meeting. Cue your "
     "conviction with a short powerful phrase, breathe your body, attach your "
     "attention to the one thing that matters right now."),
    ("8", "The audit",
     "The after action review, in three questions. What happened. So what does "
     "that tell you. Now what will you do. It ends by banking the highlights, "
     "which is what makes the next first victory cheaper than the last one."),
)


# ---------------------------------------------------------------------------
# Vocabulary
# ---------------------------------------------------------------------------

VOCABULARY_INTRO = (
    "Most of these are ordinary words used with unusual precision, and the "
    "precision is the point. A performer who has a name for the thing that just "
    "happened in their head can do something about it."
)

DEFINITIONS = (
    ("The first victory",
     "Sun Tzu's phrase, and the book's organising idea: the victory won in your "
     "own mind before you enter the arena. Victorious warriors win first and "
     "then go to war; defeated warriors go to war first and then seek to win."),
    ("Confidence",
     "A sense of certainty about your ability that allows you to bypass "
     "conscious thought and execute unconsciously. Note what is absent from "
     "this definition: any requirement that the certainty be justified."),
    ("The mental bank account",
     "The running total of every thought you have entertained about yourself "
     "and your field. It rises on memories of effort, success and progress, and "
     "falls on replayed setbacks and rehearsed future trouble."),
    ("The daily ESP",
     "A five-minute end-of-day journal entry with three headings: effort, "
     "success, progress. One instance of each, however small. Three deposits "
     "minimum, every day, regardless of what the day looked like."),
    ("Immediate progress review",
     "The same filtering done between activities rather than at the end of the "
     "day. Take the best rep of the drill you just finished into the drill you "
     "are walking to. A dozen small deposits per session instead of one."),
    ("Affirmation",
     "A statement of the reality you want, made in the present tense as though "
     "it is already true. To affirm is to say yes. Five specifications: first "
     "person, present tense, positive, precise, powerful."),
    ("Envisioning",
     "The deliberate production of an emotionally powerful, multi-sensory "
     "imagined experience of a desired event — sight, sound, touch, smell, "
     "position and movement, not pictures alone. Distinguished from daydreaming "
     "by control, detail and genuine feeling."),
    ("Explanatory style",
     "Martin Seligman's term for how you explain the causes of what happens to "
     "you. Pessimists read bad events as permanent, pervasive and personal. The "
     "corrective is to read them as temporary, limited and non-representative."),
    ("The shooter's mentality",
     "Two beliefs held at once, neither of them logical: a miss means the next "
     "one is more likely to go in, and a hit means the next one is too. Not "
     "defensible as probability. Extremely effective as a state of mind."),
)


# ---------------------------------------------------------------------------
# Insights (6 max)
# ---------------------------------------------------------------------------

INSIGHTS = (
    dict(
        n=1,
        title="Certainty is quiet",
        lede=(
            "Confidence is not a loud belief laid over a skill. It is the "
            "absence of everything that would interfere with the skill. The "
            "working definition is a sense of certainty about your ability that "
            "allows you to bypass conscious thought and execute unconsciously — "
            "and the reason it has to be phrased that way is that human beings "
            "are wired to execute well-learned skills without watching "
            "themselves do it."
        ),
        evidence=(
            "The psychologist Sian Beilock offers a demonstration anyone can "
            "run. If you were shuffling quickly down a flight of stairs and "
            "someone asked you to think about exactly what both your knees were "
            "doing, there is a good chance you would end up in a pile at the "
            "bottom. You already perform far more delicate things with total "
            "confidence. Ten fingers tie a shoelace through a sequence of "
            "tensions and releases and leave the right length of lace at the "
            "end, and no part of that reaches your conscious mind."
        ),
        operative=(
            "Conscious, deliberate thought consumes a sizeable portion of the "
            "nervous system's capacity to take in what is happening, retrieve "
            "the right response, and send instructions back out to the hands, "
            "feet, throat and tongue. Every thought about how you are doing is "
            "taken out of the same budget as the doing. This is also why "
            "competence and confidence are different problems. The student who "
            "has learned all the material but doubts she has will not recall it "
            "cleanly, because the chatter blocks the retrieval."
        ),
        img="img/insight-01.png",
        alt=(
            "A flight of stairs in profile. A stick figure part way down, "
            "mid-stride, with a thick line running from its head, looping down "
            "and wrapping twice around its own ankles, pulled taut. At the foot "
            "of the stairs the same stick figure lies sprawled."
        ),
    ),
    dict(
        n=2,
        title="Confidence is a running total, and nothing enters it by itself",
        lede=(
            "It is tempting to think of confidence as a balance that events "
            "adjust for you — win and it goes up, lose and it goes down. It does "
            "not work that way. Nothing that happens to you enters the account. "
            "A thought about what happened enters the account. Success builds "
            "confidence only if you let it, and failure erodes it only if you "
            "let it."
        ),
        evidence=(
            "In 1998 Michael Strahan recorded ten sacks in ten games, coming off "
            "an All-Pro season in which he led the league with fourteen. He told "
            "Sports Illustrated that he thought he sucked, that it was like we "
            "had no hope. Asked what being on the field looked like in his mind, "
            "he described chasing the quarterback, almost getting there, not "
            "getting there, and then everything goes black. Twenty years of "
            "highlights were sitting outside the account because the picture he "
            "replayed was of the near miss."
        ),
        operative=(
            "The same asymmetry runs the other way, which is the encouraging "
            "half. Ilya Kulik's warm-up before the 1998 Olympic short program "
            "was a mess — slips, wobbles, no clean jumps. He skated near-perfect "
            "minutes later and won gold. Asked where the confidence came from, "
            "he shrugged: just from my mind. Two performers, opposite raw "
            "material, and in both cases the balance tracked what they chose to "
            "replay rather than what had actually occurred."
        ),
        img="img/insight-02.png",
        alt=(
            "An open bank vault door with a bare interior and empty shelves. On "
            "the floor outside it, a tall heap of trophies and medals. A stick "
            "figure stands beside the heap looking into the empty vault."
        ),
    ),
    dict(
        n=3,
        title="The jitters are the delivery, not the warning",
        lede=(
            "The racing heart, the sweating palms, the twitching hands and the "
            "stomach turning over are almost universally read as evidence that "
            "something is wrong. They are the opposite. They are the receipt for "
            "a delivery your body just made because it worked out that something "
            "important is about to happen."
        ),
        evidence=(
            "Zinsser lays out the mechanism plainly. The unconscious part of the "
            "brain that registers an upcoming performance signals the adrenal "
            "glands, two small wads of tissue above the kidneys, whose one job "
            "is to release adrenaline into the bloodstream. The heart, receiving "
            "it, pumps harder and louder. Muscles primed by faster neural "
            "signalling twitch in anticipation. The hundred million neurons "
            "connecting brain to gut fire faster, and the smooth muscle in the "
            "stomach vibrates. Pupils widen. What you feel is the dose arriving, "
            "custom-made, correctly timed, and free."
        ),
        operative=(
            "The misreading is learned, and learned early. Your first experiences "
            "of performance came before you had any skill, so arousal was "
            "reliably followed by disappointment and the two got wired together. "
            "It can be rewired. Michael Johnson, asked after the 1996 Games "
            "whether his heart was pounding in the blocks, said definitely, I was "
            "nervous — and when I'm nervous, I'm comfortable. Bill Belichick, "
            "forty-four years and six Super Bowls in, admitted he still gets "
            "nervous before every game. Expecting it is what makes it usable."
        ),
        img="img/insight-03.png",
        alt=(
            "A stick figure standing at a starting line with a fuel pump nozzle "
            "inserted into its side. A hose runs back to a pump whose dial "
            "needle is swung fully over. Short motion lines shake at the "
            "figure's hands and feet, and three butterfly shapes sit at its belly."
        ),
    ),
    dict(
        n=4,
        title="The plateau is where the improvement is made",
        lede=(
            "Practice does not pay out in a straight line. It pays out in long "
            "flat stretches interrupted by sudden bursts — and the longer you "
            "stay in a field, the longer the flats get and the smaller the "
            "bursts. This is the shape of every serious pursuit and almost "
            "nobody is told about it, which is why so many people conclude from "
            "a plateau that they do not have what it takes."
        ),
        evidence=(
            "Neuroanatomy offers an account of where the work goes. Each nerve "
            "fibre is sheathed in myelin, a fatty insulation that behaves like "
            "the covering on household wiring; the more a circuit fires, the "
            "more myelin is laid down, and the faster and more precisely the "
            "signal travels through it. Zinsser cites a figure of up to a "
            "hundredfold increase in impulse speed once the sheath is thick "
            "enough. The catch is that laying it down is slow. The change is "
            "real, continuous and invisible."
        ),
        operative=(
            "George Leonard put it in terms of learning systems: at the "
            "threshold there is an apparent spurt of learning, but this learning "
            "has been going on all along. The burst is not when you improve. It "
            "is when the accumulated improvement becomes visible. That reframes "
            "the flat stretch entirely — not something to be endured until "
            "progress resumes, but the place progress is manufactured. Everyone "
            "you are competing against is on the same schedule. Working with it "
            "slightly better than they do is the whole advantage."
        ),
        img="img/insight-04.png",
        alt=(
            "In the upper half, a line running flat for a long stretch, then "
            "stepping up, then flat again, then a smaller step. Directly beneath "
            "the long flat stretch, a single cable with coils of insulation "
            "being wrapped around it, thickest under the middle of the flat."
        ),
    ),
    dict(
        n=5,
        title="A rep you imagine runs down the same wire as a rep you take",
        lede=(
            "Vivid imagination is not a private slideshow with no consequences. "
            "It engages many of the same neural structures the real action "
            "engages, and the body responds accordingly — which means mental "
            "rehearsal is a way of getting reps that cost your joints nothing, "
            "and also that rehearsed failure carves its groove just as "
            "faithfully as rehearsed success."
        ),
        evidence=(
            "Zinsser's demonstration is a lemon. Picture one on a plate, feel "
            "its waxy skin, cut it, lift a half to your face, bite into it. Your "
            "nostrils flare, the muscles around your mouth tighten, and you "
            "produce saliva — for a fruit that does not exist. In 1929 Edmund "
            "Jacobson recorded electrical activity in the thigh and calf of a "
            "sprinter lying still on a table imagining a hundred-metre dash; the "
            "extensors and flexors fired in the same alternating sequence as in "
            "running. A more recent study by Kai Miller's group at the "
            "University of Washington found imagined finger movements producing "
            "roughly a quarter of the motor cortex activity of real ones."
        ),
        operative=(
            "Two things follow. Control is not optional — if an image of a "
            "mistake appears, you do what a director does and call cut, then "
            "reset the scene and run it to the ending you want. And perspective "
            "matters: rehearse from inside your own body, seeing what you would "
            "actually see, rather than watching yourself from the stands. "
            "Picture a rollercoaster from the car park and then from the front "
            "seat. Only one of those changes your heart rate."
        ),
        img="img/insight-05.png",
        alt=(
            "A stick figure in profile with a bare plate on the table in front "
            "of it. Above its head, a thought bubble containing a lemon half. A "
            "single line runs from the lemon in the bubble down through the head "
            "and neck to a small gland at the jaw, where one drop is falling."
        ),
    ),
    dict(
        n=6,
        title="A belief that helps you beats a belief that is accurate",
        lede=(
            "There is a moment in every performance where strict logic stops "
            "being useful. Logic says the best predictor of future behaviour is "
            "past behaviour, so the opponent who beat you will beat you again "
            "and the shot you have been missing will keep missing. Accuracy "
            "about what has already happened has no vote on what happens next, "
            "and treating it as though it does is often just negativity wearing "
            "a lab coat."
        ),
        evidence=(
            "Bob Rotella once assembled a panel of Virginia's best athletes to "
            "describe their most confident moment. One of them, Stuart Anderson, "
            "told a story about a high school playoff game in which he had made "
            "one shot from fourteen. Score tied, final timeout, and the coach "
            "drew up the last play for somebody else. Anderson interrupted him: "
            "give me the ball, I want the shot, I'm due to get one in. He got "
            "the ball. He made it. The graduate students, all of them studying "
            "probability, asked how missing could improve his odds. After "
            "missing four or five in a row, he said, I figured my odds were way "
            "better than fifty percent. And on a hot streak? Then I think I'm "
            "going to make everything I look at."
        ),
        operative=(
            "You have run this software before. At six years old you held a "
            "belief that you could ride a bicycle with no evidence for it and "
            "recent evidence against it, and that belief is the only reason you "
            "got back on. Zinsser calls it constructive delusion and treats it "
            "as a prerequisite rather than a flaw. Keep logic for the small "
            "hour-by-hour decisions and the single-skill drills. Throw it out "
            "for complex execution and for long horizons, where its only "
            "function is to talk you out of trying."
        ),
        img="img/insight-06.png",
        alt=(
            "A basketball hoop on a post. Beneath it a heap of balls resting on "
            "the ground. Beside the heap a tall upright gauge, with a marker "
            "pushed near the top of the gauge by the height of the heap. A stick "
            "figure stands with one ball raised, looking at the hoop."
        ),
    ),
)


# ---------------------------------------------------------------------------
# Actions (5 max)
# ---------------------------------------------------------------------------

ACTIONS = (
    dict(
        n=1,
        title="Put the day through the filter and keep three things",
        lede=(
            "At the end of each working day, take five minutes and a notebook. "
            "Write E and record one instance of honest effort — the drill where "
            "you dialled in, the stack of paper you finally sorted. Write S and "
            "record one thing you got right, however small. Write P and record "
            "one thing you got better at, even if you did not get it right. "
            "Three deposits, every day, whatever kind of day it was."
        ),
        operative=(
            "Do the same thing at a smaller scale between activities and the "
            "count multiplies. Walking from one drill to the next, from one "
            "patient to the next, out of one class and toward another, take the "
            "single best rep of what you have just finished and carry it with "
            "you — a highlight with a very small h. A basketball player who does "
            "this arrives at the end of practice with a dozen already banked and "
            "a better practice behind them. Tony Gwynn ran the professional "
            "version: after every game he cut his at-bats into three video "
            "files, one for solid contact, one for good decisions, and a third "
            "for the bad ones, which he deleted."
        ),
        caveat=(
            "Clients regularly say they could not find an E or an S or a P. The "
            "answer is that they are not looking carefully enough — go back "
            "through the day hour by hour and it is there. The deeper resistance "
            "is a belief that remembering your good moments is somehow improper "
            "or unrealistic. Consider what you are remembering instead."
        ),
        img="img/action-01.png",
        alt=(
            "A large funnel. A jumble of small shapes pours into the top. Below "
            "the spout, an open notebook with three ruled lines, each beginning "
            "with a large capital letter, E, S and P. Three shapes are dropping "
            "through into it."
        ),
    ),
    dict(
        n=2,
        title="Write the statement to five specifications, then hang it on a doorway",
        lede=(
            "Compose three statements about the reality you want, phrased as "
            "though it is already here. Each one must be first person, present "
            "tense, positively worded, precise, and powerful. Then write three "
            "more: one for a quality you do not yet have, one for an action you "
            "do not yet take, one for an outcome you have not yet achieved. "
            "Then attach them to something you pass constantly."
        ),
        operative=(
            "Alessandra Ross, a middle-distance runner whose personal best was "
            "two minutes and two seconds, repeated I run a one fifty-six eight "
            "hundred every time she walked through a doorway for nine months. At "
            "roughly fifty doorways a day that is thirteen thousand repetitions. "
            "Within a month she noticed the self-image starting to hold. She "
            "never ran the one fifty-six; she did set two consecutive personal "
            "bests at the Olympic trials, the only competitor in her event to do "
            "so. Dan Jansen used the other trigger — writing I love the "
            "thousand a dozen times a night for two years before finally winning "
            "his event in world record time."
        ),
        caveat=(
            "Positive wording is not a stylistic preference. I never miss my "
            "second serve and my second serve lands just inside the line sound "
            "similar and are not: the part of the brain that runs the serve "
            "recognises the active verb missing and pulls up the memories that "
            "go with it, reinforcing exactly what you were trying to avoid. "
            "State what you want more of."
        ),
        img="img/action-02.png",
        alt=(
            "Two panels. In the first, a small card on which one line is written "
            "by a stick-figure hand, with five short tick marks down the side "
            "labelled I, NOW, YES, EXACT and STRONG. In the second, a corridor "
            "of doorways receding in perspective, a stick figure walking through "
            "one, and a coin dropping into a slot in each door frame."
        ),
    ),
    dict(
        n=3,
        title="Rehearse the breakthrough in the room where it will happen",
        lede=(
            "Pick the outcome that gives you goosebumps. Find the actual room — "
            "visit it, or find photographs of it. List the handful of moments "
            "that will decide it. Then sit somewhere comfortable, settle, and "
            "run those moments in order, from inside your own body, in full "
            "sensory detail, with the emotion turned up. Finish by letting "
            "yourself enjoy the win."
        ),
        operative=(
            "The target is a sense of having been there before. Sylvie Bernier "
            "knew the time of her 1984 Olympic final, where the scoreboard would "
            "be, where the coaches would sit; when she reached the podium it was "
            "like I had been there before. Around twenty minutes is as long as "
            "most people can hold the control, detail and feeling required, so a "
            "short performance can be run whole and a long one has to be run as "
            "key moments. Then rehearse the disruptions separately. Name three "
            "things that could throw you, spend ten seconds on the problem and "
            "at least thirty on getting back in control — the ratio is the "
            "point. Do enough of them and even an unrehearsed surprise finds the "
            "subroutine already built."
        ),
        caveat=(
            "This works because your nervous system takes it seriously, which "
            "means a rehearsed failure is also taken seriously. Keep the content "
            "controlled. If an image of a mistake appears, stop the scene, reset "
            "it, and run it through to the ending you want."
        ),
        img="img/action-03.png",
        alt=(
            "Two panels. In the first, a stick figure sits in a chair with its "
            "eyes closed; a line runs from its head to a podium on which stands "
            "a solid outlined cut-out silhouette the same shape as the figure. "
            "In the second, the same podium without the line, and the stick "
            "figure stepping into that cut-out and filling it exactly."
        ),
    ),
    dict(
        n=4,
        title="Explain the setback as temporary, limited, and not you",
        lede=(
            "The moment something goes wrong, say three things to yourself, in "
            "this order. It happened that one time. It happened in that one "
            "place. That is not how I really am. Each sentence blocks one of the "
            "three routes by which a single bad moment turns into a general "
            "belief about yourself."
        ),
        operative=(
            "The three traps are distinct and they escalate. Temporary blocks "
            "here I go again. Limited blocks now the whole day is going down the "
            "drain — the golfer who puts one drive in the trees keeps it from "
            "spreading to his irons and his putting. Non-representative blocks "
            "the last and worst one, maybe I'm not good enough. Martin Seligman "
            "gave his Attributional Styles Questionnaire to the entire incoming "
            "West Point class of 1988; the cadets who quit during basic training "
            "or the following year had significantly more pessimistic "
            "explanatory styles than those who stayed. Maddie Burns, a college "
            "lacrosse goalkeeper, concedes seven goals in an average game and "
            "treats each one as just that one time, seven times a game."
        ),
        caveat=(
            "This is not denial and it does not dissolve responsibility. You "
            "still acknowledge what happened, you still take the consequences, "
            "and you still go and fix the thing. What you refuse is the "
            "generalisation — the move from a fact about one moment to a verdict "
            "on your whole capability."
        ),
        img="img/action-04.png",
        alt=(
            "A stick figure standing on a floor with a single dark blot near its "
            "feet. Three straight barrier walls are set around the blot: one "
            "between it and a row of day-boxes stretching away to the right, one "
            "between it and the rest of the floor, and one between it and the "
            "stick figure."
        ),
    ),
    dict(
        n=5,
        title="Cue, breathe, attach — before every single engagement",
        lede=(
            "Before each rep, pitch, shift, patient, call or meeting, run three "
            "steps in about ten seconds. Cue your conviction with a short "
            "powerful phrase. Breathe your body — belly out on the inhale, abs "
            "in on the exhale, two or three times, finishing on a strong "
            "settling breath out. Attach your attention to the single thing that "
            "matters right now, and let yourself become genuinely curious about "
            "it."
        ),
        operative=(
            "The cue is a statement, not a question, and it names a process "
            "rather than an outcome. Be a wall. Time to cruise. Do it like you "
            "know it. Here's my chance. Michael Phelps's coach Bob Bowman "
            "described watching an Olympic coach tell an already-nervous skater "
            "this is what you've worked so hard for; she was so tight the two of "
            "them missed a high five, and she skated badly. The rival's coach "
            "made small talk and one technical point. Process talk lowers "
            "arousal; outcome talk raises it. An offensive lineman runs this "
            "sixty times in a game. A neurosurgeon runs it between the steps of "
            "an operation. Danny Brière ran it in ninety seconds on the bench "
            "between shifts."
        ),
        caveat=(
            "Breathing is the one autonomic function with a manual override, so "
            "do it properly. A correct inhale is down and out — the diaphragm "
            "drops, the belly expands on all sides, the lower ribs lift. It is "
            "not the upward shoulder lift most people were taught. The exhale is "
            "up and in, abdominals and obliques drawing toward the spine."
        ),
        img="img/action-05.png",
        alt=(
            "Three panels in a row. In the first, a stick figure with a speech "
            "line from its mouth carrying a short phrase in capitals. In the "
            "second, the same figure in profile with its belly pushed out and an "
            "arrow curving down and out at the belly. In the third, the same "
            "figure with two straight lines running from its eyes and converging "
            "on a single ball."
        ),
    ),
)


# ---------------------------------------------------------------------------
# Quick reference
# ---------------------------------------------------------------------------

QUICK_REFERENCE = (
    ("The definition",
     "Certainty about your ability sufficient to bypass conscious thought and "
     "execute unconsciously. Confidence is the absence of interference, not an "
     "addition."),
    ("The account",
     "A running total of thoughts, not a record of events. Deposits: effort, "
     "success, progress, and the future you want. Withdrawals: replayed "
     "setbacks and rehearsed trouble."),
    ("Four foundations",
     "Thoughts drive physical state. You will never be perfect. Your nerves "
     "will fire before anything that matters. Practice pays late and unevenly."),
    ("Three sources",
     "Past — Top 10, daily ESP, immediate progress review. Present — "
     "affirmations on a trigger. Future — envisioning, and the flat tire drill."),
    ("Five specs for an affirmation",
     "First person. Present tense. Positive. Precise. Powerful. State what you "
     "want more of, never what you are trying to avoid."),
    ("Four specs for envisioning",
     "Control the content. Maximum sensory detail. Internal perspective. Real "
     "emotion. Twenty minutes is the ceiling."),
    ("Three safeguards",
     "Temporary, limited, non-representative. Acknowledge, silence, replace. "
     "Then the shooter's mentality: a miss means the next one is due."),
    ("In the arena",
     "Take stock of the account, the task, the hidden opponent and the room. "
     "Decide you are enough, then statements only. Every engagement: cue the "
     "conviction, breathe down and out, attach the attention."),
    ("Afterwards",
     "What happened, so what does it tell you, now what will you do. Eighty "
     "percent of the review on the gems after a loss, sixty after a win."),
)

CLOSING_LINE = (
    "Victorious warriors win first and then go to war. Defeated warriors go to "
    "war first and then seek to win."
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
    "insight-1": "Watch your own knees on the stairs and you fall. Certainty is what is left when the commentary stops.",
    "insight-2": "Ten sacks in ten games and he thought he was terrible. Nothing enters the account except a thought.",
    "insight-3": "The pounding heart is adrenaline arriving on time. Champions expect the feeling and read it as fuel.",
    "insight-4": "The flat stretch is not stalled progress. It is where the wiring thickens, invisibly, until the jump shows up.",
    "insight-5": "Bite an imaginary lemon and you really salivate. Rehearsed reps run down the wire the real ones use.",
    "insight-6": "He had made one shot from fourteen and asked for the last one. Useful beat accurate, and it went in.",
    "action-1": "Every day, bank one instance of effort, one success, one bit of progress. Five minutes, three deposits.",
    "action-2": "Write it first person, present tense, positive, precise, powerful. Then say it at every doorway you pass.",
    "action-3": "Rehearse the real room from inside your own body, then rehearse recovering from what could go wrong.",
    "action-4": "It happened once, it happened there, and it is not who you are. Three sentences, three escape routes blocked.",
    "action-5": "Cue the conviction, breathe belly-out then abs-in, attach your attention. Ten seconds, before every single engagement.",
}

for _e in BOOK["insights"] + BOOK["actions"]:
    _e["takeaway"] = TAKEAWAY[_e["id"]]


# ---------------------------------------------------------------------------
# LETTERING — the exact hand-lettered title each image prompt asks for.
# verify_lettering.py scores each plate against every one of these.
# ---------------------------------------------------------------------------

LETTERING = {
    "insight-1": "MIND ON THE KNEES",
    "insight-2": "THE WINS NEVER GOT IN",
    "insight-3": "THE JITTERS ARE THE FILL",
    "insight-4": "THE FLAT IS THE FACTORY",
    "insight-5": "NO LEMON, SAME MOUTH",
    "insight-6": "THE MISSES RAISE THE GAUGE",
    "action-1": "THREE OUT OF EVERY DAY",
    "action-2": "EVERY DOOR IS A DEPOSIT",
    "action-3": "CUT THE SHAPE, THEN STEP IN",
    "action-4": "THREE WALLS ROUND ONE SPILL",
    "action-5": "CUE, BREATHE, ATTACH",
}


# ---------------------------------------------------------------------------
# COMPANION — the Spoken Companion text. build_docx.py renders this;
# the text is never written straight to a .docx.
# ---------------------------------------------------------------------------

COMPANION_FOOTER = "The Confident Mind — Spoken Companion"

COMPANION = [
    {"level": 1, "heading": "What Confidence Actually Is", "paras": []},

    {"level": 2, "heading": "The Victory Won Before You Arrive", "paras": [
        "On the morning of the third of October, 2009, Captain Stoney Portis was "
        "thirty kilometres away when his own outpost came under attack. Combat "
        "Outpost Keating sat at the bottom of a valley in eastern Afghanistan, "
        "ringed by high mountains and exposed from every direction; the soldiers "
        "called it Camp Custer. Fifty-three of them were there that morning "
        "against roughly three hundred Taliban fighters, and Portis was in a "
        "Black Hawk trying to get back to them.",

        "There I was in the helicopter thinking this is how I'm going to die, he "
        "said later. But I stopped that thought, slowed down my breathing and "
        "repeated one of the affirmations I had been using since the day I took "
        "command. I am the leader. I make the decisions when it counts. Then I "
        "pictured exactly where we would land and exactly what each of us would "
        "do once we hit the ground. Before I knew it, I was completely relaxed "
        "and in my zone.",

        "The landing zone was taken and the helicopter turned back. Portis "
        "assembled a quick reaction force, flew to a mountaintop and descended "
        "two thousand vertical feet on foot over five hours through one ambush "
        "after another, doing that same piece of mental work the whole way down.",

        "Notice what he did, because most people do the opposite. Most people let "
        "themselves feel confident when good things are happening, which puts "
        "their inner state on a roller coaster driven by outside events. Portis "
        "decided to be certain in circumstances that gave him no reason to be. "
        "Sun Tzu: victorious warriors win first and then go to war, while "
        "defeated warriors go to war first and then seek to win.",

        "It needs a definition you can use, and the usual ones — believing in "
        "yourself, knowing you can do something — are no help, because they miss "
        "the central fact about performance. Human beings are built to execute "
        "well-learned skills unconsciously, and the more complex the skill, the "
        "more that matters. So: confidence is a sense of certainty about your "
        "ability that allows you to bypass conscious thought and execute "
        "unconsciously. Not a feeling laid over the skill. The absence of "
        "everything that would get in the skill's way.",

        "The psychologist Sian Beilock makes it physical. If you were moving "
        "quickly down a flight of stairs and someone asked you to think about "
        "exactly what both your knees were doing, there is a good chance you "
        "would end up in a pile at the bottom.",

        "This does not make skill optional. A student who studied half the "
        "material and feels certain will ace half the exam. But a student who "
        "learned all of it and doubts she has will not recall it cleanly either, "
        "because the chatter blocks the retrieval. Whatever competence you have "
        "reached, what you get out of it depends on feeling certain about it.",
    ]},

    {"level": 2, "heading": "The Running Total", "paras": [
        "Confidence has little to do with what happens to you and almost "
        "everything to do with how you think about what happens to you. Which "
        "makes it a running total — the sum of every thought you have "
        "entertained about yourself and your field, changing as each new one is "
        "added.",

        "The useful image is a bank account. Deposit memories of success, of "
        "progress, of honest effort, and thoughts about improvements still to "
        "come, and the balance grows. Withdraw by replaying old setbacks or "
        "rehearsing future ones, and it shrinks. Building confidence, protecting "
        "it and spending it are all one activity: managing that account.",

        "This explains two things that otherwise look like contradictions. In "
        "1998 Michael Strahan had ten sacks in ten games, coming off an All-Pro "
        "season, and told a reporter he thought he sucked, that it was like we "
        "had no hope. Asked what the field looked like in his mind, he described "
        "chasing the quarterback, almost getting there, not getting there, and "
        "then everything goes black. Years of highlights sitting outside the "
        "account, because the picture he replayed was of the near miss. Run it "
        "the other way and you get Ilya Kulik, whose warm-up before the 1998 "
        "Olympic short program was a mess of slips and missed jumps. He skated "
        "nearly perfectly twenty minutes later and won gold. Where did the "
        "confidence come from, the interviewer asked. He shrugged. Just from my "
        "mind.",

        "Nothing that happens to you enters the account. A thought about it does, "
        "and the thought is yours to choose. Viktor Frankl called that choice the "
        "last of the human freedoms — to choose one's attitude in any given set "
        "of circumstances. Everything that follows is an exercise of it.",
    ]},

    {"level": 1, "heading": "Four Things You Do Not Get to Argue With", "paras": []},

    {"level": 2, "heading": "The Body Is Listening, and You Will Never Be Perfect", "paras": [
        "Your thoughts shape your mood, your mood shapes your physical state, "
        "your physical state shapes your execution, and your execution becomes "
        "the subject of more thoughts. That loop runs continuously and has no "
        "neutral setting. The cheapest way to steer it is the framing you take in "
        "with you: not this meeting is critically important so I have to do well, "
        "but let's see how well I can do this right now.",

        "The second reality is that you will never be perfect, and it is your "
        "reaction to the imperfection rather than the imperfection itself that "
        "drains the account — which is why the highest achievers in a field tend "
        "to carry only moderate perfectionism. Greg Louganis stated the paradox "
        "exactly: in order to do it perfectly, I have to let go of perfectionism "
        "a little. There is a sweet spot on the diving board and he could not "
        "always hit it. That is why I train so hard, he said — not just to do it, "
        "but to do it right from all the wrong places.",
    ]},

    {"level": 2, "heading": "Fall in Love With Your Butterflies", "paras": [
        "A performer sits down and describes the problem. I'm good in practice, "
        "but at a game I get psyched out. Heart speeding up, palms sweating, "
        "hands jittery, stomach flipping over. Those sensations mean nervous, and "
        "nervous means something is wrong.",

        "This is the greatest psych-out in human performance, and it rests on a "
        "misreading of one word. Nervous has two dictionary senses — easily "
        "agitated, and relating to the nerves. The second is the accurate one. "
        "Your nervous system is simply more active, and Zinsser's account of why "
        "runs like this. Whenever you are about to do something that matters, the "
        "unconscious part of the brain that registers it signals the adrenal "
        "glands, two small wads of tissue on top of your kidneys whose one job is "
        "to release adrenaline into the bloodstream. The heart, receiving it, "
        "pumps harder — loud enough for you to notice. Muscles primed by faster "
        "neural signalling twitch in anticipation, which is the jitter in your "
        "hands. The hundred million neurons connecting brain to gut fire faster, "
        "and the smooth muscle of the stomach vibrates like wings. Your pupils "
        "widen.",

        "So your body has manufactured a performance-enhancing compound to your "
        "own specification, delivered it at the right dose at the right moment, "
        "charged you nothing and broken no rules. What you feel is the delivery "
        "arriving.",

        "Why do so many read it as a warning? Because the association formed "
        "early. Your first performances came before you had any skill, so arousal "
        "was reliably followed by disappointment and the two got wired together. "
        "It can be rewired, sometimes in one moment. Michael Johnson, asked after "
        "the 1996 Games whether his heart was pounding in the blocks, said "
        "definitely, I was nervous — and when I'm nervous, I'm comfortable. Sit "
        "with that sentence. He has converted a signal of unease into a source of "
        "power. It will not feel normal, and it should not — you are about to do "
        "something that matters more to you than filling the car with petrol. "
        "Expect that, and it becomes usable.",
    ]},

    {"level": 2, "heading": "The Plateau Is Where the Work Goes", "paras": [
        "You have heard that ten thousand hours of deliberate practice makes an "
        "expert. What that story leaves out is the shape of the payoff. Returns "
        "are uneven — long flat stretches where nothing seems to improve, "
        "interrupted by sudden bursts. And it gets worse with experience: the "
        "further along you are, the longer the flats and the smaller the bursts. "
        "Nobody warns us, so people conclude from a plateau that they do not have "
        "what it takes, and quit.",

        "The corrective is understanding where the work goes. Every nerve fibre "
        "is sheathed in myelin, a fatty insulation that behaves like the covering "
        "on household wiring. The more a circuit fires, the more myelin is laid "
        "down, and the faster and more precisely the signal travels — Zinsser "
        "cites an increase of up to a hundredfold in impulse speed once the "
        "sheath is thick enough. Building it is slow. The change is real, "
        "continuous and completely invisible.",

        "George Leonard described the same thing in terms of learning systems. At "
        "the threshold, he wrote, there is an apparent spurt of learning — but "
        "this learning has been going on all along. The burst is not when you "
        "improve. It is when the accumulated improvement becomes visible. Which "
        "makes the plateau not something to endure until progress resumes, but "
        "the factory where progress is manufactured. Everyone you compete with is "
        "on the same schedule. Working with it slightly better than they do is "
        "the entire advantage.",
    ]},

    {"level": 1, "heading": "Filling the Account", "paras": []},

    {"level": 2, "heading": "Mining What Has Already Happened", "paras": [
        "You already have a mental filter and it is running right now, deciding "
        "what gets in and what gets screened out. The only question is which way "
        "it is pointed.",

        "Start with the past. Take a blank page, write My Top 10 at the top, and "
        "list ten accomplishments in whatever field matters to you. It does not "
        "need to be awe-inspiring; every parent who taught a toddler to share has "
        "plenty to draw on. The usual objection is that the past is irrelevant "
        "now — I was a big fish in a small pond and now I'm a small fish in a big "
        "one. Consider what actually happens to a healthy fish moved into a "
        "bigger pond with more room and more food. It grows. You are the same "
        "fish. You stopped remembering how big.",

        "Then bank the present, daily. Five minutes, a notebook, the date at the "
        "top. Write E and record one instance of honest effort. Write S and "
        "record one thing you got right, however small. Write P and record one "
        "thing you got better at, even if you did not get it right. Effort, "
        "success, progress — three deposits minimum, and easily ten if you look "
        "properly. People tell me they could not find one. They are not looking "
        "carefully enough; go back hour by hour and it is there.",

        "Then shorten the interval. Between one drill and the next, one patient "
        "and the next, take the single best rep of what you just finished and "
        "carry it with you — a highlight with a very small h. Skip it and you "
        "tend to carry the worst rep forward instead, which is the same "
        "mechanism pointed the wrong way.",

        "The professional version belongs to Tony Gwynn, who after every game cut "
        "his at-bats into three video files. One for solid contact. One for good "
        "decisions at the plate. One for the bad ones, which he deleted. The last "
        "thing I need to do, he said, is watch myself looking like a fool "
        "swinging at somebody's curveball.",
    ]},

    {"level": 2, "heading": "Saying Yes, in the Present Tense", "paras": [
        "Memory is half the account. The other half is the thousands of "
        "statements you make to yourself about yourself right now, because those "
        "statements set a prophecy you then act to fulfil. Watch it run in a room "
        "of West Point cadets on the first day of the military movement course. A "
        "minority think this looks like a playground, put in real effort, and "
        "finish well. The majority think I'm not built for this, put in just "
        "enough to get through, and pass with a C — confirming, to their own "
        "satisfaction, that they were right about themselves all along.",

        "An affirmation is a deliberate prophecy, stated as though it were "
        "already true. To affirm is to say yes. Five specifications: first "
        "person, because it is your account being built; present tense, because "
        "the balance is what is in it now and future-tense language quietly "
        "postpones the change forever; positive, precise and powerful.",

        "That third one is not a stylistic preference. I never miss my second "
        "serve and my second serve lands just inside the line sound similar and "
        "are not. The part of the brain that runs the serve recognises the active "
        "verb missing and retrieves the memories that go with it, strengthening "
        "those pathways every time you repeat the phrase. State what you want "
        "more of.",

        "Then hang the statement on a trigger you meet constantly. Alessandra "
        "Ross, whose personal best over eight hundred metres was two minutes and "
        "two seconds, repeated I run a one fifty-six eight hundred every time she "
        "walked through a doorway for nine months. At around fifty doorways a day "
        "that is thirteen thousand repetitions. Her first reaction had been who "
        "am I to think that. Within a month it was holding — she felt herself "
        "becoming a one fifty-six runner before she had run anything like one. At "
        "the Olympic trials she set two consecutive personal bests, the only "
        "competitor in her event to do so. She never did run the one fifty-six. "
        "She won the first victory.",
    ]},

    {"level": 2, "heading": "Fooling Your Nervous System on Purpose", "paras": [
        "Try this. Picture your kitchen table, and on it a plate holding a bright "
        "yellow lemon. Pick it up and feel the weight. Take the small knife "
        "beside the plate and cut it in half. Lift one half; it is lighter and "
        "softer. Bring it to your face and take in the scent. Now put it to your "
        "lips and bite. Your nostrils flared, the muscles round your mouth "
        "tightened, and you produced saliva — for a fruit that does not exist.",

        "That is not a parlour trick, it is the mechanism. In 1929 Edmund "
        "Jacobson recorded electrical activity in the thigh and calf of a "
        "sprinter lying motionless on a table imagining a hundred-metre dash, and "
        "the extensors and flexors fired in the same alternating sequence as in "
        "real running. At a meaningful level, the nervous system "
        "does not distinguish a real rep from a vividly imagined one.",

        "Which cuts both ways, and that is the part to hold onto — a rehearsed "
        "failure is taken every bit as seriously as a rehearsed success. So four "
        "specifications. Control the content: if a picture of a mistake flashes "
        "up, do what a director does, call cut, reset the scene and run it to the "
        "ending you want. Maximum sensory detail, not sight alone but sound, "
        "temperature, the feel of the equipment. Genuine emotion, which is what "
        "separates this from daydreaming. And the internal perspective — seeing "
        "out of your own eyes rather than watching yourself from outside. Picture "
        "a rollercoaster from the car park, then from the front seat. Only one of "
        "those changed your heart rate.",

        "Then aim it at something specific. Pick the outcome that gives you "
        "goosebumps, find the actual room or photographs of it, list the moments "
        "that will decide it, and run them in order. Sylvie Bernier knew she "
        "would dive at four in the afternoon on the sixth of August, knew where "
        "the scoreboard would be and where the coaches would sit. When I got on "
        "the medal podium, she said, it was like I had been there before.",

        "Finally, rehearse the trouble. Name three specific things that could "
        "throw you and spend ten seconds on the problem, then at least thirty "
        "getting yourself back in control. The ratio is the point, and it builds "
        "a subroutine that fires even for the surprise you never rehearsed.",
    ]},

    {"level": 1, "heading": "Defending It", "paras": []},

    {"level": 2, "heading": "Temporary, Limited, and Not You", "paras": [
        "Building the account is half the filter's job. The other half is "
        "restructuring the material that would draw it down, and it is the half "
        "most people never run.",

        "Martin Seligman spent a career on the difference. Optimists and "
        "pessimists, he found, differ not in intelligence or talent or motivation "
        "but in explanatory style — how they account to themselves for what "
        "happens. Pessimists read bad events as permanent, pervasive and "
        "personal. In the summer of 1988 he gave his questionnaire to the whole "
        "incoming West Point class, and the cadets who quit during basic training "
        "or the following year scored significantly more pessimistic than those "
        "who stayed.",

        "The corrective is three sentences, each blocking a different escape "
        "route. It happened that one time, which stops here I go again. It "
        "happened in that one place, which stops now my whole day is going down "
        "the drain — and keeps the golfer who put a drive in the trees from "
        "concluding his irons and his putting are gone too. That is not how I "
        "really am, which stops the last and worst one, maybe I'm not good "
        "enough. Maddie Burns kept goal for West Point's lacrosse team with the "
        "fifth-best goals-against average in the country, which still means seven "
        "times a game she digs the ball out of the net while the other team "
        "celebrates. She treats each one as just that one time. Seven times a "
        "game.",

        "None of this is denial. You still acknowledge what happened, still take "
        "the consequences, still go and fix the thing. What you refuse is the "
        "generalisation.",

        "A three-step works on the voice in your head, where the framing is an "
        "argument: two positions competing, and whoever gets the last word wins. "
        "Acknowledge it — you cannot win a fight you have not noticed — then "
        "silence it with a firm stop, then replace it with a line out of your own "
        "notebook. Do not expect it to leave. Arthur Ashe walked onto Centre "
        "Court for a Wimbledon semi-final wondering what if I don't get any first "
        "serves in, and won. Confidence is not the absence of doubt but the way "
        "you respond to doubt.",
    ]},

    {"level": 2, "heading": "The Shooter's Mentality", "paras": [
        "Bob Rotella once put a panel of the University of Virginia's best "
        "athletes in front of his graduate students and asked each to describe "
        "the most confident moment of their career. One after another they told "
        "stories of dominance — touchdowns, records, rivals beaten. Then it was "
        "Stuart Anderson's turn, and he told them about a high school basketball "
        "playoff game in which he had made one shot from fourteen.",

        "His team had played well enough to be tied with under a minute left. The "
        "coach called timeout and began drawing up the final play for somebody "
        "else, which was the obvious call. Anderson interrupted him. No, coach, "
        "give me the ball, I want the shot. The coach refused. Then Anderson said "
        "the thing that changed his mind, and said it with complete seriousness: "
        "I'm due to get one in.",

        "He got the ball. He made it. Two from fifteen, and carried off the court "
        "on his teammates' shoulders.",

        "The graduate students, all of them studying probability, asked how "
        "missing could improve his odds. Anderson explained that he was a fifty "
        "percent shooter over his career, so after missing a couple the next ones "
        "were better than even. After four or five in a row, way better. And by "
        "the end of the game, I figured it just had to go in. So does making "
        "several in a row mean you're due to miss, someone asked. No, he said. If "
        "I'm on a hot streak I think I'm going to make everything I look at. So I "
        "keep shooting. How can you have it both ways, a student finally asked. I "
        "don't know, Anderson said. That's just how I think.",

        "It is not logical and it does not need to be. You have run this software "
        "before: at six years old you held a belief that you could ride a bicycle "
        "with no evidence for it and immediate evidence against it, and that "
        "belief is the only reason you got back on. Zinsser calls it constructive "
        "delusion and treats it as a prerequisite rather than a flaw. Keep logic "
        "for the small hour-by-hour decisions and the single-skill drills. Throw "
        "it out for complex execution and for long horizons, where its main "
        "function is to talk you out of trying.",
    ]},

    {"level": 1, "heading": "Spending It", "paras": []},

    {"level": 2, "heading": "Deciding That You Are Enough", "paras": [
        "Everything so far has been accumulation. At some point you open the "
        "vault and spend, and that transition does not happen by itself.",

        "Take stock of yourself first. This is where the journal earns its keep. "
        "Billy Mills, an unknown before the 1964 Tokyo Games, went back through a "
        "full year of workout books two days before the ten thousand metres and "
        "found, in his own handwriting from six weeks earlier, I'm in great "
        "shape, I'm starting to have a strong finish, I'm ready for a "
        "twenty-eight twenty-five in Tokyo. His conclusion: I was totally "
        "confident that I could win.",

        "Take stock of the situation next, remembering that inside the obvious "
        "task — win the game, make the sale — sits the real one, which is paying "
        "attention to what is in front of you minute by minute rather than to how "
        "much the outcome matters. Then go and stand in the room. Get the "
        "practice round, the empty conference hall, the photographs. Make the "
        "place yours before it is full.",

        "Then decide that you have enough. This is the gate, and it is a decision "
        "rather than a conclusion. Saver to spender. Workhorse to racehorse. At "
        "the moment you decide you are enough, you stop caring about getting "
        "better and start caring only about being your best.",

        "Helen Maroulis made it a mantra. Walking onto the mat for an Olympic "
        "final against a wrestler who had not lost internationally in sixteen "
        "years and had beaten her twice, she told herself I am enough. That was "
        "the most liberating thing I ever said to myself, she explained "
        "afterwards. I thought there was some extreme level I would have to reach "
        "before I could be an Olympic champion. But you don't have to be "
        "extraordinary. You can be an Olympic champion by just being enough. She "
        "won.",

        "One rule protects the decision once it is made: statements only. Once "
        "the line is crossed — your feet hit the floor on game day, you pass "
        "through the operating room door — you ask no questions, of yourself or "
        "anyone else. Ready to go today? sounds harmless, and it is the ember "
        "that starts am I really ready, have I honestly done enough. And if you "
        "know you have not prepared as well as you should have, go in with the "
        "same conviction anyway. You never know how much is in the tank until "
        "you go out and empty it.",
    ]},

    {"level": 2, "heading": "Cue, Breathe, Attach", "paras": [
        "Entering the arena is one victory. A performance is a series of them, "
        "and you have to reopen the account before each engagement — each pitch, "
        "each point, each shift, each patient, each meeting. Fritz Perls used to "
        "tell his patients to lose your mind and come to your senses, which turns "
        "out to describe high performance rather well.",

        "Three steps, ten seconds. Cue your conviction: a short, powerful, "
        "present-tense statement naming a process rather than an outcome. Be a "
        "wall. Time to cruise. Do it like you know it. I've done the work. Bob "
        "Bowman, who coached Michael Phelps, described watching a coach tell an "
        "already-nervous Olympic skater this is what you've worked so hard for. "
        "The two of them were so tight they missed a high five, and she skated "
        "badly. Her rival's coach made small talk. Outcome talk raises arousal; "
        "process talk lowers it.",

        "Breathe your body. Breathing is the one autonomic function with a manual "
        "override, which as the karate teacher Tsutomu Ohshima put it makes it "
        "the glue connecting the conscious and the unconscious. Do it correctly, "
        "which is probably not how you were taught. A correct inhale is down and "
        "out — the diaphragm drops, the belly expands on every side, the lower "
        "ribs lift. Not an upward heave of the shoulders. The exhale is up and "
        "in, abdominals and obliques drawing toward the spine. Two or three "
        "cycles, finishing on a strong settling breath out.",

        "Attach your attention. This is nothing more complicated than letting "
        "yourself become fascinated by what is in front of you — the ball as your "
        "opponent tosses it, the first note you come in on, the row of figures "
        "that holds the decision. Tiger Woods described becoming so engrossed in "
        "a shot that the noise and the self-conscious thoughts disappeared: it's "
        "almost as if I get out of the way. And while you are out "
        "there, look for your slightest break — an attention pointed outward, "
        "quietly assuming there is one to find.",

        "Then run it again, and again — sixty times in a football game, between "
        "every step of an operation. And keep the importance at the right level, "
        "because the last enemy is the belief that a big moment deserves more "
        "thought. Pressure makes diamonds, but once the diamond is made you do "
        "not squeeze it further; you set it where it can be seen.",
    ]},

    {"level": 2, "heading": "Faith Takes Practice", "paras": [
        "The performance is not over when it ends. There is one more step, and it "
        "is the one almost everyone skips: an honest review, in three questions. "
        "What happened — the result, where you slipped, and what your highlight "
        "reel would contain. So what does that tell you. Now what will you do "
        "about it, each learning rewritten as a present-tense statement. Balance "
        "kindness against criticism deliberately and do not split it evenly: "
        "after a loss, eighty percent of the time goes to the gems and twenty to "
        "the junk, because a loss is exactly when you are least likely to give "
        "yourself any. After a win, tighten your chin straps and move criticism "
        "up to forty.",

        "One closing image. In December 2004, then-Colonel Robert Brown was twenty feet from a suicide bomb that killed twenty-two people "
        "in a mess hall in Mosul, six of them his own soldiers. The worst day of "
        "my life, he called it. His unit went out on missions that same night and "
        "kept going for months, and by the elections that followed, incidents in "
        "the city had fallen from three hundred a week to two. Asked how, he "
        "said: faith takes practice. You take that first step envisioning the "
        "success of one mission at a time.",

        "That is the whole thing, and it is worth resisting the more comfortable "
        "story — that certainty arrives one day as a gift, from a mentor or a "
        "moment or a run of luck. It does not. It is a habit you build in small "
        "deposits, defend from theft, spend deliberately, and rebuild the next "
        "morning. Victorious warriors win first and then go to war. Defeated "
        "warriors go to war first and then seek to win. Which one you are is "
        "decided long before you arrive.",
    ]},
]
