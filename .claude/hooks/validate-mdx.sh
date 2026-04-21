#!/bin/bash
# .claude/hooks/validate-mdx.sh
# PostToolUse hook — Write|Edit된 MDX 파일의 frontmatter 필수 필드 검증
# 필수 필드 누락 또는 slug 포맷 오류 시 exit 2 (Claude에게 수정 요구)

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_input.path // empty')

case "$FILE_PATH" in
  *.mdx) ;;
  *) exit 0 ;;
esac

[ ! -f "$FILE_PATH" ] && exit 0

FRONTMATTER=$(awk '/^---$/{if(++c==2)exit}c' "$FILE_PATH")

MISSING=""
for field in title date slug description tags thumbnail; do
  if ! echo "$FRONTMATTER" | grep -q "^${field}:"; then
    MISSING="${MISSING} ${field}"
  fi
done

FAIL=0
if [ -n "$MISSING" ]; then
  echo "❌ MDX frontmatter 필수 필드 누락:${MISSING} — ${FILE_PATH}" >&2
  FAIL=1
fi

SLUG=$(echo "$FRONTMATTER" | grep '^slug:' | sed 's/slug:\s*//;s/["'\'']//g' | tr -d ' ')
if [ -n "$SLUG" ]; then
  if echo "$SLUG" | grep -qE '[A-Z가-힣 _]'; then
    echo "❌ slug에 대문자·한글·공백·언더스코어 감지: '${SLUG}' — kebab-case 영문 소문자만 사용" >&2
    FAIL=1
  fi
fi

if [ "$FAIL" -ne 0 ]; then
  exit 2
fi
exit 0
