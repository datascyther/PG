# 06_DATADICTIONARY.md — Field Definitions

> **INTERNAL ONLY — DO NOT SHARE.** Unredacted working file: contains venture/product names and partner references. Not for external distribution.

Covers `01_PROFILE.md` entities and `03_POSTS.csv` columns.

## Profile fields (`01_PROFILE.md`)

| Field | Definition | Source | Notes |
|---|---|---|---|
| Name | Full display name | pg.pdf p1 | Puneet Gupta |
| Headline | LinkedIn headline (220 chars) | pg.pdf p1 | Founder, Stealth AI \| Member@SPC \| National Awardee |
| Location | Free-text location | pg.pdf | Gurugram, Haryana, India |
| Summary/About | Long-form bio + awards list | pg.pdf p1 | 20+ awards enumerated; keep verbatim |
| Experience.title / company / dates / duration / location / description | One block per role (9 total) | pg.pdf pp1-3 | Dates may show future months (export artifact); preserve verbatim, flag in analysis |
| Education.school / degree / field / dates | 4 entries | pg.pdf pp3-4 | DBA In Progress (GGU), MBA (IIM-C), Instrumentation (AIT), Non-Medical (SBM) |
| Top Skills | 3 tags from export sidebar | pg.pdf p1 | Private Equity, Venture Capital, Strategy |
| Languages + proficiency | Self-reported | pg.pdf p1 | EN/HI Full Professional, JA Elementary |
| Honors-Awards | Sidebar list | pg.pdf p1 | 5 items; overlaps Summary awards |
| Publications | Titles only | pg.pdf p1 | Waterless Body Bath and Shampoo |
| Patents | Titles only (no numbers in export) | pg.pdf p1 | 5 items; numbers require USPTO/Indian Patent search |
| Follower count | Public counter on post pages | live guest fetch | 28,471 (Oct 2026); volatile — re-fetch, timestamp it |
| Post/Article counts | Public counters | live guest fetch | 1,349 Posts / 7 Articles; only 3 article titles known |
| Connection count | N/A in export | — | Requires login; leave null, do not guess |
| Recommendations / endorsements | N/A in export | — | Requires login |

## Posts CSV (`03_POSTS.csv`)

| Column | Type | Definition | How obtained | Missing-value code |
|---|---|---|---|---|
| post_id | string | `P1…P22` local key (or LinkedIn activity ID via pipeline) | Assigned during discovery; pipeline uses `activity-(\d+)` | — |
| url | URL | Canonical public post URL | websearch discovery; verified fetchable | — |
| date_published | ISO date `YYYY-MM-DD` | Original publish date | Search snippet or `<time datetime>` / JSON-LD `datePublished` | empty = confirm via fetch |
| title_snippet | string | First ~80 chars / search title | `og:title` or snippet | — |
| likes | int | Reaction count | Guest page regex (`… Reactions`) | `n/a` = not yet fetched (login or re-run pipeline) |
| comments | int | Comment count | Guest page (`N Comments`) | `n/a` = same |
| shares | int | Repost/share count | Guest pages hide this | `n/a` (login required) |
| has_image | yes/no | Whether `og:image` present | Parser | empty if unfetched |
| notes | string | Provenance: FULL TEXT vs snippet, context tags | Manual | — |
| (pipeline only) text_full | long text | Complete post body (up to 8000 chars) | `og:description` + `<article><p>` fallback | empty on 999 throttle |
| (pipeline only) error | string | Fetch error (e.g. HTTP 999) | Script | empty = OK |

## Conventions
- `n/a` = field exists on LinkedIn but needs login / re-fetch (not zero).
- Dates: trust post-page `<time>` over search-index date when they conflict (see P16).
- Dedupe key: `url` (activity ID embedded). Search may surface same post twice with different slugs — normalize on activity ID.
- Do not fabricate engagement numbers; leave `n/a` until `05_PIPELINE.py` fills them.
- PII: only public professional data retained; no emails except publicly posted business contact (Falcon fund); no phone scraping.
