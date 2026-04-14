# babipanote

바비파의 빌더 저널 — 1인 개발자가 AIGrit 블로그와 GentleLab 앱을 만들어가는 과정을 기록하는 사이트.

- **도메인:** [babipanote.com](https://babipanote.com)
- **레이아웃:** 타임라인형 (연대기)
- **수익화:** 없음 (브랜드 자산 축적)

## 로컬 개발

모노레포 루트(`unpack-blogs/`)에서 실행:

```bash
pnpm install                                   # 모노레포 전체 의존성
pnpm dev --filter=@unpack/babipanote           # babipanote 개발 서버
pnpm turbo run build --filter=@unpack/babipanote  # 빌드
```

## 문서
- 앱 규칙 · 환경변수 · 브랜드: [`CLAUDE.md`](./CLAUDE.md)
- 모노레포 전체 구조: 루트 [`CLAUDE.md`](../../CLAUDE.md)
- 공유 엔진 API: `@unpack/blog-core` (`packages/blog-core/`)
