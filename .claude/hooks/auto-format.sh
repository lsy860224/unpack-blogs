#!/bin/bash
# .claude/hooks/auto-format.sh
# PostToolUse hook — Write|Edit 후 자동 포맷팅
# Prettier로 수정된 파일을 자동 포맷 (Tailwind 클래스 정렬 포함)

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_input.path // empty')

# 파일 경로 없으면 스킵
[ -z "$FILE_PATH" ] && exit 0

# 존재하지 않는 파일 스킵
[ ! -f "$FILE_PATH" ] && exit 0

# 포맷 대상 확장자만
case "$FILE_PATH" in
  *.ts|*.tsx|*.js|*.jsx|*.json|*.css|*.md|*.mdx)
    npx prettier --write "$FILE_PATH" 2>/dev/null
    ;;
esac

exit 0
