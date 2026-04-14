"use client";

import { createContext, useContext } from "react";
import type { BrandConfig } from "../types/brand";

const BrandContext = createContext<BrandConfig | null>(null);

export function BrandProvider({
  config,
  children,
}: {
  config: BrandConfig;
  children: React.ReactNode;
}) {
  return <BrandContext.Provider value={config}>{children}</BrandContext.Provider>;
}

export function useBrand(): BrandConfig {
  const ctx = useContext(BrandContext);
  if (!ctx) {
    throw new Error("useBrand must be called within a <BrandProvider>");
  }
  return ctx;
}
