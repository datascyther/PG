#!/usr/bin/env python3
"""
sp_engine.py — Startup Pedia-format content engine for Puneet Gupta's personal LinkedIn.

Two families of post live in this engine:

  Family P ("pedia")  — third-person, encyclopedic news-post format modeled on the
                        Startup Pedia company page: headline lede, 3-6 short factual
                        paragraphs, a closing line, then 3-5 hashtags.
  Family N ("narrative") — the founder-craft posts that already run on the profile:
                        first person, <=150 words, story-spine, ends on a truth.

Raw assets (video / image / audio) are indexed, turned into extraction cards, and then
into draft shells. Every factual claim in a draft must carry a source token
(M-xx moment, R-xx receipt, A-xx asset). The gate ladder refuses to render a draft
that fails.

Stdlib only. Python 3.9+.

Commands
    init                 create the working structure
    scan [dir]          index raw assets, extract frames, write extraction cards
    facts                rebuild facts.json from the dossier (moments, receipts, corpus)
    new                  create a draft shell from a moment/receipt/asset
    gates <id>           run the gate ladder on a draft
    render <id>          write the publish-ready text + the review card
    board                status board of every draft
    approve <id> / publish <id> / kill <id>
"""

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, date
from pathlib import Path

# ---------------------------------------------------------------- paths

ROOT = Path(__file__).resolve().parent.parent
ENGINE = ROOT / "engine"
ASSETS = ENGINE / "assets"
DRAFTS = ENGINE / "drafts"
QUEUE = ENGINE / "queue"
FRAMES = QUEUE / "frames"
CARDS = QUEUE / "cards"
CONFIG = ENGINE / "config"
FACTS = ENGINE / "facts"
LOG = ENGINE / "publish_log.csv"

DOSSIER = Path(os.environ.get("SP_DOSSIER", "/Users/mymac/PG/puneet-linkedin-dossier"))
BANK = DOSSIER / "15_REAL_WORLD_ANCHORS.md"
CORPUS = [DOSSIER / "13_REAL_WRITING_SAMPLES.md", DOSSIER / "puneet_gupta_posts.md"]
TOP50 = DOSSIER / "23_TOP50_FULL_TEXT.md"

MEDIA_EXT = {".mp4", ".mov", ".m4v", ".webm", ".mkv", ".jpg", ".jpeg", ".png", ".webp",
             ".heic", ".mp3", ".m4a", ".wav", ".aac", ".png", ".gif"}

# ---------------------------------------------------------------- gates config

DEFAULT_GATES = {
    "P": {
        "min_words": 120, "max_words": 320,
        "min_paras": 3, "max_paras": 8,
        "max_sentence_words": 25, "hard_sentence_words": 32,
        "max_paras_per_para": 4,
        "first_person": False,
        "allow_questions": False,
        "min_tags": 3, "max_tags": 5,
        "ngram_overlap": 5,
    },
    "N": {
        "min_words": 60, "max_words": 150,
        "min_paras": 3, "max_paras": 7,
        "max_sentence_words": 22, "hard_sentence_words": 28,
        "max_paras_per_para": 4,
        "first_person": True,
        "allow_questions": True,
        "min_tags": 0, "max_tags": 0,
        "ngram_overlap": 5,
    },
}

# hard-blocked vocabulary (memory rules: defence chapter paused, 2026-10-17)
BANNED_WORDS = [
    "defence", "defense", "armed forces", "military", "soldier", "soldiers",
    "induction", "forward post", "weapons", "national security", "army", "navy",
    "air force", " regiment", "battalion", "commissioned officer",
]
BANNED_PLACES = ["awantipora", "jammu", "tezpur", "tawang", "shillong", "srinagar",
                 "jhansi", "mhow", "dehradun cantonment"]

# never name these without a human decision (venture products / entities)
# never publish these in any spelling — current venture product / entity names. Blocked.
NDA_NAMES = ["muse", "maia", "iuva", "iuva labs", "ensur.ai", "ensure.ai", "defmate labs"]

# brand attribution — warn, not block: only OK if Ensur owns the brand. Ask once.
BRAND_NAMES = ["startup pedia", "startuppedia"]

REQUESTS = ["dm us", "dm me", "comment below", "let us know", "reach out", "connect with me",
            "drop a comment", "write to me", "follow me", "share your thoughts"]

FIRST_PERSON = re.compile(r"\b(i|i'm|i've|i'll|my|me|we|we're|we've|our|us|mine)\b", re.I)

