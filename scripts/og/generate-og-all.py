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
def render_aigrit(title, category, subtitle, lang="ko"):
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
    tagline = "AI의 알맹이만 남긴다" if lang == "ko" else "Only the essence of AI"
    draw.text((60, 556), tagline,
              fill=AG["slate"], font=font("pretendard_reg", 14))

    # Domain right-align
    dom_f = font("pretendard_reg", 14)
    dom = "aigrit.dev"
    dw = draw.textlength(dom, font=dom_f)
    draw.text((W - 60 - dw, 556), dom, fill=AG["slate"], font=dom_f)

    return img


# === AIGrit subtitle map (1-line keyword summaries) ===
AG_SUBTITLES = {
    "hello-world": "글의 근거와 쓰지 않는 것",
    "ai-tools-2026-guide": "챗봇 · 검색 · 코딩 · 이미지 · 자동화 10개",
    "apple-shortcuts-ai-automation": "요약 · 캡처 · 음성 · 번역 · 일정",
    "claude-4-sonnet-vs-gpt-4o": "공식 스펙·가격 · 직접 비교하는 5단계",
    "claude-code-vs-cursor": "터미널 에이전트 vs AI 에디터",
    "claude-mcp-guide": "AI가 내 파일을 직접 다룬다",
    "craft-vs-notion": "글쓰기 앱과 워크스페이스, 역할로 고르기",
    "notion-ai-guide": "5가지 용도와 요금제 판단",
    "perplexity-ai-guide": "구글 검색을 대체할 수 있을까?",
    "solo-developer-automation-stack": "월 6만 원대 실제 구성과 도입 순서",
    "claude-code-flutter-app-guide": "비개발자 2주 App Store 출시기",
    "ai-side-income-100man-roadmap": "9가지 경로 · 한국 거주자 체크포인트",
    "make-automation-guide": "첫 시나리오부터 Slack · Notion · Gmail",
    "sell-ai-prompts-promptbase": "팔리는 조건 · 정산 체크포인트",
    "ai-ebook-kindle-kdp": "로열티 · AI 공개 규정 · 파이프라인",
    "chatgpt-coupang-partners-automation": "자동화 범위 · 대가성 표시",
    "prompt-engineering-freelance": "패키지 · 가격 · 수주 프로세스",
    "ai-newsletter-substack-growth": "니치 · 첫 구독자 · 한국 정산 현실",
    "ai-coding-complete-guide-2026": "Claude Code · Cursor · MCP 흐름 설계",
    "runway-vs-sora-video-ai": "편집해서 깎을까, 문장으로 뽑을까",
    "notion-alternatives-best-5": "Obsidian · Craft · Logseq · Anytype · Capacities",
    "adsense-approval-prep-checklist": "공식 미승인 사유 4가지로 점검하기",
    "ai-translation-tools-comparison": "DeepL vs ChatGPT vs Claude",
    "claude-projects-vs-chatgpt-gpts": "비공개 작업공간 vs 배포용 어시스턴트",
    "obsidian-mcp-plugins-best-5": "Claude와 vault를 연결하는 방법",
    "claude-blog-workflow-seo": "1인 운영자의 자동화 SOP",
    "obsidian-claude-code-mcp": "노트와 코드를 한 워크플로우로",
    # 예약 글 (2026-10 정비)
    "elevenlabs-vs-resemble-ai": "음성 합성 vs 딥페이크 탐지, 두 회사의 길",
    "ai-search-engines-comparison": "Perplexity vs ChatGPT Search vs Gemini",
    "ai-presentation-tools-2026": "Gamma vs Canva AI vs PowerPoint Copilot",
    "zapier-vs-make-vs-n8n": "쉬움 · 분기 · 셀프호스팅으로 고르기",
    "v0-vs-bolt-vs-lovable": "AI 웹 빌더, 결과물 성격으로 고르기",
    "github-copilot-vs-claude-code": "IDE 자동완성 vs 터미널 에이전트",
    "ai-writing-tools-comparison": "Jasper vs Copy.ai vs Claude",
    "ai-video-tools-complete-guide-2026": "생성 · 편집 · 아바타 · 음성, 역할로 고르기",
    "ai-design-tools-complete-guide-2026": "이미지 · 로고 · UI · 라이선스 확인",
    "nocode-vibe-coding-saas-guide-2026": "도구 역할 · 출시 스택 · 결제 체크",
    "ai-agent-complete-guide-2026": "MCP · 도입 순서 · 도구 비교",
    "heygen-vs-synthesia-vrew": "글로벌 · 기업 교육 · 한국어 자막으로 고르기",
    "canva-ai-vs-firefly-vs-recraft": "콘텐츠 · 상업 이용 · 벡터로 고르기",
    "build-saas-with-lovable-14days": "2주 출시 계획과 결제·보안 점검",
    "claude-agent-sdk-getting-started": "툴 정의 · 에이전트 루프 · 배포",
    "chatgpt-blog-content-pipeline": "양산 대신 품질을 지키는 6단계",
    "kling-vs-sora-vs-veo": "접근 경로와 용도로 고르는 AI 영상 생성",
    "ai-marketing-automation-guide-2026": "콘텐츠 · SNS · 이메일 · 광고 · 세일즈",
    "suno-vs-udio-ai-music": "음반사 합의 이후 달라진 AI 음악 조건",
    "cursor-vs-windsurf-vs-claude-code": "AI 에디터와 터미널 에이전트, 작업 방식으로",
    "figma-ai-design-automation": "Figma Make · 에이전트 · MCP 자동화",
    "bubble-vs-flutterflow": "결과물과 코드 소유로 고르는 노코드 빌더",
    "n8n-ai-agent-workflows": "메일 · 리서치 · 문의 · 콘텐츠 · 모니터링 레시피",
    "ai-instagram-reels-automation": "얼굴 없는 채널 파이프라인과 수익화 조건",
    "elevenlabs-audiobook-monetization": "제작 절차와 AI 낭독을 받는 판매처",
    "ai-cold-email-sales-automation": "Clay · Instantly와 보내기 전 법규 체크",
    "midjourney-pod-print-on-demand": "Redbubble · 마플 판매 조건과 저작권 체크",
    "replit-agent-vs-bolt": "운영까지 한 곳에서 vs 빠른 프로토타입",
    "ai-translation-content-localization": "현지화와 hreflang 세팅",
    "perplexity-vs-chatgpt-search-gemini": "Perplexity vs ChatGPT vs Gemini",
    "gamma-vs-tome-vs-beautiful-ai": "Tome 종료 이후 AI 발표자료 도구",
    "claude-discord-slack-bot": "공용 Claude 호출 + 플랫폼별 입출구",
    "ai-social-content-calendar": "한 달치를 배치로 만드는 4단계",
    "descript-video-podcast-editing": "팟캐스트 · 유튜브를 글처럼 편집하기",
    "supabase-ai-saas-backend": "인증 · RLS · 타입 · 결제 웹훅",
    "ai-data-analysis-tools-comparison": "ChatGPT vs Julius vs Claude",
    "solo-saas-pricing-payments": "Stripe · MoR · 국내 PG, 한국 사업자 기준",
    "ai-newsletter-automation-system": "Beehiiv · Substack · Kit + 검수 한 칸",
    "ideogram-vs-recraft-text-image": "글자 들어간 AI 이미지 — 래스터 vs 벡터",
    "cline-vs-roo-code": "단계별 승인 vs 역할별 모드",
    "ai-ebook-kmong-talent-market": "제작 5단계 · 판매처 · 가격 역산",
    "make-ai-automation-recipes": "트리거 → AI → 분기 → 출력 레시피",
    "ai-voice-cloning-guide": "내 목소리 복제 절차와 넘으면 안 되는 선",
    "korean-ai-chatbot-comparison": "클로바X 종료 이후 ChatGPT · Gemini · Claude · 뤼튼",
    "ai-coupang-product-content": "카피 · 리뷰 요약 · 이미지 분담과 등록 전 검수",
    "claude-code-chrome-extension": "Manifest V3 작성부터 웹 스토어 등록까지",
    "ai-thumbnail-generation-workflow": "배경 · 글자 분리, 변형 제작, 유튜브 A/B 테스트",
    "zapier-ai-actions-guide": "Copilot · AI by Zapier · Zapier MCP",
    "ai-agent-research-automation": "수집 · 검증 · 요약 · 합성 파이프라인 설계",
    "notion-ai-vs-chatgpt-docs": "업무 문서 작성, 어디서 할까",
    "ai-online-course-creation": "커리큘럼 · 슬라이드 · 대본 초안과 플랫폼 고르기",
    "obsidian-ai-second-brain": "캡처 · 정리 · 연결 · 회수 워크플로우",
    "ai-resume-job-tools-comparison": "자소서 · 이력서 · 면접 — 범용 챗봇과 이력서 전용 도구",
    "stable-diffusion-local-guide": "ComfyUI · ControlNet · LoRA · 라이선스 확인",
    "ai-subtitle-translation-youtube": "YouTube 자동 더빙과 다국어 오디오 트랙",
    "build-rag-chatbot-saas": "pgvector 스키마 · 테넌트 분리 · 비용 구조",
    "ai-prompt-management-tools": "PromptLayer · Langfuse · Helicone",
}

