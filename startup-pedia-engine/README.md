> **INTERNAL ONLY — DO NOT SHARE.** This folder contains derived working material
> from the owner's internal dossier (anchor bank, corpus 5-gram index, receipts). Not for
> external distribution. Owner-only permissions are intentional.

# startup-pedia-engine

Content engine for **Puneet Gupta's personal LinkedIn**, built for the new direction:
raw founder media → dated, sourced, third-person records in the **Startup Pedia** house
format, published on a Mon/Wed/Fri cadence, and cut across five surfaces.

The engine is the anti-fabrication lock. A paragraph cannot render without a source id
pointing at the anchor bank (`M-xx` moment, `R-xx` receipt) or at a raw asset (`A-xx`).
The gate ladder refuses anything that breaks the format, reuses his own language, or
names something that has not been cleared.

---

## Quick start

```bash
cd /Users/mymac/PG/startup-pedia-engine

python3 engine/sp_engine.py init          # create the structure
python3 engine/sp_engine.py facts         # rebuild facts.json from the dossier
python3 engine/sp_engine.py scan engine/assets   # index the raw dump
python3 engine/sp_engine.py board         # what is in flight
python3 engine/sp_engine.py gates SP-001  # 16 gates, pass/fail with reasons
python3 engine/sp_engine.py render SP-001 # paste-ready text + review card
```

## What is in here

| Path | What it is |
|---|---|
| `FORMAT_SPEC.md` | the anatomy of a pedia post, both families, all 16 gates, what we do not copy from Startup Pedia |
| `LINKEDIN_STRATEGY.md` | cadence, the fortnight plan, one post → five surfaces, governance, what is deliberately not done |
| `ASSETS_GUIDE.md` | folder convention, sidecar format, triage tiers, freshness rule, capture protocol |
| `BU_INTAKE.md` | **Born Unicorn Season 1** — the data contract, the consent gate, the one manual step, the 3-command run |
| `engine/sp_engine.py` | the CLI: init · facts · scan · new · gates · render · board · approve · publish · kill |
| `engine/bu_convert.py` | turns the Born Unicorn episode CSV into pedia drafts, one per episode, with new source ids |
| `engine/config/gates.json` | the gate thresholds per family |
| `engine/config/names_allowlist.txt` | every proper name that may appear, with its clearance flag |
| `engine/drafts/` | drafts, the rendered post, and the review card |
| `engine/queue/` | asset index, extraction cards, keyframes |
| `engine/facts/` | the machine-readable anchor bank and the corpus 5-gram index |
| `engine/publish_log.csv` | what shipped, with impressions, engagements and ER |

## The drafts that exist today

| ID | Slot | Family | Subject | What it is |
|---|---|---|---|---|
| SP-006 | Mon 26 Oct | P | Born Unicorn | the season as a record: two shooting days, the jury of six, five sectors, the crew working to 2 AM |
| SP-010 | Wed 28 Oct | N | Puneet | the jury lesson: investors bet on founders who execute through uncertainty |
| SP-007 | Fri 30 Oct | P | Puneet | the jury side of the table, from his side of it |
| SP-001 | Mon 2 Nov | P | Clensta | four lakh products out of the door on one Sunday shift, October 2023 |
| SP-002 | Fri 6 Nov | P | Clensta | one billion litres of water saved, April 2026 |
| SP-003 | Mon 9 Nov | P | Puneet | a thousand hires, and the speed of hiring |
| SP-004 | Wed 11 Nov | P | Puneet | a company that began in an IIT Delhi lab |
| SP-005 | Fri 13 Nov | P | Puneet | the founder entry: nine dated roles, 2007 to 2026 |
| SP-008 | Mon 16 Nov | P | Born Unicorn | the line on the set wall |
| SP-009 | Wed 18 Nov | P | Born Unicorn | the platform's first season: the funnel, the dates, the China trip, the ₹10 crore |
| SP-011 | Fri 20 Nov | P | Born Unicorn | the room as a record — six jurors, one guest, a table that worked on paper (**held on third-party consent**) |
| SP-012 | Mon 23 Nov | N | Puneet | the notebook: a pitch is ninety seconds, and the note that changes an answer |
| SP-013 | Wed 25 Nov | P | Rahul Agarwal | the mentor behind the table, 100+ entrepreneurs, with a juror listening |
| SP-014 | Fri 27 Nov | P | Born Unicorn | the guest seat: AIC IIT Delhi's CEO on the jury, and a mixed panel |

All fourteen pass 17/17 gates and carry zero 4-gram overlap with his published writing.
SP-003 and SP-005 still need one confirmation from the founder before they can be
scheduled. SP-011 is held until the other juror in the frame consents, or the show
releases it. See the review card for each.

**Two documents to read before writing anything new:**

- `THREE_FRAMES_BRIEF.md` — what the three stills of 1 October 2026 are worth, what they
  cannot prove, the consent trap on the strongest frame, and the honest ceiling on how
  many posts one event can carry.
- `BATCH_B_FOUR_SAMPLES.md` — the four samples of Batch B, paste-ready, each with what it
  still needs.


## The two things it needs from a human

1. **The raw dump.** Drop it in `engine/assets/` with the sidecar files described in
   `ASSETS_GUIDE.md`, then run `scan`. The dump was not shared when this was built, so
   the pipeline is written against a folder rather than against the files.
2. **One decision on the brand.** Is "Startup Pedia" usable on his personal profile? The
   answer changes one hashtag and one closing line in every post in the batch. The
   engine warns (G13b) rather than blocking, because the answer is not the engine's to
   give.

## What it deliberately does not do

- It does not publish. Ever. It renders text for a human to paste, and it keeps a log.
- It does not write from an idea. No source id, no render.
- It does not use the owner's own sentences. A 5-gram match against his published corpus
  fails the draft.
- It does not name the current venture, its products, partners or investors.