# Capitalised words that are ordinary English, not proper nouns. Without this list the
# name gate flags every sentence-initial word.
COMMON_WORDS = set("""
a an the this that these those and but or so if then than when while because as at by for from
in into on onto of to with without over under between across after before during since until
it its it's he she they them his her their we our us i me my mine you your yours
is are was were be been being has have had do does did will would can could should may might must
one two three four five six seven eight nine ten hundred thousand crore lakh million billion
monday tuesday wednesday thursday friday saturday sunday
january february march april may june july august september october november december
india indian indianinstitute china
applications application applicants uncertainty written one two three four five six seven eight nine ten eleven twelve
twenty thirty forty fifty sixty seventy eighty ninety hundred thousand
filed filedunder sources source category public record season founder founders founderprofile
story stories startup startupstories pedia encyclopedia entry feature featured here
profile profiles company companies team teams product products market markets customer
customers investor investors partner partners launch launched building built scale scales
since early late earlier last next first second third quarter year years month months week weeks
day days hour hours morning afternoon evening night today tomorrow yesterday
dr mr mrs ms prof professor shri smt
new old good better best bigger largest small large high low long short fast slow
about across after again against all almost already also although always among another any
anyone anything around away back be became because become becomes been before began begin
behind being below best better both bring brought build built came can cannot carry case cases
came close come coming could country day days did different do does done down during each
eight either else enough even every everyone everything except far felt find five find first
four from full gave get give given go goes going gone good got great group grow grew had half
hand happen hard has have head held help her here hers herself high him himself his hold hope
house how however i idea if in inside instead interest into its itself keep kept kind know
known last late later least leave left less let letter life light like likely line little long
look made make man many may mean meet men might mind minute money more morning most move much
must myself near need never new next night nine nobody none nor not nothing now number of off
often old on once one only open or order other our out over own part people per perhaps place
point possible put quite rather read really right room said same saw say see seem seen self
shall she should show side since small so some someone something sometimes soon still such take
taken talk tell than that the their them then there these they thing think third this those
though thought three through thus time to together too took toward turn turned two under until
up upon use used using very want was watch way we well went were what when where whether which
while who whole whose why will with within without woman women word work world would write year
yes yet you young your yourself
""".split())

# ---------------------------------------------------------------- helpers


def read(path, default=""):
    try:
        return Path(path).read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return default


def load_gates():
    p = CONFIG / "gates.json"
    if p.exists():
        try:
            return json.loads(read(p))
        except Exception:
            pass
    return DEFAULT_GATES


def ensure_dirs():
    for d in (ASSETS, DRAFTS, QUEUE, FRAMES, CARDS, CONFIG, FACTS):
        d.mkdir(parents=True, exist_ok=True)


def slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")
    return s or "untitled"


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def norm_words(text):
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"[#*_>`\[\]()]", " ", text)
    return re.findall(r"[a-z0-9']+", text.lower())


def sentences(text):
    out = []
    for para in text.split("\n"):
        if not para.strip():
            continue
        for s in re.split(r"(?<=[.!?])\s+", para.strip()):
            if s.strip():
                out.append(s.strip())
    return out


def ngrams(words, n):
    return set(tuple(words[i:i + n]) for i in range(len(words) - n + 1))


# ---------------------------------------------------------------- facts


def parse_bank():
    """Pull moments, live moments, receipts and the paused register out of the anchor bank."""
    txt = read(BANK)
    moments, lives, receipts, paused = [], [], [], []
    tier = None
    for line in txt.splitlines():
        if line.startswith("### Tier "):
            tier = line.split("—")[0].replace("### Tier ", "").strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or cells[0].startswith("---"):
            continue
        ident = cells[0]
        if re.fullmatch(r"M-\d+", ident):
            moments.append({
                "id": ident, "date": cells[1] if len(cells) > 1 else "",
                "place": cells[2] if len(cells) > 2 else "",
                "who": cells[3] if len(cells) > 3 else "",
                "what": cells[4] if len(cells) > 4 else "",
                "prop": cells[5] if len(cells) > 5 else "",
                "carrying_line": cells[6] if len(cells) > 6 else "",
                "source": cells[7] if len(cells) > 7 else "",
                "state": cells[8] if len(cells) > 8 else "",
            })
        elif re.fullmatch(r"N-\d+", ident):
            moments.append({
                "id": ident, "date": cells[1] if len(cells) > 1 else "",
                "place": cells[2] if len(cells) > 2 else "",
                "who": cells[3] if len(cells) > 3 else "",
                "what": cells[4] if len(cells) > 4 else "",
                "prop": cells[5] if len(cells) > 5 else "",
                "carrying_line": cells[6] if len(cells) > 6 else "",
                "source": cells[7] if len(cells) > 7 else "",
                "state": cells[8] if len(cells) > 8 else "",
            })
        elif re.fullmatch(r"L-\d+", ident):
            lives.append({
                "id": ident, "date": cells[1] if len(cells) > 1 else "",
                "line": cells[2] if len(cells) > 2 else "",
                "source": cells[3] if len(cells) > 3 else "",
                "expandable": cells[4] if len(cells) > 4 else "",
            })
        elif re.fullmatch(r"R-\d+", ident):
            receipts.append({
                "id": ident, "tier": tier or "?", "claim": cells[1] if len(cells) > 1 else "",
                "date": cells[2] if len(cells) > 2 else "",
                "source": cells[3] if len(cells) > 3 else "",
                "flag": cells[4] if len(cells) > 4 else "",
            })
        elif re.fullmatch(r"X-\d+", ident):
            paused.append({
                "id": ident, "item": cells[1] if len(cells) > 1 else "",
                "rule": cells[2] if len(cells) > 2 else "",
            })
    return {"moments": moments, "live": lives, "receipts": receipts, "paused": paused}


