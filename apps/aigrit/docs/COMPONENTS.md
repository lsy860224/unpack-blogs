# COMPONENTS.md — 컴포넌트 상세 설계

> 모든 React 컴포넌트의 역할, props, 구현 가이드.
> **모노레포 배치:** blog/mdx/ads 컴포넌트는 **공유 엔진** `@unpack/blog-core`에 배치됨. layout만 앱 로컬. Phase 1 완료 후 컴포넌트들은 `useBrand()` 훅으로 사이트별 설정 주입 받음(하드코딩 금지).

## 디렉토리 구조 (목표 — Phase 2 이후)

### 공유 엔진 (`packages/blog-core/`)
```
blog-core/components/
├── blog/           ← 블로그 전용 컴포넌트 (양쪽 사이트 공통)
│   ├── PostCard.tsx
│   ├── PostHeader.tsx
│   ├── PostList.tsx
│   ├── TableOfContents.tsx
│   ├── RelatedPosts.tsx
│   ├── TagList.tsx
│   └── Comments.tsx       ← Giscus (brand.config.ts의 comments로 설정 주입)
├── mdx/            ← MDX 본문 내 커스텀 컴포넌트
│   ├── AffiliateLink.tsx  ← brand.config.ts의 monetization.affiliateLinks 플래그로 on/off
│   ├── CompareTable.tsx
│   ├── Callout.tsx
│   └── ProCon.tsx
└── ads/            ← 광고 컴포넌트
    ├── AdBanner.tsx       ← brand.config.ts의 monetization.adsense 플래그로 on/off
    └── AdInArticle.tsx
```

앱에서는 barrel export로 import:
```typescript
import { PostCard, TableOfContents, Callout, AdBanner } from "@unpack/blog-core"
```

### 앱 로컬 (`apps/aigrit/src/components/`)
```
src/components/
└── layout/         ← 페이지 레이아웃 (사이트별 커스텀)
    ├── Header.tsx      ← AIGrit: 로고 + 네비 + 검색 + ThemeToggle
    ├── Footer.tsx      ← AIGrit: 3열 + 제휴 고지
    ├── Sidebar.tsx     ← AIGrit: 카테고리 · 최근 글 (babipanote는 없음)
    └── ThemeToggle.tsx
```

`babipanote`는 `apps/babipanote/src/components/layout/`에 자체 Header/Footer(미니멀, 사이드바 없음) 작성.

## layout/ 컴포넌트

## layout/ 컴포넌트

### Header.tsx
- AIGrit 워드마크 로고 (좌)
- 네비게이션: 홈 / 블로그 / About
- ThemeToggle (우)
- 모바일: 햄버거 메뉴
- 스크롤 시 배경 블러 효과 (`backdrop-blur`)
- sticky top-0

### Footer.tsx
- 3열 레이아웃: 브랜드 소개 / 네비게이션 / SNS 링크
- 하단: copyright + privacy/disclaimer 링크
- 다크모드 대응

### ThemeToggle.tsx
- 라이트/다크 모드 전환 버튼
- `next-themes` 패키지 사용
- 아이콘: 해/달 (lucide-react)
- localStorage에 선택 저장

## blog/ 컴포넌트
> 위치: `packages/blog-core/components/blog/*` (Phase 2). 타입은 `@unpack/blog-core`의 `Post` / `PostSummary` / `PostFrontmatter`. 문서에 `PostMeta`로 표기된 과거 네이밍은 `PostFrontmatter`로 읽으세요.

### PostCard.tsx
```typescript
import type { PostSummary } from "@unpack/blog-core"
interface PostCardProps {
  post: PostSummary
  variant?: 'default' | 'featured'  // featured는 홈에서 사용
}
```
- 썸네일 이미지 (Next.js Image, lazy loading)
- 제목 + 설명 (2줄 clamp)
- 태그 (Amber 배지)
- 날짜 + 읽기 시간
- hover: 카드 전체가 링크, 미묘한 상승 효과

### PostHeader.tsx
```typescript
interface PostHeaderProps {
  meta: PostMeta
}
```
- 글 상단: 태그 배지 → 제목 (H1) → 설명 → 날짜/읽기시간/작성자
- 썸네일 이미지 (full width)
- 소셜 공유 버튼 (X, 링크 복사)

### TableOfContents.tsx
- MDX 본문의 H2/H3 태그를 파싱하여 목차 생성
- 사이드바 (데스크탑) / 접이식 (모바일)
- 스크롤 시 현재 섹션 하이라이트 (Intersection Observer)
- sticky positioning

### RelatedPosts.tsx
```typescript
interface RelatedPostsProps {
  currentSlug: string
  tags: string[]
  limit?: number  // 기본 3
}
```
- 같은 태그를 가진 글 3개 표시
- PostCard compact 버전 사용

### Comments.tsx
- Giscus 임베드 (GitHub Discussions 기반)
- 다크모드 자동 감지하여 테마 전환
- lazy loading (뷰포트 진입 시 로드)

## mdx/ 컴포넌트

### AffiliateLink.tsx
```typescript
interface AffiliateLinkProps {
  href: string
  label: string
  description?: string
}
```
- 카드형 CTA 박스
- Amber 테두리 + "제휴 링크" 라벨 (투명성)
- `rel="nofollow sponsored"` + `target="_blank"` 자동 적용
- 클릭 시 GA4 이벤트 전송

### CompareTable.tsx
```typescript
interface CompareTableProps {
  headers: string[]
  rows: { feature: string; values: (string | boolean)[] }[]
  recommendation?: number  // 추천 칼럼 인덱스
}
```
- 비교표 (2~4열)
- boolean 값은 ✅/❌ 아이콘으로 표시
- 추천 칼럼: Emerald 배경 강조
- 모바일: 가로 스크롤 with 첫 칼럼 고정

### Callout.tsx
```typescript
interface CalloutProps {
  type: 'info' | 'warning' | 'tip' | 'danger'
  title?: string
  children: React.ReactNode
}
```
- 좌측 컬러 바 + 아이콘 + 배경색
- info: Blue, warning: Amber, tip: Emerald, danger: Red

### ProCon.tsx
```typescript
interface ProConProps {
  pros: string[]
  cons: string[]
}
```
- 2열 레이아웃: 장점(Emerald) / 단점(Red)
- 각 항목 앞에 ✅/❌ 아이콘
- 모바일: 1열로 스택

## ads/ 컴포넌트

### AdBanner.tsx
```typescript
interface AdBannerProps {
  slot: string        // 애드센스 광고 슬롯 ID
  format?: 'auto' | 'rectangle' | 'horizontal'
  className?: string
}
```
- Google AdSense 디스플레이 광고
- 개발 환경에서는 placeholder 박스 표시
- 애드센스 ID는 환경변수에서 로드
- `ins` 태그 기반

### AdInArticle.tsx
- 글 본문 중간에 삽입하는 인아티클 광고
- AdBanner와 동일하지만 format="fluid" 고정
- MDX 본문에서 `{/* ad */}` 마커 위치에 자동 삽입 또는 수동 배치

## 공통 규칙

1. 모든 컴포넌트는 **함수형 + named export**
2. Props 인터페이스는 컴포넌트 파일 내 정의 (별도 파일 X)
3. Tailwind 클래스만 사용 (인라인 스타일, CSS 모듈 사용 안 함)
4. 다크모드: `dark:` 프리픽스로 항상 대응
5. 접근성: 시맨틱 HTML, aria-label, 키보드 네비게이션
6. 반응형: 모바일 퍼스트 (sm → md → lg)
