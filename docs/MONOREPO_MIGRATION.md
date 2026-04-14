# 모노레포 전환 가이드 (아카이브)

> **상태 (2026-04-15 기준):** Phase 0-1 / 0-2 완료. Phase 1 이후는 미착수.
> **용도:** 이 문서는 AIGrit 단일 레포에서 unpack-blogs 모노레포로 전환하던 시점의 단계별 지침 아카이브입니다. Phase 0 섹션의 프롬프트들은 이미 수행되었으므로 재실행하지 마세요 — 의사결정 맥락을 되짚을 때만 참조하세요.
> **다음 단계(Phase 1~3)의 실제 실행 계획:** 필요 시 새 계획 문서를 작성하거나 Claude Code와 대화하며 결정하세요.
> **앱 스케폴딩(앱 내부 구현) 가이드:** `apps/aigrit/docs/APP_SCAFFOLDING_GUIDE.md`를 참조하세요.

---

## Phase 0: 모노레포 전환 (Day 1 전반)

### 0-1. Turborepo + pnpm 워크스페이스 초기화

Claude Code 프롬프트:
```
현재 AIGrit 프로젝트를 Turborepo 모노레포로 리팩터링해줘.

지금 상태: 단일 Next.js 프로젝트 (aigrit/)
목표 상태: Turborepo 모노레포 (unpack-blogs/)

순서:
1. 루트에 pnpm-workspace.yaml 생성
   - packages: ["packages/*", "apps/*"]

2. 루트 package.json 생성
   - name: "unpack-blogs"
   - scripts: dev/build/lint을 turbo로 래핑
   - devDependencies: turbo

3. turbo.json 생성
   - build: dependsOn ["^build"]
   - dev: cache false, persistent true
   - lint: {}

4. 기존 AIGrit 코드를 apps/aigrit/로 이동
   - package.json의 name을 "@unpack/aigrit"로 변경

5. apps/babipanote/ 디렉토리 생성 (빈 Next.js 앱)
   - apps/aigrit를 복사하되 content/posts/는 비우기
   - package.json name을 "@unpack/babipanote"로 변경

6. packages/blog-core/ 디렉토리 생성
   - package.json name: "@unpack/blog-core"
   - tsconfig.json 설정

모든 경로 참조와 import가 정상 동작하는지 확인.
```

### 0-2. 공유 코드 추출 (blog-core)

Claude Code 프롬프트:
```
apps/aigrit/에서 재사용 가능한 코드를 packages/blog-core/로 추출해줘.

추출 대상:
1. lib/mdx.ts → packages/blog-core/lib/mdx.ts
2. lib/posts.ts → packages/blog-core/lib/posts.ts
3. lib/seo.ts → packages/blog-core/lib/seo.ts
4. types/post.ts → packages/blog-core/types/post.ts
5. components/blog/* → packages/blog-core/components/blog/
   (PostCard, PostHeader, TableOfContents, RelatedPosts, Comments)
6. components/mdx/* → packages/blog-core/components/mdx/
   (Callout, CompareTable, ProCon, AffiliateLink)
7. components/ads/* → packages/blog-core/components/ads/
   (AdBanner, AdInArticle)
8. hooks/* → packages/blog-core/hooks/

packages/blog-core/index.ts에서 모든 export를 barrel export.

apps/aigrit/의 import를 "@unpack/blog-core"로 전부 변경.
apps/babipanote/에서도 동일하게 "@unpack/blog-core"에서 import.

빌드 확인: turbo run build
```

---

## Phase 1: 브랜드 분리 시스템 (Day 1 후반)

### 1-1. brand.config.ts 타입 정의

