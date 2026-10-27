# BORN UNICORN — INTAKE

You have the raw images and the data for Born Unicorn Season 1. You do not yet have
posts. This page is the gap between the two, and it is one small job, not a project.

**The insight:** a pedia post is not a story you write. It is a **record you assemble** —
one episode, one founder, one number, one date, one picture. The raw data already holds
most of it. Your job is to line the fields up; the engine writes the prose and checks it.

---

## 1. What you already have, and what each part is for

| You have | What it becomes |
|---|---|
| Episode stills and behind-the-scenes images | **one anchor image per post**. The format is text + one image. No carousel, no video, no gallery |
| The episode data (which founder, which episode, which day, which sector) | **the headline and paragraph 1**. This is the substance of a Startup Pedia entry |
| The episode clips / rough cuts | **one quotable line per post**, if there is a line worth quoting |
| Your own notes from the shoot | the *number*: ARR, users, patents, pilots, headcount, funding |
| The show's own episode titles | the *slug* — they are usually already written as headlines |

## 2. The data contract

One row per episode. `engine/queue/bu_episodes.csv` is already created with the header
and three empty rows. Fill it in — this is the only manual step.

| Column | What goes in it | Required |
|---|---|---|
| `episode` | episode number or title | yes |
| `shoot_date` | 2026-09-30 or 2026-10-01 | yes |
| `founder` | the founder's name as it should appear | yes |
| `company` | the company name | yes |
| `city` | where they are based | yes |
| `sector` | AI, consumer, mobility, healthcare, sports, … | yes |
| `what_they_build` | one line, in plain words | yes |
| `one_number` | the single number that makes them worth a post | yes |
| `one_line_quote` | one line from the episode, in quotes | no, but it lifts the post |
| `image_file` | the filename of the still to attach | yes |
| `consent` | `yes` only if the show has cleared the founder to be profiled publicly | yes |

**`consent` is not a formality.** Startup Pedia's own model is opt-in — "DM us to get your
startup featured" — because a founder's name and numbers on a public page is a
commercial and reputational event for them. A row with `consent` blank is skipped by the
converter and listed back to you. Get the show team to confirm which founders are
cleared; that is one message, not a project.

## 3. Run it

```bash
cd /Users/mymac/PG/startup-pedia-engine

python3 engine/bu_convert.py --dry-run     # see what would be created, nothing blocked
python3 engine/bu_convert.py               # create the drafts
python3 engine/sp_engine.py board          # they appear in the queue
python3 engine/sp_engine.py render SP-008  # check one, see what is still missing
```

The converter writes the first-pass prose from your columns and registers a new moment
(`N-xx`) and a new receipt (`R-xx`) for each episode, so the gate ladder accepts the
source ids. It also assigns the Mon/Wed/Fri slot.

**Then the only work that is yours is editing the draft.** The gates will tell you what
is missing:

```
[FAIL] G14  no placeholder paragraphs left
          stub paragraphs: [2]
```

`TODO_` in a paragraph means a field was empty in your CSV. The gates will not let an
incomplete post render — that is the point of the lock.

## 4. What the post looks like once the fields are filled

> **Pune-based Sample Co pitched in Born Unicorn Season 1**
>
> Sample Co was one of the founders who pitched in Born Unicorn Season 1 on 2026-09-30.
> It builds an engine that drafts and tests API integrations. [N-01]
>
> AI company, founded by Sample Founder. [R-69]
>
> By the pitch stage the company reported 3 paying teams. [R-69]
>
> In the episode, Sample Founder said: "you can watch the agent work" [R-69]
>
> Born Unicorn Season 1 was shot on 30 September and 1 October 2026, with a jury of six
> and episodes produced across five sectors. [R-60]
>
> Filed under: Startup Stories — Born Unicorn Season 1, 2026.
>
> #buildinindia #startupstories #iitdelhi

Then you attach the one image, paste the text, and it goes out on the slot.

## 5. Two posts that are already written, from public material only

You do not have to wait for the data to start. These are drafted and gated today:

| ID | Slot | What it is |
|---|---|---|
| SP-006 | Mon 27 Oct | The season as a record — two shooting days, the jury of six, the guest jury, five sectors, AIC IIT Delhi, the crew working to 2 AM |
| SP-007 | Fri 30 Oct | Puneet on the jury side of the table — the same record, from his side of it |

Both use only facts that are already public in his own published posts, and both are
listed in the anchor bank as `N-01` to `N-05` and `R-60` to `R-68`.

## 5b. Two image rules the dump taught us

**Rule 1 — check provenance, not just pixels.** One file in this dump
(`3FC8FA7C-EAC2-4A33-910B-DC825DF73B1F.png`) is AI-generated and carries a signed C2PA
manifest naming ChatGPT / gpt-image. It looks exactly like a frame from the shoot, because it
was built from the real photographs. A synthetic image of a real, identifiable person is
never an anchor image and is never captioned with a real face. Read the C2PA/EXIF metadata on
every incoming file.

**Rule 2 — look at the converted file, do not trust the converter.** `sips -s format jpeg`
silently dropped the EXIF orientation tag on three of the four HEICs and left them sideways,
while getting the fourth right. The working conversion is:

```bash
ffmpeg -y -i IMG_2519.HEIC -frames:v 1 -q:v 2 IMG_2519.jpg
```

Then open the JPG and look at it. An upright frame is 3024x4032.

## 6. The image rule

One image per post, and it must be **the right kind of image**:

- a still of the founder or the product — not a group photo, not a logo, not a frame from
  someone else's post;
- landscape, at least 1200 px wide;
- no text on it that a caption would repeat;
- **never a frame that carries the paused 2008–2016 chapter.** His own Born Unicorn wrap
  post mentions defence, and the pedia version of it must not. If a still shows anything
  from that chapter, it does not run.

The engine records the chosen file in the draft's `image:` field and prints it on the
review card, so nothing gets published with the wrong picture attached.

## 7. The order of work, in order

1. Fill `engine/queue/bu_episodes.csv` — one row per episode, `consent=yes` only where cleared.
2. Run `bu_convert.py`.
3. Open each draft, fix the TODOs, replace the generated headline with a better one.
4. `render` each one, read the review card, attach the image.
5. Send the batch to the founder as one approval, not one at a time.

That is the whole job. The prose, the sourcing, the checks, the slots and the log are
already built.
