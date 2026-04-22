# /publish-post

사용자가 붙여넣은 Craft 본문을 MDX로 변환해 **aigrit** 또는 **babipanote** 중 한 앱에 발행합니다.

## 인자

`/publish-post <app>` — `app`은 `aigrit` 또는 `babipanote`. 생략 시 먼저 사용자에게 물어보세요.

## 사전 조건

- 공용 마커·테이블 변환 규칙은 `apps/aigrit/docs/PUBLISH_WORKFLOW.md`를 참조.
- 앱별 차이:
  - **aigrit**: `AffiliateLink`·`AdInArticle` 등 MDX 컴포넌트 사용 가능. 커밋 메시지 prefix `post(aigrit):`, URL `https://aigrit.dev`.
  - **babipanote**: `AffiliateLink` 비활성 — 해당 라인은 경고 후 일반 링크 `[라벨](URL)`로 변환. 커밋 메시지 prefix `post(babipanote):`, URL `https://babipanote.com`.

## 입력

Craft에서 복사한 본문 전체. 최상단에 frontmatter 코드 블록 포함.

## 처리 순서 (APP = 선택한 앱)

1. **frontmatter 파싱** — 최상단 `---`에서 slug, title, date 추출
2. **재발행 여부 감지 (B-2)** — 대상 경로의 기존 파일 존재 여부로 판별:
   - aigrit: `apps/aigrit/content/posts/ko/{slug}.mdx`
   - babipanote: `apps/babipanote/content/posts/{slug}.mdx`

   - **미존재 → 최초 발행 (first publish)**
   - **존재 → 재발행 (republish)**: `⚠️ 기존 글 덮어쓰기: {slug}` 경고 출력. 사용자가 의도한 업데이트인지 진행 전에 한 번 확인받기 (파일이 이미 반영 배포된 상태라면 `date` 는 유지하고 본문·메타만 갱신).
3. **`updated` 필드 자동 계산 및 주입 (B-2):**
   - **최초 발행:** `updated = frontmatter.date` (입력된 date 값 그대로 복제)
   - **재발행:** `updated = ` **현재 KST 시각** `"YYYY-MM-DD HH:mm"`
     ```bash
     TZ=Asia/Seoul date +"%Y-%m-%d %H:%M"
     ```
     (동등 구현: node 스크립트에서 `date-fns-tz` 의 `formatInTimeZone(new Date(), "Asia/Seoul", "yyyy-MM-dd HH:mm")`)
   - 결과값을 frontmatter 의 `updated:` 키에 주입 — 기존에 같은 키가 있으면 덮어쓰기, 없으면 `date:` 다음 줄에 새로 삽입.
   - **`date` 필드는 절대 수정 금지** — 최초 발행 시점은 영구 유지 (검색엔진·애드센스 기준 발행일).
   - sitemap 의 `lastModified` 는 `updated`(있으면) → `date`(폴백) 순으로 읽음.
4. **`{LINK}` 마커 내부 링크 치환 (B-4)** — 본문 전체에서 아래 패턴 처리:

   - **정규식:** `\{LINK:\s*([a-z0-9-]+)\s*\|\s*anchor:\s*([^}]+)\}`
   - **치환:**
     - aigrit: `<Link href="/ko/blog/{slug}">{anchor}</Link>`
     - babipanote: `<Link href="/blog/{slug}">{anchor}</Link>`
   - **타겟 slug 실재 검증 (필수):**
     - aigrit: `apps/aigrit/content/posts/ko/{slug}.mdx` 파일 존재 확인
     - babipanote: `apps/babipanote/content/posts/{slug}.mdx` 파일 존재 확인
     - **미존재 시 즉시 중단:** `❌ LINK 타겟 "{slug}"가 존재하지 않습니다 (본문 라인 NN)` 출력 후 빌드·커밋 없이 종료
   - anchor 텍스트는 trim. 공백 양끝만 제거, 중간 공백은 유지.
   - `<Link>` 는 `defaultMdxComponents` 에 이미 주입되어 있어 MDX 에서 바로 사용 가능.

5. **기타 마커 변환:**
   - `📸 [유형: 설명]` → `![설명](/images/{slug}/image-NN.png)` (NN은 01부터 순서 부여)
   - `📸 [설명]` (콜론 없음) → `![설명](/images/{slug}/image-NN.png)`
   - `🔗 [AffiliateLink: URL | 라벨]`:
     - aigrit: `<AffiliateLink href="URL" label="라벨" />`
     - babipanote: **경고 출력 후** `[라벨](URL)`
   - `📎 [RelatedPost: /blog/slug | 텍스트]` → `[텍스트](/blog/slug)` (레거시 — 신규는 `{LINK}` 사용 권장)
   - `📎 [RelatedPost: /blog/slug]` → slug에서 제목 조회하여 링크 텍스트
