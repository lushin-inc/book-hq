# The Data Detective — Tim Harford
# Durable artifact. The page, the guide and the companion all read from this file.
# Nothing downstream hardcodes content.

SLUG = "the-data-detective"

CENTRAL_QUESTION = (
    "Statistics can be made to show that storks deliver babies. They also showed that "
    "smoking causes lung cancer. How do you take numbers seriously without being fooled "
    "by them?"
)

CENTRAL_ANSWER = (
    "The failure is almost never in the arithmetic. It is in what you wanted the number "
    "to say, and in the questions nobody asked before it was published. A claim that "
    "flatters you gets waved through; a claim that annoys you gets audited. Reverse that "
    "and most of the work is done."
    "\n\n"
    "The ten rules are habits of attention rather than techniques. Notice the feeling. "
    "Ask what was counted and what the figure should sit beside. Find out who produced "
    "it, who was in the sample, and what never got published. Watch the chart as closely "
    "as the sentence. Underneath all of them is one instruction: be curious — want to "
    "know more about a number than whether it supports you."
)

FRAMEWORK = {
    "name": "The Detective's Order of Work",
    "intro": (
        "The rules run in a direction: inward first, then at the claim, then at the "
        "machinery behind it, then forward to the version of you who will have to admit "
        "being wrong. Taken out of order they stop working, because the first one is "
        "what makes the rest usable."
    ),
    "steps": [
        {
            "mark": "01",
            "term": "Notice the feeling",
            "gloss": (
                "Before evaluating anything, register your own reaction. Outrage, "
                "delight and denial all arrive before judgment does, and each of them "
                "decides in advance what the evidence will be allowed to mean."
            ),
        },
        {
            "mark": "02",
            "term": "Weigh it against your own experience",
            "gloss": (
                "A statistic and a lived experience are usually answering different "
                "questions. Work out which question each one answers instead of asking "
                "which of them is lying."
            ),
        },
        {
            "mark": "03",
            "term": "Ask what was counted",
            "gloss": (
                "Every figure rests on a definition somebody chose. Find the definition "
                "before arguing about the number, because that is where the real "
                "disagreement usually is."
            ),
        },
        {
            "mark": "04",
            "term": "Ask what it should sit beside",
            "gloss": (
                "One number alone is not information. Supply the comparison the "
                "presenter left out — over time, or against a total large enough to "
                "give the figure a size."
            ),
        },
        {
            "mark": "05",
            "term": "Find out where it came from",
            "gloss": (
                "Who produced it, who was in the sample, who was missed, what never got "
                "published, and what the algorithm was actually keying on. The number is "
                "the last step of a process, not the first."
            ),
        },
        {
            "mark": "06",
            "term": "Keep the case open",
            "gloss": (
                "Say what you expect in terms clear enough to be shown wrong, and go "
                "back and check. The people who forecast best are not the ones who know "
                "most; they are the ones willing to change their minds."
            ),
        },
    ],
}

