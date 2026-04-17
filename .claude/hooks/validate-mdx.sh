#!/bin/bash
# .claude/hooks/validate-mdx.sh
# PostToolUse hook — Write|Edit된 MDX 파일의 frontmatter 필수 필드 검증

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_input.path // empty')

# MDX 파일만 대상
case "$FILE_PATH" in
  *.mdx) ;;
  *) exit 0 ;;
esac

[ ! -f "$FILE_PATH" ] && exit 0

# frontmatter 추출 (--- 사이)
FRONTMATTER=$(awk '/^---$/{if(++c==2)exit}c' "$FILE_PATH")

# 필수 필드 체크
MISSING=""
for field in title date slug description tags; do
  if ! echo "$FRONTMATTER" | grep -q "^${field}:"; then
    MISSING="${MISSING} ${field}"
  fi
done

if [ -n "$MISSING" ]; then
  echo "⚠️ MDX frontmatter 필수 필드 누락:${MISSING} — ${FILE_PATH}" >&2
fi

# slug에 한글·대문자·공백 감지
SLUG=$(echo "$FRONTMATTER" | grep '^slug:' | sed 's/slug:\s*//;s/["\x27]//g' | tr -d ' ')
if echo "$SLUG" | grep -qE '[A-Z가-힣 ]'; then
  echo "⚠️ slug에 대문자·한글·공백 감지: '${SLUG}' — kebab-case 영문 소문자만 사용" >&2
fi

exit 0
