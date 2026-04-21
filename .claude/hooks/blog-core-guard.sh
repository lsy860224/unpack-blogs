#!/bin/bash
# .claude/hooks/blog-core-guard.sh
# PostToolUse hook — blog-core 파일 수정 시 양쪽 앱 타입 검증 dry-run
# blog-core 변경은 AIGrit + babipanote 양쪽에 영향. 실제 빌드는 너무 무거우므로
# 타입 체크만 빠르게 돌려 회귀를 조기에 감지한다.

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_input.path // empty')

case "$FILE_PATH" in
  */packages/blog-core/*) ;;
  *) exit 0 ;;
esac

echo "⚠️ blog-core 수정 감지: $FILE_PATH" >&2
echo "   → AIGrit + babipanote 타입 체크 진행…" >&2

ROOT="/Users/seung-yeoblee/dev/unpack-blogs"
FAIL=0
for dir in packages/blog-core apps/aigrit apps/babipanote; do
  if [ -f "$ROOT/$dir/tsconfig.json" ] && [ -x "$ROOT/$dir/node_modules/.bin/tsc" ]; then
    if ! (cd "$ROOT/$dir" && ./node_modules/.bin/tsc --noEmit) 2>&1 | sed "s|^|  [$dir] |" >&2; then
      FAIL=1
    fi
  fi
done

if [ "$FAIL" -ne 0 ]; then
  echo "❌ blog-core 변경이 양쪽 앱 타입 체크를 실패시킵니다. 수정하세요." >&2
  exit 2
fi

echo "✅ blog-core 변경 양쪽 타입 통과" >&2
exit 0
