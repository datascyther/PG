#!/usr/bin/env python3
"""
05_PIPELINE.py — Reusable LinkedIn public-post scraper (no login) for puneet-linkedin-dossier.

What it does:
  1. Takes a list of public LinkedIn post URLs (/posts/...-activity-...).
  2. Guest-fetches each (same technique as Method 1 Web Extract that worked for P1).
  3. Parses title, author, date, full text, reactions, comments count, follower counts.
  4. Appends/updates 03_POSTS.csv + optionally saves raw HTML for audit.

Why this design:
  - Main profile URL 999-blocks bots; individual post URLs do NOT (verified 2026-10-16).
  - So: discover URLs via search (websearch), then bulk-fetch posts — exactly this script.

Usage:
  python 05_PIPELINE.py --post-urls post_urls.txt --out 03_POSTS.csv --archive ./raw_html --delay 3
  python 05_PIPELINE.py --post-url https://www.linkedin.com/posts/... --out 03_POSTS.csv

  post_urls.txt = one URL per line (see 02_POSTS.md for 22 seeds).

Requirements:
  pip install requests beautifulsoup4 lxml pandas

Compliance:
  - Guest-only, throttled, cached. For bulk (>100 posts) prefer LinkedIn data export or official API.
  - If you get HTTP 999 / login wall, back off, rotate UA, or fetch manually while logged in
    and drop HTML into --archive for offline parsing (--offline flag).

Output CSV columns match 06_DATADICTIONARY.md / 03_POSTS.csv.
"""

from __future__ import annotations
import argparse
import csv
import re
import time
import random
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

UA_LIST = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
]

def fetch_post(url: str, session: requests.Session, archive_dir: Path | None = None) -> dict:
    """Fetch one public LinkedIn post as guest. Returns dict matching CSV schema."""
    headers = {"User-Agent": random.choice(UA_LIST), "Accept-Language": "en-US,en;q=0.9"}
    resp = session.get(url, headers=headers, timeout=30)
    # LinkedIn returns 999 when throttled
    if resp.status_code == 999:
        return {"url": url, "error": "HTTP 999 throttled — retry later / rotate IP / use login HTML",
                "post_id": "", "date_published": "", "title_snippet": "",
                "likes": "n/a", "comments": "n/a", "shares": "n/a",
                "has_image": "", "text_full": "", "notes": "throttled"}
    resp.raise_for_status()
    if archive_dir:
        archive_dir.mkdir(parents=True, exist_ok=True)
        slug = re.sub(r"[^a-zA-Z0-9_-]+", "_", urlparse(url).path.strip("/")[-80:])
        (archive_dir / f"{slug}.html").write_text(resp.text, encoding="utf-8")

    soup = BeautifulSoup(resp.text, "lxml")
    # Guest pages embed post text in <meta property="og:description"> + main article body
    og_desc = soup.find("meta", property="og:description")
    og_title = soup.find("meta", property="og:title")
    text_full = (og_desc["content"] if og_desc and og_desc.get("content") else "").strip()
    # Fallback: article paragraphs
    if len(text_full) < 200:
        article = soup.find("article") or soup
        paras = [p.get_text(" ", strip=True) for p in article.find_all("p")]
        candidate = " ".join(paras)
        if len(candidate) > len(text_full):
            text_full = candidate[:8000]

    title = (og_title["content"] if og_title and og_title.get("content") else "")[:200]
    # Reactions / comments: guest page shows e.g. "112" + "48 Comments"
    likes = "n/a"
    comments = "n/a"
    m_like = re.search(r'(\d[\d,]*)\s*(?:reactions?|likes?)', resp.text, re.I)
    # LinkedIn guest markup: social-actions-reactions with count
    if m_like:
        likes = m_like.group(1).replace(",", "")
    m_com = re.search(r'(\d[\d,]*)\s*Comments?', resp.text, re.I)
    if m_com:
        comments = m_com.group(1).replace(",", "")
    # Date: <time datetime="..."> or JSON-LD datePublished
    date_published = ""
    t = soup.find("time")
    if t and t.get("datetime"):
        date_published = t["datetime"][:10]
    if not date_published:
        m_date = re.search(r'"datePublished"\s*:\s*"([^"]+)"', resp.text)
        if m_date:
            date_published = m_date.group(1)[:10]
    has_image = "yes" if soup.find("meta", property="og:image") else "no"
    # post_id from activity-(\d+)
    m_id = re.search(r"activity-(\d+)", url)
    post_id = m_id.group(1) if m_id else url[-20:]

    return {
        "post_id": post_id,
        "url": url,
        "date_published": date_published,
        "title_snippet": title or text_full[:80],
        "likes": likes,
        "comments": comments,
        "shares": "n/a",
        "has_image": has_image,
        "text_full": text_full,
        "notes": "",
        "error": "",
    }


