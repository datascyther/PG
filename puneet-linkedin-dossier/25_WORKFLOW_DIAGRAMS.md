# 25_WORKFLOW_DIAGRAMS.md — Excalidraw-ready Mermaid

> **INTERNAL ONLY — DO NOT SHARE.** Presentation material for the meeting with Puneet.
> Not for external distribution.

**Created:** 2026-10-21
**How to use:** Excalidraw → left panel → **Mermaid** → paste one block → it converts to editable
shapes. Export to PNG/SVG for the deck. Each block is self-contained; paste them one at a time.

**Slide order for the meeting:** 1 · 2 · 4 · 6 · 3 — then the five drafts (block 5).

---

# BLOCK 1 — The system in one picture (opening slide)

```mermaid
flowchart LR
    subgraph P["PUNEET — 60 seconds a day"]
        P1["One line<br/>WhatsApp, 07:45 IST<br/>voice note welcome<br/>Nothing today is valid"]
    end

    subgraph M["MANAGER — the whole machine"]
        M1["Capture and check<br/>is there a real anchor?"]
        M2["Draft from his material<br/>every line tagged"]
        M3["Nine gates<br/>compliance is not overridable"]
        M4["Approval<br/>one word: yes or no"]
        M5["Publish<br/>Mon / Wed / Fri, 08:30"]
        M6["Measure<br/>72 hours, then 7 days"]
    end

    subgraph R["THE READER"]
        R1["Founders and operators<br/>Delhi NCR, small firms"]
    end

    P1 --> M1
    M1 -->|yes| M2
    M1 -->|no| M1b["Thesis seed<br/>closing argument only"]
    M1b --> M2
    M2 --> M3 --> M4
    M4 -->|yes| M5
    M4 -->|no| M4b["Killed<br/>no questions asked"]
    M5 --> R1 --> M6
    M6 -->|one change a week| P1

    style P fill:#e8f4ff,stroke:#2b6cb0,stroke-width:1px
    style M fill:#f7fafc,stroke:#4a5568,stroke-width:1px
    style R fill:#fff8e6,stroke:#b7791f,stroke-width:1px
    style M4b fill:#fff5f5,stroke:#c53030,stroke-width:1px
```

---

# BLOCK 2 — The weekly rhythm (how a week actually runs)

```mermaid
flowchart TD
    D1["MON 08:30<br/>publish slot 1"] --> D1b["MON 09:30<br/>weekly review<br/>one change only"]
    D1b --> D2["TUE<br/>capture, draft, gates,<br/>send for approval"]
    D2 --> D3["WED 08:30<br/>publish slot 2"]
    D3 --> D4["THU<br/>capture, draft, gates,<br/>send for approval"]
    D4 --> D5["FRI 08:30<br/>publish slot 3"]
    D5 --> D6["SAT<br/>weekly catch-all prompt<br/>anything from the week"]
    D6 --> D7["SUN<br/>personal prompt<br/>a place, a habit, a person"]
    D7 --> D1

    D2 -.->|"voice note"| D2
    D4 -.->|"voice note"| D4

    style D1 fill:#e8f4ff,stroke:#2b6cb0
    style D3 fill:#e8f4ff,stroke:#2b6cb0
    style D5 fill:#e8f4ff,stroke:#2b6cb0
    style D1b fill:#f7fafc,stroke:#4a5568
    style D6 fill:#fff8e6,stroke:#b7791f
    style D7 fill:#fff8e6,stroke:#b7791f
```

---

# BLOCK 3 — The anchor test (the rule that keeps the feed real)

```mermaid
flowchart TD
    L["His one line"] --> A{"Does it contain at least one:<br/>place, date or year,<br/>number, named person,<br/>object, named decision?"}
    A -->|yes| B["DRAFTABLE<br/>the anchor becomes the spine of the post"]
    A -->|no| C["THESIS SEED<br/>a thought, not a story"]
    C --> D["May only be the closing argument<br/>of a post whose body has a scene"]
    D --> A
    B --> E["POST<br/>one moment + one receipt + the reflection"]
    E --> F["Close on the idea<br/>no CTA, no link, no hashtag"]
```

---

# BLOCK 4 — Anatomy of a post (why it sounds like him)

