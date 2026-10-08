#!/bin/zsh
# 编译 Compositor（macOS 14 适配版），错误归类输出。
# 用法： ./build.sh [仓库根目录] [日志文件]
set -u
REPO=${1:-$(cd "$(dirname "$0")/.." && pwd)}
LOG=${2:-/tmp/compositor-build.log}
cd "$REPO" || exit 1
xcodebuild -project Compositor.xcodeproj -target Compositor -configuration Debug \
  SYMROOT="$REPO/build" OBJROOT="$REPO/build/obj" ONLY_ACTIVE_ARCH=YES \
  CODE_SIGNING_ALLOWED=NO "$@" build > "$LOG" 2>&1
code=$?
echo "exit=$code"
echo "--- error 数量: $(grep -c 'error:' "$LOG") ---"
grep 'error:' "$LOG" | sed 's/^\([^:]*:[0-9]*:[0-9]*\): error: /\1 | /' | sort -u | head -80
if [ $code -ne 0 ]; then tail -5 "$LOG"; fi
