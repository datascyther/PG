#!/usr/bin/env python3
"""Stdlib-only bulk guest fetcher for Phase-2 URLs. No pip deps."""
import json, re, time, random, urllib.request
from pathlib import Path
from html import unescape

BASE = Path("/Users/mymac/PG/puneet-linkedin-dossier")
URLS = [l.strip() for l in (BASE/"phase2_urls.txt").read_text().splitlines() if l.strip().startswith("http")]
UAS = [
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36",
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
]

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": random.choice(UAS), "Accept-Language": "en-US,en;q=0.9"})
    try:
        r = urllib.request.urlopen(req, timeout=30)
        html = r.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return {"url": url, "error": str(e), "post_id": "", "date": "", "title": "", "text": "", "likes": "n/a", "comments": "n/a", "image": "", "hashtags": []}
    def meta(prop):
        m = re.search(r'<meta[^>]+property="%s"[^>]+content="([^"]+)"' % re.escape(prop), html)
        if not m:
            m = re.search(r'<meta[^>]+content="([^"]+)"[^>]+property="%s"' % re.escape(prop), html)
        return unescape(m.group(1)).strip() if m else ""
    text = meta("og:description")
    title = meta("og:title")
    image = meta("og:image")
    m = re.search(r'"datePublished"\s*:\s*"([^"]+)"', html)
    date = m.group(1)[:10] if m else ""
    if not date:
        m2 = re.search(r'<time[^>]+datetime="([^"]+)"', html)
        date = m2.group(1)[:10] if m2 else ""
    ml = re.search(r'(\d[\d,]*)\s*(?:reactions?|likes?)', html, re.I)
    likes = ml.group(1).replace(",", "") if ml else "n/a"
    mc = re.search(r'(\d[\d,]*)\s*Comments?', html, re.I)
    comments = mc.group(1).replace(",", "") if mc else "n/a"
    # strip trailing "| N comments on LinkedIn"
    text = re.sub(r'\s*\|\s*\d+\s*comments?\s*on\s*LinkedIn\.?\s*$', '', text, flags=re.I).strip()
    mid = re.search(r"activity-(\d+)", url)
    pid = mid.group(1) if mid else url[-20:]
    hashtags = sorted(set(re.findall(r"#(\w+)", text)))
    return {"url": url, "error": "", "post_id": pid, "date": date, "title": title[:200], "text": text[:8000],
            "likes": likes, "comments": comments, "shares": "n/a",
            "image": image, "has_image": "yes" if image and "static.licdn" not in image else "no",
            "hashtags": hashtags, "html_len": len(html)}

rows = []
for i, u in enumerate(URLS):
    print(f"[{i+1}/{len(URLS)}] {u[:90]}", flush=True)
    rows.append(fetch(u))
    time.sleep(2.0 + random.uniform(0, 1.5))

out = BASE/"phase2_results.json"
out.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
ok = sum(1 for r in rows if not r["error"] and r["text"])
print(f"DONE ok_fulltext={ok}/{len(rows)} -> {out}")
for r in rows:
    print(f"- {r['date']} | L={r['likes']} C={r['comments']} | len={len(r['text'])} | err={r['error'][:60]} | {r['url'][:70]}")
