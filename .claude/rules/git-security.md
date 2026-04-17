---
description: Rules for git operations and sensitive files
globs: [".env*", ".gitignore", "*.pem", "*.key"]
---

# Git 및 보안 규칙

## 절대 금지
- .env.local 파일을 git에 커밋하지 않는다
- API 키, 시크릿을 코드에 하드코딩하지 않는다
- git push --force main/master 금지
- .pem, .key 파일 커밋 금지

## 커밋 컨벤션
- `feat: 기능 추가` — 새 기능
- `fix: 버그 수정` — 버그 픽스
- `post: 글 제목` — 새 블로그 글 발행
- `chore: 설정 변경` — 빌드, 설정, 도구
- `docs: 문서 업데이트` — 문서 변경
- `style: 코드 포맷` — 포맷팅만 (기능 변경 없음)
- `refactor: 리팩토링` — 동작 변경 없는 코드 개선

## 브랜치 전략
- main = 프로덕션 (직접 push)
- feature/* = 기능 개발 (필요 시)
- 1인 운영이라 PR 없이 main 직접 push OK
