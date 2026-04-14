# APP_SCAFFOLDING_GUIDE.md — AIGrit 앱 스케폴딩 단계별 가이드

> **스코프:** 이 문서는 `apps/aigrit/` 앱 내부 구현 절차(엔진, 컴포넌트, 페이지, 배포)만 다룹니다. 모노레포 전환 절차는 루트 `docs/MONOREPO_MIGRATION.md`를 참조하세요.
> **상태 (2026-04-15 기준):** Phase 0(초기화: setup.sh·tailwind·eslint)는 완료. Phase 1 이후(엔진/UI/배포)는 대부분 미착수 — 단, 모노레포 전환에 따라 일부 Phase가 루트 수준 작업과 겹치거나 `@unpack/blog-core`로 대체되었음. 각 Phase 실행 전 실제 상태와 대조하세요.
> **선행:** 루트 `pnpm install` 완료. `pnpm dev --filter=@unpack/aigrit`로 로컬 실행 가능.
> 각 Phase의 프롬프트를 Claude Code에 순서대로 입력하세요.
> 예상 총 소요: 5~6일 (하루 2~3시간 기준, 모노레포 전환 상태에 따라 변동)

---

## Phase 0: 프로젝트 초기화 (Day 1 전반)

### 0-1. setup.sh 실행

```bash
chmod +x scripts/setup.sh && ./scripts/setup.sh
```

### 0-2. 기본 설정 파일 확인

Claude Code 프롬프트:
```
CLAUDE.md를 읽고, docs/SETUP.md를 참조해서 다음을 확인/수정해줘:

1. tailwind.config.ts — 브랜드 컬러 + 폰트 + typography 플러그인 적용
2. tsconfig.json — strict mode, path alias (@/*)
3. .eslintrc.json — Next.js 기본 + import 순서 규칙
4. next.config.ts — MDX, 이미지 도메인 설정
5. .gitignore — .env.local, .next/, node_modules/

docs/SETUP.md에 있는 Tailwind Config 코드를 그대로 적용해.
```

---

## Phase 1: 블로그 엔진 (Day 1 후반 ~ Day 2)

### 1-1. 타입 + 유틸리티

Claude Code 프롬프트:
```
CLAUDE.md를 읽고, docs/MDX_ENGINE.md를 참조해서 다음을 구현해줘:

1. src/types/post.ts — PostMeta, PostData 타입 정의
2. src/lib/posts.ts — getAllPosts, getPostBySlug, getAllSlugs, getPostsByTag, getRelatedPosts, getAllTags 함수
3. src/lib/mdx.ts — compileMDX 함수 (next-mdx-remote + rehype 플러그인 체인)
4. src/lib/seo.ts — generateSiteMetadata, generatePostMetadata, SITE_CONFIG

docs/MDX_ENGINE.md의 타입과 함수 시그니처를 정확히 따라줘.
gray-matter로 frontmatter 파싱, reading-time으로 읽기 시간 계산.
```

### 1-2. 레이아웃 + 홈

Claude Code 프롬프트:
```
docs/COMPONENTS.md를 참조해서 다음을 구현해줘:

1. src/app/layout.tsx — 루트 레이아웃
   - Pretendard + Inter + JetBrains Mono 폰트 로드
   - 브랜드 메타데이터 (lib/seo.ts 사용)
   - GA4 스크립트 (환경변수 조건부)
   - AdSense 스크립트 (환경변수 조건부)
   - ThemeProvider (next-themes)
   - Header + Footer

2. src/components/layout/Header.tsx — 스펙 참조
3. src/components/layout/Footer.tsx — 스펙 참조
4. src/components/layout/ThemeToggle.tsx — 다크/라이트 전환

5. src/app/page.tsx — 홈 페이지
   - 히어로 섹션: AIGrit 소개 + UVP
   - Featured 글 목록 (PostCard featured variant)
   - 최신 글 목록
```

### 1-3. 블로그 목록 + 개별 글 페이지

Claude Code 프롬프트:
```
docs/MDX_ENGINE.md와 docs/COMPONENTS.md를 참조해서 다음을 구현해줘:

1. src/components/blog/PostCard.tsx — default + featured variant
2. src/components/blog/PostList.tsx — PostCard 목록 래퍼
3. src/components/blog/PostHeader.tsx — 글 상단 (태그, 제목, 메타)
4. src/components/blog/TableOfContents.tsx — H2/H3 기반 목차 (Intersection Observer)
5. src/components/blog/TagList.tsx — 태그 필터 UI

6. src/app/blog/page.tsx — 전체 글 목록 페이지
   - 태그 필터링
   - PostCard 그리드

7. src/app/blog/[slug]/page.tsx — 개별 글 페이지
   - generateStaticParams로 SSG
   - generateMetadata로 글별 SEO
   - MDX 렌더링 (커스텀 컴포넌트 매핑)
   - TableOfContents (사이드바)
   - RelatedPosts (하단)
```

### 1-4. 샘플 글 + 사이트맵

Claude Code 프롬프트:
```
다음을 생성해줘:

1. content/posts/hello-world.mdx — 샘플 글
   frontmatter:
   - title: "AIGrit 첫 번째 글 — 이 블로그는 무엇인가"
   - date: "2026-04-15"
   - slug: "hello-world"
   - description: "AIGrit 블로그를 시작합니다. AI 도구를 직접 써보고 솔직하게 비교하는 공간입니다."
   - tags: ["AIGrit", "소개"]
   - thumbnail: "/images/hello-world/thumbnail.png"
   - featured: true

2. src/app/sitemap.ts — 자동 사이트맵 (docs/SEO_MONETIZATION.md 참조)
3. src/app/robots.ts — robots.txt

빌드 확인: 모노레포 루트에서 `pnpm turbo run build --filter=@unpack/aigrit`
```

