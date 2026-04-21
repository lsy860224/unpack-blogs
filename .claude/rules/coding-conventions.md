---
description: TypeScript coding conventions and naming rules
globs: ["**/*.ts", "**/*.tsx"]
---

# 코딩 컨벤션

## 언어
- TypeScript strict mode 필수
- ESLint + Prettier (자동 포맷은 Hook이 처리)

## 네이밍
- 파일: kebab-case (`post-card.tsx`)
- 컴포넌트: PascalCase (`PostCard`)
- 함수·변수: camelCase (`getAllPosts`)
- 상수: UPPER_SNAKE_CASE (`DEFAULT_OG_IMAGE`)
- 타입·인터페이스: PascalCase (`PostFrontmatter`)

## 컴포넌트
- 함수형 컴포넌트 + React Hooks (클래스 컴포넌트 금지)
- `'use client'` 최소화 — 서버 컴포넌트 기본
- Props 타입은 별도 인터페이스로 정의

## 타입 안전
- `any` 금지 — `unknown` + 타입 가드 사용
- 반환 타입 명시 (추론 가능해도)
- 제네릭 적극 활용

## 임포트
- 절대 경로 사용 (`@unpack/blog-core`)
- barrel export (`index.ts`) 유지
- 미사용 import 금지 (ESLint가 잡음)

## 함수
- 순수 함수 선호 — 사이드 이펙트 최소화
- 함수당 하나의 책임
- 유틸리티는 `lib/` 하위에 배치