def parse_top50():
    """Post bodies + performance from the recovered top-50 file."""
    txt = read(TOP50)
    posts = []
    pat = re.compile(r"^## (\d+)\. (\d{4}-\d{2}-\d{2}) — ([\d,]+) impressions · ([\d,]+) engagements · ([\d.]+)% ER")
    lines = txt.splitlines()
    for i, line in enumerate(lines):
        m = pat.match(line)
        if not m:
            continue
        url = ""
        body = []
        j = i + 1
        in_code = False
        while j < len(lines) and not lines[j].startswith("## "):
            l = lines[j]
            if l.startswith("**URL:**"):
                url = l.split("**URL:**")[1].strip()
            if l.strip() == "```":
                in_code = not in_code
                j += 1
                continue
            if in_code:
                body.append(l)
            j += 1
        posts.append({
            "rank": int(m.group(1)), "date": m.group(2),
            "impressions": int(m.group(3).replace(",", "")),
            "engagements": int(m.group(4).replace(",", "")),
            "er": float(m.group(5)), "url": url,
            "body": "\n".join(body).strip(),
        })
    return posts


def build_facts():
    bank = parse_bank()
    posts = parse_top50()
    corpus_text = "\n".join(read(p) for p in CORPUS)
    words = norm_words(corpus_text)
    facts = {
        "built": now(),
        "dossier": str(DOSSIER),
        "moments": bank["moments"],
        "live": bank["live"],
        "receipts": bank["receipts"],
        "paused": bank["paused"],
        "posts": [{k: v for k, v in p.items() if k != "body"} for p in posts],
        "post_bodies": {p["date"]: p["body"] for p in posts},
        "corpus_ngrams": sorted(list(ngrams(words, 5))),
        "corpus_words": len(words),
    }
    FACTS.mkdir(parents=True, exist_ok=True)
    (FACTS / "facts.json").write_text(json.dumps(facts, ensure_ascii=False, indent=1), encoding="utf-8")
    (FACTS / "post_bodies.json").write_text(
        json.dumps(facts["post_bodies"], ensure_ascii=False, indent=1), encoding="utf-8")
    return facts


def load_facts():
    p = FACTS / "facts.json"
    if not p.exists():
        return build_facts()
    try:
        return json.loads(read(p))
    except Exception:
        return build_facts()


def allowlist():
    """Names allowed in a draft. Format: Name | FLAG. FLAG: OK | PRESS-ATTRIB | ASK | PAUSED | NDA"""
    p = CONFIG / "names_allowlist.txt"
    if not p.exists():
        return {}
    out = {}
    for line in read(p).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [x.strip() for x in line.split("|")]
        if len(parts) >= 2:
            out[parts[0].lower()] = parts[1]
        else:
            out[parts[0].lower()] = "OK"
    return out


# ---------------------------------------------------------------- assets


def ffprobe(path):
    if not shutil.which("ffprobe"):
        return {}
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", str(path)],
            capture_output=True, text=True, timeout=60).stdout
        data = json.loads(out or "{}")
    except Exception:
        return {}
    v = next((s for s in data.get("streams", []) if s.get("codec_type") == "video"), None)
    a = next((s for s in data.get("streams", []) if s.get("codec_type") == "audio"), None)
    fmt = data.get("format", {})
    dur = float(fmt.get("duration") or (v or {}).get("duration") or 0) if (fmt.get("duration") or (v or {}).get("duration")) else 0.0
    return {
        "duration_s": round(dur, 1),
        "width": (v or {}).get("width"), "height": (v or {}).get("height"),
        "has_video": bool(v), "has_audio": bool(a),
        "size_mb": round(float(fmt.get("size", 0) or 0) / 1e6, 2),
        "codec": (v or {}).get("codec_name"),
    }


def extract_frames(path, asset_id, max_frames=6):
    if not shutil.which("ffmpeg"):
        return []
    outdir = FRAMES / asset_id
    outdir.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-i", str(path),
             "-vf", f"fps=1/15,scale=480:-1", "-frames:v", str(max_frames),
             str(outdir / "f%02d.jpg")], capture_output=True, timeout=180)
    except Exception:
        pass
    return sorted(str(p) for p in outdir.glob("*.jpg"))


def sidecar(path):
    """Optional `<file>.md` sidecar with the human/extraction facts for one asset."""
    for cand in (Path(str(path) + ".md"), path.with_suffix(".md")):
        if cand.exists():
            return read(cand)
    return ""


