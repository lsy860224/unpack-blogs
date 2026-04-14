import { Callout } from "./Callout";
import { CompareTable } from "./CompareTable";
import { ProCon, Pros, Cons } from "./ProCon";
import { AffiliateLink } from "./AffiliateLink";

export { Callout } from "./Callout";
export type { CalloutProps, CalloutType } from "./Callout";
export { CompareTable } from "./CompareTable";
export type {
  CompareTableProps,
  CompareTableRow,
  CompareTableColumn,
} from "./CompareTable";
export { ProCon, Pros, Cons } from "./ProCon";
export type { ProConProps, ProsConsWrapperProps } from "./ProCon";
export { AffiliateLink } from "./AffiliateLink";
export type { AffiliateLinkProps } from "./AffiliateLink";

/**
 * PostRenderer에 주입할 기본 MDX 컴포넌트 맵.
 * 배열/객체 prop 전달은 next-mdx-remote/rsc에서 지원되지 않으므로
 * 사용자는 children 기반 API를 사용해야 한다 (Pros/Cons 서브컴포넌트 등).
 */
export const defaultMdxComponents = {
  Callout,
  CompareTable,
  ProCon,
  Pros,
  Cons,
  AffiliateLink,
};
