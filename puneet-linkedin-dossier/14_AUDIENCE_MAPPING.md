# 14_AUDIENCE_MAPPING.md — Audience Mapping

> **INTERNAL ONLY — DO NOT SHARE.** Unredacted working file: contains per-post performance data, follower and engager demographics, and named employer segments. Not for external distribution.

**Date:** 2026-10-19
**Source:** `AggregateAnalytics_Puneet Gupta_2025-10-20_2026-10-19.xlsx` (LinkedIn native analytics export, owner-supplied; 6 sheets, read-only). Secondary: `01_PROFILE.md`, `07_PERSONA_ANALYSIS.md`, `09_MANAGER_BRIEF.md`, `13_REAL_WRITING_SAMPLES.md`, `puneet_gupta_posts.md`.
**Period:** 2025-10-20 to 2026-10-19 (365 consecutive days, no gaps).
**Purpose:** Establish who actually reads the account, what each post type is doing for them, and what the export can and cannot prove before any further post or CTA decisions are made.

## 1. What the export contains

| Sheet | Granularity | Fields |
|---|---|---|
| `DISCOVERY` | Period total | Impressions, members reached |
| `ENGAGEMENT` | Daily, 365 rows | Impressions, engagements (net) |
| `TOP POSTS` | Per post, 50 max | Two independent rankings: by engagements (A–C) and by impressions (E–G). Same 50 URLs in both. |
| `FOLLOWERS` | Daily, 365 rows | New followers, plus a single total-followers cell |
| `AUDIENCE DEMOGRAPHICS` | Segment share | Followers: company, location, size, seniority, job title, industry |
| `CONTENT DEMOGRAPHICS` | Segment share | People reached by content: same six dimensions |

Two structural facts drive everything below. The demographics are **top-10 lists of percentages**, not counts, so coverage is partial and segment counts are [inferred]. And the export has **no post-by-demographic cross-tab**, so any claim linking a theme to a segment is [inferred], not measured.

## 2. Period summary

| Metric | Value |
|---|---|
| Impressions | 447,562 |
| Members reached | 189,589 (2.36 impressions per member) |
| Engagements (net) | 19,250 |
| Engagement rate | 4.30% |
| Followers on 2026-10-19 | 28,485 |
| New followers in period | 4,449 (gross; no unfollow data) |
| Implied followers at period start | 24,036 [inferred: 28,485 − 4,449] |
| Period growth | +18.51% (upper bound, gross) |
| Top-50 posts | 88.7% of impressions, 87.7% of engagements |

A live guest fetch on 2026-10-16 returned 28,471 followers; the export says 28,485 on 10-19. The two are consistent within normal movement.

Data quality: 5 days carry negative engagements (−43, −2, −2, −5, −1), so the metric is net of reversals; 72 of 365 days show zero engagement; the 20–23 June 2026 window reports 11,251 impressions against 3 engagements, which reads as a tracking gap rather than a real collapse.

## 3. The year splits into two regimes

| Window | Days | Impressions | Engagements | ER |
|---|---|---|---|---|
| Before 2026-07-18 | 271 | 265,981 | 2,678 | **1.01%** |
| From 2026-07-18 | 94 | 181,581 | 16,572 | **9.13%** |

A looser split at 2026-04-20 gives 0.79% against 6.58%. Either way the second half is a different account. The last quarter holds 39.3% of annual impressions but 84.1% of annual engagement.

Monthly, the turn is visible in July and then compounds:

| Month | Impressions | Engagements | ER |
|---|---|---|---|
| 2026-07 | 78,348 | 5,212 | 6.65% |
| 2026-08 | 80,263 | 7,137 | 8.89% |
| 2026-09 | 26,584 | 3,063 | 11.52% |
| 2026-10 (19 days) | 10,080 | 1,433 | 14.22% |

Two caveats before anyone reads a trend into this. December 2025 alone is 22.4% of annual impressions at 0.49% ER, so it drags the early regime down; excluding December the pre-July figure is 1.32%, not 1.01%. And part of the late rise is a denominator effect: impressions fell sharply in September and October while engagement held, so ER rose partly because reach narrowed.

## 4. Two populations, not one

This is the central finding. The follower base and the audience reached by content are demographically different groups.

