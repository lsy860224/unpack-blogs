---
description: Vercel deployment and CI/CD rules
globs: ["vercel.json", "turbo.json", ".github/workflows/**", "next.config.ts"]
---

# 배포 규칙

## Vercel 구조
- GitHub 모노레포 1개 → Vercel 프로젝트 2개
- AIGrit: Root Directory = `apps/aigrit`
- babipanote: Root Directory = `apps/babipanote`
- `packages/blog-core` 변경 시 양쪽 자동 재배포 (Turborepo 감지)

## 배포 플로우
```
git push origin main
  → Vercel 자동 빌드 (1~2분)
  → aigrit.dev + babipanote.com 동시 배포
```

## CI (GitHub Actions)
- `.github/workflows/ci.yml` — pnpm install + turbo build + lint
- PR 없이 main 직접 push (1인 운영)
- CI 실패 시 Vercel 배포도 차단

## turbo.json
- `build`: 양쪽 앱 병렬 빌드
- `dev`: 양쪽 앱 병렬 dev 서버
- `lint`: ESLint
- blog-core 의존성 자동 감지 — 수동 설정 불필요

## next.config.ts
- transpilePackages: `['@unpack/blog-core']` 필수
- output: standalone 아님 (Vercel 기본)
- images: domains에 외부 이미지 소스 등록
