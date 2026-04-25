"""
Perplexity 에디션 07-weaknesses.png · 08-use-cases.png를 AIGrit 다크 톤으로 재생성.
기존 babipanote 종이 톤 → AIGrit Indigo+Cyan 다크 톤으로 통일.

기준: 04-usage-chart.png (이미 AIGrit 톤)와 시각 일관성.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# ---------- 디자인 토큰 (AIGrit Dark) ----------
W, H = 1500, 845  # 16:9 기준 비율 유지

BG = (15, 23, 42)              # #0F172A
CARD_BG = (30, 41, 59)         # #1E293B (surface dark)
CARD_BORDER = (51, 65, 85, 200)  # slate-700
ACCENT_CYAN = (34, 211, 238)   # #22D3EE
TEXT_WHITE = (248, 250, 252)   # snow
TEXT_SLATE = (203, 213, 225)   # slate-300
TEXT_DIM = (148, 163, 184)     # slate-400
FOOTER_DIM = (100, 116, 139)   # slate-500

FONT_BOLD = "/private/tmp/og-fonts/Pretendard-Bold.otf"
FONT_SEMI = "/private/tmp/og-fonts/Pretendard-SemiBold.otf"
FONT_REG = "/private/tmp/og-fonts/Pretendard-Regular.otf"

OUT = Path("/Users/seung-yeoblee/dev/unpack-blogs/docs/naver-setup/editions/images/03-perplexity")


def wrap(text, font, max_w):
    lines, cur = [], ""
    for w in text.split(" "):
        trial = (cur + " " + w).strip()
        if font.getbbox(trial)[2] <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_card(draw, x, y, w, h, num, title, body, num_color=ACCENT_CYAN):
    # Card background
    draw.rounded_rectangle((x, y, x + w, y + h), radius=18, fill=CARD_BG, outline=CARD_BORDER, width=1)
    # Number badge (circle)
    badge_size = 50
    badge_x, badge_y = x + 28, y + 28
    draw.ellipse((badge_x, badge_y, badge_x + badge_size, badge_y + badge_size), fill=num_color)
    num_font = ImageFont.truetype(FONT_BOLD, 28)
    nb = num_font.getbbox(str(num))
    nx = badge_x + (badge_size - (nb[2] - nb[0])) // 2 - nb[0]
    ny = badge_y + (badge_size - (nb[3] - nb[1])) // 2 - nb[1] - 2
    draw.text((nx, ny), str(num), font=num_font, fill=BG)

    # Title
    title_font = ImageFont.truetype(FONT_BOLD, 28)
    title_y = y + 100
    draw.text((x + 28, title_y), title, font=title_font, fill=TEXT_WHITE)

    # Body (multi-line)
    body_font = ImageFont.truetype(FONT_REG, 19)
    body_lines = wrap(body, body_font, w - 56)
    by = title_y + 50
    for line in body_lines:
        draw.text((x + 28, by), line, font=body_font, fill=TEXT_SLATE)
        by += 28


def render_weaknesses():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")

    # 미세 가로선 noise
    for y in range(0, H, 80):
        draw.line([(0, y), (W, y)], fill=(20, 30, 50), width=1)

    # 헤더
    title_font = ImageFont.truetype(FONT_BOLD, 56)
    sub_font = ImageFont.truetype(FONT_SEMI, 22)
    title = "Perplexity 3가지 단점"
    sub = "3일 실사용 후 발견한 솔직한 한계"
    tw = title_font.getbbox(title)[2]
    draw.text(((W - tw) // 2, 60), title, font=title_font, fill=TEXT_WHITE)
    sw = sub_font.getbbox(sub)[2]
    draw.text(((W - sw) // 2, 130), sub, font=sub_font, fill=TEXT_DIM)
    # divider underline
    draw.rectangle(((W // 2 - 60), 180, (W // 2 + 60), 184), fill=ACCENT_CYAN)

    # 카드 3개
    card_w = 420
    card_h = 380
    gap = 30
    total_w = card_w * 3 + gap * 2
    start_x = (W - total_w) // 2
    cy = 230

    cards = [
        (1, "최신 뉴스 속도", "네이버가 20~30분 빠름. 긴급 뉴스·주가 변동은 네이버 승. 인덱싱 시간차 존재."),
        (2, "한국 커뮤니티", "디시·뽐뿌·맘카페 같은 한국 전용 사이트 검색은 네이버가 압도적."),
        (3, "쇼핑·지도", "시도할 필요도 없음. 네이버 쇼핑·지도는 한국 전용 영역, Perplexity 미지원."),
    ]
    for i, (n, t, b) in enumerate(cards):
        x = start_x + i * (card_w + gap)
        draw_card(draw, x, cy, card_w, card_h, n, t, b)

    # 푸터 결론
    foot_font = ImageFont.truetype(FONT_BOLD, 26)
    foot = "정보 리서치는 Perplexity, 쇼핑·지도·실시간은 네이버"
    fw = foot_font.getbbox(foot)[2]
    draw.text(((W - fw) // 2, H - 110), foot, font=foot_font, fill=ACCENT_CYAN)

    # 하단 브랜드
    brand_font = ImageFont.truetype(FONT_REG, 18)
    brand = "babipa의 AIGrit · 네이버 블로그"
    bw = brand_font.getbbox(brand)[2]
    draw.text((W - bw - 40, H - 38), brand, font=brand_font, fill=FOOTER_DIM)

    out = OUT / "07-weaknesses.png"
    img.save(out, "PNG", optimize=True)
    print(f"✓ {out.name} (AIGrit dark tone)")


def render_use_cases():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")

    for y in range(0, H, 80):
        draw.line([(0, y), (W, y)], fill=(20, 30, 50), width=1)

    title_font = ImageFont.truetype(FONT_BOLD, 56)
    sub_font = ImageFont.truetype(FONT_SEMI, 22)
    title = "Perplexity 부업 활용 꿀팁"
    sub = "3일 실사용에서 건진 실전 유즈케이스 5가지"
    tw = title_font.getbbox(title)[2]
    draw.text(((W - tw) // 2, 60), title, font=title_font, fill=TEXT_WHITE)
    sw = sub_font.getbbox(sub)[2]
    draw.text(((W - sw) // 2, 130), sub, font=sub_font, fill=TEXT_DIM)
    draw.rectangle(((W // 2 - 60), 180, (W // 2 + 60), 184), fill=ACCENT_CYAN)

    # 카드 5개 (작은 크기로 배치)
    card_w = 260
    card_h = 380
    gap = 18
    total_w = card_w * 5 + gap * 4
    start_x = (W - total_w) // 2
    cy = 230

    cards = [
        (1, "트렌드 조사", "출처 포함 답변으로 블로그·유튜브 기획안 자동화"),
        (2, "경쟁사 분석", "스마트스토어 상위 판매자 공통점 실제 데이터 기반"),
        (3, "법·세금 질문", "국세청·공식 출처 바로 연결. 2026 최신 개정안 반영"),
        (4, "외국 부업 트렌드", "영어권 원문 자동 번역해서 국내로 가져오기"),
        (5, "학습 자료", "입문 커리큘럼을 단계별로 자동 정리"),
    ]
    for i, (n, t, b) in enumerate(cards):
        x = start_x + i * (card_w + gap)
        draw_card(draw, x, cy, card_w, card_h, n, t, b)

    foot_font = ImageFont.truetype(FONT_BOLD, 26)
    foot = "부업 리서치 시간 70% 단축 — 출처 있는 답변의 힘"
    fw = foot_font.getbbox(foot)[2]
    draw.text(((W - fw) // 2, H - 110), foot, font=foot_font, fill=ACCENT_CYAN)

    brand_font = ImageFont.truetype(FONT_REG, 18)
    brand = "babipa의 AIGrit · 네이버 블로그"
    bw = brand_font.getbbox(brand)[2]
    draw.text((W - bw - 40, H - 38), brand, font=brand_font, fill=FOOTER_DIM)

    out = OUT / "08-use-cases.png"
    img.save(out, "PNG", optimize=True)
    print(f"✓ {out.name} (AIGrit dark tone)")


if __name__ == "__main__":
    render_weaknesses()
    render_use_cases()
    print("\n완료 — 톤 통일 (AIGrit Indigo+Cyan dark)")