| Dimension | Followers | Content reach | Index (reach ÷ followers) |
|---|---|---|---|
| Seniority: Senior | 30% | 26% | 0.87 |
| Seniority: Entry | 13% | 18% | **1.38** |
| Seniority: Owner | 10% | 5% | **0.50** |
| Seniority: CXO | 7% | 4% | **0.57** |
| Title: Founder | 8% | 4% | **0.50** |
| Title: Co-Founder | 5% | 3% | 0.60 |
| Title: Software Engineer | 1% | 4% | **4.00** |
| Size: 10,001+ | 13% | 20% | **1.54** |
| Size: 11–50 | 16% | 10% | 0.63 |
| Size: 2–10 | 12% | 7% | 0.58 |
| Location: Greater Delhi | 36% | 20% | **0.56** |
| Location: Greater Bengaluru | 11% | 12% | 1.09 |
| Location: Greater Hyderabad | 3% | 5% | 1.67 |
| Industry: IT Services & Consulting | 9% | 15% | **1.67** |
| Industry: Software Development | 4% | 7% | **1.75** |

Roll-ups [inferred from listed shares]: the follower base is roughly two-thirds senior and above, about 15% founder or co-founder titled, about 40% in firms of 200 people or fewer, and about 40% in the Delhi NCR belt. Content reach is closer to one-third at firms of 1,001 or more, about 28% junior, and about 19% in the southern metros.

Named employers confirm the split. Followers skew toward Amazon, Deloitte, EY, Self Employed, Honasa, Accenture, Flipkart, TCS, Google and ICICI Bank. Reach skews toward TCS, EY, Deloitte, Coforge, Accenture, Amazon, Infosys and HCLTech. All are under 1% individually, so there is no usable concentration view.

**Read:** the account writes for an owner-operator audience and is distributed to an enterprise-IT employee audience. The follower list is who the posts are for; the reach list is who the algorithm shows them to.

## 5. What each post type is doing

Theme assignment below is manual coding of the 50 posts, not a field in the export. Treat it as a working classification.

| Theme | Posts | Sum impressions | Median impressions | Median ER (year) | Median ER (from 2026-07-18) |
|---|---|---|---|---|---|
| Faith / festival / culture | 3 | 13,283 | 3,784 | **13.77%** | 13.77% |
| Art / people portrait | 1 | 3,743 | 3,743 | 12.34% | 12.34% |
| Founder craft / operator lessons | 15 | 88,475 | 4,371 | **9.88%** | 11.21% |
| Event / ecosystem | 6 | 31,924 | 5,710 | 6.16% | 10.22% |
| Travel / places | 4 | 15,867 | 3,850 | 3.98% | 6.96% |
| Personal reflection / origin | 12 | 92,710 | 4,555 | 1.95% | 8.91% |
| India / ecosystem / policy | 5 | 90,863 | 4,163 | 1.63% | 11.74% |
| Cricket / film / celebrity | 3 | 29,003 | 9,074 | 1.22% | 4.98% |
| Brand campaign | 1 | 31,041 | 31,041 | 0.66% | — |

The year column is distorted by timing: the same theme scores very differently before and after July. Inside the recent window the spread narrows sharply and founder craft, India/ecosystem, faith and events converge in the 10–14% band. The honest conclusion is that **the era effect is larger than the theme effect**, so theme rankings from the full year should not be used to plan content.

What survives as signal:

- **Founder craft** is the only high-volume theme that also carries high engagement. Fifteen posts, the largest share of impressions among engaged content, 9.88% median for the year and 11.21% recently. This is the account's core product.
- **Faith, festival and personal-anniversary posts** produce the highest engagement rates but are low-volume and identity-driven. They build warmth, not reach.
- **India/ecosystem posts** produce the largest impressions but the weakest rate in the early period. They buy distribution, not depth.
- **Brand campaign and congratulations posts** sit at the bottom on both dimensions. They serve the relationship, not the audience.

## 6. Reach and depth trade off

| Metric | Value |
|---|---|
| Median post impressions (50-post set) | 4,659 |
| Mean post impressions | 7,938 |
| Median post ER | 5.42% |
| Mean post ER | 6.69% |
| P25 / P75 ER | 1.34% / 11.35% |
| Weighted ER across the 50 posts | 4.25% |
| Pearson correlation, impressions vs ER | **−0.311** |
| Spearman correlation | −0.446 |
| Correlation excluding the 74k post | −0.339 |

The inverse relationship is stable across methods. The five largest posts average 0.65% ER; the five smallest in the top-50 set average 13.4%. The single largest post of the year — 74,295 impressions on 2025-12-06 — did 159 engagements, or 0.21%. The highest-engagement post of the year — 1,155 engagements on 2026-09-14 — did 6,010 impressions, or 19.22%.

Concentration: the top five posts hold 36.8% of annual impressions but 21.9% of annual engagements. The top ten days hold 31.1% of impressions; the top fifty days hold 65.2%.