6. **테이블 변환** — Craft 테이블 → MDX 파이프 테이블
7. **파일 생성 / 덮어쓰기:**
   - 최초 발행: 새 파일 생성
   - 재발행: 기존 파일 덮어쓰기 (본문·메타 전체 교체, `date` 필드만 보존)
   - 경로:
     - aigrit: `apps/aigrit/content/posts/ko/{slug}.mdx`
     - babipanote: `apps/babipanote/content/posts/{slug}.mdx`
   - `mkdir -p apps/{APP}/public/images/{slug}/`
8. **이미지 확인** — 📸 마커 수와 실제 파일 대조. 누락 시 목록 출력 후 사용자에 안내
8.1. **캡쳐 가이드 생성 (필수)** — 매 글마다 `docs/capture-guides/{app}-{slug}.md` 파일 생성:
    - `docs/capture-guides/README.md` 의 템플릿을 따라 작성
    - **자동 생성 이미지**(OG·다이어그램)는 `[x]` 체크 + "Claude 렌더 완료"
    - **사용자 캡쳐 필요 이미지**는 `[ ]` 미체크 + 도구 URL·캡쳐 방법·권장 영역·민감정보 마스킹 주의사항 명시
    - Obsidian Pipeline 카드의 `internal_links_planned`·`primary_keyword` 를 가이드 상단 메타에 포함
    - 파일이 이미 존재하면 보강(append) 없이 덮어쓰기
8.5. **Preflight Review (필수 게이트)** — `.claude/commands/review-post.md` 를 호출:
    - `/review-post {resolved_path}` 실행 (내부적으로 `post-reviewer` 에이전트 호출)
    - 결과 리포트를 사용자에게 출력
    - **PASS**: 사용자 명시 승인(`승인`/`approve`/`ok`/`진행`)까지 대기. 미승인 시 발행 중단
    - **WARN**: 경고 요약 후 사용자 판단 대기. 이대로 발행 선택 시에만 진행
    - **FAIL**: 발행 **차단**. 사용자가 강제 진행 지시해도 "수정 후 재검토 강력 권장" 고지하고 다시 한 번 승인 요구
    - 이 단계 통과 없이 9~10번(커밋·푸시) 절대 금지
9. **빌드 테스트** — 모노레포 루트에서
   ```bash
   pnpm turbo run build --filter=@unpack/{APP}
   ```
   실패 시 에러 표시하고 중단 (커밋 금지)
10. **Git 커밋 + 푸시:**
    ```bash
    git add apps/{APP}/content/posts/ apps/{APP}/public/images/{slug}/
    git commit -m "post({APP}): {title}"          # 최초 발행
    # 또는
    git commit -m "post({APP}): update — {title}" # 재발행
    git push origin main
    ```
11. **결과 출력:**
    ```
    ✅ 발행 완료! (MODE: 최초|재발행)
    📄 파일: apps/{APP}/content/posts/{LOCALE_DIR}{slug}.mdx
    🔗 URL: https://{DOMAIN}{LOCALE_PREFIX}/blog/{slug}
    📅 date (최초 발행일): {frontmatter.date}
    🕒 updated: {계산된 updated}
    ⏱️ Vercel 배포: 1~2분 후 라이브

    다음 단계:
    1. https://{DOMAIN}{LOCALE_PREFIX}/blog/{slug} 접속하여 확인
    2. Google Search Console에서 색인 요청 (해당 사이트 속성)
    3. Obsidian에서 status: published 로 업데이트
    ```
    - DOMAIN: aigrit → `aigrit.dev`, babipanote → `babipanote.com`
    - LOCALE_DIR: aigrit → `ko/`, babipanote → `` (없음)
    - LOCALE_PREFIX: aigrit → `/ko`, babipanote → `` (없음)

## 주의사항

- frontmatter 의 `date` 가 미래 날짜면 경고 (발행은 진행)
- 재발행 시 `date` 는 유지, `updated` 만 KST now 로 갱신. 본문·설명 등 메타는 새 입력으로 교체.
- 이미지 파일 누락 시 빌드 에러 가능 → Step 8 실패하면 커밋하지 말고 사용자에게 알림
- URL 에 프로토콜 없으면 `https://` 자동 추가
- 앱 지정이 없으면 먼저 AskUserQuestion 등으로 확인
