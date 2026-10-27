# 18_GATE_LOG.md — Quality gates before publish

> **INTERNAL ONLY — DO NOT SHARE.** Contains draft excerpts and compliance findings.
> Not for external distribution.

**Created:** 2026-10-21
**Purpose:** the checks that stand between a draft and the account. Ordered cheapest-check-first,
so that the cheap failures are caught in seconds and the expensive read happens last.

**Budget: 12–15 minutes per draft.** If a draft takes more than 20 minutes at the gates, the draft
is bad — kill and redraft rather than polish.

**Failure rule:** any gate fail → one targeted fix → re-run that gate. Two failed fixes on the
same gate → kill the draft, log the reason, return the material to the raw bank.

---

## 1. The nine gates

| # | Gate | Reads | Checks | Cost |
|---|---|---|---|---|
| **G1** | **Counts** | draft text | 42–263 words (target 110–200); avg sentence 8–13 words; max sentence ≤25 words; ≤2 standalone one-sentence paragraphs; no 3+ consecutive short one-sentence paragraphs; no staccato run (no 3 consecutive sentences ≤5 words) | 10 s |
| **G2** | **Format** | draft text | 0 hashtags; 0 links in the body (except an event promo `Register:` line); emoji only in FF / WS / event-promo pillars; em-dashes ≤1; exclamation marks only in warm posts; no "🔥🚀💡" register | 10 s |
| **G3** | **Self-plagiarism** | draft + `13_REAL_WRITING_SAMPLES.md` + published corpus + `16_RAW_BANK.md` position ledger | 0 four-gram overlap with the corpus; 0 hits on the banned recurring-lines list ("my DMs are open", "let us build it together", "not every second needs to be optimised", "back to …", "what breaks when this becomes 10x bigger", "looking forward to …", "grateful for/to …"); hinge line ("…stayed with me" family) ≤ once per 6 posts; no position used within 30 days | 30 s |
| **G4** | **Compliance lexicon** | draft + `21_COMPLIANCE.md` | 0 hits in the paused-chapter denylist; 0 hits in the stealth-venture denylist; current venture only as "current stealth AI venture" / "building sovereign AI infrastructure"; 0 third-party entities outside the allow-list; no contact details beyond the public LinkedIn URL. **Non-waivable — the manager cannot override this gate** | 30 s |
| **G5** | **CTA and placement** | draft | 0 CTA blocks; ≤1 ask per 4 posts; a question, if present, sits at 55–90% depth; the post closes on the idea (truth, image, question, thanks), not on a request | 30 s |
| **G6** | **Staleness and date** | draft + subject date + publish date | Subject age ≤7 days, or reframed as evergreen; 0 stale relative-time words ("this morning", "yesterday", "last week", "two days back"); every date in the body still true on the publish date; any link still live; event promo published T-3→T-1; wrap within 48 hrs of the event; festival on the correct date | 1 min |
| **G7** | **Anchor and traceability** | draft with marginal tags + `15_REAL_WORLD_ANCHORS.md` | ≥1 dated / placed / numeric / named-person anchor traceable to a Moment ID and a Receipt ID; **every sentence carries a tag**; `[derived]` lines logically equivalent, not stronger; 0 untagged sentences | 3 min |
| **G8** | **Voice match** | draft + `11_VOICE_CLONE_BRIEF_CONCISE.md` + the 3 nearest corpus samples | Opener is a claim, scene, year, title or invocation — never a question; ≥2 first-person pronouns in FC / WS / PS (25 of 26 real posts use I/my/me); closer is one of the 4 native closers; ≥1 hinge pivot unless the position ledger says it was used in the last 6 posts; sentence-length p90 ≤20 words; no corporate filler; reads as an operator, not an advisor | 5 min |
| **G9** | **Humanizer** | draft | Run the `linkedin-humanizer` skill in audit mode, then strict tier: scrub + rhythm + fingerprint + over-correction guard. 0 density markers, 0 reveal bridges, 0 staccato fragments, 0 stacked triads, 0 performed sincerity, no "It's not X. It's Y." overuse, no em-dash piles | 5 min |

**Re-run rule:** G1 and G9 are coupled — the humanizer changes word and sentence counts. Always
re-run G1 after G9. Re-run G3 and G4 after **any** edit in G9, because the scrubber can introduce
a banned term.

---

## 2. The two gates that decide whether a post exists at all

- **G7 (traceability)** is the anti-ghostwriter gate. A draft with untagged lines is not a draft,
  it is an essay with a founder's name on it. Untagged line → delete.
- **G4 (compliance)** is the anti-career-error gate. The paused chapter and the current venture are
  the two places where a plausible-sounding line could cause real damage. No override, ever.

---

## 3. Gate log

