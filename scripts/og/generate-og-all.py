#!/usr/bin/env python3
"""
Mass OG generator for UnpackBlogs (babipanote + AIGrit).

Spec sources:
  - apps/babipanote/docs/BRAND_GUIDELINES.md
  - docs/THUMBNAIL.md

Both blogs: 1200x630 PNG.

babipanote: Gowun Batang Bold (title/brand/author, 세리프), Lora Bold (quote),
            Pretendard (body). Paper gradient, Plum primary.

AIGrit: Inter-like sans-serif via Pretendard+Inter mix. Slate→Indigo gradient,
        Cyan accent.
"""
import json, re
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630

# === Fonts ===
F = {
    "gowun_bold": "/tmp/og-fonts/GowunBatang-Bold.ttf",
    "gowun_reg": "/tmp/og-fonts/GowunBatang-Regular.ttf",
    "lora_bold": "/tmp/og-fonts/Lora-Bold.ttf",
    "pretendard_bold": "/tmp/og-fonts/Pretendard-Bold.otf",
    "pretendard_semi": "/tmp/og-fonts/Pretendard-SemiBold.otf",
    "pretendard_reg": "/tmp/og-fonts/Pretendard-Regular.otf",
}

def font(path_key, size):
    return ImageFont.truetype(F[path_key], size)


# === Color helpers ===
BB = {
    "plum": (107, 46, 78),
    "ink": (43, 36, 32),
    "terracotta": (200, 159, 124),
    "muted": (160, 139, 122),
    "paperLight": (250, 247, 242),
    "paperDeep": (240, 235, 227),
    "white": (255, 255, 255),
}
AG = {
    "bgTop": (15, 23, 42),
    "bgBot": (30, 27, 75),
    "red": (239, 68, 68),
    "cyan": (6, 182, 212),
    "indigo": (55, 48, 163),
    "slate": (148, 163, 184),
    "white": (255, 255, 255),
}


def gradient(top_left, bot_right):
    img = Image.new("RGB", (W, H), top_left)
    px = img.load()
    for y in range(H):
        for x in range(W):
            t = (x / W + y / H) / 2
            px[x, y] = (
                int(top_left[0] * (1 - t) + bot_right[0] * t),
                int(top_left[1] * (1 - t) + bot_right[1] * t),
                int(top_left[2] * (1 - t) + bot_right[2] * t),
            )
    return img


def rounded(draw, xy, r, fill):
    x1, y1, x2, y2 = xy
    draw.rectangle([x1 + r, y1, x2 - r, y2], fill=fill)
    draw.rectangle([x1, y1 + r, x2, y2 - r], fill=fill)
    for cx, cy, a1, a2 in [(x1, y1, 180, 270), (x2 - 2*r, y1, 270, 360),
                            (x1, y2 - 2*r, 90, 180), (x2 - 2*r, y2 - 2*r, 0, 90)]:
        draw.pieslice([cx, cy, cx + 2*r, cy + 2*r], a1, a2, fill=fill)


def wrap_text(text, f, max_width, draw, max_lines=2):
    # Prefer wrapping at em-dash
    if " — " in text and draw.textlength(text, font=f) > max_width:
        a, b = text.split(" — ", 1)
        lines = [a + " —", b]
        # If b itself still too wide, further wrap b
        if draw.textlength(b, font=f) > max_width:
            wrapped = _word_wrap(b, f, max_width, draw)
            lines = [a + " —"] + wrapped[:max_lines - 1]
        return lines[:max_lines]
    if draw.textlength(text, font=f) <= max_width:
        return [text]
    return _word_wrap(text, f, max_width, draw)[:max_lines]


def _word_wrap(text, f, max_width, draw):
    # First try space-based
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=f) <= max_width:
            cur = trial
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    # If still too wide (no spaces), hard break
    final = []
    for ln in lines:
        if draw.textlength(ln, font=f) <= max_width:
            final.append(ln)
        else:
            # Hard character break
            buf = ""
            for ch in ln:
                if draw.textlength(buf + ch, font=f) <= max_width:
                    buf += ch
                else:
                    final.append(buf)
                    buf = ch
            if buf: final.append(buf)
    return final


