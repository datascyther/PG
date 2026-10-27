#!/usr/bin/env python3
"""
build_carousel.py — render a gated Family N draft as a LinkedIn document carousel.

    python3 engine/build_carousel.py CAR-01            # review copy, footer marked DRAFT
    python3 engine/build_carousel.py CAR-01 --final    # no footer, for a post that is approved

Slide 1 is the headline (the cover). Each body paragraph becomes one slide. Source tags
([N-10], [R-79]) are stripped from the slide text but stay in the draft file. Any run of
ALL-CAPS words is drawn in the accent colour, so the one emphasis device per card is the
thing you would screenshot. Output: engine/carousels/<ID>/slide-NN.png and <ID>.pdf
(1080x1350, 4:5, the portrait size LinkedIn document posts display best).

Refuses to render a draft that fails the gate ladder, the same as sp_engine render.
Stdlib plus Pillow. Pillow is already on this machine.
"""
import argparse
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sp_engine  # noqa: E402

W, H = 1080, 1350
BG = (14, 26, 43)
INK = (244, 246, 250)
MUTED = (150, 165, 186)
ACCENT = (255, 201, 60)
MARGIN = 96
FONT_HEAVY = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
FONT_TEXT = "/System/Library/Fonts/Supplemental/Arial.ttf"
TAG = re.compile(r"\s*\[[^\]]*\]")


def wrap_runs(draw, text, font, max_w):
    """Greedy word wrap that keeps each word's caps flag so the accent can be applied."""
    lines, line, width = [], [], 0
    space = draw.textlength(" ", font=font)
    for word in text.split():
        w = draw.textlength(word, font=font)
        if line and width + space + w > max_w:
            lines.append(line)
            line, width = [], 0
        width += (space if line else 0) + w
        line.append(word)
    if line:
        lines.append(line)
    return lines


def draw_lines(draw, lines, font, x, y, line_h):
    space = draw.textlength(" ", font=font)
    for line in lines:
        cx = x
        for i, word in enumerate(line):
            core = word.strip(".,;:!?'\"")
            accent = len(core) > 1 and core.isupper()
            draw.text((cx, y), word, font=font, fill=ACCENT if accent else INK)
            cx += draw.textlength(word, font=font) + (space if i < len(line) - 1 else 0)
        y += line_h
    return y


def footer(draw, n, total, final):
    f = ImageFont.truetype(FONT_TEXT, 28)
    draw.text((W - MARGIN, H - 96), f"{n} / {total}", font=f, fill=MUTED, anchor="ra")
    if not final:
        draw.text((MARGIN, H - 96), "DRAFT — NOT APPROVED", font=f, fill=MUTED)


def cover(text, n, total, final):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    label = ImageFont.truetype(FONT_TEXT, 30)
    d.text((MARGIN, 150), "BORN UNICORN  ·  SEASON 1  ·  JURY SEAT", font=label, fill=MUTED)
    d.rectangle([MARGIN, 210, MARGIN + 120, 218], fill=ACCENT)
    font = ImageFont.truetype(FONT_HEAVY, 88)
    lines = wrap_runs(d, text, font, W - 2 * MARGIN)
    draw_lines(d, lines, font, MARGIN, 360, 112)
    footer(d, n, total, final)
    return im


def body(text, n, total, final):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    font = ImageFont.truetype(FONT_TEXT, 54)
    lines = wrap_runs(d, text, font, W - 2 * MARGIN)
    block = len(lines) * 76
    y = max(200, (H - block) // 2 - 40)
    draw_lines(d, lines, font, MARGIN, y, 76)
    footer(d, n, total, final)
    return im


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("id")
    ap.add_argument("--final", action="store_true", help="drop the DRAFT footer")
    args = ap.parse_args()

    p = sp_engine.DRAFTS / f"{args.id}.md"
    if not p.exists():
        raise SystemExit(f"no such draft: {args.id}")
    d = sp_engine.parse_draft(p)
    results = sp_engine.run_gates(d)
    bad = [r for r in results if not r["ok"]]
    if bad:
        raise SystemExit(f"refused: gates failing {', '.join(r['id'] for r in bad)}")

    slides = [("cover", d["headline"])] + [("body", TAG.sub("", para["text"]).strip())
                                           for para in d["paras"]]
    total = len(slides)
    out_dir = sp_engine.ENGINE / "carousels" / args.id
    out_dir.mkdir(parents=True, exist_ok=True)

    images = []
    for i, (kind, text) in enumerate(slides, 1):
        im = cover(text, i, total, args.final) if kind == "cover" else body(text, i, total, args.final)
        im.save(out_dir / f"slide-{i:02d}.png")
        images.append(im)

    pdf = out_dir / f"{args.id}.pdf"
    images[0].save(pdf, save_all=True, append_images=images[1:], resolution=72.0)
    print(f"wrote {total} slides and {pdf}")


if __name__ == "__main__":
    main()
