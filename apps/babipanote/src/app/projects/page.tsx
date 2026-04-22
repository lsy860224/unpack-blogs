import type { Metadata } from "next";
import Link from "next/link";
import { buildMetadata } from "@unpack/blog-core";
import { brandConfig } from "../../../brand.config";

export const metadata: Metadata = buildMetadata({
  title: "Projects",
  description: "바비파가 운영·개발 중인 프로젝트 모음 — AIGrit 블로그와 GentleLab 앱 시리즈.",
  siteName: brandConfig.name,
  siteUrl: brandConfig.url,
  path: "/projects",
});

type Status = "운영중" | "개발중" | "계획중";

interface Project {
  name: string;
  href: string;
  description: string;
  status: Status;
  tags: string[];
}

const BLOGS: Project[] = [
  {
    name: "AIGrit",
    href: "https://aigrit.dev",
    description:
      "AI 도구를 직접 써보고 속도·비용·정확도를 숫자로 비교하는 한국어 리뷰 블로그.",
    status: "운영중",
    tags: ["블로그", "AI 리뷰", "수익형"],
  },
];

const APPS: Project[] = [
  {
    name: "GentleDo",
    href: "#",
    description: "가족과 함께 쓰는 부드러운 할 일 앱. 알림보다 제안.",
    status: "개발중",
    tags: ["iOS", "가족", "할 일"],
  },
  {
    name: "GentleFast",
    href: "#",
    description: "단식/간헐적 식사 리듬을 가볍게 기록하는 앱.",
    status: "계획중",
    tags: ["iOS", "건강"],
  },
  {
    name: "GentleStudy",
    href: "#",
    description: "부모-아이 공동 학습 플래너. 숙제 알림이 아닌 격려 중심.",
    status: "계획중",
    tags: ["iOS", "교육"],
  },
];

const STATUS_COLOR: Record<Status, string> = {
  운영중: "bg-[color-mix(in_oklab,var(--color-accent-green)_20%,transparent)] text-[var(--color-accent-green)]",
  개발중: "bg-[color-mix(in_oklab,var(--color-brand-secondary)_25%,transparent)] text-[color-mix(in_oklab,var(--color-brand-secondary)_80%,var(--foreground))]",
  계획중: "bg-[color-mix(in_oklab,var(--foreground)_8%,transparent)] text-[color-mix(in_oklab,var(--foreground)_65%,transparent)]",
};

export default function ProjectsPage() {
  return (
    <div className="mx-auto max-w-3xl px-6 py-12">
      <h1
        className="text-3xl font-bold tracking-tight"
        style={{ fontFamily: "var(--font-serif)" }}
      >
        Projects
      </h1>
      <p className="mt-2 text-sm text-[color-mix(in_oklab,var(--foreground)_65%,transparent)] max-w-xl leading-relaxed">
        글을 쓰는 곳과 앱을 만드는 곳을 한 페이지로. 상태는 솔직하게 표기.
      </p>

      <section className="mt-12">
        <h2
          className="text-sm font-semibold uppercase tracking-widest text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]"
          style={{ fontFamily: "var(--font-mono)" }}
        >
          Blogs
        </h2>
        <ul className="mt-4 space-y-3">
          {BLOGS.map((p) => (
            <ProjectCard key={p.name} project={p} />
          ))}
        </ul>
      </section>

      <section className="mt-12">
        <h2
          className="text-sm font-semibold uppercase tracking-widest text-[color-mix(in_oklab,var(--foreground)_55%,transparent)]"
          style={{ fontFamily: "var(--font-mono)" }}
        >
          GentleLab — 가족용 앱 시리즈
        </h2>
        <ul className="mt-4 space-y-3">
          {APPS.map((p) => (
            <ProjectCard key={p.name} project={p} />
          ))}
        </ul>
      </section>
    </div>
  );
}

function ProjectCard({ project }: { project: Project }) {
  const isExternal = /^https?:\/\//.test(project.href);
  const content = (
    <div className="flex items-start justify-between gap-4">
      <div className="flex-1">
        <div className="flex items-center gap-2">
          <h3 className="text-lg font-semibold">{project.name}</h3>
          <span
            className={`text-[10px] px-2 py-0.5 rounded uppercase tracking-wider ${STATUS_COLOR[project.status]}`}
            style={{ fontFamily: "var(--font-mono)" }}
          >
            {project.status}
          </span>
        </div>
        <p className="mt-1 text-sm leading-relaxed text-[color-mix(in_oklab,var(--foreground)_75%,transparent)]">
          {project.description}
        </p>
        <div className="mt-2 flex flex-wrap gap-1.5">
          {project.tags.map((tag) => (
            <span
              key={tag}
              className="text-xs px-2 py-0.5 rounded bg-[color-mix(in_oklab,var(--foreground)_6%,transparent)] text-[color-mix(in_oklab,var(--foreground)_65%,transparent)]"
            >
              {tag}
            </span>
          ))}
        </div>
      </div>
    </div>
  );

  return (
    <li>
      {isExternal ? (
        <a
          href={project.href}
          target="_blank"
          rel="noopener noreferrer"
          className="block p-4 rounded-lg border border-[color-mix(in_oklab,var(--foreground)_10%,transparent)] hover:border-[var(--color-brand-primary)] transition"
        >
          {content}
        </a>
      ) : (
        <Link
          href={project.href}
          className="block p-4 rounded-lg border border-[color-mix(in_oklab,var(--foreground)_10%,transparent)] hover:border-[var(--color-brand-primary)] transition"
        >
          {content}
        </Link>
      )}
    </li>
  );
}
