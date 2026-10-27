# ASSETS GUIDE — how the raw dump becomes posts

The founder's office now has every raw image, video and recording behind the existing
content. That dump is not the problem. The problem is turning 500 files into 20 sourced
facts without reading 500 files.

**One asset → one moment → one receipt → one post.** If an asset does not carry at least
one of {place, date or year, number, named person, object, named decision}, it is not a
post. It is a footnote, and it goes in the queue, not on the calendar.

---

## 1. The folder convention

```
engine/assets/
  2026-10-11_interview_r1/
    2026-10-11_r1_take1.mp4
    2026-10-11_r1_take1.md      <- sidecar, one per asset
    2026-10-11_r1_take2.mp4
  2026-10-19_offsite/
    ...
```

The folder name carries the date and the context. The sidecar carries the facts. No
sidecar, no post — the scan will still index the file and produce a card, but the card
will have empty fact fields, which means "not ready".

## 2. The sidecar

One plain markdown file per asset, same name plus `.md`. Seven fields. Any field can be
empty, but the first four are what make an asset usable.

```markdown
date: 2026-10-11
place: IIT Delhi, Department of Management Studies
who: 120 students, Prof Rangan Banerjee
what_happened: talked on how great products get built, then took questions
quotable_line: the room asked what to do when the first version is not good enough
number: 120
source: own recording
```

`engine/sp_engine.py scan engine/assets` reads these, writes an extraction card per asset
with the ffprobe metadata and the extracted keyframes, and lists everything in
`engine/queue/assets.csv`.

## 3. What to do with each asset, in order

| Step | Command | What you get |
|---|---|---|
| index | `python3 engine/sp_engine.py scan engine/assets` | `queue/assets.csv`, one card per asset, keyframes pulled out of every video |
| read the card | open `queue/cards/A-xxxx.md` | the frames, so you can see what the clip actually contains without scrubbing the file |
| fill the facts | edit the sidecar | date, place, who, what happened, a quotable line, a number, a source |
| promote to a moment | add an `N-xx` row to the bank, or use an existing `M-xx` | the moment becomes citable |
| draft | `python3 engine/sp_engine.py new --moment M-xx --format P` | a draft shell with the gate ladder attached |
| write | edit `drafts/SP-xxx.md`, tagging every paragraph with `[M-xx]` / `[R-xx]` / `[A-xx]` | the post |
| check | `python3 engine/sp_engine.py gates SP-xxx` | 16 gates, pass or fail, with the reason |
| render | `python3 engine/sp_engine.py render SP-xxx` | `SP-xxx.linkedin.txt` (paste-ready) and `SP-xxx.card.md` (review card) |
| approve | `python3 engine/sp_engine.py approve SP-xxx` | status moves to approved |

## 4. The triage rule — how to spend the time

Not every asset deserves an afternoon. Sort the dump by this, and work top-down:

| Tier | Test | Action |
|---|---|---|
| **A** | has a date + a named person + a number | write it this week |
| **B** | has a date + a number, no person | write it, but keep the person out unless it is cleared |
| **C** | has a date only | mine it for a single fact, then reuse it in a bigger post |
| **D** | no date, no number, no person | park it. It is stock footage, not a story |

A 60-second clip with a date, a room and one number is worth more than a two-hour
keynote recording, because the post is built from the fact, not the length of the file.

## 5. Freshness and dating

- **A post built from a fresh event** must be published within 7 days of the event
  (publish date − subject date ≤ 7 days). A 48–72 hour hold does not fix a stale
  subject; strip the relative time instead ("last Sunday" → "on 11 October") or kill it.
- **Batch posts are evergreen by construction** — absolute years, no relative time, no
  dated event. That is why a two-week batch can be approved on the 20th for a 27th
  slot.
- Relative language is banned in the draft: "yesterday", "last week", "recently",
  "this month". Use the date.

## 6. Capturing new material without a recording

The best material is a voice note with a scene in it. The standing prompt, sent at 07:45
and caught on Saturday:

> One thing that happened today — a scene, a number, or a decision. One voice note, no editing.

"Nothing today" is a valid answer and needs no follow-up.

## 7. Rules that travel with the assets

- The current venture is referred to only as the current stealth AI venture. No product,
  partner, customer, investor, competitor or fund name, ever, including in a filename
  that ends up in a caption. The engine blocks the known names (G13); the human has to
  catch the new ones.
- The 2008–2016 chapter is paused. No defence or military vocabulary, no named military
  locations, in any caption, any frame, any alt text.
- Historical ventures (Clensta, Honeywell) may be named, always with a year anchor.
- Nothing is published from an asset the founder has not seen. Approval is his word, not
  an inference.
