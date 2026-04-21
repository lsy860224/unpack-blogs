# Hooks & Rules 상세 가이드

## 개념

| | CLAUDE.md | Rules | Hooks |
|---|---|---|---|
| 성격 | 프로젝트 지도 | 파일별 표지판 | 강제 게이트 |
| 로드 | 매 세션 | 해당 파일 작업 시 | 해당 이벤트 시 |
| 보장 | 요청 (따를 수 있음) | 요청 (맥락 주입) | **결정론적 실행** |
| 기준 | "어기면 품질 떨어짐" | "어기면 품질 떨어짐" | **"어기면 사고남"** |

## Hooks

`.claude/settings.json`에 등록. `.claude/hooks/` 스크립트 실행.

### Hook 목록

| 이벤트 | 스크립트 | 동작 |
|---|---|---|
| PreToolUse (Bash) | `git-safety.sh` | force push · .env 커밋 · reset --hard · branch 삭제 차단 |
| PostToolUse (Write\|Edit) | `auto-format.sh` | Prettier 자동 실행 (.ts/.tsx/.json/.css/.md/.mdx) |
| PostToolUse (Write\|Edit) | `validate-mdx.sh` | MDX frontmatter 필수 필드 검증 + slug 포맷 경고 |
| PostToolUse (Write\|Edit) | `blog-core-guard.sh` | blog-core 수정 시 "양쪽 빌드 확인" 경고 |
| Notification | `notify-mac.sh` | macOS 네이티브 알림 (terminal-notifier or osascript) |
| Stop | `stop-typecheck.sh` | tsc --noEmit 실행. 실패 시 exit 2 → Claude 계속 작업 |

### 동작 흐름 예시

```
Claude: Edit(content/posts/hello-world.mdx)
  → [PostToolUse] auto-format.sh    → Prettier 실행
  → [PostToolUse] validate-mdx.sh   → frontmatter 검증
  → [PostToolUse] blog-core-guard.sh → blog-core 아니므로 스킵

Claude: Bash(git push --force origin main)
  → [PreToolUse] git-safety.sh
  → ⛔ {"decision": "block", "reason": "Force push 차단"}

Claude: "작업 완료"
  → [Stop] stop-typecheck.sh → tsc 실행
  → ❌ 타입 에러 → exit 2 → Claude 자동 수정 계속
  → ✅ 통과 → exit 0 → 정상 종료
```

### Hook 추가 방법

1. `.claude/hooks/새-스크립트.sh` 생성
2. `chmod +x .claude/hooks/새-스크립트.sh`
3. `.claude/settings.json`에 이벤트+matcher+command 등록
4. Claude Code 재시작

### 디버깅

- `Ctrl+O` — verbose 모드 (hook stdout/stderr 실시간 표시)
- `/hooks` — 활성 hooks 목록 확인

## Rules

`.claude/rules/*.md` — frontmatter `globs` 패턴에 매칭되는 파일 작업 시 자동 로드.

### Rule 목록

| 파일 | globs | 핵심 내용 |
|---|---|---|
| `mdx-content.md` | `*.mdx` | frontmatter 스키마, 마커 포맷, slug 불변 |
| `blog-core.md` | `packages/blog-core/**` | 사이트 특화 금지, className prop, 양쪽 빌드 |
| `brand-config.md` | `brand.config.ts` | BrandConfig 타입 준수, babipanote 광고 금지 |
| `nextjs-app.md` | `src/app/**` | SSG 기본, generateMetadata 필수, 서버 컴포넌트 |
| `git-security.md` | `.env*` | 커밋 금지, 커밋 컨벤션, 브랜치 전략 |
| `styling.md` | `*.tsx`, `globals.css` | Tailwind 유틸리티, 하드코딩 색상 금지, 모바일 퍼스트 |
| `coding-conventions.md` | `*.ts`, `*.tsx` | TS strict, 네이밍, 함수형 컴포넌트, ESLint |
| `deployment.md` | `vercel.json`, `turbo.json`, `ci.yml` | Vercel 배포 구조, CI 파이프라인 |

### Rule 추가 방법

`.claude/rules/새-규칙.md`:
```markdown
---
description: 설명
globs: ["패턴1", "패턴2"]
---
# 규칙 내용
```

### Settings 계층

| 파일 | 범위 | Git |
|---|---|:---:|
| `~/.claude/settings.json` | 전역 | ❌ |
| `.claude/settings.json` | 프로젝트 (Hooks) | ✅ |
| `.claude/settings.local.json` | 프로젝트 개인 (권한) | ❌ |

우선순위: local > project > global
