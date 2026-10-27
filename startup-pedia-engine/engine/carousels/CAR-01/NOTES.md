# CAR-01 — jury-table carousel (review copy, not approved, not scheduled)

**Format:** LinkedIn document post, 6 slides, 1080x1350 (4:5). Text only, no photo.
**Family N:** first person, ≤150 words, the story spine. Gates 17/17 (`sp_engine.py gates CAR-01`).
**Proposed slot:** Mon 30 Nov 2026, 08:30 IST (the next free Monday; Batch B holds Fri 20, Mon 23, Wed 25, Fri 27 Nov).
**Status:** drafted. Nothing published. Needs an explicit yes.

## Build

    python3 engine/build_carousel.py CAR-01            # review copy, DRAFT footer
    python3 engine/build_carousel.py CAR-01 --final    # after approval, no footer

Output: `slide-01.png` … `slide-06.png` and `CAR-01.pdf`. Upload the PDF as a LinkedIn
document. The post text above the document is the first slide's line, not a separate hook.

## What he needs to answer before yes

1. **Slide 3 — "the test"** (`[R-77]`): the claim that the finalists have already run something
   real, and what a juror tests in a few minutes. Confirm it, or give the sentence he would use.
2. **Slide 5 — "the practice"** (`[N-10]`): that he starts with the least certain number and asks
   the founder to prove it. This is a description of what he does, so only he can confirm it.
3. **Slide 6 — the closing truth**: the claim that a pitch that only sounds good gets found out
   within minutes. Opinion, his to keep or cut.
4. **Slide 4 — the hinge** (`[R-79]`): the field "cut to thirty". The record has a date problem
   (see below), so this line must stay as written until the date is confirmed.

## Record problems found while building it

- **R-79 date conflict.** It says the Top 30 were "announced on 15 September 2026", but its
  source row is dated 27 August 2026, the launch date. A launch article can state the schedule,
  not the outcome. Confirm the announcement really happened on 15 September, with a link to it.
- **M-44 is already published.** The bank marks the exhausted-founder meeting LIVE, but his
  2025-11-16 post (`post_bodies.json`) already tells that scene. A carousel built on it would
  repeat his own post. It is not used here. The bank entry should be BURNED.
- **N-07, R-69 and R-74 cite the synthetic PNG** (`3FC8FA7C…png`). A C2PA-signed ChatGPT image
  cannot be a source. Re-source to a real frame or remove them before any post cites them.
- **The jury-notebook scene is saturated.** SP-010 (Wed 28 Oct) and SP-012 (Mon 23 Nov) already
  use the 1 October notebook and pen moment. This carousel tags N-10 on slides 2, 5 and 6, so it
  leans on the same frame as SP-012. Before approval, check that slide 2 does not read as a
  repeat of SP-012, and check that slides 5 and 6 do not repeat SP-012's closing line.
- **Format conflict.** `28_CONTENT_TYPES.md` says carousels are not part of the format, because
  none of the top 50 posts were carousels. That is absence of data, not evidence against them.
  The owner decides whether a carousel is allowed.

## Photos (held)

- **IMG_2529.HEIC** (group shot, 1 Oct 2026, 08:53 UTC): about 30 people, most unnamed. Held
  until everyone in it is cleared or the show releases it. Not in the anchor bank yet.
- **IMG_2568.HEIC** (stage talk, 1 Oct 2026, 11:19 UTC): at least one unnamed third party (back
  of head, centre-right) and another at the left edge. Held. The image is not in the bank, and
  which person is him must come from him, not from the face. A crop to him alone can be made
  after that answer, and the crop must not include any other person.
- **IMG_2619** (the notebook frame cited by N-10): not in `engine/assets/` today, which holds
  only three files. This carousel does not need it, but any post that uses that frame must wait
  until it is back on disk.
- **3FC8FA7C…png**: synthetic. Never publish.
