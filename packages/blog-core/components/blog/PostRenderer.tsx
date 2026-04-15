import { MDXRemote, type MDXRemoteProps } from "next-mdx-remote/rsc";
import remarkGfm from "remark-gfm";
import rehypeSlug from "rehype-slug";
import rehypeAutolinkHeadings from "rehype-autolink-headings";
import rehypePrettyCode from "rehype-pretty-code";

export interface PostRendererProps {
  source: string;
  components?: MDXRemoteProps["components"];
}

export function PostRenderer({ source, components }: PostRendererProps) {
  return (
    <MDXRemote
      source={source}
      components={components}
      options={{
        mdxOptions: {
          remarkPlugins: [remarkGfm],
          rehypePlugins: [
            rehypeSlug,
            [rehypeAutolinkHeadings, { behavior: "wrap" }],
            [
              rehypePrettyCode,
              {
                theme: { dark: "github-dark", light: "github-light" },
                keepBackground: false,
              },
            ],
          ],
        },
      }}
    />
  );
}
