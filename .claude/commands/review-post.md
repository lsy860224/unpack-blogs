# /review-post — 발행 전 Preflight 검증

블로그 글 MDX 파일을 `post-reviewer` 에이전트로 검증하고 리포트를 출력합니다. 모든 `post(aigrit)`·`post(babipanote)` 커밋 전에 반드시 실행.

## 인자

`/review-post <target>` — 대상 지정 방법 3가지:

- **파일 경로** 직접: `/review-post apps/aigrit/content/posts/ko/notion-ai-guide.mdx`
- **slug 지정**: `/review-post aigrit/notion-ai-guide` 또는 `/review-post babipanote/sprint-week1-review`
- **인자 생략**: 마지막으로 편집한 MDX 파일 자동 감지 (`git status --short | grep ".mdx"`)

## 실행 순서

1. **대상 파일 확정**:
   - 인자 있으면 그대로 사용
   - 인자 없으면 `git status -s | grep -E "apps/.*content/posts/.*\.mdx$"` 로 대기 중 MDX 식별
   - 여러 개면 사용자에게 선택 요청
2. **post-reviewer 에이전트 호출**:
   - Agent tool 사용 · `subagent_type: "post-reviewer"`
   - 프롬프트: `파일 경로 = {resolved_path}. .claude/rules/post-requirements.md 기준으로 preflight 검증 리포트 생성.`
3. **결과 처리**:
   - PASS → 사용자에게 "발행 진행할까요? (승인 / 수정 / 중단)" 명시 질문
   - WARN → 경고 요약 후 "이대로 발행 / 수정 후 재검토" 질문
   - FAIL → "❌ 발행 차단. 위 문제 수정 후 다시 `/review-post` 실행" 안내
4. **승인 대기**:
   - 사용자가 `승인`, `approve`, `ok`, `진행` 중 하나 명시하면 그 결과를 반환
   - 외 응답은 "보류" 로 간주하고 발행 차단

## 출력

post-reviewer 에이전트 리포트 그대로 + 마지막에 **승인 여부 질문**:

```
---

**발행 승인**: 위 결과를 확인하셨나요?
- ✅ `승인` 또는 `approve` → /publish-post 진행
- ✏️ `수정` → 문제 항목 보수 후 `/review-post` 재실행
- ⛔ `중단` → 커밋·푸시 완전 중단
```

## 관련
- 기준 룰: `.claude/rules/post-requirements.md`
- 에이전트: `.claude/agents/post-reviewer.md`
- 연계: `/publish-post` 는 커밋 직전 이 커맨드 결과를 기다림

$ARGUMENTS
