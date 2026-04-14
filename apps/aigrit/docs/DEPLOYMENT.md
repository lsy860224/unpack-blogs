# DEPLOYMENT.md — 배포 + CI/CD 상세 설계

> Vercel 배포, 도메인 설정, GitHub Actions CI, 배포 전 체크리스트.
> **모노레포 구조:** 하나의 GitHub 저장소(`unpack-blogs`) → Vercel 프로젝트 2개(AIGrit, babipanote). AIGrit 프로젝트의 Root Directory는 `apps/aigrit`.

## Vercel 배포 구조

```
GitHub (unpack-blogs 저장소)
  → push to main
    → Vercel 두 프로젝트 동시 감지
        ├── AIGrit 프로젝트 (Root: apps/aigrit) → aigrit.dev
        └── babipanote 프로젝트 (Root: apps/babipanote) → babipanote.com
      → Turborepo가 변경 파일 분석해 필요한 앱만 재빌드
        (apps/aigrit 변경 → AIGrit만, apps/babipanote 변경 → babipanote만,
         packages/blog-core 변경 → 양쪽 모두)
```

### Vercel 설정 (AIGrit 프로젝트)

| 항목 | 값 |
|------|-----|
| Framework | Next.js (자동 감지) |
| Root Directory | `apps/aigrit` |
| Build Command | `pnpm turbo run build --filter=@unpack/aigrit` (또는 Vercel 자동 감지 기본값) |
| Install Command | (기본값 — 루트 `pnpm install`이 워크스페이스 해석) |
| Output Directory | `.next` (기본값) |
| Node.js Version | 20.x |
| 환경변수 | Vercel Dashboard → Settings → Environment Variables |

babipanote 프로젝트도 동일 규칙, `Root Directory = apps/babipanote`, filter는 `@unpack/babipanote`.

### 환경변수 등록 (Vercel)

AIGrit 프로젝트 대시보드에서 다음 변수를 등록:

```
NEXT_PUBLIC_GA_ID=G-XXXXXXXXXX
NEXT_PUBLIC_ADSENSE_ID=ca-pub-XXXXXXX
NEXT_PUBLIC_GISCUS_REPO=lsy860224/aigrit
NEXT_PUBLIC_GISCUS_REPO_ID=R_xxxxx
NEXT_PUBLIC_GISCUS_CATEGORY=Announcements
NEXT_PUBLIC_GISCUS_CATEGORY_ID=DIC_xxxxx
NEXT_PUBLIC_SITE_URL=https://aigrit.dev
```

babipanote는 별도 프로젝트에서 AdSense 제외하고 등록. 모든 변수를 Production + Preview + Development에 적용.

## 도메인 설정

### Vercel Domains

도메인은 Vercel에서 직접 관리하거나 외부 레지스트라에서 Vercel 네임서버로 위임.

- `aigrit.dev` → AIGrit 프로젝트
- `babipanote.com` → babipanote 프로젝트
- `www.aigrit.dev` → `aigrit.dev` 리다이렉트 (Vercel Dashboard에서 설정)

SSL은 Vercel이 자동으로 Let's Encrypt 인증서 발급.

## GitHub Actions CI

루트 `.github/workflows/ci.yml` (모노레포 전체 검사):

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
      - uses: pnpm/action-setup@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: pnpm

      - run: pnpm install --frozen-lockfile
      - name: Lint
        run: pnpm turbo run lint
      - name: Build
        run: pnpm turbo run build
```

### CI가 체크하는 것

1. 모노레포 전체 ESLint 에러 없음 (`turbo run lint`)
2. 양쪽 앱 Next.js 빌드 성공 — SSG 포함 (`turbo run build`)
3. TypeScript 에러는 Next.js 빌드 과정에서 함께 검증됨

CI가 실패해도 Vercel은 별도로 빌드를 시도하므로, CI는 **PR 머지 게이트** 역할이 주.

## 배포 전 체크리스트

```
□ pnpm turbo run lint — Lint 에러 없음 (양쪽 앱)
□ pnpm turbo run build — 양쪽 앱 빌드 성공
□ .env.local의 모든 변수가 해당 Vercel 프로젝트에도 등록되었는지 확인
□ console.log 제거 (개발용 로그)
□ 하드코딩된 URL이 있으면 환경변수/brand.config.ts로 전환 (Phase 1 이후)
□ 새 글의 이미지 파일이 apps/{app}/public/images/{slug}/에 있는지 확인
□ 새 글의 frontmatter 필수 필드(title, date, slug, description) 모두 작성
□ packages/blog-core 변경 시 양쪽 앱 영향 여부 확인
```

## 배포 워크플로우

### 일반 글 추가 (AIGrit)

```bash
git add apps/aigrit/content/posts/{slug}.mdx apps/aigrit/public/images/{slug}/
git commit -m "post(aigrit): {글 제목}"
git push origin main
```

### 일반 글 추가 (babipanote)

```bash
git add apps/babipanote/content/posts/{slug}.mdx apps/babipanote/public/images/{slug}/
git commit -m "post(babipanote): {글 제목}"
git push origin main
```

### 기능 변경

```bash
git add .
git commit -m "feat(aigrit): {기능 설명}"   # 또는 feat(babipanote), feat(blog-core)
git push origin main
```

### 긴급 수정

```bash
git add .
git commit -m "fix(aigrit): {수정 내용}"
git push origin main
```

## 프리뷰 배포

Vercel은 PR마다 자동으로 두 프로젝트 각각 프리뷰 URL을 생성:

```
main에 PR 생성
→ Vercel이 변경된 앱(또는 blog-core 변경 시 양쪽)만 프리뷰 빌드
→ https://aigrit-{hash}.vercel.app 및/또는 https://babipanote-{hash}.vercel.app
→ 머지 → main 프로덕션 배포
```

## 모니터링

### Vercel Analytics
- `@vercel/analytics` 패키지로 자동 수집
- Core Web Vitals (LCP, FID, CLS) 추적
- Vercel Dashboard → Analytics 에서 프로젝트별 확인

### Vercel Speed Insights
- `@vercel/speed-insights` 패키지
- 실제 사용자 성능 데이터 (RUM)

### 에러 모니터링
- 초기: Vercel 빌트인 로그 (Functions → Logs)
- 향후: Sentry 연동 (글 50개 이상 시)
