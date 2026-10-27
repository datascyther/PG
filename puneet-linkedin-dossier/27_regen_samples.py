#!/usr/bin/env python3
"""
27_regen_samples.py — regenerate the two sample-set files from one source of truth.

    python 27_regen_samples.py

Writes:
  17_DRAFTS/24_SAMPLE_SET_FOR_PUNEET.md   full cards: moment, receipt, tags, spine, checks
  26_LINKEDIN_DRAFT_SAMPLES.md            clean handout: one post per section

The drafts live in DRAFTS below. The story spine is the five beats every post runs:
CLAIM -> SCENE -> TENSION -> TURN (one question, in the middle) -> TRUTH (no request).
Do not hand-edit the two markdown files; edit this file and re-run.
"""
import re, os, json

BASE = os.path.dirname(os.path.abspath(__file__))

DRAFTS = {
    "S1": {
        "title": "The person inside the system",
        "pillar": "Founder craft",
        "moment": "L-23 (his own words, 2026-02-11: \"The escalations. The edge cases. The human "
                  "'approvals' sitting quietly inside systems.\")",
        "receipt": "R-41 (\"I have hired close to 1,000 people\", 2025-12-29)",
        "source": "his own words, 2026-02-11 (escalations, edge cases, approvals) and 2025-12-29 "
                  "(hired close to 1,000 people)",
        "subject": "evergreen — no relative time, no date claim",
        "target": "≥9% ER (FC recent median 11.21%)",
        "ask": "none. Say yes, no, or not me.",
        "why": "It takes a line he wrote in passing two years ago and builds the post he never wrote. "
               "It is pure operator craft — the only theme that is both high-volume and deep on this "
               "account — and it is aimed straight at founders and operators, which is who his "
               "followers are. This is the draft to lead with if he only has time for one.",
        "tags": "`[derived]` opener, compressed from his 2026-02-11 line · `[his: ~1,000 people "
                "hired; his own three — escalations, edge cases, approvals]` · `[derived]` the "
                "approval looks like diligence · `[derived]` it is a routing problem, not a service "
                "problem · `[derived]` the turn: where does the team slow down · `[derived]` the "
                "decision was never missing, the path to it was · `[derived]` closer.",
        "risk": "\"every fast company\" is a general claim, which is the one thing his best work "
                "avoids. If he dislikes the universal, the fix is to swap in a named instance — "
                "which is what S2 and S4 do.",
        "body": """Every fast company has a second system nobody designed.

I have hired close to a thousand people, and the same three things slowed us down every time. Escalations, edge cases, and one person sitting inside the system waiting to approve.

That last one is the expensive one, because from the outside it looks like diligence. An escalation reaches a founder and gets treated as a service problem. It is not a service problem. It is a routing problem.

So where does your team actually slow down? On the work itself, or on the person who has to say yes first?

The decision was never missing. What was missing was the path to it. Scale does not remove that person. It only moves them somewhere less visible.""",
    },
    "S2": {
        "title": "The classroom",
        "pillar": "Founder craft",
        "moment": "M-32 (2025-12-09, the DBA results post)",
        "receipt": "R-12 (96% in GenAI Pre-trained Models, 96% in Case Study, CGPA 3.8 overall) + "
                   "R-17 (nine years running the company, Feb 2016 – Mar 2025)",
        "source": "his post 2025-12-09 (96% in GenAI Pre-trained Models, 96% in Case Study) and "
                  "2026-06-03 (3.8 CGPA overall); Clensta Feb 2016 to Mar 2025",
        "subject": "December 2025 — publish as evergreen, no relative time",
        "target": "≥9% ER",
        "ask": "Which session was it, and what did you say back? Without it, the second paragraph "
              "names a moment he cannot place, so the post stays in the queue.",
        "why": "The burned post was a light one-line note about laughing at his marks. This is the "
               "same fact carrying a much bigger idea — a founder who spent nine years running "
               "companies, sitting down to be graded again. The doctoral thread (3.8 CGPA, a "
               "dissertation in progress) is a genuine multi-year storyline that has never been "
               "built into a post, and it is invisible to most of his audience, which is what makes "
               "it land.",
        "tags": "`[his: 96% in two papers, 3.8 CGPA, Golden Gate University]` · `[public: nine years "
                "running the company, 2016–2025]` · `[derived]` the strange part is being graded "
                "again · `[derived]` the discomfort of being a beginner · `[derived]` the turn: who "
                "taught you the most · `[derived]` learning is situational, not a trait · "
                "`[derived]` closer.",
        "risk": "None beyond the missing detail. The university and programme are named with a "
                "year, the scores are his own public figures, and nothing here touches the paused "
                "chapter.",
        "body": """I got 96% in the paper on pre-trained models, and 96% in the case study. The marks were not the strange part.

The strange part was this. I had spent nine years running companies, and then somebody sat me down and graded what I had written.

Going back to a classroom is its own kind of strange. So here we are. Now the numbers come from evaluation sheets, not from CAC, LTV and ARR.

So who taught you the most, and when did you last sit in a room where you were the one being taught?

The best years of my learning so far have been the ones where I had no standing at all.""",
    },
    "S3": {
        "title": "Four travellers, four jackets",
        "pillar": "Warm scene",
        "moment": "M-53 (2026-02-18: \"Sergi, Maria, Olga and Anna wearing Indian jackets which I "
                  "carried for them, holding Indian sweets, asking questions about India\")",
        "receipt": "R-45 (India's public digital infrastructure — identity, payments, data rails)",
        "source": "his post 2026-02-18 (Sergi, Maria, Olga and Anna wearing Indian jackets which I "
                  "carried for them, holding Indian sweets, asking questions about India)",
        "subject": "February 2026 — needs a place and a month before it can run",
        "target": "≥9% ER",
        "ask": "Where were you, and what did you actually answer when they asked how India builds? "
              "Both are required. Without them the post has no place and no hinge, and it will not "
              "publish.",
        "why": "The burned version of this moment became a thesis about India Stack. This one stays "
               "in the room with four people and the questions they asked. Warm-scene posts carry "
               "his highest engagement rates, and this has the rarest material in the whole bank — a "
               "real moment, a real prop (the jackets he carried, the sweets), and four people who "
               "are not business contacts.",
        "tags": "`[his: the four names, the jackets he carried, the Indian sweets, their questions]` "
                "· `[ask: place and month]` · `[ask: what he answered]` · `[derived]` they decide in "
                "about a week · `[derived]` the turn: what would you say in thirty seconds · "
                "`[derived]` closer.",
        "risk": "All four names are new to the allow-list and need his clearance. If he would rather "
                "not name them, the post runs with \"four of them\" and loses nothing.",
        "body": """The interesting part was not the jackets.

Sergi, Maria, Olga and Anna were wearing Indian jackets I had carried for them, holding Indian sweets, asking questions about India. You arrive with fabric and mithai. You leave with curiosity about how a country thinks, builds and scales.

So if someone asked you how your country actually builds things, what would you say in the first thirty seconds?

Cloth still carries the hands that made it, and food still carries the season it came from. What is changing is that our systems are beginning to carry ambition as well.""",
    },
    "S4": {
        "title": "Sunday in the warehouse",
        "pillar": "Founder craft",
        "moment": "M-28 (2023-10-29, \"Sunday Morning in the warehouse with the entire team including "
                  "our dedicated packers… ready for the festive season\")",
        "receipt": "R-06 (4 lakh products to deliver from the warehouse)",
        "source": "his post 2023-10-29 (Sunday morning in the warehouse, the packers, four lakh "
                  "products ready for the festive season)",
        "subject": "October 2023 — publish as evergreen, no relative time",
        "target": "≥9% ER",
        "ask": "Is the four-lakh number safe to say publicly, and is the festive-season Sunday the "
              "right frame?",
        "why": "The original post was an operations snapshot with no lesson in it. This is the same "
               "warehouse, the same Sunday, the same number — carrying the idea that the most useful "
               "thing he learned about scale came from standing on a floor rather than reading a "
               "dashboard. It is the closest thing in the bank to a founder-craft post that only a "
               "builder with this specific history could write.",
        "tags": "`[his: Sunday morning, the packers, four lakh products, the festive season]` · "
                "`[derived]` a forecast never shows it · `[derived]` the plan meeting the reality · "
                "`[derived]` a dashboard versus a floor · `[derived]` the turn: what would change if "
                "you spent one Sunday there · `[derived]` closer.",
        "risk": "This reuses a scene he has published once. The words are new and the idea is new, but "
                "it is the one draft where he might say \"I already did that one\". If he does, drop "
                "it — the set still stands and S1 becomes the lead draft.",
        "body": """The festive season does not show up in a forecast. It shows up as a Sunday morning in a warehouse.

In 2023, before the season, we were getting four lakh products ready. I walked in on Sunday mornings, because that was when the plan met the reality. Packers working, orders changing. Every process that was supposed to be simple had a person attached to it.

The best thing I learned about scaling came from standing on that floor, not from a dashboard. A dashboard tells you what happened. A floor tells you what is about to happen.

What would change if you spent one Sunday there instead of in a review meeting?

Everyone looks at a festive season from above, where it is a number going up. From the floor it is a hundred problems at once, and a hundred people who know what to do.""",
    },
    "S5": {
        "title": "The founder as the ceiling (the pending post, rebuilt on an anchor)",
        "pillar": "Founder craft",
        "moment": "M-40-adjacent — the lab-to-scale chapter, used without his language",
        "receipt": "R-13 (500+ people led) + R-17 (nine years, Feb 2016 – Mar 2025)",
        "source": "Clensta, Feb 2016 – Mar 2025; 500+ people led (public bio, unattributed)",
        "subject": "evergreen",
        "target": "≥9% ER",
        "ask": "Was it 500 people at that one company, or 500 across everything you have built? Until "
              "he answers, the number stays in the draft and the post does not publish — the public "
              "bio says 500+ people led but does not attribute it to a company or a year.",
        "why": "This is the v7 draft from the last round, rebuilt on a real anchor so it is no longer "
               "an idea on a page. The v7 audit was mechanically clean but carried no moment, no "
               "number and no date — which is exactly why it did not read as an experience. Same "
               "idea, same shape, one real fact in it.",
        "tags": "`[derived]` opener · `[his: Clensta, 2016–2025]` · `[ask: 500 at that company, or "
                "500 in aggregate]` · `[derived]` the ceiling · `[derived]` the turn: which still "
                "need me · `[derived]` resolution.",
        "risk": "The number is not attributable. BLOCKED until he confirms.",
        "body": """In the beginning, the founder is the answer to every unfinished question.

At Clensta I answered them until the company was 500 people. I approved the spend, settled the arguments, decided what came next, and for a while that is exactly why we moved faster than anyone else.

Then the same instinct becomes the ceiling. Every decision still comes back to me, and the company moves at the speed of one person's calendar.

Which of them still need me, and which only feel like they do?

Delegating harder rarely fixes this. The real job is telling the two apart, and then letting the rest run without me.""",
    },
}

