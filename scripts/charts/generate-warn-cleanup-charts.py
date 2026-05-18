#!/usr/bin/env python3
"""
W22 WARN 정리 — claude-blog-workflow-seo + hello-world 본문 차트 자동 생성.

AIGrit 브랜드 컬러·Pretendard 다크 테마.

claude-blog-workflow-seo (3장):
  - 01-workflow-4steps   초안→발행→색인→추적 4단계 박스 흐름
  - 02-step-tooling      Step별 도구 매핑 매트릭스
  - 03-30min-timeline    30분 타임라인 누적 막대

hello-world (1장):
  - 01-review-principles  4가지 리뷰 원칙 박스 다이어그램

Usage:
  /Users/seung-yeoblee/.local/bin/uv run --with matplotlib --with pillow \
    python3 scripts/charts/generate-warn-cleanup-charts.py
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

OUT_A = Path("/Users/seung-yeoblee/dev/unpack-blogs/apps/aigrit/public/images/claude-blog-workflow-seo")
OUT_B = Path("/Users/seung-yeoblee/dev/unpack-blogs/apps/aigrit/public/images/hello-world")
OUT_A.mkdir(parents=True, exist_ok=True)
OUT_B.mkdir(parents=True, exist_ok=True)


def setup_fig(w=12, h=6.75):
    return plt.figure(figsize=(w, h), facecolor=BG_TOP)


def save(fig, out_path):
    fig.savefig(out_path, dpi=180, facecolor=BG_TOP, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ {out_path.parent.name}/{out_path.name}  ({out_path.stat().st_size/1024:.1f}KB)")


# ============================================================
# claude-blog-workflow-seo
# ============================================================

def workflow_4steps(out_path):
    fig = setup_fig(13, 6.6)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 6.6)
    ax.set_axis_off()

    fig.text(0.5, 0.92, "Claude 블로그 워크플로우 4단계", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.86, "초안 → 발행 → 색인 → 추적 — 한 글당 30분 SOP", ha="center", color=SLATE, fontsize=12)

    steps = [
        ("01", "초안", "Claude로\n키워드→구조→FAQ", "15분", CYAN),
        ("02", "발행", "Git → Vercel\n+ IndexNow ping", "5분", INDIGO_LT),
        ("03", "색인", "GSC URL 검사\n색인 요청", "5분", GREEN),
        ("04", "추적", "Obsidian 대시보드\n주간 분석", "5분", AMBER),
    ]
    box_w = 2.7
    box_h = 3.6
    gap = 0.30
    total_w = 4 * box_w + 3 * gap
    x_start = (13 - total_w) / 2
    y0 = 1.2

    for i, (num, name, desc, dur, color) in enumerate(steps):
        x = x_start + i * (box_w + gap)
        box = FancyBboxPatch((x, y0), box_w, box_h,
                              boxstyle="round,pad=0,rounding_size=0.18",
                              linewidth=2.5, edgecolor=color, facecolor=SLATE_BOX)
        ax.add_patch(box)
        ax.text(x + box_w / 2, y0 + box_h - 0.5, num, ha="center", color=color, fontsize=15, fontweight="bold")
        ax.text(x + box_w / 2, y0 + box_h - 1.15, name, ha="center", color=WHITE, fontsize=20, fontweight="bold")
        ax.text(x + box_w / 2, y0 + box_h - 2.25, desc, ha="center", color=WHITE, fontsize=12, linespacing=1.5)
        ax.text(x + box_w / 2, y0 + 0.5, dur, ha="center", color=color, fontsize=14, fontweight="bold")
        if i < len(steps) - 1:
            arr = FancyArrowPatch((x + box_w + 0.02, y0 + box_h / 2),
                                  (x + box_w + gap - 0.02, y0 + box_h / 2),
                                  arrowstyle="->", color=SLATE, mutation_scale=18, linewidth=1.8)
            ax.add_patch(arr)

    save(fig, out_path)


def step_tooling(out_path):
    fig = setup_fig(13, 7.0)
    ax = fig.add_axes([0.20, 0.12, 0.75, 0.72])
    ax.set_facecolor(BG_TOP)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(colors=SLATE, labelsize=11)

    fig.text(0.5, 0.93, "Step별 도구 매핑 — 어떤 단계에 무엇을 쓰는가", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.88, "한 도구로 다 안 됨 — 단계별로 강한 도구를 묶어 30분 안에", ha="center", color=SLATE, fontsize=12)

    steps = ["01 초안", "02 발행", "03 색인", "04 추적"]
    tools = ["Claude / Claude Code", "Git + Vercel + IndexNow", "GSC URL 검사", "Obsidian + Dataview"]
    colors = [CYAN, INDIGO_LT, GREEN, AMBER]

    y = list(range(len(steps)))
    for yi, (step, tool, color) in enumerate(zip(steps, tools, colors)):
        ax.barh(yi, 1, height=0.55, color=color, alpha=0.9)
        ax.text(0.04, yi, tool, va="center", color=WHITE, fontsize=14, fontweight="bold")

    ax.set_yticks(y)
    ax.set_yticklabels(steps, color=WHITE, fontsize=14, fontweight="bold")
    ax.invert_yaxis()
    ax.set_xlim(0, 1)
    ax.set_xticks([])

    save(fig, out_path)


def timeline_30min(out_path):
    fig = setup_fig(13, 6.0)
    ax = fig.add_axes([0.10, 0.20, 0.84, 0.55])
    ax.set_facecolor(BG_TOP)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(colors=SLATE, labelsize=12)

    fig.text(0.5, 0.92, "한 글당 누적 30분 — 단계별 시간 소비", ha="center", color=WHITE, fontsize=22, fontweight="bold")
    fig.text(0.5, 0.86, "예전 4시간짜리 작업이 W18 자동화 후 30분으로 압축", ha="center", color=SLATE, fontsize=12)

    labels = ["01 초안", "02 발행", "03 색인", "04 추적"]
    times = [15, 5, 5, 5]
    colors = [CYAN, INDIGO_LT, GREEN, AMBER]

    left = 0
    for label, t, color in zip(labels, times, colors):
        ax.barh(0, t, left=left, height=0.5, color=color, edgecolor=BG_TOP, linewidth=2)
        ax.text(left + t / 2, 0, f"{label}\n{t}분", ha="center", va="center", color=WHITE, fontsize=12, fontweight="bold", linespacing=1.4)
        left += t

    ax.set_xlim(0, 30)
    ax.set_ylim(-0.6, 0.6)
    ax.set_xticks([0, 5, 10, 15, 20, 25, 30])
    ax.set_xticklabels(["0", "5분", "10분", "15분", "20분", "25분", "30분"], color=SLATE)
    ax.set_yticks([])

    save(fig, out_path)


# ============================================================
# hello-world
# ============================================================

def review_principles(out_path):
    fig = setup_fig(13, 7.0)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7.0)
    ax.set_axis_off()

    fig.text(0.5, 0.92, "AIGrit 리뷰 4원칙", ha="center", color=WHITE, fontsize=24, fontweight="bold")
    fig.text(0.5, 0.86, "Validation · Numbers · Comparison · Context — 모든 글에 일관 적용", ha="center", color=SLATE, fontsize=12)

    principles = [
        ("검증", "Validation", "광고 카피가 아닌\n실사용 결과\n(3일 이상 사용)", CYAN),
        ("수치", "Numbers", "속도·비용·정확도를\n숫자로 표기\n표본 크기 명시", INDIGO_LT),
        ("비교", "Comparison", "1:1 또는 N:N\n대체재가 있을 때\n반드시 함께 다룸", GREEN),
        ("맥락", "Context", "직장인 / 개발자\n시나리오 명시\n자기 상황 대입 가능", AMBER),
    ]
    box_w = 2.9
    box_h = 3.8
    gap = 0.25
    total_w = 4 * box_w + 3 * gap
    x_start = (13 - total_w) / 2
    y0 = 1.4

    for i, (ko, en, desc, color) in enumerate(principles):
        x = x_start + i * (box_w + gap)
        box = FancyBboxPatch((x, y0), box_w, box_h,
                              boxstyle="round,pad=0,rounding_size=0.20",
                              linewidth=2.5, edgecolor=color, facecolor=SLATE_BOX)
        ax.add_patch(box)
        ax.text(x + box_w / 2, y0 + box_h - 0.55, ko, ha="center", color=color, fontsize=22, fontweight="bold")
        ax.text(x + box_w / 2, y0 + box_h - 1.30, en, ha="center", color=WHITE, fontsize=13, fontweight="bold", style="italic")
        ax.text(x + box_w / 2, y0 + box_h - 2.85, desc, ha="center", color=WHITE, fontsize=11.5, linespacing=1.7)

    save(fig, out_path)


if __name__ == "__main__":
    workflow_4steps(OUT_A / "01-workflow-4steps.png")
    step_tooling(OUT_A / "02-step-tooling.png")
    timeline_30min(OUT_A / "03-30min-timeline.png")
    review_principles(OUT_B / "01-review-principles.png")
    print("\n출력:")
    print(f"  {OUT_A}")
    print(f"  {OUT_B}")
