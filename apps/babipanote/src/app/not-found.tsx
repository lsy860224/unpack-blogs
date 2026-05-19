import Link from "next/link";
import type { Metadata } from "next";
import { buildMetadata } from "@unpack/blog-core";
import { brandConfig } from "../../brand.config";

export const metadata: Metadata = buildMetadata({
  title: "404 Not Found",
  description: `${brandConfig.name}에서 찾을 수 없는 페이지입니다.`,
  siteName: brandConfig.name,
  siteUrl: brandConfig.url,
  path: "/404",
});

export default function NotFound() {
  return (
    <div className="mx-auto max-w-3xl px-6 py-24 text-center">
      <p className="text-7xl font-extrabold tracking-tight text-[var(--color-brand-primary)]">
        404
      </p>
      <h1 className="mt-6 text-2xl sm:text-3xl font-bold tracking-tight">
        찾을 수 없는 페이지
      </h1>
      <p className="mt-4 text-[color-mix(in_oklab,var(--foreground)_75%,transparent)]">
        요청하신 페이지가 존재하지 않거나 삭제되었습니다. 아래 링크로 이동해 주세요.
      </p>
      <nav className="mt-10 flex flex-wrap justify-center gap-x-6 gap-y-3 text-sm">
        <Link
          href="/"
          className="text-[var(--color-brand-primary)] underline-offset-4 hover:underline"
        >
          홈으로
        </Link>
        <Link
          href="/blog"
          className="text-[var(--color-brand-primary)] underline-offset-4 hover:underline"
        >
          전체 글 보기
        </Link>
        <Link
          href="/projects"
          className="text-[var(--color-brand-primary)] underline-offset-4 hover:underline"
        >
          프로젝트
        </Link>
        <Link
          href="/about"
          className="text-[var(--color-brand-primary)] underline-offset-4 hover:underline"
        >
          운영자 소개
        </Link>
      </nav>
      <p className="mt-12 text-xs text-[color-mix(in_oklab,var(--foreground)_45%,transparent)]">
        {brandConfig.name} — {brandConfig.tagline}
      </p>
    </div>
  );
}
