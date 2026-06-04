import type { Metadata } from "next";
import { buildMetadata, toOgLocale } from "@unpack/blog-core";
import { brandConfig, getLocalizedBrand } from "../../../../brand.config";

export async function generateMetadata({
  params,
}: {
  params: Promise<{ locale: string }>;
}): Promise<Metadata> {
  const { locale } = await params;
  const localized = getLocalizedBrand(locale);
  const description =
    locale === "en"
      ? `${localized.name} Terms of Service`
      : `${localized.name} 이용약관`;
  return buildMetadata({
    title: "Terms of Service",
    description,
    siteName: localized.name,
    siteUrl: localized.url,
    path: `/${locale}/terms`,
    locale: toOgLocale(locale),
    hrefLangs: {
      ko: "/ko/terms",
      en: "/en/terms",
      "x-default": "/ko/terms",
    },
  });
}

export default async function TermsPage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  return locale === "en" ? <TermsEn /> : <TermsKo />;
}

function Header({ subtitle }: { subtitle: string }) {
  return (
    <header className="mb-10 border-b border-[color-mix(in_oklab,var(--foreground)_8%,transparent)] pb-6">
      <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-[var(--color-brand-primary)]">
        Terms of Service
      </h1>
      <p className="mt-2 text-sm font-mono text-[color-mix(in_oklab,var(--foreground)_65%,transparent)]">
        {subtitle}
      </p>
    </header>
  );
}