# === babipanote renderer ===
def render_babipanote(title, category, date_str):
    img = gradient(BB["paperLight"], BB["paperDeep"])
    draw = ImageDraw.Draw(img)

    # Badge (Plum, rounded 22, Pretendard SemiBold 20 white)
    badge_f = font("pretendard_semi", 20)
    bw = int(draw.textlength(category, font=badge_f)) + 48
    rounded(draw, (60, 40, 60 + bw, 40 + 44), 22, BB["plum"])
    bx = 60 + (bw - draw.textlength(category, font=badge_f)) / 2
    draw.text((bx, 40 + 10), category, fill=BB["white"], font=badge_f)

    # Date (Pretendard Regular 18 Muted)
    date_f = font("pretendard_reg", 18)
    draw.text((60 + bw + 16, 40 + 12), date_str, fill=BB["muted"], font=date_f)

    # Quote "" (Lora Bold 90 Plum 40%)
    quote_f = font("lora_bold", 90)
    q = "“”"
    qw = draw.textlength(q, font=quote_f)
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.text((W - qw - 60, 10), q,
            fill=(*BB["plum"], 102), font=quote_f)
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(img)

    # Title (Gowun Batang Bold 56 Ink, 2 lines)
    title_f = font("gowun_bold", 56)
    lines = wrap_text(title, title_f, 1080, draw, max_lines=2)
    y = 210
    for ln in lines:
        draw.text((60, y), ln, fill=BB["ink"], font=title_f)
        y += 78

    # Divider (60x4 Terracotta at y:500)
    draw.rectangle([60, 500, 120, 504], fill=BB["terracotta"])

    # Author "babipa" (Gowun Batang Bold 26 Ink)
    draw.text((60, 520), "babipa", fill=BB["ink"], font=font("gowun_bold", 26))

    # Tagline (Pretendard Regular 16 Muted)
    draw.text((60, 562), "빌더의 하루는 코드와 고민 사이에서",
              fill=BB["muted"], font=font("pretendard_reg", 16))

    # Brand "babipanote·" (Gowun Batang Bold 26 Plum, right-align)
    brand_f = font("gowun_bold", 26)
    bt = "babipanote·"
    btw = draw.textlength(bt, font=brand_f)
    draw.text((W - 60 - btw, 518), bt, fill=BB["plum"], font=brand_f)

    # Domain (Pretendard Regular 16 Muted, right-align)
    dom_f = font("pretendard_reg", 16)
    dom = "babipanote.com"
    dw = draw.textlength(dom, font=dom_f)
    draw.text((W - 60 - dw, 562), dom, fill=BB["muted"], font=dom_f)

    return img


