"use client";

import { useEffect, useRef } from "react";
import { cn } from "../../lib/cn";

export interface CommentsProps {
  repo?: string;
  repoId?: string;
  category?: string;
  categoryId?: string;
  /** Giscus mapping (default: pathname) */
  mapping?: "pathname" | "url" | "title" | "og:title";
  theme?: string;
  lang?: string;
  reactionsEnabled?: boolean;
  className?: string;
  /**
   * 브랜드 식별자 — 두 앱이 같은 repo를 공유하면 댓글이 섞일 수 있어 경고.
   * mapping="url"이면 경로별 격리되므로 경고 생략.
   */
  brand?: string;
}

const WARNED_REPOS = new Set<string>();

/**
 * Giscus 댓글 위젯. repo/repoId/category/categoryId 가 모두 설정된 경우에만 렌더.
 * next/script를 쓰지 않는 이유: Giscus는 `<script>`의 parent node에 iframe을
 * 삽입하므로, container div에 append 해야 한다. React 친화적으로 DOM을 직접
 * 조작하되 innerHTML 대신 명시적 child cleanup 사용.
 */
export function Comments({
  repo,
  repoId,
  category,
  categoryId,
  mapping = "pathname",
  theme = "preferred_color_scheme",
  lang = "ko",
  reactionsEnabled = true,
  className,
  brand,
}: CommentsProps) {
  const ref = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    if (!ref.current) return;
    if (!repo || !repoId || !category || !categoryId) return;

    if (
      brand &&
      mapping === "pathname" &&
      process.env.NODE_ENV !== "production" &&
      !WARNED_REPOS.has(`${brand}:${repo}`)
    ) {
      WARNED_REPOS.add(`${brand}:${repo}`);
      // eslint-disable-next-line no-console
      console.warn(
        `[Comments] brand="${brand}" uses repo="${repo}" with mapping="pathname". ` +
          "If another brand shares the same repo, same-pathname posts will collide. " +
          'Use a dedicated repo per brand, or set mapping="url".',
      );
    }

    const node = ref.current;
    clearChildren(node);

    const script = document.createElement("script");
    script.src = "https://giscus.app/client.js";
    script.async = true;
    script.crossOrigin = "anonymous";
    script.setAttribute("data-repo", repo);
    script.setAttribute("data-repo-id", repoId);
    script.setAttribute("data-category", category);
    script.setAttribute("data-category-id", categoryId);
    script.setAttribute("data-mapping", mapping);
    script.setAttribute("data-strict", "0");
    script.setAttribute("data-reactions-enabled", reactionsEnabled ? "1" : "0");
    script.setAttribute("data-emit-metadata", "0");
    script.setAttribute("data-input-position", "bottom");
    script.setAttribute("data-theme", theme);
    script.setAttribute("data-lang", lang);
    script.setAttribute("data-loading", "lazy");

    node.appendChild(script);

    return () => {
      clearChildren(node);
    };
  }, [
    repo,
    repoId,
    category,
    categoryId,
    mapping,
    theme,
    lang,
    reactionsEnabled,
    brand,
  ]);

  if (!repo || !repoId || !category || !categoryId) return null;

  return <div ref={ref} className={cn("mt-16 not-prose", className)} />;
}

function clearChildren(node: HTMLElement) {
  while (node.firstChild) node.removeChild(node.firstChild);
}
