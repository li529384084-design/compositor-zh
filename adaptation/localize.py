#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 Compositor 源码里的界面文案改成简体中文。

用法：
    python3 localize.py <repo_root> [--dry]

替换方式是「整条字符串字面量精确匹配」，即只把源码里与对照表 key 完全一致
的双引号内容换掉，不做子串替换，因此不会碰到文件名、标识符一类字符串。
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from translations import ZH  # noqa: E402

DRY = "--dry" in sys.argv
ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else ".")
APP = ROOT / "Compositor"

# 同形异义的词只能按文件定向替换，且必须在全局替换之前做
TARGETED = [
    # 文字对齐：Left/Right 与「裁切方向」同形，只有这里指对齐
    ("Document/TypeTool.swift", '"Left"', '"左对齐"'),
    ("Document/TypeTool.swift", '"Right"', '"右对齐"'),
    # 裁切方向
    ("UI/TrimSheet.swift", '"Left"', '"左侧"'),
    ("UI/TrimSheet.swift", '"Right"', '"右侧"'),
    # 色阶端点：与参考线预设的同名颜色区分开
    ("Document/LevelsAutomatic.swift",
     'case black = "Black", gray = "Gray", white = "White"',
     'case black = "黑场", gray = "灰场", white = "白场"'),
    # Camera Raw 的 Light 是「光线」，滤镜里的 Light 是「浅色」
    ("UI/CameraRawControls.swift", '"Light"', '"光线"'),
    ("UI/FilterSheet.swift", '"Light"', '"浅色"'),
    # 变换面板标题（避免 "Transform" 波及别处，按文件定向）
    ("UI/TransformInspector.swift", '"Transform Mask"', '"变换蒙版"'),
    ("UI/TransformInspector.swift", '"Transform"', '"变换"'),
    # 命令面板里的工具前缀是拼出来的
    ("UI/CommandPalette.swift", '"Tool › \\(name)"', '"工具 › \\(name)"'),
    # 命令面板要跳过的菜单：菜单名随系统语言变，中英都列上
    ("UI/CommandPaletteView.swift",
     'static let skipped: Set<String> = ["Command Palette…", "Window", "Help", "Services"]',
     'static let skipped: Set<String> = ["Command Palette…", "命令面板…", "Window", "窗口", "Help", "帮助", "Services", "服务"]'),
    # 新建画布的背景层名称由枚举值拼出来，改成按分支取中文
    ("UI/NewCanvasSheet.swift",
     'var title: String { "\\(rawValue.capitalized) canvas" }',
     'var title: String {\n'
     '        switch self {\n'
     '        case .transparent: "透明画布"\n'
     '        case .white: "白色画布"\n'
     '        case .black: "黑色画布"\n'
     '        }\n'
     '    }'),
]


def apply_targeted(records):
    for rel, old, new in TARGETED:
        p = APP / rel
        s = p.read_text()
        if old not in s:
            records.setdefault("!! 定向未命中 " + rel, 0)
            continue
        records["定向 " + rel] = records.get("定向 " + rel, 0) + s.count(old)
        if not DRY:
            p.write_text(s.replace(old, new))


def main():
    files = sorted(APP.rglob("*.swift"))
    hits = {}
    touched = 0

    apply_targeted(hits)

    for p in files:
        src = p.read_text()
        out = src
        for en, zh in ZH.items():
            needle = '"' + en + '"'
            n = out.count(needle)
            if n:
                hits[en] = hits.get(en, 0) + n
                out = out.replace(needle, '"' + zh + '"')
        if out != src:
            touched += 1
            if not DRY:
                p.write_text(out)

    missing = [k for k in ZH if k not in hits]
    total = sum(v for k, v in hits.items() if not k.startswith("定向"))
    print(f"全局替换命中 {total} 处，涉及 {touched} 个文件")
    print(f"对照表条目 {len(ZH)} 条，未命中 {len(missing)} 条")
    for k, v in hits.items():
        if k.startswith("定向"):
            print(f"   {k}: {v} 处")
        if k.startswith("!!"):
            print(f"   {k}")
    if missing:
        print("\n未命中（可能拼写不符）：")
        for m in sorted(missing):
            print("   ", m)



if __name__ == "__main__":
    main()
