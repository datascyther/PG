# FORMAT SPEC — two families of post

Reverse-engineered from the Startup Pedia LinkedIn company page (713k followers) and
cross-checked against the owner's own archive. The engine enforces this file; if a draft
fails a gate, it does not render.

---

## 1. What the Startup Pedia post actually looks like

Measured from live posts on `linkedin.com/company/startup-pedia`:

| Element | Their pattern | Our rule |
|---|---|---|
| Headline | one bold lede sentence, ~18–24 words, "<City>-based <Company> <did what>" | same shape, ≤24 words, no hype, no question |
| Body | 3–6 short paragraphs, each 1–3 sentences, strictly chronological and factual | 3–6 paragraphs, ≤4 sentences each, every paragraph tagged with a source id |
| Numbers | inline, always specific ("₹2,500 crore", "1 lakh sq ft", "15 years") | same, and every number must trace to a receipt |
| Quotes | rare, and only from the source, in quotation marks | same, only from a receipt |
| Closing | no closing line — the last body paragraph ends the piece | one closing line, a fact, never a request |
| CTA | "Get your startup story featured here: <link>" | **do not copy.** See §5 |
| Hashtags | 3–5, all lowercase, one brand tag | 3–5, all lowercase, no borrowed brand tag |
| Volume | high — several posts a day, each one news item | 2 per week, quality over volume |

The DNA is: **short factual paragraphs, dates and numbers everywhere, no adjectives, no
lesson, no request.** A Startup Pedia post reads like a wire report, not like a founder
speaking. That is the whole style.

## 2. Family P — "pedia" (the new direction)

Third person, encyclopedic, dated, sourced.

```
Headline (<=24 words, one line, no question)

Paragraph 1 — the what and the when.            [source id]
Paragraph 2 — the scale or context.              [source id]
Paragraph 3 — the detail that makes it concrete. [source id]
Closing — one fact, one line.                     [source id]

CTA: <one neutral line: a fact, a pointer or a label>

#tag1 #tag2 #tag3
```

Gates (`engine/config/gates.json`, family `P`):

| Gate | Rule |
|---|---|
| G1 | 120–320 words |
| G2 | 3–8 body paragraphs, none longer than 4 sentences |
| G3 | no sentence over 25 words (hard fail over 32) |
| G4 | **no first person.** No I, we, my, our. Third person only |
| G5 | no question marks anywhere |
| G6 | the closing line is not a request |
| G6b | the CTA line is neutral — not a request, not a borrowed brand CTA |
| G7 | every paragraph carries a source id (`M-xx` / `R-xx` / `A-xx`) and the id exists |
| G8 | no paused-chapter vocabulary or place names (defence, military, soldier, induction, bases, weapons, national security) |
| G9 | every proper name is on the allow-list (`engine/config/names_allowlist.txt`) |
| G10 | no 5-gram reused from the owner's own published writing (proper nouns exempt) |
| G11 | 3–5 hashtags, all lowercase |
| G12 | headline: one line, ≤24 words, no question |
| G13 | no current-venture product or entity names (hard block) |
| G13b | brand attribution check — warns if "Startup Pedia" appears (one decision for the founder) |
| G14 | no placeholder paragraphs left |

## 3. Family N — "narrative" (the founder-craft posts that already work)

Unchanged from the existing dossier rules. First person, ≤150 words, story spine
(CLAIM → SCENE → TENSION → TURN → TRUTH), question as the hinge, never a question or a
request at the end, ≤2 standalone one-sentence paragraphs.

Both families feed the same profile. Family P is the new surface for facts and record;
family N is the surface for judgement and lessons. Mixing them inside one post is the
one thing the gate ladder forbids — a post is either a wire report or a piece of writing,
never a blend.

## 4. Third person about himself

This is the one genuine tension in the format, and it is worth naming.

Startup Pedia writes about **companies**, in the third person, from the outside. On a
personal profile, third person about yourself reads as a Wikipedia entry you wrote about
yourself. That is a known genre and it works when three things hold:

1. the subject of the sentences is the **company or the record**, not the person;
2. every claim is dated and sourced, so the piece reads as documentation, not as praise;
3. the closing line is a fact, and it is flat.

The example that proves the shape is the best post of the year — 2026-07-22, IIT Delhi,
402 engagements, 13.19% ER: **institution + year + named people + one quotable line.**
Copy that shape, never his line.

Rule of thumb for the mix: **at most one in four Family P posts should be written about
him rather than about a company.** The rest should be about the record, the institution,
the deal, the market.

## 5. What we do NOT copy from Startup Pedia

| Do not | Why |
|---|---|
| the `#startuppedia` hashtag | it is a claim of provenance. On his personal profile it is a false attribution unless Ensur owns the brand — **confirm once, then either use it or never use it** |
| "Get your startup story featured here: <link>" | borrowed CTA, points at their media desk, asks for a favour |
| their banner, logo, layout, post template | brand assets |
| their byline style (a journalist's name) | he is not their journalist |

We take the **structure**. We do not take the brand, and we do not pretend to be an
outlet. If Ensur owns Startup Pedia, the honest version is that the founder of the
publisher is writing the entries.

## 6. Voice, borrowed from the corpus

- Plain business language. No hype, no corporate filler, no "thrilled", "proud",
  "excited", "game-changer", "landscape", "journey", "leverage" as a verb.
- Numbers instead of adjectives. "four lakh products", not "a staggering volume".
- Dates instead of "recently".
- Active voice, subject first. "Clensta shipped four lakh products", not "four lakh
  products were shipped".
- One idea per paragraph. A paragraph that carries two ideas is two paragraphs.
- No adjectives doing the work that a number should do.

## 7. Anti-self-plagiarism (unchanged, and mechanically enforced)

Never reuse his own lines. Not "my DMs are open", not "what breaks when this becomes 10x
bigger", not "trust is the real go to market strategy", not "not every second needs to be
optimised", not "Hire slow. Fire fast." The G10 gate checks every 5-gram in the draft
against his entire published corpus and fails the draft on a hit.

This is the single most important rule for this profile. A founder posting his own
sentence back at himself is the fastest way to look like a ghostwriter, and the
2026-10-14 Ramayana post is proof that his best material is what he writes in his own
words — not what we write about him.

## 8. Source ids

| Prefix | Meaning | Where it lives |
|---|---|---|
| `M-xx` | a dated moment from his published writing | dossier `15_REAL_WORLD_ANCHORS.md` |
| `L-xx` | a live, unexpanded moment | same file |
| `R-xx` | a receipt — a verifiable fact with a source | same file |
| `A-xx` | a raw asset from the new dump | `engine/queue/assets.json` |
| `N-xx` | a new moment captured from the founder himself | to be created |

A paragraph with no source id does not render. That is the anti-fabrication lock: there
is no way to write a sentence in this format without pointing at where it came from.