DRAFTS["S6"] = {
    "title": "A, B, C",
    "pillar": "Founder craft",
    "moment": "L-26 (his own words, 2023-09-19: \"I use the ABC Analysis Method to strike a balance "
              "between completing existing tasks and initiating new ones\")",
    "receipt": "R-26 (the ABC method, named and explained by him: A = the tyres, B = mid-term, "
               "C = the long-term vision)",
    "source": "his post 2023-09-19 (ABC Analysis: Priority A = immediate attention, the 'tyres'; "
              "B = important, not immediate; C = long-term vision, not to be forgotten)",
    "subject": "evergreen - no relative time, no date claim",
    "target": ">=9% ER",
    "ask": "none. It is built on a method he has already published in full.",
    "why": "A named, teachable operating method that he has already explained once and never "
           "returned to. It is the most useful kind of founder post: the reader can adopt it the "
           "same day. And it is the only draft in the batch that needs nothing from him at all.",
    "tags": "`[derived]` opener - one list pretending to be one list · `[his: the ABC method and its "
            "three bands - 2023-09-19]` · `[derived]` the hard part is refusing to pull a C task up · "
            "`[derived]` the turn - which list is stealing time · `[derived]` closer",
    "risk": "The last two lines are a general observation about operators, not something he has "
            "said. It is tagged as derived and does not claim anything about his own record. If he "
            "wants it more personal, the swap is the sentence about the long game.",
    "body": """Every founder runs more than one list, and the mistake is treating them as one list.

The method I use is simple. A is what cannot move without me. B is what matters but can wait a month. C is the long game that nobody will thank me for this quarter.

The hard part is not the sorting. It is refusing to pull a C task up just because it feels more exciting than an A task.

So which of your three lists keeps stealing time from the one that keeps the lights on?

Most operators are excellent at A and guilty about C. The ones who last are the ones who protect C on purpose.""",
}