function TermsKo() {
  return (
    <div className="mx-auto max-w-3xl px-6 py-12">
      <Header subtitle="이용약관 · 최종 업데이트 2026-06-04" />
      <section className="prose prose-neutral max-w-none dark:prose-invert prose-headings:tracking-tight prose-a:text-[var(--color-brand-primary)]">
        <h2>1. 약관의 동의</h2>
        <p>
          본 약관은 {brandConfig.name}({brandConfig.url})이 제공하는 콘텐츠·웹사이트
          서비스(이하 &quot;서비스&quot;)의 이용 조건을 규정합니다. 이용자는 서비스
          접속·이용 시점에 본 약관에 동의한 것으로 간주됩니다. 동의하지 않는 경우
          서비스 이용을 중단해 주세요.
        </p>

        <h2>2. 서비스 설명</h2>
        <p>
          {brandConfig.name}은 AI 도구·생산성 자동화·1인 빌더 워크플로우에 관한
          리뷰·비교·실전 가이드를 제공합니다. 서비스는 정보 제공을 목적으로 하며,
          전문적 자문(법률·세무·투자 등)이 아닙니다.
        </p>

        <h2>3. 콘텐츠 저작권</h2>
        <ol>
          <li>
            {brandConfig.name}의 본문·이미지·인포그래픽·코드 예제 등 모든 콘텐츠의
            저작권은 별도 표기가 없는 한 {brandConfig.name} 또는 정당한 권리자에게
            귀속됩니다.
          </li>
          <li>
            <strong>개인적·비상업적 인용</strong>은 출처({brandConfig.url})를 명기한
            경우 허용됩니다. 인용 분량은 단일 글 기준 200자 이내를 권장합니다.
          </li>
          <li>
            <strong>상업적 재배포·전문 복제·AI 학습용 대량 스크래핑</strong>은
            사전 서면 허가 없이 금지됩니다.
          </li>
          <li>
            제3자 저작물(스크린샷·로고·인용문 등)은 해당 권리자의 라이선스를 따르며,
            오인용·권리 침해 발견 시 즉시 수정합니다.
          </li>
        </ol>

        <h2>4. 이용자의 책임</h2>
        <ol>
          <li>
            서비스의 정보를 근거로 한 모든 결정(구매·계약·투자·업무 적용 등)은
            <strong>이용자 본인의 책임</strong>이며, {brandConfig.name}은 그 결과에
            대해 책임지지 않습니다.
          </li>
          <li>
            서비스 접근을 방해하거나 운영을 저해하는 행위(자동화된 대량 요청·우회
            크롤링·보안 취약점 탐색 등)는 금지됩니다.
          </li>
          <li>
            댓글(Giscus 등 외부 댓글 시스템 포함)에서 타인의 권리를 침해하거나
            법령에 위반되는 내용은 게시할 수 없습니다.
          </li>
        </ol>

        <h2>5. 정보의 정확성 면책</h2>
        <p>
          모든 리뷰·가이드·수치는 <strong>작성 시점</strong>의 제품 상태·정책·가격에
          기반합니다. 이후 업데이트·정책 변경·시장 변동이 반영되지 않았을 수 있으며,
          이용자는 구매·결정 전 반드시 공식 출처에서 최신 정보를 확인해야 합니다.
          {brandConfig.name}은 콘텐츠의 완전성·시의성을 보증하지 않습니다.
        </p>

        <h2>6. 보증의 부인</h2>
        <p>
          서비스는 &quot;있는 그대로(AS IS)&quot; 제공됩니다. {brandConfig.name}은
          서비스의 무중단성·오류 부재·특정 목적 적합성에 대해 명시적·묵시적 보증을
          하지 않습니다. 일시적 서비스 중단·데이터 손실·외부 시스템(분석·광고·댓글
          등) 장애에 대한 책임을 지지 않습니다.
        </p>

        <h2>7. 책임의 제한</h2>
        <p>
          관련 법령이 허용하는 최대 범위 내에서 {brandConfig.name}은 서비스 이용으로
          인한 직접·간접·부수적·결과적 손해(매출 손실·데이터 손실·평판 손상 등)에
          대해 책임지지 않습니다. 본 약관에 따른 모든 책임의 합산 한도는 이용자가
          서비스에 대해 직접 지급한 금액(없는 경우 0원)으로 제한됩니다.
        </p>

        <h2>8. 외부 링크에 대한 면책</h2>
        <p>
          서비스에는 외부 웹사이트로 연결되는 링크가 포함될 수 있습니다. 외부 사이트의
          콘텐츠·약관·개인정보 처리·상품·서비스에 대해 {brandConfig.name}은 책임지지
          않습니다. 외부 링크 이용 시 해당 사이트의 약관과 정책을 별도로 확인해 주세요.
        </p>

        <h2>9. 광고·제휴 마케팅</h2>
        <p>
          {brandConfig.name}은 Google AdSense 디스플레이 광고와 제휴 마케팅 링크를
          포함합니다. 광고·제휴 관련 상세 사항은{" "}
          <a href={`${brandConfig.url}/ko/disclaimer`}>광고·제휴 고지사항</a>을,
          쿠키·개인정보 처리는{" "}
          <a href={`${brandConfig.url}/ko/privacy`}>개인정보 처리방침</a>을 참고해
          주세요. 광고 클릭·제휴 가입의 결과는 이용자 본인 책임입니다.
        </p>

        <h2>10. 약관의 변경</h2>
        <p>
          {brandConfig.name}은 법령 변경, 서비스 운영 정책 조정, 신규 기능 도입 등을
          반영하기 위해 본 약관을 사전 통지 없이 개정할 수 있습니다. 개정된 약관은
          본 페이지에 게시된 시점부터 효력이 발생하며, 페이지 상단의{" "}
          <em>&quot;최종 업데이트&quot;</em> 일자를 갱신합니다. 개정 후에도 서비스를
          계속 이용하는 경우 변경된 약관에 동의한 것으로 간주됩니다.
        </p>

        <h2>11. 관할법 및 분쟁 해결</h2>
        <p>
          본 약관의 해석과 적용은 대한민국 법령에 따릅니다. 서비스 이용과 관련하여
          분쟁이 발생한 경우 양 당사자는 우선 협의를 통해 해결하며, 협의가 어려운
          경우 민사소송법상 관할 법원에 제소합니다.
        </p>

        <h2>12. 문의</h2>
        <p>
          본 약관에 관한 질문·이의·저작권 관련 문의는{" "}
          <a href="mailto:contact@aigrit.dev">contact@aigrit.dev</a>{" "}
          또는{" "}
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
          로 연락해 주세요.
        </p>
      </section>
    </div>
  );
}

