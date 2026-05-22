#!/usr/bin/env python3
"""
Naver 에디션 SNS 자동 생성 — IG 캐러셀 5개 + X 이미지 5장 + 캡션·Threads·X 트윗·메타.

Spec source:
  - docs/SNS_AUTOMATION.md
  - 기존 generate-sns-cards.py 의 render_aigrit_card / render_babipanote_card 재사용

Output (per Naver post):
  ~/dev/sns/aigrit/naver-{NN}-{slug}/
    ├── ig/post-{1..5}/{NN}-{role}.png   # 1080×1080
    ├── x/post-{1..5}.png                # 1600×900
    ├── ig-captions.md
    ├── threads.md
    ├── x.md
    └── _meta.json

Usage:
  python3 scripts/sns/generate-sns-naver-batch.py            # 전체 배치
  python3 scripts/sns/generate-sns-naver-batch.py --only 1   # NAVER_SPECS[0]만
  python3 scripts/sns/generate-sns-naver-batch.py --slug naver-01-apple-shortcuts-50000won

각 Naver 에디션 SPEC 은 NAVER_SPECS 리스트에 push. 각 응답에서 한 편씩 추가.
"""
from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import sys
from pathlib import Path

THIS = Path(__file__).resolve()
SCRIPTS_SNS = THIS.parent
REPO = SCRIPTS_SNS.parent.parent
SNS_ROOT = Path.home() / "dev" / "sns"

# === Reuse renderers from canonical SNS card script ===
_renderer_path = SCRIPTS_SNS / "generate-sns-cards.py"
_spec = importlib.util.spec_from_file_location("sns_renderers", _renderer_path)
_mod = importlib.util.module_from_spec(_spec)
sys.modules["sns_renderers"] = _mod
_spec.loader.exec_module(_mod)
render_aigrit_card = _mod.render_aigrit_card
render_babipanote_card = _mod.render_babipanote_card


# ============================================================
# Spec format (Naver edition)
# ============================================================
# {
#   "naver_no": "01",                           # Naver edition number, zero-padded
#   "slug": "apple-shortcuts-50000won",         # short slug (folder = naver-NN-slug)
#   "log_no": "224263045957",                    # Naver logNo
#   "title": "...",                              # 발행 제목
#   "tone": "aigrit",                            # aigrit (dark) | babipanote (paper)
#   "carousels": [                               # 5 carousels × 5 cards (compatible with render_post)
#     {"label": "Hook", "cards": [...]},
#     ...
#   ],
#   "ig_captions": [                             # 5 main captions (one per carousel)
#     {"label": "Hook", "main": "...", "slides": ["s2", "s3", "s4", "s5"], "tags": ["#tag", ...]}
#   ],
#   "threads": [                                 # 5 단발 Threads
#     {"label": "Hook", "body": "...", "reply": None}
#   ],
#   "tweets": [                                  # 5 단발 X
#     {"label": "Hook", "body": "...", "reply": None}
#   ],
# }


def naver_url(log_no: str) -> str:
    return f"blog.naver.com/aigrit/{log_no}"


