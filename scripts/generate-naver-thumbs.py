"""
Naver Blog 프롤로그 정사각형 썸네일 생성기 (1080x1080)

- AIGrit 브랜드 톤 (Dark BG + Cyan accent + [AI]Grit 로고)
- 한글 제목 중앙 정렬 (자동 줄바꿈)
- 하단 브랜드 마크
- 출력: docs/naver-setup/editions/images/{slug}/thumb-square.png
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# ---------- 디자인 토큰 ----------
SIZE = 1080
BG = (15, 23, 42)  # #0F172A — Naver dark slate
ACCENT_CYAN = (34, 211, 238)  # #22D3EE
TEXT_WHITE = (248, 250, 252)  # #F8FAFC
TEXT_DIM = (148, 163, 184)  # slate-400
BADGE_BG = (34, 211, 238, 38)  # cyan @ 15%

FONT_BOLD = "/private/tmp/og-fonts/Pretendard-Bold.otf"
FONT_SEMI = "/private/tmp/og-fonts/Pretendard-SemiBold.otf"
FONT_REG = "/private/tmp/og-fonts/Pretendard-Regular.otf"

PADDING = 80


# ---------- 유틸 ----------
def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    """글자 단위 wrap (한글 안전)"""
    lines: list[str] = []
    words = text.split(" ")
    cur = ""
    for w in words:
        trial = (cur + " " + w).strip()
        if font.getbbox(trial)[2] <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_rounded_rect(draw, xy, radius, fill):
    draw.rounded_rectangle(xy, radius=radius, fill=fill)


# ---------- 메인 렌더 ----------
def render(slug: str, category: str, title: str, accent: str, output: Path) -> None:
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img, "RGBA")

    # subtle horizontal gradient lines (faux noise)
    for y in range(0, SIZE, 80):
        draw.line([(0, y), (SIZE, y)], fill=(20, 30, 50), width=1)

    # 상단 좌측 카테고리 배지
    cat_font = ImageFont.truetype(FONT_SEMI, 28)
    cat_w = cat_font.getbbox(category)[2] + 40
    cat_h = 50
    draw_rounded_rect(
        draw,
        (PADDING, PADDING, PADDING + cat_w, PADDING + cat_h),
        radius=25,
        fill=(34, 211, 238, 50),
    )
    draw.text(
        (PADDING + 20, PADDING + 8),
        category,
        font=cat_font,
        fill=ACCENT_CYAN,
    )

    # 본문 (제목) — 폰트 크기 자동 조정
    max_w = SIZE - PADDING * 2
    title_size = 92
    while title_size > 56:
        title_font = ImageFont.truetype(FONT_BOLD, title_size)
        lines = wrap_text(title, title_font, max_w)
        line_height = int(title_size * 1.25)
        block_h = line_height * len(lines)
        if len(lines) <= 4 and block_h <= 580:
            break
        title_size -= 6

    title_font = ImageFont.truetype(FONT_BOLD, title_size)
    lines = wrap_text(title, title_font, max_w)
    line_height = int(title_size * 1.25)
    block_h = line_height * len(lines)

    # 중앙 수직 정렬
    start_y = (SIZE - block_h) // 2 - 20
    for i, line in enumerate(lines):
        line_w = title_font.getbbox(line)[2]
        x = (SIZE - line_w) // 2
        draw.text((x, start_y + i * line_height), line, font=title_font, fill=TEXT_WHITE)

    # 강조 한 줄 (accent — 옵션)
    if accent:
        accent_font = ImageFont.truetype(FONT_SEMI, 38)
        accent_w = accent_font.getbbox(accent)[2]
        ax = (SIZE - accent_w) // 2
        ay = start_y + block_h + 30
        draw.text((ax, ay), accent, font=accent_font, fill=ACCENT_CYAN)

    # 하단 [AI]Grit 워드마크 (좌측 정렬)
    brand_font = ImageFont.truetype(FONT_BOLD, 56)
    bracket_w = brand_font.getbbox("[AI]")[2]
    grit_w = brand_font.getbbox("Grit")[2]
    brand_y = SIZE - PADDING - 56
    # [AI] - cyan
    draw.text((PADDING, brand_y), "[AI]", font=brand_font, fill=ACCENT_CYAN)
    # Grit - white
    draw.text((PADDING + bracket_w + 8, brand_y), "Grit", font=brand_font, fill=TEXT_WHITE)

    # 우측 하단 도메인
    dom_font = ImageFont.truetype(FONT_REG, 28)
    dom_w = dom_font.getbbox("aigrit.dev")[2]
    draw.text(
        (SIZE - PADDING - dom_w, brand_y + 22),
        "aigrit.dev",
        font=dom_font,
        fill=TEXT_DIM,
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output, "PNG", optimize=True)
    print(f"✓ {output.relative_to(Path('/Users/seung-yeoblee/dev/unpack-blogs'))}  ({title_size}px)")


# ---------- 데이터 ----------
BASE = Path("/Users/seung-yeoblee/dev/unpack-blogs/docs/naver-setup/editions/images")

POSTS = [
    {
        "slug": "01-apple-shortcuts",
        "category": "AI 자동화",
        "title": "아이폰 단축어 AI 자동화 5가지",
        "accent": '"이걸 왜 이제 알았지?"',
    },
    {
        "slug": "02-notion-ai",
        "category": "AI 도구 리뷰",
        "title": "퇴근 후 30분, Notion AI로 부업 기반 만들기",
        "accent": "직장인 부업 5가지 활용법",
    },
    {
        "slug": "03-perplexity",
        "category": "AI 도구 리뷰",
        "title": "네이버 검색 대신 AI 검색 3일 써본 후기",
        "accent": "Perplexity 부업 리서치",
    },
]

if __name__ == "__main__":
    for p in POSTS:
        out = BASE / p["slug"] / "00-thumb-square.png"
        render(p["slug"], p["category"], p["title"], p["accent"], out)
    print("\n✅ 완료 — 각 폴더 00-thumb-square.png")
