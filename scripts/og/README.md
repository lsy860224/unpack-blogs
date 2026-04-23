# OG 썸네일 생성 스크립트

BRAND_GUIDELINES + THUMBNAIL.md 스펙대로 babipanote + AIGrit 의 OG 썸네일(1200×630 PNG)을 일괄 생성한다.

## 왜 Python PIL + Figma 투트랙인가

- **Figma 파일** ([UnpackBlogs — OG Templates](https://www.figma.com/design/1Md9ud8CQ43AQn2dKUo7YV)) = 디자인 단일 소스. Master Component + Component Properties + Variables 로 관리
- **Python PIL** = 실제 PNG 렌더링. Figma Cloud에는 Pretendard 미포함이라 `get_screenshot` 추출 시 body 텍스트가 Inter 폴백으로 렌더됨. PIL은 로컬 Pretendard OTF 사용 → 정확한 BRAND_GUIDELINES 일치

Figma는 스펙 변경 시 시각 확인용, 실제 생성은 이 스크립트가 담당.

## 사용법

```bash
# 1) 폰트 다운로드 (최초 1회)
bash scripts/og/download-fonts.sh

# 2) 모든 MDX frontmatter 에서 posts-sample.json 갱신
bash scripts/og/extract-frontmatter.sh

# 3) 23장 일괄 생성
python3 scripts/og/generate-og-all.py
```

## 필수 폰트

다음 파일이 `/tmp/og-fonts/` 에 있어야 한다 (`download-fonts.sh` 가 자동 배치):

| 파일 | 소스 | 용도 |
|---|---|---|
| `GowunBatang-Bold.ttf` | Google Fonts | babipanote 제목·로고·저자 |
| `GowunBatang-Regular.ttf` | Google Fonts | (예비) |
| `Lora-Bold.ttf` | Google Fonts | babipanote 인용 장식 |
| `Pretendard-Bold.otf` | [github.com/orioncactus/pretendard](https://github.com/orioncactus/pretendard) | AIGrit 제목·서브타이틀 + babipanote body |
| `Pretendard-SemiBold.otf` | 동일 | 뱃지·로고 |
| `Pretendard-Regular.otf` | 동일 | body·date·domain |

## Figma 템플릿에 Pretendard 추가하는 법 (선택사항)

`use_figma` MCP로 OG를 생성하고 싶을 경우, Figma Cloud에 Pretendard가 없어서 Inter 폴백이 발생한다. 정확한 렌더가 필요하면:

1. [Figma 데스크톱 앱](https://www.figma.com/downloads/) 다운로드·로그인
2. 메뉴: **Figma → Settings → Font installers**
3. "Enable local fonts" 토글 ON
4. 시스템에 Pretendard 설치 (이 스크립트가 받은 OTF 를 `~/Library/Fonts/` 로 복사)
5. Figma 재실행 → 파일에서 Pretendard 사용 가능

> 팀 공유 폰트로 업로드하려면 **Enterprise 플랜 필요**. Pro 플랜(현재)에서는 개별 설정만 가능.

## 생성 스크립트 구조

- `generate-og-all.py`:
  - `/tmp/og-posts.json` 읽기
  - `render_babipanote()` / `render_aigrit()` 별도 함수
  - 긴 제목은 `BB_TITLE_OVERRIDES` / `AG_TITLE_OVERRIDES` 로 단축 관리
  - AIGrit 서브타이틀은 `AG_SUBTITLES` dict 로 매핑 (frontmatter 에 subtitle 필드 없어서)

- `posts-sample.json`:
  - 2026-04-23 생성 스냅샷. 실제 사용 시 `extract-frontmatter.sh` 로 최신화 후 사용
