import Link from "next/link";
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
      ? `About ${localized.name} — hands-on AI tool reviews, compared with numbers.`
      : `${localized.name}을 소개합니다 — AI 도구를 직접 써보고 숫자로 비교하는 한국어 리뷰.`;
  return buildMetadata({
    title: "About",
    description,
    siteName: localized.name,
    siteUrl: localized.url,
    path: `/${locale}/about`,
    locale: toOgLocale(locale),
    hrefLangs: {
      ko: "/ko/about",
      en: "/en/about",
      "x-default": "/ko/about",
    },
  });
}

export default async function AboutPage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  return locale === "en" ? <AboutEn /> : <AboutKo />;
}

function PageHeader({ subtitle }: { subtitle: string }) {
  return (
    <header className="mb-10 border-b border-[color-mix(in_oklab,var(--foreground)_8%,transparent)] pb-6">
      <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-[var(--color-brand-primary)]">
        About
      </h1>
      <p className="mt-2 text-sm font-mono text-[color-mix(in_oklab,var(--foreground)_65%,transparent)]">
        {subtitle}
      </p>
    </header>
  );
}

function AboutKo() {
  return (
    <div className="mx-auto max-w-3xl px-6 py-12">
      <PageHeader subtitle={`${brandConfig.name} · ${brandConfig.url.replace(/^https?:\/\//, "")}`} />
      <section className="prose prose-neutral max-w-none dark:prose-invert prose-headings:tracking-tight prose-a:text-[var(--color-brand-primary)]">
        <h2>운영자</h2>
        <p>
          <strong>babipa</strong> — 1인 빌더로 Flutter 기반 iOS 앱(App Store
          라이브)·Next.js 블로그 모노레포(AIGrit·babipanote)·자동화 시스템을
          직접 만들고 운영합니다. AI 도구는 마케팅 카피가 아니라 본인의 실제
          워크플로우에 며칠씩 넣어보고, 결과만 글로 옮깁니다. 운영기는 자매
          사이트{" "}
          <a
            href="https://babipanote.com"
            target="_blank"
            rel="noopener noreferrer"
          >
            babipanote
          </a>
          에 1인칭으로 기록합니다.
        </p>
        <p>
          <strong>경력 요약</strong> — 비개발자 출신으로 2026년 1분기부터
          Claude Code·Cursor·MCP 4종 도구 스택을 1인 빌더 워크플로우에 도입해
          Flutter iOS 앱 3종(GentleDo·GentleFast·GentleStudy)을 App Store에
          출시했습니다. 블로그 모노레포는 Next.js 16 App Router + Turborepo +
          MDX 기반으로 직접 설계·운영 중이고, 6주 운영하며 글 20편을 누적
          발행했습니다. AI 도구를 평가할 때 항상 "이 도구를 내 실제
          프로젝트에 며칠 넣었을 때 무엇이 빨라지거나 막혔는가"를 1차 데이터로
          확보한 뒤 글로 옮깁니다.
        </p>
        <p>
          <strong>리뷰 신뢰도 근거</strong> — 본 사이트의 모든 글은 작성자가
          직접 사용한 결과를 기반으로 합니다. 스폰서 리뷰는 받지 않고, 제휴
          링크가 들어가는 글에는 본문 안 명시적 라벨과 글 상단 1줄 고지를
          동시에 표기합니다. 데이터·수치는 측정 환경과 표본 크기를 함께
          공개하며, 분기마다 도구 변화에 맞춰 Pillar 글을 갱신합니다.
        </p>

        <h2>우리가 하는 일</h2>
        <p>
          {brandConfig.name}은 AI 도구를 직접 며칠간 써본 뒤, 속도·비용·정확도를
          <strong> 숫자로 비교</strong>하는 한국어 리뷰 블로그입니다. 마케팅 카피를
          다시 옮기지 않고, 실사용 결과만 남깁니다.
        </p>

        <h2>리뷰 원칙</h2>
        <ol>
          <li>
            <strong>검증 (Validation)</strong> — 광고 카피가 아닌 실사용 결과. 각
            리뷰는 최소 3일 이상 사용 후 작성합니다.
          </li>
          <li>
            <strong>수치 (Numbers)</strong> — 속도·비용·정확도를 숫자로 표기.
            테스트 방법과 표본 크기(n=??)를 본문에 명시합니다.
          </li>
          <li>
            <strong>비교 (Comparison)</strong> — 단독 리뷰보다 1:1 또는 N:N 비교를
            우선. 대체재가 있을 때는 반드시 함께 다룹니다.
          </li>
          <li>
            <strong>맥락 (Context)</strong> — &quot;직장인이 쓴다면&quot; /
            &quot;개발자가 쓴다면&quot; 시나리오를 명시. 독자가 자기 상황에
            대입할 수 있게 합니다.
          </li>
        </ol>

        <h2>리뷰하지 않는 것</h2>
        <ul>
          <li>5분 만에 만져본 도구 — 최소 3일 사용 원칙 위반</li>
          <li>공식 데모 영상만 본 상태 — 실사용 대체 불가</li>
          <li>
            공개 스포너 제안을 거절하지 못한 리뷰 — 우리는 스폰서 리뷰를 받지
            않습니다.
          </li>
        </ul>

        <h2>수익 구조</h2>
        <p>
          {brandConfig.name}은 <strong>Google AdSense 광고</strong>와{" "}
          <strong>제휴 마케팅(affiliate) 링크</strong>로 운영됩니다. 리뷰 판단은
          이 두 가지 수익원과 독립적이며, 관련 세부 사항은{" "}
          <Link href="/ko/disclaimer">Disclaimer</Link>에서 확인하세요.
        </p>

        <h2>문의</h2>
        <p>
          이메일:{" "}
          <a href="mailto:contact@aigrit.dev">contact@aigrit.dev</a>
          <br />
          {brandConfig.social.x && (
            <>
              X:{" "}
              <a
                href={`https://x.com/${brandConfig.social.x.replace(/^@/, "")}`}
                target="_blank"
                rel="noopener noreferrer"
              >
                {brandConfig.social.x}
              </a>
              <br />
            </>
          )}
          {brandConfig.social.github && (
            <>
              GitHub:{" "}
              <a
                href={`https://github.com/${brandConfig.social.github}`}
                target="_blank"
                rel="noopener noreferrer"
              >
                {brandConfig.social.github}
              </a>
              <br />
            </>
          )}
          개인정보 처리 방침은{" "}
          <Link href="/ko/privacy">Privacy</Link>, 제휴 마케팅·광고 고지는{" "}
          <Link href="/ko/disclaimer">Disclaimer</Link>에서 확인하세요.
        </p>
      </section>
    </div>
  );
}

