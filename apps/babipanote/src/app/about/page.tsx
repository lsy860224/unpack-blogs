import type { Metadata } from "next";
import { buildMetadata } from "@unpack/blog-core";
import { brandConfig } from "../../../brand.config";

export const metadata: Metadata = buildMetadata({
  title: "About",
  description: `${brandConfig.name} 운영자 소개. ${brandConfig.tagline}`,
  siteName: brandConfig.name,
  siteUrl: brandConfig.url,
  path: "/about",
});

export default function AboutPage() {
  return (
    <article className="mx-auto max-w-2xl px-6 py-12 prose prose-neutral dark:prose-invert">
      <h1 style={{ fontFamily: "var(--font-serif)" }}>About</h1>
      <p>
        바비파입니다. 평일에는 회사에서 일하고, 남는 시간으로 {" "}
        <a href="https://aigrit.dev" target="_blank" rel="noopener noreferrer">
          AIGrit
        </a>{" "}
        블로그를 쓰고 GentleLab 앱 시리즈를 만듭니다.
      </p>
      <p>
        이 저널은 결과보다 <strong>과정</strong>을 기록하기 위해 만들었습니다. 잘 된 것만
        쓰는 블로그는 이미 많으니, 여기서는 실패·매출·감정까지 가능한 한 날것으로
        남깁니다. 1인 빌더에게 필요한 건 멋진 최종 결과 사진보다, 한 사람이 어떻게
        꾸준히 버티는지에 대한 기록이라고 믿습니다.
      </p>
      <h2 style={{ fontFamily: "var(--font-serif)" }}>무엇을 다루나요</h2>
      <ul>
        <li>주/월 단위 회고 — 지난 기간의 숫자와 배움</li>
        <li>앱 개발기 — GentleLab 시리즈의 설계·출시·운영 과정</li>
        <li>블로그 운영기 — AIGrit의 수익·트래픽·의사결정</li>
        <li>실패 기록 — 중단한 실험, 철회한 의사결정</li>
      </ul>
      <h2 style={{ fontFamily: "var(--font-serif)" }}>연락</h2>
      <p>
        X{" "}
        <a
          href={`https://x.com/${brandConfig.social.x?.replace(/^@/, "")}`}
          target="_blank"
          rel="noopener noreferrer"
        >
          {brandConfig.social.x}
        </a>{" "}
        또는 글 하단 댓글(Giscus)로 남겨주세요.
      </p>
    </article>
  );
}