Claude Code 프롬프트:
```
packages/blog-core/types/brand.ts에 BrandConfig 타입을 정의해줘:

export interface BrandConfig {
  // 사이트 기본
  name: string;              // "AIGrit" | "babipanote"
  tagline: string;           // 한 줄 설명
  description: string;       // SEO용 설명 (150자)
  url: string;               // "https://aigrit.dev"
  locale: string;            // "ko-KR"

  // 네비게이션
  nav: { label: string; href: string }[];

  // 소셜 링크
  social: {
    github?: string;
    x?: string;
    instagram?: string;
  };

  // 테마
  theme: {
    primary: string;          // HEX
    secondary: string;        // HEX
    accent: string;           // HEX
    fontHeading: string;      // "Pretendard"
    fontBody: string;         // "Pretendard"
    fontCode: string;         // "JetBrains Mono"
  };

  // 수익화
  monetization: {
    adsense: boolean;
    affiliateLinks: boolean;
  };

  // 레이아웃
  layout: {
    style: "category" | "timeline";  // 홈 레이아웃
    showSidebar: boolean;
    postsPerPage: number;
  };

  // GA/Giscus
  analytics: {
    gaId?: string;
  };
  comments: {
    giscusRepo?: string;
    giscusRepoId?: string;
    giscusCategory?: string;
  };
}
```

### 1-2. 사이트별 brand.config.ts 생성

Claude Code 프롬프트:
```
두 사이트의 brand.config.ts를 생성해줘.

apps/aigrit/brand.config.ts:
- name: "AIGrit"
- tagline: "AI 도구, 직접 쓰고 솔직하게 씁니다"
- url: "https://aigrit.dev"
- nav: Home, Blog, About, Disclaimer
- theme.primary: "#6366F1" (Indigo)
- theme.secondary: "#10B981" (Emerald)
- theme.accent: "#F59E0B" (Amber)
- monetization: adsense true, affiliateLinks true
- layout.style: "category"
- layout.showSidebar: true

apps/babipanote/brand.config.ts:
- name: "babipanote"
- tagline: "만드는 과정을 기록합니다"
- url: "https://babipanote.com"
- nav: Home, Blog, Projects, About
- theme.primary: "#8B5CF6" (Violet)
- theme.secondary: "#F97316" (Orange)
- theme.accent: "#06B6D4" (Cyan)
- monetization: adsense false, affiliateLinks false
- layout.style: "timeline"
- layout.showSidebar: false

BrandConfig 타입을 import해서 타입 안전하게 작성.
```

### 1-3. BrandProvider 컨텍스트 생성

Claude Code 프롬프트:
```
packages/blog-core/에 BrandProvider를 만들어줘.

1. contexts/brand-context.tsx
   - React Context로 BrandConfig를 앱 전체에 주입
   - useBrand() 훅으로 어디서든 접근

2. 기존 blog-core 컴포넌트들을 수정:
   - 하드코딩된 사이트명 → useBrand().name
   - 하드코딩된 색상 → CSS 변수 또는 useBrand().theme
   - AdBanner/AdInArticle → useBrand().monetization.adsense로 on/off
   - AffiliateLink → useBrand().monetization.affiliateLinks로 on/off

3. 각 앱의 layout.tsx에서 BrandProvider로 감싸기:
   - import { brandConfig } from "@/brand.config"
   - <BrandProvider config={brandConfig}>

4. Tailwind에서 CSS 변수 기반 색상 사용:
   - tailwind.config.ts에 extend.colors에 brand-primary 등 추가
   - BrandProvider가 :root에 --brand-primary 등 CSS 변수 설정
```

---

## Phase 2: babipanote 사이트 구현 (Day 2)

### 2-1. babipanote 레이아웃

Claude Code 프롬프트:
```
apps/babipanote/의 레이아웃을 빌더 저널 스타일로 만들어줘.

AIGrit과 다른 점:
1. 홈 페이지: 타임라인형 (날짜순 스크롤, 사이드바 없음)
2. Header: 미니멀 (로고 + 네비게이션만, 검색 없음)
3. Footer: 소셜 링크 + "AIGrit" / "GentleLab" 프로젝트 링크
4. /projects 페이지 추가:
   - AIGrit 블로그 카드 (링크: aigrit.dev)
   - GentleLab 앱 시리즈 카드 (GentleDo, GentleFast, GentleStudy)
   - 각 프로젝트 상태 뱃지 (개발중/운영중)

폰트: Pretendard (한글) + Inter (영문) + JetBrains Mono (코드)
babipanote는 광고 없음 — AdBanner/AdInArticle 비활성.
```

