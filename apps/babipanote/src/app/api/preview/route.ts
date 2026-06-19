import { draftMode } from "next/headers";
import { redirect } from "next/navigation";
import { NextResponse } from "next/server";

/**
 * Draft Mode 미리보기 토글 — 미래(예약) 글을 발행 전에 확인할 때만 사용.
 *
 *   활성화:  /api/preview?secret=<CRON_SECRET>&slug=<slug>
 *   비활성화: /api/preview?disable=1
 *
 * 활성화하면 쿠키가 설정되어 상세 페이지가 `includeFuture`로 미래글을 렌더한다.
 */
export const dynamic = "force-dynamic";

export async function GET(request: Request): Promise<NextResponse> {
  const { searchParams } = new URL(request.url);
  const draft = await draftMode();

  if (searchParams.get("disable")) {
    draft.disable();
    redirect("/");
  }

  const secret = process.env.CRON_SECRET;
  if (!secret || searchParams.get("secret") !== secret) {
    return NextResponse.json(
      { ok: false, error: "Unauthorized" },
      { status: 401 },
    );
  }

  draft.enable();
  const slug = searchParams.get("slug");
  redirect(slug ? `/blog/${slug}` : "/");
}
