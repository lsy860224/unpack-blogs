import type { ImgHTMLAttributes } from "react";

/**
 * MDX의 ![alt](src)를 대체하는 이미지 컴포넌트.
 * Next.js `<Image>` 대신 plain `<img>` 사용 — width/height을 frontmatter나
 * 빌드 타임 sharp 측정 없이도 동작하도록 함. 대신 lazy loading·async
 * decoding·CLS 방지 style을 자동 주입해 LCP·모바일 데이터를 개선한다.
 *
 * 추가 시 next.config.ts의 images.remotePatterns 등록은 불필요.
 */
export function MdxImage({
  src,
  alt = "",
  loading,
  decoding,
  style,
  ...rest
}: ImgHTMLAttributes<HTMLImageElement>) {
  return (
    <img
      src={src}
      alt={alt}
      loading={loading ?? "lazy"}
      decoding={decoding ?? "async"}
      style={{
        maxWidth: "100%",
        height: "auto",
        display: "block",
        margin: "0 auto",
        ...style,
      }}
      {...rest}
    />
  );
}
