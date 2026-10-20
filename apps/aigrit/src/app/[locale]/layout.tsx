import { notFound } from "next/navigation";
import type { Metadata, Viewport } from "next";
import { Inter, JetBrains_Mono } from "next/font/google";
import localFont from "next/font/local";
import {
  BrandProvider,
  buildMetadata,
  GoogleAnalytics,
  AdSenseScript,
  SUPPORTED_LOCALES,
  toBcp47,
  toOgLocale,
} from "@unpack/blog-core";
import { brandConfig, getLocalizedBrand } from "../../../brand.config";
import { Header } from "../../components/layout/Header";
import { buildLocaleIndex } from "../../lib/locale-index";
import { Footer } from "../../components/layout/Footer";
import "../globals.css";

const pretendard = localFont({
  src: "../../../public/fonts/PretendardVariable.woff2",
  variable: "--font-pretendard",
  display: "swap",
  weight: "45 920",
});

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
  display: "swap",
});

const jetbrains = JetBrains_Mono({
  subsets: ["latin"],
  variable: "--font-jetbrains",
  display: "swap",
});

export function generateStaticParams() {
  return SUPPORTED_LOCALES.map((locale) => ({ locale }));
}

const adsenseClientId = brandConfig.monetization.adsense
  ? brandConfig.monetization.adsensePublisherId
  : undefined;

export async function generateMetadata({
  params,
}: {
  params: Promise<{ locale: string }>;
}): Promise<Metadata> {
  const { locale } = await params;
  const localized = getLocalizedBrand(locale);
  return {
    ...buildMetadata({
      title: `${localized.name} — ${localized.tagline}`,
      description: localized.description,
      siteName: localized.name,
      siteUrl: localized.url,
      path: `/${locale}`,
      locale: toOgLocale(locale),
      hrefLangs: {
        ko: "/ko",
        en: "/en",
        "x-default": "/ko",
      },
    }),
    title: {
      default: `${localized.name} — ${localized.tagline}`,
      template: `%s | ${localized.name}`,
    },
    verification: {
      google: "OAmX5Qm-Z-IU2IOnM60RakOqHqY-h99z1eE2iE5tyTE",
      other: {
        "naver-site-verification": "58fbc5aa649e7772ee090c6fe2cee3296cf34870",
      },
    },
    // AdSense 사이트 소유권 확인용 메타 태그 (광고 스크립트·ads.txt 와 함께 3중 확인)
    ...(adsenseClientId
      ? { other: { "google-adsense-account": adsenseClientId } }
      : {}),
  };
}

export const viewport: Viewport = {
  themeColor: [
    {
      media: "(prefers-color-scheme: light)",
      color: brandConfig.theme.colors.background,
    },
    {
      media: "(prefers-color-scheme: dark)",
      color:
        brandConfig.theme.dark?.background ??
        brandConfig.theme.colors.background,
    },
  ],
};

export default async function RootLayout({
  children,
  params,
}: Readonly<{
  children: React.ReactNode;
  params: Promise<{ locale: string }>;
}>) {
  const { locale } = await params;
  if (!(SUPPORTED_LOCALES as readonly string[]).includes(locale)) {
    notFound();
  }
  const localized = getLocalizedBrand(locale);
  const runtimeConfig = {
    ...brandConfig,
    locale: toBcp47(locale),
    tagline: localized.tagline,
    description: localized.description,
    nav: localized.nav,
  };

  return (
    <html
      lang={locale}
      suppressHydrationWarning
      className={`${pretendard.variable} ${inter.variable} ${jetbrains.variable} h-full antialiased`}
    >
      <head>
        <script
          dangerouslySetInnerHTML={{
            __html: `(function(){try{var s=localStorage.getItem('aigrit-theme');var m=window.matchMedia('(prefers-color-scheme: dark)').matches;if(s==='dark'||(!s&&m)){document.documentElement.classList.add('dark');}}catch(e){}})();`,
          }}
        />
      </head>
      <body className="min-h-full flex flex-col">
        <BrandProvider config={runtimeConfig}>
          <Header locale={locale} localeIndex={buildLocaleIndex()} />
          <main className="flex-1">{children}</main>
          <Footer locale={locale} />
        </BrandProvider>
        <GoogleAnalytics gaId={brandConfig.analytics.gaId} />
        <AdSenseScript publisherId={adsenseClientId} />
      </body>
    </html>
  );
}
