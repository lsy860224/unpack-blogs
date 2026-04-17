#!/bin/bash
# .claude/hooks/setup.sh
# Hooks 초기 셋업 — 실행 권한 부여 + 의존성 확인
# 사용법: bash .claude/hooks/setup.sh

HOOKS_DIR="$(dirname "$0")"

echo "🔧 Claude Code Hooks 셋업 시작..."
echo ""

# 1. 실행 권한 부여
echo "1️⃣ 스크립트 실행 권한 부여"
chmod +x "$HOOKS_DIR"/*.sh
echo "   ✅ 완료"
echo ""

# 2. 의존성 확인
echo "2️⃣ 의존성 확인"

# jq (JSON 파싱 — hooks 필수)
if command -v jq &>/dev/null; then
  echo "   ✅ jq $(jq --version)"
else
  echo "   ❌ jq 미설치 — brew install jq"
fi

# prettier (auto-format hook)
if npx --no-install prettier --version &>/dev/null; then
  echo "   ✅ prettier $(npx --no-install prettier --version)"
else
  echo "   ⚠️ prettier 미설치 — pnpm add -D prettier (프로젝트에 이미 있을 수 있음)"
fi

# terminal-notifier (알림 hook, 선택)
if command -v terminal-notifier &>/dev/null; then
  echo "   ✅ terminal-notifier 설치됨"
else
  echo "   ⚠️ terminal-notifier 미설치 (선택) — brew install terminal-notifier"
  echo "      → 없으면 osascript fallback 사용"
fi

echo ""

# 3. 현재 hooks 목록
echo "3️⃣ 등록된 hooks"
for f in "$HOOKS_DIR"/*.sh; do
  [ "$f" = "$HOOKS_DIR/setup.sh" ] && continue
  name=$(basename "$f" .sh)
  echo "   📌 $name"
done
echo ""

# 4. settings.json 확인
SETTINGS="$(dirname "$HOOKS_DIR")/settings.json"
if [ -f "$SETTINGS" ]; then
  echo "4️⃣ .claude/settings.json 존재 ✅"
  hook_count=$(jq '.hooks | to_entries | map(.value | length) | add // 0' "$SETTINGS" 2>/dev/null)
  echo "   등록된 hook 이벤트 수: $hook_count"
else
  echo "4️⃣ .claude/settings.json 미존재 ⚠️"
  echo "   → settings.json 생성이 필요합니다"
fi

echo ""
echo "🎉 셋업 완료. Claude Code 재시작 후 적용됩니다."
echo "   확인: Claude Code에서 /hooks 실행"
