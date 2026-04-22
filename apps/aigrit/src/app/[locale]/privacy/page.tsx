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
      ? `${localized.name} Privacy Policy`
      : `${localized.name} 개인정보 처리방침`;
  return buildMetadata({
    title: "Privacy Policy",
    description,
    siteName: localized.name,
    siteUrl: localized.url,
    path: `/${locale}/privacy`,
    locale: toOgLocale(locale),
    hrefLangs: {
      ko: "/ko/privacy",
      en: "/en/privacy",
      "x-default": "/ko/privacy",
    },
  });
}

export default async function PrivacyPage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  return locale === "en" ? <PrivacyEn /> : <PrivacyKo />;
}

function Header({ subtitle }: { subtitle: string }) {
  return (
    <header className="mb-10 border-b border-[color-mix(in_oklab,var(--foreground)_8%,transparent)] pb-6">
      <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-[var(--color-brand-primary)]">
        Privacy Policy
      </h1>
      <p className="mt-2 text-sm font-mono text-[color-mix(in_oklab,var(--foreground)_65%,transparent)]">
        {subtitle}
      </p>
    </header>
  );
}

function PrivacyKo() {
  return (
    <div className="mx-auto max-w-3xl px-6 py-12">
      <Header subtitle="개인정보 처리방침 · 최종 업데이트 2026-04-15" />
      <section className="prose prose-neutral max-w-none dark:prose-invert prose-headings:tracking-tight prose-a:text-[var(--color-brand-primary)]">
        <p>
          {brandConfig.name}({brandConfig.url})은 방문자의 개인정보를 소중히
          다룹니다. 본 사이트는 아래와 같이 개인정보를 수집·이용합니다.
        </p>

        <h2>1. 수집하는 정보</h2>
        <ul>
          <li>
            <strong>접속 로그</strong> — IP 주소(익명화), User-Agent, 참조
            페이지, 방문 시각. 웹 서버·CDN이 자동으로 기록합니다.
          </li>
          <li>
            <strong>분석 쿠키</strong> — Google Analytics(GA4)가 방문 패턴을
            집계하기 위해 쿠키를 설정합니다. IP 익명화 옵션이 적용됩니다.
          </li>
          <li>
            <strong>광고 쿠키</strong> — Google AdSense가 관련 광고 송출을 위해
            쿠키를 사용합니다. 광고 맞춤 설정은{" "}
            <a
              href="https://adssettings.google.com"
              target="_blank"
              rel="noopener noreferrer"
            >
              Google 광고 설정
            </a>
            에서 관리할 수 있습니다.
          </li>
          <li>
            <strong>댓글 로그인</strong> — Giscus 댓글은 GitHub 계정 인증을
            사용합니다. 로그인 정보는 GitHub에서만 처리되며 본 사이트는 저장하지
            않습니다.
          </li>
        </ul>

        <h2>2. 이용 목적</h2>
        <ul>
          <li>사이트 운영·보안 (접속 기록, 오류 추적)</li>
          <li>콘텐츠 개선을 위한 통계 분석 (GA4)</li>
          <li>광고 송출 및 부정 클릭 방지 (AdSense)</li>
        </ul>

        <h2>3. 보관 기간</h2>
        <p>
          접속 로그는 최대 6개월 보관 후 파기됩니다. GA4·AdSense는 각 서비스의
          정책에 따릅니다.
        </p>

        <h2>4. 제3자 제공</h2>
        <p>수집된 정보는 다음 외 제3자에게 제공되지 않습니다.</p>
        <ul>
          <li>Google LLC (Analytics, AdSense)</li>
          <li>Vercel Inc. (호스팅)</li>
          <li>GitHub, Inc. (Giscus 댓글)</li>
        </ul>

        <h2>5. 쿠키 거부</h2>
        <p>
          브라우저 설정에서 쿠키를 차단할 수 있습니다. 차단 시 일부 기능(댓글,
          테마 저장 등)이 제한될 수 있습니다.
        </p>

        <h2>6. 권리 행사</h2>
        <p>
          개인정보 열람·정정·삭제를 원하실 경우{" "}
          {brandConfig.social.x && (
            <>
              X(
              <a
                href={`https://x.com/${brandConfig.social.x.replace(/^@/, "")}`}
                target="_blank"
                rel="noopener noreferrer"
              >
                {brandConfig.social.x}
              </a>
              )
            </>
          )}{" "}
          으로 문의해주세요.
        </p>

        <h2>7. 방침 변경</h2>
        <p>
          본 방침은 사이트 운영 방식이 바뀔 때 예고 후 업데이트됩니다. 변경 이력은
          본 페이지 상단의 &quot;최종 업데이트&quot; 날짜로 확인할 수 있습니다.
        </p>
      </section>
    </div>
  );
}