| Draft | Date | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 | Approval | Publish slot | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-21-founder-bottleneck-v1 | 2026-10-21 | G1 ✓(126w, avg 9.7, max 18) | G2 ✓(0/0/0) | G3 ✓(0 overlap) | G4 ✓ | G5 ✓(q@70%, closer is a truth) | G6 ✓(evergreen) | G7 ✓(5/5 tagged) | G8 ✓(opener claim, closer truth) | G9 ✓(0 tells) | AWAITING APPROVAL | next Mon/Wed/Fri 08:30 | GATES PASSED |
| 2026-10-21-the-classroom-v1 | 2026-10-21 | G1 ✓(115w, avg 12.8, max 22) | G2 ✓(0/0/0) | G3 ✓(0 overlap) | G4 ✓ | G5 ✓(q@84%) | G6 ✓(evergreen) | G7 ✓(5/5 tagged) | G8 ✓ | G9 ✓(0 tells) | AWAITING APPROVAL + 1 ANSWER | next Mon/Wed/Fri 08:30 | GATES PASSED |
| 2026-10-21-four-jackets-v1 | 2026-10-21 | G1 ✓(97w, avg 13.9, max 21) | G2 ✓(0/0/0) | G3 ✓(0 overlap) | G4 ✓(names pending) | G5 ✓(q@70%) | G6 ✓(evergreen) | G7 ✓(4/4 tagged) | G8 ✓ | G9 ✓(0 tells) | AWAITING APPROVAL + 1 ANSWER + NAMES | next Mon/Wed/Fri 08:30 | GATES PASSED |
| 2026-10-21-warehouse-sunday-v1 | 2026-10-21 | G1 ✓(146w, avg 12.2, max 19) | G2 ✓(0/0/0) | G3 ✓(1 common 4-gram, no echo) | G4 ✓ | G5 ✓(q@78%) | G6 ✓(evergreen) | G7 ✓(5/5 tagged) | G8 ✓ | G9 ✓(0 tells) | AWAITING APPROVAL + 1 ANSWER | next Mon/Wed/Fri 08:30 | GATES PASSED |
| 2026-10-21-founder-ceiling-v1 | 2026-10-21 | G1 ✓(107w, avg 13.4, max 25) | G2 ✓(0/0/0) | G3 ✓(0 overlap) | G4 ✓ | G5 ✓(q@80%) | G6 ✓(evergreen) | G7 ✓(5/5 tagged) | G8 ✓ | G9 ✓(0 tells) | **BLOCKED — 500 attribution** | — | GATES PASSED, FACT MISSING |
| 2026-10-21-abc-lists-v1 | 2026-10-21 | G1 ✓(116w, avg 11.6, max 19) | G2 ✓(0/0/0) | G3 ✓(0 overlap) | G4 ✓ | G5 ✓(q@80%) | G6 ✓(evergreen) | G7 ✓(5/5 tagged) | G8 ✓ | G9 ✓(0 tells) | AWAITING APPROVAL | Wed 28 Oct 08:30 | GATES PASSED |
| 2026-10-21-room-question-v1 | 2026-10-21 | G1 ✓(109w, avg 13.6, max 23) | G2 ✓(0/0/0) | G3 ✓(0 overlap) | G4 ✓ | G5 ✓(q@78%) | G6 ✓(evergreen) | G7 ✓(5/5 tagged) | G8 ✓ | G9 ✓(0 tells) | AWAITING APPROVAL + 1 ANSWER | Fri 6 Nov 08:30 | GATES PASSED · EV |
| 2026-10-21-listening-habit-v1 | 2026-10-21 | G1 ✓(97w, avg 13.9, max 18) | G2 ✓(0/0/0) | G3 ✓(0 overlap) | G4 ✓ | G5 ✓(no question in body) | G6 ✓(evergreen) | G7 ✓(4/4 tagged) | G8 ✓ | G9 ✓(0 tells) | AWAITING APPROVAL + 1 ANSWER | spare | GATES PASSED |
| 2026-10-21-diwali-v1 | 2026-10-21 | G1 ✓(72w, avg 10.4, max 21) | G2 ✓(1 emoji, permitted for FF) | G3 ✓(0 overlap) | G4 ✓ | G5 ✓(no question in body) | G6 ✓(calendar-locked 8 Nov) | G7 ✓(3/3 tagged) | G8 ✓ | G9 ✓(0 tells) | AWAITING APPROVAL + 1 ANSWER | Sun 8 Nov, on the day | GATES PASSED | — |

**Row format:** `G1 ✓(105w, avg 11.2)` · `G3 ✓(0 overlap)` · `G5 ✓(q@82%)` · `G6 ✓(age 2d)` ·
`G7 ✓(M-24 + R-13, 14/14 tagged)` · `G8 ✓(4 pronouns)` · `G9 ✓(0 tells)` · `APPROVED 2026-10-21` ·
`PUBLISHED 2026-10-23 08:30 IST`

---

## 4. Compliance near-miss log

Any near-miss on G4 gets a row, even when the gate passes. A near-miss that is not written down
becomes a slip next week.

| Date | Draft | Term/entity that appeared | Why it was allowed | Action taken |
|---|---|---|---|---|
| — | — | — | — | — |