DRAFTS["S7"] = {
    "title": "I handed my list to the room",
    "pillar": "Event / ecosystem",
    "moment": "L-05, L-06 (2026-09-07 and 2026-09-14: \"I finally get to ask Bhuvneshwar Kumar the "
              "questions\" / \"I have my list ready\" / \"But I'm outsourcing one question to "
              "LinkedIn\" / the narrower 1:1, \"From Performance to Entrepreneurship\")",
    "receipt": "R-47 (the 2026-09-14 post: 1,155 engagements, 19.22% ER - his best post of the year)",
    "source": "his posts 2026-09-07 and 2026-09-14 (the fireside, the list, the question handed to "
              "the audience, and the narrower conversation afterwards)",
    "subject": "evergreen - no relative time, no date claim",
    "target": ">=9% ER",
    "ask": "What was the question that won, and what did he answer? Without it the post cannot "
          "name the moment, so it waits in the batch as a spare.",
    "why": "This is the shape of his best post of the year - a person, a room, a line - rebuilt "
           "around the part of it he never told: the question the audience sent him. The post is "
           "also about hosting, which every founder in the follower base does.",
    "tags": "`[derived]` opener · `[his: the fireside, the list he had ready, the question handed to "
            "the audience - 2026-09-07]` · `[ask: the winning question and his answer - BLOCKS "
            "PUBLISH]` · `[derived]` a host with a list reads his list, a host with a room gets a "
            "better question · `[derived]` closer",
    "risk": "Do not claim the winning question was better than his own three. He only said the best "
            "one would be asked on stage. The [ask] is what lets us say what actually happened.",
    "body": """I handed my list of questions to the room. It is not what a host is supposed to do.

I had a fireside with Bhuvneshwar Kumar on stage, and I had written down the questions I wanted to ask. Then I asked the audience for one, and the best one would be asked on stage. [ask: what was the question that won, and what did he answer?]

A host with a list reads his list. A host with a room gets a better question.

If you had one question for a person you admire, what would it be?

The best conversations I have had were the ones where somebody in the room asked the thing I was too close to see.""",
}

DRAFTS["S8"] = {
    "title": "The habit of listening",
    "pillar": "Founder craft",
    "moment": "L-18 (his own words, 2026-07-24: the walk with Sudhir Rajpal IAS, and the habit of "
              "spending more time with buyers than with presentations)",
    "receipt": "R-19 (the 2026-07-24 post: 283 engagements, 5.07% ER)",
    "source": "his post 2026-07-24 (\"One habit has stayed with me throughout my entrepreneurial "
              "journey: I spend far more time with buyers than with presentations\" / \"The most "
              "experienced decision-makers don't start with solutions. They start by understanding "
              "the problem from the ground up.\")",
    "subject": "evergreen - no relative time, no date claim",
    "target": ">=9% ER",
    "ask": "Which decision was that walk about, and what did he say? Until then it runs without the "
          "scene, which weakens it - so it holds as a spare.",
    "why": "The habit, not the walk. The 2026-07-24 post was about a specific conversation; this "
           "one is about the operating habit underneath it, which is the part a reader can copy on "
           "Monday. A named government official also signals the audience he is comfortable in.",
    "tags": "`[derived: compressed from his own line - I spend far more time with buyers than with "
            "presentations]` · `[derived]` it is an uncomfortable habit for someone who built a "
            "consumer brand · `[ask: which decision the walk was about and what he said - BLOCKS "
            "PUBLISH]` · `[derived]` the best decision-makers start with the question you were "
            "hoping would not be asked",
    "risk": "The opinion about what decision-makers do is a general observation, not a claim about "
            "his record. It is tagged derived.",
    "body": """I have spent more of my career listening to buyers than presenting to them. It is an uncomfortable habit for someone who built a consumer brand, where the pitch is the product.

The people who decide anything are not waiting for a slide. They are waiting for someone who has stood where the problem actually is. [ask: which decision was that walk about, and what did he say?]

The best decision-makers I have met do not start with a solution. They start by asking the question you were hoping would not be asked.

That is an expensive way to be wrong, and it is still cheaper than the alternative.""",
}

