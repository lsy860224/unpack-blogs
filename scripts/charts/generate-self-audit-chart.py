#!/usr/bin/env python3
"""
babipanote — wrote-adsense-guide-found-5-fails 본문 차트 1장 생성.

babipanote 브랜드 컬러 (Plum + Terracotta) · Gowun Batang 세리프.

Usage:
  /Users/seung-yeoblee/.local/bin/uv run --with matplotlib --with pillow \
    python3 scripts/charts/generate-self-audit-chart.py
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch

# babipanote palette
BG_PAPER = "#F7F1E8"   # warm paper
PLUM = "#6B2C5C"
TERRACOTTA = "#C75B3F"
INK = "#2D2419"
INK_DIM = "#8B7D6B"
GREEN = "#3F7D58"
AMBER = "#C89F4A"
RED = "#C75B3F"

F_BOLD = "/tmp/og-fonts/GowunBatang-Bold.ttf"
F_REG = "/tmp/og-fonts/GowunBatang-Regular.ttf"
F_PRET_BOLD = "/tmp/og-fonts/Pretendard-Bold.otf"
F_PRET_REG = "/tmp/og-fonts/Pretendard-Regular.otf"
for f in (F_BOLD, F_REG, F_PRET_BOLD, F_PRET_REG):
    font_manager.fontManager.addfont(f)
plt.rcParams["font.family"] = "Pretendard"

OUT = Path("/Users/seung-yeoblee/dev/unpack-blogs/apps/babipanote/public/images/wrote-adsense-guide-found-5-fails")
OUT.mkdir(parents=True, exist_ok=True)


def audit_result(out_path):
    fig = plt.figure(figsize=(13, 7.0), facecolor=BG_PAPER)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7.0)
    ax.set_axis_off()
    ax.set_facecolor(BG_PAPER)

    fig.text(0.5, 0.92, "W21 자가점검 결과 — AIGrit ko 18편 전수 검증", ha="center", color=INK, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.86, "직접 만든 체크리스트 13항목을, 직접 발행한 글 18편에 적용", ha="center", color=INK_DIM, fontsize=12)

    buckets = [
        ("PASS", "1편", "모든 기준 통과", GREEN, "solo-developer-automation-stack"),
        ("WARN", "11편", "분량·H2·물음표 등\n구조 경고", AMBER, "주로 H2 과다·FAQ 형식"),
        ("FAIL", "5편", "broken link·image\n또는 이미지 0장", RED, "발행 차단 사유"),
    ]

    box_w = 3.6
    box_h = 4.4
    gap = 0.4
    total_w = 3 * box_w + 2 * gap
    start_x = (13 - total_w) / 2
    y0 = 1.0

    for i, (label, value, desc, color, note) in enumerate(buckets):
        x = start_x + i * (box_w + gap)
        box = FancyBboxPatch((x, y0), box_w, box_h,
                              boxstyle="round,pad=0,rounding_size=0.20",
                              linewidth=2.5, edgecolor=color, facecolor="#FFFFFF")
        ax.add_patch(box)
        ax.text(x + box_w / 2, y0 + box_h - 0.55, label, ha="center", color=color, fontsize=18, fontweight="bold")
        ax.text(x + box_w / 2, y0 + box_h - 1.85, value, ha="center", color=INK, fontsize=36, fontweight="bold")
        ax.text(x + box_w / 2, y0 + box_h - 3.10, desc, ha="center", color=INK, fontsize=12, linespacing=1.6)
        ax.text(x + box_w / 2, y0 + 0.55, note, ha="center", color=INK_DIM, fontsize=10, style="italic")

    fig.savefig(out_path, dpi=180, facecolor=BG_PAPER, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ {out_path.name}  ({out_path.stat().st_size/1024:.1f}KB)")


if __name__ == "__main__":
    audit_result(OUT / "01-audit-result.png")
    print(f"\n출력 폴더: {OUT}")
