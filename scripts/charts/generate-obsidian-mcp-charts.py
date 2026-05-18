#!/usr/bin/env python3
"""
obsidian-mcp-plugins-best-5 + obsidian-claude-code-mcp 본문 차트 6장 생성.

AIGrit 브랜드 컬러·Pretendard 다크 테마.

obsidian-mcp-plugins-best-5 (지식관리 cluster):
  - 01-mcp-stack-layers     Claude Desktop ↔ MCP server ↔ Obsidian vault 3단
  - 02-five-plugins-matrix  5개 플러그인 매일사용 × 안정성 scatter
  - 03-adoption-roadmap     도입 순서 (#1 → #3 → #5 → #2 → #4)

obsidian-claude-code-mcp (AI 코딩 cluster):
  - 01-bridge-before-after  분리 비용 → MCP 다리 비교
  - 02-mcp-layers           Client/Protocol/Server/Data 4레이어
  - 03-workflow-loop        Obsidian → Claude Code → vault 루프

Usage:
  /Users/seung-yeoblee/.local/bin/uv run --with matplotlib --with pillow \
    python3 scripts/charts/generate-obsidian-mcp-charts.py
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

OUT_A = Path("/Users/seung-yeoblee/dev/unpack-blogs/apps/aigrit/public/images/obsidian-mcp-plugins-best-5")
OUT_B = Path("/Users/seung-yeoblee/dev/unpack-blogs/apps/aigrit/public/images/obsidian-claude-code-mcp")
OUT_A.mkdir(parents=True, exist_ok=True)
OUT_B.mkdir(parents=True, exist_ok=True)


def setup_fig(w=12, h=6.75):
    return plt.figure(figsize=(w, h), facecolor=BG_TOP)


def style_axes(ax):
    ax.set_facecolor(BG_TOP)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(colors=SLATE, labelsize=11)


def save(fig, out_path):
    fig.savefig(out_path, dpi=180, facecolor=BG_TOP, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ {out_path.parent.name}/{out_path.name}  ({out_path.stat().st_size/1024:.1f}KB)")


# ============================================================
# obsidian-mcp-plugins-best-5
# ============================================================

def mcp_stack_layers(out_path):
    fig = setup_fig(13, 6.8)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 6.8)
    ax.set_axis_off()

    fig.text(0.5, 0.92, "MCP가 Obsidian과 만나는 3단 레이어", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.86, "Claude Desktop ↔ MCP server ↔ Obsidian vault — 가운데 어댑터가 양쪽 권한을 전달", ha="center", color=SLATE, fontsize=12)

    layers = [
        ("Claude Desktop", "클라이언트 — 자연어 입력 + LLM 추론", CYAN),
        ("MCP server", "어댑터 — JSON-RPC로 도구 호출 표준화", INDIGO_LT),
        ("Obsidian vault", "데이터 — 마크다운 노트 + Local REST API", AMBER),
    ]

    box_w = 8.0
    box_h = 1.05
    gap = 0.45
    x0 = (13 - box_w) / 2
    y_start = 4.5

    for i, (name, desc, color) in enumerate(layers):
        y = y_start - i * (box_h + gap)
        box = FancyBboxPatch((x0, y), box_w, box_h,
                              boxstyle="round,pad=0,rounding_size=0.18",
                              linewidth=2.2, edgecolor=color, facecolor=SLATE_BOX)
        ax.add_patch(box)
        ax.text(x0 + 0.4, y + box_h / 2 + 0.18, name, color=color, fontsize=16, fontweight="bold", va="center")
        ax.text(x0 + 0.4, y + box_h / 2 - 0.22, desc, color=WHITE, fontsize=11, va="center")
        if i < len(layers) - 1:
            arr = FancyArrowPatch((x0 + box_w / 2, y - 0.05),
                                  (x0 + box_w / 2, y - gap + 0.05),
                                  arrowstyle="<->", color=SLATE, mutation_scale=18, linewidth=1.8)
            ax.add_patch(arr)

    save(fig, out_path)


def five_plugins_matrix(out_path):
    fig = setup_fig(12, 7.0)
    ax = fig.add_axes([0.12, 0.13, 0.82, 0.70])
    style_axes(ax)

    fig.text(0.5, 0.94, "5개 MCP 플러그인 — 매일 사용도 × 안정성", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.88, "6주 운영 실측 — 우상단(매일·안정)이 핵심 플러그인", ha="center", color=SLATE, fontsize=12)

    plugins = [
        ("① Obsidian MCP Server", 0.85, 0.92, CYAN),
        ("② obsidian-mcp (커뮤니티)", 0.50, 0.55, INDIGO_LT),
        ("③ Smart Connections + MCP", 0.90, 0.78, GREEN),
        ("④ Templater + MCP", 0.30, 0.80, PURPLE),
        ("⑤ Dataview + MCP", 0.75, 0.85, AMBER),
    ]
    for name, x, y, color in plugins:
        ax.scatter([x], [y], s=700, c=color, alpha=0.92, edgecolors=WHITE, linewidths=2, zorder=3)
        ax.text(x + 0.02, y + 0.035, name, color=color, fontsize=12, fontweight="bold")

    ax.axhline(0.5, color=SLATE_DIM, linewidth=0.7, linestyle="--", alpha=0.6)
    ax.axvline(0.5, color=SLATE_DIM, linewidth=0.7, linestyle="--", alpha=0.6)
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.1)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["가끔", "매일"], color=WHITE, fontsize=12)
    ax.set_yticks([0.05, 1.0])
    ax.set_yticklabels(["베타·불안정", "안정"], color=WHITE, fontsize=12)

    save(fig, out_path)


def adoption_roadmap(out_path):
    fig = setup_fig(13, 6.8)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 6.8)
    ax.set_axis_off()

    fig.text(0.5, 0.92, "추천 도입 순서 — 6주 운영해서 정한 5단계", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.86, "한 번에 다 깔지 말고 1주에 하나씩 — 충돌·중복 회피", ha="center", color=SLATE, fontsize=12)

    steps = [
        ("W1\n①", "Obsidian MCP\nServer", "베이스라인 연결", CYAN),
        ("W2\n③", "Smart Connections\n+ MCP", "의미 검색 추가", GREEN),
        ("W3\n⑤", "Dataview\n+ MCP", "쿼리 자동화", AMBER),
        ("W4\n②", "obsidian-mcp\n(커뮤니티)", "vault가 커진 뒤", INDIGO_LT),
        ("W5\n④", "Templater\n+ MCP", "자동 노트 생성", PURPLE),
    ]
    box_w = 2.2
    box_h = 3.4
    gap = 0.18
    total_w = 5 * box_w + 4 * gap
    x_start = (13 - total_w) / 2
    y0 = 1.4

    for i, (week, name, desc, color) in enumerate(steps):
        x = x_start + i * (box_w + gap)
        box = FancyBboxPatch((x, y0), box_w, box_h,
                              boxstyle="round,pad=0,rounding_size=0.16",
                              linewidth=2.2, edgecolor=color, facecolor=SLATE_BOX)
        ax.add_patch(box)
        ax.text(x + box_w / 2, y0 + box_h - 0.55, week, ha="center", color=color, fontsize=15, fontweight="bold", linespacing=1.2)
        ax.text(x + box_w / 2, y0 + box_h - 1.65, name, ha="center", color=WHITE, fontsize=11.5, fontweight="bold", linespacing=1.5)
        ax.text(x + box_w / 2, y0 + 0.5, desc, ha="center", color=SLATE, fontsize=10)
        if i < len(steps) - 1:
            arr = FancyArrowPatch((x + box_w + 0.02, y0 + box_h / 2),
                                  (x + box_w + gap - 0.02, y0 + box_h / 2),
                                  arrowstyle="->", color=SLATE, mutation_scale=15, linewidth=1.5)
            ax.add_patch(arr)

    save(fig, out_path)


# ============================================================
# obsidian-claude-code-mcp
# ============================================================

def bridge_before_after(out_path):
    fig = setup_fig(13, 6.8)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 6.8)
    ax.set_axis_off()

    fig.text(0.5, 0.92, "노트와 코드의 분리 비용 — MCP 다리 전/후", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.86, "같은 텍스트가 세 번 이동하던 흐름이 한 명령어로 합쳐진다", ha="center", color=SLATE, fontsize=12)

    # Before (left)
    fig.text(0.25, 0.78, "Before — 분리", ha="center", color=RED, fontsize=15, fontweight="bold")
    nodes_b = [("Obsidian\n기획 노트", 2.0, 5.0, PURPLE),
               ("VS Code /\nCursor 코드", 2.0, 3.4, INDIGO_LT),
               ("Obsidian\n회고 정리", 2.0, 1.8, PURPLE)]
    for name, x, y, color in nodes_b:
        box = FancyBboxPatch((x, y - 0.45), 2.4, 0.9,
                              boxstyle="round,pad=0,rounding_size=0.12",
                              linewidth=1.8, edgecolor=color, facecolor=SLATE_BOX)
        ax.add_patch(box)
        ax.text(x + 1.2, y, name, ha="center", color=WHITE, fontsize=11, va="center", linespacing=1.5)
    for y1, y2 in [(5.0 - 0.45, 3.4 + 0.45), (3.4 - 0.45, 1.8 + 0.45)]:
        arr = FancyArrowPatch((3.2, y1), (3.2, y2), arrowstyle="->", color=RED, mutation_scale=14, linewidth=1.6)
        ax.add_patch(arr)
        ax.text(3.45, (y1 + y2) / 2, "복붙", color=RED, fontsize=10, va="center")

    # After (right)
    fig.text(0.75, 0.78, "After — MCP로 합쳐짐", ha="center", color=GREEN, fontsize=15, fontweight="bold")
    nodes_a = [("Obsidian\nvault", 8.4, 4.6, PURPLE),
               ("Claude Code\nCLI", 11.0, 4.6, CYAN)]
    for name, x, y, color in nodes_a:
        box = FancyBboxPatch((x, y - 0.45), 2.0, 0.9,
                              boxstyle="round,pad=0,rounding_size=0.12",
                              linewidth=2, edgecolor=color, facecolor=SLATE_BOX)
        ax.add_patch(box)
        ax.text(x + 1.0, y, name, ha="center", color=WHITE, fontsize=11, va="center", linespacing=1.5)
    # MCP bridge in middle
    box_mcp = FancyBboxPatch((9.0, 2.4), 1.9, 0.9,
                              boxstyle="round,pad=0,rounding_size=0.12",
                              linewidth=2, edgecolor=GREEN, facecolor=SLATE_BOX)
    ax.add_patch(box_mcp)
    ax.text(9.95, 2.85, "MCP server", ha="center", color=GREEN, fontsize=11, fontweight="bold", va="center")
    # arrows two-way
    for x_node in [9.4, 12.0]:
        arr = FancyArrowPatch((x_node, 4.15), (9.95, 3.3), arrowstyle="<->", color=GREEN, mutation_scale=14, linewidth=1.5)
        ax.add_patch(arr)

    save(fig, out_path)


def mcp_layers(out_path):
    fig = setup_fig(12, 6.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.5)
    ax.set_axis_off()

    fig.text(0.5, 0.93, "MCP 4-layer — Client·Protocol·Server·Data", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.87, "Claude Code CLI → MCP(stdio) → obsidian-mcp → vault·git repo", ha="center", color=SLATE, fontsize=12)

    layers = [
        ("Client", "Claude Code CLI (터미널)", "명령 입력 + LLM 추론", CYAN),
        ("Protocol", "MCP (stdio 또는 SSE)", "JSON-RPC 표준 통신", INDIGO_LT),
        ("Server", "obsidian-mcp · filesystem MCP", "도구 어댑터", GREEN),
        ("Data", "Obsidian vault + git repo", "마크다운 + 코드 파일", AMBER),
    ]
    box_w = 9.0
    box_h = 0.85
    gap = 0.30
    x0 = (12 - box_w) / 2
    y_start = 4.5
    for i, (layer, impl, desc, color) in enumerate(layers):
        y = y_start - i * (box_h + gap)
        box = FancyBboxPatch((x0, y), box_w, box_h,
                              boxstyle="round,pad=0,rounding_size=0.14",
                              linewidth=2, edgecolor=color, facecolor=SLATE_BOX)
        ax.add_patch(box)
        ax.text(x0 + 0.3, y + box_h / 2, layer, color=color, fontsize=13, fontweight="bold", va="center")
        ax.text(x0 + 1.85, y + box_h / 2 + 0.16, impl, color=WHITE, fontsize=12, va="center", fontweight="bold")
        ax.text(x0 + 1.85, y + box_h / 2 - 0.18, desc, color=SLATE, fontsize=10.5, va="center")
        if i < len(layers) - 1:
            arr = FancyArrowPatch((x0 + box_w / 2, y - 0.02),
                                  (x0 + box_w / 2, y - gap + 0.02),
                                  arrowstyle="<->", color=SLATE_DIM, mutation_scale=14, linewidth=1.3)
            ax.add_patch(arr)

    save(fig, out_path)


def workflow_loop(out_path):
    fig = setup_fig(13, 7.0)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7.0)
    ax.set_axis_off()

    fig.text(0.5, 0.93, "한 명령어 안에서 끝나는 기획·구현·회고 루프", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.87, "Obsidian vault → Claude Code → vault back — 양방향 흐름", ha="center", color=SLATE, fontsize=12)

    nodes = [
        ("Obsidian\n기획 노트 작성", 2.5, 4.6, PURPLE),
        ("Claude Code\n노트 읽기 + 구현", 7.0, 5.5, CYAN),
        ("Vault\n변경사항 자동 요약", 11.0, 4.6, GREEN),
        ("Obsidian\n다음 기획 연결", 7.0, 2.4, AMBER),
    ]
    for name, x, y, color in nodes:
        box = FancyBboxPatch((x - 1.4, y - 0.55), 2.8, 1.1,
                              boxstyle="round,pad=0,rounding_size=0.18",
                              linewidth=2.2, edgecolor=color, facecolor=SLATE_BOX)
        ax.add_patch(box)
        ax.text(x, y, name, ha="center", color=WHITE, fontsize=12, va="center", linespacing=1.5)

    arrows = [
        ((4.0, 4.7), (5.5, 5.4)),  # 기획 → Claude
        ((8.4, 5.5), (9.7, 4.7)),  # Claude → 요약
        ((10.5, 4.0), (8.0, 2.6)), # 요약 → 다음 기획
        ((6.0, 2.6), (3.0, 4.0)),  # 다음 기획 → 기획 (루프)
    ]
    for (x1, y1), (x2, y2) in arrows:
        arr = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="->", color=SLATE, mutation_scale=16, linewidth=1.6, connectionstyle="arc3,rad=0.1")
        ax.add_patch(arr)

    save(fig, out_path)


if __name__ == "__main__":
    # obsidian-mcp-plugins-best-5
    mcp_stack_layers(OUT_A / "01-mcp-stack-layers.png")
    five_plugins_matrix(OUT_A / "02-five-plugins-matrix.png")
    adoption_roadmap(OUT_A / "03-adoption-roadmap.png")
    # obsidian-claude-code-mcp
    bridge_before_after(OUT_B / "01-bridge-before-after.png")
    mcp_layers(OUT_B / "02-mcp-layers.png")
    workflow_loop(OUT_B / "03-workflow-loop.png")
    print("\n출력:")
    print(f"  {OUT_A}")
    print(f"  {OUT_B}")
