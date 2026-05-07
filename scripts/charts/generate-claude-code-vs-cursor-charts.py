#!/usr/bin/env python3
"""
Claude Code vs Cursor 본문 차트 3장 영문판 생성 (matplotlib).

AIGrit 브랜드 컬러·Pretendard 다크 테마.
- 02-workflow-comparison-en.png  좌우 워크플로우 비교 (5 step × 2 tool)
- scenarios-comparison-en.png    4 scenario 시간 비교 bar chart
- 03-use-case-matrix-en.png      5 scenario × winner matrix table

Usage:
  python3 scripts/charts/generate-claude-code-vs-cursor-charts.py
"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager
import numpy as np

# ---- AIGrit brand colors ----
BG = "#0F172A"
INDIGO = "#3730A3"
INDIGO_LIGHT = "#6366F1"
CYAN = "#06B6D4"
CYAN_LIGHT = "#22D3EE"
WHITE = "#FFFFFF"
SLATE = "#94A3B8"
SLATE_DIM = "#64748B"
PANEL = "#1E293B"
GREEN = "#10B981"

# ---- Fonts ----
F_BOLD = "/tmp/og-fonts/Pretendard-Bold.otf"
F_SEMI = "/tmp/og-fonts/Pretendard-SemiBold.otf"
F_REG = "/tmp/og-fonts/Pretendard-Regular.otf"
font_manager.fontManager.addfont(F_BOLD)
font_manager.fontManager.addfont(F_SEMI)
font_manager.fontManager.addfont(F_REG)
plt.rcParams["font.family"] = "Pretendard"

OUT = Path("/Users/seung-yeoblee/dev/unpack-blogs/apps/aigrit/public/images/claude-code-vs-cursor")
OUT.mkdir(parents=True, exist_ok=True)


def setup(w=12, h=6.75):
    return plt.figure(figsize=(w, h), facecolor=BG)


def style_off(ax):
    ax.set_facecolor(BG)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])


# ---- 02: Workflow comparison (left/right boxes with steps) ----
def workflow_comparison(out_path):
    fig = setup(13.5, 7.5)
    ax = fig.add_axes([0, 0, 1, 1])
    style_off(ax)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    fig.text(0.5, 0.94, "Claude Code vs Cursor — Workflow structure",
             ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.89, "Same AI coding job, different shape of intervention",
             ha="center", color=SLATE, fontsize=13)

    # Left panel: Claude Code
    left = mpatches.FancyBboxPatch(
        (4, 8), 44, 70, boxstyle="round,pad=1.5,rounding_size=2",
        linewidth=2, edgecolor=CYAN, facecolor=PANEL,
    )
    ax.add_patch(left)

    ax.text(26, 76, "Claude Code — CLI", ha="center", color=CYAN,
            fontsize=18, fontweight="bold")
    ax.text(26, 71, "Terminal-native · project-wide context",
            ha="center", color=SLATE, fontsize=11)

    claude_steps = [
        "1. Prompt input",
        "2. CLAUDE.md auto-loaded",
        "3. Multi-file edit in one pass",
        "4. Chains build · test runs",
        "5. Suggests git commit",
    ]
    y = 62
    for s in claude_steps:
        step_box = mpatches.FancyBboxPatch(
            (8, y - 4), 36, 7, boxstyle="round,pad=0.4,rounding_size=1.2",
            linewidth=1, edgecolor=CYAN, facecolor=BG,
        )
        ax.add_patch(step_box)
        ax.text(26, y - 0.5, s, ha="center", color=WHITE, fontsize=12, fontweight="semibold")
        y -= 9

    # Right panel: Cursor
    right = mpatches.FancyBboxPatch(
        (52, 8), 44, 70, boxstyle="round,pad=1.5,rounding_size=2",
        linewidth=2, edgecolor=INDIGO_LIGHT, facecolor=PANEL,
    )
    ax.add_patch(right)

    ax.text(74, 76, "Cursor — IDE", ha="center", color=INDIGO_LIGHT,
            fontsize=18, fontweight="bold")
    ax.text(74, 71, "Editor-native · file-level intervention",
            ha="center", color=SLATE, fontsize=11)

    cursor_steps = [
        "1. Open the file",
        "2. Cmd+K inline / Cmd+L chat",
        "3. AI edits selection only",
        "4. Diff review → Accept",
        "5. Move to next file",
    ]
    y = 62
    for s in cursor_steps:
        step_box = mpatches.FancyBboxPatch(
            (56, y - 4), 36, 7, boxstyle="round,pad=0.4,rounding_size=1.2",
            linewidth=1, edgecolor=INDIGO_LIGHT, facecolor=BG,
        )
        ax.add_patch(step_box)
        ax.text(74, y - 0.5, s, ha="center", color=WHITE, fontsize=12, fontweight="semibold")
        y -= 9

    # Bottom verdict band
    bottom = mpatches.FancyBboxPatch(
        (4, 1), 92, 4.5, boxstyle="round,pad=0.4,rounding_size=1",
        linewidth=1, edgecolor=SLATE_DIM, facecolor=PANEL,
    )
    ax.add_patch(bottom)
    ax.text(50, 3.2,
            "Claude Code = large or new features · Cursor = small or exploratory · best when run in parallel",
            ha="center", color=SLATE, fontsize=11)

    fig.savefig(out_path, dpi=200, facecolor=BG, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ {out_path.name}  ({out_path.stat().st_size / 1024:.1f}KB)")


# ---- scenarios bar chart (4 timed scenarios) ----
def scenarios_chart(out_path):
    scenarios = [
        "New feature\n(Flutter widget)",
        "Bug fix",
        "Refactor\n(158 tests)",
        "Repetitive task\n(i18n × 50 strings)",
    ]
    claude_min = [25, 3, 15, 3]
    cursor_min = [55, 8, 40, 12]

    fig = setup(13.5, 7.5)
    ax = fig.add_axes([0.10, 0.14, 0.86, 0.66])
    ax.set_facecolor(BG)
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    for s in ["left", "bottom"]:
        ax.spines[s].set_color(SLATE_DIM)

    x = np.arange(len(scenarios))
    bw = 0.36
    ax.bar(x - bw / 2 - 0.02, claude_min, bw, color=CYAN, label="Claude Code")
    ax.bar(x + bw / 2 + 0.02, cursor_min, bw, color=INDIGO_LIGHT, label="Cursor")

    for xi, v in zip(x, claude_min):
        ax.text(xi - bw / 2 - 0.02, v + 1.3, f"{v} min",
                ha="center", color=CYAN, fontsize=11, fontweight="bold")
    for xi, v in zip(x, cursor_min):
        ax.text(xi + bw / 2 + 0.02, v + 1.3, f"{v} min",
                ha="center", color=INDIGO_LIGHT, fontsize=11, fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(scenarios, color=WHITE, fontsize=11)
    ax.tick_params(axis="y", colors=SLATE, labelsize=10)
    ax.set_ylabel("Time to complete (minutes)", color=SLATE, fontsize=12)
    ax.set_ylim(0, max(cursor_min) + 12)
    ax.grid(axis="y", color=SLATE_DIM, alpha=0.2, linewidth=0.6)

    fig.text(0.5, 0.92, "Which AI coding tool wins which scenario?",
             ha="center", color=WHITE, fontsize=20, fontweight="bold")
    fig.text(0.5, 0.87, "Lower bar = faster · 4 timed scenarios from a 14-day cross-test",
             ha="center", color=SLATE, fontsize=12)

    leg = ax.legend(loc="upper right", facecolor=BG, edgecolor="none",
                    labelcolor=WHITE, fontsize=11, frameon=False)

    fig.savefig(out_path, dpi=200, facecolor=BG, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ {out_path.name}  ({out_path.stat().st_size / 1024:.1f}KB)")


# ---- 03: Use-case matrix (5 scenarios × winner) ----
def use_case_matrix(out_path):
    rows = [
        ("Large new feature build",     "Claude", "Aux", "Multi-file consistency = Claude"),
        ("Small code edit",              "Aux",    "Cursor", "Inline Cmd+K is faster"),
        ("Error debugging exploration",  "Claude", "Aux", "Logs + file trace chain"),
        ("UI component markup",          "Aux",    "Cursor", "Live preview side-by-side"),
        ("Refactor / rename",            "Claude", "Aux", "Project-wide search + bulk edit"),
    ]

    fig = setup(13.5, 7.5)
    ax = fig.add_axes([0.04, 0.06, 0.92, 0.78])
    style_off(ax)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    # Column headers
    headers = [("Scenario", 4, 28), ("Claude Code", 32, 50), ("Cursor", 54, 70), ("Why", 72, 96)]
    header_y = 92
    for h, x0, x1 in headers:
        if h == "Claude Code":
            color = CYAN
        elif h == "Cursor":
            color = INDIGO_LIGHT
        else:
            color = SLATE
        ax.text((x0 + x1) / 2, header_y, h, ha="center", color=color,
                fontsize=14, fontweight="bold")

    # Header divider
    ax.plot([4, 96], [88, 88], color=SLATE_DIM, linewidth=1)

    # Rows
    row_h = 14
    y = 80
    for i, (scen, claude, cursor, why) in enumerate(rows):
        bg_color = PANEL if i % 2 == 0 else BG
        rect = mpatches.FancyBboxPatch(
            (4, y - row_h + 1), 92, row_h - 1,
            boxstyle="round,pad=0.2,rounding_size=0.6",
            linewidth=0, facecolor=bg_color, alpha=0.6,
        )
        ax.add_patch(rect)

        ax.text(16, y - row_h / 2 + 1, scen, ha="center", va="center",
                color=WHITE, fontsize=12, fontweight="semibold")

        # Claude pill
        c_color = CYAN if claude == "Claude" else SLATE_DIM
        c_text = "WINS" if claude == "Claude" else "Aux"
        pill_c = mpatches.FancyBboxPatch(
            (37, y - row_h / 2 - 1.5), 8, 4,
            boxstyle="round,pad=0.3,rounding_size=2",
            linewidth=0, facecolor=c_color, alpha=0.85 if claude == "Claude" else 0.4,
        )
        ax.add_patch(pill_c)
        ax.text(41, y - row_h / 2 + 0.5, c_text, ha="center", va="center",
                color=BG if claude == "Claude" else WHITE,
                fontsize=10, fontweight="bold")

        # Cursor pill
        u_color = INDIGO_LIGHT if cursor == "Cursor" else SLATE_DIM
        u_text = "WINS" if cursor == "Cursor" else "Aux"
        pill_u = mpatches.FancyBboxPatch(
            (58, y - row_h / 2 - 1.5), 8, 4,
            boxstyle="round,pad=0.3,rounding_size=2",
            linewidth=0, facecolor=u_color, alpha=0.85 if cursor == "Cursor" else 0.4,
        )
        ax.add_patch(pill_u)
        ax.text(62, y - row_h / 2 + 0.5, u_text, ha="center", va="center",
                color=BG if cursor == "Cursor" else WHITE,
                fontsize=10, fontweight="bold")

        ax.text(73, y - row_h / 2 + 1, why, ha="left", va="center",
                color=SLATE, fontsize=10)

        y -= row_h

    fig.text(0.5, 0.94, "5-scenario winner matrix",
             ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.89, "Based on 14-day cross-tests on real shipping projects",
             ha="center", color=SLATE, fontsize=12)

    fig.savefig(out_path, dpi=200, facecolor=BG, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ {out_path.name}  ({out_path.stat().st_size / 1024:.1f}KB)")


def main():
    workflow_comparison(OUT / "02-workflow-comparison-en.png")
    scenarios_chart(OUT / "scenarios-comparison-en.png")
    use_case_matrix(OUT / "03-use-case-matrix-en.png")
    print("\n✅ Generated 3 EN charts.")


if __name__ == "__main__":
    main()
