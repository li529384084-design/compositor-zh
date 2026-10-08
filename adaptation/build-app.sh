#!/bin/zsh
# 构建「可分发给别人」的 Compositor.app：
#   - Release 配置（优化过，体积更小、跑得更快）
#   - 通用二进制（arm64 + x86_64，Apple Silicon 与 Intel 都能跑）
#   - ad-hoc 签名（无需开发者证书）
#   - 打包成 zip 放到 download/
#
# 用法： ./build-app.sh [仓库根目录]
set -u
REPO=${1:-$(cd "$(dirname "$0")/.." && pwd)}
cd "$REPO" || exit 1
LOG=/tmp/compositor-release.log

echo "==> 编译 Release（通用二进制，可能要几分钟）"
xcodebuild -project Compositor.xcodeproj -target Compositor -configuration Release \
  SYMROOT="$REPO/build" OBJROOT="$REPO/build/obj" \
  ARCHS="arm64 x86_64" ONLY_ACTIVE_ARCH=NO \
  CODE_SIGNING_ALLOWED=NO build > "$LOG" 2>&1
code=$?
echo "exit=$code  错误数=$(grep -c 'error:' "$LOG")"
if [ $code -ne 0 ]; then
  grep 'error:' "$LOG" | sed 's/^\([^:]*:[0-9]*:[0-9]*\): error: /\1 | /' | sort -u | head -40
  tail -5 "$LOG"
  exit $code
fi

APP="$REPO/build/Release/Compositor.app"
echo "==> 签名（ad-hoc）"
codesign --force --sign - --entitlements "$REPO/Config/Compositor.entitlements" \
  --options runtime --timestamp=none "$APP" || exit 1
codesign --verify --verbose=2 "$APP" 2>&1 | tail -2

echo "==> 架构检查"
lipo -info "$APP/Contents/MacOS/Compositor"

echo "==> 打包 zip"
mkdir -p "$REPO/download"
rm -f "$REPO/download/Compositor-macOS14-zh.zip"
ditto -c -k --sequesterRsrc --keepParent "$APP" "$REPO/download/Compositor-macOS14-zh.zip"
ls -lh "$REPO/download/Compositor-macOS14-zh.zip"
echo "==> 完成：$REPO/download/Compositor-macOS14-zh.zip"
