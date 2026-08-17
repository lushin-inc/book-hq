"""Content module — the durable artifact.

The page, the PDF and the docx all read from this. None of them hardcode
content, which is what makes a rebuild a re-render.

The Insights + Action Guide PDF is still produced and still ships in the
folder — it just is not linked from the page.
"""

BOOK = {
    "title": "Chop Wood Carry Water",
    "author": "Joshua Medcalf",
    "subtitle": "How to Fall in Love with the Process of Becoming Great",
    "cover": "img/cover.png",
    "links": [
        {
            "mark": "↓",
            "label": "Spoken companion",
            "href": "Chop Wood Carry Water - Spoken Companion.docx"
        }
    ],
    "insights": [
        {
            "id": "insight-1",
            "title": "You Are Always Building Your Own House",
            "lede": [
                "Every day you are producing two things: the work, and the person doing the work. The work gets handed over, forgotten, or lost. The person is the only permanent output. Treat any assignment as something you are doing for someone else and you will quietly lower the standard, because the cost of lowering it seems to land on them."
            ],
            "operative": "Before you cut a corner, ask who actually receives the cut. The answer is always the same person.",
            "plate": "img/insight-01.png",
            "evidence": "Kota built the finest houses in Tokyo for thirty years, hand-selecting every material. Asked to build one last house before retiring, he agreed with his head but not his heart — he delegated, details slipped, the house passed code and nothing more. When he finished, his boss handed him a small box with the keys inside. It was his house. It had been his the whole time."
        },
        {
            "id": "insight-2",
            "title": "With One Eye on the Goal, You Only Have One Eye for the Journey",
            "lede": [
                "Attention is not additive. Whatever you give the outcome comes out of the process, and the process is the only place the skill is actually built. A related trap: treating situations as tests. If it is a test, you optimize for passing it. If it is an opportunity, you optimize for what you take out of it. Over years those two people end up in different places."
            ],
            "operative": "Judge your day by whether you did the work well, not by where the work left you on the scoreboard.",
            "plate": "img/insight-02.png",
            "evidence": "John asks how long it will take to become a samurai archer. Ten years. And if he skips chopping wood and carrying water? Twenty. And if he gives every waking moment to archery alone? Thirty. Ice climbers who stare at the summit cannot see where to put a foot; they slip and they die."
        },
        {
            "id": "insight-3",
            "title": "Your Value Comes From Who You Are, Not From What You Do",
            "lede": [
                "When identity is fused to performance, every result becomes a verdict on your worth — which inflates you when things go well, flattens you when they don't, and quietly corrupts your decisions, because now every choice is also a defense of your value. The fix is to locate identity in something that cannot be taken away in a moment."
            ],
            "operative": "Answer the question now, in writing, while nothing has been taken away — because the day it is taken away is the worst day to start looking.",
            "plate": "img/insight-03.png",
            "evidence": "John overtrains, tears his shoulder, and is put out of action for six to eight weeks. Akira asks him: you cannot shoot, you cannot chop wood or carry water — so who are you? John has no answer. Akira's own: I am not a samurai archer; I am a human being who happens to be world class at archery."
        },
        {
            "id": "insight-4",
            "title": "Achievement Is Salt Water",
            "lede": [
                "Achievement does not fill the hole people expect it to fill; it enlarges the thirst. If what you have accomplished so far has not done the job, more of it will not do the job either. The society-issued scorecard — win more, earn more, be seen more — is not a hard scorecard to top. It is an impossible one, which is a different problem entirely."
            ],
            "operative": "You need a scorecard of your own, made of characteristics rather than results, and you need to actually grade yourself on it.",
            "plate": "img/insight-04.png",
            "evidence": "Kobe Bryant says a sixth title will satisfy him and let him retire. Andre Agassi, after reaching number one in the world: “I thought that getting to number one was going to be the moment I made sense of my life. But it left me a little empty, and I spiraled down.”"
        },
        {
            "id": "insight-5",
            "title": "Growth Happens Underground Long Before It Happens in the Air",
            "lede": [
                "Mastery moves in steps, not constants — long flat plateaus broken by sudden jumps. Feeling stuck is therefore not evidence of being stuck; it is the normal texture of the middle. And the invisible years are not wasted time before the growth. They are the structure that lets the growth hold."
            ],
            "operative": "Measure the watering, not the height, and do not read a plateau as a verdict.",
            "plate": "img/insight-05.png",
            "evidence": "Plant bamboo in good soil and water it faithfully and you see nothing for roughly five years — while underground a dense mat of roots spreads out to carry weight that does not yet exist. Then it comes up ninety feet in six weeks. Height without roots is the story of people who arrive at success and cannot hold it."
        },
        {
            "id": "insight-6",
            "title": "Surrender the Outcome",
            "lede": [
                "Partially controllable goals — winning, sales, someone else's record — are alluring and dangerous, because pursuing them hard enough leaves a wake regardless of whether you arrive. Reaching the goal makes the wake easier to justify. It does not make it smaller. Surrender is not indifference; it is removing the one thing that makes you tight, forces your hand, and keeps you out of the moment."
            ],
            "operative": "Name what you actually control, commit everything to it, and let the rest go before it costs you the people standing next to you.",
            "plate": "img/insight-06.png",
            "evidence": "Akira drives all day through Croatian mountains to reach a waterfall, snapping at the woman he loves, ignoring her when she says she only wants to spend the day with him, ignoring locals who warn him off the trail — and finally, in the dark and the rain, having sent her back down with strangers, he turns around without ever seeing it."
        }
    ],
    "actions": [
        {
            "id": "action-1",
            "title": "Build Your Own Scorecard",
            "lede": [
                "List the people you genuinely admire and the characteristics they embodied that you would want to be known for. Narrow it to the four that matter most. Grade yourself on those four twice a day.",
                "When: Set it up once. Grade at midday and again at night — midday so you still have an evening to correct what is slipping."
            ],
            "operative": "Any situation, including a bad one, becomes a place to move a number you chose yourself rather than one the world assigned you.",
            "plate": "img/action-01.png",
            "caveat": "Four, not eight. A scorecard you cannot hold in your head is a list, not a scorecard."
        },
        {
            "id": "action-2",
            "title": "Keep a What Went Well Journal",
            "lede": [
                "Write a worth statement at the top — my value comes from who I am, not from what I do — then a growth statement: anything that happens to me today is in my best interest and an opportunity to learn and grow. Then fifteen specific things you did well. Then, and only then, two areas for growth and two things you learned.",
                "When: After every training session, performance, or working day."
            ],
            "operative": "Fifteen stops being hard. You start noticing good repetitions while they are happening rather than reconstructing them at night.",
            "plate": "img/action-02.png",
            "caveat": "Two growth areas, never more — nobody can hold more than two in mind the next day. If you quit short of fifteen, beat yesterday's stopping point by two."
        },
        {
            "id": "action-3",
            "title": "Carry Your Principles in Your Pocket",
            "lede": [
                "Each morning, before the work starts, write out four to six principles you will hold to no matter what. Fold the paper and put it in your pocket.",
                "When: Daily, and especially on days you can already feel your mood making decisions for you."
            ],
            "operative": "When feelings surge, you touch the pocket or read the list aloud, and the decision is already made.",
            "plate": "img/action-03.png",
            "caveat": "Borrow principles that have been tested for a long time rather than inventing clever ones. You will still slip; the practice is getting back on the road, not never leaving it."
        },
        {
            "id": "action-4",
            "title": "Set Your Warrior Dial Before You Perform",
            "lede": [
                "Notice where your activation sits on a one-to-ten scale, decide where it needs to be for this particular task, and move it deliberately. Down: slow breathing, slower speech, lower voice, slower movement, calm music. Up: upbeat music, movement, anything that fires you.",
                "When: In the minutes before anything that requires precision — and before the games that feel too big, which is exactly when everyone overshoots."
            ],
            "operative": "You arrive at the line at your number instead of whatever number the occasion handed you.",
            "plate": "img/action-04.png",
            "caveat": "Turning the dial down is much harder than turning it up, and most training cultures only ever practice up."
        },
        {
            "id": "action-5",
            "title": "Take the Two-Minute Gratefulness Walk",
            "lede": [
                "Walk for two minutes naming everything you are grateful for, with deliberate attention on the things you normally take for granted.",
                "When: Immediately after a loss, a bad session, or any moment you notice perspective has gone."
            ],
            "operative": "You can feel the shift inside two minutes — and you are markedly easier to be around for the people who have to live with your result.",
            "plate": "img/action-05.png",
            "caveat": "It works as a reset, not as a substitute for the reckoning. Do the walk, then have the honest conversation about what went wrong."
        }
    ]
}
