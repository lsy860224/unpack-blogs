---
description: Rules for brand configuration files
globs: ["apps/*/brand.config.ts"]
---

# brand.config.ts 규칙

## 구조
- 각 앱의 brand.config.ts가 사이트 정체성을 결정한다
- name, tagline, colors, monetization, labels, navigation, social 포함
- BrandConfig 타입(packages/blog-core/types/brand.ts)을 준수해야 한다

## AIGrit vs babipanote
- AIGrit: monetization.adsense = true, affiliateLinks = true
- babipanote: monetization.adsense = false, affiliateLinks = false
- 절대로 babipanote에 광고 플래그를 켜지 않는다

## 수정 시
- brand.config.ts 수정 후 로컬 dev 서버에서 시각적 확인
- 컬러 변경 시 BRAND_GUIDELINES.md와 일치하는지 확인
