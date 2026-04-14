#!/bin/bash
# unpack-blogs 모노레포 초기화 스크립트
# 사용법: chmod +x scripts/setup.sh && ./scripts/setup.sh

echo "🚀 unpack-blogs 모노레포 초기화 시작..."

# 1. pnpm 확인
if ! command -v pnpm &> /dev/null; then
  echo "📦 pnpm 설치 중..."
  npm install -g pnpm
fi

# 2. 의존성 설치
echo "📦 패키지 설치 중..."
pnpm install

# 3. 환경변수 세팅
if [ ! -f .env.local ]; then
  cp .env.example .env.local
  echo "⚙️ .env.local 생성됨 — 실제 값을 입력해주세요"
else
  echo "⚙️ .env.local 이미 존재"
fi

# 4. 빌드 테스트
echo "🔨 전체 빌드 테스트..."
pnpm turbo run build

if [ $? -eq 0 ]; then
  echo ""
  echo "✅ 초기화 완료!"
  echo ""
  echo "다음 단계:"
  echo "  1. .env.local에 실제 API 키를 입력하세요"
  echo "  2. AIGrit 개발:  cd apps/aigrit && pnpm dev"
  echo "  3. babipanote 개발: cd apps/babipanote && pnpm dev"
  echo "  4. 전체 빌드:    pnpm turbo run build"
else
  echo ""
  echo "❌ 빌드 실패 — 에러를 확인하세요"
fi
