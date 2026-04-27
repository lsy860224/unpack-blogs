"""네이버 #4 — 노션 vs 크래프트 1년 갈아탄 솔직 후기.

이미지 9장 + 정사각 썸네일 1장 (00-thumb-square.png).
AIGrit 다크 톤 (Indigo+Cyan).
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W, H = 1500, 845

BG = (15, 23, 42)
CARD_BG = (30, 41, 59)
CARD_BORDER = (51, 65, 85, 200)
ACCENT = (34, 211, 238)
INDIGO = (99, 102, 241)
SUCCESS = (34, 197, 94)
WARN = (251, 191, 36)
DANGER = (239, 68, 68)
TEXT_WHITE = (248, 250, 252)
TEXT_SLATE = (203, 213, 225)
TEXT_DIM = (148, 163, 184)
FOOTER_DIM = (100, 116, 139)

CRAFT_COLOR = (96, 165, 250)
NOTION_COLOR = (231, 229, 228)

FB = "/private/tmp/og-fonts/Pretendard-Bold.otf"
FS = "/private/tmp/og-fonts/Pretendard-SemiBold.otf"
FR = "/private/tmp/og-fonts/Pretendard-Regular.otf"

OUT = Path("/Users/seung-yeoblee/dev/unpack-blogs/docs/naver-setup/editions/images/04-craft-vs-notion")
OUT.mkdir(parents=True, exist_ok=True)


def font(p, s):
    return ImageFont.truetype(p, s)


def wrap(text, f, max_w):
    lines, cur = [], ""
    for w in text.split(" "):
        trial = (cur + " " + w).strip()
        if f.getbbox(trial)[2] <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def hero_header(d, title, subtitle):
    tf = font(FB, 56)
    tw = tf.getbbox(title)[2]
    d.text(((W - tw) // 2, 60), title, font=tf, fill=TEXT_WHITE)
    sf = font(FS, 22)
    sw = sf.getbbox(subtitle)[2]
    d.text(((W - sw) // 2, 130), subtitle, font=sf, fill=TEXT_DIM)
    d.rectangle(((W // 2 - 60), 180, (W // 2 + 60), 184), fill=ACCENT)


def footer(d, conclusion):
    cf = font(FB, 26)
    cw = cf.getbbox(conclusion)[2]
    d.text(((W - cw) // 2, H - 110), conclusion, font=cf, fill=ACCENT)
    bf = font(FR, 18)
    brand = "babipa의 AIGrit · 네이버 블로그"
    bw = bf.getbbox(brand)[2]
    d.text((W - bw - 40, H - 38), brand, font=bf, fill=FOOTER_DIM)


def background_lines(d):
    for y in range(0, H, 80):
        d.line([(0, y), (W, y)], fill=(20, 30, 50), width=1)


def render_cover():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img, "RGBA")
    background_lines(d)

    # Big two-column visual: Craft vs Notion
    badge_f = font(FS, 18)
    badge_text = "AI 도구 리뷰 · 1년 사용 비교"
    bw = badge_f.getbbox(badge_text)[2] + 36
    bx, by = (W - bw) // 2, 70
    d.rounded_rectangle((bx, by, bx + bw, by + 36), radius=18, fill=ACCENT)
    bw_t = badge_f.getbbox(badge_text)[2]
    d.text((bx + (bw - bw_t) // 2, by + 8), badge_text, font=badge_f, fill=BG)

    title_f = font(FB, 76)
    line1 = "노션 vs 크래프트"
    line2 = "1년 갈아탄 솔직 후기"
    l1w = title_f.getbbox(line1)[2]
    l2w = title_f.getbbox(line2)[2]
    d.text(((W - l1w) // 2, 160), line1, font=title_f, fill=TEXT_WHITE)
    d.text(((W - l2w) // 2, 250), line2, font=title_f, fill=ACCENT)

    # Two big cards: Craft / Notion
    card_w = 540
    card_h = 280
    gap = 48
    total = card_w * 2 + gap
    sx = (W - total) // 2
    cy = 400

    # Craft card
    d.rounded_rectangle((sx, cy, sx + card_w, cy + card_h), radius=22, fill=CARD_BG, outline=ACCENT, width=2)
    cf_t = font(FB, 50)
    d.text((sx + 36, cy + 28), "Craft", font=cf_t, fill=CRAFT_COLOR)
    cf_s = font(FS, 22)
    d.text((sx + 36, cy + 90), "글쓰기·속도·디자인", font=cf_s, fill=TEXT_WHITE)
    pf = font(FR, 18)
    bullets_c = [
        "✓ Apple 네이티브 (즉시 반응)",
        "✓ 복붙 품질 압도적",
        "✓ 오프라인 완벽",
        "× DB·협업·Android 약함",
    ]
    for i, b in enumerate(bullets_c):
        d.text((sx + 36, cy + 132 + i * 30), b, font=pf, fill=TEXT_SLATE)

    # Notion card
    nx = sx + card_w + gap
    d.rounded_rectangle((nx, cy, nx + card_w, cy + card_h), radius=22, fill=CARD_BG, outline=NOTION_COLOR, width=2)
    d.text((nx + 36, cy + 28), "Notion", font=cf_t, fill=NOTION_COLOR)
    d.text((nx + 36, cy + 90), "DB·협업·플랫폼", font=cf_s, fill=TEXT_WHITE)
    bullets_n = [
        "✓ 관계형 DB 표준",
        "✓ 팀 협업 무제한",
        "✓ Android·Windows 지원",
        "× 글쓰기 속도 떨어짐",
    ]
    for i, b in enumerate(bullets_n):
        d.text((nx + 36, cy + 132 + i * 30), b, font=pf, fill=TEXT_SLATE)

    footer(d, "글쓰기는 Craft, DB·협업은 Notion — 역할 분리가 정답")
    out = OUT / "01-cover.png"
    img.save(out, "PNG", optimize=True)
    print(f"✓ {out.name}")


def render_vs_table():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img, "RGBA")
    background_lines(d)
    hero_header(d, "한눈에 보는 핵심 비교", "Craft vs Notion · 1년 실사용 기준")

    rows = [
        ("핵심 강점", "글쓰기·디자인·속도", "DB·관계형·협업"),
        ("속도", "즉시 반응 (네이티브)", "로딩 1~2초 (웹)"),
        ("오프라인", "완벽", "제한적"),
        ("DB 기능", "없음", "강력한 관계형 DB"),
        ("협업", "5인 이하 소규모", "무제한 (팀 위키)"),
        ("가격", "무료~$5/월", "무료~$10/월"),
        ("플랫폼", "Apple 전용", "iOS·Android·Web·Win"),
    ]

    table_x = 100
    table_y = 230
    col_widths = [200, 540, 540]
    row_h = 64
    table_w = sum(col_widths)

    # Header row
    d.rounded_rectangle((table_x, table_y, table_x + table_w, table_y + row_h), radius=10, fill=CARD_BG, outline=ACCENT, width=2)
    hf = font(FB, 24)
    headers = ["항목", "Craft", "Notion"]
    colors = [TEXT_WHITE, CRAFT_COLOR, NOTION_COLOR]
    cx = table_x
    for i, h in enumerate(headers):
        hw = hf.getbbox(h)[2]
        d.text((cx + (col_widths[i] - hw) // 2, table_y + 18), h, font=hf, fill=colors[i])
        cx += col_widths[i]

    # Data rows
    rf = font(FS, 19)
    for i, (label, c, n) in enumerate(rows):
        ry = table_y + (i + 1) * row_h
        if i % 2 == 0:
            d.rectangle((table_x, ry, table_x + table_w, ry + row_h), fill=(22, 32, 50))
        cx = table_x
        items = [label, c, n]
        item_colors = [TEXT_DIM, CRAFT_COLOR, NOTION_COLOR]
        for j, item in enumerate(items):
            iw = rf.getbbox(item)[2]
            d.text((cx + (col_widths[j] - iw) // 2, ry + 20), item, font=rf, fill=item_colors[j])
            cx += col_widths[j]

    footer(d, "철학이 다르다 — \"좋은 문단\" vs \"좋은 구조\"")
    out = OUT / "02-vs-table.png"
    img.save(out, "PNG", optimize=True)
    print(f"✓ {out.name}")


def render_strengths_cards(slug, title, sub, cards, color, accent_text):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img, "RGBA")
    background_lines(d)
    hero_header(d, title, sub)

    card_w = 320
    card_h = 380
    gap = 28
    total = card_w * 4 + gap * 3
    sx = (W - total) // 2
    cy = 230

    for i, (n, head, body) in enumerate(cards):
        x = sx + i * (card_w + gap)
        d.rounded_rectangle((x, cy, x + card_w, cy + card_h), radius=18, fill=CARD_BG, outline=CARD_BORDER, width=1)
        # badge
        bz = 50
        bx, by = x + 28, cy + 28
        d.ellipse((bx, by, bx + bz, by + bz), fill=color)
        nf = font(FB, 26)
        nw = nf.getbbox(str(n))[2]
        d.text((bx + (bz - nw) // 2, by + 9), str(n), font=nf, fill=BG)
        # title
        hf = font(FB, 24)
        head_lines = wrap(head, hf, card_w - 56)
        hy = cy + 100
        for ln in head_lines[:2]:
            d.text((x + 28, hy), ln, font=hf, fill=TEXT_WHITE)
            hy += 32
        # body
        bf = font(FR, 18)
        body_lines = wrap(body, bf, card_w - 56)
        by_ = hy + 16
        for ln in body_lines[:8]:
            d.text((x + 28, by_), ln, font=bf, fill=TEXT_SLATE)
            by_ += 26

    footer(d, accent_text)
    out = OUT / f"{slug}.png"
    img.save(out, "PNG", optimize=True)
    print(f"✓ {out.name}")


def render_divider():
    img = Image.new("RGB", (W, 240), BG)
    d = ImageDraw.Draw(img, "RGBA")
    # Centered Cyan dot pattern
    cy_ = 120
    spacing = 36
    count = 13
    total_w = (count - 1) * spacing
    sx = (W - total_w) // 2
    for i in range(count):
        size = 8 if i == count // 2 else 6
        cx = sx + i * spacing
        col = ACCENT if abs(i - count // 2) < 2 else FOOTER_DIM
        d.ellipse((cx - size, cy_ - size, cx + size, cy_ + size), fill=col)
    f = font(FS, 18)
    label = "역할 분리가 정답"
    lw = f.getbbox(label)[2]
    d.text(((W - lw) // 2, cy_ + 24), label, font=f, fill=TEXT_DIM)
    out = OUT / "05-divider.png"
    img.save(out, "PNG", optimize=True)
    print(f"✓ {out.name}")


def render_role_separation():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img, "RGBA")
    background_lines(d)
    hero_header(d, "1인 부업러를 위한 역할 분리", "Craft·Obsidian·Notion 3열 구조 — 겹치는 기능 없음")

    cols = [
        ("Craft", "글쓰기·복붙 발행", CRAFT_COLOR, [
            "블로그 글 초안",
            "Craft → 네이버 복붙",
            "오프라인 글쓰기",
            "정적 문서·메모",
        ]),
        ("Obsidian", "기획·SEO 관제", INDIGO, [
            "키워드 분석",
            "Dataview 대시보드",
            "글 발행 추적",
            "지식관리 (제텔카스텐)",
        ]),
        ("Notion", "협업·관계형 DB", NOTION_COLOR, [
            "팀 위키",
            "부업 매출 DB",
            "고객 관리",
            "노션 AI 워크스페이스",
        ]),
    ]

    card_w = 420
    card_h = 470
    gap = 30
    total = card_w * 3 + gap * 2
    sx = (W - total) // 2
    cy = 240

    for i, (name, sub, color, items) in enumerate(cols):
        x = sx + i * (card_w + gap)
        d.rounded_rectangle((x, cy, x + card_w, cy + card_h), radius=18, fill=CARD_BG, outline=color, width=2)
        nf = font(FB, 38)
        d.text((x + 30, cy + 30), name, font=nf, fill=color)
        sf = font(FS, 18)
        d.text((x + 30, cy + 88), sub, font=sf, fill=TEXT_DIM)
        d.rectangle((x + 30, cy + 124, x + 70, cy + 127), fill=color)
        f = font(FR, 20)
        for j, it in enumerate(items):
            d.text((x + 30, cy + 155 + j * 44), f"• {it}", font=f, fill=TEXT_SLATE)
        # Cost
        cf = font(FB, 18)
        d.text((x + 30, cy + card_h - 50), "월 ₩0~6,500", font=cf, fill=color)

    footer(d, "월 0원 시작 가능 (Craft 무료 + Obsidian 무료)")
    out = OUT / "06-role-separation.png"
    img.save(out, "PNG", optimize=True)
    print(f"✓ {out.name}")


def render_pricing():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img, "RGBA")
    background_lines(d)
    hero_header(d, "1년 비용 정확히", "무료 시작 가능 · Craft 유료가 Notion 절반 가격")

    rows = [
        ("무료 한도", "1,000 블록", "무제한 페이지"),
        ("개인 유료", "$5/월 (₩6,500)", "$10/월 (₩13,000)"),
        ("팀", "$10/월/인", "$10/월/인"),
        ("학생 할인", "❌ 없음", "✅ 무료 업그레이드"),
        ("Android", "❌ 안 됨", "✅ 정식 지원"),
        ("Windows", "❌ 안 됨", "✅ 정식 지원"),
    ]

    table_x = 100
    table_y = 230
    col_widths = [280, 500, 500]
    row_h = 68
    table_w = sum(col_widths)

    d.rounded_rectangle((table_x, table_y, table_x + table_w, table_y + row_h), radius=10, fill=CARD_BG, outline=ACCENT, width=2)
    hf = font(FB, 24)
    headers = ["항목", "Craft", "Notion"]
    colors = [TEXT_WHITE, CRAFT_COLOR, NOTION_COLOR]
    cx = table_x
    for i, h in enumerate(headers):
        hw = hf.getbbox(h)[2]
        d.text((cx + (col_widths[i] - hw) // 2, table_y + 20), h, font=hf, fill=colors[i])
        cx += col_widths[i]

    rf = font(FS, 20)
    for i, (label, c, n) in enumerate(rows):
        ry = table_y + (i + 1) * row_h
        if i % 2 == 0:
            d.rectangle((table_x, ry, table_x + table_w, ry + row_h), fill=(22, 32, 50))
        cx = table_x
        items = [label, c, n]
        item_colors = [TEXT_DIM, CRAFT_COLOR, NOTION_COLOR]
        for j, item in enumerate(items):
            iw = rf.getbbox(item)[2]
            d.text((cx + (col_widths[j] - iw) // 2, ry + 22), item, font=rf, fill=item_colors[j])
            cx += col_widths[j]

    footer(d, "Craft = Notion 절반 가격 · 단점은 Apple 전용")
    out = OUT / "07-pricing.png"
    img.save(out, "PNG", optimize=True)
    print(f"✓ {out.name}")


def render_decision_tree():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img, "RGBA")
    background_lines(d)
    hero_header(d, "어떤 도구가 맞을까?", "5가지 질문으로 결정하는 노트앱 가이드")

    # Decision flow as a top-down tree
    cy = 220

    # Q1
    q1 = "주 기기가 Apple(맥·아이폰)인가?"
    qf = font(FB, 26)
    qw = qf.getbbox(q1)[2]
    qx = (W - qw - 60) // 2
    d.rounded_rectangle((qx, cy, qx + qw + 60, cy + 60), radius=14, fill=CARD_BG, outline=ACCENT, width=2)
    d.text((qx + 30, cy + 16), q1, font=qf, fill=TEXT_WHITE)

    # Branch
    by = cy + 90
    af = font(FS, 18)
    yes_x = W // 2 - 240
    no_x = W // 2 + 60
    d.line((W // 2, cy + 60, yes_x + 60, by), fill=ACCENT, width=2)
    d.line((W // 2, cy + 60, no_x + 60, by), fill=NOTION_COLOR, width=2)
    d.text((yes_x, by - 10), "예", font=af, fill=ACCENT)
    d.text((no_x, by - 10), "아니오", font=af, fill=NOTION_COLOR)

    # Q2 left + result right
    cy2 = by + 30
    q2 = "혼자 쓸 건가? (협업 X)"
    qw2 = qf.getbbox(q2)[2]
    q2x = yes_x - 50
    d.rounded_rectangle((q2x, cy2, q2x + qw2 + 60, cy2 + 60), radius=14, fill=CARD_BG, outline=CRAFT_COLOR, width=2)
    d.text((q2x + 30, cy2 + 16), q2, font=qf, fill=TEXT_WHITE)

    r1 = "→ Notion 결정"
    rw = qf.getbbox(r1)[2]
    rx = no_x - 30
    d.rounded_rectangle((rx, cy2, rx + rw + 60, cy2 + 60), radius=14, fill=NOTION_COLOR, outline=NOTION_COLOR, width=2)
    d.text((rx + 30, cy2 + 16), r1, font=qf, fill=BG)

    # Final results
    cy3 = cy2 + 110
    result_y = cy3
    d.line((q2x + (qw2 + 60) // 2, cy2 + 60, q2x - 80, result_y), fill=CRAFT_COLOR, width=2)
    d.line((q2x + (qw2 + 60) // 2, cy2 + 60, q2x + qw2 + 140, result_y), fill=NOTION_COLOR, width=2)

    final_l = "→ Craft (글쓰기 중심)"
    flw = qf.getbbox(final_l)[2]
    flx = q2x - 130 - flw // 2
    d.rounded_rectangle((flx, result_y, flx + flw + 60, result_y + 60), radius=14, fill=CRAFT_COLOR, outline=CRAFT_COLOR, width=2)
    d.text((flx + 30, result_y + 16), final_l, font=qf, fill=BG)

    final_r = "→ Notion (DB·협업)"
    frw = qf.getbbox(final_r)[2]
    frx = q2x + qw2 + 80
    d.rounded_rectangle((frx, result_y, frx + frw + 60, result_y + 60), radius=14, fill=NOTION_COLOR, outline=NOTION_COLOR, width=2)
    d.text((frx + 30, result_y + 16), final_r, font=qf, fill=BG)

    # Bottom note
    note = "여전히 고민? → 둘 다 쓰면서 역할 분리하세요. 월 ₩0부터 시작 가능."
    nf = font(FS, 22)
    nw = nf.getbbox(note)[2]
    d.text(((W - nw) // 2, H - 200), note, font=nf, fill=TEXT_DIM)

    footer(d, "정답은 \"하나 고르기\"가 아니라 \"역할 나누기\"")
    out = OUT / "08-decision-tree.png"
    img.save(out, "PNG", optimize=True)
    print(f"✓ {out.name}")


def render_closing():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img, "RGBA")
    background_lines(d)
    hero_header(d, "1년 결론 — 역할 분리가 정답", "Craft = 글쓰기 / Notion = DB·협업 / Obsidian = 기획")

    # Center summary
    cy = 250
    f1 = font(FB, 38)
    text1 = "둘은 경쟁자가 아니라 동료입니다."
    tw1 = f1.getbbox(text1)[2]
    d.text(((W - tw1) // 2, cy), text1, font=f1, fill=TEXT_WHITE)

    f2 = font(FB, 32)
    text2 = "글쓰기 속도가 일주일 만에 차이를 만든다."
    tw2 = f2.getbbox(text2)[2]
    d.text(((W - tw2) // 2, cy + 70), text2, font=f2, fill=ACCENT)

    # CTA bullets
    cta = [
        "✓ 부업 글쓰기 — Craft (월 ₩0~6,500)",
        "✓ 부업 매출·고객 DB — Notion (무료부터)",
        "✓ Android·Windows 환경 — Notion (Craft는 Apple 전용)",
        "✓ 학생 — Notion 무료 업그레이드",
        "✓ 팀 협업 5인+ — Notion 외 대안 거의 없음",
    ]
    cf = font(FS, 22)
    cy2 = cy + 160
    for i, c in enumerate(cta):
        cw = cf.getbbox(c)[2]
        d.text(((W - cw) // 2, cy2 + i * 36), c, font=cf, fill=TEXT_SLATE)

    footer(d, "다음 편 — Claude Code로 비개발자가 앱 만든 후기")
    out = OUT / "09-closing.png"
    img.save(out, "PNG", optimize=True)
    print(f"✓ {out.name}")


def render_thumb_square():
    """1080×1080 정사각형 — 네이버 프롤로그 대표 이미지용."""
    SZ = 1080
    img = Image.new("RGB", (SZ, SZ), BG)
    d = ImageDraw.Draw(img, "RGBA")
    for y in range(0, SZ, 60):
        d.line([(0, y), (SZ, y)], fill=(20, 30, 50), width=1)

    # Category badge
    badge_f = font(FS, 22)
    badge = "AI 도구 리뷰"
    bw = badge_f.getbbox(badge)[2] + 36
    bx, by = (SZ - bw) // 2, 80
    d.rounded_rectangle((bx, by, bx + bw, by + 44), radius=22, fill=ACCENT)
    bw_t = badge_f.getbbox(badge)[2]
    d.text((bx + (bw - bw_t) // 2, by + 10), badge, font=badge_f, fill=BG)

    # Title — 3 lines
    tf = font(FB, 80)
    lines = ["노션 vs 크래프트", "1년 갈아탄", "솔직 후기"]
    ly = 200
    for ln in lines:
        lw = tf.getbbox(ln)[2]
        col = ACCENT if ln == "1년 갈아탄" else TEXT_WHITE
        d.text(((SZ - lw) // 2, ly), ln, font=tf, fill=col)
        ly += 100

    # Divider
    d.rectangle(((SZ // 2 - 60), 530, (SZ // 2 + 60), 536), fill=ACCENT)

    # 2-column comparison summary
    sub_f = font(FB, 36)
    cy = 580
    # Craft side
    d.text((150, cy), "Craft", font=sub_f, fill=CRAFT_COLOR)
    d.text((150, cy + 56), "글쓰기·속도", font=font(FS, 26), fill=TEXT_DIM)
    # Notion side
    notion_t = "Notion"
    nx = SZ - 150 - sub_f.getbbox(notion_t)[2]
    d.text((nx, cy), notion_t, font=sub_f, fill=NOTION_COLOR)
    notion_s = "DB·협업"
    nxs = SZ - 150 - font(FS, 26).getbbox(notion_s)[2]
    d.text((nxs, cy + 56), notion_s, font=font(FS, 26), fill=TEXT_DIM)
    # vs in middle
    vs_f = font(FB, 60)
    vs = "vs"
    vw = vs_f.getbbox(vs)[2]
    d.text(((SZ - vw) // 2, cy + 6), vs, font=vs_f, fill=TEXT_WHITE)

    # Wordmark
    wm_f = font(FB, 32)
    wm = "[AI]Grit"
    wmw = wm_f.getbbox(wm)[2]
    d.text(((SZ - wmw) // 2, SZ - 130), wm, font=wm_f, fill=ACCENT)
    bf = font(FR, 20)
    brand = "babipa의 AIGrit · 네이버 블로그"
    bw_b = bf.getbbox(brand)[2]
    d.text(((SZ - bw_b) // 2, SZ - 80), brand, font=bf, fill=FOOTER_DIM)

    out = OUT / "00-thumb-square.png"
    img.save(out, "PNG", optimize=True)
    print(f"✓ {out.name}")


if __name__ == "__main__":
    render_thumb_square()
    render_cover()
    render_vs_table()
    render_strengths_cards(
        "03-craft-strengths",
        "Craft가 Notion보다 나은 점",
        "1년 실사용으로 체감한 4가지 차이",
        [
            (1, "글쓰기 속도", "Apple 네이티브. 키 입력 즉시 반영. 3,000자 넘어도 끊김 없음."),
            (2, "복붙 품질", "테이블·이미지·포맷 그대로. 네이버 스마트에디터 호환 우수."),
            (3, "오프라인 완벽", "비행기·지하철 즉시 열림. 동기화 충돌 없음."),
            (4, "디자인 기본값", "처음부터 \"읽기 좋은 글\". 커스텀 작업 불필요."),
        ],
        CRAFT_COLOR,
        "글쓰기 일주일이면 차이 체감 — Apple 사용자 강추",
    )
    render_strengths_cards(
        "04-notion-strengths",
        "Notion이 Craft보다 나은 점",
        "Craft가 절대 못 따라가는 4가지 영역",
        [
            (1, "관계형 DB", "부업 매출·고객 관리 표준. SQL 몰라도 사용 가능."),
            (2, "팀 협업", "5인+ 표준. 권한 관리·코멘트 완비. 위키 표준."),
            (3, "전 플랫폼", "Android·Windows 정식 지원. 학생 무료 업그레이드."),
            (4, "Notion AI", "워크스페이스 데이터 직접 읽음. 회의록 자동 요약."),
        ],
        NOTION_COLOR,
        "협업·DB·Android 환경이면 Notion 외 대안 없음",
    )
    render_divider()
    render_role_separation()
    render_pricing()
    render_decision_tree()
    render_closing()
    print("\n완료 — 9장 본문 + 1장 정사각 썸네일 (AIGrit 다크 톤)")
