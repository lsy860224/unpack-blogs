#!/usr/bin/env python3
"""
SNS 카드 생성기 — 글 1편당 IG 캐러셀 5개 × 카드 ≥5장 + X 트윗 이미지 5장.

Spec source:
  - docs/SNS_AUTOMATION.md
  - scripts/og/generate-og-all.py (brand colors / fonts 재사용)

Output:
  ~/dev/sns/{brand}/{NN}-{slug}/ig/post-{1..5}/{NN}-{role}.png   # 1080×1080
  ~/dev/sns/{brand}/{NN}-{slug}/x/post-{1..5}.png                # 1600×900

Roles: cover | context | finding | finding | cta  (per carousel)

Brand tones:
- AIGrit: Slate→Indigo gradient bg, Cyan accent, Pretendard sans
- babipanote: Paper gradient bg, Plum primary, Gowun Batang serif (heading)
"""
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# === Fonts (shared with OG pipeline) ===
F = {
    "gowun_bold": "/tmp/og-fonts/GowunBatang-Bold.ttf",
    "gowun_reg": "/tmp/og-fonts/GowunBatang-Regular.ttf",
    "lora_bold": "/tmp/og-fonts/Lora-Bold.ttf",
    "pretendard_bold": "/tmp/og-fonts/Pretendard-Bold.otf",
    "pretendard_semi": "/tmp/og-fonts/Pretendard-SemiBold.otf",
    "pretendard_reg": "/tmp/og-fonts/Pretendard-Regular.otf",
}


def font(key, size):
    return ImageFont.truetype(F[key], size)


# === Brand colors ===
BB = {
    "plum": (107, 46, 78),
    "ink": (43, 36, 32),
    "terracotta": (200, 159, 124),
    "muted": (160, 139, 122),
    "paperLight": (250, 247, 242),
    "paperDeep": (240, 235, 227),
    "white": (255, 255, 255),
}
AG = {
    "bgTop": (15, 23, 42),
    "bgBot": (30, 27, 75),
    "red": (239, 68, 68),
    "cyan": (6, 182, 212),
    "indigo": (55, 48, 163),
    "slate": (148, 163, 184),
    "white": (255, 255, 255),
    "ink": (226, 232, 240),
    "cardBg": (24, 33, 65),
}


def gradient(W, H, top_left, bot_right):
    img = Image.new("RGB", (W, H), top_left)
    px = img.load()
    for y in range(H):
        for x in range(W):
            t = (x / W + y / H) / 2
            px[x, y] = (
                int(top_left[0] * (1 - t) + bot_right[0] * t),
                int(top_left[1] * (1 - t) + bot_right[1] * t),
                int(top_left[2] * (1 - t) + bot_right[2] * t),
            )
    return img


def rounded(draw, xy, r, fill):
    x1, y1, x2, y2 = xy
    draw.rectangle([x1 + r, y1, x2 - r, y2], fill=fill)
    draw.rectangle([x1, y1 + r, x2, y2 - r], fill=fill)
    for cx, cy, a1, a2 in [
        (x1, y1, 180, 270),
        (x2 - 2 * r, y1, 270, 360),
        (x1, y2 - 2 * r, 90, 180),
        (x2 - 2 * r, y2 - 2 * r, 0, 90),
    ]:
        draw.pieslice([cx, cy, cx + 2 * r, cy + 2 * r], a1, a2, fill=fill)


def wrap(text, f, max_w, draw, max_lines=4):
    """Char-aware wrap. \\n splits hard; rest by char width."""
    out = []
    for segment in text.split("\n"):
        if draw.textlength(segment, font=f) <= max_w:
            out.append(segment)
            continue
        buf = ""
        for ch in segment:
            trial = buf + ch
            if draw.textlength(trial, font=f) <= max_w:
                buf = trial
            else:
                out.append(buf)
                buf = ch
        if buf:
            out.append(buf)
    return out[:max_lines]


