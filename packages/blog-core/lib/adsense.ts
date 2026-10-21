/**
 * AdSense 게시자 ID 정규화 헬퍼.
 *
 * AdSense 는 같은 ID 를 두 가지 표기로 요구한다.
 * - 광고 스크립트 `client=` · `data-ad-client` · `google-adsense-account` 메타: `ca-pub-XXXXXXXXXXXXXXXX`
 * - ads.txt: `pub-XXXXXXXXXXXXXXXX`
 * 환경변수에 어느 형식을 넣어도 양쪽이 맞도록 여기서 한 번만 변환한다.
 */

/** AdSense 게시자 ID 는 `pub-` 뒤에 숫자 16자리 */
const PUBLISHER_ID_PATTERN = /^(?:ca-)?(pub-\d{16})$/;

/** Google 의 ads.txt 인증기관 ID (모든 AdSense 게시자 공통) */
export const GOOGLE_ADS_TXT_CERT_ID = "f08c47fec0942fa0";

/**
 * `pub-…` 또는 `ca-pub-…` 를 받아 `ca-pub-…` 로 돌려준다.
 * 비어 있거나 형식이 틀리면 undefined (광고 코드를 아예 렌더하지 않게).
 */
export function normalizeAdsenseClientId(raw?: string): string | undefined {
  const trimmed = raw?.trim();
  if (!trimmed) return undefined;
  const match = PUBLISHER_ID_PATTERN.exec(trimmed);
  if (!match) {
    console.warn(
      `[adsense] NEXT_PUBLIC_ADSENSE_ID 형식이 올바르지 않습니다: "${trimmed}" — "ca-pub-" + 숫자 16자리여야 합니다. 광고 코드를 렌더하지 않습니다.`,
    );
    return undefined;
  }
  return `ca-${match[1]}`;
}

/** `ca-pub-…` → ads.txt 용 `pub-…` */
export function toAdsTxtPublisherId(clientId: string): string {
  return clientId.replace(/^ca-/, "");
}

/** ads.txt 본문 생성. ID 가 없으면 주석만 담아 200 으로 응답할 수 있게 한다. */
export function buildAdsTxt(clientId?: string): string {
  if (!clientId) {
    return [
      "# Google AdSense — ads.txt",
      "# NEXT_PUBLIC_ADSENSE_ID 환경변수가 설정되면 아래에 게시자 줄이 자동으로 생성됩니다.",
      "",
    ].join("\n");
  }
  return [
    `google.com, ${toAdsTxtPublisherId(clientId)}, DIRECT, ${GOOGLE_ADS_TXT_CERT_ID}`,
    "",
  ].join("\n");
}
