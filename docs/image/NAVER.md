# 네이버 에디션 — 이미지 가이드

> **blog.naver.com/aigrit** — 네이버 블로그용 이미지 패키지는 본사이트와 다르게 **8장 표준** + **정사각형 프롤로그 썸네일** 별도 제작.
> 글은 [post/NAVER.md](../post/NAVER.md), SEO는 [seo/NAVER.md](../seo/NAVER.md) 참조.

---

## 🛡️ 절대 준수 사항

1. **OG 이미지는 반드시 제목을 포함한다** — 1200×630 본사이트 OG는 제목 포함 (Figma Master)
2. **프롤로그 썸네일은 1:1 정사각형 별도 제작** — 1080×1080 `00-thumb-square.png` (제목 포함)
3. **이미지 생성 시 Figma를 우선 고려**한다 — AIGrit OG Master + 네이버 자체 썸네일 스크립트
4. **인포그래픽은 NapkinAI를 우선 고려**한다 — 비교 차트·타임라인

---

## 1. 이미지 패키지 구조 (8장 표준)

```
docs/naver-setup/editions/images/{NN}-{slug}/
├── 00-thumb-square.png       ← 1080×1080, 프롤로그 대표 이미지 (신규)
├── 01-cover.png              ← 1200×630, 글 첫 이미지 (본사이트 og.png 재활용)
├── 02-{comparison}.png       ← Notion vs ChatGPT 등 비교
├── 03-{use-cases}.png        ← 활용 사례 인포그래픽 (NapkinAI)
├── 04-{pricing}.png          ← 가격 비교표 (NapkinAI 또는 Figma)
├── 05-divider.png            ← 구분선 (공통 재사용, Figma)
├── 06-{extra-infographic}.png ← PIL 신규 (카드 그리드 등)
├── 07-{timeline}.png         ← PIL 신규 (루틴·타임라인)
└── 08-closing.png            ← 마무리 (01-cover 재활용 가능)
```

---

## 2. OG 이미지 (01-cover.png)

### 규격
- **1200×630**, PNG, **제목 포함 필수**
- 본사이트 AIGrit OG 이미지 재활용 가능 (Figma Master `6:13`)
- 네이버 리프레이밍 제목으로 **재생성 권장** (e.g., "퇴근 후 30분, Notion AI로 부업 기반 만들기")

### 제작
- Figma OG Templates `1Md9ud8CQ43AQn2dKUo7YV` · AIGrit Component `6:13`
- 제목 텍스트 교체 → Export PNG 2x

---

## 3. 프롤로그 썸네일 (00-thumb-square.png) ⭐ 네이버 전용

### 왜 별도 제작인가
네이버 프롤로그 **이미지 강조형** 레이아웃은 썸네일을 **약 1:1 정사각형**으로 크롭. 1200×630 가로 OG를 그대로 쓰면 좌우가 잘리면서 제목이 깨진다.

### 규격
- **1080×1080**, PNG
- **제목 중앙 정렬** (필수)
- 좌상단 카테고리 배지 (Cyan) · 좌하단 `[AI]Grit` 워드마크 · 우하단 `aigrit.dev`

### 자동 생성 스크립트

`scripts/generate-naver-thumbs.py` (PIL + Pretendard 폰트):

```bash
python3 scripts/generate-naver-thumbs.py
```

스크립트 내 `POSTS` 리스트:
```python
{
    "slug": "02-notion-ai",
    "category": "AI 도구 리뷰",
    "title": "퇴근 후 30분, Notion AI로 부업 기반 만들기",
    "accent": "직장인 부업 5가지 활용법",
}
```

신규 에디션 추가 시 리스트에 entry 추가 → 실행.

### 등록 방법
글 편집 → 우측 톱니바퀴 → **대표 이미지** → `00-thumb-square.png` 업로드 → 저장
→ 프롤로그 + 카카오톡 공유 미리보기에 동시 적용

---

## 4. 본문 인포그래픽 (NapkinAI 우선)

