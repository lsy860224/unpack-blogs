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

1. **frontmatter 파싱** — 최상단 `---`에서 slug, title 추출
2. **slug 중복 체크** — `apps/{APP}/content/posts/` 내 동일 slug 파일 존재 여부. 중복 시 중단
3. **마커 변환:**
   - `📸 [유형: 설명]` → `![설명](/images/{slug}/image-NN.png)` (NN은 01부터 순서 부여)
   - `📸 [설명]` (콜론 없음) → `![설명](/images/{slug}/image-NN.png)`
   - `🔗 [AffiliateLink: URL | 라벨]`:
     - aigrit: `<AffiliateLink href="URL" label="라벨" />`
     - babipanote: **경고 출력 후** `[라벨](URL)`
   - `📎 [RelatedPost: /blog/slug | 텍스트]` → `[텍스트](/blog/slug)`
   - `📎 [RelatedPost: /blog/slug]` → slug에서 제목 조회하여 링크 텍스트
4. **테이블 변환** — Craft 테이블 → MDX 파이프 테이블
5. **파일 생성:**
   - `apps/{APP}/content/posts/{slug}.mdx`
   - `mkdir -p apps/{APP}/public/images/{slug}/`
6. **이미지 확인** — 📸 마커 수와 실제 파일 대조. 누락 시 목록 출력 후 사용자에 안내
7. **빌드 테스트** — 모노레포 루트에서
   ```bash
   pnpm turbo run build --filter=@unpack/{APP}
   ```
   실패 시 에러 표시하고 중단 (커밋 금지)
8. **Git 커밋 + 푸시:**
   ```bash
   git add apps/{APP}/content/posts/{slug}.mdx apps/{APP}/public/images/{slug}/
   git commit -m "post({APP}): {title}"
   git push origin main
   ```
9. **결과 출력:**
   ```
   ✅ 발행 완료!
   📄 파일: apps/{APP}/content/posts/{slug}.mdx
   🔗 URL: https://{DOMAIN}/blog/{slug}
   ⏱️ Vercel 배포: 1~2분 후 라이브

   다음 단계:
   1. https://{DOMAIN}/blog/{slug} 접속하여 확인
   2. Google Search Console에서 색인 요청 (해당 사이트 속성)
   3. Obsidian에서 status: published 로 업데이트
   ```
   - DOMAIN: aigrit → `aigrit.dev`, babipanote → `babipanote.com`

## 주의사항

- frontmatter의 date가 미래 날짜면 경고 (발행은 진행)
- 이미지 파일 누락 시 빌드 에러 가능 → Step 7 실패하면 커밋하지 말고 사용자에게 알림
- URL에 프로토콜 없으면 `https://` 자동 추가
- 앱 지정이 없으면 먼저 AskUserQuestion 등으로 확인
