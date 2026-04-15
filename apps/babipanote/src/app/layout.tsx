import type { Metadata, Viewport } from "next";
import { Inter, JetBrains_Mono, Gowun_Batang, Lora } from "next/font/google";
import localFont from "next/font/local";
import { BrandProvider, GoogleAnalytics, buildMetadata } from "@unpack/blog-core";
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

const gowunBatang = Gowun_Batang({
  subsets: ["latin"],
  weight: ["400", "700"],
  variable: "--font-gowun-batang",
  display: "swap",
});

const lora = Lora({
  subsets: ["latin"],
  variable: "--font-lora",
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
    other: {
      "naver-site-verification": "e114db7c0ebcb7a99c7635f44b05ea88b26fa057",
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
      className={`${pretendard.variable} ${inter.variable} ${jetbrains.variable} ${gowunBatang.variable} ${lora.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col">
        <BrandProvider config={brandConfig}>
          <Header />
          <main className="flex-1">{children}</main>
          <Footer />
        </BrandProvider>
        <GoogleAnalytics gaId={brandConfig.analytics.gaId} />
      </body>
    </html>
  );
}
