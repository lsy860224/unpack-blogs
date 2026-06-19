#!/usr/bin/env python3
"""
Reusable inline-infographic generator for UnpackBlogs (AIGrit + babipanote).

Replaces the per-batch bespoke scripts with one spec-driven renderer.
Input: a JSON specs file (default /tmp/infographic-specs.json), shape:

{
  "items": [
    {
      "blog": "aigrit" | "babipanote",
      "slug": "post-slug",
      "charts": [
        {"file": "01-overview.png", "type": "comparison_table",
         "title": "...", "subtitle": "...",
         "columns": ["", "A", "B", "C"],
         "rows": [["항목", "v1", "v2", "v3"], ...],
         "highlight_col": 2 },
        {"file": "02-scores.png", "type": "score_bars",
         "title": "...", "subtitle": "...",
         "criteria": ["쉬움","가격",...],
         "series": [{"name":"A","color":"cyan","scores":[4,5,...]}, ...]},
        {"file": "03-flow.png", "type": "decision_flow",
         "title": "...", "subtitle":"...",
         "nodes": [{"q":"질문?","yes":"추천 A","no":"→ 다음"}, ...]},
        {"file": "04-pipeline.png", "type": "pipeline",
         "title":"...","subtitle":"...","steps":["단계1","단계2",...]},
        {"file": "05-stats.png", "type": "stat_cards",
         "title":"...","subtitle":"...",
         "cards":[{"big":"38%","label":"설명"}, ...]}
      ]
    }
  ]
}

Usage: python3 scripts/gen-infographics.py [specs.json]
"""
import json, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE = Path("/Users/seung-yeoblee/dev/unpack-blogs/apps")
F = {
    "pb": "/tmp/og-fonts/Pretendard-Bold.otf",
    "ps": "/tmp/og-fonts/Pretendard-SemiBold.otf",
    "pr": "/tmp/og-fonts/Pretendard-Regular.otf",
    "gb": "/tmp/og-fonts/GowunBatang-Bold.ttf",
}
_fc = {}
def font(k, s):
    key = (k, s)
    if key not in _fc:
        _fc[key] = ImageFont.truetype(F[k], s)
    return _fc[key]

# Brand themes
AG = {
    "bgTop": (15, 23, 42), "bgBot": (30, 27, 75),
    "card": (30, 41, 59), "cardLine": (51, 65, 85),
    "red": (239, 68, 68), "cyan": (6, 182, 212), "indigo": (99, 102, 241),
    "slate": (148, 163, 184), "slateDim": (100, 116, 139),
    "green": (16, 185, 129), "white": (255, 255, 255), "amber": (245, 158, 11),
    "accent": (6, 182, 212), "head": (255, 255, 255), "sub": (6, 182, 212),
    "titlefont": "pb",
}
BB = {
    "bgTop": (250, 247, 242), "bgBot": (240, 235, 227),
    "card": (255, 255, 255), "cardLine": (224, 214, 201),
    "red": (156, 74, 62), "cyan": (147, 110, 132), "indigo": (107, 46, 78),
    "slate": (120, 104, 92), "slateDim": (160, 139, 122),
    "green": (107, 138, 99), "white": (255, 255, 255), "amber": (185, 138, 92),
    "accent": (200, 159, 124), "head": (43, 36, 32), "sub": (107, 46, 78),
    "titlefont": "gb",
}
COLORMAP = {"cyan": "cyan", "indigo": "indigo", "green": "green",
            "red": "red", "amber": "amber", "slate": "slate"}

def theme(blog):
    return AG if blog == "aigrit" else BB

def gradient(w, h, tl, br):
    img = Image.new("RGB", (w, h), tl); px = img.load()
    for y in range(h):
        t = y / h
        row = (int(tl[0]*(1-t)+br[0]*t), int(tl[1]*(1-t)+br[1]*t), int(tl[2]*(1-t)+br[2]*t))
        for x in range(w):
            px[x, y] = row
    return img

def rounded(d, xy, r, fill=None, outline=None, width=1):
    d.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)

def wrap(d, text, f, maxw):
    words = text.split(" "); lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    # hard-break long tokens
    out = []
    for ln in lines:
        if d.textlength(ln, font=f) <= maxw: out.append(ln); continue
        buf = ""
        for ch in ln:
            if d.textlength(buf+ch, font=f) <= maxw: buf += ch
            else: out.append(buf); buf = ch
        if buf: out.append(buf)
    return out

def header(d, T, title, subtitle, W):
    d.text((60, 46), title, font=font(T["titlefont"], 40), fill=T["head"])
    if subtitle:
        for i, ln in enumerate(wrap(d, subtitle, font("ps", 22), W-120)):
            d.text((60, 100 + i*30), ln, font=font("ps", 22), fill=T["sub"])