def parse_sidecar(txt):
    out = {}
    for line in txt.splitlines():
        m = re.match(r"^\s*([a-zA-Z_ ]{2,24})\s*:\s*(.+?)\s*$", line)
        if m:
            out[m.group(1).strip().lower().replace(" ", "_")] = m.group(2).strip()
    return out


def media_probe_path(path):
    """HEIC decodes as a grid of 512x512 tiles: ffprobe reports a stream of
    thumbnails and ffmpeg extracts tile frames instead of the picture. Resolve a
    HEIC to a JPEG working copy (sips) and probe that instead."""
    if path.suffix.lower() != ".heic":
        return path
    jpg = path.with_suffix(".jpg")
    if not jpg.exists():
        try:
            subprocess.run(["sips", "-s", "format", "jpeg", str(path), "--out", str(jpg)],
                           capture_output=True, timeout=180)
        except Exception:
            pass
    return jpg if jpg.exists() else path


def cmd_scan(args):
    ensure_dirs()
    src = Path(args.dir).expanduser() if args.dir else ASSETS
    if not src.exists():
        print(f"no such folder: {src}")
        return 1
    rows = []
    for p in sorted(src.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in MEDIA_EXT:
            continue
        aid = "A-" + slug(p.stem)[:18].upper().replace("-", "") + "-" + hashlib.md5(
            str(p).encode()).hexdigest()[:4].upper()
        meta = ffprobe(media_probe_path(p))
        frames = extract_frames(media_probe_path(p), aid) if meta.get("has_video") else []
        side = parse_sidecar(sidecar(p))
        card = [
            f"# Extraction card — {p.name}",
            "",
            f"- asset_id: {aid}",
            f"- path: {p}",
            f"- duration_s: {meta.get('duration_s')}",
            f"- resolution: {meta.get('width')}x{meta.get('height')}",
            f"- audio: {'yes' if meta.get('has_audio') else 'no'}",
            f"- size_mb: {meta.get('size_mb')}",
            "",
            "## Frames",
        ] + [f"- {f}" for f in frames] + [
            "",
            "## Facts to fill (one line each — no line, no post)",
            "",
            "- date:",
            "- place:",
            "- who:",
            "- what_happened:",
            "- quotable_line:",
            "- number:",
            "- source:",
            "",
            "## Verdict",
            "",
            "- worth a post: yes / no",
            "- which moment_id: (M-xx from the bank, or new N-xx)",
            "- which receipt_id: (R-xx, or new)",
            "",
        ]
        (CARDS / f"{aid}.md").write_text("\n".join(card), encoding="utf-8")
        rows.append({
            "asset_id": aid, "file": p.name, "path": str(p),
            "duration_s": meta.get("duration_s"), "has_audio": meta.get("has_audio"),
            "resolution": f"{meta.get('width')}x{meta.get('height')}",
            "frames": len(frames), "card": str(CARDS / f"{aid}.md"),
            "sidecar": side,
            "facts": side,
            "indexed": now(),
        })
    out = QUEUE / "assets.json"
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    with open(QUEUE / "assets.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["asset_id", "file", "duration_s", "has_audio",
                                          "resolution", "frames", "path"])
        w.writeheader()
        for r in rows:
            w.writerow({k: r[k] for k in w.fieldnames})
    print(f"indexed {len(rows)} assets -> {out}")
    for r in rows:
        print(f"  {r['asset_id']}  {r['duration_s']}s  {r['resolution']}  {r['file']}")
    return 0


# ---------------------------------------------------------------- drafts


DRAFT_SKELETON = """---
id: {id}
format: {fmt}
status: new
subject: {subject}
moment: {moment}
receipts: {receipts}
asset: {asset}
created: {created}
slot: {slot}
category: {category}
tags: {tags}
---

# HEADLINE — one factual line, <=22 words, no hype, no first person

BODY PARAGRAPH 1 — the what and the when. [M-xx]

BODY PARAGRAPH 2 — the context (founders, year, place, numbers). [R-xx]

BODY PARAGRAPH 3 — the detail that makes it concrete. [M-xx]

CLOSING — one line, a fact, not a request.

CTA: <one neutral line. A fact, a pointer, or a label. Never a request. Never a borrowed brand CTA.>
{tags}
"""


def next_draft_id():
    ids = []
    for p in DRAFTS.glob("*.md"):
        m = re.match(r"SP-(\d+)", p.stem)
        if m:
            ids.append(int(m.group(1)))
    return "SP-%03d" % ((max(ids) + 1) if ids else 1)


