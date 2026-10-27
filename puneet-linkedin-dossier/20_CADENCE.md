# 20_CADENCE.md — The posting system

> **INTERNAL ONLY — DO NOT SHARE.** Operating file for the manager. Not for external distribution.

**Created:** 2026-10-21
**Purpose:** one page that a second operator could follow to run a week without asking a single
question. The gates are written down, not remembered.

---

## 1. The shape of a week

| When | What | Who | Output |
|---|---|---|---|
| Daily 07:45 IST | One capture prompt on WhatsApp | Manager → Puneet | his line, voice note or "nothing today" |
| Daily, within 4 hrs | Ingest + anchor test | Manager | a row in `16_RAW_BANK.md` |
| Daily 12:00 IST | Draft v1 from the day's material | Drafter | a draft in `17_DRAFTS/` with tags |
| Daily 16:00 IST | Gates G1–G6 | Drafter | gate log rows |
| Daily 17:00 IST | Gates G7–G9 | Manager | gate log rows |
| Daily 18:00 IST | Approval request to Puneet (only for a draft that has passed the gates) | Manager | a preview + a one-word reply request |
| Publish day, 05:30 IST | Staleness sweep, publish-date lock | Manager | publish log row locked |
| Publish day, 08:30 IST | Publish + screenshot | Manager | live post + screenshot into `19_PUBLISH_LOG.csv` |
| Publish day +72 hrs | Measurement freeze | Manager | 72-hour metrics in the log |
| Publish day +7 days | Final read | Manager | 7-day metrics appended |
| Monday 09:30 IST | Weekly review, 30 min | Manager | one change for the coming week |
| First Monday of the month, 10:00 | Monthly review, 60 min | Manager (+ 5-min async note to Puneet) | pillar re-ranking, festival calendar refresh |

---

## 2. Publish slots

**Mon 08:30 · Wed 08:30 · Fri 08:30 IST.** Three per week. Skip a slot without apology.

**Why these days** (from the native analytics export, `14_AUDIENCE_MAPPING.md` and the top-50
post set):

| Weekday | Median ER, top-50 posts | Median daily ER, post-2026-07-18 | Verdict |
|---|---|---|---|
| **Monday** | **11.12%** (n=9) | **9.74%** | strongest on both measures |
| Friday | 9.88% (n=5) | 1.71% | strong post-level, weak daily — mixed |
| Tuesday | 5.08% (n=8) | 3.84% | middle |
| Wednesday | 3.59% (n=14) | 8.65% | mixed |
| Sunday | 2.95% (n=2) | 1.01% | weak |
| Thursday | 1.62% (n=6) | 2.36% | weak |
| Saturday | 1.56% (n=6) | 1.85% | weak |

Monday is the only weekday that is strong on **both** measures. Thursday, Saturday and Sunday are
weak on both and are avoided. **08:30 IST is a house default, not a finding** — the export contains
no post timestamps, so no time-of-day claim can be made. Do not churn the time without evidence.

**Festival posts publish on the festival day**, whatever weekday it falls on. **Event promos
publish T-3 to T-1** before the event. Those two are calendar-bound and override the slot rule.

---

## 3. Volume and pillar mix

**3 posts per week.** Standing permission to publish 2. Never 4. Never a filler week.

| Code | Pillar | Per week | Use it when | Never when |
|---|---|---|---|---|
| **FC** | Founder craft / operator lessons | **2** | the material holds a decision, a number, a person, a customer-facing moment, a failure, or a process he changed | — (a week with 0 FC is a failed week) |
| **WS** | Warm scene / place / travel / hobby | 0–1 | a place, trip, sport, photo or small human moment happened in the last 7 days | the scene has no lesson attached and you would have to invent one |
| **EV** | Event / ecosystem | 0–1 | he is actually speaking, moderating or present | he is not there |
| **FF** | Festival / faith | 0–1 per fortnight | the festival is on the calendar (highest ER on the account, 13.77%) | the occasion is commercial |
| **PS** | Personal / origin | ≤1 per 14 days | a genuine milestone, or an origin story not used in 6+ months | it rehashes the office-wall or selection-setback stories |
| **IE** | India / ecosystem / policy | **0 scheduled** | opportunistically only, where the account has a real point of view | it is being published to buy reach — IE is a reach instrument and reach is not the target |

