import Link from "next/link";
import path from "node:path";
import type { Metadata } from "next";
import {
  buildMetadata,
  getAllPostSummaries,
  toOgLocale,
} from "@unpack/blog-core";
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
      ? `About ${localized.name} — Korean AI tool guides compared by official sources and real use cases.`
      : `${localized.name}을 소개합니다 — AI 도구를 공식 자료와 실제 쓰임새로 비교하는 한국어 가이드.`;
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
  // 글 수는 하드코딩하지 않고 발행된 글에서 계산 (예약 글 제외) — "6주·20편" 같은 낡은 숫자 방지
  const postCount = getAllPostSummaries(
    path.join(process.cwd(), "content/posts", locale),
    { brand: "aigrit" },
  ).length;
  return locale === "en" ? (
    <AboutEn postCount={postCount} />
  ) : (
    <AboutKo postCount={postCount} />
  );
}

/** 사이트 오픈일 (첫 글 hello-world 발행일) */
const LAUNCHED_KO = "2026년 4월";
const LAUNCHED_EN = "April 2026";

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

function AboutKo({ postCount }: { postCount: number }) {
  return (
    <div className="mx-auto max-w-3xl px-6 py-12">
      <PageHeader subtitle={`${brandConfig.name} · ${brandConfig.url.replace(/^https?:\/\//, "")}`} />
      <section className="prose prose-neutral max-w-none dark:prose-invert prose-headings:tracking-tight prose-a:text-[var(--color-brand-primary)]">
        <h2>운영자</h2>
        <p>
          <strong>babipa</strong> — 1인 빌더로 Flutter 기반 iOS 앱(App Store
          라이브)·Next.js 블로그 모노레포(AIGrit·babipanote)·자동화 시스템을
          직접 만들고 운영합니다. 운영기는 자매 사이트{" "}
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
          MDX 기반으로 직접 설계·운영 중이고, {LAUNCHED_KO} 오픈 이후 글{" "}
          {postCount}편을 발행했습니다.
        </p>
        <p>
          <strong>글의 근거</strong> — 기능·가격·정책은 공식 문서와 1차 출처로
          확인하고 본문에 링크를 남깁니다. 작성자가 직접 써 본 경험은 그렇다고
          밝힌 경우에만 싣고, 통제된 테스트를 거치지 않은 점수·측정 수치나
          검증할 수 없는 수익 인증은 싣지 않습니다. 스폰서 리뷰는 받지 않고,
          제휴 링크가 들어가는 글에는 글 상단 고지와 본문 라벨을 함께
          표기합니다. 도구는 자주 바뀌므로 Pillar 글은 분기마다 갱신합니다.
        </p>

        <h2>우리가 하는 일</h2>
        <p>
          {brandConfig.name}은 AI 도구를 공식 문서·가격·정책과 실제 쓰임새
          기준으로 <strong>비교</strong>하는 한국어 가이드입니다. 마케팅 카피를
          옮기지 않고, 어떤 상황에 어떤 도구가 맞는지 판단 기준을 남깁니다.
        </p>

        <h2>글쓰기 원칙</h2>
        <ol>
          <li>
            <strong>근거 (Sources)</strong> — 기능·가격·정책은 공식 문서와 1차
            출처로 확인하고 링크합니다. 확인 날짜가 중요한 정보는 기준
            시점을 함께 적습니다.
          </li>
          <li>
            <strong>정직 (Honesty)</strong> — 직접 측정하지 않은 속도·정확도
            점수, 검증할 수 없는 수익 수치는 싣지 않습니다. 경험을 쓸 때는
            경험이라고 밝힙니다.
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

        <h2>쓰지 않는 것</h2>
        <ul>
          <li>출처 없이 만든 벤치마크 점수·측정 수치</li>
          <li>검증할 수 없는 수익 인증</li>
          <li>스폰서 제안을 받고 쓰는 리뷰 — 우리는 스폰서 리뷰를 받지 않습니다.</li>
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

function AboutEn({ postCount }: { postCount: number }) {
  return (
    <div className="mx-auto max-w-3xl px-6 py-12">
      <PageHeader subtitle={`${brandConfig.name} · ${brandConfig.url.replace(/^https?:\/\//, "")}`} />
      <section className="prose prose-neutral max-w-none dark:prose-invert prose-headings:tracking-tight prose-a:text-[var(--color-brand-primary)]">
        <h2>Who runs this site</h2>
        <p>
          <strong>babipa</strong> — a solo builder running a Flutter-based iOS
          app (live on App Store), a Next.js blog monorepo (AIGrit and
          babipanote), and supporting automation systems. The first-person
          operations log lives at the sister site{" "}
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
          by the same single person.{" "}
          {`Since launching in ${LAUNCHED_EN}, it has published ${postCount} posts in this language.`}
        </p>
        <p>
          <strong>How posts are sourced</strong> — Features, pricing, and
          policies are checked against official documentation and primary
          sources, and linked in the text. The author&apos;s own experience is
          included only when it is labeled as such. We don&apos;t publish
          scores or measurements that didn&apos;t come from a controlled test,
          or income claims we can&apos;t verify. We don&apos;t accept sponsored
          reviews; affiliate links carry a disclosure at the top of the article
          and an inline label. Pillar posts are revised quarterly.
        </p>

        <h2>What we do</h2>
        <p>
          {brandConfig.name} publishes Korean-language AI tool guides that{" "}
          <strong>compare tools</strong> by official documentation, pricing,
          policy, and real use cases. We don&apos;t rewrite marketing copy — we
          leave decision criteria for which tool fits which situation.
        </p>

        <h2>Editorial principles</h2>
        <ol>
          <li>
            <strong>Sources</strong> — features, pricing, and policies are
            verified against official documentation and linked. Time-sensitive
            facts carry the date they were checked.
          </li>
          <li>
            <strong>Honesty</strong> — no speed or accuracy scores we
            didn&apos;t measure, no income figures we can&apos;t verify.
            Personal experience is labeled as experience.
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

        <h2>What we don&apos;t publish</h2>
        <ul>
          <li>Benchmark scores or measurements without a source.</li>
          <li>Income claims we can&apos;t verify.</li>
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
