"""Content module — the durable artifact.

The page, the PDF and the docx all read from this. None of them hardcode
content, which is what makes a rebuild a re-render.

The Insights + Action Guide PDF is still produced and still ships in the
folder — it just is not linked from the page.
"""

BOOK = {
    "title": "The Art of Spending Money",
    "author": "Morgan Housel",
    "subtitle": "Simple Choices for a Richer Life",
    "cover": "img/cover.jpg",
    "links": [
        {
            "mark": "↓",
            "label": "Spoken companion",
            "href": "Spoken_Companion.docx"
        },
        {
            "mark": "↗",
            "label": "Speechify",
            "href": "https://speechify.app.link/TKiJ8O7KB5b"
        }
    ],
    "argument": {
        "question": "Once you have money — a little or a lot — how do you actually use it to live a better life?",
        "answer": "Spending is an art, not a science. There is no formula, because what feeds one person leaves another empty. But there is one distinction that organizes almost everything: there are two ways to use money. One is as a tool to live a better life. The other is as a yardstick of status to measure yourself against other people. Nearly everyone says they want the first. Most spend their lives chasing the second."
    },
    "framework": {
        "name": "The Tool or the Yardstick",
        "intro": "The book keeps returning to one question asked four different ways. Each part is the same distinction viewed from a different angle.",
        "steps": [
            {
                "mark": "01",
                "term": "Two uses",
                "gloss": "Every dollar either improves your life or adjusts someone's opinion of you. Most spending confusion is a failure to say which one is happening."
            },
            {
                "mark": "02",
                "term": "The gap",
                "gloss": "Happiness is the distance between expectations and circumstances. That gap can be closed from either end, and the expectations end is the one you control."
            },
            {
                "mark": "03",
                "term": "The hidden debts",
                "gloss": "Status, envy, and money-as-identity are liabilities that never appear on a balance sheet. Like all debt, they come due."
            },
            {
                "mark": "04",
                "term": "Independence and purpose",
                "gloss": "The simplest formula for a pretty nice life: the independence to do what you want, and the wisdom to want to do meaningful things."
            }
        ]
    },
    "insights": [
        {
            "id": "insight-1",
            "title": "Every purchase is a tool or a yardstick",
            "lede": [
                "Money does one of two things for you. It gives you something that makes your life better, or it adjusts what other people think of you. Both are real, but they are not the same purchase and they do not deliver the same return. Most spending regret comes from buying the second while telling yourself you bought the first."
            ],
            "evidence": "Working as a valet at a Los Angeles hotel during college, Housel overheard a man at an invite-only furniture show say he had just spent twenty-one thousand dollars on an armchair. Catching the stunned expressions of the valets, the man explained: when you have money, this is what you're supposed to do. Not that he liked it. That he was supposed to.",
            "operative": "Before a purchase of any size that makes you hesitate, say out loud which of the two you are buying. The answer is usually available immediately, and naming it is most of the work.",
            "plate": "img/insight-01.png",
            "alt": "A stick figure hammering to build a house on one side; on the other, a figure holding a giant ruler up against three onlookers. Labelled Tool, checked, and Yardstick, crossed out."
        },
        {
            "id": "insight-2",
            "title": "You don't want nice things. You want respect and admiration",
            "lede": [
                "The desire for money and what it buys usually stands in for something else — being noticed, taken seriously, thought well of. Stuff is one lever for getting that, and it is the fastest one, which is why it gets reached for first. It is also the least durable and the least effective on the people whose opinion you actually want."
            ],
            "evidence": "This is not a modern complaint about social media. Adam Smith argued in 1759 that the point of all the toil and bustle of the world was not to supply the necessities of nature — even the poorest workers of his day had those — but to be observed and attended to. It is the vanity, he wrote, not the ease or the pleasure, that interests us.",
            "operative": "Write the obituary you'd want, then notice what isn't in it: horsepower, square footage, carats, salary. Judge new spending against three questions — how effective is this at getting attention, how long does the attention last, and whose attention is it. Strangers gawk at the car, not at you.",
            "plate": "img/insight-02.png",
            "alt": "A sports car drawing admiring stares from strangers on one side; on the other, a person at a table being listened to by friends. Stuff crossed out, Respect checked."
        },
        {
            "id": "insight-3",
            "title": "Wealth is what you have minus what you want",
            "lede": [
                "Wealth looks additive — more money, more wealth. It isn't. What matters is the gap between what you have and what you want, and that gap has two ends. Wanting less does the same work as earning more, is more in your control, and unlike the earning game it can actually be won."
            ],
            "evidence": "Housel's grandmother-in-law spent three decades in retirement on a Social Security check and nothing else, technically on the verge of poverty, perfectly content in a small garden with books from the library. He has met half a dozen billionaires. Not one was as happy as she was.",
            "operative": "Treat rising expectations as a cost, not a neutral fact. When you notice yourself saying you'd be happier with the next thing, you are mostly reporting that you are not happy now. Desire is a form of debt that has to be repaid before any satisfaction arrives.",
            "plate": "img/insight-03.png",
            "alt": "A balance scale: a small stack of coins on the Have side, outweighed by a heap of cars, watches, a boat and a house on the Want side, while a figure looks on."
        },
        {
            "id": "insight-4",
            "title": "Contrast, not amount, is what you actually feel",
            "lede": [
                "There is no such thing as an objectively good experience. Every amount of good is the distance between what you have now and what came just before. This is why the same luxury thrills one person and bores another, and why it stops thrilling the person who has it every day."
            ],
            "evidence": "Michael May was blinded as a baby and had his sight restored at forty-six. Walking out of the doctor's office, what stopped him cold was the lobby carpet — the shapes, the colors. He could not understand how the other patients were sitting there ignoring it. He was getting more from an office carpet than most people get from a perfect sunset.",
            "operative": "Ration the things you love instead of installing them. When you find something that delights you, ask how to keep it an occasional treat rather than a permanent fixture. A simple life is not the opposite of enjoying luxury; it is the mechanism that makes luxury land.",
            "plate": "img/insight-04.png",
            "alt": "Three panels: a flat-faced figure before, the same figure amazed by a patterned carpet, then three bored figures sitting on that same carpet."
        },
        {
            "id": "insight-5",
            "title": "Rich is having money. Wealthy is having control over what it does to you",
            "lede": [
                "Rich means the account balance covers what you want to buy. Wealthy means you have control over what that money does to your personality, your freedom, your ambitions, your friendships. The two come apart constantly, and being controlled by money is a hidden debt that eventually gets repaid with interest."
            ],
            "evidence": "Cornelius Vanderbilt left his heirs something on the order of three hundred billion in today's dollars. Within sixty years almost nothing was left — three generations competing over who could spend it fastest, one heir listing his occupation as gentleman. Chuck Feeney, who co-founded Duty Free Shoppers, tried the luxury version of that life in the 1980s, decided it wasn't for him, and gave away 99.99 percent of eight billion dollars while living in a small apartment and flying coach.",
            "operative": "The tell is whether you can change your mind. Any sentence starting with “I am a” — a saver, a rich person, a value investor — has become an identity, and identities get defended past the point of usefulness. Watch for the version of this that looks like a virtue: a lifetime of good saving habits that can't be switched off in retirement.",
            "plate": "img/insight-05.png",
            "alt": "A figure hung on puppet strings from a giant hand and marked with a dollar sign, labelled Rich and crossed out; beside it a free figure holding a dollar bill, labelled Wealthy and checked."
        },
        {
            "id": "insight-6",
            "title": "There is no such thing as unspent money",
            "lede": [
                "You spend every cent you have ever earned. Money in the account isn't idle; it has already bought something intangible — freedom, options, the ability to spend your time your own way. Every dollar of savings is a claim check on your future. Every dollar of debt is a piece of your future that someone else holds."
            ],
            "evidence": "Antoine Walker earned one hundred and eight million dollars over twelve NBA seasons and filed for bankruptcy in 2010, ending with twelve point seven million in liabilities against four point three million in assets. John Urschel made roughly six hundred thousand across three seasons in the NFL, saved most of it, retired at twenty-six, and went to get a doctorate. Ask whose life you admire more and the answer is not about the money. It is about who still owned their decisions.",
            "operative": "Independence is a spectrum, not a state — every additional dollar of savings and every dollar of lower expense moves you up a rung. Stop asking what the interest rate is and start asking how much independence a debt will cost. Wealth without independence is its own kind of poverty.",
            "plate": "img/insight-06.png",
            "alt": "A large dollar coin with two arrows: one to a television and armchair labelled Things, one to a figure walking out through an open door labelled Independence."
        }
    ],
    "actions": [
        {
            "id": "action-1",
            "title": "Run the island test",
            "lede": [
                "Before a purchase you're uncertain about, ask what you would own if your family were stranded somewhere with everything available and nobody around to notice. On that island you'd take comfort over appearance, the right fabric over the right logo, a great view over a prestigious address — a high-end Toyota over an entry-level BMW.",
                "When: Any purchase large enough to make you pause, and any purchase you find yourself justifying out loud."
            ],
            "operative": "It is working when you can name which one you're buying without flinching, and you buy status on purpose when you buy it at all.",
            "caveat": "Status is not worthless. Fitting into a group you chose is a real part of a good life, and caring about nothing risks nobody caring about you. The failure is confusing one for the other.",
            "plate": "img/action-01.png",
            "alt": "A family of stick figures on a small island with a chair and a window, a handbag crossed out overhead, captioned No one watching."
        },
        {
            "id": "action-2",
            "title": "Decide by future regret",
            "lede": [
                "When you're stuck between spending today and saving for tomorrow, stop arguing the general case. Project forward and ask which choice you'll regret from there. Guppies get eaten young so they spend everything on reproducing immediately; Greenland sharks have no predators and take a hundred and fifty years to reach maturity. Both allocations are correct for the risks they face.",
                "When: Any decision where the live-for-today and save-for-tomorrow camps both have a plausible case — which is most of them."
            ],
            "operative": "It is working when your decisions stop swinging between extreme frugality and impulse, and you can say what specifically you'd regret.",
            "caveat": "What you'd regret changes as you age. The answer that fits a parent of young children is not the answer that fits the same person thirty years later. Recalibrate rather than defending an old conclusion.",
            "plate": "img/action-02.png",
            "alt": "Three panels: a figure at a fork in the road today, the same figure at age eighty looking back along a winding path, then the figure choosing a road."
        },
        {
            "id": "action-3",
            "title": "Buy independence on purpose",
            "lede": [
                "Treat each transfer to savings as an actual purchase with an actual product: five hundred dollars moved is five hundred dollars of independence bought, no different in kind from buying a television. Find yourself on the independence ladder — from covering small hassles, to covering a crisis, to being able to walk away from a bad boss, to not needing a paycheck at all — and aim at the next rung rather than at a number.",
                "When: Every pay period, and every time a purchase would move you down a rung."
            ],
            "operative": "It is working when you can say what a given month of saving bought you: a job you can quit, a month you can take off, a calendar you control.",
            "plate": "img/action-03.png",
            "alt": "A figure climbing a ladder whose rungs are stacked dollar coins, with an arrow reading one rung up and the caption One dollar."
        },
        {
            "id": "action-4",
            "title": "Wide funnel, tight filter",
            "lede": [
                "Nobody can tell you what will make you happy, so test it. Try many kinds of spending — a ten-dollar new food, a fifty-dollar treat, slightly better shoes — and cut without mercy anything that isn't landing, the way you'd abandon a book that isn't working. Finding your thing is a process of elimination, and the cutting matters more than the trying.",
                "When: Continuously, in small amounts, inside whatever budget you already have."
            ],
            "operative": "It is working when you can name your thing, and you can name several expensive things you tried and rejected.",
            "caveat": "Price is a poor proxy for joy. A brand signals consistency, not quality — you can know a McDonald's hamburger tastes the same everywhere without thinking it's the best hamburger.",
            "plate": "img/action-04.png",
            "alt": "Food, shoes, plane tickets, books and event tickets pouring into a wide funnel; most are ejected out the side and crossed out, one item comes through labelled Your thing."
        },
        {
            "id": "action-5",
            "title": "Compound quietly",
            "lede": [
                "Keep your financial life inside the walls of your own house. Judge results by whether you'd be satisfied if nobody but your family could see them. Don't announce wins, don't compare to benchmarks, don't perform. The country bumpkin who quietly compounds a fortune over forty decades has exactly one financial skill, and it is the only one that matters.",
                "When: Always, and especially right after a windfall — money made quickly tends to be spent quickly and to come from luck that reverts just as fast."
            ],
            "operative": "It is working when nobody can guess your net worth from how you live, and you've stopped checking what anyone else is doing.",
            "plate": "img/action-05.png",
            "alt": "A figure with a megaphone before a cheering crowd while coins spill away, labelled Loud and crossed out; beside it a house with growing stacks of coins, labelled Quiet and checked."
        }
    ],
    "vocabulary": {
        "intro": "Most of these are pairs, and the distinction between the two halves is where the argument actually lives.",
        "terms": [
            {
                "id": "v-rich-wealthy",
                "term": "Rich vs. wealthy",
                "def": "Rich is having money in the bank to buy what you want. Wealthy is having control over what that money does to your personality, freedom, desires, and friendships."
            },
            {
                "id": "v-utility-status",
                "term": "Utility vs. status",
                "def": "Utility makes your own life better and lets you be yourself. Status changes someone else's opinion of you and requires conforming to what they want to see. Utility is durable; status expires the moment others catch up."
            },
            {
                "id": "v-social-debt",
                "term": "Social debt",
                "def": "What happens when how you spend changes what people think of you in unwanted ways — envy, obligation, lost privacy, and the higher bar you'll have to clear next time. Assets are easy to measure; this liability is not."
            },
            {
                "id": "v-contentment",
                "term": "Contentment",
                "def": "Not the absence of desire but the absence of something missing. Happiness is the gap between expectations and circumstances, so contentment is a state you can reach at any income."
            },
            {
                "id": "v-benchmark",
                "term": "Internal vs. external benchmark",
                "def": "Whether you measure yourself by how you're doing or by what others think of how you're doing. Buffett's inner and outer scorecard."
            },
            {
                "id": "v-quiet-compounding",
                "term": "Quiet compounding",
                "def": "Growing money slowly, privately, on your own terms, with no performance for anyone. Speed gets the attention; slow has the power."
            },
            {
                "id": "v-frugality-inertia",
                "term": "Frugality inertia",
                "def": "When a lifetime of good saving habits can't be switched into a reasonable spending phase, because saving has become an identity rather than a strategy."
            },
            {
                "id": "v-mental-liquidity",
                "term": "Mental liquidity",
                "def": "The ability to abandon a belief or strategy quickly when the facts or your life change. Conviction feels like a virtue, which is what makes its absence hard to spot."
            },
            {
                "id": "v-price-cost",
                "term": "Price vs. cost",
                "def": "Price is what you hand over once and can calculate. Cost is the slow drip afterward — maintenance, taxes, obligation, attention — and it usually dwarfs the price."
            }
        ]
    },
    "quickReference": [
        {
            "kind": "line",
            "label": "The question",
            "text": "Once you have money — a little or a lot — how do you actually use it to live a better life?"
        },
        {
            "kind": "line",
            "label": "The answer",
            "text": "Two ways to use money: a tool to live a better life, or a yardstick to measure yourself against others. Name which one, every time."
        },
        {
            "kind": "line",
            "label": "The equation",
            "text": "Wealth = what you have minus what you want."
        },
        {
            "kind": "line",
            "label": "The mechanism",
            "text": "Contrast, not amount. Every good is a gap."
        },
        {
            "kind": "line",
            "label": "The hidden cost",
            "text": "Social debt, envy, identity. Never on the balance sheet."
        },
        {
            "kind": "line",
            "label": "The highest return",
            "text": "Independence. There is no such thing as unspent money."
        },
        {
            "kind": "list",
            "label": "Housel's own list",
            "items": [
                "Spend less than you make.",
                "Quietly compound.",
                "Money serves you, not the other way around.",
                "No one is thinking about you as much as you are.",
                "Independence is wealth.",
                "Health is wealth.",
                "Aim to be a good ancestor.",
                "Love your family."
            ]
        }
    ],
    "closingLine": "All behavior makes sense with enough information — including yours."
}
