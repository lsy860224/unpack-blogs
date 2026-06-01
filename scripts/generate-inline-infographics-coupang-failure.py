#!/usr/bin/env python3
"""
Inline infographics for:
  - AIGrit  #20  chatgpt-coupang-partners-automation (4 charts, Indigo/Cyan dark)
  - babipanote #16  side-hustle-failure-lessons      (1 timeline, Paper/Plum)

Visual style mirrors scripts/og/generate-og-all.py + previous inline scripts.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE = Path("/Users/seung-yeoblee/dev/unpack-blogs/apps")
AG_DIR = BASE / "aigrit" / "public" / "images" / "chatgpt-coupang-partners-automation"
BB_DIR = BASE / "babipanote" / "public" / "images" / "side-hustle-failure-lessons"
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
def pipeline_4steps():
    W, H = 1200, 460
    img = gradient(W, H, AG["bgTop"], AG["bgBot"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "쿠팡파트너스 자동화 4단계", font=font("pb", 42), fill=AG["white"])
    d.text((60, 104), "ChatGPT가 줄여주는 건 초안 1구간 — 통과·전환의 12분은 사람",
           font=font("ps", 22), fill=AG["cyan"])

    nodes = [
        ("상품 리서치", "5분", AG["indigo"]),
        ("ChatGPT 초안", "4분", AG["cyan"]),
        ("사람 보정+이미지", "12분", AG["amber"]),
        ("발행·인덱싱", "4분", AG["green"]),
    ]
    nw, nh, cy = 230, 112, 240
    centers = [180 + i * 280 for i in range(4)]
    for i, ((t1, t2, col), cx) in enumerate(zip(nodes, centers)):
        x1, x2 = cx - nw//2, cx + nw//2
        rounded(d, (x1, cy - nh//2, x2, cy + nh//2), 16, fill=AG["card"], outline=col, width=3)
        d.text((cx, cy - 24), t1, font=font("pb", 24), fill=AG["white"], anchor="ma")
        d.text((cx, cy + 14), t2, font=font("ps", 22), fill=col, anchor="ma")
        if i < 3:
            ax = x2 + 10; axe = centers[i+1] - nw//2 - 10
            d.line([(ax, cy), (axe, cy)], fill=AG["slateDim"], width=3)
            d.polygon([(axe, cy-7), (axe, cy+7), (axe+10, cy)], fill=AG["slateDim"])
    # total badge
    rounded(d, (430, 360, 770, 412), 26, fill=AG["cyan"])
    d.text((600, 372), "글당 합계 25분", font=font("pb", 26), fill=AG["bgTop"], anchor="ma")
    out = AG_DIR / "01-pipeline.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


# ---------------------------------------------------------------- AIGrit 02
def prompt_structure():
    W, H = 1200, 660
    img = gradient(W, H, AG["bgTop"], AG["bgBot"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "ChatGPT 프롬프트 3-블록 구조", font=font("pb", 40), fill=AG["white"])
    d.text((60, 100), "AI 블록 3개 + 사람 보정 4요소 = 저품질 회피 84%",
           font=font("ps", 22), fill=AG["cyan"])

    # Top: 3 blocks A, B, C
    blocks = [
        ("A", "제품 사양 정리", "공식 페이지 스펙·가격·구성품"),
        ("B", "카테고리 3개 비교 표", "경쟁 상품 가격·기능·평점"),
        ("C", "사용 시나리오 3개", "출근·운동·캠핑 등 구체 상황"),
    ]
    bw, bh, y = 350, 180, 168
    gx = 30
    x0 = 60
    for i, (n, t, sub) in enumerate(blocks):
        x = x0 + i * (bw + gx)
        rounded(d, (x, y, x + bw, y + bh), 16, fill=AG["card"], outline=AG["cyan"], width=3)
        d.ellipse((x + 24, y + 24, x + 24 + 50, y + 24 + 50), fill=AG["cyan"])
        d.text((x + 24 + 25, y + 24 + 25), n, font=font("pb", 30), fill=AG["bgTop"], anchor="mm")
        d.text((x + 100, y + 30), t, font=font("pb", 26), fill=AG["white"])
        d.text((x + 24, y + 100), sub, font=font("pr", 20), fill=AG["slate"])
        d.text((x + 24, y + 132), "(ChatGPT 자동 생성)", font=font("pr", 18), fill=AG["slateDim"])

    # Arrow down
    d.line([(600, 374), (600, 422)], fill=AG["amber"], width=4)
    d.polygon([(590, 418), (610, 418), (600, 438)], fill=AG["amber"])

    # Bottom: 사람 4요소 box
    rounded(d, (60, 460, 1140, 600), 18, fill=AG["card"], outline=AG["amber"], width=3)
    d.text((90, 478), "사람 보정 4요소", font=font("pb", 26), fill=AG["amber"])
    items = [
        ("• 본인 사용 경험 1문단", "2~3주 실사용 · 구체 수치"),
        ("• 자체 촬영 이미지 3장+", "박스·세팅·1주 사용 후"),
        ("• 단점 2개 이상", "과장 회피 신호"),
        ("• 자연스러운 CTA 1줄", "본인 사용 패턴에 맞으면 추천"),
    ]
    for i, (head, sub) in enumerate(items):
        col = i % 2; row = i // 2
        x = 90 + col * 530; yy = 524 + row * 36
        d.text((x, yy), head, font=font("ps", 20), fill=AG["white"])
        d.text((x + 240, yy + 2), sub, font=font("pr", 18), fill=AG["slate"])
    out = AG_DIR / "02-prompt-structure.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


# ---------------------------------------------------------------- AIGrit 03
def platform_comparison():
    W, H = 1200, 620
    img = gradient(W, H, AG["bgTop"], AG["bgBot"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "발행처 비교 — 30글 ×3개월", font=font("pb", 40), fill=AG["white"])
    d.text((60, 100), "네이버 빠른 노출·짧은 잔존 / 티스토리 중간 / 워드프레스 긴 잔존",
           font=font("ps", 22), fill=AG["cyan"])

    platforms = [
        ("네이버 블로그", "48h~",    "30~45일", 42, AG["green"]),
        ("티스토리",     "7~14일",   "60~90일", 31, AG["cyan"]),
        ("워드프레스",   "30~60일",  "180일+",  27, AG["indigo"]),
    ]
    cw, ch, y0 = 350, 380, 168
    gx = 30
    x0 = 60
    for i, (name, fast, persist, share, col) in enumerate(platforms):
        x = x0 + i * (cw + gx)
        rounded(d, (x, y0, x + cw, y0 + ch), 18, fill=AG["card"], outline=col, width=3)
        # header bar
        d.rounded_rectangle((x, y0, x + cw, y0 + 64), radius=18, fill=col)
        d.text((x + cw//2, y0 + 18), name, font=font("pb", 26), fill=AG["bgTop"], anchor="ma")
        # stats
        rows = [("초기 노출", fast), ("90일 잔존", persist), ("매출 비중", f"{share}%")]
        for j, (lbl, val) in enumerate(rows):
            yy = y0 + 96 + j * 70
            d.text((x + 26, yy), lbl, font=font("pr", 20), fill=AG["slate"])
            d.text((x + cw - 26, yy - 2), val, font=font("pb", 26), fill=AG["white"], anchor="ra")
            d.line([(x + 26, yy + 38), (x + cw - 26, yy + 38)], fill=AG["cardLine"], width=1)
    out = AG_DIR / "03-platform-comparison.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


# ---------------------------------------------------------------- AIGrit 04
def revenue_curve_coupang():
    W, H = 1200, 660
    img = gradient(W, H, AG["bgTop"], AG["bgBot"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "3개월 30글 누적 매출", font=font("pb", 42), fill=AG["white"])
    d.text((60, 104), "M3 = M1 대비 5.6배 — 누적 25글 이후 잔존 매출 본격화",
           font=font("ps", 22), fill=AG["cyan"])

    months = [("M1", "누적 10글", 8400), ("M2", "누적 20글", 21000), ("M3", "누적 30글", 47000)]
    maxv = 47000
    base_y, top_y = 580, 230
    centers = [310, 600, 890]
    bw = 180
    d.line([(60, base_y), (1140, base_y)], fill=AG["cardLine"], width=2)
    for (label, sub, val), cx in zip(months, centers):
        h = int(val / maxv * (base_y - top_y))
        rounded(d, (cx - bw//2, base_y - h, cx + bw//2, base_y), 10, fill=AG["cyan"])
        d.text((cx, base_y - h - 38), f"₩{val:,}", font=font("pb", 30),
               fill=AG["white"], anchor="ma")
        d.text((cx, base_y + 14), label, font=font("ps", 26), fill=AG["white"], anchor="ma")
        d.text((cx, base_y + 50), sub, font=font("pr", 20), fill=AG["slate"], anchor="ma")
    # callout transition point
    d.text((centers[1], 210), "전환점 = 누적 25글", font=font("ps", 20),
           fill=AG["amber"], anchor="ma")
    d.polygon([(centers[1]-12, 226), (centers[1]+12, 226), (centers[1], 246)], fill=AG["amber"])
    out = AG_DIR / "04-3month-revenue.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


# ---------------------------------------------------------------- babipanote 01
def failure_timeline():
    W, H = 1200, 680
    img = gradient(W, H, BB["paperLight"], BB["paperDeep"]); d = ImageDraw.Draw(img)
    d.text((60, 48), "6개 시체 — 14개월의 정산", font=font("gb", 44), fill=BB["ink"])
    d.text((60, 118), "투입 620시간 · 지출 ₩220k · 매출 ₩14k (시급 ₩22)",
           font=font("pr", 22), fill=BB["muted"])

    cards = [
        ("1", "TaskFlow",      "SaaS 할일관리",    "240h · ₩88k", "가입 13 · 유료 0"),
        ("2", "ReadStock",     "영문책 뉴스레터",  "90h · ₩0",    "구독 47 · 매출 0"),
        ("3", "PromptShop",    "프롬프트 묶음",    "60h · ₩22k",  "판매 2 · ₩14k"),
        ("4", "DevWeekly KR",  "개발자 뉴스레터",  "70h · ₩0",    "구독 88 · 광고 0"),
        ("5", "MoodLog",       "감정일기 iOS",     "110h · ₩110k","다운 142 · 구독 1"),
        ("6", "InboxZero AI",  "Gmail 확장",       "50h · ₩0",    "설치 12 · 유료 0"),
    ]
    cw, ch, gx, gy = 360, 184, 20, 22
    x0, y0 = 60, 196
    for i, (n, name, kind, time_cost, result) in enumerate(cards):
        cx = x0 + (i % 3) * (cw + gx)
        cy = y0 + (i // 3) * (ch + gy)
        rounded(d, (cx, cy, cx + cw, cy + ch), 16, fill=BB["white"], outline=BB["terracotta"], width=2)
        # left index strip
        d.rounded_rectangle((cx, cy, cx + 10, cy + ch), radius=0, fill=BB["redEarth"])
        d.ellipse((cx + 22, cy + 22, cx + 22 + 44, cy + 22 + 44), fill=BB["redEarth"])
        d.text((cx + 22 + 22, cy + 22 + 22), n, font=font("gb", 24), fill=BB["paperLight"], anchor="mm")
        d.text((cx + 82, cy + 24), name, font=font("gb", 26), fill=BB["ink"])
        d.text((cx + 82, cy + 60), kind, font=font("pr", 18), fill=BB["muted"])
        # divider
        d.line([(cx + 22, cy + 96), (cx + cw - 22, cy + 96)], fill=BB["paperDeep"], width=2)
        d.text((cx + 22, cy + 108), "투입", font=font("pr", 16), fill=BB["muted"])
        d.text((cx + cw - 22, cy + 108), time_cost, font=font("ps", 18), fill=BB["ink"], anchor="ra")
        d.text((cx + 22, cy + 138), "결과", font=font("pr", 16), fill=BB["muted"])
        d.text((cx + cw - 22, cy + 138), result, font=font("ps", 18), fill=BB["redEarth"], anchor="ra")
    out = BB_DIR / "01-failure-timeline.png"; img.save(out, "PNG", optimize=True)
    print("✓", out.name)


if __name__ == "__main__":
    pipeline_4steps()
    prompt_structure()
    platform_comparison()
    revenue_curve_coupang()
    failure_timeline()
    print("\n✅ inline infographics done.")
