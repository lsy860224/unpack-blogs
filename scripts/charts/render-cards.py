#!/usr/bin/env python3
"""
AIGrit 다이어그램 렌더러 — 카드형(N열) / 단계형(흐름) / 표형 인포그래픽.

사실 기반 다이어그램(공식 수수료 구조, 체크리스트, 작업 흐름)만 그린다.
측정하지 않은 점수·벤치마크 차트를 만들지 않는다.

Usage:
  python3 scripts/charts/render-cards.py spec.json
spec.json: [{ "out": "apps/aigrit/public/images/{slug}/01-x.png",
              "kind": "cards" | "flow" | "table",
              "title": "...", "subtitle": "...",
              "items": [{"head": "...", "sub": "...", "body": "줄1\\n줄2"}],   # cards / flow
              "columns": ["..."], "rows": [["..."]],                          # table
              "footer": "..." }]
Fonts: Pretendard OTF. PRETENDARD_DIR 환경변수 또는 /tmp/og-fonts 사용.
"""
import json, os, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 2000, 1090
BG = (15, 23, 42); CARD = (30, 41, 59); TEXT = (241, 245, 249); MUTED = (148, 163, 184)
ACCENTS = [(6, 182, 212), (99, 102, 241), (16, 185, 129), (245, 158, 11), (239, 68, 68), (168, 85, 247)]
FD = Path(os.environ.get("PRETENDARD_DIR", "/tmp/og-fonts"))

def f(weight, size):
    return ImageFont.truetype(str(FD / f"Pretendard-{weight}.otf"), size)

def center(d, text, font, cx, y, fill):
    w = d.textlength(text, font=font); d.text((cx - w / 2, y), text, font=font, fill=fill)

def wrap(d, text, font, maxw):
    out = []
    for para in text.split("\n"):
        line = ""
        for ch in para:
            if d.textlength(line + ch, font=font) > maxw and line:
                cut = line.rfind(" ")
                if cut > 0:
                    out.append(line[:cut]); line = line[cut + 1:] + ch
                else:
                    out.append(line); line = ch
            else:
                line += ch
        out.append(line)
    return out

def header(d, spec):
    center(d, spec["title"], f("Bold", 64), W / 2, 60, TEXT)
    if spec.get("subtitle"):
        center(d, spec["subtitle"], f("Regular", 32), W / 2, 150, MUTED)
    if spec.get("footer"):
        center(d, spec["footer"], f("SemiBold", 30), W / 2, H - 90, ACCENTS[0])
    d.text((W - 260, H - 44), "[AI]Grit · aigrit.dev", font=f("Regular", 22), fill=MUTED)

def cards(d, spec):
    items = spec["items"]; n = len(items)
    gap = 36; mx = 70; cw = (W - 2 * mx - gap * (n - 1)) / n
    maxl = max(len(wrap(d, it.get("body", ""), f("Regular", 30), cw - 60)) for it in items)
    ch = 230 + maxl * 46 + 60
    top = 230 + max(0, (H - 160 - 230 - ch) / 2); bot = top + ch
    for i, it in enumerate(items):
        x = mx + i * (cw + gap); col = ACCENTS[i % len(ACCENTS)]
        d.rounded_rectangle([x, top, x + cw, bot], 28, fill=CARD, outline=col, width=5)
        center(d, it["head"], f("Bold", 52), x + cw / 2, top + 50, col)
        if it.get("sub"):
            center(d, it["sub"], f("SemiBold", 34), x + cw / 2, top + 135, TEXT)
        y = top + 230
        for ln in wrap(d, it.get("body", ""), f("Regular", 30), cw - 60):
            center(d, ln, f("Regular", 30), x + cw / 2, y, TEXT); y += 46

def flow(d, spec):
    items = spec["items"]; n = len(items)
    gap = 56; mx = 60; cw = (W - 2 * mx - gap * (n - 1)) / n
    hf, bf = f("Bold", 40), f("Regular", 32)
    hl = max(len(wrap(d, it["head"], hf, cw - 40)) for it in items)
    bl = max(len(wrap(d, it.get("body", ""), bf, cw - 40)) for it in items)
    ch = 70 + hl * 54 + 20 + bl * 46 + 50
    top = 260 + max(0, (H - 170 - 260 - ch) / 2); bot = top + ch
    for i, it in enumerate(items):
        x = mx + i * (cw + gap); col = ACCENTS[i % len(ACCENTS)]
        d.rounded_rectangle([x, top, x + cw, bot], 24, fill=CARD, outline=col, width=4)
        d.ellipse([x + cw / 2 - 34, top - 34, x + cw / 2 + 34, top + 34], fill=col)
        center(d, str(i + 1), f("Bold", 38), x + cw / 2, top - 24, BG)
        y = top + 70
        for ln in wrap(d, it["head"], hf, cw - 40):
            center(d, ln, hf, x + cw / 2, y, TEXT); y += 54
        y += 20
        for ln in wrap(d, it.get("body", ""), bf, cw - 40):
            center(d, ln, bf, x + cw / 2, y, MUTED); y += 46
        if i < n - 1:
            ax = x + cw + 8; ay = (top + bot) / 2
            d.polygon([(ax, ay - 16), (ax + gap - 16, ay), (ax, ay + 16)], fill=MUTED)

def table(d, spec):
    cols = spec["columns"]; rows = spec["rows"]; n = len(cols)
    mx = 90; top = 250; tw = W - 2 * mx
    widths = spec.get("widths") or [1] * n; tot = sum(widths)
    xs = [mx]; [xs.append(xs[-1] + tw * w / tot) for w in widths]
    rh = min(110, (H - 170 - top) / (len(rows) + 1))
    d.rounded_rectangle([mx, top, mx + tw, top + rh], 14, fill=ACCENTS[1])
    for j, c in enumerate(cols):
        center(d, c, f("Bold", 34), (xs[j] + xs[j + 1]) / 2, top + rh / 2 - 22, TEXT)
    for i, r in enumerate(rows):
        y = top + rh * (i + 1)
        if i % 2 == 0:
            d.rectangle([mx, y, mx + tw, y + rh], fill=CARD)
        for j, cell in enumerate(r):
            font = f("SemiBold" if j == 0 else "Regular", 34)
            center(d, cell, font, (xs[j] + xs[j + 1]) / 2, y + rh / 2 - 22, TEXT)

def render(spec):
    img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img)
    header(d, spec); {"cards": cards, "flow": flow, "table": table}[spec["kind"]](d, spec)
    out = Path(spec["out"]); out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, optimize=True); print("wrote", out)

if __name__ == "__main__":
    for s in json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")):
        render(s)