**The weekly rule, in one line:** two FC + one rotating slot, where the rotating slot is FF if a
festival falls in the week, else EV if he is on stage, else WS. FC may take all three slots if the
week produces three good ones. The mix is a default, not a quota.

---

## 4. Capture protocol

**One prompt per day, 07:45 IST, WhatsApp, one message, no follow-up question, no chase.**

> Send me one thing from today — what happened, where, and what it made you think. Voice note is
> fine. "Nothing today" is also fine.

**7-day prompt rotation** (designed to force a *scene*, not an opinion):

| Day | Theme | Prompt |
|---|---|---|
| Mon | Scene | "One moment from today. Where were you, and what happened?" |
| Tue | Number / fact | "One number, one fact, or one thing someone said this week that you are still thinking about." |
| Wed | Change | "One thing you are doing differently now than a year ago. One line, and why." |
| Thu | Mistake | "One thing that did not work — a call, a hire, a plan, a conversation. One sentence." |
| Fri | Operator | "One thing a founder would get wrong if they only heard your version." |
| Sat | Catch-all | "Anything from the week you'd actually write about. One line or a voice note. 'Nothing' is fine." |
| Sun | Personal | "One thing from your own life this week — a place, a habit, a person, a moment." |

Friday and Sunday are the only two that skew personal, and they sit there deliberately: the rest of
the week must produce founder craft.

**His time budget:** ≤60 seconds a day + one 20-minute meeting a week. Nothing else. No draft is
ever sent to him for editing. No comment threads requiring replies. If he says he is travelling or
blocked, the prompt queue skips him; it does not accumulate.

---

## 5. The three publish tracks

| Track | Applies to | Rule |
|---|---|---|
| **Default — 48–72 hrs** | FC, WS, PS | Capture D0 → draft D0/D1 → gates D1 → approval D1 → publish on the next slot. Realistic lag is 2–3 days because approval is explicit, not automatic. |
| **Countdown — T-3 → T-1** | EV promos | Publish no later than the day before the event. A promo on the event morning is wasted. |
| **Calendar-locked** | FF | Publish on the day. Drafted at D-7. **Diwali: 8 Nov 2026 — confirm with Puneet.** |

**Post-approval rule:** the approval reply arrives, then the publish date is the next slot whose
subject-age check still passes. A draft that waits more than 7 days past its subject date is
reframed as evergreen or dropped — **never published late without reframing.**

---

## 6. The staleness rules (the hold does not solve these on its own)

1. **Subject age ≤ 7 days.** Subject date = when the thing actually happened, not when it was
   captured. Recorded at ingest in `16_RAW_BANK.md`.
2. **Past 7 days → exactly two options.** *Reframe as evergreen* — strip every relative time
   reference and rebuild as an operator lesson with the same anchor; or *kill*. If the subject has
   been overtaken by news, kill it and return the material to the bank.
3. **Relative language rots inside a hold.** Draft in absolute time by default ("On 14 October",
   "In 2024"). Relative language is added only if the post publishes the same day the thing
   happened — which with an explicit approval cycle is almost never. A sweep at T-3 hrs scans for
   "this morning", "today", "yesterday", "last week", "two days back", "recently" and re-anchors
   anything that no longer reads true on the publish date.
4. **Event wraps publish within 48 hrs of the event.** A miss means refactor to evergreen or drop.

---

## 7. If news breaks before a draft publishes

Decided by the manager at T-3 hrs, without asking Puneet:

