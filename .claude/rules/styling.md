---
description: Rules for Tailwind CSS and styling
globs: ["apps/*/src/**/*.tsx", "apps/*/src/app/globals.css"]
---

# 스타일링 규칙

## Tailwind CSS
- Tailwind 유틸리티 클래스 사용 (inline style 금지)
- 색상은 globals.css @theme 토큰 또는 CSS 변수 사용
- 하드코딩 색상 (hex/rgb 직접 입력) 금지
- @apply는 최소한으로 — 컴포넌트 추출 선호

## 브랜드별 색상
- AIGrit: globals.css의 @theme 토큰 (Indigo 계열)
- babipanote: globals.css의 @theme 토큰 (Plum 계열)
- blog-core 컴포넌트는 CSS 변수로 색상 주입받음

## 반응형
- 모바일 퍼스트 (sm: → md: → lg:)
- 본문 최대 폭: prose 클래스 (max-w-prose 또는 max-w-3xl)
- 이미지: Next.js <Image> 컴포넌트 필수 (자동 최적화)