# AIGrit: shorten overly long titles for OG (title area)
AG_TITLE_OVERRIDES = {
    "claude-4-sonnet-vs-gpt-4o": "Claude Sonnet 4 vs GPT-4o 비교",
    "claude-code-vs-cursor": "Claude Code vs Cursor 비교",
    "claude-mcp-guide": "Claude MCP 활용법",
    "craft-vs-notion": "Craft vs Notion 비교",
    "apple-shortcuts-ai-automation": "Apple 단축어 AI 자동화 5가지",
    "notion-ai-guide": "Notion AI 활용법",
    "perplexity-ai-guide": "Perplexity AI 사용법",
    "solo-developer-automation-stack": "1인 개발자 자동화 스택 10가지",
    "ai-tools-2026-guide": "2026 AI 도구 가이드",
    "hello-world": "AIGrit — 리뷰 원칙과 첫 글",
    "claude-code-flutter-app-guide": "Claude Code + Flutter로 앱 만들기 실전 가이드",
    "ai-side-income-100man-roadmap": "AI 부업 로드맵 2026",
    "make-automation-guide": "Make 자동화 사용법",
    "sell-ai-prompts-promptbase": "AI 프롬프트 판매 시작 가이드",
    "ai-ebook-kindle-kdp": "AI 전자책 Kindle KDP 출판 가이드",
    "chatgpt-coupang-partners-automation": "ChatGPT 쿠팡파트너스 글쓰기 가이드",
    "prompt-engineering-freelance": "프롬프트 엔지니어 프리랜싱 가이드",
    "ai-newsletter-substack-growth": "Substack AI 뉴스레터 시작 가이드",
    "ai-coding-complete-guide-2026": "AI 코딩 완벽 가이드 2026",
    "runway-vs-sora-video-ai": "Runway vs Sora — AI 영상 생성 비교",
    "notion-alternatives-best-5": "Notion 대체 앱 BEST 5",
    "adsense-approval-prep-checklist": "AdSense 승인 셋업 체크리스트",
    "ai-translation-tools-comparison": "AI 번역 도구 비교",
    "claude-projects-vs-chatgpt-gpts": "Claude Projects vs ChatGPT GPTs",
    "obsidian-mcp-plugins-best-5": "Obsidian MCP 플러그인 BEST 5",
    "claude-blog-workflow-seo": "Claude로 블로그 글쓰기·발행·SEO 추적",
    "obsidian-claude-code-mcp": "Obsidian × Claude Code MCP 연결",
    # 예약 글 (2026-10 정비)
    "elevenlabs-vs-resemble-ai": "ElevenLabs vs Resemble AI",
    "ai-search-engines-comparison": "AI 검색 엔진 비교",
    "ai-presentation-tools-2026": "AI PPT 도구 비교",
    "zapier-vs-make-vs-n8n": "Zapier vs Make vs n8n 비교",
    "v0-vs-bolt-vs-lovable": "v0 vs Bolt vs Lovable",
    "github-copilot-vs-claude-code": "GitHub Copilot vs Claude Code",
    "ai-writing-tools-comparison": "AI 글쓰기 도구 비교",
    "ai-video-tools-complete-guide-2026": "AI 영상 제작 도구 완벽 가이드 2026",
    "ai-design-tools-complete-guide-2026": "AI 디자인 도구 완벽 가이드 2026",
    "nocode-vibe-coding-saas-guide-2026": "노코드·바이브 코딩 SaaS 가이드 2026",
    "ai-agent-complete-guide-2026": "AI 에이전트 완벽 가이드 2026",
    "heygen-vs-synthesia-vrew": "HeyGen vs Synthesia vs Vrew",
    "canva-ai-vs-firefly-vs-recraft": "Canva AI vs Firefly vs Recraft",
    "build-saas-with-lovable-14days": "Lovable로 SaaS 만들기",
    "claude-agent-sdk-getting-started": "Claude Agent SDK 입문",
    "chatgpt-blog-content-pipeline": "ChatGPT 블로그 글쓰기 파이프라인",
    "kling-vs-sora-vs-veo": "Kling vs Sora vs Veo",
    "ai-marketing-automation-guide-2026": "AI 마케팅 자동화 완벽 가이드 2026",
    "suno-vs-udio-ai-music": "Suno vs Udio",
    "cursor-vs-windsurf-vs-claude-code": "Cursor vs Windsurf vs Claude Code",
    "figma-ai-design-automation": "Figma AI 활용법",
    "bubble-vs-flutterflow": "Bubble vs FlutterFlow",
    "n8n-ai-agent-workflows": "n8n AI 에이전트 워크플로우",
    "ai-instagram-reels-automation": "AI로 인스타그램 릴스 만들기",
    "elevenlabs-audiobook-monetization": "ElevenLabs로 오디오북 만들기",
    "ai-cold-email-sales-automation": "AI 콜드메일·세일즈 자동화",
    "midjourney-pod-print-on-demand": "Midjourney로 굿즈·POD 시작하기",
    "replit-agent-vs-bolt": "Replit Agent vs Bolt",
    "ai-translation-content-localization": "AI 번역으로 콘텐츠 다국어화하기",
    "perplexity-vs-chatgpt-search-gemini": "딥 리서치 비교",
    "gamma-vs-tome-vs-beautiful-ai": "Gamma vs Beautiful.ai",
    "claude-discord-slack-bot": "Claude로 디스코드·슬랙 봇 만들기",
    "ai-social-content-calendar": "AI SNS 콘텐츠 캘린더 자동화",
    "descript-video-podcast-editing": "Descript로 영상 편집 자동화",
    "supabase-ai-saas-backend": "Supabase + AI로 SaaS 백엔드 구축",
    "ai-data-analysis-tools-comparison": "AI 데이터 분석 도구 비교",
    "solo-saas-pricing-payments": "1인 SaaS 가격·결제 붙이기",
    "ai-newsletter-automation-system": "AI 뉴스레터 자동화 시스템",
    "ideogram-vs-recraft-text-image": "Ideogram vs Recraft",
    "cline-vs-roo-code": "Cline vs Roo Code",
    "ai-ebook-kmong-talent-market": "AI 전자책 크몽·탈잉 판매",
    "make-ai-automation-recipes": "Make로 AI 자동화 시나리오 10선",
    "ai-voice-cloning-guide": "AI 음성 클로닝 가이드",
    "korean-ai-chatbot-comparison": "한국어 AI 챗봇 고르기 2026",
    "ai-coupang-product-content": "AI로 쿠팡 상세페이지 만들기",
    "claude-code-chrome-extension": "Claude Code로 크롬 확장 만들기",
    "ai-thumbnail-generation-workflow": "AI 썸네일 제작 워크플로우",
    "zapier-ai-actions-guide": "Zapier AI 기능 정리",
    "ai-agent-research-automation": "AI 에이전트로 리서치 자동화",
    "notion-ai-vs-chatgpt-docs": "Notion AI vs ChatGPT",
    "ai-online-course-creation": "AI로 온라인 강의 만들기",
    "obsidian-ai-second-brain": "Obsidian + AI 제2의 뇌",
    "ai-resume-job-tools-comparison": "AI 취업 준비 도구 비교",
    "stable-diffusion-local-guide": "Stable Diffusion 로컬 가이드",
    "ai-subtitle-translation-youtube": "AI 자막·번역·더빙으로 유튜브 다국어 확장",
    "build-rag-chatbot-saas": "RAG 챗봇 SaaS 직접 만들기",
    "ai-prompt-management-tools": "AI 프롬프트 관리 도구 비교",
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
    "turborepo-brand-config":
        "Turborepo brand.config.ts로 사이트 2개 운영하는 법",
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
        subtitle = AG_SUBTITLES.get(p["slug"], "AI 도구 가이드")
        out_dir = base / "aigrit" / "public" / "images" / p["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        img = render_aigrit(title, p["category"], subtitle)
        out = out_dir / "og.png"
        img.save(out, "PNG", optimize=True)
        kb = out.stat().st_size / 1024
        print(f"✓ aigrit/{p['slug']}/og.png  ({kb:.1f}KB)")
        count += 1

    # AIGrit EN — title·subtitle·category use raw frontmatter strings (no overrides)
    # Saved as og-en.png alongside og.png in the same image folder.
    for p in posts.get("aigrit_en", []):
        out_dir = base / "aigrit" / "public" / "images" / p["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        img = render_aigrit(p["title"], p["category"], p["subtitle"], lang="en")
        out = out_dir / "og-en.png"
        img.save(out, "PNG", optimize=True)
        kb = out.stat().st_size / 1024
        print(f"✓ aigrit/{p['slug']}/og-en.png  ({kb:.1f}KB)")
        count += 1

    print(f"\n✅ Generated {count} OG images.")


if __name__ == "__main__":
    main()