function TermsEn() {
  return (
    <div className="mx-auto max-w-3xl px-6 py-12">
      <Header subtitle="Terms of Service · Last updated 2026-06-04" />
      <section className="prose prose-neutral max-w-none dark:prose-invert prose-headings:tracking-tight prose-a:text-[var(--color-brand-primary)]">
        <h2>1. Acceptance of Terms</h2>
        <p>
          These Terms govern your use of the content and website services
          (the &quot;Service&quot;) provided by {brandConfig.name}{" "}
          ({brandConfig.url}). By accessing or using the Service, you agree to
          be bound by these Terms. If you do not agree, please discontinue use.
        </p>

        <h2>2. Description of Service</h2>
        <p>
          {brandConfig.name} publishes reviews, comparisons, and hands-on guides
          related to AI tools, productivity automation, and solo-builder
          workflows. The Service is provided for informational purposes only
          and does not constitute professional advice (legal, tax, investment,
          etc.).
        </p>

        <h2>3. Content Ownership</h2>
        <ol>
          <li>
            All articles, images, infographics, and code examples on{" "}
            {brandConfig.name} are owned by {brandConfig.name} or its rightful
            licensors unless otherwise indicated.
          </li>
          <li>
            <strong>Personal, non-commercial quotation</strong> is permitted if
            you attribute the source ({brandConfig.url}). We recommend keeping
            quoted passages under 200 characters per article.
          </li>
          <li>
            <strong>
              Commercial redistribution, full reproduction, or large-scale
              scraping for AI training
            </strong>{" "}
            is prohibited without prior written consent.
          </li>
          <li>
            Third-party materials (screenshots, logos, citations) remain subject
            to their original licenses. We correct misattribution or rights
            violations upon notification.
          </li>
        </ol>

        <h2>4. User Responsibilities</h2>
        <ol>
          <li>
            Any decision made on the basis of information from the Service —
            including purchases, contracts, investments, and work applications —
            is <strong>solely your responsibility</strong>. {brandConfig.name}{" "}
            assumes no liability for outcomes.
          </li>
          <li>
            You must not interfere with the Service through automated bulk
            requests, circumvention of access controls, or security probing.
          </li>
          <li>
            Content posted via embedded comment systems (such as Giscus) must
            not infringe on the rights of others or violate applicable law.
          </li>
        </ol>

        <h2>5. Accuracy Disclaimer</h2>
        <p>
          All reviews, guides, and figures are based on the state of the
          product, policy, or market <strong>at the time of writing</strong>.
          Subsequent updates, policy changes, or market shifts may not be
          reflected. Always confirm the latest information from official
          sources before making decisions. {brandConfig.name} does not
          guarantee the completeness or timeliness of the content.
        </p>

        <h2>6. Disclaimer of Warranties</h2>
        <p>
          The Service is provided on an &quot;AS IS&quot; basis.{" "}
          {brandConfig.name} disclaims all express or implied warranties,
          including those of uninterrupted operation, error-free performance,
          and fitness for a particular purpose. We are not liable for temporary
          downtime, data loss, or failures of third-party systems
          (analytics, ad networks, comment systems, etc.).
        </p>

        <h2>7. Limitation of Liability</h2>
        <p>
          To the maximum extent permitted by applicable law, {brandConfig.name}{" "}
          shall not be liable for any direct, indirect, incidental, or
          consequential damages (including loss of revenue, data, or
          reputation) arising from your use of the Service. The aggregate
          liability under these Terms shall not exceed the amount you have paid
          directly for the Service (zero if no payment was made).
        </p>

        <h2>8. External Links</h2>
        <p>
          The Service may contain links to external websites.{" "}
          {brandConfig.name} is not responsible for the content, terms, privacy
          practices, products, or services of those external sites. Please
          review their terms and policies before use.
        </p>

        <h2>9. Advertising and Affiliate Marketing</h2>
        <p>
          {brandConfig.name} includes Google AdSense display ads and affiliate
          marketing links. For details on advertising and affiliate
          relationships, see our{" "}
          <a href={`${brandConfig.url}/en/disclaimer`}>Disclaimer</a>; for
          cookie and personal data handling, see our{" "}
          <a href={`${brandConfig.url}/en/privacy`}>Privacy Policy</a>.
          Outcomes of clicking ads or signing up via affiliate links are your
          responsibility.
        </p>

        <h2>10. Changes to These Terms</h2>
        <p>
          {brandConfig.name} may revise these Terms without prior notice to
          reflect legal changes, operational adjustments, or new features.
          Revised Terms take effect upon posting to this page, and the{" "}
          <em>&quot;Last updated&quot;</em> date at the top will be updated.
          Continued use after revision constitutes acceptance of the updated
          Terms.
        </p>

        <h2>11. Governing Law and Jurisdiction</h2>
        <p>
          These Terms are governed by and construed in accordance with the laws
          of the Republic of Korea. Disputes arising from use of the Service
          shall first be addressed through good-faith negotiation, and failing
          that, submitted to the competent courts under the Korean Civil
          Procedure Act.
        </p>

        <h2>12. Contact</h2>
        <p>
          Questions about these Terms, objections, or copyright inquiries:{" "}
          <a href="mailto:contact@aigrit.dev">contact@aigrit.dev</a> or{" "}
          {brandConfig.social.x ? (
            <a
              href={`https://x.com/${brandConfig.social.x.replace(/^@/, "")}`}
              target="_blank"
              rel="noopener noreferrer"
            >
              {brandConfig.social.x}
            </a>
          ) : (
            "the site owner"
          )}
          .
        </p>
      </section>
    </div>
  );
}
