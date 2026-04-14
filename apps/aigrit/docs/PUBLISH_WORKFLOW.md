# PUBLISH_WORKFLOW.md — 글 발행 워크플로우

> Craft 완성본 → MDX 변환 → Git Push → Vercel 배포까지의 전체 흐름.
> `.claude/commands/publish-post.md` 슬래시 커맨드의 동작 명세.

## 전체 흐름

```
1. Craft에서 글 편집 완료
2. Craft 전체 선택 → 복사
3. Claude Code에서 /publish-post 실행
4. 붙여넣기 → MDX 변환 자동 처리
5. 이미지 파일 확인
6. git push → Vercel 배포
```

## /publish-post 커맨드

### 위치
`.claude/commands/publish-post.md`

### 입력
사용자가 Craft에서 복사한 전체 본문 텍스트. 최상단에 MDX frontmatter 코드 블록이 포함되어 있어야 함.

### 처리 순서

#### Step 1: frontmatter 추출
- 본문 최상단의 `---` 블록 파싱
- slug 값 추출 → 파일명 결정

#### Step 2: slug 중복 체크
```bash
ls content/posts/ | grep {slug}
```
- 중복이면 작업 중단 + 경고

#### Step 3: 마커 변환

| 입력 마커 | 출력 MDX |
|----------|---------|
| `📸 [설명]` | `![설명](/images/{slug}/image-NN.png)` |
| `🔗 [AffiliateLink: url \| label]` | `<AffiliateLink href="url" label="label" />` |
| `📎 [RelatedPost: /blog/slug]` | `[관련 글](/blog/slug)` |

이미지 번호(NN)는 등장 순서대로 01, 02, 03... 자동 부여.

#### Step 4: 테이블 변환
Craft 테이블 (탭/파이프 구분) → MDX 파이프 테이블 문법

#### Step 5: 파일 생성
```bash
# MDX 파일
content/posts/{slug}.mdx

# 이미지 폴더
mkdir -p public/images/{slug}/
```

#### Step 6: 이미지 확인
- 📸 마커 수만큼 이미지 파일이 필요한지 알림
- 파일이 없으면 placeholder 목록 출력:
  ```
  ⚠️ 다음 이미지 파일을 public/images/{slug}/에 추가하세요:
  - image-01.png (Claude 대화 화면)
  - image-02.png (ChatGPT 대화 화면)
  ```

#### Step 7: 빌드 테스트
```bash
npm run build
```
- 빌드 실패 시 에러 표시 + 수정 제안

#### Step 8: Git 커밋 + 푸시
```bash
git add content/posts/{slug}.mdx
git add public/images/{slug}/
git commit -m "post: {title}"
git push origin main
```

#### Step 9: 결과 출력
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

## 마커 변환 상세 규칙

### 📸 이미지 마커
```
입력: 📸 [스크린샷: Claude 대화 화면]
출력: ![Claude 대화 화면](/images/claude-vs-chatgpt/image-01.png)
```
- `📸` 뒤의 `[` `]` 사이가 alt 텍스트
- 콜론(`:`) 앞부분(유형)은 무시하고 뒷부분만 alt로 사용
- `📸 [Claude 화면]` → 콜론 없으면 전체가 alt

### 🔗 제휴 링크 마커
```
입력: 🔗 [AffiliateLink: https://claude.ai | Claude Pro 구독하기]
출력: <AffiliateLink href="https://claude.ai" label="Claude Pro 구독하기" />
```
- `|` 기준으로 URL과 label 분리
- URL에 프로토콜 없으면 `https://` 자동 추가

### 📎 내부 링크 마커
```
입력: 📎 [RelatedPost: /blog/cursor-review | Cursor 리뷰 보기]
출력: [Cursor 리뷰 보기](/blog/cursor-review)
```
- `|`가 없으면 slug에서 제목 자동 조회

## 이미지 네이밍 규칙

```
public/images/{slug}/
├── thumbnail.png      ← OG/썸네일 (1200×630)
├── image-01.png       ← 본문 이미지 (순서대로)
├── image-02.png
├── comparison.png     ← 비교 스크린샷 (선택)
└── screenshot-*.png   ← 스크린샷 (선택)
```

## 수동 발행 (커맨드 없이)

```bash
# 1. MDX 파일 직접 작성
vim content/posts/my-new-post.mdx

# 2. 이미지 배치
cp ~/screenshots/*.png public/images/my-new-post/

# 3. 빌드 확인
npm run build

# 4. 커밋 + 푸시
git add .
git commit -m "post: 새 글 제목"
git push
```