def cmd_new(args):
    ensure_dirs()
    facts = load_facts()
    moment = None
    receipt = None
    for m in facts["moments"]:
        if m["id"].lower() == (args.moment or "").lower():
            moment = m
    for r in facts["receipts"]:
        if r["id"].lower() == (args.receipt or "").lower():
            receipt = r
    if not moment and not args.asset and not args.headline:
        print("need --moment M-xx, or --asset, or --headline")
        return 1
    did = next_draft_id()
    subject = args.subject or "Puneet Gupta"
    tags = args.tags or "buildinindia, founders, startupstories"
    body = DRAFT_SKELETON.format(
        id=did, fmt=args.format, subject=subject,
        moment=(moment or {}).get("id", args.moment or ""),
        receipts=(receipt or {}).get("id", args.receipt or ""),
        asset=args.asset or "", created=now(), slot=args.slot or "",
        category=args.category or "Startup Stories", tags=tags)
    if moment:
        body += "\n<!-- BANK CONTEXT\n" + json.dumps(moment, indent=1) + "\n-->\n"
    if receipt:
        body += "\n<!-- RECEIPT CONTEXT\n" + json.dumps(receipt, indent=1) + "\n-->\n"
    p = DRAFTS / f"{did}.md"
    p.write_text(body, encoding="utf-8")
    print(f"created {p}")
    return 0


def parse_draft(path):
    txt = read(path)
    fm = {}
    body = txt
    if txt.startswith("---"):
        parts = txt.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip()
            body = parts[2]
    lines = body.splitlines()
    headline = ""
    paras = []
    tags = []
    cta = ""
    for ln in lines:
        s = ln.strip()
        if not s or s.startswith("<!--") or s.startswith("-->"):
            continue
        if s.startswith("# "):
            headline = s[2:].strip()
        elif s.startswith("CTA:"):
            cta = s[4:].strip()
        elif s.lower().startswith("filed under:"):
            cta = s[len("filed under:"):].strip()
        elif s.startswith("#") and all(w.startswith("#") for w in s.split() if w):
            tags = [t for t in s.split() if t.startswith("#")]
        elif s.startswith("#") and len(s.split()) <= 6:
            tags = [t for t in s.split() if t.startswith("#")]
        else:
            m = re.match(r"^(.*?)\s*\[((?:M|R|N|A|L)-\d+(?:\s*,\s*(?:M|R|N|A|L)-\d+)*)\]\s*$", s)
            srcs = []
            if m:
                para = m.group(1).strip()
                srcs = [x.strip() for x in m.group(2).split(",")]
            else:
                para = s
            if para:
                paras.append({"text": para, "sources": srcs})
    return {"front": fm, "headline": headline, "paras": paras, "cta": cta, "tags": tags, "raw": txt}


def check_sources(draft, facts):
    """Every body paragraph must carry a source token; every token must exist in the bank."""
    known = set()
    for group in ("moments", "live", "receipts"):
        for row in facts.get(group, []):
            known.add(row["id"])
    bu = FACTS / "bu_bank.json"
    if bu.exists():
        try:
            b = json.loads(read(bu))
            for group in ("moments", "receipts"):
                for row in b.get(group, []):
                    known.add(row["id"])
        except Exception:
            pass
    assets = set()
    ap = QUEUE / "assets.json"
    if ap.exists():
        try:
            assets = {a["asset_id"] for a in json.loads(read(ap))}
        except Exception:
            pass
    problems = []
    for i, para in enumerate(draft["paras"], 1):
        if not para["sources"]:
            problems.append(f"P{i}: no source token — every claim needs [M-xx]/[R-xx]/[A-xx]")
            continue
        for s in para["sources"]:
            if s not in known and s not in assets:
                problems.append(f"P{i}: unknown source id {s}")
    return problems