```mermaid
flowchart LR
    M["MOMENT<br/>a real dated scene<br/>where, who, what happened,<br/>the physical prop"] --> P["THE POST<br/>one idea<br/>100 to 140 words"]
    R["RECEIPT<br/>a fact he has already said<br/>a number, a year,<br/>an institution, an award"] --> P
    P --> F["REFLECTION<br/>what it means for a builder"]
    F --> G["CLOSE<br/>a quiet truth<br/>never a request"]

    style M fill:#e8f4ff,stroke:#2b6cb0
    style R fill:#e8f4ff,stroke:#2b6cb0
    style P fill:#f7fafc,stroke:#4a5568
    style F fill:#f7fafc,stroke:#4a5568
    style G fill:#f0fff4,stroke:#2f855a
```

---

# BLOCK 5 — The five drafts and what each one needs

```mermaid
flowchart TD
    S1["S1 · The person inside the system<br/>1,000 people hired<br/>escalations, edge cases, approvals"] --> Q1{"Needs anything?"}
    S2["S2 · The classroom<br/>96% in two papers<br/>nine years running the company"] --> Q2{"Needs anything?"}
    S3["S3 · Four travellers, four jackets<br/>the scene of 18 Feb 2026"] --> Q3{"Needs anything?"}
    S4["S4 · Sunday in the warehouse<br/>four lakh products"] --> Q4{"Needs anything?"}
    S5["S5 · The founder as the ceiling<br/>the company outgrows its founder"] --> Q5{"Needs anything?"}

    Q1 -->|no| A1["READY<br/>approve and publish"]
    Q2 -->|yes| A2["one sentence<br/>which session, what he said back"]
    Q3 -->|yes| A3["one sentence<br/>where, when, what he answered"]
    Q4 -->|yes| A4["one sentence<br/>is the number safe to say"]
    Q5 -->|yes| A5["one fact<br/>500 at that company, or 500 in total"]

    A1 --> P["APPROVED<br/>gates, sweep, publish<br/>Mon / Wed / Fri 08:30"]
    A2 --> P
    A3 --> P
    A4 --> P
    A5 --> P

    style S1 fill:#e8f4ff,stroke:#2b6cb0
    style S2 fill:#e8f4ff,stroke:#2b6cb0
    style S3 fill:#e8f4ff,stroke:#2b6cb0
    style S4 fill:#e8f4ff,stroke:#2b6cb0
    style S5 fill:#e8f4ff,stroke:#2b6cb0
    style A1 fill:#f0fff4,stroke:#2f855a
    style A2 fill:#fff8e6,stroke:#b7791f
    style A3 fill:#fff8e6,stroke:#b7791f
    style A4 fill:#fff8e6,stroke:#b7791f
    style A5 fill:#fff8e6,stroke:#b7791f
    style P fill:#f7fafc,stroke:#4a5568
```

---

# BLOCK 6 — The gate ladder (nothing goes out half-checked)

```mermaid
flowchart TD
    A["DRAFT"] --> G1["1 · Counts<br/>words, sentence length, rhythm"]
    G1 --> G2["2 · Format<br/>no hashtag, link or emoji"]
    G2 --> G3["3 · Self-plagiarism<br/>zero overlap with his own words"]
    G3 --> G4["4 · Compliance<br/>paused chapter, stealth venture,<br/>name allow-list"]
    G4 --> G5["5 · No CTA<br/>the question sits at the turn"]
    G5 --> G6["6 · Staleness<br/>subject age 7 days,<br/>no stale time words"]
    G6 --> G7["7 · Traceability<br/>every line tagged,<br/>nothing invented"]
    G7 --> G8["8 · Voice match<br/>read against his own posts"]
    G8 --> G9["9 · Humanizer<br/>scrub the AI tells"]
    G9 --> B["READY FOR HIS YES"]

    style G4 fill:#fff5f5,stroke:#c53030,stroke-width:2px
    style B fill:#f0fff4,stroke:#2f855a
```

---

# BLOCK 7 — Depth, not reach (the proof slide)

```mermaid
flowchart TD
    subgraph W["WINNERS — a room, a moment, a person"]
        W1["22 Jul 2026 · IIT Delhi<br/>3,048 impressions<br/>402 engagements · 13.19%"]
        W2["14 Sep 2026 · a conversation<br/>6,010 impressions<br/>1,155 engagements · 19.22%"]
        W3["19 Jul 2026 · a library on a Sunday<br/>5,580 impressions<br/>283 engagements · 5.07%"]
    end

    subgraph T["THE TRAP — a topic, not a room"]
        T1["06 Dec 2025 · national impact<br/>74,295 impressions<br/>159 engagements · 0.21%"]
    end

    W --> R["Judge the post on depth<br/>engagement rate, never on reach"]
    T --> R

    style W fill:#f0fff4,stroke:#2f855a
    style T fill:#fff5f5,stroke:#c53030
    style R fill:#f7fafc,stroke:#4a5568
```

---

