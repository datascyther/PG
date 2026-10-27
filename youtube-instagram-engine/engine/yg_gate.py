#!/usr/bin/env python3
"""
yg_gate.py — the gate ladder for YouTube episodes and Instagram assets.

Same philosophy as startup-pedia-engine/engine/sp_engine.py: a draft cannot be shot
unless it passes, and every beat must point at a source id that exists in the anchor bank.

Usage:
    python3 engine/yg_gate.py check drafts/YT-001.md
    python3 engine/yg_gate.py check drafts/*.md
    python3 engine/yg_gate.py board
    python3 engine/yg_gate.py ids

Exit code is the number of failing drafts (0 = all clean).

Stdlib only. No network. No writes except the optional --card file.
"""

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOSSIER = ROOT.parent / "puneet-linkedin-dossier"
BANK = DOSSIER / "15_REAL_WORLD_ANCHORS.md"
POST_BODIES = ROOT.parent / "startup-pedia-engine" / "engine" / "facts" / "post_bodies.json"

SPEED_WPM = 145          # spoken words per minute, measured pace for this register
RUNTIME_TOLERANCE = 0.25

# Held chapter. These never appear in a script, a title or a caption.
BANNED = [
    "defence", "defense", "armed forces", "military", "soldier", "soldiers",
    "induction", "forward post", "weapons", "national security", "army", "navy",
    "air force", "war", "battlefield", "border skirmish", "covert operative",
    "awantipora", "jammu", "tezpur", "tawang", "shillong",
]

# Current venture, its people and its counterparties. NDA.
NDA = [
    "defmate", "ensur", "medhansh",
]

REQUEST_WORDS = [
    "subscribe", "like and subscribe", "hit the bell", "follow me", "follow us",
    "share this", "comment below", "dm me", "link in bio", "check out my",
    "buy now", "sign up", "register now", "book a call",
]

PLACEHOLDER_HARD = ["TODO", "FIXME", "XXX", "TKTK", "PLACEHOLDER"]
PLACEHOLDER_SOFT = ["[ASK]", "[TBD]", "[TBC]", "[?]"]

STOP_PREFIX = ("**", ">", "-", "*", "|", "CAPTION", "HASHTAG", "TITLE",
               "THUMBNAIL", "ON SCREEN", "NOTE", "B-ROLL", "SFX", "MUSIC")


# ---------------------------------------------------------------- helpers

