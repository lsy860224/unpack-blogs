#!/usr/bin/env node
// 모든 MDX 본문(예약 글 포함)을 컴파일해 문법 오류를 미리 잡는다.
// 빌드는 발행 시각이 지난 글만 렌더링하므로, 예약 글의 MDX 오류는 발행일에야 드러난다.
// 사용: node scripts/check-mdx.mjs [디렉터리...]  (기본: 두 앱의 content/posts 전체)
import { readFileSync, readdirSync, statSync } from "node:fs";
import { join } from "node:path";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL("..", import.meta.url));
const require = createRequire(join(root, "packages/blog-core/package.json"));
const { compile } = await import(
  require.resolve("@mdx-js/mdx", { paths: [require.resolve("next-mdx-remote")] })
);
const remarkGfm = (await import(require.resolve("remark-gfm"))).default;

const defaults = [
  "apps/aigrit/content/posts/ko",
  "apps/aigrit/content/posts/en",
  "apps/babipanote/content/posts",
].map((d) => join(root, d));
const dirs = process.argv.length > 2 ? process.argv.slice(2) : defaults;

function listMdx(dir) {
  return readdirSync(dir).flatMap((name) => {
    const path = join(dir, name);
    if (statSync(path).isDirectory()) return listMdx(path);
    return name.endsWith(".mdx") ? [path] : [];
  });
}

let total = 0;
const failures = [];
for (const dir of dirs) {
  for (const file of listMdx(dir)) {
    total += 1;
    const body = readFileSync(file, "utf8").replace(/^---\n[\s\S]*?\n---\n/, "");
    try {
      await compile(body, { remarkPlugins: [remarkGfm] });
    } catch (error) {
      failures.push(`${file.replace(root, "")}: ${String(error.message).slice(0, 200)}`);
    }
  }
}

console.log(`MDX compiled: ${total}, failed: ${failures.length}`);
for (const line of failures) console.log(`  ✗ ${line}`);
process.exit(failures.length > 0 ? 1 : 0);
