#!/bin/bash
# ============================================
# babipanote 프로젝트 초기 세팅 스크립트
# 사용법: chmod +x scripts/setup.sh && ./scripts/setup.sh
# ============================================

set -e

echo ""
echo "🚀 babipanote 프로젝트 초기화 시작..."
echo "=================================="
echo ""

# --- 1. Node.js 버전 확인 ---
NODE_VERSION=$(node -v 2>/dev/null | sed 's/v//' | cut -d. -f1)
if [ -z "$NODE_VERSION" ] || [ "$NODE_VERSION" -lt 20 ]; then
  echo "❌ Node.js 20 이상이 필요합니다. (현재: $(node -v 2>/dev/null || echo '미설치'))"
  echo "   설치: https://nodejs.org/"
  exit 1
fi
echo "✅ Node.js $(node -v)"

# --- 2. 프로젝트 생성 (이미 있으면 스킵) ---
if [ ! -f "package.json" ]; then
  echo ""
  echo "📦 Next.js 프로젝트 생성 중..."
  npx create-next-app@latest . \
    --typescript \
    --tailwind \
    --app \
    --src-dir \
    --eslint \
    --import-alias "@/*" \
    --turbopack \
    --no-git \
    --yes
  echo "✅ Next.js 프로젝트 생성 완료"
else
  echo "✅ package.json 이미 존재 — 프로젝트 생성 스킵"
fi

# --- 3. 의존성 설치 ---
echo ""
echo "📦 의존성 설치 중..."

# 프로덕션 의존성
npm install \
  next-mdx-remote \
  gray-matter \
  reading-time \
  rehype-slug \
  rehype-autolink-headings \
  rehype-pretty-code \
  shiki \
  @tailwindcss/typography \
  @vercel/analytics \
  @vercel/speed-insights \
  next-themes \
  lucide-react

echo "✅ 의존성 설치 완료"

# --- 4. 디렉토리 구조 생성 ---
echo ""
echo "📁 디렉토리 구조 생성 중..."

mkdir -p content/posts
mkdir -p public/images
mkdir -p public/fonts
mkdir -p src/components/layout
mkdir -p src/components/blog
mkdir -p src/components/mdx
mkdir -p src/components/ads
mkdir -p src/lib
mkdir -p src/types
mkdir -p docs
mkdir -p scripts
mkdir -p .claude/commands
mkdir -p .github/workflows

echo "✅ 디렉토리 구조 생성 완료"

# --- 5. 환경변수 세팅 ---
if [ ! -f ".env.local" ]; then
  cp .env.example .env.local 2>/dev/null || true
  echo "⚙️  .env.local 생성됨 — 실제 값을 입력해주세요"
else
  echo "⚙️  .env.local 이미 존재"
fi

# --- 6. Pretendard 폰트 다운로드 (선택) ---
echo ""
if [ ! -f "public/fonts/PretendardVariable.woff2" ]; then
  echo "📝 Pretendard 폰트를 다운로드하시겠습니까? (y/N)"
  read -r DOWNLOAD_FONT
  if [ "$DOWNLOAD_FONT" = "y" ] || [ "$DOWNLOAD_FONT" = "Y" ]; then
    curl -sL "https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/woff2/PretendardVariable.woff2" \
      -o public/fonts/PretendardVariable.woff2
    echo "✅ Pretendard 폰트 다운로드 완료"
  else
    echo "⏭️  폰트 다운로드 스킵 — CDN 링크를 사용하세요"
  fi
else
  echo "✅ Pretendard 폰트 이미 존재"
fi

# --- 7. Git 초기화 ---
echo ""
if [ ! -d ".git" ]; then
  git init
  git add .
  git commit -m "feat: initial project setup by cc-kickstart"
  echo "✅ Git 초기화 + 첫 커밋 완료"
else
  echo "✅ Git 이미 초기화됨"
fi

# --- 8. 완료 ---
echo ""
echo "============================================"
echo "✅ babipanote 초기화 완료!"
echo "============================================"
echo ""
echo "다음 단계:"
echo "  1. .env.local에 실제 API 키를 입력하세요"
echo "  2. npm run dev 로 개발 서버를 시작하세요"
echo "  3. Claude Code를 열고:"
echo "     \"루트 CLAUDE.md와 apps/babipanote/CLAUDE.md를 읽고 작업을 시작해줘\""
echo "  4. 각 Phase의 프롬프트를 순서대로 실행하세요"
echo ""
echo "📖 문서:"
echo "  - CLAUDE.md              ← 프로젝트 컨텍스트 (자동 인식)"
echo "  - docs/ (babipanote 특화 문서는 Phase 2에서 작성 예정)"
echo "  - docs/SETUP.md          ← 초기 세팅 상세"
echo "  - docs/MDX_ENGINE.md     ← MDX 엔진 설계"
echo "  - docs/COMPONENTS.md     ← 컴포넌트 설계"
echo "  - docs/SEO_MONETIZATION.md ← SEO + 수익화"
echo "  - docs/DEPLOYMENT.md     ← 배포 + CI/CD"
echo "  - docs/PUBLISH_WORKFLOW.md ← 글 발행 워크플로우"
echo ""
