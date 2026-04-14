import Script from "next/script";

export interface AdSenseScriptProps {
  publisherId?: string;
}

export function AdSenseScript({ publisherId }: AdSenseScriptProps) {
  if (!publisherId) return null;
  return (
    <Script
      async
      src={`https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${publisherId}`}
      crossOrigin="anonymous"
      strategy="afterInteractive"
    />
  );
}
