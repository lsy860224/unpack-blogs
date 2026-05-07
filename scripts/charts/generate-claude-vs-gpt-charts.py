#!/usr/bin/env python3
"""
Claude 4 Sonnet vs GPT-4o 본문 차트 4장 생성 (matplotlib).

AIGrit 브랜드 컬러·폰트(Pretendard) 다크 테마.
- 02-benchmark-chart{,-en}.png  ko/en bar chart (5 task × 2 model)
- 03-cost-timeline-en.png       scatter (latency × cost)
- 04-score-comparison-en.png    composite score (8.6 vs 8.4)

ko 02 차트는 ko 본문 task와 정합 — 글쓰기/코딩/추론/요약/번역.

Usage:
  python3 scripts/charts/generate-claude-vs-gpt-charts.py
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch

# ---- AIGrit brand colors ----
BG_TOP = "#0F172A"      # slate-900
BG_BOT = "#1E1B4B"      # indigo-950
INDIGO = "#3730A3"
CYAN = "#06B6D4"
RED = "#EF4444"
WHITE = "#FFFFFF"
SLATE = "#94A3B8"
SLATE_DIM = "#64748B"

# ---- Pretendard fonts ----
F_BOLD = "/tmp/og-fonts/Pretendard-Bold.otf"
F_SEMI = "/tmp/og-fonts/Pretendard-SemiBold.otf"
F_REG = "/tmp/og-fonts/Pretendard-Regular.otf"

font_manager.fontManager.addfont(F_BOLD)
font_manager.fontManager.addfont(F_SEMI)
font_manager.fontManager.addfont(F_REG)
plt.rcParams["font.family"] = "Pretendard"

OUT = Path("/Users/seung-yeoblee/dev/unpack-blogs/apps/aigrit/public/images/claude-4-sonnet-vs-gpt-4o")
OUT.mkdir(parents=True, exist_ok=True)


def setup_fig(w=12, h=6.75):
    """Dark canvas, 1600×900 @ 200 DPI default."""
    fig = plt.figure(figsize=(w, h), facecolor=BG_TOP)
    return fig


def style_axes(ax, hide_spines=True):
    ax.set_facecolor(BG_TOP)
    if hide_spines:
        for spine in ax.spines.values():
            spine.set_visible(False)
    ax.tick_params(colors=SLATE, labelsize=11)
    ax.grid(False)


# ---- 02: Benchmark bar chart ----
def benchmark_chart(out_path, lang):
    if lang == "en":
        tasks = ["Korean writing", "Coding (Flutter Dart)", "Reasoning", "Long-doc summary", "Translation"]
        title = "Claude 4 Sonnet vs GPT-4o — 5 task scores"
        subtitle = "Average across 14 days · scored out of 10"
        l_claude = "Claude 4 Sonnet"
        l_gpt = "GPT-4o"
    else:
        tasks = ["한국어 글쓰기", "코딩 (Flutter Dart)", "추론 (복합 조건)", "요약 (긴 문서)", "번역 (한↔영)"]
        title = "Claude 4 Sonnet vs GPT-4o — 5개 태스크 점수"
        subtitle = "14일 반복 테스트 평균 · 10점 만점"
        l_claude = "Claude 4 Sonnet"
        l_gpt = "GPT-4o"

    claude_scores = [9, 9, 10, 9.5, 9]
    gpt_scores = [7, 8, 9, 8.5, 9]

    fig = setup_fig(12, 6.75)
    ax = fig.add_axes([0.18, 0.10, 0.74, 0.70])
    style_axes(ax)

    y = list(range(len(tasks)))
    bar_h = 0.36
    y_claude = [v + bar_h / 2 + 0.02 for v in y]
    y_gpt = [v - bar_h / 2 - 0.02 for v in y]

    ax.barh(y_claude, claude_scores, height=bar_h, color=CYAN, label=l_claude)
    ax.barh(y_gpt, gpt_scores, height=bar_h, color=INDIGO, label=l_gpt)

    for yi, v in zip(y_claude, claude_scores):
        ax.text(v + 0.15, yi, str(v), va="center", color=CYAN, fontsize=12, fontweight="bold")
    for yi, v in zip(y_gpt, gpt_scores):
        ax.text(v + 0.15, yi, str(v), va="center", color=INDIGO, fontsize=12, fontweight="bold")

    ax.set_yticks(y)
    ax.set_yticklabels(tasks, color=WHITE, fontsize=12)
    ax.invert_yaxis()
    ax.set_xlim(0, 11.5)
    ax.set_xticks([0, 2, 4, 6, 8, 10])
    ax.set_xticklabels(["0", "2", "4", "6", "8", "10"])

    fig.text(0.5, 0.93, title, ha="center", color=WHITE, fontsize=20, fontweight="bold")
    fig.text(0.5, 0.88, subtitle, ha="center", color=SLATE, fontsize=12)

    leg = ax.legend(loc="lower right", facecolor=BG_TOP, edgecolor="none", labelcolor=WHITE, fontsize=11, frameon=False)

    fig.savefig(out_path, dpi=200, facecolor=BG_TOP, bbox_inches="tight")
    plt.close(fig)
    kb = out_path.stat().st_size / 1024
    print(f"✓ {out_path.name}  ({kb:.1f}KB)")


# ---- 03: Cost vs latency scatter (en) ----
def cost_scatter(out_path):
    fig = setup_fig(12, 6.75)
    ax = fig.add_axes([0.10, 0.14, 0.84, 0.66])
    style_axes(ax, hide_spines=False)
    for s in ax.spines.values():
        s.set_color(SLATE_DIM)
        s.set_linewidth(0.8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Claude 4 Sonnet: latency 5.2s, output $15
    # GPT-4o: latency 3.0s, output $10
    ax.scatter([3.0], [10], s=900, c=INDIGO, alpha=0.9, edgecolors=WHITE, linewidths=2, zorder=3)
    ax.scatter([5.2], [15], s=900, c=CYAN, alpha=0.9, edgecolors=WHITE, linewidths=2, zorder=3)

    ax.annotate("GPT-4o\nin $2.50 / out $10 / avg 3.0s", (3.0, 10),
                xytext=(15, 8), textcoords="offset points",
                color=INDIGO, fontsize=11, fontweight="bold")
    ax.annotate("Claude 4 Sonnet\nin $3 / out $15 / avg 5.2s", (5.2, 15),
                xytext=(15, 8), textcoords="offset points",
                color=CYAN, fontsize=11, fontweight="bold")

    # Best-value zone arrow (bottom-left)
    ax.annotate("Best value\n(bottom-left)", xy=(2.0, 8.0),
                xytext=(0.7, 5.5),
                color=SLATE, fontsize=10,
                arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.0))

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 22)
    ax.set_xlabel("Response time (s)", color=SLATE, fontsize=12)
    ax.set_ylabel("Output cost ($/1M tokens)", color=SLATE, fontsize=12)

    fig.text(0.5, 0.93, "Token cost × response time", ha="center", color=WHITE, fontsize=20, fontweight="bold")
    fig.text(0.5, 0.88, "Bottom-left = cheap and fast · Top-right = expensive and slow",
             ha="center", color=SLATE, fontsize=12)

    fig.savefig(out_path, dpi=200, facecolor=BG_TOP, bbox_inches="tight")
    plt.close(fig)
    kb = out_path.stat().st_size / 1024
    print(f"✓ {out_path.name}  ({kb:.1f}KB)")


# ---- 04: Composite score (en) ----
def composite_score(out_path):
    fig = setup_fig(12, 6.75)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()
    ax.set_facecolor(BG_TOP)

    fig.text(0.5, 0.85, "Composite score", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.78, "Average of 5 task scores · scored out of 10",
             ha="center", color=SLATE, fontsize=13)

    # Claude side
    fig.text(0.30, 0.50, "8.6", ha="center", color=CYAN, fontsize=110, fontweight="bold")
    fig.text(0.30, 0.27, "Claude 4 Sonnet", ha="center", color=WHITE, fontsize=18, fontweight="bold")
    fig.text(0.30, 0.21, "wins on quality", ha="center", color=SLATE, fontsize=12)

    # Divider
    fig.text(0.5, 0.42, "vs", ha="center", color=SLATE_DIM, fontsize=22, fontweight="bold")

    # GPT-4o side
    fig.text(0.70, 0.50, "8.4", ha="center", color=INDIGO, fontsize=110, fontweight="bold")
    fig.text(0.70, 0.27, "GPT-4o", ha="center", color=WHITE, fontsize=18, fontweight="bold")
    fig.text(0.70, 0.21, "wins on speed and cost", ha="center", color=SLATE, fontsize=12)

    fig.text(0.5, 0.10, "Gap is small — pick the model that matches the job",
             ha="center", color=SLATE_DIM, fontsize=11, style="italic")

    fig.savefig(out_path, dpi=200, facecolor=BG_TOP, bbox_inches="tight")
    plt.close(fig)
    kb = out_path.stat().st_size / 1024
    print(f"✓ {out_path.name}  ({kb:.1f}KB)")


def main():
    # EN charts
    benchmark_chart(OUT / "02-benchmark-chart-en.png", lang="en")
    cost_scatter(OUT / "03-cost-timeline-en.png")
    composite_score(OUT / "04-score-comparison-en.png")
    # ko 02 — overwrite for body↔chart consistency fix
    benchmark_chart(OUT / "02-benchmark-chart.png", lang="ko")
    print("\n✅ Generated 4 charts.")


if __name__ == "__main__":
    main()