# BLOCK 8 — The answer to "we cannot match his writing style"

```mermaid
flowchart TD
    Q["We cannot match his exact writing style"] --> A["So do not imitate it"]
    A --> B["Reproduce the material<br/>and the shape"]
    B --> C["The voice arrives with the material"]
    C --> D1["40 archived moments<br/>35 spent, 30 unspent"]
    C --> D2["A live capture every day<br/>one line, one minute"]
    C --> D3["All 50 of his best posts<br/>recovered, with metrics"]
    D1 --> E["THE ANCHOR BANK"]
    D2 --> E
    D3 --> E
    E --> F["Every post carries<br/>a Moment ID and a Receipt ID"]

    style Q fill:#ebf8ff,stroke:#2b6cb0
    style E fill:#f7fafc,stroke:#4a5568
    style F fill:#f0fff4,stroke:#2f855a
```

---

# BLOCK 9 — The story spine (the answer to "it reads like a list of sentences")

```mermaid
flowchart TD
    C["CLAIM<br/>one blunt line, no warm-up<br/>the reader stops"] --> S["SCENE<br/>a real thing that happened<br/>with a number, a place, a person<br/>the reader sees it"]
    S --> T["TENSION<br/>what it cost, what went wrong,<br/>why it was not obvious<br/>the reader leans in"]
    T --> Q["TURN<br/>ONE question, in the middle<br/>the reader answers it in their head"]
    Q --> U["TRUTH<br/>a portable line, no request<br/>the reader carries it"]
    U -.->|"next post"| C

    R1["RULE 1<br/>the last line is never a question<br/>and never a request"] -.-> C
    R2["RULE 2<br/>one question per post,<br/>at the turn, not at the close"] -.-> Q
    R3["RULE 3<br/>if a paragraph does not do<br/>one of these five jobs, it is cut"] -.-> T

    style C fill:#e8f4ff,stroke:#2b6cb0
    style S fill:#e8f4ff,stroke:#2b6cb0
    style T fill:#f7fafc,stroke:#4a5568
    style Q fill:#fff8e6,stroke:#b7791f,stroke-width:2px
    style U fill:#f0fff4,stroke:#2f855a
    style R1 fill:#fff5f5,stroke:#c53030
    style R2 fill:#fff5f5,stroke:#c53030
    style R3 fill:#fff5f5,stroke:#c53030
```

---

# BLOCK 10 — From a line to a post (the transformation, for the "how do you do this" question)

```mermaid
flowchart LR
    L["His line<br/>60 seconds, one day"] --> A["Anchor test<br/>place, date, number,<br/>person, object, decision"]
    A -- fail --> X["Thesis seed<br/>a thought, not a story"]
    A -- pass --> M["Moment<br/>the scene, with its detail"]
    M --> Q["The turn<br/>one question, in the middle"]
    R["Receipt<br/>a fact he has already said"] --> Q
    Q --> D["Draft<br/>100 to 140 words<br/>every line tagged"]
    D --> G["Nine gates"]
    G --> P["He says yes<br/>one word"]
    P --> L2["Published<br/>Mon / Wed / Fri 08:30"]

    style L fill:#e8f4ff,stroke:#2b6cb0
    style M fill:#e8f4ff,stroke:#2b6cb0
    style R fill:#e8f4ff,stroke:#2b6cb0
    style Q fill:#fff8e6,stroke:#b7791f
    style X fill:#fff5f5,stroke:#c53030
    style P fill:#f0fff4,stroke:#2f855a
```

---

# Slide copy (paste under each diagram)

**1 · The system.** He gives 60 seconds a day. We do the rest. Nothing goes out without his yes.
One word kills a post and we never ask why.

**2 · The rhythm.** Three posts a week, Monday Wednesday Friday at 08:30. Monday is the only day
his own data supports on both measures. A slot is skipped without apology.

**3 · The rule.** If his line has no place, date, number, person or object in it, it is not a
post. It is a thought, and it can only close a post that has a scene.

**4 · The anatomy.** One real moment. One fact he has already said. What it means for a builder.
Close on the truth, never on a request.

**5 · The ask.** Five drafts, four one-sentence answers, one fact to confirm. Yes, no, or not me.

**6 · The gates.** Nine checks, cheapest first. The compliance gate is the one the manager cannot
override.

**7 · The proof.** 25 of his 50 best posts name a place. 25 name a person. 22 use a number. The
biggest post of the year earned 0.21% engagement. The best post of the period earned 13.19% on
a third of the reach.

**8 · The honesty.** We were never going to imitate his voice. We put his own moments back in
front of him and let him approve them.