INSIGHTS = [
    {
        "id": "insight-1",
        "n": 1,
        "title": "Your Feelings Reach the Verdict First",
        "plate": "img/insight-01.png",
        "alt": (
            "A stick figure faces a painting on an easel. A short arrow runs from the "
            "figure's chest straight to a stamp on the frame reading GENUINE, while a "
            "much longer arrow leaves the head, loops all the way around the easel and "
            "arrives at the same stamp afterwards."
        ),
        "lede": (
            "Abraham Bredius, the foremost Vermeer scholar of his day, was shown a "
            "painting called Christ at Emmaus. He inspected it for every sign of "
            "forgery he knew and found none, then declared it genuine, perhaps "
            "Vermeer's finest work. He said afterwards that when he saw it, he had "
            "difficulty controlling his emotion."
        ),
        "evidence": (
            "The painting was a forgery, and not even a good one. The remark about his "
            "emotion is what explains the failure: the feeling arrived first, and the "
            "expert examination that followed was hunting for reasons rather than for "
            "the truth. Some studies find that experts are less likely to change their "
            "minds when contradicted, not more."
        ),
        "operative": (
            "Most numbers carry no charge at all — nobody's pulse rises at the distance "
            "to Mars. But a claim touching politics, crime or money produces a reaction "
            "before any judgment is made, and from that point evidence is being shopped "
            "in rather than weighed. Reading a statistic well starts with noticing what "
            "you want it to say."
        ),
    },
    {
        "id": "insight-2",
        "n": 2,
        "title": "The Average Is True and the Train Is Full",
        "plate": "img/insight-02.png",
        "alt": (
            "Ten simple train carriages stand in a row. One is packed with stick "
            "figures shoulder to shoulder and the other nine are empty. A bracket "
            "beneath all ten leads to a single carriage lettered AVERAGE, holding a few "
            "evenly spaced stick figures."
        ),
        "lede": (
            "Presenting a radio programme in London meant a daily commute on a crowded "
            "bus and a Tube train bursting at the seams. The published figures said the "
            "average bus carried twelve people and the average Tube train fewer than a "
            "hundred and thirty. Both came from Transport for London, which counts "
            "payment cards tapped at boarding."
        ),
        "evidence": (
            "Picture a line running ten trains a day. One carries a thousand passengers "
            "and the other nine carry nobody. Average occupancy is a hundred a train, "
            "close to London's real figure, and yet every passenger on that line "
            "travelled in a crush. The average is accurate and silent about the only "
            "thing anyone noticed."
        ),
        "operative": (
            "Statistics and personal experience are usually answering different "
            "questions, which is why arguing over which one is lying settles so little. "
            "On health the statistics win, because they describe the likeliest outcome "
            "across the greatest number of people: a chain-smoking grandmother in fine "
            "health has not repealed the sixteenfold rise in lung cancer risk."
        ),
    },
    {
        "id": "insight-3",
        "n": 3,
        "title": "Every Number Is a Definition in Disguise",
        "plate": "img/insight-03.png",
        "alt": (
            "A row of identical small circles. Two hand-drawn loops enclose overlapping "
            "but different subsets of the same circles, and each loop leads to its own "
            "tally box showing a different total. Two circles sit exactly where the "
            "loops diverge."
        ),
        "lede": (
            "In the late 2010s British infant mortality rates varied sharply from one "
            "region to another and at first nobody could say why. The answer was a "
            "definition. A pregnancy ending at twenty-two or twenty-three weeks was "
            "recorded in London as a miscarriage, and in the English Midlands as a live "
            "birth followed by an early death."
        ),
        "evidence": (
            "That difference in recording was enough on its own to account for the gap "
            "between the two regions' rates. Count the babies who died sounds like the "
            "simplest instruction imaginable, and one step in it stops being simple, "
            "because the line between a fetus and a baby is genuinely difficult and "
            "bitterly contested."
        ),
        "operative": (
            "Murky definitions are useful to anyone who wants to move you. A 2017 "
            "proposal from a Brexit lobby group would have frozen unskilled immigration "
            "for five years, with unskilled meaning anyone earning under thirty-five "
            "thousand pounds — most nurses, primary school teachers, paralegals and "
            "pharmacists. Support the policy or reject it, but argue about the policy "
            "rather than the word."
        ),
    },
    {
        "id": "insight-4",
        "n": 4,
        "title": "One Number Alone Is Not Information",
        "plate": "img/insight-04.png",
        "alt": (
            "A long horizontal strip of fifty-two small squares runs across the page, "
            "lettered ONE YEAR. Two squares near the left are inked solid black and "
            "lettered WALL. A stick figure stands beside the strip looking along its "
            "full length."
        ),
        "lede": (
            "In April 2018 London's newspapers announced that the city's murder rate "
            "had overtaken New York's. Fourteen murders in New York that February, "
            "fifteen in London. Setting aside that the two cities define murder "
            "differently, the claim was technically true — and it supports no "
            "conclusion whatsoever."
        ),
        "evidence": (
            "In 1990 London recorded a hundred and eighty-four murders and New York two "
            "thousand two hundred and sixty-two. By 2017 the figures were a hundred and "
            "thirty and two hundred and ninety-two. Both cities had become far safer, "
            "and New York had improved so much that its rate now sometimes dips below "
            "London's."
        ),
        "operative": (
            "Scale works the way time does. A border wall costing twenty-five billion "
            "dollars sounds enormous beside nothing at all; beside a defence budget of "
            "just under seven hundred billion a year, about two billion a day, it is a "
            "fortnight of military operations. The comparison does not settle the "
            "argument. It establishes what size of thing is being argued about."
        ),
    },
    {
        "id": "insight-5",
        "n": 5,
        "title": "What Gets Published Is Not What Was Found",
        "plate": "img/insight-05.png",
        "alt": (
            "A sieve above a shelf. Many small cards marked with flat lines and a few "
            "marked with tall spikes press against the mesh; only the spiked cards pass "
            "through a narrow chute lettered PRINTED onto the shelf, while the flat "
            "ones stack in a drawer below."
        ),
        "lede": (
            "Psychologists Sheena Iyengar and Mark Lepper ran a supermarket stall "
            "offering shoppers either twenty-four varieties of jam to taste or six. The "
            "larger display drew more people, but three per cent of them bought a jar "
            "against thirty per cent at the smaller one. Too much choice paralyses us, "
            "ran the conclusion, and it went everywhere."
        ),
        "evidence": (
            "Gathered together, the published and unpublished research on choice tells "
            "a different story. Published papers tended to find a large effect, "
            "strongly positive or strongly negative. Unpublished papers tended to find "
            "no effect at all. Averaged across the whole body of work, offering more "
            "choices came to approximately zero."
        ),
        "operative": (
            "No cheating is required to produce that. Journals prefer surprises, so the "
            "studies anyone hears about are a selected sample of the studies that were "
            "run; and because careers and incomes depend on publishing, researchers "
            "carry a standing incentive to make a finding look more significant than it "
            "is. A lone spectacular result is the least reliable evidence there is."
        ),
    },
    {
        "id": "insight-6",
        "n": 6,
        "title": "An Algorithm Finds Patterns, Not Causes",
        "plate": "img/insight-06.png",
        "alt": (
            "A boxy machine with a cut-away panel revealing a large snowflake inside. "
            "Arrows feed in from a snowman, a basketball, a scarf and a coughing stick "
            "figure; one arrow leaves the machine and drives a sharply spiking chart "
            "lettered FLU."
        ),
        "lede": (
            "Google Flu Trends counted searches for terms like flu symptoms and "
            "pharmacies near me, and estimated new cases faster than the Centers for "
            "Disease Control could. Four years after launch it collapsed, announcing a "
            "severe outbreak in a winter without one and at one point putting flu at "
            "twice the official level."
        ),
        "evidence": (
            "Google never knew what connected those searches to the disease. The "
            "algorithm hunted for correlations and found some with nothing to do with "
            "flu, high school basketball among them. What it had built was a "
            "general-purpose winter detector, which is also why it missed a summer "
            "outbreak in 2009."
        ),
        "operative": (
            "This is not an argument against algorithms. Human judges are neither "
            "wholly objective nor consistent in sentencing, and a system comparing a "
            "case against similar past ones can be fairer than a person having a bad "
            "morning. Telling the two situations apart requires seeing inside, which is "
            "what the companies operating these systems are least willing to allow."
        ),
    },
]