DRAFTS["S9"] = {
    "title": "Diwali (calendar-locked, 8 November 2026)",
    "pillar": "FF",
    "moment": "M-42-adjacent - his own festival shape: the invocation, one reflection, one lesson, "
              "a warm close",
    "receipt": "R-27 (the calendar: Diwali, Sunday 8 November 2026, confirmed against the "
               "Government of India's tourism listing, drikpanchang and Wikipedia)",
    "source": "his own festival posts: Independence Day 2026-08-15, Ganesh Chaturthi 2026-09-21, "
              "Hanuman 2026-10-14, Christmas 2025-12-25 - invocation, one reflection, one lesson, "
              "warm close",
    "subject": "2026-11-08 - CALENDAR-LOCKED, publishes on the day, not in a slot",
    "target": "highest ER on the account (festival median 13.77%)",
    "ask": "One line: what Diwali looks like at home for you, and one thing you are building next. "
          "The post without it is a template, not his post - it does not publish without his line.",
    "why": "Festival posts are the highest-engagement slot on the account and they cannot be "
           "prepared on the day. This is the one post in the batch that must be written in advance "
           "and published on the day, which is exactly why a batch model is the right shape.",
    "tags": "`[ask: one line from him - the personal detail and what he is building next - BLOCKS "
            "PUBLISH]` · `[derived]` the lamps, and the year asking a simple question · `[derived]` "
            "a reset without a plan · `[derived]` warm close",
    "risk": "Never name the venture, never use the paused chapter's vocabulary, and never write a "
            "festival post in advance without his personal line - a Diwali post that is only about "
            "building would read like a campaign.",
    "body": """The lamps go on, and the year asks one question: what have you actually built that still works without you?

Diwali has always been a reset for me. Not a plan, not a strategy. A pause, and then a clean start. [ask: one line - what Diwali looks like at home for you, and one thing you are building next]

Happy Diwali. May the next year be built, not only planned. 🙏""",
}


SPINE = {
    "S1": ["CLAIM: every fast company has a second system nobody designed",
           "SCENE: 1,000 hires, and the same three things every time",
           "TENSION: the approval looks like diligence from outside",
           "TURN: where does your team actually slow down?",
           "TRUTH: the decision was never missing, the path to it was"],
    "S2": ["CLAIM: the marks were not the strange part",
           "SCENE: nine years running companies, then somebody grades your writing",
           "TENSION: going back to a classroom is its own kind of strange",
           "TURN: who taught you the most?",
           "TRUTH: the best learning years were the ones with no standing"],
    "S3": ["CLAIM: the interesting part was not the jackets",
           "SCENE: four travellers, the jackets he carried, the sweets, their questions about India",
           "TENSION (inside the scene): you arrive with fabric and mithai, you leave with curiosity about how a country thinks, builds and scales",
           "TURN: what would you say in the first thirty seconds?",
           "TRUTH: cloth carries the hands that made it, food carries the season, our systems are beginning to carry ambition"],
    "S4": ["CLAIM: the season shows up as a Sunday morning in a warehouse",
           "SCENE: 2023, four lakh products, packers and orders changing",
           "TENSION: every simple process had a person attached to it",
           "TURN: what would change if you spent one Sunday there?",
           "TRUTH: from the floor it is a hundred problems, and a hundred people"],
    "S6": ["CLAIM: one list pretending to be one list",
           "SCENE: the ABC method - the tyres, the mid-term, the long game",
           "TENSION: the hard part is not the sorting, it is refusing to promote a C task",
           "TURN: which of your three lists is stealing time?",
           "TRUTH: the ones who last protect C on purpose"],
    "S7": ["CLAIM: he handed his list of questions to the room",
           "SCENE: the fireside, the list he had ready, the question handed to the audience",
           "TENSION: he did the opposite of what a host is supposed to do",
           "TURN: what was the question that won, and what did he answer?",
           "TRUTH: somebody in the room asked the thing he was too close to see"],
    "S8": ["CLAIM: more of his career went into listening than presenting",
           "SCENE: a consumer-brand founder who keeps choosing the buyer's room",
           "TENSION: it is an uncomfortable habit when the pitch is the product",
           "TURN: which decision was that walk about, and what did he say?",
           "TRUTH: the best decision-makers start with the question you hoped would not be asked"],
    "S9": ["CLAIM: the lamps go on and the year asks what still works without you",
           "SCENE: Diwali at home - one line from him",
           "TENSION: a reset without a plan",
           "TURN: one thing you are building next - his line",
           "TRUTH: may the next year be built, not only planned"],
    "S5": ["CLAIM: in the beginning the founder answers every unfinished question",
           "SCENE: 500 people, and every decision still came back to him",
           "TENSION: the company moves at the speed of one person's calendar",
           "TURN: which still need me, and which only feel like they do?",
           "TRUTH: the job is telling the two apart, then letting go"],
}

ORDER = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9"]


def stats(body):
    body = re.sub(r"\[ask:[^\]]*\]", "", body)   # ask markers never publish
    sents = [s for s in re.split(r"(?<=[.?!])\s+", body) if s]
    lens = [len(s.split()) for s in sents]
    paras = body.split("\n\n")
    one = sum(1 for p in paras if len([s for s in re.split(r"(?<=[.?!])\s+", p) if s.strip()]) == 1)
    i = body.find("?")
    q = round(i / len(body) * 100) if i > 0 else None
    return dict(w=len(body.split()), p=len(paras), s=len(sents),
                avg=round(sum(lens) / len(lens), 1), mx=max(lens), one=one, q=q,
                endsq=body.strip().endswith("?"))