1. **The news makes the draft wrong or incomplete** → kill it. Do not rewrite around it; a
   late draft responding to a fresh event reads as late. Return the material to the bank.
2. **The news makes it more urgent but not wrong** → do not chase it. Reach-optimising is a trap.
   Publish as drafted.
3. **A better subject just landed** → kill the slot. A better anchor beats a finished draft. Budget
   one missed slot a week.

---

## 8. Approval model (owner decision, 2026-10-21)

**Nothing is published without Puneet's explicit yes.** There is no silent-publishing tier.

| Level | Content | What happens |
|---|---|---|
| **A** | Founder craft, warm scene, personal, festival | Preview sent. If he replies "yes" (or a correction), it publishes in the next slot. Silence = held, never auto-published |
| **B** | Anything with a number, any name outside the allow-list, event promos and wraps | Same. Silence = held |
| **C** | Current venture, board and investment roles, awards claims, anything from the paused chapter, another party's business | **Explicit yes required. Silence = do not publish.** After 24 hrs it waits for the next week, it does not publish and it does not die |

**His verbs are: capture, answer, yes, no.** He never edits, never redlines, never sees a redline.
**One word kills any post at any time, no explanation and no penalty.** Say this out loud to him —
a painless veto is what makes silence worth waiting for.

**Batching, because silence is the default:** the weekly 20-minute meeting *is* the approval
session. Three drafts on one screen, three one-word replies. Everything outside the meeting gets an
individual approval request with a 24-hour deadline.

---

## 9. Weekly review — Monday, 30 minutes, manager only

1. **Scoreboard (10 min):** last week's posts — ER at 72 hrs against the post-2026-07-18 pillar
   benchmarks (FC 11.21%, FF 13.77%, EV 10.22%, IE 11.74%; overall band 10–14%); impressions
   against the 4,659 median; comments; follower-day delta. **Hit line: 9% ER.**
2. **Material conversion (5 min):** captured → drafted → published. Bank depth. Below 10 usable
   items, act: seed evergreen posts from `15_REAL_WORLD_ANCHORS.md` §2 and shift a slot to WS or FF.
3. **One change, not five (5 min):** exactly one adjustment for the coming week — a pillar swap, a
   prompt-theme swap, or a slot time. Multiple simultaneous changes make the week uninterpretable.
4. **Position ledger (5 min):** which positions are now exhausted, which material is at risk of
   duplication.
5. **Compliance log (5 min):** any G4 near-miss this week. Record it.

---

## 10. Monthly review — first Monday, 60 minutes

1. Re-rank pillars on the trailing 28 days only, minimum 8 posts per pillar before concluding.
   Compare against the post-2026-07-18 benchmarks, not the 4.30% annual figure.
2. Read the top two posts side by side and name what they share — that becomes next month's prompt
   emphasis. Read the bottom two and name the failure mode (opener shape, subject age, missing
   anchor, wrong pillar, wrong slot).
3. Refresh the festival and milestone calendar for the next 90 days with Puneet.
4. Sample engager quality on the top two posts (job titles and company sizes). If a high-ER post
   attracts only enterprise-IT employees, it is a reach post in disguise and the pillar label is
   wrong.
5. **Erosion check:** read the month's best draft and the best corpus sample blind. If they are
   indistinguishable, the pipeline has drifted toward the manager's voice — fix by asking Puneet
   one more factual question per draft.

---

## 12. The batch model — how to run this without his daily time

**The problem:** a daily capture + daily approval model needs him every day. He is busy, and a
prompt he fails is a prompt he stops answering.

**The resolution:** we prepare two weeks of posts in advance and he approves the whole batch in one
20-minute meeting. His touchpoint drops from three times a week to **once every two weeks**, and
each touchpoint is a form, not a review.

