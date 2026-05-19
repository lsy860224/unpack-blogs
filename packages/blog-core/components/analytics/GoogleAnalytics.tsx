import Script from "next/script";

export interface GoogleAnalyticsProps {
  gaId?: string;
  /**
   * Google Signals (demographics·interest reports).
   * `true` (default) keeps parity with AdSense personalized ads.
   * `false` opts out — disclose accordingly in the privacy policy.
   */
  allowGoogleSignals?: boolean;
  /**
   * Ad personalization signals. Same trade-off as `allowGoogleSignals`.
   * Default `true` matches AdSense default behavior.
   */
  allowAdPersonalization?: boolean;
}

export function GoogleAnalytics({
  gaId,
  allowGoogleSignals = true,
  allowAdPersonalization = true,
}: GoogleAnalyticsProps) {
  if (!gaId) return null;
  return (
    <>
      <Script
        src={`https://www.googletagmanager.com/gtag/js?id=${gaId}`}
        strategy="afterInteractive"
      />
      <Script id="ga4-init" strategy="afterInteractive">
        {`
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
          gtag('config', '${gaId}', {
            anonymize_ip: true,
            allow_google_signals: ${allowGoogleSignals},
            allow_ad_personalization_signals: ${allowAdPersonalization}
          });
        `}
      </Script>
    </>
  );
}