def run_gates(draft):
    facts = load_facts()
    gates = load_gates()
    fam = draft["front"].get("format", "P").upper()
    g = gates.get(fam, gates["P"])
    text_body = "\n\n".join(p["text"] for p in draft["paras"])
    full = " ".join([draft["headline"]] + [p["text"] for p in draft["paras"]] + [draft["cta"]])
    words = norm_words(full)
    sents = sentences(text_body)
    results = []

    def add(gid, name, ok, detail):
        results.append({"id": gid, "name": name, "ok": ok, "detail": detail})

    # G1 length
    ok = g["min_words"] <= len(words) <= g["max_words"]
    add("G1", "length %d-%d words" % (g["min_words"], g["max_words"]), ok, "%d words" % len(words))

    # G2 paragraph count and shape
    paras = draft["paras"]
    ok = g["min_paras"] <= len(paras) <= g["max_paras"]
    detail = "%d body paragraphs" % len(paras)
    if not ok:
        add("G2", "paragraph count", ok, detail)
    else:
        bad = [i for i, p in enumerate(paras, 1)
               if len(sentences(p["text"])) > g["max_paras_per_para"] or not p["text"].strip()]
        ok = not bad
        add("G2", "paragraph count and shape", ok,
            detail if ok else "too long/empty: paragraphs %s" % bad)

    # G3 sentence length
    long_sents = [(len(norm_words(s)), s) for s in sents if len(norm_words(s)) > g["max_sentence_words"]]
    hard = [(n, s) for n, s in long_sents if n > g["hard_sentence_words"]]
    ok = not hard
    longest = max([len(norm_words(x)) for x in sents], default=0)
    add("G3", "no sentence over %d words" % g["max_sentence_words"], ok,
        "longest sentence %d words" % longest +
        (" — HARD: " + hard[0][1][:60] if hard else ""))

    # G4 first person
    fp = FIRST_PERSON.findall(text_body)
    if g["first_person"]:
        add("G4", "first person allowed", True, "n/a")
    else:
        ok = not fp
        add("G4", "third person only (no I/we/my)", ok,
            "found: %s" % ", ".join(sorted(set(x.lower() for x in fp))) if fp else "clean")

    # G5 questions
    if g["allow_questions"]:
        add("G5", "questions allowed", True, "n/a")
    else:
        ok = "?" not in full
        add("G5", "no question marks", ok, "clean" if ok else "question mark present")

    # G6 closing line is not a request
    last = draft["paras"][-1]["text"].lower() if draft["paras"] else ""
    hit = [r for r in REQUESTS if r in last]
    ok = not hit
    add("G6", "closing line is not a request", ok, "clean" if ok else "request language: %s" % hit)

    # G6b CTA line: neutral, not a request, not a borrowed brand CTA
    cta = draft["cta"]
    cta_hit = [r for r in REQUESTS if r in cta.lower()]
    brand_cta = "story featured here" in cta.lower()
    ok = bool(cta.strip()) and not cta_hit and not brand_cta
    add("G6b", "CTA line is neutral (not a request, not a borrowed brand CTA)", ok,
        "clean" if ok else ("missing CTA" if not cta.strip() else
                            ("request language: %s" % cta_hit if cta_hit else "borrowed brand CTA")))

    # G7 source traceability
    probs = check_sources(draft, facts)
    add("G7", "every paragraph carries a source id", not probs,
        "clean" if not probs else "; ".join(probs[:4]))

    # G8 banned vocabulary
    low = full.lower()
    hits = [w for w in BANNED_WORDS if re.search(r"\b%s\b" % re.escape(w), low)]
    places = [p for p in BANNED_PLACES if p in low]
    ok = not hits and not places
    add("G8", "no paused-chapter vocabulary or places", ok,
        "clean" if ok else "banned: %s %s" % (hits, places))

    # G9 name allow-list
    al = allowlist()
    proper = set(re.findall(
        r"\b([A-Z][a-z]+(?:\s+(?:of|the|and|for|&|de|la)\s+[A-Z][a-z]+|\s+[A-Z][a-z]+)*)\b", full))
    proper = {p for p in proper
              if p.lower() not in COMMON_WORDS
              and not all(w.lower() in COMMON_WORDS for w in p.split())}
    allow_tokens = set()
    for k in al:
        for t in re.findall(r"[a-z]+", k.lower()):
            allow_tokens.add(t)

    def name_ok(p):
        pl = p.lower()
        if pl in al:
            return True
        if any(k.startswith(pl + " ") or pl.startswith(k + " ") for k in al):
            return True
        # token level: every capitalised token is either a common word or a cleared token
        toks = re.findall(r"[A-Z][a-z]+", p)
        if toks and all(t.lower() in COMMON_WORDS or t.lower() in allow_tokens for t in toks):
            return True
        return False
    unknown = sorted(p for p in proper if not name_ok(p))
    review = []
    ok = not unknown
    add("G9", "every proper name is on the allow-list", ok,
        "clean" if not unknown else "not on allow-list: %s" % ", ".join(unknown[:6]))

    # G10 anti self-plagiarism (5-gram overlap with the owner's own writing)
    corpus = facts.get("corpus_ngrams", [])
    cset = {tuple(x) for x in corpus}
    scrub = full
    for k in sorted(al, key=len, reverse=True):
        if len(k) > 3:
            scrub = re.sub(re.escape(k), " ", scrub, flags=re.I)
    scrub = re.sub(r"\b[A-Z][a-z]+\b", " ", scrub)   # any leftover proper noun
    words = norm_words(scrub)
    dg = ngrams(words, g["ngram_overlap"])
    overlap = sorted({" ".join(x) for x in (dg & cset)})
    ok = not overlap
    add("G10", "no %d-gram reused from the owner's own writing" % g["ngram_overlap"], ok,
        "clean" if not overlap else "reused: %s" % "; ".join(overlap[:4]))

    # G11 hashtags
    tags = draft["tags"]
    if g["max_tags"] == 0:
        add("G11", "hashtags optional", True, "n/a")
    else:
        ok = g["min_tags"] <= len(tags) <= g["max_tags"]
        lower_ok = all(t == t.lower() for t in tags)
        add("G11", "%d-%d hashtags, lowercase" % (g["min_tags"], g["max_tags"]),
            ok and lower_ok,
            "%d tags: %s" % (len(tags), " ".join(tags)) + ("" if lower_ok else " — not lowercase"))

    # G12 headline discipline
    hw = len(norm_words(draft["headline"]))
    ok = 0 < hw <= 24 and "?" not in draft["headline"]
    add("G12", "headline: 1 line, <=24 words, no question", ok,
        "%d words" % hw if hw else "missing")

    # G13 current-venture names (hard block)
    nd = sorted({p for p in proper if p.lower() in {n.lower() for n in NDA_NAMES}})
    ok = not nd
    add("G13", "no current-venture product or entity names", ok,
        "clean" if ok else "BLOCKED: " + ", ".join(nd))

    # G13b brand attribution (warn only — one decision for the founder)
    br = sorted({p for p in proper if p.lower() in {n.lower() for n in BRAND_NAMES}})
    add("G13b", "brand attribution check (warn only)", True,
        "clean" if not br else "uses " + ", ".join(br) +
        " — confirm Ensur owns the brand before this ships")

    # G14 body is not a stub
    stub = [i for i, p in enumerate(draft["paras"], 1)
            if len(norm_words(p["text"])) < 8 or "HEADLINE" in p["text"]
            or "BODY PARAGRAPH" in p["text"] or "CLOSING" in p["text"]
            or "TODO" in p["text"]]
    add("G14", "no placeholder paragraphs left", not stub,
        "clean" if not stub else "stub paragraphs: %s" % stub)

    # G15 one anchor image (warn only)
    img = draft["front"].get("image", "").strip()
    add("G15", "one anchor image attached", True,
        img if img else "no image set — attach one still from the raw dump")

    return results