def generate_post(spec: dict) -> dict:
    """One Naver edition → all assets (PNG + 4 text files)."""
    folder_name = f"naver-{spec['naver_no']}-{spec['slug']}"
    base = SNS_ROOT / "aigrit" / folder_name
    base.mkdir(parents=True, exist_ok=True)

    renderer = render_aigrit_card if spec["tone"] == "aigrit" else render_babipanote_card

    # --- 1. IG carousel cards (5×5 = 25 PNGs at 1080×1080) ---
    ig_files: list[str] = []
    for pi, carousel in enumerate(spec["carousels"], start=1):
        cdir = base / "ig" / f"post-{pi}"
        cdir.mkdir(parents=True, exist_ok=True)
        for ci, card in enumerate(carousel["cards"], start=1):
            role = card["role"]
            name_role = {"cover": "cover", "cta": "cta"}.get(role, "card")
            fname = f"{ci:02d}-{name_role}.png"
            img = renderer(1080, 1080, role, card["payload"], post_idx=pi)
            out = cdir / fname
            img.save(out, "PNG", optimize=True)
            ig_files.append(f"ig/post-{pi}/{fname}  ({out.stat().st_size / 1024:.1f}KB)")

    # --- 2. X images (5 PNGs at 1600×900) ---
    x_files: list[str] = []
    x_dir = base / "x"
    x_dir.mkdir(parents=True, exist_ok=True)
    for pi, carousel in enumerate(spec["carousels"], start=1):
        x_card = carousel.get("x_card", carousel["cards"][0])
        img = renderer(1600, 900, x_card["role"], x_card["payload"], post_idx=pi)
        out = x_dir / f"post-{pi}.png"
        img.save(out, "PNG", optimize=True)
        x_files.append(f"x/post-{pi}.png  ({out.stat().st_size / 1024:.1f}KB)")

    # --- 3. ig-captions.md ---
    blog_link = naver_url(spec["log_no"])
    captions_md = [f"# {spec['title']} · IG Captions (5 캐러셀)\n"]
    for i, cap in enumerate(spec["ig_captions"], start=1):
        captions_md.append(f"\n## Carousel post-{i} — {cap['label']}\n")
        captions_md.append("\n### Slide 1 (Main / 피드 본문)\n")
        captions_md.append(f"{cap['main']}\n")
        captions_md.append(f"\n→ {blog_link}\n")
        captions_md.append("\n.\n.\n.\n")
        if cap.get("tags"):
            captions_md.append(" ".join(cap["tags"]) + "\n")
        if cap.get("slides"):
            captions_md.append("\n### Slide 2-5 (보조)\n")
            for j, slide in enumerate(cap["slides"], start=2):
                captions_md.append(f"- Slide {j}: {slide}\n")
    (base / "ig-captions.md").write_text("".join(captions_md), encoding="utf-8")

    # --- 4. threads.md ---
    th_md = [f"# {spec['title']} · Threads (5 posts)\n"]
    for i, th in enumerate(spec["threads"], start=1):
        th_md.append(f"\n## Post {i} — {th['label']}\n")
        th_md.append(f"{th['body']}\n")
        if th.get("reply"):
            th_md.append(f"\n(옵션) Reply 1: {th['reply']}\n")
    (base / "threads.md").write_text("".join(th_md), encoding="utf-8")

    # --- 5. x.md ---
    x_md = [f"# {spec['title']} · X (5 tweets)\n"]
    for i, tw in enumerate(spec["tweets"], start=1):
        x_md.append(f"\n## Tweet {i} — {tw['label']}\n")
        x_md.append(f"{tw['body']}\n")
        x_md.append(f"[image: x/post-{i}.png]\n")
        if tw.get("reply"):
            x_md.append(f"\n(옵션) Reply 1: {tw['reply']}\n")
    (base / "x.md").write_text("".join(x_md), encoding="utf-8")

    # --- 6. _meta.json ---
    meta = {
        "brand": "aigrit",
        "platform_root": "naver",
        "naver_no": spec["naver_no"],
        "slug": spec["slug"],
        "folder": folder_name,
        "title": spec["title"],
        "log_no": spec["log_no"],
        "blog_url": f"https://{blog_link}",
        "tone": spec["tone"],
        "ig_carousels": len(spec["carousels"]),
        "ig_cards_total": sum(len(c["cards"]) for c in spec["carousels"]),
        "x_images": len(spec["carousels"]),
        "threads_posts": len(spec["threads"]),
        "x_tweets": len(spec["tweets"]),
        "generated_at": dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds"),
    }
    (base / "_meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    return {"folder": str(base), "ig": ig_files, "x": x_files, "meta": meta}


# ============================================================
# Naver SPECS — 한 응답에서 한 편씩 push
# ============================================================
NAVER_SPECS: list[dict] = [
    # ============================================================
    # Naver #5 — 퇴근 후 2주, Claude Code로 iOS 앱 만든 후기
    # ============================================================
    {
        "naver_no": "05",
        "slug": "ai-ios-app-2weeks",
        "log_no": "224269781667",
        "title": "퇴근 후 2주, Claude Code로 iOS 앱 만든 후기",
        "tone": "aigrit",
        "carousels": [
            # ----- post-1: Hook -----
            {
                "label": "Hook",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "Naver #05",
                        "title": "퇴근 후 2주",
                        "hook": "Claude Code로 iOS 앱 출시 / 45h · $28",
                    }},
                    {"role": "context", "payload": {
                        "badge": "한 줄 결론",
                        "heading": "Flutter 한 줄 안 짜본 직장인의 후기",
                        "bullets": [
                            "평일 저녁 9시 · 노트북 + Claude Code",
                            "3일 연속 build #6 같은 일상",
                            "App Store에 본인 명의로 출시 완료 (GentleDo)",
                            "비결은 도구 1개 — Claude Code",
                        ],
                    }},
                    {"role": "finding", "payload": {
                        "badge": "총 투입",
                        "heading": "출시까지의 비용",
                        "metrics": [
                            {"tool": "시간", "value": "45h", "note": "평일 야간 2h × 10일 + 주말 5h × 2", "winner": True},
                            {"tool": "비용", "value": "$28/월", "note": "Claude Max $20 + Apple Dev $99/년", "winner": True},
                        ],
                        "caption": "Flutter 외주 견적은 최소 300만원부터 — 75배 차이.",
                    }},
                    {"role": "list", "payload": {
                        "badge": "오늘 다룰 것",
                        "heading": "솔직 후기 5장",
                        "items": [
                            {"primary": "기술 스택 — 비개발자 현실 조합"},
                            {"primary": "비용 정산 — 월 $28의 정체"},
                            {"primary": "사람 vs AI 역할 분담"},
                            {"primary": "AI로 안 됐던 3가지"},
                            {"primary": "추천 매트릭스 — 누구에게 권하나"},
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "지금 읽기",
                        "heading": "전체 후기 + 매트릭스",
                        "bullets": [
                            "build 2 → build 8 타임라인",
                            "사람·AI 역할 분담 표",
                            "권장·비권장 조건",
                        ],
                        "url": "blog.naver.com/aigrit/224269781667",
                    }},
                ],
            },
            # ----- post-2: 기술 스택 -----
            {
                "label": "Stack",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "기술 스택",
                        "title": "Flutter + Claude Code",
                        "hook": "비개발자에게 가장 현실적인 조합",
                    }},
                    {"role": "list", "payload": {
                        "badge": "선택한 4가지",
                        "heading": "스택 구성",
                        "items": [
                            {"primary": "언어 / FW", "sub": "Flutter + Dart (정적 타입 → AI 페어 실수 적음)"},
                            {"primary": "상태관리", "sub": "Riverpod (Provider 패턴 표준)"},
                            {"primary": "로컬 DB", "sub": "Drift (SQLite 래퍼, 마이그레이션 안전)"},
                            {"primary": "AI 페어", "sub": "Claude Code Max 구독"},
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "왜 Flutter인가",
                        "heading": "한 코드베이스 = 3 플랫폼",
                        "bullets": [
                            "iOS · Android · macOS 동일 코드",
                            "Dart 정적 타입 = AI 작성 코드 검증 빠름",
                            "Hot reload — 디자인 반복 시간 ↓",
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "왜 로컬 전용인가",
                        "heading": "MVP 범위 설계",
                        "bullets": [
                            "서버·인증·결제 = 난이도 급상승",
                            "로컬 저장 = 완성까지 거리 최단",
                            "‘작게, 확실하게’ — 첫 앱의 핵심",
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "스택 결정 가이드",
                        "heading": "본인 환경에 적용",
                        "bullets": [
                            "Flutter 외 Swift·React Native 비교",
                            "MVP 범위 설계 패턴",
                            "AI 친화 정적 타입 언어 선택",
                        ],
                        "url": "blog.naver.com/aigrit/224269781667",
                    }},
                ],
            },
            # ----- post-3: 사람 vs AI 역할 -----
            {
                "label": "Roles",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "역할 분담",
                        "title": "사람 vs AI",
                        "hook": "AI가 다 해 준 게 아니다",
                    }},
                    {"role": "list", "payload": {
                        "badge": "사람의 영역",
                        "heading": "내가 한 일",
                        "items": [
                            {"primary": "프로젝트 컨텍스트 문서화", "sub": "CLAUDE.md 규칙집 — 4줄 규칙이 핵심"},
                            {"primary": "실기기 테스트 + 디자인 + 카피"},
                            {"primary": "‘지금은 하지 마세요’ 리스트 유지"},
                            {"primary": "가설 정의 · 검증 지표 설정"},
                        ],
                    }},
                    {"role": "list", "payload": {
                        "badge": "AI의 영역",
                        "heading": "Claude Code가 한 일",
                        "items": [
                            {"primary": "Dart 코드 실제 작성"},
                            {"primary": "Drift DB 스키마 · 마이그레이션"},
                            {"primary": "Riverpod 상태관리 설계"},
                            {"primary": "반복 태스크 · 테스트 · 리팩토링"},
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "비결",
                        "heading": "CLAUDE.md 규칙 문서",
                        "bullets": [
                            "‘Red 컬러 금지’ · ‘다국어 파일 경유 필수’",
                            "4줄 규칙이 수백 번의 ‘그거 말고’ 절약",
                            "프로젝트 컨벤션 = 1차 시간 회수 도구",
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "분담표 본문",
                        "heading": "역할 매트릭스 + 예시",
                        "bullets": [
                            "CLAUDE.md 실제 4줄 규칙 공개",
                            "AI에 못 맡기는 결정 카테고리",
                            "검증 지표 설계법",
                        ],
                        "url": "blog.naver.com/aigrit/224269781667",
                    }},
                ],
            },
            # ----- post-4: AI 한계 3가지 + 타임라인 -----
            {
                "label": "Limits",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "솔직 한계",
                        "title": "AI로 안 됐던 3",
                        "hook": "바이브 코딩 한계도 알고 시작",
                    }},
                    {"role": "context", "payload": {
                        "badge": "한계 ①",
                        "heading": "실기기 디버깅",
                        "bullets": [
                            "시뮬레이터 OK · 실기기 크래시",
                            "Claude에 로그 줘도 원인 X",
                            "결국 GitHub 이슈 트래커 직접 검색",
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "한계 ②",
                        "heading": "Xcode 체크박스 한 칸",
                        "bullets": [
                            "TestFlight 암호화 선언",
                            "iPad 타깃 제거 · provisioning profile",
                            "여기서 하루 날림 — Xcode UI는 AI가 못 봄",
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "한계 ③",
                        "heading": "디자인 감각",
                        "bullets": [
                            "‘이 카드가 무거워 보인다’ 텍스트로 못 옮김",
                            "Figma에서 직접 조정",
                            "색·간격 값만 AI에 옮기는 흐름이 빠름",
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "한계 인지 후",
                        "heading": "어떻게 우회했나",
                        "bullets": [
                            "실기기 크래시 디버깅 패턴",
                            "Xcode 체크박스 체크리스트",
                            "Figma → AI 핸드오프 흐름",
                        ],
                        "url": "blog.naver.com/aigrit/224269781667",
                    }},
                ],
            },
            # ----- post-5: 추천 매트릭스 + CTA -----
            {
                "label": "Matrix-CTA",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "추천 매트릭스",
                        "title": "누구에게 권하나",
                        "hook": "권장 4 · 비권장 3 · 도구 시작 순서",
                    }},
                    {"role": "list", "payload": {
                        "badge": "권장 조건",
                        "heading": "이런 분께 추천",
                        "items": [
                            {"primary": "월 4만원 구독비 감당 가능"},
                            {"primary": "주 10~15시간 투입 가능"},
                            {"primary": "기술 용어 20개 정도 읽을 수 있음"},
                            {"primary": "로컬 전용 단순 MVP 범위"},
                        ],
                    }},
                    {"role": "list", "payload": {
                        "badge": "비권장",
                        "heading": "다른 길이 빠른 분",
                        "items": [
                            {"primary": "서버·인증·결제 핵심 앱", "sub": "난이도 급상승 · 외주 검토"},
                            {"primary": "기술 문서 자체가 어려움", "sub": "기초 학습 먼저"},
                            {"primary": "‘그냥 만들어 보고 싶다’", "sub": "아이디어 검증부터"},
                        ],
                    }},
                    {"role": "list", "payload": {
                        "badge": "도구 시작 순서",
                        "heading": "처음 쓰는 분께",
                        "items": [
                            {"primary": "1) 무료 ChatGPT", "sub": "개념 질문 · 디버깅 시작점"},
                            {"primary": "2) Claude Code Max $20", "sub": "본격 개발 시작 · 가성비 최강"},
                            {"primary": "3) Cursor Pro $20 (옵션)", "sub": "IDE 안에서 작업하고 싶으면"},
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "이웃추가",
                        "heading": "다음 편 — 심사 2일 통과기",
                        "bullets": [
                            "App Store 심사 2일 후기 (금요일)",
                            "공감 ♡ + 댓글 = 다음 편 동력",
                            "어떤 앱 만들고 싶은지 댓글로",
                        ],
                        "url": "blog.naver.com/aigrit/224269781667",
                    }},
                ],
            },
        ],
        "ig_captions": [
            {
                "label": "Hook",
                "main": (
                    "Flutter 한 줄 안 짜본 직장인이 퇴근 후 2주 만에 iOS 앱을 출시했습니다.\n\n"
                    "총 45시간 + 월 $28 (Claude Code Max + Apple Developer). "
                    "Flutter 외주 견적 최소 300만원과 비교하면 75배 차이. 솔직히 ‘혼자서는 못 만들었을 앱’이 만들어졌어요. "
                    "단 AI가 다 해 준 게 아닙니다 — 사람·AI 역할 분담이 핵심."
                ),
                "slides": [
                    "한 줄 결론 — 비개발자 직장인이 출시까지",
                    "총 투입 — 45h · $28/월",
                    "오늘 다룰 5가지",
                    "본문 — 매트릭스·타임라인",
                ],
                "tags": [
                    "#1인개발", "#바이브코딩", "#ClaudeCode", "#비개발자", "#AI코딩",
                    "#Flutter", "#iOS앱개발", "#GentleDo", "#사이드프로젝트", "#앱출시",
                    "#1인부업", "#사이드잡", "#디지털노마드", "#네이버블로그", "#aigrit",
                    "#개발기", "#빌더저널", "#개발일지", "#Apple", "#앱스토어",
                    "#원격근무", "#스타트업", "#AppStore",
                ],
            },
            {
                "label": "Stack",
                "main": (
                    "기술 스택 — 비개발자에게 가장 현실적인 조합.\n\n"
                    "Flutter + Dart(정적 타입), Riverpod, Drift(SQLite 래퍼), Claude Code Max. "
                    "iOS·Android·macOS 한 코드베이스가 핵심. "
                    "MVP 범위는 로컬 전용으로 — 서버·인증·결제 들어가면 난이도가 급상승합니다."
                ),
                "slides": [
                    "스택 4가지 — Flutter / Riverpod / Drift / Claude",
                    "Flutter 선택 이유 — 한 코드베이스 3 플랫폼",
                    "MVP 로컬 전용 — 서버 X로 거리 최단",
                    "본문에 스택 결정 가이드",
                ],
                "tags": [
                    "#Flutter", "#Dart", "#Riverpod", "#Drift", "#SQLite",
                    "#ClaudeCode", "#1인개발", "#앱스택", "#GentleDo", "#비개발자",
                    "#사이드프로젝트", "#빌더저널", "#개발기", "#네이버블로그", "#aigrit",
                    "#1인부업", "#사이드잡", "#디지털노마드", "#앱개발", "#개발일지",
                ],
            },
            {
                "label": "Roles",
                "main": (
                    "AI가 다 해 준 게 아닙니다. 사람 vs AI 역할이 분명해요.\n\n"
                    "사람: CLAUDE.md 규칙집·실기기 테스트·디자인·카피. "
                    "AI: Dart 코드 실제 작성·Drift 마이그레이션·Riverpod 설계·테스트. "
                    "비결은 4줄 규칙으로 ‘그거 말고’ 수백 번을 절약하는 것."
                ),
                "slides": [
                    "사람의 영역 — CLAUDE.md / 실기기 / 디자인",
                    "AI의 영역 — Dart / DB / 상태관리 / 테스트",
                    "비결 — 4줄 규칙 컨벤션",
                    "본문에 분담 매트릭스 + 예시",
                ],
                "tags": [
                    "#1인개발", "#바이브코딩", "#ClaudeCode", "#AI코딩", "#CLAUDEmd",
                    "#프로젝트관리", "#개발컨벤션", "#GentleDo", "#사이드프로젝트", "#빌더저널",
                    "#네이버블로그", "#aigrit", "#개발기", "#1인부업", "#사이드잡",
                    "#디지털노마드", "#앱개발", "#비개발자", "#개발일지", "#Riverpod",
                ],
            },
            {
                "label": "Limits",
                "main": (
                    "솔직히 AI로 안 됐던 3가지.\n\n"
                    "① 실기기 크래시 — 로그 줘도 원인 못 찾음, GitHub 이슈 직접 검색.\n"
                    "② Xcode 체크박스 — TestFlight·iPad·provisioning, AI가 UI를 못 봄, 하루 날림.\n"
                    "③ 디자인 감각 — Figma 직접 조정 후 색·간격만 AI에 핸드오프."
                ),
                "slides": [
                    "한계 ① 실기기 디버깅",
                    "한계 ② Xcode UI 체크박스",
                    "한계 ③ 디자인 감각 → Figma",
                    "어떻게 우회했나는 본문",
                ],
                "tags": [
                    "#1인개발", "#바이브코딩", "#AI한계", "#실기기디버깅", "#Xcode",
                    "#TestFlight", "#Figma", "#GentleDo", "#ClaudeCode", "#사이드프로젝트",
                    "#빌더저널", "#개발기", "#네이버블로그", "#aigrit", "#1인부업",
                    "#사이드잡", "#디지털노마드", "#앱개발", "#개발일지", "#솔직리뷰",
                ],
            },
            {
                "label": "Matrix-CTA",
                "main": (
                    "추천 매트릭스 — 누구에게 권하나.\n\n"
                    "권장: 월 4만원 구독 / 주 10~15시간 / 기술 용어 20개 / 로컬 MVP 범위. "
                    "비권장: 서버·인증·결제 핵심 / 기술 문서 어려움 / 아이디어 미정. "
                    "도구 순서는 무료 ChatGPT → Claude Code Max → (옵션) Cursor."
                ),
                "slides": [
                    "권장 조건 4",
                    "비권장 3 — 다른 길이 빠른 경우",
                    "도구 시작 순서 3단계",
                    "다음 편 — 심사 2일 통과기",
                ],
                "tags": [
                    "#1인개발", "#바이브코딩", "#ClaudeCode", "#앱개발", "#GentleDo",
                    "#사이드프로젝트", "#빌더저널", "#네이버블로그", "#aigrit", "#aigrit이웃추가",
                    "#예고편", "#앱스토어심사", "#앱출시후기", "#1인부업", "#사이드잡",
                    "#디지털노마드", "#개발일지", "#개발기", "#비개발자", "#AppStore",
                ],
            },
        ],
        "threads": [
            {
                "label": "Hook",
                "body": (
                    "Flutter 한 줄 안 짜본 직장인이 퇴근 후 2주 만에 iOS 앱을 출시했습니다.\n\n"
                    "총 45시간 + 월 $28 (Claude Max + Apple Dev). 외주 견적 최소 300만원과 75배 차이.\n"
                    "단 AI가 다 해 준 게 아닙니다 — 사람·AI 역할 분담이 핵심.\n\n"
                    "→ blog.naver.com/aigrit/224269781667"
                ),
            },
            {
                "label": "Stack",
                "body": (
                    "스택 — Flutter + Dart + Riverpod + Drift + Claude Code Max.\n\n"
                    "한 코드베이스로 iOS·Android·macOS, Dart 정적 타입이 AI 페어에 유리.\n"
                    "MVP는 로컬 전용 — 서버·인증·결제 들어가면 난이도 급상승.\n\n"
                    "→ blog.naver.com/aigrit/224269781667"
                ),
            },
            {
                "label": "Roles",
                "body": (
                    "사람 vs AI 역할.\n\n"
                    "사람: CLAUDE.md 규칙·실기기·디자인·카피.\n"
                    "AI: 코드 작성·DB 마이그·상태관리·테스트.\n"
                    "비결은 4줄 규칙 컨벤션 — 수백 번의 ‘그거 말고’를 절약.\n\n"
                    "→ blog.naver.com/aigrit/224269781667"
                ),
            },
            {
                "label": "Limits",
                "body": (
                    "솔직 한계 3.\n\n"
                    "① 실기기 크래시 — 로그 줘도 원인 X.\n"
                    "② Xcode UI 체크박스 — AI가 못 봄, 하루 날림.\n"
                    "③ 디자인 감각 — Figma 직접 조정.\n\n"
                    "→ blog.naver.com/aigrit/224269781667"
                ),
            },
            {
                "label": "Matrix-CTA",
                "body": (
                    "추천 매트릭스.\n\n"
                    "권장: 4만원 / 주 10~15h / 기술 용어 OK / 로컬 MVP.\n"
                    "비권장: 서버·인증·결제 핵심 앱.\n"
                    "도구 순서: 무료 GPT → Claude Code Max → (옵션) Cursor.\n\n"
                    "→ blog.naver.com/aigrit/224269781667"
                ),
            },
        ],
        "tweets": [
            {
                "label": "Hook",
                "body": (
                    "Flutter 안 짜본 직장인이 퇴근 후 2주에 iOS 앱 출시.\n"
                    "45h · 월 $28. 외주 견적 300만원의 75배 절감.\n"
                    "단 AI가 다 한 건 아니다 — 사람·AI 분담.\n"
                    "→ blog.naver.com/aigrit/224269781667"
                ),
            },
            {
                "label": "Stack",
                "body": (
                    "스택 — Flutter + Dart + Riverpod + Drift + Claude Code Max.\n"
                    "한 코드베이스 = iOS·Android·macOS.\n"
                    "MVP 로컬 전용으로 거리 최단.\n"
                    "→ blog.naver.com/aigrit/224269781667"
                ),
            },
            {
                "label": "Roles",
                "body": (
                    "사람 vs AI.\n"
                    "사람: CLAUDE.md / 실기기 / 디자인 / 카피.\n"
                    "AI: 코드 / DB / 상태관리 / 테스트.\n"
                    "4줄 규칙 컨벤션이 가장 큰 시간 회수.\n"
                    "→ blog.naver.com/aigrit/224269781667"
                ),
            },
            {
                "label": "Limits",
                "body": (
                    "AI로 안 된 3.\n"
                    "① 실기기 크래시 (로그 줘도 못 찾음).\n"
                    "② Xcode UI 체크박스 (하루 날림).\n"
                    "③ 디자인 감각 (Figma 직접).\n"
                    "→ blog.naver.com/aigrit/224269781667"
                ),
            },
            {
                "label": "Matrix-CTA",
                "body": (
                    "추천 매트릭스.\n"
                    "권장 — 4만원/주 10~15h/로컬 MVP.\n"
                    "비권장 — 서버·결제 핵심 앱.\n"
                    "도구 — 무료 GPT → Claude Code Max.\n"
                    "다음 편 심사 2일 통과기.\n"
                    "→ blog.naver.com/aigrit/224269781667"
                ),
            },
        ],
    },
    # ============================================================
    # Naver #4 — GentleDo 네이밍 실패담 (Keelry → GentleDo)
    # ============================================================
    {
        "naver_no": "04",
        "slug": "app-naming-failure",
        "log_no": "224268598962",
        "title": "앱 이름 한 번 갈아엎은 이야기 | GentleDo 네이밍 스토리",
        "tone": "aigrit",
        "carousels": [
            # ----- post-1: Hook -----
            {
                "label": "Hook",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "Naver #04",
                        "title": "Keelry → GentleDo",
                        "hook": "3개월 키운 앱 이름을 버린 날",
                    }},
                    {"role": "context", "payload": {
                        "badge": "그날의 한 줄",
                        "heading": "테스터 5명이 똑같이 물었다",
                        "bullets": [
                            "‘Keelry가 뭐에요? 발음이 어려워요’",
                            "5명 전부 같은 첫 질문",
                            "그날 저녁 이름을 버리기로 결정",
                            "3주 후 GentleDo로 App Store 출시",
                        ],
                    }},
                    {"role": "finding", "payload": {
                        "badge": "교체 비용",
                        "heading": "리네임은 빠를수록 싸다",
                        "metrics": [
                            {"tool": "3개월 시점", "value": "반나절", "note": "DB 마이그레이션 + 코드 리네임", "winner": True},
                            {"tool": "6개월 후 가정", "value": "1주+", "note": "코드·DB·스토어·도메인·SNS 전부"},
                        ],
                        "caption": "출시 전에 바꾸는 게 어떤 경우든 가장 쌉니다.",
                    }},
                    {"role": "list", "payload": {
                        "badge": "오늘 다룰 것",
                        "heading": "3개월짜리 실패에서 남긴 것",
                        "items": [
                            {"primary": "왜 Keelry가 멋있어 보였나"},
                            {"primary": "테스터 피드백 — ‘무슨 뜻?’ 이 시그널"},
                            {"primary": "결정타 — 3개 앱 시리즈 일관성"},
                            {"primary": "리네임 당일 커밋 3개"},
                            {"primary": "1인 개발자 네이밍 체크리스트 5"},
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "지금 읽기",
                        "heading": "전체 후기 + 체크리스트",
                        "bullets": [
                            "테스터 피드백 원문 + 첫 5초 룰",
                            "리네임 커밋 3개 (DB · 번들명 · 코드)",
                            "출시 전 네이밍 체크리스트 5",
                        ],
                        "url": "blog.naver.com/aigrit/224268598962",
                    }},
                ],
            },
            # ----- post-2: 왜 실패했나 (Keelry 분석) -----
            {
                "label": "Why-Failed",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "왜 실패했나",
                        "title": "Keel + ry",
                        "hook": "내가 좋아한 거였지 사용자가 좋아한 게 아니었다",
                    }},
                    {"role": "list", "payload": {
                        "badge": "콘셉트는 깔끔",
                        "heading": "항해 용어로 통일했다",
                        "items": [
                            {"primary": "컨디션 체크 → Wind Check"},
                            {"primary": "집중 모드 → Helm Mode"},
                            {"primary": "미루기 → Tack Log"},
                            {"primary": "새 출발 → New Bearing"},
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "테스터 첫 질문",
                        "heading": "5명이 같은 반응",
                        "bullets": [
                            "‘Keelry가 무슨 뜻이에요?’",
                            "‘발음 어떻게 해요? 킬리? 켈리?’",
                            "‘아이콘만 봐서는 뭐 하는 앱인지 모르겠어요’",
                            "공통점 — 첫 5초에 기능 전달 실패",
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "치명적 ASO",
                        "heading": "App Store 검색에서 보이지 않음",
                        "bullets": [
                            "‘할 일 관리’ 검색 → 절대 등장 X",
                            "Keelry에 ‘할 일’ 단어 0",
                            "출발부터 진 싸움이었음",
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "전문 분석",
                        "heading": "왜 ‘좋은 콘셉트’가 망했나",
                        "bullets": [
                            "콘셉트 일관성 ≠ 사용자 인지",
                            "ASO 관점의 첫 단어 룰",
                            "테스터 5명이 시그널이 된 이유",
                        ],
                        "url": "blog.naver.com/aigrit/224268598962",
                    }},
                ],
            },
            # ----- post-3: 결정타 — 3앱 시리즈 -----
            {
                "label": "Series",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "결정타",
                        "title": "3개 앱 시리즈",
                        "hook": "Keelry · GentleFast · GentleStudy = 시너지 0",
                    }},
                    {"role": "context", "payload": {
                        "badge": "공유 철학",
                        "heading": "세 앱이 같은 무드를 공유한다",
                        "bullets": [
                            "‘No Red’ — 빨강 알림 배제",
                            "모멘텀 시스템 — 점수 누적 구조",
                            "에너지 체크인 — 컨디션 기반 필터",
                        ],
                    }},
                    {"role": "list", "payload": {
                        "badge": "Before · After",
                        "heading": "이름 통일 전후",
                        "items": [
                            {"primary": "Before — 뒤죽박죽", "sub": "Keelry · GentleFast · GentleStudy / 같은 시리즈로 인식 X"},
                            {"primary": "After — Gentle 시리즈", "sub": "GentleDo · GentleFast · GentleStudy / 한 줄로 정렬"},
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "교훈",
                        "heading": "브랜드 일관성 = 시너지의 기본",
                        "bullets": [
                            "이름 다르면 같은 디자인도 별개로 보임",
                            "검색·SNS 해시태그·스토어 카테고리 분산",
                            "1인 개발은 통일이 곧 마케팅 비용 절감",
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "시리즈 인식",
                        "heading": "‘하나의 무드’ 만드는 법",
                        "bullets": [
                            "공통 접두사 + 카테고리 동사",
                            "디자인 토큰 공유 (컬러·폰트)",
                            "스토어 부제목 동일 패턴",
                        ],
                        "url": "blog.naver.com/aigrit/224268598962",
                    }},
                ],
            },
            # ----- post-4: 리네임 당일 -----
            {
                "label": "Rename-Day",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "그날 커밋",
                        "title": "2026-04-11",
                        "hook": "커밋 3개 + 반나절 검증",
                    }},
                    {"role": "list", "payload": {
                        "badge": "남은 로그",
                        "heading": "3개의 커밋",
                        "items": [
                            {"primary": "d5923f2", "sub": "앱 내부 이름 Keelry → GentleDo 전면 변경"},
                            {"primary": "7390a15", "sub": "keelryScore → momentumScore DB 컬럼 리네임"},
                            {"primary": "76440c2", "sub": "macOS 앱 번들명 keelry.app → GentleDo.app"},
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "가장 아팠던",
                        "heading": "DB 컬럼 리네임",
                        "bullets": [
                            "베타 테스터 기기에 이미 데이터 쌓임",
                            "마이그레이션 스크립트 작성",
                            "실기기 검증까지 반나절 소요",
                            "오류 1건 = 베타 신뢰도 직격",
                        ],
                    }},
                    {"role": "finding", "payload": {
                        "badge": "결과",
                        "heading": "테스터 반응 변화",
                        "metrics": [
                            {"tool": "Before", "value": "??", "note": "‘무슨 뜻이에요?’"},
                            {"tool": "After", "value": "✓", "note": "‘아 그 태스크 관리 앱!’", "winner": True},
                        ],
                        "caption": "이름이 바뀐 직후 첫 5초 인지 성공.",
                    }},
                    {"role": "cta", "payload": {
                        "badge": "이전 가이드",
                        "heading": "커밋·DB 검증 디테일",
                        "bullets": [
                            "마이그레이션 스크립트 패턴",
                            "실기기 검증 체크리스트",
                            "다국가 스토어 메타 동기화",
                        ],
                        "url": "blog.naver.com/aigrit/224268598962",
                    }},
                ],
            },
            # ----- post-5: 체크리스트 + CTA -----
            {
                "label": "Checklist",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "출시 전 체크",
                        "title": "네이밍 체크리스트 5",
                        "hook": "3개 이상 No면 다시 지으세요",
                    }},
                    {"role": "list", "payload": {
                        "badge": "5가지 질문",
                        "heading": "출시 전 자가 진단",
                        "items": [
                            {"primary": "발음이 즉시 되는가?", "sub": "듣자마자 받아 적을 수 있는가"},
                            {"primary": "의미가 3초 안에 전달?", "sub": "첫 5초 룰"},
                            {"primary": "검색어 단어가 포함?", "sub": "ASO 관점"},
                            {"primary": "확장 가능한가?", "sub": "시리즈·해외·카테고리"},
                            {"primary": "도메인·SNS 확보 가능?", "sub": "선점 여부 즉시 검증"},
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "교훈 3",
                        "heading": "3개월짜리에서 남은 것",
                        "bullets": [
                            "① 브랜드 이름은 1차 문서다",
                            "② 리네임은 빠를수록 싸다",
                            "③ ‘무슨 뜻이에요?’ 1명이라도 = 시그널",
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "GentleDo",
                        "heading": "App Store에 올라온 그 앱",
                        "bullets": [
                            "에너지에 맞춰 할 일을 보여주는 생산성 앱",
                            "iOS 전용 · 무료 · 광고 없음",
                            "‘GentleDo’ 검색 또는 본문 링크",
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "이웃추가",
                        "heading": "다음 편 — AI로 2주 만에 출시",
                        "bullets": [
                            "비개발자가 Claude Code로 iOS 앱",
                            "공감 ♡ + 댓글 = 다음 편 동력",
                            "비슷한 경험 댓글로 공유",
                        ],
                        "url": "blog.naver.com/aigrit/224268598962",
                    }},
                ],
            },
        ],
        "ig_captions": [
            {
                "label": "Hook",
                "main": (
                    "‘Keelry가 뭐에요? 발음이 어려워요.’\n"
                    "테스터 5명이 똑같이 물은 그 한 마디에, 3개월 키운 앱 이름을 버리기로 결정했어요.\n\n"
                    "그 후 3주 만에 GentleDo로 App Store 출시. "
                    "리네임 비용은 반나절 — 6개월 후 바꿨다면 1주+. 출시 전에 바꾸는 게 어떤 경우든 가장 쌉니다."
                ),
                "slides": [
                    "그날의 한 줄 — 5명이 같은 첫 질문",
                    "교체 비용 — 반나절 vs 1주+",
                    "오늘 다룰 5가지",
                    "체크리스트는 본문 마지막",
                ],
                "tags": [
                    "#1인개발", "#1인개발자", "#앱개발", "#네이밍", "#브랜딩",
                    "#GentleDo", "#앱스토어", "#AppStore", "#아이폰앱", "#사이드프로젝트",
                    "#1인부업", "#사이드잡", "#디지털노마드", "#네이버블로그", "#aigrit",
                    "#태스크관리", "#생산성앱", "#개발기", "#빌더저널", "#리네임",
                    "#실패담", "#개발일지", "#스타트업",
                ],
            },
            {
                "label": "Why-Failed",
                "main": (
                    "Keelry는 콘셉트가 깔끔했어요. Keel(용골) + ry. 항해 용어로 통일.\n\n"
                    "근데 테스터 5명이 똑같이 ‘무슨 뜻이에요?’부터 물었습니다. "
                    "App Store에서 ‘할 일 관리’ 검색해도 안 나옴(ASO 0). "
                    "내가 좋아한 거였지 사용자가 좋아한 게 아니었어요."
                ),
                "slides": [
                    "콘셉트 정렬 — Wind Check / Helm / Tack",
                    "테스터 5명 같은 첫 질문",
                    "ASO 0 — 검색에 ‘할 일’ 없음",
                    "교훈 — 첫 5초 룰",
                ],
                "tags": [
                    "#1인개발", "#앱네이밍", "#브랜딩실패", "#ASO", "#앱스토어최적화",
                    "#사이드프로젝트", "#빌더저널", "#GentleDo", "#생산성앱", "#태스크관리",
                    "#1인부업", "#사이드잡", "#네이버블로그", "#aigrit", "#개발기",
                    "#앱출시", "#스타트업", "#앱스토어", "#디지털노마드", "#개발일지",
                ],
            },
            {
                "label": "Series",
                "main": (
                    "결정타는 3개 앱 시리즈 계획이었어요.\n\n"
                    "GentleFast(단식)·GentleStudy(학습)을 같이 만들고 있는데, "
                    "이름이 Keelry·GentleFast·GentleStudy로 뒤죽박죽이면 같은 시리즈로 인식 자체가 안 됩니다. "
                    "디자인 철학(No Red·모멘텀·에너지)은 공유하는데 이름이 어긋나면 시너지 0."
                ),
                "slides": [
                    "공유 철학 — No Red / 모멘텀 / 에너지",
                    "Before — 뒤죽박죽 / 시너지 0",
                    "After — Gentle 시리즈로 정렬",
                    "이름 통일이 1인 개발 마케팅 비용 절감",
                ],
                "tags": [
                    "#1인개발", "#앱시리즈", "#브랜딩", "#GentleDo", "#GentleFast",
                    "#GentleStudy", "#사이드프로젝트", "#디자인시스템", "#디자인토큰", "#빌더저널",
                    "#네이버블로그", "#aigrit", "#앱개발", "#개발기", "#디지털노마드",
                    "#사이드잡", "#1인부업", "#스타트업", "#개발일지", "#앱스토어",
                ],
            },
            {
                "label": "Rename-Day",
                "main": (
                    "리네임 당일(2026-04-11) 남은 커밋 3개와 반나절 검증.\n\n"
                    "가장 아팠던 건 DB 컬럼 리네임. 베타 테스터 기기에 데이터가 이미 쌓여있어서 "
                    "마이그레이션 스크립트 + 실기기 검증으로 반나절 소요. "
                    "이름 바꾼 직후 테스터 반응이 ‘아 그 태스크 관리 앱!’으로 바로 변했어요."
                ),
                "slides": [
                    "커밋 3개 — 코드 / DB / 번들명",
                    "DB 마이그레이션이 가장 아팠다",
                    "Before ?? → After 즉시 인지",
                    "마이그레이션 패턴은 본문",
                ],
                "tags": [
                    "#1인개발", "#리네임", "#DB마이그레이션", "#git", "#커밋",
                    "#GentleDo", "#앱개발", "#사이드프로젝트", "#빌더저널", "#개발기",
                    "#네이버블로그", "#aigrit", "#앱출시", "#디지털노마드", "#사이드잡",
                    "#1인부업", "#개발일지", "#앱스토어", "#스타트업", "#테스트플라이트",
                ],
            },
            {
                "label": "Checklist",
                "main": (
                    "출시 전 네이밍 체크리스트 5.\n\n"
                    "① 발음 즉시 ② 의미 3초 ③ 검색어 단어 ④ 확장성 ⑤ 도메인·SNS 확보. "
                    "5개 중 3개 이상 No면 다시 지으세요. 출시 전에. "
                    "다음 편은 비개발자가 AI로 2주 만에 iOS 앱 만든 후기입니다."
                ),
                "slides": [
                    "체크리스트 5 — 발음/의미/검색/확장/도메인",
                    "교훈 3 — 1차 문서 / 빠를수록 싸다 / 시그널",
                    "GentleDo App Store 출시 완료",
                    "다음 편 — 2주 만에 출시 후기",
                ],
                "tags": [
                    "#1인개발", "#앱네이밍", "#네이밍체크리스트", "#브랜딩", "#GentleDo",
                    "#사이드프로젝트", "#빌더저널", "#개발기", "#네이버블로그", "#aigrit",
                    "#aigrit이웃추가", "#예고편", "#바이브코딩", "#ClaudeCode", "#앱개발",
                    "#1인부업", "#사이드잡", "#디지털노마드", "#개발일지", "#앱스토어",
                ],
            },
        ],
        "threads": [
            {
                "label": "Hook",
                "body": (
                    "‘Keelry가 뭐에요? 발음이 어려워요.’\n"
                    "테스터 5명이 똑같이 물어서 그날 저녁 3개월 키운 앱 이름을 버렸어요.\n\n"
                    "3주 후 GentleDo로 App Store 출시. 리네임 비용은 반나절. "
                    "6개월 후 바꿨다면 1주+ — 출시 전에 바꾸는 게 가장 싸다.\n\n"
                    "→ blog.naver.com/aigrit/224268598962"
                ),
            },
            {
                "label": "Why-Failed",
                "body": (
                    "왜 Keelry가 실패했나.\n\n"
                    "콘셉트는 깔끔(Keel + ry, 항해 용어 통일).\n"
                    "근데 테스터 5명 모두 ‘무슨 뜻?’부터.\n"
                    "App Store ‘할 일 관리’ 검색에 절대 등장 X (ASO 0).\n"
                    "내가 좋아한 거였지 사용자가 좋아한 게 아니었다.\n\n"
                    "→ blog.naver.com/aigrit/224268598962"
                ),
            },
            {
                "label": "Series",
                "body": (
                    "결정타는 3앱 시리즈.\n\n"
                    "GentleFast·GentleStudy 같이 개발 중인데 이름이 Keelry로 시작하면 같은 시리즈 인식 X.\n"
                    "디자인 철학(No Red·모멘텀·에너지) 공유해도 이름 어긋나면 시너지 0.\n"
                    "이름 통일 = 1인 개발 마케팅 비용 절감.\n\n"
                    "→ blog.naver.com/aigrit/224268598962"
                ),
            },
            {
                "label": "Rename-Day",
                "body": (
                    "리네임 당일 2026-04-11 — 커밋 3개.\n\n"
                    "코드 전면 리네임 / DB 컬럼 리네임 / macOS 번들명.\n"
                    "DB가 가장 아팠다. 베타 테스터 기기 데이터 쌓여있어서 마이그레이션 + 실기기 검증 반나절.\n"
                    "직후 테스터 반응 ‘아 그 태스크 관리 앱!’.\n\n"
                    "→ blog.naver.com/aigrit/224268598962"
                ),
            },
            {
                "label": "Checklist",
                "body": (
                    "출시 전 네이밍 체크리스트 5.\n\n"
                    "① 발음 즉시 ② 의미 3초 ③ 검색어 단어 ④ 확장성 ⑤ 도메인·SNS.\n"
                    "5개 중 3개 No면 다시. 출시 전에.\n"
                    "GentleDo는 App Store에 올라왔습니다.\n\n"
                    "→ blog.naver.com/aigrit/224268598962"
                ),
            },
        ],
        "tweets": [
            {
                "label": "Hook",
                "body": (
                    "테스터 5명이 똑같이 물었다.\n"
                    "‘Keelry가 뭐에요? 발음 어려워요.’\n"
                    "그날 저녁 3개월 키운 이름을 버리기로.\n"
                    "3주 후 GentleDo로 App Store 출시.\n"
                    "→ blog.naver.com/aigrit/224268598962"
                ),
            },
            {
                "label": "Why-Failed",
                "body": (
                    "왜 Keelry가 실패했나.\n"
                    "콘셉트 정렬(Wind Check / Helm / Tack)은 깔끔.\n"
                    "근데 테스터는 모두 ‘무슨 뜻?’부터.\n"
                    "App Store ‘할 일 관리’ 검색 0건. ASO 출발부터 진 싸움.\n"
                    "→ blog.naver.com/aigrit/224268598962"
                ),
            },
            {
                "label": "Series",
                "body": (
                    "결정타 — 3앱 시리즈.\n"
                    "Keelry·GentleFast·GentleStudy = 같은 시리즈로 인식 X.\n"
                    "디자인 철학 공유해도 이름 어긋나면 시너지 0.\n"
                    "이름 통일 = 1인 마케팅 비용 절감.\n"
                    "→ blog.naver.com/aigrit/224268598962"
                ),
            },
            {
                "label": "Rename-Day",
                "body": (
                    "리네임 당일 커밋 3.\n"
                    "코드 / DB 컬럼 / 번들명.\n"
                    "DB 마이그레이션이 가장 아팠다 — 베타 데이터 쌓여있어서 검증 반나절.\n"
                    "직후 테스터 ‘아 그 태스크 관리 앱!’.\n"
                    "→ blog.naver.com/aigrit/224268598962"
                ),
            },
            {
                "label": "Checklist",
                "body": (
                    "출시 전 네이밍 체크 5.\n"
                    "① 발음 ② 의미 3초 ③ 검색어 ④ 확장 ⑤ 도메인.\n"
                    "3개 No → 다시.\n"
                    "GentleDo App Store 출시 완료.\n"
                    "→ blog.naver.com/aigrit/224268598962"
                ),
            },
        ],
    },
    # ============================================================
    # Naver #3 — 네이버 검색 대신 AI 검색 3일 후기 (Perplexity)
    # ============================================================
    {
        "naver_no": "03",
        "slug": "perplexity-vs-naver-search",
        "log_no": "224265199173",
        "title": "네이버 검색 대신 AI 검색 3일 써본 후기 — Perplexity 솔직 리뷰",
        "tone": "aigrit",
        "carousels": [
            # ----- post-1: Hook + 한 줄 결론 -----
            {
                "label": "Hook",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "Naver #03",
                        "title": "AI 검색 3일",
                        "hook": "쇼핑·지도 빼고는 Perplexity로 바꿨다",
                    }},
                    {"role": "context", "payload": {
                        "badge": "왜 갈아탔나",
                        "heading": "네이버 광고 · 구글 영어 한계",
                        "bullets": [
                            "부업 리서치할수록 광고가 상단",
                            "구글은 한국어 정보가 얕음",
                            "ChatGPT는 출처가 없음",
                            "Perplexity = AI 답변 + 출처 5~10개 자동",
                        ],
                    }},
                    {"role": "finding", "payload": {
                        "badge": "리서치 시간",
                        "heading": "부업 아이디어 1건 기준",
                        "metrics": [
                            {"tool": "네이버", "value": "20분", "note": "광고 우회 + 글마다 신뢰도 판단"},
                            {"tool": "Perplexity", "value": "3분", "note": "출처 포함 답변 + 추가 질문 즉답", "winner": True},
                        ],
                        "caption": "리서치 전체 시간은 70% 단축. 본업 회수 효과까지.",
                    }},
                    {"role": "list", "payload": {
                        "badge": "3일 실험 요약",
                        "heading": "어디서 결정적 차이가 났나",
                        "items": [
                            {"primary": "1. 부업 아이디어 리서치", "sub": "20분 → 3분 / 출처 자동"},
                            {"primary": "2. 제품 비교 (노트북)", "sub": "2시간 → 15분 / 단점 즉시"},
                            {"primary": "3. 법·규정 리서치", "sub": "공식 출처 즉시 연결 / 일방적 승"},
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "지금 읽기",
                        "heading": "3실험 + 단점 3 + 활용 5",
                        "bullets": [
                            "실험별 검색 화면 캡처",
                            "솔직한 단점 3가지 (네이버 우위 영역)",
                            "부업·재테크 5활용 프롬프트 공개",
                        ],
                        "url": "blog.naver.com/aigrit/224265199173",
                    }},
                ],
            },
            # ----- post-2: 3실험 비교 -----
            {
                "label": "Experiments",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "3일 실험",
                        "title": "네이버 vs Perplexity",
                        "hook": "리서치·비교·법규정 3가지 시나리오",
                    }},
                    {"role": "finding", "payload": {
                        "badge": "실험 1",
                        "heading": "부업 아이디어 리서치",
                        "metrics": [
                            {"tool": "네이버", "value": "20분", "note": "광고 + 2022~2023 옛 정보"},
                            {"tool": "Perplexity", "value": "3분", "note": "10가지 + 출처 + 추가 질문 즉답", "winner": True},
                        ],
                        "caption": "‘진입장벽 낮은 건?’ 같은 추가 질문 한 번에 답변.",
                    }},
                    {"role": "finding", "payload": {
                        "badge": "실험 2",
                        "heading": "제품 비교 (맥북에어 vs 그램)",
                        "metrics": [
                            {"tool": "네이버", "value": "2시간", "note": "체험단 리뷰 독점 · 단점 10p 뒤"},
                            {"tool": "Perplexity", "value": "15분", "note": "장단점 표 + 광고 vs 리뷰 판별", "winner": True},
                        ],
                        "caption": "구매 결정 시간 8배 단축.",
                    }},
                    {"role": "context", "payload": {
                        "badge": "실험 3",
                        "heading": "법·규정 리서치",
                        "bullets": [
                            "질문: 2026 개정 근로기준법 연장근로 조항",
                            "네이버: 광고 + 2023년 옛 정보",
                            "Perplexity: 고용노동부 공식 자료 즉시 연결",
                            "‘적용 시점은?’ 추가 질문 즉답",
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "전체 캡처",
                        "heading": "실험별 화면 + 출처",
                        "bullets": [
                            "각 실험 검색 결과 비교 캡처",
                            "Perplexity 출처 링크 5~10개 패턴",
                            "추가 질문 분기 흐름",
                        ],
                        "url": "blog.naver.com/aigrit/224265199173",
                    }},
                ],
            },
            # ----- post-3: 단점 3가지 솔직 -----
            {
                "label": "Limits",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "솔직 단점 3",
                        "title": "다 좋진 않다",
                        "hook": "네이버가 압도하는 영역도 있다",
                    }},
                    {"role": "context", "payload": {
                        "badge": "단점 ①",
                        "heading": "최신 뉴스는 네이버가 20~30분 빠름",
                        "bullets": [
                            "긴급 뉴스 · 주가 변동: 네이버 승",
                            "Perplexity는 인덱싱 시간차 존재",
                            "실시간 정보는 네이버 그대로",
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "단점 ②",
                        "heading": "한국 커뮤니티 검색은 네이버 승",
                        "bullets": [
                            "디시 · 뽐뿌 · 맘카페 등 한국 전용",
                            "Perplexity는 영어권 중심 인덱싱",
                            "한국 전용 사이트 정보 놓침",
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "단점 ③",
                        "heading": "쇼핑·지도는 네이버 압도",
                        "bullets": [
                            "네이버 쇼핑 · 지도 = 한국 전용 영역",
                            "시도할 필요도 없음",
                            "Perplexity 사용 대상 아님",
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "역할 분리",
                        "heading": "정보는 P · 쇼핑·지도·실시간은 N",
                        "bullets": [
                            "둘 다 깔아두고 상황별 호출",
                            "‘이 검색은 어디로?’ 판단 패턴",
                            "본문에 분기 가이드",
                        ],
                        "url": "blog.naver.com/aigrit/224265199173",
                    }},
                ],
            },
            # ----- post-4: 부업·재테크 5활용 -----
            {
                "label": "Use-5",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "부업 활용",
                        "title": "5가지 꿀팁",
                        "hook": "부업·재테크 리서치를 즉시 답으로",
                    }},
                    {"role": "list", "payload": {
                        "badge": "활용 ①·②",
                        "heading": "트렌드·경쟁사",
                        "items": [
                            {"primary": "트렌드 조사", "sub": "‘2026 한국 1인 사업 Top 5’ → 출처 포함 기획안 직행"},
                            {"primary": "경쟁사 분석", "sub": "‘스마트스토어 상위 판매자 공통점’ → 데이터 기반 답"},
                        ],
                    }},
                    {"role": "list", "payload": {
                        "badge": "활용 ③·④",
                        "heading": "법·세금 + 외국 부업",
                        "items": [
                            {"primary": "법·세금 질문", "sub": "‘간이사업자 부가세 신고 2026’ → 국세청 출처 즉시"},
                            {"primary": "외국 부업 트렌드", "sub": "‘미국 인기 AI 부업’ → 영어권 원문 자동 번역"},
                        ],
                    }},
                    {"role": "list", "payload": {
                        "badge": "활용 ⑤",
                        "heading": "학습 자료 검색",
                        "items": [
                            {"primary": "‘[주제] 입문 가이드 단계별로’"},
                            {"primary": "커리큘럼처럼 정리된 답변"},
                            {"primary": "후속 질문으로 깊이 파기"},
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "프롬프트 공개",
                        "heading": "5활용 본문 패턴",
                        "bullets": [
                            "활용별 실측 프롬프트 5개",
                            "한국어 vs 영어 질문 차이",
                            "후속 질문 패턴",
                        ],
                        "url": "blog.naver.com/aigrit/224265199173",
                    }},
                ],
            },
            # ----- post-5: 가격·CTA -----
            {
                "label": "Cost-CTA",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "가격 · CTA",
                        "title": "무료로도 충분",
                        "hook": "Pro 28,000원은 매일 5회 이상부터",
                    }},
                    {"role": "list", "payload": {
                        "badge": "플랜 비교",
                        "heading": "무료 vs Pro",
                        "items": [
                            {"primary": "무료 ₩0", "sub": "일일 5회 Pro 검색 / 가볍게 1주일 체험 추천"},
                            {"primary": "Pro 28,000원/월", "sub": "무제한 + GPT-4 사용 / 매일 5회+ 부업 리서치"},
                            {"primary": "결제 권장 시점", "sub": "본업·부업 합쳐 매일 10회 검색 시 본전 회수"},
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "FAQ 핵심",
                        "heading": "구독 전 자주 묻는 4가지",
                        "bullets": [
                            "가입 30초 — 구글·애플 계정 연동",
                            "iOS · 안드로이드 앱 모두 존재 (웹이 편함)",
                            "한국어 OK — 복잡 리서치는 영어 질문 + 한국어 답변",
                            "개인정보: Privacy → AI Data Retention OFF",
                        ],
                    }},
                    {"role": "list", "payload": {
                        "badge": "둘 다 쓰는 패턴",
                        "heading": "리서치 P · 글쓰기 G",
                        "items": [
                            {"primary": "리서치 → Perplexity", "sub": "출처 자동 + 최신 정보"},
                            {"primary": "글쓰기 → ChatGPT", "sub": "다재다능 모델 선택"},
                            {"primary": "둘 다 월 $40 — 시간 가치 회수"},
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "이웃추가",
                        "heading": "다음 편 — 자동화 5단계 시리즈",
                        "bullets": [
                            "AI로 블로그 포스팅 자동화",
                            "공감 ♡ + 댓글이 다음 편 동력",
                            "주 1편씩 AI 도구 실사용 후기",
                        ],
                        "url": "blog.naver.com/aigrit/224265199173",
                    }},
                ],
            },
        ],
        "ig_captions": [
            {
                "label": "Hook",
                "main": (
                    "네이버 광고만, 구글은 영어만. 한국에서 진짜 원하는 정보 찾기 왜 이렇게 어렵죠?\n\n"
                    "지난 3일 동안 모든 검색을 Perplexity로만 해봤어요. 결론부터 — 쇼핑·지도 빼고는 갈아탔습니다. "
                    "부업 아이디어 리서치 20분 → 3분, 제품 비교 2시간 → 15분, 법·규정은 공식 출처 즉시 연결."
                ),
                "slides": [
                    "왜 갈아탔나 — 광고·옛 정보·출처 부재",
                    "리서치 1건 20분 → 3분",
                    "3일 실험 — 리서치 / 비교 / 법규정",
                    "단점·활용·가격은 본문",
                ],
                "tags": [
                    "#Perplexity", "#퍼플렉시티", "#AI검색", "#네이버검색", "#구글검색",
                    "#ChatGPT", "#리서치도구", "#부업도구", "#사이드잡", "#1인부업",
                    "#재택부업", "#디지털노마드", "#네이버블로그", "#aigrit", "#AI도구",
                    "#생산성앱", "#효율화", "#트렌드조사", "#1인사업가", "#경쟁사분석",
                    "#원격근무", "#정보검색",
                ],
            },
            {
                "label": "Experiments",
                "main": (
                    "3일 실험 결과를 시나리오별로 정리.\n\n"
                    "실험 1 부업 아이디어: 네이버 20분(광고·옛글) vs Perplexity 3분(출처 포함 + 추가 질문). "
                    "실험 2 제품 비교: 2시간 vs 15분. "
                    "실험 3 법·규정: 고용노동부 공식 자료 즉시 연결로 일방적 승."
                ),
                "slides": [
                    "실험 1 — 부업 아이디어 / 20 → 3분",
                    "실험 2 — 제품 비교 / 2h → 15분",
                    "실험 3 — 법·규정 / 공식 출처 즉시",
                    "실험별 화면 캡처는 본문",
                ],
                "tags": [
                    "#Perplexity", "#퍼플렉시티", "#AI검색", "#리서치도구", "#네이버검색",
                    "#제품비교", "#노트북비교", "#법률검색", "#부업도구", "#사이드잡",
                    "#1인부업", "#재택부업", "#디지털노마드", "#네이버블로그", "#aigrit",
                    "#AI도구", "#원격근무", "#1인사업가", "#트렌드조사", "#정보검색",
                ],
            },
            {
                "label": "Limits",
                "main": (
                    "솔직 단점 3가지 — 다 좋진 않습니다.\n\n"
                    "① 최신 뉴스·주가는 네이버가 20~30분 빠름. ② 디시·맘카페 같은 한국 커뮤니티는 네이버 승. "
                    "③ 쇼핑·지도는 네이버 압도. 결론 — 정보 리서치는 Perplexity, 쇼핑·지도·실시간은 네이버."
                ),
                "slides": [
                    "단점 ① 최신 뉴스 네이버 빠름",
                    "단점 ② 한국 커뮤니티 네이버 승",
                    "단점 ③ 쇼핑·지도 네이버 압도",
                    "역할 분리: P vs N",
                ],
                "tags": [
                    "#Perplexity", "#퍼플렉시티", "#AI검색", "#네이버검색", "#솔직리뷰",
                    "#단점리뷰", "#쇼핑검색", "#커뮤니티검색", "#실시간뉴스", "#부업도구",
                    "#사이드잡", "#1인부업", "#재택부업", "#디지털노마드", "#네이버블로그",
                    "#aigrit", "#AI도구", "#원격근무", "#1인사업가", "#정보검색",
                ],
            },
            {
                "label": "Use-5",
                "main": (
                    "부업·재테크 활용 5가지 — 3일 써보면서 가장 유용했던 패턴.\n\n"
                    "① 트렌드 조사 ② 경쟁사 분석 ③ 법·세금 질문 ④ 외국 부업 트렌드 ⑤ 학습 자료. "
                    "각 활용에 들어가는 실제 프롬프트는 본문에. 출처 포함 답변이라 그대로 기획안으로 직행됩니다."
                ),
                "slides": [
                    "활용 ①·② 트렌드·경쟁사",
                    "활용 ③·④ 법·세금 + 외국 부업",
                    "활용 ⑤ 학습 자료 / 커리큘럼처럼",
                    "프롬프트 5개 본문 공개",
                ],
                "tags": [
                    "#Perplexity", "#퍼플렉시티", "#AI검색", "#트렌드조사", "#경쟁사분석",
                    "#법률검색", "#세금공부", "#스마트스토어", "#1인사업가", "#부업도구",
                    "#사이드잡", "#1인부업", "#재택부업", "#디지털노마드", "#네이버블로그",
                    "#aigrit", "#AI도구", "#원격근무", "#리서치도구", "#정보검색",
                ],
            },
            {
                "label": "Cost-CTA",
                "main": (
                    "무료 vs Pro — 어디서 갈리나.\n\n"
                    "무료는 일일 5회 Pro 검색 → 가볍게 체험 충분. 매일 5회+ 부업 리서치하시면 Pro 28,000원이 본전. "
                    "둘 다 쓰는 패턴은 리서치 Perplexity + 글쓰기 ChatGPT 분리. 다음 편은 자동화 5단계 시리즈."
                ),
                "slides": [
                    "무료 ₩0 / 일일 5회 — 1주 체험",
                    "Pro 28,000원 / 매일 5회+ 부업 리서치",
                    "FAQ — 가입 30초 / 한국어 OK / 개인정보",
                    "다음 편 — 자동화 5단계",
                ],
                "tags": [
                    "#Perplexity", "#퍼플렉시티", "#AI검색", "#PerplexityPro", "#월구독",
                    "#FAQ", "#가입가이드", "#개인정보", "#한국어AI", "#부업도구",
                    "#사이드잡", "#1인부업", "#재택부업", "#디지털노마드", "#네이버블로그",
                    "#aigrit", "#aigrit이웃추가", "#예고편", "#자동화", "#AI도구",
                ],
            },
        ],
        "threads": [
            {
                "label": "Hook",
                "body": (
                    "네이버 광고만, 구글은 영어만.\n"
                    "지난 3일 동안 모든 검색을 Perplexity로만 해봤습니다.\n\n"
                    "쇼핑·지도 빼고는 갈아탔어요. 부업 아이디어 20분 → 3분, 제품 비교 2시간 → 15분, "
                    "법·규정은 공식 출처 즉시 연결.\n\n"
                    "→ blog.naver.com/aigrit/224265199173"
                ),
            },
            {
                "label": "Experiments",
                "body": (
                    "3실험 결과.\n\n"
                    "1) 부업 아이디어: 네이버 20분(광고·옛글) vs Perplexity 3분(출처 + 추가 질문)\n"
                    "2) 제품 비교: 2시간 vs 15분, 단점 즉시\n"
                    "3) 법·규정: 고용노동부 공식 자료 즉시\n\n"
                    "→ blog.naver.com/aigrit/224265199173"
                ),
            },
            {
                "label": "Limits",
                "body": (
                    "솔직 단점 3.\n\n"
                    "① 최신 뉴스·주가 — 네이버 20~30분 빠름\n"
                    "② 한국 커뮤니티(디시·맘카페) — 네이버 승\n"
                    "③ 쇼핑·지도 — 네이버 압도\n\n"
                    "정보 리서치는 P, 쇼핑·실시간은 N — 역할 분리.\n\n"
                    "→ blog.naver.com/aigrit/224265199173"
                ),
            },
            {
                "label": "Use-5",
                "body": (
                    "부업·재테크 5활용.\n\n"
                    "① 트렌드 조사 ② 경쟁사 분석 ③ 법·세금 ④ 외국 부업 ⑤ 학습 자료.\n"
                    "출처 포함 답변이라 그대로 기획안으로 직행.\n\n"
                    "→ blog.naver.com/aigrit/224265199173"
                ),
            },
            {
                "label": "Cost-CTA",
                "body": (
                    "무료 일일 5회 → 1주 체험.\n"
                    "매일 5회+면 Pro 28,000원 본전.\n"
                    "리서치 P + 글쓰기 ChatGPT 분리 패턴.\n"
                    "다음 편 자동화 5단계.\n\n"
                    "→ blog.naver.com/aigrit/224265199173"
                ),
            },
        ],
        "tweets": [
            {
                "label": "Hook",
                "body": (
                    "네이버는 광고만, 구글은 영어만.\n"
                    "Perplexity 3일 실측 — 쇼핑·지도 빼고 갈아탔다.\n"
                    "리서치 20 → 3분, 비교 2h → 15분, 법규정 공식 출처 즉시.\n"
                    "→ blog.naver.com/aigrit/224265199173"
                ),
            },
            {
                "label": "Experiments",
                "body": (
                    "3실험 결과.\n"
                    "부업 아이디어: 20 → 3분.\n"
                    "제품 비교: 2h → 15분.\n"
                    "법·규정: 공식 출처 즉시 (일방적 승).\n"
                    "→ blog.naver.com/aigrit/224265199173"
                ),
            },
            {
                "label": "Limits",
                "body": (
                    "솔직 단점 3.\n"
                    "① 최신 뉴스 네이버 빠름.\n"
                    "② 한국 커뮤니티 네이버 승.\n"
                    "③ 쇼핑·지도 네이버 압도.\n"
                    "리서치 P · 실시간 N 분리.\n"
                    "→ blog.naver.com/aigrit/224265199173"
                ),
            },
            {
                "label": "Use-5",
                "body": (
                    "부업 5활용.\n"
                    "① 트렌드 ② 경쟁사 ③ 법·세금 ④ 외국 부업 ⑤ 학습.\n"
                    "출처 자동이라 기획안 직행.\n"
                    "→ blog.naver.com/aigrit/224265199173"
                ),
            },
            {
                "label": "Cost-CTA",
                "body": (
                    "무료 일일 5회로 1주 체험.\n"
                    "매일 5회+ Pro 28,000원 본전.\n"
                    "리서치 P + 글쓰기 GPT.\n"
                    "다음 편 자동화 5단계.\n"
                    "→ blog.naver.com/aigrit/224265199173"
                ),
            },
        ],
    },
    # ============================================================
    # Naver #2 — 퇴근 후 30분, Notion AI로 부업 기반 만들기
    # ============================================================
    {
        "naver_no": "02",
        "slug": "notion-ai-side-income",
        "log_no": "224264267004",
        "title": "퇴근 후 30분, Notion AI로 부업 기반 만들기 — 회의록 5분에 끝내기",
        "tone": "aigrit",
        "carousels": [
            # ----- post-1: Hook + 30분의 의미 -----
            {
                "label": "Hook",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "Naver #02",
                        "title": "퇴근 후 30분",
                        "hook": "Notion AI로 부업 기반 · 월 14,000원",
                    }},
                    {"role": "context", "payload": {
                        "badge": "왜 30분인가",
                        "heading": "평일 저녁 9시 이후의 30분",
                        "bullets": [
                            "설거지 · 아이 재우기 끝나면 남는 시간",
                            "이걸로 부업 기반이 만들어질까 고민",
                            "정답은 도구 → Notion AI 월 $10",
                            "투자 1개월차에 회수 시작",
                        ],
                    }},
                    {"role": "finding", "payload": {
                        "badge": "본업 회수",
                        "heading": "회의록 정리 시간",
                        "metrics": [
                            {"tool": "수동 정리", "value": "30분", "note": "1시간 회의 후 작업 평균"},
                            {"tool": "Notion AI", "value": "5분", "note": "AI 요약 → 사람 검토", "winner": True},
                        ],
                        "caption": "퇴근 25분 빨라짐. 부업 시간이 본업 정리에서 회수됨.",
                    }},
                    {"role": "list", "payload": {
                        "badge": "5활용 미리보기",
                        "heading": "30분짜리 자동 루틴 5종",
                        "items": [
                            {"primary": "1. 회의록 5분 요약", "sub": "Custom prompt 1회 저장 → 매번 동일 포맷"},
                            {"primary": "2. DB 자연어 쿼리", "sub": "한국어 한 줄로 SQL 필터 대체"},
                            {"primary": "3. 긴 문서 핵심 3줄", "sub": "PDF·웹문서 붙여넣고 목적 지정"},
                            {"primary": "4. 한·영 번역", "sub": "DeepL·파파고보다 문맥 이해 우수"},
                            {"primary": "5. 아이디어 10개 확장", "sub": "월요일 30분 → 그 주 콘텐츠 5개"},
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "지금 읽기",
                        "heading": "월 1.4만원 회수표",
                        "bullets": [
                            "투자 1개월 회수 조건",
                            "Custom prompt 회의록 템플릿 공개",
                            "주 5일 30분 → 월 10시간 부업 시간",
                        ],
                        "url": "blog.naver.com/aigrit/224264267004",
                    }},
                ],
            },
            # ----- post-2: Notion AI vs ChatGPT 차이 -----
            {
                "label": "Compare",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "차이점",
                        "title": "Notion AI vs ChatGPT",
                        "hook": "둘 다 필요하지만 용도가 다르다",
                    }},
                    {"role": "context", "payload": {
                        "badge": "ChatGPT",
                        "heading": "대화창 안에서 작동",
                        "bullets": [
                            "뭘 물어보려면 매번 복붙 필요",
                            "범용성 최고 · 다재다능",
                            "혼자 쓸 때 압도적",
                            "월 $20",
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "Notion AI",
                        "heading": "내 노션 안에서 작동",
                        "bullets": [
                            "이미 정리한 회의록·DB를 직접 읽음",
                            "팀 워크스페이스에 통합",
                            "복붙 작업 자체가 사라짐",
                            "월 $10",
                        ],
                    }},
                    {"role": "list", "payload": {
                        "badge": "선택 기준",
                        "heading": "어디에 더 손이 갈까",
                        "items": [
                            {"primary": "팀에서 쓴다 → Notion AI", "sub": "공동 워크스페이스 통합 가치 큼"},
                            {"primary": "혼자 쓴다 → ChatGPT", "sub": "다재다능 + 모델 선택지 많음"},
                            {"primary": "Notion 정리 많다 → Notion AI", "sub": "기존 자료 직접 호출 가치"},
                            {"primary": "둘 다 → 월 $30이지만 시간 가치 10배", "sub": "회의록·DB는 Notion AI · 글쓰기 ChatGPT"},
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "구독 결정",
                        "heading": "본인 패턴 분석",
                        "bullets": [
                            "노션 사용 빈도 체크",
                            "팀 vs 1인 환경 차이",
                            "둘 다 쓰는 분리 워크플로우",
                        ],
                        "url": "blog.naver.com/aigrit/224264267004",
                    }},
                ],
            },
            # ----- post-3: 활용 #1·#2 회의록 + DB 쿼리 -----
            {
                "label": "Detail-1",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "디테일 1/2",
                        "title": "회의록 · DB 쿼리",
                        "hook": "5분 요약 + 한국어 한 줄 쿼리",
                    }},
                    {"role": "context", "payload": {
                        "badge": "활용 #1",
                        "heading": "회의록 5분에 끝내기",
                        "bullets": [
                            "녹음 → Notion 받아쓰기 → AI 요약 버튼",
                            "30분 → 5분 (퇴근 25분 단축)",
                            "Custom prompt 저장 → 매번 동일 포맷",
                            "결정 사항 · 액션 · 미해결 자동 분리",
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "활용 #2",
                        "heading": "DB 자연어 쿼리",
                        "bullets": [
                            "이번 달 완료된 태스크 몇 개? → 즉시",
                            "지난주 매출 TOP 3 → 즉시",
                            "마감 지난 할 일 → 즉시",
                            "필터 매번 설정하는 작업 자체 사라짐",
                        ],
                    }},
                    {"role": "list", "payload": {
                        "badge": "Custom prompt",
                        "heading": "회의록 템플릿 1개로 평생",
                        "items": [
                            {"primary": "결정 사항 (불릿 형식)"},
                            {"primary": "액션 아이템 (담당자·마감일)"},
                            {"primary": "미해결 이슈"},
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "전체 가이드",
                        "heading": "본문에 단계 + 캡처",
                        "bullets": [
                            "Custom prompt 저장 위치",
                            "녹음 → 받아쓰기 도구 추천",
                            "DB 쿼리 한국어 패턴",
                        ],
                        "url": "blog.naver.com/aigrit/224264267004",
                    }},
                ],
            },
            # ----- post-4: 활용 #3·#4·#5 -----
            {
                "label": "Detail-2",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "디테일 2/2",
                        "title": "요약 · 번역 · 아이디어",
                        "hook": "리서치 · 해외 부업 · 콘텐츠 기획",
                    }},
                    {"role": "context", "payload": {
                        "badge": "활용 #3",
                        "heading": "긴 문서 핵심 3줄",
                        "bullets": [
                            "PDF · 웹문서 붙여넣고 목적 지정",
                            "단순 요약보다 ‘목적별 요약’이 품질 차이",
                            "창업 관점 / 마케팅 관점 / 초보자용",
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "활용 #4",
                        "heading": "한·영 번역",
                        "bullets": [
                            "DeepL · 파파고보다 문맥 이해 우수",
                            "긴 문서 톤앤매너 유지",
                            "크몽 · 유튜브 자막 · 영문 메일 즉시",
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "활용 #5",
                        "heading": "아이디어 10개 확장",
                        "bullets": [
                            "월요일 30분 → 그 주 콘텐츠 5개",
                            "제목 1개 → 세부 아웃라인 자동",
                            "주 5개 콘텐츠가 자동으로 굴러감",
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "전체 프롬프트",
                        "heading": "목적별 요약 패턴 공개",
                        "bullets": [
                            "‘무엇 관점에서’ 요약 템플릿",
                            "번역 톤앤매너 유지 옵션",
                            "아이디어 확장 → 아웃라인 → 실행",
                        ],
                        "url": "blog.naver.com/aigrit/224264267004",
                    }},
                ],
            },
            # ----- post-5: 비용·결론·CTA -----
            {
                "label": "Cost-CTA",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "비용 · 결정",
                        "title": "월 14,000원의 회수",
                        "hook": "주 2시간 문서 작업이면 1~2개월 안에 본전",
                    }},
                    {"role": "finding", "payload": {
                        "badge": "월 누적",
                        "heading": "30분 × 주 5일",
                        "metrics": [
                            {"tool": "주 누적", "value": "2.5시간", "note": "평일 저녁 30분 × 5일"},
                            {"tool": "월 누적", "value": "10시간", "note": "부업 사이드 프로젝트 1개 분량", "winner": True},
                        ],
                        "caption": "10시간 = 한 달이 한 프로젝트가 굴러가는 시간 단위.",
                    }},
                    {"role": "list", "payload": {
                        "badge": "FAQ 핵심",
                        "heading": "구독 전 자주 묻는 4가지",
                        "items": [
                            {"primary": "월 1.4만원 가치?", "sub": "주 2h 문서 작업이면 1~2개월에 본전"},
                            {"primary": "1인 가능?", "sub": "1인 플랜 존재 · 개인 지식관리용으로 우수"},
                            {"primary": "무료 체험?", "sub": "AI 무료 크레딧 20회 후 유료 전환"},
                            {"primary": "한국어 품질?", "sub": "2025년 들어 대폭 개선 · 한국어 부담 없음"},
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "한 줄 결론",
                        "heading": "거창한 게 아니라 작은 누적",
                        "bullets": [
                            "회의록 5분 끝내기 = 본업 시간 회수",
                            "콘텐츠 10개 뽑기 = 부업 기반 누적",
                            "30분 × 한 달 = 사이드 프로젝트 한 개",
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "이웃추가",
                        "heading": "다음 편 — Perplexity 3일 실험",
                        "bullets": [
                            "네이버 검색 대신 AI 검색 후기",
                            "부업 리서치 활용법",
                            "공감 ♡ + 댓글 = 다음 편 동력",
                        ],
                        "url": "blog.naver.com/aigrit/224264267004",
                    }},
                ],
            },
        ],
        "ig_captions": [
            {
                "label": "Hook",
                "main": (
                    "평일 저녁 9시. 설거지 끝내고 아이 재우고 나면 남는 30분.\n\n"
                    "이걸로 부업 기반이 만들어질까 고민하다 답으로 정착한 도구가 Notion AI ($10/월)였어요. "
                    "회의록 30분 → 5분 단축으로 본업 시간이 회수되고, 그 시간이 부업 30분으로 굴러갑니다."
                ),
                "slides": [
                    "왜 30분인가 — 부업 사이드 프로젝트의 단위",
                    "회의록 30 → 5분 = 본업 회수 25분",
                    "5활용 미리보기 — 회의·DB·요약·번역·아이디어",
                    "월 1.4만원 회수 시점 → 본문",
                ],
                "tags": [
                    "#NotionAI", "#노션AI", "#직장인부업", "#부업도구", "#사이드잡",
                    "#1인부업", "#생산성앱", "#회의록정리", "#재택부업", "#디지털노마드",
                    "#네이버블로그", "#aigrit", "#AI도구", "#아이디어기획", "#콘텐츠기획",
                    "#원격근무", "#1인사업가", "#개인지식관리", "#PKM", "#노트앱",
                    "#효율화", "#시간관리", "#퇴근후",
                ],
            },
            {
                "label": "Compare",
                "main": (
                    "Notion AI vs ChatGPT — 둘 다 필요하지만 용도가 달라요.\n\n"
                    "ChatGPT는 대화창에서 작동(매번 복붙), Notion AI는 내 노션 안에서 작동(기존 자료 직접 호출). "
                    "팀에서 쓰면 Notion AI, 혼자 다재다능이면 ChatGPT, 둘 다 쓰면 월 $30 시간 가치 10배."
                ),
                "slides": [
                    "ChatGPT — 대화창, 다재다능, $20",
                    "Notion AI — 내 노션 안, 팀 통합, $10",
                    "팀 vs 1인 vs Notion 정리량으로 결정",
                    "둘 다 쓰는 분리 워크플로우 → 본문",
                ],
                "tags": [
                    "#NotionAI", "#ChatGPT", "#OpenAI", "#노션AI", "#AI도구비교",
                    "#직장인부업", "#1인사업가", "#부업도구", "#사이드잡", "#생산성앱",
                    "#네이버블로그", "#aigrit", "#디지털노마드", "#재택부업", "#원격근무",
                    "#팀협업", "#개인지식관리", "#PKM", "#1인부업", "#AI비교",
                ],
            },
            {
                "label": "Detail-1",
                "main": (
                    "활용 #1·#2 — 회의록 5분 + DB 자연어 쿼리.\n\n"
                    "Custom prompt 한 번 저장하면 매번 동일 포맷으로 결정사항·액션·미해결이 자동 분리. "
                    "DB는 ‘이번 달 완료 태스크 몇 개?’ 한국어 한 줄로 SQL 필터 대체. "
                    "필터 매번 설정하는 작업 자체가 사라집니다."
                ),
                "slides": [
                    "활용 #1 — 회의록 30 → 5분 / 퇴근 25분 단축",
                    "활용 #2 — DB 자연어 쿼리 / 필터 작업 소멸",
                    "Custom prompt 템플릿 — 결정·액션·미해결",
                    "단계별 캡처는 본문",
                ],
                "tags": [
                    "#NotionAI", "#노션AI", "#회의록정리", "#회의록자동화", "#노션DB",
                    "#NotionDB", "#1인사업가", "#팀협업", "#직장인부업", "#부업도구",
                    "#사이드잡", "#생산성앱", "#AI도구", "#네이버블로그", "#aigrit",
                    "#PKM", "#개인지식관리", "#디지털노마드", "#재택부업", "#1인부업",
                ],
            },
            {
                "label": "Detail-2",
                "main": (
                    "활용 #3·#4·#5 — 요약·번역·아이디어 확장.\n\n"
                    "긴 문서는 ‘목적별 요약’이 품질 차이 (창업 관점/마케팅 관점/초보자용). "
                    "번역은 DeepL·파파고보다 문맥 우수, 톤앤매너 유지. "
                    "아이디어 10개 확장으로 월요일 30분이 그 주 콘텐츠 5개로 굴러갑니다."
                ),
                "slides": [
                    "활용 #3 — 긴 문서 핵심 3줄 / 목적 지정 필수",
                    "활용 #4 — 한·영 번역 / 톤앤매너 유지",
                    "활용 #5 — 아이디어 10개 → 세부 아웃라인",
                    "월요일 30분 = 그 주 콘텐츠 5개",
                ],
                "tags": [
                    "#NotionAI", "#노션AI", "#문서요약", "#번역도구", "#콘텐츠기획",
                    "#아이디어기획", "#1인사업가", "#부업도구", "#사이드잡", "#재택부업",
                    "#네이버블로그", "#aigrit", "#디지털노마드", "#AI도구", "#개인지식관리",
                    "#PKM", "#원격근무", "#1인부업", "#생산성앱", "#직장인부업",
                ],
            },
            {
                "label": "Cost-CTA",
                "main": (
                    "월 14,000원이 어떻게 회수되나.\n\n"
                    "30분 × 주 5일 = 2.5시간, 한 달이면 10시간. 사이드 프로젝트 1개가 굴러가는 시간 단위입니다. "
                    "주 2시간 이상 문서 작업이 있으시면 1~2개월 안에 본전. "
                    "다음 편은 Perplexity 3일 실험입니다."
                ),
                "slides": [
                    "월 누적 10시간 = 사이드 프로젝트 1개",
                    "FAQ 4종 — 1.4만원 가치 / 1인 / 무료 / 한국어",
                    "한 줄 결론 — 거창함이 아니라 작은 누적",
                    "다음 편 — Perplexity 3일 실험",
                ],
                "tags": [
                    "#NotionAI", "#노션AI", "#월구독", "#FAQ", "#부업비용",
                    "#사이드잡", "#1인부업", "#재택부업", "#1인사업가", "#디지털노마드",
                    "#네이버블로그", "#aigrit", "#aigrit이웃추가", "#Perplexity", "#예고편",
                    "#AI검색", "#원격근무", "#콘텐츠기획", "#PKM", "#생산성앱",
                ],
            },
        ],
        "threads": [
            {
                "label": "Hook",
                "body": (
                    "평일 저녁 9시. 설거지 끝내고 아이 재우면 남는 30분.\n\n"
                    "이걸로 부업 기반이 만들어질까 고민하다 정착한 게 Notion AI 월 $10. "
                    "회의록 30분 → 5분으로 본업 시간이 회수되고, 그 시간이 부업 30분으로 굴러갑니다.\n\n"
                    "→ blog.naver.com/aigrit/224264267004"
                ),
            },
            {
                "label": "Compare",
                "body": (
                    "Notion AI vs ChatGPT — 둘 다 필요하지만 용도가 다릅니다.\n\n"
                    "ChatGPT는 대화창(매번 복붙), Notion AI는 내 노션 안(기존 자료 직접 호출).\n"
                    "팀이면 Notion AI, 혼자 다재다능이면 ChatGPT.\n"
                    "둘 다 쓰면 월 $30 — 시간 가치 10배.\n\n"
                    "→ blog.naver.com/aigrit/224264267004"
                ),
            },
            {
                "label": "Detail-1",
                "body": (
                    "활용 #1·#2 — 회의록 + DB 쿼리.\n\n"
                    "Custom prompt 1회 저장 → 매번 결정·액션·미해결 자동 분리.\n"
                    "DB는 ‘이번 달 완료 태스크 몇 개?’ 한국어 한 줄로 SQL 필터 대체.\n"
                    "필터 매번 설정하는 작업 자체가 사라집니다.\n\n"
                    "→ blog.naver.com/aigrit/224264267004"
                ),
            },
            {
                "label": "Detail-2",
                "body": (
                    "활용 #3·#4·#5 — 요약·번역·아이디어.\n\n"
                    "긴 문서는 ‘목적별 요약’이 품질 차이.\n"
                    "번역은 DeepL·파파고보다 문맥·톤 우수.\n"
                    "아이디어 10개 확장으로 월요일 30분이 그 주 콘텐츠 5개.\n\n"
                    "→ blog.naver.com/aigrit/224264267004"
                ),
            },
            {
                "label": "Cost-CTA",
                "body": (
                    "월 1.4만원 회수.\n\n"
                    "30분 × 주 5일 = 2.5시간, 한 달이면 10시간.\n"
                    "사이드 프로젝트 1개가 굴러가는 단위입니다.\n"
                    "다음 편은 Perplexity 3일 실험.\n\n"
                    "→ blog.naver.com/aigrit/224264267004"
                ),
            },
        ],
        "tweets": [
            {
                "label": "Hook",
                "body": (
                    "평일 저녁 9시 30분.\n"
                    "Notion AI ($10/월)로 회의록 30 → 5분.\n"
                    "본업 25분 회수 → 부업 30분으로 굴러감.\n"
                    "월 1.4만원이 1~2개월에 본전.\n"
                    "→ blog.naver.com/aigrit/224264267004"
                ),
            },
            {
                "label": "Compare",
                "body": (
                    "Notion AI vs ChatGPT.\n"
                    "ChatGPT — 대화창, 다재다능, $20.\n"
                    "Notion AI — 노션 안, 팀 통합, $10.\n"
                    "팀이면 Notion AI, 1인 다재다능이면 ChatGPT.\n"
                    "→ blog.naver.com/aigrit/224264267004"
                ),
            },
            {
                "label": "Detail-1",
                "body": (
                    "회의록 + DB 쿼리.\n"
                    "Custom prompt 저장 → 결정·액션·미해결 자동 분리.\n"
                    "DB는 한국어 한 줄로 SQL 대체.\n"
                    "필터 작업 자체가 사라짐.\n"
                    "→ blog.naver.com/aigrit/224264267004"
                ),
            },
            {
                "label": "Detail-2",
                "body": (
                    "요약·번역·아이디어.\n"
                    "목적별 요약이 품질 차이.\n"
                    "DeepL·파파고보다 문맥·톤 우수.\n"
                    "월요일 30분 = 그 주 콘텐츠 5개.\n"
                    "→ blog.naver.com/aigrit/224264267004"
                ),
            },
            {
                "label": "Cost-CTA",
                "body": (
                    "월 누적 10시간 = 사이드 프로젝트 1개.\n"
                    "주 2h 문서 작업이면 1~2개월 본전.\n"
                    "다음 편 Perplexity 3일 실험.\n"
                    "→ blog.naver.com/aigrit/224264267004"
                ),
            },
        ],
    },
    # ============================================================
    # Naver #1 — 월 5만원 절약하는 아이폰 단축어 5개
    # ============================================================
    {
        "naver_no": "01",
        "slug": "apple-shortcuts-50000won",
        "log_no": "224263045957",
        "title": "월 5만원 절약하는 아이폰 단축어 5개 — 퇴근 후 40분 벌기",
        "tone": "aigrit",
        "carousels": [
            # ----- post-1: Hook + 한 줄 결론 -----
            {
                "label": "Hook",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "Naver #01",
                        "title": "퇴근 후 40분 벌기",
                        "hook": "아이폰 단축어 + AI · 월 5만원 절약",
                    }},
                    {"role": "context", "payload": {
                        "badge": "왜 단축어인가",
                        "heading": "아이폰에 이미 깔려 있는 무료 자동화",
                        "bullets": [
                            "안드로이드엔 없는 iOS 전용 도구",
                            "ChatGPT·Claude 연결 → Siri보다 똑똑한 비서",
                            "단축어 1개 만드는 데 10~20분",
                            "한 번 만들면 평생 작동",
                        ],
                    }},
                    {"role": "finding", "payload": {
                        "badge": "시간 회수",
                        "heading": "5단축어 합산 절약량",
                        "metrics": [
                            {"tool": "월 절약", "value": "21시간", "note": "5단축어 합 일평균 ≥40분", "winner": True},
                            {"tool": "환산 가치", "value": "5만~30만원", "note": "본인 시급 기준 환산"},
                        ],
                        "caption": "측정 조건: 출퇴근 지하철 40분 + 부업 운영 1편/주 가정",
                    }},
                    {"role": "list", "payload": {
                        "badge": "5단축어 미리보기",
                        "heading": "퇴근 후 자동화 5종",
                        "items": [
                            {"primary": "1. 한 줄 요약", "sub": "선택 → 공유 → 5초 요약 (매일 10분)"},
                            {"primary": "2. 스크린샷 자동 분석", "sub": "alt·캡션·파일명 자동 (편당 15분)"},
                            {"primary": "3. 음성 → Notion", "sub": "Whisper 받아쓰기 (매일 10분)"},
                            {"primary": "4. 초고속 번역", "sub": "Cmd+C → 단축키 → Cmd+V (매일 5분)"},
                            {"primary": "5. 말로 캘린더 입력", "sub": "복잡한 반복도 정확 파싱 (주 20분)"},
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "지금 읽기",
                        "heading": "단축어 5개 만드는 법",
                        "bullets": [
                            "단축어별 만드는 방법 단계별 정리",
                            "API 비용 진짜 얼마 나오나",
                            "API 키 없이 무료로 쓰는 두 가지 길",
                        ],
                        "url": "blog.naver.com/aigrit/224263045957",
                    }},
                ],
            },
            # ----- post-2: 시간 회수 비교 -----
            {
                "label": "TimeBack",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "시간 회수",
                        "title": "월 21시간이 어디서 오나",
                        "hook": "5단축어가 가져다 주는 분 단위 회수",
                    }},
                    {"role": "finding", "payload": {
                        "badge": "Top 1",
                        "heading": "스크린샷 자동 분석",
                        "metrics": [
                            {"tool": "수동 (글 1편)", "value": "150분", "note": "이미지 10장 alt 직접 작성"},
                            {"tool": "단축어", "value": "15분", "note": "GPT-4 Vision 자동 캡션", "winner": True},
                        ],
                        "caption": "블로그 부업 운영자 기준 가장 큰 시간 회수.",
                    }},
                    {"role": "finding", "payload": {
                        "badge": "Top 2",
                        "heading": "한 줄 요약",
                        "metrics": [
                            {"tool": "기사 20개 정독", "value": "60분", "note": "출근 지하철 환경"},
                            {"tool": "요약 스캔", "value": "10분", "note": "선택 → 공유 → 5초", "winner": True},
                        ],
                        "caption": "체감 정보 처리 속도가 6배.",
                    }},
                    {"role": "list", "payload": {
                        "badge": "나머지 3종",
                        "heading": "음성·번역·캘린더",
                        "items": [
                            {"primary": "음성 → Notion", "sub": "Siri 노트 대비 정확도·검색성 모두 우위"},
                            {"primary": "초고속 번역", "sub": "파파고 대비 문맥 이해 우수, 월 500원"},
                            {"primary": "말로 캘린더", "sub": "복잡한 반복(격주·다음 주 화)도 정확"},
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "전체 표 보기",
                        "heading": "월 21시간 환산표",
                        "bullets": [
                            "단축어별 일·월 분 단위 절약량",
                            "시급 환산 기준 5만~30만원 가치",
                            "부업 1~2시간 추가 확보 가능",
                        ],
                        "url": "blog.naver.com/aigrit/224263045957",
                    }},
                ],
            },
            # ----- post-3: 단축어 #1·#2 디테일 -----
            {
                "label": "Detail-1",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "디테일 1/2",
                        "title": "요약 · 스크린샷",
                        "hook": "선택 → 공유 → 5초 / 글 1편당 15분",
                    }},
                    {"role": "context", "payload": {
                        "badge": "단축어 #1",
                        "heading": "긴 글 한 줄 요약",
                        "bullets": [
                            "Safari · 메일 · 카톡 모두 공유 메뉴 호출",
                            "5초 뒤 클립보드에 50자 요약 자동 복사",
                            "출근 지하철 40분 → 뉴스 20개 스캔 가능",
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "단축어 #2",
                        "heading": "스크린샷 자동 분석",
                        "bullets": [
                            "GPT-4 Vision이 화면을 직접 분석",
                            "alt 텍스트 · 캡션 · 파일명 동시 생성",
                            "블로그 1편당 150분 → 15분",
                        ],
                    }},
                    {"role": "list", "payload": {
                        "badge": "공통 핵심",
                        "heading": "공유 메뉴가 입구",
                        "items": [
                            {"primary": "단축어 앱 → 갤러리", "sub": "공유 메뉴에 등록 옵션 ON"},
                            {"primary": "API Key 입력 1회", "sub": "OpenAI 또는 Anthropic 콘솔에서 발급"},
                            {"primary": "테스트 입력 1회", "sub": "5초 안에 응답 안 오면 재시도 분기"},
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "단계별 캡처",
                        "heading": "만드는 법 본문에",
                        "bullets": [
                            "단축어 앱 어떤 메뉴를 쓰는지",
                            "ChatGPT 앱 vs API 모드 차이",
                            "응답 5초 넘을 때 디버깅",
                        ],
                        "url": "blog.naver.com/aigrit/224263045957",
                    }},
                ],
            },
            # ----- post-4: 단축어 #3·#4·#5 디테일 -----
            {
                "label": "Detail-2",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "디테일 2/2",
                        "title": "음성 · 번역 · 캘린더",
                        "hook": "터치 1번 / 단축키 1번 / 한 문장 1번",
                    }},
                    {"role": "context", "payload": {
                        "badge": "단축어 #3",
                        "heading": "음성 → Notion 저장",
                        "bullets": [
                            "홈 화면 터치 → 말하기 → 끝",
                            "Whisper가 한국어 받아쓰기 자동",
                            "검색 가능한 형태로 DB에 누적",
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "단축어 #4",
                        "heading": "초고속 번역",
                        "bullets": [
                            "Cmd+C → 단축키 → Cmd+V (3초)",
                            "Claude Haiku 사용 시 월 500원 수준",
                            "파파고 대비 문맥 이해 우수",
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "단축어 #5",
                        "heading": "말로 캘린더 입력",
                        "bullets": [
                            "내일 오후 3시 강남역 → 정확히 등록",
                            "다음 주·격주 같은 복잡 표현 정확",
                            "Siri보다 파싱 정확도 압도적",
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "전체 가이드",
                        "heading": "본문에서 단계별",
                        "bullets": [
                            "Whisper 권한·API 셋업",
                            "맥 키보드 단축키 등록 방법",
                            "캘린더·반복 일정 파싱 패턴",
                        ],
                        "url": "blog.naver.com/aigrit/224263045957",
                    }},
                ],
            },
            # ----- post-5: 비용·무료법·CTA -----
            {
                "label": "Cost-CTA",
                "cards": [
                    {"role": "cover", "payload": {
                        "badge": "비용 · 무료법",
                        "title": "월 1천~5천원이 끝",
                        "hook": "API 결제 부담? 무료로도 충분",
                    }},
                    {"role": "finding", "payload": {
                        "badge": "월 비용",
                        "heading": "API 사용량 실측",
                        "metrics": [
                            {"tool": "일반 사용", "value": "월 1~5천원", "note": "5단축어 일상 사용", "winner": True},
                            {"tool": "헤비 사용", "value": "월 1만원", "note": "블로그 운영 + 매일 음성"},
                        ],
                        "caption": "시간 절약 가치 5만~30만원 대비 비용은 무시할 수준.",
                    }},
                    {"role": "list", "payload": {
                        "badge": "무료 옵션 2종",
                        "heading": "API 키 없이 시작",
                        "items": [
                            {"primary": "① ChatGPT 앱 연동", "sub": "아이폰에 앱만 깔려 있으면 단축어에서 직접 호출"},
                            {"primary": "② 웹 URL 호출", "sub": "claude.ai 같은 웹을 단축어로 자동 호출"},
                            {"primary": "두 옵션 모두 무제한 무료", "sub": "유료보다 제한적이나 시작은 충분"},
                        ],
                    }},
                    {"role": "context", "payload": {
                        "badge": "주말 1회",
                        "heading": "5개 다 만드는 데 한나절",
                        "bullets": [
                            "처음엔 기술적 설명에 막히는 게 정상",
                            "실제로는 레고 조립 수준의 단계 조합",
                            "한 번 만들면 평생 매일 사용",
                        ],
                    }},
                    {"role": "cta", "payload": {
                        "badge": "이웃추가",
                        "heading": "다음 편 — Notion AI 부업 기반",
                        "bullets": [
                            "회의록 5분에 끝내는 법",
                            "1인 사업가 DB 관리 꿀팁",
                            "공감 ♡ + 댓글 = 큰 힘",
                        ],
                        "url": "blog.naver.com/aigrit/224263045957",
                    }},
                ],
            },
        ],
        "ig_captions": [
            {
                "label": "Hook",
                "main": (
                    "퇴근 후 40분, 어디로 사라지셨나요?\n\n"
                    "출퇴근 지하철에서 뉴스 요약 · 영어 번역 · 캘린더 입력만 하다 보면 시간이 다 갑니다. "
                    "이걸 모두 아이폰 단축어 + AI로 자동화한 후기를 정리했어요.\n\n"
                    "월 5만원 절약 · 21시간 회수 · 단축어 1개 만드는 데 10분."
                ),
                "slides": [
                    "왜 단축어인가 — 안드로이드엔 없는 iOS 무료 도구",
                    "월 21시간 시간 회수, 5만~30만원 환산 가치",
                    "5단축어 미리보기 — 요약·스크린샷·음성·번역·캘린더",
                    "본문 가이드 → 만드는 단계별 캡처",
                ],
                "tags": [
                    "#아이폰단축어", "#iOS자동화", "#AI자동화", "#직장인부업", "#부업도구",
                    "#생산성앱", "#ChatGPT", "#Claude", "#아이폰꿀팁", "#아이폰활용",
                    "#퇴근후", "#시간관리", "#시간절약", "#자동화", "#네이버블로그",
                    "#블로그부업", "#1인부업", "#디지털노마드", "#사이드잡", "#아이폰",
                    "#사이드프로젝트", "#원격업무", "#aigrit",
                ],
            },
            {
                "label": "TimeBack",
                "main": (
                    "월 21시간이 어디서 오나, 분 단위로 분해해봤습니다.\n\n"
                    "스크린샷 자동 분석이 압도적 1위 (글 1편당 150분 → 15분), "
                    "한 줄 요약이 2위 (기사 20개 60분 → 10분). "
                    "나머지 3종은 음성·번역·캘린더로 매일 짧게 절약."
                ),
                "slides": [
                    "Top 1: 스크린샷 분석 — 150분 → 15분",
                    "Top 2: 한 줄 요약 — 60분 → 10분",
                    "음성·번역·캘린더 — 매일 짧게, 합산하면 큰 회수",
                    "전체 표 → 본문",
                ],
                "tags": [
                    "#아이폰단축어", "#시간관리", "#생산성", "#AI자동화", "#블로그부업",
                    "#GPT4Vision", "#Whisper", "#Claude", "#효율화", "#직장인부업",
                    "#부업도구", "#스크린샷", "#alt텍스트", "#네이버블로그", "#aigrit",
                    "#아이폰활용", "#디지털노마드", "#사이드잡", "#원격업무", "#1인부업",
                ],
            },
            {
                "label": "Detail-1",
                "main": (
                    "단축어 #1·#2 디테일 — 둘 다 공유 메뉴가 입구입니다.\n\n"
                    "한 줄 요약은 Safari·메일·카톡 어디서나 5초 컷, "
                    "스크린샷 자동 분석은 GPT-4 Vision이 alt·캡션·파일명을 동시에. "
                    "블로그 부업하시는 분들껜 #2가 가장 큰 시간 회수입니다."
                ),
                "slides": [
                    "단축어 #1 — 긴 글 한 줄 요약 / 5초 컷",
                    "단축어 #2 — 스크린샷 자동 분석 / 150 → 15분",
                    "공통 핵심: 공유 메뉴 등록 → API Key 1회 → 테스트",
                    "단계별 캡처는 본문",
                ],
                "tags": [
                    "#아이폰단축어", "#GPT4Vision", "#스크린샷분석", "#alt텍스트", "#블로그부업",
                    "#한줄요약", "#AI자동화", "#iOS자동화", "#ChatGPT", "#OpenAI",
                    "#Anthropic", "#API", "#네이버블로그", "#aigrit", "#1인부업",
                    "#사이드잡", "#디지털노마드", "#생산성앱", "#아이폰활용", "#부업도구",
                ],
            },
            {
                "label": "Detail-2",
                "main": (
                    "단축어 #3·#4·#5 — 매일 짧게 쓰는 3종.\n\n"
                    "음성→Notion은 홈 화면 터치 한 번, 번역은 Cmd+C→단축키→Cmd+V, "
                    "캘린더는 한 문장 말하면 등록. Siri보다 정확하고 검색·반복 표현까지 정확하게 파싱."
                ),
                "slides": [
                    "단축어 #3 — 음성 → Notion / Whisper 받아쓰기",
                    "단축어 #4 — 초고속 번역 / 월 500원",
                    "단축어 #5 — 말로 캘린더 / 격주·다음 주 정확",
                    "단계별 셋업은 본문",
                ],
                "tags": [
                    "#아이폰단축어", "#Whisper", "#Notion", "#음성메모", "#번역단축키",
                    "#캘린더자동화", "#ClaudeHaiku", "#AI자동화", "#iOS자동화", "#Siri대체",
                    "#네이버블로그", "#aigrit", "#사이드잡", "#디지털노마드", "#1인부업",
                    "#부업도구", "#생산성앱", "#아이폰활용", "#직장인부업", "#원격업무",
                ],
            },
            {
                "label": "Cost-CTA",
                "main": (
                    "API 비용 진짜 얼마 나오나 + 무료로 쓰는 법.\n\n"
                    "일반 사용 월 1천~5천원, 헤비 사용도 1만원 수준. "
                    "결제 부담되시면 ① ChatGPT 앱 연동 ② 웹 URL 호출 두 가지 무료 옵션이 있어요. "
                    "주말 한나절이면 5개 다 만들 수 있습니다."
                ),
                "slides": [
                    "월 비용 1~5천원 / 헤비 1만원",
                    "무료법 ① ChatGPT 앱 / ② 웹 URL",
                    "주말 1회 셋업 → 평생 사용",
                    "다음 편 — Notion AI 부업 기반",
                ],
                "tags": [
                    "#아이폰단축어", "#API비용", "#무료자동화", "#ChatGPT앱", "#ClaudeHaiku",
                    "#AI자동화", "#iOS자동화", "#1인부업", "#사이드잡", "#디지털노마드",
                    "#네이버블로그", "#aigrit", "#아이폰활용", "#부업도구", "#생산성앱",
                    "#직장인부업", "#원격업무", "#이웃추가", "#NotionAI", "#예고편",
                ],
            },
        ],
        "threads": [
            {
                "label": "Hook",
                "body": (
                    "퇴근 후 40분 어디로 사라지셨나요?\n\n"
                    "출퇴근 지하철에서 뉴스 요약·번역·캘린더 입력만 하다 보면 시간이 다 갑니다. "
                    "아이폰 단축어 + AI로 자동화한 후 매일 40분이 회수됐어요. 5단축어 합하면 월 21시간.\n\n"
                    "→ blog.naver.com/aigrit/224263045957"
                ),
            },
            {
                "label": "TimeBack",
                "body": (
                    "월 21시간 회수가 어디서 오나, 분 단위로 분해.\n\n"
                    "스크린샷 자동 분석: 글 1편당 150분 → 15분 (압도적 1위)\n"
                    "한 줄 요약: 기사 20개 60분 → 10분\n"
                    "나머지 음성·번역·캘린더는 매일 짧게 합산.\n\n"
                    "→ blog.naver.com/aigrit/224263045957"
                ),
            },
            {
                "label": "Detail-1",
                "body": (
                    "단축어 #1 한 줄 요약 / #2 스크린샷 자동 분석 디테일.\n\n"
                    "둘 다 공유 메뉴가 입구. 한 줄 요약은 Safari·메일·카톡 어디서든 5초 컷. "
                    "스크린샷은 GPT-4 Vision이 alt·캡션·파일명까지 한 번에. 블로그 부업하시면 #2가 가장 큼.\n\n"
                    "→ blog.naver.com/aigrit/224263045957"
                ),
            },
            {
                "label": "Detail-2",
                "body": (
                    "단축어 #3 음성→Notion / #4 번역 / #5 캘린더 디테일.\n\n"
                    "음성은 홈 화면 터치 한 번 + Whisper 받아쓰기. 번역은 Cmd+C → 단축키 → Cmd+V 3초. "
                    "캘린더는 한 문장 말하면 등록 (Siri보다 정확).\n\n"
                    "→ blog.naver.com/aigrit/224263045957"
                ),
            },
            {
                "label": "Cost-CTA",
                "body": (
                    "API 비용 — 일반 월 1~5천원, 헤비도 1만원 수준.\n\n"
                    "결제 부담되시면 ① ChatGPT 앱 연동 ② 웹 URL 호출 두 가지 무료 옵션 있습니다. "
                    "주말 한나절이면 5개 다. 다음 편은 Notion AI 부업 기반.\n\n"
                    "→ blog.naver.com/aigrit/224263045957"
                ),
            },
        ],
        "tweets": [
            {
                "label": "Hook",
                "body": (
                    "퇴근 후 40분 어디로 사라졌나.\n"
                    "아이폰 단축어 + AI 5종으로 월 21시간 회수, 환산 5만~30만원.\n"
                    "단축어 1개 만드는 데 10분. 한 번 만들면 평생 작동.\n"
                    "→ blog.naver.com/aigrit/224263045957"
                ),
            },
            {
                "label": "TimeBack",
                "body": (
                    "월 21시간이 어디서 오나, 분해.\n"
                    "스크린샷 분석: 150 → 15분 (1위)\n"
                    "한 줄 요약: 60 → 10분 (2위)\n"
                    "음성·번역·캘린더는 매일 짧게 합산.\n"
                    "→ blog.naver.com/aigrit/224263045957"
                ),
            },
            {
                "label": "Detail-1",
                "body": (
                    "단축어 #1·#2 디테일.\n"
                    "한 줄 요약 — Safari·메일·카톡 5초 컷.\n"
                    "스크린샷 분석 — GPT-4 Vision이 alt·캡션·파일명 동시.\n"
                    "둘 다 공유 메뉴가 입구.\n"
                    "→ blog.naver.com/aigrit/224263045957"
                ),
            },
            {
                "label": "Detail-2",
                "body": (
                    "단축어 #3·#4·#5 디테일.\n"
                    "음성→Notion: Whisper + 홈 화면 터치 1번.\n"
                    "번역: Cmd+C→단축키→Cmd+V 3초, 월 500원.\n"
                    "캘린더: 한 문장 말하면 정확 파싱.\n"
                    "→ blog.naver.com/aigrit/224263045957"
                ),
            },
            {
                "label": "Cost-CTA",
                "body": (
                    "API 비용: 일반 월 1~5천원, 헤비 1만원.\n"
                    "무료 옵션 ① ChatGPT 앱 ② 웹 URL.\n"
                    "주말 한나절 셋업 → 평생.\n"
                    "다음 편 Notion AI 부업 기반.\n"
                    "→ blog.naver.com/aigrit/224263045957"
                ),
            },
        ],
    },
]


