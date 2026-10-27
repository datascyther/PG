#!/usr/bin/env python3
"""
bu_convert.py — turn the Born Unicorn raw data into pedia-format drafts.

Reads  engine/queue/bu_episodes.csv  (the data contract, see BU_INTAKE.md)
Writes  engine/drafts/SP-xxx.md    (one draft per episode, first-pass prose)
        engine/facts/bu_bank.json  (the new N-xx moments and R-xx receipts, so the
                                   gate ladder accepts the source ids)

Rows whose `consent` column is not exactly `yes` are skipped and reported. A founder
cannot be profiled in a public record without the show's clearance.

Usage:
    python3 engine/bu_convert.py                 # convert every eligible row
    python3 engine/bu_convert.py --dry-run       # show what would be created
    python3 engine/bu_convert.py --from 2        # start at row 2
"""

import argparse
import csv
import json
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRAFTS = ROOT / "engine" / "drafts"
QUEUE = ROOT / "engine" / "queue"
FACTS = ROOT / "engine" / "facts"
CSV_IN = QUEUE / "bu_episodes.csv"
BANK_OUT = FACTS / "bu_bank.json"
TEMPLATE = ROOT / "engine" / "templates" / "bu_episode.md.tmpl"

# slots: Mon / Wed / Fri 08:30, starting 2026-11-12 (after the current batch)
FIRST_SLOT = date(2026, 11, 12)


def next_ids(start_m=1, start_r=69):
    m, r = start_m, start_r
    if BANK_OUT.exists():
        try:
            b = json.loads(BANK_OUT.read_text())
            for row in b.get("moments", []):
                mm = re.search(r"N-(\d+)", row.get("id", ""))
                if mm:
                    m = max(m, int(mm.group(1)) + 1)
            for row in b.get("receipts", []):
                rr = re.search(r"R-(\d+)", row.get("id", ""))
                if rr:
                    r = max(r, int(rr.group(1)) + 1)
        except Exception:
            pass
    return m, r


def next_draft_id():
    ids = []
    for p in DRAFTS.glob("SP-[0-9][0-9][0-9].md"):
        mm = re.match(r"SP-(\d+)", p.stem)
        if mm:
            ids.append(int(mm.group(1)))
    return "SP-%03d" % ((max(ids) + 1) if ids else 1)


def slots(n):
    """n publishable Mon/Wed/Fri slots after FIRST_SLOT."""
    out, d = [], FIRST_SLOT
    while len(out) < n:
        if d.weekday() in (0, 2, 4):
            out.append(d.isoformat())
        d += timedelta(days=1)
    return out


def clean(s):
    return (s or "").strip().rstrip(".")