# ---------- templates ----------
def comparison_table(spec, T):
    cols = spec["columns"]; rows = spec["rows"]
    ncol = len(cols)
    W = 1200; top = 168
    rowh = 64; H = top + 60 + rowh*(len(rows)+1) + 50
    img = gradient(W, H, T["bgTop"], T["bgBot"]); d = ImageDraw.Draw(img)
    header(d, T, spec["title"], spec.get("subtitle",""), W)
    x0, x1 = 60, W-60
    tw = x1 - x0
    c0 = int(tw*0.26); rest = tw - c0
    cw = rest // (ncol-1)
    xs = [x0] + [x0 + c0 + i*cw for i in range(ncol)]
    hl = spec.get("highlight_col")
    y = top + 50
    rounded(d, (x0, y, x1, y+rowh*(len(rows)+1)), 16, fill=T["card"], outline=T["cardLine"], width=2)
    # header row
    for ci, ct in enumerate(cols):
        cx = xs[ci] + (12 if ci==0 else (cw//2))
        col = T["accent"] if (hl is not None and ci==hl) else T["head"]
        anchor = "lm" if ci==0 else "mm"
        d.text((cx, y+rowh//2), str(ct), font=font("pb", 23), fill=col, anchor=anchor)
    d.line((x0+12, y+rowh, x1-12, y+rowh), fill=T["cardLine"], width=2)
    for ri, row in enumerate(rows):
        ry = y + rowh*(ri+1)
        if hl is not None and 0 <= hl < ncol:
            hx0 = xs[hl] if hl>0 else x0
            hx1 = (xs[hl]+cw if hl < ncol-1 else x1) - 2
            if hx1 > hx0 + 2:
                d.rectangle((hx0, ry+2, hx1, ry+rowh-2), fill=T["cardLine"])
        for ci, cell in enumerate(row):
            cx = xs[ci] + (12 if ci==0 else (cw//2))
            anchor = "lm" if ci==0 else "mm"
            fnt = font("ps", 20) if ci==0 else font("pb" if (hl is not None and ci==hl) else "ps", 20)
            col = T["accent"] if (hl is not None and ci==hl) else (T["head"] if ci==0 else T["slate"] if T is AG else T["ink"] if False else T["head"])
            txt = str(cell)
            if d.textlength(txt, font=fnt) > (c0-20 if ci==0 else cw-16):
                fnt = font("ps", 16)
            d.text((cx, ry+rowh//2), txt, font=fnt, fill=col, anchor=anchor)
        if ri < len(rows)-1:
            d.line((x0+12, ry+rowh, x1-12, ry+rowh), fill=T["cardLine"], width=1)
    return img

def score_bars(spec, T):
    crit = spec["criteria"]; series = spec["series"]
    W = 1200; top = 168
    bar_area_y = top + 60
    rowgap = 70; H = bar_area_y + rowgap*len(crit) + 60
    img = gradient(W, H, T["bgTop"], T["bgBot"]); d = ImageDraw.Draw(img)
    header(d, T, spec["title"], spec.get("subtitle",""), W)
    # legend
    lx = 60
    for s in series:
        col = T[COLORMAP.get(s.get("color","cyan"),"cyan")]
        d.ellipse((lx, top+18, lx+18, top+36), fill=col)
        d.text((lx+26, top+16), s["name"], font=font("ps", 20), fill=T["head"])
        lx += 40 + d.textlength(s["name"], font=font("ps",20)) + 26
    label_w = 150; bx0 = 60+label_w; bx1 = W-90; bw = bx1-bx0
    maxv = 5
    for ri, c in enumerate(crit):
        ry = bar_area_y + ri*rowgap
        d.text((60, ry+ (len(series)*22)//2 - 6), c, font=font("ps", 20), fill=T["head"])
        for si, s in enumerate(series):
            col = T[COLORMAP.get(s.get("color","cyan"),"cyan")]
            v = s["scores"][ri]; bh = 18
            yy = ry + si*22
            d.rounded_rectangle((bx0, yy, bx0+bw, yy+bh), radius=9, fill=T["card"])
            fillw = int(bw * (v/maxv))
            if fillw > 18:
                d.rounded_rectangle((bx0, yy, bx0+fillw, yy+bh), radius=9, fill=col)
            d.text((bx0+bw+10, yy-2), str(v), font=font("pb", 18), fill=col)
    return img

def decision_flow(spec, T):
    nodes = spec["nodes"]
    W = 1200; top = 168
    ny = top + 60; nh = 92; gap = 26
    H = ny + (nh+gap)*len(nodes) + 50
    img = gradient(W, H, T["bgTop"], T["bgBot"]); d = ImageDraw.Draw(img)
    header(d, T, spec["title"], spec.get("subtitle",""), W)
    x0, x1 = 60, W-60
    for i, n in enumerate(nodes):
        y = ny + i*(nh+gap)
        rounded(d, (x0, y, x1, y+nh), 16, fill=T["card"], outline=T["cardLine"], width=2)
        # question
        d.text((x0+28, y+18), "Q", font=font("pb", 22), fill=T["accent"])
        for li, ln in enumerate(wrap(d, n["q"], font("pb", 23), 560)):
            d.text((x0+60, y+16+li*30), ln, font=font("pb", 23), fill=T["head"])
        # yes recommendation chip
        rx = x1-360
        d.rounded_rectangle((rx, y+20, x1-28, y+nh-20), radius=12, fill=T["green"])
        ytext = n.get("yes","")
        fnt = font("pb", 21)
        if d.textlength(ytext, font=fnt) > 300: fnt = font("pb", 17)
        d.text(((rx+x1-28)//2, y+nh//2), ytext, font=fnt, fill=(255,255,255), anchor="mm")
        if i < len(nodes)-1:
            cx = x0+40
            d.line((cx, y+nh, cx, y+nh+gap), fill=T["slateDim"], width=3)
    return img

def pipeline(spec, T):
    steps = spec["steps"]
    has_desc = any(isinstance(s, dict) and s.get("desc") for s in steps)
    bh = 210 if has_desc else 130
    W = 1200; top = 168
    img_h = top + 90 + bh + 40
    img = gradient(W, img_h, T["bgTop"], T["bgBot"]); d = ImageDraw.Draw(img)
    header(d, T, spec["title"], spec.get("subtitle",""), W)
    n = len(steps); x0 = 60; x1 = W-60; tw = x1-x0
    gap = 30 if n <= 5 else 20; bw = (tw - gap*(n-1)) // n
    y = top + 90
    for i, st in enumerate(steps):
        x = x0 + i*(bw+gap)
        col = T["accent"] if i == n-1 else T["card"]
        rounded(d, (x, y, x+bw, y+bh), 16, fill=col, outline=T["cardLine"], width=2)
        d.ellipse((x+bw//2-18, y+18, x+bw//2+18, y+54), fill=T["bgTop"] if i==n-1 else T["accent"])
        d.text((x+bw//2, y+24), str(i+1), font=font("pb", 22),
               fill=T["accent"] if i==n-1 else T["bgTop"], anchor="ma")
        tc = T["bgTop"] if i==n-1 else T["head"]
        # step may be a string, or {"label":..,"desc":..}
        label = st["label"] if isinstance(st, dict) else st
        desc = st.get("desc") if isinstance(st, dict) else None
        lab_lines = wrap(d, label, font("pb", 19), bw-20)[:2]
        ly = y+64
        for li, ln in enumerate(lab_lines):
            d.text((x+bw//2, ly+li*23), ln, font=font("pb", 19), fill=tc, anchor="ma")
        if desc:
            dy = ly + len(lab_lines)*23 + 4
            dc = T["bgTop"] if i==n-1 else (T["slate"] if T is AG else T["slateDim"])
            for li, ln in enumerate(wrap(d, desc, font("pr", 15), bw-22)[:3]):
                d.text((x+bw//2, dy+li*19), ln, font=font("pr", 15), fill=dc, anchor="ma")
        if i < n-1:
            ay = y+bh//2
            d.line((x+bw+6, ay, x+bw+gap-6, ay), fill=T["slateDim"], width=3)
            d.polygon([(x+bw+gap-6, ay-6),(x+bw+gap-6, ay+6),(x+bw+gap, ay)], fill=T["slateDim"])
    return img

def stat_cards(spec, T):
    cards = spec["cards"]
    W = 1200; top = 168
    H = top + 60 + 230
    img = gradient(W, H, T["bgTop"], T["bgBot"]); d = ImageDraw.Draw(img)
    header(d, T, spec["title"], spec.get("subtitle",""), W)
    n = len(cards); x0=60; x1=W-60; tw=x1-x0; gap=24
    cw = (tw - gap*(n-1))//n; y = top+80; ch = 180
    palette = ["cyan","indigo","green","amber"]
    for i, c in enumerate(cards):
        x = x0 + i*(cw+gap)
        col = T[COLORMAP.get(c.get("color", palette[i%4]), "cyan")]
        rounded(d, (x, y, x+cw, y+ch), 16, fill=T["card"], outline=col, width=3)
        d.text((x+cw//2, y+34), str(c["big"]), font=font("pb", 52), fill=col, anchor="ma")
        for li, ln in enumerate(wrap(d, c["label"], font("ps", 20), cw-30)[:3]):
            d.text((x+cw//2, y+112+li*26), ln, font=font("ps", 20), fill=T["head"], anchor="ma")
    return img

RENDER = {
    "comparison_table": comparison_table, "score_bars": score_bars,
    "decision_flow": decision_flow, "pipeline": pipeline, "stat_cards": stat_cards,
}

def main():
    sppath = sys.argv[1] if len(sys.argv) > 1 else "/tmp/infographic-specs.json"
    data = json.loads(Path(sppath).read_text(encoding="utf-8"))
    count = 0
    for item in data["items"]:
        blog = item["blog"]; slug = item["slug"]; T = theme(blog)
        out_dir = BASE / blog / "public" / "images" / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        for ch in item["charts"]:
            fn = RENDER[ch["type"]]
            img = fn(ch, T)
            out = out_dir / ch["file"]
            img.save(out, "PNG", optimize=True)
            count += 1
            print(f"✓ {blog}/{slug}/{ch['file']}  ({out.stat().st_size/1024:.0f}KB)")
    print(f"\n✅ {count} infographics generated.")

if __name__ == "__main__":
    main()
