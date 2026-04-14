# SETUP.md — AIGrit 앱 초기 세팅 상세

> **상태:** 본 문서의 1~5단계(프로젝트 생성, 의존성, Tailwind, 폰트, 디렉토리)는 모노레포 전환 이전에 이미 수행되었습니다. 현재는 **신규 세팅 가이드가 아니라 구성 요소 레퍼런스**로 활용하세요.
> **모노레포 컨텍스트:** 이 앱은 `unpack-blogs/` 워크스페이스의 일부이며 루트 `pnpm install` 한 번으로 모든 앱·패키지 의존성이 설치됩니다. 공유 엔진은 `@unpack/blog-core`에 있고, 앱은 이를 `transpilePackages`로 참조합니다.

## 사전 요구사항

- Node.js 20+ (LTS)
- pnpm 9+ (모노레포 패키지 매니저 — `package.json`의 `packageManager: pnpm@9.12.0` 고정)
- Git
- GitHub 계정 + `unpack-blogs` 저장소
- Vercel 계정 (GitHub 연결)
- aigrit.dev 도메인 (Vercel Domains 관리)

## 1. 신규 생성 (아카이브 — 이미 완료)

단일 레포 시절 다음 명령으로 초기 생성했습니다. 재실행하지 마세요.

```bash
npx create-next-app@latest aigrit \
  --typescript \
  --tailwind \
  --app \
  --src-dir \
  --eslint \
  --import-alias "@/*"
```

현재 상태 기준 신규 개발자 셋업:
```bash
git clone <unpack-blogs 저장소>
cd unpack-blogs
pnpm install                 # 모노레포 전체
cp .env.example .env.local   # 루트 템플릿 (또는 apps/aigrit/.env.local)
pnpm dev --filter=@unpack/aigrit
```

## 2. 의존성 (현재 앱 기준)

`apps/aigrit/package.json`에 이미 포함됨. 새로 추가할 때만 아래 참조.

```bash
# 모노레포 루트에서:
pnpm add --filter=@unpack/aigrit next-mdx-remote rehype-slug rehype-autolink-headings rehype-pretty-code
pnpm add --filter=@unpack/aigrit @tailwindcss/typography
pnpm add --filter=@unpack/aigrit @vercel/analytics @vercel/speed-insights

# 공유 엔진에서 사용하는 것들 (이미 blog-core에 존재):
#   gray-matter, reading-time  → packages/blog-core에 정의됨
```

### 패키지별 용도

| 패키지 | 용도 |
|--------|------|
| next-mdx-remote | MDX → React 변환 (서버 컴포넌트 호환) |
| gray-matter | frontmatter YAML 파싱 |
| reading-time | 읽기 시간 자동 계산 |
| rehype-slug | 헤딩에 자동 id 부여 (TOC용) |
| rehype-autolink-headings | 헤딩에 앵커 링크 추가 |
| rehype-pretty-code | 코드 블록 신택스 하이라이팅 |
| @tailwindcss/typography | prose 클래스 (블로그 본문 스타일) |
| @vercel/analytics | Vercel Web Analytics |
| @vercel/speed-insights | Core Web Vitals 추적 |

## 3. Tailwind 설정

`tailwind.config.ts`에 브랜드 컬러, 폰트, typography 플러그인 적용:

```typescript
import type { Config } from 'tailwindcss'

const config: Config = {
  darkMode: 'class',
  content: [
    './src/**/*.{ts,tsx,mdx}',
    './content/**/*.mdx',
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          primary: '#1E293B',
          secondary: '#F59E0B',
          'secondary-hover': '#D97706',
          'accent-red': '#EF4444',
          'accent-green': '#10B981',
        },
      },
      fontFamily: {
        sans: ['var(--font-pretendard)', 'var(--font-inter)', 'system-ui', 'sans-serif'],
        mono: ['var(--font-jetbrains)', 'monospace'],
      },
      typography: {
        DEFAULT: {
          css: {
            maxWidth: '72ch',
            a: { color: '#F59E0B', textDecoration: 'none' },
            'a:hover': { color: '#D97706' },
            code: {
              backgroundColor: '#F8FAFC',
              padding: '2px 6px',
              borderRadius: '4px',
              fontSize: '0.875rem',
            },
            'code::before': { content: 'none' },
            'code::after': { content: 'none' },
          },
        },
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
}

export default config
```

## 4. 폰트 설정

`src/app/layout.tsx`에서 next/font로 로드:

```typescript
import { Inter, JetBrains_Mono } from 'next/font/google'
import localFont from 'next/font/local'

const pretendard = localFont({
  src: '../../public/fonts/PretendardVariable.woff2',
  variable: '--font-pretendard',
  display: 'swap',
})

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
  display: 'swap',
})

const jetbrains = JetBrains_Mono({
  subsets: ['latin'],
  variable: '--font-jetbrains',
  display: 'swap',
})
```

Pretendard는 CDN 또는 woff2 파일 직접 포함. CDN 사용 시:
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/pretendardvariable.min.css" />
```

## 5. 디렉토리 (현재 상태)

다음 디렉토리는 이미 생성되어 있습니다:
```
apps/aigrit/
├── content/posts/          # 비어있음
├── public/{images,fonts}/
└── src/
    ├── app/
    └── components/{layout,blog,mdx,ads}/   # 비어있음 — Phase 2에서 채움
```

> **⚠ blog/mdx/ads 컴포넌트는 앱이 아니라 공유 엔진으로:** 해당 디렉토리는 과거 단일 레포 구조의 잔재입니다. 실제 컴포넌트는 `packages/blog-core/components/` 아래에 작성하고, 앱에서는 `@unpack/blog-core`로 import합니다. 앱 로컬 `src/components/`에는 **레이아웃 전용(Header/Footer/Sidebar)**만 남기는 것이 원칙(Phase 2).

## 6. Git 설정

루트 `.gitignore`에서 관리 (모노레포 통합). 앱 수준 추가 필요 항목이 있을 때만 `apps/aigrit/.gitignore`에 추가.

## 7. Vercel 연결

모노레포 1개 → Vercel 프로젝트 2개 구조. AIGrit 프로젝트는 **Root Directory = `apps/aigrit`**로 설정.

```bash
# Vercel CLI (선택)
npm i -g vercel
cd apps/aigrit && vercel link

# 또는 vercel.com에서 GitHub Import
# New Project → unpack-blogs 선택 → Root Directory = apps/aigrit
# Build Command: (기본) — Turborepo가 자동 감지
# Settings → Domains → aigrit.dev 추가
```

도메인은 Vercel Domains에서 관리. 외부 DNS 레지스트라 사용 시 Vercel 네임서버로 위임.

## 8. 확인

```bash
# 모노레포 루트에서
pnpm dev --filter=@unpack/aigrit
# http://localhost:3000 에서 기본 페이지 확인

# 전체 앱 빌드 체크 (blog-core 변경 시)
pnpm turbo run build
```
