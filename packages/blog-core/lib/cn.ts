/**
 * Tailwind class 조립 유틸. clsx 의존성 없이 falsy 제거 + 공백 join.
 *
 * @example
 *   cn("base", condition && "active", className)
 *   cn("mt-4", className) // className가 undefined면 자동 생략
 */
export type ClassValue = string | number | false | null | undefined;

export function cn(...classes: ClassValue[]): string {
  return classes.filter(Boolean).join(" ");
}
