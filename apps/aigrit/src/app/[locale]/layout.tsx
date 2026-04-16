import type { Metadata, Viewport } from "next";
import { Inter, JetBrains_Mono } from "next/font/google";
import localFont from "next/font/local";
import {
  BrandProvider,
  buildMetadata,
  GoogleAnalytics,
  AdSenseScript,
} from "@unpack/blog-core";
import { brandConfig } from "../../brand.config";
import { Header } from "../components/layout/Header";
import { Footer } from "../components/layout/Footer";
import "./globals.css";

const pretendard = localFont({
  src: "../../public/fonts/PretendardVariable.woff2",
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

export const metadata: Metadata = {
  ...buildMetadata({
    title: `${brandConfig.name} — ${brandConfig.tagline}`,
    description: brandConfig.description,
    siteName: brandConfig.name,
    siteUrl: brandConfig.url,
  }),
  title: {
    default: `${brandConfig.name} — ${brandConfig.tagline}`,
    template: `%s | ${brandConfig.name}`,
  },
  verification: {
    google: "OAmX5Qm-Z-IU2IOnM60RakOqHqY-h99z1eE2iE5tyTE",
    other: {
      "naver-site-verification": "b034ba1644492f2a15ffa439789554ca2b037777",
    },
  },
};

export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: brandConfig.theme.colors.background },
    {
      media: "(prefers-color-scheme: dark)",
      color: brandConfig.theme.dark?.background ?? brandConfig.theme.colors.background,
    },
  ],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang={brandConfig.locale.replace("-", "_").slice(0, 2)}
      className={`${pretendard.variable} ${inter.variable} ${jetbrains.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col">
        <BrandProvider config={brandConfig}>
          <Header />
          <main className="flex-1">{children}</main>
          <Footer />
        </BrandProvider>
        <GoogleAnalytics gaId={brandConfig.analytics.gaId} />
        {brandConfig.monetization.adsense && (
          <AdSenseScript publisherId={brandConfig.monetization.adsensePublisherId} />
        )}
      </body>
    </html>
  );
}
