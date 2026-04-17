#!/bin/bash
# .claude/hooks/blog-core-guard.sh
# PostToolUse hook — blog-core 파일 수정 시 양쪽 빌드 알림
# blog-core 변경은 AIGrit + babipanote 양쪽에 영향

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_input.path // empty')

# blog-core 파일인지 확인
case "$FILE_PATH" in
  */packages/blog-core/*)
    echo "⚠️ blog-core 수정 감지: $FILE_PATH" >&2
    echo "   → AIGrit + babipanote 양쪽 빌드 확인 필요" >&2
    echo "   → pnpm turbo run build 실행 권장" >&2
    ;;
esac

exit 0
