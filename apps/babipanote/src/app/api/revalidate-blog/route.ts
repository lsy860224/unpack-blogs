import { NextResponse } from "next/server";
import { revalidatePath } from "next/cache";

/**
 * 예약 발행 재검증 엔드포인트.
 *
 * Hobby 플랜은 sub-daily Vercel cron 배포가 거부되므로 `vercel.json` cron 대신
 * 외부 스케줄러(UptimeRobot / cron-job.org 등)로 5~15분마다 아래를 호출한다:
 *
 *   GET https://babipanote.com/api/revalidate-blog
 *   Header: Authorization: Bearer <CRON_SECRET>
 *
 * 발행 시각이 지난 예약글을 목록·홈·상세·sitemap에 즉시 반영한다.
 * (각 페이지 revalidate=600 으로도 최대 10분 내 자동 반영되지만, 핀거가 지연을 없앤다.)
 */
export const dynamic = "force-dynamic";

export function GET(request: Request): NextResponse {
  const secret = process.env.CRON_SECRET;
  if (!secret) {
    return NextResponse.json(
      { ok: false, error: "CRON_SECRET not configured" },
      { status: 500 },
    );
  }
  if (request.headers.get("authorization") !== `Bearer ${secret}`) {
    return NextResponse.json(
      { ok: false, error: "Unauthorized" },
      { status: 401 },
    );
  }

  revalidatePath("/");
  revalidatePath("/blog");
  revalidatePath("/blog/[slug]", "page");
  revalidatePath("/sitemap.xml");

  return NextResponse.json({
    ok: true,
    revalidatedAt: new Date().toISOString(),
  });
}