def build_paragraphs(row, mid, rid):
    """First-pass pedia prose from the row's facts. Anything missing stays TODO and
    the gate ladder refuses to render it."""
    company = clean(row.get("company")) or "TODO_COMPANY"
    founder = clean(row.get("founder"))
    city = clean(row.get("city"))
    sector = clean(row.get("sector"))
    builds = clean(row.get("what_they_build"))
    number = clean(row.get("one_number"))
    quote = clean(row.get("one_line_quote"))
    when = clean(row.get("shoot_date"))

    p1 = (f"{city + '-based ' if city else ''}{company} was one of the founders who pitched "
          f"in Born Unicorn Season 1{f' on {when}' if when else ' on TODO_DATE'}. "
          f"{builds if builds else 'TODO_WHAT_THEY_BUILD'}.")
    p2 = (f"{sector} company, founded by {founder}." if founder and sector else
          (f"{sector} company." if sector else "TODO_SECTOR_AND_FOUNDER."))
    if number:
        p3 = f"By the pitch stage the company reported {number}."
    else:
        p3 = "TODO_NUMBER — one number, from the episode or the founder's own material."
    if quote:
        p4 = f"In the episode, {founder or 'the founder'} said: \"{quote}\""
    else:
        p4 = "TODO_QUOTE — one quotable line from the episode, or drop this paragraph."
    p5 = ("Born Unicorn Season 1 was shot on 30 September and 1 October 2026, with a jury of "
          "six and episodes produced across five sectors.")
    return [f"{p1} [{mid}]", f"{p2} [{rid}]", f"{p3} [{rid}]", f"{p4} [{rid}]", f"{p5} [R-60]"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--from", dest="start", type=int, default=1)
    args = ap.parse_args()

    if not CSV_IN.exists():
        print("no data file:", CSV_IN)
        return 1
    rows = list(csv.DictReader(CSV_IN.open(encoding="utf-8")))
    rows = [r for r in rows if any((v or "").strip() for v in r.values())]

    blocked = [r for r in rows if (r.get("consent") or "").strip().lower() != "yes"]
    live = [r for r in rows if (r.get("consent") or "").strip().lower() == "yes"]
    live = live[args.start - 1:]

    print(f"{len(rows)} rows — {len(live)} eligible (consent=yes), {len(blocked)} blocked")
    for r in blocked:
        who = clean(r.get("company")) or clean(r.get("founder")) or "unnamed"
        print(f"  BLOCKED  {who}: no clearance (consent={r.get('consent') or 'blank'})")

    if not live:
        print("nothing to convert")
        return 0

    m_id, r_id = next_ids()
    did = next_draft_id()
    slot_list = slots(len(live))
    moments, receipts = [], []
    if BANK_OUT.exists():
        b = json.loads(BANK_OUT.read_text())
        moments, receipts = b.get("moments", []), b.get("receipts", [])

    for i, row in enumerate(live):
        mid, rid = "N-%02d" % m_id, "R-%d" % r_id
        m_id += 1
        r_id += 1
        paras = build_paragraphs(row, mid, rid)
        company = clean(row.get("company")) or "TODO"
        founder = clean(row.get("founder")) or "TODO"
        image = clean(row.get("image_file"))
        body = f"""---
id: {did}
format: P
status: new
subject: {company}
series: born-unicorn-s1
moment: {mid}
receipts: {rid}
asset:
image: {image}
created: {datetime.now().strftime('%Y-%m-%d %H:%M')}
slot: {slot_list[i]} 08:30
category: Startup Stories
tags: buildinindia, startupstories, iitdelhi
---

# {clean(row.get('city')) + '-based ' if clean(row.get('city')) else ''}{company} pitched in Born Unicorn Season 1

{chr(10).join(paras)}

Filed under: Startup Stories — Born Unicorn Season 1, 2026.

#buildinindia #startupstories #iitdelhi
"""
        moments.append({
            "id": mid, "date": clean(row.get("shoot_date")), "place": clean(row.get("city")),
            "who": founder, "what": f"{company} pitched in Born Unicorn Season 1",
            "source": "raw episode data", "state": "NEW",
        })
        receipts.append({
            "id": rid, "tier": "A", "claim": f"{company} — {clean(row.get('sector'))}; "
                                               f"{clean(row.get('one_number')) or 'number pending'}",
            "date": clean(row.get("shoot_date")), "source": "raw episode data", "flag": "OK",
        })
        if not args.dry_run:
            (DRAFTS / f"{did}.md").write_text(body, encoding="utf-8")
        print(f"  {'would create' if args.dry_run else 'created'} {did}  {company}  "
              f"slot {slot_list[i]}  src [{mid}, {rid}]  image: {image or 'NONE'}")
        did = "SP-%03d" % (int(did[3:]) + 1)

    if not args.dry_run:
        FACTS.mkdir(parents=True, exist_ok=True)
        BANK_OUT.write_text(json.dumps({"moments": moments, "receipts": receipts},
                                       ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"bank updated -> {BANK_OUT}")
        print("next: python3 engine/sp_engine.py render " + did)
    return 0


if __name__ == "__main__":
    sys.exit(main())
