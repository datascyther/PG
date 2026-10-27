# PUBLISH — the next three posts

Everything below is written, gated 17/17, and has its image in `engine/assets/`. For each
post: open the text file, copy all of it, paste into LinkedIn, upload the one image, set
the date and time, publish. Nothing is published until Puneet replies yes for that post.

Slots are Mon / Wed / Fri, 08:30 IST. Diwali (Sunday 8 November 2026) is calendar-locked
and is not in this list.

---

## 1 · Monday 26 October 2026, 08:30 IST

**Text:** `engine/drafts/SP-006.linkedin.txt`
**Image:** `engine/assets/IMG_2519.jpg` — the wide stage shot: host in the black dress, four men, gold backdrop

Headline (already in the text, first line):
> Born Unicorn Season 1 was shot on 30 September and 1 October 2026, by a jury of six and a guest

---

## 2 · Wednesday 28 October 2026, 08:30 IST

**Text:** `engine/drafts/SP-010.linkedin.txt`
**Image:** `engine/assets/Investors Bet on Resilient Founders (real).png` — Puneet on the jury set, rebuilt as a quote card over the real frame `IMG_2579.jpg`

Headline:
> Investors don't bet on 50-page pitch decks. They bet on founders who execute through uncertainty.

Do **not** upload `Investors Bet on Resilient Founders.png` (no "(real)"). That file is
AI-generated, carries a signed C2PA manifest, and is design template only.

---

## 3 · Friday 30 October 2026, 08:30 IST

**Text:** `engine/drafts/SP-007.linkedin.txt`
**Image:** `engine/assets/IMG_2579.jpg` — two men in cream armchairs on the raised stage, the set line behind them

Headline:
> Puneet Gupta sat on the Born Unicorn jury in September and October 2026, having pitched to tables like it for years

---

## Already scheduled, not in this list

| Date | Draft | Image | Note |
|---|---|---|---|
| Mon 2 Nov | SP-001 | **none** | Clensta warehouse post. Needs a Clensta still from Puneet before it can ship |
| Fri 6 Nov | SP-002 | **none** | Clensta water post. Same blocker |
| Sun 8 Nov | SP-007-F | — | Diwali. Not started, calendar-locked to the day |
| Mon 9 Nov | SP-003 | **none** | hiring post. Needs one still |
| Wed 11 Nov | SP-004 | **none** | IIT Delhi lab post. Needs one still |
| Fri 13 Nov | SP-005 | **none** | public record post. Needs one still |
| Mon 16 Nov | SP-008 | IMG_2515.jpg | ready |
| Wed 18 Nov | SP-009 | **none** | needs one still, or reuse IMG_2515/2519 |

The five posts marked **none** pass the text gates but have no anchor image. The house
format is text + one image, so they stay held until an image is supplied. Do not publish
them text-only.

`N-01` and `N-02` are spares with no capture yet. They are not on the calendar.

---

## Do not use

| File | Why |
|---|---|
| `Investors Bet on Resilient Founders.png` | AI-generated (C2PA: ChatGPT / gpt-image, trainedAlgorithmicMedia). Synthetic likeness of a real person. Design template only |
| `3FC8FA7C-EAC2-4A33-910B-DC825DF73B1F.png` | AI-generated. Signed C2PA manifest. Never publish it as a photo of a real person |
| `IMG_2515.jpg` | a group shot of the same stage as IMG_2519; keep it for SP-008 so the two posts do not repeat |
| `IMG_2515.HEIC`, `IMG_2519.HEIC`, `IMG_2547.HEIC`, `IMG_2579.HEIC` | phone originals. Upload the `.jpg` — same photo, already upright |

## Before you publish, check four things

1. The text file was copied in full, from the first line to the last.
2. The right image is attached — the file name is listed above.
3. The image is upright and shows what the post describes.
4. Puneet has replied **yes** for this specific post.

## If you want to change a headline

Do not rewrite it in your own words. A headline is one factual line, no more than 24 words,
no hype, no question mark, no first person. It must be true and it must come from the fact
in the post. Examples that pass: "Four lakh products shipped in one Sunday shift."
Examples that fail: "The most incredible Sunday of my life."

If a headline has to change, change it in `engine/drafts/SP-00X.md` (the line starting
`# `), then run:

```bash
python3 engine/sp_engine.py gates SP-00X     # must still be 17/17
python3 engine/sp_engine.py render SP-00X    # regenerates the .linkedin.txt
```