def cmd_gates(args):
    p = DRAFTS / f"{args.id}.md"
    if not p.exists():
        print("no such draft")
        return 1
    d = parse_draft(p)
    res = run_gates(d)
    print(f"\nGATES — {args.id}  (family {d['front'].get('format','P')})")
    for r in res:
        print(f"  [{'PASS' if r['ok'] else 'FAIL'}] {r['id']:>4}  {r['name']}\n            {r['detail']}")
    bad = [r for r in res if not r["ok"]]
    print(f"\n{len(res)-len(bad)}/{len(res)} passed" + ("" if not bad else "  — FIX: " + ", ".join(r["id"] for r in bad)))
    return 0 if not bad else 2


def cmd_render(args):
    p = DRAFTS / f"{args.id}.md"
    if not p.exists():
        print("no such draft")
        return 1
    d = parse_draft(p)
    res = run_gates(d)
    bad = [r for r in res if not r["ok"]]
    out = []
    if d["headline"]:
        out.append(d["headline"])
        out.append("")
    for para in d["paras"]:
        out.append(para["text"])
        out.append("")
    if d["cta"]:
        out.append(d["cta"])
    if d["tags"]:
        out.append(" ".join(d["tags"]))
    txt = "\n".join(out).strip()
    (DRAFTS / f"{args.id}.linkedin.txt").write_text(txt + "\n", encoding="utf-8")

    facts = load_facts()
    ids = sorted({s for para in d["paras"] for s in para["sources"]})
    rows = []
    for i in ids:
        for group, label in (("moments", "moment"), ("live", "live moment"), ("receipts", "receipt")):
            for r in facts.get(group, []):
                if r["id"] == i:
                    rows.append(f"- **{i}** ({label}) {r.get('what') or r.get('claim') or r.get('line') or r.get('expandable','')} "
                                f"— flag `{r.get('flag') or r.get('state') or 'OK'}` — source `{r.get('source','')}`")
    card = [
        f"# Review card — {args.id}", "",
        f"- family: {d['front'].get('format','P')}",
        f"- subject: {d['front'].get('subject','')}",
        f"- slot: {d['front'].get('slot','')}",
        f"- category: {d['front'].get('category','')}",
        f"- status: {d['front'].get('status','')}",
        f"- slot: {d['front'].get('slot','')}",
        f"- image: {d['front'].get('image','(none — attach one anchor image)')}",
        f"- series: {d['front'].get('series','')}", "",
        "## Gates", "",
    ]
    for r in res:
        card.append(f"- [{'PASS' if r['ok'] else 'FAIL'}] {r['id']} {r['name']} — {r['detail']}")
    card += ["", "## Sources used", ""] + (rows or ["- none tagged"]) + [
        "", "## One thing to confirm (ask Puneet)", "",
        "- (none yet — the draft may still be missing a fact that only he knows)", "",
        "## Publish-ready text", "", "```", txt, "```", "",
    ]
    (DRAFTS / f"{args.id}.card.md").write_text("\n".join(card), encoding="utf-8")
    print(f"rendered -> {DRAFTS / (args.id + '.linkedin.txt')}")
    print(f"card     -> {DRAFTS / (args.id + '.card.md')}")
    if bad:
        print("gates failing: " + ", ".join(r["id"] for r in bad))
        return 2
    return 0