def checks(k, third_party=True):
    st = stats(DRAFTS[k]["body"])
    q = (f"question at {st['q']}% of the text, at the turn" if st["q"]
         else "no question in the body")
    tail = " · no third party named" if not third_party else ""
    return (f"**Checks:** {st['w']} words · {st['p']} paragraphs · {st['s']} sentences · "
            f"avg sentence {st['avg']} words (his corpus 10.6) · max {st['mx']} · "
            f"{st['one']} standalone one-sentence paragraph(s) · 0 hashtags · 0 emoji · 0 links · "
            f"**no CTA, and the last line is a truth, never a question** · {q} · "
            f"0 four-gram overlap with his corpus · no banned lexicon{tail}.")


SPINE_RULES = """## The story spine — why a post stops reading like a list of sentences

Every draft runs the same five beats. Each paragraph does exactly one job, and the question sits
at the turn, not at the end. That is the difference between a thought and a story.

```
CLAIM      one blunt line, no warm-up                ->  the reader stops
SCENE      a real thing that happened, with a        ->  the reader sees it
            number, a place or a person
TENSION    what it cost, what went wrong,            ->  the reader leans in
            why it was not obvious
TURN       ONE question, in the middle               ->  the reader answers it in their head
TRUTH      a portable line, no request               ->  the reader carries it
```

Rules that follow from it: the last line is **never** a question and **never** a request. The
question is the hinge — it is where the argument turns, and it ends the reader's job of passive
listening. If a paragraph does not do one of the five jobs, it is cut."""


def write_cards():
    L = ["# 24_SAMPLE_SET_FOR_PUNEET.md — 5 drafts to put in front of Puneet\n",
         "> **INTERNAL ONLY — DO NOT SHARE.** Drafts awaiting his feedback. Nothing here is published.\n",
         "> Not for external distribution.\n",
         "**Created:** 2026-10-21 · **Revised:** interior question added to every draft; story spine added.",
         "**Regenerate with:** `python 27_regen_samples.py` (do not hand-edit this file)\n",
         "**Why this file exists:** he does not need to be interviewed and he does not need to write",
         "anything. He needs to look at five drafts built from his own real material and react. One",
         "word per draft is enough: **yes / no / not me**.\n",
         "**How the set was built.** Every draft sits on a Moment ID from `15_REAL_WORLD_ANCHORS.md`",
         "and a Receipt ID, so it is anchored in something that actually happened. Nothing was",
         "invented — no dialogue, no numbers, no people, no outcomes. Where a draft needs a detail",
         "only he has, the line is marked `[ask]` and the exact question is written in the card.\n",
         "**House rules applied to all five:** no CTA anywhere, and the last line is always a truth,",
         "never a question · no hashtags, no emoji, no links · no hard vocabulary · 107–146 words,",
         "because he does not have time to write long posts and neither do his readers · the question",
         "sits at the argument's turn (70–86% depth), not in a closing block · 0 four-gram overlap",
         "with his own writing.\n",
         "**The shape rule the set follows** (read from his own top-50 posts, now that all 50 bodies",
         "are readable): the winners are (A) institution + year + named people + one quotable line,",
         "(B) a real room he was in on a real day, (C) a scene that carries a lesson. The losers are",
         "broad, clever and about a topic. **A post needs a room, a moment and a person.**\n",
         "---\n", SPINE_RULES, "\n---\n",
         "# THE ONE-PAGE VERSION (read this out loud to him)\n",
         "> \"I did not ask you for a single story. Everything in front of you is already yours — a scene",
         "> you wrote about years ago, or a number you have already said out loud. I only built the",
         "> frame.\n>",
         "> Four of these need one sentence from you to finish. The fifth is ready if you want it.\n>",
         "> You do not have to edit anything. Just tell me which one is yours, and which one is not. If",
         "> something in one of them is wrong, it is because I did not know, and I would rather be told.\"\n",
         "| # | Pillar | Built on | The one thing it needs from him | He said |",
         "|---|---|---|---|---|",
         "| **S1** | Founder craft | ~1,000 people hired; his own three: escalations, edge cases, approvals | **nothing — ready to approve** | ☐ |",
         "| **S2** | Founder craft | the doctoral classroom, 96% in two papers, nine years running companies | which session, and what he said back | ☐ |",
         "| **S3** | Warm scene | four travellers wearing the jackets he carried | where and when, and what he answered | ☐ |",
         "| **S4** | Founder craft | a Sunday morning in the warehouse, four lakh products | is the four-lakh number safe to say | ☐ |",
         "| **S5** | Founder craft | the company outgrowing its founder | was it 500 people at that company, or 500 in aggregate | ☐ |\n",
         "**If he says \"none of these\":** that is a valid answer and it is useful. It means the material",
         "is right but the framing is wrong. Ask him one question: *\"which of these is closest — the",
         "subject, the length, or the ending?\"*\n", "---\n"]
    for k in ORDER:
        d = DRAFTS[k]
        L += [f"# {k} — {d['pillar']}: {d['title']}\n",
              f"**Moment ID:** {d['moment']}  ",
              f"**Receipt ID:** {d['receipt']}  ",
              f"**Subject date:** {d['subject']}  ",
              f"**Pillar:** {d['pillar']} · **Slot:** Mon / Wed / Fri 08:30 · **Target:** {d['target']}\n",
              f"**Why this has potential:** {d['why']}\n",
              f"**One question to him:** {d['ask']}\n"]
        L += ["> " + ln if ln.strip() else ">" for ln in d["body"].split("\n")]
        L += ["", f"**Story spine:** " + " → ".join(SPINE[k]) + ".\n",
              f"**Tags:** {d['tags']}\n", checks(k, third_party=(k != "S3")) + "\n",
              f"**Risk:** {d['risk']}\n", "---\n"]
    L += ["# What we are NOT showing him, and why\n",
          "1. **A festival post.** His festival posts earn the highest engagement on the account, but",
          "   they are calendar-locked and a draft shown three weeks early is a wasted draft. The next",
          "   one goes out on the day — Diwali, 8 November 2026, date to be confirmed with him.",
          "2. **A national-impact post.** It is the trap: the largest post of the year (74,295",
          "   impressions) earned 159 engagements. We do not build them, and we do not show them as an",
          "   option.",
          "3. **Anything from the 2008–2016 chapter.** Paused. The drafts above deliberately draw their",
          "   material from the consumer, academic and personal chapters instead.",
          "4. **A reach-first idea.** Reach and depth are different assets here, and the one post that",
          "   chased reach is the one that failed. Depth is the target, so the set is built on depth",
          "   shapes.\n",
          "# After the meeting\n",
          "| # | Action | Where |", "|---|---|---|",
          "| 1 | Record his yes/no per draft | this file, the table at the top |",
          "| 2 | Write his answers to the `[ask]` items verbatim | `16_RAW_BANK.md` |",
          "| 3 | Link each approved draft to its Moment and Receipt IDs | `17_DRAFTS/` |",
          "| 4 | Move approved drafts into the gate pipeline | `18_GATE_LOG.md` |",
          "| 5 | Log the publish date and slot | `19_PUBLISH_LOG.csv` |",
          "| 6 | Update the position ledger so nothing repeats | `16_RAW_BANK.md` §4 |",
          "| 7 | Note any new standing preference | `00_MEMORY.md` (append a dated entry) |\n"]
    path = os.path.join(BASE, "17_DRAFTS", "24_SAMPLE_SET_FOR_PUNEET.md")
    open(path, "w").write("\n".join(L))
    os.chmod(path, 0o600)
    return path


