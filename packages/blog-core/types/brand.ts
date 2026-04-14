export interface BrandNavItem {
  label: string;
  href: string;
}

export interface BrandSocial {
  x?: string;
  instagram?: string;
  github?: string;
  threads?: string;
  youtube?: string;
}

export interface BrandThemeColors {
  primary: string;
  secondary: string;
  secondaryHover?: string;
  accentGreen: string;
  accentRed: string;
  background: string;
  foreground: string;
  surface?: string;
}

export interface BrandThemeFonts {
  sans: string;
  serif?: string;
  mono: string;
}

export interface BrandTheme {
  colors: BrandThemeColors;
  dark?: Partial<BrandThemeColors>;
  fonts: BrandThemeFonts;
}

export interface BrandMonetization {
  adsense: boolean;
  affiliateLinks: boolean;
  adsensePublisherId?: string;
}

export interface BrandLayout {
  style: "category" | "timeline";
  showSidebar: boolean;
  postsPerPage: number;
}

export interface BrandAnalytics {
  gaId?: string;
}

export interface BrandComments {
  giscusRepo?: string;
  giscusRepoId?: string;
  giscusCategory?: string;
  giscusCategoryId?: string;
}

export interface BrandConfig {
  name: string;
  tagline: string;
  description: string;
  url: string;
  locale: string;
  nav: BrandNavItem[];
  social: BrandSocial;
  theme: BrandTheme;
  monetization: BrandMonetization;
  layout: BrandLayout;
  analytics: BrandAnalytics;
  comments: BrandComments;
}
