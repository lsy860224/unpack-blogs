# /publish-post

사용자가 붙여넣은 Craft 본문을 MDX로 변환하여 발행합니다.

## 사전 조건

- `docs/PUBLISH_WORKFLOW.md`를 먼저 읽고 마커 변환 규칙을 숙지할 것

## 입력

사용자가 Craft에서 복사한 전체 본문. 최상단에 frontmatter 코드 블록 포함.

## 처리 순서

1. **frontmatter 파싱** — 최상단 `---` 블록에서 slug, title 추출
2. **slug 중복 체크** — `content/posts/` 폴더에서 동일 slug 파일 존재 여부 확인. 중복 시 중단
3. **마커 변환:**
   - `📸 [유형: 설명]` → `![설명](/images/{slug}/image-NN.png)` (NN = 순서번호 01, 02...)
   - `📸 [설명]` (콜론 없음) → `![설명](/images/{slug}/image-NN.png)`
   - `🔗 [AffiliateLink: URL | 라벨]` → `<AffiliateLink href="URL" label="라벨" />`
   - `📎 [RelatedPost: /blog/slug | 텍스트]` → `[텍스트](/blog/slug)`
   - `📎 [RelatedPost: /blog/slug]` → slug에서 제목 조회하여 링크 텍스트 사용
4. **테이블 변환** — Craft 테이블 → MDX 파이프 테이블 문법
5. **파일 생성:**
   - `content/posts/{slug}.mdx`
   - `mkdir -p public/images/{slug}/`
6. **이미지 확인** — 📸 마커 수와 실제 파일 대조. 누락 시 목록 출력
7. **빌드 테스트** — `npm run build` 실행. 실패 시 에러 표시
8. **Git 커밋 + 푸시:**
   ```bash
   git add content/posts/{slug}.mdx public/images/{slug}/
   git commit -m "post: {title}"
   git push origin main
   ```
9. **결과 출력:**
   ```
   ✅ 발행 완료!
   📄 파일: content/posts/{slug}.mdx
   🔗 URL: https://aigrit.dev/blog/{slug}
   ⏱️ Vercel 배포: 1~2분 후 라이브

   다음 단계:
   1. https://aigrit.dev/blog/{slug} 접속하여 확인
   2. Google Search Console에서 색인 요청
   3. Obsidian에서 status: published 로 업데이트
   ```

## 주의사항

- frontmatter의 date가 미래 날짜면 경고 (발행은 진행)
- 이미지 파일 누락 시 빌드 에러 발생 가능 → 확인 후 push
- URL에 프로토콜 없으면 https:// 자동 추가
