> **SUPERSEDED 26 Oct 2026.** This file was written for the earlier direction (defence paused,
> manufacturing / consumer framing). The owner re-enabled defence and set five domains: defence,
> entrepreneurship, investor, founder, AI. Current sources: `presentation/DECK.html` and
> `09_IDEATION_PLAN.md`. Kept for history only.

# 08 — WORKED EXAMPLES

Three assets, fully written, all three passing the gate ladder. They exist to prove the
structure is executable, not to be published as they stand — each one has a short list of
things only the founder can answer.

| File | What | Slot | Gates |
|---|---|---|---|
| `drafts/YT-001.md` | On the Floor — the festival Sunday warehouse shift | Wed 4 Nov 2026, 19:00 | 13 pass, 1 warn (open questions), 0 fail |
| `drafts/IG-R001.md` | Reel — 20 ml replaced an entire bath | Fri 6 Nov 2026, 08:30 | 14 pass |
| `drafts/IG-C001.md` | Carousel — 20 patents, and the line | Mon 9 Nov 2026, 08:30 | 14 pass |

Run them yourself:

```bash
cd /Users/mymac/PG/youtube-instagram-engine
python3 engine/yg_gate.py check drafts/*.md
```

---

## 1. One moment, three assets

All three come from two moments that are already in the anchor bank. Nothing was invented
for the exercise.

| Asset | Moment | Receipts | What it uses |
|---|---|---|---|
| YT-001 | M-28 — the warehouse, Sunday 29 Oct 2023 | R-06 — 4 lakh products shipped | the scene, the number, the team |
| IG-R001 | M-50 — the milestone post, 22 Apr 2026 | R-22 (~2 lakh units a month, 20 ml a use), R-42 (1 bn litres) | the product, the volume, the result |
| IG-C001 | M-46 — the IIT Delhi post, 22 Jul 2026 | R-08 (~20 patents, 6 technologies), R-43 (the campus origin) | the origin, the patent count, the gap |

Note what is **not** used: no invented dialogue, no invented detail about the warehouse, no
"one day I walked in and…". The only line that is his and not yet written is flagged as
`[ASK]` inside the script, because it cannot be sourced — it is his to say, not ours to write.

---

## 2. How the script is tagged

The LinkedIn engine tags every paragraph with a source id. Video does the same, per beat:

```
## BEAT 5 — the number (2:15–2:45) [R-06]
```

Meaning: everything spoken in that beat rests on R-06. If a sentence in beat 5 needs a fact
R-06 does not carry, the sentence moves to a beat that has the right receipt, or it is cut.

Three tags exist beyond the source id:

| Tag | Meaning |
|---|---|
| `**NOTE**` | direction to the founder or the editor, never spoken |
| `[ASK]` | an open question. The gate warns, and the script is not shootable until answered |
| `[derived: illustrative]` | a framing that is not a fact and not his words — allowed once per script, never twice |

---

## 3. What each example still needs

### YT-001 — the warehouse

- the name of the person at the packing table and whether she will be on camera
- written site permission before the shoot day
- his own one-sentence version of beat 6
- whether the warehouse can be named, or only described

The script deliberately documents nothing it cannot support — no colour of the crates, no
time anyone arrived, no number of staff in the room. That is why it reads thinner than the
final episode: the body arrives from the recorded answers, and those do not exist yet.

### IG-R001 — the reel

Sourced entirely from R-22 and R-42. The one line to check before publication is the
"twenty millilitres a use" phrasing, which is the receipt's own wording and should be spoken
as fact, not as a claim about a specific product range.

### IG-C001 — the carousel

The slide copy is written; the design pass is not. Seven slides, 4:5, house typeface, one
accent colour, no stock photography. Slides 3, 4, 5 and 6 are argument, not fact, which is
allowed — but every number on the carousel traces to R-08 or R-43.

---

## 4. The gate output, verbatim

```
IG-C001.md  20 patents left a lab. The line is the hard part
  [PASS] VG1    runtime not applicable to a still format — n/a
  [PASS] VG2    hook <= 12 words, not a question — 7 words: Six technologies, about twenty patents, one campus.
  [PASS] VG3    title <= 60 chars, has a number, no question — 48 chars
  [PASS] VG4    every beat carries a source id from the bank — clean
  [PASS] VG5    no held-chapter vocabulary — clean
  [PASS] VG6    no current-venture or counterparty names — clean
  [PASS] VG7    no placeholders left — clean
  [PASS] VG8    last spoken line is not a question or a request — clean
  [PASS] VG9    3-5 hashtags, all lowercase — 4 tags
  [PASS] VG10   caption first line carries a number — 20 patents out of one campus...
  [PASS] VG11   no 4-gram reused from his published writing — clean
  [PASS] VG12   thumbnail <= 5 words — 3 words: THE MISSING LINE
  [PASS] VG13   format is a live format — carousel
  [PASS] VG14   domain declared and live (1-6) — 3
  14 passed, 0 warn, 0 failed
```

### The three things the gate caught during this pass

Worth recording, because they are the errors a human reviewer misses on video:

1. **A spliced number.** The first reel draft said "one bath takes roughly a hundred and fifty
   litres" — a true fact with no receipt in the bank. Rewritten around the sourced figure
   (20 ml a use, ~2 lakh units a month).
2. **An echo of his own line.** "One billion litres of water" is a four-gram he has already
   published. Changed to "saved a billion litres". On video this is the error nobody catches,
   because the presenter sounds right.
3. **A borrowed legalism.** "A patent is the right to stop someone else" was too close to his
   own phrasing. Rewritten to "stops someone else from using an idea".

A fourth check failed and stayed: the title "Four lakh units…" was spelled out and had no
digit, so the gate now accepts spelled numbers. That is a fix to the gate, not to the script.

---

## 5. What a full episode adds

These examples are short by design. The formats in `03_YOUTUBE.md` are longer, and the extra
minutes come from three places only:

- **the recorded answers** — the packer, the plant head, the guest
- **the object on camera** — hands, tape, the line, the bay door, held for longer than feels
  comfortable
- **the receipt explained** — where the number came from and why it is trustworthy

Never from a longer script. A long episode with a thin script is a short episode with padding.
