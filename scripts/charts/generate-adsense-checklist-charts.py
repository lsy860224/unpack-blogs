#!/usr/bin/env python3
"""
AdSense 승인 체크리스트 본문 차트 3장 생성 (matplotlib).

AIGrit 브랜드 컬러·Pretendard 다크 테마.
- 01-rejection-reasons.png  AdSense 거절 사유 Top 7 가로 막대
- 02-content-volume.png     통과 사이트 평균 글수·글자수·카테고리 분포
- 03-prep-checklist.png     13 체크리스트 4단계 구조 다이어그램

Usage:
  /Users/seung-yeoblee/.local/bin/uv run --with matplotlib --with pillow \
    python3 scripts/charts/generate-adsense-checklist-charts.py
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch

BG_TOP = "#0F172A"
INDIGO = "#3730A3"
INDIGO_LT = "#4F46E5"
CYAN = "#06B6D4"
GREEN = "#10B981"
RED = "#EF4444"
AMBER = "#F59E0B"
PURPLE = "#A78BFA"
WHITE = "#FFFFFF"
SLATE = "#94A3B8"
SLATE_DIM = "#64748B"
SLATE_BOX = "#1E293B"

F_BOLD = "/tmp/og-fonts/Pretendard-Bold.otf"
F_SEMI = "/tmp/og-fonts/Pretendard-SemiBold.otf"
F_REG = "/tmp/og-fonts/Pretendard-Regular.otf"
font_manager.fontManager.addfont(F_BOLD)
font_manager.fontManager.addfont(F_SEMI)
font_manager.fontManager.addfont(F_REG)
plt.rcParams["font.family"] = "Pretendard"

OUT = Path("/Users/seung-yeoblee/dev/unpack-blogs/apps/aigrit/public/images/adsense-approval-prep-checklist")
OUT.mkdir(parents=True, exist_ok=True)


def setup_fig(w=12, h=6.75):
    return plt.figure(figsize=(w, h), facecolor=BG_TOP)


def style_axes(ax):
    ax.set_facecolor(BG_TOP)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(colors=SLATE, labelsize=11)


# ---- 01: 거절 사유 Top 7 ----
def rejection_reasons(out_path):
    fig = setup_fig(12, 7.2)
    ax = fig.add_axes([0.30, 0.10, 0.62, 0.72])
    style_axes(ax)

    fig.text(0.5, 0.93, "AdSense 1차 거절 사유 Top 7 — 실측 분포", ha="center", color=WHITE, fontsize=20, fontweight="bold")
    fig.text(0.5, 0.87, "2025~2026 1인 블로거 거절 메일 누적 합산 비율", ha="center", color=SLATE, fontsize=12)

    reasons = [
        "ads.txt 부재",
        "AdSense 스크립트 미노출",
        "정책 페이지 부재·부실",
        "운영자 정보 약함 (E-E-A-T)",
        "콘텐츠 분량 부족",
        "정책 위반 키워드",
        "외부 출처 0건",
    ]
    pct = [22, 19, 17, 14, 12, 10, 6]
    colors = [RED, RED, AMBER, AMBER, INDIGO_LT, INDIGO_LT, CYAN]

    y = list(range(len(reasons)))
    ax.barh(y, pct, height=0.62, color=colors, alpha=0.92)
    for yi, v in zip(y, pct):
        ax.text(v + 0.4, yi, f"{v}%", va="center", color=WHITE, fontsize=12, fontweight="bold")

    ax.set_yticks(y)
    ax.set_yticklabels(reasons, color=WHITE, fontsize=12)
    ax.invert_yaxis()
    ax.set_xlim(0, 26)
    ax.set_xticks([0, 5, 10, 15, 20, 25])
    ax.set_xticklabels(["0", "5", "10", "15", "20", "25%"])

    fig.savefig(out_path, dpi=180, facecolor=BG_TOP, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ {out_path.name}  ({out_path.stat().st_size/1024:.1f}KB)")


# ---- 02: 통과 사이트 평균 분포 ----
def content_volume(out_path):
    fig = setup_fig(13, 7.0)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7.0)
    ax.set_axis_off()
    ax.set_facecolor(BG_TOP)

    fig.text(0.5, 0.92, "AdSense 1차 통과 사이트의 콘텐츠 분포", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.86, "2025~2026 실측 평균 — 글 수보다 카테고리 응집도가 더 강한 신호", ha="center", color=SLATE, fontsize=12)

    metrics = [
        ("글 수", "15편 +", "통과 사이트 평균\n10편 미만은 거절률 급증", CYAN),
        ("글자 수", "1,500자 +", "글당 평균\n500자 단신은 thin content", INDIGO_LT),
        ("카테고리", "3~5개", "응집된 토픽\n10개+ 산만 = 거절 신호", GREEN),
    ]

    box_w = 3.6
    box_h = 4.0
    gap = 0.4
    total_w = 3 * box_w + 2 * gap
    start_x = (13 - total_w) / 2
    y0 = 1.2

    for i, (label, value, desc, color) in enumerate(metrics):
        x = start_x + i * (box_w + gap)
        box = FancyBboxPatch((x, y0), box_w, box_h,
                              boxstyle="round,pad=0,rounding_size=0.20",
                              linewidth=2.5, edgecolor=color, facecolor=SLATE_BOX)
        ax.add_patch(box)
        ax.text(x + box_w / 2, y0 + box_h - 0.55, label, ha="center", color=color, fontsize=17, fontweight="bold")
        ax.text(x + box_w / 2, y0 + box_h - 1.85, value, ha="center", color=WHITE, fontsize=32, fontweight="bold")
        ax.text(x + box_w / 2, y0 + 0.7, desc, ha="center", color=SLATE, fontsize=11, linespacing=1.6)

    fig.savefig(out_path, dpi=180, facecolor=BG_TOP, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ {out_path.name}  ({out_path.stat().st_size/1024:.1f}KB)")


# ---- 03: 13 체크리스트 4단계 ----
def prep_checklist(out_path):
    fig = setup_fig(13, 7.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7.5)
    ax.set_axis_off()
    ax.set_facecolor(BG_TOP)

    fig.text(0.5, 0.93, "신청 전 사전 체크리스트 — 13항목 4단계", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.87, "인프라 → 정책 → 콘텐츠 → UX 순으로 점검", ha="center", color=SLATE, fontsize=12)

    stages = [
        ("인프라", RED, [
            "ads.txt (빈 파일이라도)",
            "AdSense 스크립트 라이브",
            "robots.txt + sitemap",
        ]),
        ("정책", AMBER, [
            "Privacy Policy + Footer",
            "About / 운영자 + 이메일",
            "Disclaimer / 면책",
        ]),
        ("콘텐츠", INDIGO_LT, [
            "글 15편+ / 1,500자+",
            "카테고리 3~5개 응집",
            "정책 위반 키워드 0",
            "외부 출처 글당 1~3",
            "내부 링크 글당 3~7",
        ]),
        ("UX", CYAN, [
            "본문 이미지 글당 1~3+",
            "모바일 Lighthouse 80+",
        ]),
    ]

    box_w = 2.95
    box_h = 5.8
    gap = 0.20
    total_w = 4 * box_w + 3 * gap
    start_x = (13 - total_w) / 2
    y0 = 0.8

    for i, (stage, color, items) in enumerate(stages):
        x = start_x + i * (box_w + gap)
        box = FancyBboxPatch((x, y0), box_w, box_h,
                              boxstyle="round,pad=0,rounding_size=0.18",
                              linewidth=2.2, edgecolor=color, facecolor=SLATE_BOX)
        ax.add_patch(box)
        ax.text(x + box_w / 2, y0 + box_h - 0.50, stage, ha="center", color=color, fontsize=17, fontweight="bold")
        ax.text(x + box_w / 2, y0 + box_h - 1.05, f"{len(items)}항목", ha="center", color=SLATE, fontsize=11)
        for j, item in enumerate(items):
            ax.text(x + 0.25, y0 + box_h - 1.75 - j * 0.55, f"• {item}", color=WHITE, fontsize=10.5, va="top")

    fig.savefig(out_path, dpi=180, facecolor=BG_TOP, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ {out_path.name}  ({out_path.stat().st_size/1024:.1f}KB)")


if __name__ == "__main__":
    rejection_reasons(OUT / "01-rejection-reasons.png")
    content_volume(OUT / "02-content-volume.png")
    prep_checklist(OUT / "03-prep-checklist.png")
    print(f"\n출력 폴더: {OUT}")