# ============================================================
# AIGrit cards
# ============================================================
def aigrit_brand_mark(draw, W, H, scale=1.0, post_label=None):
    margin = int(60 * scale)
    line_y = H - margin - int(56 * scale)
    draw.rectangle(
        [margin, line_y, margin + int(60 * scale), line_y + int(3 * scale)],
        fill=AG["cyan"],
    )
    draw.text(
        (margin, line_y + int(14 * scale)),
        "[AI] Grit",
        fill=AG["cyan"],
        font=font("pretendard_bold", int(28 * scale)),
    )
    f_dom = font("pretendard_reg", int(16 * scale))
    dom = "aigrit.dev"
    dw = draw.textlength(dom, font=f_dom)
    draw.text((W - margin - dw, line_y + int(20 * scale)), dom, fill=AG["slate"], font=f_dom)
    if post_label:
        f_lbl = font("pretendard_semi", int(14 * scale))
        lw = draw.textlength(post_label, font=f_lbl)
        draw.text(
            (W - margin - lw, line_y - int(22 * scale)),
            post_label,
            fill=AG["slate"],
            font=f_lbl,
        )


def aigrit_corner_bracket(draw, W, scale=1.0):
    margin = int(60 * scale)
    size = int(50 * scale)
    t = max(2, int(3 * scale))
    x = W - margin - size
    y = margin
    draw.rectangle([x, y, x + size, y + t], fill=AG["cyan"])
    draw.rectangle([x + size - t, y, x + size, y + size], fill=AG["cyan"])


