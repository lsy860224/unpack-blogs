#!/bin/bash
# .claude/hooks/stop-typecheck.sh
# Stop hook — Claude가 작업 완료 선언 시 타입 체크 실행
# 실패하면 exit 2로 Claude에게 "아직 끝나지 않았다"고 전달

INPUT=$(cat)

# stop_hook_active 체크 — 무한 루프 방지
if [ "$(echo "$INPUT" | jq -r '.stop_hook_active // false')" = "true" ]; then
  exit 0
fi

cd /Users/seung-yeoblee/dev/unpack-blogs || exit 0

# TypeScript 타입 체크 (워크스페이스별, 빠른 검증)
echo "🔍 TypeScript 타입 체크 중..." >&2
FAIL=0
for dir in packages/blog-core apps/aigrit apps/babipanote; do
  if [ -f "$dir/tsconfig.json" ] && [ -x "$dir/node_modules/.bin/tsc" ]; then
    if ! (cd "$dir" && ./node_modules/.bin/tsc --noEmit) 2>&1 | sed "s|^|  [$dir] |" >&2; then
      FAIL=1
    fi
  fi
done

if [ "$FAIL" -ne 0 ]; then
  echo "❌ TypeScript 타입 에러 발견. 수정이 필요합니다." >&2
  exit 2  # Claude에게 계속 작업하라고 지시
fi

echo "✅ 타입 체크 통과" >&2
exit 0
