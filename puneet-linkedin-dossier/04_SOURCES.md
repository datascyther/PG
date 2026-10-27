# 04_SOURCES.md — All Sources Used

> **INTERNAL ONLY — DO NOT SHARE.** Unredacted source ledger: contains fund URLs, partner names, and contact details. Not for external distribution.

## Primary (local)
- `../pg.pdf` — LinkedIn PDF export, 4 pages. Contains: contact, Top Skills, Languages, Honors-Awards, Publications, Patents, Name/Headline/Location/Summary, 9 Experience roles, 4 Education entries. Parsed 2026-10-16. **Most complete / authoritative for profile.**
- No screenshots / manual HTML saves yet. Recommended: save `pg.pdf` SHA + export date alongside.

## Live LinkedIn (guest fetch, no login, 2026-10-16)
- Profile: https://www.linkedin.com/in/puneetgbuilds/ → **HTTP 999** (blocked, anti-bot). Confirms Method 1 limitation: main profile sections (About, Experience, Education, Skills, Recommendations, connection count) cannot be guest-scraped at scale; use PDF export instead.
- Canonical mirror: https://linkedin.com/in/puneetgbuilds (same, indexed 2026-10-11 via search)
- Post P1 (FULL fetch OK): https://www.linkedin.com/posts/puneetgbuilds_i-was-wrong-and-i-need-to-say-this-out-loud-activity-7348658710925168640-MpHi → 112 reactions, 48 comments, follower count 28,471, 1,349 Posts, 7 Articles. Proves individual `/posts/` URLs ARE guest-fetchable.
- Author articles index (requires login for full list): https://www.linkedin.com/today/author/puneetgbuilds
- Recent activity (requires login): https://www.linkedin.com/in/puneetgbuilds/recent-activity/
- All 22 post URLs: see `02_POSTS.md` / `03_POSTS.csv`. Each individually re-fetchable via `05_PIPELINE.py`.

## Secondary (web enrichment)
- https://puneetgupta.org/ — personal site: second-time founder, $30M+ raised, $100M+ enterprise value, 500+ team, IIM Calcutta / GGU DBA.
- https://falconinnovationfund.com/ (via Experience description) — $100M fund context.
- https://www.iimcal.ac.in/puneet-gupta-pgdm-46th-batch-comes-waterless-bathing-products — IIM Calcutta alumni story (waterless bath origin, Army/Navy induction).
- IIM Calcutta alumni news snippet (waterless tech accepted by Army Design Bureau).
- Search discovery queries used: `Puneet Gupta Clensta linkedin puneetgbuilds posts`, `"puneetgbuilds" linkedin Stealth AI Falcon`, `site:linkedin.com/posts/puneetgbuilds`, `Puneet Gupta Clensta Founder education IIM Calcutta`.

## Native LinkedIn analytics (owner-supplied, PRIMARY metrics source)
- `../AggregateAnalytics_Puneet Gupta_2025-10-20_2026-10-19.xlsx` — LinkedIn native export, 6 sheets (DISCOVERY, ENGAGEMENT, TOP POSTS, FOLLOWERS, AUDIENCE DEMOGRAPHICS, CONTENT DEMOGRAPHICS), period 2025-10-20 → 2026-10-19, read-only, every cell stored as text. **USED and authoritative** for impressions, engagements, ER, follower counts and demographics. It supersedes live guest-fetch follower counts (28,485 on 2026-10-19 vs 28,471 on 2026-10-16 vs 27,643 in a later third-party scrape — the native export is the number of record). Analysis: `14_AUDIENCE_MAPPING.md`. Structural limits: top-50 post cap, no per-post timestamps, no engagement split, no post × demographic cross-tab, no long tail.
- Duplicate copy `...(1).xlsx` in the same folder — same export, keep only one.