function PrivacyEn() {
  return (
    <div className="mx-auto max-w-3xl px-6 py-12">
      <Header subtitle="Privacy Policy · Last updated 2026-04-15" />
      <section className="prose prose-neutral max-w-none dark:prose-invert prose-headings:tracking-tight prose-a:text-[var(--color-brand-primary)]">
        <p>
          {brandConfig.name} ({brandConfig.url}) respects visitor privacy. This
          policy explains what we collect and how we use it.
        </p>

        <h2>1. What we collect</h2>
        <ul>
          <li>
            <strong>Access logs</strong> — IP address (anonymized), User-Agent,
            referrer, and timestamp, recorded automatically by our web server
            and CDN.
          </li>
          <li>
            <strong>Analytics cookies</strong> — Google Analytics (GA4) sets
            cookies to aggregate visit patterns. IP anonymization is enabled.
          </li>
          <li>
            <strong>Ad cookies</strong> — Google AdSense uses cookies to serve
            relevant ads. You can manage ad personalization at{" "}
            <a
              href="https://adssettings.google.com"
              target="_blank"
              rel="noopener noreferrer"
            >
              Google Ad Settings
            </a>
            .
          </li>
          <li>
            <strong>Comment sign-in</strong> — Giscus comments use GitHub
            account authentication. Sign-in data is processed by GitHub only and
            not stored on this site.
          </li>
        </ul>

        <h2>2. Purpose</h2>
        <ul>
          <li>Site operation and security (access records, error tracking).</li>
          <li>Content improvement via aggregate analytics (GA4).</li>
          <li>Ad delivery and invalid-click prevention (AdSense).</li>
        </ul>

        <h2>3. Retention</h2>
        <p>
          Access logs are retained for up to 6 months and then deleted. GA4 and
          AdSense follow the retention policies of their respective services.
        </p>

        <h2>4. Third parties</h2>
        <p>We do not share collected data with third parties except:</p>
        <ul>
          <li>Google LLC (Analytics, AdSense)</li>
          <li>Vercel Inc. (hosting)</li>
          <li>GitHub, Inc. (Giscus comments)</li>
        </ul>

        <h2>5. Opting out of cookies</h2>
        <p>
          You can block cookies in your browser settings. Some features (comments,
          theme preference) may be limited when cookies are disabled.
        </p>

        <h2>6. Your rights</h2>
        <p>
          To access, correct, or delete your personal data, please contact us via{" "}
          {brandConfig.social.x && (
            <>
              X (
              <a
                href={`https://x.com/${brandConfig.social.x.replace(/^@/, "")}`}
                target="_blank"
                rel="noopener noreferrer"
              >
                {brandConfig.social.x}
              </a>
              )
            </>
          )}
          .
        </p>

        <h2>7. Changes</h2>
        <p>
          This policy is updated when the site&apos;s operations change, with
          prior notice. The &quot;Last updated&quot; date at the top of this page
          reflects the most recent revision.
        </p>
      </section>
    </div>
  );
}