def render_aigrit_card(W, H, role, payload, post_idx=None):
    img = gradient(W, H, AG["bgTop"], AG["bgBot"])
    draw = ImageDraw.Draw(img)
    margin = int(60 * (W / 1080))
    scale = W / 1080
    aigrit_corner_bracket(draw, W, scale)

    # Badge
    badge_text = payload.get("badge", "AIGrit")
    f_badge = font("pretendard_semi", int(20 * scale))
    bw = int(draw.textlength(badge_text, font=f_badge)) + int(40 * scale)
    bh = int(40 * scale)
    rounded(draw, (margin, margin, margin + bw, margin + bh), bh // 2, AG["red"])
    bx = margin + (bw - draw.textlength(badge_text, font=f_badge)) / 2
    draw.text(
        (bx, margin + (bh - 20 * scale) / 2 - 2),
        badge_text,
        fill=AG["white"],
        font=f_badge,
    )

    if role == "cover":
        f_title = font("pretendard_bold", int(60 * scale))
        title_lines = wrap(payload["title"], f_title, W - margin * 2, draw, max_lines=3)
        y = int(H * 0.30) - len(title_lines) * int(36 * scale)
        for ln in title_lines:
            draw.text((margin, y), ln, fill=AG["white"], font=f_title)
            y += int(74 * scale)
        if "hook" in payload:
            f_hook = font("pretendard_bold", int(34 * scale))
            for ln in wrap(payload["hook"], f_hook, W - margin * 2, draw, max_lines=2):
                y += int(20 * scale)
                draw.text((margin, y), ln, fill=AG["cyan"], font=f_hook)
                y += int(46 * scale)

    elif role == "context":
        f_h = font("pretendard_bold", int(44 * scale))
        f_b = font("pretendard_reg", int(28 * scale))
        for ln in wrap(payload["heading"], f_h, W - margin * 2, draw, max_lines=2):
            draw.text((margin, int(H * 0.16)), ln, fill=AG["cyan"], font=f_h)
        y = int(H * 0.16) + int(78 * scale)
        for line in payload["bullets"]:
            for ln in wrap("· " + line, f_b, W - margin * 2, draw, max_lines=2):
                draw.text((margin, y), ln, fill=AG["white"], font=f_b)
                y += int(42 * scale)
            y += int(8 * scale)

    elif role == "finding":
        f_h = font("pretendard_bold", int(38 * scale))
        f_metric = font("pretendard_bold", int(72 * scale))
        f_label = font("pretendard_semi", int(24 * scale))
        for ln in wrap(payload["heading"], f_h, W - margin * 2, draw, max_lines=2):
            draw.text((margin, int(H * 0.14)), ln, fill=AG["cyan"], font=f_h)
        col_w = (W - margin * 2 - int(40 * scale)) // 2
        cy = int(H * 0.40)
        for i, m in enumerate(payload["metrics"]):
            cx = margin + i * (col_w + int(40 * scale))
            rounded(draw, (cx, cy, cx + col_w, cy + int(220 * scale)), int(20 * scale), AG["cardBg"])
            draw.text((cx + int(28 * scale), cy + int(28 * scale)), m["tool"], fill=AG["slate"], font=f_label)
            draw.text(
                (cx + int(28 * scale), cy + int(64 * scale)),
                m["value"],
                fill=AG["cyan"] if m.get("winner") else AG["white"],
                font=f_metric,
            )
            f_note = font("pretendard_reg", int(20 * scale))
            for j, ln in enumerate(wrap(m["note"], f_note, col_w - int(56 * scale), draw, max_lines=2)):
                draw.text(
                    (cx + int(28 * scale), cy + int(160 * scale) + j * int(28 * scale)),
                    ln,
                    fill=AG["slate"],
                    font=f_note,
                )
        if "caption" in payload:
            f_cap = font("pretendard_reg", int(22 * scale))
            for j, ln in enumerate(wrap(payload["caption"], f_cap, W - margin * 2, draw, max_lines=2)):
                draw.text(
                    (margin, cy + int(260 * scale) + j * int(34 * scale)),
                    ln,
                    fill=AG["slate"],
                    font=f_cap,
                )

    elif role == "list":
        # bulleted list with optional sub-bullets
        f_h = font("pretendard_bold", int(40 * scale))
        f_b = font("pretendard_semi", int(26 * scale))
        f_sub = font("pretendard_reg", int(22 * scale))
        for ln in wrap(payload["heading"], f_h, W - margin * 2, draw, max_lines=2):
            draw.text((margin, int(H * 0.14)), ln, fill=AG["cyan"], font=f_h)
        y = int(H * 0.14) + int(72 * scale)
        for it in payload["items"]:
            # primary
            txt = it["primary"]
            for ln in wrap("· " + txt, f_b, W - margin * 2, draw, max_lines=2):
                draw.text((margin, y), ln, fill=AG["white"], font=f_b)
                y += int(38 * scale)
            if "sub" in it:
                for ln in wrap("    " + it["sub"], f_sub, W - margin * 2, draw, max_lines=2):
                    draw.text((margin, y), ln, fill=AG["slate"], font=f_sub)
                    y += int(32 * scale)
            y += int(8 * scale)

    elif role == "cta":
        f_h = font("pretendard_bold", int(54 * scale))
        f_url = font("pretendard_bold", int(34 * scale))
        f_b = font("pretendard_reg", int(24 * scale))
        for ln in wrap(payload["heading"], f_h, W - margin * 2, draw, max_lines=2):
            draw.text((margin, int(H * 0.18)), ln, fill=AG["cyan"], font=f_h)
        y = int(H * 0.42)
        for line in payload.get("bullets", []):
            for ln in wrap("· " + line, f_b, W - margin * 2, draw, max_lines=2):
                draw.text((margin, y), ln, fill=AG["white"], font=f_b)
                y += int(36 * scale)
            y += int(6 * scale)
        url = payload["url"]
        url_y = int(H * 0.78)
        rounded(draw, (margin, url_y, W - margin, url_y + int(72 * scale)), int(36 * scale), AG["cyan"])
        uw = draw.textlength(url, font=f_url)
        draw.text(
            (margin + (W - margin * 2 - uw) / 2, url_y + int(18 * scale)),
            url,
            fill=AG["bgTop"],
            font=f_url,
        )

    post_label = f"Carousel {post_idx} of 5" if post_idx else None
    aigrit_brand_mark(draw, W, H, scale, post_label)
    return img


# ============================================================
# babipanote cards
# ============================================================
def babi_brand_mark(draw, W, H, scale=1.0, post_label=None):
    margin = int(60 * scale)
    line_y = H - margin - int(56 * scale)
    draw.rectangle(
        [margin, line_y, margin + int(60 * scale), line_y + int(3 * scale)],
        fill=BB["terracotta"],
    )
    draw.text((margin, line_y + int(14 * scale)), "babipa", fill=BB["ink"], font=font("gowun_bold", int(28 * scale)))
    f_brand_r = font("gowun_bold", int(28 * scale))
    bt = "babipanote·"
    bw = draw.textlength(bt, font=f_brand_r)
    draw.text((W - margin - bw, line_y + int(14 * scale)), bt, fill=BB["plum"], font=f_brand_r)
    f_dom = font("pretendard_reg", int(16 * scale))
    dom = "babipanote.com"
    dw = draw.textlength(dom, font=f_dom)
    draw.text((W - margin - dw, line_y + int(50 * scale)), dom, fill=BB["muted"], font=f_dom)
    if post_label:
        f_lbl = font("pretendard_semi", int(14 * scale))
        lw = draw.textlength(post_label, font=f_lbl)
        draw.text((W - margin - lw, line_y - int(22 * scale)), post_label, fill=BB["muted"], font=f_lbl)


def babi_quote_glyph(img, W, scale=1.0):
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    f_q = font("lora_bold", int(120 * scale))
    q = "“”"
    qw = od.textlength(q, font=f_q)
    od.text((W - qw - int(60 * scale), int(20 * scale)), q, fill=(*BB["plum"], 80), font=f_q)
    return Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")


def render_babipanote_card(W, H, role, payload, post_idx=None):
    img = gradient(W, H, BB["paperLight"], BB["paperDeep"])
    draw = ImageDraw.Draw(img)
    margin = int(60 * (W / 1080))
    scale = W / 1080

    badge_text = payload.get("badge", "babipanote")
    f_badge = font("pretendard_semi", int(20 * scale))
    bw = int(draw.textlength(badge_text, font=f_badge)) + int(40 * scale)
    bh = int(40 * scale)
    rounded(draw, (margin, margin, margin + bw, margin + bh), bh // 2, BB["plum"])
    bx = margin + (bw - draw.textlength(badge_text, font=f_badge)) / 2
    draw.text((bx, margin + (bh - 20 * scale) / 2 - 2), badge_text, fill=BB["white"], font=f_badge)

    if role == "cover":
        img = babi_quote_glyph(img, W, scale)
        draw = ImageDraw.Draw(img)
        f_title = font("gowun_bold", int(60 * scale))
        title_lines = wrap(payload["title"], f_title, W - margin * 2, draw, max_lines=3)
        y = int(H * 0.30) - len(title_lines) * int(36 * scale)
        for ln in title_lines:
            draw.text((margin, y), ln, fill=BB["ink"], font=f_title)
            y += int(78 * scale)
        if "hook" in payload:
            f_hook = font("pretendard_reg", int(28 * scale))
            for ln in wrap(payload["hook"], f_hook, W - margin * 2, draw, max_lines=2):
                y += int(8 * scale)
                draw.text((margin, y), ln, fill=BB["plum"], font=f_hook)
                y += int(40 * scale)

    elif role == "context":
        f_h = font("gowun_bold", int(44 * scale))
        f_b = font("pretendard_reg", int(28 * scale))
        for ln in wrap(payload["heading"], f_h, W - margin * 2, draw, max_lines=2):
            draw.text((margin, int(H * 0.16)), ln, fill=BB["plum"], font=f_h)
        y = int(H * 0.16) + int(78 * scale)
        for line in payload["bullets"]:
            for ln in wrap("· " + line, f_b, W - margin * 2, draw, max_lines=2):
                draw.text((margin, y), ln, fill=BB["ink"], font=f_b)
                y += int(42 * scale)
            y += int(8 * scale)

    elif role == "quote":
        img = babi_quote_glyph(img, W, scale)
        draw = ImageDraw.Draw(img)
        f_q = font("gowun_bold", int(46 * scale))
        body = payload["body"]
        y = int(H * 0.30)
        for ln in wrap(body, f_q, W - margin * 2, draw, max_lines=5):
            draw.text((margin, y), ln, fill=BB["ink"], font=f_q)
            y += int(64 * scale)
        if "footer" in payload:
            f_f = font("pretendard_reg", int(24 * scale))
            for ln in wrap(payload["footer"], f_f, W - margin * 2, draw, max_lines=2):
                draw.text((margin, int(H * 0.78)), ln, fill=BB["muted"], font=f_f)
                break

    elif role == "limit":
        f_h = font("gowun_bold", int(38 * scale))
        f_b = font("pretendard_reg", int(26 * scale))
        y = int(H * 0.16)
        for blk in payload["blocks"]:
            draw.text((margin, y), blk["label"], fill=BB["plum"], font=f_h)
            y += int(56 * scale)
            for line in blk["lines"]:
                for ln in wrap("· " + line, f_b, W - margin * 2, draw, max_lines=2):
                    draw.text((margin, y), ln, fill=BB["ink"], font=f_b)
                    y += int(38 * scale)
            y += int(24 * scale)

    elif role == "list":
        f_h = font("gowun_bold", int(40 * scale))
        f_b = font("pretendard_reg", int(26 * scale))
        f_sub = font("pretendard_reg", int(22 * scale))
        for ln in wrap(payload["heading"], f_h, W - margin * 2, draw, max_lines=2):
            draw.text((margin, int(H * 0.16)), ln, fill=BB["plum"], font=f_h)
        y = int(H * 0.16) + int(72 * scale)
        for it in payload["items"]:
            for ln in wrap("· " + it["primary"], f_b, W - margin * 2, draw, max_lines=2):
                draw.text((margin, y), ln, fill=BB["ink"], font=f_b)
                y += int(38 * scale)
            if "sub" in it:
                for ln in wrap("    " + it["sub"], f_sub, W - margin * 2, draw, max_lines=2):
                    draw.text((margin, y), ln, fill=BB["muted"], font=f_sub)
                    y += int(32 * scale)
            y += int(8 * scale)

    elif role == "cta":
        f_h = font("gowun_bold", int(46 * scale))
        f_url = font("pretendard_bold", int(30 * scale))
        f_b = font("pretendard_reg", int(24 * scale))
        for ln in wrap(payload["heading"], f_h, W - margin * 2, draw, max_lines=2):
            draw.text((margin, int(H * 0.20)), ln, fill=BB["plum"], font=f_h)
        y = int(H * 0.42)
        for line in payload.get("bullets", []):
            for ln in wrap("· " + line, f_b, W - margin * 2, draw, max_lines=2):
                draw.text((margin, y), ln, fill=BB["ink"], font=f_b)
                y += int(36 * scale)
            y += int(6 * scale)
        url = payload["url"]
        url_y = int(H * 0.78)
        rounded(draw, (margin, url_y, W - margin, url_y + int(72 * scale)), int(36 * scale), BB["plum"])
        uw = draw.textlength(url, font=f_url)
        draw.text(
            (margin + (W - margin * 2 - uw) / 2, url_y + int(20 * scale)),
            url,
            fill=BB["paperLight"],
            font=f_url,
        )

    post_label = f"Carousel {post_idx} of 5" if post_idx else None
    babi_brand_mark(draw, W, H, scale, post_label)
    return img


# ============================================================
# Driver
# ============================================================
def render_post(spec):
    brand = spec["brand"]
    folder = Path.home() / "dev" / "sns" / brand / spec["pipeline_file"]
    renderer = render_aigrit_card if brand == "aigrit" else render_babipanote_card

    written = []

    for pi, carousel in enumerate(spec["carousels"], start=1):
        cdir = folder / "ig" / f"post-{pi}"
        cdir.mkdir(parents=True, exist_ok=True)
        for ci, card in enumerate(carousel["cards"], start=1):
            role = card["role"]
            name_role = {"cover": "cover", "cta": "cta"}.get(role, "card")
            fname = f"{ci:02d}-{name_role}.png"
            img = renderer(1080, 1080, role, card["payload"], post_idx=pi)
            out = cdir / fname
            img.save(out, "PNG", optimize=True)
            kb = out.stat().st_size / 1024
            written.append(f"ig/post-{pi}/{fname}  ({kb:.1f}KB)")

        # X feed image (one per carousel, using its first finding/quote card)
        x_dir = folder / "x"
        x_dir.mkdir(parents=True, exist_ok=True)
        x_card = carousel.get("x_card", carousel["cards"][0])
        img = renderer(1600, 900, x_card["role"], x_card["payload"], post_idx=pi)
        out = x_dir / f"post-{pi}.png"
        img.save(out, "PNG", optimize=True)
        kb = out.stat().st_size / 1024
        written.append(f"x/post-{pi}.png  ({kb:.1f}KB)")

    return written


# ============================================================
# CLI entry — _spec.json disk-based
# ============================================================
import argparse
import datetime
import json as _json
from pathlib import Path as _Path

SNS_ROOT = _Path.home() / "dev" / "sns"
BRAND_DOMAIN = {
    "aigrit": "aigrit.dev/ko/blog",
    "babipanote": "babipanote.com/blog",
}


def load_spec(path: _Path) -> dict:
    with path.open(encoding="utf-8") as f:
        spec = _json.load(f)
    for k in ("brand", "pipeline_file", "carousels"):
        if k not in spec:
            raise SystemExit(f"❌ spec missing field: {k} ({path})")
    if spec["brand"] not in ("aigrit", "babipanote"):
        raise SystemExit(f"❌ unknown brand: {spec['brand']}")
    if len(spec["carousels"]) != 5:
        raise SystemExit(
            f"❌ {path} carousels != 5 (got {len(spec['carousels'])})"
        )
    return spec


def discover_specs(brand=None, slug_prefix=None):
    if slug_prefix and brand:
        return [SNS_ROOT / brand / slug_prefix / "_spec.json"]
    if brand:
        return sorted(SNS_ROOT.glob(f"{brand}/*/_spec.json"))
    return sorted(SNS_ROOT.glob("*/*/_spec.json"))


def write_meta(spec: dict) -> _Path:
    brand = spec["brand"]
    pf = spec["pipeline_file"]
    folder = SNS_ROOT / brand / pf
    slug = spec.get("slug") or pf
    blog_url = spec.get("blog_url") or f"https://{BRAND_DOMAIN[brand]}/{slug}"
    meta = {
        "brand": brand,
        "pipeline_file": pf,
        "slug": slug,
        "title": spec.get("title", ""),
        "blog_url": blog_url,
        "date_published": spec.get("date_published", ""),
        "tags": spec.get("tags", []),
        "feeds_per_platform": 5,
        "carousels": [
            {
                "post": i + 1,
                "label": c.get("label", f"post-{i+1}"),
                "folder": f"ig/post-{i+1}",
            }
            for i, c in enumerate(spec["carousels"])
        ],
        "x_images": [f"x/post-{i+1}.png" for i in range(5)],
        "generated_at": datetime.datetime.now().strftime("%Y-%m-%d"),
        "status": "drafted-not-posted",
    }
    out = folder / "_meta.json"
    out.write_text(
        _json.dumps(meta, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return out


def main():
    ap = argparse.ArgumentParser(
        description="SNS 카드 생성기 — _spec.json 기반 (IG 5 캐러셀 + X 5 이미지)"
    )
    ap.add_argument("--spec", type=_Path, help="단일 spec 파일 경로")
    ap.add_argument(
        "--brand",
        choices=["aigrit", "babipanote"],
        help="브랜드만 지정 시 해당 브랜드의 모든 spec 자동 스캔",
    )
    ap.add_argument(
        "--slug-prefix",
        help="파이프라인 파일명 prefix (예: 15-aigrit-sell-ai-prompts-promptbase). --brand 와 함께 사용",
    )
    ap.add_argument(
        "--skip-meta",
        action="store_true",
        help="_meta.json 자동 생성 건너뛰기",
    )
    args = ap.parse_args()

    if args.spec:
        paths = [args.spec.resolve()]
    else:
        paths = discover_specs(args.brand, args.slug_prefix)

    if not paths:
        ap.error(
            "처리할 _spec.json 을 찾지 못했습니다. --spec, --brand, --slug-prefix 중 하나 이상을 지정하세요."
        )

    total = 0
    for path in paths:
        if not path.exists():
            print(f"⚠️  스킵 (파일 없음): {path}")
            continue
        spec = load_spec(path)
        out = render_post(spec)
        for line in out:
            print(f"✓ {spec['brand']}/{spec['pipeline_file']}/{line}")
        if not args.skip_meta:
            meta_path = write_meta(spec)
            print(f"📝 meta: {meta_path}")
        total += len(out)
    print(f"\n✅ Generated {total} cards from {len(paths)} spec(s).")


if __name__ == "__main__":
    main()