ACTIONS = [
    {
        "id": "action-1",
        "n": 1,
        "title": "Ask Who Is Missing From the Sample",
        "plate": "img/action-01.png",
        "alt": (
            "Three panels. A small ring of identical stick figures lettered SAMPLE; the "
            "same ring drawn small inside a much larger crowd of varied stick figures "
            "lettered EVERYONE; then one stick figure with a clipboard walking out "
            "toward the people standing outside the ring."
        ),
        "lede": (
            "Before accepting what a study or a poll found, establish who was in it. "
            "Solomon Asch's famous conformity experiments were run on white male "
            "American college students in the 1950s, and so much research is run on "
            "people who are Western, Educated, Industrialised, Rich and Democratic that "
            "the acronym WEIRD was coined for it."
        ),
        "operative": (
            "Use this on any finding presented as a fact about people in general, and "
            "on every poll. It is working when you can name the population a result "
            "actually covers. By 1996 Asch's study had a hundred and thirty-three "
            "follow-ups and the effect held; the more diverse ones added that people "
            "conform more readily to friends than to strangers."
        ),
        "caveat": (
            "Polling cannot fix this by recruiting better, because some kinds of people "
            "simply respond and others do not — that is sample bias, and no arithmetic "
            "afterwards removes it. Where the data was gathered matters too: a survey "
            "of American Twitter users describes American Twitter users."
        ),
    },
    {
        "id": "action-2",
        "n": 2,
        "title": "Trace the Number Back to Whoever Produced It",
        "plate": "img/action-02.png",
        "alt": (
            "A stick figure pulls a long thread hand over hand. The thread runs across "
            "the page from a small card in the figure's hand, around two turns, to an "
            "office building where a second stick figure sits at a desk holding the "
            "other end."
        ),
        "lede": (
            "Follow a figure back to the body that made it, and ask what happens to "
            "that body when the number is inconvenient. The Congressional Budget "
            "Office, created in 1974, was described by one official as a manhole you "
            "drop a bill into and get a cost estimate back from twenty minutes later."
        ),
        "operative": (
            "Do this before a number becomes the basis of an argument, and especially "
            "when it flatters whoever is quoting it. Jimmy Carter's administration "
            "complained that the CBO was not helping when it found his energy "
            "efficiency proposals would fall short of their promises. That complaint is "
            "the sign of an agency doing its job."
        ),
        "caveat": (
            "The alternative is on record. Greece, needing to hold its deficit below "
            "three per cent of GDP to stay in the eurozone, left several billion euros "
            "of borrowing out of its accounts. The European Union found the real figure "
            "during the financial crisis, and the Greek economy collapsed."
        ),
    },
    {
        "id": "action-3",
        "n": 3,
        "title": "Read a Chart in the Same Order You Read a Claim",
        "plate": "img/action-03.png",
        "alt": (
            "Three panels. A stick figure faces a steeply rising chart with motion "
            "lines at the chest; the same figure runs a finger down the vertical axis "
            "where tick marks now appear; then the chart redrawn with its full axis, "
            "the line rising gently."
        ),
        "lede": (
            "Notice what the picture makes you feel, and only then work out what it "
            "says: what the axes are, what is being counted, which dataset or "
            "experiment produced it. David McCandless's animation Debtris drops costs "
            "down the screen as coloured blocks, some of them setting a net figure "
            "against a gross one."
        ),
        "operative": (
            "Apply it to any chart built to be memorable, which now means most of them. "
            "It is working when you can state the graphic's claim in a plain sentence "
            "before deciding whether you believe it. Elegance is not evidence, and a "
            "chart that moves beautifully is one you are less likely to interrogate."
        ),
        "caveat": (
            "Persuasive design is not itself a scandal. Florence Nightingale's rose "
            "diagram — two roses side by side, deaths before sanitary measures and "
            "after — was built to convince doctors who did not yet know that poor "
            "hygiene spread germs. It convinced them, and public health acts followed."
        ),
    },
    {
        "id": "action-4",
        "n": 4,
        "title": "Keep a Short List of Landmark Numbers",
        "plate": "img/action-04.png",
        "alt": (
            "A stick figure draws a folding carpenter's rule out of a shirt pocket and "
            "holds it up against a floating block. The rule's marks carry short "
            "lettered figures, and the block reaches only a small way along it."
        ),
        "lede": (
            "Memorise a handful of reference figures so that a comparison is always to "
            "hand without looking anything up — the entrepreneur Andrew Elliott "
            "recommends exactly this. The population of the United States is three "
            "hundred and twenty-five million, the United Kingdom's is sixty-five "
            "million, Boston to Seattle is three thousand miles, and the average novel "
            "runs a hundred thousand words."
        ),
        "operative": (
            "Reach for the list whenever a figure arrives on its own, which is most of "
            "the time. A ten-thousand-word report sounds long until it turns out to be "
            "a tenth of a novel. It is working when the comparison is a reflex: "
            "something in your head already has something to set beside the new number."
        ),
    },
    {
        "id": "action-5",
        "n": 5,
        "title": "Write the Prediction Down Where It Can Be Checked",
        "plate": "img/action-05.png",
        "alt": (
            "Three panels. A stick figure writes on a card and drops it into a box "
            "marked with a date; a calendar page; the same figure lifting the card back "
            "out and holding it beside a newspaper, looking from one to the other."
        ),
        "lede": (
            "State what you expect in terms clear enough to be declared true or false "
            "later, record it, and go back to it. Philip Tetlock collected some "
            "twenty-seven thousand five hundred predictions from almost three hundred "
            "experts in politics, geopolitics and economics, framed as answerable "
            "questions, and then waited eighteen years for the results."
        ),
        "operative": (
            "Do it whenever you catch yourself confident about how something will turn "
            "out. Tetlock's experts were wrong, overconfident, and misremembered their "
            "own forecasts as right where the record showed otherwise. It is working "
            "when you hold a record capable of embarrassing you; the alternative is a "
            "memory that edits itself in your favour."
        ),
        "caveat": (
            "Being wrong is not the failure to guard against. Tetlock's second study, "
            "drawing on twenty thousand forecasters, found a group who were "
            "consistently above average and improving over time. The trait that marked "
            "them out was open-mindedness — a willingness to drop a view when the "
            "evidence moved."
        ),
    },
]

