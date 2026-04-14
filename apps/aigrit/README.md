# AIGrit

AI 도구를 직접 써보고 솔직하게 비교하는 수익형 블로그.

- **도메인:** [aigrit.dev](https://aigrit.dev)
- **수익화:** Google AdSense + SaaS 제휴 마케팅
- **태그라인:** "AI의 알맹이만 남긴다"

## 로컬 개발

모노레포 루트(`unpack-blogs/`)에서 실행:

```bash
pnpm install                                   # 모노레포 전체 의존성
pnpm dev --filter=@unpack/aigrit               # AIGrit 개발 서버
pnpm turbo run build --filter=@unpack/aigrit   # 빌드
```

## 문서
- 앱 규칙 · 환경변수 · 브랜드: [`CLAUDE.md`](./CLAUDE.md)
- 앱 내부 구현 단계: [`docs/APP_SCAFFOLDING_GUIDE.md`](./docs/APP_SCAFFOLDING_GUIDE.md)
- 상세 설계(MDX·SEO·배포 등): [`docs/`](./docs/)
- 모노레포 전체 구조: 루트 [`CLAUDE.md`](../../CLAUDE.md)
- 공유 엔진 API: `@unpack/blog-core` (`packages/blog-core/`)