function AboutEn() {
  return (
    <div className="mx-auto max-w-3xl px-6 py-12">
      <PageHeader subtitle={`${brandConfig.name} · ${brandConfig.url.replace(/^https?:\/\//, "")}`} />
      <section className="prose prose-neutral max-w-none dark:prose-invert prose-headings:tracking-tight prose-a:text-[var(--color-brand-primary)]">
        <h2>Who runs this site</h2>
        <p>
          <strong>babipa</strong> — a solo builder running a Flutter-based iOS
          app (live on App Store), a Next.js blog monorepo (AIGrit and
          babipanote), and supporting automation systems. Every AI tool covered
          here is used for several days in real workflows before publication;
          marketing copy is excluded. The first-person operations log lives at
          the sister site{" "}
          <a
            href="https://babipanote.com"
            target="_blank"
            rel="noopener noreferrer"
          >
            babipanote
          </a>
          .
        </p>
        <p>
          <strong>Background</strong> — Coming from a non-engineering
          background, the operator adopted a four-tool AI coding stack (Claude
          Code, Cursor, Claude Desktop with MCP, and Obsidian MCP) in early
          2026 and shipped three Flutter iOS apps (GentleDo, GentleFast,
          GentleStudy) to the App Store. The blog monorepo is built on Next.js
          16 App Router, Turborepo, and MDX, designed and operated end-to-end
          by the same single person, and has accumulated 20+ published posts
          over six weeks of active use. Every tool review starts with the
          question "what got faster or broke when I pushed this tool into a
          real project for several days," then becomes a writeup only after
          the first-party data exists.
        </p>
        <p>
          <strong>Review credibility</strong> — Every post on this site is
          based on hands-on use by the author. We do not accept sponsored
          reviews. Affiliate links carry both an inline label inside the
          paragraph and a one-line disclosure at the top of the article. Data
          and numbers are published with the measurement setup and sample
          size, and Pillar posts are revised quarterly to reflect tool
          changes.
        </p>

        <h2>What we do</h2>
        <p>
          {brandConfig.name} is a hands-on AI tool review blog. We use each tool
          for several days, then <strong>compare speed, cost, and accuracy
          with numbers</strong>. We don&apos;t rewrite marketing copy — we report
          what actually happened when we used the tool.
        </p>

        <h2>Review principles</h2>
        <ol>
          <li>
            <strong>Validation</strong> — hands-on results over marketing copy.
            Every review is based on at least 3 days of real usage.
          </li>
          <li>
            <strong>Numbers</strong> — speed, cost, and accuracy expressed as
            numbers. We disclose the test setup and sample size (n=??).
          </li>
          <li>
            <strong>Comparison</strong> — 1:1 or N:N comparisons over solo
            reviews. When alternatives exist, we include them.
          </li>
          <li>
            <strong>Context</strong> — we specify scenarios like &quot;as an
            office worker&quot; or &quot;as a developer&quot; so readers can map
            results to their own situation.
          </li>
        </ol>

        <h2>What we don&apos;t review</h2>
        <ul>
          <li>Tools we only tried for 5 minutes — violates the 3-day rule.</li>
          <li>Tools we only saw in an official demo video — no substitute for hands-on.</li>
          <li>Anything written under sponsorship — we don&apos;t accept sponsored reviews.</li>
        </ul>

        <h2>How we&apos;re funded</h2>
        <p>
          {brandConfig.name} is supported by <strong>Google AdSense display
          ads</strong> and <strong>affiliate links</strong>. Review judgments are
          independent of these revenue streams. See the{" "}
          <Link href="/en/disclaimer">Disclaimer</Link> for the full policy.
        </p>

        <h2>Contact</h2>
        <p>
          Email: <a href="mailto:contact@aigrit.dev">contact@aigrit.dev</a>
          <br />
          {brandConfig.social.x && (
            <>
              X:{" "}
              <a
                href={`https://x.com/${brandConfig.social.x.replace(/^@/, "")}`}
                target="_blank"
                rel="noopener noreferrer"
              >
                {brandConfig.social.x}
              </a>
              <br />
            </>
          )}
          {brandConfig.social.github && (
            <>
              GitHub:{" "}
              <a
                href={`https://github.com/${brandConfig.social.github}`}
                target="_blank"
                rel="noopener noreferrer"
              >
                {brandConfig.social.github}
              </a>
              <br />
            </>
          )}
          See <Link href="/en/privacy">Privacy</Link> for data handling and{" "}
          <Link href="/en/disclaimer">Disclaimer</Link> for ad & affiliate
          policy.
        </p>
      </section>
    </div>
  );
}