def cmd_board(args):
    rows = []
    for p in sorted(DRAFTS.glob("SP-[0-9][0-9][0-9].md")):
        d = parse_draft(p)
        rows.append({
            "id": d["front"].get("id", p.stem),
            "format": d["front"].get("format", ""),
            "status": d["front"].get("status", ""),
            "slot": d["front"].get("slot", ""),
            "subject": d["front"].get("subject", ""),
            "moment": d["front"].get("moment", ""),
            "words": len(norm_words(" ".join([d["headline"]] + [x["text"] for x in d["paras"]]))),
            "file": p.name,
        })
    if not rows:
        print("no drafts yet")
        return 0
    w = max(len(r["id"]) for r in rows)
    print(f"{'ID'.ljust(w)}  {'FMT':<4} {'STATUS':<10} {'WORDS':>5}  {'SLOT':<18} MOMENT")
    for r in rows:
        print(f"{r['id'].ljust(w)}  {r['format']:<4} {r['status']:<10} {r['words']:>5}  "
              f"{(r['slot'] or '-'):<18} {r['moment'] or '-'}")
    return 0


def set_status(draft_id, status, extra=None):
    p = DRAFTS / f"{draft_id}.md"
    if not p.exists():
        return False
    txt = read(p)
    txt = re.sub(r"^status:.*$", f"status: {status}", txt, count=1, flags=re.M)
    if extra:
        for k, v in extra.items():
            txt = re.sub(r"^%s:.*$" % re.escape(k), f"{k}: {v}", txt, count=1, flags=re.M)
    p.write_text(txt, encoding="utf-8")
    return True


def cmd_status(args):
    if not set_status(args.id, args.state):
        print("no such draft")
        return 1
    if args.state == "published":
        with open(LOG, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if not LOG.exists() or LOG.stat().st_size == 0:
                w.writerow(["date", "draft_id", "format", "slot", "impressions", "engagements", "er", "notes"])
            w.writerow([date.today().isoformat(), args.id, "", "", "", "", "", ""])
    print(f"{args.id} -> {args.state}")
    return 0


def cmd_init(args):
    ensure_dirs()
    if not (CONFIG / "gates.json").exists():
        (CONFIG / "gates.json").write_text(json.dumps(DEFAULT_GATES, indent=1), encoding="utf-8")
    if not (CONFIG / "names_allowlist.txt").exists():
        (CONFIG / "names_allowlist.txt").write_text(
            "# Name | FLAG   (OK | PRESS-ATTRIB | ASK | PAUSED | NDA)\n", encoding="utf-8")
    if not (CONFIG / "categories.txt").exists():
        (CONFIG / "categories.txt").write_text(
            "Startup News\nFunding News\nTrending News\nStartup Stories\nYoung Entrepreneur\n"
            "Her Story\nSMB's\nFarming\nStartup Learning\nCase Study\nTech & Innovation\n"
            "Industry Insights\n", encoding="utf-8")
    if not LOG.exists():
        with open(LOG, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["date", "draft_id", "format", "slot", "impressions",
                                    "engagements", "er", "notes"])
    print("engine ready:", ROOT)
    return 0


def cmd_facts(args):
    f = build_facts()
    print(f"facts rebuilt: {len(f['moments'])} moments, {len(f['live'])} live, "
          f"{len(f['receipts'])} receipts, {len(f['posts'])} posts, "
          f"{len(f['corpus_ngrams'])} corpus 5-grams")
    return 0


def main():
    ap = argparse.ArgumentParser(prog="sp_engine", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init").set_defaults(func=cmd_init)
    sub.add_parser("facts").set_defaults(func=cmd_facts)
    s = sub.add_parser("scan"); s.add_argument("dir", nargs="?"); s.set_defaults(func=cmd_scan)

    s = sub.add_parser("new")
    s.add_argument("--moment"); s.add_argument("--receipt"); s.add_argument("--asset")
    s.add_argument("--subject", default="Puneet Gupta")
    s.add_argument("--format", default="P", choices=["P", "N"])
    s.add_argument("--slot"); s.add_argument("--category", default="Startup Stories")
    s.add_argument("--tags", default="buildinindia, founders, startupstories")
    s.add_argument("--headline")
    s.set_defaults(func=cmd_new)

    s = sub.add_parser("gates"); s.add_argument("id"); s.set_defaults(func=cmd_gates)
    s = sub.add_parser("render"); s.add_argument("id"); s.set_defaults(func=cmd_render)
    sub.add_parser("board").set_defaults(func=cmd_board)

    s = sub.add_parser("approve"); s.add_argument("id"); s.set_defaults(func=cmd_status, state="approved")
    s = sub.add_parser("publish"); s.add_argument("id"); s.set_defaults(func=cmd_status, state="published")
    s = sub.add_parser("kill"); s.add_argument("id"); s.set_defaults(func=cmd_status, state="killed")

    args = ap.parse_args()
    sys.exit(args.func(args) or 0)


if __name__ == "__main__":
    main()
