import type { Metadata } from "next";
import { buildMetadata } from "@unpack/blog-core";
import { brandConfig } from "../../../brand.config";

export const metadata: Metadata = buildMetadata({
  title: "Disclaimer",
  description: `${brandConfig.name} 광고·제휴 고지사항`,
  siteName: brandConfig.name,
  siteUrl: brandConfig.url,
  path: "/disclaimer",
});

export default function DisclaimerPage() {
  return (
    <div className="mx-auto max-w-3xl px-6 py-12">
      <header className="mb-10 border-b border-[color-mix(in_oklab,var(--foreground)_8%,transparent)] pb-6">
        <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-[var(--color-brand-primary)]">
          Disclaimer
        </h1>
        <p
          className="mt-2 text-sm text-[color-mix(in_oklab,var(--foreground)_65%,transparent)]"
          style={{ fontFamily: "var(--font-mono)" }}
        >
          광고·제휴 고지사항 · 최종 업데이트 2026-04-15
        </p>
      </header>

      <section className="prose prose-neutral max-w-none dark:prose-invert prose-headings:tracking-tight prose-a:text-[var(--color-brand-primary)]">
        <h2>1. 사이트의 수익 구조</h2>
        <p>
          {brandConfig.name}은 다음 두 가지로 운영비·원고료를 충당합니다.
        </p>
        <ul>
          <li>
            <strong>Google AdSense 디스플레이 광고</strong> — 본문 상·하단, 본문
            중간에 삽입됩니다. 광고 영역은 <code>광고 · Sponsored</code>로 명시
            됩니다.
          </li>
          <li>
            <strong>제휴 마케팅(Affiliate) 링크</strong> — 리뷰 대상 도구의 공식
            가입 링크를 제공하고, 독자가 가입·구매 시 수수료를 받습니다. 해당
            링크는 <code>AD</code> 배지 또는{" "}
            <em>&quot;제휴 링크 · 구매 시 커미션 지급&quot;</em> 문구로 표시됩니
            다.
          </li>
        </ul>

        <h2>2. 리뷰 독립성 약속</h2>
        <ol>
          <li>
            제휴 보상은 <strong>독자가 자발적으로 결정</strong>할 때만 발생합니
            다. 링크 클릭·가입을 강요하지 않습니다.
          </li>
          <li>
            제휴 관계가 있는 도구라도 <strong>단점·한계는 그대로 기술</strong>
            합니다. 별점·권장 대상은 제휴와 무관하게 결정됩니다.
          </li>
          <li>
            <strong>스폰서십·협찬 리뷰는 받지 않습니다.</strong> 협찬 제안이
            있어도 본문 판단에 반영하지 않으며, 자금을 받고 호의적으로 작성하는
            글은 존재하지 않습니다.
          </li>
          <li>
            제휴 관계가 있는 도구의 리뷰에는 본문 상단에{" "}
            <strong>&quot;제휴 링크 포함&quot;</strong>을 고지합니다.
          </li>
        </ol>

        <h2>3. 정보의 한계</h2>
        <p>
          리뷰는 작성 시점의 제품 상태를 기준으로 합니다. 업데이트·가격 변경·정책
          변경이 반영되지 않았을 수 있으니, 구매·계약 전에는 반드시 제공사의 최신
          공식 정보를 확인하세요.
        </p>

        <h2>4. 책임 한계</h2>
        <p>
          {brandConfig.name}의 리뷰와 비교는 저자 개인의 실사용 경험·수치에 기반
          합니다. 이를 근거로 한 구매·투자·업무 결정의 결과에 대해{" "}
          {brandConfig.name}은 법적 책임을 지지 않습니다.
        </p>

        <h2>5. 외부 링크</h2>
        <p>
          외부 사이트로 연결되는 링크(<code>target=&quot;_blank&quot;</code>
          )의 콘텐츠에 대해서는 {brandConfig.name}이 책임지지 않습니다. 각 사이트
          의 개인정보 방침과 약관을 별도로 확인해주세요.
        </p>

        <h2>6. 문의</h2>
        <p>
          고지 내용에 대한 질문은{" "}
          {brandConfig.social.x ? (
            <a
              href={`https://x.com/${brandConfig.social.x.replace(/^@/, "")}`}
              target="_blank"
              rel="noopener noreferrer"
            >
              {brandConfig.social.x}
            </a>
          ) : (
            "사이트 운영자"
          )}
          로 연락해주세요.
        </p>
      </section>
    </div>
  );
}
