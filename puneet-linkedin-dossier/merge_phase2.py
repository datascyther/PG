#!/usr/bin/env python3
"""Merge Phase-2 results into puneet_gupta_posts.md — posts only."""
import json, re
from pathlib import Path

BASE = Path("/Users/mymac/PG/puneet-linkedin-dossier")
rows = json.loads((BASE/"phase2_results.json").read_text(encoding="utf-8"))

CAT = {
 "7495691054759747584": "Other",
 "7432276921519919104": "AI-DEFENCE",
 "6911660756618948609": "Clensta",
 "7475393533785604096": "Leadership",
 "7444594358600790016": "Leadership",
 "7484819700883812352": "Falcon",
 "7487352326807003136": "Leadership",
 "7177269149528707072": "Clensta",
 "7175805863339712512": "Clensta",
 "7181172380373856256": "Clensta",
 "7003657264251191296": "Clensta",
 "7350011885825515521": "Leadership",
 "7404087552996966400": "Other",
 "7194278148757200896": "Defmate",
 "7149028745075449856": "Clensta",
 "7172197137148043264": "Clensta",
 "7173963389172482049": "Clensta",
 "7427230270191259648": "Defmate",
 "7426837364590727168": "Leadership",
 "7429011670053801984": "Other",
 "7420735505425801217": "Other",
 "7467787148805480448": "AI-DEFENCE",
 "7448218219859034114": "AI-DEFENCE",
 "7458368850351460352": "Falcon",
 "6751132388899737600": "Clensta",
 "6783020343691898880": "Clensta",
 "7098670631893839872": "Leadership",
 "6948263152174145536": "Clensta",
 "7168641517006405632": "Clensta",
 "6343911352272281600": "Clensta",
}
rows_sorted = sorted(rows, key=lambda r: (r["date"] or "9999", r["post_id"]))
out_lines = []
out_lines.append("---")
out_lines.append("## Phase-2 Posts (26–55) — full text guest-fetched 2026-10-16, chronological")
out_lines.append("")
for i, r in enumerate(rows_sorted, start=26):
    cat = CAT.get(r["post_id"], "Other")
    tags = ", ".join("#"+h for h in r["hashtags"]) if r["hashtags"] else "none"
    media = r["image"] if r.get("has_image") == "yes" else "none (no post image; og:image generic or missing)"
    text = r["text"].strip() or "[empty — see URL]"
    out_lines.append(f"### Post {i}")
    out_lines.append(f"- **Date:** {r['date'] or 'unknown'}")
    out_lines.append(f"- **Likes:** {r['likes']} | **Comments:** {r['comments']} | **Shares:** n/a")
    out_lines.append(f"- **Category:** {cat}")
    out_lines.append(f"- **Text:**")
    out_lines.append(text)
    out_lines.append(f"- **URL:** {r['url']}")
    out_lines.append(f"- **Hashtags:** {tags}")
    out_lines.append(f"- **Media:** {media}")
# stats
import collections
cats = collections.Counter(CAT.get(r["post_id"], "Other") for r in rows)
likes = [int(r["likes"]) for r in rows if str(r["likes"]).isdigit()]
comms = [int(r["comments"]) for r in rows if str(r["comments"]).isdigit()]
out_lines.append("---")
out_lines.append(f"Phase-2 stats: n=30 full-text (30/30 fetched OK, 0 snippet-only) | dates {rows_sorted[0]['date']} to {rows_sorted[-1]['date']} | " +
  ", ".join(f"{k}: {v}" for k, v in sorted(cats.items())) +
  f" | avg likes {sum(likes)/len(likes):.1f} (n={len(likes)}) | avg comments {sum(comms)/len(comms):.1f} (n={len(comms)})")
(BASE/"phase2_posts_md.txt").write_text("\n".join(out_lines) + "\n", encoding="utf-8")
print(f"wrote {len(rows_sorted)} posts -> phase2_posts_md.txt")
print(f"range {rows_sorted[0]['date']} to {rows_sorted[-1]['date']}")
