#!/bin/bash
# .claude/hooks/notify-mac.sh
# Notification hook — Claude Code 알림을 macOS 네이티브 알림으로 전달
# terminal-notifier 또는 osascript 사용

INPUT=$(cat)
MESSAGE=$(echo "$INPUT" | jq -r '.message // "Claude Code 알림"')

# terminal-notifier 있으면 사용 (brew install terminal-notifier)
if command -v terminal-notifier &>/dev/null; then
  terminal-notifier \
    -title "Claude Code" \
    -subtitle "unpack-blogs" \
    -message "$MESSAGE" \
    -sound "Ping" \
    -group "claude-code" \
    2>/dev/null
else
  # fallback: osascript
  osascript -e "display notification \"$MESSAGE\" with title \"Claude Code\" subtitle \"unpack-blogs\" sound name \"Ping\"" 2>/dev/null
fi

exit 0