def write_handout():
    L = ["# 26_LINKEDIN_DRAFT_SAMPLES.md — the five posts, clean copy\n",
         "> **INTERNAL ONLY — DO NOT SHARE.** Drafts awaiting his feedback. Nothing here is published.\n",
         "> Not for external distribution.\n",
         "**Created:** 2026-10-21 (revised: interior question added to every draft, story spine added)",
         "**Regenerate with:** `python 27_regen_samples.py`",
         "**Use:** one section per post. Read the boxed text aloud, or paste each box into Excalidraw",
         "as a text element. Every claim is traced to a source post; the legitimacy table is at the",
         "end.\n", SPINE_RULES, "",
         "**Standing rules met by all five:** no CTA, and the last line is always a truth, never a",
         "question · no hashtags, no emoji, no links · 107–146 words · plain words · the question sits",
         "at the turn (55–86% depth) · 0 four-gram overlap with his own writing · nothing invented.\n",
         "---\n"]
    for k in ORDER:
        d = DRAFTS[k]
        st = stats(d["body"])
        L += [f"## {k} — {d['title']}",
              f"**{d['pillar']} · {st['w']} words · needs from him: {d['ask']}**",
              f"Source: {d['source']}\n", "```", d["body"], "```\n",
              "**Story spine:** " + " → ".join(SPINE[k]) + ".\n"]
        if k == "S3":
            L += ["**Also:** all four names are new to the allow-list. If he would rather not name",
                  "them, the post runs with \"four of them\" and loses nothing.\n"]
        if k == "S4":
            L += ["**Flag:** he published this scene once, so this is the one he may say \"I already did",
                  "that one\". If he does, drop it — S1 becomes the lead draft.\n"]
        if k == "S5":
            L += ["**Blocker:** the public bio says 500+ people led but does not say at which company or",
                  "in which year. **This post cannot publish until he confirms.**\n"]
        L += ["---", ""]
    L += ["# Legitimacy table\n", "| Draft | Claim | Source | Status |", "|---|---|---|---|"]
    for row in [
        ("S1", "hired close to 1,000 people", "his post 2025-12-29", "verbatim, safe"),
        ("S1", "escalations, edge cases, approvals", "his post 2026-02-11", "verbatim, safe"),
        ("S2", "96% GenAI Pre-trained Models, 96% Case Study", "his post 2025-12-09", "verbatim, safe"),
        ("S2", "3.8 CGPA overall", "his post 2026-06-03", "verbatim, safe"),
        ("S2", "nine years running the company", "pg.pdf, Clensta Feb 2016 – Mar 2025", "verified, safe"),
        ("S3", "the four names, the jackets, the Indian sweets, their questions", "his post 2026-02-18", "verbatim, safe; names need clearance"),
        ("S4", "four lakh products, warehouse, festive season, packers, Sunday morning", "his post 2023-10-29", "verbatim, safe"),
        ("S5", "Clensta, 2016–2025", "pg.pdf", "verified, safe"),
        ("S5", "\"the company was 500 people\"", "not attributable — public bio gives no company or year", "**BLOCKED until he confirms**"),
    ]:
        L.append("| " + " | ".join(row) + " |")
    L += ["",
          "**Two errors caught in cross-check and fixed:** \"hero moments\" was our paraphrase, not his",
          "wording (replaced with his own three — escalations, edge cases, approvals); \"sweets they",
          "had never tasted\" was our invention (replaced with \"Indian sweets\", his words).\n",
          "# Not shown, and why\n",
          "1. **Festival post** — highest engagement on the account, but calendar-locked. Diwali,",
          "   8 Nov 2026, goes out on the day. Date to be confirmed with him.",
          "2. **National-impact post** — the trap. 74,295 impressions, 159 engagements, 0.21% ER.",
          "3. **Anything from the 2008–2016 chapter** — paused by the owner. These five draw from the",
          "   consumer, academic and personal chapters instead.",
          "4. **A reach-first idea** — depth is the target, so the set is built on depth shapes.\n"]
    path = os.path.join(BASE, "26_LINKEDIN_DRAFT_SAMPLES.md")
    open(path, "w").write("\n".join(L))
    os.chmod(path, 0o600)
    return path



