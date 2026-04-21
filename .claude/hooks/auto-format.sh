#!/bin/bash
# .claude/hooks/auto-format.sh
# PostToolUse hook — Write|Edit 후 자동 포맷팅
# Prettier는 npx 대신 로컬 pnpm exec로 실행 (기동 시간 단축)

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_input.path // empty')

[ -z "$FILE_PATH" ] && exit 0
[ ! -f "$FILE_PATH" ] && exit 0

# 포맷 대상 확장자만
case "$FILE_PATH" in
  *.ts|*.tsx|*.js|*.jsx|*.json|*.css|*.md|*.mdx) ;;
  *) exit 0 ;;
esac

ROOT="/Users/seung-yeoblee/dev/unpack-blogs"
PRETTIER="$ROOT/node_modules/.bin/prettier"

if [ -x "$PRETTIER" ]; then
  "$PRETTIER" --log-level=silent --write "$FILE_PATH" 2>/dev/null
elif command -v pnpm >/dev/null 2>&1; then
  (cd "$ROOT" && pnpm exec prettier --log-level=silent --write "$FILE_PATH") 2>/dev/null
fi

exit 0