VOCABULARY = {
    "intro": "Each one is a place where a number goes wrong before anybody reads it.",
    "terms": [
        {
            "term": "Publication bias",
            "def": (
                "Journals far prefer a surprising result to an inconclusive one, so the "
                "findings that reach the public are a selected sample of those produced."
            ),
        },
        {
            "term": "Sample bias",
            "def": (
                "Some kinds of people are likelier to answer a poll than others, so "
                "respondents differ systematically from the population. No later "
                "calculation removes it."
            ),
        },
        {
            "term": "WEIRD",
            "def": (
                "Western, Educated, Industrialised, Rich and Democratic — the narrow "
                "population from which a great deal of psychological research draws its "
                "subjects, and therefore its conclusions about people in general."
            ),
        },
        {
            "term": "Big data and algorithms",
            "def": (
                "Big data is the information thrown off by ordinary life — browsing, "
                "card payments, phones — collected for reasons unrelated to the "
                "question. An algorithm finds patterns in it, reporting correlations it "
                "can measure rather than causes it understands."
            ),
        },
        {
            "term": "Average",
            "def": (
                "A single figure standing in for a whole distribution. It can be "
                "perfectly accurate and describe nobody's actual experience — ten "
                "trains, one full and nine empty, average out to a hundred passengers "
                "each."
            ),
        },
        {
            "term": "Statistical bedrock",
            "def": (
                "The official figures a country produces about itself, and the "
                "independent agencies producing them. Acting on evidence requires "
                "somewhere for evidence to come from."
            ),
        },
        {
            "term": "Landmark numbers",
            "def": (
                "A short memorised list of reference figures — populations, distances, "
                "budgets — held in the head so that any new number arrives with "
                "something to be compared against."
            ),
        },
        {
            "term": "Superforecaster",
            "def": (
                "One of the minority who predict better than average and improve with "
                "practice. What marks them is open-mindedness, not expertise."
            ),
        },
    ],
}