# ============================================================
# Driver
# ============================================================
def main() -> int:
    parser = argparse.ArgumentParser(description="Naver 에디션 SNS 자동 생성")
    parser.add_argument("--only", type=int, help="NAVER_SPECS 의 1-based index 만 생성")
    parser.add_argument("--slug", help="naver_no-slug 매칭 (예: 01-apple-shortcuts-50000won)")
    parser.add_argument("--list", action="store_true", help="등록된 SPEC 목록만 출력")
    args = parser.parse_args()

    if args.list:
        if not NAVER_SPECS:
            print("(빈 SPECS — 한 편도 등록되지 않았습니다)")
            return 0
        for i, s in enumerate(NAVER_SPECS, start=1):
            print(f"  [{i}] naver-{s['naver_no']}-{s['slug']}  ({s['title']})")
        return 0

    targets: list[dict] = []
    if args.only:
        if not (1 <= args.only <= len(NAVER_SPECS)):
            print(f"--only out of range (max={len(NAVER_SPECS)})", file=sys.stderr)
            return 1
        targets = [NAVER_SPECS[args.only - 1]]
    elif args.slug:
        targets = [
            s for s in NAVER_SPECS
            if f"{s['naver_no']}-{s['slug']}" == args.slug.removeprefix("naver-")
        ]
        if not targets:
            print(f"slug 매칭 실패: {args.slug}", file=sys.stderr)
            return 1
    else:
        targets = NAVER_SPECS

    if not targets:
        print("⚠ 생성할 SPEC 가 없습니다. NAVER_SPECS 에 항목을 추가하거나 --list 로 확인하세요.")
        return 0

    total_cards = 0
    for spec in targets:
        result = generate_post(spec)
        print(f"\n📦 {result['folder']}")
        for line in result["ig"]:
            print(f"  ✓ {line}")
        for line in result["x"]:
            print(f"  ✓ {line}")
        print(f"  ✓ ig-captions.md / threads.md / x.md / _meta.json")
        total_cards += result["meta"]["ig_cards_total"] + result["meta"]["x_images"]

    print(f"\n✅ {len(targets)}개 Naver 포스트 · 이미지 {total_cards}장 생성 완료.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
