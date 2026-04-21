# Inspection Log Template

---

```markdown
# 점검 로그 YYYY-MM

- **점검일:** YYYY-MM-DD
- **점검자:** Claude Code / 사람 이름
- **실행 프롬프트:** (1/2/3/4/5 중 어느 것)
- **대상:** AIGrit / babipanote / both

## 요약

- 상태: 🟢 Green / 🟡 Yellow / 🔴 Red
- Must-fix 개수: N
- Should-fix 개수: N
- Nice-to-have 개수: N

## 점검 결과

### 1. (프롬프트별 주요 영역)

| 항목 | 상태 | 비고 |
|---|---|---|
| ... | ✅ | ... |
| ... | ⚠️ | ... |
| ... | ❌ | ... |

## Must-fix (즉시 수정)

1. [ ] (이슈) — (파일 경로) — (수정안)
2. [ ] ...

## Should-fix (이번 주 내)

1. [ ] ...

## Nice-to-have (백로그)

1. [ ] ...

## 자동화 제안

- (예: X 항목은 GitHub Actions 로 이관 가능)

## 다음 점검 시 확인할 것

- ...

## 참조

- Pull Request: #NNN
- 관련 문서: docs/design-system.md, docs/site-health-checklist.md
```