---

## Phase 2: MDX 커스텀 컴포넌트 (Day 3)

### 2-1. MDX 컴포넌트

Claude Code 프롬프트:
```
docs/COMPONENTS.md의 mdx/ 섹션을 참조해서 다음을 구현해줘:

1. src/components/mdx/AffiliateLink.tsx
   - 카드형 CTA 박스
   - rel="nofollow sponsored" 자동 적용
   - 클릭 시 GA4 이벤트 (affiliate_click)
   - "제휴 링크" 라벨 표시

2. src/components/mdx/CompareTable.tsx
   - 비교표 (boolean → ✅/❌ 아이콘)
   - 추천 칼럼 하이라이트
   - 모바일 가로 스크롤

3. src/components/mdx/Callout.tsx
   - info/warning/tip/danger 4종류
   - 좌측 컬러 바 + 아이콘

4. src/components/mdx/ProCon.tsx
   - 2열: 장점(Emerald) / 단점(Red)
   - 모바일 1열 스택

5. src/lib/mdx.ts의 components 매핑에 위 4개 추가

hello-world.mdx에 각 컴포넌트 사용 예시를 추가해서 테스트.
```

---

## Phase 3: SEO + 수익화 (Day 4)

### 3-1. 광고 + 분석

Claude Code 프롬프트:
```
docs/SEO_MONETIZATION.md를 참조해서 다음을 구현해줘:

1. src/components/ads/AdBanner.tsx — 애드센스 배너
   - 개발 환경: placeholder 박스 표시
   - 프로덕션: 실제 광고 로드

2. src/components/ads/AdInArticle.tsx — 인아티클 광고

3. src/components/layout/Analytics.tsx — GA4 스크립트 컴포넌트
   - @vercel/analytics, @vercel/speed-insights 연결

4. 구조화 데이터 (JSON-LD)
   - Article 스키마 (글 페이지에 자동 삽입)
   - WebSite 스키마 (루트 레이아웃)
```

### 3-2. 필수 페이지

Claude Code 프롬프트:
```
docs/SEO_MONETIZATION.md의 필수 페이지 섹션을 참조해서:

1. src/app/about/page.tsx — About 페이지
   - AIGrit 소개, 저자 소개
   - 블로그 방법론 ("직접 써보고 리뷰")
   - E-E-A-T에 유리한 콘텐츠

2. src/app/privacy/page.tsx — 개인정보처리방침
   - GA4, AdSense, Giscus 데이터 수집 고지
   - 쿠키 정책

3. src/app/disclaimer/page.tsx — 면책 고지
   - 제휴 마케팅 고지
   - 리뷰 독립성 선언

각 페이지에 적절한 SEO 메타데이터 포함.
```

---

## Phase 4: 마무리 (Day 5~6)

### 4-1. 댓글 + 관련 글

Claude Code 프롬프트:
```
docs/COMPONENTS.md를 참조해서:

1. src/components/blog/Comments.tsx — Giscus 댓글
   - 다크모드 자동 감지
   - lazy loading

2. src/components/blog/RelatedPosts.tsx — 관련 글 3개
   - 같은 태그 기반 추천

3. app/blog/[slug]/page.tsx에 Comments + RelatedPosts 추가
```

### 4-2. 다크모드 + 반응형 점검

Claude Code 프롬프트:
```
전체 페이지의 다크모드 + 반응형을 점검해줘:

1. next-themes 설정이 정상 작동하는지 확인
2. 모든 컴포넌트에 dark: 프리픽스 적용 여부 확인
3. 모바일(sm), 태블릿(md), 데스크탑(lg) 레이아웃 확인
4. Header 모바일 메뉴 동작 확인
5. 이미지 lazy loading + Next.js Image 최적화 확인
```

### 4-3. /publish-post 커맨드 설치

Claude Code 프롬프트:
```
docs/PUBLISH_WORKFLOW.md를 참조해서 .claude/commands/publish-post.md 파일을 생성해줘.

이 파일은 Claude Code에서 /publish-post 슬래시 커맨드로 사용된다.
PUBLISH_WORKFLOW.md의 마커 변환 규칙, 처리 순서, 결과 출력 형식을 정확히 따라줘.
```

### 4-4. 배포 전 체크 + 첫 배포

Claude Code 프롬프트:
```
docs/DEPLOYMENT.md의 배포 전 체크리스트를 실행해줘:

1. 모노레포 루트에서 pnpm turbo run lint
2. (빌드 과정이 타입 검증 포함) pnpm turbo run build
3. console.log 확인
4. 하드코딩된 URL 확인
5. 루트 .github/workflows/ci.yml 은 이미 존재 — 변경 불필요

모두 통과하면:
git add .
git commit -m "feat(aigrit): initial blog setup"
git push origin main
```

---

## Phase 5: 콘텐츠 시작 (Day 7~)

### 5-1. 첫 실전 글 발행

```
1. Obsidian에서 2026-04-20-claude-vs-chatgpt.md 열기
2. Claude 요청 프롬프트 복사 → Claude.ai에 붙여넣기
3. blog-wordpress 스킬 → Craft에 초안 저장
4. Craft에서 편집 (이미지 교체, 문체 수정)
5. Claude Code에서 /publish-post → 발행
6. Obsidian status: published 업데이트
```

이후 주 2회 반복.