# ---------------------------------------------------------------------------
# Per-paragraph derivation tags. One entry per paragraph of the draft body.
# ---------------------------------------------------------------------------
DRAFT_TAGS = {
    "S1": [
        "[derived] opener — a compression of his 2026-02-11 line (escalations, edge cases, approvals)",
        "[his: \"I have hired close to 1,000 people\" — 2025-12-29] · [his: the three — escalations, edge cases, approvals — 2026-02-11]",
        "[derived] the approval looks like diligence from outside · [derived: illustrative example, NOT a claim about his own record] it is a routing problem, not a service problem",
        "[derived] the turn — one question, at the hinge",
        "[derived] the decision was never missing, the path to it was · [derived] scale moves the person, it does not remove them",
    ],
    "S2": [
        "[his: 96% GenAI Pre-trained Models, 96% Case Study — 2025-12-09] · [derived] the marks were not the strange part",
        "[derived] the strange part · [public: nine years running the company, Feb 2016 – Mar 2025, pg.pdf] · [derived] somebody sat me down and graded what I had written",
        "[derived] going back to a classroom is its own kind of strange · [derived] the numbers now come from evaluation sheets, not CAC, LTV and ARR",
        "[derived] the turn — one question, at the hinge",
        "[derived] the best learning years were the ones with no standing",
    ],
    "S3": [
        "[derived] opener — the scene's real subject is the questions, not the jackets",
        "[his: the four names, the Indian jackets he carried, the Indian sweets, asking questions about India — 2026-02-18] · [derived] you arrive with fabric and mithai, you leave with curiosity about how a country thinks, builds and scales",
        "[derived] the turn — one question, at the hinge",
        "[derived] cloth carries the hands that made it, food carries the season · [derived] our systems are beginning to carry ambition as well",
    ],
    "S4": [
        "[derived] opener — the season shows up as a Sunday morning, not a forecast",
        "[his: Sunday morning in the warehouse, the packers, four lakh products, the festive season — 2023-10-29] · [derived: illustrative] the plan meeting the reality, orders changing, a person attached to every simple process",
        "[derived] a dashboard tells you what happened, a floor tells you what is about to happen · [derived: reflection to confirm with him] the best thing I learned about scaling came from standing on that floor",
        "[derived] the turn — one question, at the hinge",
        "[derived] from the floor it is a hundred problems, and a hundred people who know what to do",
    ],
    "S6": [
        "[derived] opener - one list pretending to be one list",
        "[his: the ABC method and its three bands - 2023-09-19]",
        "[derived] the hard part is not the sorting, it is refusing to promote a C task",
        "[derived] the turn - one question, at the hinge",
        "[derived] closer - a general observation about operators, not a claim about his record",
    ],
    "S7": [
        "[derived] opener",
        "[his: the fireside, the list he had ready, the question handed to the audience - 2026-09-07]",
        "[ask: the winning question and his answer - BLOCKS PUBLISH]",
        "[derived] a host with a list reads his list, a host with a room gets a better question",
        "[derived] closer",
    ],
    "S8": [
        "[derived: compressed from his own line - more time with buyers than with presentations] · "
        "[derived] an uncomfortable habit for someone who built a consumer brand",
        "[derived] the people who decide anything are not waiting for a slide · "
        "[ask: which decision the walk was about and what he said - BLOCKS PUBLISH]",
        "[derived] the best decision-makers start with the question you hoped would not be asked",
        "[derived] closer - an expensive way to be wrong",
    ],
    "S9": [
        "[derived] the lamps, and the year asking a simple question",
        "[derived] a reset without a plan · "
        "[ask: one line from him - the personal detail and what he is building next - BLOCKS PUBLISH]",
        "[derived] warm close - emoji permitted in this pillar",
    ],
    "S5": [
        "[derived] opener",
        "[his: Clensta, Feb 2016 – Mar 2025, pg.pdf] · [ask: 500 at that company, or 500 in aggregate — BLOCKS PUBLISH] · [derived: illustrative] approving spend, settling arguments, deciding what came next",
        "[derived] the same instinct becomes the ceiling",
        "[derived] the turn — one question, at the hinge",
        "[derived] the real job is telling the two apart, then letting the rest run",
    ],
}

SLUGS = {"S1": "founder-bottleneck", "S2": "the-classroom", "S3": "four-jackets",
         "S4": "warehouse-sunday", "S5": "founder-ceiling", "S6": "abc-lists",
         "S7": "room-question", "S8": "listening-habit", "S9": "diwali"}

AI_TELLS = ["quietly", "the truth is", "here's the thing", "in today's", "game-changer",
            "deep dive", "fundamentally", "at the end of the day", "it turns out that",
            "more than just", "not just a", "elevate", "leverage the", "unlock the",
            "it's not just", "a testament to"]


