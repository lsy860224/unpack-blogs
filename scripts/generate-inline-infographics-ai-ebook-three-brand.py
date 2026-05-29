#!/usr/bin/env python3
"""
Inline infographics for:
  - AIGrit  #19  ai-ebook-kindle-kdp  (4 charts, dark Indigo/Cyan)
  - babipanote #15  three-brand-strategy (1 diagram, Paper/Plum)

Brand specs mirror scripts/og/generate-og-all.py (same fonts, palettes) so the
inline visuals stay consistent with the OG cards and prior gpt-store infographics.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE = Path("/Users/seung-yeoblee/dev/unpack-blogs/apps")
AG_DIR = BASE / "aigrit" / "public" / "images" / "ai-ebook-kindle-kdp"
BB_DIR = BASE / "babipanote" / "public" / "images" / "three-brand-strategy"
AG_DIR.mkdir(parents=True, exist_ok=True)
BB_DIR.mkdir(parents=True, exist_ok=True)

F = {
    "pb": "/tmp/og-fonts/Pretendard-Bold.otf",
    "ps": "/tmp/og-fonts/Pretendard-SemiBold.otf",
    "pr": "/tmp/og-fonts/Pretendard-Regular.otf",
    "gb": "/tmp/og-fonts/GowunBatang-Bold.ttf",
}
def font(k, s): return ImageFont.truetype(F[k], s)

AG = {
    "bgTop": (15, 23, 42), "bgBot": (30, 27, 75),
    "card": (30, 41, 59), "cardLine": (51, 65, 85),
    "red": (239, 68, 68), "cyan": (6, 182, 212), "indigo": (79, 70, 229),
    "slate": (148, 163, 184), "slateDim": (100, 116, 139),
    "green": (16, 185, 129), "white": (255, 255, 255),
}
BB = {
    "plum": (107, 46, 78), "ink": (43, 36, 32), "terracotta": (200, 159, 124),
    "muted": (160, 139, 122), "paperLight": (250, 247, 242),
    "paperDeep": (240, 235, 227), "white": (255, 255, 255),
    "redEarth": (156, 74, 62),
}

def gradient(w, h, tl, br):
    img = Image.new("RGB", (w, h), tl)
    px = img.load()
    for y in range(h):
        t = y / h
        row = (int(tl[0]*(1-t)+br[0]*t), int(tl[1]*(1-t)+br[1]*t), int(tl[2]*(1-t)+br[2]*t))
        for x in range(w):
            px[x, y] = row
    return img

def rounded(draw, xy, r, fill=None, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)

def ctext(draw, cx, y, s, fnt, fill, anchor="ma"):
    draw.text((cx, y), s, font=fnt, fill=fill, anchor=anchor)

def tw(draw, s, fnt):
    return draw.textlength(s, font=fnt)


# ---------------------------------------------------------------- AIGrit 01
def royalty_structure():
    W, H = 1200, 680
    img = gradient(W, H, AG["bgTop"], AG["bgBot"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "Kindle KDP 권당 실수령액", font=font("pb", 42), fill=AG["white"])
    d.text((60, 104), "$2.99~$9.99 구간만 로열티 70% — 그 바깥은 35%",
           font=font("ps", 24), fill=AG["cyan"])

    bars = [
        ("$0.99", "35%", 0.35, AG["slate"]),
        ("$2.99", "70%", 2.03, AG["cyan"]),
        ("$4.99", "70%", 3.43, AG["cyan"]),
        ("$9.99", "70%", 6.89, AG["cyan"]),
        ("$14.99", "35%", 5.25, AG["red"]),
    ]
    base_y, top_y = 580, 250
    maxv = 6.89
    centers = [210 + i * 190 for i in range(5)]
    bw = 112

    # 70% zone band behind middle three bars
    zone_x1, zone_x2 = centers[1] - bw//2 - 22, centers[3] + bw//2 + 22
    band = Image.new("RGBA", (W, H), (0, 0, 0, 0)); bd = ImageDraw.Draw(band)
    rounded(bd, (zone_x1, top_y - 28, zone_x2, base_y), 16, fill=(6, 182, 212, 28))
    img = Image.alpha_composite(img.convert("RGBA"), band).convert("RGB"); d = ImageDraw.Draw(img)
    d.text(((zone_x1+zone_x2)//2, top_y - 26), "로열티 70% 구간",
           font=font("ps", 18), fill=AG["cyan"], anchor="ma")

    d.line([(60, base_y), (1140, base_y)], fill=AG["cardLine"], width=2)
    for (price, rate, val, col), cx in zip(bars, centers):
        h = int(val / maxv * (base_y - top_y))
        rounded(d, (cx - bw//2, base_y - h, cx + bw//2, base_y), 10, fill=col)
        d.text((cx, base_y - h - 34), f"${val:.2f}", font=font("pb", 26),
               fill=AG["white"], anchor="ma")
        d.text((cx, base_y + 14), price, font=font("ps", 22), fill=AG["white"], anchor="ma")
        d.text((cx, base_y + 44), f"({rate})", font=font("pr", 18), fill=AG["slate"], anchor="ma")

    # callouts
    d.text((centers[3], 184), "★ 최고 실수령", font=font("ps", 18), fill=AG["green"], anchor="ma")
    d.text((centers[4], base_y - int(5.25/maxv*(base_y-top_y)) - 64),
           "70% 이탈 → 손해", font=font("ps", 18), fill=AG["red"], anchor="ma")
    out = AG_DIR / "01-royalty-structure.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


# ---------------------------------------------------------------- AIGrit 02
def niche_selection():
    W, H = 1200, 660
    img = gradient(W, H, AG["bgTop"], AG["bgBot"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "팔리는 틈새 4조건", font=font("pb", 42), fill=AG["white"])
    d.text((60, 104), "베스트셀러가 아니라 '검색되는데 책이 부족한 좁은 틈새'",
           font=font("ps", 24), fill=AG["cyan"])

    cards = [
        ("1", "검색 수요 존재", "Amazon 자동완성에 뜨고", "리뷰 50+ = 사는 사람이 있다"),
        ("2", "경쟁서 부족", "정확히 그 주제 책 30권 미만", "레드오션 회피"),
        ("3", "명확한 ICP", "'누가 사는가'가 한 문장", "예: 이직 준비 3년차 마케터"),
        ("4", "시리즈 확장성", "1권 성공 → 2·3권으로", "잇기 좋은 구조"),
    ]
    cw, ch, gx, gy = 530, 200, 20, 24
    x0, y0 = 60, 188
    for i, (n, title, l1, l2) in enumerate(cards):
        cx = x0 + (i % 2) * (cw + gx)
        cy = y0 + (i // 2) * (ch + gy)
        rounded(d, (cx, cy, cx + cw, cy + ch), 18, fill=AG["card"], outline=AG["cardLine"], width=2)
        d.ellipse((cx + 28, cy + 30, cx + 28 + 52, cy + 30 + 52), fill=AG["cyan"])
        d.text((cx + 28 + 26, cy + 30 + 26), n, font=font("pb", 30), fill=AG["bgTop"], anchor="mm")
        d.text((cx + 104, cy + 36), title, font=font("pb", 30), fill=AG["white"])
        d.text((cx + 104, cy + 92), l1, font=font("pr", 21), fill=AG["slate"])
        d.text((cx + 104, cy + 126), l2, font=font("pr", 21), fill=AG["slate"])
    out = AG_DIR / "02-niche-selection.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


# ---------------------------------------------------------------- AIGrit 03
def upload_flow():
    W, H = 1200, 440
    img = gradient(W, H, AG["bgTop"], AG["bgBot"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "KDP 업로드 흐름", font=font("pb", 42), fill=AG["white"])
    d.text((60, 104), "원고가 끝나면 출판은 빠르다 — 막히는 곳은 표지와 등록 옵션",
           font=font("ps", 22), fill=AG["cyan"])

    nodes = [
        ("원고", "EPUB", AG["indigo"]),
        ("표지", "1600×2560", AG["indigo"]),
        ("메타데이터", "카테고리·키워드", AG["indigo"]),
        ("KDP Select", "독점 여부", AG["cyan"]),
        ("가격", "$2.99~9.99", AG["indigo"]),
        ("검수", "24~72h", AG["green"]),
    ]
    nw, nh = 156, 104
    cy = 250
    centers = [138 + i * 186 for i in range(6)]
    for i, ((t1, t2, col), cx) in enumerate(zip(nodes, centers)):
        x1, x2 = cx - nw//2, cx + nw//2
        rounded(d, (x1, cy - nh//2, x2, cy + nh//2), 14, fill=AG["card"], outline=col, width=3)
        d.text((cx, cy - 22), t1, font=font("pb", 24), fill=AG["white"], anchor="ma")
        d.text((cx, cy + 14), t2, font=font("pr", 18), fill=AG["slate"], anchor="ma")
        if i < 5:
            ax = x2 + 8; axe = centers[i+1] - nw//2 - 8
            d.line([(ax, cy), (axe, cy)], fill=AG["slateDim"], width=3)
            d.polygon([(axe, cy-7), (axe, cy+7), (axe+10, cy)], fill=AG["slateDim"])
    out = AG_DIR / "03-kdp-upload-flow.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


# ---------------------------------------------------------------- AIGrit 04
def revenue_curve():
    W, H = 1200, 680
    img = gradient(W, H, AG["bgTop"], AG["bgBot"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "3권 × 3개월 누적 매출", font=font("pb", 42), fill=AG["white"])
    d.text((60, 104), "영문 실용서 1권이 매출 80% — M3부터 잔존 매출 본격화",
           font=font("ps", 24), fill=AG["cyan"])

    # months: each stacked (EN, KR, ChatGPT)
    months = [
        ("M1", 31, 9, 4),
        ("M2", 58, 11, 6),
        ("M3", 82, 7, 6),
    ]
    seg_cols = [AG["cyan"], AG["indigo"], AG["slate"]]
    base_y, top_y = 580, 220
    maxv = 95
    centers = [310, 600, 890]
    bw = 150
    d.line([(60, base_y), (1140, base_y)], fill=AG["cardLine"], width=2)
    for (label, en, kr, cg), cx in zip(months, centers):
        total = en + kr + cg
        y = base_y
        for val, col in zip((en, kr, cg), seg_cols):
            h = int(val / maxv * (base_y - top_y))
            rounded(d, (cx - bw//2, y - h, cx + bw//2, y), 6, fill=col)
            y -= h + 2
        d.text((cx, y - 38), f"${total}", font=font("pb", 30), fill=AG["white"], anchor="ma")
        d.text((cx, base_y + 14), label, font=font("ps", 24), fill=AG["white"], anchor="ma")

    # legend
    lx, ly = 60, 612
    legend = [("원격근무 노션(영문)", AG["cyan"]),
              ("국문판", AG["indigo"]),
              ("ChatGPT 자동화(영문)", AG["slate"])]
    for name, col in legend:
        d.rectangle((lx, ly, lx + 22, ly + 22), fill=col)
        d.text((lx + 32, ly + 1), name, font=font("pr", 20), fill=AG["slate"])
        lx += tw(d, name, font("pr", 20)) + 90
    out = AG_DIR / "04-3month-revenue.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


# ---------------------------------------------------------------- babipanote 01
def tone_conflict():
    W, H = 1200, 620
    img = gradient(W, H, BB["paperLight"], BB["paperDeep"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "한 브랜드에 톤을 섞으면", font=font("gb", 44), fill=BB["ink"])
    d.text((60, 116), "한 사람이 세 톤을 가질 수는 있다. 한 브랜드가 동시에 내면 정체성이 흐려진다.",
           font=font("pr", 22), fill=BB["muted"])

    # umbrella label
    d.rounded_rectangle((430, 178, 770, 226), radius=24, fill=BB["ink"])
    d.text((600, 184), "한 지붕 아래", font=font("gb", 26), fill=BB["paperLight"], anchor="ma")
    # connectors
    for cx in (240, 600, 960):
        d.line([(600, 226), (cx, 286)], fill=BB["terracotta"], width=3)

    boxes = [
        ("공격적 SEO 수익 글", "키워드·제휴 링크", BB["plum"]),
        ("솔직한 실패 저널", "0원·실수 그대로", BB["redEarth"]),
        ("절제된 앱", "광고 없는 무드", BB["muted"]),
    ]
    bw, bh, y = 320, 150, 290
    centers = [240, 600, 960]
    for (t1, t2, col), cx in zip(boxes, centers):
        x1, x2 = cx - bw//2, cx + bw//2
        rounded(d, (x1, y, x2, y + bh), 18, fill=BB["white"], outline=col, width=3)
        d.rounded_rectangle((x1, y, x1 + 10, y + bh), radius=0, fill=col)
        d.text((cx + 6, y + 34), t1, font=font("gb", 26), fill=BB["ink"], anchor="ma")
        d.text((cx + 6, y + 84), t2, font=font("pr", 20), fill=BB["muted"], anchor="ma")

    # downward arrow + result
    d.line([(600, 460), (600, 502)], fill=BB["plum"], width=4)
    d.polygon([(590, 500), (610, 500), (600, 516)], fill=BB["plum"])
    d.rounded_rectangle((300, 528, 900, 588), radius=18, fill=BB["plum"])
    d.text((600, 540), "독자는 이 브랜드가 무엇인지 알 수 없다 → 셋 다 약해진다",
           font=font("gb", 24), fill=BB["paperLight"], anchor="ma")
    out = BB_DIR / "01-tone-conflict.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


if __name__ == "__main__":
    royalty_structure()
    niche_selection()
    upload_flow()
    revenue_curve()
    tone_conflict()
    print("\n✅ inline infographics done.")