## External press and official publications (collected 2026-10-21 — Tier B receipts)
- Business Standard — Clensta acquisition, $36M valuation, adviser, "waterless man" (2025-07-08/09): https://www.business-standard.com/content/press-releases-ani/puneet-gupta-steps-down-as-ceo-after-clensta-s-acquisition-125071000008_1.html
- Tribune India — same release (2025-07-09): https://www.tribuneindia.com/news/business/puneet-gupta-steps-down-as-ceo-after-clenstas-acquisition
- PTI News / ThePrint (ANI release) — same coverage: https://www.ptinews.com/press-release/puneet-gupta-steps-down-as-ceo-after-clensta's-acquisition/2713037 · https://theprint.in/ani-press-releases/puneet-gupta-steps-down-as-ceo-after-clenstas-acquisition/2684902
- IndianStartupNews — Series A ₹20 cr, IIT-Delhi and DST backing, 30+ products, growth figures (2021-12-08): https://indianstartupnews.com/news/iit-delhi-backed-clensta-raises-rs-20-crore-led-by-venture-catalyst-and-ipv
- BW Disrupt — pre-Series A valuation, founding team, 2017 customer supply: https://www.bwdisrupt.com/article/biotechnology-startup-clensta-raises-pre-series-a-round-at-rs-25-cr-valuation-134267
- IIT Madras press release — unit volumes, per-use quantity, IIT-Delhi sweat equity: https://www.iitm.ac.in/happenings/press-releases-and-coverages/startups-partner-iits-develop-cutting-edge-niche-products
- Mediabrief — founder interview, origin of the waterless category (2021-05-12): https://mediabrief.com/exclusive-puneet-gupta-clensta-international/
- Silicon India — "The Man Who Builds Anyway" profile (2026-04-09): https://www.siliconindia.com/news/general/the-man-who-builds-anyway-puneet-gupta-on-passion-policy-rooms-and-why-15-years-of-real-exposure-beats-any-shortcut-nid-240127-cid-1.html
- Inc42 — founder/keynote profile: https://inc42.com/author/puneet-gupta · company people: https://inc42.com/company/clensta/people
- Tracxn — company profile, investors, incubators: https://platform.tracxn.com/a/d/company/59ae0fafe4b0428d95a18a3f/clensta
- Economic Times — 40 Under Forty winners 2019: https://economictimes.indiatimes.com/winners-2019/40-under-forty-celebrating-young-leaders/slideshow/70838913.cms
- These back receipts R-19 to R-26 in `15_REAL_WORLD_ANCHORS.md`. Buyer names, investor names and the adviser are held at `ASK` and need the owner's clearance.

## What was NOT used / still needed
- Screenshots / PDFs of post pages (recommended for audit trail — see pipeline `--archive`).
- Authenticated scrape (login cookies) for: full 1,349 posts, likes/comments/shares per post, images/links, Skills endorsements, Recommendations, connection count.
- LinkedIn official data export (owner): Settings > Data Privacy > Get a copy of your data — preferred compliant path for complete posts.
- LinkedIn API (Marketing Developer Platform / unlisted UGC endpoints) — requires app approval.
- **17 of the 50 posts in the native export have no body in the dossier** (URL slug only, all from the pre-2026-07-18 era). URLs are known and `/posts/` URLs are guest-fetchable, so these are recoverable — see `15_REAL_WORLD_ANCHORS.md` §6.

## Reproducibility
1. `python 05_PIPELINE.py --post-urls post_urls.txt --out 03_POSTS.csv` re-fetches each post as guest.
2. Re-run `websearch` queries above to discover new posts; append to CSV.
3. Keep `pg.pdf` as ground truth for profile; do not overwrite with scraped fragments.

## Compliance note
LinkedIn ToS discourages automated scraping; guest fetch of your own public dossier for research is low-risk but can 999-throttle. Prefer official export/API for bulk. Add delays, cache, and respect `robots.txt`. Script includes throttling + user-agent rotation hooks.