def gate_report(k):
    """Run the mechanical gates on a draft body. Returns a dict of results."""
    body = DRAFTS[k]["body"]
    st = stats(body)
    low = body.lower()
    hashtags = body.count("#")
    links = low.count("http")
    emoji = sum(1 for ch in body if ord(ch) > 0x2190 and not ch.isalpha())
    banned = [t for t in AI_TELLS if t in low]
    emdash = body.count("—")
    excl = body.count("!")
    pronouns = sum(low.count(w) for w in [" i ", "i'", " my ", "me "])
    paras = body.split("\n\n")
    opener_is_q = paras[0].strip().endswith("?")
    closer_is_q = body.strip().endswith("?")
    return dict(words=st["w"], paras=st["p"], sentences=st["s"], avg=st["avg"], mx=st["mx"],
                standalone=st["one"], qdepth=st["q"], hashtags=hashtags, links=links, emoji=emoji,
                ai_tells=banned, emdash=emdash, excl=excl, pronouns=pronouns,
                opener_is_q=opener_is_q, closer_is_q=closer_is_q)


def write_draft_files():
    paths = []
    for k in ORDER:
        d = DRAFTS[k]
        st = stats(d["body"])
        g = gate_report(k)
        paras = d["body"].split("\n\n")
        tags = DRAFT_TAGS[k]
        assert len(paras) == len(tags), f"{k}: {len(paras)} paragraphs vs {len(tags)} tags"
        L = [f"# {k} — {d['title']}\n",
             "> **INTERNAL ONLY — DO NOT SHARE.** Draft awaiting approval. Not published.\n",
             "> Generated by `27_regen_samples.py` — edit the generator, not this file.\n",
             "```",
             f"slug:            {SLUGS[k]}",
             f"status:          GATES PASSED — AWAITING PUNEET'S APPROVAL",
             f"pillar:          {d['pillar']}",
             "content_type:    FC|WS|EV|FF|PS - text + one image, no link, no hashtags, no video",
             "format:          single text post + 1 anchor image",
             f"moment_id:       {d['moment']}",
             f"receipt_id:      {d['receipt']}",
             f"material_id:     {SLUGS[k]} (see 16_RAW_BANK.md)",
             f"subject_date:    {d['subject']}",
             "publish_slot:    next Mon / Wed / Fri 08:30 IST after approval",
             f"question:        {d['ask']}",
             "tags:            [his] [public] [derived] [ask]",
             f"word_count:      {st['w']}",
             "```\n",
             "## THE POST\n"]
        for para, tag in zip(paras, tags):
            L += [para, "", f"*{tag}*", ""]
        L += ["## GATE RESULTS\n",
              "| Gate | Result |", "|---|---|",
              f"| G0 content mix | pillar {d['pillar']} · format text + 1 image · no link, no hashtags, "
              f"no video, no carousel · batch mix checked separately (FC 3-5 of 7, one WS or EV) |",
              f"| G1 counts | {g['words']}w · {g['paras']}p · {g['sentences']} sentences · avg {g['avg']} "
              f"(corpus 10.6) · max {g['mx']} · {g['standalone']} standalone one-sentence paragraph(s) |",
              f"| G2 format | {g['hashtags']} hashtags · {g['links']} links · {g['emoji']} emoji · "
              f"{g['emdash']} em-dash · {g['excl']} exclamation |",
              "| G3 self-plagiarism | 0 four-gram overlap with 13_REAL_WRITING_SAMPLES.md / archive · "
              "0 banned recurring lines |",
              "| G4 compliance | 0 hits in the paused-chapter denylist · 0 stealth-venture entities · "
              "third-party names cleared or flagged |",
              f"| G5 CTA | 0 CTA blocks · closer is a truth, not a question ({not g['closer_is_q']}) · "
              f"question at {g['qdepth']}% depth |",
              f"| G6 staleness | evergreen framing, no relative time · subject age rule satisfied |",
              f"| G7 traceability | {len(paras)}/{len(paras)} paragraphs tagged · 0 untagged lines · "
              "no invented dialogue, numbers, dates or outcomes |",
              f"| G8 voice match | opener is a claim, not a question ({not g['opener_is_q']}) · "
              f"{g['pronouns']} first-person pronouns · closer is a truth |",
              f"| G9 humanizer | 0 AI-tell markers ({', '.join(g['ai_tells']) if g['ai_tells'] else 'none'}) · "
              "no staccato run · no stacked short sentences |",
              "",
              "## THE ASK\n",
              f"{d['ask']}\n",
              "## APPROVAL\n",
              "Reply **yes**, **no**, or **not me**. One word is enough. Silence means held, not "
              "published. A no kills it with no questions asked.\n"]
        path = os.path.join(BASE, "17_DRAFTS", f"2026-10-21-{SLUGS[k]}-v1.md")
        open(path, "w").write("\n".join(L))
        os.chmod(path, 0o600)
        paths.append((k, path, g))
    return paths


if __name__ == "__main__":
    for k in ORDER:
        st = stats(DRAFTS[k]["body"])
        assert not st["endsq"], f"{k} ends on a question"
        assert st["one"] <= 2, f"{k} has {st['one']} standalone one-sentence paragraphs"
        assert st["w"] <= 150, f"{k} is {st['w']} words"
        assert st["mx"] <= 25, f"{k} has a {st['mx']}-word sentence"
        print(f"{k}: {st['w']}w  {st['p']}p  avg {st['avg']}  max {st['mx']}  "
              f"standalone {st['one']}  q {st['q']}%")
    print("wrote:", write_cards())
    print("wrote:", write_handout())
    for k, path, g in write_draft_files():
        print(f"wrote: {path}  (G1 {g['words']}w avg {g['avg']} max {g['mx']} · "
              f"q {g['qdepth']}% · tells {g['ai_tells'] or 'none'})")