def parse_offline(html_path: Path) -> dict:
    """Parse a manually-saved (logged-in) post HTML file. Same schema as fetch_post."""
    html = html_path.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "lxml")
    return {
        "post_id": html_path.stem,
        "url": "",
        "date_published": "",
        "title_snippet": "",
        "likes": "n/a",
        "comments": "n/a",
        "shares": "n/a",
        "has_image": "",
        "text_full": soup.get_text(" ", strip=True)[:8000],
        "notes": f"offline:{html_path.name}",
        "error": "",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--post-url", default="", help="Single post URL")
    ap.add_argument("--post-urls", default="", help="Text file, one URL per line")
    ap.add_argument("--out", default="03_POSTS.csv", help="Output CSV path")
    ap.add_argument("--archive", default="", help="Dir to save raw HTML")
    ap.add_argument("--delay", type=float, default=3.0, help="Seconds between requests (min)")
    ap.add_argument("--offline", default="", help="Dir of manually saved HTML files to parse instead")
    args = ap.parse_args()

    if args.offline:
        rows = [parse_offline(p) for p in sorted(Path(args.offline).glob("*.html"))]
    else:
        urls: list[str] = []
        if args.post_url:
            urls.append(args.post_url.strip())
        if args.post_urls:
            urls += [l.strip() for l in Path(args.post_urls).read_text().splitlines()
                     if l.strip().startswith("http")]
        if not urls:
            ap.error("Provide --post-url or --post-urls file.")
        session = requests.Session()
        archive = Path(args.archive) if args.archive else None
        rows = []
        for i, u in enumerate(urls):
            print(f"[{i+1}/{len(urls)}] {u}")
            try:
                rows.append(fetch_post(u, session, archive))
            except Exception as e:  # keep going; record error
                print(f"  ERROR: {e}")
                rows.append({"post_id": "", "url": u, "date_published": "",
                             "title_snippet": "", "likes": "n/a", "comments": "n/a",
                             "shares": "n/a", "has_image": "", "text_full": "",
                             "notes": f"error: {e}", "error": str(e)})
            time.sleep(args.delay + random.uniform(0, 2))

    # Write CSV (union with existing to preserve manual notes)
    out = Path(args.out)
    fieldnames = ["post_id", "url", "date_published", "title_snippet",
                  "likes", "comments", "shares", "has_image", "text_full", "notes"]
    # Merge: keep existing rows for URLs not re-fetched
    existing = {}
    if out.exists():
        with out.open(newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                existing[r.get("url", "")] = r
    for r in rows:
        # adapt to 03_POSTS.csv slim schema if needed (drop text_full/error into notes)
        existing[r["url"] or r["post_id"]] = r
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(existing.values())
    print(f"Wrote {len(existing)} rows -> {out}")
    print("Tip: full text lives in text_full; to regenerate slim 03_POSTS.csv, drop that column.")


if __name__ == "__main__":
    main()
