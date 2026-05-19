#!/usr/bin/env python3
"""
babipanote — sprint-week4-review 본문 차트 1장 생성.

W22 1주에 머지된 13 PR을 4개 그룹(P0·P1 콘텐츠·P1 UX·보조)으로 분류한
박스 다이어그램. babipanote 종이 톤 (Plum + Terracotta).

Usage:
  /Users/seung-yeoblee/.local/bin/uv run --with matplotlib --with pillow \
    python3 scripts/charts/generate-sprint-week4-chart.py
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch

BG_PAPER = "#F7F1E8"
PLUM = "#6B2C5C"
TERRACOTTA = "#C75B3F"
INK = "#2D2419"
INK_DIM = "#8B7D6B"
GREEN = "#3F7D58"
AMBER = "#C89F4A"
RED = "#C75B3F"
PURPLE_DEEP = "#5A2B5A"

F_BOLD = "/tmp/og-fonts/GowunBatang-Bold.ttf"
F_REG = "/tmp/og-fonts/GowunBatang-Regular.ttf"
F_PRET_BOLD = "/tmp/og-fonts/Pretendard-Bold.otf"
F_PRET_REG = "/tmp/og-fonts/Pretendard-Regular.otf"
for f in (F_BOLD, F_REG, F_PRET_BOLD, F_PRET_REG):
    font_manager.fontManager.addfont(f)
plt.rcParams["font.family"] = "Pretendard"

OUT = Path("/Users/seung-yeoblee/dev/unpack-blogs/apps/babipanote/public/images/sprint-week4-review")
OUT.mkdir(parents=True, exist_ok=True)


def prs_timeline(out_path):
    fig = plt.figure(figsize=(13, 7.0), facecolor=BG_PAPER)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7.0)
    ax.set_axis_off()
    ax.set_facecolor(BG_PAPER)

    fig.text(0.5, 0.92, "W22 sprint — 1주 13 PR 분류", ha="center", color=INK, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.86, "단일 책임 원칙으로 PR 분리 — 각 PR이 다음 PR의 base를 깨뜨리지 않도록", ha="center", color=INK_DIM, fontsize=12)

    groups = [
        ("P0 보안·인프라·SEO schema", "5 PR · #34·#35·#36·#37·#38",
         "Next.js 16.2.6·favicon·manifest·EN 카테고리\nFAQ + BreadcrumbList JSON-LD·regex fix", GREEN),
        ("P1 콘텐츠 구조", "2 PR · #39·#40",
         "AI 코딩 Pillar 신규 작성 (cluster 4편 보조)\nhello-world 3,067자 확장·카테고리 4→3 통합·301 redirect", AMBER),
        ("P1 UX·E-E-A-T", "3 PR · #41·#42·#43",
         "404 nav + GA4 광고 시그널 + About 경력 보강\n고아 글 백링크 + MDX img lazy·async decoding", PLUM),
        ("보조 (hot fix · 누락분)", "포함 PR · lint·FAQ regex·obsidian-getting-started",
         "ESLint 따옴표 escape·JS regex \\b 한국어 매칭\n지식관리 cluster Pillar 백링크 누락분", TERRACOTTA),
    ]

    box_w = 11.5
    box_h = 1.2
    gap = 0.18
    x0 = (13 - box_w) / 2
    y_start = 5.0

    for i, (label, prs, desc, color) in enumerate(groups):
        y = y_start - i * (box_h + gap)
        box = FancyBboxPatch((x0, y), box_w, box_h,
                              boxstyle="round,pad=0,rounding_size=0.16",
                              linewidth=2.2, edgecolor=color, facecolor="#FFFFFF")
        ax.add_patch(box)
        ax.text(x0 + 0.4, y + box_h - 0.32, label, color=color, fontsize=14, fontweight="bold", va="top")
        ax.text(x0 + 0.4, y + box_h - 0.66, prs, color=INK_DIM, fontsize=10.5, va="top", style="italic")
        ax.text(x0 + 0.4, y + 0.18, desc, color=INK, fontsize=10.5, va="bottom", linespacing=1.5)

    fig.text(0.5, 0.05, "총 13 PR · 자가점검 5 FAIL 시발점 → AdSense 신청 직전 상태로 정리",
             ha="center", color=INK_DIM, fontsize=10, style="italic")

    fig.savefig(out_path, dpi=180, facecolor=BG_PAPER, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ {out_path.name}  ({out_path.stat().st_size/1024:.1f}KB)")


if __name__ == "__main__":
    prs_timeline(OUT / "01-13-prs-timeline.png")
