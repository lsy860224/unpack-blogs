#!/bin/bash
# Download fonts needed by generate-og-all.py into /tmp/og-fonts/

set -e
mkdir -p /tmp/og-fonts
cd /tmp/og-fonts

echo "== Gowun Batang (Google Fonts) =="
[ -f GowunBatang-Bold.ttf ] || curl -sSL -o GowunBatang-Bold.ttf \
  "https://fonts.gstatic.com/s/gowunbatang/v12/ijwNs5nhRMIjYsdSgcMa3wRZ4J7awg.ttf"
[ -f GowunBatang-Regular.ttf ] || curl -sSL -o GowunBatang-Regular.ttf \
  "https://fonts.gstatic.com/s/gowunbatang/v12/ijwSs5nhRMIjYsdSgcMa3wRhXA.ttf"

echo "== Lora (Google Fonts) =="
[ -f Lora-Bold.ttf ] || curl -sSL -o Lora-Bold.ttf \
  "https://fonts.gstatic.com/s/lora/v37/0QI6MX1D_JOuGQbT0gvTJPa787z5vCJG.ttf"

echo "== Pretendard (GitHub orioncactus/pretendard) =="
BASE="https://github.com/orioncactus/pretendard/raw/main/packages/pretendard/dist/public/static"
for w in Regular SemiBold Bold; do
  F="Pretendard-${w}.otf"
  [ -f "$F" ] || curl -sSL -o "$F" "${BASE}/${F}"
done

ls -la /tmp/og-fonts/
echo ""
echo "✅ Fonts ready at /tmp/og-fonts/"