def norm(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s']", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def words(s):
    return [w for w in norm(s).split() if w]


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def front_matter(text):
    meta = {}
    if not text.startswith("---"):
        return meta, text
    end = text.find("\n---", 3)
    if end == -1:
        return meta, text
    block = text[3:end]
    body = text[end + 4:]
    for line in block.splitlines():
        if ":" in line and not line.strip().startswith("#"):
            k, v = line.split(":", 1)
            meta[k.strip().lower()] = v.strip()
    return meta, body


def beats(body):
    """Split a body into (heading, lines, is_content).

    Only BEAT / SLIDE sections are content: they carry spoken or on-screen copy and must
    point at a source id. CAPTION, OPEN and NOTES are auxiliary and are read separately.
    """
    out = []
    cur = None
    for raw in body.splitlines():
        line = raw.rstrip()
        if line.startswith("## "):
            heading = line[3:].strip()
            content = bool(re.match(r"(beat|slide)\b", heading, re.I))
            cur = (heading, [], content)
            out.append(cur)
        elif cur is not None:
            cur[1].append(line)
    return out


def spoken_lines(lines):
    keep = []
    for line in lines:
        s = line.strip()
        if not s:
            continue
        if s.startswith(STOP_PREFIX):
            continue
        keep.append(s)
    return keep


def spoken_text(lines):
    return " ".join(spoken_lines(lines))


def source_ids(text):
    return re.findall(r"\b([MRLN]-\d{2,3})\b", text)


def load_bank_ids():
    ids = set()
    if BANK.exists():
        txt = BANK.read_text(encoding="utf-8", errors="ignore")
        ids |= set(re.findall(r"\b([MRLN]-\d{2,3})\b", txt))
    return ids


def load_corpus_grams(n=4):
    grams = set()
    if POST_BODIES.exists():
        data = json.loads(POST_BODIES.read_text(encoding="utf-8"))
        blob = " ".join(str(v) for v in data.values())
        w = words(blob)
        for i in range(len(w) - n + 1):
            grams.add(tuple(w[i:i + n]))
    return grams


# ---------------------------------------------------------------- gates

def gate(meta, body, bank_ids, corpus):
    results = []
    platform = (meta.get("platform") or "youtube").lower()
    fmt = (meta.get("format") or "").lower()
    title = meta.get("title", "")
    thumb = meta.get("thumbnail", "")
    all_beats = beats(body)
    be = [b for b in all_beats if b[2]]
    all_spoken = " ".join(spoken_text(l) for _, l, _c in be)
    w = words(all_spoken)

    def add(gid, label, ok, detail, warn=False):
        results.append((gid, label, "WARN" if (ok and warn) else ("PASS" if ok else "FAIL"), detail))

    # VG1 runtime
    try:
        target = float(meta.get("runtime", "0"))
    except ValueError:
        target = 0.0
    if fmt in {"carousel", "card"}:
        add("VG1", "runtime not applicable to a still format", True, "n/a")
    elif target > 0:
        mins = len(w) / SPEED_WPM
        lo, hi = target * (1 - RUNTIME_TOLERANCE), target * (1 + RUNTIME_TOLERANCE)
        add("VG1", "runtime %.1f min vs %.0f min target" % (mins, target),
            lo <= mins <= hi, "%d spoken words" % len(w))
    else:
        add("VG1", "runtime declared", False, "no 'runtime:' in front matter")

    # VG2 hook: first spoken sentence, <=12 words, no question
    hook = ""
    for _, lines, _c in be:
        sp = spoken_lines(lines)
        if sp:
            hook = sentences(sp[0])[0] if sentences(sp[0]) else sp[0]
            break
    hook_w = len(words(hook))
    add("VG2", "hook <= 12 words, not a question",
        bool(hook) and hook_w <= 12 and "?" not in hook,
        "%d words: %s" % (hook_w, hook[:70] or "missing"))

    # VG3 title
    has_num = bool(re.search(r"\d", title)) or bool(re.search(
        r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|twenty|thirty|"
        r"forty|fifty|hundred|thousand|lakh|lakhs|crore|crores|million|billion|half|first)\b",
        title, re.I))
    t_ok = bool(title) and len(title) <= 60 and "?" not in title and has_num
    add("VG3", "title <= 60 chars, has a number, no question", t_ok,
        "%d chars: %s" % (len(title), title or "missing"))

    # VG4 a source id on every beat, and every id exists
    missing = [h for h, _l, _c in be if not source_ids(h)]
    unknown = sorted({i for _, ls, _c in be for i in source_ids(" ".join(ls))} - bank_ids)
    add("VG4", "every beat carries a source id from the bank",
        not missing and not unknown,
        ("no id on: " + ", ".join(missing[:3])) if missing
        else ("not in bank: " + ", ".join(unknown[:5])) if unknown else "clean")

    # VG5 held-chapter vocabulary
    low = (all_spoken + " " + title + " " + thumb).lower()
    hits = [b for b in BANNED if re.search(r"\b" + re.escape(b) + r"\b", low)]
    add("VG5", "no held-chapter vocabulary", not hits, ", ".join(hits) if hits else "clean")

    # VG6 NDA names
    nhits = [n for n in NDA if re.search(r"\b" + re.escape(n) + r"\b", low)]
    add("VG6", "no current-venture or counterparty names", not nhits,
        ", ".join(nhits) if nhits else "clean")

    # VG7 placeholders
    hard = [p for p in PLACEHOLDER_HARD if p in body]
    soft = [p for p in PLACEHOLDER_SOFT if p in body]
    add("VG7", "no placeholders left", not hard,
        ("hard: " + ", ".join(hard)) if hard else ("open questions: " + ", ".join(soft) if soft else "clean"),
        warn=bool(soft) and not hard)

    # VG8 closing line
    last = ""
    for _, lines, _c in reversed(be):
        sp = spoken_lines(lines)
        if sp:
            last = sp[-1]
            break
    req = [r for r in REQUEST_WORDS if r in last.lower()]
    add("VG8", "last spoken line is not a question or a request",
        bool(last) and "?" not in last and not req,
        ("request: " + ", ".join(req)) if req else (last[-70:] or "missing"))

    # VG9 hashtags (instagram only)
    if platform == "instagram":
        tag_lines = re.findall(r"(?m)^#\S.*$", body)
        tags = re.findall(r"#[A-Za-z0-9_]+", " ".join(tag_lines))
        lc = [t for t in tags if t[1:] == t[1:].lower()]
        add("VG9", "3-5 hashtags, all lowercase",
            3 <= len(tags) <= 5 and len(lc) == len(tags),
            "%d tags" % len(tags))
    else:
        add("VG9", "hashtags not required", True, "n/a")

    # VG10 caption first line carries a number (instagram only)
    if platform == "instagram":
        cap = ""
        m = re.search(r"(?ms)^## CAPTION\s*$(.*?)(?=^## |\Z)", body)
        if m:
            for line in m.group(1).splitlines():
                if line.strip() and not line.strip().startswith("#"):
                    cap = line.strip()
                    break
        add("VG10", "caption first line carries a number",
            bool(cap) and bool(re.search(r"\d", cap)), cap[:70] or "no CAPTION block")
    else:
        add("VG10", "caption rule not applicable", True, "n/a")

    # VG11 anti self-plagiarism, 4-gram against his published corpus
    toks = re.findall(r"[A-Za-z0-9']+", all_spoken)
    low_toks = [t.lower() for t in toks]
    bad = []
    for i in range(len(low_toks) - 3):
        gram = tuple(low_toks[i:i + 4])
        if gram in corpus:
            proper = any(toks[i + k][:1].isupper() for k in range(4))
            bad.append((" ".join(gram), proper))
    real = [g for g, p in bad if not p]
    add("VG11", "no 4-gram reused from his published writing", not real,
        ", ".join(g for g, _ in bad[:3]) if bad else "clean",
        warn=bool(bad) and not real)

    # VG12 thumbnail <= 5 words (when declared)
    if thumb:
        n = len([x for x in re.split(r"[\s/]+", thumb) if x])
        add("VG12", "thumbnail <= 5 words", n <= 5, "%d words: %s" % (n, thumb))
    else:
        add("VG12", "thumbnail declared", False, "no 'thumbnail:' in front matter")

    # VG13 format is one of the live formats
    live = {"on-the-floor", "teardown", "post-mortem", "versus", "the-gap",
            "policy-to-plant", "2035", "long-conversation", "reel", "carousel", "card"}
    add("VG13", "format is a live format", fmt in live, fmt or "missing")

    # VG14 domain declared and live (1-6). Domain 7 is the held chapter.
    dom = meta.get("domain", "")
    add("VG14", "domain declared and live (1-6)", dom in {str(i) for i in range(1, 7)}, dom or "missing")

    return results


# ---------------------------------------------------------------- commands

def check(path, bank_ids, corpus, quiet=False):
    text = path.read_text(encoding="utf-8")
    meta, body = front_matter(text)
    res = gate(meta, body, bank_ids, corpus)
    fails = [r for r in res if r[2] == "FAIL"]
    warns = [r for r in res if r[2] == "WARN"]
    if not quiet:
        print("\n%s  %s" % (path.name, meta.get("title", "")))
        for gid, label, state, detail in res:
            print("  [%s] %-6s %s — %s" % (state, gid, label, detail))
        print("  %d passed, %d warn, %d failed" % (len(res) - len(fails) - len(warns), len(warns), len(fails)))
    return fails


def board():
    p = ROOT / "BOARD.csv"
    if not p.exists():
        print("no BOARD.csv")
        return 1
    rows = list(csv.DictReader(p.open(encoding="utf-8")))
    w = [max(len(str(r.get(k, ""))) for r in rows + [{k: k}]) for k in rows[0].keys()]
    for r in rows:
        print("  ".join(str(r.get(k, "")).ljust(w[i]) for i, k in enumerate(r.keys())))
    return 0


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    cmd = argv[1]
    bank_ids = load_bank_ids()
    if cmd == "ids":
        print("known source ids: %d" % len(bank_ids))
        return 0
    if cmd == "board":
        return board()
    if cmd == "check":
        if len(argv) < 3:
            print("usage: yg_gate.py check <file> [...]")
            return 2
        corpus = load_corpus_grams(4)
        total = 0
        for arg in argv[2:]:
            p = Path(arg)
            if p.is_dir():
                files = sorted(p.glob("*.md"))
            else:
                files = [p]
            for f in files:
                total += len(check(f, bank_ids, corpus))
        print("\n%d failing gate(s) across the checked drafts" % total)
        return min(total, 120)
    print("unknown command: %s" % cmd)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