QUICK_REFERENCE = [
    {"kind": "line", "label": "01", "text": "Notice how a claim makes you feel before deciding whether it is true."},
    {"kind": "line", "label": "02", "text": "Ask which question the statistic answers and which one your experience answers."},
    {"kind": "line", "label": "03", "text": "Find out what was counted before arguing about the count."},
    {"kind": "line", "label": "04", "text": "Put the figure beside something: a longer timescale, or a bigger total."},
    {"kind": "line", "label": "05", "text": "Ask what happened to the studies that found nothing."},
    {"kind": "line", "label": "06", "text": "Ask who was in the sample, and who never had the chance to be."},
    {"kind": "line", "label": "07", "text": "Judge each algorithm on evidence; demand enough access to judge it."},
    {"kind": "line", "label": "08", "text": "Ask who produced the number and whether they answer to the people it flatters."},
    {"kind": "line", "label": "09", "text": "Read a chart's axes before accepting what its shape made you feel."},
    {"kind": "line", "label": "10", "text": "Say what you expect, record it, and change your mind when it fails."},
]

CLOSING_LINE = "Be curious. Look deeply for the facts, and keep asking questions."

BOOK = {
    "title": "The Data Detective",
    "subtitle": "Ten Easy Rules to Make Sense of Statistics",
    "author": "Tim Harford",
    "cover": "img/cover.jpg",
    "links": [
        {"mark": "\u2193", "label": "Spoken Companion", "href": "Spoken_Companion.docx"},
    ],
    "question": CENTRAL_QUESTION,
    "answer": CENTRAL_ANSWER,
    "framework": FRAMEWORK,
    "insights": INSIGHTS,
    "actions": ACTIONS,
    "vocabulary": VOCABULARY,
    "quickReference": QUICK_REFERENCE,
    "closingLine": CLOSING_LINE,
}

# --- flat tail blocks, applied after BOOK is built -------------------------

TAKEAWAY = {
    "insight-1": "The verdict arrives before the reasoning does. Expertise builds a better case for what you already believe.",
    "insight-2": "A statistic and your own experience answer different questions. Work out which question each one is answering.",
    "insight-3": "Every count rests on a definition somebody chose. The definition is usually where the real argument is.",
    "insight-4": "A figure with nothing beside it can be entirely true and still tell you nothing at all.",
    "insight-5": "Journals prefer surprises, so famous findings are a selected sample. A lone spectacular study proves least.",
    "insight-6": "Google built a flu detector and got a winter detector. A system nobody can inspect is one nobody can correct.",
    "action-1": "Ask who was counted, then ask who never had the chance to be. The gap is where the error lives.",
    "action-2": "Find out who made the number and what happens to them when it turns out to be inconvenient.",
    "action-3": "Notice what the picture makes you feel, then find out what its axes actually say.",
    "action-4": "Memorise a few reference figures so a comparison is always available without looking anything up.",
    "action-5": "State what you expect clearly enough to be proved wrong, then go back and check.",
}

for _e in BOOK["insights"] + BOOK["actions"]:
    _e["takeaway"] = TAKEAWAY[_e["id"]]

# The exact hand-lettered title each prompt asks for, recorded when the prompt
# was authored. verify_lettering.py scores plates against these.
LETTERING = {
    "insight-1": "THE FEELING ARRIVES FIRST",
    "insight-2": "THE AVERAGE IS TRUE",
    "insight-3": "WHAT DID YOU COUNT?",
    "insight-4": "ONE NUMBER, NO SCALE",
    "insight-5": "WHAT GETS PRINTED",
    "insight-6": "PATTERN, NOT CAUSE",
    "action-1": "WHO IS MISSING?",
    "action-2": "WHERE DID IT COME FROM?",
    "action-3": "READ THE AXES",
    "action-4": "LANDMARK NUMBERS",
    "action-5": "WRITE IT DOWN",
}

COMPANION_FOOTER = "The Data Detective — Spoken Companion"

