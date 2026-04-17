---
description: Rules for blog-core shared package
globs: ["packages/blog-core/**/*.ts", "packages/blog-core/**/*.tsx"]
---

# blog-core 패키지 규칙

## 핵심 원칙
- 사이트 특화 로직 절대 금지 — brand.config.ts에서 주입받아야 한다
- 모든 컴포넌트는 className prop 수용 (Tailwind 오버라이드 가능)
- 색상은 CSS 변수 또는 Tailwind 테마 토큰 (하드코딩 금지)
- 광고 컴포넌트는 brand.config의 enabled 플래그로 on/off 제어

## 수정 시 주의
- blog-core 수정은 AIGrit + babipanote 양쪽에 영향
- 수정 후 반드시 `pnpm turbo run build` 로 양쪽 빌드 확인
- 타입 변경 시 apps/*/brand.config.ts 호환성 확인

## 타입 규칙
- Post 타입은 types/post.ts에서만 정의
- BrandConfig 타입은 types/brand.ts에서만 정의
- unknown + 타입 가드 사용, any 금지