### 위치별 가이드
| 슬롯 | 유형 | 추천 도구 |
|:---:|---|---|
| 02 | 비교 (A vs B) | **Figma** (수동 디자인, 네이버는 비주얼 무게감 중요) |
| 03 | 활용 사례 인포그래픽 | **NapkinAI** (`use_cases` 프롬프트) |
| 04 | 가격 비교표 | **Figma** 또는 **NapkinAI** 수평 bar |
| 06 | 카드 그리드 | **PIL 스크립트** (`/tmp/generate-infographics.py` 또는 Figma) |
| 07 | 타임라인 | **PIL 스크립트** 또는 NapkinAI timeline |

### NapkinAI 사용 시
- 프롬프트에 **네이버 독자 톤** 반영: "친근한·이해하기 쉬운", "한국어 레이블"
- AIGrit의 Cyan 외에 **포인트 컬러 허용** (네이버는 시각적 재미 중요)
- 브랜드 일관성보다 **클릭률·체류시간** 우선

---

## 5. 구분선 (05-divider.png)

- Figma 템플릿 공통 재사용 (3가지 variant: warm/cool/neutral)
- 원본: `/tmp/generate-dividers.py` 또는 Figma Dividers 페이지 (`1Md9ud8CQ43AQn2dKUo7YV`)
- 본문 섹션 간 시각 분기용 (체류시간 ↑)

---

## 6. 스크린샷

- 해상도 Retina 2x
- **네이버 독자 = 모바일 비율 높음** → 가로 1200px도 충분히 큼. 3000px 이상은 낭비
- 파일 크기 압축 필수 (네이버 업로드 속도 고려, 각 이미지 < 300KB)

---

## 7. 파일 네이밍 & 경로

```
docs/naver-setup/editions/images/{NN}-{slug}/
├── 00-thumb-square.png   ← 프롤로그 (신규 필수)
├── 01-cover.png
├── 02~07-{name}.png
└── 08-closing.png
```

**경로는 본사이트 `apps/aigrit/public/images/`와 분리**. 네이버 스마트에디터는 개별 업로드 방식이라 별도 관리.

---

## 8. Alt 텍스트

- 네이버 C-Rank는 alt 텍스트 신호 영향력 약함
- 그래도 **키워드 포함 alt 입력** (접근성 + 마이너 SEO)
- 스마트에디터 이미지 삽입 시 "대체 텍스트" 필드 채우기

---

## 9. 업로드 순서 (스마트에디터)

1. Craft 본문 복붙 (Cmd+A → Cmd+C → Cmd+V)
2. Craft의 이미지는 따라오지 않음 → **수동 재업로드 필수**
3. 본문 마커 위치에 번호 순서대로 이미지 삽입:
   `01 → 02 → 03 → 04 → 05 → 06 → 07 → 08`
4. 각 이미지 alt 텍스트 입력 (선택)
5. 우측 톱니바퀴 → **대표 이미지**: `00-thumb-square.png` 업로드

---

## 10. 검증 (`/review-post` 네이버 버전)

- [ ] `00-thumb-square.png` 존재 확인
- [ ] `01-cover.png` 존재 + 제목 포함 확인
- [ ] 본문 이미지 6장 이상 (02~08)
- [ ] 모든 파일이 1200px 이상 가로 (구분선 제외)
- [ ] 각 파일 < 300KB

---

## 11. 자주 쓰는 자동 생성 명령

```bash
# 프롤로그 썸네일 생성 (전 에디션 일괄)
python3 scripts/generate-naver-thumbs.py

# 구분선 생성
python3 /tmp/generate-dividers.py

# PIL 인포그래픽 (카드 그리드·타임라인)
python3 /tmp/generate-infographics.py

# 이미지 최적화
for dir in docs/naver-setup/editions/images/*/; do
  pngquant --quality=70-90 --ext .png --force "$dir"*.png
done
```

---

## 12. 관련

- [post/NAVER.md](../post/NAVER.md) — 네이버 글 작성 규칙
- [seo/NAVER.md](../seo/NAVER.md) — 네이버 SEO (C-Rank 이미지 영향)
- [image/AIGRIT.md](../image/AIGRIT.md) — 본사이트 OG 원본
- `docs/naver-setup/editions/images/README.md` — 에디션별 패키지 상세
- Memory: `reference_naver_prologue_thumb`, `reference_figma_og_templates`
