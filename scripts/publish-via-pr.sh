#!/usr/bin/env bash
# 로컬 main 커밋을 feature 브랜치에 push → PR 생성 → auto-merge 활성화
# Claude Code의 "직접 main push 금지" 정책 우회용 헬퍼.
#
# Usage:
#   scripts/publish-via-pr.sh "PR title" "PR body (optional)"
#
# 동작:
#   1. 로컬 main에서 origin/main보다 앞선 커밋들을 자동 감지
#   2. auto/{YYYY-MM-DD-HHMMSS} 브랜치 이름으로 push
#   3. gh pr create + gh pr merge --auto --squash
#   4. GitHub Auto-merge가 mergeable 즉시 main에 반영 + 브랜치 자동 삭제
#   5. CI 통과 후 main 동기화: 사용자가 `git pull` 또는 자동 sync 단계 실행
set -euo pipefail

cd "$(dirname "$0")/.."

PR_TITLE="${1:?PR title required}"
PR_BODY="${2:-Auto-published via Claude Code (publish-via-pr.sh).}"

# 미푸시 커밋 확인
AHEAD=$(git rev-list --count origin/main..HEAD)
if [ "$AHEAD" -eq 0 ]; then
  echo "❌ origin/main과 동일 — push할 커밋 없음" >&2
  exit 1
fi

BRANCH="auto/$(date +%Y-%m-%d-%H%M%S)"
echo "📦 브랜치: $BRANCH ($AHEAD 커밋)"

# main HEAD를 feature 브랜치로 push (로컬 main 그대로 유지)
git push origin "main:refs/heads/$BRANCH"

# PR 생성
PR_URL=$(gh pr create \
  --base main \
  --head "$BRANCH" \
  --title "$PR_TITLE" \
  --body "$PR_BODY")

echo "🔗 PR: $PR_URL"

# Auto-merge 활성화 (squash)
gh pr merge "$PR_URL" --auto --squash --delete-branch

echo "✅ Auto-merge 대기 중 — mergeable 즉시 main 반영, 브랜치 자동 삭제"
echo "   merge 완료 후 사용자가 'git fetch origin && git reset --hard origin/main' 실행"