COMPANION = [
    {
        "level": 1,
        "heading": "Before the Number Reaches You",
        "paras": [
            "In countries with more storks, more babies are born. The correlation is real, and it proves nothing at all, because storks do not deliver babies. Arguments like that are easy to build, and the ease of building them has left a lot of sensible people suspicious of statistics on principle.",
            "The suspicion costs more than it saves. Without statistics nobody would know that a smoker is sixteen times more likely to develop lung cancer, or that COVID-19 passes from one person to another. The goal is not to distrust numbers. It is to tell the good ones from the bad ones, and that turns out to depend far less on mathematics than on ten habits of attention.",
        ],
    },
    {
        "level": 2,
        "heading": "The Forgery That Was Too Beautiful to Doubt",
        "paras": [
            "When Abraham Bredius, the most respected Vermeer scholar of his day, was shown a painting called Christ at Emmaus, he was awestruck. He was also careful. He examined it for every sign of forgery he knew and found none. He declared it a genuine Vermeer, perhaps the finest one. He said afterwards that when he saw it, he had difficulty controlling his emotion.",
            "It was a fake. It was not even a very good painting. And the sentence about his emotion is the one that explains the mistake, because the feeling arrived before the verdict did.",
            "Most statistical claims do the same thing to most people. Some numbers carry no charge at all — nobody's pulse rises at the news that Mars is more than thirty million miles from Earth. But a claim about immigration, or crime, or a policy you already hold views about gets a rise out of you before you have decided anything, and from that point on you are not weighing the evidence, you are shopping in it. If it fits what you already believe it becomes proof. If it does not, it becomes an outlier, a bad study, an agenda.",
            "Expertise offers no protection. Some studies have found that experts are less likely to change their minds in the face of contradictory evidence, not more. They are both motivated to avoid the uncomfortable finding and unusually good at producing the argument that lets them dismiss it. Knowing more gives you better tools for defending what you already think.",
            "So the first rule is not a technique for reading numbers. It is a question about yourself. When a claim arrives, notice what you feel. Are you outraged, delighted, or already reaching for the reason it cannot be right? Then pause, and ask whether you are straining toward a particular conclusion. That pause is what makes all the other rules usable.",
        ],
    },
    {
        "level": 2,
        "heading": "The Crowded Train and the Empty Average",
        "paras": [
            "Presenting a radio programme in London meant a commute from the east of the city to the west: a crowded bus, then a Tube train practically bursting at the seams. Harford went looking for the figures on how busy London's transport really was, and found that the average bus carried twelve people and the average Tube train fewer than a hundred and thirty. The numbers felt like a lie. He had been standing in those trains.",
            "They were not a lie, and neither was his experience. Start with where the figures came from: Transport for London, which counts passengers from the payment cards they tap before boarding. That origin is credible. Then ask why lived experience would differ.",
            "Imagine a line running ten trains a day. One carries a thousand people; the other nine carry nobody at all. Average occupancy on that line is a hundred people a train, close to London's real figure, and yet every single passenger who travelled that day travelled in a crush. The average is true. It is also silent about the only thing the passengers noticed.",
            "Statistics and personal experience are usually answering different questions, which is why the argument between them so rarely resolves anything. Sometimes both are informative, as here. Sometimes one clearly wins. On health the statistics win, because they describe the most likely outcome across the greatest number of people. A ninety-year-old grandmother who has smoked all her life and is doing fine has not repealed the finding that smoking makes lung cancer sixteen times more likely. She is one train on the line.",
            "Understanding comes from knowing which of the two answers your question — and often from asking what would have to be true for both of them to be right at once.",
        ],
    },
    {"level": 1, "heading": "What the Number Is Actually Saying", "paras": []},
    {
        "level": 2,
        "heading": "Count the Babies, But Which Ones",
        "paras": [
            "In the late 2010s the United Kingdom appeared to be in the middle of an infant mortality crisis. Rates of early death varied sharply from one part of the country to another, and at first nobody could say why.",
            "The explanation turned out to be a definition. A pregnancy ending at twenty-two or twenty-three weeks was recorded in London as a miscarriage, and in the English Midlands as a live birth followed by an early death. Those are two ways of counting the same events, and the difference between them was enough to account for the entire gap between London's mortality rate and the Midlands'.",
            "Count the babies who died sounds like the simplest instruction in the world. Go one step in and it stops being simple, because the line between a fetus and a baby is genuinely difficult and bitterly contested. Statistics are, at bottom, counting, and yet almost nobody asks what was counted.",
            "Take the claim that children who play violent video games are more likely to be violent in real life. What is a violent video game? How often does a child have to play one to qualify? And how was violence measured — a police record, a questionnaire, something done in a laboratory? Until those are answered there is nothing in the sentence to agree or disagree with.",
            "Murky definitions are useful to anyone who wants to move you. In 2017 a lobby group campaigning for Brexit proposed a five-year freeze on unskilled immigration. Unskilled, in that proposal, meant anyone earning under thirty-five thousand pounds, which would have covered most nurses, primary school teachers, paralegals and pharmacists. You can still support the policy or reject it. But you are now arguing about the policy rather than about the word.",
            "So before you accept or refute a claim, ask what it counted. If someone tells you inequality has risen, the first question is: inequality of what?",
        ],
    },
    {
        "level": 2,
        "heading": "Fifteen Murders and Nothing to Compare Them To",
        "paras": [
            "In April 2018 London's newspapers announced that the city's murder rate had overtaken New York's. Setting aside that the two cities define murder differently, the claim was technically true: fourteen murders in New York in February, fifteen in London.",
            "It tells you nothing. In 1990 London had a hundred and eighty-four murders and New York had two thousand two hundred and sixty-two, more than ten times as many. By 2017 London was at a hundred and thirty and New York at two hundred and ninety-two. Both cities had become dramatically safer, and New York had improved so much that its rate now occasionally dips below London's. Read in that light, one month's figures describe a triumph rather than a collapse. London had not descended into gang-ridden mayhem in February.",
            "The news works against this, because it is built to deliver what has happened since yesterday. Imagine a newspaper published once every twenty-five years. Its front page would carry the arrival of the World Wide Web and the rise of China as a global power. It would not carry the murder count of two cities in a single month.",
            "The same move works on scale as well as on time. A border wall costing twenty-five billion dollars sounds enormous until you set it beside a defence budget of just under seven hundred billion a year, which is about two billion a day. The wall is roughly a fortnight of American military operations.",
            "You may still conclude that the wall costs too much, or that fifteen murders in a month is a scandal. Both are defensible positions. They are simply better positions once you have stepped back far enough to see what the number sits beside.",
        ],
    },
    {"level": 1, "heading": "Where the Number Came From", "paras": []},
    {
        "level": 2,
        "heading": "The Jam That Wasn't There",
        "paras": [
            "The psychologists Sheena Iyengar and Mark Lepper ran a supermarket stall offering jam to taste, sometimes twenty-four varieties and sometimes six. Tasters were given a voucher to buy at a discount. The big display attracted more customers, but only three per cent of them bought a jar, against thirty per cent at the small display. The conclusion, that too much choice paralyses us, went everywhere: pop psychology, business books, TED talks.",
            "Then researchers gathered the whole body of work on choice, published and unpublished. Published papers tended to find a large effect, either strongly positive or strongly negative. Unpublished papers tended to find no effect at all. Averaged together, the effect of offering more choices came to approximately zero.",
            "Nothing in that requires anyone to have cheated. It only requires journals to prefer surprises, which they do, because a result that overturns something is publishable and a result confirming what everyone assumed is not. That is publication bias, and it means the studies you hear about are a selected sample of the studies that were run. On top of it sits a plainer problem: careers and incomes depend on publishing, which gives researchers a standing incentive to present a finding as more significant than it really is.",
            "The practical consequence is not to disbelieve research. It is to notice that a single spectacular study is the least reliable kind of evidence there is, and to ask what happened after it. Does the finding fit with what else is known, or is it a lone outlier that became famous because it was fun? Has anyone repeated it? A result that has survived a decade of other people trying to reproduce it is a different object from one that made a splash last month.",
        ],
    },
    {
        "level": 2,
        "heading": "Who Wasn't in the Room",
        "paras": [
            "In the 1950s the psychologist Solomon Asch showed people a reference line and three comparison lines, and asked which of the three matched. The task was trivial. The catch was that the room was full of people placed there to give the same wrong answer, and a significant share of the time the real subject went along with them. It is one of the most quoted findings in psychology: people conform.",
            "What the experiment demonstrated was that white male American college students in the 1950s conform. Every subject came from one narrow population, and a finding from a narrow population is a finding about that population until somebody checks. Psychologists have become uncomfortably aware of how often this happens. So much research is run on people who are Western, Educated, Industrialised, Rich and Democratic that the acronym WEIRD was coined for it.",
            "In Asch's case the conclusion mostly survived. By 1996 the study had inspired a hundred and thirty-three follow-ups and the overall result held up. Most of those follow-ups were not very diverse either, but the ones that were added things the original could not have seen: people conform more readily to groups of friends than to strangers, and groups of women conformed more than groups of men. Widening the sample did not overturn the finding. It changed what the finding meant.",
            "Academic research can usually fix this by recruiting better. Polling cannot, because the people who answer polls are not a random slice of anybody. Some kinds of people simply respond and others do not, which is sample bias, and no arithmetic applied afterwards removes it. Where the data is gathered matters too. A poll of American Twitter users tells you about young, college-educated Americans who use Twitter.",
            "So when a number arrives, ask who is in it, and then ask who is missing.",
        ],
    },
    {
        "level": 2,
        "heading": "The Algorithm That Learned Winter",
        "paras": [
            "Google Flu Trends counted searches for things like flu symptoms and pharmacies near me, and could estimate new daily flu cases faster than the Centers for Disease Control. It looked like the future: big data, meaning everything generated by browsing the web, paying with cards and carrying phones, fed to an algorithm that finds patterns in it. Four years after it was announced, the project collapsed.",
            "It failed by declaring a severe outbreak in a winter when there was not one, at one point estimating flu at twice the level in the official figures. The reason is worth sitting with. Google never knew what connected those searches to the disease. The algorithm was hunting for correlations, and it found some that had nothing to do with flu, high school basketball among them. What it had built was not a flu detector but a general-purpose winter detector, which is why it also failed to spot a summer outbreak in 2009.",
            "None of this is an argument against algorithms. There is a good deal of evidence that human judges are neither wholly objective nor consistent when handing down criminal sentences, and an algorithm comparing a case against similar cases from the past can produce fairer results than a person having a bad morning. Sometimes the machine is better. Sometimes it is a winter detector.",
            "The only way to tell is case by case, and that requires seeing inside, which is exactly what the companies operating these systems are least willing to allow, because the workings are the business. But an algorithm nobody can inspect is an algorithm nobody can correct. When it is deciding something that matters, the reasonable demand is not that it be perfect. It is that enough people can look under the hood to find out how it decides, and where it is wrong.",
        ],
    },
    {
        "level": 2,
        "heading": "The Dull Institutions That Keep a Country Honest",
        "paras": [
            "The Congressional Budget Office was established in 1974 to tell Congress what its own proposals would cost. One official described the process as dropping a bill down a manhole and having the cost estimate handed back up twenty minutes later. Objective, uncontroversial and dull, which is the point.",
            "The first president to complain was Jimmy Carter, whose proposals for improving American energy efficiency the CBO assessed and found would not work as well as planned. His administration was unhappy that the office was not helping. It was doing precisely its job. A statistical agency that produces the numbers the government wants has stopped being a statistical agency.",
            "What happens without one is on record. To remain in the eurozone, a country must keep its budget deficit below three per cent of its GDP. Greece could not manage that legitimately, so its officials left several billion euros of borrowing out of the accounts here and there. In the middle of the global financial crisis the European Union discovered how much Greece had actually borrowed, and that it could not pay it back. The Greek economy promptly collapsed.",
            "The case for these institutions is not only defensive. A cost-benefit analysis in the United Kingdom found data from the national census feeding into everything from pension policy to deciding where to build schools and hospitals, and enabling every per-capita figure anybody else calculates. Much of the value could not be given a number at all. The measurable part alone came, on a conservative estimate, to five hundred million pounds a year. The census costs less than that and serves for ten years, which is roughly a tenfold return on the investment.",
            "Governments are expected to act on evidence. The evidence has to come from somewhere, and a country that stops paying for honest numbers does not thereby stop needing them.",
        ],
    },
    {"level": 1, "heading": "What You Do Next", "paras": []},
    {
        "level": 2,
        "heading": "Beautiful and Wrong",
        "paras": [
            "David McCandless, the author of Information is Beautiful, made a striking animation called Debtris. Coloured blocks fall down the screen like the old video game, each block sized by cost: the United Nations budget, the estimated cost of the 2003 Iraq war, Walmart's revenue. It is elegant and memorable, and the elegance is the problem, because the thing moves so well that nobody stops to check what is being compared. Some of the blocks set a net measure against a gross one, which is like comparing one company's profit with another's turnover.",
            "The answer is not to distrust anything that has been well designed. In the nineteenth century Florence Nightingale set out to convince doctors that sanitary measures could cut deaths from infectious disease, at a time when nobody yet knew that poor hygiene helped transmit germs. She drew what became known as the rose diagram: two roses side by side, one showing deaths before the measures and one after. The difference was visible at a glance. Hesitant doctors were persuaded, and public health acts followed.",
            "So a graph gets the same treatment as any other claim, in the same order. Notice what it makes you feel, because a good chart is built to make you feel something. Then, before accepting the feeling, work out what the thing actually says: what the axes mean, what is being counted, which experiment or dataset it reflects.",
            "And accept that someone is trying to persuade you. That is not automatically a scandal. Nightingale was trying to persuade people too.",
        ],
    },
    {
        "level": 2,
        "heading": "The Experts Who Were Certain",
        "paras": [
            "Philip Tetlock was one of a group of social scientists handed an enormous task: to think about how to prevent nuclear war between the United States and the Soviet Union. He interviewed expert after expert about what might happen next and why, and noticed how relentless they were in justifying forecasts that had already failed.",
            "So he tested it properly. He collected some twenty-seven thousand five hundred predictions from almost three hundred experts in politics, geopolitics and, to a lesser extent, economics. He asked clear questions that could later be declared true or false without argument. Then he waited eighteen years for the results. The experts were terrible. Their predictions were wrong, they were overconfident, and they selectively misremembered their own forecasts, recalling themselves as having been right all along where the record showed they had been wrong.",
            "That could mean the world is simply too complex to predict. Tetlock thought not, and ran a second, more ambitious study drawing forecasts from twenty thousand experts and amateurs alike. Some people really were better than others. Not perfect, but consistently above average, and improving over time, which ruled out luck. He called them superforecasters, and the quality that marked them out most clearly was open-mindedness. They held no loyalty to a particular forecasting method or to a view they had already expressed, and they were happy to change their minds when shown new evidence.",
            "That locates the problem precisely. Mistakes about the world are not usually caused by a shortage of statistical knowledge. They are caused by a refusal to accept data that contradicts something already decided, which is the same reflex that fooled a great scholar standing in front of a fake Vermeer.",
            "So keep the case open. Say what you expect, in terms clear enough that you could be shown to be wrong, and notice when the world disagrees.",
        ],
    },
    {
        "level": 2,
        "heading": "A Short List of Landmark Numbers",
        "paras": [
            "One habit makes all of this cheaper to run. The entrepreneur Andrew Elliott recommends memorising a handful of landmark numbers, so that comparisons are available without looking anything up. The population of the United States is three hundred and twenty-five million. The United Kingdom's is sixty-five million. The drive from Boston to Seattle is three thousand miles. The average novel is a hundred thousand words long. A ten-thousand-word report sounds long until you notice it is a tenth of a novel.",
            "Landmark numbers turn the fourth rule from an intention into a reflex. When a figure arrives with nothing beside it, something in your head already has something to set beside it.",
            "That is the shape of the whole thing. Notice what you feel. Weigh the statistic against your own experience, and work out which question each is answering. Ask what was counted, and what the number should be compared with. Find out where it came from, who was in the sample, and who was left out. Watch the chart as carefully as the sentence. And stay willing to be wrong.",
            "None of it is arithmetic. The one instruction underneath all ten rules is to be curious: to look at a number and want to know more about it than whether it supports you. Look deeply for the facts, and keep asking questions.",
        ],
    },
]
