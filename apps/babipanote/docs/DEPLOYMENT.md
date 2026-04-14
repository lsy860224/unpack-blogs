# DEPLOYMENT.md — 배포 + CI/CD 상세 설계

> Vercel 배포, 도메인 설정, GitHub Actions CI, 배포 전 체크리스트.

## Vercel 배포 구조

```
GitHub (aigrit 저장소)
  → push to main
    → Vercel 자동 빌드 (Next.js)
      → aigrit.dev 라이브 (1~2분)
```

### Vercel 설정

| 항목 | 값 |
|------|-----|
| Framework | Next.js (자동 감지) |
| Build Command | `next build` (기본값) |
| Output Directory | `.next` (기본값) |
| Node.js Version | 20.x |
| 환경변수 | Vercel Dashboard → Settings → Environment Variables |

### 환경변수 등록 (Vercel)

Vercel 대시보드에서 다음 변수를 등록:

```
NEXT_PUBLIC_GA_ID=G-XXXXXXXXXX
NEXT_PUBLIC_ADSENSE_ID=ca-pub-XXXXXXX
NEXT_PUBLIC_GISCUS_REPO=aigrit/aigrit
NEXT_PUBLIC_GISCUS_REPO_ID=R_xxxxx
NEXT_PUBLIC_GISCUS_CATEGORY_ID=DIC_xxxxx
NEXT_PUBLIC_SITE_URL=https://aigrit.dev
```

모든 변수를 Production + Preview + Development에 적용.

## 도메인 설정

### Namecheap DNS → Vercel

Namecheap Advanced DNS에서:

| Type | Host | Value | TTL |
|------|------|-------|-----|
| A | @ | 76.76.21.21 | Automatic |
| CNAME | www | cname.vercel-dns.com. | Automatic |

### Vercel 도메인 추가

```
Vercel Dashboard → Project → Settings → Domains
→ aigrit.dev 추가
→ www.aigrit.dev → aigrit.dev 리다이렉트 설정
```

SSL은 Vercel이 자동으로 Let's Encrypt 인증서 발급.

## GitHub Actions CI

`.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint-and-build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm

      - run: npm ci

      - name: Lint
        run: npm run lint

      - name: Type Check
        run: npx tsc --noEmit

      - name: Build
        run: npm run build
```

### CI가 체크하는 것

1. ESLint 에러 없음
2. TypeScript 타입 에러 없음
3. Next.js 빌드 성공 (SSG 포함)

CI가 실패하면 Vercel 배포도 자동으로 중단됨.

## 배포 전 체크리스트

```
□ npm run lint — Lint 에러 없음
□ npx tsc --noEmit — TypeScript 에러 없음
□ npm run build — 빌드 성공
□ .env.local의 모든 변수가 Vercel에도 등록되었는지 확인
□ console.log 제거 (개발용 로그)
□ 하드코딩된 URL이 있으면 환경변수/SITE_CONFIG으로 전환
□ 새 글의 이미지 파일이 public/images/{slug}/에 있는지 확인
□ 새 글의 frontmatter 필수 필드 모두 작성되었는지 확인
```

## 배포 워크플로우

### 일반 글 추가

```bash
git add content/posts/{slug}.mdx public/images/{slug}/
git commit -m "post: {글 제목}"
git push origin main
```

### 기능 변경

```bash
git add .
git commit -m "feat: {기능 설명}"
git push origin main
```

### 긴급 수정

```bash
git add .
git commit -m "fix: {수정 내용}"
git push origin main
```

## 프리뷰 배포

Vercel은 PR마다 자동으로 프리뷰 URL을 생성:

```
main에 PR 생성
→ Vercel이 프리뷰 빌드
→ https://aigrit-{hash}.vercel.app 에서 확인
→ 머지 → main 배포
```

## 모니터링

### Vercel Analytics
- `@vercel/analytics` 패키지로 자동 수집
- Core Web Vitals (LCP, FID, CLS) 추적
- Vercel Dashboard → Analytics 에서 확인

### Vercel Speed Insights
- `@vercel/speed-insights` 패키지
- 실제 사용자 성능 데이터 (RUM)

### 에러 모니터링
- 초기: Vercel 빌트인 로그 (Functions → Logs)
- 향후: Sentry 연동 (글 50개 이상 시)