**Read:** reach and resonance are not the same asset here. The posts that travel are not the posts that land, and the account's best work sits at modest reach with very high depth.

## 7. Reader intent [inferred]

The export cannot link a reader to a post, so this section is interpretation built on the two demographic bases plus the theme table. It is a hypothesis to validate, not a finding.

| Reader group | Approx. share | What they come for | Which posts serve them |
|---|---|---|---|
| Founder / owner-operator core | 15% titled, 66% senior+, 40% small firms, 40% NCR | Pattern recognition and validation from someone who has built and exited | Founder craft, second-time-builder, clarity, customer-assumption posts |
| Enterprise IT and engineering layer | 20% at 10,001+, engineers 4× over-indexed | Career lessons, operating insight, a view into founder life | Founder craft, travel/life-lesson posts, India/ecosystem |
| Students and early career | 18% entry level in reach | Inspiration, career direction, proximity to builders | Origin stories, award and event posts, festival posts |
| Event and ecosystem network | Small but high-intent | Presence, association, networking | Event recaps, fireside promos, board announcements |
| Existing personal network | Not measurable from the export | Relationship maintenance | Personal reflection, congratulations, faith |

Two motives recur across the corpus and the data. The first is **learning how the game actually works** — founder craft is the only theme that is both frequently posted and consistently well received, which is what a teaching motive looks like in the numbers. The second is **affiliation** — faith, festival and India-pride posts draw engagement disproportionate to their reach, which is identity rather than information.

## 8. What this means for post design

Three practical consequences, all traceable to the data above:

1. **The core product is founder craft.** It is the theme with both volume and depth, and it matches the follower base. Every other theme is either reach-buying or relationship-building.
2. **Reach is not the target.** Optimising for impressions pushes toward India/ecosystem and celebrity content at 0.2–1.2% ER. The account's strongest work is at 3,000–6,000 impressions and 9–19% ER.
3. **Placement of any ask matters.** See §9 — the fold, not the CTA wording, is the constraint.

### 9. CTA placement note

The corpus in `13_REAL_WRITING_SAMPLES.md` contains a call to action in only 6 of 26 posts, and four of those six are event logistics rather than engagement asks. The native pattern is a post that closes on the idea. Where a question does appear, it sits at roughly 60–90% depth, at the point where the argument turns, not in a closing block.

The analytics explain why that works. The median post is 4,659 impressions and 5.42% ER, and the top-50 set is capped, so the visible sample is dominated by posts people actually read. A closing ask is seen only by readers who expand; a question placed at the argument's hinge is read by everyone who gets that far, and it performs the same function without adding length. Any future CTA test should move an existing line rather than append a block.

This also puts a caveat against `09_MANAGER_BRIEF.md` §7, which recommends ending every piece with a single call to action. That advice is not supported by the owner's own corpus or by the placement logic above.

## 10. Gaps — what this export cannot answer

| Gap | Consequence |
|---|---|
| No post × demographic cross-tab | Cannot prove which segment engages with which theme. §7 stays [inferred]. |
| No reactions / comments / reposts split | Cannot separate passive likes from intent (comments) or amplification (reposts). |
| Top-50 cap only | No long-tail view, no total post count, no worst-post baseline. |
| No per-post members reached | Reach is account-level only. |
| Demographics are percentages, top-10 only | Counts must remain [inferred]; job title coverage is 22.5% of followers and 12% of reach. |
| No education, age, gender or language | Cannot profile the audience beyond professional attributes. |
| No format, hashtag or posting-time metadata | Cannot test whether format or timing drives the July inflection. |
| Gross new followers only | Growth is an upper bound; churn is invisible. |
| Named employers all under 1% | No account-based targeting possible from this file. |
| No traffic source, saves, clicks or profile views | Cannot separate feed reach from search or profile discovery. |

Closing the first gap is the single highest-value next step. Engager-level data — names and titles on the top posts — would turn §7 from inference into evidence, and would let the theme table be tested segment by segment.

## 11. Data notes

- Every cell in the export is stored as text; all arithmetic here casts to numeric first.
- ER throughout is engagements ÷ impressions, computed, because the export has no ER field.
- "Net engagements" means LinkedIn's reported figure after reversals; positive engagements total 19,303 and reversals −53.
- Segment counts in §4 are [inferred] by applying listed shares to the stated base. They are estimates, not exported values.
- Theme coding in §5 is manual and revisable; the impression and engagement figures behind it are exact.
- `04_SOURCES.md` currently records the native analytics export as not used. That entry is now out of date and should be updated on the next pass.
