# SETUP.md — 프로젝트 초기 세팅 상세

> CLAUDE.md의 기술 스택과 파일 구조를 실제로 구현하는 상세 가이드.
> `scripts/setup.sh`가 이 문서의 자동화 버전이다.

## 사전 요구사항

- Node.js 20+ (LTS)
- npm 10+ 또는 pnpm 9+
- Git
- GitHub 계정 + `aigrit` 저장소 (Public)
- Vercel 계정 (GitHub 연결)
- aigrit.dev 도메인 (Namecheap 구매)

## 1. 프로젝트 생성

```bash
npx create-next-app@latest aigrit \
  --typescript \
  --tailwind \
  --app \
  --src-dir \
  --eslint \
  --import-alias "@/*"
```

## 2. 의존성 설치

```bash
# 콘텐츠
npm install next-mdx-remote gray-matter reading-time rehype-slug rehype-autolink-headings rehype-pretty-code

# 스타일
npm install @tailwindcss/typography

# 분석
npm install @vercel/analytics @vercel/speed-insights

# 개발용
npm install -D @types/node
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

## 5. 디렉토리 생성

```bash
mkdir -p content/posts
mkdir -p public/images
mkdir -p public/fonts
mkdir -p src/components/{layout,blog,mdx,ads}
mkdir -p src/lib
mkdir -p src/types
```

## 6. Git 설정

`.gitignore`에 추가:
```
.env.local
.env*.local
node_modules/
.next/
out/
.vercel/
*.tsbuildinfo
```

## 7. Vercel 연결

```bash
# Vercel CLI (선택)
npm i -g vercel
vercel link

# 또는 vercel.com에서 GitHub Import
# Settings → Domains → aigrit.dev 추가
```

### Namecheap DNS → Vercel

Namecheap DNS 레코드 설정:
```
A     @     76.76.21.21
CNAME www   cname.vercel-dns.com.
```

## 8. 확인

```bash
npm run dev
# http://localhost:3000 에서 기본 페이지 확인
```
