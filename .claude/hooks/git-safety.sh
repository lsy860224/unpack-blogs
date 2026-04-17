#!/bin/bash
# .claude/hooks/git-safety.sh
# PreToolUse hook — Bash(git *) 위험 명령 차단
# force push, branch 삭제, reset --hard 방지

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# git 명령이 아니면 스킵
echo "$COMMAND" | grep -qE '\bgit\b' || exit 0

# force push 차단
if echo "$COMMAND" | grep -qiE 'git\s+push\s+.*--force'; then
  cat << 'EOF'
{"decision": "block", "reason": "⛔ Force push 차단. main 브랜치 보호 정책 위반."}
EOF
  exit 0
fi

# branch 삭제 차단 (main/master)
if echo "$COMMAND" | grep -qiE 'git\s+branch\s+-[dD]\s+(main|master)'; then
  cat << 'EOF'
{"decision": "block", "reason": "⛔ main/master 브랜치 삭제 차단."}
EOF
  exit 0
fi

# reset --hard 차단
if echo "$COMMAND" | grep -qiE 'git\s+reset\s+--hard'; then
  cat << 'EOF'
{"decision": "block", "reason": "⛔ git reset --hard 차단. 커밋 손실 위험. --soft 또는 revert를 사용하세요."}
EOF
  exit 0
fi

# .env 파일 커밋 감지
if echo "$COMMAND" | grep -qiE 'git\s+add.*\.env'; then
  cat << 'EOF'
{"decision": "block", "reason": "⛔ .env 파일 커밋 차단. 환경변수가 노출됩니다. .gitignore에 추가하세요."}
EOF
  exit 0
fi

exit 0