| | Per-post model | **Batch model (adopted)** |
|---|---|---|
| His touchpoints | 3 per week | **1 per fortnight** |
| His work per touchpoint | approve 1 post | **approve 6-7 posts, one word each** |
| Material needed from him | daily, or nothing to publish | **none — the bank has 30 unspent live moments** |
| Capture frequency | daily prompt | **weekly Saturday catch-all + one live demo per meeting** |
| Staleness risk | low | **handled: batch posts are evergreen by construction** |

**Why it is safe.** The 7-day subject-age rule is a rule for posts built from a *fresh* event. A
batch post is drawn from the archive and written in absolute time, so it carries no relative time
and no dated event — that is what makes it eligible for a fortnight of advance approval. Fresh
material from a capture joins the **next** batch, never the current one. The rule survives: a post
built from something that happened this week is never pre-approved.

**Approval rules inside a batch**
- Every post still needs **its own explicit yes**. A batch is not a blanket approval.
- Silence on a post = held, not published. Silence on the whole batch = the batch waits.
- A batch approval is valid for **its own dates only**. A missed post is re-offered in the next
  batch, it does not publish late.
- One word kills any post in the batch, with no explanation and no penalty.
- If two slots in a batch have no approved post, they are skipped without apology.

### Batch A — the first fortnight (approval meeting → publishing 26 Oct to 8 Nov)

| Publish | Slot | Draft | Words | What it needs from him |
|---|---|---|---|---|
| Mon 26 Oct | 08:30 | **S1** the person inside the system | 126 | nothing — ready on a yes |
| Wed 28 Oct | 08:30 | **S6** A, B, C | 116 | nothing |
| Fri 30 Oct | 08:30 | **S4** Sunday in the warehouse | 146 | one yes/no: is the four-lakh number safe to say |
| Mon 2 Nov | 08:30 | **S2** the classroom | 115 | one fact: which session, what he said back |
| Wed 4 Nov | 08:30 | **S3** four travellers, four jackets | 97 | one fact + the four names cleared |
| Fri 6 Nov | 08:30 | **S7** I handed my list to the room | 109 | one fact: the winning question |
| **Sun 8 Nov** | **on the day** | **S9** Diwali | 72 | one fact: what Diwali looks like at home, and what he is building next |

**Spares, already drafted and ready if a slot falls:** S8 the listening habit (109 words, one
fact) · S5 the founder as the ceiling (107 words, blocked until the 500 attribution is confirmed).

**If the meeting slips past Friday 23 Oct:** drop Monday 26 October and start the batch on
Wednesday 28 October. The batch compresses, it does not break.

**Batch B** is assembled from the next LIVE moments in the bank (L-05, L-11, L-14, L-16, L-20,
L-22, L-23, L-26, L-31) plus anything he sends in the weekly capture, and is taken to the meeting
after Batch A publishes.

## 12b. Content type — what each post IS (full system: `28_CONTENT_TYPES.md`)

