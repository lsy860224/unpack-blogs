#!/usr/bin/env python3
"""
Inline infographics for:
  - AIGrit  #21  prompt-engineering-freelance (3 charts, Indigo/Cyan dark)
  - babipanote #17 my-pkm-stack-2026 (Pillar, 3 diagrams, Paper/Plum)
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE = Path("/Users/seung-yeoblee/dev/unpack-blogs/apps")
AG_DIR = BASE / "aigrit" / "public" / "images" / "prompt-engineering-freelance"
BB_DIR = BASE / "babipanote" / "public" / "images" / "my-pkm-stack-2026"
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
    "amber": (245, 158, 11),
}
BB = {
    "plum": (107, 46, 78), "ink": (43, 36, 32), "terracotta": (200, 159, 124),
    "muted": (160, 139, 122), "paperLight": (250, 247, 242),
    "paperDeep": (240, 235, 227), "white": (255, 255, 255),
    "redEarth": (156, 74, 62), "greenEarth": (107, 138, 99),
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


# ---------------------------------------------------------------- AIGrit 01
def market_overview():
    W, H = 1200, 620
    img = gradient(W, H, AG["bgTop"], AG["bgBot"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "크몽 vs Upwork — 프롬프트 엔지니어 시장 (2026-Q2)",
           font=font("pb", 36), fill=AG["white"])
    d.text((60, 100), "크몽은 진입장벽 낮음·국내 결제 / Upwork는 단가 높음·영어 통신",
           font=font("ps", 22), fill=AG["cyan"])

    cols = [
        ("크몽",        "3,400건",  "₩50,000",  "1~4주",  "국내 입금",        AG["green"]),
        ("Upwork",      "41,000건", "$30",       "1~8주",  "Payoneer/Wise",    AG["cyan"]),
    ]
    rows_label = ["등록 서비스 수", "평균 시작 단가", "프로젝트 기간", "정산 방식"]
    cw, ch, y0 = 530, 380, 168
    gx = 40
    x0 = 60
    for i, (name, *vals, col) in enumerate(cols):
        x = x0 + i * (cw + gx)
        rounded(d, (x, y0, x + cw, y0 + ch), 18, fill=AG["card"], outline=col, width=3)
        d.rounded_rectangle((x, y0, x + cw, y0 + 70), radius=18, fill=col)
        d.text((x + cw//2, y0 + 20), name, font=font("pb", 32), fill=AG["bgTop"], anchor="ma")
        for j, (lbl, val) in enumerate(zip(rows_label, vals)):
            yy = y0 + 102 + j * 68
            d.text((x + 26, yy), lbl, font=font("pr", 20), fill=AG["slate"])
            d.text((x + cw - 26, yy - 2), val, font=font("pb", 26), fill=AG["white"], anchor="ra")
            d.line([(x + 26, yy + 40), (x + cw - 26, yy + 40)], fill=AG["cardLine"], width=1)
    out = AG_DIR / "01-market-overview.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


# ---------------------------------------------------------------- AIGrit 02
def packages_compare():
    W, H = 1200, 660
    img = gradient(W, H, AG["bgTop"], AG["bgBot"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "팔리는 패키지 3종 — 11건 매출 비중", font=font("pb", 40), fill=AG["white"])
    d.text((60, 104), "ChatGPT 업무 자동화 시스템이 매출 68% — ROI 환산 가능한 패키지가 본질",
           font=font("ps", 22), fill=AG["cyan"])

    items = [
        ("자동화 시스템",      "₩280k~₩520k", "2~3주", "6건", 68, AG["cyan"]),
        ("사내 활용 가이드",   "₩150k~₩240k", "1~2주", "3건", 21, AG["indigo"]),
        ("도입 컨설팅",        "₩220k",        "1주",   "2건", 11, AG["slate"]),
    ]
    cw, ch, y0 = 350, 380, 178
    gx = 30
    x0 = 60
    for i, (name, price, dur, cnt, share, col) in enumerate(items):
        x = x0 + i * (cw + gx)
        rounded(d, (x, y0, x + cw, y0 + ch), 18, fill=AG["card"], outline=col, width=3)
        # share badge top
        d.rounded_rectangle((x, y0, x + cw, y0 + 70), radius=18, fill=col)
        d.text((x + cw//2, y0 + 20), f"매출 {share}%", font=font("pb", 28), fill=AG["bgTop"], anchor="ma")
        d.text((x + 26, y0 + 90), name, font=font("pb", 26), fill=AG["white"])
        rows = [("단가", price), ("기간", dur), ("11건 중", cnt)]
        for j, (lbl, val) in enumerate(rows):
            yy = y0 + 156 + j * 60
            d.text((x + 26, yy), lbl, font=font("pr", 20), fill=AG["slate"])
            d.text((x + cw - 26, yy - 2), val, font=font("pb", 22), fill=AG["white"], anchor="ra")
            d.line([(x + 26, yy + 36), (x + cw - 26, yy + 36)], fill=AG["cardLine"], width=1)
    out = AG_DIR / "02-packages.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


# ---------------------------------------------------------------- AIGrit 03
def platform_revenue():
    W, H = 1200, 640
    img = gradient(W, H, AG["bgTop"], AG["bgBot"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "3개월 누적 매출 — 크몽 vs Upwork", font=font("pb", 40), fill=AG["white"])
    d.text((60, 104), "크몽 ₩820k(8건) · Upwork ₩382k(3건) · 합계 ₩1,202,000 (시급 ₩18,500)",
           font=font("ps", 22), fill=AG["cyan"])

    # 2 grouped bars (총 매출 + 시급)
    bars = [
        ("크몽",   820, "₩820,000", 8, AG["green"]),
        ("Upwork", 382, "₩382,000", 3, AG["cyan"]),
    ]
    base_y, top_y = 560, 220
    maxv = 820
    centers = [400, 800]
    bw = 220
    d.line([(60, base_y), (1140, base_y)], fill=AG["cardLine"], width=2)
    for (label, val, vlabel, cnt, col), cx in zip(bars, centers):
        h = int(val / maxv * (base_y - top_y))
        rounded(d, (cx - bw//2, base_y - h, cx + bw//2, base_y), 12, fill=col)
        d.text((cx, base_y - h - 42), vlabel, font=font("pb", 30), fill=AG["white"], anchor="ma")
        d.text((cx, base_y + 16), label, font=font("ps", 26), fill=AG["white"], anchor="ma")
        d.text((cx, base_y + 52), f"수주 {cnt}건", font=font("pr", 20), fill=AG["slate"], anchor="ma")
    # right-side summary box
    rounded(d, (1000, 240, 1140, 380), 14, fill=AG["card"], outline=AG["amber"], width=2)
    d.text((1070, 256), "합계", font=font("ps", 20), fill=AG["amber"], anchor="ma")
    d.text((1070, 290), "₩1.2M", font=font("pb", 28), fill=AG["white"], anchor="ma")
    d.text((1070, 332), "시급", font=font("ps", 16), fill=AG["slate"], anchor="ma")
    d.text((1070, 352), "₩18,500", font=font("pb", 20), fill=AG["amber"], anchor="ma")
    out = AG_DIR / "03-platform-revenue.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


# ---------------------------------------------------------------- babipanote 01
def three_tools_roles():
    W, H = 1200, 660
    img = gradient(W, H, BB["paperLight"], BB["paperDeep"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "3-도구 PKM 스택 — 역할 분담", font=font("gb", 42), fill=BB["ink"])
    d.text((60, 116), "한 도구로 다 하지 않는다. 각자 잘하는 자리에서만 일한다.",
           font=font("pr", 22), fill=BB["muted"])

    cards = [
        ("Obsidian",      "영구 기억",     ["노트·일기", "회의록·자료", "PARA 4 폴더"], BB["plum"]),
        ("Craft",         "글 초안",       ["블로그 초안", "기획 카드", "협업·코멘트"], BB["redEarth"]),
        ("Claude (MCP)",  "자동 처리",     ["검색·요약", "노트 확장", "발행 자동화"],   BB["greenEarth"]),
    ]
    cw, ch, y0 = 350, 400, 180
    gx = 30
    x0 = 60
    for i, (name, role, items, col) in enumerate(cards):
        x = x0 + i * (cw + gx)
        rounded(d, (x, y0, x + cw, y0 + ch), 18, fill=BB["white"], outline=col, width=3)
        # left index strip
        d.rounded_rectangle((x, y0, x + 10, y0 + ch), radius=0, fill=col)
        d.text((x + 30, y0 + 28), name, font=font("gb", 30), fill=BB["ink"])
        d.text((x + 30, y0 + 76), role, font=font("pr", 20), fill=col)
        d.line([(x + 30, y0 + 116), (x + cw - 30, y0 + 116)], fill=BB["paperDeep"], width=2)
        for j, it in enumerate(items):
            yy = y0 + 138 + j * 56
            d.ellipse((x + 30, yy + 8, x + 42, yy + 20), fill=col)
            d.text((x + 56, yy), it, font=font("ps", 22), fill=BB["ink"])
    # bottom arrow strip
    d.text((600, 600), "Obsidian → Claude → Craft → 발행",
           font=font("ps", 22), fill=BB["plum"], anchor="ma")
    out = BB_DIR / "01-three-tools-roles.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


# ---------------------------------------------------------------- babipanote 02
def workflow_5steps():
    W, H = 1200, 460
    img = gradient(W, H, BB["paperLight"], BB["paperDeep"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "아이디어 → 발행 5단계", font=font("gb", 42), fill=BB["ink"])
    d.text((60, 118), "도구 사이의 복사·붙여넣기 마찰을 MCP가 0에 가깝게 줄였다.",
           font=font("pr", 22), fill=BB["muted"])

    steps = [
        ("1", "캡처",       "Obsidian Inbox",     BB["plum"]),
        ("2", "확장",       "Claude (MCP)",        BB["redEarth"]),
        ("3", "초안",       "Craft",               BB["terracotta"]),
        ("4", "검증",       "Claude",              BB["redEarth"]),
        ("5", "발행",       "MDX 자동",            BB["greenEarth"]),
    ]
    nw, nh, cy = 190, 130, 290
    centers = [125 + i * 232 for i in range(5)]
    for i, ((n, name, tool, col), cx) in enumerate(zip(steps, centers)):
        x1, x2 = cx - nw//2, cx + nw//2
        rounded(d, (x1, cy - nh//2, x2, cy + nh//2), 16, fill=BB["white"], outline=col, width=3)
        # number badge top-left
        d.ellipse((x1 + 12, cy - nh//2 + 12, x1 + 50, cy - nh//2 + 50), fill=col)
        d.text((x1 + 31, cy - nh//2 + 31), n, font=font("gb", 22), fill=BB["paperLight"], anchor="mm")
        d.text((cx + 14, cy - 22), name, font=font("gb", 26), fill=BB["ink"], anchor="ma")
        d.text((cx + 14, cy + 16), tool, font=font("pr", 18), fill=BB["muted"], anchor="ma")
        if i < 4:
            ax = x2 + 6; axe = centers[i+1] - nw//2 - 6
            d.line([(ax, cy), (axe, cy)], fill=BB["terracotta"], width=3)
            d.polygon([(axe, cy-7), (axe, cy+7), (axe+10, cy)], fill=BB["terracotta"])
    out = BB_DIR / "02-workflow.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


# ---------------------------------------------------------------- babipanote 03
def one_year_metrics():
    W, H = 1200, 660
    img = gradient(W, H, BB["paperLight"], BB["paperDeep"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "1년치 PKM 스택 지표 (2025-05 ~ 2026-05)",
           font=font("gb", 38), fill=BB["ink"])
    d.text((60, 116), "노트가 늘어난 게 아니다. *다시 열리는 노트*가 늘었다.",
           font=font("pr", 22), fill=BB["muted"])

    metrics = [
        ("3,200",   "Obsidian 노트", "PARA 4 폴더",        BB["plum"]),
        ("178",     "Craft 문서",     "블로그 + 기획 카드", BB["redEarth"]),
        ("2,400",   "MCP 호출",       "도구 사이의 대화",   BB["greenEarth"]),
        ("64",      "발행 글",        "3 채널 합산",        BB["plum"]),
        ("95h",     "검색 시간 절감", "MCP 자동 검색",      BB["redEarth"]),
        ("72%",     "Inbox 전환율",   "단편 → 노트·글",     BB["greenEarth"]),
    ]
    cw, ch, gx, gy = 360, 156, 20, 22
    x0, y0 = 60, 180
    for i, (n, head, sub, col) in enumerate(metrics):
        cx = x0 + (i % 3) * (cw + gx)
        cy = y0 + (i // 3) * (ch + gy)
        rounded(d, (cx, cy, cx + cw, cy + ch), 16, fill=BB["white"], outline=col, width=3)
        d.rounded_rectangle((cx, cy, cx + 10, cy + ch), radius=0, fill=col)
        d.text((cx + 28, cy + 18), n, font=font("gb", 42), fill=BB["ink"])
        d.text((cx + 28, cy + 80), head, font=font("ps", 22), fill=col)
        d.text((cx + 28, cy + 114), sub, font=font("pr", 18), fill=BB["muted"])
    # bottom takeaway strip
    d.rounded_rectangle((300, 540, 900, 596), radius=18, fill=BB["plum"])
    d.text((600, 552), "노트당 평균 재방문 1.4회 (단일 도구 시기엔 0회 60%+)",
           font=font("gb", 22), fill=BB["paperLight"], anchor="ma")
    out = BB_DIR / "03-1year-metrics.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


if __name__ == "__main__":
    market_overview()
    packages_compare()
    platform_revenue()
    three_tools_roles()
    workflow_5steps()
    one_year_metrics()
    print("\n✅ inline infographics done.")
