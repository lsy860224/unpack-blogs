import type { NextConfig } from "next";

type ImagesConfig = NonNullable<NextConfig["images"]>;
type RemotePattern = NonNullable<ImagesConfig["remotePatterns"]>[number];

export interface NextConfigFactoryOptions {
  /** 앱별 override — 기본값을 확장하고 싶을 때 */
  overrides?: Partial<NextConfig>;
  /** remotePatterns 추가 (기본 목록에 append) */
  extraRemotePatterns?: RemotePattern[];
}

const DEFAULT_REMOTE_PATTERNS: RemotePattern[] = [
  { protocol: "https", hostname: "avatars.githubusercontent.com" },
  { protocol: "https", hostname: "cdn.jsdelivr.net" },
];

/**
 * 두 앱이 공유하는 Next.js 기본 설정 팩토리.
 * 개별 앱 전용 옵션은 `overrides`로 확장.
 */
export function createNextConfig(
  opts: NextConfigFactoryOptions = {},
): NextConfig {
  const { overrides, extraRemotePatterns } = opts;
  const base: NextConfig = {
    transpilePackages: ["@unpack/blog-core"],
    images: {
      remotePatterns: [...DEFAULT_REMOTE_PATTERNS, ...(extraRemotePatterns ?? [])],
    },
  };
  return { ...base, ...overrides };
}
