"use client";

import { useEffect, useRef } from "react";

export interface CommentsProps {
  repo?: string;
  repoId?: string;
  category?: string;
  categoryId?: string;
  /** Giscus mapping (default: pathname) */
  mapping?: "pathname" | "url" | "title" | "og:title";
  /** Light/dark 테마. "preferred_color_scheme" 권장 */
  theme?: string;
  lang?: string;
  reactionsEnabled?: boolean;
  className?: string;
}

/**
 * Giscus 댓글 위젯. repo/repoId/category/categoryId 가 모두 설정된 경우에만 렌더.
 * 자세한 설정은 https://giscus.app 에서 생성한 값을 brandConfig.comments에 주입.
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
}: CommentsProps) {
  const ref = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    if (!ref.current) return;
    if (!repo || !repoId || !category || !categoryId) return;

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

    const node = ref.current;
    node.innerHTML = "";
    node.appendChild(script);
    return () => {
      node.innerHTML = "";
    };
  }, [repo, repoId, category, categoryId, mapping, theme, lang, reactionsEnabled]);

  if (!repo || !repoId || !category || !categoryId) return null;

  return <div ref={ref} className={["mt-16 not-prose", className ?? ""].join(" ")} />;
}