# === AIGrit renderer ===
def render_aigrit(title, category, subtitle):
    img = gradient(AG["bgTop"], AG["bgBot"])
    draw = ImageDraw.Draw(img)

    # Badge (Red, pill shape, Pretendard SemiBold 16 white)
    badge_f = font("pretendard_semi", 16)
    bh = 40
    bw = int(draw.textlength(category, font=badge_f)) + 48
    rounded(draw, (60, 40, 60 + bw, 40 + bh), bh // 2, AG["red"])
    bx = 60 + (bw - draw.textlength(category, font=badge_f)) / 2
    draw.text((bx, 40 + 11), category, fill=AG["white"], font=badge_f)

    # L-bracket top-right (Cyan 3px, 50×50)
    draw.rectangle([1090, 40, 1140, 43], fill=AG["cyan"])   # horizontal
    draw.rectangle([1137, 40, 1140, 90], fill=AG["cyan"])   # vertical

    # Title (Pretendard Bold 48 white, maxWidth 1000, 2 lines)
    title_f = font("pretendard_bold", 48)
    lines = wrap_text(title, title_f, 1000, draw, max_lines=2)
    y = 180
    for ln in lines:
        draw.text((60, y), ln, fill=AG["white"], font=title_f)
        y += 58

    # Subtitle (Pretendard Bold 40 Cyan, 1 line, positioned after title)
    sub_f = font("pretendard_bold", 40)
    sub_lines = wrap_text(subtitle, sub_f, 1000, draw, max_lines=1)
    draw.text((60, y + 16), sub_lines[0] if sub_lines else subtitle,
              fill=AG["cyan"], font=sub_f)

    # Divider (60x3 Indigo at y:500)
    draw.rectangle([60, 500, 120, 503], fill=AG["indigo"])

    # Logo "[AI] Grit" (Pretendard SemiBold 24 Cyan)
    draw.text((60, 520), "[AI] Grit", fill=AG["cyan"],
              font=font("pretendard_semi", 24))

    # Tagline (Pretendard Regular 14 Slate)
    draw.text((60, 556), "AI의 알맹이만 남긴다",
              fill=AG["slate"], font=font("pretendard_reg", 14))

    # Domain right-align
    dom_f = font("pretendard_reg", 14)
    dom = "aigrit.dev"
    dw = draw.textlength(dom, font=dom_f)
    draw.text((W - 60 - dw, 556), dom, fill=AG["slate"], font=dom_f)

    return img


# === AIGrit subtitle map (1-line keyword summaries) ===
AG_SUBTITLES = {
    "hello-world": "리뷰 원칙 · 3일 이상 직접 사용",
    "ai-tools-2026-guide": "20개 써보고 살아남은 10개",
    "apple-shortcuts-ai-automation": "하루 40분 절약 레시피",
    "claude-4-sonnet-vs-gpt-4o": "한국어·코딩·추론 실전 테스트",
    "claude-code-vs-cursor": "실제 프로젝트 교차 테스트",
    "claude-mcp-guide": "AI가 내 파일을 직접 다룬다",
    "craft-vs-notion": "1년씩 써본 노트앱 비교",
    "notion-ai-guide": "5가지 용도 실측 후기",
    "perplexity-ai-guide": "구글을 완전히 대체할까",
    "solo-developer-automation-stack": "월 6.5만원 자동화 스택",
    "claude-code-flutter-app-guide": "비개발자 2주 App Store 출시기",
}

# AIGrit: shorten overly long titles for OG (title area)
AG_TITLE_OVERRIDES = {
    "claude-4-sonnet-vs-gpt-4o": "Claude 4 Sonnet vs GPT-4o 비교",
    "claude-code-vs-cursor": "Claude Code vs Cursor 비교",
    "claude-mcp-guide": "Claude MCP 활용법",
    "craft-vs-notion": "Craft vs Notion — 2026 결정 가이드",
    "apple-shortcuts-ai-automation": "Apple 단축어로 만드는 AI 자동화 5가지",
    "notion-ai-guide": "Notion AI 완벽 활용법",
    "perplexity-ai-guide": "Perplexity AI 사용법",
    "solo-developer-automation-stack": "1인 개발자 자동화 스택 10가지",
    "ai-tools-2026-guide": "2026 AI 도구 완벽 가이드",
    "hello-world": "AIGrit — 리뷰 원칙과 첫 글",
    "claude-code-flutter-app-guide": "Claude Code + Flutter로 앱 만들기 실전 가이드",
}

# babipanote: shorten overly long titles for OG if needed
BB_TITLE_OVERRIDES = {
    "app-store-review-gentledo-launch":
        "App Store 심사 2일 통과기 — path_provider와 iPad 함정",
    "building-gentledo-with-claude-code":
        "비개발자가 Claude Code로 Flutter 앱을 만든다는 것",
    "craft-naver-workflow":
        "Craft → 네이버 복붙 워크플로우 — 이중 플랫폼 10단계",
    "time-management-solo-builder":
        "1인 빌더의 시간 관리 — 주 13시간 분할법",
    "aigrit-month1-revenue":
        "AIGrit 첫 달 중간 리포트 (1주차)",
}


def main():
    posts = json.loads(Path("/tmp/og-posts.json").read_text(encoding="utf-8"))

    base = Path("/Users/seung-yeoblee/dev/unpack-blogs/apps")
    count = 0

    for p in posts["babipanote"]:
        title = BB_TITLE_OVERRIDES.get(p["slug"], p["title"])
        out_dir = base / "babipanote" / "public" / "images" / p["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        img = render_babipanote(title, p["category"], p["date_str"])
        out = out_dir / "og.png"
        img.save(out, "PNG", optimize=True)
        kb = out.stat().st_size / 1024
        print(f"✓ babipanote/{p['slug']}/og.png  ({kb:.1f}KB)")
        count += 1

    for p in posts["aigrit"]:
        title = AG_TITLE_OVERRIDES.get(p["slug"], p["title"])
        subtitle = AG_SUBTITLES.get(p["slug"], "AI 도구 실사용 리뷰")
        out_dir = base / "aigrit" / "public" / "images" / p["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        img = render_aigrit(title, p["category"], subtitle)
        out = out_dir / "og.png"
        img.save(out, "PNG", optimize=True)
        kb = out.stat().st_size / 1024
        print(f"✓ aigrit/{p['slug']}/og.png  ({kb:.1f}KB)")
        count += 1

    print(f"\n✅ Generated {count} OG images.")


if __name__ == "__main__":
    main()
