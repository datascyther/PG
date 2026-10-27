# 07 — GOVERNANCE

The LinkedIn engine's rule is simple: no source id, no render. Video needs the same rule,
plus three it has never needed — consent, release, and a switch.

---

## 1. Chapter D — the switch

**State: HELD.** The owner's standing rule pauses that chapter until he explicitly re-enables
it. Until then:

- no script, title, thumbnail, caption, comment, pinned reply or story frame uses its vocabulary
- no named location from it
- no guest is booked from it
- the episode slate in `00_DECK_AUDIT.md` stays unshot

**What turns it on:** one explicit instruction from the owner, in the meeting, on the record.
Not "the deck says so", not "the client wants it", not an inference from a brief.

**What happens when it turns on:** it becomes **one series inside Option C**, not a
re-positioning. It gets its own gate list, its own clearance pass, and it does not re-tune the
channel's other six domains. The reason is structural: a channel built on a single restricted
topic has one point of failure, and this one has already failed once.

---

## 2. Consent — the highest-risk surface

A podcast puts other people's faces, voices and claims on his channel permanently. Four rules:

1. **Written release before recording.** Scope: the name that may be used, the company that may
   be named, whether figures may be quoted, and the right to withdraw before publication.
2. **A face is never named from a photograph.** A name comes from a person's own public
   announcement or from their release — never from our recognition of them in a frame.
3. **A frame with an unnamed third party is held** until that person consents or the event
   organiser releases it. The dossier's own case: the strongest photograph in the dump was
   also the only one showing an unidentified second person. Cropping to keep the name kept the
   stranger; the derived 4:5 crop that removed the stranger was the publishable version.
4. **A founder is named only if they announced it themselves**, and then the episode cites their
   announcement rather than presenting it as our finding. This is how a media platform covers a
   company, and it is what keeps a founder-level episode defensible without the show's clearance.

### The consent sentence, said on camera

> "This is being recorded for the channel. If you want any part of it out, tell me before
> Friday and it comes out, no questions."

Said once, at the top, on the recording. Not in a document nobody reads.

---

## 3. NDA — the current venture

Never on camera, never in a title, never in a caption, never in a thumbnail:

- the current venture's name, products, roadmap, milestones
- partners, customers, investors, advisers, competitors
- fund size, portfolio, strategy, geographies

Themes are allowed: ownership of compute and data, why infrastructure decides policy, what
India's stack already gets right. A theme has no proper nouns in it. If a sentence needs a
company name to land, it is an NDA sentence.

---

## 4. The clearance flags that actually bite

Pulled from the anchor bank's `ASK` rows — these are the questions that decide whether an
episode can name something:

| # | Question | Blocks |
|---|---|---|
| A-01 | which awards he will state publicly, with years | the journey episodes |
| A-02 | "500+ people led" — which company, which year, or aggregate only | the leadership episodes |
| A-03 | "$30M+ raised" — aggregate across ventures, or not at all | the capital episodes |
| A-04 | naming a customer or buyer | the Clensta milestone episodes |
| A-05 | naming investors or the adviser | the capital episodes |
| A-06 | the board and investment-platform roles — generic or silent | the manufacturing episodes |
| Intertech figures | the 6-unit / 170,000 sq ft / 350-people numbers, repeated on camera | the whole manufacturing domain |
| Guest names | five names in `02_DOMAIN_MAP.md` §8 | The Long Conversation |

Until each is answered, the episode is written with the number replaced by a **[ASK]** marker
and is not shot. The validator fails a script that still contains a marker.

---

## 5. Source discipline for video

The engine's per-paragraph source id becomes a **per-beat source id**:

```
BEAT 3 — what it costs                         [R-22, R-01]
```

Rules:

- a beat with no source id is cut, not argued about
- a number with no receipt does not enter a script, a title, a thumbnail or a caption
- a receipt flagged `PRESS-ATTRIB` is spoken as attribution — "the company's own release says"
  — never as fact in his mouth
- a receipt flagged `ASK` becomes a marker, never an estimate
- a receipt flagged `PAUSED` or `NDA` does not appear at all
- **his own published lines are never reused verbatim.** A 4-gram overlap with his corpus fails
  the script, proper nouns excepted

---

## 6. Never ships

- a claim about a third party's business, health, litigation or finances
- a private detail about a named person that they have not said publicly themselves
- a number that only exists in our notes
- an asset with synthetic provenance
- an episode recorded without a release
- Chapter D, in any form, while it is held
- anything from the current venture

---

## 7. Pre-upload checklist

Ten items, in order, none skippable:

1. Every beat carries a source id, and the id exists in the anchor bank.
2. No number appears on screen or in speech without a receipt.
3. No `ASK` marker, no `[TBD]`, no `TODO` anywhere in the file.
4. Banned vocabulary scan is clean (`engine/yg_gate.py check`).
5. Every proper name is on the allow-list with a clearance flag.
6. 4-gram overlap with his corpus is zero.
7. Consent: every face has a release or a public self-announcement.
8. Title ≤ 60 characters, no question mark, number present.
9. Thumbnail ≤ 5 words, one object, one number.
10. Caption: first line carries a number, 3–5 lowercase hashtags, no link in the body.

---

## 8. Platform disclosure

- **YouTube:** a video containing realistic synthetic media must be disclosed as altered or
  synthetic in the upload flow. The channel should not use synthetic likeness at all; if a
  commissioned graphic ever does, it is disclosed and it is never a real person's face.
- **YouTube:** paid promotion is flagged in the upload flow. No episode will carry a paid
  promotion in the first year; if one does, it is flagged and it is spoken aloud.
- **Instagram:** a paid partnership uses the branded-content label, not a hashtag in the
  caption. A sponsored card is marked on the card itself, not buried.
