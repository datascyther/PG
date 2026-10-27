> **INTERNAL ONLY — DO NOT SHARE.** This folder carries derived material from the owner's
> dossier (anchor bank, receipts, clearance flags). Owner-only permissions are intentional.

# youtube-instagram-engine

The video and image structure for **Puneet Gupta's personal YouTube and Instagram**.

One content strategy across five domains: defence, entrepreneurship, investor, founder and AI.
Defence gives the channels their edge; the other four make them his and widen the audience
(about 40% defence, 60% the rest).

It sits beside the LinkedIn engine and shares its spine:

| | LinkedIn | YouTube / Instagram |
|---|---|---|
| folder | `startup-pedia-engine/` | `youtube-instagram-engine/` (this) |
| unit | a post | an episode, a reel, a carousel |
| proof | source id per paragraph | source id per beat |
| source of facts | `puneet-linkedin-dossier/15_REAL_WORLD_ANCHORS.md` | same file, same IDs |
| rule | no source id, no render | no source id, no shoot |

Nothing here publishes. It produces scripts, shot lists, titles and captions for a human to
read, shoot and upload.

---

## Read in this order

| # | File | What it settles |
|---|---|---|
| 0 | `00_DECK_AUDIT.md` | what the colleague's deck says, slide by slide, and what we keep, change or drop |
| 1 | `01_POSITIONING.md` | who the channel says he is — three options, one recommended, one switch |
| 2 | `02_DOMAIN_MAP.md` | **the add-on**: the seven domains, their receipts, and which are live, held or blocked |
| 3 | `03_YOUTUBE.md` | 8 formats rebuilt for those domains, episode anatomy, titles, thumbnails, Shorts |
| 4 | `04_INSTAGRAM.md` | the grid, reels, carousels, captions, stories, and the one-handle question |
| 5 | `05_CADENCE.md` | the fortnight, the slot board, the approval model inherited from LinkedIn |
| 6 | `06_PRODUCTION.md` | the deck's "Prod / Process" slide made concrete: shoot day, edit, naming, assets |
| 7 | `07_GOVERNANCE.md` | held chapter, consent, NDA, clearance flags, what never ships |
| 8 | `08_WORKED_EXAMPLES.md` | one episode, one reel, one carousel — fully written, fully sourced |

Templates: `templates/youtube_episode.md`, `templates/reel_script.md`,
`templates/carousel.md`.
Board: `BOARD.csv` — every slot, its status and what it is waiting on.
Validator: `engine/yg_gate.py` — the 14 gates, run before anything is shot.

```bash
python3 engine/yg_gate.py check drafts/YT-001.md
python3 engine/yg_gate.py board
```

## The presentation

Two separate decks, two separate channel plans (HTML only; arrow keys, `F` for fullscreen):

- `presentation/DECK_PERSONAL.html` (17 slides): **@puneetgbuilds**, personal YouTube + Instagram.
  One track, five pillars (one per domain), same pillars on both platforms, about 40% defence. Script:
  `presentation/SLIDE_SCRIPT_PERSONAL.md`. Guide: `10_BLUEPRINT_PERSONAL.md`.
- `presentation/DECK_PODCAST.html` (15 slides): **Podcast with Puneet**, its own YouTube channel and
  clips handle. Script: `presentation/SLIDE_SCRIPT_PODCAST.md`.
- `presentation/build_decks.py` regenerates both decks. The earlier combined 35-slide deck and
  script are in `presentation/archive/`.
- `09_IDEATION_PLAN.md` is the idea bank behind every pillar.

---

## The three decisions this structure cannot make for you

1. **Chapter D.** The deck's entire positioning is one domain. The owner's standing rule has
   that chapter paused. Until he says otherwise, Chapter D is written, held and not shot.
   See `07_GOVERNANCE.md` §1. One word from him turns it on.
2. **One handle or two.** The deck asks for "a dedicated Instagram page for podcast shorts".
   A second handle splits a young audience in half. Recommendation in `04_INSTAGRAM.md` §6.
3. **The guest list.** A podcast about people is only as good as who sits down. The deck's
   guest categories follow the held chapter. `02_DOMAIN_MAP.md` §8 gives the live list; the
   names still need his yes.

## What this deliberately does not do

- It does not write the held chapter's content, not even as a placeholder.
- It does not name the current venture, its products, partners, investors or fund. NDA.
- It does not invent guests, episodes, numbers or scenes. A beat without a source id is cut.
- It does not copy the deck's production claims it cannot support (e.g. a 60-75 minute
  podcast needs a set, a crew and a guest pipeline that do not exist yet — see `06_PRODUCTION.md` §2).
