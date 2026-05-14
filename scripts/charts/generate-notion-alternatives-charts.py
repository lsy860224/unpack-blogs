#!/usr/bin/env python3
"""
Notion 대체 앱 BEST 5 본문 차트 4장 생성 (matplotlib).

AIGrit 브랜드 컬러·Pretendard 다크 테마.
- 01-five-apps-overview.png    5개 앱 5박스 한눈 비교
- 03-comparison-matrix.png     로컬↔클라우드 × 글쓰기↔DB scatter
- 04-user-type-decision.png    사용자 유형 × 앱 매핑 매트릭스
- 05-cluster-positioning.png   데이터 소유권 × 협업 scatter

Usage:
  python3 scripts/charts/generate-notion-alternatives-charts.py
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

OUT = Path("/Users/seung-yeoblee/dev/unpack-blogs/apps/aigrit/public/images/notion-alternatives-best-5")
OUT.mkdir(parents=True, exist_ok=True)


def setup_fig(w=12, h=6.75):
    return plt.figure(figsize=(w, h), facecolor=BG_TOP)


def style_axes(ax):
    ax.set_facecolor(BG_TOP)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(colors=SLATE, labelsize=11)


# ---- 01: 5 app overview boxes ----
def five_apps_overview(out_path):
    fig = setup_fig(13, 7.3)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7.3)
    ax.set_axis_off()
    ax.set_facecolor(BG_TOP)

    fig.text(0.5, 0.92, "Notion 대체 앱 BEST 5 — 1년 실측 한눈", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.86, "5개 앱 모두 메인 자리에 올려본 결과 — 같은 카테고리지만 해결하는 문제가 다르다", ha="center", color=SLATE, fontsize=12)

    apps = [
        ("Obsidian", "로컬 마크다운\n평생 보관", "0원~", CYAN),
        ("Craft", "Apple 글쓰기\n복붙·디자인", "무료~$5", INDIGO_LT),
        ("Logseq", "데일리 노트\n아웃라이너", "완전 무료", GREEN),
        ("Anytype", "Notion 클론\nOSS·P2P", "무료~", PURPLE),
        ("Capacities", "객체 기반\n캘린더 통합", "무료~$10", AMBER),
    ]

    box_w = 2.2
    box_h = 3.5
    gap = 0.25
    total_w = 5 * box_w + 4 * gap
    start_x = (13 - total_w) / 2
    y0 = 1.3

    for i, (name, desc, price, color) in enumerate(apps):
        x = start_x + i * (box_w + gap)
        box = FancyBboxPatch((x, y0), box_w, box_h,
                              boxstyle="round,pad=0,rounding_size=0.18",
                              linewidth=2, edgecolor=color, facecolor=SLATE_BOX)
        ax.add_patch(box)
        ax.text(x + box_w / 2, y0 + box_h - 0.5, name, ha="center", color=color, fontsize=18, fontweight="bold")
        ax.text(x + box_w / 2, y0 + box_h - 1.5, desc, ha="center", color=WHITE, fontsize=12, linespacing=1.6)
        ax.text(x + box_w / 2, y0 + 0.55, price, ha="center", color=SLATE, fontsize=11, fontweight="bold")

    fig.savefig(out_path, dpi=180, facecolor=BG_TOP, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ {out_path.name}  ({out_path.stat().st_size/1024:.1f}KB)")


# ---- 03: X local↔cloud × Y writing↔DB scatter ----
def comparison_matrix(out_path):
    fig = setup_fig(12, 7.0)
    ax = fig.add_axes([0.10, 0.13, 0.84, 0.70])
    style_axes(ax)

    fig.text(0.5, 0.94, "5개 앱 비교 매트릭스", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.88, "가로: 로컬 ↔ 클라우드 / 세로: 글쓰기 ↔ DB 중심", ha="center", color=SLATE, fontsize=12)

    apps = [
        ("Obsidian", 0.10, 0.30, CYAN),
        ("Craft", 0.30, 0.20, INDIGO_LT),
        ("Logseq", 0.15, 0.55, GREEN),
        ("Anytype", 0.25, 0.80, PURPLE),
        ("Capacities", 0.78, 0.85, AMBER),
        ("Notion", 0.90, 0.95, RED),
    ]

    for name, x, y, color in apps:
        ax.scatter([x], [y], s=600, c=color, alpha=0.9, edgecolors=WHITE, linewidths=2, zorder=3)
        ax.text(x + 0.02, y + 0.03, name, color=color, fontsize=13, fontweight="bold")

    ax.axhline(0.5, color=SLATE_DIM, linewidth=0.7, linestyle="--", alpha=0.6)
    ax.axvline(0.5, color=SLATE_DIM, linewidth=0.7, linestyle="--", alpha=0.6)

    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.1)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["로컬 우선", "클라우드 우선"], color=WHITE, fontsize=12)
    ax.set_yticks([0.05, 1.0])
    ax.set_yticklabels(["글쓰기 중심", "DB 중심"], color=WHITE, fontsize=12)

    ax.text(0.02, 1.04, "로컬 + DB", color=SLATE, fontsize=10, alpha=0.7)
    ax.text(0.78, 1.04, "클라우드 + DB", color=SLATE, fontsize=10, alpha=0.7)
    ax.text(0.02, -0.02, "로컬 + 글쓰기", color=SLATE, fontsize=10, alpha=0.7)
    ax.text(0.74, -0.02, "클라우드 + 글쓰기", color=SLATE, fontsize=10, alpha=0.7)

    fig.savefig(out_path, dpi=180, facecolor=BG_TOP, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ {out_path.name}  ({out_path.stat().st_size/1024:.1f}KB)")


# ---- 04: User type × app matrix ----
def user_type_decision(out_path):
    fig = setup_fig(13, 7.5)
    ax = fig.add_axes([0.20, 0.10, 0.75, 0.78])
    style_axes(ax)

    fig.text(0.5, 0.94, "사용자 유형별 추천 앱", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.89, "6가지 유형 × 6개 앱 — 큰 점은 최우선, 흐린 점은 보조", ha="center", color=SLATE, fontsize=12)

    user_types = [
        "Apple+글쓰기",
        "데이터 소유권",
        "데일리·메모",
        "Notion 그대로",
        "위키+일기",
        "팀 5명+",
    ]
    apps = ["Obsidian", "Craft", "Logseq", "Anytype", "Capacities", "Notion"]

    # 0=빈칸, 1=보조(◐), 2=최우선(●)
    matrix = [
        [1, 2, 0, 0, 0, 0],
        [2, 0, 1, 1, 0, 0],
        [1, 0, 2, 0, 1, 0],
        [0, 0, 0, 2, 0, 1],
        [1, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 2],
    ]

    colors = [CYAN, INDIGO_LT, GREEN, PURPLE, AMBER, RED]

    n_y = len(user_types)
    n_x = len(apps)
    for yi in range(n_y):
        for xi in range(n_x):
            val = matrix[yi][xi]
            if val == 2:
                ax.scatter([xi], [n_y - 1 - yi], s=520, c=colors[xi], alpha=0.95, edgecolors=WHITE, linewidths=1.5, zorder=3)
            elif val == 1:
                ax.scatter([xi], [n_y - 1 - yi], s=260, c=colors[xi], alpha=0.45, edgecolors=colors[xi], linewidths=1.2, zorder=2)

    ax.set_xticks(range(n_x))
    ax.set_xticklabels(apps, color=WHITE, fontsize=12, fontweight="bold")
    ax.set_yticks(range(n_y))
    ax.set_yticklabels(list(reversed(user_types)), color=WHITE, fontsize=12)
    ax.set_xlim(-0.6, n_x - 0.4)
    ax.set_ylim(-0.6, n_y - 0.4)

    for y in [0.5 + i for i in range(n_y - 1)]:
        ax.axhline(y, color=SLATE_DIM, linewidth=0.4, alpha=0.3)
    for x in [0.5 + i for i in range(n_x - 1)]:
        ax.axvline(x, color=SLATE_DIM, linewidth=0.4, alpha=0.3)

    fig.savefig(out_path, dpi=180, facecolor=BG_TOP, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ {out_path.name}  ({out_path.stat().st_size/1024:.1f}KB)")


# ---- 05: ownership × collaboration scatter ----
def cluster_positioning(out_path):
    fig = setup_fig(12, 7.0)
    ax = fig.add_axes([0.10, 0.13, 0.84, 0.70])
    style_axes(ax)

    fig.text(0.5, 0.94, "데이터 소유권 × 협업 — 5개 앱 위치", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.88, "가로: 데이터 소유권 / 세로: 협업 강도 — 본인 사분면 선택", ha="center", color=SLATE, fontsize=12)

    apps = [
        ("Obsidian", 0.95, 0.20, CYAN),
        ("Craft", 0.40, 0.50, INDIGO_LT),
        ("Logseq", 0.90, 0.15, GREEN),
        ("Anytype", 0.85, 0.40, PURPLE),
        ("Capacities", 0.25, 0.55, AMBER),
        ("Notion", 0.10, 0.95, RED),
    ]

    for name, x, y, color in apps:
        ax.scatter([x], [y], s=700, c=color, alpha=0.9, edgecolors=WHITE, linewidths=2, zorder=3)
        ax.text(x + 0.02, y + 0.04, name, color=color, fontsize=13, fontweight="bold")

    ax.axhline(0.5, color=SLATE_DIM, linewidth=0.7, linestyle="--", alpha=0.6)
    ax.axvline(0.5, color=SLATE_DIM, linewidth=0.7, linestyle="--", alpha=0.6)

    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.1)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["클라우드 종속", "내 데이터 우선"], color=WHITE, fontsize=12)
    ax.set_yticks([0.05, 1.0])
    ax.set_yticklabels(["혼자", "팀 협업"], color=WHITE, fontsize=12)

    ax.text(0.02, 1.04, "협업 강·클라우드", color=SLATE, fontsize=10, alpha=0.7)
    ax.text(0.78, 1.04, "협업 강·소유권", color=SLATE, fontsize=10, alpha=0.7)
    ax.text(0.02, -0.02, "혼자·클라우드", color=SLATE, fontsize=10, alpha=0.7)
    ax.text(0.78, -0.02, "혼자·소유권", color=SLATE, fontsize=10, alpha=0.7)

    fig.savefig(out_path, dpi=180, facecolor=BG_TOP, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ {out_path.name}  ({out_path.stat().st_size/1024:.1f}KB)")


# ---- 02: AI integration depth bar chart ----
def ai_integration_chart(out_path):
    fig = setup_fig(12, 6.75)
    ax = fig.add_axes([0.22, 0.13, 0.70, 0.68])
    style_axes(ax)

    fig.text(0.5, 0.93, "2026년 5월 — 노트앱별 AI 통합도", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.86, "공식 통합·플러그인·LLM 자유도 종합 점수 (10점 만점)", ha="center", color=SLATE, fontsize=12)

    apps = ["Notion", "Obsidian", "Capacities", "Craft", "Anytype", "Logseq"]
    scores = [9.5, 9.0, 7.0, 6.5, 4.0, 5.5]
    colors = [RED, CYAN, AMBER, INDIGO_LT, PURPLE, GREEN]
    notes = [
        "공식 Notion AI — 가장 매끄러움",
        "Smart Connections·Copilot 플러그인",
        "AI Assistant 내장 + 객체 기반",
        "공식 MCP·AI 어시스턴트",
        "공식 AI는 아직 초기",
        "커뮤니티 플러그인 의존",
    ]

    y = list(range(len(apps)))
    ax.barh(y, scores, height=0.62, color=colors, alpha=0.9)
    for yi, v, note in zip(y, scores, notes):
        ax.text(v + 0.15, yi, f"{v}  ·  {note}", va="center", color=WHITE, fontsize=11)

    ax.set_yticks(y)
    ax.set_yticklabels(apps, color=WHITE, fontsize=13, fontweight="bold")
    ax.invert_yaxis()
    ax.set_xlim(0, 14)
    ax.set_xticks([0, 2, 4, 6, 8, 10])
    ax.set_xticklabels(["0", "2", "4", "6", "8", "10"])

    fig.savefig(out_path, dpi=180, facecolor=BG_TOP, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ {out_path.name}  ({out_path.stat().st_size/1024:.1f}KB)")


if __name__ == "__main__":
    five_apps_overview(OUT / "01-five-apps-overview.png")
    ai_integration_chart(OUT / "02-ai-integration-depth.png")
    comparison_matrix(OUT / "03-comparison-matrix.png")
    user_type_decision(OUT / "04-user-type-decision.png")
    cluster_positioning(OUT / "05-cluster-positioning.png")
    print(f"\n출력 폴더: {OUT}")
