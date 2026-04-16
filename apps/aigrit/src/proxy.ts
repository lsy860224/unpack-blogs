import { NextResponse, type NextRequest } from "next/server";

const LOCALES = ["ko", "en"] as const;
const DEFAULT_LOCALE = "ko";

export function proxy(request: NextRequest) {
  const { pathname } = request.nextUrl;
  const hasLocale = LOCALES.some(
    (l) => pathname === `/${l}` || pathname.startsWith(`/${l}/`),
  );
  if (hasLocale) return NextResponse.next();

  const url = request.nextUrl.clone();
  url.pathname = `/${DEFAULT_LOCALE}${pathname === "/" ? "" : pathname}`;
  return NextResponse.redirect(url, 301);
}

export const config = {
  matcher: ["/((?!api|_next|_vercel|.*\\..*|sitemap\\.xml|robots\\.txt).*)"],
};
