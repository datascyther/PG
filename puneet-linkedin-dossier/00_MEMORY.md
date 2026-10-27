# 00 — AUTO-LEARN MEMORY (owner rules & preferences)

> READ THIS FIRST, EVERY CONVERSATION, BEFORE ANY OTHER ACTION.
> This is the persistent, append-only memory for the Puneet LinkedIn dossier work.
> It records hard rules and preferences the owner has stated. Rules here override
> defaults and override anything in older notes when they conflict.

## How this works

- This file is the single source of truth for the owner's standing rules.
- It is loaded automatically at the start of every conversation. The mechanism is:
  `/Users/mymac/.config/opencode/AGENTS.md` carries a directive telling the agent to
  read this file first, and `/Users/mymac/.config/opencode/opencode.jsonc` lists this
  file in its `instructions` array so its contents are injected into context on every
  session. `~/.config/opencode/AGENTS.md` is the global instructions file opencode
  loads for all sessions (verified against opencode docs — Rules / Global).
- At the START of every conversation, read this whole file before writing or editing
  anything in this dossier.
- Whenever the owner states a NEW rule or preference (e.g. "always do X", "never do
  Y", "from now on…"), APPEND a new dated entry to the LEARNED RULES log below. Do not
  rewrite or delete old entries — the log is append-only so history is preserved. If a
  new rule reverses an old one, add a new entry that says so rather than editing the old.
- Keep entries short: date, the rule, and one line of why/scope if given.

---

## LEARNED RULES (append-only)

### 2026-10-17 — Stealth discipline (current venture)

- Refer to the current venture ONLY as "current stealth AI venture" (or "building
  sovereign AI infrastructure").
- Never name any current-venture product, partner, customer, investor, competitor, or
  fund.
- No contact details beyond the public LinkedIn URL (https://www.linkedin.com/in/puneetgbuilds/).
- Historical ventures (Honeywell, TAK/DarVi, Clensta) and public institutions/awards may
  be named, but always with a year/place anchor.

### 2026-10-17 — PAUSED BY OWNER: no defence / military / national-security wording

- STOP using any defence / military / national-security language and any named military
  locations, until the owner explicitly re-enables it.
- Banned vocabulary includes: "defence", "armed forces", "military", "soldier",
  "induction", "bases", "forward post", "weapons", "national security".
- Banned place names include named military locations (e.g. Awantipora, Jammu, Tezpur,
  Tawang, Shillong).
- Describe the historical builder story generically instead (contracts, field, customers,
  deployment, technical systems).
- Status: PAUSED. Re-enable only on an explicit owner instruction.

### 2026-10-17 — No AI tells (writing rules)

- NEVER isolate a short punch line as its own paragraph (e.g. a standalone line like
  "Nobody buys a demo." or "Trust is the real go to market strategy.").
- NEVER stack 2–4 short full-stop sentences in a row (no "sentence. full stop." ladder).
- Vary sentence length WITHIN paragraphs — long carrying sentences (20–30 words) with
  short punches integrated inside the paragraph.
- Run the humanizer skill on every draft before it is considered done.

### 2026-10-17 — File protection (permissions)

- Share-safe deliverables (files 08–12) stay readable by others: mode 644.
- Internal files (01–07 plus all raw source files) are owner-only: mode 600, and must
  carry an "INTERNAL ONLY" banner.
- Keep this separation intact whenever files are created, copied, or re-synced.

### 2026-10-17 — LinkedIn skills install locations (keep in sync)

- The LinkedIn skills are installed in TWO places and both must stay current:
  - manual install: `~/.config/opencode/skills/` (references also under
    `~/.config/opencode/references/`)
  - npx install: `~/.agents/skills/` (references also under `~/.agents/references/` and
    `~/.agents/skills/linkedin-marketing/references/`)
- The filled `voice-profile.md` and `story-bank.md` must be synced to ALL reference
  locations above.
- The filled copies are owner-only: mode 600.
- After any edit, verify md5 match across all three locations.

### 2026-10-17 — Success criteria

- Output must be manager-presentable.
- It must NOT look AI-generated (no detectable AI tells).
- Use plain business language — no hype, no corporate filler.

### 2026-10-17 — REVISED: punch-line rule is now a data-matched hybrid (supersedes the strict "never isolate" rule above)

- The earlier strict rule ("never isolate a punch line as its own paragraph; never stack 2–4 short
  sentences") is SUPERSEDED by the hybrid below, which the owner chose after corpus analysis.
- Allow at most 1–2 isolated one-line punch paragraphs per post. His real average is ~1.2/post, and
  standalone one-sentence paragraphs are 55.5% of his paragraphs — so a single isolated punch line
  is native to him, not an AI tell.
- Still FORBIDDEN: a uniform wall of short one-liners; stacking 2–4 short full-stop sentences inside
  a paragraph; 3+ consecutive short one-sentence paragraphs; reusing one of his own lines verbatim
  (e.g. "trust is the real go to market strategy", Post 9 2026-07-21).
- Vary sentence length within paragraphs (mix short and long). The real AI tell is uniformity and
  density, not one isolated line.
- Corpus facts (55 posts, 416 paragraphs, 718 sentences): standalone one-sentence paras 55.5%;
  short punch-line isolations ~1.2/post across 64% of posts; stacked short-sentence runs in only 29%
  of posts (71% have none); aphoristic one-liners never exceed 2 in a row; avg sentence 11.8 words;
  full "Not X. Not Y. Not Z." triple appears in only 2 posts.

### 2026-10-17 — Clone briefs rewritten to defer to the corpus (anti-ghostwriter pass)

- `10_VOICE_CLONE_BRIEF.md`, `11_VOICE_CLONE_BRIEF_CONCISE.md`, and `08_PERSONA_ANALYSIS_STEALTH.md`
  were rewritten to match `13_REAL_WRITING_SAMPLES.md` exactly. The corpus wins over any brief.
- Removed the stale/contradictory instructions: the directive to reuse his own lines verbatim (the
  "my DMs are open. Let us build it together." and "What breaks when this becomes 10x bigger?" closes);
  the 180-280 word rule (now median ~160, range 42-262); the "20-30 word sentences" claim (now avg
  ~10.5 words, ~58% of sentences ≤10); the "opens with I / year / India" rule (now the blunt
  aphoristic claim is the default, "I" only ~1 in 5, a question NEVER opens); and the "near-zero
  emoji" claim (now 🙏 😊 😄 ❤️ 🇮🇳 and ":)" appear in warm festival/personal/event posts; none in
  serious posts).
- Anti-self-plagiarism list expanded; every quoted owner line is now labelled calibration-only.
- 08 is de-defenced and generic; defence/military wording remains only as the PAUSED rule statement.
- Permissions: 08/10/11 are share-safe (644). The briefs are now the ground-truth-aligned source.

### 2026-10-17 — REAL WRITING SAMPLES: ground-truth voice corpus + anti-self-plagiarism

- 26 verbatim owner-written posts are stored at
  `/Users/mymac/PG/puneet-linkedin-dossier/13_REAL_WRITING_SAMPLES.md` (INTERNAL ONLY,
  mode 600). It contains current-venture and partner names, named individuals, personal
  detail, and (paused) defence content: never publish it, never copy its lines verbatim
  into any draft.
- This file is the GROUND-TRUTH VOICE CORPUS — the most authentic record of how he actually
  writes and thinks. Style docs must defer to it: `voice-profile.md` and `story-bank.md`
  both now name it as the ground-truth source, and their §1 voice fingerprint / positions /
  recurring stories / receipts were enriched from it (real opener shapes, closer shapes,
  humor + emoji usage, thinking modes, argument shape).
- ANTI-SELF-PLAGIARISM (hard rule): these recurring owner lines must NEVER be reused verbatim
  in our drafts — "my DMs are open"; "what breaks when this becomes 10x bigger?";
  "Let us build it together"; "Not every second needs to be optimised"; "back to ...". Echo
  the shape and rhythm, never the words. Self-repetition is the fastest way to expose a
  ghostwriter.
- Corrections vs the earlier profile: he DOES use emoji/emoticons (🙏 😊 😄 ❤️ 🇮🇳, ":")
  in festival, birthday, gratitude and event posts (zero in serious business/board posts);
  openers are most often blunt declarative claims (questions, if any, close the post).

### 2026-10-19 — Audience mapping from the owner's LinkedIn analytics export

- New authoritative metrics source: `AggregateAnalytics_Puneet Gupta_2025-10-20_2026-10-19.xlsx`
  (LinkedIn native analytics export, owner-supplied, period 2025-10-20 to 2026-10-19). It supersedes
  live guest-fetch counts for impressions/engagement/followers. `04_SOURCES.md` still lists the native
  export under "What was NOT used" — stale, fix on the next sources pass.
- Analysis lives in `14_AUDIENCE_MAPPING.md` (INTERNAL ONLY, mode 600). It contains per-post data and
  engager demographics: never publish it.
- Standing finding: the account has TWO audiences — a founder/owner-operator follower base
  (Delhi-NCR-heavy, 40% in ≤200-person firms) and an enterprise-IT/engineering reach base
  (10,001+ firms, software engineers over-indexed 4x). Write for the first, expect distribution to the second.
- Standing finding: theme rankings must be computed on the post-2026-07-18 window only. ER moved from
  1.01% to 9.13% at that date, so full-year theme comparisons measure timing, not topic.
- Reach and depth trade off (corr. −0.31 between impressions and ER). Do not judge a post by impressions.
- CTA placement: the corpus contains a CTA in only 6 of 26 real posts (4 are event logistics), and
  questions sit at ~60-90% depth where the argument turns. Prefer moving an existing line into a
  question over appending a CTA block. This contradicts `09_MANAGER_BRIEF.md` §7 ("end every piece
  with a single call to action") — the owner's own corpus and the fold logic win.

### 2026-10-21 — LinkedIn management operating system: moments over ideas

- NEW RULE — MOMENTS OVER IDEAS: a post is built on ONE real moment (a dated scene: place, person,
  prop) + ONE verifiable receipt + the reflection. Never from an idea alone. We do not imitate his
  writing style; we reproduce his material and his shape, and the voice arrives with the material.
  The owner stated the problem directly: "we can whatever try, we couldn't match their exact writing
  style." That is why the bank, not the brief, is the source of truth.
- NEW FILE — ANCHOR BANK: `15_REAL_WORLD_ANCHORS.md` (INTERNAL, 600) holds 40 dated archived
  moments (each marked BURNED = already spent in a published post, or LIVE = unspent and expandable
  without repeating his words), ~30 LIVE one-line mentions, and 40 receipts with tiers
  (A owner-stated / B press / C profile-awards / D inference-never-publish) and flags
  (OK / PRESS-ATTRIB / ASK / PAUSED / NDA). No figure, name, place or scene may be used in a draft
  unless it is in this file with a source.
- NEW RULE — ANCHOR TEST AT INGEST: captured material must contain at least one of {place,
  date/year, number, named person, object, named decision}. If not, it is a thesis seed and may only
  be the closing argument of a scene-anchored post. His words are logged verbatim, never paraphrased.
- NEW RULE — SUBJECT-AGE RULE: publish_date − subject_date ≤ 7 days, else reframe as evergreen
  (strip relative time) or kill. The 48-72 hour hold does not fix staleness; a mechanical
  relative-language sweep at T-3 hrs does. Draft in absolute time by default.
- NEW RULE — EXPLICIT APPROVAL ONLY: nothing publishes without Puneet's explicit yes. There is NO
  silent-publishing tier at any level. Silence = held, never auto-published. His verbs are capture,
  answer, yes, no — he never edits or redlines. One word kills any post, no explanation, no penalty.
  Approval is BATCHED in the weekly 20-minute meeting (three drafts, three one-word replies).
- NEW RULE — CAPTURE PROTOCOL: one WhatsApp prompt daily at 07:45 IST, one standing sentence, voice
  note accepted, "Nothing today" is a valid answer. His time budget is ≤60 seconds/day plus one
  20-minute meeting a week. Never chase, never ask him to review a draft.
- NEW RULE — PUBLISH SLOTS: Mon / Wed / Fri 08:30 IST. Monday is the only weekday strong on both
  measures (post-level median ER 11.12%, post-2026-07-18 daily 9.74%); Thursday, Saturday and
  Sunday are weak in both. 08:30 is a house default, NOT a finding — the export has no post
  timestamps, so no time-of-day claim may ever be made. 3 posts/week (2 founder-craft + 1
  rotating); skipping a slot without apology.
- STANDING FINDING — specificity is weakly supported, not proven: posts carrying a date/place/number/
  name show 8.10% median ER vs 1.93% for those without, but the test is confounded by the
  2026-07-18 era break, 17 of 50 posts coded from URL slugs only (all pre-July), and a full-text
  control group of n=2. State it as "anchors are what his best work does", never as a causal promise.
- STANDING GAP — CLOSED 2026-10-21: all 17 body-less top-50 posts were guest-fetched (50/50 URLs,
  0 failures). Full text + impressions + engagements + ER for every ranked post is now in
  `23_TOP50_FULL_TEXT.md` (INTERNAL, 600). This produced 17 new dated moments (M-41…M-57) and 11
  new receipts (R-41…R-51) in the bank. The recovery also revealed the design lesson now recorded
  in the bank §8: the winning post shapes are (A) institution + year + named people + one quotable
  line — the best post of the period, 2026-07-22, 13.19% ER, 402 engagements; (B) a real room he
  was in on a real day — 2026-07-19, 5.07%; (C) a scene carrying a lesson — 2026-09-14, 19.22%, the
  highest-engagement post of the year. The trap is the national-impact post: 2025-12-06, 74,295
  impressions, 159 engagements, 0.21% ER. Winning posts need a room, a moment and a person — not a
  topic.
- The owner's own live corpus is now mined: `16_RAW_BANK.md` (live capture log + position ledger),
  `17_DRAFTS/TEMPLATE.md` (derivation tags [his]/[public]/[derived]/[ask] — a line with no tag is
  deleted), `18_GATE_LOG.md` (9 gates, cheapest-first, G4 non-waivable), `19_PUBLISH_LOG.csv`
  (per-post history — the native export caps at 50 posts and has no per-post history, so this log
  becomes more valuable than the export within three months), `20_CADENCE.md`, `21_COMPLIANCE.md`,
  `22_MEETING_CARD.md` (the 20-minute agenda for the meeting with Puneet).
- NEXT PASS (Pass 2, after the owner approves Pass 1): wire Moment ID + Receipt ID into
  `10`/`11` briefs and the approval card in `12`; enrich `voice-profile.md` + `story-bank.md` and
  md5-sync to all three skill install locations; add the anchor check to the `linkedin-post-writer`
  skill; write v8 of the founder-ceiling post (hard anchor "500 people", soft "nine years
  2016-2025"); fetch the 17 missing post bodies.
- 2026-10-21 — PASS 1 DELIVERED: `15`–`23` created (anchor bank, raw bank, drafts folder, gate
  log, publish log, cadence, compliance, meeting card, full-text corpus) and `10`/`11`/`12`,
  `voice-profile.md`, `story-bank.md`, `linkedin-post-writer` and `04_SOURCES.md` all wired. All 50
  top-50 post bodies recovered. **Sample set for the owner:** `17_DRAFTS/24_SAMPLE_SET_FOR_PUNEET.md`
  — 5 drafts, each on a Moment ID + Receipt ID, none published, each needing at most one factual
  answer from him. The manager's stated goal (show him samples, take his feedback) is met by that
  file, which is designed to be read aloud in one sitting.
- 2026-10-21 — capture/approval model decided by the manager: nothing publishes without an
  explicit yes (no silent publishing at any tier), approval batched in the weekly 20-minute
  meeting, slots Mon/Wed/Fri 08:30 IST, 3 posts/week, daily 07:45 WhatsApp capture prompt.
- 2026-10-21 — `25_WORKFLOW_DIAGRAMS.md`: 10 Excalidraw-ready Mermaid diagrams (system in one picture,
  weekly rhythm, anchor test, post anatomy, the five drafts and what each needs, gate ladder,
  depth-not-reach proof, "style is in the material", the story spine, and line-to-post) plus slide
  copy. **All 10 blocks validated against mermaid v11 with mermaid.parse — 0 failures.** Slide order:
  1, 2, 4, 6, 9, 3, then the five drafts (block 5).
- 2026-10-21 — NEW RULE — STORY SPINE (owner: "it looks like a random sentence, we have to master
  the strategic storytelling"). Every post runs five beats, one paragraph each: **CLAIM** (one blunt
  line) → **SCENE** (a real thing that happened, with a number, place or person) → **TENSION** (what
  it cost / what went wrong) → **TURN** (ONE question, in the middle) → **TRUTH** (a portable line,
  no request). Rules: the last line is never a question and never a request; the question is the
  hinge, not the close; if a paragraph does not do one of the five jobs, it is cut. The question
  inside the post is what stops a post reading as a list of statements.
- 2026-10-21 — `27_regen_samples.py` is now the single source of truth for the sample set; it
  regenerates `17_DRAFTS/24_SAMPLE_SET_FOR_PUNEET.md` and `26_LINKEDIN_DRAFT_SAMPLES.md` and
  asserts the house rules (no question ending, ≤2 standalone one-sentence paragraphs, ≤150 words,
  max sentence ≤25 words). Do not hand-edit those two markdown files — edit the script and re-run.
- 2026-10-21 — EXECUTION PASS 1: five individual draft files written with per-paragraph derivation
  tags and the nine gate results (`17_DRAFTS/2026-10-21-<slug>-v1.md`), gates logged in
  `18_GATE_LOG.md`, and the bank seeded with 10 READY rows (RB-101…RB-110) so week 1 does not wait
  on the owner's first capture. `23_ASK_SHEET.md` is the cross-checked ask sheet and **supersedes
  `22_MEETING_CARD.md` for the meeting** — it separates what is already cleared by the public
  record (do not ask) from the three name/attribution questions and five decisions only he can make.
- 2026-10-21 — SECOND FABRICATION SWEEP: removed "a queue outside a shop", "I had good answers for
  maybe half of it", "they decide in about a week" (S3 — none of it in his post) and "This time the
  numbers" (S2 — his exact 4-gram). S3 now says only what his 2026-02-18 post says, plus one
  marked [ask]. Lesson: the illustrative example is the danger zone, not the facts. When a line is
  a plausible general truth rather than his words, it must be tagged `[derived: illustrative]`.
- 2026-10-21 — Diwali confirmed as **Sunday 8 November 2026** (Government of India tourism
  listing, drikpanchang, Wikipedia). It is a Sunday, so the festival post is calendar-locked and
  publishes on the day, not in a Mon/Wed/Fri slot.
- 2026-10-21 — MEETING ORDER DECIDED (manager): the two asks are not alternatives. **The five
  drafts with yes / no / not me come first** (a multiple-choice ask is the lowest-friction thing
  we can put in front of him, and his pattern of answers tells us what he likes without him
  explaining it). **The daily "one real context" line is the real goal and comes last** — the
  drafts are a one-off, they do not scale, and five "not me" answers leave us with no material.
  The daily line is installed by a **live capture demo in the room**: "send me one voice note right
  now about something that happened today." If he has nothing, accept it and start the prompt
  anyway. Order: 5 drafts (5 min) → the one fact each needs (5) → three name/attribution
  questions (3) → five decisions only he can make (3) → live capture demo (2).
- 2026-10-21 — `24_WHATSAPP_TEMPLATES.md`: the five messages he will ever receive, copy-paste
  ready — daily capture (26 words), weekly meeting invite, the approval message carrying all five
  drafts with a "1, 3" reply format plus the three outstanding questions, the live capture demo,
  and the one-line held note. Design rule for all five: one message, one ask, one reply word.
- 2026-10-21 — NEW RULE — BATCH MODEL (owner: "he is very busy day to day, how do I manage it?").
  We prepare two weeks of posts in advance and he approves the whole batch in ONE 20-minute
  meeting. His touchpoint drops from 3x/week to 1x/fortnight, and each touchpoint is a form
  (reply "1, 3, 6"), not a review. **Every post in a batch still needs its own explicit yes** — a
  batch is not a blanket approval; silence = held; a one-word "no" kills one post with no penalty.
  **Material is not the bottleneck: the bank holds 30 unspent LIVE moments from his own published
  writing, so the capture prompt drops from DAILY to WEEKLY (Saturday catch-all) and any answer
  joins the NEXT batch, never the current one.** This also resolves the staleness risk: batch posts
  are evergreen by construction (absolute years, no relative time, no dated event), while the
  7-day subject-age rule still binds any post built from a fresh event — a fresh post is never
  pre-approved. Batch A: 7 posts published 26 Oct – 8 Nov, plus 2 drafted spares; if the meeting
  slips past 23 Oct, drop the 26 Oct slot and compress.
- 2026-10-21 — CONTENT TYPE DEFINED (`28_CONTENT_TYPES.md`), the gap the owner spotted. Three
  layers, not one. **PILLARS (subject):** 4 FC + 1 WS + 1 EV/FF/PS per 2-week batch; IE never
  scheduled; a skipped slot beats a weak post. **FORMATS (shape):** exactly one format works —
  text + one anchor image, no link in the body, zero hashtags, no video, no carousel. Evidence:
  0 of 50 top posts are video or document/carousel; only 3 of 50 carry a link in the body and
  those 3 median 0.98% ER against 7.24% for the 47 without; hashtags went from 23 of 35 posts
  pre-July 2026 to 1 of 20 after (the hashtag era ended with the regime break). **SURFACES (where
  he shows up):** the post + THE COMMENT (reply to every substantive comment on his own posts
  within 24 hours, plus 3-5 comments a week on other people's posts — the only surface that
  produces depth without producing another post, and it needs nothing from us) + the profile (one
  Featured slot per approved post, plus 7 unused articles) + the DM (log every one; recurring
  questions become the next batch's material). Reposting is replaced by commenting: his one
  "big congratulations" post ran 0.80% ER. S7 reclassified FC -> EV so Batch A reads 4 FC + 1 WS
  + 1 EV + 1 FF instead of five lessons in a row.
- 2026-10-21 — `28_CONTENT_TYPES.md` now carries 10 Excalidraw-ready Mermaid diagrams: the three
  layers as a fan (1) and as a stack from foundation to reader (2), one deep-dive per layer —
  pillar decision with quotas and benchmarks (3), what the post is made of (4), what his week
  looks like across the four surfaces (5) — plus the pillar mix (6), the format decision with its
  evidence (7), the four surfaces (8), the G0 mix check (9) and Batch A slot by slot (10). All 10
  validated against mermaid v11 — 0 failures. Slide order 1, 2, 3, 4, 5, 6, 7, 8, 10, 9.
- 2026-10-21 — BATCH A BUILT: 9 drafts now exist and are gated (S1 founder-bottleneck 126w,
  S2 the-classroom 115w, S3 four-jackets 97w, S4 warehouse-sunday 146w, S5 founder-ceiling 107w,
  S6 abc-lists 116w, S7 room-question 109w, S8 listening-habit 97w, S9 diwali 72w). All 9 pass
  G1-G9; 0 four-gram overlap with his corpus (S4 has one common phrase, "that was supposed to",
  no echo of his wording). S9 Diwali is calendar-locked to Sunday 8 Nov 2026. Cross-check in this
  pass removed 3 more reuses of his own wording ("i use the abc", "from the ground up", "a simple
  question").
- 2026-10-21 — `17_DRAFTS/24_SAMPLE_SET_FOR_PUNEET.md` re-verified after the story-spine pass:
  107–146 words each, avg sentence 9.7–13.4, interior question at 70–86% depth, last line always a
  truth, 0 four-gram overlap with his corpus. Cross-check caught 2 errors: "hero moments" was our
  paraphrase (his words are escalations / edge cases / approvals) and "sweets they had never tasted"
  was an invention (his words: Indian sweets). Still open: S5's "500 people" is not attributable in
  the public record and must not publish until he confirms.

---

### 2026-10-22 — NEW DIRECTION: Startup Pedia-format posts on Puneet's personal LinkedIn

- Owner instruction (via the founder's-office intern at Ensur): the direction for the LinkedIn
  profile has changed. Content is now built in the **Startup Pedia house format** — third-person,
  encyclopedic, dated, sourced news-post format modeled on the Startup Pedia company page
  (713k followers) — and posted strategically on **Puneet Gupta's personal LinkedIn only**.
  Subject scope for this batch: **Puneet only**. The raw dump (every raw image, video and
  recording behind the existing content) was handed over; the data bottleneck is solved and the
  intern's job is now conversion of raw media into structured, publishable content.
- NEW FILE — `/Users/mymac/PG/startup-pedia-engine/` (INTERNAL ONLY, mode 700/600): a stdlib-only
  CLI (`engine/sp_engine.py`: init · facts · scan · new · gates · render · board · approve ·
  publish · kill) plus `FORMAT_SPEC.md`, `LINKEDIN_STRATEGY.md`, `ASSETS_GUIDE.md`.
- NEW RULE — TWO FORMAT FAMILIES. **Family P (pedia)**: 120-320 words, 3-6 short factual
  paragraphs, third person, no question mark, closing line is a fact and never a request,
  3-5 lowercase hashtags, one neutral CTA line. **Family N (narrative)**: the existing
  founder-craft rules (≤150 words, story spine, ≤2 standalone one-sentence paragraphs,
  question as hinge, never a question or request at the end). A post is one family or the
  other — never a blend.
- NEW RULE — SOURCE-PER-PARAGRAPH LOCK (mechanical, replaces "trust the writer"): every body
  paragraph in a Family P draft must carry a source id — `M-xx`/`L-xx` (moment), `R-xx`
  (receipt), `A-xx` (raw asset) — and the id must exist in the anchor bank. No source id, no
  render. This is the anti-fabrication lock; the illustrative-example zone is where fabrication
  happened before.
- NEW RULE — NO BORROWED BRAND. Do not copy Startup Pedia's `#startuppedia` hashtag, their
  "Get your startup story featured here" CTA, their byline, banner or layout. We take the
  structure, not the brand. One open decision for the owner: may "Startup Pedia" be used on his
  personal profile (only if Ensur owns it)? The engine warns (G13b), it does not decide.
- GATE LADDER (16 gates) lives in `engine/config/gates.json` + `names_allowlist.txt`: length,
  paragraph shape, sentence ≤25 words, no first person in P, no questions, no request closing,
  neutral CTA, source id present, no paused-chapter vocabulary or military place names, every
  proper name on the allow-list, no 5-gram reused from the owner's corpus (proper nouns
  exempt), 3-5 lowercase hashtags, headline discipline, no current-venture product/entity names,
  no placeholder paragraphs.
- FIVE P DRAFTS BUILT AND GATED 16/16: SP-001 Clensta's warehouse Sunday (M-28, R-06),
  SP-002 one billion litres of water saved (M-50, R-42), SP-003 a thousand hires (M-41, R-41),
  SP-004 a company that began in an IIT Delhi lab (M-46, R-43), SP-005 the founder entry
  (R-13, R-17, R-27). Slots: Mon/Wed/Fri 08:30 IST, 3 posts a week, 2 P + 1 N.
- STILL OPEN: the raw dump itself was not shared (the engine is written against a folder);
  the brand decision above; and the N-01 / N-02 slots in the fortnight need one capture each
  from the founder. SP-003 and SP-005 need one confirmation from him before scheduling.
- 2026-10-22 (later) — the raw dump is **Born Unicorn Season 1** (raw images + episode data),
  and the intern has no clear next step. Response: built `BU_INTAKE.md` (the data contract
  CSV, the consent gate, the 3-command run), `engine/bu_convert.py` (CSV → pedia drafts with
  new N-xx/R-xx ids in `engine/facts/bu_bank.json`, skipping any row without `consent=yes`),
  and two drafts from public material only: SP-006 (the season as a record, Mon 27 Oct) and
  SP-007 (Puneet on the jury side, Fri 30 Oct). Bank extended with Born Unicorn moments
  N-01..N-05 and receipts R-60..R-68 (all sourced from his own published posts 13:56-108).
  Two rules to carry: **a founder cannot be profiled in a public record without the show's
  clearance** (Startup Pedia's own model is opt-in), and the Born Unicorn material must never
  carry the defence framing that appears in his own wrap post (chapter is PAUSED).
- 2026-10-22 (later still) — the intern uploaded **5 raw Born Unicorn Season 1 frames**
  (3FC8FA7C-EAC2-4A33-910B-DC825DF73B1F.png + IMG_2515/2519/2547/2579.HEIC) into
  `engine/assets/`. What they turned out to be: production stills of the Season 1 jury
  set — the gold unicorn-head emblem and BORN gold wordmark on the backdrop, the panel
  line **"BOLD FOUNDERS BRIGHTER TOMORROW"** (white "BOLD FOUNDERS", yellow-green
  "BRIGHTER TOMORROW"), a raised wood stage platform, cream armchairs, side tables with
  notebooks and vases of yellow orchids, a host in a black dress with a sequined bodice
  holding a folder, four/five men on stage and a seated audience. The four HEICs carry
  file capture timestamps of **1 October 2026** (08:37, 08:46, 09:56, 11:36 +0000), the
  second shooting day in R-60; the PNG's timestamp (2026-10-22) is an export date, not a
  capture date. Created: `engine/drafts/SP-008.md` (Mon 16 Nov 08:30, 17/17 gates, image
  IMG_2547.jpg), sidecars for all five assets, and anchor-bank rows **N-06..N-08** and
  **R-69..R-74** in section 9 of `15_REAL_WORLD_ANCHORS.md` (sourced to "raw asset: ").
  Images attached to the two existing Born Unicorn posts: SP-006 → IMG_2519.jpg,
  SP-007 → IMG_2579.jpg. `bu_episodes.csv` now has 4 rows and **all 4 are blocked**:
  the frames carry no episode title, founder name, company, sector or figure, and the
  show's clearance for the people in them is unknown — so the converter correctly refuses
  to draft. Nothing was published and nothing was logged as published.
- 2026-10-22 (later still) — NEW TRAPS FOUND IN THE RAW DUMP, carry these forward:
  (1) **HEIC is not a normal image for tooling.** ffprobe reports a HEIC as dozens of
  512x512 hevc "streams" (the HEVC tile grid), so the engine's frame extractor produced
  tile thumbnails instead of the picture. Fix applied in `sp_engine.py`: `media_probe_path()`
  resolves a `.heic` to a sibling `.jpg` via sips before ffprobe/ffmpeg. Keep the HEIC,
  keep the JPG as the working copy.
  (2) **sips does not rotate.** `sips -s format jpeg` keeps EXIF orientation 6 on these
  files, so the JPG looks sideways in every tool that ignores EXIF and upright in the ones
  that honour it. PIL `ImageOps.exif_transpose` is the reliable way to get an upright
  copy for reading. Never read a cropped region of these files without transposing first.
  (3) **The show's own line is a usable quotable line** — the only fully legible words in
  the whole dump. The gold second line on the backdrop and the white two-line tagline
  behind the panel are occluded in every frame and must not be reconstructed.
  (4) A frame with no episode data is not a post; it is a receipt.
- 2026-10-22 (third pass) — TWO HARD FINDINGS FROM THE UPLOADED ASSETS, both must be carried forward:
  (1) **ONE ASSET IN THE DUMP IS AI-GENERATED AND MUST NEVER BE PUBLISHED.**
  `3FC8FA7C-EAC2-4A33-910B-DC825DF73B1F.png` carries a signed C2PA `caBX` manifest:
  softwareAgent "ChatGPT" (gpt-image), digitalSourceType "trainedAlgorithmicMedia", claim
  generator "OpenAI Media Service API", OpenAI OpCo LLC, created 2026-10-01T10:27:22Z. It is a
  synthetic image of a real, identifiable person, built from the real Born Unicorn photos.
  NEW RULE: an asset with synthetic provenance is never an anchor image and is never captioned
  with a real person's face. Check C2PA/EXIF on every incoming file, not just the obvious ones.
  Its sidecar is marked DO-NOT-PUBLISH.
  (2) **CORRECTION to the earlier "sips does not rotate" note — sips is not reliable either.**
  `sips -s format jpeg` DROPPED the EXIF orientation tag on IMG_2515/2519/2579, leaving three
  JPEGs stored sideways (4032x3024 pixels, no orientation tag) that would have gone to LinkedIn
  rotated 90 degrees. It happened to come out upright for IMG_2547, which is exactly what makes
  the bug dangerous. FIX: convert with `ffmpeg -y -i <file>.HEIC -frames:v 1 -q:v 2 out.jpg`
  (autorotate on, full 3024x4032, pixels upright), then READ the output with the image tool and
  look at it before it is attached to any post. Never trust a converted image you have not
  looked at. The four camera frames are now upright; the PNG is untouched.
  (3) What the frames actually support: the only fully legible words in the entire dump are the
  show's own set line, BOLD FOUNDERS BRIGHTER TOMORROW. The white two-line credit line on the
  backdrop is occluded in every frame (fragments only) and must never be reconstructed. The
  frames carry no founder name, company, sector, number or quote — so they are receipts and
  scenes, not episode data. All episode-level facts remain ASK until the show team clears the
  founders and supplies the episode data.
- 2026-10-22 (fourth pass) — THE CONTEXT LAYER FOR BORN UNICORN, and the rule behind it. The
  raw dump supplied SCENES, not FACTS: the only legible words in the five assets are the show's
  own set line, BOLD FOUNDERS BRIGHTER TOMORROW. The facts came from the PUBLIC RECORD instead,
  and they are rich: RASA Group launched NEXT UNICORN - Season 1 on 27 Aug 2026 (branded BORN
  UNICORN on set), funnel 5,000-6,000 applications (17 Aug-10 Sep) -> Top 30 (announced 15 Sep)
  -> two-day Delhi Founder Experience 25-26 Sep -> Top 6 -> Canton Fair China in Oct at zero cost
  -> potential investment up to Rs 10 Cr. Mentor: Rahul Agarwal (20+ yrs, ex-Organic Harvest,
  100+ entrepreneurs mentored). Ecosystem partner: AIC IIT Delhi (Atal Incubation Centre, IIT
  Delhi Sonipat Campus), CEO Alok Pandey = the guest jury. 110M+ reach claim. All of it now in
  the anchor bank as R-75..R-88, `PRESS-ATTRIB` (cite the release / the show's page), plus
  R-86..R-88 as `OK` from the raw assets. NEW FILE `BU_CONTEXT.md` = the context sheet: the
  record in wire-report order, the one-paragraph version, and the founder-entry blueprint.
  NEW RULE — A FOUNDER MAY BE NAMED ONLY IF THE FOUNDER ANNOUNCED IT THEMSELVES, PUBLICLY; then
  cite their announcement, never present it as our finding. That is how a media platform covers
  a company, and it is the rule that keeps the founder-level posts defensible without the
  show's clearance. R-68 (episode list, per-founder facts) stays `ASK`.
  NEW DRAFT SP-009 (Wed 18 Nov, 17/17): the platform's first season as a pedia entry — the
  funnel, the dates, the China trip, the Rs 10 Cr opportunity, the mentor's record. Nine drafts
  now exist, all 17/17.

- 2026-10-22 (fifth pass) — THE QUOTE CARD IS REBUILT ON A REAL FRAME, AND THREE SCHEDULE
  BUGS ARE FIXED. (1) `engine/assets/Investors Bet on Resilient Founders (real).png` now
  exists: `build_card.py` was fixed to lift the whole footer band (icons + URL) from the
  template instead of a guessed 80px strip that clipped the icons, and to paste only the
  glyph pixels (the template's "black" is 3,3,3 and left a visible seam on a 0,0,0 canvas).
  The synthetic template stays design-only; its likeness pixels are not in the rebuild.
  Sidecars written for both files; SP-010 repointed to the `(real)` file and still 17/17.
  RULE: the card's footer may be lifted from the template (no person, pure design), but no
  pixel of the synthetic likeness may survive into a publishable asset.
  (2) THREE PUBLISH DATES WERE WRONG. SP-006, SP-001 and SP-003 were labelled Monday but fell
  on a Tuesday (27 Oct, 3 Nov, 10 Nov 2026). Corrected to Mon 26 Oct, Mon 2 Nov, Mon 9 Nov in
  `schedule.csv`, `PUBLISH_THIS_WEEK.md` and each draft's `slot:`; card files re-rendered.
  RULE: always compute the weekday from the date; never trust a hand-typed day label.
  (3) G15 IS WARN-ONLY, so five drafts (SP-001..SP-005) show 17/17 while carrying NO anchor
  image. They are text-only and must stay held — the house format is text + one image (0 of
  50 top posts are video/carousel, 47 of 50 carry no body link). `PUBLISH_THIS_WEEK.md` now
  lists them as blocked-on-image; the five Born Unicorn posts are the only image-ready ones.
  NEXT: either make G15 a hard fail (a product decision) or keep it warn-only and trust the
  queue page; and get Clensta / pre-2016 stills from Puneet for SP-001..SP-005.

- 2026-10-23 — FIRST PERSON WHEN IT GOES ON HIS OWN ACCOUNT (owner instruction). A piece
  written to be pasted directly into Puneet's personal LinkedIn is written in the first person,
  not the Startup Pedia third person. The third-person Family P format stays for the
  pedia-format batch; a first-person post follows the narrative rules instead (≤150 words,
  story spine, no question mark and no request in the final line). Same sourcing and anchor
  rules apply either way.

- 2026-10-25 — THE THREE NEW FRAMES (IMG_2546, IMG_2618, IMG_2619) AND FOUR NEW SAMPLES.
  All three are iPhone 13 Pro files with an EXIF capture date of 1 October 2026 — 09:56:08,
  12:11:37, 12:11:49 UTC — so they are the **second shooting day**, not a new event, and any
  post built on them is evergreen. Bank extended: moments N-09..N-11 and receipts
  R-89..R-93 in section 9b of `15_REAL_WORLD_ANCHORS.md`; sidecars written for all three.
  The frames show the work at the table, not the stage: **09:56 listening → 12:11 writing →
  12:11 speaking**. That is the shape of a jury's job, and it is why three stills are three
  posts and not one (a pedia post carries one image).
- 2026-10-25 — NEW RULE — THE CONSENT TRAP ON THE BEST FRAME. IMG_2618 is the only frame that
  shows the show's own name (…ORN / …ICORN / …EASON 1 in gold capitals) and it is also the
  only one carrying an unnamed third party (a second juror, plus a third panelist's hand).
  It cannot be cropped both ways at once: crop to Puneet and the name is lost, crop to keep
  the name and the third party stays. RULE: a face is never named from a photograph, and a
  frame with an unnamed third party is held until their consent or the show's release. A
  derived 4:5 crop (`IMG_2618_crop.jpg`) gives a publishable version of Puneet alone.
- 2026-10-25 — THE ASSETS FOLDER WAS CLEARED. The five files present on 22 Oct (IMG_2515,
  IMG_2519, IMG_2547, IMG_2579 and the synthetic PNG) are gone from disk; a full search of
  `/Users/mymac/PG` found nothing. Four existing drafts point at them and two slots are this
  week: SP-006 (Mon 26 Oct), SP-010 (Wed 28 Oct), SP-007 (Fri 30 Oct), SP-008 (Mon 16 Nov).
  RULE: three cleared images cannot cover eight posts, and reusing one frame across adjacent
  slots is the tell that a feed is automated. Get the originals back or re-export from the
  show; do not shuffle.
- 2026-10-25 — BATCH B BUILT: SP-011 (the room as a record, IMG_2618, held on consent),
  SP-012 (the notebook, Family N, first person, IMG_2619), SP-013 (the mentor — Rahul
  Agarwal, 100+ entrepreneurs, IMG_2546), SP-014 (the guest seat — AIC IIT Delhi, CEO Alok
  Pandey, IMG_2618_crop). All 17/17 gates, zero 4-gram overlap with his corpus. Slots Fri 20,
  Mon 23, Wed 25, Fri 27 Nov. `THREE_FRAMES_BRIEF.md` is the reasoning document;
  `BATCH_B_FOUR_SAMPLES.md` is the paste-ready set.
- 2026-10-25 — THE STRATEGIC ANSWER TO "MORE RELEVANCY": the **gatekeeper position**. He was
  one of six on a jury that took 5,000–6,000 applications to thirty, then six. For a founder
  audience that is a stronger authority position than any award — an award says a jury liked
  him, a jury seat says he is the jury. The next batch is a theme, not a post: the gatekeeper's
  view, all Family N, all written from the seat.
- 2026-10-25 — BORN UNICORN IS NEARLY SPENT: nine posts off one event (SP-006..SP-014). The
  unspent numbers left are thin (110M+ reach, the 2 AM crew, the five sectors, the ₹10 crore).
  Say this to the seniors now; the next batch must come from the 30 unspent live moments in the
  anchor bank and the Clensta / Honeywell / IIT Delhi receipts, not from the show.
- 2026-10-25 — TWO ENGINE FINDINGS. (1) **G7 checks that a source id exists, not that it
  supports the sentence.** SP-010 tags four opinion paragraphs with [R-60], a receipt about
  shooting dates, and passes. Recommended fix: a warn-only gate comparing each paragraph with
  its receipt's claim text and flagging zero content-word overlap. (2) **G10 runs at 5-grams
  and lets 4-gram echoes through.** Two of the four new drafts had one; "i spent most of" in
  SP-012 was a genuine echo of his voice and the gate passed it. Caught by hand, both fixed.
  Recommend `ngram_overlap: 4` for family N.

- 2026-10-25 — THE HEADLINE FORMAT THEY ACTUALLY WANT (learned from the first in-house card,
  `Founder's 10X Scale Question.png`). The headline is not a LinkedIn first line: it is text
  burned onto the image, with one capitalised payoff run. Reference sentence: "The quietest
  moment on set isn't a forgotten script, it's when a founder is asked WHAT BREAKS AT 10X
  SCALE." The five slots are: **superlative + place** ("the quietest moment on set") →
  **the obvious answer, rejected** ("isn't a forgotten script") → **the pivot** ("it's when")
  → **a specific human moment** ("a founder is asked") → **the payoff in caps, carrying a
  number**. Rules: 18–24 words; exactly one caps run and it goes last; the caps line carries
  the number; the negation must name a real cliché; the place is two or three words; no
  adjectives in the payoff; sayable in one breath; the description answers the headline and
  never restates the caps line. Spec and three worked examples in
  `startup-pedia-engine/HEADLINE_FORMAT.md`.
- 2026-10-25 — the earlier headline advice was wrong and is superseded: 9–10 word aphoristic
  headlines ("A selection round is an argument, not a verdict") are too small for a card and
  three of them read as one note repeated. The card format wants a scene, a rejection and a
  number, at 18–24 words.
- 2026-10-25 — "What breaks at 10x" is HIS OWN published line ("What breaks when this becomes
  10x bigger? And what does the founder understand that the rest of us don't yet?"). The card
  keeps the shape and changes the words, which is the right way to reuse it, but it is the
  second time the idea ships: treat it as a signature question, never as a fresh insight, and
  if it returns a third time it needs new material under it.

- 2026-10-25 — **VOICE DECIDED: FIRST PERSON, AS IF HE WROTE IT HIMSELF.** Owner instruction:
  do not write in the third person, and do not frame the post around him writing or saying
  something — the post must read as him writing it. This supersedes the third-person Family P
  direction of 2026-10-22 for his **personal profile**. What survives from the pedia format is
  the discipline, not the pronoun: dated, sourced, no hype, no adjectives doing a number's
  work, short factual paragraphs. The pronoun is always I.
- 2026-10-25 — CONSEQUENCE FOR THE ENGINE: G4 currently fails any Family P draft containing
  I/we/my/our, so **every one of SP-001..SP-014 (except SP-012) is now off-direction and will
  not pass if converted as Family P.** The fix is either a third family ("P1": pedia structure,
  first-person voice) or `first_person: true` on P. Until that is decided, new posts are
  written to the Family N rules (≤150 words, ≤2 standalone one-sentence paragraphs, question as
  the hinge at 60–90% depth, never a question or a request at the end) even when the body is
  built from dated record lines.
- 2026-10-25 — first person must follow the photograph, not the other way round. In IMG_2618 he
  is the one **talking** with a pen raised and the other juror is the one writing, so the first
  person there is "I was the one talking", never "I was taking notes".

- 2026-10-25 — THE THREE EMPHASIS VARIANTS ON THE CARD HEADLINE, now all recorded in
  `startup-pedia-engine/HEADLINE_FORMAT.md` §3b/§3c from the three in-house cards:
  (1) **caps on the closing payoff** — 10X Scale Question ("…a founder is asked WHAT BREAKS AT
  10X SCALE."), the caption owes an *answer* to the question the caps poses; (2) **caps on a
  coined term, mid-sentence** — Distribution Density ("DISTRIBUTION DENSITY determines if you
  survive."), the caption owes a *definition* of the coinage; (3) **ellipsis, no caps** —
  Defending Founders ("…while another tests the defence…"), where the highlight bars carry the
  emphasis and the caption owes a *completion* of the hanging sentence. The reconciling rule:
  exactly one emphasis device per card, always on the thing you would screenshot; a caps line
  closes a thought, an ellipsis hands it over.
- 2026-10-25 — all three card descriptions are written, gated and filed
  (`CARD_10X_SCALE_QUESTION.md` 142w, `CARD_DISTRIBUTION_DENSITY.md` 141w,
  `CARD_DEFENDING_FOUNDERS.md` 133w): first person, 6 paragraphs each, no sentence over 21
  words, at most 2 standalone one-sentence paragraphs, hinge question at 57–68% depth, never a
  question or request at the end, zero 4-gram overlap with his published corpus. Each file ends
  with the one or two lines that need his explicit yes, and none of the three has been
  published or scheduled.
- 2026-10-25 — REUSABLE MOVE, worth keeping: a first-person draft with only one "I" in 130+
  words reads as third person wearing a pronoun. The fix is not to sprinkle pronouns; it is to
  make him the *actor* of the opening clause ("I watched the same job happen twice at that
  table", "Then I ask what breaks first at ten times the size"). Target is roughly 2+ first
  person acts per post, and never zero.

---

### 2026-10-26 — NEW SURFACE: YouTube + Instagram, built from the colleague's Canva deck

- Owner direction: the LinkedIn work is done; the next build is **YouTube and Instagram for
  Puneet's personal channels**. Base it on the colleague's deck
  (`Puneet Gupta x bingelabs`, Canva `DAHNTLyav2Q`) — "copy the style" — and **add the missing
  domain layer**: the deck only carries one domain of his career, so the persona has to be
  shown across the others too.
- NEW FOLDER — `/Users/mymac/PG/youtube-instagram-engine/` (INTERNAL ONLY, mode 700/600):
  00 deck audit · 01 positioning · 02 domain map · 03 YouTube · 04 Instagram · 05 cadence ·
  06 production · 07 governance · 08 worked examples · BOARD.csv · templates/ · engine/yg_gate.py.
  It shares the LinkedIn engine's spine: same anchor bank, same source-id discipline, same
  explicit-approval model. It does not duplicate facts.
- NEW RULE — THE DECK IS A SOURCE, NOT A SPEC. Its eight formats and its seven-beat podcast
  theme are kept intact; its subjects are moved to the live domains. Same machine, new inputs.
- NEW RULE — THE HELD CHAPTER STAYS HELD ON VIDEO TOO. The deck's entire positioning sits in
  the paused chapter, so it cannot be shot as written. It is preserved verbatim in
  `00_DECK_AUDIT.md` §7 and switched off. Turning it on takes one explicit owner instruction
  and it then becomes **one series inside the live positioning**, never a re-positioning.
- POSITIONING CHOSEN (recommended, not yet approved): "**the builder who explains how India
  actually makes things**" — every episode, one thing India makes: how it works, what it
  costs, where it is still weak. The four attributes become Credible · **Operator** (replacing
  "Veteran", which points at the held chapter) · Approachable · Strategic.
- DOMAIN MAP (the add-on): 1 manufacturing/industrial LIVE · 2 consumer/D2C LIVE · 3 deep tech
  from a lab LIVE · 4 capital & the gatekeeper seat LIVE · 5 AI & sovereignty THEMES ONLY (NDA)
  · 6 leadership & founder craft LIVE · 7 the held chapter. Six live, one held.
- NEW RULE — VIDEO GATE LADDER (14 gates, `engine/yg_gate.py`): runtime from spoken word count,
  hook ≤12 words and never a question, title ≤60 chars with a number and no question mark,
  a source id on every beat that exists in the bank, no held-chapter vocabulary, no NDA names,
  no placeholders, last spoken line never a question or a request, 3–5 lowercase hashtags,
  caption first line carries a number, no 4-gram reuse of his published writing, thumbnail ≤5
  words, format must be live, domain must be 1–6. Stdlib only; run before anything is shot.
- THE GATE EARNED ITS KEEP ON DAY ONE: it caught a spliced number ("a bath takes ~150 litres",
  true, no receipt), an echo of his own published line ("one billion litres of water"), and a
  borrowed legalism ("a patent is the right to stop"). All three rewritten.
- NEW RULE — ONE HANDLE FOR NOW. The deck asks for a dedicated Instagram page for podcast
  shorts; recommendation is to keep clips on his own handle. A second handle splits a young
  audience and starts at zero. Revisit only past ~50k followers with data, not preference.
- NEW RULE — CAPACITY IS THE REAL CONSTRAINT. The deck's weekly 60–75 min podcast implies a
  set, a guest pipeline and an editor, none of which exist. The fortnight is ~42 hours of work,
  i.e. one full-time person. If that is not funded, the honest slate is one long-form a month,
  one Short a week, one card a week — planned now rather than missed later.
- STILL OPEN (three decisions only the owner can make): (1) the held chapter, on or off;
  (2) one Instagram handle or two; (3) the five guest names. Plus the existing ASK rows that
  block specific episodes (Intertech figures for camera, the packaging detail, the 500+
  and $30M claims).
- 2026-10-26 (later) — PRE-EXECUTION PRESENTATION BUILT for the room:
  `youtube-instagram-engine/presentation/DECK.html` (22 slides, self-contained, arrow keys, `F`
  fullscreen, `P` print, `#n` deep-link), `DECK.pdf` (22 pages, A4 landscape, full-bleed dark),
  and `SLIDE_SCRIPT.md` (per-slide copy, what to say, timings, the three answers to record, the
  five objections). Deck order: the ask first → credit the bingelabs deck → the one-domain
  problem → his own analytics as evidence → positioning → domains → slate → Instagram →
  one-moment-eight-surfaces → rhythm → the source lock → the honest 42 hours → two versions of
  the plan → first 90 days → what we need → the refusals → close.
- NEW RULE — THE PRESENTATION NAMES NO HELD-CHAPTER WORDING. The deck's own bucket names are
  not printed anywhere in it; the chapter appears once, as "the chapter on hold", with the
  question "back on or stay off". The slide script tells the presenter to use his own phrasing
  out loud and to keep it off the slides. Same rule as the posts.
- NEW RULE — THE ASK GOES ON SLIDE TWO. The deck leads with the three decisions (the paused
  chapter, one handle or two, the first guest) before any strategy, because a busy founder needs
  to know the meeting has a shape and an end. The positioning sentence is the one decision that
  matters that day; everything after slide seven is detail.
- PRESENTATION HONESTY RULE — slide 17 states the 42 hours and the three things that do not
  exist (set, guest pipeline, editor), and slide 18 offers the reduced 14-hour slate as an
  equal option. Do not lobby for the fuller slate in the room; it is the one that fails quietly.

### 2026-10-26 — RE-ENABLED BY OWNER: defence wording is back ON (supersedes the 2026-10-17 pause)

- Owner explicitly chose "Re-enable fully": defence / military / national-security wording, pillars,
  guests and references from the bingelabs deck are allowed again for the YouTube + Instagram plan.
  The 2026-10-17 PAUSED entry is superseded (kept above for history, not deleted).
- DOMAINS for the video plan are exactly five: **Defence, Entrepreneurship, Investor, Founder, AI.**
  NO manufacturing / consumer / D2C / "on the floor" / warehouse framing — the owner rejected it.
- NEW RULE — CROSS-CHECK BEFORE GENERATING: do not invent structure. Every slide and idea must be
  checked against the bingelabs Canva deck (DAHNTLyav2Q) first; we ADD to their structure (their
  pillars, their Podcast Theme four-box loop, their guest categories, their "The idea / Why this
  idea / Reference" pattern), we do not replace it.
- Stealth discipline still holds: never name the current venture's products, partners, customers,
  investors or fund.
- DELIVERED 2026-10-26: `youtube-instagram-engine/presentation/DECK.html` rebuilt as 37 slides that
  mirror the bingelabs deck page for page (Vision, Brand Persona with "Veteran", Anti Positioning,
  Content Index, Podcast with the four-box theme, Probable Guests, their 8 YouTube pillars and 5
  Instagram pillars with their verbatim idea / why / references, Podcast Shorts handle, Formats,
  Monthly Cadence 16 reels · 4 carousels · 6 long-form · 2 podcasts · 10-12 shorts, Process
  Pre Prod → Prod → Post Prod → Post Publish, "Let's build it together"). Every addition carries an
  ADDED tag. `09_IDEATION_PLAN.md` rebuilt as the idea bank (BL = theirs verbatim, + = ours with
  domain and receipt). Older files 00-04, 08 and SLIDE_SCRIPT carry a SUPERSEDED banner. No PDF —
  owner said HTML is enough.
- LESSON: bingelabs' Content Index numbers (8-14, 15-18 …) are SLIDE numbers (a table of contents),
  not episode counts.

### 2026-10-26 — NEW RULE: no "bingelabs" wording in anything shown to Puneet; one unified strategy

- Owner instruction: remove every mention of "bingelabs" from the presentation materials, and
  present the plan as one complete strategy (no "ADDED" tags, no "their / our" split). Applies to
  `presentation/DECK.html`, `presentation/SLIDE_SCRIPT.md`, `09_IDEATION_PLAN.md`, `README.md`.
  The superseded history files (00-04, 08) and this memory log keep the name for provenance only.
- The deck is now 35 slides organised by TRACK: YouTube = Flagship / Defence & Strategy /
  Future & AI / Building & Capital (12 pillars); Instagram = Founder's Journey / Defence &
  Strategy / Building & Capital / Future & AI (8 pillars). Non-strategic slides were cut (Formats
  link, separate Podcast Shorts slide, agency-portfolio references); a Monthly Cadence & Mix slide
  sets the balance at 11 of 28 core pieces (~40%) defence, 60% the other four domains.
- Purpose of this meeting is DIRECTION ONLY; execution (episodes, guests, shoots) comes after
  Puneet signs off.

### 2026-10-26 — NEW RULE: two separate decks — personal channel and podcast

- Owner instruction: the personal channel (@puneetgbuilds, YouTube + Instagram) and the Podcast
  with Puneet are SEPARATE channels with SEPARATE decks. The 35-slide combined deck is archived in
  `youtube-instagram-engine/presentation/archive/`.
- Owner answers: split into two decks; podcast has its own channels (personal handle is
  @puneetgbuilds); personal deck uses the same sections, concise; DIRECTION ONLY, no roadmap/phases.
- DELIVERED: `DECK_PERSONAL.html` (18 slides: vision, persona, anti-positioning, five domains, two
  channels two jobs, YouTube 11 pillars in 3 tracks, Instagram 8 pillars in 3 tracks, cadence 10 of 26
  core pieces ~40% defence, process, close), `DECK_PODCAST.html` (12 slides), both speaker scripts,
  `10_BLUEPRINT_PERSONAL.md` (guide + brainstorm + domain x pillar matrix + rules + open questions),
  and `build_decks.py` to regenerate. Domains for the personal channel: Defence, Entrepreneurship,
  Investor, Founder, AI. Defence wording on (re-enabled 2026-10-26); stealth rule holds.
- Open for the owner: confirm handle spelling @puneetgbuilds on both platforms; whether the podcast
  clips handle stays separate.

### 2026-10-26 — NEW RULE: personal channel = ONE track, FIVE pillars (one per domain)

- Owner: too many pillars and tracks. The personal deck now has a single track and one pillar per
  domain, the same five on YouTube and Instagram: The Strategic Affairs (defence), Startup Breakdown
  (entrepreneurship), The Investor's Table (investor), Journey Decoded (founder), AI Decoded (AI).
  Former pillars survive only as "recurring formats" inside these five. Deck is 14 slides. Mix:
  long form 2/1/1/1/1, reels 7/3/2/2/2, carousels 1/1/1/0/1 = 10 of 26 defence.
- Brand persona cross-checked against Canva p03: Veteran top, Credible right, Strategic left,
  Approachable bottom, words only (no definitions on the original). Owner chose to KEEP it exactly
  as Canva on both decks.

### 2026-10-26 — NEW RULE: every deck follows the strategy flow, ending on growth & engagement

- Owner: both decks must run Content Strategy → Index → Ideas → What the ideas are → Strategic
  theme → Why (in the last), all in service of growth and engagement.
- Applied: personal deck 17 slides (Content Strategy divider, index with slide numbers, 5 pillar
  slides each reading idea → example ideas → strategic theme → why growth & engagement, channel
  theme loop Moment → Context → Insider View → Takeaway, closing Why slide with a Discover → Watch →
  Engage → Follow funnel and a measure per stage). Podcast deck 15 slides (added divider, index,
  "What the episodes are" five-lane table, theme eyebrow, closing Why slide).
- Growth claims stay honest: no targets, no platform benchmarks; the only data cited is his own
  LinkedIn (19.22% best post on a real scene; 74,295 impressions at 0.21% on a broad post).

### 2026-10-26 — FACT-CHECK PASS on both video decks (dossier audit + web check) — carry forward

- Corrected facts (use these, everywhere): patents = 5 on record (filings 15–20+; never "~20 patents");
  ₹100 cr ARR is COMPANY-REPORTED (Inc42: FY24 revenue ₹78 cr); Clensta = IIT Delhi-INCUBATED;
  Series A ₹20 cr+ Dec 2021 is press-verified (investors not named); stepped down: role ended MAR 2025,
  announced JUL 2025, buyer NOT public; defence = TAK Technologies 2008–2016, head of strategy then
  core team building DarVi — NOT a founder of TAK; ~1,000 = cumulative hires, never "a team of 1,000";
  Born Unicorn: he joined the jury AFTER the Top 30 (15 Sep) — never "picked 6 from 5,000";
  5,000–6,000 was the show's target, not a count. 74,295 = impressions, not people.
- Don't use "Dr." until the DBA is complete. Most 2025–26 profile pieces about him are PAID
  releases (NewsVoir, VMPL, Outlook Hub4Business, SiliconIndia) — never cite them as independent press.
- Example-title corrections: Russia+France ≈ 69% (SIPRI 2021–25), Russia 70%→40% in a decade; "80% of
  China's energy" is false (≈80% of OIL imports, CSIS 2016); India is still the #2 arms importer;
  Chabahar waiver expired 26 Apr 2026; DRDO is 68 years old; iDEX 548 contracts (Feb 2026).
- Guests: Lt Gen Hasnain = Governor of Bihar (removed); Dr Ajay Kumar = UPSC Chairman (on hold);
  Deepika Rathore is Lt Col; never pair Karnad and Sawhney; disclose FITT–Clensta link if Dr Nikhil
  Agarwal appears; Bhuvneshwar Kumar added (Puneet moderated his FITT session, Sep 2026).
- "Let's build it together" removed from both decks (near-verbatim of his own line). Each deck now
  ends on a decision slide ("Three answers to move ahead") plus an appendix of sources.
- Decks are now interactive: M menu, N speaker notes + timer (from the SLIDE_SCRIPT files), F full
  screen, ? help, clickable index rows, step-by-step reveals on the theme and Why slides, swipe.
  Regenerate with `presentation/build_decks.py`; never hand-edit the HTML.

### 2026-10-26 — Brand persona and anti-positioning are STRATEGY, labelled and backed

- Owner chose: label both slides as strategy and back each word. Persona = "a strategic choice" (not a
  fact, not the vision): Veteran = "19 years building, 8 in defence technology. An industry veteran,
  not a military one" (he was selected by the Army but did NOT serve — never imply service);
  Credible = NEA 2019 · ₹20 cr+ Series A 2021 · IIT Delhi-incubated company; Strategic = head of
  strategy at TAK · Born Unicorn jury · his frameworks; Approachable = plain, warm, self-deprecating.
- Anti-positioning = "Guardrails", each with a test: Preachy → show the decision and the number;
  Pro-politics → policy yes, party politics no; Typical Motivator → no advice without his own
  example. Podcast versions are host-specific. Canva words and layout kept on both decks.

### 2026-10-26 — References on every pillar + "Voice Cloning" in Pre Prod

- Owner supplied 4 references; mapped by checking each live page: Ritesh Agarwal "The Truth About
  Building a Business in the US" (youtu.be/q554XAT8x-c) → Journey Decoded (and the model for a
  founder's personal channel); Aman Gupta boAt "7 Cr to 3000 Cr" Short → Startup Breakdown; Aman
  Gupta MBA reel (DVQLqlcEqlt) → Journey Decoded; Liran Wizman partnership post (DdQ7HO8OG29) →
  Investor's Table. Canva links reused per pillar; new finds added (SeedToScale × Elevation, VC
  checklist, Think School, Nilekani/Bloomberg, Perplexity case study; podcast: Nikhil Kamath and Raj
  Shamani episodes with Aravind Srinivas). Lives in REFS in build_decks.py.
- Owner: add only the text "Voice Cloning" to Pre Prod (both decks). Internal note: cloning his voice
  needs his explicit written consent and must never publish without his yes.
- 2026-10-26 (later): owner replaced it with "Audio Cloning" + "Video Cloning" in Pre Prod, after
  Scripting, both decks. Same internal rule: explicit written consent for his voice and likeness;
  nothing cloned publishes without his yes.



### 2026-10-26 — Carousels allowed; Top 30 date unconfirmed; IMG_2568 identity

- Owner: LinkedIn carousels (document posts) are ALLOWED for Puneet's profile. This supersedes the
  "text + one image only" format line in `28_CONTENT_TYPES.md` for carousels.
- Owner has no knowledge of a 15 September Top 30 announcement. R-79's date is unconfirmed: do NOT
  write "cut to thirty" or any Top 30 figure in any draft until a source is supplied.
- Owner identified Puneet in IMG_2568 as the man seated nearest the plant (brown blazer, striped shirt).
  Owner-stated, so usable for captions; still never name other people from a photo.
- Owner wants plain slide text he can place in order against his photos, not renders.

### 2026-10-27 — NEW RULE: ONE SHORT, ALL PLATFORMS (personal channel)

- Owner: we do not create different content per platform. Each piece is ONE short video made once and
  posted on YouTube Shorts, Instagram Reels and Facebook Reels. No separate long form, posts or carousels
  in the personal-channel plan (supersedes the 12 reels / 4 posts / 4 carousels split of the same day).
- Cadence: 12 shorts a month, 3 a week. Strategic Affairs 4 (every week); Startup Breakdown, The Investor's
  Table 2 each (weeks 1, 3); Journey Decoded, AI Decoded 2 each (weeks 2, 4). Defence = 4 of 12 (one in three).
- Content Index keeps three platform columns (YouTube / Instagram / Facebook) showing the same count.
- 2026-10-27 (addendum) — the one-piece-all-platforms rule also covers one monthly POST (Journey Decoded,
  week 3) and one monthly CAROUSEL (Startup Breakdown, week 2). Each is made once and uploaded to YouTube
  (Posts tab, up to 10 images), Instagram and Facebook at the same time. This partly reverses "no posts or
  carousels" above: one of each is back, nothing else. Per-month count is the assistant's reading, unconfirmed.

### 2026-10-27 — NEW RULE: run the humanizer skill before EVERY output; goal is a Puneet voice clone

- Owner: the work is to clone Puneet's writing style, thinking style, tone and voice, and the text must not
  look like AI slop. Run the blader `humanizer` skill (v3.1.0, MIT) on every piece of generated text before
  it is shown to the owner. No exceptions, including slide copy, captions, scripts and replies.
- Installed (manual, not via the Claude Code /plugin commands, which opencode does not have):
  `~/.config/opencode/skills/humanizer/SKILL.md` and `~/.agents/skills/humanizer/SKILL.md` (md5 match).
  Keep both in sync. Separate from the older `linkedin-humanizer` skill; run both on LinkedIn text.
- Voice source: the humanizer says a writing sample overrides its patterns. The sample is
  `13_REAL_WRITING_SAMPLES.md` (INTERNAL, 600), so his own habits (dashes, one-line paragraphs, emoji in
  warm posts) win over the generic rules where the corpus shows them.
- Process each time: mark tells (not-X-but-Y, one-line closers, triads, dashes, stock words, bold labels),
  rewrite, check no fact was added or lost, then search again for survivors. Never add a fact, name or number
  that is not in the anchor bank.
- Honest limit recorded: a humanizer removes AI tells; it does not create his voice. The clone depends on his
  real material (anchor bank, corpus). "100%" is not a claim we can make.
- 2026-10-27 — Owner confirmed `1st.jpg` shows Puneet and is a real photo (Born Unicorn set). Draft saved at
  `17_DRAFTS/2026-10-27-jury-reasons-v1.md`. Owner declined the optional "real moment" upgrade: ship as opinion.
