#!/usr/bin/env python3
"""
Inline infographics for:
  - AIGrit  #22  ai-newsletter-substack-growth (3 charts, Indigo/Cyan dark)
  - babipanote #18 obsidian-folder-structure-final (2 diagrams, Paper/Plum)
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE = Path("/Users/seung-yeoblee/dev/unpack-blogs/apps")
AG_DIR = BASE / "aigrit" / "public" / "images" / "ai-newsletter-substack-growth"
BB_DIR = BASE / "babipanote" / "public" / "images" / "obsidian-folder-structure-final"
AG_DIR.mkdir(parents=True, exist_ok=True)
BB_DIR.mkdir(parents=True, exist_ok=True)

F = {
    "pb": "/tmp/og-fonts/Pretendard-Bold.otf",
    "ps": "/tmp/og-fonts/Pretendard-SemiBold.otf",
    "pr": "/tmp/og-fonts/Pretendard-Regular.otf",
    "gb": "/tmp/og-fonts/GowunBatang-Bold.ttf",
    "mono": "/tmp/og-fonts/Pretendard-SemiBold.otf",
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
def newsletter_formats():
    W, H = 1200, 620
    img = gradient(W, H, AG["bgTop"], AG["bgBot"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "뉴스레터 포맷 4종 — 6개월 테스트 결과",
           font=font("pb", 40), fill=AG["white"])
    d.text((60, 104), "유료 전환은 주간 심층 1개에서만 발생 — 깊이가 ROI로 환산되기 때문",
           font=font("ps", 22), fill=AG["cyan"])

    items = [
        ("주간 심층 1개", "주 1회", "1,800~2,400자", "38%", "7.4%", AG["cyan"], True),
        ("주간 요약 5개", "주 1회", "600~900자",     "41%", "1.2%", AG["indigo"], False),
        ("격주 심층 1개", "격주",   "2,400~3,200자", "29%", "2.1%", AG["slate"], False),
        ("일간 토픽",     "일 1회", "300~500자",     "22%", "0.4%", AG["red"], False),
    ]
    cw, ch, y0 = 270, 380, 168
    gx = 20
    x0 = 60
    for i, (name, freq, length, open_rate, conv, col, winner) in enumerate(items):
        x = x0 + i * (cw + gx)
        outline_w = 4 if winner else 2
        rounded(d, (x, y0, x + cw, y0 + ch), 16, fill=AG["card"], outline=col, width=outline_w)
        if winner:
            d.rounded_rectangle((x, y0, x + cw, y0 + 50), radius=16, fill=col)
            d.text((x + cw//2, y0 + 12), "★ 유료 전환 정답", font=font("pb", 22),
                   fill=AG["bgTop"], anchor="ma")
            head_y = y0 + 68
        else:
            head_y = y0 + 26
        d.text((x + cw//2, head_y), name, font=font("pb", 24), fill=AG["white"], anchor="ma")
        rows = [("발행", freq), ("길이", length), ("오픈율", open_rate), ("유료 전환", conv)]
        ry = head_y + 56
        for j, (lbl, val) in enumerate(rows):
            yy = ry + j * 56
            d.text((x + 22, yy), lbl, font=font("pr", 18), fill=AG["slate"])
            d.text((x + cw - 22, yy - 2), val, font=font("pb", 22),
                   fill=col if j == 3 else AG["white"], anchor="ra")
            d.line([(x + 22, yy + 36), (x + cw - 22, yy + 36)], fill=AG["cardLine"], width=1)
    out = AG_DIR / "01-formats.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


# ---------------------------------------------------------------- AIGrit 02
def channel_funnel():
    W, H = 1200, 620
    img = gradient(W, H, AG["bgTop"], AG["bgBot"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "첫 100명 모은 채널 — 누적 1,020명까지 기여도",
           font=font("pb", 38), fill=AG["white"])
    d.text((60, 104), "블로그 본문 CTA가 41% — 검색 유입자의 전환율이 SNS보다 2~3배",
           font=font("ps", 22), fill=AG["cyan"])

    channels = [
        ("블로그 본문 CTA (AIGrit)",  41, "3.8%", AG["cyan"]),
        ("X(트위터) 글 인용",           27, "1.9%", AG["indigo"]),
        ("링크드인 게시물",             18, "2.1%", AG["green"]),
        ("직접 추천·DM",                11, "—",    AG["amber"]),
        ("Substack Recommendations",   3,  "—",    AG["slateDim"]),
    ]
    # horizontal bar chart
    y0 = 180
    bar_x0 = 360
    bar_w_max = 720
    row_h = 70
    for i, (name, pct, conv, col) in enumerate(channels):
        y = y0 + i * row_h
        d.text((40, y + 8), name, font=font("ps", 20), fill=AG["white"])
        bw = int(pct / 41 * bar_w_max)
        rounded(d, (bar_x0, y, bar_x0 + bw, y + 40), 10, fill=col)
        d.text((bar_x0 + bw + 12, y + 8), f"{pct}%", font=font("pb", 24), fill=AG["white"])
        d.text((bar_x0 + bw + 90, y + 12), f"전환 {conv}", font=font("pr", 18), fill=AG["slate"])
    # bottom summary
    d.rounded_rectangle((60, 540, 1140, 596), radius=14, fill=AG["card"])
    d.text((600, 552), "누적 구독자 1,020명 · 채널 다각화로 알고리즘 변동 헤지",
           font=font("ps", 22), fill=AG["white"], anchor="ma")
    out = AG_DIR / "02-channel-funnel.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


# ---------------------------------------------------------------- AIGrit 03
def six_month_revenue():
    W, H = 1200, 640
    img = gradient(W, H, AG["bgTop"], AG["bgBot"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "6개월 누적 매출 곡선", font=font("pb", 42), fill=AG["white"])
    d.text((60, 104), "M3 이후 작업 시간 -42% 감소 — 누적 매출 $975 (실수령 $778)",
           font=font("ps", 22), fill=AG["cyan"])

    months = [("M1", 0), ("M2", 35), ("M3", 95), ("M4", 185), ("M5", 280), ("M6", 380)]
    base_y, top_y = 540, 220
    maxv = 380
    n = len(months)
    x_left, x_right = 130, 1100
    step = (x_right - x_left) // (n - 1)
    points = []
    for i, (label, val) in enumerate(months):
        cx = x_left + i * step
        h = int(val / maxv * (base_y - top_y))
        y = base_y - h
        points.append((cx, y, val, label))
    d.line([(60, base_y), (1140, base_y)], fill=AG["cardLine"], width=2)
    # connector line
    for i in range(n - 1):
        d.line([points[i][:2], points[i+1][:2]], fill=AG["cyan"], width=4)
    # dots and labels
    for cx, y, val, label in points:
        d.ellipse((cx - 10, y - 10, cx + 10, y + 10), fill=AG["cyan"], outline=AG["white"], width=2)
        d.text((cx, y - 38), f"${val}", font=font("pb", 22), fill=AG["white"], anchor="ma")
        d.text((cx, base_y + 14), label, font=font("ps", 22), fill=AG["white"], anchor="ma")
    # summary right
    rounded(d, (940, 220, 1130, 380), 14, fill=AG["card"], outline=AG["amber"], width=2)
    d.text((1035, 234), "6개월 누적", font=font("ps", 20), fill=AG["amber"], anchor="ma")
    d.text((1035, 270), "$975", font=font("pb", 36), fill=AG["white"], anchor="ma")
    d.text((1035, 324), "실수령", font=font("pr", 18), fill=AG["slate"], anchor="ma")
    d.text((1035, 348), "$778", font=font("pb", 24), fill=AG["green"], anchor="ma")
    out = AG_DIR / "03-6month-revenue.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


# ---------------------------------------------------------------- babipanote 01
def v1_flat():
    W, H = 1200, 620
    img = gradient(W, H, BB["paperLight"], BB["paperDeep"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "v1 (2022) — 모든 노트를 한 폴더에", font=font("gb", 42), fill=BB["ink"])
    d.text((60, 116), "노트 1,800개 + 태그 47개 → 6개월 만에 폐기",
           font=font("pr", 22), fill=BB["muted"])

    # central single folder
    rounded(d, (440, 192, 760, 320), 16, fill=BB["white"], outline=BB["redEarth"], width=3)
    d.text((600, 220), "Notes/", font=font("gb", 36), fill=BB["ink"], anchor="ma")
    d.text((600, 268), "1,800 노트", font=font("ps", 22), fill=BB["redEarth"], anchor="ma")

    # tags scattered
    tags = ["#productivity", "#생산성", "#효율", "#보고서", "#meeting", "#회의록",
            "#book", "#책", "#review", "#리뷰", "#daily", "#일기", "#idea",
            "#project", "#archive", "#tool"]
    positions = [
        (100, 200), (250, 240), (820, 200), (1000, 220),
        (140, 360), (300, 380), (820, 360), (1020, 360),
        (180, 440), (340, 460), (780, 440), (980, 440),
        (60, 510), (220, 530), (860, 510), (1040, 530),
    ]
    for tag, (x, y) in zip(tags, positions):
        w = d.textlength(tag, font=font("pr", 18)) + 20
        rounded(d, (x, y, x + w, y + 32), 16, fill=BB["paperDeep"], outline=BB["muted"], width=1)
        d.text((x + w//2, y + 5), tag, font=font("pr", 18), fill=BB["muted"], anchor="ma")

    # bottom warning strip
    d.rounded_rectangle((300, 560, 900, 600), radius=14, fill=BB["redEarth"])
    d.text((600, 569), "재방문 0회 노트 60%+ → 못 찾는 상태로 폐기",
           font=font("gb", 20), fill=BB["paperLight"], anchor="ma")
    out = BB_DIR / "01-v1-flat.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


# ---------------------------------------------------------------- babipanote 02
def v3_tree():
    W, H = 1200, 720
    img = gradient(W, H, BB["paperLight"], BB["paperDeep"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "v3 (2026) — PARA 변형 + Inbox + Daily 분리",
           font=font("gb", 40), fill=BB["ink"])
    d.text((60, 116), "14개월째 안정 · 노트 3,200개 · Archive 비대 해소(90%→24%)",
           font=font("pr", 22), fill=BB["muted"])

    folders = [
        ("00-Inbox",      "내가 1주 안에 분류할 노트",       5,  BB["redEarth"]),
        ("10-Projects",   "마감일이 있는 작업",              8,  BB["plum"]),
        ("20-Areas",      "마감 없이 계속 책임지는 영역",     22, BB["plum"]),
        ("30-Resources",  "1년 안에 다시 꺼낼 자료",          36, BB["plum"]),
        ("40-Archive",    "1년 이상 안 본 모든 것",          24, BB["muted"]),
        ("99-Daily",      "자동 생성, 분류 안 함",            10, BB["greenEarth"]),
    ]
    row_h = 70
    y0 = 196
    bar_x0 = 700
    bar_w_max = 380
    for i, (name, rule, pct, col) in enumerate(folders):
        y = y0 + i * row_h
        rounded(d, (60, y, 1140, y + 56), 14, fill=BB["white"], outline=col, width=2)
        d.rounded_rectangle((60, y, 70, y + 56), radius=0, fill=col)
        d.text((90, y + 8), name, font=font("gb", 24), fill=BB["ink"])
        d.text((90, y + 36), rule, font=font("pr", 16), fill=BB["muted"])
        bw = int(pct / 36 * bar_w_max)
        rounded(d, (bar_x0, y + 14, bar_x0 + bw, y + 42), 8, fill=col)
        d.text((bar_x0 + bw + 12, y + 14), f"{pct}%", font=font("pb", 22), fill=BB["ink"])

    # bottom takeaway strip
    d.rounded_rectangle((300, 644, 900, 696), radius=14, fill=BB["plum"])
    d.text((600, 655), "Inbox 도입으로 분류 마찰 -73% (14개월 데이터)",
           font=font("gb", 20), fill=BB["paperLight"], anchor="ma")
    out = BB_DIR / "02-v3-tree.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


if __name__ == "__main__":
    newsletter_formats()
    channel_funnel()
    six_month_revenue()
    v1_flat()
    v3_tree()
    print("\n✅ inline infographics done.")
