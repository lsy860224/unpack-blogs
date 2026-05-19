#!/usr/bin/env python3
"""
AI 코딩 완벽 가이드 2026 Pillar 본문 차트 5장 생성.

AIGrit 브랜드 컬러·Pretendard 다크 테마.

- 01-tools-matrix         4-quadrant 도구 매트릭스 (CLI vs IDE × 단일 vs 프로젝트)
- 02-cli-vs-ide           Claude Code vs Cursor 분업 흐름·시간 비교
- 03-mcp-layers           Claude Client ↔ MCP Server ↔ 외부 도구 3단
- 04-workflow-6steps      Obsidian → Claude Desktop → Code → Cursor → Git → 회고
- 05-cost-productivity    도구별 월 비용 × 생산성 증가율

Usage:
  /Users/seung-yeoblee/.local/bin/uv run --with matplotlib --with pillow \
    python3 scripts/charts/generate-ai-coding-pillar-charts.py
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

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
for f in (F_BOLD, F_SEMI, F_REG):
    font_manager.fontManager.addfont(f)
plt.rcParams["font.family"] = "Pretendard"

OUT = Path("/Users/seung-yeoblee/dev/unpack-blogs/apps/aigrit/public/images/ai-coding-complete-guide-2026")
OUT.mkdir(parents=True, exist_ok=True)


def setup_fig(w=12, h=6.75):
    return plt.figure(figsize=(w, h), facecolor=BG_TOP)


def save(fig, out_path):
    fig.savefig(out_path, dpi=180, facecolor=BG_TOP, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ {out_path.name}  ({out_path.stat().st_size/1024:.1f}KB)")


# ---- 01: 4-quadrant matrix ----
def tools_matrix(out_path):
    fig = setup_fig(12, 7.5)
    ax = fig.add_axes([0.12, 0.13, 0.82, 0.70])
    ax.set_facecolor(BG_TOP)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(colors=SLATE, labelsize=11)

    fig.text(0.5, 0.94, "AI 코딩 도구 4분면 — 2026 실측", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.88, "가로: CLI ↔ IDE · 세로: 단일 파일 ↔ 프로젝트 전체", ha="center", color=SLATE, fontsize=12)

    tools = [
        ("Claude Code", 0.20, 0.85, CYAN, "CLI + 프로젝트 전체"),
        ("Cursor", 0.85, 0.30, INDIGO_LT, "IDE + 단일 파일"),
        ("Claude Desktop\n+ MCP", 0.30, 0.55, GREEN, "데스크톱 + 외부 도구"),
        ("Obsidian MCP", 0.18, 0.40, AMBER, "노트 vault 어댑터"),
    ]
    for name, x, y, color, _note in tools:
        ax.scatter([x], [y], s=900, c=color, alpha=0.92, edgecolors=WHITE, linewidths=2, zorder=3)
        ax.text(x + 0.03, y + 0.04, name, color=color, fontsize=14, fontweight="bold", linespacing=1.3)

    ax.axhline(0.5, color=SLATE_DIM, linewidth=0.7, linestyle="--", alpha=0.6)
    ax.axvline(0.5, color=SLATE_DIM, linewidth=0.7, linestyle="--", alpha=0.6)
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.1)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["CLI (터미널)", "IDE (에디터)"], color=WHITE, fontsize=12)
    ax.set_yticks([0.05, 1.0])
    ax.set_yticklabels(["단일 파일", "프로젝트 전체"], color=WHITE, fontsize=12)

    save(fig, out_path)


# ---- 02: Claude Code vs Cursor 시간 비교 ----
def cli_vs_ide(out_path):
    fig = setup_fig(12, 6.5)
    ax = fig.add_axes([0.18, 0.13, 0.74, 0.68])
    ax.set_facecolor(BG_TOP)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(colors=SLATE, labelsize=11)

    fig.text(0.5, 0.93, "Claude Code vs Cursor — 5개 시나리오 완료 시간", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.86, "1인 빌더 6주 평균 — 다중 파일·리팩토링은 Claude Code 우세", ha="center", color=SLATE, fontsize=12)

    scenarios = ["새 기능 (다중 파일)", "버그 수정", "리팩토링 (대규모)", "스캐폴딩", "반복 작업"]
    claude_t = [25, 3, 15, 30, 3]
    cursor_t = [55, 8, 40, 35, 12]

    y = list(range(len(scenarios)))
    bar_h = 0.36
    y_claude = [v + bar_h / 2 + 0.02 for v in y]
    y_cursor = [v - bar_h / 2 - 0.02 for v in y]

    ax.barh(y_claude, claude_t, height=bar_h, color=CYAN, label="Claude Code")
    ax.barh(y_cursor, cursor_t, height=bar_h, color=INDIGO_LT, label="Cursor")

    for yi, v in zip(y_claude, claude_t):
        ax.text(v + 1, yi, f"{v}분", va="center", color=CYAN, fontsize=11, fontweight="bold")
    for yi, v in zip(y_cursor, cursor_t):
        ax.text(v + 1, yi, f"{v}분", va="center", color=INDIGO_LT, fontsize=11, fontweight="bold")

    ax.set_yticks(y)
    ax.set_yticklabels(scenarios, color=WHITE, fontsize=12)
    ax.invert_yaxis()
    ax.set_xlim(0, 65)
    ax.set_xticks([0, 10, 20, 30, 40, 50, 60])

    ax.legend(loc="lower right", facecolor=BG_TOP, edgecolor="none", labelcolor=WHITE, fontsize=11, frameon=False)

    save(fig, out_path)


# ---- 03: MCP 3단 레이어 ----
def mcp_layers(out_path):
    fig = setup_fig(13, 6.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 6.5)
    ax.set_axis_off()

    fig.text(0.5, 0.92, "MCP 3단 레이어 — Claude ↔ 외부 도구 양방향", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.86, "JSON 설정 1개로 Claude가 vault·git repo·웹 API를 직접 조작", ha="center", color=SLATE, fontsize=12)

    layers = [
        ("Claude Client", "Claude Desktop · Claude Code CLI", "자연어 입력 + LLM 추론", CYAN),
        ("MCP Server", "obsidian-mcp · filesystem · custom", "JSON-RPC 표준 어댑터", INDIGO_LT),
        ("외부 도구", "Obsidian vault · git repo · GitHub API · Slack", "마크다운·코드·메시지·데이터", AMBER),
    ]
    box_w = 9.5
    box_h = 1.1
    gap = 0.40
    x0 = (13 - box_w) / 2
    y_start = 4.6

    for i, (name, impl, desc, color) in enumerate(layers):
        y = y_start - i * (box_h + gap)
        box = FancyBboxPatch((x0, y), box_w, box_h,
                              boxstyle="round,pad=0,rounding_size=0.18",
                              linewidth=2.2, edgecolor=color, facecolor=SLATE_BOX)
        ax.add_patch(box)
        ax.text(x0 + 0.4, y + box_h / 2 + 0.25, name, color=color, fontsize=15, fontweight="bold", va="center")
        ax.text(x0 + 0.4, y + box_h / 2 - 0.05, impl, color=WHITE, fontsize=12, va="center")
        ax.text(x0 + 0.4, y + box_h / 2 - 0.35, desc, color=SLATE, fontsize=10.5, va="center", style="italic")
        if i < len(layers) - 1:
            arr = FancyArrowPatch((x0 + box_w / 2, y - 0.05),
                                  (x0 + box_w / 2, y - gap + 0.05),
                                  arrowstyle="<->", color=SLATE, mutation_scale=18, linewidth=1.8)
            ax.add_patch(arr)

    save(fig, out_path)


# ---- 04: 6단계 워크플로우 ----
def workflow_6steps(out_path):
    fig = setup_fig(13, 7.2)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7.2)
    ax.set_axis_off()

    fig.text(0.5, 0.93, "1인 빌더 AI 코딩 워크플로우 6단계", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.87, "기획부터 회고까지 — 각 단계 도구 1~2개로 핸드오프 산출물 1개", ha="center", color=SLATE, fontsize=12)

    steps = [
        ("01", "기획", "Obsidian\nspec.md", PURPLE),
        ("02", "설계", "Claude Desktop\n+ MCP", GREEN),
        ("03", "구현", "Claude Code\n다중 파일", CYAN),
        ("04", "정밀", "Cursor\n단일 파일", INDIGO_LT),
        ("05", "배포", "Git push\nVercel", AMBER),
        ("06", "회고", "Obsidian\n회고 노트", PURPLE),
    ]
    box_w = 1.95
    box_h = 3.0
    gap = 0.13
    total_w = 6 * box_w + 5 * gap
    x_start = (13 - total_w) / 2
    y0 = 1.8

    for i, (num, name, tool, color) in enumerate(steps):
        x = x_start + i * (box_w + gap)
        box = FancyBboxPatch((x, y0), box_w, box_h,
                              boxstyle="round,pad=0,rounding_size=0.14",
                              linewidth=2, edgecolor=color, facecolor=SLATE_BOX)
        ax.add_patch(box)
        ax.text(x + box_w / 2, y0 + box_h - 0.42, num, ha="center", color=color, fontsize=13, fontweight="bold")
        ax.text(x + box_w / 2, y0 + box_h - 1.0, name, ha="center", color=WHITE, fontsize=16, fontweight="bold")
        ax.text(x + box_w / 2, y0 + 0.7, tool, ha="center", color=SLATE, fontsize=10.5, linespacing=1.5)
        if i < len(steps) - 1:
            arr = FancyArrowPatch((x + box_w + 0.005, y0 + box_h / 2),
                                  (x + box_w + gap - 0.005, y0 + box_h / 2),
                                  arrowstyle="->", color=SLATE, mutation_scale=13, linewidth=1.4)
            ax.add_patch(arr)

    save(fig, out_path)


# ---- 05: 비용·생산성 ----
def cost_productivity(out_path):
    fig = setup_fig(12, 6.75)
    ax = fig.add_axes([0.12, 0.14, 0.82, 0.66])
    ax.set_facecolor(BG_TOP)
    for s in ax.spines.values():
        s.set_color(SLATE_DIM)
        s.set_linewidth(0.7)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(colors=SLATE, labelsize=11)

    fig.text(0.5, 0.93, "도구별 월 비용 × 생산성 증가율", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.87, "6주 실측 — Claude Code가 ROI 마진 가장 큼", ha="center", color=SLATE, fontsize=12)

    tools = [
        ("Claude Code", 40, 75, CYAN),
        ("Cursor", 20, 30, INDIGO_LT),
        ("Claude Desktop\n+ MCP", 0, 45, GREEN),
        ("Obsidian MCP", 0, 35, AMBER),
    ]
    for name, cost, gain, color in tools:
        ax.scatter([cost], [gain], s=800, c=color, alpha=0.9, edgecolors=WHITE, linewidths=2, zorder=3)
        offset_x = 2.5 if cost < 30 else -10
        ax.text(cost + offset_x, gain + 3, name, color=color, fontsize=12, fontweight="bold", linespacing=1.4,
                ha="left" if cost < 30 else "right")

    ax.set_xlim(-5, 55)
    ax.set_ylim(0, 90)
    ax.set_xlabel("월 비용 (USD)", color=SLATE, fontsize=12)
    ax.set_ylabel("생산성 증가율 (%)", color=SLATE, fontsize=12)
    ax.set_xticks([0, 10, 20, 30, 40, 50])
    ax.set_yticks([0, 25, 50, 75])

    # Best ROI zone (top-left)
    ax.annotate("ROI 최적", xy=(8, 65), xytext=(15, 80),
                color=SLATE, fontsize=10,
                arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.0))

    save(fig, out_path)


if __name__ == "__main__":
    tools_matrix(OUT / "01-tools-matrix.png")
    cli_vs_ide(OUT / "02-cli-vs-ide.png")
    mcp_layers(OUT / "03-mcp-layers.png")
    workflow_6steps(OUT / "04-workflow-6steps.png")
    cost_productivity(OUT / "05-cost-productivity.png")
    print(f"\n출력 폴더: {OUT}")