**Pillars (subject):** 4 FC + 1 WS + 1 EV + 1 FF per two-week batch. IE is never scheduled. A
skipped slot beats a weak post.
**Formats (shape):** one format only — text plus one anchor image. No link in the body (the 3
top-50 posts with links average 0.98% ER against 7.24% for the 47 without). No hashtags (1 in the
last 20 posts). No video, no carousel (0 of 50).
**Surfaces (where he shows up):** the post · **the comment** (reply to every substantive comment
on his own posts within 24 hours, plus 3–5 comments a week on other people's posts — the only
surface that produces depth without producing another post) · the profile (one Featured slot per
approved post, plus his 7 unused articles) · the DM (log every one; recurring questions become the
next batch's material).

**Batch A content mix:** S1 FC · S6 FC · S4 FC · S2 FC · S3 WS · S7 EV · S9 FF = 4 FC + 1 WS +
1 EV + 1 FF. On target. S7 was reclassified from FC to EV — it is a fireside, not a lesson, and
five FC in seven would have read like a lecture series.

## 13. The launch plan (from 2026-10-21)

**Week 0 — now.** Five drafts are written, gated and waiting. Files:
`17_DRAFTS/2026-10-21-<slug>-v1.md` (one per post, with per-paragraph tags and the gate
results), `17_DRAFTS/24_SAMPLE_SET_FOR_PUNEET.md` (the cards), `26_LINKEDIN_DRAFT_SAMPLES.md`
(the clean handout), `23_ASK_SHEET.md` (what we ask him, cross-checked). The generator
`27_regen_samples.py` is the single source of truth for all four and re-asserts the house rules on
every run.

**The meeting.** 20 minutes, one slot a week. Eight answers: three name/attribution questions
(ask sheet §1) and five decisions only he can make (§2). Everything else is already cleared from
his own public record (§3) and must **not** be read out to him.

**Order of publishing once he says yes** — first slot wins, so the best post goes first:

| Order | Draft | Words | Slot | Condition |
|---|---|---|---|---|
| 1 | S1 founder-bottleneck | 126 | first Mon/Wed/Fri 08:30 | ready on a yes, no answer needed |
| 2 | S2 the-classroom | 115 | next slot | needs: which session, what he said back |
| 3 | S3 four-jackets | 97 | next slot | needs: where and when, what he answered + the four names cleared |
| 4 | S4 warehouse-sunday | 146 | next slot | needs: is the four-lakh number safe to say |
| 5 | S5 founder-ceiling | 107 | next slot | **blocked** until the 500 attribution is confirmed |

**Week 1 — the rhythm starts.** One capture prompt at 07:45 IST from day one. Bank floor is 10:
RB-101 to RB-110 are already READY and sourced, so the pipeline does not wait on him. Every
capture adds to the bank; every approved post is logged in `19_PUBLISH_LOG.csv` with a screenshot.

**Diwali.** Sunday 8 November 2026 — confirmed against the Government of India's tourism listing,
drikpanchang and Wikipedia. It falls on a Sunday, so the festival post is **calendar-locked and
publishes on the day**, not in a slot, and the subject-age rule does not apply to it. The draft is
written at D-7 (1 November). This is historically his highest-ER post type (13.77% median) and
needs his confirmation of the date and any family ritual that belongs in it.

**Week 2 onwards.** The position ledger (`16_RAW_BANK.md` §4) enforces a 30-day cooldown per
position. The Friday review makes exactly one change a week. Skip a slot without apology.

## 14. Day-1 checklist

1. ~~Confirm the festival calendar for the next 90 days with Puneet, including 8 Nov 2026.~~ Diwali
   = **Sunday 8 November 2026**, independently confirmed. Confirm only the 90-day window and his
   own milestones.
2. ~~Create the pipeline files.~~ Done: `15`–`23` and `27_regen_samples.py` exist; the bank holds 10
   READY rows; `19_PUBLISH_LOG.csv` is open; `21_COMPLIANCE.md` §4a is pre-cleared and only §4b/§4c
   need him.
3. Decide the publish path: a scheduler, or a single 15-minute manual paste window at 08:15 with a
   mandatory post-publish screenshot. **A post with no screenshot is treated as unpublished.**
4. Run the 20-minute meeting — use **`23_ASK_SHEET.md`** (the cross-checked version), not the
   original meeting card. Land the three name/attribution answers and the five decisions.
5. ~~Seed the bank so week 1 does not open with a drought.~~ Done: RB-101 to RB-110.
6. ~~Update `04_SOURCES.md`.~~ Done — the native analytics export is now a used source, and the
   external press sources are logged.
7. Send the first daily prompt and verify on day 3 that it produced usable material. If two
   consecutive prompts produce unusable material, **rewrite the prompt — do not ask harder.**
8. After his yes: re-run the gates on the edited draft, sweep for stale relative time 3 hours
   before publish, paste, screenshot, log.