### 2-2. babipanote 첫 글

Claude Code 프롬프트:
```
apps/babipanote/content/posts/에 첫 글을 생성해줘.

파일: hello-world.mdx

frontmatter:
  title: "빌더 저널을 시작합니다"
  date: "2026-04-14"
  slug: "hello-world"
  description: "1인 개발자 바비파가 AIGrit 블로그와 GentleLab 앱을 만들어가는 과정을 기록합니다."
  tags: ["빌더저널", "시작"]
  thumbnail: "/images/hello-world.png"
  category: "저널"

내용 (200자 내외 placeholder):
- 자기소개 (바비파, 1인 개발자, 가족)
- 왜 빌더 저널을 시작하는지
- AIGrit: AI 도구 리뷰 블로그 (aigrit.dev)
- GentleLab: 가족용 앱 시리즈
- 앞으로 공유할 내용 (수익 공개, 개발 과정, 실패담)
```

---

## Phase 3: 배포 설정 (Day 2~3)

### 3-1. Vercel 프로젝트 설정

Claude Code 프롬프트:
```
Vercel 배포를 위한 설정을 정리해줘.

1. .github/workflows/ci.yml 생성:
   - push/PR 시 turbo run lint && turbo run build
   - pnpm 캐시 사용

2. apps/aigrit/vercel.json (필요 시):
   - headers, redirects 등

3. apps/babipanote/vercel.json (필요 시):
   - headers, redirects 등

4. 루트 .gitignore 업데이트:
   - node_modules, .next, .turbo, .env.local, dist

Vercel에서 수동 설정할 것 (Claude Code 외부):
- 모노레포 → 프로젝트 2개 생성
- AIGrit: Root Directory = apps/aigrit
- babipanote: Root Directory = apps/babipanote
- 각 프로젝트에 환경변수 설정
- 각 프로젝트에 도메인 연결
```

### 3-2. 최종 빌드 확인

Claude Code 프롬프트:
```
배포 전 전체 점검을 해줘:

1. pnpm install — 의존성 정상 설치
2. turbo run build — 양쪽 사이트 빌드 성공
3. turbo run lint — lint 에러 없음
4. blog-core에서 양쪽 앱으로의 import 정상 확인
5. 각 앱의 brand.config.ts 반영 확인
   - aigrit: 카테고리 레이아웃 + 광고 활성
   - babipanote: 타임라인 레이아웃 + 광고 비활성
6. MDX 글 렌더링 정상 확인 (양쪽 각 1개 이상)
7. .env.example 업데이트 (양쪽 환경변수 모두 포함)
8. console.log 정리
9. CLAUDE.md와 실제 구조 일치 여부 확인
```

---

## 리팩터링 후 워크플로우

### 글 추가
```bash
# AIGrit에 글 추가
apps/aigrit/content/posts/새-글.mdx 생성
git add . && git commit -m "post(aigrit): 글 제목" && git push

# babipanote에 글 추가
apps/babipanote/content/posts/새-글.mdx 생성
git add . && git commit -m "post(babipanote): 글 제목" && git push
```

### 공유 컴포넌트 수정
```bash
# blog-core 수정 → 양쪽 사이트 모두 재배포
packages/blog-core/components/... 수정
turbo run build  # 양쪽 빌드 확인 후 push
```

### 새 MDX 컴포넌트 추가
```bash
# 1. blog-core에 컴포넌트 생성
packages/blog-core/components/mdx/NewComponent.tsx

# 2. blog-core/index.ts에 export 추가

# 3. 양쪽 앱의 MDX 설정에 컴포넌트 등록
```
